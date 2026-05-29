# SNMP MIB module (LIBRENMS-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\librenms\LIBRENMS-NOTIFICATIONS-MIB

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

notifications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1)
)
if mibBuilder.loadTexts:
    notifications.setRevisions(
        ("2026-02-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Librenms_ObjectIdentity = ObjectIdentity
librenms = _Librenms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 60652)
)
_Alerting_ObjectIdentity = ObjectIdentity
alerting = _Alerting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 60652, 1)
)
_DefaultAlert_ObjectIdentity = ObjectIdentity
defaultAlert = _DefaultAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1)
)
_DefaultAlertTitle_Type = OctetString
_DefaultAlertTitle_Object = MibScalar
defaultAlertTitle = _DefaultAlertTitle_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 1),
    _DefaultAlertTitle_Type()
)
defaultAlertTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertTitle.setStatus("current")
_DefaultAlertID_Type = Integer32
_DefaultAlertID_Object = MibScalar
defaultAlertID = _DefaultAlertID_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 2),
    _DefaultAlertID_Type()
)
defaultAlertID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertID.setStatus("current")
_DefaultAlertEventID_Type = Integer32
_DefaultAlertEventID_Object = MibScalar
defaultAlertEventID = _DefaultAlertEventID_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 3),
    _DefaultAlertEventID_Type()
)
defaultAlertEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertEventID.setStatus("current")


class _DefaultAlertState_Type(Integer32):
    """Custom type defaultAlertState based on Integer32"""
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
        *(("stateClear", 0),
          ("stateActive", 1),
          ("stateAcknowledged", 2),
          ("stateWorse", 3),
          ("stateBetter", 4))
    )


_DefaultAlertState_Type.__name__ = "Integer32"
_DefaultAlertState_Object = MibScalar
defaultAlertState = _DefaultAlertState_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 4),
    _DefaultAlertState_Type()
)
defaultAlertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertState.setStatus("current")
_DefaultAlertSeverity_Type = OctetString
_DefaultAlertSeverity_Object = MibScalar
defaultAlertSeverity = _DefaultAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 5),
    _DefaultAlertSeverity_Type()
)
defaultAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertSeverity.setStatus("current")
_DefaultAlertRuleID_Type = Integer32
_DefaultAlertRuleID_Object = MibScalar
defaultAlertRuleID = _DefaultAlertRuleID_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 6),
    _DefaultAlertRuleID_Type()
)
defaultAlertRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertRuleID.setStatus("current")
_DefaultAlertRuleName_Type = OctetString
_DefaultAlertRuleName_Object = MibScalar
defaultAlertRuleName = _DefaultAlertRuleName_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 7),
    _DefaultAlertRuleName_Type()
)
defaultAlertRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertRuleName.setStatus("current")
_DefaultAlertProcedure_Type = OctetString
_DefaultAlertProcedure_Object = MibScalar
defaultAlertProcedure = _DefaultAlertProcedure_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 8),
    _DefaultAlertProcedure_Type()
)
defaultAlertProcedure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertProcedure.setStatus("current")
_DefaultAlertACKNotes_Type = OctetString
_DefaultAlertACKNotes_Object = MibScalar
defaultAlertACKNotes = _DefaultAlertACKNotes_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 9),
    _DefaultAlertACKNotes_Type()
)
defaultAlertACKNotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertACKNotes.setStatus("current")
_DefaultAlertTimestamp_Type = OctetString
_DefaultAlertTimestamp_Object = MibScalar
defaultAlertTimestamp = _DefaultAlertTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 10),
    _DefaultAlertTimestamp_Type()
)
defaultAlertTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertTimestamp.setStatus("current")
_DefaultAlertTimeElapsed_Type = OctetString
_DefaultAlertTimeElapsed_Object = MibScalar
defaultAlertTimeElapsed = _DefaultAlertTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 11),
    _DefaultAlertTimeElapsed_Type()
)
defaultAlertTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertTimeElapsed.setStatus("current")
_DefaultAlertDevice_ObjectIdentity = ObjectIdentity
defaultAlertDevice = _DefaultAlertDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12)
)
_DefaultAlertDeviceID_Type = Integer32
_DefaultAlertDeviceID_Object = MibScalar
defaultAlertDeviceID = _DefaultAlertDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 1),
    _DefaultAlertDeviceID_Type()
)
defaultAlertDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDeviceID.setStatus("current")
_DefaultAlertDevHostname_Type = OctetString
_DefaultAlertDevHostname_Object = MibScalar
defaultAlertDevHostname = _DefaultAlertDevHostname_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 2),
    _DefaultAlertDevHostname_Type()
)
defaultAlertDevHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevHostname.setStatus("current")
_DefaultAlertDevSysName_Type = OctetString
_DefaultAlertDevSysName_Object = MibScalar
defaultAlertDevSysName = _DefaultAlertDevSysName_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 3),
    _DefaultAlertDevSysName_Type()
)
defaultAlertDevSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevSysName.setStatus("current")
_DefaultAlertDevSysDescr_Type = OctetString
_DefaultAlertDevSysDescr_Object = MibScalar
defaultAlertDevSysDescr = _DefaultAlertDevSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 4),
    _DefaultAlertDevSysDescr_Type()
)
defaultAlertDevSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevSysDescr.setStatus("current")
_DefaultAlertDevMgmtIP_Type = OctetString
_DefaultAlertDevMgmtIP_Object = MibScalar
defaultAlertDevMgmtIP = _DefaultAlertDevMgmtIP_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 5),
    _DefaultAlertDevMgmtIP_Type()
)
defaultAlertDevMgmtIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevMgmtIP.setStatus("current")
_DefaultAlertDevOS_Type = OctetString
_DefaultAlertDevOS_Object = MibScalar
defaultAlertDevOS = _DefaultAlertDevOS_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 6),
    _DefaultAlertDevOS_Type()
)
defaultAlertDevOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevOS.setStatus("current")
_DefaultAlertDevType_Type = OctetString
_DefaultAlertDevType_Object = MibScalar
defaultAlertDevType = _DefaultAlertDevType_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 7),
    _DefaultAlertDevType_Type()
)
defaultAlertDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevType.setStatus("current")
_DefaultAlertDevHardware_Type = OctetString
_DefaultAlertDevHardware_Object = MibScalar
defaultAlertDevHardware = _DefaultAlertDevHardware_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 8),
    _DefaultAlertDevHardware_Type()
)
defaultAlertDevHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevHardware.setStatus("current")
_DefaultAlertDevVersion_Type = OctetString
_DefaultAlertDevVersion_Object = MibScalar
defaultAlertDevVersion = _DefaultAlertDevVersion_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 9),
    _DefaultAlertDevVersion_Type()
)
defaultAlertDevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevVersion.setStatus("current")
_DefaultAlertDevFeatures_Type = OctetString
_DefaultAlertDevFeatures_Object = MibScalar
defaultAlertDevFeatures = _DefaultAlertDevFeatures_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 10),
    _DefaultAlertDevFeatures_Type()
)
defaultAlertDevFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevFeatures.setStatus("current")
_DefaultAlertDevSerial_Type = OctetString
_DefaultAlertDevSerial_Object = MibScalar
defaultAlertDevSerial = _DefaultAlertDevSerial_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 11),
    _DefaultAlertDevSerial_Type()
)
defaultAlertDevSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevSerial.setStatus("current")
_DefaultAlertDevLocation_Type = OctetString
_DefaultAlertDevLocation_Object = MibScalar
defaultAlertDevLocation = _DefaultAlertDevLocation_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 12),
    _DefaultAlertDevLocation_Type()
)
defaultAlertDevLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevLocation.setStatus("current")
_DefaultAlertDevUptime_Type = TimeTicks
_DefaultAlertDevUptime_Object = MibScalar
defaultAlertDevUptime = _DefaultAlertDevUptime_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 13),
    _DefaultAlertDevUptime_Type()
)
defaultAlertDevUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevUptime.setStatus("current")
_DefaultAlertDevShortUptime_Type = OctetString
_DefaultAlertDevShortUptime_Object = MibScalar
defaultAlertDevShortUptime = _DefaultAlertDevShortUptime_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 14),
    _DefaultAlertDevShortUptime_Type()
)
defaultAlertDevShortUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevShortUptime.setStatus("current")
_DefaultAlertDevLongUptime_Type = OctetString
_DefaultAlertDevLongUptime_Object = MibScalar
defaultAlertDevLongUptime = _DefaultAlertDevLongUptime_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 15),
    _DefaultAlertDevLongUptime_Type()
)
defaultAlertDevLongUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevLongUptime.setStatus("current")
_DefaultAlertDevPurpose_Type = OctetString
_DefaultAlertDevPurpose_Object = MibScalar
defaultAlertDevPurpose = _DefaultAlertDevPurpose_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 16),
    _DefaultAlertDevPurpose_Type()
)
defaultAlertDevPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevPurpose.setStatus("current")
_DefaultAlertDevNotes_Type = OctetString
_DefaultAlertDevNotes_Object = MibScalar
defaultAlertDevNotes = _DefaultAlertDevNotes_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 17),
    _DefaultAlertDevNotes_Type()
)
defaultAlertDevNotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevNotes.setStatus("current")
_DefaultAlertDevPingLoss_Type = OctetString
_DefaultAlertDevPingLoss_Object = MibScalar
defaultAlertDevPingLoss = _DefaultAlertDevPingLoss_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 18),
    _DefaultAlertDevPingLoss_Type()
)
defaultAlertDevPingLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevPingLoss.setStatus("current")
_DefaultAlertDevPingMin_Type = OctetString
_DefaultAlertDevPingMin_Object = MibScalar
defaultAlertDevPingMin = _DefaultAlertDevPingMin_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 19),
    _DefaultAlertDevPingMin_Type()
)
defaultAlertDevPingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevPingMin.setStatus("current")
_DefaultAlertDevPingMax_Type = OctetString
_DefaultAlertDevPingMax_Object = MibScalar
defaultAlertDevPingMax = _DefaultAlertDevPingMax_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 20),
    _DefaultAlertDevPingMax_Type()
)
defaultAlertDevPingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevPingMax.setStatus("current")
_DefaultAlertDevPingAvg_Type = OctetString
_DefaultAlertDevPingAvg_Object = MibScalar
defaultAlertDevPingAvg = _DefaultAlertDevPingAvg_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 12, 21),
    _DefaultAlertDevPingAvg_Type()
)
defaultAlertDevPingAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertDevPingAvg.setStatus("current")
_DefaultAlertFaultTable_Object = MibTable
defaultAlertFaultTable = _DefaultAlertFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    defaultAlertFaultTable.setStatus("current")
_DefaultAlertFaultTableEntry_Object = MibTableRow
defaultAlertFaultTableEntry = _DefaultAlertFaultTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 13, 1)
)
defaultAlertFaultTableEntry.setIndexNames(
    (0, "LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertFaultEntryID"),
)
if mibBuilder.loadTexts:
    defaultAlertFaultTableEntry.setStatus("current")
_DefaultAlertFaultEntryID_Type = Unsigned32
_DefaultAlertFaultEntryID_Object = MibTableColumn
defaultAlertFaultEntryID = _DefaultAlertFaultEntryID_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 13, 1, 1),
    _DefaultAlertFaultEntryID_Type()
)
defaultAlertFaultEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    defaultAlertFaultEntryID.setStatus("current")
_DefaultAlertFaultDetail_Type = OctetString
_DefaultAlertFaultDetail_Object = MibTableColumn
defaultAlertFaultDetail = _DefaultAlertFaultDetail_Object(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 1, 13, 1, 2),
    _DefaultAlertFaultDetail_Type()
)
defaultAlertFaultDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAlertFaultDetail.setStatus("current")

# Managed Objects groups


# Notification objects

defaultAlertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 60652, 1, 1, 2)
)
defaultAlertEvent.setObjects(
      *(("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertTitle"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertID"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertEventID"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertState"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertSeverity"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertRuleID"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertRuleName"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertProcedure"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertACKNotes"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertTimestamp"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertTimeElapsed"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDeviceID"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevHostname"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevSysName"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevSysDescr"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevMgmtIP"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevOS"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevType"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevHardware"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevVersion"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevFeatures"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevSerial"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevLocation"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevUptime"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevShortUptime"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevLongUptime"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevPurpose"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevNotes"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevPingLoss"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevPingMin"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevPingMax"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertDevPingAvg"),
        ("LIBRENMS-NOTIFICATIONS-MIB", "defaultAlertFaultDetail"))
)
if mibBuilder.loadTexts:
    defaultAlertEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIBRENMS-NOTIFICATIONS-MIB",
    **{"librenms": librenms,
       "alerting": alerting,
       "notifications": notifications,
       "defaultAlert": defaultAlert,
       "defaultAlertTitle": defaultAlertTitle,
       "defaultAlertID": defaultAlertID,
       "defaultAlertEventID": defaultAlertEventID,
       "defaultAlertState": defaultAlertState,
       "defaultAlertSeverity": defaultAlertSeverity,
       "defaultAlertRuleID": defaultAlertRuleID,
       "defaultAlertRuleName": defaultAlertRuleName,
       "defaultAlertProcedure": defaultAlertProcedure,
       "defaultAlertACKNotes": defaultAlertACKNotes,
       "defaultAlertTimestamp": defaultAlertTimestamp,
       "defaultAlertTimeElapsed": defaultAlertTimeElapsed,
       "defaultAlertDevice": defaultAlertDevice,
       "defaultAlertDeviceID": defaultAlertDeviceID,
       "defaultAlertDevHostname": defaultAlertDevHostname,
       "defaultAlertDevSysName": defaultAlertDevSysName,
       "defaultAlertDevSysDescr": defaultAlertDevSysDescr,
       "defaultAlertDevMgmtIP": defaultAlertDevMgmtIP,
       "defaultAlertDevOS": defaultAlertDevOS,
       "defaultAlertDevType": defaultAlertDevType,
       "defaultAlertDevHardware": defaultAlertDevHardware,
       "defaultAlertDevVersion": defaultAlertDevVersion,
       "defaultAlertDevFeatures": defaultAlertDevFeatures,
       "defaultAlertDevSerial": defaultAlertDevSerial,
       "defaultAlertDevLocation": defaultAlertDevLocation,
       "defaultAlertDevUptime": defaultAlertDevUptime,
       "defaultAlertDevShortUptime": defaultAlertDevShortUptime,
       "defaultAlertDevLongUptime": defaultAlertDevLongUptime,
       "defaultAlertDevPurpose": defaultAlertDevPurpose,
       "defaultAlertDevNotes": defaultAlertDevNotes,
       "defaultAlertDevPingLoss": defaultAlertDevPingLoss,
       "defaultAlertDevPingMin": defaultAlertDevPingMin,
       "defaultAlertDevPingMax": defaultAlertDevPingMax,
       "defaultAlertDevPingAvg": defaultAlertDevPingAvg,
       "defaultAlertFaultTable": defaultAlertFaultTable,
       "defaultAlertFaultTableEntry": defaultAlertFaultTableEntry,
       "defaultAlertFaultEntryID": defaultAlertFaultEntryID,
       "defaultAlertFaultDetail": defaultAlertFaultDetail,
       "defaultAlertEvent": defaultAlertEvent}
)
