# SNMP MIB module (AVIAT-RXPERFORMANCE-EX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aviat-wtm\AVIAT-RXPERFORMANCE-EX-MIB

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

(aviatRxPerformDayIndex,
 aviatRxPerformDayPeriod,
 aviatRxPerformQHourIndex,
 aviatRxPerformQHourPeriod) = mibBuilder.importSymbols(
    "AVIAT-RXPERFORMANCE-MIB",
    "aviatRxPerformDayIndex",
    "aviatRxPerformDayPeriod",
    "aviatRxPerformQHourIndex",
    "aviatRxPerformQHourPeriod")

(AviatPowerLevel,) = mibBuilder.importSymbols(
    "AVIAT-TEXTCONVENTION-MIB",
    "AviatPowerLevel")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(aviatModules,) = mibBuilder.importSymbols(
    "STXN-GLOBALREGISTER-MIB",
    "aviatModules")


# MODULE-IDENTITY

aviatRxPerformanceExModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33)
)
if mibBuilder.loadTexts:
    aviatRxPerformanceExModule.setRevisions(
        ("2014-01-21 01:57",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviatRxPerformanceExConf_ObjectIdentity = ObjectIdentity
aviatRxPerformanceExConf = _AviatRxPerformanceExConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 1)
)
_AviatRxPerformanceExGroups_ObjectIdentity = ObjectIdentity
aviatRxPerformanceExGroups = _AviatRxPerformanceExGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 1, 1)
)
_AviatRxPerformanceExCompl_ObjectIdentity = ObjectIdentity
aviatRxPerformanceExCompl = _AviatRxPerformanceExCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 1, 2)
)
_AviatRxPerformanceExMIBObjs_ObjectIdentity = ObjectIdentity
aviatRxPerformanceExMIBObjs = _AviatRxPerformanceExMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2)
)
_AviatRxPerformExTable_Object = MibTable
aviatRxPerformExTable = _AviatRxPerformExTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2)
)
if mibBuilder.loadTexts:
    aviatRxPerformExTable.setStatus("current")
_AviatRxPerformExEntry_Object = MibTableRow
aviatRxPerformExEntry = _AviatRxPerformExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1)
)
aviatRxPerformExEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatRxPerformExEntry.setStatus("current")
_AviatRxPerformCinrReadingMean_Type = AviatPowerLevel
_AviatRxPerformCinrReadingMean_Object = MibTableColumn
aviatRxPerformCinrReadingMean = _AviatRxPerformCinrReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 2),
    _AviatRxPerformCinrReadingMean_Type()
)
aviatRxPerformCinrReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformCinrReadingMean.setStatus("current")
_AviatRxPerformCinrReadingCurrent_Type = AviatPowerLevel
_AviatRxPerformCinrReadingCurrent_Object = MibTableColumn
aviatRxPerformCinrReadingCurrent = _AviatRxPerformCinrReadingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 3),
    _AviatRxPerformCinrReadingCurrent_Type()
)
aviatRxPerformCinrReadingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformCinrReadingCurrent.setStatus("current")
_AviatRxPerformCinrReadingMax_Type = AviatPowerLevel
_AviatRxPerformCinrReadingMax_Object = MibTableColumn
aviatRxPerformCinrReadingMax = _AviatRxPerformCinrReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 4),
    _AviatRxPerformCinrReadingMax_Type()
)
aviatRxPerformCinrReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformCinrReadingMax.setStatus("current")
_AviatRxPerformCinrReadingMin_Type = AviatPowerLevel
_AviatRxPerformCinrReadingMin_Object = MibTableColumn
aviatRxPerformCinrReadingMin = _AviatRxPerformCinrReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 5),
    _AviatRxPerformCinrReadingMin_Type()
)
aviatRxPerformCinrReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformCinrReadingMin.setStatus("current")
_AviatRxPerformTxpowReadingMean_Type = AviatPowerLevel
_AviatRxPerformTxpowReadingMean_Object = MibTableColumn
aviatRxPerformTxpowReadingMean = _AviatRxPerformTxpowReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 6),
    _AviatRxPerformTxpowReadingMean_Type()
)
aviatRxPerformTxpowReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformTxpowReadingMean.setStatus("current")
_AviatRxPerformTxpowReadingCurrent_Type = AviatPowerLevel
_AviatRxPerformTxpowReadingCurrent_Object = MibTableColumn
aviatRxPerformTxpowReadingCurrent = _AviatRxPerformTxpowReadingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 7),
    _AviatRxPerformTxpowReadingCurrent_Type()
)
aviatRxPerformTxpowReadingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformTxpowReadingCurrent.setStatus("current")
_AviatRxPerformTxpowReadingMax_Type = AviatPowerLevel
_AviatRxPerformTxpowReadingMax_Object = MibTableColumn
aviatRxPerformTxpowReadingMax = _AviatRxPerformTxpowReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 8),
    _AviatRxPerformTxpowReadingMax_Type()
)
aviatRxPerformTxpowReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformTxpowReadingMax.setStatus("current")
_AviatRxPerformTxpowReadingMin_Type = AviatPowerLevel
_AviatRxPerformTxpowReadingMin_Object = MibTableColumn
aviatRxPerformTxpowReadingMin = _AviatRxPerformTxpowReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 9),
    _AviatRxPerformTxpowReadingMin_Type()
)
aviatRxPerformTxpowReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformTxpowReadingMin.setStatus("current")
_AviatRxPerformQuarterHourExTable_Object = MibTable
aviatRxPerformQuarterHourExTable = _AviatRxPerformQuarterHourExTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3)
)
if mibBuilder.loadTexts:
    aviatRxPerformQuarterHourExTable.setStatus("current")
_AviatRxPerformQuarterHourExEntry_Object = MibTableRow
aviatRxPerformQuarterHourExEntry = _AviatRxPerformQuarterHourExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1)
)
aviatRxPerformQuarterHourExEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourIndex"),
    (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourPeriod"),
)
if mibBuilder.loadTexts:
    aviatRxPerformQuarterHourExEntry.setStatus("current")
_AviatRxPerformQHourCinrReadingMean_Type = AviatPowerLevel
_AviatRxPerformQHourCinrReadingMean_Object = MibTableColumn
aviatRxPerformQHourCinrReadingMean = _AviatRxPerformQHourCinrReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 4),
    _AviatRxPerformQHourCinrReadingMean_Type()
)
aviatRxPerformQHourCinrReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourCinrReadingMean.setStatus("current")
_AviatRxPerformQHourCinrReadingMax_Type = AviatPowerLevel
_AviatRxPerformQHourCinrReadingMax_Object = MibTableColumn
aviatRxPerformQHourCinrReadingMax = _AviatRxPerformQHourCinrReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 5),
    _AviatRxPerformQHourCinrReadingMax_Type()
)
aviatRxPerformQHourCinrReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourCinrReadingMax.setStatus("current")
_AviatRxPerformQHourCinrReadingMin_Type = AviatPowerLevel
_AviatRxPerformQHourCinrReadingMin_Object = MibTableColumn
aviatRxPerformQHourCinrReadingMin = _AviatRxPerformQHourCinrReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 6),
    _AviatRxPerformQHourCinrReadingMin_Type()
)
aviatRxPerformQHourCinrReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourCinrReadingMin.setStatus("current")
_AviatRxPerformQHourTxpowReadingMean_Type = AviatPowerLevel
_AviatRxPerformQHourTxpowReadingMean_Object = MibTableColumn
aviatRxPerformQHourTxpowReadingMean = _AviatRxPerformQHourTxpowReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 7),
    _AviatRxPerformQHourTxpowReadingMean_Type()
)
aviatRxPerformQHourTxpowReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourTxpowReadingMean.setStatus("current")
_AviatRxPerformQHourTxpowReadingMax_Type = AviatPowerLevel
_AviatRxPerformQHourTxpowReadingMax_Object = MibTableColumn
aviatRxPerformQHourTxpowReadingMax = _AviatRxPerformQHourTxpowReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 8),
    _AviatRxPerformQHourTxpowReadingMax_Type()
)
aviatRxPerformQHourTxpowReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourTxpowReadingMax.setStatus("current")
_AviatRxPerformQHourTxpowReadingMin_Type = AviatPowerLevel
_AviatRxPerformQHourTxpowReadingMin_Object = MibTableColumn
aviatRxPerformQHourTxpowReadingMin = _AviatRxPerformQHourTxpowReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 9),
    _AviatRxPerformQHourTxpowReadingMin_Type()
)
aviatRxPerformQHourTxpowReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourTxpowReadingMin.setStatus("current")
_AviatRxPerformDayExTable_Object = MibTable
aviatRxPerformDayExTable = _AviatRxPerformDayExTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4)
)
if mibBuilder.loadTexts:
    aviatRxPerformDayExTable.setStatus("current")
_AviatRxPerformDayExEntry_Object = MibTableRow
aviatRxPerformDayExEntry = _AviatRxPerformDayExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1)
)
aviatRxPerformDayExEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayIndex"),
    (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayPeriod"),
)
if mibBuilder.loadTexts:
    aviatRxPerformDayExEntry.setStatus("current")
_AviatRxPerformDayCinrReadingMean_Type = AviatPowerLevel
_AviatRxPerformDayCinrReadingMean_Object = MibTableColumn
aviatRxPerformDayCinrReadingMean = _AviatRxPerformDayCinrReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 4),
    _AviatRxPerformDayCinrReadingMean_Type()
)
aviatRxPerformDayCinrReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayCinrReadingMean.setStatus("current")
_AviatRxPerformDayCinrReadingMax_Type = AviatPowerLevel
_AviatRxPerformDayCinrReadingMax_Object = MibTableColumn
aviatRxPerformDayCinrReadingMax = _AviatRxPerformDayCinrReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 5),
    _AviatRxPerformDayCinrReadingMax_Type()
)
aviatRxPerformDayCinrReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayCinrReadingMax.setStatus("current")
_AviatRxPerformDayCinrReadingMin_Type = AviatPowerLevel
_AviatRxPerformDayCinrReadingMin_Object = MibTableColumn
aviatRxPerformDayCinrReadingMin = _AviatRxPerformDayCinrReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 6),
    _AviatRxPerformDayCinrReadingMin_Type()
)
aviatRxPerformDayCinrReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayCinrReadingMin.setStatus("current")
_AviatRxPerformDayTxpowReadingMean_Type = AviatPowerLevel
_AviatRxPerformDayTxpowReadingMean_Object = MibTableColumn
aviatRxPerformDayTxpowReadingMean = _AviatRxPerformDayTxpowReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 7),
    _AviatRxPerformDayTxpowReadingMean_Type()
)
aviatRxPerformDayTxpowReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayTxpowReadingMean.setStatus("current")
_AviatRxPerformDayTxpowReadingMax_Type = AviatPowerLevel
_AviatRxPerformDayTxpowReadingMax_Object = MibTableColumn
aviatRxPerformDayTxpowReadingMax = _AviatRxPerformDayTxpowReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 8),
    _AviatRxPerformDayTxpowReadingMax_Type()
)
aviatRxPerformDayTxpowReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayTxpowReadingMax.setStatus("current")
_AviatRxPerformDayTxpowReadingMin_Type = AviatPowerLevel
_AviatRxPerformDayTxpowReadingMin_Object = MibTableColumn
aviatRxPerformDayTxpowReadingMin = _AviatRxPerformDayTxpowReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 9),
    _AviatRxPerformDayTxpowReadingMin_Type()
)
aviatRxPerformDayTxpowReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayTxpowReadingMin.setStatus("current")

# Managed Objects groups

aviatRxPerformExObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 1, 1, 1)
)
aviatRxPerformExObjectGroup.setObjects(
      *(("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformCinrReadingMean"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformCinrReadingCurrent"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformCinrReadingMax"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformCinrReadingMin"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformTxpowReadingMean"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformTxpowReadingCurrent"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformTxpowReadingMax"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformTxpowReadingMin"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourCinrReadingMean"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourCinrReadingMax"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourCinrReadingMin"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourTxpowReadingMean"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourTxpowReadingMax"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourTxpowReadingMin"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayCinrReadingMean"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayCinrReadingMax"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayCinrReadingMin"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayTxpowReadingMean"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayTxpowReadingMax"),
        ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayTxpowReadingMin"))
)
if mibBuilder.loadTexts:
    aviatRxPerformExObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviatRxPerformanceExComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2509, 9, 33, 1, 2, 1)
)
aviatRxPerformanceExComplV1.setObjects(
    ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformExObjectGroup")
)
if mibBuilder.loadTexts:
    aviatRxPerformanceExComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVIAT-RXPERFORMANCE-EX-MIB",
    **{"aviatRxPerformanceExModule": aviatRxPerformanceExModule,
       "aviatRxPerformanceExConf": aviatRxPerformanceExConf,
       "aviatRxPerformanceExGroups": aviatRxPerformanceExGroups,
       "aviatRxPerformExObjectGroup": aviatRxPerformExObjectGroup,
       "aviatRxPerformanceExCompl": aviatRxPerformanceExCompl,
       "aviatRxPerformanceExComplV1": aviatRxPerformanceExComplV1,
       "aviatRxPerformanceExMIBObjs": aviatRxPerformanceExMIBObjs,
       "aviatRxPerformExTable": aviatRxPerformExTable,
       "aviatRxPerformExEntry": aviatRxPerformExEntry,
       "aviatRxPerformCinrReadingMean": aviatRxPerformCinrReadingMean,
       "aviatRxPerformCinrReadingCurrent": aviatRxPerformCinrReadingCurrent,
       "aviatRxPerformCinrReadingMax": aviatRxPerformCinrReadingMax,
       "aviatRxPerformCinrReadingMin": aviatRxPerformCinrReadingMin,
       "aviatRxPerformTxpowReadingMean": aviatRxPerformTxpowReadingMean,
       "aviatRxPerformTxpowReadingCurrent": aviatRxPerformTxpowReadingCurrent,
       "aviatRxPerformTxpowReadingMax": aviatRxPerformTxpowReadingMax,
       "aviatRxPerformTxpowReadingMin": aviatRxPerformTxpowReadingMin,
       "aviatRxPerformQuarterHourExTable": aviatRxPerformQuarterHourExTable,
       "aviatRxPerformQuarterHourExEntry": aviatRxPerformQuarterHourExEntry,
       "aviatRxPerformQHourCinrReadingMean": aviatRxPerformQHourCinrReadingMean,
       "aviatRxPerformQHourCinrReadingMax": aviatRxPerformQHourCinrReadingMax,
       "aviatRxPerformQHourCinrReadingMin": aviatRxPerformQHourCinrReadingMin,
       "aviatRxPerformQHourTxpowReadingMean": aviatRxPerformQHourTxpowReadingMean,
       "aviatRxPerformQHourTxpowReadingMax": aviatRxPerformQHourTxpowReadingMax,
       "aviatRxPerformQHourTxpowReadingMin": aviatRxPerformQHourTxpowReadingMin,
       "aviatRxPerformDayExTable": aviatRxPerformDayExTable,
       "aviatRxPerformDayExEntry": aviatRxPerformDayExEntry,
       "aviatRxPerformDayCinrReadingMean": aviatRxPerformDayCinrReadingMean,
       "aviatRxPerformDayCinrReadingMax": aviatRxPerformDayCinrReadingMax,
       "aviatRxPerformDayCinrReadingMin": aviatRxPerformDayCinrReadingMin,
       "aviatRxPerformDayTxpowReadingMean": aviatRxPerformDayTxpowReadingMean,
       "aviatRxPerformDayTxpowReadingMax": aviatRxPerformDayTxpowReadingMax,
       "aviatRxPerformDayTxpowReadingMin": aviatRxPerformDayTxpowReadingMin}
)
