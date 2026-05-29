# SNMP MIB module (A3COM0004-GENERIC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\3com\A3COM0004-GENERIC

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

(generic,) = mibBuilder.importSymbols(
    "A3Com-products-MIB",
    "generic")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2)
)
_SysLoader_ObjectIdentity = ObjectIdentity
sysLoader = _SysLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 3)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 4)
)
_Gauges_ObjectIdentity = ObjectIdentity
gauges = _Gauges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 5)
)
_AsciiAgent_ObjectIdentity = ObjectIdentity
asciiAgent = _AsciiAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 6)
)
_SerialIf_ObjectIdentity = ObjectIdentity
serialIf = _SerialIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 7)
)
_RepeaterMgmt_ObjectIdentity = ObjectIdentity
repeaterMgmt = _RepeaterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8)
)
_EndStation_ObjectIdentity = ObjectIdentity
endStation = _EndStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 9)
)
_LocalSnmp_ObjectIdentity = ObjectIdentity
localSnmp = _LocalSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 10)
)
_Manager_ObjectIdentity = ObjectIdentity
manager = _Manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 11)
)
_UnusedGeneric12_ObjectIdentity = ObjectIdentity
unusedGeneric12 = _UnusedGeneric12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 12)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 14)
)
_MrmResilience_ObjectIdentity = ObjectIdentity
mrmResilience = _MrmResilience_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 15)
)
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 16)
)
_MultiRepeater_ObjectIdentity = ObjectIdentity
multiRepeater = _MultiRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17)
)
_BridgeMgmt_ObjectIdentity = ObjectIdentity
bridgeMgmt = _BridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18)
)
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 19)
)
_Poll_ObjectIdentity = ObjectIdentity
poll = _Poll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 20)
)
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 21)
)
_SecurePort_ObjectIdentity = ObjectIdentity
securePort = _SecurePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 22)
)
_AlertLed_ObjectIdentity = ObjectIdentity
alertLed = _AlertLed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 23)
)
_RemoteControl_ObjectIdentity = ObjectIdentity
remoteControl = _RemoteControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 24)
)
_RmonExtensions_ObjectIdentity = ObjectIdentity
rmonExtensions = _RmonExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 25)
)
_Rfc1516extensions_ObjectIdentity = ObjectIdentity
rfc1516extensions = _Rfc1516extensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 26)
)
_SuperStackIIconfig_ObjectIdentity = ObjectIdentity
superStackIIconfig = _SuperStackIIconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 27)
)
_ExtendedIfInfo_ObjectIdentity = ObjectIdentity
extendedIfInfo = _ExtendedIfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 28)
)
_A3ComVlan_ObjectIdentity = ObjectIdentity
a3ComVlan = _A3ComVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 29)
)
_VlanServerClient_ObjectIdentity = ObjectIdentity
vlanServerClient = _VlanServerClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 30)
)
_SegmentLoadBalancing_ObjectIdentity = ObjectIdentity
segmentLoadBalancing = _SegmentLoadBalancing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 31)
)
_VirtualFileSystem_ObjectIdentity = ObjectIdentity
virtualFileSystem = _VirtualFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 32)
)
_SmartAutosensing_ObjectIdentity = ObjectIdentity
smartAutosensing = _SmartAutosensing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 33)
)
_Brasica2_ObjectIdentity = ObjectIdentity
brasica2 = _Brasica2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 34)
)
_SmaVlanSupport_ObjectIdentity = ObjectIdentity
smaVlanSupport = _SmaVlanSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 35)
)
_A3ComBridgeExt_ObjectIdentity = ObjectIdentity
a3ComBridgeExt = _A3ComBridgeExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 36)
)
_IgmpMIB_ObjectIdentity = ObjectIdentity
igmpMIB = _IgmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 37)
)
_MibSummary_ObjectIdentity = ObjectIdentity
mibSummary = _MibSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 38)
)
_QosProfiles_ObjectIdentity = ObjectIdentity
qosProfiles = _QosProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 39)
)
_L4Redirect_ObjectIdentity = ObjectIdentity
l4Redirect = _L4Redirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 40)
)
_A3ComTrafficStats_ObjectIdentity = ObjectIdentity
a3ComTrafficStats = _A3ComTrafficStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 41)
)
_A3ComRadiusMIB_ObjectIdentity = ObjectIdentity
a3ComRadiusMIB = _A3ComRadiusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 42)
)
_A3ComBackup_mib_ObjectIdentity = ObjectIdentity
a3ComBackup_mib = _A3ComBackup_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 43)
)
_A3comLicenseGroup_ObjectIdentity = ObjectIdentity
a3comLicenseGroup = _A3comLicenseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 44)
)
_A3ComPowerEthernetExt_ObjectIdentity = ObjectIdentity
a3ComPowerEthernetExt = _A3ComPowerEthernetExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 45)
)
_A3ComQBridgeMIB_ObjectIdentity = ObjectIdentity
a3ComQBridgeMIB = _A3ComQBridgeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 46)
)
_A3ComFabric_ObjectIdentity = ObjectIdentity
a3ComFabric = _A3ComFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 47)
)
_A3ComLinkAgg_ObjectIdentity = ObjectIdentity
a3ComLinkAgg = _A3ComLinkAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 48)
)
_A3ComPaeMIB_ObjectIdentity = ObjectIdentity
a3ComPaeMIB = _A3ComPaeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 49)
)
_A3ComSntpGroup_ObjectIdentity = ObjectIdentity
a3ComSntpGroup = _A3ComSntpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 50)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM0004-GENERIC",
    **{"setup": setup,
       "sysLoader": sysLoader,
       "security": security,
       "gauges": gauges,
       "asciiAgent": asciiAgent,
       "serialIf": serialIf,
       "repeaterMgmt": repeaterMgmt,
       "endStation": endStation,
       "localSnmp": localSnmp,
       "manager": manager,
       "unusedGeneric12": unusedGeneric12,
       "chassis": chassis,
       "mrmResilience": mrmResilience,
       "tokenRing": tokenRing,
       "multiRepeater": multiRepeater,
       "bridgeMgmt": bridgeMgmt,
       "fault": fault,
       "poll": poll,
       "powerSupply": powerSupply,
       "securePort": securePort,
       "alertLed": alertLed,
       "remoteControl": remoteControl,
       "rmonExtensions": rmonExtensions,
       "rfc1516extensions": rfc1516extensions,
       "superStackIIconfig": superStackIIconfig,
       "extendedIfInfo": extendedIfInfo,
       "a3ComVlan": a3ComVlan,
       "vlanServerClient": vlanServerClient,
       "segmentLoadBalancing": segmentLoadBalancing,
       "virtualFileSystem": virtualFileSystem,
       "smartAutosensing": smartAutosensing,
       "brasica2": brasica2,
       "smaVlanSupport": smaVlanSupport,
       "a3ComBridgeExt": a3ComBridgeExt,
       "igmpMIB": igmpMIB,
       "mibSummary": mibSummary,
       "qosProfiles": qosProfiles,
       "l4Redirect": l4Redirect,
       "a3ComTrafficStats": a3ComTrafficStats,
       "a3ComRadiusMIB": a3ComRadiusMIB,
       "a3ComBackup-mib": a3ComBackup_mib,
       "a3comLicenseGroup": a3comLicenseGroup,
       "a3ComPowerEthernetExt": a3ComPowerEthernetExt,
       "a3ComQBridgeMIB": a3ComQBridgeMIB,
       "a3ComFabric": a3ComFabric,
       "a3ComLinkAgg": a3ComLinkAgg,
       "a3ComPaeMIB": a3ComPaeMIB,
       "a3ComSntpGroup": a3ComSntpGroup}
)
