# SNMP MIB module (JUNIPER-WIRELESS-WAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\juniper\junos\JUNIPER-WIRELESS-WAN-MIB

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

(jnxWirelessWANStatusMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxWirelessWANStatusMibRoot")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

jnxWirelessWANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1)
)
if mibBuilder.loadTexts:
    jnxWirelessWANMIB.setRevisions(
        ("2018-04-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxWirelessWANNetworkObjects_ObjectIdentity = ObjectIdentity
jnxWirelessWANNetworkObjects = _JnxWirelessWANNetworkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1)
)
_JnxWirelessWANNetworkInfoTable_Object = MibTable
jnxWirelessWANNetworkInfoTable = _JnxWirelessWANNetworkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoTable.setStatus("current")
_JnxWirelessWANNetworkInfoEntry_Object = MibTableRow
jnxWirelessWANNetworkInfoEntry = _JnxWirelessWANNetworkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1)
)
jnxWirelessWANNetworkInfoEntry.setIndexNames(
    (0, "JUNIPER-WIRELESS-WAN-MIB", "jnxWirelessWANNetworkInfoIfdIndex"),
)
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoEntry.setStatus("current")
_JnxWirelessWANNetworkInfoIfdIndex_Type = Counter32
_JnxWirelessWANNetworkInfoIfdIndex_Object = MibTableColumn
jnxWirelessWANNetworkInfoIfdIndex = _JnxWirelessWANNetworkInfoIfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 1),
    _JnxWirelessWANNetworkInfoIfdIndex_Type()
)
jnxWirelessWANNetworkInfoIfdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoIfdIndex.setStatus("current")
_JnxWirelessWANNetworkInfoConnectTime_Type = Counter32
_JnxWirelessWANNetworkInfoConnectTime_Object = MibTableColumn
jnxWirelessWANNetworkInfoConnectTime = _JnxWirelessWANNetworkInfoConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 2),
    _JnxWirelessWANNetworkInfoConnectTime_Type()
)
jnxWirelessWANNetworkInfoConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoConnectTime.setStatus("current")
_JnxWirelessWANNetworkInfoIP_Type = IpAddress
_JnxWirelessWANNetworkInfoIP_Object = MibTableColumn
jnxWirelessWANNetworkInfoIP = _JnxWirelessWANNetworkInfoIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 3),
    _JnxWirelessWANNetworkInfoIP_Type()
)
jnxWirelessWANNetworkInfoIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoIP.setStatus("current")
_JnxWirelessWANNetworkInfoGateway_Type = IpAddress
_JnxWirelessWANNetworkInfoGateway_Object = MibTableColumn
jnxWirelessWANNetworkInfoGateway = _JnxWirelessWANNetworkInfoGateway_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 4),
    _JnxWirelessWANNetworkInfoGateway_Type()
)
jnxWirelessWANNetworkInfoGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoGateway.setStatus("current")
_JnxWirelessWANNetworkInfoDNS_Type = IpAddress
_JnxWirelessWANNetworkInfoDNS_Object = MibTableColumn
jnxWirelessWANNetworkInfoDNS = _JnxWirelessWANNetworkInfoDNS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 5),
    _JnxWirelessWANNetworkInfoDNS_Type()
)
jnxWirelessWANNetworkInfoDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoDNS.setStatus("current")
_JnxWirelessWANNetworkInfoIPv6_Type = DisplayString
_JnxWirelessWANNetworkInfoIPv6_Object = MibTableColumn
jnxWirelessWANNetworkInfoIPv6 = _JnxWirelessWANNetworkInfoIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 6),
    _JnxWirelessWANNetworkInfoIPv6_Type()
)
jnxWirelessWANNetworkInfoIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoIPv6.setStatus("current")
_JnxWirelessWANNetworkInfoIPv6Gateway_Type = DisplayString
_JnxWirelessWANNetworkInfoIPv6Gateway_Object = MibTableColumn
jnxWirelessWANNetworkInfoIPv6Gateway = _JnxWirelessWANNetworkInfoIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 7),
    _JnxWirelessWANNetworkInfoIPv6Gateway_Type()
)
jnxWirelessWANNetworkInfoIPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoIPv6Gateway.setStatus("current")
_JnxWirelessWANNetworkInfoIPv6DNS_Type = DisplayString
_JnxWirelessWANNetworkInfoIPv6DNS_Object = MibTableColumn
jnxWirelessWANNetworkInfoIPv6DNS = _JnxWirelessWANNetworkInfoIPv6DNS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 8),
    _JnxWirelessWANNetworkInfoIPv6DNS_Type()
)
jnxWirelessWANNetworkInfoIPv6DNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoIPv6DNS.setStatus("current")
_JnxWirelessWANNetworkInfoInputbps_Type = Counter32
_JnxWirelessWANNetworkInfoInputbps_Object = MibTableColumn
jnxWirelessWANNetworkInfoInputbps = _JnxWirelessWANNetworkInfoInputbps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 9),
    _JnxWirelessWANNetworkInfoInputbps_Type()
)
jnxWirelessWANNetworkInfoInputbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoInputbps.setStatus("current")
_JnxWirelessWANNetworkInfoOutputbps_Type = Counter32
_JnxWirelessWANNetworkInfoOutputbps_Object = MibTableColumn
jnxWirelessWANNetworkInfoOutputbps = _JnxWirelessWANNetworkInfoOutputbps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 10),
    _JnxWirelessWANNetworkInfoOutputbps_Type()
)
jnxWirelessWANNetworkInfoOutputbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoOutputbps.setStatus("current")
_JnxWirelessWANNetworkInfoBytesReceived_Type = Counter64
_JnxWirelessWANNetworkInfoBytesReceived_Object = MibTableColumn
jnxWirelessWANNetworkInfoBytesReceived = _JnxWirelessWANNetworkInfoBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 11),
    _JnxWirelessWANNetworkInfoBytesReceived_Type()
)
jnxWirelessWANNetworkInfoBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoBytesReceived.setStatus("current")
_JnxWirelessWANNetworkInfoBytesTransferred_Type = Counter64
_JnxWirelessWANNetworkInfoBytesTransferred_Object = MibTableColumn
jnxWirelessWANNetworkInfoBytesTransferred = _JnxWirelessWANNetworkInfoBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 12),
    _JnxWirelessWANNetworkInfoBytesTransferred_Type()
)
jnxWirelessWANNetworkInfoBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoBytesTransferred.setStatus("current")
_JnxWirelessWANNetworkInfoPacketsReceived_Type = Counter64
_JnxWirelessWANNetworkInfoPacketsReceived_Object = MibTableColumn
jnxWirelessWANNetworkInfoPacketsReceived = _JnxWirelessWANNetworkInfoPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 13),
    _JnxWirelessWANNetworkInfoPacketsReceived_Type()
)
jnxWirelessWANNetworkInfoPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoPacketsReceived.setStatus("current")
_JnxWirelessWANNetworkInfoPacketsTransferred_Type = Counter64
_JnxWirelessWANNetworkInfoPacketsTransferred_Object = MibTableColumn
jnxWirelessWANNetworkInfoPacketsTransferred = _JnxWirelessWANNetworkInfoPacketsTransferred_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 14),
    _JnxWirelessWANNetworkInfoPacketsTransferred_Type()
)
jnxWirelessWANNetworkInfoPacketsTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoPacketsTransferred.setStatus("current")
_JnxWirelessWANNetworkInfoCurrentModemStatus_Type = DisplayString
_JnxWirelessWANNetworkInfoCurrentModemStatus_Object = MibTableColumn
jnxWirelessWANNetworkInfoCurrentModemStatus = _JnxWirelessWANNetworkInfoCurrentModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 15),
    _JnxWirelessWANNetworkInfoCurrentModemStatus_Type()
)
jnxWirelessWANNetworkInfoCurrentModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoCurrentModemStatus.setStatus("current")
_JnxWirelessWANNetworkInfoCurrentServiceStatus_Type = DisplayString
_JnxWirelessWANNetworkInfoCurrentServiceStatus_Object = MibTableColumn
jnxWirelessWANNetworkInfoCurrentServiceStatus = _JnxWirelessWANNetworkInfoCurrentServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 16),
    _JnxWirelessWANNetworkInfoCurrentServiceStatus_Type()
)
jnxWirelessWANNetworkInfoCurrentServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoCurrentServiceStatus.setStatus("current")
_JnxWirelessWANNetworkInfoCurrentServiceType_Type = DisplayString
_JnxWirelessWANNetworkInfoCurrentServiceType_Object = MibTableColumn
jnxWirelessWANNetworkInfoCurrentServiceType = _JnxWirelessWANNetworkInfoCurrentServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 17),
    _JnxWirelessWANNetworkInfoCurrentServiceType_Type()
)
jnxWirelessWANNetworkInfoCurrentServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoCurrentServiceType.setStatus("current")
_JnxWirelessWANNetworkInfoCurrentServiceMode_Type = DisplayString
_JnxWirelessWANNetworkInfoCurrentServiceMode_Object = MibTableColumn
jnxWirelessWANNetworkInfoCurrentServiceMode = _JnxWirelessWANNetworkInfoCurrentServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 18),
    _JnxWirelessWANNetworkInfoCurrentServiceMode_Type()
)
jnxWirelessWANNetworkInfoCurrentServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoCurrentServiceMode.setStatus("current")
_JnxWirelessWANNetworkInfoCurrentBand_Type = DisplayString
_JnxWirelessWANNetworkInfoCurrentBand_Object = MibTableColumn
jnxWirelessWANNetworkInfoCurrentBand = _JnxWirelessWANNetworkInfoCurrentBand_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 19),
    _JnxWirelessWANNetworkInfoCurrentBand_Type()
)
jnxWirelessWANNetworkInfoCurrentBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoCurrentBand.setStatus("current")
_JnxWirelessWANNetworkInfoNetwork_Type = DisplayString
_JnxWirelessWANNetworkInfoNetwork_Object = MibTableColumn
jnxWirelessWANNetworkInfoNetwork = _JnxWirelessWANNetworkInfoNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 20),
    _JnxWirelessWANNetworkInfoNetwork_Type()
)
jnxWirelessWANNetworkInfoNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoNetwork.setStatus("current")
_JnxWirelessWANNetworkInfoMCC_Type = Counter32
_JnxWirelessWANNetworkInfoMCC_Object = MibTableColumn
jnxWirelessWANNetworkInfoMCC = _JnxWirelessWANNetworkInfoMCC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 21),
    _JnxWirelessWANNetworkInfoMCC_Type()
)
jnxWirelessWANNetworkInfoMCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoMCC.setStatus("current")
_JnxWirelessWANNetworkInfoMNC_Type = Counter32
_JnxWirelessWANNetworkInfoMNC_Object = MibTableColumn
jnxWirelessWANNetworkInfoMNC = _JnxWirelessWANNetworkInfoMNC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 22),
    _JnxWirelessWANNetworkInfoMNC_Type()
)
jnxWirelessWANNetworkInfoMNC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoMNC.setStatus("current")
_JnxWirelessWANNetworkInfoLAC_Type = Counter32
_JnxWirelessWANNetworkInfoLAC_Object = MibTableColumn
jnxWirelessWANNetworkInfoLAC = _JnxWirelessWANNetworkInfoLAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 23),
    _JnxWirelessWANNetworkInfoLAC_Type()
)
jnxWirelessWANNetworkInfoLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoLAC.setStatus("current")
_JnxWirelessWANNetworkInfoRAC_Type = Counter32
_JnxWirelessWANNetworkInfoRAC_Object = MibTableColumn
jnxWirelessWANNetworkInfoRAC = _JnxWirelessWANNetworkInfoRAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 24),
    _JnxWirelessWANNetworkInfoRAC_Type()
)
jnxWirelessWANNetworkInfoRAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoRAC.setStatus("current")
_JnxWirelessWANNetworkInfoCellIdentification_Type = Counter32
_JnxWirelessWANNetworkInfoCellIdentification_Object = MibTableColumn
jnxWirelessWANNetworkInfoCellIdentification = _JnxWirelessWANNetworkInfoCellIdentification_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 25),
    _JnxWirelessWANNetworkInfoCellIdentification_Type()
)
jnxWirelessWANNetworkInfoCellIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoCellIdentification.setStatus("current")
_JnxWirelessWANNetworkInfoAPN_Type = DisplayString
_JnxWirelessWANNetworkInfoAPN_Object = MibTableColumn
jnxWirelessWANNetworkInfoAPN = _JnxWirelessWANNetworkInfoAPN_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 26),
    _JnxWirelessWANNetworkInfoAPN_Type()
)
jnxWirelessWANNetworkInfoAPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoAPN.setStatus("current")
_JnxWirelessWANNetworkInfoPLMN_Type = DisplayString
_JnxWirelessWANNetworkInfoPLMN_Object = MibTableColumn
jnxWirelessWANNetworkInfoPLMN = _JnxWirelessWANNetworkInfoPLMN_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 27),
    _JnxWirelessWANNetworkInfoPLMN_Type()
)
jnxWirelessWANNetworkInfoPLMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoPLMN.setStatus("current")
_JnxWirelessWANNetworkInfoPCI_Type = DisplayString
_JnxWirelessWANNetworkInfoPCI_Object = MibTableColumn
jnxWirelessWANNetworkInfoPCI = _JnxWirelessWANNetworkInfoPCI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 28),
    _JnxWirelessWANNetworkInfoPCI_Type()
)
jnxWirelessWANNetworkInfoPCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoPCI.setStatus("current")
_JnxWirelessWANNetworkInfoIMSI_Type = DisplayString
_JnxWirelessWANNetworkInfoIMSI_Object = MibTableColumn
jnxWirelessWANNetworkInfoIMSI = _JnxWirelessWANNetworkInfoIMSI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 29),
    _JnxWirelessWANNetworkInfoIMSI_Type()
)
jnxWirelessWANNetworkInfoIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoIMSI.setStatus("current")
_JnxWirelessWANNetworkInfoIMEI_Type = DisplayString
_JnxWirelessWANNetworkInfoIMEI_Object = MibTableColumn
jnxWirelessWANNetworkInfoIMEI = _JnxWirelessWANNetworkInfoIMEI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 30),
    _JnxWirelessWANNetworkInfoIMEI_Type()
)
jnxWirelessWANNetworkInfoIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoIMEI.setStatus("current")
_JnxWirelessWANNetworkInfoICCID_Type = DisplayString
_JnxWirelessWANNetworkInfoICCID_Object = MibTableColumn
jnxWirelessWANNetworkInfoICCID = _JnxWirelessWANNetworkInfoICCID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 31),
    _JnxWirelessWANNetworkInfoICCID_Type()
)
jnxWirelessWANNetworkInfoICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoICCID.setStatus("current")
_JnxWirelessWANNetworkInfoRSRP_Type = DisplayString
_JnxWirelessWANNetworkInfoRSRP_Object = MibTableColumn
jnxWirelessWANNetworkInfoRSRP = _JnxWirelessWANNetworkInfoRSRP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 32),
    _JnxWirelessWANNetworkInfoRSRP_Type()
)
jnxWirelessWANNetworkInfoRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoRSRP.setStatus("current")
_JnxWirelessWANNetworkInfoRSRQ_Type = DisplayString
_JnxWirelessWANNetworkInfoRSRQ_Object = MibTableColumn
jnxWirelessWANNetworkInfoRSRQ = _JnxWirelessWANNetworkInfoRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 33),
    _JnxWirelessWANNetworkInfoRSRQ_Type()
)
jnxWirelessWANNetworkInfoRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoRSRQ.setStatus("current")
_JnxWirelessWANNetworkInfoSINR_Type = DisplayString
_JnxWirelessWANNetworkInfoSINR_Object = MibTableColumn
jnxWirelessWANNetworkInfoSINR = _JnxWirelessWANNetworkInfoSINR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 34),
    _JnxWirelessWANNetworkInfoSINR_Type()
)
jnxWirelessWANNetworkInfoSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoSINR.setStatus("current")
_JnxWirelessWANNetworkInfoSNR_Type = DisplayString
_JnxWirelessWANNetworkInfoSNR_Object = MibTableColumn
jnxWirelessWANNetworkInfoSNR = _JnxWirelessWANNetworkInfoSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 35),
    _JnxWirelessWANNetworkInfoSNR_Type()
)
jnxWirelessWANNetworkInfoSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoSNR.setStatus("current")
_JnxWirelessWANNetworkInfoECIO_Type = Counter32
_JnxWirelessWANNetworkInfoECIO_Object = MibTableColumn
jnxWirelessWANNetworkInfoECIO = _JnxWirelessWANNetworkInfoECIO_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 36),
    _JnxWirelessWANNetworkInfoECIO_Type()
)
jnxWirelessWANNetworkInfoECIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoECIO.setStatus("current")
_JnxWirelessWANNetworkInfoRSSI_Type = DisplayString
_JnxWirelessWANNetworkInfoRSSI_Object = MibTableColumn
jnxWirelessWANNetworkInfoRSSI = _JnxWirelessWANNetworkInfoRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 1, 1, 1, 37),
    _JnxWirelessWANNetworkInfoRSSI_Type()
)
jnxWirelessWANNetworkInfoRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANNetworkInfoRSSI.setStatus("current")
_JnxWirelessWANFirmwareObjects_ObjectIdentity = ObjectIdentity
jnxWirelessWANFirmwareObjects = _JnxWirelessWANFirmwareObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2)
)
_JnxWirelessWANFirmwareInfoTable_Object = MibTable
jnxWirelessWANFirmwareInfoTable = _JnxWirelessWANFirmwareInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoTable.setStatus("current")
_JnxWirelessWANFirmwareInfoEntry_Object = MibTableRow
jnxWirelessWANFirmwareInfoEntry = _JnxWirelessWANFirmwareInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1)
)
jnxWirelessWANFirmwareInfoEntry.setIndexNames(
    (0, "JUNIPER-WIRELESS-WAN-MIB", "jnxWirelessWANFirmwareInfoIfdIndex"),
)
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoEntry.setStatus("current")
_JnxWirelessWANFirmwareInfoIfdIndex_Type = Counter32
_JnxWirelessWANFirmwareInfoIfdIndex_Object = MibTableColumn
jnxWirelessWANFirmwareInfoIfdIndex = _JnxWirelessWANFirmwareInfoIfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 1),
    _JnxWirelessWANFirmwareInfoIfdIndex_Type()
)
jnxWirelessWANFirmwareInfoIfdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoIfdIndex.setStatus("current")
_JnxWirelessWANFirmwareInfomPIMProductName_Type = DisplayString
_JnxWirelessWANFirmwareInfomPIMProductName_Object = MibTableColumn
jnxWirelessWANFirmwareInfomPIMProductName = _JnxWirelessWANFirmwareInfomPIMProductName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 2),
    _JnxWirelessWANFirmwareInfomPIMProductName_Type()
)
jnxWirelessWANFirmwareInfomPIMProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfomPIMProductName.setStatus("current")
_JnxWirelessWANFirmwareInfomPIMSerialNumber_Type = DisplayString
_JnxWirelessWANFirmwareInfomPIMSerialNumber_Object = MibTableColumn
jnxWirelessWANFirmwareInfomPIMSerialNumber = _JnxWirelessWANFirmwareInfomPIMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 3),
    _JnxWirelessWANFirmwareInfomPIMSerialNumber_Type()
)
jnxWirelessWANFirmwareInfomPIMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfomPIMSerialNumber.setStatus("current")
_JnxWirelessWANFirmwareInfomPIMHardwareVersion_Type = DisplayString
_JnxWirelessWANFirmwareInfomPIMHardwareVersion_Object = MibTableColumn
jnxWirelessWANFirmwareInfomPIMHardwareVersion = _JnxWirelessWANFirmwareInfomPIMHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 4),
    _JnxWirelessWANFirmwareInfomPIMHardwareVersion_Type()
)
jnxWirelessWANFirmwareInfomPIMHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfomPIMHardwareVersion.setStatus("current")
_JnxWirelessWANFirmwareInfomPIMFirmwareVersion_Type = DisplayString
_JnxWirelessWANFirmwareInfomPIMFirmwareVersion_Object = MibTableColumn
jnxWirelessWANFirmwareInfomPIMFirmwareVersion = _JnxWirelessWANFirmwareInfomPIMFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 5),
    _JnxWirelessWANFirmwareInfomPIMFirmwareVersion_Type()
)
jnxWirelessWANFirmwareInfomPIMFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfomPIMFirmwareVersion.setStatus("current")
_JnxWirelessWANFirmwareInfomPIMMAC_Type = DisplayString
_JnxWirelessWANFirmwareInfomPIMMAC_Object = MibTableColumn
jnxWirelessWANFirmwareInfomPIMMAC = _JnxWirelessWANFirmwareInfomPIMMAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 6),
    _JnxWirelessWANFirmwareInfomPIMMAC_Type()
)
jnxWirelessWANFirmwareInfomPIMMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfomPIMMAC.setStatus("current")
_JnxWirelessWANFirmwareInfomPIMSystemUptime_Type = TimeStamp
_JnxWirelessWANFirmwareInfomPIMSystemUptime_Object = MibTableColumn
jnxWirelessWANFirmwareInfomPIMSystemUptime = _JnxWirelessWANFirmwareInfomPIMSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 7),
    _JnxWirelessWANFirmwareInfomPIMSystemUptime_Type()
)
jnxWirelessWANFirmwareInfomPIMSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfomPIMSystemUptime.setStatus("current")
_JnxWirelessWANFirmwareInfoModemFirmwareVersion_Type = DisplayString
_JnxWirelessWANFirmwareInfoModemFirmwareVersion_Object = MibTableColumn
jnxWirelessWANFirmwareInfoModemFirmwareVersion = _JnxWirelessWANFirmwareInfoModemFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 8),
    _JnxWirelessWANFirmwareInfoModemFirmwareVersion_Type()
)
jnxWirelessWANFirmwareInfoModemFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoModemFirmwareVersion.setStatus("current")
_JnxWirelessWANFirmwareInfoModemFirmwareBuildDate_Type = DisplayString
_JnxWirelessWANFirmwareInfoModemFirmwareBuildDate_Object = MibTableColumn
jnxWirelessWANFirmwareInfoModemFirmwareBuildDate = _JnxWirelessWANFirmwareInfoModemFirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 9),
    _JnxWirelessWANFirmwareInfoModemFirmwareBuildDate_Type()
)
jnxWirelessWANFirmwareInfoModemFirmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoModemFirmwareBuildDate.setStatus("current")
_JnxWirelessWANFirmwareInfoModemCardType_Type = DisplayString
_JnxWirelessWANFirmwareInfoModemCardType_Object = MibTableColumn
jnxWirelessWANFirmwareInfoModemCardType = _JnxWirelessWANFirmwareInfoModemCardType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 10),
    _JnxWirelessWANFirmwareInfoModemCardType_Type()
)
jnxWirelessWANFirmwareInfoModemCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoModemCardType.setStatus("current")
_JnxWirelessWANFirmwareInfoModemManufacturer_Type = DisplayString
_JnxWirelessWANFirmwareInfoModemManufacturer_Object = MibTableColumn
jnxWirelessWANFirmwareInfoModemManufacturer = _JnxWirelessWANFirmwareInfoModemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 11),
    _JnxWirelessWANFirmwareInfoModemManufacturer_Type()
)
jnxWirelessWANFirmwareInfoModemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoModemManufacturer.setStatus("current")
_JnxWirelessWANFirmwareInfoModemHardwareVersion_Type = DisplayString
_JnxWirelessWANFirmwareInfoModemHardwareVersion_Object = MibTableColumn
jnxWirelessWANFirmwareInfoModemHardwareVersion = _JnxWirelessWANFirmwareInfoModemHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 12),
    _JnxWirelessWANFirmwareInfoModemHardwareVersion_Type()
)
jnxWirelessWANFirmwareInfoModemHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoModemHardwareVersion.setStatus("current")
_JnxWirelessWANFirmwareInfoModemPowerAndTemperature_Type = DisplayString
_JnxWirelessWANFirmwareInfoModemPowerAndTemperature_Object = MibTableColumn
jnxWirelessWANFirmwareInfoModemPowerAndTemperature = _JnxWirelessWANFirmwareInfoModemPowerAndTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 13),
    _JnxWirelessWANFirmwareInfoModemPowerAndTemperature_Type()
)
jnxWirelessWANFirmwareInfoModemPowerAndTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoModemPowerAndTemperature.setStatus("current")
_JnxWirelessWANFirmwareInfoOTAState_Type = DisplayString
_JnxWirelessWANFirmwareInfoOTAState_Object = MibTableColumn
jnxWirelessWANFirmwareInfoOTAState = _JnxWirelessWANFirmwareInfoOTAState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 14),
    _JnxWirelessWANFirmwareInfoOTAState_Type()
)
jnxWirelessWANFirmwareInfoOTAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoOTAState.setStatus("current")
_JnxWirelessWANFirmwareInfoOTANewFirmwareAvailable_Type = DisplayString
_JnxWirelessWANFirmwareInfoOTANewFirmwareAvailable_Object = MibTableColumn
jnxWirelessWANFirmwareInfoOTANewFirmwareAvailable = _JnxWirelessWANFirmwareInfoOTANewFirmwareAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 15),
    _JnxWirelessWANFirmwareInfoOTANewFirmwareAvailable_Type()
)
jnxWirelessWANFirmwareInfoOTANewFirmwareAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoOTANewFirmwareAvailable.setStatus("current")
_JnxWirelessWANFirmwareInfoOTANewVersion_Type = DisplayString
_JnxWirelessWANFirmwareInfoOTANewVersion_Object = MibTableColumn
jnxWirelessWANFirmwareInfoOTANewVersion = _JnxWirelessWANFirmwareInfoOTANewVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 16),
    _JnxWirelessWANFirmwareInfoOTANewVersion_Type()
)
jnxWirelessWANFirmwareInfoOTANewVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoOTANewVersion.setStatus("current")
_JnxWirelessWANFirmwareInfoNumberOfSIM_Type = Counter32
_JnxWirelessWANFirmwareInfoNumberOfSIM_Object = MibTableColumn
jnxWirelessWANFirmwareInfoNumberOfSIM = _JnxWirelessWANFirmwareInfoNumberOfSIM_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 17),
    _JnxWirelessWANFirmwareInfoNumberOfSIM_Type()
)
jnxWirelessWANFirmwareInfoNumberOfSIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoNumberOfSIM.setStatus("current")
_JnxWirelessWANFirmwareInfoSlotOfActive_Type = Counter32
_JnxWirelessWANFirmwareInfoSlotOfActive_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSlotOfActive = _JnxWirelessWANFirmwareInfoSlotOfActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 18),
    _JnxWirelessWANFirmwareInfoSlotOfActive_Type()
)
jnxWirelessWANFirmwareInfoSlotOfActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSlotOfActive.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM1State_Type = DisplayString
_JnxWirelessWANFirmwareInfoSIM1State_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM1State = _JnxWirelessWANFirmwareInfoSIM1State_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 19),
    _JnxWirelessWANFirmwareInfoSIM1State_Type()
)
jnxWirelessWANFirmwareInfoSIM1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM1State.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM1ModemPINSecurityStatus_Type = DisplayString
_JnxWirelessWANFirmwareInfoSIM1ModemPINSecurityStatus_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM1ModemPINSecurityStatus = _JnxWirelessWANFirmwareInfoSIM1ModemPINSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 20),
    _JnxWirelessWANFirmwareInfoSIM1ModemPINSecurityStatus_Type()
)
jnxWirelessWANFirmwareInfoSIM1ModemPINSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM1ModemPINSecurityStatus.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM1Status_Type = DisplayString
_JnxWirelessWANFirmwareInfoSIM1Status_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM1Status = _JnxWirelessWANFirmwareInfoSIM1Status_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 21),
    _JnxWirelessWANFirmwareInfoSIM1Status_Type()
)
jnxWirelessWANFirmwareInfoSIM1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM1Status.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM1UserOperationNeeded_Type = DisplayString
_JnxWirelessWANFirmwareInfoSIM1UserOperationNeeded_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM1UserOperationNeeded = _JnxWirelessWANFirmwareInfoSIM1UserOperationNeeded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 22),
    _JnxWirelessWANFirmwareInfoSIM1UserOperationNeeded_Type()
)
jnxWirelessWANFirmwareInfoSIM1UserOperationNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM1UserOperationNeeded.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM1RetriesRemaining_Type = Counter32
_JnxWirelessWANFirmwareInfoSIM1RetriesRemaining_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM1RetriesRemaining = _JnxWirelessWANFirmwareInfoSIM1RetriesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 23),
    _JnxWirelessWANFirmwareInfoSIM1RetriesRemaining_Type()
)
jnxWirelessWANFirmwareInfoSIM1RetriesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM1RetriesRemaining.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM2State_Type = DisplayString
_JnxWirelessWANFirmwareInfoSIM2State_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM2State = _JnxWirelessWANFirmwareInfoSIM2State_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 24),
    _JnxWirelessWANFirmwareInfoSIM2State_Type()
)
jnxWirelessWANFirmwareInfoSIM2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM2State.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM2ModemPINSecurityStatus_Type = DisplayString
_JnxWirelessWANFirmwareInfoSIM2ModemPINSecurityStatus_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM2ModemPINSecurityStatus = _JnxWirelessWANFirmwareInfoSIM2ModemPINSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 25),
    _JnxWirelessWANFirmwareInfoSIM2ModemPINSecurityStatus_Type()
)
jnxWirelessWANFirmwareInfoSIM2ModemPINSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM2ModemPINSecurityStatus.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM2Status_Type = DisplayString
_JnxWirelessWANFirmwareInfoSIM2Status_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM2Status = _JnxWirelessWANFirmwareInfoSIM2Status_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 26),
    _JnxWirelessWANFirmwareInfoSIM2Status_Type()
)
jnxWirelessWANFirmwareInfoSIM2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM2Status.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM2UserOperationNeeded_Type = DisplayString
_JnxWirelessWANFirmwareInfoSIM2UserOperationNeeded_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM2UserOperationNeeded = _JnxWirelessWANFirmwareInfoSIM2UserOperationNeeded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 27),
    _JnxWirelessWANFirmwareInfoSIM2UserOperationNeeded_Type()
)
jnxWirelessWANFirmwareInfoSIM2UserOperationNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM2UserOperationNeeded.setStatus("current")
_JnxWirelessWANFirmwareInfoSIM2RetriesRemaining_Type = Counter32
_JnxWirelessWANFirmwareInfoSIM2RetriesRemaining_Object = MibTableColumn
jnxWirelessWANFirmwareInfoSIM2RetriesRemaining = _JnxWirelessWANFirmwareInfoSIM2RetriesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 87, 1, 2, 1, 1, 28),
    _JnxWirelessWANFirmwareInfoSIM2RetriesRemaining_Type()
)
jnxWirelessWANFirmwareInfoSIM2RetriesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWirelessWANFirmwareInfoSIM2RetriesRemaining.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WIRELESS-WAN-MIB",
    **{"jnxWirelessWANMIB": jnxWirelessWANMIB,
       "jnxWirelessWANNetworkObjects": jnxWirelessWANNetworkObjects,
       "jnxWirelessWANNetworkInfoTable": jnxWirelessWANNetworkInfoTable,
       "jnxWirelessWANNetworkInfoEntry": jnxWirelessWANNetworkInfoEntry,
       "jnxWirelessWANNetworkInfoIfdIndex": jnxWirelessWANNetworkInfoIfdIndex,
       "jnxWirelessWANNetworkInfoConnectTime": jnxWirelessWANNetworkInfoConnectTime,
       "jnxWirelessWANNetworkInfoIP": jnxWirelessWANNetworkInfoIP,
       "jnxWirelessWANNetworkInfoGateway": jnxWirelessWANNetworkInfoGateway,
       "jnxWirelessWANNetworkInfoDNS": jnxWirelessWANNetworkInfoDNS,
       "jnxWirelessWANNetworkInfoIPv6": jnxWirelessWANNetworkInfoIPv6,
       "jnxWirelessWANNetworkInfoIPv6Gateway": jnxWirelessWANNetworkInfoIPv6Gateway,
       "jnxWirelessWANNetworkInfoIPv6DNS": jnxWirelessWANNetworkInfoIPv6DNS,
       "jnxWirelessWANNetworkInfoInputbps": jnxWirelessWANNetworkInfoInputbps,
       "jnxWirelessWANNetworkInfoOutputbps": jnxWirelessWANNetworkInfoOutputbps,
       "jnxWirelessWANNetworkInfoBytesReceived": jnxWirelessWANNetworkInfoBytesReceived,
       "jnxWirelessWANNetworkInfoBytesTransferred": jnxWirelessWANNetworkInfoBytesTransferred,
       "jnxWirelessWANNetworkInfoPacketsReceived": jnxWirelessWANNetworkInfoPacketsReceived,
       "jnxWirelessWANNetworkInfoPacketsTransferred": jnxWirelessWANNetworkInfoPacketsTransferred,
       "jnxWirelessWANNetworkInfoCurrentModemStatus": jnxWirelessWANNetworkInfoCurrentModemStatus,
       "jnxWirelessWANNetworkInfoCurrentServiceStatus": jnxWirelessWANNetworkInfoCurrentServiceStatus,
       "jnxWirelessWANNetworkInfoCurrentServiceType": jnxWirelessWANNetworkInfoCurrentServiceType,
       "jnxWirelessWANNetworkInfoCurrentServiceMode": jnxWirelessWANNetworkInfoCurrentServiceMode,
       "jnxWirelessWANNetworkInfoCurrentBand": jnxWirelessWANNetworkInfoCurrentBand,
       "jnxWirelessWANNetworkInfoNetwork": jnxWirelessWANNetworkInfoNetwork,
       "jnxWirelessWANNetworkInfoMCC": jnxWirelessWANNetworkInfoMCC,
       "jnxWirelessWANNetworkInfoMNC": jnxWirelessWANNetworkInfoMNC,
       "jnxWirelessWANNetworkInfoLAC": jnxWirelessWANNetworkInfoLAC,
       "jnxWirelessWANNetworkInfoRAC": jnxWirelessWANNetworkInfoRAC,
       "jnxWirelessWANNetworkInfoCellIdentification": jnxWirelessWANNetworkInfoCellIdentification,
       "jnxWirelessWANNetworkInfoAPN": jnxWirelessWANNetworkInfoAPN,
       "jnxWirelessWANNetworkInfoPLMN": jnxWirelessWANNetworkInfoPLMN,
       "jnxWirelessWANNetworkInfoPCI": jnxWirelessWANNetworkInfoPCI,
       "jnxWirelessWANNetworkInfoIMSI": jnxWirelessWANNetworkInfoIMSI,
       "jnxWirelessWANNetworkInfoIMEI": jnxWirelessWANNetworkInfoIMEI,
       "jnxWirelessWANNetworkInfoICCID": jnxWirelessWANNetworkInfoICCID,
       "jnxWirelessWANNetworkInfoRSRP": jnxWirelessWANNetworkInfoRSRP,
       "jnxWirelessWANNetworkInfoRSRQ": jnxWirelessWANNetworkInfoRSRQ,
       "jnxWirelessWANNetworkInfoSINR": jnxWirelessWANNetworkInfoSINR,
       "jnxWirelessWANNetworkInfoSNR": jnxWirelessWANNetworkInfoSNR,
       "jnxWirelessWANNetworkInfoECIO": jnxWirelessWANNetworkInfoECIO,
       "jnxWirelessWANNetworkInfoRSSI": jnxWirelessWANNetworkInfoRSSI,
       "jnxWirelessWANFirmwareObjects": jnxWirelessWANFirmwareObjects,
       "jnxWirelessWANFirmwareInfoTable": jnxWirelessWANFirmwareInfoTable,
       "jnxWirelessWANFirmwareInfoEntry": jnxWirelessWANFirmwareInfoEntry,
       "jnxWirelessWANFirmwareInfoIfdIndex": jnxWirelessWANFirmwareInfoIfdIndex,
       "jnxWirelessWANFirmwareInfomPIMProductName": jnxWirelessWANFirmwareInfomPIMProductName,
       "jnxWirelessWANFirmwareInfomPIMSerialNumber": jnxWirelessWANFirmwareInfomPIMSerialNumber,
       "jnxWirelessWANFirmwareInfomPIMHardwareVersion": jnxWirelessWANFirmwareInfomPIMHardwareVersion,
       "jnxWirelessWANFirmwareInfomPIMFirmwareVersion": jnxWirelessWANFirmwareInfomPIMFirmwareVersion,
       "jnxWirelessWANFirmwareInfomPIMMAC": jnxWirelessWANFirmwareInfomPIMMAC,
       "jnxWirelessWANFirmwareInfomPIMSystemUptime": jnxWirelessWANFirmwareInfomPIMSystemUptime,
       "jnxWirelessWANFirmwareInfoModemFirmwareVersion": jnxWirelessWANFirmwareInfoModemFirmwareVersion,
       "jnxWirelessWANFirmwareInfoModemFirmwareBuildDate": jnxWirelessWANFirmwareInfoModemFirmwareBuildDate,
       "jnxWirelessWANFirmwareInfoModemCardType": jnxWirelessWANFirmwareInfoModemCardType,
       "jnxWirelessWANFirmwareInfoModemManufacturer": jnxWirelessWANFirmwareInfoModemManufacturer,
       "jnxWirelessWANFirmwareInfoModemHardwareVersion": jnxWirelessWANFirmwareInfoModemHardwareVersion,
       "jnxWirelessWANFirmwareInfoModemPowerAndTemperature": jnxWirelessWANFirmwareInfoModemPowerAndTemperature,
       "jnxWirelessWANFirmwareInfoOTAState": jnxWirelessWANFirmwareInfoOTAState,
       "jnxWirelessWANFirmwareInfoOTANewFirmwareAvailable": jnxWirelessWANFirmwareInfoOTANewFirmwareAvailable,
       "jnxWirelessWANFirmwareInfoOTANewVersion": jnxWirelessWANFirmwareInfoOTANewVersion,
       "jnxWirelessWANFirmwareInfoNumberOfSIM": jnxWirelessWANFirmwareInfoNumberOfSIM,
       "jnxWirelessWANFirmwareInfoSlotOfActive": jnxWirelessWANFirmwareInfoSlotOfActive,
       "jnxWirelessWANFirmwareInfoSIM1State": jnxWirelessWANFirmwareInfoSIM1State,
       "jnxWirelessWANFirmwareInfoSIM1ModemPINSecurityStatus": jnxWirelessWANFirmwareInfoSIM1ModemPINSecurityStatus,
       "jnxWirelessWANFirmwareInfoSIM1Status": jnxWirelessWANFirmwareInfoSIM1Status,
       "jnxWirelessWANFirmwareInfoSIM1UserOperationNeeded": jnxWirelessWANFirmwareInfoSIM1UserOperationNeeded,
       "jnxWirelessWANFirmwareInfoSIM1RetriesRemaining": jnxWirelessWANFirmwareInfoSIM1RetriesRemaining,
       "jnxWirelessWANFirmwareInfoSIM2State": jnxWirelessWANFirmwareInfoSIM2State,
       "jnxWirelessWANFirmwareInfoSIM2ModemPINSecurityStatus": jnxWirelessWANFirmwareInfoSIM2ModemPINSecurityStatus,
       "jnxWirelessWANFirmwareInfoSIM2Status": jnxWirelessWANFirmwareInfoSIM2Status,
       "jnxWirelessWANFirmwareInfoSIM2UserOperationNeeded": jnxWirelessWANFirmwareInfoSIM2UserOperationNeeded,
       "jnxWirelessWANFirmwareInfoSIM2RetriesRemaining": jnxWirelessWANFirmwareInfoSIM2RetriesRemaining}
)
