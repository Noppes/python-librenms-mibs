# SNMP MIB module (GIGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sagemcom\GIGE-MIB

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

(adr2500c,) = mibBuilder.importSymbols(
    "ADR2500C-MIB",
    "adr2500c")

(SagemBoolean,
 Severity) = mibBuilder.importSymbols(
    "EQUIPMENT-MIB",
    "SagemBoolean",
    "Severity")

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


# MODULE-IDENTITY

gige = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10)
)


# Types definitions



class BandwidthSize(Integer32):
    """Custom type BandwidthSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              16,
              64)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("stm1", 1),
          ("stm4", 4),
          ("stm16", 16),
          ("stm64", 64))
    )





class LoopbackGE(Integer32):
    """Custom type LoopbackGE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("remote", 10))
    )





class QosType(Integer32):
    """Custom type QosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pauseMode", 1),
          ("userPriority", 2),
          ("vlanId", 3),
          ("balanced", 4),
          ("ipv4TOS", 10),
          ("ipv6TClass", 11),
          ("dscp", 13))
    )





class CongestionControl(Integer32):
    """Custom type CongestionControl based on Integer32"""
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
          ("red", 1),
          ("wred", 2))
    )





class SchedulingSystem(Integer32):
    """Custom type SchedulingSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("spq", 1),
          ("wfq", 4),
          ("cbwfq", 5),
          ("wrr", 10))
    )





class CosId(Integer32):
    """Custom type CosId based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 0),
          ("cos1", 1),
          ("cos2", 2),
          ("cos3", 3),
          ("cos4", 4),
          ("cos5", 5),
          ("cos6", 6),
          ("cos7", 7))
    )





class GfpFailure(Integer32):
    """Custom type GfpFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("oofd", 1),
          ("lofd", 2),
          ("fdsc", 3))
    )





class GfpState(Integer32):
    """Custom type GfpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class PauseFailure(Integer32):
    """Custom type PauseFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pauseModeRejected", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _GigeNumber_Type(Integer32):
    """Custom type gigeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GigeNumber_Type.__name__ = "Integer32"
_GigeNumber_Object = MibScalar
gigeNumber = _GigeNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 10),
    _GigeNumber_Type()
)
gigeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeNumber.setStatus("current")
_GigeTable_Object = MibTable
gigeTable = _GigeTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 11)
)
if mibBuilder.loadTexts:
    gigeTable.setStatus("current")
_GigeEntry_Object = MibTableRow
gigeEntry = _GigeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 11, 1)
)
gigeEntry.setIndexNames(
    (0, "GIGE-MIB", "gigeIndex"),
)
if mibBuilder.loadTexts:
    gigeEntry.setStatus("current")


class _GigeIndex_Type(Integer32):
    """Custom type gigeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GigeIndex_Type.__name__ = "Integer32"
_GigeIndex_Object = MibTableColumn
gigeIndex = _GigeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 11, 1, 1),
    _GigeIndex_Type()
)
gigeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigeIndex.setStatus("current")
_GigeSdhBandwidth_Type = BandwidthSize
_GigeSdhBandwidth_Object = MibTableColumn
gigeSdhBandwidth = _GigeSdhBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 11, 1, 2),
    _GigeSdhBandwidth_Type()
)
gigeSdhBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigeSdhBandwidth.setStatus("current")
_GigeAutoTest_Type = SagemBoolean
_GigeAutoTest_Object = MibTableColumn
gigeAutoTest = _GigeAutoTest_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 11, 1, 3),
    _GigeAutoTest_Type()
)
gigeAutoTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigeAutoTest.setStatus("current")
_GigeWarmStart_Type = SagemBoolean
_GigeWarmStart_Object = MibTableColumn
gigeWarmStart = _GigeWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 11, 1, 4),
    _GigeWarmStart_Type()
)
gigeWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigeWarmStart.setStatus("current")


class _MaintenanceNumber_Type(Integer32):
    """Custom type maintenanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MaintenanceNumber_Type.__name__ = "Integer32"
_MaintenanceNumber_Object = MibScalar
maintenanceNumber = _MaintenanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 20),
    _MaintenanceNumber_Type()
)
maintenanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceNumber.setStatus("current")
_MaintenanceTable_Object = MibTable
maintenanceTable = _MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21)
)
if mibBuilder.loadTexts:
    maintenanceTable.setStatus("current")
_MaintenanceEntry_Object = MibTableRow
maintenanceEntry = _MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1)
)
maintenanceEntry.setIndexNames(
    (0, "GIGE-MIB", "maintenanceIndex"),
)
if mibBuilder.loadTexts:
    maintenanceEntry.setStatus("current")


class _MaintenanceIndex_Type(Integer32):
    """Custom type maintenanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MaintenanceIndex_Type.__name__ = "Integer32"
_MaintenanceIndex_Object = MibTableColumn
maintenanceIndex = _MaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1, 1),
    _MaintenanceIndex_Type()
)
maintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenanceIndex.setStatus("current")
_MaintenanceAutoTest_Type = SagemBoolean
_MaintenanceAutoTest_Object = MibTableColumn
maintenanceAutoTest = _MaintenanceAutoTest_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1, 2),
    _MaintenanceAutoTest_Type()
)
maintenanceAutoTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceAutoTest.setStatus("current")
_MaintenanceLoopback_Type = LoopbackGE
_MaintenanceLoopback_Object = MibTableColumn
maintenanceLoopback = _MaintenanceLoopback_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1, 3),
    _MaintenanceLoopback_Type()
)
maintenanceLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceLoopback.setStatus("current")
_MaintenancePRBSSent_Type = DisplayString
_MaintenancePRBSSent_Object = MibTableColumn
maintenancePRBSSent = _MaintenancePRBSSent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1, 4),
    _MaintenancePRBSSent_Type()
)
maintenancePRBSSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenancePRBSSent.setStatus("current")
_MaintenancePRBSReceived_Type = DisplayString
_MaintenancePRBSReceived_Object = MibTableColumn
maintenancePRBSReceived = _MaintenancePRBSReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1, 5),
    _MaintenancePRBSReceived_Type()
)
maintenancePRBSReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenancePRBSReceived.setStatus("current")
_MaintenanceResetAllCounters_Type = SagemBoolean
_MaintenanceResetAllCounters_Object = MibTableColumn
maintenanceResetAllCounters = _MaintenanceResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1, 6),
    _MaintenanceResetAllCounters_Type()
)
maintenanceResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceResetAllCounters.setStatus("current")
_MaintenanceResetLanCounters_Type = SagemBoolean
_MaintenanceResetLanCounters_Object = MibTableColumn
maintenanceResetLanCounters = _MaintenanceResetLanCounters_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1, 7),
    _MaintenanceResetLanCounters_Type()
)
maintenanceResetLanCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceResetLanCounters.setStatus("current")
_MaintenanceResetGfpCounters_Type = SagemBoolean
_MaintenanceResetGfpCounters_Object = MibTableColumn
maintenanceResetGfpCounters = _MaintenanceResetGfpCounters_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1, 8),
    _MaintenanceResetGfpCounters_Type()
)
maintenanceResetGfpCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceResetGfpCounters.setStatus("current")
_MaintenanceResetQosCounters_Type = SagemBoolean
_MaintenanceResetQosCounters_Object = MibTableColumn
maintenanceResetQosCounters = _MaintenanceResetQosCounters_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 21, 1, 9),
    _MaintenanceResetQosCounters_Type()
)
maintenanceResetQosCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintenanceResetQosCounters.setStatus("current")


class _QosNumber_Type(Integer32):
    """Custom type qosNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QosNumber_Type.__name__ = "Integer32"
_QosNumber_Object = MibScalar
qosNumber = _QosNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 30),
    _QosNumber_Type()
)
qosNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosNumber.setStatus("current")
_QosTable_Object = MibTable
qosTable = _QosTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31)
)
if mibBuilder.loadTexts:
    qosTable.setStatus("current")
_QosEntry_Object = MibTableRow
qosEntry = _QosEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31, 1)
)
qosEntry.setIndexNames(
    (0, "GIGE-MIB", "qosIndex"),
)
if mibBuilder.loadTexts:
    qosEntry.setStatus("current")


class _QosIndex_Type(Integer32):
    """Custom type qosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QosIndex_Type.__name__ = "Integer32"
_QosIndex_Object = MibTableColumn
qosIndex = _QosIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31, 1, 1),
    _QosIndex_Type()
)
qosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIndex.setStatus("current")


class _QosClassNumber_Type(Integer32):
    """Custom type qosClassNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QosClassNumber_Type.__name__ = "Integer32"
_QosClassNumber_Object = MibTableColumn
qosClassNumber = _QosClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31, 1, 2),
    _QosClassNumber_Type()
)
qosClassNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosClassNumber.setStatus("current")
_QosType_Type = QosType
_QosType_Object = MibTableColumn
qosType = _QosType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31, 1, 3),
    _QosType_Type()
)
qosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosType.setStatus("current")
_QosCongestionControl_Type = CongestionControl
_QosCongestionControl_Object = MibTableColumn
qosCongestionControl = _QosCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31, 1, 4),
    _QosCongestionControl_Type()
)
qosCongestionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCongestionControl.setStatus("current")
_QosSchedulingSystem_Type = SchedulingSystem
_QosSchedulingSystem_Object = MibTableColumn
qosSchedulingSystem = _QosSchedulingSystem_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31, 1, 5),
    _QosSchedulingSystem_Type()
)
qosSchedulingSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingSystem.setStatus("current")
_QosBwREnable_Type = SagemBoolean
_QosBwREnable_Object = MibTableColumn
qosBwREnable = _QosBwREnable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31, 1, 6),
    _QosBwREnable_Type()
)
qosBwREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosBwREnable.setStatus("current")
_QosHCInCCDiscardsGe_Type = Counter64
_QosHCInCCDiscardsGe_Object = MibTableColumn
qosHCInCCDiscardsGe = _QosHCInCCDiscardsGe_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31, 1, 7),
    _QosHCInCCDiscardsGe_Type()
)
qosHCInCCDiscardsGe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosHCInCCDiscardsGe.setStatus("current")
_QosHCInCCDiscardsWan_Type = Counter64
_QosHCInCCDiscardsWan_Object = MibTableColumn
qosHCInCCDiscardsWan = _QosHCInCCDiscardsWan_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 31, 1, 8),
    _QosHCInCCDiscardsWan_Type()
)
qosHCInCCDiscardsWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosHCInCCDiscardsWan.setStatus("current")


class _CosNumber_Type(Integer32):
    """Custom type cosNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CosNumber_Type.__name__ = "Integer32"
_CosNumber_Object = MibScalar
cosNumber = _CosNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 40),
    _CosNumber_Type()
)
cosNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosNumber.setStatus("current")
_CosTable_Object = MibTable
cosTable = _CosTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41)
)
if mibBuilder.loadTexts:
    cosTable.setStatus("current")
_CosEntry_Object = MibTableRow
cosEntry = _CosEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1)
)
cosEntry.setIndexNames(
    (0, "GIGE-MIB", "cosIndex"),
)
if mibBuilder.loadTexts:
    cosEntry.setStatus("current")


class _CosIndex_Type(Integer32):
    """Custom type cosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CosIndex_Type.__name__ = "Integer32"
_CosIndex_Object = MibTableColumn
cosIndex = _CosIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 1),
    _CosIndex_Type()
)
cosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosIndex.setStatus("current")


class _CosQosId_Type(Integer32):
    """Custom type cosQosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CosQosId_Type.__name__ = "Integer32"
_CosQosId_Object = MibTableColumn
cosQosId = _CosQosId_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 2),
    _CosQosId_Type()
)
cosQosId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosQosId.setStatus("current")
_CosId_Type = CosId
_CosId_Object = MibTableColumn
cosId = _CosId_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 3),
    _CosId_Type()
)
cosId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosId.setStatus("current")
_CosDefinition_Type = DisplayString
_CosDefinition_Object = MibTableColumn
cosDefinition = _CosDefinition_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 4),
    _CosDefinition_Type()
)
cosDefinition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosDefinition.setStatus("current")


class _CosBwRRatioMin_Type(Integer32):
    """Custom type cosBwRRatioMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CosBwRRatioMin_Type.__name__ = "Integer32"
_CosBwRRatioMin_Object = MibTableColumn
cosBwRRatioMin = _CosBwRRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 5),
    _CosBwRRatioMin_Type()
)
cosBwRRatioMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cosBwRRatioMin.setStatus("current")


class _CosBwRRatioMax_Type(Integer32):
    """Custom type cosBwRRatioMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CosBwRRatioMax_Type.__name__ = "Integer32"
_CosBwRRatioMax_Object = MibTableColumn
cosBwRRatioMax = _CosBwRRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 6),
    _CosBwRRatioMax_Type()
)
cosBwRRatioMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cosBwRRatioMax.setStatus("current")
_CosHCInOctets_Type = Counter64
_CosHCInOctets_Object = MibTableColumn
cosHCInOctets = _CosHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 7),
    _CosHCInOctets_Type()
)
cosHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosHCInOctets.setStatus("current")
_CosHCOutOctets_Type = Counter64
_CosHCOutOctets_Object = MibTableColumn
cosHCOutOctets = _CosHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 8),
    _CosHCOutOctets_Type()
)
cosHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosHCOutOctets.setStatus("current")
_CosHCInPkts_Type = Counter64
_CosHCInPkts_Object = MibTableColumn
cosHCInPkts = _CosHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 9),
    _CosHCInPkts_Type()
)
cosHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosHCInPkts.setStatus("current")
_CosHCOutPkts_Type = Counter64
_CosHCOutPkts_Object = MibTableColumn
cosHCOutPkts = _CosHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 10),
    _CosHCOutPkts_Type()
)
cosHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosHCOutPkts.setStatus("current")
_CosHCInCCDiscards_Type = Counter64
_CosHCInCCDiscards_Object = MibTableColumn
cosHCInCCDiscards = _CosHCInCCDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 41, 1, 11),
    _CosHCInCCDiscards_Type()
)
cosHCInCCDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosHCInCCDiscards.setStatus("current")


class _GfpNumber_Type(Integer32):
    """Custom type gfpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GfpNumber_Type.__name__ = "Integer32"
_GfpNumber_Object = MibScalar
gfpNumber = _GfpNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 50),
    _GfpNumber_Type()
)
gfpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpNumber.setStatus("current")
_GfpTable_Object = MibTable
gfpTable = _GfpTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51)
)
if mibBuilder.loadTexts:
    gfpTable.setStatus("current")
_GfpEntry_Object = MibTableRow
gfpEntry = _GfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1)
)
gfpEntry.setIndexNames(
    (0, "GIGE-MIB", "gfpIndex"),
)
if mibBuilder.loadTexts:
    gfpEntry.setStatus("current")


class _GfpIndex_Type(Integer32):
    """Custom type gfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GfpIndex_Type.__name__ = "Integer32"
_GfpIndex_Object = MibTableColumn
gfpIndex = _GfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 1),
    _GfpIndex_Type()
)
gfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpIndex.setStatus("current")
_GfpHCInPkts_Type = Counter64
_GfpHCInPkts_Object = MibTableColumn
gfpHCInPkts = _GfpHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 2),
    _GfpHCInPkts_Type()
)
gfpHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCInPkts.setStatus("current")
_GfpHCInIdlePkts_Type = Counter64
_GfpHCInIdlePkts_Object = MibTableColumn
gfpHCInIdlePkts = _GfpHCInIdlePkts_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 3),
    _GfpHCInIdlePkts_Type()
)
gfpHCInIdlePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCInIdlePkts.setStatus("current")
_GfpHCInCorruptedPkts_Type = Counter64
_GfpHCInCorruptedPkts_Object = MibTableColumn
gfpHCInCorruptedPkts = _GfpHCInCorruptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 4),
    _GfpHCInCorruptedPkts_Type()
)
gfpHCInCorruptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCInCorruptedPkts.setStatus("current")
_GfpHCInErrors_Type = Counter64
_GfpHCInErrors_Object = MibTableColumn
gfpHCInErrors = _GfpHCInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 5),
    _GfpHCInErrors_Type()
)
gfpHCInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCInErrors.setStatus("current")
_GfpHCInCorrectedPkts_Type = Counter64
_GfpHCInCorrectedPkts_Object = MibTableColumn
gfpHCInCorrectedPkts = _GfpHCInCorrectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 6),
    _GfpHCInCorrectedPkts_Type()
)
gfpHCInCorrectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCInCorrectedPkts.setStatus("current")
_GfpHCFCSErrors_Type = Counter64
_GfpHCFCSErrors_Object = MibTableColumn
gfpHCFCSErrors = _GfpHCFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 7),
    _GfpHCFCSErrors_Type()
)
gfpHCFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCFCSErrors.setStatus("current")
_GfpHCInOctets_Type = Counter64
_GfpHCInOctets_Object = MibTableColumn
gfpHCInOctets = _GfpHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 8),
    _GfpHCInOctets_Type()
)
gfpHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCInOctets.setStatus("current")
_GfpHCOutPkts_Type = Counter64
_GfpHCOutPkts_Object = MibTableColumn
gfpHCOutPkts = _GfpHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 9),
    _GfpHCOutPkts_Type()
)
gfpHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCOutPkts.setStatus("current")
_GfpHCOutIdlePkts_Type = Counter64
_GfpHCOutIdlePkts_Object = MibTableColumn
gfpHCOutIdlePkts = _GfpHCOutIdlePkts_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 10),
    _GfpHCOutIdlePkts_Type()
)
gfpHCOutIdlePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCOutIdlePkts.setStatus("current")
_GfpHCOutOctets_Type = Counter64
_GfpHCOutOctets_Object = MibTableColumn
gfpHCOutOctets = _GfpHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 11),
    _GfpHCOutOctets_Type()
)
gfpHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpHCOutOctets.setStatus("current")


class _GfpIdleRate_Type(Integer32):
    """Custom type gfpIdleRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GfpIdleRate_Type.__name__ = "Integer32"
_GfpIdleRate_Object = MibTableColumn
gfpIdleRate = _GfpIdleRate_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 12),
    _GfpIdleRate_Type()
)
gfpIdleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpIdleRate.setStatus("current")


class _GfpSendingRate_Type(Integer32):
    """Custom type gfpSendingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GfpSendingRate_Type.__name__ = "Integer32"
_GfpSendingRate_Object = MibTableColumn
gfpSendingRate = _GfpSendingRate_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 13),
    _GfpSendingRate_Type()
)
gfpSendingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpSendingRate.setStatus("current")
_GfpState_Type = GfpState
_GfpState_Object = MibTableColumn
gfpState = _GfpState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 14),
    _GfpState_Type()
)
gfpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpState.setStatus("current")


class _GfpAdminStatus_Type(Integer32):
    """Custom type gfpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_GfpAdminStatus_Type.__name__ = "Integer32"
_GfpAdminStatus_Object = MibTableColumn
gfpAdminStatus = _GfpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 15),
    _GfpAdminStatus_Type()
)
gfpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpAdminStatus.setStatus("current")


class _GfpOperStatus_Type(Integer32):
    """Custom type gfpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_GfpOperStatus_Type.__name__ = "Integer32"
_GfpOperStatus_Object = MibTableColumn
gfpOperStatus = _GfpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 16),
    _GfpOperStatus_Type()
)
gfpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpOperStatus.setStatus("current")
_GfpMonitor_Type = SagemBoolean
_GfpMonitor_Object = MibTableColumn
gfpMonitor = _GfpMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 17),
    _GfpMonitor_Type()
)
gfpMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpMonitor.setStatus("current")
_GfpFailure_Type = GfpFailure
_GfpFailure_Object = MibTableColumn
gfpFailure = _GfpFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 18),
    _GfpFailure_Type()
)
gfpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpFailure.setStatus("current")
_GfpSeverity_Type = Severity
_GfpSeverity_Object = MibTableColumn
gfpSeverity = _GfpSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 19),
    _GfpSeverity_Type()
)
gfpSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpSeverity.setStatus("current")
_GfpOOFD_Type = Severity
_GfpOOFD_Object = MibTableColumn
gfpOOFD = _GfpOOFD_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 20),
    _GfpOOFD_Type()
)
gfpOOFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpOOFD.setStatus("current")
_GfpLOFD_Type = Severity
_GfpLOFD_Object = MibTableColumn
gfpLOFD = _GfpLOFD_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 21),
    _GfpLOFD_Type()
)
gfpLOFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpLOFD.setStatus("current")
_GfpFDSC_Type = Severity
_GfpFDSC_Object = MibTableColumn
gfpFDSC = _GfpFDSC_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 51, 1, 22),
    _GfpFDSC_Type()
)
gfpFDSC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpFDSC.setStatus("current")


class _PauseNumber_Type(Integer32):
    """Custom type pauseNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PauseNumber_Type.__name__ = "Integer32"
_PauseNumber_Object = MibScalar
pauseNumber = _PauseNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 60),
    _PauseNumber_Type()
)
pauseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pauseNumber.setStatus("current")
_PauseTable_Object = MibTable
pauseTable = _PauseTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61)
)
if mibBuilder.loadTexts:
    pauseTable.setStatus("current")
_PauseEntry_Object = MibTableRow
pauseEntry = _PauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1)
)
pauseEntry.setIndexNames(
    (0, "GIGE-MIB", "pauseIndex"),
)
if mibBuilder.loadTexts:
    pauseEntry.setStatus("current")


class _PauseIndex_Type(Integer32):
    """Custom type pauseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PauseIndex_Type.__name__ = "Integer32"
_PauseIndex_Object = MibTableColumn
pauseIndex = _PauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 1),
    _PauseIndex_Type()
)
pauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pauseIndex.setStatus("current")


class _PauseTime_Type(Integer32):
    """Custom type pauseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PauseTime_Type.__name__ = "Integer32"
_PauseTime_Object = MibTableColumn
pauseTime = _PauseTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 2),
    _PauseTime_Type()
)
pauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pauseTime.setStatus("current")


class _PauseBetweenTime_Type(Integer32):
    """Custom type pauseBetweenTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PauseBetweenTime_Type.__name__ = "Integer32"
_PauseBetweenTime_Object = MibTableColumn
pauseBetweenTime = _PauseBetweenTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 3),
    _PauseBetweenTime_Type()
)
pauseBetweenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pauseBetweenTime.setStatus("current")
_PauseMacSA_Type = PhysAddress
_PauseMacSA_Object = MibTableColumn
pauseMacSA = _PauseMacSA_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 4),
    _PauseMacSA_Type()
)
pauseMacSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pauseMacSA.setStatus("current")
_PauseMacDA_Type = PhysAddress
_PauseMacDA_Object = MibTableColumn
pauseMacDA = _PauseMacDA_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 5),
    _PauseMacDA_Type()
)
pauseMacDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pauseMacDA.setStatus("current")


class _PauseCHT_Type(Integer32):
    """Custom type pauseCHT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PauseCHT_Type.__name__ = "Integer32"
_PauseCHT_Object = MibTableColumn
pauseCHT = _PauseCHT_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 6),
    _PauseCHT_Type()
)
pauseCHT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pauseCHT.setStatus("current")


class _PauseCLT_Type(Integer32):
    """Custom type pauseCLT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PauseCLT_Type.__name__ = "Integer32"
_PauseCLT_Object = MibTableColumn
pauseCLT = _PauseCLT_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 7),
    _PauseCLT_Type()
)
pauseCLT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pauseCLT.setStatus("current")
_PauseMonitor_Type = SagemBoolean
_PauseMonitor_Object = MibTableColumn
pauseMonitor = _PauseMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 10),
    _PauseMonitor_Type()
)
pauseMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pauseMonitor.setStatus("current")
_PauseFailure_Type = PauseFailure
_PauseFailure_Object = MibTableColumn
pauseFailure = _PauseFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 11),
    _PauseFailure_Type()
)
pauseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pauseFailure.setStatus("current")
_PauseSeverity_Type = Severity
_PauseSeverity_Object = MibTableColumn
pauseSeverity = _PauseSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 12),
    _PauseSeverity_Type()
)
pauseSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pauseSeverity.setStatus("current")
_PauseModeRejected_Type = Severity
_PauseModeRejected_Object = MibTableColumn
pauseModeRejected = _PauseModeRejected_Object(
    (1, 3, 6, 1, 4, 1, 1038, 17, 10, 61, 1, 13),
    _PauseModeRejected_Type()
)
pauseModeRejected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pauseModeRejected.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GIGE-MIB",
    **{"BandwidthSize": BandwidthSize,
       "LoopbackGE": LoopbackGE,
       "QosType": QosType,
       "CongestionControl": CongestionControl,
       "SchedulingSystem": SchedulingSystem,
       "CosId": CosId,
       "GfpFailure": GfpFailure,
       "GfpState": GfpState,
       "PauseFailure": PauseFailure,
       "gige": gige,
       "gigeNumber": gigeNumber,
       "gigeTable": gigeTable,
       "gigeEntry": gigeEntry,
       "gigeIndex": gigeIndex,
       "gigeSdhBandwidth": gigeSdhBandwidth,
       "gigeAutoTest": gigeAutoTest,
       "gigeWarmStart": gigeWarmStart,
       "maintenanceNumber": maintenanceNumber,
       "maintenanceTable": maintenanceTable,
       "maintenanceEntry": maintenanceEntry,
       "maintenanceIndex": maintenanceIndex,
       "maintenanceAutoTest": maintenanceAutoTest,
       "maintenanceLoopback": maintenanceLoopback,
       "maintenancePRBSSent": maintenancePRBSSent,
       "maintenancePRBSReceived": maintenancePRBSReceived,
       "maintenanceResetAllCounters": maintenanceResetAllCounters,
       "maintenanceResetLanCounters": maintenanceResetLanCounters,
       "maintenanceResetGfpCounters": maintenanceResetGfpCounters,
       "maintenanceResetQosCounters": maintenanceResetQosCounters,
       "qosNumber": qosNumber,
       "qosTable": qosTable,
       "qosEntry": qosEntry,
       "qosIndex": qosIndex,
       "qosClassNumber": qosClassNumber,
       "qosType": qosType,
       "qosCongestionControl": qosCongestionControl,
       "qosSchedulingSystem": qosSchedulingSystem,
       "qosBwREnable": qosBwREnable,
       "qosHCInCCDiscardsGe": qosHCInCCDiscardsGe,
       "qosHCInCCDiscardsWan": qosHCInCCDiscardsWan,
       "cosNumber": cosNumber,
       "cosTable": cosTable,
       "cosEntry": cosEntry,
       "cosIndex": cosIndex,
       "cosQosId": cosQosId,
       "cosId": cosId,
       "cosDefinition": cosDefinition,
       "cosBwRRatioMin": cosBwRRatioMin,
       "cosBwRRatioMax": cosBwRRatioMax,
       "cosHCInOctets": cosHCInOctets,
       "cosHCOutOctets": cosHCOutOctets,
       "cosHCInPkts": cosHCInPkts,
       "cosHCOutPkts": cosHCOutPkts,
       "cosHCInCCDiscards": cosHCInCCDiscards,
       "gfpNumber": gfpNumber,
       "gfpTable": gfpTable,
       "gfpEntry": gfpEntry,
       "gfpIndex": gfpIndex,
       "gfpHCInPkts": gfpHCInPkts,
       "gfpHCInIdlePkts": gfpHCInIdlePkts,
       "gfpHCInCorruptedPkts": gfpHCInCorruptedPkts,
       "gfpHCInErrors": gfpHCInErrors,
       "gfpHCInCorrectedPkts": gfpHCInCorrectedPkts,
       "gfpHCFCSErrors": gfpHCFCSErrors,
       "gfpHCInOctets": gfpHCInOctets,
       "gfpHCOutPkts": gfpHCOutPkts,
       "gfpHCOutIdlePkts": gfpHCOutIdlePkts,
       "gfpHCOutOctets": gfpHCOutOctets,
       "gfpIdleRate": gfpIdleRate,
       "gfpSendingRate": gfpSendingRate,
       "gfpState": gfpState,
       "gfpAdminStatus": gfpAdminStatus,
       "gfpOperStatus": gfpOperStatus,
       "gfpMonitor": gfpMonitor,
       "gfpFailure": gfpFailure,
       "gfpSeverity": gfpSeverity,
       "gfpOOFD": gfpOOFD,
       "gfpLOFD": gfpLOFD,
       "gfpFDSC": gfpFDSC,
       "pauseNumber": pauseNumber,
       "pauseTable": pauseTable,
       "pauseEntry": pauseEntry,
       "pauseIndex": pauseIndex,
       "pauseTime": pauseTime,
       "pauseBetweenTime": pauseBetweenTime,
       "pauseMacSA": pauseMacSA,
       "pauseMacDA": pauseMacDA,
       "pauseCHT": pauseCHT,
       "pauseCLT": pauseCLT,
       "pauseMonitor": pauseMonitor,
       "pauseFailure": pauseFailure,
       "pauseSeverity": pauseSeverity,
       "pauseModeRejected": pauseModeRejected}
)
