# SNMP MIB module (SPEEDCARRIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pandacom\SPEEDCARRIER-MIB

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

(descr,
 panDacom,
 port,
 slot,
 traps) = mibBuilder.importSymbols(
    "PanDacom-MIB",
    "descr",
    "panDacom",
    "port",
    "slot",
    "traps")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nmSPEEDCARRIER = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3)
)
if mibBuilder.loadTexts:
    nmSPEEDCARRIER.setRevisions(
        ("2020-01-14 00:00",
         "2019-11-21 00:00",
         "2019-04-24 00:00",
         "2019-01-15 00:00",
         "2018-04-24 00:00",
         "2017-11-30 00:00",
         "2017-08-16 00:00",
         "2013-12-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmAgent_ObjectIdentity = ObjectIdentity
nmAgent = _NmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1)
)
_NmAgentGeneralInfo_ObjectIdentity = ObjectIdentity
nmAgentGeneralInfo = _NmAgentGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1)
)


class _NmARamdiskVersion_Type(DisplayString):
    """Custom type nmARamdiskVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmARamdiskVersion_Type.__name__ = "DisplayString"
_NmARamdiskVersion_Object = MibScalar
nmARamdiskVersion = _NmARamdiskVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 1),
    _NmARamdiskVersion_Type()
)
nmARamdiskVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmARamdiskVersion.setStatus("current")


class _NmASlot_Type(Integer32):
    """Custom type nmASlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NmASlot_Type.__name__ = "Integer32"
_NmASlot_Object = MibScalar
nmASlot = _NmASlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 2),
    _NmASlot_Type()
)
nmASlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmASlot.setStatus("current")


class _NmADate_Type(DisplayString):
    """Custom type nmADate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NmADate_Type.__name__ = "DisplayString"
_NmADate_Object = MibScalar
nmADate = _NmADate_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 3),
    _NmADate_Type()
)
nmADate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmADate.setStatus("current")


class _NmATime_Type(DisplayString):
    """Custom type nmATime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NmATime_Type.__name__ = "DisplayString"
_NmATime_Object = MibScalar
nmATime = _NmATime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 4),
    _NmATime_Type()
)
nmATime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmATime.setStatus("current")


class _NmAUpTime_Type(DisplayString):
    """Custom type nmAUpTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NmAUpTime_Type.__name__ = "DisplayString"
_NmAUpTime_Object = MibScalar
nmAUpTime = _NmAUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 5),
    _NmAUpTime_Type()
)
nmAUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAUpTime.setStatus("current")
_NmATemperature_Type = Integer32
_NmATemperature_Object = MibScalar
nmATemperature = _NmATemperature_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 6),
    _NmATemperature_Type()
)
nmATemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmATemperature.setStatus("current")


class _NmAAlarmState_Type(Integer32):
    """Custom type nmAAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAlarms", 0),
          ("activeAlarms", 1))
    )


_NmAAlarmState_Type.__name__ = "Integer32"
_NmAAlarmState_Object = MibScalar
nmAAlarmState = _NmAAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 7),
    _NmAAlarmState_Type()
)
nmAAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAAlarmState.setStatus("current")


class _NmASerialNumber_Type(DisplayString):
    """Custom type nmASerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NmASerialNumber_Type.__name__ = "DisplayString"
_NmASerialNumber_Object = MibScalar
nmASerialNumber = _NmASerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 8),
    _NmASerialNumber_Type()
)
nmASerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmASerialNumber.setStatus("current")


class _NmAKernelVersion_Type(DisplayString):
    """Custom type nmAKernelVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAKernelVersion_Type.__name__ = "DisplayString"
_NmAKernelVersion_Object = MibScalar
nmAKernelVersion = _NmAKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 9),
    _NmAKernelVersion_Type()
)
nmAKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAKernelVersion.setStatus("current")


class _NmASoftwareVersion_Type(DisplayString):
    """Custom type nmASoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmASoftwareVersion_Type.__name__ = "DisplayString"
_NmASoftwareVersion_Object = MibScalar
nmASoftwareVersion = _NmASoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 1, 10),
    _NmASoftwareVersion_Type()
)
nmASoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmASoftwareVersion.setStatus("current")
_NmAgentConfig_ObjectIdentity = ObjectIdentity
nmAgentConfig = _NmAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2)
)
_NmAgentConfigNetwork_ObjectIdentity = ObjectIdentity
nmAgentConfigNetwork = _NmAgentConfigNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 1)
)
_NmAgentConfigNetworkIP_Type = IpAddress
_NmAgentConfigNetworkIP_Object = MibScalar
nmAgentConfigNetworkIP = _NmAgentConfigNetworkIP_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 1, 1),
    _NmAgentConfigNetworkIP_Type()
)
nmAgentConfigNetworkIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigNetworkIP.setStatus("current")
_NmAgentConfigNetworkMask_Type = IpAddress
_NmAgentConfigNetworkMask_Object = MibScalar
nmAgentConfigNetworkMask = _NmAgentConfigNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 1, 2),
    _NmAgentConfigNetworkMask_Type()
)
nmAgentConfigNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigNetworkMask.setStatus("current")
_NmAgentConfigNetworkGateway_Type = IpAddress
_NmAgentConfigNetworkGateway_Object = MibScalar
nmAgentConfigNetworkGateway = _NmAgentConfigNetworkGateway_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 1, 3),
    _NmAgentConfigNetworkGateway_Type()
)
nmAgentConfigNetworkGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigNetworkGateway.setStatus("current")


class _NmAgentConfigNetworkIPv6_Type(DisplayString):
    """Custom type nmAgentConfigNetworkIPv6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigNetworkIPv6_Type.__name__ = "DisplayString"
_NmAgentConfigNetworkIPv6_Object = MibScalar
nmAgentConfigNetworkIPv6 = _NmAgentConfigNetworkIPv6_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 1, 5),
    _NmAgentConfigNetworkIPv6_Type()
)
nmAgentConfigNetworkIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigNetworkIPv6.setStatus("current")


class _NmAgentConfigNetworkGatewayv6_Type(DisplayString):
    """Custom type nmAgentConfigNetworkGatewayv6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigNetworkGatewayv6_Type.__name__ = "DisplayString"
_NmAgentConfigNetworkGatewayv6_Object = MibScalar
nmAgentConfigNetworkGatewayv6 = _NmAgentConfigNetworkGatewayv6_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 1, 6),
    _NmAgentConfigNetworkGatewayv6_Type()
)
nmAgentConfigNetworkGatewayv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigNetworkGatewayv6.setStatus("current")
_NmAgentConfigSnmp_ObjectIdentity = ObjectIdentity
nmAgentConfigSnmp = _NmAgentConfigSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2)
)


class _NmAgentConfigSnmpReadCommunity_Type(DisplayString):
    """Custom type nmAgentConfigSnmpReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NmAgentConfigSnmpReadCommunity_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpReadCommunity_Object = MibScalar
nmAgentConfigSnmpReadCommunity = _NmAgentConfigSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 1),
    _NmAgentConfigSnmpReadCommunity_Type()
)
nmAgentConfigSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpReadCommunity.setStatus("current")


class _NmAgentConfigSnmpWriteCommunity_Type(DisplayString):
    """Custom type nmAgentConfigSnmpWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NmAgentConfigSnmpWriteCommunity_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpWriteCommunity_Object = MibScalar
nmAgentConfigSnmpWriteCommunity = _NmAgentConfigSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 2),
    _NmAgentConfigSnmpWriteCommunity_Type()
)
nmAgentConfigSnmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpWriteCommunity.setStatus("current")


class _NmAgentConfigSnmpSysLocation_Type(DisplayString):
    """Custom type nmAgentConfigSnmpSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NmAgentConfigSnmpSysLocation_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpSysLocation_Object = MibScalar
nmAgentConfigSnmpSysLocation = _NmAgentConfigSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 3),
    _NmAgentConfigSnmpSysLocation_Type()
)
nmAgentConfigSnmpSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpSysLocation.setStatus("current")


class _NmAgentConfigSnmpSysContact_Type(DisplayString):
    """Custom type nmAgentConfigSnmpSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NmAgentConfigSnmpSysContact_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpSysContact_Object = MibScalar
nmAgentConfigSnmpSysContact = _NmAgentConfigSnmpSysContact_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 4),
    _NmAgentConfigSnmpSysContact_Type()
)
nmAgentConfigSnmpSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpSysContact.setStatus("current")


class _NmAgentConfigSnmpTrapSink1_Type(DisplayString):
    """Custom type nmAgentConfigSnmpTrapSink1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigSnmpTrapSink1_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpTrapSink1_Object = MibScalar
nmAgentConfigSnmpTrapSink1 = _NmAgentConfigSnmpTrapSink1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 5),
    _NmAgentConfigSnmpTrapSink1_Type()
)
nmAgentConfigSnmpTrapSink1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpTrapSink1.setStatus("current")


class _NmAgentConfigSnmpTrapSink2_Type(DisplayString):
    """Custom type nmAgentConfigSnmpTrapSink2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigSnmpTrapSink2_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpTrapSink2_Object = MibScalar
nmAgentConfigSnmpTrapSink2 = _NmAgentConfigSnmpTrapSink2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 6),
    _NmAgentConfigSnmpTrapSink2_Type()
)
nmAgentConfigSnmpTrapSink2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpTrapSink2.setStatus("current")


class _NmAgentConfigSnmpTrapSink3_Type(DisplayString):
    """Custom type nmAgentConfigSnmpTrapSink3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigSnmpTrapSink3_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpTrapSink3_Object = MibScalar
nmAgentConfigSnmpTrapSink3 = _NmAgentConfigSnmpTrapSink3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 7),
    _NmAgentConfigSnmpTrapSink3_Type()
)
nmAgentConfigSnmpTrapSink3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpTrapSink3.setStatus("current")


class _NmAgentConfigSnmpTrapSink4_Type(DisplayString):
    """Custom type nmAgentConfigSnmpTrapSink4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigSnmpTrapSink4_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpTrapSink4_Object = MibScalar
nmAgentConfigSnmpTrapSink4 = _NmAgentConfigSnmpTrapSink4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 8),
    _NmAgentConfigSnmpTrapSink4_Type()
)
nmAgentConfigSnmpTrapSink4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpTrapSink4.setStatus("current")


class _NmAgentConfigSnmpTrapSink5_Type(DisplayString):
    """Custom type nmAgentConfigSnmpTrapSink5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigSnmpTrapSink5_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpTrapSink5_Object = MibScalar
nmAgentConfigSnmpTrapSink5 = _NmAgentConfigSnmpTrapSink5_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 9),
    _NmAgentConfigSnmpTrapSink5_Type()
)
nmAgentConfigSnmpTrapSink5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpTrapSink5.setStatus("current")


class _NmAgentConfigSnmpAgent_Type(Integer32):
    """Custom type nmAgentConfigSnmpAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("snmpV1-V2c", 1),
          ("snmpV3", 2),
          ("notAvailable", 255))
    )


_NmAgentConfigSnmpAgent_Type.__name__ = "Integer32"
_NmAgentConfigSnmpAgent_Object = MibScalar
nmAgentConfigSnmpAgent = _NmAgentConfigSnmpAgent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 10),
    _NmAgentConfigSnmpAgent_Type()
)
nmAgentConfigSnmpAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpAgent.setStatus("current")
_NmAgentConfigSNMPv3UserConfigTable_Object = MibTable
nmAgentConfigSNMPv3UserConfigTable = _NmAgentConfigSNMPv3UserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 11)
)
if mibBuilder.loadTexts:
    nmAgentConfigSNMPv3UserConfigTable.setStatus("current")
_NmAgentConfigSNMPv3UserConfigEntry_Object = MibTableRow
nmAgentConfigSNMPv3UserConfigEntry = _NmAgentConfigSNMPv3UserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 11, 1)
)
nmAgentConfigSNMPv3UserConfigEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmAgentConfigSNMPv3UserConfigIndex"),
)
if mibBuilder.loadTexts:
    nmAgentConfigSNMPv3UserConfigEntry.setStatus("current")


class _NmAgentConfigSNMPv3UserConfigIndex_Type(Integer32):
    """Custom type nmAgentConfigSNMPv3UserConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_NmAgentConfigSNMPv3UserConfigIndex_Type.__name__ = "Integer32"
_NmAgentConfigSNMPv3UserConfigIndex_Object = MibTableColumn
nmAgentConfigSNMPv3UserConfigIndex = _NmAgentConfigSNMPv3UserConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 11, 1, 1),
    _NmAgentConfigSNMPv3UserConfigIndex_Type()
)
nmAgentConfigSNMPv3UserConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentConfigSNMPv3UserConfigIndex.setStatus("current")


class _NmAgentConfigSnmpv3UserConfigName_Type(DisplayString):
    """Custom type nmAgentConfigSnmpv3UserConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentConfigSnmpv3UserConfigName_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpv3UserConfigName_Object = MibTableColumn
nmAgentConfigSnmpv3UserConfigName = _NmAgentConfigSnmpv3UserConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 11, 1, 2),
    _NmAgentConfigSnmpv3UserConfigName_Type()
)
nmAgentConfigSnmpv3UserConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpv3UserConfigName.setStatus("current")


class _NmAgentConfigSnmpv3UserConfigUserLevel_Type(Integer32):
    """Custom type nmAgentConfigSnmpv3UserConfigUserLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("rouser", 1),
          ("rwuser", 2))
    )


_NmAgentConfigSnmpv3UserConfigUserLevel_Type.__name__ = "Integer32"
_NmAgentConfigSnmpv3UserConfigUserLevel_Object = MibTableColumn
nmAgentConfigSnmpv3UserConfigUserLevel = _NmAgentConfigSnmpv3UserConfigUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 11, 1, 3),
    _NmAgentConfigSnmpv3UserConfigUserLevel_Type()
)
nmAgentConfigSnmpv3UserConfigUserLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpv3UserConfigUserLevel.setStatus("current")


class _NmAgentConfigSnmpv3UserConfigAuthType_Type(Integer32):
    """Custom type nmAgentConfigSnmpv3UserConfigAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("mD5", 1),
          ("sHA", 2))
    )


_NmAgentConfigSnmpv3UserConfigAuthType_Type.__name__ = "Integer32"
_NmAgentConfigSnmpv3UserConfigAuthType_Object = MibTableColumn
nmAgentConfigSnmpv3UserConfigAuthType = _NmAgentConfigSnmpv3UserConfigAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 11, 1, 4),
    _NmAgentConfigSnmpv3UserConfigAuthType_Type()
)
nmAgentConfigSnmpv3UserConfigAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpv3UserConfigAuthType.setStatus("current")


class _NmAgentConfigSnmpv3UserConfigAuthPassPhrase_Type(DisplayString):
    """Custom type nmAgentConfigSnmpv3UserConfigAuthPassPhrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentConfigSnmpv3UserConfigAuthPassPhrase_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpv3UserConfigAuthPassPhrase_Object = MibTableColumn
nmAgentConfigSnmpv3UserConfigAuthPassPhrase = _NmAgentConfigSnmpv3UserConfigAuthPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 11, 1, 5),
    _NmAgentConfigSnmpv3UserConfigAuthPassPhrase_Type()
)
nmAgentConfigSnmpv3UserConfigAuthPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpv3UserConfigAuthPassPhrase.setStatus("current")


class _NmAgentConfigSnmpv3UserConfigEncType_Type(Integer32):
    """Custom type nmAgentConfigSnmpv3UserConfigEncType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("dES", 1),
          ("aES", 2))
    )


_NmAgentConfigSnmpv3UserConfigEncType_Type.__name__ = "Integer32"
_NmAgentConfigSnmpv3UserConfigEncType_Object = MibTableColumn
nmAgentConfigSnmpv3UserConfigEncType = _NmAgentConfigSnmpv3UserConfigEncType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 11, 1, 6),
    _NmAgentConfigSnmpv3UserConfigEncType_Type()
)
nmAgentConfigSnmpv3UserConfigEncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpv3UserConfigEncType.setStatus("current")


class _NmAgentConfigSnmpv3UserConfigPrivPassPhrase_Type(DisplayString):
    """Custom type nmAgentConfigSnmpv3UserConfigPrivPassPhrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentConfigSnmpv3UserConfigPrivPassPhrase_Type.__name__ = "DisplayString"
_NmAgentConfigSnmpv3UserConfigPrivPassPhrase_Object = MibTableColumn
nmAgentConfigSnmpv3UserConfigPrivPassPhrase = _NmAgentConfigSnmpv3UserConfigPrivPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 2, 11, 1, 7),
    _NmAgentConfigSnmpv3UserConfigPrivPassPhrase_Type()
)
nmAgentConfigSnmpv3UserConfigPrivPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSnmpv3UserConfigPrivPassPhrase.setStatus("current")
_NmAgentConfigSlotAlarmsTable_Object = MibTable
nmAgentConfigSlotAlarmsTable = _NmAgentConfigSlotAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    nmAgentConfigSlotAlarmsTable.setStatus("current")
_NmAgentConfigSlotAlarmsEntry_Object = MibTableRow
nmAgentConfigSlotAlarmsEntry = _NmAgentConfigSlotAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 3, 1)
)
nmAgentConfigSlotAlarmsEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmAgentConfigSlotAlarmsSlotNumber"),
)
if mibBuilder.loadTexts:
    nmAgentConfigSlotAlarmsEntry.setStatus("current")


class _NmAgentConfigSlotAlarmsSlotNumber_Type(Integer32):
    """Custom type nmAgentConfigSlotAlarmsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NmAgentConfigSlotAlarmsSlotNumber_Type.__name__ = "Integer32"
_NmAgentConfigSlotAlarmsSlotNumber_Object = MibTableColumn
nmAgentConfigSlotAlarmsSlotNumber = _NmAgentConfigSlotAlarmsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 3, 1, 1),
    _NmAgentConfigSlotAlarmsSlotNumber_Type()
)
nmAgentConfigSlotAlarmsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentConfigSlotAlarmsSlotNumber.setStatus("current")


class _NmAgentConfigSlotAlarmsInsertedCard_Type(DisplayString):
    """Custom type nmAgentConfigSlotAlarmsInsertedCard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NmAgentConfigSlotAlarmsInsertedCard_Type.__name__ = "DisplayString"
_NmAgentConfigSlotAlarmsInsertedCard_Object = MibTableColumn
nmAgentConfigSlotAlarmsInsertedCard = _NmAgentConfigSlotAlarmsInsertedCard_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 3, 1, 2),
    _NmAgentConfigSlotAlarmsInsertedCard_Type()
)
nmAgentConfigSlotAlarmsInsertedCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentConfigSlotAlarmsInsertedCard.setStatus("current")


class _NmAgentConfigSlotAlarmsConfig_Type(Integer32):
    """Custom type nmAgentConfigSlotAlarmsConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("alarmsEnabled", 0),
          ("alarmsDisabled", 1),
          ("fail", 255))
    )


_NmAgentConfigSlotAlarmsConfig_Type.__name__ = "Integer32"
_NmAgentConfigSlotAlarmsConfig_Object = MibTableColumn
nmAgentConfigSlotAlarmsConfig = _NmAgentConfigSlotAlarmsConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 3, 1, 3),
    _NmAgentConfigSlotAlarmsConfig_Type()
)
nmAgentConfigSlotAlarmsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSlotAlarmsConfig.setStatus("current")
_NmAgentConfigSlotModulesTable_Object = MibTable
nmAgentConfigSlotModulesTable = _NmAgentConfigSlotModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    nmAgentConfigSlotModulesTable.setStatus("current")
_NmAgentConfigSlotModulesEntry_Object = MibTableRow
nmAgentConfigSlotModulesEntry = _NmAgentConfigSlotModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 4, 1)
)
nmAgentConfigSlotModulesEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmAgentConfigModulesSlotNumber"),
)
if mibBuilder.loadTexts:
    nmAgentConfigSlotModulesEntry.setStatus("current")


class _NmAgentConfigModulesSlotNumber_Type(Integer32):
    """Custom type nmAgentConfigModulesSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NmAgentConfigModulesSlotNumber_Type.__name__ = "Integer32"
_NmAgentConfigModulesSlotNumber_Object = MibTableColumn
nmAgentConfigModulesSlotNumber = _NmAgentConfigModulesSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 4, 1, 1),
    _NmAgentConfigModulesSlotNumber_Type()
)
nmAgentConfigModulesSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentConfigModulesSlotNumber.setStatus("current")


class _NmAgentConfigModulesInstalledCard_Type(DisplayString):
    """Custom type nmAgentConfigModulesInstalledCard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NmAgentConfigModulesInstalledCard_Type.__name__ = "DisplayString"
_NmAgentConfigModulesInstalledCard_Object = MibTableColumn
nmAgentConfigModulesInstalledCard = _NmAgentConfigModulesInstalledCard_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 4, 1, 2),
    _NmAgentConfigModulesInstalledCard_Type()
)
nmAgentConfigModulesInstalledCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentConfigModulesInstalledCard.setStatus("current")


class _NmAgentConfigModulesExpectedCard_Type(Integer32):
    """Custom type nmAgentConfigModulesExpectedCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              71,
              72,
              74,
              75,
              80,
              81,
              83,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 0),
          ("speedCWDM21", 11),
          ("speedCWDM41", 12),
          ("speedCWDM41E", 13),
          ("speedCWDM51", 14),
          ("speedCWDM81", 15),
          ("speedCWDM81E", 16),
          ("speedCWDM91", 17),
          ("speedADCWDM", 18),
          ("oneSlotPassiveCard", 19),
          ("twoSlotPassiveCard", 20),
          ("threeSlotPassiveCard", 21),
          ("speedNMS", 50),
          ("speedNMS4ETH", 51),
          ("speedDualline3RProt", 53),
          ("speedDualline3R", 54),
          ("speedDuallineSfp3RB", 55),
          ("speedDuallineSfp", 56),
          ("speedSinglelineSfp", 57),
          ("speedSinglelineXFP3R", 58),
          ("speedSinglelineXFP", 59),
          ("speedDuallineFcXFP", 60),
          ("speedDuallineFcSfp", 61),
          ("speedDualline10GXFP", 62),
          ("speedDualline10GSfp", 63),
          ("speedDualline16GXFP", 64),
          ("speedDualline16GSfp", 65),
          ("speedDualline10GXFP2R", 66),
          ("speedDualline16GSfpH", 67),
          ("speedMux200G2CFP", 71),
          ("speedMux200G2CFPS", 72),
          ("speedMux200GCFP2", 74),
          ("speedMux200GCFP2S", 75),
          ("speedDuallineSfp2R", 80),
          ("speedDualline10G3R", 81),
          ("speedSixline10G3R", 83),
          ("speedAmpEdfaPREAMP14", 101),
          ("speedAmpEdfaBOOSTER17", 102),
          ("speedAmpEdfaBOOSTER17OSC", 103),
          ("speedAmpEdfaBOOSTER23OSC", 104),
          ("speedAmpEdfaINLINE17OSC", 105),
          ("speedAmpEdfaINLINE23OSC", 106),
          ("speedAmpReserved1", 107),
          ("speedAmpReserved2", 108),
          ("speedAmpReserved3", 109),
          ("speedAmpReserved4", 110),
          ("speedAmpRamanSTANDALONE10", 111),
          ("speedAmpRamanSTANDALONE15", 112),
          ("speedAmpEdfaPREAMP14Ext", 113),
          ("speedAmpEdfaBOOSTER17Ext", 114),
          ("speedAmpEdfaBOOSTER17OSCExt", 115),
          ("speedAmpEdfaBOOSTER23OSCExt", 116),
          ("speedAmpEdfaINLINE17OSCExt", 117),
          ("speedAmpEdfaINLINE23OSCExt", 118),
          ("reserved", 255))
    )


_NmAgentConfigModulesExpectedCard_Type.__name__ = "Integer32"
_NmAgentConfigModulesExpectedCard_Object = MibTableColumn
nmAgentConfigModulesExpectedCard = _NmAgentConfigModulesExpectedCard_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 4, 1, 3),
    _NmAgentConfigModulesExpectedCard_Type()
)
nmAgentConfigModulesExpectedCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigModulesExpectedCard.setStatus("current")


class _NmAgentConfigModulesSlotText_Type(DisplayString):
    """Custom type nmAgentConfigModulesSlotText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentConfigModulesSlotText_Type.__name__ = "DisplayString"
_NmAgentConfigModulesSlotText_Object = MibTableColumn
nmAgentConfigModulesSlotText = _NmAgentConfigModulesSlotText_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 4, 1, 4),
    _NmAgentConfigModulesSlotText_Type()
)
nmAgentConfigModulesSlotText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigModulesSlotText.setStatus("current")


class _NmAgentConfigModulesInstalledState_Type(DisplayString):
    """Custom type nmAgentConfigModulesInstalledState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentConfigModulesInstalledState_Type.__name__ = "DisplayString"
_NmAgentConfigModulesInstalledState_Object = MibTableColumn
nmAgentConfigModulesInstalledState = _NmAgentConfigModulesInstalledState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 4, 1, 5),
    _NmAgentConfigModulesInstalledState_Type()
)
nmAgentConfigModulesInstalledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentConfigModulesInstalledState.setStatus("current")


class _NmAgentConfigAlarmRelay_Type(Integer32):
    """Custom type nmAgentConfigAlarmRelay based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("psu", 1),
          ("fan", 2),
          ("psuFan", 3),
          ("slots", 4),
          ("psuSlots", 5),
          ("fanSlots", 6),
          ("psuFanSlots", 7),
          ("notAvailable", 255))
    )


_NmAgentConfigAlarmRelay_Type.__name__ = "Integer32"
_NmAgentConfigAlarmRelay_Object = MibScalar
nmAgentConfigAlarmRelay = _NmAgentConfigAlarmRelay_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 7),
    _NmAgentConfigAlarmRelay_Type()
)
nmAgentConfigAlarmRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigAlarmRelay.setStatus("current")


class _NmAgentConfigFAN_Type(Integer32):
    """Custom type nmAgentConfigFAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOn", 1),
          ("auto", 2))
    )


_NmAgentConfigFAN_Type.__name__ = "Integer32"
_NmAgentConfigFAN_Object = MibScalar
nmAgentConfigFAN = _NmAgentConfigFAN_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 8),
    _NmAgentConfigFAN_Type()
)
nmAgentConfigFAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigFAN.setStatus("current")


class _NmAgentConfigNtpServer_Type(DisplayString):
    """Custom type nmAgentConfigNtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigNtpServer_Type.__name__ = "DisplayString"
_NmAgentConfigNtpServer_Object = MibScalar
nmAgentConfigNtpServer = _NmAgentConfigNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 9),
    _NmAgentConfigNtpServer_Type()
)
nmAgentConfigNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigNtpServer.setStatus("current")


class _NmAgentConfigTftpServer_Type(Integer32):
    """Custom type nmAgentConfigTftpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notAvailable", 255))
    )


_NmAgentConfigTftpServer_Type.__name__ = "Integer32"
_NmAgentConfigTftpServer_Object = MibScalar
nmAgentConfigTftpServer = _NmAgentConfigTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 10),
    _NmAgentConfigTftpServer_Type()
)
nmAgentConfigTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigTftpServer.setStatus("current")


class _NmAgentConfigWebServer_Type(Integer32):
    """Custom type nmAgentConfigWebServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("http", 1),
          ("https", 2),
          ("notAvailable", 255))
    )


_NmAgentConfigWebServer_Type.__name__ = "Integer32"
_NmAgentConfigWebServer_Object = MibScalar
nmAgentConfigWebServer = _NmAgentConfigWebServer_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 11),
    _NmAgentConfigWebServer_Type()
)
nmAgentConfigWebServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigWebServer.setStatus("current")


class _NmAgentConfigMyWebView_Type(Integer32):
    """Custom type nmAgentConfigMyWebView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pictureAndDeviceList", 1),
          ("pictureAndActiveAlarms", 2),
          ("deviceListAndActiveAlarms", 3),
          ("notAvailable", 255))
    )


_NmAgentConfigMyWebView_Type.__name__ = "Integer32"
_NmAgentConfigMyWebView_Object = MibScalar
nmAgentConfigMyWebView = _NmAgentConfigMyWebView_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 12),
    _NmAgentConfigMyWebView_Type()
)
nmAgentConfigMyWebView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigMyWebView.setStatus("current")


class _NmAgentConfigTimezone_Type(Integer32):
    """Custom type nmAgentConfigTimezone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("utc", 0),
          ("cet", 1),
          ("jst", 2),
          ("notAvailable", 255))
    )


_NmAgentConfigTimezone_Type.__name__ = "Integer32"
_NmAgentConfigTimezone_Object = MibScalar
nmAgentConfigTimezone = _NmAgentConfigTimezone_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 15),
    _NmAgentConfigTimezone_Type()
)
nmAgentConfigTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigTimezone.setStatus("current")


class _NmAgentConfigAccess_Type(Integer32):
    """Custom type nmAgentConfigAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("off", 1),
          ("telnet", 2),
          ("ssh2", 3),
          ("sshWithPreSharedKeys", 4))
    )


_NmAgentConfigAccess_Type.__name__ = "Integer32"
_NmAgentConfigAccess_Object = MibScalar
nmAgentConfigAccess = _NmAgentConfigAccess_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 16),
    _NmAgentConfigAccess_Type()
)
nmAgentConfigAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigAccess.setStatus("current")


class _NmAgentConfigCliTimeout_Type(Integer32):
    """Custom type nmAgentConfigCliTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_NmAgentConfigCliTimeout_Type.__name__ = "Integer32"
_NmAgentConfigCliTimeout_Object = MibScalar
nmAgentConfigCliTimeout = _NmAgentConfigCliTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 17),
    _NmAgentConfigCliTimeout_Type()
)
nmAgentConfigCliTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigCliTimeout.setStatus("current")


class _NmAgentConfigRadiusStateConfig_Type(Integer32):
    """Custom type nmAgentConfigRadiusStateConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("useLocalPasswords", 1),
          ("useRadiusAuthentication", 2))
    )


_NmAgentConfigRadiusStateConfig_Type.__name__ = "Integer32"
_NmAgentConfigRadiusStateConfig_Object = MibScalar
nmAgentConfigRadiusStateConfig = _NmAgentConfigRadiusStateConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 19),
    _NmAgentConfigRadiusStateConfig_Type()
)
nmAgentConfigRadiusStateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigRadiusStateConfig.setStatus("current")


class _NmAgentConfigNMSState_Type(Integer32):
    """Custom type nmAgentConfigNMSState based on Integer32"""
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
        *(("notAvailable", 0),
          ("running", 1),
          ("resetSystem", 2),
          ("resetConfig", 3))
    )


_NmAgentConfigNMSState_Type.__name__ = "Integer32"
_NmAgentConfigNMSState_Object = MibScalar
nmAgentConfigNMSState = _NmAgentConfigNMSState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 21),
    _NmAgentConfigNMSState_Type()
)
nmAgentConfigNMSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigNMSState.setStatus("current")
_NmAgentConfigRadiusServerConfigTable_Object = MibTable
nmAgentConfigRadiusServerConfigTable = _NmAgentConfigRadiusServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 26)
)
if mibBuilder.loadTexts:
    nmAgentConfigRadiusServerConfigTable.setStatus("current")
_NmAgentConfigRadiusServerConfigEntry_Object = MibTableRow
nmAgentConfigRadiusServerConfigEntry = _NmAgentConfigRadiusServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 26, 1)
)
nmAgentConfigRadiusServerConfigEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmAgentConfigRadiusServerConfigNumber"),
)
if mibBuilder.loadTexts:
    nmAgentConfigRadiusServerConfigEntry.setStatus("current")


class _NmAgentConfigRadiusServerConfigNumber_Type(Integer32):
    """Custom type nmAgentConfigRadiusServerConfigNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NmAgentConfigRadiusServerConfigNumber_Type.__name__ = "Integer32"
_NmAgentConfigRadiusServerConfigNumber_Object = MibTableColumn
nmAgentConfigRadiusServerConfigNumber = _NmAgentConfigRadiusServerConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 26, 1, 1),
    _NmAgentConfigRadiusServerConfigNumber_Type()
)
nmAgentConfigRadiusServerConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentConfigRadiusServerConfigNumber.setStatus("current")


class _NmAgentConfigRadiusServerConfigIPAddress_Type(DisplayString):
    """Custom type nmAgentConfigRadiusServerConfigIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigRadiusServerConfigIPAddress_Type.__name__ = "DisplayString"
_NmAgentConfigRadiusServerConfigIPAddress_Object = MibTableColumn
nmAgentConfigRadiusServerConfigIPAddress = _NmAgentConfigRadiusServerConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 26, 1, 2),
    _NmAgentConfigRadiusServerConfigIPAddress_Type()
)
nmAgentConfigRadiusServerConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigRadiusServerConfigIPAddress.setStatus("current")


class _NmAgentConfigRadiusServerConfigSharedSecret_Type(DisplayString):
    """Custom type nmAgentConfigRadiusServerConfigSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentConfigRadiusServerConfigSharedSecret_Type.__name__ = "DisplayString"
_NmAgentConfigRadiusServerConfigSharedSecret_Object = MibTableColumn
nmAgentConfigRadiusServerConfigSharedSecret = _NmAgentConfigRadiusServerConfigSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 26, 1, 3),
    _NmAgentConfigRadiusServerConfigSharedSecret_Type()
)
nmAgentConfigRadiusServerConfigSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigRadiusServerConfigSharedSecret.setStatus("current")


class _NmAgentConfigSyslogServerIPAddress_Type(DisplayString):
    """Custom type nmAgentConfigSyslogServerIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NmAgentConfigSyslogServerIPAddress_Type.__name__ = "DisplayString"
_NmAgentConfigSyslogServerIPAddress_Object = MibScalar
nmAgentConfigSyslogServerIPAddress = _NmAgentConfigSyslogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 27),
    _NmAgentConfigSyslogServerIPAddress_Type()
)
nmAgentConfigSyslogServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSyslogServerIPAddress.setStatus("current")


class _NmAgentConfigSyslogSeverity_Type(Integer32):
    """Custom type nmAgentConfigSyslogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7))
    )


_NmAgentConfigSyslogSeverity_Type.__name__ = "Integer32"
_NmAgentConfigSyslogSeverity_Object = MibScalar
nmAgentConfigSyslogSeverity = _NmAgentConfigSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 28),
    _NmAgentConfigSyslogSeverity_Type()
)
nmAgentConfigSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSyslogSeverity.setStatus("current")


class _NmAgentConfigSyslogFacility_Type(Integer32):
    """Custom type nmAgentConfigSyslogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16)
        )
    )
    namedValues = NamedValues(
        *(("userLevelMessages", 1),
          ("all", 16))
    )


_NmAgentConfigSyslogFacility_Type.__name__ = "Integer32"
_NmAgentConfigSyslogFacility_Object = MibScalar
nmAgentConfigSyslogFacility = _NmAgentConfigSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 2, 29),
    _NmAgentConfigSyslogFacility_Type()
)
nmAgentConfigSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentConfigSyslogFacility.setStatus("current")
_NmAgentPorts_ObjectIdentity = ObjectIdentity
nmAgentPorts = _NmAgentPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3)
)
_NmAgentPortsPortOverviewTable_Object = MibTable
nmAgentPortsPortOverviewTable = _NmAgentPortsPortOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nmAgentPortsPortOverviewTable.setStatus("current")
_NmAgentPortsPortOverviewEntry_Object = MibTableRow
nmAgentPortsPortOverviewEntry = _NmAgentPortsPortOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1)
)
nmAgentPortsPortOverviewEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmAgentPortsIndex"),
)
if mibBuilder.loadTexts:
    nmAgentPortsPortOverviewEntry.setStatus("current")


class _NmAgentPortsIndex_Type(Integer32):
    """Custom type nmAgentPortsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_NmAgentPortsIndex_Type.__name__ = "Integer32"
_NmAgentPortsIndex_Object = MibTableColumn
nmAgentPortsIndex = _NmAgentPortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1, 1),
    _NmAgentPortsIndex_Type()
)
nmAgentPortsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmAgentPortsIndex.setStatus("current")
_NmAgentPortsSlot_Type = Integer32
_NmAgentPortsSlot_Object = MibTableColumn
nmAgentPortsSlot = _NmAgentPortsSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1, 2),
    _NmAgentPortsSlot_Type()
)
nmAgentPortsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSlot.setStatus("current")
_NmAgentPortsPort_Type = Integer32
_NmAgentPortsPort_Object = MibTableColumn
nmAgentPortsPort = _NmAgentPortsPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1, 3),
    _NmAgentPortsPort_Type()
)
nmAgentPortsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsPort.setStatus("current")


class _NmAgentPortsAdminConfig_Type(Integer32):
    """Custom type nmAgentPortsAdminConfig based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("adminDown", 1),
          ("hdx10", 2),
          ("fdx10", 3),
          ("hdx100", 4),
          ("fdx100", 5),
          ("adminAutoneg", 6),
          ("x1000", 7),
          ("unknown", 255))
    )


_NmAgentPortsAdminConfig_Type.__name__ = "Integer32"
_NmAgentPortsAdminConfig_Object = MibTableColumn
nmAgentPortsAdminConfig = _NmAgentPortsAdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1, 4),
    _NmAgentPortsAdminConfig_Type()
)
nmAgentPortsAdminConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentPortsAdminConfig.setStatus("current")


class _NmAgentPortsOperStateSFP_Type(Integer32):
    """Custom type nmAgentPortsOperStateSFP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("notInserted", 1),
          ("up", 2),
          ("down", 3),
          ("txFault", 4),
          ("txDisabled", 5),
          ("unknown", 255))
    )


_NmAgentPortsOperStateSFP_Type.__name__ = "Integer32"
_NmAgentPortsOperStateSFP_Object = MibTableColumn
nmAgentPortsOperStateSFP = _NmAgentPortsOperStateSFP_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1, 5),
    _NmAgentPortsOperStateSFP_Type()
)
nmAgentPortsOperStateSFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsOperStateSFP.setStatus("current")


class _NmAgentPortsAlarmState_Type(Integer32):
    """Custom type nmAgentPortsAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("inactive", 1),
          ("active", 2),
          ("unknown", 255))
    )


_NmAgentPortsAlarmState_Type.__name__ = "Integer32"
_NmAgentPortsAlarmState_Object = MibTableColumn
nmAgentPortsAlarmState = _NmAgentPortsAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1, 6),
    _NmAgentPortsAlarmState_Type()
)
nmAgentPortsAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsAlarmState.setStatus("current")


class _NmAgentPortsPortType_Type(DisplayString):
    """Custom type nmAgentPortsPortType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentPortsPortType_Type.__name__ = "DisplayString"
_NmAgentPortsPortType_Object = MibTableColumn
nmAgentPortsPortType = _NmAgentPortsPortType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1, 7),
    _NmAgentPortsPortType_Type()
)
nmAgentPortsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsPortType.setStatus("current")


class _NmAgentPortsPortDescription_Type(DisplayString):
    """Custom type nmAgentPortsPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentPortsPortDescription_Type.__name__ = "DisplayString"
_NmAgentPortsPortDescription_Object = MibTableColumn
nmAgentPortsPortDescription = _NmAgentPortsPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1, 8),
    _NmAgentPortsPortDescription_Type()
)
nmAgentPortsPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAgentPortsPortDescription.setStatus("current")


class _NmAgentPortsOperStateCopper_Type(Integer32):
    """Custom type nmAgentPortsOperStateCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up10hdx", 1),
          ("up10fdx", 2),
          ("up100hdx", 3),
          ("up100fdx", 4),
          ("up1000x", 5),
          ("notAvailable", 255))
    )


_NmAgentPortsOperStateCopper_Type.__name__ = "Integer32"
_NmAgentPortsOperStateCopper_Object = MibTableColumn
nmAgentPortsOperStateCopper = _NmAgentPortsOperStateCopper_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 1, 1, 9),
    _NmAgentPortsOperStateCopper_Type()
)
nmAgentPortsOperStateCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsOperStateCopper.setStatus("current")
_NmAgentPortsSFPOverviewTable_Object = MibTable
nmAgentPortsSFPOverviewTable = _NmAgentPortsSFPOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nmAgentPortsSFPOverviewTable.setStatus("current")
_NmAgentPortsSFPOverviewEntry_Object = MibTableRow
nmAgentPortsSFPOverviewEntry = _NmAgentPortsSFPOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1)
)
nmAgentPortsSFPOverviewEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmAgentPortsSFPIndex"),
)
if mibBuilder.loadTexts:
    nmAgentPortsSFPOverviewEntry.setStatus("current")


class _NmAgentPortsSFPIndex_Type(Integer32):
    """Custom type nmAgentPortsSFPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_NmAgentPortsSFPIndex_Type.__name__ = "Integer32"
_NmAgentPortsSFPIndex_Object = MibTableColumn
nmAgentPortsSFPIndex = _NmAgentPortsSFPIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1, 1),
    _NmAgentPortsSFPIndex_Type()
)
nmAgentPortsSFPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmAgentPortsSFPIndex.setStatus("current")
_NmAgentPortsSFPSlot_Type = Integer32
_NmAgentPortsSFPSlot_Object = MibTableColumn
nmAgentPortsSFPSlot = _NmAgentPortsSFPSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1, 2),
    _NmAgentPortsSFPSlot_Type()
)
nmAgentPortsSFPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPSlot.setStatus("current")
_NmAgentPortsSFPPort_Type = Integer32
_NmAgentPortsSFPPort_Object = MibTableColumn
nmAgentPortsSFPPort = _NmAgentPortsSFPPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1, 3),
    _NmAgentPortsSFPPort_Type()
)
nmAgentPortsSFPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPPort.setStatus("current")


class _NmAgentPortsSFPState_Type(Integer32):
    """Custom type nmAgentPortsSFPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sfpRemoved", 1),
          ("sfpInstalled", 2),
          ("notAvailable", 255))
    )


_NmAgentPortsSFPState_Type.__name__ = "Integer32"
_NmAgentPortsSFPState_Object = MibTableColumn
nmAgentPortsSFPState = _NmAgentPortsSFPState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1, 4),
    _NmAgentPortsSFPState_Type()
)
nmAgentPortsSFPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPState.setStatus("current")
_NmAgentPortsDMIState_Type = Integer32
_NmAgentPortsDMIState_Object = MibTableColumn
nmAgentPortsDMIState = _NmAgentPortsDMIState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1, 5),
    _NmAgentPortsDMIState_Type()
)
nmAgentPortsDMIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsDMIState.setStatus("current")


class _NmAgentPortsVendorName_Type(DisplayString):
    """Custom type nmAgentPortsVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentPortsVendorName_Type.__name__ = "DisplayString"
_NmAgentPortsVendorName_Object = MibTableColumn
nmAgentPortsVendorName = _NmAgentPortsVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1, 6),
    _NmAgentPortsVendorName_Type()
)
nmAgentPortsVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsVendorName.setStatus("current")


class _NmAgentPortsVendorPartNumber_Type(DisplayString):
    """Custom type nmAgentPortsVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentPortsVendorPartNumber_Type.__name__ = "DisplayString"
_NmAgentPortsVendorPartNumber_Object = MibTableColumn
nmAgentPortsVendorPartNumber = _NmAgentPortsVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1, 7),
    _NmAgentPortsVendorPartNumber_Type()
)
nmAgentPortsVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsVendorPartNumber.setStatus("current")


class _NmAgentPortsVendorSerialNumber_Type(DisplayString):
    """Custom type nmAgentPortsVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmAgentPortsVendorSerialNumber_Type.__name__ = "DisplayString"
_NmAgentPortsVendorSerialNumber_Object = MibTableColumn
nmAgentPortsVendorSerialNumber = _NmAgentPortsVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1, 8),
    _NmAgentPortsVendorSerialNumber_Type()
)
nmAgentPortsVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsVendorSerialNumber.setStatus("current")
_NmAgentPortsWavelength_Type = Integer32
_NmAgentPortsWavelength_Object = MibTableColumn
nmAgentPortsWavelength = _NmAgentPortsWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 2, 1, 9),
    _NmAgentPortsWavelength_Type()
)
nmAgentPortsWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsWavelength.setStatus("current")
_NmAgentPortsSFPMeassurementTable_Object = MibTable
nmAgentPortsSFPMeassurementTable = _NmAgentPortsSFPMeassurementTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    nmAgentPortsSFPMeassurementTable.setStatus("current")
_NmAgentPortsSFPMeassurementEntry_Object = MibTableRow
nmAgentPortsSFPMeassurementEntry = _NmAgentPortsSFPMeassurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3, 1)
)
nmAgentPortsSFPMeassurementEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmAgentPortsSFPMIndex"),
)
if mibBuilder.loadTexts:
    nmAgentPortsSFPMeassurementEntry.setStatus("current")


class _NmAgentPortsSFPMIndex_Type(Integer32):
    """Custom type nmAgentPortsSFPMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_NmAgentPortsSFPMIndex_Type.__name__ = "Integer32"
_NmAgentPortsSFPMIndex_Object = MibTableColumn
nmAgentPortsSFPMIndex = _NmAgentPortsSFPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3, 1, 1),
    _NmAgentPortsSFPMIndex_Type()
)
nmAgentPortsSFPMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmAgentPortsSFPMIndex.setStatus("current")
_NmAgentPortsSFPMSlot_Type = Integer32
_NmAgentPortsSFPMSlot_Object = MibTableColumn
nmAgentPortsSFPMSlot = _NmAgentPortsSFPMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3, 1, 2),
    _NmAgentPortsSFPMSlot_Type()
)
nmAgentPortsSFPMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPMSlot.setStatus("current")
_NmAgentPortsSFPMPort_Type = Integer32
_NmAgentPortsSFPMPort_Object = MibTableColumn
nmAgentPortsSFPMPort = _NmAgentPortsSFPMPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3, 1, 3),
    _NmAgentPortsSFPMPort_Type()
)
nmAgentPortsSFPMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPMPort.setStatus("current")
_NmAgentPortsSFPDMIRxLevel_Type = Integer32
_NmAgentPortsSFPDMIRxLevel_Object = MibTableColumn
nmAgentPortsSFPDMIRxLevel = _NmAgentPortsSFPDMIRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3, 1, 4),
    _NmAgentPortsSFPDMIRxLevel_Type()
)
nmAgentPortsSFPDMIRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMIRxLevel.setStatus("current")
_NmAgentPortsSFPDMITxLevel_Type = Integer32
_NmAgentPortsSFPDMITxLevel_Object = MibTableColumn
nmAgentPortsSFPDMITxLevel = _NmAgentPortsSFPDMITxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3, 1, 5),
    _NmAgentPortsSFPDMITxLevel_Type()
)
nmAgentPortsSFPDMITxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMITxLevel.setStatus("current")
_NmAgentPortsSFPDMITxBias_Type = Integer32
_NmAgentPortsSFPDMITxBias_Object = MibTableColumn
nmAgentPortsSFPDMITxBias = _NmAgentPortsSFPDMITxBias_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3, 1, 6),
    _NmAgentPortsSFPDMITxBias_Type()
)
nmAgentPortsSFPDMITxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMITxBias.setStatus("current")
_NmAgentPortsSFPDMIVcc_Type = Integer32
_NmAgentPortsSFPDMIVcc_Object = MibTableColumn
nmAgentPortsSFPDMIVcc = _NmAgentPortsSFPDMIVcc_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3, 1, 7),
    _NmAgentPortsSFPDMIVcc_Type()
)
nmAgentPortsSFPDMIVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMIVcc.setStatus("current")
_NmAgentPortsSFPDMITemp_Type = Integer32
_NmAgentPortsSFPDMITemp_Object = MibTableColumn
nmAgentPortsSFPDMITemp = _NmAgentPortsSFPDMITemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 3, 1, 8),
    _NmAgentPortsSFPDMITemp_Type()
)
nmAgentPortsSFPDMITemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMITemp.setStatus("current")
_NmAgentPortsSFPAlarmTable_Object = MibTable
nmAgentPortsSFPAlarmTable = _NmAgentPortsSFPAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    nmAgentPortsSFPAlarmTable.setStatus("current")
_NmAgentPortsSFPAlarmEntry_Object = MibTableRow
nmAgentPortsSFPAlarmEntry = _NmAgentPortsSFPAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1)
)
nmAgentPortsSFPAlarmEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmAgentPortsSFPAIndex"),
)
if mibBuilder.loadTexts:
    nmAgentPortsSFPAlarmEntry.setStatus("current")


class _NmAgentPortsSFPAIndex_Type(Integer32):
    """Custom type nmAgentPortsSFPAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_NmAgentPortsSFPAIndex_Type.__name__ = "Integer32"
_NmAgentPortsSFPAIndex_Object = MibTableColumn
nmAgentPortsSFPAIndex = _NmAgentPortsSFPAIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 1),
    _NmAgentPortsSFPAIndex_Type()
)
nmAgentPortsSFPAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmAgentPortsSFPAIndex.setStatus("current")
_NmAgentPortsSFPASlot_Type = Integer32
_NmAgentPortsSFPASlot_Object = MibTableColumn
nmAgentPortsSFPASlot = _NmAgentPortsSFPASlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 2),
    _NmAgentPortsSFPASlot_Type()
)
nmAgentPortsSFPASlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPASlot.setStatus("current")
_NmAgentPortsSFPAPort_Type = Integer32
_NmAgentPortsSFPAPort_Object = MibTableColumn
nmAgentPortsSFPAPort = _NmAgentPortsSFPAPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 3),
    _NmAgentPortsSFPAPort_Type()
)
nmAgentPortsSFPAPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPAPort.setStatus("current")


class _NmAgentPortsSFPDMIRxLowWarningEvent_Type(Integer32):
    """Custom type nmAgentPortsSFPDMIRxLowWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("inactive", 1),
          ("active", 2),
          ("notimplemented", 255))
    )


_NmAgentPortsSFPDMIRxLowWarningEvent_Type.__name__ = "Integer32"
_NmAgentPortsSFPDMIRxLowWarningEvent_Object = MibTableColumn
nmAgentPortsSFPDMIRxLowWarningEvent = _NmAgentPortsSFPDMIRxLowWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 4),
    _NmAgentPortsSFPDMIRxLowWarningEvent_Type()
)
nmAgentPortsSFPDMIRxLowWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMIRxLowWarningEvent.setStatus("current")


class _NmAgentPortsSFPDMIRxLowAlarmEvent_Type(Integer32):
    """Custom type nmAgentPortsSFPDMIRxLowAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("inactive", 1),
          ("active", 2),
          ("notimplemented", 255))
    )


_NmAgentPortsSFPDMIRxLowAlarmEvent_Type.__name__ = "Integer32"
_NmAgentPortsSFPDMIRxLowAlarmEvent_Object = MibTableColumn
nmAgentPortsSFPDMIRxLowAlarmEvent = _NmAgentPortsSFPDMIRxLowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 5),
    _NmAgentPortsSFPDMIRxLowAlarmEvent_Type()
)
nmAgentPortsSFPDMIRxLowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMIRxLowAlarmEvent.setStatus("current")


class _NmAgentPortsSFPDMITxPowerAlarm_Type(Integer32):
    """Custom type nmAgentPortsSFPDMITxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("inactive", 1),
          ("active", 2),
          ("notimplemented", 255))
    )


_NmAgentPortsSFPDMITxPowerAlarm_Type.__name__ = "Integer32"
_NmAgentPortsSFPDMITxPowerAlarm_Object = MibTableColumn
nmAgentPortsSFPDMITxPowerAlarm = _NmAgentPortsSFPDMITxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 6),
    _NmAgentPortsSFPDMITxPowerAlarm_Type()
)
nmAgentPortsSFPDMITxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMITxPowerAlarm.setStatus("current")


class _NmAgentPortsSFPDMIBiasAlarmEvent_Type(Integer32):
    """Custom type nmAgentPortsSFPDMIBiasAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("inactive", 1),
          ("active", 2),
          ("notimplemented", 255))
    )


_NmAgentPortsSFPDMIBiasAlarmEvent_Type.__name__ = "Integer32"
_NmAgentPortsSFPDMIBiasAlarmEvent_Object = MibTableColumn
nmAgentPortsSFPDMIBiasAlarmEvent = _NmAgentPortsSFPDMIBiasAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 7),
    _NmAgentPortsSFPDMIBiasAlarmEvent_Type()
)
nmAgentPortsSFPDMIBiasAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMIBiasAlarmEvent.setStatus("current")


class _NmAgentPortsSFPDMIRxHighAlarmEvent_Type(Integer32):
    """Custom type nmAgentPortsSFPDMIRxHighAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("inactive", 1),
          ("active", 2),
          ("notimplemented", 255))
    )


_NmAgentPortsSFPDMIRxHighAlarmEvent_Type.__name__ = "Integer32"
_NmAgentPortsSFPDMIRxHighAlarmEvent_Object = MibTableColumn
nmAgentPortsSFPDMIRxHighAlarmEvent = _NmAgentPortsSFPDMIRxHighAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 8),
    _NmAgentPortsSFPDMIRxHighAlarmEvent_Type()
)
nmAgentPortsSFPDMIRxHighAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDMIRxHighAlarmEvent.setStatus("current")


class _NmAgentPortsSFPDWDMTECAlarmEvent_Type(Integer32):
    """Custom type nmAgentPortsSFPDWDMTECAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("inactive", 1),
          ("active", 2),
          ("notimplemented", 255))
    )


_NmAgentPortsSFPDWDMTECAlarmEvent_Type.__name__ = "Integer32"
_NmAgentPortsSFPDWDMTECAlarmEvent_Object = MibTableColumn
nmAgentPortsSFPDWDMTECAlarmEvent = _NmAgentPortsSFPDWDMTECAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 9),
    _NmAgentPortsSFPDWDMTECAlarmEvent_Type()
)
nmAgentPortsSFPDWDMTECAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPDWDMTECAlarmEvent.setStatus("current")


class _NmAgentPortsSFPTempAlarmEvent_Type(Integer32):
    """Custom type nmAgentPortsSFPTempAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("inactive", 1),
          ("active", 2),
          ("notimplemented", 255))
    )


_NmAgentPortsSFPTempAlarmEvent_Type.__name__ = "Integer32"
_NmAgentPortsSFPTempAlarmEvent_Object = MibTableColumn
nmAgentPortsSFPTempAlarmEvent = _NmAgentPortsSFPTempAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 1, 3, 4, 1, 10),
    _NmAgentPortsSFPTempAlarmEvent_Type()
)
nmAgentPortsSFPTempAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmAgentPortsSFPTempAlarmEvent.setStatus("current")
_NmCarrier_ObjectIdentity = ObjectIdentity
nmCarrier = _NmCarrier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2)
)
_NmCarrierGerneralInfo_ObjectIdentity = ObjectIdentity
nmCarrierGerneralInfo = _NmCarrierGerneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1)
)


class _NmCarrierName_Type(DisplayString):
    """Custom type nmCarrierName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NmCarrierName_Type.__name__ = "DisplayString"
_NmCarrierName_Object = MibScalar
nmCarrierName = _NmCarrierName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 1),
    _NmCarrierName_Type()
)
nmCarrierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierName.setStatus("current")


class _NmCarrierType_Type(Integer32):
    """Custom type nmCarrierType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("carrier4U", 1),
          ("carrier1U", 2),
          ("carrier45U", 3),
          ("carrier5U", 4),
          ("carrier5UHighPower", 5))
    )


_NmCarrierType_Type.__name__ = "Integer32"
_NmCarrierType_Object = MibScalar
nmCarrierType = _NmCarrierType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 2),
    _NmCarrierType_Type()
)
nmCarrierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierType.setStatus("current")


class _NmPSU1Status_Type(Integer32):
    """Custom type nmPSU1Status based on Integer32"""
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
        *(("notInstalled", 0),
          ("fail", 1),
          ("temperatureWarning", 2),
          ("pass", 3))
    )


_NmPSU1Status_Type.__name__ = "Integer32"
_NmPSU1Status_Object = MibScalar
nmPSU1Status = _NmPSU1Status_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 3),
    _NmPSU1Status_Type()
)
nmPSU1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmPSU1Status.setStatus("current")


class _NmPSU2Status_Type(Integer32):
    """Custom type nmPSU2Status based on Integer32"""
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
        *(("notInstalled", 0),
          ("fail", 1),
          ("temperatureWarning", 2),
          ("pass", 3))
    )


_NmPSU2Status_Type.__name__ = "Integer32"
_NmPSU2Status_Object = MibScalar
nmPSU2Status = _NmPSU2Status_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 4),
    _NmPSU2Status_Type()
)
nmPSU2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmPSU2Status.setStatus("current")


class _NmFanState_Type(Integer32):
    """Custom type nmFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("pass", 3),
          ("fail", 4),
          ("notInstalled", 5))
    )


_NmFanState_Type.__name__ = "Integer32"
_NmFanState_Object = MibScalar
nmFanState = _NmFanState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 5),
    _NmFanState_Type()
)
nmFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFanState.setStatus("current")


class _NmCarrierPSU1Type_Type(Integer32):
    """Custom type nmCarrierPSU1Type based on Integer32"""
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
              8,
              9,
              10,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 0),
          ("psu230VAC75W", 1),
          ("psu230VAC160W", 2),
          ("psu48VDC75W", 3),
          ("psu48VDC150W", 4),
          ("psu48VDC60W", 5),
          ("psu230VAC60W", 6),
          ("psu48VDC250W", 7),
          ("psu230VAC250W", 8),
          ("psu48VDC1100W", 9),
          ("psu230VAC1100W", 10),
          ("notAvailable", 255))
    )


_NmCarrierPSU1Type_Type.__name__ = "Integer32"
_NmCarrierPSU1Type_Object = MibScalar
nmCarrierPSU1Type = _NmCarrierPSU1Type_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 6),
    _NmCarrierPSU1Type_Type()
)
nmCarrierPSU1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierPSU1Type.setStatus("current")


class _NmCarrierPSU2Type_Type(Integer32):
    """Custom type nmCarrierPSU2Type based on Integer32"""
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
              8,
              9,
              10,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 0),
          ("psu230VAC75W", 1),
          ("psu230VAC160W", 2),
          ("psu48VDC75W", 3),
          ("psu48VDC150W", 4),
          ("psu48VDC60W", 5),
          ("psu230VAC60W", 6),
          ("psu48VDC250W", 7),
          ("psu230VAC250W", 8),
          ("psu48VDC1100W", 9),
          ("psu230VAC1100W", 10),
          ("notAvailable", 255))
    )


_NmCarrierPSU2Type_Type.__name__ = "Integer32"
_NmCarrierPSU2Type_Object = MibScalar
nmCarrierPSU2Type = _NmCarrierPSU2Type_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 7),
    _NmCarrierPSU2Type_Type()
)
nmCarrierPSU2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierPSU2Type.setStatus("current")


class _NmCarrierPSU1Text_Type(DisplayString):
    """Custom type nmCarrierPSU1Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierPSU1Text_Type.__name__ = "DisplayString"
_NmCarrierPSU1Text_Object = MibScalar
nmCarrierPSU1Text = _NmCarrierPSU1Text_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 8),
    _NmCarrierPSU1Text_Type()
)
nmCarrierPSU1Text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierPSU1Text.setStatus("current")


class _NmCarrierPSU2Text_Type(DisplayString):
    """Custom type nmCarrierPSU2Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierPSU2Text_Type.__name__ = "DisplayString"
_NmCarrierPSU2Text_Object = MibScalar
nmCarrierPSU2Text = _NmCarrierPSU2Text_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 9),
    _NmCarrierPSU2Text_Type()
)
nmCarrierPSU2Text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierPSU2Text.setStatus("current")


class _NmCarrierPSU3Text_Type(DisplayString):
    """Custom type nmCarrierPSU3Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierPSU3Text_Type.__name__ = "DisplayString"
_NmCarrierPSU3Text_Object = MibScalar
nmCarrierPSU3Text = _NmCarrierPSU3Text_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 10),
    _NmCarrierPSU3Text_Type()
)
nmCarrierPSU3Text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierPSU3Text.setStatus("current")


class _NmCarrierPSU3Type_Type(Integer32):
    """Custom type nmCarrierPSU3Type based on Integer32"""
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
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 0),
          ("psu230VAC75W", 1),
          ("psu230VAC160W", 2),
          ("psu48VDC75W", 3),
          ("psu48VDC150W", 4),
          ("psu48VDC60W", 5),
          ("psu230VAC60W", 6),
          ("psu48VDC250W", 7),
          ("psu230VAC250W", 8),
          ("notAvailable", 255))
    )


_NmCarrierPSU3Type_Type.__name__ = "Integer32"
_NmCarrierPSU3Type_Object = MibScalar
nmCarrierPSU3Type = _NmCarrierPSU3Type_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 11),
    _NmCarrierPSU3Type_Type()
)
nmCarrierPSU3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierPSU3Type.setStatus("current")


class _NmPSU3Status_Type(Integer32):
    """Custom type nmPSU3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 0),
          ("fail", 1),
          ("temperatureWarning", 2),
          ("pass", 3),
          ("notAvailable", 255))
    )


_NmPSU3Status_Type.__name__ = "Integer32"
_NmPSU3Status_Object = MibScalar
nmPSU3Status = _NmPSU3Status_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 12),
    _NmPSU3Status_Type()
)
nmPSU3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmPSU3Status.setStatus("current")


class _NmCarrierSerialNumber_Type(DisplayString):
    """Custom type nmCarrierSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NmCarrierSerialNumber_Type.__name__ = "DisplayString"
_NmCarrierSerialNumber_Object = MibScalar
nmCarrierSerialNumber = _NmCarrierSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 13),
    _NmCarrierSerialNumber_Type()
)
nmCarrierSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierSerialNumber.setStatus("current")


class _NmCarrierAssemblyAlarm_Type(Integer32):
    """Custom type nmCarrierAssemblyAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_NmCarrierAssemblyAlarm_Type.__name__ = "Integer32"
_NmCarrierAssemblyAlarm_Object = MibScalar
nmCarrierAssemblyAlarm = _NmCarrierAssemblyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 1, 14),
    _NmCarrierAssemblyAlarm_Type()
)
nmCarrierAssemblyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierAssemblyAlarm.setStatus("current")
_NmCarrierSlotOverviewTable_Object = MibTable
nmCarrierSlotOverviewTable = _NmCarrierSlotOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 2)
)
if mibBuilder.loadTexts:
    nmCarrierSlotOverviewTable.setStatus("current")
_NmCarrierSlotOverviewEntry_Object = MibTableRow
nmCarrierSlotOverviewEntry = _NmCarrierSlotOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 2, 1)
)
nmCarrierSlotOverviewEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmCarrierSlotNumber"),
)
if mibBuilder.loadTexts:
    nmCarrierSlotOverviewEntry.setStatus("current")


class _NmCarrierSlotNumber_Type(Integer32):
    """Custom type nmCarrierSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_NmCarrierSlotNumber_Type.__name__ = "Integer32"
_NmCarrierSlotNumber_Object = MibTableColumn
nmCarrierSlotNumber = _NmCarrierSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 2, 1, 1),
    _NmCarrierSlotNumber_Type()
)
nmCarrierSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierSlotNumber.setStatus("current")


class _NmCarrierSlotType_Type(DisplayString):
    """Custom type nmCarrierSlotType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierSlotType_Type.__name__ = "DisplayString"
_NmCarrierSlotType_Object = MibTableColumn
nmCarrierSlotType = _NmCarrierSlotType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 2, 1, 2),
    _NmCarrierSlotType_Type()
)
nmCarrierSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierSlotType.setStatus("current")


class _NmCarrierSlotPassiveText_Type(DisplayString):
    """Custom type nmCarrierSlotPassiveText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierSlotPassiveText_Type.__name__ = "DisplayString"
_NmCarrierSlotPassiveText_Object = MibTableColumn
nmCarrierSlotPassiveText = _NmCarrierSlotPassiveText_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 2, 1, 3),
    _NmCarrierSlotPassiveText_Type()
)
nmCarrierSlotPassiveText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierSlotPassiveText.setStatus("current")
_NmFanOverviewTable_Object = MibTable
nmFanOverviewTable = _NmFanOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 3)
)
if mibBuilder.loadTexts:
    nmFanOverviewTable.setStatus("current")
_NmFanOverviewEntry_Object = MibTableRow
nmFanOverviewEntry = _NmFanOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 3, 1)
)
nmFanOverviewEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmFanGroupNumber"),
)
if mibBuilder.loadTexts:
    nmFanOverviewEntry.setStatus("current")


class _NmFanGroupNumber_Type(Integer32):
    """Custom type nmFanGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NmFanGroupNumber_Type.__name__ = "Integer32"
_NmFanGroupNumber_Object = MibTableColumn
nmFanGroupNumber = _NmFanGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 3, 1, 1),
    _NmFanGroupNumber_Type()
)
nmFanGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFanGroupNumber.setStatus("current")


class _NmFanGroupStatus_Type(Integer32):
    """Custom type nmFanGroupStatus based on Integer32"""
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
        *(("notAvailable", 0),
          ("on", 1),
          ("off", 2),
          ("pass", 3),
          ("fail", 4),
          ("notInstalled", 5),
          ("auto", 6))
    )


_NmFanGroupStatus_Type.__name__ = "Integer32"
_NmFanGroupStatus_Object = MibTableColumn
nmFanGroupStatus = _NmFanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 3, 1, 2),
    _NmFanGroupStatus_Type()
)
nmFanGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmFanGroupStatus.setStatus("current")
_NmCarrierFWUpdate_ObjectIdentity = ObjectIdentity
nmCarrierFWUpdate = _NmCarrierFWUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 4)
)


class _NmCarrierFWUpdateFilename_Type(DisplayString):
    """Custom type nmCarrierFWUpdateFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierFWUpdateFilename_Type.__name__ = "DisplayString"
_NmCarrierFWUpdateFilename_Object = MibScalar
nmCarrierFWUpdateFilename = _NmCarrierFWUpdateFilename_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 4, 1),
    _NmCarrierFWUpdateFilename_Type()
)
nmCarrierFWUpdateFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmCarrierFWUpdateFilename.setStatus("current")


class _NmCarrierFirmwareTransferConfig_Type(Integer32):
    """Custom type nmCarrierFirmwareTransferConfig based on Integer32"""
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
        *(("notAvailable", 0),
          ("idle", 1),
          ("startTransfer", 2),
          ("transferReady", 3),
          ("transferActive", 4),
          ("transferFailure", 5),
          ("abortTransfer", 6))
    )


_NmCarrierFirmwareTransferConfig_Type.__name__ = "Integer32"
_NmCarrierFirmwareTransferConfig_Object = MibScalar
nmCarrierFirmwareTransferConfig = _NmCarrierFirmwareTransferConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 4, 2),
    _NmCarrierFirmwareTransferConfig_Type()
)
nmCarrierFirmwareTransferConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmCarrierFirmwareTransferConfig.setStatus("current")
_NmCarrierFWTransferProgress_Type = Integer32
_NmCarrierFWTransferProgress_Object = MibScalar
nmCarrierFWTransferProgress = _NmCarrierFWTransferProgress_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 4, 3),
    _NmCarrierFWTransferProgress_Type()
)
nmCarrierFWTransferProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierFWTransferProgress.setStatus("current")


class _NmCarrierFWUpdateConfig_Type(Integer32):
    """Custom type nmCarrierFWUpdateConfig based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("idle", 1),
          ("updateRunning", 2),
          ("updateReady", 3),
          ("copyToFlash", 4),
          ("copyToFlashAndRestart", 5),
          ("restartOnly", 6),
          ("updateFailure", 7))
    )


_NmCarrierFWUpdateConfig_Type.__name__ = "Integer32"
_NmCarrierFWUpdateConfig_Object = MibScalar
nmCarrierFWUpdateConfig = _NmCarrierFWUpdateConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 4, 4),
    _NmCarrierFWUpdateConfig_Type()
)
nmCarrierFWUpdateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmCarrierFWUpdateConfig.setStatus("current")
_NmCarrierFWUpdatePolicyTable_Object = MibTable
nmCarrierFWUpdatePolicyTable = _NmCarrierFWUpdatePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 5)
)
if mibBuilder.loadTexts:
    nmCarrierFWUpdatePolicyTable.setStatus("current")
_NmCarrierFWUpdatePolicyEntry_Object = MibTableRow
nmCarrierFWUpdatePolicyEntry = _NmCarrierFWUpdatePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 5, 1)
)
nmCarrierFWUpdatePolicyEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmCarrierFWUpdatePolicySlot"),
)
if mibBuilder.loadTexts:
    nmCarrierFWUpdatePolicyEntry.setStatus("current")


class _NmCarrierFWUpdatePolicySlot_Type(Integer32):
    """Custom type nmCarrierFWUpdatePolicySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_NmCarrierFWUpdatePolicySlot_Type.__name__ = "Integer32"
_NmCarrierFWUpdatePolicySlot_Object = MibTableColumn
nmCarrierFWUpdatePolicySlot = _NmCarrierFWUpdatePolicySlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 5, 1, 1),
    _NmCarrierFWUpdatePolicySlot_Type()
)
nmCarrierFWUpdatePolicySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierFWUpdatePolicySlot.setStatus("current")
_NmCarrierFWUpdatePolicyCardName_Type = DisplayString
_NmCarrierFWUpdatePolicyCardName_Object = MibTableColumn
nmCarrierFWUpdatePolicyCardName = _NmCarrierFWUpdatePolicyCardName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 5, 1, 2),
    _NmCarrierFWUpdatePolicyCardName_Type()
)
nmCarrierFWUpdatePolicyCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierFWUpdatePolicyCardName.setStatus("current")


class _NmCarrierFWUpdatePolicyConfig_Type(Integer32):
    """Custom type nmCarrierFWUpdatePolicyConfig based on Integer32"""
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
        *(("notAvailable", 0),
          ("updatesEnabled", 1),
          ("updatesDisabled", 2),
          ("notApplicable", 3))
    )


_NmCarrierFWUpdatePolicyConfig_Type.__name__ = "Integer32"
_NmCarrierFWUpdatePolicyConfig_Object = MibTableColumn
nmCarrierFWUpdatePolicyConfig = _NmCarrierFWUpdatePolicyConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 5, 1, 3),
    _NmCarrierFWUpdatePolicyConfig_Type()
)
nmCarrierFWUpdatePolicyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmCarrierFWUpdatePolicyConfig.setStatus("current")


class _NmCarrierFWUpdatePolicyTransferState_Type(Integer32):
    """Custom type nmCarrierFWUpdatePolicyTransferState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("idle", 1),
          ("running", 2),
          ("ready", 3),
          ("fail", 7))
    )


_NmCarrierFWUpdatePolicyTransferState_Type.__name__ = "Integer32"
_NmCarrierFWUpdatePolicyTransferState_Object = MibTableColumn
nmCarrierFWUpdatePolicyTransferState = _NmCarrierFWUpdatePolicyTransferState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 5, 1, 4),
    _NmCarrierFWUpdatePolicyTransferState_Type()
)
nmCarrierFWUpdatePolicyTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierFWUpdatePolicyTransferState.setStatus("current")
_NmCarrierConfigTransferTable_Object = MibTable
nmCarrierConfigTransferTable = _NmCarrierConfigTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 6)
)
if mibBuilder.loadTexts:
    nmCarrierConfigTransferTable.setStatus("current")
_NmCarrierConfigTransferEntry_Object = MibTableRow
nmCarrierConfigTransferEntry = _NmCarrierConfigTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 6, 1)
)
nmCarrierConfigTransferEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmCarrierConfigSlot"),
)
if mibBuilder.loadTexts:
    nmCarrierConfigTransferEntry.setStatus("current")


class _NmCarrierConfigSlot_Type(Integer32):
    """Custom type nmCarrierConfigSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_NmCarrierConfigSlot_Type.__name__ = "Integer32"
_NmCarrierConfigSlot_Object = MibTableColumn
nmCarrierConfigSlot = _NmCarrierConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 6, 1, 1),
    _NmCarrierConfigSlot_Type()
)
nmCarrierConfigSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierConfigSlot.setStatus("current")


class _NmCarrierConfigModuleName_Type(DisplayString):
    """Custom type nmCarrierConfigModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierConfigModuleName_Type.__name__ = "DisplayString"
_NmCarrierConfigModuleName_Object = MibTableColumn
nmCarrierConfigModuleName = _NmCarrierConfigModuleName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 6, 1, 2),
    _NmCarrierConfigModuleName_Type()
)
nmCarrierConfigModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierConfigModuleName.setStatus("current")


class _NmCarrierConfigTransferState_Type(Integer32):
    """Custom type nmCarrierConfigTransferState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("upToDate", 1),
          ("fileUpdateScheduled", 2),
          ("updating", 3),
          ("invalidConfigFile", 4),
          ("error", 5))
    )


_NmCarrierConfigTransferState_Type.__name__ = "Integer32"
_NmCarrierConfigTransferState_Object = MibTableColumn
nmCarrierConfigTransferState = _NmCarrierConfigTransferState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 6, 1, 3),
    _NmCarrierConfigTransferState_Type()
)
nmCarrierConfigTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierConfigTransferState.setStatus("current")


class _NmCarrierConfigTransfer_Type(Integer32):
    """Custom type nmCarrierConfigTransfer based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("idle", 1),
          ("pushToSlot", 2),
          ("updateFromSlot", 3),
          ("transferReady", 4),
          ("transferRunning", 5),
          ("transferERROR", 6),
          ("abortTransfer", 7))
    )


_NmCarrierConfigTransfer_Type.__name__ = "Integer32"
_NmCarrierConfigTransfer_Object = MibTableColumn
nmCarrierConfigTransfer = _NmCarrierConfigTransfer_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 6, 1, 4),
    _NmCarrierConfigTransfer_Type()
)
nmCarrierConfigTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmCarrierConfigTransfer.setStatus("current")


class _NmCarrierConfigFilename_Type(DisplayString):
    """Custom type nmCarrierConfigFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NmCarrierConfigFilename_Type.__name__ = "DisplayString"
_NmCarrierConfigFilename_Object = MibTableColumn
nmCarrierConfigFilename = _NmCarrierConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 6, 1, 5),
    _NmCarrierConfigFilename_Type()
)
nmCarrierConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmCarrierConfigFilename.setStatus("current")


class _NmCarrierConfigActivation_Type(Integer32):
    """Custom type nmCarrierConfigActivation based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("idle", 1),
          ("activating", 2),
          ("ready", 3),
          ("copyToFlash", 4),
          ("copyToFlashAndRestart", 5),
          ("restartOnly", 6),
          ("failure", 7))
    )


_NmCarrierConfigActivation_Type.__name__ = "Integer32"
_NmCarrierConfigActivation_Object = MibTableColumn
nmCarrierConfigActivation = _NmCarrierConfigActivation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 6, 1, 6),
    _NmCarrierConfigActivation_Type()
)
nmCarrierConfigActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmCarrierConfigActivation.setStatus("current")
_NmCarrierInventoryTable_Object = MibTable
nmCarrierInventoryTable = _NmCarrierInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7)
)
if mibBuilder.loadTexts:
    nmCarrierInventoryTable.setStatus("current")
_NmCarrierInventoryEntry_Object = MibTableRow
nmCarrierInventoryEntry = _NmCarrierInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7, 1)
)
nmCarrierInventoryEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "nmCarrierInventoryIndex"),
)
if mibBuilder.loadTexts:
    nmCarrierInventoryEntry.setStatus("current")


class _NmCarrierInventoryIndex_Type(Integer32):
    """Custom type nmCarrierInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18000),
    )


_NmCarrierInventoryIndex_Type.__name__ = "Integer32"
_NmCarrierInventoryIndex_Object = MibTableColumn
nmCarrierInventoryIndex = _NmCarrierInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7, 1, 1),
    _NmCarrierInventoryIndex_Type()
)
nmCarrierInventoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmCarrierInventoryIndex.setStatus("current")


class _NmCarrierInventorySlotNumber_Type(Integer32):
    """Custom type nmCarrierInventorySlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_NmCarrierInventorySlotNumber_Type.__name__ = "Integer32"
_NmCarrierInventorySlotNumber_Object = MibTableColumn
nmCarrierInventorySlotNumber = _NmCarrierInventorySlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7, 1, 2),
    _NmCarrierInventorySlotNumber_Type()
)
nmCarrierInventorySlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierInventorySlotNumber.setStatus("current")


class _NmCarrierInventoryPort_Type(DisplayString):
    """Custom type nmCarrierInventoryPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierInventoryPort_Type.__name__ = "DisplayString"
_NmCarrierInventoryPort_Object = MibTableColumn
nmCarrierInventoryPort = _NmCarrierInventoryPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7, 1, 3),
    _NmCarrierInventoryPort_Type()
)
nmCarrierInventoryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierInventoryPort.setStatus("current")


class _NmCarrierInventoryModuleName_Type(DisplayString):
    """Custom type nmCarrierInventoryModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NmCarrierInventoryModuleName_Type.__name__ = "DisplayString"
_NmCarrierInventoryModuleName_Object = MibTableColumn
nmCarrierInventoryModuleName = _NmCarrierInventoryModuleName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7, 1, 4),
    _NmCarrierInventoryModuleName_Type()
)
nmCarrierInventoryModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierInventoryModuleName.setStatus("current")


class _NmCarrierInventoryPartNumber_Type(DisplayString):
    """Custom type nmCarrierInventoryPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierInventoryPartNumber_Type.__name__ = "DisplayString"
_NmCarrierInventoryPartNumber_Object = MibTableColumn
nmCarrierInventoryPartNumber = _NmCarrierInventoryPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7, 1, 5),
    _NmCarrierInventoryPartNumber_Type()
)
nmCarrierInventoryPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierInventoryPartNumber.setStatus("current")


class _NmCarrierInventorySerialNumber_Type(DisplayString):
    """Custom type nmCarrierInventorySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierInventorySerialNumber_Type.__name__ = "DisplayString"
_NmCarrierInventorySerialNumber_Object = MibTableColumn
nmCarrierInventorySerialNumber = _NmCarrierInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7, 1, 6),
    _NmCarrierInventorySerialNumber_Type()
)
nmCarrierInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierInventorySerialNumber.setStatus("current")


class _NmCarrierInventoryFirmwareRelease_Type(DisplayString):
    """Custom type nmCarrierInventoryFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierInventoryFirmwareRelease_Type.__name__ = "DisplayString"
_NmCarrierInventoryFirmwareRelease_Object = MibTableColumn
nmCarrierInventoryFirmwareRelease = _NmCarrierInventoryFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7, 1, 7),
    _NmCarrierInventoryFirmwareRelease_Type()
)
nmCarrierInventoryFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierInventoryFirmwareRelease.setStatus("current")


class _NmCarrierInventoryKernelLoader_Type(DisplayString):
    """Custom type nmCarrierInventoryKernelLoader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmCarrierInventoryKernelLoader_Type.__name__ = "DisplayString"
_NmCarrierInventoryKernelLoader_Object = MibTableColumn
nmCarrierInventoryKernelLoader = _NmCarrierInventoryKernelLoader_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 2, 7, 1, 8),
    _NmCarrierInventoryKernelLoader_Type()
)
nmCarrierInventoryKernelLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmCarrierInventoryKernelLoader.setStatus("current")
_Converter_ObjectIdentity = ObjectIdentity
converter = _Converter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3)
)
_ConvSPEEDDUALLINE_ObjectIdentity = ObjectIdentity
convSPEEDDUALLINE = _ConvSPEEDDUALLINE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1)
)
_ConvSxLModuleOverviewTable_Object = MibTable
convSxLModuleOverviewTable = _ConvSxLModuleOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    convSxLModuleOverviewTable.setStatus("current")
_ConvSxLModuleOverviewEntry_Object = MibTableRow
convSxLModuleOverviewEntry = _ConvSxLModuleOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1)
)
convSxLModuleOverviewEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLMSlot"),
)
if mibBuilder.loadTexts:
    convSxLModuleOverviewEntry.setStatus("current")


class _ConvSxLMSlot_Type(Integer32):
    """Custom type convSxLMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLMSlot_Type.__name__ = "Integer32"
_ConvSxLMSlot_Object = MibTableColumn
convSxLMSlot = _ConvSxLMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 2),
    _ConvSxLMSlot_Type()
)
convSxLMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMSlot.setStatus("current")


class _ConvSxLMDevice_Type(Integer32):
    """Custom type convSxLMDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("devSPEEDSINGLELINE", 0),
          ("devSPEEDDUALLINE", 1),
          ("devSPEEDDUALLINE3R", 2),
          ("devSPEEDPROTECT3R", 3),
          ("devunknown", 255))
    )


_ConvSxLMDevice_Type.__name__ = "Integer32"
_ConvSxLMDevice_Object = MibTableColumn
convSxLMDevice = _ConvSxLMDevice_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 3),
    _ConvSxLMDevice_Type()
)
convSxLMDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMDevice.setStatus("current")


class _ConvSxLMStatus_Type(Integer32):
    """Custom type convSxLMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("resetHardware", 1),
          ("resetConfig", 2),
          ("resetCAN", 3),
          ("resetSoftware", 4),
          ("unknown", 255))
    )


_ConvSxLMStatus_Type.__name__ = "Integer32"
_ConvSxLMStatus_Object = MibTableColumn
convSxLMStatus = _ConvSxLMStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 4),
    _ConvSxLMStatus_Type()
)
convSxLMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLMStatus.setStatus("current")
_ConvSxLMSysUpTime_Type = TimeTicks
_ConvSxLMSysUpTime_Object = MibTableColumn
convSxLMSysUpTime = _ConvSxLMSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 5),
    _ConvSxLMSysUpTime_Type()
)
convSxLMSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMSysUpTime.setStatus("current")
_ConvSxLMTemp_Type = Integer32
_ConvSxLMTemp_Object = MibTableColumn
convSxLMTemp = _ConvSxLMTemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 6),
    _ConvSxLMTemp_Type()
)
convSxLMTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMTemp.setStatus("current")


class _ConvSxLMAlarmState_Type(Integer32):
    """Custom type convSxLMAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeAlarms", 1),
          ("unknown", 255))
    )


_ConvSxLMAlarmState_Type.__name__ = "Integer32"
_ConvSxLMAlarmState_Object = MibTableColumn
convSxLMAlarmState = _ConvSxLMAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 7),
    _ConvSxLMAlarmState_Type()
)
convSxLMAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMAlarmState.setStatus("current")


class _ConvSxLMBootSWVersion_Type(DisplayString):
    """Custom type convSxLMBootSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ConvSxLMBootSWVersion_Type.__name__ = "DisplayString"
_ConvSxLMBootSWVersion_Object = MibTableColumn
convSxLMBootSWVersion = _ConvSxLMBootSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 8),
    _ConvSxLMBootSWVersion_Type()
)
convSxLMBootSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMBootSWVersion.setStatus("current")


class _ConvSxLMAppSWVersion_Type(DisplayString):
    """Custom type convSxLMAppSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ConvSxLMAppSWVersion_Type.__name__ = "DisplayString"
_ConvSxLMAppSWVersion_Object = MibTableColumn
convSxLMAppSWVersion = _ConvSxLMAppSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 9),
    _ConvSxLMAppSWVersion_Type()
)
convSxLMAppSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMAppSWVersion.setStatus("current")


class _ConvSxLMHWVersion_Type(DisplayString):
    """Custom type convSxLMHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ConvSxLMHWVersion_Type.__name__ = "DisplayString"
_ConvSxLMHWVersion_Object = MibTableColumn
convSxLMHWVersion = _ConvSxLMHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 10),
    _ConvSxLMHWVersion_Type()
)
convSxLMHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMHWVersion.setStatus("current")


class _ConvSxLMPLDVersion_Type(DisplayString):
    """Custom type convSxLMPLDVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ConvSxLMPLDVersion_Type.__name__ = "DisplayString"
_ConvSxLMPLDVersion_Object = MibTableColumn
convSxLMPLDVersion = _ConvSxLMPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 11),
    _ConvSxLMPLDVersion_Type()
)
convSxLMPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMPLDVersion.setStatus("current")


class _ConvSxLMSerialNumber_Type(DisplayString):
    """Custom type convSxLMSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLMSerialNumber_Type.__name__ = "DisplayString"
_ConvSxLMSerialNumber_Object = MibTableColumn
convSxLMSerialNumber = _ConvSxLMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 1, 1, 12),
    _ConvSxLMSerialNumber_Type()
)
convSxLMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMSerialNumber.setStatus("current")
_ConvSxLSWImagesOverviewTable_Object = MibTable
convSxLSWImagesOverviewTable = _ConvSxLSWImagesOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    convSxLSWImagesOverviewTable.setStatus("current")
_ConvSxLSWImagesOverviewEntry_Object = MibTableRow
convSxLSWImagesOverviewEntry = _ConvSxLSWImagesOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 2, 1)
)
convSxLSWImagesOverviewEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSWSlot"),
)
if mibBuilder.loadTexts:
    convSxLSWImagesOverviewEntry.setStatus("current")


class _ConvSxLSWSlot_Type(Integer32):
    """Custom type convSxLSWSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSWSlot_Type.__name__ = "Integer32"
_ConvSxLSWSlot_Object = MibTableColumn
convSxLSWSlot = _ConvSxLSWSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 2, 1, 2),
    _ConvSxLSWSlot_Type()
)
convSxLSWSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSWSlot.setStatus("current")


class _ConvSxLSWBootImage_Type(DisplayString):
    """Custom type convSxLSWBootImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_ConvSxLSWBootImage_Type.__name__ = "DisplayString"
_ConvSxLSWBootImage_Object = MibTableColumn
convSxLSWBootImage = _ConvSxLSWBootImage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 2, 1, 3),
    _ConvSxLSWBootImage_Type()
)
convSxLSWBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSWBootImage.setStatus("current")


class _ConvSxLSWAppImage1_Type(DisplayString):
    """Custom type convSxLSWAppImage1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_ConvSxLSWAppImage1_Type.__name__ = "DisplayString"
_ConvSxLSWAppImage1_Object = MibTableColumn
convSxLSWAppImage1 = _ConvSxLSWAppImage1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 2, 1, 4),
    _ConvSxLSWAppImage1_Type()
)
convSxLSWAppImage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSWAppImage1.setStatus("current")


class _ConvSxLSWAppImage2_Type(DisplayString):
    """Custom type convSxLSWAppImage2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_ConvSxLSWAppImage2_Type.__name__ = "DisplayString"
_ConvSxLSWAppImage2_Object = MibTableColumn
convSxLSWAppImage2 = _ConvSxLSWAppImage2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 2, 1, 5),
    _ConvSxLSWAppImage2_Type()
)
convSxLSWAppImage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSWAppImage2.setStatus("current")


class _ConvSxLSWUploadStatus_Type(Integer32):
    """Custom type convSxLSWUploadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("startUpload", 1),
          ("uploadActive", 2),
          ("uploadFailure", 255))
    )


_ConvSxLSWUploadStatus_Type.__name__ = "Integer32"
_ConvSxLSWUploadStatus_Object = MibTableColumn
convSxLSWUploadStatus = _ConvSxLSWUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 2, 1, 6),
    _ConvSxLSWUploadStatus_Type()
)
convSxLSWUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSWUploadStatus.setStatus("current")


class _ConvSxLSWUpdateStatus_Type(Integer32):
    """Custom type convSxLSWUpdateStatus based on Integer32"""
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
        *(("idle", 0),
          ("activateImage1", 1),
          ("activateImage2", 2),
          ("invalidImages", 3))
    )


_ConvSxLSWUpdateStatus_Type.__name__ = "Integer32"
_ConvSxLSWUpdateStatus_Object = MibTableColumn
convSxLSWUpdateStatus = _ConvSxLSWUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 2, 1, 7),
    _ConvSxLSWUpdateStatus_Type()
)
convSxLSWUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSWUpdateStatus.setStatus("current")
_ConvSxLModuleConfigTable_Object = MibTable
convSxLModuleConfigTable = _ConvSxLModuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    convSxLModuleConfigTable.setStatus("current")
_ConvSxLModuleConfigEntry_Object = MibTableRow
convSxLModuleConfigEntry = _ConvSxLModuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1)
)
convSxLModuleConfigEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLMCSlot"),
)
if mibBuilder.loadTexts:
    convSxLModuleConfigEntry.setStatus("current")


class _ConvSxLMCSlot_Type(Integer32):
    """Custom type convSxLMCSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLMCSlot_Type.__name__ = "Integer32"
_ConvSxLMCSlot_Object = MibTableColumn
convSxLMCSlot = _ConvSxLMCSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 2),
    _ConvSxLMCSlot_Type()
)
convSxLMCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMCSlot.setStatus("current")
_ConvSxLMIpAddress_Type = IpAddress
_ConvSxLMIpAddress_Object = MibTableColumn
convSxLMIpAddress = _ConvSxLMIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 3),
    _ConvSxLMIpAddress_Type()
)
convSxLMIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMIpAddress.setStatus("current")
_ConvSxLMIpNetmask_Type = IpAddress
_ConvSxLMIpNetmask_Object = MibTableColumn
convSxLMIpNetmask = _ConvSxLMIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 4),
    _ConvSxLMIpNetmask_Type()
)
convSxLMIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMIpNetmask.setStatus("current")
_ConvSxLMIpGateway_Type = IpAddress
_ConvSxLMIpGateway_Object = MibTableColumn
convSxLMIpGateway = _ConvSxLMIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 5),
    _ConvSxLMIpGateway_Type()
)
convSxLMIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMIpGateway.setStatus("current")
_ConvSxLMIpTftpServer_Type = IpAddress
_ConvSxLMIpTftpServer_Object = MibTableColumn
convSxLMIpTftpServer = _ConvSxLMIpTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 6),
    _ConvSxLMIpTftpServer_Type()
)
convSxLMIpTftpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMIpTftpServer.setStatus("current")
_ConvSxLMIpTrapSink_Type = IpAddress
_ConvSxLMIpTrapSink_Object = MibTableColumn
convSxLMIpTrapSink = _ConvSxLMIpTrapSink_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 7),
    _ConvSxLMIpTrapSink_Type()
)
convSxLMIpTrapSink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMIpTrapSink.setStatus("current")


class _ConvSxLMSNMPReadCommunity_Type(DisplayString):
    """Custom type convSxLMSNMPReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLMSNMPReadCommunity_Type.__name__ = "DisplayString"
_ConvSxLMSNMPReadCommunity_Object = MibTableColumn
convSxLMSNMPReadCommunity = _ConvSxLMSNMPReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 8),
    _ConvSxLMSNMPReadCommunity_Type()
)
convSxLMSNMPReadCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMSNMPReadCommunity.setStatus("current")


class _ConvSxLMSNMPWriteCommunity_Type(DisplayString):
    """Custom type convSxLMSNMPWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLMSNMPWriteCommunity_Type.__name__ = "DisplayString"
_ConvSxLMSNMPWriteCommunity_Object = MibTableColumn
convSxLMSNMPWriteCommunity = _ConvSxLMSNMPWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 9),
    _ConvSxLMSNMPWriteCommunity_Type()
)
convSxLMSNMPWriteCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMSNMPWriteCommunity.setStatus("current")


class _ConvSxLMTempWarningLevel_Type(Integer32):
    """Custom type convSxLMTempWarningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ConvSxLMTempWarningLevel_Type.__name__ = "Integer32"
_ConvSxLMTempWarningLevel_Object = MibTableColumn
convSxLMTempWarningLevel = _ConvSxLMTempWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 10),
    _ConvSxLMTempWarningLevel_Type()
)
convSxLMTempWarningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLMTempWarningLevel.setStatus("current")
_ConvSxLMTempAlarmLevel_Type = Integer32
_ConvSxLMTempAlarmLevel_Object = MibTableColumn
convSxLMTempAlarmLevel = _ConvSxLMTempAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 11),
    _ConvSxLMTempAlarmLevel_Type()
)
convSxLMTempAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMTempAlarmLevel.setStatus("current")


class _ConvSxLMAlarmReport_Type(Integer32):
    """Custom type convSxLMAlarmReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("toNMA", 1),
          ("toETH", 2),
          ("toNMAandETH", 3),
          ("notavailable", 255))
    )


_ConvSxLMAlarmReport_Type.__name__ = "Integer32"
_ConvSxLMAlarmReport_Object = MibTableColumn
convSxLMAlarmReport = _ConvSxLMAlarmReport_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 12),
    _ConvSxLMAlarmReport_Type()
)
convSxLMAlarmReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMAlarmReport.setStatus("current")


class _ConvSxLMEthPortConfig_Type(Integer32):
    """Custom type convSxLMEthPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("portDown", 1),
          ("portUp", 2),
          ("notavailable", 255))
    )


_ConvSxLMEthPortConfig_Type.__name__ = "Integer32"
_ConvSxLMEthPortConfig_Object = MibTableColumn
convSxLMEthPortConfig = _ConvSxLMEthPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 13),
    _ConvSxLMEthPortConfig_Type()
)
convSxLMEthPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLMEthPortConfig.setStatus("current")


class _ConvSxLMEthPortState_Type(Integer32):
    """Custom type convSxLMEthPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("portDown", 1),
          ("portUp", 2),
          ("notavailable", 255))
    )


_ConvSxLMEthPortState_Type.__name__ = "Integer32"
_ConvSxLMEthPortState_Object = MibTableColumn
convSxLMEthPortState = _ConvSxLMEthPortState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 14),
    _ConvSxLMEthPortState_Type()
)
convSxLMEthPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMEthPortState.setStatus("current")


class _ConvSxLMCliUserTimeout_Type(Integer32):
    """Custom type convSxLMCliUserTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_ConvSxLMCliUserTimeout_Type.__name__ = "Integer32"
_ConvSxLMCliUserTimeout_Object = MibTableColumn
convSxLMCliUserTimeout = _ConvSxLMCliUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 3, 1, 15),
    _ConvSxLMCliUserTimeout_Type()
)
convSxLMCliUserTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLMCliUserTimeout.setStatus("current")
_ConvSxLModuleProtectionTable_Object = MibTable
convSxLModuleProtectionTable = _ConvSxLModuleProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    convSxLModuleProtectionTable.setStatus("current")
_ConvSxLModuleProtectionEntry_Object = MibTableRow
convSxLModuleProtectionEntry = _ConvSxLModuleProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 4, 1)
)
convSxLModuleProtectionEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLMPSlot"),
)
if mibBuilder.loadTexts:
    convSxLModuleProtectionEntry.setStatus("current")


class _ConvSxLMPSlot_Type(Integer32):
    """Custom type convSxLMPSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLMPSlot_Type.__name__ = "Integer32"
_ConvSxLMPSlot_Object = MibTableColumn
convSxLMPSlot = _ConvSxLMPSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 4, 1, 2),
    _ConvSxLMPSlot_Type()
)
convSxLMPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMPSlot.setStatus("current")


class _ConvSxLMLinkProtectionConfig_Type(Integer32):
    """Custom type convSxLMLinkProtectionConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("fallbackPort1", 1),
          ("fallbackPort2", 2),
          ("staticPort1", 3),
          ("staticPort2", 4),
          ("protectionOFF", 5),
          ("notAvailable", 255))
    )


_ConvSxLMLinkProtectionConfig_Type.__name__ = "Integer32"
_ConvSxLMLinkProtectionConfig_Object = MibTableColumn
convSxLMLinkProtectionConfig = _ConvSxLMLinkProtectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 4, 1, 3),
    _ConvSxLMLinkProtectionConfig_Type()
)
convSxLMLinkProtectionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLMLinkProtectionConfig.setStatus("current")


class _ConvSxLMLinkProtectionStatus_Type(Integer32):
    """Custom type convSxLMLinkProtectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("port1active", 1),
          ("port2active", 2),
          ("testing", 3),
          ("noneActive", 4),
          ("notAvailable", 255))
    )


_ConvSxLMLinkProtectionStatus_Type.__name__ = "Integer32"
_ConvSxLMLinkProtectionStatus_Object = MibTableColumn
convSxLMLinkProtectionStatus = _ConvSxLMLinkProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 4, 1, 4),
    _ConvSxLMLinkProtectionStatus_Type()
)
convSxLMLinkProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLMLinkProtectionStatus.setStatus("current")


class _ConvSxLMLinkProtectionFallback_Type(Integer32):
    """Custom type convSxLMLinkProtectionFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_ConvSxLMLinkProtectionFallback_Type.__name__ = "Integer32"
_ConvSxLMLinkProtectionFallback_Object = MibTableColumn
convSxLMLinkProtectionFallback = _ConvSxLMLinkProtectionFallback_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 4, 1, 5),
    _ConvSxLMLinkProtectionFallback_Type()
)
convSxLMLinkProtectionFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLMLinkProtectionFallback.setStatus("current")
_ConvSxLPortOverviewTable_Object = MibTable
convSxLPortOverviewTable = _ConvSxLPortOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    convSxLPortOverviewTable.setStatus("current")
_ConvSxLPortOverviewEntry_Object = MibTableRow
convSxLPortOverviewEntry = _ConvSxLPortOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1)
)
convSxLPortOverviewEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLPortOverviewEntry.setStatus("current")


class _ConvSxLPortIndex_Type(Integer32):
    """Custom type convSxLPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLPortIndex_Type.__name__ = "Integer32"
_ConvSxLPortIndex_Object = MibTableColumn
convSxLPortIndex = _ConvSxLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 1),
    _ConvSxLPortIndex_Type()
)
convSxLPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLPortIndex.setStatus("current")


class _ConvSxLSlot_Type(Integer32):
    """Custom type convSxLSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSlot_Type.__name__ = "Integer32"
_ConvSxLSlot_Object = MibTableColumn
convSxLSlot = _ConvSxLSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 2),
    _ConvSxLSlot_Type()
)
convSxLSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSlot.setStatus("current")
_ConvSxLPort_Type = Integer32
_ConvSxLPort_Object = MibTableColumn
convSxLPort = _ConvSxLPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 3),
    _ConvSxLPort_Type()
)
convSxLPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLPort.setStatus("current")


class _ConvSxLDescription_Type(DisplayString):
    """Custom type convSxLDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ConvSxLDescription_Type.__name__ = "DisplayString"
_ConvSxLDescription_Object = MibTableColumn
convSxLDescription = _ConvSxLDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 4),
    _ConvSxLDescription_Type()
)
convSxLDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLDescription.setStatus("current")


class _ConvSxLAdminState_Type(Integer32):
    """Custom type convSxLAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("adminUp", 1),
          ("notAvailable", 255))
    )


_ConvSxLAdminState_Type.__name__ = "Integer32"
_ConvSxLAdminState_Object = MibTableColumn
convSxLAdminState = _ConvSxLAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 5),
    _ConvSxLAdminState_Type()
)
convSxLAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLAdminState.setStatus("current")


class _ConvSxLOperState_Type(Integer32):
    """Custom type convSxLOperState based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("loop", 2),
          ("downLLCF", 3),
          ("downTxFault", 4),
          ("downRxLevel", 5),
          ("downTxLevel", 6),
          ("notAvailable", 255))
    )


_ConvSxLOperState_Type.__name__ = "Integer32"
_ConvSxLOperState_Object = MibTableColumn
convSxLOperState = _ConvSxLOperState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 6),
    _ConvSxLOperState_Type()
)
convSxLOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLOperState.setStatus("current")


class _ConvSxLSFPState_Type(Integer32):
    """Custom type convSxLSFPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sfpRemoved", 0),
          ("sfpInstalled", 1),
          ("sfpTxFault", 2),
          ("notAvailable", 255))
    )


_ConvSxLSFPState_Type.__name__ = "Integer32"
_ConvSxLSFPState_Object = MibTableColumn
convSxLSFPState = _ConvSxLSFPState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 7),
    _ConvSxLSFPState_Type()
)
convSxLSFPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPState.setStatus("current")


class _ConvSxLLLCFState_Type(Integer32):
    """Custom type convSxLLLCFState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notAvailable", 255))
    )


_ConvSxLLLCFState_Type.__name__ = "Integer32"
_ConvSxLLLCFState_Object = MibTableColumn
convSxLLLCFState = _ConvSxLLLCFState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 8),
    _ConvSxLLLCFState_Type()
)
convSxLLLCFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLLLCFState.setStatus("current")


class _ConvSxLLoopState_Type(Integer32):
    """Custom type convSxLLoopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notAvailable", 255))
    )


_ConvSxLLoopState_Type.__name__ = "Integer32"
_ConvSxLLoopState_Object = MibTableColumn
convSxLLoopState = _ConvSxLLoopState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 9),
    _ConvSxLLoopState_Type()
)
convSxLLoopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLLoopState.setStatus("current")


class _ConvSxLSpeed_Type(Integer32):
    """Custom type convSxLSpeed based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              255)
        )
    )
    namedValues = NamedValues(
        *(("speedTransparent", 0),
          ("speedSTM1-155Mbit", 1),
          ("speedSTM4-622Mbit", 2),
          ("speedSTM16-2488Mbit", 3),
          ("sSTM16FEC2666Mbit", 4),
          ("sFastEthernet125Mbit", 5),
          ("sGigabitEthernet1250Mbit", 6),
          ("sFibreChannel133Mbit", 7),
          ("sFibreChannel266Mbit", 8),
          ("sFibreChannel531Mbit", 9),
          ("sFibreChannel1062Mbit", 10),
          ("sFibreChannel2125Mbit", 11),
          ("sESCON200Mbit", 12),
          ("notAvailable", 255))
    )


_ConvSxLSpeed_Type.__name__ = "Integer32"
_ConvSxLSpeed_Object = MibTableColumn
convSxLSpeed = _ConvSxLSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 10),
    _ConvSxLSpeed_Type()
)
convSxLSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSpeed.setStatus("current")


class _ConvSxLTxPortConnection_Type(Integer32):
    """Custom type convSxLTxPortConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 0),
          ("toPort1", 1),
          ("toPort2", 2),
          ("toPort3", 3),
          ("toPort4", 4),
          ("notAvailable", 255))
    )


_ConvSxLTxPortConnection_Type.__name__ = "Integer32"
_ConvSxLTxPortConnection_Object = MibTableColumn
convSxLTxPortConnection = _ConvSxLTxPortConnection_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 11),
    _ConvSxLTxPortConnection_Type()
)
convSxLTxPortConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLTxPortConnection.setStatus("current")


class _ConvSxLAlarmState_Type(Integer32):
    """Custom type convSxLAlarmState based on Integer32"""
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
              16,
              32,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("alarmLOS", 1),
          ("alarmCDR", 2),
          ("alarmTxFault", 3),
          ("alarmRxLevel", 4),
          ("warningRxLevel", 5),
          ("warningTxLevel", 6),
          ("activeAlarms", 16),
          ("activeWarnigs", 32),
          ("notAvailable", 255))
    )


_ConvSxLAlarmState_Type.__name__ = "Integer32"
_ConvSxLAlarmState_Object = MibTableColumn
convSxLAlarmState = _ConvSxLAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 12),
    _ConvSxLAlarmState_Type()
)
convSxLAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLAlarmState.setStatus("current")


class _ConvSxLDMIState_Type(Integer32):
    """Custom type convSxLDMIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("sff-8472Rev9-3", 1),
          ("sff-8472Rev9-4", 2))
    )


_ConvSxLDMIState_Type.__name__ = "Integer32"
_ConvSxLDMIState_Object = MibTableColumn
convSxLDMIState = _ConvSxLDMIState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 5, 1, 13),
    _ConvSxLDMIState_Type()
)
convSxLDMIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLDMIState.setStatus("current")
_ConvSxLPortConfigTable_Object = MibTable
convSxLPortConfigTable = _ConvSxLPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6)
)
if mibBuilder.loadTexts:
    convSxLPortConfigTable.setStatus("current")
_ConvSxLPortConfigEntry_Object = MibTableRow
convSxLPortConfigEntry = _ConvSxLPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1)
)
convSxLPortConfigEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLCPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLPortConfigEntry.setStatus("current")


class _ConvSxLCPortIndex_Type(Integer32):
    """Custom type convSxLCPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLCPortIndex_Type.__name__ = "Integer32"
_ConvSxLCPortIndex_Object = MibTableColumn
convSxLCPortIndex = _ConvSxLCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 1),
    _ConvSxLCPortIndex_Type()
)
convSxLCPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLCPortIndex.setStatus("current")


class _ConvSxLCSlot_Type(Integer32):
    """Custom type convSxLCSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLCSlot_Type.__name__ = "Integer32"
_ConvSxLCSlot_Object = MibTableColumn
convSxLCSlot = _ConvSxLCSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 2),
    _ConvSxLCSlot_Type()
)
convSxLCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLCSlot.setStatus("current")
_ConvSxLCPort_Type = Integer32
_ConvSxLCPort_Object = MibTableColumn
convSxLCPort = _ConvSxLCPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 3),
    _ConvSxLCPort_Type()
)
convSxLCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLCPort.setStatus("current")


class _ConvSxLAdminConfig_Type(Integer32):
    """Custom type convSxLAdminConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("adminUp", 1),
          ("notAvailable", 255))
    )


_ConvSxLAdminConfig_Type.__name__ = "Integer32"
_ConvSxLAdminConfig_Object = MibTableColumn
convSxLAdminConfig = _ConvSxLAdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 4),
    _ConvSxLAdminConfig_Type()
)
convSxLAdminConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLAdminConfig.setStatus("current")


class _ConvSxLLLCFConfig_Type(Integer32):
    """Custom type convSxLLLCFConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notAvailable", 255))
    )


_ConvSxLLLCFConfig_Type.__name__ = "Integer32"
_ConvSxLLLCFConfig_Object = MibTableColumn
convSxLLLCFConfig = _ConvSxLLLCFConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 5),
    _ConvSxLLLCFConfig_Type()
)
convSxLLLCFConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLLLCFConfig.setStatus("current")


class _ConvSxLLoopConfig_Type(Integer32):
    """Custom type convSxLLoopConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notAvailable", 255))
    )


_ConvSxLLoopConfig_Type.__name__ = "Integer32"
_ConvSxLLoopConfig_Object = MibTableColumn
convSxLLoopConfig = _ConvSxLLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 6),
    _ConvSxLLoopConfig_Type()
)
convSxLLoopConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLLoopConfig.setStatus("current")


class _ConvSxLSpeedConfig_Type(Integer32):
    """Custom type convSxLSpeedConfig based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              255)
        )
    )
    namedValues = NamedValues(
        *(("speedTransparent", 0),
          ("speedSTM1-155Mbit", 1),
          ("speedSTM4-622Mbit", 2),
          ("speedSTM16-2488Mbit", 3),
          ("sSTM16FEC2666Mbit", 4),
          ("sFastEthernet125Mbit", 5),
          ("sGigabitEthernet1250Mbit", 6),
          ("sFibreChannel133Mbit", 7),
          ("sFibreChannel266Mbit", 8),
          ("sFibreChannel531Mbit", 9),
          ("sFibreChannel1062Mbit", 10),
          ("sFibreChannel2125Mbit", 11),
          ("sESCON200Mbit", 12),
          ("sVIDEO143Mbit", 13),
          ("sVIDEO177Mbit", 14),
          ("sVIDEO270Mbit", 15),
          ("sVIDEO360Mbit", 16),
          ("sVIDEO540Mbit", 17),
          ("sVIDEO1001Mbit", 18),
          ("sVIDEO1485Mbit", 19),
          ("sVIDEO2970Mbit", 20),
          ("notAvailable", 255))
    )


_ConvSxLSpeedConfig_Type.__name__ = "Integer32"
_ConvSxLSpeedConfig_Object = MibTableColumn
convSxLSpeedConfig = _ConvSxLSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 7),
    _ConvSxLSpeedConfig_Type()
)
convSxLSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLSpeedConfig.setStatus("current")


class _ConvSxLPortConnection_Type(Integer32):
    """Custom type convSxLPortConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noConnection", 0),
          ("fromPort1", 1),
          ("fromPort2", 2),
          ("fromPort3", 3),
          ("fromPort4", 4),
          ("notPossible", 255))
    )


_ConvSxLPortConnection_Type.__name__ = "Integer32"
_ConvSxLPortConnection_Object = MibTableColumn
convSxLPortConnection = _ConvSxLPortConnection_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 8),
    _ConvSxLPortConnection_Type()
)
convSxLPortConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLPortConnection.setStatus("current")


class _ConvSxLPortAlarmDeactivation_Type(Integer32):
    """Custom type convSxLPortAlarmDeactivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("alarmReportingEnabled", 1),
          ("alarmReportingDisabledbySchedule", 2),
          ("alarmReportingDisabledPermanent", 3),
          ("unknown", 255))
    )


_ConvSxLPortAlarmDeactivation_Type.__name__ = "Integer32"
_ConvSxLPortAlarmDeactivation_Object = MibTableColumn
convSxLPortAlarmDeactivation = _ConvSxLPortAlarmDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 9),
    _ConvSxLPortAlarmDeactivation_Type()
)
convSxLPortAlarmDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLPortAlarmDeactivation.setStatus("current")


class _ConvSxLPortAlarmSchedule_Type(Integer32):
    """Custom type convSxLPortAlarmSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_ConvSxLPortAlarmSchedule_Type.__name__ = "Integer32"
_ConvSxLPortAlarmSchedule_Object = MibTableColumn
convSxLPortAlarmSchedule = _ConvSxLPortAlarmSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 6, 1, 10),
    _ConvSxLPortAlarmSchedule_Type()
)
convSxLPortAlarmSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLPortAlarmSchedule.setStatus("current")
_ConvSxSFPIdentifikation_ObjectIdentity = ObjectIdentity
convSxSFPIdentifikation = _ConvSxSFPIdentifikation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7)
)
_ConvSXLSFPDescriptionTable_Object = MibTable
convSXLSFPDescriptionTable = _ConvSXLSFPDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    convSXLSFPDescriptionTable.setStatus("current")
_ConvSXLSFPDescriptionEntry_Object = MibTableRow
convSXLSFPDescriptionEntry = _ConvSXLSFPDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1)
)
convSXLSFPDescriptionEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSFPPortIndex"),
)
if mibBuilder.loadTexts:
    convSXLSFPDescriptionEntry.setStatus("current")


class _ConvSxLSFPPortIndex_Type(Integer32):
    """Custom type convSxLSFPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLSFPPortIndex_Type.__name__ = "Integer32"
_ConvSxLSFPPortIndex_Object = MibTableColumn
convSxLSFPPortIndex = _ConvSxLSFPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 1),
    _ConvSxLSFPPortIndex_Type()
)
convSxLSFPPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLSFPPortIndex.setStatus("current")


class _ConvSxLSFPSlot_Type(Integer32):
    """Custom type convSxLSFPSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSFPSlot_Type.__name__ = "Integer32"
_ConvSxLSFPSlot_Object = MibTableColumn
convSxLSFPSlot = _ConvSxLSFPSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 2),
    _ConvSxLSFPSlot_Type()
)
convSxLSFPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPSlot.setStatus("current")
_ConvSxLSFPPort_Type = Integer32
_ConvSxLSFPPort_Object = MibTableColumn
convSxLSFPPort = _ConvSxLSFPPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 3),
    _ConvSxLSFPPort_Type()
)
convSxLSFPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPPort.setStatus("current")


class _ConvSxLSFPVendor_Type(DisplayString):
    """Custom type convSxLSFPVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConvSxLSFPVendor_Type.__name__ = "DisplayString"
_ConvSxLSFPVendor_Object = MibTableColumn
convSxLSFPVendor = _ConvSxLSFPVendor_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 4),
    _ConvSxLSFPVendor_Type()
)
convSxLSFPVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPVendor.setStatus("current")


class _ConvSxLSFPVendorOUI_Type(DisplayString):
    """Custom type convSxLSFPVendorOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ConvSxLSFPVendorOUI_Type.__name__ = "DisplayString"
_ConvSxLSFPVendorOUI_Object = MibTableColumn
convSxLSFPVendorOUI = _ConvSxLSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 5),
    _ConvSxLSFPVendorOUI_Type()
)
convSxLSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPVendorOUI.setStatus("current")


class _ConvSxLSFPVendorCode_Type(DisplayString):
    """Custom type convSxLSFPVendorCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLSFPVendorCode_Type.__name__ = "DisplayString"
_ConvSxLSFPVendorCode_Object = MibTableColumn
convSxLSFPVendorCode = _ConvSxLSFPVendorCode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 6),
    _ConvSxLSFPVendorCode_Type()
)
convSxLSFPVendorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPVendorCode.setStatus("current")


class _ConvSxLSFPVendorRevisionCode_Type(DisplayString):
    """Custom type convSxLSFPVendorRevisionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ConvSxLSFPVendorRevisionCode_Type.__name__ = "DisplayString"
_ConvSxLSFPVendorRevisionCode_Object = MibTableColumn
convSxLSFPVendorRevisionCode = _ConvSxLSFPVendorRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 7),
    _ConvSxLSFPVendorRevisionCode_Type()
)
convSxLSFPVendorRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPVendorRevisionCode.setStatus("current")


class _ConvSxLSFPVendorDateCode_Type(DisplayString):
    """Custom type convSxLSFPVendorDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ConvSxLSFPVendorDateCode_Type.__name__ = "DisplayString"
_ConvSxLSFPVendorDateCode_Object = MibTableColumn
convSxLSFPVendorDateCode = _ConvSxLSFPVendorDateCode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 8),
    _ConvSxLSFPVendorDateCode_Type()
)
convSxLSFPVendorDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPVendorDateCode.setStatus("current")


class _ConvSxLSFPVendorSerialNumber_Type(DisplayString):
    """Custom type convSxLSFPVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLSFPVendorSerialNumber_Type.__name__ = "DisplayString"
_ConvSxLSFPVendorSerialNumber_Object = MibTableColumn
convSxLSFPVendorSerialNumber = _ConvSxLSFPVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 9),
    _ConvSxLSFPVendorSerialNumber_Type()
)
convSxLSFPVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPVendorSerialNumber.setStatus("current")


class _ConvSxLSFPType_Type(Integer32):
    """Custom type convSxLSFPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              11,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("tGBIC", 1),
          ("tModuleSolderedToMotherboard", 2),
          ("tSFPTransceiver", 3),
          ("tDWDMSFPTransceiver", 11),
          ("tCopperSFPTransceiver", 254),
          ("vendorSpecific", 255))
    )


_ConvSxLSFPType_Type.__name__ = "Integer32"
_ConvSxLSFPType_Object = MibTableColumn
convSxLSFPType = _ConvSxLSFPType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 10),
    _ConvSxLSFPType_Type()
)
convSxLSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPType.setStatus("current")


class _ConvSxLSFPConnector_Type(Integer32):
    """Custom type convSxLSFPConnector based on Integer32"""
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
              8,
              9,
              10,
              11,
              32,
              33,
              34,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("cSC", 1),
          ("cFibreChannelStyle1CopperConnector", 2),
          ("cFibreChannelStyle2CopperConnector", 3),
          ("cBncTnc", 4),
          ("cFibreChannerCoaxialHeader", 5),
          ("cFibreJack", 6),
          ("cLC", 7),
          ("cMTRJ", 8),
          ("cMU", 9),
          ("cSG", 10),
          ("cOpticalPigtail", 11),
          ("cHSSDCII", 32),
          ("cCopperPigtail", 33),
          ("cRJ45", 34),
          ("unknown", 255))
    )


_ConvSxLSFPConnector_Type.__name__ = "Integer32"
_ConvSxLSFPConnector_Object = MibTableColumn
convSxLSFPConnector = _ConvSxLSFPConnector_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 11),
    _ConvSxLSFPConnector_Type()
)
convSxLSFPConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPConnector.setStatus("current")


class _ConvSxLSFPWavelength_Type(DisplayString):
    """Custom type convSxLSFPWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ConvSxLSFPWavelength_Type.__name__ = "DisplayString"
_ConvSxLSFPWavelength_Object = MibTableColumn
convSxLSFPWavelength = _ConvSxLSFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 1, 1, 12),
    _ConvSxLSFPWavelength_Type()
)
convSxLSFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPWavelength.setStatus("current")
_ConvSxLSFPBitrateTable_Object = MibTable
convSxLSFPBitrateTable = _ConvSxLSFPBitrateTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    convSxLSFPBitrateTable.setStatus("current")
_ConvSxLSFPBitrateEntry_Object = MibTableRow
convSxLSFPBitrateEntry = _ConvSxLSFPBitrateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 2, 1)
)
convSxLSFPBitrateEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSFPBitratePortIndex"),
)
if mibBuilder.loadTexts:
    convSxLSFPBitrateEntry.setStatus("current")


class _ConvSxLSFPBitratePortIndex_Type(Integer32):
    """Custom type convSxLSFPBitratePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLSFPBitratePortIndex_Type.__name__ = "Integer32"
_ConvSxLSFPBitratePortIndex_Object = MibTableColumn
convSxLSFPBitratePortIndex = _ConvSxLSFPBitratePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 2, 1, 1),
    _ConvSxLSFPBitratePortIndex_Type()
)
convSxLSFPBitratePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLSFPBitratePortIndex.setStatus("current")


class _ConvSxLSFPBitrateSlot_Type(Integer32):
    """Custom type convSxLSFPBitrateSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSFPBitrateSlot_Type.__name__ = "Integer32"
_ConvSxLSFPBitrateSlot_Object = MibTableColumn
convSxLSFPBitrateSlot = _ConvSxLSFPBitrateSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 2, 1, 2),
    _ConvSxLSFPBitrateSlot_Type()
)
convSxLSFPBitrateSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPBitrateSlot.setStatus("current")
_ConvSxLSFPBitratePort_Type = Integer32
_ConvSxLSFPBitratePort_Object = MibTableColumn
convSxLSFPBitratePort = _ConvSxLSFPBitratePort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 2, 1, 3),
    _ConvSxLSFPBitratePort_Type()
)
convSxLSFPBitratePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPBitratePort.setStatus("current")


class _ConvSxLSFPBitrateNominal_Type(Integer32):
    """Custom type convSxLSFPBitrateNominal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("notAvailable", 255)
    )


_ConvSxLSFPBitrateNominal_Type.__name__ = "Integer32"
_ConvSxLSFPBitrateNominal_Object = MibTableColumn
convSxLSFPBitrateNominal = _ConvSxLSFPBitrateNominal_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 2, 1, 4),
    _ConvSxLSFPBitrateNominal_Type()
)
convSxLSFPBitrateNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPBitrateNominal.setStatus("current")


class _ConvSxLSFPBitrateMax_Type(Integer32):
    """Custom type convSxLSFPBitrateMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("notAvailable", 255)
    )


_ConvSxLSFPBitrateMax_Type.__name__ = "Integer32"
_ConvSxLSFPBitrateMax_Object = MibTableColumn
convSxLSFPBitrateMax = _ConvSxLSFPBitrateMax_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 2, 1, 5),
    _ConvSxLSFPBitrateMax_Type()
)
convSxLSFPBitrateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPBitrateMax.setStatus("current")


class _ConvSxLSFPBitrateMin_Type(Integer32):
    """Custom type convSxLSFPBitrateMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("notAvailable", 255)
    )


_ConvSxLSFPBitrateMin_Type.__name__ = "Integer32"
_ConvSxLSFPBitrateMin_Object = MibTableColumn
convSxLSFPBitrateMin = _ConvSxLSFPBitrateMin_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 2, 1, 6),
    _ConvSxLSFPBitrateMin_Type()
)
convSxLSFPBitrateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPBitrateMin.setStatus("current")
_ConvSxLSFPLengthTable_Object = MibTable
convSxLSFPLengthTable = _ConvSxLSFPLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3)
)
if mibBuilder.loadTexts:
    convSxLSFPLengthTable.setStatus("current")
_ConvSxLSFPLengthEntry_Object = MibTableRow
convSxLSFPLengthEntry = _ConvSxLSFPLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3, 1)
)
convSxLSFPLengthEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSFPLengthPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLSFPLengthEntry.setStatus("current")


class _ConvSxLSFPLengthPortIndex_Type(Integer32):
    """Custom type convSxLSFPLengthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLSFPLengthPortIndex_Type.__name__ = "Integer32"
_ConvSxLSFPLengthPortIndex_Object = MibTableColumn
convSxLSFPLengthPortIndex = _ConvSxLSFPLengthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3, 1, 1),
    _ConvSxLSFPLengthPortIndex_Type()
)
convSxLSFPLengthPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLSFPLengthPortIndex.setStatus("current")


class _ConvSxLSFPLengthSlot_Type(Integer32):
    """Custom type convSxLSFPLengthSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSFPLengthSlot_Type.__name__ = "Integer32"
_ConvSxLSFPLengthSlot_Object = MibTableColumn
convSxLSFPLengthSlot = _ConvSxLSFPLengthSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3, 1, 2),
    _ConvSxLSFPLengthSlot_Type()
)
convSxLSFPLengthSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPLengthSlot.setStatus("current")
_ConvSxLSFPLengthPort_Type = Integer32
_ConvSxLSFPLengthPort_Object = MibTableColumn
convSxLSFPLengthPort = _ConvSxLSFPLengthPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3, 1, 3),
    _ConvSxLSFPLengthPort_Type()
)
convSxLSFPLengthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPLengthPort.setStatus("current")


class _ConvSxLSFPLength9km_Type(Integer32):
    """Custom type convSxLSFPLength9km based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("grater254km", 255)
    )


_ConvSxLSFPLength9km_Type.__name__ = "Integer32"
_ConvSxLSFPLength9km_Object = MibTableColumn
convSxLSFPLength9km = _ConvSxLSFPLength9km_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3, 1, 4),
    _ConvSxLSFPLength9km_Type()
)
convSxLSFPLength9km.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPLength9km.setStatus("current")


class _ConvSxLSFPLength9m_Type(Integer32):
    """Custom type convSxLSFPLength9m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("greater25km", 255)
    )


_ConvSxLSFPLength9m_Type.__name__ = "Integer32"
_ConvSxLSFPLength9m_Object = MibTableColumn
convSxLSFPLength9m = _ConvSxLSFPLength9m_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3, 1, 5),
    _ConvSxLSFPLength9m_Type()
)
convSxLSFPLength9m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPLength9m.setStatus("current")


class _ConvSxLSFPLength50_Type(Integer32):
    """Custom type convSxLSFPLength50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("greater2540m", 255)
    )


_ConvSxLSFPLength50_Type.__name__ = "Integer32"
_ConvSxLSFPLength50_Object = MibTableColumn
convSxLSFPLength50 = _ConvSxLSFPLength50_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3, 1, 6),
    _ConvSxLSFPLength50_Type()
)
convSxLSFPLength50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPLength50.setStatus("current")


class _ConvSxLSFPLength62_Type(Integer32):
    """Custom type convSxLSFPLength62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("greater2540m", 255)
    )


_ConvSxLSFPLength62_Type.__name__ = "Integer32"
_ConvSxLSFPLength62_Object = MibTableColumn
convSxLSFPLength62 = _ConvSxLSFPLength62_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3, 1, 7),
    _ConvSxLSFPLength62_Type()
)
convSxLSFPLength62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPLength62.setStatus("current")


class _ConvSxLSFPLengthCopper_Type(Integer32):
    """Custom type convSxLSFPLengthCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("greater254m", 255)
    )


_ConvSxLSFPLengthCopper_Type.__name__ = "Integer32"
_ConvSxLSFPLengthCopper_Object = MibTableColumn
convSxLSFPLengthCopper = _ConvSxLSFPLengthCopper_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 3, 1, 8),
    _ConvSxLSFPLengthCopper_Type()
)
convSxLSFPLengthCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPLengthCopper.setStatus("current")
_ConvSxLSFPCompCodes_ObjectIdentity = ObjectIdentity
convSxLSFPCompCodes = _ConvSxLSFPCompCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4)
)
_ConvSxLSFPCompCodeSonetTable_Object = MibTable
convSxLSFPCompCodeSonetTable = _ConvSxLSFPCompCodeSonetTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    convSxLSFPCompCodeSonetTable.setStatus("current")
_ConvSxLSFPCompCodeSonetEntry_Object = MibTableRow
convSxLSFPCompCodeSonetEntry = _ConvSxLSFPCompCodeSonetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 1, 1)
)
convSxLSFPCompCodeSonetEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSFPCSPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLSFPCompCodeSonetEntry.setStatus("current")


class _ConvSxLSFPCSPortIndex_Type(Integer32):
    """Custom type convSxLSFPCSPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLSFPCSPortIndex_Type.__name__ = "Integer32"
_ConvSxLSFPCSPortIndex_Object = MibTableColumn
convSxLSFPCSPortIndex = _ConvSxLSFPCSPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 1, 1, 1),
    _ConvSxLSFPCSPortIndex_Type()
)
convSxLSFPCSPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLSFPCSPortIndex.setStatus("current")


class _ConvSxLSFPCSSlot_Type(Integer32):
    """Custom type convSxLSFPCSSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSFPCSSlot_Type.__name__ = "Integer32"
_ConvSxLSFPCSSlot_Object = MibTableColumn
convSxLSFPCSSlot = _ConvSxLSFPCSSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 1, 1, 2),
    _ConvSxLSFPCSSlot_Type()
)
convSxLSFPCSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCSSlot.setStatus("current")
_ConvSxLSFPCSPort_Type = Integer32
_ConvSxLSFPCSPort_Object = MibTableColumn
convSxLSFPCSPort = _ConvSxLSFPCSPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 1, 1, 3),
    _ConvSxLSFPCSPort_Type()
)
convSxLSFPCSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCSPort.setStatus("current")


class _ConvSxLSFPCSProtocol_Type(Integer32):
    """Custom type convSxLSFPCSProtocol based on Integer32"""
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
          ("sOC3", 1),
          ("sOC12", 2),
          ("sOC48", 3))
    )


_ConvSxLSFPCSProtocol_Type.__name__ = "Integer32"
_ConvSxLSFPCSProtocol_Object = MibTableColumn
convSxLSFPCSProtocol = _ConvSxLSFPCSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 1, 1, 4),
    _ConvSxLSFPCSProtocol_Type()
)
convSxLSFPCSProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCSProtocol.setStatus("current")


class _ConvSxLSFPCSRange_Type(Integer32):
    """Custom type convSxLSFPCSRange based on Integer32"""
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
          ("short", 1),
          ("intermediate", 2),
          ("long", 3))
    )


_ConvSxLSFPCSRange_Type.__name__ = "Integer32"
_ConvSxLSFPCSRange_Object = MibTableColumn
convSxLSFPCSRange = _ConvSxLSFPCSRange_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 1, 1, 5),
    _ConvSxLSFPCSRange_Type()
)
convSxLSFPCSRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCSRange.setStatus("current")


class _ConvSxLSFPCSFiberType_Type(Integer32):
    """Custom type convSxLSFPCSFiberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("multimode", 1),
          ("singlemode", 4))
    )


_ConvSxLSFPCSFiberType_Type.__name__ = "Integer32"
_ConvSxLSFPCSFiberType_Object = MibTableColumn
convSxLSFPCSFiberType = _ConvSxLSFPCSFiberType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 1, 1, 6),
    _ConvSxLSFPCSFiberType_Type()
)
convSxLSFPCSFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCSFiberType.setStatus("current")
_ConvSxLSFPCompCodeGigabitEthernetTable_Object = MibTable
convSxLSFPCompCodeGigabitEthernetTable = _ConvSxLSFPCompCodeGigabitEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 2)
)
if mibBuilder.loadTexts:
    convSxLSFPCompCodeGigabitEthernetTable.setStatus("current")
_ConvSxLSFPCompCodeGigabitEthernetEntry_Object = MibTableRow
convSxLSFPCompCodeGigabitEthernetEntry = _ConvSxLSFPCompCodeGigabitEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 2, 1)
)
convSxLSFPCompCodeGigabitEthernetEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSFPCGPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLSFPCompCodeGigabitEthernetEntry.setStatus("current")


class _ConvSxLSFPCGPortIndex_Type(Integer32):
    """Custom type convSxLSFPCGPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLSFPCGPortIndex_Type.__name__ = "Integer32"
_ConvSxLSFPCGPortIndex_Object = MibTableColumn
convSxLSFPCGPortIndex = _ConvSxLSFPCGPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 2, 1, 1),
    _ConvSxLSFPCGPortIndex_Type()
)
convSxLSFPCGPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLSFPCGPortIndex.setStatus("current")


class _ConvSxLSFPCGSlot_Type(Integer32):
    """Custom type convSxLSFPCGSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSFPCGSlot_Type.__name__ = "Integer32"
_ConvSxLSFPCGSlot_Object = MibTableColumn
convSxLSFPCGSlot = _ConvSxLSFPCGSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 2, 1, 2),
    _ConvSxLSFPCGSlot_Type()
)
convSxLSFPCGSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCGSlot.setStatus("current")
_ConvSxLSFPCGPort_Type = Integer32
_ConvSxLSFPCGPort_Object = MibTableColumn
convSxLSFPCGPort = _ConvSxLSFPCGPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 2, 1, 3),
    _ConvSxLSFPCGPort_Type()
)
convSxLSFPCGPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCGPort.setStatus("current")


class _ConvSxLSFPCGType_Type(Integer32):
    """Custom type convSxLSFPCGType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              32,
              48)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("g1000BASE-SX", 1),
          ("g1000BASE-LX", 2),
          ("g1000BASE-CX", 4),
          ("g1000BASE-T", 8),
          ("g100Base-Fx", 32),
          ("g100Base-Fx-LX", 48))
    )


_ConvSxLSFPCGType_Type.__name__ = "Integer32"
_ConvSxLSFPCGType_Object = MibTableColumn
convSxLSFPCGType = _ConvSxLSFPCGType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 2, 1, 4),
    _ConvSxLSFPCGType_Type()
)
convSxLSFPCGType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCGType.setStatus("current")
_ConvSxLSFPCompCodeFibreChannelTable_Object = MibTable
convSxLSFPCompCodeFibreChannelTable = _ConvSxLSFPCompCodeFibreChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 3)
)
if mibBuilder.loadTexts:
    convSxLSFPCompCodeFibreChannelTable.setStatus("current")
_ConvSxLSFPCompCodeFibreChannelEntry_Object = MibTableRow
convSxLSFPCompCodeFibreChannelEntry = _ConvSxLSFPCompCodeFibreChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 3, 1)
)
convSxLSFPCompCodeFibreChannelEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSFPCFcPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLSFPCompCodeFibreChannelEntry.setStatus("current")


class _ConvSxLSFPCFcPortIndex_Type(Integer32):
    """Custom type convSxLSFPCFcPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLSFPCFcPortIndex_Type.__name__ = "Integer32"
_ConvSxLSFPCFcPortIndex_Object = MibTableColumn
convSxLSFPCFcPortIndex = _ConvSxLSFPCFcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 3, 1, 1),
    _ConvSxLSFPCFcPortIndex_Type()
)
convSxLSFPCFcPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLSFPCFcPortIndex.setStatus("current")


class _ConvSxLSFPCFcSlot_Type(Integer32):
    """Custom type convSxLSFPCFcSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSFPCFcSlot_Type.__name__ = "Integer32"
_ConvSxLSFPCFcSlot_Object = MibTableColumn
convSxLSFPCFcSlot = _ConvSxLSFPCFcSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 3, 1, 2),
    _ConvSxLSFPCFcSlot_Type()
)
convSxLSFPCFcSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCFcSlot.setStatus("current")
_ConvSxLSFPCFcPort_Type = Integer32
_ConvSxLSFPCFcPort_Object = MibTableColumn
convSxLSFPCFcPort = _ConvSxLSFPCFcPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 3, 1, 3),
    _ConvSxLSFPCFcPort_Type()
)
convSxLSFPCFcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCFcPort.setStatus("current")


class _ConvSxLSFPCFcMedia_Type(Integer32):
    """Custom type convSxLSFPCFcMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              12,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("mnotSupported", 0),
          ("mSingleMode", 1),
          ("reserved", 2),
          ("mMultiMode50", 4),
          ("mMultiMode62-5", 8),
          ("mMultiMode50m-62-5m", 12),
          ("mVideoCoax", 16),
          ("mMiniatureCoax", 32),
          ("mShieldedTwistedPair", 64),
          ("mTwinAxialPair", 128))
    )


_ConvSxLSFPCFcMedia_Type.__name__ = "Integer32"
_ConvSxLSFPCFcMedia_Object = MibTableColumn
convSxLSFPCFcMedia = _ConvSxLSFPCFcMedia_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 3, 1, 4),
    _ConvSxLSFPCFcMedia_Type()
)
convSxLSFPCFcMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCFcMedia.setStatus("current")


class _ConvSxLSFPCFcTech_Type(Integer32):
    """Custom type convSxLSFPCFcTech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              11,
              12,
              13,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("tLongwaveLaserLL", 10),
          ("tLongwaveLaserLC", 11),
          ("tShortwaveLaserW-OFC", 12),
          ("tShortwaveLaserW-O-OFC", 13),
          ("tElectricalInterenclosure", 20),
          ("tElectricalIntraenclosure", 21))
    )


_ConvSxLSFPCFcTech_Type.__name__ = "Integer32"
_ConvSxLSFPCFcTech_Object = MibTableColumn
convSxLSFPCFcTech = _ConvSxLSFPCFcTech_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 3, 1, 5),
    _ConvSxLSFPCFcTech_Type()
)
convSxLSFPCFcTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCFcTech.setStatus("current")


class _ConvSxLSFPCFcLinkLength_Type(Integer32):
    """Custom type convSxLSFPCFcLinkLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("longDistance", 16),
          ("intermediateDistance", 32),
          ("shortDistance", 64),
          ("verylongDistance", 128))
    )


_ConvSxLSFPCFcLinkLength_Type.__name__ = "Integer32"
_ConvSxLSFPCFcLinkLength_Object = MibTableColumn
convSxLSFPCFcLinkLength = _ConvSxLSFPCFcLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 3, 1, 6),
    _ConvSxLSFPCFcLinkLength_Type()
)
convSxLSFPCFcLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCFcLinkLength.setStatus("current")


class _ConvSxLSFPCFcSpeed_Type(Integer32):
    """Custom type convSxLSFPCFcSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              16,
              21)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("fcSpeed100MByte", 1),
          ("fcSpeed200MByte", 4),
          ("fcSpeed100-200MByte", 5),
          ("fcSpeed400MByte", 16),
          ("fcSpeed100-200-400MByte", 21))
    )


_ConvSxLSFPCFcSpeed_Type.__name__ = "Integer32"
_ConvSxLSFPCFcSpeed_Object = MibTableColumn
convSxLSFPCFcSpeed = _ConvSxLSFPCFcSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 4, 3, 1, 7),
    _ConvSxLSFPCFcSpeed_Type()
)
convSxLSFPCFcSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPCFcSpeed.setStatus("current")
_ConvSxLCopperSFPTable_Object = MibTable
convSxLCopperSFPTable = _ConvSxLCopperSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5)
)
if mibBuilder.loadTexts:
    convSxLCopperSFPTable.setStatus("current")
_ConvSxLCopperSFPEntry_Object = MibTableRow
convSxLCopperSFPEntry = _ConvSxLCopperSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1)
)
convSxLCopperSFPEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLCuSFPPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLCopperSFPEntry.setStatus("current")


class _ConvSxLCuSFPPortIndex_Type(Integer32):
    """Custom type convSxLCuSFPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLCuSFPPortIndex_Type.__name__ = "Integer32"
_ConvSxLCuSFPPortIndex_Object = MibTableColumn
convSxLCuSFPPortIndex = _ConvSxLCuSFPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 1),
    _ConvSxLCuSFPPortIndex_Type()
)
convSxLCuSFPPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLCuSFPPortIndex.setStatus("current")


class _ConvSxLCuSFPSlot_Type(Integer32):
    """Custom type convSxLCuSFPSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLCuSFPSlot_Type.__name__ = "Integer32"
_ConvSxLCuSFPSlot_Object = MibTableColumn
convSxLCuSFPSlot = _ConvSxLCuSFPSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 2),
    _ConvSxLCuSFPSlot_Type()
)
convSxLCuSFPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLCuSFPSlot.setStatus("current")
_ConvSxLCuSFPPort_Type = Integer32
_ConvSxLCuSFPPort_Object = MibTableColumn
convSxLCuSFPPort = _ConvSxLCuSFPPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 3),
    _ConvSxLCuSFPPort_Type()
)
convSxLCuSFPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLCuSFPPort.setStatus("current")


class _ConvSxLConfigSpeed_Type(Integer32):
    """Custom type convSxLConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("s10Mbit", 1),
          ("s100Mbit", 2),
          ("s1000Mbit", 3),
          ("notSupported", 255))
    )


_ConvSxLConfigSpeed_Type.__name__ = "Integer32"
_ConvSxLConfigSpeed_Object = MibTableColumn
convSxLConfigSpeed = _ConvSxLConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 4),
    _ConvSxLConfigSpeed_Type()
)
convSxLConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLConfigSpeed.setStatus("current")


class _ConvSxLConfigDuplex_Type(Integer32):
    """Custom type convSxLConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("halfduplex", 1),
          ("fullduplex", 2),
          ("notSupported", 255))
    )


_ConvSxLConfigDuplex_Type.__name__ = "Integer32"
_ConvSxLConfigDuplex_Object = MibTableColumn
convSxLConfigDuplex = _ConvSxLConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 5),
    _ConvSxLConfigDuplex_Type()
)
convSxLConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLConfigDuplex.setStatus("current")


class _ConvSxLCuPhyId_Type(Integer32):
    """Custom type convSxLCuPhyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("marvellPhy", 1),
          ("notSupported", 255))
    )


_ConvSxLCuPhyId_Type.__name__ = "Integer32"
_ConvSxLCuPhyId_Object = MibTableColumn
convSxLCuPhyId = _ConvSxLCuPhyId_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 6),
    _ConvSxLCuPhyId_Type()
)
convSxLCuPhyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLCuPhyId.setStatus("current")


class _ConvSxLCuSFPLink_Type(Integer32):
    """Custom type convSxLCuSFPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("notSupported", 255))
    )


_ConvSxLCuSFPLink_Type.__name__ = "Integer32"
_ConvSxLCuSFPLink_Object = MibTableColumn
convSxLCuSFPLink = _ConvSxLCuSFPLink_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 7),
    _ConvSxLCuSFPLink_Type()
)
convSxLCuSFPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLCuSFPLink.setStatus("current")


class _ConvSxLCuSFPSpeed_Type(Integer32):
    """Custom type convSxLCuSFPSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("s10Mbit", 1),
          ("s100Mbit", 2),
          ("s1000Mbit", 3),
          ("notSupported", 255))
    )


_ConvSxLCuSFPSpeed_Type.__name__ = "Integer32"
_ConvSxLCuSFPSpeed_Object = MibTableColumn
convSxLCuSFPSpeed = _ConvSxLCuSFPSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 8),
    _ConvSxLCuSFPSpeed_Type()
)
convSxLCuSFPSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLCuSFPSpeed.setStatus("current")


class _ConvSxLCuSFPDuplex_Type(Integer32):
    """Custom type convSxLCuSFPDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("halfduplex", 1),
          ("fullduplex", 2),
          ("notSupported", 255))
    )


_ConvSxLCuSFPDuplex_Type.__name__ = "Integer32"
_ConvSxLCuSFPDuplex_Object = MibTableColumn
convSxLCuSFPDuplex = _ConvSxLCuSFPDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 9),
    _ConvSxLCuSFPDuplex_Type()
)
convSxLCuSFPDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLCuSFPDuplex.setStatus("current")


class _ConvSxLCuSFPAutoMDIx_Type(Integer32):
    """Custom type convSxLCuSFPAutoMDIx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1),
          ("notSupported", 255))
    )


_ConvSxLCuSFPAutoMDIx_Type.__name__ = "Integer32"
_ConvSxLCuSFPAutoMDIx_Object = MibTableColumn
convSxLCuSFPAutoMDIx = _ConvSxLCuSFPAutoMDIx_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 10),
    _ConvSxLCuSFPAutoMDIx_Type()
)
convSxLCuSFPAutoMDIx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLCuSFPAutoMDIx.setStatus("current")


class _ConvSxLCuSFPConfigMode_Type(Integer32):
    """Custom type convSxLCuSFPConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("auto", 1),
          ("forced", 2),
          ("notSupported", 255))
    )


_ConvSxLCuSFPConfigMode_Type.__name__ = "Integer32"
_ConvSxLCuSFPConfigMode_Object = MibTableColumn
convSxLCuSFPConfigMode = _ConvSxLCuSFPConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 5, 1, 11),
    _ConvSxLCuSFPConfigMode_Type()
)
convSxLCuSFPConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLCuSFPConfigMode.setStatus("current")
_ConvSxLDWDMSFPTable_Object = MibTable
convSxLDWDMSFPTable = _ConvSxLDWDMSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 6)
)
if mibBuilder.loadTexts:
    convSxLDWDMSFPTable.setStatus("current")
_ConvSxLDWDMSFPEntry_Object = MibTableRow
convSxLDWDMSFPEntry = _ConvSxLDWDMSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 6, 1)
)
convSxLDWDMSFPEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLDWDMPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLDWDMSFPEntry.setStatus("current")


class _ConvSxLDWDMPortIndex_Type(Integer32):
    """Custom type convSxLDWDMPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLDWDMPortIndex_Type.__name__ = "Integer32"
_ConvSxLDWDMPortIndex_Object = MibTableColumn
convSxLDWDMPortIndex = _ConvSxLDWDMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 6, 1, 1),
    _ConvSxLDWDMPortIndex_Type()
)
convSxLDWDMPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLDWDMPortIndex.setStatus("current")


class _ConvSxLDWDMSlot_Type(Integer32):
    """Custom type convSxLDWDMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLDWDMSlot_Type.__name__ = "Integer32"
_ConvSxLDWDMSlot_Object = MibTableColumn
convSxLDWDMSlot = _ConvSxLDWDMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 6, 1, 2),
    _ConvSxLDWDMSlot_Type()
)
convSxLDWDMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLDWDMSlot.setStatus("current")
_ConvSxLDWDMPort_Type = Integer32
_ConvSxLDWDMPort_Object = MibTableColumn
convSxLDWDMPort = _ConvSxLDWDMPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 6, 1, 3),
    _ConvSxLDWDMPort_Type()
)
convSxLDWDMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLDWDMPort.setStatus("current")


class _ConvSxLDWDMPowerClass_Type(Integer32):
    """Custom type convSxLDWDMPowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("p-upto1W", 0),
          ("p-between1Wand1-5W", 1),
          ("p-morethan1-5W", 2),
          ("notSupported", 255))
    )


_ConvSxLDWDMPowerClass_Type.__name__ = "Integer32"
_ConvSxLDWDMPowerClass_Object = MibTableColumn
convSxLDWDMPowerClass = _ConvSxLDWDMPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 6, 1, 4),
    _ConvSxLDWDMPowerClass_Type()
)
convSxLDWDMPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLDWDMPowerClass.setStatus("current")
_ConvSxLDWDMMaxSupplyCurrent_Type = Integer32
_ConvSxLDWDMMaxSupplyCurrent_Object = MibTableColumn
convSxLDWDMMaxSupplyCurrent = _ConvSxLDWDMMaxSupplyCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 6, 1, 5),
    _ConvSxLDWDMMaxSupplyCurrent_Type()
)
convSxLDWDMMaxSupplyCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLDWDMMaxSupplyCurrent.setStatus("current")


class _ConvSxLChannelSpacing_Type(Integer32):
    """Custom type convSxLChannelSpacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("g200GHz", 0),
          ("g100GHz", 1),
          ("g50GHz", 2),
          ("notSupported", 255))
    )


_ConvSxLChannelSpacing_Type.__name__ = "Integer32"
_ConvSxLChannelSpacing_Object = MibTableColumn
convSxLChannelSpacing = _ConvSxLChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 6, 1, 6),
    _ConvSxLChannelSpacing_Type()
)
convSxLChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLChannelSpacing.setStatus("current")
_ConvSxLNumberofChannels_Type = Integer32
_ConvSxLNumberofChannels_Object = MibTableColumn
convSxLNumberofChannels = _ConvSxLNumberofChannels_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 7, 6, 1, 7),
    _ConvSxLNumberofChannels_Type()
)
convSxLNumberofChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLNumberofChannels.setStatus("current")
_ConvSxLSFPDMIParamTable_Object = MibTable
convSxLSFPDMIParamTable = _ConvSxLSFPDMIParamTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8)
)
if mibBuilder.loadTexts:
    convSxLSFPDMIParamTable.setStatus("current")
_ConvSxLSFPDMIParamEntry_Object = MibTableRow
convSxLSFPDMIParamEntry = _ConvSxLSFPDMIParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1)
)
convSxLSFPDMIParamEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSFPDMIPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLSFPDMIParamEntry.setStatus("current")


class _ConvSxLSFPDMIPortIndex_Type(Integer32):
    """Custom type convSxLSFPDMIPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLSFPDMIPortIndex_Type.__name__ = "Integer32"
_ConvSxLSFPDMIPortIndex_Object = MibTableColumn
convSxLSFPDMIPortIndex = _ConvSxLSFPDMIPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1, 1),
    _ConvSxLSFPDMIPortIndex_Type()
)
convSxLSFPDMIPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMIPortIndex.setStatus("current")


class _ConvSxLSFPDMISlot_Type(Integer32):
    """Custom type convSxLSFPDMISlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSFPDMISlot_Type.__name__ = "Integer32"
_ConvSxLSFPDMISlot_Object = MibTableColumn
convSxLSFPDMISlot = _ConvSxLSFPDMISlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1, 2),
    _ConvSxLSFPDMISlot_Type()
)
convSxLSFPDMISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMISlot.setStatus("current")
_ConvSxLSFPDMIPort_Type = Integer32
_ConvSxLSFPDMIPort_Object = MibTableColumn
convSxLSFPDMIPort = _ConvSxLSFPDMIPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1, 3),
    _ConvSxLSFPDMIPort_Type()
)
convSxLSFPDMIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMIPort.setStatus("current")
_ConvSxLSFPDMIRxLevel_Type = Integer32
_ConvSxLSFPDMIRxLevel_Object = MibTableColumn
convSxLSFPDMIRxLevel = _ConvSxLSFPDMIRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1, 4),
    _ConvSxLSFPDMIRxLevel_Type()
)
convSxLSFPDMIRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMIRxLevel.setStatus("current")


class _ConvSxLSFPDMIRxHighAlarm_Type(Integer32):
    """Custom type convSxLSFPDMIRxHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1))
    )


_ConvSxLSFPDMIRxHighAlarm_Type.__name__ = "Integer32"
_ConvSxLSFPDMIRxHighAlarm_Object = MibTableColumn
convSxLSFPDMIRxHighAlarm = _ConvSxLSFPDMIRxHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1, 5),
    _ConvSxLSFPDMIRxHighAlarm_Type()
)
convSxLSFPDMIRxHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMIRxHighAlarm.setStatus("current")
_ConvSxLSFPDMITxLevel_Type = Integer32
_ConvSxLSFPDMITxLevel_Object = MibTableColumn
convSxLSFPDMITxLevel = _ConvSxLSFPDMITxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1, 6),
    _ConvSxLSFPDMITxLevel_Type()
)
convSxLSFPDMITxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITxLevel.setStatus("current")
_ConvSxLSFPDMITxBias_Type = Integer32
_ConvSxLSFPDMITxBias_Object = MibTableColumn
convSxLSFPDMITxBias = _ConvSxLSFPDMITxBias_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1, 7),
    _ConvSxLSFPDMITxBias_Type()
)
convSxLSFPDMITxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITxBias.setStatus("current")
_ConvSxLSFPDMIVcc_Type = Integer32
_ConvSxLSFPDMIVcc_Object = MibTableColumn
convSxLSFPDMIVcc = _ConvSxLSFPDMIVcc_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1, 8),
    _ConvSxLSFPDMIVcc_Type()
)
convSxLSFPDMIVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMIVcc.setStatus("current")
_ConvSxLSFPDMITemp_Type = Integer32
_ConvSxLSFPDMITemp_Object = MibTableColumn
convSxLSFPDMITemp = _ConvSxLSFPDMITemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 8, 1, 9),
    _ConvSxLSFPDMITemp_Type()
)
convSxLSFPDMITemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITemp.setStatus("current")
_ConvSxLSFPDMIThresholdTable_Object = MibTable
convSxLSFPDMIThresholdTable = _ConvSxLSFPDMIThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9)
)
if mibBuilder.loadTexts:
    convSxLSFPDMIThresholdTable.setStatus("current")
_ConvSxLSFPDMIThresholdEntry_Object = MibTableRow
convSxLSFPDMIThresholdEntry = _ConvSxLSFPDMIThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9, 1)
)
convSxLSFPDMIThresholdEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSFPDMITPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLSFPDMIThresholdEntry.setStatus("current")


class _ConvSxLSFPDMITPortIndex_Type(Integer32):
    """Custom type convSxLSFPDMITPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLSFPDMITPortIndex_Type.__name__ = "Integer32"
_ConvSxLSFPDMITPortIndex_Object = MibTableColumn
convSxLSFPDMITPortIndex = _ConvSxLSFPDMITPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9, 1, 1),
    _ConvSxLSFPDMITPortIndex_Type()
)
convSxLSFPDMITPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLSFPDMITPortIndex.setStatus("current")


class _ConvSxLSFPDMITSlot_Type(Integer32):
    """Custom type convSxLSFPDMITSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSFPDMITSlot_Type.__name__ = "Integer32"
_ConvSxLSFPDMITSlot_Object = MibTableColumn
convSxLSFPDMITSlot = _ConvSxLSFPDMITSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9, 1, 2),
    _ConvSxLSFPDMITSlot_Type()
)
convSxLSFPDMITSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITSlot.setStatus("current")
_ConvSxLSFPDMITPort_Type = Integer32
_ConvSxLSFPDMITPort_Object = MibTableColumn
convSxLSFPDMITPort = _ConvSxLSFPDMITPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9, 1, 3),
    _ConvSxLSFPDMITPort_Type()
)
convSxLSFPDMITPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITPort.setStatus("current")
_ConvSxLSFPDMITRxLowThresholdWarningLevel_Type = Integer32
_ConvSxLSFPDMITRxLowThresholdWarningLevel_Object = MibTableColumn
convSxLSFPDMITRxLowThresholdWarningLevel = _ConvSxLSFPDMITRxLowThresholdWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9, 1, 4),
    _ConvSxLSFPDMITRxLowThresholdWarningLevel_Type()
)
convSxLSFPDMITRxLowThresholdWarningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLSFPDMITRxLowThresholdWarningLevel.setStatus("current")
_ConvSxLSFPDMITRxLowThresholdAlarmLevel_Type = Integer32
_ConvSxLSFPDMITRxLowThresholdAlarmLevel_Object = MibTableColumn
convSxLSFPDMITRxLowThresholdAlarmLevel = _ConvSxLSFPDMITRxLowThresholdAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9, 1, 5),
    _ConvSxLSFPDMITRxLowThresholdAlarmLevel_Type()
)
convSxLSFPDMITRxLowThresholdAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITRxLowThresholdAlarmLevel.setStatus("current")
_ConvSxLSFPDMITTxLowThresholdWarningLevel_Type = Integer32
_ConvSxLSFPDMITTxLowThresholdWarningLevel_Object = MibTableColumn
convSxLSFPDMITTxLowThresholdWarningLevel = _ConvSxLSFPDMITTxLowThresholdWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9, 1, 6),
    _ConvSxLSFPDMITTxLowThresholdWarningLevel_Type()
)
convSxLSFPDMITTxLowThresholdWarningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLSFPDMITTxLowThresholdWarningLevel.setStatus("current")
_ConvSxLSFPDMITTxLowThresholdAlarmLevel_Type = Integer32
_ConvSxLSFPDMITTxLowThresholdAlarmLevel_Object = MibTableColumn
convSxLSFPDMITTxLowThresholdAlarmLevel = _ConvSxLSFPDMITTxLowThresholdAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9, 1, 7),
    _ConvSxLSFPDMITTxLowThresholdAlarmLevel_Type()
)
convSxLSFPDMITTxLowThresholdAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITTxLowThresholdAlarmLevel.setStatus("current")


class _ConvSxLSFPDMITThresholdsUsage_Type(Integer32):
    """Custom type convSxLSFPDMITThresholdsUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("userDefinedThresholds", 0),
          ("sFPVendorThresholds", 1),
          ("notAvailable", 255))
    )


_ConvSxLSFPDMITThresholdsUsage_Type.__name__ = "Integer32"
_ConvSxLSFPDMITThresholdsUsage_Object = MibTableColumn
convSxLSFPDMITThresholdsUsage = _ConvSxLSFPDMITThresholdsUsage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 9, 1, 8),
    _ConvSxLSFPDMITThresholdsUsage_Type()
)
convSxLSFPDMITThresholdsUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSxLSFPDMITThresholdsUsage.setStatus("current")
_ConvSxLPortEventTable_Object = MibTable
convSxLPortEventTable = _ConvSxLPortEventTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10)
)
if mibBuilder.loadTexts:
    convSxLPortEventTable.setStatus("current")
_ConvSxLPortEventEntry_Object = MibTableRow
convSxLPortEventEntry = _ConvSxLPortEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1)
)
convSxLPortEventEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLSFPEPortIndex"),
)
if mibBuilder.loadTexts:
    convSxLPortEventEntry.setStatus("current")


class _ConvSxLSFPEPortIndex_Type(Integer32):
    """Custom type convSxLSFPEPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_ConvSxLSFPEPortIndex_Type.__name__ = "Integer32"
_ConvSxLSFPEPortIndex_Object = MibTableColumn
convSxLSFPEPortIndex = _ConvSxLSFPEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 1),
    _ConvSxLSFPEPortIndex_Type()
)
convSxLSFPEPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSxLSFPEPortIndex.setStatus("current")


class _ConvSxLSFPESlot_Type(Integer32):
    """Custom type convSxLSFPESlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLSFPESlot_Type.__name__ = "Integer32"
_ConvSxLSFPESlot_Object = MibTableColumn
convSxLSFPESlot = _ConvSxLSFPESlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 2),
    _ConvSxLSFPESlot_Type()
)
convSxLSFPESlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPESlot.setStatus("current")
_ConvSxLSFPEPort_Type = Integer32
_ConvSxLSFPEPort_Object = MibTableColumn
convSxLSFPEPort = _ConvSxLSFPEPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 3),
    _ConvSxLSFPEPort_Type()
)
convSxLSFPEPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPEPort.setStatus("current")


class _ConvSxLSFPDMIRxLowWarningEvent_Type(Integer32):
    """Custom type convSxLSFPDMIRxLowWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDMIRxLowWarningEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDMIRxLowWarningEvent_Object = MibTableColumn
convSxLSFPDMIRxLowWarningEvent = _ConvSxLSFPDMIRxLowWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 4),
    _ConvSxLSFPDMIRxLowWarningEvent_Type()
)
convSxLSFPDMIRxLowWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMIRxLowWarningEvent.setStatus("current")


class _ConvSxLSFPDMIRxLowAlarmEvent_Type(Integer32):
    """Custom type convSxLSFPDMIRxLowAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDMIRxLowAlarmEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDMIRxLowAlarmEvent_Object = MibTableColumn
convSxLSFPDMIRxLowAlarmEvent = _ConvSxLSFPDMIRxLowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 5),
    _ConvSxLSFPDMIRxLowAlarmEvent_Type()
)
convSxLSFPDMIRxLowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMIRxLowAlarmEvent.setStatus("current")


class _ConvSxLSFPDMITxLowWarningEvent_Type(Integer32):
    """Custom type convSxLSFPDMITxLowWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDMITxLowWarningEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDMITxLowWarningEvent_Object = MibTableColumn
convSxLSFPDMITxLowWarningEvent = _ConvSxLSFPDMITxLowWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 6),
    _ConvSxLSFPDMITxLowWarningEvent_Type()
)
convSxLSFPDMITxLowWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITxLowWarningEvent.setStatus("current")


class _ConvSxLSFPDMITxLowAlarmEvent_Type(Integer32):
    """Custom type convSxLSFPDMITxLowAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDMITxLowAlarmEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDMITxLowAlarmEvent_Object = MibTableColumn
convSxLSFPDMITxLowAlarmEvent = _ConvSxLSFPDMITxLowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 7),
    _ConvSxLSFPDMITxLowAlarmEvent_Type()
)
convSxLSFPDMITxLowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITxLowAlarmEvent.setStatus("current")


class _ConvSxLSFPDMIBiasAlarmEvent_Type(Integer32):
    """Custom type convSxLSFPDMIBiasAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDMIBiasAlarmEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDMIBiasAlarmEvent_Object = MibTableColumn
convSxLSFPDMIBiasAlarmEvent = _ConvSxLSFPDMIBiasAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 8),
    _ConvSxLSFPDMIBiasAlarmEvent_Type()
)
convSxLSFPDMIBiasAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMIBiasAlarmEvent.setStatus("current")


class _ConvSxLSFPDMIRxHighAlarmEvent_Type(Integer32):
    """Custom type convSxLSFPDMIRxHighAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDMIRxHighAlarmEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDMIRxHighAlarmEvent_Object = MibTableColumn
convSxLSFPDMIRxHighAlarmEvent = _ConvSxLSFPDMIRxHighAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 9),
    _ConvSxLSFPDMIRxHighAlarmEvent_Type()
)
convSxLSFPDMIRxHighAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMIRxHighAlarmEvent.setStatus("current")


class _ConvSxLSFPDWDMLaserTHighAlarmEvent_Type(Integer32):
    """Custom type convSxLSFPDWDMLaserTHighAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDWDMLaserTHighAlarmEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDWDMLaserTHighAlarmEvent_Object = MibTableColumn
convSxLSFPDWDMLaserTHighAlarmEvent = _ConvSxLSFPDWDMLaserTHighAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 10),
    _ConvSxLSFPDWDMLaserTHighAlarmEvent_Type()
)
convSxLSFPDWDMLaserTHighAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDWDMLaserTHighAlarmEvent.setStatus("current")


class _ConvSxLSFPDWDMLaserTLowAlarmEvent_Type(Integer32):
    """Custom type convSxLSFPDWDMLaserTLowAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDWDMLaserTLowAlarmEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDWDMLaserTLowAlarmEvent_Object = MibTableColumn
convSxLSFPDWDMLaserTLowAlarmEvent = _ConvSxLSFPDWDMLaserTLowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 11),
    _ConvSxLSFPDWDMLaserTLowAlarmEvent_Type()
)
convSxLSFPDWDMLaserTLowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDWDMLaserTLowAlarmEvent.setStatus("current")


class _ConvSxLSFPDWDMTECHighAlarmEvent_Type(Integer32):
    """Custom type convSxLSFPDWDMTECHighAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDWDMTECHighAlarmEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDWDMTECHighAlarmEvent_Object = MibTableColumn
convSxLSFPDWDMTECHighAlarmEvent = _ConvSxLSFPDWDMTECHighAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 12),
    _ConvSxLSFPDWDMTECHighAlarmEvent_Type()
)
convSxLSFPDWDMTECHighAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDWDMTECHighAlarmEvent.setStatus("current")


class _ConvSxLSFPDWDMTECLowAlarmEvent_Type(Integer32):
    """Custom type convSxLSFPDWDMTECLowAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDWDMTECLowAlarmEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDWDMTECLowAlarmEvent_Object = MibTableColumn
convSxLSFPDWDMTECLowAlarmEvent = _ConvSxLSFPDWDMTECLowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 13),
    _ConvSxLSFPDWDMTECLowAlarmEvent_Type()
)
convSxLSFPDWDMTECLowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDWDMTECLowAlarmEvent.setStatus("current")


class _ConvSxLSFPDMITempHighWarningEvent_Type(Integer32):
    """Custom type convSxLSFPDMITempHighWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDMITempHighWarningEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDMITempHighWarningEvent_Object = MibTableColumn
convSxLSFPDMITempHighWarningEvent = _ConvSxLSFPDMITempHighWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 14),
    _ConvSxLSFPDMITempHighWarningEvent_Type()
)
convSxLSFPDMITempHighWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITempHighWarningEvent.setStatus("current")


class _ConvSxLSFPDMITempHighAlarmEvent_Type(Integer32):
    """Custom type convSxLSFPDMITempHighAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notimplemented", 255))
    )


_ConvSxLSFPDMITempHighAlarmEvent_Type.__name__ = "Integer32"
_ConvSxLSFPDMITempHighAlarmEvent_Object = MibTableColumn
convSxLSFPDMITempHighAlarmEvent = _ConvSxLSFPDMITempHighAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 10, 1, 15),
    _ConvSxLSFPDMITempHighAlarmEvent_Type()
)
convSxLSFPDMITempHighAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPDMITempHighAlarmEvent.setStatus("current")
_ConvSxLInventoryTable_Object = MibTable
convSxLInventoryTable = _ConvSxLInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 11)
)
if mibBuilder.loadTexts:
    convSxLInventoryTable.setStatus("current")
_ConvSxLInventoryEntry_Object = MibTableRow
convSxLInventoryEntry = _ConvSxLInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 11, 1)
)
convSxLInventoryEntry.setIndexNames(
    (0, "SPEEDCARRIER-MIB", "convSxLInvSlot"),
)
if mibBuilder.loadTexts:
    convSxLInventoryEntry.setStatus("current")


class _ConvSxLInvSlot_Type(Integer32):
    """Custom type convSxLInvSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSxLInvSlot_Type.__name__ = "Integer32"
_ConvSxLInvSlot_Object = MibTableColumn
convSxLInvSlot = _ConvSxLInvSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 11, 1, 2),
    _ConvSxLInvSlot_Type()
)
convSxLInvSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLInvSlot.setStatus("current")


class _ConvSxLModuleSerialNumber_Type(DisplayString):
    """Custom type convSxLModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLModuleSerialNumber_Type.__name__ = "DisplayString"
_ConvSxLModuleSerialNumber_Object = MibTableColumn
convSxLModuleSerialNumber = _ConvSxLModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 11, 1, 3),
    _ConvSxLModuleSerialNumber_Type()
)
convSxLModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLModuleSerialNumber.setStatus("current")


class _ConvSxLSFPPort1SerialNumber_Type(DisplayString):
    """Custom type convSxLSFPPort1SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLSFPPort1SerialNumber_Type.__name__ = "DisplayString"
_ConvSxLSFPPort1SerialNumber_Object = MibTableColumn
convSxLSFPPort1SerialNumber = _ConvSxLSFPPort1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 11, 1, 4),
    _ConvSxLSFPPort1SerialNumber_Type()
)
convSxLSFPPort1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPPort1SerialNumber.setStatus("current")


class _ConvSxLSFPPort2SerialNumber_Type(DisplayString):
    """Custom type convSxLSFPPort2SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLSFPPort2SerialNumber_Type.__name__ = "DisplayString"
_ConvSxLSFPPort2SerialNumber_Object = MibTableColumn
convSxLSFPPort2SerialNumber = _ConvSxLSFPPort2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 11, 1, 5),
    _ConvSxLSFPPort2SerialNumber_Type()
)
convSxLSFPPort2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPPort2SerialNumber.setStatus("current")


class _ConvSxLSFPPort3SerialNumber_Type(DisplayString):
    """Custom type convSxLSFPPort3SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLSFPPort3SerialNumber_Type.__name__ = "DisplayString"
_ConvSxLSFPPort3SerialNumber_Object = MibTableColumn
convSxLSFPPort3SerialNumber = _ConvSxLSFPPort3SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 11, 1, 6),
    _ConvSxLSFPPort3SerialNumber_Type()
)
convSxLSFPPort3SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPPort3SerialNumber.setStatus("current")


class _ConvSxLSFPPort4SerialNumber_Type(DisplayString):
    """Custom type convSxLSFPPort4SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ConvSxLSFPPort4SerialNumber_Type.__name__ = "DisplayString"
_ConvSxLSFPPort4SerialNumber_Object = MibTableColumn
convSxLSFPPort4SerialNumber = _ConvSxLSFPPort4SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 1, 11, 1, 7),
    _ConvSxLSFPPort4SerialNumber_Type()
)
convSxLSFPPort4SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSxLSFPPort4SerialNumber.setStatus("current")
_Multiplexer_ObjectIdentity = ObjectIdentity
multiplexer = _Multiplexer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4)
)
_Amplifier_ObjectIdentity = ObjectIdentity
amplifier = _Amplifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5)
)

# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 40)
)
coldStart.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        "current"
    )

reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 41)
)
reboot.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    reboot.setStatus(
        "current"
    )

fanError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 42)
)
fanError.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    fanError.setStatus(
        "current"
    )

fanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 43)
)
fanOK.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    fanOK.setStatus(
        "current"
    )

powerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 44)
)
powerFailure.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    powerFailure.setStatus(
        "current"
    )

powerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 45)
)
powerOK.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    powerOK.setStatus(
        "current"
    )

highTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 46)
)
highTemp.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    highTemp.setStatus(
        "current"
    )

tempOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 47)
)
tempOK.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    tempOK.setStatus(
        "current"
    )

transceiverRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 48)
)
transceiverRemoved.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    transceiverRemoved.setStatus(
        "current"
    )

transceiverInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 49)
)
transceiverInserted.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    transceiverInserted.setStatus(
        "current"
    )

moduleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 50)
)
moduleInserted.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    moduleInserted.setStatus(
        "current"
    )

moduleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 51)
)
moduleRemoved.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    moduleRemoved.setStatus(
        "current"
    )

portTxUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 52)
)
portTxUp.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    portTxUp.setStatus(
        "current"
    )

portTxDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 53)
)
portTxDown.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    portTxDown.setStatus(
        "current"
    )

portUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 54)
)
portUp.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    portUp.setStatus(
        "current"
    )

portDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 55)
)
portDown.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    portDown.setStatus(
        "current"
    )

txFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 56)
)
txFault.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    txFault.setStatus(
        "current"
    )

badPasswd = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 57)
)
badPasswd.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    badPasswd.setStatus(
        "current"
    )

softwareUpdateReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 58)
)
softwareUpdateReady.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    softwareUpdateReady.setStatus(
        "current"
    )

hardwareTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 59)
)
hardwareTrap.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    hardwareTrap.setStatus(
        "current"
    )

cdrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 60)
)
cdrAlarm.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    cdrAlarm.setStatus(
        "current"
    )

protectionMain = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 61)
)
protectionMain.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    protectionMain.setStatus(
        "current"
    )

protectionBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 62)
)
protectionBackup.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    protectionBackup.setStatus(
        "current"
    )

optRxLevelWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 63)
)
optRxLevelWarning.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    optRxLevelWarning.setStatus(
        "current"
    )

optRxLevelAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 64)
)
optRxLevelAlarm.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    optRxLevelAlarm.setStatus(
        "current"
    )

optRxLevelOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 65)
)
optRxLevelOK.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    optRxLevelOK.setStatus(
        "current"
    )

optTxLevelWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 66)
)
optTxLevelWarning.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    optTxLevelWarning.setStatus(
        "current"
    )

optTxLevelAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 67)
)
optTxLevelAlarm.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    optTxLevelAlarm.setStatus(
        "current"
    )

optTxLevelOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 68)
)
optTxLevelOK.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    optTxLevelOK.setStatus(
        "current"
    )

optTxBiasAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 69)
)
optTxBiasAlarm.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    optTxBiasAlarm.setStatus(
        "current"
    )

optTxBiasOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 70)
)
optTxBiasOK.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    optTxBiasOK.setStatus(
        "current"
    )

optRxPowerOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 71)
)
optRxPowerOverload.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    optRxPowerOverload.setStatus(
        "current"
    )

configError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 72)
)
configError.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    configError.setStatus(
        "current"
    )

configuration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 73)
)
configuration.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    configuration.setStatus(
        "current"
    )

maintenance = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 74)
)
maintenance.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    maintenance.setStatus(
        "current"
    )

ampFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 75)
)
ampFail.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    ampFail.setStatus(
        "current"
    )

ampOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 76)
)
ampOk.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    ampOk.setStatus(
        "current"
    )

dwdmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 77)
)
dwdmAlarm.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    dwdmAlarm.setStatus(
        "current"
    )

dwdmOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 78)
)
dwdmOk.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    dwdmOk.setStatus(
        "current"
    )

firmwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 79)
)
firmwareError.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    firmwareError.setStatus(
        "current"
    )

tuningError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 80)
)
tuningError.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    tuningError.setStatus(
        "current"
    )

encryption = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 81)
)
encryption.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    encryption.setStatus(
        "current"
    )

emergencyShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 82)
)
emergencyShutdown.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"))
)
if mibBuilder.loadTexts:
    emergencyShutdown.setStatus(
        "current"
    )

unspecified = NotificationType(
    (1, 3, 6, 1, 4, 1, 3652, 0, 255)
)
unspecified.setObjects(
      *(("PanDacom-MIB", "descr"),
        ("PanDacom-MIB", "slot"),
        ("PanDacom-MIB", "port"))
)
if mibBuilder.loadTexts:
    unspecified.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPEEDCARRIER-MIB",
    **{"coldStart": coldStart,
       "reboot": reboot,
       "fanError": fanError,
       "fanOK": fanOK,
       "powerFailure": powerFailure,
       "powerOK": powerOK,
       "highTemp": highTemp,
       "tempOK": tempOK,
       "transceiverRemoved": transceiverRemoved,
       "transceiverInserted": transceiverInserted,
       "moduleInserted": moduleInserted,
       "moduleRemoved": moduleRemoved,
       "portTxUp": portTxUp,
       "portTxDown": portTxDown,
       "portUp": portUp,
       "portDown": portDown,
       "txFault": txFault,
       "badPasswd": badPasswd,
       "softwareUpdateReady": softwareUpdateReady,
       "hardwareTrap": hardwareTrap,
       "cdrAlarm": cdrAlarm,
       "protectionMain": protectionMain,
       "protectionBackup": protectionBackup,
       "optRxLevelWarning": optRxLevelWarning,
       "optRxLevelAlarm": optRxLevelAlarm,
       "optRxLevelOK": optRxLevelOK,
       "optTxLevelWarning": optTxLevelWarning,
       "optTxLevelAlarm": optTxLevelAlarm,
       "optTxLevelOK": optTxLevelOK,
       "optTxBiasAlarm": optTxBiasAlarm,
       "optTxBiasOK": optTxBiasOK,
       "optRxPowerOverload": optRxPowerOverload,
       "configError": configError,
       "configuration": configuration,
       "maintenance": maintenance,
       "ampFail": ampFail,
       "ampOk": ampOk,
       "dwdmAlarm": dwdmAlarm,
       "dwdmOk": dwdmOk,
       "firmwareError": firmwareError,
       "tuningError": tuningError,
       "encryption": encryption,
       "emergencyShutdown": emergencyShutdown,
       "unspecified": unspecified,
       "nmSPEEDCARRIER": nmSPEEDCARRIER,
       "nmAgent": nmAgent,
       "nmAgentGeneralInfo": nmAgentGeneralInfo,
       "nmARamdiskVersion": nmARamdiskVersion,
       "nmASlot": nmASlot,
       "nmADate": nmADate,
       "nmATime": nmATime,
       "nmAUpTime": nmAUpTime,
       "nmATemperature": nmATemperature,
       "nmAAlarmState": nmAAlarmState,
       "nmASerialNumber": nmASerialNumber,
       "nmAKernelVersion": nmAKernelVersion,
       "nmASoftwareVersion": nmASoftwareVersion,
       "nmAgentConfig": nmAgentConfig,
       "nmAgentConfigNetwork": nmAgentConfigNetwork,
       "nmAgentConfigNetworkIP": nmAgentConfigNetworkIP,
       "nmAgentConfigNetworkMask": nmAgentConfigNetworkMask,
       "nmAgentConfigNetworkGateway": nmAgentConfigNetworkGateway,
       "nmAgentConfigNetworkIPv6": nmAgentConfigNetworkIPv6,
       "nmAgentConfigNetworkGatewayv6": nmAgentConfigNetworkGatewayv6,
       "nmAgentConfigSnmp": nmAgentConfigSnmp,
       "nmAgentConfigSnmpReadCommunity": nmAgentConfigSnmpReadCommunity,
       "nmAgentConfigSnmpWriteCommunity": nmAgentConfigSnmpWriteCommunity,
       "nmAgentConfigSnmpSysLocation": nmAgentConfigSnmpSysLocation,
       "nmAgentConfigSnmpSysContact": nmAgentConfigSnmpSysContact,
       "nmAgentConfigSnmpTrapSink1": nmAgentConfigSnmpTrapSink1,
       "nmAgentConfigSnmpTrapSink2": nmAgentConfigSnmpTrapSink2,
       "nmAgentConfigSnmpTrapSink3": nmAgentConfigSnmpTrapSink3,
       "nmAgentConfigSnmpTrapSink4": nmAgentConfigSnmpTrapSink4,
       "nmAgentConfigSnmpTrapSink5": nmAgentConfigSnmpTrapSink5,
       "nmAgentConfigSnmpAgent": nmAgentConfigSnmpAgent,
       "nmAgentConfigSNMPv3UserConfigTable": nmAgentConfigSNMPv3UserConfigTable,
       "nmAgentConfigSNMPv3UserConfigEntry": nmAgentConfigSNMPv3UserConfigEntry,
       "nmAgentConfigSNMPv3UserConfigIndex": nmAgentConfigSNMPv3UserConfigIndex,
       "nmAgentConfigSnmpv3UserConfigName": nmAgentConfigSnmpv3UserConfigName,
       "nmAgentConfigSnmpv3UserConfigUserLevel": nmAgentConfigSnmpv3UserConfigUserLevel,
       "nmAgentConfigSnmpv3UserConfigAuthType": nmAgentConfigSnmpv3UserConfigAuthType,
       "nmAgentConfigSnmpv3UserConfigAuthPassPhrase": nmAgentConfigSnmpv3UserConfigAuthPassPhrase,
       "nmAgentConfigSnmpv3UserConfigEncType": nmAgentConfigSnmpv3UserConfigEncType,
       "nmAgentConfigSnmpv3UserConfigPrivPassPhrase": nmAgentConfigSnmpv3UserConfigPrivPassPhrase,
       "nmAgentConfigSlotAlarmsTable": nmAgentConfigSlotAlarmsTable,
       "nmAgentConfigSlotAlarmsEntry": nmAgentConfigSlotAlarmsEntry,
       "nmAgentConfigSlotAlarmsSlotNumber": nmAgentConfigSlotAlarmsSlotNumber,
       "nmAgentConfigSlotAlarmsInsertedCard": nmAgentConfigSlotAlarmsInsertedCard,
       "nmAgentConfigSlotAlarmsConfig": nmAgentConfigSlotAlarmsConfig,
       "nmAgentConfigSlotModulesTable": nmAgentConfigSlotModulesTable,
       "nmAgentConfigSlotModulesEntry": nmAgentConfigSlotModulesEntry,
       "nmAgentConfigModulesSlotNumber": nmAgentConfigModulesSlotNumber,
       "nmAgentConfigModulesInstalledCard": nmAgentConfigModulesInstalledCard,
       "nmAgentConfigModulesExpectedCard": nmAgentConfigModulesExpectedCard,
       "nmAgentConfigModulesSlotText": nmAgentConfigModulesSlotText,
       "nmAgentConfigModulesInstalledState": nmAgentConfigModulesInstalledState,
       "nmAgentConfigAlarmRelay": nmAgentConfigAlarmRelay,
       "nmAgentConfigFAN": nmAgentConfigFAN,
       "nmAgentConfigNtpServer": nmAgentConfigNtpServer,
       "nmAgentConfigTftpServer": nmAgentConfigTftpServer,
       "nmAgentConfigWebServer": nmAgentConfigWebServer,
       "nmAgentConfigMyWebView": nmAgentConfigMyWebView,
       "nmAgentConfigTimezone": nmAgentConfigTimezone,
       "nmAgentConfigAccess": nmAgentConfigAccess,
       "nmAgentConfigCliTimeout": nmAgentConfigCliTimeout,
       "nmAgentConfigRadiusStateConfig": nmAgentConfigRadiusStateConfig,
       "nmAgentConfigNMSState": nmAgentConfigNMSState,
       "nmAgentConfigRadiusServerConfigTable": nmAgentConfigRadiusServerConfigTable,
       "nmAgentConfigRadiusServerConfigEntry": nmAgentConfigRadiusServerConfigEntry,
       "nmAgentConfigRadiusServerConfigNumber": nmAgentConfigRadiusServerConfigNumber,
       "nmAgentConfigRadiusServerConfigIPAddress": nmAgentConfigRadiusServerConfigIPAddress,
       "nmAgentConfigRadiusServerConfigSharedSecret": nmAgentConfigRadiusServerConfigSharedSecret,
       "nmAgentConfigSyslogServerIPAddress": nmAgentConfigSyslogServerIPAddress,
       "nmAgentConfigSyslogSeverity": nmAgentConfigSyslogSeverity,
       "nmAgentConfigSyslogFacility": nmAgentConfigSyslogFacility,
       "nmAgentPorts": nmAgentPorts,
       "nmAgentPortsPortOverviewTable": nmAgentPortsPortOverviewTable,
       "nmAgentPortsPortOverviewEntry": nmAgentPortsPortOverviewEntry,
       "nmAgentPortsIndex": nmAgentPortsIndex,
       "nmAgentPortsSlot": nmAgentPortsSlot,
       "nmAgentPortsPort": nmAgentPortsPort,
       "nmAgentPortsAdminConfig": nmAgentPortsAdminConfig,
       "nmAgentPortsOperStateSFP": nmAgentPortsOperStateSFP,
       "nmAgentPortsAlarmState": nmAgentPortsAlarmState,
       "nmAgentPortsPortType": nmAgentPortsPortType,
       "nmAgentPortsPortDescription": nmAgentPortsPortDescription,
       "nmAgentPortsOperStateCopper": nmAgentPortsOperStateCopper,
       "nmAgentPortsSFPOverviewTable": nmAgentPortsSFPOverviewTable,
       "nmAgentPortsSFPOverviewEntry": nmAgentPortsSFPOverviewEntry,
       "nmAgentPortsSFPIndex": nmAgentPortsSFPIndex,
       "nmAgentPortsSFPSlot": nmAgentPortsSFPSlot,
       "nmAgentPortsSFPPort": nmAgentPortsSFPPort,
       "nmAgentPortsSFPState": nmAgentPortsSFPState,
       "nmAgentPortsDMIState": nmAgentPortsDMIState,
       "nmAgentPortsVendorName": nmAgentPortsVendorName,
       "nmAgentPortsVendorPartNumber": nmAgentPortsVendorPartNumber,
       "nmAgentPortsVendorSerialNumber": nmAgentPortsVendorSerialNumber,
       "nmAgentPortsWavelength": nmAgentPortsWavelength,
       "nmAgentPortsSFPMeassurementTable": nmAgentPortsSFPMeassurementTable,
       "nmAgentPortsSFPMeassurementEntry": nmAgentPortsSFPMeassurementEntry,
       "nmAgentPortsSFPMIndex": nmAgentPortsSFPMIndex,
       "nmAgentPortsSFPMSlot": nmAgentPortsSFPMSlot,
       "nmAgentPortsSFPMPort": nmAgentPortsSFPMPort,
       "nmAgentPortsSFPDMIRxLevel": nmAgentPortsSFPDMIRxLevel,
       "nmAgentPortsSFPDMITxLevel": nmAgentPortsSFPDMITxLevel,
       "nmAgentPortsSFPDMITxBias": nmAgentPortsSFPDMITxBias,
       "nmAgentPortsSFPDMIVcc": nmAgentPortsSFPDMIVcc,
       "nmAgentPortsSFPDMITemp": nmAgentPortsSFPDMITemp,
       "nmAgentPortsSFPAlarmTable": nmAgentPortsSFPAlarmTable,
       "nmAgentPortsSFPAlarmEntry": nmAgentPortsSFPAlarmEntry,
       "nmAgentPortsSFPAIndex": nmAgentPortsSFPAIndex,
       "nmAgentPortsSFPASlot": nmAgentPortsSFPASlot,
       "nmAgentPortsSFPAPort": nmAgentPortsSFPAPort,
       "nmAgentPortsSFPDMIRxLowWarningEvent": nmAgentPortsSFPDMIRxLowWarningEvent,
       "nmAgentPortsSFPDMIRxLowAlarmEvent": nmAgentPortsSFPDMIRxLowAlarmEvent,
       "nmAgentPortsSFPDMITxPowerAlarm": nmAgentPortsSFPDMITxPowerAlarm,
       "nmAgentPortsSFPDMIBiasAlarmEvent": nmAgentPortsSFPDMIBiasAlarmEvent,
       "nmAgentPortsSFPDMIRxHighAlarmEvent": nmAgentPortsSFPDMIRxHighAlarmEvent,
       "nmAgentPortsSFPDWDMTECAlarmEvent": nmAgentPortsSFPDWDMTECAlarmEvent,
       "nmAgentPortsSFPTempAlarmEvent": nmAgentPortsSFPTempAlarmEvent,
       "nmCarrier": nmCarrier,
       "nmCarrierGerneralInfo": nmCarrierGerneralInfo,
       "nmCarrierName": nmCarrierName,
       "nmCarrierType": nmCarrierType,
       "nmPSU1Status": nmPSU1Status,
       "nmPSU2Status": nmPSU2Status,
       "nmFanState": nmFanState,
       "nmCarrierPSU1Type": nmCarrierPSU1Type,
       "nmCarrierPSU2Type": nmCarrierPSU2Type,
       "nmCarrierPSU1Text": nmCarrierPSU1Text,
       "nmCarrierPSU2Text": nmCarrierPSU2Text,
       "nmCarrierPSU3Text": nmCarrierPSU3Text,
       "nmCarrierPSU3Type": nmCarrierPSU3Type,
       "nmPSU3Status": nmPSU3Status,
       "nmCarrierSerialNumber": nmCarrierSerialNumber,
       "nmCarrierAssemblyAlarm": nmCarrierAssemblyAlarm,
       "nmCarrierSlotOverviewTable": nmCarrierSlotOverviewTable,
       "nmCarrierSlotOverviewEntry": nmCarrierSlotOverviewEntry,
       "nmCarrierSlotNumber": nmCarrierSlotNumber,
       "nmCarrierSlotType": nmCarrierSlotType,
       "nmCarrierSlotPassiveText": nmCarrierSlotPassiveText,
       "nmFanOverviewTable": nmFanOverviewTable,
       "nmFanOverviewEntry": nmFanOverviewEntry,
       "nmFanGroupNumber": nmFanGroupNumber,
       "nmFanGroupStatus": nmFanGroupStatus,
       "nmCarrierFWUpdate": nmCarrierFWUpdate,
       "nmCarrierFWUpdateFilename": nmCarrierFWUpdateFilename,
       "nmCarrierFirmwareTransferConfig": nmCarrierFirmwareTransferConfig,
       "nmCarrierFWTransferProgress": nmCarrierFWTransferProgress,
       "nmCarrierFWUpdateConfig": nmCarrierFWUpdateConfig,
       "nmCarrierFWUpdatePolicyTable": nmCarrierFWUpdatePolicyTable,
       "nmCarrierFWUpdatePolicyEntry": nmCarrierFWUpdatePolicyEntry,
       "nmCarrierFWUpdatePolicySlot": nmCarrierFWUpdatePolicySlot,
       "nmCarrierFWUpdatePolicyCardName": nmCarrierFWUpdatePolicyCardName,
       "nmCarrierFWUpdatePolicyConfig": nmCarrierFWUpdatePolicyConfig,
       "nmCarrierFWUpdatePolicyTransferState": nmCarrierFWUpdatePolicyTransferState,
       "nmCarrierConfigTransferTable": nmCarrierConfigTransferTable,
       "nmCarrierConfigTransferEntry": nmCarrierConfigTransferEntry,
       "nmCarrierConfigSlot": nmCarrierConfigSlot,
       "nmCarrierConfigModuleName": nmCarrierConfigModuleName,
       "nmCarrierConfigTransferState": nmCarrierConfigTransferState,
       "nmCarrierConfigTransfer": nmCarrierConfigTransfer,
       "nmCarrierConfigFilename": nmCarrierConfigFilename,
       "nmCarrierConfigActivation": nmCarrierConfigActivation,
       "nmCarrierInventoryTable": nmCarrierInventoryTable,
       "nmCarrierInventoryEntry": nmCarrierInventoryEntry,
       "nmCarrierInventoryIndex": nmCarrierInventoryIndex,
       "nmCarrierInventorySlotNumber": nmCarrierInventorySlotNumber,
       "nmCarrierInventoryPort": nmCarrierInventoryPort,
       "nmCarrierInventoryModuleName": nmCarrierInventoryModuleName,
       "nmCarrierInventoryPartNumber": nmCarrierInventoryPartNumber,
       "nmCarrierInventorySerialNumber": nmCarrierInventorySerialNumber,
       "nmCarrierInventoryFirmwareRelease": nmCarrierInventoryFirmwareRelease,
       "nmCarrierInventoryKernelLoader": nmCarrierInventoryKernelLoader,
       "converter": converter,
       "convSPEEDDUALLINE": convSPEEDDUALLINE,
       "convSxLModuleOverviewTable": convSxLModuleOverviewTable,
       "convSxLModuleOverviewEntry": convSxLModuleOverviewEntry,
       "convSxLMSlot": convSxLMSlot,
       "convSxLMDevice": convSxLMDevice,
       "convSxLMStatus": convSxLMStatus,
       "convSxLMSysUpTime": convSxLMSysUpTime,
       "convSxLMTemp": convSxLMTemp,
       "convSxLMAlarmState": convSxLMAlarmState,
       "convSxLMBootSWVersion": convSxLMBootSWVersion,
       "convSxLMAppSWVersion": convSxLMAppSWVersion,
       "convSxLMHWVersion": convSxLMHWVersion,
       "convSxLMPLDVersion": convSxLMPLDVersion,
       "convSxLMSerialNumber": convSxLMSerialNumber,
       "convSxLSWImagesOverviewTable": convSxLSWImagesOverviewTable,
       "convSxLSWImagesOverviewEntry": convSxLSWImagesOverviewEntry,
       "convSxLSWSlot": convSxLSWSlot,
       "convSxLSWBootImage": convSxLSWBootImage,
       "convSxLSWAppImage1": convSxLSWAppImage1,
       "convSxLSWAppImage2": convSxLSWAppImage2,
       "convSxLSWUploadStatus": convSxLSWUploadStatus,
       "convSxLSWUpdateStatus": convSxLSWUpdateStatus,
       "convSxLModuleConfigTable": convSxLModuleConfigTable,
       "convSxLModuleConfigEntry": convSxLModuleConfigEntry,
       "convSxLMCSlot": convSxLMCSlot,
       "convSxLMIpAddress": convSxLMIpAddress,
       "convSxLMIpNetmask": convSxLMIpNetmask,
       "convSxLMIpGateway": convSxLMIpGateway,
       "convSxLMIpTftpServer": convSxLMIpTftpServer,
       "convSxLMIpTrapSink": convSxLMIpTrapSink,
       "convSxLMSNMPReadCommunity": convSxLMSNMPReadCommunity,
       "convSxLMSNMPWriteCommunity": convSxLMSNMPWriteCommunity,
       "convSxLMTempWarningLevel": convSxLMTempWarningLevel,
       "convSxLMTempAlarmLevel": convSxLMTempAlarmLevel,
       "convSxLMAlarmReport": convSxLMAlarmReport,
       "convSxLMEthPortConfig": convSxLMEthPortConfig,
       "convSxLMEthPortState": convSxLMEthPortState,
       "convSxLMCliUserTimeout": convSxLMCliUserTimeout,
       "convSxLModuleProtectionTable": convSxLModuleProtectionTable,
       "convSxLModuleProtectionEntry": convSxLModuleProtectionEntry,
       "convSxLMPSlot": convSxLMPSlot,
       "convSxLMLinkProtectionConfig": convSxLMLinkProtectionConfig,
       "convSxLMLinkProtectionStatus": convSxLMLinkProtectionStatus,
       "convSxLMLinkProtectionFallback": convSxLMLinkProtectionFallback,
       "convSxLPortOverviewTable": convSxLPortOverviewTable,
       "convSxLPortOverviewEntry": convSxLPortOverviewEntry,
       "convSxLPortIndex": convSxLPortIndex,
       "convSxLSlot": convSxLSlot,
       "convSxLPort": convSxLPort,
       "convSxLDescription": convSxLDescription,
       "convSxLAdminState": convSxLAdminState,
       "convSxLOperState": convSxLOperState,
       "convSxLSFPState": convSxLSFPState,
       "convSxLLLCFState": convSxLLLCFState,
       "convSxLLoopState": convSxLLoopState,
       "convSxLSpeed": convSxLSpeed,
       "convSxLTxPortConnection": convSxLTxPortConnection,
       "convSxLAlarmState": convSxLAlarmState,
       "convSxLDMIState": convSxLDMIState,
       "convSxLPortConfigTable": convSxLPortConfigTable,
       "convSxLPortConfigEntry": convSxLPortConfigEntry,
       "convSxLCPortIndex": convSxLCPortIndex,
       "convSxLCSlot": convSxLCSlot,
       "convSxLCPort": convSxLCPort,
       "convSxLAdminConfig": convSxLAdminConfig,
       "convSxLLLCFConfig": convSxLLLCFConfig,
       "convSxLLoopConfig": convSxLLoopConfig,
       "convSxLSpeedConfig": convSxLSpeedConfig,
       "convSxLPortConnection": convSxLPortConnection,
       "convSxLPortAlarmDeactivation": convSxLPortAlarmDeactivation,
       "convSxLPortAlarmSchedule": convSxLPortAlarmSchedule,
       "convSxSFPIdentifikation": convSxSFPIdentifikation,
       "convSXLSFPDescriptionTable": convSXLSFPDescriptionTable,
       "convSXLSFPDescriptionEntry": convSXLSFPDescriptionEntry,
       "convSxLSFPPortIndex": convSxLSFPPortIndex,
       "convSxLSFPSlot": convSxLSFPSlot,
       "convSxLSFPPort": convSxLSFPPort,
       "convSxLSFPVendor": convSxLSFPVendor,
       "convSxLSFPVendorOUI": convSxLSFPVendorOUI,
       "convSxLSFPVendorCode": convSxLSFPVendorCode,
       "convSxLSFPVendorRevisionCode": convSxLSFPVendorRevisionCode,
       "convSxLSFPVendorDateCode": convSxLSFPVendorDateCode,
       "convSxLSFPVendorSerialNumber": convSxLSFPVendorSerialNumber,
       "convSxLSFPType": convSxLSFPType,
       "convSxLSFPConnector": convSxLSFPConnector,
       "convSxLSFPWavelength": convSxLSFPWavelength,
       "convSxLSFPBitrateTable": convSxLSFPBitrateTable,
       "convSxLSFPBitrateEntry": convSxLSFPBitrateEntry,
       "convSxLSFPBitratePortIndex": convSxLSFPBitratePortIndex,
       "convSxLSFPBitrateSlot": convSxLSFPBitrateSlot,
       "convSxLSFPBitratePort": convSxLSFPBitratePort,
       "convSxLSFPBitrateNominal": convSxLSFPBitrateNominal,
       "convSxLSFPBitrateMax": convSxLSFPBitrateMax,
       "convSxLSFPBitrateMin": convSxLSFPBitrateMin,
       "convSxLSFPLengthTable": convSxLSFPLengthTable,
       "convSxLSFPLengthEntry": convSxLSFPLengthEntry,
       "convSxLSFPLengthPortIndex": convSxLSFPLengthPortIndex,
       "convSxLSFPLengthSlot": convSxLSFPLengthSlot,
       "convSxLSFPLengthPort": convSxLSFPLengthPort,
       "convSxLSFPLength9km": convSxLSFPLength9km,
       "convSxLSFPLength9m": convSxLSFPLength9m,
       "convSxLSFPLength50": convSxLSFPLength50,
       "convSxLSFPLength62": convSxLSFPLength62,
       "convSxLSFPLengthCopper": convSxLSFPLengthCopper,
       "convSxLSFPCompCodes": convSxLSFPCompCodes,
       "convSxLSFPCompCodeSonetTable": convSxLSFPCompCodeSonetTable,
       "convSxLSFPCompCodeSonetEntry": convSxLSFPCompCodeSonetEntry,
       "convSxLSFPCSPortIndex": convSxLSFPCSPortIndex,
       "convSxLSFPCSSlot": convSxLSFPCSSlot,
       "convSxLSFPCSPort": convSxLSFPCSPort,
       "convSxLSFPCSProtocol": convSxLSFPCSProtocol,
       "convSxLSFPCSRange": convSxLSFPCSRange,
       "convSxLSFPCSFiberType": convSxLSFPCSFiberType,
       "convSxLSFPCompCodeGigabitEthernetTable": convSxLSFPCompCodeGigabitEthernetTable,
       "convSxLSFPCompCodeGigabitEthernetEntry": convSxLSFPCompCodeGigabitEthernetEntry,
       "convSxLSFPCGPortIndex": convSxLSFPCGPortIndex,
       "convSxLSFPCGSlot": convSxLSFPCGSlot,
       "convSxLSFPCGPort": convSxLSFPCGPort,
       "convSxLSFPCGType": convSxLSFPCGType,
       "convSxLSFPCompCodeFibreChannelTable": convSxLSFPCompCodeFibreChannelTable,
       "convSxLSFPCompCodeFibreChannelEntry": convSxLSFPCompCodeFibreChannelEntry,
       "convSxLSFPCFcPortIndex": convSxLSFPCFcPortIndex,
       "convSxLSFPCFcSlot": convSxLSFPCFcSlot,
       "convSxLSFPCFcPort": convSxLSFPCFcPort,
       "convSxLSFPCFcMedia": convSxLSFPCFcMedia,
       "convSxLSFPCFcTech": convSxLSFPCFcTech,
       "convSxLSFPCFcLinkLength": convSxLSFPCFcLinkLength,
       "convSxLSFPCFcSpeed": convSxLSFPCFcSpeed,
       "convSxLCopperSFPTable": convSxLCopperSFPTable,
       "convSxLCopperSFPEntry": convSxLCopperSFPEntry,
       "convSxLCuSFPPortIndex": convSxLCuSFPPortIndex,
       "convSxLCuSFPSlot": convSxLCuSFPSlot,
       "convSxLCuSFPPort": convSxLCuSFPPort,
       "convSxLConfigSpeed": convSxLConfigSpeed,
       "convSxLConfigDuplex": convSxLConfigDuplex,
       "convSxLCuPhyId": convSxLCuPhyId,
       "convSxLCuSFPLink": convSxLCuSFPLink,
       "convSxLCuSFPSpeed": convSxLCuSFPSpeed,
       "convSxLCuSFPDuplex": convSxLCuSFPDuplex,
       "convSxLCuSFPAutoMDIx": convSxLCuSFPAutoMDIx,
       "convSxLCuSFPConfigMode": convSxLCuSFPConfigMode,
       "convSxLDWDMSFPTable": convSxLDWDMSFPTable,
       "convSxLDWDMSFPEntry": convSxLDWDMSFPEntry,
       "convSxLDWDMPortIndex": convSxLDWDMPortIndex,
       "convSxLDWDMSlot": convSxLDWDMSlot,
       "convSxLDWDMPort": convSxLDWDMPort,
       "convSxLDWDMPowerClass": convSxLDWDMPowerClass,
       "convSxLDWDMMaxSupplyCurrent": convSxLDWDMMaxSupplyCurrent,
       "convSxLChannelSpacing": convSxLChannelSpacing,
       "convSxLNumberofChannels": convSxLNumberofChannels,
       "convSxLSFPDMIParamTable": convSxLSFPDMIParamTable,
       "convSxLSFPDMIParamEntry": convSxLSFPDMIParamEntry,
       "convSxLSFPDMIPortIndex": convSxLSFPDMIPortIndex,
       "convSxLSFPDMISlot": convSxLSFPDMISlot,
       "convSxLSFPDMIPort": convSxLSFPDMIPort,
       "convSxLSFPDMIRxLevel": convSxLSFPDMIRxLevel,
       "convSxLSFPDMIRxHighAlarm": convSxLSFPDMIRxHighAlarm,
       "convSxLSFPDMITxLevel": convSxLSFPDMITxLevel,
       "convSxLSFPDMITxBias": convSxLSFPDMITxBias,
       "convSxLSFPDMIVcc": convSxLSFPDMIVcc,
       "convSxLSFPDMITemp": convSxLSFPDMITemp,
       "convSxLSFPDMIThresholdTable": convSxLSFPDMIThresholdTable,
       "convSxLSFPDMIThresholdEntry": convSxLSFPDMIThresholdEntry,
       "convSxLSFPDMITPortIndex": convSxLSFPDMITPortIndex,
       "convSxLSFPDMITSlot": convSxLSFPDMITSlot,
       "convSxLSFPDMITPort": convSxLSFPDMITPort,
       "convSxLSFPDMITRxLowThresholdWarningLevel": convSxLSFPDMITRxLowThresholdWarningLevel,
       "convSxLSFPDMITRxLowThresholdAlarmLevel": convSxLSFPDMITRxLowThresholdAlarmLevel,
       "convSxLSFPDMITTxLowThresholdWarningLevel": convSxLSFPDMITTxLowThresholdWarningLevel,
       "convSxLSFPDMITTxLowThresholdAlarmLevel": convSxLSFPDMITTxLowThresholdAlarmLevel,
       "convSxLSFPDMITThresholdsUsage": convSxLSFPDMITThresholdsUsage,
       "convSxLPortEventTable": convSxLPortEventTable,
       "convSxLPortEventEntry": convSxLPortEventEntry,
       "convSxLSFPEPortIndex": convSxLSFPEPortIndex,
       "convSxLSFPESlot": convSxLSFPESlot,
       "convSxLSFPEPort": convSxLSFPEPort,
       "convSxLSFPDMIRxLowWarningEvent": convSxLSFPDMIRxLowWarningEvent,
       "convSxLSFPDMIRxLowAlarmEvent": convSxLSFPDMIRxLowAlarmEvent,
       "convSxLSFPDMITxLowWarningEvent": convSxLSFPDMITxLowWarningEvent,
       "convSxLSFPDMITxLowAlarmEvent": convSxLSFPDMITxLowAlarmEvent,
       "convSxLSFPDMIBiasAlarmEvent": convSxLSFPDMIBiasAlarmEvent,
       "convSxLSFPDMIRxHighAlarmEvent": convSxLSFPDMIRxHighAlarmEvent,
       "convSxLSFPDWDMLaserTHighAlarmEvent": convSxLSFPDWDMLaserTHighAlarmEvent,
       "convSxLSFPDWDMLaserTLowAlarmEvent": convSxLSFPDWDMLaserTLowAlarmEvent,
       "convSxLSFPDWDMTECHighAlarmEvent": convSxLSFPDWDMTECHighAlarmEvent,
       "convSxLSFPDWDMTECLowAlarmEvent": convSxLSFPDWDMTECLowAlarmEvent,
       "convSxLSFPDMITempHighWarningEvent": convSxLSFPDMITempHighWarningEvent,
       "convSxLSFPDMITempHighAlarmEvent": convSxLSFPDMITempHighAlarmEvent,
       "convSxLInventoryTable": convSxLInventoryTable,
       "convSxLInventoryEntry": convSxLInventoryEntry,
       "convSxLInvSlot": convSxLInvSlot,
       "convSxLModuleSerialNumber": convSxLModuleSerialNumber,
       "convSxLSFPPort1SerialNumber": convSxLSFPPort1SerialNumber,
       "convSxLSFPPort2SerialNumber": convSxLSFPPort2SerialNumber,
       "convSxLSFPPort3SerialNumber": convSxLSFPPort3SerialNumber,
       "convSxLSFPPort4SerialNumber": convSxLSFPPort4SerialNumber,
       "multiplexer": multiplexer,
       "amplifier": amplifier}
)
