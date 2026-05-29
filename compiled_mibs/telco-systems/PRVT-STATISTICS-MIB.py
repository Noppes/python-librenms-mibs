# SNMP MIB module (PRVT-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-STATISTICS-MIB

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

(sapEntry,
 sdpEntry) = mibBuilder.importSymbols(
    "PRVT-SERV-MIB",
    "sapEntry",
    "sdpEntry")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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

prvtStatisticsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181)
)
if mibBuilder.loadTexts:
    prvtStatisticsMIB.setRevisions(
        ("2014-01-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class StatType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("bytes", 2),
          ("all", 3))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtStatObjects_ObjectIdentity = ObjectIdentity
prvtStatObjects = _PrvtStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1)
)
_PrvtStatIngressPolicyTable_Object = MibTable
prvtStatIngressPolicyTable = _PrvtStatIngressPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1)
)
if mibBuilder.loadTexts:
    prvtStatIngressPolicyTable.setStatus("current")
_PrvtStatIngressPolicyEntry_Object = MibTableRow
prvtStatIngressPolicyEntry = _PrvtStatIngressPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1)
)
prvtStatIngressPolicyEntry.setIndexNames(
    (0, "PRVT-STATISTICS-MIB", "prvtStatIngressPolicyName"),
)
if mibBuilder.loadTexts:
    prvtStatIngressPolicyEntry.setStatus("current")


class _PrvtStatIngressPolicyName_Type(OctetString):
    """Custom type prvtStatIngressPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtStatIngressPolicyName_Type.__name__ = "OctetString"
_PrvtStatIngressPolicyName_Object = MibTableColumn
prvtStatIngressPolicyName = _PrvtStatIngressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 1),
    _PrvtStatIngressPolicyName_Type()
)
prvtStatIngressPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyName.setStatus("current")
_PrvtStatIngressPolicyRowStatus_Type = RowStatus
_PrvtStatIngressPolicyRowStatus_Object = MibTableColumn
prvtStatIngressPolicyRowStatus = _PrvtStatIngressPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 2),
    _PrvtStatIngressPolicyRowStatus_Type()
)
prvtStatIngressPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyRowStatus.setStatus("current")
_PrvtStatIngressPolicyDetailed_Type = TruthValue
_PrvtStatIngressPolicyDetailed_Object = MibTableColumn
prvtStatIngressPolicyDetailed = _PrvtStatIngressPolicyDetailed_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 3),
    _PrvtStatIngressPolicyDetailed_Type()
)
prvtStatIngressPolicyDetailed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyDetailed.setStatus("current")


class _PrvtStatIngressPolicyDescription_Type(OctetString):
    """Custom type prvtStatIngressPolicyDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_PrvtStatIngressPolicyDescription_Type.__name__ = "OctetString"
_PrvtStatIngressPolicyDescription_Object = MibTableColumn
prvtStatIngressPolicyDescription = _PrvtStatIngressPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 4),
    _PrvtStatIngressPolicyDescription_Type()
)
prvtStatIngressPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyDescription.setStatus("current")
_PrvtStatIngressPolicyFc_Type = TruthValue
_PrvtStatIngressPolicyFc_Object = MibTableColumn
prvtStatIngressPolicyFc = _PrvtStatIngressPolicyFc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 5),
    _PrvtStatIngressPolicyFc_Type()
)
prvtStatIngressPolicyFc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyFc.setStatus("current")
_PrvtStatIngressPolicyFcBwMeasurement_Type = StatType
_PrvtStatIngressPolicyFcBwMeasurement_Object = MibTableColumn
prvtStatIngressPolicyFcBwMeasurement = _PrvtStatIngressPolicyFcBwMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 6),
    _PrvtStatIngressPolicyFcBwMeasurement_Type()
)
prvtStatIngressPolicyFcBwMeasurement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyFcBwMeasurement.setStatus("current")
_PrvtStatIngressPolicyColor_Type = TruthValue
_PrvtStatIngressPolicyColor_Object = MibTableColumn
prvtStatIngressPolicyColor = _PrvtStatIngressPolicyColor_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 7),
    _PrvtStatIngressPolicyColor_Type()
)
prvtStatIngressPolicyColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyColor.setStatus("current")
_PrvtStatIngressPolicyColorBwMeasurement_Type = StatType
_PrvtStatIngressPolicyColorBwMeasurement_Object = MibTableColumn
prvtStatIngressPolicyColorBwMeasurement = _PrvtStatIngressPolicyColorBwMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 8),
    _PrvtStatIngressPolicyColorBwMeasurement_Type()
)
prvtStatIngressPolicyColorBwMeasurement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyColorBwMeasurement.setStatus("current")
_PrvtStatIngressPolicyUnicast_Type = TruthValue
_PrvtStatIngressPolicyUnicast_Object = MibTableColumn
prvtStatIngressPolicyUnicast = _PrvtStatIngressPolicyUnicast_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 9),
    _PrvtStatIngressPolicyUnicast_Type()
)
prvtStatIngressPolicyUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyUnicast.setStatus("current")
_PrvtStatIngressPolicyUnicastBwMeasurement_Type = StatType
_PrvtStatIngressPolicyUnicastBwMeasurement_Object = MibTableColumn
prvtStatIngressPolicyUnicastBwMeasurement = _PrvtStatIngressPolicyUnicastBwMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 10),
    _PrvtStatIngressPolicyUnicastBwMeasurement_Type()
)
prvtStatIngressPolicyUnicastBwMeasurement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyUnicastBwMeasurement.setStatus("current")
_PrvtStatIngressPolicyBroadcast_Type = TruthValue
_PrvtStatIngressPolicyBroadcast_Object = MibTableColumn
prvtStatIngressPolicyBroadcast = _PrvtStatIngressPolicyBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 11),
    _PrvtStatIngressPolicyBroadcast_Type()
)
prvtStatIngressPolicyBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyBroadcast.setStatus("current")
_PrvtStatIngressPolicyBroadcastBwMeasurement_Type = StatType
_PrvtStatIngressPolicyBroadcastBwMeasurement_Object = MibTableColumn
prvtStatIngressPolicyBroadcastBwMeasurement = _PrvtStatIngressPolicyBroadcastBwMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 12),
    _PrvtStatIngressPolicyBroadcastBwMeasurement_Type()
)
prvtStatIngressPolicyBroadcastBwMeasurement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyBroadcastBwMeasurement.setStatus("current")
_PrvtStatIngressPolicyMulticast_Type = TruthValue
_PrvtStatIngressPolicyMulticast_Object = MibTableColumn
prvtStatIngressPolicyMulticast = _PrvtStatIngressPolicyMulticast_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 13),
    _PrvtStatIngressPolicyMulticast_Type()
)
prvtStatIngressPolicyMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyMulticast.setStatus("current")
_PrvtStatIngressPolicyMulticastBwMeasurement_Type = StatType
_PrvtStatIngressPolicyMulticastBwMeasurement_Object = MibTableColumn
prvtStatIngressPolicyMulticastBwMeasurement = _PrvtStatIngressPolicyMulticastBwMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 1, 1, 14),
    _PrvtStatIngressPolicyMulticastBwMeasurement_Type()
)
prvtStatIngressPolicyMulticastBwMeasurement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatIngressPolicyMulticastBwMeasurement.setStatus("current")
_PrvtStatEgressPolicyTable_Object = MibTable
prvtStatEgressPolicyTable = _PrvtStatEgressPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2)
)
if mibBuilder.loadTexts:
    prvtStatEgressPolicyTable.setStatus("current")
_PrvtStatEgressPolicyEntry_Object = MibTableRow
prvtStatEgressPolicyEntry = _PrvtStatEgressPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1)
)
prvtStatEgressPolicyEntry.setIndexNames(
    (0, "PRVT-STATISTICS-MIB", "prvtStatEgressPolicyName"),
)
if mibBuilder.loadTexts:
    prvtStatEgressPolicyEntry.setStatus("current")


class _PrvtStatEgressPolicyName_Type(OctetString):
    """Custom type prvtStatEgressPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtStatEgressPolicyName_Type.__name__ = "OctetString"
_PrvtStatEgressPolicyName_Object = MibTableColumn
prvtStatEgressPolicyName = _PrvtStatEgressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 1),
    _PrvtStatEgressPolicyName_Type()
)
prvtStatEgressPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyName.setStatus("current")
_PrvtStatEgressPolicyRowStatus_Type = RowStatus
_PrvtStatEgressPolicyRowStatus_Object = MibTableColumn
prvtStatEgressPolicyRowStatus = _PrvtStatEgressPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 2),
    _PrvtStatEgressPolicyRowStatus_Type()
)
prvtStatEgressPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyRowStatus.setStatus("current")
_PrvtStatEgressPolicyDetailed_Type = TruthValue
_PrvtStatEgressPolicyDetailed_Object = MibTableColumn
prvtStatEgressPolicyDetailed = _PrvtStatEgressPolicyDetailed_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 3),
    _PrvtStatEgressPolicyDetailed_Type()
)
prvtStatEgressPolicyDetailed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyDetailed.setStatus("current")


class _PrvtStatEgressPolicyDescription_Type(OctetString):
    """Custom type prvtStatEgressPolicyDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_PrvtStatEgressPolicyDescription_Type.__name__ = "OctetString"
_PrvtStatEgressPolicyDescription_Object = MibTableColumn
prvtStatEgressPolicyDescription = _PrvtStatEgressPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 4),
    _PrvtStatEgressPolicyDescription_Type()
)
prvtStatEgressPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyDescription.setStatus("current")
_PrvtStatEgressPolicyFc_Type = TruthValue
_PrvtStatEgressPolicyFc_Object = MibTableColumn
prvtStatEgressPolicyFc = _PrvtStatEgressPolicyFc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 5),
    _PrvtStatEgressPolicyFc_Type()
)
prvtStatEgressPolicyFc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyFc.setStatus("current")
_PrvtStatEgressPolicyFcBwMeasurement_Type = StatType
_PrvtStatEgressPolicyFcBwMeasurement_Object = MibTableColumn
prvtStatEgressPolicyFcBwMeasurement = _PrvtStatEgressPolicyFcBwMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 6),
    _PrvtStatEgressPolicyFcBwMeasurement_Type()
)
prvtStatEgressPolicyFcBwMeasurement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyFcBwMeasurement.setStatus("current")
_PrvtStatEgressPolicyColor_Type = TruthValue
_PrvtStatEgressPolicyColor_Object = MibTableColumn
prvtStatEgressPolicyColor = _PrvtStatEgressPolicyColor_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 7),
    _PrvtStatEgressPolicyColor_Type()
)
prvtStatEgressPolicyColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyColor.setStatus("current")
_PrvtStatEgressPolicyColorBwMeasurement_Type = StatType
_PrvtStatEgressPolicyColorBwMeasurement_Object = MibTableColumn
prvtStatEgressPolicyColorBwMeasurement = _PrvtStatEgressPolicyColorBwMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 8),
    _PrvtStatEgressPolicyColorBwMeasurement_Type()
)
prvtStatEgressPolicyColorBwMeasurement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyColorBwMeasurement.setStatus("current")
_PrvtStatEgressPolicyDaType_Type = TruthValue
_PrvtStatEgressPolicyDaType_Object = MibTableColumn
prvtStatEgressPolicyDaType = _PrvtStatEgressPolicyDaType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 9),
    _PrvtStatEgressPolicyDaType_Type()
)
prvtStatEgressPolicyDaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyDaType.setStatus("current")
_PrvtStatEgressPolicyDaTypeBwMeasurement_Type = StatType
_PrvtStatEgressPolicyDaTypeBwMeasurement_Object = MibTableColumn
prvtStatEgressPolicyDaTypeBwMeasurement = _PrvtStatEgressPolicyDaTypeBwMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 2, 1, 10),
    _PrvtStatEgressPolicyDaTypeBwMeasurement_Type()
)
prvtStatEgressPolicyDaTypeBwMeasurement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatEgressPolicyDaTypeBwMeasurement.setStatus("current")
_PrvtStatSapTable_Object = MibTable
prvtStatSapTable = _PrvtStatSapTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3)
)
if mibBuilder.loadTexts:
    prvtStatSapTable.setStatus("current")
_PrvtStatSapEntry_Object = MibTableRow
prvtStatSapEntry = _PrvtStatSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1)
)
if mibBuilder.loadTexts:
    prvtStatSapEntry.setStatus("current")


class _PrvtStatSapIngressPolicy_Type(OctetString):
    """Custom type prvtStatSapIngressPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtStatSapIngressPolicy_Type.__name__ = "OctetString"
_PrvtStatSapIngressPolicy_Object = MibTableColumn
prvtStatSapIngressPolicy = _PrvtStatSapIngressPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 1),
    _PrvtStatSapIngressPolicy_Type()
)
prvtStatSapIngressPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatSapIngressPolicy.setStatus("current")


class _PrvtStatSapEgressPolicy_Type(OctetString):
    """Custom type prvtStatSapEgressPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtStatSapEgressPolicy_Type.__name__ = "OctetString"
_PrvtStatSapEgressPolicy_Object = MibTableColumn
prvtStatSapEgressPolicy = _PrvtStatSapEgressPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 2),
    _PrvtStatSapEgressPolicy_Type()
)
prvtStatSapEgressPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatSapEgressPolicy.setStatus("current")
_PrvtStatSapClear_Type = TruthValue
_PrvtStatSapClear_Object = MibTableColumn
prvtStatSapClear = _PrvtStatSapClear_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 3),
    _PrvtStatSapClear_Type()
)
prvtStatSapClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatSapClear.setStatus("current")
_PrvtStatSapInPackets_Type = Counter64
_PrvtStatSapInPackets_Object = MibTableColumn
prvtStatSapInPackets = _PrvtStatSapInPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 4),
    _PrvtStatSapInPackets_Type()
)
prvtStatSapInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapInPackets.setStatus("current")
_PrvtStatSapInBytes_Type = Counter64
_PrvtStatSapInBytes_Object = MibTableColumn
prvtStatSapInBytes = _PrvtStatSapInBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 5),
    _PrvtStatSapInBytes_Type()
)
prvtStatSapInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapInBytes.setStatus("current")
_PrvtStatSapDropPackets_Type = Counter64
_PrvtStatSapDropPackets_Object = MibTableColumn
prvtStatSapDropPackets = _PrvtStatSapDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 6),
    _PrvtStatSapDropPackets_Type()
)
prvtStatSapDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapDropPackets.setStatus("current")
_PrvtStatSapDropBytes_Type = Counter64
_PrvtStatSapDropBytes_Object = MibTableColumn
prvtStatSapDropBytes = _PrvtStatSapDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 7),
    _PrvtStatSapDropBytes_Type()
)
prvtStatSapDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapDropBytes.setStatus("current")
_PrvtStatSapUnicastPackets_Type = Counter64
_PrvtStatSapUnicastPackets_Object = MibTableColumn
prvtStatSapUnicastPackets = _PrvtStatSapUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 8),
    _PrvtStatSapUnicastPackets_Type()
)
prvtStatSapUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapUnicastPackets.setStatus("current")
_PrvtStatSapUnicastBytes_Type = Counter64
_PrvtStatSapUnicastBytes_Object = MibTableColumn
prvtStatSapUnicastBytes = _PrvtStatSapUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 9),
    _PrvtStatSapUnicastBytes_Type()
)
prvtStatSapUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapUnicastBytes.setStatus("current")
_PrvtStatSapMulticastPackets_Type = Counter64
_PrvtStatSapMulticastPackets_Object = MibTableColumn
prvtStatSapMulticastPackets = _PrvtStatSapMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 10),
    _PrvtStatSapMulticastPackets_Type()
)
prvtStatSapMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapMulticastPackets.setStatus("current")
_PrvtStatSapMulticastBytes_Type = Counter64
_PrvtStatSapMulticastBytes_Object = MibTableColumn
prvtStatSapMulticastBytes = _PrvtStatSapMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 11),
    _PrvtStatSapMulticastBytes_Type()
)
prvtStatSapMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapMulticastBytes.setStatus("current")
_PrvtStatSapBroadcastPackets_Type = Counter64
_PrvtStatSapBroadcastPackets_Object = MibTableColumn
prvtStatSapBroadcastPackets = _PrvtStatSapBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 12),
    _PrvtStatSapBroadcastPackets_Type()
)
prvtStatSapBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapBroadcastPackets.setStatus("current")
_PrvtStatSapBroadcastBytes_Type = Counter64
_PrvtStatSapBroadcastBytes_Object = MibTableColumn
prvtStatSapBroadcastBytes = _PrvtStatSapBroadcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 13),
    _PrvtStatSapBroadcastBytes_Type()
)
prvtStatSapBroadcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapBroadcastBytes.setStatus("current")
_PrvtStatSapPri0Packets_Type = Counter64
_PrvtStatSapPri0Packets_Object = MibTableColumn
prvtStatSapPri0Packets = _PrvtStatSapPri0Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 14),
    _PrvtStatSapPri0Packets_Type()
)
prvtStatSapPri0Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri0Packets.setStatus("current")
_PrvtStatSapPri0Bytes_Type = Counter64
_PrvtStatSapPri0Bytes_Object = MibTableColumn
prvtStatSapPri0Bytes = _PrvtStatSapPri0Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 15),
    _PrvtStatSapPri0Bytes_Type()
)
prvtStatSapPri0Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri0Bytes.setStatus("current")
_PrvtStatSapPri1Packets_Type = Counter64
_PrvtStatSapPri1Packets_Object = MibTableColumn
prvtStatSapPri1Packets = _PrvtStatSapPri1Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 16),
    _PrvtStatSapPri1Packets_Type()
)
prvtStatSapPri1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri1Packets.setStatus("current")
_PrvtStatSapPri1Bytes_Type = Counter64
_PrvtStatSapPri1Bytes_Object = MibTableColumn
prvtStatSapPri1Bytes = _PrvtStatSapPri1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 17),
    _PrvtStatSapPri1Bytes_Type()
)
prvtStatSapPri1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri1Bytes.setStatus("current")
_PrvtStatSapPri2Packets_Type = Counter64
_PrvtStatSapPri2Packets_Object = MibTableColumn
prvtStatSapPri2Packets = _PrvtStatSapPri2Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 18),
    _PrvtStatSapPri2Packets_Type()
)
prvtStatSapPri2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri2Packets.setStatus("current")
_PrvtStatSapPri2Bytes_Type = Counter64
_PrvtStatSapPri2Bytes_Object = MibTableColumn
prvtStatSapPri2Bytes = _PrvtStatSapPri2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 19),
    _PrvtStatSapPri2Bytes_Type()
)
prvtStatSapPri2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri2Bytes.setStatus("current")
_PrvtStatSapPri3Packets_Type = Counter64
_PrvtStatSapPri3Packets_Object = MibTableColumn
prvtStatSapPri3Packets = _PrvtStatSapPri3Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 20),
    _PrvtStatSapPri3Packets_Type()
)
prvtStatSapPri3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri3Packets.setStatus("current")
_PrvtStatSapPri3Bytes_Type = Counter64
_PrvtStatSapPri3Bytes_Object = MibTableColumn
prvtStatSapPri3Bytes = _PrvtStatSapPri3Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 21),
    _PrvtStatSapPri3Bytes_Type()
)
prvtStatSapPri3Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri3Bytes.setStatus("current")
_PrvtStatSapPri4Packets_Type = Counter64
_PrvtStatSapPri4Packets_Object = MibTableColumn
prvtStatSapPri4Packets = _PrvtStatSapPri4Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 22),
    _PrvtStatSapPri4Packets_Type()
)
prvtStatSapPri4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri4Packets.setStatus("current")
_PrvtStatSapPri4Bytes_Type = Counter64
_PrvtStatSapPri4Bytes_Object = MibTableColumn
prvtStatSapPri4Bytes = _PrvtStatSapPri4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 23),
    _PrvtStatSapPri4Bytes_Type()
)
prvtStatSapPri4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri4Bytes.setStatus("current")
_PrvtStatSapPri5Packets_Type = Counter64
_PrvtStatSapPri5Packets_Object = MibTableColumn
prvtStatSapPri5Packets = _PrvtStatSapPri5Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 24),
    _PrvtStatSapPri5Packets_Type()
)
prvtStatSapPri5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri5Packets.setStatus("current")
_PrvtStatSapPri5Bytes_Type = Counter64
_PrvtStatSapPri5Bytes_Object = MibTableColumn
prvtStatSapPri5Bytes = _PrvtStatSapPri5Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 25),
    _PrvtStatSapPri5Bytes_Type()
)
prvtStatSapPri5Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri5Bytes.setStatus("current")
_PrvtStatSapPri6Packets_Type = Counter64
_PrvtStatSapPri6Packets_Object = MibTableColumn
prvtStatSapPri6Packets = _PrvtStatSapPri6Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 26),
    _PrvtStatSapPri6Packets_Type()
)
prvtStatSapPri6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri6Packets.setStatus("current")
_PrvtStatSapPri6Bytes_Type = Counter64
_PrvtStatSapPri6Bytes_Object = MibTableColumn
prvtStatSapPri6Bytes = _PrvtStatSapPri6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 27),
    _PrvtStatSapPri6Bytes_Type()
)
prvtStatSapPri6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri6Bytes.setStatus("current")
_PrvtStatSapPri7Packets_Type = Counter64
_PrvtStatSapPri7Packets_Object = MibTableColumn
prvtStatSapPri7Packets = _PrvtStatSapPri7Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 28),
    _PrvtStatSapPri7Packets_Type()
)
prvtStatSapPri7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri7Packets.setStatus("current")
_PrvtStatSapPri7Bytes_Type = Counter64
_PrvtStatSapPri7Bytes_Object = MibTableColumn
prvtStatSapPri7Bytes = _PrvtStatSapPri7Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 29),
    _PrvtStatSapPri7Bytes_Type()
)
prvtStatSapPri7Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri7Bytes.setStatus("current")
_PrvtStatSapPri0yPackets_Type = Counter64
_PrvtStatSapPri0yPackets_Object = MibTableColumn
prvtStatSapPri0yPackets = _PrvtStatSapPri0yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 30),
    _PrvtStatSapPri0yPackets_Type()
)
prvtStatSapPri0yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri0yPackets.setStatus("current")
_PrvtStatSapPri0yBytes_Type = Counter64
_PrvtStatSapPri0yBytes_Object = MibTableColumn
prvtStatSapPri0yBytes = _PrvtStatSapPri0yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 31),
    _PrvtStatSapPri0yBytes_Type()
)
prvtStatSapPri0yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri0yBytes.setStatus("current")
_PrvtStatSapPri1yPackets_Type = Counter64
_PrvtStatSapPri1yPackets_Object = MibTableColumn
prvtStatSapPri1yPackets = _PrvtStatSapPri1yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 32),
    _PrvtStatSapPri1yPackets_Type()
)
prvtStatSapPri1yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri1yPackets.setStatus("current")
_PrvtStatSapPri1yBytes_Type = Counter64
_PrvtStatSapPri1yBytes_Object = MibTableColumn
prvtStatSapPri1yBytes = _PrvtStatSapPri1yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 33),
    _PrvtStatSapPri1yBytes_Type()
)
prvtStatSapPri1yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri1yBytes.setStatus("current")
_PrvtStatSapPri2yPackets_Type = Counter64
_PrvtStatSapPri2yPackets_Object = MibTableColumn
prvtStatSapPri2yPackets = _PrvtStatSapPri2yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 34),
    _PrvtStatSapPri2yPackets_Type()
)
prvtStatSapPri2yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri2yPackets.setStatus("current")
_PrvtStatSapPri2yBytes_Type = Counter64
_PrvtStatSapPri2yBytes_Object = MibTableColumn
prvtStatSapPri2yBytes = _PrvtStatSapPri2yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 35),
    _PrvtStatSapPri2yBytes_Type()
)
prvtStatSapPri2yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri2yBytes.setStatus("current")
_PrvtStatSapPri3yPackets_Type = Counter64
_PrvtStatSapPri3yPackets_Object = MibTableColumn
prvtStatSapPri3yPackets = _PrvtStatSapPri3yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 36),
    _PrvtStatSapPri3yPackets_Type()
)
prvtStatSapPri3yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri3yPackets.setStatus("current")
_PrvtStatSapPri3yBytes_Type = Counter64
_PrvtStatSapPri3yBytes_Object = MibTableColumn
prvtStatSapPri3yBytes = _PrvtStatSapPri3yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 37),
    _PrvtStatSapPri3yBytes_Type()
)
prvtStatSapPri3yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri3yBytes.setStatus("current")
_PrvtStatSapPri4yPackets_Type = Counter64
_PrvtStatSapPri4yPackets_Object = MibTableColumn
prvtStatSapPri4yPackets = _PrvtStatSapPri4yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 38),
    _PrvtStatSapPri4yPackets_Type()
)
prvtStatSapPri4yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri4yPackets.setStatus("current")
_PrvtStatSapPri4yBytes_Type = Counter64
_PrvtStatSapPri4yBytes_Object = MibTableColumn
prvtStatSapPri4yBytes = _PrvtStatSapPri4yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 39),
    _PrvtStatSapPri4yBytes_Type()
)
prvtStatSapPri4yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri4yBytes.setStatus("current")
_PrvtStatSapPri5yPackets_Type = Counter64
_PrvtStatSapPri5yPackets_Object = MibTableColumn
prvtStatSapPri5yPackets = _PrvtStatSapPri5yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 40),
    _PrvtStatSapPri5yPackets_Type()
)
prvtStatSapPri5yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri5yPackets.setStatus("current")
_PrvtStatSapPri5yBytes_Type = Counter64
_PrvtStatSapPri5yBytes_Object = MibTableColumn
prvtStatSapPri5yBytes = _PrvtStatSapPri5yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 41),
    _PrvtStatSapPri5yBytes_Type()
)
prvtStatSapPri5yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri5yBytes.setStatus("current")
_PrvtStatSapPri6yPackets_Type = Counter64
_PrvtStatSapPri6yPackets_Object = MibTableColumn
prvtStatSapPri6yPackets = _PrvtStatSapPri6yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 42),
    _PrvtStatSapPri6yPackets_Type()
)
prvtStatSapPri6yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri6yPackets.setStatus("current")
_PrvtStatSapPri6yBytes_Type = Counter64
_PrvtStatSapPri6yBytes_Object = MibTableColumn
prvtStatSapPri6yBytes = _PrvtStatSapPri6yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 43),
    _PrvtStatSapPri6yBytes_Type()
)
prvtStatSapPri6yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri6yBytes.setStatus("current")
_PrvtStatSapPri7yPackets_Type = Counter64
_PrvtStatSapPri7yPackets_Object = MibTableColumn
prvtStatSapPri7yPackets = _PrvtStatSapPri7yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 44),
    _PrvtStatSapPri7yPackets_Type()
)
prvtStatSapPri7yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri7yPackets.setStatus("current")
_PrvtStatSapPri7yBytes_Type = Counter64
_PrvtStatSapPri7yBytes_Object = MibTableColumn
prvtStatSapPri7yBytes = _PrvtStatSapPri7yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 45),
    _PrvtStatSapPri7yBytes_Type()
)
prvtStatSapPri7yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapPri7yBytes.setStatus("current")
_PrvtStatSapEgPackets_Type = Counter64
_PrvtStatSapEgPackets_Object = MibTableColumn
prvtStatSapEgPackets = _PrvtStatSapEgPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 46),
    _PrvtStatSapEgPackets_Type()
)
prvtStatSapEgPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPackets.setStatus("current")
_PrvtStatSapEgBytes_Type = Counter64
_PrvtStatSapEgBytes_Object = MibTableColumn
prvtStatSapEgBytes = _PrvtStatSapEgBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 47),
    _PrvtStatSapEgBytes_Type()
)
prvtStatSapEgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgBytes.setStatus("current")
_PrvtStatSapEgUnicastPackets_Type = Counter64
_PrvtStatSapEgUnicastPackets_Object = MibTableColumn
prvtStatSapEgUnicastPackets = _PrvtStatSapEgUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 48),
    _PrvtStatSapEgUnicastPackets_Type()
)
prvtStatSapEgUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgUnicastPackets.setStatus("current")
_PrvtStatSapEgUnicastBytes_Type = Counter64
_PrvtStatSapEgUnicastBytes_Object = MibTableColumn
prvtStatSapEgUnicastBytes = _PrvtStatSapEgUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 49),
    _PrvtStatSapEgUnicastBytes_Type()
)
prvtStatSapEgUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgUnicastBytes.setStatus("current")
_PrvtStatSapEgMulticastPackets_Type = Counter64
_PrvtStatSapEgMulticastPackets_Object = MibTableColumn
prvtStatSapEgMulticastPackets = _PrvtStatSapEgMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 50),
    _PrvtStatSapEgMulticastPackets_Type()
)
prvtStatSapEgMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgMulticastPackets.setStatus("current")
_PrvtStatSapEgMulticastBytes_Type = Counter64
_PrvtStatSapEgMulticastBytes_Object = MibTableColumn
prvtStatSapEgMulticastBytes = _PrvtStatSapEgMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 51),
    _PrvtStatSapEgMulticastBytes_Type()
)
prvtStatSapEgMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgMulticastBytes.setStatus("current")
_PrvtStatSapEgBroadcastPackets_Type = Counter64
_PrvtStatSapEgBroadcastPackets_Object = MibTableColumn
prvtStatSapEgBroadcastPackets = _PrvtStatSapEgBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 52),
    _PrvtStatSapEgBroadcastPackets_Type()
)
prvtStatSapEgBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgBroadcastPackets.setStatus("current")
_PrvtStatSapEgBroadcastBytes_Type = Counter64
_PrvtStatSapEgBroadcastBytes_Object = MibTableColumn
prvtStatSapEgBroadcastBytes = _PrvtStatSapEgBroadcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 53),
    _PrvtStatSapEgBroadcastBytes_Type()
)
prvtStatSapEgBroadcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgBroadcastBytes.setStatus("current")
_PrvtStatSapEgPri0Packets_Type = Counter64
_PrvtStatSapEgPri0Packets_Object = MibTableColumn
prvtStatSapEgPri0Packets = _PrvtStatSapEgPri0Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 54),
    _PrvtStatSapEgPri0Packets_Type()
)
prvtStatSapEgPri0Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri0Packets.setStatus("current")
_PrvtStatSapEgPri0Bytes_Type = Counter64
_PrvtStatSapEgPri0Bytes_Object = MibTableColumn
prvtStatSapEgPri0Bytes = _PrvtStatSapEgPri0Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 55),
    _PrvtStatSapEgPri0Bytes_Type()
)
prvtStatSapEgPri0Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri0Bytes.setStatus("current")
_PrvtStatSapEgPri1Packets_Type = Counter64
_PrvtStatSapEgPri1Packets_Object = MibTableColumn
prvtStatSapEgPri1Packets = _PrvtStatSapEgPri1Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 56),
    _PrvtStatSapEgPri1Packets_Type()
)
prvtStatSapEgPri1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri1Packets.setStatus("current")
_PrvtStatSapEgPri1Bytes_Type = Counter64
_PrvtStatSapEgPri1Bytes_Object = MibTableColumn
prvtStatSapEgPri1Bytes = _PrvtStatSapEgPri1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 57),
    _PrvtStatSapEgPri1Bytes_Type()
)
prvtStatSapEgPri1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri1Bytes.setStatus("current")
_PrvtStatSapEgPri2Packets_Type = Counter64
_PrvtStatSapEgPri2Packets_Object = MibTableColumn
prvtStatSapEgPri2Packets = _PrvtStatSapEgPri2Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 58),
    _PrvtStatSapEgPri2Packets_Type()
)
prvtStatSapEgPri2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri2Packets.setStatus("current")
_PrvtStatSapEgPri2Bytes_Type = Counter64
_PrvtStatSapEgPri2Bytes_Object = MibTableColumn
prvtStatSapEgPri2Bytes = _PrvtStatSapEgPri2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 59),
    _PrvtStatSapEgPri2Bytes_Type()
)
prvtStatSapEgPri2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri2Bytes.setStatus("current")
_PrvtStatSapEgPri3Packets_Type = Counter64
_PrvtStatSapEgPri3Packets_Object = MibTableColumn
prvtStatSapEgPri3Packets = _PrvtStatSapEgPri3Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 60),
    _PrvtStatSapEgPri3Packets_Type()
)
prvtStatSapEgPri3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri3Packets.setStatus("current")
_PrvtStatSapEgPri3Bytes_Type = Counter64
_PrvtStatSapEgPri3Bytes_Object = MibTableColumn
prvtStatSapEgPri3Bytes = _PrvtStatSapEgPri3Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 61),
    _PrvtStatSapEgPri3Bytes_Type()
)
prvtStatSapEgPri3Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri3Bytes.setStatus("current")
_PrvtStatSapEgPri4Packets_Type = Counter64
_PrvtStatSapEgPri4Packets_Object = MibTableColumn
prvtStatSapEgPri4Packets = _PrvtStatSapEgPri4Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 62),
    _PrvtStatSapEgPri4Packets_Type()
)
prvtStatSapEgPri4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri4Packets.setStatus("current")
_PrvtStatSapEgPri4Bytes_Type = Counter64
_PrvtStatSapEgPri4Bytes_Object = MibTableColumn
prvtStatSapEgPri4Bytes = _PrvtStatSapEgPri4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 63),
    _PrvtStatSapEgPri4Bytes_Type()
)
prvtStatSapEgPri4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri4Bytes.setStatus("current")
_PrvtStatSapEgPri5Packets_Type = Counter64
_PrvtStatSapEgPri5Packets_Object = MibTableColumn
prvtStatSapEgPri5Packets = _PrvtStatSapEgPri5Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 64),
    _PrvtStatSapEgPri5Packets_Type()
)
prvtStatSapEgPri5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri5Packets.setStatus("current")
_PrvtStatSapEgPri5Bytes_Type = Counter64
_PrvtStatSapEgPri5Bytes_Object = MibTableColumn
prvtStatSapEgPri5Bytes = _PrvtStatSapEgPri5Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 65),
    _PrvtStatSapEgPri5Bytes_Type()
)
prvtStatSapEgPri5Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri5Bytes.setStatus("current")
_PrvtStatSapEgPri6Packets_Type = Counter64
_PrvtStatSapEgPri6Packets_Object = MibTableColumn
prvtStatSapEgPri6Packets = _PrvtStatSapEgPri6Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 66),
    _PrvtStatSapEgPri6Packets_Type()
)
prvtStatSapEgPri6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri6Packets.setStatus("current")
_PrvtStatSapEgPri6Bytes_Type = Counter64
_PrvtStatSapEgPri6Bytes_Object = MibTableColumn
prvtStatSapEgPri6Bytes = _PrvtStatSapEgPri6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 67),
    _PrvtStatSapEgPri6Bytes_Type()
)
prvtStatSapEgPri6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri6Bytes.setStatus("current")
_PrvtStatSapEgPri7Packets_Type = Counter64
_PrvtStatSapEgPri7Packets_Object = MibTableColumn
prvtStatSapEgPri7Packets = _PrvtStatSapEgPri7Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 68),
    _PrvtStatSapEgPri7Packets_Type()
)
prvtStatSapEgPri7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri7Packets.setStatus("current")
_PrvtStatSapEgPri7Bytes_Type = Counter64
_PrvtStatSapEgPri7Bytes_Object = MibTableColumn
prvtStatSapEgPri7Bytes = _PrvtStatSapEgPri7Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 69),
    _PrvtStatSapEgPri7Bytes_Type()
)
prvtStatSapEgPri7Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri7Bytes.setStatus("current")
_PrvtStatSapEgPri0yPackets_Type = Counter64
_PrvtStatSapEgPri0yPackets_Object = MibTableColumn
prvtStatSapEgPri0yPackets = _PrvtStatSapEgPri0yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 70),
    _PrvtStatSapEgPri0yPackets_Type()
)
prvtStatSapEgPri0yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri0yPackets.setStatus("current")
_PrvtStatSapEgPri0yBytes_Type = Counter64
_PrvtStatSapEgPri0yBytes_Object = MibTableColumn
prvtStatSapEgPri0yBytes = _PrvtStatSapEgPri0yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 71),
    _PrvtStatSapEgPri0yBytes_Type()
)
prvtStatSapEgPri0yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri0yBytes.setStatus("current")
_PrvtStatSapEgPri1yPackets_Type = Counter64
_PrvtStatSapEgPri1yPackets_Object = MibTableColumn
prvtStatSapEgPri1yPackets = _PrvtStatSapEgPri1yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 72),
    _PrvtStatSapEgPri1yPackets_Type()
)
prvtStatSapEgPri1yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri1yPackets.setStatus("current")
_PrvtStatSapEgPri1yBytes_Type = Counter64
_PrvtStatSapEgPri1yBytes_Object = MibTableColumn
prvtStatSapEgPri1yBytes = _PrvtStatSapEgPri1yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 73),
    _PrvtStatSapEgPri1yBytes_Type()
)
prvtStatSapEgPri1yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri1yBytes.setStatus("current")
_PrvtStatSapEgPri2yPackets_Type = Counter64
_PrvtStatSapEgPri2yPackets_Object = MibTableColumn
prvtStatSapEgPri2yPackets = _PrvtStatSapEgPri2yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 74),
    _PrvtStatSapEgPri2yPackets_Type()
)
prvtStatSapEgPri2yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri2yPackets.setStatus("current")
_PrvtStatSapEgPri2yBytes_Type = Counter64
_PrvtStatSapEgPri2yBytes_Object = MibTableColumn
prvtStatSapEgPri2yBytes = _PrvtStatSapEgPri2yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 75),
    _PrvtStatSapEgPri2yBytes_Type()
)
prvtStatSapEgPri2yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri2yBytes.setStatus("current")
_PrvtStatSapEgPri3yPackets_Type = Counter64
_PrvtStatSapEgPri3yPackets_Object = MibTableColumn
prvtStatSapEgPri3yPackets = _PrvtStatSapEgPri3yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 76),
    _PrvtStatSapEgPri3yPackets_Type()
)
prvtStatSapEgPri3yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri3yPackets.setStatus("current")
_PrvtStatSapEgPri3yBytes_Type = Counter64
_PrvtStatSapEgPri3yBytes_Object = MibTableColumn
prvtStatSapEgPri3yBytes = _PrvtStatSapEgPri3yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 77),
    _PrvtStatSapEgPri3yBytes_Type()
)
prvtStatSapEgPri3yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri3yBytes.setStatus("current")
_PrvtStatSapEgPri4yPackets_Type = Counter64
_PrvtStatSapEgPri4yPackets_Object = MibTableColumn
prvtStatSapEgPri4yPackets = _PrvtStatSapEgPri4yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 78),
    _PrvtStatSapEgPri4yPackets_Type()
)
prvtStatSapEgPri4yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri4yPackets.setStatus("current")
_PrvtStatSapEgPri4yBytes_Type = Counter64
_PrvtStatSapEgPri4yBytes_Object = MibTableColumn
prvtStatSapEgPri4yBytes = _PrvtStatSapEgPri4yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 79),
    _PrvtStatSapEgPri4yBytes_Type()
)
prvtStatSapEgPri4yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri4yBytes.setStatus("current")
_PrvtStatSapEgPri5yPackets_Type = Counter64
_PrvtStatSapEgPri5yPackets_Object = MibTableColumn
prvtStatSapEgPri5yPackets = _PrvtStatSapEgPri5yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 80),
    _PrvtStatSapEgPri5yPackets_Type()
)
prvtStatSapEgPri5yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri5yPackets.setStatus("current")
_PrvtStatSapEgPri5yBytes_Type = Counter64
_PrvtStatSapEgPri5yBytes_Object = MibTableColumn
prvtStatSapEgPri5yBytes = _PrvtStatSapEgPri5yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 81),
    _PrvtStatSapEgPri5yBytes_Type()
)
prvtStatSapEgPri5yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri5yBytes.setStatus("current")
_PrvtStatSapEgPri6yPackets_Type = Counter64
_PrvtStatSapEgPri6yPackets_Object = MibTableColumn
prvtStatSapEgPri6yPackets = _PrvtStatSapEgPri6yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 82),
    _PrvtStatSapEgPri6yPackets_Type()
)
prvtStatSapEgPri6yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri6yPackets.setStatus("current")
_PrvtStatSapEgPri6yBytes_Type = Counter64
_PrvtStatSapEgPri6yBytes_Object = MibTableColumn
prvtStatSapEgPri6yBytes = _PrvtStatSapEgPri6yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 83),
    _PrvtStatSapEgPri6yBytes_Type()
)
prvtStatSapEgPri6yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri6yBytes.setStatus("current")
_PrvtStatSapEgPri7yPackets_Type = Counter64
_PrvtStatSapEgPri7yPackets_Object = MibTableColumn
prvtStatSapEgPri7yPackets = _PrvtStatSapEgPri7yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 84),
    _PrvtStatSapEgPri7yPackets_Type()
)
prvtStatSapEgPri7yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri7yPackets.setStatus("current")
_PrvtStatSapEgPri7yBytes_Type = Counter64
_PrvtStatSapEgPri7yBytes_Object = MibTableColumn
prvtStatSapEgPri7yBytes = _PrvtStatSapEgPri7yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 3, 1, 85),
    _PrvtStatSapEgPri7yBytes_Type()
)
prvtStatSapEgPri7yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSapEgPri7yBytes.setStatus("current")
_PrvtStatSdpTable_Object = MibTable
prvtStatSdpTable = _PrvtStatSdpTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4)
)
if mibBuilder.loadTexts:
    prvtStatSdpTable.setStatus("current")
_PrvtStatSdpEntry_Object = MibTableRow
prvtStatSdpEntry = _PrvtStatSdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1)
)
if mibBuilder.loadTexts:
    prvtStatSdpEntry.setStatus("current")


class _PrvtStatSdpIngressPolicy_Type(OctetString):
    """Custom type prvtStatSdpIngressPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtStatSdpIngressPolicy_Type.__name__ = "OctetString"
_PrvtStatSdpIngressPolicy_Object = MibTableColumn
prvtStatSdpIngressPolicy = _PrvtStatSdpIngressPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 1),
    _PrvtStatSdpIngressPolicy_Type()
)
prvtStatSdpIngressPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatSdpIngressPolicy.setStatus("current")


class _PrvtStatSdpEgressPolicy_Type(OctetString):
    """Custom type prvtStatSdpEgressPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtStatSdpEgressPolicy_Type.__name__ = "OctetString"
_PrvtStatSdpEgressPolicy_Object = MibTableColumn
prvtStatSdpEgressPolicy = _PrvtStatSdpEgressPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 2),
    _PrvtStatSdpEgressPolicy_Type()
)
prvtStatSdpEgressPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatSdpEgressPolicy.setStatus("current")
_PrvtStatSdpClear_Type = TruthValue
_PrvtStatSdpClear_Object = MibTableColumn
prvtStatSdpClear = _PrvtStatSdpClear_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 3),
    _PrvtStatSdpClear_Type()
)
prvtStatSdpClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatSdpClear.setStatus("current")
_PrvtStatSdpInPackets_Type = Counter64
_PrvtStatSdpInPackets_Object = MibTableColumn
prvtStatSdpInPackets = _PrvtStatSdpInPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 4),
    _PrvtStatSdpInPackets_Type()
)
prvtStatSdpInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpInPackets.setStatus("current")
_PrvtStatSdpInBytes_Type = Counter64
_PrvtStatSdpInBytes_Object = MibTableColumn
prvtStatSdpInBytes = _PrvtStatSdpInBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 5),
    _PrvtStatSdpInBytes_Type()
)
prvtStatSdpInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpInBytes.setStatus("current")
_PrvtStatSdpDropPackets_Type = Counter64
_PrvtStatSdpDropPackets_Object = MibTableColumn
prvtStatSdpDropPackets = _PrvtStatSdpDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 6),
    _PrvtStatSdpDropPackets_Type()
)
prvtStatSdpDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpDropPackets.setStatus("current")
_PrvtStatSdpDropBytes_Type = Counter64
_PrvtStatSdpDropBytes_Object = MibTableColumn
prvtStatSdpDropBytes = _PrvtStatSdpDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 7),
    _PrvtStatSdpDropBytes_Type()
)
prvtStatSdpDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpDropBytes.setStatus("current")
_PrvtStatSdpUnicastPackets_Type = Counter64
_PrvtStatSdpUnicastPackets_Object = MibTableColumn
prvtStatSdpUnicastPackets = _PrvtStatSdpUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 8),
    _PrvtStatSdpUnicastPackets_Type()
)
prvtStatSdpUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpUnicastPackets.setStatus("current")
_PrvtStatSdpUnicastBytes_Type = Counter64
_PrvtStatSdpUnicastBytes_Object = MibTableColumn
prvtStatSdpUnicastBytes = _PrvtStatSdpUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 9),
    _PrvtStatSdpUnicastBytes_Type()
)
prvtStatSdpUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpUnicastBytes.setStatus("current")
_PrvtStatSdpMulticastPackets_Type = Counter64
_PrvtStatSdpMulticastPackets_Object = MibTableColumn
prvtStatSdpMulticastPackets = _PrvtStatSdpMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 10),
    _PrvtStatSdpMulticastPackets_Type()
)
prvtStatSdpMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpMulticastPackets.setStatus("current")
_PrvtStatSdpMulticastBytes_Type = Counter64
_PrvtStatSdpMulticastBytes_Object = MibTableColumn
prvtStatSdpMulticastBytes = _PrvtStatSdpMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 11),
    _PrvtStatSdpMulticastBytes_Type()
)
prvtStatSdpMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpMulticastBytes.setStatus("current")
_PrvtStatSdpBroadcastPackets_Type = Counter64
_PrvtStatSdpBroadcastPackets_Object = MibTableColumn
prvtStatSdpBroadcastPackets = _PrvtStatSdpBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 12),
    _PrvtStatSdpBroadcastPackets_Type()
)
prvtStatSdpBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpBroadcastPackets.setStatus("current")
_PrvtStatSdpBroadcastBytes_Type = Counter64
_PrvtStatSdpBroadcastBytes_Object = MibTableColumn
prvtStatSdpBroadcastBytes = _PrvtStatSdpBroadcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 13),
    _PrvtStatSdpBroadcastBytes_Type()
)
prvtStatSdpBroadcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpBroadcastBytes.setStatus("current")
_PrvtStatSdpPri0Packets_Type = Counter64
_PrvtStatSdpPri0Packets_Object = MibTableColumn
prvtStatSdpPri0Packets = _PrvtStatSdpPri0Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 14),
    _PrvtStatSdpPri0Packets_Type()
)
prvtStatSdpPri0Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri0Packets.setStatus("current")
_PrvtStatSdpPri0Bytes_Type = Counter64
_PrvtStatSdpPri0Bytes_Object = MibTableColumn
prvtStatSdpPri0Bytes = _PrvtStatSdpPri0Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 15),
    _PrvtStatSdpPri0Bytes_Type()
)
prvtStatSdpPri0Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri0Bytes.setStatus("current")
_PrvtStatSdpPri1Packets_Type = Counter64
_PrvtStatSdpPri1Packets_Object = MibTableColumn
prvtStatSdpPri1Packets = _PrvtStatSdpPri1Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 16),
    _PrvtStatSdpPri1Packets_Type()
)
prvtStatSdpPri1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri1Packets.setStatus("current")
_PrvtStatSdpPri1Bytes_Type = Counter64
_PrvtStatSdpPri1Bytes_Object = MibTableColumn
prvtStatSdpPri1Bytes = _PrvtStatSdpPri1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 17),
    _PrvtStatSdpPri1Bytes_Type()
)
prvtStatSdpPri1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri1Bytes.setStatus("current")
_PrvtStatSdpPri2Packets_Type = Counter64
_PrvtStatSdpPri2Packets_Object = MibTableColumn
prvtStatSdpPri2Packets = _PrvtStatSdpPri2Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 18),
    _PrvtStatSdpPri2Packets_Type()
)
prvtStatSdpPri2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri2Packets.setStatus("current")
_PrvtStatSdpPri2Bytes_Type = Counter64
_PrvtStatSdpPri2Bytes_Object = MibTableColumn
prvtStatSdpPri2Bytes = _PrvtStatSdpPri2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 19),
    _PrvtStatSdpPri2Bytes_Type()
)
prvtStatSdpPri2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri2Bytes.setStatus("current")
_PrvtStatSdpPri3Packets_Type = Counter64
_PrvtStatSdpPri3Packets_Object = MibTableColumn
prvtStatSdpPri3Packets = _PrvtStatSdpPri3Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 20),
    _PrvtStatSdpPri3Packets_Type()
)
prvtStatSdpPri3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri3Packets.setStatus("current")
_PrvtStatSdpPri3Bytes_Type = Counter64
_PrvtStatSdpPri3Bytes_Object = MibTableColumn
prvtStatSdpPri3Bytes = _PrvtStatSdpPri3Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 21),
    _PrvtStatSdpPri3Bytes_Type()
)
prvtStatSdpPri3Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri3Bytes.setStatus("current")
_PrvtStatSdpPri4Packets_Type = Counter64
_PrvtStatSdpPri4Packets_Object = MibTableColumn
prvtStatSdpPri4Packets = _PrvtStatSdpPri4Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 22),
    _PrvtStatSdpPri4Packets_Type()
)
prvtStatSdpPri4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri4Packets.setStatus("current")
_PrvtStatSdpPri4Bytes_Type = Counter64
_PrvtStatSdpPri4Bytes_Object = MibTableColumn
prvtStatSdpPri4Bytes = _PrvtStatSdpPri4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 23),
    _PrvtStatSdpPri4Bytes_Type()
)
prvtStatSdpPri4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri4Bytes.setStatus("current")
_PrvtStatSdpPri5Packets_Type = Counter64
_PrvtStatSdpPri5Packets_Object = MibTableColumn
prvtStatSdpPri5Packets = _PrvtStatSdpPri5Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 24),
    _PrvtStatSdpPri5Packets_Type()
)
prvtStatSdpPri5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri5Packets.setStatus("current")
_PrvtStatSdpPri5Bytes_Type = Counter64
_PrvtStatSdpPri5Bytes_Object = MibTableColumn
prvtStatSdpPri5Bytes = _PrvtStatSdpPri5Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 25),
    _PrvtStatSdpPri5Bytes_Type()
)
prvtStatSdpPri5Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri5Bytes.setStatus("current")
_PrvtStatSdpPri6Packets_Type = Counter64
_PrvtStatSdpPri6Packets_Object = MibTableColumn
prvtStatSdpPri6Packets = _PrvtStatSdpPri6Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 26),
    _PrvtStatSdpPri6Packets_Type()
)
prvtStatSdpPri6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri6Packets.setStatus("current")
_PrvtStatSdpPri6Bytes_Type = Counter64
_PrvtStatSdpPri6Bytes_Object = MibTableColumn
prvtStatSdpPri6Bytes = _PrvtStatSdpPri6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 27),
    _PrvtStatSdpPri6Bytes_Type()
)
prvtStatSdpPri6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri6Bytes.setStatus("current")
_PrvtStatSdpPri7Packets_Type = Counter64
_PrvtStatSdpPri7Packets_Object = MibTableColumn
prvtStatSdpPri7Packets = _PrvtStatSdpPri7Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 28),
    _PrvtStatSdpPri7Packets_Type()
)
prvtStatSdpPri7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri7Packets.setStatus("current")
_PrvtStatSdpPri7Bytes_Type = Counter64
_PrvtStatSdpPri7Bytes_Object = MibTableColumn
prvtStatSdpPri7Bytes = _PrvtStatSdpPri7Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 29),
    _PrvtStatSdpPri7Bytes_Type()
)
prvtStatSdpPri7Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri7Bytes.setStatus("current")
_PrvtStatSdpPri0yPackets_Type = Counter64
_PrvtStatSdpPri0yPackets_Object = MibTableColumn
prvtStatSdpPri0yPackets = _PrvtStatSdpPri0yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 30),
    _PrvtStatSdpPri0yPackets_Type()
)
prvtStatSdpPri0yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri0yPackets.setStatus("current")
_PrvtStatSdpPri0yBytes_Type = Counter64
_PrvtStatSdpPri0yBytes_Object = MibTableColumn
prvtStatSdpPri0yBytes = _PrvtStatSdpPri0yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 31),
    _PrvtStatSdpPri0yBytes_Type()
)
prvtStatSdpPri0yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri0yBytes.setStatus("current")
_PrvtStatSdpPri1yPackets_Type = Counter64
_PrvtStatSdpPri1yPackets_Object = MibTableColumn
prvtStatSdpPri1yPackets = _PrvtStatSdpPri1yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 32),
    _PrvtStatSdpPri1yPackets_Type()
)
prvtStatSdpPri1yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri1yPackets.setStatus("current")
_PrvtStatSdpPri1yBytes_Type = Counter64
_PrvtStatSdpPri1yBytes_Object = MibTableColumn
prvtStatSdpPri1yBytes = _PrvtStatSdpPri1yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 33),
    _PrvtStatSdpPri1yBytes_Type()
)
prvtStatSdpPri1yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri1yBytes.setStatus("current")
_PrvtStatSdpPri2yPackets_Type = Counter64
_PrvtStatSdpPri2yPackets_Object = MibTableColumn
prvtStatSdpPri2yPackets = _PrvtStatSdpPri2yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 34),
    _PrvtStatSdpPri2yPackets_Type()
)
prvtStatSdpPri2yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri2yPackets.setStatus("current")
_PrvtStatSdpPri2yBytes_Type = Counter64
_PrvtStatSdpPri2yBytes_Object = MibTableColumn
prvtStatSdpPri2yBytes = _PrvtStatSdpPri2yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 35),
    _PrvtStatSdpPri2yBytes_Type()
)
prvtStatSdpPri2yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri2yBytes.setStatus("current")
_PrvtStatSdpPri3yPackets_Type = Counter64
_PrvtStatSdpPri3yPackets_Object = MibTableColumn
prvtStatSdpPri3yPackets = _PrvtStatSdpPri3yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 36),
    _PrvtStatSdpPri3yPackets_Type()
)
prvtStatSdpPri3yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri3yPackets.setStatus("current")
_PrvtStatSdpPri3yBytes_Type = Counter64
_PrvtStatSdpPri3yBytes_Object = MibTableColumn
prvtStatSdpPri3yBytes = _PrvtStatSdpPri3yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 37),
    _PrvtStatSdpPri3yBytes_Type()
)
prvtStatSdpPri3yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri3yBytes.setStatus("current")
_PrvtStatSdpPri4yPackets_Type = Counter64
_PrvtStatSdpPri4yPackets_Object = MibTableColumn
prvtStatSdpPri4yPackets = _PrvtStatSdpPri4yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 38),
    _PrvtStatSdpPri4yPackets_Type()
)
prvtStatSdpPri4yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri4yPackets.setStatus("current")
_PrvtStatSdpPri4yBytes_Type = Counter64
_PrvtStatSdpPri4yBytes_Object = MibTableColumn
prvtStatSdpPri4yBytes = _PrvtStatSdpPri4yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 39),
    _PrvtStatSdpPri4yBytes_Type()
)
prvtStatSdpPri4yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri4yBytes.setStatus("current")
_PrvtStatSdpPri5yPackets_Type = Counter64
_PrvtStatSdpPri5yPackets_Object = MibTableColumn
prvtStatSdpPri5yPackets = _PrvtStatSdpPri5yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 40),
    _PrvtStatSdpPri5yPackets_Type()
)
prvtStatSdpPri5yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri5yPackets.setStatus("current")
_PrvtStatSdpPri5yBytes_Type = Counter64
_PrvtStatSdpPri5yBytes_Object = MibTableColumn
prvtStatSdpPri5yBytes = _PrvtStatSdpPri5yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 41),
    _PrvtStatSdpPri5yBytes_Type()
)
prvtStatSdpPri5yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri5yBytes.setStatus("current")
_PrvtStatSdpPri6yPackets_Type = Counter64
_PrvtStatSdpPri6yPackets_Object = MibTableColumn
prvtStatSdpPri6yPackets = _PrvtStatSdpPri6yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 42),
    _PrvtStatSdpPri6yPackets_Type()
)
prvtStatSdpPri6yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri6yPackets.setStatus("current")
_PrvtStatSdpPri6yBytes_Type = Counter64
_PrvtStatSdpPri6yBytes_Object = MibTableColumn
prvtStatSdpPri6yBytes = _PrvtStatSdpPri6yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 43),
    _PrvtStatSdpPri6yBytes_Type()
)
prvtStatSdpPri6yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri6yBytes.setStatus("current")
_PrvtStatSdpPri7yPackets_Type = Counter64
_PrvtStatSdpPri7yPackets_Object = MibTableColumn
prvtStatSdpPri7yPackets = _PrvtStatSdpPri7yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 44),
    _PrvtStatSdpPri7yPackets_Type()
)
prvtStatSdpPri7yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri7yPackets.setStatus("current")
_PrvtStatSdpPri7yBytes_Type = Counter64
_PrvtStatSdpPri7yBytes_Object = MibTableColumn
prvtStatSdpPri7yBytes = _PrvtStatSdpPri7yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 45),
    _PrvtStatSdpPri7yBytes_Type()
)
prvtStatSdpPri7yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpPri7yBytes.setStatus("current")
_PrvtStatSdpEgPackets_Type = Counter64
_PrvtStatSdpEgPackets_Object = MibTableColumn
prvtStatSdpEgPackets = _PrvtStatSdpEgPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 46),
    _PrvtStatSdpEgPackets_Type()
)
prvtStatSdpEgPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPackets.setStatus("current")
_PrvtStatSdpEgBytes_Type = Counter64
_PrvtStatSdpEgBytes_Object = MibTableColumn
prvtStatSdpEgBytes = _PrvtStatSdpEgBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 47),
    _PrvtStatSdpEgBytes_Type()
)
prvtStatSdpEgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgBytes.setStatus("current")
_PrvtStatSdpEgUnicastPackets_Type = Counter64
_PrvtStatSdpEgUnicastPackets_Object = MibTableColumn
prvtStatSdpEgUnicastPackets = _PrvtStatSdpEgUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 48),
    _PrvtStatSdpEgUnicastPackets_Type()
)
prvtStatSdpEgUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgUnicastPackets.setStatus("current")
_PrvtStatSdpEgUnicastBytes_Type = Counter64
_PrvtStatSdpEgUnicastBytes_Object = MibTableColumn
prvtStatSdpEgUnicastBytes = _PrvtStatSdpEgUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 49),
    _PrvtStatSdpEgUnicastBytes_Type()
)
prvtStatSdpEgUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgUnicastBytes.setStatus("current")
_PrvtStatSdpEgMulticastPackets_Type = Counter64
_PrvtStatSdpEgMulticastPackets_Object = MibTableColumn
prvtStatSdpEgMulticastPackets = _PrvtStatSdpEgMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 50),
    _PrvtStatSdpEgMulticastPackets_Type()
)
prvtStatSdpEgMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgMulticastPackets.setStatus("current")
_PrvtStatSdpEgMulticastBytes_Type = Counter64
_PrvtStatSdpEgMulticastBytes_Object = MibTableColumn
prvtStatSdpEgMulticastBytes = _PrvtStatSdpEgMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 51),
    _PrvtStatSdpEgMulticastBytes_Type()
)
prvtStatSdpEgMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgMulticastBytes.setStatus("current")
_PrvtStatSdpEgBroadcastPackets_Type = Counter64
_PrvtStatSdpEgBroadcastPackets_Object = MibTableColumn
prvtStatSdpEgBroadcastPackets = _PrvtStatSdpEgBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 52),
    _PrvtStatSdpEgBroadcastPackets_Type()
)
prvtStatSdpEgBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgBroadcastPackets.setStatus("current")
_PrvtStatSdpEgBroadcastBytes_Type = Counter64
_PrvtStatSdpEgBroadcastBytes_Object = MibTableColumn
prvtStatSdpEgBroadcastBytes = _PrvtStatSdpEgBroadcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 53),
    _PrvtStatSdpEgBroadcastBytes_Type()
)
prvtStatSdpEgBroadcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgBroadcastBytes.setStatus("current")
_PrvtStatSdpEgPri0Packets_Type = Counter64
_PrvtStatSdpEgPri0Packets_Object = MibTableColumn
prvtStatSdpEgPri0Packets = _PrvtStatSdpEgPri0Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 54),
    _PrvtStatSdpEgPri0Packets_Type()
)
prvtStatSdpEgPri0Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri0Packets.setStatus("current")
_PrvtStatSdpEgPri0Bytes_Type = Counter64
_PrvtStatSdpEgPri0Bytes_Object = MibTableColumn
prvtStatSdpEgPri0Bytes = _PrvtStatSdpEgPri0Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 55),
    _PrvtStatSdpEgPri0Bytes_Type()
)
prvtStatSdpEgPri0Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri0Bytes.setStatus("current")
_PrvtStatSdpEgPri1Packets_Type = Counter64
_PrvtStatSdpEgPri1Packets_Object = MibTableColumn
prvtStatSdpEgPri1Packets = _PrvtStatSdpEgPri1Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 56),
    _PrvtStatSdpEgPri1Packets_Type()
)
prvtStatSdpEgPri1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri1Packets.setStatus("current")
_PrvtStatSdpEgPri1Bytes_Type = Counter64
_PrvtStatSdpEgPri1Bytes_Object = MibTableColumn
prvtStatSdpEgPri1Bytes = _PrvtStatSdpEgPri1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 57),
    _PrvtStatSdpEgPri1Bytes_Type()
)
prvtStatSdpEgPri1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri1Bytes.setStatus("current")
_PrvtStatSdpEgPri2Packets_Type = Counter64
_PrvtStatSdpEgPri2Packets_Object = MibTableColumn
prvtStatSdpEgPri2Packets = _PrvtStatSdpEgPri2Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 58),
    _PrvtStatSdpEgPri2Packets_Type()
)
prvtStatSdpEgPri2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri2Packets.setStatus("current")
_PrvtStatSdpEgPri2Bytes_Type = Counter64
_PrvtStatSdpEgPri2Bytes_Object = MibTableColumn
prvtStatSdpEgPri2Bytes = _PrvtStatSdpEgPri2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 59),
    _PrvtStatSdpEgPri2Bytes_Type()
)
prvtStatSdpEgPri2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri2Bytes.setStatus("current")
_PrvtStatSdpEgPri3Packets_Type = Counter64
_PrvtStatSdpEgPri3Packets_Object = MibTableColumn
prvtStatSdpEgPri3Packets = _PrvtStatSdpEgPri3Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 60),
    _PrvtStatSdpEgPri3Packets_Type()
)
prvtStatSdpEgPri3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri3Packets.setStatus("current")
_PrvtStatSdpEgPri3Bytes_Type = Counter64
_PrvtStatSdpEgPri3Bytes_Object = MibTableColumn
prvtStatSdpEgPri3Bytes = _PrvtStatSdpEgPri3Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 61),
    _PrvtStatSdpEgPri3Bytes_Type()
)
prvtStatSdpEgPri3Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri3Bytes.setStatus("current")
_PrvtStatSdpEgPri4Packets_Type = Counter64
_PrvtStatSdpEgPri4Packets_Object = MibTableColumn
prvtStatSdpEgPri4Packets = _PrvtStatSdpEgPri4Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 62),
    _PrvtStatSdpEgPri4Packets_Type()
)
prvtStatSdpEgPri4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri4Packets.setStatus("current")
_PrvtStatSdpEgPri4Bytes_Type = Counter64
_PrvtStatSdpEgPri4Bytes_Object = MibTableColumn
prvtStatSdpEgPri4Bytes = _PrvtStatSdpEgPri4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 63),
    _PrvtStatSdpEgPri4Bytes_Type()
)
prvtStatSdpEgPri4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri4Bytes.setStatus("current")
_PrvtStatSdpEgPri5Packets_Type = Counter64
_PrvtStatSdpEgPri5Packets_Object = MibTableColumn
prvtStatSdpEgPri5Packets = _PrvtStatSdpEgPri5Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 64),
    _PrvtStatSdpEgPri5Packets_Type()
)
prvtStatSdpEgPri5Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri5Packets.setStatus("current")
_PrvtStatSdpEgPri5Bytes_Type = Counter64
_PrvtStatSdpEgPri5Bytes_Object = MibTableColumn
prvtStatSdpEgPri5Bytes = _PrvtStatSdpEgPri5Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 65),
    _PrvtStatSdpEgPri5Bytes_Type()
)
prvtStatSdpEgPri5Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri5Bytes.setStatus("current")
_PrvtStatSdpEgPri6Packets_Type = Counter64
_PrvtStatSdpEgPri6Packets_Object = MibTableColumn
prvtStatSdpEgPri6Packets = _PrvtStatSdpEgPri6Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 66),
    _PrvtStatSdpEgPri6Packets_Type()
)
prvtStatSdpEgPri6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri6Packets.setStatus("current")
_PrvtStatSdpEgPri6Bytes_Type = Counter64
_PrvtStatSdpEgPri6Bytes_Object = MibTableColumn
prvtStatSdpEgPri6Bytes = _PrvtStatSdpEgPri6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 67),
    _PrvtStatSdpEgPri6Bytes_Type()
)
prvtStatSdpEgPri6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri6Bytes.setStatus("current")
_PrvtStatSdpEgPri7Packets_Type = Counter64
_PrvtStatSdpEgPri7Packets_Object = MibTableColumn
prvtStatSdpEgPri7Packets = _PrvtStatSdpEgPri7Packets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 68),
    _PrvtStatSdpEgPri7Packets_Type()
)
prvtStatSdpEgPri7Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri7Packets.setStatus("current")
_PrvtStatSdpEgPri7Bytes_Type = Counter64
_PrvtStatSdpEgPri7Bytes_Object = MibTableColumn
prvtStatSdpEgPri7Bytes = _PrvtStatSdpEgPri7Bytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 69),
    _PrvtStatSdpEgPri7Bytes_Type()
)
prvtStatSdpEgPri7Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri7Bytes.setStatus("current")
_PrvtStatSdpEgPri0yPackets_Type = Counter64
_PrvtStatSdpEgPri0yPackets_Object = MibTableColumn
prvtStatSdpEgPri0yPackets = _PrvtStatSdpEgPri0yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 70),
    _PrvtStatSdpEgPri0yPackets_Type()
)
prvtStatSdpEgPri0yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri0yPackets.setStatus("current")
_PrvtStatSdpEgPri0yBytes_Type = Counter64
_PrvtStatSdpEgPri0yBytes_Object = MibTableColumn
prvtStatSdpEgPri0yBytes = _PrvtStatSdpEgPri0yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 71),
    _PrvtStatSdpEgPri0yBytes_Type()
)
prvtStatSdpEgPri0yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri0yBytes.setStatus("current")
_PrvtStatSdpEgPri1yPackets_Type = Counter64
_PrvtStatSdpEgPri1yPackets_Object = MibTableColumn
prvtStatSdpEgPri1yPackets = _PrvtStatSdpEgPri1yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 72),
    _PrvtStatSdpEgPri1yPackets_Type()
)
prvtStatSdpEgPri1yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri1yPackets.setStatus("current")
_PrvtStatSdpEgPri1yBytes_Type = Counter64
_PrvtStatSdpEgPri1yBytes_Object = MibTableColumn
prvtStatSdpEgPri1yBytes = _PrvtStatSdpEgPri1yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 73),
    _PrvtStatSdpEgPri1yBytes_Type()
)
prvtStatSdpEgPri1yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri1yBytes.setStatus("current")
_PrvtStatSdpEgPri2yPackets_Type = Counter64
_PrvtStatSdpEgPri2yPackets_Object = MibTableColumn
prvtStatSdpEgPri2yPackets = _PrvtStatSdpEgPri2yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 74),
    _PrvtStatSdpEgPri2yPackets_Type()
)
prvtStatSdpEgPri2yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri2yPackets.setStatus("current")
_PrvtStatSdpEgPri2yBytes_Type = Counter64
_PrvtStatSdpEgPri2yBytes_Object = MibTableColumn
prvtStatSdpEgPri2yBytes = _PrvtStatSdpEgPri2yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 75),
    _PrvtStatSdpEgPri2yBytes_Type()
)
prvtStatSdpEgPri2yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri2yBytes.setStatus("current")
_PrvtStatSdpEgPri3yPackets_Type = Counter64
_PrvtStatSdpEgPri3yPackets_Object = MibTableColumn
prvtStatSdpEgPri3yPackets = _PrvtStatSdpEgPri3yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 76),
    _PrvtStatSdpEgPri3yPackets_Type()
)
prvtStatSdpEgPri3yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri3yPackets.setStatus("current")
_PrvtStatSdpEgPri3yBytes_Type = Counter64
_PrvtStatSdpEgPri3yBytes_Object = MibTableColumn
prvtStatSdpEgPri3yBytes = _PrvtStatSdpEgPri3yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 77),
    _PrvtStatSdpEgPri3yBytes_Type()
)
prvtStatSdpEgPri3yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri3yBytes.setStatus("current")
_PrvtStatSdpEgPri4yPackets_Type = Counter64
_PrvtStatSdpEgPri4yPackets_Object = MibTableColumn
prvtStatSdpEgPri4yPackets = _PrvtStatSdpEgPri4yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 78),
    _PrvtStatSdpEgPri4yPackets_Type()
)
prvtStatSdpEgPri4yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri4yPackets.setStatus("current")
_PrvtStatSdpEgPri4yBytes_Type = Counter64
_PrvtStatSdpEgPri4yBytes_Object = MibTableColumn
prvtStatSdpEgPri4yBytes = _PrvtStatSdpEgPri4yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 79),
    _PrvtStatSdpEgPri4yBytes_Type()
)
prvtStatSdpEgPri4yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri4yBytes.setStatus("current")
_PrvtStatSdpEgPri5yPackets_Type = Counter64
_PrvtStatSdpEgPri5yPackets_Object = MibTableColumn
prvtStatSdpEgPri5yPackets = _PrvtStatSdpEgPri5yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 80),
    _PrvtStatSdpEgPri5yPackets_Type()
)
prvtStatSdpEgPri5yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri5yPackets.setStatus("current")
_PrvtStatSdpEgPri5yBytes_Type = Counter64
_PrvtStatSdpEgPri5yBytes_Object = MibTableColumn
prvtStatSdpEgPri5yBytes = _PrvtStatSdpEgPri5yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 81),
    _PrvtStatSdpEgPri5yBytes_Type()
)
prvtStatSdpEgPri5yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri5yBytes.setStatus("current")
_PrvtStatSdpEgPri6yPackets_Type = Counter64
_PrvtStatSdpEgPri6yPackets_Object = MibTableColumn
prvtStatSdpEgPri6yPackets = _PrvtStatSdpEgPri6yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 82),
    _PrvtStatSdpEgPri6yPackets_Type()
)
prvtStatSdpEgPri6yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri6yPackets.setStatus("current")
_PrvtStatSdpEgPri6yBytes_Type = Counter64
_PrvtStatSdpEgPri6yBytes_Object = MibTableColumn
prvtStatSdpEgPri6yBytes = _PrvtStatSdpEgPri6yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 83),
    _PrvtStatSdpEgPri6yBytes_Type()
)
prvtStatSdpEgPri6yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri6yBytes.setStatus("current")
_PrvtStatSdpEgPri7yPackets_Type = Counter64
_PrvtStatSdpEgPri7yPackets_Object = MibTableColumn
prvtStatSdpEgPri7yPackets = _PrvtStatSdpEgPri7yPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 84),
    _PrvtStatSdpEgPri7yPackets_Type()
)
prvtStatSdpEgPri7yPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri7yPackets.setStatus("current")
_PrvtStatSdpEgPri7yBytes_Type = Counter64
_PrvtStatSdpEgPri7yBytes_Object = MibTableColumn
prvtStatSdpEgPri7yBytes = _PrvtStatSdpEgPri7yBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 181, 1, 4, 1, 85),
    _PrvtStatSdpEgPri7yBytes_Type()
)
prvtStatSdpEgPri7yBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatSdpEgPri7yBytes.setStatus("current")
sapEntry.registerAugmentions(
    ("PRVT-STATISTICS-MIB",
     "prvtStatSapEntry")
)
prvtStatSapEntry.setIndexNames(*sapEntry.getIndexNames())
sdpEntry.registerAugmentions(
    ("PRVT-STATISTICS-MIB",
     "prvtStatSdpEntry")
)
prvtStatSdpEntry.setIndexNames(*sdpEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-STATISTICS-MIB",
    **{"StatType": StatType,
       "prvtStatisticsMIB": prvtStatisticsMIB,
       "prvtStatObjects": prvtStatObjects,
       "prvtStatIngressPolicyTable": prvtStatIngressPolicyTable,
       "prvtStatIngressPolicyEntry": prvtStatIngressPolicyEntry,
       "prvtStatIngressPolicyName": prvtStatIngressPolicyName,
       "prvtStatIngressPolicyRowStatus": prvtStatIngressPolicyRowStatus,
       "prvtStatIngressPolicyDetailed": prvtStatIngressPolicyDetailed,
       "prvtStatIngressPolicyDescription": prvtStatIngressPolicyDescription,
       "prvtStatIngressPolicyFc": prvtStatIngressPolicyFc,
       "prvtStatIngressPolicyFcBwMeasurement": prvtStatIngressPolicyFcBwMeasurement,
       "prvtStatIngressPolicyColor": prvtStatIngressPolicyColor,
       "prvtStatIngressPolicyColorBwMeasurement": prvtStatIngressPolicyColorBwMeasurement,
       "prvtStatIngressPolicyUnicast": prvtStatIngressPolicyUnicast,
       "prvtStatIngressPolicyUnicastBwMeasurement": prvtStatIngressPolicyUnicastBwMeasurement,
       "prvtStatIngressPolicyBroadcast": prvtStatIngressPolicyBroadcast,
       "prvtStatIngressPolicyBroadcastBwMeasurement": prvtStatIngressPolicyBroadcastBwMeasurement,
       "prvtStatIngressPolicyMulticast": prvtStatIngressPolicyMulticast,
       "prvtStatIngressPolicyMulticastBwMeasurement": prvtStatIngressPolicyMulticastBwMeasurement,
       "prvtStatEgressPolicyTable": prvtStatEgressPolicyTable,
       "prvtStatEgressPolicyEntry": prvtStatEgressPolicyEntry,
       "prvtStatEgressPolicyName": prvtStatEgressPolicyName,
       "prvtStatEgressPolicyRowStatus": prvtStatEgressPolicyRowStatus,
       "prvtStatEgressPolicyDetailed": prvtStatEgressPolicyDetailed,
       "prvtStatEgressPolicyDescription": prvtStatEgressPolicyDescription,
       "prvtStatEgressPolicyFc": prvtStatEgressPolicyFc,
       "prvtStatEgressPolicyFcBwMeasurement": prvtStatEgressPolicyFcBwMeasurement,
       "prvtStatEgressPolicyColor": prvtStatEgressPolicyColor,
       "prvtStatEgressPolicyColorBwMeasurement": prvtStatEgressPolicyColorBwMeasurement,
       "prvtStatEgressPolicyDaType": prvtStatEgressPolicyDaType,
       "prvtStatEgressPolicyDaTypeBwMeasurement": prvtStatEgressPolicyDaTypeBwMeasurement,
       "prvtStatSapTable": prvtStatSapTable,
       "prvtStatSapEntry": prvtStatSapEntry,
       "prvtStatSapIngressPolicy": prvtStatSapIngressPolicy,
       "prvtStatSapEgressPolicy": prvtStatSapEgressPolicy,
       "prvtStatSapClear": prvtStatSapClear,
       "prvtStatSapInPackets": prvtStatSapInPackets,
       "prvtStatSapInBytes": prvtStatSapInBytes,
       "prvtStatSapDropPackets": prvtStatSapDropPackets,
       "prvtStatSapDropBytes": prvtStatSapDropBytes,
       "prvtStatSapUnicastPackets": prvtStatSapUnicastPackets,
       "prvtStatSapUnicastBytes": prvtStatSapUnicastBytes,
       "prvtStatSapMulticastPackets": prvtStatSapMulticastPackets,
       "prvtStatSapMulticastBytes": prvtStatSapMulticastBytes,
       "prvtStatSapBroadcastPackets": prvtStatSapBroadcastPackets,
       "prvtStatSapBroadcastBytes": prvtStatSapBroadcastBytes,
       "prvtStatSapPri0Packets": prvtStatSapPri0Packets,
       "prvtStatSapPri0Bytes": prvtStatSapPri0Bytes,
       "prvtStatSapPri1Packets": prvtStatSapPri1Packets,
       "prvtStatSapPri1Bytes": prvtStatSapPri1Bytes,
       "prvtStatSapPri2Packets": prvtStatSapPri2Packets,
       "prvtStatSapPri2Bytes": prvtStatSapPri2Bytes,
       "prvtStatSapPri3Packets": prvtStatSapPri3Packets,
       "prvtStatSapPri3Bytes": prvtStatSapPri3Bytes,
       "prvtStatSapPri4Packets": prvtStatSapPri4Packets,
       "prvtStatSapPri4Bytes": prvtStatSapPri4Bytes,
       "prvtStatSapPri5Packets": prvtStatSapPri5Packets,
       "prvtStatSapPri5Bytes": prvtStatSapPri5Bytes,
       "prvtStatSapPri6Packets": prvtStatSapPri6Packets,
       "prvtStatSapPri6Bytes": prvtStatSapPri6Bytes,
       "prvtStatSapPri7Packets": prvtStatSapPri7Packets,
       "prvtStatSapPri7Bytes": prvtStatSapPri7Bytes,
       "prvtStatSapPri0yPackets": prvtStatSapPri0yPackets,
       "prvtStatSapPri0yBytes": prvtStatSapPri0yBytes,
       "prvtStatSapPri1yPackets": prvtStatSapPri1yPackets,
       "prvtStatSapPri1yBytes": prvtStatSapPri1yBytes,
       "prvtStatSapPri2yPackets": prvtStatSapPri2yPackets,
       "prvtStatSapPri2yBytes": prvtStatSapPri2yBytes,
       "prvtStatSapPri3yPackets": prvtStatSapPri3yPackets,
       "prvtStatSapPri3yBytes": prvtStatSapPri3yBytes,
       "prvtStatSapPri4yPackets": prvtStatSapPri4yPackets,
       "prvtStatSapPri4yBytes": prvtStatSapPri4yBytes,
       "prvtStatSapPri5yPackets": prvtStatSapPri5yPackets,
       "prvtStatSapPri5yBytes": prvtStatSapPri5yBytes,
       "prvtStatSapPri6yPackets": prvtStatSapPri6yPackets,
       "prvtStatSapPri6yBytes": prvtStatSapPri6yBytes,
       "prvtStatSapPri7yPackets": prvtStatSapPri7yPackets,
       "prvtStatSapPri7yBytes": prvtStatSapPri7yBytes,
       "prvtStatSapEgPackets": prvtStatSapEgPackets,
       "prvtStatSapEgBytes": prvtStatSapEgBytes,
       "prvtStatSapEgUnicastPackets": prvtStatSapEgUnicastPackets,
       "prvtStatSapEgUnicastBytes": prvtStatSapEgUnicastBytes,
       "prvtStatSapEgMulticastPackets": prvtStatSapEgMulticastPackets,
       "prvtStatSapEgMulticastBytes": prvtStatSapEgMulticastBytes,
       "prvtStatSapEgBroadcastPackets": prvtStatSapEgBroadcastPackets,
       "prvtStatSapEgBroadcastBytes": prvtStatSapEgBroadcastBytes,
       "prvtStatSapEgPri0Packets": prvtStatSapEgPri0Packets,
       "prvtStatSapEgPri0Bytes": prvtStatSapEgPri0Bytes,
       "prvtStatSapEgPri1Packets": prvtStatSapEgPri1Packets,
       "prvtStatSapEgPri1Bytes": prvtStatSapEgPri1Bytes,
       "prvtStatSapEgPri2Packets": prvtStatSapEgPri2Packets,
       "prvtStatSapEgPri2Bytes": prvtStatSapEgPri2Bytes,
       "prvtStatSapEgPri3Packets": prvtStatSapEgPri3Packets,
       "prvtStatSapEgPri3Bytes": prvtStatSapEgPri3Bytes,
       "prvtStatSapEgPri4Packets": prvtStatSapEgPri4Packets,
       "prvtStatSapEgPri4Bytes": prvtStatSapEgPri4Bytes,
       "prvtStatSapEgPri5Packets": prvtStatSapEgPri5Packets,
       "prvtStatSapEgPri5Bytes": prvtStatSapEgPri5Bytes,
       "prvtStatSapEgPri6Packets": prvtStatSapEgPri6Packets,
       "prvtStatSapEgPri6Bytes": prvtStatSapEgPri6Bytes,
       "prvtStatSapEgPri7Packets": prvtStatSapEgPri7Packets,
       "prvtStatSapEgPri7Bytes": prvtStatSapEgPri7Bytes,
       "prvtStatSapEgPri0yPackets": prvtStatSapEgPri0yPackets,
       "prvtStatSapEgPri0yBytes": prvtStatSapEgPri0yBytes,
       "prvtStatSapEgPri1yPackets": prvtStatSapEgPri1yPackets,
       "prvtStatSapEgPri1yBytes": prvtStatSapEgPri1yBytes,
       "prvtStatSapEgPri2yPackets": prvtStatSapEgPri2yPackets,
       "prvtStatSapEgPri2yBytes": prvtStatSapEgPri2yBytes,
       "prvtStatSapEgPri3yPackets": prvtStatSapEgPri3yPackets,
       "prvtStatSapEgPri3yBytes": prvtStatSapEgPri3yBytes,
       "prvtStatSapEgPri4yPackets": prvtStatSapEgPri4yPackets,
       "prvtStatSapEgPri4yBytes": prvtStatSapEgPri4yBytes,
       "prvtStatSapEgPri5yPackets": prvtStatSapEgPri5yPackets,
       "prvtStatSapEgPri5yBytes": prvtStatSapEgPri5yBytes,
       "prvtStatSapEgPri6yPackets": prvtStatSapEgPri6yPackets,
       "prvtStatSapEgPri6yBytes": prvtStatSapEgPri6yBytes,
       "prvtStatSapEgPri7yPackets": prvtStatSapEgPri7yPackets,
       "prvtStatSapEgPri7yBytes": prvtStatSapEgPri7yBytes,
       "prvtStatSdpTable": prvtStatSdpTable,
       "prvtStatSdpEntry": prvtStatSdpEntry,
       "prvtStatSdpIngressPolicy": prvtStatSdpIngressPolicy,
       "prvtStatSdpEgressPolicy": prvtStatSdpEgressPolicy,
       "prvtStatSdpClear": prvtStatSdpClear,
       "prvtStatSdpInPackets": prvtStatSdpInPackets,
       "prvtStatSdpInBytes": prvtStatSdpInBytes,
       "prvtStatSdpDropPackets": prvtStatSdpDropPackets,
       "prvtStatSdpDropBytes": prvtStatSdpDropBytes,
       "prvtStatSdpUnicastPackets": prvtStatSdpUnicastPackets,
       "prvtStatSdpUnicastBytes": prvtStatSdpUnicastBytes,
       "prvtStatSdpMulticastPackets": prvtStatSdpMulticastPackets,
       "prvtStatSdpMulticastBytes": prvtStatSdpMulticastBytes,
       "prvtStatSdpBroadcastPackets": prvtStatSdpBroadcastPackets,
       "prvtStatSdpBroadcastBytes": prvtStatSdpBroadcastBytes,
       "prvtStatSdpPri0Packets": prvtStatSdpPri0Packets,
       "prvtStatSdpPri0Bytes": prvtStatSdpPri0Bytes,
       "prvtStatSdpPri1Packets": prvtStatSdpPri1Packets,
       "prvtStatSdpPri1Bytes": prvtStatSdpPri1Bytes,
       "prvtStatSdpPri2Packets": prvtStatSdpPri2Packets,
       "prvtStatSdpPri2Bytes": prvtStatSdpPri2Bytes,
       "prvtStatSdpPri3Packets": prvtStatSdpPri3Packets,
       "prvtStatSdpPri3Bytes": prvtStatSdpPri3Bytes,
       "prvtStatSdpPri4Packets": prvtStatSdpPri4Packets,
       "prvtStatSdpPri4Bytes": prvtStatSdpPri4Bytes,
       "prvtStatSdpPri5Packets": prvtStatSdpPri5Packets,
       "prvtStatSdpPri5Bytes": prvtStatSdpPri5Bytes,
       "prvtStatSdpPri6Packets": prvtStatSdpPri6Packets,
       "prvtStatSdpPri6Bytes": prvtStatSdpPri6Bytes,
       "prvtStatSdpPri7Packets": prvtStatSdpPri7Packets,
       "prvtStatSdpPri7Bytes": prvtStatSdpPri7Bytes,
       "prvtStatSdpPri0yPackets": prvtStatSdpPri0yPackets,
       "prvtStatSdpPri0yBytes": prvtStatSdpPri0yBytes,
       "prvtStatSdpPri1yPackets": prvtStatSdpPri1yPackets,
       "prvtStatSdpPri1yBytes": prvtStatSdpPri1yBytes,
       "prvtStatSdpPri2yPackets": prvtStatSdpPri2yPackets,
       "prvtStatSdpPri2yBytes": prvtStatSdpPri2yBytes,
       "prvtStatSdpPri3yPackets": prvtStatSdpPri3yPackets,
       "prvtStatSdpPri3yBytes": prvtStatSdpPri3yBytes,
       "prvtStatSdpPri4yPackets": prvtStatSdpPri4yPackets,
       "prvtStatSdpPri4yBytes": prvtStatSdpPri4yBytes,
       "prvtStatSdpPri5yPackets": prvtStatSdpPri5yPackets,
       "prvtStatSdpPri5yBytes": prvtStatSdpPri5yBytes,
       "prvtStatSdpPri6yPackets": prvtStatSdpPri6yPackets,
       "prvtStatSdpPri6yBytes": prvtStatSdpPri6yBytes,
       "prvtStatSdpPri7yPackets": prvtStatSdpPri7yPackets,
       "prvtStatSdpPri7yBytes": prvtStatSdpPri7yBytes,
       "prvtStatSdpEgPackets": prvtStatSdpEgPackets,
       "prvtStatSdpEgBytes": prvtStatSdpEgBytes,
       "prvtStatSdpEgUnicastPackets": prvtStatSdpEgUnicastPackets,
       "prvtStatSdpEgUnicastBytes": prvtStatSdpEgUnicastBytes,
       "prvtStatSdpEgMulticastPackets": prvtStatSdpEgMulticastPackets,
       "prvtStatSdpEgMulticastBytes": prvtStatSdpEgMulticastBytes,
       "prvtStatSdpEgBroadcastPackets": prvtStatSdpEgBroadcastPackets,
       "prvtStatSdpEgBroadcastBytes": prvtStatSdpEgBroadcastBytes,
       "prvtStatSdpEgPri0Packets": prvtStatSdpEgPri0Packets,
       "prvtStatSdpEgPri0Bytes": prvtStatSdpEgPri0Bytes,
       "prvtStatSdpEgPri1Packets": prvtStatSdpEgPri1Packets,
       "prvtStatSdpEgPri1Bytes": prvtStatSdpEgPri1Bytes,
       "prvtStatSdpEgPri2Packets": prvtStatSdpEgPri2Packets,
       "prvtStatSdpEgPri2Bytes": prvtStatSdpEgPri2Bytes,
       "prvtStatSdpEgPri3Packets": prvtStatSdpEgPri3Packets,
       "prvtStatSdpEgPri3Bytes": prvtStatSdpEgPri3Bytes,
       "prvtStatSdpEgPri4Packets": prvtStatSdpEgPri4Packets,
       "prvtStatSdpEgPri4Bytes": prvtStatSdpEgPri4Bytes,
       "prvtStatSdpEgPri5Packets": prvtStatSdpEgPri5Packets,
       "prvtStatSdpEgPri5Bytes": prvtStatSdpEgPri5Bytes,
       "prvtStatSdpEgPri6Packets": prvtStatSdpEgPri6Packets,
       "prvtStatSdpEgPri6Bytes": prvtStatSdpEgPri6Bytes,
       "prvtStatSdpEgPri7Packets": prvtStatSdpEgPri7Packets,
       "prvtStatSdpEgPri7Bytes": prvtStatSdpEgPri7Bytes,
       "prvtStatSdpEgPri0yPackets": prvtStatSdpEgPri0yPackets,
       "prvtStatSdpEgPri0yBytes": prvtStatSdpEgPri0yBytes,
       "prvtStatSdpEgPri1yPackets": prvtStatSdpEgPri1yPackets,
       "prvtStatSdpEgPri1yBytes": prvtStatSdpEgPri1yBytes,
       "prvtStatSdpEgPri2yPackets": prvtStatSdpEgPri2yPackets,
       "prvtStatSdpEgPri2yBytes": prvtStatSdpEgPri2yBytes,
       "prvtStatSdpEgPri3yPackets": prvtStatSdpEgPri3yPackets,
       "prvtStatSdpEgPri3yBytes": prvtStatSdpEgPri3yBytes,
       "prvtStatSdpEgPri4yPackets": prvtStatSdpEgPri4yPackets,
       "prvtStatSdpEgPri4yBytes": prvtStatSdpEgPri4yBytes,
       "prvtStatSdpEgPri5yPackets": prvtStatSdpEgPri5yPackets,
       "prvtStatSdpEgPri5yBytes": prvtStatSdpEgPri5yBytes,
       "prvtStatSdpEgPri6yPackets": prvtStatSdpEgPri6yPackets,
       "prvtStatSdpEgPri6yBytes": prvtStatSdpEgPri6yBytes,
       "prvtStatSdpEgPri7yPackets": prvtStatSdpEgPri7yPackets,
       "prvtStatSdpEgPri7yBytes": prvtStatSdpEgPri7yBytes}
)
