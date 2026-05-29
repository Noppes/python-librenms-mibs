# SNMP MIB module (AX-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-VLAN-MIB

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

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

axVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    axVlan.setRevisions(
        ("2014-07-15 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanIdOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_AxVlanBridge_ObjectIdentity = ObjectIdentity
axVlanBridge = _AxVlanBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1)
)
_AxVlanBridgeBase_ObjectIdentity = ObjectIdentity
axVlanBridgeBase = _AxVlanBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1)
)
_AxVBBaseTable_Object = MibTable
axVBBaseTable = _AxVBBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    axVBBaseTable.setStatus("current")
_AxVBBaseEntry_Object = MibTableRow
axVBBaseEntry = _AxVBBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1)
)
axVBBaseEntry.setIndexNames(
    (0, "AX-VLAN-MIB", "axVBBaseIndex"),
)
if mibBuilder.loadTexts:
    axVBBaseEntry.setStatus("current")
_AxVBBaseIndex_Type = VlanIndex
_AxVBBaseIndex_Object = MibTableColumn
axVBBaseIndex = _AxVBBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 1),
    _AxVBBaseIndex_Type()
)
axVBBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseIndex.setStatus("current")
_AxVBBaseBridgeAddress_Type = MacAddress
_AxVBBaseBridgeAddress_Object = MibTableColumn
axVBBaseBridgeAddress = _AxVBBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 2),
    _AxVBBaseBridgeAddress_Type()
)
axVBBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseBridgeAddress.setStatus("current")
_AxVBBaseNumPorts_Type = Integer32
_AxVBBaseNumPorts_Object = MibTableColumn
axVBBaseNumPorts = _AxVBBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 3),
    _AxVBBaseNumPorts_Type()
)
axVBBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseNumPorts.setStatus("current")


class _AxVBBaseType_Type(Integer32):
    """Custom type axVBBaseType based on Integer32"""
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
        *(("unknown", 1),
          ("transparentOnly", 2),
          ("sourcerouteOnly", 3),
          ("srt", 4))
    )


_AxVBBaseType_Type.__name__ = "Integer32"
_AxVBBaseType_Object = MibTableColumn
axVBBaseType = _AxVBBaseType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 4),
    _AxVBBaseType_Type()
)
axVBBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseType.setStatus("current")
_AxVBBaseVlanIfIndex_Type = Integer32
_AxVBBaseVlanIfIndex_Object = MibTableColumn
axVBBaseVlanIfIndex = _AxVBBaseVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 5),
    _AxVBBaseVlanIfIndex_Type()
)
axVBBaseVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseVlanIfIndex.setStatus("current")


class _AxVBBaseVlanType_Type(Integer32):
    """Custom type axVBBaseVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("macBased", 2),
          ("protocolBased", 3))
    )


_AxVBBaseVlanType_Type.__name__ = "Integer32"
_AxVBBaseVlanType_Object = MibTableColumn
axVBBaseVlanType = _AxVBBaseVlanType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 6),
    _AxVBBaseVlanType_Type()
)
axVBBaseVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseVlanType.setStatus("current")
_AxVBBaseVlanID_Type = VlanIdOrZero
_AxVBBaseVlanID_Object = MibTableColumn
axVBBaseVlanID = _AxVBBaseVlanID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 7),
    _AxVBBaseVlanID_Type()
)
axVBBaseVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseVlanID.setStatus("current")
_AxVBBaseAssociatedPrimaryVlan_Type = VlanIdOrZero
_AxVBBaseAssociatedPrimaryVlan_Object = MibTableColumn
axVBBaseAssociatedPrimaryVlan = _AxVBBaseAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 8),
    _AxVBBaseAssociatedPrimaryVlan_Type()
)
axVBBaseAssociatedPrimaryVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseAssociatedPrimaryVlan.setStatus("current")


class _AxVBBaseIfStatus_Type(Integer32):
    """Custom type axVBBaseIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AxVBBaseIfStatus_Type.__name__ = "Integer32"
_AxVBBaseIfStatus_Object = MibTableColumn
axVBBaseIfStatus = _AxVBBaseIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 9),
    _AxVBBaseIfStatus_Type()
)
axVBBaseIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseIfStatus.setStatus("current")
_AxVBBaseLastChange_Type = TimeTicks
_AxVBBaseLastChange_Object = MibTableColumn
axVBBaseLastChange = _AxVBBaseLastChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 10),
    _AxVBBaseLastChange_Type()
)
axVBBaseLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBaseLastChange.setStatus("current")


class _AxVBBasePrivateVlanType_Type(Integer32):
    """Custom type axVBBasePrivateVlanType based on Integer32"""
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
        *(("normal", 1),
          ("primary", 2),
          ("isolated", 3),
          ("community", 4))
    )


_AxVBBasePrivateVlanType_Type.__name__ = "Integer32"
_AxVBBasePrivateVlanType_Object = MibTableColumn
axVBBasePrivateVlanType = _AxVBBasePrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 1, 1, 11),
    _AxVBBasePrivateVlanType_Type()
)
axVBBasePrivateVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePrivateVlanType.setStatus("current")
_AxVBBasePortTable_Object = MibTable
axVBBasePortTable = _AxVBBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    axVBBasePortTable.setStatus("current")
_AxVBBasePortEntry_Object = MibTableRow
axVBBasePortEntry = _AxVBBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1)
)
axVBBasePortEntry.setIndexNames(
    (0, "AX-VLAN-MIB", "axVBBasePortIndex"),
    (0, "AX-VLAN-MIB", "axVBBasePort"),
)
if mibBuilder.loadTexts:
    axVBBasePortEntry.setStatus("current")
_AxVBBasePortIndex_Type = VlanIndex
_AxVBBasePortIndex_Object = MibTableColumn
axVBBasePortIndex = _AxVBBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1, 1),
    _AxVBBasePortIndex_Type()
)
axVBBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePortIndex.setStatus("current")


class _AxVBBasePort_Type(Integer32):
    """Custom type axVBBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AxVBBasePort_Type.__name__ = "Integer32"
_AxVBBasePort_Object = MibTableColumn
axVBBasePort = _AxVBBasePort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1, 2),
    _AxVBBasePort_Type()
)
axVBBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePort.setStatus("current")
_AxVBBasePortIfIndex_Type = Integer32
_AxVBBasePortIfIndex_Object = MibTableColumn
axVBBasePortIfIndex = _AxVBBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1, 3),
    _AxVBBasePortIfIndex_Type()
)
axVBBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePortIfIndex.setStatus("current")
_AxVBBasePortCircuit_Type = ObjectIdentifier
_AxVBBasePortCircuit_Object = MibTableColumn
axVBBasePortCircuit = _AxVBBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1, 4),
    _AxVBBasePortCircuit_Type()
)
axVBBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePortCircuit.setStatus("current")
_AxVBBasePortDelayExceededDiscards_Type = Counter32
_AxVBBasePortDelayExceededDiscards_Object = MibTableColumn
axVBBasePortDelayExceededDiscards = _AxVBBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1, 5),
    _AxVBBasePortDelayExceededDiscards_Type()
)
axVBBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePortDelayExceededDiscards.setStatus("current")
_AxVBBasePortMtuExceededDiscards_Type = Counter32
_AxVBBasePortMtuExceededDiscards_Object = MibTableColumn
axVBBasePortMtuExceededDiscards = _AxVBBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1, 6),
    _AxVBBasePortMtuExceededDiscards_Type()
)
axVBBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePortMtuExceededDiscards.setStatus("current")


class _AxVBBasePortState_Type(Integer32):
    """Custom type axVBBasePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6),
          ("fixForwarding", 7))
    )


_AxVBBasePortState_Type.__name__ = "Integer32"
_AxVBBasePortState_Object = MibTableColumn
axVBBasePortState = _AxVBBasePortState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1, 7),
    _AxVBBasePortState_Type()
)
axVBBasePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePortState.setStatus("current")


class _AxVBBasePortTaggedState_Type(Integer32):
    """Custom type axVBBasePortTaggedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untagged", 1),
          ("tagged", 2))
    )


_AxVBBasePortTaggedState_Type.__name__ = "Integer32"
_AxVBBasePortTaggedState_Object = MibTableColumn
axVBBasePortTaggedState = _AxVBBasePortTaggedState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1, 8),
    _AxVBBasePortTaggedState_Type()
)
axVBBasePortTaggedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePortTaggedState.setStatus("current")
_AxVBBasePortTranslatedTagID_Type = VlanIdOrZero
_AxVBBasePortTranslatedTagID_Object = MibTableColumn
axVBBasePortTranslatedTagID = _AxVBBasePortTranslatedTagID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 1, 2, 1, 9),
    _AxVBBasePortTranslatedTagID_Type()
)
axVBBasePortTranslatedTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBBasePortTranslatedTagID.setStatus("current")
_AxVlanBridgeTp_ObjectIdentity = ObjectIdentity
axVlanBridgeTp = _AxVlanBridgeTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4)
)
_AxVBTpTable_Object = MibTable
axVBTpTable = _AxVBTpTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    axVBTpTable.setStatus("current")
_AxVBTpEntry_Object = MibTableRow
axVBTpEntry = _AxVBTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 1, 1)
)
axVBTpEntry.setIndexNames(
    (0, "AX-VLAN-MIB", "axVBTpIndex"),
)
if mibBuilder.loadTexts:
    axVBTpEntry.setStatus("current")
_AxVBTpIndex_Type = VlanIndex
_AxVBTpIndex_Object = MibTableColumn
axVBTpIndex = _AxVBTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 1, 1, 1),
    _AxVBTpIndex_Type()
)
axVBTpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBTpIndex.setStatus("current")
_AxVBTpLearnedEntryDiscards_Type = Counter32
_AxVBTpLearnedEntryDiscards_Object = MibTableColumn
axVBTpLearnedEntryDiscards = _AxVBTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 1, 1, 2),
    _AxVBTpLearnedEntryDiscards_Type()
)
axVBTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBTpLearnedEntryDiscards.setStatus("current")
_AxVBTpAgingTime_Type = Integer32
_AxVBTpAgingTime_Object = MibTableColumn
axVBTpAgingTime = _AxVBTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 1, 1, 3),
    _AxVBTpAgingTime_Type()
)
axVBTpAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBTpAgingTime.setStatus("current")
_AxVBTpPortTable_Object = MibTable
axVBTpPortTable = _AxVBTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    axVBTpPortTable.setStatus("current")
_AxVBTpPortEntry_Object = MibTableRow
axVBTpPortEntry = _AxVBTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 3, 1)
)
axVBTpPortEntry.setIndexNames(
    (0, "AX-VLAN-MIB", "axVBTpPortIndex"),
    (0, "AX-VLAN-MIB", "axVBTpPort"),
)
if mibBuilder.loadTexts:
    axVBTpPortEntry.setStatus("current")
_AxVBTpPortIndex_Type = VlanIndex
_AxVBTpPortIndex_Object = MibTableColumn
axVBTpPortIndex = _AxVBTpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 3, 1, 1),
    _AxVBTpPortIndex_Type()
)
axVBTpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBTpPortIndex.setStatus("current")


class _AxVBTpPort_Type(Integer32):
    """Custom type axVBTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AxVBTpPort_Type.__name__ = "Integer32"
_AxVBTpPort_Object = MibTableColumn
axVBTpPort = _AxVBTpPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 3, 1, 2),
    _AxVBTpPort_Type()
)
axVBTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBTpPort.setStatus("current")
_AxVBTpPortMaxInfo_Type = Integer32
_AxVBTpPortMaxInfo_Object = MibTableColumn
axVBTpPortMaxInfo = _AxVBTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 3, 1, 3),
    _AxVBTpPortMaxInfo_Type()
)
axVBTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBTpPortMaxInfo.setStatus("current")
_AxVBTpPortInFrames_Type = Counter32
_AxVBTpPortInFrames_Object = MibTableColumn
axVBTpPortInFrames = _AxVBTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 3, 1, 4),
    _AxVBTpPortInFrames_Type()
)
axVBTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBTpPortInFrames.setStatus("current")
_AxVBTpPortOutFrames_Type = Counter32
_AxVBTpPortOutFrames_Object = MibTableColumn
axVBTpPortOutFrames = _AxVBTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 3, 1, 5),
    _AxVBTpPortOutFrames_Type()
)
axVBTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBTpPortOutFrames.setStatus("current")
_AxVBTpPortInDiscards_Type = Counter32
_AxVBTpPortInDiscards_Object = MibTableColumn
axVBTpPortInDiscards = _AxVBTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 4, 3, 1, 6),
    _AxVBTpPortInDiscards_Type()
)
axVBTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVBTpPortInDiscards.setStatus("current")
_AxVlanBridgeStatic_ObjectIdentity = ObjectIdentity
axVlanBridgeStatic = _AxVlanBridgeStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 5)
)
_AxVlanBridgeMaxVlans_Type = VlanIndex
_AxVlanBridgeMaxVlans_Object = MibScalar
axVlanBridgeMaxVlans = _AxVlanBridgeMaxVlans_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 101),
    _AxVlanBridgeMaxVlans_Type()
)
axVlanBridgeMaxVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVlanBridgeMaxVlans.setStatus("current")
_AxVlanBridgeMaxSpans_Type = VlanIndex
_AxVlanBridgeMaxSpans_Object = MibScalar
axVlanBridgeMaxSpans = _AxVlanBridgeMaxSpans_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1, 102),
    _AxVlanBridgeMaxSpans_Type()
)
axVlanBridgeMaxSpans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVlanBridgeMaxSpans.setStatus("current")
_AxVlanTagTranslation_ObjectIdentity = ObjectIdentity
axVlanTagTranslation = _AxVlanTagTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 10)
)
_AxVlanTagTranslationTable_Object = MibTable
axVlanTagTranslationTable = _AxVlanTagTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 10, 1)
)
if mibBuilder.loadTexts:
    axVlanTagTranslationTable.setStatus("current")
_AxVlanTagTranslationEntry_Object = MibTableRow
axVlanTagTranslationEntry = _AxVlanTagTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 10, 1, 1)
)
axVlanTagTranslationEntry.setIndexNames(
    (0, "AX-VLAN-MIB", "axVlanTagTranslationVlanId"),
    (0, "AX-VLAN-MIB", "axVlanTagTranslationTranslatedId"),
)
if mibBuilder.loadTexts:
    axVlanTagTranslationEntry.setStatus("current")


class _AxVlanTagTranslationVlanId_Type(Integer32):
    """Custom type axVlanTagTranslationVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AxVlanTagTranslationVlanId_Type.__name__ = "Integer32"
_AxVlanTagTranslationVlanId_Object = MibTableColumn
axVlanTagTranslationVlanId = _AxVlanTagTranslationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 10, 1, 1, 1),
    _AxVlanTagTranslationVlanId_Type()
)
axVlanTagTranslationVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axVlanTagTranslationVlanId.setStatus("current")


class _AxVlanTagTranslationTranslatedId_Type(Integer32):
    """Custom type axVlanTagTranslationTranslatedId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AxVlanTagTranslationTranslatedId_Type.__name__ = "Integer32"
_AxVlanTagTranslationTranslatedId_Object = MibTableColumn
axVlanTagTranslationTranslatedId = _AxVlanTagTranslationTranslatedId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 10, 1, 1, 2),
    _AxVlanTagTranslationTranslatedId_Type()
)
axVlanTagTranslationTranslatedId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axVlanTagTranslationTranslatedId.setStatus("current")
_AxVlanTagTranslationPorts_Type = PortList
_AxVlanTagTranslationPorts_Object = MibTableColumn
axVlanTagTranslationPorts = _AxVlanTagTranslationPorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 10, 1, 1, 3),
    _AxVlanTagTranslationPorts_Type()
)
axVlanTagTranslationPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVlanTagTranslationPorts.setStatus("current")
_AxVlanConformance_ObjectIdentity = ObjectIdentity
axVlanConformance = _AxVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1000)
)
_AxVlanCompliances_ObjectIdentity = ObjectIdentity
axVlanCompliances = _AxVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1000, 1)
)
_AxVlanGroups_ObjectIdentity = ObjectIdentity
axVlanGroups = _AxVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1000, 2)
)

# Managed Objects groups

axVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1000, 2, 1)
)
axVlanGroup.setObjects(
      *(("AX-VLAN-MIB", "axVBBaseBridgeAddress"),
        ("AX-VLAN-MIB", "axVBBaseNumPorts"),
        ("AX-VLAN-MIB", "axVBBaseType"),
        ("AX-VLAN-MIB", "axVBBaseVlanIfIndex"),
        ("AX-VLAN-MIB", "axVBBaseVlanType"),
        ("AX-VLAN-MIB", "axVBBaseVlanID"),
        ("AX-VLAN-MIB", "axVBBaseAssociatedPrimaryVlan"),
        ("AX-VLAN-MIB", "axVBBaseIfStatus"),
        ("AX-VLAN-MIB", "axVBBaseLastChange"),
        ("AX-VLAN-MIB", "axVBBasePrivateVlanType"),
        ("AX-VLAN-MIB", "axVBBasePortIfIndex"),
        ("AX-VLAN-MIB", "axVBBasePortCircuit"),
        ("AX-VLAN-MIB", "axVBBasePortDelayExceededDiscards"),
        ("AX-VLAN-MIB", "axVBBasePortMtuExceededDiscards"),
        ("AX-VLAN-MIB", "axVBBasePortState"),
        ("AX-VLAN-MIB", "axVBBasePortTaggedState"),
        ("AX-VLAN-MIB", "axVBBasePortTranslatedTagID"),
        ("AX-VLAN-MIB", "axVBTpLearnedEntryDiscards"),
        ("AX-VLAN-MIB", "axVBTpAgingTime"),
        ("AX-VLAN-MIB", "axVBTpPortMaxInfo"),
        ("AX-VLAN-MIB", "axVBTpPortInFrames"),
        ("AX-VLAN-MIB", "axVBTpPortOutFrames"),
        ("AX-VLAN-MIB", "axVBTpPortInDiscards"),
        ("AX-VLAN-MIB", "axVlanBridgeMaxVlans"),
        ("AX-VLAN-MIB", "axVlanBridgeMaxSpans"),
        ("AX-VLAN-MIB", "axVlanTagTranslationPorts"),
        ("AX-VLAN-MIB", "axVBBaseIndex"),
        ("AX-VLAN-MIB", "axVBBasePortIndex"),
        ("AX-VLAN-MIB", "axVBBasePort"),
        ("AX-VLAN-MIB", "axVBTpIndex"),
        ("AX-VLAN-MIB", "axVBTpPortIndex"),
        ("AX-VLAN-MIB", "axVBTpPort"))
)
if mibBuilder.loadTexts:
    axVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 6, 1000, 1, 1)
)
axVlanCompliance.setObjects(
    ("AX-VLAN-MIB", "axVlanGroup")
)
if mibBuilder.loadTexts:
    axVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-VLAN-MIB",
    **{"VlanIdOrZero": VlanIdOrZero,
       "axVlan": axVlan,
       "axVlanBridge": axVlanBridge,
       "axVlanBridgeBase": axVlanBridgeBase,
       "axVBBaseTable": axVBBaseTable,
       "axVBBaseEntry": axVBBaseEntry,
       "axVBBaseIndex": axVBBaseIndex,
       "axVBBaseBridgeAddress": axVBBaseBridgeAddress,
       "axVBBaseNumPorts": axVBBaseNumPorts,
       "axVBBaseType": axVBBaseType,
       "axVBBaseVlanIfIndex": axVBBaseVlanIfIndex,
       "axVBBaseVlanType": axVBBaseVlanType,
       "axVBBaseVlanID": axVBBaseVlanID,
       "axVBBaseAssociatedPrimaryVlan": axVBBaseAssociatedPrimaryVlan,
       "axVBBaseIfStatus": axVBBaseIfStatus,
       "axVBBaseLastChange": axVBBaseLastChange,
       "axVBBasePrivateVlanType": axVBBasePrivateVlanType,
       "axVBBasePortTable": axVBBasePortTable,
       "axVBBasePortEntry": axVBBasePortEntry,
       "axVBBasePortIndex": axVBBasePortIndex,
       "axVBBasePort": axVBBasePort,
       "axVBBasePortIfIndex": axVBBasePortIfIndex,
       "axVBBasePortCircuit": axVBBasePortCircuit,
       "axVBBasePortDelayExceededDiscards": axVBBasePortDelayExceededDiscards,
       "axVBBasePortMtuExceededDiscards": axVBBasePortMtuExceededDiscards,
       "axVBBasePortState": axVBBasePortState,
       "axVBBasePortTaggedState": axVBBasePortTaggedState,
       "axVBBasePortTranslatedTagID": axVBBasePortTranslatedTagID,
       "axVlanBridgeTp": axVlanBridgeTp,
       "axVBTpTable": axVBTpTable,
       "axVBTpEntry": axVBTpEntry,
       "axVBTpIndex": axVBTpIndex,
       "axVBTpLearnedEntryDiscards": axVBTpLearnedEntryDiscards,
       "axVBTpAgingTime": axVBTpAgingTime,
       "axVBTpPortTable": axVBTpPortTable,
       "axVBTpPortEntry": axVBTpPortEntry,
       "axVBTpPortIndex": axVBTpPortIndex,
       "axVBTpPort": axVBTpPort,
       "axVBTpPortMaxInfo": axVBTpPortMaxInfo,
       "axVBTpPortInFrames": axVBTpPortInFrames,
       "axVBTpPortOutFrames": axVBTpPortOutFrames,
       "axVBTpPortInDiscards": axVBTpPortInDiscards,
       "axVlanBridgeStatic": axVlanBridgeStatic,
       "axVlanBridgeMaxVlans": axVlanBridgeMaxVlans,
       "axVlanBridgeMaxSpans": axVlanBridgeMaxSpans,
       "axVlanTagTranslation": axVlanTagTranslation,
       "axVlanTagTranslationTable": axVlanTagTranslationTable,
       "axVlanTagTranslationEntry": axVlanTagTranslationEntry,
       "axVlanTagTranslationVlanId": axVlanTagTranslationVlanId,
       "axVlanTagTranslationTranslatedId": axVlanTagTranslationTranslatedId,
       "axVlanTagTranslationPorts": axVlanTagTranslationPorts,
       "axVlanConformance": axVlanConformance,
       "axVlanCompliances": axVlanCompliances,
       "axVlanCompliance": axVlanCompliance,
       "axVlanGroups": axVlanGroups,
       "axVlanGroup": axVlanGroup}
)
