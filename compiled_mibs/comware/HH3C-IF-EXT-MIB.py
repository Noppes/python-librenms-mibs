# SNMP MIB module (HH3C-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-IF-EXT-MIB

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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cIfExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40)
)
if mibBuilder.loadTexts:
    hh3cIfExt.setRevisions(
        ("2021-05-14 00:00",
         "2021-04-27 00:00",
         "2020-08-05 00:00",
         "2020-08-04 00:00",
         "2020-06-09 00:00",
         "2019-08-06 00:00",
         "2018-06-05 00:00",
         "2018-04-26 00:00",
         "2018-02-07 00:00",
         "2018-01-09 00:00",
         "2017-12-13 18:20",
         "2017-07-13 10:40",
         "2016-12-05 18:00",
         "2016-07-01 17:00",
         "2015-12-10 10:00",
         "2015-04-02 04:58",
         "2014-11-20 08:00",
         "2009-05-06 19:36",
         "2004-11-13 19:36")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cIfExtScalarGroup_ObjectIdentity = ObjectIdentity
hh3cIfExtScalarGroup = _Hh3cIfExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 1)
)
_Hh3cIfStatGlobalFlowInterval_Type = Integer32
_Hh3cIfStatGlobalFlowInterval_Object = MibScalar
hh3cIfStatGlobalFlowInterval = _Hh3cIfStatGlobalFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 1, 1),
    _Hh3cIfStatGlobalFlowInterval_Type()
)
hh3cIfStatGlobalFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfStatGlobalFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIfStatGlobalFlowInterval.setUnits("seconds")
_Hh3cIfShutDownInterval_Type = Integer32
_Hh3cIfShutDownInterval_Object = MibScalar
hh3cIfShutDownInterval = _Hh3cIfShutDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 1, 2),
    _Hh3cIfShutDownInterval_Type()
)
hh3cIfShutDownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfShutDownInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIfShutDownInterval.setUnits("seconds")
_Hh3cIfThroughputInKbps_Type = CounterBasedGauge64
_Hh3cIfThroughputInKbps_Object = MibScalar
hh3cIfThroughputInKbps = _Hh3cIfThroughputInKbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 1, 3),
    _Hh3cIfThroughputInKbps_Type()
)
hh3cIfThroughputInKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfThroughputInKbps.setStatus("current")
_Hh3cIfThroughputOutKbps_Type = CounterBasedGauge64
_Hh3cIfThroughputOutKbps_Object = MibScalar
hh3cIfThroughputOutKbps = _Hh3cIfThroughputOutKbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 1, 4),
    _Hh3cIfThroughputOutKbps_Type()
)
hh3cIfThroughputOutKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfThroughputOutKbps.setStatus("current")
_Hh3cIfExtGroup_ObjectIdentity = ObjectIdentity
hh3cIfExtGroup = _Hh3cIfExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2)
)
_Hh3cIfStat_ObjectIdentity = ObjectIdentity
hh3cIfStat = _Hh3cIfStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1)
)
_Hh3cIfStatScalarGroup_ObjectIdentity = ObjectIdentity
hh3cIfStatScalarGroup = _Hh3cIfStatScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 1)
)
_Hh3cIfStatTable_ObjectIdentity = ObjectIdentity
hh3cIfStatTable = _Hh3cIfStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2)
)
_Hh3cIfFlowStatTable_Object = MibTable
hh3cIfFlowStatTable = _Hh3cIfFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfFlowStatTable.setStatus("current")
_Hh3cIfFlowStatEntry_Object = MibTableRow
hh3cIfFlowStatEntry = _Hh3cIfFlowStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1)
)
hh3cIfFlowStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfFlowStatEntry.setStatus("current")
_Hh3cIfStatFlowInterval_Type = Integer32
_Hh3cIfStatFlowInterval_Object = MibTableColumn
hh3cIfStatFlowInterval = _Hh3cIfStatFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 1),
    _Hh3cIfStatFlowInterval_Type()
)
hh3cIfStatFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInterval.setUnits("seconds")
_Hh3cIfStatFlowInBits_Type = Unsigned32
_Hh3cIfStatFlowInBits_Object = MibTableColumn
hh3cIfStatFlowInBits = _Hh3cIfStatFlowInBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 2),
    _Hh3cIfStatFlowInBits_Type()
)
hh3cIfStatFlowInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInBits.setStatus("current")
_Hh3cIfStatFlowOutBits_Type = Unsigned32
_Hh3cIfStatFlowOutBits_Object = MibTableColumn
hh3cIfStatFlowOutBits = _Hh3cIfStatFlowOutBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 3),
    _Hh3cIfStatFlowOutBits_Type()
)
hh3cIfStatFlowOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowOutBits.setStatus("current")
_Hh3cIfStatFlowInPkts_Type = Unsigned32
_Hh3cIfStatFlowInPkts_Object = MibTableColumn
hh3cIfStatFlowInPkts = _Hh3cIfStatFlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 4),
    _Hh3cIfStatFlowInPkts_Type()
)
hh3cIfStatFlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInPkts.setStatus("current")
_Hh3cIfStatFlowOutPkts_Type = Unsigned32
_Hh3cIfStatFlowOutPkts_Object = MibTableColumn
hh3cIfStatFlowOutPkts = _Hh3cIfStatFlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 5),
    _Hh3cIfStatFlowOutPkts_Type()
)
hh3cIfStatFlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowOutPkts.setStatus("current")
_Hh3cIfStatFlowInBytes_Type = Unsigned32
_Hh3cIfStatFlowInBytes_Object = MibTableColumn
hh3cIfStatFlowInBytes = _Hh3cIfStatFlowInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 6),
    _Hh3cIfStatFlowInBytes_Type()
)
hh3cIfStatFlowInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInBytes.setStatus("current")
_Hh3cIfStatFlowOutBytes_Type = Unsigned32
_Hh3cIfStatFlowOutBytes_Object = MibTableColumn
hh3cIfStatFlowOutBytes = _Hh3cIfStatFlowOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 7),
    _Hh3cIfStatFlowOutBytes_Type()
)
hh3cIfStatFlowOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowOutBytes.setStatus("current")
_Hh3cIfSpeedStatTable_Object = MibTable
hh3cIfSpeedStatTable = _Hh3cIfSpeedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cIfSpeedStatTable.setStatus("current")
_Hh3cIfSpeedStatEntry_Object = MibTableRow
hh3cIfSpeedStatEntry = _Hh3cIfSpeedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1)
)
hh3cIfSpeedStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfSpeedStatEntry.setStatus("current")
_Hh3cIfSpeedStatInterval_Type = Integer32
_Hh3cIfSpeedStatInterval_Object = MibTableColumn
hh3cIfSpeedStatInterval = _Hh3cIfSpeedStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 1),
    _Hh3cIfSpeedStatInterval_Type()
)
hh3cIfSpeedStatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatInterval.setUnits("seconds")
_Hh3cIfSpeedStatInPkts_Type = Unsigned32
_Hh3cIfSpeedStatInPkts_Object = MibTableColumn
hh3cIfSpeedStatInPkts = _Hh3cIfSpeedStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 2),
    _Hh3cIfSpeedStatInPkts_Type()
)
hh3cIfSpeedStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatInPkts.setStatus("current")
_Hh3cIfSpeedStatOutPkts_Type = Unsigned32
_Hh3cIfSpeedStatOutPkts_Object = MibTableColumn
hh3cIfSpeedStatOutPkts = _Hh3cIfSpeedStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 3),
    _Hh3cIfSpeedStatOutPkts_Type()
)
hh3cIfSpeedStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatOutPkts.setStatus("current")
_Hh3cIfSpeedStatInBytes_Type = Unsigned32
_Hh3cIfSpeedStatInBytes_Object = MibTableColumn
hh3cIfSpeedStatInBytes = _Hh3cIfSpeedStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 4),
    _Hh3cIfSpeedStatInBytes_Type()
)
hh3cIfSpeedStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatInBytes.setStatus("current")
_Hh3cIfSpeedStatOutBytes_Type = Unsigned32
_Hh3cIfSpeedStatOutBytes_Object = MibTableColumn
hh3cIfSpeedStatOutBytes = _Hh3cIfSpeedStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 5),
    _Hh3cIfSpeedStatOutBytes_Type()
)
hh3cIfSpeedStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatOutBytes.setStatus("current")
_Hh3cIfSpeedStatInBits_Type = Unsigned32
_Hh3cIfSpeedStatInBits_Object = MibTableColumn
hh3cIfSpeedStatInBits = _Hh3cIfSpeedStatInBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 6),
    _Hh3cIfSpeedStatInBits_Type()
)
hh3cIfSpeedStatInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatInBits.setStatus("current")
_Hh3cIfSpeedStatOutBits_Type = Unsigned32
_Hh3cIfSpeedStatOutBits_Object = MibTableColumn
hh3cIfSpeedStatOutBits = _Hh3cIfSpeedStatOutBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 7),
    _Hh3cIfSpeedStatOutBits_Type()
)
hh3cIfSpeedStatOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatOutBits.setStatus("current")
_Hh3cIfHCFlowStatTable_Object = MibTable
hh3cIfHCFlowStatTable = _Hh3cIfHCFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cIfHCFlowStatTable.setStatus("current")
_Hh3cIfHCFlowStatEntry_Object = MibTableRow
hh3cIfHCFlowStatEntry = _Hh3cIfHCFlowStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1)
)
hh3cIfHCFlowStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfHCFlowStatEntry.setStatus("current")
_Hh3cIfStatFlowHCInBits_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCInBits_Object = MibTableColumn
hh3cIfStatFlowHCInBits = _Hh3cIfStatFlowHCInBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 1),
    _Hh3cIfStatFlowHCInBits_Type()
)
hh3cIfStatFlowHCInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCInBits.setStatus("current")
_Hh3cIfStatFlowHCOutBits_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCOutBits_Object = MibTableColumn
hh3cIfStatFlowHCOutBits = _Hh3cIfStatFlowHCOutBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 2),
    _Hh3cIfStatFlowHCOutBits_Type()
)
hh3cIfStatFlowHCOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCOutBits.setStatus("current")
_Hh3cIfStatFlowHCInPkts_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCInPkts_Object = MibTableColumn
hh3cIfStatFlowHCInPkts = _Hh3cIfStatFlowHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 3),
    _Hh3cIfStatFlowHCInPkts_Type()
)
hh3cIfStatFlowHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCInPkts.setStatus("current")
_Hh3cIfStatFlowHCOutPkts_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCOutPkts_Object = MibTableColumn
hh3cIfStatFlowHCOutPkts = _Hh3cIfStatFlowHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 4),
    _Hh3cIfStatFlowHCOutPkts_Type()
)
hh3cIfStatFlowHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCOutPkts.setStatus("current")
_Hh3cIfStatFlowHCInBytes_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCInBytes_Object = MibTableColumn
hh3cIfStatFlowHCInBytes = _Hh3cIfStatFlowHCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 5),
    _Hh3cIfStatFlowHCInBytes_Type()
)
hh3cIfStatFlowHCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCInBytes.setStatus("current")
_Hh3cIfStatFlowHCOutBytes_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCOutBytes_Object = MibTableColumn
hh3cIfStatFlowHCOutBytes = _Hh3cIfStatFlowHCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 6),
    _Hh3cIfStatFlowHCOutBytes_Type()
)
hh3cIfStatFlowHCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCOutBytes.setStatus("current")
_Hh3cIfHCSpeedStatTable_Object = MibTable
hh3cIfHCSpeedStatTable = _Hh3cIfHCSpeedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cIfHCSpeedStatTable.setStatus("current")
_Hh3cIfHCSpeedStatEntry_Object = MibTableRow
hh3cIfHCSpeedStatEntry = _Hh3cIfHCSpeedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 4, 1)
)
hh3cIfHCSpeedStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfHCSpeedStatEntry.setStatus("current")
_Hh3cIfSpeedStatHCInPkts_Type = CounterBasedGauge64
_Hh3cIfSpeedStatHCInPkts_Object = MibTableColumn
hh3cIfSpeedStatHCInPkts = _Hh3cIfSpeedStatHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 4, 1, 1),
    _Hh3cIfSpeedStatHCInPkts_Type()
)
hh3cIfSpeedStatHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatHCInPkts.setStatus("current")
_Hh3cIfSpeedStatHCOutPkts_Type = CounterBasedGauge64
_Hh3cIfSpeedStatHCOutPkts_Object = MibTableColumn
hh3cIfSpeedStatHCOutPkts = _Hh3cIfSpeedStatHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 4, 1, 2),
    _Hh3cIfSpeedStatHCOutPkts_Type()
)
hh3cIfSpeedStatHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatHCOutPkts.setStatus("current")
_Hh3cIfSpeedStatHCInBytes_Type = CounterBasedGauge64
_Hh3cIfSpeedStatHCInBytes_Object = MibTableColumn
hh3cIfSpeedStatHCInBytes = _Hh3cIfSpeedStatHCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 4, 1, 3),
    _Hh3cIfSpeedStatHCInBytes_Type()
)
hh3cIfSpeedStatHCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatHCInBytes.setStatus("current")
_Hh3cIfSpeedStatHCOutBytes_Type = CounterBasedGauge64
_Hh3cIfSpeedStatHCOutBytes_Object = MibTableColumn
hh3cIfSpeedStatHCOutBytes = _Hh3cIfSpeedStatHCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 4, 1, 4),
    _Hh3cIfSpeedStatHCOutBytes_Type()
)
hh3cIfSpeedStatHCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatHCOutBytes.setStatus("current")
_Hh3cIfSpeedStatHCInBits_Type = CounterBasedGauge64
_Hh3cIfSpeedStatHCInBits_Object = MibTableColumn
hh3cIfSpeedStatHCInBits = _Hh3cIfSpeedStatHCInBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 4, 1, 5),
    _Hh3cIfSpeedStatHCInBits_Type()
)
hh3cIfSpeedStatHCInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatHCInBits.setStatus("current")
_Hh3cIfSpeedStatHCOutBits_Type = CounterBasedGauge64
_Hh3cIfSpeedStatHCOutBits_Object = MibTableColumn
hh3cIfSpeedStatHCOutBits = _Hh3cIfSpeedStatHCOutBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 4, 1, 6),
    _Hh3cIfSpeedStatHCOutBits_Type()
)
hh3cIfSpeedStatHCOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatHCOutBits.setStatus("current")
_Hh3cIfControl_ObjectIdentity = ObjectIdentity
hh3cIfControl = _Hh3cIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2)
)
_Hh3cRTParentIfTable_Object = MibTable
hh3cRTParentIfTable = _Hh3cRTParentIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cRTParentIfTable.setStatus("current")
_Hh3cRTParentIfEntry_Object = MibTableRow
hh3cRTParentIfEntry = _Hh3cRTParentIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1, 1)
)
hh3cRTParentIfEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cRTParentIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cRTParentIfEntry.setStatus("current")


class _Hh3cRTParentIfIndex_Type(Integer32):
    """Custom type hh3cRTParentIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cRTParentIfIndex_Type.__name__ = "Integer32"
_Hh3cRTParentIfIndex_Object = MibTableColumn
hh3cRTParentIfIndex = _Hh3cRTParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1, 1, 1),
    _Hh3cRTParentIfIndex_Type()
)
hh3cRTParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRTParentIfIndex.setStatus("current")
_Hh3cRTMinSubIfOrdinal_Type = Integer32
_Hh3cRTMinSubIfOrdinal_Object = MibTableColumn
hh3cRTMinSubIfOrdinal = _Hh3cRTMinSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1, 1, 2),
    _Hh3cRTMinSubIfOrdinal_Type()
)
hh3cRTMinSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTMinSubIfOrdinal.setStatus("current")
_Hh3cRTMaxSubIfOrdinal_Type = Integer32
_Hh3cRTMaxSubIfOrdinal_Object = MibTableColumn
hh3cRTMaxSubIfOrdinal = _Hh3cRTMaxSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1, 1, 3),
    _Hh3cRTMaxSubIfOrdinal_Type()
)
hh3cRTMaxSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTMaxSubIfOrdinal.setStatus("current")
_Hh3cRTSubIfTable_Object = MibTable
hh3cRTSubIfTable = _Hh3cRTSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cRTSubIfTable.setStatus("current")
_Hh3cRTSubIfEntry_Object = MibTableRow
hh3cRTSubIfEntry = _Hh3cRTSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1)
)
hh3cRTSubIfEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cRTSubIfParentIfIndex"),
    (0, "HH3C-IF-EXT-MIB", "hh3cRTSubIfOrdinal"),
)
if mibBuilder.loadTexts:
    hh3cRTSubIfEntry.setStatus("current")


class _Hh3cRTSubIfParentIfIndex_Type(Integer32):
    """Custom type hh3cRTSubIfParentIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cRTSubIfParentIfIndex_Type.__name__ = "Integer32"
_Hh3cRTSubIfParentIfIndex_Object = MibTableColumn
hh3cRTSubIfParentIfIndex = _Hh3cRTSubIfParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 1),
    _Hh3cRTSubIfParentIfIndex_Type()
)
hh3cRTSubIfParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRTSubIfParentIfIndex.setStatus("current")


class _Hh3cRTSubIfOrdinal_Type(Integer32):
    """Custom type hh3cRTSubIfOrdinal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cRTSubIfOrdinal_Type.__name__ = "Integer32"
_Hh3cRTSubIfOrdinal_Object = MibTableColumn
hh3cRTSubIfOrdinal = _Hh3cRTSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 2),
    _Hh3cRTSubIfOrdinal_Type()
)
hh3cRTSubIfOrdinal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRTSubIfOrdinal.setStatus("current")
_Hh3cRTSubIfSubIfIndex_Type = Integer32
_Hh3cRTSubIfSubIfIndex_Object = MibTableColumn
hh3cRTSubIfSubIfIndex = _Hh3cRTSubIfSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 3),
    _Hh3cRTSubIfSubIfIndex_Type()
)
hh3cRTSubIfSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTSubIfSubIfIndex.setStatus("current")


class _Hh3cRTSubIfSubIfDesc_Type(DisplayString):
    """Custom type hh3cRTSubIfSubIfDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cRTSubIfSubIfDesc_Type.__name__ = "DisplayString"
_Hh3cRTSubIfSubIfDesc_Object = MibTableColumn
hh3cRTSubIfSubIfDesc = _Hh3cRTSubIfSubIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 4),
    _Hh3cRTSubIfSubIfDesc_Type()
)
hh3cRTSubIfSubIfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTSubIfSubIfDesc.setStatus("current")
_Hh3cRTSubIfRowStatus_Type = RowStatus
_Hh3cRTSubIfRowStatus_Object = MibTableColumn
hh3cRTSubIfRowStatus = _Hh3cRTSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 5),
    _Hh3cRTSubIfRowStatus_Type()
)
hh3cRTSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRTSubIfRowStatus.setStatus("current")
_Hh3cIfLinkModeTable_Object = MibTable
hh3cIfLinkModeTable = _Hh3cIfLinkModeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cIfLinkModeTable.setStatus("current")
_Hh3cIfLinkModeEntry_Object = MibTableRow
hh3cIfLinkModeEntry = _Hh3cIfLinkModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3, 1)
)
hh3cIfLinkModeEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cIfLinkModeIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfLinkModeEntry.setStatus("current")


class _Hh3cIfLinkModeIndex_Type(Integer32):
    """Custom type hh3cIfLinkModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIfLinkModeIndex_Type.__name__ = "Integer32"
_Hh3cIfLinkModeIndex_Object = MibTableColumn
hh3cIfLinkModeIndex = _Hh3cIfLinkModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3, 1, 1),
    _Hh3cIfLinkModeIndex_Type()
)
hh3cIfLinkModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfLinkModeIndex.setStatus("current")


class _Hh3cIfLinkMode_Type(Integer32):
    """Custom type hh3cIfLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridgeMode", 1),
          ("routeMode", 2))
    )


_Hh3cIfLinkMode_Type.__name__ = "Integer32"
_Hh3cIfLinkMode_Object = MibTableColumn
hh3cIfLinkMode = _Hh3cIfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3, 1, 2),
    _Hh3cIfLinkMode_Type()
)
hh3cIfLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfLinkMode.setStatus("current")
_Hh3cIfLinkModeSwitchSupport_Type = TruthValue
_Hh3cIfLinkModeSwitchSupport_Object = MibTableColumn
hh3cIfLinkModeSwitchSupport = _Hh3cIfLinkModeSwitchSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3, 1, 3),
    _Hh3cIfLinkModeSwitchSupport_Type()
)
hh3cIfLinkModeSwitchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfLinkModeSwitchSupport.setStatus("current")
_Hh3cIfPortTypeTable_Object = MibTable
hh3cIfPortTypeTable = _Hh3cIfPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cIfPortTypeTable.setStatus("current")
_Hh3cIfPortTypeEntry_Object = MibTableRow
hh3cIfPortTypeEntry = _Hh3cIfPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 4, 1)
)
hh3cIfPortTypeEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cIfPortTypeIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfPortTypeEntry.setStatus("current")
_Hh3cIfPortTypeIndex_Type = InterfaceIndex
_Hh3cIfPortTypeIndex_Object = MibTableColumn
hh3cIfPortTypeIndex = _Hh3cIfPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 4, 1, 1),
    _Hh3cIfPortTypeIndex_Type()
)
hh3cIfPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfPortTypeIndex.setStatus("current")


class _Hh3cIfPortType_Type(Integer32):
    """Custom type hh3cIfPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ethernet", 2),
          ("fc", 3))
    )


_Hh3cIfPortType_Type.__name__ = "Integer32"
_Hh3cIfPortType_Object = MibTableColumn
hh3cIfPortType = _Hh3cIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 4, 1, 2),
    _Hh3cIfPortType_Type()
)
hh3cIfPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfPortType.setStatus("current")
_Hh3cIfPfcDot1pTable_Object = MibTable
hh3cIfPfcDot1pTable = _Hh3cIfPfcDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cIfPfcDot1pTable.setStatus("current")
_Hh3cIfPfcDot1pEntry_Object = MibTableRow
hh3cIfPfcDot1pEntry = _Hh3cIfPfcDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 5, 1)
)
hh3cIfPfcDot1pEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IF-EXT-MIB", "hh3cIfPfcDot1pValue"),
)
if mibBuilder.loadTexts:
    hh3cIfPfcDot1pEntry.setStatus("current")


class _Hh3cIfPfcDot1pValue_Type(Integer32):
    """Custom type hh3cIfPfcDot1pValue based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pri0", 1),
          ("pri1", 2),
          ("pri2", 3),
          ("pri3", 4),
          ("pri4", 5),
          ("pri5", 6),
          ("pri6", 7),
          ("pri7", 8))
    )


_Hh3cIfPfcDot1pValue_Type.__name__ = "Integer32"
_Hh3cIfPfcDot1pValue_Object = MibTableColumn
hh3cIfPfcDot1pValue = _Hh3cIfPfcDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 5, 1, 1),
    _Hh3cIfPfcDot1pValue_Type()
)
hh3cIfPfcDot1pValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfPfcDot1pValue.setStatus("current")
_Hh3cIfPfcDot1pInPps_Type = Unsigned32
_Hh3cIfPfcDot1pInPps_Object = MibTableColumn
hh3cIfPfcDot1pInPps = _Hh3cIfPfcDot1pInPps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 5, 1, 2),
    _Hh3cIfPfcDot1pInPps_Type()
)
hh3cIfPfcDot1pInPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfPfcDot1pInPps.setStatus("current")
_Hh3cIfPfcDot1pOutPps_Type = Unsigned32
_Hh3cIfPfcDot1pOutPps_Object = MibTableColumn
hh3cIfPfcDot1pOutPps = _Hh3cIfPfcDot1pOutPps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 5, 1, 3),
    _Hh3cIfPfcDot1pOutPps_Type()
)
hh3cIfPfcDot1pOutPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfPfcDot1pOutPps.setStatus("current")
_Hh3cIfPfcDot1pInPpsThreshold_Type = Unsigned32
_Hh3cIfPfcDot1pInPpsThreshold_Object = MibTableColumn
hh3cIfPfcDot1pInPpsThreshold = _Hh3cIfPfcDot1pInPpsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 5, 1, 4),
    _Hh3cIfPfcDot1pInPpsThreshold_Type()
)
hh3cIfPfcDot1pInPpsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfPfcDot1pInPpsThreshold.setStatus("current")
_Hh3cIfPfcDot1pOutPpsThreshold_Type = Unsigned32
_Hh3cIfPfcDot1pOutPpsThreshold_Object = MibTableColumn
hh3cIfPfcDot1pOutPpsThreshold = _Hh3cIfPfcDot1pOutPpsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 5, 1, 5),
    _Hh3cIfPfcDot1pOutPpsThreshold_Type()
)
hh3cIfPfcDot1pOutPpsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfPfcDot1pOutPpsThreshold.setStatus("current")
_Hh3cIfQueBufferTable_Object = MibTable
hh3cIfQueBufferTable = _Hh3cIfQueBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cIfQueBufferTable.setStatus("current")
_Hh3cIfQueBufferEntry_Object = MibTableRow
hh3cIfQueBufferEntry = _Hh3cIfQueBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1)
)
hh3cIfQueBufferEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IF-EXT-MIB", "hh3cIfQueId"),
)
if mibBuilder.loadTexts:
    hh3cIfQueBufferEntry.setStatus("current")


class _Hh3cIfQueId_Type(Integer32):
    """Custom type hh3cIfQueId based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("que0", 1),
          ("que1", 2),
          ("que2", 3),
          ("que3", 4),
          ("que4", 5),
          ("que5", 6),
          ("que6", 7),
          ("que7", 8))
    )


_Hh3cIfQueId_Type.__name__ = "Integer32"
_Hh3cIfQueId_Object = MibTableColumn
hh3cIfQueId = _Hh3cIfQueId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 1),
    _Hh3cIfQueId_Type()
)
hh3cIfQueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueId.setStatus("current")
_Hh3cIfQueOutUcastTotal_Type = Unsigned32
_Hh3cIfQueOutUcastTotal_Object = MibTableColumn
hh3cIfQueOutUcastTotal = _Hh3cIfQueOutUcastTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 2),
    _Hh3cIfQueOutUcastTotal_Type()
)
hh3cIfQueOutUcastTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueOutUcastTotal.setStatus("current")
_Hh3cIfQueOutUcastFree_Type = Unsigned32
_Hh3cIfQueOutUcastFree_Object = MibTableColumn
hh3cIfQueOutUcastFree = _Hh3cIfQueOutUcastFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 3),
    _Hh3cIfQueOutUcastFree_Type()
)
hh3cIfQueOutUcastFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueOutUcastFree.setStatus("current")
_Hh3cIfQueOutUcastUsedRatio_Type = Unsigned32
_Hh3cIfQueOutUcastUsedRatio_Object = MibTableColumn
hh3cIfQueOutUcastUsedRatio = _Hh3cIfQueOutUcastUsedRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 4),
    _Hh3cIfQueOutUcastUsedRatio_Type()
)
hh3cIfQueOutUcastUsedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueOutUcastUsedRatio.setStatus("current")
_Hh3cIfQueOutUcastUsedPeak_Type = Unsigned32
_Hh3cIfQueOutUcastUsedPeak_Object = MibTableColumn
hh3cIfQueOutUcastUsedPeak = _Hh3cIfQueOutUcastUsedPeak_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 5),
    _Hh3cIfQueOutUcastUsedPeak_Type()
)
hh3cIfQueOutUcastUsedPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueOutUcastUsedPeak.setStatus("current")
_Hh3cIfQueOutUcastThreshold_Type = Unsigned32
_Hh3cIfQueOutUcastThreshold_Object = MibTableColumn
hh3cIfQueOutUcastThreshold = _Hh3cIfQueOutUcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 6),
    _Hh3cIfQueOutUcastThreshold_Type()
)
hh3cIfQueOutUcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQueOutUcastThreshold.setStatus("current")
_Hh3cIfQueOutUcastOverThres_Type = Unsigned32
_Hh3cIfQueOutUcastOverThres_Object = MibTableColumn
hh3cIfQueOutUcastOverThres = _Hh3cIfQueOutUcastOverThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 7),
    _Hh3cIfQueOutUcastOverThres_Type()
)
hh3cIfQueOutUcastOverThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueOutUcastOverThres.setStatus("current")
_Hh3cIfQueInTotal_Type = Unsigned32
_Hh3cIfQueInTotal_Object = MibTableColumn
hh3cIfQueInTotal = _Hh3cIfQueInTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 8),
    _Hh3cIfQueInTotal_Type()
)
hh3cIfQueInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueInTotal.setStatus("current")
_Hh3cIfQueInFree_Type = Unsigned32
_Hh3cIfQueInFree_Object = MibTableColumn
hh3cIfQueInFree = _Hh3cIfQueInFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 9),
    _Hh3cIfQueInFree_Type()
)
hh3cIfQueInFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueInFree.setStatus("current")
_Hh3cIfQueInUsedRatio_Type = Unsigned32
_Hh3cIfQueInUsedRatio_Object = MibTableColumn
hh3cIfQueInUsedRatio = _Hh3cIfQueInUsedRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 10),
    _Hh3cIfQueInUsedRatio_Type()
)
hh3cIfQueInUsedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueInUsedRatio.setStatus("current")
_Hh3cIfQueInUsedPeak_Type = Unsigned32
_Hh3cIfQueInUsedPeak_Object = MibTableColumn
hh3cIfQueInUsedPeak = _Hh3cIfQueInUsedPeak_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 11),
    _Hh3cIfQueInUsedPeak_Type()
)
hh3cIfQueInUsedPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueInUsedPeak.setStatus("current")
_Hh3cIfQueInThreshold_Type = Unsigned32
_Hh3cIfQueInThreshold_Object = MibTableColumn
hh3cIfQueInThreshold = _Hh3cIfQueInThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 12),
    _Hh3cIfQueInThreshold_Type()
)
hh3cIfQueInThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQueInThreshold.setStatus("current")
_Hh3cIfQueInOverThres_Type = Unsigned32
_Hh3cIfQueInOverThres_Object = MibTableColumn
hh3cIfQueInOverThres = _Hh3cIfQueInOverThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 13),
    _Hh3cIfQueInOverThres_Type()
)
hh3cIfQueInOverThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueInOverThres.setStatus("current")
_Hh3cIfQueInHeadRoomTotal_Type = Unsigned32
_Hh3cIfQueInHeadRoomTotal_Object = MibTableColumn
hh3cIfQueInHeadRoomTotal = _Hh3cIfQueInHeadRoomTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 14),
    _Hh3cIfQueInHeadRoomTotal_Type()
)
hh3cIfQueInHeadRoomTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueInHeadRoomTotal.setStatus("current")
_Hh3cIfQueInHeadRoomFree_Type = Unsigned32
_Hh3cIfQueInHeadRoomFree_Object = MibTableColumn
hh3cIfQueInHeadRoomFree = _Hh3cIfQueInHeadRoomFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 15),
    _Hh3cIfQueInHeadRoomFree_Type()
)
hh3cIfQueInHeadRoomFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueInHeadRoomFree.setStatus("current")
_Hh3cIfQueInHeadRoomUsedRatio_Type = Unsigned32
_Hh3cIfQueInHeadRoomUsedRatio_Object = MibTableColumn
hh3cIfQueInHeadRoomUsedRatio = _Hh3cIfQueInHeadRoomUsedRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 16),
    _Hh3cIfQueInHeadRoomUsedRatio_Type()
)
hh3cIfQueInHeadRoomUsedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueInHeadRoomUsedRatio.setStatus("current")
_Hh3cIfQueInHeadRoomUsedPeak_Type = Unsigned32
_Hh3cIfQueInHeadRoomUsedPeak_Object = MibTableColumn
hh3cIfQueInHeadRoomUsedPeak = _Hh3cIfQueInHeadRoomUsedPeak_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 6, 1, 17),
    _Hh3cIfQueInHeadRoomUsedPeak_Type()
)
hh3cIfQueInHeadRoomUsedPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQueInHeadRoomUsedPeak.setStatus("current")
_Hh3cIfInterfaces_ObjectIdentity = ObjectIdentity
hh3cIfInterfaces = _Hh3cIfInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3)
)
_Hh3cIfPhysicalNumber_Type = Integer32
_Hh3cIfPhysicalNumber_Object = MibScalar
hh3cIfPhysicalNumber = _Hh3cIfPhysicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 1),
    _Hh3cIfPhysicalNumber_Type()
)
hh3cIfPhysicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfPhysicalNumber.setStatus("current")
_Hh3cIfTable_Object = MibTable
hh3cIfTable = _Hh3cIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cIfTable.setStatus("current")
_Hh3cIfEntry_Object = MibTableRow
hh3cIfEntry = _Hh3cIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1)
)
hh3cIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfEntry.setStatus("current")
_Hh3cIfUpDownTimes_Type = Integer32
_Hh3cIfUpDownTimes_Object = MibTableColumn
hh3cIfUpDownTimes = _Hh3cIfUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 1),
    _Hh3cIfUpDownTimes_Type()
)
hh3cIfUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfUpDownTimes.setStatus("current")
_Hh3cIfMtu_Type = Integer32
_Hh3cIfMtu_Object = MibTableColumn
hh3cIfMtu = _Hh3cIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 2),
    _Hh3cIfMtu_Type()
)
hh3cIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMtu.setStatus("current")


class _Hh3cIfBandwidthRate_Type(Integer32):
    """Custom type hh3cIfBandwidthRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cIfBandwidthRate_Type.__name__ = "Integer32"
_Hh3cIfBandwidthRate_Object = MibTableColumn
hh3cIfBandwidthRate = _Hh3cIfBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 3),
    _Hh3cIfBandwidthRate_Type()
)
hh3cIfBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfBandwidthRate.setStatus("current")


class _Hh3cIfDiscardPktRate_Type(Integer32):
    """Custom type hh3cIfDiscardPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cIfDiscardPktRate_Type.__name__ = "Integer32"
_Hh3cIfDiscardPktRate_Object = MibTableColumn
hh3cIfDiscardPktRate = _Hh3cIfDiscardPktRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 4),
    _Hh3cIfDiscardPktRate_Type()
)
hh3cIfDiscardPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfDiscardPktRate.setStatus("current")
_Hh3cIfStatusKeepTime_Type = TimeTicks
_Hh3cIfStatusKeepTime_Object = MibTableColumn
hh3cIfStatusKeepTime = _Hh3cIfStatusKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 5),
    _Hh3cIfStatusKeepTime_Type()
)
hh3cIfStatusKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatusKeepTime.setStatus("current")
_Hh3cIfInNUcastPkts_Type = Counter64
_Hh3cIfInNUcastPkts_Object = MibTableColumn
hh3cIfInNUcastPkts = _Hh3cIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 6),
    _Hh3cIfInNUcastPkts_Type()
)
hh3cIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfInNUcastPkts.setStatus("current")
_Hh3cIfOutNUcastPkts_Type = Counter64
_Hh3cIfOutNUcastPkts_Object = MibTableColumn
hh3cIfOutNUcastPkts = _Hh3cIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 7),
    _Hh3cIfOutNUcastPkts_Type()
)
hh3cIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfOutNUcastPkts.setStatus("current")
_Hh3cIfIsPoe_Type = TruthValue
_Hh3cIfIsPoe_Object = MibTableColumn
hh3cIfIsPoe = _Hh3cIfIsPoe_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 8),
    _Hh3cIfIsPoe_Type()
)
hh3cIfIsPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfIsPoe.setStatus("current")


class _Hh3cIfOperStatus_Type(Integer32):
    """Custom type hh3cIfOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("admindown", 4))
    )


_Hh3cIfOperStatus_Type.__name__ = "Integer32"
_Hh3cIfOperStatus_Object = MibTableColumn
hh3cIfOperStatus = _Hh3cIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 9),
    _Hh3cIfOperStatus_Type()
)
hh3cIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfOperStatus.setStatus("current")
_Hh3cIfDownTimes_Type = Integer32
_Hh3cIfDownTimes_Object = MibTableColumn
hh3cIfDownTimes = _Hh3cIfDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 10),
    _Hh3cIfDownTimes_Type()
)
hh3cIfDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfDownTimes.setStatus("current")


class _Hh3cIfPfcStatus_Type(Integer32):
    """Custom type hh3cIfPfcStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("auto", 3))
    )


_Hh3cIfPfcStatus_Type.__name__ = "Integer32"
_Hh3cIfPfcStatus_Object = MibTableColumn
hh3cIfPfcStatus = _Hh3cIfPfcStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 11),
    _Hh3cIfPfcStatus_Type()
)
hh3cIfPfcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfPfcStatus.setStatus("current")


class _Hh3cIfPfcDot1pNoDrop_Type(Bits):
    """Custom type hh3cIfPfcDot1pNoDrop based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("pri0", 0),
          ("pri1", 1),
          ("pri2", 2),
          ("pri3", 3),
          ("pri4", 4),
          ("pri5", 5),
          ("pri6", 6),
          ("pri7", 7))
    )

_Hh3cIfPfcDot1pNoDrop_Type.__name__ = "Bits"
_Hh3cIfPfcDot1pNoDrop_Object = MibTableColumn
hh3cIfPfcDot1pNoDrop = _Hh3cIfPfcDot1pNoDrop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 12),
    _Hh3cIfPfcDot1pNoDrop_Type()
)
hh3cIfPfcDot1pNoDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfPfcDot1pNoDrop.setStatus("current")


class _Hh3cIfDescription_Type(DisplayString):
    """Custom type hh3cIfDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIfDescription_Type.__name__ = "DisplayString"
_Hh3cIfDescription_Object = MibTableColumn
hh3cIfDescription = _Hh3cIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 13),
    _Hh3cIfDescription_Type()
)
hh3cIfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfDescription.setStatus("current")
_Hh3cIfFwdErrDiscards_Type = Unsigned32
_Hh3cIfFwdErrDiscards_Object = MibTableColumn
hh3cIfFwdErrDiscards = _Hh3cIfFwdErrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 14),
    _Hh3cIfFwdErrDiscards_Type()
)
hh3cIfFwdErrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfFwdErrDiscards.setStatus("current")


class _Hh3cIfFiberOrCopper_Type(Integer32):
    """Custom type hh3cIfFiberOrCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("fiber", 1),
          ("copper", 2))
    )


_Hh3cIfFiberOrCopper_Type.__name__ = "Integer32"
_Hh3cIfFiberOrCopper_Object = MibTableColumn
hh3cIfFiberOrCopper = _Hh3cIfFiberOrCopper_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 15),
    _Hh3cIfFiberOrCopper_Type()
)
hh3cIfFiberOrCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfFiberOrCopper.setStatus("current")


class _Hh3cIfTransferMode_Type(Integer32):
    """Custom type hh3cIfTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("wan", 2))
    )


_Hh3cIfTransferMode_Type.__name__ = "Integer32"
_Hh3cIfTransferMode_Object = MibTableColumn
hh3cIfTransferMode = _Hh3cIfTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 16),
    _Hh3cIfTransferMode_Type()
)
hh3cIfTransferMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfTransferMode.setStatus("current")
_Hh3cIfUsingTable_Object = MibTable
hh3cIfUsingTable = _Hh3cIfUsingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cIfUsingTable.setStatus("current")
_Hh3cIfUsingEntry_Object = MibTableRow
hh3cIfUsingEntry = _Hh3cIfUsingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1)
)
hh3cIfUsingEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cIfUsingIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfUsingEntry.setStatus("current")


class _Hh3cIfUsingIndex_Type(Integer32):
    """Custom type hh3cIfUsingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIfUsingIndex_Type.__name__ = "Integer32"
_Hh3cIfUsingIndex_Object = MibTableColumn
hh3cIfUsingIndex = _Hh3cIfUsingIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1, 1),
    _Hh3cIfUsingIndex_Type()
)
hh3cIfUsingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfUsingIndex.setStatus("current")
_Hh3cIfUsingSupportType_Type = Integer32
_Hh3cIfUsingSupportType_Object = MibTableColumn
hh3cIfUsingSupportType = _Hh3cIfUsingSupportType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1, 2),
    _Hh3cIfUsingSupportType_Type()
)
hh3cIfUsingSupportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfUsingSupportType.setStatus("current")


class _Hh3cIfUsingType_Type(Integer32):
    """Custom type hh3cIfUsingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noUsing", 0),
          ("using10GE", 1),
          ("using20GE", 2),
          ("using40GE", 3),
          ("using100GE", 4),
          ("using25GE", 5),
          ("using50GE", 6),
          ("using200GE", 7),
          ("using400GE", 8))
    )


_Hh3cIfUsingType_Type.__name__ = "Integer32"
_Hh3cIfUsingType_Object = MibTableColumn
hh3cIfUsingType = _Hh3cIfUsingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1, 3),
    _Hh3cIfUsingType_Type()
)
hh3cIfUsingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfUsingType.setStatus("current")


class _Hh3cIfUsingStatus_Type(Integer32):
    """Custom type hh3cIfUsingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noUsing", 0),
          ("needReboot", 1))
    )


_Hh3cIfUsingStatus_Type.__name__ = "Integer32"
_Hh3cIfUsingStatus_Object = MibTableColumn
hh3cIfUsingStatus = _Hh3cIfUsingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1, 4),
    _Hh3cIfUsingStatus_Type()
)
hh3cIfUsingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfUsingStatus.setStatus("current")
_Hh3cIfExtTrap_ObjectIdentity = ObjectIdentity
hh3cIfExtTrap = _Hh3cIfExtTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3)
)
_Hh3cIfExtTrapPrex_ObjectIdentity = ObjectIdentity
hh3cIfExtTrapPrex = _Hh3cIfExtTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0)
)
_Hh3cIfExtTrapObject_ObjectIdentity = ObjectIdentity
hh3cIfExtTrapObject = _Hh3cIfExtTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1)
)
_Hh3cIfExtTrapCfgTable_Object = MibTable
hh3cIfExtTrapCfgTable = _Hh3cIfExtTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfExtTrapCfgTable.setStatus("current")
_Hh3cIfExtTrapCfgEntry_Object = MibTableRow
hh3cIfExtTrapCfgEntry = _Hh3cIfExtTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1, 1, 1)
)
hh3cIfExtTrapCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfExtTrapCfgEntry.setStatus("current")


class _Hh3cIfBandwidthUpperLimit_Type(Integer32):
    """Custom type hh3cIfBandwidthUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cIfBandwidthUpperLimit_Type.__name__ = "Integer32"
_Hh3cIfBandwidthUpperLimit_Object = MibTableColumn
hh3cIfBandwidthUpperLimit = _Hh3cIfBandwidthUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1, 1, 1, 1),
    _Hh3cIfBandwidthUpperLimit_Type()
)
hh3cIfBandwidthUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfBandwidthUpperLimit.setStatus("current")


class _Hh3cIfDiscardPktRateUpperLimit_Type(Integer32):
    """Custom type hh3cIfDiscardPktRateUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cIfDiscardPktRateUpperLimit_Type.__name__ = "Integer32"
_Hh3cIfDiscardPktRateUpperLimit_Object = MibTableColumn
hh3cIfDiscardPktRateUpperLimit = _Hh3cIfDiscardPktRateUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1, 1, 1, 2),
    _Hh3cIfDiscardPktRateUpperLimit_Type()
)
hh3cIfDiscardPktRateUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfDiscardPktRateUpperLimit.setStatus("current")
_Hh3cIfMonScalarGroup_ObjectIdentity = ObjectIdentity
hh3cIfMonScalarGroup = _Hh3cIfMonScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 4)
)
_Hh3cIfMonGroup_ObjectIdentity = ObjectIdentity
hh3cIfMonGroup = _Hh3cIfMonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5)
)
_Hh3cIfMonStat_ObjectIdentity = ObjectIdentity
hh3cIfMonStat = _Hh3cIfMonStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1)
)
_Hh3cIfMonStatTable_Object = MibTable
hh3cIfMonStatTable = _Hh3cIfMonStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfMonStatTable.setStatus("current")
_Hh3cIfMonStatEntry_Object = MibTableRow
hh3cIfMonStatEntry = _Hh3cIfMonStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1)
)
hh3cIfMonStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfMonStatEntry.setStatus("current")
_Hh3cIfMonInputUsageStatistics_Type = Unsigned32
_Hh3cIfMonInputUsageStatistics_Object = MibTableColumn
hh3cIfMonInputUsageStatistics = _Hh3cIfMonInputUsageStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 1),
    _Hh3cIfMonInputUsageStatistics_Type()
)
hh3cIfMonInputUsageStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonInputUsageStatistics.setStatus("current")
_Hh3cIfMonOutputUsageStatistics_Type = Unsigned32
_Hh3cIfMonOutputUsageStatistics_Object = MibTableColumn
hh3cIfMonOutputUsageStatistics = _Hh3cIfMonOutputUsageStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 2),
    _Hh3cIfMonOutputUsageStatistics_Type()
)
hh3cIfMonOutputUsageStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonOutputUsageStatistics.setStatus("current")
_Hh3cIfMonInputErrorAlarmStatistics_Type = Counter64
_Hh3cIfMonInputErrorAlarmStatistics_Object = MibTableColumn
hh3cIfMonInputErrorAlarmStatistics = _Hh3cIfMonInputErrorAlarmStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 3),
    _Hh3cIfMonInputErrorAlarmStatistics_Type()
)
hh3cIfMonInputErrorAlarmStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonInputErrorAlarmStatistics.setStatus("current")
_Hh3cIfMonOutputErrorAlarmStatistics_Type = Counter64
_Hh3cIfMonOutputErrorAlarmStatistics_Object = MibTableColumn
hh3cIfMonOutputErrorAlarmStatistics = _Hh3cIfMonOutputErrorAlarmStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 4),
    _Hh3cIfMonOutputErrorAlarmStatistics_Type()
)
hh3cIfMonOutputErrorAlarmStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonOutputErrorAlarmStatistics.setStatus("current")
_Hh3cIfMonSdhErrorStatistics_Type = Counter64
_Hh3cIfMonSdhErrorStatistics_Object = MibTableColumn
hh3cIfMonSdhErrorStatistics = _Hh3cIfMonSdhErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 5),
    _Hh3cIfMonSdhErrorStatistics_Type()
)
hh3cIfMonSdhErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonSdhErrorStatistics.setStatus("current")
_Hh3cIfMonSdhB1ErrorStatistics_Type = Counter64
_Hh3cIfMonSdhB1ErrorStatistics_Object = MibTableColumn
hh3cIfMonSdhB1ErrorStatistics = _Hh3cIfMonSdhB1ErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 6),
    _Hh3cIfMonSdhB1ErrorStatistics_Type()
)
hh3cIfMonSdhB1ErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB1ErrorStatistics.setStatus("current")
_Hh3cIfMonSdhB2ErrorStatistics_Type = Counter64
_Hh3cIfMonSdhB2ErrorStatistics_Object = MibTableColumn
hh3cIfMonSdhB2ErrorStatistics = _Hh3cIfMonSdhB2ErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 7),
    _Hh3cIfMonSdhB2ErrorStatistics_Type()
)
hh3cIfMonSdhB2ErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB2ErrorStatistics.setStatus("current")
_Hh3cIfMonCRCErrorStatistics_Type = Counter64
_Hh3cIfMonCRCErrorStatistics_Object = MibTableColumn
hh3cIfMonCRCErrorStatistics = _Hh3cIfMonCRCErrorStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 8),
    _Hh3cIfMonCRCErrorStatistics_Type()
)
hh3cIfMonCRCErrorStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonCRCErrorStatistics.setStatus("current")
_Hh3cIfMonRxPauseFrameStatistics_Type = Counter64
_Hh3cIfMonRxPauseFrameStatistics_Object = MibTableColumn
hh3cIfMonRxPauseFrameStatistics = _Hh3cIfMonRxPauseFrameStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 9),
    _Hh3cIfMonRxPauseFrameStatistics_Type()
)
hh3cIfMonRxPauseFrameStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonRxPauseFrameStatistics.setStatus("current")
_Hh3cIfMonTxPauseFrameStatistics_Type = Counter64
_Hh3cIfMonTxPauseFrameStatistics_Object = MibTableColumn
hh3cIfMonTxPauseFrameStatistics = _Hh3cIfMonTxPauseFrameStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 10),
    _Hh3cIfMonTxPauseFrameStatistics_Type()
)
hh3cIfMonTxPauseFrameStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonTxPauseFrameStatistics.setStatus("current")
_Hh3cIfMonRuntStatistics_Type = Counter64
_Hh3cIfMonRuntStatistics_Object = MibTableColumn
hh3cIfMonRuntStatistics = _Hh3cIfMonRuntStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 11),
    _Hh3cIfMonRuntStatistics_Type()
)
hh3cIfMonRuntStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonRuntStatistics.setStatus("current")
_Hh3cIfMonGiantStatistics_Type = Counter64
_Hh3cIfMonGiantStatistics_Object = MibTableColumn
hh3cIfMonGiantStatistics = _Hh3cIfMonGiantStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 1, 1, 1, 12),
    _Hh3cIfMonGiantStatistics_Type()
)
hh3cIfMonGiantStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfMonGiantStatistics.setStatus("current")
_Hh3cIfMonControl_ObjectIdentity = ObjectIdentity
hh3cIfMonControl = _Hh3cIfMonControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2)
)
_Hh3cIfMonThresholdTable_Object = MibTable
hh3cIfMonThresholdTable = _Hh3cIfMonThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfMonThresholdTable.setStatus("current")
_Hh3cIfMonThresholdEntry_Object = MibTableRow
hh3cIfMonThresholdEntry = _Hh3cIfMonThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1)
)
hh3cIfMonThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfMonThresholdEntry.setStatus("current")


class _Hh3cIfMonInputUsageLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonInputUsageLowThres based on Unsigned32"""
    defaultValue = 80


_Hh3cIfMonInputUsageLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonInputUsageLowThres_Object = MibTableColumn
hh3cIfMonInputUsageLowThres = _Hh3cIfMonInputUsageLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 1),
    _Hh3cIfMonInputUsageLowThres_Type()
)
hh3cIfMonInputUsageLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonInputUsageLowThres.setStatus("current")


class _Hh3cIfMonInputUsageHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonInputUsageHighThres based on Unsigned32"""
    defaultValue = 90


_Hh3cIfMonInputUsageHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonInputUsageHighThres_Object = MibTableColumn
hh3cIfMonInputUsageHighThres = _Hh3cIfMonInputUsageHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 2),
    _Hh3cIfMonInputUsageHighThres_Type()
)
hh3cIfMonInputUsageHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonInputUsageHighThres.setStatus("current")


class _Hh3cIfMonOutputUsageLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonOutputUsageLowThres based on Unsigned32"""
    defaultValue = 80


_Hh3cIfMonOutputUsageLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonOutputUsageLowThres_Object = MibTableColumn
hh3cIfMonOutputUsageLowThres = _Hh3cIfMonOutputUsageLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 3),
    _Hh3cIfMonOutputUsageLowThres_Type()
)
hh3cIfMonOutputUsageLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonOutputUsageLowThres.setStatus("current")


class _Hh3cIfMonOutputUsageHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonOutputUsageHighThres based on Unsigned32"""
    defaultValue = 90


_Hh3cIfMonOutputUsageHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonOutputUsageHighThres_Object = MibTableColumn
hh3cIfMonOutputUsageHighThres = _Hh3cIfMonOutputUsageHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 4),
    _Hh3cIfMonOutputUsageHighThres_Type()
)
hh3cIfMonOutputUsageHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonOutputUsageHighThres.setStatus("current")


class _Hh3cIfMonInputErrorAlarmLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonInputErrorAlarmLowThres based on Unsigned32"""
    defaultValue = 100


_Hh3cIfMonInputErrorAlarmLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonInputErrorAlarmLowThres_Object = MibTableColumn
hh3cIfMonInputErrorAlarmLowThres = _Hh3cIfMonInputErrorAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 5),
    _Hh3cIfMonInputErrorAlarmLowThres_Type()
)
hh3cIfMonInputErrorAlarmLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonInputErrorAlarmLowThres.setStatus("current")


class _Hh3cIfMonInputErrorAlarmHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonInputErrorAlarmHighThres based on Unsigned32"""
    defaultValue = 1000


_Hh3cIfMonInputErrorAlarmHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonInputErrorAlarmHighThres_Object = MibTableColumn
hh3cIfMonInputErrorAlarmHighThres = _Hh3cIfMonInputErrorAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 6),
    _Hh3cIfMonInputErrorAlarmHighThres_Type()
)
hh3cIfMonInputErrorAlarmHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonInputErrorAlarmHighThres.setStatus("current")


class _Hh3cIfMonInputErrorAlarmInterval_Type(Unsigned32):
    """Custom type hh3cIfMonInputErrorAlarmInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonInputErrorAlarmInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonInputErrorAlarmInterval_Object = MibTableColumn
hh3cIfMonInputErrorAlarmInterval = _Hh3cIfMonInputErrorAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 7),
    _Hh3cIfMonInputErrorAlarmInterval_Type()
)
hh3cIfMonInputErrorAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonInputErrorAlarmInterval.setStatus("current")


class _Hh3cIfMonOutputErrorAlarmLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonOutputErrorAlarmLowThres based on Unsigned32"""
    defaultValue = 100


_Hh3cIfMonOutputErrorAlarmLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonOutputErrorAlarmLowThres_Object = MibTableColumn
hh3cIfMonOutputErrorAlarmLowThres = _Hh3cIfMonOutputErrorAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 8),
    _Hh3cIfMonOutputErrorAlarmLowThres_Type()
)
hh3cIfMonOutputErrorAlarmLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonOutputErrorAlarmLowThres.setStatus("current")


class _Hh3cIfMonOutputErrorAlarmHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonOutputErrorAlarmHighThres based on Unsigned32"""
    defaultValue = 1000


_Hh3cIfMonOutputErrorAlarmHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonOutputErrorAlarmHighThres_Object = MibTableColumn
hh3cIfMonOutputErrorAlarmHighThres = _Hh3cIfMonOutputErrorAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 9),
    _Hh3cIfMonOutputErrorAlarmHighThres_Type()
)
hh3cIfMonOutputErrorAlarmHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonOutputErrorAlarmHighThres.setStatus("current")


class _Hh3cIfMonOutputErrorAlarmInterval_Type(Unsigned32):
    """Custom type hh3cIfMonOutputErrorAlarmInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonOutputErrorAlarmInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonOutputErrorAlarmInterval_Object = MibTableColumn
hh3cIfMonOutputErrorAlarmInterval = _Hh3cIfMonOutputErrorAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 10),
    _Hh3cIfMonOutputErrorAlarmInterval_Type()
)
hh3cIfMonOutputErrorAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonOutputErrorAlarmInterval.setStatus("current")


class _Hh3cIfMonSdhErrorLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonSdhErrorLowThres based on Unsigned32"""
    defaultValue = 100


_Hh3cIfMonSdhErrorLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonSdhErrorLowThres_Object = MibTableColumn
hh3cIfMonSdhErrorLowThres = _Hh3cIfMonSdhErrorLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 11),
    _Hh3cIfMonSdhErrorLowThres_Type()
)
hh3cIfMonSdhErrorLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhErrorLowThres.setStatus("current")


class _Hh3cIfMonSdhErrorHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonSdhErrorHighThres based on Unsigned32"""
    defaultValue = 1000


_Hh3cIfMonSdhErrorHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonSdhErrorHighThres_Object = MibTableColumn
hh3cIfMonSdhErrorHighThres = _Hh3cIfMonSdhErrorHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 12),
    _Hh3cIfMonSdhErrorHighThres_Type()
)
hh3cIfMonSdhErrorHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhErrorHighThres.setStatus("current")


class _Hh3cIfMonSdhErrorInterval_Type(Unsigned32):
    """Custom type hh3cIfMonSdhErrorInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonSdhErrorInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonSdhErrorInterval_Object = MibTableColumn
hh3cIfMonSdhErrorInterval = _Hh3cIfMonSdhErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 13),
    _Hh3cIfMonSdhErrorInterval_Type()
)
hh3cIfMonSdhErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhErrorInterval.setStatus("current")


class _Hh3cIfMonSdhB1ErrorLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonSdhB1ErrorLowThres based on Unsigned32"""
    defaultValue = 100


_Hh3cIfMonSdhB1ErrorLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonSdhB1ErrorLowThres_Object = MibTableColumn
hh3cIfMonSdhB1ErrorLowThres = _Hh3cIfMonSdhB1ErrorLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 14),
    _Hh3cIfMonSdhB1ErrorLowThres_Type()
)
hh3cIfMonSdhB1ErrorLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB1ErrorLowThres.setStatus("current")


class _Hh3cIfMonSdhB1ErrorHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonSdhB1ErrorHighThres based on Unsigned32"""
    defaultValue = 1000


_Hh3cIfMonSdhB1ErrorHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonSdhB1ErrorHighThres_Object = MibTableColumn
hh3cIfMonSdhB1ErrorHighThres = _Hh3cIfMonSdhB1ErrorHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 15),
    _Hh3cIfMonSdhB1ErrorHighThres_Type()
)
hh3cIfMonSdhB1ErrorHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB1ErrorHighThres.setStatus("current")


class _Hh3cIfMonSdhB1ErrorInterval_Type(Unsigned32):
    """Custom type hh3cIfMonSdhB1ErrorInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonSdhB1ErrorInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonSdhB1ErrorInterval_Object = MibTableColumn
hh3cIfMonSdhB1ErrorInterval = _Hh3cIfMonSdhB1ErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 16),
    _Hh3cIfMonSdhB1ErrorInterval_Type()
)
hh3cIfMonSdhB1ErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB1ErrorInterval.setStatus("current")


class _Hh3cIfMonSdhB2ErrorLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonSdhB2ErrorLowThres based on Unsigned32"""
    defaultValue = 100


_Hh3cIfMonSdhB2ErrorLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonSdhB2ErrorLowThres_Object = MibTableColumn
hh3cIfMonSdhB2ErrorLowThres = _Hh3cIfMonSdhB2ErrorLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 17),
    _Hh3cIfMonSdhB2ErrorLowThres_Type()
)
hh3cIfMonSdhB2ErrorLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB2ErrorLowThres.setStatus("current")


class _Hh3cIfMonSdhB2ErrorHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonSdhB2ErrorHighThres based on Unsigned32"""
    defaultValue = 1000


_Hh3cIfMonSdhB2ErrorHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonSdhB2ErrorHighThres_Object = MibTableColumn
hh3cIfMonSdhB2ErrorHighThres = _Hh3cIfMonSdhB2ErrorHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 18),
    _Hh3cIfMonSdhB2ErrorHighThres_Type()
)
hh3cIfMonSdhB2ErrorHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB2ErrorHighThres.setStatus("current")


class _Hh3cIfMonSdhB2ErrorInterval_Type(Unsigned32):
    """Custom type hh3cIfMonSdhB2ErrorInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonSdhB2ErrorInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonSdhB2ErrorInterval_Object = MibTableColumn
hh3cIfMonSdhB2ErrorInterval = _Hh3cIfMonSdhB2ErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 19),
    _Hh3cIfMonSdhB2ErrorInterval_Type()
)
hh3cIfMonSdhB2ErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB2ErrorInterval.setStatus("current")
_Hh3cIfMonCRCErrorLowThres_Type = Unsigned32
_Hh3cIfMonCRCErrorLowThres_Object = MibTableColumn
hh3cIfMonCRCErrorLowThres = _Hh3cIfMonCRCErrorLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 20),
    _Hh3cIfMonCRCErrorLowThres_Type()
)
hh3cIfMonCRCErrorLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonCRCErrorLowThres.setStatus("current")
_Hh3cIfMonCRCErrorHighThres_Type = Unsigned32
_Hh3cIfMonCRCErrorHighThres_Object = MibTableColumn
hh3cIfMonCRCErrorHighThres = _Hh3cIfMonCRCErrorHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 21),
    _Hh3cIfMonCRCErrorHighThres_Type()
)
hh3cIfMonCRCErrorHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonCRCErrorHighThres.setStatus("current")


class _Hh3cIfMonCRCErrorInterval_Type(Unsigned32):
    """Custom type hh3cIfMonCRCErrorInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonCRCErrorInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonCRCErrorInterval_Object = MibTableColumn
hh3cIfMonCRCErrorInterval = _Hh3cIfMonCRCErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 22),
    _Hh3cIfMonCRCErrorInterval_Type()
)
hh3cIfMonCRCErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonCRCErrorInterval.setStatus("current")


class _Hh3cIfMonCRCErrType_Type(Integer32):
    """Custom type hh3cIfMonCRCErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("ratio", 2),
          ("invalid", 65535))
    )


_Hh3cIfMonCRCErrType_Type.__name__ = "Integer32"
_Hh3cIfMonCRCErrType_Object = MibTableColumn
hh3cIfMonCRCErrType = _Hh3cIfMonCRCErrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 23),
    _Hh3cIfMonCRCErrType_Type()
)
hh3cIfMonCRCErrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonCRCErrType.setStatus("current")


class _Hh3cIfMonRxPauseFrameLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonRxPauseFrameLowThres based on Unsigned32"""
    defaultValue = 100


_Hh3cIfMonRxPauseFrameLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonRxPauseFrameLowThres_Object = MibTableColumn
hh3cIfMonRxPauseFrameLowThres = _Hh3cIfMonRxPauseFrameLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 24),
    _Hh3cIfMonRxPauseFrameLowThres_Type()
)
hh3cIfMonRxPauseFrameLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonRxPauseFrameLowThres.setStatus("current")


class _Hh3cIfMonRxPauseFrameHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonRxPauseFrameHighThres based on Unsigned32"""
    defaultValue = 500


_Hh3cIfMonRxPauseFrameHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonRxPauseFrameHighThres_Object = MibTableColumn
hh3cIfMonRxPauseFrameHighThres = _Hh3cIfMonRxPauseFrameHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 25),
    _Hh3cIfMonRxPauseFrameHighThres_Type()
)
hh3cIfMonRxPauseFrameHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonRxPauseFrameHighThres.setStatus("current")


class _Hh3cIfMonRxPauseFrameInterval_Type(Unsigned32):
    """Custom type hh3cIfMonRxPauseFrameInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonRxPauseFrameInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonRxPauseFrameInterval_Object = MibTableColumn
hh3cIfMonRxPauseFrameInterval = _Hh3cIfMonRxPauseFrameInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 26),
    _Hh3cIfMonRxPauseFrameInterval_Type()
)
hh3cIfMonRxPauseFrameInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonRxPauseFrameInterval.setStatus("current")


class _Hh3cIfMonTxPauseFrameLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonTxPauseFrameLowThres based on Unsigned32"""
    defaultValue = 100


_Hh3cIfMonTxPauseFrameLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonTxPauseFrameLowThres_Object = MibTableColumn
hh3cIfMonTxPauseFrameLowThres = _Hh3cIfMonTxPauseFrameLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 27),
    _Hh3cIfMonTxPauseFrameLowThres_Type()
)
hh3cIfMonTxPauseFrameLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonTxPauseFrameLowThres.setStatus("current")


class _Hh3cIfMonTxPauseFrameHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonTxPauseFrameHighThres based on Unsigned32"""
    defaultValue = 500


_Hh3cIfMonTxPauseFrameHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonTxPauseFrameHighThres_Object = MibTableColumn
hh3cIfMonTxPauseFrameHighThres = _Hh3cIfMonTxPauseFrameHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 28),
    _Hh3cIfMonTxPauseFrameHighThres_Type()
)
hh3cIfMonTxPauseFrameHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonTxPauseFrameHighThres.setStatus("current")


class _Hh3cIfMonTxPauseFrameInterval_Type(Unsigned32):
    """Custom type hh3cIfMonTxPauseFrameInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonTxPauseFrameInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonTxPauseFrameInterval_Object = MibTableColumn
hh3cIfMonTxPauseFrameInterval = _Hh3cIfMonTxPauseFrameInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 29),
    _Hh3cIfMonTxPauseFrameInterval_Type()
)
hh3cIfMonTxPauseFrameInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonTxPauseFrameInterval.setStatus("current")


class _Hh3cIfMonGiantLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonGiantLowThres based on Unsigned32"""
    defaultValue = 100


_Hh3cIfMonGiantLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonGiantLowThres_Object = MibTableColumn
hh3cIfMonGiantLowThres = _Hh3cIfMonGiantLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 30),
    _Hh3cIfMonGiantLowThres_Type()
)
hh3cIfMonGiantLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonGiantLowThres.setStatus("current")


class _Hh3cIfMonGiantHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonGiantHighThres based on Unsigned32"""
    defaultValue = 1000


_Hh3cIfMonGiantHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonGiantHighThres_Object = MibTableColumn
hh3cIfMonGiantHighThres = _Hh3cIfMonGiantHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 31),
    _Hh3cIfMonGiantHighThres_Type()
)
hh3cIfMonGiantHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonGiantHighThres.setStatus("current")


class _Hh3cIfMonGiantInterval_Type(Unsigned32):
    """Custom type hh3cIfMonGiantInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonGiantInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonGiantInterval_Object = MibTableColumn
hh3cIfMonGiantInterval = _Hh3cIfMonGiantInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 32),
    _Hh3cIfMonGiantInterval_Type()
)
hh3cIfMonGiantInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonGiantInterval.setStatus("current")


class _Hh3cIfMonRuntLowThres_Type(Unsigned32):
    """Custom type hh3cIfMonRuntLowThres based on Unsigned32"""
    defaultValue = 100


_Hh3cIfMonRuntLowThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonRuntLowThres_Object = MibTableColumn
hh3cIfMonRuntLowThres = _Hh3cIfMonRuntLowThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 33),
    _Hh3cIfMonRuntLowThres_Type()
)
hh3cIfMonRuntLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonRuntLowThres.setStatus("current")


class _Hh3cIfMonRuntHighThres_Type(Unsigned32):
    """Custom type hh3cIfMonRuntHighThres based on Unsigned32"""
    defaultValue = 1000


_Hh3cIfMonRuntHighThres_Type.__name__ = "Unsigned32"
_Hh3cIfMonRuntHighThres_Object = MibTableColumn
hh3cIfMonRuntHighThres = _Hh3cIfMonRuntHighThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 34),
    _Hh3cIfMonRuntHighThres_Type()
)
hh3cIfMonRuntHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonRuntHighThres.setStatus("current")


class _Hh3cIfMonRuntInterval_Type(Unsigned32):
    """Custom type hh3cIfMonRuntInterval based on Unsigned32"""
    defaultValue = 10


_Hh3cIfMonRuntInterval_Type.__name__ = "Unsigned32"
_Hh3cIfMonRuntInterval_Object = MibTableColumn
hh3cIfMonRuntInterval = _Hh3cIfMonRuntInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 1, 1, 35),
    _Hh3cIfMonRuntInterval_Type()
)
hh3cIfMonRuntInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonRuntInterval.setStatus("current")
_Hh3cIfMonAlarmDownEnableTable_Object = MibTable
hh3cIfMonAlarmDownEnableTable = _Hh3cIfMonAlarmDownEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cIfMonAlarmDownEnableTable.setStatus("current")
_Hh3cIfMonAlarmDownEnableEntry_Object = MibTableRow
hh3cIfMonAlarmDownEnableEntry = _Hh3cIfMonAlarmDownEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2, 1)
)
hh3cIfMonAlarmDownEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfMonAlarmDownEnableEntry.setStatus("current")


class _Hh3cIfMonInputErrorAlarmEnableDown_Type(TruthValue):
    """Custom type hh3cIfMonInputErrorAlarmEnableDown based on TruthValue"""
    defaultValue = 2


_Hh3cIfMonInputErrorAlarmEnableDown_Type.__name__ = "TruthValue"
_Hh3cIfMonInputErrorAlarmEnableDown_Object = MibTableColumn
hh3cIfMonInputErrorAlarmEnableDown = _Hh3cIfMonInputErrorAlarmEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2, 1, 1),
    _Hh3cIfMonInputErrorAlarmEnableDown_Type()
)
hh3cIfMonInputErrorAlarmEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonInputErrorAlarmEnableDown.setStatus("current")


class _Hh3cIfMonOutputErrorAlarmEnableDown_Type(TruthValue):
    """Custom type hh3cIfMonOutputErrorAlarmEnableDown based on TruthValue"""
    defaultValue = 2


_Hh3cIfMonOutputErrorAlarmEnableDown_Type.__name__ = "TruthValue"
_Hh3cIfMonOutputErrorAlarmEnableDown_Object = MibTableColumn
hh3cIfMonOutputErrorAlarmEnableDown = _Hh3cIfMonOutputErrorAlarmEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2, 1, 2),
    _Hh3cIfMonOutputErrorAlarmEnableDown_Type()
)
hh3cIfMonOutputErrorAlarmEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonOutputErrorAlarmEnableDown.setStatus("current")


class _Hh3cIfMonSdhErrorEnableDown_Type(TruthValue):
    """Custom type hh3cIfMonSdhErrorEnableDown based on TruthValue"""
    defaultValue = 2


_Hh3cIfMonSdhErrorEnableDown_Type.__name__ = "TruthValue"
_Hh3cIfMonSdhErrorEnableDown_Object = MibTableColumn
hh3cIfMonSdhErrorEnableDown = _Hh3cIfMonSdhErrorEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2, 1, 3),
    _Hh3cIfMonSdhErrorEnableDown_Type()
)
hh3cIfMonSdhErrorEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhErrorEnableDown.setStatus("current")


class _Hh3cIfMonSdhB1ErrorEnableDown_Type(TruthValue):
    """Custom type hh3cIfMonSdhB1ErrorEnableDown based on TruthValue"""
    defaultValue = 2


_Hh3cIfMonSdhB1ErrorEnableDown_Type.__name__ = "TruthValue"
_Hh3cIfMonSdhB1ErrorEnableDown_Object = MibTableColumn
hh3cIfMonSdhB1ErrorEnableDown = _Hh3cIfMonSdhB1ErrorEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2, 1, 4),
    _Hh3cIfMonSdhB1ErrorEnableDown_Type()
)
hh3cIfMonSdhB1ErrorEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB1ErrorEnableDown.setStatus("current")


class _Hh3cIfMonSdhB2ErrorEnableDown_Type(TruthValue):
    """Custom type hh3cIfMonSdhB2ErrorEnableDown based on TruthValue"""
    defaultValue = 2


_Hh3cIfMonSdhB2ErrorEnableDown_Type.__name__ = "TruthValue"
_Hh3cIfMonSdhB2ErrorEnableDown_Object = MibTableColumn
hh3cIfMonSdhB2ErrorEnableDown = _Hh3cIfMonSdhB2ErrorEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2, 1, 5),
    _Hh3cIfMonSdhB2ErrorEnableDown_Type()
)
hh3cIfMonSdhB2ErrorEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonSdhB2ErrorEnableDown.setStatus("current")


class _Hh3cIfMonCRCErrorEnableDown_Type(TruthValue):
    """Custom type hh3cIfMonCRCErrorEnableDown based on TruthValue"""
    defaultValue = 2


_Hh3cIfMonCRCErrorEnableDown_Type.__name__ = "TruthValue"
_Hh3cIfMonCRCErrorEnableDown_Object = MibTableColumn
hh3cIfMonCRCErrorEnableDown = _Hh3cIfMonCRCErrorEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2, 1, 6),
    _Hh3cIfMonCRCErrorEnableDown_Type()
)
hh3cIfMonCRCErrorEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonCRCErrorEnableDown.setStatus("current")


class _Hh3cIfMonGiantEnableDown_Type(TruthValue):
    """Custom type hh3cIfMonGiantEnableDown based on TruthValue"""
    defaultValue = 2


_Hh3cIfMonGiantEnableDown_Type.__name__ = "TruthValue"
_Hh3cIfMonGiantEnableDown_Object = MibTableColumn
hh3cIfMonGiantEnableDown = _Hh3cIfMonGiantEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2, 1, 7),
    _Hh3cIfMonGiantEnableDown_Type()
)
hh3cIfMonGiantEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonGiantEnableDown.setStatus("current")


class _Hh3cIfMonRuntEnableDown_Type(TruthValue):
    """Custom type hh3cIfMonRuntEnableDown based on TruthValue"""
    defaultValue = 2


_Hh3cIfMonRuntEnableDown_Type.__name__ = "TruthValue"
_Hh3cIfMonRuntEnableDown_Object = MibTableColumn
hh3cIfMonRuntEnableDown = _Hh3cIfMonRuntEnableDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 5, 2, 2, 1, 8),
    _Hh3cIfMonRuntEnableDown_Type()
)
hh3cIfMonRuntEnableDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMonRuntEnableDown.setStatus("current")
_Hh3cIfMonTrap_ObjectIdentity = ObjectIdentity
hh3cIfMonTrap = _Hh3cIfMonTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6)
)
_Hh3cIfMonTrapPrex_ObjectIdentity = ObjectIdentity
hh3cIfMonTrapPrex = _Hh3cIfMonTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0)
)
_Hh3cIfMonTrapObject_ObjectIdentity = ObjectIdentity
hh3cIfMonTrapObject = _Hh3cIfMonTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 1)
)

# Managed Objects groups


# Notification objects

hh3cIfBandwidthUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 1)
)
hh3cIfBandwidthUsageHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfBandwidthRate"),
        ("HH3C-IF-EXT-MIB", "hh3cIfBandwidthUpperLimit"))
)
if mibBuilder.loadTexts:
    hh3cIfBandwidthUsageHigh.setStatus(
        "current"
    )

hh3cIfDiscardPktRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 2)
)
hh3cIfDiscardPktRateHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfDiscardPktRate"),
        ("HH3C-IF-EXT-MIB", "hh3cIfDiscardPktRateUpperLimit"))
)
if mibBuilder.loadTexts:
    hh3cIfDiscardPktRateHigh.setStatus(
        "current"
    )

hh3cIfDampeningSuppressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 3)
)
hh3cIfDampeningSuppressed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cIfDampeningSuppressed.setStatus(
        "current"
    )

hh3cIfDampeningNotSuppressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 4)
)
hh3cIfDampeningNotSuppressed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cIfDampeningNotSuppressed.setStatus(
        "current"
    )

hh3cIfPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 5)
)
hh3cIfPortUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cIfPortUp.setStatus(
        "current"
    )

hh3cIfPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 6)
)
hh3cIfPortDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cIfPortDown.setStatus(
        "current"
    )

hh3cIfPfcOutRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 7)
)
hh3cIfPfcOutRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfPfcDot1pValue"),
        ("HH3C-IF-EXT-MIB", "hh3cIfPfcDot1pOutPps"),
        ("HH3C-IF-EXT-MIB", "hh3cIfPfcDot1pOutPpsThreshold"))
)
if mibBuilder.loadTexts:
    hh3cIfPfcOutRising.setStatus(
        "current"
    )

hh3cIfPfcInRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 8)
)
hh3cIfPfcInRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfPfcDot1pValue"),
        ("HH3C-IF-EXT-MIB", "hh3cIfPfcDot1pInPps"),
        ("HH3C-IF-EXT-MIB", "hh3cIfPfcDot1pInPpsThreshold"))
)
if mibBuilder.loadTexts:
    hh3cIfPfcInRising.setStatus(
        "current"
    )

hh3cIfMonInputUsageRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 1)
)
hh3cIfMonInputUsageRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputUsageLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputUsageHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputUsageStatistics"))
)
if mibBuilder.loadTexts:
    hh3cIfMonInputUsageRising.setStatus(
        "current"
    )

hh3cIfMonInputUsageResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 2)
)
hh3cIfMonInputUsageResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputUsageLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputUsageHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputUsageStatistics"))
)
if mibBuilder.loadTexts:
    hh3cIfMonInputUsageResume.setStatus(
        "current"
    )

hh3cIfMonOutputUsageRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 3)
)
hh3cIfMonOutputUsageRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputUsageLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputUsageHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputUsageStatistics"))
)
if mibBuilder.loadTexts:
    hh3cIfMonOutputUsageRising.setStatus(
        "current"
    )

hh3cIfMonOutputUsageResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 4)
)
hh3cIfMonOutputUsageResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputUsageLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputUsageHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputUsageStatistics"))
)
if mibBuilder.loadTexts:
    hh3cIfMonOutputUsageResume.setStatus(
        "current"
    )

hh3cIfMonInputErrorAlarmRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 5)
)
hh3cIfMonInputErrorAlarmRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputErrorAlarmHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputErrorAlarmLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputErrorAlarmStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputErrorAlarmInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonInputErrorAlarmRising.setStatus(
        "current"
    )

hh3cIfMonInputErrorAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 6)
)
hh3cIfMonInputErrorAlarmResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputErrorAlarmHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputErrorAlarmLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputErrorAlarmStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonInputErrorAlarmInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonInputErrorAlarmResume.setStatus(
        "current"
    )

hh3cIfMonOutputErrorAlarmRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 7)
)
hh3cIfMonOutputErrorAlarmRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputErrorAlarmHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputErrorAlarmLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputErrorAlarmStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputErrorAlarmInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonOutputErrorAlarmRising.setStatus(
        "current"
    )

hh3cIfMonOutputErrorAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 8)
)
hh3cIfMonOutputErrorAlarmResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputErrorAlarmHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputErrorAlarmLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputErrorAlarmStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonOutputErrorAlarmInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonOutputErrorAlarmResume.setStatus(
        "current"
    )

hh3cIfMonSdhErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 9)
)
hh3cIfMonSdhErrorRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhErrorLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhErrorHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhErrorStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhErrorInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonSdhErrorRising.setStatus(
        "current"
    )

hh3cIfMonSdhErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 10)
)
hh3cIfMonSdhErrorResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhErrorLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhErrorHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhErrorStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhErrorInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonSdhErrorResume.setStatus(
        "current"
    )

hh3cIfMonSdhB1ErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 11)
)
hh3cIfMonSdhB1ErrorRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB1ErrorLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB1ErrorHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB1ErrorStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB1ErrorInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonSdhB1ErrorRising.setStatus(
        "current"
    )

hh3cIfMonSdhB1ErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 12)
)
hh3cIfMonSdhB1ErrorResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB1ErrorLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB1ErrorHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB1ErrorStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB1ErrorInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonSdhB1ErrorResume.setStatus(
        "current"
    )

hh3cIfMonSdhB2ErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 13)
)
hh3cIfMonSdhB2ErrorRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB2ErrorLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB2ErrorHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB2ErrorStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB2ErrorInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonSdhB2ErrorRising.setStatus(
        "current"
    )

hh3cIfMonSdhB2ErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 14)
)
hh3cIfMonSdhB2ErrorResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB2ErrorLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB2ErrorHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB2ErrorStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonSdhB2ErrorInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonSdhB2ErrorResume.setStatus(
        "current"
    )

hh3cIfMonCRCErrorRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 15)
)
hh3cIfMonCRCErrorRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrorHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrorLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrorStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrorInterval"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrType"))
)
if mibBuilder.loadTexts:
    hh3cIfMonCRCErrorRising.setStatus(
        "current"
    )

hh3cIfMonCRCErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 16)
)
hh3cIfMonCRCErrorResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrorHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrorLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrorStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrorInterval"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonCRCErrType"))
)
if mibBuilder.loadTexts:
    hh3cIfMonCRCErrorResume.setStatus(
        "current"
    )

hh3cIfMonRxPauseFrameRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 17)
)
hh3cIfMonRxPauseFrameRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRxPauseFrameHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRxPauseFrameLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRxPauseFrameStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRxPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonRxPauseFrameRising.setStatus(
        "current"
    )

hh3cIfMonRxPauseFrameResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 18)
)
hh3cIfMonRxPauseFrameResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRxPauseFrameHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRxPauseFrameLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRxPauseFrameStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRxPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonRxPauseFrameResume.setStatus(
        "current"
    )

hh3cIfMonTxPauseFrameRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 19)
)
hh3cIfMonTxPauseFrameRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonTxPauseFrameHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonTxPauseFrameLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonTxPauseFrameStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonTxPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonTxPauseFrameRising.setStatus(
        "current"
    )

hh3cIfMonTxPauseFrameResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 20)
)
hh3cIfMonTxPauseFrameResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonTxPauseFrameHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonTxPauseFrameLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonTxPauseFrameStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonTxPauseFrameInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonTxPauseFrameResume.setStatus(
        "current"
    )

hh3cIfMonGiantRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 21)
)
hh3cIfMonGiantRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonGiantLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonGiantHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonGiantStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonGiantInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonGiantRising.setStatus(
        "current"
    )

hh3cIfMonGiantResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 22)
)
hh3cIfMonGiantResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonGiantLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonGiantHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonGiantStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonGiantInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonGiantResume.setStatus(
        "current"
    )

hh3cIfMonRuntRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 23)
)
hh3cIfMonRuntRising.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRuntLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRuntHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRuntStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRuntInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonRuntRising.setStatus(
        "current"
    )

hh3cIfMonRuntResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 6, 0, 24)
)
hh3cIfMonRuntResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRuntLowThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRuntHighThres"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRuntStatistics"),
        ("HH3C-IF-EXT-MIB", "hh3cIfMonRuntInterval"))
)
if mibBuilder.loadTexts:
    hh3cIfMonRuntResume.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IF-EXT-MIB",
    **{"hh3cIfExt": hh3cIfExt,
       "hh3cIfExtScalarGroup": hh3cIfExtScalarGroup,
       "hh3cIfStatGlobalFlowInterval": hh3cIfStatGlobalFlowInterval,
       "hh3cIfShutDownInterval": hh3cIfShutDownInterval,
       "hh3cIfThroughputInKbps": hh3cIfThroughputInKbps,
       "hh3cIfThroughputOutKbps": hh3cIfThroughputOutKbps,
       "hh3cIfExtGroup": hh3cIfExtGroup,
       "hh3cIfStat": hh3cIfStat,
       "hh3cIfStatScalarGroup": hh3cIfStatScalarGroup,
       "hh3cIfStatTable": hh3cIfStatTable,
       "hh3cIfFlowStatTable": hh3cIfFlowStatTable,
       "hh3cIfFlowStatEntry": hh3cIfFlowStatEntry,
       "hh3cIfStatFlowInterval": hh3cIfStatFlowInterval,
       "hh3cIfStatFlowInBits": hh3cIfStatFlowInBits,
       "hh3cIfStatFlowOutBits": hh3cIfStatFlowOutBits,
       "hh3cIfStatFlowInPkts": hh3cIfStatFlowInPkts,
       "hh3cIfStatFlowOutPkts": hh3cIfStatFlowOutPkts,
       "hh3cIfStatFlowInBytes": hh3cIfStatFlowInBytes,
       "hh3cIfStatFlowOutBytes": hh3cIfStatFlowOutBytes,
       "hh3cIfSpeedStatTable": hh3cIfSpeedStatTable,
       "hh3cIfSpeedStatEntry": hh3cIfSpeedStatEntry,
       "hh3cIfSpeedStatInterval": hh3cIfSpeedStatInterval,
       "hh3cIfSpeedStatInPkts": hh3cIfSpeedStatInPkts,
       "hh3cIfSpeedStatOutPkts": hh3cIfSpeedStatOutPkts,
       "hh3cIfSpeedStatInBytes": hh3cIfSpeedStatInBytes,
       "hh3cIfSpeedStatOutBytes": hh3cIfSpeedStatOutBytes,
       "hh3cIfSpeedStatInBits": hh3cIfSpeedStatInBits,
       "hh3cIfSpeedStatOutBits": hh3cIfSpeedStatOutBits,
       "hh3cIfHCFlowStatTable": hh3cIfHCFlowStatTable,
       "hh3cIfHCFlowStatEntry": hh3cIfHCFlowStatEntry,
       "hh3cIfStatFlowHCInBits": hh3cIfStatFlowHCInBits,
       "hh3cIfStatFlowHCOutBits": hh3cIfStatFlowHCOutBits,
       "hh3cIfStatFlowHCInPkts": hh3cIfStatFlowHCInPkts,
       "hh3cIfStatFlowHCOutPkts": hh3cIfStatFlowHCOutPkts,
       "hh3cIfStatFlowHCInBytes": hh3cIfStatFlowHCInBytes,
       "hh3cIfStatFlowHCOutBytes": hh3cIfStatFlowHCOutBytes,
       "hh3cIfHCSpeedStatTable": hh3cIfHCSpeedStatTable,
       "hh3cIfHCSpeedStatEntry": hh3cIfHCSpeedStatEntry,
       "hh3cIfSpeedStatHCInPkts": hh3cIfSpeedStatHCInPkts,
       "hh3cIfSpeedStatHCOutPkts": hh3cIfSpeedStatHCOutPkts,
       "hh3cIfSpeedStatHCInBytes": hh3cIfSpeedStatHCInBytes,
       "hh3cIfSpeedStatHCOutBytes": hh3cIfSpeedStatHCOutBytes,
       "hh3cIfSpeedStatHCInBits": hh3cIfSpeedStatHCInBits,
       "hh3cIfSpeedStatHCOutBits": hh3cIfSpeedStatHCOutBits,
       "hh3cIfControl": hh3cIfControl,
       "hh3cRTParentIfTable": hh3cRTParentIfTable,
       "hh3cRTParentIfEntry": hh3cRTParentIfEntry,
       "hh3cRTParentIfIndex": hh3cRTParentIfIndex,
       "hh3cRTMinSubIfOrdinal": hh3cRTMinSubIfOrdinal,
       "hh3cRTMaxSubIfOrdinal": hh3cRTMaxSubIfOrdinal,
       "hh3cRTSubIfTable": hh3cRTSubIfTable,
       "hh3cRTSubIfEntry": hh3cRTSubIfEntry,
       "hh3cRTSubIfParentIfIndex": hh3cRTSubIfParentIfIndex,
       "hh3cRTSubIfOrdinal": hh3cRTSubIfOrdinal,
       "hh3cRTSubIfSubIfIndex": hh3cRTSubIfSubIfIndex,
       "hh3cRTSubIfSubIfDesc": hh3cRTSubIfSubIfDesc,
       "hh3cRTSubIfRowStatus": hh3cRTSubIfRowStatus,
       "hh3cIfLinkModeTable": hh3cIfLinkModeTable,
       "hh3cIfLinkModeEntry": hh3cIfLinkModeEntry,
       "hh3cIfLinkModeIndex": hh3cIfLinkModeIndex,
       "hh3cIfLinkMode": hh3cIfLinkMode,
       "hh3cIfLinkModeSwitchSupport": hh3cIfLinkModeSwitchSupport,
       "hh3cIfPortTypeTable": hh3cIfPortTypeTable,
       "hh3cIfPortTypeEntry": hh3cIfPortTypeEntry,
       "hh3cIfPortTypeIndex": hh3cIfPortTypeIndex,
       "hh3cIfPortType": hh3cIfPortType,
       "hh3cIfPfcDot1pTable": hh3cIfPfcDot1pTable,
       "hh3cIfPfcDot1pEntry": hh3cIfPfcDot1pEntry,
       "hh3cIfPfcDot1pValue": hh3cIfPfcDot1pValue,
       "hh3cIfPfcDot1pInPps": hh3cIfPfcDot1pInPps,
       "hh3cIfPfcDot1pOutPps": hh3cIfPfcDot1pOutPps,
       "hh3cIfPfcDot1pInPpsThreshold": hh3cIfPfcDot1pInPpsThreshold,
       "hh3cIfPfcDot1pOutPpsThreshold": hh3cIfPfcDot1pOutPpsThreshold,
       "hh3cIfQueBufferTable": hh3cIfQueBufferTable,
       "hh3cIfQueBufferEntry": hh3cIfQueBufferEntry,
       "hh3cIfQueId": hh3cIfQueId,
       "hh3cIfQueOutUcastTotal": hh3cIfQueOutUcastTotal,
       "hh3cIfQueOutUcastFree": hh3cIfQueOutUcastFree,
       "hh3cIfQueOutUcastUsedRatio": hh3cIfQueOutUcastUsedRatio,
       "hh3cIfQueOutUcastUsedPeak": hh3cIfQueOutUcastUsedPeak,
       "hh3cIfQueOutUcastThreshold": hh3cIfQueOutUcastThreshold,
       "hh3cIfQueOutUcastOverThres": hh3cIfQueOutUcastOverThres,
       "hh3cIfQueInTotal": hh3cIfQueInTotal,
       "hh3cIfQueInFree": hh3cIfQueInFree,
       "hh3cIfQueInUsedRatio": hh3cIfQueInUsedRatio,
       "hh3cIfQueInUsedPeak": hh3cIfQueInUsedPeak,
       "hh3cIfQueInThreshold": hh3cIfQueInThreshold,
       "hh3cIfQueInOverThres": hh3cIfQueInOverThres,
       "hh3cIfQueInHeadRoomTotal": hh3cIfQueInHeadRoomTotal,
       "hh3cIfQueInHeadRoomFree": hh3cIfQueInHeadRoomFree,
       "hh3cIfQueInHeadRoomUsedRatio": hh3cIfQueInHeadRoomUsedRatio,
       "hh3cIfQueInHeadRoomUsedPeak": hh3cIfQueInHeadRoomUsedPeak,
       "hh3cIfInterfaces": hh3cIfInterfaces,
       "hh3cIfPhysicalNumber": hh3cIfPhysicalNumber,
       "hh3cIfTable": hh3cIfTable,
       "hh3cIfEntry": hh3cIfEntry,
       "hh3cIfUpDownTimes": hh3cIfUpDownTimes,
       "hh3cIfMtu": hh3cIfMtu,
       "hh3cIfBandwidthRate": hh3cIfBandwidthRate,
       "hh3cIfDiscardPktRate": hh3cIfDiscardPktRate,
       "hh3cIfStatusKeepTime": hh3cIfStatusKeepTime,
       "hh3cIfInNUcastPkts": hh3cIfInNUcastPkts,
       "hh3cIfOutNUcastPkts": hh3cIfOutNUcastPkts,
       "hh3cIfIsPoe": hh3cIfIsPoe,
       "hh3cIfOperStatus": hh3cIfOperStatus,
       "hh3cIfDownTimes": hh3cIfDownTimes,
       "hh3cIfPfcStatus": hh3cIfPfcStatus,
       "hh3cIfPfcDot1pNoDrop": hh3cIfPfcDot1pNoDrop,
       "hh3cIfDescription": hh3cIfDescription,
       "hh3cIfFwdErrDiscards": hh3cIfFwdErrDiscards,
       "hh3cIfFiberOrCopper": hh3cIfFiberOrCopper,
       "hh3cIfTransferMode": hh3cIfTransferMode,
       "hh3cIfUsingTable": hh3cIfUsingTable,
       "hh3cIfUsingEntry": hh3cIfUsingEntry,
       "hh3cIfUsingIndex": hh3cIfUsingIndex,
       "hh3cIfUsingSupportType": hh3cIfUsingSupportType,
       "hh3cIfUsingType": hh3cIfUsingType,
       "hh3cIfUsingStatus": hh3cIfUsingStatus,
       "hh3cIfExtTrap": hh3cIfExtTrap,
       "hh3cIfExtTrapPrex": hh3cIfExtTrapPrex,
       "hh3cIfBandwidthUsageHigh": hh3cIfBandwidthUsageHigh,
       "hh3cIfDiscardPktRateHigh": hh3cIfDiscardPktRateHigh,
       "hh3cIfDampeningSuppressed": hh3cIfDampeningSuppressed,
       "hh3cIfDampeningNotSuppressed": hh3cIfDampeningNotSuppressed,
       "hh3cIfPortUp": hh3cIfPortUp,
       "hh3cIfPortDown": hh3cIfPortDown,
       "hh3cIfPfcOutRising": hh3cIfPfcOutRising,
       "hh3cIfPfcInRising": hh3cIfPfcInRising,
       "hh3cIfExtTrapObject": hh3cIfExtTrapObject,
       "hh3cIfExtTrapCfgTable": hh3cIfExtTrapCfgTable,
       "hh3cIfExtTrapCfgEntry": hh3cIfExtTrapCfgEntry,
       "hh3cIfBandwidthUpperLimit": hh3cIfBandwidthUpperLimit,
       "hh3cIfDiscardPktRateUpperLimit": hh3cIfDiscardPktRateUpperLimit,
       "hh3cIfMonScalarGroup": hh3cIfMonScalarGroup,
       "hh3cIfMonGroup": hh3cIfMonGroup,
       "hh3cIfMonStat": hh3cIfMonStat,
       "hh3cIfMonStatTable": hh3cIfMonStatTable,
       "hh3cIfMonStatEntry": hh3cIfMonStatEntry,
       "hh3cIfMonInputUsageStatistics": hh3cIfMonInputUsageStatistics,
       "hh3cIfMonOutputUsageStatistics": hh3cIfMonOutputUsageStatistics,
       "hh3cIfMonInputErrorAlarmStatistics": hh3cIfMonInputErrorAlarmStatistics,
       "hh3cIfMonOutputErrorAlarmStatistics": hh3cIfMonOutputErrorAlarmStatistics,
       "hh3cIfMonSdhErrorStatistics": hh3cIfMonSdhErrorStatistics,
       "hh3cIfMonSdhB1ErrorStatistics": hh3cIfMonSdhB1ErrorStatistics,
       "hh3cIfMonSdhB2ErrorStatistics": hh3cIfMonSdhB2ErrorStatistics,
       "hh3cIfMonCRCErrorStatistics": hh3cIfMonCRCErrorStatistics,
       "hh3cIfMonRxPauseFrameStatistics": hh3cIfMonRxPauseFrameStatistics,
       "hh3cIfMonTxPauseFrameStatistics": hh3cIfMonTxPauseFrameStatistics,
       "hh3cIfMonRuntStatistics": hh3cIfMonRuntStatistics,
       "hh3cIfMonGiantStatistics": hh3cIfMonGiantStatistics,
       "hh3cIfMonControl": hh3cIfMonControl,
       "hh3cIfMonThresholdTable": hh3cIfMonThresholdTable,
       "hh3cIfMonThresholdEntry": hh3cIfMonThresholdEntry,
       "hh3cIfMonInputUsageLowThres": hh3cIfMonInputUsageLowThres,
       "hh3cIfMonInputUsageHighThres": hh3cIfMonInputUsageHighThres,
       "hh3cIfMonOutputUsageLowThres": hh3cIfMonOutputUsageLowThres,
       "hh3cIfMonOutputUsageHighThres": hh3cIfMonOutputUsageHighThres,
       "hh3cIfMonInputErrorAlarmLowThres": hh3cIfMonInputErrorAlarmLowThres,
       "hh3cIfMonInputErrorAlarmHighThres": hh3cIfMonInputErrorAlarmHighThres,
       "hh3cIfMonInputErrorAlarmInterval": hh3cIfMonInputErrorAlarmInterval,
       "hh3cIfMonOutputErrorAlarmLowThres": hh3cIfMonOutputErrorAlarmLowThres,
       "hh3cIfMonOutputErrorAlarmHighThres": hh3cIfMonOutputErrorAlarmHighThres,
       "hh3cIfMonOutputErrorAlarmInterval": hh3cIfMonOutputErrorAlarmInterval,
       "hh3cIfMonSdhErrorLowThres": hh3cIfMonSdhErrorLowThres,
       "hh3cIfMonSdhErrorHighThres": hh3cIfMonSdhErrorHighThres,
       "hh3cIfMonSdhErrorInterval": hh3cIfMonSdhErrorInterval,
       "hh3cIfMonSdhB1ErrorLowThres": hh3cIfMonSdhB1ErrorLowThres,
       "hh3cIfMonSdhB1ErrorHighThres": hh3cIfMonSdhB1ErrorHighThres,
       "hh3cIfMonSdhB1ErrorInterval": hh3cIfMonSdhB1ErrorInterval,
       "hh3cIfMonSdhB2ErrorLowThres": hh3cIfMonSdhB2ErrorLowThres,
       "hh3cIfMonSdhB2ErrorHighThres": hh3cIfMonSdhB2ErrorHighThres,
       "hh3cIfMonSdhB2ErrorInterval": hh3cIfMonSdhB2ErrorInterval,
       "hh3cIfMonCRCErrorLowThres": hh3cIfMonCRCErrorLowThres,
       "hh3cIfMonCRCErrorHighThres": hh3cIfMonCRCErrorHighThres,
       "hh3cIfMonCRCErrorInterval": hh3cIfMonCRCErrorInterval,
       "hh3cIfMonCRCErrType": hh3cIfMonCRCErrType,
       "hh3cIfMonRxPauseFrameLowThres": hh3cIfMonRxPauseFrameLowThres,
       "hh3cIfMonRxPauseFrameHighThres": hh3cIfMonRxPauseFrameHighThres,
       "hh3cIfMonRxPauseFrameInterval": hh3cIfMonRxPauseFrameInterval,
       "hh3cIfMonTxPauseFrameLowThres": hh3cIfMonTxPauseFrameLowThres,
       "hh3cIfMonTxPauseFrameHighThres": hh3cIfMonTxPauseFrameHighThres,
       "hh3cIfMonTxPauseFrameInterval": hh3cIfMonTxPauseFrameInterval,
       "hh3cIfMonGiantLowThres": hh3cIfMonGiantLowThres,
       "hh3cIfMonGiantHighThres": hh3cIfMonGiantHighThres,
       "hh3cIfMonGiantInterval": hh3cIfMonGiantInterval,
       "hh3cIfMonRuntLowThres": hh3cIfMonRuntLowThres,
       "hh3cIfMonRuntHighThres": hh3cIfMonRuntHighThres,
       "hh3cIfMonRuntInterval": hh3cIfMonRuntInterval,
       "hh3cIfMonAlarmDownEnableTable": hh3cIfMonAlarmDownEnableTable,
       "hh3cIfMonAlarmDownEnableEntry": hh3cIfMonAlarmDownEnableEntry,
       "hh3cIfMonInputErrorAlarmEnableDown": hh3cIfMonInputErrorAlarmEnableDown,
       "hh3cIfMonOutputErrorAlarmEnableDown": hh3cIfMonOutputErrorAlarmEnableDown,
       "hh3cIfMonSdhErrorEnableDown": hh3cIfMonSdhErrorEnableDown,
       "hh3cIfMonSdhB1ErrorEnableDown": hh3cIfMonSdhB1ErrorEnableDown,
       "hh3cIfMonSdhB2ErrorEnableDown": hh3cIfMonSdhB2ErrorEnableDown,
       "hh3cIfMonCRCErrorEnableDown": hh3cIfMonCRCErrorEnableDown,
       "hh3cIfMonGiantEnableDown": hh3cIfMonGiantEnableDown,
       "hh3cIfMonRuntEnableDown": hh3cIfMonRuntEnableDown,
       "hh3cIfMonTrap": hh3cIfMonTrap,
       "hh3cIfMonTrapPrex": hh3cIfMonTrapPrex,
       "hh3cIfMonInputUsageRising": hh3cIfMonInputUsageRising,
       "hh3cIfMonInputUsageResume": hh3cIfMonInputUsageResume,
       "hh3cIfMonOutputUsageRising": hh3cIfMonOutputUsageRising,
       "hh3cIfMonOutputUsageResume": hh3cIfMonOutputUsageResume,
       "hh3cIfMonInputErrorAlarmRising": hh3cIfMonInputErrorAlarmRising,
       "hh3cIfMonInputErrorAlarmResume": hh3cIfMonInputErrorAlarmResume,
       "hh3cIfMonOutputErrorAlarmRising": hh3cIfMonOutputErrorAlarmRising,
       "hh3cIfMonOutputErrorAlarmResume": hh3cIfMonOutputErrorAlarmResume,
       "hh3cIfMonSdhErrorRising": hh3cIfMonSdhErrorRising,
       "hh3cIfMonSdhErrorResume": hh3cIfMonSdhErrorResume,
       "hh3cIfMonSdhB1ErrorRising": hh3cIfMonSdhB1ErrorRising,
       "hh3cIfMonSdhB1ErrorResume": hh3cIfMonSdhB1ErrorResume,
       "hh3cIfMonSdhB2ErrorRising": hh3cIfMonSdhB2ErrorRising,
       "hh3cIfMonSdhB2ErrorResume": hh3cIfMonSdhB2ErrorResume,
       "hh3cIfMonCRCErrorRising": hh3cIfMonCRCErrorRising,
       "hh3cIfMonCRCErrorResume": hh3cIfMonCRCErrorResume,
       "hh3cIfMonRxPauseFrameRising": hh3cIfMonRxPauseFrameRising,
       "hh3cIfMonRxPauseFrameResume": hh3cIfMonRxPauseFrameResume,
       "hh3cIfMonTxPauseFrameRising": hh3cIfMonTxPauseFrameRising,
       "hh3cIfMonTxPauseFrameResume": hh3cIfMonTxPauseFrameResume,
       "hh3cIfMonGiantRising": hh3cIfMonGiantRising,
       "hh3cIfMonGiantResume": hh3cIfMonGiantResume,
       "hh3cIfMonRuntRising": hh3cIfMonRuntRising,
       "hh3cIfMonRuntResume": hh3cIfMonRuntResume,
       "hh3cIfMonTrapObject": hh3cIfMonTrapObject}
)
