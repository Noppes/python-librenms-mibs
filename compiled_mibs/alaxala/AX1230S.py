# SNMP MIB module (AX1230S) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX1230S-MIB

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

alaxala = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839)
)


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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaxalaProductId_ObjectIdentity = ObjectIdentity
alaxalaProductId = _AlaxalaProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1)
)
_AxSwitch_ObjectIdentity = ObjectIdentity
axSwitch = _AxSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2)
)
_Ax1230s_ObjectIdentity = ObjectIdentity
ax1230s = _Ax1230s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10)
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
    axsIfStatsTable.setStatus("current")
_AxsIfStatsEntry_Object = MibTableRow
axsIfStatsEntry = _AxsIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1)
)
axsIfStatsEntry.setIndexNames(
    (0, "AX1230S", "axsIfStatsIndex"),
)
if mibBuilder.loadTexts:
    axsIfStatsEntry.setStatus("current")
_AxsIfStatsIndex_Type = Integer32
_AxsIfStatsIndex_Object = MibTableColumn
axsIfStatsIndex = _AxsIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 1),
    _AxsIfStatsIndex_Type()
)
axsIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsIfStatsIndex.setStatus("current")
_AxsIfStatsName_Type = DisplayString
_AxsIfStatsName_Object = MibTableColumn
axsIfStatsName = _AxsIfStatsName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 2),
    _AxsIfStatsName_Type()
)
axsIfStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsName.setStatus("current")
_AxsIfStatsInMegaOctets_Type = Counter32
_AxsIfStatsInMegaOctets_Object = MibTableColumn
axsIfStatsInMegaOctets = _AxsIfStatsInMegaOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 3),
    _AxsIfStatsInMegaOctets_Type()
)
axsIfStatsInMegaOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsInMegaOctets.setStatus("current")
_AxsIfStatsInUcastMegaPkts_Type = Counter32
_AxsIfStatsInUcastMegaPkts_Object = MibTableColumn
axsIfStatsInUcastMegaPkts = _AxsIfStatsInUcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 4),
    _AxsIfStatsInUcastMegaPkts_Type()
)
axsIfStatsInUcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsInUcastMegaPkts.setStatus("current")
_AxsIfStatsInMulticastMegaPkts_Type = Counter32
_AxsIfStatsInMulticastMegaPkts_Object = MibTableColumn
axsIfStatsInMulticastMegaPkts = _AxsIfStatsInMulticastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 5),
    _AxsIfStatsInMulticastMegaPkts_Type()
)
axsIfStatsInMulticastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsInMulticastMegaPkts.setStatus("current")
_AxsIfStatsInBroadcastMegaPkts_Type = Counter32
_AxsIfStatsInBroadcastMegaPkts_Object = MibTableColumn
axsIfStatsInBroadcastMegaPkts = _AxsIfStatsInBroadcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 6),
    _AxsIfStatsInBroadcastMegaPkts_Type()
)
axsIfStatsInBroadcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsInBroadcastMegaPkts.setStatus("current")
_AxsIfStatsOutMegaOctets_Type = Counter32
_AxsIfStatsOutMegaOctets_Object = MibTableColumn
axsIfStatsOutMegaOctets = _AxsIfStatsOutMegaOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 7),
    _AxsIfStatsOutMegaOctets_Type()
)
axsIfStatsOutMegaOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsOutMegaOctets.setStatus("current")
_AxsIfStatsOutUcastMegaPkts_Type = Counter32
_AxsIfStatsOutUcastMegaPkts_Object = MibTableColumn
axsIfStatsOutUcastMegaPkts = _AxsIfStatsOutUcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 8),
    _AxsIfStatsOutUcastMegaPkts_Type()
)
axsIfStatsOutUcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsOutUcastMegaPkts.setStatus("current")
_AxsIfStatsOutMulticastMegaPkts_Type = Counter32
_AxsIfStatsOutMulticastMegaPkts_Object = MibTableColumn
axsIfStatsOutMulticastMegaPkts = _AxsIfStatsOutMulticastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 9),
    _AxsIfStatsOutMulticastMegaPkts_Type()
)
axsIfStatsOutMulticastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsOutMulticastMegaPkts.setStatus("current")
_AxsIfStatsOutBroadcastMegaPkts_Type = Counter32
_AxsIfStatsOutBroadcastMegaPkts_Object = MibTableColumn
axsIfStatsOutBroadcastMegaPkts = _AxsIfStatsOutBroadcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 10),
    _AxsIfStatsOutBroadcastMegaPkts_Type()
)
axsIfStatsOutBroadcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsOutBroadcastMegaPkts.setStatus("current")
_AxsIfStatsHighSpeed_Type = Counter32
_AxsIfStatsHighSpeed_Object = MibTableColumn
axsIfStatsHighSpeed = _AxsIfStatsHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 4, 1, 1, 11),
    _AxsIfStatsHighSpeed_Type()
)
axsIfStatsHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsIfStatsHighSpeed.setStatus("current")
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
    axsEtherTxQoSStatsTable.setStatus("current")
_AxsEtherTxQoSStatsEntry_Object = MibTableRow
axsEtherTxQoSStatsEntry = _AxsEtherTxQoSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1)
)
axsEtherTxQoSStatsEntry.setIndexNames(
    (0, "AX1230S", "axsEtherTxQoSStatsIndex"),
)
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsEntry.setStatus("current")
_AxsEtherTxQoSStatsIndex_Type = Integer32
_AxsEtherTxQoSStatsIndex_Object = MibTableColumn
axsEtherTxQoSStatsIndex = _AxsEtherTxQoSStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 1),
    _AxsEtherTxQoSStatsIndex_Type()
)
axsEtherTxQoSStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsIndex.setStatus("current")
_AxsEtherTxQoSStatsMaxQnum_Type = Integer32
_AxsEtherTxQoSStatsMaxQnum_Object = MibTableColumn
axsEtherTxQoSStatsMaxQnum = _AxsEtherTxQoSStatsMaxQnum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 2),
    _AxsEtherTxQoSStatsMaxQnum_Type()
)
axsEtherTxQoSStatsMaxQnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsMaxQnum.setStatus("current")
_AxsEtherTxQoSStatsLimitQlen_Type = Integer32
_AxsEtherTxQoSStatsLimitQlen_Object = MibTableColumn
axsEtherTxQoSStatsLimitQlen = _AxsEtherTxQoSStatsLimitQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 3),
    _AxsEtherTxQoSStatsLimitQlen_Type()
)
axsEtherTxQoSStatsLimitQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsLimitQlen.setStatus("current")
_AxsEtherTxQoSStatsTotalOutFrames_Type = Counter32
_AxsEtherTxQoSStatsTotalOutFrames_Object = MibTableColumn
axsEtherTxQoSStatsTotalOutFrames = _AxsEtherTxQoSStatsTotalOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 4),
    _AxsEtherTxQoSStatsTotalOutFrames_Type()
)
axsEtherTxQoSStatsTotalOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsTotalOutFrames.setStatus("current")
_AxsEtherTxQoSStatsTotalOutBytesHigh_Type = Counter32
_AxsEtherTxQoSStatsTotalOutBytesHigh_Object = MibTableColumn
axsEtherTxQoSStatsTotalOutBytesHigh = _AxsEtherTxQoSStatsTotalOutBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 5),
    _AxsEtherTxQoSStatsTotalOutBytesHigh_Type()
)
axsEtherTxQoSStatsTotalOutBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsTotalOutBytesHigh.setStatus("current")
_AxsEtherTxQoSStatsTotalOutBytesLow_Type = Counter32
_AxsEtherTxQoSStatsTotalOutBytesLow_Object = MibTableColumn
axsEtherTxQoSStatsTotalOutBytesLow = _AxsEtherTxQoSStatsTotalOutBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 6),
    _AxsEtherTxQoSStatsTotalOutBytesLow_Type()
)
axsEtherTxQoSStatsTotalOutBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsTotalOutBytesLow.setStatus("current")
_AxsEtherTxQoSStatsTotalDiscardFrames_Type = Counter32
_AxsEtherTxQoSStatsTotalDiscardFrames_Object = MibTableColumn
axsEtherTxQoSStatsTotalDiscardFrames = _AxsEtherTxQoSStatsTotalDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 1, 1, 7),
    _AxsEtherTxQoSStatsTotalDiscardFrames_Type()
)
axsEtherTxQoSStatsTotalDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsTotalDiscardFrames.setStatus("current")
_AxsEtherTxQoSStatsQueueTable_Object = MibTable
axsEtherTxQoSStatsQueueTable = _AxsEtherTxQoSStatsQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueTable.setStatus("current")
_AxsEtherTxQoSStatsQueueEntry_Object = MibTableRow
axsEtherTxQoSStatsQueueEntry = _AxsEtherTxQoSStatsQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1)
)
axsEtherTxQoSStatsQueueEntry.setIndexNames(
    (0, "AX1230S", "axsEtherTxQoSStatsQueueIndex"),
    (0, "AX1230S", "axsEtherTxQoSStatsQueueQueIndex"),
)
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueEntry.setStatus("current")
_AxsEtherTxQoSStatsQueueIndex_Type = Integer32
_AxsEtherTxQoSStatsQueueIndex_Object = MibTableColumn
axsEtherTxQoSStatsQueueIndex = _AxsEtherTxQoSStatsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 1),
    _AxsEtherTxQoSStatsQueueIndex_Type()
)
axsEtherTxQoSStatsQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueIndex.setStatus("current")
_AxsEtherTxQoSStatsQueueQueIndex_Type = Integer32
_AxsEtherTxQoSStatsQueueQueIndex_Object = MibTableColumn
axsEtherTxQoSStatsQueueQueIndex = _AxsEtherTxQoSStatsQueueQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 2),
    _AxsEtherTxQoSStatsQueueQueIndex_Type()
)
axsEtherTxQoSStatsQueueQueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueQueIndex.setStatus("current")
_AxsEtherTxQoSStatsQueueQlen_Type = Integer32
_AxsEtherTxQoSStatsQueueQlen_Object = MibTableColumn
axsEtherTxQoSStatsQueueQlen = _AxsEtherTxQoSStatsQueueQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 3),
    _AxsEtherTxQoSStatsQueueQlen_Type()
)
axsEtherTxQoSStatsQueueQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueQlen.setStatus("current")
_AxsEtherTxQoSStatsQueueMaxQlen_Type = Integer32
_AxsEtherTxQoSStatsQueueMaxQlen_Object = MibTableColumn
axsEtherTxQoSStatsQueueMaxQlen = _AxsEtherTxQoSStatsQueueMaxQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 4),
    _AxsEtherTxQoSStatsQueueMaxQlen_Type()
)
axsEtherTxQoSStatsQueueMaxQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueMaxQlen.setStatus("current")
_AxsEtherTxQoSStatsQueueDiscardFramesClass1_Type = Counter64
_AxsEtherTxQoSStatsQueueDiscardFramesClass1_Object = MibTableColumn
axsEtherTxQoSStatsQueueDiscardFramesClass1 = _AxsEtherTxQoSStatsQueueDiscardFramesClass1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 5),
    _AxsEtherTxQoSStatsQueueDiscardFramesClass1_Type()
)
axsEtherTxQoSStatsQueueDiscardFramesClass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueDiscardFramesClass1.setStatus("current")
_AxsEtherTxQoSStatsQueueDiscardFramesClass2_Type = Counter64
_AxsEtherTxQoSStatsQueueDiscardFramesClass2_Object = MibTableColumn
axsEtherTxQoSStatsQueueDiscardFramesClass2 = _AxsEtherTxQoSStatsQueueDiscardFramesClass2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 6),
    _AxsEtherTxQoSStatsQueueDiscardFramesClass2_Type()
)
axsEtherTxQoSStatsQueueDiscardFramesClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueDiscardFramesClass2.setStatus("current")
_AxsEtherTxQoSStatsQueueDiscardFramesClass3_Type = Counter64
_AxsEtherTxQoSStatsQueueDiscardFramesClass3_Object = MibTableColumn
axsEtherTxQoSStatsQueueDiscardFramesClass3 = _AxsEtherTxQoSStatsQueueDiscardFramesClass3_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 7),
    _AxsEtherTxQoSStatsQueueDiscardFramesClass3_Type()
)
axsEtherTxQoSStatsQueueDiscardFramesClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueDiscardFramesClass3.setStatus("current")
_AxsEtherTxQoSStatsQueueDiscardFramesClass4_Type = Counter64
_AxsEtherTxQoSStatsQueueDiscardFramesClass4_Object = MibTableColumn
axsEtherTxQoSStatsQueueDiscardFramesClass4 = _AxsEtherTxQoSStatsQueueDiscardFramesClass4_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 1, 2, 1, 8),
    _AxsEtherTxQoSStatsQueueDiscardFramesClass4_Type()
)
axsEtherTxQoSStatsQueueDiscardFramesClass4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsEtherTxQoSStatsQueueDiscardFramesClass4.setStatus("current")
_AxsEthShaper_ObjectIdentity = ObjectIdentity
axsEthShaper = _AxsEthShaper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 4)
)
_AxsEthShaperAgQue_ObjectIdentity = ObjectIdentity
axsEthShaperAgQue = _AxsEthShaperAgQue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 6, 5)
)
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
    axsDHCPAddrValue.setStatus("current")
_AxsDHCPFreeAddrValue_Type = Integer32
_AxsDHCPFreeAddrValue_Object = MibScalar
axsDHCPFreeAddrValue = _AxsDHCPFreeAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 1, 10, 2),
    _AxsDHCPFreeAddrValue_Type()
)
axsDHCPFreeAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsDHCPFreeAddrValue.setStatus("current")
_AxsGsrp_ObjectIdentity = ObjectIdentity
axsGsrp = _AxsGsrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4)
)
_AxsGsrpGroupTable_Object = MibTable
axsGsrpGroupTable = _AxsGsrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    axsGsrpGroupTable.setStatus("current")
_AxsGsrpGroupEntry_Object = MibTableRow
axsGsrpGroupEntry = _AxsGsrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1)
)
axsGsrpGroupEntry.setIndexNames(
    (0, "AX1230S", "axsGsrpGroupId"),
)
if mibBuilder.loadTexts:
    axsGsrpGroupEntry.setStatus("current")
_AxsGsrpGroupId_Type = Integer32
_AxsGsrpGroupId_Object = MibTableColumn
axsGsrpGroupId = _AxsGsrpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 1),
    _AxsGsrpGroupId_Type()
)
axsGsrpGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpGroupId.setStatus("current")
_AxsGsrpGroupRowStatus_Type = RowStatus
_AxsGsrpGroupRowStatus_Object = MibTableColumn
axsGsrpGroupRowStatus = _AxsGsrpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 2),
    _AxsGsrpGroupRowStatus_Type()
)
axsGsrpGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpGroupRowStatus.setStatus("current")
_AxsGsrpMacAddress_Type = MacAddress
_AxsGsrpMacAddress_Object = MibTableColumn
axsGsrpMacAddress = _AxsGsrpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 3),
    _AxsGsrpMacAddress_Type()
)
axsGsrpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpMacAddress.setStatus("current")
_AxsGsrpAdvertiseHoldTime_Type = Integer32
_AxsGsrpAdvertiseHoldTime_Object = MibTableColumn
axsGsrpAdvertiseHoldTime = _AxsGsrpAdvertiseHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 4),
    _AxsGsrpAdvertiseHoldTime_Type()
)
axsGsrpAdvertiseHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpAdvertiseHoldTime.setStatus("current")
_AxsGsrpAdvertiseInterval_Type = Integer32
_AxsGsrpAdvertiseInterval_Object = MibTableColumn
axsGsrpAdvertiseInterval = _AxsGsrpAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 1, 1, 5),
    _AxsGsrpAdvertiseInterval_Type()
)
axsGsrpAdvertiseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpAdvertiseInterval.setStatus("current")


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
    axsGsrpSelectionPattern.setStatus("current")


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
    axsGsrpLayer3Redundancy.setStatus("current")
_AxsGsrpVlanGroupTable_Object = MibTable
axsGsrpVlanGroupTable = _AxsGsrpVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    axsGsrpVlanGroupTable.setStatus("current")
_AxsGsrpVlanGroupEntry_Object = MibTableRow
axsGsrpVlanGroupEntry = _AxsGsrpVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1)
)
axsGsrpVlanGroupEntry.setIndexNames(
    (0, "AX1230S", "axsGsrpGroupId"),
    (0, "AX1230S", "axsGsrpVlanGroupId"),
)
if mibBuilder.loadTexts:
    axsGsrpVlanGroupEntry.setStatus("current")
_AxsGsrpVlanGroupId_Type = Integer32
_AxsGsrpVlanGroupId_Object = MibTableColumn
axsGsrpVlanGroupId = _AxsGsrpVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 1),
    _AxsGsrpVlanGroupId_Type()
)
axsGsrpVlanGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpVlanGroupId.setStatus("current")
_AxsGsrpVlanGroupRowStatus_Type = RowStatus
_AxsGsrpVlanGroupRowStatus_Object = MibTableColumn
axsGsrpVlanGroupRowStatus = _AxsGsrpVlanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 2),
    _AxsGsrpVlanGroupRowStatus_Type()
)
axsGsrpVlanGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpVlanGroupRowStatus.setStatus("current")


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
    axsGsrpState.setStatus("current")
_AxsGsrpPriority_Type = Integer32
_AxsGsrpPriority_Object = MibTableColumn
axsGsrpPriority = _AxsGsrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 4),
    _AxsGsrpPriority_Type()
)
axsGsrpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpPriority.setStatus("current")
_AxsGsrpActivePorts_Type = Integer32
_AxsGsrpActivePorts_Object = MibTableColumn
axsGsrpActivePorts = _AxsGsrpActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 5),
    _AxsGsrpActivePorts_Type()
)
axsGsrpActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpActivePorts.setStatus("current")
_AxsGsrpTransitionToMasterCounts_Type = Integer32
_AxsGsrpTransitionToMasterCounts_Object = MibTableColumn
axsGsrpTransitionToMasterCounts = _AxsGsrpTransitionToMasterCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 6),
    _AxsGsrpTransitionToMasterCounts_Type()
)
axsGsrpTransitionToMasterCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpTransitionToMasterCounts.setStatus("current")
_AxsGsrpTransitionFromMasterCounts_Type = Integer32
_AxsGsrpTransitionFromMasterCounts_Object = MibTableColumn
axsGsrpTransitionFromMasterCounts = _AxsGsrpTransitionFromMasterCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 7),
    _AxsGsrpTransitionFromMasterCounts_Type()
)
axsGsrpTransitionFromMasterCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpTransitionFromMasterCounts.setStatus("current")
_AxsGsrpLastTransitionTime_Type = TimeStamp
_AxsGsrpLastTransitionTime_Object = MibTableColumn
axsGsrpLastTransitionTime = _AxsGsrpLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 8),
    _AxsGsrpLastTransitionTime_Type()
)
axsGsrpLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpLastTransitionTime.setStatus("current")
_AxsGsrpVirtualMacAddress_Type = MacAddress
_AxsGsrpVirtualMacAddress_Object = MibTableColumn
axsGsrpVirtualMacAddress = _AxsGsrpVirtualMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 2, 1, 9),
    _AxsGsrpVirtualMacAddress_Type()
)
axsGsrpVirtualMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpVirtualMacAddress.setStatus("current")
_AxsGsrpNeighborGroupTable_Object = MibTable
axsGsrpNeighborGroupTable = _AxsGsrpNeighborGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    axsGsrpNeighborGroupTable.setStatus("current")
_AxsGsrpNeighborGroupEntry_Object = MibTableRow
axsGsrpNeighborGroupEntry = _AxsGsrpNeighborGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1)
)
axsGsrpNeighborGroupEntry.setIndexNames(
    (0, "AX1230S", "axsGsrpNeighborGroupId"),
    (0, "AX1230S", "axsGsrpNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    axsGsrpNeighborGroupEntry.setStatus("current")
_AxsGsrpNeighborGroupId_Type = Integer32
_AxsGsrpNeighborGroupId_Object = MibTableColumn
axsGsrpNeighborGroupId = _AxsGsrpNeighborGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1, 1),
    _AxsGsrpNeighborGroupId_Type()
)
axsGsrpNeighborGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpNeighborGroupId.setStatus("current")
_AxsGsrpNeighborMacAddress_Type = MacAddress
_AxsGsrpNeighborMacAddress_Object = MibTableColumn
axsGsrpNeighborMacAddress = _AxsGsrpNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1, 2),
    _AxsGsrpNeighborMacAddress_Type()
)
axsGsrpNeighborMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpNeighborMacAddress.setStatus("current")
_AxsGsrpNeighborAdvertiseHoldTime_Type = Integer32
_AxsGsrpNeighborAdvertiseHoldTime_Object = MibTableColumn
axsGsrpNeighborAdvertiseHoldTime = _AxsGsrpNeighborAdvertiseHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1, 3),
    _AxsGsrpNeighborAdvertiseHoldTime_Type()
)
axsGsrpNeighborAdvertiseHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpNeighborAdvertiseHoldTime.setStatus("current")
_AxsGsrpNeighborAdvertiseInterval_Type = Integer32
_AxsGsrpNeighborAdvertiseInterval_Object = MibTableColumn
axsGsrpNeighborAdvertiseInterval = _AxsGsrpNeighborAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 3, 1, 4),
    _AxsGsrpNeighborAdvertiseInterval_Type()
)
axsGsrpNeighborAdvertiseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpNeighborAdvertiseInterval.setStatus("current")


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
    axsGsrpNeighborSelectionPattern.setStatus("current")
_AxsGsrpNeighborVlanGroupTable_Object = MibTable
axsGsrpNeighborVlanGroupTable = _AxsGsrpNeighborVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    axsGsrpNeighborVlanGroupTable.setStatus("current")
_AxsGsrpNeighborVlanGroupEntry_Object = MibTableRow
axsGsrpNeighborVlanGroupEntry = _AxsGsrpNeighborVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4, 1)
)
axsGsrpNeighborVlanGroupEntry.setIndexNames(
    (0, "AX1230S", "axsGsrpNeighborGroupId"),
    (0, "AX1230S", "axsGsrpNeighborVlanGroupId"),
    (0, "AX1230S", "axsGsrpNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    axsGsrpNeighborVlanGroupEntry.setStatus("current")
_AxsGsrpNeighborVlanGroupId_Type = Integer32
_AxsGsrpNeighborVlanGroupId_Object = MibTableColumn
axsGsrpNeighborVlanGroupId = _AxsGsrpNeighborVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4, 1, 1),
    _AxsGsrpNeighborVlanGroupId_Type()
)
axsGsrpNeighborVlanGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsGsrpNeighborVlanGroupId.setStatus("current")


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
    axsGsrpNeighborState.setStatus("current")
_AxsGsrpNeighborPriority_Type = Integer32
_AxsGsrpNeighborPriority_Object = MibTableColumn
axsGsrpNeighborPriority = _AxsGsrpNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4, 1, 3),
    _AxsGsrpNeighborPriority_Type()
)
axsGsrpNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpNeighborPriority.setStatus("current")
_AxsGsrpNeighborActivePorts_Type = Integer32
_AxsGsrpNeighborActivePorts_Object = MibTableColumn
axsGsrpNeighborActivePorts = _AxsGsrpNeighborActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 4, 4, 1, 4),
    _AxsGsrpNeighborActivePorts_Type()
)
axsGsrpNeighborActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsGsrpNeighborActivePorts.setStatus("current")
_AxsFdb_ObjectIdentity = ObjectIdentity
axsFdb = _AxsFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5)
)
_AxsFdbCounterTable_Object = MibTable
axsFdbCounterTable = _AxsFdbCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    axsFdbCounterTable.setStatus("current")
_AxsFdbCounterEntry_Object = MibTableRow
axsFdbCounterEntry = _AxsFdbCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1)
)
axsFdbCounterEntry.setIndexNames(
    (0, "AX1230S", "axsFdbCounterNifIndex"),
    (0, "AX1230S", "axsFdbCounterLineIndex"),
)
if mibBuilder.loadTexts:
    axsFdbCounterEntry.setStatus("current")
_AxsFdbCounterNifIndex_Type = Integer32
_AxsFdbCounterNifIndex_Object = MibTableColumn
axsFdbCounterNifIndex = _AxsFdbCounterNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1, 1),
    _AxsFdbCounterNifIndex_Type()
)
axsFdbCounterNifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsFdbCounterNifIndex.setStatus("current")
_AxsFdbCounterLineIndex_Type = Integer32
_AxsFdbCounterLineIndex_Object = MibTableColumn
axsFdbCounterLineIndex = _AxsFdbCounterLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1, 2),
    _AxsFdbCounterLineIndex_Type()
)
axsFdbCounterLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsFdbCounterLineIndex.setStatus("current")
_AxsFdbCounterCounts_Type = Counter32
_AxsFdbCounterCounts_Object = MibTableColumn
axsFdbCounterCounts = _AxsFdbCounterCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1, 3),
    _AxsFdbCounterCounts_Type()
)
axsFdbCounterCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsFdbCounterCounts.setStatus("current")


class _AxsFdbCounterType_Type(Integer32):
    """Custom type axsFdbCounterType based on Integer32"""
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


_AxsFdbCounterType_Type.__name__ = "Integer32"
_AxsFdbCounterType_Object = MibTableColumn
axsFdbCounterType = _AxsFdbCounterType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1, 4),
    _AxsFdbCounterType_Type()
)
axsFdbCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsFdbCounterType.setStatus("current")
_AxsFdbCounterLimits_Type = Counter32
_AxsFdbCounterLimits_Object = MibTableColumn
axsFdbCounterLimits = _AxsFdbCounterLimits_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1, 5),
    _AxsFdbCounterLimits_Type()
)
axsFdbCounterLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsFdbCounterLimits.setStatus("current")
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
    axsVBBaseTable.setStatus("current")
_AxsVBBaseEntry_Object = MibTableRow
axsVBBaseEntry = _AxsVBBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1)
)
axsVBBaseEntry.setIndexNames(
    (0, "AX1230S", "axsVBBaseIndex"),
)
if mibBuilder.loadTexts:
    axsVBBaseEntry.setStatus("current")
_AxsVBBaseIndex_Type = VlanIndex
_AxsVBBaseIndex_Object = MibTableColumn
axsVBBaseIndex = _AxsVBBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 1),
    _AxsVBBaseIndex_Type()
)
axsVBBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseIndex.setStatus("current")
_AxsVBBaseBridgeAddress_Type = MacAddress
_AxsVBBaseBridgeAddress_Object = MibTableColumn
axsVBBaseBridgeAddress = _AxsVBBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 2),
    _AxsVBBaseBridgeAddress_Type()
)
axsVBBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseBridgeAddress.setStatus("current")
_AxsVBBaseNumPorts_Type = Integer32
_AxsVBBaseNumPorts_Object = MibTableColumn
axsVBBaseNumPorts = _AxsVBBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 3),
    _AxsVBBaseNumPorts_Type()
)
axsVBBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseNumPorts.setStatus("current")


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
    axsVBBaseType.setStatus("current")
_AxsVBBaseVlanIfIndex_Type = Integer32
_AxsVBBaseVlanIfIndex_Object = MibTableColumn
axsVBBaseVlanIfIndex = _AxsVBBaseVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 5),
    _AxsVBBaseVlanIfIndex_Type()
)
axsVBBaseVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseVlanIfIndex.setStatus("current")


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
    axsVBBaseVlanType.setStatus("current")
_AxsVBBaseVlanID_Type = VlanIdOrZero
_AxsVBBaseVlanID_Object = MibTableColumn
axsVBBaseVlanID = _AxsVBBaseVlanID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 7),
    _AxsVBBaseVlanID_Type()
)
axsVBBaseVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseVlanID.setStatus("current")
_AxsVBBaseAssociatedPrimaryVlan_Type = VlanIdOrZero
_AxsVBBaseAssociatedPrimaryVlan_Object = MibTableColumn
axsVBBaseAssociatedPrimaryVlan = _AxsVBBaseAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 8),
    _AxsVBBaseAssociatedPrimaryVlan_Type()
)
axsVBBaseAssociatedPrimaryVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseAssociatedPrimaryVlan.setStatus("current")


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
    axsVBBaseIfStatus.setStatus("current")
_AxsVBBaseLastChange_Type = TimeTicks
_AxsVBBaseLastChange_Object = MibTableColumn
axsVBBaseLastChange = _AxsVBBaseLastChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 1, 1, 10),
    _AxsVBBaseLastChange_Type()
)
axsVBBaseLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBaseLastChange.setStatus("current")


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
    axsVBBasePrivateVlanType.setStatus("current")
_AxsVBBasePortTable_Object = MibTable
axsVBBasePortTable = _AxsVBBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    axsVBBasePortTable.setStatus("current")
_AxsVBBasePortEntry_Object = MibTableRow
axsVBBasePortEntry = _AxsVBBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1)
)
axsVBBasePortEntry.setIndexNames(
    (0, "AX1230S", "axsVBBasePortIndex"),
    (0, "AX1230S", "axsVBBasePort"),
)
if mibBuilder.loadTexts:
    axsVBBasePortEntry.setStatus("current")
_AxsVBBasePortIndex_Type = VlanIndex
_AxsVBBasePortIndex_Object = MibTableColumn
axsVBBasePortIndex = _AxsVBBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 1),
    _AxsVBBasePortIndex_Type()
)
axsVBBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortIndex.setStatus("current")
_AxsVBBasePort_Type = Integer32
_AxsVBBasePort_Object = MibTableColumn
axsVBBasePort = _AxsVBBasePort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 2),
    _AxsVBBasePort_Type()
)
axsVBBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePort.setStatus("current")
_AxsVBBasePortIfIndex_Type = Integer32
_AxsVBBasePortIfIndex_Object = MibTableColumn
axsVBBasePortIfIndex = _AxsVBBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 3),
    _AxsVBBasePortIfIndex_Type()
)
axsVBBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortIfIndex.setStatus("current")
_AxsVBBasePortCircuit_Type = ObjectIdentifier
_AxsVBBasePortCircuit_Object = MibTableColumn
axsVBBasePortCircuit = _AxsVBBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 4),
    _AxsVBBasePortCircuit_Type()
)
axsVBBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortCircuit.setStatus("current")
_AxsVBBasePortDelayExceededDiscards_Type = Counter32
_AxsVBBasePortDelayExceededDiscards_Object = MibTableColumn
axsVBBasePortDelayExceededDiscards = _AxsVBBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 5),
    _AxsVBBasePortDelayExceededDiscards_Type()
)
axsVBBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortDelayExceededDiscards.setStatus("current")
_AxsVBBasePortMtuExceededDiscards_Type = Counter32
_AxsVBBasePortMtuExceededDiscards_Object = MibTableColumn
axsVBBasePortMtuExceededDiscards = _AxsVBBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 6),
    _AxsVBBasePortMtuExceededDiscards_Type()
)
axsVBBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortMtuExceededDiscards.setStatus("current")


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
    axsVBBasePortState.setStatus("current")


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
    axsVBBasePortTaggedState.setStatus("current")
_AxsVBBasePortTranslatedTagID_Type = VlanIdOrZero
_AxsVBBasePortTranslatedTagID_Object = MibTableColumn
axsVBBasePortTranslatedTagID = _AxsVBBasePortTranslatedTagID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 1, 2, 1, 9),
    _AxsVBBasePortTranslatedTagID_Type()
)
axsVBBasePortTranslatedTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBBasePortTranslatedTagID.setStatus("current")
_AxsVlanBridgeStp_ObjectIdentity = ObjectIdentity
axsVlanBridgeStp = _AxsVlanBridgeStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2)
)
_AxsVBStpTable_Object = MibTable
axsVBStpTable = _AxsVBStpTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    axsVBStpTable.setStatus("current")
_AxsVBStpEntry_Object = MibTableRow
axsVBStpEntry = _AxsVBStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1)
)
axsVBStpEntry.setIndexNames(
    (0, "AX1230S", "axsVBStpIndex"),
)
if mibBuilder.loadTexts:
    axsVBStpEntry.setStatus("current")
_AxsVBStpIndex_Type = VlanIndex
_AxsVBStpIndex_Object = MibTableColumn
axsVBStpIndex = _AxsVBStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 1),
    _AxsVBStpIndex_Type()
)
axsVBStpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpIndex.setStatus("current")


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
    axsVBStpProtocolSpecification.setStatus("current")
_AxsVBStpPriority_Type = Integer32
_AxsVBStpPriority_Object = MibTableColumn
axsVBStpPriority = _AxsVBStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 3),
    _AxsVBStpPriority_Type()
)
axsVBStpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPriority.setStatus("current")
_AxsVBStpTimeSinceTopologyChange_Type = TimeTicks
_AxsVBStpTimeSinceTopologyChange_Object = MibTableColumn
axsVBStpTimeSinceTopologyChange = _AxsVBStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 4),
    _AxsVBStpTimeSinceTopologyChange_Type()
)
axsVBStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpTimeSinceTopologyChange.setStatus("current")
_AxsVBStpTopChanges_Type = Counter32
_AxsVBStpTopChanges_Object = MibTableColumn
axsVBStpTopChanges = _AxsVBStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 5),
    _AxsVBStpTopChanges_Type()
)
axsVBStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpTopChanges.setStatus("current")
_AxsVBStpDesignatedRoot_Type = BridgeId
_AxsVBStpDesignatedRoot_Object = MibTableColumn
axsVBStpDesignatedRoot = _AxsVBStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 6),
    _AxsVBStpDesignatedRoot_Type()
)
axsVBStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpDesignatedRoot.setStatus("current")
_AxsVBStpRootCost_Type = Integer32
_AxsVBStpRootCost_Object = MibTableColumn
axsVBStpRootCost = _AxsVBStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 7),
    _AxsVBStpRootCost_Type()
)
axsVBStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpRootCost.setStatus("current")
_AxsVBStpRootPort_Type = Integer32
_AxsVBStpRootPort_Object = MibTableColumn
axsVBStpRootPort = _AxsVBStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 8),
    _AxsVBStpRootPort_Type()
)
axsVBStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpRootPort.setStatus("current")
_AxsVBStpMaxAge_Type = Timeout
_AxsVBStpMaxAge_Object = MibTableColumn
axsVBStpMaxAge = _AxsVBStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 9),
    _AxsVBStpMaxAge_Type()
)
axsVBStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpMaxAge.setStatus("current")
_AxsVBStpHelloTime_Type = Timeout
_AxsVBStpHelloTime_Object = MibTableColumn
axsVBStpHelloTime = _AxsVBStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 10),
    _AxsVBStpHelloTime_Type()
)
axsVBStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpHelloTime.setStatus("current")
_AxsVBStpHoldTime_Type = Integer32
_AxsVBStpHoldTime_Object = MibTableColumn
axsVBStpHoldTime = _AxsVBStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 11),
    _AxsVBStpHoldTime_Type()
)
axsVBStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpHoldTime.setStatus("current")
_AxsVBStpForwardDelay_Type = Timeout
_AxsVBStpForwardDelay_Object = MibTableColumn
axsVBStpForwardDelay = _AxsVBStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 12),
    _AxsVBStpForwardDelay_Type()
)
axsVBStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpForwardDelay.setStatus("current")
_AxsVBStpBridgeMaxAge_Type = Timeout
_AxsVBStpBridgeMaxAge_Object = MibTableColumn
axsVBStpBridgeMaxAge = _AxsVBStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 13),
    _AxsVBStpBridgeMaxAge_Type()
)
axsVBStpBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpBridgeMaxAge.setStatus("current")
_AxsVBStpBridgeHelloTime_Type = Timeout
_AxsVBStpBridgeHelloTime_Object = MibTableColumn
axsVBStpBridgeHelloTime = _AxsVBStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 14),
    _AxsVBStpBridgeHelloTime_Type()
)
axsVBStpBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpBridgeHelloTime.setStatus("current")
_AxsVBStpBridgeForwardDelay_Type = Timeout
_AxsVBStpBridgeForwardDelay_Object = MibTableColumn
axsVBStpBridgeForwardDelay = _AxsVBStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 1, 1, 15),
    _AxsVBStpBridgeForwardDelay_Type()
)
axsVBStpBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpBridgeForwardDelay.setStatus("current")
_AxsVBStpPortTable_Object = MibTable
axsVBStpPortTable = _AxsVBStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    axsVBStpPortTable.setStatus("current")
_AxsVBStpPortEntry_Object = MibTableRow
axsVBStpPortEntry = _AxsVBStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1)
)
axsVBStpPortEntry.setIndexNames(
    (0, "AX1230S", "axsVBStpPortIndex"),
    (0, "AX1230S", "axsVBStpPort"),
)
if mibBuilder.loadTexts:
    axsVBStpPortEntry.setStatus("current")
_AxsVBStpPortIndex_Type = VlanIndex
_AxsVBStpPortIndex_Object = MibTableColumn
axsVBStpPortIndex = _AxsVBStpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 1),
    _AxsVBStpPortIndex_Type()
)
axsVBStpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortIndex.setStatus("current")
_AxsVBStpPort_Type = Integer32
_AxsVBStpPort_Object = MibTableColumn
axsVBStpPort = _AxsVBStpPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 2),
    _AxsVBStpPort_Type()
)
axsVBStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPort.setStatus("current")
_AxsVBStpPortPriority_Type = Integer32
_AxsVBStpPortPriority_Object = MibTableColumn
axsVBStpPortPriority = _AxsVBStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 3),
    _AxsVBStpPortPriority_Type()
)
axsVBStpPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortPriority.setStatus("current")


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
    axsVBStpPortState.setStatus("current")


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
    axsVBStpPortEnable.setStatus("current")
_AxsVBStpPortPathCost_Type = Integer32
_AxsVBStpPortPathCost_Object = MibTableColumn
axsVBStpPortPathCost = _AxsVBStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 6),
    _AxsVBStpPortPathCost_Type()
)
axsVBStpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortPathCost.setStatus("current")
_AxsVBStpPortDesignatedRoot_Type = BridgeId
_AxsVBStpPortDesignatedRoot_Object = MibTableColumn
axsVBStpPortDesignatedRoot = _AxsVBStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 7),
    _AxsVBStpPortDesignatedRoot_Type()
)
axsVBStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortDesignatedRoot.setStatus("current")
_AxsVBStpPortDesignatedCost_Type = Integer32
_AxsVBStpPortDesignatedCost_Object = MibTableColumn
axsVBStpPortDesignatedCost = _AxsVBStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 8),
    _AxsVBStpPortDesignatedCost_Type()
)
axsVBStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortDesignatedCost.setStatus("current")
_AxsVBStpPortDesignatedBridge_Type = BridgeId
_AxsVBStpPortDesignatedBridge_Object = MibTableColumn
axsVBStpPortDesignatedBridge = _AxsVBStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 9),
    _AxsVBStpPortDesignatedBridge_Type()
)
axsVBStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortDesignatedBridge.setStatus("current")
_AxsVBStpPortDesignatedPort_Type = OctetString
_AxsVBStpPortDesignatedPort_Object = MibTableColumn
axsVBStpPortDesignatedPort = _AxsVBStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 10),
    _AxsVBStpPortDesignatedPort_Type()
)
axsVBStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortDesignatedPort.setStatus("current")
_AxsVBStpPortForwardTransitions_Type = Counter32
_AxsVBStpPortForwardTransitions_Object = MibTableColumn
axsVBStpPortForwardTransitions = _AxsVBStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 2, 2, 1, 11),
    _AxsVBStpPortForwardTransitions_Type()
)
axsVBStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStpPortForwardTransitions.setStatus("current")
_AxsVlanBridgeTp_ObjectIdentity = ObjectIdentity
axsVlanBridgeTp = _AxsVlanBridgeTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4)
)
_AxsVBTpTable_Object = MibTable
axsVBTpTable = _AxsVBTpTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    axsVBTpTable.setStatus("current")
_AxsVBTpEntry_Object = MibTableRow
axsVBTpEntry = _AxsVBTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1, 1)
)
axsVBTpEntry.setIndexNames(
    (0, "AX1230S", "axsVBTpIndex"),
)
if mibBuilder.loadTexts:
    axsVBTpEntry.setStatus("current")
_AxsVBTpIndex_Type = VlanIndex
_AxsVBTpIndex_Object = MibTableColumn
axsVBTpIndex = _AxsVBTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1, 1, 1),
    _AxsVBTpIndex_Type()
)
axsVBTpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpIndex.setStatus("current")
_AxsVBTpLearnedEntryDiscards_Type = Counter32
_AxsVBTpLearnedEntryDiscards_Object = MibTableColumn
axsVBTpLearnedEntryDiscards = _AxsVBTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1, 1, 2),
    _AxsVBTpLearnedEntryDiscards_Type()
)
axsVBTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpLearnedEntryDiscards.setStatus("current")
_AxsVBTpAgingTime_Type = Integer32
_AxsVBTpAgingTime_Object = MibTableColumn
axsVBTpAgingTime = _AxsVBTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 1, 1, 3),
    _AxsVBTpAgingTime_Type()
)
axsVBTpAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpAgingTime.setStatus("current")
_AxsVBTpFdbTable_Object = MibTable
axsVBTpFdbTable = _AxsVBTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    axsVBTpFdbTable.setStatus("current")
_AxsVBTpFdbEntry_Object = MibTableRow
axsVBTpFdbEntry = _AxsVBTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2, 1)
)
axsVBTpFdbEntry.setIndexNames(
    (0, "AX1230S", "axsVBTpFdbIndex"),
    (0, "AX1230S", "axsVBTpFdbAddress"),
)
if mibBuilder.loadTexts:
    axsVBTpFdbEntry.setStatus("current")
_AxsVBTpFdbIndex_Type = VlanIndex
_AxsVBTpFdbIndex_Object = MibTableColumn
axsVBTpFdbIndex = _AxsVBTpFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2, 1, 1),
    _AxsVBTpFdbIndex_Type()
)
axsVBTpFdbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpFdbIndex.setStatus("current")
_AxsVBTpFdbAddress_Type = MacAddress
_AxsVBTpFdbAddress_Object = MibTableColumn
axsVBTpFdbAddress = _AxsVBTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2, 1, 2),
    _AxsVBTpFdbAddress_Type()
)
axsVBTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpFdbAddress.setStatus("current")
_AxsVBTpFdbPort_Type = Integer32
_AxsVBTpFdbPort_Object = MibTableColumn
axsVBTpFdbPort = _AxsVBTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 2, 1, 3),
    _AxsVBTpFdbPort_Type()
)
axsVBTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpFdbPort.setStatus("current")


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
    axsVBTpFdbStatus.setStatus("current")
_AxsVBTpPortTable_Object = MibTable
axsVBTpPortTable = _AxsVBTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    axsVBTpPortTable.setStatus("current")
_AxsVBTpPortEntry_Object = MibTableRow
axsVBTpPortEntry = _AxsVBTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1)
)
axsVBTpPortEntry.setIndexNames(
    (0, "AX1230S", "axsVBTpPortIndex"),
    (0, "AX1230S", "axsVBTpPort"),
)
if mibBuilder.loadTexts:
    axsVBTpPortEntry.setStatus("current")
_AxsVBTpPortIndex_Type = VlanIndex
_AxsVBTpPortIndex_Object = MibTableColumn
axsVBTpPortIndex = _AxsVBTpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 1),
    _AxsVBTpPortIndex_Type()
)
axsVBTpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortIndex.setStatus("current")
_AxsVBTpPort_Type = Integer32
_AxsVBTpPort_Object = MibTableColumn
axsVBTpPort = _AxsVBTpPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 2),
    _AxsVBTpPort_Type()
)
axsVBTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPort.setStatus("current")
_AxsVBTpPortMaxInfo_Type = Integer32
_AxsVBTpPortMaxInfo_Object = MibTableColumn
axsVBTpPortMaxInfo = _AxsVBTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 3),
    _AxsVBTpPortMaxInfo_Type()
)
axsVBTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortMaxInfo.setStatus("current")
_AxsVBTpPortInFrames_Type = Counter32
_AxsVBTpPortInFrames_Object = MibTableColumn
axsVBTpPortInFrames = _AxsVBTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 4),
    _AxsVBTpPortInFrames_Type()
)
axsVBTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortInFrames.setStatus("current")
_AxsVBTpPortOutFrames_Type = Counter32
_AxsVBTpPortOutFrames_Object = MibTableColumn
axsVBTpPortOutFrames = _AxsVBTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 5),
    _AxsVBTpPortOutFrames_Type()
)
axsVBTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortOutFrames.setStatus("current")
_AxsVBTpPortInDiscards_Type = Counter32
_AxsVBTpPortInDiscards_Object = MibTableColumn
axsVBTpPortInDiscards = _AxsVBTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 4, 3, 1, 6),
    _AxsVBTpPortInDiscards_Type()
)
axsVBTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBTpPortInDiscards.setStatus("current")
_AxsVlanBridgeStatic_ObjectIdentity = ObjectIdentity
axsVlanBridgeStatic = _AxsVlanBridgeStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5)
)
_AxsVBStaticTable_Object = MibTable
axsVBStaticTable = _AxsVBStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    axsVBStaticTable.setStatus("current")
_AxsVBStaticEntry_Object = MibTableRow
axsVBStaticEntry = _AxsVBStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1)
)
axsVBStaticEntry.setIndexNames(
    (0, "AX1230S", "axsVBStaticIndex"),
    (0, "AX1230S", "axsVBStaticAddress"),
)
if mibBuilder.loadTexts:
    axsVBStaticEntry.setStatus("current")
_AxsVBStaticIndex_Type = VlanIndex
_AxsVBStaticIndex_Object = MibTableColumn
axsVBStaticIndex = _AxsVBStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1, 1),
    _AxsVBStaticIndex_Type()
)
axsVBStaticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStaticIndex.setStatus("current")
_AxsVBStaticAddress_Type = MacAddress
_AxsVBStaticAddress_Object = MibTableColumn
axsVBStaticAddress = _AxsVBStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1, 2),
    _AxsVBStaticAddress_Type()
)
axsVBStaticAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStaticAddress.setStatus("current")
_AxsVBStaticReceivePort_Type = Integer32
_AxsVBStaticReceivePort_Object = MibTableColumn
axsVBStaticReceivePort = _AxsVBStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1, 3),
    _AxsVBStaticReceivePort_Type()
)
axsVBStaticReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStaticReceivePort.setStatus("current")
_AxsVBStaticAllowedToGoTo_Type = OctetString
_AxsVBStaticAllowedToGoTo_Object = MibTableColumn
axsVBStaticAllowedToGoTo = _AxsVBStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 5, 1, 1, 4),
    _AxsVBStaticAllowedToGoTo_Type()
)
axsVBStaticAllowedToGoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVBStaticAllowedToGoTo.setStatus("current")


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
    axsVBStaticStatus.setStatus("current")
_AxsVlanBridgeMaxVlans_Type = VlanIndex
_AxsVlanBridgeMaxVlans_Object = MibScalar
axsVlanBridgeMaxVlans = _AxsVlanBridgeMaxVlans_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 101),
    _AxsVlanBridgeMaxVlans_Type()
)
axsVlanBridgeMaxVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVlanBridgeMaxVlans.setStatus("current")
_AxsVlanBridgeMaxSpans_Type = VlanIndex
_AxsVlanBridgeMaxSpans_Object = MibScalar
axsVlanBridgeMaxSpans = _AxsVlanBridgeMaxSpans_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 1, 102),
    _AxsVlanBridgeMaxSpans_Type()
)
axsVlanBridgeMaxSpans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVlanBridgeMaxSpans.setStatus("current")
_AxsVlanTagTranslation_ObjectIdentity = ObjectIdentity
axsVlanTagTranslation = _AxsVlanTagTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10)
)
_AxsVlanTagTranslationTable_Object = MibTable
axsVlanTagTranslationTable = _AxsVlanTagTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1)
)
if mibBuilder.loadTexts:
    axsVlanTagTranslationTable.setStatus("current")
_AxsVlanTagTranslationEntry_Object = MibTableRow
axsVlanTagTranslationEntry = _AxsVlanTagTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1)
)
axsVlanTagTranslationEntry.setIndexNames(
    (0, "AX1230S", "axsVlanTagTranslationVlanId"),
    (0, "AX1230S", "axsVlanTagTranslationTranslatedId"),
)
if mibBuilder.loadTexts:
    axsVlanTagTranslationEntry.setStatus("current")
_AxsVlanTagTranslationVlanId_Type = Integer32
_AxsVlanTagTranslationVlanId_Object = MibTableColumn
axsVlanTagTranslationVlanId = _AxsVlanTagTranslationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1, 1),
    _AxsVlanTagTranslationVlanId_Type()
)
axsVlanTagTranslationVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVlanTagTranslationVlanId.setStatus("current")
_AxsVlanTagTranslationTranslatedId_Type = Integer32
_AxsVlanTagTranslationTranslatedId_Object = MibTableColumn
axsVlanTagTranslationTranslatedId = _AxsVlanTagTranslationTranslatedId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1, 2),
    _AxsVlanTagTranslationTranslatedId_Type()
)
axsVlanTagTranslationTranslatedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVlanTagTranslationTranslatedId.setStatus("current")
_AxsVlanTagTranslationPorts_Type = PortList
_AxsVlanTagTranslationPorts_Object = MibTableColumn
axsVlanTagTranslationPorts = _AxsVlanTagTranslationPorts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1, 3),
    _AxsVlanTagTranslationPorts_Type()
)
axsVlanTagTranslationPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVlanTagTranslationPorts.setStatus("current")
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
    axsOadpGlobalActive.setStatus("current")
_AxsOadpGlobalCdpActive_Type = TruthValue
_AxsOadpGlobalCdpActive_Object = MibScalar
axsOadpGlobalCdpActive = _AxsOadpGlobalCdpActive_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 2),
    _AxsOadpGlobalCdpActive_Type()
)
axsOadpGlobalCdpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalCdpActive.setStatus("current")
_AxsOadpGlobalMessageInterval_Type = Integer32
_AxsOadpGlobalMessageInterval_Object = MibScalar
axsOadpGlobalMessageInterval = _AxsOadpGlobalMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 3),
    _AxsOadpGlobalMessageInterval_Type()
)
axsOadpGlobalMessageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalMessageInterval.setStatus("current")
_AxsOadpGlobalHoldTime_Type = Integer32
_AxsOadpGlobalHoldTime_Object = MibScalar
axsOadpGlobalHoldTime = _AxsOadpGlobalHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 4),
    _AxsOadpGlobalHoldTime_Type()
)
axsOadpGlobalHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalHoldTime.setStatus("current")
_AxsOadpGlobalCacheLastChange_Type = TimeTicks
_AxsOadpGlobalCacheLastChange_Object = MibScalar
axsOadpGlobalCacheLastChange = _AxsOadpGlobalCacheLastChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 5),
    _AxsOadpGlobalCacheLastChange_Type()
)
axsOadpGlobalCacheLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalCacheLastChange.setStatus("current")
_AxsOadpGlobalName_Type = DisplayString
_AxsOadpGlobalName_Object = MibScalar
axsOadpGlobalName = _AxsOadpGlobalName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 1, 6),
    _AxsOadpGlobalName_Type()
)
axsOadpGlobalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpGlobalName.setStatus("current")


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
    axsOadpGlobalNameType.setStatus("current")
_AxsOadpPortInfo_ObjectIdentity = ObjectIdentity
axsOadpPortInfo = _AxsOadpPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2)
)
_AxsOadpPortConfigTable_Object = MibTable
axsOadpPortConfigTable = _AxsOadpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    axsOadpPortConfigTable.setStatus("current")
_AxsOadpPortConfigEntry_Object = MibTableRow
axsOadpPortConfigEntry = _AxsOadpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2, 1, 1)
)
axsOadpPortConfigEntry.setIndexNames(
    (0, "AX1230S", "axsOadpPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    axsOadpPortConfigEntry.setStatus("current")
_AxsOadpPortConfigIfIndex_Type = InterfaceIndex
_AxsOadpPortConfigIfIndex_Object = MibTableColumn
axsOadpPortConfigIfIndex = _AxsOadpPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2, 1, 1, 1),
    _AxsOadpPortConfigIfIndex_Type()
)
axsOadpPortConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpPortConfigIfIndex.setStatus("current")
_AxsOadpPortConfigActive_Type = TruthValue
_AxsOadpPortConfigActive_Object = MibTableColumn
axsOadpPortConfigActive = _AxsOadpPortConfigActive_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 2, 1, 1, 2),
    _AxsOadpPortConfigActive_Type()
)
axsOadpPortConfigActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpPortConfigActive.setStatus("current")
_AxsOadpNeighborInfo_ObjectIdentity = ObjectIdentity
axsOadpNeighborInfo = _AxsOadpNeighborInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3)
)
_AxsOadpNeighborTable_Object = MibTable
axsOadpNeighborTable = _AxsOadpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    axsOadpNeighborTable.setStatus("current")
_AxsOadpNeighborEntry_Object = MibTableRow
axsOadpNeighborEntry = _AxsOadpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1)
)
axsOadpNeighborEntry.setIndexNames(
    (0, "AX1230S", "axsOadpIfIndex"),
    (0, "AX1230S", "axsOadpTagID"),
    (0, "AX1230S", "axsOadpNeighborIndex"),
    (0, "AX1230S", "axsOadpNeighborTagID"),
)
if mibBuilder.loadTexts:
    axsOadpNeighborEntry.setStatus("current")
_AxsOadpIfIndex_Type = InterfaceIndex
_AxsOadpIfIndex_Object = MibTableColumn
axsOadpIfIndex = _AxsOadpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 1),
    _AxsOadpIfIndex_Type()
)
axsOadpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpIfIndex.setStatus("current")
_AxsOadpTagID_Type = Integer32
_AxsOadpTagID_Object = MibTableColumn
axsOadpTagID = _AxsOadpTagID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 2),
    _AxsOadpTagID_Type()
)
axsOadpTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpTagID.setStatus("current")
_AxsOadpNeighborIndex_Type = Integer32
_AxsOadpNeighborIndex_Object = MibTableColumn
axsOadpNeighborIndex = _AxsOadpNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 3),
    _AxsOadpNeighborIndex_Type()
)
axsOadpNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborIndex.setStatus("current")
_AxsOadpNeighborTagID_Type = Integer32
_AxsOadpNeighborTagID_Object = MibTableColumn
axsOadpNeighborTagID = _AxsOadpNeighborTagID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 4),
    _AxsOadpNeighborTagID_Type()
)
axsOadpNeighborTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborTagID.setStatus("current")


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
    axsOadpNeighborVendorType.setStatus("current")


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
    axsOadpNeighborSNMPAgentAddressType.setStatus("current")
_AxsOadpNeighborSNMPAgentAddress_Type = DisplayString
_AxsOadpNeighborSNMPAgentAddress_Object = MibTableColumn
axsOadpNeighborSNMPAgentAddress = _AxsOadpNeighborSNMPAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 7),
    _AxsOadpNeighborSNMPAgentAddress_Type()
)
axsOadpNeighborSNMPAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSNMPAgentAddress.setStatus("current")
_AxsOadpNeighborDescr_Type = DisplayString
_AxsOadpNeighborDescr_Object = MibTableColumn
axsOadpNeighborDescr = _AxsOadpNeighborDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 8),
    _AxsOadpNeighborDescr_Type()
)
axsOadpNeighborDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborDescr.setStatus("current")
_AxsOadpNeighborDeviceID_Type = DisplayString
_AxsOadpNeighborDeviceID_Object = MibTableColumn
axsOadpNeighborDeviceID = _AxsOadpNeighborDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 9),
    _AxsOadpNeighborDeviceID_Type()
)
axsOadpNeighborDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborDeviceID.setStatus("current")
_AxsOadpNeighborSlotPort_Type = DisplayString
_AxsOadpNeighborSlotPort_Object = MibTableColumn
axsOadpNeighborSlotPort = _AxsOadpNeighborSlotPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 10),
    _AxsOadpNeighborSlotPort_Type()
)
axsOadpNeighborSlotPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSlotPort.setStatus("current")
_AxsOadpNeighborIfIndex_Type = InterfaceIndex
_AxsOadpNeighborIfIndex_Object = MibTableColumn
axsOadpNeighborIfIndex = _AxsOadpNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 11),
    _AxsOadpNeighborIfIndex_Type()
)
axsOadpNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborIfIndex.setStatus("current")
_AxsOadpNeighborIfSpeed_Type = Gauge32
_AxsOadpNeighborIfSpeed_Object = MibTableColumn
axsOadpNeighborIfSpeed = _AxsOadpNeighborIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 12),
    _AxsOadpNeighborIfSpeed_Type()
)
axsOadpNeighborIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborIfSpeed.setStatus("current")
_AxsOadpNeighborDeviceType_Type = DisplayString
_AxsOadpNeighborDeviceType_Object = MibTableColumn
axsOadpNeighborDeviceType = _AxsOadpNeighborDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 13),
    _AxsOadpNeighborDeviceType_Type()
)
axsOadpNeighborDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborDeviceType.setStatus("current")
_AxsOadpNeighborService_Type = OctetString
_AxsOadpNeighborService_Object = MibTableColumn
axsOadpNeighborService = _AxsOadpNeighborService_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 14),
    _AxsOadpNeighborService_Type()
)
axsOadpNeighborService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborService.setStatus("current")
_AxsOadpNeighborVTPMgmtDomain_Type = DisplayString
_AxsOadpNeighborVTPMgmtDomain_Object = MibTableColumn
axsOadpNeighborVTPMgmtDomain = _AxsOadpNeighborVTPMgmtDomain_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 15),
    _AxsOadpNeighborVTPMgmtDomain_Type()
)
axsOadpNeighborVTPMgmtDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborVTPMgmtDomain.setStatus("current")
_AxsOadpNeighborNativeVLAN_Type = Integer32
_AxsOadpNeighborNativeVLAN_Object = MibTableColumn
axsOadpNeighborNativeVLAN = _AxsOadpNeighborNativeVLAN_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 16),
    _AxsOadpNeighborNativeVLAN_Type()
)
axsOadpNeighborNativeVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborNativeVLAN.setStatus("current")


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
    axsOadpNeighborDuplex.setStatus("current")
_AxsOadpNeighborApplianceID_Type = Gauge32
_AxsOadpNeighborApplianceID_Object = MibTableColumn
axsOadpNeighborApplianceID = _AxsOadpNeighborApplianceID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 18),
    _AxsOadpNeighborApplianceID_Type()
)
axsOadpNeighborApplianceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborApplianceID.setStatus("current")
_AxsOadpNeighborVlanID_Type = Gauge32
_AxsOadpNeighborVlanID_Object = MibTableColumn
axsOadpNeighborVlanID = _AxsOadpNeighborVlanID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 19),
    _AxsOadpNeighborVlanID_Type()
)
axsOadpNeighborVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborVlanID.setStatus("current")
_AxsOadpNeighborPowerConsumption_Type = Gauge32
_AxsOadpNeighborPowerConsumption_Object = MibTableColumn
axsOadpNeighborPowerConsumption = _AxsOadpNeighborPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 20),
    _AxsOadpNeighborPowerConsumption_Type()
)
axsOadpNeighborPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborPowerConsumption.setStatus("current")
_AxsOadpNeighborMTU_Type = Gauge32
_AxsOadpNeighborMTU_Object = MibTableColumn
axsOadpNeighborMTU = _AxsOadpNeighborMTU_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 21),
    _AxsOadpNeighborMTU_Type()
)
axsOadpNeighborMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborMTU.setStatus("current")
_AxsOadpNeighborSysName_Type = DisplayString
_AxsOadpNeighborSysName_Object = MibTableColumn
axsOadpNeighborSysName = _AxsOadpNeighborSysName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 22),
    _AxsOadpNeighborSysName_Type()
)
axsOadpNeighborSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSysName.setStatus("current")
_AxsOadpNeighborSysObjectID_Type = ObjectIdentifier
_AxsOadpNeighborSysObjectID_Object = MibTableColumn
axsOadpNeighborSysObjectID = _AxsOadpNeighborSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 23),
    _AxsOadpNeighborSysObjectID_Type()
)
axsOadpNeighborSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSysObjectID.setStatus("current")


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
    axsOadpNeighborSecondarySNMPAgentAddressType.setStatus("current")
_AxsOadpNeighborSecondarySNMPAgentAddress_Type = DisplayString
_AxsOadpNeighborSecondarySNMPAgentAddress_Object = MibTableColumn
axsOadpNeighborSecondarySNMPAgentAddress = _AxsOadpNeighborSecondarySNMPAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 25),
    _AxsOadpNeighborSecondarySNMPAgentAddress_Type()
)
axsOadpNeighborSecondarySNMPAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborSecondarySNMPAgentAddress.setStatus("current")
_AxsOadpNeighborPhysLocation_Type = DisplayString
_AxsOadpNeighborPhysLocation_Object = MibTableColumn
axsOadpNeighborPhysLocation = _AxsOadpNeighborPhysLocation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 26),
    _AxsOadpNeighborPhysLocation_Type()
)
axsOadpNeighborPhysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborPhysLocation.setStatus("current")
_AxsOadpNeighborCacheLastChange_Type = TimeTicks
_AxsOadpNeighborCacheLastChange_Object = MibTableColumn
axsOadpNeighborCacheLastChange = _AxsOadpNeighborCacheLastChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 27),
    _AxsOadpNeighborCacheLastChange_Type()
)
axsOadpNeighborCacheLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborCacheLastChange.setStatus("current")
_AxsOadpNeighborIfHighSpeed_Type = Gauge32
_AxsOadpNeighborIfHighSpeed_Object = MibTableColumn
axsOadpNeighborIfHighSpeed = _AxsOadpNeighborIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 1, 3, 1, 1, 28),
    _AxsOadpNeighborIfHighSpeed_Type()
)
axsOadpNeighborIfHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOadpNeighborIfHighSpeed.setStatus("current")
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
    axsAccessFilterStatsInTable.setStatus("current")
_AxsAccessFilterStatsInEntry_Object = MibTableRow
axsAccessFilterStatsInEntry = _AxsAccessFilterStatsInEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1)
)
axsAccessFilterStatsInEntry.setIndexNames(
    (0, "AX1230S", "axsAccessFilterStatsInifIndex"),
    (0, "AX1230S", "axsAccessFilterStatsInifIndexType"),
    (0, "AX1230S", "axsAccessFilterStatsInListIndex"),
    (0, "AX1230S", "axsAccessFilterStatsInSequenceNumber"),
)
if mibBuilder.loadTexts:
    axsAccessFilterStatsInEntry.setStatus("current")
_AxsAccessFilterStatsInifIndex_Type = Integer32
_AxsAccessFilterStatsInifIndex_Object = MibTableColumn
axsAccessFilterStatsInifIndex = _AxsAccessFilterStatsInifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 1),
    _AxsAccessFilterStatsInifIndex_Type()
)
axsAccessFilterStatsInifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInifIndex.setStatus("current")
_AxsAccessFilterStatsInifIndexType_Type = Integer32
_AxsAccessFilterStatsInifIndexType_Object = MibTableColumn
axsAccessFilterStatsInifIndexType = _AxsAccessFilterStatsInifIndexType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 2),
    _AxsAccessFilterStatsInifIndexType_Type()
)
axsAccessFilterStatsInifIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInifIndexType.setStatus("current")
_AxsAccessFilterStatsInListIndex_Type = Unsigned32
_AxsAccessFilterStatsInListIndex_Object = MibTableColumn
axsAccessFilterStatsInListIndex = _AxsAccessFilterStatsInListIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 3),
    _AxsAccessFilterStatsInListIndex_Type()
)
axsAccessFilterStatsInListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInListIndex.setStatus("current")
_AxsAccessFilterStatsInSequenceNumber_Type = Unsigned32
_AxsAccessFilterStatsInSequenceNumber_Object = MibTableColumn
axsAccessFilterStatsInSequenceNumber = _AxsAccessFilterStatsInSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 4),
    _AxsAccessFilterStatsInSequenceNumber_Type()
)
axsAccessFilterStatsInSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInSequenceNumber.setStatus("current")
_AxsAccessFilterStatsInListName_Type = DisplayString
_AxsAccessFilterStatsInListName_Object = MibTableColumn
axsAccessFilterStatsInListName = _AxsAccessFilterStatsInListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 5),
    _AxsAccessFilterStatsInListName_Type()
)
axsAccessFilterStatsInListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInListName.setStatus("current")
_AxsAccessFilterStatsInMatchedPackets_Type = Counter64
_AxsAccessFilterStatsInMatchedPackets_Object = MibTableColumn
axsAccessFilterStatsInMatchedPackets = _AxsAccessFilterStatsInMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 9, 1, 1, 6),
    _AxsAccessFilterStatsInMatchedPackets_Type()
)
axsAccessFilterStatsInMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsAccessFilterStatsInMatchedPackets.setStatus("current")
_AxsQosFlowStats_ObjectIdentity = ObjectIdentity
axsQosFlowStats = _AxsQosFlowStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11)
)
_AxsQosFlowStatsInTable_Object = MibTable
axsQosFlowStatsInTable = _AxsQosFlowStatsInTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1)
)
if mibBuilder.loadTexts:
    axsQosFlowStatsInTable.setStatus("current")
_AxsQosFlowStatsInEntry_Object = MibTableRow
axsQosFlowStatsInEntry = _AxsQosFlowStatsInEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1)
)
axsQosFlowStatsInEntry.setIndexNames(
    (0, "AX1230S", "axsQosFlowStatsInifIndex"),
    (0, "AX1230S", "axsQosFlowStatsInifIndexType"),
    (0, "AX1230S", "axsQosFlowStatsInListIndex"),
    (0, "AX1230S", "axsQosFlowStatsInSequenceNumber"),
)
if mibBuilder.loadTexts:
    axsQosFlowStatsInEntry.setStatus("current")
_AxsQosFlowStatsInifIndex_Type = Integer32
_AxsQosFlowStatsInifIndex_Object = MibTableColumn
axsQosFlowStatsInifIndex = _AxsQosFlowStatsInifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 1),
    _AxsQosFlowStatsInifIndex_Type()
)
axsQosFlowStatsInifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsQosFlowStatsInifIndex.setStatus("current")
_AxsQosFlowStatsInifIndexType_Type = Integer32
_AxsQosFlowStatsInifIndexType_Object = MibTableColumn
axsQosFlowStatsInifIndexType = _AxsQosFlowStatsInifIndexType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 2),
    _AxsQosFlowStatsInifIndexType_Type()
)
axsQosFlowStatsInifIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsQosFlowStatsInifIndexType.setStatus("current")
_AxsQosFlowStatsInListIndex_Type = Unsigned32
_AxsQosFlowStatsInListIndex_Object = MibTableColumn
axsQosFlowStatsInListIndex = _AxsQosFlowStatsInListIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 3),
    _AxsQosFlowStatsInListIndex_Type()
)
axsQosFlowStatsInListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsQosFlowStatsInListIndex.setStatus("current")
_AxsQosFlowStatsInSequenceNumber_Type = Unsigned32
_AxsQosFlowStatsInSequenceNumber_Object = MibTableColumn
axsQosFlowStatsInSequenceNumber = _AxsQosFlowStatsInSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 4),
    _AxsQosFlowStatsInSequenceNumber_Type()
)
axsQosFlowStatsInSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsQosFlowStatsInSequenceNumber.setStatus("current")
_AxsQosFlowStatsInListName_Type = DisplayString
_AxsQosFlowStatsInListName_Object = MibTableColumn
axsQosFlowStatsInListName = _AxsQosFlowStatsInListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 5),
    _AxsQosFlowStatsInListName_Type()
)
axsQosFlowStatsInListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInListName.setStatus("current")
_AxsQosFlowStatsInMatchedPackets_Type = Counter64
_AxsQosFlowStatsInMatchedPackets_Object = MibTableColumn
axsQosFlowStatsInMatchedPackets = _AxsQosFlowStatsInMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 6),
    _AxsQosFlowStatsInMatchedPackets_Type()
)
axsQosFlowStatsInMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPackets.setStatus("current")
_AxsQosFlowStatsInMatchedPacketsMinUnder_Type = Counter64
_AxsQosFlowStatsInMatchedPacketsMinUnder_Object = MibTableColumn
axsQosFlowStatsInMatchedPacketsMinUnder = _AxsQosFlowStatsInMatchedPacketsMinUnder_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 7),
    _AxsQosFlowStatsInMatchedPacketsMinUnder_Type()
)
axsQosFlowStatsInMatchedPacketsMinUnder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPacketsMinUnder.setStatus("current")
_AxsQosFlowStatsInMatchedPacketsMinOver_Type = Counter64
_AxsQosFlowStatsInMatchedPacketsMinOver_Object = MibTableColumn
axsQosFlowStatsInMatchedPacketsMinOver = _AxsQosFlowStatsInMatchedPacketsMinOver_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 8),
    _AxsQosFlowStatsInMatchedPacketsMinOver_Type()
)
axsQosFlowStatsInMatchedPacketsMinOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPacketsMinOver.setStatus("current")
_AxsQosFlowStatsInMatchedPacketsMaxUnder_Type = Counter64
_AxsQosFlowStatsInMatchedPacketsMaxUnder_Object = MibTableColumn
axsQosFlowStatsInMatchedPacketsMaxUnder = _AxsQosFlowStatsInMatchedPacketsMaxUnder_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 9),
    _AxsQosFlowStatsInMatchedPacketsMaxUnder_Type()
)
axsQosFlowStatsInMatchedPacketsMaxUnder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPacketsMaxUnder.setStatus("current")
_AxsQosFlowStatsInMatchedPacketsMaxOver_Type = Counter64
_AxsQosFlowStatsInMatchedPacketsMaxOver_Object = MibTableColumn
axsQosFlowStatsInMatchedPacketsMaxOver = _AxsQosFlowStatsInMatchedPacketsMaxOver_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 8, 11, 1, 1, 10),
    _AxsQosFlowStatsInMatchedPacketsMaxOver_Type()
)
axsQosFlowStatsInMatchedPacketsMaxOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsQosFlowStatsInMatchedPacketsMaxOver.setStatus("current")
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
    (0, "AX1230S", "axsL2ldPortIndex"),
    (0, "AX1230S", "axsL2ldPortIfIndex"),
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
_AxsOspf_ObjectIdentity = ObjectIdentity
axsOspf = _AxsOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14)
)
_AxsOspfGeneralTable_Object = MibTable
axsOspfGeneralTable = _AxsOspfGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    axsOspfGeneralTable.setStatus("current")
_AxsOspfGeneralEntry_Object = MibTableRow
axsOspfGeneralEntry = _AxsOspfGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1)
)
axsOspfGeneralEntry.setIndexNames(
    (0, "AX1230S", "axsOspfGeneralDomainNumber"),
)
if mibBuilder.loadTexts:
    axsOspfGeneralEntry.setStatus("current")
_AxsOspfGeneralDomainNumber_Type = Integer32
_AxsOspfGeneralDomainNumber_Object = MibTableColumn
axsOspfGeneralDomainNumber = _AxsOspfGeneralDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 1),
    _AxsOspfGeneralDomainNumber_Type()
)
axsOspfGeneralDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfGeneralDomainNumber.setStatus("current")
_AxsOspfRouterId_Type = IpAddress
_AxsOspfRouterId_Object = MibTableColumn
axsOspfRouterId = _AxsOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 2),
    _AxsOspfRouterId_Type()
)
axsOspfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfRouterId.setStatus("current")


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
    axsOspfAdminStat.setStatus("current")
_AxsOspfVersionNumber_Type = Integer32
_AxsOspfVersionNumber_Object = MibTableColumn
axsOspfVersionNumber = _AxsOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 4),
    _AxsOspfVersionNumber_Type()
)
axsOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVersionNumber.setStatus("current")


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
    axsOspfAreaBdrRtrStatus.setStatus("current")


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
    axsOspfASBdrRtrStatus.setStatus("current")
_AxsOspfExternLsaCount_Type = Gauge32
_AxsOspfExternLsaCount_Object = MibTableColumn
axsOspfExternLsaCount = _AxsOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 7),
    _AxsOspfExternLsaCount_Type()
)
axsOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExternLsaCount.setStatus("current")
_AxsOspfExternLsaCksumSum_Type = Integer32
_AxsOspfExternLsaCksumSum_Object = MibTableColumn
axsOspfExternLsaCksumSum = _AxsOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 8),
    _AxsOspfExternLsaCksumSum_Type()
)
axsOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExternLsaCksumSum.setStatus("current")


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
    axsOspfTOSSupport.setStatus("current")
_AxsOspfOriginateNewLsas_Type = Counter32
_AxsOspfOriginateNewLsas_Object = MibTableColumn
axsOspfOriginateNewLsas = _AxsOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 10),
    _AxsOspfOriginateNewLsas_Type()
)
axsOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfOriginateNewLsas.setStatus("current")
_AxsOspfRxNewLsas_Type = Counter32
_AxsOspfRxNewLsas_Object = MibTableColumn
axsOspfRxNewLsas = _AxsOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 11),
    _AxsOspfRxNewLsas_Type()
)
axsOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfRxNewLsas.setStatus("current")
_AxsOspfExtLsdbLimit_Type = Integer32
_AxsOspfExtLsdbLimit_Object = MibTableColumn
axsOspfExtLsdbLimit = _AxsOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 12),
    _AxsOspfExtLsdbLimit_Type()
)
axsOspfExtLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbLimit.setStatus("current")
_AxsOspfMulticastExtensions_Type = Integer32
_AxsOspfMulticastExtensions_Object = MibTableColumn
axsOspfMulticastExtensions = _AxsOspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1, 13),
    _AxsOspfMulticastExtensions_Type()
)
axsOspfMulticastExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfMulticastExtensions.setStatus("current")
_AxsOspfAreaTable_Object = MibTable
axsOspfAreaTable = _AxsOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2)
)
if mibBuilder.loadTexts:
    axsOspfAreaTable.setStatus("current")
_AxsOspfAreaEntry_Object = MibTableRow
axsOspfAreaEntry = _AxsOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1)
)
axsOspfAreaEntry.setIndexNames(
    (0, "AX1230S", "axsOspfAreaDomainNumber"),
    (0, "AX1230S", "axsOspfAreaId"),
)
if mibBuilder.loadTexts:
    axsOspfAreaEntry.setStatus("current")
_AxsOspfAreaDomainNumber_Type = Integer32
_AxsOspfAreaDomainNumber_Object = MibTableColumn
axsOspfAreaDomainNumber = _AxsOspfAreaDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 1),
    _AxsOspfAreaDomainNumber_Type()
)
axsOspfAreaDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaDomainNumber.setStatus("current")
_AxsOspfAreaId_Type = IpAddress
_AxsOspfAreaId_Object = MibTableColumn
axsOspfAreaId = _AxsOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 2),
    _AxsOspfAreaId_Type()
)
axsOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaId.setStatus("current")
_AxsOspfAuthType_Type = Integer32
_AxsOspfAuthType_Object = MibTableColumn
axsOspfAuthType = _AxsOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 3),
    _AxsOspfAuthType_Type()
)
axsOspfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAuthType.setStatus("current")


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
    axsOspfImportAsExtern.setStatus("current")
_AxsOspfSpfRuns_Type = Counter32
_AxsOspfSpfRuns_Object = MibTableColumn
axsOspfSpfRuns = _AxsOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 5),
    _AxsOspfSpfRuns_Type()
)
axsOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfSpfRuns.setStatus("current")
_AxsOspfAreaBdrRtrCount_Type = Gauge32
_AxsOspfAreaBdrRtrCount_Object = MibTableColumn
axsOspfAreaBdrRtrCount = _AxsOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 6),
    _AxsOspfAreaBdrRtrCount_Type()
)
axsOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaBdrRtrCount.setStatus("current")
_AxsOspfAsBdrRtrCount_Type = Gauge32
_AxsOspfAsBdrRtrCount_Object = MibTableColumn
axsOspfAsBdrRtrCount = _AxsOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 7),
    _AxsOspfAsBdrRtrCount_Type()
)
axsOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAsBdrRtrCount.setStatus("current")
_AxsOspfAreaLsaCount_Type = Gauge32
_AxsOspfAreaLsaCount_Object = MibTableColumn
axsOspfAreaLsaCount = _AxsOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 8),
    _AxsOspfAreaLsaCount_Type()
)
axsOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaLsaCount.setStatus("current")
_AxsOspfAreaLsaCksumSum_Type = Integer32
_AxsOspfAreaLsaCksumSum_Object = MibTableColumn
axsOspfAreaLsaCksumSum = _AxsOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 2, 1, 9),
    _AxsOspfAreaLsaCksumSum_Type()
)
axsOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaLsaCksumSum.setStatus("current")


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
    axsOspfAreaSummary.setStatus("current")


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
    axsOspfAreaStatus.setStatus("current")
_AxsOspfStubAreaTable_Object = MibTable
axsOspfStubAreaTable = _AxsOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3)
)
if mibBuilder.loadTexts:
    axsOspfStubAreaTable.setStatus("current")
_AxsOspfStubAreaEntry_Object = MibTableRow
axsOspfStubAreaEntry = _AxsOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1)
)
axsOspfStubAreaEntry.setIndexNames(
    (0, "AX1230S", "axsOspfStubDomainNumber"),
    (0, "AX1230S", "axsOspfStubAreaId"),
    (0, "AX1230S", "axsOspfStubTOS"),
)
if mibBuilder.loadTexts:
    axsOspfStubAreaEntry.setStatus("current")
_AxsOspfStubDomainNumber_Type = Integer32
_AxsOspfStubDomainNumber_Object = MibTableColumn
axsOspfStubDomainNumber = _AxsOspfStubDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 1),
    _AxsOspfStubDomainNumber_Type()
)
axsOspfStubDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubDomainNumber.setStatus("current")
_AxsOspfStubAreaId_Type = IpAddress
_AxsOspfStubAreaId_Object = MibTableColumn
axsOspfStubAreaId = _AxsOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 2),
    _AxsOspfStubAreaId_Type()
)
axsOspfStubAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubAreaId.setStatus("current")
_AxsOspfStubTOS_Type = Integer32
_AxsOspfStubTOS_Object = MibTableColumn
axsOspfStubTOS = _AxsOspfStubTOS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 3),
    _AxsOspfStubTOS_Type()
)
axsOspfStubTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubTOS.setStatus("current")
_AxsOspfStubMetric_Type = Integer32
_AxsOspfStubMetric_Object = MibTableColumn
axsOspfStubMetric = _AxsOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 3, 1, 4),
    _AxsOspfStubMetric_Type()
)
axsOspfStubMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfStubMetric.setStatus("current")


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
    axsOspfStubStatus.setStatus("current")


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
    axsOspfStubMetricType.setStatus("current")
_AxsOspfLsdbTable_Object = MibTable
axsOspfLsdbTable = _AxsOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4)
)
if mibBuilder.loadTexts:
    axsOspfLsdbTable.setStatus("current")
_AxsOspfLsdbEntry_Object = MibTableRow
axsOspfLsdbEntry = _AxsOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1)
)
axsOspfLsdbEntry.setIndexNames(
    (0, "AX1230S", "axsOspfLsdbDomainNumber"),
    (0, "AX1230S", "axsOspfLsdbAreaId"),
    (0, "AX1230S", "axsOspfLsdbType"),
    (0, "AX1230S", "axsOspfLsdbLsid"),
    (0, "AX1230S", "axsOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    axsOspfLsdbEntry.setStatus("current")
_AxsOspfLsdbDomainNumber_Type = Integer32
_AxsOspfLsdbDomainNumber_Object = MibTableColumn
axsOspfLsdbDomainNumber = _AxsOspfLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 1),
    _AxsOspfLsdbDomainNumber_Type()
)
axsOspfLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbDomainNumber.setStatus("current")
_AxsOspfLsdbAreaId_Type = IpAddress
_AxsOspfLsdbAreaId_Object = MibTableColumn
axsOspfLsdbAreaId = _AxsOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 2),
    _AxsOspfLsdbAreaId_Type()
)
axsOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbAreaId.setStatus("current")


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
    axsOspfLsdbType.setStatus("current")
_AxsOspfLsdbLsid_Type = IpAddress
_AxsOspfLsdbLsid_Object = MibTableColumn
axsOspfLsdbLsid = _AxsOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 4),
    _AxsOspfLsdbLsid_Type()
)
axsOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbLsid.setStatus("current")
_AxsOspfLsdbRouterId_Type = IpAddress
_AxsOspfLsdbRouterId_Object = MibTableColumn
axsOspfLsdbRouterId = _AxsOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 5),
    _AxsOspfLsdbRouterId_Type()
)
axsOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbRouterId.setStatus("current")
_AxsOspfLsdbSequence_Type = Integer32
_AxsOspfLsdbSequence_Object = MibTableColumn
axsOspfLsdbSequence = _AxsOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 6),
    _AxsOspfLsdbSequence_Type()
)
axsOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbSequence.setStatus("current")
_AxsOspfLsdbAge_Type = Integer32
_AxsOspfLsdbAge_Object = MibTableColumn
axsOspfLsdbAge = _AxsOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 7),
    _AxsOspfLsdbAge_Type()
)
axsOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbAge.setStatus("current")
_AxsOspfLsdbChecksum_Type = Integer32
_AxsOspfLsdbChecksum_Object = MibTableColumn
axsOspfLsdbChecksum = _AxsOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 8),
    _AxsOspfLsdbChecksum_Type()
)
axsOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbChecksum.setStatus("current")
_AxsOspfLsdbAdvertisement_Type = OctetString
_AxsOspfLsdbAdvertisement_Object = MibTableColumn
axsOspfLsdbAdvertisement = _AxsOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 4, 1, 9),
    _AxsOspfLsdbAdvertisement_Type()
)
axsOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfLsdbAdvertisement.setStatus("current")
_AxsOspfAreaRangeTable_Object = MibTable
axsOspfAreaRangeTable = _AxsOspfAreaRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5)
)
if mibBuilder.loadTexts:
    axsOspfAreaRangeTable.setStatus("current")
_AxsOspfAreaRangeEntry_Object = MibTableRow
axsOspfAreaRangeEntry = _AxsOspfAreaRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1)
)
axsOspfAreaRangeEntry.setIndexNames(
    (0, "AX1230S", "axsOspfAreaRangeDomainNumber"),
    (0, "AX1230S", "axsOspfAreaRangeAreaId"),
    (0, "AX1230S", "axsOspfAreaRangeNet"),
)
if mibBuilder.loadTexts:
    axsOspfAreaRangeEntry.setStatus("current")
_AxsOspfAreaRangeDomainNumber_Type = Integer32
_AxsOspfAreaRangeDomainNumber_Object = MibTableColumn
axsOspfAreaRangeDomainNumber = _AxsOspfAreaRangeDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 1),
    _AxsOspfAreaRangeDomainNumber_Type()
)
axsOspfAreaRangeDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeDomainNumber.setStatus("current")
_AxsOspfAreaRangeAreaId_Type = IpAddress
_AxsOspfAreaRangeAreaId_Object = MibTableColumn
axsOspfAreaRangeAreaId = _AxsOspfAreaRangeAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 2),
    _AxsOspfAreaRangeAreaId_Type()
)
axsOspfAreaRangeAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeAreaId.setStatus("current")
_AxsOspfAreaRangeNet_Type = IpAddress
_AxsOspfAreaRangeNet_Object = MibTableColumn
axsOspfAreaRangeNet = _AxsOspfAreaRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 3),
    _AxsOspfAreaRangeNet_Type()
)
axsOspfAreaRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeNet.setStatus("current")
_AxsOspfAreaRangeMask_Type = IpAddress
_AxsOspfAreaRangeMask_Object = MibTableColumn
axsOspfAreaRangeMask = _AxsOspfAreaRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 5, 1, 4),
    _AxsOspfAreaRangeMask_Type()
)
axsOspfAreaRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaRangeMask.setStatus("current")


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
    axsOspfAreaRangeStatus.setStatus("current")


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
    axsOspfAreaRangeEffect.setStatus("current")
_AxsOspfIfTable_Object = MibTable
axsOspfIfTable = _AxsOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7)
)
if mibBuilder.loadTexts:
    axsOspfIfTable.setStatus("current")
_AxsOspfIfEntry_Object = MibTableRow
axsOspfIfEntry = _AxsOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1)
)
axsOspfIfEntry.setIndexNames(
    (0, "AX1230S", "axsOspfIfDomainNumber"),
    (0, "AX1230S", "axsOspfIfIpAddress"),
    (0, "AX1230S", "axsOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    axsOspfIfEntry.setStatus("current")
_AxsOspfIfDomainNumber_Type = Integer32
_AxsOspfIfDomainNumber_Object = MibTableColumn
axsOspfIfDomainNumber = _AxsOspfIfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 1),
    _AxsOspfIfDomainNumber_Type()
)
axsOspfIfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfDomainNumber.setStatus("current")
_AxsOspfIfIpAddress_Type = IpAddress
_AxsOspfIfIpAddress_Object = MibTableColumn
axsOspfIfIpAddress = _AxsOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 2),
    _AxsOspfIfIpAddress_Type()
)
axsOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfIpAddress.setStatus("current")
_AxsOspfAddressLessIf_Type = Integer32
_AxsOspfAddressLessIf_Object = MibTableColumn
axsOspfAddressLessIf = _AxsOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 3),
    _AxsOspfAddressLessIf_Type()
)
axsOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAddressLessIf.setStatus("current")
_AxsOspfIfAreaId_Type = IpAddress
_AxsOspfIfAreaId_Object = MibTableColumn
axsOspfIfAreaId = _AxsOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 4),
    _AxsOspfIfAreaId_Type()
)
axsOspfIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfAreaId.setStatus("current")


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
    axsOspfIfType.setStatus("current")


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
    axsOspfIfAdminStat.setStatus("current")
_AxsOspfIfRtrPriority_Type = Integer32
_AxsOspfIfRtrPriority_Object = MibTableColumn
axsOspfIfRtrPriority = _AxsOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 7),
    _AxsOspfIfRtrPriority_Type()
)
axsOspfIfRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfRtrPriority.setStatus("current")
_AxsOspfIfTransitDelay_Type = Integer32
_AxsOspfIfTransitDelay_Object = MibTableColumn
axsOspfIfTransitDelay = _AxsOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 8),
    _AxsOspfIfTransitDelay_Type()
)
axsOspfIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfTransitDelay.setStatus("current")
_AxsOspfIfRetransInterval_Type = Integer32
_AxsOspfIfRetransInterval_Object = MibTableColumn
axsOspfIfRetransInterval = _AxsOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 9),
    _AxsOspfIfRetransInterval_Type()
)
axsOspfIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfRetransInterval.setStatus("current")
_AxsOspfIfHelloInterval_Type = Integer32
_AxsOspfIfHelloInterval_Object = MibTableColumn
axsOspfIfHelloInterval = _AxsOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 10),
    _AxsOspfIfHelloInterval_Type()
)
axsOspfIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfHelloInterval.setStatus("current")
_AxsOspfIfRtrDeadInterval_Type = Integer32
_AxsOspfIfRtrDeadInterval_Object = MibTableColumn
axsOspfIfRtrDeadInterval = _AxsOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 11),
    _AxsOspfIfRtrDeadInterval_Type()
)
axsOspfIfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfRtrDeadInterval.setStatus("current")
_AxsOspfIfPollInterval_Type = Integer32
_AxsOspfIfPollInterval_Object = MibTableColumn
axsOspfIfPollInterval = _AxsOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 12),
    _AxsOspfIfPollInterval_Type()
)
axsOspfIfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfPollInterval.setStatus("current")


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
    axsOspfIfState.setStatus("current")
_AxsOspfIfDesignatedRouter_Type = IpAddress
_AxsOspfIfDesignatedRouter_Object = MibTableColumn
axsOspfIfDesignatedRouter = _AxsOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 14),
    _AxsOspfIfDesignatedRouter_Type()
)
axsOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfDesignatedRouter.setStatus("current")
_AxsOspfIfBackupDesignatedRouter_Type = IpAddress
_AxsOspfIfBackupDesignatedRouter_Object = MibTableColumn
axsOspfIfBackupDesignatedRouter = _AxsOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 15),
    _AxsOspfIfBackupDesignatedRouter_Type()
)
axsOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfBackupDesignatedRouter.setStatus("current")
_AxsOspfIfEvents_Type = Counter32
_AxsOspfIfEvents_Object = MibTableColumn
axsOspfIfEvents = _AxsOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 16),
    _AxsOspfIfEvents_Type()
)
axsOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfEvents.setStatus("current")
_AxsOspfIfAuthKey_Type = OctetString
_AxsOspfIfAuthKey_Object = MibTableColumn
axsOspfIfAuthKey = _AxsOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 7, 1, 17),
    _AxsOspfIfAuthKey_Type()
)
axsOspfIfAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfAuthKey.setStatus("current")


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
    axsOspfIfStatus.setStatus("current")


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
    axsOspfIfMulticastForwarding.setStatus("current")
_AxsOspfIfMetricTable_Object = MibTable
axsOspfIfMetricTable = _AxsOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8)
)
if mibBuilder.loadTexts:
    axsOspfIfMetricTable.setStatus("current")
_AxsOspfIfMetricEntry_Object = MibTableRow
axsOspfIfMetricEntry = _AxsOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1)
)
axsOspfIfMetricEntry.setIndexNames(
    (0, "AX1230S", "axsOspfIfMetricDomainNumber"),
    (0, "AX1230S", "axsOspfIfMetricIpAddress"),
    (0, "AX1230S", "axsOspfIfMetricAddressLessIf"),
    (0, "AX1230S", "axsOspfIfMetricTOS"),
)
if mibBuilder.loadTexts:
    axsOspfIfMetricEntry.setStatus("current")
_AxsOspfIfMetricDomainNumber_Type = Integer32
_AxsOspfIfMetricDomainNumber_Object = MibTableColumn
axsOspfIfMetricDomainNumber = _AxsOspfIfMetricDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 1),
    _AxsOspfIfMetricDomainNumber_Type()
)
axsOspfIfMetricDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricDomainNumber.setStatus("current")
_AxsOspfIfMetricIpAddress_Type = IpAddress
_AxsOspfIfMetricIpAddress_Object = MibTableColumn
axsOspfIfMetricIpAddress = _AxsOspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 2),
    _AxsOspfIfMetricIpAddress_Type()
)
axsOspfIfMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricIpAddress.setStatus("current")
_AxsOspfIfMetricAddressLessIf_Type = Integer32
_AxsOspfIfMetricAddressLessIf_Object = MibTableColumn
axsOspfIfMetricAddressLessIf = _AxsOspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 3),
    _AxsOspfIfMetricAddressLessIf_Type()
)
axsOspfIfMetricAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricAddressLessIf.setStatus("current")
_AxsOspfIfMetricTOS_Type = Integer32
_AxsOspfIfMetricTOS_Object = MibTableColumn
axsOspfIfMetricTOS = _AxsOspfIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 4),
    _AxsOspfIfMetricTOS_Type()
)
axsOspfIfMetricTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricTOS.setStatus("current")
_AxsOspfIfMetricValue_Type = Integer32
_AxsOspfIfMetricValue_Object = MibTableColumn
axsOspfIfMetricValue = _AxsOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 8, 1, 5),
    _AxsOspfIfMetricValue_Type()
)
axsOspfIfMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfIfMetricValue.setStatus("current")


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
    axsOspfIfMetricStatus.setStatus("current")
_AxsOspfVirtIfTable_Object = MibTable
axsOspfVirtIfTable = _AxsOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9)
)
if mibBuilder.loadTexts:
    axsOspfVirtIfTable.setStatus("current")
_AxsOspfVirtIfEntry_Object = MibTableRow
axsOspfVirtIfEntry = _AxsOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1)
)
axsOspfVirtIfEntry.setIndexNames(
    (0, "AX1230S", "axsOspfVirtIfDomainNumber"),
    (0, "AX1230S", "axsOspfVirtIfAreaId"),
    (0, "AX1230S", "axsOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    axsOspfVirtIfEntry.setStatus("current")
_AxsOspfVirtIfDomainNumber_Type = Integer32
_AxsOspfVirtIfDomainNumber_Object = MibTableColumn
axsOspfVirtIfDomainNumber = _AxsOspfVirtIfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 1),
    _AxsOspfVirtIfDomainNumber_Type()
)
axsOspfVirtIfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfDomainNumber.setStatus("current")
_AxsOspfVirtIfAreaId_Type = IpAddress
_AxsOspfVirtIfAreaId_Object = MibTableColumn
axsOspfVirtIfAreaId = _AxsOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 2),
    _AxsOspfVirtIfAreaId_Type()
)
axsOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfAreaId.setStatus("current")
_AxsOspfVirtIfNeighbor_Type = IpAddress
_AxsOspfVirtIfNeighbor_Object = MibTableColumn
axsOspfVirtIfNeighbor = _AxsOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 3),
    _AxsOspfVirtIfNeighbor_Type()
)
axsOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfNeighbor.setStatus("current")
_AxsOspfVirtIfTransitDelay_Type = Integer32
_AxsOspfVirtIfTransitDelay_Object = MibTableColumn
axsOspfVirtIfTransitDelay = _AxsOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 4),
    _AxsOspfVirtIfTransitDelay_Type()
)
axsOspfVirtIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfTransitDelay.setStatus("current")
_AxsOspfVirtIfRetransInterval_Type = Integer32
_AxsOspfVirtIfRetransInterval_Object = MibTableColumn
axsOspfVirtIfRetransInterval = _AxsOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 5),
    _AxsOspfVirtIfRetransInterval_Type()
)
axsOspfVirtIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfRetransInterval.setStatus("current")
_AxsOspfVirtIfHelloInterval_Type = Integer32
_AxsOspfVirtIfHelloInterval_Object = MibTableColumn
axsOspfVirtIfHelloInterval = _AxsOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 6),
    _AxsOspfVirtIfHelloInterval_Type()
)
axsOspfVirtIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfHelloInterval.setStatus("current")
_AxsOspfVirtIfRtrDeadInterval_Type = Integer32
_AxsOspfVirtIfRtrDeadInterval_Object = MibTableColumn
axsOspfVirtIfRtrDeadInterval = _AxsOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 7),
    _AxsOspfVirtIfRtrDeadInterval_Type()
)
axsOspfVirtIfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfRtrDeadInterval.setStatus("current")


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
    axsOspfVirtIfState.setStatus("current")
_AxsOspfVirtIfEvents_Type = Counter32
_AxsOspfVirtIfEvents_Object = MibTableColumn
axsOspfVirtIfEvents = _AxsOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 9),
    _AxsOspfVirtIfEvents_Type()
)
axsOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfEvents.setStatus("current")
_AxsOspfVirtIfAuthKey_Type = OctetString
_AxsOspfVirtIfAuthKey_Object = MibTableColumn
axsOspfVirtIfAuthKey = _AxsOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 9, 1, 10),
    _AxsOspfVirtIfAuthKey_Type()
)
axsOspfVirtIfAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtIfAuthKey.setStatus("current")


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
    axsOspfVirtIfStatus.setStatus("current")
_AxsOspfNbrTable_Object = MibTable
axsOspfNbrTable = _AxsOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10)
)
if mibBuilder.loadTexts:
    axsOspfNbrTable.setStatus("current")
_AxsOspfNbrEntry_Object = MibTableRow
axsOspfNbrEntry = _AxsOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1)
)
axsOspfNbrEntry.setIndexNames(
    (0, "AX1230S", "axsOspfNbrDomainNumber"),
    (0, "AX1230S", "axsOspfNbrIpAddr"),
    (0, "AX1230S", "axsOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    axsOspfNbrEntry.setStatus("current")
_AxsOspfNbrDomainNumber_Type = Integer32
_AxsOspfNbrDomainNumber_Object = MibTableColumn
axsOspfNbrDomainNumber = _AxsOspfNbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 1),
    _AxsOspfNbrDomainNumber_Type()
)
axsOspfNbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrDomainNumber.setStatus("current")
_AxsOspfNbrIpAddr_Type = IpAddress
_AxsOspfNbrIpAddr_Object = MibTableColumn
axsOspfNbrIpAddr = _AxsOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 2),
    _AxsOspfNbrIpAddr_Type()
)
axsOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrIpAddr.setStatus("current")
_AxsOspfNbrAddressLessIndex_Type = Integer32
_AxsOspfNbrAddressLessIndex_Object = MibTableColumn
axsOspfNbrAddressLessIndex = _AxsOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 3),
    _AxsOspfNbrAddressLessIndex_Type()
)
axsOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrAddressLessIndex.setStatus("current")
_AxsOspfNbrRtrId_Type = IpAddress
_AxsOspfNbrRtrId_Object = MibTableColumn
axsOspfNbrRtrId = _AxsOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 4),
    _AxsOspfNbrRtrId_Type()
)
axsOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrRtrId.setStatus("current")
_AxsOspfNbrOptions_Type = Integer32
_AxsOspfNbrOptions_Object = MibTableColumn
axsOspfNbrOptions = _AxsOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 5),
    _AxsOspfNbrOptions_Type()
)
axsOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrOptions.setStatus("current")
_AxsOspfNbrPriority_Type = Integer32
_AxsOspfNbrPriority_Object = MibTableColumn
axsOspfNbrPriority = _AxsOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 6),
    _AxsOspfNbrPriority_Type()
)
axsOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrPriority.setStatus("current")


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
    axsOspfNbrState.setStatus("current")
_AxsOspfNbrEvents_Type = Counter32
_AxsOspfNbrEvents_Object = MibTableColumn
axsOspfNbrEvents = _AxsOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 8),
    _AxsOspfNbrEvents_Type()
)
axsOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrEvents.setStatus("current")
_AxsOspfNbrLsRetransQLen_Type = Gauge32
_AxsOspfNbrLsRetransQLen_Object = MibTableColumn
axsOspfNbrLsRetransQLen = _AxsOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 10, 1, 9),
    _AxsOspfNbrLsRetransQLen_Type()
)
axsOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfNbrLsRetransQLen.setStatus("current")


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
    axsOspfNbmaNbrStatus.setStatus("current")


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
    axsOspfNbmaNbrPermanence.setStatus("current")
_AxsOspfVirtNbrTable_Object = MibTable
axsOspfVirtNbrTable = _AxsOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11)
)
if mibBuilder.loadTexts:
    axsOspfVirtNbrTable.setStatus("current")
_AxsOspfVirtNbrEntry_Object = MibTableRow
axsOspfVirtNbrEntry = _AxsOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1)
)
axsOspfVirtNbrEntry.setIndexNames(
    (0, "AX1230S", "axsOspfVirtNbrDomainNumber"),
    (0, "AX1230S", "axsOspfVirtNbrArea"),
    (0, "AX1230S", "axsOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    axsOspfVirtNbrEntry.setStatus("current")
_AxsOspfVirtNbrDomainNumber_Type = Integer32
_AxsOspfVirtNbrDomainNumber_Object = MibTableColumn
axsOspfVirtNbrDomainNumber = _AxsOspfVirtNbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 1),
    _AxsOspfVirtNbrDomainNumber_Type()
)
axsOspfVirtNbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrDomainNumber.setStatus("current")
_AxsOspfVirtNbrArea_Type = IpAddress
_AxsOspfVirtNbrArea_Object = MibTableColumn
axsOspfVirtNbrArea = _AxsOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 2),
    _AxsOspfVirtNbrArea_Type()
)
axsOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrArea.setStatus("current")
_AxsOspfVirtNbrRtrId_Type = IpAddress
_AxsOspfVirtNbrRtrId_Object = MibTableColumn
axsOspfVirtNbrRtrId = _AxsOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 3),
    _AxsOspfVirtNbrRtrId_Type()
)
axsOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrRtrId.setStatus("current")
_AxsOspfVirtNbrIpAddr_Type = IpAddress
_AxsOspfVirtNbrIpAddr_Object = MibTableColumn
axsOspfVirtNbrIpAddr = _AxsOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 4),
    _AxsOspfVirtNbrIpAddr_Type()
)
axsOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrIpAddr.setStatus("current")
_AxsOspfVirtNbrOptions_Type = Integer32
_AxsOspfVirtNbrOptions_Object = MibTableColumn
axsOspfVirtNbrOptions = _AxsOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 5),
    _AxsOspfVirtNbrOptions_Type()
)
axsOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrOptions.setStatus("current")


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
    axsOspfVirtNbrState.setStatus("current")
_AxsOspfVirtNbrEvents_Type = Counter32
_AxsOspfVirtNbrEvents_Object = MibTableColumn
axsOspfVirtNbrEvents = _AxsOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 7),
    _AxsOspfVirtNbrEvents_Type()
)
axsOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrEvents.setStatus("current")
_AxsOspfVirtNbrLsRetransQLen_Type = Gauge32
_AxsOspfVirtNbrLsRetransQLen_Object = MibTableColumn
axsOspfVirtNbrLsRetransQLen = _AxsOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 11, 1, 8),
    _AxsOspfVirtNbrLsRetransQLen_Type()
)
axsOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfVirtNbrLsRetransQLen.setStatus("current")
_AxsOspfExtLsdbTable_Object = MibTable
axsOspfExtLsdbTable = _AxsOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12)
)
if mibBuilder.loadTexts:
    axsOspfExtLsdbTable.setStatus("current")
_AxsOspfExtLsdbEntry_Object = MibTableRow
axsOspfExtLsdbEntry = _AxsOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1)
)
axsOspfExtLsdbEntry.setIndexNames(
    (0, "AX1230S", "axsOspfExtLsdbDomainNumber"),
    (0, "AX1230S", "axsOspfExtLsdbType"),
    (0, "AX1230S", "axsOspfExtLsdbLsid"),
    (0, "AX1230S", "axsOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    axsOspfExtLsdbEntry.setStatus("current")
_AxsOspfExtLsdbDomainNumber_Type = Integer32
_AxsOspfExtLsdbDomainNumber_Object = MibTableColumn
axsOspfExtLsdbDomainNumber = _AxsOspfExtLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 1),
    _AxsOspfExtLsdbDomainNumber_Type()
)
axsOspfExtLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbDomainNumber.setStatus("current")


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
    axsOspfExtLsdbType.setStatus("current")
_AxsOspfExtLsdbLsid_Type = IpAddress
_AxsOspfExtLsdbLsid_Object = MibTableColumn
axsOspfExtLsdbLsid = _AxsOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 3),
    _AxsOspfExtLsdbLsid_Type()
)
axsOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbLsid.setStatus("current")
_AxsOspfExtLsdbRouterId_Type = IpAddress
_AxsOspfExtLsdbRouterId_Object = MibTableColumn
axsOspfExtLsdbRouterId = _AxsOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 4),
    _AxsOspfExtLsdbRouterId_Type()
)
axsOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbRouterId.setStatus("current")
_AxsOspfExtLsdbSequence_Type = Integer32
_AxsOspfExtLsdbSequence_Object = MibTableColumn
axsOspfExtLsdbSequence = _AxsOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 5),
    _AxsOspfExtLsdbSequence_Type()
)
axsOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbSequence.setStatus("current")
_AxsOspfExtLsdbAge_Type = Integer32
_AxsOspfExtLsdbAge_Object = MibTableColumn
axsOspfExtLsdbAge = _AxsOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 6),
    _AxsOspfExtLsdbAge_Type()
)
axsOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbAge.setStatus("current")
_AxsOspfExtLsdbChecksum_Type = Integer32
_AxsOspfExtLsdbChecksum_Object = MibTableColumn
axsOspfExtLsdbChecksum = _AxsOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 7),
    _AxsOspfExtLsdbChecksum_Type()
)
axsOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbChecksum.setStatus("current")
_AxsOspfExtLsdbAdvertisement_Type = OctetString
_AxsOspfExtLsdbAdvertisement_Object = MibTableColumn
axsOspfExtLsdbAdvertisement = _AxsOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 12, 1, 8),
    _AxsOspfExtLsdbAdvertisement_Type()
)
axsOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfExtLsdbAdvertisement.setStatus("current")
_AxsOspfAreaAggregateTable_Object = MibTable
axsOspfAreaAggregateTable = _AxsOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14)
)
if mibBuilder.loadTexts:
    axsOspfAreaAggregateTable.setStatus("current")
_AxsOspfAreaAggregateEntry_Object = MibTableRow
axsOspfAreaAggregateEntry = _AxsOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1)
)
axsOspfAreaAggregateEntry.setIndexNames(
    (0, "AX1230S", "axsOspfAreaAggregateDomainNumber"),
    (0, "AX1230S", "axsOspfAreaAggregateAreaID"),
    (0, "AX1230S", "axsOspfAreaAggregateLsdbType"),
    (0, "AX1230S", "axsOspfAreaAggregateNet"),
    (0, "AX1230S", "axsOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    axsOspfAreaAggregateEntry.setStatus("current")
_AxsOspfAreaAggregateDomainNumber_Type = Integer32
_AxsOspfAreaAggregateDomainNumber_Object = MibTableColumn
axsOspfAreaAggregateDomainNumber = _AxsOspfAreaAggregateDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 1),
    _AxsOspfAreaAggregateDomainNumber_Type()
)
axsOspfAreaAggregateDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateDomainNumber.setStatus("current")
_AxsOspfAreaAggregateAreaID_Type = IpAddress
_AxsOspfAreaAggregateAreaID_Object = MibTableColumn
axsOspfAreaAggregateAreaID = _AxsOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 2),
    _AxsOspfAreaAggregateAreaID_Type()
)
axsOspfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateAreaID.setStatus("current")


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
    axsOspfAreaAggregateLsdbType.setStatus("current")
_AxsOspfAreaAggregateNet_Type = IpAddress
_AxsOspfAreaAggregateNet_Object = MibTableColumn
axsOspfAreaAggregateNet = _AxsOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 4),
    _AxsOspfAreaAggregateNet_Type()
)
axsOspfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateNet.setStatus("current")
_AxsOspfAreaAggregateMask_Type = IpAddress
_AxsOspfAreaAggregateMask_Object = MibTableColumn
axsOspfAreaAggregateMask = _AxsOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 14, 1, 5),
    _AxsOspfAreaAggregateMask_Type()
)
axsOspfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfAreaAggregateMask.setStatus("current")


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
    axsOspfAreaAggregateStatus.setStatus("current")


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
    axsOspfAreaAggregateEffect.setStatus("current")
_AxsOspfTrap_ObjectIdentity = ObjectIdentity
axsOspfTrap = _AxsOspfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16)
)
_AxsOspfTrapControlTable_Object = MibTable
axsOspfTrapControlTable = _AxsOspfTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1)
)
if mibBuilder.loadTexts:
    axsOspfTrapControlTable.setStatus("current")
_AxsOspfTrapControlEntry_Object = MibTableRow
axsOspfTrapControlEntry = _AxsOspfTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1)
)
axsOspfTrapControlEntry.setIndexNames(
    (0, "AX1230S", "axsOspfTrapDomainNumber"),
)
if mibBuilder.loadTexts:
    axsOspfTrapControlEntry.setStatus("current")
_AxsOspfTrapDomainNumber_Type = Integer32
_AxsOspfTrapDomainNumber_Object = MibTableColumn
axsOspfTrapDomainNumber = _AxsOspfTrapDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1, 1),
    _AxsOspfTrapDomainNumber_Type()
)
axsOspfTrapDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfTrapDomainNumber.setStatus("current")
_AxsOspfSetTrap_Type = OctetString
_AxsOspfSetTrap_Object = MibTableColumn
axsOspfSetTrap = _AxsOspfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1, 2),
    _AxsOspfSetTrap_Type()
)
axsOspfSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    axsOspfSetTrap.setStatus("current")


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
    axsOspfConfigErrorType.setStatus("current")


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
    axsOspfPacketType.setStatus("current")
_AxsOspfPacketSrc_Type = IpAddress
_AxsOspfPacketSrc_Object = MibTableColumn
axsOspfPacketSrc = _AxsOspfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 1, 1, 5),
    _AxsOspfPacketSrc_Type()
)
axsOspfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfPacketSrc.setStatus("current")
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
    axsOspfv3GeneralTable.setStatus("current")
_AxsOspfv3GeneralEntry_Object = MibTableRow
axsOspfv3GeneralEntry = _AxsOspfv3GeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1)
)
axsOspfv3GeneralEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3GeneralDomainNumber"),
)
if mibBuilder.loadTexts:
    axsOspfv3GeneralEntry.setStatus("current")
_AxsOspfv3GeneralDomainNumber_Type = Integer32
_AxsOspfv3GeneralDomainNumber_Object = MibTableColumn
axsOspfv3GeneralDomainNumber = _AxsOspfv3GeneralDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 1),
    _AxsOspfv3GeneralDomainNumber_Type()
)
axsOspfv3GeneralDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3GeneralDomainNumber.setStatus("current")
_AxsOspfv3RouterId_Type = RouterID
_AxsOspfv3RouterId_Object = MibTableColumn
axsOspfv3RouterId = _AxsOspfv3RouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 2),
    _AxsOspfv3RouterId_Type()
)
axsOspfv3RouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3RouterId.setStatus("current")
_AxsOspfv3AdminStat_Type = Status
_AxsOspfv3AdminStat_Object = MibTableColumn
axsOspfv3AdminStat = _AxsOspfv3AdminStat_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 3),
    _AxsOspfv3AdminStat_Type()
)
axsOspfv3AdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AdminStat.setStatus("current")


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
    axsOspfv3VersionNumber.setStatus("current")
_AxsOspfv3AreaBdrRtrStatus_Type = TruthValue
_AxsOspfv3AreaBdrRtrStatus_Object = MibTableColumn
axsOspfv3AreaBdrRtrStatus = _AxsOspfv3AreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 5),
    _AxsOspfv3AreaBdrRtrStatus_Type()
)
axsOspfv3AreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaBdrRtrStatus.setStatus("current")
_AxsOspfv3ASBdrRtrStatus_Type = TruthValue
_AxsOspfv3ASBdrRtrStatus_Object = MibTableColumn
axsOspfv3ASBdrRtrStatus = _AxsOspfv3ASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 6),
    _AxsOspfv3ASBdrRtrStatus_Type()
)
axsOspfv3ASBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3ASBdrRtrStatus.setStatus("current")
_AxsOspfv3AsScopeLsaCount_Type = Gauge32
_AxsOspfv3AsScopeLsaCount_Object = MibTableColumn
axsOspfv3AsScopeLsaCount = _AxsOspfv3AsScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 7),
    _AxsOspfv3AsScopeLsaCount_Type()
)
axsOspfv3AsScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsScopeLsaCount.setStatus("current")
_AxsOspfv3AsScopeLsaCksumSum_Type = Integer32
_AxsOspfv3AsScopeLsaCksumSum_Object = MibTableColumn
axsOspfv3AsScopeLsaCksumSum = _AxsOspfv3AsScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 8),
    _AxsOspfv3AsScopeLsaCksumSum_Type()
)
axsOspfv3AsScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsScopeLsaCksumSum.setStatus("current")
_AxsOspfv3OriginateNewLsas_Type = Counter32
_AxsOspfv3OriginateNewLsas_Object = MibTableColumn
axsOspfv3OriginateNewLsas = _AxsOspfv3OriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 9),
    _AxsOspfv3OriginateNewLsas_Type()
)
axsOspfv3OriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3OriginateNewLsas.setStatus("current")
_AxsOspfv3RxNewLsas_Type = Counter32
_AxsOspfv3RxNewLsas_Object = MibTableColumn
axsOspfv3RxNewLsas = _AxsOspfv3RxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 10),
    _AxsOspfv3RxNewLsas_Type()
)
axsOspfv3RxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3RxNewLsas.setStatus("current")


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
    axsOspfv3ExtAreaLsdbLimit.setStatus("current")


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
    axsOspfv3MulticastExtensions.setStatus("current")
_AxsOspfv3DemandExtensions_Type = TruthValue
_AxsOspfv3DemandExtensions_Object = MibTableColumn
axsOspfv3DemandExtensions = _AxsOspfv3DemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 14),
    _AxsOspfv3DemandExtensions_Type()
)
axsOspfv3DemandExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3DemandExtensions.setStatus("current")
_AxsOspfv3TrafficEngineeringSupport_Type = TruthValue
_AxsOspfv3TrafficEngineeringSupport_Object = MibTableColumn
axsOspfv3TrafficEngineeringSupport = _AxsOspfv3TrafficEngineeringSupport_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 1, 1, 15),
    _AxsOspfv3TrafficEngineeringSupport_Type()
)
axsOspfv3TrafficEngineeringSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3TrafficEngineeringSupport.setStatus("current")
_AxsOspfv3AreaTable_Object = MibTable
axsOspfv3AreaTable = _AxsOspfv3AreaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2)
)
if mibBuilder.loadTexts:
    axsOspfv3AreaTable.setStatus("current")
_AxsOspfv3AreaEntry_Object = MibTableRow
axsOspfv3AreaEntry = _AxsOspfv3AreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1)
)
axsOspfv3AreaEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3AreaId"),
)
if mibBuilder.loadTexts:
    axsOspfv3AreaEntry.setStatus("current")
_AxsOspfv3AreaDomainNumber_Type = Integer32
_AxsOspfv3AreaDomainNumber_Object = MibTableColumn
axsOspfv3AreaDomainNumber = _AxsOspfv3AreaDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 1),
    _AxsOspfv3AreaDomainNumber_Type()
)
axsOspfv3AreaDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaDomainNumber.setStatus("current")
_AxsOspfv3AreaId_Type = AreaID
_AxsOspfv3AreaId_Object = MibTableColumn
axsOspfv3AreaId = _AxsOspfv3AreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 2),
    _AxsOspfv3AreaId_Type()
)
axsOspfv3AreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaId.setStatus("current")


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
    axsOspfv3ImportAsExtern.setStatus("current")
_AxsOspfv3SpfRuns_Type = Counter32
_AxsOspfv3SpfRuns_Object = MibTableColumn
axsOspfv3SpfRuns = _AxsOspfv3SpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 4),
    _AxsOspfv3SpfRuns_Type()
)
axsOspfv3SpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3SpfRuns.setStatus("current")
_AxsOspfv3AreaBdrRtrCount_Type = Gauge32
_AxsOspfv3AreaBdrRtrCount_Object = MibTableColumn
axsOspfv3AreaBdrRtrCount = _AxsOspfv3AreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 5),
    _AxsOspfv3AreaBdrRtrCount_Type()
)
axsOspfv3AreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaBdrRtrCount.setStatus("current")
_AxsOspfv3AsBdrRtrCount_Type = Gauge32
_AxsOspfv3AsBdrRtrCount_Object = MibTableColumn
axsOspfv3AsBdrRtrCount = _AxsOspfv3AsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 6),
    _AxsOspfv3AsBdrRtrCount_Type()
)
axsOspfv3AsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsBdrRtrCount.setStatus("current")
_AxsOspfv3AreaScopeLsaCount_Type = Gauge32
_AxsOspfv3AreaScopeLsaCount_Object = MibTableColumn
axsOspfv3AreaScopeLsaCount = _AxsOspfv3AreaScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 7),
    _AxsOspfv3AreaScopeLsaCount_Type()
)
axsOspfv3AreaScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaScopeLsaCount.setStatus("current")


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
    axsOspfv3AreaScopeLsaCksumSum.setStatus("current")


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
    axsOspfv3AreaSummary.setStatus("current")
_AxsOspfv3AreaStatus_Type = RowStatus
_AxsOspfv3AreaStatus_Object = MibTableColumn
axsOspfv3AreaStatus = _AxsOspfv3AreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 10),
    _AxsOspfv3AreaStatus_Type()
)
axsOspfv3AreaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaStatus.setStatus("current")
_AxsOspfv3StubMetric_Type = BigMetric
_AxsOspfv3StubMetric_Object = MibTableColumn
axsOspfv3StubMetric = _AxsOspfv3StubMetric_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 2, 1, 11),
    _AxsOspfv3StubMetric_Type()
)
axsOspfv3StubMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3StubMetric.setStatus("current")
_AxsOspfv3AsLsdbTable_Object = MibTable
axsOspfv3AsLsdbTable = _AxsOspfv3AsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3)
)
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbTable.setStatus("current")
_AxsOspfv3AsLsdbEntry_Object = MibTableRow
axsOspfv3AsLsdbEntry = _AxsOspfv3AsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1)
)
axsOspfv3AsLsdbEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3AsLsdbType"),
    (0, "AX1230S", "axsOspfv3AsLsdbRouterId"),
    (0, "AX1230S", "axsOspfv3AsLsdbLsid"),
)
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbEntry.setStatus("current")
_AxsOspfv3AsLsdbDomainNumber_Type = Integer32
_AxsOspfv3AsLsdbDomainNumber_Object = MibTableColumn
axsOspfv3AsLsdbDomainNumber = _AxsOspfv3AsLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 1),
    _AxsOspfv3AsLsdbDomainNumber_Type()
)
axsOspfv3AsLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbDomainNumber.setStatus("current")


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
    axsOspfv3AsLsdbType.setStatus("current")
_AxsOspfv3AsLsdbRouterId_Type = RouterID
_AxsOspfv3AsLsdbRouterId_Object = MibTableColumn
axsOspfv3AsLsdbRouterId = _AxsOspfv3AsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 3),
    _AxsOspfv3AsLsdbRouterId_Type()
)
axsOspfv3AsLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbRouterId.setStatus("current")
_AxsOspfv3AsLsdbLsid_Type = IpAddress
_AxsOspfv3AsLsdbLsid_Object = MibTableColumn
axsOspfv3AsLsdbLsid = _AxsOspfv3AsLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 4),
    _AxsOspfv3AsLsdbLsid_Type()
)
axsOspfv3AsLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbLsid.setStatus("current")
_AxsOspfv3AsLsdbSequence_Type = Integer32
_AxsOspfv3AsLsdbSequence_Object = MibTableColumn
axsOspfv3AsLsdbSequence = _AxsOspfv3AsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 5),
    _AxsOspfv3AsLsdbSequence_Type()
)
axsOspfv3AsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbSequence.setStatus("current")
_AxsOspfv3AsLsdbAge_Type = Integer32
_AxsOspfv3AsLsdbAge_Object = MibTableColumn
axsOspfv3AsLsdbAge = _AxsOspfv3AsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 6),
    _AxsOspfv3AsLsdbAge_Type()
)
axsOspfv3AsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbAge.setStatus("current")
_AxsOspfv3AsLsdbChecksum_Type = Integer32
_AxsOspfv3AsLsdbChecksum_Object = MibTableColumn
axsOspfv3AsLsdbChecksum = _AxsOspfv3AsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 3, 1, 7),
    _AxsOspfv3AsLsdbChecksum_Type()
)
axsOspfv3AsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AsLsdbChecksum.setStatus("current")


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
    axsOspfv3AsLsdbAdvertisement.setStatus("current")
_AxsOspfv3AreaLsdbTable_Object = MibTable
axsOspfv3AreaLsdbTable = _AxsOspfv3AreaLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4)
)
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbTable.setStatus("current")
_AxsOspfv3AreaLsdbEntry_Object = MibTableRow
axsOspfv3AreaLsdbEntry = _AxsOspfv3AreaLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1)
)
axsOspfv3AreaLsdbEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3AreaLsdbAreaId"),
    (0, "AX1230S", "axsOspfv3AreaLsdbType"),
    (0, "AX1230S", "axsOspfv3AreaLsdbRouterId"),
    (0, "AX1230S", "axsOspfv3AreaLsdbLsid"),
)
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbEntry.setStatus("current")
_AxsOspfv3AreaLsdbDomainNumber_Type = Integer32
_AxsOspfv3AreaLsdbDomainNumber_Object = MibTableColumn
axsOspfv3AreaLsdbDomainNumber = _AxsOspfv3AreaLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 1),
    _AxsOspfv3AreaLsdbDomainNumber_Type()
)
axsOspfv3AreaLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbDomainNumber.setStatus("current")
_AxsOspfv3AreaLsdbAreaId_Type = AreaID
_AxsOspfv3AreaLsdbAreaId_Object = MibTableColumn
axsOspfv3AreaLsdbAreaId = _AxsOspfv3AreaLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 2),
    _AxsOspfv3AreaLsdbAreaId_Type()
)
axsOspfv3AreaLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbAreaId.setStatus("current")


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
    axsOspfv3AreaLsdbType.setStatus("current")
_AxsOspfv3AreaLsdbRouterId_Type = RouterID
_AxsOspfv3AreaLsdbRouterId_Object = MibTableColumn
axsOspfv3AreaLsdbRouterId = _AxsOspfv3AreaLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 4),
    _AxsOspfv3AreaLsdbRouterId_Type()
)
axsOspfv3AreaLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbRouterId.setStatus("current")
_AxsOspfv3AreaLsdbLsid_Type = IpAddress
_AxsOspfv3AreaLsdbLsid_Object = MibTableColumn
axsOspfv3AreaLsdbLsid = _AxsOspfv3AreaLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 5),
    _AxsOspfv3AreaLsdbLsid_Type()
)
axsOspfv3AreaLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbLsid.setStatus("current")
_AxsOspfv3AreaLsdbSequence_Type = Integer32
_AxsOspfv3AreaLsdbSequence_Object = MibTableColumn
axsOspfv3AreaLsdbSequence = _AxsOspfv3AreaLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 6),
    _AxsOspfv3AreaLsdbSequence_Type()
)
axsOspfv3AreaLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbSequence.setStatus("current")
_AxsOspfv3AreaLsdbAge_Type = Integer32
_AxsOspfv3AreaLsdbAge_Object = MibTableColumn
axsOspfv3AreaLsdbAge = _AxsOspfv3AreaLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 7),
    _AxsOspfv3AreaLsdbAge_Type()
)
axsOspfv3AreaLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbAge.setStatus("current")
_AxsOspfv3AreaLsdbChecksum_Type = Integer32
_AxsOspfv3AreaLsdbChecksum_Object = MibTableColumn
axsOspfv3AreaLsdbChecksum = _AxsOspfv3AreaLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 4, 1, 8),
    _AxsOspfv3AreaLsdbChecksum_Type()
)
axsOspfv3AreaLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaLsdbChecksum.setStatus("current")


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
    axsOspfv3AreaLsdbAdvertisement.setStatus("current")
_AxsOspfv3LinkLsdbTable_Object = MibTable
axsOspfv3LinkLsdbTable = _AxsOspfv3LinkLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5)
)
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbTable.setStatus("current")
_AxsOspfv3LinkLsdbEntry_Object = MibTableRow
axsOspfv3LinkLsdbEntry = _AxsOspfv3LinkLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1)
)
axsOspfv3LinkLsdbEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3LinkLsdbIfIndex"),
    (0, "AX1230S", "axsOspfv3LinkLsdbType"),
    (0, "AX1230S", "axsOspfv3LinkLsdbRouterId"),
    (0, "AX1230S", "axsOspfv3LinkLsdbLsid"),
)
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbEntry.setStatus("current")
_AxsOspfv3LinkLsdbDomainNumber_Type = Integer32
_AxsOspfv3LinkLsdbDomainNumber_Object = MibTableColumn
axsOspfv3LinkLsdbDomainNumber = _AxsOspfv3LinkLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 1),
    _AxsOspfv3LinkLsdbDomainNumber_Type()
)
axsOspfv3LinkLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbDomainNumber.setStatus("current")
_AxsOspfv3LinkLsdbIfIndex_Type = Ipv6IfIndex
_AxsOspfv3LinkLsdbIfIndex_Object = MibTableColumn
axsOspfv3LinkLsdbIfIndex = _AxsOspfv3LinkLsdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 2),
    _AxsOspfv3LinkLsdbIfIndex_Type()
)
axsOspfv3LinkLsdbIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbIfIndex.setStatus("current")


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
    axsOspfv3LinkLsdbType.setStatus("current")
_AxsOspfv3LinkLsdbRouterId_Type = RouterID
_AxsOspfv3LinkLsdbRouterId_Object = MibTableColumn
axsOspfv3LinkLsdbRouterId = _AxsOspfv3LinkLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 4),
    _AxsOspfv3LinkLsdbRouterId_Type()
)
axsOspfv3LinkLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbRouterId.setStatus("current")
_AxsOspfv3LinkLsdbLsid_Type = IpAddress
_AxsOspfv3LinkLsdbLsid_Object = MibTableColumn
axsOspfv3LinkLsdbLsid = _AxsOspfv3LinkLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 5),
    _AxsOspfv3LinkLsdbLsid_Type()
)
axsOspfv3LinkLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbLsid.setStatus("current")
_AxsOspfv3LinkLsdbSequence_Type = Integer32
_AxsOspfv3LinkLsdbSequence_Object = MibTableColumn
axsOspfv3LinkLsdbSequence = _AxsOspfv3LinkLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 6),
    _AxsOspfv3LinkLsdbSequence_Type()
)
axsOspfv3LinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbSequence.setStatus("current")
_AxsOspfv3LinkLsdbAge_Type = Integer32
_AxsOspfv3LinkLsdbAge_Object = MibTableColumn
axsOspfv3LinkLsdbAge = _AxsOspfv3LinkLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 7),
    _AxsOspfv3LinkLsdbAge_Type()
)
axsOspfv3LinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbAge.setStatus("current")
_AxsOspfv3LinkLsdbChecksum_Type = Integer32
_AxsOspfv3LinkLsdbChecksum_Object = MibTableColumn
axsOspfv3LinkLsdbChecksum = _AxsOspfv3LinkLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 5, 1, 8),
    _AxsOspfv3LinkLsdbChecksum_Type()
)
axsOspfv3LinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3LinkLsdbChecksum.setStatus("current")


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
    axsOspfv3LinkLsdbAdvertisement.setStatus("current")
_AxsOspfv3IfTable_Object = MibTable
axsOspfv3IfTable = _AxsOspfv3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7)
)
if mibBuilder.loadTexts:
    axsOspfv3IfTable.setStatus("current")
_AxsOspfv3IfEntry_Object = MibTableRow
axsOspfv3IfEntry = _AxsOspfv3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1)
)
axsOspfv3IfEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3IfIndex"),
)
if mibBuilder.loadTexts:
    axsOspfv3IfEntry.setStatus("current")
_AxsOspfv3IfDomainNumber_Type = Integer32
_AxsOspfv3IfDomainNumber_Object = MibTableColumn
axsOspfv3IfDomainNumber = _AxsOspfv3IfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 1),
    _AxsOspfv3IfDomainNumber_Type()
)
axsOspfv3IfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfDomainNumber.setStatus("current")
_AxsOspfv3IfIndex_Type = Ipv6IfIndex
_AxsOspfv3IfIndex_Object = MibTableColumn
axsOspfv3IfIndex = _AxsOspfv3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 2),
    _AxsOspfv3IfIndex_Type()
)
axsOspfv3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfIndex.setStatus("current")


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
    axsOspfv3IfAreaId.setStatus("current")


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
    axsOspfv3IfType.setStatus("current")


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
    axsOspfv3IfAdminStat.setStatus("current")


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
    axsOspfv3IfRtrPriority.setStatus("current")


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
    axsOspfv3IfTransitDelay.setStatus("current")


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
    axsOspfv3IfRetransInterval.setStatus("current")


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
    axsOspfv3IfHelloInterval.setStatus("current")


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
    axsOspfv3IfRtrDeadInterval.setStatus("current")


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
    axsOspfv3IfPollInterval.setStatus("current")


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
    axsOspfv3IfState.setStatus("current")


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
    axsOspfv3IfDesignatedRouter.setStatus("current")


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
    axsOspfv3IfBackupDesignatedRouter.setStatus("current")
_AxsOspfv3IfEvents_Type = Counter32
_AxsOspfv3IfEvents_Object = MibTableColumn
axsOspfv3IfEvents = _AxsOspfv3IfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 16),
    _AxsOspfv3IfEvents_Type()
)
axsOspfv3IfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfEvents.setStatus("current")
_AxsOspfv3IfStatus_Type = RowStatus
_AxsOspfv3IfStatus_Object = MibTableColumn
axsOspfv3IfStatus = _AxsOspfv3IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 18),
    _AxsOspfv3IfStatus_Type()
)
axsOspfv3IfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfStatus.setStatus("current")


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
    axsOspfv3IfMulticastForwarding.setStatus("current")


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
    axsOspfv3IfDemand.setStatus("current")
_AxsOspfv3IfMetricValue_Type = Metric
_AxsOspfv3IfMetricValue_Object = MibTableColumn
axsOspfv3IfMetricValue = _AxsOspfv3IfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 21),
    _AxsOspfv3IfMetricValue_Type()
)
axsOspfv3IfMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfMetricValue.setStatus("current")
_AxsOspfv3IfLinkScopeLsaCount_Type = Gauge32
_AxsOspfv3IfLinkScopeLsaCount_Object = MibTableColumn
axsOspfv3IfLinkScopeLsaCount = _AxsOspfv3IfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 7, 1, 22),
    _AxsOspfv3IfLinkScopeLsaCount_Type()
)
axsOspfv3IfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3IfLinkScopeLsaCount.setStatus("current")


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
    axsOspfv3IfLinkLsaCksumSum.setStatus("current")


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
    axsOspfv3IfInstId.setStatus("current")
_AxsOspfv3VirtIfTable_Object = MibTable
axsOspfv3VirtIfTable = _AxsOspfv3VirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8)
)
if mibBuilder.loadTexts:
    axsOspfv3VirtIfTable.setStatus("current")
_AxsOspfv3VirtIfEntry_Object = MibTableRow
axsOspfv3VirtIfEntry = _AxsOspfv3VirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1)
)
axsOspfv3VirtIfEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3VirtIfAreaId"),
    (0, "AX1230S", "axsOspfv3VirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    axsOspfv3VirtIfEntry.setStatus("current")
_AxsOspfv3VirtIfDomainNumber_Type = Integer32
_AxsOspfv3VirtIfDomainNumber_Object = MibTableColumn
axsOspfv3VirtIfDomainNumber = _AxsOspfv3VirtIfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 1),
    _AxsOspfv3VirtIfDomainNumber_Type()
)
axsOspfv3VirtIfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfDomainNumber.setStatus("current")
_AxsOspfv3VirtIfAreaId_Type = AreaID
_AxsOspfv3VirtIfAreaId_Object = MibTableColumn
axsOspfv3VirtIfAreaId = _AxsOspfv3VirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 2),
    _AxsOspfv3VirtIfAreaId_Type()
)
axsOspfv3VirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfAreaId.setStatus("current")
_AxsOspfv3VirtIfNeighbor_Type = RouterID
_AxsOspfv3VirtIfNeighbor_Object = MibTableColumn
axsOspfv3VirtIfNeighbor = _AxsOspfv3VirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 3),
    _AxsOspfv3VirtIfNeighbor_Type()
)
axsOspfv3VirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfNeighbor.setStatus("current")
_AxsOspfv3VirtIfIndex_Type = Ipv6IfIndex
_AxsOspfv3VirtIfIndex_Object = MibTableColumn
axsOspfv3VirtIfIndex = _AxsOspfv3VirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 4),
    _AxsOspfv3VirtIfIndex_Type()
)
axsOspfv3VirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfIndex.setStatus("current")


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
    axsOspfv3VirtIfTransitDelay.setStatus("current")


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
    axsOspfv3VirtIfRetransInterval.setStatus("current")


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
    axsOspfv3VirtIfHelloInterval.setStatus("current")


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
    axsOspfv3VirtIfRtrDeadInterval.setStatus("current")


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
    axsOspfv3VirtIfState.setStatus("current")
_AxsOspfv3VirtIfEvents_Type = Counter32
_AxsOspfv3VirtIfEvents_Object = MibTableColumn
axsOspfv3VirtIfEvents = _AxsOspfv3VirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 10),
    _AxsOspfv3VirtIfEvents_Type()
)
axsOspfv3VirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfEvents.setStatus("current")
_AxsOspfv3VirtIfStatus_Type = RowStatus
_AxsOspfv3VirtIfStatus_Object = MibTableColumn
axsOspfv3VirtIfStatus = _AxsOspfv3VirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 11),
    _AxsOspfv3VirtIfStatus_Type()
)
axsOspfv3VirtIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfStatus.setStatus("current")
_AxsOspfv3VirtIfLinkScopeLsaCount_Type = Gauge32
_AxsOspfv3VirtIfLinkScopeLsaCount_Object = MibTableColumn
axsOspfv3VirtIfLinkScopeLsaCount = _AxsOspfv3VirtIfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 8, 1, 12),
    _AxsOspfv3VirtIfLinkScopeLsaCount_Type()
)
axsOspfv3VirtIfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtIfLinkScopeLsaCount.setStatus("current")


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
    axsOspfv3VirtIfLinkLsaCksumSum.setStatus("current")
_AxsOspfv3NbrTable_Object = MibTable
axsOspfv3NbrTable = _AxsOspfv3NbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9)
)
if mibBuilder.loadTexts:
    axsOspfv3NbrTable.setStatus("current")
_AxsOspfv3NbrEntry_Object = MibTableRow
axsOspfv3NbrEntry = _AxsOspfv3NbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1)
)
axsOspfv3NbrEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3NbrIfIndex"),
    (0, "AX1230S", "axsOspfv3NbrIpv6Addr"),
)
if mibBuilder.loadTexts:
    axsOspfv3NbrEntry.setStatus("current")
_AxsOspfv3NbrDomainNumber_Type = Integer32
_AxsOspfv3NbrDomainNumber_Object = MibTableColumn
axsOspfv3NbrDomainNumber = _AxsOspfv3NbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 1),
    _AxsOspfv3NbrDomainNumber_Type()
)
axsOspfv3NbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrDomainNumber.setStatus("current")
_AxsOspfv3NbrIfIndex_Type = Ipv6IfIndex
_AxsOspfv3NbrIfIndex_Object = MibTableColumn
axsOspfv3NbrIfIndex = _AxsOspfv3NbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 2),
    _AxsOspfv3NbrIfIndex_Type()
)
axsOspfv3NbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrIfIndex.setStatus("current")
_AxsOspfv3NbrIpv6Addr_Type = Ipv6Address
_AxsOspfv3NbrIpv6Addr_Object = MibTableColumn
axsOspfv3NbrIpv6Addr = _AxsOspfv3NbrIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 3),
    _AxsOspfv3NbrIpv6Addr_Type()
)
axsOspfv3NbrIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrIpv6Addr.setStatus("current")
_AxsOspfv3NbrRtrId_Type = RouterID
_AxsOspfv3NbrRtrId_Object = MibTableColumn
axsOspfv3NbrRtrId = _AxsOspfv3NbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 4),
    _AxsOspfv3NbrRtrId_Type()
)
axsOspfv3NbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrRtrId.setStatus("current")


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
    axsOspfv3NbrOptions.setStatus("current")


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
    axsOspfv3NbrPriority.setStatus("current")


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
    axsOspfv3NbrState.setStatus("current")
_AxsOspfv3NbrEvents_Type = Counter32
_AxsOspfv3NbrEvents_Object = MibTableColumn
axsOspfv3NbrEvents = _AxsOspfv3NbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 8),
    _AxsOspfv3NbrEvents_Type()
)
axsOspfv3NbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrEvents.setStatus("current")
_AxsOspfv3NbrLsRetransQLen_Type = Gauge32
_AxsOspfv3NbrLsRetransQLen_Object = MibTableColumn
axsOspfv3NbrLsRetransQLen = _AxsOspfv3NbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 9),
    _AxsOspfv3NbrLsRetransQLen_Type()
)
axsOspfv3NbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrLsRetransQLen.setStatus("current")
_AxsOspfv3NbrHelloSuppressed_Type = TruthValue
_AxsOspfv3NbrHelloSuppressed_Object = MibTableColumn
axsOspfv3NbrHelloSuppressed = _AxsOspfv3NbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 12),
    _AxsOspfv3NbrHelloSuppressed_Type()
)
axsOspfv3NbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrHelloSuppressed.setStatus("current")
_AxsOspfv3NbrIfId_Type = Ipv6IfIndex
_AxsOspfv3NbrIfId_Object = MibTableColumn
axsOspfv3NbrIfId = _AxsOspfv3NbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 9, 1, 13),
    _AxsOspfv3NbrIfId_Type()
)
axsOspfv3NbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3NbrIfId.setStatus("current")
_AxsOspfv3VirtNbrTable_Object = MibTable
axsOspfv3VirtNbrTable = _AxsOspfv3VirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10)
)
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrTable.setStatus("current")
_AxsOspfv3VirtNbrEntry_Object = MibTableRow
axsOspfv3VirtNbrEntry = _AxsOspfv3VirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1)
)
axsOspfv3VirtNbrEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3VirtNbrArea"),
    (0, "AX1230S", "axsOspfv3VirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrEntry.setStatus("current")
_AxsOspfv3VirtNbrDomainNumber_Type = Integer32
_AxsOspfv3VirtNbrDomainNumber_Object = MibTableColumn
axsOspfv3VirtNbrDomainNumber = _AxsOspfv3VirtNbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 1),
    _AxsOspfv3VirtNbrDomainNumber_Type()
)
axsOspfv3VirtNbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrDomainNumber.setStatus("current")
_AxsOspfv3VirtNbrArea_Type = AreaID
_AxsOspfv3VirtNbrArea_Object = MibTableColumn
axsOspfv3VirtNbrArea = _AxsOspfv3VirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 2),
    _AxsOspfv3VirtNbrArea_Type()
)
axsOspfv3VirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrArea.setStatus("current")
_AxsOspfv3VirtNbrRtrId_Type = RouterID
_AxsOspfv3VirtNbrRtrId_Object = MibTableColumn
axsOspfv3VirtNbrRtrId = _AxsOspfv3VirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 3),
    _AxsOspfv3VirtNbrRtrId_Type()
)
axsOspfv3VirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrRtrId.setStatus("current")
_AxsOspfv3VirtNbrIfIndex_Type = Ipv6IfIndex
_AxsOspfv3VirtNbrIfIndex_Object = MibTableColumn
axsOspfv3VirtNbrIfIndex = _AxsOspfv3VirtNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 4),
    _AxsOspfv3VirtNbrIfIndex_Type()
)
axsOspfv3VirtNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrIfIndex.setStatus("current")
_AxsOspfv3VirtNbrIpv6Addr_Type = Ipv6Address
_AxsOspfv3VirtNbrIpv6Addr_Object = MibTableColumn
axsOspfv3VirtNbrIpv6Addr = _AxsOspfv3VirtNbrIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 5),
    _AxsOspfv3VirtNbrIpv6Addr_Type()
)
axsOspfv3VirtNbrIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrIpv6Addr.setStatus("current")
_AxsOspfv3VirtNbrOptions_Type = Integer32
_AxsOspfv3VirtNbrOptions_Object = MibTableColumn
axsOspfv3VirtNbrOptions = _AxsOspfv3VirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 6),
    _AxsOspfv3VirtNbrOptions_Type()
)
axsOspfv3VirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrOptions.setStatus("current")


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
    axsOspfv3VirtNbrState.setStatus("current")
_AxsOspfv3VirtNbrEvents_Type = Counter32
_AxsOspfv3VirtNbrEvents_Object = MibTableColumn
axsOspfv3VirtNbrEvents = _AxsOspfv3VirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 8),
    _AxsOspfv3VirtNbrEvents_Type()
)
axsOspfv3VirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrEvents.setStatus("current")
_AxsOspfv3VirtNbrLsRetransQLen_Type = Gauge32
_AxsOspfv3VirtNbrLsRetransQLen_Object = MibTableColumn
axsOspfv3VirtNbrLsRetransQLen = _AxsOspfv3VirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 9),
    _AxsOspfv3VirtNbrLsRetransQLen_Type()
)
axsOspfv3VirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrLsRetransQLen.setStatus("current")
_AxsOspfv3VirtNbrHelloSuppressed_Type = TruthValue
_AxsOspfv3VirtNbrHelloSuppressed_Object = MibTableColumn
axsOspfv3VirtNbrHelloSuppressed = _AxsOspfv3VirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 10),
    _AxsOspfv3VirtNbrHelloSuppressed_Type()
)
axsOspfv3VirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrHelloSuppressed.setStatus("current")
_AxsOspfv3VirtNbrIfId_Type = Ipv6IfIndex
_AxsOspfv3VirtNbrIfId_Object = MibTableColumn
axsOspfv3VirtNbrIfId = _AxsOspfv3VirtNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 10, 1, 11),
    _AxsOspfv3VirtNbrIfId_Type()
)
axsOspfv3VirtNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3VirtNbrIfId.setStatus("current")
_AxsOspfv3AreaAggregateTable_Object = MibTable
axsOspfv3AreaAggregateTable = _AxsOspfv3AreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11)
)
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateTable.setStatus("current")
_AxsOspfv3AreaAggregateEntry_Object = MibTableRow
axsOspfv3AreaAggregateEntry = _AxsOspfv3AreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1)
)
axsOspfv3AreaAggregateEntry.setIndexNames(
    (0, "AX1230S", "axsOspfv3AreaAggregateAreaID"),
    (0, "AX1230S", "axsOspfv3AreaAggregateAreaLsdbType"),
    (0, "AX1230S", "axsOspfv3AreaAggregateIndex"),
)
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateEntry.setStatus("current")
_AxsOspfv3AreaAggregateDomainNumber_Type = Integer32
_AxsOspfv3AreaAggregateDomainNumber_Object = MibTableColumn
axsOspfv3AreaAggregateDomainNumber = _AxsOspfv3AreaAggregateDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 1),
    _AxsOspfv3AreaAggregateDomainNumber_Type()
)
axsOspfv3AreaAggregateDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateDomainNumber.setStatus("current")
_AxsOspfv3AreaAggregateAreaID_Type = AreaID
_AxsOspfv3AreaAggregateAreaID_Object = MibTableColumn
axsOspfv3AreaAggregateAreaID = _AxsOspfv3AreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 2),
    _AxsOspfv3AreaAggregateAreaID_Type()
)
axsOspfv3AreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateAreaID.setStatus("current")


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
    axsOspfv3AreaAggregateAreaLsdbType.setStatus("current")


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
    axsOspfv3AreaAggregateIndex.setStatus("current")
_AxsOspfv3AreaAggregatePrefix_Type = Ipv6AddressPrefix
_AxsOspfv3AreaAggregatePrefix_Object = MibTableColumn
axsOspfv3AreaAggregatePrefix = _AxsOspfv3AreaAggregatePrefix_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 5),
    _AxsOspfv3AreaAggregatePrefix_Type()
)
axsOspfv3AreaAggregatePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregatePrefix.setStatus("current")


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
    axsOspfv3AreaAggregatePrefixLen.setStatus("current")
_AxsOspfv3AreaAggregateStatus_Type = RowStatus
_AxsOspfv3AreaAggregateStatus_Object = MibTableColumn
axsOspfv3AreaAggregateStatus = _AxsOspfv3AreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 15, 11, 1, 7),
    _AxsOspfv3AreaAggregateStatus_Type()
)
axsOspfv3AreaAggregateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsOspfv3AreaAggregateStatus.setStatus("current")


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
    axsOspfv3AreaAggregateEffect.setStatus("current")
_AxsStatic_ObjectIdentity = ObjectIdentity
axsStatic = _AxsStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38)
)
_AxsStaticTable_Object = MibTable
axsStaticTable = _AxsStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 1)
)
if mibBuilder.loadTexts:
    axsStaticTable.setStatus("current")
_AxsStaticGatewayEntry_Object = MibTableRow
axsStaticGatewayEntry = _AxsStaticGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 1, 1)
)
axsStaticGatewayEntry.setIndexNames(
    (0, "AX1230S", "axsStaticGatewayAddr"),
)
if mibBuilder.loadTexts:
    axsStaticGatewayEntry.setStatus("current")
_AxsStaticGatewayAddr_Type = IpAddress
_AxsStaticGatewayAddr_Object = MibTableColumn
axsStaticGatewayAddr = _AxsStaticGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 1, 1, 1),
    _AxsStaticGatewayAddr_Type()
)
axsStaticGatewayAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStaticGatewayAddr.setStatus("current")
_AxsStaticGatewayState_Type = Integer32
_AxsStaticGatewayState_Object = MibTableColumn
axsStaticGatewayState = _AxsStaticGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 1, 1, 2),
    _AxsStaticGatewayState_Type()
)
axsStaticGatewayState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStaticGatewayState.setStatus("current")
_AxsStaticTraps_ObjectIdentity = ObjectIdentity
axsStaticTraps = _AxsStaticTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 2)
)
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("power-on", 1),
          ("reload", 2),
          ("system-fault", 3),
          ("system-stall", 4),
          ("reset", 5),
          ("fail-over", 6),
          ("default-restart", 7))
    )


_AxsBootReason_Type.__name__ = "Integer32"
_AxsBootReason_Object = MibScalar
axsBootReason = _AxsBootReason_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 51, 1),
    _AxsBootReason_Type()
)
axsBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsBootReason.setStatus("current")
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
    axsLoginName.setStatus("current")
_AxsLoginTime_Type = DisplayString
_AxsLoginTime_Object = MibScalar
axsLoginTime = _AxsLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 2),
    _AxsLoginTime_Type()
)
axsLoginTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLoginTime.setStatus("current")
_AxsLogoutTime_Type = DisplayString
_AxsLogoutTime_Object = MibScalar
axsLogoutTime = _AxsLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 3),
    _AxsLogoutTime_Type()
)
axsLogoutTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLogoutTime.setStatus("current")
_AxsLoginFailureTime_Type = DisplayString
_AxsLoginFailureTime_Object = MibScalar
axsLoginFailureTime = _AxsLoginFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 4),
    _AxsLoginFailureTime_Type()
)
axsLoginFailureTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLoginFailureTime.setStatus("current")
_AxsLoginLocation_Type = DisplayString
_AxsLoginLocation_Object = MibScalar
axsLoginLocation = _AxsLoginLocation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 5),
    _AxsLoginLocation_Type()
)
axsLoginLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLoginLocation.setStatus("current")
_AxsLoginLine_Type = DisplayString
_AxsLoginLine_Object = MibScalar
axsLoginLine = _AxsLoginLine_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 52, 6),
    _AxsLoginLine_Type()
)
axsLoginLine.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsLoginLine.setStatus("current")


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
    axsLogoutStatus.setStatus("current")
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
    axslldpMessageTxInterval.setStatus("current")
_AxslldpMessageTxHoldMultiplier_Type = Integer32
_AxslldpMessageTxHoldMultiplier_Object = MibScalar
axslldpMessageTxHoldMultiplier = _AxslldpMessageTxHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 2),
    _AxslldpMessageTxHoldMultiplier_Type()
)
axslldpMessageTxHoldMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpMessageTxHoldMultiplier.setStatus("current")
_AxslldpPortConfigTable_Object = MibTable
axslldpPortConfigTable = _AxslldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6)
)
if mibBuilder.loadTexts:
    axslldpPortConfigTable.setStatus("current")
_AxslldpPortConfigEntry_Object = MibTableRow
axslldpPortConfigEntry = _AxslldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6, 1)
)
axslldpPortConfigEntry.setIndexNames(
    (0, "AX1230S", "axslldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    axslldpPortConfigEntry.setStatus("current")
_AxslldpPortConfigPortNum_Type = Integer32
_AxslldpPortConfigPortNum_Object = MibTableColumn
axslldpPortConfigPortNum = _AxslldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6, 1, 2),
    _AxslldpPortConfigPortNum_Type()
)
axslldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpPortConfigPortNum.setStatus("current")


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
    axslldpPortConfigAdminStatus.setStatus("current")


class _AxslldpPortConfigTLVsTxEnable_Type(Bits):
    """Custom type axslldpPortConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("foo0", 0),
          ("foo1", 1),
          ("foo2", 2),
          ("foo3", 3),
          ("portDesc", 4),
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
    axslldpPortConfigTLVsTxEnable.setStatus("current")
_AxslldpPortConfigRowStatus_Type = RowStatus
_AxslldpPortConfigRowStatus_Object = MibTableColumn
axslldpPortConfigRowStatus = _AxslldpPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 1, 6, 1, 5),
    _AxslldpPortConfigRowStatus_Type()
)
axslldpPortConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpPortConfigRowStatus.setStatus("current")
_AxslldpStats_ObjectIdentity = ObjectIdentity
axslldpStats = _AxslldpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2)
)
_AxslldpStatsTable_Object = MibTable
axslldpStatsTable = _AxslldpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    axslldpStatsTable.setStatus("current")
_AxslldpStatsEntry_Object = MibTableRow
axslldpStatsEntry = _AxslldpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1)
)
axslldpStatsEntry.setIndexNames(
    (0, "AX1230S", "axslldpStatsPortNum"),
)
if mibBuilder.loadTexts:
    axslldpStatsEntry.setStatus("current")
_AxslldpStatsPortNum_Type = Integer32
_AxslldpStatsPortNum_Object = MibTableColumn
axslldpStatsPortNum = _AxslldpStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 2),
    _AxslldpStatsPortNum_Type()
)
axslldpStatsPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpStatsPortNum.setStatus("current")
_AxslldpStatsOperStatus_Type = Integer32
_AxslldpStatsOperStatus_Object = MibTableColumn
axslldpStatsOperStatus = _AxslldpStatsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 3),
    _AxslldpStatsOperStatus_Type()
)
axslldpStatsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsOperStatus.setStatus("current")
_AxslldpStatsFramesInErrors_Type = Counter32
_AxslldpStatsFramesInErrors_Object = MibTableColumn
axslldpStatsFramesInErrors = _AxslldpStatsFramesInErrors_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 4),
    _AxslldpStatsFramesInErrors_Type()
)
axslldpStatsFramesInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsFramesInErrors.setStatus("current")
_AxslldpStatsFramesInTotal_Type = Counter32
_AxslldpStatsFramesInTotal_Object = MibTableColumn
axslldpStatsFramesInTotal = _AxslldpStatsFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 5),
    _AxslldpStatsFramesInTotal_Type()
)
axslldpStatsFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsFramesInTotal.setStatus("current")
_AxslldpStatsFramesOutTotal_Type = Counter32
_AxslldpStatsFramesOutTotal_Object = MibTableColumn
axslldpStatsFramesOutTotal = _AxslldpStatsFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 6),
    _AxslldpStatsFramesOutTotal_Type()
)
axslldpStatsFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsFramesOutTotal.setStatus("current")
_AxslldpStatsTLVsInErrors_Type = Counter32
_AxslldpStatsTLVsInErrors_Object = MibTableColumn
axslldpStatsTLVsInErrors = _AxslldpStatsTLVsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 7),
    _AxslldpStatsTLVsInErrors_Type()
)
axslldpStatsTLVsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsTLVsInErrors.setStatus("current")
_AxslldpStatsTLVsDiscardedTotal_Type = Counter32
_AxslldpStatsTLVsDiscardedTotal_Object = MibTableColumn
axslldpStatsTLVsDiscardedTotal = _AxslldpStatsTLVsDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 2, 1, 1, 8),
    _AxslldpStatsTLVsDiscardedTotal_Type()
)
axslldpStatsTLVsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpStatsTLVsDiscardedTotal.setStatus("current")
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
    axslldpLocChassisType.setStatus("current")
_AxslldpLocChassisId_Type = OctetString
_AxslldpLocChassisId_Object = MibScalar
axslldpLocChassisId = _AxslldpLocChassisId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 2),
    _AxslldpLocChassisId_Type()
)
axslldpLocChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocChassisId.setStatus("current")
_AxslldpLocSysName_Type = OctetString
_AxslldpLocSysName_Object = MibScalar
axslldpLocSysName = _AxslldpLocSysName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 3),
    _AxslldpLocSysName_Type()
)
axslldpLocSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocSysName.setStatus("current")
_AxslldpLocSysDesc_Type = DisplayString
_AxslldpLocSysDesc_Object = MibScalar
axslldpLocSysDesc = _AxslldpLocSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 4),
    _AxslldpLocSysDesc_Type()
)
axslldpLocSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocSysDesc.setStatus("current")
_AxslldpLocPortTable_Object = MibTable
axslldpLocPortTable = _AxslldpLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7)
)
if mibBuilder.loadTexts:
    axslldpLocPortTable.setStatus("current")
_AxslldpLocPortEntry_Object = MibTableRow
axslldpLocPortEntry = _AxslldpLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7, 1)
)
axslldpLocPortEntry.setIndexNames(
    (0, "AX1230S", "axslldpLocPortNum"),
)
if mibBuilder.loadTexts:
    axslldpLocPortEntry.setStatus("current")
_AxslldpLocPortNum_Type = Integer32
_AxslldpLocPortNum_Object = MibTableColumn
axslldpLocPortNum = _AxslldpLocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7, 1, 1),
    _AxslldpLocPortNum_Type()
)
axslldpLocPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpLocPortNum.setStatus("current")


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
    axslldpLocPortType.setStatus("current")
_AxslldpLocPortId_Type = OctetString
_AxslldpLocPortId_Object = MibTableColumn
axslldpLocPortId = _AxslldpLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7, 1, 3),
    _AxslldpLocPortId_Type()
)
axslldpLocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocPortId.setStatus("current")
_AxslldpLocPortDesc_Type = OctetString
_AxslldpLocPortDesc_Object = MibTableColumn
axslldpLocPortDesc = _AxslldpLocPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 3, 7, 1, 4),
    _AxslldpLocPortDesc_Type()
)
axslldpLocPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpLocPortDesc.setStatus("current")
_AxslldpRemoteSystemData_ObjectIdentity = ObjectIdentity
axslldpRemoteSystemData = _AxslldpRemoteSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4)
)
_AxslldpRemTable_Object = MibTable
axslldpRemTable = _AxslldpRemTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1)
)
if mibBuilder.loadTexts:
    axslldpRemTable.setStatus("current")
_AxslldpRemEntry_Object = MibTableRow
axslldpRemEntry = _AxslldpRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1)
)
axslldpRemEntry.setIndexNames(
    (0, "AX1230S", "axslldpRemLocalPortNum"),
    (0, "AX1230S", "axslldpRemIndex"),
)
if mibBuilder.loadTexts:
    axslldpRemEntry.setStatus("current")
_AxslldpRemLocalPortNum_Type = Integer32
_AxslldpRemLocalPortNum_Object = MibTableColumn
axslldpRemLocalPortNum = _AxslldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 2),
    _AxslldpRemLocalPortNum_Type()
)
axslldpRemLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemLocalPortNum.setStatus("current")
_AxslldpRemIndex_Type = Integer32
_AxslldpRemIndex_Object = MibTableColumn
axslldpRemIndex = _AxslldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 3),
    _AxslldpRemIndex_Type()
)
axslldpRemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemIndex.setStatus("current")


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
    axslldpRemRemoteChassisType.setStatus("current")
_AxslldpRemRemoteChassis_Type = OctetString
_AxslldpRemRemoteChassis_Object = MibTableColumn
axslldpRemRemoteChassis = _AxslldpRemRemoteChassis_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 5),
    _AxslldpRemRemoteChassis_Type()
)
axslldpRemRemoteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemRemoteChassis.setStatus("current")


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
    axslldpRemRemotePortType.setStatus("current")
_AxslldpRemRemotePort_Type = OctetString
_AxslldpRemRemotePort_Object = MibTableColumn
axslldpRemRemotePort = _AxslldpRemRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 7),
    _AxslldpRemRemotePort_Type()
)
axslldpRemRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemRemotePort.setStatus("current")
_AxslldpRemPortDesc_Type = OctetString
_AxslldpRemPortDesc_Object = MibTableColumn
axslldpRemPortDesc = _AxslldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 8),
    _AxslldpRemPortDesc_Type()
)
axslldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemPortDesc.setStatus("current")
_AxslldpRemSysName_Type = OctetString
_AxslldpRemSysName_Object = MibTableColumn
axslldpRemSysName = _AxslldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 9),
    _AxslldpRemSysName_Type()
)
axslldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemSysName.setStatus("current")
_AxslldpRemSysDesc_Type = OctetString
_AxslldpRemSysDesc_Object = MibTableColumn
axslldpRemSysDesc = _AxslldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 10),
    _AxslldpRemSysDesc_Type()
)
axslldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemSysDesc.setStatus("current")
_AxslldpRemoteOriginInfoData_ObjectIdentity = ObjectIdentity
axslldpRemoteOriginInfoData = _AxslldpRemoteOriginInfoData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20)
)
_AxslldpRemOriginInfoTable_Object = MibTable
axslldpRemOriginInfoTable = _AxslldpRemOriginInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1)
)
if mibBuilder.loadTexts:
    axslldpRemOriginInfoTable.setStatus("current")
_AxslldpRemOriginInfoEntry_Object = MibTableRow
axslldpRemOriginInfoEntry = _AxslldpRemOriginInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1)
)
axslldpRemOriginInfoEntry.setIndexNames(
    (0, "AX1230S", "axslldpRemOriginInfoPortNum"),
    (0, "AX1230S", "axslldpRemOriginInfoIndex"),
)
if mibBuilder.loadTexts:
    axslldpRemOriginInfoEntry.setStatus("current")
_AxslldpRemOriginInfoPortNum_Type = Integer32
_AxslldpRemOriginInfoPortNum_Object = MibTableColumn
axslldpRemOriginInfoPortNum = _AxslldpRemOriginInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 1),
    _AxslldpRemOriginInfoPortNum_Type()
)
axslldpRemOriginInfoPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoPortNum.setStatus("current")
_AxslldpRemOriginInfoIndex_Type = Integer32
_AxslldpRemOriginInfoIndex_Object = MibTableColumn
axslldpRemOriginInfoIndex = _AxslldpRemOriginInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 2),
    _AxslldpRemOriginInfoIndex_Type()
)
axslldpRemOriginInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIndex.setStatus("current")
_AxslldpRemOriginInfoLowerVlanList_Type = OctetString
_AxslldpRemOriginInfoLowerVlanList_Object = MibTableColumn
axslldpRemOriginInfoLowerVlanList = _AxslldpRemOriginInfoLowerVlanList_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 3),
    _AxslldpRemOriginInfoLowerVlanList_Type()
)
axslldpRemOriginInfoLowerVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoLowerVlanList.setStatus("current")
_AxslldpRemOriginInfoHigherVlanList_Type = OctetString
_AxslldpRemOriginInfoHigherVlanList_Object = MibTableColumn
axslldpRemOriginInfoHigherVlanList = _AxslldpRemOriginInfoHigherVlanList_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 4),
    _AxslldpRemOriginInfoHigherVlanList_Type()
)
axslldpRemOriginInfoHigherVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoHigherVlanList.setStatus("current")
_AxslldpRemOriginInfoIPv4Address_Type = OctetString
_AxslldpRemOriginInfoIPv4Address_Object = MibTableColumn
axslldpRemOriginInfoIPv4Address = _AxslldpRemOriginInfoIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 5),
    _AxslldpRemOriginInfoIPv4Address_Type()
)
axslldpRemOriginInfoIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv4Address.setStatus("current")
_AxslldpRemOriginInfoIPv4PortType_Type = Integer32
_AxslldpRemOriginInfoIPv4PortType_Object = MibTableColumn
axslldpRemOriginInfoIPv4PortType = _AxslldpRemOriginInfoIPv4PortType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 6),
    _AxslldpRemOriginInfoIPv4PortType_Type()
)
axslldpRemOriginInfoIPv4PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv4PortType.setStatus("current")
_AxslldpRemOriginInfoIPv4VlanId_Type = Integer32
_AxslldpRemOriginInfoIPv4VlanId_Object = MibTableColumn
axslldpRemOriginInfoIPv4VlanId = _AxslldpRemOriginInfoIPv4VlanId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 7),
    _AxslldpRemOriginInfoIPv4VlanId_Type()
)
axslldpRemOriginInfoIPv4VlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv4VlanId.setStatus("current")
_AxslldpRemOriginInfoIPv6Address_Type = OctetString
_AxslldpRemOriginInfoIPv6Address_Object = MibTableColumn
axslldpRemOriginInfoIPv6Address = _AxslldpRemOriginInfoIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 8),
    _AxslldpRemOriginInfoIPv6Address_Type()
)
axslldpRemOriginInfoIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv6Address.setStatus("current")
_AxslldpRemOriginInfoIPv6PortType_Type = Integer32
_AxslldpRemOriginInfoIPv6PortType_Object = MibTableColumn
axslldpRemOriginInfoIPv6PortType = _AxslldpRemOriginInfoIPv6PortType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 9),
    _AxslldpRemOriginInfoIPv6PortType_Type()
)
axslldpRemOriginInfoIPv6PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv6PortType.setStatus("current")
_AxslldpRemOriginInfoIPv6VlanId_Type = Integer32
_AxslldpRemOriginInfoIPv6VlanId_Object = MibTableColumn
axslldpRemOriginInfoIPv6VlanId = _AxslldpRemOriginInfoIPv6VlanId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 20, 1, 1, 10),
    _AxslldpRemOriginInfoIPv6VlanId_Type()
)
axslldpRemOriginInfoIPv6VlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemOriginInfoIPv6VlanId.setStatus("current")
_Ax1230sMib_ObjectIdentity = ObjectIdentity
ax1230sMib = _Ax1230sMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10)
)
_Ax1230sSwitch_ObjectIdentity = ObjectIdentity
ax1230sSwitch = _Ax1230sSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1)
)


class _Ax1230sModelType_Type(Integer32):
    """Custom type ax1230sModelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              300,
              301,
              302)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("model-AX1230S-24T2C", 300),
          ("model-AX1230S-48T2C", 301),
          ("model-AX1230S-24P2C", 302))
    )


_Ax1230sModelType_Type.__name__ = "Integer32"
_Ax1230sModelType_Object = MibScalar
ax1230sModelType = _Ax1230sModelType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 1),
    _Ax1230sModelType_Type()
)
ax1230sModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sModelType.setStatus("current")
_Ax1230sSoftware_ObjectIdentity = ObjectIdentity
ax1230sSoftware = _Ax1230sSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 2)
)


class _Ax1230sSoftwareName_Type(DisplayString):
    """Custom type ax1230sSoftwareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax1230sSoftwareName_Type.__name__ = "DisplayString"
_Ax1230sSoftwareName_Object = MibScalar
ax1230sSoftwareName = _Ax1230sSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 2, 1),
    _Ax1230sSoftwareName_Type()
)
ax1230sSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSoftwareName.setStatus("current")


class _Ax1230sSoftwareAbbreviation_Type(DisplayString):
    """Custom type ax1230sSoftwareAbbreviation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax1230sSoftwareAbbreviation_Type.__name__ = "DisplayString"
_Ax1230sSoftwareAbbreviation_Object = MibScalar
ax1230sSoftwareAbbreviation = _Ax1230sSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 2, 2),
    _Ax1230sSoftwareAbbreviation_Type()
)
ax1230sSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSoftwareAbbreviation.setStatus("current")


class _Ax1230sSoftwareVersion_Type(DisplayString):
    """Custom type ax1230sSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax1230sSoftwareVersion_Type.__name__ = "DisplayString"
_Ax1230sSoftwareVersion_Object = MibScalar
ax1230sSoftwareVersion = _Ax1230sSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 2, 3),
    _Ax1230sSoftwareVersion_Type()
)
ax1230sSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSoftwareVersion.setStatus("current")
_Ax1230sSystemMsg_ObjectIdentity = ObjectIdentity
ax1230sSystemMsg = _Ax1230sSystemMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 3)
)


class _Ax1230sSystemMsgText_Type(DisplayString):
    """Custom type ax1230sSystemMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Ax1230sSystemMsgText_Type.__name__ = "DisplayString"
_Ax1230sSystemMsgText_Object = MibScalar
ax1230sSystemMsgText = _Ax1230sSystemMsgText_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 3, 1),
    _Ax1230sSystemMsgText_Type()
)
ax1230sSystemMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSystemMsgText.setStatus("current")


class _Ax1230sSystemMsgType_Type(OctetString):
    """Custom type ax1230sSystemMsgType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Ax1230sSystemMsgType_Type.__name__ = "OctetString"
_Ax1230sSystemMsgType_Object = MibScalar
ax1230sSystemMsgType = _Ax1230sSystemMsgType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 3, 2),
    _Ax1230sSystemMsgType_Type()
)
ax1230sSystemMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSystemMsgType.setStatus("current")


class _Ax1230sSystemMsgTimeStamp_Type(DisplayString):
    """Custom type ax1230sSystemMsgTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Ax1230sSystemMsgTimeStamp_Type.__name__ = "DisplayString"
_Ax1230sSystemMsgTimeStamp_Object = MibScalar
ax1230sSystemMsgTimeStamp = _Ax1230sSystemMsgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 3, 3),
    _Ax1230sSystemMsgTimeStamp_Type()
)
ax1230sSystemMsgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSystemMsgTimeStamp.setStatus("current")


class _Ax1230sSystemMsgLevel_Type(OctetString):
    """Custom type ax1230sSystemMsgLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Ax1230sSystemMsgLevel_Type.__name__ = "OctetString"
_Ax1230sSystemMsgLevel_Object = MibScalar
ax1230sSystemMsgLevel = _Ax1230sSystemMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 3, 4),
    _Ax1230sSystemMsgLevel_Type()
)
ax1230sSystemMsgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSystemMsgLevel.setStatus("current")


class _Ax1230sSystemMsgEventPoint_Type(DisplayString):
    """Custom type ax1230sSystemMsgEventPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ax1230sSystemMsgEventPoint_Type.__name__ = "DisplayString"
_Ax1230sSystemMsgEventPoint_Object = MibScalar
ax1230sSystemMsgEventPoint = _Ax1230sSystemMsgEventPoint_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 3, 5),
    _Ax1230sSystemMsgEventPoint_Type()
)
ax1230sSystemMsgEventPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSystemMsgEventPoint.setStatus("current")


class _Ax1230sSystemMsgEventInterfaceID_Type(DisplayString):
    """Custom type ax1230sSystemMsgEventInterfaceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Ax1230sSystemMsgEventInterfaceID_Type.__name__ = "DisplayString"
_Ax1230sSystemMsgEventInterfaceID_Object = MibScalar
ax1230sSystemMsgEventInterfaceID = _Ax1230sSystemMsgEventInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 3, 6),
    _Ax1230sSystemMsgEventInterfaceID_Type()
)
ax1230sSystemMsgEventInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSystemMsgEventInterfaceID.setStatus("current")


class _Ax1230sSystemMsgEventCode_Type(OctetString):
    """Custom type ax1230sSystemMsgEventCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Ax1230sSystemMsgEventCode_Type.__name__ = "OctetString"
_Ax1230sSystemMsgEventCode_Object = MibScalar
ax1230sSystemMsgEventCode = _Ax1230sSystemMsgEventCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 3, 7),
    _Ax1230sSystemMsgEventCode_Type()
)
ax1230sSystemMsgEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSystemMsgEventCode.setStatus("current")


class _Ax1230sSystemMsgAdditionalCode_Type(OctetString):
    """Custom type ax1230sSystemMsgAdditionalCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Ax1230sSystemMsgAdditionalCode_Type.__name__ = "OctetString"
_Ax1230sSystemMsgAdditionalCode_Object = MibScalar
ax1230sSystemMsgAdditionalCode = _Ax1230sSystemMsgAdditionalCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 3, 8),
    _Ax1230sSystemMsgAdditionalCode_Type()
)
ax1230sSystemMsgAdditionalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSystemMsgAdditionalCode.setStatus("current")
_Ax1230sSnmpAgent_ObjectIdentity = ObjectIdentity
ax1230sSnmpAgent = _Ax1230sSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 4)
)
_Ax1230sSnmpSendReceiveSize_Type = Integer32
_Ax1230sSnmpSendReceiveSize_Object = MibScalar
ax1230sSnmpSendReceiveSize = _Ax1230sSnmpSendReceiveSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 4, 1),
    _Ax1230sSnmpSendReceiveSize_Type()
)
ax1230sSnmpSendReceiveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSnmpSendReceiveSize.setStatus("current")
_Ax1230sSnmpReceiveDelay_Type = Integer32
_Ax1230sSnmpReceiveDelay_Object = MibScalar
ax1230sSnmpReceiveDelay = _Ax1230sSnmpReceiveDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 4, 2),
    _Ax1230sSnmpReceiveDelay_Type()
)
ax1230sSnmpReceiveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSnmpReceiveDelay.setStatus("current")
_Ax1230sSnmpContinuousSend_Type = Integer32
_Ax1230sSnmpContinuousSend_Object = MibScalar
ax1230sSnmpContinuousSend = _Ax1230sSnmpContinuousSend_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 4, 3),
    _Ax1230sSnmpContinuousSend_Type()
)
ax1230sSnmpContinuousSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSnmpContinuousSend.setStatus("current")
_Ax1230sSnmpObjectMaxNumber_Type = Integer32
_Ax1230sSnmpObjectMaxNumber_Object = MibScalar
ax1230sSnmpObjectMaxNumber = _Ax1230sSnmpObjectMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 4, 4),
    _Ax1230sSnmpObjectMaxNumber_Type()
)
ax1230sSnmpObjectMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSnmpObjectMaxNumber.setStatus("current")
_Ax1230sLicense_ObjectIdentity = ObjectIdentity
ax1230sLicense = _Ax1230sLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6)
)
_Ax1230sLicenseNumber_Type = Integer32
_Ax1230sLicenseNumber_Object = MibScalar
ax1230sLicenseNumber = _Ax1230sLicenseNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 1),
    _Ax1230sLicenseNumber_Type()
)
ax1230sLicenseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sLicenseNumber.setStatus("current")
_Ax1230sLicenseTable_Object = MibTable
ax1230sLicenseTable = _Ax1230sLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ax1230sLicenseTable.setStatus("current")
_Ax1230sLicenseEntry_Object = MibTableRow
ax1230sLicenseEntry = _Ax1230sLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 2, 1)
)
ax1230sLicenseEntry.setIndexNames(
    (0, "AX1230S", "ax1230sLicenseIndex"),
)
if mibBuilder.loadTexts:
    ax1230sLicenseEntry.setStatus("current")
_Ax1230sLicenseIndex_Type = Integer32
_Ax1230sLicenseIndex_Object = MibTableColumn
ax1230sLicenseIndex = _Ax1230sLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 2, 1, 1),
    _Ax1230sLicenseIndex_Type()
)
ax1230sLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sLicenseIndex.setStatus("current")
_Ax1230sLicenseSerialNumber_Type = DisplayString
_Ax1230sLicenseSerialNumber_Object = MibTableColumn
ax1230sLicenseSerialNumber = _Ax1230sLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 2, 1, 2),
    _Ax1230sLicenseSerialNumber_Type()
)
ax1230sLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sLicenseSerialNumber.setStatus("current")
_Ax1230sLicenseOptionNumber_Type = Integer32
_Ax1230sLicenseOptionNumber_Object = MibTableColumn
ax1230sLicenseOptionNumber = _Ax1230sLicenseOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 2, 1, 3),
    _Ax1230sLicenseOptionNumber_Type()
)
ax1230sLicenseOptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sLicenseOptionNumber.setStatus("current")
_Ax1230sLicenseOptionTable_Object = MibTable
ax1230sLicenseOptionTable = _Ax1230sLicenseOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 3)
)
if mibBuilder.loadTexts:
    ax1230sLicenseOptionTable.setStatus("current")
_Ax1230sLicenseOptionEntry_Object = MibTableRow
ax1230sLicenseOptionEntry = _Ax1230sLicenseOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 3, 1)
)
ax1230sLicenseOptionEntry.setIndexNames(
    (0, "AX1230S", "ax1230sLicenseOptionIndex"),
    (0, "AX1230S", "ax1230sLicenseOptionNumberIndex"),
)
if mibBuilder.loadTexts:
    ax1230sLicenseOptionEntry.setStatus("current")
_Ax1230sLicenseOptionIndex_Type = Integer32
_Ax1230sLicenseOptionIndex_Object = MibTableColumn
ax1230sLicenseOptionIndex = _Ax1230sLicenseOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 3, 1, 1),
    _Ax1230sLicenseOptionIndex_Type()
)
ax1230sLicenseOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sLicenseOptionIndex.setStatus("current")
_Ax1230sLicenseOptionNumberIndex_Type = Integer32
_Ax1230sLicenseOptionNumberIndex_Object = MibTableColumn
ax1230sLicenseOptionNumberIndex = _Ax1230sLicenseOptionNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 3, 1, 2),
    _Ax1230sLicenseOptionNumberIndex_Type()
)
ax1230sLicenseOptionNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sLicenseOptionNumberIndex.setStatus("current")
_Ax1230sLicenseOptionSoftwareName_Type = DisplayString
_Ax1230sLicenseOptionSoftwareName_Object = MibTableColumn
ax1230sLicenseOptionSoftwareName = _Ax1230sLicenseOptionSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 3, 1, 3),
    _Ax1230sLicenseOptionSoftwareName_Type()
)
ax1230sLicenseOptionSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sLicenseOptionSoftwareName.setStatus("current")
_Ax1230sLicenseOptionSoftwareAbbreviation_Type = DisplayString
_Ax1230sLicenseOptionSoftwareAbbreviation_Object = MibTableColumn
ax1230sLicenseOptionSoftwareAbbreviation = _Ax1230sLicenseOptionSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 1, 6, 3, 1, 4),
    _Ax1230sLicenseOptionSoftwareAbbreviation_Type()
)
ax1230sLicenseOptionSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sLicenseOptionSoftwareAbbreviation.setStatus("current")
_Ax1230sDevice_ObjectIdentity = ObjectIdentity
ax1230sDevice = _Ax1230sDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2)
)
_Ax1230sChassis_ObjectIdentity = ObjectIdentity
ax1230sChassis = _Ax1230sChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1)
)
_Ax1230sChassisMaxNumber_Type = Integer32
_Ax1230sChassisMaxNumber_Object = MibScalar
ax1230sChassisMaxNumber = _Ax1230sChassisMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 1),
    _Ax1230sChassisMaxNumber_Type()
)
ax1230sChassisMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sChassisMaxNumber.setStatus("current")
_Ax1230sChassisTable_Object = MibTable
ax1230sChassisTable = _Ax1230sChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ax1230sChassisTable.setStatus("current")
_Ax1230sChassisEntry_Object = MibTableRow
ax1230sChassisEntry = _Ax1230sChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1)
)
ax1230sChassisEntry.setIndexNames(
    (0, "AX1230S", "ax1230sChassisIndex"),
)
if mibBuilder.loadTexts:
    ax1230sChassisEntry.setStatus("current")
_Ax1230sChassisIndex_Type = Integer32
_Ax1230sChassisIndex_Object = MibTableColumn
ax1230sChassisIndex = _Ax1230sChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 1),
    _Ax1230sChassisIndex_Type()
)
ax1230sChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sChassisIndex.setStatus("current")


class _Ax1230sChassisType_Type(Integer32):
    """Custom type ax1230sChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              300,
              301,
              302)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("model-AX1230S-24T2C", 300),
          ("model-AX1230S-48T2C", 301),
          ("model-AX1230S-24P2C", 302))
    )


_Ax1230sChassisType_Type.__name__ = "Integer32"
_Ax1230sChassisType_Object = MibTableColumn
ax1230sChassisType = _Ax1230sChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 2),
    _Ax1230sChassisType_Type()
)
ax1230sChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sChassisType.setStatus("current")


class _Ax1230sChassisStatus_Type(Integer32):
    """Custom type ax1230sChassisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("up", 2)
    )


_Ax1230sChassisStatus_Type.__name__ = "Integer32"
_Ax1230sChassisStatus_Object = MibTableColumn
ax1230sChassisStatus = _Ax1230sChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 3),
    _Ax1230sChassisStatus_Type()
)
ax1230sChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sChassisStatus.setStatus("current")


class _Ax1230sStsLedStatus_Type(Integer32):
    """Custom type ax1230sStsLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("red-light-on", 0),
          ("red-light-off", 1),
          ("orange-light-on", 2),
          ("orange-light-off", 3),
          ("green-light-off", 4),
          ("green-light-on", 5),
          ("light-off", 6))
    )


_Ax1230sStsLedStatus_Type.__name__ = "Integer32"
_Ax1230sStsLedStatus_Object = MibTableColumn
ax1230sStsLedStatus = _Ax1230sStsLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 4),
    _Ax1230sStsLedStatus_Type()
)
ax1230sStsLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sStsLedStatus.setStatus("current")
_Ax1230sCpuName_Type = DisplayString
_Ax1230sCpuName_Object = MibTableColumn
ax1230sCpuName = _Ax1230sCpuName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 5),
    _Ax1230sCpuName_Type()
)
ax1230sCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sCpuName.setStatus("current")
_Ax1230sCpuClock_Type = Integer32
_Ax1230sCpuClock_Object = MibTableColumn
ax1230sCpuClock = _Ax1230sCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 6),
    _Ax1230sCpuClock_Type()
)
ax1230sCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sCpuClock.setStatus("current")
_Ax1230sMemoryTotalSize_Type = Integer32
_Ax1230sMemoryTotalSize_Object = MibTableColumn
ax1230sMemoryTotalSize = _Ax1230sMemoryTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 7),
    _Ax1230sMemoryTotalSize_Type()
)
ax1230sMemoryTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sMemoryTotalSize.setStatus("current")
_Ax1230sMemoryUsedSize_Type = Integer32
_Ax1230sMemoryUsedSize_Object = MibTableColumn
ax1230sMemoryUsedSize = _Ax1230sMemoryUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 8),
    _Ax1230sMemoryUsedSize_Type()
)
ax1230sMemoryUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sMemoryUsedSize.setStatus("current")
_Ax1230sMemoryFreeSize_Type = Integer32
_Ax1230sMemoryFreeSize_Object = MibTableColumn
ax1230sMemoryFreeSize = _Ax1230sMemoryFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 9),
    _Ax1230sMemoryFreeSize_Type()
)
ax1230sMemoryFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sMemoryFreeSize.setStatus("current")
_Ax1230sRomVersion_Type = DisplayString
_Ax1230sRomVersion_Object = MibTableColumn
ax1230sRomVersion = _Ax1230sRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 10),
    _Ax1230sRomVersion_Type()
)
ax1230sRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sRomVersion.setStatus("current")
_Ax1230sCpuLoad1m_Type = Integer32
_Ax1230sCpuLoad1m_Object = MibTableColumn
ax1230sCpuLoad1m = _Ax1230sCpuLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 11),
    _Ax1230sCpuLoad1m_Type()
)
ax1230sCpuLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sCpuLoad1m.setStatus("current")
_Ax1230sFlashTotalSize_Type = Integer32
_Ax1230sFlashTotalSize_Object = MibTableColumn
ax1230sFlashTotalSize = _Ax1230sFlashTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 12),
    _Ax1230sFlashTotalSize_Type()
)
ax1230sFlashTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sFlashTotalSize.setStatus("current")
_Ax1230sFlashUsedSize_Type = Integer32
_Ax1230sFlashUsedSize_Object = MibTableColumn
ax1230sFlashUsedSize = _Ax1230sFlashUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 13),
    _Ax1230sFlashUsedSize_Type()
)
ax1230sFlashUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sFlashUsedSize.setStatus("current")
_Ax1230sFlashFreeSize_Type = Integer32
_Ax1230sFlashFreeSize_Object = MibTableColumn
ax1230sFlashFreeSize = _Ax1230sFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 14),
    _Ax1230sFlashFreeSize_Type()
)
ax1230sFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sFlashFreeSize.setStatus("current")


class _Ax1230sSdCardStatus_Type(Integer32):
    """Custom type ax1230sSdCardStatus based on Integer32"""
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


_Ax1230sSdCardStatus_Type.__name__ = "Integer32"
_Ax1230sSdCardStatus_Object = MibTableColumn
ax1230sSdCardStatus = _Ax1230sSdCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 15),
    _Ax1230sSdCardStatus_Type()
)
ax1230sSdCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSdCardStatus.setStatus("current")
_Ax1230sSdCardTotalSize_Type = Integer32
_Ax1230sSdCardTotalSize_Object = MibTableColumn
ax1230sSdCardTotalSize = _Ax1230sSdCardTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 16),
    _Ax1230sSdCardTotalSize_Type()
)
ax1230sSdCardTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSdCardTotalSize.setStatus("current")
_Ax1230sSdCardUsedSize_Type = Integer32
_Ax1230sSdCardUsedSize_Object = MibTableColumn
ax1230sSdCardUsedSize = _Ax1230sSdCardUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 17),
    _Ax1230sSdCardUsedSize_Type()
)
ax1230sSdCardUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSdCardUsedSize.setStatus("current")
_Ax1230sSdCardFreeSize_Type = Integer32
_Ax1230sSdCardFreeSize_Object = MibTableColumn
ax1230sSdCardFreeSize = _Ax1230sSdCardFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 18),
    _Ax1230sSdCardFreeSize_Type()
)
ax1230sSdCardFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sSdCardFreeSize.setStatus("current")
_Ax1230sPhysLineNumber_Type = Integer32
_Ax1230sPhysLineNumber_Object = MibTableColumn
ax1230sPhysLineNumber = _Ax1230sPhysLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 19),
    _Ax1230sPhysLineNumber_Type()
)
ax1230sPhysLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sPhysLineNumber.setStatus("current")
_Ax1230sTemperatureStatusNumber_Type = Integer32
_Ax1230sTemperatureStatusNumber_Object = MibTableColumn
ax1230sTemperatureStatusNumber = _Ax1230sTemperatureStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 20),
    _Ax1230sTemperatureStatusNumber_Type()
)
ax1230sTemperatureStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sTemperatureStatusNumber.setStatus("current")
_Ax1230sPowerUnitNumber_Type = Integer32
_Ax1230sPowerUnitNumber_Object = MibTableColumn
ax1230sPowerUnitNumber = _Ax1230sPowerUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 21),
    _Ax1230sPowerUnitNumber_Type()
)
ax1230sPowerUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sPowerUnitNumber.setStatus("current")
_Ax1230sRedundantPsNumber_Type = Integer32
_Ax1230sRedundantPsNumber_Object = MibTableColumn
ax1230sRedundantPsNumber = _Ax1230sRedundantPsNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 22),
    _Ax1230sRedundantPsNumber_Type()
)
ax1230sRedundantPsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sRedundantPsNumber.setStatus("current")
_Ax1230sFanNumber_Type = Integer32
_Ax1230sFanNumber_Object = MibTableColumn
ax1230sFanNumber = _Ax1230sFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 23),
    _Ax1230sFanNumber_Type()
)
ax1230sFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sFanNumber.setStatus("current")
_Ax1230sTotalAccumRunTime_Type = Integer32
_Ax1230sTotalAccumRunTime_Object = MibTableColumn
ax1230sTotalAccumRunTime = _Ax1230sTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 24),
    _Ax1230sTotalAccumRunTime_Type()
)
ax1230sTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sTotalAccumRunTime.setStatus("current")
_Ax1230sCriticalAccumRunTime_Type = Integer32
_Ax1230sCriticalAccumRunTime_Object = MibTableColumn
ax1230sCriticalAccumRunTime = _Ax1230sCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 2, 1, 25),
    _Ax1230sCriticalAccumRunTime_Type()
)
ax1230sCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sCriticalAccumRunTime.setStatus("current")
_Ax1230sTemperatureStatusTable_Object = MibTable
ax1230sTemperatureStatusTable = _Ax1230sTemperatureStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ax1230sTemperatureStatusTable.setStatus("current")
_Ax1230sTemperatureStatusEntry_Object = MibTableRow
ax1230sTemperatureStatusEntry = _Ax1230sTemperatureStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 3, 1)
)
ax1230sTemperatureStatusEntry.setIndexNames(
    (0, "AX1230S", "ax1230sChassisIndex"),
    (0, "AX1230S", "ax1230sTemperatureStatusIndex"),
)
if mibBuilder.loadTexts:
    ax1230sTemperatureStatusEntry.setStatus("current")
_Ax1230sTemperatureStatusIndex_Type = Integer32
_Ax1230sTemperatureStatusIndex_Object = MibTableColumn
ax1230sTemperatureStatusIndex = _Ax1230sTemperatureStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 3, 1, 1),
    _Ax1230sTemperatureStatusIndex_Type()
)
ax1230sTemperatureStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sTemperatureStatusIndex.setStatus("current")


class _Ax1230sTemperatureStatusDescr_Type(DisplayString):
    """Custom type ax1230sTemperatureStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ax1230sTemperatureStatusDescr_Type.__name__ = "DisplayString"
_Ax1230sTemperatureStatusDescr_Object = MibTableColumn
ax1230sTemperatureStatusDescr = _Ax1230sTemperatureStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 3, 1, 2),
    _Ax1230sTemperatureStatusDescr_Type()
)
ax1230sTemperatureStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sTemperatureStatusDescr.setStatus("current")
_Ax1230sTemperatureStatusValue_Type = Integer32
_Ax1230sTemperatureStatusValue_Object = MibTableColumn
ax1230sTemperatureStatusValue = _Ax1230sTemperatureStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 3, 1, 3),
    _Ax1230sTemperatureStatusValue_Type()
)
ax1230sTemperatureStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sTemperatureStatusValue.setStatus("current")
_Ax1230sTemperatureThreshold_Type = Integer32
_Ax1230sTemperatureThreshold_Object = MibTableColumn
ax1230sTemperatureThreshold = _Ax1230sTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 3, 1, 4),
    _Ax1230sTemperatureThreshold_Type()
)
ax1230sTemperatureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sTemperatureThreshold.setStatus("current")


class _Ax1230sTemperatureState_Type(Integer32):
    """Custom type ax1230sTemperatureState based on Integer32"""
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


_Ax1230sTemperatureState_Type.__name__ = "Integer32"
_Ax1230sTemperatureState_Object = MibTableColumn
ax1230sTemperatureState = _Ax1230sTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 3, 1, 5),
    _Ax1230sTemperatureState_Type()
)
ax1230sTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sTemperatureState.setStatus("current")
_Ax1230sPowerUnitTable_Object = MibTable
ax1230sPowerUnitTable = _Ax1230sPowerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ax1230sPowerUnitTable.setStatus("current")
_Ax1230sPowerUnitEntry_Object = MibTableRow
ax1230sPowerUnitEntry = _Ax1230sPowerUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 4, 1)
)
ax1230sPowerUnitEntry.setIndexNames(
    (0, "AX1230S", "ax1230sChassisIndex"),
    (0, "AX1230S", "ax1230sPowerUnitIndex"),
)
if mibBuilder.loadTexts:
    ax1230sPowerUnitEntry.setStatus("current")
_Ax1230sPowerUnitIndex_Type = Integer32
_Ax1230sPowerUnitIndex_Object = MibTableColumn
ax1230sPowerUnitIndex = _Ax1230sPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 4, 1, 1),
    _Ax1230sPowerUnitIndex_Type()
)
ax1230sPowerUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sPowerUnitIndex.setStatus("current")


class _Ax1230sPowerConnectStatus_Type(Integer32):
    """Custom type ax1230sPowerConnectStatus based on Integer32"""
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


_Ax1230sPowerConnectStatus_Type.__name__ = "Integer32"
_Ax1230sPowerConnectStatus_Object = MibTableColumn
ax1230sPowerConnectStatus = _Ax1230sPowerConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 4, 1, 2),
    _Ax1230sPowerConnectStatus_Type()
)
ax1230sPowerConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sPowerConnectStatus.setStatus("current")


class _Ax1230sPowerSupplyStatus_Type(Integer32):
    """Custom type ax1230sPowerSupplyStatus based on Integer32"""
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


_Ax1230sPowerSupplyStatus_Type.__name__ = "Integer32"
_Ax1230sPowerSupplyStatus_Object = MibTableColumn
ax1230sPowerSupplyStatus = _Ax1230sPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 4, 1, 3),
    _Ax1230sPowerSupplyStatus_Type()
)
ax1230sPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sPowerSupplyStatus.setStatus("current")
_Ax1230sFanTable_Object = MibTable
ax1230sFanTable = _Ax1230sFanTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ax1230sFanTable.setStatus("current")
_Ax1230sFanEntry_Object = MibTableRow
ax1230sFanEntry = _Ax1230sFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 5, 1)
)
ax1230sFanEntry.setIndexNames(
    (0, "AX1230S", "ax1230sChassisIndex"),
    (0, "AX1230S", "ax1230sFanIndex"),
)
if mibBuilder.loadTexts:
    ax1230sFanEntry.setStatus("current")
_Ax1230sFanIndex_Type = Integer32
_Ax1230sFanIndex_Object = MibTableColumn
ax1230sFanIndex = _Ax1230sFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 5, 1, 1),
    _Ax1230sFanIndex_Type()
)
ax1230sFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sFanIndex.setStatus("current")


class _Ax1230sFanStatus_Type(Integer32):
    """Custom type ax1230sFanStatus based on Integer32"""
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


_Ax1230sFanStatus_Type.__name__ = "Integer32"
_Ax1230sFanStatus_Object = MibTableColumn
ax1230sFanStatus = _Ax1230sFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 5, 1, 2),
    _Ax1230sFanStatus_Type()
)
ax1230sFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sFanStatus.setStatus("current")
_Ax1230sRedundantPsTable_Object = MibTable
ax1230sRedundantPsTable = _Ax1230sRedundantPsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ax1230sRedundantPsTable.setStatus("current")
_Ax1230sRedundantPsEntry_Object = MibTableRow
ax1230sRedundantPsEntry = _Ax1230sRedundantPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 6, 1)
)
ax1230sRedundantPsEntry.setIndexNames(
    (0, "AX1230S", "ax1230sChassisIndex"),
    (0, "AX1230S", "ax1230sRedundantPsIndex"),
)
if mibBuilder.loadTexts:
    ax1230sRedundantPsEntry.setStatus("current")
_Ax1230sRedundantPsIndex_Type = Integer32
_Ax1230sRedundantPsIndex_Object = MibTableColumn
ax1230sRedundantPsIndex = _Ax1230sRedundantPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 6, 1, 1),
    _Ax1230sRedundantPsIndex_Type()
)
ax1230sRedundantPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sRedundantPsIndex.setStatus("current")


class _Ax1230sRedundantPsConnectStatus_Type(Integer32):
    """Custom type ax1230sRedundantPsConnectStatus based on Integer32"""
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


_Ax1230sRedundantPsConnectStatus_Type.__name__ = "Integer32"
_Ax1230sRedundantPsConnectStatus_Object = MibTableColumn
ax1230sRedundantPsConnectStatus = _Ax1230sRedundantPsConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 6, 1, 2),
    _Ax1230sRedundantPsConnectStatus_Type()
)
ax1230sRedundantPsConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sRedundantPsConnectStatus.setStatus("current")


class _Ax1230sRedundantPsStatus_Type(Integer32):
    """Custom type ax1230sRedundantPsStatus based on Integer32"""
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


_Ax1230sRedundantPsStatus_Type.__name__ = "Integer32"
_Ax1230sRedundantPsStatus_Object = MibTableColumn
ax1230sRedundantPsStatus = _Ax1230sRedundantPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 1, 6, 1, 3),
    _Ax1230sRedundantPsStatus_Type()
)
ax1230sRedundantPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sRedundantPsStatus.setStatus("current")
_Ax1230sPhysLine_ObjectIdentity = ObjectIdentity
ax1230sPhysLine = _Ax1230sPhysLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 2)
)
_Ax1230sPhysLineTable_Object = MibTable
ax1230sPhysLineTable = _Ax1230sPhysLineTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ax1230sPhysLineTable.setStatus("current")
_Ax1230sPhysLineEntry_Object = MibTableRow
ax1230sPhysLineEntry = _Ax1230sPhysLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 2, 1, 1)
)
ax1230sPhysLineEntry.setIndexNames(
    (0, "AX1230S", "ax1230sChassisIndex"),
    (0, "AX1230S", "ax1230sPhysLineIndex"),
)
if mibBuilder.loadTexts:
    ax1230sPhysLineEntry.setStatus("current")
_Ax1230sPhysLineIndex_Type = Integer32
_Ax1230sPhysLineIndex_Object = MibTableColumn
ax1230sPhysLineIndex = _Ax1230sPhysLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 2, 1, 1, 1),
    _Ax1230sPhysLineIndex_Type()
)
ax1230sPhysLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sPhysLineIndex.setStatus("current")


class _Ax1230sPhysLineConnectorType_Type(Integer32):
    """Custom type ax1230sPhysLineConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              401,
              402,
              403)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("type1000BASE-LX", 301),
          ("type1000BASE-SX", 302),
          ("type1000BASE-LH", 303),
          ("type1000BASE-BX10-D", 304),
          ("type1000BASE-BX10-U", 305),
          ("type1000BASE-BX40-D", 306),
          ("type1000BASE-BX40-U", 307),
          ("type1000BASE-SX2", 308),
          ("type10GBASE-SR", 401),
          ("type10GBASE-LR", 402),
          ("type10GBASE-ER", 403))
    )


_Ax1230sPhysLineConnectorType_Type.__name__ = "Integer32"
_Ax1230sPhysLineConnectorType_Object = MibTableColumn
ax1230sPhysLineConnectorType = _Ax1230sPhysLineConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 2, 1, 1, 2),
    _Ax1230sPhysLineConnectorType_Type()
)
ax1230sPhysLineConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sPhysLineConnectorType.setStatus("current")


class _Ax1230sPhysLineOperStatus_Type(Integer32):
    """Custom type ax1230sPhysLineOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              8,
              9,
              20)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("active", 2),
          ("initialization", 3),
          ("down", 4),
          ("lock", 6),
          ("line-fault", 8),
          ("test", 9),
          ("inactive", 20))
    )


_Ax1230sPhysLineOperStatus_Type.__name__ = "Integer32"
_Ax1230sPhysLineOperStatus_Object = MibTableColumn
ax1230sPhysLineOperStatus = _Ax1230sPhysLineOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 2, 1, 1, 3),
    _Ax1230sPhysLineOperStatus_Type()
)
ax1230sPhysLineOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sPhysLineOperStatus.setStatus("current")
_Ax1230sPhysLineIfIndexNumber_Type = Integer32
_Ax1230sPhysLineIfIndexNumber_Object = MibTableColumn
ax1230sPhysLineIfIndexNumber = _Ax1230sPhysLineIfIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 2, 1, 1, 4),
    _Ax1230sPhysLineIfIndexNumber_Type()
)
ax1230sPhysLineIfIndexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sPhysLineIfIndexNumber.setStatus("current")


class _Ax1230sPhysLineTransceiverStatus_Type(Integer32):
    """Custom type ax1230sPhysLineTransceiverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              20,
              21,
              22,
              23,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("unchangeable-transceiver", 1),
          ("sfp-mounted", 20),
          ("sfp-unmounted", 21),
          ("unsupported-sfp-mounted", 22),
          ("sfp-status-unknown", 23),
          ("xfp-mounted", 30),
          ("xfp-unmounted", 31),
          ("unsupported-xfp-mounted", 32),
          ("xfp-status-unknown", 33))
    )


_Ax1230sPhysLineTransceiverStatus_Type.__name__ = "Integer32"
_Ax1230sPhysLineTransceiverStatus_Object = MibTableColumn
ax1230sPhysLineTransceiverStatus = _Ax1230sPhysLineTransceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 2, 2, 1, 1, 5),
    _Ax1230sPhysLineTransceiverStatus_Type()
)
ax1230sPhysLineTransceiverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sPhysLineTransceiverStatus.setStatus("current")
_Ax1230sManagementMIB_ObjectIdentity = ObjectIdentity
ax1230sManagementMIB = _Ax1230sManagementMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 3)
)
_Ax1230sOperationCommand_ObjectIdentity = ObjectIdentity
ax1230sOperationCommand = _Ax1230sOperationCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 3, 1)
)
_Ax1230sFdbClearMIB_ObjectIdentity = ObjectIdentity
ax1230sFdbClearMIB = _Ax1230sFdbClearMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 3, 1, 1)
)


class _Ax1230sFdbClearSet_Type(Integer32):
    """Custom type ax1230sFdbClearSet based on Integer32"""
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


_Ax1230sFdbClearSet_Type.__name__ = "Integer32"
_Ax1230sFdbClearSet_Object = MibScalar
ax1230sFdbClearSet = _Ax1230sFdbClearSet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 3, 1, 1, 1),
    _Ax1230sFdbClearSet_Type()
)
ax1230sFdbClearSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ax1230sFdbClearSet.setStatus("current")
_Ax1230sFdbClearReqTime_Type = TimeTicks
_Ax1230sFdbClearReqTime_Object = MibScalar
ax1230sFdbClearReqTime = _Ax1230sFdbClearReqTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 3, 1, 1, 2),
    _Ax1230sFdbClearReqTime_Type()
)
ax1230sFdbClearReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sFdbClearReqTime.setStatus("current")
_Ax1230sFdbClearSuccessTime_Type = TimeTicks
_Ax1230sFdbClearSuccessTime_Object = MibScalar
ax1230sFdbClearSuccessTime = _Ax1230sFdbClearSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 3, 1, 1, 3),
    _Ax1230sFdbClearSuccessTime_Type()
)
ax1230sFdbClearSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax1230sFdbClearSuccessTime.setStatus("current")
_Ax1230sAuth_ObjectIdentity = ObjectIdentity
ax1230sAuth = _Ax1230sAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10)
)
_Ax1230sAuthInfo_ObjectIdentity = ObjectIdentity
ax1230sAuthInfo = _Ax1230sAuthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 1)
)


class _Ax1230sAuthSysName_Type(DisplayString):
    """Custom type ax1230sAuthSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_Ax1230sAuthSysName_Type.__name__ = "DisplayString"
_Ax1230sAuthSysName_Object = MibTableColumn
ax1230sAuthSysName = _Ax1230sAuthSysName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 1, 1),
    _Ax1230sAuthSysName_Type()
)
ax1230sAuthSysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sAuthSysName.setStatus("current")
_Ax1230sAuthIfIndex_Type = Integer32
_Ax1230sAuthIfIndex_Object = MibTableColumn
ax1230sAuthIfIndex = _Ax1230sAuthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 1, 2),
    _Ax1230sAuthIfIndex_Type()
)
ax1230sAuthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sAuthIfIndex.setStatus("current")
_Ax1230sAuthSupplicantMac_Type = MacAddress
_Ax1230sAuthSupplicantMac_Object = MibTableColumn
ax1230sAuthSupplicantMac = _Ax1230sAuthSupplicantMac_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 1, 3),
    _Ax1230sAuthSupplicantMac_Type()
)
ax1230sAuthSupplicantMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sAuthSupplicantMac.setStatus("current")


class _Ax1230sAuthMessage_Type(DisplayString):
    """Custom type ax1230sAuthMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 280),
    )


_Ax1230sAuthMessage_Type.__name__ = "DisplayString"
_Ax1230sAuthMessage_Object = MibTableColumn
ax1230sAuthMessage = _Ax1230sAuthMessage_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 1, 4),
    _Ax1230sAuthMessage_Type()
)
ax1230sAuthMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax1230sAuthMessage.setStatus("current")
_Ax1230sDot1x_ObjectIdentity = ObjectIdentity
ax1230sDot1x = _Ax1230sDot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 2)
)
_Ax1230sDot1xFailure_Object = MibTable
ax1230sDot1xFailure = _Ax1230sDot1xFailure_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 2, 1)
)
if mibBuilder.loadTexts:
    ax1230sDot1xFailure.setStatus("current")
_Ax1230sDot1xEvent_Object = MibTable
ax1230sDot1xEvent = _Ax1230sDot1xEvent_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 2, 2)
)
if mibBuilder.loadTexts:
    ax1230sDot1xEvent.setStatus("current")
_Ax1230sDot1xSystem_Object = MibTable
ax1230sDot1xSystem = _Ax1230sDot1xSystem_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 2, 3)
)
if mibBuilder.loadTexts:
    ax1230sDot1xSystem.setStatus("current")
_Ax1230sWauth_ObjectIdentity = ObjectIdentity
ax1230sWauth = _Ax1230sWauth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 3)
)
_Ax1230sWauthFailure_Object = MibTable
ax1230sWauthFailure = _Ax1230sWauthFailure_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 3, 1)
)
if mibBuilder.loadTexts:
    ax1230sWauthFailure.setStatus("current")
_Ax1230sWauthEvent_Object = MibTable
ax1230sWauthEvent = _Ax1230sWauthEvent_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 3, 2)
)
if mibBuilder.loadTexts:
    ax1230sWauthEvent.setStatus("current")
_Ax1230sWauthSystem_Object = MibTable
ax1230sWauthSystem = _Ax1230sWauthSystem_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 3, 3)
)
if mibBuilder.loadTexts:
    ax1230sWauthSystem.setStatus("current")
_Ax1230sMauth_ObjectIdentity = ObjectIdentity
ax1230sMauth = _Ax1230sMauth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 4)
)
_Ax1230sMauthFailure_Object = MibTable
ax1230sMauthFailure = _Ax1230sMauthFailure_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 4, 1)
)
if mibBuilder.loadTexts:
    ax1230sMauthFailure.setStatus("current")
_Ax1230sMauthEvent_Object = MibTable
ax1230sMauthEvent = _Ax1230sMauthEvent_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 4, 2)
)
if mibBuilder.loadTexts:
    ax1230sMauthEvent.setStatus("current")
_Ax1230sMauthSystem_Object = MibTable
ax1230sMauthSystem = _Ax1230sMauthSystem_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 10, 10, 4, 3)
)
if mibBuilder.loadTexts:
    ax1230sMauthSystem.setStatus("current")

# Managed Objects groups


# Notification objects

ax1230sSystemMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 1)
)
ax1230sSystemMsgTrap.setObjects(
      *(("AX1230S", "ax1230sSystemMsgType"),
        ("AX1230S", "ax1230sSystemMsgTimeStamp"),
        ("AX1230S", "ax1230sSystemMsgLevel"),
        ("AX1230S", "ax1230sSystemMsgEventPoint"),
        ("AX1230S", "ax1230sSystemMsgEventInterfaceID"),
        ("AX1230S", "ax1230sSystemMsgEventCode"),
        ("AX1230S", "ax1230sSystemMsgAdditionalCode"),
        ("AX1230S", "ax1230sSystemMsgText"))
)
if mibBuilder.loadTexts:
    ax1230sSystemMsgTrap.setStatus(
        ""
    )

ax1230sStandbySystemUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 2)
)
ax1230sStandbySystemUpTrap.setObjects(
    ("AX1230S", "ax1230sChassisIndex")
)
if mibBuilder.loadTexts:
    ax1230sStandbySystemUpTrap.setStatus(
        ""
    )

ax1230sStandbySystemDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 3)
)
ax1230sStandbySystemDownTrap.setObjects(
    ("AX1230S", "ax1230sChassisIndex")
)
if mibBuilder.loadTexts:
    ax1230sStandbySystemDownTrap.setStatus(
        ""
    )

ax1230sTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 4)
)
ax1230sTemperatureTrap.setObjects(
      *(("AX1230S", "ax1230sChassisIndex"),
        ("AX1230S", "ax1230sTemperatureStatusIndex"),
        ("AX1230S", "ax1230sTemperatureStatusDescr"),
        ("AX1230S", "ax1230sTemperatureStatusValue"),
        ("AX1230S", "ax1230sTemperatureState"))
)
if mibBuilder.loadTexts:
    ax1230sTemperatureTrap.setStatus(
        ""
    )

ax1230sGsrpStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 6)
)
ax1230sGsrpStateTransitionTrap.setObjects(
      *(("AX1230S", "axsGsrpGroupId"),
        ("AX1230S", "axsGsrpVlanGroupId"),
        ("AX1230S", "axsGsrpState"))
)
if mibBuilder.loadTexts:
    ax1230sGsrpStateTransitionTrap.setStatus(
        ""
    )

ax1230sEoeMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 7)
)
ax1230sEoeMsgTrap.setObjects(
      *(("AX1230S", "ax1230sSystemMsgType"),
        ("AX1230S", "ax1230sSystemMsgTimeStamp"),
        ("AX1230S", "ax1230sSystemMsgLevel"),
        ("AX1230S", "ax1230sSystemMsgEventPoint"),
        ("AX1230S", "ax1230sSystemMsgEventInterfaceID"),
        ("AX1230S", "ax1230sSystemMsgEventCode"),
        ("AX1230S", "ax1230sSystemMsgAdditionalCode"),
        ("AX1230S", "ax1230sSystemMsgText"))
)
if mibBuilder.loadTexts:
    ax1230sEoeMsgTrap.setStatus(
        ""
    )

ax1230sAirFanStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 8)
)
if mibBuilder.loadTexts:
    ax1230sAirFanStopTrap.setStatus(
        ""
    )

ax1230sPowerSupplyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 9)
)
if mibBuilder.loadTexts:
    ax1230sPowerSupplyFailureTrap.setStatus(
        ""
    )

ax1230sLoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 10)
)
ax1230sLoginSuccessTrap.setObjects(
      *(("AX1230S", "axsLoginName"),
        ("AX1230S", "axsLoginTime"),
        ("AX1230S", "axsLoginLocation"),
        ("AX1230S", "axsLoginLine"))
)
if mibBuilder.loadTexts:
    ax1230sLoginSuccessTrap.setStatus(
        ""
    )

ax1230sLoginFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 11)
)
ax1230sLoginFailureTrap.setObjects(
      *(("AX1230S", "axsLoginName"),
        ("AX1230S", "axsLoginFailureTime"),
        ("AX1230S", "axsLoginLocation"),
        ("AX1230S", "axsLoginLine"))
)
if mibBuilder.loadTexts:
    ax1230sLoginFailureTrap.setStatus(
        ""
    )

ax1230sLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 12)
)
ax1230sLogoutTrap.setObjects(
      *(("AX1230S", "axsLoginName"),
        ("AX1230S", "axsLoginTime"),
        ("AX1230S", "axsLogoutTime"),
        ("AX1230S", "axsLoginLocation"),
        ("AX1230S", "axsLoginLine"),
        ("AX1230S", "axsLogoutStatus"))
)
if mibBuilder.loadTexts:
    ax1230sLogoutTrap.setStatus(
        ""
    )

ax1230sMemoryUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 13)
)
if mibBuilder.loadTexts:
    ax1230sMemoryUsageTrap.setStatus(
        ""
    )

ax1230sFrameErrorReceiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 18)
)
ax1230sFrameErrorReceiveTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax1230sFrameErrorReceiveTrap.setStatus(
        ""
    )

ax1230sFrameErrorSendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 19)
)
ax1230sFrameErrorSendTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax1230sFrameErrorSendTrap.setStatus(
        ""
    )

axsBroadcastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 20)
)
axsBroadcastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsBroadcastStormDetectTrap.setStatus(
        ""
    )

axsMulticastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 21)
)
axsMulticastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsMulticastStormDetectTrap.setStatus(
        ""
    )

axsUnicastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 22)
)
axsUnicastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsUnicastStormDetectTrap.setStatus(
        ""
    )

axsBroadcastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 23)
)
axsBroadcastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsBroadcastStormPortInactivateTrap.setStatus(
        ""
    )

axsMulticastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 24)
)
axsMulticastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsMulticastStormPortInactivateTrap.setStatus(
        ""
    )

axsUniticastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 25)
)
axsUniticastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsUniticastStormPortInactivateTrap.setStatus(
        ""
    )

axsBroadcastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 26)
)
axsBroadcastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsBroadcastStormRecoverTrap.setStatus(
        ""
    )

axsMulticastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 27)
)
axsMulticastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsMulticastStormRecoverTrap.setStatus(
        ""
    )

axsUnicastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 28)
)
axsUnicastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsUnicastStormRecoverTrap.setStatus(
        ""
    )

axsEfmoamUdldPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 29)
)
axsEfmoamUdldPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsEfmoamUdldPortInactivateTrap.setStatus(
        ""
    )

axsEfmoamLoopDetectPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 30)
)
axsEfmoamLoopDetectPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axsEfmoamLoopDetectPortInactivateTrap.setStatus(
        ""
    )

ax1230sDot1xFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 31)
)
ax1230sDot1xFailureTrap.setObjects(
      *(("AX1230S", "ax1230sAuthSysName"),
        ("AX1230S", "ax1230sAuthIfIndex"),
        ("AX1230S", "ax1230sAuthSupplicantMac"),
        ("AX1230S", "ax1230sAuthMessage"))
)
if mibBuilder.loadTexts:
    ax1230sDot1xFailureTrap.setStatus(
        ""
    )

ax1230sDot1xEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 32)
)
ax1230sDot1xEventTrap.setObjects(
      *(("AX1230S", "ax1230sAuthSysName"),
        ("AX1230S", "ax1230sAuthIfIndex"),
        ("AX1230S", "ax1230sAuthSupplicantMac"),
        ("AX1230S", "ax1230sAuthMessage"))
)
if mibBuilder.loadTexts:
    ax1230sDot1xEventTrap.setStatus(
        ""
    )

ax1230sWauthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 33)
)
ax1230sWauthFailureTrap.setObjects(
      *(("AX1230S", "ax1230sAuthSysName"),
        ("AX1230S", "ax1230sAuthIfIndex"),
        ("AX1230S", "ax1230sAuthSupplicantMac"),
        ("AX1230S", "ax1230sAuthMessage"))
)
if mibBuilder.loadTexts:
    ax1230sWauthFailureTrap.setStatus(
        ""
    )

ax1230sWauthEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 34)
)
ax1230sWauthEventTrap.setObjects(
      *(("AX1230S", "ax1230sAuthSysName"),
        ("AX1230S", "ax1230sAuthIfIndex"),
        ("AX1230S", "ax1230sAuthSupplicantMac"),
        ("AX1230S", "ax1230sAuthMessage"))
)
if mibBuilder.loadTexts:
    ax1230sWauthEventTrap.setStatus(
        ""
    )

ax1230sMauthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 35)
)
ax1230sMauthFailureTrap.setObjects(
      *(("AX1230S", "ax1230sAuthSysName"),
        ("AX1230S", "ax1230sAuthIfIndex"),
        ("AX1230S", "ax1230sAuthSupplicantMac"),
        ("AX1230S", "ax1230sAuthMessage"))
)
if mibBuilder.loadTexts:
    ax1230sMauthFailureTrap.setStatus(
        ""
    )

ax1230sMauthEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 36)
)
ax1230sMauthEventTrap.setObjects(
      *(("AX1230S", "ax1230sAuthSysName"),
        ("AX1230S", "ax1230sAuthIfIndex"),
        ("AX1230S", "ax1230sAuthSupplicantMac"),
        ("AX1230S", "ax1230sAuthMessage"))
)
if mibBuilder.loadTexts:
    ax1230sMauthEventTrap.setStatus(
        ""
    )

ax1230sDot1xSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 37)
)
ax1230sDot1xSystemTrap.setObjects(
      *(("AX1230S", "ax1230sAuthSysName"),
        ("AX1230S", "ax1230sAuthIfIndex"),
        ("AX1230S", "ax1230sAuthSupplicantMac"),
        ("AX1230S", "ax1230sAuthMessage"))
)
if mibBuilder.loadTexts:
    ax1230sDot1xSystemTrap.setStatus(
        ""
    )

ax1230sWauthSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 38)
)
ax1230sWauthSystemTrap.setObjects(
      *(("AX1230S", "ax1230sAuthSysName"),
        ("AX1230S", "ax1230sAuthIfIndex"),
        ("AX1230S", "ax1230sAuthSupplicantMac"),
        ("AX1230S", "ax1230sAuthMessage"))
)
if mibBuilder.loadTexts:
    ax1230sWauthSystemTrap.setStatus(
        ""
    )

ax1230sMauthSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 39)
)
ax1230sMauthSystemTrap.setObjects(
      *(("AX1230S", "ax1230sAuthSysName"),
        ("AX1230S", "ax1230sAuthIfIndex"),
        ("AX1230S", "ax1230sAuthSupplicantMac"),
        ("AX1230S", "ax1230sAuthMessage"))
)
if mibBuilder.loadTexts:
    ax1230sMauthSystemTrap.setStatus(
        ""
    )

axsL2ldLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 51)
)
axsL2ldLinkDown.setObjects(
      *(("AX1230S", "axsL2ldPortIfIndex"),
        ("AX1230S", "axsL2ldPortSourcePortIfindex"),
        ("AX1230S", "axsL2ldPortDestinationPortIfindex"),
        ("AX1230S", "axsL2ldPortSourceVlan"))
)
if mibBuilder.loadTexts:
    axsL2ldLinkDown.setStatus(
        ""
    )

axsL2ldLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 52)
)
axsL2ldLinkUp.setObjects(
    ("AX1230S", "axsL2ldPortIfIndex")
)
if mibBuilder.loadTexts:
    axsL2ldLinkUp.setStatus(
        ""
    )

axsL2ldLoopDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 10, 0, 53)
)
axsL2ldLoopDetection.setObjects(
      *(("AX1230S", "axsL2ldPortIndex"),
        ("AX1230S", "axsL2ldPortIfIndex"),
        ("AX1230S", "axsL2ldPortSourcePortIfindex"),
        ("AX1230S", "axsL2ldPortSourceVlan"))
)
if mibBuilder.loadTexts:
    axsL2ldLoopDetection.setStatus(
        ""
    )

axsOadpNeighborCachelastChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 2, 0, 1)
)
axsOadpNeighborCachelastChangeTrap.setObjects(
    ("AX1230S", "axsOadpNeighborCacheLastChange")
)
if mibBuilder.loadTexts:
    axsOadpNeighborCachelastChangeTrap.setStatus(
        ""
    )

axsOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 1)
)
axsOspfVirtIfStateChange.setObjects(
      *(("AX1230S", "axsOspfVirtIfDomainNumber"),
        ("AX1230S", "axsOspfRouterId"),
        ("AX1230S", "axsOspfVirtIfAreaId"),
        ("AX1230S", "axsOspfVirtIfNeighbor"),
        ("AX1230S", "axsOspfVirtIfState"))
)
if mibBuilder.loadTexts:
    axsOspfVirtIfStateChange.setStatus(
        ""
    )

axsOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 2)
)
axsOspfNbrStateChange.setObjects(
      *(("AX1230S", "axsOspfNbrDomainNumber"),
        ("AX1230S", "axsOspfRouterId"),
        ("AX1230S", "axsOspfNbrIpAddr"),
        ("AX1230S", "axsOspfNbrAddressLessIndex"),
        ("AX1230S", "axsOspfNbrRtrId"),
        ("AX1230S", "axsOspfNbrState"))
)
if mibBuilder.loadTexts:
    axsOspfNbrStateChange.setStatus(
        ""
    )

axsOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 3)
)
axsOspfVirtNbrStateChange.setObjects(
      *(("AX1230S", "axsOspfVirtNbrDomainNumber"),
        ("AX1230S", "axsOspfRouterId"),
        ("AX1230S", "axsOspfVirtNbrArea"),
        ("AX1230S", "axsOspfVirtNbrRtrId"),
        ("AX1230S", "axsOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    axsOspfVirtNbrStateChange.setStatus(
        ""
    )

axsOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 4)
)
axsOspfIfConfigError.setObjects(
      *(("AX1230S", "axsOspfIfDomainNumber"),
        ("AX1230S", "axsOspfRouterId"),
        ("AX1230S", "axsOspfIfIpAddress"),
        ("AX1230S", "axsOspfAddressLessIf"),
        ("AX1230S", "axsOspfPacketSrc"),
        ("AX1230S", "axsOspfConfigErrorType"),
        ("AX1230S", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfIfConfigError.setStatus(
        ""
    )

axsOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 5)
)
axsOspfVirtIfConfigError.setObjects(
      *(("AX1230S", "axsOspfVirtIfDomainNumber"),
        ("AX1230S", "axsOspfRouterId"),
        ("AX1230S", "axsOspfVirtIfAreaId"),
        ("AX1230S", "axsOspfVirtIfNeighbor"),
        ("AX1230S", "axsOspfConfigErrorType"),
        ("AX1230S", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfVirtIfConfigError.setStatus(
        ""
    )

axsOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 6)
)
axsOspfIfAuthFailure.setObjects(
      *(("AX1230S", "axsOspfIfDomainNumber"),
        ("AX1230S", "axsOspfRouterId"),
        ("AX1230S", "axsOspfIfIpAddress"),
        ("AX1230S", "axsOspfAddressLessIf"),
        ("AX1230S", "axsOspfPacketSrc"),
        ("AX1230S", "axsOspfConfigErrorType"),
        ("AX1230S", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfIfAuthFailure.setStatus(
        ""
    )

axsOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 7)
)
axsOspfVirtIfAuthFailure.setObjects(
      *(("AX1230S", "axsOspfVirtIfDomainNumber"),
        ("AX1230S", "axsOspfRouterId"),
        ("AX1230S", "axsOspfVirtIfAreaId"),
        ("AX1230S", "axsOspfVirtIfNeighbor"),
        ("AX1230S", "axsOspfConfigErrorType"),
        ("AX1230S", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfVirtIfAuthFailure.setStatus(
        ""
    )

axsOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 16)
)
axsOspfIfStateChange.setObjects(
      *(("AX1230S", "axsOspfIfDomainNumber"),
        ("AX1230S", "axsOspfRouterId"),
        ("AX1230S", "axsOspfIfIpAddress"),
        ("AX1230S", "axsOspfAddressLessIf"),
        ("AX1230S", "axsOspfIfState"))
)
if mibBuilder.loadTexts:
    axsOspfIfStateChange.setStatus(
        ""
    )

axsStaticGatewayStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 38, 2, 0, 1)
)
axsStaticGatewayStateChange.setObjects(
      *(("AX1230S", "axsStaticGatewayAddr"),
        ("AX1230S", "axsStaticGatewayState"))
)
if mibBuilder.loadTexts:
    axsStaticGatewayStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX1230S",
    **{"VlanIndex": VlanIndex,
       "VlanIdOrZero": VlanIdOrZero,
       "alaxala": alaxala,
       "alaxalaProductId": alaxalaProductId,
       "axSwitch": axSwitch,
       "ax1230s": ax1230s,
       "ax1230sSystemMsgTrap": ax1230sSystemMsgTrap,
       "ax1230sStandbySystemUpTrap": ax1230sStandbySystemUpTrap,
       "ax1230sStandbySystemDownTrap": ax1230sStandbySystemDownTrap,
       "ax1230sTemperatureTrap": ax1230sTemperatureTrap,
       "ax1230sGsrpStateTransitionTrap": ax1230sGsrpStateTransitionTrap,
       "ax1230sEoeMsgTrap": ax1230sEoeMsgTrap,
       "ax1230sAirFanStopTrap": ax1230sAirFanStopTrap,
       "ax1230sPowerSupplyFailureTrap": ax1230sPowerSupplyFailureTrap,
       "ax1230sLoginSuccessTrap": ax1230sLoginSuccessTrap,
       "ax1230sLoginFailureTrap": ax1230sLoginFailureTrap,
       "ax1230sLogoutTrap": ax1230sLogoutTrap,
       "ax1230sMemoryUsageTrap": ax1230sMemoryUsageTrap,
       "ax1230sFrameErrorReceiveTrap": ax1230sFrameErrorReceiveTrap,
       "ax1230sFrameErrorSendTrap": ax1230sFrameErrorSendTrap,
       "axsBroadcastStormDetectTrap": axsBroadcastStormDetectTrap,
       "axsMulticastStormDetectTrap": axsMulticastStormDetectTrap,
       "axsUnicastStormDetectTrap": axsUnicastStormDetectTrap,
       "axsBroadcastStormPortInactivateTrap": axsBroadcastStormPortInactivateTrap,
       "axsMulticastStormPortInactivateTrap": axsMulticastStormPortInactivateTrap,
       "axsUniticastStormPortInactivateTrap": axsUniticastStormPortInactivateTrap,
       "axsBroadcastStormRecoverTrap": axsBroadcastStormRecoverTrap,
       "axsMulticastStormRecoverTrap": axsMulticastStormRecoverTrap,
       "axsUnicastStormRecoverTrap": axsUnicastStormRecoverTrap,
       "axsEfmoamUdldPortInactivateTrap": axsEfmoamUdldPortInactivateTrap,
       "axsEfmoamLoopDetectPortInactivateTrap": axsEfmoamLoopDetectPortInactivateTrap,
       "ax1230sDot1xFailureTrap": ax1230sDot1xFailureTrap,
       "ax1230sDot1xEventTrap": ax1230sDot1xEventTrap,
       "ax1230sWauthFailureTrap": ax1230sWauthFailureTrap,
       "ax1230sWauthEventTrap": ax1230sWauthEventTrap,
       "ax1230sMauthFailureTrap": ax1230sMauthFailureTrap,
       "ax1230sMauthEventTrap": ax1230sMauthEventTrap,
       "ax1230sDot1xSystemTrap": ax1230sDot1xSystemTrap,
       "ax1230sWauthSystemTrap": ax1230sWauthSystemTrap,
       "ax1230sMauthSystemTrap": ax1230sMauthSystemTrap,
       "axsL2ldLinkDown": axsL2ldLinkDown,
       "axsL2ldLinkUp": axsL2ldLinkUp,
       "axsL2ldLoopDetection": axsL2ldLoopDetection,
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
       "axsFdb": axsFdb,
       "axsFdbCounterTable": axsFdbCounterTable,
       "axsFdbCounterEntry": axsFdbCounterEntry,
       "axsFdbCounterNifIndex": axsFdbCounterNifIndex,
       "axsFdbCounterLineIndex": axsFdbCounterLineIndex,
       "axsFdbCounterCounts": axsFdbCounterCounts,
       "axsFdbCounterType": axsFdbCounterType,
       "axsFdbCounterLimits": axsFdbCounterLimits,
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
       "axsStatic": axsStatic,
       "axsStaticTable": axsStaticTable,
       "axsStaticGatewayEntry": axsStaticGatewayEntry,
       "axsStaticGatewayAddr": axsStaticGatewayAddr,
       "axsStaticGatewayState": axsStaticGatewayState,
       "axsStaticTraps": axsStaticTraps,
       "axsStaticGatewayStateChange": axsStaticGatewayStateChange,
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
       "ax1230sMib": ax1230sMib,
       "ax1230sSwitch": ax1230sSwitch,
       "ax1230sModelType": ax1230sModelType,
       "ax1230sSoftware": ax1230sSoftware,
       "ax1230sSoftwareName": ax1230sSoftwareName,
       "ax1230sSoftwareAbbreviation": ax1230sSoftwareAbbreviation,
       "ax1230sSoftwareVersion": ax1230sSoftwareVersion,
       "ax1230sSystemMsg": ax1230sSystemMsg,
       "ax1230sSystemMsgText": ax1230sSystemMsgText,
       "ax1230sSystemMsgType": ax1230sSystemMsgType,
       "ax1230sSystemMsgTimeStamp": ax1230sSystemMsgTimeStamp,
       "ax1230sSystemMsgLevel": ax1230sSystemMsgLevel,
       "ax1230sSystemMsgEventPoint": ax1230sSystemMsgEventPoint,
       "ax1230sSystemMsgEventInterfaceID": ax1230sSystemMsgEventInterfaceID,
       "ax1230sSystemMsgEventCode": ax1230sSystemMsgEventCode,
       "ax1230sSystemMsgAdditionalCode": ax1230sSystemMsgAdditionalCode,
       "ax1230sSnmpAgent": ax1230sSnmpAgent,
       "ax1230sSnmpSendReceiveSize": ax1230sSnmpSendReceiveSize,
       "ax1230sSnmpReceiveDelay": ax1230sSnmpReceiveDelay,
       "ax1230sSnmpContinuousSend": ax1230sSnmpContinuousSend,
       "ax1230sSnmpObjectMaxNumber": ax1230sSnmpObjectMaxNumber,
       "ax1230sLicense": ax1230sLicense,
       "ax1230sLicenseNumber": ax1230sLicenseNumber,
       "ax1230sLicenseTable": ax1230sLicenseTable,
       "ax1230sLicenseEntry": ax1230sLicenseEntry,
       "ax1230sLicenseIndex": ax1230sLicenseIndex,
       "ax1230sLicenseSerialNumber": ax1230sLicenseSerialNumber,
       "ax1230sLicenseOptionNumber": ax1230sLicenseOptionNumber,
       "ax1230sLicenseOptionTable": ax1230sLicenseOptionTable,
       "ax1230sLicenseOptionEntry": ax1230sLicenseOptionEntry,
       "ax1230sLicenseOptionIndex": ax1230sLicenseOptionIndex,
       "ax1230sLicenseOptionNumberIndex": ax1230sLicenseOptionNumberIndex,
       "ax1230sLicenseOptionSoftwareName": ax1230sLicenseOptionSoftwareName,
       "ax1230sLicenseOptionSoftwareAbbreviation": ax1230sLicenseOptionSoftwareAbbreviation,
       "ax1230sDevice": ax1230sDevice,
       "ax1230sChassis": ax1230sChassis,
       "ax1230sChassisMaxNumber": ax1230sChassisMaxNumber,
       "ax1230sChassisTable": ax1230sChassisTable,
       "ax1230sChassisEntry": ax1230sChassisEntry,
       "ax1230sChassisIndex": ax1230sChassisIndex,
       "ax1230sChassisType": ax1230sChassisType,
       "ax1230sChassisStatus": ax1230sChassisStatus,
       "ax1230sStsLedStatus": ax1230sStsLedStatus,
       "ax1230sCpuName": ax1230sCpuName,
       "ax1230sCpuClock": ax1230sCpuClock,
       "ax1230sMemoryTotalSize": ax1230sMemoryTotalSize,
       "ax1230sMemoryUsedSize": ax1230sMemoryUsedSize,
       "ax1230sMemoryFreeSize": ax1230sMemoryFreeSize,
       "ax1230sRomVersion": ax1230sRomVersion,
       "ax1230sCpuLoad1m": ax1230sCpuLoad1m,
       "ax1230sFlashTotalSize": ax1230sFlashTotalSize,
       "ax1230sFlashUsedSize": ax1230sFlashUsedSize,
       "ax1230sFlashFreeSize": ax1230sFlashFreeSize,
       "ax1230sSdCardStatus": ax1230sSdCardStatus,
       "ax1230sSdCardTotalSize": ax1230sSdCardTotalSize,
       "ax1230sSdCardUsedSize": ax1230sSdCardUsedSize,
       "ax1230sSdCardFreeSize": ax1230sSdCardFreeSize,
       "ax1230sPhysLineNumber": ax1230sPhysLineNumber,
       "ax1230sTemperatureStatusNumber": ax1230sTemperatureStatusNumber,
       "ax1230sPowerUnitNumber": ax1230sPowerUnitNumber,
       "ax1230sRedundantPsNumber": ax1230sRedundantPsNumber,
       "ax1230sFanNumber": ax1230sFanNumber,
       "ax1230sTotalAccumRunTime": ax1230sTotalAccumRunTime,
       "ax1230sCriticalAccumRunTime": ax1230sCriticalAccumRunTime,
       "ax1230sTemperatureStatusTable": ax1230sTemperatureStatusTable,
       "ax1230sTemperatureStatusEntry": ax1230sTemperatureStatusEntry,
       "ax1230sTemperatureStatusIndex": ax1230sTemperatureStatusIndex,
       "ax1230sTemperatureStatusDescr": ax1230sTemperatureStatusDescr,
       "ax1230sTemperatureStatusValue": ax1230sTemperatureStatusValue,
       "ax1230sTemperatureThreshold": ax1230sTemperatureThreshold,
       "ax1230sTemperatureState": ax1230sTemperatureState,
       "ax1230sPowerUnitTable": ax1230sPowerUnitTable,
       "ax1230sPowerUnitEntry": ax1230sPowerUnitEntry,
       "ax1230sPowerUnitIndex": ax1230sPowerUnitIndex,
       "ax1230sPowerConnectStatus": ax1230sPowerConnectStatus,
       "ax1230sPowerSupplyStatus": ax1230sPowerSupplyStatus,
       "ax1230sFanTable": ax1230sFanTable,
       "ax1230sFanEntry": ax1230sFanEntry,
       "ax1230sFanIndex": ax1230sFanIndex,
       "ax1230sFanStatus": ax1230sFanStatus,
       "ax1230sRedundantPsTable": ax1230sRedundantPsTable,
       "ax1230sRedundantPsEntry": ax1230sRedundantPsEntry,
       "ax1230sRedundantPsIndex": ax1230sRedundantPsIndex,
       "ax1230sRedundantPsConnectStatus": ax1230sRedundantPsConnectStatus,
       "ax1230sRedundantPsStatus": ax1230sRedundantPsStatus,
       "ax1230sPhysLine": ax1230sPhysLine,
       "ax1230sPhysLineTable": ax1230sPhysLineTable,
       "ax1230sPhysLineEntry": ax1230sPhysLineEntry,
       "ax1230sPhysLineIndex": ax1230sPhysLineIndex,
       "ax1230sPhysLineConnectorType": ax1230sPhysLineConnectorType,
       "ax1230sPhysLineOperStatus": ax1230sPhysLineOperStatus,
       "ax1230sPhysLineIfIndexNumber": ax1230sPhysLineIfIndexNumber,
       "ax1230sPhysLineTransceiverStatus": ax1230sPhysLineTransceiverStatus,
       "ax1230sManagementMIB": ax1230sManagementMIB,
       "ax1230sOperationCommand": ax1230sOperationCommand,
       "ax1230sFdbClearMIB": ax1230sFdbClearMIB,
       "ax1230sFdbClearSet": ax1230sFdbClearSet,
       "ax1230sFdbClearReqTime": ax1230sFdbClearReqTime,
       "ax1230sFdbClearSuccessTime": ax1230sFdbClearSuccessTime,
       "ax1230sAuth": ax1230sAuth,
       "ax1230sAuthInfo": ax1230sAuthInfo,
       "ax1230sAuthSysName": ax1230sAuthSysName,
       "ax1230sAuthIfIndex": ax1230sAuthIfIndex,
       "ax1230sAuthSupplicantMac": ax1230sAuthSupplicantMac,
       "ax1230sAuthMessage": ax1230sAuthMessage,
       "ax1230sDot1x": ax1230sDot1x,
       "ax1230sDot1xFailure": ax1230sDot1xFailure,
       "ax1230sDot1xEvent": ax1230sDot1xEvent,
       "ax1230sDot1xSystem": ax1230sDot1xSystem,
       "ax1230sWauth": ax1230sWauth,
       "ax1230sWauthFailure": ax1230sWauthFailure,
       "ax1230sWauthEvent": ax1230sWauthEvent,
       "ax1230sWauthSystem": ax1230sWauthSystem,
       "ax1230sMauth": ax1230sMauth,
       "ax1230sMauthFailure": ax1230sMauthFailure,
       "ax1230sMauthEvent": ax1230sMauthEvent,
       "ax1230sMauthSystem": ax1230sMauthSystem}
)
