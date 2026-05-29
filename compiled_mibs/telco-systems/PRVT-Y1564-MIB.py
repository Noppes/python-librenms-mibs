# SNMP MIB module (PRVT-Y1564-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-Y1564-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

prvtY1564Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129)
)
if mibBuilder.loadTexts:
    prvtY1564Mib.setRevisions(
        ("2012-02-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtY1564Notifications_ObjectIdentity = ObjectIdentity
prvtY1564Notifications = _PrvtY1564Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 0)
)
_PrvtY1564Objects_ObjectIdentity = ObjectIdentity
prvtY1564Objects = _PrvtY1564Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1)
)
_PrvtY1564Test_ObjectIdentity = ObjectIdentity
prvtY1564Test = _PrvtY1564Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1)
)
_PrvtY1564TestTable_Object = MibTable
prvtY1564TestTable = _PrvtY1564TestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtY1564TestTable.setStatus("current")
_PrvtY1564TestEntry_Object = MibTableRow
prvtY1564TestEntry = _PrvtY1564TestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1)
)
prvtY1564TestEntry.setIndexNames(
    (0, "PRVT-Y1564-MIB", "prvtY1564TestName"),
)
if mibBuilder.loadTexts:
    prvtY1564TestEntry.setStatus("current")


class _PrvtY1564TestName_Type(SnmpAdminString):
    """Custom type prvtY1564TestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtY1564TestName_Type.__name__ = "SnmpAdminString"
_PrvtY1564TestName_Object = MibTableColumn
prvtY1564TestName = _PrvtY1564TestName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 1),
    _PrvtY1564TestName_Type()
)
prvtY1564TestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtY1564TestName.setStatus("current")


class _PrvtY1564TestType_Type(Integer32):
    """Custom type prvtY1564TestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testHead", 1),
          ("testLoopback", 2))
    )


_PrvtY1564TestType_Type.__name__ = "Integer32"
_PrvtY1564TestType_Object = MibTableColumn
prvtY1564TestType = _PrvtY1564TestType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 2),
    _PrvtY1564TestType_Type()
)
prvtY1564TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestType.setStatus("current")


class _PrvtY1564TestMode_Type(Integer32):
    """Custom type prvtY1564TestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configurationTest", 1),
          ("performanceTest", 2),
          ("both", 3))
    )


_PrvtY1564TestMode_Type.__name__ = "Integer32"
_PrvtY1564TestMode_Object = MibTableColumn
prvtY1564TestMode = _PrvtY1564TestMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 3),
    _PrvtY1564TestMode_Type()
)
prvtY1564TestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestMode.setStatus("current")


class _PrvtY1564TestExecStatus_Type(Integer32):
    """Custom type prvtY1564TestExecStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 1),
          ("running", 2))
    )


_PrvtY1564TestExecStatus_Type.__name__ = "Integer32"
_PrvtY1564TestExecStatus_Object = MibTableColumn
prvtY1564TestExecStatus = _PrvtY1564TestExecStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 4),
    _PrvtY1564TestExecStatus_Type()
)
prvtY1564TestExecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestExecStatus.setStatus("current")


class _PrvtY1564TestSourceType_Type(Integer32):
    """Custom type prvtY1564TestSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mac", 1),
          ("mep", 2))
    )


_PrvtY1564TestSourceType_Type.__name__ = "Integer32"
_PrvtY1564TestSourceType_Object = MibTableColumn
prvtY1564TestSourceType = _PrvtY1564TestSourceType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 5),
    _PrvtY1564TestSourceType_Type()
)
prvtY1564TestSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestSourceType.setStatus("current")


class _PrvtY1564TestSource_Type(OctetString):
    """Custom type prvtY1564TestSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_PrvtY1564TestSource_Type.__name__ = "OctetString"
_PrvtY1564TestSource_Object = MibTableColumn
prvtY1564TestSource = _PrvtY1564TestSource_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 6),
    _PrvtY1564TestSource_Type()
)
prvtY1564TestSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestSource.setStatus("current")


class _PrvtY1564TestTargetType_Type(Integer32):
    """Custom type prvtY1564TestTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mac", 1),
          ("mep", 2))
    )


_PrvtY1564TestTargetType_Type.__name__ = "Integer32"
_PrvtY1564TestTargetType_Object = MibTableColumn
prvtY1564TestTargetType = _PrvtY1564TestTargetType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 7),
    _PrvtY1564TestTargetType_Type()
)
prvtY1564TestTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestTargetType.setStatus("current")


class _PrvtY1564TestTarget_Type(OctetString):
    """Custom type prvtY1564TestTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_PrvtY1564TestTarget_Type.__name__ = "OctetString"
_PrvtY1564TestTarget_Object = MibTableColumn
prvtY1564TestTarget = _PrvtY1564TestTarget_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 8),
    _PrvtY1564TestTarget_Type()
)
prvtY1564TestTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestTarget.setStatus("current")


class _PrvtY1564TestTimeout_Type(Unsigned32):
    """Custom type prvtY1564TestTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PrvtY1564TestTimeout_Type.__name__ = "Unsigned32"
_PrvtY1564TestTimeout_Object = MibTableColumn
prvtY1564TestTimeout = _PrvtY1564TestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 9),
    _PrvtY1564TestTimeout_Type()
)
prvtY1564TestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestTimeout.setStatus("current")


class _PrvtY1564TestCIR_Type(Unsigned32):
    """Custom type prvtY1564TestCIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_PrvtY1564TestCIR_Type.__name__ = "Unsigned32"
_PrvtY1564TestCIR_Object = MibTableColumn
prvtY1564TestCIR = _PrvtY1564TestCIR_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 10),
    _PrvtY1564TestCIR_Type()
)
prvtY1564TestCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestCIR.setStatus("current")


class _PrvtY1564TestEIR_Type(Unsigned32):
    """Custom type prvtY1564TestEIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_PrvtY1564TestEIR_Type.__name__ = "Unsigned32"
_PrvtY1564TestEIR_Object = MibTableColumn
prvtY1564TestEIR = _PrvtY1564TestEIR_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 11),
    _PrvtY1564TestEIR_Type()
)
prvtY1564TestEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestEIR.setStatus("current")
_PrvtY1564TestConfigurationTestTrafficPolicing_Type = TruthValue
_PrvtY1564TestConfigurationTestTrafficPolicing_Object = MibTableColumn
prvtY1564TestConfigurationTestTrafficPolicing = _PrvtY1564TestConfigurationTestTrafficPolicing_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 12),
    _PrvtY1564TestConfigurationTestTrafficPolicing_Type()
)
prvtY1564TestConfigurationTestTrafficPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestConfigurationTestTrafficPolicing.setStatus("current")


class _PrvtY1564TestConfigurationTestCirSteps_Type(Unsigned32):
    """Custom type prvtY1564TestConfigurationTestCirSteps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtY1564TestConfigurationTestCirSteps_Type.__name__ = "Unsigned32"
_PrvtY1564TestConfigurationTestCirSteps_Object = MibTableColumn
prvtY1564TestConfigurationTestCirSteps = _PrvtY1564TestConfigurationTestCirSteps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 13),
    _PrvtY1564TestConfigurationTestCirSteps_Type()
)
prvtY1564TestConfigurationTestCirSteps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestConfigurationTestCirSteps.setStatus("current")


class _PrvtY1564TestConfigurationStepDuration_Type(Unsigned32):
    """Custom type prvtY1564TestConfigurationStepDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PrvtY1564TestConfigurationStepDuration_Type.__name__ = "Unsigned32"
_PrvtY1564TestConfigurationStepDuration_Object = MibTableColumn
prvtY1564TestConfigurationStepDuration = _PrvtY1564TestConfigurationStepDuration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 14),
    _PrvtY1564TestConfigurationStepDuration_Type()
)
prvtY1564TestConfigurationStepDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestConfigurationStepDuration.setStatus("current")


class _PrvtY1564TestPerformanceTestDuration_Type(Integer32):
    """Custom type prvtY1564TestPerformanceTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              30)
        )
    )
    namedValues = NamedValues(
        *(("testDuration15min", 15),
          ("testDuration30min", 30))
    )


_PrvtY1564TestPerformanceTestDuration_Type.__name__ = "Integer32"
_PrvtY1564TestPerformanceTestDuration_Object = MibTableColumn
prvtY1564TestPerformanceTestDuration = _PrvtY1564TestPerformanceTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 15),
    _PrvtY1564TestPerformanceTestDuration_Type()
)
prvtY1564TestPerformanceTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestPerformanceTestDuration.setStatus("current")


class _PrvtY1564TestCVLAN_Type(Unsigned32):
    """Custom type prvtY1564TestCVLAN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrvtY1564TestCVLAN_Type.__name__ = "Unsigned32"
_PrvtY1564TestCVLAN_Object = MibTableColumn
prvtY1564TestCVLAN = _PrvtY1564TestCVLAN_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 16),
    _PrvtY1564TestCVLAN_Type()
)
prvtY1564TestCVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestCVLAN.setStatus("current")


class _PrvtY1564TestCVLANPriority_Type(Unsigned32):
    """Custom type prvtY1564TestCVLANPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtY1564TestCVLANPriority_Type.__name__ = "Unsigned32"
_PrvtY1564TestCVLANPriority_Object = MibTableColumn
prvtY1564TestCVLANPriority = _PrvtY1564TestCVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 17),
    _PrvtY1564TestCVLANPriority_Type()
)
prvtY1564TestCVLANPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestCVLANPriority.setStatus("current")
_PrvtY1564TestCVLANDropEligible_Type = TruthValue
_PrvtY1564TestCVLANDropEligible_Object = MibTableColumn
prvtY1564TestCVLANDropEligible = _PrvtY1564TestCVLANDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 18),
    _PrvtY1564TestCVLANDropEligible_Type()
)
prvtY1564TestCVLANDropEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestCVLANDropEligible.setStatus("current")


class _PrvtY1564TestSVLAN_Type(Unsigned32):
    """Custom type prvtY1564TestSVLAN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrvtY1564TestSVLAN_Type.__name__ = "Unsigned32"
_PrvtY1564TestSVLAN_Object = MibTableColumn
prvtY1564TestSVLAN = _PrvtY1564TestSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 19),
    _PrvtY1564TestSVLAN_Type()
)
prvtY1564TestSVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestSVLAN.setStatus("current")


class _PrvtY1564TestSVLANPriority_Type(Unsigned32):
    """Custom type prvtY1564TestSVLANPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtY1564TestSVLANPriority_Type.__name__ = "Unsigned32"
_PrvtY1564TestSVLANPriority_Object = MibTableColumn
prvtY1564TestSVLANPriority = _PrvtY1564TestSVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 20),
    _PrvtY1564TestSVLANPriority_Type()
)
prvtY1564TestSVLANPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestSVLANPriority.setStatus("current")
_PrvtY1564TestSVLANDropEligible_Type = TruthValue
_PrvtY1564TestSVLANDropEligible_Object = MibTableColumn
prvtY1564TestSVLANDropEligible = _PrvtY1564TestSVLANDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 21),
    _PrvtY1564TestSVLANDropEligible_Type()
)
prvtY1564TestSVLANDropEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestSVLANDropEligible.setStatus("current")


class _PrvtY1564TestPDUSize_Type(Integer32):
    """Custom type prvtY1564TestPDUSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128,
              256,
              512,
              1024,
              1280,
              1518,
              2000,
              9000)
        )
    )
    namedValues = NamedValues(
        *(("value64", 64),
          ("value128", 128),
          ("value256", 256),
          ("value512", 512),
          ("value1024", 1024),
          ("value1280", 1280),
          ("value1518", 1518),
          ("value2000", 2000),
          ("value9000", 9000))
    )


_PrvtY1564TestPDUSize_Type.__name__ = "Integer32"
_PrvtY1564TestPDUSize_Object = MibTableColumn
prvtY1564TestPDUSize = _PrvtY1564TestPDUSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 22),
    _PrvtY1564TestPDUSize_Type()
)
prvtY1564TestPDUSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestPDUSize.setStatus("current")


class _PrvtY1564TestLoopbackType_Type(Integer32):
    """Custom type prvtY1564TestLoopbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macSwap", 1),
          ("oam", 2))
    )


_PrvtY1564TestLoopbackType_Type.__name__ = "Integer32"
_PrvtY1564TestLoopbackType_Object = MibTableColumn
prvtY1564TestLoopbackType = _PrvtY1564TestLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 23),
    _PrvtY1564TestLoopbackType_Type()
)
prvtY1564TestLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestLoopbackType.setStatus("current")


class _PrvtY1564TestPaternType_Type(Integer32):
    """Custom type prvtY1564TestPaternType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("nullCRC", 2),
          ("prbs", 3),
          ("prbsCRC", 4),
          ("none", 8))
    )


_PrvtY1564TestPaternType_Type.__name__ = "Integer32"
_PrvtY1564TestPaternType_Object = MibTableColumn
prvtY1564TestPaternType = _PrvtY1564TestPaternType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 24),
    _PrvtY1564TestPaternType_Type()
)
prvtY1564TestPaternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtY1564TestPaternType.setStatus("current")


class _PrvtY1564TestProfileName_Type(OctetString):
    """Custom type prvtY1564TestProfileName based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtY1564TestProfileName_Type.__name__ = "OctetString"
_PrvtY1564TestProfileName_Object = MibTableColumn
prvtY1564TestProfileName = _PrvtY1564TestProfileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 25),
    _PrvtY1564TestProfileName_Type()
)
prvtY1564TestProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestProfileName.setStatus("current")
_PrvtY1564TestRowStatus_Type = RowStatus
_PrvtY1564TestRowStatus_Object = MibTableColumn
prvtY1564TestRowStatus = _PrvtY1564TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 1, 1, 1, 26),
    _PrvtY1564TestRowStatus_Type()
)
prvtY1564TestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564TestRowStatus.setStatus("current")
_PrvtY1564TestResult_ObjectIdentity = ObjectIdentity
prvtY1564TestResult = _PrvtY1564TestResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2)
)
_PrvtY1564TestResultTable_Object = MibTable
prvtY1564TestResultTable = _PrvtY1564TestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1)
)
if mibBuilder.loadTexts:
    prvtY1564TestResultTable.setStatus("current")
_PrvtY1564TestResultEntry_Object = MibTableRow
prvtY1564TestResultEntry = _PrvtY1564TestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1)
)
prvtY1564TestResultEntry.setIndexNames(
    (0, "PRVT-Y1564-MIB", "prvtY1564TestName"),
    (0, "PRVT-Y1564-MIB", "prvtY1564TestResultIndex"),
)
if mibBuilder.loadTexts:
    prvtY1564TestResultEntry.setStatus("current")
_PrvtY1564TestResultIndex_Type = Unsigned32
_PrvtY1564TestResultIndex_Object = MibTableColumn
prvtY1564TestResultIndex = _PrvtY1564TestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1, 1),
    _PrvtY1564TestResultIndex_Type()
)
prvtY1564TestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtY1564TestResultIndex.setStatus("current")
_PrvtY1564TestResultSentInformationRate_Type = Unsigned32
_PrvtY1564TestResultSentInformationRate_Object = MibTableColumn
prvtY1564TestResultSentInformationRate = _PrvtY1564TestResultSentInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1, 2),
    _PrvtY1564TestResultSentInformationRate_Type()
)
prvtY1564TestResultSentInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestResultSentInformationRate.setStatus("current")
_PrvtY1564TestResultPacketSize_Type = Unsigned32
_PrvtY1564TestResultPacketSize_Object = MibTableColumn
prvtY1564TestResultPacketSize = _PrvtY1564TestResultPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1, 3),
    _PrvtY1564TestResultPacketSize_Type()
)
prvtY1564TestResultPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestResultPacketSize.setStatus("current")


class _PrvtY1564TestResultMode_Type(Integer32):
    """Custom type prvtY1564TestResultMode based on Integer32"""
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
        *(("notAvailable", 1),
          ("configurationCIRTest", 2),
          ("configurationEIRTest", 3),
          ("configurationPolicingTest", 4),
          ("performanceTest", 5))
    )


_PrvtY1564TestResultMode_Type.__name__ = "Integer32"
_PrvtY1564TestResultMode_Object = MibTableColumn
prvtY1564TestResultMode = _PrvtY1564TestResultMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1, 4),
    _PrvtY1564TestResultMode_Type()
)
prvtY1564TestResultMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestResultMode.setStatus("current")
_PrvtY1564TestResultFrameLoss_Type = Unsigned32
_PrvtY1564TestResultFrameLoss_Object = MibTableColumn
prvtY1564TestResultFrameLoss = _PrvtY1564TestResultFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1, 5),
    _PrvtY1564TestResultFrameLoss_Type()
)
prvtY1564TestResultFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestResultFrameLoss.setStatus("current")
_PrvtY1564TestResultInformationRate_Type = Unsigned32
_PrvtY1564TestResultInformationRate_Object = MibTableColumn
prvtY1564TestResultInformationRate = _PrvtY1564TestResultInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1, 6),
    _PrvtY1564TestResultInformationRate_Type()
)
prvtY1564TestResultInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestResultInformationRate.setStatus("current")
_PrvtY1564TestResultFrameTransferDelay_Type = Unsigned32
_PrvtY1564TestResultFrameTransferDelay_Object = MibTableColumn
prvtY1564TestResultFrameTransferDelay = _PrvtY1564TestResultFrameTransferDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1, 7),
    _PrvtY1564TestResultFrameTransferDelay_Type()
)
prvtY1564TestResultFrameTransferDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestResultFrameTransferDelay.setStatus("current")
_PrvtY1564TestResutFrameDelayVariation_Type = Unsigned32
_PrvtY1564TestResutFrameDelayVariation_Object = MibTableColumn
prvtY1564TestResutFrameDelayVariation = _PrvtY1564TestResutFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1, 8),
    _PrvtY1564TestResutFrameDelayVariation_Type()
)
prvtY1564TestResutFrameDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestResutFrameDelayVariation.setStatus("current")


class _PrvtY1564TestResultStatus_Type(Integer32):
    """Custom type prvtY1564TestResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("ready", 2),
          ("error", 3))
    )


_PrvtY1564TestResultStatus_Type.__name__ = "Integer32"
_PrvtY1564TestResultStatus_Object = MibTableColumn
prvtY1564TestResultStatus = _PrvtY1564TestResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 2, 1, 1, 9),
    _PrvtY1564TestResultStatus_Type()
)
prvtY1564TestResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtY1564TestResultStatus.setStatus("current")
_PrvtY1564Profiles_ObjectIdentity = ObjectIdentity
prvtY1564Profiles = _PrvtY1564Profiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 3)
)
_PrvtY1564ProfileTable_Object = MibTable
prvtY1564ProfileTable = _PrvtY1564ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 3, 1)
)
if mibBuilder.loadTexts:
    prvtY1564ProfileTable.setStatus("current")
_PrvtY1564ProfileEntry_Object = MibTableRow
prvtY1564ProfileEntry = _PrvtY1564ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 3, 1, 1)
)
prvtY1564ProfileEntry.setIndexNames(
    (0, "PRVT-Y1564-MIB", "prvtY1564ProfileName"),
)
if mibBuilder.loadTexts:
    prvtY1564ProfileEntry.setStatus("current")


class _PrvtY1564ProfileName_Type(SnmpAdminString):
    """Custom type prvtY1564ProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtY1564ProfileName_Type.__name__ = "SnmpAdminString"
_PrvtY1564ProfileName_Object = MibTableColumn
prvtY1564ProfileName = _PrvtY1564ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 3, 1, 1, 1),
    _PrvtY1564ProfileName_Type()
)
prvtY1564ProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtY1564ProfileName.setStatus("current")


class _PrvtY1564ProfileFrameLoss_Type(Unsigned32):
    """Custom type prvtY1564ProfileFrameLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PrvtY1564ProfileFrameLoss_Type.__name__ = "Unsigned32"
_PrvtY1564ProfileFrameLoss_Object = MibTableColumn
prvtY1564ProfileFrameLoss = _PrvtY1564ProfileFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 3, 1, 1, 2),
    _PrvtY1564ProfileFrameLoss_Type()
)
prvtY1564ProfileFrameLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564ProfileFrameLoss.setStatus("current")


class _PrvtY1564ProfileFrameTransferDelay_Type(Unsigned32):
    """Custom type prvtY1564ProfileFrameTransferDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000000),
    )


_PrvtY1564ProfileFrameTransferDelay_Type.__name__ = "Unsigned32"
_PrvtY1564ProfileFrameTransferDelay_Object = MibTableColumn
prvtY1564ProfileFrameTransferDelay = _PrvtY1564ProfileFrameTransferDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 3, 1, 1, 3),
    _PrvtY1564ProfileFrameTransferDelay_Type()
)
prvtY1564ProfileFrameTransferDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564ProfileFrameTransferDelay.setStatus("current")


class _PrvtY1564ProfileFrameDelayVariation_Type(Unsigned32):
    """Custom type prvtY1564ProfileFrameDelayVariation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000000),
    )


_PrvtY1564ProfileFrameDelayVariation_Type.__name__ = "Unsigned32"
_PrvtY1564ProfileFrameDelayVariation_Object = MibTableColumn
prvtY1564ProfileFrameDelayVariation = _PrvtY1564ProfileFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 3, 1, 1, 4),
    _PrvtY1564ProfileFrameDelayVariation_Type()
)
prvtY1564ProfileFrameDelayVariation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564ProfileFrameDelayVariation.setStatus("current")
_PrvtY1564ProfileRowStatus_Type = RowStatus
_PrvtY1564ProfileRowStatus_Object = MibTableColumn
prvtY1564ProfileRowStatus = _PrvtY1564ProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 1, 3, 1, 1, 5),
    _PrvtY1564ProfileRowStatus_Type()
)
prvtY1564ProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtY1564ProfileRowStatus.setStatus("current")
_PrvtY1564Conformance_ObjectIdentity = ObjectIdentity
prvtY1564Conformance = _PrvtY1564Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 2)
)
_PrvtY1564Compliances_ObjectIdentity = ObjectIdentity
prvtY1564Compliances = _PrvtY1564Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 2, 1)
)
_PrvtY1564Groups_ObjectIdentity = ObjectIdentity
prvtY1564Groups = _PrvtY1564Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 2, 2)
)

# Managed Objects groups

prvtY1564TestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 2, 2, 1)
)
prvtY1564TestGroup.setObjects(
      *(("PRVT-Y1564-MIB", "prvtY1564TestType"),
        ("PRVT-Y1564-MIB", "prvtY1564TestMode"),
        ("PRVT-Y1564-MIB", "prvtY1564TestExecStatus"),
        ("PRVT-Y1564-MIB", "prvtY1564TestSourceType"),
        ("PRVT-Y1564-MIB", "prvtY1564TestSource"),
        ("PRVT-Y1564-MIB", "prvtY1564TestTargetType"),
        ("PRVT-Y1564-MIB", "prvtY1564TestTarget"),
        ("PRVT-Y1564-MIB", "prvtY1564TestTimeout"),
        ("PRVT-Y1564-MIB", "prvtY1564TestCIR"),
        ("PRVT-Y1564-MIB", "prvtY1564TestEIR"),
        ("PRVT-Y1564-MIB", "prvtY1564TestConfigurationTestTrafficPolicing"),
        ("PRVT-Y1564-MIB", "prvtY1564TestConfigurationTestCirSteps"),
        ("PRVT-Y1564-MIB", "prvtY1564TestConfigurationStepDuration"),
        ("PRVT-Y1564-MIB", "prvtY1564TestPerformanceTestDuration"),
        ("PRVT-Y1564-MIB", "prvtY1564TestCVLAN"),
        ("PRVT-Y1564-MIB", "prvtY1564TestCVLANPriority"),
        ("PRVT-Y1564-MIB", "prvtY1564TestCVLANDropEligible"),
        ("PRVT-Y1564-MIB", "prvtY1564TestSVLAN"),
        ("PRVT-Y1564-MIB", "prvtY1564TestSVLANPriority"),
        ("PRVT-Y1564-MIB", "prvtY1564TestSVLANDropEligible"),
        ("PRVT-Y1564-MIB", "prvtY1564TestPDUSize"),
        ("PRVT-Y1564-MIB", "prvtY1564TestLoopbackType"),
        ("PRVT-Y1564-MIB", "prvtY1564TestPaternType"),
        ("PRVT-Y1564-MIB", "prvtY1564TestProfileName"),
        ("PRVT-Y1564-MIB", "prvtY1564TestRowStatus"))
)
if mibBuilder.loadTexts:
    prvtY1564TestGroup.setStatus("current")

prvtY1564TestResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 2, 2, 2)
)
prvtY1564TestResultsGroup.setObjects(
      *(("PRVT-Y1564-MIB", "prvtY1564TestResultSentInformationRate"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResultPacketSize"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResultMode"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResultFrameLoss"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResultInformationRate"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResultFrameTransferDelay"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResutFrameDelayVariation"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResultStatus"))
)
if mibBuilder.loadTexts:
    prvtY1564TestResultsGroup.setStatus("current")

prvtY1564ProfilesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 2, 2, 3)
)
prvtY1564ProfilesGroup.setObjects(
      *(("PRVT-Y1564-MIB", "prvtY1564ProfileFrameLoss"),
        ("PRVT-Y1564-MIB", "prvtY1564ProfileFrameTransferDelay"),
        ("PRVT-Y1564-MIB", "prvtY1564ProfileFrameDelayVariation"),
        ("PRVT-Y1564-MIB", "prvtY1564ProfileRowStatus"))
)
if mibBuilder.loadTexts:
    prvtY1564ProfilesGroup.setStatus("current")


# Notification objects

prvtY1564ProbeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 0, 1)
)
prvtY1564ProbeFailed.setObjects(
      *(("PRVT-Y1564-MIB", "prvtY1564TestType"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResultStatus"))
)
if mibBuilder.loadTexts:
    prvtY1564ProbeFailed.setStatus(
        "current"
    )

prvtY1564ProbeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 0, 2)
)
prvtY1564ProbeSuccess.setObjects(
      *(("PRVT-Y1564-MIB", "prvtY1564TestType"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResultStatus"))
)
if mibBuilder.loadTexts:
    prvtY1564ProbeSuccess.setStatus(
        "current"
    )

prvtY1564TestFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 0, 3)
)
prvtY1564TestFinished.setObjects(
    ("PRVT-Y1564-MIB", "prvtY1564TestExecStatus")
)
if mibBuilder.loadTexts:
    prvtY1564TestFinished.setStatus(
        "current"
    )


# Notifications groups

prvtY1564NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 2, 2, 4)
)
prvtY1564NotificationsGroup.setObjects(
      *(("PRVT-Y1564-MIB", "prvtY1564ProbeFailed"),
        ("PRVT-Y1564-MIB", "prvtY1564ProbeSuccess"),
        ("PRVT-Y1564-MIB", "prvtY1564TestFinished"))
)
if mibBuilder.loadTexts:
    prvtY1564NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prvtY1564Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 129, 2, 1, 1)
)
prvtY1564Compliance.setObjects(
      *(("PRVT-Y1564-MIB", "prvtY1564TestGroup"),
        ("PRVT-Y1564-MIB", "prvtY1564TestResultsGroup"),
        ("PRVT-Y1564-MIB", "prvtY1564ProfilesGroup"),
        ("PRVT-Y1564-MIB", "prvtY1564NotificationsGroup"))
)
if mibBuilder.loadTexts:
    prvtY1564Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-Y1564-MIB",
    **{"prvtY1564Mib": prvtY1564Mib,
       "prvtY1564Notifications": prvtY1564Notifications,
       "prvtY1564ProbeFailed": prvtY1564ProbeFailed,
       "prvtY1564ProbeSuccess": prvtY1564ProbeSuccess,
       "prvtY1564TestFinished": prvtY1564TestFinished,
       "prvtY1564Objects": prvtY1564Objects,
       "prvtY1564Test": prvtY1564Test,
       "prvtY1564TestTable": prvtY1564TestTable,
       "prvtY1564TestEntry": prvtY1564TestEntry,
       "prvtY1564TestName": prvtY1564TestName,
       "prvtY1564TestType": prvtY1564TestType,
       "prvtY1564TestMode": prvtY1564TestMode,
       "prvtY1564TestExecStatus": prvtY1564TestExecStatus,
       "prvtY1564TestSourceType": prvtY1564TestSourceType,
       "prvtY1564TestSource": prvtY1564TestSource,
       "prvtY1564TestTargetType": prvtY1564TestTargetType,
       "prvtY1564TestTarget": prvtY1564TestTarget,
       "prvtY1564TestTimeout": prvtY1564TestTimeout,
       "prvtY1564TestCIR": prvtY1564TestCIR,
       "prvtY1564TestEIR": prvtY1564TestEIR,
       "prvtY1564TestConfigurationTestTrafficPolicing": prvtY1564TestConfigurationTestTrafficPolicing,
       "prvtY1564TestConfigurationTestCirSteps": prvtY1564TestConfigurationTestCirSteps,
       "prvtY1564TestConfigurationStepDuration": prvtY1564TestConfigurationStepDuration,
       "prvtY1564TestPerformanceTestDuration": prvtY1564TestPerformanceTestDuration,
       "prvtY1564TestCVLAN": prvtY1564TestCVLAN,
       "prvtY1564TestCVLANPriority": prvtY1564TestCVLANPriority,
       "prvtY1564TestCVLANDropEligible": prvtY1564TestCVLANDropEligible,
       "prvtY1564TestSVLAN": prvtY1564TestSVLAN,
       "prvtY1564TestSVLANPriority": prvtY1564TestSVLANPriority,
       "prvtY1564TestSVLANDropEligible": prvtY1564TestSVLANDropEligible,
       "prvtY1564TestPDUSize": prvtY1564TestPDUSize,
       "prvtY1564TestLoopbackType": prvtY1564TestLoopbackType,
       "prvtY1564TestPaternType": prvtY1564TestPaternType,
       "prvtY1564TestProfileName": prvtY1564TestProfileName,
       "prvtY1564TestRowStatus": prvtY1564TestRowStatus,
       "prvtY1564TestResult": prvtY1564TestResult,
       "prvtY1564TestResultTable": prvtY1564TestResultTable,
       "prvtY1564TestResultEntry": prvtY1564TestResultEntry,
       "prvtY1564TestResultIndex": prvtY1564TestResultIndex,
       "prvtY1564TestResultSentInformationRate": prvtY1564TestResultSentInformationRate,
       "prvtY1564TestResultPacketSize": prvtY1564TestResultPacketSize,
       "prvtY1564TestResultMode": prvtY1564TestResultMode,
       "prvtY1564TestResultFrameLoss": prvtY1564TestResultFrameLoss,
       "prvtY1564TestResultInformationRate": prvtY1564TestResultInformationRate,
       "prvtY1564TestResultFrameTransferDelay": prvtY1564TestResultFrameTransferDelay,
       "prvtY1564TestResutFrameDelayVariation": prvtY1564TestResutFrameDelayVariation,
       "prvtY1564TestResultStatus": prvtY1564TestResultStatus,
       "prvtY1564Profiles": prvtY1564Profiles,
       "prvtY1564ProfileTable": prvtY1564ProfileTable,
       "prvtY1564ProfileEntry": prvtY1564ProfileEntry,
       "prvtY1564ProfileName": prvtY1564ProfileName,
       "prvtY1564ProfileFrameLoss": prvtY1564ProfileFrameLoss,
       "prvtY1564ProfileFrameTransferDelay": prvtY1564ProfileFrameTransferDelay,
       "prvtY1564ProfileFrameDelayVariation": prvtY1564ProfileFrameDelayVariation,
       "prvtY1564ProfileRowStatus": prvtY1564ProfileRowStatus,
       "prvtY1564Conformance": prvtY1564Conformance,
       "prvtY1564Compliances": prvtY1564Compliances,
       "prvtY1564Compliance": prvtY1564Compliance,
       "prvtY1564Groups": prvtY1564Groups,
       "prvtY1564TestGroup": prvtY1564TestGroup,
       "prvtY1564TestResultsGroup": prvtY1564TestResultsGroup,
       "prvtY1564ProfilesGroup": prvtY1564ProfilesGroup,
       "prvtY1564NotificationsGroup": prvtY1564NotificationsGroup}
)
