# SNMP MIB module (PRVT-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-DHCP-MIB

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtDHCPMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105)
)
if mibBuilder.loadTexts:
    prvtDHCPMib.setRevisions(
        ("2005-02-16 00:00",
         "2003-05-06 00:00",
         "2002-05-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtDHCPObjects_ObjectIdentity = ObjectIdentity
prvtDHCPObjects = _PrvtDHCPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1)
)
_DhcpPackets_ObjectIdentity = ObjectIdentity
dhcpPackets = _DhcpPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1)
)
_DhcpStatusTotalNoOfDiscovers_Type = Counter32
_DhcpStatusTotalNoOfDiscovers_Object = MibScalar
dhcpStatusTotalNoOfDiscovers = _DhcpStatusTotalNoOfDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 1),
    _DhcpStatusTotalNoOfDiscovers_Type()
)
dhcpStatusTotalNoOfDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStatusTotalNoOfDiscovers.setStatus("current")
_DhcpStatusTotalNoOfRequests_Type = Counter32
_DhcpStatusTotalNoOfRequests_Object = MibScalar
dhcpStatusTotalNoOfRequests = _DhcpStatusTotalNoOfRequests_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 2),
    _DhcpStatusTotalNoOfRequests_Type()
)
dhcpStatusTotalNoOfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStatusTotalNoOfRequests.setStatus("current")
_DhcpStatusTotalNoOfReleases_Type = Counter32
_DhcpStatusTotalNoOfReleases_Object = MibScalar
dhcpStatusTotalNoOfReleases = _DhcpStatusTotalNoOfReleases_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 3),
    _DhcpStatusTotalNoOfReleases_Type()
)
dhcpStatusTotalNoOfReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStatusTotalNoOfReleases.setStatus("current")
_DhcpStatusTotalNoOfOffers_Type = Counter32
_DhcpStatusTotalNoOfOffers_Object = MibScalar
dhcpStatusTotalNoOfOffers = _DhcpStatusTotalNoOfOffers_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 4),
    _DhcpStatusTotalNoOfOffers_Type()
)
dhcpStatusTotalNoOfOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStatusTotalNoOfOffers.setStatus("current")
_DhcpStatusTotalNoOfAcks_Type = Counter32
_DhcpStatusTotalNoOfAcks_Object = MibScalar
dhcpStatusTotalNoOfAcks = _DhcpStatusTotalNoOfAcks_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 5),
    _DhcpStatusTotalNoOfAcks_Type()
)
dhcpStatusTotalNoOfAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStatusTotalNoOfAcks.setStatus("current")
_DhcpStatusTotalNoOfNacks_Type = Counter32
_DhcpStatusTotalNoOfNacks_Object = MibScalar
dhcpStatusTotalNoOfNacks = _DhcpStatusTotalNoOfNacks_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 6),
    _DhcpStatusTotalNoOfNacks_Type()
)
dhcpStatusTotalNoOfNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStatusTotalNoOfNacks.setStatus("current")
_DhcpStatusTotalNoOfDeclines_Type = Counter32
_DhcpStatusTotalNoOfDeclines_Object = MibScalar
dhcpStatusTotalNoOfDeclines = _DhcpStatusTotalNoOfDeclines_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 7),
    _DhcpStatusTotalNoOfDeclines_Type()
)
dhcpStatusTotalNoOfDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStatusTotalNoOfDeclines.setStatus("current")
_DhcpRanges_ObjectIdentity = ObjectIdentity
dhcpRanges = _DhcpRanges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2)
)
_DhcpRangeTable_Object = MibTable
dhcpRangeTable = _DhcpRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpRangeTable.setStatus("current")
_DhcpRangeEntry_Object = MibTableRow
dhcpRangeEntry = _DhcpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1)
)
dhcpRangeEntry.setIndexNames(
    (0, "PRVT-DHCP-MIB", "dhcpRangeStartIp"),
)
if mibBuilder.loadTexts:
    dhcpRangeEntry.setStatus("current")
_DhcpRangeStartIp_Type = IpAddress
_DhcpRangeStartIp_Object = MibTableColumn
dhcpRangeStartIp = _DhcpRangeStartIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 1),
    _DhcpRangeStartIp_Type()
)
dhcpRangeStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRangeStartIp.setStatus("current")
_DhcpRangeStopIp_Type = IpAddress
_DhcpRangeStopIp_Object = MibTableColumn
dhcpRangeStopIp = _DhcpRangeStopIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 2),
    _DhcpRangeStopIp_Type()
)
dhcpRangeStopIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRangeStopIp.setStatus("current")
_DhcpRangeNoAddInUse_Type = Counter32
_DhcpRangeNoAddInUse_Object = MibTableColumn
dhcpRangeNoAddInUse = _DhcpRangeNoAddInUse_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 3),
    _DhcpRangeNoAddInUse_Type()
)
dhcpRangeNoAddInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeNoAddInUse.setStatus("current")
_DhcpRangeNoAddFree_Type = Counter32
_DhcpRangeNoAddFree_Object = MibTableColumn
dhcpRangeNoAddFree = _DhcpRangeNoAddFree_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 4),
    _DhcpRangeNoAddFree_Type()
)
dhcpRangeNoAddFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeNoAddFree.setStatus("current")
_DhcpRangeCircuitID_Type = DisplayString
_DhcpRangeCircuitID_Object = MibTableColumn
dhcpRangeCircuitID = _DhcpRangeCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 5),
    _DhcpRangeCircuitID_Type()
)
dhcpRangeCircuitID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRangeCircuitID.setStatus("current")


class _DhcpRangeCircuitIDType_Type(Integer32):
    """Custom type dhcpRangeCircuitIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("string", 1),
          ("hex", 2))
    )


_DhcpRangeCircuitIDType_Type.__name__ = "Integer32"
_DhcpRangeCircuitIDType_Object = MibTableColumn
dhcpRangeCircuitIDType = _DhcpRangeCircuitIDType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 6),
    _DhcpRangeCircuitIDType_Type()
)
dhcpRangeCircuitIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRangeCircuitIDType.setStatus("current")
_DhcpRangeRangeName_Type = DisplayString
_DhcpRangeRangeName_Object = MibTableColumn
dhcpRangeRangeName = _DhcpRangeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 7),
    _DhcpRangeRangeName_Type()
)
dhcpRangeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRangeRangeName.setStatus("current")
_DhcpRangeSubnetIp_Type = IpAddress
_DhcpRangeSubnetIp_Object = MibTableColumn
dhcpRangeSubnetIp = _DhcpRangeSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 8),
    _DhcpRangeSubnetIp_Type()
)
dhcpRangeSubnetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeSubnetIp.setStatus("current")
_DhcpRangeSubnetName_Type = DisplayString
_DhcpRangeSubnetName_Object = MibTableColumn
dhcpRangeSubnetName = _DhcpRangeSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 9),
    _DhcpRangeSubnetName_Type()
)
dhcpRangeSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeSubnetName.setStatus("current")
_DhcpRangeRowStatus_Type = RowStatus
_DhcpRangeRowStatus_Object = MibTableColumn
dhcpRangeRowStatus = _DhcpRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 10),
    _DhcpRangeRowStatus_Type()
)
dhcpRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRangeRowStatus.setStatus("current")
_DhcpSubnets_ObjectIdentity = ObjectIdentity
dhcpSubnets = _DhcpSubnets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3)
)
_DhcpSubnetTable_Object = MibTable
dhcpSubnetTable = _DhcpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpSubnetTable.setStatus("current")
_DhcpSubnetEntry_Object = MibTableRow
dhcpSubnetEntry = _DhcpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1)
)
dhcpSubnetEntry.setIndexNames(
    (0, "PRVT-DHCP-MIB", "dhcpSubnetIp"),
)
if mibBuilder.loadTexts:
    dhcpSubnetEntry.setStatus("current")
_DhcpSubnetIp_Type = IpAddress
_DhcpSubnetIp_Object = MibTableColumn
dhcpSubnetIp = _DhcpSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 1),
    _DhcpSubnetIp_Type()
)
dhcpSubnetIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetIp.setStatus("current")
_DhcpSubnetMask_Type = IpAddress
_DhcpSubnetMask_Object = MibTableColumn
dhcpSubnetMask = _DhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 2),
    _DhcpSubnetMask_Type()
)
dhcpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetMask.setStatus("current")
_DhcpSubnetName_Type = DisplayString
_DhcpSubnetName_Object = MibTableColumn
dhcpSubnetName = _DhcpSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 3),
    _DhcpSubnetName_Type()
)
dhcpSubnetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetName.setStatus("current")
_DhcpSubnetNoAddInUse_Type = Counter32
_DhcpSubnetNoAddInUse_Object = MibTableColumn
dhcpSubnetNoAddInUse = _DhcpSubnetNoAddInUse_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 4),
    _DhcpSubnetNoAddInUse_Type()
)
dhcpSubnetNoAddInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetNoAddInUse.setStatus("current")
_DhcpSubnetNoAddFree_Type = Counter32
_DhcpSubnetNoAddFree_Object = MibTableColumn
dhcpSubnetNoAddFree = _DhcpSubnetNoAddFree_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 5),
    _DhcpSubnetNoAddFree_Type()
)
dhcpSubnetNoAddFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetNoAddFree.setStatus("current")
_DhcpSubnetRowStatus_Type = RowStatus
_DhcpSubnetRowStatus_Object = MibTableColumn
dhcpSubnetRowStatus = _DhcpSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 6),
    _DhcpSubnetRowStatus_Type()
)
dhcpSubnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRowStatus.setStatus("current")
_DhcpHosts_ObjectIdentity = ObjectIdentity
dhcpHosts = _DhcpHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4)
)
_DhcpStaticHosts_ObjectIdentity = ObjectIdentity
dhcpStaticHosts = _DhcpStaticHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1)
)
_DhcpStaticHostsTable_Object = MibTable
dhcpStaticHostsTable = _DhcpStaticHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpStaticHostsTable.setStatus("current")
_DhcpStaticHostsEntry_Object = MibTableRow
dhcpStaticHostsEntry = _DhcpStaticHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1)
)
dhcpStaticHostsEntry.setIndexNames(
    (0, "PRVT-DHCP-MIB", "dhcpStaticHostIPAddress"),
)
if mibBuilder.loadTexts:
    dhcpStaticHostsEntry.setStatus("current")
_DhcpStaticHostIPAddress_Type = IpAddress
_DhcpStaticHostIPAddress_Object = MibTableColumn
dhcpStaticHostIPAddress = _DhcpStaticHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 1),
    _DhcpStaticHostIPAddress_Type()
)
dhcpStaticHostIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticHostIPAddress.setStatus("current")
_DhcpStaticHostName_Type = DisplayString
_DhcpStaticHostName_Object = MibTableColumn
dhcpStaticHostName = _DhcpStaticHostName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 2),
    _DhcpStaticHostName_Type()
)
dhcpStaticHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticHostName.setStatus("current")
_DhcpStaticHostConnected_Type = TruthValue
_DhcpStaticHostConnected_Object = MibTableColumn
dhcpStaticHostConnected = _DhcpStaticHostConnected_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 3),
    _DhcpStaticHostConnected_Type()
)
dhcpStaticHostConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticHostConnected.setStatus("current")
_DhcpStaticHostMACAddr_Type = MacAddress
_DhcpStaticHostMACAddr_Object = MibTableColumn
dhcpStaticHostMACAddr = _DhcpStaticHostMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 4),
    _DhcpStaticHostMACAddr_Type()
)
dhcpStaticHostMACAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticHostMACAddr.setStatus("current")
_DhcpStaticHostFilename_Type = DisplayString
_DhcpStaticHostFilename_Object = MibTableColumn
dhcpStaticHostFilename = _DhcpStaticHostFilename_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 5),
    _DhcpStaticHostFilename_Type()
)
dhcpStaticHostFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticHostFilename.setStatus("current")
_DhcpStaticHostBootpIP_Type = IpAddress
_DhcpStaticHostBootpIP_Object = MibTableColumn
dhcpStaticHostBootpIP = _DhcpStaticHostBootpIP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 6),
    _DhcpStaticHostBootpIP_Type()
)
dhcpStaticHostBootpIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticHostBootpIP.setStatus("current")
_DhcpStaticHostServer_Type = DisplayString
_DhcpStaticHostServer_Object = MibTableColumn
dhcpStaticHostServer = _DhcpStaticHostServer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 7),
    _DhcpStaticHostServer_Type()
)
dhcpStaticHostServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticHostServer.setStatus("current")
_DhcpStatisHostSnoofPort_Type = Counter32
_DhcpStatisHostSnoofPort_Object = MibTableColumn
dhcpStatisHostSnoofPort = _DhcpStatisHostSnoofPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 8),
    _DhcpStatisHostSnoofPort_Type()
)
dhcpStatisHostSnoofPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStatisHostSnoofPort.setStatus("current")
_DhcpStaticHostRowStatus_Type = RowStatus
_DhcpStaticHostRowStatus_Object = MibTableColumn
dhcpStaticHostRowStatus = _DhcpStaticHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 9),
    _DhcpStaticHostRowStatus_Type()
)
dhcpStaticHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticHostRowStatus.setStatus("current")
_DhcpDynamicHosts_ObjectIdentity = ObjectIdentity
dhcpDynamicHosts = _DhcpDynamicHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2)
)
_DhcpLeaseStateTable_Object = MibTable
dhcpLeaseStateTable = _DhcpLeaseStateTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpLeaseStateTable.setStatus("current")
_DhcpLeaseStateEntry_Object = MibTableRow
dhcpLeaseStateEntry = _DhcpLeaseStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1)
)
dhcpLeaseStateEntry.setIndexNames(
    (0, "PRVT-DHCP-MIB", "dhcpLeaseIp"),
)
if mibBuilder.loadTexts:
    dhcpLeaseStateEntry.setStatus("current")
_DhcpLeaseIp_Type = IpAddress
_DhcpLeaseIp_Object = MibTableColumn
dhcpLeaseIp = _DhcpLeaseIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 1),
    _DhcpLeaseIp_Type()
)
dhcpLeaseIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseIp.setStatus("current")
_DhcpLeaseName_Type = DisplayString
_DhcpLeaseName_Object = MibTableColumn
dhcpLeaseName = _DhcpLeaseName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 2),
    _DhcpLeaseName_Type()
)
dhcpLeaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseName.setStatus("current")
_DhcpLeaseETime_Type = DisplayString
_DhcpLeaseETime_Object = MibTableColumn
dhcpLeaseETime = _DhcpLeaseETime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 3),
    _DhcpLeaseETime_Type()
)
dhcpLeaseETime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseETime.setStatus("current")
_DhcpLeaseMac_Type = MacAddress
_DhcpLeaseMac_Object = MibTableColumn
dhcpLeaseMac = _DhcpLeaseMac_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 4),
    _DhcpLeaseMac_Type()
)
dhcpLeaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseMac.setStatus("current")
_DhcpLeaseSnoofPort_Type = Counter32
_DhcpLeaseSnoofPort_Object = MibTableColumn
dhcpLeaseSnoofPort = _DhcpLeaseSnoofPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 5),
    _DhcpLeaseSnoofPort_Type()
)
dhcpLeaseSnoofPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseSnoofPort.setStatus("current")
_DhcpOptions_ObjectIdentity = ObjectIdentity
dhcpOptions = _DhcpOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5)
)
_DhcpOptionsTable_Object = MibTable
dhcpOptionsTable = _DhcpOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dhcpOptionsTable.setStatus("current")
_DhcpOptionsEntry_Object = MibTableRow
dhcpOptionsEntry = _DhcpOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1)
)
dhcpOptionsEntry.setIndexNames(
    (0, "PRVT-DHCP-MIB", "dhcpOptionsSubnetIp"),
)
if mibBuilder.loadTexts:
    dhcpOptionsEntry.setStatus("current")
_DhcpOptionsSubnetIp_Type = DisplayString
_DhcpOptionsSubnetIp_Object = MibTableColumn
dhcpOptionsSubnetIp = _DhcpOptionsSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 1),
    _DhcpOptionsSubnetIp_Type()
)
dhcpOptionsSubnetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOptionsSubnetIp.setStatus("current")
_DhcpOptionsMaxLTime_Type = Counter32
_DhcpOptionsMaxLTime_Object = MibTableColumn
dhcpOptionsMaxLTime = _DhcpOptionsMaxLTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 2),
    _DhcpOptionsMaxLTime_Type()
)
dhcpOptionsMaxLTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsMaxLTime.setStatus("current")
_DhcpOptionsDfltLTime_Type = Counter32
_DhcpOptionsDfltLTime_Object = MibTableColumn
dhcpOptionsDfltLTime = _DhcpOptionsDfltLTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 3),
    _DhcpOptionsDfltLTime_Type()
)
dhcpOptionsDfltLTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsDfltLTime.setStatus("current")
_DhcpOptionsRouter_Type = IpAddress
_DhcpOptionsRouter_Object = MibTableColumn
dhcpOptionsRouter = _DhcpOptionsRouter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 4),
    _DhcpOptionsRouter_Type()
)
dhcpOptionsRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsRouter.setStatus("current")
_DhcpOptionsBrcstAddr_Type = IpAddress
_DhcpOptionsBrcstAddr_Object = MibTableColumn
dhcpOptionsBrcstAddr = _DhcpOptionsBrcstAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 5),
    _DhcpOptionsBrcstAddr_Type()
)
dhcpOptionsBrcstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsBrcstAddr.setStatus("current")
_DhcpOptionsSubnetMask_Type = IpAddress
_DhcpOptionsSubnetMask_Object = MibTableColumn
dhcpOptionsSubnetMask = _DhcpOptionsSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 6),
    _DhcpOptionsSubnetMask_Type()
)
dhcpOptionsSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsSubnetMask.setStatus("current")
_DhcpOptionsDomainName_Type = DisplayString
_DhcpOptionsDomainName_Object = MibTableColumn
dhcpOptionsDomainName = _DhcpOptionsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 7),
    _DhcpOptionsDomainName_Type()
)
dhcpOptionsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsDomainName.setStatus("current")
_DhcpOptionsMeritDump_Type = DisplayString
_DhcpOptionsMeritDump_Object = MibTableColumn
dhcpOptionsMeritDump = _DhcpOptionsMeritDump_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 8),
    _DhcpOptionsMeritDump_Type()
)
dhcpOptionsMeritDump.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsMeritDump.setStatus("current")
_DhcpOptionsRootPath_Type = DisplayString
_DhcpOptionsRootPath_Object = MibTableColumn
dhcpOptionsRootPath = _DhcpOptionsRootPath_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 9),
    _DhcpOptionsRootPath_Type()
)
dhcpOptionsRootPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsRootPath.setStatus("current")
_DhcpOptionsBootStSrv_Type = IpAddress
_DhcpOptionsBootStSrv_Object = MibTableColumn
dhcpOptionsBootStSrv = _DhcpOptionsBootStSrv_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 10),
    _DhcpOptionsBootStSrv_Type()
)
dhcpOptionsBootStSrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsBootStSrv.setStatus("current")
_DhcpOptionsBootFileName_Type = DisplayString
_DhcpOptionsBootFileName_Object = MibTableColumn
dhcpOptionsBootFileName = _DhcpOptionsBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 11),
    _DhcpOptionsBootFileName_Type()
)
dhcpOptionsBootFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsBootFileName.setStatus("current")
_DhcpOptionsDNSServer1_Type = IpAddress
_DhcpOptionsDNSServer1_Object = MibTableColumn
dhcpOptionsDNSServer1 = _DhcpOptionsDNSServer1_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 12),
    _DhcpOptionsDNSServer1_Type()
)
dhcpOptionsDNSServer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsDNSServer1.setStatus("current")
_DhcpOptionsDNSServer2_Type = IpAddress
_DhcpOptionsDNSServer2_Object = MibTableColumn
dhcpOptionsDNSServer2 = _DhcpOptionsDNSServer2_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 13),
    _DhcpOptionsDNSServer2_Type()
)
dhcpOptionsDNSServer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsDNSServer2.setStatus("current")
_DhcpOptionsDNSServer3_Type = IpAddress
_DhcpOptionsDNSServer3_Object = MibTableColumn
dhcpOptionsDNSServer3 = _DhcpOptionsDNSServer3_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 14),
    _DhcpOptionsDNSServer3_Type()
)
dhcpOptionsDNSServer3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsDNSServer3.setStatus("current")
_DhcpOptionsDNSServer4_Type = IpAddress
_DhcpOptionsDNSServer4_Object = MibTableColumn
dhcpOptionsDNSServer4 = _DhcpOptionsDNSServer4_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 15),
    _DhcpOptionsDNSServer4_Type()
)
dhcpOptionsDNSServer4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsDNSServer4.setStatus("current")
_DhcpOptionsDNSServer5_Type = IpAddress
_DhcpOptionsDNSServer5_Object = MibTableColumn
dhcpOptionsDNSServer5 = _DhcpOptionsDNSServer5_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 16),
    _DhcpOptionsDNSServer5_Type()
)
dhcpOptionsDNSServer5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsDNSServer5.setStatus("current")
_DhcpOptionsLogServer1_Type = IpAddress
_DhcpOptionsLogServer1_Object = MibTableColumn
dhcpOptionsLogServer1 = _DhcpOptionsLogServer1_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 17),
    _DhcpOptionsLogServer1_Type()
)
dhcpOptionsLogServer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsLogServer1.setStatus("current")
_DhcpOptionsLogServer2_Type = IpAddress
_DhcpOptionsLogServer2_Object = MibTableColumn
dhcpOptionsLogServer2 = _DhcpOptionsLogServer2_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 18),
    _DhcpOptionsLogServer2_Type()
)
dhcpOptionsLogServer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsLogServer2.setStatus("current")
_DhcpOptionsLogServer3_Type = IpAddress
_DhcpOptionsLogServer3_Object = MibTableColumn
dhcpOptionsLogServer3 = _DhcpOptionsLogServer3_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 19),
    _DhcpOptionsLogServer3_Type()
)
dhcpOptionsLogServer3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsLogServer3.setStatus("current")
_DhcpOptionsLogServer4_Type = IpAddress
_DhcpOptionsLogServer4_Object = MibTableColumn
dhcpOptionsLogServer4 = _DhcpOptionsLogServer4_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 20),
    _DhcpOptionsLogServer4_Type()
)
dhcpOptionsLogServer4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsLogServer4.setStatus("current")
_DhcpOptionsLogServer5_Type = IpAddress
_DhcpOptionsLogServer5_Object = MibTableColumn
dhcpOptionsLogServer5 = _DhcpOptionsLogServer5_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 21),
    _DhcpOptionsLogServer5_Type()
)
dhcpOptionsLogServer5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsLogServer5.setStatus("current")
_DhcpOptionsWinsServer1_Type = IpAddress
_DhcpOptionsWinsServer1_Object = MibTableColumn
dhcpOptionsWinsServer1 = _DhcpOptionsWinsServer1_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 22),
    _DhcpOptionsWinsServer1_Type()
)
dhcpOptionsWinsServer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsWinsServer1.setStatus("current")
_DhcpOptionsWinsServer2_Type = IpAddress
_DhcpOptionsWinsServer2_Object = MibTableColumn
dhcpOptionsWinsServer2 = _DhcpOptionsWinsServer2_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 23),
    _DhcpOptionsWinsServer2_Type()
)
dhcpOptionsWinsServer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsWinsServer2.setStatus("current")
_DhcpOptionsWinsServer3_Type = IpAddress
_DhcpOptionsWinsServer3_Object = MibTableColumn
dhcpOptionsWinsServer3 = _DhcpOptionsWinsServer3_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 24),
    _DhcpOptionsWinsServer3_Type()
)
dhcpOptionsWinsServer3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsWinsServer3.setStatus("current")
_DhcpOptionsWinsServer4_Type = IpAddress
_DhcpOptionsWinsServer4_Object = MibTableColumn
dhcpOptionsWinsServer4 = _DhcpOptionsWinsServer4_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 25),
    _DhcpOptionsWinsServer4_Type()
)
dhcpOptionsWinsServer4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsWinsServer4.setStatus("current")
_DhcpOptionsWinsServer5_Type = IpAddress
_DhcpOptionsWinsServer5_Object = MibTableColumn
dhcpOptionsWinsServer5 = _DhcpOptionsWinsServer5_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 26),
    _DhcpOptionsWinsServer5_Type()
)
dhcpOptionsWinsServer5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOptionsWinsServer5.setStatus("current")
_DhcpPorts_ObjectIdentity = ObjectIdentity
dhcpPorts = _DhcpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6)
)
_DhcpPortTable_Object = MibTable
dhcpPortTable = _DhcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dhcpPortTable.setStatus("current")
_DhcpPortEntry_Object = MibTableRow
dhcpPortEntry = _DhcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1)
)
dhcpPortEntry.setIndexNames(
    (0, "PRVT-DHCP-MIB", "dhcpPort"),
)
if mibBuilder.loadTexts:
    dhcpPortEntry.setStatus("current")


class _DhcpPort_Type(Integer32):
    """Custom type dhcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpPort_Type.__name__ = "Integer32"
_DhcpPort_Object = MibTableColumn
dhcpPort = _DhcpPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 1),
    _DhcpPort_Type()
)
dhcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPort.setStatus("current")
_DhcpMaxPortIP_Type = Counter32
_DhcpMaxPortIP_Object = MibTableColumn
dhcpMaxPortIP = _DhcpMaxPortIP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 2),
    _DhcpMaxPortIP_Type()
)
dhcpMaxPortIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpMaxPortIP.setStatus("current")
_DhcpPortSnoof_Type = TruthValue
_DhcpPortSnoof_Object = MibTableColumn
dhcpPortSnoof = _DhcpPortSnoof_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 3),
    _DhcpPortSnoof_Type()
)
dhcpPortSnoof.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpPortSnoof.setStatus("current")
_DhcpPortServiceEnable_Type = TruthValue
_DhcpPortServiceEnable_Object = MibTableColumn
dhcpPortServiceEnable = _DhcpPortServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 4),
    _DhcpPortServiceEnable_Type()
)
dhcpPortServiceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpPortServiceEnable.setStatus("current")
_DhcpVlans_ObjectIdentity = ObjectIdentity
dhcpVlans = _DhcpVlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7)
)
_DhcpVlanTable_Object = MibTable
dhcpVlanTable = _DhcpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1)
)
if mibBuilder.loadTexts:
    dhcpVlanTable.setStatus("current")
_DhcpVlanEntry_Object = MibTableRow
dhcpVlanEntry = _DhcpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1, 1)
)
dhcpVlanEntry.setIndexNames(
    (0, "PRVT-DHCP-MIB", "dhcpVlanID"),
)
if mibBuilder.loadTexts:
    dhcpVlanEntry.setStatus("current")
_DhcpVlanID_Type = Unsigned32
_DhcpVlanID_Object = MibTableColumn
dhcpVlanID = _DhcpVlanID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1, 1, 1),
    _DhcpVlanID_Type()
)
dhcpVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpVlanID.setStatus("current")
_DhcpVlanEnable_Type = TruthValue
_DhcpVlanEnable_Object = MibTableColumn
dhcpVlanEnable = _DhcpVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1, 1, 2),
    _DhcpVlanEnable_Type()
)
dhcpVlanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpVlanEnable.setStatus("current")
_DhcpMiscSettings_ObjectIdentity = ObjectIdentity
dhcpMiscSettings = _DhcpMiscSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8)
)
_DhcpDBExpire_Type = Counter32
_DhcpDBExpire_Object = MibScalar
dhcpDBExpire = _DhcpDBExpire_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 1),
    _DhcpDBExpire_Type()
)
dhcpDBExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpDBExpire.setStatus("current")
_DhcpTFTPServer_Type = IpAddress
_DhcpTFTPServer_Object = MibScalar
dhcpTFTPServer = _DhcpTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 2),
    _DhcpTFTPServer_Type()
)
dhcpTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpTFTPServer.setStatus("current")
_DhcpFTPServer_Type = IpAddress
_DhcpFTPServer_Object = MibScalar
dhcpFTPServer = _DhcpFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 3),
    _DhcpFTPServer_Type()
)
dhcpFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFTPServer.setStatus("current")
_DhcpFTPServerUser_Type = DisplayString
_DhcpFTPServerUser_Object = MibScalar
dhcpFTPServerUser = _DhcpFTPServerUser_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 4),
    _DhcpFTPServerUser_Type()
)
dhcpFTPServerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFTPServerUser.setStatus("current")
_DhcpFTPServerPass_Type = DisplayString
_DhcpFTPServerPass_Object = MibScalar
dhcpFTPServerPass = _DhcpFTPServerPass_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 5),
    _DhcpFTPServerPass_Type()
)
dhcpFTPServerPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFTPServerPass.setStatus("current")
_DhcpRemoteDBDelay_Type = Counter32
_DhcpRemoteDBDelay_Object = MibScalar
dhcpRemoteDBDelay = _DhcpRemoteDBDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 6),
    _DhcpRemoteDBDelay_Type()
)
dhcpRemoteDBDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRemoteDBDelay.setStatus("current")
_DhcpRemoteDBFilename_Type = DisplayString
_DhcpRemoteDBFilename_Object = MibScalar
dhcpRemoteDBFilename = _DhcpRemoteDBFilename_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 7),
    _DhcpRemoteDBFilename_Type()
)
dhcpRemoteDBFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRemoteDBFilename.setStatus("current")


class _DhcpUnknownCircuitIDPolicy_Type(Integer32):
    """Custom type dhcpUnknownCircuitIDPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_DhcpUnknownCircuitIDPolicy_Type.__name__ = "Integer32"
_DhcpUnknownCircuitIDPolicy_Object = MibScalar
dhcpUnknownCircuitIDPolicy = _DhcpUnknownCircuitIDPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 8),
    _DhcpUnknownCircuitIDPolicy_Type()
)
dhcpUnknownCircuitIDPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpUnknownCircuitIDPolicy.setStatus("current")


class _DhcpEnableServer_Type(Integer32):
    """Custom type dhcpEnableServer based on Integer32"""
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


_DhcpEnableServer_Type.__name__ = "Integer32"
_DhcpEnableServer_Object = MibScalar
dhcpEnableServer = _DhcpEnableServer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 9),
    _DhcpEnableServer_Type()
)
dhcpEnableServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpEnableServer.setStatus("current")
_DhcpRRSettings_ObjectIdentity = ObjectIdentity
dhcpRRSettings = _DhcpRRSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9)
)
_DhcpRRTable_Object = MibTable
dhcpRRTable = _DhcpRRTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1)
)
if mibBuilder.loadTexts:
    dhcpRRTable.setStatus("current")
_DhcpRREntry_Object = MibTableRow
dhcpRREntry = _DhcpRREntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1, 1)
)
dhcpRREntry.setIndexNames(
    (0, "PRVT-DHCP-MIB", "dhcpRRif"),
)
if mibBuilder.loadTexts:
    dhcpRREntry.setStatus("current")
_DhcpRRif_Type = DisplayString
_DhcpRRif_Object = MibTableColumn
dhcpRRif = _DhcpRRif_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1, 1, 1),
    _DhcpRRif_Type()
)
dhcpRRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRRif.setStatus("current")
_DhcpRREnable_Type = TruthValue
_DhcpRREnable_Object = MibTableColumn
dhcpRREnable = _DhcpRREnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1, 1, 2),
    _DhcpRREnable_Type()
)
dhcpRREnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRREnable.setStatus("current")
_PrvtDHCPNotifications_ObjectIdentity = ObjectIdentity
prvtDHCPNotifications = _PrvtDHCPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-DHCP-MIB",
    **{"prvtDHCPMib": prvtDHCPMib,
       "prvtDHCPObjects": prvtDHCPObjects,
       "dhcpPackets": dhcpPackets,
       "dhcpStatusTotalNoOfDiscovers": dhcpStatusTotalNoOfDiscovers,
       "dhcpStatusTotalNoOfRequests": dhcpStatusTotalNoOfRequests,
       "dhcpStatusTotalNoOfReleases": dhcpStatusTotalNoOfReleases,
       "dhcpStatusTotalNoOfOffers": dhcpStatusTotalNoOfOffers,
       "dhcpStatusTotalNoOfAcks": dhcpStatusTotalNoOfAcks,
       "dhcpStatusTotalNoOfNacks": dhcpStatusTotalNoOfNacks,
       "dhcpStatusTotalNoOfDeclines": dhcpStatusTotalNoOfDeclines,
       "dhcpRanges": dhcpRanges,
       "dhcpRangeTable": dhcpRangeTable,
       "dhcpRangeEntry": dhcpRangeEntry,
       "dhcpRangeStartIp": dhcpRangeStartIp,
       "dhcpRangeStopIp": dhcpRangeStopIp,
       "dhcpRangeNoAddInUse": dhcpRangeNoAddInUse,
       "dhcpRangeNoAddFree": dhcpRangeNoAddFree,
       "dhcpRangeCircuitID": dhcpRangeCircuitID,
       "dhcpRangeCircuitIDType": dhcpRangeCircuitIDType,
       "dhcpRangeRangeName": dhcpRangeRangeName,
       "dhcpRangeSubnetIp": dhcpRangeSubnetIp,
       "dhcpRangeSubnetName": dhcpRangeSubnetName,
       "dhcpRangeRowStatus": dhcpRangeRowStatus,
       "dhcpSubnets": dhcpSubnets,
       "dhcpSubnetTable": dhcpSubnetTable,
       "dhcpSubnetEntry": dhcpSubnetEntry,
       "dhcpSubnetIp": dhcpSubnetIp,
       "dhcpSubnetMask": dhcpSubnetMask,
       "dhcpSubnetName": dhcpSubnetName,
       "dhcpSubnetNoAddInUse": dhcpSubnetNoAddInUse,
       "dhcpSubnetNoAddFree": dhcpSubnetNoAddFree,
       "dhcpSubnetRowStatus": dhcpSubnetRowStatus,
       "dhcpHosts": dhcpHosts,
       "dhcpStaticHosts": dhcpStaticHosts,
       "dhcpStaticHostsTable": dhcpStaticHostsTable,
       "dhcpStaticHostsEntry": dhcpStaticHostsEntry,
       "dhcpStaticHostIPAddress": dhcpStaticHostIPAddress,
       "dhcpStaticHostName": dhcpStaticHostName,
       "dhcpStaticHostConnected": dhcpStaticHostConnected,
       "dhcpStaticHostMACAddr": dhcpStaticHostMACAddr,
       "dhcpStaticHostFilename": dhcpStaticHostFilename,
       "dhcpStaticHostBootpIP": dhcpStaticHostBootpIP,
       "dhcpStaticHostServer": dhcpStaticHostServer,
       "dhcpStatisHostSnoofPort": dhcpStatisHostSnoofPort,
       "dhcpStaticHostRowStatus": dhcpStaticHostRowStatus,
       "dhcpDynamicHosts": dhcpDynamicHosts,
       "dhcpLeaseStateTable": dhcpLeaseStateTable,
       "dhcpLeaseStateEntry": dhcpLeaseStateEntry,
       "dhcpLeaseIp": dhcpLeaseIp,
       "dhcpLeaseName": dhcpLeaseName,
       "dhcpLeaseETime": dhcpLeaseETime,
       "dhcpLeaseMac": dhcpLeaseMac,
       "dhcpLeaseSnoofPort": dhcpLeaseSnoofPort,
       "dhcpOptions": dhcpOptions,
       "dhcpOptionsTable": dhcpOptionsTable,
       "dhcpOptionsEntry": dhcpOptionsEntry,
       "dhcpOptionsSubnetIp": dhcpOptionsSubnetIp,
       "dhcpOptionsMaxLTime": dhcpOptionsMaxLTime,
       "dhcpOptionsDfltLTime": dhcpOptionsDfltLTime,
       "dhcpOptionsRouter": dhcpOptionsRouter,
       "dhcpOptionsBrcstAddr": dhcpOptionsBrcstAddr,
       "dhcpOptionsSubnetMask": dhcpOptionsSubnetMask,
       "dhcpOptionsDomainName": dhcpOptionsDomainName,
       "dhcpOptionsMeritDump": dhcpOptionsMeritDump,
       "dhcpOptionsRootPath": dhcpOptionsRootPath,
       "dhcpOptionsBootStSrv": dhcpOptionsBootStSrv,
       "dhcpOptionsBootFileName": dhcpOptionsBootFileName,
       "dhcpOptionsDNSServer1": dhcpOptionsDNSServer1,
       "dhcpOptionsDNSServer2": dhcpOptionsDNSServer2,
       "dhcpOptionsDNSServer3": dhcpOptionsDNSServer3,
       "dhcpOptionsDNSServer4": dhcpOptionsDNSServer4,
       "dhcpOptionsDNSServer5": dhcpOptionsDNSServer5,
       "dhcpOptionsLogServer1": dhcpOptionsLogServer1,
       "dhcpOptionsLogServer2": dhcpOptionsLogServer2,
       "dhcpOptionsLogServer3": dhcpOptionsLogServer3,
       "dhcpOptionsLogServer4": dhcpOptionsLogServer4,
       "dhcpOptionsLogServer5": dhcpOptionsLogServer5,
       "dhcpOptionsWinsServer1": dhcpOptionsWinsServer1,
       "dhcpOptionsWinsServer2": dhcpOptionsWinsServer2,
       "dhcpOptionsWinsServer3": dhcpOptionsWinsServer3,
       "dhcpOptionsWinsServer4": dhcpOptionsWinsServer4,
       "dhcpOptionsWinsServer5": dhcpOptionsWinsServer5,
       "dhcpPorts": dhcpPorts,
       "dhcpPortTable": dhcpPortTable,
       "dhcpPortEntry": dhcpPortEntry,
       "dhcpPort": dhcpPort,
       "dhcpMaxPortIP": dhcpMaxPortIP,
       "dhcpPortSnoof": dhcpPortSnoof,
       "dhcpPortServiceEnable": dhcpPortServiceEnable,
       "dhcpVlans": dhcpVlans,
       "dhcpVlanTable": dhcpVlanTable,
       "dhcpVlanEntry": dhcpVlanEntry,
       "dhcpVlanID": dhcpVlanID,
       "dhcpVlanEnable": dhcpVlanEnable,
       "dhcpMiscSettings": dhcpMiscSettings,
       "dhcpDBExpire": dhcpDBExpire,
       "dhcpTFTPServer": dhcpTFTPServer,
       "dhcpFTPServer": dhcpFTPServer,
       "dhcpFTPServerUser": dhcpFTPServerUser,
       "dhcpFTPServerPass": dhcpFTPServerPass,
       "dhcpRemoteDBDelay": dhcpRemoteDBDelay,
       "dhcpRemoteDBFilename": dhcpRemoteDBFilename,
       "dhcpUnknownCircuitIDPolicy": dhcpUnknownCircuitIDPolicy,
       "dhcpEnableServer": dhcpEnableServer,
       "dhcpRRSettings": dhcpRRSettings,
       "dhcpRRTable": dhcpRRTable,
       "dhcpRREntry": dhcpRREntry,
       "dhcpRRif": dhcpRRif,
       "dhcpRREnable": dhcpRREnable,
       "prvtDHCPNotifications": prvtDHCPNotifications}
)
