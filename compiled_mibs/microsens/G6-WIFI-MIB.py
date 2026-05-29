# SNMP MIB module (G6-WIFI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsens\G6-WIFI-MIB

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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2023-02-14 11:27",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wifi_ObjectIdentity = ObjectIdentity
wifi = _Wifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98)
)


class _WifiEnableWifi_Type(Integer32):
    """Custom type wifiEnableWifi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WifiEnableWifi_Type.__name__ = "Integer32"
_WifiEnableWifi_Object = MibScalar
wifiEnableWifi = _WifiEnableWifi_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 1),
    _WifiEnableWifi_Type()
)
wifiEnableWifi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wifiEnableWifi.setStatus("current")
_AccessPointTable_Object = MibTable
accessPointTable = _AccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 2)
)
if mibBuilder.loadTexts:
    accessPointTable.setStatus("current")
_AccessPointEntry_Object = MibTableRow
accessPointEntry = _AccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 2, 1)
)
accessPointEntry.setIndexNames(
    (0, "G6-WIFI-MIB", "accessPointIndex"),
)
if mibBuilder.loadTexts:
    accessPointEntry.setStatus("current")


class _AccessPointIndex_Type(Integer32):
    """Custom type accessPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AccessPointIndex_Type.__name__ = "Integer32"
_AccessPointIndex_Object = MibTableColumn
accessPointIndex = _AccessPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 2, 1, 1),
    _AccessPointIndex_Type()
)
accessPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessPointIndex.setStatus("current")
_AccessPointHostname_Type = DisplayString
_AccessPointHostname_Object = MibTableColumn
accessPointHostname = _AccessPointHostname_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 2, 1, 2),
    _AccessPointHostname_Type()
)
accessPointHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPointHostname.setStatus("current")


class _AccessPointDeviceIp_Type(OctetString):
    """Custom type accessPointDeviceIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AccessPointDeviceIp_Type.__name__ = "OctetString"
_AccessPointDeviceIp_Object = MibTableColumn
accessPointDeviceIp = _AccessPointDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 2, 1, 3),
    _AccessPointDeviceIp_Type()
)
accessPointDeviceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPointDeviceIp.setStatus("current")


class _AccessPointSubnetMask_Type(OctetString):
    """Custom type accessPointSubnetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AccessPointSubnetMask_Type.__name__ = "OctetString"
_AccessPointSubnetMask_Object = MibTableColumn
accessPointSubnetMask = _AccessPointSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 2, 1, 4),
    _AccessPointSubnetMask_Type()
)
accessPointSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPointSubnetMask.setStatus("current")


class _AccessPointGateway_Type(OctetString):
    """Custom type accessPointGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AccessPointGateway_Type.__name__ = "OctetString"
_AccessPointGateway_Object = MibTableColumn
accessPointGateway = _AccessPointGateway_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 2, 1, 5),
    _AccessPointGateway_Type()
)
accessPointGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPointGateway.setStatus("current")
_AccessPointUpdateFirmware_Type = DisplayString
_AccessPointUpdateFirmware_Object = MibTableColumn
accessPointUpdateFirmware = _AccessPointUpdateFirmware_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 2, 1, 6),
    _AccessPointUpdateFirmware_Type()
)
accessPointUpdateFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPointUpdateFirmware.setStatus("current")
_AccessPointReboot_Type = DisplayString
_AccessPointReboot_Object = MibTableColumn
accessPointReboot = _AccessPointReboot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 2, 1, 7),
    _AccessPointReboot_Type()
)
accessPointReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPointReboot.setStatus("current")
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("current")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1)
)
interfaceEntry.setIndexNames(
    (0, "G6-WIFI-MIB", "interfaceIndex"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("current")


class _InterfaceIndex_Type(Integer32):
    """Custom type interfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_InterfaceIndex_Type.__name__ = "Integer32"
_InterfaceIndex_Object = MibTableColumn
interfaceIndex = _InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 1),
    _InterfaceIndex_Type()
)
interfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceIndex.setStatus("current")
_InterfaceCountryCode_Type = DisplayString
_InterfaceCountryCode_Object = MibTableColumn
interfaceCountryCode = _InterfaceCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 2),
    _InterfaceCountryCode_Type()
)
interfaceCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceCountryCode.setStatus("current")
_InterfaceSsid_Type = DisplayString
_InterfaceSsid_Object = MibTableColumn
interfaceSsid = _InterfaceSsid_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 3),
    _InterfaceSsid_Type()
)
interfaceSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceSsid.setStatus("current")
_InterfaceEnterPresharedKey_Type = DisplayString
_InterfaceEnterPresharedKey_Object = MibTableColumn
interfaceEnterPresharedKey = _InterfaceEnterPresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 4),
    _InterfaceEnterPresharedKey_Type()
)
interfaceEnterPresharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceEnterPresharedKey.setStatus("current")
_InterfaceEncryptedPresharedKey_Type = DisplayString
_InterfaceEncryptedPresharedKey_Object = MibTableColumn
interfaceEncryptedPresharedKey = _InterfaceEncryptedPresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 5),
    _InterfaceEncryptedPresharedKey_Type()
)
interfaceEncryptedPresharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceEncryptedPresharedKey.setStatus("current")


class _InterfaceExposeSsid_Type(Integer32):
    """Custom type interfaceExposeSsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 0),
          ("visible", 1))
    )


_InterfaceExposeSsid_Type.__name__ = "Integer32"
_InterfaceExposeSsid_Object = MibTableColumn
interfaceExposeSsid = _InterfaceExposeSsid_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 6),
    _InterfaceExposeSsid_Type()
)
interfaceExposeSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceExposeSsid.setStatus("current")


class _InterfaceEncryption_Type(Integer32):
    """Custom type interfaceEncryption based on Integer32"""
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
          ("wep", 1),
          ("wpaPsk", 2),
          ("wpaPsk2", 3))
    )


_InterfaceEncryption_Type.__name__ = "Integer32"
_InterfaceEncryption_Object = MibTableColumn
interfaceEncryption = _InterfaceEncryption_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 7),
    _InterfaceEncryption_Type()
)
interfaceEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceEncryption.setStatus("current")


class _InterfaceDhcpServer_Type(Integer32):
    """Custom type interfaceDhcpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_InterfaceDhcpServer_Type.__name__ = "Integer32"
_InterfaceDhcpServer_Object = MibTableColumn
interfaceDhcpServer = _InterfaceDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 8),
    _InterfaceDhcpServer_Type()
)
interfaceDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceDhcpServer.setStatus("current")


class _InterfaceDhcpStartAddress_Type(OctetString):
    """Custom type interfaceDhcpStartAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InterfaceDhcpStartAddress_Type.__name__ = "OctetString"
_InterfaceDhcpStartAddress_Object = MibTableColumn
interfaceDhcpStartAddress = _InterfaceDhcpStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 9),
    _InterfaceDhcpStartAddress_Type()
)
interfaceDhcpStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceDhcpStartAddress.setStatus("current")


class _InterfaceDhcpNumberOfAddresses_Type(Integer32):
    """Custom type interfaceDhcpNumberOfAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InterfaceDhcpNumberOfAddresses_Type.__name__ = "Integer32"
_InterfaceDhcpNumberOfAddresses_Object = MibTableColumn
interfaceDhcpNumberOfAddresses = _InterfaceDhcpNumberOfAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 10),
    _InterfaceDhcpNumberOfAddresses_Type()
)
interfaceDhcpNumberOfAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceDhcpNumberOfAddresses.setStatus("current")
_InterfaceChannelNumber_Type = Unsigned32
_InterfaceChannelNumber_Object = MibTableColumn
interfaceChannelNumber = _InterfaceChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 11),
    _InterfaceChannelNumber_Type()
)
interfaceChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceChannelNumber.setStatus("current")


class _InterfaceChannelWidth_Type(Integer32):
    """Custom type interfaceChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ht20", 1),
          ("ht40p", 2),
          ("ht40n", 3))
    )


_InterfaceChannelWidth_Type.__name__ = "Integer32"
_InterfaceChannelWidth_Object = MibTableColumn
interfaceChannelWidth = _InterfaceChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 3, 1, 12),
    _InterfaceChannelWidth_Type()
)
interfaceChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceChannelWidth.setStatus("current")
_FirewallConfigTable_Object = MibTable
firewallConfigTable = _FirewallConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 4)
)
if mibBuilder.loadTexts:
    firewallConfigTable.setStatus("current")
_FirewallConfigEntry_Object = MibTableRow
firewallConfigEntry = _FirewallConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 4, 1)
)
firewallConfigEntry.setIndexNames(
    (0, "G6-WIFI-MIB", "firewallConfigIndex"),
)
if mibBuilder.loadTexts:
    firewallConfigEntry.setStatus("current")


class _FirewallConfigIndex_Type(Integer32):
    """Custom type firewallConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_FirewallConfigIndex_Type.__name__ = "Integer32"
_FirewallConfigIndex_Object = MibTableColumn
firewallConfigIndex = _FirewallConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 4, 1, 1),
    _FirewallConfigIndex_Type()
)
firewallConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    firewallConfigIndex.setStatus("current")


class _FirewallConfigEnableIngressFirewall_Type(Integer32):
    """Custom type firewallConfigEnableIngressFirewall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FirewallConfigEnableIngressFirewall_Type.__name__ = "Integer32"
_FirewallConfigEnableIngressFirewall_Object = MibTableColumn
firewallConfigEnableIngressFirewall = _FirewallConfigEnableIngressFirewall_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 4, 1, 2),
    _FirewallConfigEnableIngressFirewall_Type()
)
firewallConfigEnableIngressFirewall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConfigEnableIngressFirewall.setStatus("current")


class _FirewallConfigEnableEgressFirewall_Type(Integer32):
    """Custom type firewallConfigEnableEgressFirewall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FirewallConfigEnableEgressFirewall_Type.__name__ = "Integer32"
_FirewallConfigEnableEgressFirewall_Object = MibTableColumn
firewallConfigEnableEgressFirewall = _FirewallConfigEnableEgressFirewall_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 4, 1, 3),
    _FirewallConfigEnableEgressFirewall_Type()
)
firewallConfigEnableEgressFirewall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConfigEnableEgressFirewall.setStatus("current")


class _FirewallConfigDropInvalidPackets_Type(Integer32):
    """Custom type firewallConfigDropInvalidPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FirewallConfigDropInvalidPackets_Type.__name__ = "Integer32"
_FirewallConfigDropInvalidPackets_Object = MibTableColumn
firewallConfigDropInvalidPackets = _FirewallConfigDropInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 4, 1, 4),
    _FirewallConfigDropInvalidPackets_Type()
)
firewallConfigDropInvalidPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConfigDropInvalidPackets.setStatus("current")


class _FirewallConfigSynRateLimiting_Type(Integer32):
    """Custom type firewallConfigSynRateLimiting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FirewallConfigSynRateLimiting_Type.__name__ = "Integer32"
_FirewallConfigSynRateLimiting_Object = MibTableColumn
firewallConfigSynRateLimiting = _FirewallConfigSynRateLimiting_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 4, 1, 5),
    _FirewallConfigSynRateLimiting_Type()
)
firewallConfigSynRateLimiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConfigSynRateLimiting.setStatus("current")


class _FirewallConfigUseSynCookies_Type(Integer32):
    """Custom type firewallConfigUseSynCookies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FirewallConfigUseSynCookies_Type.__name__ = "Integer32"
_FirewallConfigUseSynCookies_Object = MibTableColumn
firewallConfigUseSynCookies = _FirewallConfigUseSynCookies_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 4, 1, 6),
    _FirewallConfigUseSynCookies_Type()
)
firewallConfigUseSynCookies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConfigUseSynCookies.setStatus("current")


class _FirewallConfigTcpWindowScaling_Type(Integer32):
    """Custom type firewallConfigTcpWindowScaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FirewallConfigTcpWindowScaling_Type.__name__ = "Integer32"
_FirewallConfigTcpWindowScaling_Object = MibTableColumn
firewallConfigTcpWindowScaling = _FirewallConfigTcpWindowScaling_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 4, 1, 7),
    _FirewallConfigTcpWindowScaling_Type()
)
firewallConfigTcpWindowScaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConfigTcpWindowScaling.setStatus("current")
_FirewallRulesTable_Object = MibTable
firewallRulesTable = _FirewallRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 5)
)
if mibBuilder.loadTexts:
    firewallRulesTable.setStatus("current")
_FirewallRulesEntry_Object = MibTableRow
firewallRulesEntry = _FirewallRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 5, 1)
)
firewallRulesEntry.setIndexNames(
    (0, "G6-WIFI-MIB", "firewallRulesIndex"),
)
if mibBuilder.loadTexts:
    firewallRulesEntry.setStatus("current")


class _FirewallRulesIndex_Type(Integer32):
    """Custom type firewallRulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_FirewallRulesIndex_Type.__name__ = "Integer32"
_FirewallRulesIndex_Object = MibTableColumn
firewallRulesIndex = _FirewallRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 5, 1, 1),
    _FirewallRulesIndex_Type()
)
firewallRulesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    firewallRulesIndex.setStatus("current")
_FirewallRulesIncomingAclList_Type = DisplayString
_FirewallRulesIncomingAclList_Object = MibTableColumn
firewallRulesIncomingAclList = _FirewallRulesIncomingAclList_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 5, 1, 2),
    _FirewallRulesIncomingAclList_Type()
)
firewallRulesIncomingAclList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallRulesIncomingAclList.setStatus("current")


class _FirewallRulesIncomingAclDefault_Type(Integer32):
    """Custom type firewallRulesIncomingAclDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_FirewallRulesIncomingAclDefault_Type.__name__ = "Integer32"
_FirewallRulesIncomingAclDefault_Object = MibTableColumn
firewallRulesIncomingAclDefault = _FirewallRulesIncomingAclDefault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 5, 1, 3),
    _FirewallRulesIncomingAclDefault_Type()
)
firewallRulesIncomingAclDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallRulesIncomingAclDefault.setStatus("current")
_FirewallRulesOutgoingAclList_Type = DisplayString
_FirewallRulesOutgoingAclList_Object = MibTableColumn
firewallRulesOutgoingAclList = _FirewallRulesOutgoingAclList_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 5, 1, 4),
    _FirewallRulesOutgoingAclList_Type()
)
firewallRulesOutgoingAclList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallRulesOutgoingAclList.setStatus("current")


class _FirewallRulesOutgoingAclDefault_Type(Integer32):
    """Custom type firewallRulesOutgoingAclDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_FirewallRulesOutgoingAclDefault_Type.__name__ = "Integer32"
_FirewallRulesOutgoingAclDefault_Object = MibTableColumn
firewallRulesOutgoingAclDefault = _FirewallRulesOutgoingAclDefault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 5, 1, 5),
    _FirewallRulesOutgoingAclDefault_Type()
)
firewallRulesOutgoingAclDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallRulesOutgoingAclDefault.setStatus("current")
_StatusTable_Object = MibTable
statusTable = _StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 100)
)
if mibBuilder.loadTexts:
    statusTable.setStatus("current")
_StatusEntry_Object = MibTableRow
statusEntry = _StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 100, 1)
)
statusEntry.setIndexNames(
    (0, "G6-WIFI-MIB", "statusIndex"),
)
if mibBuilder.loadTexts:
    statusEntry.setStatus("current")


class _StatusIndex_Type(Integer32):
    """Custom type statusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_StatusIndex_Type.__name__ = "Integer32"
_StatusIndex_Object = MibTableColumn
statusIndex = _StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 100, 1, 1),
    _StatusIndex_Type()
)
statusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statusIndex.setStatus("current")


class _StatusOverallStatus_Type(Integer32):
    """Custom type statusOverallStatus based on Integer32"""
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
        *(("notPresent", 0),
          ("disabled", 1),
          ("fault", 2),
          ("operational", 3))
    )


_StatusOverallStatus_Type.__name__ = "Integer32"
_StatusOverallStatus_Object = MibTableColumn
statusOverallStatus = _StatusOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 100, 1, 2),
    _StatusOverallStatus_Type()
)
statusOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusOverallStatus.setStatus("current")
_StatusNumberOfConnections_Type = Unsigned32
_StatusNumberOfConnections_Object = MibTableColumn
statusNumberOfConnections = _StatusNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 100, 1, 3),
    _StatusNumberOfConnections_Type()
)
statusNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusNumberOfConnections.setStatus("current")
_IpV4StatusTable_Object = MibTable
ipV4StatusTable = _IpV4StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 101)
)
if mibBuilder.loadTexts:
    ipV4StatusTable.setStatus("current")
_IpV4StatusEntry_Object = MibTableRow
ipV4StatusEntry = _IpV4StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 101, 1)
)
ipV4StatusEntry.setIndexNames(
    (0, "G6-WIFI-MIB", "ipV4StatusIndex"),
)
if mibBuilder.loadTexts:
    ipV4StatusEntry.setStatus("current")


class _IpV4StatusIndex_Type(Integer32):
    """Custom type ipV4StatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_IpV4StatusIndex_Type.__name__ = "Integer32"
_IpV4StatusIndex_Object = MibTableColumn
ipV4StatusIndex = _IpV4StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 101, 1, 1),
    _IpV4StatusIndex_Type()
)
ipV4StatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipV4StatusIndex.setStatus("current")


class _IpV4StatusDynamicDeviceIp_Type(OctetString):
    """Custom type ipV4StatusDynamicDeviceIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpV4StatusDynamicDeviceIp_Type.__name__ = "OctetString"
_IpV4StatusDynamicDeviceIp_Object = MibTableColumn
ipV4StatusDynamicDeviceIp = _IpV4StatusDynamicDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 101, 1, 2),
    _IpV4StatusDynamicDeviceIp_Type()
)
ipV4StatusDynamicDeviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipV4StatusDynamicDeviceIp.setStatus("current")


class _IpV4StatusDynamicSubnetMask_Type(OctetString):
    """Custom type ipV4StatusDynamicSubnetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpV4StatusDynamicSubnetMask_Type.__name__ = "OctetString"
_IpV4StatusDynamicSubnetMask_Object = MibTableColumn
ipV4StatusDynamicSubnetMask = _IpV4StatusDynamicSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 101, 1, 3),
    _IpV4StatusDynamicSubnetMask_Type()
)
ipV4StatusDynamicSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipV4StatusDynamicSubnetMask.setStatus("current")


class _IpV4StatusDynamicGateway_Type(OctetString):
    """Custom type ipV4StatusDynamicGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpV4StatusDynamicGateway_Type.__name__ = "OctetString"
_IpV4StatusDynamicGateway_Object = MibTableColumn
ipV4StatusDynamicGateway = _IpV4StatusDynamicGateway_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 98, 101, 1, 4),
    _IpV4StatusDynamicGateway_Type()
)
ipV4StatusDynamicGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipV4StatusDynamicGateway.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-WIFI-MIB",
    **{"device": device,
       "wifi": wifi,
       "wifiEnableWifi": wifiEnableWifi,
       "accessPointTable": accessPointTable,
       "accessPointEntry": accessPointEntry,
       "accessPointIndex": accessPointIndex,
       "accessPointHostname": accessPointHostname,
       "accessPointDeviceIp": accessPointDeviceIp,
       "accessPointSubnetMask": accessPointSubnetMask,
       "accessPointGateway": accessPointGateway,
       "accessPointUpdateFirmware": accessPointUpdateFirmware,
       "accessPointReboot": accessPointReboot,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfaceIndex": interfaceIndex,
       "interfaceCountryCode": interfaceCountryCode,
       "interfaceSsid": interfaceSsid,
       "interfaceEnterPresharedKey": interfaceEnterPresharedKey,
       "interfaceEncryptedPresharedKey": interfaceEncryptedPresharedKey,
       "interfaceExposeSsid": interfaceExposeSsid,
       "interfaceEncryption": interfaceEncryption,
       "interfaceDhcpServer": interfaceDhcpServer,
       "interfaceDhcpStartAddress": interfaceDhcpStartAddress,
       "interfaceDhcpNumberOfAddresses": interfaceDhcpNumberOfAddresses,
       "interfaceChannelNumber": interfaceChannelNumber,
       "interfaceChannelWidth": interfaceChannelWidth,
       "firewallConfigTable": firewallConfigTable,
       "firewallConfigEntry": firewallConfigEntry,
       "firewallConfigIndex": firewallConfigIndex,
       "firewallConfigEnableIngressFirewall": firewallConfigEnableIngressFirewall,
       "firewallConfigEnableEgressFirewall": firewallConfigEnableEgressFirewall,
       "firewallConfigDropInvalidPackets": firewallConfigDropInvalidPackets,
       "firewallConfigSynRateLimiting": firewallConfigSynRateLimiting,
       "firewallConfigUseSynCookies": firewallConfigUseSynCookies,
       "firewallConfigTcpWindowScaling": firewallConfigTcpWindowScaling,
       "firewallRulesTable": firewallRulesTable,
       "firewallRulesEntry": firewallRulesEntry,
       "firewallRulesIndex": firewallRulesIndex,
       "firewallRulesIncomingAclList": firewallRulesIncomingAclList,
       "firewallRulesIncomingAclDefault": firewallRulesIncomingAclDefault,
       "firewallRulesOutgoingAclList": firewallRulesOutgoingAclList,
       "firewallRulesOutgoingAclDefault": firewallRulesOutgoingAclDefault,
       "statusTable": statusTable,
       "statusEntry": statusEntry,
       "statusIndex": statusIndex,
       "statusOverallStatus": statusOverallStatus,
       "statusNumberOfConnections": statusNumberOfConnections,
       "ipV4StatusTable": ipV4StatusTable,
       "ipV4StatusEntry": ipV4StatusEntry,
       "ipV4StatusIndex": ipV4StatusIndex,
       "ipV4StatusDynamicDeviceIp": ipV4StatusDynamicDeviceIp,
       "ipV4StatusDynamicSubnetMask": ipV4StatusDynamicSubnetMask,
       "ipV4StatusDynamicGateway": ipV4StatusDynamicGateway}
)
