# SNMP MIB module (PRVT-SAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SAA-MIB

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

prvtSaaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130)
)
if mibBuilder.loadTexts:
    prvtSaaMib.setRevisions(
        ("2015-03-25 00:00",
         "2014-05-16 00:00",
         "2011-10-20 00:00",
         "2011-02-07 00:00",
         "2010-09-29 00:00",
         "2010-09-27 00:00",
         "2010-09-13 00:00",
         "2010-08-24 00:00",
         "2010-05-05 00:00",
         "2010-03-26 00:00",
         "2010-03-18 00:00",
         "2010-03-12 00:00",
         "2010-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtTwampTestNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class PrvtTwampDecimalPercent(TextualConvention, OctetString):
    status = "current"
    displayHint = "3d.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )



# MIB Managed Objects in the order of their OIDs

_PrvtSaaNotifications_ObjectIdentity = ObjectIdentity
prvtSaaNotifications = _PrvtSaaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0)
)
_PrvtSaaObjects_ObjectIdentity = ObjectIdentity
prvtSaaObjects = _PrvtSaaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1)
)
_PrvtSaaTest_ObjectIdentity = ObjectIdentity
prvtSaaTest = _PrvtSaaTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1)
)
_PrvtSaaY1731PmTestTable_Object = MibTable
prvtSaaY1731PmTestTable = _PrvtSaaY1731PmTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestTable.setStatus("current")
_PrvtSaaY1731PmTestEntry_Object = MibTableRow
prvtSaaY1731PmTestEntry = _PrvtSaaY1731PmTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1)
)
prvtSaaY1731PmTestEntry.setIndexNames(
    (0, "PRVT-SAA-MIB", "prvtSaaY1731PmTestOwner"),
    (0, "PRVT-SAA-MIB", "prvtSaaY1731PmTestName"),
)
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestEntry.setStatus("current")


class _PrvtSaaY1731PmTestOwner_Type(SnmpAdminString):
    """Custom type prvtSaaY1731PmTestOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtSaaY1731PmTestOwner_Type.__name__ = "SnmpAdminString"
_PrvtSaaY1731PmTestOwner_Object = MibTableColumn
prvtSaaY1731PmTestOwner = _PrvtSaaY1731PmTestOwner_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 1),
    _PrvtSaaY1731PmTestOwner_Type()
)
prvtSaaY1731PmTestOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestOwner.setStatus("current")


class _PrvtSaaY1731PmTestName_Type(SnmpAdminString):
    """Custom type prvtSaaY1731PmTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtSaaY1731PmTestName_Type.__name__ = "SnmpAdminString"
_PrvtSaaY1731PmTestName_Object = MibTableColumn
prvtSaaY1731PmTestName = _PrvtSaaY1731PmTestName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 2),
    _PrvtSaaY1731PmTestName_Type()
)
prvtSaaY1731PmTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestName.setStatus("current")


class _PrvtSaaY1731PmTestType_Type(Integer32):
    """Custom type prvtSaaY1731PmTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frameloss", 1),
          ("framedelayAndDelayvariation", 2),
          ("framelossAndFramedelayAndDelayvariation", 3))
    )


_PrvtSaaY1731PmTestType_Type.__name__ = "Integer32"
_PrvtSaaY1731PmTestType_Object = MibTableColumn
prvtSaaY1731PmTestType = _PrvtSaaY1731PmTestType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 3),
    _PrvtSaaY1731PmTestType_Type()
)
prvtSaaY1731PmTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestType.setStatus("current")


class _PrvtSaaY1731PmTestExecStatus_Type(Integer32):
    """Custom type prvtSaaY1731PmTestExecStatus based on Integer32"""
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


_PrvtSaaY1731PmTestExecStatus_Type.__name__ = "Integer32"
_PrvtSaaY1731PmTestExecStatus_Object = MibTableColumn
prvtSaaY1731PmTestExecStatus = _PrvtSaaY1731PmTestExecStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 4),
    _PrvtSaaY1731PmTestExecStatus_Type()
)
prvtSaaY1731PmTestExecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestExecStatus.setStatus("current")


class _PrvtSaaY1731PmTestEncapType_Type(Integer32):
    """Custom type prvtSaaY1731PmTestEncapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("service", 2),
          ("vlan", 3))
    )


_PrvtSaaY1731PmTestEncapType_Type.__name__ = "Integer32"
_PrvtSaaY1731PmTestEncapType_Object = MibTableColumn
prvtSaaY1731PmTestEncapType = _PrvtSaaY1731PmTestEncapType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 5),
    _PrvtSaaY1731PmTestEncapType_Type()
)
prvtSaaY1731PmTestEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestEncapType.setStatus("current")


class _PrvtSaaY1731PmTestEncapValue_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestEncapValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PrvtSaaY1731PmTestEncapValue_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestEncapValue_Object = MibTableColumn
prvtSaaY1731PmTestEncapValue = _PrvtSaaY1731PmTestEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 6),
    _PrvtSaaY1731PmTestEncapValue_Type()
)
prvtSaaY1731PmTestEncapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestEncapValue.setStatus("current")
_PrvtSaaY1731PmTestUserPort_Type = Unsigned32
_PrvtSaaY1731PmTestUserPort_Object = MibTableColumn
prvtSaaY1731PmTestUserPort = _PrvtSaaY1731PmTestUserPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 7),
    _PrvtSaaY1731PmTestUserPort_Type()
)
prvtSaaY1731PmTestUserPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestUserPort.setStatus("current")
_PrvtSaaY1731PmTestUplinkPort_Type = Unsigned32
_PrvtSaaY1731PmTestUplinkPort_Object = MibTableColumn
prvtSaaY1731PmTestUplinkPort = _PrvtSaaY1731PmTestUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 8),
    _PrvtSaaY1731PmTestUplinkPort_Type()
)
prvtSaaY1731PmTestUplinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestUplinkPort.setStatus("current")


class _PrvtSaaY1731PmTestTargetMac_Type(DisplayString):
    """Custom type prvtSaaY1731PmTestTargetMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_PrvtSaaY1731PmTestTargetMac_Type.__name__ = "DisplayString"
_PrvtSaaY1731PmTestTargetMac_Object = MibTableColumn
prvtSaaY1731PmTestTargetMac = _PrvtSaaY1731PmTestTargetMac_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 9),
    _PrvtSaaY1731PmTestTargetMac_Type()
)
prvtSaaY1731PmTestTargetMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestTargetMac.setStatus("current")


class _PrvtSaaY1731PmTestCfmDomainLevel_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestCfmDomainLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtSaaY1731PmTestCfmDomainLevel_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestCfmDomainLevel_Object = MibTableColumn
prvtSaaY1731PmTestCfmDomainLevel = _PrvtSaaY1731PmTestCfmDomainLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 10),
    _PrvtSaaY1731PmTestCfmDomainLevel_Type()
)
prvtSaaY1731PmTestCfmDomainLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestCfmDomainLevel.setStatus("current")


class _PrvtSaaY1731PmTestRemoteCfmMep_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestRemoteCfmMep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_PrvtSaaY1731PmTestRemoteCfmMep_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestRemoteCfmMep_Object = MibTableColumn
prvtSaaY1731PmTestRemoteCfmMep = _PrvtSaaY1731PmTestRemoteCfmMep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 11),
    _PrvtSaaY1731PmTestRemoteCfmMep_Type()
)
prvtSaaY1731PmTestRemoteCfmMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestRemoteCfmMep.setStatus("current")


class _PrvtSaaY1731PmTestProfile_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_PrvtSaaY1731PmTestProfile_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestProfile_Object = MibTableColumn
prvtSaaY1731PmTestProfile = _PrvtSaaY1731PmTestProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 12),
    _PrvtSaaY1731PmTestProfile_Type()
)
prvtSaaY1731PmTestProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestProfile.setStatus("current")


class _PrvtSaaY1731PmTestHistoryDepth_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestHistoryDepth based on Unsigned32"""
    defaultValue = 96

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_PrvtSaaY1731PmTestHistoryDepth_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestHistoryDepth_Object = MibTableColumn
prvtSaaY1731PmTestHistoryDepth = _PrvtSaaY1731PmTestHistoryDepth_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 13),
    _PrvtSaaY1731PmTestHistoryDepth_Type()
)
prvtSaaY1731PmTestHistoryDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestHistoryDepth.setStatus("current")


class _PrvtSaaY1731PmTestPeriod_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestPeriod based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_PrvtSaaY1731PmTestPeriod_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestPeriod_Object = MibTableColumn
prvtSaaY1731PmTestPeriod = _PrvtSaaY1731PmTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 14),
    _PrvtSaaY1731PmTestPeriod_Type()
)
prvtSaaY1731PmTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestPeriod.setStatus("current")


class _PrvtSaaY1731PmTestTimeout_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PrvtSaaY1731PmTestTimeout_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestTimeout_Object = MibTableColumn
prvtSaaY1731PmTestTimeout = _PrvtSaaY1731PmTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 15),
    _PrvtSaaY1731PmTestTimeout_Type()
)
prvtSaaY1731PmTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestTimeout.setStatus("current")


class _PrvtSaaY1731PmTestMonitorInterval_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestMonitorInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PrvtSaaY1731PmTestMonitorInterval_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestMonitorInterval_Object = MibTableColumn
prvtSaaY1731PmTestMonitorInterval = _PrvtSaaY1731PmTestMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 16),
    _PrvtSaaY1731PmTestMonitorInterval_Type()
)
prvtSaaY1731PmTestMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestMonitorInterval.setStatus("current")


class _PrvtSaaY1731PmTestFrequency_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestFrequency based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtSaaY1731PmTestFrequency_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestFrequency_Object = MibTableColumn
prvtSaaY1731PmTestFrequency = _PrvtSaaY1731PmTestFrequency_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 17),
    _PrvtSaaY1731PmTestFrequency_Type()
)
prvtSaaY1731PmTestFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestFrequency.setStatus("current")


class _PrvtSaaY1731PmTestClocksInSync_Type(TruthValue):
    """Custom type prvtSaaY1731PmTestClocksInSync based on TruthValue"""
    defaultValue = 2


_PrvtSaaY1731PmTestClocksInSync_Type.__name__ = "TruthValue"
_PrvtSaaY1731PmTestClocksInSync_Object = MibTableColumn
prvtSaaY1731PmTestClocksInSync = _PrvtSaaY1731PmTestClocksInSync_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 18),
    _PrvtSaaY1731PmTestClocksInSync_Type()
)
prvtSaaY1731PmTestClocksInSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestClocksInSync.setStatus("current")


class _PrvtSaaY1731PmTestDelayMethod_Type(Integer32):
    """Custom type prvtSaaY1731PmTestDelayMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("percentile", 2))
    )


_PrvtSaaY1731PmTestDelayMethod_Type.__name__ = "Integer32"
_PrvtSaaY1731PmTestDelayMethod_Object = MibTableColumn
prvtSaaY1731PmTestDelayMethod = _PrvtSaaY1731PmTestDelayMethod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 19),
    _PrvtSaaY1731PmTestDelayMethod_Type()
)
prvtSaaY1731PmTestDelayMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestDelayMethod.setStatus("current")


class _PrvtSaaY1731PmTestDelayPvalue_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestDelayPvalue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PrvtSaaY1731PmTestDelayPvalue_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestDelayPvalue_Object = MibTableColumn
prvtSaaY1731PmTestDelayPvalue = _PrvtSaaY1731PmTestDelayPvalue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 20),
    _PrvtSaaY1731PmTestDelayPvalue_Type()
)
prvtSaaY1731PmTestDelayPvalue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestDelayPvalue.setStatus("current")


class _PrvtSaaY1731PmTestJitterMethod_Type(Integer32):
    """Custom type prvtSaaY1731PmTestJitterMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("peakToPeak", 1),
          ("variance", 2),
          ("percentile", 3))
    )


_PrvtSaaY1731PmTestJitterMethod_Type.__name__ = "Integer32"
_PrvtSaaY1731PmTestJitterMethod_Object = MibTableColumn
prvtSaaY1731PmTestJitterMethod = _PrvtSaaY1731PmTestJitterMethod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 21),
    _PrvtSaaY1731PmTestJitterMethod_Type()
)
prvtSaaY1731PmTestJitterMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestJitterMethod.setStatus("current")


class _PrvtSaaY1731PmTestJitterPvalue_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestJitterPvalue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PrvtSaaY1731PmTestJitterPvalue_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestJitterPvalue_Object = MibTableColumn
prvtSaaY1731PmTestJitterPvalue = _PrvtSaaY1731PmTestJitterPvalue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 22),
    _PrvtSaaY1731PmTestJitterPvalue_Type()
)
prvtSaaY1731PmTestJitterPvalue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestJitterPvalue.setStatus("current")


class _PrvtSaaY1731PmTestPriority_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtSaaY1731PmTestPriority_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestPriority_Object = MibTableColumn
prvtSaaY1731PmTestPriority = _PrvtSaaY1731PmTestPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 23),
    _PrvtSaaY1731PmTestPriority_Type()
)
prvtSaaY1731PmTestPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestPriority.setStatus("current")
_PrvtSaaY1731PmTestRowStatus_Type = RowStatus
_PrvtSaaY1731PmTestRowStatus_Object = MibTableColumn
prvtSaaY1731PmTestRowStatus = _PrvtSaaY1731PmTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 24),
    _PrvtSaaY1731PmTestRowStatus_Type()
)
prvtSaaY1731PmTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestRowStatus.setStatus("current")


class _PrvtSaaY1731PmTestCCMAPSCount_Type(TruthValue):
    """Custom type prvtSaaY1731PmTestCCMAPSCount based on TruthValue"""
    defaultValue = 2


_PrvtSaaY1731PmTestCCMAPSCount_Type.__name__ = "TruthValue"
_PrvtSaaY1731PmTestCCMAPSCount_Object = MibTableColumn
prvtSaaY1731PmTestCCMAPSCount = _PrvtSaaY1731PmTestCCMAPSCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 25),
    _PrvtSaaY1731PmTestCCMAPSCount_Type()
)
prvtSaaY1731PmTestCCMAPSCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestCCMAPSCount.setStatus("current")


class _PrvtSaaY1731PmTestLossMeasurementType_Type(Integer32):
    """Custom type prvtSaaY1731PmTestLossMeasurementType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lmm", 0),
          ("slm", 1))
    )


_PrvtSaaY1731PmTestLossMeasurementType_Type.__name__ = "Integer32"
_PrvtSaaY1731PmTestLossMeasurementType_Object = MibTableColumn
prvtSaaY1731PmTestLossMeasurementType = _PrvtSaaY1731PmTestLossMeasurementType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 26),
    _PrvtSaaY1731PmTestLossMeasurementType_Type()
)
prvtSaaY1731PmTestLossMeasurementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestLossMeasurementType.setStatus("current")


class _PrvtSaaY1731PmTestSLMTransmit_Type(TruthValue):
    """Custom type prvtSaaY1731PmTestSLMTransmit based on TruthValue"""
    defaultValue = 2


_PrvtSaaY1731PmTestSLMTransmit_Type.__name__ = "TruthValue"
_PrvtSaaY1731PmTestSLMTransmit_Object = MibTableColumn
prvtSaaY1731PmTestSLMTransmit = _PrvtSaaY1731PmTestSLMTransmit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 27),
    _PrvtSaaY1731PmTestSLMTransmit_Type()
)
prvtSaaY1731PmTestSLMTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestSLMTransmit.setStatus("current")


class _PrvtSaaY1731PmTestTestId_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestTestId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PrvtSaaY1731PmTestTestId_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestTestId_Object = MibTableColumn
prvtSaaY1731PmTestTestId = _PrvtSaaY1731PmTestTestId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 28),
    _PrvtSaaY1731PmTestTestId_Type()
)
prvtSaaY1731PmTestTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestTestId.setStatus("current")


class _PrvtSaaY1731PmTestDropEligible_Type(TruthValue):
    """Custom type prvtSaaY1731PmTestDropEligible based on TruthValue"""
    defaultValue = 2


_PrvtSaaY1731PmTestDropEligible_Type.__name__ = "TruthValue"
_PrvtSaaY1731PmTestDropEligible_Object = MibTableColumn
prvtSaaY1731PmTestDropEligible = _PrvtSaaY1731PmTestDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 29),
    _PrvtSaaY1731PmTestDropEligible_Type()
)
prvtSaaY1731PmTestDropEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestDropEligible.setStatus("current")


class _PrvtSaaY1731PmTestDataSize_Type(Unsigned32):
    """Custom type prvtSaaY1731PmTestDataSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_PrvtSaaY1731PmTestDataSize_Type.__name__ = "Unsigned32"
_PrvtSaaY1731PmTestDataSize_Object = MibTableColumn
prvtSaaY1731PmTestDataSize = _PrvtSaaY1731PmTestDataSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 30),
    _PrvtSaaY1731PmTestDataSize_Type()
)
prvtSaaY1731PmTestDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestDataSize.setStatus("current")


class _PrvtSaaY1731PmTestCountAllPriorities_Type(TruthValue):
    """Custom type prvtSaaY1731PmTestCountAllPriorities based on TruthValue"""
    defaultValue = 2


_PrvtSaaY1731PmTestCountAllPriorities_Type.__name__ = "TruthValue"
_PrvtSaaY1731PmTestCountAllPriorities_Object = MibTableColumn
prvtSaaY1731PmTestCountAllPriorities = _PrvtSaaY1731PmTestCountAllPriorities_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 1, 1, 31),
    _PrvtSaaY1731PmTestCountAllPriorities_Type()
)
prvtSaaY1731PmTestCountAllPriorities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731PmTestCountAllPriorities.setStatus("current")
_PrvtSaaRFC2544ThroughputTestTable_Object = MibTable
prvtSaaRFC2544ThroughputTestTable = _PrvtSaaRFC2544ThroughputTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2)
)
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestTable.setStatus("current")
_PrvtSaaRFC2544ThroughputTestEntry_Object = MibTableRow
prvtSaaRFC2544ThroughputTestEntry = _PrvtSaaRFC2544ThroughputTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1)
)
prvtSaaRFC2544ThroughputTestEntry.setIndexNames(
    (0, "PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestOwner"),
    (0, "PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestName"),
)
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestEntry.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestOwner_Type(SnmpAdminString):
    """Custom type prvtSaaRFC2544ThroughputTestOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtSaaRFC2544ThroughputTestOwner_Type.__name__ = "SnmpAdminString"
_PrvtSaaRFC2544ThroughputTestOwner_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestOwner = _PrvtSaaRFC2544ThroughputTestOwner_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 1),
    _PrvtSaaRFC2544ThroughputTestOwner_Type()
)
prvtSaaRFC2544ThroughputTestOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestOwner.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestName_Type(SnmpAdminString):
    """Custom type prvtSaaRFC2544ThroughputTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtSaaRFC2544ThroughputTestName_Type.__name__ = "SnmpAdminString"
_PrvtSaaRFC2544ThroughputTestName_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestName = _PrvtSaaRFC2544ThroughputTestName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 2),
    _PrvtSaaRFC2544ThroughputTestName_Type()
)
prvtSaaRFC2544ThroughputTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestName.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestType_Type(Integer32):
    """Custom type prvtSaaRFC2544ThroughputTestType based on Integer32"""
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
        *(("unidirectionalTestHead", 1),
          ("bidirectionalTestHead", 2),
          ("testTail", 3),
          ("testLoopback", 4))
    )


_PrvtSaaRFC2544ThroughputTestType_Type.__name__ = "Integer32"
_PrvtSaaRFC2544ThroughputTestType_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestType = _PrvtSaaRFC2544ThroughputTestType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 3),
    _PrvtSaaRFC2544ThroughputTestType_Type()
)
prvtSaaRFC2544ThroughputTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestType.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestExecStatus_Type(Integer32):
    """Custom type prvtSaaRFC2544ThroughputTestExecStatus based on Integer32"""
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


_PrvtSaaRFC2544ThroughputTestExecStatus_Type.__name__ = "Integer32"
_PrvtSaaRFC2544ThroughputTestExecStatus_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestExecStatus = _PrvtSaaRFC2544ThroughputTestExecStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 4),
    _PrvtSaaRFC2544ThroughputTestExecStatus_Type()
)
prvtSaaRFC2544ThroughputTestExecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestExecStatus.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestSourceType_Type(Integer32):
    """Custom type prvtSaaRFC2544ThroughputTestSourceType based on Integer32"""
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


_PrvtSaaRFC2544ThroughputTestSourceType_Type.__name__ = "Integer32"
_PrvtSaaRFC2544ThroughputTestSourceType_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestSourceType = _PrvtSaaRFC2544ThroughputTestSourceType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 5),
    _PrvtSaaRFC2544ThroughputTestSourceType_Type()
)
prvtSaaRFC2544ThroughputTestSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestSourceType.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestSource_Type(OctetString):
    """Custom type prvtSaaRFC2544ThroughputTestSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_PrvtSaaRFC2544ThroughputTestSource_Type.__name__ = "OctetString"
_PrvtSaaRFC2544ThroughputTestSource_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestSource = _PrvtSaaRFC2544ThroughputTestSource_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 6),
    _PrvtSaaRFC2544ThroughputTestSource_Type()
)
prvtSaaRFC2544ThroughputTestSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestSource.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestTargetType_Type(Integer32):
    """Custom type prvtSaaRFC2544ThroughputTestTargetType based on Integer32"""
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


_PrvtSaaRFC2544ThroughputTestTargetType_Type.__name__ = "Integer32"
_PrvtSaaRFC2544ThroughputTestTargetType_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestTargetType = _PrvtSaaRFC2544ThroughputTestTargetType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 7),
    _PrvtSaaRFC2544ThroughputTestTargetType_Type()
)
prvtSaaRFC2544ThroughputTestTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestTargetType.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestTarget_Type(OctetString):
    """Custom type prvtSaaRFC2544ThroughputTestTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_PrvtSaaRFC2544ThroughputTestTarget_Type.__name__ = "OctetString"
_PrvtSaaRFC2544ThroughputTestTarget_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestTarget = _PrvtSaaRFC2544ThroughputTestTarget_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 8),
    _PrvtSaaRFC2544ThroughputTestTarget_Type()
)
prvtSaaRFC2544ThroughputTestTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestTarget.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestTimeout_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PrvtSaaRFC2544ThroughputTestTimeout_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestTimeout_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestTimeout = _PrvtSaaRFC2544ThroughputTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 9),
    _PrvtSaaRFC2544ThroughputTestTimeout_Type()
)
prvtSaaRFC2544ThroughputTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestTimeout.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestCIR_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestCIR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_PrvtSaaRFC2544ThroughputTestCIR_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestCIR_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestCIR = _PrvtSaaRFC2544ThroughputTestCIR_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 10),
    _PrvtSaaRFC2544ThroughputTestCIR_Type()
)
prvtSaaRFC2544ThroughputTestCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestCIR.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestCBS_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestCBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2048),
    )


_PrvtSaaRFC2544ThroughputTestCBS_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestCBS_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestCBS = _PrvtSaaRFC2544ThroughputTestCBS_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 11),
    _PrvtSaaRFC2544ThroughputTestCBS_Type()
)
prvtSaaRFC2544ThroughputTestCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestCBS.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestBurstPercentage_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestBurstPercentage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PrvtSaaRFC2544ThroughputTestBurstPercentage_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestBurstPercentage_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestBurstPercentage = _PrvtSaaRFC2544ThroughputTestBurstPercentage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 12),
    _PrvtSaaRFC2544ThroughputTestBurstPercentage_Type()
)
prvtSaaRFC2544ThroughputTestBurstPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestBurstPercentage.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestDuration_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_PrvtSaaRFC2544ThroughputTestDuration_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestDuration_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestDuration = _PrvtSaaRFC2544ThroughputTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 13),
    _PrvtSaaRFC2544ThroughputTestDuration_Type()
)
prvtSaaRFC2544ThroughputTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestDuration.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestMaxFrameloss_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestMaxFrameloss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PrvtSaaRFC2544ThroughputTestMaxFrameloss_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestMaxFrameloss_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestMaxFrameloss = _PrvtSaaRFC2544ThroughputTestMaxFrameloss_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 14),
    _PrvtSaaRFC2544ThroughputTestMaxFrameloss_Type()
)
prvtSaaRFC2544ThroughputTestMaxFrameloss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestMaxFrameloss.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestCVLAN0_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestCVLAN0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrvtSaaRFC2544ThroughputTestCVLAN0_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestCVLAN0_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestCVLAN0 = _PrvtSaaRFC2544ThroughputTestCVLAN0_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 15),
    _PrvtSaaRFC2544ThroughputTestCVLAN0_Type()
)
prvtSaaRFC2544ThroughputTestCVLAN0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestCVLAN0.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestCVLAN0Priority_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestCVLAN0Priority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtSaaRFC2544ThroughputTestCVLAN0Priority_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestCVLAN0Priority_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestCVLAN0Priority = _PrvtSaaRFC2544ThroughputTestCVLAN0Priority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 16),
    _PrvtSaaRFC2544ThroughputTestCVLAN0Priority_Type()
)
prvtSaaRFC2544ThroughputTestCVLAN0Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestCVLAN0Priority.setStatus("current")
_PrvtSaaRFC2544ThroughputTestCVLAN0DropEligible_Type = TruthValue
_PrvtSaaRFC2544ThroughputTestCVLAN0DropEligible_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestCVLAN0DropEligible = _PrvtSaaRFC2544ThroughputTestCVLAN0DropEligible_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 17),
    _PrvtSaaRFC2544ThroughputTestCVLAN0DropEligible_Type()
)
prvtSaaRFC2544ThroughputTestCVLAN0DropEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestCVLAN0DropEligible.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestSVLAN_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestSVLAN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrvtSaaRFC2544ThroughputTestSVLAN_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestSVLAN_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestSVLAN = _PrvtSaaRFC2544ThroughputTestSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 18),
    _PrvtSaaRFC2544ThroughputTestSVLAN_Type()
)
prvtSaaRFC2544ThroughputTestSVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestSVLAN.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestSVLANPriority_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestSVLANPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtSaaRFC2544ThroughputTestSVLANPriority_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestSVLANPriority_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestSVLANPriority = _PrvtSaaRFC2544ThroughputTestSVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 19),
    _PrvtSaaRFC2544ThroughputTestSVLANPriority_Type()
)
prvtSaaRFC2544ThroughputTestSVLANPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestSVLANPriority.setStatus("current")
_PrvtSaaRFC2544ThroughputTestSVLANDropEligible_Type = TruthValue
_PrvtSaaRFC2544ThroughputTestSVLANDropEligible_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestSVLANDropEligible = _PrvtSaaRFC2544ThroughputTestSVLANDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 20),
    _PrvtSaaRFC2544ThroughputTestSVLANDropEligible_Type()
)
prvtSaaRFC2544ThroughputTestSVLANDropEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestSVLANDropEligible.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestPDUSize_Type(DisplayString):
    """Custom type prvtSaaRFC2544ThroughputTestPDUSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_PrvtSaaRFC2544ThroughputTestPDUSize_Type.__name__ = "DisplayString"
_PrvtSaaRFC2544ThroughputTestPDUSize_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestPDUSize = _PrvtSaaRFC2544ThroughputTestPDUSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 21),
    _PrvtSaaRFC2544ThroughputTestPDUSize_Type()
)
prvtSaaRFC2544ThroughputTestPDUSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestPDUSize.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestACKTimeout_Type(Unsigned32):
    """Custom type prvtSaaRFC2544ThroughputTestACKTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PrvtSaaRFC2544ThroughputTestACKTimeout_Type.__name__ = "Unsigned32"
_PrvtSaaRFC2544ThroughputTestACKTimeout_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestACKTimeout = _PrvtSaaRFC2544ThroughputTestACKTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 22),
    _PrvtSaaRFC2544ThroughputTestACKTimeout_Type()
)
prvtSaaRFC2544ThroughputTestACKTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestACKTimeout.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestLoopbackType_Type(Integer32):
    """Custom type prvtSaaRFC2544ThroughputTestLoopbackType based on Integer32"""
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


_PrvtSaaRFC2544ThroughputTestLoopbackType_Type.__name__ = "Integer32"
_PrvtSaaRFC2544ThroughputTestLoopbackType_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestLoopbackType = _PrvtSaaRFC2544ThroughputTestLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 23),
    _PrvtSaaRFC2544ThroughputTestLoopbackType_Type()
)
prvtSaaRFC2544ThroughputTestLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestLoopbackType.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestPaternType_Type(Integer32):
    """Custom type prvtSaaRFC2544ThroughputTestPaternType based on Integer32"""
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


_PrvtSaaRFC2544ThroughputTestPaternType_Type.__name__ = "Integer32"
_PrvtSaaRFC2544ThroughputTestPaternType_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestPaternType = _PrvtSaaRFC2544ThroughputTestPaternType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 24),
    _PrvtSaaRFC2544ThroughputTestPaternType_Type()
)
prvtSaaRFC2544ThroughputTestPaternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestPaternType.setStatus("current")
_PrvtSaaRFC2544ThroughputTestRowStatus_Type = RowStatus
_PrvtSaaRFC2544ThroughputTestRowStatus_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestRowStatus = _PrvtSaaRFC2544ThroughputTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 25),
    _PrvtSaaRFC2544ThroughputTestRowStatus_Type()
)
prvtSaaRFC2544ThroughputTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestRowStatus.setStatus("current")


class _PrvtSaaRFC2544ThroughputTestEthertype_Type(OctetString):
    """Custom type prvtSaaRFC2544ThroughputTestEthertype based on OctetString"""
    defaultHexValue = "8902"


_PrvtSaaRFC2544ThroughputTestEthertype_Type.__name__ = "OctetString"
_PrvtSaaRFC2544ThroughputTestEthertype_Object = MibTableColumn
prvtSaaRFC2544ThroughputTestEthertype = _PrvtSaaRFC2544ThroughputTestEthertype_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 2, 1, 26),
    _PrvtSaaRFC2544ThroughputTestEthertype_Type()
)
prvtSaaRFC2544ThroughputTestEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSaaRFC2544ThroughputTestEthertype.setStatus("current")
_PrvtSaaY1731LoopbackTestTable_Object = MibTable
prvtSaaY1731LoopbackTestTable = _PrvtSaaY1731LoopbackTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3)
)
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestTable.setStatus("current")
_PrvtSaaY1731LoopbackTestEntry_Object = MibTableRow
prvtSaaY1731LoopbackTestEntry = _PrvtSaaY1731LoopbackTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3, 1)
)
prvtSaaY1731LoopbackTestEntry.setIndexNames(
    (0, "PRVT-SAA-MIB", "prvtSaaY1731LoopbackTestEncapType"),
    (0, "PRVT-SAA-MIB", "prvtSaaY1731LoopbackTestEncapValue"),
)
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestEntry.setStatus("current")


class _PrvtSaaY1731LoopbackTestEncapType_Type(Integer32):
    """Custom type prvtSaaY1731LoopbackTestEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("service", 1),
          ("vlan", 2))
    )


_PrvtSaaY1731LoopbackTestEncapType_Type.__name__ = "Integer32"
_PrvtSaaY1731LoopbackTestEncapType_Object = MibTableColumn
prvtSaaY1731LoopbackTestEncapType = _PrvtSaaY1731LoopbackTestEncapType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3, 1, 1),
    _PrvtSaaY1731LoopbackTestEncapType_Type()
)
prvtSaaY1731LoopbackTestEncapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestEncapType.setStatus("current")


class _PrvtSaaY1731LoopbackTestEncapValue_Type(Unsigned32):
    """Custom type prvtSaaY1731LoopbackTestEncapValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PrvtSaaY1731LoopbackTestEncapValue_Type.__name__ = "Unsigned32"
_PrvtSaaY1731LoopbackTestEncapValue_Object = MibTableColumn
prvtSaaY1731LoopbackTestEncapValue = _PrvtSaaY1731LoopbackTestEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3, 1, 2),
    _PrvtSaaY1731LoopbackTestEncapValue_Type()
)
prvtSaaY1731LoopbackTestEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestEncapValue.setStatus("current")
_PrvtSaaY1731LoopbackTestUserPort_Type = Unsigned32
_PrvtSaaY1731LoopbackTestUserPort_Object = MibTableColumn
prvtSaaY1731LoopbackTestUserPort = _PrvtSaaY1731LoopbackTestUserPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3, 1, 3),
    _PrvtSaaY1731LoopbackTestUserPort_Type()
)
prvtSaaY1731LoopbackTestUserPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestUserPort.setStatus("current")
_PrvtSaaY1731LoopbackTestUplinkPort_Type = Unsigned32
_PrvtSaaY1731LoopbackTestUplinkPort_Object = MibTableColumn
prvtSaaY1731LoopbackTestUplinkPort = _PrvtSaaY1731LoopbackTestUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3, 1, 4),
    _PrvtSaaY1731LoopbackTestUplinkPort_Type()
)
prvtSaaY1731LoopbackTestUplinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestUplinkPort.setStatus("current")


class _PrvtSaaY1731LoopbackTestType_Type(Integer32):
    """Custom type prvtSaaY1731LoopbackTestType based on Integer32"""
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
        *(("none", 1),
          ("frameloss", 2),
          ("delayvariation", 3),
          ("framelossAndDelayvariation", 4))
    )


_PrvtSaaY1731LoopbackTestType_Type.__name__ = "Integer32"
_PrvtSaaY1731LoopbackTestType_Object = MibTableColumn
prvtSaaY1731LoopbackTestType = _PrvtSaaY1731LoopbackTestType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3, 1, 5),
    _PrvtSaaY1731LoopbackTestType_Type()
)
prvtSaaY1731LoopbackTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestType.setStatus("current")
_PrvtSaaY1731LoopbackTestRowStatus_Type = RowStatus
_PrvtSaaY1731LoopbackTestRowStatus_Object = MibTableColumn
prvtSaaY1731LoopbackTestRowStatus = _PrvtSaaY1731LoopbackTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3, 1, 6),
    _PrvtSaaY1731LoopbackTestRowStatus_Type()
)
prvtSaaY1731LoopbackTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestRowStatus.setStatus("current")


class _PrvtSaaY1731LoopbackTestCCMAPSCount_Type(TruthValue):
    """Custom type prvtSaaY1731LoopbackTestCCMAPSCount based on TruthValue"""
    defaultValue = 2


_PrvtSaaY1731LoopbackTestCCMAPSCount_Type.__name__ = "TruthValue"
_PrvtSaaY1731LoopbackTestCCMAPSCount_Object = MibTableColumn
prvtSaaY1731LoopbackTestCCMAPSCount = _PrvtSaaY1731LoopbackTestCCMAPSCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3, 1, 7),
    _PrvtSaaY1731LoopbackTestCCMAPSCount_Type()
)
prvtSaaY1731LoopbackTestCCMAPSCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestCCMAPSCount.setStatus("current")


class _PrvtSaaY1731LoopbackTestCountAllPriorities_Type(TruthValue):
    """Custom type prvtSaaY1731LoopbackTestCountAllPriorities based on TruthValue"""
    defaultValue = 2


_PrvtSaaY1731LoopbackTestCountAllPriorities_Type.__name__ = "TruthValue"
_PrvtSaaY1731LoopbackTestCountAllPriorities_Object = MibTableColumn
prvtSaaY1731LoopbackTestCountAllPriorities = _PrvtSaaY1731LoopbackTestCountAllPriorities_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 1, 3, 1, 8),
    _PrvtSaaY1731LoopbackTestCountAllPriorities_Type()
)
prvtSaaY1731LoopbackTestCountAllPriorities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestCountAllPriorities.setStatus("current")
_PrvtSaaTestResult_ObjectIdentity = ObjectIdentity
prvtSaaTestResult = _PrvtSaaTestResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2)
)
_PrvtSaaY1731TestResultTable_Object = MibTable
prvtSaaY1731TestResultTable = _PrvtSaaY1731TestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1)
)
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultTable.setStatus("current")
_PrvtSaaY1731TestResultEntry_Object = MibTableRow
prvtSaaY1731TestResultEntry = _PrvtSaaY1731TestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1)
)
prvtSaaY1731TestResultEntry.setIndexNames(
    (0, "PRVT-SAA-MIB", "prvtSaaY1731PmTestOwner"),
    (0, "PRVT-SAA-MIB", "prvtSaaY1731PmTestName"),
    (0, "PRVT-SAA-MIB", "prvtSaaY1731TestResultIndex"),
)
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultEntry.setStatus("current")
_PrvtSaaY1731TestResultIndex_Type = Unsigned32
_PrvtSaaY1731TestResultIndex_Object = MibTableColumn
prvtSaaY1731TestResultIndex = _PrvtSaaY1731TestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 1),
    _PrvtSaaY1731TestResultIndex_Type()
)
prvtSaaY1731TestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultIndex.setStatus("current")
_PrvtSaaY1731TestResultDelayNE_Type = Unsigned32
_PrvtSaaY1731TestResultDelayNE_Object = MibTableColumn
prvtSaaY1731TestResultDelayNE = _PrvtSaaY1731TestResultDelayNE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 2),
    _PrvtSaaY1731TestResultDelayNE_Type()
)
prvtSaaY1731TestResultDelayNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultDelayNE.setStatus("current")
_PrvtSaaY1731TestResultDelayFE_Type = Unsigned32
_PrvtSaaY1731TestResultDelayFE_Object = MibTableColumn
prvtSaaY1731TestResultDelayFE = _PrvtSaaY1731TestResultDelayFE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 3),
    _PrvtSaaY1731TestResultDelayFE_Type()
)
prvtSaaY1731TestResultDelayFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultDelayFE.setStatus("current")
_PrvtSaaY1731TestResultJitterNE_Type = Unsigned32
_PrvtSaaY1731TestResultJitterNE_Object = MibTableColumn
prvtSaaY1731TestResultJitterNE = _PrvtSaaY1731TestResultJitterNE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 4),
    _PrvtSaaY1731TestResultJitterNE_Type()
)
prvtSaaY1731TestResultJitterNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultJitterNE.setStatus("current")
_PrvtSaaY1731TestResultJitterFE_Type = Unsigned32
_PrvtSaaY1731TestResultJitterFE_Object = MibTableColumn
prvtSaaY1731TestResultJitterFE = _PrvtSaaY1731TestResultJitterFE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 5),
    _PrvtSaaY1731TestResultJitterFE_Type()
)
prvtSaaY1731TestResultJitterFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultJitterFE.setStatus("current")
_PrvtSaaY1731TestResultFrameLossNE_Type = Unsigned32
_PrvtSaaY1731TestResultFrameLossNE_Object = MibTableColumn
prvtSaaY1731TestResultFrameLossNE = _PrvtSaaY1731TestResultFrameLossNE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 6),
    _PrvtSaaY1731TestResultFrameLossNE_Type()
)
prvtSaaY1731TestResultFrameLossNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultFrameLossNE.setStatus("current")
_PrvtSaaY1731TestResultFrameLossFE_Type = Unsigned32
_PrvtSaaY1731TestResultFrameLossFE_Object = MibTableColumn
prvtSaaY1731TestResultFrameLossFE = _PrvtSaaY1731TestResultFrameLossFE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 7),
    _PrvtSaaY1731TestResultFrameLossFE_Type()
)
prvtSaaY1731TestResultFrameLossFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultFrameLossFE.setStatus("current")
_PrvtSaaY1731TestResultFramesSentNE_Type = Counter32
_PrvtSaaY1731TestResultFramesSentNE_Object = MibTableColumn
prvtSaaY1731TestResultFramesSentNE = _PrvtSaaY1731TestResultFramesSentNE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 8),
    _PrvtSaaY1731TestResultFramesSentNE_Type()
)
prvtSaaY1731TestResultFramesSentNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultFramesSentNE.setStatus("current")
_PrvtSaaY1731TestResultFramesSentFE_Type = Counter32
_PrvtSaaY1731TestResultFramesSentFE_Object = MibTableColumn
prvtSaaY1731TestResultFramesSentFE = _PrvtSaaY1731TestResultFramesSentFE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 9),
    _PrvtSaaY1731TestResultFramesSentFE_Type()
)
prvtSaaY1731TestResultFramesSentFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultFramesSentFE.setStatus("current")
_PrvtSaaY1731TestResultFramesRcvdNE_Type = Counter32
_PrvtSaaY1731TestResultFramesRcvdNE_Object = MibTableColumn
prvtSaaY1731TestResultFramesRcvdNE = _PrvtSaaY1731TestResultFramesRcvdNE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 10),
    _PrvtSaaY1731TestResultFramesRcvdNE_Type()
)
prvtSaaY1731TestResultFramesRcvdNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultFramesRcvdNE.setStatus("current")
_PrvtSaaY1731TestResultFramesRcvdFE_Type = Counter32
_PrvtSaaY1731TestResultFramesRcvdFE_Object = MibTableColumn
prvtSaaY1731TestResultFramesRcvdFE = _PrvtSaaY1731TestResultFramesRcvdFE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 11),
    _PrvtSaaY1731TestResultFramesRcvdFE_Type()
)
prvtSaaY1731TestResultFramesRcvdFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultFramesRcvdFE.setStatus("current")
_PrvtSaaY1731TestResultPacketsSent_Type = Counter32
_PrvtSaaY1731TestResultPacketsSent_Object = MibTableColumn
prvtSaaY1731TestResultPacketsSent = _PrvtSaaY1731TestResultPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 12),
    _PrvtSaaY1731TestResultPacketsSent_Type()
)
prvtSaaY1731TestResultPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultPacketsSent.setStatus("current")
_PrvtSaaY1731TestResultNoTimeouts_Type = Unsigned32
_PrvtSaaY1731TestResultNoTimeouts_Object = MibTableColumn
prvtSaaY1731TestResultNoTimeouts = _PrvtSaaY1731TestResultNoTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 13),
    _PrvtSaaY1731TestResultNoTimeouts_Type()
)
prvtSaaY1731TestResultNoTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultNoTimeouts.setStatus("current")
_PrvtSaaY1731TestResultNoErrors_Type = Unsigned32
_PrvtSaaY1731TestResultNoErrors_Object = MibTableColumn
prvtSaaY1731TestResultNoErrors = _PrvtSaaY1731TestResultNoErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 14),
    _PrvtSaaY1731TestResultNoErrors_Type()
)
prvtSaaY1731TestResultNoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultNoErrors.setStatus("current")
_PrvtSaaY1731TestResultCompletionTime_Type = Unsigned32
_PrvtSaaY1731TestResultCompletionTime_Object = MibTableColumn
prvtSaaY1731TestResultCompletionTime = _PrvtSaaY1731TestResultCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 1, 1, 15),
    _PrvtSaaY1731TestResultCompletionTime_Type()
)
prvtSaaY1731TestResultCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultCompletionTime.setStatus("current")
_PrvtSaaRFC2544TestResultTable_Object = MibTable
prvtSaaRFC2544TestResultTable = _PrvtSaaRFC2544TestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2)
)
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultTable.setStatus("current")
_PrvtSaaRFC2544TestResultEntry_Object = MibTableRow
prvtSaaRFC2544TestResultEntry = _PrvtSaaRFC2544TestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1)
)
prvtSaaRFC2544TestResultEntry.setIndexNames(
    (0, "PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestOwner"),
    (0, "PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestName"),
    (0, "PRVT-SAA-MIB", "prvtSaaRFC2544TestResultIndex"),
)
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultEntry.setStatus("current")
_PrvtSaaRFC2544TestResultIndex_Type = Unsigned32
_PrvtSaaRFC2544TestResultIndex_Object = MibTableColumn
prvtSaaRFC2544TestResultIndex = _PrvtSaaRFC2544TestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1, 1),
    _PrvtSaaRFC2544TestResultIndex_Type()
)
prvtSaaRFC2544TestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultIndex.setStatus("current")
_PrvtSaaRFC2544TestResultFrameSize_Type = Unsigned32
_PrvtSaaRFC2544TestResultFrameSize_Object = MibTableColumn
prvtSaaRFC2544TestResultFrameSize = _PrvtSaaRFC2544TestResultFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1, 2),
    _PrvtSaaRFC2544TestResultFrameSize_Type()
)
prvtSaaRFC2544TestResultFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultFrameSize.setStatus("current")
_PrvtSaaRFC2544TestResultFrameLoss_Type = Unsigned32
_PrvtSaaRFC2544TestResultFrameLoss_Object = MibTableColumn
prvtSaaRFC2544TestResultFrameLoss = _PrvtSaaRFC2544TestResultFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1, 3),
    _PrvtSaaRFC2544TestResultFrameLoss_Type()
)
prvtSaaRFC2544TestResultFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultFrameLoss.setStatus("current")
_PrvtSaaRFC2544TestResultThroughput_Type = Unsigned32
_PrvtSaaRFC2544TestResultThroughput_Object = MibTableColumn
prvtSaaRFC2544TestResultThroughput = _PrvtSaaRFC2544TestResultThroughput_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1, 4),
    _PrvtSaaRFC2544TestResultThroughput_Type()
)
prvtSaaRFC2544TestResultThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultThroughput.setStatus("current")
_PrvtSaaRFC2544TestResultNetThroughput_Type = Unsigned32
_PrvtSaaRFC2544TestResultNetThroughput_Object = MibTableColumn
prvtSaaRFC2544TestResultNetThroughput = _PrvtSaaRFC2544TestResultNetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1, 5),
    _PrvtSaaRFC2544TestResultNetThroughput_Type()
)
prvtSaaRFC2544TestResultNetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultNetThroughput.setStatus("current")


class _PrvtSaaRFC2544TestResultStatus_Type(Integer32):
    """Custom type prvtSaaRFC2544TestResultStatus based on Integer32"""
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


_PrvtSaaRFC2544TestResultStatus_Type.__name__ = "Integer32"
_PrvtSaaRFC2544TestResultStatus_Object = MibTableColumn
prvtSaaRFC2544TestResultStatus = _PrvtSaaRFC2544TestResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1, 6),
    _PrvtSaaRFC2544TestResultStatus_Type()
)
prvtSaaRFC2544TestResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultStatus.setStatus("current")
_PrvtSaaRFC2544TestResultDelayMinimum_Type = Unsigned32
_PrvtSaaRFC2544TestResultDelayMinimum_Object = MibTableColumn
prvtSaaRFC2544TestResultDelayMinimum = _PrvtSaaRFC2544TestResultDelayMinimum_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1, 7),
    _PrvtSaaRFC2544TestResultDelayMinimum_Type()
)
prvtSaaRFC2544TestResultDelayMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultDelayMinimum.setStatus("current")
_PrvtSaaRFC2544TestResultDelayAverage_Type = Unsigned32
_PrvtSaaRFC2544TestResultDelayAverage_Object = MibTableColumn
prvtSaaRFC2544TestResultDelayAverage = _PrvtSaaRFC2544TestResultDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1, 8),
    _PrvtSaaRFC2544TestResultDelayAverage_Type()
)
prvtSaaRFC2544TestResultDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultDelayAverage.setStatus("current")
_PrvtSaaRFC2544TestResultDelayMaximum_Type = Unsigned32
_PrvtSaaRFC2544TestResultDelayMaximum_Object = MibTableColumn
prvtSaaRFC2544TestResultDelayMaximum = _PrvtSaaRFC2544TestResultDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 2, 2, 1, 9),
    _PrvtSaaRFC2544TestResultDelayMaximum_Type()
)
prvtSaaRFC2544TestResultDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultDelayMaximum.setStatus("current")
_PrvtSaaProfiles_ObjectIdentity = ObjectIdentity
prvtSaaProfiles = _PrvtSaaProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3)
)
_PrvtSaaProfileTable_Object = MibTable
prvtSaaProfileTable = _PrvtSaaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1)
)
if mibBuilder.loadTexts:
    prvtSaaProfileTable.setStatus("current")
_PrvtSaaProfileEntry_Object = MibTableRow
prvtSaaProfileEntry = _PrvtSaaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1)
)
prvtSaaProfileEntry.setIndexNames(
    (0, "PRVT-SAA-MIB", "prvtSaaProfileIndex"),
)
if mibBuilder.loadTexts:
    prvtSaaProfileEntry.setStatus("current")


class _PrvtSaaProfileIndex_Type(Unsigned32):
    """Custom type prvtSaaProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PrvtSaaProfileIndex_Type.__name__ = "Unsigned32"
_PrvtSaaProfileIndex_Object = MibTableColumn
prvtSaaProfileIndex = _PrvtSaaProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1, 1),
    _PrvtSaaProfileIndex_Type()
)
prvtSaaProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSaaProfileIndex.setStatus("current")


class _PrvtSaaProfileDelayNE_Type(Unsigned32):
    """Custom type prvtSaaProfileDelayNE based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000000),
    )


_PrvtSaaProfileDelayNE_Type.__name__ = "Unsigned32"
_PrvtSaaProfileDelayNE_Object = MibTableColumn
prvtSaaProfileDelayNE = _PrvtSaaProfileDelayNE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1, 2),
    _PrvtSaaProfileDelayNE_Type()
)
prvtSaaProfileDelayNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaProfileDelayNE.setStatus("current")


class _PrvtSaaProfileDelayFE_Type(Unsigned32):
    """Custom type prvtSaaProfileDelayFE based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000000),
    )


_PrvtSaaProfileDelayFE_Type.__name__ = "Unsigned32"
_PrvtSaaProfileDelayFE_Object = MibTableColumn
prvtSaaProfileDelayFE = _PrvtSaaProfileDelayFE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1, 3),
    _PrvtSaaProfileDelayFE_Type()
)
prvtSaaProfileDelayFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaProfileDelayFE.setStatus("current")


class _PrvtSaaProfileJitterNE_Type(Unsigned32):
    """Custom type prvtSaaProfileJitterNE based on Unsigned32"""
    defaultValue = 300000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000000),
    )


_PrvtSaaProfileJitterNE_Type.__name__ = "Unsigned32"
_PrvtSaaProfileJitterNE_Object = MibTableColumn
prvtSaaProfileJitterNE = _PrvtSaaProfileJitterNE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1, 4),
    _PrvtSaaProfileJitterNE_Type()
)
prvtSaaProfileJitterNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaProfileJitterNE.setStatus("current")


class _PrvtSaaProfileJitterFE_Type(Unsigned32):
    """Custom type prvtSaaProfileJitterFE based on Unsigned32"""
    defaultValue = 300000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000000),
    )


_PrvtSaaProfileJitterFE_Type.__name__ = "Unsigned32"
_PrvtSaaProfileJitterFE_Object = MibTableColumn
prvtSaaProfileJitterFE = _PrvtSaaProfileJitterFE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1, 5),
    _PrvtSaaProfileJitterFE_Type()
)
prvtSaaProfileJitterFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaProfileJitterFE.setStatus("current")


class _PrvtSaaProfileFrameLossNE_Type(Unsigned32):
    """Custom type prvtSaaProfileFrameLossNE based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PrvtSaaProfileFrameLossNE_Type.__name__ = "Unsigned32"
_PrvtSaaProfileFrameLossNE_Object = MibTableColumn
prvtSaaProfileFrameLossNE = _PrvtSaaProfileFrameLossNE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1, 6),
    _PrvtSaaProfileFrameLossNE_Type()
)
prvtSaaProfileFrameLossNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaProfileFrameLossNE.setStatus("current")


class _PrvtSaaProfileFrameLossFE_Type(Unsigned32):
    """Custom type prvtSaaProfileFrameLossFE based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PrvtSaaProfileFrameLossFE_Type.__name__ = "Unsigned32"
_PrvtSaaProfileFrameLossFE_Object = MibTableColumn
prvtSaaProfileFrameLossFE = _PrvtSaaProfileFrameLossFE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1, 7),
    _PrvtSaaProfileFrameLossFE_Type()
)
prvtSaaProfileFrameLossFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSaaProfileFrameLossFE.setStatus("current")
_PrvtSaaProfileRowStatus_Type = RowStatus
_PrvtSaaProfileRowStatus_Object = MibTableColumn
prvtSaaProfileRowStatus = _PrvtSaaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1, 8),
    _PrvtSaaProfileRowStatus_Type()
)
prvtSaaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSaaProfileRowStatus.setStatus("current")


class _PrvtSaaProfileName_Type(OctetString):
    """Custom type prvtSaaProfileName based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtSaaProfileName_Type.__name__ = "OctetString"
_PrvtSaaProfileName_Object = MibTableColumn
prvtSaaProfileName = _PrvtSaaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 3, 1, 1, 9),
    _PrvtSaaProfileName_Type()
)
prvtSaaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSaaProfileName.setStatus("current")
_PrvtTwampObjects_ObjectIdentity = ObjectIdentity
prvtTwampObjects = _PrvtTwampObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4)
)
_PrvtTwampTest_ObjectIdentity = ObjectIdentity
prvtTwampTest = _PrvtTwampTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1)
)
_PrvtTwampTestTable_Object = MibTable
prvtTwampTestTable = _PrvtTwampTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    prvtTwampTestTable.setStatus("current")
_PrvtTwampTestEntry_Object = MibTableRow
prvtTwampTestEntry = _PrvtTwampTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1, 1)
)
prvtTwampTestEntry.setIndexNames(
    (0, "PRVT-SAA-MIB", "prvtTwampTestName"),
)
if mibBuilder.loadTexts:
    prvtTwampTestEntry.setStatus("current")
_PrvtTwampTestName_Type = PrvtTwampTestNameType
_PrvtTwampTestName_Object = MibTableColumn
prvtTwampTestName = _PrvtTwampTestName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1, 1, 1),
    _PrvtTwampTestName_Type()
)
prvtTwampTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtTwampTestName.setStatus("current")
_PrvtTwampTestRowStatus_Type = RowStatus
_PrvtTwampTestRowStatus_Object = MibTableColumn
prvtTwampTestRowStatus = _PrvtTwampTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1, 1, 2),
    _PrvtTwampTestRowStatus_Type()
)
prvtTwampTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestRowStatus.setStatus("current")
_PrvtTwampTestServer_Type = IpAddress
_PrvtTwampTestServer_Object = MibTableColumn
prvtTwampTestServer = _PrvtTwampTestServer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1, 1, 3),
    _PrvtTwampTestServer_Type()
)
prvtTwampTestServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestServer.setStatus("current")


class _PrvtTwampTestSessionsCount_Type(Integer32):
    """Custom type prvtTwampTestSessionsCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtTwampTestSessionsCount_Type.__name__ = "Integer32"
_PrvtTwampTestSessionsCount_Object = MibTableColumn
prvtTwampTestSessionsCount = _PrvtTwampTestSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1, 1, 4),
    _PrvtTwampTestSessionsCount_Type()
)
prvtTwampTestSessionsCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestSessionsCount.setStatus("current")


class _PrvtTwampTestPackets_Type(Integer32):
    """Custom type prvtTwampTestPackets based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_PrvtTwampTestPackets_Type.__name__ = "Integer32"
_PrvtTwampTestPackets_Object = MibTableColumn
prvtTwampTestPackets = _PrvtTwampTestPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1, 1, 5),
    _PrvtTwampTestPackets_Type()
)
prvtTwampTestPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestPackets.setStatus("current")


class _PrvtTwampTestTimeout_Type(Integer32):
    """Custom type prvtTwampTestTimeout based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_PrvtTwampTestTimeout_Type.__name__ = "Integer32"
_PrvtTwampTestTimeout_Object = MibTableColumn
prvtTwampTestTimeout = _PrvtTwampTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1, 1, 6),
    _PrvtTwampTestTimeout_Type()
)
prvtTwampTestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestTimeout.setStatus("current")


class _PrvtTwampTestDelay_Type(Integer32):
    """Custom type prvtTwampTestDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_PrvtTwampTestDelay_Type.__name__ = "Integer32"
_PrvtTwampTestDelay_Object = MibTableColumn
prvtTwampTestDelay = _PrvtTwampTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1, 1, 7),
    _PrvtTwampTestDelay_Type()
)
prvtTwampTestDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestDelay.setStatus("current")


class _PrvtTwampTestExecuteNow_Type(Integer32):
    """Custom type prvtTwampTestExecuteNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PrvtTwampTestExecuteNow_Type.__name__ = "Integer32"
_PrvtTwampTestExecuteNow_Object = MibTableColumn
prvtTwampTestExecuteNow = _PrvtTwampTestExecuteNow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 1, 1, 1, 8),
    _PrvtTwampTestExecuteNow_Type()
)
prvtTwampTestExecuteNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestExecuteNow.setStatus("current")
_PrvtTwampServer_ObjectIdentity = ObjectIdentity
prvtTwampServer = _PrvtTwampServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2)
)


class _PrvtTwampServerInnactivity_Type(Integer32):
    """Custom type prvtTwampServerInnactivity based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_PrvtTwampServerInnactivity_Type.__name__ = "Integer32"
_PrvtTwampServerInnactivity_Object = MibScalar
prvtTwampServerInnactivity = _PrvtTwampServerInnactivity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 1),
    _PrvtTwampServerInnactivity_Type()
)
prvtTwampServerInnactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerInnactivity.setStatus("current")


class _PrvtTwampServerSessionInnactivity_Type(Integer32):
    """Custom type prvtTwampServerSessionInnactivity based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_PrvtTwampServerSessionInnactivity_Type.__name__ = "Integer32"
_PrvtTwampServerSessionInnactivity_Object = MibScalar
prvtTwampServerSessionInnactivity = _PrvtTwampServerSessionInnactivity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 2),
    _PrvtTwampServerSessionInnactivity_Type()
)
prvtTwampServerSessionInnactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerSessionInnactivity.setStatus("current")


class _PrvtTwampServerMaxSessions_Type(Integer32):
    """Custom type prvtTwampServerMaxSessions based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PrvtTwampServerMaxSessions_Type.__name__ = "Integer32"
_PrvtTwampServerMaxSessions_Object = MibScalar
prvtTwampServerMaxSessions = _PrvtTwampServerMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 3),
    _PrvtTwampServerMaxSessions_Type()
)
prvtTwampServerMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerMaxSessions.setStatus("current")


class _PrvtTwampServerMaxParallelSessions_Type(Integer32):
    """Custom type prvtTwampServerMaxParallelSessions based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtTwampServerMaxParallelSessions_Type.__name__ = "Integer32"
_PrvtTwampServerMaxParallelSessions_Object = MibScalar
prvtTwampServerMaxParallelSessions = _PrvtTwampServerMaxParallelSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 4),
    _PrvtTwampServerMaxParallelSessions_Type()
)
prvtTwampServerMaxParallelSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerMaxParallelSessions.setStatus("current")


class _PrvtTwampServerShutdown_Type(TruthValue):
    """Custom type prvtTwampServerShutdown based on TruthValue"""
    defaultValue = 2


_PrvtTwampServerShutdown_Type.__name__ = "TruthValue"
_PrvtTwampServerShutdown_Object = MibScalar
prvtTwampServerShutdown = _PrvtTwampServerShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 5),
    _PrvtTwampServerShutdown_Type()
)
prvtTwampServerShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerShutdown.setStatus("current")
_PrvtTwampClientTable_Object = MibTable
prvtTwampClientTable = _PrvtTwampClientTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 6)
)
if mibBuilder.loadTexts:
    prvtTwampClientTable.setStatus("current")
_PrvtTwampClientEntry_Object = MibTableRow
prvtTwampClientEntry = _PrvtTwampClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 6, 1)
)
prvtTwampClientEntry.setIndexNames(
    (0, "PRVT-SAA-MIB", "prvtTwampClientIp"),
)
if mibBuilder.loadTexts:
    prvtTwampClientEntry.setStatus("current")
_PrvtTwampClientIp_Type = IpAddress
_PrvtTwampClientIp_Object = MibTableColumn
prvtTwampClientIp = _PrvtTwampClientIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 6, 1, 1),
    _PrvtTwampClientIp_Type()
)
prvtTwampClientIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtTwampClientIp.setStatus("current")
_PrvtTwampClientRowStatus_Type = RowStatus
_PrvtTwampClientRowStatus_Object = MibTableColumn
prvtTwampClientRowStatus = _PrvtTwampClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 6, 1, 2),
    _PrvtTwampClientRowStatus_Type()
)
prvtTwampClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampClientRowStatus.setStatus("current")
_PrvtTwampServerControlSessions_Type = Integer32
_PrvtTwampServerControlSessions_Object = MibScalar
prvtTwampServerControlSessions = _PrvtTwampServerControlSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 7),
    _PrvtTwampServerControlSessions_Type()
)
prvtTwampServerControlSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampServerControlSessions.setStatus("current")
_PrvtTwampServerTestSessions_Type = Integer32
_PrvtTwampServerTestSessions_Object = MibScalar
prvtTwampServerTestSessions = _PrvtTwampServerTestSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 2, 8),
    _PrvtTwampServerTestSessions_Type()
)
prvtTwampServerTestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampServerTestSessions.setStatus("current")
_PrvtTwampTestResult_ObjectIdentity = ObjectIdentity
prvtTwampTestResult = _PrvtTwampTestResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3)
)
_PrvtTwampTestResultTable_Object = MibTable
prvtTwampTestResultTable = _PrvtTwampTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    prvtTwampTestResultTable.setStatus("current")
_PrvtTwampTestResultEntry_Object = MibTableRow
prvtTwampTestResultEntry = _PrvtTwampTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1)
)
prvtTwampTestResultEntry.setIndexNames(
    (0, "PRVT-SAA-MIB", "prvtTwampTestId"),
)
if mibBuilder.loadTexts:
    prvtTwampTestResultEntry.setStatus("current")
_PrvtTwampTestId_Type = Unsigned32
_PrvtTwampTestId_Object = MibTableColumn
prvtTwampTestId = _PrvtTwampTestId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 1),
    _PrvtTwampTestId_Type()
)
prvtTwampTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestId.setStatus("current")
_PrvtTwampTestResultName_Type = PrvtTwampTestNameType
_PrvtTwampTestResultName_Object = MibTableColumn
prvtTwampTestResultName = _PrvtTwampTestResultName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 2),
    _PrvtTwampTestResultName_Type()
)
prvtTwampTestResultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestResultName.setStatus("current")
_PrvtTwampTestStartTime_Type = Unsigned32
_PrvtTwampTestStartTime_Object = MibTableColumn
prvtTwampTestStartTime = _PrvtTwampTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 3),
    _PrvtTwampTestStartTime_Type()
)
prvtTwampTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestStartTime.setStatus("current")
_PrvtTwampTestServerAddress_Type = IpAddress
_PrvtTwampTestServerAddress_Object = MibTableColumn
prvtTwampTestServerAddress = _PrvtTwampTestServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 4),
    _PrvtTwampTestServerAddress_Type()
)
prvtTwampTestServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestServerAddress.setStatus("current")


class _PrvtTwampTestSessions_Type(Unsigned32):
    """Custom type prvtTwampTestSessions based on Unsigned32"""
    defaultValue = 0


_PrvtTwampTestSessions_Type.__name__ = "Unsigned32"
_PrvtTwampTestSessions_Object = MibTableColumn
prvtTwampTestSessions = _PrvtTwampTestSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 5),
    _PrvtTwampTestSessions_Type()
)
prvtTwampTestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestSessions.setStatus("current")


class _PrvtTwampTestState_Type(Integer32):
    """Custom type prvtTwampTestState based on Integer32"""
    defaultValue = 2

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
        *(("failed", 1),
          ("running", 2),
          ("stopped", 3),
          ("finished", 4))
    )


_PrvtTwampTestState_Type.__name__ = "Integer32"
_PrvtTwampTestState_Object = MibTableColumn
prvtTwampTestState = _PrvtTwampTestState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 6),
    _PrvtTwampTestState_Type()
)
prvtTwampTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestState.setStatus("current")


class _PrvtTwampTestRtt_Type(Counter64):
    """Custom type prvtTwampTestRtt based on Counter64"""
    defaultValue = 0


_PrvtTwampTestRtt_Type.__name__ = "Counter64"
_PrvtTwampTestRtt_Object = MibTableColumn
prvtTwampTestRtt = _PrvtTwampTestRtt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 7),
    _PrvtTwampTestRtt_Type()
)
prvtTwampTestRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestRtt.setStatus("current")


class _PrvtTwampTestMinRtt_Type(Counter64):
    """Custom type prvtTwampTestMinRtt based on Counter64"""
    defaultValue = 0


_PrvtTwampTestMinRtt_Type.__name__ = "Counter64"
_PrvtTwampTestMinRtt_Object = MibTableColumn
prvtTwampTestMinRtt = _PrvtTwampTestMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 8),
    _PrvtTwampTestMinRtt_Type()
)
prvtTwampTestMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestMinRtt.setStatus("current")


class _PrvtTwampTestMaxRtt_Type(Counter64):
    """Custom type prvtTwampTestMaxRtt based on Counter64"""
    defaultValue = 0


_PrvtTwampTestMaxRtt_Type.__name__ = "Counter64"
_PrvtTwampTestMaxRtt_Object = MibTableColumn
prvtTwampTestMaxRtt = _PrvtTwampTestMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 9),
    _PrvtTwampTestMaxRtt_Type()
)
prvtTwampTestMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestMaxRtt.setStatus("current")


class _PrvtTwampTestPcktSent_Type(Unsigned32):
    """Custom type prvtTwampTestPcktSent based on Unsigned32"""
    defaultValue = 0


_PrvtTwampTestPcktSent_Type.__name__ = "Unsigned32"
_PrvtTwampTestPcktSent_Object = MibTableColumn
prvtTwampTestPcktSent = _PrvtTwampTestPcktSent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 10),
    _PrvtTwampTestPcktSent_Type()
)
prvtTwampTestPcktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestPcktSent.setStatus("current")


class _PrvtTwampTestPcktLost_Type(Unsigned32):
    """Custom type prvtTwampTestPcktLost based on Unsigned32"""
    defaultValue = 0


_PrvtTwampTestPcktLost_Type.__name__ = "Unsigned32"
_PrvtTwampTestPcktLost_Object = MibTableColumn
prvtTwampTestPcktLost = _PrvtTwampTestPcktLost_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 11),
    _PrvtTwampTestPcktLost_Type()
)
prvtTwampTestPcktLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestPcktLost.setStatus("current")


class _PrvtTwampTestPcktDrop_Type(Unsigned32):
    """Custom type prvtTwampTestPcktDrop based on Unsigned32"""
    defaultValue = 0


_PrvtTwampTestPcktDrop_Type.__name__ = "Unsigned32"
_PrvtTwampTestPcktDrop_Object = MibTableColumn
prvtTwampTestPcktDrop = _PrvtTwampTestPcktDrop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 12),
    _PrvtTwampTestPcktDrop_Type()
)
prvtTwampTestPcktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestPcktDrop.setStatus("current")


class _PrvtTwampTestVariation_Type(Counter64):
    """Custom type prvtTwampTestVariation based on Counter64"""
    defaultValue = 0


_PrvtTwampTestVariation_Type.__name__ = "Counter64"
_PrvtTwampTestVariation_Object = MibTableColumn
prvtTwampTestVariation = _PrvtTwampTestVariation_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 13),
    _PrvtTwampTestVariation_Type()
)
prvtTwampTestVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestVariation.setStatus("current")
_PrvtTwampTestVariationLow_Type = PrvtTwampDecimalPercent
_PrvtTwampTestVariationLow_Object = MibTableColumn
prvtTwampTestVariationLow = _PrvtTwampTestVariationLow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 14),
    _PrvtTwampTestVariationLow_Type()
)
prvtTwampTestVariationLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestVariationLow.setStatus("current")
_PrvtTwampTestVariationMiddle_Type = PrvtTwampDecimalPercent
_PrvtTwampTestVariationMiddle_Object = MibTableColumn
prvtTwampTestVariationMiddle = _PrvtTwampTestVariationMiddle_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 15),
    _PrvtTwampTestVariationMiddle_Type()
)
prvtTwampTestVariationMiddle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestVariationMiddle.setStatus("current")
_PrvtTwampTestVariationHigh_Type = PrvtTwampDecimalPercent
_PrvtTwampTestVariationHigh_Object = MibTableColumn
prvtTwampTestVariationHigh = _PrvtTwampTestVariationHigh_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 1, 4, 3, 1, 1, 16),
    _PrvtTwampTestVariationHigh_Type()
)
prvtTwampTestVariationHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestVariationHigh.setStatus("current")
_PrvtSaaConformance_ObjectIdentity = ObjectIdentity
prvtSaaConformance = _PrvtSaaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2)
)
_PrvtSaaCompliances_ObjectIdentity = ObjectIdentity
prvtSaaCompliances = _PrvtSaaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 1)
)
_PrvtSaaGroups_ObjectIdentity = ObjectIdentity
prvtSaaGroups = _PrvtSaaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 2)
)

# Managed Objects groups

prvtSaaY1731TestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 2, 1)
)
prvtSaaY1731TestGroup.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731PmTestType"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestExecStatus"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestEncapType"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestEncapValue"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestUserPort"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestUplinkPort"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestTargetMac"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestCfmDomainLevel"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestRemoteCfmMep"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestProfile"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestHistoryDepth"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestPeriod"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestTimeout"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestMonitorInterval"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestFrequency"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestClocksInSync"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestDelayMethod"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestDelayPvalue"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestJitterMethod"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestJitterPvalue"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestPriority"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestCCMAPSCount"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestLossMeasurementType"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestSLMTransmit"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestTestId"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestDropEligible"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestDataSize"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestRowStatus"),
        ("PRVT-SAA-MIB", "prvtSaaY1731PmTestCountAllPriorities"))
)
if mibBuilder.loadTexts:
    prvtSaaY1731TestGroup.setStatus("current")

prvtSaaRFC2544TestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 2, 2)
)
prvtSaaRFC2544TestGroup.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestType"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestExecStatus"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestSourceType"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestSource"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestTargetType"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestTarget"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestTimeout"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestCIR"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestCBS"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestBurstPercentage"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestDuration"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestMaxFrameloss"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestCVLAN0"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestCVLAN0Priority"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestCVLAN0DropEligible"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestSVLAN"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestSVLANPriority"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestSVLANDropEligible"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestPDUSize"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestACKTimeout"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestLoopbackType"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestPaternType"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestRowStatus"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestEthertype"))
)
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestGroup.setStatus("current")

prvtSaaY1731TestResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 2, 3)
)
prvtSaaY1731TestResultsGroup.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731TestResultDelayNE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultDelayFE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultJitterNE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultJitterFE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultFrameLossNE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultFrameLossFE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultFramesSentNE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultFramesSentFE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultFramesRcvdNE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultFramesRcvdFE"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultPacketsSent"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultNoTimeouts"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultNoErrors"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultCompletionTime"))
)
if mibBuilder.loadTexts:
    prvtSaaY1731TestResultsGroup.setStatus("current")

prvtSaaRFC2544TestResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 2, 4)
)
prvtSaaRFC2544TestResultsGroup.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultFrameSize"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultFrameLoss"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultThroughput"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultNetThroughput"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultStatus"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultDelayMinimum"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultDelayAverage"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultDelayMaximum"))
)
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestResultsGroup.setStatus("current")

prvtSaaProfilesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 2, 5)
)
prvtSaaProfilesGroup.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaProfileDelayNE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileDelayFE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileJitterNE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileJitterFE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileFrameLossNE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileFrameLossFE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileRowStatus"),
        ("PRVT-SAA-MIB", "prvtSaaProfileName"))
)
if mibBuilder.loadTexts:
    prvtSaaProfilesGroup.setStatus("current")

prvtSaaY1731LoopbackTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 2, 7)
)
prvtSaaY1731LoopbackTestGroup.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731LoopbackTestUserPort"),
        ("PRVT-SAA-MIB", "prvtSaaY1731LoopbackTestUplinkPort"),
        ("PRVT-SAA-MIB", "prvtSaaY1731LoopbackTestType"),
        ("PRVT-SAA-MIB", "prvtSaaY1731LoopbackTestCCMAPSCount"),
        ("PRVT-SAA-MIB", "prvtSaaY1731LoopbackTestRowStatus"),
        ("PRVT-SAA-MIB", "prvtSaaY1731LoopbackTestCountAllPriorities"))
)
if mibBuilder.loadTexts:
    prvtSaaY1731LoopbackTestGroup.setStatus("current")


# Notification objects

prvtSaaRFC2544ProbeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0, 1)
)
prvtSaaRFC2544ProbeFailed.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestType"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultStatus"))
)
if mibBuilder.loadTexts:
    prvtSaaRFC2544ProbeFailed.setStatus(
        "current"
    )

prvtSaaRFC2544ProbeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0, 2)
)
prvtSaaRFC2544ProbeSuccess.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestType"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultStatus"))
)
if mibBuilder.loadTexts:
    prvtSaaRFC2544ProbeSuccess.setStatus(
        "current"
    )

prvtSaaRFC2544TestFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0, 3)
)
prvtSaaRFC2544TestFinished.setObjects(
    ("PRVT-SAA-MIB", "prvtSaaRFC2544ThroughputTestExecStatus")
)
if mibBuilder.loadTexts:
    prvtSaaRFC2544TestFinished.setStatus(
        "current"
    )

prvtSaaY1731DelayNEThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0, 4)
)
prvtSaaY1731DelayNEThreshold.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731TestResultDelayNE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileDelayNE"))
)
if mibBuilder.loadTexts:
    prvtSaaY1731DelayNEThreshold.setStatus(
        "current"
    )

prvtSaaY1731DelayFEThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0, 5)
)
prvtSaaY1731DelayFEThreshold.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731TestResultDelayFE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileDelayFE"))
)
if mibBuilder.loadTexts:
    prvtSaaY1731DelayFEThreshold.setStatus(
        "current"
    )

prvtSaaY1731JitterNEThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0, 6)
)
prvtSaaY1731JitterNEThreshold.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731TestResultJitterNE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileJitterNE"))
)
if mibBuilder.loadTexts:
    prvtSaaY1731JitterNEThreshold.setStatus(
        "current"
    )

prvtSaaY1731JitterFEThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0, 7)
)
prvtSaaY1731JitterFEThreshold.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731TestResultJitterFE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileJitterFE"))
)
if mibBuilder.loadTexts:
    prvtSaaY1731JitterFEThreshold.setStatus(
        "current"
    )

prvtSaaY1731FrLossNEThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0, 8)
)
prvtSaaY1731FrLossNEThreshold.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731TestResultFrameLossNE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileFrameLossNE"))
)
if mibBuilder.loadTexts:
    prvtSaaY1731FrLossNEThreshold.setStatus(
        "current"
    )

prvtSaaY1731FrLossFEThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 0, 9)
)
prvtSaaY1731FrLossFEThreshold.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731TestResultFrameLossFE"),
        ("PRVT-SAA-MIB", "prvtSaaProfileFrameLossFE"))
)
if mibBuilder.loadTexts:
    prvtSaaY1731FrLossFEThreshold.setStatus(
        "current"
    )


# Notifications groups

prvtSaaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 2, 6)
)
prvtSaaNotificationsGroup.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaRFC2544ProbeFailed"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544ProbeSuccess"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestFinished"),
        ("PRVT-SAA-MIB", "prvtSaaY1731DelayNEThreshold"),
        ("PRVT-SAA-MIB", "prvtSaaY1731DelayFEThreshold"),
        ("PRVT-SAA-MIB", "prvtSaaY1731JitterNEThreshold"),
        ("PRVT-SAA-MIB", "prvtSaaY1731JitterFEThreshold"),
        ("PRVT-SAA-MIB", "prvtSaaY1731FrLossNEThreshold"),
        ("PRVT-SAA-MIB", "prvtSaaY1731FrLossFEThreshold"))
)
if mibBuilder.loadTexts:
    prvtSaaNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prvtSaaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 130, 2, 1, 1)
)
prvtSaaCompliance.setObjects(
      *(("PRVT-SAA-MIB", "prvtSaaY1731TestGroup"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestGroup"),
        ("PRVT-SAA-MIB", "prvtSaaY1731TestResultsGroup"),
        ("PRVT-SAA-MIB", "prvtSaaRFC2544TestResultsGroup"),
        ("PRVT-SAA-MIB", "prvtSaaProfilesGroup"),
        ("PRVT-SAA-MIB", "prvtSaaNotificationsGroup"),
        ("PRVT-SAA-MIB", "prvtSaaY1731LoopbackTestGroup"))
)
if mibBuilder.loadTexts:
    prvtSaaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SAA-MIB",
    **{"PrvtTwampTestNameType": PrvtTwampTestNameType,
       "PrvtTwampDecimalPercent": PrvtTwampDecimalPercent,
       "prvtSaaMib": prvtSaaMib,
       "prvtSaaNotifications": prvtSaaNotifications,
       "prvtSaaRFC2544ProbeFailed": prvtSaaRFC2544ProbeFailed,
       "prvtSaaRFC2544ProbeSuccess": prvtSaaRFC2544ProbeSuccess,
       "prvtSaaRFC2544TestFinished": prvtSaaRFC2544TestFinished,
       "prvtSaaY1731DelayNEThreshold": prvtSaaY1731DelayNEThreshold,
       "prvtSaaY1731DelayFEThreshold": prvtSaaY1731DelayFEThreshold,
       "prvtSaaY1731JitterNEThreshold": prvtSaaY1731JitterNEThreshold,
       "prvtSaaY1731JitterFEThreshold": prvtSaaY1731JitterFEThreshold,
       "prvtSaaY1731FrLossNEThreshold": prvtSaaY1731FrLossNEThreshold,
       "prvtSaaY1731FrLossFEThreshold": prvtSaaY1731FrLossFEThreshold,
       "prvtSaaObjects": prvtSaaObjects,
       "prvtSaaTest": prvtSaaTest,
       "prvtSaaY1731PmTestTable": prvtSaaY1731PmTestTable,
       "prvtSaaY1731PmTestEntry": prvtSaaY1731PmTestEntry,
       "prvtSaaY1731PmTestOwner": prvtSaaY1731PmTestOwner,
       "prvtSaaY1731PmTestName": prvtSaaY1731PmTestName,
       "prvtSaaY1731PmTestType": prvtSaaY1731PmTestType,
       "prvtSaaY1731PmTestExecStatus": prvtSaaY1731PmTestExecStatus,
       "prvtSaaY1731PmTestEncapType": prvtSaaY1731PmTestEncapType,
       "prvtSaaY1731PmTestEncapValue": prvtSaaY1731PmTestEncapValue,
       "prvtSaaY1731PmTestUserPort": prvtSaaY1731PmTestUserPort,
       "prvtSaaY1731PmTestUplinkPort": prvtSaaY1731PmTestUplinkPort,
       "prvtSaaY1731PmTestTargetMac": prvtSaaY1731PmTestTargetMac,
       "prvtSaaY1731PmTestCfmDomainLevel": prvtSaaY1731PmTestCfmDomainLevel,
       "prvtSaaY1731PmTestRemoteCfmMep": prvtSaaY1731PmTestRemoteCfmMep,
       "prvtSaaY1731PmTestProfile": prvtSaaY1731PmTestProfile,
       "prvtSaaY1731PmTestHistoryDepth": prvtSaaY1731PmTestHistoryDepth,
       "prvtSaaY1731PmTestPeriod": prvtSaaY1731PmTestPeriod,
       "prvtSaaY1731PmTestTimeout": prvtSaaY1731PmTestTimeout,
       "prvtSaaY1731PmTestMonitorInterval": prvtSaaY1731PmTestMonitorInterval,
       "prvtSaaY1731PmTestFrequency": prvtSaaY1731PmTestFrequency,
       "prvtSaaY1731PmTestClocksInSync": prvtSaaY1731PmTestClocksInSync,
       "prvtSaaY1731PmTestDelayMethod": prvtSaaY1731PmTestDelayMethod,
       "prvtSaaY1731PmTestDelayPvalue": prvtSaaY1731PmTestDelayPvalue,
       "prvtSaaY1731PmTestJitterMethod": prvtSaaY1731PmTestJitterMethod,
       "prvtSaaY1731PmTestJitterPvalue": prvtSaaY1731PmTestJitterPvalue,
       "prvtSaaY1731PmTestPriority": prvtSaaY1731PmTestPriority,
       "prvtSaaY1731PmTestRowStatus": prvtSaaY1731PmTestRowStatus,
       "prvtSaaY1731PmTestCCMAPSCount": prvtSaaY1731PmTestCCMAPSCount,
       "prvtSaaY1731PmTestLossMeasurementType": prvtSaaY1731PmTestLossMeasurementType,
       "prvtSaaY1731PmTestSLMTransmit": prvtSaaY1731PmTestSLMTransmit,
       "prvtSaaY1731PmTestTestId": prvtSaaY1731PmTestTestId,
       "prvtSaaY1731PmTestDropEligible": prvtSaaY1731PmTestDropEligible,
       "prvtSaaY1731PmTestDataSize": prvtSaaY1731PmTestDataSize,
       "prvtSaaY1731PmTestCountAllPriorities": prvtSaaY1731PmTestCountAllPriorities,
       "prvtSaaRFC2544ThroughputTestTable": prvtSaaRFC2544ThroughputTestTable,
       "prvtSaaRFC2544ThroughputTestEntry": prvtSaaRFC2544ThroughputTestEntry,
       "prvtSaaRFC2544ThroughputTestOwner": prvtSaaRFC2544ThroughputTestOwner,
       "prvtSaaRFC2544ThroughputTestName": prvtSaaRFC2544ThroughputTestName,
       "prvtSaaRFC2544ThroughputTestType": prvtSaaRFC2544ThroughputTestType,
       "prvtSaaRFC2544ThroughputTestExecStatus": prvtSaaRFC2544ThroughputTestExecStatus,
       "prvtSaaRFC2544ThroughputTestSourceType": prvtSaaRFC2544ThroughputTestSourceType,
       "prvtSaaRFC2544ThroughputTestSource": prvtSaaRFC2544ThroughputTestSource,
       "prvtSaaRFC2544ThroughputTestTargetType": prvtSaaRFC2544ThroughputTestTargetType,
       "prvtSaaRFC2544ThroughputTestTarget": prvtSaaRFC2544ThroughputTestTarget,
       "prvtSaaRFC2544ThroughputTestTimeout": prvtSaaRFC2544ThroughputTestTimeout,
       "prvtSaaRFC2544ThroughputTestCIR": prvtSaaRFC2544ThroughputTestCIR,
       "prvtSaaRFC2544ThroughputTestCBS": prvtSaaRFC2544ThroughputTestCBS,
       "prvtSaaRFC2544ThroughputTestBurstPercentage": prvtSaaRFC2544ThroughputTestBurstPercentage,
       "prvtSaaRFC2544ThroughputTestDuration": prvtSaaRFC2544ThroughputTestDuration,
       "prvtSaaRFC2544ThroughputTestMaxFrameloss": prvtSaaRFC2544ThroughputTestMaxFrameloss,
       "prvtSaaRFC2544ThroughputTestCVLAN0": prvtSaaRFC2544ThroughputTestCVLAN0,
       "prvtSaaRFC2544ThroughputTestCVLAN0Priority": prvtSaaRFC2544ThroughputTestCVLAN0Priority,
       "prvtSaaRFC2544ThroughputTestCVLAN0DropEligible": prvtSaaRFC2544ThroughputTestCVLAN0DropEligible,
       "prvtSaaRFC2544ThroughputTestSVLAN": prvtSaaRFC2544ThroughputTestSVLAN,
       "prvtSaaRFC2544ThroughputTestSVLANPriority": prvtSaaRFC2544ThroughputTestSVLANPriority,
       "prvtSaaRFC2544ThroughputTestSVLANDropEligible": prvtSaaRFC2544ThroughputTestSVLANDropEligible,
       "prvtSaaRFC2544ThroughputTestPDUSize": prvtSaaRFC2544ThroughputTestPDUSize,
       "prvtSaaRFC2544ThroughputTestACKTimeout": prvtSaaRFC2544ThroughputTestACKTimeout,
       "prvtSaaRFC2544ThroughputTestLoopbackType": prvtSaaRFC2544ThroughputTestLoopbackType,
       "prvtSaaRFC2544ThroughputTestPaternType": prvtSaaRFC2544ThroughputTestPaternType,
       "prvtSaaRFC2544ThroughputTestRowStatus": prvtSaaRFC2544ThroughputTestRowStatus,
       "prvtSaaRFC2544ThroughputTestEthertype": prvtSaaRFC2544ThroughputTestEthertype,
       "prvtSaaY1731LoopbackTestTable": prvtSaaY1731LoopbackTestTable,
       "prvtSaaY1731LoopbackTestEntry": prvtSaaY1731LoopbackTestEntry,
       "prvtSaaY1731LoopbackTestEncapType": prvtSaaY1731LoopbackTestEncapType,
       "prvtSaaY1731LoopbackTestEncapValue": prvtSaaY1731LoopbackTestEncapValue,
       "prvtSaaY1731LoopbackTestUserPort": prvtSaaY1731LoopbackTestUserPort,
       "prvtSaaY1731LoopbackTestUplinkPort": prvtSaaY1731LoopbackTestUplinkPort,
       "prvtSaaY1731LoopbackTestType": prvtSaaY1731LoopbackTestType,
       "prvtSaaY1731LoopbackTestRowStatus": prvtSaaY1731LoopbackTestRowStatus,
       "prvtSaaY1731LoopbackTestCCMAPSCount": prvtSaaY1731LoopbackTestCCMAPSCount,
       "prvtSaaY1731LoopbackTestCountAllPriorities": prvtSaaY1731LoopbackTestCountAllPriorities,
       "prvtSaaTestResult": prvtSaaTestResult,
       "prvtSaaY1731TestResultTable": prvtSaaY1731TestResultTable,
       "prvtSaaY1731TestResultEntry": prvtSaaY1731TestResultEntry,
       "prvtSaaY1731TestResultIndex": prvtSaaY1731TestResultIndex,
       "prvtSaaY1731TestResultDelayNE": prvtSaaY1731TestResultDelayNE,
       "prvtSaaY1731TestResultDelayFE": prvtSaaY1731TestResultDelayFE,
       "prvtSaaY1731TestResultJitterNE": prvtSaaY1731TestResultJitterNE,
       "prvtSaaY1731TestResultJitterFE": prvtSaaY1731TestResultJitterFE,
       "prvtSaaY1731TestResultFrameLossNE": prvtSaaY1731TestResultFrameLossNE,
       "prvtSaaY1731TestResultFrameLossFE": prvtSaaY1731TestResultFrameLossFE,
       "prvtSaaY1731TestResultFramesSentNE": prvtSaaY1731TestResultFramesSentNE,
       "prvtSaaY1731TestResultFramesSentFE": prvtSaaY1731TestResultFramesSentFE,
       "prvtSaaY1731TestResultFramesRcvdNE": prvtSaaY1731TestResultFramesRcvdNE,
       "prvtSaaY1731TestResultFramesRcvdFE": prvtSaaY1731TestResultFramesRcvdFE,
       "prvtSaaY1731TestResultPacketsSent": prvtSaaY1731TestResultPacketsSent,
       "prvtSaaY1731TestResultNoTimeouts": prvtSaaY1731TestResultNoTimeouts,
       "prvtSaaY1731TestResultNoErrors": prvtSaaY1731TestResultNoErrors,
       "prvtSaaY1731TestResultCompletionTime": prvtSaaY1731TestResultCompletionTime,
       "prvtSaaRFC2544TestResultTable": prvtSaaRFC2544TestResultTable,
       "prvtSaaRFC2544TestResultEntry": prvtSaaRFC2544TestResultEntry,
       "prvtSaaRFC2544TestResultIndex": prvtSaaRFC2544TestResultIndex,
       "prvtSaaRFC2544TestResultFrameSize": prvtSaaRFC2544TestResultFrameSize,
       "prvtSaaRFC2544TestResultFrameLoss": prvtSaaRFC2544TestResultFrameLoss,
       "prvtSaaRFC2544TestResultThroughput": prvtSaaRFC2544TestResultThroughput,
       "prvtSaaRFC2544TestResultNetThroughput": prvtSaaRFC2544TestResultNetThroughput,
       "prvtSaaRFC2544TestResultStatus": prvtSaaRFC2544TestResultStatus,
       "prvtSaaRFC2544TestResultDelayMinimum": prvtSaaRFC2544TestResultDelayMinimum,
       "prvtSaaRFC2544TestResultDelayAverage": prvtSaaRFC2544TestResultDelayAverage,
       "prvtSaaRFC2544TestResultDelayMaximum": prvtSaaRFC2544TestResultDelayMaximum,
       "prvtSaaProfiles": prvtSaaProfiles,
       "prvtSaaProfileTable": prvtSaaProfileTable,
       "prvtSaaProfileEntry": prvtSaaProfileEntry,
       "prvtSaaProfileIndex": prvtSaaProfileIndex,
       "prvtSaaProfileDelayNE": prvtSaaProfileDelayNE,
       "prvtSaaProfileDelayFE": prvtSaaProfileDelayFE,
       "prvtSaaProfileJitterNE": prvtSaaProfileJitterNE,
       "prvtSaaProfileJitterFE": prvtSaaProfileJitterFE,
       "prvtSaaProfileFrameLossNE": prvtSaaProfileFrameLossNE,
       "prvtSaaProfileFrameLossFE": prvtSaaProfileFrameLossFE,
       "prvtSaaProfileRowStatus": prvtSaaProfileRowStatus,
       "prvtSaaProfileName": prvtSaaProfileName,
       "prvtTwampObjects": prvtTwampObjects,
       "prvtTwampTest": prvtTwampTest,
       "prvtTwampTestTable": prvtTwampTestTable,
       "prvtTwampTestEntry": prvtTwampTestEntry,
       "prvtTwampTestName": prvtTwampTestName,
       "prvtTwampTestRowStatus": prvtTwampTestRowStatus,
       "prvtTwampTestServer": prvtTwampTestServer,
       "prvtTwampTestSessionsCount": prvtTwampTestSessionsCount,
       "prvtTwampTestPackets": prvtTwampTestPackets,
       "prvtTwampTestTimeout": prvtTwampTestTimeout,
       "prvtTwampTestDelay": prvtTwampTestDelay,
       "prvtTwampTestExecuteNow": prvtTwampTestExecuteNow,
       "prvtTwampServer": prvtTwampServer,
       "prvtTwampServerInnactivity": prvtTwampServerInnactivity,
       "prvtTwampServerSessionInnactivity": prvtTwampServerSessionInnactivity,
       "prvtTwampServerMaxSessions": prvtTwampServerMaxSessions,
       "prvtTwampServerMaxParallelSessions": prvtTwampServerMaxParallelSessions,
       "prvtTwampServerShutdown": prvtTwampServerShutdown,
       "prvtTwampClientTable": prvtTwampClientTable,
       "prvtTwampClientEntry": prvtTwampClientEntry,
       "prvtTwampClientIp": prvtTwampClientIp,
       "prvtTwampClientRowStatus": prvtTwampClientRowStatus,
       "prvtTwampServerControlSessions": prvtTwampServerControlSessions,
       "prvtTwampServerTestSessions": prvtTwampServerTestSessions,
       "prvtTwampTestResult": prvtTwampTestResult,
       "prvtTwampTestResultTable": prvtTwampTestResultTable,
       "prvtTwampTestResultEntry": prvtTwampTestResultEntry,
       "prvtTwampTestId": prvtTwampTestId,
       "prvtTwampTestResultName": prvtTwampTestResultName,
       "prvtTwampTestStartTime": prvtTwampTestStartTime,
       "prvtTwampTestServerAddress": prvtTwampTestServerAddress,
       "prvtTwampTestSessions": prvtTwampTestSessions,
       "prvtTwampTestState": prvtTwampTestState,
       "prvtTwampTestRtt": prvtTwampTestRtt,
       "prvtTwampTestMinRtt": prvtTwampTestMinRtt,
       "prvtTwampTestMaxRtt": prvtTwampTestMaxRtt,
       "prvtTwampTestPcktSent": prvtTwampTestPcktSent,
       "prvtTwampTestPcktLost": prvtTwampTestPcktLost,
       "prvtTwampTestPcktDrop": prvtTwampTestPcktDrop,
       "prvtTwampTestVariation": prvtTwampTestVariation,
       "prvtTwampTestVariationLow": prvtTwampTestVariationLow,
       "prvtTwampTestVariationMiddle": prvtTwampTestVariationMiddle,
       "prvtTwampTestVariationHigh": prvtTwampTestVariationHigh,
       "prvtSaaConformance": prvtSaaConformance,
       "prvtSaaCompliances": prvtSaaCompliances,
       "prvtSaaCompliance": prvtSaaCompliance,
       "prvtSaaGroups": prvtSaaGroups,
       "prvtSaaY1731TestGroup": prvtSaaY1731TestGroup,
       "prvtSaaRFC2544TestGroup": prvtSaaRFC2544TestGroup,
       "prvtSaaY1731TestResultsGroup": prvtSaaY1731TestResultsGroup,
       "prvtSaaRFC2544TestResultsGroup": prvtSaaRFC2544TestResultsGroup,
       "prvtSaaProfilesGroup": prvtSaaProfilesGroup,
       "prvtSaaNotificationsGroup": prvtSaaNotificationsGroup,
       "prvtSaaY1731LoopbackTestGroup": prvtSaaY1731LoopbackTestGroup}
)
