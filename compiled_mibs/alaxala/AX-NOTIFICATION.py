# SNMP MIB module (AX-NOTIFICATION) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-NOTIFICATION

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

axFrameError = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71)
)
if mibBuilder.loadTexts:
    axFrameError.setRevisions(
        ("2013-02-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxFrameErrorTraps_ObjectIdentity = ObjectIdentity
axFrameErrorTraps = _AxFrameErrorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71, 1)
)
_AxFrameErrorTrapsPrefix_ObjectIdentity = ObjectIdentity
axFrameErrorTrapsPrefix = _AxFrameErrorTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71, 1, 0)
)
_AxFrameErrorConformance_ObjectIdentity = ObjectIdentity
axFrameErrorConformance = _AxFrameErrorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71, 1000)
)
_AxFrameErrorCompliances_ObjectIdentity = ObjectIdentity
axFrameErrorCompliances = _AxFrameErrorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71, 1000, 1)
)
_AxFrameErrorGroups_ObjectIdentity = ObjectIdentity
axFrameErrorGroups = _AxFrameErrorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71, 1000, 2)
)

# Managed Objects groups


# Notification objects

axFrameErrorReceiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71, 1, 0, 1)
)
axFrameErrorReceiveTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axFrameErrorReceiveTrap.setStatus(
        "current"
    )

axFrameErrorSendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71, 1, 0, 2)
)
axFrameErrorSendTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    axFrameErrorSendTrap.setStatus(
        "current"
    )


# Notifications groups

axFrameErrorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71, 1000, 2, 10)
)
axFrameErrorNotificationGroup.setObjects(
      *(("AX-NOTIFICATION", "axFrameErrorReceiveTrap"),
        ("AX-NOTIFICATION", "axFrameErrorSendTrap"))
)
if mibBuilder.loadTexts:
    axFrameErrorNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axFrameErrorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 71, 1000, 1, 1)
)
axFrameErrorCompliance.setObjects(
    ("AX-NOTIFICATION", "axFrameErrorNotificationGroup")
)
if mibBuilder.loadTexts:
    axFrameErrorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-NOTIFICATION",
    **{"axFrameError": axFrameError,
       "axFrameErrorTraps": axFrameErrorTraps,
       "axFrameErrorTrapsPrefix": axFrameErrorTrapsPrefix,
       "axFrameErrorReceiveTrap": axFrameErrorReceiveTrap,
       "axFrameErrorSendTrap": axFrameErrorSendTrap,
       "axFrameErrorConformance": axFrameErrorConformance,
       "axFrameErrorCompliances": axFrameErrorCompliances,
       "axFrameErrorCompliance": axFrameErrorCompliance,
       "axFrameErrorGroups": axFrameErrorGroups,
       "axFrameErrorNotificationGroup": axFrameErrorNotificationGroup}
)
