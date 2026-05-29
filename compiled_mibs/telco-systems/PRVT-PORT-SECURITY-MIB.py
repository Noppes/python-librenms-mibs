# SNMP MIB module (PRVT-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-PORT-SECURITY-MIB

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

(configL2IfaceEnable,
 switch) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "configL2IfaceEnable",
    "switch")

(dot1qTpFdbStatus,
 dot1qVlanStatus) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qTpFdbStatus",
    "dot1qVlanStatus")

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

prvtPortSecurityMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109)
)
if mibBuilder.loadTexts:
    prvtPortSecurityMib.setRevisions(
        ("2008-06-18 00:00",
         "2005-02-16 00:00",
         "2004-05-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtPortSECNotifications_ObjectIdentity = ObjectIdentity
prvtPortSECNotifications = _PrvtPortSECNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0)
)
_PrvtPortSECObjects_ObjectIdentity = ObjectIdentity
prvtPortSECObjects = _PrvtPortSECObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1)
)
_PrvtPortSECConformance_ObjectIdentity = ObjectIdentity
prvtPortSECConformance = _PrvtPortSECConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 2)
)
_PrvtPortSECMIBGroups_ObjectIdentity = ObjectIdentity
prvtPortSECMIBGroups = _PrvtPortSECMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 2, 2)
)

# Managed Objects groups


# Notification objects

prvtPortSECViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0, 1)
)
prvtPortSECViolation.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qVlanStatus"),
        ("Q-BRIDGE-MIB", "dot1qTpFdbStatus"),
        ("PRVT-SWITCH-MIB", "configL2IfaceEnable"))
)
if mibBuilder.loadTexts:
    prvtPortSECViolation.setStatus(
        "current"
    )

prvtDuplicatedMACAddressAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0, 2)
)
prvtDuplicatedMACAddressAlarm.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qVlanStatus"),
        ("Q-BRIDGE-MIB", "dot1qTpFdbStatus"),
        ("PRVT-SWITCH-MIB", "configL2IfaceEnable"))
)
if mibBuilder.loadTexts:
    prvtDuplicatedMACAddressAlarm.setStatus(
        "current"
    )


# Notifications groups

prvtPortSECNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 2, 2, 1)
)
prvtPortSECNotificationGroup.setObjects(
    ("PRVT-PORT-SECURITY-MIB", "prvtPortSECViolation")
)
if mibBuilder.loadTexts:
    prvtPortSECNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-PORT-SECURITY-MIB",
    **{"prvtPortSecurityMib": prvtPortSecurityMib,
       "prvtPortSECNotifications": prvtPortSECNotifications,
       "prvtPortSECViolation": prvtPortSECViolation,
       "prvtDuplicatedMACAddressAlarm": prvtDuplicatedMACAddressAlarm,
       "prvtPortSECObjects": prvtPortSECObjects,
       "prvtPortSECConformance": prvtPortSECConformance,
       "prvtPortSECMIBGroups": prvtPortSECMIBGroups,
       "prvtPortSECNotificationGroup": prvtPortSECNotificationGroup}
)
