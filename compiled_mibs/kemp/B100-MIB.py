# SNMP MIB module (B100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\kemp\B100-MIB

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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(one4net,) = mibBuilder.importSymbols(
    "ONE4NET-MIB",
    "one4net")

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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

b100 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12196, 13)
)
if mibBuilder.loadTexts:
    b100.setRevisions(
        ("2021-06-25 09:09",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Version_Type(OctetString):
    """Custom type version based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Version_Type.__name__ = "OctetString"
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")


class _NumServices_Type(Integer32):
    """Custom type numServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NumServices_Type.__name__ = "Integer32"
_NumServices_Object = MibScalar
numServices = _NumServices_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 2),
    _NumServices_Type()
)
numServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numServices.setStatus("current")
_HashTableSize_Type = Integer32
_HashTableSize_Object = MibScalar
hashTableSize = _HashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 3),
    _HashTableSize_Type()
)
hashTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashTableSize.setStatus("current")
_TcpTimeOut_Type = TimeInterval
_TcpTimeOut_Object = MibScalar
tcpTimeOut = _TcpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 4),
    _TcpTimeOut_Type()
)
tcpTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTimeOut.setStatus("current")
_TcpFinTimeOut_Type = TimeInterval
_TcpFinTimeOut_Object = MibScalar
tcpFinTimeOut = _TcpFinTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 5),
    _TcpFinTimeOut_Type()
)
tcpFinTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpFinTimeOut.setStatus("current")
_UdpTimeOut_Type = TimeInterval
_UdpTimeOut_Object = MibScalar
udpTimeOut = _UdpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 6),
    _UdpTimeOut_Type()
)
udpTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTimeOut.setStatus("current")


class _DaemonState_Type(Integer32):
    """Custom type daemonState based on Integer32"""
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
          ("master", 1),
          ("backup", 2))
    )


_DaemonState_Type.__name__ = "Integer32"
_DaemonState_Object = MibScalar
daemonState = _DaemonState_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 7),
    _DaemonState_Type()
)
daemonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daemonState.setStatus("current")


class _McastInterface_Type(OctetString):
    """Custom type mcastInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_McastInterface_Type.__name__ = "OctetString"
_McastInterface_Object = MibScalar
mcastInterface = _McastInterface_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 8),
    _McastInterface_Type()
)
mcastInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastInterface.setStatus("current")


class _HaState_Type(Integer32):
    """Custom type haState based on Integer32"""
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
          ("master", 1),
          ("standby", 2),
          ("passive", 3))
    )


_HaState_Type.__name__ = "Integer32"
_HaState_Object = MibScalar
haState = _HaState_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 9),
    _HaState_Type()
)
haState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haState.setStatus("current")


class _PatchVersion_Type(OctetString):
    """Custom type patchVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PatchVersion_Type.__name__ = "OctetString"
_PatchVersion_Object = MibScalar
patchVersion = _PatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 10),
    _PatchVersion_Type()
)
patchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    patchVersion.setStatus("current")
_TotalTps_Type = Integer32
_TotalTps_Object = MibScalar
totalTps = _TotalTps_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 11),
    _TotalTps_Type()
)
totalTps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalTps.setStatus("current")
_SslTps_Type = Integer32
_SslTps_Object = MibScalar
sslTps = _SslTps_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 12),
    _SslTps_Type()
)
sslTps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTps.setStatus("current")
_B100VSTable_Object = MibTable
b100VSTable = _B100VSTable_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1)
)
if mibBuilder.loadTexts:
    b100VSTable.setStatus("current")
_VsEntry_Object = MibTableRow
vsEntry = _VsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1)
)
vsEntry.setIndexNames(
    (0, "B100-MIB", "vSIdx"),
)
if mibBuilder.loadTexts:
    vsEntry.setStatus("current")


class _VSIdx_Type(Integer32):
    """Custom type vSIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VSIdx_Type.__name__ = "Integer32"
_VSIdx_Object = MibTableColumn
vSIdx = _VSIdx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 1),
    _VSIdx_Type()
)
vSIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSIdx.setStatus("current")
_VSIp_Type = InetAddress
_VSIp_Object = MibTableColumn
vSIp = _VSIp_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 2),
    _VSIp_Type()
)
vSIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSIp.setStatus("current")
_VSPort_Type = InetPortNumber
_VSPort_Object = MibTableColumn
vSPort = _VSPort_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 3),
    _VSPort_Type()
)
vSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSPort.setStatus("current")
_VSAddrtype_Type = InetAddressType
_VSAddrtype_Object = MibTableColumn
vSAddrtype = _VSAddrtype_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 4),
    _VSAddrtype_Type()
)
vSAddrtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSAddrtype.setStatus("current")


class _VSProtocol_Type(Integer32):
    """Custom type vSProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_VSProtocol_Type.__name__ = "Integer32"
_VSProtocol_Object = MibTableColumn
vSProtocol = _VSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 5),
    _VSProtocol_Type()
)
vSProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSProtocol.setStatus("current")


class _VSSchedulingMethod_Type(OctetString):
    """Custom type vSSchedulingMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VSSchedulingMethod_Type.__name__ = "OctetString"
_VSSchedulingMethod_Object = MibTableColumn
vSSchedulingMethod = _VSSchedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 6),
    _VSSchedulingMethod_Type()
)
vSSchedulingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSSchedulingMethod.setStatus("current")
_VSPersistenceTimeout_Type = TimeInterval
_VSPersistenceTimeout_Object = MibTableColumn
vSPersistenceTimeout = _VSPersistenceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 7),
    _VSPersistenceTimeout_Type()
)
vSPersistenceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSPersistenceTimeout.setStatus("current")


class _VSCheckerType_Type(OctetString):
    """Custom type vSCheckerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VSCheckerType_Type.__name__ = "OctetString"
_VSCheckerType_Object = MibTableColumn
vSCheckerType = _VSCheckerType_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 8),
    _VSCheckerType_Type()
)
vSCheckerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCheckerType.setStatus("current")


class _VSAdaptiveMethod_Type(OctetString):
    """Custom type vSAdaptiveMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VSAdaptiveMethod_Type.__name__ = "OctetString"
_VSAdaptiveMethod_Object = MibTableColumn
vSAdaptiveMethod = _VSAdaptiveMethod_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 9),
    _VSAdaptiveMethod_Type()
)
vSAdaptiveMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSAdaptiveMethod.setStatus("current")


class _VSNumDests_Type(Integer32):
    """Custom type vSNumDests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VSNumDests_Type.__name__ = "Integer32"
_VSNumDests_Object = MibTableColumn
vSNumDests = _VSNumDests_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 10),
    _VSNumDests_Type()
)
vSNumDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSNumDests.setStatus("current")


class _VSL7persist_Type(OctetString):
    """Custom type vSL7persist based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VSL7persist_Type.__name__ = "OctetString"
_VSL7persist_Object = MibTableColumn
vSL7persist = _VSL7persist_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 11),
    _VSL7persist_Type()
)
vSL7persist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSL7persist.setStatus("current")


class _VSL7cookieId_Type(OctetString):
    """Custom type vSL7cookieId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VSL7cookieId_Type.__name__ = "OctetString"
_VSL7cookieId_Object = MibTableColumn
vSL7cookieId = _VSL7cookieId_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 12),
    _VSL7cookieId_Type()
)
vSL7cookieId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSL7cookieId.setStatus("current")


class _VSName_Type(OctetString):
    """Custom type vSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VSName_Type.__name__ = "OctetString"
_VSName_Object = MibTableColumn
vSName = _VSName_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 13),
    _VSName_Type()
)
vSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSName.setStatus("current")


class _VSState_Type(Integer32):
    """Custom type vSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2),
          ("disabled", 4),
          ("sorry", 5),
          ("redirect", 6),
          ("errormsg", 7),
          ("securityDown", 8))
    )


_VSState_Type.__name__ = "Integer32"
_VSState_Object = MibTableColumn
vSState = _VSState_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 14),
    _VSState_Type()
)
vSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSState.setStatus("current")
_VSFollow_Type = InetPortNumber
_VSFollow_Object = MibTableColumn
vSFollow = _VSFollow_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 15),
    _VSFollow_Type()
)
vSFollow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFollow.setStatus("current")
_VSConns_Type = Counter32
_VSConns_Object = MibTableColumn
vSConns = _VSConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 16),
    _VSConns_Type()
)
vSConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSConns.setStatus("current")
_VSInPkts_Type = Counter32
_VSInPkts_Object = MibTableColumn
vSInPkts = _VSInPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 17),
    _VSInPkts_Type()
)
vSInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSInPkts.setStatus("current")
_VSOutPkts_Type = Counter32
_VSOutPkts_Object = MibTableColumn
vSOutPkts = _VSOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 18),
    _VSOutPkts_Type()
)
vSOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSOutPkts.setStatus("current")
_VSInBytes_Type = Counter64
_VSInBytes_Object = MibTableColumn
vSInBytes = _VSInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 19),
    _VSInBytes_Type()
)
vSInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSInBytes.setStatus("current")
_VSOutBytes_Type = Counter64
_VSOutBytes_Object = MibTableColumn
vSOutBytes = _VSOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 20),
    _VSOutBytes_Type()
)
vSOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSOutBytes.setStatus("current")
_VSActiveConns_Type = Gauge32
_VSActiveConns_Object = MibTableColumn
vSActiveConns = _VSActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 21),
    _VSActiveConns_Type()
)
vSActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSActiveConns.setStatus("current")
_VSCurrentAvgRequest_Type = Integer32
_VSCurrentAvgRequest_Object = MibTableColumn
vSCurrentAvgRequest = _VSCurrentAvgRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 22),
    _VSCurrentAvgRequest_Type()
)
vSCurrentAvgRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCurrentAvgRequest.setStatus("current")
_VSCurrentAvgResponse_Type = Integer32
_VSCurrentAvgResponse_Object = MibTableColumn
vSCurrentAvgResponse = _VSCurrentAvgResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 23),
    _VSCurrentAvgResponse_Type()
)
vSCurrentAvgResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCurrentAvgResponse.setStatus("current")
_VSCurrentMaxRequest_Type = Integer32
_VSCurrentMaxRequest_Object = MibTableColumn
vSCurrentMaxRequest = _VSCurrentMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 24),
    _VSCurrentMaxRequest_Type()
)
vSCurrentMaxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCurrentMaxRequest.setStatus("current")
_VSCurrentMaxResponse_Type = Integer32
_VSCurrentMaxResponse_Object = MibTableColumn
vSCurrentMaxResponse = _VSCurrentMaxResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 25),
    _VSCurrentMaxResponse_Type()
)
vSCurrentMaxResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCurrentMaxResponse.setStatus("current")
_VSCurrentMinRequest_Type = Integer32
_VSCurrentMinRequest_Object = MibTableColumn
vSCurrentMinRequest = _VSCurrentMinRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 26),
    _VSCurrentMinRequest_Type()
)
vSCurrentMinRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCurrentMinRequest.setStatus("current")
_VSCurrentMinResponse_Type = Integer32
_VSCurrentMinResponse_Object = MibTableColumn
vSCurrentMinResponse = _VSCurrentMinResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 27),
    _VSCurrentMinResponse_Type()
)
vSCurrentMinResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCurrentMinResponse.setStatus("current")
_VSLongTermAvgRequest_Type = Integer32
_VSLongTermAvgRequest_Object = MibTableColumn
vSLongTermAvgRequest = _VSLongTermAvgRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 28),
    _VSLongTermAvgRequest_Type()
)
vSLongTermAvgRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSLongTermAvgRequest.setStatus("current")
_VSLongTermAvgResponse_Type = Integer32
_VSLongTermAvgResponse_Object = MibTableColumn
vSLongTermAvgResponse = _VSLongTermAvgResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 29),
    _VSLongTermAvgResponse_Type()
)
vSLongTermAvgResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSLongTermAvgResponse.setStatus("current")
_VSLongTermMaxRequest_Type = Integer32
_VSLongTermMaxRequest_Object = MibTableColumn
vSLongTermMaxRequest = _VSLongTermMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 30),
    _VSLongTermMaxRequest_Type()
)
vSLongTermMaxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSLongTermMaxRequest.setStatus("current")
_VSLongTermMaxResponse_Type = Integer32
_VSLongTermMaxResponse_Object = MibTableColumn
vSLongTermMaxResponse = _VSLongTermMaxResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 31),
    _VSLongTermMaxResponse_Type()
)
vSLongTermMaxResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSLongTermMaxResponse.setStatus("current")
_VSLongTermMinRequest_Type = Integer32
_VSLongTermMinRequest_Object = MibTableColumn
vSLongTermMinRequest = _VSLongTermMinRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 32),
    _VSLongTermMinRequest_Type()
)
vSLongTermMinRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSLongTermMinRequest.setStatus("current")
_VSLongTermMinResponse_Type = Integer32
_VSLongTermMinResponse_Object = MibTableColumn
vSLongTermMinResponse = _VSLongTermMinResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 33),
    _VSLongTermMinResponse_Type()
)
vSLongTermMinResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSLongTermMinResponse.setStatus("current")
_VSCurrentAvgRTTTimes_Type = Integer32
_VSCurrentAvgRTTTimes_Object = MibTableColumn
vSCurrentAvgRTTTimes = _VSCurrentAvgRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 34),
    _VSCurrentAvgRTTTimes_Type()
)
vSCurrentAvgRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCurrentAvgRTTTimes.setStatus("current")
_VSCurrentMaxRTTTimes_Type = Integer32
_VSCurrentMaxRTTTimes_Object = MibTableColumn
vSCurrentMaxRTTTimes = _VSCurrentMaxRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 35),
    _VSCurrentMaxRTTTimes_Type()
)
vSCurrentMaxRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCurrentMaxRTTTimes.setStatus("current")
_VSCurrentMinRTTTimes_Type = Integer32
_VSCurrentMinRTTTimes_Object = MibTableColumn
vSCurrentMinRTTTimes = _VSCurrentMinRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 36),
    _VSCurrentMinRTTTimes_Type()
)
vSCurrentMinRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSCurrentMinRTTTimes.setStatus("current")
_VSLongTermAvgRTTTimes_Type = Integer32
_VSLongTermAvgRTTTimes_Object = MibTableColumn
vSLongTermAvgRTTTimes = _VSLongTermAvgRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 37),
    _VSLongTermAvgRTTTimes_Type()
)
vSLongTermAvgRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSLongTermAvgRTTTimes.setStatus("current")
_VSLongTermMaxRTTTimes_Type = Integer32
_VSLongTermMaxRTTTimes_Object = MibTableColumn
vSLongTermMaxRTTTimes = _VSLongTermMaxRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 38),
    _VSLongTermMaxRTTTimes_Type()
)
vSLongTermMaxRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSLongTermMaxRTTTimes.setStatus("current")
_VSLongTermMinRTTTimes_Type = Integer32
_VSLongTermMinRTTTimes_Object = MibTableColumn
vSLongTermMinRTTTimes = _VSLongTermMinRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 39),
    _VSLongTermMinRTTTimes_Type()
)
vSLongTermMinRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSLongTermMinRTTTimes.setStatus("current")
_B100RSTable_Object = MibTable
b100RSTable = _B100RSTable_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2)
)
if mibBuilder.loadTexts:
    b100RSTable.setStatus("current")
_RsEntry_Object = MibTableRow
rsEntry = _RsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1)
)
rsEntry.setIndexNames(
    (0, "B100-MIB", "rSIdx"),
)
if mibBuilder.loadTexts:
    rsEntry.setStatus("current")


class _RSVsIdx_Type(Integer32):
    """Custom type rSVsIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RSVsIdx_Type.__name__ = "Integer32"
_RSVsIdx_Object = MibTableColumn
rSVsIdx = _RSVsIdx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 1),
    _RSVsIdx_Type()
)
rSVsIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSVsIdx.setStatus("current")
_RSIp_Type = InetAddress
_RSIp_Object = MibTableColumn
rSIp = _RSIp_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 2),
    _RSIp_Type()
)
rSIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSIp.setStatus("current")
_RSPort_Type = InetPortNumber
_RSPort_Object = MibTableColumn
rSPort = _RSPort_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 3),
    _RSPort_Type()
)
rSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSPort.setStatus("current")
_RSAddrType_Type = InetAddressType
_RSAddrType_Object = MibTableColumn
rSAddrType = _RSAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 4),
    _RSAddrType_Type()
)
rSAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSAddrType.setStatus("current")


class _RSIdx_Type(Integer32):
    """Custom type rSIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_RSIdx_Type.__name__ = "Integer32"
_RSIdx_Object = MibTableColumn
rSIdx = _RSIdx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 5),
    _RSIdx_Type()
)
rSIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSIdx.setStatus("current")


class _RSForwardingMethod_Type(OctetString):
    """Custom type rSForwardingMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RSForwardingMethod_Type.__name__ = "OctetString"
_RSForwardingMethod_Object = MibTableColumn
rSForwardingMethod = _RSForwardingMethod_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 6),
    _RSForwardingMethod_Type()
)
rSForwardingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSForwardingMethod.setStatus("current")


class _RSWeight_Type(Integer32):
    """Custom type rSWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RSWeight_Type.__name__ = "Integer32"
_RSWeight_Object = MibTableColumn
rSWeight = _RSWeight_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 7),
    _RSWeight_Type()
)
rSWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSWeight.setStatus("current")


class _RSState_Type(Integer32):
    """Custom type rSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2),
          ("disabled", 4))
    )


_RSState_Type.__name__ = "Integer32"
_RSState_Object = MibTableColumn
rSState = _RSState_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 8),
    _RSState_Type()
)
rSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSState.setStatus("current")
_RSConns_Type = Counter32
_RSConns_Object = MibTableColumn
rSConns = _RSConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 12),
    _RSConns_Type()
)
rSConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSConns.setStatus("current")
_RSInPkts_Type = Counter32
_RSInPkts_Object = MibTableColumn
rSInPkts = _RSInPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 13),
    _RSInPkts_Type()
)
rSInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSInPkts.setStatus("current")
_RSOutPkts_Type = Counter32
_RSOutPkts_Object = MibTableColumn
rSOutPkts = _RSOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 14),
    _RSOutPkts_Type()
)
rSOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSOutPkts.setStatus("current")
_RSInBytes_Type = Counter64
_RSInBytes_Object = MibTableColumn
rSInBytes = _RSInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 15),
    _RSInBytes_Type()
)
rSInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSInBytes.setStatus("current")
_RSOutBytes_Type = Counter64
_RSOutBytes_Object = MibTableColumn
rSOutBytes = _RSOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 16),
    _RSOutBytes_Type()
)
rSOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSOutBytes.setStatus("current")
_RSActiveConns_Type = Gauge32
_RSActiveConns_Object = MibTableColumn
rSActiveConns = _RSActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 17),
    _RSActiveConns_Type()
)
rSActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSActiveConns.setStatus("current")
_RSInactiveConns_Type = Counter32
_RSInactiveConns_Object = MibTableColumn
rSInactiveConns = _RSInactiveConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 18),
    _RSInactiveConns_Type()
)
rSInactiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSInactiveConns.setStatus("current")
_RSCurrentAvgRequest_Type = Integer32
_RSCurrentAvgRequest_Object = MibTableColumn
rSCurrentAvgRequest = _RSCurrentAvgRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 19),
    _RSCurrentAvgRequest_Type()
)
rSCurrentAvgRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSCurrentAvgRequest.setStatus("current")
_RSCurrentAvgResponse_Type = Integer32
_RSCurrentAvgResponse_Object = MibTableColumn
rSCurrentAvgResponse = _RSCurrentAvgResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 20),
    _RSCurrentAvgResponse_Type()
)
rSCurrentAvgResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSCurrentAvgResponse.setStatus("current")
_RSCurrentMaxRequest_Type = Integer32
_RSCurrentMaxRequest_Object = MibTableColumn
rSCurrentMaxRequest = _RSCurrentMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 21),
    _RSCurrentMaxRequest_Type()
)
rSCurrentMaxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSCurrentMaxRequest.setStatus("current")
_RSCurrentMaxResponse_Type = Integer32
_RSCurrentMaxResponse_Object = MibTableColumn
rSCurrentMaxResponse = _RSCurrentMaxResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 22),
    _RSCurrentMaxResponse_Type()
)
rSCurrentMaxResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSCurrentMaxResponse.setStatus("current")
_RSCurrentMinRequest_Type = Integer32
_RSCurrentMinRequest_Object = MibTableColumn
rSCurrentMinRequest = _RSCurrentMinRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 23),
    _RSCurrentMinRequest_Type()
)
rSCurrentMinRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSCurrentMinRequest.setStatus("current")
_RSCurrentMinResponse_Type = Integer32
_RSCurrentMinResponse_Object = MibTableColumn
rSCurrentMinResponse = _RSCurrentMinResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 24),
    _RSCurrentMinResponse_Type()
)
rSCurrentMinResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSCurrentMinResponse.setStatus("current")
_RSLongTermAvgRequest_Type = Integer32
_RSLongTermAvgRequest_Object = MibTableColumn
rSLongTermAvgRequest = _RSLongTermAvgRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 25),
    _RSLongTermAvgRequest_Type()
)
rSLongTermAvgRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSLongTermAvgRequest.setStatus("current")
_RSLongTermAvgResponse_Type = Integer32
_RSLongTermAvgResponse_Object = MibTableColumn
rSLongTermAvgResponse = _RSLongTermAvgResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 26),
    _RSLongTermAvgResponse_Type()
)
rSLongTermAvgResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSLongTermAvgResponse.setStatus("current")
_RSLongTermMaxRequest_Type = Integer32
_RSLongTermMaxRequest_Object = MibTableColumn
rSLongTermMaxRequest = _RSLongTermMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 27),
    _RSLongTermMaxRequest_Type()
)
rSLongTermMaxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSLongTermMaxRequest.setStatus("current")
_RSLongTermMaxResponse_Type = Integer32
_RSLongTermMaxResponse_Object = MibTableColumn
rSLongTermMaxResponse = _RSLongTermMaxResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 28),
    _RSLongTermMaxResponse_Type()
)
rSLongTermMaxResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSLongTermMaxResponse.setStatus("current")
_RSLongTermMinRequest_Type = Integer32
_RSLongTermMinRequest_Object = MibTableColumn
rSLongTermMinRequest = _RSLongTermMinRequest_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 29),
    _RSLongTermMinRequest_Type()
)
rSLongTermMinRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSLongTermMinRequest.setStatus("current")
_RSLongTermMinResponse_Type = Integer32
_RSLongTermMinResponse_Object = MibTableColumn
rSLongTermMinResponse = _RSLongTermMinResponse_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 30),
    _RSLongTermMinResponse_Type()
)
rSLongTermMinResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSLongTermMinResponse.setStatus("current")
_RSCurrentAvgRTTTimes_Type = Integer32
_RSCurrentAvgRTTTimes_Object = MibTableColumn
rSCurrentAvgRTTTimes = _RSCurrentAvgRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 31),
    _RSCurrentAvgRTTTimes_Type()
)
rSCurrentAvgRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSCurrentAvgRTTTimes.setStatus("current")
_RSCurrentMaxRTTTimes_Type = Integer32
_RSCurrentMaxRTTTimes_Object = MibTableColumn
rSCurrentMaxRTTTimes = _RSCurrentMaxRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 32),
    _RSCurrentMaxRTTTimes_Type()
)
rSCurrentMaxRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSCurrentMaxRTTTimes.setStatus("current")
_RSCurrentMinRTTTimes_Type = Integer32
_RSCurrentMinRTTTimes_Object = MibTableColumn
rSCurrentMinRTTTimes = _RSCurrentMinRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 33),
    _RSCurrentMinRTTTimes_Type()
)
rSCurrentMinRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSCurrentMinRTTTimes.setStatus("current")
_RSLongTermAvgRTTTimes_Type = Integer32
_RSLongTermAvgRTTTimes_Object = MibTableColumn
rSLongTermAvgRTTTimes = _RSLongTermAvgRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 34),
    _RSLongTermAvgRTTTimes_Type()
)
rSLongTermAvgRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSLongTermAvgRTTTimes.setStatus("current")
_RSLongTermMaxRTTTimes_Type = Integer32
_RSLongTermMaxRTTTimes_Object = MibTableColumn
rSLongTermMaxRTTTimes = _RSLongTermMaxRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 35),
    _RSLongTermMaxRTTTimes_Type()
)
rSLongTermMaxRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSLongTermMaxRTTTimes.setStatus("current")
_RSLongTermMinRTTTimes_Type = Integer32
_RSLongTermMinRTTTimes_Object = MibTableColumn
rSLongTermMinRTTTimes = _RSLongTermMinRTTTimes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 36),
    _RSLongTermMinRTTTimes_Type()
)
rSLongTermMinRTTTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSLongTermMinRTTTimes.setStatus("current")
_B100NotificationsPrefix_ObjectIdentity = ObjectIdentity
b100NotificationsPrefix = _B100NotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3)
)
_B100Notifications_ObjectIdentity = ObjectIdentity
b100Notifications = _B100Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1)
)


class _AdaptiveInterval_Type(Integer32):
    """Custom type adaptiveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdaptiveInterval_Type.__name__ = "Integer32"
_AdaptiveInterval_Object = MibScalar
adaptiveInterval = _AdaptiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 13),
    _AdaptiveInterval_Type()
)
adaptiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptiveInterval.setStatus("current")


class _AdaptiveUrl_Type(OctetString):
    """Custom type adaptiveUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_AdaptiveUrl_Type.__name__ = "OctetString"
_AdaptiveUrl_Object = MibScalar
adaptiveUrl = _AdaptiveUrl_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 14),
    _AdaptiveUrl_Type()
)
adaptiveUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptiveUrl.setStatus("current")


class _AdaptiveCtrlMinP_Type(Integer32):
    """Custom type adaptiveCtrlMinP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdaptiveCtrlMinP_Type.__name__ = "Integer32"
_AdaptiveCtrlMinP_Object = MibScalar
adaptiveCtrlMinP = _AdaptiveCtrlMinP_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 15),
    _AdaptiveCtrlMinP_Type()
)
adaptiveCtrlMinP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptiveCtrlMinP.setStatus("current")


class _AdaptiveMinWeight_Type(Integer32):
    """Custom type adaptiveMinWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdaptiveMinWeight_Type.__name__ = "Integer32"
_AdaptiveMinWeight_Object = MibScalar
adaptiveMinWeight = _AdaptiveMinWeight_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 16),
    _AdaptiveMinWeight_Type()
)
adaptiveMinWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptiveMinWeight.setStatus("current")

# Managed Objects groups


# Notification objects

vSstateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 1)
)
vSstateChange.setObjects(
      *(("B100-MIB", "vSState"),
        ("B100-MIB", "vSIp"),
        ("B100-MIB", "vSPort"),
        ("B100-MIB", "vSAddrtype"),
        ("B100-MIB", "vSName"),
        ("B100-MIB", "vSIdx"))
)
if mibBuilder.loadTexts:
    vSstateChange.setStatus(
        "current"
    )

rSstateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 2)
)
rSstateChange.setObjects(
      *(("B100-MIB", "rSState"),
        ("B100-MIB", "rSIp"),
        ("B100-MIB", "rSPort"),
        ("B100-MIB", "rSAddrType"),
        ("B100-MIB", "rSIdx"),
        ("B100-MIB", "vSIp"),
        ("B100-MIB", "vSPort"),
        ("B100-MIB", "vSAddrtype"),
        ("B100-MIB", "vSName"),
        ("B100-MIB", "vSIdx"))
)
if mibBuilder.loadTexts:
    rSstateChange.setStatus(
        "current"
    )

hAstateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 3)
)
hAstateChange.setObjects(
    ("B100-MIB", "haState")
)
if mibBuilder.loadTexts:
    hAstateChange.setStatus(
        "current"
    )

licenseExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 4)
)
if mibBuilder.loadTexts:
    licenseExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "B100-MIB",
    **{"b100": b100,
       "version": version,
       "numServices": numServices,
       "hashTableSize": hashTableSize,
       "tcpTimeOut": tcpTimeOut,
       "tcpFinTimeOut": tcpFinTimeOut,
       "udpTimeOut": udpTimeOut,
       "daemonState": daemonState,
       "mcastInterface": mcastInterface,
       "haState": haState,
       "patchVersion": patchVersion,
       "totalTps": totalTps,
       "sslTps": sslTps,
       "b100VSTable": b100VSTable,
       "vsEntry": vsEntry,
       "vSIdx": vSIdx,
       "vSIp": vSIp,
       "vSPort": vSPort,
       "vSAddrtype": vSAddrtype,
       "vSProtocol": vSProtocol,
       "vSSchedulingMethod": vSSchedulingMethod,
       "vSPersistenceTimeout": vSPersistenceTimeout,
       "vSCheckerType": vSCheckerType,
       "vSAdaptiveMethod": vSAdaptiveMethod,
       "vSNumDests": vSNumDests,
       "vSL7persist": vSL7persist,
       "vSL7cookieId": vSL7cookieId,
       "vSName": vSName,
       "vSState": vSState,
       "vSFollow": vSFollow,
       "vSConns": vSConns,
       "vSInPkts": vSInPkts,
       "vSOutPkts": vSOutPkts,
       "vSInBytes": vSInBytes,
       "vSOutBytes": vSOutBytes,
       "vSActiveConns": vSActiveConns,
       "vSCurrentAvgRequest": vSCurrentAvgRequest,
       "vSCurrentAvgResponse": vSCurrentAvgResponse,
       "vSCurrentMaxRequest": vSCurrentMaxRequest,
       "vSCurrentMaxResponse": vSCurrentMaxResponse,
       "vSCurrentMinRequest": vSCurrentMinRequest,
       "vSCurrentMinResponse": vSCurrentMinResponse,
       "vSLongTermAvgRequest": vSLongTermAvgRequest,
       "vSLongTermAvgResponse": vSLongTermAvgResponse,
       "vSLongTermMaxRequest": vSLongTermMaxRequest,
       "vSLongTermMaxResponse": vSLongTermMaxResponse,
       "vSLongTermMinRequest": vSLongTermMinRequest,
       "vSLongTermMinResponse": vSLongTermMinResponse,
       "vSCurrentAvgRTTTimes": vSCurrentAvgRTTTimes,
       "vSCurrentMaxRTTTimes": vSCurrentMaxRTTTimes,
       "vSCurrentMinRTTTimes": vSCurrentMinRTTTimes,
       "vSLongTermAvgRTTTimes": vSLongTermAvgRTTTimes,
       "vSLongTermMaxRTTTimes": vSLongTermMaxRTTTimes,
       "vSLongTermMinRTTTimes": vSLongTermMinRTTTimes,
       "b100RSTable": b100RSTable,
       "rsEntry": rsEntry,
       "rSVsIdx": rSVsIdx,
       "rSIp": rSIp,
       "rSPort": rSPort,
       "rSAddrType": rSAddrType,
       "rSIdx": rSIdx,
       "rSForwardingMethod": rSForwardingMethod,
       "rSWeight": rSWeight,
       "rSState": rSState,
       "rSConns": rSConns,
       "rSInPkts": rSInPkts,
       "rSOutPkts": rSOutPkts,
       "rSInBytes": rSInBytes,
       "rSOutBytes": rSOutBytes,
       "rSActiveConns": rSActiveConns,
       "rSInactiveConns": rSInactiveConns,
       "rSCurrentAvgRequest": rSCurrentAvgRequest,
       "rSCurrentAvgResponse": rSCurrentAvgResponse,
       "rSCurrentMaxRequest": rSCurrentMaxRequest,
       "rSCurrentMaxResponse": rSCurrentMaxResponse,
       "rSCurrentMinRequest": rSCurrentMinRequest,
       "rSCurrentMinResponse": rSCurrentMinResponse,
       "rSLongTermAvgRequest": rSLongTermAvgRequest,
       "rSLongTermAvgResponse": rSLongTermAvgResponse,
       "rSLongTermMaxRequest": rSLongTermMaxRequest,
       "rSLongTermMaxResponse": rSLongTermMaxResponse,
       "rSLongTermMinRequest": rSLongTermMinRequest,
       "rSLongTermMinResponse": rSLongTermMinResponse,
       "rSCurrentAvgRTTTimes": rSCurrentAvgRTTTimes,
       "rSCurrentMaxRTTTimes": rSCurrentMaxRTTTimes,
       "rSCurrentMinRTTTimes": rSCurrentMinRTTTimes,
       "rSLongTermAvgRTTTimes": rSLongTermAvgRTTTimes,
       "rSLongTermMaxRTTTimes": rSLongTermMaxRTTTimes,
       "rSLongTermMinRTTTimes": rSLongTermMinRTTTimes,
       "b100NotificationsPrefix": b100NotificationsPrefix,
       "b100Notifications": b100Notifications,
       "vSstateChange": vSstateChange,
       "rSstateChange": rSstateChange,
       "hAstateChange": hAstateChange,
       "licenseExceeded": licenseExceeded,
       "adaptiveInterval": adaptiveInterval,
       "adaptiveUrl": adaptiveUrl,
       "adaptiveCtrlMinP": adaptiveCtrlMinP,
       "adaptiveMinWeight": adaptiveMinWeight}
)
