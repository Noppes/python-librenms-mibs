# SNMP MIB module (ALPHA-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alpha\ALPHA-NOTIFICATION-MIB

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

(alarmActiveModelPointer,
 alarmActiveResourceId,
 alarmModelDescription) = mibBuilder.importSymbols(
    "ALARM-MIB",
    "alarmActiveModelPointer",
    "alarmActiveResourceId",
    "alarmModelDescription")

(alpha,
 componentListReference,
 componentListStaticName,
 controllerInfoName) = mibBuilder.importSymbols(
    "ALPHA-RESOURCE-MIB",
    "alpha",
    "componentListReference",
    "componentListStaticName",
    "controllerInfoName")

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

alphaAlarmNotifications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 100)
)
if mibBuilder.loadTexts:
    alphaAlarmNotifications.setRevisions(
        ("2017-07-31 00:00",
         "2015-07-28 00:00",
         "2015-07-23 00:00",
         "2015-06-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlphaAlarmNotificationConformance_ObjectIdentity = ObjectIdentity
alphaAlarmNotificationConformance = _AlphaAlarmNotificationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 100, 102)
)
_AlphaAlarmNotificationCompliances_ObjectIdentity = ObjectIdentity
alphaAlarmNotificationCompliances = _AlphaAlarmNotificationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 100, 102, 1)
)
_AlphaAlarmNotificationGroups_ObjectIdentity = ObjectIdentity
alphaAlarmNotificationGroups = _AlphaAlarmNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2)
)
_AlphaAlarmNotificationsExtension_ObjectIdentity = ObjectIdentity
alphaAlarmNotificationsExtension = _AlphaAlarmNotificationsExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 101)
)
_AlarmSeverity_Type = Integer32
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 101, 1),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmCustomDescription_Type = OctetString
_AlarmCustomDescription_Object = MibScalar
alarmCustomDescription = _AlarmCustomDescription_Object(
    (1, 3, 6, 1, 4, 1, 7309, 101, 2),
    _AlarmCustomDescription_Type()
)
alarmCustomDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCustomDescription.setStatus("current")
_AlarmPriority_Type = OctetString
_AlarmPriority_Object = MibScalar
alarmPriority = _AlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 7309, 101, 3),
    _AlarmPriority_Type()
)
alarmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPriority.setStatus("current")
_AlarmAdditionalInformation_Type = OctetString
_AlarmAdditionalInformation_Object = MibScalar
alarmAdditionalInformation = _AlarmAdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 7309, 101, 4),
    _AlarmAdditionalInformation_Type()
)
alarmAdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAdditionalInformation.setStatus("current")

# Managed Objects groups

alphaParameterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2, 1)
)
alphaParameterGroup.setObjects(
      *(("ALPHA-NOTIFICATION-MIB", "alarmSeverity"),
        ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"),
        ("ALPHA-NOTIFICATION-MIB", "alarmPriority"),
        ("ALPHA-NOTIFICATION-MIB", "alarmAdditionalInformation"))
)
if mibBuilder.loadTexts:
    alphaParameterGroup.setStatus("current")


# Notification objects

alphaAlarmActiveState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 100, 1)
)
alphaAlarmActiveState.setObjects(
      *(("ALARM-MIB", "alarmActiveModelPointer"),
        ("ALARM-MIB", "alarmActiveResourceId"),
        ("ALPHA-NOTIFICATION-MIB", "alarmPriority"),
        ("ALARM-MIB", "alarmModelDescription"),
        ("ALPHA-RESOURCE-MIB", "componentListStaticName"),
        ("ALPHA-RESOURCE-MIB", "componentListReference"),
        ("ALPHA-NOTIFICATION-MIB", "alarmSeverity"),
        ("ALPHA-RESOURCE-MIB", "controllerInfoName"),
        ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"),
        ("ALPHA-NOTIFICATION-MIB", "alarmAdditionalInformation"))
)
if mibBuilder.loadTexts:
    alphaAlarmActiveState.setStatus(
        "current"
    )

alphaAlarmClearState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 100, 2)
)
alphaAlarmClearState.setObjects(
      *(("ALARM-MIB", "alarmActiveModelPointer"),
        ("ALARM-MIB", "alarmActiveResourceId"),
        ("ALPHA-NOTIFICATION-MIB", "alarmPriority"),
        ("ALARM-MIB", "alarmModelDescription"),
        ("ALPHA-RESOURCE-MIB", "componentListStaticName"),
        ("ALPHA-RESOURCE-MIB", "componentListReference"),
        ("ALPHA-NOTIFICATION-MIB", "alarmSeverity"),
        ("ALPHA-RESOURCE-MIB", "controllerInfoName"),
        ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"),
        ("ALPHA-NOTIFICATION-MIB", "alarmAdditionalInformation"))
)
if mibBuilder.loadTexts:
    alphaAlarmClearState.setStatus(
        "current"
    )


# Notifications groups

alphaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2, 2)
)
alphaNotificationsGroup.setObjects(
      *(("ALPHA-NOTIFICATION-MIB", "alphaAlarmActiveState"),
        ("ALPHA-NOTIFICATION-MIB", "alphaAlarmClearState"))
)
if mibBuilder.loadTexts:
    alphaNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alphaAlarmNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 1)
)
alphaAlarmNotificationCompliance.setObjects(
      *(("ALPHA-NOTIFICATION-MIB", "alphaParameterGroup"),
        ("ALPHA-NOTIFICATION-MIB", "alphaNotificationsGroup"))
)
if mibBuilder.loadTexts:
    alphaAlarmNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPHA-NOTIFICATION-MIB",
    **{"alphaAlarmNotifications": alphaAlarmNotifications,
       "alphaAlarmActiveState": alphaAlarmActiveState,
       "alphaAlarmClearState": alphaAlarmClearState,
       "alphaAlarmNotificationConformance": alphaAlarmNotificationConformance,
       "alphaAlarmNotificationCompliances": alphaAlarmNotificationCompliances,
       "alphaAlarmNotificationCompliance": alphaAlarmNotificationCompliance,
       "alphaAlarmNotificationGroups": alphaAlarmNotificationGroups,
       "alphaParameterGroup": alphaParameterGroup,
       "alphaNotificationsGroup": alphaNotificationsGroup,
       "alphaAlarmNotificationsExtension": alphaAlarmNotificationsExtension,
       "alarmSeverity": alarmSeverity,
       "alarmCustomDescription": alarmCustomDescription,
       "alarmPriority": alarmPriority,
       "alarmAdditionalInformation": alarmAdditionalInformation}
)
