# SNMP MIB module (GRANDSTREAM-GWN-PRODUCTS-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\grandstream\GRANDSTREAM-GWN-PRODUCTS-AP-MIB

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

(gwnAp,) = mibBuilder.importSymbols(
    "GRANDSTREAM-GWN-PRODUCTS-MIB",
    "gwnAp")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gwnApWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GwnApSystemInfo_ObjectIdentity = ObjectIdentity
gwnApSystemInfo = _GwnApSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2)
)
_GwnDeviceModel_Type = DisplayString
_GwnDeviceModel_Object = MibScalar
gwnDeviceModel = _GwnDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1),
    _GwnDeviceModel_Type()
)
gwnDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceModel.setStatus("current")
_GwnDeviceName_Type = DisplayString
_GwnDeviceName_Object = MibScalar
gwnDeviceName = _GwnDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2),
    _GwnDeviceName_Type()
)
gwnDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceName.setStatus("current")
_GwnDeviceMac_Type = DisplayString
_GwnDeviceMac_Object = MibScalar
gwnDeviceMac = _GwnDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3),
    _GwnDeviceMac_Type()
)
gwnDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceMac.setStatus("current")
_GwnDeviceVersion_Type = DisplayString
_GwnDeviceVersion_Object = MibScalar
gwnDeviceVersion = _GwnDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4),
    _GwnDeviceVersion_Type()
)
gwnDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceVersion.setStatus("current")
_GwnDeviceIPAddress_Type = DisplayString
_GwnDeviceIPAddress_Object = MibScalar
gwnDeviceIPAddress = _GwnDeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5),
    _GwnDeviceIPAddress_Type()
)
gwnDeviceIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceIPAddress.setStatus("current")
_GwnDeviceUptime_Type = TimeTicks
_GwnDeviceUptime_Object = MibScalar
gwnDeviceUptime = _GwnDeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6),
    _GwnDeviceUptime_Type()
)
gwnDeviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceUptime.setStatus("current")
_GwnStatusTable_Object = MibTable
gwnStatusTable = _GwnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    gwnStatusTable.setStatus("current")
_GwnStatusEntry_Object = MibTableRow
gwnStatusEntry = _GwnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 7, 1)
)
gwnStatusEntry.setIndexNames(
    (0, "GRANDSTREAM-GWN-PRODUCTS-AP-MIB", "gwnStatusMac"),
)
if mibBuilder.loadTexts:
    gwnStatusEntry.setStatus("current")
_GwnStatusMac_Type = DisplayString
_GwnStatusMac_Object = MibTableColumn
gwnStatusMac = _GwnStatusMac_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 7, 1, 1),
    _GwnStatusMac_Type()
)
gwnStatusMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnStatusMac.setStatus("current")
_GwnApStatus_Type = DisplayString
_GwnApStatus_Object = MibTableColumn
gwnApStatus = _GwnApStatus_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 7, 1, 2),
    _GwnApStatus_Type()
)
gwnApStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnApStatus.setStatus("current")
_GwnRadioTable_Object = MibTable
gwnRadioTable = _GwnRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    gwnRadioTable.setStatus("current")
_GwnRadioEntry_Object = MibTableRow
gwnRadioEntry = _GwnRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1)
)
gwnRadioEntry.setIndexNames(
    (0, "GRANDSTREAM-GWN-PRODUCTS-AP-MIB", "gwnRadioIndex"),
)
if mibBuilder.loadTexts:
    gwnRadioEntry.setStatus("current")
_GwnRadioIndex_Type = Integer32
_GwnRadioIndex_Object = MibTableColumn
gwnRadioIndex = _GwnRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 1),
    _GwnRadioIndex_Type()
)
gwnRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioIndex.setStatus("current")
_GwnRadioName_Type = DisplayString
_GwnRadioName_Object = MibTableColumn
gwnRadioName = _GwnRadioName_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 2),
    _GwnRadioName_Type()
)
gwnRadioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioName.setStatus("current")
_GwnRadioStatus_Type = Integer32
_GwnRadioStatus_Object = MibTableColumn
gwnRadioStatus = _GwnRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 3),
    _GwnRadioStatus_Type()
)
gwnRadioStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioStatus.setStatus("current")
_GwnRadioChannel_Type = Integer32
_GwnRadioChannel_Object = MibTableColumn
gwnRadioChannel = _GwnRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 4),
    _GwnRadioChannel_Type()
)
gwnRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioChannel.setStatus("current")
_GwnRadioTransmitPower_Type = Integer32
_GwnRadioTransmitPower_Object = MibTableColumn
gwnRadioTransmitPower = _GwnRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 5),
    _GwnRadioTransmitPower_Type()
)
gwnRadioTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioTransmitPower.setStatus("current")
_GwnRadioTxTotalFrames_Type = Counter32
_GwnRadioTxTotalFrames_Object = MibTableColumn
gwnRadioTxTotalFrames = _GwnRadioTxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 6),
    _GwnRadioTxTotalFrames_Type()
)
gwnRadioTxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioTxTotalFrames.setStatus("current")
_GwnRadioTxMgmtFrames_Type = Counter32
_GwnRadioTxMgmtFrames_Object = MibTableColumn
gwnRadioTxMgmtFrames = _GwnRadioTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 7),
    _GwnRadioTxMgmtFrames_Type()
)
gwnRadioTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioTxMgmtFrames.setStatus("current")
_GwnRadioTxDataFrames_Type = Counter32
_GwnRadioTxDataFrames_Object = MibTableColumn
gwnRadioTxDataFrames = _GwnRadioTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 8),
    _GwnRadioTxDataFrames_Type()
)
gwnRadioTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioTxDataFrames.setStatus("current")
_GwnRadioTxDataBytes_Type = Counter32
_GwnRadioTxDataBytes_Object = MibTableColumn
gwnRadioTxDataBytes = _GwnRadioTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 9),
    _GwnRadioTxDataBytes_Type()
)
gwnRadioTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioTxDataBytes.setStatus("current")
_GwnRadioTxDrops_Type = Counter32
_GwnRadioTxDrops_Object = MibTableColumn
gwnRadioTxDrops = _GwnRadioTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 10),
    _GwnRadioTxDrops_Type()
)
gwnRadioTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioTxDrops.setStatus("current")
_GwnRadioRxTotalFrames_Type = Counter32
_GwnRadioRxTotalFrames_Object = MibTableColumn
gwnRadioRxTotalFrames = _GwnRadioRxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 11),
    _GwnRadioRxTotalFrames_Type()
)
gwnRadioRxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioRxTotalFrames.setStatus("current")
_GwnRadioRxDataFrames_Type = Counter32
_GwnRadioRxDataFrames_Object = MibTableColumn
gwnRadioRxDataFrames = _GwnRadioRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 12),
    _GwnRadioRxDataFrames_Type()
)
gwnRadioRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioRxDataFrames.setStatus("current")
_GwnRadioRxDataBytes_Type = Counter32
_GwnRadioRxDataBytes_Object = MibTableColumn
gwnRadioRxDataBytes = _GwnRadioRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 13),
    _GwnRadioRxDataBytes_Type()
)
gwnRadioRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioRxDataBytes.setStatus("current")
_GwnRadioRxMgmtFrames_Type = Counter32
_GwnRadioRxMgmtFrames_Object = MibTableColumn
gwnRadioRxMgmtFrames = _GwnRadioRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 14),
    _GwnRadioRxMgmtFrames_Type()
)
gwnRadioRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioRxMgmtFrames.setStatus("current")
_GwnRadioRxBad_Type = Counter32
_GwnRadioRxBad_Object = MibTableColumn
gwnRadioRxBad = _GwnRadioRxBad_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1, 1, 15),
    _GwnRadioRxBad_Type()
)
gwnRadioRxBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnRadioRxBad.setStatus("current")
_GwnWlanTable_Object = MibTable
gwnWlanTable = _GwnWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gwnWlanTable.setStatus("current")
_GwnWlanEntry_Object = MibTableRow
gwnWlanEntry = _GwnWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1)
)
gwnWlanEntry.setIndexNames(
    (0, "GRANDSTREAM-GWN-PRODUCTS-AP-MIB", "gwnWlanIndex"),
)
if mibBuilder.loadTexts:
    gwnWlanEntry.setStatus("current")
_GwnWlanIndex_Type = Integer32
_GwnWlanIndex_Object = MibTableColumn
gwnWlanIndex = _GwnWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1, 1),
    _GwnWlanIndex_Type()
)
gwnWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnWlanIndex.setStatus("current")
_GwnWlanESSID_Type = DisplayString
_GwnWlanESSID_Object = MibTableColumn
gwnWlanESSID = _GwnWlanESSID_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1, 2),
    _GwnWlanESSID_Type()
)
gwnWlanESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnWlanESSID.setStatus("current")
_GwnWlanBSSID_Type = DisplayString
_GwnWlanBSSID_Object = MibTableColumn
gwnWlanBSSID = _GwnWlanBSSID_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1, 3),
    _GwnWlanBSSID_Type()
)
gwnWlanBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnWlanBSSID.setStatus("current")
_GwnWlanTxTotalFrames_Type = Counter32
_GwnWlanTxTotalFrames_Object = MibTableColumn
gwnWlanTxTotalFrames = _GwnWlanTxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1, 4),
    _GwnWlanTxTotalFrames_Type()
)
gwnWlanTxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnWlanTxTotalFrames.setStatus("current")
_GwnWlanTxDataFrames_Type = Counter32
_GwnWlanTxDataFrames_Object = MibTableColumn
gwnWlanTxDataFrames = _GwnWlanTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1, 5),
    _GwnWlanTxDataFrames_Type()
)
gwnWlanTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnWlanTxDataFrames.setStatus("current")
_GwnWlanTxDataBytes_Type = Counter32
_GwnWlanTxDataBytes_Object = MibTableColumn
gwnWlanTxDataBytes = _GwnWlanTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1, 6),
    _GwnWlanTxDataBytes_Type()
)
gwnWlanTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnWlanTxDataBytes.setStatus("current")
_GwnWlanRxTotalFrames_Type = Counter32
_GwnWlanRxTotalFrames_Object = MibTableColumn
gwnWlanRxTotalFrames = _GwnWlanRxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1, 7),
    _GwnWlanRxTotalFrames_Type()
)
gwnWlanRxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnWlanRxTotalFrames.setStatus("current")
_GwnWlanRxDataFrames_Type = Counter32
_GwnWlanRxDataFrames_Object = MibTableColumn
gwnWlanRxDataFrames = _GwnWlanRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1, 8),
    _GwnWlanRxDataFrames_Type()
)
gwnWlanRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnWlanRxDataFrames.setStatus("current")
_GwnWlanRxDataBytes_Type = Counter32
_GwnWlanRxDataBytes_Object = MibTableColumn
gwnWlanRxDataBytes = _GwnWlanRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2, 1, 9),
    _GwnWlanRxDataBytes_Type()
)
gwnWlanRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnWlanRxDataBytes.setStatus("current")
_GwnClientTable_Object = MibTable
gwnClientTable = _GwnClientTable_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    gwnClientTable.setStatus("current")
_GwnClientEntry_Object = MibTableRow
gwnClientEntry = _GwnClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1)
)
gwnClientEntry.setIndexNames(
    (0, "GRANDSTREAM-GWN-PRODUCTS-AP-MIB", "gwnClientMACAddress"),
)
if mibBuilder.loadTexts:
    gwnClientEntry.setStatus("current")
_GwnClientMACAddress_Type = DisplayString
_GwnClientMACAddress_Object = MibTableColumn
gwnClientMACAddress = _GwnClientMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 1),
    _GwnClientMACAddress_Type()
)
gwnClientMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientMACAddress.setStatus("current")
_GwnClienttIPAddress_Type = IpAddress
_GwnClienttIPAddress_Object = MibTableColumn
gwnClienttIPAddress = _GwnClienttIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 2),
    _GwnClienttIPAddress_Type()
)
gwnClienttIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClienttIPAddress.setStatus("current")
_GwnClientWlanMACAddress_Type = DisplayString
_GwnClientWlanMACAddress_Object = MibTableColumn
gwnClientWlanMACAddress = _GwnClientWlanMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 3),
    _GwnClientWlanMACAddress_Type()
)
gwnClientWlanMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientWlanMACAddress.setStatus("current")
_GwnClientESSID_Type = DisplayString
_GwnClientESSID_Object = MibTableColumn
gwnClientESSID = _GwnClientESSID_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 4),
    _GwnClientESSID_Type()
)
gwnClientESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientESSID.setStatus("current")
_GwnClientRSSI_Type = Integer32
_GwnClientRSSI_Object = MibTableColumn
gwnClientRSSI = _GwnClientRSSI_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 5),
    _GwnClientRSSI_Type()
)
gwnClientRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientRSSI.setStatus("current")
_GwnClientAssoctime_Type = TimeTicks
_GwnClientAssoctime_Object = MibTableColumn
gwnClientAssoctime = _GwnClientAssoctime_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 6),
    _GwnClientAssoctime_Type()
)
gwnClientAssoctime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientAssoctime.setStatus("current")
_GwnClientManufacture_Type = DisplayString
_GwnClientManufacture_Object = MibTableColumn
gwnClientManufacture = _GwnClientManufacture_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 7),
    _GwnClientManufacture_Type()
)
gwnClientManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientManufacture.setStatus("current")
_GwnClientHostname_Type = DisplayString
_GwnClientHostname_Object = MibTableColumn
gwnClientHostname = _GwnClientHostname_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 8),
    _GwnClientHostname_Type()
)
gwnClientHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientHostname.setStatus("current")
_GwnClientOS_Type = DisplayString
_GwnClientOS_Object = MibTableColumn
gwnClientOS = _GwnClientOS_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 9),
    _GwnClientOS_Type()
)
gwnClientOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientOS.setStatus("current")
_GwnClientTxRate_Type = Integer32
_GwnClientTxRate_Object = MibTableColumn
gwnClientTxRate = _GwnClientTxRate_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 10),
    _GwnClientTxRate_Type()
)
gwnClientTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientTxRate.setStatus("current")
_GwnClientTxDataFrames_Type = Counter32
_GwnClientTxDataFrames_Object = MibTableColumn
gwnClientTxDataFrames = _GwnClientTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 11),
    _GwnClientTxDataFrames_Type()
)
gwnClientTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientTxDataFrames.setStatus("current")
_GwnClientTxDataBytes_Type = Counter32
_GwnClientTxDataBytes_Object = MibTableColumn
gwnClientTxDataBytes = _GwnClientTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 12),
    _GwnClientTxDataBytes_Type()
)
gwnClientTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientTxDataBytes.setStatus("current")
_GwnClientRxRate_Type = Integer32
_GwnClientRxRate_Object = MibTableColumn
gwnClientRxRate = _GwnClientRxRate_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 13),
    _GwnClientRxRate_Type()
)
gwnClientRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientRxRate.setStatus("current")
_GwnClientRxDataFrames_Type = Counter32
_GwnClientRxDataFrames_Object = MibTableColumn
gwnClientRxDataFrames = _GwnClientRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 14),
    _GwnClientRxDataFrames_Type()
)
gwnClientRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientRxDataFrames.setStatus("current")
_GwnClientRxDataBytes_Type = Counter32
_GwnClientRxDataBytes_Object = MibTableColumn
gwnClientRxDataBytes = _GwnClientRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3, 1, 15),
    _GwnClientRxDataBytes_Type()
)
gwnClientRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnClientRxDataBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GRANDSTREAM-GWN-PRODUCTS-AP-MIB",
    **{"gwnApSystemInfo": gwnApSystemInfo,
       "gwnDeviceModel": gwnDeviceModel,
       "gwnDeviceName": gwnDeviceName,
       "gwnDeviceMac": gwnDeviceMac,
       "gwnDeviceVersion": gwnDeviceVersion,
       "gwnDeviceIPAddress": gwnDeviceIPAddress,
       "gwnDeviceUptime": gwnDeviceUptime,
       "gwnStatusTable": gwnStatusTable,
       "gwnStatusEntry": gwnStatusEntry,
       "gwnStatusMac": gwnStatusMac,
       "gwnApStatus": gwnApStatus,
       "gwnApWireless": gwnApWireless,
       "gwnRadioTable": gwnRadioTable,
       "gwnRadioEntry": gwnRadioEntry,
       "gwnRadioIndex": gwnRadioIndex,
       "gwnRadioName": gwnRadioName,
       "gwnRadioStatus": gwnRadioStatus,
       "gwnRadioChannel": gwnRadioChannel,
       "gwnRadioTransmitPower": gwnRadioTransmitPower,
       "gwnRadioTxTotalFrames": gwnRadioTxTotalFrames,
       "gwnRadioTxMgmtFrames": gwnRadioTxMgmtFrames,
       "gwnRadioTxDataFrames": gwnRadioTxDataFrames,
       "gwnRadioTxDataBytes": gwnRadioTxDataBytes,
       "gwnRadioTxDrops": gwnRadioTxDrops,
       "gwnRadioRxTotalFrames": gwnRadioRxTotalFrames,
       "gwnRadioRxDataFrames": gwnRadioRxDataFrames,
       "gwnRadioRxDataBytes": gwnRadioRxDataBytes,
       "gwnRadioRxMgmtFrames": gwnRadioRxMgmtFrames,
       "gwnRadioRxBad": gwnRadioRxBad,
       "gwnWlanTable": gwnWlanTable,
       "gwnWlanEntry": gwnWlanEntry,
       "gwnWlanIndex": gwnWlanIndex,
       "gwnWlanESSID": gwnWlanESSID,
       "gwnWlanBSSID": gwnWlanBSSID,
       "gwnWlanTxTotalFrames": gwnWlanTxTotalFrames,
       "gwnWlanTxDataFrames": gwnWlanTxDataFrames,
       "gwnWlanTxDataBytes": gwnWlanTxDataBytes,
       "gwnWlanRxTotalFrames": gwnWlanRxTotalFrames,
       "gwnWlanRxDataFrames": gwnWlanRxDataFrames,
       "gwnWlanRxDataBytes": gwnWlanRxDataBytes,
       "gwnClientTable": gwnClientTable,
       "gwnClientEntry": gwnClientEntry,
       "gwnClientMACAddress": gwnClientMACAddress,
       "gwnClienttIPAddress": gwnClienttIPAddress,
       "gwnClientWlanMACAddress": gwnClientWlanMACAddress,
       "gwnClientESSID": gwnClientESSID,
       "gwnClientRSSI": gwnClientRSSI,
       "gwnClientAssoctime": gwnClientAssoctime,
       "gwnClientManufacture": gwnClientManufacture,
       "gwnClientHostname": gwnClientHostname,
       "gwnClientOS": gwnClientOS,
       "gwnClientTxRate": gwnClientTxRate,
       "gwnClientTxDataFrames": gwnClientTxDataFrames,
       "gwnClientTxDataBytes": gwnClientTxDataBytes,
       "gwnClientRxRate": gwnClientRxRate,
       "gwnClientRxDataFrames": gwnClientRxDataFrames,
       "gwnClientRxDataBytes": gwnClientRxDataBytes}
)
