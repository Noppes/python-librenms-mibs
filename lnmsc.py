#!/usr/bin/env python3
"""
LibreNMS MIB Compiler for Python
Compiles vendor MIB folders from LibreNMS repository for use with PySNMP.

Usage:
    python mib_compiler.py /path/to/librenms/mibs/cisco --output ./compiled_mibs
    python mib_compiler.py /path/to/librenms/mibs --vendor cisco --output ./compiled_mibs
    python mib_compiler.py /path/to/librenms/mibs --all --output ./compiled_mibs
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List, Dict
import json
import logging
from datetime import datetime
import re

try:
    from pysmi.reader import FileReader
    from pysmi.searcher import StubSearcher, PyFileSearcher
    from pysmi.writer import PyFileWriter
    from pysmi.parser import SmiStarParser
    from pysmi.codegen import PySnmpCodeGen
    from pysmi.compiler import MibCompiler
    from pysmi import debug
except ImportError:
    print("ERROR: pysmi is required. Install it with: pip install pysmi")
    sys.exit(1)

class NoHeaderPySnmpCodeGen(PySnmpCodeGen):
    def gen_code(self, ast, symbolTable, **kwargs):
        comments = kwargs.get("comments", [])
        if comments:
            kwargs["comments"] = [comments[0]]
        return super().gen_code(ast, symbolTable, **kwargs)
    
class CachedFileReader(FileReader):

    def __init__(self, path, recursive=True, ignoreErrors=True):
        super().__init__(path, recursive, ignoreErrors)
        self._loading = True
        self._subdirs = self.get_subdirs(self._path, self._recursive, self._ignoreErrors)
        self._loading = False

        
    def get_subdirs(self, path, recursive=True, ignoreErrors=True):
        if self._loading:
            return super().get_subdirs(path, recursive, ignoreErrors)
        return self._subdirs

class MibCompilerTool:
    """Tool to compile MIB files from LibreNMS vendor folders."""
    MIB_NAME_PATTERN = re.compile(
        br'^\s*([A-Za-z0-9][A-Za-z0-9\-_]+)\s+DEFINITIONS\s+::=\s+BEGIN',
        re.IGNORECASE | re.MULTILINE
    )

    def __init__(self, source_dir: Path, output_dir: Path, verbose: bool = False):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.verbose = verbose
        self.stats = {
            'total': 0,
            'compiled': 0,
            'failed': 0,
            'skipped': 0,
            'errors': []
        }

        log_level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            level=log_level,
            format='%(message)s'
        )
        self.logger = logging.getLogger(__name__)
        #debug.set_logger(debug.Debug("compiler"))
        if verbose:
            try:
                debug.set_logger(debug.Debug('all'))
            except AttributeError:
                debug.setLogger(debug.Debug('all'))

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def get_mib_files(self, directory: Path) -> List[Path]:
        """Find all plausible MIB source files under a directory."""
        mib_files = []
        extensions = {'.mib', '.txt', '.my', ''}

        for file_path in directory.rglob('*'):
            if file_path.is_file():
                if file_path.suffix.lower() in extensions:
                    try:
                        mib_name = self._get_mib_name(file_path)
                        if mib_name:
                            mib_files.append(mib_name)
                        else:
                            self.logger.info(f"Skipped: {file_path.stem}")
                                    
                    except Exception as e:
                        if self.verbose:
                            self.logger.debug(f"Could not read {file_path}: {e}")
                            self.logger.exception(e)

        return sorted(mib_files)
    
    MARKER = b"DEFINITIONS ::= BEGIN"
    def _get_mib_name(self, file_path, chunk_size=8192, tries=10):
        overlap = 512
        tail = b""

        with open(file_path, "rb") as f:
            while True:
                if tries < 0:
                    break
                chunk = f.read(chunk_size)
                if not chunk:
                    return False

                data = tail + chunk

                if self.MARKER in data:
                    match = self.MIB_NAME_PATTERN.search(data)
                    if match:
                        return match.group(1).decode("ascii", errors="ignore").strip()
                    return file_path.stem

                tail = data[-overlap:]
                tries-=1
        return False

    def get_vendor_folders(self) -> List[Path]:
        """Get all vendor subdirectories."""
        vendors = []
        if not self.source_dir.exists():
            self.logger.error(f"Source directory does not exist: {self.source_dir}")
            return vendors

        for item in self.source_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                vendors.append(item)

        return sorted(vendors)

    def _build_compiler(self, search_paths: List[str]) -> MibCompiler:
        """Instantiate and configure a MibCompiler instance."""
        mib_compiler = MibCompiler(
            SmiStarParser(),
            NoHeaderPySnmpCodeGen(),
            PyFileWriter(str(self.output_dir))
        )
        
        if self.verbose:
            self.logger.debug(f"Search paths: {search_paths[:3]}...")

        for path in search_paths:
            mib_compiler.add_sources(CachedFileReader(path))
            

        mib_compiler.add_searchers(PyFileSearcher(str(self.output_dir)))
        mib_compiler.add_searchers(StubSearcher(*PySnmpCodeGen.baseMibs))

        return mib_compiler

    def compile_folder(self, folder: Path, vendor_name: str = None) -> Dict:
        """Compile all MIBs in a folder."""
        if vendor_name is None:
            vendor_name = folder.name

        print(f"\n{'=' * 70}")
        print(f"Compiling: {vendor_name}")
        print(f"Source: {folder}")
        print(f"{'=' * 70}\n")

        mib_files = self.get_mib_files(folder)

        if not mib_files:
            self.logger.warning(f"No MIB files found in {folder}")
            return self.stats

        print(f"Found {len(mib_files)} MIB files\n")
        self.stats['total'] += len(mib_files)

        # Build search paths - always include parent if we're in a subdirectory
        search_paths = [str(folder)]

        # Check if this folder is a subdirectory of a larger mibs collection
        parent = folder.parent
        if parent.exists() and parent != folder:
            # Add parent directory first (for base MIBs)
            search_paths.insert(0, str(parent))

            # Add sibling directories (for cross-vendor dependencies)
            for sibling in parent.iterdir():
                sibling_str = str(sibling)
                if sibling.is_dir() and sibling != folder and not sibling.name.startswith('.'):
                    search_paths.append(sibling_str)

        compiler = self._build_compiler(search_paths)

        # Compile each MIB individually
        for idx, mib_name in enumerate(mib_files, 1):
            prefix = f"[{idx}/{len(mib_files)}]"

            try:
                results = compiler.compile(mib_name)
                status = results.get(mib_name, 'unknown')

                if status == 'compiled':
                    print(f"{prefix} ✓ {mib_name}")
                    self.stats['compiled'] += 1
                elif status == 'untouched':
                    print(f"{prefix} - {mib_name} (already exists)")
                    self.stats['skipped'] += 1
                else:
                    print(f"{prefix} ✗ {mib_name}: {status}")
                    self.stats['failed'] += 1
                    self.stats['errors'].append({'mib': mib_name, 'error': status})
            except Exception as e:
                error_msg = str(e)[:100]
                print(f"{prefix} ✗ {mib_name}: {error_msg}")
                self.stats['failed'] += 1
                self.stats['errors'].append({'mib': mib_name, 'error': str(e)})

        return self.stats

    def compile_all_vendors(self) -> Dict:
        """Compile all vendor folders."""
        vendors = self.get_vendor_folders()

        if not vendors:
            self.logger.error(f"No vendor folders found in {self.source_dir}")
            return self.stats

        print(f"\nFound {len(vendors)} vendor folders\n")

        for vendor in vendors:
            self.compile_folder(vendor, vendor.name)

        return self.stats

    def print_summary(self):
        """Print final compilation summary."""
        print(f"\n{'=' * 70}")
        print("COMPILATION SUMMARY")
        print(f"{'=' * 70}")
        print(f"Total MIBs:      {self.stats['total']}")
        print(f"Compiled:        {self.stats['compiled']}")
        print(f"Already existed: {self.stats['skipped']}")
        print(f"Failed:          {self.stats['failed']}")
        print(f"Output:          {self.output_dir.absolute()}")

        if self.stats['errors']:
            print(f"\n{'=' * 70}")
            print("ERRORS (first 20):")
            print(f"{'=' * 70}")
            for error in self.stats['errors'][:20]:
                print(f"  {error['mib']}: {error['error']}")

            remaining = len(self.stats['errors']) - 20
            if remaining > 0:
                print(f"  ... and {remaining} more errors")

        report_file = self.output_dir / 'compilation_report.json'
        try:
            with open(report_file, 'w') as f:
                json.dump({
                    'timestamp': datetime.now().isoformat(),
                    'stats': self.stats,
                    'output_dir': str(self.output_dir.absolute())
                }, f, indent=2)
            print(f"\nDetailed report: {report_file}")
        except Exception as e:
            self.logger.error(f"Failed to write report: {e}")

class MibCompilerRunner:
    @staticmethod
    def start(source, output, vendor, all=False, verbose=False):
        source_path = Path(source)
        if not source_path.exists():
            print(f"ERROR: Source path does not exist: {source_path}")
            return 1

        output_path = Path(output)
        compiler = MibCompilerTool(source_path, output_path, verbose)

        try:
            if all:
                compiler.compile_all_vendors()
            elif vendor:
                vendor_path = source_path / vendor
                if not vendor_path.exists():
                    print(f"ERROR: Vendor folder does not exist: {vendor_path}")
                    return 1
                compiler.compile_folder(vendor_path, vendor)
            else:
                if source_path.is_dir():
                    compiler.compile_folder(source_path)
                else:
                    print("ERROR: Source must be a directory")
                    return 1

            compiler.print_summary()

            if compiler.stats['failed'] > 0:
                return 1

        except KeyboardInterrupt:
            print("\n\nInterrupted by user")
            compiler.print_summary()
            return 130
        except Exception as e:
            print(f"\nERROR: {e}")
            if verbose:
                import traceback
                traceback.print_exc()
            return 1
        return 0

def main():
    parser = argparse.ArgumentParser(
        description='Compile LibreNMS MIBs for use with PySNMP',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Compile a specific vendor folder
  %(prog)s /path/to/librenms/mibs/cisco -o ./compiled_mibs

  # Compile all vendors
  %(prog)s /path/to/librenms/mibs --all -o ./compiled_mibs

  # Compile with verbose output
  %(prog)s /path/to/librenms/mibs/cisco -o ./compiled_mibs -v
        """
    )

    parser.add_argument('source', type=str, help='Path to LibreNMS mibs directory or specific vendor folder')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output directory for compiled MIBs')
    parser.add_argument('--all', action='store_true', help='Compile all vendor folders')
    parser.add_argument('--vendor', type=str, help='Specific vendor folder name')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')

    args = parser.parse_args()

    result = MibCompilerRunner.start(args.source, args.output, args.vendor, args.all, args.verbose)
    if result:
        sys.exit(result)


if __name__ == '__main__':
    main()