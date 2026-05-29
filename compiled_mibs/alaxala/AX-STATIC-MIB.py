# SNMP MIB module (AX-STATIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-STATIC-MIB

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

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

axStatic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38)
)
if mibBuilder.loadTexts:
    axStatic.setRevisions(
        ("2015-05-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxStaticGatewayTable_Object = MibTable
axStaticGatewayTable = _AxStaticGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1)
)
if mibBuilder.loadTexts:
    axStaticGatewayTable.setStatus("current")
_AxStaticGatewayEntry_Object = MibTableRow
axStaticGatewayEntry = _AxStaticGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1, 1)
)
axStaticGatewayEntry.setIndexNames(
    (0, "AX-STATIC-MIB", "axStaticGatewayVRFIndex"),
    (0, "AX-STATIC-MIB", "axStaticGatewayAddr"),
)
if mibBuilder.loadTexts:
    axStaticGatewayEntry.setStatus("current")
_AxStaticGatewayVRFIndex_Type = Integer32
_AxStaticGatewayVRFIndex_Object = MibTableColumn
axStaticGatewayVRFIndex = _AxStaticGatewayVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1, 1, 1),
    _AxStaticGatewayVRFIndex_Type()
)
axStaticGatewayVRFIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axStaticGatewayVRFIndex.setStatus("current")
_AxStaticGatewayAddr_Type = IpAddress
_AxStaticGatewayAddr_Object = MibTableColumn
axStaticGatewayAddr = _AxStaticGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1, 1, 2),
    _AxStaticGatewayAddr_Type()
)
axStaticGatewayAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axStaticGatewayAddr.setStatus("current")


class _AxStaticGatewayState_Type(Integer32):
    """Custom type axStaticGatewayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 2))
    )


_AxStaticGatewayState_Type.__name__ = "Integer32"
_AxStaticGatewayState_Object = MibTableColumn
axStaticGatewayState = _AxStaticGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1, 1, 3),
    _AxStaticGatewayState_Type()
)
axStaticGatewayState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axStaticGatewayState.setStatus("current")
_AxStaticTrap_ObjectIdentity = ObjectIdentity
axStaticTrap = _AxStaticTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 2)
)
_AxStaticTrapsPrefix_ObjectIdentity = ObjectIdentity
axStaticTrapsPrefix = _AxStaticTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 2, 0)
)
_AxStaticIpv6GatewayTable_Object = MibTable
axStaticIpv6GatewayTable = _AxStaticIpv6GatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 3)
)
if mibBuilder.loadTexts:
    axStaticIpv6GatewayTable.setStatus("current")
_AxStaticIpv6GatewayEntry_Object = MibTableRow
axStaticIpv6GatewayEntry = _AxStaticIpv6GatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 3, 1)
)
axStaticIpv6GatewayEntry.setIndexNames(
    (0, "AX-STATIC-MIB", "axStaticIpv6GatewayVRFIndex"),
    (0, "AX-STATIC-MIB", "axStaticIpv6GatewayIfindex"),
    (0, "AX-STATIC-MIB", "axStaticIpv6GatewayAddr"),
)
if mibBuilder.loadTexts:
    axStaticIpv6GatewayEntry.setStatus("current")
_AxStaticIpv6GatewayVRFIndex_Type = Integer32
_AxStaticIpv6GatewayVRFIndex_Object = MibTableColumn
axStaticIpv6GatewayVRFIndex = _AxStaticIpv6GatewayVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 3, 1, 1),
    _AxStaticIpv6GatewayVRFIndex_Type()
)
axStaticIpv6GatewayVRFIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axStaticIpv6GatewayVRFIndex.setStatus("current")
_AxStaticIpv6GatewayIfindex_Type = Integer32
_AxStaticIpv6GatewayIfindex_Object = MibTableColumn
axStaticIpv6GatewayIfindex = _AxStaticIpv6GatewayIfindex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 3, 1, 2),
    _AxStaticIpv6GatewayIfindex_Type()
)
axStaticIpv6GatewayIfindex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axStaticIpv6GatewayIfindex.setStatus("current")
_AxStaticIpv6GatewayAddr_Type = Ipv6Address
_AxStaticIpv6GatewayAddr_Object = MibTableColumn
axStaticIpv6GatewayAddr = _AxStaticIpv6GatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 3, 1, 3),
    _AxStaticIpv6GatewayAddr_Type()
)
axStaticIpv6GatewayAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axStaticIpv6GatewayAddr.setStatus("current")


class _AxStaticIpv6GatewayState_Type(Integer32):
    """Custom type axStaticIpv6GatewayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 2))
    )


_AxStaticIpv6GatewayState_Type.__name__ = "Integer32"
_AxStaticIpv6GatewayState_Object = MibTableColumn
axStaticIpv6GatewayState = _AxStaticIpv6GatewayState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 3, 1, 4),
    _AxStaticIpv6GatewayState_Type()
)
axStaticIpv6GatewayState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axStaticIpv6GatewayState.setStatus("current")
_AxStaticConformance_ObjectIdentity = ObjectIdentity
axStaticConformance = _AxStaticConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1000)
)
_AxStaticCompliances_ObjectIdentity = ObjectIdentity
axStaticCompliances = _AxStaticCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1000, 1)
)
_AxStaticGroups_ObjectIdentity = ObjectIdentity
axStaticGroups = _AxStaticGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1000, 2)
)

# Managed Objects groups

axStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1000, 2, 1)
)
axStaticGroup.setObjects(
      *(("AX-STATIC-MIB", "axStaticGatewayVRFIndex"),
        ("AX-STATIC-MIB", "axStaticGatewayAddr"),
        ("AX-STATIC-MIB", "axStaticGatewayState"),
        ("AX-STATIC-MIB", "axStaticIpv6GatewayVRFIndex"),
        ("AX-STATIC-MIB", "axStaticIpv6GatewayIfindex"),
        ("AX-STATIC-MIB", "axStaticIpv6GatewayAddr"),
        ("AX-STATIC-MIB", "axStaticIpv6GatewayState"))
)
if mibBuilder.loadTexts:
    axStaticGroup.setStatus("current")


# Notification objects

axStaticGatewayStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 2, 0, 1)
)
axStaticGatewayStateChange.setObjects(
      *(("AX-STATIC-MIB", "axStaticGatewayVRFIndex"),
        ("AX-STATIC-MIB", "axStaticGatewayAddr"),
        ("AX-STATIC-MIB", "axStaticGatewayState"))
)
if mibBuilder.loadTexts:
    axStaticGatewayStateChange.setStatus(
        "current"
    )

axStaticIpv6GatewayStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 2, 0, 2)
)
axStaticIpv6GatewayStateChange.setObjects(
      *(("AX-STATIC-MIB", "axStaticIpv6GatewayVRFIndex"),
        ("AX-STATIC-MIB", "axStaticIpv6GatewayIfindex"),
        ("AX-STATIC-MIB", "axStaticIpv6GatewayAddr"),
        ("AX-STATIC-MIB", "axStaticIpv6GatewayState"))
)
if mibBuilder.loadTexts:
    axStaticIpv6GatewayStateChange.setStatus(
        "current"
    )


# Notifications groups

axStaticTrapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1000, 2, 100)
)
axStaticTrapNotificationGroup.setObjects(
      *(("AX-STATIC-MIB", "axStaticGatewayStateChange"),
        ("AX-STATIC-MIB", "axStaticIpv6GatewayStateChange"))
)
if mibBuilder.loadTexts:
    axStaticTrapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axStaticCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 38, 1000, 1, 1)
)
axStaticCompliance.setObjects(
      *(("AX-STATIC-MIB", "axStaticGroup"),
        ("AX-STATIC-MIB", "axStaticTrapNotificationGroup"))
)
if mibBuilder.loadTexts:
    axStaticCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-STATIC-MIB",
    **{"axStatic": axStatic,
       "axStaticGatewayTable": axStaticGatewayTable,
       "axStaticGatewayEntry": axStaticGatewayEntry,
       "axStaticGatewayVRFIndex": axStaticGatewayVRFIndex,
       "axStaticGatewayAddr": axStaticGatewayAddr,
       "axStaticGatewayState": axStaticGatewayState,
       "axStaticTrap": axStaticTrap,
       "axStaticTrapsPrefix": axStaticTrapsPrefix,
       "axStaticGatewayStateChange": axStaticGatewayStateChange,
       "axStaticIpv6GatewayStateChange": axStaticIpv6GatewayStateChange,
       "axStaticIpv6GatewayTable": axStaticIpv6GatewayTable,
       "axStaticIpv6GatewayEntry": axStaticIpv6GatewayEntry,
       "axStaticIpv6GatewayVRFIndex": axStaticIpv6GatewayVRFIndex,
       "axStaticIpv6GatewayIfindex": axStaticIpv6GatewayIfindex,
       "axStaticIpv6GatewayAddr": axStaticIpv6GatewayAddr,
       "axStaticIpv6GatewayState": axStaticIpv6GatewayState,
       "axStaticConformance": axStaticConformance,
       "axStaticCompliances": axStaticCompliances,
       "axStaticCompliance": axStaticCompliance,
       "axStaticGroups": axStaticGroups,
       "axStaticGroup": axStaticGroup,
       "axStaticTrapNotificationGroup": axStaticTrapNotificationGroup}
)
