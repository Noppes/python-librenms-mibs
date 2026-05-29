# SNMP MIB module (STORMSHIELD-SYSTEM-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-SYSTEM-MONITOR-MIB

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsSystemMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10)
)
if mibBuilder.loadTexts:
    snsSystemMonitor.setRevisions(
        ("2025-04-10 00:00",
         "2022-06-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SnsDate_Type(DisplayString):
    """Custom type snsDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsDate_Type.__name__ = "DisplayString"
_SnsDate_Object = MibScalar
snsDate = _SnsDate_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 1),
    _SnsDate_Type()
)
snsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsDate.setStatus("current")


class _SnsUptime_Type(DisplayString):
    """Custom type snsUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsUptime_Type.__name__ = "DisplayString"
_SnsUptime_Object = MibScalar
snsUptime = _SnsUptime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 2),
    _SnsUptime_Type()
)
snsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsUptime.setStatus("current")


class _SnsMem_Type(DisplayString):
    """Custom type snsMem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsMem_Type.__name__ = "DisplayString"
_SnsMem_Object = MibScalar
snsMem = _SnsMem_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 3),
    _SnsMem_Type()
)
snsMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMem.setStatus("current")


class _SnsStartTime_Type(DisplayString):
    """Custom type snsStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsStartTime_Type.__name__ = "DisplayString"
_SnsStartTime_Object = MibScalar
snsStartTime = _SnsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 4),
    _SnsStartTime_Type()
)
snsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsStartTime.setStatus("current")
_SnsDiskTable_Object = MibTable
snsDiskTable = _SnsDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 5)
)
if mibBuilder.loadTexts:
    snsDiskTable.setStatus("current")
_SnsDiskEntry_Object = MibTableRow
snsDiskEntry = _SnsDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1)
)
snsDiskEntry.setIndexNames(
    (0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsDiskEntryIndex"),
)
if mibBuilder.loadTexts:
    snsDiskEntry.setStatus("current")


class _SnsDiskEntryIndex_Type(Integer32):
    """Custom type snsDiskEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsDiskEntryIndex_Type.__name__ = "Integer32"
_SnsDiskEntryIndex_Object = MibTableColumn
snsDiskEntryIndex = _SnsDiskEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 1),
    _SnsDiskEntryIndex_Type()
)
snsDiskEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsDiskEntryIndex.setStatus("current")
_SnsDiskEntryDiskName_Type = DisplayString
_SnsDiskEntryDiskName_Object = MibTableColumn
snsDiskEntryDiskName = _SnsDiskEntryDiskName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 2),
    _SnsDiskEntryDiskName_Type()
)
snsDiskEntryDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsDiskEntryDiskName.setStatus("current")
_SnsDiskEntrySmartResult_Type = DisplayString
_SnsDiskEntrySmartResult_Object = MibTableColumn
snsDiskEntrySmartResult = _SnsDiskEntrySmartResult_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 3),
    _SnsDiskEntrySmartResult_Type()
)
snsDiskEntrySmartResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsDiskEntrySmartResult.setStatus("current")


class _SnsDiskEntryIsRaid_Type(Integer32):
    """Custom type snsDiskEntryIsRaid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SnsDiskEntryIsRaid_Type.__name__ = "Integer32"
_SnsDiskEntryIsRaid_Object = MibTableColumn
snsDiskEntryIsRaid = _SnsDiskEntryIsRaid_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 4),
    _SnsDiskEntryIsRaid_Type()
)
snsDiskEntryIsRaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsDiskEntryIsRaid.setStatus("current")
_SnsDiskEntryRaidStatus_Type = DisplayString
_SnsDiskEntryRaidStatus_Object = MibTableColumn
snsDiskEntryRaidStatus = _SnsDiskEntryRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 5),
    _SnsDiskEntryRaidStatus_Type()
)
snsDiskEntryRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsDiskEntryRaidStatus.setStatus("current")
_SnsDiskEntryPosition_Type = DisplayString
_SnsDiskEntryPosition_Object = MibTableColumn
snsDiskEntryPosition = _SnsDiskEntryPosition_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 6),
    _SnsDiskEntryPosition_Type()
)
snsDiskEntryPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsDiskEntryPosition.setStatus("current")
_SnsPowerSupplyTable_Object = MibTable
snsPowerSupplyTable = _SnsPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 6)
)
if mibBuilder.loadTexts:
    snsPowerSupplyTable.setStatus("current")
_SnsPowerSupplyEntry_Object = MibTableRow
snsPowerSupplyEntry = _SnsPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1)
)
snsPowerSupplyEntry.setIndexNames(
    (0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    snsPowerSupplyEntry.setStatus("current")


class _SnsPowerSupplyIndex_Type(Integer32):
    """Custom type snsPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsPowerSupplyIndex_Type.__name__ = "Integer32"
_SnsPowerSupplyIndex_Object = MibTableColumn
snsPowerSupplyIndex = _SnsPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1, 1),
    _SnsPowerSupplyIndex_Type()
)
snsPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsPowerSupplyIndex.setStatus("current")
_SnsPowerSupplyPowered_Type = TruthValue
_SnsPowerSupplyPowered_Object = MibTableColumn
snsPowerSupplyPowered = _SnsPowerSupplyPowered_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1, 2),
    _SnsPowerSupplyPowered_Type()
)
snsPowerSupplyPowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPowerSupplyPowered.setStatus("current")
_SnsPowerSupplyStatus_Type = DisplayString
_SnsPowerSupplyStatus_Object = MibTableColumn
snsPowerSupplyStatus = _SnsPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1, 3),
    _SnsPowerSupplyStatus_Type()
)
snsPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPowerSupplyStatus.setStatus("current")
_SnsCpuTable_Object = MibTable
snsCpuTable = _SnsCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 7)
)
if mibBuilder.loadTexts:
    snsCpuTable.setStatus("current")
_SnsCpuEntry_Object = MibTableRow
snsCpuEntry = _SnsCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 7, 1)
)
snsCpuEntry.setIndexNames(
    (0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsCpuIndex"),
)
if mibBuilder.loadTexts:
    snsCpuEntry.setStatus("current")


class _SnsCpuIndex_Type(Integer32):
    """Custom type snsCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsCpuIndex_Type.__name__ = "Integer32"
_SnsCpuIndex_Object = MibTableColumn
snsCpuIndex = _SnsCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 7, 1, 1),
    _SnsCpuIndex_Type()
)
snsCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsCpuIndex.setStatus("current")
_SnsCpuTemp_Type = Integer32
_SnsCpuTemp_Object = MibTableColumn
snsCpuTemp = _SnsCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 7, 1, 2),
    _SnsCpuTemp_Type()
)
snsCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsCpuTemp.setStatus("current")
_SnsBypassTable_Object = MibTable
snsBypassTable = _SnsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 8)
)
if mibBuilder.loadTexts:
    snsBypassTable.setStatus("current")
_SnsBypassEntry_Object = MibTableRow
snsBypassEntry = _SnsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1)
)
snsBypassEntry.setIndexNames(
    (0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsBypassIndex"),
)
if mibBuilder.loadTexts:
    snsBypassEntry.setStatus("current")


class _SnsBypassIndex_Type(Integer32):
    """Custom type snsBypassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsBypassIndex_Type.__name__ = "Integer32"
_SnsBypassIndex_Object = MibTableColumn
snsBypassIndex = _SnsBypassIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 1),
    _SnsBypassIndex_Type()
)
snsBypassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsBypassIndex.setStatus("current")


class _SnsBypassI2CAddress_Type(Unsigned32):
    """Custom type snsBypassI2CAddress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SnsBypassI2CAddress_Type.__name__ = "Unsigned32"
_SnsBypassI2CAddress_Object = MibTableColumn
snsBypassI2CAddress = _SnsBypassI2CAddress_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 2),
    _SnsBypassI2CAddress_Type()
)
snsBypassI2CAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsBypassI2CAddress.setStatus("current")
_SnsBypassSystemOff_Type = TruthValue
_SnsBypassSystemOff_Object = MibTableColumn
snsBypassSystemOff = _SnsBypassSystemOff_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 3),
    _SnsBypassSystemOff_Type()
)
snsBypassSystemOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsBypassSystemOff.setStatus("current")
_SnsBypassJustOn_Type = TruthValue
_SnsBypassJustOn_Object = MibTableColumn
snsBypassJustOn = _SnsBypassJustOn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 4),
    _SnsBypassJustOn_Type()
)
snsBypassJustOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsBypassJustOn.setStatus("current")
_SnsBypassRunTime_Type = TruthValue
_SnsBypassRunTime_Object = MibTableColumn
snsBypassRunTime = _SnsBypassRunTime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 5),
    _SnsBypassRunTime_Type()
)
snsBypassRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsBypassRunTime.setStatus("current")
_SnsBypassWatchdog_Type = DisplayString
_SnsBypassWatchdog_Object = MibTableColumn
snsBypassWatchdog = _SnsBypassWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 6),
    _SnsBypassWatchdog_Type()
)
snsBypassWatchdog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsBypassWatchdog.setStatus("current")
_SnsFanTable_Object = MibTable
snsFanTable = _SnsFanTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 9)
)
if mibBuilder.loadTexts:
    snsFanTable.setStatus("current")
_SnsFanEntry_Object = MibTableRow
snsFanEntry = _SnsFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 9, 1)
)
snsFanEntry.setIndexNames(
    (0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsFanIndex"),
)
if mibBuilder.loadTexts:
    snsFanEntry.setStatus("current")


class _SnsFanIndex_Type(Integer32):
    """Custom type snsFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsFanIndex_Type.__name__ = "Integer32"
_SnsFanIndex_Object = MibTableColumn
snsFanIndex = _SnsFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 9, 1, 1),
    _SnsFanIndex_Type()
)
snsFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsFanIndex.setStatus("current")
_SnsFanName_Type = DisplayString
_SnsFanName_Object = MibTableColumn
snsFanName = _SnsFanName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 9, 1, 2),
    _SnsFanName_Type()
)
snsFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsFanName.setStatus("current")
_SnsFanStatus_Type = DisplayString
_SnsFanStatus_Object = MibTableColumn
snsFanStatus = _SnsFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 9, 1, 3),
    _SnsFanStatus_Type()
)
snsFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsFanStatus.setStatus("current")


class _SnsFanRpm_Type(Unsigned32):
    """Custom type snsFanRpm based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SnsFanRpm_Type.__name__ = "Unsigned32"
_SnsFanRpm_Object = MibTableColumn
snsFanRpm = _SnsFanRpm_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 9, 1, 4),
    _SnsFanRpm_Type()
)
snsFanRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsFanRpm.setStatus("current")
_SnsMemUsageTable_Object = MibTable
snsMemUsageTable = _SnsMemUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10)
)
if mibBuilder.loadTexts:
    snsMemUsageTable.setStatus("current")
_SnsMemUsageEntry_Object = MibTableRow
snsMemUsageEntry = _SnsMemUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1)
)
snsMemUsageEntry.setIndexNames(
    (0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsMemUsageIndex"),
)
if mibBuilder.loadTexts:
    snsMemUsageEntry.setStatus("current")


class _SnsMemUsageIndex_Type(Integer32):
    """Custom type snsMemUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsMemUsageIndex_Type.__name__ = "Integer32"
_SnsMemUsageIndex_Object = MibTableColumn
snsMemUsageIndex = _SnsMemUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 1),
    _SnsMemUsageIndex_Type()
)
snsMemUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsMemUsageIndex.setStatus("current")
_SnsMemHost_Type = Integer32
_SnsMemHost_Object = MibTableColumn
snsMemHost = _SnsMemHost_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 2),
    _SnsMemHost_Type()
)
snsMemHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemHost.setStatus("current")
if mibBuilder.loadTexts:
    snsMemHost.setUnits("%")
_SnsMemFrag_Type = Integer32
_SnsMemFrag_Object = MibTableColumn
snsMemFrag = _SnsMemFrag_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 3),
    _SnsMemFrag_Type()
)
snsMemFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemFrag.setStatus("current")
if mibBuilder.loadTexts:
    snsMemFrag.setUnits("%")
_SnsMemIcmp_Type = Integer32
_SnsMemIcmp_Object = MibTableColumn
snsMemIcmp = _SnsMemIcmp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 4),
    _SnsMemIcmp_Type()
)
snsMemIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemIcmp.setStatus("current")
if mibBuilder.loadTexts:
    snsMemIcmp.setUnits("%")
_SnsMemConn_Type = Integer32
_SnsMemConn_Object = MibTableColumn
snsMemConn = _SnsMemConn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 5),
    _SnsMemConn_Type()
)
snsMemConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemConn.setStatus("current")
if mibBuilder.loadTexts:
    snsMemConn.setUnits("%")
_SnsMemEther_Type = Integer32
_SnsMemEther_Object = MibTableColumn
snsMemEther = _SnsMemEther_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 6),
    _SnsMemEther_Type()
)
snsMemEther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemEther.setStatus("current")
if mibBuilder.loadTexts:
    snsMemEther.setUnits("%")
_SnsMemDataTrack_Type = Integer32
_SnsMemDataTrack_Object = MibTableColumn
snsMemDataTrack = _SnsMemDataTrack_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 7),
    _SnsMemDataTrack_Type()
)
snsMemDataTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemDataTrack.setStatus("current")
if mibBuilder.loadTexts:
    snsMemDataTrack.setUnits("%")
_SnsMemSystem_Type = Integer32
_SnsMemSystem_Object = MibTableColumn
snsMemSystem = _SnsMemSystem_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 8),
    _SnsMemSystem_Type()
)
snsMemSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemSystem.setStatus("current")
if mibBuilder.loadTexts:
    snsMemSystem.setUnits("%")
_SnsMemUser_Type = Integer32
_SnsMemUser_Object = MibTableColumn
snsMemUser = _SnsMemUser_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 9),
    _SnsMemUser_Type()
)
snsMemUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemUser.setStatus("current")
if mibBuilder.loadTexts:
    snsMemUser.setUnits("%")
_SnsMemMbuf_Type = Integer32
_SnsMemMbuf_Object = MibTableColumn
snsMemMbuf = _SnsMemMbuf_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 10, 10, 1, 10),
    _SnsMemMbuf_Type()
)
snsMemMbuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemMbuf.setStatus("current")
if mibBuilder.loadTexts:
    snsMemMbuf.setUnits("%")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-SYSTEM-MONITOR-MIB",
    **{"snsSystemMonitor": snsSystemMonitor,
       "snsDate": snsDate,
       "snsUptime": snsUptime,
       "snsMem": snsMem,
       "snsStartTime": snsStartTime,
       "snsDiskTable": snsDiskTable,
       "snsDiskEntry": snsDiskEntry,
       "snsDiskEntryIndex": snsDiskEntryIndex,
       "snsDiskEntryDiskName": snsDiskEntryDiskName,
       "snsDiskEntrySmartResult": snsDiskEntrySmartResult,
       "snsDiskEntryIsRaid": snsDiskEntryIsRaid,
       "snsDiskEntryRaidStatus": snsDiskEntryRaidStatus,
       "snsDiskEntryPosition": snsDiskEntryPosition,
       "snsPowerSupplyTable": snsPowerSupplyTable,
       "snsPowerSupplyEntry": snsPowerSupplyEntry,
       "snsPowerSupplyIndex": snsPowerSupplyIndex,
       "snsPowerSupplyPowered": snsPowerSupplyPowered,
       "snsPowerSupplyStatus": snsPowerSupplyStatus,
       "snsCpuTable": snsCpuTable,
       "snsCpuEntry": snsCpuEntry,
       "snsCpuIndex": snsCpuIndex,
       "snsCpuTemp": snsCpuTemp,
       "snsBypassTable": snsBypassTable,
       "snsBypassEntry": snsBypassEntry,
       "snsBypassIndex": snsBypassIndex,
       "snsBypassI2CAddress": snsBypassI2CAddress,
       "snsBypassSystemOff": snsBypassSystemOff,
       "snsBypassJustOn": snsBypassJustOn,
       "snsBypassRunTime": snsBypassRunTime,
       "snsBypassWatchdog": snsBypassWatchdog,
       "snsFanTable": snsFanTable,
       "snsFanEntry": snsFanEntry,
       "snsFanIndex": snsFanIndex,
       "snsFanName": snsFanName,
       "snsFanStatus": snsFanStatus,
       "snsFanRpm": snsFanRpm,
       "snsMemUsageTable": snsMemUsageTable,
       "snsMemUsageEntry": snsMemUsageEntry,
       "snsMemUsageIndex": snsMemUsageIndex,
       "snsMemHost": snsMemHost,
       "snsMemFrag": snsMemFrag,
       "snsMemIcmp": snsMemIcmp,
       "snsMemConn": snsMemConn,
       "snsMemEther": snsMemEther,
       "snsMemDataTrack": snsMemDataTrack,
       "snsMemSystem": snsMemSystem,
       "snsMemUser": snsMemUser,
       "snsMemMbuf": snsMemMbuf}
)
