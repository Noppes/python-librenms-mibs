# SNMP MIB module (AVIAT-RXPERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aviat-wtm\AVIAT-RXPERFORMANCE-MIB

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(aviatModules,) = mibBuilder.importSymbols(
    "STXN-GLOBALREGISTER-MIB",
    "aviatModules")


# MODULE-IDENTITY

aviatRxPerformanceModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15)
)
if mibBuilder.loadTexts:
    aviatRxPerformanceModule.setRevisions(
        ("2014-01-21 01:57",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AviatPackedRxPerformData(TextualConvention, OctetString):
    status = "current"
    displayHint = "63x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(63, 63),
    )



# MIB Managed Objects in the order of their OIDs

_AviatRxPerformanceConf_ObjectIdentity = ObjectIdentity
aviatRxPerformanceConf = _AviatRxPerformanceConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 1)
)
_AviatRxPerformanceGroups_ObjectIdentity = ObjectIdentity
aviatRxPerformanceGroups = _AviatRxPerformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 1, 1)
)
_AviatRxPerformanceCompl_ObjectIdentity = ObjectIdentity
aviatRxPerformanceCompl = _AviatRxPerformanceCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 1, 2)
)
_AviatRxPerformanceMIBObjs_ObjectIdentity = ObjectIdentity
aviatRxPerformanceMIBObjs = _AviatRxPerformanceMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2)
)
_AviatRxPerformControlTable_Object = MibTable
aviatRxPerformControlTable = _AviatRxPerformControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1)
)
if mibBuilder.loadTexts:
    aviatRxPerformControlTable.setStatus("current")
_AviatRxPerformControlEntry_Object = MibTableRow
aviatRxPerformControlEntry = _AviatRxPerformControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1, 1)
)
aviatRxPerformControlEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatRxPerformControlEntry.setStatus("current")


class _AviatRxPerformReset_Type(Integer32):
    """Custom type aviatRxPerformReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("all", 2),
          ("realtime", 3),
          ("quarterhour", 4),
          ("daily", 5))
    )


_AviatRxPerformReset_Type.__name__ = "Integer32"
_AviatRxPerformReset_Object = MibTableColumn
aviatRxPerformReset = _AviatRxPerformReset_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1, 1, 1),
    _AviatRxPerformReset_Type()
)
aviatRxPerformReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRxPerformReset.setStatus("current")
_AviatRxPerformLastQHourChangeIndex_Type = Gauge32
_AviatRxPerformLastQHourChangeIndex_Object = MibTableColumn
aviatRxPerformLastQHourChangeIndex = _AviatRxPerformLastQHourChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1, 1, 2),
    _AviatRxPerformLastQHourChangeIndex_Type()
)
aviatRxPerformLastQHourChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformLastQHourChangeIndex.setStatus("current")
_AviatRxPerformLastDayChangeIndex_Type = Gauge32
_AviatRxPerformLastDayChangeIndex_Object = MibTableColumn
aviatRxPerformLastDayChangeIndex = _AviatRxPerformLastDayChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1, 1, 3),
    _AviatRxPerformLastDayChangeIndex_Type()
)
aviatRxPerformLastDayChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformLastDayChangeIndex.setStatus("current")
_AviatRxPerformTable_Object = MibTable
aviatRxPerformTable = _AviatRxPerformTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2)
)
if mibBuilder.loadTexts:
    aviatRxPerformTable.setStatus("current")
_AviatRxPerformEntry_Object = MibTableRow
aviatRxPerformEntry = _AviatRxPerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1)
)
aviatRxPerformEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatRxPerformEntry.setStatus("current")
_AviatRxPerformRslReadingMean_Type = AviatPowerLevel
_AviatRxPerformRslReadingMean_Object = MibTableColumn
aviatRxPerformRslReadingMean = _AviatRxPerformRslReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 3),
    _AviatRxPerformRslReadingMean_Type()
)
aviatRxPerformRslReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformRslReadingMean.setStatus("current")
_AviatRxPerformRslReadingCurrent_Type = AviatPowerLevel
_AviatRxPerformRslReadingCurrent_Object = MibTableColumn
aviatRxPerformRslReadingCurrent = _AviatRxPerformRslReadingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 4),
    _AviatRxPerformRslReadingCurrent_Type()
)
aviatRxPerformRslReadingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformRslReadingCurrent.setStatus("current")
_AviatRxPerformRslReadingMax_Type = AviatPowerLevel
_AviatRxPerformRslReadingMax_Object = MibTableColumn
aviatRxPerformRslReadingMax = _AviatRxPerformRslReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 5),
    _AviatRxPerformRslReadingMax_Type()
)
aviatRxPerformRslReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformRslReadingMax.setStatus("current")
_AviatRxPerformRslReadingMin_Type = AviatPowerLevel
_AviatRxPerformRslReadingMin_Object = MibTableColumn
aviatRxPerformRslReadingMin = _AviatRxPerformRslReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 6),
    _AviatRxPerformRslReadingMin_Type()
)
aviatRxPerformRslReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformRslReadingMin.setStatus("current")
_AviatRxPerformBerReadingMean_Type = Counter64
_AviatRxPerformBerReadingMean_Object = MibTableColumn
aviatRxPerformBerReadingMean = _AviatRxPerformBerReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 7),
    _AviatRxPerformBerReadingMean_Type()
)
aviatRxPerformBerReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformBerReadingMean.setStatus("current")
_AviatRxPerformBerReadingCurrent_Type = Counter64
_AviatRxPerformBerReadingCurrent_Object = MibTableColumn
aviatRxPerformBerReadingCurrent = _AviatRxPerformBerReadingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 8),
    _AviatRxPerformBerReadingCurrent_Type()
)
aviatRxPerformBerReadingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformBerReadingCurrent.setStatus("current")
_AviatRxPerformBerReadingMax_Type = Counter64
_AviatRxPerformBerReadingMax_Object = MibTableColumn
aviatRxPerformBerReadingMax = _AviatRxPerformBerReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 9),
    _AviatRxPerformBerReadingMax_Type()
)
aviatRxPerformBerReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformBerReadingMax.setStatus("current")
_AviatRxPerformBerReadingMin_Type = Counter64
_AviatRxPerformBerReadingMin_Object = MibTableColumn
aviatRxPerformBerReadingMin = _AviatRxPerformBerReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 10),
    _AviatRxPerformBerReadingMin_Type()
)
aviatRxPerformBerReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformBerReadingMin.setStatus("current")
_AviatRxPerformFrameLossSeconds_Type = Gauge32
_AviatRxPerformFrameLossSeconds_Object = MibTableColumn
aviatRxPerformFrameLossSeconds = _AviatRxPerformFrameLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 11),
    _AviatRxPerformFrameLossSeconds_Type()
)
aviatRxPerformFrameLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformFrameLossSeconds.setStatus("current")
_AviatRxPerformPackedData_Type = AviatPackedRxPerformData
_AviatRxPerformPackedData_Object = MibTableColumn
aviatRxPerformPackedData = _AviatRxPerformPackedData_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 12),
    _AviatRxPerformPackedData_Type()
)
aviatRxPerformPackedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformPackedData.setStatus("current")
_AviatRxPerformQuarterHourTable_Object = MibTable
aviatRxPerformQuarterHourTable = _AviatRxPerformQuarterHourTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3)
)
if mibBuilder.loadTexts:
    aviatRxPerformQuarterHourTable.setStatus("current")
_AviatRxPerformQuarterHourEntry_Object = MibTableRow
aviatRxPerformQuarterHourEntry = _AviatRxPerformQuarterHourEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1)
)
aviatRxPerformQuarterHourEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourIndex"),
    (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourPeriod"),
)
if mibBuilder.loadTexts:
    aviatRxPerformQuarterHourEntry.setStatus("current")
_AviatRxPerformQHourIndex_Type = Gauge32
_AviatRxPerformQHourIndex_Object = MibTableColumn
aviatRxPerformQHourIndex = _AviatRxPerformQHourIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 1),
    _AviatRxPerformQHourIndex_Type()
)
aviatRxPerformQHourIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatRxPerformQHourIndex.setStatus("current")
_AviatRxPerformQHourPeriod_Type = Gauge32
_AviatRxPerformQHourPeriod_Object = MibTableColumn
aviatRxPerformQHourPeriod = _AviatRxPerformQHourPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 2),
    _AviatRxPerformQHourPeriod_Type()
)
aviatRxPerformQHourPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatRxPerformQHourPeriod.setStatus("current")
_AviatRxPerformQHourDateAndTime_Type = DateAndTime
_AviatRxPerformQHourDateAndTime_Object = MibTableColumn
aviatRxPerformQHourDateAndTime = _AviatRxPerformQHourDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 4),
    _AviatRxPerformQHourDateAndTime_Type()
)
aviatRxPerformQHourDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourDateAndTime.setStatus("current")
_AviatRxPerformQHourRslReadingMean_Type = AviatPowerLevel
_AviatRxPerformQHourRslReadingMean_Object = MibTableColumn
aviatRxPerformQHourRslReadingMean = _AviatRxPerformQHourRslReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 5),
    _AviatRxPerformQHourRslReadingMean_Type()
)
aviatRxPerformQHourRslReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourRslReadingMean.setStatus("current")
_AviatRxPerformQHourRslReadingMax_Type = AviatPowerLevel
_AviatRxPerformQHourRslReadingMax_Object = MibTableColumn
aviatRxPerformQHourRslReadingMax = _AviatRxPerformQHourRslReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 6),
    _AviatRxPerformQHourRslReadingMax_Type()
)
aviatRxPerformQHourRslReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourRslReadingMax.setStatus("current")
_AviatRxPerformQHourRslReadingMin_Type = AviatPowerLevel
_AviatRxPerformQHourRslReadingMin_Object = MibTableColumn
aviatRxPerformQHourRslReadingMin = _AviatRxPerformQHourRslReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 7),
    _AviatRxPerformQHourRslReadingMin_Type()
)
aviatRxPerformQHourRslReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourRslReadingMin.setStatus("current")
_AviatRxPerformQHourBerReadingMean_Type = Counter64
_AviatRxPerformQHourBerReadingMean_Object = MibTableColumn
aviatRxPerformQHourBerReadingMean = _AviatRxPerformQHourBerReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 8),
    _AviatRxPerformQHourBerReadingMean_Type()
)
aviatRxPerformQHourBerReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourBerReadingMean.setStatus("current")
_AviatRxPerformQHourBerReadingMax_Type = Counter64
_AviatRxPerformQHourBerReadingMax_Object = MibTableColumn
aviatRxPerformQHourBerReadingMax = _AviatRxPerformQHourBerReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 9),
    _AviatRxPerformQHourBerReadingMax_Type()
)
aviatRxPerformQHourBerReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourBerReadingMax.setStatus("current")
_AviatRxPerformQHourBerReadingMin_Type = Counter64
_AviatRxPerformQHourBerReadingMin_Object = MibTableColumn
aviatRxPerformQHourBerReadingMin = _AviatRxPerformQHourBerReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 10),
    _AviatRxPerformQHourBerReadingMin_Type()
)
aviatRxPerformQHourBerReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourBerReadingMin.setStatus("current")
_AviatRxPerformQHourFrameLossSeconds_Type = Gauge32
_AviatRxPerformQHourFrameLossSeconds_Object = MibTableColumn
aviatRxPerformQHourFrameLossSeconds = _AviatRxPerformQHourFrameLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 11),
    _AviatRxPerformQHourFrameLossSeconds_Type()
)
aviatRxPerformQHourFrameLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourFrameLossSeconds.setStatus("current")
_AviatRxPerformQHourInvalidEntry_Type = TruthValue
_AviatRxPerformQHourInvalidEntry_Object = MibTableColumn
aviatRxPerformQHourInvalidEntry = _AviatRxPerformQHourInvalidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 12),
    _AviatRxPerformQHourInvalidEntry_Type()
)
aviatRxPerformQHourInvalidEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformQHourInvalidEntry.setStatus("current")
_AviatRxPerformDayTable_Object = MibTable
aviatRxPerformDayTable = _AviatRxPerformDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4)
)
if mibBuilder.loadTexts:
    aviatRxPerformDayTable.setStatus("current")
_AviatRxPerformDayEntry_Object = MibTableRow
aviatRxPerformDayEntry = _AviatRxPerformDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1)
)
aviatRxPerformDayEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayIndex"),
    (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayPeriod"),
)
if mibBuilder.loadTexts:
    aviatRxPerformDayEntry.setStatus("current")
_AviatRxPerformDayIndex_Type = Gauge32
_AviatRxPerformDayIndex_Object = MibTableColumn
aviatRxPerformDayIndex = _AviatRxPerformDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 1),
    _AviatRxPerformDayIndex_Type()
)
aviatRxPerformDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatRxPerformDayIndex.setStatus("current")
_AviatRxPerformDayPeriod_Type = Gauge32
_AviatRxPerformDayPeriod_Object = MibTableColumn
aviatRxPerformDayPeriod = _AviatRxPerformDayPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 2),
    _AviatRxPerformDayPeriod_Type()
)
aviatRxPerformDayPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatRxPerformDayPeriod.setStatus("current")
_AviatRxPerformDayDateAndTime_Type = DateAndTime
_AviatRxPerformDayDateAndTime_Object = MibTableColumn
aviatRxPerformDayDateAndTime = _AviatRxPerformDayDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 4),
    _AviatRxPerformDayDateAndTime_Type()
)
aviatRxPerformDayDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayDateAndTime.setStatus("current")
_AviatRxPerformDayRslReadingMean_Type = AviatPowerLevel
_AviatRxPerformDayRslReadingMean_Object = MibTableColumn
aviatRxPerformDayRslReadingMean = _AviatRxPerformDayRslReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 5),
    _AviatRxPerformDayRslReadingMean_Type()
)
aviatRxPerformDayRslReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayRslReadingMean.setStatus("current")
_AviatRxPerformDayRslReadingMax_Type = AviatPowerLevel
_AviatRxPerformDayRslReadingMax_Object = MibTableColumn
aviatRxPerformDayRslReadingMax = _AviatRxPerformDayRslReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 6),
    _AviatRxPerformDayRslReadingMax_Type()
)
aviatRxPerformDayRslReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayRslReadingMax.setStatus("current")
_AviatRxPerformDayRslReadingMin_Type = AviatPowerLevel
_AviatRxPerformDayRslReadingMin_Object = MibTableColumn
aviatRxPerformDayRslReadingMin = _AviatRxPerformDayRslReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 7),
    _AviatRxPerformDayRslReadingMin_Type()
)
aviatRxPerformDayRslReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayRslReadingMin.setStatus("current")
_AviatRxPerformDayBerReadingMean_Type = Counter64
_AviatRxPerformDayBerReadingMean_Object = MibTableColumn
aviatRxPerformDayBerReadingMean = _AviatRxPerformDayBerReadingMean_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 8),
    _AviatRxPerformDayBerReadingMean_Type()
)
aviatRxPerformDayBerReadingMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayBerReadingMean.setStatus("current")
_AviatRxPerformDayBerReadingMax_Type = Counter64
_AviatRxPerformDayBerReadingMax_Object = MibTableColumn
aviatRxPerformDayBerReadingMax = _AviatRxPerformDayBerReadingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 9),
    _AviatRxPerformDayBerReadingMax_Type()
)
aviatRxPerformDayBerReadingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayBerReadingMax.setStatus("current")
_AviatRxPerformDayBerReadingMin_Type = Counter64
_AviatRxPerformDayBerReadingMin_Object = MibTableColumn
aviatRxPerformDayBerReadingMin = _AviatRxPerformDayBerReadingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 10),
    _AviatRxPerformDayBerReadingMin_Type()
)
aviatRxPerformDayBerReadingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayBerReadingMin.setStatus("current")
_AviatRxPerformDayFrameLossSeconds_Type = Gauge32
_AviatRxPerformDayFrameLossSeconds_Object = MibTableColumn
aviatRxPerformDayFrameLossSeconds = _AviatRxPerformDayFrameLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 11),
    _AviatRxPerformDayFrameLossSeconds_Type()
)
aviatRxPerformDayFrameLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayFrameLossSeconds.setStatus("current")
_AviatRxPerformDayInvalidEntry_Type = TruthValue
_AviatRxPerformDayInvalidEntry_Object = MibTableColumn
aviatRxPerformDayInvalidEntry = _AviatRxPerformDayInvalidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 12),
    _AviatRxPerformDayInvalidEntry_Type()
)
aviatRxPerformDayInvalidEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRxPerformDayInvalidEntry.setStatus("current")

# Managed Objects groups

aviatRxPerformObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 1, 1, 1)
)
aviatRxPerformObjectGroup.setObjects(
      *(("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformReset"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformLastQHourChangeIndex"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformLastDayChangeIndex"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformRslReadingMean"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformRslReadingCurrent"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformRslReadingMax"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformRslReadingMin"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformBerReadingMean"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformBerReadingCurrent"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformBerReadingMax"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformBerReadingMin"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformFrameLossSeconds"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformPackedData"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourDateAndTime"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourRslReadingMean"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourRslReadingMax"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourRslReadingMin"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourBerReadingMean"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourBerReadingMax"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourBerReadingMin"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourFrameLossSeconds"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourInvalidEntry"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayDateAndTime"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayRslReadingMean"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayRslReadingMax"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayRslReadingMin"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayBerReadingMean"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayBerReadingMax"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayBerReadingMin"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayFrameLossSeconds"),
        ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayInvalidEntry"))
)
if mibBuilder.loadTexts:
    aviatRxPerformObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviatRxPerformanceComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2509, 9, 15, 1, 2, 1)
)
aviatRxPerformanceComplV1.setObjects(
    ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformObjectGroup")
)
if mibBuilder.loadTexts:
    aviatRxPerformanceComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVIAT-RXPERFORMANCE-MIB",
    **{"AviatPackedRxPerformData": AviatPackedRxPerformData,
       "aviatRxPerformanceModule": aviatRxPerformanceModule,
       "aviatRxPerformanceConf": aviatRxPerformanceConf,
       "aviatRxPerformanceGroups": aviatRxPerformanceGroups,
       "aviatRxPerformObjectGroup": aviatRxPerformObjectGroup,
       "aviatRxPerformanceCompl": aviatRxPerformanceCompl,
       "aviatRxPerformanceComplV1": aviatRxPerformanceComplV1,
       "aviatRxPerformanceMIBObjs": aviatRxPerformanceMIBObjs,
       "aviatRxPerformControlTable": aviatRxPerformControlTable,
       "aviatRxPerformControlEntry": aviatRxPerformControlEntry,
       "aviatRxPerformReset": aviatRxPerformReset,
       "aviatRxPerformLastQHourChangeIndex": aviatRxPerformLastQHourChangeIndex,
       "aviatRxPerformLastDayChangeIndex": aviatRxPerformLastDayChangeIndex,
       "aviatRxPerformTable": aviatRxPerformTable,
       "aviatRxPerformEntry": aviatRxPerformEntry,
       "aviatRxPerformRslReadingMean": aviatRxPerformRslReadingMean,
       "aviatRxPerformRslReadingCurrent": aviatRxPerformRslReadingCurrent,
       "aviatRxPerformRslReadingMax": aviatRxPerformRslReadingMax,
       "aviatRxPerformRslReadingMin": aviatRxPerformRslReadingMin,
       "aviatRxPerformBerReadingMean": aviatRxPerformBerReadingMean,
       "aviatRxPerformBerReadingCurrent": aviatRxPerformBerReadingCurrent,
       "aviatRxPerformBerReadingMax": aviatRxPerformBerReadingMax,
       "aviatRxPerformBerReadingMin": aviatRxPerformBerReadingMin,
       "aviatRxPerformFrameLossSeconds": aviatRxPerformFrameLossSeconds,
       "aviatRxPerformPackedData": aviatRxPerformPackedData,
       "aviatRxPerformQuarterHourTable": aviatRxPerformQuarterHourTable,
       "aviatRxPerformQuarterHourEntry": aviatRxPerformQuarterHourEntry,
       "aviatRxPerformQHourIndex": aviatRxPerformQHourIndex,
       "aviatRxPerformQHourPeriod": aviatRxPerformQHourPeriod,
       "aviatRxPerformQHourDateAndTime": aviatRxPerformQHourDateAndTime,
       "aviatRxPerformQHourRslReadingMean": aviatRxPerformQHourRslReadingMean,
       "aviatRxPerformQHourRslReadingMax": aviatRxPerformQHourRslReadingMax,
       "aviatRxPerformQHourRslReadingMin": aviatRxPerformQHourRslReadingMin,
       "aviatRxPerformQHourBerReadingMean": aviatRxPerformQHourBerReadingMean,
       "aviatRxPerformQHourBerReadingMax": aviatRxPerformQHourBerReadingMax,
       "aviatRxPerformQHourBerReadingMin": aviatRxPerformQHourBerReadingMin,
       "aviatRxPerformQHourFrameLossSeconds": aviatRxPerformQHourFrameLossSeconds,
       "aviatRxPerformQHourInvalidEntry": aviatRxPerformQHourInvalidEntry,
       "aviatRxPerformDayTable": aviatRxPerformDayTable,
       "aviatRxPerformDayEntry": aviatRxPerformDayEntry,
       "aviatRxPerformDayIndex": aviatRxPerformDayIndex,
       "aviatRxPerformDayPeriod": aviatRxPerformDayPeriod,
       "aviatRxPerformDayDateAndTime": aviatRxPerformDayDateAndTime,
       "aviatRxPerformDayRslReadingMean": aviatRxPerformDayRslReadingMean,
       "aviatRxPerformDayRslReadingMax": aviatRxPerformDayRslReadingMax,
       "aviatRxPerformDayRslReadingMin": aviatRxPerformDayRslReadingMin,
       "aviatRxPerformDayBerReadingMean": aviatRxPerformDayBerReadingMean,
       "aviatRxPerformDayBerReadingMax": aviatRxPerformDayBerReadingMax,
       "aviatRxPerformDayBerReadingMin": aviatRxPerformDayBerReadingMin,
       "aviatRxPerformDayFrameLossSeconds": aviatRxPerformDayFrameLossSeconds,
       "aviatRxPerformDayInvalidEntry": aviatRxPerformDayInvalidEntry}
)
