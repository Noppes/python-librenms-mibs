# SNMP MIB module (PRVT-SPANNING-TREE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-SPANNING-TREE-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

prvtSpanningTreeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107)
)
if mibBuilder.loadTexts:
    prvtSpanningTreeMIB.setRevisions(
        ("2010-04-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtStInstIdTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class PrvtStInstIdExceptZeroTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class PrvtStPortIdTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class PrvtStBridgeIdTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d.1x:1x:1x:1x:1x:1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class PrvtStLearnModeTC(TextualConvention, Integer32):
    status = "current"
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
          ("standard", 1),
          ("temporary-disabled", 2))
    )



class PrvtStLinkTypeTC(TextualConvention, Integer32):
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
        *(("auto", 1),
          ("pointToPoint", 2),
          ("shared", 3))
    )



class PrvtStPortRoleTC(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("root", 2),
          ("designated", 3),
          ("alternate", 4),
          ("backup", 5),
          ("master", 6))
    )



class PrvtStPortStateTC(TextualConvention, Integer32):
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
        *(("forward", 1),
          ("block", 2),
          ("learn", 3))
    )



class PrvtStPortPriorityTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(176, 176),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(240, 240),
    )



class PrvtStBridgePriorityTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4096, 4096),
        ValueRangeConstraint(8192, 8192),
        ValueRangeConstraint(12288, 12288),
        ValueRangeConstraint(16384, 16384),
        ValueRangeConstraint(20480, 20480),
        ValueRangeConstraint(24576, 24576),
        ValueRangeConstraint(28672, 28672),
        ValueRangeConstraint(32768, 32768),
        ValueRangeConstraint(36864, 36864),
        ValueRangeConstraint(40960, 40960),
        ValueRangeConstraint(45056, 45056),
        ValueRangeConstraint(49152, 49152),
        ValueRangeConstraint(53248, 53248),
        ValueRangeConstraint(57344, 57344),
        ValueRangeConstraint(61440, 61440),
    )



# MIB Managed Objects in the order of their OIDs

_PrvtStNotifications_ObjectIdentity = ObjectIdentity
prvtStNotifications = _PrvtStNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0)
)
_PrvtStObjects_ObjectIdentity = ObjectIdentity
prvtStObjects = _PrvtStObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1)
)
_PrvtStCommon_ObjectIdentity = ObjectIdentity
prvtStCommon = _PrvtStCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1)
)


class _PrvtStProviderBridgeAddress_Type(Integer32):
    """Custom type prvtStProviderBridgeAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 0),
          ("dot1ad", 1))
    )


_PrvtStProviderBridgeAddress_Type.__name__ = "Integer32"
_PrvtStProviderBridgeAddress_Object = MibScalar
prvtStProviderBridgeAddress = _PrvtStProviderBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1),
    _PrvtStProviderBridgeAddress_Type()
)
prvtStProviderBridgeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStProviderBridgeAddress.setStatus("current")


class _PrvtStMaxAge_Type(Unsigned32):
    """Custom type prvtStMaxAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_PrvtStMaxAge_Type.__name__ = "Unsigned32"
_PrvtStMaxAge_Object = MibScalar
prvtStMaxAge = _PrvtStMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2),
    _PrvtStMaxAge_Type()
)
prvtStMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStMaxAge.setStatus("current")


class _PrvtStHelloTime_Type(Unsigned32):
    """Custom type prvtStHelloTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_PrvtStHelloTime_Type.__name__ = "Unsigned32"
_PrvtStHelloTime_Object = MibScalar
prvtStHelloTime = _PrvtStHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 3),
    _PrvtStHelloTime_Type()
)
prvtStHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStHelloTime.setStatus("current")


class _PrvtStForwardDelay_Type(Unsigned32):
    """Custom type prvtStForwardDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_PrvtStForwardDelay_Type.__name__ = "Unsigned32"
_PrvtStForwardDelay_Object = MibScalar
prvtStForwardDelay = _PrvtStForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 4),
    _PrvtStForwardDelay_Type()
)
prvtStForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStForwardDelay.setStatus("current")
_PrvtStPriority_Type = PrvtStBridgePriorityTC
_PrvtStPriority_Object = MibScalar
prvtStPriority = _PrvtStPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 5),
    _PrvtStPriority_Type()
)
prvtStPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStPriority.setStatus("current")
_PrvtStTimeSinceTopologyChange_Type = Unsigned32
_PrvtStTimeSinceTopologyChange_Object = MibScalar
prvtStTimeSinceTopologyChange = _PrvtStTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 6),
    _PrvtStTimeSinceTopologyChange_Type()
)
prvtStTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStTimeSinceTopologyChange.setStatus("current")
_PrvtStTopChanges_Type = Unsigned32
_PrvtStTopChanges_Object = MibScalar
prvtStTopChanges = _PrvtStTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 7),
    _PrvtStTopChanges_Type()
)
prvtStTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStTopChanges.setStatus("current")
_PrvtStPortTable_Object = MibTable
prvtStPortTable = _PrvtStPortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8)
)
if mibBuilder.loadTexts:
    prvtStPortTable.setStatus("current")
_PrvtStPortEntry_Object = MibTableRow
prvtStPortEntry = _PrvtStPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1)
)
prvtStPortEntry.setIndexNames(
    (0, "PRVT-SPANNING-TREE-MIB", "prvtStPortIfName"),
)
if mibBuilder.loadTexts:
    prvtStPortEntry.setStatus("current")
_PrvtStPortIfName_Type = OctetString
_PrvtStPortIfName_Object = MibTableColumn
prvtStPortIfName = _PrvtStPortIfName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 1),
    _PrvtStPortIfName_Type()
)
prvtStPortIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStPortIfName.setStatus("current")
_PrvtStPortRowStatus_Type = RowStatus
_PrvtStPortRowStatus_Object = MibTableColumn
prvtStPortRowStatus = _PrvtStPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 2),
    _PrvtStPortRowStatus_Type()
)
prvtStPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortRowStatus.setStatus("current")
_PrvtStPortBpduTx_Type = TruthValue
_PrvtStPortBpduTx_Object = MibTableColumn
prvtStPortBpduTx = _PrvtStPortBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 3),
    _PrvtStPortBpduTx_Type()
)
prvtStPortBpduTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortBpduTx.setStatus("current")
_PrvtStPortBpduRx_Type = TruthValue
_PrvtStPortBpduRx_Object = MibTableColumn
prvtStPortBpduRx = _PrvtStPortBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 4),
    _PrvtStPortBpduRx_Type()
)
prvtStPortBpduRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortBpduRx.setStatus("current")
_PrvtStPortDetectBpduLoss_Type = TruthValue
_PrvtStPortDetectBpduLoss_Object = MibTableColumn
prvtStPortDetectBpduLoss = _PrvtStPortDetectBpduLoss_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 5),
    _PrvtStPortDetectBpduLoss_Type()
)
prvtStPortDetectBpduLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortDetectBpduLoss.setStatus("current")
_PrvtStPortCiscoCompliant_Type = TruthValue
_PrvtStPortCiscoCompliant_Object = MibTableColumn
prvtStPortCiscoCompliant = _PrvtStPortCiscoCompliant_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 6),
    _PrvtStPortCiscoCompliant_Type()
)
prvtStPortCiscoCompliant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortCiscoCompliant.setStatus("current")
_PrvtStPortEdge_Type = TruthValue
_PrvtStPortEdge_Object = MibTableColumn
prvtStPortEdge = _PrvtStPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 7),
    _PrvtStPortEdge_Type()
)
prvtStPortEdge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortEdge.setStatus("current")
_PrvtStPortEdgeStatus_Type = TruthValue
_PrvtStPortEdgeStatus_Object = MibTableColumn
prvtStPortEdgeStatus = _PrvtStPortEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 8),
    _PrvtStPortEdgeStatus_Type()
)
prvtStPortEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStPortEdgeStatus.setStatus("current")
_PrvtStPortEdgeFlush_Type = TruthValue
_PrvtStPortEdgeFlush_Object = MibTableColumn
prvtStPortEdgeFlush = _PrvtStPortEdgeFlush_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 9),
    _PrvtStPortEdgeFlush_Type()
)
prvtStPortEdgeFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortEdgeFlush.setStatus("current")
_PrvtStPortLinkType_Type = PrvtStLinkTypeTC
_PrvtStPortLinkType_Object = MibTableColumn
prvtStPortLinkType = _PrvtStPortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 10),
    _PrvtStPortLinkType_Type()
)
prvtStPortLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortLinkType.setStatus("current")
_PrvtStPortLinkTypeStatus_Type = PrvtStLinkTypeTC
_PrvtStPortLinkTypeStatus_Object = MibTableColumn
prvtStPortLinkTypeStatus = _PrvtStPortLinkTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 11),
    _PrvtStPortLinkTypeStatus_Type()
)
prvtStPortLinkTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStPortLinkTypeStatus.setStatus("current")
_PrvtStPortRestrictedRoot_Type = TruthValue
_PrvtStPortRestrictedRoot_Object = MibTableColumn
prvtStPortRestrictedRoot = _PrvtStPortRestrictedRoot_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 12),
    _PrvtStPortRestrictedRoot_Type()
)
prvtStPortRestrictedRoot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortRestrictedRoot.setStatus("current")
_PrvtStPortRestrictedTcn_Type = TruthValue
_PrvtStPortRestrictedTcn_Object = MibTableColumn
prvtStPortRestrictedTcn = _PrvtStPortRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 13),
    _PrvtStPortRestrictedTcn_Type()
)
prvtStPortRestrictedTcn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortRestrictedTcn.setStatus("current")


class _PrvtStPortPathCost_Type(Unsigned32):
    """Custom type prvtStPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_PrvtStPortPathCost_Type.__name__ = "Unsigned32"
_PrvtStPortPathCost_Object = MibTableColumn
prvtStPortPathCost = _PrvtStPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 14),
    _PrvtStPortPathCost_Type()
)
prvtStPortPathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortPathCost.setStatus("current")
_PrvtStPortPriority_Type = PrvtStPortPriorityTC
_PrvtStPortPriority_Object = MibTableColumn
prvtStPortPriority = _PrvtStPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 15),
    _PrvtStPortPriority_Type()
)
prvtStPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortPriority.setStatus("current")
_PrvtStPortAdminStatus_Type = TruthValue
_PrvtStPortAdminStatus_Object = MibTableColumn
prvtStPortAdminStatus = _PrvtStPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 16),
    _PrvtStPortAdminStatus_Type()
)
prvtStPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStPortAdminStatus.setStatus("current")
_PrvtStPortState_Type = PrvtStPortStateTC
_PrvtStPortState_Object = MibTableColumn
prvtStPortState = _PrvtStPortState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 17),
    _PrvtStPortState_Type()
)
prvtStPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStPortState.setStatus("current")
_PrvtStPortRole_Type = PrvtStPortRoleTC
_PrvtStPortRole_Object = MibTableColumn
prvtStPortRole = _PrvtStPortRole_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 18),
    _PrvtStPortRole_Type()
)
prvtStPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStPortRole.setStatus("current")
_PrvtStPortDesPCost_Type = Unsigned32
_PrvtStPortDesPCost_Object = MibTableColumn
prvtStPortDesPCost = _PrvtStPortDesPCost_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 19),
    _PrvtStPortDesPCost_Type()
)
prvtStPortDesPCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStPortDesPCost.setStatus("current")
_PrvtStPortDesBridgeID_Type = OctetString
_PrvtStPortDesBridgeID_Object = MibTableColumn
prvtStPortDesBridgeID = _PrvtStPortDesBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 20),
    _PrvtStPortDesBridgeID_Type()
)
prvtStPortDesBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStPortDesBridgeID.setStatus("current")
_PrvtStPortDesPortID_Type = PrvtStPortIdTC
_PrvtStPortDesPortID_Object = MibTableColumn
prvtStPortDesPortID = _PrvtStPortDesPortID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 8, 1, 21),
    _PrvtStPortDesPortID_Type()
)
prvtStPortDesPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStPortDesPortID.setStatus("current")


class _PrvtStTxHoldCount_Type(Unsigned32):
    """Custom type prvtStTxHoldCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PrvtStTxHoldCount_Type.__name__ = "Unsigned32"
_PrvtStTxHoldCount_Object = MibScalar
prvtStTxHoldCount = _PrvtStTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 9),
    _PrvtStTxHoldCount_Type()
)
prvtStTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStTxHoldCount.setStatus("current")
_PrvtStLearnMode_Type = PrvtStLearnModeTC
_PrvtStLearnMode_Object = MibScalar
prvtStLearnMode = _PrvtStLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 10),
    _PrvtStLearnMode_Type()
)
prvtStLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStLearnMode.setStatus("current")
_PrvtStStp_ObjectIdentity = ObjectIdentity
prvtStStp = _PrvtStStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2)
)
_PrvtStStpProtocolDisabled_Type = TruthValue
_PrvtStStpProtocolDisabled_Object = MibScalar
prvtStStpProtocolDisabled = _PrvtStStpProtocolDisabled_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 1),
    _PrvtStStpProtocolDisabled_Type()
)
prvtStStpProtocolDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStStpProtocolDisabled.setStatus("current")
_PrvtStRstp_ObjectIdentity = ObjectIdentity
prvtStRstp = _PrvtStRstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3)
)
_PrvtStRstpProtocolDisabled_Type = TruthValue
_PrvtStRstpProtocolDisabled_Object = MibScalar
prvtStRstpProtocolDisabled = _PrvtStRstpProtocolDisabled_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 1),
    _PrvtStRstpProtocolDisabled_Type()
)
prvtStRstpProtocolDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStRstpProtocolDisabled.setStatus("current")
_PrvtStMstp_ObjectIdentity = ObjectIdentity
prvtStMstp = _PrvtStMstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4)
)
_PrvtStMstpProtocolDisabled_Type = TruthValue
_PrvtStMstpProtocolDisabled_Object = MibScalar
prvtStMstpProtocolDisabled = _PrvtStMstpProtocolDisabled_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1),
    _PrvtStMstpProtocolDisabled_Type()
)
prvtStMstpProtocolDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStMstpProtocolDisabled.setStatus("current")


class _PrvtStMstpRegionName_Type(OctetString):
    """Custom type prvtStMstpRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtStMstpRegionName_Type.__name__ = "OctetString"
_PrvtStMstpRegionName_Object = MibScalar
prvtStMstpRegionName = _PrvtStMstpRegionName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2),
    _PrvtStMstpRegionName_Type()
)
prvtStMstpRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStMstpRegionName.setStatus("current")


class _PrvtStMstpRegionRevision_Type(Unsigned32):
    """Custom type prvtStMstpRegionRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtStMstpRegionRevision_Type.__name__ = "Unsigned32"
_PrvtStMstpRegionRevision_Object = MibScalar
prvtStMstpRegionRevision = _PrvtStMstpRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 3),
    _PrvtStMstpRegionRevision_Type()
)
prvtStMstpRegionRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStMstpRegionRevision.setStatus("current")


class _PrvtStMstpMaxHops_Type(Unsigned32):
    """Custom type prvtStMstpMaxHops based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_PrvtStMstpMaxHops_Type.__name__ = "Unsigned32"
_PrvtStMstpMaxHops_Object = MibScalar
prvtStMstpMaxHops = _PrvtStMstpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 4),
    _PrvtStMstpMaxHops_Type()
)
prvtStMstpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStMstpMaxHops.setStatus("current")
_PrvtStMstpMigrationDelay_Type = Unsigned32
_PrvtStMstpMigrationDelay_Object = MibScalar
prvtStMstpMigrationDelay = _PrvtStMstpMigrationDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 6),
    _PrvtStMstpMigrationDelay_Type()
)
prvtStMstpMigrationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMstpMigrationDelay.setStatus("current")
_PrvtStMstpInstTable_Object = MibTable
prvtStMstpInstTable = _PrvtStMstpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 8)
)
if mibBuilder.loadTexts:
    prvtStMstpInstTable.setStatus("current")
_PrvtStMstpInstEntry_Object = MibTableRow
prvtStMstpInstEntry = _PrvtStMstpInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 8, 1)
)
prvtStMstpInstEntry.setIndexNames(
    (0, "PRVT-SPANNING-TREE-MIB", "prvtStMstpInstId"),
)
if mibBuilder.loadTexts:
    prvtStMstpInstEntry.setStatus("current")
_PrvtStMstpInstId_Type = PrvtStInstIdExceptZeroTC
_PrvtStMstpInstId_Object = MibTableColumn
prvtStMstpInstId = _PrvtStMstpInstId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 8, 1, 1),
    _PrvtStMstpInstId_Type()
)
prvtStMstpInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStMstpInstId.setStatus("current")
_PrvtStMstpInstRowStatus_Type = RowStatus
_PrvtStMstpInstRowStatus_Object = MibTableColumn
prvtStMstpInstRowStatus = _PrvtStMstpInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 8, 1, 2),
    _PrvtStMstpInstRowStatus_Type()
)
prvtStMstpInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStMstpInstRowStatus.setStatus("current")
_PrvtStMstpInstPriority_Type = PrvtStBridgePriorityTC
_PrvtStMstpInstPriority_Object = MibTableColumn
prvtStMstpInstPriority = _PrvtStMstpInstPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 8, 1, 3),
    _PrvtStMstpInstPriority_Type()
)
prvtStMstpInstPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStMstpInstPriority.setStatus("current")
_PrvtStMstpInstTimeSinceTopChng_Type = Unsigned32
_PrvtStMstpInstTimeSinceTopChng_Object = MibTableColumn
prvtStMstpInstTimeSinceTopChng = _PrvtStMstpInstTimeSinceTopChng_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 8, 1, 4),
    _PrvtStMstpInstTimeSinceTopChng_Type()
)
prvtStMstpInstTimeSinceTopChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMstpInstTimeSinceTopChng.setStatus("current")
_PrvtStMstpInstTopChanges_Type = Unsigned32
_PrvtStMstpInstTopChanges_Object = MibTableColumn
prvtStMstpInstTopChanges = _PrvtStMstpInstTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 8, 1, 5),
    _PrvtStMstpInstTopChanges_Type()
)
prvtStMstpInstTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMstpInstTopChanges.setStatus("current")
_PrvtStMstpInstStatTable_Object = MibTable
prvtStMstpInstStatTable = _PrvtStMstpInstStatTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 9)
)
if mibBuilder.loadTexts:
    prvtStMstpInstStatTable.setStatus("current")
_PrvtStMstpInstStatEntry_Object = MibTableRow
prvtStMstpInstStatEntry = _PrvtStMstpInstStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 9, 1)
)
prvtStMstpInstStatEntry.setIndexNames(
    (0, "PRVT-SPANNING-TREE-MIB", "prvtStMstpInstId"),
)
if mibBuilder.loadTexts:
    prvtStMstpInstStatEntry.setStatus("current")
_PrvtStMstpInstStatRRootID_Type = OctetString
_PrvtStMstpInstStatRRootID_Object = MibTableColumn
prvtStMstpInstStatRRootID = _PrvtStMstpInstStatRRootID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 9, 1, 2),
    _PrvtStMstpInstStatRRootID_Type()
)
prvtStMstpInstStatRRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMstpInstStatRRootID.setStatus("current")
_PrvtStMstpInstStatRemHopCount_Type = Unsigned32
_PrvtStMstpInstStatRemHopCount_Object = MibTableColumn
prvtStMstpInstStatRemHopCount = _PrvtStMstpInstStatRemHopCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 9, 1, 3),
    _PrvtStMstpInstStatRemHopCount_Type()
)
prvtStMstpInstStatRemHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMstpInstStatRemHopCount.setStatus("current")
_PrvtStMstpVlanPerInstTable_Object = MibTable
prvtStMstpVlanPerInstTable = _PrvtStMstpVlanPerInstTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 10)
)
if mibBuilder.loadTexts:
    prvtStMstpVlanPerInstTable.setStatus("current")
_PrvtStMstpVlanPerInstEntry_Object = MibTableRow
prvtStMstpVlanPerInstEntry = _PrvtStMstpVlanPerInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 10, 1)
)
prvtStMstpVlanPerInstEntry.setIndexNames(
    (0, "PRVT-SPANNING-TREE-MIB", "prvtStMstpVlanPerInstVlanId"),
)
if mibBuilder.loadTexts:
    prvtStMstpVlanPerInstEntry.setStatus("current")


class _PrvtStMstpVlanPerInstVlanId_Type(Unsigned32):
    """Custom type prvtStMstpVlanPerInstVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_PrvtStMstpVlanPerInstVlanId_Type.__name__ = "Unsigned32"
_PrvtStMstpVlanPerInstVlanId_Object = MibTableColumn
prvtStMstpVlanPerInstVlanId = _PrvtStMstpVlanPerInstVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 10, 1, 1),
    _PrvtStMstpVlanPerInstVlanId_Type()
)
prvtStMstpVlanPerInstVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStMstpVlanPerInstVlanId.setStatus("current")
_PrvtStMstpVlanPerInstRowStatus_Type = RowStatus
_PrvtStMstpVlanPerInstRowStatus_Object = MibTableColumn
prvtStMstpVlanPerInstRowStatus = _PrvtStMstpVlanPerInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 10, 1, 2),
    _PrvtStMstpVlanPerInstRowStatus_Type()
)
prvtStMstpVlanPerInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStMstpVlanPerInstRowStatus.setStatus("current")
_PrvtStMstpVlanPerInstMstId_Type = PrvtStInstIdTC
_PrvtStMstpVlanPerInstMstId_Object = MibTableColumn
prvtStMstpVlanPerInstMstId = _PrvtStMstpVlanPerInstMstId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 10, 1, 3),
    _PrvtStMstpVlanPerInstMstId_Type()
)
prvtStMstpVlanPerInstMstId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStMstpVlanPerInstMstId.setStatus("current")
_PrvtStMstpInstPortTable_Object = MibTable
prvtStMstpInstPortTable = _PrvtStMstpInstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12)
)
if mibBuilder.loadTexts:
    prvtStMstpInstPortTable.setStatus("current")
_PrvtStMstpInstPortEntry_Object = MibTableRow
prvtStMstpInstPortEntry = _PrvtStMstpInstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1)
)
prvtStMstpInstPortEntry.setIndexNames(
    (0, "PRVT-SPANNING-TREE-MIB", "prvtStPortIfName"),
    (0, "PRVT-SPANNING-TREE-MIB", "prvtStMInstPortInstId"),
)
if mibBuilder.loadTexts:
    prvtStMstpInstPortEntry.setStatus("current")
_PrvtStMInstPortInstId_Type = PrvtStInstIdExceptZeroTC
_PrvtStMInstPortInstId_Object = MibTableColumn
prvtStMInstPortInstId = _PrvtStMInstPortInstId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 2),
    _PrvtStMInstPortInstId_Type()
)
prvtStMInstPortInstId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStMInstPortInstId.setStatus("current")
_PrvtStMInstPortRowStatus_Type = RowStatus
_PrvtStMInstPortRowStatus_Object = MibTableColumn
prvtStMInstPortRowStatus = _PrvtStMInstPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 3),
    _PrvtStMInstPortRowStatus_Type()
)
prvtStMInstPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStMInstPortRowStatus.setStatus("current")


class _PrvtStMInstPortPathCost_Type(Unsigned32):
    """Custom type prvtStMInstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_PrvtStMInstPortPathCost_Type.__name__ = "Unsigned32"
_PrvtStMInstPortPathCost_Object = MibTableColumn
prvtStMInstPortPathCost = _PrvtStMInstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 4),
    _PrvtStMInstPortPathCost_Type()
)
prvtStMInstPortPathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStMInstPortPathCost.setStatus("current")
_PrvtStMInstPortPriority_Type = PrvtStPortPriorityTC
_PrvtStMInstPortPriority_Object = MibTableColumn
prvtStMInstPortPriority = _PrvtStMInstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 5),
    _PrvtStMInstPortPriority_Type()
)
prvtStMInstPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStMInstPortPriority.setStatus("current")
_PrvtStMInstPortAdminStatus_Type = TruthValue
_PrvtStMInstPortAdminStatus_Object = MibTableColumn
prvtStMInstPortAdminStatus = _PrvtStMInstPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 6),
    _PrvtStMInstPortAdminStatus_Type()
)
prvtStMInstPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStMInstPortAdminStatus.setStatus("current")
_PrvtStMInstPortState_Type = PrvtStPortStateTC
_PrvtStMInstPortState_Object = MibTableColumn
prvtStMInstPortState = _PrvtStMInstPortState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 7),
    _PrvtStMInstPortState_Type()
)
prvtStMInstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMInstPortState.setStatus("current")
_PrvtStMInstPortFwdTrans_Type = Unsigned32
_PrvtStMInstPortFwdTrans_Object = MibTableColumn
prvtStMInstPortFwdTrans = _PrvtStMInstPortFwdTrans_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 8),
    _PrvtStMInstPortFwdTrans_Type()
)
prvtStMInstPortFwdTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMInstPortFwdTrans.setStatus("current")
_PrvtStMInstPortStatRole_Type = PrvtStPortRoleTC
_PrvtStMInstPortStatRole_Object = MibTableColumn
prvtStMInstPortStatRole = _PrvtStMInstPortStatRole_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 9),
    _PrvtStMInstPortStatRole_Type()
)
prvtStMInstPortStatRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMInstPortStatRole.setStatus("current")
_PrvtStMInstPortDesPCost_Type = Unsigned32
_PrvtStMInstPortDesPCost_Object = MibTableColumn
prvtStMInstPortDesPCost = _PrvtStMInstPortDesPCost_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 10),
    _PrvtStMInstPortDesPCost_Type()
)
prvtStMInstPortDesPCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMInstPortDesPCost.setStatus("current")
_PrvtStMInstPortDesBridgeID_Type = OctetString
_PrvtStMInstPortDesBridgeID_Object = MibTableColumn
prvtStMInstPortDesBridgeID = _PrvtStMInstPortDesBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 11),
    _PrvtStMInstPortDesBridgeID_Type()
)
prvtStMInstPortDesBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMInstPortDesBridgeID.setStatus("current")
_PrvtStMInstPortDesPortID_Type = PrvtStPortIdTC
_PrvtStMInstPortDesPortID_Object = MibTableColumn
prvtStMInstPortDesPortID = _PrvtStMInstPortDesPortID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 12, 1, 12),
    _PrvtStMInstPortDesPortID_Type()
)
prvtStMInstPortDesPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStMInstPortDesPortID.setStatus("current")
_PrvtStFRing_ObjectIdentity = ObjectIdentity
prvtStFRing = _PrvtStFRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 5)
)
_PrvtStFRingProtocolDisabled_Type = TruthValue
_PrvtStFRingProtocolDisabled_Object = MibScalar
prvtStFRingProtocolDisabled = _PrvtStFRingProtocolDisabled_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 5, 1),
    _PrvtStFRingProtocolDisabled_Type()
)
prvtStFRingProtocolDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStFRingProtocolDisabled.setStatus("current")
_PrvtStFRingPrefLink_Type = OctetString
_PrvtStFRingPrefLink_Object = MibScalar
prvtStFRingPrefLink = _PrvtStFRingPrefLink_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 5, 2),
    _PrvtStFRingPrefLink_Type()
)
prvtStFRingPrefLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStFRingPrefLink.setStatus("current")
_PrvtStFRingInstTable_Object = MibTable
prvtStFRingInstTable = _PrvtStFRingInstTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 5, 3)
)
if mibBuilder.loadTexts:
    prvtStFRingInstTable.setStatus("current")
_PrvtStFRingInstEntry_Object = MibTableRow
prvtStFRingInstEntry = _PrvtStFRingInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 5, 3, 1)
)
prvtStFRingInstEntry.setIndexNames(
    (0, "PRVT-SPANNING-TREE-MIB", "prvtStFRingInstPort1"),
    (0, "PRVT-SPANNING-TREE-MIB", "prvtStFRingInstPort2"),
)
if mibBuilder.loadTexts:
    prvtStFRingInstEntry.setStatus("current")
_PrvtStFRingInstPort1_Type = OctetString
_PrvtStFRingInstPort1_Object = MibTableColumn
prvtStFRingInstPort1 = _PrvtStFRingInstPort1_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 5, 3, 1, 1),
    _PrvtStFRingInstPort1_Type()
)
prvtStFRingInstPort1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStFRingInstPort1.setStatus("current")
_PrvtStFRingInstPort2_Type = OctetString
_PrvtStFRingInstPort2_Object = MibTableColumn
prvtStFRingInstPort2 = _PrvtStFRingInstPort2_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 5, 3, 1, 2),
    _PrvtStFRingInstPort2_Type()
)
prvtStFRingInstPort2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStFRingInstPort2.setStatus("current")
_PrvtStFRingInstRowStatus_Type = RowStatus
_PrvtStFRingInstRowStatus_Object = MibTableColumn
prvtStFRingInstRowStatus = _PrvtStFRingInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 5, 3, 1, 3),
    _PrvtStFRingInstRowStatus_Type()
)
prvtStFRingInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStFRingInstRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

stTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 1)
)
if mibBuilder.loadTexts:
    stTopologyChange.setStatus(
        "current"
    )

stNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 2)
)
if mibBuilder.loadTexts:
    stNewRoot.setStatus(
        "current"
    )

mstTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 3)
)
mstTopologyChange.setObjects(
      *(("PRVT-SPANNING-TREE-MIB", "prvtStMInstPortStatRole"),
        ("PRVT-SPANNING-TREE-MIB", "prvtStTimeSinceTopologyChange"))
)
if mibBuilder.loadTexts:
    mstTopologyChange.setStatus(
        "current"
    )

mstNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 4)
)
mstNewRoot.setObjects(
    ("PRVT-SPANNING-TREE-MIB", "prvtStMInstPortStatRole")
)
if mibBuilder.loadTexts:
    mstNewRoot.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SPANNING-TREE-MIB",
    **{"PrvtStInstIdTC": PrvtStInstIdTC,
       "PrvtStInstIdExceptZeroTC": PrvtStInstIdExceptZeroTC,
       "PrvtStPortIdTC": PrvtStPortIdTC,
       "PrvtStBridgeIdTC": PrvtStBridgeIdTC,
       "PrvtStLearnModeTC": PrvtStLearnModeTC,
       "PrvtStLinkTypeTC": PrvtStLinkTypeTC,
       "PrvtStPortRoleTC": PrvtStPortRoleTC,
       "PrvtStPortStateTC": PrvtStPortStateTC,
       "PrvtStPortPriorityTC": PrvtStPortPriorityTC,
       "PrvtStBridgePriorityTC": PrvtStBridgePriorityTC,
       "prvtSpanningTreeMIB": prvtSpanningTreeMIB,
       "prvtStNotifications": prvtStNotifications,
       "stTopologyChange": stTopologyChange,
       "stNewRoot": stNewRoot,
       "mstTopologyChange": mstTopologyChange,
       "mstNewRoot": mstNewRoot,
       "prvtStObjects": prvtStObjects,
       "prvtStCommon": prvtStCommon,
       "prvtStProviderBridgeAddress": prvtStProviderBridgeAddress,
       "prvtStMaxAge": prvtStMaxAge,
       "prvtStHelloTime": prvtStHelloTime,
       "prvtStForwardDelay": prvtStForwardDelay,
       "prvtStPriority": prvtStPriority,
       "prvtStTimeSinceTopologyChange": prvtStTimeSinceTopologyChange,
       "prvtStTopChanges": prvtStTopChanges,
       "prvtStPortTable": prvtStPortTable,
       "prvtStPortEntry": prvtStPortEntry,
       "prvtStPortIfName": prvtStPortIfName,
       "prvtStPortRowStatus": prvtStPortRowStatus,
       "prvtStPortBpduTx": prvtStPortBpduTx,
       "prvtStPortBpduRx": prvtStPortBpduRx,
       "prvtStPortDetectBpduLoss": prvtStPortDetectBpduLoss,
       "prvtStPortCiscoCompliant": prvtStPortCiscoCompliant,
       "prvtStPortEdge": prvtStPortEdge,
       "prvtStPortEdgeStatus": prvtStPortEdgeStatus,
       "prvtStPortEdgeFlush": prvtStPortEdgeFlush,
       "prvtStPortLinkType": prvtStPortLinkType,
       "prvtStPortLinkTypeStatus": prvtStPortLinkTypeStatus,
       "prvtStPortRestrictedRoot": prvtStPortRestrictedRoot,
       "prvtStPortRestrictedTcn": prvtStPortRestrictedTcn,
       "prvtStPortPathCost": prvtStPortPathCost,
       "prvtStPortPriority": prvtStPortPriority,
       "prvtStPortAdminStatus": prvtStPortAdminStatus,
       "prvtStPortState": prvtStPortState,
       "prvtStPortRole": prvtStPortRole,
       "prvtStPortDesPCost": prvtStPortDesPCost,
       "prvtStPortDesBridgeID": prvtStPortDesBridgeID,
       "prvtStPortDesPortID": prvtStPortDesPortID,
       "prvtStTxHoldCount": prvtStTxHoldCount,
       "prvtStLearnMode": prvtStLearnMode,
       "prvtStStp": prvtStStp,
       "prvtStStpProtocolDisabled": prvtStStpProtocolDisabled,
       "prvtStRstp": prvtStRstp,
       "prvtStRstpProtocolDisabled": prvtStRstpProtocolDisabled,
       "prvtStMstp": prvtStMstp,
       "prvtStMstpProtocolDisabled": prvtStMstpProtocolDisabled,
       "prvtStMstpRegionName": prvtStMstpRegionName,
       "prvtStMstpRegionRevision": prvtStMstpRegionRevision,
       "prvtStMstpMaxHops": prvtStMstpMaxHops,
       "prvtStMstpMigrationDelay": prvtStMstpMigrationDelay,
       "prvtStMstpInstTable": prvtStMstpInstTable,
       "prvtStMstpInstEntry": prvtStMstpInstEntry,
       "prvtStMstpInstId": prvtStMstpInstId,
       "prvtStMstpInstRowStatus": prvtStMstpInstRowStatus,
       "prvtStMstpInstPriority": prvtStMstpInstPriority,
       "prvtStMstpInstTimeSinceTopChng": prvtStMstpInstTimeSinceTopChng,
       "prvtStMstpInstTopChanges": prvtStMstpInstTopChanges,
       "prvtStMstpInstStatTable": prvtStMstpInstStatTable,
       "prvtStMstpInstStatEntry": prvtStMstpInstStatEntry,
       "prvtStMstpInstStatRRootID": prvtStMstpInstStatRRootID,
       "prvtStMstpInstStatRemHopCount": prvtStMstpInstStatRemHopCount,
       "prvtStMstpVlanPerInstTable": prvtStMstpVlanPerInstTable,
       "prvtStMstpVlanPerInstEntry": prvtStMstpVlanPerInstEntry,
       "prvtStMstpVlanPerInstVlanId": prvtStMstpVlanPerInstVlanId,
       "prvtStMstpVlanPerInstRowStatus": prvtStMstpVlanPerInstRowStatus,
       "prvtStMstpVlanPerInstMstId": prvtStMstpVlanPerInstMstId,
       "prvtStMstpInstPortTable": prvtStMstpInstPortTable,
       "prvtStMstpInstPortEntry": prvtStMstpInstPortEntry,
       "prvtStMInstPortInstId": prvtStMInstPortInstId,
       "prvtStMInstPortRowStatus": prvtStMInstPortRowStatus,
       "prvtStMInstPortPathCost": prvtStMInstPortPathCost,
       "prvtStMInstPortPriority": prvtStMInstPortPriority,
       "prvtStMInstPortAdminStatus": prvtStMInstPortAdminStatus,
       "prvtStMInstPortState": prvtStMInstPortState,
       "prvtStMInstPortFwdTrans": prvtStMInstPortFwdTrans,
       "prvtStMInstPortStatRole": prvtStMInstPortStatRole,
       "prvtStMInstPortDesPCost": prvtStMInstPortDesPCost,
       "prvtStMInstPortDesBridgeID": prvtStMInstPortDesBridgeID,
       "prvtStMInstPortDesPortID": prvtStMInstPortDesPortID,
       "prvtStFRing": prvtStFRing,
       "prvtStFRingProtocolDisabled": prvtStFRingProtocolDisabled,
       "prvtStFRingPrefLink": prvtStFRingPrefLink,
       "prvtStFRingInstTable": prvtStFRingInstTable,
       "prvtStFRingInstEntry": prvtStFRingInstEntry,
       "prvtStFRingInstPort1": prvtStFRingInstPort1,
       "prvtStFRingInstPort2": prvtStFRingInstPort2,
       "prvtStFRingInstRowStatus": prvtStFRingInstRowStatus}
)
