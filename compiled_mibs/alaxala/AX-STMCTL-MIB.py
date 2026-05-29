# SNMP MIB module (AX-STMCTL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-STMCTL-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

axStormControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60)
)
if mibBuilder.loadTexts:
    axStormControl.setRevisions(
        ("2015-12-25 00:00",
         "2015-12-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxStormControlNotifications_ObjectIdentity = ObjectIdentity
axStormControlNotifications = _AxStormControlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0)
)
_AxStormControlConformance_ObjectIdentity = ObjectIdentity
axStormControlConformance = _AxStormControlConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 1000)
)
_AxStormControlCompliances_ObjectIdentity = ObjectIdentity
axStormControlCompliances = _AxStormControlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 1000, 1)
)
_AxStormControlGroups_ObjectIdentity = ObjectIdentity
axStormControlGroups = _AxStormControlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 1000, 2)
)

# Managed Objects groups


# Notification objects

axBroadcastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0, 1)
)
axBroadcastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axBroadcastStormDetectTrap.setStatus(
        "current"
    )

axMulticastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0, 2)
)
axMulticastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axMulticastStormDetectTrap.setStatus(
        "current"
    )

axUnicastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0, 3)
)
axUnicastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axUnicastStormDetectTrap.setStatus(
        "current"
    )

axBroadcastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0, 4)
)
axBroadcastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axBroadcastStormPortInactivateTrap.setStatus(
        "current"
    )

axMulticastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0, 5)
)
axMulticastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axMulticastStormPortInactivateTrap.setStatus(
        "current"
    )

axUnicastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0, 6)
)
axUnicastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axUnicastStormPortInactivateTrap.setStatus(
        "current"
    )

axBroadcastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0, 7)
)
axBroadcastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axBroadcastStormRecoverTrap.setStatus(
        "current"
    )

axMulticastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0, 8)
)
axMulticastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axMulticastStormRecoverTrap.setStatus(
        "current"
    )

axUnicastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 0, 9)
)
axUnicastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axUnicastStormRecoverTrap.setStatus(
        "current"
    )


# Notifications groups

axStormControlNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 1000, 2, 10)
)
axStormControlNotificationGroup.setObjects(
      *(("AX-STMCTL-MIB", "axBroadcastStormDetectTrap"),
        ("AX-STMCTL-MIB", "axMulticastStormDetectTrap"),
        ("AX-STMCTL-MIB", "axUnicastStormDetectTrap"),
        ("AX-STMCTL-MIB", "axBroadcastStormPortInactivateTrap"),
        ("AX-STMCTL-MIB", "axMulticastStormPortInactivateTrap"),
        ("AX-STMCTL-MIB", "axUnicastStormPortInactivateTrap"),
        ("AX-STMCTL-MIB", "axBroadcastStormRecoverTrap"),
        ("AX-STMCTL-MIB", "axMulticastStormRecoverTrap"),
        ("AX-STMCTL-MIB", "axUnicastStormRecoverTrap"))
)
if mibBuilder.loadTexts:
    axStormControlNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axStormControlCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 60, 1000, 1, 1)
)
axStormControlCompliance.setObjects(
    ("AX-STMCTL-MIB", "axStormControlNotificationGroup")
)
if mibBuilder.loadTexts:
    axStormControlCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-STMCTL-MIB",
    **{"axStormControl": axStormControl,
       "axStormControlNotifications": axStormControlNotifications,
       "axBroadcastStormDetectTrap": axBroadcastStormDetectTrap,
       "axMulticastStormDetectTrap": axMulticastStormDetectTrap,
       "axUnicastStormDetectTrap": axUnicastStormDetectTrap,
       "axBroadcastStormPortInactivateTrap": axBroadcastStormPortInactivateTrap,
       "axMulticastStormPortInactivateTrap": axMulticastStormPortInactivateTrap,
       "axUnicastStormPortInactivateTrap": axUnicastStormPortInactivateTrap,
       "axBroadcastStormRecoverTrap": axBroadcastStormRecoverTrap,
       "axMulticastStormRecoverTrap": axMulticastStormRecoverTrap,
       "axUnicastStormRecoverTrap": axUnicastStormRecoverTrap,
       "axStormControlConformance": axStormControlConformance,
       "axStormControlCompliances": axStormControlCompliances,
       "axStormControlCompliance": axStormControlCompliance,
       "axStormControlGroups": axStormControlGroups,
       "axStormControlNotificationGroup": axStormControlNotificationGroup}
)
