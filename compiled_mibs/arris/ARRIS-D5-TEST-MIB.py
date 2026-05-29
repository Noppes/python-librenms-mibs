# SNMP MIB module (ARRIS-D5-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-TEST-MIB

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

(arrisD5UEQam,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisD5UEQam")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

d5TestMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19)
)
if mibBuilder.loadTexts:
    d5TestMIB.setRevisions(
        ("2008-12-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class D5TestState(TextualConvention, Integer32):
    status = "current"
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
        *(("idle", 0),
          ("start", 1),
          ("stop", 2),
          ("startCategory", 3),
          ("startSlot", 4),
          ("startAll", 5),
          ("clearCategory", 6),
          ("clearSlot", 7),
          ("clearAll", 8))
    )



class D5TestStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("skipped", 2),
          ("notRun", 3),
          ("running", 4),
          ("stopped", 5),
          ("continuous", 6))
    )



class D5TestResult(TextualConvention, Integer32):
    status = "current"
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
        *(("passed", 1),
          ("failed", 2),
          ("notAvailable", 3),
          ("incomplete", 4))
    )



# MIB Managed Objects in the order of their OIDs

_D5TestControl_ObjectIdentity = ObjectIdentity
d5TestControl = _D5TestControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1)
)
_D5TestControlSlot_Type = Unsigned32
_D5TestControlSlot_Object = MibScalar
d5TestControlSlot = _D5TestControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1, 1),
    _D5TestControlSlot_Type()
)
d5TestControlSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5TestControlSlot.setStatus("current")
_D5TestControlCategory_Type = Unsigned32
_D5TestControlCategory_Object = MibScalar
d5TestControlCategory = _D5TestControlCategory_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1, 2),
    _D5TestControlCategory_Type()
)
d5TestControlCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5TestControlCategory.setStatus("current")
_D5TestControlNumber_Type = Unsigned32
_D5TestControlNumber_Object = MibScalar
d5TestControlNumber = _D5TestControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1, 3),
    _D5TestControlNumber_Type()
)
d5TestControlNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5TestControlNumber.setStatus("current")
_D5TestControlState_Type = D5TestState
_D5TestControlState_Object = MibScalar
d5TestControlState = _D5TestControlState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1, 4),
    _D5TestControlState_Type()
)
d5TestControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5TestControlState.setStatus("current")
_D5TestControlIterations_Type = Unsigned32
_D5TestControlIterations_Object = MibScalar
d5TestControlIterations = _D5TestControlIterations_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1, 5),
    _D5TestControlIterations_Type()
)
d5TestControlIterations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5TestControlIterations.setStatus("current")
_D5TestControlArg0_Type = Unsigned32
_D5TestControlArg0_Object = MibScalar
d5TestControlArg0 = _D5TestControlArg0_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1, 6),
    _D5TestControlArg0_Type()
)
d5TestControlArg0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5TestControlArg0.setStatus("current")
_D5TestControlArg1_Type = Unsigned32
_D5TestControlArg1_Object = MibScalar
d5TestControlArg1 = _D5TestControlArg1_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1, 7),
    _D5TestControlArg1_Type()
)
d5TestControlArg1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5TestControlArg1.setStatus("current")
_D5TestControlArg2_Type = Unsigned32
_D5TestControlArg2_Object = MibScalar
d5TestControlArg2 = _D5TestControlArg2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1, 8),
    _D5TestControlArg2_Type()
)
d5TestControlArg2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5TestControlArg2.setStatus("current")
_D5TestControlArg3_Type = Unsigned32
_D5TestControlArg3_Object = MibScalar
d5TestControlArg3 = _D5TestControlArg3_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 1, 9),
    _D5TestControlArg3_Type()
)
d5TestControlArg3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5TestControlArg3.setStatus("current")
_D5TestResultTable_Object = MibTable
d5TestResultTable = _D5TestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2)
)
if mibBuilder.loadTexts:
    d5TestResultTable.setStatus("current")
_D5TestResultEntry_Object = MibTableRow
d5TestResultEntry = _D5TestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1)
)
d5TestResultEntry.setIndexNames(
    (0, "ARRIS-D5-TEST-MIB", "d5TestSlot"),
    (0, "ARRIS-D5-TEST-MIB", "d5TestCategory"),
    (0, "ARRIS-D5-TEST-MIB", "d5TestNumber"),
)
if mibBuilder.loadTexts:
    d5TestResultEntry.setStatus("current")
_D5TestSlot_Type = Unsigned32
_D5TestSlot_Object = MibTableColumn
d5TestSlot = _D5TestSlot_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 1),
    _D5TestSlot_Type()
)
d5TestSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5TestSlot.setStatus("current")
_D5TestCategory_Type = Unsigned32
_D5TestCategory_Object = MibTableColumn
d5TestCategory = _D5TestCategory_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 2),
    _D5TestCategory_Type()
)
d5TestCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5TestCategory.setStatus("current")
_D5TestNumber_Type = Unsigned32
_D5TestNumber_Object = MibTableColumn
d5TestNumber = _D5TestNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 3),
    _D5TestNumber_Type()
)
d5TestNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5TestNumber.setStatus("current")
_D5TestDescr_Type = DisplayString
_D5TestDescr_Object = MibTableColumn
d5TestDescr = _D5TestDescr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 4),
    _D5TestDescr_Type()
)
d5TestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestDescr.setStatus("current")
_D5TestStatus_Type = D5TestStatus
_D5TestStatus_Object = MibTableColumn
d5TestStatus = _D5TestStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 5),
    _D5TestStatus_Type()
)
d5TestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestStatus.setStatus("current")
_D5TestLastRunTime_Type = DateAndTime
_D5TestLastRunTime_Object = MibTableColumn
d5TestLastRunTime = _D5TestLastRunTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 6),
    _D5TestLastRunTime_Type()
)
d5TestLastRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestLastRunTime.setStatus("current")
_D5TestResult_Type = D5TestResult
_D5TestResult_Object = MibTableColumn
d5TestResult = _D5TestResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 7),
    _D5TestResult_Type()
)
d5TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResult.setStatus("current")


class _D5TestResultVector0_Type(Unsigned32):
    """Custom type d5TestResultVector0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector0_Type.__name__ = "Unsigned32"
_D5TestResultVector0_Object = MibTableColumn
d5TestResultVector0 = _D5TestResultVector0_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 8),
    _D5TestResultVector0_Type()
)
d5TestResultVector0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector0.setStatus("current")


class _D5TestResultVector1_Type(Unsigned32):
    """Custom type d5TestResultVector1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector1_Type.__name__ = "Unsigned32"
_D5TestResultVector1_Object = MibTableColumn
d5TestResultVector1 = _D5TestResultVector1_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 9),
    _D5TestResultVector1_Type()
)
d5TestResultVector1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector1.setStatus("current")


class _D5TestResultVector2_Type(Unsigned32):
    """Custom type d5TestResultVector2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector2_Type.__name__ = "Unsigned32"
_D5TestResultVector2_Object = MibTableColumn
d5TestResultVector2 = _D5TestResultVector2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 10),
    _D5TestResultVector2_Type()
)
d5TestResultVector2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector2.setStatus("current")


class _D5TestResultVector3_Type(Unsigned32):
    """Custom type d5TestResultVector3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector3_Type.__name__ = "Unsigned32"
_D5TestResultVector3_Object = MibTableColumn
d5TestResultVector3 = _D5TestResultVector3_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 11),
    _D5TestResultVector3_Type()
)
d5TestResultVector3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector3.setStatus("current")


class _D5TestResultVector4_Type(Unsigned32):
    """Custom type d5TestResultVector4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector4_Type.__name__ = "Unsigned32"
_D5TestResultVector4_Object = MibTableColumn
d5TestResultVector4 = _D5TestResultVector4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 12),
    _D5TestResultVector4_Type()
)
d5TestResultVector4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector4.setStatus("current")


class _D5TestResultVector5_Type(Unsigned32):
    """Custom type d5TestResultVector5 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector5_Type.__name__ = "Unsigned32"
_D5TestResultVector5_Object = MibTableColumn
d5TestResultVector5 = _D5TestResultVector5_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 13),
    _D5TestResultVector5_Type()
)
d5TestResultVector5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector5.setStatus("current")


class _D5TestResultVector6_Type(Unsigned32):
    """Custom type d5TestResultVector6 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector6_Type.__name__ = "Unsigned32"
_D5TestResultVector6_Object = MibTableColumn
d5TestResultVector6 = _D5TestResultVector6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 14),
    _D5TestResultVector6_Type()
)
d5TestResultVector6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector6.setStatus("current")


class _D5TestResultVector7_Type(Unsigned32):
    """Custom type d5TestResultVector7 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector7_Type.__name__ = "Unsigned32"
_D5TestResultVector7_Object = MibTableColumn
d5TestResultVector7 = _D5TestResultVector7_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 15),
    _D5TestResultVector7_Type()
)
d5TestResultVector7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector7.setStatus("current")


class _D5TestResultVector8_Type(Unsigned32):
    """Custom type d5TestResultVector8 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector8_Type.__name__ = "Unsigned32"
_D5TestResultVector8_Object = MibTableColumn
d5TestResultVector8 = _D5TestResultVector8_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 16),
    _D5TestResultVector8_Type()
)
d5TestResultVector8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector8.setStatus("current")


class _D5TestResultVector9_Type(Unsigned32):
    """Custom type d5TestResultVector9 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector9_Type.__name__ = "Unsigned32"
_D5TestResultVector9_Object = MibTableColumn
d5TestResultVector9 = _D5TestResultVector9_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 17),
    _D5TestResultVector9_Type()
)
d5TestResultVector9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector9.setStatus("current")


class _D5TestResultVector10_Type(Unsigned32):
    """Custom type d5TestResultVector10 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector10_Type.__name__ = "Unsigned32"
_D5TestResultVector10_Object = MibTableColumn
d5TestResultVector10 = _D5TestResultVector10_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 18),
    _D5TestResultVector10_Type()
)
d5TestResultVector10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector10.setStatus("current")


class _D5TestResultVector11_Type(Unsigned32):
    """Custom type d5TestResultVector11 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector11_Type.__name__ = "Unsigned32"
_D5TestResultVector11_Object = MibTableColumn
d5TestResultVector11 = _D5TestResultVector11_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 19),
    _D5TestResultVector11_Type()
)
d5TestResultVector11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector11.setStatus("current")


class _D5TestResultVector12_Type(Unsigned32):
    """Custom type d5TestResultVector12 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector12_Type.__name__ = "Unsigned32"
_D5TestResultVector12_Object = MibTableColumn
d5TestResultVector12 = _D5TestResultVector12_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 20),
    _D5TestResultVector12_Type()
)
d5TestResultVector12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector12.setStatus("current")


class _D5TestResultVector13_Type(Unsigned32):
    """Custom type d5TestResultVector13 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector13_Type.__name__ = "Unsigned32"
_D5TestResultVector13_Object = MibTableColumn
d5TestResultVector13 = _D5TestResultVector13_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 21),
    _D5TestResultVector13_Type()
)
d5TestResultVector13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector13.setStatus("current")


class _D5TestResultVector14_Type(Unsigned32):
    """Custom type d5TestResultVector14 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector14_Type.__name__ = "Unsigned32"
_D5TestResultVector14_Object = MibTableColumn
d5TestResultVector14 = _D5TestResultVector14_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 22),
    _D5TestResultVector14_Type()
)
d5TestResultVector14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector14.setStatus("current")


class _D5TestResultVector15_Type(Unsigned32):
    """Custom type d5TestResultVector15 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_D5TestResultVector15_Type.__name__ = "Unsigned32"
_D5TestResultVector15_Object = MibTableColumn
d5TestResultVector15 = _D5TestResultVector15_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 2, 1, 23),
    _D5TestResultVector15_Type()
)
d5TestResultVector15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5TestResultVector15.setStatus("current")
_D5TestMibConformance_ObjectIdentity = ObjectIdentity
d5TestMibConformance = _D5TestMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 99)
)
_D5TestMibGroups_ObjectIdentity = ObjectIdentity
d5TestMibGroups = _D5TestMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 99, 1)
)
_D5TestMibCompliances_ObjectIdentity = ObjectIdentity
d5TestMibCompliances = _D5TestMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 99, 2)
)

# Managed Objects groups

d5TestMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 99, 1, 1)
)
d5TestMibGroup.setObjects(
      *(("ARRIS-D5-TEST-MIB", "d5TestControlSlot"),
        ("ARRIS-D5-TEST-MIB", "d5TestControlCategory"),
        ("ARRIS-D5-TEST-MIB", "d5TestControlNumber"),
        ("ARRIS-D5-TEST-MIB", "d5TestControlState"),
        ("ARRIS-D5-TEST-MIB", "d5TestControlIterations"),
        ("ARRIS-D5-TEST-MIB", "d5TestControlArg0"),
        ("ARRIS-D5-TEST-MIB", "d5TestControlArg1"),
        ("ARRIS-D5-TEST-MIB", "d5TestControlArg2"),
        ("ARRIS-D5-TEST-MIB", "d5TestControlArg3"),
        ("ARRIS-D5-TEST-MIB", "d5TestDescr"),
        ("ARRIS-D5-TEST-MIB", "d5TestStatus"),
        ("ARRIS-D5-TEST-MIB", "d5TestLastRunTime"),
        ("ARRIS-D5-TEST-MIB", "d5TestResult"),
        ("ARRIS-D5-TEST-MIB", "d5TestResultVector1"),
        ("ARRIS-D5-TEST-MIB", "d5TestResultVector2"),
        ("ARRIS-D5-TEST-MIB", "d5TestResultVector3"),
        ("ARRIS-D5-TEST-MIB", "d5TestResultVector4"))
)
if mibBuilder.loadTexts:
    d5TestMibGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

d5TestMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 19, 99, 2, 1)
)
d5TestMibCompliance.setObjects(
    ("ARRIS-D5-TEST-MIB", "d5TestMibGroup")
)
if mibBuilder.loadTexts:
    d5TestMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-TEST-MIB",
    **{"D5TestState": D5TestState,
       "D5TestStatus": D5TestStatus,
       "D5TestResult": D5TestResult,
       "d5TestMIB": d5TestMIB,
       "d5TestControl": d5TestControl,
       "d5TestControlSlot": d5TestControlSlot,
       "d5TestControlCategory": d5TestControlCategory,
       "d5TestControlNumber": d5TestControlNumber,
       "d5TestControlState": d5TestControlState,
       "d5TestControlIterations": d5TestControlIterations,
       "d5TestControlArg0": d5TestControlArg0,
       "d5TestControlArg1": d5TestControlArg1,
       "d5TestControlArg2": d5TestControlArg2,
       "d5TestControlArg3": d5TestControlArg3,
       "d5TestResultTable": d5TestResultTable,
       "d5TestResultEntry": d5TestResultEntry,
       "d5TestSlot": d5TestSlot,
       "d5TestCategory": d5TestCategory,
       "d5TestNumber": d5TestNumber,
       "d5TestDescr": d5TestDescr,
       "d5TestStatus": d5TestStatus,
       "d5TestLastRunTime": d5TestLastRunTime,
       "d5TestResult": d5TestResult,
       "d5TestResultVector0": d5TestResultVector0,
       "d5TestResultVector1": d5TestResultVector1,
       "d5TestResultVector2": d5TestResultVector2,
       "d5TestResultVector3": d5TestResultVector3,
       "d5TestResultVector4": d5TestResultVector4,
       "d5TestResultVector5": d5TestResultVector5,
       "d5TestResultVector6": d5TestResultVector6,
       "d5TestResultVector7": d5TestResultVector7,
       "d5TestResultVector8": d5TestResultVector8,
       "d5TestResultVector9": d5TestResultVector9,
       "d5TestResultVector10": d5TestResultVector10,
       "d5TestResultVector11": d5TestResultVector11,
       "d5TestResultVector12": d5TestResultVector12,
       "d5TestResultVector13": d5TestResultVector13,
       "d5TestResultVector14": d5TestResultVector14,
       "d5TestResultVector15": d5TestResultVector15,
       "d5TestMibConformance": d5TestMibConformance,
       "d5TestMibGroups": d5TestMibGroups,
       "d5TestMibGroup": d5TestMibGroup,
       "d5TestMibCompliances": d5TestMibCompliances,
       "d5TestMibCompliance": d5TestMibCompliance}
)
