# SNMP MIB module (AX4630S) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX4630S-MIB

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

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,
 Ipv6AddressPrefix,
 Ipv6IfIndex) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix",
    "Ipv6IfIndex")

(AreaID,
 BigMetric,
 DesignatedRouterPriority,
 HelloRange,
 Metric,
 PositiveInteger,
 RouterID,
 Status,
 UpToMaxAge) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "BigMetric",
    "DesignatedRouterPriority",
    "HelloRange",
    "Metric",
    "PositiveInteger",
    "RouterID",
    "Status",
    "UpToMaxAge")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class VlanIndex(Integer32):
    """Custom type VlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class VlanIdOrZero(Integer32):
    """Custom type VlanIdOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )





class VniIndex(Integer32):
    """Custom type VniIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alaxala_ObjectIdentity = ObjectIdentity
alaxala = _Alaxala_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839)
)
_AlaxalaProductId_ObjectIdentity = ObjectIdentity
alaxalaProductId = _AlaxalaProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1)
)
_AxSwitch_ObjectIdentity = ObjectIdentity
axSwitch = _AxSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2)
)
_Ax4630s_ObjectIdentity = ObjectIdentity
ax4630s = _Ax4630s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20)
)
_AlaxalaMib_ObjectIdentity = ObjectIdentity
alaxalaMib = _AlaxalaMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2)
)
_AxsEx_ObjectIdentity = ObjectIdentity
axsEx = _AxsEx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2)
)
_AxsMib_ObjectIdentity = ObjectIdentity
axsMib = _AxsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1)
)
_AxsStats_ObjectIdentity = ObjectIdentity
axsStats = _AxsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1)
)
_AxsIfStats_ObjectIdentity = ObjectIdentity
axsIfStats = _AxsIfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4)
)
_AxsIfStatsTable_Object = MibTable
axsIfStatsTable = _AxsIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    axsIfStatsTable.setStatus("mandatory")
_AxsIfStatsEntry_Object = MibTableRow
axsIfStatsEntry = _AxsIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1)
)
axsIfStatsEntry.setIndexNames(
    (0, "AX4630S", "axsIfStatsIndex"),
)
if mibBuilder.loadTexts:
    axsIfStatsEntry.setStatus("mandatory")
_AxsIfStatsIndex_Type = Integer32
_AxsIfStatsIndex_Object = MibTableColumn
axsIfStatsIndex = _AxsIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 1),
    _AxsIfStatsIndex_Type()
)
axsIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsIfStatsIndex.setStatus("mandatory")
_AxsIfStatsName_Type = DisplayString
_AxsIfStatsName_Object = MibTableColumn
axsIfStatsName = _AxsIfStatsName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 2),
    _AxsIfStatsName_Type()
)
axsIfStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsName.setStatus("mandatory")
_AxsIfStatsInMegaOctets_Type = Counter32
_AxsIfStatsInMegaOctets_Object = MibTableColumn
axsIfStatsInMegaOctets = _AxsIfStatsInMegaOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 3),
    _AxsIfStatsInMegaOctets_Type()
)
axsIfStatsInMegaOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsInMegaOctets.setStatus("mandatory")
_AxsIfStatsInUcastMegaPkts_Type = Counter32
_AxsIfStatsInUcastMegaPkts_Object = MibTableColumn
axsIfStatsInUcastMegaPkts = _AxsIfStatsInUcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 4),
    _AxsIfStatsInUcastMegaPkts_Type()
)
axsIfStatsInUcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsInUcastMegaPkts.setStatus("mandatory")
_AxsIfStatsInMulticastMegaPkts_Type = Counter32
_AxsIfStatsInMulticastMegaPkts_Object = MibTableColumn
axsIfStatsInMulticastMegaPkts = _AxsIfStatsInMulticastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 5),
    _AxsIfStatsInMulticastMegaPkts_Type()
)
axsIfStatsInMulticastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsInMulticastMegaPkts.setStatus("mandatory")
_AxsIfStatsInBroadcastMegaPkts_Type = Counter32
_AxsIfStatsInBroadcastMegaPkts_Object = MibTableColumn
axsIfStatsInBroadcastMegaPkts = _AxsIfStatsInBroadcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 6),
    _AxsIfStatsInBroadcastMegaPkts_Type()
)
axsIfStatsInBroadcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsInBroadcastMegaPkts.setStatus("mandatory")
_AxsIfStatsOutMegaOctets_Type = Counter32
_AxsIfStatsOutMegaOctets_Object = MibTableColumn
axsIfStatsOutMegaOctets = _AxsIfStatsOutMegaOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 7),
    _AxsIfStatsOutMegaOctets_Type()
)
axsIfStatsOutMegaOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsOutMegaOctets.setStatus("mandatory")
_AxsIfStatsOutUcastMegaPkts_Type = Counter32
_AxsIfStatsOutUcastMegaPkts_Object = MibTableColumn
axsIfStatsOutUcastMegaPkts = _AxsIfStatsOutUcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 8),
    _AxsIfStatsOutUcastMegaPkts_Type()
)
axsIfStatsOutUcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsOutUcastMegaPkts.setStatus("mandatory")
_AxsIfStatsOutMulticastMegaPkts_Type = Counter32
_AxsIfStatsOutMulticastMegaPkts_Object = MibTableColumn
axsIfStatsOutMulticastMegaPkts = _AxsIfStatsOutMulticastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 9),
    _AxsIfStatsOutMulticastMegaPkts_Type()
)
axsIfStatsOutMulticastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsOutMulticastMegaPkts.setStatus("mandatory")
_AxsIfStatsOutBroadcastMegaPkts_Type = Counter32
_AxsIfStatsOutBroadcastMegaPkts_Object = MibTableColumn
axsIfStatsOutBroadcastMegaPkts = _AxsIfStatsOutBroadcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 10),
    _AxsIfStatsOutBroadcastMegaPkts_Type()
)
axsIfStatsOutBroadcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsOutBroadcastMegaPkts.setStatus("mandatory")
_AxsIfStatsHighSpeed_Type = Counter32
_AxsIfStatsHighSpeed_Object = MibTableColumn
axsIfStatsHighSpeed = _AxsIfStatsHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 11),
    _AxsIfStatsHighSpeed_Type()
)
axsIfStatsHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsHighSpeed.setStatus("mandatory")
_AxsQoS_ObjectIdentity = ObjectIdentity
axsQoS = _AxsQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6)
)
_AxsEtherTxQoS_ObjectIdentity = ObjectIdentity
axsEtherTxQoS = _AxsEtherTxQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1)
)
_AxsEtherTxQoSStatsTable_Object = MibTable
axsEtherTxQoSStatsTable = _AxsEtherTxQoSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsTable.setStatus("mandatory")
_AxsEtherTxQoSStatsEntry_Object = MibTableRow
axsEtherTxQoSStatsEntry = _AxsEtherTxQoSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1)
)
axsEtherTxQoSStatsEntry.setIndexNames(
    (0, "AX4630S", "axsEtherTxQoSStatsIndex"),
)
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsEntry.setStatus("mandatory")
_AxsEtherTxQoSStatsIndex_Type = Integer32
_AxsEtherTxQoSStatsIndex_Object = MibTableColumn
axsEtherTxQoSStatsIndex = _AxsEtherTxQoSStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 1),
    _AxsEtherTxQoSStatsIndex_Type()
)
axsEtherTxQoSStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsIndex.setStatus("mandatory")
_AxsEtherTxQoSStatsMaxQnum_Type = Integer32
_AxsEtherTxQoSStatsMaxQnum_Object = MibTableColumn
axsEtherTxQoSStatsMaxQnum = _AxsEtherTxQoSStatsMaxQnum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 2),
    _AxsEtherTxQoSStatsMaxQnum_Type()
)
axsEtherTxQoSStatsMaxQnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsMaxQnum.setStatus("mandatory")
_AxsEtherTxQoSStatsLimitQlen_Type = Integer32
_AxsEtherTxQoSStatsLimitQlen_Object = MibTableColumn
axsEtherTxQoSStatsLimitQlen = _AxsEtherTxQoSStatsLimitQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 3),
    _AxsEtherTxQoSStatsLimitQlen_Type()
)
axsEtherTxQoSStatsLimitQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsLimitQlen.setStatus("mandatory")
_AxsEtherTxQoSStatsTotalOutFrames_Type = Counter32
_AxsEtherTxQoSStatsTotalOutFrames_Object = MibTableColumn
axsEtherTxQoSStatsTotalOutFrames = _AxsEtherTxQoSStatsTotalOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 4),
    _AxsEtherTxQoSStatsTotalOutFrames_Type()
)
axsEtherTxQoSStatsTotalOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsTotalOutFrames.setStatus("mandatory")
_AxsEtherTxQoSStatsTotalOutBytesHigh_Type = Counter32
_AxsEtherTxQoSStatsTotalOutBytesHigh_Object = MibTableColumn
axsEtherTxQoSStatsTotalOutBytesHigh = _AxsEtherTxQoSStatsTotalOutBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 5),
    _AxsEtherTxQoSStatsTotalOutBytesHigh_Type()
)
axsEtherTxQoSStatsTotalOutBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsTotalOutBytesHigh.setStatus("mandatory")
_AxsEtherTxQoSStatsTotalOutBytesLow_Type = Counter32
_AxsEtherTxQoSStatsTotalOutBytesLow_Object = MibTableColumn
axsEtherTxQoSStatsTotalOutBytesLow = _AxsEtherTxQoSStatsTotalOutBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 6),
    _AxsEtherTxQoSStatsTotalOutBytesLow_Type()
)
axsEtherTxQoSStatsTotalOutBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsTotalOutBytesLow.setStatus("mandatory")
_AxsEtherTxQoSStatsTotalDiscardFrames_Type = Counter32
_AxsEtherTxQoSStatsTotalDiscardFrames_Object = MibTableColumn
axsEtherTxQoSStatsTotalDiscardFrames = _AxsEtherTxQoSStatsTotalDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 7),
    _AxsEtherTxQoSStatsTotalDiscardFrames_Type()
)
axsEtherTxQoSStatsTotalDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsTotalDiscardFrames.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueTable_Object = MibTable
axsEtherTxQoSStatsQueueTable = _AxsEtherTxQoSStatsQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueTable.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueEntry_Object = MibTableRow
axsEtherTxQoSStatsQueueEntry = _AxsEtherTxQoSStatsQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1)
)
axsEtherTxQoSStatsQueueEntry.setIndexNames(
    (0, "AX4630S", "axsEtherTxQoSStatsQueueIndex"),
    (0, "AX4630S", "axsEtherTxQoSStatsQueueQueIndex"),
)
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueEntry.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueIndex_Type = Integer32
_AxsEtherTxQoSStatsQueueIndex_Object = MibTableColumn
axsEtherTxQoSStatsQueueIndex = _AxsEtherTxQoSStatsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 1),
    _AxsEtherTxQoSStatsQueueIndex_Type()
)
axsEtherTxQoSStatsQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueIndex.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueQueIndex_Type = Integer32
_AxsEtherTxQoSStatsQueueQueIndex_Object = MibTableColumn
axsEtherTxQoSStatsQueueQueIndex = _AxsEtherTxQoSStatsQueueQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 2),
    _AxsEtherTxQoSStatsQueueQueIndex_Type()
)
axsEtherTxQoSStatsQueueQueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueQueIndex.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueQlen_Type = Integer32
_AxsEtherTxQoSStatsQueueQlen_Object = MibTableColumn
axsEtherTxQoSStatsQueueQlen = _AxsEtherTxQoSStatsQueueQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 3),
    _AxsEtherTxQoSStatsQueueQlen_Type()
)
axsEtherTxQoSStatsQueueQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueQlen.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueMaxQlen_Type = Integer32
_AxsEtherTxQoSStatsQueueMaxQlen_Object = MibTableColumn
axsEtherTxQoSStatsQueueMaxQlen = _AxsEtherTxQoSStatsQueueMaxQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 4),
    _AxsEtherTxQoSStatsQueueMaxQlen_Type()
)
axsEtherTxQoSStatsQueueMaxQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueMaxQlen.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueDiscardFramesClass1_Type = Counter64
_AxsEtherTxQoSStatsQueueDiscardFramesClass1_Object = MibTableColumn
axsEtherTxQoSStatsQueueDiscardFramesClass1 = _AxsEtherTxQoSStatsQueueDiscardFramesClass1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 5),
    _AxsEtherTxQoSStatsQueueDiscardFramesClass1_Type()
)
axsEtherTxQoSStatsQueueDiscardFramesClass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueDiscardFramesClass1.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueDiscardFramesClass2_Type = Counter64
_AxsEtherTxQoSStatsQueueDiscardFramesClass2_Object = MibTableColumn
axsEtherTxQoSStatsQueueDiscardFramesClass2 = _AxsEtherTxQoSStatsQueueDiscardFramesClass2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 6),
    _AxsEtherTxQoSStatsQueueDiscardFramesClass2_Type()
)
axsEtherTxQoSStatsQueueDiscardFramesClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueDiscardFramesClass2.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueDiscardFramesClass3_Type = Counter64
_AxsEtherTxQoSStatsQueueDiscardFramesClass3_Object = MibTableColumn
axsEtherTxQoSStatsQueueDiscardFramesClass3 = _AxsEtherTxQoSStatsQueueDiscardFramesClass3_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 7),
    _AxsEtherTxQoSStatsQueueDiscardFramesClass3_Type()
)
axsEtherTxQoSStatsQueueDiscardFramesClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueDiscardFramesClass3.setStatus("mandatory")
_AxsEtherTxQoSStatsQueueDiscardFramesClass4_Type = Counter64
_AxsEtherTxQoSStatsQueueDiscardFramesClass4_Object = MibTableColumn
axsEtherTxQoSStatsQueueDiscardFramesClass4 = _AxsEtherTxQoSStatsQueueDiscardFramesClass4_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 8),
    _AxsEtherTxQoSStatsQueueDiscardFramesClass4_Type()
)
axsEtherTxQoSStatsQueueDiscardFramesClass4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueDiscardFramesClass4.setStatus("mandatory")
_AxsEthShaper_ObjectIdentity = ObjectIdentity
axsEthShaper = _AxsEthShaper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 4)
)
_AxsEthShaperAgQue_ObjectIdentity = ObjectIdentity
axsEthShaperAgQue = _AxsEthShaperAgQue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 5)
)
_AxsToCpuQoS_ObjectIdentity = ObjectIdentity
axsToCpuQoS = _AxsToCpuQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11)
)
_AxsToCpuQoSStatsTable_Object = MibTable
axsToCpuQoSStatsTable = _AxsToCpuQoSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 1)
)
if mibBuilder.loadTexts:
    axsToCpuQoSStatsTable.setStatus("mandatory")
_AxsToCpuQoSStatsEntry_Object = MibTableRow
axsToCpuQoSStatsEntry = _AxsToCpuQoSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 1, 1)
)
axsToCpuQoSStatsEntry.setIndexNames(
    (0, "AX4630S", "axsToCpuQoSStatsIndex"),
)
if mibBuilder.loadTexts:
    axsToCpuQoSStatsEntry.setStatus("mandatory")
_AxsToCpuQoSStatsIndex_Type = Integer32
_AxsToCpuQoSStatsIndex_Object = MibTableColumn
axsToCpuQoSStatsIndex = _AxsToCpuQoSStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 1, 1, 1),
    _AxsToCpuQoSStatsIndex_Type()
)
axsToCpuQoSStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsIndex.setStatus("mandatory")
_AxsToCpuQoSStatsMaxQnum_Type = Integer32
_AxsToCpuQoSStatsMaxQnum_Object = MibTableColumn
axsToCpuQoSStatsMaxQnum = _AxsToCpuQoSStatsMaxQnum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 1, 1, 2),
    _AxsToCpuQoSStatsMaxQnum_Type()
)
axsToCpuQoSStatsMaxQnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsMaxQnum.setStatus("mandatory")
_AxsToCpuQoSStatsLimitQlen_Type = Integer32
_AxsToCpuQoSStatsLimitQlen_Object = MibTableColumn
axsToCpuQoSStatsLimitQlen = _AxsToCpuQoSStatsLimitQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 1, 1, 3),
    _AxsToCpuQoSStatsLimitQlen_Type()
)
axsToCpuQoSStatsLimitQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsLimitQlen.setStatus("mandatory")
_AxsToCpuQoSStatsTotalOutFrames_Type = Counter32
_AxsToCpuQoSStatsTotalOutFrames_Object = MibTableColumn
axsToCpuQoSStatsTotalOutFrames = _AxsToCpuQoSStatsTotalOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 1, 1, 4),
    _AxsToCpuQoSStatsTotalOutFrames_Type()
)
axsToCpuQoSStatsTotalOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsTotalOutFrames.setStatus("mandatory")
_AxsToCpuQoSStatsTotalOutBytesHigh_Type = Counter32
_AxsToCpuQoSStatsTotalOutBytesHigh_Object = MibTableColumn
axsToCpuQoSStatsTotalOutBytesHigh = _AxsToCpuQoSStatsTotalOutBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 1, 1, 5),
    _AxsToCpuQoSStatsTotalOutBytesHigh_Type()
)
axsToCpuQoSStatsTotalOutBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsTotalOutBytesHigh.setStatus("mandatory")
_AxsToCpuQoSStatsTotalOutBytesLow_Type = Counter32
_AxsToCpuQoSStatsTotalOutBytesLow_Object = MibTableColumn
axsToCpuQoSStatsTotalOutBytesLow = _AxsToCpuQoSStatsTotalOutBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 1, 1, 6),
    _AxsToCpuQoSStatsTotalOutBytesLow_Type()
)
axsToCpuQoSStatsTotalOutBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsTotalOutBytesLow.setStatus("mandatory")
_AxsToCpuQoSStatsTotalDiscardFrames_Type = Counter32
_AxsToCpuQoSStatsTotalDiscardFrames_Object = MibTableColumn
axsToCpuQoSStatsTotalDiscardFrames = _AxsToCpuQoSStatsTotalDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 1, 1, 7),
    _AxsToCpuQoSStatsTotalDiscardFrames_Type()
)
axsToCpuQoSStatsTotalDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsTotalDiscardFrames.setStatus("mandatory")
_AxsToCpuQoSStatsQueueTable_Object = MibTable
axsToCpuQoSStatsQueueTable = _AxsToCpuQoSStatsQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2)
)
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueTable.setStatus("mandatory")
_AxsToCpuQoSStatsQueueEntry_Object = MibTableRow
axsToCpuQoSStatsQueueEntry = _AxsToCpuQoSStatsQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2, 1)
)
axsToCpuQoSStatsQueueEntry.setIndexNames(
    (0, "AX4630S", "axsToCpuQoSStatsQueueIndex"),
    (0, "AX4630S", "axsToCpuQoSStatsQueueQueIndex"),
)
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueEntry.setStatus("mandatory")
_AxsToCpuQoSStatsQueueIndex_Type = Integer32
_AxsToCpuQoSStatsQueueIndex_Object = MibTableColumn
axsToCpuQoSStatsQueueIndex = _AxsToCpuQoSStatsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2, 1, 1),
    _AxsToCpuQoSStatsQueueIndex_Type()
)
axsToCpuQoSStatsQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueIndex.setStatus("mandatory")
_AxsToCpuQoSStatsQueueQueIndex_Type = Integer32
_AxsToCpuQoSStatsQueueQueIndex_Object = MibTableColumn
axsToCpuQoSStatsQueueQueIndex = _AxsToCpuQoSStatsQueueQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2, 1, 2),
    _AxsToCpuQoSStatsQueueQueIndex_Type()
)
axsToCpuQoSStatsQueueQueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueQueIndex.setStatus("mandatory")
_AxsToCpuQoSStatsQueueQlen_Type = Integer32
_AxsToCpuQoSStatsQueueQlen_Object = MibTableColumn
axsToCpuQoSStatsQueueQlen = _AxsToCpuQoSStatsQueueQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2, 1, 3),
    _AxsToCpuQoSStatsQueueQlen_Type()
)
axsToCpuQoSStatsQueueQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueQlen.setStatus("mandatory")
_AxsToCpuQoSStatsQueueMaxQlen_Type = Integer32
_AxsToCpuQoSStatsQueueMaxQlen_Object = MibTableColumn
axsToCpuQoSStatsQueueMaxQlen = _AxsToCpuQoSStatsQueueMaxQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2, 1, 4),
    _AxsToCpuQoSStatsQueueMaxQlen_Type()
)
axsToCpuQoSStatsQueueMaxQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueMaxQlen.setStatus("mandatory")
_AxsToCpuQoSStatsQueueDiscardFramesClass1_Type = Counter64
_AxsToCpuQoSStatsQueueDiscardFramesClass1_Object = MibTableColumn
axsToCpuQoSStatsQueueDiscardFramesClass1 = _AxsToCpuQoSStatsQueueDiscardFramesClass1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2, 1, 5),
    _AxsToCpuQoSStatsQueueDiscardFramesClass1_Type()
)
axsToCpuQoSStatsQueueDiscardFramesClass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueDiscardFramesClass1.setStatus("mandatory")
_AxsToCpuQoSStatsQueueDiscardFramesClass2_Type = Counter64
_AxsToCpuQoSStatsQueueDiscardFramesClass2_Object = MibTableColumn
axsToCpuQoSStatsQueueDiscardFramesClass2 = _AxsToCpuQoSStatsQueueDiscardFramesClass2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2, 1, 6),
    _AxsToCpuQoSStatsQueueDiscardFramesClass2_Type()
)
axsToCpuQoSStatsQueueDiscardFramesClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueDiscardFramesClass2.setStatus("mandatory")
_AxsToCpuQoSStatsQueueDiscardFramesClass3_Type = Counter64
_AxsToCpuQoSStatsQueueDiscardFramesClass3_Object = MibTableColumn
axsToCpuQoSStatsQueueDiscardFramesClass3 = _AxsToCpuQoSStatsQueueDiscardFramesClass3_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2, 1, 7),
    _AxsToCpuQoSStatsQueueDiscardFramesClass3_Type()
)
axsToCpuQoSStatsQueueDiscardFramesClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueDiscardFramesClass3.setStatus("mandatory")
_AxsToCpuQoSStatsQueueDiscardFramesClass4_Type = Counter64
_AxsToCpuQoSStatsQueueDiscardFramesClass4_Object = MibTableColumn
axsToCpuQoSStatsQueueDiscardFramesClass4 = _AxsToCpuQoSStatsQueueDiscardFramesClass4_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 11, 2, 1, 8),
    _AxsToCpuQoSStatsQueueDiscardFramesClass4_Type()
)
axsToCpuQoSStatsQueueDiscardFramesClass4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsToCpuQoSStatsQueueDiscardFramesClass4.setStatus("mandatory")
_AxsDHCP_ObjectIdentity = ObjectIdentity
axsDHCP = _AxsDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 10)
)
_AxsDHCPAddrValue_Type = Integer32
_AxsDHCPAddrValue_Object = MibScalar
axsDHCPAddrValue = _AxsDHCPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 10, 1),
    _AxsDHCPAddrValue_Type()
)
axsDHCPAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsDHCPAddrValue.setStatus("mandatory")
_AxsDHCPFreeAddrValue_Type = Integer32
_AxsDHCPFreeAddrValue_Object = MibScalar
axsDHCPFreeAddrValue = _AxsDHCPFreeAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 10, 2),
    _AxsDHCPFreeAddrValue_Type()
)
axsDHCPFreeAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsDHCPFreeAddrValue.setStatus("mandatory")
_AxsGsrp_ObjectIdentity = ObjectIdentity
axsGsrp = _AxsGsrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4)
)
_AxsGsrpGroupTable_Object = MibTable
axsGsrpGroupTable = _AxsGsrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    axsGsrpGroupTable.setStatus("mandatory")
_AxsGsrpGroupEntry_Object = MibTableRow
axsGsrpGroupEntry = _AxsGsrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1)
)
axsGsrpGroupEntry.setIndexNames(
    (0, "AX4630S", "axsGsrpGroupId"),
)
if mibBuilder.loadTexts:
    axsGsrpGroupEntry.setStatus("mandatory")
_AxsGsrpGroupId_Type = Integer32
_AxsGsrpGroupId_Object = MibTableColumn
axsGsrpGroupId = _AxsGsrpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 1),
    _AxsGsrpGroupId_Type()
)
axsGsrpGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpGroupId.setStatus("mandatory")
_AxsGsrpGroupRowStatus_Type = RowStatus
_AxsGsrpGroupRowStatus_Object = MibTableColumn
axsGsrpGroupRowStatus = _AxsGsrpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 2),
    _AxsGsrpGroupRowStatus_Type()
)
axsGsrpGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpGroupRowStatus.setStatus("mandatory")
_AxsGsrpMacAddress_Type = MacAddress
_AxsGsrpMacAddress_Object = MibTableColumn
axsGsrpMacAddress = _AxsGsrpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 3),
    _AxsGsrpMacAddress_Type()
)
axsGsrpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpMacAddress.setStatus("mandatory")
_AxsGsrpAdvertiseHoldTime_Type = Integer32
_AxsGsrpAdvertiseHoldTime_Object = MibTableColumn
axsGsrpAdvertiseHoldTime = _AxsGsrpAdvertiseHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 4),
    _AxsGsrpAdvertiseHoldTime_Type()
)
axsGsrpAdvertiseHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpAdvertiseHoldTime.setStatus("mandatory")
_AxsGsrpAdvertiseInterval_Type = Integer32
_AxsGsrpAdvertiseInterval_Object = MibTableColumn
axsGsrpAdvertiseInterval = _AxsGsrpAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 5),
    _AxsGsrpAdvertiseInterval_Type()
)
axsGsrpAdvertiseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpAdvertiseInterval.setStatus("mandatory")


class _AxsGsrpSelectionPattern_Type(Integer32):
    """Custom type axsGsrpSelectionPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ports-Priority-MAC", 1),
          ("priority-Ports-MAC", 2))
    )


_AxsGsrpSelectionPattern_Type.__name__ = "Integer32"
_AxsGsrpSelectionPattern_Object = MibTableColumn
axsGsrpSelectionPattern = _AxsGsrpSelectionPattern_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 6),
    _AxsGsrpSelectionPattern_Type()
)
axsGsrpSelectionPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpSelectionPattern.setStatus("mandatory")


class _AxsGsrpLayer3Redundancy_Type(Integer32):
    """Custom type axsGsrpLayer3Redundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AxsGsrpLayer3Redundancy_Type.__name__ = "Integer32"
_AxsGsrpLayer3Redundancy_Object = MibTableColumn
axsGsrpLayer3Redundancy = _AxsGsrpLayer3Redundancy_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 7),
    _AxsGsrpLayer3Redundancy_Type()
)
axsGsrpLayer3Redundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpLayer3Redundancy.setStatus("mandatory")
_AxsGsrpVlanGroupTable_Object = MibTable
axsGsrpVlanGroupTable = _AxsGsrpVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    axsGsrpVlanGroupTable.setStatus("mandatory")
_AxsGsrpVlanGroupEntry_Object = MibTableRow
axsGsrpVlanGroupEntry = _AxsGsrpVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1)
)
axsGsrpVlanGroupEntry.setIndexNames(
    (0, "AX4630S", "axsGsrpGroupId"),
    (0, "AX4630S", "axsGsrpVlanGroupId"),
)
if mibBuilder.loadTexts:
    axsGsrpVlanGroupEntry.setStatus("mandatory")
_AxsGsrpVlanGroupId_Type = Integer32
_AxsGsrpVlanGroupId_Object = MibTableColumn
axsGsrpVlanGroupId = _AxsGsrpVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 1),
    _AxsGsrpVlanGroupId_Type()
)
axsGsrpVlanGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpVlanGroupId.setStatus("mandatory")
_AxsGsrpVlanGroupRowStatus_Type = RowStatus
_AxsGsrpVlanGroupRowStatus_Object = MibTableColumn
axsGsrpVlanGroupRowStatus = _AxsGsrpVlanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 2),
    _AxsGsrpVlanGroupRowStatus_Type()
)
axsGsrpVlanGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpVlanGroupRowStatus.setStatus("mandatory")


class _AxsGsrpState_Type(Integer32):
    """Custom type axsGsrpState based on Integer32"""
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
        *(("backUp", 1),
          ("backUp-Waiting", 2),
          ("master", 3),
          ("backUp-No-Neighbor", 4),
          ("backUp-Lock", 5))
    )


_AxsGsrpState_Type.__name__ = "Integer32"
_AxsGsrpState_Object = MibTableColumn
axsGsrpState = _AxsGsrpState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 3),
    _AxsGsrpState_Type()
)
axsGsrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpState.setStatus("mandatory")
_AxsGsrpPriority_Type = Integer32
_AxsGsrpPriority_Object = MibTableColumn
axsGsrpPriority = _AxsGsrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 4),
    _AxsGsrpPriority_Type()
)
axsGsrpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpPriority.setStatus("mandatory")
_AxsGsrpActivePorts_Type = Integer32
_AxsGsrpActivePorts_Object = MibTableColumn
axsGsrpActivePorts = _AxsGsrpActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 5),
    _AxsGsrpActivePorts_Type()
)
axsGsrpActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpActivePorts.setStatus("mandatory")
_AxsGsrpTransitionToMasterCounts_Type = Integer32
_AxsGsrpTransitionToMasterCounts_Object = MibTableColumn
axsGsrpTransitionToMasterCounts = _AxsGsrpTransitionToMasterCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 6),
    _AxsGsrpTransitionToMasterCounts_Type()
)
axsGsrpTransitionToMasterCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpTransitionToMasterCounts.setStatus("mandatory")
_AxsGsrpTransitionFromMasterCounts_Type = Integer32
_AxsGsrpTransitionFromMasterCounts_Object = MibTableColumn
axsGsrpTransitionFromMasterCounts = _AxsGsrpTransitionFromMasterCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 7),
    _AxsGsrpTransitionFromMasterCounts_Type()
)
axsGsrpTransitionFromMasterCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpTransitionFromMasterCounts.setStatus("mandatory")
_AxsGsrpLastTransitionTime_Type = TimeStamp
_AxsGsrpLastTransitionTime_Object = MibTableColumn
axsGsrpLastTransitionTime = _AxsGsrpLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 8),
    _AxsGsrpLastTransitionTime_Type()
)
axsGsrpLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpLastTransitionTime.setStatus("mandatory")
_AxsGsrpVirtualMacAddress_Type = MacAddress
_AxsGsrpVirtualMacAddress_Object = MibTableColumn
axsGsrpVirtualMacAddress = _AxsGsrpVirtualMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 9),
    _AxsGsrpVirtualMacAddress_Type()
)
axsGsrpVirtualMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpVirtualMacAddress.setStatus("mandatory")
_AxsGsrpNeighborGroupTable_Object = MibTable
axsGsrpNeighborGroupTable = _AxsGsrpNeighborGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    axsGsrpNeighborGroupTable.setStatus("mandatory")
_AxsGsrpNeighborGroupEntry_Object = MibTableRow
axsGsrpNeighborGroupEntry = _AxsGsrpNeighborGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1)
)
axsGsrpNeighborGroupEntry.setIndexNames(
    (0, "AX4630S", "axsGsrpNeighborGroupId"),
    (0, "AX4630S", "axsGsrpNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    axsGsrpNeighborGroupEntry.setStatus("mandatory")
_AxsGsrpNeighborGroupId_Type = Integer32
_AxsGsrpNeighborGroupId_Object = MibTableColumn
axsGsrpNeighborGroupId = _AxsGsrpNeighborGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1, 1),
    _AxsGsrpNeighborGroupId_Type()
)
axsGsrpNeighborGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpNeighborGroupId.setStatus("mandatory")
_AxsGsrpNeighborMacAddress_Type = MacAddress
_AxsGsrpNeighborMacAddress_Object = MibTableColumn
axsGsrpNeighborMacAddress = _AxsGsrpNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1, 2),
    _AxsGsrpNeighborMacAddress_Type()
)
axsGsrpNeighborMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpNeighborMacAddress.setStatus("mandatory")
_AxsGsrpNeighborAdvertiseHoldTime_Type = Integer32
_AxsGsrpNeighborAdvertiseHoldTime_Object = MibTableColumn
axsGsrpNeighborAdvertiseHoldTime = _AxsGsrpNeighborAdvertiseHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1, 3),
    _AxsGsrpNeighborAdvertiseHoldTime_Type()
)
axsGsrpNeighborAdvertiseHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpNeighborAdvertiseHoldTime.setStatus("mandatory")
_AxsGsrpNeighborAdvertiseInterval_Type = Integer32
_AxsGsrpNeighborAdvertiseInterval_Object = MibTableColumn
axsGsrpNeighborAdvertiseInterval = _AxsGsrpNeighborAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1, 4),
    _AxsGsrpNeighborAdvertiseInterval_Type()
)
axsGsrpNeighborAdvertiseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpNeighborAdvertiseInterval.setStatus("mandatory")


class _AxsGsrpNeighborSelectionPattern_Type(Integer32):
    """Custom type axsGsrpNeighborSelectionPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-Priority-MAC", 1),
          ("priority-Port-MAC", 2))
    )


_AxsGsrpNeighborSelectionPattern_Type.__name__ = "Integer32"
_AxsGsrpNeighborSelectionPattern_Object = MibTableColumn
axsGsrpNeighborSelectionPattern = _AxsGsrpNeighborSelectionPattern_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1, 5),
    _AxsGsrpNeighborSelectionPattern_Type()
)
axsGsrpNeighborSelectionPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpNeighborSelectionPattern.setStatus("mandatory")
_AxsGsrpNeighborVlanGroupTable_Object = MibTable
axsGsrpNeighborVlanGroupTable = _AxsGsrpNeighborVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    axsGsrpNeighborVlanGroupTable.setStatus("mandatory")
_AxsGsrpNeighborVlanGroupEntry_Object = MibTableRow
axsGsrpNeighborVlanGroupEntry = _AxsGsrpNeighborVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4, 1)
)
axsGsrpNeighborVlanGroupEntry.setIndexNames(
    (0, "AX4630S", "axsGsrpNeighborGroupId"),
    (0, "AX4630S", "axsGsrpNeighborVlanGroupId"),
    (0, "AX4630S", "axsGsrpNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    axsGsrpNeighborVlanGroupEntry.setStatus("mandatory")
_AxsGsrpNeighborVlanGroupId_Type = Integer32
_AxsGsrpNeighborVlanGroupId_Object = MibTableColumn
axsGsrpNeighborVlanGroupId = _AxsGsrpNeighborVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4, 1, 1),
    _AxsGsrpNeighborVlanGroupId_Type()
)
axsGsrpNeighborVlanGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpNeighborVlanGroupId.setStatus("mandatory")


class _AxsGsrpNeighborState_Type(Integer32):
    """Custom type axsGsrpNeighborState based on Integer32"""
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
        *(("backUp", 1),
          ("backUp-Waiting", 2),
          ("master", 3),
          ("backUp-No-Neighbor", 4),
          ("backUp-Lock", 5))
    )


_AxsGsrpNeighborState_Type.__name__ = "Integer32"
_AxsGsrpNeighborState_Object = MibTableColumn
axsGsrpNeighborState = _AxsGsrpNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4, 1, 2),
    _AxsGsrpNeighborState_Type()
)
axsGsrpNeighborState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpNeighborState.setStatus("mandatory")
_AxsGsrpNeighborPriority_Type = Integer32
_AxsGsrpNeighborPriority_Object = MibTableColumn
axsGsrpNeighborPriority = _AxsGsrpNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4, 1, 3),
    _AxsGsrpNeighborPriority_Type()
)
axsGsrpNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpNeighborPriority.setStatus("mandatory")
_AxsGsrpNeighborActivePorts_Type = Integer32
_AxsGsrpNeighborActivePorts_Object = MibTableColumn
axsGsrpNeighborActivePorts = _AxsGsrpNeighborActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4, 1, 4),
    _AxsGsrpNeighborActivePorts_Type()
)
axsGsrpNeighborActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpNeighborActivePorts.setStatus("mandatory")
_AxsVlan_ObjectIdentity = ObjectIdentity
axsVlan = _AxsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6)
)
_AxsVlanBridge_ObjectIdentity = ObjectIdentity
axsVlanBridge = _AxsVlanBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1)
)
_AxsVlanBridgeBase_ObjectIdentity = ObjectIdentity
axsVlanBridgeBase = _AxsVlanBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1)
)
_AxsVBBaseTable_Object = MibTable
axsVBBaseTable = _AxsVBBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    axsVBBaseTable.setStatus("mandatory")
_AxsVBBaseEntry_Object = MibTableRow
axsVBBaseEntry = _AxsVBBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1)
)
axsVBBaseEntry.setIndexNames(
    (0, "AX4630S", "axsVBBaseIndex"),
)
if mibBuilder.loadTexts:
    axsVBBaseEntry.setStatus("mandatory")
_AxsVBBaseIndex_Type = VlanIndex
_AxsVBBaseIndex_Object = MibTableColumn
axsVBBaseIndex = _AxsVBBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 1),
    _AxsVBBaseIndex_Type()
)
axsVBBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseIndex.setStatus("mandatory")
_AxsVBBaseBridgeAddress_Type = MacAddress
_AxsVBBaseBridgeAddress_Object = MibTableColumn
axsVBBaseBridgeAddress = _AxsVBBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 2),
    _AxsVBBaseBridgeAddress_Type()
)
axsVBBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseBridgeAddress.setStatus("mandatory")
_AxsVBBaseNumPorts_Type = Integer32
_AxsVBBaseNumPorts_Object = MibTableColumn
axsVBBaseNumPorts = _AxsVBBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 3),
    _AxsVBBaseNumPorts_Type()
)
axsVBBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseNumPorts.setStatus("mandatory")


class _AxsVBBaseType_Type(Integer32):
    """Custom type axsVBBaseType based on Integer32"""
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
          ("transparent-only", 2),
          ("sourceroute-only", 3),
          ("srt", 4))
    )


_AxsVBBaseType_Type.__name__ = "Integer32"
_AxsVBBaseType_Object = MibTableColumn
axsVBBaseType = _AxsVBBaseType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 4),
    _AxsVBBaseType_Type()
)
axsVBBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseType.setStatus("mandatory")
_AxsVBBaseVlanIfIndex_Type = Integer32
_AxsVBBaseVlanIfIndex_Object = MibTableColumn
axsVBBaseVlanIfIndex = _AxsVBBaseVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 5),
    _AxsVBBaseVlanIfIndex_Type()
)
axsVBBaseVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseVlanIfIndex.setStatus("mandatory")


class _AxsVBBaseVlanType_Type(Integer32):
    """Custom type axsVBBaseVlanType based on Integer32"""
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
        *(("port-based", 1),
          ("mac-based", 2),
          ("protocol-based", 3),
          ("ipsubnet-based", 4))
    )


_AxsVBBaseVlanType_Type.__name__ = "Integer32"
_AxsVBBaseVlanType_Object = MibTableColumn
axsVBBaseVlanType = _AxsVBBaseVlanType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 6),
    _AxsVBBaseVlanType_Type()
)
axsVBBaseVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseVlanType.setStatus("mandatory")
_AxsVBBaseVlanID_Type = VlanIdOrZero
_AxsVBBaseVlanID_Object = MibTableColumn
axsVBBaseVlanID = _AxsVBBaseVlanID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 7),
    _AxsVBBaseVlanID_Type()
)
axsVBBaseVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseVlanID.setStatus("mandatory")
_AxsVBBaseAssociatedPrimaryVlan_Type = VlanIdOrZero
_AxsVBBaseAssociatedPrimaryVlan_Object = MibTableColumn
axsVBBaseAssociatedPrimaryVlan = _AxsVBBaseAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 8),
    _AxsVBBaseAssociatedPrimaryVlan_Type()
)
axsVBBaseAssociatedPrimaryVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseAssociatedPrimaryVlan.setStatus("mandatory")


class _AxsVBBaseIfStatus_Type(Integer32):
    """Custom type axsVBBaseIfStatus based on Integer32"""
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


_AxsVBBaseIfStatus_Type.__name__ = "Integer32"
_AxsVBBaseIfStatus_Object = MibTableColumn
axsVBBaseIfStatus = _AxsVBBaseIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 9),
    _AxsVBBaseIfStatus_Type()
)
axsVBBaseIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseIfStatus.setStatus("mandatory")
_AxsVBBaseLastChange_Type = TimeTicks
_AxsVBBaseLastChange_Object = MibTableColumn
axsVBBaseLastChange = _AxsVBBaseLastChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 10),
    _AxsVBBaseLastChange_Type()
)
axsVBBaseLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseLastChange.setStatus("mandatory")


class _AxsVBBasePrivateVlanType_Type(Integer32):
    """Custom type axsVBBasePrivateVlanType based on Integer32"""
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


_AxsVBBasePrivateVlanType_Type.__name__ = "Integer32"
_AxsVBBasePrivateVlanType_Object = MibTableColumn
axsVBBasePrivateVlanType = _AxsVBBasePrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 11),
    _AxsVBBasePrivateVlanType_Type()
)
axsVBBasePrivateVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePrivateVlanType.setStatus("mandatory")
_AxsVBBasePortTable_Object = MibTable
axsVBBasePortTable = _AxsVBBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    axsVBBasePortTable.setStatus("mandatory")
_AxsVBBasePortEntry_Object = MibTableRow
axsVBBasePortEntry = _AxsVBBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1)
)
axsVBBasePortEntry.setIndexNames(
    (0, "AX4630S", "axsVBBasePortIndex"),
    (0, "AX4630S", "axsVBBasePort"),
)
if mibBuilder.loadTexts:
    axsVBBasePortEntry.setStatus("mandatory")
_AxsVBBasePortIndex_Type = VlanIndex
_AxsVBBasePortIndex_Object = MibTableColumn
axsVBBasePortIndex = _AxsVBBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 1),
    _AxsVBBasePortIndex_Type()
)
axsVBBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortIndex.setStatus("mandatory")
_AxsVBBasePort_Type = Integer32
_AxsVBBasePort_Object = MibTableColumn
axsVBBasePort = _AxsVBBasePort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 2),
    _AxsVBBasePort_Type()
)
axsVBBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePort.setStatus("mandatory")
_AxsVBBasePortIfIndex_Type = Integer32
_AxsVBBasePortIfIndex_Object = MibTableColumn
axsVBBasePortIfIndex = _AxsVBBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 3),
    _AxsVBBasePortIfIndex_Type()
)
axsVBBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortIfIndex.setStatus("mandatory")
_AxsVBBasePortCircuit_Type = ObjectIdentifier
_AxsVBBasePortCircuit_Object = MibTableColumn
axsVBBasePortCircuit = _AxsVBBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 4),
    _AxsVBBasePortCircuit_Type()
)
axsVBBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortCircuit.setStatus("mandatory")
_AxsVBBasePortDelayExceededDiscards_Type = Counter32
_AxsVBBasePortDelayExceededDiscards_Object = MibTableColumn
axsVBBasePortDelayExceededDiscards = _AxsVBBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 5),
    _AxsVBBasePortDelayExceededDiscards_Type()
)
axsVBBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortDelayExceededDiscards.setStatus("mandatory")
_AxsVBBasePortMtuExceededDiscards_Type = Counter32
_AxsVBBasePortMtuExceededDiscards_Object = MibTableColumn
axsVBBasePortMtuExceededDiscards = _AxsVBBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 6),
    _AxsVBBasePortMtuExceededDiscards_Type()
)
axsVBBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortMtuExceededDiscards.setStatus("mandatory")


class _AxsVBBasePortState_Type(Integer32):
    """Custom type axsVBBasePortState based on Integer32"""
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
          ("fix-forwarding", 7))
    )


_AxsVBBasePortState_Type.__name__ = "Integer32"
_AxsVBBasePortState_Object = MibTableColumn
axsVBBasePortState = _AxsVBBasePortState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 7),
    _AxsVBBasePortState_Type()
)
axsVBBasePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortState.setStatus("mandatory")


class _AxsVBBasePortTaggedState_Type(Integer32):
    """Custom type axsVBBasePortTaggedState based on Integer32"""
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


_AxsVBBasePortTaggedState_Type.__name__ = "Integer32"
_AxsVBBasePortTaggedState_Object = MibTableColumn
axsVBBasePortTaggedState = _AxsVBBasePortTaggedState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 8),
    _AxsVBBasePortTaggedState_Type()
)
axsVBBasePortTaggedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortTaggedState.setStatus("mandatory")
_AxsVBBasePortTranslatedTagID_Type = VlanIdOrZero
_AxsVBBasePortTranslatedTagID_Object = MibTableColumn
axsVBBasePortTranslatedTagID = _AxsVBBasePortTranslatedTagID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 9),
    _AxsVBBasePortTranslatedTagID_Type()
)
axsVBBasePortTranslatedTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortTranslatedTagID.setStatus("mandatory")
_AxsVlanBridgeStp_ObjectIdentity = ObjectIdentity
axsVlanBridgeStp = _AxsVlanBridgeStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2)
)
_AxsVBStpTable_Object = MibTable
axsVBStpTable = _AxsVBStpTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    axsVBStpTable.setStatus("mandatory")
_AxsVBStpEntry_Object = MibTableRow
axsVBStpEntry = _AxsVBStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1)
)
axsVBStpEntry.setIndexNames(
    (0, "AX4630S", "axsVBStpIndex"),
)
if mibBuilder.loadTexts:
    axsVBStpEntry.setStatus("mandatory")
_AxsVBStpIndex_Type = VlanIndex
_AxsVBStpIndex_Object = MibTableColumn
axsVBStpIndex = _AxsVBStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 1),
    _AxsVBStpIndex_Type()
)
axsVBStpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpIndex.setStatus("mandatory")


class _AxsVBStpProtocolSpecification_Type(Integer32):
    """Custom type axsVBStpProtocolSpecification based on Integer32"""
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
          ("decLb100", 2),
          ("ieee8021d", 3),
          ("ieee8021w", 4))
    )


_AxsVBStpProtocolSpecification_Type.__name__ = "Integer32"
_AxsVBStpProtocolSpecification_Object = MibTableColumn
axsVBStpProtocolSpecification = _AxsVBStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 2),
    _AxsVBStpProtocolSpecification_Type()
)
axsVBStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpProtocolSpecification.setStatus("mandatory")
_AxsVBStpPriority_Type = Integer32
_AxsVBStpPriority_Object = MibTableColumn
axsVBStpPriority = _AxsVBStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 3),
    _AxsVBStpPriority_Type()
)
axsVBStpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPriority.setStatus("mandatory")
_AxsVBStpTimeSinceTopologyChange_Type = TimeTicks
_AxsVBStpTimeSinceTopologyChange_Object = MibTableColumn
axsVBStpTimeSinceTopologyChange = _AxsVBStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 4),
    _AxsVBStpTimeSinceTopologyChange_Type()
)
axsVBStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpTimeSinceTopologyChange.setStatus("mandatory")
_AxsVBStpTopChanges_Type = Counter32
_AxsVBStpTopChanges_Object = MibTableColumn
axsVBStpTopChanges = _AxsVBStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 5),
    _AxsVBStpTopChanges_Type()
)
axsVBStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpTopChanges.setStatus("mandatory")
_AxsVBStpDesignatedRoot_Type = BridgeId
_AxsVBStpDesignatedRoot_Object = MibTableColumn
axsVBStpDesignatedRoot = _AxsVBStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 6),
    _AxsVBStpDesignatedRoot_Type()
)
axsVBStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpDesignatedRoot.setStatus("mandatory")
_AxsVBStpRootCost_Type = Integer32
_AxsVBStpRootCost_Object = MibTableColumn
axsVBStpRootCost = _AxsVBStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 7),
    _AxsVBStpRootCost_Type()
)
axsVBStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpRootCost.setStatus("mandatory")
_AxsVBStpRootPort_Type = Integer32
_AxsVBStpRootPort_Object = MibTableColumn
axsVBStpRootPort = _AxsVBStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 8),
    _AxsVBStpRootPort_Type()
)
axsVBStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpRootPort.setStatus("mandatory")
_AxsVBStpMaxAge_Type = Timeout
_AxsVBStpMaxAge_Object = MibTableColumn
axsVBStpMaxAge = _AxsVBStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 9),
    _AxsVBStpMaxAge_Type()
)
axsVBStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpMaxAge.setStatus("mandatory")
_AxsVBStpHelloTime_Type = Timeout
_AxsVBStpHelloTime_Object = MibTableColumn
axsVBStpHelloTime = _AxsVBStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 10),
    _AxsVBStpHelloTime_Type()
)
axsVBStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpHelloTime.setStatus("mandatory")
_AxsVBStpHoldTime_Type = Integer32
_AxsVBStpHoldTime_Object = MibTableColumn
axsVBStpHoldTime = _AxsVBStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 11),
    _AxsVBStpHoldTime_Type()
)
axsVBStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpHoldTime.setStatus("mandatory")
_AxsVBStpForwardDelay_Type = Timeout
_AxsVBStpForwardDelay_Object = MibTableColumn
axsVBStpForwardDelay = _AxsVBStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 12),
    _AxsVBStpForwardDelay_Type()
)
axsVBStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpForwardDelay.setStatus("mandatory")
_AxsVBStpBridgeMaxAge_Type = Timeout
_AxsVBStpBridgeMaxAge_Object = MibTableColumn
axsVBStpBridgeMaxAge = _AxsVBStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 13),
    _AxsVBStpBridgeMaxAge_Type()
)
axsVBStpBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpBridgeMaxAge.setStatus("mandatory")
_AxsVBStpBridgeHelloTime_Type = Timeout
_AxsVBStpBridgeHelloTime_Object = MibTableColumn
axsVBStpBridgeHelloTime = _AxsVBStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 14),
    _AxsVBStpBridgeHelloTime_Type()
)
axsVBStpBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpBridgeHelloTime.setStatus("mandatory")
_AxsVBStpBridgeForwardDelay_Type = Timeout
_AxsVBStpBridgeForwardDelay_Object = MibTableColumn
axsVBStpBridgeForwardDelay = _AxsVBStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 15),
    _AxsVBStpBridgeForwardDelay_Type()
)
axsVBStpBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpBridgeForwardDelay.setStatus("mandatory")
_AxsVBStpPortTable_Object = MibTable
axsVBStpPortTable = _AxsVBStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    axsVBStpPortTable.setStatus("mandatory")
_AxsVBStpPortEntry_Object = MibTableRow
axsVBStpPortEntry = _AxsVBStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1)
)
axsVBStpPortEntry.setIndexNames(
    (0, "AX4630S", "axsVBStpPortIndex"),
    (0, "AX4630S", "axsVBStpPort"),
)
if mibBuilder.loadTexts:
    axsVBStpPortEntry.setStatus("mandatory")
_AxsVBStpPortIndex_Type = VlanIndex
_AxsVBStpPortIndex_Object = MibTableColumn
axsVBStpPortIndex = _AxsVBStpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 1),
    _AxsVBStpPortIndex_Type()
)
axsVBStpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortIndex.setStatus("mandatory")
_AxsVBStpPort_Type = Integer32
_AxsVBStpPort_Object = MibTableColumn
axsVBStpPort = _AxsVBStpPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 2),
    _AxsVBStpPort_Type()
)
axsVBStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPort.setStatus("mandatory")
_AxsVBStpPortPriority_Type = Integer32
_AxsVBStpPortPriority_Object = MibTableColumn
axsVBStpPortPriority = _AxsVBStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 3),
    _AxsVBStpPortPriority_Type()
)
axsVBStpPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortPriority.setStatus("mandatory")


class _AxsVBStpPortState_Type(Integer32):
    """Custom type axsVBStpPortState based on Integer32"""
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
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_AxsVBStpPortState_Type.__name__ = "Integer32"
_AxsVBStpPortState_Object = MibTableColumn
axsVBStpPortState = _AxsVBStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 4),
    _AxsVBStpPortState_Type()
)
axsVBStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortState.setStatus("mandatory")


class _AxsVBStpPortEnable_Type(Integer32):
    """Custom type axsVBStpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AxsVBStpPortEnable_Type.__name__ = "Integer32"
_AxsVBStpPortEnable_Object = MibTableColumn
axsVBStpPortEnable = _AxsVBStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 5),
    _AxsVBStpPortEnable_Type()
)
axsVBStpPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortEnable.setStatus("mandatory")
_AxsVBStpPortPathCost_Type = Integer32
_AxsVBStpPortPathCost_Object = MibTableColumn
axsVBStpPortPathCost = _AxsVBStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 6),
    _AxsVBStpPortPathCost_Type()
)
axsVBStpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortPathCost.setStatus("mandatory")
_AxsVBStpPortDesignatedRoot_Type = BridgeId
_AxsVBStpPortDesignatedRoot_Object = MibTableColumn
axsVBStpPortDesignatedRoot = _AxsVBStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 7),
    _AxsVBStpPortDesignatedRoot_Type()
)
axsVBStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortDesignatedRoot.setStatus("mandatory")
_AxsVBStpPortDesignatedCost_Type = Integer32
_AxsVBStpPortDesignatedCost_Object = MibTableColumn
axsVBStpPortDesignatedCost = _AxsVBStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 8),
    _AxsVBStpPortDesignatedCost_Type()
)
axsVBStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortDesignatedCost.setStatus("mandatory")
_AxsVBStpPortDesignatedBridge_Type = BridgeId
_AxsVBStpPortDesignatedBridge_Object = MibTableColumn
axsVBStpPortDesignatedBridge = _AxsVBStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 9),
    _AxsVBStpPortDesignatedBridge_Type()
)
axsVBStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortDesignatedBridge.setStatus("mandatory")
_AxsVBStpPortDesignatedPort_Type = OctetString
_AxsVBStpPortDesignatedPort_Object = MibTableColumn
axsVBStpPortDesignatedPort = _AxsVBStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 10),
    _AxsVBStpPortDesignatedPort_Type()
)
axsVBStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortDesignatedPort.setStatus("mandatory")
_AxsVBStpPortForwardTransitions_Type = Counter32
_AxsVBStpPortForwardTransitions_Object = MibTableColumn
axsVBStpPortForwardTransitions = _AxsVBStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 11),
    _AxsVBStpPortForwardTransitions_Type()
)
axsVBStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortForwardTransitions.setStatus("mandatory")
_AxsVlanBridgeTp_ObjectIdentity = ObjectIdentity
axsVlanBridgeTp = _AxsVlanBridgeTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4)
)
_AxsVBTpTable_Object = MibTable
axsVBTpTable = _AxsVBTpTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    axsVBTpTable.setStatus("mandatory")
_AxsVBTpEntry_Object = MibTableRow
axsVBTpEntry = _AxsVBTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1, 1)
)
axsVBTpEntry.setIndexNames(
    (0, "AX4630S", "axsVBTpIndex"),
)
if mibBuilder.loadTexts:
    axsVBTpEntry.setStatus("mandatory")
_AxsVBTpIndex_Type = VlanIndex
_AxsVBTpIndex_Object = MibTableColumn
axsVBTpIndex = _AxsVBTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1, 1, 1),
    _AxsVBTpIndex_Type()
)
axsVBTpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpIndex.setStatus("mandatory")
_AxsVBTpLearnedEntryDiscards_Type = Counter32
_AxsVBTpLearnedEntryDiscards_Object = MibTableColumn
axsVBTpLearnedEntryDiscards = _AxsVBTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1, 1, 2),
    _AxsVBTpLearnedEntryDiscards_Type()
)
axsVBTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpLearnedEntryDiscards.setStatus("mandatory")
_AxsVBTpAgingTime_Type = Integer32
_AxsVBTpAgingTime_Object = MibTableColumn
axsVBTpAgingTime = _AxsVBTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1, 1, 3),
    _AxsVBTpAgingTime_Type()
)
axsVBTpAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpAgingTime.setStatus("mandatory")
_AxsVBTpFdbTable_Object = MibTable
axsVBTpFdbTable = _AxsVBTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    axsVBTpFdbTable.setStatus("mandatory")
_AxsVBTpFdbEntry_Object = MibTableRow
axsVBTpFdbEntry = _AxsVBTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2, 1)
)
axsVBTpFdbEntry.setIndexNames(
    (0, "AX4630S", "axsVBTpFdbIndex"),
    (0, "AX4630S", "axsVBTpFdbAddress"),
)
if mibBuilder.loadTexts:
    axsVBTpFdbEntry.setStatus("mandatory")
_AxsVBTpFdbIndex_Type = VlanIndex
_AxsVBTpFdbIndex_Object = MibTableColumn
axsVBTpFdbIndex = _AxsVBTpFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2, 1, 1),
    _AxsVBTpFdbIndex_Type()
)
axsVBTpFdbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpFdbIndex.setStatus("mandatory")
_AxsVBTpFdbAddress_Type = MacAddress
_AxsVBTpFdbAddress_Object = MibTableColumn
axsVBTpFdbAddress = _AxsVBTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2, 1, 2),
    _AxsVBTpFdbAddress_Type()
)
axsVBTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpFdbAddress.setStatus("mandatory")
_AxsVBTpFdbPort_Type = Integer32
_AxsVBTpFdbPort_Object = MibTableColumn
axsVBTpFdbPort = _AxsVBTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2, 1, 3),
    _AxsVBTpFdbPort_Type()
)
axsVBTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpFdbPort.setStatus("mandatory")


class _AxsVBTpFdbStatus_Type(Integer32):
    """Custom type axsVBTpFdbStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("learned", 3),
          ("self", 4),
          ("mgmt", 5))
    )


_AxsVBTpFdbStatus_Type.__name__ = "Integer32"
_AxsVBTpFdbStatus_Object = MibTableColumn
axsVBTpFdbStatus = _AxsVBTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2, 1, 4),
    _AxsVBTpFdbStatus_Type()
)
axsVBTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpFdbStatus.setStatus("mandatory")
_AxsVBTpPortTable_Object = MibTable
axsVBTpPortTable = _AxsVBTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    axsVBTpPortTable.setStatus("mandatory")
_AxsVBTpPortEntry_Object = MibTableRow
axsVBTpPortEntry = _AxsVBTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1)
)
axsVBTpPortEntry.setIndexNames(
    (0, "AX4630S", "axsVBTpPortIndex"),
    (0, "AX4630S", "axsVBTpPort"),
)
if mibBuilder.loadTexts:
    axsVBTpPortEntry.setStatus("mandatory")
_AxsVBTpPortIndex_Type = VlanIndex
_AxsVBTpPortIndex_Object = MibTableColumn
axsVBTpPortIndex = _AxsVBTpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 1),
    _AxsVBTpPortIndex_Type()
)
axsVBTpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortIndex.setStatus("mandatory")
_AxsVBTpPort_Type = Integer32
_AxsVBTpPort_Object = MibTableColumn
axsVBTpPort = _AxsVBTpPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 2),
    _AxsVBTpPort_Type()
)
axsVBTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPort.setStatus("mandatory")
_AxsVBTpPortMaxInfo_Type = Integer32
_AxsVBTpPortMaxInfo_Object = MibTableColumn
axsVBTpPortMaxInfo = _AxsVBTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 3),
    _AxsVBTpPortMaxInfo_Type()
)
axsVBTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortMaxInfo.setStatus("mandatory")
_AxsVBTpPortInFrames_Type = Counter32
_AxsVBTpPortInFrames_Object = MibTableColumn
axsVBTpPortInFrames = _AxsVBTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 4),
    _AxsVBTpPortInFrames_Type()
)
axsVBTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortInFrames.setStatus("mandatory")
_AxsVBTpPortOutFrames_Type = Counter32
_AxsVBTpPortOutFrames_Object = MibTableColumn
axsVBTpPortOutFrames = _AxsVBTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 5),
    _AxsVBTpPortOutFrames_Type()
)
axsVBTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortOutFrames.setStatus("mandatory")
_AxsVBTpPortInDiscards_Type = Counter32
_AxsVBTpPortInDiscards_Object = MibTableColumn
axsVBTpPortInDiscards = _AxsVBTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 6),
    _AxsVBTpPortInDiscards_Type()
)
axsVBTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortInDiscards.setStatus("mandatory")
_AxsVlanBridgeStatic_ObjectIdentity = ObjectIdentity
axsVlanBridgeStatic = _AxsVlanBridgeStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5)
)
_AxsVBStaticTable_Object = MibTable
axsVBStaticTable = _AxsVBStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    axsVBStaticTable.setStatus("mandatory")
_AxsVBStaticEntry_Object = MibTableRow
axsVBStaticEntry = _AxsVBStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1)
)
axsVBStaticEntry.setIndexNames(
    (0, "AX4630S", "axsVBStaticIndex"),
    (0, "AX4630S", "axsVBStaticAddress"),
)
if mibBuilder.loadTexts:
    axsVBStaticEntry.setStatus("mandatory")
_AxsVBStaticIndex_Type = VlanIndex
_AxsVBStaticIndex_Object = MibTableColumn
axsVBStaticIndex = _AxsVBStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1, 1),
    _AxsVBStaticIndex_Type()
)
axsVBStaticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStaticIndex.setStatus("mandatory")
_AxsVBStaticAddress_Type = MacAddress
_AxsVBStaticAddress_Object = MibTableColumn
axsVBStaticAddress = _AxsVBStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1, 2),
    _AxsVBStaticAddress_Type()
)
axsVBStaticAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStaticAddress.setStatus("mandatory")
_AxsVBStaticReceivePort_Type = Integer32
_AxsVBStaticReceivePort_Object = MibTableColumn
axsVBStaticReceivePort = _AxsVBStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1, 3),
    _AxsVBStaticReceivePort_Type()
)
axsVBStaticReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStaticReceivePort.setStatus("mandatory")
_AxsVBStaticAllowedToGoTo_Type = OctetString
_AxsVBStaticAllowedToGoTo_Object = MibTableColumn
axsVBStaticAllowedToGoTo = _AxsVBStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1, 4),
    _AxsVBStaticAllowedToGoTo_Type()
)
axsVBStaticAllowedToGoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStaticAllowedToGoTo.setStatus("mandatory")


class _AxsVBStaticStatus_Type(Integer32):
    """Custom type axsVBStaticStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("permanent", 3),
          ("deleteOnReset", 4),
          ("deleteOnTimeout", 5))
    )


_AxsVBStaticStatus_Type.__name__ = "Integer32"
_AxsVBStaticStatus_Object = MibTableColumn
axsVBStaticStatus = _AxsVBStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1, 5),
    _AxsVBStaticStatus_Type()
)
axsVBStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStaticStatus.setStatus("mandatory")
_AxsVlanBridgeMaxVlans_Type = VlanIndex
_AxsVlanBridgeMaxVlans_Object = MibScalar
axsVlanBridgeMaxVlans = _AxsVlanBridgeMaxVlans_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 101),
    _AxsVlanBridgeMaxVlans_Type()
)
axsVlanBridgeMaxVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVlanBridgeMaxVlans.setStatus("mandatory")
_AxsVlanBridgeMaxSpans_Type = VlanIndex
_AxsVlanBridgeMaxSpans_Object = MibScalar
axsVlanBridgeMaxSpans = _AxsVlanBridgeMaxSpans_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 102),
    _AxsVlanBridgeMaxSpans_Type()
)
axsVlanBridgeMaxSpans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVlanBridgeMaxSpans.setStatus("mandatory")
_AxsVlanTagTranslation_ObjectIdentity = ObjectIdentity
axsVlanTagTranslation = _AxsVlanTagTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10)
)
_AxsVlanTagTranslationTable_Object = MibTable
axsVlanTagTranslationTable = _AxsVlanTagTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1)
)
if mibBuilder.loadTexts:
    axsVlanTagTranslationTable.setStatus("mandatory")
_AxsVlanTagTranslationEntry_Object = MibTableRow
axsVlanTagTranslationEntry = _AxsVlanTagTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1)
)
axsVlanTagTranslationEntry.setIndexNames(
    (0, "AX4630S", "axsVlanTagTranslationVlanId"),
    (0, "AX4630S", "axsVlanTagTranslationTranslatedId"),
)
if mibBuilder.loadTexts:
    axsVlanTagTranslationEntry.setStatus("mandatory")
_AxsVlanTagTranslationVlanId_Type = Integer32
_AxsVlanTagTranslationVlanId_Object = MibTableColumn
axsVlanTagTranslationVlanId = _AxsVlanTagTranslationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1, 1),
    _AxsVlanTagTranslationVlanId_Type()
)
axsVlanTagTranslationVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsVlanTagTranslationVlanId.setStatus("mandatory")
_AxsVlanTagTranslationTranslatedId_Type = Integer32
_AxsVlanTagTranslationTranslatedId_Object = MibTableColumn
axsVlanTagTranslationTranslatedId = _AxsVlanTagTranslationTranslatedId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1, 2),
    _AxsVlanTagTranslationTranslatedId_Type()
)
axsVlanTagTranslationTranslatedId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsVlanTagTranslationTranslatedId.setStatus("mandatory")
_AxsVlanTagTranslationPorts_Type = PortList
_AxsVlanTagTranslationPorts_Object = MibTableColumn
axsVlanTagTranslationPorts = _AxsVlanTagTranslationPorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1, 3),
    _AxsVlanTagTranslationPorts_Type()
)
axsVlanTagTranslationPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVlanTagTranslationPorts.setStatus("mandatory")
_AxsOadp_ObjectIdentity = ObjectIdentity
axsOadp = _AxsOadp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7)
)
_AxsOadpMIBObjects_ObjectIdentity = ObjectIdentity
axsOadpMIBObjects = _AxsOadpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1)
)
_AxsOadpGlobalInfo_ObjectIdentity = ObjectIdentity
axsOadpGlobalInfo = _AxsOadpGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1)
)
_AxsOadpGlobalActive_Type = TruthValue
_AxsOadpGlobalActive_Object = MibScalar
axsOadpGlobalActive = _AxsOadpGlobalActive_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 1),
    _AxsOadpGlobalActive_Type()
)
axsOadpGlobalActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalActive.setStatus("mandatory")
_AxsOadpGlobalCdpActive_Type = TruthValue
_AxsOadpGlobalCdpActive_Object = MibScalar
axsOadpGlobalCdpActive = _AxsOadpGlobalCdpActive_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 2),
    _AxsOadpGlobalCdpActive_Type()
)
axsOadpGlobalCdpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalCdpActive.setStatus("mandatory")
_AxsOadpGlobalMessageInterval_Type = Integer32
_AxsOadpGlobalMessageInterval_Object = MibScalar
axsOadpGlobalMessageInterval = _AxsOadpGlobalMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 3),
    _AxsOadpGlobalMessageInterval_Type()
)
axsOadpGlobalMessageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalMessageInterval.setStatus("mandatory")
_AxsOadpGlobalHoldTime_Type = Integer32
_AxsOadpGlobalHoldTime_Object = MibScalar
axsOadpGlobalHoldTime = _AxsOadpGlobalHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 4),
    _AxsOadpGlobalHoldTime_Type()
)
axsOadpGlobalHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalHoldTime.setStatus("mandatory")
_AxsOadpGlobalCacheLastChange_Type = TimeTicks
_AxsOadpGlobalCacheLastChange_Object = MibScalar
axsOadpGlobalCacheLastChange = _AxsOadpGlobalCacheLastChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 5),
    _AxsOadpGlobalCacheLastChange_Type()
)
axsOadpGlobalCacheLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalCacheLastChange.setStatus("mandatory")
_AxsOadpGlobalName_Type = DisplayString
_AxsOadpGlobalName_Object = MibScalar
axsOadpGlobalName = _AxsOadpGlobalName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 6),
    _AxsOadpGlobalName_Type()
)
axsOadpGlobalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalName.setStatus("mandatory")


class _AxsOadpGlobalNameType_Type(Integer32):
    """Custom type axsOadpGlobalNameType based on Integer32"""
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
        *(("other", 1),
          ("sysName", 2),
          ("serialNumber", 3),
          ("macaddress", 4))
    )


_AxsOadpGlobalNameType_Type.__name__ = "Integer32"
_AxsOadpGlobalNameType_Object = MibScalar
axsOadpGlobalNameType = _AxsOadpGlobalNameType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 7),
    _AxsOadpGlobalNameType_Type()
)
axsOadpGlobalNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalNameType.setStatus("mandatory")
_AxsOadpPortInfo_ObjectIdentity = ObjectIdentity
axsOadpPortInfo = _AxsOadpPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2)
)
_AxsOadpPortConfigTable_Object = MibTable
axsOadpPortConfigTable = _AxsOadpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    axsOadpPortConfigTable.setStatus("mandatory")
_AxsOadpPortConfigEntry_Object = MibTableRow
axsOadpPortConfigEntry = _AxsOadpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2, 1, 1)
)
axsOadpPortConfigEntry.setIndexNames(
    (0, "AX4630S", "axsOadpPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    axsOadpPortConfigEntry.setStatus("mandatory")
_AxsOadpPortConfigIfIndex_Type = InterfaceIndex
_AxsOadpPortConfigIfIndex_Object = MibTableColumn
axsOadpPortConfigIfIndex = _AxsOadpPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2, 1, 1, 1),
    _AxsOadpPortConfigIfIndex_Type()
)
axsOadpPortConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpPortConfigIfIndex.setStatus("mandatory")
_AxsOadpPortConfigActive_Type = TruthValue
_AxsOadpPortConfigActive_Object = MibTableColumn
axsOadpPortConfigActive = _AxsOadpPortConfigActive_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2, 1, 1, 2),
    _AxsOadpPortConfigActive_Type()
)
axsOadpPortConfigActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpPortConfigActive.setStatus("mandatory")
_AxsOadpNeighborInfo_ObjectIdentity = ObjectIdentity
axsOadpNeighborInfo = _AxsOadpNeighborInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3)
)
_AxsOadpNeighborTable_Object = MibTable
axsOadpNeighborTable = _AxsOadpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    axsOadpNeighborTable.setStatus("mandatory")
_AxsOadpNeighborEntry_Object = MibTableRow
axsOadpNeighborEntry = _AxsOadpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1)
)
axsOadpNeighborEntry.setIndexNames(
    (0, "AX4630S", "axsOadpIfIndex"),
    (0, "AX4630S", "axsOadpTagID"),
    (0, "AX4630S", "axsOadpNeighborIndex"),
    (0, "AX4630S", "axsOadpNeighborTagID"),
)
if mibBuilder.loadTexts:
    axsOadpNeighborEntry.setStatus("mandatory")
_AxsOadpIfIndex_Type = InterfaceIndex
_AxsOadpIfIndex_Object = MibTableColumn
axsOadpIfIndex = _AxsOadpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 1),
    _AxsOadpIfIndex_Type()
)
axsOadpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpIfIndex.setStatus("mandatory")
_AxsOadpTagID_Type = Integer32
_AxsOadpTagID_Object = MibTableColumn
axsOadpTagID = _AxsOadpTagID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 2),
    _AxsOadpTagID_Type()
)
axsOadpTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpTagID.setStatus("mandatory")
_AxsOadpNeighborIndex_Type = Integer32
_AxsOadpNeighborIndex_Object = MibTableColumn
axsOadpNeighborIndex = _AxsOadpNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 3),
    _AxsOadpNeighborIndex_Type()
)
axsOadpNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborIndex.setStatus("mandatory")
_AxsOadpNeighborTagID_Type = Integer32
_AxsOadpNeighborTagID_Object = MibTableColumn
axsOadpNeighborTagID = _AxsOadpNeighborTagID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 4),
    _AxsOadpNeighborTagID_Type()
)
axsOadpNeighborTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborTagID.setStatus("mandatory")


class _AxsOadpNeighborVendorType_Type(Integer32):
    """Custom type axsOadpNeighborVendorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("oadp", 2),
          ("cdp", 3))
    )


_AxsOadpNeighborVendorType_Type.__name__ = "Integer32"
_AxsOadpNeighborVendorType_Object = MibTableColumn
axsOadpNeighborVendorType = _AxsOadpNeighborVendorType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 5),
    _AxsOadpNeighborVendorType_Type()
)
axsOadpNeighborVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborVendorType.setStatus("mandatory")


class _AxsOadpNeighborSNMPAgentAddressType_Type(Integer32):
    """Custom type axsOadpNeighborSNMPAgentAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              20,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 20),
          ("other-notSupported", 65535))
    )


_AxsOadpNeighborSNMPAgentAddressType_Type.__name__ = "Integer32"
_AxsOadpNeighborSNMPAgentAddressType_Object = MibTableColumn
axsOadpNeighborSNMPAgentAddressType = _AxsOadpNeighborSNMPAgentAddressType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 6),
    _AxsOadpNeighborSNMPAgentAddressType_Type()
)
axsOadpNeighborSNMPAgentAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSNMPAgentAddressType.setStatus("mandatory")
_AxsOadpNeighborSNMPAgentAddress_Type = DisplayString
_AxsOadpNeighborSNMPAgentAddress_Object = MibTableColumn
axsOadpNeighborSNMPAgentAddress = _AxsOadpNeighborSNMPAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 7),
    _AxsOadpNeighborSNMPAgentAddress_Type()
)
axsOadpNeighborSNMPAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSNMPAgentAddress.setStatus("mandatory")
_AxsOadpNeighborDescr_Type = DisplayString
_AxsOadpNeighborDescr_Object = MibTableColumn
axsOadpNeighborDescr = _AxsOadpNeighborDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 8),
    _AxsOadpNeighborDescr_Type()
)
axsOadpNeighborDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborDescr.setStatus("mandatory")
_AxsOadpNeighborDeviceID_Type = DisplayString
_AxsOadpNeighborDeviceID_Object = MibTableColumn
axsOadpNeighborDeviceID = _AxsOadpNeighborDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 9),
    _AxsOadpNeighborDeviceID_Type()
)
axsOadpNeighborDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborDeviceID.setStatus("mandatory")
_AxsOadpNeighborSlotPort_Type = DisplayString
_AxsOadpNeighborSlotPort_Object = MibTableColumn
axsOadpNeighborSlotPort = _AxsOadpNeighborSlotPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 10),
    _AxsOadpNeighborSlotPort_Type()
)
axsOadpNeighborSlotPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSlotPort.setStatus("mandatory")
_AxsOadpNeighborIfIndex_Type = InterfaceIndex
_AxsOadpNeighborIfIndex_Object = MibTableColumn
axsOadpNeighborIfIndex = _AxsOadpNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 11),
    _AxsOadpNeighborIfIndex_Type()
)
axsOadpNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborIfIndex.setStatus("mandatory")
_AxsOadpNeighborIfSpeed_Type = Gauge32
_AxsOadpNeighborIfSpeed_Object = MibTableColumn
axsOadpNeighborIfSpeed = _AxsOadpNeighborIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 12),
    _AxsOadpNeighborIfSpeed_Type()
)
axsOadpNeighborIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborIfSpeed.setStatus("mandatory")
_AxsOadpNeighborDeviceType_Type = DisplayString
_AxsOadpNeighborDeviceType_Object = MibTableColumn
axsOadpNeighborDeviceType = _AxsOadpNeighborDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 13),
    _AxsOadpNeighborDeviceType_Type()
)
axsOadpNeighborDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborDeviceType.setStatus("mandatory")
_AxsOadpNeighborService_Type = OctetString
_AxsOadpNeighborService_Object = MibTableColumn
axsOadpNeighborService = _AxsOadpNeighborService_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 14),
    _AxsOadpNeighborService_Type()
)
axsOadpNeighborService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborService.setStatus("mandatory")
_AxsOadpNeighborVTPMgmtDomain_Type = DisplayString
_AxsOadpNeighborVTPMgmtDomain_Object = MibTableColumn
axsOadpNeighborVTPMgmtDomain = _AxsOadpNeighborVTPMgmtDomain_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 15),
    _AxsOadpNeighborVTPMgmtDomain_Type()
)
axsOadpNeighborVTPMgmtDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborVTPMgmtDomain.setStatus("mandatory")
_AxsOadpNeighborNativeVLAN_Type = Integer32
_AxsOadpNeighborNativeVLAN_Object = MibTableColumn
axsOadpNeighborNativeVLAN = _AxsOadpNeighborNativeVLAN_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 16),
    _AxsOadpNeighborNativeVLAN_Type()
)
axsOadpNeighborNativeVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborNativeVLAN.setStatus("mandatory")


class _AxsOadpNeighborDuplex_Type(Integer32):
    """Custom type axsOadpNeighborDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("half", 2),
          ("full", 3))
    )


_AxsOadpNeighborDuplex_Type.__name__ = "Integer32"
_AxsOadpNeighborDuplex_Object = MibTableColumn
axsOadpNeighborDuplex = _AxsOadpNeighborDuplex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 17),
    _AxsOadpNeighborDuplex_Type()
)
axsOadpNeighborDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborDuplex.setStatus("mandatory")
_AxsOadpNeighborApplianceID_Type = Gauge32
_AxsOadpNeighborApplianceID_Object = MibTableColumn
axsOadpNeighborApplianceID = _AxsOadpNeighborApplianceID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 18),
    _AxsOadpNeighborApplianceID_Type()
)
axsOadpNeighborApplianceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborApplianceID.setStatus("mandatory")
_AxsOadpNeighborVlanID_Type = Gauge32
_AxsOadpNeighborVlanID_Object = MibTableColumn
axsOadpNeighborVlanID = _AxsOadpNeighborVlanID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 19),
    _AxsOadpNeighborVlanID_Type()
)
axsOadpNeighborVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborVlanID.setStatus("mandatory")
_AxsOadpNeighborPowerConsumption_Type = Gauge32
_AxsOadpNeighborPowerConsumption_Object = MibTableColumn
axsOadpNeighborPowerConsumption = _AxsOadpNeighborPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 20),
    _AxsOadpNeighborPowerConsumption_Type()
)
axsOadpNeighborPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborPowerConsumption.setStatus("mandatory")
_AxsOadpNeighborMTU_Type = Gauge32
_AxsOadpNeighborMTU_Object = MibTableColumn
axsOadpNeighborMTU = _AxsOadpNeighborMTU_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 21),
    _AxsOadpNeighborMTU_Type()
)
axsOadpNeighborMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborMTU.setStatus("mandatory")
_AxsOadpNeighborSysName_Type = DisplayString
_AxsOadpNeighborSysName_Object = MibTableColumn
axsOadpNeighborSysName = _AxsOadpNeighborSysName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 22),
    _AxsOadpNeighborSysName_Type()
)
axsOadpNeighborSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSysName.setStatus("mandatory")
_AxsOadpNeighborSysObjectID_Type = ObjectIdentifier
_AxsOadpNeighborSysObjectID_Object = MibTableColumn
axsOadpNeighborSysObjectID = _AxsOadpNeighborSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 23),
    _AxsOadpNeighborSysObjectID_Type()
)
axsOadpNeighborSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSysObjectID.setStatus("mandatory")


class _AxsOadpNeighborSecondarySNMPAgentAddressType_Type(Integer32):
    """Custom type axsOadpNeighborSecondarySNMPAgentAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              20,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 20),
          ("other-notSupported", 65535))
    )


_AxsOadpNeighborSecondarySNMPAgentAddressType_Type.__name__ = "Integer32"
_AxsOadpNeighborSecondarySNMPAgentAddressType_Object = MibTableColumn
axsOadpNeighborSecondarySNMPAgentAddressType = _AxsOadpNeighborSecondarySNMPAgentAddressType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 24),
    _AxsOadpNeighborSecondarySNMPAgentAddressType_Type()
)
axsOadpNeighborSecondarySNMPAgentAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSecondarySNMPAgentAddressType.setStatus("mandatory")
_AxsOadpNeighborSecondarySNMPAgentAddress_Type = DisplayString
_AxsOadpNeighborSecondarySNMPAgentAddress_Object = MibTableColumn
axsOadpNeighborSecondarySNMPAgentAddress = _AxsOadpNeighborSecondarySNMPAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 25),
    _AxsOadpNeighborSecondarySNMPAgentAddress_Type()
)
axsOadpNeighborSecondarySNMPAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSecondarySNMPAgentAddress.setStatus("mandatory")
_AxsOadpNeighborPhysLocation_Type = DisplayString
_AxsOadpNeighborPhysLocation_Object = MibTableColumn
axsOadpNeighborPhysLocation = _AxsOadpNeighborPhysLocation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 26),
    _AxsOadpNeighborPhysLocation_Type()
)
axsOadpNeighborPhysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborPhysLocation.setStatus("mandatory")
_AxsOadpNeighborCacheLastChange_Type = TimeTicks
_AxsOadpNeighborCacheLastChange_Object = MibTableColumn
axsOadpNeighborCacheLastChange = _AxsOadpNeighborCacheLastChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 27),
    _AxsOadpNeighborCacheLastChange_Type()
)
axsOadpNeighborCacheLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborCacheLastChange.setStatus("mandatory")
_AxsOadpNeighborIfHighSpeed_Type = Gauge32
_AxsOadpNeighborIfHighSpeed_Object = MibTableColumn
axsOadpNeighborIfHighSpeed = _AxsOadpNeighborIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 28),
    _AxsOadpNeighborIfHighSpeed_Type()
)
axsOadpNeighborIfHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborIfHighSpeed.setStatus("mandatory")
_AxsOadpMIBNotifications_ObjectIdentity = ObjectIdentity
axsOadpMIBNotifications = _AxsOadpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 2)
)
_AxsFlow_ObjectIdentity = ObjectIdentity
axsFlow = _AxsFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8)
)
_AxsAccessFilterStats_ObjectIdentity = ObjectIdentity
axsAccessFilterStats = _AxsAccessFilterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9)
)
_AxsAccessFilterStatsInTable_Object = MibTable
axsAccessFilterStatsInTable = _AxsAccessFilterStatsInTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1)
)
if mibBuilder.loadTexts:
    axsAccessFilterStatsInTable.setStatus("mandatory")
_AxsAccessFilterStatsInEntry_Object = MibTableRow
axsAccessFilterStatsInEntry = _AxsAccessFilterStatsInEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1)
)
axsAccessFilterStatsInEntry.setIndexNames(
    (0, "AX4630S", "axsAccessFilterStatsInifIndex"),
    (0, "AX4630S", "axsAccessFilterStatsInifIndexType"),
    (0, "AX4630S", "axsAccessFilterStatsInListIndex"),
    (0, "AX4630S", "axsAccessFilterStatsInSequenceNumber"),
)
if mibBuilder.loadTexts:
    axsAccessFilterStatsInEntry.setStatus("mandatory")
_AxsAccessFilterStatsInifIndex_Type = Integer32
_AxsAccessFilterStatsInifIndex_Object = MibTableColumn
axsAccessFilterStatsInifIndex = _AxsAccessFilterStatsInifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 1),
    _AxsAccessFilterStatsInifIndex_Type()
)
axsAccessFilterStatsInifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInifIndex.setStatus("mandatory")
_AxsAccessFilterStatsInifIndexType_Type = Integer32
_AxsAccessFilterStatsInifIndexType_Object = MibTableColumn
axsAccessFilterStatsInifIndexType = _AxsAccessFilterStatsInifIndexType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 2),
    _AxsAccessFilterStatsInifIndexType_Type()
)
axsAccessFilterStatsInifIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInifIndexType.setStatus("mandatory")
_AxsAccessFilterStatsInListIndex_Type = Unsigned32
_AxsAccessFilterStatsInListIndex_Object = MibTableColumn
axsAccessFilterStatsInListIndex = _AxsAccessFilterStatsInListIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 3),
    _AxsAccessFilterStatsInListIndex_Type()
)
axsAccessFilterStatsInListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInListIndex.setStatus("mandatory")
_AxsAccessFilterStatsInSequenceNumber_Type = Unsigned32
_AxsAccessFilterStatsInSequenceNumber_Object = MibTableColumn
axsAccessFilterStatsInSequenceNumber = _AxsAccessFilterStatsInSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 4),
    _AxsAccessFilterStatsInSequenceNumber_Type()
)
axsAccessFilterStatsInSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInSequenceNumber.setStatus("mandatory")
_AxsAccessFilterStatsInListName_Type = DisplayString
_AxsAccessFilterStatsInListName_Object = MibTableColumn
axsAccessFilterStatsInListName = _AxsAccessFilterStatsInListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 5),
    _AxsAccessFilterStatsInListName_Type()
)
axsAccessFilterStatsInListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInListName.setStatus("mandatory")
_AxsAccessFilterStatsInMatchedPackets_Type = Counter64
_AxsAccessFilterStatsInMatchedPackets_Object = MibTableColumn
axsAccessFilterStatsInMatchedPackets = _AxsAccessFilterStatsInMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 6),
    _AxsAccessFilterStatsInMatchedPackets_Type()
)
axsAccessFilterStatsInMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMatchedPackets.setStatus("mandatory")
_AxsAccessFilterStatsOutTable_Object = MibTable
axsAccessFilterStatsOutTable = _AxsAccessFilterStatsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 2)
)
if mibBuilder.loadTexts:
    axsAccessFilterStatsOutTable.setStatus("mandatory")
_AxsAccessFilterStatsOutEntry_Object = MibTableRow
axsAccessFilterStatsOutEntry = _AxsAccessFilterStatsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 2, 1)
)
axsAccessFilterStatsOutEntry.setIndexNames(
    (0, "AX4630S", "axsAccessFilterStatsOutifIndex"),
    (0, "AX4630S", "axsAccessFilterStatsOutifIndexType"),
    (0, "AX4630S", "axsAccessFilterStatsOutListIndex"),
    (0, "AX4630S", "axsAccessFilterStatsOutSequenceNumber"),
)
if mibBuilder.loadTexts:
    axsAccessFilterStatsOutEntry.setStatus("mandatory")
_AxsAccessFilterStatsOutifIndex_Type = Integer32
_AxsAccessFilterStatsOutifIndex_Object = MibTableColumn
axsAccessFilterStatsOutifIndex = _AxsAccessFilterStatsOutifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 2, 1, 1),
    _AxsAccessFilterStatsOutifIndex_Type()
)
axsAccessFilterStatsOutifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsOutifIndex.setStatus("mandatory")
_AxsAccessFilterStatsOutifIndexType_Type = Integer32
_AxsAccessFilterStatsOutifIndexType_Object = MibTableColumn
axsAccessFilterStatsOutifIndexType = _AxsAccessFilterStatsOutifIndexType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 2, 1, 2),
    _AxsAccessFilterStatsOutifIndexType_Type()
)
axsAccessFilterStatsOutifIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsOutifIndexType.setStatus("mandatory")
_AxsAccessFilterStatsOutListIndex_Type = Unsigned32
_AxsAccessFilterStatsOutListIndex_Object = MibTableColumn
axsAccessFilterStatsOutListIndex = _AxsAccessFilterStatsOutListIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 2, 1, 3),
    _AxsAccessFilterStatsOutListIndex_Type()
)
axsAccessFilterStatsOutListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsOutListIndex.setStatus("mandatory")
_AxsAccessFilterStatsOutSequenceNumber_Type = Unsigned32
_AxsAccessFilterStatsOutSequenceNumber_Object = MibTableColumn
axsAccessFilterStatsOutSequenceNumber = _AxsAccessFilterStatsOutSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 2, 1, 4),
    _AxsAccessFilterStatsOutSequenceNumber_Type()
)
axsAccessFilterStatsOutSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsOutSequenceNumber.setStatus("mandatory")
_AxsAccessFilterStatsOutListName_Type = DisplayString
_AxsAccessFilterStatsOutListName_Object = MibTableColumn
axsAccessFilterStatsOutListName = _AxsAccessFilterStatsOutListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 2, 1, 5),
    _AxsAccessFilterStatsOutListName_Type()
)
axsAccessFilterStatsOutListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAccessFilterStatsOutListName.setStatus("mandatory")
_AxsAccessFilterStatsOutMatchedPackets_Type = Counter64
_AxsAccessFilterStatsOutMatchedPackets_Object = MibTableColumn
axsAccessFilterStatsOutMatchedPackets = _AxsAccessFilterStatsOutMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 2, 1, 6),
    _AxsAccessFilterStatsOutMatchedPackets_Type()
)
axsAccessFilterStatsOutMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAccessFilterStatsOutMatchedPackets.setStatus("mandatory")
_AxsAccessFilterStatsInMirrorTable_Object = MibTable
axsAccessFilterStatsInMirrorTable = _AxsAccessFilterStatsInMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 9)
)
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMirrorTable.setStatus("mandatory")
_AxsAccessFilterStatsInMirrorEntry_Object = MibTableRow
axsAccessFilterStatsInMirrorEntry = _AxsAccessFilterStatsInMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 9, 1)
)
axsAccessFilterStatsInMirrorEntry.setIndexNames(
    (0, "AX4630S", "axsAccessFilterStatsInMirrorifIndex"),
    (0, "AX4630S", "axsAccessFilterStatsInMirrorifIndexType"),
    (0, "AX4630S", "axsAccessFilterStatsInMirrorListIndex"),
    (0, "AX4630S", "axsAccessFilterStatsInMirrorSequenceNumber"),
)
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMirrorEntry.setStatus("mandatory")
_AxsAccessFilterStatsInMirrorifIndex_Type = Integer32
_AxsAccessFilterStatsInMirrorifIndex_Object = MibTableColumn
axsAccessFilterStatsInMirrorifIndex = _AxsAccessFilterStatsInMirrorifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 9, 1, 1),
    _AxsAccessFilterStatsInMirrorifIndex_Type()
)
axsAccessFilterStatsInMirrorifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMirrorifIndex.setStatus("mandatory")
_AxsAccessFilterStatsInMirrorifIndexType_Type = Integer32
_AxsAccessFilterStatsInMirrorifIndexType_Object = MibTableColumn
axsAccessFilterStatsInMirrorifIndexType = _AxsAccessFilterStatsInMirrorifIndexType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 9, 1, 2),
    _AxsAccessFilterStatsInMirrorifIndexType_Type()
)
axsAccessFilterStatsInMirrorifIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMirrorifIndexType.setStatus("mandatory")
_AxsAccessFilterStatsInMirrorListIndex_Type = Unsigned32
_AxsAccessFilterStatsInMirrorListIndex_Object = MibTableColumn
axsAccessFilterStatsInMirrorListIndex = _AxsAccessFilterStatsInMirrorListIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 9, 1, 3),
    _AxsAccessFilterStatsInMirrorListIndex_Type()
)
axsAccessFilterStatsInMirrorListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMirrorListIndex.setStatus("mandatory")
_AxsAccessFilterStatsInMirrorSequenceNumber_Type = Unsigned32
_AxsAccessFilterStatsInMirrorSequenceNumber_Object = MibTableColumn
axsAccessFilterStatsInMirrorSequenceNumber = _AxsAccessFilterStatsInMirrorSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 9, 1, 4),
    _AxsAccessFilterStatsInMirrorSequenceNumber_Type()
)
axsAccessFilterStatsInMirrorSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMirrorSequenceNumber.setStatus("mandatory")
_AxsAccessFilterStatsInMirrorListName_Type = DisplayString
_AxsAccessFilterStatsInMirrorListName_Object = MibTableColumn
axsAccessFilterStatsInMirrorListName = _AxsAccessFilterStatsInMirrorListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 9, 1, 5),
    _AxsAccessFilterStatsInMirrorListName_Type()
)
axsAccessFilterStatsInMirrorListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMirrorListName.setStatus("mandatory")
_AxsAccessFilterStatsInMirrorMatchedPackets_Type = Counter64
_AxsAccessFilterStatsInMirrorMatchedPackets_Object = MibTableColumn
axsAccessFilterStatsInMirrorMatchedPackets = _AxsAccessFilterStatsInMirrorMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 9, 1, 6),
    _AxsAccessFilterStatsInMirrorMatchedPackets_Type()
)
axsAccessFilterStatsInMirrorMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMirrorMatchedPackets.setStatus("mandatory")
_AxsQosFlowStats_ObjectIdentity = ObjectIdentity
axsQosFlowStats = _AxsQosFlowStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11)
)
_AxsQosFlowStatsInTable_Object = MibTable
axsQosFlowStatsInTable = _AxsQosFlowStatsInTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1)
)
if mibBuilder.loadTexts:
    axsQosFlowStatsInTable.setStatus("mandatory")
_AxsQosFlowStatsInEntry_Object = MibTableRow
axsQosFlowStatsInEntry = _AxsQosFlowStatsInEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1)
)
axsQosFlowStatsInEntry.setIndexNames(
    (0, "AX4630S", "axsQosFlowStatsInifIndex"),
    (0, "AX4630S", "axsQosFlowStatsInifIndexType"),
    (0, "AX4630S", "axsQosFlowStatsInListIndex"),
    (0, "AX4630S", "axsQosFlowStatsInSequenceNumber"),
)
if mibBuilder.loadTexts:
    axsQosFlowStatsInEntry.setStatus("mandatory")
_AxsQosFlowStatsInifIndex_Type = Integer32
_AxsQosFlowStatsInifIndex_Object = MibTableColumn
axsQosFlowStatsInifIndex = _AxsQosFlowStatsInifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 1),
    _AxsQosFlowStatsInifIndex_Type()
)
axsQosFlowStatsInifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsQosFlowStatsInifIndex.setStatus("mandatory")
_AxsQosFlowStatsInifIndexType_Type = Integer32
_AxsQosFlowStatsInifIndexType_Object = MibTableColumn
axsQosFlowStatsInifIndexType = _AxsQosFlowStatsInifIndexType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 2),
    _AxsQosFlowStatsInifIndexType_Type()
)
axsQosFlowStatsInifIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsQosFlowStatsInifIndexType.setStatus("mandatory")
_AxsQosFlowStatsInListIndex_Type = Unsigned32
_AxsQosFlowStatsInListIndex_Object = MibTableColumn
axsQosFlowStatsInListIndex = _AxsQosFlowStatsInListIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 3),
    _AxsQosFlowStatsInListIndex_Type()
)
axsQosFlowStatsInListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsQosFlowStatsInListIndex.setStatus("mandatory")
_AxsQosFlowStatsInSequenceNumber_Type = Unsigned32
_AxsQosFlowStatsInSequenceNumber_Object = MibTableColumn
axsQosFlowStatsInSequenceNumber = _AxsQosFlowStatsInSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 4),
    _AxsQosFlowStatsInSequenceNumber_Type()
)
axsQosFlowStatsInSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsQosFlowStatsInSequenceNumber.setStatus("mandatory")
_AxsQosFlowStatsInListName_Type = DisplayString
_AxsQosFlowStatsInListName_Object = MibTableColumn
axsQosFlowStatsInListName = _AxsQosFlowStatsInListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 5),
    _AxsQosFlowStatsInListName_Type()
)
axsQosFlowStatsInListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInListName.setStatus("mandatory")
_AxsQosFlowStatsInMatchedPackets_Type = Counter64
_AxsQosFlowStatsInMatchedPackets_Object = MibTableColumn
axsQosFlowStatsInMatchedPackets = _AxsQosFlowStatsInMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 6),
    _AxsQosFlowStatsInMatchedPackets_Type()
)
axsQosFlowStatsInMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPackets.setStatus("mandatory")
_AxsQosFlowStatsInMatchedPacketsMinUnder_Type = Counter64
_AxsQosFlowStatsInMatchedPacketsMinUnder_Object = MibTableColumn
axsQosFlowStatsInMatchedPacketsMinUnder = _AxsQosFlowStatsInMatchedPacketsMinUnder_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 7),
    _AxsQosFlowStatsInMatchedPacketsMinUnder_Type()
)
axsQosFlowStatsInMatchedPacketsMinUnder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPacketsMinUnder.setStatus("mandatory")
_AxsQosFlowStatsInMatchedPacketsMinOver_Type = Counter64
_AxsQosFlowStatsInMatchedPacketsMinOver_Object = MibTableColumn
axsQosFlowStatsInMatchedPacketsMinOver = _AxsQosFlowStatsInMatchedPacketsMinOver_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 8),
    _AxsQosFlowStatsInMatchedPacketsMinOver_Type()
)
axsQosFlowStatsInMatchedPacketsMinOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPacketsMinOver.setStatus("mandatory")
_AxsQosFlowStatsInMatchedPacketsMaxUnder_Type = Counter64
_AxsQosFlowStatsInMatchedPacketsMaxUnder_Object = MibTableColumn
axsQosFlowStatsInMatchedPacketsMaxUnder = _AxsQosFlowStatsInMatchedPacketsMaxUnder_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 9),
    _AxsQosFlowStatsInMatchedPacketsMaxUnder_Type()
)
axsQosFlowStatsInMatchedPacketsMaxUnder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPacketsMaxUnder.setStatus("mandatory")
_AxsQosFlowStatsInMatchedPacketsMaxOver_Type = Counter64
_AxsQosFlowStatsInMatchedPacketsMaxOver_Object = MibTableColumn
axsQosFlowStatsInMatchedPacketsMaxOver = _AxsQosFlowStatsInMatchedPacketsMaxOver_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 10),
    _AxsQosFlowStatsInMatchedPacketsMaxOver_Type()
)
axsQosFlowStatsInMatchedPacketsMaxOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPacketsMaxOver.setStatus("mandatory")
_AxsL2ld_ObjectIdentity = ObjectIdentity
axsL2ld = _AxsL2ld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10)
)
_AxsL2ldGlobalInfo_ObjectIdentity = ObjectIdentity
axsL2ldGlobalInfo = _AxsL2ldGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1)
)
_AxsL2ldVersion_Type = Integer32
_AxsL2ldVersion_Object = MibScalar
axsL2ldVersion = _AxsL2ldVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1, 1),
    _AxsL2ldVersion_Type()
)
axsL2ldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldVersion.setStatus("mandatory")
_AxsL2ldLoopDetectionId_Type = Integer32
_AxsL2ldLoopDetectionId_Object = MibScalar
axsL2ldLoopDetectionId = _AxsL2ldLoopDetectionId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1, 2),
    _AxsL2ldLoopDetectionId_Type()
)
axsL2ldLoopDetectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldLoopDetectionId.setStatus("mandatory")
_AxsL2ldIntervalTime_Type = Integer32
_AxsL2ldIntervalTime_Object = MibScalar
axsL2ldIntervalTime = _AxsL2ldIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1, 3),
    _AxsL2ldIntervalTime_Type()
)
axsL2ldIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldIntervalTime.setStatus("mandatory")
_AxsL2ldOutputRate_Type = Integer32
_AxsL2ldOutputRate_Object = MibScalar
axsL2ldOutputRate = _AxsL2ldOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1, 4),
    _AxsL2ldOutputRate_Type()
)
axsL2ldOutputRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldOutputRate.setStatus("mandatory")
_AxsL2ldThreshold_Type = Integer32
_AxsL2ldThreshold_Object = MibScalar
axsL2ldThreshold = _AxsL2ldThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1, 5),
    _AxsL2ldThreshold_Type()
)
axsL2ldThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldThreshold.setStatus("mandatory")
_AxsL2ldHoldTime_Type = Integer32
_AxsL2ldHoldTime_Object = MibScalar
axsL2ldHoldTime = _AxsL2ldHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1, 6),
    _AxsL2ldHoldTime_Type()
)
axsL2ldHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldHoldTime.setStatus("mandatory")
_AxsL2ldAutoRestoreTime_Type = Integer32
_AxsL2ldAutoRestoreTime_Object = MibScalar
axsL2ldAutoRestoreTime = _AxsL2ldAutoRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1, 7),
    _AxsL2ldAutoRestoreTime_Type()
)
axsL2ldAutoRestoreTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldAutoRestoreTime.setStatus("mandatory")
_AxsL2ldConfigurationVlanPortCounts_Type = Integer32
_AxsL2ldConfigurationVlanPortCounts_Object = MibScalar
axsL2ldConfigurationVlanPortCounts = _AxsL2ldConfigurationVlanPortCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1, 8),
    _AxsL2ldConfigurationVlanPortCounts_Type()
)
axsL2ldConfigurationVlanPortCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldConfigurationVlanPortCounts.setStatus("mandatory")
_AxsL2ldCapacityVlanPortCounts_Type = Integer32
_AxsL2ldCapacityVlanPortCounts_Object = MibScalar
axsL2ldCapacityVlanPortCounts = _AxsL2ldCapacityVlanPortCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 1, 9),
    _AxsL2ldCapacityVlanPortCounts_Type()
)
axsL2ldCapacityVlanPortCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldCapacityVlanPortCounts.setStatus("mandatory")
_AxsL2ldPortTable_Object = MibTable
axsL2ldPortTable = _AxsL2ldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    axsL2ldPortTable.setStatus("mandatory")
_AxsL2ldPortEntry_Object = MibTableRow
axsL2ldPortEntry = _AxsL2ldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1)
)
axsL2ldPortEntry.setIndexNames(
    (0, "AX4630S", "axsL2ldPortIndex"),
    (0, "AX4630S", "axsL2ldPortIfIndex"),
)
if mibBuilder.loadTexts:
    axsL2ldPortEntry.setStatus("mandatory")
_AxsL2ldPortIndex_Type = Integer32
_AxsL2ldPortIndex_Object = MibTableColumn
axsL2ldPortIndex = _AxsL2ldPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 1),
    _AxsL2ldPortIndex_Type()
)
axsL2ldPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortIndex.setStatus("mandatory")
_AxsL2ldPortIfIndex_Type = Integer32
_AxsL2ldPortIfIndex_Object = MibTableColumn
axsL2ldPortIfIndex = _AxsL2ldPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 2),
    _AxsL2ldPortIfIndex_Type()
)
axsL2ldPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortIfIndex.setStatus("mandatory")


class _AxsL2ldPortStatus_Type(Integer32):
    """Custom type axsL2ldPortStatus based on Integer32"""
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
          ("loopDown", 3))
    )


_AxsL2ldPortStatus_Type.__name__ = "Integer32"
_AxsL2ldPortStatus_Object = MibTableColumn
axsL2ldPortStatus = _AxsL2ldPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 3),
    _AxsL2ldPortStatus_Type()
)
axsL2ldPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortStatus.setStatus("mandatory")


class _AxsL2ldPortType_Type(Integer32):
    """Custom type axsL2ldPortType based on Integer32"""
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
        *(("trap", 1),
          ("sendInact", 2),
          ("send", 3),
          ("upLink", 4),
          ("exception", 5))
    )


_AxsL2ldPortType_Type.__name__ = "Integer32"
_AxsL2ldPortType_Object = MibTableColumn
axsL2ldPortType = _AxsL2ldPortType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 4),
    _AxsL2ldPortType_Type()
)
axsL2ldPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortType.setStatus("mandatory")
_AxsL2ldPortDetectCount_Type = Integer32
_AxsL2ldPortDetectCount_Object = MibTableColumn
axsL2ldPortDetectCount = _AxsL2ldPortDetectCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 5),
    _AxsL2ldPortDetectCount_Type()
)
axsL2ldPortDetectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortDetectCount.setStatus("mandatory")
_AxsL2ldPortAutoRestoringTimer_Type = Integer32
_AxsL2ldPortAutoRestoringTimer_Object = MibTableColumn
axsL2ldPortAutoRestoringTimer = _AxsL2ldPortAutoRestoringTimer_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 6),
    _AxsL2ldPortAutoRestoringTimer_Type()
)
axsL2ldPortAutoRestoringTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortAutoRestoringTimer.setStatus("mandatory")
_AxsL2ldPortSourcePortIfindex_Type = Integer32
_AxsL2ldPortSourcePortIfindex_Object = MibTableColumn
axsL2ldPortSourcePortIfindex = _AxsL2ldPortSourcePortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 7),
    _AxsL2ldPortSourcePortIfindex_Type()
)
axsL2ldPortSourcePortIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortSourcePortIfindex.setStatus("mandatory")
_AxsL2ldPortDestinationPortIfindex_Type = Integer32
_AxsL2ldPortDestinationPortIfindex_Object = MibTableColumn
axsL2ldPortDestinationPortIfindex = _AxsL2ldPortDestinationPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 8),
    _AxsL2ldPortDestinationPortIfindex_Type()
)
axsL2ldPortDestinationPortIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortDestinationPortIfindex.setStatus("mandatory")
_AxsL2ldPortSourceVlan_Type = Integer32
_AxsL2ldPortSourceVlan_Object = MibTableColumn
axsL2ldPortSourceVlan = _AxsL2ldPortSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 9),
    _AxsL2ldPortSourceVlan_Type()
)
axsL2ldPortSourceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortSourceVlan.setStatus("mandatory")
_AxsL2ldPortHCInFrames_Type = Counter64
_AxsL2ldPortHCInFrames_Object = MibTableColumn
axsL2ldPortHCInFrames = _AxsL2ldPortHCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 10),
    _AxsL2ldPortHCInFrames_Type()
)
axsL2ldPortHCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortHCInFrames.setStatus("mandatory")
_AxsL2ldPortHCOutFrames_Type = Counter64
_AxsL2ldPortHCOutFrames_Object = MibTableColumn
axsL2ldPortHCOutFrames = _AxsL2ldPortHCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 11),
    _AxsL2ldPortHCOutFrames_Type()
)
axsL2ldPortHCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortHCOutFrames.setStatus("mandatory")
_AxsL2ldPortHCInDiscards_Type = Counter64
_AxsL2ldPortHCInDiscards_Object = MibTableColumn
axsL2ldPortHCInDiscards = _AxsL2ldPortHCInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 12),
    _AxsL2ldPortHCInDiscards_Type()
)
axsL2ldPortHCInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortHCInDiscards.setStatus("mandatory")
_AxsL2ldPortInactiveCount_Type = Integer32
_AxsL2ldPortInactiveCount_Object = MibTableColumn
axsL2ldPortInactiveCount = _AxsL2ldPortInactiveCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 13),
    _AxsL2ldPortInactiveCount_Type()
)
axsL2ldPortInactiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortInactiveCount.setStatus("mandatory")
_AxsL2ldPortLastInactiveTime_Type = TimeStamp
_AxsL2ldPortLastInactiveTime_Object = MibTableColumn
axsL2ldPortLastInactiveTime = _AxsL2ldPortLastInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 14),
    _AxsL2ldPortLastInactiveTime_Type()
)
axsL2ldPortLastInactiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortLastInactiveTime.setStatus("mandatory")
_AxsL2ldPortLastInFramesTime_Type = TimeStamp
_AxsL2ldPortLastInFramesTime_Object = MibTableColumn
axsL2ldPortLastInFramesTime = _AxsL2ldPortLastInFramesTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 10, 2, 1, 15),
    _AxsL2ldPortLastInFramesTime_Type()
)
axsL2ldPortLastInFramesTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsL2ldPortLastInFramesTime.setStatus("mandatory")
_AxsVrf_ObjectIdentity = ObjectIdentity
axsVrf = _AxsVrf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11)
)
_AxsVrfIp_ObjectIdentity = ObjectIdentity
axsVrfIp = _AxsVrfIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1)
)
_AxsVrfIpAddrTable_Object = MibTable
axsVrfIpAddrTable = _AxsVrfIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    axsVrfIpAddrTable.setStatus("mandatory")
_AxsVrfIpAddrEntry_Object = MibTableRow
axsVrfIpAddrEntry = _AxsVrfIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 1, 1)
)
axsVrfIpAddrEntry.setIndexNames(
    (0, "AX4630S", "axsVrfIpAddrVrfIndex"),
    (0, "AX4630S", "axsVrfIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    axsVrfIpAddrEntry.setStatus("mandatory")
_AxsVrfIpAddrVrfIndex_Type = Integer32
_AxsVrfIpAddrVrfIndex_Object = MibTableColumn
axsVrfIpAddrVrfIndex = _AxsVrfIpAddrVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 1, 1, 1),
    _AxsVrfIpAddrVrfIndex_Type()
)
axsVrfIpAddrVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpAddrVrfIndex.setStatus("mandatory")
_AxsVrfIpAdEntAddr_Type = IpAddress
_AxsVrfIpAdEntAddr_Object = MibTableColumn
axsVrfIpAdEntAddr = _AxsVrfIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 1, 1, 2),
    _AxsVrfIpAdEntAddr_Type()
)
axsVrfIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpAdEntAddr.setStatus("mandatory")
_AxsVrfIpAdEntIfIndex_Type = Integer32
_AxsVrfIpAdEntIfIndex_Object = MibTableColumn
axsVrfIpAdEntIfIndex = _AxsVrfIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 1, 1, 3),
    _AxsVrfIpAdEntIfIndex_Type()
)
axsVrfIpAdEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpAdEntIfIndex.setStatus("mandatory")
_AxsVrfIpAdEntNetMask_Type = IpAddress
_AxsVrfIpAdEntNetMask_Object = MibTableColumn
axsVrfIpAdEntNetMask = _AxsVrfIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 1, 1, 4),
    _AxsVrfIpAdEntNetMask_Type()
)
axsVrfIpAdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpAdEntNetMask.setStatus("mandatory")
_AxsVrfIpAdEntBcastAddr_Type = Integer32
_AxsVrfIpAdEntBcastAddr_Object = MibTableColumn
axsVrfIpAdEntBcastAddr = _AxsVrfIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 1, 1, 5),
    _AxsVrfIpAdEntBcastAddr_Type()
)
axsVrfIpAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpAdEntBcastAddr.setStatus("mandatory")
_AxsVrfIpAdEntReasmMaxSize_Type = Integer32
_AxsVrfIpAdEntReasmMaxSize_Object = MibTableColumn
axsVrfIpAdEntReasmMaxSize = _AxsVrfIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 1, 1, 6),
    _AxsVrfIpAdEntReasmMaxSize_Type()
)
axsVrfIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpAdEntReasmMaxSize.setStatus("mandatory")
_AxsVrfIpAdEntDescr_Type = DisplayString
_AxsVrfIpAdEntDescr_Object = MibTableColumn
axsVrfIpAdEntDescr = _AxsVrfIpAdEntDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 1, 1, 7),
    _AxsVrfIpAdEntDescr_Type()
)
axsVrfIpAdEntDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpAdEntDescr.setStatus("mandatory")
_AxsVrfIpNetToMediaTable_Object = MibTable
axsVrfIpNetToMediaTable = _AxsVrfIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    axsVrfIpNetToMediaTable.setStatus("mandatory")
_AxsVrfIpNetToMediaEntry_Object = MibTableRow
axsVrfIpNetToMediaEntry = _AxsVrfIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 2, 1)
)
axsVrfIpNetToMediaEntry.setIndexNames(
    (0, "AX4630S", "axsVrfIpNetMediaVrfIndex"),
    (0, "AX4630S", "axsVrfIpNetToMediaIfIndex"),
    (0, "AX4630S", "axsVrfIpNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    axsVrfIpNetToMediaEntry.setStatus("mandatory")
_AxsVrfIpNetMediaVrfIndex_Type = Integer32
_AxsVrfIpNetMediaVrfIndex_Object = MibTableColumn
axsVrfIpNetMediaVrfIndex = _AxsVrfIpNetMediaVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 2, 1, 1),
    _AxsVrfIpNetMediaVrfIndex_Type()
)
axsVrfIpNetMediaVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpNetMediaVrfIndex.setStatus("mandatory")
_AxsVrfIpNetToMediaIfIndex_Type = Integer32
_AxsVrfIpNetToMediaIfIndex_Object = MibTableColumn
axsVrfIpNetToMediaIfIndex = _AxsVrfIpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 2, 1, 2),
    _AxsVrfIpNetToMediaIfIndex_Type()
)
axsVrfIpNetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpNetToMediaIfIndex.setStatus("mandatory")
_AxsVrfIpNetToMediaPhysAddress_Type = PhysAddress
_AxsVrfIpNetToMediaPhysAddress_Object = MibTableColumn
axsVrfIpNetToMediaPhysAddress = _AxsVrfIpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 2, 1, 3),
    _AxsVrfIpNetToMediaPhysAddress_Type()
)
axsVrfIpNetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpNetToMediaPhysAddress.setStatus("mandatory")
_AxsVrfIpNetToMediaNetAddress_Type = IpAddress
_AxsVrfIpNetToMediaNetAddress_Object = MibTableColumn
axsVrfIpNetToMediaNetAddress = _AxsVrfIpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 2, 1, 4),
    _AxsVrfIpNetToMediaNetAddress_Type()
)
axsVrfIpNetToMediaNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpNetToMediaNetAddress.setStatus("mandatory")


class _AxsVrfIpNetToMediaType_Type(Integer32):
    """Custom type axsVrfIpNetToMediaType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4))
    )


_AxsVrfIpNetToMediaType_Type.__name__ = "Integer32"
_AxsVrfIpNetToMediaType_Object = MibTableColumn
axsVrfIpNetToMediaType = _AxsVrfIpNetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 2, 1, 5),
    _AxsVrfIpNetToMediaType_Type()
)
axsVrfIpNetToMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpNetToMediaType.setStatus("mandatory")
_AxsVrfIpNetToMediaDescr_Type = DisplayString
_AxsVrfIpNetToMediaDescr_Object = MibTableColumn
axsVrfIpNetToMediaDescr = _AxsVrfIpNetToMediaDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 1, 2, 1, 6),
    _AxsVrfIpNetToMediaDescr_Type()
)
axsVrfIpNetToMediaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpNetToMediaDescr.setStatus("mandatory")
_AxsVrfIpForward_ObjectIdentity = ObjectIdentity
axsVrfIpForward = _AxsVrfIpForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2)
)
_AxsVrfIpFwNoTable_Object = MibTable
axsVrfIpFwNoTable = _AxsVrfIpFwNoTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    axsVrfIpFwNoTable.setStatus("mandatory")
_AxsVrfIpFwNoEntry_Object = MibTableRow
axsVrfIpFwNoEntry = _AxsVrfIpFwNoEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 1, 1)
)
axsVrfIpFwNoEntry.setIndexNames(
    (0, "AX4630S", "axsVrfIpFwNoVRFIndex"),
)
if mibBuilder.loadTexts:
    axsVrfIpFwNoEntry.setStatus("mandatory")
_AxsVrfIpFwNoVRFIndex_Type = Integer32
_AxsVrfIpFwNoVRFIndex_Object = MibTableColumn
axsVrfIpFwNoVRFIndex = _AxsVrfIpFwNoVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 1, 1, 1),
    _AxsVrfIpFwNoVRFIndex_Type()
)
axsVrfIpFwNoVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwNoVRFIndex.setStatus("mandatory")
_AxsVrfIpFwNo_Type = Integer32
_AxsVrfIpFwNo_Object = MibTableColumn
axsVrfIpFwNo = _AxsVrfIpFwNo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 1, 1, 2),
    _AxsVrfIpFwNo_Type()
)
axsVrfIpFwNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwNo.setStatus("mandatory")
_AxsVrfIpFwNoDescr_Type = DisplayString
_AxsVrfIpFwNoDescr_Object = MibTableColumn
axsVrfIpFwNoDescr = _AxsVrfIpFwNoDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 1, 1, 3),
    _AxsVrfIpFwNoDescr_Type()
)
axsVrfIpFwNoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwNoDescr.setStatus("mandatory")
_AxsVrfIpFwTable_Object = MibTable
axsVrfIpFwTable = _AxsVrfIpFwTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    axsVrfIpFwTable.setStatus("mandatory")
_AxsVrfIpFwEntry_Object = MibTableRow
axsVrfIpFwEntry = _AxsVrfIpFwEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1)
)
axsVrfIpFwEntry.setIndexNames(
    (0, "AX4630S", "axsVrfIpFwVRFIndex"),
    (0, "AX4630S", "axsVrfIpFwDest"),
    (0, "AX4630S", "axsVrfIpFwProto"),
    (0, "AX4630S", "axsVrfIpFwPolicy"),
    (0, "AX4630S", "axsVrfIpFwNextHop"),
)
if mibBuilder.loadTexts:
    axsVrfIpFwEntry.setStatus("mandatory")
_AxsVrfIpFwVRFIndex_Type = Integer32
_AxsVrfIpFwVRFIndex_Object = MibTableColumn
axsVrfIpFwVRFIndex = _AxsVrfIpFwVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 1),
    _AxsVrfIpFwVRFIndex_Type()
)
axsVrfIpFwVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwVRFIndex.setStatus("mandatory")
_AxsVrfIpFwDest_Type = IpAddress
_AxsVrfIpFwDest_Object = MibTableColumn
axsVrfIpFwDest = _AxsVrfIpFwDest_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 2),
    _AxsVrfIpFwDest_Type()
)
axsVrfIpFwDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwDest.setStatus("mandatory")
_AxsVrfIpFwMask_Type = IpAddress
_AxsVrfIpFwMask_Object = MibTableColumn
axsVrfIpFwMask = _AxsVrfIpFwMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 3),
    _AxsVrfIpFwMask_Type()
)
axsVrfIpFwMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwMask.setStatus("mandatory")
_AxsVrfIpFwPolicy_Type = Integer32
_AxsVrfIpFwPolicy_Object = MibTableColumn
axsVrfIpFwPolicy = _AxsVrfIpFwPolicy_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 4),
    _AxsVrfIpFwPolicy_Type()
)
axsVrfIpFwPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwPolicy.setStatus("mandatory")
_AxsVrfIpFwNextHop_Type = IpAddress
_AxsVrfIpFwNextHop_Object = MibTableColumn
axsVrfIpFwNextHop = _AxsVrfIpFwNextHop_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 5),
    _AxsVrfIpFwNextHop_Type()
)
axsVrfIpFwNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwNextHop.setStatus("mandatory")
_AxsVrfIpFwIfIndex_Type = Integer32
_AxsVrfIpFwIfIndex_Object = MibTableColumn
axsVrfIpFwIfIndex = _AxsVrfIpFwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 6),
    _AxsVrfIpFwIfIndex_Type()
)
axsVrfIpFwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwIfIndex.setStatus("mandatory")


class _AxsVrfIpFwType_Type(Integer32):
    """Custom type axsVrfIpFwType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("local", 3),
          ("remote", 4))
    )


_AxsVrfIpFwType_Type.__name__ = "Integer32"
_AxsVrfIpFwType_Object = MibTableColumn
axsVrfIpFwType = _AxsVrfIpFwType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 7),
    _AxsVrfIpFwType_Type()
)
axsVrfIpFwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwType.setStatus("mandatory")


class _AxsVrfIpFwProto_Type(Integer32):
    """Custom type axsVrfIpFwProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("rip", 8),
          ("ospf", 13),
          ("bgp", 14))
    )


_AxsVrfIpFwProto_Type.__name__ = "Integer32"
_AxsVrfIpFwProto_Object = MibTableColumn
axsVrfIpFwProto = _AxsVrfIpFwProto_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 8),
    _AxsVrfIpFwProto_Type()
)
axsVrfIpFwProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwProto.setStatus("mandatory")
_AxsVrfIpFwAge_Type = Integer32
_AxsVrfIpFwAge_Object = MibTableColumn
axsVrfIpFwAge = _AxsVrfIpFwAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 9),
    _AxsVrfIpFwAge_Type()
)
axsVrfIpFwAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwAge.setStatus("mandatory")
_AxsVrfIpFwInfo_Type = ObjectIdentifier
_AxsVrfIpFwInfo_Object = MibTableColumn
axsVrfIpFwInfo = _AxsVrfIpFwInfo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 10),
    _AxsVrfIpFwInfo_Type()
)
axsVrfIpFwInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwInfo.setStatus("mandatory")
_AxsVrfIpFwNextHopAS_Type = Integer32
_AxsVrfIpFwNextHopAS_Object = MibTableColumn
axsVrfIpFwNextHopAS = _AxsVrfIpFwNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 11),
    _AxsVrfIpFwNextHopAS_Type()
)
axsVrfIpFwNextHopAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwNextHopAS.setStatus("mandatory")
_AxsVrfIpFwMetric1_Type = Integer32
_AxsVrfIpFwMetric1_Object = MibTableColumn
axsVrfIpFwMetric1 = _AxsVrfIpFwMetric1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 12),
    _AxsVrfIpFwMetric1_Type()
)
axsVrfIpFwMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwMetric1.setStatus("mandatory")
_AxsVrfIpFwMetric2_Type = Integer32
_AxsVrfIpFwMetric2_Object = MibTableColumn
axsVrfIpFwMetric2 = _AxsVrfIpFwMetric2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 13),
    _AxsVrfIpFwMetric2_Type()
)
axsVrfIpFwMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwMetric2.setStatus("mandatory")
_AxsVrfIpFwMetric3_Type = Integer32
_AxsVrfIpFwMetric3_Object = MibTableColumn
axsVrfIpFwMetric3 = _AxsVrfIpFwMetric3_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 14),
    _AxsVrfIpFwMetric3_Type()
)
axsVrfIpFwMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwMetric3.setStatus("mandatory")
_AxsVrfIpFwMetric4_Type = Integer32
_AxsVrfIpFwMetric4_Object = MibTableColumn
axsVrfIpFwMetric4 = _AxsVrfIpFwMetric4_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 15),
    _AxsVrfIpFwMetric4_Type()
)
axsVrfIpFwMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwMetric4.setStatus("mandatory")
_AxsVrfIpFwMetric5_Type = Integer32
_AxsVrfIpFwMetric5_Object = MibTableColumn
axsVrfIpFwMetric5 = _AxsVrfIpFwMetric5_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 16),
    _AxsVrfIpFwMetric5_Type()
)
axsVrfIpFwMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwMetric5.setStatus("mandatory")
_AxsVrfIpFwDescr_Type = DisplayString
_AxsVrfIpFwDescr_Object = MibTableColumn
axsVrfIpFwDescr = _AxsVrfIpFwDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 2, 2, 1, 17),
    _AxsVrfIpFwDescr_Type()
)
axsVrfIpFwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpFwDescr.setStatus("mandatory")
_AxsVrfIpv6_ObjectIdentity = ObjectIdentity
axsVrfIpv6 = _AxsVrfIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3)
)
_AxsVrfIpv6AddrTable_Object = MibTable
axsVrfIpv6AddrTable = _AxsVrfIpv6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    axsVrfIpv6AddrTable.setStatus("mandatory")
_AxsVrfIpv6AddrEntry_Object = MibTableRow
axsVrfIpv6AddrEntry = _AxsVrfIpv6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1, 1)
)
axsVrfIpv6AddrEntry.setIndexNames(
    (0, "AX4630S", "axsVrfIpv6AddrVrfIndex"),
    (0, "AX4630S", "axsVrfIpv6AddrIfIndex"),
    (0, "AX4630S", "axsVrfIpv6AddrAddress"),
)
if mibBuilder.loadTexts:
    axsVrfIpv6AddrEntry.setStatus("mandatory")
_AxsVrfIpv6AddrVrfIndex_Type = Integer32
_AxsVrfIpv6AddrVrfIndex_Object = MibTableColumn
axsVrfIpv6AddrVrfIndex = _AxsVrfIpv6AddrVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1, 1, 1),
    _AxsVrfIpv6AddrVrfIndex_Type()
)
axsVrfIpv6AddrVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrVrfIndex.setStatus("mandatory")
_AxsVrfIpv6AddrIfIndex_Type = Integer32
_AxsVrfIpv6AddrIfIndex_Object = MibTableColumn
axsVrfIpv6AddrIfIndex = _AxsVrfIpv6AddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1, 1, 2),
    _AxsVrfIpv6AddrIfIndex_Type()
)
axsVrfIpv6AddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrIfIndex.setStatus("mandatory")
_AxsVrfIpv6AddrAddress_Type = Ipv6Address
_AxsVrfIpv6AddrAddress_Object = MibTableColumn
axsVrfIpv6AddrAddress = _AxsVrfIpv6AddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1, 1, 3),
    _AxsVrfIpv6AddrAddress_Type()
)
axsVrfIpv6AddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrAddress.setStatus("mandatory")


class _AxsVrfIpv6AddrPfxLength_Type(Integer32):
    """Custom type axsVrfIpv6AddrPfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AxsVrfIpv6AddrPfxLength_Type.__name__ = "Integer32"
_AxsVrfIpv6AddrPfxLength_Object = MibTableColumn
axsVrfIpv6AddrPfxLength = _AxsVrfIpv6AddrPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1, 1, 4),
    _AxsVrfIpv6AddrPfxLength_Type()
)
axsVrfIpv6AddrPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPfxLength.setStatus("mandatory")


class _AxsVrfIpv6AddrType_Type(Integer32):
    """Custom type axsVrfIpv6AddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateless", 1),
          ("stateful", 2),
          ("unknown", 3))
    )


_AxsVrfIpv6AddrType_Type.__name__ = "Integer32"
_AxsVrfIpv6AddrType_Object = MibTableColumn
axsVrfIpv6AddrType = _AxsVrfIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1, 1, 5),
    _AxsVrfIpv6AddrType_Type()
)
axsVrfIpv6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrType.setStatus("mandatory")
_AxsVrfIpv6AddrAnycastFlag_Type = TruthValue
_AxsVrfIpv6AddrAnycastFlag_Object = MibTableColumn
axsVrfIpv6AddrAnycastFlag = _AxsVrfIpv6AddrAnycastFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1, 1, 6),
    _AxsVrfIpv6AddrAnycastFlag_Type()
)
axsVrfIpv6AddrAnycastFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrAnycastFlag.setStatus("mandatory")


class _AxsVrfIpv6AddrStatus_Type(Integer32):
    """Custom type axsVrfIpv6AddrStatus based on Integer32"""
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
        *(("preferred", 1),
          ("deprecated", 2),
          ("invalid", 3),
          ("inaccessible", 4),
          ("unknown", 5))
    )


_AxsVrfIpv6AddrStatus_Type.__name__ = "Integer32"
_AxsVrfIpv6AddrStatus_Object = MibTableColumn
axsVrfIpv6AddrStatus = _AxsVrfIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1, 1, 7),
    _AxsVrfIpv6AddrStatus_Type()
)
axsVrfIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrStatus.setStatus("mandatory")
_AxsVrfIpv6AddrDescr_Type = DisplayString
_AxsVrfIpv6AddrDescr_Object = MibTableColumn
axsVrfIpv6AddrDescr = _AxsVrfIpv6AddrDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 1, 1, 8),
    _AxsVrfIpv6AddrDescr_Type()
)
axsVrfIpv6AddrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrDescr.setStatus("mandatory")
_AxsVrfIpv6AddrPrefixTable_Object = MibTable
axsVrfIpv6AddrPrefixTable = _AxsVrfIpv6AddrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2)
)
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefixTable.setStatus("mandatory")
_AxsVrfIpv6AddrPrefixEntry_Object = MibTableRow
axsVrfIpv6AddrPrefixEntry = _AxsVrfIpv6AddrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2, 1)
)
axsVrfIpv6AddrPrefixEntry.setIndexNames(
    (0, "AX4630S", "axsVrfIpv6AddrPrefixVrfIndex"),
    (0, "AX4630S", "axsVrfIpv6AddrPrefixIfIndex"),
    (0, "AX4630S", "axsVrfIpv6AddrPrefix"),
    (0, "AX4630S", "axsVrfIpv6AddrPrefixLength"),
)
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefixEntry.setStatus("mandatory")
_AxsVrfIpv6AddrPrefixVrfIndex_Type = Integer32
_AxsVrfIpv6AddrPrefixVrfIndex_Object = MibTableColumn
axsVrfIpv6AddrPrefixVrfIndex = _AxsVrfIpv6AddrPrefixVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2, 1, 1),
    _AxsVrfIpv6AddrPrefixVrfIndex_Type()
)
axsVrfIpv6AddrPrefixVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefixVrfIndex.setStatus("mandatory")
_AxsVrfIpv6AddrPrefixIfIndex_Type = Integer32
_AxsVrfIpv6AddrPrefixIfIndex_Object = MibTableColumn
axsVrfIpv6AddrPrefixIfIndex = _AxsVrfIpv6AddrPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2, 1, 2),
    _AxsVrfIpv6AddrPrefixIfIndex_Type()
)
axsVrfIpv6AddrPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefixIfIndex.setStatus("mandatory")
_AxsVrfIpv6AddrPrefix_Type = Ipv6AddressPrefix
_AxsVrfIpv6AddrPrefix_Object = MibTableColumn
axsVrfIpv6AddrPrefix = _AxsVrfIpv6AddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2, 1, 3),
    _AxsVrfIpv6AddrPrefix_Type()
)
axsVrfIpv6AddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefix.setStatus("mandatory")


class _AxsVrfIpv6AddrPrefixLength_Type(Integer32):
    """Custom type axsVrfIpv6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AxsVrfIpv6AddrPrefixLength_Type.__name__ = "Integer32"
_AxsVrfIpv6AddrPrefixLength_Object = MibTableColumn
axsVrfIpv6AddrPrefixLength = _AxsVrfIpv6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2, 1, 4),
    _AxsVrfIpv6AddrPrefixLength_Type()
)
axsVrfIpv6AddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefixLength.setStatus("mandatory")
_AxsVrfIpv6AddrPrefixOnLinkFlag_Type = TruthValue
_AxsVrfIpv6AddrPrefixOnLinkFlag_Object = MibTableColumn
axsVrfIpv6AddrPrefixOnLinkFlag = _AxsVrfIpv6AddrPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2, 1, 5),
    _AxsVrfIpv6AddrPrefixOnLinkFlag_Type()
)
axsVrfIpv6AddrPrefixOnLinkFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefixOnLinkFlag.setStatus("mandatory")
_AxsVrfIpv6AddrPrefixAutonomousFlag_Type = TruthValue
_AxsVrfIpv6AddrPrefixAutonomousFlag_Object = MibTableColumn
axsVrfIpv6AddrPrefixAutonomousFlag = _AxsVrfIpv6AddrPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2, 1, 6),
    _AxsVrfIpv6AddrPrefixAutonomousFlag_Type()
)
axsVrfIpv6AddrPrefixAutonomousFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefixAutonomousFlag.setStatus("mandatory")
_AxsVrfIpv6AddrPrefixAdvPreferredLifetime_Type = Unsigned32
_AxsVrfIpv6AddrPrefixAdvPreferredLifetime_Object = MibTableColumn
axsVrfIpv6AddrPrefixAdvPreferredLifetime = _AxsVrfIpv6AddrPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2, 1, 7),
    _AxsVrfIpv6AddrPrefixAdvPreferredLifetime_Type()
)
axsVrfIpv6AddrPrefixAdvPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefixAdvPreferredLifetime.setStatus("mandatory")
_AxsVrfIpv6AddrPrefixAdvValidLifetime_Type = Unsigned32
_AxsVrfIpv6AddrPrefixAdvValidLifetime_Object = MibTableColumn
axsVrfIpv6AddrPrefixAdvValidLifetime = _AxsVrfIpv6AddrPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 2, 1, 8),
    _AxsVrfIpv6AddrPrefixAdvValidLifetime_Type()
)
axsVrfIpv6AddrPrefixAdvValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6AddrPrefixAdvValidLifetime.setStatus("mandatory")
_AxsVrfIpv6NetToMediaTable_Object = MibTable
axsVrfIpv6NetToMediaTable = _AxsVrfIpv6NetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    axsVrfIpv6NetToMediaTable.setStatus("mandatory")
_AxsVrfIpv6NetToMediaEntry_Object = MibTableRow
axsVrfIpv6NetToMediaEntry = _AxsVrfIpv6NetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1)
)
axsVrfIpv6NetToMediaEntry.setIndexNames(
    (0, "AX4630S", "axsVrfIpv6NetToMediaVrfIndex"),
    (0, "AX4630S", "axsVrfIpv6NetToMediaIfIndex"),
    (0, "AX4630S", "axsVrfIpv6NetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    axsVrfIpv6NetToMediaEntry.setStatus("mandatory")
_AxsVrfIpv6NetToMediaVrfIndex_Type = Integer32
_AxsVrfIpv6NetToMediaVrfIndex_Object = MibTableColumn
axsVrfIpv6NetToMediaVrfIndex = _AxsVrfIpv6NetToMediaVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1, 1),
    _AxsVrfIpv6NetToMediaVrfIndex_Type()
)
axsVrfIpv6NetToMediaVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6NetToMediaVrfIndex.setStatus("mandatory")
_AxsVrfIpv6NetToMediaIfIndex_Type = Integer32
_AxsVrfIpv6NetToMediaIfIndex_Object = MibTableColumn
axsVrfIpv6NetToMediaIfIndex = _AxsVrfIpv6NetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1, 2),
    _AxsVrfIpv6NetToMediaIfIndex_Type()
)
axsVrfIpv6NetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6NetToMediaIfIndex.setStatus("mandatory")
_AxsVrfIpv6NetToMediaNetAddress_Type = Ipv6Address
_AxsVrfIpv6NetToMediaNetAddress_Object = MibTableColumn
axsVrfIpv6NetToMediaNetAddress = _AxsVrfIpv6NetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1, 3),
    _AxsVrfIpv6NetToMediaNetAddress_Type()
)
axsVrfIpv6NetToMediaNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6NetToMediaNetAddress.setStatus("mandatory")
_AxsVrfIpv6NetToMediaPhysAddress_Type = PhysAddress
_AxsVrfIpv6NetToMediaPhysAddress_Object = MibTableColumn
axsVrfIpv6NetToMediaPhysAddress = _AxsVrfIpv6NetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1, 4),
    _AxsVrfIpv6NetToMediaPhysAddress_Type()
)
axsVrfIpv6NetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6NetToMediaPhysAddress.setStatus("mandatory")


class _AxsVrfIpv6NetToMediaType_Type(Integer32):
    """Custom type axsVrfIpv6NetToMediaType based on Integer32"""
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
        *(("other", 1),
          ("dynamic", 2),
          ("static", 3),
          ("local", 4))
    )


_AxsVrfIpv6NetToMediaType_Type.__name__ = "Integer32"
_AxsVrfIpv6NetToMediaType_Object = MibTableColumn
axsVrfIpv6NetToMediaType = _AxsVrfIpv6NetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1, 5),
    _AxsVrfIpv6NetToMediaType_Type()
)
axsVrfIpv6NetToMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6NetToMediaType.setStatus("mandatory")


class _AxsVrfIpv6IfNetToMediaState_Type(Integer32):
    """Custom type axsVrfIpv6IfNetToMediaState based on Integer32"""
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
        *(("reachable", 1),
          ("stale", 2),
          ("delay", 3),
          ("probe", 4),
          ("invalid", 5),
          ("unknown", 6))
    )


_AxsVrfIpv6IfNetToMediaState_Type.__name__ = "Integer32"
_AxsVrfIpv6IfNetToMediaState_Object = MibTableColumn
axsVrfIpv6IfNetToMediaState = _AxsVrfIpv6IfNetToMediaState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1, 6),
    _AxsVrfIpv6IfNetToMediaState_Type()
)
axsVrfIpv6IfNetToMediaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6IfNetToMediaState.setStatus("mandatory")
_AxsVrfIpv6IfNetToMediaLastUpdated_Type = TimeStamp
_AxsVrfIpv6IfNetToMediaLastUpdated_Object = MibTableColumn
axsVrfIpv6IfNetToMediaLastUpdated = _AxsVrfIpv6IfNetToMediaLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1, 7),
    _AxsVrfIpv6IfNetToMediaLastUpdated_Type()
)
axsVrfIpv6IfNetToMediaLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6IfNetToMediaLastUpdated.setStatus("mandatory")
_AxsVrfIpv6NetToMediaValid_Type = TruthValue
_AxsVrfIpv6NetToMediaValid_Object = MibTableColumn
axsVrfIpv6NetToMediaValid = _AxsVrfIpv6NetToMediaValid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1, 8),
    _AxsVrfIpv6NetToMediaValid_Type()
)
axsVrfIpv6NetToMediaValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6NetToMediaValid.setStatus("mandatory")
_AxsVrfIpv6NetToMediaDescr_Type = DisplayString
_AxsVrfIpv6NetToMediaDescr_Object = MibTableColumn
axsVrfIpv6NetToMediaDescr = _AxsVrfIpv6NetToMediaDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 3, 3, 1, 9),
    _AxsVrfIpv6NetToMediaDescr_Type()
)
axsVrfIpv6NetToMediaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6NetToMediaDescr.setStatus("mandatory")
_AxsVrfIpv6Forward_ObjectIdentity = ObjectIdentity
axsVrfIpv6Forward = _AxsVrfIpv6Forward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4)
)
_AxsVrfIpv6FwNoTable_Object = MibTable
axsVrfIpv6FwNoTable = _AxsVrfIpv6FwNoTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 1)
)
if mibBuilder.loadTexts:
    axsVrfIpv6FwNoTable.setStatus("mandatory")
_AxsVrfIpv6FwNoEntry_Object = MibTableRow
axsVrfIpv6FwNoEntry = _AxsVrfIpv6FwNoEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 1, 1)
)
axsVrfIpv6FwNoEntry.setIndexNames(
    (0, "AX4630S", "axsVrfIpv6FwNoVRFIndex"),
)
if mibBuilder.loadTexts:
    axsVrfIpv6FwNoEntry.setStatus("mandatory")
_AxsVrfIpv6FwNoVRFIndex_Type = Integer32
_AxsVrfIpv6FwNoVRFIndex_Object = MibTableColumn
axsVrfIpv6FwNoVRFIndex = _AxsVrfIpv6FwNoVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 1, 1, 1),
    _AxsVrfIpv6FwNoVRFIndex_Type()
)
axsVrfIpv6FwNoVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwNoVRFIndex.setStatus("mandatory")
_AxsVrfIpv6FwNo_Type = Integer32
_AxsVrfIpv6FwNo_Object = MibTableColumn
axsVrfIpv6FwNo = _AxsVrfIpv6FwNo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 1, 1, 2),
    _AxsVrfIpv6FwNo_Type()
)
axsVrfIpv6FwNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwNo.setStatus("mandatory")
_AxsVrfIpv6FwNoDescr_Type = DisplayString
_AxsVrfIpv6FwNoDescr_Object = MibTableColumn
axsVrfIpv6FwNoDescr = _AxsVrfIpv6FwNoDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 1, 1, 3),
    _AxsVrfIpv6FwNoDescr_Type()
)
axsVrfIpv6FwNoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwNoDescr.setStatus("mandatory")
_AxsVrfIpv6FwTable_Object = MibTable
axsVrfIpv6FwTable = _AxsVrfIpv6FwTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2)
)
if mibBuilder.loadTexts:
    axsVrfIpv6FwTable.setStatus("mandatory")
_AxsVrfIpv6FwEntry_Object = MibTableRow
axsVrfIpv6FwEntry = _AxsVrfIpv6FwEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1)
)
axsVrfIpv6FwEntry.setIndexNames(
    (0, "AX4630S", "axsVrfIpv6FwVrfIndex"),
    (0, "AX4630S", "axsVrfIpv6FwDest"),
    (0, "AX4630S", "axsVrfIpv6FwProto"),
    (0, "AX4630S", "axsVrfIpv6FwPolicy"),
    (0, "AX4630S", "axsVrfIpv6FwNextHop"),
)
if mibBuilder.loadTexts:
    axsVrfIpv6FwEntry.setStatus("mandatory")
_AxsVrfIpv6FwVrfIndex_Type = Integer32
_AxsVrfIpv6FwVrfIndex_Object = MibTableColumn
axsVrfIpv6FwVrfIndex = _AxsVrfIpv6FwVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 1),
    _AxsVrfIpv6FwVrfIndex_Type()
)
axsVrfIpv6FwVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwVrfIndex.setStatus("mandatory")
_AxsVrfIpv6FwDest_Type = Ipv6Address
_AxsVrfIpv6FwDest_Object = MibTableColumn
axsVrfIpv6FwDest = _AxsVrfIpv6FwDest_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 2),
    _AxsVrfIpv6FwDest_Type()
)
axsVrfIpv6FwDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwDest.setStatus("mandatory")
_AxsVrfIpv6FwPfxLength_Type = Integer32
_AxsVrfIpv6FwPfxLength_Object = MibTableColumn
axsVrfIpv6FwPfxLength = _AxsVrfIpv6FwPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 3),
    _AxsVrfIpv6FwPfxLength_Type()
)
axsVrfIpv6FwPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwPfxLength.setStatus("mandatory")
_AxsVrfIpv6FwPolicy_Type = Integer32
_AxsVrfIpv6FwPolicy_Object = MibTableColumn
axsVrfIpv6FwPolicy = _AxsVrfIpv6FwPolicy_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 4),
    _AxsVrfIpv6FwPolicy_Type()
)
axsVrfIpv6FwPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwPolicy.setStatus("mandatory")
_AxsVrfIpv6FwNextHop_Type = Ipv6Address
_AxsVrfIpv6FwNextHop_Object = MibTableColumn
axsVrfIpv6FwNextHop = _AxsVrfIpv6FwNextHop_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 5),
    _AxsVrfIpv6FwNextHop_Type()
)
axsVrfIpv6FwNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwNextHop.setStatus("mandatory")
_AxsVrfIpv6FwIfIndex_Type = Integer32
_AxsVrfIpv6FwIfIndex_Object = MibTableColumn
axsVrfIpv6FwIfIndex = _AxsVrfIpv6FwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 6),
    _AxsVrfIpv6FwIfIndex_Type()
)
axsVrfIpv6FwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwIfIndex.setStatus("mandatory")


class _AxsVrfIpv6FwType_Type(Integer32):
    """Custom type axsVrfIpv6FwType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("local", 3),
          ("remote", 4))
    )


_AxsVrfIpv6FwType_Type.__name__ = "Integer32"
_AxsVrfIpv6FwType_Object = MibTableColumn
axsVrfIpv6FwType = _AxsVrfIpv6FwType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 7),
    _AxsVrfIpv6FwType_Type()
)
axsVrfIpv6FwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwType.setStatus("mandatory")


class _AxsVrfIpv6FwProto_Type(Integer32):
    """Custom type axsVrfIpv6FwProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("rip", 8),
          ("ospf", 13),
          ("bgp", 14))
    )


_AxsVrfIpv6FwProto_Type.__name__ = "Integer32"
_AxsVrfIpv6FwProto_Object = MibTableColumn
axsVrfIpv6FwProto = _AxsVrfIpv6FwProto_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 8),
    _AxsVrfIpv6FwProto_Type()
)
axsVrfIpv6FwProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwProto.setStatus("mandatory")
_AxsVrfIpv6FwAge_Type = Integer32
_AxsVrfIpv6FwAge_Object = MibTableColumn
axsVrfIpv6FwAge = _AxsVrfIpv6FwAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 9),
    _AxsVrfIpv6FwAge_Type()
)
axsVrfIpv6FwAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwAge.setStatus("mandatory")
_AxsVrfIpv6FwInfo_Type = ObjectIdentifier
_AxsVrfIpv6FwInfo_Object = MibTableColumn
axsVrfIpv6FwInfo = _AxsVrfIpv6FwInfo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 10),
    _AxsVrfIpv6FwInfo_Type()
)
axsVrfIpv6FwInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwInfo.setStatus("mandatory")
_AxsVrfIpv6FwNextHopAS_Type = Integer32
_AxsVrfIpv6FwNextHopAS_Object = MibTableColumn
axsVrfIpv6FwNextHopAS = _AxsVrfIpv6FwNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 11),
    _AxsVrfIpv6FwNextHopAS_Type()
)
axsVrfIpv6FwNextHopAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwNextHopAS.setStatus("mandatory")
_AxsVrfIpv6FwMetric1_Type = Integer32
_AxsVrfIpv6FwMetric1_Object = MibTableColumn
axsVrfIpv6FwMetric1 = _AxsVrfIpv6FwMetric1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 12),
    _AxsVrfIpv6FwMetric1_Type()
)
axsVrfIpv6FwMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwMetric1.setStatus("mandatory")
_AxsVrfIpv6FwMetric2_Type = Integer32
_AxsVrfIpv6FwMetric2_Object = MibTableColumn
axsVrfIpv6FwMetric2 = _AxsVrfIpv6FwMetric2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 13),
    _AxsVrfIpv6FwMetric2_Type()
)
axsVrfIpv6FwMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwMetric2.setStatus("mandatory")
_AxsVrfIpv6FwMetric3_Type = Integer32
_AxsVrfIpv6FwMetric3_Object = MibTableColumn
axsVrfIpv6FwMetric3 = _AxsVrfIpv6FwMetric3_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 14),
    _AxsVrfIpv6FwMetric3_Type()
)
axsVrfIpv6FwMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwMetric3.setStatus("mandatory")
_AxsVrfIpv6FwMetric4_Type = Integer32
_AxsVrfIpv6FwMetric4_Object = MibTableColumn
axsVrfIpv6FwMetric4 = _AxsVrfIpv6FwMetric4_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 15),
    _AxsVrfIpv6FwMetric4_Type()
)
axsVrfIpv6FwMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwMetric4.setStatus("mandatory")
_AxsVrfIpv6FwMetric5_Type = Integer32
_AxsVrfIpv6FwMetric5_Object = MibTableColumn
axsVrfIpv6FwMetric5 = _AxsVrfIpv6FwMetric5_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 16),
    _AxsVrfIpv6FwMetric5_Type()
)
axsVrfIpv6FwMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwMetric5.setStatus("mandatory")
_AxsVrfIpv6FwDescr_Type = DisplayString
_AxsVrfIpv6FwDescr_Object = MibTableColumn
axsVrfIpv6FwDescr = _AxsVrfIpv6FwDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 11, 4, 2, 1, 17),
    _AxsVrfIpv6FwDescr_Type()
)
axsVrfIpv6FwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVrfIpv6FwDescr.setStatus("mandatory")
_AxsOspf_ObjectIdentity = ObjectIdentity
axsOspf = _AxsOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14)
)
_AxsOspfGeneralTable_Object = MibTable
axsOspfGeneralTable = _AxsOspfGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    axsOspfGeneralTable.setStatus("mandatory")
_AxsOspfGeneralEntry_Object = MibTableRow
axsOspfGeneralEntry = _AxsOspfGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1)
)
axsOspfGeneralEntry.setIndexNames(
    (0, "AX4630S", "axsOspfGeneralDomainNumber"),
)
if mibBuilder.loadTexts:
    axsOspfGeneralEntry.setStatus("mandatory")
_AxsOspfGeneralDomainNumber_Type = Integer32
_AxsOspfGeneralDomainNumber_Object = MibTableColumn
axsOspfGeneralDomainNumber = _AxsOspfGeneralDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 1),
    _AxsOspfGeneralDomainNumber_Type()
)
axsOspfGeneralDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfGeneralDomainNumber.setStatus("mandatory")
_AxsOspfRouterId_Type = IpAddress
_AxsOspfRouterId_Object = MibTableColumn
axsOspfRouterId = _AxsOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 2),
    _AxsOspfRouterId_Type()
)
axsOspfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfRouterId.setStatus("mandatory")


class _AxsOspfAdminStat_Type(Integer32):
    """Custom type axsOspfAdminStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AxsOspfAdminStat_Type.__name__ = "Integer32"
_AxsOspfAdminStat_Object = MibTableColumn
axsOspfAdminStat = _AxsOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 3),
    _AxsOspfAdminStat_Type()
)
axsOspfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAdminStat.setStatus("mandatory")
_AxsOspfVersionNumber_Type = Integer32
_AxsOspfVersionNumber_Object = MibTableColumn
axsOspfVersionNumber = _AxsOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 4),
    _AxsOspfVersionNumber_Type()
)
axsOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVersionNumber.setStatus("mandatory")


class _AxsOspfAreaBdrRtrStatus_Type(Integer32):
    """Custom type axsOspfAreaBdrRtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AxsOspfAreaBdrRtrStatus_Type.__name__ = "Integer32"
_AxsOspfAreaBdrRtrStatus_Object = MibTableColumn
axsOspfAreaBdrRtrStatus = _AxsOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 5),
    _AxsOspfAreaBdrRtrStatus_Type()
)
axsOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaBdrRtrStatus.setStatus("mandatory")


class _AxsOspfASBdrRtrStatus_Type(Integer32):
    """Custom type axsOspfASBdrRtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AxsOspfASBdrRtrStatus_Type.__name__ = "Integer32"
_AxsOspfASBdrRtrStatus_Object = MibTableColumn
axsOspfASBdrRtrStatus = _AxsOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 6),
    _AxsOspfASBdrRtrStatus_Type()
)
axsOspfASBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfASBdrRtrStatus.setStatus("mandatory")
_AxsOspfExternLsaCount_Type = Gauge32
_AxsOspfExternLsaCount_Object = MibTableColumn
axsOspfExternLsaCount = _AxsOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 7),
    _AxsOspfExternLsaCount_Type()
)
axsOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExternLsaCount.setStatus("mandatory")
_AxsOspfExternLsaCksumSum_Type = Integer32
_AxsOspfExternLsaCksumSum_Object = MibTableColumn
axsOspfExternLsaCksumSum = _AxsOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 8),
    _AxsOspfExternLsaCksumSum_Type()
)
axsOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExternLsaCksumSum.setStatus("mandatory")


class _AxsOspfTOSSupport_Type(Integer32):
    """Custom type axsOspfTOSSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AxsOspfTOSSupport_Type.__name__ = "Integer32"
_AxsOspfTOSSupport_Object = MibTableColumn
axsOspfTOSSupport = _AxsOspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 9),
    _AxsOspfTOSSupport_Type()
)
axsOspfTOSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfTOSSupport.setStatus("mandatory")
_AxsOspfOriginateNewLsas_Type = Counter32
_AxsOspfOriginateNewLsas_Object = MibTableColumn
axsOspfOriginateNewLsas = _AxsOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 10),
    _AxsOspfOriginateNewLsas_Type()
)
axsOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfOriginateNewLsas.setStatus("mandatory")
_AxsOspfRxNewLsas_Type = Counter32
_AxsOspfRxNewLsas_Object = MibTableColumn
axsOspfRxNewLsas = _AxsOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 11),
    _AxsOspfRxNewLsas_Type()
)
axsOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfRxNewLsas.setStatus("mandatory")
_AxsOspfExtLsdbLimit_Type = Integer32
_AxsOspfExtLsdbLimit_Object = MibTableColumn
axsOspfExtLsdbLimit = _AxsOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 12),
    _AxsOspfExtLsdbLimit_Type()
)
axsOspfExtLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbLimit.setStatus("mandatory")
_AxsOspfMulticastExtensions_Type = Integer32
_AxsOspfMulticastExtensions_Object = MibTableColumn
axsOspfMulticastExtensions = _AxsOspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 13),
    _AxsOspfMulticastExtensions_Type()
)
axsOspfMulticastExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfMulticastExtensions.setStatus("mandatory")
_AxsOspfAreaTable_Object = MibTable
axsOspfAreaTable = _AxsOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2)
)
if mibBuilder.loadTexts:
    axsOspfAreaTable.setStatus("mandatory")
_AxsOspfAreaEntry_Object = MibTableRow
axsOspfAreaEntry = _AxsOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1)
)
axsOspfAreaEntry.setIndexNames(
    (0, "AX4630S", "axsOspfAreaDomainNumber"),
    (0, "AX4630S", "axsOspfAreaId"),
)
if mibBuilder.loadTexts:
    axsOspfAreaEntry.setStatus("mandatory")
_AxsOspfAreaDomainNumber_Type = Integer32
_AxsOspfAreaDomainNumber_Object = MibTableColumn
axsOspfAreaDomainNumber = _AxsOspfAreaDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 1),
    _AxsOspfAreaDomainNumber_Type()
)
axsOspfAreaDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaDomainNumber.setStatus("mandatory")
_AxsOspfAreaId_Type = IpAddress
_AxsOspfAreaId_Object = MibTableColumn
axsOspfAreaId = _AxsOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 2),
    _AxsOspfAreaId_Type()
)
axsOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaId.setStatus("mandatory")
_AxsOspfAuthType_Type = Integer32
_AxsOspfAuthType_Object = MibTableColumn
axsOspfAuthType = _AxsOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 3),
    _AxsOspfAuthType_Type()
)
axsOspfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAuthType.setStatus("mandatory")


class _AxsOspfImportAsExtern_Type(Integer32):
    """Custom type axsOspfImportAsExtern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_AxsOspfImportAsExtern_Type.__name__ = "Integer32"
_AxsOspfImportAsExtern_Object = MibTableColumn
axsOspfImportAsExtern = _AxsOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 4),
    _AxsOspfImportAsExtern_Type()
)
axsOspfImportAsExtern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfImportAsExtern.setStatus("mandatory")
_AxsOspfSpfRuns_Type = Counter32
_AxsOspfSpfRuns_Object = MibTableColumn
axsOspfSpfRuns = _AxsOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 5),
    _AxsOspfSpfRuns_Type()
)
axsOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfSpfRuns.setStatus("mandatory")
_AxsOspfAreaBdrRtrCount_Type = Gauge32
_AxsOspfAreaBdrRtrCount_Object = MibTableColumn
axsOspfAreaBdrRtrCount = _AxsOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 6),
    _AxsOspfAreaBdrRtrCount_Type()
)
axsOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaBdrRtrCount.setStatus("mandatory")
_AxsOspfAsBdrRtrCount_Type = Gauge32
_AxsOspfAsBdrRtrCount_Object = MibTableColumn
axsOspfAsBdrRtrCount = _AxsOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 7),
    _AxsOspfAsBdrRtrCount_Type()
)
axsOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAsBdrRtrCount.setStatus("mandatory")
_AxsOspfAreaLsaCount_Type = Gauge32
_AxsOspfAreaLsaCount_Object = MibTableColumn
axsOspfAreaLsaCount = _AxsOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 8),
    _AxsOspfAreaLsaCount_Type()
)
axsOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaLsaCount.setStatus("mandatory")
_AxsOspfAreaLsaCksumSum_Type = Integer32
_AxsOspfAreaLsaCksumSum_Object = MibTableColumn
axsOspfAreaLsaCksumSum = _AxsOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 9),
    _AxsOspfAreaLsaCksumSum_Type()
)
axsOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaLsaCksumSum.setStatus("mandatory")


class _AxsOspfAreaSummary_Type(Integer32):
    """Custom type axsOspfAreaSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_AxsOspfAreaSummary_Type.__name__ = "Integer32"
_AxsOspfAreaSummary_Object = MibTableColumn
axsOspfAreaSummary = _AxsOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 10),
    _AxsOspfAreaSummary_Type()
)
axsOspfAreaSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaSummary.setStatus("mandatory")


class _AxsOspfAreaStatus_Type(Integer32):
    """Custom type axsOspfAreaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_AxsOspfAreaStatus_Type.__name__ = "Integer32"
_AxsOspfAreaStatus_Object = MibTableColumn
axsOspfAreaStatus = _AxsOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 11),
    _AxsOspfAreaStatus_Type()
)
axsOspfAreaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaStatus.setStatus("mandatory")
_AxsOspfStubAreaTable_Object = MibTable
axsOspfStubAreaTable = _AxsOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3)
)
if mibBuilder.loadTexts:
    axsOspfStubAreaTable.setStatus("mandatory")
_AxsOspfStubAreaEntry_Object = MibTableRow
axsOspfStubAreaEntry = _AxsOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1)
)
axsOspfStubAreaEntry.setIndexNames(
    (0, "AX4630S", "axsOspfStubDomainNumber"),
    (0, "AX4630S", "axsOspfStubAreaId"),
    (0, "AX4630S", "axsOspfStubTOS"),
)
if mibBuilder.loadTexts:
    axsOspfStubAreaEntry.setStatus("mandatory")
_AxsOspfStubDomainNumber_Type = Integer32
_AxsOspfStubDomainNumber_Object = MibTableColumn
axsOspfStubDomainNumber = _AxsOspfStubDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 1),
    _AxsOspfStubDomainNumber_Type()
)
axsOspfStubDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubDomainNumber.setStatus("mandatory")
_AxsOspfStubAreaId_Type = IpAddress
_AxsOspfStubAreaId_Object = MibTableColumn
axsOspfStubAreaId = _AxsOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 2),
    _AxsOspfStubAreaId_Type()
)
axsOspfStubAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubAreaId.setStatus("mandatory")
_AxsOspfStubTOS_Type = Integer32
_AxsOspfStubTOS_Object = MibTableColumn
axsOspfStubTOS = _AxsOspfStubTOS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 3),
    _AxsOspfStubTOS_Type()
)
axsOspfStubTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubTOS.setStatus("mandatory")
_AxsOspfStubMetric_Type = Integer32
_AxsOspfStubMetric_Object = MibTableColumn
axsOspfStubMetric = _AxsOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 4),
    _AxsOspfStubMetric_Type()
)
axsOspfStubMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubMetric.setStatus("mandatory")


class _AxsOspfStubStatus_Type(Integer32):
    """Custom type axsOspfStubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_AxsOspfStubStatus_Type.__name__ = "Integer32"
_AxsOspfStubStatus_Object = MibTableColumn
axsOspfStubStatus = _AxsOspfStubStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 5),
    _AxsOspfStubStatus_Type()
)
axsOspfStubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubStatus.setStatus("mandatory")


class _AxsOspfStubMetricType_Type(Integer32):
    """Custom type axsOspfStubMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ospfMetric", 1),
          ("comparableCost", 2),
          ("nonComparable", 3))
    )


_AxsOspfStubMetricType_Type.__name__ = "Integer32"
_AxsOspfStubMetricType_Object = MibTableColumn
axsOspfStubMetricType = _AxsOspfStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 6),
    _AxsOspfStubMetricType_Type()
)
axsOspfStubMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubMetricType.setStatus("mandatory")
_AxsOspfLsdbTable_Object = MibTable
axsOspfLsdbTable = _AxsOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4)
)
if mibBuilder.loadTexts:
    axsOspfLsdbTable.setStatus("mandatory")
_AxsOspfLsdbEntry_Object = MibTableRow
axsOspfLsdbEntry = _AxsOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1)
)
axsOspfLsdbEntry.setIndexNames(
    (0, "AX4630S", "axsOspfLsdbDomainNumber"),
    (0, "AX4630S", "axsOspfLsdbAreaId"),
    (0, "AX4630S", "axsOspfLsdbType"),
    (0, "AX4630S", "axsOspfLsdbLsid"),
    (0, "AX4630S", "axsOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    axsOspfLsdbEntry.setStatus("mandatory")
_AxsOspfLsdbDomainNumber_Type = Integer32
_AxsOspfLsdbDomainNumber_Object = MibTableColumn
axsOspfLsdbDomainNumber = _AxsOspfLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 1),
    _AxsOspfLsdbDomainNumber_Type()
)
axsOspfLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbDomainNumber.setStatus("mandatory")
_AxsOspfLsdbAreaId_Type = IpAddress
_AxsOspfLsdbAreaId_Object = MibTableColumn
axsOspfLsdbAreaId = _AxsOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 2),
    _AxsOspfLsdbAreaId_Type()
)
axsOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbAreaId.setStatus("mandatory")


class _AxsOspfLsdbType_Type(Integer32):
    """Custom type axsOspfLsdbType based on Integer32"""
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
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7))
    )


_AxsOspfLsdbType_Type.__name__ = "Integer32"
_AxsOspfLsdbType_Object = MibTableColumn
axsOspfLsdbType = _AxsOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 3),
    _AxsOspfLsdbType_Type()
)
axsOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbType.setStatus("mandatory")
_AxsOspfLsdbLsid_Type = IpAddress
_AxsOspfLsdbLsid_Object = MibTableColumn
axsOspfLsdbLsid = _AxsOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 4),
    _AxsOspfLsdbLsid_Type()
)
axsOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbLsid.setStatus("mandatory")
_AxsOspfLsdbRouterId_Type = IpAddress
_AxsOspfLsdbRouterId_Object = MibTableColumn
axsOspfLsdbRouterId = _AxsOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 5),
    _AxsOspfLsdbRouterId_Type()
)
axsOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbRouterId.setStatus("mandatory")
_AxsOspfLsdbSequence_Type = Integer32
_AxsOspfLsdbSequence_Object = MibTableColumn
axsOspfLsdbSequence = _AxsOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 6),
    _AxsOspfLsdbSequence_Type()
)
axsOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbSequence.setStatus("mandatory")
_AxsOspfLsdbAge_Type = Integer32
_AxsOspfLsdbAge_Object = MibTableColumn
axsOspfLsdbAge = _AxsOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 7),
    _AxsOspfLsdbAge_Type()
)
axsOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbAge.setStatus("mandatory")
_AxsOspfLsdbChecksum_Type = Integer32
_AxsOspfLsdbChecksum_Object = MibTableColumn
axsOspfLsdbChecksum = _AxsOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 8),
    _AxsOspfLsdbChecksum_Type()
)
axsOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbChecksum.setStatus("mandatory")
_AxsOspfLsdbAdvertisement_Type = OctetString
_AxsOspfLsdbAdvertisement_Object = MibTableColumn
axsOspfLsdbAdvertisement = _AxsOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 9),
    _AxsOspfLsdbAdvertisement_Type()
)
axsOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbAdvertisement.setStatus("mandatory")
_AxsOspfAreaRangeTable_Object = MibTable
axsOspfAreaRangeTable = _AxsOspfAreaRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5)
)
if mibBuilder.loadTexts:
    axsOspfAreaRangeTable.setStatus("mandatory")
_AxsOspfAreaRangeEntry_Object = MibTableRow
axsOspfAreaRangeEntry = _AxsOspfAreaRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1)
)
axsOspfAreaRangeEntry.setIndexNames(
    (0, "AX4630S", "axsOspfAreaRangeDomainNumber"),
    (0, "AX4630S", "axsOspfAreaRangeAreaId"),
    (0, "AX4630S", "axsOspfAreaRangeNet"),
)
if mibBuilder.loadTexts:
    axsOspfAreaRangeEntry.setStatus("mandatory")
_AxsOspfAreaRangeDomainNumber_Type = Integer32
_AxsOspfAreaRangeDomainNumber_Object = MibTableColumn
axsOspfAreaRangeDomainNumber = _AxsOspfAreaRangeDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 1),
    _AxsOspfAreaRangeDomainNumber_Type()
)
axsOspfAreaRangeDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeDomainNumber.setStatus("mandatory")
_AxsOspfAreaRangeAreaId_Type = IpAddress
_AxsOspfAreaRangeAreaId_Object = MibTableColumn
axsOspfAreaRangeAreaId = _AxsOspfAreaRangeAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 2),
    _AxsOspfAreaRangeAreaId_Type()
)
axsOspfAreaRangeAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeAreaId.setStatus("mandatory")
_AxsOspfAreaRangeNet_Type = IpAddress
_AxsOspfAreaRangeNet_Object = MibTableColumn
axsOspfAreaRangeNet = _AxsOspfAreaRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 3),
    _AxsOspfAreaRangeNet_Type()
)
axsOspfAreaRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeNet.setStatus("mandatory")
_AxsOspfAreaRangeMask_Type = IpAddress
_AxsOspfAreaRangeMask_Object = MibTableColumn
axsOspfAreaRangeMask = _AxsOspfAreaRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 4),
    _AxsOspfAreaRangeMask_Type()
)
axsOspfAreaRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeMask.setStatus("mandatory")


class _AxsOspfAreaRangeStatus_Type(Integer32):
    """Custom type axsOspfAreaRangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AxsOspfAreaRangeStatus_Type.__name__ = "Integer32"
_AxsOspfAreaRangeStatus_Object = MibTableColumn
axsOspfAreaRangeStatus = _AxsOspfAreaRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 5),
    _AxsOspfAreaRangeStatus_Type()
)
axsOspfAreaRangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeStatus.setStatus("mandatory")


class _AxsOspfAreaRangeEffect_Type(Integer32):
    """Custom type axsOspfAreaRangeEffect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2))
    )


_AxsOspfAreaRangeEffect_Type.__name__ = "Integer32"
_AxsOspfAreaRangeEffect_Object = MibTableColumn
axsOspfAreaRangeEffect = _AxsOspfAreaRangeEffect_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 6),
    _AxsOspfAreaRangeEffect_Type()
)
axsOspfAreaRangeEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeEffect.setStatus("mandatory")
_AxsOspfIfTable_Object = MibTable
axsOspfIfTable = _AxsOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7)
)
if mibBuilder.loadTexts:
    axsOspfIfTable.setStatus("mandatory")
_AxsOspfIfEntry_Object = MibTableRow
axsOspfIfEntry = _AxsOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1)
)
axsOspfIfEntry.setIndexNames(
    (0, "AX4630S", "axsOspfIfDomainNumber"),
    (0, "AX4630S", "axsOspfIfIpAddress"),
    (0, "AX4630S", "axsOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    axsOspfIfEntry.setStatus("mandatory")
_AxsOspfIfDomainNumber_Type = Integer32
_AxsOspfIfDomainNumber_Object = MibTableColumn
axsOspfIfDomainNumber = _AxsOspfIfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 1),
    _AxsOspfIfDomainNumber_Type()
)
axsOspfIfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfDomainNumber.setStatus("mandatory")
_AxsOspfIfIpAddress_Type = IpAddress
_AxsOspfIfIpAddress_Object = MibTableColumn
axsOspfIfIpAddress = _AxsOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 2),
    _AxsOspfIfIpAddress_Type()
)
axsOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfIpAddress.setStatus("mandatory")
_AxsOspfAddressLessIf_Type = Integer32
_AxsOspfAddressLessIf_Object = MibTableColumn
axsOspfAddressLessIf = _AxsOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 3),
    _AxsOspfAddressLessIf_Type()
)
axsOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAddressLessIf.setStatus("mandatory")
_AxsOspfIfAreaId_Type = IpAddress
_AxsOspfIfAreaId_Object = MibTableColumn
axsOspfIfAreaId = _AxsOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 4),
    _AxsOspfIfAreaId_Type()
)
axsOspfIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfAreaId.setStatus("mandatory")


class _AxsOspfIfType_Type(Integer32):
    """Custom type axsOspfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3),
          ("pointToMultipoint", 5))
    )


_AxsOspfIfType_Type.__name__ = "Integer32"
_AxsOspfIfType_Object = MibTableColumn
axsOspfIfType = _AxsOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 5),
    _AxsOspfIfType_Type()
)
axsOspfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfType.setStatus("mandatory")


class _AxsOspfIfAdminStat_Type(Integer32):
    """Custom type axsOspfIfAdminStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AxsOspfIfAdminStat_Type.__name__ = "Integer32"
_AxsOspfIfAdminStat_Object = MibTableColumn
axsOspfIfAdminStat = _AxsOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 6),
    _AxsOspfIfAdminStat_Type()
)
axsOspfIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfAdminStat.setStatus("mandatory")
_AxsOspfIfRtrPriority_Type = Integer32
_AxsOspfIfRtrPriority_Object = MibTableColumn
axsOspfIfRtrPriority = _AxsOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 7),
    _AxsOspfIfRtrPriority_Type()
)
axsOspfIfRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfRtrPriority.setStatus("mandatory")
_AxsOspfIfTransitDelay_Type = Integer32
_AxsOspfIfTransitDelay_Object = MibTableColumn
axsOspfIfTransitDelay = _AxsOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 8),
    _AxsOspfIfTransitDelay_Type()
)
axsOspfIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfTransitDelay.setStatus("mandatory")
_AxsOspfIfRetransInterval_Type = Integer32
_AxsOspfIfRetransInterval_Object = MibTableColumn
axsOspfIfRetransInterval = _AxsOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 9),
    _AxsOspfIfRetransInterval_Type()
)
axsOspfIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfRetransInterval.setStatus("mandatory")
_AxsOspfIfHelloInterval_Type = Integer32
_AxsOspfIfHelloInterval_Object = MibTableColumn
axsOspfIfHelloInterval = _AxsOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 10),
    _AxsOspfIfHelloInterval_Type()
)
axsOspfIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfHelloInterval.setStatus("mandatory")
_AxsOspfIfRtrDeadInterval_Type = Integer32
_AxsOspfIfRtrDeadInterval_Object = MibTableColumn
axsOspfIfRtrDeadInterval = _AxsOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 11),
    _AxsOspfIfRtrDeadInterval_Type()
)
axsOspfIfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfRtrDeadInterval.setStatus("mandatory")
_AxsOspfIfPollInterval_Type = Integer32
_AxsOspfIfPollInterval_Object = MibTableColumn
axsOspfIfPollInterval = _AxsOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 12),
    _AxsOspfIfPollInterval_Type()
)
axsOspfIfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfPollInterval.setStatus("mandatory")


class _AxsOspfIfState_Type(Integer32):
    """Custom type axsOspfIfState based on Integer32"""
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
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_AxsOspfIfState_Type.__name__ = "Integer32"
_AxsOspfIfState_Object = MibTableColumn
axsOspfIfState = _AxsOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 13),
    _AxsOspfIfState_Type()
)
axsOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfState.setStatus("mandatory")
_AxsOspfIfDesignatedRouter_Type = IpAddress
_AxsOspfIfDesignatedRouter_Object = MibTableColumn
axsOspfIfDesignatedRouter = _AxsOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 14),
    _AxsOspfIfDesignatedRouter_Type()
)
axsOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfDesignatedRouter.setStatus("mandatory")
_AxsOspfIfBackupDesignatedRouter_Type = IpAddress
_AxsOspfIfBackupDesignatedRouter_Object = MibTableColumn
axsOspfIfBackupDesignatedRouter = _AxsOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 15),
    _AxsOspfIfBackupDesignatedRouter_Type()
)
axsOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfBackupDesignatedRouter.setStatus("mandatory")
_AxsOspfIfEvents_Type = Counter32
_AxsOspfIfEvents_Object = MibTableColumn
axsOspfIfEvents = _AxsOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 16),
    _AxsOspfIfEvents_Type()
)
axsOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfEvents.setStatus("mandatory")
_AxsOspfIfAuthKey_Type = OctetString
_AxsOspfIfAuthKey_Object = MibTableColumn
axsOspfIfAuthKey = _AxsOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 17),
    _AxsOspfIfAuthKey_Type()
)
axsOspfIfAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfAuthKey.setStatus("mandatory")


class _AxsOspfIfStatus_Type(Integer32):
    """Custom type axsOspfIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AxsOspfIfStatus_Type.__name__ = "Integer32"
_AxsOspfIfStatus_Object = MibTableColumn
axsOspfIfStatus = _AxsOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 18),
    _AxsOspfIfStatus_Type()
)
axsOspfIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfStatus.setStatus("mandatory")


class _AxsOspfIfMulticastForwarding_Type(Integer32):
    """Custom type axsOspfIfMulticastForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_AxsOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_AxsOspfIfMulticastForwarding_Object = MibTableColumn
axsOspfIfMulticastForwarding = _AxsOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 19),
    _AxsOspfIfMulticastForwarding_Type()
)
axsOspfIfMulticastForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMulticastForwarding.setStatus("mandatory")
_AxsOspfIfMetricTable_Object = MibTable
axsOspfIfMetricTable = _AxsOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8)
)
if mibBuilder.loadTexts:
    axsOspfIfMetricTable.setStatus("mandatory")
_AxsOspfIfMetricEntry_Object = MibTableRow
axsOspfIfMetricEntry = _AxsOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1)
)
axsOspfIfMetricEntry.setIndexNames(
    (0, "AX4630S", "axsOspfIfMetricDomainNumber"),
    (0, "AX4630S", "axsOspfIfMetricIpAddress"),
    (0, "AX4630S", "axsOspfIfMetricAddressLessIf"),
    (0, "AX4630S", "axsOspfIfMetricTOS"),
)
if mibBuilder.loadTexts:
    axsOspfIfMetricEntry.setStatus("mandatory")
_AxsOspfIfMetricDomainNumber_Type = Integer32
_AxsOspfIfMetricDomainNumber_Object = MibTableColumn
axsOspfIfMetricDomainNumber = _AxsOspfIfMetricDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 1),
    _AxsOspfIfMetricDomainNumber_Type()
)
axsOspfIfMetricDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricDomainNumber.setStatus("mandatory")
_AxsOspfIfMetricIpAddress_Type = IpAddress
_AxsOspfIfMetricIpAddress_Object = MibTableColumn
axsOspfIfMetricIpAddress = _AxsOspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 2),
    _AxsOspfIfMetricIpAddress_Type()
)
axsOspfIfMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricIpAddress.setStatus("mandatory")
_AxsOspfIfMetricAddressLessIf_Type = Integer32
_AxsOspfIfMetricAddressLessIf_Object = MibTableColumn
axsOspfIfMetricAddressLessIf = _AxsOspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 3),
    _AxsOspfIfMetricAddressLessIf_Type()
)
axsOspfIfMetricAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricAddressLessIf.setStatus("mandatory")
_AxsOspfIfMetricTOS_Type = Integer32
_AxsOspfIfMetricTOS_Object = MibTableColumn
axsOspfIfMetricTOS = _AxsOspfIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 4),
    _AxsOspfIfMetricTOS_Type()
)
axsOspfIfMetricTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricTOS.setStatus("mandatory")
_AxsOspfIfMetricValue_Type = Integer32
_AxsOspfIfMetricValue_Object = MibTableColumn
axsOspfIfMetricValue = _AxsOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 5),
    _AxsOspfIfMetricValue_Type()
)
axsOspfIfMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricValue.setStatus("mandatory")


class _AxsOspfIfMetricStatus_Type(Integer32):
    """Custom type axsOspfIfMetricStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_AxsOspfIfMetricStatus_Type.__name__ = "Integer32"
_AxsOspfIfMetricStatus_Object = MibTableColumn
axsOspfIfMetricStatus = _AxsOspfIfMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 6),
    _AxsOspfIfMetricStatus_Type()
)
axsOspfIfMetricStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricStatus.setStatus("mandatory")
_AxsOspfVirtIfTable_Object = MibTable
axsOspfVirtIfTable = _AxsOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9)
)
if mibBuilder.loadTexts:
    axsOspfVirtIfTable.setStatus("mandatory")
_AxsOspfVirtIfEntry_Object = MibTableRow
axsOspfVirtIfEntry = _AxsOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1)
)
axsOspfVirtIfEntry.setIndexNames(
    (0, "AX4630S", "axsOspfVirtIfDomainNumber"),
    (0, "AX4630S", "axsOspfVirtIfAreaId"),
    (0, "AX4630S", "axsOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    axsOspfVirtIfEntry.setStatus("mandatory")
_AxsOspfVirtIfDomainNumber_Type = Integer32
_AxsOspfVirtIfDomainNumber_Object = MibTableColumn
axsOspfVirtIfDomainNumber = _AxsOspfVirtIfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 1),
    _AxsOspfVirtIfDomainNumber_Type()
)
axsOspfVirtIfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfDomainNumber.setStatus("mandatory")
_AxsOspfVirtIfAreaId_Type = IpAddress
_AxsOspfVirtIfAreaId_Object = MibTableColumn
axsOspfVirtIfAreaId = _AxsOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 2),
    _AxsOspfVirtIfAreaId_Type()
)
axsOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfAreaId.setStatus("mandatory")
_AxsOspfVirtIfNeighbor_Type = IpAddress
_AxsOspfVirtIfNeighbor_Object = MibTableColumn
axsOspfVirtIfNeighbor = _AxsOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 3),
    _AxsOspfVirtIfNeighbor_Type()
)
axsOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfNeighbor.setStatus("mandatory")
_AxsOspfVirtIfTransitDelay_Type = Integer32
_AxsOspfVirtIfTransitDelay_Object = MibTableColumn
axsOspfVirtIfTransitDelay = _AxsOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 4),
    _AxsOspfVirtIfTransitDelay_Type()
)
axsOspfVirtIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfTransitDelay.setStatus("mandatory")
_AxsOspfVirtIfRetransInterval_Type = Integer32
_AxsOspfVirtIfRetransInterval_Object = MibTableColumn
axsOspfVirtIfRetransInterval = _AxsOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 5),
    _AxsOspfVirtIfRetransInterval_Type()
)
axsOspfVirtIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfRetransInterval.setStatus("mandatory")
_AxsOspfVirtIfHelloInterval_Type = Integer32
_AxsOspfVirtIfHelloInterval_Object = MibTableColumn
axsOspfVirtIfHelloInterval = _AxsOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 6),
    _AxsOspfVirtIfHelloInterval_Type()
)
axsOspfVirtIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfHelloInterval.setStatus("mandatory")
_AxsOspfVirtIfRtrDeadInterval_Type = Integer32
_AxsOspfVirtIfRtrDeadInterval_Object = MibTableColumn
axsOspfVirtIfRtrDeadInterval = _AxsOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 7),
    _AxsOspfVirtIfRtrDeadInterval_Type()
)
axsOspfVirtIfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfRtrDeadInterval.setStatus("mandatory")


class _AxsOspfVirtIfState_Type(Integer32):
    """Custom type axsOspfVirtIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_AxsOspfVirtIfState_Type.__name__ = "Integer32"
_AxsOspfVirtIfState_Object = MibTableColumn
axsOspfVirtIfState = _AxsOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 8),
    _AxsOspfVirtIfState_Type()
)
axsOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfState.setStatus("mandatory")
_AxsOspfVirtIfEvents_Type = Counter32
_AxsOspfVirtIfEvents_Object = MibTableColumn
axsOspfVirtIfEvents = _AxsOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 9),
    _AxsOspfVirtIfEvents_Type()
)
axsOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfEvents.setStatus("mandatory")
_AxsOspfVirtIfAuthKey_Type = OctetString
_AxsOspfVirtIfAuthKey_Object = MibTableColumn
axsOspfVirtIfAuthKey = _AxsOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 10),
    _AxsOspfVirtIfAuthKey_Type()
)
axsOspfVirtIfAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfAuthKey.setStatus("mandatory")


class _AxsOspfVirtIfStatus_Type(Integer32):
    """Custom type axsOspfVirtIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AxsOspfVirtIfStatus_Type.__name__ = "Integer32"
_AxsOspfVirtIfStatus_Object = MibTableColumn
axsOspfVirtIfStatus = _AxsOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 11),
    _AxsOspfVirtIfStatus_Type()
)
axsOspfVirtIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfStatus.setStatus("mandatory")
_AxsOspfNbrTable_Object = MibTable
axsOspfNbrTable = _AxsOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10)
)
if mibBuilder.loadTexts:
    axsOspfNbrTable.setStatus("mandatory")
_AxsOspfNbrEntry_Object = MibTableRow
axsOspfNbrEntry = _AxsOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1)
)
axsOspfNbrEntry.setIndexNames(
    (0, "AX4630S", "axsOspfNbrDomainNumber"),
    (0, "AX4630S", "axsOspfNbrIpAddr"),
    (0, "AX4630S", "axsOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    axsOspfNbrEntry.setStatus("mandatory")
_AxsOspfNbrDomainNumber_Type = Integer32
_AxsOspfNbrDomainNumber_Object = MibTableColumn
axsOspfNbrDomainNumber = _AxsOspfNbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 1),
    _AxsOspfNbrDomainNumber_Type()
)
axsOspfNbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrDomainNumber.setStatus("mandatory")
_AxsOspfNbrIpAddr_Type = IpAddress
_AxsOspfNbrIpAddr_Object = MibTableColumn
axsOspfNbrIpAddr = _AxsOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 2),
    _AxsOspfNbrIpAddr_Type()
)
axsOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrIpAddr.setStatus("mandatory")
_AxsOspfNbrAddressLessIndex_Type = Integer32
_AxsOspfNbrAddressLessIndex_Object = MibTableColumn
axsOspfNbrAddressLessIndex = _AxsOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 3),
    _AxsOspfNbrAddressLessIndex_Type()
)
axsOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrAddressLessIndex.setStatus("mandatory")
_AxsOspfNbrRtrId_Type = IpAddress
_AxsOspfNbrRtrId_Object = MibTableColumn
axsOspfNbrRtrId = _AxsOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 4),
    _AxsOspfNbrRtrId_Type()
)
axsOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrRtrId.setStatus("mandatory")
_AxsOspfNbrOptions_Type = Integer32
_AxsOspfNbrOptions_Object = MibTableColumn
axsOspfNbrOptions = _AxsOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 5),
    _AxsOspfNbrOptions_Type()
)
axsOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrOptions.setStatus("mandatory")
_AxsOspfNbrPriority_Type = Integer32
_AxsOspfNbrPriority_Object = MibTableColumn
axsOspfNbrPriority = _AxsOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 6),
    _AxsOspfNbrPriority_Type()
)
axsOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrPriority.setStatus("mandatory")


class _AxsOspfNbrState_Type(Integer32):
    """Custom type axsOspfNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_AxsOspfNbrState_Type.__name__ = "Integer32"
_AxsOspfNbrState_Object = MibTableColumn
axsOspfNbrState = _AxsOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 7),
    _AxsOspfNbrState_Type()
)
axsOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrState.setStatus("mandatory")
_AxsOspfNbrEvents_Type = Counter32
_AxsOspfNbrEvents_Object = MibTableColumn
axsOspfNbrEvents = _AxsOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 8),
    _AxsOspfNbrEvents_Type()
)
axsOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrEvents.setStatus("mandatory")
_AxsOspfNbrLsRetransQLen_Type = Gauge32
_AxsOspfNbrLsRetransQLen_Object = MibTableColumn
axsOspfNbrLsRetransQLen = _AxsOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 9),
    _AxsOspfNbrLsRetransQLen_Type()
)
axsOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrLsRetransQLen.setStatus("mandatory")


class _AxsOspfNbmaNbrStatus_Type(Integer32):
    """Custom type axsOspfNbmaNbrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_AxsOspfNbmaNbrStatus_Type.__name__ = "Integer32"
_AxsOspfNbmaNbrStatus_Object = MibTableColumn
axsOspfNbmaNbrStatus = _AxsOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 10),
    _AxsOspfNbmaNbrStatus_Type()
)
axsOspfNbmaNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbmaNbrStatus.setStatus("mandatory")


class _AxsOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type axsOspfNbmaNbrPermanence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_AxsOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_AxsOspfNbmaNbrPermanence_Object = MibTableColumn
axsOspfNbmaNbrPermanence = _AxsOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 11),
    _AxsOspfNbmaNbrPermanence_Type()
)
axsOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbmaNbrPermanence.setStatus("mandatory")
_AxsOspfVirtNbrTable_Object = MibTable
axsOspfVirtNbrTable = _AxsOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11)
)
if mibBuilder.loadTexts:
    axsOspfVirtNbrTable.setStatus("mandatory")
_AxsOspfVirtNbrEntry_Object = MibTableRow
axsOspfVirtNbrEntry = _AxsOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1)
)
axsOspfVirtNbrEntry.setIndexNames(
    (0, "AX4630S", "axsOspfVirtNbrDomainNumber"),
    (0, "AX4630S", "axsOspfVirtNbrArea"),
    (0, "AX4630S", "axsOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    axsOspfVirtNbrEntry.setStatus("mandatory")
_AxsOspfVirtNbrDomainNumber_Type = Integer32
_AxsOspfVirtNbrDomainNumber_Object = MibTableColumn
axsOspfVirtNbrDomainNumber = _AxsOspfVirtNbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 1),
    _AxsOspfVirtNbrDomainNumber_Type()
)
axsOspfVirtNbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrDomainNumber.setStatus("mandatory")
_AxsOspfVirtNbrArea_Type = IpAddress
_AxsOspfVirtNbrArea_Object = MibTableColumn
axsOspfVirtNbrArea = _AxsOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 2),
    _AxsOspfVirtNbrArea_Type()
)
axsOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrArea.setStatus("mandatory")
_AxsOspfVirtNbrRtrId_Type = IpAddress
_AxsOspfVirtNbrRtrId_Object = MibTableColumn
axsOspfVirtNbrRtrId = _AxsOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 3),
    _AxsOspfVirtNbrRtrId_Type()
)
axsOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrRtrId.setStatus("mandatory")
_AxsOspfVirtNbrIpAddr_Type = IpAddress
_AxsOspfVirtNbrIpAddr_Object = MibTableColumn
axsOspfVirtNbrIpAddr = _AxsOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 4),
    _AxsOspfVirtNbrIpAddr_Type()
)
axsOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrIpAddr.setStatus("mandatory")
_AxsOspfVirtNbrOptions_Type = Integer32
_AxsOspfVirtNbrOptions_Object = MibTableColumn
axsOspfVirtNbrOptions = _AxsOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 5),
    _AxsOspfVirtNbrOptions_Type()
)
axsOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrOptions.setStatus("mandatory")


class _AxsOspfVirtNbrState_Type(Integer32):
    """Custom type axsOspfVirtNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_AxsOspfVirtNbrState_Type.__name__ = "Integer32"
_AxsOspfVirtNbrState_Object = MibTableColumn
axsOspfVirtNbrState = _AxsOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 6),
    _AxsOspfVirtNbrState_Type()
)
axsOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrState.setStatus("mandatory")
_AxsOspfVirtNbrEvents_Type = Counter32
_AxsOspfVirtNbrEvents_Object = MibTableColumn
axsOspfVirtNbrEvents = _AxsOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 7),
    _AxsOspfVirtNbrEvents_Type()
)
axsOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrEvents.setStatus("mandatory")
_AxsOspfVirtNbrLsRetransQLen_Type = Gauge32
_AxsOspfVirtNbrLsRetransQLen_Object = MibTableColumn
axsOspfVirtNbrLsRetransQLen = _AxsOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 8),
    _AxsOspfVirtNbrLsRetransQLen_Type()
)
axsOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrLsRetransQLen.setStatus("mandatory")
_AxsOspfExtLsdbTable_Object = MibTable
axsOspfExtLsdbTable = _AxsOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12)
)
if mibBuilder.loadTexts:
    axsOspfExtLsdbTable.setStatus("mandatory")
_AxsOspfExtLsdbEntry_Object = MibTableRow
axsOspfExtLsdbEntry = _AxsOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1)
)
axsOspfExtLsdbEntry.setIndexNames(
    (0, "AX4630S", "axsOspfExtLsdbDomainNumber"),
    (0, "AX4630S", "axsOspfExtLsdbType"),
    (0, "AX4630S", "axsOspfExtLsdbLsid"),
    (0, "AX4630S", "axsOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    axsOspfExtLsdbEntry.setStatus("mandatory")
_AxsOspfExtLsdbDomainNumber_Type = Integer32
_AxsOspfExtLsdbDomainNumber_Object = MibTableColumn
axsOspfExtLsdbDomainNumber = _AxsOspfExtLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 1),
    _AxsOspfExtLsdbDomainNumber_Type()
)
axsOspfExtLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbDomainNumber.setStatus("mandatory")


class _AxsOspfExtLsdbType_Type(Integer32):
    """Custom type axsOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_AxsOspfExtLsdbType_Type.__name__ = "Integer32"
_AxsOspfExtLsdbType_Object = MibTableColumn
axsOspfExtLsdbType = _AxsOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 2),
    _AxsOspfExtLsdbType_Type()
)
axsOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbType.setStatus("mandatory")
_AxsOspfExtLsdbLsid_Type = IpAddress
_AxsOspfExtLsdbLsid_Object = MibTableColumn
axsOspfExtLsdbLsid = _AxsOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 3),
    _AxsOspfExtLsdbLsid_Type()
)
axsOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbLsid.setStatus("mandatory")
_AxsOspfExtLsdbRouterId_Type = IpAddress
_AxsOspfExtLsdbRouterId_Object = MibTableColumn
axsOspfExtLsdbRouterId = _AxsOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 4),
    _AxsOspfExtLsdbRouterId_Type()
)
axsOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbRouterId.setStatus("mandatory")
_AxsOspfExtLsdbSequence_Type = Integer32
_AxsOspfExtLsdbSequence_Object = MibTableColumn
axsOspfExtLsdbSequence = _AxsOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 5),
    _AxsOspfExtLsdbSequence_Type()
)
axsOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbSequence.setStatus("mandatory")
_AxsOspfExtLsdbAge_Type = Integer32
_AxsOspfExtLsdbAge_Object = MibTableColumn
axsOspfExtLsdbAge = _AxsOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 6),
    _AxsOspfExtLsdbAge_Type()
)
axsOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbAge.setStatus("mandatory")
_AxsOspfExtLsdbChecksum_Type = Integer32
_AxsOspfExtLsdbChecksum_Object = MibTableColumn
axsOspfExtLsdbChecksum = _AxsOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 7),
    _AxsOspfExtLsdbChecksum_Type()
)
axsOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbChecksum.setStatus("mandatory")
_AxsOspfExtLsdbAdvertisement_Type = OctetString
_AxsOspfExtLsdbAdvertisement_Object = MibTableColumn
axsOspfExtLsdbAdvertisement = _AxsOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 8),
    _AxsOspfExtLsdbAdvertisement_Type()
)
axsOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbAdvertisement.setStatus("mandatory")
_AxsOspfAreaAggregateTable_Object = MibTable
axsOspfAreaAggregateTable = _AxsOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14)
)
if mibBuilder.loadTexts:
    axsOspfAreaAggregateTable.setStatus("mandatory")
_AxsOspfAreaAggregateEntry_Object = MibTableRow
axsOspfAreaAggregateEntry = _AxsOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1)
)
axsOspfAreaAggregateEntry.setIndexNames(
    (0, "AX4630S", "axsOspfAreaAggregateDomainNumber"),
    (0, "AX4630S", "axsOspfAreaAggregateAreaID"),
    (0, "AX4630S", "axsOspfAreaAggregateLsdbType"),
    (0, "AX4630S", "axsOspfAreaAggregateNet"),
    (0, "AX4630S", "axsOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    axsOspfAreaAggregateEntry.setStatus("mandatory")
_AxsOspfAreaAggregateDomainNumber_Type = Integer32
_AxsOspfAreaAggregateDomainNumber_Object = MibTableColumn
axsOspfAreaAggregateDomainNumber = _AxsOspfAreaAggregateDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 1),
    _AxsOspfAreaAggregateDomainNumber_Type()
)
axsOspfAreaAggregateDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateDomainNumber.setStatus("mandatory")
_AxsOspfAreaAggregateAreaID_Type = IpAddress
_AxsOspfAreaAggregateAreaID_Object = MibTableColumn
axsOspfAreaAggregateAreaID = _AxsOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 2),
    _AxsOspfAreaAggregateAreaID_Type()
)
axsOspfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateAreaID.setStatus("mandatory")


class _AxsOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type axsOspfAreaAggregateLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("summaryLink", 3),
          ("nssaExternalLink", 7))
    )


_AxsOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_AxsOspfAreaAggregateLsdbType_Object = MibTableColumn
axsOspfAreaAggregateLsdbType = _AxsOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 3),
    _AxsOspfAreaAggregateLsdbType_Type()
)
axsOspfAreaAggregateLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateLsdbType.setStatus("mandatory")
_AxsOspfAreaAggregateNet_Type = IpAddress
_AxsOspfAreaAggregateNet_Object = MibTableColumn
axsOspfAreaAggregateNet = _AxsOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 4),
    _AxsOspfAreaAggregateNet_Type()
)
axsOspfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateNet.setStatus("mandatory")
_AxsOspfAreaAggregateMask_Type = IpAddress
_AxsOspfAreaAggregateMask_Object = MibTableColumn
axsOspfAreaAggregateMask = _AxsOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 5),
    _AxsOspfAreaAggregateMask_Type()
)
axsOspfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateMask.setStatus("mandatory")


class _AxsOspfAreaAggregateStatus_Type(Integer32):
    """Custom type axsOspfAreaAggregateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_AxsOspfAreaAggregateStatus_Type.__name__ = "Integer32"
_AxsOspfAreaAggregateStatus_Object = MibTableColumn
axsOspfAreaAggregateStatus = _AxsOspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 6),
    _AxsOspfAreaAggregateStatus_Type()
)
axsOspfAreaAggregateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateStatus.setStatus("mandatory")


class _AxsOspfAreaAggregateEffect_Type(Integer32):
    """Custom type axsOspfAreaAggregateEffect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2))
    )


_AxsOspfAreaAggregateEffect_Type.__name__ = "Integer32"
_AxsOspfAreaAggregateEffect_Object = MibTableColumn
axsOspfAreaAggregateEffect = _AxsOspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 7),
    _AxsOspfAreaAggregateEffect_Type()
)
axsOspfAreaAggregateEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateEffect.setStatus("mandatory")
_AxsOspfTrap_ObjectIdentity = ObjectIdentity
axsOspfTrap = _AxsOspfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16)
)
_AxsOspfTrapControlTable_Object = MibTable
axsOspfTrapControlTable = _AxsOspfTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1)
)
if mibBuilder.loadTexts:
    axsOspfTrapControlTable.setStatus("mandatory")
_AxsOspfTrapControlEntry_Object = MibTableRow
axsOspfTrapControlEntry = _AxsOspfTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1)
)
axsOspfTrapControlEntry.setIndexNames(
    (0, "AX4630S", "axsOspfTrapDomainNumber"),
)
if mibBuilder.loadTexts:
    axsOspfTrapControlEntry.setStatus("mandatory")
_AxsOspfTrapDomainNumber_Type = Integer32
_AxsOspfTrapDomainNumber_Object = MibTableColumn
axsOspfTrapDomainNumber = _AxsOspfTrapDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1, 1),
    _AxsOspfTrapDomainNumber_Type()
)
axsOspfTrapDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfTrapDomainNumber.setStatus("mandatory")
_AxsOspfSetTrap_Type = OctetString
_AxsOspfSetTrap_Object = MibTableColumn
axsOspfSetTrap = _AxsOspfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1, 2),
    _AxsOspfSetTrap_Type()
)
axsOspfSetTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfSetTrap.setStatus("mandatory")


class _AxsOspfConfigErrorType_Type(Integer32):
    """Custom type axsOspfConfigErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("badVersion", 1),
          ("areaMismatch", 2),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4),
          ("authTypeMismatch", 5),
          ("authFailure", 6),
          ("netMaskMismatch", 7),
          ("helloIntervalMismatch", 8),
          ("deadIntervalMismatch", 9),
          ("optionMismatch", 10),
          ("duplicateRouterId", 12),
          ("noError", 13))
    )


_AxsOspfConfigErrorType_Type.__name__ = "Integer32"
_AxsOspfConfigErrorType_Object = MibTableColumn
axsOspfConfigErrorType = _AxsOspfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1, 3),
    _AxsOspfConfigErrorType_Type()
)
axsOspfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfConfigErrorType.setStatus("mandatory")


class _AxsOspfPacketType_Type(Integer32):
    """Custom type axsOspfPacketType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5),
          ("nullPacket", 6))
    )


_AxsOspfPacketType_Type.__name__ = "Integer32"
_AxsOspfPacketType_Object = MibTableColumn
axsOspfPacketType = _AxsOspfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1, 4),
    _AxsOspfPacketType_Type()
)
axsOspfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfPacketType.setStatus("mandatory")
_AxsOspfPacketSrc_Type = IpAddress
_AxsOspfPacketSrc_Object = MibTableColumn
axsOspfPacketSrc = _AxsOspfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1, 5),
    _AxsOspfPacketSrc_Type()
)
axsOspfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfPacketSrc.setStatus("mandatory")
_AxsOspfTraps_ObjectIdentity = ObjectIdentity
axsOspfTraps = _AxsOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2)
)
_AxsOspfv3_ObjectIdentity = ObjectIdentity
axsOspfv3 = _AxsOspfv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15)
)
_AxsOspfv3GeneralTable_Object = MibTable
axsOspfv3GeneralTable = _AxsOspfv3GeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    axsOspfv3GeneralTable.setStatus("mandatory")
_AxsOspfv3GeneralEntry_Object = MibTableRow
axsOspfv3GeneralEntry = _AxsOspfv3GeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1)
)
axsOspfv3GeneralEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3GeneralDomainNumber"),
)
if mibBuilder.loadTexts:
    axsOspfv3GeneralEntry.setStatus("mandatory")
_AxsOspfv3GeneralDomainNumber_Type = Integer32
_AxsOspfv3GeneralDomainNumber_Object = MibTableColumn
axsOspfv3GeneralDomainNumber = _AxsOspfv3GeneralDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 1),
    _AxsOspfv3GeneralDomainNumber_Type()
)
axsOspfv3GeneralDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3GeneralDomainNumber.setStatus("mandatory")
_AxsOspfv3RouterId_Type = RouterID
_AxsOspfv3RouterId_Object = MibTableColumn
axsOspfv3RouterId = _AxsOspfv3RouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 2),
    _AxsOspfv3RouterId_Type()
)
axsOspfv3RouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3RouterId.setStatus("mandatory")
_AxsOspfv3AdminStat_Type = Status
_AxsOspfv3AdminStat_Object = MibTableColumn
axsOspfv3AdminStat = _AxsOspfv3AdminStat_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 3),
    _AxsOspfv3AdminStat_Type()
)
axsOspfv3AdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AdminStat.setStatus("mandatory")


class _AxsOspfv3VersionNumber_Type(Integer32):
    """Custom type axsOspfv3VersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("version3", 3)
    )


_AxsOspfv3VersionNumber_Type.__name__ = "Integer32"
_AxsOspfv3VersionNumber_Object = MibTableColumn
axsOspfv3VersionNumber = _AxsOspfv3VersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 4),
    _AxsOspfv3VersionNumber_Type()
)
axsOspfv3VersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VersionNumber.setStatus("mandatory")
_AxsOspfv3AreaBdrRtrStatus_Type = TruthValue
_AxsOspfv3AreaBdrRtrStatus_Object = MibTableColumn
axsOspfv3AreaBdrRtrStatus = _AxsOspfv3AreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 5),
    _AxsOspfv3AreaBdrRtrStatus_Type()
)
axsOspfv3AreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaBdrRtrStatus.setStatus("mandatory")
_AxsOspfv3ASBdrRtrStatus_Type = TruthValue
_AxsOspfv3ASBdrRtrStatus_Object = MibTableColumn
axsOspfv3ASBdrRtrStatus = _AxsOspfv3ASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 6),
    _AxsOspfv3ASBdrRtrStatus_Type()
)
axsOspfv3ASBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3ASBdrRtrStatus.setStatus("mandatory")
_AxsOspfv3AsScopeLsaCount_Type = Gauge32
_AxsOspfv3AsScopeLsaCount_Object = MibTableColumn
axsOspfv3AsScopeLsaCount = _AxsOspfv3AsScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 7),
    _AxsOspfv3AsScopeLsaCount_Type()
)
axsOspfv3AsScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsScopeLsaCount.setStatus("mandatory")
_AxsOspfv3AsScopeLsaCksumSum_Type = Integer32
_AxsOspfv3AsScopeLsaCksumSum_Object = MibTableColumn
axsOspfv3AsScopeLsaCksumSum = _AxsOspfv3AsScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 8),
    _AxsOspfv3AsScopeLsaCksumSum_Type()
)
axsOspfv3AsScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsScopeLsaCksumSum.setStatus("mandatory")
_AxsOspfv3OriginateNewLsas_Type = Counter32
_AxsOspfv3OriginateNewLsas_Object = MibTableColumn
axsOspfv3OriginateNewLsas = _AxsOspfv3OriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 9),
    _AxsOspfv3OriginateNewLsas_Type()
)
axsOspfv3OriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3OriginateNewLsas.setStatus("mandatory")
_AxsOspfv3RxNewLsas_Type = Counter32
_AxsOspfv3RxNewLsas_Object = MibTableColumn
axsOspfv3RxNewLsas = _AxsOspfv3RxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 10),
    _AxsOspfv3RxNewLsas_Type()
)
axsOspfv3RxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3RxNewLsas.setStatus("mandatory")


class _AxsOspfv3ExtAreaLsdbLimit_Type(Integer32):
    """Custom type axsOspfv3ExtAreaLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AxsOspfv3ExtAreaLsdbLimit_Type.__name__ = "Integer32"
_AxsOspfv3ExtAreaLsdbLimit_Object = MibTableColumn
axsOspfv3ExtAreaLsdbLimit = _AxsOspfv3ExtAreaLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 11),
    _AxsOspfv3ExtAreaLsdbLimit_Type()
)
axsOspfv3ExtAreaLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3ExtAreaLsdbLimit.setStatus("mandatory")


class _AxsOspfv3MulticastExtensions_Type(Integer32):
    """Custom type axsOspfv3MulticastExtensions based on Integer32"""
    defaultValue = 0


_AxsOspfv3MulticastExtensions_Type.__name__ = "Integer32"
_AxsOspfv3MulticastExtensions_Object = MibTableColumn
axsOspfv3MulticastExtensions = _AxsOspfv3MulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 12),
    _AxsOspfv3MulticastExtensions_Type()
)
axsOspfv3MulticastExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3MulticastExtensions.setStatus("mandatory")
_AxsOspfv3DemandExtensions_Type = TruthValue
_AxsOspfv3DemandExtensions_Object = MibTableColumn
axsOspfv3DemandExtensions = _AxsOspfv3DemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 14),
    _AxsOspfv3DemandExtensions_Type()
)
axsOspfv3DemandExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3DemandExtensions.setStatus("mandatory")
_AxsOspfv3TrafficEngineeringSupport_Type = TruthValue
_AxsOspfv3TrafficEngineeringSupport_Object = MibTableColumn
axsOspfv3TrafficEngineeringSupport = _AxsOspfv3TrafficEngineeringSupport_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 15),
    _AxsOspfv3TrafficEngineeringSupport_Type()
)
axsOspfv3TrafficEngineeringSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3TrafficEngineeringSupport.setStatus("mandatory")
_AxsOspfv3AreaTable_Object = MibTable
axsOspfv3AreaTable = _AxsOspfv3AreaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2)
)
if mibBuilder.loadTexts:
    axsOspfv3AreaTable.setStatus("mandatory")
_AxsOspfv3AreaEntry_Object = MibTableRow
axsOspfv3AreaEntry = _AxsOspfv3AreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1)
)
axsOspfv3AreaEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3AreaDomainNumber"),
    (0, "AX4630S", "axsOspfv3AreaId"),
)
if mibBuilder.loadTexts:
    axsOspfv3AreaEntry.setStatus("mandatory")
_AxsOspfv3AreaDomainNumber_Type = Integer32
_AxsOspfv3AreaDomainNumber_Object = MibTableColumn
axsOspfv3AreaDomainNumber = _AxsOspfv3AreaDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 1),
    _AxsOspfv3AreaDomainNumber_Type()
)
axsOspfv3AreaDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaDomainNumber.setStatus("mandatory")
_AxsOspfv3AreaId_Type = AreaID
_AxsOspfv3AreaId_Object = MibTableColumn
axsOspfv3AreaId = _AxsOspfv3AreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 2),
    _AxsOspfv3AreaId_Type()
)
axsOspfv3AreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaId.setStatus("mandatory")


class _AxsOspfv3ImportAsExtern_Type(Integer32):
    """Custom type axsOspfv3ImportAsExtern based on Integer32"""
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
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_AxsOspfv3ImportAsExtern_Type.__name__ = "Integer32"
_AxsOspfv3ImportAsExtern_Object = MibTableColumn
axsOspfv3ImportAsExtern = _AxsOspfv3ImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 3),
    _AxsOspfv3ImportAsExtern_Type()
)
axsOspfv3ImportAsExtern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3ImportAsExtern.setStatus("mandatory")
_AxsOspfv3SpfRuns_Type = Counter32
_AxsOspfv3SpfRuns_Object = MibTableColumn
axsOspfv3SpfRuns = _AxsOspfv3SpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 4),
    _AxsOspfv3SpfRuns_Type()
)
axsOspfv3SpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3SpfRuns.setStatus("mandatory")
_AxsOspfv3AreaBdrRtrCount_Type = Gauge32
_AxsOspfv3AreaBdrRtrCount_Object = MibTableColumn
axsOspfv3AreaBdrRtrCount = _AxsOspfv3AreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 5),
    _AxsOspfv3AreaBdrRtrCount_Type()
)
axsOspfv3AreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaBdrRtrCount.setStatus("mandatory")
_AxsOspfv3AsBdrRtrCount_Type = Gauge32
_AxsOspfv3AsBdrRtrCount_Object = MibTableColumn
axsOspfv3AsBdrRtrCount = _AxsOspfv3AsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 6),
    _AxsOspfv3AsBdrRtrCount_Type()
)
axsOspfv3AsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsBdrRtrCount.setStatus("mandatory")
_AxsOspfv3AreaScopeLsaCount_Type = Gauge32
_AxsOspfv3AreaScopeLsaCount_Object = MibTableColumn
axsOspfv3AreaScopeLsaCount = _AxsOspfv3AreaScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 7),
    _AxsOspfv3AreaScopeLsaCount_Type()
)
axsOspfv3AreaScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaScopeLsaCount.setStatus("mandatory")


class _AxsOspfv3AreaScopeLsaCksumSum_Type(Integer32):
    """Custom type axsOspfv3AreaScopeLsaCksumSum based on Integer32"""
    defaultValue = 0


_AxsOspfv3AreaScopeLsaCksumSum_Type.__name__ = "Integer32"
_AxsOspfv3AreaScopeLsaCksumSum_Object = MibTableColumn
axsOspfv3AreaScopeLsaCksumSum = _AxsOspfv3AreaScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 8),
    _AxsOspfv3AreaScopeLsaCksumSum_Type()
)
axsOspfv3AreaScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaScopeLsaCksumSum.setStatus("mandatory")


class _AxsOspfv3AreaSummary_Type(Integer32):
    """Custom type axsOspfv3AreaSummary based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_AxsOspfv3AreaSummary_Type.__name__ = "Integer32"
_AxsOspfv3AreaSummary_Object = MibTableColumn
axsOspfv3AreaSummary = _AxsOspfv3AreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 9),
    _AxsOspfv3AreaSummary_Type()
)
axsOspfv3AreaSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaSummary.setStatus("mandatory")
_AxsOspfv3AreaStatus_Type = RowStatus
_AxsOspfv3AreaStatus_Object = MibTableColumn
axsOspfv3AreaStatus = _AxsOspfv3AreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 10),
    _AxsOspfv3AreaStatus_Type()
)
axsOspfv3AreaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaStatus.setStatus("mandatory")
_AxsOspfv3StubMetric_Type = BigMetric
_AxsOspfv3StubMetric_Object = MibTableColumn
axsOspfv3StubMetric = _AxsOspfv3StubMetric_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 11),
    _AxsOspfv3StubMetric_Type()
)
axsOspfv3StubMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3StubMetric.setStatus("mandatory")
_AxsOspfv3AsLsdbTable_Object = MibTable
axsOspfv3AsLsdbTable = _AxsOspfv3AsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3)
)
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbTable.setStatus("mandatory")
_AxsOspfv3AsLsdbEntry_Object = MibTableRow
axsOspfv3AsLsdbEntry = _AxsOspfv3AsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1)
)
axsOspfv3AsLsdbEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3AsLsdbDomainNumber"),
    (0, "AX4630S", "axsOspfv3AsLsdbType"),
    (0, "AX4630S", "axsOspfv3AsLsdbRouterId"),
    (0, "AX4630S", "axsOspfv3AsLsdbLsid"),
)
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbEntry.setStatus("mandatory")
_AxsOspfv3AsLsdbDomainNumber_Type = Integer32
_AxsOspfv3AsLsdbDomainNumber_Object = MibTableColumn
axsOspfv3AsLsdbDomainNumber = _AxsOspfv3AsLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 1),
    _AxsOspfv3AsLsdbDomainNumber_Type()
)
axsOspfv3AsLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbDomainNumber.setStatus("mandatory")


class _AxsOspfv3AsLsdbType_Type(Integer32):
    """Custom type axsOspfv3AsLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            16389
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 16389)
    )


_AxsOspfv3AsLsdbType_Type.__name__ = "Integer32"
_AxsOspfv3AsLsdbType_Object = MibTableColumn
axsOspfv3AsLsdbType = _AxsOspfv3AsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 2),
    _AxsOspfv3AsLsdbType_Type()
)
axsOspfv3AsLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbType.setStatus("mandatory")
_AxsOspfv3AsLsdbRouterId_Type = RouterID
_AxsOspfv3AsLsdbRouterId_Object = MibTableColumn
axsOspfv3AsLsdbRouterId = _AxsOspfv3AsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 3),
    _AxsOspfv3AsLsdbRouterId_Type()
)
axsOspfv3AsLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbRouterId.setStatus("mandatory")
_AxsOspfv3AsLsdbLsid_Type = IpAddress
_AxsOspfv3AsLsdbLsid_Object = MibTableColumn
axsOspfv3AsLsdbLsid = _AxsOspfv3AsLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 4),
    _AxsOspfv3AsLsdbLsid_Type()
)
axsOspfv3AsLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbLsid.setStatus("mandatory")
_AxsOspfv3AsLsdbSequence_Type = Integer32
_AxsOspfv3AsLsdbSequence_Object = MibTableColumn
axsOspfv3AsLsdbSequence = _AxsOspfv3AsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 5),
    _AxsOspfv3AsLsdbSequence_Type()
)
axsOspfv3AsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbSequence.setStatus("mandatory")
_AxsOspfv3AsLsdbAge_Type = Integer32
_AxsOspfv3AsLsdbAge_Object = MibTableColumn
axsOspfv3AsLsdbAge = _AxsOspfv3AsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 6),
    _AxsOspfv3AsLsdbAge_Type()
)
axsOspfv3AsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbAge.setStatus("mandatory")
_AxsOspfv3AsLsdbChecksum_Type = Integer32
_AxsOspfv3AsLsdbChecksum_Object = MibTableColumn
axsOspfv3AsLsdbChecksum = _AxsOspfv3AsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 7),
    _AxsOspfv3AsLsdbChecksum_Type()
)
axsOspfv3AsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbChecksum.setStatus("mandatory")


class _AxsOspfv3AsLsdbAdvertisement_Type(OctetString):
    """Custom type axsOspfv3AsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_AxsOspfv3AsLsdbAdvertisement_Type.__name__ = "OctetString"
_AxsOspfv3AsLsdbAdvertisement_Object = MibTableColumn
axsOspfv3AsLsdbAdvertisement = _AxsOspfv3AsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 8),
    _AxsOspfv3AsLsdbAdvertisement_Type()
)
axsOspfv3AsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbAdvertisement.setStatus("mandatory")
_AxsOspfv3AreaLsdbTable_Object = MibTable
axsOspfv3AreaLsdbTable = _AxsOspfv3AreaLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4)
)
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbTable.setStatus("mandatory")
_AxsOspfv3AreaLsdbEntry_Object = MibTableRow
axsOspfv3AreaLsdbEntry = _AxsOspfv3AreaLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1)
)
axsOspfv3AreaLsdbEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3AreaLsdbDomainNumber"),
    (0, "AX4630S", "axsOspfv3AreaLsdbAreaId"),
    (0, "AX4630S", "axsOspfv3AreaLsdbType"),
    (0, "AX4630S", "axsOspfv3AreaLsdbRouterId"),
    (0, "AX4630S", "axsOspfv3AreaLsdbLsid"),
)
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbEntry.setStatus("mandatory")
_AxsOspfv3AreaLsdbDomainNumber_Type = Integer32
_AxsOspfv3AreaLsdbDomainNumber_Object = MibTableColumn
axsOspfv3AreaLsdbDomainNumber = _AxsOspfv3AreaLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 1),
    _AxsOspfv3AreaLsdbDomainNumber_Type()
)
axsOspfv3AreaLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbDomainNumber.setStatus("mandatory")
_AxsOspfv3AreaLsdbAreaId_Type = AreaID
_AxsOspfv3AreaLsdbAreaId_Object = MibTableColumn
axsOspfv3AreaLsdbAreaId = _AxsOspfv3AreaLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 2),
    _AxsOspfv3AreaLsdbAreaId_Type()
)
axsOspfv3AreaLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbAreaId.setStatus("mandatory")


class _AxsOspfv3AreaLsdbType_Type(Integer32):
    """Custom type axsOspfv3AreaLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8193,
              8194,
              8195,
              8196,
              8198,
              8199,
              8201)
        )
    )
    namedValues = NamedValues(
        *(("routerLsa", 8193),
          ("networkLsa", 8194),
          ("interAreaPrefixLsa", 8195),
          ("interAreaRouterLsa", 8196),
          ("groupMembershipLsa", 8198),
          ("nssaExternalLsa", 8199),
          ("intraAreaPrefixLsa", 8201))
    )


_AxsOspfv3AreaLsdbType_Type.__name__ = "Integer32"
_AxsOspfv3AreaLsdbType_Object = MibTableColumn
axsOspfv3AreaLsdbType = _AxsOspfv3AreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 3),
    _AxsOspfv3AreaLsdbType_Type()
)
axsOspfv3AreaLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbType.setStatus("mandatory")
_AxsOspfv3AreaLsdbRouterId_Type = RouterID
_AxsOspfv3AreaLsdbRouterId_Object = MibTableColumn
axsOspfv3AreaLsdbRouterId = _AxsOspfv3AreaLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 4),
    _AxsOspfv3AreaLsdbRouterId_Type()
)
axsOspfv3AreaLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbRouterId.setStatus("mandatory")
_AxsOspfv3AreaLsdbLsid_Type = IpAddress
_AxsOspfv3AreaLsdbLsid_Object = MibTableColumn
axsOspfv3AreaLsdbLsid = _AxsOspfv3AreaLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 5),
    _AxsOspfv3AreaLsdbLsid_Type()
)
axsOspfv3AreaLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbLsid.setStatus("mandatory")
_AxsOspfv3AreaLsdbSequence_Type = Integer32
_AxsOspfv3AreaLsdbSequence_Object = MibTableColumn
axsOspfv3AreaLsdbSequence = _AxsOspfv3AreaLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 6),
    _AxsOspfv3AreaLsdbSequence_Type()
)
axsOspfv3AreaLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbSequence.setStatus("mandatory")
_AxsOspfv3AreaLsdbAge_Type = Integer32
_AxsOspfv3AreaLsdbAge_Object = MibTableColumn
axsOspfv3AreaLsdbAge = _AxsOspfv3AreaLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 7),
    _AxsOspfv3AreaLsdbAge_Type()
)
axsOspfv3AreaLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbAge.setStatus("mandatory")
_AxsOspfv3AreaLsdbChecksum_Type = Integer32
_AxsOspfv3AreaLsdbChecksum_Object = MibTableColumn
axsOspfv3AreaLsdbChecksum = _AxsOspfv3AreaLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 8),
    _AxsOspfv3AreaLsdbChecksum_Type()
)
axsOspfv3AreaLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbChecksum.setStatus("mandatory")


class _AxsOspfv3AreaLsdbAdvertisement_Type(OctetString):
    """Custom type axsOspfv3AreaLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_AxsOspfv3AreaLsdbAdvertisement_Type.__name__ = "OctetString"
_AxsOspfv3AreaLsdbAdvertisement_Object = MibTableColumn
axsOspfv3AreaLsdbAdvertisement = _AxsOspfv3AreaLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 9),
    _AxsOspfv3AreaLsdbAdvertisement_Type()
)
axsOspfv3AreaLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbAdvertisement.setStatus("mandatory")
_AxsOspfv3LinkLsdbTable_Object = MibTable
axsOspfv3LinkLsdbTable = _AxsOspfv3LinkLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5)
)
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbTable.setStatus("mandatory")
_AxsOspfv3LinkLsdbEntry_Object = MibTableRow
axsOspfv3LinkLsdbEntry = _AxsOspfv3LinkLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1)
)
axsOspfv3LinkLsdbEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3LinkLsdbDomainNumber"),
    (0, "AX4630S", "axsOspfv3LinkLsdbIfIndex"),
    (0, "AX4630S", "axsOspfv3LinkLsdbType"),
    (0, "AX4630S", "axsOspfv3LinkLsdbRouterId"),
    (0, "AX4630S", "axsOspfv3LinkLsdbLsid"),
)
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbEntry.setStatus("mandatory")
_AxsOspfv3LinkLsdbDomainNumber_Type = Integer32
_AxsOspfv3LinkLsdbDomainNumber_Object = MibTableColumn
axsOspfv3LinkLsdbDomainNumber = _AxsOspfv3LinkLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 1),
    _AxsOspfv3LinkLsdbDomainNumber_Type()
)
axsOspfv3LinkLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbDomainNumber.setStatus("mandatory")
_AxsOspfv3LinkLsdbIfIndex_Type = Ipv6IfIndex
_AxsOspfv3LinkLsdbIfIndex_Object = MibTableColumn
axsOspfv3LinkLsdbIfIndex = _AxsOspfv3LinkLsdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 2),
    _AxsOspfv3LinkLsdbIfIndex_Type()
)
axsOspfv3LinkLsdbIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbIfIndex.setStatus("mandatory")


class _AxsOspfv3LinkLsdbType_Type(Integer32):
    """Custom type axsOspfv3LinkLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("linkLsa", 8)
    )


_AxsOspfv3LinkLsdbType_Type.__name__ = "Integer32"
_AxsOspfv3LinkLsdbType_Object = MibTableColumn
axsOspfv3LinkLsdbType = _AxsOspfv3LinkLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 3),
    _AxsOspfv3LinkLsdbType_Type()
)
axsOspfv3LinkLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbType.setStatus("mandatory")
_AxsOspfv3LinkLsdbRouterId_Type = RouterID
_AxsOspfv3LinkLsdbRouterId_Object = MibTableColumn
axsOspfv3LinkLsdbRouterId = _AxsOspfv3LinkLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 4),
    _AxsOspfv3LinkLsdbRouterId_Type()
)
axsOspfv3LinkLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbRouterId.setStatus("mandatory")
_AxsOspfv3LinkLsdbLsid_Type = IpAddress
_AxsOspfv3LinkLsdbLsid_Object = MibTableColumn
axsOspfv3LinkLsdbLsid = _AxsOspfv3LinkLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 5),
    _AxsOspfv3LinkLsdbLsid_Type()
)
axsOspfv3LinkLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbLsid.setStatus("mandatory")
_AxsOspfv3LinkLsdbSequence_Type = Integer32
_AxsOspfv3LinkLsdbSequence_Object = MibTableColumn
axsOspfv3LinkLsdbSequence = _AxsOspfv3LinkLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 6),
    _AxsOspfv3LinkLsdbSequence_Type()
)
axsOspfv3LinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbSequence.setStatus("mandatory")
_AxsOspfv3LinkLsdbAge_Type = Integer32
_AxsOspfv3LinkLsdbAge_Object = MibTableColumn
axsOspfv3LinkLsdbAge = _AxsOspfv3LinkLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 7),
    _AxsOspfv3LinkLsdbAge_Type()
)
axsOspfv3LinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbAge.setStatus("mandatory")
_AxsOspfv3LinkLsdbChecksum_Type = Integer32
_AxsOspfv3LinkLsdbChecksum_Object = MibTableColumn
axsOspfv3LinkLsdbChecksum = _AxsOspfv3LinkLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 8),
    _AxsOspfv3LinkLsdbChecksum_Type()
)
axsOspfv3LinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbChecksum.setStatus("mandatory")


class _AxsOspfv3LinkLsdbAdvertisement_Type(OctetString):
    """Custom type axsOspfv3LinkLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_AxsOspfv3LinkLsdbAdvertisement_Type.__name__ = "OctetString"
_AxsOspfv3LinkLsdbAdvertisement_Object = MibTableColumn
axsOspfv3LinkLsdbAdvertisement = _AxsOspfv3LinkLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 9),
    _AxsOspfv3LinkLsdbAdvertisement_Type()
)
axsOspfv3LinkLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbAdvertisement.setStatus("mandatory")
_AxsOspfv3IfTable_Object = MibTable
axsOspfv3IfTable = _AxsOspfv3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7)
)
if mibBuilder.loadTexts:
    axsOspfv3IfTable.setStatus("mandatory")
_AxsOspfv3IfEntry_Object = MibTableRow
axsOspfv3IfEntry = _AxsOspfv3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1)
)
axsOspfv3IfEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3IfDomainNumber"),
    (0, "AX4630S", "axsOspfv3IfIndex"),
)
if mibBuilder.loadTexts:
    axsOspfv3IfEntry.setStatus("mandatory")
_AxsOspfv3IfDomainNumber_Type = Integer32
_AxsOspfv3IfDomainNumber_Object = MibTableColumn
axsOspfv3IfDomainNumber = _AxsOspfv3IfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 1),
    _AxsOspfv3IfDomainNumber_Type()
)
axsOspfv3IfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfDomainNumber.setStatus("mandatory")
_AxsOspfv3IfIndex_Type = Ipv6IfIndex
_AxsOspfv3IfIndex_Object = MibTableColumn
axsOspfv3IfIndex = _AxsOspfv3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 2),
    _AxsOspfv3IfIndex_Type()
)
axsOspfv3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfIndex.setStatus("mandatory")


class _AxsOspfv3IfAreaId_Type(AreaID):
    """Custom type axsOspfv3IfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_AxsOspfv3IfAreaId_Type.__name__ = "AreaID"
_AxsOspfv3IfAreaId_Object = MibTableColumn
axsOspfv3IfAreaId = _AxsOspfv3IfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 3),
    _AxsOspfv3IfAreaId_Type()
)
axsOspfv3IfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfAreaId.setStatus("mandatory")


class _AxsOspfv3IfType_Type(Integer32):
    """Custom type axsOspfv3IfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3),
          ("pointToMultipoint", 5))
    )


_AxsOspfv3IfType_Type.__name__ = "Integer32"
_AxsOspfv3IfType_Object = MibTableColumn
axsOspfv3IfType = _AxsOspfv3IfType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 4),
    _AxsOspfv3IfType_Type()
)
axsOspfv3IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfType.setStatus("mandatory")


class _AxsOspfv3IfAdminStat_Type(Status):
    """Custom type axsOspfv3IfAdminStat based on Status"""
    defaultValue = 1


_AxsOspfv3IfAdminStat_Type.__name__ = "Status"
_AxsOspfv3IfAdminStat_Object = MibTableColumn
axsOspfv3IfAdminStat = _AxsOspfv3IfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 5),
    _AxsOspfv3IfAdminStat_Type()
)
axsOspfv3IfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfAdminStat.setStatus("mandatory")


class _AxsOspfv3IfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type axsOspfv3IfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_AxsOspfv3IfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_AxsOspfv3IfRtrPriority_Object = MibTableColumn
axsOspfv3IfRtrPriority = _AxsOspfv3IfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 6),
    _AxsOspfv3IfRtrPriority_Type()
)
axsOspfv3IfRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfRtrPriority.setStatus("mandatory")


class _AxsOspfv3IfTransitDelay_Type(UpToMaxAge):
    """Custom type axsOspfv3IfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_AxsOspfv3IfTransitDelay_Type.__name__ = "UpToMaxAge"
_AxsOspfv3IfTransitDelay_Object = MibTableColumn
axsOspfv3IfTransitDelay = _AxsOspfv3IfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 7),
    _AxsOspfv3IfTransitDelay_Type()
)
axsOspfv3IfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfTransitDelay.setStatus("mandatory")


class _AxsOspfv3IfRetransInterval_Type(UpToMaxAge):
    """Custom type axsOspfv3IfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_AxsOspfv3IfRetransInterval_Type.__name__ = "UpToMaxAge"
_AxsOspfv3IfRetransInterval_Object = MibTableColumn
axsOspfv3IfRetransInterval = _AxsOspfv3IfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 8),
    _AxsOspfv3IfRetransInterval_Type()
)
axsOspfv3IfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfRetransInterval.setStatus("mandatory")


class _AxsOspfv3IfHelloInterval_Type(HelloRange):
    """Custom type axsOspfv3IfHelloInterval based on HelloRange"""
    defaultValue = 10


_AxsOspfv3IfHelloInterval_Type.__name__ = "HelloRange"
_AxsOspfv3IfHelloInterval_Object = MibTableColumn
axsOspfv3IfHelloInterval = _AxsOspfv3IfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 9),
    _AxsOspfv3IfHelloInterval_Type()
)
axsOspfv3IfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfHelloInterval.setStatus("mandatory")


class _AxsOspfv3IfRtrDeadInterval_Type(PositiveInteger):
    """Custom type axsOspfv3IfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_AxsOspfv3IfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_AxsOspfv3IfRtrDeadInterval_Object = MibTableColumn
axsOspfv3IfRtrDeadInterval = _AxsOspfv3IfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 10),
    _AxsOspfv3IfRtrDeadInterval_Type()
)
axsOspfv3IfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfRtrDeadInterval.setStatus("mandatory")


class _AxsOspfv3IfPollInterval_Type(PositiveInteger):
    """Custom type axsOspfv3IfPollInterval based on PositiveInteger"""
    defaultValue = 120


_AxsOspfv3IfPollInterval_Type.__name__ = "PositiveInteger"
_AxsOspfv3IfPollInterval_Object = MibTableColumn
axsOspfv3IfPollInterval = _AxsOspfv3IfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 11),
    _AxsOspfv3IfPollInterval_Type()
)
axsOspfv3IfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfPollInterval.setStatus("mandatory")


class _AxsOspfv3IfState_Type(Integer32):
    """Custom type axsOspfv3IfState based on Integer32"""
    defaultValue = 1

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
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_AxsOspfv3IfState_Type.__name__ = "Integer32"
_AxsOspfv3IfState_Object = MibTableColumn
axsOspfv3IfState = _AxsOspfv3IfState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 12),
    _AxsOspfv3IfState_Type()
)
axsOspfv3IfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfState.setStatus("mandatory")


class _AxsOspfv3IfDesignatedRouter_Type(RouterID):
    """Custom type axsOspfv3IfDesignatedRouter based on RouterID"""
    defaultHexValue = "00000000"


_AxsOspfv3IfDesignatedRouter_Type.__name__ = "RouterID"
_AxsOspfv3IfDesignatedRouter_Object = MibTableColumn
axsOspfv3IfDesignatedRouter = _AxsOspfv3IfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 13),
    _AxsOspfv3IfDesignatedRouter_Type()
)
axsOspfv3IfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfDesignatedRouter.setStatus("mandatory")


class _AxsOspfv3IfBackupDesignatedRouter_Type(RouterID):
    """Custom type axsOspfv3IfBackupDesignatedRouter based on RouterID"""
    defaultHexValue = "00000000"


_AxsOspfv3IfBackupDesignatedRouter_Type.__name__ = "RouterID"
_AxsOspfv3IfBackupDesignatedRouter_Object = MibTableColumn
axsOspfv3IfBackupDesignatedRouter = _AxsOspfv3IfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 15),
    _AxsOspfv3IfBackupDesignatedRouter_Type()
)
axsOspfv3IfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfBackupDesignatedRouter.setStatus("mandatory")
_AxsOspfv3IfEvents_Type = Counter32
_AxsOspfv3IfEvents_Object = MibTableColumn
axsOspfv3IfEvents = _AxsOspfv3IfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 16),
    _AxsOspfv3IfEvents_Type()
)
axsOspfv3IfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfEvents.setStatus("mandatory")
_AxsOspfv3IfStatus_Type = RowStatus
_AxsOspfv3IfStatus_Object = MibTableColumn
axsOspfv3IfStatus = _AxsOspfv3IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 18),
    _AxsOspfv3IfStatus_Type()
)
axsOspfv3IfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfStatus.setStatus("mandatory")


class _AxsOspfv3IfMulticastForwarding_Type(Integer32):
    """Custom type axsOspfv3IfMulticastForwarding based on Integer32"""
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
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_AxsOspfv3IfMulticastForwarding_Type.__name__ = "Integer32"
_AxsOspfv3IfMulticastForwarding_Object = MibTableColumn
axsOspfv3IfMulticastForwarding = _AxsOspfv3IfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 19),
    _AxsOspfv3IfMulticastForwarding_Type()
)
axsOspfv3IfMulticastForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfMulticastForwarding.setStatus("mandatory")


class _AxsOspfv3IfDemand_Type(TruthValue):
    """Custom type axsOspfv3IfDemand based on TruthValue"""
    defaultValue = 2


_AxsOspfv3IfDemand_Type.__name__ = "TruthValue"
_AxsOspfv3IfDemand_Object = MibTableColumn
axsOspfv3IfDemand = _AxsOspfv3IfDemand_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 20),
    _AxsOspfv3IfDemand_Type()
)
axsOspfv3IfDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfDemand.setStatus("mandatory")
_AxsOspfv3IfMetricValue_Type = Metric
_AxsOspfv3IfMetricValue_Object = MibTableColumn
axsOspfv3IfMetricValue = _AxsOspfv3IfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 21),
    _AxsOspfv3IfMetricValue_Type()
)
axsOspfv3IfMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfMetricValue.setStatus("mandatory")
_AxsOspfv3IfLinkScopeLsaCount_Type = Gauge32
_AxsOspfv3IfLinkScopeLsaCount_Object = MibTableColumn
axsOspfv3IfLinkScopeLsaCount = _AxsOspfv3IfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 22),
    _AxsOspfv3IfLinkScopeLsaCount_Type()
)
axsOspfv3IfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfLinkScopeLsaCount.setStatus("mandatory")


class _AxsOspfv3IfLinkLsaCksumSum_Type(Integer32):
    """Custom type axsOspfv3IfLinkLsaCksumSum based on Integer32"""
    defaultValue = 0


_AxsOspfv3IfLinkLsaCksumSum_Type.__name__ = "Integer32"
_AxsOspfv3IfLinkLsaCksumSum_Object = MibTableColumn
axsOspfv3IfLinkLsaCksumSum = _AxsOspfv3IfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 23),
    _AxsOspfv3IfLinkLsaCksumSum_Type()
)
axsOspfv3IfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfLinkLsaCksumSum.setStatus("mandatory")


class _AxsOspfv3IfInstId_Type(Integer32):
    """Custom type axsOspfv3IfInstId based on Integer32"""
    defaultValue = 0


_AxsOspfv3IfInstId_Type.__name__ = "Integer32"
_AxsOspfv3IfInstId_Object = MibTableColumn
axsOspfv3IfInstId = _AxsOspfv3IfInstId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 24),
    _AxsOspfv3IfInstId_Type()
)
axsOspfv3IfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfInstId.setStatus("mandatory")
_AxsOspfv3VirtIfTable_Object = MibTable
axsOspfv3VirtIfTable = _AxsOspfv3VirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8)
)
if mibBuilder.loadTexts:
    axsOspfv3VirtIfTable.setStatus("mandatory")
_AxsOspfv3VirtIfEntry_Object = MibTableRow
axsOspfv3VirtIfEntry = _AxsOspfv3VirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1)
)
axsOspfv3VirtIfEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3VirtIfDomainNumber"),
    (0, "AX4630S", "axsOspfv3VirtIfAreaId"),
    (0, "AX4630S", "axsOspfv3VirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    axsOspfv3VirtIfEntry.setStatus("mandatory")
_AxsOspfv3VirtIfDomainNumber_Type = Integer32
_AxsOspfv3VirtIfDomainNumber_Object = MibTableColumn
axsOspfv3VirtIfDomainNumber = _AxsOspfv3VirtIfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 1),
    _AxsOspfv3VirtIfDomainNumber_Type()
)
axsOspfv3VirtIfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfDomainNumber.setStatus("mandatory")
_AxsOspfv3VirtIfAreaId_Type = AreaID
_AxsOspfv3VirtIfAreaId_Object = MibTableColumn
axsOspfv3VirtIfAreaId = _AxsOspfv3VirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 2),
    _AxsOspfv3VirtIfAreaId_Type()
)
axsOspfv3VirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfAreaId.setStatus("mandatory")
_AxsOspfv3VirtIfNeighbor_Type = RouterID
_AxsOspfv3VirtIfNeighbor_Object = MibTableColumn
axsOspfv3VirtIfNeighbor = _AxsOspfv3VirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 3),
    _AxsOspfv3VirtIfNeighbor_Type()
)
axsOspfv3VirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfNeighbor.setStatus("mandatory")
_AxsOspfv3VirtIfIndex_Type = Ipv6IfIndex
_AxsOspfv3VirtIfIndex_Object = MibTableColumn
axsOspfv3VirtIfIndex = _AxsOspfv3VirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 4),
    _AxsOspfv3VirtIfIndex_Type()
)
axsOspfv3VirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfIndex.setStatus("mandatory")


class _AxsOspfv3VirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type axsOspfv3VirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_AxsOspfv3VirtIfTransitDelay_Type.__name__ = "UpToMaxAge"
_AxsOspfv3VirtIfTransitDelay_Object = MibTableColumn
axsOspfv3VirtIfTransitDelay = _AxsOspfv3VirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 5),
    _AxsOspfv3VirtIfTransitDelay_Type()
)
axsOspfv3VirtIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfTransitDelay.setStatus("mandatory")


class _AxsOspfv3VirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type axsOspfv3VirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_AxsOspfv3VirtIfRetransInterval_Type.__name__ = "UpToMaxAge"
_AxsOspfv3VirtIfRetransInterval_Object = MibTableColumn
axsOspfv3VirtIfRetransInterval = _AxsOspfv3VirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 6),
    _AxsOspfv3VirtIfRetransInterval_Type()
)
axsOspfv3VirtIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfRetransInterval.setStatus("mandatory")


class _AxsOspfv3VirtIfHelloInterval_Type(HelloRange):
    """Custom type axsOspfv3VirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_AxsOspfv3VirtIfHelloInterval_Type.__name__ = "HelloRange"
_AxsOspfv3VirtIfHelloInterval_Object = MibTableColumn
axsOspfv3VirtIfHelloInterval = _AxsOspfv3VirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 7),
    _AxsOspfv3VirtIfHelloInterval_Type()
)
axsOspfv3VirtIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfHelloInterval.setStatus("mandatory")


class _AxsOspfv3VirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type axsOspfv3VirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_AxsOspfv3VirtIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_AxsOspfv3VirtIfRtrDeadInterval_Object = MibTableColumn
axsOspfv3VirtIfRtrDeadInterval = _AxsOspfv3VirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 8),
    _AxsOspfv3VirtIfRtrDeadInterval_Type()
)
axsOspfv3VirtIfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfRtrDeadInterval.setStatus("mandatory")


class _AxsOspfv3VirtIfState_Type(Integer32):
    """Custom type axsOspfv3VirtIfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_AxsOspfv3VirtIfState_Type.__name__ = "Integer32"
_AxsOspfv3VirtIfState_Object = MibTableColumn
axsOspfv3VirtIfState = _AxsOspfv3VirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 9),
    _AxsOspfv3VirtIfState_Type()
)
axsOspfv3VirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfState.setStatus("mandatory")
_AxsOspfv3VirtIfEvents_Type = Counter32
_AxsOspfv3VirtIfEvents_Object = MibTableColumn
axsOspfv3VirtIfEvents = _AxsOspfv3VirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 10),
    _AxsOspfv3VirtIfEvents_Type()
)
axsOspfv3VirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfEvents.setStatus("mandatory")
_AxsOspfv3VirtIfStatus_Type = RowStatus
_AxsOspfv3VirtIfStatus_Object = MibTableColumn
axsOspfv3VirtIfStatus = _AxsOspfv3VirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 11),
    _AxsOspfv3VirtIfStatus_Type()
)
axsOspfv3VirtIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfStatus.setStatus("mandatory")
_AxsOspfv3VirtIfLinkScopeLsaCount_Type = Gauge32
_AxsOspfv3VirtIfLinkScopeLsaCount_Object = MibTableColumn
axsOspfv3VirtIfLinkScopeLsaCount = _AxsOspfv3VirtIfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 12),
    _AxsOspfv3VirtIfLinkScopeLsaCount_Type()
)
axsOspfv3VirtIfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfLinkScopeLsaCount.setStatus("mandatory")


class _AxsOspfv3VirtIfLinkLsaCksumSum_Type(Integer32):
    """Custom type axsOspfv3VirtIfLinkLsaCksumSum based on Integer32"""
    defaultValue = 0


_AxsOspfv3VirtIfLinkLsaCksumSum_Type.__name__ = "Integer32"
_AxsOspfv3VirtIfLinkLsaCksumSum_Object = MibTableColumn
axsOspfv3VirtIfLinkLsaCksumSum = _AxsOspfv3VirtIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 13),
    _AxsOspfv3VirtIfLinkLsaCksumSum_Type()
)
axsOspfv3VirtIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfLinkLsaCksumSum.setStatus("mandatory")
_AxsOspfv3NbrTable_Object = MibTable
axsOspfv3NbrTable = _AxsOspfv3NbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9)
)
if mibBuilder.loadTexts:
    axsOspfv3NbrTable.setStatus("mandatory")
_AxsOspfv3NbrEntry_Object = MibTableRow
axsOspfv3NbrEntry = _AxsOspfv3NbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1)
)
axsOspfv3NbrEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3NbrDomainNumber"),
    (0, "AX4630S", "axsOspfv3NbrIfIndex"),
    (0, "AX4630S", "axsOspfv3NbrIpv6Addr"),
)
if mibBuilder.loadTexts:
    axsOspfv3NbrEntry.setStatus("mandatory")
_AxsOspfv3NbrDomainNumber_Type = Integer32
_AxsOspfv3NbrDomainNumber_Object = MibTableColumn
axsOspfv3NbrDomainNumber = _AxsOspfv3NbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 1),
    _AxsOspfv3NbrDomainNumber_Type()
)
axsOspfv3NbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrDomainNumber.setStatus("mandatory")
_AxsOspfv3NbrIfIndex_Type = Ipv6IfIndex
_AxsOspfv3NbrIfIndex_Object = MibTableColumn
axsOspfv3NbrIfIndex = _AxsOspfv3NbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 2),
    _AxsOspfv3NbrIfIndex_Type()
)
axsOspfv3NbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrIfIndex.setStatus("mandatory")
_AxsOspfv3NbrIpv6Addr_Type = Ipv6Address
_AxsOspfv3NbrIpv6Addr_Object = MibTableColumn
axsOspfv3NbrIpv6Addr = _AxsOspfv3NbrIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 3),
    _AxsOspfv3NbrIpv6Addr_Type()
)
axsOspfv3NbrIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrIpv6Addr.setStatus("mandatory")
_AxsOspfv3NbrRtrId_Type = RouterID
_AxsOspfv3NbrRtrId_Object = MibTableColumn
axsOspfv3NbrRtrId = _AxsOspfv3NbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 4),
    _AxsOspfv3NbrRtrId_Type()
)
axsOspfv3NbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrRtrId.setStatus("mandatory")


class _AxsOspfv3NbrOptions_Type(Integer32):
    """Custom type axsOspfv3NbrOptions based on Integer32"""
    defaultValue = 0


_AxsOspfv3NbrOptions_Type.__name__ = "Integer32"
_AxsOspfv3NbrOptions_Object = MibTableColumn
axsOspfv3NbrOptions = _AxsOspfv3NbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 5),
    _AxsOspfv3NbrOptions_Type()
)
axsOspfv3NbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrOptions.setStatus("mandatory")


class _AxsOspfv3NbrPriority_Type(DesignatedRouterPriority):
    """Custom type axsOspfv3NbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_AxsOspfv3NbrPriority_Type.__name__ = "DesignatedRouterPriority"
_AxsOspfv3NbrPriority_Object = MibTableColumn
axsOspfv3NbrPriority = _AxsOspfv3NbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 6),
    _AxsOspfv3NbrPriority_Type()
)
axsOspfv3NbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrPriority.setStatus("mandatory")


class _AxsOspfv3NbrState_Type(Integer32):
    """Custom type axsOspfv3NbrState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_AxsOspfv3NbrState_Type.__name__ = "Integer32"
_AxsOspfv3NbrState_Object = MibTableColumn
axsOspfv3NbrState = _AxsOspfv3NbrState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 7),
    _AxsOspfv3NbrState_Type()
)
axsOspfv3NbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrState.setStatus("mandatory")
_AxsOspfv3NbrEvents_Type = Counter32
_AxsOspfv3NbrEvents_Object = MibTableColumn
axsOspfv3NbrEvents = _AxsOspfv3NbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 8),
    _AxsOspfv3NbrEvents_Type()
)
axsOspfv3NbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrEvents.setStatus("mandatory")
_AxsOspfv3NbrLsRetransQLen_Type = Gauge32
_AxsOspfv3NbrLsRetransQLen_Object = MibTableColumn
axsOspfv3NbrLsRetransQLen = _AxsOspfv3NbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 9),
    _AxsOspfv3NbrLsRetransQLen_Type()
)
axsOspfv3NbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrLsRetransQLen.setStatus("mandatory")
_AxsOspfv3NbrHelloSuppressed_Type = TruthValue
_AxsOspfv3NbrHelloSuppressed_Object = MibTableColumn
axsOspfv3NbrHelloSuppressed = _AxsOspfv3NbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 12),
    _AxsOspfv3NbrHelloSuppressed_Type()
)
axsOspfv3NbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrHelloSuppressed.setStatus("mandatory")
_AxsOspfv3NbrIfId_Type = Ipv6IfIndex
_AxsOspfv3NbrIfId_Object = MibTableColumn
axsOspfv3NbrIfId = _AxsOspfv3NbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 13),
    _AxsOspfv3NbrIfId_Type()
)
axsOspfv3NbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrIfId.setStatus("mandatory")
_AxsOspfv3VirtNbrTable_Object = MibTable
axsOspfv3VirtNbrTable = _AxsOspfv3VirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10)
)
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrTable.setStatus("mandatory")
_AxsOspfv3VirtNbrEntry_Object = MibTableRow
axsOspfv3VirtNbrEntry = _AxsOspfv3VirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1)
)
axsOspfv3VirtNbrEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3VirtNbrDomainNumber"),
    (0, "AX4630S", "axsOspfv3VirtNbrArea"),
    (0, "AX4630S", "axsOspfv3VirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrEntry.setStatus("mandatory")
_AxsOspfv3VirtNbrDomainNumber_Type = Integer32
_AxsOspfv3VirtNbrDomainNumber_Object = MibTableColumn
axsOspfv3VirtNbrDomainNumber = _AxsOspfv3VirtNbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 1),
    _AxsOspfv3VirtNbrDomainNumber_Type()
)
axsOspfv3VirtNbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrDomainNumber.setStatus("mandatory")
_AxsOspfv3VirtNbrArea_Type = AreaID
_AxsOspfv3VirtNbrArea_Object = MibTableColumn
axsOspfv3VirtNbrArea = _AxsOspfv3VirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 2),
    _AxsOspfv3VirtNbrArea_Type()
)
axsOspfv3VirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrArea.setStatus("mandatory")
_AxsOspfv3VirtNbrRtrId_Type = RouterID
_AxsOspfv3VirtNbrRtrId_Object = MibTableColumn
axsOspfv3VirtNbrRtrId = _AxsOspfv3VirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 3),
    _AxsOspfv3VirtNbrRtrId_Type()
)
axsOspfv3VirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrRtrId.setStatus("mandatory")
_AxsOspfv3VirtNbrIfIndex_Type = Ipv6IfIndex
_AxsOspfv3VirtNbrIfIndex_Object = MibTableColumn
axsOspfv3VirtNbrIfIndex = _AxsOspfv3VirtNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 4),
    _AxsOspfv3VirtNbrIfIndex_Type()
)
axsOspfv3VirtNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrIfIndex.setStatus("mandatory")
_AxsOspfv3VirtNbrIpv6Addr_Type = Ipv6Address
_AxsOspfv3VirtNbrIpv6Addr_Object = MibTableColumn
axsOspfv3VirtNbrIpv6Addr = _AxsOspfv3VirtNbrIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 5),
    _AxsOspfv3VirtNbrIpv6Addr_Type()
)
axsOspfv3VirtNbrIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrIpv6Addr.setStatus("mandatory")
_AxsOspfv3VirtNbrOptions_Type = Integer32
_AxsOspfv3VirtNbrOptions_Object = MibTableColumn
axsOspfv3VirtNbrOptions = _AxsOspfv3VirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 6),
    _AxsOspfv3VirtNbrOptions_Type()
)
axsOspfv3VirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrOptions.setStatus("mandatory")


class _AxsOspfv3VirtNbrState_Type(Integer32):
    """Custom type axsOspfv3VirtNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_AxsOspfv3VirtNbrState_Type.__name__ = "Integer32"
_AxsOspfv3VirtNbrState_Object = MibTableColumn
axsOspfv3VirtNbrState = _AxsOspfv3VirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 7),
    _AxsOspfv3VirtNbrState_Type()
)
axsOspfv3VirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrState.setStatus("mandatory")
_AxsOspfv3VirtNbrEvents_Type = Counter32
_AxsOspfv3VirtNbrEvents_Object = MibTableColumn
axsOspfv3VirtNbrEvents = _AxsOspfv3VirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 8),
    _AxsOspfv3VirtNbrEvents_Type()
)
axsOspfv3VirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrEvents.setStatus("mandatory")
_AxsOspfv3VirtNbrLsRetransQLen_Type = Gauge32
_AxsOspfv3VirtNbrLsRetransQLen_Object = MibTableColumn
axsOspfv3VirtNbrLsRetransQLen = _AxsOspfv3VirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 9),
    _AxsOspfv3VirtNbrLsRetransQLen_Type()
)
axsOspfv3VirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrLsRetransQLen.setStatus("mandatory")
_AxsOspfv3VirtNbrHelloSuppressed_Type = TruthValue
_AxsOspfv3VirtNbrHelloSuppressed_Object = MibTableColumn
axsOspfv3VirtNbrHelloSuppressed = _AxsOspfv3VirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 10),
    _AxsOspfv3VirtNbrHelloSuppressed_Type()
)
axsOspfv3VirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrHelloSuppressed.setStatus("mandatory")
_AxsOspfv3VirtNbrIfId_Type = Ipv6IfIndex
_AxsOspfv3VirtNbrIfId_Object = MibTableColumn
axsOspfv3VirtNbrIfId = _AxsOspfv3VirtNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 11),
    _AxsOspfv3VirtNbrIfId_Type()
)
axsOspfv3VirtNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrIfId.setStatus("mandatory")
_AxsOspfv3AreaAggregateTable_Object = MibTable
axsOspfv3AreaAggregateTable = _AxsOspfv3AreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11)
)
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateTable.setStatus("mandatory")
_AxsOspfv3AreaAggregateEntry_Object = MibTableRow
axsOspfv3AreaAggregateEntry = _AxsOspfv3AreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1)
)
axsOspfv3AreaAggregateEntry.setIndexNames(
    (0, "AX4630S", "axsOspfv3AreaAggregateDomainNumber"),
    (0, "AX4630S", "axsOspfv3AreaAggregateAreaID"),
    (0, "AX4630S", "axsOspfv3AreaAggregateAreaLsdbType"),
    (0, "AX4630S", "axsOspfv3AreaAggregateIndex"),
)
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateEntry.setStatus("mandatory")
_AxsOspfv3AreaAggregateDomainNumber_Type = Integer32
_AxsOspfv3AreaAggregateDomainNumber_Object = MibTableColumn
axsOspfv3AreaAggregateDomainNumber = _AxsOspfv3AreaAggregateDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 1),
    _AxsOspfv3AreaAggregateDomainNumber_Type()
)
axsOspfv3AreaAggregateDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateDomainNumber.setStatus("mandatory")
_AxsOspfv3AreaAggregateAreaID_Type = AreaID
_AxsOspfv3AreaAggregateAreaID_Object = MibTableColumn
axsOspfv3AreaAggregateAreaID = _AxsOspfv3AreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 2),
    _AxsOspfv3AreaAggregateAreaID_Type()
)
axsOspfv3AreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateAreaID.setStatus("mandatory")


class _AxsOspfv3AreaAggregateAreaLsdbType_Type(Integer32):
    """Custom type axsOspfv3AreaAggregateAreaLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8195,
              8199)
        )
    )
    namedValues = NamedValues(
        *(("interAreaPrefixLsa", 8195),
          ("nssaExternalLsa", 8199))
    )


_AxsOspfv3AreaAggregateAreaLsdbType_Type.__name__ = "Integer32"
_AxsOspfv3AreaAggregateAreaLsdbType_Object = MibTableColumn
axsOspfv3AreaAggregateAreaLsdbType = _AxsOspfv3AreaAggregateAreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 3),
    _AxsOspfv3AreaAggregateAreaLsdbType_Type()
)
axsOspfv3AreaAggregateAreaLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateAreaLsdbType.setStatus("mandatory")


class _AxsOspfv3AreaAggregateIndex_Type(Integer32):
    """Custom type axsOspfv3AreaAggregateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxsOspfv3AreaAggregateIndex_Type.__name__ = "Integer32"
_AxsOspfv3AreaAggregateIndex_Object = MibTableColumn
axsOspfv3AreaAggregateIndex = _AxsOspfv3AreaAggregateIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 4),
    _AxsOspfv3AreaAggregateIndex_Type()
)
axsOspfv3AreaAggregateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateIndex.setStatus("mandatory")
_AxsOspfv3AreaAggregatePrefix_Type = Ipv6AddressPrefix
_AxsOspfv3AreaAggregatePrefix_Object = MibTableColumn
axsOspfv3AreaAggregatePrefix = _AxsOspfv3AreaAggregatePrefix_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 5),
    _AxsOspfv3AreaAggregatePrefix_Type()
)
axsOspfv3AreaAggregatePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregatePrefix.setStatus("mandatory")


class _AxsOspfv3AreaAggregatePrefixLen_Type(Integer32):
    """Custom type axsOspfv3AreaAggregatePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_AxsOspfv3AreaAggregatePrefixLen_Type.__name__ = "Integer32"
_AxsOspfv3AreaAggregatePrefixLen_Object = MibTableColumn
axsOspfv3AreaAggregatePrefixLen = _AxsOspfv3AreaAggregatePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 6),
    _AxsOspfv3AreaAggregatePrefixLen_Type()
)
axsOspfv3AreaAggregatePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregatePrefixLen.setStatus("mandatory")
_AxsOspfv3AreaAggregateStatus_Type = RowStatus
_AxsOspfv3AreaAggregateStatus_Object = MibTableColumn
axsOspfv3AreaAggregateStatus = _AxsOspfv3AreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 7),
    _AxsOspfv3AreaAggregateStatus_Type()
)
axsOspfv3AreaAggregateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateStatus.setStatus("mandatory")


class _AxsOspfv3AreaAggregateEffect_Type(Integer32):
    """Custom type axsOspfv3AreaAggregateEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2))
    )


_AxsOspfv3AreaAggregateEffect_Type.__name__ = "Integer32"
_AxsOspfv3AreaAggregateEffect_Object = MibTableColumn
axsOspfv3AreaAggregateEffect = _AxsOspfv3AreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 8),
    _AxsOspfv3AreaAggregateEffect_Type()
)
axsOspfv3AreaAggregateEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateEffect.setStatus("mandatory")
_AxsUlr_ObjectIdentity = ObjectIdentity
axsUlr = _AxsUlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20)
)
_AxsUlrGlobalInfo_ObjectIdentity = ObjectIdentity
axsUlrGlobalInfo = _AxsUlrGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 1)
)
_AxsUlrID_Type = MacAddress
_AxsUlrID_Object = MibScalar
axsUlrID = _AxsUlrID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 1, 2),
    _AxsUlrID_Type()
)
axsUlrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrID.setStatus("mandatory")
_AxsUlrConfigurationPortCounts_Type = Integer32
_AxsUlrConfigurationPortCounts_Object = MibScalar
axsUlrConfigurationPortCounts = _AxsUlrConfigurationPortCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 1, 3),
    _AxsUlrConfigurationPortCounts_Type()
)
axsUlrConfigurationPortCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrConfigurationPortCounts.setStatus("mandatory")
_AxsUlrStartupActivePortSelection_Type = Integer32
_AxsUlrStartupActivePortSelection_Object = MibScalar
axsUlrStartupActivePortSelection = _AxsUlrStartupActivePortSelection_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 1, 4),
    _AxsUlrStartupActivePortSelection_Type()
)
axsUlrStartupActivePortSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrStartupActivePortSelection.setStatus("mandatory")
_AxsUlrPortTable_Object = MibTable
axsUlrPortTable = _AxsUlrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2)
)
if mibBuilder.loadTexts:
    axsUlrPortTable.setStatus("mandatory")
_AxsUlrPortEntry_Object = MibTableRow
axsUlrPortEntry = _AxsUlrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1)
)
axsUlrPortEntry.setIndexNames(
    (0, "AX4630S", "axsUlrPortIfIndex"),
)
if mibBuilder.loadTexts:
    axsUlrPortEntry.setStatus("mandatory")
_AxsUlrPortIfIndex_Type = Integer32
_AxsUlrPortIfIndex_Object = MibTableColumn
axsUlrPortIfIndex = _AxsUlrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 1),
    _AxsUlrPortIfIndex_Type()
)
axsUlrPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrPortIfIndex.setStatus("mandatory")
_AxsUlrPortType_Type = Integer32
_AxsUlrPortType_Object = MibTableColumn
axsUlrPortType = _AxsUlrPortType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 2),
    _AxsUlrPortType_Type()
)
axsUlrPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrPortType.setStatus("mandatory")
_AxsUlrPairedPortIfIndex_Type = Integer32
_AxsUlrPairedPortIfIndex_Object = MibTableColumn
axsUlrPairedPortIfIndex = _AxsUlrPairedPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 3),
    _AxsUlrPairedPortIfIndex_Type()
)
axsUlrPairedPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrPairedPortIfIndex.setStatus("mandatory")


class _AxsUlrPortStatus_Type(Integer32):
    """Custom type axsUlrPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("down", 2),
          ("blocking", 3))
    )


_AxsUlrPortStatus_Type.__name__ = "Integer32"
_AxsUlrPortStatus_Object = MibTableColumn
axsUlrPortStatus = _AxsUlrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 4),
    _AxsUlrPortStatus_Type()
)
axsUlrPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrPortStatus.setStatus("mandatory")


class _AxsUlrPairedPortStatus_Type(Integer32):
    """Custom type axsUlrPairedPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("down", 2),
          ("blocking", 3))
    )


_AxsUlrPairedPortStatus_Type.__name__ = "Integer32"
_AxsUlrPairedPortStatus_Object = MibTableColumn
axsUlrPairedPortStatus = _AxsUlrPairedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 5),
    _AxsUlrPairedPortStatus_Type()
)
axsUlrPairedPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrPairedPortStatus.setStatus("mandatory")


class _AxsUlrAutoChangeToPrimary_Type(Integer32):
    """Custom type axsUlrAutoChangeToPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AxsUlrAutoChangeToPrimary_Type.__name__ = "Integer32"
_AxsUlrAutoChangeToPrimary_Object = MibTableColumn
axsUlrAutoChangeToPrimary = _AxsUlrAutoChangeToPrimary_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 6),
    _AxsUlrAutoChangeToPrimary_Type()
)
axsUlrAutoChangeToPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrAutoChangeToPrimary.setStatus("mandatory")
_AxsUlrAutoChangeToPrimaryDelay_Type = Integer32
_AxsUlrAutoChangeToPrimaryDelay_Object = MibTableColumn
axsUlrAutoChangeToPrimaryDelay = _AxsUlrAutoChangeToPrimaryDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 7),
    _AxsUlrAutoChangeToPrimaryDelay_Type()
)
axsUlrAutoChangeToPrimaryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrAutoChangeToPrimaryDelay.setStatus("mandatory")
_AxsUlrAutoChangeToPrimaryRest_Type = Integer32
_AxsUlrAutoChangeToPrimaryRest_Object = MibTableColumn
axsUlrAutoChangeToPrimaryRest = _AxsUlrAutoChangeToPrimaryRest_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 8),
    _AxsUlrAutoChangeToPrimaryRest_Type()
)
axsUlrAutoChangeToPrimaryRest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrAutoChangeToPrimaryRest.setStatus("mandatory")


class _AxsUlrStartupActivePortSelectionStatus_Type(Integer32):
    """Custom type axsUlrStartupActivePortSelectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AxsUlrStartupActivePortSelectionStatus_Type.__name__ = "Integer32"
_AxsUlrStartupActivePortSelectionStatus_Object = MibTableColumn
axsUlrStartupActivePortSelectionStatus = _AxsUlrStartupActivePortSelectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 9),
    _AxsUlrStartupActivePortSelectionStatus_Type()
)
axsUlrStartupActivePortSelectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrStartupActivePortSelectionStatus.setStatus("mandatory")


class _AxsUlrFlushTransmit_Type(Integer32):
    """Custom type axsUlrFlushTransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AxsUlrFlushTransmit_Type.__name__ = "Integer32"
_AxsUlrFlushTransmit_Object = MibTableColumn
axsUlrFlushTransmit = _AxsUlrFlushTransmit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 10),
    _AxsUlrFlushTransmit_Type()
)
axsUlrFlushTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrFlushTransmit.setStatus("mandatory")
_AxsUlrFlushVlan_Type = Integer32
_AxsUlrFlushVlan_Object = MibTableColumn
axsUlrFlushVlan = _AxsUlrFlushVlan_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 11),
    _AxsUlrFlushVlan_Type()
)
axsUlrFlushVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrFlushVlan.setStatus("mandatory")
_AxsUlrMacAddressUpdateTransmit_Type = Integer32
_AxsUlrMacAddressUpdateTransmit_Object = MibTableColumn
axsUlrMacAddressUpdateTransmit = _AxsUlrMacAddressUpdateTransmit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 12),
    _AxsUlrMacAddressUpdateTransmit_Type()
)
axsUlrMacAddressUpdateTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrMacAddressUpdateTransmit.setStatus("mandatory")
_AxsUlrLastActivePortDecisionTime_Type = TimeStamp
_AxsUlrLastActivePortDecisionTime_Object = MibTableColumn
axsUlrLastActivePortDecisionTime = _AxsUlrLastActivePortDecisionTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 13),
    _AxsUlrLastActivePortDecisionTime_Type()
)
axsUlrLastActivePortDecisionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrLastActivePortDecisionTime.setStatus("mandatory")
_AxsUlrLastFlushTransmitTime_Type = TimeStamp
_AxsUlrLastFlushTransmitTime_Object = MibTableColumn
axsUlrLastFlushTransmitTime = _AxsUlrLastFlushTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 14),
    _AxsUlrLastFlushTransmitTime_Type()
)
axsUlrLastFlushTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrLastFlushTransmitTime.setStatus("mandatory")
_AxsUlrLastMacUpdateTransmitTime_Type = TimeStamp
_AxsUlrLastMacUpdateTransmitTime_Object = MibTableColumn
axsUlrLastMacUpdateTransmitTime = _AxsUlrLastMacUpdateTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 15),
    _AxsUlrLastMacUpdateTransmitTime_Type()
)
axsUlrLastMacUpdateTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrLastMacUpdateTransmitTime.setStatus("mandatory")


class _AxsUlrLastChangeFactor_Type(Integer32):
    """Custom type axsUlrLastChangeFactor based on Integer32"""
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
        *(("command", 1),
          ("configure", 2),
          ("primary-down", 3),
          ("primary-up", 4),
          ("secondary-down", 5),
          ("secondary-up", 6),
          ("preemption", 7))
    )


_AxsUlrLastChangeFactor_Type.__name__ = "Integer32"
_AxsUlrLastChangeFactor_Object = MibTableColumn
axsUlrLastChangeFactor = _AxsUlrLastChangeFactor_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 16),
    _AxsUlrLastChangeFactor_Type()
)
axsUlrLastChangeFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrLastChangeFactor.setStatus("mandatory")
_AxsUlrFlushTransmitTotalPackets_Type = Integer32
_AxsUlrFlushTransmitTotalPackets_Object = MibTableColumn
axsUlrFlushTransmitTotalPackets = _AxsUlrFlushTransmitTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 17),
    _AxsUlrFlushTransmitTotalPackets_Type()
)
axsUlrFlushTransmitTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrFlushTransmitTotalPackets.setStatus("mandatory")
_AxsUlrMacAddressUpdateTransmitTotalPackets_Type = Integer32
_AxsUlrMacAddressUpdateTransmitTotalPackets_Object = MibTableColumn
axsUlrMacAddressUpdateTransmitTotalPackets = _AxsUlrMacAddressUpdateTransmitTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 18),
    _AxsUlrMacAddressUpdateTransmitTotalPackets_Type()
)
axsUlrMacAddressUpdateTransmitTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrMacAddressUpdateTransmitTotalPackets.setStatus("mandatory")
_AxsUlrMacAddressUpdateTransmitOverFlow_Type = Integer32
_AxsUlrMacAddressUpdateTransmitOverFlow_Object = MibTableColumn
axsUlrMacAddressUpdateTransmitOverFlow = _AxsUlrMacAddressUpdateTransmitOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 19),
    _AxsUlrMacAddressUpdateTransmitOverFlow_Type()
)
axsUlrMacAddressUpdateTransmitOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrMacAddressUpdateTransmitOverFlow.setStatus("mandatory")
_AxsUlrActiveDecisionCount_Type = Integer32
_AxsUlrActiveDecisionCount_Object = MibTableColumn
axsUlrActiveDecisionCount = _AxsUlrActiveDecisionCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 2, 1, 20),
    _AxsUlrActiveDecisionCount_Type()
)
axsUlrActiveDecisionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrActiveDecisionCount.setStatus("mandatory")
_AxsStatic_ObjectIdentity = ObjectIdentity
axsStatic = _AxsStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38)
)
_AxsStaticTable_Object = MibTable
axsStaticTable = _AxsStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 1)
)
if mibBuilder.loadTexts:
    axsStaticTable.setStatus("mandatory")
_AxsStaticGatewayEntry_Object = MibTableRow
axsStaticGatewayEntry = _AxsStaticGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 1, 1)
)
axsStaticGatewayEntry.setIndexNames(
    (0, "AX4630S", "axsStaticGatewayAddr"),
)
if mibBuilder.loadTexts:
    axsStaticGatewayEntry.setStatus("mandatory")
_AxsStaticGatewayAddr_Type = IpAddress
_AxsStaticGatewayAddr_Object = MibTableColumn
axsStaticGatewayAddr = _AxsStaticGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 1, 1, 1),
    _AxsStaticGatewayAddr_Type()
)
axsStaticGatewayAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStaticGatewayAddr.setStatus("mandatory")


class _AxsStaticGatewayState_Type(Integer32):
    """Custom type axsStaticGatewayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 2))
    )


_AxsStaticGatewayState_Type.__name__ = "Integer32"
_AxsStaticGatewayState_Object = MibTableColumn
axsStaticGatewayState = _AxsStaticGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 1, 1, 2),
    _AxsStaticGatewayState_Type()
)
axsStaticGatewayState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStaticGatewayState.setStatus("mandatory")
_AxsStaticTrap_ObjectIdentity = ObjectIdentity
axsStaticTrap = _AxsStaticTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 2)
)
_AxsStaticIpv6Table_Object = MibTable
axsStaticIpv6Table = _AxsStaticIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 3)
)
if mibBuilder.loadTexts:
    axsStaticIpv6Table.setStatus("mandatory")
_AxsStaticIpv6GatewayEntry_Object = MibTableRow
axsStaticIpv6GatewayEntry = _AxsStaticIpv6GatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 3, 1)
)
axsStaticIpv6GatewayEntry.setIndexNames(
    (0, "AX4630S", "axsStaticIpv6Ifindex"),
    (0, "AX4630S", "axsStaticIpv6GatewayAddr"),
)
if mibBuilder.loadTexts:
    axsStaticIpv6GatewayEntry.setStatus("mandatory")
_AxsStaticIpv6Ifindex_Type = Integer32
_AxsStaticIpv6Ifindex_Object = MibTableColumn
axsStaticIpv6Ifindex = _AxsStaticIpv6Ifindex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 3, 1, 1),
    _AxsStaticIpv6Ifindex_Type()
)
axsStaticIpv6Ifindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStaticIpv6Ifindex.setStatus("mandatory")
_AxsStaticIpv6GatewayAddr_Type = Ipv6Address
_AxsStaticIpv6GatewayAddr_Object = MibTableColumn
axsStaticIpv6GatewayAddr = _AxsStaticIpv6GatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 3, 1, 2),
    _AxsStaticIpv6GatewayAddr_Type()
)
axsStaticIpv6GatewayAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStaticIpv6GatewayAddr.setStatus("mandatory")


class _AxsStaticIpv6GatewayState_Type(Integer32):
    """Custom type axsStaticIpv6GatewayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 2))
    )


_AxsStaticIpv6GatewayState_Type.__name__ = "Integer32"
_AxsStaticIpv6GatewayState_Object = MibTableColumn
axsStaticIpv6GatewayState = _AxsStaticIpv6GatewayState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 3, 1, 3),
    _AxsStaticIpv6GatewayState_Type()
)
axsStaticIpv6GatewayState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStaticIpv6GatewayState.setStatus("mandatory")
_AxsTrackObject_ObjectIdentity = ObjectIdentity
axsTrackObject = _AxsTrackObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41)
)
_AxsTrackObjectGeneralGroup_ObjectIdentity = ObjectIdentity
axsTrackObjectGeneralGroup = _AxsTrackObjectGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 1)
)
_AxsTrackObjectGeneralLastChange_Type = TimeTicks
_AxsTrackObjectGeneralLastChange_Object = MibScalar
axsTrackObjectGeneralLastChange = _AxsTrackObjectGeneralLastChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 1, 1),
    _AxsTrackObjectGeneralLastChange_Type()
)
axsTrackObjectGeneralLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsTrackObjectGeneralLastChange.setStatus("mandatory")
_AxsTrackObjectTraps_ObjectIdentity = ObjectIdentity
axsTrackObjectTraps = _AxsTrackObjectTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 2)
)
_AxsTrackObjectTable_Object = MibTable
axsTrackObjectTable = _AxsTrackObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 3)
)
if mibBuilder.loadTexts:
    axsTrackObjectTable.setStatus("mandatory")
_AxsTrackObjectEntry_Object = MibTableRow
axsTrackObjectEntry = _AxsTrackObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 3, 1)
)
axsTrackObjectEntry.setIndexNames(
    (0, "AX4630S", "axsTrackObjectId"),
)
if mibBuilder.loadTexts:
    axsTrackObjectEntry.setStatus("mandatory")
_AxsTrackObjectId_Type = Integer32
_AxsTrackObjectId_Object = MibTableColumn
axsTrackObjectId = _AxsTrackObjectId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 3, 1, 1),
    _AxsTrackObjectId_Type()
)
axsTrackObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsTrackObjectId.setStatus("mandatory")


class _AxsTrackObjectState_Type(Integer32):
    """Custom type axsTrackObjectState based on Integer32"""
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


_AxsTrackObjectState_Type.__name__ = "Integer32"
_AxsTrackObjectState_Object = MibTableColumn
axsTrackObjectState = _AxsTrackObjectState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 3, 1, 2),
    _AxsTrackObjectState_Type()
)
axsTrackObjectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsTrackObjectState.setStatus("mandatory")


class _AxsTrackObjectOperation_Type(Integer32):
    """Custom type axsTrackObjectOperation based on Integer32"""
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
        *(("active", 1),
          ("transit", 2),
          ("disabled", 3),
          ("init", 4),
          ("aging", 5))
    )


_AxsTrackObjectOperation_Type.__name__ = "Integer32"
_AxsTrackObjectOperation_Object = MibTableColumn
axsTrackObjectOperation = _AxsTrackObjectOperation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 3, 1, 3),
    _AxsTrackObjectOperation_Type()
)
axsTrackObjectOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsTrackObjectOperation.setStatus("mandatory")


class _AxsTrackObjectType_Type(Integer32):
    """Custom type axsTrackObjectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4-icmp", 1)
    )


_AxsTrackObjectType_Type.__name__ = "Integer32"
_AxsTrackObjectType_Object = MibTableColumn
axsTrackObjectType = _AxsTrackObjectType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 3, 1, 4),
    _AxsTrackObjectType_Type()
)
axsTrackObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsTrackObjectType.setStatus("mandatory")
_AxsTrackObjectNetIndex_Type = Integer32
_AxsTrackObjectNetIndex_Object = MibTableColumn
axsTrackObjectNetIndex = _AxsTrackObjectNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 3, 1, 5),
    _AxsTrackObjectNetIndex_Type()
)
axsTrackObjectNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsTrackObjectNetIndex.setStatus("mandatory")
_AxsPolicyBase_ObjectIdentity = ObjectIdentity
axsPolicyBase = _AxsPolicyBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 45)
)
_AxsPolicyBaseRouting_ObjectIdentity = ObjectIdentity
axsPolicyBaseRouting = _AxsPolicyBaseRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 45, 1)
)
_AxsPolicyBaseRoutingChangeListNumber_Type = Unsigned32
_AxsPolicyBaseRoutingChangeListNumber_Object = MibScalar
axsPolicyBaseRoutingChangeListNumber = _AxsPolicyBaseRoutingChangeListNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 45, 1, 1),
    _AxsPolicyBaseRoutingChangeListNumber_Type()
)
axsPolicyBaseRoutingChangeListNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsPolicyBaseRoutingChangeListNumber.setStatus("mandatory")
_AxsPolicyBaseRoutingChangeSequenceNumber_Type = Unsigned32
_AxsPolicyBaseRoutingChangeSequenceNumber_Object = MibScalar
axsPolicyBaseRoutingChangeSequenceNumber = _AxsPolicyBaseRoutingChangeSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 45, 1, 2),
    _AxsPolicyBaseRoutingChangeSequenceNumber_Type()
)
axsPolicyBaseRoutingChangeSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsPolicyBaseRoutingChangeSequenceNumber.setStatus("mandatory")
_AxsBootManagement_ObjectIdentity = ObjectIdentity
axsBootManagement = _AxsBootManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 51)
)


class _AxsBootReason_Type(Integer32):
    """Custom type axsBootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("power-on", 1),
          ("reload", 2),
          ("system-fault", 3),
          ("system-stall", 4),
          ("reset", 5),
          ("fail-over", 6),
          ("default-restart", 7),
          ("wake-on-rtc", 9),
          ("wake-on-reset", 10))
    )


_AxsBootReason_Type.__name__ = "Integer32"
_AxsBootReason_Object = MibScalar
axsBootReason = _AxsBootReason_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 51, 1),
    _AxsBootReason_Type()
)
axsBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsBootReason.setStatus("mandatory")
_AxsLogin_ObjectIdentity = ObjectIdentity
axsLogin = _AxsLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52)
)
_AxsLoginName_Type = DisplayString
_AxsLoginName_Object = MibScalar
axsLoginName = _AxsLoginName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 1),
    _AxsLoginName_Type()
)
axsLoginName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLoginName.setStatus("mandatory")
_AxsLoginTime_Type = DisplayString
_AxsLoginTime_Object = MibScalar
axsLoginTime = _AxsLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 2),
    _AxsLoginTime_Type()
)
axsLoginTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLoginTime.setStatus("mandatory")
_AxsLogoutTime_Type = DisplayString
_AxsLogoutTime_Object = MibScalar
axsLogoutTime = _AxsLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 3),
    _AxsLogoutTime_Type()
)
axsLogoutTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLogoutTime.setStatus("mandatory")
_AxsLoginFailureTime_Type = DisplayString
_AxsLoginFailureTime_Object = MibScalar
axsLoginFailureTime = _AxsLoginFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 4),
    _AxsLoginFailureTime_Type()
)
axsLoginFailureTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLoginFailureTime.setStatus("mandatory")
_AxsLoginLocation_Type = DisplayString
_AxsLoginLocation_Object = MibScalar
axsLoginLocation = _AxsLoginLocation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 5),
    _AxsLoginLocation_Type()
)
axsLoginLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLoginLocation.setStatus("mandatory")
_AxsLoginLine_Type = DisplayString
_AxsLoginLine_Object = MibScalar
axsLoginLine = _AxsLoginLine_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 6),
    _AxsLoginLine_Type()
)
axsLoginLine.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLoginLine.setStatus("mandatory")


class _AxsLogoutStatus_Type(Integer32):
    """Custom type axsLogoutStatus based on Integer32"""
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
        *(("error", 1),
          ("success", 2),
          ("timeout", 3),
          ("disconnect", 4),
          ("force", 5))
    )


_AxsLogoutStatus_Type.__name__ = "Integer32"
_AxsLogoutStatus_Object = MibScalar
axsLogoutStatus = _AxsLogoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 7),
    _AxsLogoutStatus_Type()
)
axsLogoutStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLogoutStatus.setStatus("mandatory")
_Axslldp_ObjectIdentity = ObjectIdentity
axslldp = _Axslldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100)
)
_AxslldpConfiguration_ObjectIdentity = ObjectIdentity
axslldpConfiguration = _AxslldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1)
)
_AxslldpMessageTxInterval_Type = Integer32
_AxslldpMessageTxInterval_Object = MibScalar
axslldpMessageTxInterval = _AxslldpMessageTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 1),
    _AxslldpMessageTxInterval_Type()
)
axslldpMessageTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpMessageTxInterval.setStatus("mandatory")
_AxslldpMessageTxHoldMultiplier_Type = Integer32
_AxslldpMessageTxHoldMultiplier_Object = MibScalar
axslldpMessageTxHoldMultiplier = _AxslldpMessageTxHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 2),
    _AxslldpMessageTxHoldMultiplier_Type()
)
axslldpMessageTxHoldMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpMessageTxHoldMultiplier.setStatus("mandatory")
_AxslldpPortConfigTable_Object = MibTable
axslldpPortConfigTable = _AxslldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6)
)
if mibBuilder.loadTexts:
    axslldpPortConfigTable.setStatus("mandatory")
_AxslldpPortConfigEntry_Object = MibTableRow
axslldpPortConfigEntry = _AxslldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6, 1)
)
axslldpPortConfigEntry.setIndexNames(
    (0, "AX4630S", "axslldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    axslldpPortConfigEntry.setStatus("mandatory")
_AxslldpPortConfigPortNum_Type = Integer32
_AxslldpPortConfigPortNum_Object = MibTableColumn
axslldpPortConfigPortNum = _AxslldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6, 1, 2),
    _AxslldpPortConfigPortNum_Type()
)
axslldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpPortConfigPortNum.setStatus("mandatory")


class _AxslldpPortConfigAdminStatus_Type(Integer32):
    """Custom type axslldpPortConfigAdminStatus based on Integer32"""
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
        *(("txOnly", 1),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("disabled", 4))
    )


_AxslldpPortConfigAdminStatus_Type.__name__ = "Integer32"
_AxslldpPortConfigAdminStatus_Object = MibTableColumn
axslldpPortConfigAdminStatus = _AxslldpPortConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6, 1, 3),
    _AxslldpPortConfigAdminStatus_Type()
)
axslldpPortConfigAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpPortConfigAdminStatus.setStatus("mandatory")


class _AxslldpPortConfigTLVsTxEnable_Type(Bits):
    """Custom type axslldpPortConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("portDesc", 4),
          ("sysName", 5),
          ("sysDesc", 6),
          ("sysCap", 7))
    )

_AxslldpPortConfigTLVsTxEnable_Type.__name__ = "Bits"
_AxslldpPortConfigTLVsTxEnable_Object = MibTableColumn
axslldpPortConfigTLVsTxEnable = _AxslldpPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6, 1, 4),
    _AxslldpPortConfigTLVsTxEnable_Type()
)
axslldpPortConfigTLVsTxEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpPortConfigTLVsTxEnable.setStatus("mandatory")
_AxslldpPortConfigRowStatus_Type = RowStatus
_AxslldpPortConfigRowStatus_Object = MibTableColumn
axslldpPortConfigRowStatus = _AxslldpPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6, 1, 5),
    _AxslldpPortConfigRowStatus_Type()
)
axslldpPortConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpPortConfigRowStatus.setStatus("mandatory")
_AxslldpStats_ObjectIdentity = ObjectIdentity
axslldpStats = _AxslldpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2)
)
_AxslldpStatsTable_Object = MibTable
axslldpStatsTable = _AxslldpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    axslldpStatsTable.setStatus("mandatory")
_AxslldpStatsEntry_Object = MibTableRow
axslldpStatsEntry = _AxslldpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1)
)
axslldpStatsEntry.setIndexNames(
    (0, "AX4630S", "axslldpStatsPortNum"),
)
if mibBuilder.loadTexts:
    axslldpStatsEntry.setStatus("mandatory")
_AxslldpStatsPortNum_Type = Integer32
_AxslldpStatsPortNum_Object = MibTableColumn
axslldpStatsPortNum = _AxslldpStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 2),
    _AxslldpStatsPortNum_Type()
)
axslldpStatsPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpStatsPortNum.setStatus("mandatory")
_AxslldpStatsOperStatus_Type = Integer32
_AxslldpStatsOperStatus_Object = MibTableColumn
axslldpStatsOperStatus = _AxslldpStatsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 3),
    _AxslldpStatsOperStatus_Type()
)
axslldpStatsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsOperStatus.setStatus("mandatory")
_AxslldpStatsFramesInErrors_Type = Counter32
_AxslldpStatsFramesInErrors_Object = MibTableColumn
axslldpStatsFramesInErrors = _AxslldpStatsFramesInErrors_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 4),
    _AxslldpStatsFramesInErrors_Type()
)
axslldpStatsFramesInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsFramesInErrors.setStatus("mandatory")
_AxslldpStatsFramesInTotal_Type = Counter32
_AxslldpStatsFramesInTotal_Object = MibTableColumn
axslldpStatsFramesInTotal = _AxslldpStatsFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 5),
    _AxslldpStatsFramesInTotal_Type()
)
axslldpStatsFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsFramesInTotal.setStatus("mandatory")
_AxslldpStatsFramesOutTotal_Type = Counter32
_AxslldpStatsFramesOutTotal_Object = MibTableColumn
axslldpStatsFramesOutTotal = _AxslldpStatsFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 6),
    _AxslldpStatsFramesOutTotal_Type()
)
axslldpStatsFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsFramesOutTotal.setStatus("mandatory")
_AxslldpStatsTLVsInErrors_Type = Counter32
_AxslldpStatsTLVsInErrors_Object = MibTableColumn
axslldpStatsTLVsInErrors = _AxslldpStatsTLVsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 7),
    _AxslldpStatsTLVsInErrors_Type()
)
axslldpStatsTLVsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsTLVsInErrors.setStatus("mandatory")
_AxslldpStatsTLVsDiscardedTotal_Type = Counter32
_AxslldpStatsTLVsDiscardedTotal_Object = MibTableColumn
axslldpStatsTLVsDiscardedTotal = _AxslldpStatsTLVsDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 8),
    _AxslldpStatsTLVsDiscardedTotal_Type()
)
axslldpStatsTLVsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsTLVsDiscardedTotal.setStatus("mandatory")
_AxslldpLocalSystemData_ObjectIdentity = ObjectIdentity
axslldpLocalSystemData = _AxslldpLocalSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3)
)


class _AxslldpLocChassisType_Type(Integer32):
    """Custom type axslldpLocChassisType based on Integer32"""
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
        *(("entPhysicalAlias", 1),
          ("ifAlias", 2),
          ("portEntPhysicalAlias", 3),
          ("backplaneEntPhysicalAlias", 4),
          ("macAddress", 5),
          ("networkAddress", 6))
    )


_AxslldpLocChassisType_Type.__name__ = "Integer32"
_AxslldpLocChassisType_Object = MibScalar
axslldpLocChassisType = _AxslldpLocChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 1),
    _AxslldpLocChassisType_Type()
)
axslldpLocChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocChassisType.setStatus("mandatory")
_AxslldpLocChassisId_Type = OctetString
_AxslldpLocChassisId_Object = MibScalar
axslldpLocChassisId = _AxslldpLocChassisId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 2),
    _AxslldpLocChassisId_Type()
)
axslldpLocChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocChassisId.setStatus("mandatory")
_AxslldpLocSysName_Type = OctetString
_AxslldpLocSysName_Object = MibScalar
axslldpLocSysName = _AxslldpLocSysName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 3),
    _AxslldpLocSysName_Type()
)
axslldpLocSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocSysName.setStatus("mandatory")
_AxslldpLocSysDesc_Type = DisplayString
_AxslldpLocSysDesc_Object = MibScalar
axslldpLocSysDesc = _AxslldpLocSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 4),
    _AxslldpLocSysDesc_Type()
)
axslldpLocSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocSysDesc.setStatus("mandatory")
_AxslldpLocPortTable_Object = MibTable
axslldpLocPortTable = _AxslldpLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7)
)
if mibBuilder.loadTexts:
    axslldpLocPortTable.setStatus("mandatory")
_AxslldpLocPortEntry_Object = MibTableRow
axslldpLocPortEntry = _AxslldpLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7, 1)
)
axslldpLocPortEntry.setIndexNames(
    (0, "AX4630S", "axslldpLocPortNum"),
)
if mibBuilder.loadTexts:
    axslldpLocPortEntry.setStatus("mandatory")
_AxslldpLocPortNum_Type = Integer32
_AxslldpLocPortNum_Object = MibTableColumn
axslldpLocPortNum = _AxslldpLocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7, 1, 1),
    _AxslldpLocPortNum_Type()
)
axslldpLocPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpLocPortNum.setStatus("mandatory")


class _AxslldpLocPortType_Type(Integer32):
    """Custom type axslldpLocPortType based on Integer32"""
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
        *(("ifAlias", 1),
          ("portEntPhysicalAlias", 2),
          ("backplaneEntPhysicalAlias", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("local", 6))
    )


_AxslldpLocPortType_Type.__name__ = "Integer32"
_AxslldpLocPortType_Object = MibTableColumn
axslldpLocPortType = _AxslldpLocPortType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7, 1, 2),
    _AxslldpLocPortType_Type()
)
axslldpLocPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocPortType.setStatus("mandatory")
_AxslldpLocPortId_Type = OctetString
_AxslldpLocPortId_Object = MibTableColumn
axslldpLocPortId = _AxslldpLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7, 1, 3),
    _AxslldpLocPortId_Type()
)
axslldpLocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocPortId.setStatus("mandatory")
_AxslldpLocPortDesc_Type = OctetString
_AxslldpLocPortDesc_Object = MibTableColumn
axslldpLocPortDesc = _AxslldpLocPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7, 1, 4),
    _AxslldpLocPortDesc_Type()
)
axslldpLocPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocPortDesc.setStatus("mandatory")
_AxslldpRemoteSystemData_ObjectIdentity = ObjectIdentity
axslldpRemoteSystemData = _AxslldpRemoteSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4)
)
_AxslldpRemTable_Object = MibTable
axslldpRemTable = _AxslldpRemTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1)
)
if mibBuilder.loadTexts:
    axslldpRemTable.setStatus("mandatory")
_AxslldpRemEntry_Object = MibTableRow
axslldpRemEntry = _AxslldpRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1)
)
axslldpRemEntry.setIndexNames(
    (0, "AX4630S", "axslldpRemLocalPortNum"),
    (0, "AX4630S", "axslldpRemIndex"),
)
if mibBuilder.loadTexts:
    axslldpRemEntry.setStatus("mandatory")
_AxslldpRemLocalPortNum_Type = Integer32
_AxslldpRemLocalPortNum_Object = MibTableColumn
axslldpRemLocalPortNum = _AxslldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 2),
    _AxslldpRemLocalPortNum_Type()
)
axslldpRemLocalPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpRemLocalPortNum.setStatus("mandatory")
_AxslldpRemIndex_Type = Integer32
_AxslldpRemIndex_Object = MibTableColumn
axslldpRemIndex = _AxslldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 3),
    _AxslldpRemIndex_Type()
)
axslldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpRemIndex.setStatus("mandatory")


class _AxslldpRemRemoteChassisType_Type(Integer32):
    """Custom type axslldpRemRemoteChassisType based on Integer32"""
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
        *(("entPhysicalAlias", 1),
          ("ifAlias", 2),
          ("portEntPhysicalAlias", 3),
          ("backplaneEntPhysicalAlias", 4),
          ("macAddress", 5),
          ("networkAddress", 6))
    )


_AxslldpRemRemoteChassisType_Type.__name__ = "Integer32"
_AxslldpRemRemoteChassisType_Object = MibTableColumn
axslldpRemRemoteChassisType = _AxslldpRemRemoteChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 4),
    _AxslldpRemRemoteChassisType_Type()
)
axslldpRemRemoteChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemRemoteChassisType.setStatus("mandatory")
_AxslldpRemRemoteChassis_Type = OctetString
_AxslldpRemRemoteChassis_Object = MibTableColumn
axslldpRemRemoteChassis = _AxslldpRemRemoteChassis_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 5),
    _AxslldpRemRemoteChassis_Type()
)
axslldpRemRemoteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemRemoteChassis.setStatus("mandatory")


class _AxslldpRemRemotePortType_Type(Integer32):
    """Custom type axslldpRemRemotePortType based on Integer32"""
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
        *(("ifAlias", 1),
          ("portEntPhysicalAlias", 2),
          ("backplaneEntPhysicalAlias", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("local", 6))
    )


_AxslldpRemRemotePortType_Type.__name__ = "Integer32"
_AxslldpRemRemotePortType_Object = MibTableColumn
axslldpRemRemotePortType = _AxslldpRemRemotePortType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 6),
    _AxslldpRemRemotePortType_Type()
)
axslldpRemRemotePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemRemotePortType.setStatus("mandatory")
_AxslldpRemRemotePort_Type = OctetString
_AxslldpRemRemotePort_Object = MibTableColumn
axslldpRemRemotePort = _AxslldpRemRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 7),
    _AxslldpRemRemotePort_Type()
)
axslldpRemRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemRemotePort.setStatus("mandatory")
_AxslldpRemPortDesc_Type = OctetString
_AxslldpRemPortDesc_Object = MibTableColumn
axslldpRemPortDesc = _AxslldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 8),
    _AxslldpRemPortDesc_Type()
)
axslldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemPortDesc.setStatus("mandatory")
_AxslldpRemSysName_Type = OctetString
_AxslldpRemSysName_Object = MibTableColumn
axslldpRemSysName = _AxslldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 9),
    _AxslldpRemSysName_Type()
)
axslldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemSysName.setStatus("mandatory")
_AxslldpRemSysDesc_Type = OctetString
_AxslldpRemSysDesc_Object = MibTableColumn
axslldpRemSysDesc = _AxslldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 10),
    _AxslldpRemSysDesc_Type()
)
axslldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemSysDesc.setStatus("mandatory")
_AxslldpRemoteOriginInfoData_ObjectIdentity = ObjectIdentity
axslldpRemoteOriginInfoData = _AxslldpRemoteOriginInfoData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20)
)
_AxslldpRemOriginInfoTable_Object = MibTable
axslldpRemOriginInfoTable = _AxslldpRemOriginInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1)
)
if mibBuilder.loadTexts:
    axslldpRemOriginInfoTable.setStatus("mandatory")
_AxslldpRemOriginInfoEntry_Object = MibTableRow
axslldpRemOriginInfoEntry = _AxslldpRemOriginInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1)
)
axslldpRemOriginInfoEntry.setIndexNames(
    (0, "AX4630S", "axslldpRemOriginInfoPortNum"),
    (0, "AX4630S", "axslldpRemOriginInfoIndex"),
)
if mibBuilder.loadTexts:
    axslldpRemOriginInfoEntry.setStatus("mandatory")
_AxslldpRemOriginInfoPortNum_Type = Integer32
_AxslldpRemOriginInfoPortNum_Object = MibTableColumn
axslldpRemOriginInfoPortNum = _AxslldpRemOriginInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 1),
    _AxslldpRemOriginInfoPortNum_Type()
)
axslldpRemOriginInfoPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoPortNum.setStatus("mandatory")
_AxslldpRemOriginInfoIndex_Type = Integer32
_AxslldpRemOriginInfoIndex_Object = MibTableColumn
axslldpRemOriginInfoIndex = _AxslldpRemOriginInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 2),
    _AxslldpRemOriginInfoIndex_Type()
)
axslldpRemOriginInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIndex.setStatus("mandatory")
_AxslldpRemOriginInfoLowerVlanList_Type = OctetString
_AxslldpRemOriginInfoLowerVlanList_Object = MibTableColumn
axslldpRemOriginInfoLowerVlanList = _AxslldpRemOriginInfoLowerVlanList_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 3),
    _AxslldpRemOriginInfoLowerVlanList_Type()
)
axslldpRemOriginInfoLowerVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoLowerVlanList.setStatus("mandatory")
_AxslldpRemOriginInfoHigherVlanList_Type = OctetString
_AxslldpRemOriginInfoHigherVlanList_Object = MibTableColumn
axslldpRemOriginInfoHigherVlanList = _AxslldpRemOriginInfoHigherVlanList_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 4),
    _AxslldpRemOriginInfoHigherVlanList_Type()
)
axslldpRemOriginInfoHigherVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoHigherVlanList.setStatus("mandatory")
_AxslldpRemOriginInfoIPv4Address_Type = OctetString
_AxslldpRemOriginInfoIPv4Address_Object = MibTableColumn
axslldpRemOriginInfoIPv4Address = _AxslldpRemOriginInfoIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 5),
    _AxslldpRemOriginInfoIPv4Address_Type()
)
axslldpRemOriginInfoIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv4Address.setStatus("mandatory")
_AxslldpRemOriginInfoIPv4PortType_Type = Integer32
_AxslldpRemOriginInfoIPv4PortType_Object = MibTableColumn
axslldpRemOriginInfoIPv4PortType = _AxslldpRemOriginInfoIPv4PortType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 6),
    _AxslldpRemOriginInfoIPv4PortType_Type()
)
axslldpRemOriginInfoIPv4PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv4PortType.setStatus("mandatory")
_AxslldpRemOriginInfoIPv4VlanId_Type = Integer32
_AxslldpRemOriginInfoIPv4VlanId_Object = MibTableColumn
axslldpRemOriginInfoIPv4VlanId = _AxslldpRemOriginInfoIPv4VlanId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 7),
    _AxslldpRemOriginInfoIPv4VlanId_Type()
)
axslldpRemOriginInfoIPv4VlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv4VlanId.setStatus("mandatory")
_AxslldpRemOriginInfoIPv6Address_Type = OctetString
_AxslldpRemOriginInfoIPv6Address_Object = MibTableColumn
axslldpRemOriginInfoIPv6Address = _AxslldpRemOriginInfoIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 8),
    _AxslldpRemOriginInfoIPv6Address_Type()
)
axslldpRemOriginInfoIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv6Address.setStatus("mandatory")
_AxslldpRemOriginInfoIPv6PortType_Type = Integer32
_AxslldpRemOriginInfoIPv6PortType_Object = MibTableColumn
axslldpRemOriginInfoIPv6PortType = _AxslldpRemOriginInfoIPv6PortType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 9),
    _AxslldpRemOriginInfoIPv6PortType_Type()
)
axslldpRemOriginInfoIPv6PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv6PortType.setStatus("mandatory")
_AxslldpRemOriginInfoIPv6VlanId_Type = Integer32
_AxslldpRemOriginInfoIPv6VlanId_Object = MibTableColumn
axslldpRemOriginInfoIPv6VlanId = _AxslldpRemOriginInfoIPv6VlanId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 10),
    _AxslldpRemOriginInfoIPv6VlanId_Type()
)
axslldpRemOriginInfoIPv6VlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv6VlanId.setStatus("mandatory")
_AxsAxrp_ObjectIdentity = ObjectIdentity
axsAxrp = _AxsAxrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200)
)
_AxsAxrpGroupTable_Object = MibTable
axsAxrpGroupTable = _AxsAxrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1)
)
if mibBuilder.loadTexts:
    axsAxrpGroupTable.setStatus("mandatory")
_AxsAxrpGroupEntry_Object = MibTableRow
axsAxrpGroupEntry = _AxsAxrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1)
)
axsAxrpGroupEntry.setIndexNames(
    (0, "AX4630S", "axsAxrpGroupRingId"),
)
if mibBuilder.loadTexts:
    axsAxrpGroupEntry.setStatus("mandatory")
_AxsAxrpGroupRingId_Type = Integer32
_AxsAxrpGroupRingId_Object = MibTableColumn
axsAxrpGroupRingId = _AxsAxrpGroupRingId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 1),
    _AxsAxrpGroupRingId_Type()
)
axsAxrpGroupRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAxrpGroupRingId.setStatus("mandatory")
_AxsAxrpGroupRowStatus_Type = RowStatus
_AxsAxrpGroupRowStatus_Object = MibTableColumn
axsAxrpGroupRowStatus = _AxsAxrpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 2),
    _AxsAxrpGroupRowStatus_Type()
)
axsAxrpGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRowStatus.setStatus("mandatory")


class _AxsAxrpGroupMode_Type(Integer32):
    """Custom type axsAxrpGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-config", 1),
          ("master", 2),
          ("transit", 3))
    )


_AxsAxrpGroupMode_Type.__name__ = "Integer32"
_AxsAxrpGroupMode_Object = MibTableColumn
axsAxrpGroupMode = _AxsAxrpGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 3),
    _AxsAxrpGroupMode_Type()
)
axsAxrpGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupMode.setStatus("mandatory")


class _AxsAxrpGroupRingAttribute_Type(Integer32):
    """Custom type axsAxrpGroupRingAttribute based on Integer32"""
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
        *(("no-config", 1),
          ("rift-ring", 2),
          ("rift-ring-edge1", 3),
          ("rift-ring-edge2", 4))
    )


_AxsAxrpGroupRingAttribute_Type.__name__ = "Integer32"
_AxsAxrpGroupRingAttribute_Object = MibTableColumn
axsAxrpGroupRingAttribute = _AxsAxrpGroupRingAttribute_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 4),
    _AxsAxrpGroupRingAttribute_Type()
)
axsAxrpGroupRingAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingAttribute.setStatus("mandatory")


class _AxsAxrpGroupMonitoringState_Type(Integer32):
    """Custom type axsAxrpGroupMonitoringState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("disable", 2),
          ("fault-monitoring", 3),
          ("recovery-monitoring", 4),
          ("flush-monitoring", 5),
          ("not-operating", 6),
          ("suppress-fault-recovery", 7),
          ("preempt-delay", 8),
          ("recovery-re-monitoring", 9))
    )


_AxsAxrpGroupMonitoringState_Type.__name__ = "Integer32"
_AxsAxrpGroupMonitoringState_Object = MibTableColumn
axsAxrpGroupMonitoringState = _AxsAxrpGroupMonitoringState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 5),
    _AxsAxrpGroupMonitoringState_Type()
)
axsAxrpGroupMonitoringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupMonitoringState.setStatus("mandatory")
_AxsAxrpGroupRingport1_Type = Integer32
_AxsAxrpGroupRingport1_Object = MibTableColumn
axsAxrpGroupRingport1 = _AxsAxrpGroupRingport1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 6),
    _AxsAxrpGroupRingport1_Type()
)
axsAxrpGroupRingport1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport1.setStatus("mandatory")


class _AxsAxrpGroupRingport1Shared_Type(Integer32):
    """Custom type axsAxrpGroupRingport1Shared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-config", 1),
          ("shared-edge", 2),
          ("shared", 3))
    )


_AxsAxrpGroupRingport1Shared_Type.__name__ = "Integer32"
_AxsAxrpGroupRingport1Shared_Object = MibTableColumn
axsAxrpGroupRingport1Shared = _AxsAxrpGroupRingport1Shared_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 7),
    _AxsAxrpGroupRingport1Shared_Type()
)
axsAxrpGroupRingport1Shared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport1Shared.setStatus("mandatory")
_AxsAxrpGroupRingport2_Type = Integer32
_AxsAxrpGroupRingport2_Object = MibTableColumn
axsAxrpGroupRingport2 = _AxsAxrpGroupRingport2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 8),
    _AxsAxrpGroupRingport2_Type()
)
axsAxrpGroupRingport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport2.setStatus("mandatory")


class _AxsAxrpGroupRingport2Shared_Type(Integer32):
    """Custom type axsAxrpGroupRingport2Shared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-config", 1),
          ("shared-edge", 2),
          ("shared", 3))
    )


_AxsAxrpGroupRingport2Shared_Type.__name__ = "Integer32"
_AxsAxrpGroupRingport2Shared_Object = MibTableColumn
axsAxrpGroupRingport2Shared = _AxsAxrpGroupRingport2Shared_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 9),
    _AxsAxrpGroupRingport2Shared_Type()
)
axsAxrpGroupRingport2Shared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport2Shared.setStatus("mandatory")
_AxsAxrpGroupTransitionToFaultCounts_Type = Counter32
_AxsAxrpGroupTransitionToFaultCounts_Object = MibTableColumn
axsAxrpGroupTransitionToFaultCounts = _AxsAxrpGroupTransitionToFaultCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 10),
    _AxsAxrpGroupTransitionToFaultCounts_Type()
)
axsAxrpGroupTransitionToFaultCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupTransitionToFaultCounts.setStatus("mandatory")
_AxsAxrpGroupTransitionToNormalCounts_Type = Counter32
_AxsAxrpGroupTransitionToNormalCounts_Object = MibTableColumn
axsAxrpGroupTransitionToNormalCounts = _AxsAxrpGroupTransitionToNormalCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 11),
    _AxsAxrpGroupTransitionToNormalCounts_Type()
)
axsAxrpGroupTransitionToNormalCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupTransitionToNormalCounts.setStatus("mandatory")
_AxsAxrpGroupLastTransitionTime_Type = TimeStamp
_AxsAxrpGroupLastTransitionTime_Object = MibTableColumn
axsAxrpGroupLastTransitionTime = _AxsAxrpGroupLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 12),
    _AxsAxrpGroupLastTransitionTime_Type()
)
axsAxrpGroupLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupLastTransitionTime.setStatus("mandatory")


class _AxsAxrpGroupLinkStatusAlert_Type(Integer32):
    """Custom type axsAxrpGroupLinkStatusAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-config", 1),
          ("enable", 2))
    )


_AxsAxrpGroupLinkStatusAlert_Type.__name__ = "Integer32"
_AxsAxrpGroupLinkStatusAlert_Object = MibTableColumn
axsAxrpGroupLinkStatusAlert = _AxsAxrpGroupLinkStatusAlert_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 13),
    _AxsAxrpGroupLinkStatusAlert_Type()
)
axsAxrpGroupLinkStatusAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupLinkStatusAlert.setStatus("mandatory")


class _AxsAxrpGroupRingport1LinkKeepaliveSend_Type(Integer32):
    """Custom type axsAxrpGroupRingport1LinkKeepaliveSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-config", 1),
          ("enable", 2))
    )


_AxsAxrpGroupRingport1LinkKeepaliveSend_Type.__name__ = "Integer32"
_AxsAxrpGroupRingport1LinkKeepaliveSend_Object = MibTableColumn
axsAxrpGroupRingport1LinkKeepaliveSend = _AxsAxrpGroupRingport1LinkKeepaliveSend_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 14),
    _AxsAxrpGroupRingport1LinkKeepaliveSend_Type()
)
axsAxrpGroupRingport1LinkKeepaliveSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport1LinkKeepaliveSend.setStatus("mandatory")


class _AxsAxrpGroupRingport1LinkKeepaliveMonitor_Type(Integer32):
    """Custom type axsAxrpGroupRingport1LinkKeepaliveMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-config", 1),
          ("enable", 2))
    )


_AxsAxrpGroupRingport1LinkKeepaliveMonitor_Type.__name__ = "Integer32"
_AxsAxrpGroupRingport1LinkKeepaliveMonitor_Object = MibTableColumn
axsAxrpGroupRingport1LinkKeepaliveMonitor = _AxsAxrpGroupRingport1LinkKeepaliveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 15),
    _AxsAxrpGroupRingport1LinkKeepaliveMonitor_Type()
)
axsAxrpGroupRingport1LinkKeepaliveMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport1LinkKeepaliveMonitor.setStatus("mandatory")


class _AxsAxrpGroupRingport1LinkState_Type(Integer32):
    """Custom type axsAxrpGroupRingport1LinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-monitoring", 1),
          ("normal", 2),
          ("fault", 3))
    )


_AxsAxrpGroupRingport1LinkState_Type.__name__ = "Integer32"
_AxsAxrpGroupRingport1LinkState_Object = MibTableColumn
axsAxrpGroupRingport1LinkState = _AxsAxrpGroupRingport1LinkState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 16),
    _AxsAxrpGroupRingport1LinkState_Type()
)
axsAxrpGroupRingport1LinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport1LinkState.setStatus("mandatory")
_AxsAxrpGroupRingport1LinkKeepaliveReceiveCounts_Type = Counter32
_AxsAxrpGroupRingport1LinkKeepaliveReceiveCounts_Object = MibTableColumn
axsAxrpGroupRingport1LinkKeepaliveReceiveCounts = _AxsAxrpGroupRingport1LinkKeepaliveReceiveCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 17),
    _AxsAxrpGroupRingport1LinkKeepaliveReceiveCounts_Type()
)
axsAxrpGroupRingport1LinkKeepaliveReceiveCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport1LinkKeepaliveReceiveCounts.setStatus("mandatory")


class _AxsAxrpGroupRingport2LinkKeepaliveSend_Type(Integer32):
    """Custom type axsAxrpGroupRingport2LinkKeepaliveSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-config", 1),
          ("enable", 2))
    )


_AxsAxrpGroupRingport2LinkKeepaliveSend_Type.__name__ = "Integer32"
_AxsAxrpGroupRingport2LinkKeepaliveSend_Object = MibTableColumn
axsAxrpGroupRingport2LinkKeepaliveSend = _AxsAxrpGroupRingport2LinkKeepaliveSend_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 18),
    _AxsAxrpGroupRingport2LinkKeepaliveSend_Type()
)
axsAxrpGroupRingport2LinkKeepaliveSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport2LinkKeepaliveSend.setStatus("mandatory")


class _AxsAxrpGroupRingport2LinkKeepaliveMonitor_Type(Integer32):
    """Custom type axsAxrpGroupRingport2LinkKeepaliveMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-config", 1),
          ("enable", 2))
    )


_AxsAxrpGroupRingport2LinkKeepaliveMonitor_Type.__name__ = "Integer32"
_AxsAxrpGroupRingport2LinkKeepaliveMonitor_Object = MibTableColumn
axsAxrpGroupRingport2LinkKeepaliveMonitor = _AxsAxrpGroupRingport2LinkKeepaliveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 19),
    _AxsAxrpGroupRingport2LinkKeepaliveMonitor_Type()
)
axsAxrpGroupRingport2LinkKeepaliveMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport2LinkKeepaliveMonitor.setStatus("mandatory")


class _AxsAxrpGroupRingport2LinkState_Type(Integer32):
    """Custom type axsAxrpGroupRingport2LinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-monitoring", 1),
          ("normal", 2),
          ("fault", 3))
    )


_AxsAxrpGroupRingport2LinkState_Type.__name__ = "Integer32"
_AxsAxrpGroupRingport2LinkState_Object = MibTableColumn
axsAxrpGroupRingport2LinkState = _AxsAxrpGroupRingport2LinkState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 20),
    _AxsAxrpGroupRingport2LinkState_Type()
)
axsAxrpGroupRingport2LinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport2LinkState.setStatus("mandatory")
_AxsAxrpGroupRingport2LinkKeepaliveReceiveCounts_Type = Counter32
_AxsAxrpGroupRingport2LinkKeepaliveReceiveCounts_Object = MibTableColumn
axsAxrpGroupRingport2LinkKeepaliveReceiveCounts = _AxsAxrpGroupRingport2LinkKeepaliveReceiveCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 21),
    _AxsAxrpGroupRingport2LinkKeepaliveReceiveCounts_Type()
)
axsAxrpGroupRingport2LinkKeepaliveReceiveCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupRingport2LinkKeepaliveReceiveCounts.setStatus("mandatory")


class _AxsAxrpGroupMultiFaultDetectionState_Type(Integer32):
    """Custom type axsAxrpGroupMultiFaultDetectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-monitoring", 1),
          ("normal", 2),
          ("fault", 3))
    )


_AxsAxrpGroupMultiFaultDetectionState_Type.__name__ = "Integer32"
_AxsAxrpGroupMultiFaultDetectionState_Object = MibTableColumn
axsAxrpGroupMultiFaultDetectionState = _AxsAxrpGroupMultiFaultDetectionState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 1, 1, 22),
    _AxsAxrpGroupMultiFaultDetectionState_Type()
)
axsAxrpGroupMultiFaultDetectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpGroupMultiFaultDetectionState.setStatus("mandatory")
_AxsAxrpVlanGroupTable_Object = MibTable
axsAxrpVlanGroupTable = _AxsAxrpVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2)
)
if mibBuilder.loadTexts:
    axsAxrpVlanGroupTable.setStatus("mandatory")
_AxsAxrpVlanGroupEntry_Object = MibTableRow
axsAxrpVlanGroupEntry = _AxsAxrpVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2, 1)
)
axsAxrpVlanGroupEntry.setIndexNames(
    (0, "AX4630S", "axsAxrpVlanGroupRingId"),
    (0, "AX4630S", "axsAxrpVlanGroupId"),
)
if mibBuilder.loadTexts:
    axsAxrpVlanGroupEntry.setStatus("mandatory")
_AxsAxrpVlanGroupRingId_Type = Integer32
_AxsAxrpVlanGroupRingId_Object = MibTableColumn
axsAxrpVlanGroupRingId = _AxsAxrpVlanGroupRingId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2, 1, 1),
    _AxsAxrpVlanGroupRingId_Type()
)
axsAxrpVlanGroupRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAxrpVlanGroupRingId.setStatus("mandatory")
_AxsAxrpVlanGroupId_Type = Integer32
_AxsAxrpVlanGroupId_Object = MibTableColumn
axsAxrpVlanGroupId = _AxsAxrpVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2, 1, 2),
    _AxsAxrpVlanGroupId_Type()
)
axsAxrpVlanGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAxrpVlanGroupId.setStatus("mandatory")
_AxsAxrpVlanGroupRingport1_Type = Integer32
_AxsAxrpVlanGroupRingport1_Object = MibTableColumn
axsAxrpVlanGroupRingport1 = _AxsAxrpVlanGroupRingport1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2, 1, 3),
    _AxsAxrpVlanGroupRingport1_Type()
)
axsAxrpVlanGroupRingport1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpVlanGroupRingport1.setStatus("mandatory")


class _AxsAxrpVlanGroupRingport1Role_Type(Integer32):
    """Custom type axsAxrpVlanGroupRingport1Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("other", 3))
    )


_AxsAxrpVlanGroupRingport1Role_Type.__name__ = "Integer32"
_AxsAxrpVlanGroupRingport1Role_Object = MibTableColumn
axsAxrpVlanGroupRingport1Role = _AxsAxrpVlanGroupRingport1Role_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2, 1, 4),
    _AxsAxrpVlanGroupRingport1Role_Type()
)
axsAxrpVlanGroupRingport1Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpVlanGroupRingport1Role.setStatus("mandatory")


class _AxsAxrpVlanGroupRingport1OperState_Type(Integer32):
    """Custom type axsAxrpVlanGroupRingport1OperState based on Integer32"""
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
        *(("forwarding", 1),
          ("blocking", 2),
          ("other", 3),
          ("down", 4))
    )


_AxsAxrpVlanGroupRingport1OperState_Type.__name__ = "Integer32"
_AxsAxrpVlanGroupRingport1OperState_Object = MibTableColumn
axsAxrpVlanGroupRingport1OperState = _AxsAxrpVlanGroupRingport1OperState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2, 1, 5),
    _AxsAxrpVlanGroupRingport1OperState_Type()
)
axsAxrpVlanGroupRingport1OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpVlanGroupRingport1OperState.setStatus("mandatory")
_AxsAxrpVlanGroupRingport2_Type = Integer32
_AxsAxrpVlanGroupRingport2_Object = MibTableColumn
axsAxrpVlanGroupRingport2 = _AxsAxrpVlanGroupRingport2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2, 1, 6),
    _AxsAxrpVlanGroupRingport2_Type()
)
axsAxrpVlanGroupRingport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpVlanGroupRingport2.setStatus("mandatory")


class _AxsAxrpVlanGroupRingport2Role_Type(Integer32):
    """Custom type axsAxrpVlanGroupRingport2Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("other", 3))
    )


_AxsAxrpVlanGroupRingport2Role_Type.__name__ = "Integer32"
_AxsAxrpVlanGroupRingport2Role_Object = MibTableColumn
axsAxrpVlanGroupRingport2Role = _AxsAxrpVlanGroupRingport2Role_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2, 1, 7),
    _AxsAxrpVlanGroupRingport2Role_Type()
)
axsAxrpVlanGroupRingport2Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpVlanGroupRingport2Role.setStatus("mandatory")


class _AxsAxrpVlanGroupRingport2OperState_Type(Integer32):
    """Custom type axsAxrpVlanGroupRingport2OperState based on Integer32"""
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
        *(("forwarding", 1),
          ("blocking", 2),
          ("other", 3),
          ("down", 4))
    )


_AxsAxrpVlanGroupRingport2OperState_Type.__name__ = "Integer32"
_AxsAxrpVlanGroupRingport2OperState_Object = MibTableColumn
axsAxrpVlanGroupRingport2OperState = _AxsAxrpVlanGroupRingport2OperState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 200, 2, 1, 8),
    _AxsAxrpVlanGroupRingport2OperState_Type()
)
axsAxrpVlanGroupRingport2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAxrpVlanGroupRingport2OperState.setStatus("mandatory")
_AxsPconMIB_ObjectIdentity = ObjectIdentity
axsPconMIB = _AxsPconMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300)
)
_AxsPconObjects_ObjectIdentity = ObjectIdentity
axsPconObjects = _AxsPconObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1)
)
_AxsPconModuleData_ObjectIdentity = ObjectIdentity
axsPconModuleData = _AxsPconModuleData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 1)
)
_AxsPconModuleTable_Object = MibTable
axsPconModuleTable = _AxsPconModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 1, 1)
)
if mibBuilder.loadTexts:
    axsPconModuleTable.setStatus("mandatory")
_AxsPconModuleEntry_Object = MibTableRow
axsPconModuleEntry = _AxsPconModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 1, 1, 1)
)
axsPconModuleEntry.setIndexNames(
    (0, "AX4630S", "axsPconModuleIndex"),
)
if mibBuilder.loadTexts:
    axsPconModuleEntry.setStatus("mandatory")


class _AxsPconModuleIndex_Type(Integer32):
    """Custom type axsPconModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxsPconModuleIndex_Type.__name__ = "Integer32"
_AxsPconModuleIndex_Object = MibTableColumn
axsPconModuleIndex = _AxsPconModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 1, 1, 1, 1),
    _AxsPconModuleIndex_Type()
)
axsPconModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsPconModuleIndex.setStatus("mandatory")


class _AxsPconModuleType_Type(Integer32):
    """Custom type axsPconModuleType based on Integer32"""
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
        *(("all", 1),
          ("chassis", 2),
          ("bcu", 3),
          ("csu", 4),
          ("msu", 5),
          ("bsu", 6),
          ("nif", 7))
    )


_AxsPconModuleType_Type.__name__ = "Integer32"
_AxsPconModuleType_Object = MibTableColumn
axsPconModuleType = _AxsPconModuleType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 1, 1, 1, 2),
    _AxsPconModuleType_Type()
)
axsPconModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconModuleType.setStatus("mandatory")
_AxsPconModuleSlotNo_Type = Integer32
_AxsPconModuleSlotNo_Object = MibTableColumn
axsPconModuleSlotNo = _AxsPconModuleSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 1, 1, 1, 3),
    _AxsPconModuleSlotNo_Type()
)
axsPconModuleSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconModuleSlotNo.setStatus("mandatory")
_AxsPconModuleDescr_Type = DisplayString
_AxsPconModuleDescr_Object = MibTableColumn
axsPconModuleDescr = _AxsPconModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 1, 1, 1, 4),
    _AxsPconModuleDescr_Type()
)
axsPconModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconModuleDescr.setStatus("mandatory")


class _AxsPconModuleStatus_Type(Integer32):
    """Custom type axsPconModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -1),
          ("disconnected", 0),
          ("active", 1),
          ("standby", 2),
          ("down", 3))
    )


_AxsPconModuleStatus_Type.__name__ = "Integer32"
_AxsPconModuleStatus_Object = MibTableColumn
axsPconModuleStatus = _AxsPconModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 1, 1, 1, 5),
    _AxsPconModuleStatus_Type()
)
axsPconModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconModuleStatus.setStatus("mandatory")


class _AxsPconModuleMode_Type(Integer32):
    """Custom type axsPconModuleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -1),
          ("other", 0),
          ("normal", 1),
          ("saving-mode1", 2),
          ("saving-mode2", 3),
          ("saving", 4),
          ("changing", 5))
    )


_AxsPconModuleMode_Type.__name__ = "Integer32"
_AxsPconModuleMode_Object = MibTableColumn
axsPconModuleMode = _AxsPconModuleMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 1, 1, 1, 6),
    _AxsPconModuleMode_Type()
)
axsPconModuleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconModuleMode.setStatus("mandatory")
_AxsPconPowerCon_ObjectIdentity = ObjectIdentity
axsPconPowerCon = _AxsPconPowerCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 2)
)
_AxsPconPowerConTable_Object = MibTable
axsPconPowerConTable = _AxsPconPowerConTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 2, 1)
)
if mibBuilder.loadTexts:
    axsPconPowerConTable.setStatus("mandatory")
_AxsPconPowerConEntry_Object = MibTableRow
axsPconPowerConEntry = _AxsPconPowerConEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 2, 1, 1)
)
axsPconPowerConEntry.setIndexNames(
    (0, "AX4630S", "axsPconModuleIndex"),
)
if mibBuilder.loadTexts:
    axsPconPowerConEntry.setStatus("mandatory")
_AxsPconPowerConMaxPower_Type = Gauge32
_AxsPconPowerConMaxPower_Object = MibTableColumn
axsPconPowerConMaxPower = _AxsPconPowerConMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 2, 1, 1, 1),
    _AxsPconPowerConMaxPower_Type()
)
axsPconPowerConMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconPowerConMaxPower.setStatus("mandatory")
_AxsPconPowerConPowerConsumption_Type = Counter64
_AxsPconPowerConPowerConsumption_Object = MibTableColumn
axsPconPowerConPowerConsumption = _AxsPconPowerConPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 2, 1, 1, 2),
    _AxsPconPowerConPowerConsumption_Type()
)
axsPconPowerConPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconPowerConPowerConsumption.setStatus("mandatory")
_AxsPconPowerConPowerMeter_Type = Gauge32
_AxsPconPowerConPowerMeter_Object = MibTableColumn
axsPconPowerConPowerMeter = _AxsPconPowerConPowerMeter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 2, 1, 1, 3),
    _AxsPconPowerConPowerMeter_Type()
)
axsPconPowerConPowerMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconPowerConPowerMeter.setStatus("mandatory")
_AxsPconTraffic_ObjectIdentity = ObjectIdentity
axsPconTraffic = _AxsPconTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3)
)
_AxsPconTrafficTable_Object = MibTable
axsPconTrafficTable = _AxsPconTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1)
)
if mibBuilder.loadTexts:
    axsPconTrafficTable.setStatus("mandatory")
_AxsPconTrafficEntry_Object = MibTableRow
axsPconTrafficEntry = _AxsPconTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1)
)
axsPconTrafficEntry.setIndexNames(
    (0, "AX4630S", "axsPconModuleIndex"),
)
if mibBuilder.loadTexts:
    axsPconTrafficEntry.setStatus("mandatory")
_AxsPconTrafficMaxTransferCapacity_Type = Gauge32
_AxsPconTrafficMaxTransferCapacity_Object = MibTableColumn
axsPconTrafficMaxTransferCapacity = _AxsPconTrafficMaxTransferCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 1),
    _AxsPconTrafficMaxTransferCapacity_Type()
)
axsPconTrafficMaxTransferCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficMaxTransferCapacity.setStatus("mandatory")
_AxsPconTrafficTotalTransferCapacity_Type = Gauge32
_AxsPconTrafficTotalTransferCapacity_Object = MibTableColumn
axsPconTrafficTotalTransferCapacity = _AxsPconTrafficTotalTransferCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 2),
    _AxsPconTrafficTotalTransferCapacity_Type()
)
axsPconTrafficTotalTransferCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficTotalTransferCapacity.setStatus("mandatory")
_AxsPconTrafficInOctets_Type = Counter64
_AxsPconTrafficInOctets_Object = MibTableColumn
axsPconTrafficInOctets = _AxsPconTrafficInOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 3),
    _AxsPconTrafficInOctets_Type()
)
axsPconTrafficInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficInOctets.setStatus("mandatory")
_AxsPconTrafficOutOctets_Type = Counter64
_AxsPconTrafficOutOctets_Object = MibTableColumn
axsPconTrafficOutOctets = _AxsPconTrafficOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 4),
    _AxsPconTrafficOutOctets_Type()
)
axsPconTrafficOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficOutOctets.setStatus("mandatory")
_AxsPconTrafficInPkts_Type = Counter64
_AxsPconTrafficInPkts_Object = MibTableColumn
axsPconTrafficInPkts = _AxsPconTrafficInPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 5),
    _AxsPconTrafficInPkts_Type()
)
axsPconTrafficInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficInPkts.setStatus("mandatory")
_AxsPconTrafficOutPkts_Type = Counter64
_AxsPconTrafficOutPkts_Object = MibTableColumn
axsPconTrafficOutPkts = _AxsPconTrafficOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 6),
    _AxsPconTrafficOutPkts_Type()
)
axsPconTrafficOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficOutPkts.setStatus("mandatory")
_AxsPconTrafficCapacityOctets_Type = Counter64
_AxsPconTrafficCapacityOctets_Object = MibTableColumn
axsPconTrafficCapacityOctets = _AxsPconTrafficCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 7),
    _AxsPconTrafficCapacityOctets_Type()
)
axsPconTrafficCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficCapacityOctets.setStatus("mandatory")
_AxsPconTrafficInPeakOctetsRate_Type = Gauge32
_AxsPconTrafficInPeakOctetsRate_Object = MibTableColumn
axsPconTrafficInPeakOctetsRate = _AxsPconTrafficInPeakOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 8),
    _AxsPconTrafficInPeakOctetsRate_Type()
)
axsPconTrafficInPeakOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficInPeakOctetsRate.setStatus("mandatory")
_AxsPconTrafficPeakTransferCapacity_Type = Gauge32
_AxsPconTrafficPeakTransferCapacity_Object = MibTableColumn
axsPconTrafficPeakTransferCapacity = _AxsPconTrafficPeakTransferCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 9),
    _AxsPconTrafficPeakTransferCapacity_Type()
)
axsPconTrafficPeakTransferCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficPeakTransferCapacity.setStatus("mandatory")
_AxsPconTrafficInDiscPkts_Type = Counter64
_AxsPconTrafficInDiscPkts_Object = MibTableColumn
axsPconTrafficInDiscPkts = _AxsPconTrafficInDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 300, 1, 3, 1, 1, 10),
    _AxsPconTrafficInDiscPkts_Type()
)
axsPconTrafficInDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsPconTrafficInDiscPkts.setStatus("mandatory")
_AxsVxlan_ObjectIdentity = ObjectIdentity
axsVxlan = _AxsVxlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410)
)
_AxsVxlanStatsVniTable_Object = MibTable
axsVxlanStatsVniTable = _AxsVxlanStatsVniTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1)
)
if mibBuilder.loadTexts:
    axsVxlanStatsVniTable.setStatus("mandatory")
_AxsVxlanStatsVniEntry_Object = MibTableRow
axsVxlanStatsVniEntry = _AxsVxlanStatsVniEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1, 1)
)
axsVxlanStatsVniEntry.setIndexNames(
    (0, "AX4630S", "axsChassisIndex"),
    (0, "AX4630S", "axsVniIndex"),
)
if mibBuilder.loadTexts:
    axsVxlanStatsVniEntry.setStatus("mandatory")
_AxsChassisIndex_Type = Integer32
_AxsChassisIndex_Object = MibTableColumn
axsChassisIndex = _AxsChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1, 1, 1),
    _AxsChassisIndex_Type()
)
axsChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsChassisIndex.setStatus("mandatory")
_AxsVniIndex_Type = VniIndex
_AxsVniIndex_Object = MibTableColumn
axsVniIndex = _AxsVniIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1, 1, 2),
    _AxsVniIndex_Type()
)
axsVniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVniIndex.setStatus("mandatory")
_AxsVxlanStatsVniEncapPackets_Type = Counter32
_AxsVxlanStatsVniEncapPackets_Object = MibTableColumn
axsVxlanStatsVniEncapPackets = _AxsVxlanStatsVniEncapPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1, 1, 3),
    _AxsVxlanStatsVniEncapPackets_Type()
)
axsVxlanStatsVniEncapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsVniEncapPackets.setStatus("mandatory")
_AxsVxlanStatsVniEncapOctets_Type = Counter64
_AxsVxlanStatsVniEncapOctets_Object = MibTableColumn
axsVxlanStatsVniEncapOctets = _AxsVxlanStatsVniEncapOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1, 1, 4),
    _AxsVxlanStatsVniEncapOctets_Type()
)
axsVxlanStatsVniEncapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsVniEncapOctets.setStatus("mandatory")
_AxsVxlanStatsVniDecapPackets_Type = Counter32
_AxsVxlanStatsVniDecapPackets_Object = MibTableColumn
axsVxlanStatsVniDecapPackets = _AxsVxlanStatsVniDecapPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1, 1, 5),
    _AxsVxlanStatsVniDecapPackets_Type()
)
axsVxlanStatsVniDecapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsVniDecapPackets.setStatus("mandatory")
_AxsVxlanStatsVniDecapOctets_Type = Counter64
_AxsVxlanStatsVniDecapOctets_Object = MibTableColumn
axsVxlanStatsVniDecapOctets = _AxsVxlanStatsVniDecapOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1, 1, 6),
    _AxsVxlanStatsVniDecapOctets_Type()
)
axsVxlanStatsVniDecapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsVniDecapOctets.setStatus("mandatory")
_AxsVxlanStatsVniAcsacsPackets_Type = Counter32
_AxsVxlanStatsVniAcsacsPackets_Object = MibTableColumn
axsVxlanStatsVniAcsacsPackets = _AxsVxlanStatsVniAcsacsPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1, 1, 7),
    _AxsVxlanStatsVniAcsacsPackets_Type()
)
axsVxlanStatsVniAcsacsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsVniAcsacsPackets.setStatus("mandatory")
_AxsVxlanStatsVniAcsacsOctets_Type = Counter64
_AxsVxlanStatsVniAcsacsOctets_Object = MibTableColumn
axsVxlanStatsVniAcsacsOctets = _AxsVxlanStatsVniAcsacsOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 1, 1, 8),
    _AxsVxlanStatsVniAcsacsOctets_Type()
)
axsVxlanStatsVniAcsacsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsVniAcsacsOctets.setStatus("mandatory")
_AxsVxlanStatsTunnelTable_Object = MibTable
axsVxlanStatsTunnelTable = _AxsVxlanStatsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 2)
)
if mibBuilder.loadTexts:
    axsVxlanStatsTunnelTable.setStatus("mandatory")
_AxsVxlanStatsTunnelEntry_Object = MibTableRow
axsVxlanStatsTunnelEntry = _AxsVxlanStatsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 2, 1)
)
axsVxlanStatsTunnelEntry.setIndexNames(
    (0, "AX4630S", "axsChassisIndex"),
    (0, "AX4630S", "axsTunnelAddress"),
)
if mibBuilder.loadTexts:
    axsVxlanStatsTunnelEntry.setStatus("mandatory")
_AxsTunnelAddress_Type = IpAddress
_AxsTunnelAddress_Object = MibTableColumn
axsTunnelAddress = _AxsTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 2, 1, 1),
    _AxsTunnelAddress_Type()
)
axsTunnelAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsTunnelAddress.setStatus("mandatory")
_AxsVxlanStatsTunnelEncapPackets_Type = Counter32
_AxsVxlanStatsTunnelEncapPackets_Object = MibTableColumn
axsVxlanStatsTunnelEncapPackets = _AxsVxlanStatsTunnelEncapPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 2, 1, 2),
    _AxsVxlanStatsTunnelEncapPackets_Type()
)
axsVxlanStatsTunnelEncapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsTunnelEncapPackets.setStatus("mandatory")
_AxsVxlanStatsTunnelEncapOctets_Type = Counter64
_AxsVxlanStatsTunnelEncapOctets_Object = MibTableColumn
axsVxlanStatsTunnelEncapOctets = _AxsVxlanStatsTunnelEncapOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 2, 1, 3),
    _AxsVxlanStatsTunnelEncapOctets_Type()
)
axsVxlanStatsTunnelEncapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsTunnelEncapOctets.setStatus("mandatory")
_AxsVxlanStatsTunnelDecapPackets_Type = Counter32
_AxsVxlanStatsTunnelDecapPackets_Object = MibTableColumn
axsVxlanStatsTunnelDecapPackets = _AxsVxlanStatsTunnelDecapPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 2, 1, 4),
    _AxsVxlanStatsTunnelDecapPackets_Type()
)
axsVxlanStatsTunnelDecapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsTunnelDecapPackets.setStatus("mandatory")
_AxsVxlanStatsTunnelDecapOctets_Type = Counter64
_AxsVxlanStatsTunnelDecapOctets_Object = MibTableColumn
axsVxlanStatsTunnelDecapOctets = _AxsVxlanStatsTunnelDecapOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 410, 2, 1, 5),
    _AxsVxlanStatsTunnelDecapOctets_Type()
)
axsVxlanStatsTunnelDecapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVxlanStatsTunnelDecapOctets.setStatus("mandatory")
_Ax4630sMib_ObjectIdentity = ObjectIdentity
ax4630sMib = _Ax4630sMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20)
)
_Ax4630sSwitch_ObjectIdentity = ObjectIdentity
ax4630sSwitch = _Ax4630sSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1)
)


class _Ax4630sModelType_Type(Integer32):
    """Custom type ax4630sModelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1900
        )
    )
    namedValues = NamedValues(
        ("model-AX4630S-4M", 1900)
    )


_Ax4630sModelType_Type.__name__ = "Integer32"
_Ax4630sModelType_Object = MibScalar
ax4630sModelType = _Ax4630sModelType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 1),
    _Ax4630sModelType_Type()
)
ax4630sModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sModelType.setStatus("mandatory")
_Ax4630sSoftware_ObjectIdentity = ObjectIdentity
ax4630sSoftware = _Ax4630sSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 2)
)


class _Ax4630sSoftwareName_Type(DisplayString):
    """Custom type ax4630sSoftwareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax4630sSoftwareName_Type.__name__ = "DisplayString"
_Ax4630sSoftwareName_Object = MibScalar
ax4630sSoftwareName = _Ax4630sSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 2, 1),
    _Ax4630sSoftwareName_Type()
)
ax4630sSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSoftwareName.setStatus("mandatory")


class _Ax4630sSoftwareAbbreviation_Type(DisplayString):
    """Custom type ax4630sSoftwareAbbreviation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_Ax4630sSoftwareAbbreviation_Type.__name__ = "DisplayString"
_Ax4630sSoftwareAbbreviation_Object = MibScalar
ax4630sSoftwareAbbreviation = _Ax4630sSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 2, 2),
    _Ax4630sSoftwareAbbreviation_Type()
)
ax4630sSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSoftwareAbbreviation.setStatus("mandatory")


class _Ax4630sSoftwareVersion_Type(DisplayString):
    """Custom type ax4630sSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax4630sSoftwareVersion_Type.__name__ = "DisplayString"
_Ax4630sSoftwareVersion_Object = MibScalar
ax4630sSoftwareVersion = _Ax4630sSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 2, 3),
    _Ax4630sSoftwareVersion_Type()
)
ax4630sSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSoftwareVersion.setStatus("mandatory")
_Ax4630sSystemMsg_ObjectIdentity = ObjectIdentity
ax4630sSystemMsg = _Ax4630sSystemMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 3)
)


class _Ax4630sSystemMsgText_Type(DisplayString):
    """Custom type ax4630sSystemMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Ax4630sSystemMsgText_Type.__name__ = "DisplayString"
_Ax4630sSystemMsgText_Object = MibScalar
ax4630sSystemMsgText = _Ax4630sSystemMsgText_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 3, 1),
    _Ax4630sSystemMsgText_Type()
)
ax4630sSystemMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSystemMsgText.setStatus("mandatory")


class _Ax4630sSystemMsgType_Type(OctetString):
    """Custom type ax4630sSystemMsgType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Ax4630sSystemMsgType_Type.__name__ = "OctetString"
_Ax4630sSystemMsgType_Object = MibScalar
ax4630sSystemMsgType = _Ax4630sSystemMsgType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 3, 2),
    _Ax4630sSystemMsgType_Type()
)
ax4630sSystemMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSystemMsgType.setStatus("mandatory")


class _Ax4630sSystemMsgTimeStamp_Type(DisplayString):
    """Custom type ax4630sSystemMsgTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Ax4630sSystemMsgTimeStamp_Type.__name__ = "DisplayString"
_Ax4630sSystemMsgTimeStamp_Object = MibScalar
ax4630sSystemMsgTimeStamp = _Ax4630sSystemMsgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 3, 3),
    _Ax4630sSystemMsgTimeStamp_Type()
)
ax4630sSystemMsgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSystemMsgTimeStamp.setStatus("mandatory")


class _Ax4630sSystemMsgLevel_Type(OctetString):
    """Custom type ax4630sSystemMsgLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Ax4630sSystemMsgLevel_Type.__name__ = "OctetString"
_Ax4630sSystemMsgLevel_Object = MibScalar
ax4630sSystemMsgLevel = _Ax4630sSystemMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 3, 4),
    _Ax4630sSystemMsgLevel_Type()
)
ax4630sSystemMsgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSystemMsgLevel.setStatus("mandatory")


class _Ax4630sSystemMsgEventPoint_Type(DisplayString):
    """Custom type ax4630sSystemMsgEventPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ax4630sSystemMsgEventPoint_Type.__name__ = "DisplayString"
_Ax4630sSystemMsgEventPoint_Object = MibScalar
ax4630sSystemMsgEventPoint = _Ax4630sSystemMsgEventPoint_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 3, 5),
    _Ax4630sSystemMsgEventPoint_Type()
)
ax4630sSystemMsgEventPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSystemMsgEventPoint.setStatus("mandatory")


class _Ax4630sSystemMsgEventInterfaceID_Type(DisplayString):
    """Custom type ax4630sSystemMsgEventInterfaceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Ax4630sSystemMsgEventInterfaceID_Type.__name__ = "DisplayString"
_Ax4630sSystemMsgEventInterfaceID_Object = MibScalar
ax4630sSystemMsgEventInterfaceID = _Ax4630sSystemMsgEventInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 3, 6),
    _Ax4630sSystemMsgEventInterfaceID_Type()
)
ax4630sSystemMsgEventInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSystemMsgEventInterfaceID.setStatus("mandatory")


class _Ax4630sSystemMsgEventCode_Type(OctetString):
    """Custom type ax4630sSystemMsgEventCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Ax4630sSystemMsgEventCode_Type.__name__ = "OctetString"
_Ax4630sSystemMsgEventCode_Object = MibScalar
ax4630sSystemMsgEventCode = _Ax4630sSystemMsgEventCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 3, 7),
    _Ax4630sSystemMsgEventCode_Type()
)
ax4630sSystemMsgEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSystemMsgEventCode.setStatus("mandatory")


class _Ax4630sSystemMsgAdditionalCode_Type(OctetString):
    """Custom type ax4630sSystemMsgAdditionalCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Ax4630sSystemMsgAdditionalCode_Type.__name__ = "OctetString"
_Ax4630sSystemMsgAdditionalCode_Object = MibScalar
ax4630sSystemMsgAdditionalCode = _Ax4630sSystemMsgAdditionalCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 3, 8),
    _Ax4630sSystemMsgAdditionalCode_Type()
)
ax4630sSystemMsgAdditionalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSystemMsgAdditionalCode.setStatus("mandatory")
_Ax4630sSnmpAgent_ObjectIdentity = ObjectIdentity
ax4630sSnmpAgent = _Ax4630sSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 4)
)
_Ax4630sSnmpSendReceiveSize_Type = Integer32
_Ax4630sSnmpSendReceiveSize_Object = MibScalar
ax4630sSnmpSendReceiveSize = _Ax4630sSnmpSendReceiveSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 4, 1),
    _Ax4630sSnmpSendReceiveSize_Type()
)
ax4630sSnmpSendReceiveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSnmpSendReceiveSize.setStatus("mandatory")
_Ax4630sSnmpReceiveDelay_Type = Integer32
_Ax4630sSnmpReceiveDelay_Object = MibScalar
ax4630sSnmpReceiveDelay = _Ax4630sSnmpReceiveDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 4, 2),
    _Ax4630sSnmpReceiveDelay_Type()
)
ax4630sSnmpReceiveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSnmpReceiveDelay.setStatus("mandatory")
_Ax4630sSnmpContinuousSend_Type = Integer32
_Ax4630sSnmpContinuousSend_Object = MibScalar
ax4630sSnmpContinuousSend = _Ax4630sSnmpContinuousSend_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 4, 3),
    _Ax4630sSnmpContinuousSend_Type()
)
ax4630sSnmpContinuousSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSnmpContinuousSend.setStatus("mandatory")
_Ax4630sSnmpObjectMaxNumber_Type = Integer32
_Ax4630sSnmpObjectMaxNumber_Object = MibScalar
ax4630sSnmpObjectMaxNumber = _Ax4630sSnmpObjectMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 4, 4),
    _Ax4630sSnmpObjectMaxNumber_Type()
)
ax4630sSnmpObjectMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSnmpObjectMaxNumber.setStatus("mandatory")
_Ax4630sLicense_ObjectIdentity = ObjectIdentity
ax4630sLicense = _Ax4630sLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6)
)
_Ax4630sLicenseNumber_Type = Integer32
_Ax4630sLicenseNumber_Object = MibScalar
ax4630sLicenseNumber = _Ax4630sLicenseNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 1),
    _Ax4630sLicenseNumber_Type()
)
ax4630sLicenseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sLicenseNumber.setStatus("mandatory")
_Ax4630sLicenseTable_Object = MibTable
ax4630sLicenseTable = _Ax4630sLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ax4630sLicenseTable.setStatus("mandatory")
_Ax4630sLicenseEntry_Object = MibTableRow
ax4630sLicenseEntry = _Ax4630sLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 2, 1)
)
ax4630sLicenseEntry.setIndexNames(
    (0, "AX4630S", "ax4630sLicenseIndex"),
)
if mibBuilder.loadTexts:
    ax4630sLicenseEntry.setStatus("mandatory")
_Ax4630sLicenseIndex_Type = Integer32
_Ax4630sLicenseIndex_Object = MibTableColumn
ax4630sLicenseIndex = _Ax4630sLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 2, 1, 1),
    _Ax4630sLicenseIndex_Type()
)
ax4630sLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sLicenseIndex.setStatus("mandatory")
_Ax4630sLicenseSerialNumber_Type = DisplayString
_Ax4630sLicenseSerialNumber_Object = MibTableColumn
ax4630sLicenseSerialNumber = _Ax4630sLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 2, 1, 2),
    _Ax4630sLicenseSerialNumber_Type()
)
ax4630sLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sLicenseSerialNumber.setStatus("mandatory")
_Ax4630sLicenseOptionNumber_Type = Integer32
_Ax4630sLicenseOptionNumber_Object = MibTableColumn
ax4630sLicenseOptionNumber = _Ax4630sLicenseOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 2, 1, 3),
    _Ax4630sLicenseOptionNumber_Type()
)
ax4630sLicenseOptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sLicenseOptionNumber.setStatus("mandatory")
_Ax4630sLicenseOptionTable_Object = MibTable
ax4630sLicenseOptionTable = _Ax4630sLicenseOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 3)
)
if mibBuilder.loadTexts:
    ax4630sLicenseOptionTable.setStatus("mandatory")
_Ax4630sLicenseOptionEntry_Object = MibTableRow
ax4630sLicenseOptionEntry = _Ax4630sLicenseOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 3, 1)
)
ax4630sLicenseOptionEntry.setIndexNames(
    (0, "AX4630S", "ax4630sLicenseOptionIndex"),
    (0, "AX4630S", "ax4630sLicenseOptionNumberIndex"),
)
if mibBuilder.loadTexts:
    ax4630sLicenseOptionEntry.setStatus("mandatory")
_Ax4630sLicenseOptionIndex_Type = Integer32
_Ax4630sLicenseOptionIndex_Object = MibTableColumn
ax4630sLicenseOptionIndex = _Ax4630sLicenseOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 3, 1, 1),
    _Ax4630sLicenseOptionIndex_Type()
)
ax4630sLicenseOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sLicenseOptionIndex.setStatus("mandatory")
_Ax4630sLicenseOptionNumberIndex_Type = Integer32
_Ax4630sLicenseOptionNumberIndex_Object = MibTableColumn
ax4630sLicenseOptionNumberIndex = _Ax4630sLicenseOptionNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 3, 1, 2),
    _Ax4630sLicenseOptionNumberIndex_Type()
)
ax4630sLicenseOptionNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sLicenseOptionNumberIndex.setStatus("mandatory")
_Ax4630sLicenseOptionSoftwareName_Type = DisplayString
_Ax4630sLicenseOptionSoftwareName_Object = MibTableColumn
ax4630sLicenseOptionSoftwareName = _Ax4630sLicenseOptionSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 3, 1, 3),
    _Ax4630sLicenseOptionSoftwareName_Type()
)
ax4630sLicenseOptionSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sLicenseOptionSoftwareName.setStatus("mandatory")
_Ax4630sLicenseOptionSoftwareAbbreviation_Type = DisplayString
_Ax4630sLicenseOptionSoftwareAbbreviation_Object = MibTableColumn
ax4630sLicenseOptionSoftwareAbbreviation = _Ax4630sLicenseOptionSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 1, 6, 3, 1, 4),
    _Ax4630sLicenseOptionSoftwareAbbreviation_Type()
)
ax4630sLicenseOptionSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sLicenseOptionSoftwareAbbreviation.setStatus("mandatory")
_Ax4630sDevice_ObjectIdentity = ObjectIdentity
ax4630sDevice = _Ax4630sDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2)
)
_Ax4630sChassis_ObjectIdentity = ObjectIdentity
ax4630sChassis = _Ax4630sChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1)
)
_Ax4630sChassisMaxNumber_Type = Integer32
_Ax4630sChassisMaxNumber_Object = MibScalar
ax4630sChassisMaxNumber = _Ax4630sChassisMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 1),
    _Ax4630sChassisMaxNumber_Type()
)
ax4630sChassisMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sChassisMaxNumber.setStatus("mandatory")
_Ax4630sChassisTable_Object = MibTable
ax4630sChassisTable = _Ax4630sChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ax4630sChassisTable.setStatus("mandatory")
_Ax4630sChassisEntry_Object = MibTableRow
ax4630sChassisEntry = _Ax4630sChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1)
)
ax4630sChassisEntry.setIndexNames(
    (0, "AX4630S", "ax4630sChassisIndex"),
)
if mibBuilder.loadTexts:
    ax4630sChassisEntry.setStatus("mandatory")
_Ax4630sChassisIndex_Type = Integer32
_Ax4630sChassisIndex_Object = MibTableColumn
ax4630sChassisIndex = _Ax4630sChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 1),
    _Ax4630sChassisIndex_Type()
)
ax4630sChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sChassisIndex.setStatus("mandatory")


class _Ax4630sChassisType_Type(Integer32):
    """Custom type ax4630sChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1900
        )
    )
    namedValues = NamedValues(
        ("model-AX4630S-4M", 1900)
    )


_Ax4630sChassisType_Type.__name__ = "Integer32"
_Ax4630sChassisType_Object = MibTableColumn
ax4630sChassisType = _Ax4630sChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 2),
    _Ax4630sChassisType_Type()
)
ax4630sChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sChassisType.setStatus("mandatory")


class _Ax4630sChassisStatus_Type(Integer32):
    """Custom type ax4630sChassisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("up", 2)
    )


_Ax4630sChassisStatus_Type.__name__ = "Integer32"
_Ax4630sChassisStatus_Object = MibTableColumn
ax4630sChassisStatus = _Ax4630sChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 3),
    _Ax4630sChassisStatus_Type()
)
ax4630sChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sChassisStatus.setStatus("mandatory")


class _Ax4630sStsLedStatus_Type(Integer32):
    """Custom type ax4630sStsLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("green-light-blink", 1),
          ("green-light-on", 2),
          ("red-light-blink", 3),
          ("red-light-on", 4),
          ("light-off", 6),
          ("green-light-blink2", 7))
    )


_Ax4630sStsLedStatus_Type.__name__ = "Integer32"
_Ax4630sStsLedStatus_Object = MibTableColumn
ax4630sStsLedStatus = _Ax4630sStsLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 4),
    _Ax4630sStsLedStatus_Type()
)
ax4630sStsLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sStsLedStatus.setStatus("mandatory")
_Ax4630sCpuName_Type = DisplayString
_Ax4630sCpuName_Object = MibTableColumn
ax4630sCpuName = _Ax4630sCpuName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 5),
    _Ax4630sCpuName_Type()
)
ax4630sCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sCpuName.setStatus("mandatory")
_Ax4630sCpuClock_Type = Integer32
_Ax4630sCpuClock_Object = MibTableColumn
ax4630sCpuClock = _Ax4630sCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 6),
    _Ax4630sCpuClock_Type()
)
ax4630sCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sCpuClock.setStatus("mandatory")
_Ax4630sMemoryTotalSize_Type = Integer32
_Ax4630sMemoryTotalSize_Object = MibTableColumn
ax4630sMemoryTotalSize = _Ax4630sMemoryTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 7),
    _Ax4630sMemoryTotalSize_Type()
)
ax4630sMemoryTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sMemoryTotalSize.setStatus("mandatory")
_Ax4630sMemoryUsedSize_Type = Integer32
_Ax4630sMemoryUsedSize_Object = MibTableColumn
ax4630sMemoryUsedSize = _Ax4630sMemoryUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 8),
    _Ax4630sMemoryUsedSize_Type()
)
ax4630sMemoryUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sMemoryUsedSize.setStatus("mandatory")
_Ax4630sMemoryFreeSize_Type = Integer32
_Ax4630sMemoryFreeSize_Object = MibTableColumn
ax4630sMemoryFreeSize = _Ax4630sMemoryFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 9),
    _Ax4630sMemoryFreeSize_Type()
)
ax4630sMemoryFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sMemoryFreeSize.setStatus("mandatory")
_Ax4630sRomVersion_Type = DisplayString
_Ax4630sRomVersion_Object = MibTableColumn
ax4630sRomVersion = _Ax4630sRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 10),
    _Ax4630sRomVersion_Type()
)
ax4630sRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sRomVersion.setStatus("mandatory")
_Ax4630sCpuLoad1m_Type = Integer32
_Ax4630sCpuLoad1m_Object = MibTableColumn
ax4630sCpuLoad1m = _Ax4630sCpuLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 11),
    _Ax4630sCpuLoad1m_Type()
)
ax4630sCpuLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sCpuLoad1m.setStatus("mandatory")
_Ax4630sFlashTotalSize_Type = Integer32
_Ax4630sFlashTotalSize_Object = MibTableColumn
ax4630sFlashTotalSize = _Ax4630sFlashTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 12),
    _Ax4630sFlashTotalSize_Type()
)
ax4630sFlashTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFlashTotalSize.setStatus("mandatory")
_Ax4630sFlashUsedSize_Type = Integer32
_Ax4630sFlashUsedSize_Object = MibTableColumn
ax4630sFlashUsedSize = _Ax4630sFlashUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 13),
    _Ax4630sFlashUsedSize_Type()
)
ax4630sFlashUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFlashUsedSize.setStatus("mandatory")
_Ax4630sFlashFreeSize_Type = Integer32
_Ax4630sFlashFreeSize_Object = MibTableColumn
ax4630sFlashFreeSize = _Ax4630sFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 14),
    _Ax4630sFlashFreeSize_Type()
)
ax4630sFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFlashFreeSize.setStatus("mandatory")


class _Ax4630sSdCardStatus_Type(Integer32):
    """Custom type ax4630sSdCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              32)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 32))
    )


_Ax4630sSdCardStatus_Type.__name__ = "Integer32"
_Ax4630sSdCardStatus_Object = MibTableColumn
ax4630sSdCardStatus = _Ax4630sSdCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 15),
    _Ax4630sSdCardStatus_Type()
)
ax4630sSdCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSdCardStatus.setStatus("mandatory")
_Ax4630sSdCardTotalSize_Type = Integer32
_Ax4630sSdCardTotalSize_Object = MibTableColumn
ax4630sSdCardTotalSize = _Ax4630sSdCardTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 16),
    _Ax4630sSdCardTotalSize_Type()
)
ax4630sSdCardTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSdCardTotalSize.setStatus("mandatory")
_Ax4630sSdCardUsedSize_Type = Integer32
_Ax4630sSdCardUsedSize_Object = MibTableColumn
ax4630sSdCardUsedSize = _Ax4630sSdCardUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 17),
    _Ax4630sSdCardUsedSize_Type()
)
ax4630sSdCardUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSdCardUsedSize.setStatus("mandatory")
_Ax4630sSdCardFreeSize_Type = Integer32
_Ax4630sSdCardFreeSize_Object = MibTableColumn
ax4630sSdCardFreeSize = _Ax4630sSdCardFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 18),
    _Ax4630sSdCardFreeSize_Type()
)
ax4630sSdCardFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sSdCardFreeSize.setStatus("mandatory")
_Ax4630sPhysLineNumber_Type = Integer32
_Ax4630sPhysLineNumber_Object = MibTableColumn
ax4630sPhysLineNumber = _Ax4630sPhysLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 19),
    _Ax4630sPhysLineNumber_Type()
)
ax4630sPhysLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPhysLineNumber.setStatus("mandatory")
_Ax4630sTemperatureStatusNumber_Type = Integer32
_Ax4630sTemperatureStatusNumber_Object = MibTableColumn
ax4630sTemperatureStatusNumber = _Ax4630sTemperatureStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 20),
    _Ax4630sTemperatureStatusNumber_Type()
)
ax4630sTemperatureStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sTemperatureStatusNumber.setStatus("mandatory")
_Ax4630sPowerUnitNumber_Type = Integer32
_Ax4630sPowerUnitNumber_Object = MibTableColumn
ax4630sPowerUnitNumber = _Ax4630sPowerUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 21),
    _Ax4630sPowerUnitNumber_Type()
)
ax4630sPowerUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPowerUnitNumber.setStatus("mandatory")
_Ax4630sRedundantPsNumber_Type = Integer32
_Ax4630sRedundantPsNumber_Object = MibTableColumn
ax4630sRedundantPsNumber = _Ax4630sRedundantPsNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 22),
    _Ax4630sRedundantPsNumber_Type()
)
ax4630sRedundantPsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sRedundantPsNumber.setStatus("mandatory")
_Ax4630sFanNumber_Type = Integer32
_Ax4630sFanNumber_Object = MibTableColumn
ax4630sFanNumber = _Ax4630sFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 23),
    _Ax4630sFanNumber_Type()
)
ax4630sFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFanNumber.setStatus("mandatory")
_Ax4630sTotalAccumRunTime_Type = Integer32
_Ax4630sTotalAccumRunTime_Object = MibTableColumn
ax4630sTotalAccumRunTime = _Ax4630sTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 24),
    _Ax4630sTotalAccumRunTime_Type()
)
ax4630sTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sTotalAccumRunTime.setStatus("mandatory")
_Ax4630sCriticalAccumRunTime_Type = Integer32
_Ax4630sCriticalAccumRunTime_Object = MibTableColumn
ax4630sCriticalAccumRunTime = _Ax4630sCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 25),
    _Ax4630sCriticalAccumRunTime_Type()
)
ax4630sCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sCriticalAccumRunTime.setStatus("mandatory")
_Ax4630sModuleSlotNumber_Type = Integer32
_Ax4630sModuleSlotNumber_Object = MibTableColumn
ax4630sModuleSlotNumber = _Ax4630sModuleSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 26),
    _Ax4630sModuleSlotNumber_Type()
)
ax4630sModuleSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sModuleSlotNumber.setStatus("mandatory")


class _Ax4630sMgmtPortStatus_Type(Integer32):
    """Custom type ax4630sMgmtPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              2,
              4,
              6,
              7,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", -1),
          ("active", 2),
          ("down", 4),
          ("disabled", 6),
          ("maintenance", 7),
          ("line-test", 9),
          ("unused", 10))
    )


_Ax4630sMgmtPortStatus_Type.__name__ = "Integer32"
_Ax4630sMgmtPortStatus_Object = MibTableColumn
ax4630sMgmtPortStatus = _Ax4630sMgmtPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 27),
    _Ax4630sMgmtPortStatus_Type()
)
ax4630sMgmtPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sMgmtPortStatus.setStatus("mandatory")
_Ax4630sNifBoardNumber_Type = Integer32
_Ax4630sNifBoardNumber_Object = MibTableColumn
ax4630sNifBoardNumber = _Ax4630sNifBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 2, 1, 28),
    _Ax4630sNifBoardNumber_Type()
)
ax4630sNifBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sNifBoardNumber.setStatus("mandatory")
_Ax4630sTemperatureStatusTable_Object = MibTable
ax4630sTemperatureStatusTable = _Ax4630sTemperatureStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ax4630sTemperatureStatusTable.setStatus("mandatory")
_Ax4630sTemperatureStatusEntry_Object = MibTableRow
ax4630sTemperatureStatusEntry = _Ax4630sTemperatureStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 3, 1)
)
ax4630sTemperatureStatusEntry.setIndexNames(
    (0, "AX4630S", "ax4630sChassisIndex"),
    (0, "AX4630S", "ax4630sTemperatureStatusIndex"),
)
if mibBuilder.loadTexts:
    ax4630sTemperatureStatusEntry.setStatus("mandatory")
_Ax4630sTemperatureStatusIndex_Type = Integer32
_Ax4630sTemperatureStatusIndex_Object = MibTableColumn
ax4630sTemperatureStatusIndex = _Ax4630sTemperatureStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 3, 1, 1),
    _Ax4630sTemperatureStatusIndex_Type()
)
ax4630sTemperatureStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sTemperatureStatusIndex.setStatus("mandatory")


class _Ax4630sTemperatureStatusDescr_Type(DisplayString):
    """Custom type ax4630sTemperatureStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ax4630sTemperatureStatusDescr_Type.__name__ = "DisplayString"
_Ax4630sTemperatureStatusDescr_Object = MibTableColumn
ax4630sTemperatureStatusDescr = _Ax4630sTemperatureStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 3, 1, 2),
    _Ax4630sTemperatureStatusDescr_Type()
)
ax4630sTemperatureStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sTemperatureStatusDescr.setStatus("mandatory")
_Ax4630sTemperatureStatusValue_Type = Integer32
_Ax4630sTemperatureStatusValue_Object = MibTableColumn
ax4630sTemperatureStatusValue = _Ax4630sTemperatureStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 3, 1, 3),
    _Ax4630sTemperatureStatusValue_Type()
)
ax4630sTemperatureStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sTemperatureStatusValue.setStatus("mandatory")
_Ax4630sTemperatureThreshold_Type = Integer32
_Ax4630sTemperatureThreshold_Object = MibTableColumn
ax4630sTemperatureThreshold = _Ax4630sTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 3, 1, 4),
    _Ax4630sTemperatureThreshold_Type()
)
ax4630sTemperatureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sTemperatureThreshold.setStatus("mandatory")


class _Ax4630sTemperatureState_Type(Integer32):
    """Custom type ax4630sTemperatureState based on Integer32"""
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
          ("caution", 2),
          ("warning", 3),
          ("fatal", 4))
    )


_Ax4630sTemperatureState_Type.__name__ = "Integer32"
_Ax4630sTemperatureState_Object = MibTableColumn
ax4630sTemperatureState = _Ax4630sTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 3, 1, 5),
    _Ax4630sTemperatureState_Type()
)
ax4630sTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sTemperatureState.setStatus("mandatory")
_Ax4630sPowerUnitTable_Object = MibTable
ax4630sPowerUnitTable = _Ax4630sPowerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ax4630sPowerUnitTable.setStatus("mandatory")
_Ax4630sPowerUnitEntry_Object = MibTableRow
ax4630sPowerUnitEntry = _Ax4630sPowerUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 4, 1)
)
ax4630sPowerUnitEntry.setIndexNames(
    (0, "AX4630S", "ax4630sChassisIndex"),
    (0, "AX4630S", "ax4630sPowerUnitIndex"),
)
if mibBuilder.loadTexts:
    ax4630sPowerUnitEntry.setStatus("mandatory")
_Ax4630sPowerUnitIndex_Type = Integer32
_Ax4630sPowerUnitIndex_Object = MibTableColumn
ax4630sPowerUnitIndex = _Ax4630sPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 4, 1, 1),
    _Ax4630sPowerUnitIndex_Type()
)
ax4630sPowerUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sPowerUnitIndex.setStatus("mandatory")


class _Ax4630sPowerConnectStatus_Type(Integer32):
    """Custom type ax4630sPowerConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              32)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 32))
    )


_Ax4630sPowerConnectStatus_Type.__name__ = "Integer32"
_Ax4630sPowerConnectStatus_Object = MibTableColumn
ax4630sPowerConnectStatus = _Ax4630sPowerConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 4, 1, 2),
    _Ax4630sPowerConnectStatus_Type()
)
ax4630sPowerConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPowerConnectStatus.setStatus("mandatory")


class _Ax4630sPowerSupplyStatus_Type(Integer32):
    """Custom type ax4630sPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", -1),
          ("ok", 2),
          ("fault", 4))
    )


_Ax4630sPowerSupplyStatus_Type.__name__ = "Integer32"
_Ax4630sPowerSupplyStatus_Object = MibTableColumn
ax4630sPowerSupplyStatus = _Ax4630sPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 4, 1, 3),
    _Ax4630sPowerSupplyStatus_Type()
)
ax4630sPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPowerSupplyStatus.setStatus("mandatory")


class _Ax4630sPowerSlotType_Type(Integer32):
    """Custom type ax4630sPowerSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("powerModule-AC", 1),
          ("powerModule-DC", 2))
    )


_Ax4630sPowerSlotType_Type.__name__ = "Integer32"
_Ax4630sPowerSlotType_Object = MibTableColumn
ax4630sPowerSlotType = _Ax4630sPowerSlotType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 4, 1, 4),
    _Ax4630sPowerSlotType_Type()
)
ax4630sPowerSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPowerSlotType.setStatus("mandatory")


class _Ax4630sPowerFanDirection_Type(Integer32):
    """Custom type ax4630sPowerFanDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("front-to-rear", 0),
          ("rear-to-front", 1))
    )


_Ax4630sPowerFanDirection_Type.__name__ = "Integer32"
_Ax4630sPowerFanDirection_Object = MibTableColumn
ax4630sPowerFanDirection = _Ax4630sPowerFanDirection_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 4, 1, 5),
    _Ax4630sPowerFanDirection_Type()
)
ax4630sPowerFanDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPowerFanDirection.setStatus("mandatory")
_Ax4630sFanTable_Object = MibTable
ax4630sFanTable = _Ax4630sFanTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ax4630sFanTable.setStatus("mandatory")
_Ax4630sFanEntry_Object = MibTableRow
ax4630sFanEntry = _Ax4630sFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 5, 1)
)
ax4630sFanEntry.setIndexNames(
    (0, "AX4630S", "ax4630sChassisIndex"),
    (0, "AX4630S", "ax4630sFanIndex"),
)
if mibBuilder.loadTexts:
    ax4630sFanEntry.setStatus("mandatory")
_Ax4630sFanIndex_Type = Integer32
_Ax4630sFanIndex_Object = MibTableColumn
ax4630sFanIndex = _Ax4630sFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 5, 1, 1),
    _Ax4630sFanIndex_Type()
)
ax4630sFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sFanIndex.setStatus("mandatory")


class _Ax4630sFanStatus_Type(Integer32):
    """Custom type ax4630sFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 2),
          ("high-speed", 3),
          ("fault", 4))
    )


_Ax4630sFanStatus_Type.__name__ = "Integer32"
_Ax4630sFanStatus_Object = MibTableColumn
ax4630sFanStatus = _Ax4630sFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 5, 1, 2),
    _Ax4630sFanStatus_Type()
)
ax4630sFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFanStatus.setStatus("mandatory")


class _Ax4630sFanDirection_Type(Integer32):
    """Custom type ax4630sFanDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("front-to-rear", 0),
          ("rear-to-front", 1))
    )


_Ax4630sFanDirection_Type.__name__ = "Integer32"
_Ax4630sFanDirection_Object = MibTableColumn
ax4630sFanDirection = _Ax4630sFanDirection_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 5, 1, 3),
    _Ax4630sFanDirection_Type()
)
ax4630sFanDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFanDirection.setStatus("mandatory")
_Ax4630sModuleSlotTable_Object = MibTable
ax4630sModuleSlotTable = _Ax4630sModuleSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ax4630sModuleSlotTable.setStatus("mandatory")
_Ax4630sModuleSlotEntry_Object = MibTableRow
ax4630sModuleSlotEntry = _Ax4630sModuleSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 7, 1)
)
ax4630sModuleSlotEntry.setIndexNames(
    (0, "AX4630S", "ax4630sChassisIndex"),
    (0, "AX4630S", "ax4630sModuleSlotIndex"),
)
if mibBuilder.loadTexts:
    ax4630sModuleSlotEntry.setStatus("mandatory")
_Ax4630sModuleSlotIndex_Type = Integer32
_Ax4630sModuleSlotIndex_Object = MibTableColumn
ax4630sModuleSlotIndex = _Ax4630sModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 7, 1, 1),
    _Ax4630sModuleSlotIndex_Type()
)
ax4630sModuleSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sModuleSlotIndex.setStatus("mandatory")


class _Ax4630sModuleSlotStatus_Type(Integer32):
    """Custom type ax4630sModuleSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("down", 4),
          ("disconnected", 32))
    )


_Ax4630sModuleSlotStatus_Type.__name__ = "Integer32"
_Ax4630sModuleSlotStatus_Object = MibTableColumn
ax4630sModuleSlotStatus = _Ax4630sModuleSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 7, 1, 2),
    _Ax4630sModuleSlotStatus_Type()
)
ax4630sModuleSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sModuleSlotStatus.setStatus("mandatory")


class _Ax4630sModuleSlotType_Type(Integer32):
    """Custom type ax4630sModuleSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("powerModule-AC", 1),
          ("powerModule-DC", 2))
    )


_Ax4630sModuleSlotType_Type.__name__ = "Integer32"
_Ax4630sModuleSlotType_Object = MibTableColumn
ax4630sModuleSlotType = _Ax4630sModuleSlotType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 1, 7, 1, 3),
    _Ax4630sModuleSlotType_Type()
)
ax4630sModuleSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sModuleSlotType.setStatus("mandatory")
_Ax4630sNifBoard_ObjectIdentity = ObjectIdentity
ax4630sNifBoard = _Ax4630sNifBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4)
)
_Ax4630sNifBoardTable_Object = MibTable
ax4630sNifBoardTable = _Ax4630sNifBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ax4630sNifBoardTable.setStatus("mandatory")
_Ax4630sNifBoardEntry_Object = MibTableRow
ax4630sNifBoardEntry = _Ax4630sNifBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4, 1, 1)
)
ax4630sNifBoardEntry.setIndexNames(
    (0, "AX4630S", "ax4630sChassisIndex"),
    (0, "AX4630S", "ax4630sNifBoardSlotIndex"),
)
if mibBuilder.loadTexts:
    ax4630sNifBoardEntry.setStatus("mandatory")
_Ax4630sNifBoardSlotIndex_Type = Integer32
_Ax4630sNifBoardSlotIndex_Object = MibTableColumn
ax4630sNifBoardSlotIndex = _Ax4630sNifBoardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4, 1, 1, 1),
    _Ax4630sNifBoardSlotIndex_Type()
)
ax4630sNifBoardSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sNifBoardSlotIndex.setStatus("mandatory")


class _Ax4630sNifBoardType_Type(Integer32):
    """Custom type ax4630sNifBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              6673,
              6675,
              6676,
              6679)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", -1),
          ("nif-24-port-10BASE-T-100BASE-TX-1000BASE-T", 6673),
          ("nif-24-port-1000BASE-X-SFP", 6675),
          ("nif-24-port-10GBASE-R-SFPP", 6676),
          ("nif-6-port-40GBASE-R-QSFPP", 6679))
    )


_Ax4630sNifBoardType_Type.__name__ = "Integer32"
_Ax4630sNifBoardType_Object = MibTableColumn
ax4630sNifBoardType = _Ax4630sNifBoardType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4, 1, 1, 2),
    _Ax4630sNifBoardType_Type()
)
ax4630sNifBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sNifBoardType.setStatus("mandatory")


class _Ax4630sNifBoardOperStatus_Type(Integer32):
    """Custom type ax4630sNifBoardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              32)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("active", 2),
          ("initialization", 3),
          ("down", 4),
          ("closed", 5),
          ("lock", 6),
          ("disconnect", 32))
    )


_Ax4630sNifBoardOperStatus_Type.__name__ = "Integer32"
_Ax4630sNifBoardOperStatus_Object = MibTableColumn
ax4630sNifBoardOperStatus = _Ax4630sNifBoardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4, 1, 1, 3),
    _Ax4630sNifBoardOperStatus_Type()
)
ax4630sNifBoardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sNifBoardOperStatus.setStatus("mandatory")


class _Ax4630sNifBoardName_Type(DisplayString):
    """Custom type ax4630sNifBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax4630sNifBoardName_Type.__name__ = "DisplayString"
_Ax4630sNifBoardName_Object = MibTableColumn
ax4630sNifBoardName = _Ax4630sNifBoardName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4, 1, 1, 4),
    _Ax4630sNifBoardName_Type()
)
ax4630sNifBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sNifBoardName.setStatus("mandatory")


class _Ax4630sNifBoardAbbreviation_Type(DisplayString):
    """Custom type ax4630sNifBoardAbbreviation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax4630sNifBoardAbbreviation_Type.__name__ = "DisplayString"
_Ax4630sNifBoardAbbreviation_Object = MibTableColumn
ax4630sNifBoardAbbreviation = _Ax4630sNifBoardAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4, 1, 1, 5),
    _Ax4630sNifBoardAbbreviation_Type()
)
ax4630sNifBoardAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sNifBoardAbbreviation.setStatus("mandatory")
_Ax4630sNifPhysLineNumber_Type = Integer32
_Ax4630sNifPhysLineNumber_Object = MibTableColumn
ax4630sNifPhysLineNumber = _Ax4630sNifPhysLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4, 1, 1, 7),
    _Ax4630sNifPhysLineNumber_Type()
)
ax4630sNifPhysLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sNifPhysLineNumber.setStatus("mandatory")


class _Ax4630sNifSerialNumber_Type(DisplayString):
    """Custom type ax4630sNifSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Ax4630sNifSerialNumber_Type.__name__ = "DisplayString"
_Ax4630sNifSerialNumber_Object = MibTableColumn
ax4630sNifSerialNumber = _Ax4630sNifSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 4, 1, 1, 8),
    _Ax4630sNifSerialNumber_Type()
)
ax4630sNifSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sNifSerialNumber.setStatus("mandatory")
_Ax4630sPhysLine_ObjectIdentity = ObjectIdentity
ax4630sPhysLine = _Ax4630sPhysLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 5)
)
_Ax4630sPhysLineTable_Object = MibTable
ax4630sPhysLineTable = _Ax4630sPhysLineTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ax4630sPhysLineTable.setStatus("mandatory")
_Ax4630sPhysLineEntry_Object = MibTableRow
ax4630sPhysLineEntry = _Ax4630sPhysLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 5, 1, 1)
)
ax4630sPhysLineEntry.setIndexNames(
    (0, "AX4630S", "ax4630sChassisIndex"),
    (0, "AX4630S", "ax4630sNifBoardSlotIndex"),
    (0, "AX4630S", "ax4630sPhysLineIndex"),
)
if mibBuilder.loadTexts:
    ax4630sPhysLineEntry.setStatus("mandatory")
_Ax4630sPhysLineIndex_Type = Integer32
_Ax4630sPhysLineIndex_Object = MibTableColumn
ax4630sPhysLineIndex = _Ax4630sPhysLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 5, 1, 1, 1),
    _Ax4630sPhysLineIndex_Type()
)
ax4630sPhysLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sPhysLineIndex.setStatus("mandatory")


class _Ax4630sPhysLineConnectorType_Type(Integer32):
    """Custom type ax4630sPhysLineConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              201,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              309,
              310,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              501,
              502,
              503,
              504,
              505,
              506)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("type100BASE-FX", 201),
          ("type1000BASE-LX", 301),
          ("type1000BASE-SX", 302),
          ("type1000BASE-LH", 303),
          ("type1000BASE-BX10-D", 304),
          ("type1000BASE-BX10-U", 305),
          ("type1000BASE-BX40-D", 306),
          ("type1000BASE-BX40-U", 307),
          ("type1000BASE-UTP", 309),
          ("type1000BASE-LHB", 310),
          ("type10GBASE-SR", 401),
          ("type10GBASE-LR", 402),
          ("type10GBASE-ER", 403),
          ("type10GBASE-ZR", 404),
          ("type10GBASE-CU1M", 405),
          ("type10GBASE-CU3M", 406),
          ("type10GBASE-CU5M", 407),
          ("type10GBASE-CU30CM", 408),
          ("type40GBASE-SR4", 501),
          ("type40GBASE-CU35CM", 502),
          ("type40GBASE-CU1M", 503),
          ("type40GBASE-CU3M", 504),
          ("type40GBASE-CU5M", 505),
          ("type40GBASE-LR4", 506))
    )


_Ax4630sPhysLineConnectorType_Type.__name__ = "Integer32"
_Ax4630sPhysLineConnectorType_Object = MibTableColumn
ax4630sPhysLineConnectorType = _Ax4630sPhysLineConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 5, 1, 1, 2),
    _Ax4630sPhysLineConnectorType_Type()
)
ax4630sPhysLineConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPhysLineConnectorType.setStatus("mandatory")


class _Ax4630sPhysLineOperStatus_Type(Integer32):
    """Custom type ax4630sPhysLineOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("active", 2),
          ("initialization", 3),
          ("down", 4),
          ("lock", 6),
          ("close", 7),
          ("line-fault", 8),
          ("test", 9),
          ("nothing-configuration", 10),
          ("suspend", 11))
    )


_Ax4630sPhysLineOperStatus_Type.__name__ = "Integer32"
_Ax4630sPhysLineOperStatus_Object = MibTableColumn
ax4630sPhysLineOperStatus = _Ax4630sPhysLineOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 5, 1, 1, 3),
    _Ax4630sPhysLineOperStatus_Type()
)
ax4630sPhysLineOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPhysLineOperStatus.setStatus("mandatory")
_Ax4630sPhysLineIfIndexNumber_Type = Integer32
_Ax4630sPhysLineIfIndexNumber_Object = MibTableColumn
ax4630sPhysLineIfIndexNumber = _Ax4630sPhysLineIfIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 5, 1, 1, 4),
    _Ax4630sPhysLineIfIndexNumber_Type()
)
ax4630sPhysLineIfIndexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPhysLineIfIndexNumber.setStatus("mandatory")


class _Ax4630sPhysLineTransceiverStatus_Type(Integer32):
    """Custom type ax4630sPhysLineTransceiverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              20,
              21,
              22,
              23,
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("unchangeable-transceiver", 1),
          ("sfp-mounted", 20),
          ("sfp-unmounted", 21),
          ("unsupported-sfp-mounted", 22),
          ("sfp-status-unknown", 23),
          ("qsfp-mounted", 50),
          ("qsfp-unmounted", 51),
          ("unsupported-qsfp-mounted", 52),
          ("qsfp-status-unknown", 53))
    )


_Ax4630sPhysLineTransceiverStatus_Type.__name__ = "Integer32"
_Ax4630sPhysLineTransceiverStatus_Object = MibTableColumn
ax4630sPhysLineTransceiverStatus = _Ax4630sPhysLineTransceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 5, 1, 1, 5),
    _Ax4630sPhysLineTransceiverStatus_Type()
)
ax4630sPhysLineTransceiverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sPhysLineTransceiverStatus.setStatus("mandatory")
_Ax4630sInterface_ObjectIdentity = ObjectIdentity
ax4630sInterface = _Ax4630sInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 6)
)
_Ax4630sLineIfTable_Object = MibTable
ax4630sLineIfTable = _Ax4630sLineIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ax4630sLineIfTable.setStatus("mandatory")
_Ax4630sLineIfEntry_Object = MibTableRow
ax4630sLineIfEntry = _Ax4630sLineIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 6, 1, 1)
)
ax4630sLineIfEntry.setIndexNames(
    (0, "AX4630S", "ax4630sChassisIndex"),
    (0, "AX4630S", "ax4630sNifBoardSlotIndex"),
    (0, "AX4630S", "ax4630sPhysLineIndex"),
    (0, "AX4630S", "ax4630sLineIfIndex"),
)
if mibBuilder.loadTexts:
    ax4630sLineIfEntry.setStatus("mandatory")
_Ax4630sLineIfIndex_Type = Integer32
_Ax4630sLineIfIndex_Object = MibTableColumn
ax4630sLineIfIndex = _Ax4630sLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 6, 1, 1, 1),
    _Ax4630sLineIfIndex_Type()
)
ax4630sLineIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sLineIfIndex.setStatus("mandatory")
_Ax4630sIfIndex_Type = Integer32
_Ax4630sIfIndex_Object = MibTableColumn
ax4630sIfIndex = _Ax4630sIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 2, 6, 1, 1, 2),
    _Ax4630sIfIndex_Type()
)
ax4630sIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sIfIndex.setStatus("mandatory")
_Ax4630sManagementMIB_ObjectIdentity = ObjectIdentity
ax4630sManagementMIB = _Ax4630sManagementMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 3)
)
_Ax4630sOperationCommand_ObjectIdentity = ObjectIdentity
ax4630sOperationCommand = _Ax4630sOperationCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 3, 1)
)
_Ax4630sFdbClearMIB_ObjectIdentity = ObjectIdentity
ax4630sFdbClearMIB = _Ax4630sFdbClearMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 3, 1, 1)
)


class _Ax4630sFdbClearSet_Type(Integer32):
    """Custom type ax4630sFdbClearSet based on Integer32"""
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
        *(("initialValue", 0),
          ("processing", 1),
          ("failure", 2),
          ("success", 3))
    )


_Ax4630sFdbClearSet_Type.__name__ = "Integer32"
_Ax4630sFdbClearSet_Object = MibScalar
ax4630sFdbClearSet = _Ax4630sFdbClearSet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 3, 1, 1, 1),
    _Ax4630sFdbClearSet_Type()
)
ax4630sFdbClearSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ax4630sFdbClearSet.setStatus("mandatory")
_Ax4630sFdbClearReqTime_Type = TimeTicks
_Ax4630sFdbClearReqTime_Object = MibScalar
ax4630sFdbClearReqTime = _Ax4630sFdbClearReqTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 3, 1, 1, 2),
    _Ax4630sFdbClearReqTime_Type()
)
ax4630sFdbClearReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFdbClearReqTime.setStatus("mandatory")
_Ax4630sFdbClearSuccessTime_Type = TimeTicks
_Ax4630sFdbClearSuccessTime_Object = MibScalar
ax4630sFdbClearSuccessTime = _Ax4630sFdbClearSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 3, 1, 1, 3),
    _Ax4630sFdbClearSuccessTime_Type()
)
ax4630sFdbClearSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFdbClearSuccessTime.setStatus("mandatory")
_Ax4630sFdb_ObjectIdentity = ObjectIdentity
ax4630sFdb = _Ax4630sFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 4)
)
_Ax4630sFdbCounterTable_Object = MibTable
ax4630sFdbCounterTable = _Ax4630sFdbCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 4, 1)
)
if mibBuilder.loadTexts:
    ax4630sFdbCounterTable.setStatus("mandatory")
_Ax4630sFdbCounterEntry_Object = MibTableRow
ax4630sFdbCounterEntry = _Ax4630sFdbCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 4, 1, 1)
)
ax4630sFdbCounterEntry.setIndexNames(
    (0, "AX4630S", "ax4630sChassisIndex"),
    (0, "AX4630S", "ax4630sFdbCounterNifIndex"),
    (0, "AX4630S", "ax4630sFdbCounterLineIndex"),
)
if mibBuilder.loadTexts:
    ax4630sFdbCounterEntry.setStatus("mandatory")
_Ax4630sFdbCounterNifIndex_Type = Integer32
_Ax4630sFdbCounterNifIndex_Object = MibTableColumn
ax4630sFdbCounterNifIndex = _Ax4630sFdbCounterNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 4, 1, 1, 1),
    _Ax4630sFdbCounterNifIndex_Type()
)
ax4630sFdbCounterNifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sFdbCounterNifIndex.setStatus("mandatory")
_Ax4630sFdbCounterLineIndex_Type = Integer32
_Ax4630sFdbCounterLineIndex_Object = MibTableColumn
ax4630sFdbCounterLineIndex = _Ax4630sFdbCounterLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 4, 1, 1, 2),
    _Ax4630sFdbCounterLineIndex_Type()
)
ax4630sFdbCounterLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax4630sFdbCounterLineIndex.setStatus("mandatory")
_Ax4630sFdbCounterCounts_Type = Counter32
_Ax4630sFdbCounterCounts_Object = MibTableColumn
ax4630sFdbCounterCounts = _Ax4630sFdbCounterCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 4, 1, 1, 3),
    _Ax4630sFdbCounterCounts_Type()
)
ax4630sFdbCounterCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFdbCounterCounts.setStatus("mandatory")


class _Ax4630sFdbCounterType_Type(Integer32):
    """Custom type ax4630sFdbCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlimited", 0),
          ("limited-and-Forward", 1),
          ("limited-and-Discard", 2))
    )


_Ax4630sFdbCounterType_Type.__name__ = "Integer32"
_Ax4630sFdbCounterType_Object = MibTableColumn
ax4630sFdbCounterType = _Ax4630sFdbCounterType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 4, 1, 1, 4),
    _Ax4630sFdbCounterType_Type()
)
ax4630sFdbCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFdbCounterType.setStatus("mandatory")
_Ax4630sFdbCounterLimits_Type = Counter32
_Ax4630sFdbCounterLimits_Object = MibTableColumn
ax4630sFdbCounterLimits = _Ax4630sFdbCounterLimits_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 20, 4, 1, 1, 5),
    _Ax4630sFdbCounterLimits_Type()
)
ax4630sFdbCounterLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax4630sFdbCounterLimits.setStatus("mandatory")

# Managed Objects groups


# Notification objects

axsOadpNeighborCachelastChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 2, 0, 1)
)
axsOadpNeighborCachelastChangeTrap.setObjects(
    ("AX4630S", "axsOadpNeighborCacheLastChange")
)
if mibBuilder.loadTexts:
    axsOadpNeighborCachelastChangeTrap.setStatus(
        ""
    )

axsOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 1)
)
axsOspfVirtIfStateChange.setObjects(
      *(("AX4630S", "axsOspfVirtIfDomainNumber"),
        ("AX4630S", "axsOspfRouterId"),
        ("AX4630S", "axsOspfVirtIfAreaId"),
        ("AX4630S", "axsOspfVirtIfNeighbor"),
        ("AX4630S", "axsOspfVirtIfState"))
)
if mibBuilder.loadTexts:
    axsOspfVirtIfStateChange.setStatus(
        ""
    )

axsOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 2)
)
axsOspfNbrStateChange.setObjects(
      *(("AX4630S", "axsOspfNbrDomainNumber"),
        ("AX4630S", "axsOspfRouterId"),
        ("AX4630S", "axsOspfNbrIpAddr"),
        ("AX4630S", "axsOspfNbrAddressLessIndex"),
        ("AX4630S", "axsOspfNbrRtrId"),
        ("AX4630S", "axsOspfNbrState"))
)
if mibBuilder.loadTexts:
    axsOspfNbrStateChange.setStatus(
        ""
    )

axsOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 3)
)
axsOspfVirtNbrStateChange.setObjects(
      *(("AX4630S", "axsOspfVirtNbrDomainNumber"),
        ("AX4630S", "axsOspfRouterId"),
        ("AX4630S", "axsOspfVirtNbrArea"),
        ("AX4630S", "axsOspfVirtNbrRtrId"),
        ("AX4630S", "axsOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    axsOspfVirtNbrStateChange.setStatus(
        ""
    )

axsOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 4)
)
axsOspfIfConfigError.setObjects(
      *(("AX4630S", "axsOspfIfDomainNumber"),
        ("AX4630S", "axsOspfRouterId"),
        ("AX4630S", "axsOspfIfIpAddress"),
        ("AX4630S", "axsOspfAddressLessIf"),
        ("AX4630S", "axsOspfPacketSrc"),
        ("AX4630S", "axsOspfConfigErrorType"),
        ("AX4630S", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfIfConfigError.setStatus(
        ""
    )

axsOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 5)
)
axsOspfVirtIfConfigError.setObjects(
      *(("AX4630S", "axsOspfVirtIfDomainNumber"),
        ("AX4630S", "axsOspfRouterId"),
        ("AX4630S", "axsOspfVirtIfAreaId"),
        ("AX4630S", "axsOspfVirtIfNeighbor"),
        ("AX4630S", "axsOspfConfigErrorType"),
        ("AX4630S", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfVirtIfConfigError.setStatus(
        ""
    )

axsOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 6)
)
axsOspfIfAuthFailure.setObjects(
      *(("AX4630S", "axsOspfIfDomainNumber"),
        ("AX4630S", "axsOspfRouterId"),
        ("AX4630S", "axsOspfIfIpAddress"),
        ("AX4630S", "axsOspfAddressLessIf"),
        ("AX4630S", "axsOspfPacketSrc"),
        ("AX4630S", "axsOspfConfigErrorType"),
        ("AX4630S", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfIfAuthFailure.setStatus(
        ""
    )

axsOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 7)
)
axsOspfVirtIfAuthFailure.setObjects(
      *(("AX4630S", "axsOspfVirtIfDomainNumber"),
        ("AX4630S", "axsOspfRouterId"),
        ("AX4630S", "axsOspfVirtIfAreaId"),
        ("AX4630S", "axsOspfVirtIfNeighbor"),
        ("AX4630S", "axsOspfConfigErrorType"),
        ("AX4630S", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfVirtIfAuthFailure.setStatus(
        ""
    )

axsOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 16)
)
axsOspfIfStateChange.setObjects(
      *(("AX4630S", "axsOspfIfDomainNumber"),
        ("AX4630S", "axsOspfRouterId"),
        ("AX4630S", "axsOspfIfIpAddress"),
        ("AX4630S", "axsOspfAddressLessIf"),
        ("AX4630S", "axsOspfIfState"))
)
if mibBuilder.loadTexts:
    axsOspfIfStateChange.setStatus(
        ""
    )

axsStaticGatewayStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 2, 0, 1)
)
axsStaticGatewayStateChange.setObjects(
      *(("AX4630S", "axsStaticGatewayAddr"),
        ("AX4630S", "axsStaticGatewayState"))
)
if mibBuilder.loadTexts:
    axsStaticGatewayStateChange.setStatus(
        ""
    )

axsStaticIpv6GatewayStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 2, 0, 2)
)
axsStaticIpv6GatewayStateChange.setObjects(
      *(("AX4630S", "axsStaticIpv6Ifindex"),
        ("AX4630S", "axsStaticIpv6GatewayAddr"),
        ("AX4630S", "axsStaticIpv6GatewayState"))
)
if mibBuilder.loadTexts:
    axsStaticIpv6GatewayStateChange.setStatus(
        ""
    )

axsTrackObjectStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 2, 0, 1)
)
axsTrackObjectStateUp.setObjects(
      *(("AX4630S", "axsTrackObjectId"),
        ("AX4630S", "axsTrackObjectState"),
        ("AX4630S", "axsTrackObjectOperation"),
        ("AX4630S", "axsTrackObjectType"),
        ("AX4630S", "axsTrackObjectNetIndex"))
)
if mibBuilder.loadTexts:
    axsTrackObjectStateUp.setStatus(
        ""
    )

axsTrackObjectStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 41, 2, 0, 2)
)
axsTrackObjectStateDown.setObjects(
      *(("AX4630S", "axsTrackObjectId"),
        ("AX4630S", "axsTrackObjectState"),
        ("AX4630S", "axsTrackObjectOperation"),
        ("AX4630S", "axsTrackObjectType"),
        ("AX4630S", "axsTrackObjectNetIndex"))
)
if mibBuilder.loadTexts:
    axsTrackObjectStateDown.setStatus(
        ""
    )

axsPolicyBaseRoutingRouteChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 45, 1, 0, 1)
)
axsPolicyBaseRoutingRouteChange.setObjects(
      *(("AX4630S", "axsPolicyBaseRoutingChangeListNumber"),
        ("AX4630S", "axsPolicyBaseRoutingChangeSequenceNumber"))
)
if mibBuilder.loadTexts:
    axsPolicyBaseRoutingRouteChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX4630S",
    **{"VlanIndex": VlanIndex,
       "VlanIdOrZero": VlanIdOrZero,
       "VniIndex": VniIndex,
       "alaxala": alaxala,
       "alaxalaProductId": alaxalaProductId,
       "axSwitch": axSwitch,
       "ax4630s": ax4630s,
       "alaxalaMib": alaxalaMib,
       "axsEx": axsEx,
       "axsMib": axsMib,
       "axsStats": axsStats,
       "axsIfStats": axsIfStats,
       "axsIfStatsTable": axsIfStatsTable,
       "axsIfStatsEntry": axsIfStatsEntry,
       "axsIfStatsIndex": axsIfStatsIndex,
       "axsIfStatsName": axsIfStatsName,
       "axsIfStatsInMegaOctets": axsIfStatsInMegaOctets,
       "axsIfStatsInUcastMegaPkts": axsIfStatsInUcastMegaPkts,
       "axsIfStatsInMulticastMegaPkts": axsIfStatsInMulticastMegaPkts,
       "axsIfStatsInBroadcastMegaPkts": axsIfStatsInBroadcastMegaPkts,
       "axsIfStatsOutMegaOctets": axsIfStatsOutMegaOctets,
       "axsIfStatsOutUcastMegaPkts": axsIfStatsOutUcastMegaPkts,
       "axsIfStatsOutMulticastMegaPkts": axsIfStatsOutMulticastMegaPkts,
       "axsIfStatsOutBroadcastMegaPkts": axsIfStatsOutBroadcastMegaPkts,
       "axsIfStatsHighSpeed": axsIfStatsHighSpeed,
       "axsQoS": axsQoS,
       "axsEtherTxQoS": axsEtherTxQoS,
       "axsEtherTxQoSStatsTable": axsEtherTxQoSStatsTable,
       "axsEtherTxQoSStatsEntry": axsEtherTxQoSStatsEntry,
       "axsEtherTxQoSStatsIndex": axsEtherTxQoSStatsIndex,
       "axsEtherTxQoSStatsMaxQnum": axsEtherTxQoSStatsMaxQnum,
       "axsEtherTxQoSStatsLimitQlen": axsEtherTxQoSStatsLimitQlen,
       "axsEtherTxQoSStatsTotalOutFrames": axsEtherTxQoSStatsTotalOutFrames,
       "axsEtherTxQoSStatsTotalOutBytesHigh": axsEtherTxQoSStatsTotalOutBytesHigh,
       "axsEtherTxQoSStatsTotalOutBytesLow": axsEtherTxQoSStatsTotalOutBytesLow,
       "axsEtherTxQoSStatsTotalDiscardFrames": axsEtherTxQoSStatsTotalDiscardFrames,
       "axsEtherTxQoSStatsQueueTable": axsEtherTxQoSStatsQueueTable,
       "axsEtherTxQoSStatsQueueEntry": axsEtherTxQoSStatsQueueEntry,
       "axsEtherTxQoSStatsQueueIndex": axsEtherTxQoSStatsQueueIndex,
       "axsEtherTxQoSStatsQueueQueIndex": axsEtherTxQoSStatsQueueQueIndex,
       "axsEtherTxQoSStatsQueueQlen": axsEtherTxQoSStatsQueueQlen,
       "axsEtherTxQoSStatsQueueMaxQlen": axsEtherTxQoSStatsQueueMaxQlen,
       "axsEtherTxQoSStatsQueueDiscardFramesClass1": axsEtherTxQoSStatsQueueDiscardFramesClass1,
       "axsEtherTxQoSStatsQueueDiscardFramesClass2": axsEtherTxQoSStatsQueueDiscardFramesClass2,
       "axsEtherTxQoSStatsQueueDiscardFramesClass3": axsEtherTxQoSStatsQueueDiscardFramesClass3,
       "axsEtherTxQoSStatsQueueDiscardFramesClass4": axsEtherTxQoSStatsQueueDiscardFramesClass4,
       "axsEthShaper": axsEthShaper,
       "axsEthShaperAgQue": axsEthShaperAgQue,
       "axsToCpuQoS": axsToCpuQoS,
       "axsToCpuQoSStatsTable": axsToCpuQoSStatsTable,
       "axsToCpuQoSStatsEntry": axsToCpuQoSStatsEntry,
       "axsToCpuQoSStatsIndex": axsToCpuQoSStatsIndex,
       "axsToCpuQoSStatsMaxQnum": axsToCpuQoSStatsMaxQnum,
       "axsToCpuQoSStatsLimitQlen": axsToCpuQoSStatsLimitQlen,
       "axsToCpuQoSStatsTotalOutFrames": axsToCpuQoSStatsTotalOutFrames,
       "axsToCpuQoSStatsTotalOutBytesHigh": axsToCpuQoSStatsTotalOutBytesHigh,
       "axsToCpuQoSStatsTotalOutBytesLow": axsToCpuQoSStatsTotalOutBytesLow,
       "axsToCpuQoSStatsTotalDiscardFrames": axsToCpuQoSStatsTotalDiscardFrames,
       "axsToCpuQoSStatsQueueTable": axsToCpuQoSStatsQueueTable,
       "axsToCpuQoSStatsQueueEntry": axsToCpuQoSStatsQueueEntry,
       "axsToCpuQoSStatsQueueIndex": axsToCpuQoSStatsQueueIndex,
       "axsToCpuQoSStatsQueueQueIndex": axsToCpuQoSStatsQueueQueIndex,
       "axsToCpuQoSStatsQueueQlen": axsToCpuQoSStatsQueueQlen,
       "axsToCpuQoSStatsQueueMaxQlen": axsToCpuQoSStatsQueueMaxQlen,
       "axsToCpuQoSStatsQueueDiscardFramesClass1": axsToCpuQoSStatsQueueDiscardFramesClass1,
       "axsToCpuQoSStatsQueueDiscardFramesClass2": axsToCpuQoSStatsQueueDiscardFramesClass2,
       "axsToCpuQoSStatsQueueDiscardFramesClass3": axsToCpuQoSStatsQueueDiscardFramesClass3,
       "axsToCpuQoSStatsQueueDiscardFramesClass4": axsToCpuQoSStatsQueueDiscardFramesClass4,
       "axsDHCP": axsDHCP,
       "axsDHCPAddrValue": axsDHCPAddrValue,
       "axsDHCPFreeAddrValue": axsDHCPFreeAddrValue,
       "axsGsrp": axsGsrp,
       "axsGsrpGroupTable": axsGsrpGroupTable,
       "axsGsrpGroupEntry": axsGsrpGroupEntry,
       "axsGsrpGroupId": axsGsrpGroupId,
       "axsGsrpGroupRowStatus": axsGsrpGroupRowStatus,
       "axsGsrpMacAddress": axsGsrpMacAddress,
       "axsGsrpAdvertiseHoldTime": axsGsrpAdvertiseHoldTime,
       "axsGsrpAdvertiseInterval": axsGsrpAdvertiseInterval,
       "axsGsrpSelectionPattern": axsGsrpSelectionPattern,
       "axsGsrpLayer3Redundancy": axsGsrpLayer3Redundancy,
       "axsGsrpVlanGroupTable": axsGsrpVlanGroupTable,
       "axsGsrpVlanGroupEntry": axsGsrpVlanGroupEntry,
       "axsGsrpVlanGroupId": axsGsrpVlanGroupId,
       "axsGsrpVlanGroupRowStatus": axsGsrpVlanGroupRowStatus,
       "axsGsrpState": axsGsrpState,
       "axsGsrpPriority": axsGsrpPriority,
       "axsGsrpActivePorts": axsGsrpActivePorts,
       "axsGsrpTransitionToMasterCounts": axsGsrpTransitionToMasterCounts,
       "axsGsrpTransitionFromMasterCounts": axsGsrpTransitionFromMasterCounts,
       "axsGsrpLastTransitionTime": axsGsrpLastTransitionTime,
       "axsGsrpVirtualMacAddress": axsGsrpVirtualMacAddress,
       "axsGsrpNeighborGroupTable": axsGsrpNeighborGroupTable,
       "axsGsrpNeighborGroupEntry": axsGsrpNeighborGroupEntry,
       "axsGsrpNeighborGroupId": axsGsrpNeighborGroupId,
       "axsGsrpNeighborMacAddress": axsGsrpNeighborMacAddress,
       "axsGsrpNeighborAdvertiseHoldTime": axsGsrpNeighborAdvertiseHoldTime,
       "axsGsrpNeighborAdvertiseInterval": axsGsrpNeighborAdvertiseInterval,
       "axsGsrpNeighborSelectionPattern": axsGsrpNeighborSelectionPattern,
       "axsGsrpNeighborVlanGroupTable": axsGsrpNeighborVlanGroupTable,
       "axsGsrpNeighborVlanGroupEntry": axsGsrpNeighborVlanGroupEntry,
       "axsGsrpNeighborVlanGroupId": axsGsrpNeighborVlanGroupId,
       "axsGsrpNeighborState": axsGsrpNeighborState,
       "axsGsrpNeighborPriority": axsGsrpNeighborPriority,
       "axsGsrpNeighborActivePorts": axsGsrpNeighborActivePorts,
       "axsVlan": axsVlan,
       "axsVlanBridge": axsVlanBridge,
       "axsVlanBridgeBase": axsVlanBridgeBase,
       "axsVBBaseTable": axsVBBaseTable,
       "axsVBBaseEntry": axsVBBaseEntry,
       "axsVBBaseIndex": axsVBBaseIndex,
       "axsVBBaseBridgeAddress": axsVBBaseBridgeAddress,
       "axsVBBaseNumPorts": axsVBBaseNumPorts,
       "axsVBBaseType": axsVBBaseType,
       "axsVBBaseVlanIfIndex": axsVBBaseVlanIfIndex,
       "axsVBBaseVlanType": axsVBBaseVlanType,
       "axsVBBaseVlanID": axsVBBaseVlanID,
       "axsVBBaseAssociatedPrimaryVlan": axsVBBaseAssociatedPrimaryVlan,
       "axsVBBaseIfStatus": axsVBBaseIfStatus,
       "axsVBBaseLastChange": axsVBBaseLastChange,
       "axsVBBasePrivateVlanType": axsVBBasePrivateVlanType,
       "axsVBBasePortTable": axsVBBasePortTable,
       "axsVBBasePortEntry": axsVBBasePortEntry,
       "axsVBBasePortIndex": axsVBBasePortIndex,
       "axsVBBasePort": axsVBBasePort,
       "axsVBBasePortIfIndex": axsVBBasePortIfIndex,
       "axsVBBasePortCircuit": axsVBBasePortCircuit,
       "axsVBBasePortDelayExceededDiscards": axsVBBasePortDelayExceededDiscards,
       "axsVBBasePortMtuExceededDiscards": axsVBBasePortMtuExceededDiscards,
       "axsVBBasePortState": axsVBBasePortState,
       "axsVBBasePortTaggedState": axsVBBasePortTaggedState,
       "axsVBBasePortTranslatedTagID": axsVBBasePortTranslatedTagID,
       "axsVlanBridgeStp": axsVlanBridgeStp,
       "axsVBStpTable": axsVBStpTable,
       "axsVBStpEntry": axsVBStpEntry,
       "axsVBStpIndex": axsVBStpIndex,
       "axsVBStpProtocolSpecification": axsVBStpProtocolSpecification,
       "axsVBStpPriority": axsVBStpPriority,
       "axsVBStpTimeSinceTopologyChange": axsVBStpTimeSinceTopologyChange,
       "axsVBStpTopChanges": axsVBStpTopChanges,
       "axsVBStpDesignatedRoot": axsVBStpDesignatedRoot,
       "axsVBStpRootCost": axsVBStpRootCost,
       "axsVBStpRootPort": axsVBStpRootPort,
       "axsVBStpMaxAge": axsVBStpMaxAge,
       "axsVBStpHelloTime": axsVBStpHelloTime,
       "axsVBStpHoldTime": axsVBStpHoldTime,
       "axsVBStpForwardDelay": axsVBStpForwardDelay,
       "axsVBStpBridgeMaxAge": axsVBStpBridgeMaxAge,
       "axsVBStpBridgeHelloTime": axsVBStpBridgeHelloTime,
       "axsVBStpBridgeForwardDelay": axsVBStpBridgeForwardDelay,
       "axsVBStpPortTable": axsVBStpPortTable,
       "axsVBStpPortEntry": axsVBStpPortEntry,
       "axsVBStpPortIndex": axsVBStpPortIndex,
       "axsVBStpPort": axsVBStpPort,
       "axsVBStpPortPriority": axsVBStpPortPriority,
       "axsVBStpPortState": axsVBStpPortState,
       "axsVBStpPortEnable": axsVBStpPortEnable,
       "axsVBStpPortPathCost": axsVBStpPortPathCost,
       "axsVBStpPortDesignatedRoot": axsVBStpPortDesignatedRoot,
       "axsVBStpPortDesignatedCost": axsVBStpPortDesignatedCost,
       "axsVBStpPortDesignatedBridge": axsVBStpPortDesignatedBridge,
       "axsVBStpPortDesignatedPort": axsVBStpPortDesignatedPort,
       "axsVBStpPortForwardTransitions": axsVBStpPortForwardTransitions,
       "axsVlanBridgeTp": axsVlanBridgeTp,
       "axsVBTpTable": axsVBTpTable,
       "axsVBTpEntry": axsVBTpEntry,
       "axsVBTpIndex": axsVBTpIndex,
       "axsVBTpLearnedEntryDiscards": axsVBTpLearnedEntryDiscards,
       "axsVBTpAgingTime": axsVBTpAgingTime,
       "axsVBTpFdbTable": axsVBTpFdbTable,
       "axsVBTpFdbEntry": axsVBTpFdbEntry,
       "axsVBTpFdbIndex": axsVBTpFdbIndex,
       "axsVBTpFdbAddress": axsVBTpFdbAddress,
       "axsVBTpFdbPort": axsVBTpFdbPort,
       "axsVBTpFdbStatus": axsVBTpFdbStatus,
       "axsVBTpPortTable": axsVBTpPortTable,
       "axsVBTpPortEntry": axsVBTpPortEntry,
       "axsVBTpPortIndex": axsVBTpPortIndex,
       "axsVBTpPort": axsVBTpPort,
       "axsVBTpPortMaxInfo": axsVBTpPortMaxInfo,
       "axsVBTpPortInFrames": axsVBTpPortInFrames,
       "axsVBTpPortOutFrames": axsVBTpPortOutFrames,
       "axsVBTpPortInDiscards": axsVBTpPortInDiscards,
       "axsVlanBridgeStatic": axsVlanBridgeStatic,
       "axsVBStaticTable": axsVBStaticTable,
       "axsVBStaticEntry": axsVBStaticEntry,
       "axsVBStaticIndex": axsVBStaticIndex,
       "axsVBStaticAddress": axsVBStaticAddress,
       "axsVBStaticReceivePort": axsVBStaticReceivePort,
       "axsVBStaticAllowedToGoTo": axsVBStaticAllowedToGoTo,
       "axsVBStaticStatus": axsVBStaticStatus,
       "axsVlanBridgeMaxVlans": axsVlanBridgeMaxVlans,
       "axsVlanBridgeMaxSpans": axsVlanBridgeMaxSpans,
       "axsVlanTagTranslation": axsVlanTagTranslation,
       "axsVlanTagTranslationTable": axsVlanTagTranslationTable,
       "axsVlanTagTranslationEntry": axsVlanTagTranslationEntry,
       "axsVlanTagTranslationVlanId": axsVlanTagTranslationVlanId,
       "axsVlanTagTranslationTranslatedId": axsVlanTagTranslationTranslatedId,
       "axsVlanTagTranslationPorts": axsVlanTagTranslationPorts,
       "axsOadp": axsOadp,
       "axsOadpMIBObjects": axsOadpMIBObjects,
       "axsOadpGlobalInfo": axsOadpGlobalInfo,
       "axsOadpGlobalActive": axsOadpGlobalActive,
       "axsOadpGlobalCdpActive": axsOadpGlobalCdpActive,
       "axsOadpGlobalMessageInterval": axsOadpGlobalMessageInterval,
       "axsOadpGlobalHoldTime": axsOadpGlobalHoldTime,
       "axsOadpGlobalCacheLastChange": axsOadpGlobalCacheLastChange,
       "axsOadpGlobalName": axsOadpGlobalName,
       "axsOadpGlobalNameType": axsOadpGlobalNameType,
       "axsOadpPortInfo": axsOadpPortInfo,
       "axsOadpPortConfigTable": axsOadpPortConfigTable,
       "axsOadpPortConfigEntry": axsOadpPortConfigEntry,
       "axsOadpPortConfigIfIndex": axsOadpPortConfigIfIndex,
       "axsOadpPortConfigActive": axsOadpPortConfigActive,
       "axsOadpNeighborInfo": axsOadpNeighborInfo,
       "axsOadpNeighborTable": axsOadpNeighborTable,
       "axsOadpNeighborEntry": axsOadpNeighborEntry,
       "axsOadpIfIndex": axsOadpIfIndex,
       "axsOadpTagID": axsOadpTagID,
       "axsOadpNeighborIndex": axsOadpNeighborIndex,
       "axsOadpNeighborTagID": axsOadpNeighborTagID,
       "axsOadpNeighborVendorType": axsOadpNeighborVendorType,
       "axsOadpNeighborSNMPAgentAddressType": axsOadpNeighborSNMPAgentAddressType,
       "axsOadpNeighborSNMPAgentAddress": axsOadpNeighborSNMPAgentAddress,
       "axsOadpNeighborDescr": axsOadpNeighborDescr,
       "axsOadpNeighborDeviceID": axsOadpNeighborDeviceID,
       "axsOadpNeighborSlotPort": axsOadpNeighborSlotPort,
       "axsOadpNeighborIfIndex": axsOadpNeighborIfIndex,
       "axsOadpNeighborIfSpeed": axsOadpNeighborIfSpeed,
       "axsOadpNeighborDeviceType": axsOadpNeighborDeviceType,
       "axsOadpNeighborService": axsOadpNeighborService,
       "axsOadpNeighborVTPMgmtDomain": axsOadpNeighborVTPMgmtDomain,
       "axsOadpNeighborNativeVLAN": axsOadpNeighborNativeVLAN,
       "axsOadpNeighborDuplex": axsOadpNeighborDuplex,
       "axsOadpNeighborApplianceID": axsOadpNeighborApplianceID,
       "axsOadpNeighborVlanID": axsOadpNeighborVlanID,
       "axsOadpNeighborPowerConsumption": axsOadpNeighborPowerConsumption,
       "axsOadpNeighborMTU": axsOadpNeighborMTU,
       "axsOadpNeighborSysName": axsOadpNeighborSysName,
       "axsOadpNeighborSysObjectID": axsOadpNeighborSysObjectID,
       "axsOadpNeighborSecondarySNMPAgentAddressType": axsOadpNeighborSecondarySNMPAgentAddressType,
       "axsOadpNeighborSecondarySNMPAgentAddress": axsOadpNeighborSecondarySNMPAgentAddress,
       "axsOadpNeighborPhysLocation": axsOadpNeighborPhysLocation,
       "axsOadpNeighborCacheLastChange": axsOadpNeighborCacheLastChange,
       "axsOadpNeighborIfHighSpeed": axsOadpNeighborIfHighSpeed,
       "axsOadpMIBNotifications": axsOadpMIBNotifications,
       "axsOadpNeighborCachelastChangeTrap": axsOadpNeighborCachelastChangeTrap,
       "axsFlow": axsFlow,
       "axsAccessFilterStats": axsAccessFilterStats,
       "axsAccessFilterStatsInTable": axsAccessFilterStatsInTable,
       "axsAccessFilterStatsInEntry": axsAccessFilterStatsInEntry,
       "axsAccessFilterStatsInifIndex": axsAccessFilterStatsInifIndex,
       "axsAccessFilterStatsInifIndexType": axsAccessFilterStatsInifIndexType,
       "axsAccessFilterStatsInListIndex": axsAccessFilterStatsInListIndex,
       "axsAccessFilterStatsInSequenceNumber": axsAccessFilterStatsInSequenceNumber,
       "axsAccessFilterStatsInListName": axsAccessFilterStatsInListName,
       "axsAccessFilterStatsInMatchedPackets": axsAccessFilterStatsInMatchedPackets,
       "axsAccessFilterStatsOutTable": axsAccessFilterStatsOutTable,
       "axsAccessFilterStatsOutEntry": axsAccessFilterStatsOutEntry,
       "axsAccessFilterStatsOutifIndex": axsAccessFilterStatsOutifIndex,
       "axsAccessFilterStatsOutifIndexType": axsAccessFilterStatsOutifIndexType,
       "axsAccessFilterStatsOutListIndex": axsAccessFilterStatsOutListIndex,
       "axsAccessFilterStatsOutSequenceNumber": axsAccessFilterStatsOutSequenceNumber,
       "axsAccessFilterStatsOutListName": axsAccessFilterStatsOutListName,
       "axsAccessFilterStatsOutMatchedPackets": axsAccessFilterStatsOutMatchedPackets,
       "axsAccessFilterStatsInMirrorTable": axsAccessFilterStatsInMirrorTable,
       "axsAccessFilterStatsInMirrorEntry": axsAccessFilterStatsInMirrorEntry,
       "axsAccessFilterStatsInMirrorifIndex": axsAccessFilterStatsInMirrorifIndex,
       "axsAccessFilterStatsInMirrorifIndexType": axsAccessFilterStatsInMirrorifIndexType,
       "axsAccessFilterStatsInMirrorListIndex": axsAccessFilterStatsInMirrorListIndex,
       "axsAccessFilterStatsInMirrorSequenceNumber": axsAccessFilterStatsInMirrorSequenceNumber,
       "axsAccessFilterStatsInMirrorListName": axsAccessFilterStatsInMirrorListName,
       "axsAccessFilterStatsInMirrorMatchedPackets": axsAccessFilterStatsInMirrorMatchedPackets,
       "axsQosFlowStats": axsQosFlowStats,
       "axsQosFlowStatsInTable": axsQosFlowStatsInTable,
       "axsQosFlowStatsInEntry": axsQosFlowStatsInEntry,
       "axsQosFlowStatsInifIndex": axsQosFlowStatsInifIndex,
       "axsQosFlowStatsInifIndexType": axsQosFlowStatsInifIndexType,
       "axsQosFlowStatsInListIndex": axsQosFlowStatsInListIndex,
       "axsQosFlowStatsInSequenceNumber": axsQosFlowStatsInSequenceNumber,
       "axsQosFlowStatsInListName": axsQosFlowStatsInListName,
       "axsQosFlowStatsInMatchedPackets": axsQosFlowStatsInMatchedPackets,
       "axsQosFlowStatsInMatchedPacketsMinUnder": axsQosFlowStatsInMatchedPacketsMinUnder,
       "axsQosFlowStatsInMatchedPacketsMinOver": axsQosFlowStatsInMatchedPacketsMinOver,
       "axsQosFlowStatsInMatchedPacketsMaxUnder": axsQosFlowStatsInMatchedPacketsMaxUnder,
       "axsQosFlowStatsInMatchedPacketsMaxOver": axsQosFlowStatsInMatchedPacketsMaxOver,
       "axsL2ld": axsL2ld,
       "axsL2ldGlobalInfo": axsL2ldGlobalInfo,
       "axsL2ldVersion": axsL2ldVersion,
       "axsL2ldLoopDetectionId": axsL2ldLoopDetectionId,
       "axsL2ldIntervalTime": axsL2ldIntervalTime,
       "axsL2ldOutputRate": axsL2ldOutputRate,
       "axsL2ldThreshold": axsL2ldThreshold,
       "axsL2ldHoldTime": axsL2ldHoldTime,
       "axsL2ldAutoRestoreTime": axsL2ldAutoRestoreTime,
       "axsL2ldConfigurationVlanPortCounts": axsL2ldConfigurationVlanPortCounts,
       "axsL2ldCapacityVlanPortCounts": axsL2ldCapacityVlanPortCounts,
       "axsL2ldPortTable": axsL2ldPortTable,
       "axsL2ldPortEntry": axsL2ldPortEntry,
       "axsL2ldPortIndex": axsL2ldPortIndex,
       "axsL2ldPortIfIndex": axsL2ldPortIfIndex,
       "axsL2ldPortStatus": axsL2ldPortStatus,
       "axsL2ldPortType": axsL2ldPortType,
       "axsL2ldPortDetectCount": axsL2ldPortDetectCount,
       "axsL2ldPortAutoRestoringTimer": axsL2ldPortAutoRestoringTimer,
       "axsL2ldPortSourcePortIfindex": axsL2ldPortSourcePortIfindex,
       "axsL2ldPortDestinationPortIfindex": axsL2ldPortDestinationPortIfindex,
       "axsL2ldPortSourceVlan": axsL2ldPortSourceVlan,
       "axsL2ldPortHCInFrames": axsL2ldPortHCInFrames,
       "axsL2ldPortHCOutFrames": axsL2ldPortHCOutFrames,
       "axsL2ldPortHCInDiscards": axsL2ldPortHCInDiscards,
       "axsL2ldPortInactiveCount": axsL2ldPortInactiveCount,
       "axsL2ldPortLastInactiveTime": axsL2ldPortLastInactiveTime,
       "axsL2ldPortLastInFramesTime": axsL2ldPortLastInFramesTime,
       "axsVrf": axsVrf,
       "axsVrfIp": axsVrfIp,
       "axsVrfIpAddrTable": axsVrfIpAddrTable,
       "axsVrfIpAddrEntry": axsVrfIpAddrEntry,
       "axsVrfIpAddrVrfIndex": axsVrfIpAddrVrfIndex,
       "axsVrfIpAdEntAddr": axsVrfIpAdEntAddr,
       "axsVrfIpAdEntIfIndex": axsVrfIpAdEntIfIndex,
       "axsVrfIpAdEntNetMask": axsVrfIpAdEntNetMask,
       "axsVrfIpAdEntBcastAddr": axsVrfIpAdEntBcastAddr,
       "axsVrfIpAdEntReasmMaxSize": axsVrfIpAdEntReasmMaxSize,
       "axsVrfIpAdEntDescr": axsVrfIpAdEntDescr,
       "axsVrfIpNetToMediaTable": axsVrfIpNetToMediaTable,
       "axsVrfIpNetToMediaEntry": axsVrfIpNetToMediaEntry,
       "axsVrfIpNetMediaVrfIndex": axsVrfIpNetMediaVrfIndex,
       "axsVrfIpNetToMediaIfIndex": axsVrfIpNetToMediaIfIndex,
       "axsVrfIpNetToMediaPhysAddress": axsVrfIpNetToMediaPhysAddress,
       "axsVrfIpNetToMediaNetAddress": axsVrfIpNetToMediaNetAddress,
       "axsVrfIpNetToMediaType": axsVrfIpNetToMediaType,
       "axsVrfIpNetToMediaDescr": axsVrfIpNetToMediaDescr,
       "axsVrfIpForward": axsVrfIpForward,
       "axsVrfIpFwNoTable": axsVrfIpFwNoTable,
       "axsVrfIpFwNoEntry": axsVrfIpFwNoEntry,
       "axsVrfIpFwNoVRFIndex": axsVrfIpFwNoVRFIndex,
       "axsVrfIpFwNo": axsVrfIpFwNo,
       "axsVrfIpFwNoDescr": axsVrfIpFwNoDescr,
       "axsVrfIpFwTable": axsVrfIpFwTable,
       "axsVrfIpFwEntry": axsVrfIpFwEntry,
       "axsVrfIpFwVRFIndex": axsVrfIpFwVRFIndex,
       "axsVrfIpFwDest": axsVrfIpFwDest,
       "axsVrfIpFwMask": axsVrfIpFwMask,
       "axsVrfIpFwPolicy": axsVrfIpFwPolicy,
       "axsVrfIpFwNextHop": axsVrfIpFwNextHop,
       "axsVrfIpFwIfIndex": axsVrfIpFwIfIndex,
       "axsVrfIpFwType": axsVrfIpFwType,
       "axsVrfIpFwProto": axsVrfIpFwProto,
       "axsVrfIpFwAge": axsVrfIpFwAge,
       "axsVrfIpFwInfo": axsVrfIpFwInfo,
       "axsVrfIpFwNextHopAS": axsVrfIpFwNextHopAS,
       "axsVrfIpFwMetric1": axsVrfIpFwMetric1,
       "axsVrfIpFwMetric2": axsVrfIpFwMetric2,
       "axsVrfIpFwMetric3": axsVrfIpFwMetric3,
       "axsVrfIpFwMetric4": axsVrfIpFwMetric4,
       "axsVrfIpFwMetric5": axsVrfIpFwMetric5,
       "axsVrfIpFwDescr": axsVrfIpFwDescr,
       "axsVrfIpv6": axsVrfIpv6,
       "axsVrfIpv6AddrTable": axsVrfIpv6AddrTable,
       "axsVrfIpv6AddrEntry": axsVrfIpv6AddrEntry,
       "axsVrfIpv6AddrVrfIndex": axsVrfIpv6AddrVrfIndex,
       "axsVrfIpv6AddrIfIndex": axsVrfIpv6AddrIfIndex,
       "axsVrfIpv6AddrAddress": axsVrfIpv6AddrAddress,
       "axsVrfIpv6AddrPfxLength": axsVrfIpv6AddrPfxLength,
       "axsVrfIpv6AddrType": axsVrfIpv6AddrType,
       "axsVrfIpv6AddrAnycastFlag": axsVrfIpv6AddrAnycastFlag,
       "axsVrfIpv6AddrStatus": axsVrfIpv6AddrStatus,
       "axsVrfIpv6AddrDescr": axsVrfIpv6AddrDescr,
       "axsVrfIpv6AddrPrefixTable": axsVrfIpv6AddrPrefixTable,
       "axsVrfIpv6AddrPrefixEntry": axsVrfIpv6AddrPrefixEntry,
       "axsVrfIpv6AddrPrefixVrfIndex": axsVrfIpv6AddrPrefixVrfIndex,
       "axsVrfIpv6AddrPrefixIfIndex": axsVrfIpv6AddrPrefixIfIndex,
       "axsVrfIpv6AddrPrefix": axsVrfIpv6AddrPrefix,
       "axsVrfIpv6AddrPrefixLength": axsVrfIpv6AddrPrefixLength,
       "axsVrfIpv6AddrPrefixOnLinkFlag": axsVrfIpv6AddrPrefixOnLinkFlag,
       "axsVrfIpv6AddrPrefixAutonomousFlag": axsVrfIpv6AddrPrefixAutonomousFlag,
       "axsVrfIpv6AddrPrefixAdvPreferredLifetime": axsVrfIpv6AddrPrefixAdvPreferredLifetime,
       "axsVrfIpv6AddrPrefixAdvValidLifetime": axsVrfIpv6AddrPrefixAdvValidLifetime,
       "axsVrfIpv6NetToMediaTable": axsVrfIpv6NetToMediaTable,
       "axsVrfIpv6NetToMediaEntry": axsVrfIpv6NetToMediaEntry,
       "axsVrfIpv6NetToMediaVrfIndex": axsVrfIpv6NetToMediaVrfIndex,
       "axsVrfIpv6NetToMediaIfIndex": axsVrfIpv6NetToMediaIfIndex,
       "axsVrfIpv6NetToMediaNetAddress": axsVrfIpv6NetToMediaNetAddress,
       "axsVrfIpv6NetToMediaPhysAddress": axsVrfIpv6NetToMediaPhysAddress,
       "axsVrfIpv6NetToMediaType": axsVrfIpv6NetToMediaType,
       "axsVrfIpv6IfNetToMediaState": axsVrfIpv6IfNetToMediaState,
       "axsVrfIpv6IfNetToMediaLastUpdated": axsVrfIpv6IfNetToMediaLastUpdated,
       "axsVrfIpv6NetToMediaValid": axsVrfIpv6NetToMediaValid,
       "axsVrfIpv6NetToMediaDescr": axsVrfIpv6NetToMediaDescr,
       "axsVrfIpv6Forward": axsVrfIpv6Forward,
       "axsVrfIpv6FwNoTable": axsVrfIpv6FwNoTable,
       "axsVrfIpv6FwNoEntry": axsVrfIpv6FwNoEntry,
       "axsVrfIpv6FwNoVRFIndex": axsVrfIpv6FwNoVRFIndex,
       "axsVrfIpv6FwNo": axsVrfIpv6FwNo,
       "axsVrfIpv6FwNoDescr": axsVrfIpv6FwNoDescr,
       "axsVrfIpv6FwTable": axsVrfIpv6FwTable,
       "axsVrfIpv6FwEntry": axsVrfIpv6FwEntry,
       "axsVrfIpv6FwVrfIndex": axsVrfIpv6FwVrfIndex,
       "axsVrfIpv6FwDest": axsVrfIpv6FwDest,
       "axsVrfIpv6FwPfxLength": axsVrfIpv6FwPfxLength,
       "axsVrfIpv6FwPolicy": axsVrfIpv6FwPolicy,
       "axsVrfIpv6FwNextHop": axsVrfIpv6FwNextHop,
       "axsVrfIpv6FwIfIndex": axsVrfIpv6FwIfIndex,
       "axsVrfIpv6FwType": axsVrfIpv6FwType,
       "axsVrfIpv6FwProto": axsVrfIpv6FwProto,
       "axsVrfIpv6FwAge": axsVrfIpv6FwAge,
       "axsVrfIpv6FwInfo": axsVrfIpv6FwInfo,
       "axsVrfIpv6FwNextHopAS": axsVrfIpv6FwNextHopAS,
       "axsVrfIpv6FwMetric1": axsVrfIpv6FwMetric1,
       "axsVrfIpv6FwMetric2": axsVrfIpv6FwMetric2,
       "axsVrfIpv6FwMetric3": axsVrfIpv6FwMetric3,
       "axsVrfIpv6FwMetric4": axsVrfIpv6FwMetric4,
       "axsVrfIpv6FwMetric5": axsVrfIpv6FwMetric5,
       "axsVrfIpv6FwDescr": axsVrfIpv6FwDescr,
       "axsOspf": axsOspf,
       "axsOspfGeneralTable": axsOspfGeneralTable,
       "axsOspfGeneralEntry": axsOspfGeneralEntry,
       "axsOspfGeneralDomainNumber": axsOspfGeneralDomainNumber,
       "axsOspfRouterId": axsOspfRouterId,
       "axsOspfAdminStat": axsOspfAdminStat,
       "axsOspfVersionNumber": axsOspfVersionNumber,
       "axsOspfAreaBdrRtrStatus": axsOspfAreaBdrRtrStatus,
       "axsOspfASBdrRtrStatus": axsOspfASBdrRtrStatus,
       "axsOspfExternLsaCount": axsOspfExternLsaCount,
       "axsOspfExternLsaCksumSum": axsOspfExternLsaCksumSum,
       "axsOspfTOSSupport": axsOspfTOSSupport,
       "axsOspfOriginateNewLsas": axsOspfOriginateNewLsas,
       "axsOspfRxNewLsas": axsOspfRxNewLsas,
       "axsOspfExtLsdbLimit": axsOspfExtLsdbLimit,
       "axsOspfMulticastExtensions": axsOspfMulticastExtensions,
       "axsOspfAreaTable": axsOspfAreaTable,
       "axsOspfAreaEntry": axsOspfAreaEntry,
       "axsOspfAreaDomainNumber": axsOspfAreaDomainNumber,
       "axsOspfAreaId": axsOspfAreaId,
       "axsOspfAuthType": axsOspfAuthType,
       "axsOspfImportAsExtern": axsOspfImportAsExtern,
       "axsOspfSpfRuns": axsOspfSpfRuns,
       "axsOspfAreaBdrRtrCount": axsOspfAreaBdrRtrCount,
       "axsOspfAsBdrRtrCount": axsOspfAsBdrRtrCount,
       "axsOspfAreaLsaCount": axsOspfAreaLsaCount,
       "axsOspfAreaLsaCksumSum": axsOspfAreaLsaCksumSum,
       "axsOspfAreaSummary": axsOspfAreaSummary,
       "axsOspfAreaStatus": axsOspfAreaStatus,
       "axsOspfStubAreaTable": axsOspfStubAreaTable,
       "axsOspfStubAreaEntry": axsOspfStubAreaEntry,
       "axsOspfStubDomainNumber": axsOspfStubDomainNumber,
       "axsOspfStubAreaId": axsOspfStubAreaId,
       "axsOspfStubTOS": axsOspfStubTOS,
       "axsOspfStubMetric": axsOspfStubMetric,
       "axsOspfStubStatus": axsOspfStubStatus,
       "axsOspfStubMetricType": axsOspfStubMetricType,
       "axsOspfLsdbTable": axsOspfLsdbTable,
       "axsOspfLsdbEntry": axsOspfLsdbEntry,
       "axsOspfLsdbDomainNumber": axsOspfLsdbDomainNumber,
       "axsOspfLsdbAreaId": axsOspfLsdbAreaId,
       "axsOspfLsdbType": axsOspfLsdbType,
       "axsOspfLsdbLsid": axsOspfLsdbLsid,
       "axsOspfLsdbRouterId": axsOspfLsdbRouterId,
       "axsOspfLsdbSequence": axsOspfLsdbSequence,
       "axsOspfLsdbAge": axsOspfLsdbAge,
       "axsOspfLsdbChecksum": axsOspfLsdbChecksum,
       "axsOspfLsdbAdvertisement": axsOspfLsdbAdvertisement,
       "axsOspfAreaRangeTable": axsOspfAreaRangeTable,
       "axsOspfAreaRangeEntry": axsOspfAreaRangeEntry,
       "axsOspfAreaRangeDomainNumber": axsOspfAreaRangeDomainNumber,
       "axsOspfAreaRangeAreaId": axsOspfAreaRangeAreaId,
       "axsOspfAreaRangeNet": axsOspfAreaRangeNet,
       "axsOspfAreaRangeMask": axsOspfAreaRangeMask,
       "axsOspfAreaRangeStatus": axsOspfAreaRangeStatus,
       "axsOspfAreaRangeEffect": axsOspfAreaRangeEffect,
       "axsOspfIfTable": axsOspfIfTable,
       "axsOspfIfEntry": axsOspfIfEntry,
       "axsOspfIfDomainNumber": axsOspfIfDomainNumber,
       "axsOspfIfIpAddress": axsOspfIfIpAddress,
       "axsOspfAddressLessIf": axsOspfAddressLessIf,
       "axsOspfIfAreaId": axsOspfIfAreaId,
       "axsOspfIfType": axsOspfIfType,
       "axsOspfIfAdminStat": axsOspfIfAdminStat,
       "axsOspfIfRtrPriority": axsOspfIfRtrPriority,
       "axsOspfIfTransitDelay": axsOspfIfTransitDelay,
       "axsOspfIfRetransInterval": axsOspfIfRetransInterval,
       "axsOspfIfHelloInterval": axsOspfIfHelloInterval,
       "axsOspfIfRtrDeadInterval": axsOspfIfRtrDeadInterval,
       "axsOspfIfPollInterval": axsOspfIfPollInterval,
       "axsOspfIfState": axsOspfIfState,
       "axsOspfIfDesignatedRouter": axsOspfIfDesignatedRouter,
       "axsOspfIfBackupDesignatedRouter": axsOspfIfBackupDesignatedRouter,
       "axsOspfIfEvents": axsOspfIfEvents,
       "axsOspfIfAuthKey": axsOspfIfAuthKey,
       "axsOspfIfStatus": axsOspfIfStatus,
       "axsOspfIfMulticastForwarding": axsOspfIfMulticastForwarding,
       "axsOspfIfMetricTable": axsOspfIfMetricTable,
       "axsOspfIfMetricEntry": axsOspfIfMetricEntry,
       "axsOspfIfMetricDomainNumber": axsOspfIfMetricDomainNumber,
       "axsOspfIfMetricIpAddress": axsOspfIfMetricIpAddress,
       "axsOspfIfMetricAddressLessIf": axsOspfIfMetricAddressLessIf,
       "axsOspfIfMetricTOS": axsOspfIfMetricTOS,
       "axsOspfIfMetricValue": axsOspfIfMetricValue,
       "axsOspfIfMetricStatus": axsOspfIfMetricStatus,
       "axsOspfVirtIfTable": axsOspfVirtIfTable,
       "axsOspfVirtIfEntry": axsOspfVirtIfEntry,
       "axsOspfVirtIfDomainNumber": axsOspfVirtIfDomainNumber,
       "axsOspfVirtIfAreaId": axsOspfVirtIfAreaId,
       "axsOspfVirtIfNeighbor": axsOspfVirtIfNeighbor,
       "axsOspfVirtIfTransitDelay": axsOspfVirtIfTransitDelay,
       "axsOspfVirtIfRetransInterval": axsOspfVirtIfRetransInterval,
       "axsOspfVirtIfHelloInterval": axsOspfVirtIfHelloInterval,
       "axsOspfVirtIfRtrDeadInterval": axsOspfVirtIfRtrDeadInterval,
       "axsOspfVirtIfState": axsOspfVirtIfState,
       "axsOspfVirtIfEvents": axsOspfVirtIfEvents,
       "axsOspfVirtIfAuthKey": axsOspfVirtIfAuthKey,
       "axsOspfVirtIfStatus": axsOspfVirtIfStatus,
       "axsOspfNbrTable": axsOspfNbrTable,
       "axsOspfNbrEntry": axsOspfNbrEntry,
       "axsOspfNbrDomainNumber": axsOspfNbrDomainNumber,
       "axsOspfNbrIpAddr": axsOspfNbrIpAddr,
       "axsOspfNbrAddressLessIndex": axsOspfNbrAddressLessIndex,
       "axsOspfNbrRtrId": axsOspfNbrRtrId,
       "axsOspfNbrOptions": axsOspfNbrOptions,
       "axsOspfNbrPriority": axsOspfNbrPriority,
       "axsOspfNbrState": axsOspfNbrState,
       "axsOspfNbrEvents": axsOspfNbrEvents,
       "axsOspfNbrLsRetransQLen": axsOspfNbrLsRetransQLen,
       "axsOspfNbmaNbrStatus": axsOspfNbmaNbrStatus,
       "axsOspfNbmaNbrPermanence": axsOspfNbmaNbrPermanence,
       "axsOspfVirtNbrTable": axsOspfVirtNbrTable,
       "axsOspfVirtNbrEntry": axsOspfVirtNbrEntry,
       "axsOspfVirtNbrDomainNumber": axsOspfVirtNbrDomainNumber,
       "axsOspfVirtNbrArea": axsOspfVirtNbrArea,
       "axsOspfVirtNbrRtrId": axsOspfVirtNbrRtrId,
       "axsOspfVirtNbrIpAddr": axsOspfVirtNbrIpAddr,
       "axsOspfVirtNbrOptions": axsOspfVirtNbrOptions,
       "axsOspfVirtNbrState": axsOspfVirtNbrState,
       "axsOspfVirtNbrEvents": axsOspfVirtNbrEvents,
       "axsOspfVirtNbrLsRetransQLen": axsOspfVirtNbrLsRetransQLen,
       "axsOspfExtLsdbTable": axsOspfExtLsdbTable,
       "axsOspfExtLsdbEntry": axsOspfExtLsdbEntry,
       "axsOspfExtLsdbDomainNumber": axsOspfExtLsdbDomainNumber,
       "axsOspfExtLsdbType": axsOspfExtLsdbType,
       "axsOspfExtLsdbLsid": axsOspfExtLsdbLsid,
       "axsOspfExtLsdbRouterId": axsOspfExtLsdbRouterId,
       "axsOspfExtLsdbSequence": axsOspfExtLsdbSequence,
       "axsOspfExtLsdbAge": axsOspfExtLsdbAge,
       "axsOspfExtLsdbChecksum": axsOspfExtLsdbChecksum,
       "axsOspfExtLsdbAdvertisement": axsOspfExtLsdbAdvertisement,
       "axsOspfAreaAggregateTable": axsOspfAreaAggregateTable,
       "axsOspfAreaAggregateEntry": axsOspfAreaAggregateEntry,
       "axsOspfAreaAggregateDomainNumber": axsOspfAreaAggregateDomainNumber,
       "axsOspfAreaAggregateAreaID": axsOspfAreaAggregateAreaID,
       "axsOspfAreaAggregateLsdbType": axsOspfAreaAggregateLsdbType,
       "axsOspfAreaAggregateNet": axsOspfAreaAggregateNet,
       "axsOspfAreaAggregateMask": axsOspfAreaAggregateMask,
       "axsOspfAreaAggregateStatus": axsOspfAreaAggregateStatus,
       "axsOspfAreaAggregateEffect": axsOspfAreaAggregateEffect,
       "axsOspfTrap": axsOspfTrap,
       "axsOspfTrapControlTable": axsOspfTrapControlTable,
       "axsOspfTrapControlEntry": axsOspfTrapControlEntry,
       "axsOspfTrapDomainNumber": axsOspfTrapDomainNumber,
       "axsOspfSetTrap": axsOspfSetTrap,
       "axsOspfConfigErrorType": axsOspfConfigErrorType,
       "axsOspfPacketType": axsOspfPacketType,
       "axsOspfPacketSrc": axsOspfPacketSrc,
       "axsOspfTraps": axsOspfTraps,
       "axsOspfVirtIfStateChange": axsOspfVirtIfStateChange,
       "axsOspfNbrStateChange": axsOspfNbrStateChange,
       "axsOspfVirtNbrStateChange": axsOspfVirtNbrStateChange,
       "axsOspfIfConfigError": axsOspfIfConfigError,
       "axsOspfVirtIfConfigError": axsOspfVirtIfConfigError,
       "axsOspfIfAuthFailure": axsOspfIfAuthFailure,
       "axsOspfVirtIfAuthFailure": axsOspfVirtIfAuthFailure,
       "axsOspfIfStateChange": axsOspfIfStateChange,
       "axsOspfv3": axsOspfv3,
       "axsOspfv3GeneralTable": axsOspfv3GeneralTable,
       "axsOspfv3GeneralEntry": axsOspfv3GeneralEntry,
       "axsOspfv3GeneralDomainNumber": axsOspfv3GeneralDomainNumber,
       "axsOspfv3RouterId": axsOspfv3RouterId,
       "axsOspfv3AdminStat": axsOspfv3AdminStat,
       "axsOspfv3VersionNumber": axsOspfv3VersionNumber,
       "axsOspfv3AreaBdrRtrStatus": axsOspfv3AreaBdrRtrStatus,
       "axsOspfv3ASBdrRtrStatus": axsOspfv3ASBdrRtrStatus,
       "axsOspfv3AsScopeLsaCount": axsOspfv3AsScopeLsaCount,
       "axsOspfv3AsScopeLsaCksumSum": axsOspfv3AsScopeLsaCksumSum,
       "axsOspfv3OriginateNewLsas": axsOspfv3OriginateNewLsas,
       "axsOspfv3RxNewLsas": axsOspfv3RxNewLsas,
       "axsOspfv3ExtAreaLsdbLimit": axsOspfv3ExtAreaLsdbLimit,
       "axsOspfv3MulticastExtensions": axsOspfv3MulticastExtensions,
       "axsOspfv3DemandExtensions": axsOspfv3DemandExtensions,
       "axsOspfv3TrafficEngineeringSupport": axsOspfv3TrafficEngineeringSupport,
       "axsOspfv3AreaTable": axsOspfv3AreaTable,
       "axsOspfv3AreaEntry": axsOspfv3AreaEntry,
       "axsOspfv3AreaDomainNumber": axsOspfv3AreaDomainNumber,
       "axsOspfv3AreaId": axsOspfv3AreaId,
       "axsOspfv3ImportAsExtern": axsOspfv3ImportAsExtern,
       "axsOspfv3SpfRuns": axsOspfv3SpfRuns,
       "axsOspfv3AreaBdrRtrCount": axsOspfv3AreaBdrRtrCount,
       "axsOspfv3AsBdrRtrCount": axsOspfv3AsBdrRtrCount,
       "axsOspfv3AreaScopeLsaCount": axsOspfv3AreaScopeLsaCount,
       "axsOspfv3AreaScopeLsaCksumSum": axsOspfv3AreaScopeLsaCksumSum,
       "axsOspfv3AreaSummary": axsOspfv3AreaSummary,
       "axsOspfv3AreaStatus": axsOspfv3AreaStatus,
       "axsOspfv3StubMetric": axsOspfv3StubMetric,
       "axsOspfv3AsLsdbTable": axsOspfv3AsLsdbTable,
       "axsOspfv3AsLsdbEntry": axsOspfv3AsLsdbEntry,
       "axsOspfv3AsLsdbDomainNumber": axsOspfv3AsLsdbDomainNumber,
       "axsOspfv3AsLsdbType": axsOspfv3AsLsdbType,
       "axsOspfv3AsLsdbRouterId": axsOspfv3AsLsdbRouterId,
       "axsOspfv3AsLsdbLsid": axsOspfv3AsLsdbLsid,
       "axsOspfv3AsLsdbSequence": axsOspfv3AsLsdbSequence,
       "axsOspfv3AsLsdbAge": axsOspfv3AsLsdbAge,
       "axsOspfv3AsLsdbChecksum": axsOspfv3AsLsdbChecksum,
       "axsOspfv3AsLsdbAdvertisement": axsOspfv3AsLsdbAdvertisement,
       "axsOspfv3AreaLsdbTable": axsOspfv3AreaLsdbTable,
       "axsOspfv3AreaLsdbEntry": axsOspfv3AreaLsdbEntry,
       "axsOspfv3AreaLsdbDomainNumber": axsOspfv3AreaLsdbDomainNumber,
       "axsOspfv3AreaLsdbAreaId": axsOspfv3AreaLsdbAreaId,
       "axsOspfv3AreaLsdbType": axsOspfv3AreaLsdbType,
       "axsOspfv3AreaLsdbRouterId": axsOspfv3AreaLsdbRouterId,
       "axsOspfv3AreaLsdbLsid": axsOspfv3AreaLsdbLsid,
       "axsOspfv3AreaLsdbSequence": axsOspfv3AreaLsdbSequence,
       "axsOspfv3AreaLsdbAge": axsOspfv3AreaLsdbAge,
       "axsOspfv3AreaLsdbChecksum": axsOspfv3AreaLsdbChecksum,
       "axsOspfv3AreaLsdbAdvertisement": axsOspfv3AreaLsdbAdvertisement,
       "axsOspfv3LinkLsdbTable": axsOspfv3LinkLsdbTable,
       "axsOspfv3LinkLsdbEntry": axsOspfv3LinkLsdbEntry,
       "axsOspfv3LinkLsdbDomainNumber": axsOspfv3LinkLsdbDomainNumber,
       "axsOspfv3LinkLsdbIfIndex": axsOspfv3LinkLsdbIfIndex,
       "axsOspfv3LinkLsdbType": axsOspfv3LinkLsdbType,
       "axsOspfv3LinkLsdbRouterId": axsOspfv3LinkLsdbRouterId,
       "axsOspfv3LinkLsdbLsid": axsOspfv3LinkLsdbLsid,
       "axsOspfv3LinkLsdbSequence": axsOspfv3LinkLsdbSequence,
       "axsOspfv3LinkLsdbAge": axsOspfv3LinkLsdbAge,
       "axsOspfv3LinkLsdbChecksum": axsOspfv3LinkLsdbChecksum,
       "axsOspfv3LinkLsdbAdvertisement": axsOspfv3LinkLsdbAdvertisement,
       "axsOspfv3IfTable": axsOspfv3IfTable,
       "axsOspfv3IfEntry": axsOspfv3IfEntry,
       "axsOspfv3IfDomainNumber": axsOspfv3IfDomainNumber,
       "axsOspfv3IfIndex": axsOspfv3IfIndex,
       "axsOspfv3IfAreaId": axsOspfv3IfAreaId,
       "axsOspfv3IfType": axsOspfv3IfType,
       "axsOspfv3IfAdminStat": axsOspfv3IfAdminStat,
       "axsOspfv3IfRtrPriority": axsOspfv3IfRtrPriority,
       "axsOspfv3IfTransitDelay": axsOspfv3IfTransitDelay,
       "axsOspfv3IfRetransInterval": axsOspfv3IfRetransInterval,
       "axsOspfv3IfHelloInterval": axsOspfv3IfHelloInterval,
       "axsOspfv3IfRtrDeadInterval": axsOspfv3IfRtrDeadInterval,
       "axsOspfv3IfPollInterval": axsOspfv3IfPollInterval,
       "axsOspfv3IfState": axsOspfv3IfState,
       "axsOspfv3IfDesignatedRouter": axsOspfv3IfDesignatedRouter,
       "axsOspfv3IfBackupDesignatedRouter": axsOspfv3IfBackupDesignatedRouter,
       "axsOspfv3IfEvents": axsOspfv3IfEvents,
       "axsOspfv3IfStatus": axsOspfv3IfStatus,
       "axsOspfv3IfMulticastForwarding": axsOspfv3IfMulticastForwarding,
       "axsOspfv3IfDemand": axsOspfv3IfDemand,
       "axsOspfv3IfMetricValue": axsOspfv3IfMetricValue,
       "axsOspfv3IfLinkScopeLsaCount": axsOspfv3IfLinkScopeLsaCount,
       "axsOspfv3IfLinkLsaCksumSum": axsOspfv3IfLinkLsaCksumSum,
       "axsOspfv3IfInstId": axsOspfv3IfInstId,
       "axsOspfv3VirtIfTable": axsOspfv3VirtIfTable,
       "axsOspfv3VirtIfEntry": axsOspfv3VirtIfEntry,
       "axsOspfv3VirtIfDomainNumber": axsOspfv3VirtIfDomainNumber,
       "axsOspfv3VirtIfAreaId": axsOspfv3VirtIfAreaId,
       "axsOspfv3VirtIfNeighbor": axsOspfv3VirtIfNeighbor,
       "axsOspfv3VirtIfIndex": axsOspfv3VirtIfIndex,
       "axsOspfv3VirtIfTransitDelay": axsOspfv3VirtIfTransitDelay,
       "axsOspfv3VirtIfRetransInterval": axsOspfv3VirtIfRetransInterval,
       "axsOspfv3VirtIfHelloInterval": axsOspfv3VirtIfHelloInterval,
       "axsOspfv3VirtIfRtrDeadInterval": axsOspfv3VirtIfRtrDeadInterval,
       "axsOspfv3VirtIfState": axsOspfv3VirtIfState,
       "axsOspfv3VirtIfEvents": axsOspfv3VirtIfEvents,
       "axsOspfv3VirtIfStatus": axsOspfv3VirtIfStatus,
       "axsOspfv3VirtIfLinkScopeLsaCount": axsOspfv3VirtIfLinkScopeLsaCount,
       "axsOspfv3VirtIfLinkLsaCksumSum": axsOspfv3VirtIfLinkLsaCksumSum,
       "axsOspfv3NbrTable": axsOspfv3NbrTable,
       "axsOspfv3NbrEntry": axsOspfv3NbrEntry,
       "axsOspfv3NbrDomainNumber": axsOspfv3NbrDomainNumber,
       "axsOspfv3NbrIfIndex": axsOspfv3NbrIfIndex,
       "axsOspfv3NbrIpv6Addr": axsOspfv3NbrIpv6Addr,
       "axsOspfv3NbrRtrId": axsOspfv3NbrRtrId,
       "axsOspfv3NbrOptions": axsOspfv3NbrOptions,
       "axsOspfv3NbrPriority": axsOspfv3NbrPriority,
       "axsOspfv3NbrState": axsOspfv3NbrState,
       "axsOspfv3NbrEvents": axsOspfv3NbrEvents,
       "axsOspfv3NbrLsRetransQLen": axsOspfv3NbrLsRetransQLen,
       "axsOspfv3NbrHelloSuppressed": axsOspfv3NbrHelloSuppressed,
       "axsOspfv3NbrIfId": axsOspfv3NbrIfId,
       "axsOspfv3VirtNbrTable": axsOspfv3VirtNbrTable,
       "axsOspfv3VirtNbrEntry": axsOspfv3VirtNbrEntry,
       "axsOspfv3VirtNbrDomainNumber": axsOspfv3VirtNbrDomainNumber,
       "axsOspfv3VirtNbrArea": axsOspfv3VirtNbrArea,
       "axsOspfv3VirtNbrRtrId": axsOspfv3VirtNbrRtrId,
       "axsOspfv3VirtNbrIfIndex": axsOspfv3VirtNbrIfIndex,
       "axsOspfv3VirtNbrIpv6Addr": axsOspfv3VirtNbrIpv6Addr,
       "axsOspfv3VirtNbrOptions": axsOspfv3VirtNbrOptions,
       "axsOspfv3VirtNbrState": axsOspfv3VirtNbrState,
       "axsOspfv3VirtNbrEvents": axsOspfv3VirtNbrEvents,
       "axsOspfv3VirtNbrLsRetransQLen": axsOspfv3VirtNbrLsRetransQLen,
       "axsOspfv3VirtNbrHelloSuppressed": axsOspfv3VirtNbrHelloSuppressed,
       "axsOspfv3VirtNbrIfId": axsOspfv3VirtNbrIfId,
       "axsOspfv3AreaAggregateTable": axsOspfv3AreaAggregateTable,
       "axsOspfv3AreaAggregateEntry": axsOspfv3AreaAggregateEntry,
       "axsOspfv3AreaAggregateDomainNumber": axsOspfv3AreaAggregateDomainNumber,
       "axsOspfv3AreaAggregateAreaID": axsOspfv3AreaAggregateAreaID,
       "axsOspfv3AreaAggregateAreaLsdbType": axsOspfv3AreaAggregateAreaLsdbType,
       "axsOspfv3AreaAggregateIndex": axsOspfv3AreaAggregateIndex,
       "axsOspfv3AreaAggregatePrefix": axsOspfv3AreaAggregatePrefix,
       "axsOspfv3AreaAggregatePrefixLen": axsOspfv3AreaAggregatePrefixLen,
       "axsOspfv3AreaAggregateStatus": axsOspfv3AreaAggregateStatus,
       "axsOspfv3AreaAggregateEffect": axsOspfv3AreaAggregateEffect,
       "axsUlr": axsUlr,
       "axsUlrGlobalInfo": axsUlrGlobalInfo,
       "axsUlrID": axsUlrID,
       "axsUlrConfigurationPortCounts": axsUlrConfigurationPortCounts,
       "axsUlrStartupActivePortSelection": axsUlrStartupActivePortSelection,
       "axsUlrPortTable": axsUlrPortTable,
       "axsUlrPortEntry": axsUlrPortEntry,
       "axsUlrPortIfIndex": axsUlrPortIfIndex,
       "axsUlrPortType": axsUlrPortType,
       "axsUlrPairedPortIfIndex": axsUlrPairedPortIfIndex,
       "axsUlrPortStatus": axsUlrPortStatus,
       "axsUlrPairedPortStatus": axsUlrPairedPortStatus,
       "axsUlrAutoChangeToPrimary": axsUlrAutoChangeToPrimary,
       "axsUlrAutoChangeToPrimaryDelay": axsUlrAutoChangeToPrimaryDelay,
       "axsUlrAutoChangeToPrimaryRest": axsUlrAutoChangeToPrimaryRest,
       "axsUlrStartupActivePortSelectionStatus": axsUlrStartupActivePortSelectionStatus,
       "axsUlrFlushTransmit": axsUlrFlushTransmit,
       "axsUlrFlushVlan": axsUlrFlushVlan,
       "axsUlrMacAddressUpdateTransmit": axsUlrMacAddressUpdateTransmit,
       "axsUlrLastActivePortDecisionTime": axsUlrLastActivePortDecisionTime,
       "axsUlrLastFlushTransmitTime": axsUlrLastFlushTransmitTime,
       "axsUlrLastMacUpdateTransmitTime": axsUlrLastMacUpdateTransmitTime,
       "axsUlrLastChangeFactor": axsUlrLastChangeFactor,
       "axsUlrFlushTransmitTotalPackets": axsUlrFlushTransmitTotalPackets,
       "axsUlrMacAddressUpdateTransmitTotalPackets": axsUlrMacAddressUpdateTransmitTotalPackets,
       "axsUlrMacAddressUpdateTransmitOverFlow": axsUlrMacAddressUpdateTransmitOverFlow,
       "axsUlrActiveDecisionCount": axsUlrActiveDecisionCount,
       "axsStatic": axsStatic,
       "axsStaticTable": axsStaticTable,
       "axsStaticGatewayEntry": axsStaticGatewayEntry,
       "axsStaticGatewayAddr": axsStaticGatewayAddr,
       "axsStaticGatewayState": axsStaticGatewayState,
       "axsStaticTrap": axsStaticTrap,
       "axsStaticGatewayStateChange": axsStaticGatewayStateChange,
       "axsStaticIpv6GatewayStateChange": axsStaticIpv6GatewayStateChange,
       "axsStaticIpv6Table": axsStaticIpv6Table,
       "axsStaticIpv6GatewayEntry": axsStaticIpv6GatewayEntry,
       "axsStaticIpv6Ifindex": axsStaticIpv6Ifindex,
       "axsStaticIpv6GatewayAddr": axsStaticIpv6GatewayAddr,
       "axsStaticIpv6GatewayState": axsStaticIpv6GatewayState,
       "axsTrackObject": axsTrackObject,
       "axsTrackObjectGeneralGroup": axsTrackObjectGeneralGroup,
       "axsTrackObjectGeneralLastChange": axsTrackObjectGeneralLastChange,
       "axsTrackObjectTraps": axsTrackObjectTraps,
       "axsTrackObjectStateUp": axsTrackObjectStateUp,
       "axsTrackObjectStateDown": axsTrackObjectStateDown,
       "axsTrackObjectTable": axsTrackObjectTable,
       "axsTrackObjectEntry": axsTrackObjectEntry,
       "axsTrackObjectId": axsTrackObjectId,
       "axsTrackObjectState": axsTrackObjectState,
       "axsTrackObjectOperation": axsTrackObjectOperation,
       "axsTrackObjectType": axsTrackObjectType,
       "axsTrackObjectNetIndex": axsTrackObjectNetIndex,
       "axsPolicyBase": axsPolicyBase,
       "axsPolicyBaseRouting": axsPolicyBaseRouting,
       "axsPolicyBaseRoutingRouteChange": axsPolicyBaseRoutingRouteChange,
       "axsPolicyBaseRoutingChangeListNumber": axsPolicyBaseRoutingChangeListNumber,
       "axsPolicyBaseRoutingChangeSequenceNumber": axsPolicyBaseRoutingChangeSequenceNumber,
       "axsBootManagement": axsBootManagement,
       "axsBootReason": axsBootReason,
       "axsLogin": axsLogin,
       "axsLoginName": axsLoginName,
       "axsLoginTime": axsLoginTime,
       "axsLogoutTime": axsLogoutTime,
       "axsLoginFailureTime": axsLoginFailureTime,
       "axsLoginLocation": axsLoginLocation,
       "axsLoginLine": axsLoginLine,
       "axsLogoutStatus": axsLogoutStatus,
       "axslldp": axslldp,
       "axslldpConfiguration": axslldpConfiguration,
       "axslldpMessageTxInterval": axslldpMessageTxInterval,
       "axslldpMessageTxHoldMultiplier": axslldpMessageTxHoldMultiplier,
       "axslldpPortConfigTable": axslldpPortConfigTable,
       "axslldpPortConfigEntry": axslldpPortConfigEntry,
       "axslldpPortConfigPortNum": axslldpPortConfigPortNum,
       "axslldpPortConfigAdminStatus": axslldpPortConfigAdminStatus,
       "axslldpPortConfigTLVsTxEnable": axslldpPortConfigTLVsTxEnable,
       "axslldpPortConfigRowStatus": axslldpPortConfigRowStatus,
       "axslldpStats": axslldpStats,
       "axslldpStatsTable": axslldpStatsTable,
       "axslldpStatsEntry": axslldpStatsEntry,
       "axslldpStatsPortNum": axslldpStatsPortNum,
       "axslldpStatsOperStatus": axslldpStatsOperStatus,
       "axslldpStatsFramesInErrors": axslldpStatsFramesInErrors,
       "axslldpStatsFramesInTotal": axslldpStatsFramesInTotal,
       "axslldpStatsFramesOutTotal": axslldpStatsFramesOutTotal,
       "axslldpStatsTLVsInErrors": axslldpStatsTLVsInErrors,
       "axslldpStatsTLVsDiscardedTotal": axslldpStatsTLVsDiscardedTotal,
       "axslldpLocalSystemData": axslldpLocalSystemData,
       "axslldpLocChassisType": axslldpLocChassisType,
       "axslldpLocChassisId": axslldpLocChassisId,
       "axslldpLocSysName": axslldpLocSysName,
       "axslldpLocSysDesc": axslldpLocSysDesc,
       "axslldpLocPortTable": axslldpLocPortTable,
       "axslldpLocPortEntry": axslldpLocPortEntry,
       "axslldpLocPortNum": axslldpLocPortNum,
       "axslldpLocPortType": axslldpLocPortType,
       "axslldpLocPortId": axslldpLocPortId,
       "axslldpLocPortDesc": axslldpLocPortDesc,
       "axslldpRemoteSystemData": axslldpRemoteSystemData,
       "axslldpRemTable": axslldpRemTable,
       "axslldpRemEntry": axslldpRemEntry,
       "axslldpRemLocalPortNum": axslldpRemLocalPortNum,
       "axslldpRemIndex": axslldpRemIndex,
       "axslldpRemRemoteChassisType": axslldpRemRemoteChassisType,
       "axslldpRemRemoteChassis": axslldpRemRemoteChassis,
       "axslldpRemRemotePortType": axslldpRemRemotePortType,
       "axslldpRemRemotePort": axslldpRemRemotePort,
       "axslldpRemPortDesc": axslldpRemPortDesc,
       "axslldpRemSysName": axslldpRemSysName,
       "axslldpRemSysDesc": axslldpRemSysDesc,
       "axslldpRemoteOriginInfoData": axslldpRemoteOriginInfoData,
       "axslldpRemOriginInfoTable": axslldpRemOriginInfoTable,
       "axslldpRemOriginInfoEntry": axslldpRemOriginInfoEntry,
       "axslldpRemOriginInfoPortNum": axslldpRemOriginInfoPortNum,
       "axslldpRemOriginInfoIndex": axslldpRemOriginInfoIndex,
       "axslldpRemOriginInfoLowerVlanList": axslldpRemOriginInfoLowerVlanList,
       "axslldpRemOriginInfoHigherVlanList": axslldpRemOriginInfoHigherVlanList,
       "axslldpRemOriginInfoIPv4Address": axslldpRemOriginInfoIPv4Address,
       "axslldpRemOriginInfoIPv4PortType": axslldpRemOriginInfoIPv4PortType,
       "axslldpRemOriginInfoIPv4VlanId": axslldpRemOriginInfoIPv4VlanId,
       "axslldpRemOriginInfoIPv6Address": axslldpRemOriginInfoIPv6Address,
       "axslldpRemOriginInfoIPv6PortType": axslldpRemOriginInfoIPv6PortType,
       "axslldpRemOriginInfoIPv6VlanId": axslldpRemOriginInfoIPv6VlanId,
       "axsAxrp": axsAxrp,
       "axsAxrpGroupTable": axsAxrpGroupTable,
       "axsAxrpGroupEntry": axsAxrpGroupEntry,
       "axsAxrpGroupRingId": axsAxrpGroupRingId,
       "axsAxrpGroupRowStatus": axsAxrpGroupRowStatus,
       "axsAxrpGroupMode": axsAxrpGroupMode,
       "axsAxrpGroupRingAttribute": axsAxrpGroupRingAttribute,
       "axsAxrpGroupMonitoringState": axsAxrpGroupMonitoringState,
       "axsAxrpGroupRingport1": axsAxrpGroupRingport1,
       "axsAxrpGroupRingport1Shared": axsAxrpGroupRingport1Shared,
       "axsAxrpGroupRingport2": axsAxrpGroupRingport2,
       "axsAxrpGroupRingport2Shared": axsAxrpGroupRingport2Shared,
       "axsAxrpGroupTransitionToFaultCounts": axsAxrpGroupTransitionToFaultCounts,
       "axsAxrpGroupTransitionToNormalCounts": axsAxrpGroupTransitionToNormalCounts,
       "axsAxrpGroupLastTransitionTime": axsAxrpGroupLastTransitionTime,
       "axsAxrpGroupLinkStatusAlert": axsAxrpGroupLinkStatusAlert,
       "axsAxrpGroupRingport1LinkKeepaliveSend": axsAxrpGroupRingport1LinkKeepaliveSend,
       "axsAxrpGroupRingport1LinkKeepaliveMonitor": axsAxrpGroupRingport1LinkKeepaliveMonitor,
       "axsAxrpGroupRingport1LinkState": axsAxrpGroupRingport1LinkState,
       "axsAxrpGroupRingport1LinkKeepaliveReceiveCounts": axsAxrpGroupRingport1LinkKeepaliveReceiveCounts,
       "axsAxrpGroupRingport2LinkKeepaliveSend": axsAxrpGroupRingport2LinkKeepaliveSend,
       "axsAxrpGroupRingport2LinkKeepaliveMonitor": axsAxrpGroupRingport2LinkKeepaliveMonitor,
       "axsAxrpGroupRingport2LinkState": axsAxrpGroupRingport2LinkState,
       "axsAxrpGroupRingport2LinkKeepaliveReceiveCounts": axsAxrpGroupRingport2LinkKeepaliveReceiveCounts,
       "axsAxrpGroupMultiFaultDetectionState": axsAxrpGroupMultiFaultDetectionState,
       "axsAxrpVlanGroupTable": axsAxrpVlanGroupTable,
       "axsAxrpVlanGroupEntry": axsAxrpVlanGroupEntry,
       "axsAxrpVlanGroupRingId": axsAxrpVlanGroupRingId,
       "axsAxrpVlanGroupId": axsAxrpVlanGroupId,
       "axsAxrpVlanGroupRingport1": axsAxrpVlanGroupRingport1,
       "axsAxrpVlanGroupRingport1Role": axsAxrpVlanGroupRingport1Role,
       "axsAxrpVlanGroupRingport1OperState": axsAxrpVlanGroupRingport1OperState,
       "axsAxrpVlanGroupRingport2": axsAxrpVlanGroupRingport2,
       "axsAxrpVlanGroupRingport2Role": axsAxrpVlanGroupRingport2Role,
       "axsAxrpVlanGroupRingport2OperState": axsAxrpVlanGroupRingport2OperState,
       "axsPconMIB": axsPconMIB,
       "axsPconObjects": axsPconObjects,
       "axsPconModuleData": axsPconModuleData,
       "axsPconModuleTable": axsPconModuleTable,
       "axsPconModuleEntry": axsPconModuleEntry,
       "axsPconModuleIndex": axsPconModuleIndex,
       "axsPconModuleType": axsPconModuleType,
       "axsPconModuleSlotNo": axsPconModuleSlotNo,
       "axsPconModuleDescr": axsPconModuleDescr,
       "axsPconModuleStatus": axsPconModuleStatus,
       "axsPconModuleMode": axsPconModuleMode,
       "axsPconPowerCon": axsPconPowerCon,
       "axsPconPowerConTable": axsPconPowerConTable,
       "axsPconPowerConEntry": axsPconPowerConEntry,
       "axsPconPowerConMaxPower": axsPconPowerConMaxPower,
       "axsPconPowerConPowerConsumption": axsPconPowerConPowerConsumption,
       "axsPconPowerConPowerMeter": axsPconPowerConPowerMeter,
       "axsPconTraffic": axsPconTraffic,
       "axsPconTrafficTable": axsPconTrafficTable,
       "axsPconTrafficEntry": axsPconTrafficEntry,
       "axsPconTrafficMaxTransferCapacity": axsPconTrafficMaxTransferCapacity,
       "axsPconTrafficTotalTransferCapacity": axsPconTrafficTotalTransferCapacity,
       "axsPconTrafficInOctets": axsPconTrafficInOctets,
       "axsPconTrafficOutOctets": axsPconTrafficOutOctets,
       "axsPconTrafficInPkts": axsPconTrafficInPkts,
       "axsPconTrafficOutPkts": axsPconTrafficOutPkts,
       "axsPconTrafficCapacityOctets": axsPconTrafficCapacityOctets,
       "axsPconTrafficInPeakOctetsRate": axsPconTrafficInPeakOctetsRate,
       "axsPconTrafficPeakTransferCapacity": axsPconTrafficPeakTransferCapacity,
       "axsPconTrafficInDiscPkts": axsPconTrafficInDiscPkts,
       "axsVxlan": axsVxlan,
       "axsVxlanStatsVniTable": axsVxlanStatsVniTable,
       "axsVxlanStatsVniEntry": axsVxlanStatsVniEntry,
       "axsChassisIndex": axsChassisIndex,
       "axsVniIndex": axsVniIndex,
       "axsVxlanStatsVniEncapPackets": axsVxlanStatsVniEncapPackets,
       "axsVxlanStatsVniEncapOctets": axsVxlanStatsVniEncapOctets,
       "axsVxlanStatsVniDecapPackets": axsVxlanStatsVniDecapPackets,
       "axsVxlanStatsVniDecapOctets": axsVxlanStatsVniDecapOctets,
       "axsVxlanStatsVniAcsacsPackets": axsVxlanStatsVniAcsacsPackets,
       "axsVxlanStatsVniAcsacsOctets": axsVxlanStatsVniAcsacsOctets,
       "axsVxlanStatsTunnelTable": axsVxlanStatsTunnelTable,
       "axsVxlanStatsTunnelEntry": axsVxlanStatsTunnelEntry,
       "axsTunnelAddress": axsTunnelAddress,
       "axsVxlanStatsTunnelEncapPackets": axsVxlanStatsTunnelEncapPackets,
       "axsVxlanStatsTunnelEncapOctets": axsVxlanStatsTunnelEncapOctets,
       "axsVxlanStatsTunnelDecapPackets": axsVxlanStatsTunnelDecapPackets,
       "axsVxlanStatsTunnelDecapOctets": axsVxlanStatsTunnelDecapOctets,
       "ax4630sMib": ax4630sMib,
       "ax4630sSwitch": ax4630sSwitch,
       "ax4630sModelType": ax4630sModelType,
       "ax4630sSoftware": ax4630sSoftware,
       "ax4630sSoftwareName": ax4630sSoftwareName,
       "ax4630sSoftwareAbbreviation": ax4630sSoftwareAbbreviation,
       "ax4630sSoftwareVersion": ax4630sSoftwareVersion,
       "ax4630sSystemMsg": ax4630sSystemMsg,
       "ax4630sSystemMsgText": ax4630sSystemMsgText,
       "ax4630sSystemMsgType": ax4630sSystemMsgType,
       "ax4630sSystemMsgTimeStamp": ax4630sSystemMsgTimeStamp,
       "ax4630sSystemMsgLevel": ax4630sSystemMsgLevel,
       "ax4630sSystemMsgEventPoint": ax4630sSystemMsgEventPoint,
       "ax4630sSystemMsgEventInterfaceID": ax4630sSystemMsgEventInterfaceID,
       "ax4630sSystemMsgEventCode": ax4630sSystemMsgEventCode,
       "ax4630sSystemMsgAdditionalCode": ax4630sSystemMsgAdditionalCode,
       "ax4630sSnmpAgent": ax4630sSnmpAgent,
       "ax4630sSnmpSendReceiveSize": ax4630sSnmpSendReceiveSize,
       "ax4630sSnmpReceiveDelay": ax4630sSnmpReceiveDelay,
       "ax4630sSnmpContinuousSend": ax4630sSnmpContinuousSend,
       "ax4630sSnmpObjectMaxNumber": ax4630sSnmpObjectMaxNumber,
       "ax4630sLicense": ax4630sLicense,
       "ax4630sLicenseNumber": ax4630sLicenseNumber,
       "ax4630sLicenseTable": ax4630sLicenseTable,
       "ax4630sLicenseEntry": ax4630sLicenseEntry,
       "ax4630sLicenseIndex": ax4630sLicenseIndex,
       "ax4630sLicenseSerialNumber": ax4630sLicenseSerialNumber,
       "ax4630sLicenseOptionNumber": ax4630sLicenseOptionNumber,
       "ax4630sLicenseOptionTable": ax4630sLicenseOptionTable,
       "ax4630sLicenseOptionEntry": ax4630sLicenseOptionEntry,
       "ax4630sLicenseOptionIndex": ax4630sLicenseOptionIndex,
       "ax4630sLicenseOptionNumberIndex": ax4630sLicenseOptionNumberIndex,
       "ax4630sLicenseOptionSoftwareName": ax4630sLicenseOptionSoftwareName,
       "ax4630sLicenseOptionSoftwareAbbreviation": ax4630sLicenseOptionSoftwareAbbreviation,
       "ax4630sDevice": ax4630sDevice,
       "ax4630sChassis": ax4630sChassis,
       "ax4630sChassisMaxNumber": ax4630sChassisMaxNumber,
       "ax4630sChassisTable": ax4630sChassisTable,
       "ax4630sChassisEntry": ax4630sChassisEntry,
       "ax4630sChassisIndex": ax4630sChassisIndex,
       "ax4630sChassisType": ax4630sChassisType,
       "ax4630sChassisStatus": ax4630sChassisStatus,
       "ax4630sStsLedStatus": ax4630sStsLedStatus,
       "ax4630sCpuName": ax4630sCpuName,
       "ax4630sCpuClock": ax4630sCpuClock,
       "ax4630sMemoryTotalSize": ax4630sMemoryTotalSize,
       "ax4630sMemoryUsedSize": ax4630sMemoryUsedSize,
       "ax4630sMemoryFreeSize": ax4630sMemoryFreeSize,
       "ax4630sRomVersion": ax4630sRomVersion,
       "ax4630sCpuLoad1m": ax4630sCpuLoad1m,
       "ax4630sFlashTotalSize": ax4630sFlashTotalSize,
       "ax4630sFlashUsedSize": ax4630sFlashUsedSize,
       "ax4630sFlashFreeSize": ax4630sFlashFreeSize,
       "ax4630sSdCardStatus": ax4630sSdCardStatus,
       "ax4630sSdCardTotalSize": ax4630sSdCardTotalSize,
       "ax4630sSdCardUsedSize": ax4630sSdCardUsedSize,
       "ax4630sSdCardFreeSize": ax4630sSdCardFreeSize,
       "ax4630sPhysLineNumber": ax4630sPhysLineNumber,
       "ax4630sTemperatureStatusNumber": ax4630sTemperatureStatusNumber,
       "ax4630sPowerUnitNumber": ax4630sPowerUnitNumber,
       "ax4630sRedundantPsNumber": ax4630sRedundantPsNumber,
       "ax4630sFanNumber": ax4630sFanNumber,
       "ax4630sTotalAccumRunTime": ax4630sTotalAccumRunTime,
       "ax4630sCriticalAccumRunTime": ax4630sCriticalAccumRunTime,
       "ax4630sModuleSlotNumber": ax4630sModuleSlotNumber,
       "ax4630sMgmtPortStatus": ax4630sMgmtPortStatus,
       "ax4630sNifBoardNumber": ax4630sNifBoardNumber,
       "ax4630sTemperatureStatusTable": ax4630sTemperatureStatusTable,
       "ax4630sTemperatureStatusEntry": ax4630sTemperatureStatusEntry,
       "ax4630sTemperatureStatusIndex": ax4630sTemperatureStatusIndex,
       "ax4630sTemperatureStatusDescr": ax4630sTemperatureStatusDescr,
       "ax4630sTemperatureStatusValue": ax4630sTemperatureStatusValue,
       "ax4630sTemperatureThreshold": ax4630sTemperatureThreshold,
       "ax4630sTemperatureState": ax4630sTemperatureState,
       "ax4630sPowerUnitTable": ax4630sPowerUnitTable,
       "ax4630sPowerUnitEntry": ax4630sPowerUnitEntry,
       "ax4630sPowerUnitIndex": ax4630sPowerUnitIndex,
       "ax4630sPowerConnectStatus": ax4630sPowerConnectStatus,
       "ax4630sPowerSupplyStatus": ax4630sPowerSupplyStatus,
       "ax4630sPowerSlotType": ax4630sPowerSlotType,
       "ax4630sPowerFanDirection": ax4630sPowerFanDirection,
       "ax4630sFanTable": ax4630sFanTable,
       "ax4630sFanEntry": ax4630sFanEntry,
       "ax4630sFanIndex": ax4630sFanIndex,
       "ax4630sFanStatus": ax4630sFanStatus,
       "ax4630sFanDirection": ax4630sFanDirection,
       "ax4630sModuleSlotTable": ax4630sModuleSlotTable,
       "ax4630sModuleSlotEntry": ax4630sModuleSlotEntry,
       "ax4630sModuleSlotIndex": ax4630sModuleSlotIndex,
       "ax4630sModuleSlotStatus": ax4630sModuleSlotStatus,
       "ax4630sModuleSlotType": ax4630sModuleSlotType,
       "ax4630sNifBoard": ax4630sNifBoard,
       "ax4630sNifBoardTable": ax4630sNifBoardTable,
       "ax4630sNifBoardEntry": ax4630sNifBoardEntry,
       "ax4630sNifBoardSlotIndex": ax4630sNifBoardSlotIndex,
       "ax4630sNifBoardType": ax4630sNifBoardType,
       "ax4630sNifBoardOperStatus": ax4630sNifBoardOperStatus,
       "ax4630sNifBoardName": ax4630sNifBoardName,
       "ax4630sNifBoardAbbreviation": ax4630sNifBoardAbbreviation,
       "ax4630sNifPhysLineNumber": ax4630sNifPhysLineNumber,
       "ax4630sNifSerialNumber": ax4630sNifSerialNumber,
       "ax4630sPhysLine": ax4630sPhysLine,
       "ax4630sPhysLineTable": ax4630sPhysLineTable,
       "ax4630sPhysLineEntry": ax4630sPhysLineEntry,
       "ax4630sPhysLineIndex": ax4630sPhysLineIndex,
       "ax4630sPhysLineConnectorType": ax4630sPhysLineConnectorType,
       "ax4630sPhysLineOperStatus": ax4630sPhysLineOperStatus,
       "ax4630sPhysLineIfIndexNumber": ax4630sPhysLineIfIndexNumber,
       "ax4630sPhysLineTransceiverStatus": ax4630sPhysLineTransceiverStatus,
       "ax4630sInterface": ax4630sInterface,
       "ax4630sLineIfTable": ax4630sLineIfTable,
       "ax4630sLineIfEntry": ax4630sLineIfEntry,
       "ax4630sLineIfIndex": ax4630sLineIfIndex,
       "ax4630sIfIndex": ax4630sIfIndex,
       "ax4630sManagementMIB": ax4630sManagementMIB,
       "ax4630sOperationCommand": ax4630sOperationCommand,
       "ax4630sFdbClearMIB": ax4630sFdbClearMIB,
       "ax4630sFdbClearSet": ax4630sFdbClearSet,
       "ax4630sFdbClearReqTime": ax4630sFdbClearReqTime,
       "ax4630sFdbClearSuccessTime": ax4630sFdbClearSuccessTime,
       "ax4630sFdb": ax4630sFdb,
       "ax4630sFdbCounterTable": ax4630sFdbCounterTable,
       "ax4630sFdbCounterEntry": ax4630sFdbCounterEntry,
       "ax4630sFdbCounterNifIndex": ax4630sFdbCounterNifIndex,
       "ax4630sFdbCounterLineIndex": ax4630sFdbCounterLineIndex,
       "ax4630sFdbCounterCounts": ax4630sFdbCounterCounts,
       "ax4630sFdbCounterType": ax4630sFdbCounterType,
       "ax4630sFdbCounterLimits": ax4630sFdbCounterLimits}
)
