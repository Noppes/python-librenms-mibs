# SNMP MIB module (PRVT-MPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-MPLS-LDP-MIB

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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(MplsIndexType,) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsIndexType")

(MplsAtmVcIdentifier,
 MplsLabelDistributionMethod,
 MplsLdpIdentifier,
 MplsLdpLabelType,
 MplsLspType,
 MplsLsrIdentifier,
 MplsRetentionMode,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-PRIV-STDEXT-MIB",
    "MplsAtmVcIdentifier",
    "MplsLabelDistributionMethod",
    "MplsLdpIdentifier",
    "MplsLdpLabelType",
    "MplsLspType",
    "MplsLsrIdentifier",
    "MplsRetentionMode",
    "mplsStdMIB")

(mpls,
 prvtcrldpPmIndex,
 prvtcrldpSigIndex) = mibBuilder.importSymbols(
    "PRVT-CR-LDP-MIB",
    "mpls",
    "prvtcrldpPmIndex",
    "prvtcrldpSigIndex")

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
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsLdpStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mplsLdpStdMIB.setRevisions(
        ("2009-02-17 00:00",
         "2006-06-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsLabel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class MplsLdpLabelTypes(TextualConvention, Integer32):
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
        *(("generic", 1),
          ("atm", 2),
          ("frameRelay", 3))
    )



# MIB Managed Objects in the order of their OIDs

_MplsLdpObjects_ObjectIdentity = ObjectIdentity
mplsLdpObjects = _MplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1)
)
_MplsLdpLsrObjects_ObjectIdentity = ObjectIdentity
mplsLdpLsrObjects = _MplsLdpLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 1)
)
_MplsLdpLsrTable_Object = MibTable
mplsLdpLsrTable = _MplsLdpLsrTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLdpLsrTable.setStatus("current")
_MplsLdpLsrEntry_Object = MibTableRow
mplsLdpLsrEntry = _MplsLdpLsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 1, 1, 1)
)
mplsLdpLsrEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpLsrEntry.setStatus("current")
_MplsLdpLsrId_Type = MplsLsrIdentifier
_MplsLdpLsrId_Object = MibTableColumn
mplsLdpLsrId = _MplsLdpLsrId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 1, 1, 1, 1),
    _MplsLdpLsrId_Type()
)
mplsLdpLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLsrId.setStatus("current")


class _MplsLdpLsrLoopDetectionCapable_Type(Integer32):
    """Custom type mplsLdpLsrLoopDetectionCapable based on Integer32"""
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
        *(("none", 1),
          ("other", 2),
          ("hopCount", 3),
          ("pathVector", 4),
          ("hopCountAndPathVector", 5))
    )


_MplsLdpLsrLoopDetectionCapable_Type.__name__ = "Integer32"
_MplsLdpLsrLoopDetectionCapable_Object = MibTableColumn
mplsLdpLsrLoopDetectionCapable = _MplsLdpLsrLoopDetectionCapable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 1, 1, 1, 2),
    _MplsLdpLsrLoopDetectionCapable_Type()
)
mplsLdpLsrLoopDetectionCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLsrLoopDetectionCapable.setStatus("current")
_MplsLdpEntityObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityObjects = _MplsLdpEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2)
)
_MplsLdpEntityTable_Object = MibTable
mplsLdpEntityTable = _MplsLdpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityTable.setStatus("current")
_MplsLdpEntityEntry_Object = MibTableRow
mplsLdpEntityEntry = _MplsLdpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1)
)
mplsLdpEntityEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityEntry.setStatus("current")
_MplsLdpEntityLdpId_Type = MplsLdpIdentifier
_MplsLdpEntityLdpId_Object = MibTableColumn
mplsLdpEntityLdpId = _MplsLdpEntityLdpId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 1),
    _MplsLdpEntityLdpId_Type()
)
mplsLdpEntityLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityLdpId.setStatus("current")
_MplsLdpEntityIndex_Type = Unsigned32
_MplsLdpEntityIndex_Object = MibTableColumn
mplsLdpEntityIndex = _MplsLdpEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 2),
    _MplsLdpEntityIndex_Type()
)
mplsLdpEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityIndex.setStatus("current")


class _MplsLdpEntityProtocolVersion_Type(Integer32):
    """Custom type mplsLdpEntityProtocolVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityProtocolVersion_Type.__name__ = "Integer32"
_MplsLdpEntityProtocolVersion_Object = MibTableColumn
mplsLdpEntityProtocolVersion = _MplsLdpEntityProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 3),
    _MplsLdpEntityProtocolVersion_Type()
)
mplsLdpEntityProtocolVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityProtocolVersion.setStatus("current")


class _MplsLdpEntityAdminStatus_Type(Integer32):
    """Custom type mplsLdpEntityAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MplsLdpEntityAdminStatus_Type.__name__ = "Integer32"
_MplsLdpEntityAdminStatus_Object = MibTableColumn
mplsLdpEntityAdminStatus = _MplsLdpEntityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 4),
    _MplsLdpEntityAdminStatus_Type()
)
mplsLdpEntityAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAdminStatus.setStatus("current")


class _MplsLdpEntityOperStatus_Type(Integer32):
    """Custom type mplsLdpEntityOperStatus based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_MplsLdpEntityOperStatus_Type.__name__ = "Integer32"
_MplsLdpEntityOperStatus_Object = MibTableColumn
mplsLdpEntityOperStatus = _MplsLdpEntityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 5),
    _MplsLdpEntityOperStatus_Type()
)
mplsLdpEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityOperStatus.setStatus("current")


class _MplsLdpEntityWellKnownTcpDiscoveryPort_Type(InetPortNumber):
    """Custom type mplsLdpEntityWellKnownTcpDiscoveryPort based on InetPortNumber"""
    defaultValue = 646


_MplsLdpEntityWellKnownTcpDiscoveryPort_Type.__name__ = "InetPortNumber"
_MplsLdpEntityWellKnownTcpDiscoveryPort_Object = MibTableColumn
mplsLdpEntityWellKnownTcpDiscoveryPort = _MplsLdpEntityWellKnownTcpDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 6),
    _MplsLdpEntityWellKnownTcpDiscoveryPort_Type()
)
mplsLdpEntityWellKnownTcpDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityWellKnownTcpDiscoveryPort.setStatus("current")


class _MplsLdpEntityWellKnownUdpDiscoveryPort_Type(InetPortNumber):
    """Custom type mplsLdpEntityWellKnownUdpDiscoveryPort based on InetPortNumber"""
    defaultValue = 646


_MplsLdpEntityWellKnownUdpDiscoveryPort_Type.__name__ = "InetPortNumber"
_MplsLdpEntityWellKnownUdpDiscoveryPort_Object = MibTableColumn
mplsLdpEntityWellKnownUdpDiscoveryPort = _MplsLdpEntityWellKnownUdpDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 7),
    _MplsLdpEntityWellKnownUdpDiscoveryPort_Type()
)
mplsLdpEntityWellKnownUdpDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityWellKnownUdpDiscoveryPort.setStatus("current")


class _MplsLdpEntityMaxPduLength_Type(Unsigned32):
    """Custom type mplsLdpEntityMaxPduLength based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_MplsLdpEntityMaxPduLength_Type.__name__ = "Unsigned32"
_MplsLdpEntityMaxPduLength_Object = MibTableColumn
mplsLdpEntityMaxPduLength = _MplsLdpEntityMaxPduLength_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 8),
    _MplsLdpEntityMaxPduLength_Type()
)
mplsLdpEntityMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityMaxPduLength.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityMaxPduLength.setUnits("octets")


class _MplsLdpEntityKeepAliveHoldTimer_Type(Unsigned32):
    """Custom type mplsLdpEntityKeepAliveHoldTimer based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityKeepAliveHoldTimer_Type.__name__ = "Unsigned32"
_MplsLdpEntityKeepAliveHoldTimer_Object = MibTableColumn
mplsLdpEntityKeepAliveHoldTimer = _MplsLdpEntityKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 9),
    _MplsLdpEntityKeepAliveHoldTimer_Type()
)
mplsLdpEntityKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityKeepAliveHoldTimer.setUnits("seconds")


class _MplsLdpEntityHelloHoldTimer_Type(Unsigned32):
    """Custom type mplsLdpEntityHelloHoldTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLdpEntityHelloHoldTimer_Type.__name__ = "Unsigned32"
_MplsLdpEntityHelloHoldTimer_Object = MibTableColumn
mplsLdpEntityHelloHoldTimer = _MplsLdpEntityHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 10),
    _MplsLdpEntityHelloHoldTimer_Type()
)
mplsLdpEntityHelloHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityHelloHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityHelloHoldTimer.setUnits("seconds")


class _MplsLdpEntityInitSessionThreshold_Type(Integer32):
    """Custom type mplsLdpEntityInitSessionThreshold based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MplsLdpEntityInitSessionThreshold_Type.__name__ = "Integer32"
_MplsLdpEntityInitSessionThreshold_Object = MibTableColumn
mplsLdpEntityInitSessionThreshold = _MplsLdpEntityInitSessionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 11),
    _MplsLdpEntityInitSessionThreshold_Type()
)
mplsLdpEntityInitSessionThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityInitSessionThreshold.setStatus("current")
_MplsLdpEntityLabelDistMethod_Type = MplsLabelDistributionMethod
_MplsLdpEntityLabelDistMethod_Object = MibTableColumn
mplsLdpEntityLabelDistMethod = _MplsLdpEntityLabelDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 12),
    _MplsLdpEntityLabelDistMethod_Type()
)
mplsLdpEntityLabelDistMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityLabelDistMethod.setStatus("current")
_MplsLdpEntityLabelRetentionMode_Type = MplsRetentionMode
_MplsLdpEntityLabelRetentionMode_Object = MibTableColumn
mplsLdpEntityLabelRetentionMode = _MplsLdpEntityLabelRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 13),
    _MplsLdpEntityLabelRetentionMode_Type()
)
mplsLdpEntityLabelRetentionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityLabelRetentionMode.setStatus("current")


class _MplsLdpEntityPathVectorLimit_Type(Integer32):
    """Custom type mplsLdpEntityPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpEntityPathVectorLimit_Type.__name__ = "Integer32"
_MplsLdpEntityPathVectorLimit_Object = MibTableColumn
mplsLdpEntityPathVectorLimit = _MplsLdpEntityPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 14),
    _MplsLdpEntityPathVectorLimit_Type()
)
mplsLdpEntityPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityPathVectorLimit.setStatus("current")


class _MplsLdpEntityHopCountLimit_Type(Integer32):
    """Custom type mplsLdpEntityHopCountLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpEntityHopCountLimit_Type.__name__ = "Integer32"
_MplsLdpEntityHopCountLimit_Object = MibTableColumn
mplsLdpEntityHopCountLimit = _MplsLdpEntityHopCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 15),
    _MplsLdpEntityHopCountLimit_Type()
)
mplsLdpEntityHopCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityHopCountLimit.setStatus("current")


class _MplsLdpEntityTransportAddrKind_Type(Integer32):
    """Custom type mplsLdpEntityTransportAddrKind based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("loopback", 2))
    )


_MplsLdpEntityTransportAddrKind_Type.__name__ = "Integer32"
_MplsLdpEntityTransportAddrKind_Object = MibTableColumn
mplsLdpEntityTransportAddrKind = _MplsLdpEntityTransportAddrKind_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 16),
    _MplsLdpEntityTransportAddrKind_Type()
)
mplsLdpEntityTransportAddrKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTransportAddrKind.setStatus("current")


class _MplsLdpEntityTargetPeer_Type(TruthValue):
    """Custom type mplsLdpEntityTargetPeer based on TruthValue"""
    defaultValue = 2


_MplsLdpEntityTargetPeer_Type.__name__ = "TruthValue"
_MplsLdpEntityTargetPeer_Object = MibTableColumn
mplsLdpEntityTargetPeer = _MplsLdpEntityTargetPeer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 17),
    _MplsLdpEntityTargetPeer_Type()
)
mplsLdpEntityTargetPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetPeer.setStatus("current")
_MplsLdpEntityTargetPeerAddrType_Type = InetAddressType
_MplsLdpEntityTargetPeerAddrType_Object = MibTableColumn
mplsLdpEntityTargetPeerAddrType = _MplsLdpEntityTargetPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 18),
    _MplsLdpEntityTargetPeerAddrType_Type()
)
mplsLdpEntityTargetPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetPeerAddrType.setStatus("current")
_MplsLdpEntityTargetPeerAddr_Type = InetAddress
_MplsLdpEntityTargetPeerAddr_Object = MibTableColumn
mplsLdpEntityTargetPeerAddr = _MplsLdpEntityTargetPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 19),
    _MplsLdpEntityTargetPeerAddr_Type()
)
mplsLdpEntityTargetPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetPeerAddr.setStatus("current")
_MplsLdpEntityLabelType_Type = MplsLdpLabelType
_MplsLdpEntityLabelType_Object = MibTableColumn
mplsLdpEntityLabelType = _MplsLdpEntityLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 20),
    _MplsLdpEntityLabelType_Type()
)
mplsLdpEntityLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityLabelType.setStatus("current")
_MplsLdpEntityDiscontinuityTime_Type = TimeStamp
_MplsLdpEntityDiscontinuityTime_Object = MibTableColumn
mplsLdpEntityDiscontinuityTime = _MplsLdpEntityDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 21),
    _MplsLdpEntityDiscontinuityTime_Type()
)
mplsLdpEntityDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityDiscontinuityTime.setStatus("current")


class _MplsLdpEntityStorageType_Type(StorageType):
    """Custom type mplsLdpEntityStorageType based on StorageType"""
    defaultValue = 3


_MplsLdpEntityStorageType_Type.__name__ = "StorageType"
_MplsLdpEntityStorageType_Object = MibTableColumn
mplsLdpEntityStorageType = _MplsLdpEntityStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 22),
    _MplsLdpEntityStorageType_Type()
)
mplsLdpEntityStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStorageType.setStatus("current")


class _MplsLdpEntityWildcardEntity_Type(TruthValue):
    """Custom type mplsLdpEntityWildcardEntity based on TruthValue"""
    defaultValue = 2


_MplsLdpEntityWildcardEntity_Type.__name__ = "TruthValue"
_MplsLdpEntityWildcardEntity_Object = MibTableColumn
mplsLdpEntityWildcardEntity = _MplsLdpEntityWildcardEntity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 24),
    _MplsLdpEntityWildcardEntity_Type()
)
mplsLdpEntityWildcardEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityWildcardEntity.setStatus("current")
_MplsLdpEntityRowStatus_Type = RowStatus
_MplsLdpEntityRowStatus_Object = MibTableColumn
mplsLdpEntityRowStatus = _MplsLdpEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 1, 1, 25),
    _MplsLdpEntityRowStatus_Type()
)
mplsLdpEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityRowStatus.setStatus("current")
_MplsLdpEntityIndexNextTable_Object = MibTable
mplsLdpEntityIndexNextTable = _MplsLdpEntityIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityIndexNextTable.setStatus("current")
_MplsLdpEntityIndexNextEntry_Object = MibTableRow
mplsLdpEntityIndexNextEntry = _MplsLdpEntityIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 2, 1)
)
mplsLdpEntityIndexNextEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityIndexNextEntry.setStatus("current")


class _MplsLdpEntityIndexNext_Type(Unsigned32):
    """Custom type mplsLdpEntityIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLdpEntityIndexNext_Type.__name__ = "Unsigned32"
_MplsLdpEntityIndexNext_Object = MibTableColumn
mplsLdpEntityIndexNext = _MplsLdpEntityIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 2, 1, 1),
    _MplsLdpEntityIndexNext_Type()
)
mplsLdpEntityIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityIndexNext.setStatus("current")
_MplsLdpEntityStatsTable_Object = MibTable
mplsLdpEntityStatsTable = _MplsLdpEntityStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mplsLdpEntityStatsTable.setStatus("current")
_MplsLdpEntityStatsEntry_Object = MibTableRow
mplsLdpEntityStatsEntry = _MplsLdpEntityStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityStatsEntry.setStatus("current")
_MplsLdpEntityStatsSessionAttempts_Type = Counter32
_MplsLdpEntityStatsSessionAttempts_Object = MibTableColumn
mplsLdpEntityStatsSessionAttempts = _MplsLdpEntityStatsSessionAttempts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 1),
    _MplsLdpEntityStatsSessionAttempts_Type()
)
mplsLdpEntityStatsSessionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionAttempts.setStatus("current")
_MplsLdpEntityStatsSessionRejectedNoHelloErrors_Type = Counter32
_MplsLdpEntityStatsSessionRejectedNoHelloErrors_Object = MibTableColumn
mplsLdpEntityStatsSessionRejectedNoHelloErrors = _MplsLdpEntityStatsSessionRejectedNoHelloErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 2),
    _MplsLdpEntityStatsSessionRejectedNoHelloErrors_Type()
)
mplsLdpEntityStatsSessionRejectedNoHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionRejectedNoHelloErrors.setStatus("current")
_MplsLdpEntityStatsSessionRejectedAdErrors_Type = Counter32
_MplsLdpEntityStatsSessionRejectedAdErrors_Object = MibTableColumn
mplsLdpEntityStatsSessionRejectedAdErrors = _MplsLdpEntityStatsSessionRejectedAdErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 3),
    _MplsLdpEntityStatsSessionRejectedAdErrors_Type()
)
mplsLdpEntityStatsSessionRejectedAdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionRejectedAdErrors.setStatus("current")
_MplsLdpEntityStatsSessionRejectedMaxPduErrors_Type = Counter32
_MplsLdpEntityStatsSessionRejectedMaxPduErrors_Object = MibTableColumn
mplsLdpEntityStatsSessionRejectedMaxPduErrors = _MplsLdpEntityStatsSessionRejectedMaxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 4),
    _MplsLdpEntityStatsSessionRejectedMaxPduErrors_Type()
)
mplsLdpEntityStatsSessionRejectedMaxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionRejectedMaxPduErrors.setStatus("current")
_MplsLdpEntityStatsSessionRejectedLRErrors_Type = Counter32
_MplsLdpEntityStatsSessionRejectedLRErrors_Object = MibTableColumn
mplsLdpEntityStatsSessionRejectedLRErrors = _MplsLdpEntityStatsSessionRejectedLRErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 5),
    _MplsLdpEntityStatsSessionRejectedLRErrors_Type()
)
mplsLdpEntityStatsSessionRejectedLRErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionRejectedLRErrors.setStatus("current")
_MplsLdpEntityStatsBadLdpIdentifierErrors_Type = Counter32
_MplsLdpEntityStatsBadLdpIdentifierErrors_Object = MibTableColumn
mplsLdpEntityStatsBadLdpIdentifierErrors = _MplsLdpEntityStatsBadLdpIdentifierErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 6),
    _MplsLdpEntityStatsBadLdpIdentifierErrors_Type()
)
mplsLdpEntityStatsBadLdpIdentifierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsBadLdpIdentifierErrors.setStatus("current")
_MplsLdpEntityStatsBadPduLengthErrors_Type = Counter32
_MplsLdpEntityStatsBadPduLengthErrors_Object = MibTableColumn
mplsLdpEntityStatsBadPduLengthErrors = _MplsLdpEntityStatsBadPduLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 7),
    _MplsLdpEntityStatsBadPduLengthErrors_Type()
)
mplsLdpEntityStatsBadPduLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsBadPduLengthErrors.setStatus("current")
_MplsLdpEntityStatsBadMessageLengthErrors_Type = Counter32
_MplsLdpEntityStatsBadMessageLengthErrors_Object = MibTableColumn
mplsLdpEntityStatsBadMessageLengthErrors = _MplsLdpEntityStatsBadMessageLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 8),
    _MplsLdpEntityStatsBadMessageLengthErrors_Type()
)
mplsLdpEntityStatsBadMessageLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsBadMessageLengthErrors.setStatus("current")
_MplsLdpEntityStatsBadTlvLengthErrors_Type = Counter32
_MplsLdpEntityStatsBadTlvLengthErrors_Object = MibTableColumn
mplsLdpEntityStatsBadTlvLengthErrors = _MplsLdpEntityStatsBadTlvLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 9),
    _MplsLdpEntityStatsBadTlvLengthErrors_Type()
)
mplsLdpEntityStatsBadTlvLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsBadTlvLengthErrors.setStatus("current")
_MplsLdpEntityStatsMalformedTlvValueErrors_Type = Counter32
_MplsLdpEntityStatsMalformedTlvValueErrors_Object = MibTableColumn
mplsLdpEntityStatsMalformedTlvValueErrors = _MplsLdpEntityStatsMalformedTlvValueErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 10),
    _MplsLdpEntityStatsMalformedTlvValueErrors_Type()
)
mplsLdpEntityStatsMalformedTlvValueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsMalformedTlvValueErrors.setStatus("current")
_MplsLdpEntityStatsKeepAliveTimerExpErrors_Type = Counter32
_MplsLdpEntityStatsKeepAliveTimerExpErrors_Object = MibTableColumn
mplsLdpEntityStatsKeepAliveTimerExpErrors = _MplsLdpEntityStatsKeepAliveTimerExpErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 11),
    _MplsLdpEntityStatsKeepAliveTimerExpErrors_Type()
)
mplsLdpEntityStatsKeepAliveTimerExpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsKeepAliveTimerExpErrors.setStatus("current")
_MplsLdpEntityStatsShutdownReceivedNotifications_Type = Counter32
_MplsLdpEntityStatsShutdownReceivedNotifications_Object = MibTableColumn
mplsLdpEntityStatsShutdownReceivedNotifications = _MplsLdpEntityStatsShutdownReceivedNotifications_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 12),
    _MplsLdpEntityStatsShutdownReceivedNotifications_Type()
)
mplsLdpEntityStatsShutdownReceivedNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsShutdownReceivedNotifications.setStatus("current")
_MplsLdpEntityStatsShutdownSentNotifications_Type = Counter32
_MplsLdpEntityStatsShutdownSentNotifications_Object = MibTableColumn
mplsLdpEntityStatsShutdownSentNotifications = _MplsLdpEntityStatsShutdownSentNotifications_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 2, 4, 1, 13),
    _MplsLdpEntityStatsShutdownSentNotifications_Type()
)
mplsLdpEntityStatsShutdownSentNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsShutdownSentNotifications.setStatus("current")
_MplsLdpSessionObjects_ObjectIdentity = ObjectIdentity
mplsLdpSessionObjects = _MplsLdpSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3)
)
_MplsLdpPeerLastChange_Type = TimeStamp
_MplsLdpPeerLastChange_Object = MibScalar
mplsLdpPeerLastChange = _MplsLdpPeerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 1),
    _MplsLdpPeerLastChange_Type()
)
mplsLdpPeerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerLastChange.setStatus("current")
_MplsLdpPeerTable_Object = MibTable
mplsLdpPeerTable = _MplsLdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mplsLdpPeerTable.setStatus("current")
_MplsLdpPeerEntry_Object = MibTableRow
mplsLdpPeerEntry = _MplsLdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 2, 1)
)
mplsLdpPeerEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    mplsLdpPeerEntry.setStatus("current")
_MplsLdpPeerLdpId_Type = MplsLdpIdentifier
_MplsLdpPeerLdpId_Object = MibTableColumn
mplsLdpPeerLdpId = _MplsLdpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 2, 1, 1),
    _MplsLdpPeerLdpId_Type()
)
mplsLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpPeerLdpId.setStatus("current")
_MplsLdpPeerLabelDistMethod_Type = MplsLabelDistributionMethod
_MplsLdpPeerLabelDistMethod_Object = MibTableColumn
mplsLdpPeerLabelDistMethod = _MplsLdpPeerLabelDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 2, 1, 2),
    _MplsLdpPeerLabelDistMethod_Type()
)
mplsLdpPeerLabelDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerLabelDistMethod.setStatus("current")


class _MplsLdpPeerPathVectorLimit_Type(Integer32):
    """Custom type mplsLdpPeerPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpPeerPathVectorLimit_Type.__name__ = "Integer32"
_MplsLdpPeerPathVectorLimit_Object = MibTableColumn
mplsLdpPeerPathVectorLimit = _MplsLdpPeerPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 2, 1, 3),
    _MplsLdpPeerPathVectorLimit_Type()
)
mplsLdpPeerPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerPathVectorLimit.setStatus("current")
_MplsLdpPeerTransportAddrType_Type = InetAddressType
_MplsLdpPeerTransportAddrType_Object = MibTableColumn
mplsLdpPeerTransportAddrType = _MplsLdpPeerTransportAddrType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 2, 1, 4),
    _MplsLdpPeerTransportAddrType_Type()
)
mplsLdpPeerTransportAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerTransportAddrType.setStatus("current")
_MplsLdpPeerTransportAddr_Type = InetAddress
_MplsLdpPeerTransportAddr_Object = MibTableColumn
mplsLdpPeerTransportAddr = _MplsLdpPeerTransportAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 2, 1, 5),
    _MplsLdpPeerTransportAddr_Type()
)
mplsLdpPeerTransportAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerTransportAddr.setStatus("current")
_MplsLdpSessionTable_Object = MibTable
mplsLdpSessionTable = _MplsLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    mplsLdpSessionTable.setStatus("current")
_MplsLdpSessionEntry_Object = MibTableRow
mplsLdpSessionEntry = _MplsLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1)
)
mplsLdpSessionEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionEntry.setStatus("current")
_MplsLdpSessionStateLastChange_Type = TimeStamp
_MplsLdpSessionStateLastChange_Object = MibTableColumn
mplsLdpSessionStateLastChange = _MplsLdpSessionStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 1),
    _MplsLdpSessionStateLastChange_Type()
)
mplsLdpSessionStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStateLastChange.setStatus("current")


class _MplsLdpSessionState_Type(Integer32):
    """Custom type mplsLdpSessionState based on Integer32"""
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
        *(("nonexistent", 1),
          ("initialized", 2),
          ("openrec", 3),
          ("opensent", 4),
          ("operational", 5))
    )


_MplsLdpSessionState_Type.__name__ = "Integer32"
_MplsLdpSessionState_Object = MibTableColumn
mplsLdpSessionState = _MplsLdpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 2),
    _MplsLdpSessionState_Type()
)
mplsLdpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionState.setStatus("current")


class _MplsLdpSessionRole_Type(Integer32):
    """Custom type mplsLdpSessionRole based on Integer32"""
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
          ("active", 2),
          ("passive", 3))
    )


_MplsLdpSessionRole_Type.__name__ = "Integer32"
_MplsLdpSessionRole_Object = MibTableColumn
mplsLdpSessionRole = _MplsLdpSessionRole_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 3),
    _MplsLdpSessionRole_Type()
)
mplsLdpSessionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRole.setStatus("current")


class _MplsLdpSessionProtocolVersion_Type(Integer32):
    """Custom type mplsLdpSessionProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionProtocolVersion_Type.__name__ = "Integer32"
_MplsLdpSessionProtocolVersion_Object = MibTableColumn
mplsLdpSessionProtocolVersion = _MplsLdpSessionProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 4),
    _MplsLdpSessionProtocolVersion_Type()
)
mplsLdpSessionProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionProtocolVersion.setStatus("current")
_MplsLdpSessionKeepAliveHoldTimeRemaining_Type = TimeInterval
_MplsLdpSessionKeepAliveHoldTimeRemaining_Object = MibTableColumn
mplsLdpSessionKeepAliveHoldTimeRemaining = _MplsLdpSessionKeepAliveHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 5),
    _MplsLdpSessionKeepAliveHoldTimeRemaining_Type()
)
mplsLdpSessionKeepAliveHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionKeepAliveHoldTimeRemaining.setStatus("current")


class _MplsLdpSessionKeepAliveTime_Type(Unsigned32):
    """Custom type mplsLdpSessionKeepAliveTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionKeepAliveTime_Type.__name__ = "Unsigned32"
_MplsLdpSessionKeepAliveTime_Object = MibTableColumn
mplsLdpSessionKeepAliveTime = _MplsLdpSessionKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 6),
    _MplsLdpSessionKeepAliveTime_Type()
)
mplsLdpSessionKeepAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpSessionKeepAliveTime.setUnits("seconds")


class _MplsLdpSessionMaxPduLength_Type(Unsigned32):
    """Custom type mplsLdpSessionMaxPduLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionMaxPduLength_Type.__name__ = "Unsigned32"
_MplsLdpSessionMaxPduLength_Object = MibTableColumn
mplsLdpSessionMaxPduLength = _MplsLdpSessionMaxPduLength_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 7),
    _MplsLdpSessionMaxPduLength_Type()
)
mplsLdpSessionMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionMaxPduLength.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpSessionMaxPduLength.setUnits("octets")
_MplsLdpSessionDiscontinuityTime_Type = TimeStamp
_MplsLdpSessionDiscontinuityTime_Object = MibTableColumn
mplsLdpSessionDiscontinuityTime = _MplsLdpSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 8),
    _MplsLdpSessionDiscontinuityTime_Type()
)
mplsLdpSessionDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionDiscontinuityTime.setStatus("current")
_MplsLdpSessionConfiguredHoldTime_Type = Unsigned32
_MplsLdpSessionConfiguredHoldTime_Object = MibTableColumn
mplsLdpSessionConfiguredHoldTime = _MplsLdpSessionConfiguredHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 13),
    _MplsLdpSessionConfiguredHoldTime_Type()
)
mplsLdpSessionConfiguredHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionConfiguredHoldTime.setStatus("current")
_MplsLdpSessionPeerHoldTime_Type = Unsigned32
_MplsLdpSessionPeerHoldTime_Object = MibTableColumn
mplsLdpSessionPeerHoldTime = _MplsLdpSessionPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 14),
    _MplsLdpSessionPeerHoldTime_Type()
)
mplsLdpSessionPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerHoldTime.setStatus("current")
_MplsLdpSessionHoldTimeInUse_Type = Unsigned32
_MplsLdpSessionHoldTimeInUse_Object = MibTableColumn
mplsLdpSessionHoldTimeInUse = _MplsLdpSessionHoldTimeInUse_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 3, 1, 15),
    _MplsLdpSessionHoldTimeInUse_Type()
)
mplsLdpSessionHoldTimeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionHoldTimeInUse.setStatus("current")
_MplsLdpSessionStatsTable_Object = MibTable
mplsLdpSessionStatsTable = _MplsLdpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    mplsLdpSessionStatsTable.setStatus("current")
_MplsLdpSessionStatsEntry_Object = MibTableRow
mplsLdpSessionStatsEntry = _MplsLdpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 4, 1)
)
mplsLdpSessionStatsEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionStatsEntry.setStatus("current")
_MplsLdpSessionStatsUnknownMesTypeErrors_Type = Counter32
_MplsLdpSessionStatsUnknownMesTypeErrors_Object = MibTableColumn
mplsLdpSessionStatsUnknownMesTypeErrors = _MplsLdpSessionStatsUnknownMesTypeErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 4, 1, 1),
    _MplsLdpSessionStatsUnknownMesTypeErrors_Type()
)
mplsLdpSessionStatsUnknownMesTypeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStatsUnknownMesTypeErrors.setStatus("current")
_MplsLdpSessionStatsUnknownTlvErrors_Type = Counter32
_MplsLdpSessionStatsUnknownTlvErrors_Object = MibTableColumn
mplsLdpSessionStatsUnknownTlvErrors = _MplsLdpSessionStatsUnknownTlvErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 4, 1, 2),
    _MplsLdpSessionStatsUnknownTlvErrors_Type()
)
mplsLdpSessionStatsUnknownTlvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStatsUnknownTlvErrors.setStatus("current")
_MplsLdpHelloAdjacencyObjects_ObjectIdentity = ObjectIdentity
mplsLdpHelloAdjacencyObjects = _MplsLdpHelloAdjacencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 5)
)
_MplsLdpHelloAdjacencyTable_Object = MibTable
mplsLdpHelloAdjacencyTable = _MplsLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyTable.setStatus("current")
_MplsLdpHelloAdjacencyEntry_Object = MibTableRow
mplsLdpHelloAdjacencyEntry = _MplsLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 5, 1, 1)
)
mplsLdpHelloAdjacencyEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpHelloAdjacencyIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyEntry.setStatus("current")


class _MplsLdpHelloAdjacencyIndex_Type(Unsigned32):
    """Custom type mplsLdpHelloAdjacencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpHelloAdjacencyIndex_Type.__name__ = "Unsigned32"
_MplsLdpHelloAdjacencyIndex_Object = MibTableColumn
mplsLdpHelloAdjacencyIndex = _MplsLdpHelloAdjacencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 5, 1, 1, 1),
    _MplsLdpHelloAdjacencyIndex_Type()
)
mplsLdpHelloAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyIndex.setStatus("current")
_MplsLdpHelloAdjacencyHoldTimeRemaining_Type = TimeInterval
_MplsLdpHelloAdjacencyHoldTimeRemaining_Object = MibTableColumn
mplsLdpHelloAdjacencyHoldTimeRemaining = _MplsLdpHelloAdjacencyHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 5, 1, 1, 2),
    _MplsLdpHelloAdjacencyHoldTimeRemaining_Type()
)
mplsLdpHelloAdjacencyHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyHoldTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyHoldTimeRemaining.setUnits("seconds")


class _MplsLdpHelloAdjacencyHoldTime_Type(Unsigned32):
    """Custom type mplsLdpHelloAdjacencyHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLdpHelloAdjacencyHoldTime_Type.__name__ = "Unsigned32"
_MplsLdpHelloAdjacencyHoldTime_Object = MibTableColumn
mplsLdpHelloAdjacencyHoldTime = _MplsLdpHelloAdjacencyHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 5, 1, 1, 3),
    _MplsLdpHelloAdjacencyHoldTime_Type()
)
mplsLdpHelloAdjacencyHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyHoldTime.setStatus("current")


class _MplsLdpHelloAdjacencyType_Type(Integer32):
    """Custom type mplsLdpHelloAdjacencyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("targeted", 2))
    )


_MplsLdpHelloAdjacencyType_Type.__name__ = "Integer32"
_MplsLdpHelloAdjacencyType_Object = MibTableColumn
mplsLdpHelloAdjacencyType = _MplsLdpHelloAdjacencyType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 5, 1, 1, 4),
    _MplsLdpHelloAdjacencyType_Type()
)
mplsLdpHelloAdjacencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyType.setStatus("current")
_MplsLdpHelloAdjacencyConfiguredHoldTime_Type = Unsigned32
_MplsLdpHelloAdjacencyConfiguredHoldTime_Object = MibTableColumn
mplsLdpHelloAdjacencyConfiguredHoldTime = _MplsLdpHelloAdjacencyConfiguredHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 5, 1, 1, 5),
    _MplsLdpHelloAdjacencyConfiguredHoldTime_Type()
)
mplsLdpHelloAdjacencyConfiguredHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyConfiguredHoldTime.setStatus("current")
_MplsLdpHelloAdjacencyPeerHoldTime_Type = Unsigned32
_MplsLdpHelloAdjacencyPeerHoldTime_Object = MibTableColumn
mplsLdpHelloAdjacencyPeerHoldTime = _MplsLdpHelloAdjacencyPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 5, 1, 1, 6),
    _MplsLdpHelloAdjacencyPeerHoldTime_Type()
)
mplsLdpHelloAdjacencyPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyPeerHoldTime.setStatus("current")
_MplsInSegmentLdpLspTable_Object = MibTable
mplsInSegmentLdpLspTable = _MplsInSegmentLdpLspTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspTable.setStatus("current")
_MplsInSegmentLdpLspEntry_Object = MibTableRow
mplsInSegmentLdpLspEntry = _MplsInSegmentLdpLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 6, 1)
)
mplsInSegmentLdpLspEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsInSegmentLdpLspIndex"),
)
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspEntry.setStatus("current")
_MplsInSegmentLdpLspIndex_Type = MplsIndexType
_MplsInSegmentLdpLspIndex_Object = MibTableColumn
mplsInSegmentLdpLspIndex = _MplsInSegmentLdpLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 6, 1, 1),
    _MplsInSegmentLdpLspIndex_Type()
)
mplsInSegmentLdpLspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspIndex.setStatus("current")
_MplsInSegmentLdpLspLabelType_Type = MplsLdpLabelType
_MplsInSegmentLdpLspLabelType_Object = MibTableColumn
mplsInSegmentLdpLspLabelType = _MplsInSegmentLdpLspLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 6, 1, 2),
    _MplsInSegmentLdpLspLabelType_Type()
)
mplsInSegmentLdpLspLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspLabelType.setStatus("current")
_MplsInSegmentLdpLspType_Type = MplsLspType
_MplsInSegmentLdpLspType_Object = MibTableColumn
mplsInSegmentLdpLspType = _MplsInSegmentLdpLspType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 6, 1, 3),
    _MplsInSegmentLdpLspType_Type()
)
mplsInSegmentLdpLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspType.setStatus("current")
_MplsOutSegmentLdpLspTable_Object = MibTable
mplsOutSegmentLdpLspTable = _MplsOutSegmentLdpLspTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspTable.setStatus("current")
_MplsOutSegmentLdpLspEntry_Object = MibTableRow
mplsOutSegmentLdpLspEntry = _MplsOutSegmentLdpLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 7, 1)
)
mplsOutSegmentLdpLspEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsOutSegmentLdpLspIndex"),
)
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspEntry.setStatus("current")
_MplsOutSegmentLdpLspIndex_Type = MplsIndexType
_MplsOutSegmentLdpLspIndex_Object = MibTableColumn
mplsOutSegmentLdpLspIndex = _MplsOutSegmentLdpLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 7, 1, 1),
    _MplsOutSegmentLdpLspIndex_Type()
)
mplsOutSegmentLdpLspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspIndex.setStatus("current")
_MplsOutSegmentLdpLspLabelType_Type = MplsLdpLabelType
_MplsOutSegmentLdpLspLabelType_Object = MibTableColumn
mplsOutSegmentLdpLspLabelType = _MplsOutSegmentLdpLspLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 7, 1, 2),
    _MplsOutSegmentLdpLspLabelType_Type()
)
mplsOutSegmentLdpLspLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspLabelType.setStatus("current")
_MplsOutSegmentLdpLspType_Type = MplsLspType
_MplsOutSegmentLdpLspType_Object = MibTableColumn
mplsOutSegmentLdpLspType = _MplsOutSegmentLdpLspType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 7, 1, 3),
    _MplsOutSegmentLdpLspType_Type()
)
mplsOutSegmentLdpLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspType.setStatus("current")
_MplsFecObjects_ObjectIdentity = ObjectIdentity
mplsFecObjects = _MplsFecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10)
)
_MplsFecLastChange_Type = TimeStamp
_MplsFecLastChange_Object = MibScalar
mplsFecLastChange = _MplsFecLastChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10, 1),
    _MplsFecLastChange_Type()
)
mplsFecLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFecLastChange.setStatus("current")
_MplsFecTable_Object = MibTable
mplsFecTable = _MplsFecTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10, 2)
)
if mibBuilder.loadTexts:
    mplsFecTable.setStatus("current")
_MplsFecEntry_Object = MibTableRow
mplsFecEntry = _MplsFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10, 2, 1)
)
mplsFecEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsFecIndex"),
)
if mibBuilder.loadTexts:
    mplsFecEntry.setStatus("current")


class _MplsFecIndex_Type(Unsigned32):
    """Custom type mplsFecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsFecIndex_Type.__name__ = "Unsigned32"
_MplsFecIndex_Object = MibTableColumn
mplsFecIndex = _MplsFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10, 2, 1, 1),
    _MplsFecIndex_Type()
)
mplsFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFecIndex.setStatus("current")


class _MplsFecType_Type(Integer32):
    """Custom type mplsFecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prefix", 1),
          ("hostAddress", 2))
    )


_MplsFecType_Type.__name__ = "Integer32"
_MplsFecType_Object = MibTableColumn
mplsFecType = _MplsFecType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10, 2, 1, 2),
    _MplsFecType_Type()
)
mplsFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFecType.setStatus("current")


class _MplsFecAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type mplsFecAddrPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_MplsFecAddrPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_MplsFecAddrPrefixLength_Object = MibTableColumn
mplsFecAddrPrefixLength = _MplsFecAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10, 2, 1, 3),
    _MplsFecAddrPrefixLength_Type()
)
mplsFecAddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFecAddrPrefixLength.setStatus("current")
_MplsFecAddrType_Type = InetAddressType
_MplsFecAddrType_Object = MibTableColumn
mplsFecAddrType = _MplsFecAddrType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10, 2, 1, 4),
    _MplsFecAddrType_Type()
)
mplsFecAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFecAddrType.setStatus("current")
_MplsFecAddr_Type = InetAddress
_MplsFecAddr_Object = MibTableColumn
mplsFecAddr = _MplsFecAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10, 2, 1, 5),
    _MplsFecAddr_Type()
)
mplsFecAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFecAddr.setStatus("current")


class _MplsFecStorageType_Type(StorageType):
    """Custom type mplsFecStorageType based on StorageType"""
    defaultValue = 3


_MplsFecStorageType_Type.__name__ = "StorageType"
_MplsFecStorageType_Object = MibTableColumn
mplsFecStorageType = _MplsFecStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 10, 2, 1, 6),
    _MplsFecStorageType_Type()
)
mplsFecStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFecStorageType.setStatus("current")
_MplsLdpLspFecLastChange_Type = TimeStamp
_MplsLdpLspFecLastChange_Object = MibScalar
mplsLdpLspFecLastChange = _MplsLdpLspFecLastChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 11),
    _MplsLdpLspFecLastChange_Type()
)
mplsLdpLspFecLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLspFecLastChange.setStatus("current")
_MplsLdpLspFecTable_Object = MibTable
mplsLdpLspFecTable = _MplsLdpLspFecTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    mplsLdpLspFecTable.setStatus("current")
_MplsLdpLspFecEntry_Object = MibTableRow
mplsLdpLspFecEntry = _MplsLdpLspFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 12, 1)
)
mplsLdpLspFecEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpLspFecSegment"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpLspFecSegmentIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpLspFecIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpLspFecEntry.setStatus("current")


class _MplsLdpLspFecSegment_Type(Integer32):
    """Custom type mplsLdpLspFecSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSegment", 1),
          ("outSegment", 2))
    )


_MplsLdpLspFecSegment_Type.__name__ = "Integer32"
_MplsLdpLspFecSegment_Object = MibTableColumn
mplsLdpLspFecSegment = _MplsLdpLspFecSegment_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 12, 1, 1),
    _MplsLdpLspFecSegment_Type()
)
mplsLdpLspFecSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpLspFecSegment.setStatus("current")
_MplsLdpLspFecSegmentIndex_Type = MplsIndexType
_MplsLdpLspFecSegmentIndex_Object = MibTableColumn
mplsLdpLspFecSegmentIndex = _MplsLdpLspFecSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 12, 1, 2),
    _MplsLdpLspFecSegmentIndex_Type()
)
mplsLdpLspFecSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpLspFecSegmentIndex.setStatus("current")


class _MplsLdpLspFecIndex_Type(Integer32):
    """Custom type mplsLdpLspFecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLdpLspFecIndex_Type.__name__ = "Integer32"
_MplsLdpLspFecIndex_Object = MibTableColumn
mplsLdpLspFecIndex = _MplsLdpLspFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 12, 1, 3),
    _MplsLdpLspFecIndex_Type()
)
mplsLdpLspFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpLspFecIndex.setStatus("current")


class _MplsLdpLspFecStorageType_Type(StorageType):
    """Custom type mplsLdpLspFecStorageType based on StorageType"""
    defaultValue = 3


_MplsLdpLspFecStorageType_Type.__name__ = "StorageType"
_MplsLdpLspFecStorageType_Object = MibTableColumn
mplsLdpLspFecStorageType = _MplsLdpLspFecStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 12, 1, 4),
    _MplsLdpLspFecStorageType_Type()
)
mplsLdpLspFecStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpLspFecStorageType.setStatus("current")
_MplsLdpLspFecRowStatus_Type = RowStatus
_MplsLdpLspFecRowStatus_Object = MibTableColumn
mplsLdpLspFecRowStatus = _MplsLdpLspFecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 12, 1, 5),
    _MplsLdpLspFecRowStatus_Type()
)
mplsLdpLspFecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpLspFecRowStatus.setStatus("current")
_MplsLdpSessionPeerAddrTable_Object = MibTable
mplsLdpSessionPeerAddrTable = _MplsLdpSessionPeerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddrTable.setStatus("current")
_MplsLdpSessionPeerAddrEntry_Object = MibTableRow
mplsLdpSessionPeerAddrEntry = _MplsLdpSessionPeerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 13, 1)
)
mplsLdpSessionPeerAddrEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpSessionPeerAddrIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddrEntry.setStatus("current")


class _MplsLdpSessionPeerAddrIndex_Type(Unsigned32):
    """Custom type mplsLdpSessionPeerAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpSessionPeerAddrIndex_Type.__name__ = "Unsigned32"
_MplsLdpSessionPeerAddrIndex_Object = MibTableColumn
mplsLdpSessionPeerAddrIndex = _MplsLdpSessionPeerAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 13, 1, 1),
    _MplsLdpSessionPeerAddrIndex_Type()
)
mplsLdpSessionPeerAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddrIndex.setStatus("current")
_MplsLdpSessionPeerNextHopAddrType_Type = InetAddressType
_MplsLdpSessionPeerNextHopAddrType_Object = MibTableColumn
mplsLdpSessionPeerNextHopAddrType = _MplsLdpSessionPeerNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 13, 1, 2),
    _MplsLdpSessionPeerNextHopAddrType_Type()
)
mplsLdpSessionPeerNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerNextHopAddrType.setStatus("current")
_MplsLdpSessionPeerNextHopAddr_Type = InetAddress
_MplsLdpSessionPeerNextHopAddr_Object = MibTableColumn
mplsLdpSessionPeerNextHopAddr = _MplsLdpSessionPeerNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 1, 3, 13, 1, 3),
    _MplsLdpSessionPeerNextHopAddr_Type()
)
mplsLdpSessionPeerNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerNextHopAddr.setStatus("current")
_MplsLdpNotifications_ObjectIdentity = ObjectIdentity
mplsLdpNotifications = _MplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 2, 0)
)
_MplsLdpConformance_ObjectIdentity = ObjectIdentity
mplsLdpConformance = _MplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 3)
)
_MplsLdpGroups_ObjectIdentity = ObjectIdentity
mplsLdpGroups = _MplsLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 3, 1)
)
_MplsLdpCompliances_ObjectIdentity = ObjectIdentity
mplsLdpCompliances = _MplsLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 3, 2)
)
_MplsLdpAtmObjects_ObjectIdentity = ObjectIdentity
mplsLdpAtmObjects = _MplsLdpAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4)
)
_MplsLdpEntityAtmObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityAtmObjects = _MplsLdpEntityAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1)
)
_MplsLdpEntityAtmTable_Object = MibTable
mplsLdpEntityAtmTable = _MplsLdpEntityAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmTable.setStatus("current")
_MplsLdpEntityAtmEntry_Object = MibTableRow
mplsLdpEntityAtmEntry = _MplsLdpEntityAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1)
)
mplsLdpEntityAtmEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmEntry.setStatus("current")
_MplsLdpEntityAtmIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityAtmIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityAtmIfIndexOrZero = _MplsLdpEntityAtmIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 1),
    _MplsLdpEntityAtmIfIndexOrZero_Type()
)
mplsLdpEntityAtmIfIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmIfIndexOrZero.setStatus("current")


class _MplsLdpEntityAtmMergeCap_Type(Integer32):
    """Custom type mplsLdpEntityAtmMergeCap based on Integer32"""
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
        *(("notSupported", 0),
          ("vpMerge", 1),
          ("vcMerge", 2),
          ("vpAndVcMerge", 3))
    )


_MplsLdpEntityAtmMergeCap_Type.__name__ = "Integer32"
_MplsLdpEntityAtmMergeCap_Object = MibTableColumn
mplsLdpEntityAtmMergeCap = _MplsLdpEntityAtmMergeCap_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 2),
    _MplsLdpEntityAtmMergeCap_Type()
)
mplsLdpEntityAtmMergeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmMergeCap.setStatus("current")


class _MplsLdpEntityAtmLRComponents_Type(Unsigned32):
    """Custom type mplsLdpEntityAtmLRComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityAtmLRComponents_Type.__name__ = "Unsigned32"
_MplsLdpEntityAtmLRComponents_Object = MibTableColumn
mplsLdpEntityAtmLRComponents = _MplsLdpEntityAtmLRComponents_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 3),
    _MplsLdpEntityAtmLRComponents_Type()
)
mplsLdpEntityAtmLRComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRComponents.setStatus("current")


class _MplsLdpEntityAtmVcDirectionality_Type(Integer32):
    """Custom type mplsLdpEntityAtmVcDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 0),
          ("unidirectional", 1))
    )


_MplsLdpEntityAtmVcDirectionality_Type.__name__ = "Integer32"
_MplsLdpEntityAtmVcDirectionality_Object = MibTableColumn
mplsLdpEntityAtmVcDirectionality = _MplsLdpEntityAtmVcDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 4),
    _MplsLdpEntityAtmVcDirectionality_Type()
)
mplsLdpEntityAtmVcDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmVcDirectionality.setStatus("current")


class _MplsLdpEntityAtmLsrConnectivity_Type(Integer32):
    """Custom type mplsLdpEntityAtmLsrConnectivity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("indirect", 2))
    )


_MplsLdpEntityAtmLsrConnectivity_Type.__name__ = "Integer32"
_MplsLdpEntityAtmLsrConnectivity_Object = MibTableColumn
mplsLdpEntityAtmLsrConnectivity = _MplsLdpEntityAtmLsrConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 5),
    _MplsLdpEntityAtmLsrConnectivity_Type()
)
mplsLdpEntityAtmLsrConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLsrConnectivity.setStatus("current")


class _MplsLdpEntityAtmDefaultControlVpi_Type(Integer32):
    """Custom type mplsLdpEntityAtmDefaultControlVpi based on Integer32"""
    defaultValue = 0


_MplsLdpEntityAtmDefaultControlVpi_Type.__name__ = "Integer32"
_MplsLdpEntityAtmDefaultControlVpi_Object = MibTableColumn
mplsLdpEntityAtmDefaultControlVpi = _MplsLdpEntityAtmDefaultControlVpi_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 6),
    _MplsLdpEntityAtmDefaultControlVpi_Type()
)
mplsLdpEntityAtmDefaultControlVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmDefaultControlVpi.setStatus("current")


class _MplsLdpEntityAtmDefaultControlVci_Type(MplsAtmVcIdentifier):
    """Custom type mplsLdpEntityAtmDefaultControlVci based on MplsAtmVcIdentifier"""
    defaultValue = 32


_MplsLdpEntityAtmDefaultControlVci_Type.__name__ = "MplsAtmVcIdentifier"
_MplsLdpEntityAtmDefaultControlVci_Object = MibTableColumn
mplsLdpEntityAtmDefaultControlVci = _MplsLdpEntityAtmDefaultControlVci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 7),
    _MplsLdpEntityAtmDefaultControlVci_Type()
)
mplsLdpEntityAtmDefaultControlVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmDefaultControlVci.setStatus("current")


class _MplsLdpEntityAtmUnlabTrafVpi_Type(Integer32):
    """Custom type mplsLdpEntityAtmUnlabTrafVpi based on Integer32"""
    defaultValue = 0


_MplsLdpEntityAtmUnlabTrafVpi_Type.__name__ = "Integer32"
_MplsLdpEntityAtmUnlabTrafVpi_Object = MibTableColumn
mplsLdpEntityAtmUnlabTrafVpi = _MplsLdpEntityAtmUnlabTrafVpi_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 8),
    _MplsLdpEntityAtmUnlabTrafVpi_Type()
)
mplsLdpEntityAtmUnlabTrafVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmUnlabTrafVpi.setStatus("current")


class _MplsLdpEntityAtmUnlabTrafVci_Type(MplsAtmVcIdentifier):
    """Custom type mplsLdpEntityAtmUnlabTrafVci based on MplsAtmVcIdentifier"""
    defaultValue = 32


_MplsLdpEntityAtmUnlabTrafVci_Type.__name__ = "MplsAtmVcIdentifier"
_MplsLdpEntityAtmUnlabTrafVci_Object = MibTableColumn
mplsLdpEntityAtmUnlabTrafVci = _MplsLdpEntityAtmUnlabTrafVci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 9),
    _MplsLdpEntityAtmUnlabTrafVci_Type()
)
mplsLdpEntityAtmUnlabTrafVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmUnlabTrafVci.setStatus("current")


class _MplsLdpEntityAtmStorageType_Type(StorageType):
    """Custom type mplsLdpEntityAtmStorageType based on StorageType"""
    defaultValue = 3


_MplsLdpEntityAtmStorageType_Type.__name__ = "StorageType"
_MplsLdpEntityAtmStorageType_Object = MibTableColumn
mplsLdpEntityAtmStorageType = _MplsLdpEntityAtmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 1, 1, 10),
    _MplsLdpEntityAtmStorageType_Type()
)
mplsLdpEntityAtmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmStorageType.setStatus("current")
_MplsLdpEntityAtmLRTable_Object = MibTable
mplsLdpEntityAtmLRTable = _MplsLdpEntityAtmLRTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRTable.setStatus("current")
_MplsLdpEntityAtmLREntry_Object = MibTableRow
mplsLdpEntityAtmLREntry = _MplsLdpEntityAtmLREntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 2, 1)
)
mplsLdpEntityAtmLREntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmLRMinVpi"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmLRMinVci"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLREntry.setStatus("current")


class _MplsLdpEntityAtmLRMinVpi_Type(Integer32):
    """Custom type mplsLdpEntityAtmLRMinVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLdpEntityAtmLRMinVpi_Type.__name__ = "Integer32"
_MplsLdpEntityAtmLRMinVpi_Object = MibTableColumn
mplsLdpEntityAtmLRMinVpi = _MplsLdpEntityAtmLRMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 2, 1, 1),
    _MplsLdpEntityAtmLRMinVpi_Type()
)
mplsLdpEntityAtmLRMinVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRMinVpi.setStatus("current")
_MplsLdpEntityAtmLRMinVci_Type = MplsAtmVcIdentifier
_MplsLdpEntityAtmLRMinVci_Object = MibTableColumn
mplsLdpEntityAtmLRMinVci = _MplsLdpEntityAtmLRMinVci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 2, 1, 2),
    _MplsLdpEntityAtmLRMinVci_Type()
)
mplsLdpEntityAtmLRMinVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRMinVci.setStatus("current")
_MplsLdpEntityAtmLRMaxVpi_Type = Integer32
_MplsLdpEntityAtmLRMaxVpi_Object = MibTableColumn
mplsLdpEntityAtmLRMaxVpi = _MplsLdpEntityAtmLRMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 2, 1, 3),
    _MplsLdpEntityAtmLRMaxVpi_Type()
)
mplsLdpEntityAtmLRMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRMaxVpi.setStatus("current")
_MplsLdpEntityAtmLRMaxVci_Type = MplsAtmVcIdentifier
_MplsLdpEntityAtmLRMaxVci_Object = MibTableColumn
mplsLdpEntityAtmLRMaxVci = _MplsLdpEntityAtmLRMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 2, 1, 4),
    _MplsLdpEntityAtmLRMaxVci_Type()
)
mplsLdpEntityAtmLRMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRMaxVci.setStatus("current")


class _MplsLdpEntityAtmLRStorageType_Type(StorageType):
    """Custom type mplsLdpEntityAtmLRStorageType based on StorageType"""
    defaultValue = 3


_MplsLdpEntityAtmLRStorageType_Type.__name__ = "StorageType"
_MplsLdpEntityAtmLRStorageType_Object = MibTableColumn
mplsLdpEntityAtmLRStorageType = _MplsLdpEntityAtmLRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 1, 2, 1, 5),
    _MplsLdpEntityAtmLRStorageType_Type()
)
mplsLdpEntityAtmLRStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRStorageType.setStatus("current")
_MplsLdpAtmSessionObjects_ObjectIdentity = ObjectIdentity
mplsLdpAtmSessionObjects = _MplsLdpAtmSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 2)
)
_MplsLdpAtmSessionTable_Object = MibTable
mplsLdpAtmSessionTable = _MplsLdpAtmSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpAtmSessionTable.setStatus("current")
_MplsLdpAtmSessionEntry_Object = MibTableRow
mplsLdpAtmSessionEntry = _MplsLdpAtmSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 2, 1, 1)
)
mplsLdpAtmSessionEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpSessionAtmLRLowerBoundVpi"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpSessionAtmLRLowerBoundVci"),
)
if mibBuilder.loadTexts:
    mplsLdpAtmSessionEntry.setStatus("current")


class _MplsLdpSessionAtmLRLowerBoundVpi_Type(Integer32):
    """Custom type mplsLdpSessionAtmLRLowerBoundVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLdpSessionAtmLRLowerBoundVpi_Type.__name__ = "Integer32"
_MplsLdpSessionAtmLRLowerBoundVpi_Object = MibTableColumn
mplsLdpSessionAtmLRLowerBoundVpi = _MplsLdpSessionAtmLRLowerBoundVpi_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 2, 1, 1, 1),
    _MplsLdpSessionAtmLRLowerBoundVpi_Type()
)
mplsLdpSessionAtmLRLowerBoundVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLRLowerBoundVpi.setStatus("current")
_MplsLdpSessionAtmLRLowerBoundVci_Type = MplsAtmVcIdentifier
_MplsLdpSessionAtmLRLowerBoundVci_Object = MibTableColumn
mplsLdpSessionAtmLRLowerBoundVci = _MplsLdpSessionAtmLRLowerBoundVci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 2, 1, 1, 2),
    _MplsLdpSessionAtmLRLowerBoundVci_Type()
)
mplsLdpSessionAtmLRLowerBoundVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLRLowerBoundVci.setStatus("current")
_MplsLdpSessionAtmLRUpperBoundVpi_Type = Integer32
_MplsLdpSessionAtmLRUpperBoundVpi_Object = MibTableColumn
mplsLdpSessionAtmLRUpperBoundVpi = _MplsLdpSessionAtmLRUpperBoundVpi_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 2, 1, 1, 3),
    _MplsLdpSessionAtmLRUpperBoundVpi_Type()
)
mplsLdpSessionAtmLRUpperBoundVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLRUpperBoundVpi.setStatus("current")
_MplsLdpSessionAtmLRUpperBoundVci_Type = MplsAtmVcIdentifier
_MplsLdpSessionAtmLRUpperBoundVci_Object = MibTableColumn
mplsLdpSessionAtmLRUpperBoundVci = _MplsLdpSessionAtmLRUpperBoundVci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 4, 2, 1, 1, 4),
    _MplsLdpSessionAtmLRUpperBoundVci_Type()
)
mplsLdpSessionAtmLRUpperBoundVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLRUpperBoundVci.setStatus("current")
_MplsLdpAtmConformance_ObjectIdentity = ObjectIdentity
mplsLdpAtmConformance = _MplsLdpAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 5)
)
_MplsLdpAtmGroups_ObjectIdentity = ObjectIdentity
mplsLdpAtmGroups = _MplsLdpAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 5, 1)
)
_MplsLdpAtmCompliances_ObjectIdentity = ObjectIdentity
mplsLdpAtmCompliances = _MplsLdpAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 5, 2)
)
_MplsLdpFrameRelayObjects_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelayObjects = _MplsLdpFrameRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6)
)
_MplsLdpEntityFrameRelayObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityFrameRelayObjects = _MplsLdpEntityFrameRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1)
)
_MplsLdpEntityFrameRelayTable_Object = MibTable
mplsLdpEntityFrameRelayTable = _MplsLdpEntityFrameRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayTable.setStatus("current")
_MplsLdpEntityFrameRelayEntry_Object = MibTableRow
mplsLdpEntityFrameRelayEntry = _MplsLdpEntityFrameRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 1, 1)
)
mplsLdpEntityFrameRelayEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayEntry.setStatus("current")
_MplsLdpEntityFrameRelayIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityFrameRelayIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityFrameRelayIfIndexOrZero = _MplsLdpEntityFrameRelayIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 1, 1, 1),
    _MplsLdpEntityFrameRelayIfIndexOrZero_Type()
)
mplsLdpEntityFrameRelayIfIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayIfIndexOrZero.setStatus("current")


class _MplsLdpEntityFrameRelayMergeCap_Type(Integer32):
    """Custom type mplsLdpEntityFrameRelayMergeCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("supported", 1))
    )


_MplsLdpEntityFrameRelayMergeCap_Type.__name__ = "Integer32"
_MplsLdpEntityFrameRelayMergeCap_Object = MibTableColumn
mplsLdpEntityFrameRelayMergeCap = _MplsLdpEntityFrameRelayMergeCap_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 1, 1, 2),
    _MplsLdpEntityFrameRelayMergeCap_Type()
)
mplsLdpEntityFrameRelayMergeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayMergeCap.setStatus("current")


class _MplsLdpEntityFrameRelayLRComponents_Type(Unsigned32):
    """Custom type mplsLdpEntityFrameRelayLRComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityFrameRelayLRComponents_Type.__name__ = "Unsigned32"
_MplsLdpEntityFrameRelayLRComponents_Object = MibTableColumn
mplsLdpEntityFrameRelayLRComponents = _MplsLdpEntityFrameRelayLRComponents_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 1, 1, 3),
    _MplsLdpEntityFrameRelayLRComponents_Type()
)
mplsLdpEntityFrameRelayLRComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRComponents.setStatus("current")


class _MplsLdpEntityFrameRelayVcDirectionality_Type(Integer32):
    """Custom type mplsLdpEntityFrameRelayVcDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 0),
          ("unidirection", 1))
    )


_MplsLdpEntityFrameRelayVcDirectionality_Type.__name__ = "Integer32"
_MplsLdpEntityFrameRelayVcDirectionality_Object = MibTableColumn
mplsLdpEntityFrameRelayVcDirectionality = _MplsLdpEntityFrameRelayVcDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 1, 1, 4),
    _MplsLdpEntityFrameRelayVcDirectionality_Type()
)
mplsLdpEntityFrameRelayVcDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayVcDirectionality.setStatus("current")


class _MplsLdpEntityFrameRelayStorageType_Type(StorageType):
    """Custom type mplsLdpEntityFrameRelayStorageType based on StorageType"""
    defaultValue = 3


_MplsLdpEntityFrameRelayStorageType_Type.__name__ = "StorageType"
_MplsLdpEntityFrameRelayStorageType_Object = MibTableColumn
mplsLdpEntityFrameRelayStorageType = _MplsLdpEntityFrameRelayStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 1, 1, 5),
    _MplsLdpEntityFrameRelayStorageType_Type()
)
mplsLdpEntityFrameRelayStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayStorageType.setStatus("current")
_MplsLdpEntityFrameRelayLRTable_Object = MibTable
mplsLdpEntityFrameRelayLRTable = _MplsLdpEntityFrameRelayLRTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRTable.setStatus("current")
_MplsLdpEntityFrameRelayLREntry_Object = MibTableRow
mplsLdpEntityFrameRelayLREntry = _MplsLdpEntityFrameRelayLREntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 2, 1)
)
mplsLdpEntityFrameRelayLREntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityFrameRelayLRMinDlci"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLREntry.setStatus("current")


class _MplsLdpEntityFrameRelayLRMinDlci_Type(Integer32):
    """Custom type mplsLdpEntityFrameRelayLRMinDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLdpEntityFrameRelayLRMinDlci_Type.__name__ = "Integer32"
_MplsLdpEntityFrameRelayLRMinDlci_Object = MibTableColumn
mplsLdpEntityFrameRelayLRMinDlci = _MplsLdpEntityFrameRelayLRMinDlci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 2, 1, 1),
    _MplsLdpEntityFrameRelayLRMinDlci_Type()
)
mplsLdpEntityFrameRelayLRMinDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRMinDlci.setStatus("current")
_MplsLdpEntityFrameRelayLRMaxDlci_Type = Integer32
_MplsLdpEntityFrameRelayLRMaxDlci_Object = MibTableColumn
mplsLdpEntityFrameRelayLRMaxDlci = _MplsLdpEntityFrameRelayLRMaxDlci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 2, 1, 2),
    _MplsLdpEntityFrameRelayLRMaxDlci_Type()
)
mplsLdpEntityFrameRelayLRMaxDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRMaxDlci.setStatus("current")


class _MplsLdpEntityFrameRelayLRLen_Type(Integer32):
    """Custom type mplsLdpEntityFrameRelayLRLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenDlciBits", 0),
          ("twentyThreeDlciBits", 2))
    )


_MplsLdpEntityFrameRelayLRLen_Type.__name__ = "Integer32"
_MplsLdpEntityFrameRelayLRLen_Object = MibTableColumn
mplsLdpEntityFrameRelayLRLen = _MplsLdpEntityFrameRelayLRLen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 2, 1, 3),
    _MplsLdpEntityFrameRelayLRLen_Type()
)
mplsLdpEntityFrameRelayLRLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRLen.setStatus("current")


class _MplsLdpEntityFrameRelayLRStorageType_Type(StorageType):
    """Custom type mplsLdpEntityFrameRelayLRStorageType based on StorageType"""
    defaultValue = 3


_MplsLdpEntityFrameRelayLRStorageType_Type.__name__ = "StorageType"
_MplsLdpEntityFrameRelayLRStorageType_Object = MibTableColumn
mplsLdpEntityFrameRelayLRStorageType = _MplsLdpEntityFrameRelayLRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 1, 2, 1, 4),
    _MplsLdpEntityFrameRelayLRStorageType_Type()
)
mplsLdpEntityFrameRelayLRStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRStorageType.setStatus("current")
_MplsLdpFrameRelaySessionObjects_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelaySessionObjects = _MplsLdpFrameRelaySessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 2)
)
_MplsLdpFrameRelaySessionTable_Object = MibTable
mplsLdpFrameRelaySessionTable = _MplsLdpFrameRelaySessionTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionTable.setStatus("current")
_MplsLdpFrameRelaySessionEntry_Object = MibTableRow
mplsLdpFrameRelaySessionEntry = _MplsLdpFrameRelaySessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 2, 1, 1)
)
mplsLdpFrameRelaySessionEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpFrameRelaySessionMinDlci"),
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionEntry.setStatus("current")


class _MplsLdpFrameRelaySessionMinDlci_Type(Integer32):
    """Custom type mplsLdpFrameRelaySessionMinDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLdpFrameRelaySessionMinDlci_Type.__name__ = "Integer32"
_MplsLdpFrameRelaySessionMinDlci_Object = MibTableColumn
mplsLdpFrameRelaySessionMinDlci = _MplsLdpFrameRelaySessionMinDlci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 2, 1, 1, 1),
    _MplsLdpFrameRelaySessionMinDlci_Type()
)
mplsLdpFrameRelaySessionMinDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionMinDlci.setStatus("current")
_MplsLdpFrameRelaySessionMaxDlci_Type = Integer32
_MplsLdpFrameRelaySessionMaxDlci_Object = MibTableColumn
mplsLdpFrameRelaySessionMaxDlci = _MplsLdpFrameRelaySessionMaxDlci_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 2, 1, 1, 2),
    _MplsLdpFrameRelaySessionMaxDlci_Type()
)
mplsLdpFrameRelaySessionMaxDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionMaxDlci.setStatus("current")


class _MplsLdpFrameRelaySessionLen_Type(Integer32):
    """Custom type mplsLdpFrameRelaySessionLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenDlciBits", 0),
          ("twentyThreeDlciBits", 2))
    )


_MplsLdpFrameRelaySessionLen_Type.__name__ = "Integer32"
_MplsLdpFrameRelaySessionLen_Object = MibTableColumn
mplsLdpFrameRelaySessionLen = _MplsLdpFrameRelaySessionLen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 6, 2, 1, 1, 3),
    _MplsLdpFrameRelaySessionLen_Type()
)
mplsLdpFrameRelaySessionLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionLen.setStatus("current")
_MplsLdpFrameRelayConformance_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelayConformance = _MplsLdpFrameRelayConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 7)
)
_MplsLdpFrameRelayGroups_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelayGroups = _MplsLdpFrameRelayGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 7, 1)
)
_MplsLdpFrameRelayCompliances_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelayCompliances = _MplsLdpFrameRelayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 7, 2)
)
_MplsLdpGenericObjects_ObjectIdentity = ObjectIdentity
mplsLdpGenericObjects = _MplsLdpGenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 8)
)
_MplsLdpEntityGenericObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityGenericObjects = _MplsLdpEntityGenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 8, 1)
)
_MplsLdpEntityGenericLRTable_Object = MibTable
mplsLdpEntityGenericLRTable = _MplsLdpEntityGenericLRTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLRTable.setStatus("current")
_MplsLdpEntityGenericLREntry_Object = MibTableRow
mplsLdpEntityGenericLREntry = _MplsLdpEntityGenericLREntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 8, 1, 1, 1)
)
mplsLdpEntityGenericLREntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityGenericLRMin"),
    (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityGenericLRMax"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLREntry.setStatus("current")


class _MplsLdpEntityGenericLRMin_Type(Unsigned32):
    """Custom type mplsLdpEntityGenericLRMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MplsLdpEntityGenericLRMin_Type.__name__ = "Unsigned32"
_MplsLdpEntityGenericLRMin_Object = MibTableColumn
mplsLdpEntityGenericLRMin = _MplsLdpEntityGenericLRMin_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 8, 1, 1, 1, 1),
    _MplsLdpEntityGenericLRMin_Type()
)
mplsLdpEntityGenericLRMin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLRMin.setStatus("current")


class _MplsLdpEntityGenericLRMax_Type(Unsigned32):
    """Custom type mplsLdpEntityGenericLRMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MplsLdpEntityGenericLRMax_Type.__name__ = "Unsigned32"
_MplsLdpEntityGenericLRMax_Object = MibTableColumn
mplsLdpEntityGenericLRMax = _MplsLdpEntityGenericLRMax_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 8, 1, 1, 1, 2),
    _MplsLdpEntityGenericLRMax_Type()
)
mplsLdpEntityGenericLRMax.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLRMax.setStatus("current")


class _MplsLdpEntityGenericLabelSpace_Type(Integer32):
    """Custom type mplsLdpEntityGenericLabelSpace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perPlatform", 1),
          ("perInterface", 2))
    )


_MplsLdpEntityGenericLabelSpace_Type.__name__ = "Integer32"
_MplsLdpEntityGenericLabelSpace_Object = MibTableColumn
mplsLdpEntityGenericLabelSpace = _MplsLdpEntityGenericLabelSpace_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 8, 1, 1, 1, 3),
    _MplsLdpEntityGenericLabelSpace_Type()
)
mplsLdpEntityGenericLabelSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLabelSpace.setStatus("current")
_MplsLdpEntityGenericIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityGenericIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityGenericIfIndexOrZero = _MplsLdpEntityGenericIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 8, 1, 1, 1, 4),
    _MplsLdpEntityGenericIfIndexOrZero_Type()
)
mplsLdpEntityGenericIfIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericIfIndexOrZero.setStatus("current")


class _MplsLdpEntityGenericLRStorageType_Type(StorageType):
    """Custom type mplsLdpEntityGenericLRStorageType based on StorageType"""
    defaultValue = 3


_MplsLdpEntityGenericLRStorageType_Type.__name__ = "StorageType"
_MplsLdpEntityGenericLRStorageType_Object = MibTableColumn
mplsLdpEntityGenericLRStorageType = _MplsLdpEntityGenericLRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 8, 1, 1, 1, 5),
    _MplsLdpEntityGenericLRStorageType_Type()
)
mplsLdpEntityGenericLRStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityGenericLRStorageType.setStatus("current")
_MplsLdpGenericConformance_ObjectIdentity = ObjectIdentity
mplsLdpGenericConformance = _MplsLdpGenericConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 9)
)
_MplsLdpGenericGroups_ObjectIdentity = ObjectIdentity
mplsLdpGenericGroups = _MplsLdpGenericGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 9, 1)
)
_MplsLdpGenericCompliances_ObjectIdentity = ObjectIdentity
mplsLdpGenericCompliances = _MplsLdpGenericCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 9, 2)
)
mplsLdpEntityEntry.registerAugmentions(
    ("PRVT-MPLS-LDP-MIB",
     "mplsLdpEntityStatsEntry")
)
mplsLdpEntityStatsEntry.setIndexNames(*mplsLdpEntityEntry.getIndexNames())

# Managed Objects groups

mplsLdpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 3, 1, 1)
)
mplsLdpGeneralGroup.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpLsrId"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpLsrLoopDetectionCapable"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndexNext"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityProtocolVersion"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAdminStatus"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityOperStatus"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityWellKnownTcpDiscoveryPort"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityWellKnownUdpDiscoveryPort"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityMaxPduLength"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityKeepAliveHoldTimer"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityHelloHoldTimer"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityInitSessionThreshold"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityLabelDistMethod"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityLabelRetentionMode"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityPathVectorLimit"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityHopCountLimit"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityTransportAddrKind"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityTargetPeer"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityTargetPeerAddrType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityTargetPeerAddr"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityLabelType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityDiscontinuityTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStorageType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityRowStatus"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityWildcardEntity"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsSessionAttempts"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsSessionRejectedNoHelloErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsSessionRejectedAdErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsSessionRejectedMaxPduErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsSessionRejectedLRErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsBadLdpIdentifierErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsBadPduLengthErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsBadMessageLengthErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsBadTlvLengthErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsMalformedTlvValueErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsKeepAliveTimerExpErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsShutdownReceivedNotifications"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityStatsShutdownSentNotifications"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpPeerLastChange"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpPeerLabelDistMethod"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpPeerPathVectorLimit"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpPeerTransportAddrType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpPeerTransportAddr"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpHelloAdjacencyHoldTimeRemaining"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpHelloAdjacencyHoldTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpHelloAdjacencyType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpHelloAdjacencyConfiguredHoldTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpHelloAdjacencyPeerHoldTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionStateLastChange"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionState"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionRole"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionProtocolVersion"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionKeepAliveHoldTimeRemaining"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionKeepAliveTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionMaxPduLength"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionDiscontinuityTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionConfiguredHoldTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionPeerHoldTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionHoldTimeInUse"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownMesTypeErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownTlvErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionPeerNextHopAddrType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionPeerNextHopAddr"),
        ("PRVT-MPLS-LDP-MIB", "mplsFecLastChange"),
        ("PRVT-MPLS-LDP-MIB", "mplsFecType"),
        ("PRVT-MPLS-LDP-MIB", "mplsFecAddrType"),
        ("PRVT-MPLS-LDP-MIB", "mplsFecAddr"),
        ("PRVT-MPLS-LDP-MIB", "mplsFecAddrPrefixLength"),
        ("PRVT-MPLS-LDP-MIB", "mplsFecStorageType"))
)
if mibBuilder.loadTexts:
    mplsLdpGeneralGroup.setStatus("current")

mplsLdpLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 3, 1, 2)
)
mplsLdpLspGroup.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsInSegmentLdpLspLabelType"),
        ("PRVT-MPLS-LDP-MIB", "mplsInSegmentLdpLspType"),
        ("PRVT-MPLS-LDP-MIB", "mplsOutSegmentLdpLspLabelType"),
        ("PRVT-MPLS-LDP-MIB", "mplsOutSegmentLdpLspType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpLspFecLastChange"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpLspFecStorageType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpLspFecRowStatus"))
)
if mibBuilder.loadTexts:
    mplsLdpLspGroup.setStatus("current")

mplsLdpAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 5, 1, 1)
)
mplsLdpAtmGroup.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmIfIndexOrZero"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmMergeCap"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmLRComponents"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmVcDirectionality"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmLsrConnectivity"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmDefaultControlVpi"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmDefaultControlVci"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmUnlabTrafVpi"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmUnlabTrafVci"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmStorageType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmLRMaxVpi"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmLRMaxVci"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityAtmLRStorageType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionAtmLRUpperBoundVpi"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionAtmLRUpperBoundVci"))
)
if mibBuilder.loadTexts:
    mplsLdpAtmGroup.setStatus("current")

mplsLdpFrameRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 7, 1, 1)
)
mplsLdpFrameRelayGroup.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpEntityFrameRelayIfIndexOrZero"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityFrameRelayMergeCap"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityFrameRelayLRComponents"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityFrameRelayVcDirectionality"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityFrameRelayStorageType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityFrameRelayLRMaxDlci"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityFrameRelayLRLen"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityFrameRelayLRStorageType"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpFrameRelaySessionMaxDlci"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpFrameRelaySessionLen"))
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelayGroup.setStatus("current")

mplsLdpGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 9, 1, 1)
)
mplsLdpGenericGroup.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpEntityGenericLabelSpace"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityGenericIfIndexOrZero"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityGenericLRStorageType"))
)
if mibBuilder.loadTexts:
    mplsLdpGenericGroup.setStatus("current")


# Notification objects

mplsLdpInitSessionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 2, 0, 1)
)
mplsLdpInitSessionThresholdExceeded.setObjects(
    ("PRVT-MPLS-LDP-MIB", "mplsLdpEntityInitSessionThreshold")
)
if mibBuilder.loadTexts:
    mplsLdpInitSessionThresholdExceeded.setStatus(
        "current"
    )

mplsLdpPathVectorLimitMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 2, 0, 2)
)
mplsLdpPathVectorLimitMismatch.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpEntityPathVectorLimit"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpPeerPathVectorLimit"))
)
if mibBuilder.loadTexts:
    mplsLdpPathVectorLimitMismatch.setStatus(
        "current"
    )

mplsLdpSessionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 2, 0, 3)
)
mplsLdpSessionUp.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpSessionState"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionDiscontinuityTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownMesTypeErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownTlvErrors"))
)
if mibBuilder.loadTexts:
    mplsLdpSessionUp.setStatus(
        "current"
    )

mplsLdpSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 2, 0, 4)
)
mplsLdpSessionDown.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpSessionState"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionDiscontinuityTime"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownMesTypeErrors"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownTlvErrors"))
)
if mibBuilder.loadTexts:
    mplsLdpSessionDown.setStatus(
        "current"
    )


# Notifications groups

mplsLdpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 3, 1, 3)
)
mplsLdpNotificationsGroup.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpInitSessionThresholdExceeded"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpPathVectorLimitMismatch"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionUp"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpSessionDown"))
)
if mibBuilder.loadTexts:
    mplsLdpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsLdpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 3, 2, 1)
)
mplsLdpModuleFullCompliance.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpGeneralGroup"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpNotificationsGroup"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpLspGroup"))
)
if mibBuilder.loadTexts:
    mplsLdpModuleFullCompliance.setStatus(
        "current"
    )

mplsLdpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 3, 2, 2)
)
mplsLdpModuleReadOnlyCompliance.setObjects(
      *(("PRVT-MPLS-LDP-MIB", "mplsLdpGeneralGroup"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpNotificationsGroup"),
        ("PRVT-MPLS-LDP-MIB", "mplsLdpLspGroup"))
)
if mibBuilder.loadTexts:
    mplsLdpModuleReadOnlyCompliance.setStatus(
        "current"
    )

mplsLdpAtmModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 5, 2, 1)
)
mplsLdpAtmModuleFullCompliance.setObjects(
    ("PRVT-MPLS-LDP-MIB", "mplsLdpAtmGroup")
)
if mibBuilder.loadTexts:
    mplsLdpAtmModuleFullCompliance.setStatus(
        "current"
    )

mplsLdpAtmModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 5, 2, 2)
)
mplsLdpAtmModuleReadOnlyCompliance.setObjects(
    ("PRVT-MPLS-LDP-MIB", "mplsLdpAtmGroup")
)
if mibBuilder.loadTexts:
    mplsLdpAtmModuleReadOnlyCompliance.setStatus(
        "current"
    )

mplsLdpFrameRelayModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 7, 2, 2)
)
mplsLdpFrameRelayModuleReadOnlyCompliance.setObjects(
    ("PRVT-MPLS-LDP-MIB", "mplsLdpFrameRelayGroup")
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelayModuleReadOnlyCompliance.setStatus(
        "current"
    )

mplsLdpGenericModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 1, 9, 2, 2)
)
mplsLdpGenericModuleReadOnlyCompliance.setObjects(
    ("PRVT-MPLS-LDP-MIB", "mplsLdpGenericGroup")
)
if mibBuilder.loadTexts:
    mplsLdpGenericModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-MPLS-LDP-MIB",
    **{"MplsLabel": MplsLabel,
       "MplsLdpLabelTypes": MplsLdpLabelTypes,
       "mplsLdpStdMIB": mplsLdpStdMIB,
       "mplsLdpObjects": mplsLdpObjects,
       "mplsLdpLsrObjects": mplsLdpLsrObjects,
       "mplsLdpLsrTable": mplsLdpLsrTable,
       "mplsLdpLsrEntry": mplsLdpLsrEntry,
       "mplsLdpLsrId": mplsLdpLsrId,
       "mplsLdpLsrLoopDetectionCapable": mplsLdpLsrLoopDetectionCapable,
       "mplsLdpEntityObjects": mplsLdpEntityObjects,
       "mplsLdpEntityTable": mplsLdpEntityTable,
       "mplsLdpEntityEntry": mplsLdpEntityEntry,
       "mplsLdpEntityLdpId": mplsLdpEntityLdpId,
       "mplsLdpEntityIndex": mplsLdpEntityIndex,
       "mplsLdpEntityProtocolVersion": mplsLdpEntityProtocolVersion,
       "mplsLdpEntityAdminStatus": mplsLdpEntityAdminStatus,
       "mplsLdpEntityOperStatus": mplsLdpEntityOperStatus,
       "mplsLdpEntityWellKnownTcpDiscoveryPort": mplsLdpEntityWellKnownTcpDiscoveryPort,
       "mplsLdpEntityWellKnownUdpDiscoveryPort": mplsLdpEntityWellKnownUdpDiscoveryPort,
       "mplsLdpEntityMaxPduLength": mplsLdpEntityMaxPduLength,
       "mplsLdpEntityKeepAliveHoldTimer": mplsLdpEntityKeepAliveHoldTimer,
       "mplsLdpEntityHelloHoldTimer": mplsLdpEntityHelloHoldTimer,
       "mplsLdpEntityInitSessionThreshold": mplsLdpEntityInitSessionThreshold,
       "mplsLdpEntityLabelDistMethod": mplsLdpEntityLabelDistMethod,
       "mplsLdpEntityLabelRetentionMode": mplsLdpEntityLabelRetentionMode,
       "mplsLdpEntityPathVectorLimit": mplsLdpEntityPathVectorLimit,
       "mplsLdpEntityHopCountLimit": mplsLdpEntityHopCountLimit,
       "mplsLdpEntityTransportAddrKind": mplsLdpEntityTransportAddrKind,
       "mplsLdpEntityTargetPeer": mplsLdpEntityTargetPeer,
       "mplsLdpEntityTargetPeerAddrType": mplsLdpEntityTargetPeerAddrType,
       "mplsLdpEntityTargetPeerAddr": mplsLdpEntityTargetPeerAddr,
       "mplsLdpEntityLabelType": mplsLdpEntityLabelType,
       "mplsLdpEntityDiscontinuityTime": mplsLdpEntityDiscontinuityTime,
       "mplsLdpEntityStorageType": mplsLdpEntityStorageType,
       "mplsLdpEntityWildcardEntity": mplsLdpEntityWildcardEntity,
       "mplsLdpEntityRowStatus": mplsLdpEntityRowStatus,
       "mplsLdpEntityIndexNextTable": mplsLdpEntityIndexNextTable,
       "mplsLdpEntityIndexNextEntry": mplsLdpEntityIndexNextEntry,
       "mplsLdpEntityIndexNext": mplsLdpEntityIndexNext,
       "mplsLdpEntityStatsTable": mplsLdpEntityStatsTable,
       "mplsLdpEntityStatsEntry": mplsLdpEntityStatsEntry,
       "mplsLdpEntityStatsSessionAttempts": mplsLdpEntityStatsSessionAttempts,
       "mplsLdpEntityStatsSessionRejectedNoHelloErrors": mplsLdpEntityStatsSessionRejectedNoHelloErrors,
       "mplsLdpEntityStatsSessionRejectedAdErrors": mplsLdpEntityStatsSessionRejectedAdErrors,
       "mplsLdpEntityStatsSessionRejectedMaxPduErrors": mplsLdpEntityStatsSessionRejectedMaxPduErrors,
       "mplsLdpEntityStatsSessionRejectedLRErrors": mplsLdpEntityStatsSessionRejectedLRErrors,
       "mplsLdpEntityStatsBadLdpIdentifierErrors": mplsLdpEntityStatsBadLdpIdentifierErrors,
       "mplsLdpEntityStatsBadPduLengthErrors": mplsLdpEntityStatsBadPduLengthErrors,
       "mplsLdpEntityStatsBadMessageLengthErrors": mplsLdpEntityStatsBadMessageLengthErrors,
       "mplsLdpEntityStatsBadTlvLengthErrors": mplsLdpEntityStatsBadTlvLengthErrors,
       "mplsLdpEntityStatsMalformedTlvValueErrors": mplsLdpEntityStatsMalformedTlvValueErrors,
       "mplsLdpEntityStatsKeepAliveTimerExpErrors": mplsLdpEntityStatsKeepAliveTimerExpErrors,
       "mplsLdpEntityStatsShutdownReceivedNotifications": mplsLdpEntityStatsShutdownReceivedNotifications,
       "mplsLdpEntityStatsShutdownSentNotifications": mplsLdpEntityStatsShutdownSentNotifications,
       "mplsLdpSessionObjects": mplsLdpSessionObjects,
       "mplsLdpPeerLastChange": mplsLdpPeerLastChange,
       "mplsLdpPeerTable": mplsLdpPeerTable,
       "mplsLdpPeerEntry": mplsLdpPeerEntry,
       "mplsLdpPeerLdpId": mplsLdpPeerLdpId,
       "mplsLdpPeerLabelDistMethod": mplsLdpPeerLabelDistMethod,
       "mplsLdpPeerPathVectorLimit": mplsLdpPeerPathVectorLimit,
       "mplsLdpPeerTransportAddrType": mplsLdpPeerTransportAddrType,
       "mplsLdpPeerTransportAddr": mplsLdpPeerTransportAddr,
       "mplsLdpSessionTable": mplsLdpSessionTable,
       "mplsLdpSessionEntry": mplsLdpSessionEntry,
       "mplsLdpSessionStateLastChange": mplsLdpSessionStateLastChange,
       "mplsLdpSessionState": mplsLdpSessionState,
       "mplsLdpSessionRole": mplsLdpSessionRole,
       "mplsLdpSessionProtocolVersion": mplsLdpSessionProtocolVersion,
       "mplsLdpSessionKeepAliveHoldTimeRemaining": mplsLdpSessionKeepAliveHoldTimeRemaining,
       "mplsLdpSessionKeepAliveTime": mplsLdpSessionKeepAliveTime,
       "mplsLdpSessionMaxPduLength": mplsLdpSessionMaxPduLength,
       "mplsLdpSessionDiscontinuityTime": mplsLdpSessionDiscontinuityTime,
       "mplsLdpSessionConfiguredHoldTime": mplsLdpSessionConfiguredHoldTime,
       "mplsLdpSessionPeerHoldTime": mplsLdpSessionPeerHoldTime,
       "mplsLdpSessionHoldTimeInUse": mplsLdpSessionHoldTimeInUse,
       "mplsLdpSessionStatsTable": mplsLdpSessionStatsTable,
       "mplsLdpSessionStatsEntry": mplsLdpSessionStatsEntry,
       "mplsLdpSessionStatsUnknownMesTypeErrors": mplsLdpSessionStatsUnknownMesTypeErrors,
       "mplsLdpSessionStatsUnknownTlvErrors": mplsLdpSessionStatsUnknownTlvErrors,
       "mplsLdpHelloAdjacencyObjects": mplsLdpHelloAdjacencyObjects,
       "mplsLdpHelloAdjacencyTable": mplsLdpHelloAdjacencyTable,
       "mplsLdpHelloAdjacencyEntry": mplsLdpHelloAdjacencyEntry,
       "mplsLdpHelloAdjacencyIndex": mplsLdpHelloAdjacencyIndex,
       "mplsLdpHelloAdjacencyHoldTimeRemaining": mplsLdpHelloAdjacencyHoldTimeRemaining,
       "mplsLdpHelloAdjacencyHoldTime": mplsLdpHelloAdjacencyHoldTime,
       "mplsLdpHelloAdjacencyType": mplsLdpHelloAdjacencyType,
       "mplsLdpHelloAdjacencyConfiguredHoldTime": mplsLdpHelloAdjacencyConfiguredHoldTime,
       "mplsLdpHelloAdjacencyPeerHoldTime": mplsLdpHelloAdjacencyPeerHoldTime,
       "mplsInSegmentLdpLspTable": mplsInSegmentLdpLspTable,
       "mplsInSegmentLdpLspEntry": mplsInSegmentLdpLspEntry,
       "mplsInSegmentLdpLspIndex": mplsInSegmentLdpLspIndex,
       "mplsInSegmentLdpLspLabelType": mplsInSegmentLdpLspLabelType,
       "mplsInSegmentLdpLspType": mplsInSegmentLdpLspType,
       "mplsOutSegmentLdpLspTable": mplsOutSegmentLdpLspTable,
       "mplsOutSegmentLdpLspEntry": mplsOutSegmentLdpLspEntry,
       "mplsOutSegmentLdpLspIndex": mplsOutSegmentLdpLspIndex,
       "mplsOutSegmentLdpLspLabelType": mplsOutSegmentLdpLspLabelType,
       "mplsOutSegmentLdpLspType": mplsOutSegmentLdpLspType,
       "mplsFecObjects": mplsFecObjects,
       "mplsFecLastChange": mplsFecLastChange,
       "mplsFecTable": mplsFecTable,
       "mplsFecEntry": mplsFecEntry,
       "mplsFecIndex": mplsFecIndex,
       "mplsFecType": mplsFecType,
       "mplsFecAddrPrefixLength": mplsFecAddrPrefixLength,
       "mplsFecAddrType": mplsFecAddrType,
       "mplsFecAddr": mplsFecAddr,
       "mplsFecStorageType": mplsFecStorageType,
       "mplsLdpLspFecLastChange": mplsLdpLspFecLastChange,
       "mplsLdpLspFecTable": mplsLdpLspFecTable,
       "mplsLdpLspFecEntry": mplsLdpLspFecEntry,
       "mplsLdpLspFecSegment": mplsLdpLspFecSegment,
       "mplsLdpLspFecSegmentIndex": mplsLdpLspFecSegmentIndex,
       "mplsLdpLspFecIndex": mplsLdpLspFecIndex,
       "mplsLdpLspFecStorageType": mplsLdpLspFecStorageType,
       "mplsLdpLspFecRowStatus": mplsLdpLspFecRowStatus,
       "mplsLdpSessionPeerAddrTable": mplsLdpSessionPeerAddrTable,
       "mplsLdpSessionPeerAddrEntry": mplsLdpSessionPeerAddrEntry,
       "mplsLdpSessionPeerAddrIndex": mplsLdpSessionPeerAddrIndex,
       "mplsLdpSessionPeerNextHopAddrType": mplsLdpSessionPeerNextHopAddrType,
       "mplsLdpSessionPeerNextHopAddr": mplsLdpSessionPeerNextHopAddr,
       "mplsLdpNotifications": mplsLdpNotifications,
       "mplsLdpInitSessionThresholdExceeded": mplsLdpInitSessionThresholdExceeded,
       "mplsLdpPathVectorLimitMismatch": mplsLdpPathVectorLimitMismatch,
       "mplsLdpSessionUp": mplsLdpSessionUp,
       "mplsLdpSessionDown": mplsLdpSessionDown,
       "mplsLdpConformance": mplsLdpConformance,
       "mplsLdpGroups": mplsLdpGroups,
       "mplsLdpGeneralGroup": mplsLdpGeneralGroup,
       "mplsLdpLspGroup": mplsLdpLspGroup,
       "mplsLdpNotificationsGroup": mplsLdpNotificationsGroup,
       "mplsLdpCompliances": mplsLdpCompliances,
       "mplsLdpModuleFullCompliance": mplsLdpModuleFullCompliance,
       "mplsLdpModuleReadOnlyCompliance": mplsLdpModuleReadOnlyCompliance,
       "mplsLdpAtmObjects": mplsLdpAtmObjects,
       "mplsLdpEntityAtmObjects": mplsLdpEntityAtmObjects,
       "mplsLdpEntityAtmTable": mplsLdpEntityAtmTable,
       "mplsLdpEntityAtmEntry": mplsLdpEntityAtmEntry,
       "mplsLdpEntityAtmIfIndexOrZero": mplsLdpEntityAtmIfIndexOrZero,
       "mplsLdpEntityAtmMergeCap": mplsLdpEntityAtmMergeCap,
       "mplsLdpEntityAtmLRComponents": mplsLdpEntityAtmLRComponents,
       "mplsLdpEntityAtmVcDirectionality": mplsLdpEntityAtmVcDirectionality,
       "mplsLdpEntityAtmLsrConnectivity": mplsLdpEntityAtmLsrConnectivity,
       "mplsLdpEntityAtmDefaultControlVpi": mplsLdpEntityAtmDefaultControlVpi,
       "mplsLdpEntityAtmDefaultControlVci": mplsLdpEntityAtmDefaultControlVci,
       "mplsLdpEntityAtmUnlabTrafVpi": mplsLdpEntityAtmUnlabTrafVpi,
       "mplsLdpEntityAtmUnlabTrafVci": mplsLdpEntityAtmUnlabTrafVci,
       "mplsLdpEntityAtmStorageType": mplsLdpEntityAtmStorageType,
       "mplsLdpEntityAtmLRTable": mplsLdpEntityAtmLRTable,
       "mplsLdpEntityAtmLREntry": mplsLdpEntityAtmLREntry,
       "mplsLdpEntityAtmLRMinVpi": mplsLdpEntityAtmLRMinVpi,
       "mplsLdpEntityAtmLRMinVci": mplsLdpEntityAtmLRMinVci,
       "mplsLdpEntityAtmLRMaxVpi": mplsLdpEntityAtmLRMaxVpi,
       "mplsLdpEntityAtmLRMaxVci": mplsLdpEntityAtmLRMaxVci,
       "mplsLdpEntityAtmLRStorageType": mplsLdpEntityAtmLRStorageType,
       "mplsLdpAtmSessionObjects": mplsLdpAtmSessionObjects,
       "mplsLdpAtmSessionTable": mplsLdpAtmSessionTable,
       "mplsLdpAtmSessionEntry": mplsLdpAtmSessionEntry,
       "mplsLdpSessionAtmLRLowerBoundVpi": mplsLdpSessionAtmLRLowerBoundVpi,
       "mplsLdpSessionAtmLRLowerBoundVci": mplsLdpSessionAtmLRLowerBoundVci,
       "mplsLdpSessionAtmLRUpperBoundVpi": mplsLdpSessionAtmLRUpperBoundVpi,
       "mplsLdpSessionAtmLRUpperBoundVci": mplsLdpSessionAtmLRUpperBoundVci,
       "mplsLdpAtmConformance": mplsLdpAtmConformance,
       "mplsLdpAtmGroups": mplsLdpAtmGroups,
       "mplsLdpAtmGroup": mplsLdpAtmGroup,
       "mplsLdpAtmCompliances": mplsLdpAtmCompliances,
       "mplsLdpAtmModuleFullCompliance": mplsLdpAtmModuleFullCompliance,
       "mplsLdpAtmModuleReadOnlyCompliance": mplsLdpAtmModuleReadOnlyCompliance,
       "mplsLdpFrameRelayObjects": mplsLdpFrameRelayObjects,
       "mplsLdpEntityFrameRelayObjects": mplsLdpEntityFrameRelayObjects,
       "mplsLdpEntityFrameRelayTable": mplsLdpEntityFrameRelayTable,
       "mplsLdpEntityFrameRelayEntry": mplsLdpEntityFrameRelayEntry,
       "mplsLdpEntityFrameRelayIfIndexOrZero": mplsLdpEntityFrameRelayIfIndexOrZero,
       "mplsLdpEntityFrameRelayMergeCap": mplsLdpEntityFrameRelayMergeCap,
       "mplsLdpEntityFrameRelayLRComponents": mplsLdpEntityFrameRelayLRComponents,
       "mplsLdpEntityFrameRelayVcDirectionality": mplsLdpEntityFrameRelayVcDirectionality,
       "mplsLdpEntityFrameRelayStorageType": mplsLdpEntityFrameRelayStorageType,
       "mplsLdpEntityFrameRelayLRTable": mplsLdpEntityFrameRelayLRTable,
       "mplsLdpEntityFrameRelayLREntry": mplsLdpEntityFrameRelayLREntry,
       "mplsLdpEntityFrameRelayLRMinDlci": mplsLdpEntityFrameRelayLRMinDlci,
       "mplsLdpEntityFrameRelayLRMaxDlci": mplsLdpEntityFrameRelayLRMaxDlci,
       "mplsLdpEntityFrameRelayLRLen": mplsLdpEntityFrameRelayLRLen,
       "mplsLdpEntityFrameRelayLRStorageType": mplsLdpEntityFrameRelayLRStorageType,
       "mplsLdpFrameRelaySessionObjects": mplsLdpFrameRelaySessionObjects,
       "mplsLdpFrameRelaySessionTable": mplsLdpFrameRelaySessionTable,
       "mplsLdpFrameRelaySessionEntry": mplsLdpFrameRelaySessionEntry,
       "mplsLdpFrameRelaySessionMinDlci": mplsLdpFrameRelaySessionMinDlci,
       "mplsLdpFrameRelaySessionMaxDlci": mplsLdpFrameRelaySessionMaxDlci,
       "mplsLdpFrameRelaySessionLen": mplsLdpFrameRelaySessionLen,
       "mplsLdpFrameRelayConformance": mplsLdpFrameRelayConformance,
       "mplsLdpFrameRelayGroups": mplsLdpFrameRelayGroups,
       "mplsLdpFrameRelayGroup": mplsLdpFrameRelayGroup,
       "mplsLdpFrameRelayCompliances": mplsLdpFrameRelayCompliances,
       "mplsLdpFrameRelayModuleReadOnlyCompliance": mplsLdpFrameRelayModuleReadOnlyCompliance,
       "mplsLdpGenericObjects": mplsLdpGenericObjects,
       "mplsLdpEntityGenericObjects": mplsLdpEntityGenericObjects,
       "mplsLdpEntityGenericLRTable": mplsLdpEntityGenericLRTable,
       "mplsLdpEntityGenericLREntry": mplsLdpEntityGenericLREntry,
       "mplsLdpEntityGenericLRMin": mplsLdpEntityGenericLRMin,
       "mplsLdpEntityGenericLRMax": mplsLdpEntityGenericLRMax,
       "mplsLdpEntityGenericLabelSpace": mplsLdpEntityGenericLabelSpace,
       "mplsLdpEntityGenericIfIndexOrZero": mplsLdpEntityGenericIfIndexOrZero,
       "mplsLdpEntityGenericLRStorageType": mplsLdpEntityGenericLRStorageType,
       "mplsLdpGenericConformance": mplsLdpGenericConformance,
       "mplsLdpGenericGroups": mplsLdpGenericGroups,
       "mplsLdpGenericGroup": mplsLdpGenericGroup,
       "mplsLdpGenericCompliances": mplsLdpGenericCompliances,
       "mplsLdpGenericModuleReadOnlyCompliance": mplsLdpGenericModuleReadOnlyCompliance}
)
