# SNMP MIB module (TELDAT-MON-CommonInfo-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teldat\TELDAT-MON-CommonInfo-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(telProdNpMonInterfRouter,
 telProdNpMonInterface,
 telProdNpMonitSistema) = mibBuilder.importSymbols(
    "TELDAT-SW-STRUCTURE-MIB",
    "telProdNpMonInterfRouter",
    "telProdNpMonInterface",
    "telProdNpMonitSistema")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TelProdNpMonSistemMemory_ObjectIdentity = ObjectIdentity
telProdNpMonSistemMemory = _TelProdNpMonSistemMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1)
)
_TelProdNpMonSistemMemSize_Type = Integer32
_TelProdNpMonSistemMemSize_Object = MibScalar
telProdNpMonSistemMemSize = _TelProdNpMonSistemMemSize_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 1),
    _TelProdNpMonSistemMemSize_Type()
)
telProdNpMonSistemMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemSize.setStatus("obsolete")
_TelProdNpMonSistemMemAvailable_Type = Integer32
_TelProdNpMonSistemMemAvailable_Object = MibScalar
telProdNpMonSistemMemAvailable = _TelProdNpMonSistemMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 2),
    _TelProdNpMonSistemMemAvailable_Type()
)
telProdNpMonSistemMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemAvailable.setStatus("obsolete")
_TelProdNpMonSistemMemPooldissize_Type = Integer32
_TelProdNpMonSistemMemPooldissize_Object = MibScalar
telProdNpMonSistemMemPooldissize = _TelProdNpMonSistemMemPooldissize_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 3),
    _TelProdNpMonSistemMemPooldissize_Type()
)
telProdNpMonSistemMemPooldissize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPooldissize.setStatus("obsolete")
_TelProdNpMonSistemMemPooldisavailable_Type = Integer32
_TelProdNpMonSistemMemPooldisavailable_Object = MibScalar
telProdNpMonSistemMemPooldisavailable = _TelProdNpMonSistemMemPooldisavailable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 4),
    _TelProdNpMonSistemMemPooldisavailable_Type()
)
telProdNpMonSistemMemPooldisavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPooldisavailable.setStatus("obsolete")
_TelProdNpMonSistemMemPoolmdissize_Type = Integer32
_TelProdNpMonSistemMemPoolmdissize_Object = MibScalar
telProdNpMonSistemMemPoolmdissize = _TelProdNpMonSistemMemPoolmdissize_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 5),
    _TelProdNpMonSistemMemPoolmdissize_Type()
)
telProdNpMonSistemMemPoolmdissize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPoolmdissize.setStatus("obsolete")
_TelProdNpMonSistemMemPoolmdisavailable_Type = Integer32
_TelProdNpMonSistemMemPoolmdisavailable_Object = MibScalar
telProdNpMonSistemMemPoolmdisavailable = _TelProdNpMonSistemMemPoolmdisavailable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 6),
    _TelProdNpMonSistemMemPoolmdisavailable_Type()
)
telProdNpMonSistemMemPoolmdisavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPoolmdisavailable.setStatus("obsolete")
_TelProdNpMonSistemMemPooltsize_Type = Integer32
_TelProdNpMonSistemMemPooltsize_Object = MibScalar
telProdNpMonSistemMemPooltsize = _TelProdNpMonSistemMemPooltsize_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 7),
    _TelProdNpMonSistemMemPooltsize_Type()
)
telProdNpMonSistemMemPooltsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPooltsize.setStatus("obsolete")
_TelProdNpMonSistemMemPooltavailable_Type = Integer32
_TelProdNpMonSistemMemPooltavailable_Object = MibScalar
telProdNpMonSistemMemPooltavailable = _TelProdNpMonSistemMemPooltavailable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 8),
    _TelProdNpMonSistemMemPooltavailable_Type()
)
telProdNpMonSistemMemPooltavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPooltavailable.setStatus("obsolete")
_TelProdNpMonSistemMemPoolpsize_Type = Integer32
_TelProdNpMonSistemMemPoolpsize_Object = MibScalar
telProdNpMonSistemMemPoolpsize = _TelProdNpMonSistemMemPoolpsize_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 9),
    _TelProdNpMonSistemMemPoolpsize_Type()
)
telProdNpMonSistemMemPoolpsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPoolpsize.setStatus("obsolete")
_TelProdNpMonSistemMemPoolpavailable_Type = Integer32
_TelProdNpMonSistemMemPoolpavailable_Object = MibScalar
telProdNpMonSistemMemPoolpavailable = _TelProdNpMonSistemMemPoolpavailable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 10),
    _TelProdNpMonSistemMemPoolpavailable_Type()
)
telProdNpMonSistemMemPoolpavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPoolpavailable.setStatus("obsolete")
_TelProdNpMonSistemMemPool0size_Type = Integer32
_TelProdNpMonSistemMemPool0size_Object = MibScalar
telProdNpMonSistemMemPool0size = _TelProdNpMonSistemMemPool0size_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 11),
    _TelProdNpMonSistemMemPool0size_Type()
)
telProdNpMonSistemMemPool0size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPool0size.setStatus("obsolete")
_TelProdNpMonSistemMemPool0restpart_Type = Integer32
_TelProdNpMonSistemMemPool0restpart_Object = MibScalar
telProdNpMonSistemMemPool0restpart = _TelProdNpMonSistemMemPool0restpart_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 12),
    _TelProdNpMonSistemMemPool0restpart_Type()
)
telProdNpMonSistemMemPool0restpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPool0restpart.setStatus("obsolete")
_TelProdNpMonSistemMemPool0available_Type = Integer32
_TelProdNpMonSistemMemPool0available_Object = MibScalar
telProdNpMonSistemMemPool0available = _TelProdNpMonSistemMemPool0available_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 13),
    _TelProdNpMonSistemMemPool0available_Type()
)
telProdNpMonSistemMemPool0available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPool0available.setStatus("obsolete")
_TelProdNpMonSistemMemPool1size_Type = Integer32
_TelProdNpMonSistemMemPool1size_Object = MibScalar
telProdNpMonSistemMemPool1size = _TelProdNpMonSistemMemPool1size_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 14),
    _TelProdNpMonSistemMemPool1size_Type()
)
telProdNpMonSistemMemPool1size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPool1size.setStatus("mandatory")
_TelProdNpMonSistemMemPool1restpart_Type = Integer32
_TelProdNpMonSistemMemPool1restpart_Object = MibScalar
telProdNpMonSistemMemPool1restpart = _TelProdNpMonSistemMemPool1restpart_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 15),
    _TelProdNpMonSistemMemPool1restpart_Type()
)
telProdNpMonSistemMemPool1restpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPool1restpart.setStatus("mandatory")
_TelProdNpMonSistemMemPool1available_Type = Integer32
_TelProdNpMonSistemMemPool1available_Object = MibScalar
telProdNpMonSistemMemPool1available = _TelProdNpMonSistemMemPool1available_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 16),
    _TelProdNpMonSistemMemPool1available_Type()
)
telProdNpMonSistemMemPool1available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPool1available.setStatus("mandatory")
_TelProdNpMonSistemMemPool2size_Type = Integer32
_TelProdNpMonSistemMemPool2size_Object = MibScalar
telProdNpMonSistemMemPool2size = _TelProdNpMonSistemMemPool2size_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 17),
    _TelProdNpMonSistemMemPool2size_Type()
)
telProdNpMonSistemMemPool2size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPool2size.setStatus("obsolete")
_TelProdNpMonSistemMemPool2restpart_Type = Integer32
_TelProdNpMonSistemMemPool2restpart_Object = MibScalar
telProdNpMonSistemMemPool2restpart = _TelProdNpMonSistemMemPool2restpart_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 18),
    _TelProdNpMonSistemMemPool2restpart_Type()
)
telProdNpMonSistemMemPool2restpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPool2restpart.setStatus("obsolete")
_TelProdNpMonSistemMemPool2available_Type = Integer32
_TelProdNpMonSistemMemPool2available_Object = MibScalar
telProdNpMonSistemMemPool2available = _TelProdNpMonSistemMemPool2available_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 19),
    _TelProdNpMonSistemMemPool2available_Type()
)
telProdNpMonSistemMemPool2available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPool2available.setStatus("obsolete")
_TelProdNpMonSistemMemPoolisize_Type = Integer32
_TelProdNpMonSistemMemPoolisize_Object = MibScalar
telProdNpMonSistemMemPoolisize = _TelProdNpMonSistemMemPoolisize_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 20),
    _TelProdNpMonSistemMemPoolisize_Type()
)
telProdNpMonSistemMemPoolisize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPoolisize.setStatus("obsolete")
_TelProdNpMonSistemMemPoolirestpart_Type = Integer32
_TelProdNpMonSistemMemPoolirestpart_Object = MibScalar
telProdNpMonSistemMemPoolirestpart = _TelProdNpMonSistemMemPoolirestpart_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 21),
    _TelProdNpMonSistemMemPoolirestpart_Type()
)
telProdNpMonSistemMemPoolirestpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPoolirestpart.setStatus("obsolete")
_TelProdNpMonSistemMemPooliavailable_Type = Integer32
_TelProdNpMonSistemMemPooliavailable_Object = MibScalar
telProdNpMonSistemMemPooliavailable = _TelProdNpMonSistemMemPooliavailable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 22),
    _TelProdNpMonSistemMemPooliavailable_Type()
)
telProdNpMonSistemMemPooliavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPooliavailable.setStatus("obsolete")
_TelProdNpMonSistemMemPooldlssize_Type = Integer32
_TelProdNpMonSistemMemPooldlssize_Object = MibScalar
telProdNpMonSistemMemPooldlssize = _TelProdNpMonSistemMemPooldlssize_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 23),
    _TelProdNpMonSistemMemPooldlssize_Type()
)
telProdNpMonSistemMemPooldlssize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPooldlssize.setStatus("obsolete")
_TelProdNpMonSistemMemPooldlsrestpart_Type = Integer32
_TelProdNpMonSistemMemPooldlsrestpart_Object = MibScalar
telProdNpMonSistemMemPooldlsrestpart = _TelProdNpMonSistemMemPooldlsrestpart_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 24),
    _TelProdNpMonSistemMemPooldlsrestpart_Type()
)
telProdNpMonSistemMemPooldlsrestpart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPooldlsrestpart.setStatus("obsolete")
_TelProdNpMonSistemMemPooldlsavailable_Type = Integer32
_TelProdNpMonSistemMemPooldlsavailable_Object = MibScalar
telProdNpMonSistemMemPooldlsavailable = _TelProdNpMonSistemMemPooldlsavailable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 25),
    _TelProdNpMonSistemMemPooldlsavailable_Type()
)
telProdNpMonSistemMemPooldlsavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemPooldlsavailable.setStatus("obsolete")
_TelProdNpMonSistemMemTotal_Type = Integer32
_TelProdNpMonSistemMemTotal_Object = MibScalar
telProdNpMonSistemMemTotal = _TelProdNpMonSistemMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 26),
    _TelProdNpMonSistemMemTotal_Type()
)
telProdNpMonSistemMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemTotal.setStatus("mandatory")
_TelProdNpMonSistemMemTotalcache_Type = Integer32
_TelProdNpMonSistemMemTotalcache_Object = MibScalar
telProdNpMonSistemMemTotalcache = _TelProdNpMonSistemMemTotalcache_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 27),
    _TelProdNpMonSistemMemTotalcache_Type()
)
telProdNpMonSistemMemTotalcache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemTotalcache.setStatus("mandatory")
_TelProdNpMonSistemMemFreecache_Type = Integer32
_TelProdNpMonSistemMemFreecache_Object = MibScalar
telProdNpMonSistemMemFreecache = _TelProdNpMonSistemMemFreecache_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 28),
    _TelProdNpMonSistemMemFreecache_Type()
)
telProdNpMonSistemMemFreecache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemFreecache.setStatus("mandatory")
_TelProdNpMonSistemMemTotalnoncache_Type = Integer32
_TelProdNpMonSistemMemTotalnoncache_Object = MibScalar
telProdNpMonSistemMemTotalnoncache = _TelProdNpMonSistemMemTotalnoncache_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 29),
    _TelProdNpMonSistemMemTotalnoncache_Type()
)
telProdNpMonSistemMemTotalnoncache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemTotalnoncache.setStatus("mandatory")
_TelProdNpMonSistemMemFreenoncache_Type = Integer32
_TelProdNpMonSistemMemFreenoncache_Object = MibScalar
telProdNpMonSistemMemFreenoncache = _TelProdNpMonSistemMemFreenoncache_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 30),
    _TelProdNpMonSistemMemFreenoncache_Type()
)
telProdNpMonSistemMemFreenoncache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemFreenoncache.setStatus("mandatory")


class _TelProdNpMonSistemMemCaches_Type(DisplayString):
    """Custom type telProdNpMonSistemMemCaches based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )
    fixed_length = 30


_TelProdNpMonSistemMemCaches_Type.__name__ = "DisplayString"
_TelProdNpMonSistemMemCaches_Object = MibScalar
telProdNpMonSistemMemCaches = _TelProdNpMonSistemMemCaches_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 31),
    _TelProdNpMonSistemMemCaches_Type()
)
telProdNpMonSistemMemCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemCaches.setStatus("mandatory")
_TelProdNpMonSistemMemFlash_Type = Integer32
_TelProdNpMonSistemMemFlash_Object = MibScalar
telProdNpMonSistemMemFlash = _TelProdNpMonSistemMemFlash_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 32),
    _TelProdNpMonSistemMemFlash_Type()
)
telProdNpMonSistemMemFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemFlash.setStatus("mandatory")
_TelProdNpMonSistemMemFreeglobbuffer_Type = Integer32
_TelProdNpMonSistemMemFreeglobbuffer_Object = MibScalar
telProdNpMonSistemMemFreeglobbuffer = _TelProdNpMonSistemMemFreeglobbuffer_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 33),
    _TelProdNpMonSistemMemFreeglobbuffer_Type()
)
telProdNpMonSistemMemFreeglobbuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemFreeglobbuffer.setStatus("mandatory")
_TelProdNpMonSistemMemHeap_Type = Integer32
_TelProdNpMonSistemMemHeap_Object = MibScalar
telProdNpMonSistemMemHeap = _TelProdNpMonSistemMemHeap_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 34),
    _TelProdNpMonSistemMemHeap_Type()
)
telProdNpMonSistemMemHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemHeap.setStatus("obsolete")
_TelProdNpMonSistemMemIcused_Type = Integer32
_TelProdNpMonSistemMemIcused_Object = MibScalar
telProdNpMonSistemMemIcused = _TelProdNpMonSistemMemIcused_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 35),
    _TelProdNpMonSistemMemIcused_Type()
)
telProdNpMonSistemMemIcused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemIcused.setStatus("obsolete")
_TelProdNpMonSistemMemIcindex_Type = Integer32
_TelProdNpMonSistemMemIcindex_Object = MibScalar
telProdNpMonSistemMemIcindex = _TelProdNpMonSistemMemIcindex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 36),
    _TelProdNpMonSistemMemIcindex_Type()
)
telProdNpMonSistemMemIcindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemIcindex.setStatus("obsolete")
_TelProdNpMonSistemMemTc_Type = Integer32
_TelProdNpMonSistemMemTc_Object = MibScalar
telProdNpMonSistemMemTc = _TelProdNpMonSistemMemTc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 37),
    _TelProdNpMonSistemMemTc_Type()
)
telProdNpMonSistemMemTc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemMemTc.setStatus("obsolete")
_TelProdNpMonSistemFan_ObjectIdentity = ObjectIdentity
telProdNpMonSistemFan = _TelProdNpMonSistemFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3)
)
_TelProdNpMonSistemFanCpu_Type = Integer32
_TelProdNpMonSistemFanCpu_Object = MibScalar
telProdNpMonSistemFanCpu = _TelProdNpMonSistemFanCpu_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3, 1),
    _TelProdNpMonSistemFanCpu_Type()
)
telProdNpMonSistemFanCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemFanCpu.setStatus("mandatory")
_TelProdNpMonSistemFanCpuPerCent_Type = Integer32
_TelProdNpMonSistemFanCpuPerCent_Object = MibScalar
telProdNpMonSistemFanCpuPerCent = _TelProdNpMonSistemFanCpuPerCent_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3, 2),
    _TelProdNpMonSistemFanCpuPerCent_Type()
)
telProdNpMonSistemFanCpuPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemFanCpuPerCent.setStatus("mandatory")
_TelProdNpMonSistemFanCase_Type = Integer32
_TelProdNpMonSistemFanCase_Object = MibScalar
telProdNpMonSistemFanCase = _TelProdNpMonSistemFanCase_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3, 3),
    _TelProdNpMonSistemFanCase_Type()
)
telProdNpMonSistemFanCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemFanCase.setStatus("mandatory")
_TelProdNpMonSistemFanCasePerCent_Type = Integer32
_TelProdNpMonSistemFanCasePerCent_Object = MibScalar
telProdNpMonSistemFanCasePerCent = _TelProdNpMonSistemFanCasePerCent_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3, 4),
    _TelProdNpMonSistemFanCasePerCent_Type()
)
telProdNpMonSistemFanCasePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonSistemFanCasePerCent.setStatus("mandatory")
_TelProdNpMonPoeCardsTable_Object = MibTable
telProdNpMonPoeCardsTable = _TelProdNpMonPoeCardsTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    telProdNpMonPoeCardsTable.setStatus("mandatory")
_TelProdNpMonPoeCardsEntry_Object = MibTableRow
telProdNpMonPoeCardsEntry = _TelProdNpMonPoeCardsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 4, 1)
)
telProdNpMonPoeCardsEntry.setIndexNames(
    (0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonPoeCardsInd"),
)
if mibBuilder.loadTexts:
    telProdNpMonPoeCardsEntry.setStatus("mandatory")
_TelProdNpMonPoeCardsInd_Type = Integer32
_TelProdNpMonPoeCardsInd_Object = MibTableColumn
telProdNpMonPoeCardsInd = _TelProdNpMonPoeCardsInd_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 4, 1, 1),
    _TelProdNpMonPoeCardsInd_Type()
)
telProdNpMonPoeCardsInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonPoeCardsInd.setStatus("mandatory")
_TelProdNpMonPoeCardsState_Type = DisplayString
_TelProdNpMonPoeCardsState_Object = MibTableColumn
telProdNpMonPoeCardsState = _TelProdNpMonPoeCardsState_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 4, 1, 2),
    _TelProdNpMonPoeCardsState_Type()
)
telProdNpMonPoeCardsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonPoeCardsState.setStatus("mandatory")
_TelProdNpMonInterfCommandsTable_Object = MibTable
telProdNpMonInterfCommandsTable = _TelProdNpMonInterfCommandsTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfCommandsTable.setStatus("mandatory")
_TelProdNpMonInterfCommandsEntry_Object = MibTableRow
telProdNpMonInterfCommandsEntry = _TelProdNpMonInterfCommandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 1, 1)
)
telProdNpMonInterfCommandsEntry.setIndexNames(
    (0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfCommandsIfc"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfCommandsEntry.setStatus("mandatory")
_TelProdNpMonInterfCommandsIfc_Type = Integer32
_TelProdNpMonInterfCommandsIfc_Object = MibTableColumn
telProdNpMonInterfCommandsIfc = _TelProdNpMonInterfCommandsIfc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 1, 1, 1),
    _TelProdNpMonInterfCommandsIfc_Type()
)
telProdNpMonInterfCommandsIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfCommandsIfc.setStatus("mandatory")


class _TelProdNpMonInterfCommandsClear_Type(Integer32):
    """Custom type telProdNpMonInterfCommandsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("valid", 2),
          ("error", 3),
          ("undefined", 4))
    )


_TelProdNpMonInterfCommandsClear_Type.__name__ = "Integer32"
_TelProdNpMonInterfCommandsClear_Object = MibTableColumn
telProdNpMonInterfCommandsClear = _TelProdNpMonInterfCommandsClear_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 1, 1, 2),
    _TelProdNpMonInterfCommandsClear_Type()
)
telProdNpMonInterfCommandsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telProdNpMonInterfCommandsClear.setStatus("mandatory")
_TelProdNpMonInterfBufferTable_Object = MibTable
telProdNpMonInterfBufferTable = _TelProdNpMonInterfBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferTable.setStatus("mandatory")
_TelProdNpMonInterfBufferEntry_Object = MibTableRow
telProdNpMonInterfBufferEntry = _TelProdNpMonInterfBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1)
)
telProdNpMonInterfBufferEntry.setIndexNames(
    (0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfBufferIfc"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferEntry.setStatus("mandatory")
_TelProdNpMonInterfBufferIfc_Type = Integer32
_TelProdNpMonInterfBufferIfc_Object = MibTableColumn
telProdNpMonInterfBufferIfc = _TelProdNpMonInterfBufferIfc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 1),
    _TelProdNpMonInterfBufferIfc_Type()
)
telProdNpMonInterfBufferIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferIfc.setStatus("obsolete")


class _TelProdNpMonInterfBufferKind_Type(Integer32):
    """Custom type telProdNpMonInterfBufferKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67)
        )
    )
    namedValues = NamedValues(
        *(("vi", 1),
          ("pn", 2),
          ("pri", 3),
          ("xeth", 4),
          ("arpa", 5),
          ("chp", 6),
          ("osl", 7),
          ("eth", 8),
          ("sl", 9),
          ("x28", 10),
          ("dmr", 11),
          ("tkr", 12),
          ("snk", 13),
          ("x25", 14),
          ("man", 15),
          ("atr", 16),
          ("fddi", 17),
          ("srly", 18),
          ("ippn", 19),
          ("fr", 20),
          ("ppp", 21),
          ("bdg", 22),
          ("null", 23),
          ("isdnb", 24),
          ("sdlc", 25),
          ("v25b", 26),
          ("routernode", 27),
          ("noderouter", 28),
          ("isdnd", 29),
          ("xot", 30),
          ("int270", 31),
          ("tnip", 32),
          ("mppp", 33),
          ("atm", 34),
          ("subatm", 35),
          ("ipsec", 36),
          ("bri", 37),
          ("x25fak", 38),
          ("isdnbfak", 39),
          ("isdndfak", 40),
          ("xotfak", 41),
          ("int270fak", 42),
          ("asdp", 43),
          ("syncsl", 44),
          ("asyncsl", 45),
          ("aptb", 46),
          ("dialrout", 47),
          ("arly", 48),
          ("mem", 49),
          ("vlaneth", 50),
          ("voip", 51),
          ("l2tp", 52),
          ("bvi", 53),
          ("scada", 54),
          ("wlan", 55),
          ("sepi", 56),
          ("eibz", 57),
          ("gpio", 58),
          ("autosl", 59),
          ("mdmemu", 60),
          ("frsub", 61),
          ("bvisub", 62),
          ("nic", 63),
          ("dip", 64),
          ("iec101gw", 65),
          ("gps", 66),
          ("gpsdatasl", 67))
    )


_TelProdNpMonInterfBufferKind_Type.__name__ = "Integer32"
_TelProdNpMonInterfBufferKind_Object = MibTableColumn
telProdNpMonInterfBufferKind = _TelProdNpMonInterfBufferKind_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 2),
    _TelProdNpMonInterfBufferKind_Type()
)
telProdNpMonInterfBufferKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferKind.setStatus("mandatory")
_TelProdNpMonInterfBufferOrder_Type = Integer32
_TelProdNpMonInterfBufferOrder_Object = MibTableColumn
telProdNpMonInterfBufferOrder = _TelProdNpMonInterfBufferOrder_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 3),
    _TelProdNpMonInterfBufferOrder_Type()
)
telProdNpMonInterfBufferOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferOrder.setStatus("mandatory")
_TelProdNpMonInterfBufferReq_Type = Integer32
_TelProdNpMonInterfBufferReq_Object = MibTableColumn
telProdNpMonInterfBufferReq = _TelProdNpMonInterfBufferReq_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 4),
    _TelProdNpMonInterfBufferReq_Type()
)
telProdNpMonInterfBufferReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferReq.setStatus("mandatory")
_TelProdNpMonInterfBufferAlloc_Type = Integer32
_TelProdNpMonInterfBufferAlloc_Object = MibTableColumn
telProdNpMonInterfBufferAlloc = _TelProdNpMonInterfBufferAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 5),
    _TelProdNpMonInterfBufferAlloc_Type()
)
telProdNpMonInterfBufferAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferAlloc.setStatus("mandatory")
_TelProdNpMonInterfBufferLow_Type = Integer32
_TelProdNpMonInterfBufferLow_Object = MibTableColumn
telProdNpMonInterfBufferLow = _TelProdNpMonInterfBufferLow_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 6),
    _TelProdNpMonInterfBufferLow_Type()
)
telProdNpMonInterfBufferLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferLow.setStatus("mandatory")
_TelProdNpMonInterfBufferCurr_Type = Integer32
_TelProdNpMonInterfBufferCurr_Object = MibTableColumn
telProdNpMonInterfBufferCurr = _TelProdNpMonInterfBufferCurr_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 7),
    _TelProdNpMonInterfBufferCurr_Type()
)
telProdNpMonInterfBufferCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferCurr.setStatus("mandatory")
_TelProdNpMonInterfBufferHdr_Type = Integer32
_TelProdNpMonInterfBufferHdr_Object = MibTableColumn
telProdNpMonInterfBufferHdr = _TelProdNpMonInterfBufferHdr_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 8),
    _TelProdNpMonInterfBufferHdr_Type()
)
telProdNpMonInterfBufferHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferHdr.setStatus("mandatory")
_TelProdNpMonInterfBufferWrap_Type = Integer32
_TelProdNpMonInterfBufferWrap_Object = MibTableColumn
telProdNpMonInterfBufferWrap = _TelProdNpMonInterfBufferWrap_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 9),
    _TelProdNpMonInterfBufferWrap_Type()
)
telProdNpMonInterfBufferWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferWrap.setStatus("mandatory")
_TelProdNpMonInterfBufferData_Type = Integer32
_TelProdNpMonInterfBufferData_Object = MibTableColumn
telProdNpMonInterfBufferData = _TelProdNpMonInterfBufferData_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 10),
    _TelProdNpMonInterfBufferData_Type()
)
telProdNpMonInterfBufferData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferData.setStatus("mandatory")
_TelProdNpMonInterfBufferTrail_Type = Integer32
_TelProdNpMonInterfBufferTrail_Object = MibTableColumn
telProdNpMonInterfBufferTrail = _TelProdNpMonInterfBufferTrail_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 11),
    _TelProdNpMonInterfBufferTrail_Type()
)
telProdNpMonInterfBufferTrail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferTrail.setStatus("mandatory")
_TelProdNpMonInterfBufferTotal_Type = Integer32
_TelProdNpMonInterfBufferTotal_Object = MibTableColumn
telProdNpMonInterfBufferTotal = _TelProdNpMonInterfBufferTotal_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 12),
    _TelProdNpMonInterfBufferTotal_Type()
)
telProdNpMonInterfBufferTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferTotal.setStatus("mandatory")
_TelProdNpMonInterfBufferAlloc2_Type = Integer32
_TelProdNpMonInterfBufferAlloc2_Object = MibTableColumn
telProdNpMonInterfBufferAlloc2 = _TelProdNpMonInterfBufferAlloc2_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 13),
    _TelProdNpMonInterfBufferAlloc2_Type()
)
telProdNpMonInterfBufferAlloc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfBufferAlloc2.setStatus("mandatory")
_TelProdNpMonInterfGeneralTable_Object = MibTable
telProdNpMonInterfGeneralTable = _TelProdNpMonInterfGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralTable.setStatus("mandatory")
_TelProdNpMonInterfGeneralEntry_Object = MibTableRow
telProdNpMonInterfGeneralEntry = _TelProdNpMonInterfGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1)
)
telProdNpMonInterfGeneralEntry.setIndexNames(
    (0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfGeneralIfc"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralEntry.setStatus("mandatory")
_TelProdNpMonInterfGeneralIfc_Type = Integer32
_TelProdNpMonInterfGeneralIfc_Object = MibTableColumn
telProdNpMonInterfGeneralIfc = _TelProdNpMonInterfGeneralIfc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 1),
    _TelProdNpMonInterfGeneralIfc_Type()
)
telProdNpMonInterfGeneralIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralIfc.setStatus("obsolete")


class _TelProdNpMonInterfGeneralKind_Type(Integer32):
    """Custom type telProdNpMonInterfGeneralKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67)
        )
    )
    namedValues = NamedValues(
        *(("vi", 1),
          ("pn", 2),
          ("pri", 3),
          ("xeth", 4),
          ("arpa", 5),
          ("chp", 6),
          ("osl", 7),
          ("eth", 8),
          ("sl", 9),
          ("x28", 10),
          ("dmr", 11),
          ("tkr", 12),
          ("snk", 13),
          ("x25", 14),
          ("man", 15),
          ("atr", 16),
          ("fddi", 17),
          ("srly", 18),
          ("ippn", 19),
          ("fr", 20),
          ("ppp", 21),
          ("bdg", 22),
          ("null", 23),
          ("isdnb", 24),
          ("sdlc", 25),
          ("v25b", 26),
          ("routernode", 27),
          ("noderouter", 28),
          ("isdnd", 29),
          ("xot", 30),
          ("int270", 31),
          ("tnip", 32),
          ("mppp", 33),
          ("atm", 34),
          ("subatm", 35),
          ("ipsec", 36),
          ("bri", 37),
          ("x25fak", 38),
          ("isdnbfak", 39),
          ("isdndfak", 40),
          ("xotfak", 41),
          ("int270fak", 42),
          ("asdp", 43),
          ("syncsl", 44),
          ("asyncsl", 45),
          ("aptb", 46),
          ("dialrout", 47),
          ("arly", 48),
          ("mem", 49),
          ("vlaneth", 50),
          ("voip", 51),
          ("l2tp", 52),
          ("bvi", 53),
          ("scada", 54),
          ("wlan", 55),
          ("sepi", 56),
          ("eibz", 57),
          ("gpio", 58),
          ("autosl", 59),
          ("mdmemu", 60),
          ("frsub", 61),
          ("bvisub", 62),
          ("nic", 63),
          ("dip", 64),
          ("iec101gw", 65),
          ("gps", 66),
          ("gpsdatasl", 67))
    )


_TelProdNpMonInterfGeneralKind_Type.__name__ = "Integer32"
_TelProdNpMonInterfGeneralKind_Object = MibTableColumn
telProdNpMonInterfGeneralKind = _TelProdNpMonInterfGeneralKind_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 2),
    _TelProdNpMonInterfGeneralKind_Type()
)
telProdNpMonInterfGeneralKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralKind.setStatus("mandatory")
_TelProdNpMonInterfGeneralOrder_Type = Integer32
_TelProdNpMonInterfGeneralOrder_Object = MibTableColumn
telProdNpMonInterfGeneralOrder = _TelProdNpMonInterfGeneralOrder_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 3),
    _TelProdNpMonInterfGeneralOrder_Type()
)
telProdNpMonInterfGeneralOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralOrder.setStatus("mandatory")
_TelProdNpMonInterfGeneralCsr_Type = Integer32
_TelProdNpMonInterfGeneralCsr_Object = MibTableColumn
telProdNpMonInterfGeneralCsr = _TelProdNpMonInterfGeneralCsr_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 4),
    _TelProdNpMonInterfGeneralCsr_Type()
)
telProdNpMonInterfGeneralCsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralCsr.setStatus("mandatory")
_TelProdNpMonInterfGeneralVect_Type = Integer32
_TelProdNpMonInterfGeneralVect_Object = MibTableColumn
telProdNpMonInterfGeneralVect = _TelProdNpMonInterfGeneralVect_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 5),
    _TelProdNpMonInterfGeneralVect_Type()
)
telProdNpMonInterfGeneralVect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralVect.setStatus("mandatory")
_TelProdNpMonInterfGeneralTestvalid_Type = Counter32
_TelProdNpMonInterfGeneralTestvalid_Object = MibTableColumn
telProdNpMonInterfGeneralTestvalid = _TelProdNpMonInterfGeneralTestvalid_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 6),
    _TelProdNpMonInterfGeneralTestvalid_Type()
)
telProdNpMonInterfGeneralTestvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralTestvalid.setStatus("mandatory")
_TelProdNpMonInterfGeneralTestfailure_Type = Counter32
_TelProdNpMonInterfGeneralTestfailure_Object = MibTableColumn
telProdNpMonInterfGeneralTestfailure = _TelProdNpMonInterfGeneralTestfailure_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 7),
    _TelProdNpMonInterfGeneralTestfailure_Type()
)
telProdNpMonInterfGeneralTestfailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralTestfailure.setStatus("mandatory")
_TelProdNpMonInterfGeneralMaintenFailure_Type = Counter32
_TelProdNpMonInterfGeneralMaintenFailure_Object = MibTableColumn
telProdNpMonInterfGeneralMaintenFailure = _TelProdNpMonInterfGeneralMaintenFailure_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 8),
    _TelProdNpMonInterfGeneralMaintenFailure_Type()
)
telProdNpMonInterfGeneralMaintenFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfGeneralMaintenFailure.setStatus("mandatory")
_TelProdNpMonInterfErrorsTable_Object = MibTable
telProdNpMonInterfErrorsTable = _TelProdNpMonInterfErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsTable.setStatus("mandatory")
_TelProdNpMonInterfErrorsEntry_Object = MibTableRow
telProdNpMonInterfErrorsEntry = _TelProdNpMonInterfErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1)
)
telProdNpMonInterfErrorsEntry.setIndexNames(
    (0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfErrorsIfc"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsEntry.setStatus("mandatory")
_TelProdNpMonInterfErrorsIfc_Type = Integer32
_TelProdNpMonInterfErrorsIfc_Object = MibTableColumn
telProdNpMonInterfErrorsIfc = _TelProdNpMonInterfErrorsIfc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 1),
    _TelProdNpMonInterfErrorsIfc_Type()
)
telProdNpMonInterfErrorsIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsIfc.setStatus("obsolete")


class _TelProdNpMonInterfErrorsKind_Type(Integer32):
    """Custom type telProdNpMonInterfErrorsKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67)
        )
    )
    namedValues = NamedValues(
        *(("vi", 1),
          ("pn", 2),
          ("pri", 3),
          ("xeth", 4),
          ("arpa", 5),
          ("chp", 6),
          ("osl", 7),
          ("eth", 8),
          ("sl", 9),
          ("x28", 10),
          ("dmr", 11),
          ("tkr", 12),
          ("snk", 13),
          ("x25", 14),
          ("man", 15),
          ("atr", 16),
          ("fddi", 17),
          ("srly", 18),
          ("ippn", 19),
          ("fr", 20),
          ("ppp", 21),
          ("bdg", 22),
          ("null", 23),
          ("isdnb", 24),
          ("sdlc", 25),
          ("v25b", 26),
          ("routernode", 27),
          ("noderouter", 28),
          ("isdnd", 29),
          ("xot", 30),
          ("int270", 31),
          ("tnip", 32),
          ("mppp", 33),
          ("atm", 34),
          ("subatm", 35),
          ("ipsec", 36),
          ("bri", 37),
          ("x25fak", 38),
          ("isdnbfak", 39),
          ("isdndfak", 40),
          ("xotfak", 41),
          ("int270fak", 42),
          ("asdp", 43),
          ("syncsl", 44),
          ("asyncsl", 45),
          ("aptb", 46),
          ("dialrout", 47),
          ("arly", 48),
          ("mem", 49),
          ("vlaneth", 50),
          ("voip", 51),
          ("l2tp", 52),
          ("bvi", 53),
          ("scada", 54),
          ("wlan", 55),
          ("sepi", 56),
          ("eibz", 57),
          ("gpio", 58),
          ("autosl", 59),
          ("mdmemu", 60),
          ("frsub", 61),
          ("bvisub", 62),
          ("nic", 63),
          ("dip", 64),
          ("iec101gw", 65),
          ("gps", 66),
          ("gpsdatasl", 67))
    )


_TelProdNpMonInterfErrorsKind_Type.__name__ = "Integer32"
_TelProdNpMonInterfErrorsKind_Object = MibTableColumn
telProdNpMonInterfErrorsKind = _TelProdNpMonInterfErrorsKind_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 2),
    _TelProdNpMonInterfErrorsKind_Type()
)
telProdNpMonInterfErrorsKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsKind.setStatus("mandatory")
_TelProdNpMonInterfErrorsOrder_Type = Integer32
_TelProdNpMonInterfErrorsOrder_Object = MibTableColumn
telProdNpMonInterfErrorsOrder = _TelProdNpMonInterfErrorsOrder_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 3),
    _TelProdNpMonInterfErrorsOrder_Type()
)
telProdNpMonInterfErrorsOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsOrder.setStatus("mandatory")
_TelProdNpMonInterfErrorsIdiscard_Type = Counter32
_TelProdNpMonInterfErrorsIdiscard_Object = MibTableColumn
telProdNpMonInterfErrorsIdiscard = _TelProdNpMonInterfErrorsIdiscard_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 4),
    _TelProdNpMonInterfErrorsIdiscard_Type()
)
telProdNpMonInterfErrorsIdiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsIdiscard.setStatus("mandatory")
_TelProdNpMonInterfErrorsIerrors_Type = Counter32
_TelProdNpMonInterfErrorsIerrors_Object = MibTableColumn
telProdNpMonInterfErrorsIerrors = _TelProdNpMonInterfErrorsIerrors_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 5),
    _TelProdNpMonInterfErrorsIerrors_Type()
)
telProdNpMonInterfErrorsIerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsIerrors.setStatus("mandatory")
_TelProdNpMonInterfErrorsIunkprot_Type = Counter32
_TelProdNpMonInterfErrorsIunkprot_Object = MibTableColumn
telProdNpMonInterfErrorsIunkprot = _TelProdNpMonInterfErrorsIunkprot_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 6),
    _TelProdNpMonInterfErrorsIunkprot_Type()
)
telProdNpMonInterfErrorsIunkprot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsIunkprot.setStatus("mandatory")
_TelProdNpMonInterfErrorsOflowdrop_Type = Counter32
_TelProdNpMonInterfErrorsOflowdrop_Object = MibTableColumn
telProdNpMonInterfErrorsOflowdrop = _TelProdNpMonInterfErrorsOflowdrop_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 7),
    _TelProdNpMonInterfErrorsOflowdrop_Type()
)
telProdNpMonInterfErrorsOflowdrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsOflowdrop.setStatus("mandatory")
_TelProdNpMonInterfErrorsOdiscard_Type = Counter32
_TelProdNpMonInterfErrorsOdiscard_Object = MibTableColumn
telProdNpMonInterfErrorsOdiscard = _TelProdNpMonInterfErrorsOdiscard_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 8),
    _TelProdNpMonInterfErrorsOdiscard_Type()
)
telProdNpMonInterfErrorsOdiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsOdiscard.setStatus("mandatory")
_TelProdNpMonInterfErrorsOerrors_Type = Counter32
_TelProdNpMonInterfErrorsOerrors_Object = MibTableColumn
telProdNpMonInterfErrorsOerrors = _TelProdNpMonInterfErrorsOerrors_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 9),
    _TelProdNpMonInterfErrorsOerrors_Type()
)
telProdNpMonInterfErrorsOerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfErrorsOerrors.setStatus("mandatory")
_TelProdNpMonInterfQueueTable_Object = MibTable
telProdNpMonInterfQueueTable = _TelProdNpMonInterfQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueTable.setStatus("mandatory")
_TelProdNpMonInterfQueueEntry_Object = MibTableRow
telProdNpMonInterfQueueEntry = _TelProdNpMonInterfQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1)
)
telProdNpMonInterfQueueEntry.setIndexNames(
    (0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfQueueIfc"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueEntry.setStatus("mandatory")
_TelProdNpMonInterfQueueIfc_Type = Integer32
_TelProdNpMonInterfQueueIfc_Object = MibTableColumn
telProdNpMonInterfQueueIfc = _TelProdNpMonInterfQueueIfc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 1),
    _TelProdNpMonInterfQueueIfc_Type()
)
telProdNpMonInterfQueueIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueIfc.setStatus("obsolete")


class _TelProdNpMonInterfQueueKind_Type(Integer32):
    """Custom type telProdNpMonInterfQueueKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67)
        )
    )
    namedValues = NamedValues(
        *(("vi", 1),
          ("pn", 2),
          ("pri", 3),
          ("xeth", 4),
          ("arpa", 5),
          ("chp", 6),
          ("osl", 7),
          ("eth", 8),
          ("sl", 9),
          ("x28", 10),
          ("dmr", 11),
          ("tkr", 12),
          ("snk", 13),
          ("x25", 14),
          ("man", 15),
          ("atr", 16),
          ("fddi", 17),
          ("srly", 18),
          ("ippn", 19),
          ("fr", 20),
          ("ppp", 21),
          ("bdg", 22),
          ("null", 23),
          ("isdnb", 24),
          ("sdlc", 25),
          ("v25b", 26),
          ("routernode", 27),
          ("noderouter", 28),
          ("isdnd", 29),
          ("xot", 30),
          ("int270", 31),
          ("tnip", 32),
          ("mppp", 33),
          ("atm", 34),
          ("subatm", 35),
          ("ipsec", 36),
          ("bri", 37),
          ("x25fak", 38),
          ("isdnbfak", 39),
          ("isdndfak", 40),
          ("xotfak", 41),
          ("int270fak", 42),
          ("asdp", 43),
          ("syncsl", 44),
          ("asyncsl", 45),
          ("aptb", 46),
          ("dialrout", 47),
          ("arly", 48),
          ("mem", 49),
          ("vlaneth", 50),
          ("voip", 51),
          ("l2tp", 52),
          ("bvi", 53),
          ("scada", 54),
          ("wlan", 55),
          ("sepi", 56),
          ("eibz", 57),
          ("gpio", 58),
          ("autosl", 59),
          ("mdmemu", 60),
          ("frsub", 61),
          ("bvisub", 62),
          ("nic", 63),
          ("dip", 64),
          ("iec101gw", 65),
          ("gps", 66),
          ("gpsdatasl", 67))
    )


_TelProdNpMonInterfQueueKind_Type.__name__ = "Integer32"
_TelProdNpMonInterfQueueKind_Object = MibTableColumn
telProdNpMonInterfQueueKind = _TelProdNpMonInterfQueueKind_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 2),
    _TelProdNpMonInterfQueueKind_Type()
)
telProdNpMonInterfQueueKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueKind.setStatus("mandatory")
_TelProdNpMonInterfQueueOrder_Type = Integer32
_TelProdNpMonInterfQueueOrder_Object = MibTableColumn
telProdNpMonInterfQueueOrder = _TelProdNpMonInterfQueueOrder_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 3),
    _TelProdNpMonInterfQueueOrder_Type()
)
telProdNpMonInterfQueueOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueOrder.setStatus("mandatory")
_TelProdNpMonInterfQueueIalloc_Type = Integer32
_TelProdNpMonInterfQueueIalloc_Object = MibTableColumn
telProdNpMonInterfQueueIalloc = _TelProdNpMonInterfQueueIalloc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 4),
    _TelProdNpMonInterfQueueIalloc_Type()
)
telProdNpMonInterfQueueIalloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueIalloc.setStatus("mandatory")
_TelProdNpMonInterfQueueIlow_Type = Integer32
_TelProdNpMonInterfQueueIlow_Object = MibTableColumn
telProdNpMonInterfQueueIlow = _TelProdNpMonInterfQueueIlow_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 5),
    _TelProdNpMonInterfQueueIlow_Type()
)
telProdNpMonInterfQueueIlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueIlow.setStatus("mandatory")
_TelProdNpMonInterfQueueIcurrent_Type = Integer32
_TelProdNpMonInterfQueueIcurrent_Object = MibTableColumn
telProdNpMonInterfQueueIcurrent = _TelProdNpMonInterfQueueIcurrent_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 6),
    _TelProdNpMonInterfQueueIcurrent_Type()
)
telProdNpMonInterfQueueIcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueIcurrent.setStatus("mandatory")
_TelProdNpMonInterfQueueOfair_Type = Integer32
_TelProdNpMonInterfQueueOfair_Object = MibTableColumn
telProdNpMonInterfQueueOfair = _TelProdNpMonInterfQueueOfair_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 7),
    _TelProdNpMonInterfQueueOfair_Type()
)
telProdNpMonInterfQueueOfair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueOfair.setStatus("mandatory")
_TelProdNpMonInterfQueueOcurrent_Type = Integer32
_TelProdNpMonInterfQueueOcurrent_Object = MibTableColumn
telProdNpMonInterfQueueOcurrent = _TelProdNpMonInterfQueueOcurrent_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 8),
    _TelProdNpMonInterfQueueOcurrent_Type()
)
telProdNpMonInterfQueueOcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfQueueOcurrent.setStatus("mandatory")
_TelProdNpMonInterfStatsTable_Object = MibTable
telProdNpMonInterfStatsTable = _TelProdNpMonInterfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsTable.setStatus("mandatory")
_TelProdNpMonInterfStatsEntry_Object = MibTableRow
telProdNpMonInterfStatsEntry = _TelProdNpMonInterfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1)
)
telProdNpMonInterfStatsEntry.setIndexNames(
    (0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfStatsIfc"),
)
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsEntry.setStatus("mandatory")
_TelProdNpMonInterfStatsIfc_Type = Integer32
_TelProdNpMonInterfStatsIfc_Object = MibTableColumn
telProdNpMonInterfStatsIfc = _TelProdNpMonInterfStatsIfc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 1),
    _TelProdNpMonInterfStatsIfc_Type()
)
telProdNpMonInterfStatsIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsIfc.setStatus("obsolete")


class _TelProdNpMonInterfStatsKind_Type(Integer32):
    """Custom type telProdNpMonInterfStatsKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67)
        )
    )
    namedValues = NamedValues(
        *(("vi", 1),
          ("pn", 2),
          ("pri", 3),
          ("xeth", 4),
          ("arpa", 5),
          ("chp", 6),
          ("osl", 7),
          ("eth", 8),
          ("sl", 9),
          ("x28", 10),
          ("dmr", 11),
          ("tkr", 12),
          ("snk", 13),
          ("x25", 14),
          ("man", 15),
          ("atr", 16),
          ("fddi", 17),
          ("srly", 18),
          ("ippn", 19),
          ("fr", 20),
          ("ppp", 21),
          ("bdg", 22),
          ("null", 23),
          ("isdnb", 24),
          ("sdlc", 25),
          ("v25b", 26),
          ("routernode", 27),
          ("noderouter", 28),
          ("isdnd", 29),
          ("xot", 30),
          ("int270", 31),
          ("tnip", 32),
          ("mppp", 33),
          ("atm", 34),
          ("subatm", 35),
          ("ipsec", 36),
          ("bri", 37),
          ("x25fak", 38),
          ("isdnbfak", 39),
          ("isdndfak", 40),
          ("xotfak", 41),
          ("int270fak", 42),
          ("asdp", 43),
          ("syncsl", 44),
          ("asyncsl", 45),
          ("aptb", 46),
          ("dialrout", 47),
          ("arly", 48),
          ("mem", 49),
          ("vlaneth", 50),
          ("voip", 51),
          ("l2tp", 52),
          ("bvi", 53),
          ("scada", 54),
          ("wlan", 55),
          ("sepi", 56),
          ("eibz", 57),
          ("gpio", 58),
          ("autosl", 59),
          ("mdmemu", 60),
          ("frsub", 61),
          ("bvisub", 62),
          ("nic", 63),
          ("dip", 64),
          ("iec101gw", 65),
          ("gps", 66),
          ("gpsdatasl", 67))
    )


_TelProdNpMonInterfStatsKind_Type.__name__ = "Integer32"
_TelProdNpMonInterfStatsKind_Object = MibTableColumn
telProdNpMonInterfStatsKind = _TelProdNpMonInterfStatsKind_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 2),
    _TelProdNpMonInterfStatsKind_Type()
)
telProdNpMonInterfStatsKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsKind.setStatus("mandatory")
_TelProdNpMonInterfStatsOrder_Type = Integer32
_TelProdNpMonInterfStatsOrder_Object = MibTableColumn
telProdNpMonInterfStatsOrder = _TelProdNpMonInterfStatsOrder_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 3),
    _TelProdNpMonInterfStatsOrder_Type()
)
telProdNpMonInterfStatsOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsOrder.setStatus("mandatory")
_TelProdNpMonInterfStatsUnipkrcv_Type = Counter32
_TelProdNpMonInterfStatsUnipkrcv_Object = MibTableColumn
telProdNpMonInterfStatsUnipkrcv = _TelProdNpMonInterfStatsUnipkrcv_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 4),
    _TelProdNpMonInterfStatsUnipkrcv_Type()
)
telProdNpMonInterfStatsUnipkrcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsUnipkrcv.setStatus("mandatory")
_TelProdNpMonInterfStatsMulpkrcv_Type = Counter32
_TelProdNpMonInterfStatsMulpkrcv_Object = MibTableColumn
telProdNpMonInterfStatsMulpkrcv = _TelProdNpMonInterfStatsMulpkrcv_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 5),
    _TelProdNpMonInterfStatsMulpkrcv_Type()
)
telProdNpMonInterfStatsMulpkrcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsMulpkrcv.setStatus("mandatory")
_TelProdNpMonInterfStatsBytesrcv_Type = Counter32
_TelProdNpMonInterfStatsBytesrcv_Object = MibTableColumn
telProdNpMonInterfStatsBytesrcv = _TelProdNpMonInterfStatsBytesrcv_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 6),
    _TelProdNpMonInterfStatsBytesrcv_Type()
)
telProdNpMonInterfStatsBytesrcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsBytesrcv.setStatus("mandatory")
_TelProdNpMonInterfStatsPkxt_Type = Counter32
_TelProdNpMonInterfStatsPkxt_Object = MibTableColumn
telProdNpMonInterfStatsPkxt = _TelProdNpMonInterfStatsPkxt_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 7),
    _TelProdNpMonInterfStatsPkxt_Type()
)
telProdNpMonInterfStatsPkxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsPkxt.setStatus("mandatory")
_TelProdNpMonInterfStatsBytesxt_Type = Counter32
_TelProdNpMonInterfStatsBytesxt_Object = MibTableColumn
telProdNpMonInterfStatsBytesxt = _TelProdNpMonInterfStatsBytesxt_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 8),
    _TelProdNpMonInterfStatsBytesxt_Type()
)
telProdNpMonInterfStatsBytesxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProdNpMonInterfStatsBytesxt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELDAT-MON-CommonInfo-MIB",
    **{"telProdNpMonSistemMemory": telProdNpMonSistemMemory,
       "telProdNpMonSistemMemSize": telProdNpMonSistemMemSize,
       "telProdNpMonSistemMemAvailable": telProdNpMonSistemMemAvailable,
       "telProdNpMonSistemMemPooldissize": telProdNpMonSistemMemPooldissize,
       "telProdNpMonSistemMemPooldisavailable": telProdNpMonSistemMemPooldisavailable,
       "telProdNpMonSistemMemPoolmdissize": telProdNpMonSistemMemPoolmdissize,
       "telProdNpMonSistemMemPoolmdisavailable": telProdNpMonSistemMemPoolmdisavailable,
       "telProdNpMonSistemMemPooltsize": telProdNpMonSistemMemPooltsize,
       "telProdNpMonSistemMemPooltavailable": telProdNpMonSistemMemPooltavailable,
       "telProdNpMonSistemMemPoolpsize": telProdNpMonSistemMemPoolpsize,
       "telProdNpMonSistemMemPoolpavailable": telProdNpMonSistemMemPoolpavailable,
       "telProdNpMonSistemMemPool0size": telProdNpMonSistemMemPool0size,
       "telProdNpMonSistemMemPool0restpart": telProdNpMonSistemMemPool0restpart,
       "telProdNpMonSistemMemPool0available": telProdNpMonSistemMemPool0available,
       "telProdNpMonSistemMemPool1size": telProdNpMonSistemMemPool1size,
       "telProdNpMonSistemMemPool1restpart": telProdNpMonSistemMemPool1restpart,
       "telProdNpMonSistemMemPool1available": telProdNpMonSistemMemPool1available,
       "telProdNpMonSistemMemPool2size": telProdNpMonSistemMemPool2size,
       "telProdNpMonSistemMemPool2restpart": telProdNpMonSistemMemPool2restpart,
       "telProdNpMonSistemMemPool2available": telProdNpMonSistemMemPool2available,
       "telProdNpMonSistemMemPoolisize": telProdNpMonSistemMemPoolisize,
       "telProdNpMonSistemMemPoolirestpart": telProdNpMonSistemMemPoolirestpart,
       "telProdNpMonSistemMemPooliavailable": telProdNpMonSistemMemPooliavailable,
       "telProdNpMonSistemMemPooldlssize": telProdNpMonSistemMemPooldlssize,
       "telProdNpMonSistemMemPooldlsrestpart": telProdNpMonSistemMemPooldlsrestpart,
       "telProdNpMonSistemMemPooldlsavailable": telProdNpMonSistemMemPooldlsavailable,
       "telProdNpMonSistemMemTotal": telProdNpMonSistemMemTotal,
       "telProdNpMonSistemMemTotalcache": telProdNpMonSistemMemTotalcache,
       "telProdNpMonSistemMemFreecache": telProdNpMonSistemMemFreecache,
       "telProdNpMonSistemMemTotalnoncache": telProdNpMonSistemMemTotalnoncache,
       "telProdNpMonSistemMemFreenoncache": telProdNpMonSistemMemFreenoncache,
       "telProdNpMonSistemMemCaches": telProdNpMonSistemMemCaches,
       "telProdNpMonSistemMemFlash": telProdNpMonSistemMemFlash,
       "telProdNpMonSistemMemFreeglobbuffer": telProdNpMonSistemMemFreeglobbuffer,
       "telProdNpMonSistemMemHeap": telProdNpMonSistemMemHeap,
       "telProdNpMonSistemMemIcused": telProdNpMonSistemMemIcused,
       "telProdNpMonSistemMemIcindex": telProdNpMonSistemMemIcindex,
       "telProdNpMonSistemMemTc": telProdNpMonSistemMemTc,
       "telProdNpMonSistemFan": telProdNpMonSistemFan,
       "telProdNpMonSistemFanCpu": telProdNpMonSistemFanCpu,
       "telProdNpMonSistemFanCpuPerCent": telProdNpMonSistemFanCpuPerCent,
       "telProdNpMonSistemFanCase": telProdNpMonSistemFanCase,
       "telProdNpMonSistemFanCasePerCent": telProdNpMonSistemFanCasePerCent,
       "telProdNpMonPoeCardsTable": telProdNpMonPoeCardsTable,
       "telProdNpMonPoeCardsEntry": telProdNpMonPoeCardsEntry,
       "telProdNpMonPoeCardsInd": telProdNpMonPoeCardsInd,
       "telProdNpMonPoeCardsState": telProdNpMonPoeCardsState,
       "telProdNpMonInterfCommandsTable": telProdNpMonInterfCommandsTable,
       "telProdNpMonInterfCommandsEntry": telProdNpMonInterfCommandsEntry,
       "telProdNpMonInterfCommandsIfc": telProdNpMonInterfCommandsIfc,
       "telProdNpMonInterfCommandsClear": telProdNpMonInterfCommandsClear,
       "telProdNpMonInterfBufferTable": telProdNpMonInterfBufferTable,
       "telProdNpMonInterfBufferEntry": telProdNpMonInterfBufferEntry,
       "telProdNpMonInterfBufferIfc": telProdNpMonInterfBufferIfc,
       "telProdNpMonInterfBufferKind": telProdNpMonInterfBufferKind,
       "telProdNpMonInterfBufferOrder": telProdNpMonInterfBufferOrder,
       "telProdNpMonInterfBufferReq": telProdNpMonInterfBufferReq,
       "telProdNpMonInterfBufferAlloc": telProdNpMonInterfBufferAlloc,
       "telProdNpMonInterfBufferLow": telProdNpMonInterfBufferLow,
       "telProdNpMonInterfBufferCurr": telProdNpMonInterfBufferCurr,
       "telProdNpMonInterfBufferHdr": telProdNpMonInterfBufferHdr,
       "telProdNpMonInterfBufferWrap": telProdNpMonInterfBufferWrap,
       "telProdNpMonInterfBufferData": telProdNpMonInterfBufferData,
       "telProdNpMonInterfBufferTrail": telProdNpMonInterfBufferTrail,
       "telProdNpMonInterfBufferTotal": telProdNpMonInterfBufferTotal,
       "telProdNpMonInterfBufferAlloc2": telProdNpMonInterfBufferAlloc2,
       "telProdNpMonInterfGeneralTable": telProdNpMonInterfGeneralTable,
       "telProdNpMonInterfGeneralEntry": telProdNpMonInterfGeneralEntry,
       "telProdNpMonInterfGeneralIfc": telProdNpMonInterfGeneralIfc,
       "telProdNpMonInterfGeneralKind": telProdNpMonInterfGeneralKind,
       "telProdNpMonInterfGeneralOrder": telProdNpMonInterfGeneralOrder,
       "telProdNpMonInterfGeneralCsr": telProdNpMonInterfGeneralCsr,
       "telProdNpMonInterfGeneralVect": telProdNpMonInterfGeneralVect,
       "telProdNpMonInterfGeneralTestvalid": telProdNpMonInterfGeneralTestvalid,
       "telProdNpMonInterfGeneralTestfailure": telProdNpMonInterfGeneralTestfailure,
       "telProdNpMonInterfGeneralMaintenFailure": telProdNpMonInterfGeneralMaintenFailure,
       "telProdNpMonInterfErrorsTable": telProdNpMonInterfErrorsTable,
       "telProdNpMonInterfErrorsEntry": telProdNpMonInterfErrorsEntry,
       "telProdNpMonInterfErrorsIfc": telProdNpMonInterfErrorsIfc,
       "telProdNpMonInterfErrorsKind": telProdNpMonInterfErrorsKind,
       "telProdNpMonInterfErrorsOrder": telProdNpMonInterfErrorsOrder,
       "telProdNpMonInterfErrorsIdiscard": telProdNpMonInterfErrorsIdiscard,
       "telProdNpMonInterfErrorsIerrors": telProdNpMonInterfErrorsIerrors,
       "telProdNpMonInterfErrorsIunkprot": telProdNpMonInterfErrorsIunkprot,
       "telProdNpMonInterfErrorsOflowdrop": telProdNpMonInterfErrorsOflowdrop,
       "telProdNpMonInterfErrorsOdiscard": telProdNpMonInterfErrorsOdiscard,
       "telProdNpMonInterfErrorsOerrors": telProdNpMonInterfErrorsOerrors,
       "telProdNpMonInterfQueueTable": telProdNpMonInterfQueueTable,
       "telProdNpMonInterfQueueEntry": telProdNpMonInterfQueueEntry,
       "telProdNpMonInterfQueueIfc": telProdNpMonInterfQueueIfc,
       "telProdNpMonInterfQueueKind": telProdNpMonInterfQueueKind,
       "telProdNpMonInterfQueueOrder": telProdNpMonInterfQueueOrder,
       "telProdNpMonInterfQueueIalloc": telProdNpMonInterfQueueIalloc,
       "telProdNpMonInterfQueueIlow": telProdNpMonInterfQueueIlow,
       "telProdNpMonInterfQueueIcurrent": telProdNpMonInterfQueueIcurrent,
       "telProdNpMonInterfQueueOfair": telProdNpMonInterfQueueOfair,
       "telProdNpMonInterfQueueOcurrent": telProdNpMonInterfQueueOcurrent,
       "telProdNpMonInterfStatsTable": telProdNpMonInterfStatsTable,
       "telProdNpMonInterfStatsEntry": telProdNpMonInterfStatsEntry,
       "telProdNpMonInterfStatsIfc": telProdNpMonInterfStatsIfc,
       "telProdNpMonInterfStatsKind": telProdNpMonInterfStatsKind,
       "telProdNpMonInterfStatsOrder": telProdNpMonInterfStatsOrder,
       "telProdNpMonInterfStatsUnipkrcv": telProdNpMonInterfStatsUnipkrcv,
       "telProdNpMonInterfStatsMulpkrcv": telProdNpMonInterfStatsMulpkrcv,
       "telProdNpMonInterfStatsBytesrcv": telProdNpMonInterfStatsBytesrcv,
       "telProdNpMonInterfStatsPkxt": telProdNpMonInterfStatsPkxt,
       "telProdNpMonInterfStatsBytesxt": telProdNpMonInterfStatsBytesxt}
)
