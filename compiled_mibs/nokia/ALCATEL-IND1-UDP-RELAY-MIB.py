# SNMP MIB module (ALCATEL-IND1-UDP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-UDP-RELAY-MIB

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

(alaDhcpClientTraps,
 routingIND1UdpRelay) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "alaDhcpClientTraps",
    "routingIND1UdpRelay")

(VlanBitmap,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-VLAN-STP-MIB",
    "VlanBitmap")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1UDPRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIB.setRevisions(
        ("2019-10-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IphelperServIndex(TextualConvention, Integer32):
    status = "current"
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("iphelperBootp", 1),
          ("iphelperNbnsNbdd", 2),
          ("iphelperNbdd", 3),
          ("iphelperDns", 4),
          ("iphelperTacacs", 5),
          ("iphelperTftp", 6),
          ("iphelperNtp", 7),
          ("iphelperOther1", 8),
          ("iphelperOther2", 9),
          ("iphelperOther3", 10),
          ("iphelperOther4", 11),
          ("iphelperOther5", 12),
          ("iphelperOther6", 13),
          ("iphelperOther7", 14),
          ("iphelperOther8", 15),
          ("iphelperOther9", 16),
          ("iphelperOther10", 17))
    )



class IphelpereOption82ASCIIFieldType(TextualConvention, Integer32):
    status = "current"
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("macAddress", 1),
          ("systemName", 2),
          ("userString", 3),
          ("interfaceAlias", 4),
          ("vlan", 5),
          ("interface", 6),
          ("cvlan", 7),
          ("portAlias", 8))
    )



class IphelperOption82CircuitOrRemoteId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuitid", 1),
          ("remoteid", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1UDPRelayMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBObjects = _AlcatelIND1UDPRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBObjects.setStatus("current")
_IphelperMIB_ObjectIdentity = ObjectIdentity
iphelperMIB = _IphelperMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1)
)
_IphelperTable_Object = MibTable
iphelperTable = _IphelperTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    iphelperTable.setStatus("current")
_IphelperEntry_Object = MibTableRow
iphelperEntry = _IphelperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1)
)
iphelperEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperService"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperForwAddr"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperVlan"),
)
if mibBuilder.loadTexts:
    iphelperEntry.setStatus("current")
_IphelperService_Type = IphelperServIndex
_IphelperService_Object = MibTableColumn
iphelperService = _IphelperService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 1),
    _IphelperService_Type()
)
iphelperService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperService.setStatus("current")
_IphelperForwAddr_Type = IpAddress
_IphelperForwAddr_Object = MibTableColumn
iphelperForwAddr = _IphelperForwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 2),
    _IphelperForwAddr_Type()
)
iphelperForwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperForwAddr.setStatus("current")
_IphelperVlan_Type = Unsigned32
_IphelperVlan_Object = MibTableColumn
iphelperVlan = _IphelperVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 3),
    _IphelperVlan_Type()
)
iphelperVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperVlan.setStatus("current")
_IphelperStatus_Type = RowStatus
_IphelperStatus_Object = MibTableColumn
iphelperStatus = _IphelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 4),
    _IphelperStatus_Type()
)
iphelperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperStatus.setStatus("current")
_IphelperStatTable_Object = MibTable
iphelperStatTable = _IphelperStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    iphelperStatTable.setStatus("current")
_IphelperStatEntry_Object = MibTableRow
iphelperStatEntry = _IphelperStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1)
)
iphelperStatEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperServerAddress"),
)
if mibBuilder.loadTexts:
    iphelperStatEntry.setStatus("current")
_IphelperServerAddress_Type = IpAddress
_IphelperServerAddress_Object = MibTableColumn
iphelperServerAddress = _IphelperServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 1),
    _IphelperServerAddress_Type()
)
iphelperServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperServerAddress.setStatus("current")


class _IphelperRxFromClient_Type(Unsigned32):
    """Custom type iphelperRxFromClient based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IphelperRxFromClient_Type.__name__ = "Unsigned32"
_IphelperRxFromClient_Object = MibTableColumn
iphelperRxFromClient = _IphelperRxFromClient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 2),
    _IphelperRxFromClient_Type()
)
iphelperRxFromClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperRxFromClient.setStatus("current")


class _IphelperTxToServer_Type(Unsigned32):
    """Custom type iphelperTxToServer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IphelperTxToServer_Type.__name__ = "Unsigned32"
_IphelperTxToServer_Object = MibTableColumn
iphelperTxToServer = _IphelperTxToServer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 3),
    _IphelperTxToServer_Type()
)
iphelperTxToServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperTxToServer.setStatus("current")


class _IphelperMaxHopsViolation_Type(Unsigned32):
    """Custom type iphelperMaxHopsViolation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IphelperMaxHopsViolation_Type.__name__ = "Unsigned32"
_IphelperMaxHopsViolation_Object = MibTableColumn
iphelperMaxHopsViolation = _IphelperMaxHopsViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 4),
    _IphelperMaxHopsViolation_Type()
)
iphelperMaxHopsViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperMaxHopsViolation.setStatus("current")


class _IphelperForwDelayViolation_Type(Unsigned32):
    """Custom type iphelperForwDelayViolation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IphelperForwDelayViolation_Type.__name__ = "Unsigned32"
_IphelperForwDelayViolation_Object = MibTableColumn
iphelperForwDelayViolation = _IphelperForwDelayViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 5),
    _IphelperForwDelayViolation_Type()
)
iphelperForwDelayViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperForwDelayViolation.setStatus("current")


class _IphelperResetAll_Type(Integer32):
    """Custom type iphelperResetAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IphelperResetAll_Type.__name__ = "Integer32"
_IphelperResetAll_Object = MibTableColumn
iphelperResetAll = _IphelperResetAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 6),
    _IphelperResetAll_Type()
)
iphelperResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperResetAll.setStatus("current")
_IphelperAgentInfoViolation_Type = Counter32
_IphelperAgentInfoViolation_Object = MibTableColumn
iphelperAgentInfoViolation = _IphelperAgentInfoViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 7),
    _IphelperAgentInfoViolation_Type()
)
iphelperAgentInfoViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperAgentInfoViolation.setStatus("current")
_IphelperInvalidGatewayIP_Type = Counter32
_IphelperInvalidGatewayIP_Object = MibTableColumn
iphelperInvalidGatewayIP = _IphelperInvalidGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 8),
    _IphelperInvalidGatewayIP_Type()
)
iphelperInvalidGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperInvalidGatewayIP.setStatus("current")
_IphelperInvalidAgentInfoOptFrmSrver_Type = Counter32
_IphelperInvalidAgentInfoOptFrmSrver_Object = MibTableColumn
iphelperInvalidAgentInfoOptFrmSrver = _IphelperInvalidAgentInfoOptFrmSrver_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 9),
    _IphelperInvalidAgentInfoOptFrmSrver_Type()
)
iphelperInvalidAgentInfoOptFrmSrver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperInvalidAgentInfoOptFrmSrver.setStatus("current")


class _IphelperForwDelay_Type(Unsigned32):
    """Custom type iphelperForwDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IphelperForwDelay_Type.__name__ = "Unsigned32"
_IphelperForwDelay_Object = MibScalar
iphelperForwDelay = _IphelperForwDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 3),
    _IphelperForwDelay_Type()
)
iphelperForwDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperForwDelay.setStatus("current")


class _IphelperMaxHops_Type(Unsigned32):
    """Custom type iphelperMaxHops based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IphelperMaxHops_Type.__name__ = "Unsigned32"
_IphelperMaxHops_Object = MibScalar
iphelperMaxHops = _IphelperMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 4),
    _IphelperMaxHops_Type()
)
iphelperMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperMaxHops.setStatus("current")


class _IphelperForwardOption_Type(Integer32):
    """Custom type iphelperForwardOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("avlanOnly", 2),
          ("perVlanOnly", 3))
    )


_IphelperForwardOption_Type.__name__ = "Integer32"
_IphelperForwardOption_Object = MibScalar
iphelperForwardOption = _IphelperForwardOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 5),
    _IphelperForwardOption_Type()
)
iphelperForwardOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperForwardOption.setStatus("current")


class _IphelperBootupOption_Type(Integer32):
    """Custom type iphelperBootupOption based on Integer32"""
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


_IphelperBootupOption_Type.__name__ = "Integer32"
_IphelperBootupOption_Object = MibScalar
iphelperBootupOption = _IphelperBootupOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 6),
    _IphelperBootupOption_Type()
)
iphelperBootupOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperBootupOption.setStatus("current")


class _IphelperBootupPacketOption_Type(Integer32):
    """Custom type iphelperBootupPacketOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 1),
          ("dhcp", 2))
    )


_IphelperBootupPacketOption_Type.__name__ = "Integer32"
_IphelperBootupPacketOption_Object = MibScalar
iphelperBootupPacketOption = _IphelperBootupPacketOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 7),
    _IphelperBootupPacketOption_Type()
)
iphelperBootupPacketOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperBootupPacketOption.setStatus("current")
_IphelperxServicePortAssociationTable_Object = MibTable
iphelperxServicePortAssociationTable = _IphelperxServicePortAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    iphelperxServicePortAssociationTable.setStatus("current")
_IphelperxServicePortAssociationEntry_Object = MibTableRow
iphelperxServicePortAssociationEntry = _IphelperxServicePortAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 8, 1)
)
iphelperxServicePortAssociationEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxServicePortAssociationService"),
)
if mibBuilder.loadTexts:
    iphelperxServicePortAssociationEntry.setStatus("current")
_IphelperxServicePortAssociationService_Type = IphelperServIndex
_IphelperxServicePortAssociationService_Object = MibTableColumn
iphelperxServicePortAssociationService = _IphelperxServicePortAssociationService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 8, 1, 1),
    _IphelperxServicePortAssociationService_Type()
)
iphelperxServicePortAssociationService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperxServicePortAssociationService.setStatus("current")
_IphelperxServicePortAssociationPort_Type = Unsigned32
_IphelperxServicePortAssociationPort_Object = MibTableColumn
iphelperxServicePortAssociationPort = _IphelperxServicePortAssociationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 8, 1, 2),
    _IphelperxServicePortAssociationPort_Type()
)
iphelperxServicePortAssociationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxServicePortAssociationPort.setStatus("current")


class _IphelperxServicePortAssociationName_Type(DisplayString):
    """Custom type iphelperxServicePortAssociationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IphelperxServicePortAssociationName_Type.__name__ = "DisplayString"
_IphelperxServicePortAssociationName_Object = MibTableColumn
iphelperxServicePortAssociationName = _IphelperxServicePortAssociationName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 8, 1, 3),
    _IphelperxServicePortAssociationName_Type()
)
iphelperxServicePortAssociationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxServicePortAssociationName.setStatus("current")
_IphelperxServicePortAssociationStatus_Type = RowStatus
_IphelperxServicePortAssociationStatus_Object = MibTableColumn
iphelperxServicePortAssociationStatus = _IphelperxServicePortAssociationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 8, 1, 4),
    _IphelperxServicePortAssociationStatus_Type()
)
iphelperxServicePortAssociationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperxServicePortAssociationStatus.setStatus("current")
_IphelperxPortServiceAssociationTable_Object = MibTable
iphelperxPortServiceAssociationTable = _IphelperxPortServiceAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    iphelperxPortServiceAssociationTable.setStatus("current")
_IphelperxPortServiceAssociationEntry_Object = MibTableRow
iphelperxPortServiceAssociationEntry = _IphelperxPortServiceAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 9, 1)
)
iphelperxPortServiceAssociationEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxPortServiceAssociationPort"),
)
if mibBuilder.loadTexts:
    iphelperxPortServiceAssociationEntry.setStatus("current")
_IphelperxPortServiceAssociationService_Type = IphelperServIndex
_IphelperxPortServiceAssociationService_Object = MibTableColumn
iphelperxPortServiceAssociationService = _IphelperxPortServiceAssociationService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 9, 1, 1),
    _IphelperxPortServiceAssociationService_Type()
)
iphelperxPortServiceAssociationService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxPortServiceAssociationService.setStatus("current")
_IphelperxPortServiceAssociationPort_Type = Unsigned32
_IphelperxPortServiceAssociationPort_Object = MibTableColumn
iphelperxPortServiceAssociationPort = _IphelperxPortServiceAssociationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 9, 1, 2),
    _IphelperxPortServiceAssociationPort_Type()
)
iphelperxPortServiceAssociationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperxPortServiceAssociationPort.setStatus("current")


class _IphelperxPortServiceAssociationName_Type(DisplayString):
    """Custom type iphelperxPortServiceAssociationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IphelperxPortServiceAssociationName_Type.__name__ = "DisplayString"
_IphelperxPortServiceAssociationName_Object = MibTableColumn
iphelperxPortServiceAssociationName = _IphelperxPortServiceAssociationName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 9, 1, 3),
    _IphelperxPortServiceAssociationName_Type()
)
iphelperxPortServiceAssociationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperxPortServiceAssociationName.setStatus("current")
_IphelperxPortServiceAssociationStatus_Type = RowStatus
_IphelperxPortServiceAssociationStatus_Object = MibTableColumn
iphelperxPortServiceAssociationStatus = _IphelperxPortServiceAssociationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 9, 1, 4),
    _IphelperxPortServiceAssociationStatus_Type()
)
iphelperxPortServiceAssociationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperxPortServiceAssociationStatus.setStatus("current")
_IphelperxPropertiesTable_Object = MibTable
iphelperxPropertiesTable = _IphelperxPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    iphelperxPropertiesTable.setStatus("current")
_IphelperxPropertiesEntry_Object = MibTableRow
iphelperxPropertiesEntry = _IphelperxPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 10, 1)
)
iphelperxPropertiesEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxPropertiesService"),
)
if mibBuilder.loadTexts:
    iphelperxPropertiesEntry.setStatus("current")
_IphelperxPropertiesService_Type = IphelperServIndex
_IphelperxPropertiesService_Object = MibTableColumn
iphelperxPropertiesService = _IphelperxPropertiesService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 10, 1, 1),
    _IphelperxPropertiesService_Type()
)
iphelperxPropertiesService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxPropertiesService.setStatus("current")
_IphelperxPropertiesPort_Type = Unsigned32
_IphelperxPropertiesPort_Object = MibTableColumn
iphelperxPropertiesPort = _IphelperxPropertiesPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 10, 1, 2),
    _IphelperxPropertiesPort_Type()
)
iphelperxPropertiesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxPropertiesPort.setStatus("current")


class _IphelperxPropertiesName_Type(DisplayString):
    """Custom type iphelperxPropertiesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IphelperxPropertiesName_Type.__name__ = "DisplayString"
_IphelperxPropertiesName_Object = MibTableColumn
iphelperxPropertiesName = _IphelperxPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 10, 1, 3),
    _IphelperxPropertiesName_Type()
)
iphelperxPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxPropertiesName.setStatus("current")
_IphelperxStatTable_Object = MibTable
iphelperxStatTable = _IphelperxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    iphelperxStatTable.setStatus("current")
_IphelperxStatEntry_Object = MibTableRow
iphelperxStatEntry = _IphelperxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 11, 1)
)
iphelperxStatEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxStatService"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxStatServerAddress"),
)
if mibBuilder.loadTexts:
    iphelperxStatEntry.setStatus("current")
_IphelperxStatService_Type = IphelperServIndex
_IphelperxStatService_Object = MibTableColumn
iphelperxStatService = _IphelperxStatService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 11, 1, 1),
    _IphelperxStatService_Type()
)
iphelperxStatService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxStatService.setStatus("current")
_IphelperxStatServerAddress_Type = IpAddress
_IphelperxStatServerAddress_Object = MibTableColumn
iphelperxStatServerAddress = _IphelperxStatServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 11, 1, 2),
    _IphelperxStatServerAddress_Type()
)
iphelperxStatServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperxStatServerAddress.setStatus("current")
_IphelperxStatVlan_Type = Unsigned32
_IphelperxStatVlan_Object = MibTableColumn
iphelperxStatVlan = _IphelperxStatVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 11, 1, 3),
    _IphelperxStatVlan_Type()
)
iphelperxStatVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxStatVlan.setStatus("current")


class _IphelperxStatRxFromClient_Type(Unsigned32):
    """Custom type iphelperxStatRxFromClient based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IphelperxStatRxFromClient_Type.__name__ = "Unsigned32"
_IphelperxStatRxFromClient_Object = MibTableColumn
iphelperxStatRxFromClient = _IphelperxStatRxFromClient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 11, 1, 4),
    _IphelperxStatRxFromClient_Type()
)
iphelperxStatRxFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxStatRxFromClient.setStatus("current")


class _IphelperxStatTxToServer_Type(Unsigned32):
    """Custom type iphelperxStatTxToServer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IphelperxStatTxToServer_Type.__name__ = "Unsigned32"
_IphelperxStatTxToServer_Object = MibTableColumn
iphelperxStatTxToServer = _IphelperxStatTxToServer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 11, 1, 5),
    _IphelperxStatTxToServer_Type()
)
iphelperxStatTxToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperxStatTxToServer.setStatus("current")


class _IphelperxStatReset_Type(Integer32):
    """Custom type iphelperxStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IphelperxStatReset_Type.__name__ = "Integer32"
_IphelperxStatReset_Object = MibTableColumn
iphelperxStatReset = _IphelperxStatReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 11, 1, 6),
    _IphelperxStatReset_Type()
)
iphelperxStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperxStatReset.setStatus("current")


class _IphelperAgentInformation_Type(Integer32):
    """Custom type iphelperAgentInformation based on Integer32"""
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


_IphelperAgentInformation_Type.__name__ = "Integer32"
_IphelperAgentInformation_Object = MibScalar
iphelperAgentInformation = _IphelperAgentInformation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 12),
    _IphelperAgentInformation_Type()
)
iphelperAgentInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperAgentInformation.setStatus("current")


class _IphelperAgentInformationPolicy_Type(Integer32):
    """Custom type iphelperAgentInformationPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_IphelperAgentInformationPolicy_Type.__name__ = "Integer32"
_IphelperAgentInformationPolicy_Object = MibScalar
iphelperAgentInformationPolicy = _IphelperAgentInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 13),
    _IphelperAgentInformationPolicy_Type()
)
iphelperAgentInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperAgentInformationPolicy.setStatus("current")
_IphelperDhcpSnoopingVlanTable_Object = MibTable
iphelperDhcpSnoopingVlanTable = _IphelperDhcpSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingVlanTable.setStatus("current")
_IphelperDhcpSnoopingVlanEntry_Object = MibTableRow
iphelperDhcpSnoopingVlanEntry = _IphelperDhcpSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 14, 1)
)
iphelperDhcpSnoopingVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingVlanNumber"),
)
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingVlanEntry.setStatus("current")


class _IphelperDhcpSnoopingVlanNumber_Type(Integer32):
    """Custom type iphelperDhcpSnoopingVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IphelperDhcpSnoopingVlanNumber_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingVlanNumber_Object = MibTableColumn
iphelperDhcpSnoopingVlanNumber = _IphelperDhcpSnoopingVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 14, 1, 1),
    _IphelperDhcpSnoopingVlanNumber_Type()
)
iphelperDhcpSnoopingVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingVlanNumber.setStatus("current")


class _IphelperDhcpSnoopingVlanOpt82DataInsertionStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingVlanOpt82DataInsertionStatus based on Integer32"""
    defaultValue = 1

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


_IphelperDhcpSnoopingVlanOpt82DataInsertionStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingVlanOpt82DataInsertionStatus_Object = MibTableColumn
iphelperDhcpSnoopingVlanOpt82DataInsertionStatus = _IphelperDhcpSnoopingVlanOpt82DataInsertionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 14, 1, 2),
    _IphelperDhcpSnoopingVlanOpt82DataInsertionStatus_Type()
)
iphelperDhcpSnoopingVlanOpt82DataInsertionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingVlanOpt82DataInsertionStatus.setStatus("current")


class _IphelperDhcpSnoopingVlanMacAddrVerificationStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingVlanMacAddrVerificationStatus based on Integer32"""
    defaultValue = 1

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


_IphelperDhcpSnoopingVlanMacAddrVerificationStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingVlanMacAddrVerificationStatus_Object = MibTableColumn
iphelperDhcpSnoopingVlanMacAddrVerificationStatus = _IphelperDhcpSnoopingVlanMacAddrVerificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 14, 1, 3),
    _IphelperDhcpSnoopingVlanMacAddrVerificationStatus_Type()
)
iphelperDhcpSnoopingVlanMacAddrVerificationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingVlanMacAddrVerificationStatus.setStatus("current")


class _IphelperDhcpSnoopingVlanTrafficSuppressionStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingVlanTrafficSuppressionStatus based on Integer32"""
    defaultValue = 2

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


_IphelperDhcpSnoopingVlanTrafficSuppressionStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingVlanTrafficSuppressionStatus_Object = MibTableColumn
iphelperDhcpSnoopingVlanTrafficSuppressionStatus = _IphelperDhcpSnoopingVlanTrafficSuppressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 14, 1, 4),
    _IphelperDhcpSnoopingVlanTrafficSuppressionStatus_Type()
)
iphelperDhcpSnoopingVlanTrafficSuppressionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingVlanTrafficSuppressionStatus.setStatus("current")
_IphelperDhcpSnoopingVlanStatus_Type = RowStatus
_IphelperDhcpSnoopingVlanStatus_Object = MibTableColumn
iphelperDhcpSnoopingVlanStatus = _IphelperDhcpSnoopingVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 14, 1, 5),
    _IphelperDhcpSnoopingVlanStatus_Type()
)
iphelperDhcpSnoopingVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingVlanStatus.setStatus("current")
_IphelperDhcpSnoopingPortTable_Object = MibTable
iphelperDhcpSnoopingPortTable = _IphelperDhcpSnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortTable.setStatus("current")
_IphelperDhcpSnoopingPortEntry_Object = MibTableRow
iphelperDhcpSnoopingPortEntry = _IphelperDhcpSnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1)
)
iphelperDhcpSnoopingPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingPortIfIndex"),
)
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortEntry.setStatus("current")
_IphelperDhcpSnoopingPortIfIndex_Type = InterfaceIndex
_IphelperDhcpSnoopingPortIfIndex_Object = MibTableColumn
iphelperDhcpSnoopingPortIfIndex = _IphelperDhcpSnoopingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1, 1),
    _IphelperDhcpSnoopingPortIfIndex_Type()
)
iphelperDhcpSnoopingPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortIfIndex.setStatus("current")


class _IphelperDhcpSnoopingPortTrustMode_Type(Integer32):
    """Custom type iphelperDhcpSnoopingPortTrustMode based on Integer32"""
    defaultValue = 2

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
          ("clientOnly", 2),
          ("trusted", 3))
    )


_IphelperDhcpSnoopingPortTrustMode_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingPortTrustMode_Object = MibTableColumn
iphelperDhcpSnoopingPortTrustMode = _IphelperDhcpSnoopingPortTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1, 2),
    _IphelperDhcpSnoopingPortTrustMode_Type()
)
iphelperDhcpSnoopingPortTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortTrustMode.setStatus("current")


class _IphelperDhcpSnoopingPortTrafficSuppression_Type(Integer32):
    """Custom type iphelperDhcpSnoopingPortTrafficSuppression based on Integer32"""
    defaultValue = 2

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


_IphelperDhcpSnoopingPortTrafficSuppression_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingPortTrafficSuppression_Object = MibTableColumn
iphelperDhcpSnoopingPortTrafficSuppression = _IphelperDhcpSnoopingPortTrafficSuppression_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1, 3),
    _IphelperDhcpSnoopingPortTrafficSuppression_Type()
)
iphelperDhcpSnoopingPortTrafficSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortTrafficSuppression.setStatus("current")
_IphelperDhcpSnoopingPortMacAddrViolation_Type = Counter32
_IphelperDhcpSnoopingPortMacAddrViolation_Object = MibTableColumn
iphelperDhcpSnoopingPortMacAddrViolation = _IphelperDhcpSnoopingPortMacAddrViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1, 4),
    _IphelperDhcpSnoopingPortMacAddrViolation_Type()
)
iphelperDhcpSnoopingPortMacAddrViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortMacAddrViolation.setStatus("current")
_IphelperDhcpSnoopingPortDhcpServerViolation_Type = Counter32
_IphelperDhcpSnoopingPortDhcpServerViolation_Object = MibTableColumn
iphelperDhcpSnoopingPortDhcpServerViolation = _IphelperDhcpSnoopingPortDhcpServerViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1, 5),
    _IphelperDhcpSnoopingPortDhcpServerViolation_Type()
)
iphelperDhcpSnoopingPortDhcpServerViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortDhcpServerViolation.setStatus("current")
_IphelperDhcpSnoopingPortOption82Violation_Type = Counter32
_IphelperDhcpSnoopingPortOption82Violation_Object = MibTableColumn
iphelperDhcpSnoopingPortOption82Violation = _IphelperDhcpSnoopingPortOption82Violation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1, 6),
    _IphelperDhcpSnoopingPortOption82Violation_Type()
)
iphelperDhcpSnoopingPortOption82Violation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortOption82Violation.setStatus("current")
_IphelperDhcpSnoopingPortRelayAgentViolation_Type = Counter32
_IphelperDhcpSnoopingPortRelayAgentViolation_Object = MibTableColumn
iphelperDhcpSnoopingPortRelayAgentViolation = _IphelperDhcpSnoopingPortRelayAgentViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1, 7),
    _IphelperDhcpSnoopingPortRelayAgentViolation_Type()
)
iphelperDhcpSnoopingPortRelayAgentViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortRelayAgentViolation.setStatus("current")
_IphelperDhcpSnoopingPortBindingViolation_Type = Counter32
_IphelperDhcpSnoopingPortBindingViolation_Object = MibTableColumn
iphelperDhcpSnoopingPortBindingViolation = _IphelperDhcpSnoopingPortBindingViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1, 8),
    _IphelperDhcpSnoopingPortBindingViolation_Type()
)
iphelperDhcpSnoopingPortBindingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortBindingViolation.setStatus("current")


class _IphelperDhcpSnoopingPortIpSourceFiltering_Type(Integer32):
    """Custom type iphelperDhcpSnoopingPortIpSourceFiltering based on Integer32"""
    defaultValue = 2

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


_IphelperDhcpSnoopingPortIpSourceFiltering_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingPortIpSourceFiltering_Object = MibTableColumn
iphelperDhcpSnoopingPortIpSourceFiltering = _IphelperDhcpSnoopingPortIpSourceFiltering_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 15, 1, 9),
    _IphelperDhcpSnoopingPortIpSourceFiltering_Type()
)
iphelperDhcpSnoopingPortIpSourceFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingPortIpSourceFiltering.setStatus("current")
_IphelperDhcpSnoopingBindingTable_Object = MibTable
iphelperDhcpSnoopingBindingTable = _IphelperDhcpSnoopingBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingTable.setStatus("current")
_IphelperDhcpSnoopingBindingEntry_Object = MibTableRow
iphelperDhcpSnoopingBindingEntry = _IphelperDhcpSnoopingBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16, 1)
)
iphelperDhcpSnoopingBindingEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingMacAddress"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingIfIndex"),
)
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingEntry.setStatus("current")
_IphelperDhcpSnoopingBindingMacAddress_Type = MacAddress
_IphelperDhcpSnoopingBindingMacAddress_Object = MibTableColumn
iphelperDhcpSnoopingBindingMacAddress = _IphelperDhcpSnoopingBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16, 1, 1),
    _IphelperDhcpSnoopingBindingMacAddress_Type()
)
iphelperDhcpSnoopingBindingMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingMacAddress.setStatus("current")
_IphelperDhcpSnoopingBindingIfIndex_Type = InterfaceIndex
_IphelperDhcpSnoopingBindingIfIndex_Object = MibTableColumn
iphelperDhcpSnoopingBindingIfIndex = _IphelperDhcpSnoopingBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16, 1, 2),
    _IphelperDhcpSnoopingBindingIfIndex_Type()
)
iphelperDhcpSnoopingBindingIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingIfIndex.setStatus("current")
_IphelperDhcpSnoopingBindingIpAddress_Type = IpAddress
_IphelperDhcpSnoopingBindingIpAddress_Object = MibTableColumn
iphelperDhcpSnoopingBindingIpAddress = _IphelperDhcpSnoopingBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16, 1, 3),
    _IphelperDhcpSnoopingBindingIpAddress_Type()
)
iphelperDhcpSnoopingBindingIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingIpAddress.setStatus("current")
_IphelperDhcpSnoopingBindingVlan_Type = Unsigned32
_IphelperDhcpSnoopingBindingVlan_Object = MibTableColumn
iphelperDhcpSnoopingBindingVlan = _IphelperDhcpSnoopingBindingVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16, 1, 4),
    _IphelperDhcpSnoopingBindingVlan_Type()
)
iphelperDhcpSnoopingBindingVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingVlan.setStatus("current")
_IphelperDhcpSnoopingBindingLeaseTime_Type = Unsigned32
_IphelperDhcpSnoopingBindingLeaseTime_Object = MibTableColumn
iphelperDhcpSnoopingBindingLeaseTime = _IphelperDhcpSnoopingBindingLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16, 1, 5),
    _IphelperDhcpSnoopingBindingLeaseTime_Type()
)
iphelperDhcpSnoopingBindingLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingLeaseTime.setStatus("current")


class _IphelperDhcpSnoopingBindingType_Type(Integer32):
    """Custom type iphelperDhcpSnoopingBindingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_IphelperDhcpSnoopingBindingType_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingBindingType_Object = MibTableColumn
iphelperDhcpSnoopingBindingType = _IphelperDhcpSnoopingBindingType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16, 1, 6),
    _IphelperDhcpSnoopingBindingType_Type()
)
iphelperDhcpSnoopingBindingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingType.setStatus("current")
_IphelperDhcpSnoopingBindingRowStatus_Type = RowStatus
_IphelperDhcpSnoopingBindingRowStatus_Object = MibTableColumn
iphelperDhcpSnoopingBindingRowStatus = _IphelperDhcpSnoopingBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16, 1, 7),
    _IphelperDhcpSnoopingBindingRowStatus_Type()
)
iphelperDhcpSnoopingBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingRowStatus.setStatus("current")


class _IphelperDhcpSnoopingBindingRemoteFlag_Type(Integer32):
    """Custom type iphelperDhcpSnoopingBindingRemoteFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remote", 1),
          ("local", 2))
    )


_IphelperDhcpSnoopingBindingRemoteFlag_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingBindingRemoteFlag_Object = MibTableColumn
iphelperDhcpSnoopingBindingRemoteFlag = _IphelperDhcpSnoopingBindingRemoteFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 16, 1, 8),
    _IphelperDhcpSnoopingBindingRemoteFlag_Type()
)
iphelperDhcpSnoopingBindingRemoteFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingRemoteFlag.setStatus("current")


class _IphelperDhcpSnooping_Type(Integer32):
    """Custom type iphelperDhcpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("switchLevel", 1),
          ("disabled", 2),
          ("vlanLevel", 3))
    )


_IphelperDhcpSnooping_Type.__name__ = "Integer32"
_IphelperDhcpSnooping_Object = MibScalar
iphelperDhcpSnooping = _IphelperDhcpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 17),
    _IphelperDhcpSnooping_Type()
)
iphelperDhcpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnooping.setStatus("current")


class _IphelperDhcpSnoopingOpt82DataInsertionStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingOpt82DataInsertionStatus based on Integer32"""
    defaultValue = 1

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


_IphelperDhcpSnoopingOpt82DataInsertionStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingOpt82DataInsertionStatus_Object = MibScalar
iphelperDhcpSnoopingOpt82DataInsertionStatus = _IphelperDhcpSnoopingOpt82DataInsertionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 18),
    _IphelperDhcpSnoopingOpt82DataInsertionStatus_Type()
)
iphelperDhcpSnoopingOpt82DataInsertionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOpt82DataInsertionStatus.setStatus("current")


class _IphelperDhcpSnoopingMacAddrVerificationStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingMacAddrVerificationStatus based on Integer32"""
    defaultValue = 1

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


_IphelperDhcpSnoopingMacAddrVerificationStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingMacAddrVerificationStatus_Object = MibScalar
iphelperDhcpSnoopingMacAddrVerificationStatus = _IphelperDhcpSnoopingMacAddrVerificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 19),
    _IphelperDhcpSnoopingMacAddrVerificationStatus_Type()
)
iphelperDhcpSnoopingMacAddrVerificationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingMacAddrVerificationStatus.setStatus("current")


class _IphelperDhcpSnoopingTrafficSuppressionStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingTrafficSuppressionStatus based on Integer32"""
    defaultValue = 2

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


_IphelperDhcpSnoopingTrafficSuppressionStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingTrafficSuppressionStatus_Object = MibScalar
iphelperDhcpSnoopingTrafficSuppressionStatus = _IphelperDhcpSnoopingTrafficSuppressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 20),
    _IphelperDhcpSnoopingTrafficSuppressionStatus_Type()
)
iphelperDhcpSnoopingTrafficSuppressionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingTrafficSuppressionStatus.setStatus("current")


class _IphelperDhcpSnoopingBindingStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingBindingStatus based on Integer32"""
    defaultValue = 1

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


_IphelperDhcpSnoopingBindingStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingBindingStatus_Object = MibScalar
iphelperDhcpSnoopingBindingStatus = _IphelperDhcpSnoopingBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 21),
    _IphelperDhcpSnoopingBindingStatus_Type()
)
iphelperDhcpSnoopingBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingStatus.setStatus("current")


class _IphelperDhcpSnoopingBindingDatabaseSyncTimeout_Type(Unsigned32):
    """Custom type iphelperDhcpSnoopingBindingDatabaseSyncTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 600),
    )


_IphelperDhcpSnoopingBindingDatabaseSyncTimeout_Type.__name__ = "Unsigned32"
_IphelperDhcpSnoopingBindingDatabaseSyncTimeout_Object = MibScalar
iphelperDhcpSnoopingBindingDatabaseSyncTimeout = _IphelperDhcpSnoopingBindingDatabaseSyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 22),
    _IphelperDhcpSnoopingBindingDatabaseSyncTimeout_Type()
)
iphelperDhcpSnoopingBindingDatabaseSyncTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingDatabaseSyncTimeout.setStatus("current")
_IphelperDhcpSnoopingBindingDatabaseLastSyncTime_Type = DisplayString
_IphelperDhcpSnoopingBindingDatabaseLastSyncTime_Object = MibScalar
iphelperDhcpSnoopingBindingDatabaseLastSyncTime = _IphelperDhcpSnoopingBindingDatabaseLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 23),
    _IphelperDhcpSnoopingBindingDatabaseLastSyncTime_Type()
)
iphelperDhcpSnoopingBindingDatabaseLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingDatabaseLastSyncTime.setStatus("current")


class _IphelperDhcpSnoopingBindingDatabaseAction_Type(Integer32):
    """Custom type iphelperDhcpSnoopingBindingDatabaseAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 0),
          ("purge", 1),
          ("renew", 2))
    )


_IphelperDhcpSnoopingBindingDatabaseAction_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingBindingDatabaseAction_Object = MibScalar
iphelperDhcpSnoopingBindingDatabaseAction = _IphelperDhcpSnoopingBindingDatabaseAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 24),
    _IphelperDhcpSnoopingBindingDatabaseAction_Type()
)
iphelperDhcpSnoopingBindingDatabaseAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingDatabaseAction.setStatus("current")


class _IphelperTrafficSuppressionStatus_Type(Integer32):
    """Custom type iphelperTrafficSuppressionStatus based on Integer32"""
    defaultValue = 2

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


_IphelperTrafficSuppressionStatus_Type.__name__ = "Integer32"
_IphelperTrafficSuppressionStatus_Object = MibScalar
iphelperTrafficSuppressionStatus = _IphelperTrafficSuppressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 25),
    _IphelperTrafficSuppressionStatus_Type()
)
iphelperTrafficSuppressionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperTrafficSuppressionStatus.setStatus("current")


class _IphelperDhcpSnoopingBypassOpt82CheckStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingBypassOpt82CheckStatus based on Integer32"""
    defaultValue = 2

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


_IphelperDhcpSnoopingBypassOpt82CheckStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingBypassOpt82CheckStatus_Object = MibScalar
iphelperDhcpSnoopingBypassOpt82CheckStatus = _IphelperDhcpSnoopingBypassOpt82CheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 26),
    _IphelperDhcpSnoopingBypassOpt82CheckStatus_Type()
)
iphelperDhcpSnoopingBypassOpt82CheckStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBypassOpt82CheckStatus.setStatus("current")


class _IphelperDhcpOption82FormatType_Type(Integer32):
    """Custom type iphelperDhcpOption82FormatType based on Integer32"""
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
        *(("macAddress", 1),
          ("systemName", 2),
          ("userString", 3),
          ("interfaceAlias", 4),
          ("autoInterfaceAlias", 5),
          ("ascii", 6),
          ("portAlias", 7))
    )


_IphelperDhcpOption82FormatType_Type.__name__ = "Integer32"
_IphelperDhcpOption82FormatType_Object = MibScalar
iphelperDhcpOption82FormatType = _IphelperDhcpOption82FormatType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 27),
    _IphelperDhcpOption82FormatType_Type()
)
iphelperDhcpOption82FormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatType.setStatus("current")


class _IphelperDhcpOption82StringValue_Type(DisplayString):
    """Custom type iphelperDhcpOption82StringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82StringValue_Type.__name__ = "DisplayString"
_IphelperDhcpOption82StringValue_Object = MibScalar
iphelperDhcpOption82StringValue = _IphelperDhcpOption82StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 28),
    _IphelperDhcpOption82StringValue_Type()
)
iphelperDhcpOption82StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82StringValue.setStatus("current")


class _IphelperPXESupport_Type(Integer32):
    """Custom type iphelperPXESupport based on Integer32"""
    defaultValue = 2

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


_IphelperPXESupport_Type.__name__ = "Integer32"
_IphelperPXESupport_Object = MibScalar
iphelperPXESupport = _IphelperPXESupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 29),
    _IphelperPXESupport_Type()
)
iphelperPXESupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperPXESupport.setStatus("current")


class _IphelperDhcpSnoopingBindingPersistencyStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingBindingPersistencyStatus based on Integer32"""
    defaultValue = 2

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


_IphelperDhcpSnoopingBindingPersistencyStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingBindingPersistencyStatus_Object = MibScalar
iphelperDhcpSnoopingBindingPersistencyStatus = _IphelperDhcpSnoopingBindingPersistencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 30),
    _IphelperDhcpSnoopingBindingPersistencyStatus_Type()
)
iphelperDhcpSnoopingBindingPersistencyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingBindingPersistencyStatus.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIField1_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField1 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpSnoopingOption82FormatASCIIField1_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpSnoopingOption82FormatASCIIField1_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField1 = _IphelperDhcpSnoopingOption82FormatASCIIField1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 31),
    _IphelperDhcpSnoopingOption82FormatASCIIField1_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField1.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIField1StringValue_Type(DisplayString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField1StringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIField1StringValue_Type.__name__ = "DisplayString"
_IphelperDhcpSnoopingOption82FormatASCIIField1StringValue_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField1StringValue = _IphelperDhcpSnoopingOption82FormatASCIIField1StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 32),
    _IphelperDhcpSnoopingOption82FormatASCIIField1StringValue_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField1StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField1StringValue.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIField2_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField2 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpSnoopingOption82FormatASCIIField2_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpSnoopingOption82FormatASCIIField2_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField2 = _IphelperDhcpSnoopingOption82FormatASCIIField2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 33),
    _IphelperDhcpSnoopingOption82FormatASCIIField2_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField2.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIField2StringValue_Type(DisplayString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField2StringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIField2StringValue_Type.__name__ = "DisplayString"
_IphelperDhcpSnoopingOption82FormatASCIIField2StringValue_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField2StringValue = _IphelperDhcpSnoopingOption82FormatASCIIField2StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 34),
    _IphelperDhcpSnoopingOption82FormatASCIIField2StringValue_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField2StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField2StringValue.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIField3_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField3 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpSnoopingOption82FormatASCIIField3_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpSnoopingOption82FormatASCIIField3_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField3 = _IphelperDhcpSnoopingOption82FormatASCIIField3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 35),
    _IphelperDhcpSnoopingOption82FormatASCIIField3_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField3.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIField3StringValue_Type(DisplayString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField3StringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIField3StringValue_Type.__name__ = "DisplayString"
_IphelperDhcpSnoopingOption82FormatASCIIField3StringValue_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField3StringValue = _IphelperDhcpSnoopingOption82FormatASCIIField3StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 36),
    _IphelperDhcpSnoopingOption82FormatASCIIField3StringValue_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField3StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField3StringValue.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIField4_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField4 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpSnoopingOption82FormatASCIIField4_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpSnoopingOption82FormatASCIIField4_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField4 = _IphelperDhcpSnoopingOption82FormatASCIIField4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 37),
    _IphelperDhcpSnoopingOption82FormatASCIIField4_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField4.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIField4StringValue_Type(DisplayString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField4StringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIField4StringValue_Type.__name__ = "DisplayString"
_IphelperDhcpSnoopingOption82FormatASCIIField4StringValue_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField4StringValue = _IphelperDhcpSnoopingOption82FormatASCIIField4StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 38),
    _IphelperDhcpSnoopingOption82FormatASCIIField4StringValue_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField4StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField4StringValue.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIField5_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField5 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpSnoopingOption82FormatASCIIField5_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpSnoopingOption82FormatASCIIField5_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField5 = _IphelperDhcpSnoopingOption82FormatASCIIField5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 39),
    _IphelperDhcpSnoopingOption82FormatASCIIField5_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField5.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIField5StringValue_Type(DisplayString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIField5StringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIField5StringValue_Type.__name__ = "DisplayString"
_IphelperDhcpSnoopingOption82FormatASCIIField5StringValue_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIField5StringValue = _IphelperDhcpSnoopingOption82FormatASCIIField5StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 40),
    _IphelperDhcpSnoopingOption82FormatASCIIField5StringValue_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIField5StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIField5StringValue.setStatus("deprecated")


class _IphelperDhcpSnoopingOption82FormatASCIIDelimiter_Type(DisplayString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIDelimiter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIDelimiter_Type.__name__ = "DisplayString"
_IphelperDhcpSnoopingOption82FormatASCIIDelimiter_Object = MibScalar
iphelperDhcpSnoopingOption82FormatASCIIDelimiter = _IphelperDhcpSnoopingOption82FormatASCIIDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 41),
    _IphelperDhcpSnoopingOption82FormatASCIIDelimiter_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIDelimiter.setStatus("deprecated")
_IphelperDhcpSourceFilterVlanTable_Object = MibTable
iphelperDhcpSourceFilterVlanTable = _IphelperDhcpSourceFilterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 42)
)
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterVlanTable.setStatus("current")
_IphelperDhcpSourceFilterVlanEntry_Object = MibTableRow
iphelperDhcpSourceFilterVlanEntry = _IphelperDhcpSourceFilterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 42, 1)
)
iphelperDhcpSourceFilterVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSourceFilterVlanNumber"),
)
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterVlanEntry.setStatus("current")


class _IphelperDhcpSourceFilterVlanNumber_Type(Integer32):
    """Custom type iphelperDhcpSourceFilterVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IphelperDhcpSourceFilterVlanNumber_Type.__name__ = "Integer32"
_IphelperDhcpSourceFilterVlanNumber_Object = MibTableColumn
iphelperDhcpSourceFilterVlanNumber = _IphelperDhcpSourceFilterVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 42, 1, 1),
    _IphelperDhcpSourceFilterVlanNumber_Type()
)
iphelperDhcpSourceFilterVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterVlanNumber.setStatus("current")


class _IphelperDhcpSourceFilterVlanFilteringStatus_Type(Integer32):
    """Custom type iphelperDhcpSourceFilterVlanFilteringStatus based on Integer32"""
    defaultValue = 2

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


_IphelperDhcpSourceFilterVlanFilteringStatus_Type.__name__ = "Integer32"
_IphelperDhcpSourceFilterVlanFilteringStatus_Object = MibTableColumn
iphelperDhcpSourceFilterVlanFilteringStatus = _IphelperDhcpSourceFilterVlanFilteringStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 42, 1, 2),
    _IphelperDhcpSourceFilterVlanFilteringStatus_Type()
)
iphelperDhcpSourceFilterVlanFilteringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterVlanFilteringStatus.setStatus("current")


class _IphelperOption82Policy_Type(Integer32):
    """Custom type iphelperOption82Policy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_IphelperOption82Policy_Type.__name__ = "Integer32"
_IphelperOption82Policy_Object = MibScalar
iphelperOption82Policy = _IphelperOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 43),
    _IphelperOption82Policy_Type()
)
iphelperOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperOption82Policy.setStatus("current")
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableTable_Object = MibTable
iphelperDhcpSnoopingOption82FormatASCIIConfigurableTable = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44)
)
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableTable.setStatus("current")
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableEntry_Object = MibTableRow
iphelperDhcpSnoopingOption82FormatASCIIConfigurableEntry = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1)
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex"),
)
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableEntry.setStatus("current")
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex_Type = IphelperOption82CircuitOrRemoteId
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 1),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex.setStatus("current")
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField1_Type = IphelpereOption82ASCIIFieldType
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField1_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1 = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 2),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField1_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Type(SnmpAdminString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Type.__name__ = "SnmpAdminString"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 3),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2 = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 4),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Type(SnmpAdminString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Type.__name__ = "SnmpAdminString"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 5),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3 = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 6),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Type(SnmpAdminString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Type.__name__ = "SnmpAdminString"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 7),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4 = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 8),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Type(SnmpAdminString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Type.__name__ = "SnmpAdminString"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 9),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5 = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 10),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Type(SnmpAdminString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Type.__name__ = "SnmpAdminString"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 11),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal.setStatus("current")


class _IphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Type(SnmpAdminString):
    """Custom type iphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Type.__name__ = "SnmpAdminString"
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 12),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter.setStatus("current")
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus_Type = RowStatus
_IphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus_Object = MibTableColumn
iphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus = _IphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 44, 1, 13),
    _IphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus_Type()
)
iphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus.setStatus("current")
_AlaMdnsGreTunnelName_Type = DisplayString
_AlaMdnsGreTunnelName_Object = MibScalar
alaMdnsGreTunnelName = _AlaMdnsGreTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 45),
    _AlaMdnsGreTunnelName_Type()
)
alaMdnsGreTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMdnsGreTunnelName.setStatus("current")


class _AlaMdnsAdminStatus_Type(Integer32):
    """Custom type alaMdnsAdminStatus based on Integer32"""
    defaultValue = 2

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


_AlaMdnsAdminStatus_Type.__name__ = "Integer32"
_AlaMdnsAdminStatus_Object = MibScalar
alaMdnsAdminStatus = _AlaMdnsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 46),
    _AlaMdnsAdminStatus_Type()
)
alaMdnsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMdnsAdminStatus.setStatus("current")
_AlaMdnsFloodVlans_Type = VlanBitmap
_AlaMdnsFloodVlans_Object = MibScalar
alaMdnsFloodVlans = _AlaMdnsFloodVlans_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 47),
    _AlaMdnsFloodVlans_Type()
)
alaMdnsFloodVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMdnsFloodVlans.setStatus("current")
_IphelperDhcpSourceFilterAllowSubnetTable_Object = MibTable
iphelperDhcpSourceFilterAllowSubnetTable = _IphelperDhcpSourceFilterAllowSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 48)
)
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterAllowSubnetTable.setStatus("current")
_IphelperDhcpSourceFilterAllowIpEntry_Object = MibTableRow
iphelperDhcpSourceFilterAllowIpEntry = _IphelperDhcpSourceFilterAllowIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 48, 1)
)
iphelperDhcpSourceFilterAllowIpEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSourceFilterExpIpAddress"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSourceFilterExpIpMask"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSourceFilterVlan"),
)
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterAllowIpEntry.setStatus("current")
_IphelperDhcpSourceFilterExpIpAddress_Type = IpAddress
_IphelperDhcpSourceFilterExpIpAddress_Object = MibTableColumn
iphelperDhcpSourceFilterExpIpAddress = _IphelperDhcpSourceFilterExpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 48, 1, 1),
    _IphelperDhcpSourceFilterExpIpAddress_Type()
)
iphelperDhcpSourceFilterExpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterExpIpAddress.setStatus("current")
_IphelperDhcpSourceFilterExpIpMask_Type = IpAddress
_IphelperDhcpSourceFilterExpIpMask_Object = MibTableColumn
iphelperDhcpSourceFilterExpIpMask = _IphelperDhcpSourceFilterExpIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 48, 1, 2),
    _IphelperDhcpSourceFilterExpIpMask_Type()
)
iphelperDhcpSourceFilterExpIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterExpIpMask.setStatus("current")


class _IphelperDhcpSourceFilterVlan_Type(Integer32):
    """Custom type iphelperDhcpSourceFilterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IphelperDhcpSourceFilterVlan_Type.__name__ = "Integer32"
_IphelperDhcpSourceFilterVlan_Object = MibTableColumn
iphelperDhcpSourceFilterVlan = _IphelperDhcpSourceFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 48, 1, 3),
    _IphelperDhcpSourceFilterVlan_Type()
)
iphelperDhcpSourceFilterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterVlan.setStatus("current")


class _IphelperDhcpSourceFilterExpIpStatus_Type(Integer32):
    """Custom type iphelperDhcpSourceFilterExpIpStatus based on Integer32"""
    defaultValue = 2

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


_IphelperDhcpSourceFilterExpIpStatus_Type.__name__ = "Integer32"
_IphelperDhcpSourceFilterExpIpStatus_Object = MibTableColumn
iphelperDhcpSourceFilterExpIpStatus = _IphelperDhcpSourceFilterExpIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 48, 1, 4),
    _IphelperDhcpSourceFilterExpIpStatus_Type()
)
iphelperDhcpSourceFilterExpIpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSourceFilterExpIpStatus.setStatus("current")


class _IphelperDhcpSnoopingTrapStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingTrapStatus based on Integer32"""
    defaultValue = 0

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
        *(("default", 0),
          ("reverse-enable", 1),
          ("hardware", 2),
          ("software", 3))
    )


_IphelperDhcpSnoopingTrapStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingTrapStatus_Object = MibScalar
iphelperDhcpSnoopingTrapStatus = _IphelperDhcpSnoopingTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 49),
    _IphelperDhcpSnoopingTrapStatus_Type()
)
iphelperDhcpSnoopingTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingTrapStatus.setStatus("current")


class _IphelperDhcpSnoopingArpAllowStatus_Type(Integer32):
    """Custom type iphelperDhcpSnoopingArpAllowStatus based on Integer32"""
    defaultValue = 2

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


_IphelperDhcpSnoopingArpAllowStatus_Type.__name__ = "Integer32"
_IphelperDhcpSnoopingArpAllowStatus_Object = MibScalar
iphelperDhcpSnoopingArpAllowStatus = _IphelperDhcpSnoopingArpAllowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 1, 50),
    _IphelperDhcpSnoopingArpAllowStatus_Type()
)
iphelperDhcpSnoopingArpAllowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpSnoopingArpAllowStatus.setStatus("current")
_Ipv6helperMIB_ObjectIdentity = ObjectIdentity
ipv6helperMIB = _Ipv6helperMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2)
)
_Ipv6helperTable_Object = MibTable
ipv6helperTable = _Ipv6helperTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipv6helperTable.setStatus("current")
_Ipv6helperEntry_Object = MibTableRow
ipv6helperEntry = _Ipv6helperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1)
)
ipv6helperEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperForwAddr"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperVlan"),
)
if mibBuilder.loadTexts:
    ipv6helperEntry.setStatus("current")
_Ipv6helperForwAddr_Type = InetAddressIPv6
_Ipv6helperForwAddr_Object = MibTableColumn
ipv6helperForwAddr = _Ipv6helperForwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 1),
    _Ipv6helperForwAddr_Type()
)
ipv6helperForwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6helperForwAddr.setStatus("current")


class _Ipv6helperVlan_Type(Integer32):
    """Custom type ipv6helperVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Ipv6helperVlan_Type.__name__ = "Integer32"
_Ipv6helperVlan_Object = MibTableColumn
ipv6helperVlan = _Ipv6helperVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 2),
    _Ipv6helperVlan_Type()
)
ipv6helperVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6helperVlan.setStatus("current")
_Ipv6helperStatus_Type = RowStatus
_Ipv6helperStatus_Object = MibTableColumn
ipv6helperStatus = _Ipv6helperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 3),
    _Ipv6helperStatus_Type()
)
ipv6helperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6helperStatus.setStatus("current")


class _Ipv6helperForwardOption_Type(Integer32):
    """Custom type ipv6helperForwardOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("perVlanOnly", 2))
    )


_Ipv6helperForwardOption_Type.__name__ = "Integer32"
_Ipv6helperForwardOption_Object = MibScalar
ipv6helperForwardOption = _Ipv6helperForwardOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 2),
    _Ipv6helperForwardOption_Type()
)
ipv6helperForwardOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperForwardOption.setStatus("current")


class _Ipv6helperMaxHops_Type(Unsigned32):
    """Custom type ipv6helperMaxHops based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Ipv6helperMaxHops_Type.__name__ = "Unsigned32"
_Ipv6helperMaxHops_Object = MibScalar
ipv6helperMaxHops = _Ipv6helperMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 3),
    _Ipv6helperMaxHops_Type()
)
ipv6helperMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperMaxHops.setStatus("current")


class _Ipv6helperDhcpSnooping_Type(Integer32):
    """Custom type ipv6helperDhcpSnooping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("switchLevel", 1),
          ("disabled", 2),
          ("vlanLevel", 3))
    )


_Ipv6helperDhcpSnooping_Type.__name__ = "Integer32"
_Ipv6helperDhcpSnooping_Object = MibScalar
ipv6helperDhcpSnooping = _Ipv6helperDhcpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 4),
    _Ipv6helperDhcpSnooping_Type()
)
ipv6helperDhcpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnooping.setStatus("current")
_Ipv6helperDhcpSnoopingVlanTable_Object = MibTable
ipv6helperDhcpSnoopingVlanTable = _Ipv6helperDhcpSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingVlanTable.setStatus("current")
_Ipv6helperDhcpSnoopingVlanEntry_Object = MibTableRow
ipv6helperDhcpSnoopingVlanEntry = _Ipv6helperDhcpSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 5, 1)
)
ipv6helperDhcpSnoopingVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingVlanNumber"),
)
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingVlanEntry.setStatus("current")


class _Ipv6helperDhcpSnoopingVlanNumber_Type(Integer32):
    """Custom type ipv6helperDhcpSnoopingVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Ipv6helperDhcpSnoopingVlanNumber_Type.__name__ = "Integer32"
_Ipv6helperDhcpSnoopingVlanNumber_Object = MibTableColumn
ipv6helperDhcpSnoopingVlanNumber = _Ipv6helperDhcpSnoopingVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 5, 1, 1),
    _Ipv6helperDhcpSnoopingVlanNumber_Type()
)
ipv6helperDhcpSnoopingVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingVlanNumber.setStatus("current")
_Ipv6helperDhcpSnoopingVlanStatus_Type = RowStatus
_Ipv6helperDhcpSnoopingVlanStatus_Object = MibTableColumn
ipv6helperDhcpSnoopingVlanStatus = _Ipv6helperDhcpSnoopingVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 5, 1, 2),
    _Ipv6helperDhcpSnoopingVlanStatus_Type()
)
ipv6helperDhcpSnoopingVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingVlanStatus.setStatus("current")
_Ipv6helperDhcpSnoopingPortTable_Object = MibTable
ipv6helperDhcpSnoopingPortTable = _Ipv6helperDhcpSnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingPortTable.setStatus("current")
_Ipv6helperDhcpSnoopingPortEntry_Object = MibTableRow
ipv6helperDhcpSnoopingPortEntry = _Ipv6helperDhcpSnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 6, 1)
)
ipv6helperDhcpSnoopingPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingPortIfIndex"),
)
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingPortEntry.setStatus("current")
_Ipv6helperDhcpSnoopingPortIfIndex_Type = InterfaceIndex
_Ipv6helperDhcpSnoopingPortIfIndex_Object = MibTableColumn
ipv6helperDhcpSnoopingPortIfIndex = _Ipv6helperDhcpSnoopingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 6, 1, 1),
    _Ipv6helperDhcpSnoopingPortIfIndex_Type()
)
ipv6helperDhcpSnoopingPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingPortIfIndex.setStatus("current")


class _Ipv6helperDhcpSnoopingPortTrustMode_Type(Integer32):
    """Custom type ipv6helperDhcpSnoopingPortTrustMode based on Integer32"""
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
        *(("blocked", 1),
          ("clientOnlyUntrusted", 2),
          ("clientOnlyTrusted", 3),
          ("trusted", 4))
    )


_Ipv6helperDhcpSnoopingPortTrustMode_Type.__name__ = "Integer32"
_Ipv6helperDhcpSnoopingPortTrustMode_Object = MibTableColumn
ipv6helperDhcpSnoopingPortTrustMode = _Ipv6helperDhcpSnoopingPortTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 6, 1, 2),
    _Ipv6helperDhcpSnoopingPortTrustMode_Type()
)
ipv6helperDhcpSnoopingPortTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingPortTrustMode.setStatus("current")
_Ipv6helperSnoopingClientViolation_Type = Counter32
_Ipv6helperSnoopingClientViolation_Object = MibTableColumn
ipv6helperSnoopingClientViolation = _Ipv6helperSnoopingClientViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 6, 1, 3),
    _Ipv6helperSnoopingClientViolation_Type()
)
ipv6helperSnoopingClientViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperSnoopingClientViolation.setStatus("current")
_Ipv6helperSnoopingServerViolation_Type = Counter32
_Ipv6helperSnoopingServerViolation_Object = MibTableColumn
ipv6helperSnoopingServerViolation = _Ipv6helperSnoopingServerViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 6, 1, 4),
    _Ipv6helperSnoopingServerViolation_Type()
)
ipv6helperSnoopingServerViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperSnoopingServerViolation.setStatus("current")
_Ipv6helperSnoopingBindingViolation_Type = Counter32
_Ipv6helperSnoopingBindingViolation_Object = MibTableColumn
ipv6helperSnoopingBindingViolation = _Ipv6helperSnoopingBindingViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 6, 1, 5),
    _Ipv6helperSnoopingBindingViolation_Type()
)
ipv6helperSnoopingBindingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperSnoopingBindingViolation.setStatus("current")
_Ipv6helperSnoopingInterfaceidViolation_Type = Counter32
_Ipv6helperSnoopingInterfaceidViolation_Object = MibTableColumn
ipv6helperSnoopingInterfaceidViolation = _Ipv6helperSnoopingInterfaceidViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 6, 1, 6),
    _Ipv6helperSnoopingInterfaceidViolation_Type()
)
ipv6helperSnoopingInterfaceidViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperSnoopingInterfaceidViolation.setStatus("current")


class _Ipv6helperSnoopingPortSourceFilterStatus_Type(Integer32):
    """Custom type ipv6helperSnoopingPortSourceFilterStatus based on Integer32"""
    defaultValue = 2

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


_Ipv6helperSnoopingPortSourceFilterStatus_Type.__name__ = "Integer32"
_Ipv6helperSnoopingPortSourceFilterStatus_Object = MibTableColumn
ipv6helperSnoopingPortSourceFilterStatus = _Ipv6helperSnoopingPortSourceFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 6, 1, 7),
    _Ipv6helperSnoopingPortSourceFilterStatus_Type()
)
ipv6helperSnoopingPortSourceFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperSnoopingPortSourceFilterStatus.setStatus("current")


class _Ipv6helperDhcpSnoopingBindingStatus_Type(Integer32):
    """Custom type ipv6helperDhcpSnoopingBindingStatus based on Integer32"""
    defaultValue = 1

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


_Ipv6helperDhcpSnoopingBindingStatus_Type.__name__ = "Integer32"
_Ipv6helperDhcpSnoopingBindingStatus_Object = MibScalar
ipv6helperDhcpSnoopingBindingStatus = _Ipv6helperDhcpSnoopingBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 7),
    _Ipv6helperDhcpSnoopingBindingStatus_Type()
)
ipv6helperDhcpSnoopingBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingBindingStatus.setStatus("current")
_Ipv6helperDhcpSnoopingBindingTable_Object = MibTable
ipv6helperDhcpSnoopingBindingTable = _Ipv6helperDhcpSnoopingBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingBindingTable.setStatus("current")
_Ipv6helperDhcpSnoopingBindingEntry_Object = MibTableRow
ipv6helperDhcpSnoopingBindingEntry = _Ipv6helperDhcpSnoopingBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 8, 1)
)
ipv6helperDhcpSnoopingBindingEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperBindingLinkLocalAddress"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperBindingVlan"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperBindingIfIndex"),
)
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingBindingEntry.setStatus("current")
_Ipv6helperBindingLinkLocalAddress_Type = InetAddressIPv6
_Ipv6helperBindingLinkLocalAddress_Object = MibTableColumn
ipv6helperBindingLinkLocalAddress = _Ipv6helperBindingLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 8, 1, 1),
    _Ipv6helperBindingLinkLocalAddress_Type()
)
ipv6helperBindingLinkLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperBindingLinkLocalAddress.setStatus("current")


class _Ipv6helperBindingVlan_Type(Integer32):
    """Custom type ipv6helperBindingVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Ipv6helperBindingVlan_Type.__name__ = "Integer32"
_Ipv6helperBindingVlan_Object = MibTableColumn
ipv6helperBindingVlan = _Ipv6helperBindingVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 8, 1, 2),
    _Ipv6helperBindingVlan_Type()
)
ipv6helperBindingVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperBindingVlan.setStatus("current")
_Ipv6helperBindingIfIndex_Type = InterfaceIndex
_Ipv6helperBindingIfIndex_Object = MibTableColumn
ipv6helperBindingIfIndex = _Ipv6helperBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 8, 1, 3),
    _Ipv6helperBindingIfIndex_Type()
)
ipv6helperBindingIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperBindingIfIndex.setStatus("current")
_Ipv6helperBindingGlobalIpv6Address_Type = InetAddressIPv6
_Ipv6helperBindingGlobalIpv6Address_Object = MibTableColumn
ipv6helperBindingGlobalIpv6Address = _Ipv6helperBindingGlobalIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 8, 1, 4),
    _Ipv6helperBindingGlobalIpv6Address_Type()
)
ipv6helperBindingGlobalIpv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6helperBindingGlobalIpv6Address.setStatus("current")
_Ipv6helperBindingLeaseTime_Type = Unsigned32
_Ipv6helperBindingLeaseTime_Object = MibTableColumn
ipv6helperBindingLeaseTime = _Ipv6helperBindingLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 8, 1, 5),
    _Ipv6helperBindingLeaseTime_Type()
)
ipv6helperBindingLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperBindingLeaseTime.setStatus("current")
_Ipv6helperBindingRowStatus_Type = RowStatus
_Ipv6helperBindingRowStatus_Object = MibTableColumn
ipv6helperBindingRowStatus = _Ipv6helperBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 8, 1, 6),
    _Ipv6helperBindingRowStatus_Type()
)
ipv6helperBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6helperBindingRowStatus.setStatus("current")


class _Ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout_Type(Unsigned32):
    """Custom type ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 600),
    )


_Ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout_Type.__name__ = "Unsigned32"
_Ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout_Object = MibScalar
ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout = _Ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 9),
    _Ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout_Type()
)
ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout.setStatus("current")
_Ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime_Type = DisplayString
_Ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime_Object = MibScalar
ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime = _Ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 10),
    _Ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime_Type()
)
ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime.setStatus("current")


class _Ipv6helperDhcpSnoopingBindingDatabaseAction_Type(Integer32):
    """Custom type ipv6helperDhcpSnoopingBindingDatabaseAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 0),
          ("purge", 1),
          ("renew", 2))
    )


_Ipv6helperDhcpSnoopingBindingDatabaseAction_Type.__name__ = "Integer32"
_Ipv6helperDhcpSnoopingBindingDatabaseAction_Object = MibScalar
ipv6helperDhcpSnoopingBindingDatabaseAction = _Ipv6helperDhcpSnoopingBindingDatabaseAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 11),
    _Ipv6helperDhcpSnoopingBindingDatabaseAction_Type()
)
ipv6helperDhcpSnoopingBindingDatabaseAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingBindingDatabaseAction.setStatus("current")


class _Ipv6helperDhcpSnoopingBindingPersistencyStatus_Type(Integer32):
    """Custom type ipv6helperDhcpSnoopingBindingPersistencyStatus based on Integer32"""
    defaultValue = 2

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


_Ipv6helperDhcpSnoopingBindingPersistencyStatus_Type.__name__ = "Integer32"
_Ipv6helperDhcpSnoopingBindingPersistencyStatus_Object = MibScalar
ipv6helperDhcpSnoopingBindingPersistencyStatus = _Ipv6helperDhcpSnoopingBindingPersistencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 12),
    _Ipv6helperDhcpSnoopingBindingPersistencyStatus_Type()
)
ipv6helperDhcpSnoopingBindingPersistencyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperDhcpSnoopingBindingPersistencyStatus.setStatus("current")
_Ipv6helperStatTable_Object = MibTable
ipv6helperStatTable = _Ipv6helperStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    ipv6helperStatTable.setStatus("current")
_Ipv6helperStatEntry_Object = MibTableRow
ipv6helperStatEntry = _Ipv6helperStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 13, 1)
)
ipv6helperStatEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperStatsServerAddress"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperStatsVlan"),
)
if mibBuilder.loadTexts:
    ipv6helperStatEntry.setStatus("current")
_Ipv6helperStatsServerAddress_Type = InetAddressIPv6
_Ipv6helperStatsServerAddress_Object = MibTableColumn
ipv6helperStatsServerAddress = _Ipv6helperStatsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 13, 1, 1),
    _Ipv6helperStatsServerAddress_Type()
)
ipv6helperStatsServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperStatsServerAddress.setStatus("current")


class _Ipv6helperStatsVlan_Type(Integer32):
    """Custom type ipv6helperStatsVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Ipv6helperStatsVlan_Type.__name__ = "Integer32"
_Ipv6helperStatsVlan_Object = MibTableColumn
ipv6helperStatsVlan = _Ipv6helperStatsVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 13, 1, 2),
    _Ipv6helperStatsVlan_Type()
)
ipv6helperStatsVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperStatsVlan.setStatus("current")


class _Ipv6helperTxToServer_Type(Unsigned32):
    """Custom type ipv6helperTxToServer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6helperTxToServer_Type.__name__ = "Unsigned32"
_Ipv6helperTxToServer_Object = MibTableColumn
ipv6helperTxToServer = _Ipv6helperTxToServer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 13, 1, 3),
    _Ipv6helperTxToServer_Type()
)
ipv6helperTxToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperTxToServer.setStatus("current")


class _Ipv6helperInterfaceIdPrefixValue_Type(DisplayString):
    """Custom type ipv6helperInterfaceIdPrefixValue based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 246),
    )


_Ipv6helperInterfaceIdPrefixValue_Type.__name__ = "DisplayString"
_Ipv6helperInterfaceIdPrefixValue_Object = MibScalar
ipv6helperInterfaceIdPrefixValue = _Ipv6helperInterfaceIdPrefixValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 14),
    _Ipv6helperInterfaceIdPrefixValue_Type()
)
ipv6helperInterfaceIdPrefixValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperInterfaceIdPrefixValue.setStatus("current")


class _Ipv6helperRemoteIdEnterpriseNumber_Type(Unsigned32):
    """Custom type ipv6helperRemoteIdEnterpriseNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ipv6helperRemoteIdEnterpriseNumber_Type.__name__ = "Unsigned32"
_Ipv6helperRemoteIdEnterpriseNumber_Object = MibScalar
ipv6helperRemoteIdEnterpriseNumber = _Ipv6helperRemoteIdEnterpriseNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 15),
    _Ipv6helperRemoteIdEnterpriseNumber_Type()
)
ipv6helperRemoteIdEnterpriseNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperRemoteIdEnterpriseNumber.setStatus("current")


class _Ipv6helperRemoteIdUserStringValue_Type(DisplayString):
    """Custom type ipv6helperRemoteIdUserStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Ipv6helperRemoteIdUserStringValue_Type.__name__ = "DisplayString"
_Ipv6helperRemoteIdUserStringValue_Object = MibScalar
ipv6helperRemoteIdUserStringValue = _Ipv6helperRemoteIdUserStringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 16),
    _Ipv6helperRemoteIdUserStringValue_Type()
)
ipv6helperRemoteIdUserStringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperRemoteIdUserStringValue.setStatus("current")


class _Ipv6helperRemoteIdFormatType_Type(Integer32):
    """Custom type ipv6helperRemoteIdFormatType based on Integer32"""
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
        *(("disabled", 1),
          ("baseMacAddress", 2),
          ("systemName", 3),
          ("vlan", 4),
          ("userString", 5),
          ("interfaceAlias", 6),
          ("autoInterfaceAlias", 7))
    )


_Ipv6helperRemoteIdFormatType_Type.__name__ = "Integer32"
_Ipv6helperRemoteIdFormatType_Object = MibScalar
ipv6helperRemoteIdFormatType = _Ipv6helperRemoteIdFormatType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 17),
    _Ipv6helperRemoteIdFormatType_Type()
)
ipv6helperRemoteIdFormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperRemoteIdFormatType.setStatus("current")


class _Ipv6helperRxFromClient_Type(Unsigned32):
    """Custom type ipv6helperRxFromClient based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6helperRxFromClient_Type.__name__ = "Unsigned32"
_Ipv6helperRxFromClient_Object = MibScalar
ipv6helperRxFromClient = _Ipv6helperRxFromClient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 18),
    _Ipv6helperRxFromClient_Type()
)
ipv6helperRxFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperRxFromClient.setStatus("current")


class _Ipv6helperMaxHopsViolation_Type(Unsigned32):
    """Custom type ipv6helperMaxHopsViolation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6helperMaxHopsViolation_Type.__name__ = "Unsigned32"
_Ipv6helperMaxHopsViolation_Object = MibScalar
ipv6helperMaxHopsViolation = _Ipv6helperMaxHopsViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 19),
    _Ipv6helperMaxHopsViolation_Type()
)
ipv6helperMaxHopsViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6helperMaxHopsViolation.setStatus("current")


class _Ipv6helperResetAll_Type(Integer32):
    """Custom type ipv6helperResetAll based on Integer32"""
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


_Ipv6helperResetAll_Type.__name__ = "Integer32"
_Ipv6helperResetAll_Object = MibScalar
ipv6helperResetAll = _Ipv6helperResetAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 20),
    _Ipv6helperResetAll_Type()
)
ipv6helperResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperResetAll.setStatus("current")
_Ipv6helperSourceFilterVlanTable_Object = MibTable
ipv6helperSourceFilterVlanTable = _Ipv6helperSourceFilterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 21)
)
if mibBuilder.loadTexts:
    ipv6helperSourceFilterVlanTable.setStatus("current")
_Ipv6helperSourceFilterVlanEntry_Object = MibTableRow
ipv6helperSourceFilterVlanEntry = _Ipv6helperSourceFilterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 21, 1)
)
ipv6helperSourceFilterVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperSourceFilterVlan"),
)
if mibBuilder.loadTexts:
    ipv6helperSourceFilterVlanEntry.setStatus("current")


class _Ipv6helperSourceFilterVlan_Type(Integer32):
    """Custom type ipv6helperSourceFilterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Ipv6helperSourceFilterVlan_Type.__name__ = "Integer32"
_Ipv6helperSourceFilterVlan_Object = MibTableColumn
ipv6helperSourceFilterVlan = _Ipv6helperSourceFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 21, 1, 1),
    _Ipv6helperSourceFilterVlan_Type()
)
ipv6helperSourceFilterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperSourceFilterVlan.setStatus("current")


class _Ipv6helperSourceFilterVlanStatus_Type(Integer32):
    """Custom type ipv6helperSourceFilterVlanStatus based on Integer32"""
    defaultValue = 2

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


_Ipv6helperSourceFilterVlanStatus_Type.__name__ = "Integer32"
_Ipv6helperSourceFilterVlanStatus_Object = MibTableColumn
ipv6helperSourceFilterVlanStatus = _Ipv6helperSourceFilterVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 1, 2, 21, 1, 2),
    _Ipv6helperSourceFilterVlanStatus_Type()
)
ipv6helperSourceFilterVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6helperSourceFilterVlanStatus.setStatus("current")
_AlcatelIND1UDPRelayMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBConformance = _AlcatelIND1UDPRelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBConformance.setStatus("current")
_AlcatelIND1UDPRelayMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBGroups = _AlcatelIND1UDPRelayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBGroups.setStatus("current")
_AlcatelIND1UDPRelayMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBCompliances = _AlcatelIND1UDPRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBCompliances.setStatus("current")
_AlaDhcpClientTrapsDesc_ObjectIdentity = ObjectIdentity
alaDhcpClientTrapsDesc = _AlaDhcpClientTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 1)
)
_AlaDhcpClientTrapsObj_ObjectIdentity = ObjectIdentity
alaDhcpClientTrapsObj = _AlaDhcpClientTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 2)
)
_AlaDhcpClientAddress_Type = IpAddress
_AlaDhcpClientAddress_Object = MibScalar
alaDhcpClientAddress = _AlaDhcpClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 2, 1),
    _AlaDhcpClientAddress_Type()
)
alaDhcpClientAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpClientAddress.setStatus("current")
_AlaDhcpClientNewAddress_Type = IpAddress
_AlaDhcpClientNewAddress_Object = MibScalar
alaDhcpClientNewAddress = _AlaDhcpClientNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 2, 2),
    _AlaDhcpClientNewAddress_Type()
)
alaDhcpClientNewAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpClientNewAddress.setStatus("current")
_AlaDhcpIsfDropIntervalStartTimeStamp_Type = OctetString
_AlaDhcpIsfDropIntervalStartTimeStamp_Object = MibScalar
alaDhcpIsfDropIntervalStartTimeStamp = _AlaDhcpIsfDropIntervalStartTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 2, 3),
    _AlaDhcpIsfDropIntervalStartTimeStamp_Type()
)
alaDhcpIsfDropIntervalStartTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpIsfDropIntervalStartTimeStamp.setStatus("current")
_AlaDhcpIsfDropIntervalStopTimeStamp_Type = OctetString
_AlaDhcpIsfDropIntervalStopTimeStamp_Object = MibScalar
alaDhcpIsfDropIntervalStopTimeStamp = _AlaDhcpIsfDropIntervalStopTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 2, 4),
    _AlaDhcpIsfDropIntervalStopTimeStamp_Type()
)
alaDhcpIsfDropIntervalStopTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpIsfDropIntervalStopTimeStamp.setStatus("current")
_AlaDhcpIsfDropCount_Type = Integer32
_AlaDhcpIsfDropCount_Object = MibScalar
alaDhcpIsfDropCount = _AlaDhcpIsfDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 2, 5),
    _AlaDhcpIsfDropCount_Type()
)
alaDhcpIsfDropCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpIsfDropCount.setStatus("current")
_AlaDhcpTcamFailMsg_Type = OctetString
_AlaDhcpTcamFailMsg_Object = MibScalar
alaDhcpTcamFailMsg = _AlaDhcpTcamFailMsg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 2, 6),
    _AlaDhcpTcamFailMsg_Type()
)
alaDhcpTcamFailMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpTcamFailMsg.setStatus("current")

# Managed Objects groups

iphelperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 1)
)
iphelperGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperForwAddr"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperAgentInformation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperAgentInformationPolicy"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatType"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperOption82Policy"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperPXESupport"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperService"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperTrafficSuppressionStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperVlan"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingTrapStatus"))
)
if mibBuilder.loadTexts:
    iphelperGroup.setStatus("current")

iphelperStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 2)
)
iphelperStatGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperServerAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperRxFromClient"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperTxToServer"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperMaxHopsViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperForwDelayViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperResetAll"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperAgentInfoViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperInvalidGatewayIP"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperInvalidAgentInfoOptFrmSrver"))
)
if mibBuilder.loadTexts:
    iphelperStatGroup.setStatus("current")

iphelperMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 3)
)
iphelperMiscGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperForwDelay"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperMaxHops"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperForwardOption"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperBootupOption"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperBootupPacketOption"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField1"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField1StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField2"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField2StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField3"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField3StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField4"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField4StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField5"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIField5StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIDelimiter"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnooping"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOpt82DataInsertionStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingMacAddrVerificationStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingTrafficSuppressionStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingDatabaseSyncTimeout"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingDatabaseLastSyncTime"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingDatabaseAction"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBypassOpt82CheckStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingPersistencyStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaMdnsGreTunnelName"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaMdnsAdminStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaMdnsFloodVlans"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingArpAllowStatus"))
)
if mibBuilder.loadTexts:
    iphelperMiscGroup.setStatus("current")

iphelperSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 5)
)
iphelperSourceGroup.setObjects(
    ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSourceFilterVlanFilteringStatus")
)
if mibBuilder.loadTexts:
    iphelperSourceGroup.setStatus("current")

iphelperOption82FormatASCIIConfigurableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 6)
)
iphelperOption82FormatASCIIConfigurableGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus"))
)
if mibBuilder.loadTexts:
    iphelperOption82FormatASCIIConfigurableGroup.setStatus("current")

alaDhcpClientTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 7)
)
alaDhcpClientTrapObjectsGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientNewAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpIsfDropIntervalStartTimeStamp"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpIsfDropIntervalStopTimeStamp"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpIsfDropCount"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpTcamFailMsg"))
)
if mibBuilder.loadTexts:
    alaDhcpClientTrapObjectsGroup.setStatus("current")

iphelperxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 8)
)
iphelperxGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxPortServiceAssociationName"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxPortServiceAssociationPort"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxPortServiceAssociationService"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxPortServiceAssociationStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxServicePortAssociationName"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxServicePortAssociationPort"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxServicePortAssociationService"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxServicePortAssociationStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxStatReset"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxStatRxFromClient"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxStatServerAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxStatService"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxStatTxToServer"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxStatVlan"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxPropertiesName"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxPropertiesPort"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxPropertiesService"))
)
if mibBuilder.loadTexts:
    iphelperxGroup.setStatus("current")

ipv6helperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 9)
)
ipv6helperGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperForwAddr"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperVlan"))
)
if mibBuilder.loadTexts:
    ipv6helperGroup.setStatus("current")

ipv6helperMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 10)
)
ipv6helperMiscGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperMaxHops"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperForwardOption"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnooping"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingBindingStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingBindingDatabaseAction"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingBindingPersistencyStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingVlanNumber"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingVlanStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingPortIfIndex"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperDhcpSnoopingPortTrustMode"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperSnoopingClientViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperSnoopingServerViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperSnoopingBindingViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperSnoopingInterfaceidViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperSnoopingPortSourceFilterStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperBindingLinkLocalAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperBindingIfIndex"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperBindingGlobalIpv6Address"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperBindingVlan"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperBindingLeaseTime"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperBindingRowStatus"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperStatsServerAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperStatsVlan"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperRxFromClient"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperTxToServer"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperMaxHopsViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperResetAll"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperInterfaceIdPrefixValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperRemoteIdFormatType"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperRemoteIdEnterpriseNumber"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperRemoteIdUserStringValue"))
)
if mibBuilder.loadTexts:
    ipv6helperMiscGroup.setStatus("current")

ipv6helperSourceFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 11)
)
ipv6helperSourceFilterGroup.setObjects(
    ("ALCATEL-IND1-UDP-RELAY-MIB", "ipv6helperSourceFilterVlanStatus")
)
if mibBuilder.loadTexts:
    ipv6helperSourceFilterGroup.setStatus("current")


# Notification objects

alaDhcpClientAddressAddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 1, 0, 1)
)
alaDhcpClientAddressAddTrap.setObjects(
    ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddress")
)
if mibBuilder.loadTexts:
    alaDhcpClientAddressAddTrap.setStatus(
        "current"
    )

alaDhcpClientAddressExpiryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 1, 0, 2)
)
alaDhcpClientAddressExpiryTrap.setObjects(
    ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddress")
)
if mibBuilder.loadTexts:
    alaDhcpClientAddressExpiryTrap.setStatus(
        "current"
    )

alaDhcpClientAddressModifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 1, 0, 3)
)
alaDhcpClientAddressModifyTrap.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientNewAddress"))
)
if mibBuilder.loadTexts:
    alaDhcpClientAddressModifyTrap.setStatus(
        "current"
    )

alaDhcpBindingDuplicateEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 1, 0, 4)
)
alaDhcpBindingDuplicateEntry.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingMacAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingVlan"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingIfIndex"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpSnoopingBindingIfIndex"))
)
if mibBuilder.loadTexts:
    alaDhcpBindingDuplicateEntry.setStatus(
        "current"
    )

alaDhcpBindingTcamFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 1, 0, 5)
)
alaDhcpBindingTcamFail.setObjects(
    ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpTcamFailMsg")
)
if mibBuilder.loadTexts:
    alaDhcpBindingTcamFail.setStatus(
        "current"
    )

alaDhcpIsfDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 23, 1, 0, 6)
)
alaDhcpIsfDrop.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpIsfDropIntervalStartTimeStamp"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpIsfDropIntervalStopTimeStamp"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpIsfDropCount"))
)
if mibBuilder.loadTexts:
    alaDhcpIsfDrop.setStatus(
        "current"
    )


# Notifications groups

alaDhcpClientTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 1, 4)
)
alaDhcpClientTrapsGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddressAddTrap"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddressExpiryTrap"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddressModifyTrap"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpBindingDuplicateEntry"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpBindingTcamFail"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpIsfDrop"))
)
if mibBuilder.loadTexts:
    alaDhcpClientTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1UDPRelayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 9, 1, 2, 2, 1)
)
alcatelIND1UDPRelayMIBCompliance.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperGroup"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperStatGroup"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperMiscGroup"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientTrapsGroup"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperSourceGroup"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperOption82FormatASCIIConfigurableGroup"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientTrapObjectsGroup"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperxGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-UDP-RELAY-MIB",
    **{"IphelperServIndex": IphelperServIndex,
       "IphelpereOption82ASCIIFieldType": IphelpereOption82ASCIIFieldType,
       "IphelperOption82CircuitOrRemoteId": IphelperOption82CircuitOrRemoteId,
       "alcatelIND1UDPRelayMIB": alcatelIND1UDPRelayMIB,
       "alcatelIND1UDPRelayMIBObjects": alcatelIND1UDPRelayMIBObjects,
       "iphelperMIB": iphelperMIB,
       "iphelperTable": iphelperTable,
       "iphelperEntry": iphelperEntry,
       "iphelperService": iphelperService,
       "iphelperForwAddr": iphelperForwAddr,
       "iphelperVlan": iphelperVlan,
       "iphelperStatus": iphelperStatus,
       "iphelperStatTable": iphelperStatTable,
       "iphelperStatEntry": iphelperStatEntry,
       "iphelperServerAddress": iphelperServerAddress,
       "iphelperRxFromClient": iphelperRxFromClient,
       "iphelperTxToServer": iphelperTxToServer,
       "iphelperMaxHopsViolation": iphelperMaxHopsViolation,
       "iphelperForwDelayViolation": iphelperForwDelayViolation,
       "iphelperResetAll": iphelperResetAll,
       "iphelperAgentInfoViolation": iphelperAgentInfoViolation,
       "iphelperInvalidGatewayIP": iphelperInvalidGatewayIP,
       "iphelperInvalidAgentInfoOptFrmSrver": iphelperInvalidAgentInfoOptFrmSrver,
       "iphelperForwDelay": iphelperForwDelay,
       "iphelperMaxHops": iphelperMaxHops,
       "iphelperForwardOption": iphelperForwardOption,
       "iphelperBootupOption": iphelperBootupOption,
       "iphelperBootupPacketOption": iphelperBootupPacketOption,
       "iphelperxServicePortAssociationTable": iphelperxServicePortAssociationTable,
       "iphelperxServicePortAssociationEntry": iphelperxServicePortAssociationEntry,
       "iphelperxServicePortAssociationService": iphelperxServicePortAssociationService,
       "iphelperxServicePortAssociationPort": iphelperxServicePortAssociationPort,
       "iphelperxServicePortAssociationName": iphelperxServicePortAssociationName,
       "iphelperxServicePortAssociationStatus": iphelperxServicePortAssociationStatus,
       "iphelperxPortServiceAssociationTable": iphelperxPortServiceAssociationTable,
       "iphelperxPortServiceAssociationEntry": iphelperxPortServiceAssociationEntry,
       "iphelperxPortServiceAssociationService": iphelperxPortServiceAssociationService,
       "iphelperxPortServiceAssociationPort": iphelperxPortServiceAssociationPort,
       "iphelperxPortServiceAssociationName": iphelperxPortServiceAssociationName,
       "iphelperxPortServiceAssociationStatus": iphelperxPortServiceAssociationStatus,
       "iphelperxPropertiesTable": iphelperxPropertiesTable,
       "iphelperxPropertiesEntry": iphelperxPropertiesEntry,
       "iphelperxPropertiesService": iphelperxPropertiesService,
       "iphelperxPropertiesPort": iphelperxPropertiesPort,
       "iphelperxPropertiesName": iphelperxPropertiesName,
       "iphelperxStatTable": iphelperxStatTable,
       "iphelperxStatEntry": iphelperxStatEntry,
       "iphelperxStatService": iphelperxStatService,
       "iphelperxStatServerAddress": iphelperxStatServerAddress,
       "iphelperxStatVlan": iphelperxStatVlan,
       "iphelperxStatRxFromClient": iphelperxStatRxFromClient,
       "iphelperxStatTxToServer": iphelperxStatTxToServer,
       "iphelperxStatReset": iphelperxStatReset,
       "iphelperAgentInformation": iphelperAgentInformation,
       "iphelperAgentInformationPolicy": iphelperAgentInformationPolicy,
       "iphelperDhcpSnoopingVlanTable": iphelperDhcpSnoopingVlanTable,
       "iphelperDhcpSnoopingVlanEntry": iphelperDhcpSnoopingVlanEntry,
       "iphelperDhcpSnoopingVlanNumber": iphelperDhcpSnoopingVlanNumber,
       "iphelperDhcpSnoopingVlanOpt82DataInsertionStatus": iphelperDhcpSnoopingVlanOpt82DataInsertionStatus,
       "iphelperDhcpSnoopingVlanMacAddrVerificationStatus": iphelperDhcpSnoopingVlanMacAddrVerificationStatus,
       "iphelperDhcpSnoopingVlanTrafficSuppressionStatus": iphelperDhcpSnoopingVlanTrafficSuppressionStatus,
       "iphelperDhcpSnoopingVlanStatus": iphelperDhcpSnoopingVlanStatus,
       "iphelperDhcpSnoopingPortTable": iphelperDhcpSnoopingPortTable,
       "iphelperDhcpSnoopingPortEntry": iphelperDhcpSnoopingPortEntry,
       "iphelperDhcpSnoopingPortIfIndex": iphelperDhcpSnoopingPortIfIndex,
       "iphelperDhcpSnoopingPortTrustMode": iphelperDhcpSnoopingPortTrustMode,
       "iphelperDhcpSnoopingPortTrafficSuppression": iphelperDhcpSnoopingPortTrafficSuppression,
       "iphelperDhcpSnoopingPortMacAddrViolation": iphelperDhcpSnoopingPortMacAddrViolation,
       "iphelperDhcpSnoopingPortDhcpServerViolation": iphelperDhcpSnoopingPortDhcpServerViolation,
       "iphelperDhcpSnoopingPortOption82Violation": iphelperDhcpSnoopingPortOption82Violation,
       "iphelperDhcpSnoopingPortRelayAgentViolation": iphelperDhcpSnoopingPortRelayAgentViolation,
       "iphelperDhcpSnoopingPortBindingViolation": iphelperDhcpSnoopingPortBindingViolation,
       "iphelperDhcpSnoopingPortIpSourceFiltering": iphelperDhcpSnoopingPortIpSourceFiltering,
       "iphelperDhcpSnoopingBindingTable": iphelperDhcpSnoopingBindingTable,
       "iphelperDhcpSnoopingBindingEntry": iphelperDhcpSnoopingBindingEntry,
       "iphelperDhcpSnoopingBindingMacAddress": iphelperDhcpSnoopingBindingMacAddress,
       "iphelperDhcpSnoopingBindingIfIndex": iphelperDhcpSnoopingBindingIfIndex,
       "iphelperDhcpSnoopingBindingIpAddress": iphelperDhcpSnoopingBindingIpAddress,
       "iphelperDhcpSnoopingBindingVlan": iphelperDhcpSnoopingBindingVlan,
       "iphelperDhcpSnoopingBindingLeaseTime": iphelperDhcpSnoopingBindingLeaseTime,
       "iphelperDhcpSnoopingBindingType": iphelperDhcpSnoopingBindingType,
       "iphelperDhcpSnoopingBindingRowStatus": iphelperDhcpSnoopingBindingRowStatus,
       "iphelperDhcpSnoopingBindingRemoteFlag": iphelperDhcpSnoopingBindingRemoteFlag,
       "iphelperDhcpSnooping": iphelperDhcpSnooping,
       "iphelperDhcpSnoopingOpt82DataInsertionStatus": iphelperDhcpSnoopingOpt82DataInsertionStatus,
       "iphelperDhcpSnoopingMacAddrVerificationStatus": iphelperDhcpSnoopingMacAddrVerificationStatus,
       "iphelperDhcpSnoopingTrafficSuppressionStatus": iphelperDhcpSnoopingTrafficSuppressionStatus,
       "iphelperDhcpSnoopingBindingStatus": iphelperDhcpSnoopingBindingStatus,
       "iphelperDhcpSnoopingBindingDatabaseSyncTimeout": iphelperDhcpSnoopingBindingDatabaseSyncTimeout,
       "iphelperDhcpSnoopingBindingDatabaseLastSyncTime": iphelperDhcpSnoopingBindingDatabaseLastSyncTime,
       "iphelperDhcpSnoopingBindingDatabaseAction": iphelperDhcpSnoopingBindingDatabaseAction,
       "iphelperTrafficSuppressionStatus": iphelperTrafficSuppressionStatus,
       "iphelperDhcpSnoopingBypassOpt82CheckStatus": iphelperDhcpSnoopingBypassOpt82CheckStatus,
       "iphelperDhcpOption82FormatType": iphelperDhcpOption82FormatType,
       "iphelperDhcpOption82StringValue": iphelperDhcpOption82StringValue,
       "iphelperPXESupport": iphelperPXESupport,
       "iphelperDhcpSnoopingBindingPersistencyStatus": iphelperDhcpSnoopingBindingPersistencyStatus,
       "iphelperDhcpSnoopingOption82FormatASCIIField1": iphelperDhcpSnoopingOption82FormatASCIIField1,
       "iphelperDhcpSnoopingOption82FormatASCIIField1StringValue": iphelperDhcpSnoopingOption82FormatASCIIField1StringValue,
       "iphelperDhcpSnoopingOption82FormatASCIIField2": iphelperDhcpSnoopingOption82FormatASCIIField2,
       "iphelperDhcpSnoopingOption82FormatASCIIField2StringValue": iphelperDhcpSnoopingOption82FormatASCIIField2StringValue,
       "iphelperDhcpSnoopingOption82FormatASCIIField3": iphelperDhcpSnoopingOption82FormatASCIIField3,
       "iphelperDhcpSnoopingOption82FormatASCIIField3StringValue": iphelperDhcpSnoopingOption82FormatASCIIField3StringValue,
       "iphelperDhcpSnoopingOption82FormatASCIIField4": iphelperDhcpSnoopingOption82FormatASCIIField4,
       "iphelperDhcpSnoopingOption82FormatASCIIField4StringValue": iphelperDhcpSnoopingOption82FormatASCIIField4StringValue,
       "iphelperDhcpSnoopingOption82FormatASCIIField5": iphelperDhcpSnoopingOption82FormatASCIIField5,
       "iphelperDhcpSnoopingOption82FormatASCIIField5StringValue": iphelperDhcpSnoopingOption82FormatASCIIField5StringValue,
       "iphelperDhcpSnoopingOption82FormatASCIIDelimiter": iphelperDhcpSnoopingOption82FormatASCIIDelimiter,
       "iphelperDhcpSourceFilterVlanTable": iphelperDhcpSourceFilterVlanTable,
       "iphelperDhcpSourceFilterVlanEntry": iphelperDhcpSourceFilterVlanEntry,
       "iphelperDhcpSourceFilterVlanNumber": iphelperDhcpSourceFilterVlanNumber,
       "iphelperDhcpSourceFilterVlanFilteringStatus": iphelperDhcpSourceFilterVlanFilteringStatus,
       "iphelperOption82Policy": iphelperOption82Policy,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableTable": iphelperDhcpSnoopingOption82FormatASCIIConfigurableTable,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableEntry": iphelperDhcpSnoopingOption82FormatASCIIConfigurableEntry,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex": iphelperDhcpSnoopingOption82FormatASCIIConfigurableIndex,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField1StrVal,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField2StrVal,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField3StrVal,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField4StrVal,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal": iphelperDhcpSnoopingOption82FormatASCIIConfigurableField5StrVal,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter": iphelperDhcpSnoopingOption82FormatASCIIConfigurableDelimiter,
       "iphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus": iphelperDhcpSnoopingOption82FormatASCIIConfigurableStatus,
       "alaMdnsGreTunnelName": alaMdnsGreTunnelName,
       "alaMdnsAdminStatus": alaMdnsAdminStatus,
       "alaMdnsFloodVlans": alaMdnsFloodVlans,
       "iphelperDhcpSourceFilterAllowSubnetTable": iphelperDhcpSourceFilterAllowSubnetTable,
       "iphelperDhcpSourceFilterAllowIpEntry": iphelperDhcpSourceFilterAllowIpEntry,
       "iphelperDhcpSourceFilterExpIpAddress": iphelperDhcpSourceFilterExpIpAddress,
       "iphelperDhcpSourceFilterExpIpMask": iphelperDhcpSourceFilterExpIpMask,
       "iphelperDhcpSourceFilterVlan": iphelperDhcpSourceFilterVlan,
       "iphelperDhcpSourceFilterExpIpStatus": iphelperDhcpSourceFilterExpIpStatus,
       "iphelperDhcpSnoopingTrapStatus": iphelperDhcpSnoopingTrapStatus,
       "iphelperDhcpSnoopingArpAllowStatus": iphelperDhcpSnoopingArpAllowStatus,
       "ipv6helperMIB": ipv6helperMIB,
       "ipv6helperTable": ipv6helperTable,
       "ipv6helperEntry": ipv6helperEntry,
       "ipv6helperForwAddr": ipv6helperForwAddr,
       "ipv6helperVlan": ipv6helperVlan,
       "ipv6helperStatus": ipv6helperStatus,
       "ipv6helperForwardOption": ipv6helperForwardOption,
       "ipv6helperMaxHops": ipv6helperMaxHops,
       "ipv6helperDhcpSnooping": ipv6helperDhcpSnooping,
       "ipv6helperDhcpSnoopingVlanTable": ipv6helperDhcpSnoopingVlanTable,
       "ipv6helperDhcpSnoopingVlanEntry": ipv6helperDhcpSnoopingVlanEntry,
       "ipv6helperDhcpSnoopingVlanNumber": ipv6helperDhcpSnoopingVlanNumber,
       "ipv6helperDhcpSnoopingVlanStatus": ipv6helperDhcpSnoopingVlanStatus,
       "ipv6helperDhcpSnoopingPortTable": ipv6helperDhcpSnoopingPortTable,
       "ipv6helperDhcpSnoopingPortEntry": ipv6helperDhcpSnoopingPortEntry,
       "ipv6helperDhcpSnoopingPortIfIndex": ipv6helperDhcpSnoopingPortIfIndex,
       "ipv6helperDhcpSnoopingPortTrustMode": ipv6helperDhcpSnoopingPortTrustMode,
       "ipv6helperSnoopingClientViolation": ipv6helperSnoopingClientViolation,
       "ipv6helperSnoopingServerViolation": ipv6helperSnoopingServerViolation,
       "ipv6helperSnoopingBindingViolation": ipv6helperSnoopingBindingViolation,
       "ipv6helperSnoopingInterfaceidViolation": ipv6helperSnoopingInterfaceidViolation,
       "ipv6helperSnoopingPortSourceFilterStatus": ipv6helperSnoopingPortSourceFilterStatus,
       "ipv6helperDhcpSnoopingBindingStatus": ipv6helperDhcpSnoopingBindingStatus,
       "ipv6helperDhcpSnoopingBindingTable": ipv6helperDhcpSnoopingBindingTable,
       "ipv6helperDhcpSnoopingBindingEntry": ipv6helperDhcpSnoopingBindingEntry,
       "ipv6helperBindingLinkLocalAddress": ipv6helperBindingLinkLocalAddress,
       "ipv6helperBindingVlan": ipv6helperBindingVlan,
       "ipv6helperBindingIfIndex": ipv6helperBindingIfIndex,
       "ipv6helperBindingGlobalIpv6Address": ipv6helperBindingGlobalIpv6Address,
       "ipv6helperBindingLeaseTime": ipv6helperBindingLeaseTime,
       "ipv6helperBindingRowStatus": ipv6helperBindingRowStatus,
       "ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout": ipv6helperDhcpSnoopingBindingDatabaseSyncTimeout,
       "ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime": ipv6helperDhcpSnoopingBindingDatabaseLastSyncTime,
       "ipv6helperDhcpSnoopingBindingDatabaseAction": ipv6helperDhcpSnoopingBindingDatabaseAction,
       "ipv6helperDhcpSnoopingBindingPersistencyStatus": ipv6helperDhcpSnoopingBindingPersistencyStatus,
       "ipv6helperStatTable": ipv6helperStatTable,
       "ipv6helperStatEntry": ipv6helperStatEntry,
       "ipv6helperStatsServerAddress": ipv6helperStatsServerAddress,
       "ipv6helperStatsVlan": ipv6helperStatsVlan,
       "ipv6helperTxToServer": ipv6helperTxToServer,
       "ipv6helperInterfaceIdPrefixValue": ipv6helperInterfaceIdPrefixValue,
       "ipv6helperRemoteIdEnterpriseNumber": ipv6helperRemoteIdEnterpriseNumber,
       "ipv6helperRemoteIdUserStringValue": ipv6helperRemoteIdUserStringValue,
       "ipv6helperRemoteIdFormatType": ipv6helperRemoteIdFormatType,
       "ipv6helperRxFromClient": ipv6helperRxFromClient,
       "ipv6helperMaxHopsViolation": ipv6helperMaxHopsViolation,
       "ipv6helperResetAll": ipv6helperResetAll,
       "ipv6helperSourceFilterVlanTable": ipv6helperSourceFilterVlanTable,
       "ipv6helperSourceFilterVlanEntry": ipv6helperSourceFilterVlanEntry,
       "ipv6helperSourceFilterVlan": ipv6helperSourceFilterVlan,
       "ipv6helperSourceFilterVlanStatus": ipv6helperSourceFilterVlanStatus,
       "alcatelIND1UDPRelayMIBConformance": alcatelIND1UDPRelayMIBConformance,
       "alcatelIND1UDPRelayMIBGroups": alcatelIND1UDPRelayMIBGroups,
       "iphelperGroup": iphelperGroup,
       "iphelperStatGroup": iphelperStatGroup,
       "iphelperMiscGroup": iphelperMiscGroup,
       "alaDhcpClientTrapsGroup": alaDhcpClientTrapsGroup,
       "iphelperSourceGroup": iphelperSourceGroup,
       "iphelperOption82FormatASCIIConfigurableGroup": iphelperOption82FormatASCIIConfigurableGroup,
       "alaDhcpClientTrapObjectsGroup": alaDhcpClientTrapObjectsGroup,
       "iphelperxGroup": iphelperxGroup,
       "ipv6helperGroup": ipv6helperGroup,
       "ipv6helperMiscGroup": ipv6helperMiscGroup,
       "ipv6helperSourceFilterGroup": ipv6helperSourceFilterGroup,
       "alcatelIND1UDPRelayMIBCompliances": alcatelIND1UDPRelayMIBCompliances,
       "alcatelIND1UDPRelayMIBCompliance": alcatelIND1UDPRelayMIBCompliance,
       "alaDhcpClientTrapsDesc": alaDhcpClientTrapsDesc,
       "alaDhcpClientAddressAddTrap": alaDhcpClientAddressAddTrap,
       "alaDhcpClientAddressExpiryTrap": alaDhcpClientAddressExpiryTrap,
       "alaDhcpClientAddressModifyTrap": alaDhcpClientAddressModifyTrap,
       "alaDhcpBindingDuplicateEntry": alaDhcpBindingDuplicateEntry,
       "alaDhcpBindingTcamFail": alaDhcpBindingTcamFail,
       "alaDhcpIsfDrop": alaDhcpIsfDrop,
       "alaDhcpClientTrapsObj": alaDhcpClientTrapsObj,
       "alaDhcpClientAddress": alaDhcpClientAddress,
       "alaDhcpClientNewAddress": alaDhcpClientNewAddress,
       "alaDhcpIsfDropIntervalStartTimeStamp": alaDhcpIsfDropIntervalStartTimeStamp,
       "alaDhcpIsfDropIntervalStopTimeStamp": alaDhcpIsfDropIntervalStopTimeStamp,
       "alaDhcpIsfDropCount": alaDhcpIsfDropCount,
       "alaDhcpTcamFailMsg": alaDhcpTcamFailMsg}
)
