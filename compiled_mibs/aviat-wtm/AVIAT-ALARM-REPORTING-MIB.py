# SNMP MIB module (AVIAT-ALARM-REPORTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aviat-wtm\AVIAT-ALARM-REPORTING-MIB

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

(AviatYangIdentityRef,) = mibBuilder.importSymbols(
    "AVIAT-TEXTCONVENTION-MIB",
    "AviatYangIdentityRef")

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(aviatModules,) = mibBuilder.importSymbols(
    "STXN-GLOBALREGISTER-MIB",
    "aviatModules")


# MODULE-IDENTITY

aviatAlarmReportingModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47)
)
if mibBuilder.loadTexts:
    aviatAlarmReportingModule.setRevisions(
        ("2016-05-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IetfEntityName(TextualConvention, OctetString):
    status = "current"
    displayHint = "127t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class AviatAlarmInstanceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unstable", 2))
    )



class AviatAlarmReportingMode(TextualConvention, Integer32):
    status = "current"
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
        *(("all", 0),
          ("nonSummary", 1),
          ("summaryOnly", 2),
          ("none", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AviatAlarmReportingMIBEvents_ObjectIdentity = ObjectIdentity
aviatAlarmReportingMIBEvents = _AviatAlarmReportingMIBEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 0)
)
_AviatAlarmReportingConformance_ObjectIdentity = ObjectIdentity
aviatAlarmReportingConformance = _AviatAlarmReportingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 1)
)
_AviatAlarmReportingGroups_ObjectIdentity = ObjectIdentity
aviatAlarmReportingGroups = _AviatAlarmReportingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 1)
)
_AviatAlarmReportingCompliance_ObjectIdentity = ObjectIdentity
aviatAlarmReportingCompliance = _AviatAlarmReportingCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 2)
)
_AviatAlarmReportingMIBObjects_ObjectIdentity = ObjectIdentity
aviatAlarmReportingMIBObjects = _AviatAlarmReportingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2)
)
_AviatAlarmTypeTable_Object = MibTable
aviatAlarmTypeTable = _AviatAlarmTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1)
)
if mibBuilder.loadTexts:
    aviatAlarmTypeTable.setStatus("current")
_AviatAlarmTypeEntry_Object = MibTableRow
aviatAlarmTypeEntry = _AviatAlarmTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1)
)
aviatAlarmTypeEntry.setIndexNames(
    (0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeIndex"),
)
if mibBuilder.loadTexts:
    aviatAlarmTypeEntry.setStatus("current")
_AviatAlarmTypeIndex_Type = AviatYangIdentityRef
_AviatAlarmTypeIndex_Object = MibTableColumn
aviatAlarmTypeIndex = _AviatAlarmTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 1),
    _AviatAlarmTypeIndex_Type()
)
aviatAlarmTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatAlarmTypeIndex.setStatus("current")
_AviatAlarmTypeSecurityEvent_Type = TruthValue
_AviatAlarmTypeSecurityEvent_Object = MibTableColumn
aviatAlarmTypeSecurityEvent = _AviatAlarmTypeSecurityEvent_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 2),
    _AviatAlarmTypeSecurityEvent_Type()
)
aviatAlarmTypeSecurityEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmTypeSecurityEvent.setStatus("current")


class _AviatAlarmTypeDescription_Type(DisplayString):
    """Custom type aviatAlarmTypeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviatAlarmTypeDescription_Type.__name__ = "DisplayString"
_AviatAlarmTypeDescription_Object = MibTableColumn
aviatAlarmTypeDescription = _AviatAlarmTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 3),
    _AviatAlarmTypeDescription_Type()
)
aviatAlarmTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmTypeDescription.setStatus("current")
_AviatAlarmTypeEvent_Type = IANAItuEventType
_AviatAlarmTypeEvent_Object = MibTableColumn
aviatAlarmTypeEvent = _AviatAlarmTypeEvent_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 4),
    _AviatAlarmTypeEvent_Type()
)
aviatAlarmTypeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmTypeEvent.setStatus("current")
_AviatAlarmTypeDefaultSeverity_Type = ItuPerceivedSeverity
_AviatAlarmTypeDefaultSeverity_Object = MibTableColumn
aviatAlarmTypeDefaultSeverity = _AviatAlarmTypeDefaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 1, 1, 5),
    _AviatAlarmTypeDefaultSeverity_Type()
)
aviatAlarmTypeDefaultSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmTypeDefaultSeverity.setStatus("current")
_AviatAlarmInstanceLastChange_Type = DateAndTime
_AviatAlarmInstanceLastChange_Object = MibScalar
aviatAlarmInstanceLastChange = _AviatAlarmInstanceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 2),
    _AviatAlarmInstanceLastChange_Type()
)
aviatAlarmInstanceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceLastChange.setStatus("current")
_AviatAlarmInstanceTable_Object = MibTable
aviatAlarmInstanceTable = _AviatAlarmInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3)
)
if mibBuilder.loadTexts:
    aviatAlarmInstanceTable.setStatus("current")
_AviatAlarmInstanceEntry_Object = MibTableRow
aviatAlarmInstanceEntry = _AviatAlarmInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1)
)
aviatAlarmInstanceEntry.setIndexNames(
    (0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceEntity"),
    (0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeIndex"),
)
if mibBuilder.loadTexts:
    aviatAlarmInstanceEntry.setStatus("current")
_AviatAlarmInstanceEntity_Type = IetfEntityName
_AviatAlarmInstanceEntity_Object = MibTableColumn
aviatAlarmInstanceEntity = _AviatAlarmInstanceEntity_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 1),
    _AviatAlarmInstanceEntity_Type()
)
aviatAlarmInstanceEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatAlarmInstanceEntity.setStatus("current")
_AviatAlarmInstanceSecurityEvent_Type = TruthValue
_AviatAlarmInstanceSecurityEvent_Object = MibTableColumn
aviatAlarmInstanceSecurityEvent = _AviatAlarmInstanceSecurityEvent_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 2),
    _AviatAlarmInstanceSecurityEvent_Type()
)
aviatAlarmInstanceSecurityEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceSecurityEvent.setStatus("current")


class _AviatAlarmInstanceDescription_Type(DisplayString):
    """Custom type aviatAlarmInstanceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviatAlarmInstanceDescription_Type.__name__ = "DisplayString"
_AviatAlarmInstanceDescription_Object = MibTableColumn
aviatAlarmInstanceDescription = _AviatAlarmInstanceDescription_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 3),
    _AviatAlarmInstanceDescription_Type()
)
aviatAlarmInstanceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceDescription.setStatus("current")
_AviatAlarmInstanceType_Type = IANAItuEventType
_AviatAlarmInstanceType_Object = MibTableColumn
aviatAlarmInstanceType = _AviatAlarmInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 4),
    _AviatAlarmInstanceType_Type()
)
aviatAlarmInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceType.setStatus("current")
_AviatAlarmInstanceCurrentState_Type = AviatAlarmInstanceState
_AviatAlarmInstanceCurrentState_Object = MibTableColumn
aviatAlarmInstanceCurrentState = _AviatAlarmInstanceCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 5),
    _AviatAlarmInstanceCurrentState_Type()
)
aviatAlarmInstanceCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceCurrentState.setStatus("current")
_AviatAlarmInstanceCurrentSeverity_Type = ItuPerceivedSeverity
_AviatAlarmInstanceCurrentSeverity_Object = MibTableColumn
aviatAlarmInstanceCurrentSeverity = _AviatAlarmInstanceCurrentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 6),
    _AviatAlarmInstanceCurrentSeverity_Type()
)
aviatAlarmInstanceCurrentSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceCurrentSeverity.setStatus("current")
_AviatAlarmInstanceRaisedSeverity_Type = ItuPerceivedSeverity
_AviatAlarmInstanceRaisedSeverity_Object = MibTableColumn
aviatAlarmInstanceRaisedSeverity = _AviatAlarmInstanceRaisedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 7),
    _AviatAlarmInstanceRaisedSeverity_Type()
)
aviatAlarmInstanceRaisedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceRaisedSeverity.setStatus("current")
_AviatAlarmInstanceLastStatusChange_Type = DateAndTime
_AviatAlarmInstanceLastStatusChange_Object = MibTableColumn
aviatAlarmInstanceLastStatusChange = _AviatAlarmInstanceLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 8),
    _AviatAlarmInstanceLastStatusChange_Type()
)
aviatAlarmInstanceLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceLastStatusChange.setStatus("current")
_AviatAlarmInstanceStatusChangeCount_Type = Counter32
_AviatAlarmInstanceStatusChangeCount_Object = MibTableColumn
aviatAlarmInstanceStatusChangeCount = _AviatAlarmInstanceStatusChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 9),
    _AviatAlarmInstanceStatusChangeCount_Type()
)
aviatAlarmInstanceStatusChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceStatusChangeCount.setStatus("current")
_AviatAlarmInstanceDisabled_Type = TruthValue
_AviatAlarmInstanceDisabled_Object = MibTableColumn
aviatAlarmInstanceDisabled = _AviatAlarmInstanceDisabled_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 3, 1, 10),
    _AviatAlarmInstanceDisabled_Type()
)
aviatAlarmInstanceDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmInstanceDisabled.setStatus("current")
_AviatAlarmRaisedInstanceLastChange_Type = DateAndTime
_AviatAlarmRaisedInstanceLastChange_Object = MibScalar
aviatAlarmRaisedInstanceLastChange = _AviatAlarmRaisedInstanceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 4),
    _AviatAlarmRaisedInstanceLastChange_Type()
)
aviatAlarmRaisedInstanceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceLastChange.setStatus("current")
_AviatAlarmRaisedInstanceTable_Object = MibTable
aviatAlarmRaisedInstanceTable = _AviatAlarmRaisedInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5)
)
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceTable.setStatus("current")
_AviatAlarmRaisedInstanceEntry_Object = MibTableRow
aviatAlarmRaisedInstanceEntry = _AviatAlarmRaisedInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1)
)
aviatAlarmRaisedInstanceEntry.setIndexNames(
    (0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceEntity"),
    (0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeIndex"),
)
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceEntry.setStatus("current")
_AviatAlarmRaisedInstanceSecurityEvent_Type = TruthValue
_AviatAlarmRaisedInstanceSecurityEvent_Object = MibTableColumn
aviatAlarmRaisedInstanceSecurityEvent = _AviatAlarmRaisedInstanceSecurityEvent_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 1),
    _AviatAlarmRaisedInstanceSecurityEvent_Type()
)
aviatAlarmRaisedInstanceSecurityEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceSecurityEvent.setStatus("current")


class _AviatAlarmRaisedInstanceDescription_Type(DisplayString):
    """Custom type aviatAlarmRaisedInstanceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviatAlarmRaisedInstanceDescription_Type.__name__ = "DisplayString"
_AviatAlarmRaisedInstanceDescription_Object = MibTableColumn
aviatAlarmRaisedInstanceDescription = _AviatAlarmRaisedInstanceDescription_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 2),
    _AviatAlarmRaisedInstanceDescription_Type()
)
aviatAlarmRaisedInstanceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceDescription.setStatus("current")
_AviatAlarmRaisedInstanceSeverity_Type = ItuPerceivedSeverity
_AviatAlarmRaisedInstanceSeverity_Object = MibTableColumn
aviatAlarmRaisedInstanceSeverity = _AviatAlarmRaisedInstanceSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 3),
    _AviatAlarmRaisedInstanceSeverity_Type()
)
aviatAlarmRaisedInstanceSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceSeverity.setStatus("current")
_AviatAlarmRaisedInstanceCause_Type = IANAItuProbableCause
_AviatAlarmRaisedInstanceCause_Object = MibTableColumn
aviatAlarmRaisedInstanceCause = _AviatAlarmRaisedInstanceCause_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 4),
    _AviatAlarmRaisedInstanceCause_Type()
)
aviatAlarmRaisedInstanceCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceCause.setStatus("current")
_AviatAlarmRaisedInstanceTime_Type = DateAndTime
_AviatAlarmRaisedInstanceTime_Object = MibTableColumn
aviatAlarmRaisedInstanceTime = _AviatAlarmRaisedInstanceTime_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 5),
    _AviatAlarmRaisedInstanceTime_Type()
)
aviatAlarmRaisedInstanceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceTime.setStatus("current")
_AviatAlarmRaisedInstanceIsUnstable_Type = TruthValue
_AviatAlarmRaisedInstanceIsUnstable_Object = MibTableColumn
aviatAlarmRaisedInstanceIsUnstable = _AviatAlarmRaisedInstanceIsUnstable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 5, 1, 6),
    _AviatAlarmRaisedInstanceIsUnstable_Type()
)
aviatAlarmRaisedInstanceIsUnstable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceIsUnstable.setStatus("current")
_AviatAlarmEntityTable_Object = MibTable
aviatAlarmEntityTable = _AviatAlarmEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 6)
)
if mibBuilder.loadTexts:
    aviatAlarmEntityTable.setStatus("current")
_AviatAlarmEntityEntry_Object = MibTableRow
aviatAlarmEntityEntry = _AviatAlarmEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 6, 1)
)
aviatAlarmEntityEntry.setIndexNames(
    (0, "AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceEntity"),
)
if mibBuilder.loadTexts:
    aviatAlarmEntityEntry.setStatus("current")
_AviatAlarmEntityReportingMode_Type = AviatAlarmReportingMode
_AviatAlarmEntityReportingMode_Object = MibTableColumn
aviatAlarmEntityReportingMode = _AviatAlarmEntityReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 6, 1, 1),
    _AviatAlarmEntityReportingMode_Type()
)
aviatAlarmEntityReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatAlarmEntityReportingMode.setStatus("current")
_AviatAlarmReportingNotifications_ObjectIdentity = ObjectIdentity
aviatAlarmReportingNotifications = _AviatAlarmReportingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 7)
)
_AviatAlarmEntityName_Type = IetfEntityName
_AviatAlarmEntityName_Object = MibScalar
aviatAlarmEntityName = _AviatAlarmEntityName_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 7, 1),
    _AviatAlarmEntityName_Type()
)
aviatAlarmEntityName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aviatAlarmEntityName.setStatus("current")
_AviatAlarmTypeID_Type = AviatYangIdentityRef
_AviatAlarmTypeID_Object = MibScalar
aviatAlarmTypeID = _AviatAlarmTypeID_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 2, 7, 2),
    _AviatAlarmTypeID_Type()
)
aviatAlarmTypeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aviatAlarmTypeID.setStatus("current")

# Managed Objects groups

aviatAlarmReportingObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 1, 1)
)
aviatAlarmReportingObjectGroup.setObjects(
      *(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeSecurityEvent"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeDescription"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeEvent"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeDefaultSeverity"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastChange"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceSecurityEvent"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceDescription"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceType"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceCurrentState"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceCurrentSeverity"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceRaisedSeverity"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceStatusChangeCount"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceDisabled"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceLastChange"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceSecurityEvent"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceDescription"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceSeverity"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceCause"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceTime"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceIsUnstable"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityReportingMode"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"))
)
if mibBuilder.loadTexts:
    aviatAlarmReportingObjectGroup.setStatus("current")


# Notification objects

aviatAlarmRaisedInstanceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 0, 1)
)
aviatAlarmRaisedInstanceNotification.setObjects(
      *(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceCurrentSeverity"))
)
if mibBuilder.loadTexts:
    aviatAlarmRaisedInstanceNotification.setStatus(
        "current"
    )

aviatAlarmClearedInstanceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 0, 2)
)
aviatAlarmClearedInstanceNotification.setObjects(
      *(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"))
)
if mibBuilder.loadTexts:
    aviatAlarmClearedInstanceNotification.setStatus(
        "current"
    )

aviatAlarmUnstableInstanceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 0, 3)
)
aviatAlarmUnstableInstanceNotification.setObjects(
      *(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceCurrentSeverity"))
)
if mibBuilder.loadTexts:
    aviatAlarmUnstableInstanceNotification.setStatus(
        "current"
    )

aviatAlarmStabilizedInstanceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 0, 4)
)
aviatAlarmStabilizedInstanceNotification.setObjects(
      *(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmInstanceLastStatusChange"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmEntityName"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmTypeID"))
)
if mibBuilder.loadTexts:
    aviatAlarmStabilizedInstanceNotification.setStatus(
        "current"
    )


# Notifications groups

aviatAlarmReportingNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 1, 2)
)
aviatAlarmReportingNotifyGroup.setObjects(
      *(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmRaisedInstanceNotification"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmClearedInstanceNotification"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmUnstableInstanceNotification"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmStabilizedInstanceNotification"))
)
if mibBuilder.loadTexts:
    aviatAlarmReportingNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aviatAlarmReportingComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2509, 9, 47, 1, 2, 1)
)
aviatAlarmReportingComplV1.setObjects(
      *(("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmReportingObjectGroup"),
        ("AVIAT-ALARM-REPORTING-MIB", "aviatAlarmReportingNotifyGroup"))
)
if mibBuilder.loadTexts:
    aviatAlarmReportingComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVIAT-ALARM-REPORTING-MIB",
    **{"IetfEntityName": IetfEntityName,
       "AviatAlarmInstanceState": AviatAlarmInstanceState,
       "AviatAlarmReportingMode": AviatAlarmReportingMode,
       "aviatAlarmReportingModule": aviatAlarmReportingModule,
       "aviatAlarmReportingMIBEvents": aviatAlarmReportingMIBEvents,
       "aviatAlarmRaisedInstanceNotification": aviatAlarmRaisedInstanceNotification,
       "aviatAlarmClearedInstanceNotification": aviatAlarmClearedInstanceNotification,
       "aviatAlarmUnstableInstanceNotification": aviatAlarmUnstableInstanceNotification,
       "aviatAlarmStabilizedInstanceNotification": aviatAlarmStabilizedInstanceNotification,
       "aviatAlarmReportingConformance": aviatAlarmReportingConformance,
       "aviatAlarmReportingGroups": aviatAlarmReportingGroups,
       "aviatAlarmReportingObjectGroup": aviatAlarmReportingObjectGroup,
       "aviatAlarmReportingNotifyGroup": aviatAlarmReportingNotifyGroup,
       "aviatAlarmReportingCompliance": aviatAlarmReportingCompliance,
       "aviatAlarmReportingComplV1": aviatAlarmReportingComplV1,
       "aviatAlarmReportingMIBObjects": aviatAlarmReportingMIBObjects,
       "aviatAlarmTypeTable": aviatAlarmTypeTable,
       "aviatAlarmTypeEntry": aviatAlarmTypeEntry,
       "aviatAlarmTypeIndex": aviatAlarmTypeIndex,
       "aviatAlarmTypeSecurityEvent": aviatAlarmTypeSecurityEvent,
       "aviatAlarmTypeDescription": aviatAlarmTypeDescription,
       "aviatAlarmTypeEvent": aviatAlarmTypeEvent,
       "aviatAlarmTypeDefaultSeverity": aviatAlarmTypeDefaultSeverity,
       "aviatAlarmInstanceLastChange": aviatAlarmInstanceLastChange,
       "aviatAlarmInstanceTable": aviatAlarmInstanceTable,
       "aviatAlarmInstanceEntry": aviatAlarmInstanceEntry,
       "aviatAlarmInstanceEntity": aviatAlarmInstanceEntity,
       "aviatAlarmInstanceSecurityEvent": aviatAlarmInstanceSecurityEvent,
       "aviatAlarmInstanceDescription": aviatAlarmInstanceDescription,
       "aviatAlarmInstanceType": aviatAlarmInstanceType,
       "aviatAlarmInstanceCurrentState": aviatAlarmInstanceCurrentState,
       "aviatAlarmInstanceCurrentSeverity": aviatAlarmInstanceCurrentSeverity,
       "aviatAlarmInstanceRaisedSeverity": aviatAlarmInstanceRaisedSeverity,
       "aviatAlarmInstanceLastStatusChange": aviatAlarmInstanceLastStatusChange,
       "aviatAlarmInstanceStatusChangeCount": aviatAlarmInstanceStatusChangeCount,
       "aviatAlarmInstanceDisabled": aviatAlarmInstanceDisabled,
       "aviatAlarmRaisedInstanceLastChange": aviatAlarmRaisedInstanceLastChange,
       "aviatAlarmRaisedInstanceTable": aviatAlarmRaisedInstanceTable,
       "aviatAlarmRaisedInstanceEntry": aviatAlarmRaisedInstanceEntry,
       "aviatAlarmRaisedInstanceSecurityEvent": aviatAlarmRaisedInstanceSecurityEvent,
       "aviatAlarmRaisedInstanceDescription": aviatAlarmRaisedInstanceDescription,
       "aviatAlarmRaisedInstanceSeverity": aviatAlarmRaisedInstanceSeverity,
       "aviatAlarmRaisedInstanceCause": aviatAlarmRaisedInstanceCause,
       "aviatAlarmRaisedInstanceTime": aviatAlarmRaisedInstanceTime,
       "aviatAlarmRaisedInstanceIsUnstable": aviatAlarmRaisedInstanceIsUnstable,
       "aviatAlarmEntityTable": aviatAlarmEntityTable,
       "aviatAlarmEntityEntry": aviatAlarmEntityEntry,
       "aviatAlarmEntityReportingMode": aviatAlarmEntityReportingMode,
       "aviatAlarmReportingNotifications": aviatAlarmReportingNotifications,
       "aviatAlarmEntityName": aviatAlarmEntityName,
       "aviatAlarmTypeID": aviatAlarmTypeID}
)
