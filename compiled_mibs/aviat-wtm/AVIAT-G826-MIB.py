# SNMP MIB module (AVIAT-G826-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aviat-wtm\AVIAT-G826-MIB

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

aviatG826Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14)
)
if mibBuilder.loadTexts:
    aviatG826Module.setRevisions(
        ("2014-01-21 01:57",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AviatPackedG826Data(TextualConvention, OctetString):
    status = "current"
    displayHint = "55x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(47, 47),
    )



# MIB Managed Objects in the order of their OIDs

_AviatG826Conformance_ObjectIdentity = ObjectIdentity
aviatG826Conformance = _AviatG826Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 1)
)
_AviatG826Groups_ObjectIdentity = ObjectIdentity
aviatG826Groups = _AviatG826Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 1, 1)
)
_AviatG826Compliance_ObjectIdentity = ObjectIdentity
aviatG826Compliance = _AviatG826Compliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 1, 2)
)
_AviatG826MIBObjects_ObjectIdentity = ObjectIdentity
aviatG826MIBObjects = _AviatG826MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2)
)
_AviatG826ControlTable_Object = MibTable
aviatG826ControlTable = _AviatG826ControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1)
)
if mibBuilder.loadTexts:
    aviatG826ControlTable.setStatus("current")
_AviatG826ControlEntry_Object = MibTableRow
aviatG826ControlEntry = _AviatG826ControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1, 1)
)
aviatG826ControlEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatG826ControlEntry.setStatus("current")
_AviatG826LastQHourChangeIndex_Type = Gauge32
_AviatG826LastQHourChangeIndex_Object = MibTableColumn
aviatG826LastQHourChangeIndex = _AviatG826LastQHourChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1, 1, 1),
    _AviatG826LastQHourChangeIndex_Type()
)
aviatG826LastQHourChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826LastQHourChangeIndex.setStatus("current")
_AviatG826LastDayChangeIndex_Type = Gauge32
_AviatG826LastDayChangeIndex_Object = MibTableColumn
aviatG826LastDayChangeIndex = _AviatG826LastDayChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1, 1, 2),
    _AviatG826LastDayChangeIndex_Type()
)
aviatG826LastDayChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826LastDayChangeIndex.setStatus("current")


class _AviatG826Reset_Type(Integer32):
    """Custom type aviatG826Reset based on Integer32"""
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


_AviatG826Reset_Type.__name__ = "Integer32"
_AviatG826Reset_Object = MibTableColumn
aviatG826Reset = _AviatG826Reset_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 1, 1, 3),
    _AviatG826Reset_Type()
)
aviatG826Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatG826Reset.setStatus("current")
_AviatG826PerformTable_Object = MibTable
aviatG826PerformTable = _AviatG826PerformTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2)
)
if mibBuilder.loadTexts:
    aviatG826PerformTable.setStatus("current")
_AviatG826PerformEntry_Object = MibTableRow
aviatG826PerformEntry = _AviatG826PerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1)
)
aviatG826PerformEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatG826PerformEntry.setStatus("current")
_AviatG826ErroredBlocks_Type = Gauge32
_AviatG826ErroredBlocks_Object = MibTableColumn
aviatG826ErroredBlocks = _AviatG826ErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 3),
    _AviatG826ErroredBlocks_Type()
)
aviatG826ErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826ErroredBlocks.setStatus("current")
_AviatG826ErroredSeconds_Type = Gauge32
_AviatG826ErroredSeconds_Object = MibTableColumn
aviatG826ErroredSeconds = _AviatG826ErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 4),
    _AviatG826ErroredSeconds_Type()
)
aviatG826ErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826ErroredSeconds.setStatus("current")
_AviatG826ErroredSecondsRatio_Type = Gauge32
_AviatG826ErroredSecondsRatio_Object = MibTableColumn
aviatG826ErroredSecondsRatio = _AviatG826ErroredSecondsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 5),
    _AviatG826ErroredSecondsRatio_Type()
)
aviatG826ErroredSecondsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826ErroredSecondsRatio.setStatus("current")
_AviatG826SeverelyErroredSeconds_Type = Gauge32
_AviatG826SeverelyErroredSeconds_Object = MibTableColumn
aviatG826SeverelyErroredSeconds = _AviatG826SeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 6),
    _AviatG826SeverelyErroredSeconds_Type()
)
aviatG826SeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826SeverelyErroredSeconds.setStatus("current")
_AviatG826SeverelyErroredSecsRatio_Type = Gauge32
_AviatG826SeverelyErroredSecsRatio_Object = MibTableColumn
aviatG826SeverelyErroredSecsRatio = _AviatG826SeverelyErroredSecsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 7),
    _AviatG826SeverelyErroredSecsRatio_Type()
)
aviatG826SeverelyErroredSecsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826SeverelyErroredSecsRatio.setStatus("current")
_AviatG826BackgroundBlockErrors_Type = Gauge32
_AviatG826BackgroundBlockErrors_Object = MibTableColumn
aviatG826BackgroundBlockErrors = _AviatG826BackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 8),
    _AviatG826BackgroundBlockErrors_Type()
)
aviatG826BackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826BackgroundBlockErrors.setStatus("current")
_AviatG826BackgroundBlockErrorsRatio_Type = Gauge32
_AviatG826BackgroundBlockErrorsRatio_Object = MibTableColumn
aviatG826BackgroundBlockErrorsRatio = _AviatG826BackgroundBlockErrorsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 9),
    _AviatG826BackgroundBlockErrorsRatio_Type()
)
aviatG826BackgroundBlockErrorsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826BackgroundBlockErrorsRatio.setStatus("current")
_AviatG826AvailableSeconds_Type = Gauge32
_AviatG826AvailableSeconds_Object = MibTableColumn
aviatG826AvailableSeconds = _AviatG826AvailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 10),
    _AviatG826AvailableSeconds_Type()
)
aviatG826AvailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826AvailableSeconds.setStatus("current")
_AviatG826UnavailableSeconds_Type = Gauge32
_AviatG826UnavailableSeconds_Object = MibTableColumn
aviatG826UnavailableSeconds = _AviatG826UnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 11),
    _AviatG826UnavailableSeconds_Type()
)
aviatG826UnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826UnavailableSeconds.setStatus("current")
_AviatG826PackedData_Type = AviatPackedG826Data
_AviatG826PackedData_Object = MibTableColumn
aviatG826PackedData = _AviatG826PackedData_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 2, 1, 12),
    _AviatG826PackedData_Type()
)
aviatG826PackedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826PackedData.setStatus("current")
_AviatG826QuarterHourTable_Object = MibTable
aviatG826QuarterHourTable = _AviatG826QuarterHourTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3)
)
if mibBuilder.loadTexts:
    aviatG826QuarterHourTable.setStatus("current")
_AviatG826QuarterHourEntry_Object = MibTableRow
aviatG826QuarterHourEntry = _AviatG826QuarterHourEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1)
)
aviatG826QuarterHourEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "AVIAT-G826-MIB", "aviatG826QHourIndex"),
    (0, "AVIAT-G826-MIB", "aviatG826QHourPeriod"),
)
if mibBuilder.loadTexts:
    aviatG826QuarterHourEntry.setStatus("current")
_AviatG826QHourIndex_Type = Gauge32
_AviatG826QHourIndex_Object = MibTableColumn
aviatG826QHourIndex = _AviatG826QHourIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 1),
    _AviatG826QHourIndex_Type()
)
aviatG826QHourIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatG826QHourIndex.setStatus("current")
_AviatG826QHourPeriod_Type = Gauge32
_AviatG826QHourPeriod_Object = MibTableColumn
aviatG826QHourPeriod = _AviatG826QHourPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 2),
    _AviatG826QHourPeriod_Type()
)
aviatG826QHourPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatG826QHourPeriod.setStatus("current")
_AviatG826QHourDateAndTime_Type = DateAndTime
_AviatG826QHourDateAndTime_Object = MibTableColumn
aviatG826QHourDateAndTime = _AviatG826QHourDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 3),
    _AviatG826QHourDateAndTime_Type()
)
aviatG826QHourDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourDateAndTime.setStatus("current")
_AviatG826QHourErroredBlocks_Type = Gauge32
_AviatG826QHourErroredBlocks_Object = MibTableColumn
aviatG826QHourErroredBlocks = _AviatG826QHourErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 4),
    _AviatG826QHourErroredBlocks_Type()
)
aviatG826QHourErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourErroredBlocks.setStatus("current")
_AviatG826QHourErroredSeconds_Type = Gauge32
_AviatG826QHourErroredSeconds_Object = MibTableColumn
aviatG826QHourErroredSeconds = _AviatG826QHourErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 5),
    _AviatG826QHourErroredSeconds_Type()
)
aviatG826QHourErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourErroredSeconds.setStatus("current")
_AviatG826QHourErroredSecondsRatio_Type = Gauge32
_AviatG826QHourErroredSecondsRatio_Object = MibTableColumn
aviatG826QHourErroredSecondsRatio = _AviatG826QHourErroredSecondsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 6),
    _AviatG826QHourErroredSecondsRatio_Type()
)
aviatG826QHourErroredSecondsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourErroredSecondsRatio.setStatus("current")
_AviatG826QHourSeverelyErroredSeconds_Type = Gauge32
_AviatG826QHourSeverelyErroredSeconds_Object = MibTableColumn
aviatG826QHourSeverelyErroredSeconds = _AviatG826QHourSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 7),
    _AviatG826QHourSeverelyErroredSeconds_Type()
)
aviatG826QHourSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourSeverelyErroredSeconds.setStatus("current")
_AviatG826QHourSeverelyErroredSecsRatio_Type = Gauge32
_AviatG826QHourSeverelyErroredSecsRatio_Object = MibTableColumn
aviatG826QHourSeverelyErroredSecsRatio = _AviatG826QHourSeverelyErroredSecsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 8),
    _AviatG826QHourSeverelyErroredSecsRatio_Type()
)
aviatG826QHourSeverelyErroredSecsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourSeverelyErroredSecsRatio.setStatus("current")
_AviatG826QHourBackgroundBlockErrors_Type = Gauge32
_AviatG826QHourBackgroundBlockErrors_Object = MibTableColumn
aviatG826QHourBackgroundBlockErrors = _AviatG826QHourBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 9),
    _AviatG826QHourBackgroundBlockErrors_Type()
)
aviatG826QHourBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourBackgroundBlockErrors.setStatus("current")
_AviatG826QHourBackgroundBlockErrorsRatio_Type = Gauge32
_AviatG826QHourBackgroundBlockErrorsRatio_Object = MibTableColumn
aviatG826QHourBackgroundBlockErrorsRatio = _AviatG826QHourBackgroundBlockErrorsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 10),
    _AviatG826QHourBackgroundBlockErrorsRatio_Type()
)
aviatG826QHourBackgroundBlockErrorsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourBackgroundBlockErrorsRatio.setStatus("current")
_AviatG826QHourAvailableSeconds_Type = Gauge32
_AviatG826QHourAvailableSeconds_Object = MibTableColumn
aviatG826QHourAvailableSeconds = _AviatG826QHourAvailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 11),
    _AviatG826QHourAvailableSeconds_Type()
)
aviatG826QHourAvailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourAvailableSeconds.setStatus("current")
_AviatG826QHourUnavailableSeconds_Type = Gauge32
_AviatG826QHourUnavailableSeconds_Object = MibTableColumn
aviatG826QHourUnavailableSeconds = _AviatG826QHourUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 12),
    _AviatG826QHourUnavailableSeconds_Type()
)
aviatG826QHourUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourUnavailableSeconds.setStatus("current")
_AviatG826QHourInvalidEntry_Type = TruthValue
_AviatG826QHourInvalidEntry_Object = MibTableColumn
aviatG826QHourInvalidEntry = _AviatG826QHourInvalidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 3, 1, 14),
    _AviatG826QHourInvalidEntry_Type()
)
aviatG826QHourInvalidEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826QHourInvalidEntry.setStatus("current")
_AviatG826DayTable_Object = MibTable
aviatG826DayTable = _AviatG826DayTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4)
)
if mibBuilder.loadTexts:
    aviatG826DayTable.setStatus("current")
_AviatG826DayEntry_Object = MibTableRow
aviatG826DayEntry = _AviatG826DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1)
)
aviatG826DayEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "AVIAT-G826-MIB", "aviatG826DayIndex"),
    (0, "AVIAT-G826-MIB", "aviatG826DayPeriod"),
)
if mibBuilder.loadTexts:
    aviatG826DayEntry.setStatus("current")
_AviatG826DayIndex_Type = Gauge32
_AviatG826DayIndex_Object = MibTableColumn
aviatG826DayIndex = _AviatG826DayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 1),
    _AviatG826DayIndex_Type()
)
aviatG826DayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatG826DayIndex.setStatus("current")
_AviatG826DayPeriod_Type = Gauge32
_AviatG826DayPeriod_Object = MibTableColumn
aviatG826DayPeriod = _AviatG826DayPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 2),
    _AviatG826DayPeriod_Type()
)
aviatG826DayPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatG826DayPeriod.setStatus("current")
_AviatG826DayDateAndTime_Type = DateAndTime
_AviatG826DayDateAndTime_Object = MibTableColumn
aviatG826DayDateAndTime = _AviatG826DayDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 3),
    _AviatG826DayDateAndTime_Type()
)
aviatG826DayDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DayDateAndTime.setStatus("current")
_AviatG826DayErroredBlocks_Type = Gauge32
_AviatG826DayErroredBlocks_Object = MibTableColumn
aviatG826DayErroredBlocks = _AviatG826DayErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 4),
    _AviatG826DayErroredBlocks_Type()
)
aviatG826DayErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DayErroredBlocks.setStatus("current")
_AviatG826DayErroredSeconds_Type = Gauge32
_AviatG826DayErroredSeconds_Object = MibTableColumn
aviatG826DayErroredSeconds = _AviatG826DayErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 5),
    _AviatG826DayErroredSeconds_Type()
)
aviatG826DayErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DayErroredSeconds.setStatus("current")
_AviatG826DayErroredSecondsRatio_Type = Gauge32
_AviatG826DayErroredSecondsRatio_Object = MibTableColumn
aviatG826DayErroredSecondsRatio = _AviatG826DayErroredSecondsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 6),
    _AviatG826DayErroredSecondsRatio_Type()
)
aviatG826DayErroredSecondsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DayErroredSecondsRatio.setStatus("current")
_AviatG826DaySeverelyErroredSeconds_Type = Gauge32
_AviatG826DaySeverelyErroredSeconds_Object = MibTableColumn
aviatG826DaySeverelyErroredSeconds = _AviatG826DaySeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 7),
    _AviatG826DaySeverelyErroredSeconds_Type()
)
aviatG826DaySeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DaySeverelyErroredSeconds.setStatus("current")
_AviatG826DaySeverelyErroredSecsRatio_Type = Gauge32
_AviatG826DaySeverelyErroredSecsRatio_Object = MibTableColumn
aviatG826DaySeverelyErroredSecsRatio = _AviatG826DaySeverelyErroredSecsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 8),
    _AviatG826DaySeverelyErroredSecsRatio_Type()
)
aviatG826DaySeverelyErroredSecsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DaySeverelyErroredSecsRatio.setStatus("current")
_AviatG826DayBackgroundBlockErrors_Type = Gauge32
_AviatG826DayBackgroundBlockErrors_Object = MibTableColumn
aviatG826DayBackgroundBlockErrors = _AviatG826DayBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 9),
    _AviatG826DayBackgroundBlockErrors_Type()
)
aviatG826DayBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DayBackgroundBlockErrors.setStatus("current")
_AviatG826DayBackgroundBlockErrorsRatio_Type = Gauge32
_AviatG826DayBackgroundBlockErrorsRatio_Object = MibTableColumn
aviatG826DayBackgroundBlockErrorsRatio = _AviatG826DayBackgroundBlockErrorsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 10),
    _AviatG826DayBackgroundBlockErrorsRatio_Type()
)
aviatG826DayBackgroundBlockErrorsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DayBackgroundBlockErrorsRatio.setStatus("current")
_AviatG826DayAvailableSeconds_Type = Gauge32
_AviatG826DayAvailableSeconds_Object = MibTableColumn
aviatG826DayAvailableSeconds = _AviatG826DayAvailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 11),
    _AviatG826DayAvailableSeconds_Type()
)
aviatG826DayAvailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DayAvailableSeconds.setStatus("current")
_AviatG826DayUnavailableSeconds_Type = Gauge32
_AviatG826DayUnavailableSeconds_Object = MibTableColumn
aviatG826DayUnavailableSeconds = _AviatG826DayUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 12),
    _AviatG826DayUnavailableSeconds_Type()
)
aviatG826DayUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DayUnavailableSeconds.setStatus("current")
_AviatG826DayInvalidEntry_Type = TruthValue
_AviatG826DayInvalidEntry_Object = MibTableColumn
aviatG826DayInvalidEntry = _AviatG826DayInvalidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 2, 4, 1, 13),
    _AviatG826DayInvalidEntry_Type()
)
aviatG826DayInvalidEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatG826DayInvalidEntry.setStatus("current")

# Managed Objects groups

aviatG826ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 1, 1, 1)
)
aviatG826ObjectGroup.setObjects(
      *(("AVIAT-G826-MIB", "aviatG826LastQHourChangeIndex"),
        ("AVIAT-G826-MIB", "aviatG826LastDayChangeIndex"),
        ("AVIAT-G826-MIB", "aviatG826Reset"),
        ("AVIAT-G826-MIB", "aviatG826ErroredBlocks"),
        ("AVIAT-G826-MIB", "aviatG826ErroredSeconds"),
        ("AVIAT-G826-MIB", "aviatG826ErroredSecondsRatio"),
        ("AVIAT-G826-MIB", "aviatG826SeverelyErroredSeconds"),
        ("AVIAT-G826-MIB", "aviatG826SeverelyErroredSecsRatio"),
        ("AVIAT-G826-MIB", "aviatG826BackgroundBlockErrors"),
        ("AVIAT-G826-MIB", "aviatG826BackgroundBlockErrorsRatio"),
        ("AVIAT-G826-MIB", "aviatG826AvailableSeconds"),
        ("AVIAT-G826-MIB", "aviatG826UnavailableSeconds"),
        ("AVIAT-G826-MIB", "aviatG826PackedData"),
        ("AVIAT-G826-MIB", "aviatG826QHourDateAndTime"),
        ("AVIAT-G826-MIB", "aviatG826QHourErroredBlocks"),
        ("AVIAT-G826-MIB", "aviatG826QHourErroredSeconds"),
        ("AVIAT-G826-MIB", "aviatG826QHourErroredSecondsRatio"),
        ("AVIAT-G826-MIB", "aviatG826QHourSeverelyErroredSeconds"),
        ("AVIAT-G826-MIB", "aviatG826QHourSeverelyErroredSecsRatio"),
        ("AVIAT-G826-MIB", "aviatG826QHourBackgroundBlockErrors"),
        ("AVIAT-G826-MIB", "aviatG826QHourBackgroundBlockErrorsRatio"),
        ("AVIAT-G826-MIB", "aviatG826QHourAvailableSeconds"),
        ("AVIAT-G826-MIB", "aviatG826QHourUnavailableSeconds"),
        ("AVIAT-G826-MIB", "aviatG826QHourInvalidEntry"),
        ("AVIAT-G826-MIB", "aviatG826DayDateAndTime"),
        ("AVIAT-G826-MIB", "aviatG826DayErroredBlocks"),
        ("AVIAT-G826-MIB", "aviatG826DayErroredSeconds"),
        ("AVIAT-G826-MIB", "aviatG826DayErroredSecondsRatio"),
        ("AVIAT-G826-MIB", "aviatG826DaySeverelyErroredSeconds"),
        ("AVIAT-G826-MIB", "aviatG826DaySeverelyErroredSecsRatio"),
        ("AVIAT-G826-MIB", "aviatG826DayBackgroundBlockErrors"),
        ("AVIAT-G826-MIB", "aviatG826DayBackgroundBlockErrorsRatio"),
        ("AVIAT-G826-MIB", "aviatG826DayAvailableSeconds"),
        ("AVIAT-G826-MIB", "aviatG826DayUnavailableSeconds"),
        ("AVIAT-G826-MIB", "aviatG826DayInvalidEntry"))
)
if mibBuilder.loadTexts:
    aviatG826ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviatG826ComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2509, 9, 14, 1, 2, 1)
)
aviatG826ComplV1.setObjects(
    ("AVIAT-G826-MIB", "aviatG826ObjectGroup")
)
if mibBuilder.loadTexts:
    aviatG826ComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVIAT-G826-MIB",
    **{"AviatPackedG826Data": AviatPackedG826Data,
       "aviatG826Module": aviatG826Module,
       "aviatG826Conformance": aviatG826Conformance,
       "aviatG826Groups": aviatG826Groups,
       "aviatG826ObjectGroup": aviatG826ObjectGroup,
       "aviatG826Compliance": aviatG826Compliance,
       "aviatG826ComplV1": aviatG826ComplV1,
       "aviatG826MIBObjects": aviatG826MIBObjects,
       "aviatG826ControlTable": aviatG826ControlTable,
       "aviatG826ControlEntry": aviatG826ControlEntry,
       "aviatG826LastQHourChangeIndex": aviatG826LastQHourChangeIndex,
       "aviatG826LastDayChangeIndex": aviatG826LastDayChangeIndex,
       "aviatG826Reset": aviatG826Reset,
       "aviatG826PerformTable": aviatG826PerformTable,
       "aviatG826PerformEntry": aviatG826PerformEntry,
       "aviatG826ErroredBlocks": aviatG826ErroredBlocks,
       "aviatG826ErroredSeconds": aviatG826ErroredSeconds,
       "aviatG826ErroredSecondsRatio": aviatG826ErroredSecondsRatio,
       "aviatG826SeverelyErroredSeconds": aviatG826SeverelyErroredSeconds,
       "aviatG826SeverelyErroredSecsRatio": aviatG826SeverelyErroredSecsRatio,
       "aviatG826BackgroundBlockErrors": aviatG826BackgroundBlockErrors,
       "aviatG826BackgroundBlockErrorsRatio": aviatG826BackgroundBlockErrorsRatio,
       "aviatG826AvailableSeconds": aviatG826AvailableSeconds,
       "aviatG826UnavailableSeconds": aviatG826UnavailableSeconds,
       "aviatG826PackedData": aviatG826PackedData,
       "aviatG826QuarterHourTable": aviatG826QuarterHourTable,
       "aviatG826QuarterHourEntry": aviatG826QuarterHourEntry,
       "aviatG826QHourIndex": aviatG826QHourIndex,
       "aviatG826QHourPeriod": aviatG826QHourPeriod,
       "aviatG826QHourDateAndTime": aviatG826QHourDateAndTime,
       "aviatG826QHourErroredBlocks": aviatG826QHourErroredBlocks,
       "aviatG826QHourErroredSeconds": aviatG826QHourErroredSeconds,
       "aviatG826QHourErroredSecondsRatio": aviatG826QHourErroredSecondsRatio,
       "aviatG826QHourSeverelyErroredSeconds": aviatG826QHourSeverelyErroredSeconds,
       "aviatG826QHourSeverelyErroredSecsRatio": aviatG826QHourSeverelyErroredSecsRatio,
       "aviatG826QHourBackgroundBlockErrors": aviatG826QHourBackgroundBlockErrors,
       "aviatG826QHourBackgroundBlockErrorsRatio": aviatG826QHourBackgroundBlockErrorsRatio,
       "aviatG826QHourAvailableSeconds": aviatG826QHourAvailableSeconds,
       "aviatG826QHourUnavailableSeconds": aviatG826QHourUnavailableSeconds,
       "aviatG826QHourInvalidEntry": aviatG826QHourInvalidEntry,
       "aviatG826DayTable": aviatG826DayTable,
       "aviatG826DayEntry": aviatG826DayEntry,
       "aviatG826DayIndex": aviatG826DayIndex,
       "aviatG826DayPeriod": aviatG826DayPeriod,
       "aviatG826DayDateAndTime": aviatG826DayDateAndTime,
       "aviatG826DayErroredBlocks": aviatG826DayErroredBlocks,
       "aviatG826DayErroredSeconds": aviatG826DayErroredSeconds,
       "aviatG826DayErroredSecondsRatio": aviatG826DayErroredSecondsRatio,
       "aviatG826DaySeverelyErroredSeconds": aviatG826DaySeverelyErroredSeconds,
       "aviatG826DaySeverelyErroredSecsRatio": aviatG826DaySeverelyErroredSecsRatio,
       "aviatG826DayBackgroundBlockErrors": aviatG826DayBackgroundBlockErrors,
       "aviatG826DayBackgroundBlockErrorsRatio": aviatG826DayBackgroundBlockErrorsRatio,
       "aviatG826DayAvailableSeconds": aviatG826DayAvailableSeconds,
       "aviatG826DayUnavailableSeconds": aviatG826DayUnavailableSeconds,
       "aviatG826DayInvalidEntry": aviatG826DayInvalidEntry}
)
