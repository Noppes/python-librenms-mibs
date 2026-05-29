# SNMP MIB module (AX260A) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX260A-MIB

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
_Ax260a_ObjectIdentity = ObjectIdentity
ax260a = _Ax260a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23)
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
    (0, "AX260A", "axsIfStatsIndex"),
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
    (0, "AX260A", "axsEtherTxQoSStatsIndex"),
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
    (0, "AX260A", "axsEtherTxQoSStatsQueueIndex"),
    (0, "AX260A", "axsEtherTxQoSStatsQueueQueIndex"),
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
    (0, "AX260A", "axsGsrpGroupId"),
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
    (0, "AX260A", "axsGsrpGroupId"),
    (0, "AX260A", "axsGsrpVlanGroupId"),
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
    (0, "AX260A", "axsGsrpNeighborGroupId"),
    (0, "AX260A", "axsGsrpNeighborMacAddress"),
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
    (0, "AX260A", "axsGsrpNeighborGroupId"),
    (0, "AX260A", "axsGsrpNeighborVlanGroupId"),
    (0, "AX260A", "axsGsrpNeighborMacAddress"),
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
_AxsFdb_ObjectIdentity = ObjectIdentity
axsFdb = _AxsFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5)
)
_AxsFdbCounterTable_Object = MibTable
axsFdbCounterTable = _AxsFdbCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    axsFdbCounterTable.setStatus("mandatory")
_AxsFdbCounterEntry_Object = MibTableRow
axsFdbCounterEntry = _AxsFdbCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1)
)
axsFdbCounterEntry.setIndexNames(
    (0, "AX260A", "axsFdbCounterNifIndex"),
    (0, "AX260A", "axsFdbCounterLineIndex"),
)
if mibBuilder.loadTexts:
    axsFdbCounterEntry.setStatus("mandatory")
_AxsFdbCounterNifIndex_Type = Integer32
_AxsFdbCounterNifIndex_Object = MibTableColumn
axsFdbCounterNifIndex = _AxsFdbCounterNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1, 1),
    _AxsFdbCounterNifIndex_Type()
)
axsFdbCounterNifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsFdbCounterNifIndex.setStatus("mandatory")
_AxsFdbCounterLineIndex_Type = Integer32
_AxsFdbCounterLineIndex_Object = MibTableColumn
axsFdbCounterLineIndex = _AxsFdbCounterLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1, 2),
    _AxsFdbCounterLineIndex_Type()
)
axsFdbCounterLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsFdbCounterLineIndex.setStatus("mandatory")
_AxsFdbCounterCounts_Type = Counter32
_AxsFdbCounterCounts_Object = MibTableColumn
axsFdbCounterCounts = _AxsFdbCounterCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1, 3),
    _AxsFdbCounterCounts_Type()
)
axsFdbCounterCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsFdbCounterCounts.setStatus("mandatory")


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
    axsFdbCounterType.setStatus("mandatory")
_AxsFdbCounterLimits_Type = Counter32
_AxsFdbCounterLimits_Object = MibTableColumn
axsFdbCounterLimits = _AxsFdbCounterLimits_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 5, 1, 1, 5),
    _AxsFdbCounterLimits_Type()
)
axsFdbCounterLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsFdbCounterLimits.setStatus("mandatory")
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
    (0, "AX260A", "axsVBBaseIndex"),
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
    (0, "AX260A", "axsVBBasePortIndex"),
    (0, "AX260A", "axsVBBasePort"),
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
    (0, "AX260A", "axsVBStpIndex"),
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
    (0, "AX260A", "axsVBStpPortIndex"),
    (0, "AX260A", "axsVBStpPort"),
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
    (0, "AX260A", "axsVBTpIndex"),
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
    (0, "AX260A", "axsVBTpFdbIndex"),
    (0, "AX260A", "axsVBTpFdbAddress"),
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
    (0, "AX260A", "axsVBTpPortIndex"),
    (0, "AX260A", "axsVBTpPort"),
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
    (0, "AX260A", "axsVBStaticIndex"),
    (0, "AX260A", "axsVBStaticAddress"),
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
    (0, "AX260A", "axsVlanTagTranslationVlanId"),
    (0, "AX260A", "axsVlanTagTranslationTranslatedId"),
)
if mibBuilder.loadTexts:
    axsVlanTagTranslationEntry.setStatus("mandatory")
_AxsVlanTagTranslationVlanId_Type = Integer32
_AxsVlanTagTranslationVlanId_Object = MibTableColumn
axsVlanTagTranslationVlanId = _AxsVlanTagTranslationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1, 1),
    _AxsVlanTagTranslationVlanId_Type()
)
axsVlanTagTranslationVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsVlanTagTranslationVlanId.setStatus("mandatory")
_AxsVlanTagTranslationTranslatedId_Type = Integer32
_AxsVlanTagTranslationTranslatedId_Object = MibTableColumn
axsVlanTagTranslationTranslatedId = _AxsVlanTagTranslationTranslatedId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 6, 10, 1, 1, 2),
    _AxsVlanTagTranslationTranslatedId_Type()
)
axsVlanTagTranslationTranslatedId.setMaxAccess("read-only")
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
    (0, "AX260A", "axsOadpPortConfigIfIndex"),
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
    (0, "AX260A", "axsOadpIfIndex"),
    (0, "AX260A", "axsOadpTagID"),
    (0, "AX260A", "axsOadpNeighborIndex"),
    (0, "AX260A", "axsOadpNeighborTagID"),
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
    (0, "AX260A", "axsAccessFilterStatsInifIndex"),
    (0, "AX260A", "axsAccessFilterStatsInifIndexType"),
    (0, "AX260A", "axsAccessFilterStatsInListIndex"),
    (0, "AX260A", "axsAccessFilterStatsInSequenceNumber"),
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
    (0, "AX260A", "axsAccessFilterStatsOutifIndex"),
    (0, "AX260A", "axsAccessFilterStatsOutifIndexType"),
    (0, "AX260A", "axsAccessFilterStatsOutListIndex"),
    (0, "AX260A", "axsAccessFilterStatsOutSequenceNumber"),
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
    (0, "AX260A", "axsQosFlowStatsInifIndex"),
    (0, "AX260A", "axsQosFlowStatsInifIndexType"),
    (0, "AX260A", "axsQosFlowStatsInListIndex"),
    (0, "AX260A", "axsQosFlowStatsInSequenceNumber"),
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
    (0, "AX260A", "axsL2ldPortIndex"),
    (0, "AX260A", "axsL2ldPortIfIndex"),
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
    axsOspfGeneralTable.setStatus("mandatory")
_AxsOspfGeneralEntry_Object = MibTableRow
axsOspfGeneralEntry = _AxsOspfGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 1, 1)
)
axsOspfGeneralEntry.setIndexNames(
    (0, "AX260A", "axsOspfGeneralDomainNumber"),
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
    (0, "AX260A", "axsOspfAreaDomainNumber"),
    (0, "AX260A", "axsOspfAreaId"),
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
    (0, "AX260A", "axsOspfStubDomainNumber"),
    (0, "AX260A", "axsOspfStubAreaId"),
    (0, "AX260A", "axsOspfStubTOS"),
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
    (0, "AX260A", "axsOspfLsdbDomainNumber"),
    (0, "AX260A", "axsOspfLsdbAreaId"),
    (0, "AX260A", "axsOspfLsdbType"),
    (0, "AX260A", "axsOspfLsdbLsid"),
    (0, "AX260A", "axsOspfLsdbRouterId"),
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
    (0, "AX260A", "axsOspfAreaRangeDomainNumber"),
    (0, "AX260A", "axsOspfAreaRangeAreaId"),
    (0, "AX260A", "axsOspfAreaRangeNet"),
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
    (0, "AX260A", "axsOspfIfDomainNumber"),
    (0, "AX260A", "axsOspfIfIpAddress"),
    (0, "AX260A", "axsOspfAddressLessIf"),
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
    (0, "AX260A", "axsOspfIfMetricDomainNumber"),
    (0, "AX260A", "axsOspfIfMetricIpAddress"),
    (0, "AX260A", "axsOspfIfMetricAddressLessIf"),
    (0, "AX260A", "axsOspfIfMetricTOS"),
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
    (0, "AX260A", "axsOspfVirtIfDomainNumber"),
    (0, "AX260A", "axsOspfVirtIfAreaId"),
    (0, "AX260A", "axsOspfVirtIfNeighbor"),
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
    (0, "AX260A", "axsOspfNbrDomainNumber"),
    (0, "AX260A", "axsOspfNbrIpAddr"),
    (0, "AX260A", "axsOspfNbrAddressLessIndex"),
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
    (0, "AX260A", "axsOspfVirtNbrDomainNumber"),
    (0, "AX260A", "axsOspfVirtNbrArea"),
    (0, "AX260A", "axsOspfVirtNbrRtrId"),
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
    (0, "AX260A", "axsOspfExtLsdbDomainNumber"),
    (0, "AX260A", "axsOspfExtLsdbType"),
    (0, "AX260A", "axsOspfExtLsdbLsid"),
    (0, "AX260A", "axsOspfExtLsdbRouterId"),
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
    (0, "AX260A", "axsOspfAreaAggregateDomainNumber"),
    (0, "AX260A", "axsOspfAreaAggregateAreaID"),
    (0, "AX260A", "axsOspfAreaAggregateLsdbType"),
    (0, "AX260A", "axsOspfAreaAggregateNet"),
    (0, "AX260A", "axsOspfAreaAggregateMask"),
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
    (0, "AX260A", "axsOspfTrapDomainNumber"),
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
axsOspfSetTrap.setMaxAccess("read-write")
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
    (0, "AX260A", "axsOspfv3GeneralDomainNumber"),
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
    (0, "AX260A", "axsOspfv3AreaDomainNumber"),
    (0, "AX260A", "axsOspfv3AreaId"),
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
    (0, "AX260A", "axsOspfv3AsLsdbDomainNumber"),
    (0, "AX260A", "axsOspfv3AsLsdbType"),
    (0, "AX260A", "axsOspfv3AsLsdbRouterId"),
    (0, "AX260A", "axsOspfv3AsLsdbLsid"),
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
    (0, "AX260A", "axsOspfv3AreaLsdbDomainNumber"),
    (0, "AX260A", "axsOspfv3AreaLsdbAreaId"),
    (0, "AX260A", "axsOspfv3AreaLsdbType"),
    (0, "AX260A", "axsOspfv3AreaLsdbRouterId"),
    (0, "AX260A", "axsOspfv3AreaLsdbLsid"),
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
    (0, "AX260A", "axsOspfv3LinkLsdbDomainNumber"),
    (0, "AX260A", "axsOspfv3LinkLsdbIfIndex"),
    (0, "AX260A", "axsOspfv3LinkLsdbType"),
    (0, "AX260A", "axsOspfv3LinkLsdbRouterId"),
    (0, "AX260A", "axsOspfv3LinkLsdbLsid"),
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
    (0, "AX260A", "axsOspfv3IfDomainNumber"),
    (0, "AX260A", "axsOspfv3IfIndex"),
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
    (0, "AX260A", "axsOspfv3VirtIfDomainNumber"),
    (0, "AX260A", "axsOspfv3VirtIfAreaId"),
    (0, "AX260A", "axsOspfv3VirtIfNeighbor"),
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
    (0, "AX260A", "axsOspfv3NbrDomainNumber"),
    (0, "AX260A", "axsOspfv3NbrIfIndex"),
    (0, "AX260A", "axsOspfv3NbrIpv6Addr"),
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
    (0, "AX260A", "axsOspfv3VirtNbrDomainNumber"),
    (0, "AX260A", "axsOspfv3VirtNbrArea"),
    (0, "AX260A", "axsOspfv3VirtNbrRtrId"),
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
    (0, "AX260A", "axsOspfv3AreaAggregateDomainNumber"),
    (0, "AX260A", "axsOspfv3AreaAggregateAreaID"),
    (0, "AX260A", "axsOspfv3AreaAggregateAreaLsdbType"),
    (0, "AX260A", "axsOspfv3AreaAggregateIndex"),
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
_AxsUlrVersion_Type = Integer32
_AxsUlrVersion_Object = MibScalar
axsUlrVersion = _AxsUlrVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 20, 1, 1),
    _AxsUlrVersion_Type()
)
axsUlrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsUlrVersion.setStatus("mandatory")
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
    (0, "AX260A", "axsUlrPortIfIndex"),
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
              8,
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
          ("system-exception", 8),
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
    (0, "AX260A", "axslldpPortConfigPortNum"),
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
    (0, "AX260A", "axslldpStatsPortNum"),
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
    (0, "AX260A", "axslldpLocPortNum"),
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
    (0, "AX260A", "axslldpRemLocalPortNum"),
    (0, "AX260A", "axslldpRemIndex"),
)
if mibBuilder.loadTexts:
    axslldpRemEntry.setStatus("mandatory")
_AxslldpRemLocalPortNum_Type = Integer32
_AxslldpRemLocalPortNum_Object = MibTableColumn
axslldpRemLocalPortNum = _AxslldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 2),
    _AxslldpRemLocalPortNum_Type()
)
axslldpRemLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axslldpRemLocalPortNum.setStatus("mandatory")
_AxslldpRemIndex_Type = Integer32
_AxslldpRemIndex_Object = MibTableColumn
axslldpRemIndex = _AxslldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 100, 4, 1, 1, 3),
    _AxslldpRemIndex_Type()
)
axslldpRemIndex.setMaxAccess("read-only")
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
    (0, "AX260A", "axslldpRemOriginInfoPortNum"),
    (0, "AX260A", "axslldpRemOriginInfoIndex"),
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
    (0, "AX260A", "axsAxrpGroupRingId"),
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
    (0, "AX260A", "axsAxrpVlanGroupRingId"),
    (0, "AX260A", "axsAxrpVlanGroupId"),
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
    (0, "AX260A", "axsPconModuleIndex"),
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
    (0, "AX260A", "axsPconModuleIndex"),
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
    (0, "AX260A", "axsPconModuleIndex"),
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
_AxsStack_ObjectIdentity = ObjectIdentity
axsStack = _AxsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400)
)
_AxsStackGlobalInfo_ObjectIdentity = ObjectIdentity
axsStackGlobalInfo = _AxsStackGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 1)
)
_AxsStackMasterSwitch_Type = Integer32
_AxsStackMasterSwitch_Object = MibScalar
axsStackMasterSwitch = _AxsStackMasterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 1, 1),
    _AxsStackMasterSwitch_Type()
)
axsStackMasterSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackMasterSwitch.setStatus("mandatory")
_AxsStackMember_ObjectIdentity = ObjectIdentity
axsStackMember = _AxsStackMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2)
)
_AxsStackMemberTable_Object = MibTable
axsStackMemberTable = _AxsStackMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1)
)
if mibBuilder.loadTexts:
    axsStackMemberTable.setStatus("mandatory")
_AxsStackMemberEntry_Object = MibTableRow
axsStackMemberEntry = _AxsStackMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1)
)
axsStackMemberEntry.setIndexNames(
    (0, "AX260A", "axsStackMemberIndex"),
)
if mibBuilder.loadTexts:
    axsStackMemberEntry.setStatus("mandatory")
_AxsStackMemberIndex_Type = Integer32
_AxsStackMemberIndex_Object = MibTableColumn
axsStackMemberIndex = _AxsStackMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 1),
    _AxsStackMemberIndex_Type()
)
axsStackMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStackMemberIndex.setStatus("mandatory")


class _AxsStackModelType_Type(Integer32):
    """Custom type axsStackModelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2001)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("model-AX260A-08TF", 2001))
    )


_AxsStackModelType_Type.__name__ = "Integer32"
_AxsStackModelType_Object = MibTableColumn
axsStackModelType = _AxsStackModelType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 2),
    _AxsStackModelType_Type()
)
axsStackModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackModelType.setStatus("mandatory")


class _AxsStackSoftwareName_Type(DisplayString):
    """Custom type axsStackSoftwareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AxsStackSoftwareName_Type.__name__ = "DisplayString"
_AxsStackSoftwareName_Object = MibTableColumn
axsStackSoftwareName = _AxsStackSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 3),
    _AxsStackSoftwareName_Type()
)
axsStackSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackSoftwareName.setStatus("mandatory")


class _AxsStackSoftwareAbbreviation_Type(DisplayString):
    """Custom type axsStackSoftwareAbbreviation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AxsStackSoftwareAbbreviation_Type.__name__ = "DisplayString"
_AxsStackSoftwareAbbreviation_Object = MibTableColumn
axsStackSoftwareAbbreviation = _AxsStackSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 4),
    _AxsStackSoftwareAbbreviation_Type()
)
axsStackSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackSoftwareAbbreviation.setStatus("mandatory")


class _AxsStackSoftwareVersion_Type(DisplayString):
    """Custom type axsStackSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AxsStackSoftwareVersion_Type.__name__ = "DisplayString"
_AxsStackSoftwareVersion_Object = MibTableColumn
axsStackSoftwareVersion = _AxsStackSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 5),
    _AxsStackSoftwareVersion_Type()
)
axsStackSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackSoftwareVersion.setStatus("mandatory")


class _AxsStackBootReason_Type(Integer32):
    """Custom type axsStackBootReason based on Integer32"""
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
          ("system-exception", 8),
          ("wake-on-rtc", 9),
          ("wake-on-reset", 10))
    )


_AxsStackBootReason_Type.__name__ = "Integer32"
_AxsStackBootReason_Object = MibTableColumn
axsStackBootReason = _AxsStackBootReason_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 6),
    _AxsStackBootReason_Type()
)
axsStackBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackBootReason.setStatus("mandatory")


class _AxsStackPconModuleMode_Type(Integer32):
    """Custom type axsStackPconModuleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("saving", 4))
    )


_AxsStackPconModuleMode_Type.__name__ = "Integer32"
_AxsStackPconModuleMode_Object = MibTableColumn
axsStackPconModuleMode = _AxsStackPconModuleMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 7),
    _AxsStackPconModuleMode_Type()
)
axsStackPconModuleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackPconModuleMode.setStatus("mandatory")
_AxsStackPconPowerConMaxPower_Type = Gauge32
_AxsStackPconPowerConMaxPower_Object = MibTableColumn
axsStackPconPowerConMaxPower = _AxsStackPconPowerConMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 8),
    _AxsStackPconPowerConMaxPower_Type()
)
axsStackPconPowerConMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackPconPowerConMaxPower.setStatus("mandatory")
_AxsStackPconPowerConPowerConsumption_Type = Counter64
_AxsStackPconPowerConPowerConsumption_Object = MibTableColumn
axsStackPconPowerConPowerConsumption = _AxsStackPconPowerConPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 9),
    _AxsStackPconPowerConPowerConsumption_Type()
)
axsStackPconPowerConPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackPconPowerConPowerConsumption.setStatus("mandatory")
_AxsStackPconPowerConPowerMeter_Type = Gauge32
_AxsStackPconPowerConPowerMeter_Object = MibTableColumn
axsStackPconPowerConPowerMeter = _AxsStackPconPowerConPowerMeter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 2, 1, 1, 10),
    _AxsStackPconPowerConPowerMeter_Type()
)
axsStackPconPowerConPowerMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackPconPowerConPowerMeter.setStatus("mandatory")
_AxsStackMemberLicense_ObjectIdentity = ObjectIdentity
axsStackMemberLicense = _AxsStackMemberLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3)
)
_AxsStackMemberLicenseTable_Object = MibTable
axsStackMemberLicenseTable = _AxsStackMemberLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 1)
)
if mibBuilder.loadTexts:
    axsStackMemberLicenseTable.setStatus("mandatory")
_AxsStackMemberLicenseEntry_Object = MibTableRow
axsStackMemberLicenseEntry = _AxsStackMemberLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 1, 1)
)
axsStackMemberLicenseEntry.setIndexNames(
    (0, "AX260A", "axsStackMemberIndex"),
    (0, "AX260A", "axsStackMemberLicenseIndex"),
)
if mibBuilder.loadTexts:
    axsStackMemberLicenseEntry.setStatus("mandatory")
_AxsStackMemberLicenseIndex_Type = Integer32
_AxsStackMemberLicenseIndex_Object = MibTableColumn
axsStackMemberLicenseIndex = _AxsStackMemberLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 1, 1, 1),
    _AxsStackMemberLicenseIndex_Type()
)
axsStackMemberLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStackMemberLicenseIndex.setStatus("mandatory")
_AxsStackMemberLicenseSerialNumber_Type = DisplayString
_AxsStackMemberLicenseSerialNumber_Object = MibTableColumn
axsStackMemberLicenseSerialNumber = _AxsStackMemberLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 1, 1, 2),
    _AxsStackMemberLicenseSerialNumber_Type()
)
axsStackMemberLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackMemberLicenseSerialNumber.setStatus("mandatory")
_AxsStackMemberLicenseOptionNumber_Type = Integer32
_AxsStackMemberLicenseOptionNumber_Object = MibTableColumn
axsStackMemberLicenseOptionNumber = _AxsStackMemberLicenseOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 1, 1, 3),
    _AxsStackMemberLicenseOptionNumber_Type()
)
axsStackMemberLicenseOptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackMemberLicenseOptionNumber.setStatus("mandatory")
_AxsStackMemberLicenseOptionTable_Object = MibTable
axsStackMemberLicenseOptionTable = _AxsStackMemberLicenseOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 2)
)
if mibBuilder.loadTexts:
    axsStackMemberLicenseOptionTable.setStatus("mandatory")
_AxsStackMemberLicenseOptionEntry_Object = MibTableRow
axsStackMemberLicenseOptionEntry = _AxsStackMemberLicenseOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 2, 1)
)
axsStackMemberLicenseOptionEntry.setIndexNames(
    (0, "AX260A", "axsStackMemberIndex"),
    (0, "AX260A", "axsStackMemberLicenseOptionIndex"),
    (0, "AX260A", "axsStackMemberLicenseOptionNumberIndex"),
)
if mibBuilder.loadTexts:
    axsStackMemberLicenseOptionEntry.setStatus("mandatory")
_AxsStackMemberLicenseOptionIndex_Type = Integer32
_AxsStackMemberLicenseOptionIndex_Object = MibTableColumn
axsStackMemberLicenseOptionIndex = _AxsStackMemberLicenseOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 2, 1, 1),
    _AxsStackMemberLicenseOptionIndex_Type()
)
axsStackMemberLicenseOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStackMemberLicenseOptionIndex.setStatus("mandatory")
_AxsStackMemberLicenseOptionNumberIndex_Type = Integer32
_AxsStackMemberLicenseOptionNumberIndex_Object = MibTableColumn
axsStackMemberLicenseOptionNumberIndex = _AxsStackMemberLicenseOptionNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 2, 1, 2),
    _AxsStackMemberLicenseOptionNumberIndex_Type()
)
axsStackMemberLicenseOptionNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsStackMemberLicenseOptionNumberIndex.setStatus("mandatory")
_AxsStackMemberLicenseOptionSoftwareName_Type = DisplayString
_AxsStackMemberLicenseOptionSoftwareName_Object = MibTableColumn
axsStackMemberLicenseOptionSoftwareName = _AxsStackMemberLicenseOptionSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 2, 1, 3),
    _AxsStackMemberLicenseOptionSoftwareName_Type()
)
axsStackMemberLicenseOptionSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackMemberLicenseOptionSoftwareName.setStatus("mandatory")
_AxsStackMemberLicenseOptionSoftwareAbbreviation_Type = DisplayString
_AxsStackMemberLicenseOptionSoftwareAbbreviation_Object = MibTableColumn
axsStackMemberLicenseOptionSoftwareAbbreviation = _AxsStackMemberLicenseOptionSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 400, 3, 2, 1, 4),
    _AxsStackMemberLicenseOptionSoftwareAbbreviation_Type()
)
axsStackMemberLicenseOptionSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axsStackMemberLicenseOptionSoftwareAbbreviation.setStatus("mandatory")
_Ax260aMib_ObjectIdentity = ObjectIdentity
ax260aMib = _Ax260aMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23)
)
_Ax260aSwitch_ObjectIdentity = ObjectIdentity
ax260aSwitch = _Ax260aSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1)
)


class _Ax260aModelType_Type(Integer32):
    """Custom type ax260aModelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2000,
              2001)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("model-AX260A-08T", 2000),
          ("model-AX260A-08TF", 2001))
    )


_Ax260aModelType_Type.__name__ = "Integer32"
_Ax260aModelType_Object = MibScalar
ax260aModelType = _Ax260aModelType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 1),
    _Ax260aModelType_Type()
)
ax260aModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aModelType.setStatus("mandatory")
_Ax260aSoftware_ObjectIdentity = ObjectIdentity
ax260aSoftware = _Ax260aSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 2)
)


class _Ax260aSoftwareName_Type(DisplayString):
    """Custom type ax260aSoftwareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax260aSoftwareName_Type.__name__ = "DisplayString"
_Ax260aSoftwareName_Object = MibScalar
ax260aSoftwareName = _Ax260aSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 2, 1),
    _Ax260aSoftwareName_Type()
)
ax260aSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSoftwareName.setStatus("mandatory")


class _Ax260aSoftwareAbbreviation_Type(DisplayString):
    """Custom type ax260aSoftwareAbbreviation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax260aSoftwareAbbreviation_Type.__name__ = "DisplayString"
_Ax260aSoftwareAbbreviation_Object = MibScalar
ax260aSoftwareAbbreviation = _Ax260aSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 2, 2),
    _Ax260aSoftwareAbbreviation_Type()
)
ax260aSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSoftwareAbbreviation.setStatus("mandatory")


class _Ax260aSoftwareVersion_Type(DisplayString):
    """Custom type ax260aSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ax260aSoftwareVersion_Type.__name__ = "DisplayString"
_Ax260aSoftwareVersion_Object = MibScalar
ax260aSoftwareVersion = _Ax260aSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 2, 3),
    _Ax260aSoftwareVersion_Type()
)
ax260aSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSoftwareVersion.setStatus("mandatory")
_Ax260aSystemMsg_ObjectIdentity = ObjectIdentity
ax260aSystemMsg = _Ax260aSystemMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 3)
)


class _Ax260aSystemMsgText_Type(DisplayString):
    """Custom type ax260aSystemMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Ax260aSystemMsgText_Type.__name__ = "DisplayString"
_Ax260aSystemMsgText_Object = MibScalar
ax260aSystemMsgText = _Ax260aSystemMsgText_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 3, 1),
    _Ax260aSystemMsgText_Type()
)
ax260aSystemMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSystemMsgText.setStatus("mandatory")


class _Ax260aSystemMsgType_Type(OctetString):
    """Custom type ax260aSystemMsgType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Ax260aSystemMsgType_Type.__name__ = "OctetString"
_Ax260aSystemMsgType_Object = MibScalar
ax260aSystemMsgType = _Ax260aSystemMsgType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 3, 2),
    _Ax260aSystemMsgType_Type()
)
ax260aSystemMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSystemMsgType.setStatus("mandatory")


class _Ax260aSystemMsgTimeStamp_Type(DisplayString):
    """Custom type ax260aSystemMsgTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Ax260aSystemMsgTimeStamp_Type.__name__ = "DisplayString"
_Ax260aSystemMsgTimeStamp_Object = MibScalar
ax260aSystemMsgTimeStamp = _Ax260aSystemMsgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 3, 3),
    _Ax260aSystemMsgTimeStamp_Type()
)
ax260aSystemMsgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSystemMsgTimeStamp.setStatus("mandatory")


class _Ax260aSystemMsgLevel_Type(OctetString):
    """Custom type ax260aSystemMsgLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Ax260aSystemMsgLevel_Type.__name__ = "OctetString"
_Ax260aSystemMsgLevel_Object = MibScalar
ax260aSystemMsgLevel = _Ax260aSystemMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 3, 4),
    _Ax260aSystemMsgLevel_Type()
)
ax260aSystemMsgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSystemMsgLevel.setStatus("mandatory")


class _Ax260aSystemMsgEventPoint_Type(DisplayString):
    """Custom type ax260aSystemMsgEventPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ax260aSystemMsgEventPoint_Type.__name__ = "DisplayString"
_Ax260aSystemMsgEventPoint_Object = MibScalar
ax260aSystemMsgEventPoint = _Ax260aSystemMsgEventPoint_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 3, 5),
    _Ax260aSystemMsgEventPoint_Type()
)
ax260aSystemMsgEventPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSystemMsgEventPoint.setStatus("mandatory")


class _Ax260aSystemMsgEventInterfaceID_Type(DisplayString):
    """Custom type ax260aSystemMsgEventInterfaceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Ax260aSystemMsgEventInterfaceID_Type.__name__ = "DisplayString"
_Ax260aSystemMsgEventInterfaceID_Object = MibScalar
ax260aSystemMsgEventInterfaceID = _Ax260aSystemMsgEventInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 3, 6),
    _Ax260aSystemMsgEventInterfaceID_Type()
)
ax260aSystemMsgEventInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSystemMsgEventInterfaceID.setStatus("mandatory")


class _Ax260aSystemMsgEventCode_Type(OctetString):
    """Custom type ax260aSystemMsgEventCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Ax260aSystemMsgEventCode_Type.__name__ = "OctetString"
_Ax260aSystemMsgEventCode_Object = MibScalar
ax260aSystemMsgEventCode = _Ax260aSystemMsgEventCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 3, 7),
    _Ax260aSystemMsgEventCode_Type()
)
ax260aSystemMsgEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSystemMsgEventCode.setStatus("mandatory")


class _Ax260aSystemMsgAdditionalCode_Type(OctetString):
    """Custom type ax260aSystemMsgAdditionalCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Ax260aSystemMsgAdditionalCode_Type.__name__ = "OctetString"
_Ax260aSystemMsgAdditionalCode_Object = MibScalar
ax260aSystemMsgAdditionalCode = _Ax260aSystemMsgAdditionalCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 3, 8),
    _Ax260aSystemMsgAdditionalCode_Type()
)
ax260aSystemMsgAdditionalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSystemMsgAdditionalCode.setStatus("mandatory")
_Ax260aSnmpAgent_ObjectIdentity = ObjectIdentity
ax260aSnmpAgent = _Ax260aSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 4)
)
_Ax260aSnmpSendReceiveSize_Type = Integer32
_Ax260aSnmpSendReceiveSize_Object = MibScalar
ax260aSnmpSendReceiveSize = _Ax260aSnmpSendReceiveSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 4, 1),
    _Ax260aSnmpSendReceiveSize_Type()
)
ax260aSnmpSendReceiveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSnmpSendReceiveSize.setStatus("mandatory")
_Ax260aSnmpReceiveDelay_Type = Integer32
_Ax260aSnmpReceiveDelay_Object = MibScalar
ax260aSnmpReceiveDelay = _Ax260aSnmpReceiveDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 4, 2),
    _Ax260aSnmpReceiveDelay_Type()
)
ax260aSnmpReceiveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSnmpReceiveDelay.setStatus("mandatory")
_Ax260aSnmpContinuousSend_Type = Integer32
_Ax260aSnmpContinuousSend_Object = MibScalar
ax260aSnmpContinuousSend = _Ax260aSnmpContinuousSend_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 4, 3),
    _Ax260aSnmpContinuousSend_Type()
)
ax260aSnmpContinuousSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSnmpContinuousSend.setStatus("mandatory")
_Ax260aSnmpObjectMaxNumber_Type = Integer32
_Ax260aSnmpObjectMaxNumber_Object = MibScalar
ax260aSnmpObjectMaxNumber = _Ax260aSnmpObjectMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 4, 4),
    _Ax260aSnmpObjectMaxNumber_Type()
)
ax260aSnmpObjectMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSnmpObjectMaxNumber.setStatus("mandatory")
_Ax260aLicense_ObjectIdentity = ObjectIdentity
ax260aLicense = _Ax260aLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6)
)
_Ax260aLicenseNumber_Type = Integer32
_Ax260aLicenseNumber_Object = MibScalar
ax260aLicenseNumber = _Ax260aLicenseNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 1),
    _Ax260aLicenseNumber_Type()
)
ax260aLicenseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aLicenseNumber.setStatus("mandatory")
_Ax260aLicenseTable_Object = MibTable
ax260aLicenseTable = _Ax260aLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ax260aLicenseTable.setStatus("mandatory")
_Ax260aLicenseEntry_Object = MibTableRow
ax260aLicenseEntry = _Ax260aLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 2, 1)
)
ax260aLicenseEntry.setIndexNames(
    (0, "AX260A", "ax260aLicenseIndex"),
)
if mibBuilder.loadTexts:
    ax260aLicenseEntry.setStatus("mandatory")
_Ax260aLicenseIndex_Type = Integer32
_Ax260aLicenseIndex_Object = MibTableColumn
ax260aLicenseIndex = _Ax260aLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 2, 1, 1),
    _Ax260aLicenseIndex_Type()
)
ax260aLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aLicenseIndex.setStatus("mandatory")
_Ax260aLicenseSerialNumber_Type = DisplayString
_Ax260aLicenseSerialNumber_Object = MibTableColumn
ax260aLicenseSerialNumber = _Ax260aLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 2, 1, 2),
    _Ax260aLicenseSerialNumber_Type()
)
ax260aLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aLicenseSerialNumber.setStatus("mandatory")
_Ax260aLicenseOptionNumber_Type = Integer32
_Ax260aLicenseOptionNumber_Object = MibTableColumn
ax260aLicenseOptionNumber = _Ax260aLicenseOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 2, 1, 3),
    _Ax260aLicenseOptionNumber_Type()
)
ax260aLicenseOptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aLicenseOptionNumber.setStatus("mandatory")
_Ax260aLicenseOptionTable_Object = MibTable
ax260aLicenseOptionTable = _Ax260aLicenseOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 3)
)
if mibBuilder.loadTexts:
    ax260aLicenseOptionTable.setStatus("mandatory")
_Ax260aLicenseOptionEntry_Object = MibTableRow
ax260aLicenseOptionEntry = _Ax260aLicenseOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 3, 1)
)
ax260aLicenseOptionEntry.setIndexNames(
    (0, "AX260A", "ax260aLicenseOptionIndex"),
    (0, "AX260A", "ax260aLicenseOptionNumberIndex"),
)
if mibBuilder.loadTexts:
    ax260aLicenseOptionEntry.setStatus("mandatory")
_Ax260aLicenseOptionIndex_Type = Integer32
_Ax260aLicenseOptionIndex_Object = MibTableColumn
ax260aLicenseOptionIndex = _Ax260aLicenseOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 3, 1, 1),
    _Ax260aLicenseOptionIndex_Type()
)
ax260aLicenseOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aLicenseOptionIndex.setStatus("mandatory")
_Ax260aLicenseOptionNumberIndex_Type = Integer32
_Ax260aLicenseOptionNumberIndex_Object = MibTableColumn
ax260aLicenseOptionNumberIndex = _Ax260aLicenseOptionNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 3, 1, 2),
    _Ax260aLicenseOptionNumberIndex_Type()
)
ax260aLicenseOptionNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aLicenseOptionNumberIndex.setStatus("mandatory")
_Ax260aLicenseOptionSoftwareName_Type = DisplayString
_Ax260aLicenseOptionSoftwareName_Object = MibTableColumn
ax260aLicenseOptionSoftwareName = _Ax260aLicenseOptionSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 3, 1, 3),
    _Ax260aLicenseOptionSoftwareName_Type()
)
ax260aLicenseOptionSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aLicenseOptionSoftwareName.setStatus("mandatory")
_Ax260aLicenseOptionSoftwareAbbreviation_Type = DisplayString
_Ax260aLicenseOptionSoftwareAbbreviation_Object = MibTableColumn
ax260aLicenseOptionSoftwareAbbreviation = _Ax260aLicenseOptionSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 1, 6, 3, 1, 4),
    _Ax260aLicenseOptionSoftwareAbbreviation_Type()
)
ax260aLicenseOptionSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aLicenseOptionSoftwareAbbreviation.setStatus("mandatory")
_Ax260aDevice_ObjectIdentity = ObjectIdentity
ax260aDevice = _Ax260aDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2)
)
_Ax260aChassis_ObjectIdentity = ObjectIdentity
ax260aChassis = _Ax260aChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1)
)
_Ax260aChassisMaxNumber_Type = Integer32
_Ax260aChassisMaxNumber_Object = MibScalar
ax260aChassisMaxNumber = _Ax260aChassisMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 1),
    _Ax260aChassisMaxNumber_Type()
)
ax260aChassisMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aChassisMaxNumber.setStatus("mandatory")
_Ax260aChassisTable_Object = MibTable
ax260aChassisTable = _Ax260aChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ax260aChassisTable.setStatus("mandatory")
_Ax260aChassisEntry_Object = MibTableRow
ax260aChassisEntry = _Ax260aChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1)
)
ax260aChassisEntry.setIndexNames(
    (0, "AX260A", "ax260aChassisIndex"),
)
if mibBuilder.loadTexts:
    ax260aChassisEntry.setStatus("mandatory")
_Ax260aChassisIndex_Type = Integer32
_Ax260aChassisIndex_Object = MibTableColumn
ax260aChassisIndex = _Ax260aChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 1),
    _Ax260aChassisIndex_Type()
)
ax260aChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aChassisIndex.setStatus("mandatory")


class _Ax260aChassisType_Type(Integer32):
    """Custom type ax260aChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2000,
              2001)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("model-AX260A-08T", 2000),
          ("model-AX260A-08TF", 2001))
    )


_Ax260aChassisType_Type.__name__ = "Integer32"
_Ax260aChassisType_Object = MibTableColumn
ax260aChassisType = _Ax260aChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 2),
    _Ax260aChassisType_Type()
)
ax260aChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aChassisType.setStatus("mandatory")


class _Ax260aChassisStatus_Type(Integer32):
    """Custom type ax260aChassisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("up", 2)
    )


_Ax260aChassisStatus_Type.__name__ = "Integer32"
_Ax260aChassisStatus_Object = MibTableColumn
ax260aChassisStatus = _Ax260aChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 3),
    _Ax260aChassisStatus_Type()
)
ax260aChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aChassisStatus.setStatus("mandatory")


class _Ax260aStsLedStatus_Type(Integer32):
    """Custom type ax260aStsLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("green-light-blink", 1),
          ("green-light-on", 2),
          ("red-light-blink", 3),
          ("red-light-on", 4),
          ("light-off", 6),
          ("orange-light-on", 8))
    )


_Ax260aStsLedStatus_Type.__name__ = "Integer32"
_Ax260aStsLedStatus_Object = MibTableColumn
ax260aStsLedStatus = _Ax260aStsLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 4),
    _Ax260aStsLedStatus_Type()
)
ax260aStsLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aStsLedStatus.setStatus("mandatory")
_Ax260aCpuName_Type = DisplayString
_Ax260aCpuName_Object = MibTableColumn
ax260aCpuName = _Ax260aCpuName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 5),
    _Ax260aCpuName_Type()
)
ax260aCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aCpuName.setStatus("mandatory")
_Ax260aCpuClock_Type = Integer32
_Ax260aCpuClock_Object = MibTableColumn
ax260aCpuClock = _Ax260aCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 6),
    _Ax260aCpuClock_Type()
)
ax260aCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aCpuClock.setStatus("mandatory")
_Ax260aMemoryTotalSize_Type = Integer32
_Ax260aMemoryTotalSize_Object = MibTableColumn
ax260aMemoryTotalSize = _Ax260aMemoryTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 7),
    _Ax260aMemoryTotalSize_Type()
)
ax260aMemoryTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aMemoryTotalSize.setStatus("mandatory")
_Ax260aMemoryUsedSize_Type = Integer32
_Ax260aMemoryUsedSize_Object = MibTableColumn
ax260aMemoryUsedSize = _Ax260aMemoryUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 8),
    _Ax260aMemoryUsedSize_Type()
)
ax260aMemoryUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aMemoryUsedSize.setStatus("mandatory")
_Ax260aMemoryFreeSize_Type = Integer32
_Ax260aMemoryFreeSize_Object = MibTableColumn
ax260aMemoryFreeSize = _Ax260aMemoryFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 9),
    _Ax260aMemoryFreeSize_Type()
)
ax260aMemoryFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aMemoryFreeSize.setStatus("mandatory")
_Ax260aRomVersion_Type = DisplayString
_Ax260aRomVersion_Object = MibTableColumn
ax260aRomVersion = _Ax260aRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 10),
    _Ax260aRomVersion_Type()
)
ax260aRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aRomVersion.setStatus("mandatory")
_Ax260aCpuLoad1m_Type = Integer32
_Ax260aCpuLoad1m_Object = MibTableColumn
ax260aCpuLoad1m = _Ax260aCpuLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 11),
    _Ax260aCpuLoad1m_Type()
)
ax260aCpuLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aCpuLoad1m.setStatus("mandatory")
_Ax260aFlashTotalSize_Type = Integer32
_Ax260aFlashTotalSize_Object = MibTableColumn
ax260aFlashTotalSize = _Ax260aFlashTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 12),
    _Ax260aFlashTotalSize_Type()
)
ax260aFlashTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aFlashTotalSize.setStatus("mandatory")
_Ax260aFlashUsedSize_Type = Integer32
_Ax260aFlashUsedSize_Object = MibTableColumn
ax260aFlashUsedSize = _Ax260aFlashUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 13),
    _Ax260aFlashUsedSize_Type()
)
ax260aFlashUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aFlashUsedSize.setStatus("mandatory")
_Ax260aFlashFreeSize_Type = Integer32
_Ax260aFlashFreeSize_Object = MibTableColumn
ax260aFlashFreeSize = _Ax260aFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 14),
    _Ax260aFlashFreeSize_Type()
)
ax260aFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aFlashFreeSize.setStatus("mandatory")


class _Ax260aSdCardStatus_Type(Integer32):
    """Custom type ax260aSdCardStatus based on Integer32"""
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


_Ax260aSdCardStatus_Type.__name__ = "Integer32"
_Ax260aSdCardStatus_Object = MibTableColumn
ax260aSdCardStatus = _Ax260aSdCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 15),
    _Ax260aSdCardStatus_Type()
)
ax260aSdCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSdCardStatus.setStatus("mandatory")
_Ax260aSdCardTotalSize_Type = Integer32
_Ax260aSdCardTotalSize_Object = MibTableColumn
ax260aSdCardTotalSize = _Ax260aSdCardTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 16),
    _Ax260aSdCardTotalSize_Type()
)
ax260aSdCardTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSdCardTotalSize.setStatus("mandatory")
_Ax260aSdCardUsedSize_Type = Integer32
_Ax260aSdCardUsedSize_Object = MibTableColumn
ax260aSdCardUsedSize = _Ax260aSdCardUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 17),
    _Ax260aSdCardUsedSize_Type()
)
ax260aSdCardUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSdCardUsedSize.setStatus("mandatory")
_Ax260aSdCardFreeSize_Type = Integer32
_Ax260aSdCardFreeSize_Object = MibTableColumn
ax260aSdCardFreeSize = _Ax260aSdCardFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 18),
    _Ax260aSdCardFreeSize_Type()
)
ax260aSdCardFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSdCardFreeSize.setStatus("mandatory")
_Ax260aPhysLineNumber_Type = Integer32
_Ax260aPhysLineNumber_Object = MibTableColumn
ax260aPhysLineNumber = _Ax260aPhysLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 19),
    _Ax260aPhysLineNumber_Type()
)
ax260aPhysLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aPhysLineNumber.setStatus("mandatory")
_Ax260aTemperatureStatusNumber_Type = Integer32
_Ax260aTemperatureStatusNumber_Object = MibTableColumn
ax260aTemperatureStatusNumber = _Ax260aTemperatureStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 20),
    _Ax260aTemperatureStatusNumber_Type()
)
ax260aTemperatureStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aTemperatureStatusNumber.setStatus("mandatory")
_Ax260aPowerUnitNumber_Type = Integer32
_Ax260aPowerUnitNumber_Object = MibTableColumn
ax260aPowerUnitNumber = _Ax260aPowerUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 21),
    _Ax260aPowerUnitNumber_Type()
)
ax260aPowerUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aPowerUnitNumber.setStatus("mandatory")
_Ax260aRedundantPsNumber_Type = Integer32
_Ax260aRedundantPsNumber_Object = MibTableColumn
ax260aRedundantPsNumber = _Ax260aRedundantPsNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 22),
    _Ax260aRedundantPsNumber_Type()
)
ax260aRedundantPsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aRedundantPsNumber.setStatus("mandatory")
_Ax260aFanNumber_Type = Integer32
_Ax260aFanNumber_Object = MibTableColumn
ax260aFanNumber = _Ax260aFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 23),
    _Ax260aFanNumber_Type()
)
ax260aFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aFanNumber.setStatus("mandatory")
_Ax260aTotalAccumRunTime_Type = Integer32
_Ax260aTotalAccumRunTime_Object = MibTableColumn
ax260aTotalAccumRunTime = _Ax260aTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 24),
    _Ax260aTotalAccumRunTime_Type()
)
ax260aTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aTotalAccumRunTime.setStatus("mandatory")
_Ax260aCriticalAccumRunTime_Type = Integer32
_Ax260aCriticalAccumRunTime_Object = MibTableColumn
ax260aCriticalAccumRunTime = _Ax260aCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 25),
    _Ax260aCriticalAccumRunTime_Type()
)
ax260aCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aCriticalAccumRunTime.setStatus("mandatory")


class _Ax260aSts2LedStatus_Type(Integer32):
    """Custom type ax260aSts2LedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("green-light-blink", 1),
          ("green-light-on", 2),
          ("light-off", 6),
          ("orange-light-on", 8))
    )


_Ax260aSts2LedStatus_Type.__name__ = "Integer32"
_Ax260aSts2LedStatus_Object = MibTableColumn
ax260aSts2LedStatus = _Ax260aSts2LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 2, 1, 26),
    _Ax260aSts2LedStatus_Type()
)
ax260aSts2LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aSts2LedStatus.setStatus("mandatory")
_Ax260aTemperatureStatusTable_Object = MibTable
ax260aTemperatureStatusTable = _Ax260aTemperatureStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ax260aTemperatureStatusTable.setStatus("mandatory")
_Ax260aTemperatureStatusEntry_Object = MibTableRow
ax260aTemperatureStatusEntry = _Ax260aTemperatureStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 3, 1)
)
ax260aTemperatureStatusEntry.setIndexNames(
    (0, "AX260A", "ax260aChassisIndex"),
    (0, "AX260A", "ax260aTemperatureStatusIndex"),
)
if mibBuilder.loadTexts:
    ax260aTemperatureStatusEntry.setStatus("mandatory")
_Ax260aTemperatureStatusIndex_Type = Integer32
_Ax260aTemperatureStatusIndex_Object = MibTableColumn
ax260aTemperatureStatusIndex = _Ax260aTemperatureStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 3, 1, 1),
    _Ax260aTemperatureStatusIndex_Type()
)
ax260aTemperatureStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aTemperatureStatusIndex.setStatus("mandatory")


class _Ax260aTemperatureStatusDescr_Type(DisplayString):
    """Custom type ax260aTemperatureStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ax260aTemperatureStatusDescr_Type.__name__ = "DisplayString"
_Ax260aTemperatureStatusDescr_Object = MibTableColumn
ax260aTemperatureStatusDescr = _Ax260aTemperatureStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 3, 1, 2),
    _Ax260aTemperatureStatusDescr_Type()
)
ax260aTemperatureStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aTemperatureStatusDescr.setStatus("mandatory")
_Ax260aTemperatureStatusValue_Type = Integer32
_Ax260aTemperatureStatusValue_Object = MibTableColumn
ax260aTemperatureStatusValue = _Ax260aTemperatureStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 3, 1, 3),
    _Ax260aTemperatureStatusValue_Type()
)
ax260aTemperatureStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aTemperatureStatusValue.setStatus("mandatory")
_Ax260aTemperatureThreshold_Type = Integer32
_Ax260aTemperatureThreshold_Object = MibTableColumn
ax260aTemperatureThreshold = _Ax260aTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 3, 1, 4),
    _Ax260aTemperatureThreshold_Type()
)
ax260aTemperatureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aTemperatureThreshold.setStatus("mandatory")


class _Ax260aTemperatureState_Type(Integer32):
    """Custom type ax260aTemperatureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("caution", 2),
          ("fatal", 4))
    )


_Ax260aTemperatureState_Type.__name__ = "Integer32"
_Ax260aTemperatureState_Object = MibTableColumn
ax260aTemperatureState = _Ax260aTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 3, 1, 5),
    _Ax260aTemperatureState_Type()
)
ax260aTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aTemperatureState.setStatus("mandatory")
_Ax260aPowerUnitTable_Object = MibTable
ax260aPowerUnitTable = _Ax260aPowerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ax260aPowerUnitTable.setStatus("mandatory")
_Ax260aPowerUnitEntry_Object = MibTableRow
ax260aPowerUnitEntry = _Ax260aPowerUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 4, 1)
)
ax260aPowerUnitEntry.setIndexNames(
    (0, "AX260A", "ax260aChassisIndex"),
    (0, "AX260A", "ax260aPowerUnitIndex"),
)
if mibBuilder.loadTexts:
    ax260aPowerUnitEntry.setStatus("mandatory")
_Ax260aPowerUnitIndex_Type = Integer32
_Ax260aPowerUnitIndex_Object = MibTableColumn
ax260aPowerUnitIndex = _Ax260aPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 4, 1, 1),
    _Ax260aPowerUnitIndex_Type()
)
ax260aPowerUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aPowerUnitIndex.setStatus("mandatory")


class _Ax260aPowerConnectStatus_Type(Integer32):
    """Custom type ax260aPowerConnectStatus based on Integer32"""
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


_Ax260aPowerConnectStatus_Type.__name__ = "Integer32"
_Ax260aPowerConnectStatus_Object = MibTableColumn
ax260aPowerConnectStatus = _Ax260aPowerConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 4, 1, 2),
    _Ax260aPowerConnectStatus_Type()
)
ax260aPowerConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aPowerConnectStatus.setStatus("mandatory")


class _Ax260aPowerSupplyStatus_Type(Integer32):
    """Custom type ax260aPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 2),
          ("fault", 4))
    )


_Ax260aPowerSupplyStatus_Type.__name__ = "Integer32"
_Ax260aPowerSupplyStatus_Object = MibTableColumn
ax260aPowerSupplyStatus = _Ax260aPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 4, 1, 3),
    _Ax260aPowerSupplyStatus_Type()
)
ax260aPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aPowerSupplyStatus.setStatus("mandatory")
_Ax260aFanTable_Object = MibTable
ax260aFanTable = _Ax260aFanTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ax260aFanTable.setStatus("mandatory")
_Ax260aFanEntry_Object = MibTableRow
ax260aFanEntry = _Ax260aFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 5, 1)
)
ax260aFanEntry.setIndexNames(
    (0, "AX260A", "ax260aChassisIndex"),
    (0, "AX260A", "ax260aFanIndex"),
)
if mibBuilder.loadTexts:
    ax260aFanEntry.setStatus("mandatory")
_Ax260aFanIndex_Type = Integer32
_Ax260aFanIndex_Object = MibTableColumn
ax260aFanIndex = _Ax260aFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 5, 1, 1),
    _Ax260aFanIndex_Type()
)
ax260aFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aFanIndex.setStatus("mandatory")


class _Ax260aFanStatus_Type(Integer32):
    """Custom type ax260aFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 2),
          ("fault", 4),
          ("stopping", 5))
    )


_Ax260aFanStatus_Type.__name__ = "Integer32"
_Ax260aFanStatus_Object = MibTableColumn
ax260aFanStatus = _Ax260aFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 5, 1, 2),
    _Ax260aFanStatus_Type()
)
ax260aFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aFanStatus.setStatus("mandatory")
_Ax260aRedundantPsTable_Object = MibTable
ax260aRedundantPsTable = _Ax260aRedundantPsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ax260aRedundantPsTable.setStatus("mandatory")
_Ax260aRedundantPsEntry_Object = MibTableRow
ax260aRedundantPsEntry = _Ax260aRedundantPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 6, 1)
)
ax260aRedundantPsEntry.setIndexNames(
    (0, "AX260A", "ax260aChassisIndex"),
    (0, "AX260A", "ax260aRedundantPsIndex"),
)
if mibBuilder.loadTexts:
    ax260aRedundantPsEntry.setStatus("mandatory")
_Ax260aRedundantPsIndex_Type = Integer32
_Ax260aRedundantPsIndex_Object = MibTableColumn
ax260aRedundantPsIndex = _Ax260aRedundantPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 6, 1, 1),
    _Ax260aRedundantPsIndex_Type()
)
ax260aRedundantPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aRedundantPsIndex.setStatus("mandatory")


class _Ax260aRedundantPsConnectStatus_Type(Integer32):
    """Custom type ax260aRedundantPsConnectStatus based on Integer32"""
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


_Ax260aRedundantPsConnectStatus_Type.__name__ = "Integer32"
_Ax260aRedundantPsConnectStatus_Object = MibTableColumn
ax260aRedundantPsConnectStatus = _Ax260aRedundantPsConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 6, 1, 2),
    _Ax260aRedundantPsConnectStatus_Type()
)
ax260aRedundantPsConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aRedundantPsConnectStatus.setStatus("mandatory")


class _Ax260aRedundantPsStatus_Type(Integer32):
    """Custom type ax260aRedundantPsStatus based on Integer32"""
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


_Ax260aRedundantPsStatus_Type.__name__ = "Integer32"
_Ax260aRedundantPsStatus_Object = MibTableColumn
ax260aRedundantPsStatus = _Ax260aRedundantPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 1, 6, 1, 3),
    _Ax260aRedundantPsStatus_Type()
)
ax260aRedundantPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aRedundantPsStatus.setStatus("mandatory")
_Ax260aPhysLine_ObjectIdentity = ObjectIdentity
ax260aPhysLine = _Ax260aPhysLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 2)
)
_Ax260aPhysLineTable_Object = MibTable
ax260aPhysLineTable = _Ax260aPhysLineTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ax260aPhysLineTable.setStatus("mandatory")
_Ax260aPhysLineEntry_Object = MibTableRow
ax260aPhysLineEntry = _Ax260aPhysLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 2, 1, 1)
)
ax260aPhysLineEntry.setIndexNames(
    (0, "AX260A", "ax260aChassisIndex"),
    (0, "AX260A", "ax260aPhysLineIndex"),
)
if mibBuilder.loadTexts:
    ax260aPhysLineEntry.setStatus("mandatory")
_Ax260aPhysLineIndex_Type = Integer32
_Ax260aPhysLineIndex_Object = MibTableColumn
ax260aPhysLineIndex = _Ax260aPhysLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 2, 1, 1, 1),
    _Ax260aPhysLineIndex_Type()
)
ax260aPhysLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aPhysLineIndex.setStatus("mandatory")


class _Ax260aPhysLineConnectorType_Type(Integer32):
    """Custom type ax260aPhysLineConnectorType based on Integer32"""
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
              308,
              309,
              310,
              401,
              402,
              403,
              405,
              406,
              407,
              408)
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
          ("type1000BASE-SX2", 308),
          ("type1000BASE-UTP", 309),
          ("type1000BASE-LHB", 310),
          ("type10GBASE-SR", 401),
          ("type10GBASE-LR", 402),
          ("type10GBASE-ER", 403),
          ("type10GBASE-CU1M", 405),
          ("type10GBASE-CU3M", 406),
          ("type10GBASE-CU5M", 407),
          ("type10GBASE-CU30CM", 408))
    )


_Ax260aPhysLineConnectorType_Type.__name__ = "Integer32"
_Ax260aPhysLineConnectorType_Object = MibTableColumn
ax260aPhysLineConnectorType = _Ax260aPhysLineConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 2, 1, 1, 2),
    _Ax260aPhysLineConnectorType_Type()
)
ax260aPhysLineConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aPhysLineConnectorType.setStatus("mandatory")


class _Ax260aPhysLineOperStatus_Type(Integer32):
    """Custom type ax260aPhysLineOperStatus based on Integer32"""
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


_Ax260aPhysLineOperStatus_Type.__name__ = "Integer32"
_Ax260aPhysLineOperStatus_Object = MibTableColumn
ax260aPhysLineOperStatus = _Ax260aPhysLineOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 2, 1, 1, 3),
    _Ax260aPhysLineOperStatus_Type()
)
ax260aPhysLineOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aPhysLineOperStatus.setStatus("mandatory")
_Ax260aPhysLineIfIndexNumber_Type = Integer32
_Ax260aPhysLineIfIndexNumber_Object = MibTableColumn
ax260aPhysLineIfIndexNumber = _Ax260aPhysLineIfIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 2, 1, 1, 4),
    _Ax260aPhysLineIfIndexNumber_Type()
)
ax260aPhysLineIfIndexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aPhysLineIfIndexNumber.setStatus("mandatory")


class _Ax260aPhysLineTransceiverStatus_Type(Integer32):
    """Custom type ax260aPhysLineTransceiverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("unchangeable-transceiver", 1),
          ("sfp-mounted", 20),
          ("sfp-unmounted", 21),
          ("unsupported-sfp-mounted", 22),
          ("sfp-status-unknown", 23))
    )


_Ax260aPhysLineTransceiverStatus_Type.__name__ = "Integer32"
_Ax260aPhysLineTransceiverStatus_Object = MibTableColumn
ax260aPhysLineTransceiverStatus = _Ax260aPhysLineTransceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 2, 1, 1, 5),
    _Ax260aPhysLineTransceiverStatus_Type()
)
ax260aPhysLineTransceiverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aPhysLineTransceiverStatus.setStatus("mandatory")
_Ax260aDeviceError_ObjectIdentity = ObjectIdentity
ax260aDeviceError = _Ax260aDeviceError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 3)
)


class _Ax260aMemoryError_Type(Integer32):
    """Custom type ax260aMemoryError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("parity-error", 1))
    )


_Ax260aMemoryError_Type.__name__ = "Integer32"
_Ax260aMemoryError_Object = MibScalar
ax260aMemoryError = _Ax260aMemoryError_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 2, 3, 1),
    _Ax260aMemoryError_Type()
)
ax260aMemoryError.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aMemoryError.setStatus("mandatory")
_Ax260aManagementMIB_ObjectIdentity = ObjectIdentity
ax260aManagementMIB = _Ax260aManagementMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 3)
)
_Ax260aOperationCommand_ObjectIdentity = ObjectIdentity
ax260aOperationCommand = _Ax260aOperationCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 3, 1)
)
_Ax260aFdbClearMIB_ObjectIdentity = ObjectIdentity
ax260aFdbClearMIB = _Ax260aFdbClearMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 3, 1, 1)
)


class _Ax260aFdbClearSet_Type(Integer32):
    """Custom type ax260aFdbClearSet based on Integer32"""
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


_Ax260aFdbClearSet_Type.__name__ = "Integer32"
_Ax260aFdbClearSet_Object = MibScalar
ax260aFdbClearSet = _Ax260aFdbClearSet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 3, 1, 1, 1),
    _Ax260aFdbClearSet_Type()
)
ax260aFdbClearSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ax260aFdbClearSet.setStatus("mandatory")
_Ax260aFdbClearReqTime_Type = TimeTicks
_Ax260aFdbClearReqTime_Object = MibScalar
ax260aFdbClearReqTime = _Ax260aFdbClearReqTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 3, 1, 1, 2),
    _Ax260aFdbClearReqTime_Type()
)
ax260aFdbClearReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aFdbClearReqTime.setStatus("mandatory")
_Ax260aFdbClearSuccessTime_Type = TimeTicks
_Ax260aFdbClearSuccessTime_Object = MibScalar
ax260aFdbClearSuccessTime = _Ax260aFdbClearSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 3, 1, 1, 3),
    _Ax260aFdbClearSuccessTime_Type()
)
ax260aFdbClearSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ax260aFdbClearSuccessTime.setStatus("mandatory")
_Ax260aAuth_ObjectIdentity = ObjectIdentity
ax260aAuth = _Ax260aAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 10)
)
_Ax260aAuthInfo_ObjectIdentity = ObjectIdentity
ax260aAuthInfo = _Ax260aAuthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 10, 1)
)


class _Ax260aAuthSysName_Type(DisplayString):
    """Custom type ax260aAuthSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_Ax260aAuthSysName_Type.__name__ = "DisplayString"
_Ax260aAuthSysName_Object = MibScalar
ax260aAuthSysName = _Ax260aAuthSysName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 10, 1, 1),
    _Ax260aAuthSysName_Type()
)
ax260aAuthSysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aAuthSysName.setStatus("mandatory")
_Ax260aAuthIfIndex_Type = Integer32
_Ax260aAuthIfIndex_Object = MibScalar
ax260aAuthIfIndex = _Ax260aAuthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 10, 1, 2),
    _Ax260aAuthIfIndex_Type()
)
ax260aAuthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aAuthIfIndex.setStatus("mandatory")
_Ax260aAuthSupplicantMac_Type = MacAddress
_Ax260aAuthSupplicantMac_Object = MibScalar
ax260aAuthSupplicantMac = _Ax260aAuthSupplicantMac_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 10, 1, 3),
    _Ax260aAuthSupplicantMac_Type()
)
ax260aAuthSupplicantMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aAuthSupplicantMac.setStatus("mandatory")


class _Ax260aAuthMessage_Type(DisplayString):
    """Custom type ax260aAuthMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 280),
    )


_Ax260aAuthMessage_Type.__name__ = "DisplayString"
_Ax260aAuthMessage_Object = MibScalar
ax260aAuthMessage = _Ax260aAuthMessage_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 10, 1, 4),
    _Ax260aAuthMessage_Type()
)
ax260aAuthMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ax260aAuthMessage.setStatus("mandatory")
_Ax260aDot1x_ObjectIdentity = ObjectIdentity
ax260aDot1x = _Ax260aDot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 10, 2)
)
_Ax260aWauth_ObjectIdentity = ObjectIdentity
ax260aWauth = _Ax260aWauth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 10, 3)
)
_Ax260aMauth_ObjectIdentity = ObjectIdentity
ax260aMauth = _Ax260aMauth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 23, 10, 4)
)

# Managed Objects groups


# Notification objects

ax260aSystemMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 1)
)
ax260aSystemMsgTrap.setObjects(
      *(("AX260A", "ax260aSystemMsgType"),
        ("AX260A", "ax260aSystemMsgTimeStamp"),
        ("AX260A", "ax260aSystemMsgLevel"),
        ("AX260A", "ax260aSystemMsgEventPoint"),
        ("AX260A", "ax260aSystemMsgEventInterfaceID"),
        ("AX260A", "ax260aSystemMsgEventCode"),
        ("AX260A", "ax260aSystemMsgAdditionalCode"),
        ("AX260A", "ax260aSystemMsgText"))
)
if mibBuilder.loadTexts:
    ax260aSystemMsgTrap.setStatus(
        ""
    )

ax260aTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 4)
)
ax260aTemperatureTrap.setObjects(
      *(("AX260A", "ax260aChassisIndex"),
        ("AX260A", "ax260aTemperatureStatusIndex"),
        ("AX260A", "ax260aTemperatureStatusDescr"),
        ("AX260A", "ax260aTemperatureStatusValue"),
        ("AX260A", "ax260aTemperatureState"))
)
if mibBuilder.loadTexts:
    ax260aTemperatureTrap.setStatus(
        ""
    )

ax260aAirFanStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 8)
)
ax260aAirFanStopTrap.setObjects(
    ("AX260A", "ax260aFanStatus")
)
if mibBuilder.loadTexts:
    ax260aAirFanStopTrap.setStatus(
        ""
    )

ax260aPowerSupplyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 9)
)
ax260aPowerSupplyFailureTrap.setObjects(
    ("AX260A", "ax260aPowerSupplyStatus")
)
if mibBuilder.loadTexts:
    ax260aPowerSupplyFailureTrap.setStatus(
        ""
    )

ax260aLoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 10)
)
ax260aLoginSuccessTrap.setObjects(
      *(("AX260A", "axsLoginName"),
        ("AX260A", "axsLoginTime"),
        ("AX260A", "axsLoginLocation"),
        ("AX260A", "axsLoginLine"))
)
if mibBuilder.loadTexts:
    ax260aLoginSuccessTrap.setStatus(
        ""
    )

ax260aLoginFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 11)
)
ax260aLoginFailureTrap.setObjects(
      *(("AX260A", "axsLoginName"),
        ("AX260A", "axsLoginFailureTime"),
        ("AX260A", "axsLoginLocation"),
        ("AX260A", "axsLoginLine"))
)
if mibBuilder.loadTexts:
    ax260aLoginFailureTrap.setStatus(
        ""
    )

ax260aLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 12)
)
ax260aLogoutTrap.setObjects(
      *(("AX260A", "axsLoginName"),
        ("AX260A", "axsLoginTime"),
        ("AX260A", "axsLogoutTime"),
        ("AX260A", "axsLoginLocation"),
        ("AX260A", "axsLoginLine"),
        ("AX260A", "axsLogoutStatus"))
)
if mibBuilder.loadTexts:
    ax260aLogoutTrap.setStatus(
        ""
    )

ax260aMemoryUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 13)
)
if mibBuilder.loadTexts:
    ax260aMemoryUsageTrap.setStatus(
        ""
    )

ax260aFrameErrorReceiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 18)
)
ax260aFrameErrorReceiveTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aFrameErrorReceiveTrap.setStatus(
        ""
    )

ax260aFrameErrorSendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 19)
)
ax260aFrameErrorSendTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aFrameErrorSendTrap.setStatus(
        ""
    )

ax260aBroadcastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 20)
)
ax260aBroadcastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aBroadcastStormDetectTrap.setStatus(
        ""
    )

ax260aMulticastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 21)
)
ax260aMulticastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aMulticastStormDetectTrap.setStatus(
        ""
    )

ax260aUnicastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 22)
)
ax260aUnicastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aUnicastStormDetectTrap.setStatus(
        ""
    )

ax260aBroadcastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 23)
)
ax260aBroadcastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aBroadcastStormPortInactivateTrap.setStatus(
        ""
    )

ax260aMulticastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 24)
)
ax260aMulticastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aMulticastStormPortInactivateTrap.setStatus(
        ""
    )

ax260aUnicastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 25)
)
ax260aUnicastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aUnicastStormPortInactivateTrap.setStatus(
        ""
    )

ax260aBroadcastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 26)
)
ax260aBroadcastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aBroadcastStormRecoverTrap.setStatus(
        ""
    )

ax260aMulticastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 27)
)
ax260aMulticastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aMulticastStormRecoverTrap.setStatus(
        ""
    )

ax260aUnicastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 28)
)
ax260aUnicastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aUnicastStormRecoverTrap.setStatus(
        ""
    )

ax260aEfmoamUdldPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 29)
)
ax260aEfmoamUdldPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aEfmoamUdldPortInactivateTrap.setStatus(
        ""
    )

ax260aEfmoamLoopDetectPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 30)
)
ax260aEfmoamLoopDetectPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax260aEfmoamLoopDetectPortInactivateTrap.setStatus(
        ""
    )

ax260aDot1xFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 31)
)
ax260aDot1xFailureTrap.setObjects(
      *(("AX260A", "ax260aAuthSysName"),
        ("AX260A", "ax260aAuthIfIndex"),
        ("AX260A", "ax260aAuthSupplicantMac"),
        ("AX260A", "ax260aAuthMessage"))
)
if mibBuilder.loadTexts:
    ax260aDot1xFailureTrap.setStatus(
        ""
    )

ax260aDot1xEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 32)
)
ax260aDot1xEventTrap.setObjects(
      *(("AX260A", "ax260aAuthSysName"),
        ("AX260A", "ax260aAuthIfIndex"),
        ("AX260A", "ax260aAuthSupplicantMac"),
        ("AX260A", "ax260aAuthMessage"))
)
if mibBuilder.loadTexts:
    ax260aDot1xEventTrap.setStatus(
        ""
    )

ax260aWauthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 33)
)
ax260aWauthFailureTrap.setObjects(
      *(("AX260A", "ax260aAuthSysName"),
        ("AX260A", "ax260aAuthIfIndex"),
        ("AX260A", "ax260aAuthSupplicantMac"),
        ("AX260A", "ax260aAuthMessage"))
)
if mibBuilder.loadTexts:
    ax260aWauthFailureTrap.setStatus(
        ""
    )

ax260aWauthEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 34)
)
ax260aWauthEventTrap.setObjects(
      *(("AX260A", "ax260aAuthSysName"),
        ("AX260A", "ax260aAuthIfIndex"),
        ("AX260A", "ax260aAuthSupplicantMac"),
        ("AX260A", "ax260aAuthMessage"))
)
if mibBuilder.loadTexts:
    ax260aWauthEventTrap.setStatus(
        ""
    )

ax260aMauthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 35)
)
ax260aMauthFailureTrap.setObjects(
      *(("AX260A", "ax260aAuthSysName"),
        ("AX260A", "ax260aAuthIfIndex"),
        ("AX260A", "ax260aAuthSupplicantMac"),
        ("AX260A", "ax260aAuthMessage"))
)
if mibBuilder.loadTexts:
    ax260aMauthFailureTrap.setStatus(
        ""
    )

ax260aMauthEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 36)
)
ax260aMauthEventTrap.setObjects(
      *(("AX260A", "ax260aAuthSysName"),
        ("AX260A", "ax260aAuthIfIndex"),
        ("AX260A", "ax260aAuthSupplicantMac"),
        ("AX260A", "ax260aAuthMessage"))
)
if mibBuilder.loadTexts:
    ax260aMauthEventTrap.setStatus(
        ""
    )

ax260aDot1xSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 37)
)
ax260aDot1xSystemTrap.setObjects(
      *(("AX260A", "ax260aAuthSysName"),
        ("AX260A", "ax260aAuthIfIndex"),
        ("AX260A", "ax260aAuthSupplicantMac"),
        ("AX260A", "ax260aAuthMessage"))
)
if mibBuilder.loadTexts:
    ax260aDot1xSystemTrap.setStatus(
        ""
    )

ax260aWauthSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 38)
)
ax260aWauthSystemTrap.setObjects(
      *(("AX260A", "ax260aAuthSysName"),
        ("AX260A", "ax260aAuthIfIndex"),
        ("AX260A", "ax260aAuthSupplicantMac"),
        ("AX260A", "ax260aAuthMessage"))
)
if mibBuilder.loadTexts:
    ax260aWauthSystemTrap.setStatus(
        ""
    )

ax260aMauthSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 39)
)
ax260aMauthSystemTrap.setObjects(
      *(("AX260A", "ax260aAuthSysName"),
        ("AX260A", "ax260aAuthIfIndex"),
        ("AX260A", "ax260aAuthSupplicantMac"),
        ("AX260A", "ax260aAuthMessage"))
)
if mibBuilder.loadTexts:
    ax260aMauthSystemTrap.setStatus(
        ""
    )

ax260aAxrpStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 40)
)
ax260aAxrpStateTransitionTrap.setObjects(
      *(("AX260A", "axsAxrpGroupRingId"),
        ("AX260A", "axsAxrpGroupMode"),
        ("AX260A", "axsAxrpGroupRingAttribute"),
        ("AX260A", "axsAxrpGroupMonitoringState"))
)
if mibBuilder.loadTexts:
    ax260aAxrpStateTransitionTrap.setStatus(
        ""
    )

ax260aAxrpMultiFaultDetectionStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 41)
)
ax260aAxrpMultiFaultDetectionStartTrap.setObjects(
      *(("AX260A", "axsAxrpGroupRingId"),
        ("AX260A", "axsAxrpGroupMode"),
        ("AX260A", "axsAxrpGroupRingAttribute"))
)
if mibBuilder.loadTexts:
    ax260aAxrpMultiFaultDetectionStartTrap.setStatus(
        ""
    )

ax260aAxrpMultiFaultDetectionStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 42)
)
ax260aAxrpMultiFaultDetectionStateTransitionTrap.setObjects(
      *(("AX260A", "axsAxrpGroupRingId"),
        ("AX260A", "axsAxrpGroupMode"),
        ("AX260A", "axsAxrpGroupRingAttribute"),
        ("AX260A", "axsAxrpGroupMultiFaultDetectionState"))
)
if mibBuilder.loadTexts:
    ax260aAxrpMultiFaultDetectionStateTransitionTrap.setStatus(
        ""
    )

ax260aL2ldLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 51)
)
ax260aL2ldLinkDown.setObjects(
      *(("AX260A", "axsL2ldPortIfIndex"),
        ("AX260A", "axsL2ldPortSourcePortIfindex"),
        ("AX260A", "axsL2ldPortDestinationPortIfindex"),
        ("AX260A", "axsL2ldPortSourceVlan"))
)
if mibBuilder.loadTexts:
    ax260aL2ldLinkDown.setStatus(
        ""
    )

ax260aL2ldLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 52)
)
ax260aL2ldLinkUp.setObjects(
    ("AX260A", "axsL2ldPortIfIndex")
)
if mibBuilder.loadTexts:
    ax260aL2ldLinkUp.setStatus(
        ""
    )

ax260aL2ldLoopDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 53)
)
ax260aL2ldLoopDetection.setObjects(
      *(("AX260A", "axsL2ldPortIndex"),
        ("AX260A", "axsL2ldPortIfIndex"),
        ("AX260A", "axsL2ldPortSourcePortIfindex"),
        ("AX260A", "axsL2ldPortSourceVlan"))
)
if mibBuilder.loadTexts:
    ax260aL2ldLoopDetection.setStatus(
        ""
    )

ax260aUlrChangeSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 87)
)
ax260aUlrChangeSecondary.setObjects(
      *(("AX260A", "axsUlrPortIfIndex"),
        ("AX260A", "axsUlrPairedPortIfIndex"))
)
if mibBuilder.loadTexts:
    ax260aUlrChangeSecondary.setStatus(
        ""
    )

ax260aUlrChangePrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 88)
)
ax260aUlrChangePrimary.setObjects(
      *(("AX260A", "axsUlrPortIfIndex"),
        ("AX260A", "axsUlrPairedPortIfIndex"))
)
if mibBuilder.loadTexts:
    ax260aUlrChangePrimary.setStatus(
        ""
    )

ax260aDeviceErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 23, 0, 90)
)
ax260aDeviceErrorTrap.setObjects(
    ("AX260A", "ax260aMemoryError")
)
if mibBuilder.loadTexts:
    ax260aDeviceErrorTrap.setStatus(
        ""
    )

axsOadpNeighborCachelastChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 7, 2, 0, 1)
)
axsOadpNeighborCachelastChangeTrap.setObjects(
    ("AX260A", "axsOadpNeighborCacheLastChange")
)
if mibBuilder.loadTexts:
    axsOadpNeighborCachelastChangeTrap.setStatus(
        ""
    )

axsOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 1)
)
axsOspfVirtIfStateChange.setObjects(
      *(("AX260A", "axsOspfVirtIfDomainNumber"),
        ("AX260A", "axsOspfRouterId"),
        ("AX260A", "axsOspfVirtIfAreaId"),
        ("AX260A", "axsOspfVirtIfNeighbor"),
        ("AX260A", "axsOspfVirtIfState"))
)
if mibBuilder.loadTexts:
    axsOspfVirtIfStateChange.setStatus(
        ""
    )

axsOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 2)
)
axsOspfNbrStateChange.setObjects(
      *(("AX260A", "axsOspfNbrDomainNumber"),
        ("AX260A", "axsOspfRouterId"),
        ("AX260A", "axsOspfNbrIpAddr"),
        ("AX260A", "axsOspfNbrAddressLessIndex"),
        ("AX260A", "axsOspfNbrRtrId"),
        ("AX260A", "axsOspfNbrState"))
)
if mibBuilder.loadTexts:
    axsOspfNbrStateChange.setStatus(
        ""
    )

axsOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 3)
)
axsOspfVirtNbrStateChange.setObjects(
      *(("AX260A", "axsOspfVirtNbrDomainNumber"),
        ("AX260A", "axsOspfRouterId"),
        ("AX260A", "axsOspfVirtNbrArea"),
        ("AX260A", "axsOspfVirtNbrRtrId"),
        ("AX260A", "axsOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    axsOspfVirtNbrStateChange.setStatus(
        ""
    )

axsOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 4)
)
axsOspfIfConfigError.setObjects(
      *(("AX260A", "axsOspfIfDomainNumber"),
        ("AX260A", "axsOspfRouterId"),
        ("AX260A", "axsOspfIfIpAddress"),
        ("AX260A", "axsOspfAddressLessIf"),
        ("AX260A", "axsOspfPacketSrc"),
        ("AX260A", "axsOspfConfigErrorType"),
        ("AX260A", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfIfConfigError.setStatus(
        ""
    )

axsOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 5)
)
axsOspfVirtIfConfigError.setObjects(
      *(("AX260A", "axsOspfVirtIfDomainNumber"),
        ("AX260A", "axsOspfRouterId"),
        ("AX260A", "axsOspfVirtIfAreaId"),
        ("AX260A", "axsOspfVirtIfNeighbor"),
        ("AX260A", "axsOspfConfigErrorType"),
        ("AX260A", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfVirtIfConfigError.setStatus(
        ""
    )

axsOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 6)
)
axsOspfIfAuthFailure.setObjects(
      *(("AX260A", "axsOspfIfDomainNumber"),
        ("AX260A", "axsOspfRouterId"),
        ("AX260A", "axsOspfIfIpAddress"),
        ("AX260A", "axsOspfAddressLessIf"),
        ("AX260A", "axsOspfPacketSrc"),
        ("AX260A", "axsOspfConfigErrorType"),
        ("AX260A", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfIfAuthFailure.setStatus(
        ""
    )

axsOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 7)
)
axsOspfVirtIfAuthFailure.setObjects(
      *(("AX260A", "axsOspfVirtIfDomainNumber"),
        ("AX260A", "axsOspfRouterId"),
        ("AX260A", "axsOspfVirtIfAreaId"),
        ("AX260A", "axsOspfVirtIfNeighbor"),
        ("AX260A", "axsOspfConfigErrorType"),
        ("AX260A", "axsOspfPacketType"))
)
if mibBuilder.loadTexts:
    axsOspfVirtIfAuthFailure.setStatus(
        ""
    )

axsOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 14, 16, 2, 0, 16)
)
axsOspfIfStateChange.setObjects(
      *(("AX260A", "axsOspfIfDomainNumber"),
        ("AX260A", "axsOspfRouterId"),
        ("AX260A", "axsOspfIfIpAddress"),
        ("AX260A", "axsOspfAddressLessIf"),
        ("AX260A", "axsOspfIfState"))
)
if mibBuilder.loadTexts:
    axsOspfIfStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX260A",
    **{"VlanIndex": VlanIndex,
       "VlanIdOrZero": VlanIdOrZero,
       "alaxala": alaxala,
       "alaxalaProductId": alaxalaProductId,
       "axSwitch": axSwitch,
       "ax260a": ax260a,
       "ax260aSystemMsgTrap": ax260aSystemMsgTrap,
       "ax260aTemperatureTrap": ax260aTemperatureTrap,
       "ax260aAirFanStopTrap": ax260aAirFanStopTrap,
       "ax260aPowerSupplyFailureTrap": ax260aPowerSupplyFailureTrap,
       "ax260aLoginSuccessTrap": ax260aLoginSuccessTrap,
       "ax260aLoginFailureTrap": ax260aLoginFailureTrap,
       "ax260aLogoutTrap": ax260aLogoutTrap,
       "ax260aMemoryUsageTrap": ax260aMemoryUsageTrap,
       "ax260aFrameErrorReceiveTrap": ax260aFrameErrorReceiveTrap,
       "ax260aFrameErrorSendTrap": ax260aFrameErrorSendTrap,
       "ax260aBroadcastStormDetectTrap": ax260aBroadcastStormDetectTrap,
       "ax260aMulticastStormDetectTrap": ax260aMulticastStormDetectTrap,
       "ax260aUnicastStormDetectTrap": ax260aUnicastStormDetectTrap,
       "ax260aBroadcastStormPortInactivateTrap": ax260aBroadcastStormPortInactivateTrap,
       "ax260aMulticastStormPortInactivateTrap": ax260aMulticastStormPortInactivateTrap,
       "ax260aUnicastStormPortInactivateTrap": ax260aUnicastStormPortInactivateTrap,
       "ax260aBroadcastStormRecoverTrap": ax260aBroadcastStormRecoverTrap,
       "ax260aMulticastStormRecoverTrap": ax260aMulticastStormRecoverTrap,
       "ax260aUnicastStormRecoverTrap": ax260aUnicastStormRecoverTrap,
       "ax260aEfmoamUdldPortInactivateTrap": ax260aEfmoamUdldPortInactivateTrap,
       "ax260aEfmoamLoopDetectPortInactivateTrap": ax260aEfmoamLoopDetectPortInactivateTrap,
       "ax260aDot1xFailureTrap": ax260aDot1xFailureTrap,
       "ax260aDot1xEventTrap": ax260aDot1xEventTrap,
       "ax260aWauthFailureTrap": ax260aWauthFailureTrap,
       "ax260aWauthEventTrap": ax260aWauthEventTrap,
       "ax260aMauthFailureTrap": ax260aMauthFailureTrap,
       "ax260aMauthEventTrap": ax260aMauthEventTrap,
       "ax260aDot1xSystemTrap": ax260aDot1xSystemTrap,
       "ax260aWauthSystemTrap": ax260aWauthSystemTrap,
       "ax260aMauthSystemTrap": ax260aMauthSystemTrap,
       "ax260aAxrpStateTransitionTrap": ax260aAxrpStateTransitionTrap,
       "ax260aAxrpMultiFaultDetectionStartTrap": ax260aAxrpMultiFaultDetectionStartTrap,
       "ax260aAxrpMultiFaultDetectionStateTransitionTrap": ax260aAxrpMultiFaultDetectionStateTransitionTrap,
       "ax260aL2ldLinkDown": ax260aL2ldLinkDown,
       "ax260aL2ldLinkUp": ax260aL2ldLinkUp,
       "ax260aL2ldLoopDetection": ax260aL2ldLoopDetection,
       "ax260aUlrChangeSecondary": ax260aUlrChangeSecondary,
       "ax260aUlrChangePrimary": ax260aUlrChangePrimary,
       "ax260aDeviceErrorTrap": ax260aDeviceErrorTrap,
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
       "axsAccessFilterStatsOutTable": axsAccessFilterStatsOutTable,
       "axsAccessFilterStatsOutEntry": axsAccessFilterStatsOutEntry,
       "axsAccessFilterStatsOutifIndex": axsAccessFilterStatsOutifIndex,
       "axsAccessFilterStatsOutifIndexType": axsAccessFilterStatsOutifIndexType,
       "axsAccessFilterStatsOutListIndex": axsAccessFilterStatsOutListIndex,
       "axsAccessFilterStatsOutSequenceNumber": axsAccessFilterStatsOutSequenceNumber,
       "axsAccessFilterStatsOutListName": axsAccessFilterStatsOutListName,
       "axsAccessFilterStatsOutMatchedPackets": axsAccessFilterStatsOutMatchedPackets,
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
       "axsUlr": axsUlr,
       "axsUlrGlobalInfo": axsUlrGlobalInfo,
       "axsUlrVersion": axsUlrVersion,
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
       "axsStack": axsStack,
       "axsStackGlobalInfo": axsStackGlobalInfo,
       "axsStackMasterSwitch": axsStackMasterSwitch,
       "axsStackMember": axsStackMember,
       "axsStackMemberTable": axsStackMemberTable,
       "axsStackMemberEntry": axsStackMemberEntry,
       "axsStackMemberIndex": axsStackMemberIndex,
       "axsStackModelType": axsStackModelType,
       "axsStackSoftwareName": axsStackSoftwareName,
       "axsStackSoftwareAbbreviation": axsStackSoftwareAbbreviation,
       "axsStackSoftwareVersion": axsStackSoftwareVersion,
       "axsStackBootReason": axsStackBootReason,
       "axsStackPconModuleMode": axsStackPconModuleMode,
       "axsStackPconPowerConMaxPower": axsStackPconPowerConMaxPower,
       "axsStackPconPowerConPowerConsumption": axsStackPconPowerConPowerConsumption,
       "axsStackPconPowerConPowerMeter": axsStackPconPowerConPowerMeter,
       "axsStackMemberLicense": axsStackMemberLicense,
       "axsStackMemberLicenseTable": axsStackMemberLicenseTable,
       "axsStackMemberLicenseEntry": axsStackMemberLicenseEntry,
       "axsStackMemberLicenseIndex": axsStackMemberLicenseIndex,
       "axsStackMemberLicenseSerialNumber": axsStackMemberLicenseSerialNumber,
       "axsStackMemberLicenseOptionNumber": axsStackMemberLicenseOptionNumber,
       "axsStackMemberLicenseOptionTable": axsStackMemberLicenseOptionTable,
       "axsStackMemberLicenseOptionEntry": axsStackMemberLicenseOptionEntry,
       "axsStackMemberLicenseOptionIndex": axsStackMemberLicenseOptionIndex,
       "axsStackMemberLicenseOptionNumberIndex": axsStackMemberLicenseOptionNumberIndex,
       "axsStackMemberLicenseOptionSoftwareName": axsStackMemberLicenseOptionSoftwareName,
       "axsStackMemberLicenseOptionSoftwareAbbreviation": axsStackMemberLicenseOptionSoftwareAbbreviation,
       "ax260aMib": ax260aMib,
       "ax260aSwitch": ax260aSwitch,
       "ax260aModelType": ax260aModelType,
       "ax260aSoftware": ax260aSoftware,
       "ax260aSoftwareName": ax260aSoftwareName,
       "ax260aSoftwareAbbreviation": ax260aSoftwareAbbreviation,
       "ax260aSoftwareVersion": ax260aSoftwareVersion,
       "ax260aSystemMsg": ax260aSystemMsg,
       "ax260aSystemMsgText": ax260aSystemMsgText,
       "ax260aSystemMsgType": ax260aSystemMsgType,
       "ax260aSystemMsgTimeStamp": ax260aSystemMsgTimeStamp,
       "ax260aSystemMsgLevel": ax260aSystemMsgLevel,
       "ax260aSystemMsgEventPoint": ax260aSystemMsgEventPoint,
       "ax260aSystemMsgEventInterfaceID": ax260aSystemMsgEventInterfaceID,
       "ax260aSystemMsgEventCode": ax260aSystemMsgEventCode,
       "ax260aSystemMsgAdditionalCode": ax260aSystemMsgAdditionalCode,
       "ax260aSnmpAgent": ax260aSnmpAgent,
       "ax260aSnmpSendReceiveSize": ax260aSnmpSendReceiveSize,
       "ax260aSnmpReceiveDelay": ax260aSnmpReceiveDelay,
       "ax260aSnmpContinuousSend": ax260aSnmpContinuousSend,
       "ax260aSnmpObjectMaxNumber": ax260aSnmpObjectMaxNumber,
       "ax260aLicense": ax260aLicense,
       "ax260aLicenseNumber": ax260aLicenseNumber,
       "ax260aLicenseTable": ax260aLicenseTable,
       "ax260aLicenseEntry": ax260aLicenseEntry,
       "ax260aLicenseIndex": ax260aLicenseIndex,
       "ax260aLicenseSerialNumber": ax260aLicenseSerialNumber,
       "ax260aLicenseOptionNumber": ax260aLicenseOptionNumber,
       "ax260aLicenseOptionTable": ax260aLicenseOptionTable,
       "ax260aLicenseOptionEntry": ax260aLicenseOptionEntry,
       "ax260aLicenseOptionIndex": ax260aLicenseOptionIndex,
       "ax260aLicenseOptionNumberIndex": ax260aLicenseOptionNumberIndex,
       "ax260aLicenseOptionSoftwareName": ax260aLicenseOptionSoftwareName,
       "ax260aLicenseOptionSoftwareAbbreviation": ax260aLicenseOptionSoftwareAbbreviation,
       "ax260aDevice": ax260aDevice,
       "ax260aChassis": ax260aChassis,
       "ax260aChassisMaxNumber": ax260aChassisMaxNumber,
       "ax260aChassisTable": ax260aChassisTable,
       "ax260aChassisEntry": ax260aChassisEntry,
       "ax260aChassisIndex": ax260aChassisIndex,
       "ax260aChassisType": ax260aChassisType,
       "ax260aChassisStatus": ax260aChassisStatus,
       "ax260aStsLedStatus": ax260aStsLedStatus,
       "ax260aCpuName": ax260aCpuName,
       "ax260aCpuClock": ax260aCpuClock,
       "ax260aMemoryTotalSize": ax260aMemoryTotalSize,
       "ax260aMemoryUsedSize": ax260aMemoryUsedSize,
       "ax260aMemoryFreeSize": ax260aMemoryFreeSize,
       "ax260aRomVersion": ax260aRomVersion,
       "ax260aCpuLoad1m": ax260aCpuLoad1m,
       "ax260aFlashTotalSize": ax260aFlashTotalSize,
       "ax260aFlashUsedSize": ax260aFlashUsedSize,
       "ax260aFlashFreeSize": ax260aFlashFreeSize,
       "ax260aSdCardStatus": ax260aSdCardStatus,
       "ax260aSdCardTotalSize": ax260aSdCardTotalSize,
       "ax260aSdCardUsedSize": ax260aSdCardUsedSize,
       "ax260aSdCardFreeSize": ax260aSdCardFreeSize,
       "ax260aPhysLineNumber": ax260aPhysLineNumber,
       "ax260aTemperatureStatusNumber": ax260aTemperatureStatusNumber,
       "ax260aPowerUnitNumber": ax260aPowerUnitNumber,
       "ax260aRedundantPsNumber": ax260aRedundantPsNumber,
       "ax260aFanNumber": ax260aFanNumber,
       "ax260aTotalAccumRunTime": ax260aTotalAccumRunTime,
       "ax260aCriticalAccumRunTime": ax260aCriticalAccumRunTime,
       "ax260aSts2LedStatus": ax260aSts2LedStatus,
       "ax260aTemperatureStatusTable": ax260aTemperatureStatusTable,
       "ax260aTemperatureStatusEntry": ax260aTemperatureStatusEntry,
       "ax260aTemperatureStatusIndex": ax260aTemperatureStatusIndex,
       "ax260aTemperatureStatusDescr": ax260aTemperatureStatusDescr,
       "ax260aTemperatureStatusValue": ax260aTemperatureStatusValue,
       "ax260aTemperatureThreshold": ax260aTemperatureThreshold,
       "ax260aTemperatureState": ax260aTemperatureState,
       "ax260aPowerUnitTable": ax260aPowerUnitTable,
       "ax260aPowerUnitEntry": ax260aPowerUnitEntry,
       "ax260aPowerUnitIndex": ax260aPowerUnitIndex,
       "ax260aPowerConnectStatus": ax260aPowerConnectStatus,
       "ax260aPowerSupplyStatus": ax260aPowerSupplyStatus,
       "ax260aFanTable": ax260aFanTable,
       "ax260aFanEntry": ax260aFanEntry,
       "ax260aFanIndex": ax260aFanIndex,
       "ax260aFanStatus": ax260aFanStatus,
       "ax260aRedundantPsTable": ax260aRedundantPsTable,
       "ax260aRedundantPsEntry": ax260aRedundantPsEntry,
       "ax260aRedundantPsIndex": ax260aRedundantPsIndex,
       "ax260aRedundantPsConnectStatus": ax260aRedundantPsConnectStatus,
       "ax260aRedundantPsStatus": ax260aRedundantPsStatus,
       "ax260aPhysLine": ax260aPhysLine,
       "ax260aPhysLineTable": ax260aPhysLineTable,
       "ax260aPhysLineEntry": ax260aPhysLineEntry,
       "ax260aPhysLineIndex": ax260aPhysLineIndex,
       "ax260aPhysLineConnectorType": ax260aPhysLineConnectorType,
       "ax260aPhysLineOperStatus": ax260aPhysLineOperStatus,
       "ax260aPhysLineIfIndexNumber": ax260aPhysLineIfIndexNumber,
       "ax260aPhysLineTransceiverStatus": ax260aPhysLineTransceiverStatus,
       "ax260aDeviceError": ax260aDeviceError,
       "ax260aMemoryError": ax260aMemoryError,
       "ax260aManagementMIB": ax260aManagementMIB,
       "ax260aOperationCommand": ax260aOperationCommand,
       "ax260aFdbClearMIB": ax260aFdbClearMIB,
       "ax260aFdbClearSet": ax260aFdbClearSet,
       "ax260aFdbClearReqTime": ax260aFdbClearReqTime,
       "ax260aFdbClearSuccessTime": ax260aFdbClearSuccessTime,
       "ax260aAuth": ax260aAuth,
       "ax260aAuthInfo": ax260aAuthInfo,
       "ax260aAuthSysName": ax260aAuthSysName,
       "ax260aAuthIfIndex": ax260aAuthIfIndex,
       "ax260aAuthSupplicantMac": ax260aAuthSupplicantMac,
       "ax260aAuthMessage": ax260aAuthMessage,
       "ax260aDot1x": ax260aDot1x,
       "ax260aWauth": ax260aWauth,
       "ax260aMauth": ax260aMauth}
)
