# SNMP MIB module (JUNIPER-WLAN-WAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\juniper\junos\JUNIPER-WLAN-WAP-MIB

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

(jnxWlanWAPStatusMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxWlanWAPStatusMibRoot")

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

jnxWlanWAPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1)
)
if mibBuilder.loadTexts:
    jnxWlanWAPMIB.setRevisions(
        ("2019-06-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxWlanWAPStatusObjects_ObjectIdentity = ObjectIdentity
jnxWlanWAPStatusObjects = _JnxWlanWAPStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1)
)
_JnxWlanWAPStatusTable_Object = MibTable
jnxWlanWAPStatusTable = _JnxWlanWAPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxWlanWAPStatusTable.setStatus("current")
_JnxWlanWAPStatusEntry_Object = MibTableRow
jnxWlanWAPStatusEntry = _JnxWlanWAPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1)
)
jnxWlanWAPStatusEntry.setIndexNames(
    (0, "JUNIPER-WLAN-WAP-MIB", "jnxWAPStatusIfdIndex"),
)
if mibBuilder.loadTexts:
    jnxWlanWAPStatusEntry.setStatus("current")


class _JnxWAPStatusIfdIndex_Type(Integer32):
    """Custom type jnxWAPStatusIfdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_JnxWAPStatusIfdIndex_Type.__name__ = "Integer32"
_JnxWAPStatusIfdIndex_Object = MibTableColumn
jnxWAPStatusIfdIndex = _JnxWAPStatusIfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 1),
    _JnxWAPStatusIfdIndex_Type()
)
jnxWAPStatusIfdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWAPStatusIfdIndex.setStatus("current")
_JnxWAPStatusAccessPoint_Type = DisplayString
_JnxWAPStatusAccessPoint_Object = MibTableColumn
jnxWAPStatusAccessPoint = _JnxWAPStatusAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 2),
    _JnxWAPStatusAccessPoint_Type()
)
jnxWAPStatusAccessPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusAccessPoint.setStatus("current")
_JnxWAPStatusType_Type = DisplayString
_JnxWAPStatusType_Object = MibTableColumn
jnxWAPStatusType = _JnxWAPStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 3),
    _JnxWAPStatusType_Type()
)
jnxWAPStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusType.setStatus("current")
_JnxWAPStatusLocation_Type = DisplayString
_JnxWAPStatusLocation_Object = MibTableColumn
jnxWAPStatusLocation = _JnxWAPStatusLocation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 4),
    _JnxWAPStatusLocation_Type()
)
jnxWAPStatusLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusLocation.setStatus("current")
_JnxWAPStatusSerialNumber_Type = DisplayString
_JnxWAPStatusSerialNumber_Object = MibTableColumn
jnxWAPStatusSerialNumber = _JnxWAPStatusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 5),
    _JnxWAPStatusSerialNumber_Type()
)
jnxWAPStatusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusSerialNumber.setStatus("current")
_JnxWAPStatusFirmwareVersion_Type = DisplayString
_JnxWAPStatusFirmwareVersion_Object = MibTableColumn
jnxWAPStatusFirmwareVersion = _JnxWAPStatusFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 6),
    _JnxWAPStatusFirmwareVersion_Type()
)
jnxWAPStatusFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusFirmwareVersion.setStatus("current")
_JnxWAPStatusAlternateVersion_Type = DisplayString
_JnxWAPStatusAlternateVersion_Object = MibTableColumn
jnxWAPStatusAlternateVersion = _JnxWAPStatusAlternateVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 7),
    _JnxWAPStatusAlternateVersion_Type()
)
jnxWAPStatusAlternateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusAlternateVersion.setStatus("current")
_JnxWAPStatusCountry_Type = DisplayString
_JnxWAPStatusCountry_Object = MibTableColumn
jnxWAPStatusCountry = _JnxWAPStatusCountry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 8),
    _JnxWAPStatusCountry_Type()
)
jnxWAPStatusCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusCountry.setStatus("current")
_JnxWAPStatusAccessInterface_Type = DisplayString
_JnxWAPStatusAccessInterface_Object = MibTableColumn
jnxWAPStatusAccessInterface = _JnxWAPStatusAccessInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 9),
    _JnxWAPStatusAccessInterface_Type()
)
jnxWAPStatusAccessInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusAccessInterface.setStatus("current")
_JnxWAPStatusSystemTime_Type = DisplayString
_JnxWAPStatusSystemTime_Object = MibTableColumn
jnxWAPStatusSystemTime = _JnxWAPStatusSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 10),
    _JnxWAPStatusSystemTime_Type()
)
jnxWAPStatusSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusSystemTime.setStatus("current")
_JnxWAPStatusPacketCapture_Type = DisplayString
_JnxWAPStatusPacketCapture_Object = MibTableColumn
jnxWAPStatusPacketCapture = _JnxWAPStatusPacketCapture_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 11),
    _JnxWAPStatusPacketCapture_Type()
)
jnxWAPStatusPacketCapture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusPacketCapture.setStatus("current")
_JnxWAPStatusEthernetPortMAC_Type = DisplayString
_JnxWAPStatusEthernetPortMAC_Object = MibTableColumn
jnxWAPStatusEthernetPortMAC = _JnxWAPStatusEthernetPortMAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 12),
    _JnxWAPStatusEthernetPortMAC_Type()
)
jnxWAPStatusEthernetPortMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusEthernetPortMAC.setStatus("current")
_JnxWAPStatusEthernetIPv4_Type = IpAddress
_JnxWAPStatusEthernetIPv4_Object = MibTableColumn
jnxWAPStatusEthernetIPv4 = _JnxWAPStatusEthernetIPv4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 13),
    _JnxWAPStatusEthernetIPv4_Type()
)
jnxWAPStatusEthernetIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusEthernetIPv4.setStatus("current")
_JnxWAPStatusRadio1Status_Type = DisplayString
_JnxWAPStatusRadio1Status_Object = MibTableColumn
jnxWAPStatusRadio1Status = _JnxWAPStatusRadio1Status_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 14),
    _JnxWAPStatusRadio1Status_Type()
)
jnxWAPStatusRadio1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1Status.setStatus("current")
_JnxWAPStatusRadio1MAC_Type = DisplayString
_JnxWAPStatusRadio1MAC_Object = MibTableColumn
jnxWAPStatusRadio1MAC = _JnxWAPStatusRadio1MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 15),
    _JnxWAPStatusRadio1MAC_Type()
)
jnxWAPStatusRadio1MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1MAC.setStatus("current")
_JnxWAPStatusRadio1Mode_Type = DisplayString
_JnxWAPStatusRadio1Mode_Object = MibTableColumn
jnxWAPStatusRadio1Mode = _JnxWAPStatusRadio1Mode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 16),
    _JnxWAPStatusRadio1Mode_Type()
)
jnxWAPStatusRadio1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1Mode.setStatus("current")
_JnxWAPStatusRadio1Channel_Type = DisplayString
_JnxWAPStatusRadio1Channel_Object = MibTableColumn
jnxWAPStatusRadio1Channel = _JnxWAPStatusRadio1Channel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 17),
    _JnxWAPStatusRadio1Channel_Type()
)
jnxWAPStatusRadio1Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1Channel.setStatus("current")
_JnxWAPStatusRadio1Bandwidth_Type = DisplayString
_JnxWAPStatusRadio1Bandwidth_Object = MibTableColumn
jnxWAPStatusRadio1Bandwidth = _JnxWAPStatusRadio1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 18),
    _JnxWAPStatusRadio1Bandwidth_Type()
)
jnxWAPStatusRadio1Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1Bandwidth.setStatus("current")
_JnxWAPStatusRadio1VAP0SSID_Type = DisplayString
_JnxWAPStatusRadio1VAP0SSID_Object = MibTableColumn
jnxWAPStatusRadio1VAP0SSID = _JnxWAPStatusRadio1VAP0SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 19),
    _JnxWAPStatusRadio1VAP0SSID_Type()
)
jnxWAPStatusRadio1VAP0SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP0SSID.setStatus("current")
_JnxWAPStatusRadio1VAP0MAC_Type = DisplayString
_JnxWAPStatusRadio1VAP0MAC_Object = MibTableColumn
jnxWAPStatusRadio1VAP0MAC = _JnxWAPStatusRadio1VAP0MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 20),
    _JnxWAPStatusRadio1VAP0MAC_Type()
)
jnxWAPStatusRadio1VAP0MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP0MAC.setStatus("current")
_JnxWAPStatusRadio1VAP0VLANID_Type = Counter32
_JnxWAPStatusRadio1VAP0VLANID_Object = MibTableColumn
jnxWAPStatusRadio1VAP0VLANID = _JnxWAPStatusRadio1VAP0VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 21),
    _JnxWAPStatusRadio1VAP0VLANID_Type()
)
jnxWAPStatusRadio1VAP0VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP0VLANID.setStatus("current")
_JnxWAPStatusRadio1VAP0InputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP0InputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP0InputBytes = _JnxWAPStatusRadio1VAP0InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 22),
    _JnxWAPStatusRadio1VAP0InputBytes_Type()
)
jnxWAPStatusRadio1VAP0InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP0InputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP0OutputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP0OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP0OutputBytes = _JnxWAPStatusRadio1VAP0OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 23),
    _JnxWAPStatusRadio1VAP0OutputBytes_Type()
)
jnxWAPStatusRadio1VAP0OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP0OutputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP0InputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP0InputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP0InputPackets = _JnxWAPStatusRadio1VAP0InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 24),
    _JnxWAPStatusRadio1VAP0InputPackets_Type()
)
jnxWAPStatusRadio1VAP0InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP0InputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP0OutputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP0OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP0OutputPackets = _JnxWAPStatusRadio1VAP0OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 25),
    _JnxWAPStatusRadio1VAP0OutputPackets_Type()
)
jnxWAPStatusRadio1VAP0OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP0OutputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP1SSID_Type = DisplayString
_JnxWAPStatusRadio1VAP1SSID_Object = MibTableColumn
jnxWAPStatusRadio1VAP1SSID = _JnxWAPStatusRadio1VAP1SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 26),
    _JnxWAPStatusRadio1VAP1SSID_Type()
)
jnxWAPStatusRadio1VAP1SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP1SSID.setStatus("current")
_JnxWAPStatusRadio1VAP1MAC_Type = DisplayString
_JnxWAPStatusRadio1VAP1MAC_Object = MibTableColumn
jnxWAPStatusRadio1VAP1MAC = _JnxWAPStatusRadio1VAP1MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 27),
    _JnxWAPStatusRadio1VAP1MAC_Type()
)
jnxWAPStatusRadio1VAP1MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP1MAC.setStatus("current")
_JnxWAPStatusRadio1VAP1VLANID_Type = Counter32
_JnxWAPStatusRadio1VAP1VLANID_Object = MibTableColumn
jnxWAPStatusRadio1VAP1VLANID = _JnxWAPStatusRadio1VAP1VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 28),
    _JnxWAPStatusRadio1VAP1VLANID_Type()
)
jnxWAPStatusRadio1VAP1VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP1VLANID.setStatus("current")
_JnxWAPStatusRadio1VAP1InputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP1InputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP1InputBytes = _JnxWAPStatusRadio1VAP1InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 29),
    _JnxWAPStatusRadio1VAP1InputBytes_Type()
)
jnxWAPStatusRadio1VAP1InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP1InputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP1OutputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP1OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP1OutputBytes = _JnxWAPStatusRadio1VAP1OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 30),
    _JnxWAPStatusRadio1VAP1OutputBytes_Type()
)
jnxWAPStatusRadio1VAP1OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP1OutputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP1InputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP1InputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP1InputPackets = _JnxWAPStatusRadio1VAP1InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 31),
    _JnxWAPStatusRadio1VAP1InputPackets_Type()
)
jnxWAPStatusRadio1VAP1InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP1InputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP1OutputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP1OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP1OutputPackets = _JnxWAPStatusRadio1VAP1OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 32),
    _JnxWAPStatusRadio1VAP1OutputPackets_Type()
)
jnxWAPStatusRadio1VAP1OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP1OutputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP2SSID_Type = DisplayString
_JnxWAPStatusRadio1VAP2SSID_Object = MibTableColumn
jnxWAPStatusRadio1VAP2SSID = _JnxWAPStatusRadio1VAP2SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 33),
    _JnxWAPStatusRadio1VAP2SSID_Type()
)
jnxWAPStatusRadio1VAP2SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP2SSID.setStatus("current")
_JnxWAPStatusRadio1VAP2MAC_Type = DisplayString
_JnxWAPStatusRadio1VAP2MAC_Object = MibTableColumn
jnxWAPStatusRadio1VAP2MAC = _JnxWAPStatusRadio1VAP2MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 34),
    _JnxWAPStatusRadio1VAP2MAC_Type()
)
jnxWAPStatusRadio1VAP2MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP2MAC.setStatus("current")
_JnxWAPStatusRadio1VAP2VLANID_Type = Counter32
_JnxWAPStatusRadio1VAP2VLANID_Object = MibTableColumn
jnxWAPStatusRadio1VAP2VLANID = _JnxWAPStatusRadio1VAP2VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 35),
    _JnxWAPStatusRadio1VAP2VLANID_Type()
)
jnxWAPStatusRadio1VAP2VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP2VLANID.setStatus("current")
_JnxWAPStatusRadio1VAP2InputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP2InputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP2InputBytes = _JnxWAPStatusRadio1VAP2InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 36),
    _JnxWAPStatusRadio1VAP2InputBytes_Type()
)
jnxWAPStatusRadio1VAP2InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP2InputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP2OutputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP2OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP2OutputBytes = _JnxWAPStatusRadio1VAP2OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 37),
    _JnxWAPStatusRadio1VAP2OutputBytes_Type()
)
jnxWAPStatusRadio1VAP2OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP2OutputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP2InputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP2InputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP2InputPackets = _JnxWAPStatusRadio1VAP2InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 38),
    _JnxWAPStatusRadio1VAP2InputPackets_Type()
)
jnxWAPStatusRadio1VAP2InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP2InputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP2OutputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP2OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP2OutputPackets = _JnxWAPStatusRadio1VAP2OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 39),
    _JnxWAPStatusRadio1VAP2OutputPackets_Type()
)
jnxWAPStatusRadio1VAP2OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP2OutputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP3SSID_Type = DisplayString
_JnxWAPStatusRadio1VAP3SSID_Object = MibTableColumn
jnxWAPStatusRadio1VAP3SSID = _JnxWAPStatusRadio1VAP3SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 40),
    _JnxWAPStatusRadio1VAP3SSID_Type()
)
jnxWAPStatusRadio1VAP3SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP3SSID.setStatus("current")
_JnxWAPStatusRadio1VAP3MAC_Type = DisplayString
_JnxWAPStatusRadio1VAP3MAC_Object = MibTableColumn
jnxWAPStatusRadio1VAP3MAC = _JnxWAPStatusRadio1VAP3MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 41),
    _JnxWAPStatusRadio1VAP3MAC_Type()
)
jnxWAPStatusRadio1VAP3MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP3MAC.setStatus("current")
_JnxWAPStatusRadio1VAP3VLANID_Type = Counter32
_JnxWAPStatusRadio1VAP3VLANID_Object = MibTableColumn
jnxWAPStatusRadio1VAP3VLANID = _JnxWAPStatusRadio1VAP3VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 42),
    _JnxWAPStatusRadio1VAP3VLANID_Type()
)
jnxWAPStatusRadio1VAP3VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP3VLANID.setStatus("current")
_JnxWAPStatusRadio1VAP3InputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP3InputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP3InputBytes = _JnxWAPStatusRadio1VAP3InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 43),
    _JnxWAPStatusRadio1VAP3InputBytes_Type()
)
jnxWAPStatusRadio1VAP3InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP3InputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP3OutputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP3OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP3OutputBytes = _JnxWAPStatusRadio1VAP3OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 44),
    _JnxWAPStatusRadio1VAP3OutputBytes_Type()
)
jnxWAPStatusRadio1VAP3OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP3OutputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP3InputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP3InputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP3InputPackets = _JnxWAPStatusRadio1VAP3InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 45),
    _JnxWAPStatusRadio1VAP3InputPackets_Type()
)
jnxWAPStatusRadio1VAP3InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP3InputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP3OutputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP3OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP3OutputPackets = _JnxWAPStatusRadio1VAP3OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 46),
    _JnxWAPStatusRadio1VAP3OutputPackets_Type()
)
jnxWAPStatusRadio1VAP3OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP3OutputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP4SSID_Type = DisplayString
_JnxWAPStatusRadio1VAP4SSID_Object = MibTableColumn
jnxWAPStatusRadio1VAP4SSID = _JnxWAPStatusRadio1VAP4SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 47),
    _JnxWAPStatusRadio1VAP4SSID_Type()
)
jnxWAPStatusRadio1VAP4SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP4SSID.setStatus("current")
_JnxWAPStatusRadio1VAP4MAC_Type = DisplayString
_JnxWAPStatusRadio1VAP4MAC_Object = MibTableColumn
jnxWAPStatusRadio1VAP4MAC = _JnxWAPStatusRadio1VAP4MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 48),
    _JnxWAPStatusRadio1VAP4MAC_Type()
)
jnxWAPStatusRadio1VAP4MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP4MAC.setStatus("current")
_JnxWAPStatusRadio1VAP4VLANID_Type = Counter32
_JnxWAPStatusRadio1VAP4VLANID_Object = MibTableColumn
jnxWAPStatusRadio1VAP4VLANID = _JnxWAPStatusRadio1VAP4VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 49),
    _JnxWAPStatusRadio1VAP4VLANID_Type()
)
jnxWAPStatusRadio1VAP4VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP4VLANID.setStatus("current")
_JnxWAPStatusRadio1VAP4InputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP4InputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP4InputBytes = _JnxWAPStatusRadio1VAP4InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 50),
    _JnxWAPStatusRadio1VAP4InputBytes_Type()
)
jnxWAPStatusRadio1VAP4InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP4InputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP4OutputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP4OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP4OutputBytes = _JnxWAPStatusRadio1VAP4OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 51),
    _JnxWAPStatusRadio1VAP4OutputBytes_Type()
)
jnxWAPStatusRadio1VAP4OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP4OutputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP4InputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP4InputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP4InputPackets = _JnxWAPStatusRadio1VAP4InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 52),
    _JnxWAPStatusRadio1VAP4InputPackets_Type()
)
jnxWAPStatusRadio1VAP4InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP4InputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP4OutputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP4OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP4OutputPackets = _JnxWAPStatusRadio1VAP4OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 53),
    _JnxWAPStatusRadio1VAP4OutputPackets_Type()
)
jnxWAPStatusRadio1VAP4OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP4OutputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP5SSID_Type = DisplayString
_JnxWAPStatusRadio1VAP5SSID_Object = MibTableColumn
jnxWAPStatusRadio1VAP5SSID = _JnxWAPStatusRadio1VAP5SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 54),
    _JnxWAPStatusRadio1VAP5SSID_Type()
)
jnxWAPStatusRadio1VAP5SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP5SSID.setStatus("current")
_JnxWAPStatusRadio1VAP5MAC_Type = DisplayString
_JnxWAPStatusRadio1VAP5MAC_Object = MibTableColumn
jnxWAPStatusRadio1VAP5MAC = _JnxWAPStatusRadio1VAP5MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 55),
    _JnxWAPStatusRadio1VAP5MAC_Type()
)
jnxWAPStatusRadio1VAP5MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP5MAC.setStatus("current")
_JnxWAPStatusRadio1VAP5VLANID_Type = Counter32
_JnxWAPStatusRadio1VAP5VLANID_Object = MibTableColumn
jnxWAPStatusRadio1VAP5VLANID = _JnxWAPStatusRadio1VAP5VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 56),
    _JnxWAPStatusRadio1VAP5VLANID_Type()
)
jnxWAPStatusRadio1VAP5VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP5VLANID.setStatus("current")
_JnxWAPStatusRadio1VAP5InputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP5InputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP5InputBytes = _JnxWAPStatusRadio1VAP5InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 57),
    _JnxWAPStatusRadio1VAP5InputBytes_Type()
)
jnxWAPStatusRadio1VAP5InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP5InputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP5OutputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP5OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP5OutputBytes = _JnxWAPStatusRadio1VAP5OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 58),
    _JnxWAPStatusRadio1VAP5OutputBytes_Type()
)
jnxWAPStatusRadio1VAP5OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP5OutputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP5InputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP5InputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP5InputPackets = _JnxWAPStatusRadio1VAP5InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 59),
    _JnxWAPStatusRadio1VAP5InputPackets_Type()
)
jnxWAPStatusRadio1VAP5InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP5InputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP5OutputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP5OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP5OutputPackets = _JnxWAPStatusRadio1VAP5OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 60),
    _JnxWAPStatusRadio1VAP5OutputPackets_Type()
)
jnxWAPStatusRadio1VAP5OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP5OutputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP6SSID_Type = DisplayString
_JnxWAPStatusRadio1VAP6SSID_Object = MibTableColumn
jnxWAPStatusRadio1VAP6SSID = _JnxWAPStatusRadio1VAP6SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 61),
    _JnxWAPStatusRadio1VAP6SSID_Type()
)
jnxWAPStatusRadio1VAP6SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP6SSID.setStatus("current")
_JnxWAPStatusRadio1VAP6MAC_Type = DisplayString
_JnxWAPStatusRadio1VAP6MAC_Object = MibTableColumn
jnxWAPStatusRadio1VAP6MAC = _JnxWAPStatusRadio1VAP6MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 62),
    _JnxWAPStatusRadio1VAP6MAC_Type()
)
jnxWAPStatusRadio1VAP6MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP6MAC.setStatus("current")
_JnxWAPStatusRadio1VAP6VLANID_Type = Counter32
_JnxWAPStatusRadio1VAP6VLANID_Object = MibTableColumn
jnxWAPStatusRadio1VAP6VLANID = _JnxWAPStatusRadio1VAP6VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 63),
    _JnxWAPStatusRadio1VAP6VLANID_Type()
)
jnxWAPStatusRadio1VAP6VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP6VLANID.setStatus("current")
_JnxWAPStatusRadio1VAP6InputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP6InputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP6InputBytes = _JnxWAPStatusRadio1VAP6InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 64),
    _JnxWAPStatusRadio1VAP6InputBytes_Type()
)
jnxWAPStatusRadio1VAP6InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP6InputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP6OutputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP6OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP6OutputBytes = _JnxWAPStatusRadio1VAP6OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 65),
    _JnxWAPStatusRadio1VAP6OutputBytes_Type()
)
jnxWAPStatusRadio1VAP6OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP6OutputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP6InputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP6InputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP6InputPackets = _JnxWAPStatusRadio1VAP6InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 66),
    _JnxWAPStatusRadio1VAP6InputPackets_Type()
)
jnxWAPStatusRadio1VAP6InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP6InputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP6OutputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP6OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP6OutputPackets = _JnxWAPStatusRadio1VAP6OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 67),
    _JnxWAPStatusRadio1VAP6OutputPackets_Type()
)
jnxWAPStatusRadio1VAP6OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP6OutputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP7SSID_Type = DisplayString
_JnxWAPStatusRadio1VAP7SSID_Object = MibTableColumn
jnxWAPStatusRadio1VAP7SSID = _JnxWAPStatusRadio1VAP7SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 68),
    _JnxWAPStatusRadio1VAP7SSID_Type()
)
jnxWAPStatusRadio1VAP7SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP7SSID.setStatus("current")
_JnxWAPStatusRadio1VAP7MAC_Type = DisplayString
_JnxWAPStatusRadio1VAP7MAC_Object = MibTableColumn
jnxWAPStatusRadio1VAP7MAC = _JnxWAPStatusRadio1VAP7MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 69),
    _JnxWAPStatusRadio1VAP7MAC_Type()
)
jnxWAPStatusRadio1VAP7MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP7MAC.setStatus("current")
_JnxWAPStatusRadio1VAP7VLANID_Type = Counter32
_JnxWAPStatusRadio1VAP7VLANID_Object = MibTableColumn
jnxWAPStatusRadio1VAP7VLANID = _JnxWAPStatusRadio1VAP7VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 70),
    _JnxWAPStatusRadio1VAP7VLANID_Type()
)
jnxWAPStatusRadio1VAP7VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP7VLANID.setStatus("current")
_JnxWAPStatusRadio1VAP7InputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP7InputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP7InputBytes = _JnxWAPStatusRadio1VAP7InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 71),
    _JnxWAPStatusRadio1VAP7InputBytes_Type()
)
jnxWAPStatusRadio1VAP7InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP7InputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP7OutputBytes_Type = Counter64
_JnxWAPStatusRadio1VAP7OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio1VAP7OutputBytes = _JnxWAPStatusRadio1VAP7OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 72),
    _JnxWAPStatusRadio1VAP7OutputBytes_Type()
)
jnxWAPStatusRadio1VAP7OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP7OutputBytes.setStatus("current")
_JnxWAPStatusRadio1VAP7InputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP7InputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP7InputPackets = _JnxWAPStatusRadio1VAP7InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 73),
    _JnxWAPStatusRadio1VAP7InputPackets_Type()
)
jnxWAPStatusRadio1VAP7InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP7InputPackets.setStatus("current")
_JnxWAPStatusRadio1VAP7OutputPackets_Type = Counter64
_JnxWAPStatusRadio1VAP7OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio1VAP7OutputPackets = _JnxWAPStatusRadio1VAP7OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 74),
    _JnxWAPStatusRadio1VAP7OutputPackets_Type()
)
jnxWAPStatusRadio1VAP7OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio1VAP7OutputPackets.setStatus("current")
_JnxWAPStatusRadio2Status_Type = DisplayString
_JnxWAPStatusRadio2Status_Object = MibTableColumn
jnxWAPStatusRadio2Status = _JnxWAPStatusRadio2Status_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 75),
    _JnxWAPStatusRadio2Status_Type()
)
jnxWAPStatusRadio2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2Status.setStatus("current")
_JnxWAPStatusRadio2MAC_Type = DisplayString
_JnxWAPStatusRadio2MAC_Object = MibTableColumn
jnxWAPStatusRadio2MAC = _JnxWAPStatusRadio2MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 76),
    _JnxWAPStatusRadio2MAC_Type()
)
jnxWAPStatusRadio2MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2MAC.setStatus("current")
_JnxWAPStatusRadio2Mode_Type = DisplayString
_JnxWAPStatusRadio2Mode_Object = MibTableColumn
jnxWAPStatusRadio2Mode = _JnxWAPStatusRadio2Mode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 77),
    _JnxWAPStatusRadio2Mode_Type()
)
jnxWAPStatusRadio2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2Mode.setStatus("current")
_JnxWAPStatusRadio2Channel_Type = DisplayString
_JnxWAPStatusRadio2Channel_Object = MibTableColumn
jnxWAPStatusRadio2Channel = _JnxWAPStatusRadio2Channel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 78),
    _JnxWAPStatusRadio2Channel_Type()
)
jnxWAPStatusRadio2Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2Channel.setStatus("current")
_JnxWAPStatusRadio2Bandwidth_Type = DisplayString
_JnxWAPStatusRadio2Bandwidth_Object = MibTableColumn
jnxWAPStatusRadio2Bandwidth = _JnxWAPStatusRadio2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 79),
    _JnxWAPStatusRadio2Bandwidth_Type()
)
jnxWAPStatusRadio2Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2Bandwidth.setStatus("current")
_JnxWAPStatusRadio2VAP0SSID_Type = DisplayString
_JnxWAPStatusRadio2VAP0SSID_Object = MibTableColumn
jnxWAPStatusRadio2VAP0SSID = _JnxWAPStatusRadio2VAP0SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 80),
    _JnxWAPStatusRadio2VAP0SSID_Type()
)
jnxWAPStatusRadio2VAP0SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP0SSID.setStatus("current")
_JnxWAPStatusRadio2VAP0MAC_Type = DisplayString
_JnxWAPStatusRadio2VAP0MAC_Object = MibTableColumn
jnxWAPStatusRadio2VAP0MAC = _JnxWAPStatusRadio2VAP0MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 81),
    _JnxWAPStatusRadio2VAP0MAC_Type()
)
jnxWAPStatusRadio2VAP0MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP0MAC.setStatus("current")
_JnxWAPStatusRadio2VAP0VLANID_Type = Counter32
_JnxWAPStatusRadio2VAP0VLANID_Object = MibTableColumn
jnxWAPStatusRadio2VAP0VLANID = _JnxWAPStatusRadio2VAP0VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 82),
    _JnxWAPStatusRadio2VAP0VLANID_Type()
)
jnxWAPStatusRadio2VAP0VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP0VLANID.setStatus("current")
_JnxWAPStatusRadio2VAP0InputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP0InputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP0InputBytes = _JnxWAPStatusRadio2VAP0InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 83),
    _JnxWAPStatusRadio2VAP0InputBytes_Type()
)
jnxWAPStatusRadio2VAP0InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP0InputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP0OutputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP0OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP0OutputBytes = _JnxWAPStatusRadio2VAP0OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 84),
    _JnxWAPStatusRadio2VAP0OutputBytes_Type()
)
jnxWAPStatusRadio2VAP0OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP0OutputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP0InputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP0InputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP0InputPackets = _JnxWAPStatusRadio2VAP0InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 85),
    _JnxWAPStatusRadio2VAP0InputPackets_Type()
)
jnxWAPStatusRadio2VAP0InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP0InputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP0OutputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP0OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP0OutputPackets = _JnxWAPStatusRadio2VAP0OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 86),
    _JnxWAPStatusRadio2VAP0OutputPackets_Type()
)
jnxWAPStatusRadio2VAP0OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP0OutputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP1SSID_Type = DisplayString
_JnxWAPStatusRadio2VAP1SSID_Object = MibTableColumn
jnxWAPStatusRadio2VAP1SSID = _JnxWAPStatusRadio2VAP1SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 87),
    _JnxWAPStatusRadio2VAP1SSID_Type()
)
jnxWAPStatusRadio2VAP1SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP1SSID.setStatus("current")
_JnxWAPStatusRadio2VAP1MAC_Type = DisplayString
_JnxWAPStatusRadio2VAP1MAC_Object = MibTableColumn
jnxWAPStatusRadio2VAP1MAC = _JnxWAPStatusRadio2VAP1MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 88),
    _JnxWAPStatusRadio2VAP1MAC_Type()
)
jnxWAPStatusRadio2VAP1MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP1MAC.setStatus("current")
_JnxWAPStatusRadio2VAP1VLANID_Type = Counter32
_JnxWAPStatusRadio2VAP1VLANID_Object = MibTableColumn
jnxWAPStatusRadio2VAP1VLANID = _JnxWAPStatusRadio2VAP1VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 89),
    _JnxWAPStatusRadio2VAP1VLANID_Type()
)
jnxWAPStatusRadio2VAP1VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP1VLANID.setStatus("current")
_JnxWAPStatusRadio2VAP1InputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP1InputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP1InputBytes = _JnxWAPStatusRadio2VAP1InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 90),
    _JnxWAPStatusRadio2VAP1InputBytes_Type()
)
jnxWAPStatusRadio2VAP1InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP1InputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP1OutputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP1OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP1OutputBytes = _JnxWAPStatusRadio2VAP1OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 91),
    _JnxWAPStatusRadio2VAP1OutputBytes_Type()
)
jnxWAPStatusRadio2VAP1OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP1OutputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP1InputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP1InputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP1InputPackets = _JnxWAPStatusRadio2VAP1InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 92),
    _JnxWAPStatusRadio2VAP1InputPackets_Type()
)
jnxWAPStatusRadio2VAP1InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP1InputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP1OutputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP1OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP1OutputPackets = _JnxWAPStatusRadio2VAP1OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 93),
    _JnxWAPStatusRadio2VAP1OutputPackets_Type()
)
jnxWAPStatusRadio2VAP1OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP1OutputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP2SSID_Type = DisplayString
_JnxWAPStatusRadio2VAP2SSID_Object = MibTableColumn
jnxWAPStatusRadio2VAP2SSID = _JnxWAPStatusRadio2VAP2SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 94),
    _JnxWAPStatusRadio2VAP2SSID_Type()
)
jnxWAPStatusRadio2VAP2SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP2SSID.setStatus("current")
_JnxWAPStatusRadio2VAP2MAC_Type = DisplayString
_JnxWAPStatusRadio2VAP2MAC_Object = MibTableColumn
jnxWAPStatusRadio2VAP2MAC = _JnxWAPStatusRadio2VAP2MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 95),
    _JnxWAPStatusRadio2VAP2MAC_Type()
)
jnxWAPStatusRadio2VAP2MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP2MAC.setStatus("current")
_JnxWAPStatusRadio2VAP2VLANID_Type = Counter32
_JnxWAPStatusRadio2VAP2VLANID_Object = MibTableColumn
jnxWAPStatusRadio2VAP2VLANID = _JnxWAPStatusRadio2VAP2VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 96),
    _JnxWAPStatusRadio2VAP2VLANID_Type()
)
jnxWAPStatusRadio2VAP2VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP2VLANID.setStatus("current")
_JnxWAPStatusRadio2VAP2InputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP2InputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP2InputBytes = _JnxWAPStatusRadio2VAP2InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 97),
    _JnxWAPStatusRadio2VAP2InputBytes_Type()
)
jnxWAPStatusRadio2VAP2InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP2InputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP2OutputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP2OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP2OutputBytes = _JnxWAPStatusRadio2VAP2OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 98),
    _JnxWAPStatusRadio2VAP2OutputBytes_Type()
)
jnxWAPStatusRadio2VAP2OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP2OutputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP2InputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP2InputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP2InputPackets = _JnxWAPStatusRadio2VAP2InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 99),
    _JnxWAPStatusRadio2VAP2InputPackets_Type()
)
jnxWAPStatusRadio2VAP2InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP2InputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP2OutputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP2OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP2OutputPackets = _JnxWAPStatusRadio2VAP2OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 100),
    _JnxWAPStatusRadio2VAP2OutputPackets_Type()
)
jnxWAPStatusRadio2VAP2OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP2OutputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP3SSID_Type = DisplayString
_JnxWAPStatusRadio2VAP3SSID_Object = MibTableColumn
jnxWAPStatusRadio2VAP3SSID = _JnxWAPStatusRadio2VAP3SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 101),
    _JnxWAPStatusRadio2VAP3SSID_Type()
)
jnxWAPStatusRadio2VAP3SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP3SSID.setStatus("current")
_JnxWAPStatusRadio2VAP3MAC_Type = DisplayString
_JnxWAPStatusRadio2VAP3MAC_Object = MibTableColumn
jnxWAPStatusRadio2VAP3MAC = _JnxWAPStatusRadio2VAP3MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 102),
    _JnxWAPStatusRadio2VAP3MAC_Type()
)
jnxWAPStatusRadio2VAP3MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP3MAC.setStatus("current")
_JnxWAPStatusRadio2VAP3VLANID_Type = Counter32
_JnxWAPStatusRadio2VAP3VLANID_Object = MibTableColumn
jnxWAPStatusRadio2VAP3VLANID = _JnxWAPStatusRadio2VAP3VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 103),
    _JnxWAPStatusRadio2VAP3VLANID_Type()
)
jnxWAPStatusRadio2VAP3VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP3VLANID.setStatus("current")
_JnxWAPStatusRadio2VAP3InputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP3InputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP3InputBytes = _JnxWAPStatusRadio2VAP3InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 104),
    _JnxWAPStatusRadio2VAP3InputBytes_Type()
)
jnxWAPStatusRadio2VAP3InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP3InputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP3OutputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP3OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP3OutputBytes = _JnxWAPStatusRadio2VAP3OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 105),
    _JnxWAPStatusRadio2VAP3OutputBytes_Type()
)
jnxWAPStatusRadio2VAP3OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP3OutputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP3InputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP3InputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP3InputPackets = _JnxWAPStatusRadio2VAP3InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 106),
    _JnxWAPStatusRadio2VAP3InputPackets_Type()
)
jnxWAPStatusRadio2VAP3InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP3InputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP3OutputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP3OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP3OutputPackets = _JnxWAPStatusRadio2VAP3OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 107),
    _JnxWAPStatusRadio2VAP3OutputPackets_Type()
)
jnxWAPStatusRadio2VAP3OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP3OutputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP4SSID_Type = DisplayString
_JnxWAPStatusRadio2VAP4SSID_Object = MibTableColumn
jnxWAPStatusRadio2VAP4SSID = _JnxWAPStatusRadio2VAP4SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 108),
    _JnxWAPStatusRadio2VAP4SSID_Type()
)
jnxWAPStatusRadio2VAP4SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP4SSID.setStatus("current")
_JnxWAPStatusRadio2VAP4MAC_Type = DisplayString
_JnxWAPStatusRadio2VAP4MAC_Object = MibTableColumn
jnxWAPStatusRadio2VAP4MAC = _JnxWAPStatusRadio2VAP4MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 109),
    _JnxWAPStatusRadio2VAP4MAC_Type()
)
jnxWAPStatusRadio2VAP4MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP4MAC.setStatus("current")
_JnxWAPStatusRadio2VAP4VLANID_Type = Counter32
_JnxWAPStatusRadio2VAP4VLANID_Object = MibTableColumn
jnxWAPStatusRadio2VAP4VLANID = _JnxWAPStatusRadio2VAP4VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 110),
    _JnxWAPStatusRadio2VAP4VLANID_Type()
)
jnxWAPStatusRadio2VAP4VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP4VLANID.setStatus("current")
_JnxWAPStatusRadio2VAP4InputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP4InputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP4InputBytes = _JnxWAPStatusRadio2VAP4InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 111),
    _JnxWAPStatusRadio2VAP4InputBytes_Type()
)
jnxWAPStatusRadio2VAP4InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP4InputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP4OutputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP4OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP4OutputBytes = _JnxWAPStatusRadio2VAP4OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 112),
    _JnxWAPStatusRadio2VAP4OutputBytes_Type()
)
jnxWAPStatusRadio2VAP4OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP4OutputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP4InputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP4InputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP4InputPackets = _JnxWAPStatusRadio2VAP4InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 113),
    _JnxWAPStatusRadio2VAP4InputPackets_Type()
)
jnxWAPStatusRadio2VAP4InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP4InputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP4OutputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP4OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP4OutputPackets = _JnxWAPStatusRadio2VAP4OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 114),
    _JnxWAPStatusRadio2VAP4OutputPackets_Type()
)
jnxWAPStatusRadio2VAP4OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP4OutputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP5SSID_Type = DisplayString
_JnxWAPStatusRadio2VAP5SSID_Object = MibTableColumn
jnxWAPStatusRadio2VAP5SSID = _JnxWAPStatusRadio2VAP5SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 115),
    _JnxWAPStatusRadio2VAP5SSID_Type()
)
jnxWAPStatusRadio2VAP5SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP5SSID.setStatus("current")
_JnxWAPStatusRadio2VAP5MAC_Type = DisplayString
_JnxWAPStatusRadio2VAP5MAC_Object = MibTableColumn
jnxWAPStatusRadio2VAP5MAC = _JnxWAPStatusRadio2VAP5MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 116),
    _JnxWAPStatusRadio2VAP5MAC_Type()
)
jnxWAPStatusRadio2VAP5MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP5MAC.setStatus("current")
_JnxWAPStatusRadio2VAP5VLANID_Type = Counter32
_JnxWAPStatusRadio2VAP5VLANID_Object = MibTableColumn
jnxWAPStatusRadio2VAP5VLANID = _JnxWAPStatusRadio2VAP5VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 117),
    _JnxWAPStatusRadio2VAP5VLANID_Type()
)
jnxWAPStatusRadio2VAP5VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP5VLANID.setStatus("current")
_JnxWAPStatusRadio2VAP5InputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP5InputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP5InputBytes = _JnxWAPStatusRadio2VAP5InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 118),
    _JnxWAPStatusRadio2VAP5InputBytes_Type()
)
jnxWAPStatusRadio2VAP5InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP5InputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP5OutputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP5OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP5OutputBytes = _JnxWAPStatusRadio2VAP5OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 119),
    _JnxWAPStatusRadio2VAP5OutputBytes_Type()
)
jnxWAPStatusRadio2VAP5OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP5OutputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP5InputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP5InputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP5InputPackets = _JnxWAPStatusRadio2VAP5InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 120),
    _JnxWAPStatusRadio2VAP5InputPackets_Type()
)
jnxWAPStatusRadio2VAP5InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP5InputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP5OutputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP5OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP5OutputPackets = _JnxWAPStatusRadio2VAP5OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 121),
    _JnxWAPStatusRadio2VAP5OutputPackets_Type()
)
jnxWAPStatusRadio2VAP5OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP5OutputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP6SSID_Type = DisplayString
_JnxWAPStatusRadio2VAP6SSID_Object = MibTableColumn
jnxWAPStatusRadio2VAP6SSID = _JnxWAPStatusRadio2VAP6SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 122),
    _JnxWAPStatusRadio2VAP6SSID_Type()
)
jnxWAPStatusRadio2VAP6SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP6SSID.setStatus("current")
_JnxWAPStatusRadio2VAP6MAC_Type = DisplayString
_JnxWAPStatusRadio2VAP6MAC_Object = MibTableColumn
jnxWAPStatusRadio2VAP6MAC = _JnxWAPStatusRadio2VAP6MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 123),
    _JnxWAPStatusRadio2VAP6MAC_Type()
)
jnxWAPStatusRadio2VAP6MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP6MAC.setStatus("current")
_JnxWAPStatusRadio2VAP6VLANID_Type = Counter32
_JnxWAPStatusRadio2VAP6VLANID_Object = MibTableColumn
jnxWAPStatusRadio2VAP6VLANID = _JnxWAPStatusRadio2VAP6VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 124),
    _JnxWAPStatusRadio2VAP6VLANID_Type()
)
jnxWAPStatusRadio2VAP6VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP6VLANID.setStatus("current")
_JnxWAPStatusRadio2VAP6InputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP6InputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP6InputBytes = _JnxWAPStatusRadio2VAP6InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 125),
    _JnxWAPStatusRadio2VAP6InputBytes_Type()
)
jnxWAPStatusRadio2VAP6InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP6InputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP6OutputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP6OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP6OutputBytes = _JnxWAPStatusRadio2VAP6OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 126),
    _JnxWAPStatusRadio2VAP6OutputBytes_Type()
)
jnxWAPStatusRadio2VAP6OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP6OutputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP6InputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP6InputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP6InputPackets = _JnxWAPStatusRadio2VAP6InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 127),
    _JnxWAPStatusRadio2VAP6InputPackets_Type()
)
jnxWAPStatusRadio2VAP6InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP6InputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP6OutputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP6OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP6OutputPackets = _JnxWAPStatusRadio2VAP6OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 128),
    _JnxWAPStatusRadio2VAP6OutputPackets_Type()
)
jnxWAPStatusRadio2VAP6OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP6OutputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP7SSID_Type = DisplayString
_JnxWAPStatusRadio2VAP7SSID_Object = MibTableColumn
jnxWAPStatusRadio2VAP7SSID = _JnxWAPStatusRadio2VAP7SSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 129),
    _JnxWAPStatusRadio2VAP7SSID_Type()
)
jnxWAPStatusRadio2VAP7SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP7SSID.setStatus("current")
_JnxWAPStatusRadio2VAP7MAC_Type = DisplayString
_JnxWAPStatusRadio2VAP7MAC_Object = MibTableColumn
jnxWAPStatusRadio2VAP7MAC = _JnxWAPStatusRadio2VAP7MAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 130),
    _JnxWAPStatusRadio2VAP7MAC_Type()
)
jnxWAPStatusRadio2VAP7MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP7MAC.setStatus("current")
_JnxWAPStatusRadio2VAP7VLANID_Type = Counter32
_JnxWAPStatusRadio2VAP7VLANID_Object = MibTableColumn
jnxWAPStatusRadio2VAP7VLANID = _JnxWAPStatusRadio2VAP7VLANID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 131),
    _JnxWAPStatusRadio2VAP7VLANID_Type()
)
jnxWAPStatusRadio2VAP7VLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP7VLANID.setStatus("current")
_JnxWAPStatusRadio2VAP7InputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP7InputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP7InputBytes = _JnxWAPStatusRadio2VAP7InputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 132),
    _JnxWAPStatusRadio2VAP7InputBytes_Type()
)
jnxWAPStatusRadio2VAP7InputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP7InputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP7OutputBytes_Type = Counter64
_JnxWAPStatusRadio2VAP7OutputBytes_Object = MibTableColumn
jnxWAPStatusRadio2VAP7OutputBytes = _JnxWAPStatusRadio2VAP7OutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 133),
    _JnxWAPStatusRadio2VAP7OutputBytes_Type()
)
jnxWAPStatusRadio2VAP7OutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP7OutputBytes.setStatus("current")
_JnxWAPStatusRadio2VAP7InputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP7InputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP7InputPackets = _JnxWAPStatusRadio2VAP7InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 134),
    _JnxWAPStatusRadio2VAP7InputPackets_Type()
)
jnxWAPStatusRadio2VAP7InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP7InputPackets.setStatus("current")
_JnxWAPStatusRadio2VAP7OutputPackets_Type = Counter64
_JnxWAPStatusRadio2VAP7OutputPackets_Object = MibTableColumn
jnxWAPStatusRadio2VAP7OutputPackets = _JnxWAPStatusRadio2VAP7OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 1, 1, 1, 135),
    _JnxWAPStatusRadio2VAP7OutputPackets_Type()
)
jnxWAPStatusRadio2VAP7OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPStatusRadio2VAP7OutputPackets.setStatus("current")
_JnxWlanWAPClientObjects_ObjectIdentity = ObjectIdentity
jnxWlanWAPClientObjects = _JnxWlanWAPClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2)
)
_JnxWlanWAPClientTable_Object = MibTable
jnxWlanWAPClientTable = _JnxWlanWAPClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxWlanWAPClientTable.setStatus("current")
_JnxWlanWAPClientEntry_Object = MibTableRow
jnxWlanWAPClientEntry = _JnxWlanWAPClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1)
)
jnxWlanWAPClientEntry.setIndexNames(
    (0, "JUNIPER-WLAN-WAP-MIB", "jnxWAPClientIfdIndex"),
    (0, "JUNIPER-WLAN-WAP-MIB", "jnxWAPClientIndex"),
)
if mibBuilder.loadTexts:
    jnxWlanWAPClientEntry.setStatus("current")
_JnxWAPClientIfdIndex_Type = Counter32
_JnxWAPClientIfdIndex_Object = MibTableColumn
jnxWAPClientIfdIndex = _JnxWAPClientIfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 1),
    _JnxWAPClientIfdIndex_Type()
)
jnxWAPClientIfdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWAPClientIfdIndex.setStatus("current")
_JnxWAPClientIndex_Type = Counter32
_JnxWAPClientIndex_Object = MibTableColumn
jnxWAPClientIndex = _JnxWAPClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 2),
    _JnxWAPClientIndex_Type()
)
jnxWAPClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWAPClientIndex.setStatus("current")
_JnxWAPClientRadioID_Type = Counter32
_JnxWAPClientRadioID_Object = MibTableColumn
jnxWAPClientRadioID = _JnxWAPClientRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 3),
    _JnxWAPClientRadioID_Type()
)
jnxWAPClientRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPClientRadioID.setStatus("current")
_JnxWAPClientSSID_Type = DisplayString
_JnxWAPClientSSID_Object = MibTableColumn
jnxWAPClientSSID = _JnxWAPClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 4),
    _JnxWAPClientSSID_Type()
)
jnxWAPClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPClientSSID.setStatus("current")
_JnxWAPClientMAC_Type = DisplayString
_JnxWAPClientMAC_Object = MibTableColumn
jnxWAPClientMAC = _JnxWAPClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 5),
    _JnxWAPClientMAC_Type()
)
jnxWAPClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPClientMAC.setStatus("current")
_JnxWAPClientAuth_Type = DisplayString
_JnxWAPClientAuth_Object = MibTableColumn
jnxWAPClientAuth = _JnxWAPClientAuth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 6),
    _JnxWAPClientAuth_Type()
)
jnxWAPClientAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWAPClientAuth.setStatus("current")
_JnxWAPClientPacketRx_Type = Counter64
_JnxWAPClientPacketRx_Object = MibTableColumn
jnxWAPClientPacketRx = _JnxWAPClientPacketRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 7),
    _JnxWAPClientPacketRx_Type()
)
jnxWAPClientPacketRx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWAPClientPacketRx.setStatus("current")
_JnxWAPClientPacketTx_Type = Counter64
_JnxWAPClientPacketTx_Object = MibTableColumn
jnxWAPClientPacketTx = _JnxWAPClientPacketTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 8),
    _JnxWAPClientPacketTx_Type()
)
jnxWAPClientPacketTx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWAPClientPacketTx.setStatus("current")
_JnxWAPClientBytesRx_Type = Counter64
_JnxWAPClientBytesRx_Object = MibTableColumn
jnxWAPClientBytesRx = _JnxWAPClientBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 9),
    _JnxWAPClientBytesRx_Type()
)
jnxWAPClientBytesRx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWAPClientBytesRx.setStatus("current")
_JnxWAPClientBytesTx_Type = Counter64
_JnxWAPClientBytesTx_Object = MibTableColumn
jnxWAPClientBytesTx = _JnxWAPClientBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 88, 1, 2, 1, 1, 10),
    _JnxWAPClientBytesTx_Type()
)
jnxWAPClientBytesTx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWAPClientBytesTx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WLAN-WAP-MIB",
    **{"jnxWlanWAPMIB": jnxWlanWAPMIB,
       "jnxWlanWAPStatusObjects": jnxWlanWAPStatusObjects,
       "jnxWlanWAPStatusTable": jnxWlanWAPStatusTable,
       "jnxWlanWAPStatusEntry": jnxWlanWAPStatusEntry,
       "jnxWAPStatusIfdIndex": jnxWAPStatusIfdIndex,
       "jnxWAPStatusAccessPoint": jnxWAPStatusAccessPoint,
       "jnxWAPStatusType": jnxWAPStatusType,
       "jnxWAPStatusLocation": jnxWAPStatusLocation,
       "jnxWAPStatusSerialNumber": jnxWAPStatusSerialNumber,
       "jnxWAPStatusFirmwareVersion": jnxWAPStatusFirmwareVersion,
       "jnxWAPStatusAlternateVersion": jnxWAPStatusAlternateVersion,
       "jnxWAPStatusCountry": jnxWAPStatusCountry,
       "jnxWAPStatusAccessInterface": jnxWAPStatusAccessInterface,
       "jnxWAPStatusSystemTime": jnxWAPStatusSystemTime,
       "jnxWAPStatusPacketCapture": jnxWAPStatusPacketCapture,
       "jnxWAPStatusEthernetPortMAC": jnxWAPStatusEthernetPortMAC,
       "jnxWAPStatusEthernetIPv4": jnxWAPStatusEthernetIPv4,
       "jnxWAPStatusRadio1Status": jnxWAPStatusRadio1Status,
       "jnxWAPStatusRadio1MAC": jnxWAPStatusRadio1MAC,
       "jnxWAPStatusRadio1Mode": jnxWAPStatusRadio1Mode,
       "jnxWAPStatusRadio1Channel": jnxWAPStatusRadio1Channel,
       "jnxWAPStatusRadio1Bandwidth": jnxWAPStatusRadio1Bandwidth,
       "jnxWAPStatusRadio1VAP0SSID": jnxWAPStatusRadio1VAP0SSID,
       "jnxWAPStatusRadio1VAP0MAC": jnxWAPStatusRadio1VAP0MAC,
       "jnxWAPStatusRadio1VAP0VLANID": jnxWAPStatusRadio1VAP0VLANID,
       "jnxWAPStatusRadio1VAP0InputBytes": jnxWAPStatusRadio1VAP0InputBytes,
       "jnxWAPStatusRadio1VAP0OutputBytes": jnxWAPStatusRadio1VAP0OutputBytes,
       "jnxWAPStatusRadio1VAP0InputPackets": jnxWAPStatusRadio1VAP0InputPackets,
       "jnxWAPStatusRadio1VAP0OutputPackets": jnxWAPStatusRadio1VAP0OutputPackets,
       "jnxWAPStatusRadio1VAP1SSID": jnxWAPStatusRadio1VAP1SSID,
       "jnxWAPStatusRadio1VAP1MAC": jnxWAPStatusRadio1VAP1MAC,
       "jnxWAPStatusRadio1VAP1VLANID": jnxWAPStatusRadio1VAP1VLANID,
       "jnxWAPStatusRadio1VAP1InputBytes": jnxWAPStatusRadio1VAP1InputBytes,
       "jnxWAPStatusRadio1VAP1OutputBytes": jnxWAPStatusRadio1VAP1OutputBytes,
       "jnxWAPStatusRadio1VAP1InputPackets": jnxWAPStatusRadio1VAP1InputPackets,
       "jnxWAPStatusRadio1VAP1OutputPackets": jnxWAPStatusRadio1VAP1OutputPackets,
       "jnxWAPStatusRadio1VAP2SSID": jnxWAPStatusRadio1VAP2SSID,
       "jnxWAPStatusRadio1VAP2MAC": jnxWAPStatusRadio1VAP2MAC,
       "jnxWAPStatusRadio1VAP2VLANID": jnxWAPStatusRadio1VAP2VLANID,
       "jnxWAPStatusRadio1VAP2InputBytes": jnxWAPStatusRadio1VAP2InputBytes,
       "jnxWAPStatusRadio1VAP2OutputBytes": jnxWAPStatusRadio1VAP2OutputBytes,
       "jnxWAPStatusRadio1VAP2InputPackets": jnxWAPStatusRadio1VAP2InputPackets,
       "jnxWAPStatusRadio1VAP2OutputPackets": jnxWAPStatusRadio1VAP2OutputPackets,
       "jnxWAPStatusRadio1VAP3SSID": jnxWAPStatusRadio1VAP3SSID,
       "jnxWAPStatusRadio1VAP3MAC": jnxWAPStatusRadio1VAP3MAC,
       "jnxWAPStatusRadio1VAP3VLANID": jnxWAPStatusRadio1VAP3VLANID,
       "jnxWAPStatusRadio1VAP3InputBytes": jnxWAPStatusRadio1VAP3InputBytes,
       "jnxWAPStatusRadio1VAP3OutputBytes": jnxWAPStatusRadio1VAP3OutputBytes,
       "jnxWAPStatusRadio1VAP3InputPackets": jnxWAPStatusRadio1VAP3InputPackets,
       "jnxWAPStatusRadio1VAP3OutputPackets": jnxWAPStatusRadio1VAP3OutputPackets,
       "jnxWAPStatusRadio1VAP4SSID": jnxWAPStatusRadio1VAP4SSID,
       "jnxWAPStatusRadio1VAP4MAC": jnxWAPStatusRadio1VAP4MAC,
       "jnxWAPStatusRadio1VAP4VLANID": jnxWAPStatusRadio1VAP4VLANID,
       "jnxWAPStatusRadio1VAP4InputBytes": jnxWAPStatusRadio1VAP4InputBytes,
       "jnxWAPStatusRadio1VAP4OutputBytes": jnxWAPStatusRadio1VAP4OutputBytes,
       "jnxWAPStatusRadio1VAP4InputPackets": jnxWAPStatusRadio1VAP4InputPackets,
       "jnxWAPStatusRadio1VAP4OutputPackets": jnxWAPStatusRadio1VAP4OutputPackets,
       "jnxWAPStatusRadio1VAP5SSID": jnxWAPStatusRadio1VAP5SSID,
       "jnxWAPStatusRadio1VAP5MAC": jnxWAPStatusRadio1VAP5MAC,
       "jnxWAPStatusRadio1VAP5VLANID": jnxWAPStatusRadio1VAP5VLANID,
       "jnxWAPStatusRadio1VAP5InputBytes": jnxWAPStatusRadio1VAP5InputBytes,
       "jnxWAPStatusRadio1VAP5OutputBytes": jnxWAPStatusRadio1VAP5OutputBytes,
       "jnxWAPStatusRadio1VAP5InputPackets": jnxWAPStatusRadio1VAP5InputPackets,
       "jnxWAPStatusRadio1VAP5OutputPackets": jnxWAPStatusRadio1VAP5OutputPackets,
       "jnxWAPStatusRadio1VAP6SSID": jnxWAPStatusRadio1VAP6SSID,
       "jnxWAPStatusRadio1VAP6MAC": jnxWAPStatusRadio1VAP6MAC,
       "jnxWAPStatusRadio1VAP6VLANID": jnxWAPStatusRadio1VAP6VLANID,
       "jnxWAPStatusRadio1VAP6InputBytes": jnxWAPStatusRadio1VAP6InputBytes,
       "jnxWAPStatusRadio1VAP6OutputBytes": jnxWAPStatusRadio1VAP6OutputBytes,
       "jnxWAPStatusRadio1VAP6InputPackets": jnxWAPStatusRadio1VAP6InputPackets,
       "jnxWAPStatusRadio1VAP6OutputPackets": jnxWAPStatusRadio1VAP6OutputPackets,
       "jnxWAPStatusRadio1VAP7SSID": jnxWAPStatusRadio1VAP7SSID,
       "jnxWAPStatusRadio1VAP7MAC": jnxWAPStatusRadio1VAP7MAC,
       "jnxWAPStatusRadio1VAP7VLANID": jnxWAPStatusRadio1VAP7VLANID,
       "jnxWAPStatusRadio1VAP7InputBytes": jnxWAPStatusRadio1VAP7InputBytes,
       "jnxWAPStatusRadio1VAP7OutputBytes": jnxWAPStatusRadio1VAP7OutputBytes,
       "jnxWAPStatusRadio1VAP7InputPackets": jnxWAPStatusRadio1VAP7InputPackets,
       "jnxWAPStatusRadio1VAP7OutputPackets": jnxWAPStatusRadio1VAP7OutputPackets,
       "jnxWAPStatusRadio2Status": jnxWAPStatusRadio2Status,
       "jnxWAPStatusRadio2MAC": jnxWAPStatusRadio2MAC,
       "jnxWAPStatusRadio2Mode": jnxWAPStatusRadio2Mode,
       "jnxWAPStatusRadio2Channel": jnxWAPStatusRadio2Channel,
       "jnxWAPStatusRadio2Bandwidth": jnxWAPStatusRadio2Bandwidth,
       "jnxWAPStatusRadio2VAP0SSID": jnxWAPStatusRadio2VAP0SSID,
       "jnxWAPStatusRadio2VAP0MAC": jnxWAPStatusRadio2VAP0MAC,
       "jnxWAPStatusRadio2VAP0VLANID": jnxWAPStatusRadio2VAP0VLANID,
       "jnxWAPStatusRadio2VAP0InputBytes": jnxWAPStatusRadio2VAP0InputBytes,
       "jnxWAPStatusRadio2VAP0OutputBytes": jnxWAPStatusRadio2VAP0OutputBytes,
       "jnxWAPStatusRadio2VAP0InputPackets": jnxWAPStatusRadio2VAP0InputPackets,
       "jnxWAPStatusRadio2VAP0OutputPackets": jnxWAPStatusRadio2VAP0OutputPackets,
       "jnxWAPStatusRadio2VAP1SSID": jnxWAPStatusRadio2VAP1SSID,
       "jnxWAPStatusRadio2VAP1MAC": jnxWAPStatusRadio2VAP1MAC,
       "jnxWAPStatusRadio2VAP1VLANID": jnxWAPStatusRadio2VAP1VLANID,
       "jnxWAPStatusRadio2VAP1InputBytes": jnxWAPStatusRadio2VAP1InputBytes,
       "jnxWAPStatusRadio2VAP1OutputBytes": jnxWAPStatusRadio2VAP1OutputBytes,
       "jnxWAPStatusRadio2VAP1InputPackets": jnxWAPStatusRadio2VAP1InputPackets,
       "jnxWAPStatusRadio2VAP1OutputPackets": jnxWAPStatusRadio2VAP1OutputPackets,
       "jnxWAPStatusRadio2VAP2SSID": jnxWAPStatusRadio2VAP2SSID,
       "jnxWAPStatusRadio2VAP2MAC": jnxWAPStatusRadio2VAP2MAC,
       "jnxWAPStatusRadio2VAP2VLANID": jnxWAPStatusRadio2VAP2VLANID,
       "jnxWAPStatusRadio2VAP2InputBytes": jnxWAPStatusRadio2VAP2InputBytes,
       "jnxWAPStatusRadio2VAP2OutputBytes": jnxWAPStatusRadio2VAP2OutputBytes,
       "jnxWAPStatusRadio2VAP2InputPackets": jnxWAPStatusRadio2VAP2InputPackets,
       "jnxWAPStatusRadio2VAP2OutputPackets": jnxWAPStatusRadio2VAP2OutputPackets,
       "jnxWAPStatusRadio2VAP3SSID": jnxWAPStatusRadio2VAP3SSID,
       "jnxWAPStatusRadio2VAP3MAC": jnxWAPStatusRadio2VAP3MAC,
       "jnxWAPStatusRadio2VAP3VLANID": jnxWAPStatusRadio2VAP3VLANID,
       "jnxWAPStatusRadio2VAP3InputBytes": jnxWAPStatusRadio2VAP3InputBytes,
       "jnxWAPStatusRadio2VAP3OutputBytes": jnxWAPStatusRadio2VAP3OutputBytes,
       "jnxWAPStatusRadio2VAP3InputPackets": jnxWAPStatusRadio2VAP3InputPackets,
       "jnxWAPStatusRadio2VAP3OutputPackets": jnxWAPStatusRadio2VAP3OutputPackets,
       "jnxWAPStatusRadio2VAP4SSID": jnxWAPStatusRadio2VAP4SSID,
       "jnxWAPStatusRadio2VAP4MAC": jnxWAPStatusRadio2VAP4MAC,
       "jnxWAPStatusRadio2VAP4VLANID": jnxWAPStatusRadio2VAP4VLANID,
       "jnxWAPStatusRadio2VAP4InputBytes": jnxWAPStatusRadio2VAP4InputBytes,
       "jnxWAPStatusRadio2VAP4OutputBytes": jnxWAPStatusRadio2VAP4OutputBytes,
       "jnxWAPStatusRadio2VAP4InputPackets": jnxWAPStatusRadio2VAP4InputPackets,
       "jnxWAPStatusRadio2VAP4OutputPackets": jnxWAPStatusRadio2VAP4OutputPackets,
       "jnxWAPStatusRadio2VAP5SSID": jnxWAPStatusRadio2VAP5SSID,
       "jnxWAPStatusRadio2VAP5MAC": jnxWAPStatusRadio2VAP5MAC,
       "jnxWAPStatusRadio2VAP5VLANID": jnxWAPStatusRadio2VAP5VLANID,
       "jnxWAPStatusRadio2VAP5InputBytes": jnxWAPStatusRadio2VAP5InputBytes,
       "jnxWAPStatusRadio2VAP5OutputBytes": jnxWAPStatusRadio2VAP5OutputBytes,
       "jnxWAPStatusRadio2VAP5InputPackets": jnxWAPStatusRadio2VAP5InputPackets,
       "jnxWAPStatusRadio2VAP5OutputPackets": jnxWAPStatusRadio2VAP5OutputPackets,
       "jnxWAPStatusRadio2VAP6SSID": jnxWAPStatusRadio2VAP6SSID,
       "jnxWAPStatusRadio2VAP6MAC": jnxWAPStatusRadio2VAP6MAC,
       "jnxWAPStatusRadio2VAP6VLANID": jnxWAPStatusRadio2VAP6VLANID,
       "jnxWAPStatusRadio2VAP6InputBytes": jnxWAPStatusRadio2VAP6InputBytes,
       "jnxWAPStatusRadio2VAP6OutputBytes": jnxWAPStatusRadio2VAP6OutputBytes,
       "jnxWAPStatusRadio2VAP6InputPackets": jnxWAPStatusRadio2VAP6InputPackets,
       "jnxWAPStatusRadio2VAP6OutputPackets": jnxWAPStatusRadio2VAP6OutputPackets,
       "jnxWAPStatusRadio2VAP7SSID": jnxWAPStatusRadio2VAP7SSID,
       "jnxWAPStatusRadio2VAP7MAC": jnxWAPStatusRadio2VAP7MAC,
       "jnxWAPStatusRadio2VAP7VLANID": jnxWAPStatusRadio2VAP7VLANID,
       "jnxWAPStatusRadio2VAP7InputBytes": jnxWAPStatusRadio2VAP7InputBytes,
       "jnxWAPStatusRadio2VAP7OutputBytes": jnxWAPStatusRadio2VAP7OutputBytes,
       "jnxWAPStatusRadio2VAP7InputPackets": jnxWAPStatusRadio2VAP7InputPackets,
       "jnxWAPStatusRadio2VAP7OutputPackets": jnxWAPStatusRadio2VAP7OutputPackets,
       "jnxWlanWAPClientObjects": jnxWlanWAPClientObjects,
       "jnxWlanWAPClientTable": jnxWlanWAPClientTable,
       "jnxWlanWAPClientEntry": jnxWlanWAPClientEntry,
       "jnxWAPClientIfdIndex": jnxWAPClientIfdIndex,
       "jnxWAPClientIndex": jnxWAPClientIndex,
       "jnxWAPClientRadioID": jnxWAPClientRadioID,
       "jnxWAPClientSSID": jnxWAPClientSSID,
       "jnxWAPClientMAC": jnxWAPClientMAC,
       "jnxWAPClientAuth": jnxWAPClientAuth,
       "jnxWAPClientPacketRx": jnxWAPClientPacketRx,
       "jnxWAPClientPacketTx": jnxWAPClientPacketTx,
       "jnxWAPClientBytesRx": jnxWAPClientBytesRx,
       "jnxWAPClientBytesTx": jnxWAPClientBytesTx}
)
