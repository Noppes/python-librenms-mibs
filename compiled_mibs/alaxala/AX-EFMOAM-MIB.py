# SNMP MIB module (AX-EFMOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-EFMOAM-MIB

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

axEfmoam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 81)
)
if mibBuilder.loadTexts:
    axEfmoam.setRevisions(
        ("2015-12-25 00:00",
         "2015-04-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxEfmoamNotifications_ObjectIdentity = ObjectIdentity
axEfmoamNotifications = _AxEfmoamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 81, 0)
)
_AxEfmoamConformance_ObjectIdentity = ObjectIdentity
axEfmoamConformance = _AxEfmoamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 81, 1000)
)
_AxEfmoamCompliances_ObjectIdentity = ObjectIdentity
axEfmoamCompliances = _AxEfmoamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 81, 1000, 1)
)
_AxEfmoamGroups_ObjectIdentity = ObjectIdentity
axEfmoamGroups = _AxEfmoamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 81, 1000, 2)
)

# Managed Objects groups


# Notification objects

axEfmoamUdldPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 81, 0, 1)
)
axEfmoamUdldPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axEfmoamUdldPortInactivateTrap.setStatus(
        "current"
    )

axEfmoamLoopDetectPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 81, 0, 2)
)
axEfmoamLoopDetectPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axEfmoamLoopDetectPortInactivateTrap.setStatus(
        "current"
    )


# Notifications groups

axEfmoamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 81, 1000, 2, 10)
)
axEfmoamNotificationGroup.setObjects(
      *(("AX-EFMOAM-MIB", "axEfmoamUdldPortInactivateTrap"),
        ("AX-EFMOAM-MIB", "axEfmoamLoopDetectPortInactivateTrap"))
)
if mibBuilder.loadTexts:
    axEfmoamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axEfmoamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 81, 1000, 1, 1)
)
axEfmoamCompliance.setObjects(
    ("AX-EFMOAM-MIB", "axEfmoamNotificationGroup")
)
if mibBuilder.loadTexts:
    axEfmoamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-EFMOAM-MIB",
    **{"axEfmoam": axEfmoam,
       "axEfmoamNotifications": axEfmoamNotifications,
       "axEfmoamUdldPortInactivateTrap": axEfmoamUdldPortInactivateTrap,
       "axEfmoamLoopDetectPortInactivateTrap": axEfmoamLoopDetectPortInactivateTrap,
       "axEfmoamConformance": axEfmoamConformance,
       "axEfmoamCompliances": axEfmoamCompliances,
       "axEfmoamCompliance": axEfmoamCompliance,
       "axEfmoamGroups": axEfmoamGroups,
       "axEfmoamNotificationGroup": axEfmoamNotificationGroup}
)
