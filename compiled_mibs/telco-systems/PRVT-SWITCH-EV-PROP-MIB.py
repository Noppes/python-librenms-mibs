# SNMP MIB module (PRVT-SWITCH-EV-PROP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SWITCH-EV-PROP-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtEventPropagation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166)
)
if mibBuilder.loadTexts:
    prvtEventPropagation.setRevisions(
        ("2011-01-26 00:00",
         "2011-01-17 00:00",
         "2010-08-09 00:00",
         "2010-05-20 00:00",
         "2009-09-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtEvPropNotifications_ObjectIdentity = ObjectIdentity
prvtEvPropNotifications = _PrvtEvPropNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 0)
)
_PrvtEvPropObjects_ObjectIdentity = ObjectIdentity
prvtEvPropObjects = _PrvtEvPropObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1)
)
_PrvtEventPropagationProfile_ObjectIdentity = ObjectIdentity
prvtEventPropagationProfile = _PrvtEventPropagationProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1)
)
_PrvtEventPropagationProfileTable_Object = MibTable
prvtEventPropagationProfileTable = _PrvtEventPropagationProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtEventPropagationProfileTable.setStatus("current")
_PrvtEventPropagationProfileEntry_Object = MibTableRow
prvtEventPropagationProfileEntry = _PrvtEventPropagationProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1)
)
prvtEventPropagationProfileEntry.setIndexNames(
    (0, "PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationProfileIndex"),
)
if mibBuilder.loadTexts:
    prvtEventPropagationProfileEntry.setStatus("current")
_PrvtEventPropagationProfileIndex_Type = Unsigned32
_PrvtEventPropagationProfileIndex_Object = MibTableColumn
prvtEventPropagationProfileIndex = _PrvtEventPropagationProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1, 1),
    _PrvtEventPropagationProfileIndex_Type()
)
prvtEventPropagationProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtEventPropagationProfileIndex.setStatus("current")


class _PrvtEventPropagationEvent_Type(Integer32):
    """Custom type prvtEventPropagationEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notSpecified", 1),
          ("lossOfConnectivity", 2),
          ("receivedAIS", 3),
          ("receivedRDI", 4),
          ("interfaceDown", 5),
          ("testing", 6))
    )


_PrvtEventPropagationEvent_Type.__name__ = "Integer32"
_PrvtEventPropagationEvent_Object = MibTableColumn
prvtEventPropagationEvent = _PrvtEventPropagationEvent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1, 2),
    _PrvtEventPropagationEvent_Type()
)
prvtEventPropagationEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEventPropagationEvent.setStatus("current")


class _PrvtEventPropagationRemotePeerType_Type(Integer32):
    """Custom type prvtEventPropagationRemotePeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notSpecified", 1),
          ("macAddress", 2),
          ("remoteMep", 3),
          ("interfaceID", 4),
          ("ipv4Address", 5),
          ("localMep", 6),
          ("lagID", 7))
    )


_PrvtEventPropagationRemotePeerType_Type.__name__ = "Integer32"
_PrvtEventPropagationRemotePeerType_Object = MibTableColumn
prvtEventPropagationRemotePeerType = _PrvtEventPropagationRemotePeerType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1, 3),
    _PrvtEventPropagationRemotePeerType_Type()
)
prvtEventPropagationRemotePeerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEventPropagationRemotePeerType.setStatus("current")


class _PrvtEventPropagationRemotePeerID_Type(DisplayString):
    """Custom type prvtEventPropagationRemotePeerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PrvtEventPropagationRemotePeerID_Type.__name__ = "DisplayString"
_PrvtEventPropagationRemotePeerID_Object = MibTableColumn
prvtEventPropagationRemotePeerID = _PrvtEventPropagationRemotePeerID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1, 4),
    _PrvtEventPropagationRemotePeerID_Type()
)
prvtEventPropagationRemotePeerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEventPropagationRemotePeerID.setStatus("current")


class _PrvtEventPropagationActionID_Type(Integer32):
    """Custom type prvtEventPropagationActionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSpecified", 1),
          ("dropLink", 2))
    )


_PrvtEventPropagationActionID_Type.__name__ = "Integer32"
_PrvtEventPropagationActionID_Object = MibTableColumn
prvtEventPropagationActionID = _PrvtEventPropagationActionID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1, 5),
    _PrvtEventPropagationActionID_Type()
)
prvtEventPropagationActionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEventPropagationActionID.setStatus("current")


class _PrvtEventPropagationRevertiveActionID_Type(Integer32):
    """Custom type prvtEventPropagationRevertiveActionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSpecified", 1),
          ("restoreLink", 2))
    )


_PrvtEventPropagationRevertiveActionID_Type.__name__ = "Integer32"
_PrvtEventPropagationRevertiveActionID_Object = MibTableColumn
prvtEventPropagationRevertiveActionID = _PrvtEventPropagationRevertiveActionID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1, 6),
    _PrvtEventPropagationRevertiveActionID_Type()
)
prvtEventPropagationRevertiveActionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEventPropagationRevertiveActionID.setStatus("current")
_PrvtEventPropagationProfileRowStatus_Type = RowStatus
_PrvtEventPropagationProfileRowStatus_Object = MibTableColumn
prvtEventPropagationProfileRowStatus = _PrvtEventPropagationProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1, 7),
    _PrvtEventPropagationProfileRowStatus_Type()
)
prvtEventPropagationProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationProfileRowStatus.setStatus("current")


class _PrvtEventPropagationHoldTimer_Type(Unsigned32):
    """Custom type prvtEventPropagationHoldTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_PrvtEventPropagationHoldTimer_Type.__name__ = "Unsigned32"
_PrvtEventPropagationHoldTimer_Object = MibTableColumn
prvtEventPropagationHoldTimer = _PrvtEventPropagationHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1, 8),
    _PrvtEventPropagationHoldTimer_Type()
)
prvtEventPropagationHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEventPropagationHoldTimer.setStatus("current")


class _PrvtEventPropagationWaitRestoreTimer_Type(Unsigned32):
    """Custom type prvtEventPropagationWaitRestoreTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PrvtEventPropagationWaitRestoreTimer_Type.__name__ = "Unsigned32"
_PrvtEventPropagationWaitRestoreTimer_Object = MibTableColumn
prvtEventPropagationWaitRestoreTimer = _PrvtEventPropagationWaitRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1, 9),
    _PrvtEventPropagationWaitRestoreTimer_Type()
)
prvtEventPropagationWaitRestoreTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEventPropagationWaitRestoreTimer.setStatus("current")
_PrvtEventPropagationSession_ObjectIdentity = ObjectIdentity
prvtEventPropagationSession = _PrvtEventPropagationSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2)
)
_PrvtEventPropagationSessionTable_Object = MibTable
prvtEventPropagationSessionTable = _PrvtEventPropagationSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1)
)
if mibBuilder.loadTexts:
    prvtEventPropagationSessionTable.setStatus("current")
_PrvtEventPropagationSessionEntry_Object = MibTableRow
prvtEventPropagationSessionEntry = _PrvtEventPropagationSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1, 1)
)
prvtEventPropagationSessionEntry.setIndexNames(
    (0, "PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationProfileIndex"),
    (0, "PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationSessionIndex"),
)
if mibBuilder.loadTexts:
    prvtEventPropagationSessionEntry.setStatus("current")
_PrvtEventPropagationSessionIndex_Type = Unsigned32
_PrvtEventPropagationSessionIndex_Object = MibTableColumn
prvtEventPropagationSessionIndex = _PrvtEventPropagationSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1, 1, 1),
    _PrvtEventPropagationSessionIndex_Type()
)
prvtEventPropagationSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionIndex.setStatus("current")


class _PrvtEventPropagationSessionTargetType_Type(Integer32):
    """Custom type prvtEventPropagationSessionTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSpecified", 1),
          ("interfacePort", 2),
          ("interfaceSAP", 3))
    )


_PrvtEventPropagationSessionTargetType_Type.__name__ = "Integer32"
_PrvtEventPropagationSessionTargetType_Object = MibTableColumn
prvtEventPropagationSessionTargetType = _PrvtEventPropagationSessionTargetType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1, 1, 2),
    _PrvtEventPropagationSessionTargetType_Type()
)
prvtEventPropagationSessionTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionTargetType.setStatus("current")


class _PrvtEventPropagationSessionTargetID_Type(DisplayString):
    """Custom type prvtEventPropagationSessionTargetID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_PrvtEventPropagationSessionTargetID_Type.__name__ = "DisplayString"
_PrvtEventPropagationSessionTargetID_Object = MibTableColumn
prvtEventPropagationSessionTargetID = _PrvtEventPropagationSessionTargetID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1, 1, 3),
    _PrvtEventPropagationSessionTargetID_Type()
)
prvtEventPropagationSessionTargetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionTargetID.setStatus("current")
_PrvtEventPropagationLastActionCounter_Type = Counter32
_PrvtEventPropagationLastActionCounter_Object = MibTableColumn
prvtEventPropagationLastActionCounter = _PrvtEventPropagationLastActionCounter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1, 1, 4),
    _PrvtEventPropagationLastActionCounter_Type()
)
prvtEventPropagationLastActionCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEventPropagationLastActionCounter.setStatus("current")
_PrvtEventPropagationLastRevertiveActionCounter_Type = Counter32
_PrvtEventPropagationLastRevertiveActionCounter_Object = MibTableColumn
prvtEventPropagationLastRevertiveActionCounter = _PrvtEventPropagationLastRevertiveActionCounter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1, 1, 5),
    _PrvtEventPropagationLastRevertiveActionCounter_Type()
)
prvtEventPropagationLastRevertiveActionCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEventPropagationLastRevertiveActionCounter.setStatus("current")
_PrvtEventPropagationSessionRowStatus_Type = RowStatus
_PrvtEventPropagationSessionRowStatus_Object = MibTableColumn
prvtEventPropagationSessionRowStatus = _PrvtEventPropagationSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1, 1, 6),
    _PrvtEventPropagationSessionRowStatus_Type()
)
prvtEventPropagationSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionRowStatus.setStatus("current")
_PrvtEvPropConformance_ObjectIdentity = ObjectIdentity
prvtEvPropConformance = _PrvtEvPropConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 2)
)
_PrvtEvPropCompliances_ObjectIdentity = ObjectIdentity
prvtEvPropCompliances = _PrvtEvPropCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 2, 1)
)
_PrvtEvPropGroups_ObjectIdentity = ObjectIdentity
prvtEvPropGroups = _PrvtEvPropGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 2, 2)
)

# Managed Objects groups

prvtEvPropProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 2, 2, 1)
)
prvtEvPropProfileGroup.setObjects(
      *(("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationEvent"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationRemotePeerType"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationRemotePeerID"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationActionID"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationRevertiveActionID"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationProfileRowStatus"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationHoldTimer"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationWaitRestoreTimer"))
)
if mibBuilder.loadTexts:
    prvtEvPropProfileGroup.setStatus("current")

prvtEvPropSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 2, 2, 2)
)
prvtEvPropSessionGroup.setObjects(
      *(("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationSessionTargetType"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationSessionTargetID"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationLastActionCounter"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationLastRevertiveActionCounter"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationSessionRowStatus"))
)
if mibBuilder.loadTexts:
    prvtEvPropSessionGroup.setStatus("current")


# Notification objects

prvtEvPropAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 0, 1)
)
prvtEvPropAction.setObjects(
      *(("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationEvent"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationRemotePeerType"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationRemotePeerID"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationActionID"))
)
if mibBuilder.loadTexts:
    prvtEvPropAction.setStatus(
        "current"
    )

prvtEvPropRevert = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 0, 2)
)
prvtEvPropRevert.setObjects(
      *(("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationEvent"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationRemotePeerType"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationRemotePeerID"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEventPropagationRevertiveActionID"))
)
if mibBuilder.loadTexts:
    prvtEvPropRevert.setStatus(
        "current"
    )


# Notifications groups

prvtEvPropNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 2, 2, 3)
)
prvtEvPropNotificationsGroup.setObjects(
      *(("PRVT-SWITCH-EV-PROP-MIB", "prvtEvPropAction"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEvPropRevert"))
)
if mibBuilder.loadTexts:
    prvtEvPropNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prvtEvPropCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 2, 1, 1)
)
prvtEvPropCompliance.setObjects(
      *(("PRVT-SWITCH-EV-PROP-MIB", "prvtEvPropProfileGroup"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEvPropSessionGroup"),
        ("PRVT-SWITCH-EV-PROP-MIB", "prvtEvPropNotificationsGroup"))
)
if mibBuilder.loadTexts:
    prvtEvPropCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SWITCH-EV-PROP-MIB",
    **{"prvtEventPropagation": prvtEventPropagation,
       "prvtEvPropNotifications": prvtEvPropNotifications,
       "prvtEvPropAction": prvtEvPropAction,
       "prvtEvPropRevert": prvtEvPropRevert,
       "prvtEvPropObjects": prvtEvPropObjects,
       "prvtEventPropagationProfile": prvtEventPropagationProfile,
       "prvtEventPropagationProfileTable": prvtEventPropagationProfileTable,
       "prvtEventPropagationProfileEntry": prvtEventPropagationProfileEntry,
       "prvtEventPropagationProfileIndex": prvtEventPropagationProfileIndex,
       "prvtEventPropagationEvent": prvtEventPropagationEvent,
       "prvtEventPropagationRemotePeerType": prvtEventPropagationRemotePeerType,
       "prvtEventPropagationRemotePeerID": prvtEventPropagationRemotePeerID,
       "prvtEventPropagationActionID": prvtEventPropagationActionID,
       "prvtEventPropagationRevertiveActionID": prvtEventPropagationRevertiveActionID,
       "prvtEventPropagationProfileRowStatus": prvtEventPropagationProfileRowStatus,
       "prvtEventPropagationHoldTimer": prvtEventPropagationHoldTimer,
       "prvtEventPropagationWaitRestoreTimer": prvtEventPropagationWaitRestoreTimer,
       "prvtEventPropagationSession": prvtEventPropagationSession,
       "prvtEventPropagationSessionTable": prvtEventPropagationSessionTable,
       "prvtEventPropagationSessionEntry": prvtEventPropagationSessionEntry,
       "prvtEventPropagationSessionIndex": prvtEventPropagationSessionIndex,
       "prvtEventPropagationSessionTargetType": prvtEventPropagationSessionTargetType,
       "prvtEventPropagationSessionTargetID": prvtEventPropagationSessionTargetID,
       "prvtEventPropagationLastActionCounter": prvtEventPropagationLastActionCounter,
       "prvtEventPropagationLastRevertiveActionCounter": prvtEventPropagationLastRevertiveActionCounter,
       "prvtEventPropagationSessionRowStatus": prvtEventPropagationSessionRowStatus,
       "prvtEvPropConformance": prvtEvPropConformance,
       "prvtEvPropCompliances": prvtEvPropCompliances,
       "prvtEvPropCompliance": prvtEvPropCompliance,
       "prvtEvPropGroups": prvtEvPropGroups,
       "prvtEvPropProfileGroup": prvtEvPropProfileGroup,
       "prvtEvPropSessionGroup": prvtEvPropSessionGroup,
       "prvtEvPropNotificationsGroup": prvtEvPropNotificationsGroup}
)
