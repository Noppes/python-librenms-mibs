# SNMP MIB module (VS-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zenitel\VS-DEVICE-MIB

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

stentofon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26122)
)
if mibBuilder.loadTexts:
    stentofon.setRevisions(
        ("2018-06-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipstation_ObjectIdentity = ObjectIdentity
ipstation = _Ipstation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 2)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 2, 1)
)


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 1, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_ButtonHangingStatus_Type = Integer32
_ButtonHangingStatus_Object = MibScalar
buttonHangingStatus = _ButtonHangingStatus_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 1, 2),
    _ButtonHangingStatus_Type()
)
buttonHangingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buttonHangingStatus.setStatus("current")
_ButtonHangingCounter_Type = Counter32
_ButtonHangingCounter_Object = MibScalar
buttonHangingCounter = _ButtonHangingCounter_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 1, 3),
    _ButtonHangingCounter_Type()
)
buttonHangingCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buttonHangingCounter.setStatus("current")


class _SoundTestLastResult_Type(Integer32):
    """Custom type soundTestLastResult based on Integer32"""
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
        *(("unused", 0),
          ("error", 1),
          ("failed", 2),
          ("success", 3))
    )


_SoundTestLastResult_Type.__name__ = "Integer32"
_SoundTestLastResult_Object = MibScalar
soundTestLastResult = _SoundTestLastResult_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 1, 4),
    _SoundTestLastResult_Type()
)
soundTestLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soundTestLastResult.setStatus("current")
_SoundTestFailedCounter_Type = Counter32
_SoundTestFailedCounter_Object = MibScalar
soundTestFailedCounter = _SoundTestFailedCounter_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 1, 5),
    _SoundTestFailedCounter_Type()
)
soundTestFailedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soundTestFailedCounter.setStatus("current")
_SoundTestErrorCounter_Type = Counter32
_SoundTestErrorCounter_Object = MibScalar
soundTestErrorCounter = _SoundTestErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 1, 6),
    _SoundTestErrorCounter_Type()
)
soundTestErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soundTestErrorCounter.setStatus("current")
_SoundTestSuccessCounter_Type = Counter32
_SoundTestSuccessCounter_Object = MibScalar
soundTestSuccessCounter = _SoundTestSuccessCounter_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 1, 7),
    _SoundTestSuccessCounter_Type()
)
soundTestSuccessCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soundTestSuccessCounter.setStatus("current")
_Registration_ObjectIdentity = ObjectIdentity
registration = _Registration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 2, 2)
)
_RegistrationTable_Object = MibTable
registrationTable = _RegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 2, 1)
)
if mibBuilder.loadTexts:
    registrationTable.setStatus("current")
_RegistrationEntry_Object = MibTableRow
registrationEntry = _RegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 2, 1, 1)
)
registrationEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "regIndex"),
)
if mibBuilder.loadTexts:
    registrationEntry.setStatus("current")
_RegIndex_Type = Unsigned32
_RegIndex_Object = MibTableColumn
regIndex = _RegIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 2, 1, 1, 1),
    _RegIndex_Type()
)
regIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    regIndex.setStatus("current")


class _ServerType_Type(Integer32):
    """Custom type serverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("backup", 1),
          ("backup2", 2))
    )


_ServerType_Type.__name__ = "Integer32"
_ServerType_Object = MibTableColumn
serverType = _ServerType_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 2, 1, 1, 2),
    _ServerType_Type()
)
serverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverType.setStatus("current")


class _ServerAddress_Type(DisplayString):
    """Custom type serverAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ServerAddress_Type.__name__ = "DisplayString"
_ServerAddress_Object = MibTableColumn
serverAddress = _ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 2, 1, 1, 3),
    _ServerAddress_Type()
)
serverAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAddress.setStatus("current")


class _IsRegistered_Type(Integer32):
    """Custom type isRegistered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notregistered", 0),
          ("registered", 1))
    )


_IsRegistered_Type.__name__ = "Integer32"
_IsRegistered_Object = MibTableColumn
isRegistered = _IsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 2, 1, 1, 4),
    _IsRegistered_Type()
)
isRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isRegistered.setStatus("current")


class _LastRegistration_Type(DisplayString):
    """Custom type lastRegistration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LastRegistration_Type.__name__ = "DisplayString"
_LastRegistration_Object = MibTableColumn
lastRegistration = _LastRegistration_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 2, 1, 1, 5),
    _LastRegistration_Type()
)
lastRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastRegistration.setStatus("current")
_Call_ObjectIdentity = ObjectIdentity
call = _Call_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 2, 3)
)


class _CallState_Type(Integer32):
    """Custom type callState based on Integer32"""
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
        *(("idle", 0),
          ("inprogress", 1),
          ("incoming", 2),
          ("outgoing", 3),
          ("incancel", 4))
    )


_CallState_Type.__name__ = "Integer32"
_CallState_Object = MibScalar
callState = _CallState_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 3, 1),
    _CallState_Type()
)
callState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callState.setStatus("current")


class _CallRemoteId_Type(DisplayString):
    """Custom type callRemoteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CallRemoteId_Type.__name__ = "DisplayString"
_CallRemoteId_Object = MibScalar
callRemoteId = _CallRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 3, 2),
    _CallRemoteId_Type()
)
callRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callRemoteId.setStatus("current")
_IncomingCallAttempts_Type = Counter32
_IncomingCallAttempts_Object = MibScalar
incomingCallAttempts = _IncomingCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 3, 3),
    _IncomingCallAttempts_Type()
)
incomingCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingCallAttempts.setStatus("current")
_IncomingCallsSuccess_Type = Counter32
_IncomingCallsSuccess_Object = MibScalar
incomingCallsSuccess = _IncomingCallsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 3, 4),
    _IncomingCallsSuccess_Type()
)
incomingCallsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingCallsSuccess.setStatus("current")
_IncomingCallsFailed_Type = Counter32
_IncomingCallsFailed_Object = MibScalar
incomingCallsFailed = _IncomingCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 3, 5),
    _IncomingCallsFailed_Type()
)
incomingCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingCallsFailed.setStatus("current")
_OutgoingCallAttempts_Type = Counter32
_OutgoingCallAttempts_Object = MibScalar
outgoingCallAttempts = _OutgoingCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 3, 6),
    _OutgoingCallAttempts_Type()
)
outgoingCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingCallAttempts.setStatus("current")
_OutgoingCallsSuccess_Type = Counter32
_OutgoingCallsSuccess_Object = MibScalar
outgoingCallsSuccess = _OutgoingCallsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 3, 7),
    _OutgoingCallsSuccess_Type()
)
outgoingCallsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingCallsSuccess.setStatus("current")
_OutgoingCallsFailed_Type = Counter32
_OutgoingCallsFailed_Object = MibScalar
outgoingCallsFailed = _OutgoingCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 3, 8),
    _OutgoingCallsFailed_Type()
)
outgoingCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingCallsFailed.setStatus("current")
_AlarmObjects_ObjectIdentity = ObjectIdentity
alarmObjects = _AlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 2, 4)
)


class _ManagedObjectClass_Type(DisplayString):
    """Custom type managedObjectClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ManagedObjectClass_Type.__name__ = "DisplayString"
_ManagedObjectClass_Object = MibScalar
managedObjectClass = _ManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 4, 1),
    _ManagedObjectClass_Type()
)
managedObjectClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    managedObjectClass.setStatus("current")


class _ManagedObjectInstance_Type(DisplayString):
    """Custom type managedObjectInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ManagedObjectInstance_Type.__name__ = "DisplayString"
_ManagedObjectInstance_Object = MibScalar
managedObjectInstance = _ManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 4, 2),
    _ManagedObjectInstance_Type()
)
managedObjectInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    managedObjectInstance.setStatus("current")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("info", 5),
          ("cleared", 6))
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 4, 3),
    _Severity_Type()
)
severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    severity.setStatus("current")


class _Time_Type(DisplayString):
    """Custom type time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Time_Type.__name__ = "DisplayString"
_Time_Object = MibScalar
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 4, 4),
    _Time_Type()
)
time.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    time.setStatus("current")


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 26122, 2, 4, 5),
    _Description_Type()
)
description.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    description.setStatus("current")
_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5)
)
_FaultNotifications_ObjectIdentity = ObjectIdentity
faultNotifications = _FaultNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8)
)
_VsDevice_ObjectIdentity = ObjectIdentity
vsDevice = _VsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 1)
)


class _InfoPackageVersion_Type(DisplayString):
    """Custom type infoPackageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_InfoPackageVersion_Type.__name__ = "DisplayString"
_InfoPackageVersion_Object = MibScalar
infoPackageVersion = _InfoPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 1, 1),
    _InfoPackageVersion_Type()
)
infoPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPackageVersion.setStatus("current")


class _InfoModelType_Type(DisplayString):
    """Custom type infoModelType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_InfoModelType_Type.__name__ = "DisplayString"
_InfoModelType_Object = MibScalar
infoModelType = _InfoModelType_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 1, 2),
    _InfoModelType_Type()
)
infoModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModelType.setStatus("current")


class _InfoModelNumber_Type(Integer32):
    """Custom type infoModelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_InfoModelNumber_Type.__name__ = "Integer32"
_InfoModelNumber_Object = MibScalar
infoModelNumber = _InfoModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 1, 3),
    _InfoModelNumber_Type()
)
infoModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModelNumber.setStatus("current")


class _InfoAmplifierType_Type(DisplayString):
    """Custom type infoAmplifierType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_InfoAmplifierType_Type.__name__ = "DisplayString"
_InfoAmplifierType_Object = MibScalar
infoAmplifierType = _InfoAmplifierType_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 1, 4),
    _InfoAmplifierType_Type()
)
infoAmplifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoAmplifierType.setStatus("current")


class _InfoKernelVersion_Type(DisplayString):
    """Custom type infoKernelVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_InfoKernelVersion_Type.__name__ = "DisplayString"
_InfoKernelVersion_Object = MibScalar
infoKernelVersion = _InfoKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 1, 5),
    _InfoKernelVersion_Type()
)
infoKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoKernelVersion.setStatus("current")


class _InfoDeviceTreeVersion_Type(DisplayString):
    """Custom type infoDeviceTreeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_InfoDeviceTreeVersion_Type.__name__ = "DisplayString"
_InfoDeviceTreeVersion_Object = MibScalar
infoDeviceTreeVersion = _InfoDeviceTreeVersion_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 1, 6),
    _InfoDeviceTreeVersion_Type()
)
infoDeviceTreeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDeviceTreeVersion.setStatus("current")


class _InfoDisablement_Type(Integer32):
    """Custom type infoDisablement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_InfoDisablement_Type.__name__ = "Integer32"
_InfoDisablement_Object = MibScalar
infoDisablement = _InfoDisablement_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 1, 7),
    _InfoDisablement_Type()
)
infoDisablement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDisablement.setStatus("current")
_Temp_ObjectIdentity = ObjectIdentity
temp = _Temp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2)
)


class _TempTableCount_Type(Integer32):
    """Custom type tempTableCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TempTableCount_Type.__name__ = "Integer32"
_TempTableCount_Object = MibScalar
tempTableCount = _TempTableCount_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 1),
    _TempTableCount_Type()
)
tempTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempTableCount.setStatus("current")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("current")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2, 1)
)
tempEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("current")


class _TempIndex_Type(Integer32):
    """Custom type tempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TempIndex_Type.__name__ = "Integer32"
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempIndex.setStatus("current")


class _TempSensorName_Type(DisplayString):
    """Custom type tempSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_TempSensorName_Type.__name__ = "DisplayString"
_TempSensorName_Object = MibTableColumn
tempSensorName = _TempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2, 1, 2),
    _TempSensorName_Type()
)
tempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorName.setStatus("current")


class _TempCurrentString_Type(DisplayString):
    """Custom type tempCurrentString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_TempCurrentString_Type.__name__ = "DisplayString"
_TempCurrentString_Object = MibTableColumn
tempCurrentString = _TempCurrentString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2, 1, 3),
    _TempCurrentString_Type()
)
tempCurrentString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCurrentString.setStatus("current")
_TempCurrentValue_Type = Gauge32
_TempCurrentValue_Object = MibTableColumn
tempCurrentValue = _TempCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2, 1, 4),
    _TempCurrentValue_Type()
)
tempCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCurrentValue.setStatus("current")


class _TempPeakString_Type(DisplayString):
    """Custom type tempPeakString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_TempPeakString_Type.__name__ = "DisplayString"
_TempPeakString_Object = MibTableColumn
tempPeakString = _TempPeakString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2, 1, 5),
    _TempPeakString_Type()
)
tempPeakString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempPeakString.setStatus("current")
_TempPeakValue_Type = Gauge32
_TempPeakValue_Object = MibTableColumn
tempPeakValue = _TempPeakValue_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2, 1, 6),
    _TempPeakValue_Type()
)
tempPeakValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempPeakValue.setStatus("current")


class _TempAverageString_Type(DisplayString):
    """Custom type tempAverageString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_TempAverageString_Type.__name__ = "DisplayString"
_TempAverageString_Object = MibTableColumn
tempAverageString = _TempAverageString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2, 1, 7),
    _TempAverageString_Type()
)
tempAverageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAverageString.setStatus("current")
_TempAverageValue_Type = Gauge32
_TempAverageValue_Object = MibTableColumn
tempAverageValue = _TempAverageValue_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 2, 2, 1, 8),
    _TempAverageValue_Type()
)
tempAverageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAverageValue.setStatus("current")
_Fan_ObjectIdentity = ObjectIdentity
fan = _Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 3)
)


class _FanTableCount_Type(Integer32):
    """Custom type fanTableCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FanTableCount_Type.__name__ = "Integer32"
_FanTableCount_Object = MibScalar
fanTableCount = _FanTableCount_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 3, 1),
    _FanTableCount_Type()
)
fanTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanTableCount.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 3, 2)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 3, 2, 1)
)
fanEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 3, 2, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")


class _FanString_Type(DisplayString):
    """Custom type fanString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_FanString_Type.__name__ = "DisplayString"
_FanString_Object = MibTableColumn
fanString = _FanString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 3, 2, 1, 2),
    _FanString_Type()
)
fanString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanString.setStatus("current")
_FanValue_Type = Gauge32
_FanValue_Object = MibTableColumn
fanValue = _FanValue_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 3, 2, 1, 3),
    _FanValue_Type()
)
fanValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanValue.setStatus("current")
_Voltage_ObjectIdentity = ObjectIdentity
voltage = _Voltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 4)
)


class _VoltageTableCount_Type(Integer32):
    """Custom type voltageTableCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_VoltageTableCount_Type.__name__ = "Integer32"
_VoltageTableCount_Object = MibScalar
voltageTableCount = _VoltageTableCount_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 4, 1),
    _VoltageTableCount_Type()
)
voltageTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageTableCount.setStatus("current")
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 4, 2)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("current")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 4, 2, 1)
)
voltageEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("current")


class _VoltageIndex_Type(Integer32):
    """Custom type voltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_VoltageIndex_Type.__name__ = "Integer32"
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 4, 2, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")


class _VoltageString_Type(DisplayString):
    """Custom type voltageString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_VoltageString_Type.__name__ = "DisplayString"
_VoltageString_Object = MibTableColumn
voltageString = _VoltageString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 4, 2, 1, 2),
    _VoltageString_Type()
)
voltageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageString.setStatus("current")
_VoltageValue_Type = Gauge32
_VoltageValue_Object = MibTableColumn
voltageValue = _VoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 4, 2, 1, 3),
    _VoltageValue_Type()
)
voltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageValue.setStatus("current")
_Power_ObjectIdentity = ObjectIdentity
power = _Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 5)
)
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 5, 1)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("current")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 5, 1, 1)
)
powerEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "powerIndex"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("current")


class _PowerIndex_Type(Integer32):
    """Custom type powerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PowerIndex_Type.__name__ = "Integer32"
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 5, 1, 1, 1),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerIndex.setStatus("current")


class _PowerType_Type(Integer32):
    """Custom type powerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("acPower", 2),
          ("dcPower", 3),
          ("poePower", 4))
    )


_PowerType_Type.__name__ = "Integer32"
_PowerType_Object = MibTableColumn
powerType = _PowerType_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 5, 1, 1, 2),
    _PowerType_Type()
)
powerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerType.setStatus("current")


class _PowerString_Type(DisplayString):
    """Custom type powerString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_PowerString_Type.__name__ = "DisplayString"
_PowerString_Object = MibTableColumn
powerString = _PowerString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 5, 1, 1, 3),
    _PowerString_Type()
)
powerString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerString.setStatus("current")


class _PowerMonitoring_Type(Integer32):
    """Custom type powerMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notMonitored", 2),
          ("monitored", 3))
    )


_PowerMonitoring_Type.__name__ = "Integer32"
_PowerMonitoring_Object = MibTableColumn
powerMonitoring = _PowerMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 5, 1, 1, 4),
    _PowerMonitoring_Type()
)
powerMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMonitoring.setStatus("current")


class _PowerStatus_Type(Integer32):
    """Custom type powerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notConnected", 2),
          ("connected", 3))
    )


_PowerStatus_Type.__name__ = "Integer32"
_PowerStatus_Object = MibTableColumn
powerStatus = _PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 5, 1, 1, 5),
    _PowerStatus_Type()
)
powerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus.setStatus("current")
_LineIn_ObjectIdentity = ObjectIdentity
lineIn = _LineIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 6)
)
_LineInTable_Object = MibTable
lineInTable = _LineInTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 6, 1)
)
if mibBuilder.loadTexts:
    lineInTable.setStatus("current")
_LineInEntry_Object = MibTableRow
lineInEntry = _LineInEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 6, 1, 1)
)
lineInEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "lineInIndex"),
)
if mibBuilder.loadTexts:
    lineInEntry.setStatus("current")


class _LineInIndex_Type(Integer32):
    """Custom type lineInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_LineInIndex_Type.__name__ = "Integer32"
_LineInIndex_Object = MibTableColumn
lineInIndex = _LineInIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 6, 1, 1, 1),
    _LineInIndex_Type()
)
lineInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineInIndex.setStatus("current")


class _LineInMonitoringState_Type(Integer32):
    """Custom type lineInMonitoringState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notMonitored", 2),
          ("monitored", 3))
    )


_LineInMonitoringState_Type.__name__ = "Integer32"
_LineInMonitoringState_Object = MibTableColumn
lineInMonitoringState = _LineInMonitoringState_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 6, 1, 1, 2),
    _LineInMonitoringState_Type()
)
lineInMonitoringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineInMonitoringState.setStatus("current")


class _LineInType_Type(Integer32):
    """Custom type lineInType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("lineIn1", 2),
          ("lineIn2", 3),
          ("microphoneExtern", 4),
          ("microphoneIntern", 5))
    )


_LineInType_Type.__name__ = "Integer32"
_LineInType_Object = MibTableColumn
lineInType = _LineInType_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 6, 1, 1, 3),
    _LineInType_Type()
)
lineInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineInType.setStatus("current")


class _LineInString_Type(DisplayString):
    """Custom type lineInString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_LineInString_Type.__name__ = "DisplayString"
_LineInString_Object = MibTableColumn
lineInString = _LineInString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 6, 1, 1, 4),
    _LineInString_Type()
)
lineInString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineInString.setStatus("current")


class _LineInStatus_Type(Integer32):
    """Custom type lineInStatus based on Integer32"""
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
        *(("unknown", 1),
          ("lineInOk", 2),
          ("lineInFail", 3),
          ("microphoneUnknown", 4),
          ("microphoneConnected", 5),
          ("microphoneDisconnected", 6),
          ("microphoneShorted", 7))
    )


_LineInStatus_Type.__name__ = "Integer32"
_LineInStatus_Object = MibTableColumn
lineInStatus = _LineInStatus_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 6, 1, 1, 5),
    _LineInStatus_Type()
)
lineInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineInStatus.setStatus("current")
_AmpChannel_ObjectIdentity = ObjectIdentity
ampChannel = _AmpChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 7)
)


class _AmpChannelCount_Type(Integer32):
    """Custom type ampChannelCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AmpChannelCount_Type.__name__ = "Integer32"
_AmpChannelCount_Object = MibScalar
ampChannelCount = _AmpChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 7, 1),
    _AmpChannelCount_Type()
)
ampChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampChannelCount.setStatus("current")


class _AmpType_Type(Integer32):
    """Custom type ampType based on Integer32"""
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
        *(("unknown", 1),
          ("turbine", 2),
          ("ena2200", 3),
          ("ena2400", 4),
          ("ena2060", 5),
          ("ena2100", 6))
    )


_AmpType_Type.__name__ = "Integer32"
_AmpType_Object = MibScalar
ampType = _AmpType_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 7, 2),
    _AmpType_Type()
)
ampType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampType.setStatus("current")
_AmpChannelTable_Object = MibTable
ampChannelTable = _AmpChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 7, 3)
)
if mibBuilder.loadTexts:
    ampChannelTable.setStatus("current")
_AmpChannelEntry_Object = MibTableRow
ampChannelEntry = _AmpChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 7, 3, 1)
)
ampChannelEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "ampChannelIndex"),
)
if mibBuilder.loadTexts:
    ampChannelEntry.setStatus("current")


class _AmpChannelIndex_Type(Integer32):
    """Custom type ampChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AmpChannelIndex_Type.__name__ = "Integer32"
_AmpChannelIndex_Object = MibTableColumn
ampChannelIndex = _AmpChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 7, 3, 1, 1),
    _AmpChannelIndex_Type()
)
ampChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ampChannelIndex.setStatus("current")


class _AmpChannelString_Type(DisplayString):
    """Custom type ampChannelString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_AmpChannelString_Type.__name__ = "DisplayString"
_AmpChannelString_Object = MibTableColumn
ampChannelString = _AmpChannelString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 7, 3, 1, 2),
    _AmpChannelString_Type()
)
ampChannelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampChannelString.setStatus("current")


class _AmpChannelStatus_Type(Integer32):
    """Custom type ampChannelStatus based on Integer32"""
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
        *(("unknown", 1),
          ("notOperative", 2),
          ("channelOk", 3),
          ("channelFail", 4),
          ("channelShutdown", 5),
          ("channelGracefulDegradation", 6))
    )


_AmpChannelStatus_Type.__name__ = "Integer32"
_AmpChannelStatus_Object = MibTableColumn
ampChannelStatus = _AmpChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 7, 3, 1, 3),
    _AmpChannelStatus_Type()
)
ampChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampChannelStatus.setStatus("current")


class _AmpChannelMonitorStatus_Type(Integer32):
    """Custom type ampChannelMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("channelOk", 2),
          ("channelShorted", 3),
          ("channelOpen", 4),
          ("channelLoadChange", 5),
          ("channelGroundFault", 6),
          ("channelRefreshing", 7),
          ("channelShutdown", 8),
          ("channelVoltageLow", 9),
          ("channelIndecisive", 10),
          ("channelInterrupted", 11),
          ("channelTimeoutFail", 12),
          ("channelMonitoringReceiveError", 13),
          ("channelMonitoringSuspended", 14),
          ("channelLineFault", 15))
    )


_AmpChannelMonitorStatus_Type.__name__ = "Integer32"
_AmpChannelMonitorStatus_Object = MibTableColumn
ampChannelMonitorStatus = _AmpChannelMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 7, 3, 1, 4),
    _AmpChannelMonitorStatus_Type()
)
ampChannelMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampChannelMonitorStatus.setStatus("current")
_LetStatus_ObjectIdentity = ObjectIdentity
letStatus = _LetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8)
)
_LetChannel1_ObjectIdentity = ObjectIdentity
letChannel1 = _LetChannel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1)
)


class _LetChannel1Count_Type(Integer32):
    """Custom type letChannel1Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_LetChannel1Count_Type.__name__ = "Integer32"
_LetChannel1Count_Object = MibScalar
letChannel1Count = _LetChannel1Count_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1, 1),
    _LetChannel1Count_Type()
)
letChannel1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel1Count.setStatus("current")
_LetChannel1Table_Object = MibTable
letChannel1Table = _LetChannel1Table_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1, 2)
)
if mibBuilder.loadTexts:
    letChannel1Table.setStatus("current")
_LetChannel1Entry_Object = MibTableRow
letChannel1Entry = _LetChannel1Entry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1, 2, 1)
)
letChannel1Entry.setIndexNames(
    (0, "VS-DEVICE-MIB", "letChannel1Index"),
)
if mibBuilder.loadTexts:
    letChannel1Entry.setStatus("current")


class _LetChannel1Index_Type(Integer32):
    """Custom type letChannel1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LetChannel1Index_Type.__name__ = "Integer32"
_LetChannel1Index_Object = MibTableColumn
letChannel1Index = _LetChannel1Index_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1, 2, 1, 1),
    _LetChannel1Index_Type()
)
letChannel1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    letChannel1Index.setStatus("current")


class _LetChannel1Description_Type(DisplayString):
    """Custom type letChannel1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_LetChannel1Description_Type.__name__ = "DisplayString"
_LetChannel1Description_Object = MibTableColumn
letChannel1Description = _LetChannel1Description_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1, 2, 1, 2),
    _LetChannel1Description_Type()
)
letChannel1Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel1Description.setStatus("current")


class _LetChannel1OperativeStatus_Type(Integer32):
    """Custom type letChannel1OperativeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notEnabled", 2),
          ("failed", 3),
          ("ok", 4))
    )


_LetChannel1OperativeStatus_Type.__name__ = "Integer32"
_LetChannel1OperativeStatus_Object = MibTableColumn
letChannel1OperativeStatus = _LetChannel1OperativeStatus_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1, 2, 1, 3),
    _LetChannel1OperativeStatus_Type()
)
letChannel1OperativeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel1OperativeStatus.setStatus("current")


class _LetChannel1SoftwareVersion_Type(DisplayString):
    """Custom type letChannel1SoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_LetChannel1SoftwareVersion_Type.__name__ = "DisplayString"
_LetChannel1SoftwareVersion_Object = MibTableColumn
letChannel1SoftwareVersion = _LetChannel1SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1, 2, 1, 4),
    _LetChannel1SoftwareVersion_Type()
)
letChannel1SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel1SoftwareVersion.setStatus("current")


class _LetChannel1HardwareVersion_Type(DisplayString):
    """Custom type letChannel1HardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_LetChannel1HardwareVersion_Type.__name__ = "DisplayString"
_LetChannel1HardwareVersion_Object = MibTableColumn
letChannel1HardwareVersion = _LetChannel1HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1, 2, 1, 5),
    _LetChannel1HardwareVersion_Type()
)
letChannel1HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel1HardwareVersion.setStatus("current")


class _LetChannel1Voltage_Type(Gauge32):
    """Custom type letChannel1Voltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 39999),
    )


_LetChannel1Voltage_Type.__name__ = "Gauge32"
_LetChannel1Voltage_Object = MibTableColumn
letChannel1Voltage = _LetChannel1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 1, 2, 1, 6),
    _LetChannel1Voltage_Type()
)
letChannel1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel1Voltage.setStatus("current")
_LetChannel2_ObjectIdentity = ObjectIdentity
letChannel2 = _LetChannel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2)
)


class _LetChannel2Count_Type(Integer32):
    """Custom type letChannel2Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_LetChannel2Count_Type.__name__ = "Integer32"
_LetChannel2Count_Object = MibScalar
letChannel2Count = _LetChannel2Count_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2, 1),
    _LetChannel2Count_Type()
)
letChannel2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel2Count.setStatus("current")
_LetChannel2Table_Object = MibTable
letChannel2Table = _LetChannel2Table_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2, 2)
)
if mibBuilder.loadTexts:
    letChannel2Table.setStatus("current")
_LetChannel2Entry_Object = MibTableRow
letChannel2Entry = _LetChannel2Entry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2, 2, 1)
)
letChannel2Entry.setIndexNames(
    (0, "VS-DEVICE-MIB", "letChannel2Index"),
)
if mibBuilder.loadTexts:
    letChannel2Entry.setStatus("current")


class _LetChannel2Index_Type(Integer32):
    """Custom type letChannel2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LetChannel2Index_Type.__name__ = "Integer32"
_LetChannel2Index_Object = MibTableColumn
letChannel2Index = _LetChannel2Index_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2, 2, 1, 1),
    _LetChannel2Index_Type()
)
letChannel2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    letChannel2Index.setStatus("current")


class _LetChannel2Description_Type(DisplayString):
    """Custom type letChannel2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_LetChannel2Description_Type.__name__ = "DisplayString"
_LetChannel2Description_Object = MibTableColumn
letChannel2Description = _LetChannel2Description_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2, 2, 1, 2),
    _LetChannel2Description_Type()
)
letChannel2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel2Description.setStatus("current")


class _LetChannel2OperativeStatus_Type(Integer32):
    """Custom type letChannel2OperativeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notEnabled", 2),
          ("failed", 3),
          ("ok", 4))
    )


_LetChannel2OperativeStatus_Type.__name__ = "Integer32"
_LetChannel2OperativeStatus_Object = MibTableColumn
letChannel2OperativeStatus = _LetChannel2OperativeStatus_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2, 2, 1, 3),
    _LetChannel2OperativeStatus_Type()
)
letChannel2OperativeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel2OperativeStatus.setStatus("current")


class _LetChannel2SoftwareVersion_Type(DisplayString):
    """Custom type letChannel2SoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_LetChannel2SoftwareVersion_Type.__name__ = "DisplayString"
_LetChannel2SoftwareVersion_Object = MibTableColumn
letChannel2SoftwareVersion = _LetChannel2SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2, 2, 1, 4),
    _LetChannel2SoftwareVersion_Type()
)
letChannel2SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel2SoftwareVersion.setStatus("current")


class _LetChannel2HardwareVersion_Type(DisplayString):
    """Custom type letChannel2HardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_LetChannel2HardwareVersion_Type.__name__ = "DisplayString"
_LetChannel2HardwareVersion_Object = MibTableColumn
letChannel2HardwareVersion = _LetChannel2HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2, 2, 1, 5),
    _LetChannel2HardwareVersion_Type()
)
letChannel2HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel2HardwareVersion.setStatus("current")


class _LetChannel2Voltage_Type(Gauge32):
    """Custom type letChannel2Voltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 39999),
    )


_LetChannel2Voltage_Type.__name__ = "Gauge32"
_LetChannel2Voltage_Object = MibTableColumn
letChannel2Voltage = _LetChannel2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 8, 2, 2, 1, 6),
    _LetChannel2Voltage_Type()
)
letChannel2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letChannel2Voltage.setStatus("current")
_ControlInput_ObjectIdentity = ObjectIdentity
controlInput = _ControlInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 9)
)


class _ControlInputCount_Type(Integer32):
    """Custom type controlInputCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ControlInputCount_Type.__name__ = "Integer32"
_ControlInputCount_Object = MibScalar
controlInputCount = _ControlInputCount_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 9, 1),
    _ControlInputCount_Type()
)
controlInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlInputCount.setStatus("current")
_ControlInputTable_Object = MibTable
controlInputTable = _ControlInputTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 9, 2)
)
if mibBuilder.loadTexts:
    controlInputTable.setStatus("current")
_ControlInputEntry_Object = MibTableRow
controlInputEntry = _ControlInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 9, 2, 1)
)
controlInputEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "controlInputIndex"),
)
if mibBuilder.loadTexts:
    controlInputEntry.setStatus("current")


class _ControlInputIndex_Type(Integer32):
    """Custom type controlInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ControlInputIndex_Type.__name__ = "Integer32"
_ControlInputIndex_Object = MibTableColumn
controlInputIndex = _ControlInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 9, 2, 1, 1),
    _ControlInputIndex_Type()
)
controlInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlInputIndex.setStatus("current")


class _ControlInputString_Type(DisplayString):
    """Custom type controlInputString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_ControlInputString_Type.__name__ = "DisplayString"
_ControlInputString_Object = MibTableColumn
controlInputString = _ControlInputString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 9, 2, 1, 2),
    _ControlInputString_Type()
)
controlInputString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlInputString.setStatus("current")


class _ControlInputStatus_Type(Integer32):
    """Custom type controlInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("open", 2),
          ("closed", 3),
          ("failShorted", 4),
          ("failOpen", 5))
    )


_ControlInputStatus_Type.__name__ = "Integer32"
_ControlInputStatus_Object = MibTableColumn
controlInputStatus = _ControlInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 9, 2, 1, 3),
    _ControlInputStatus_Type()
)
controlInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlInputStatus.setStatus("current")


class _ControlInputMonitored_Type(Integer32):
    """Custom type controlInputMonitored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMonitored", 1),
          ("monitored", 2))
    )


_ControlInputMonitored_Type.__name__ = "Integer32"
_ControlInputMonitored_Object = MibTableColumn
controlInputMonitored = _ControlInputMonitored_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 9, 2, 1, 4),
    _ControlInputMonitored_Type()
)
controlInputMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlInputMonitored.setStatus("current")
_ControlOutput_ObjectIdentity = ObjectIdentity
controlOutput = _ControlOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 10)
)


class _ControlOutputCount_Type(Integer32):
    """Custom type controlOutputCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ControlOutputCount_Type.__name__ = "Integer32"
_ControlOutputCount_Object = MibScalar
controlOutputCount = _ControlOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 10, 1),
    _ControlOutputCount_Type()
)
controlOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlOutputCount.setStatus("current")
_ControlOutputTable_Object = MibTable
controlOutputTable = _ControlOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 10, 2)
)
if mibBuilder.loadTexts:
    controlOutputTable.setStatus("current")
_ControlOutputEntry_Object = MibTableRow
controlOutputEntry = _ControlOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 10, 2, 1)
)
controlOutputEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "controlOutputIndex"),
)
if mibBuilder.loadTexts:
    controlOutputEntry.setStatus("current")


class _ControlOutputIndex_Type(Integer32):
    """Custom type controlOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ControlOutputIndex_Type.__name__ = "Integer32"
_ControlOutputIndex_Object = MibTableColumn
controlOutputIndex = _ControlOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 10, 2, 1, 1),
    _ControlOutputIndex_Type()
)
controlOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlOutputIndex.setStatus("current")


class _ControlOutputString_Type(DisplayString):
    """Custom type controlOutputString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_ControlOutputString_Type.__name__ = "DisplayString"
_ControlOutputString_Object = MibTableColumn
controlOutputString = _ControlOutputString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 10, 2, 1, 2),
    _ControlOutputString_Type()
)
controlOutputString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlOutputString.setStatus("current")


class _ControlOutputStatus_Type(Integer32):
    """Custom type controlOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notActive", 2),
          ("active", 3),
          ("failNotActive", 4),
          ("failActive", 5))
    )


_ControlOutputStatus_Type.__name__ = "Integer32"
_ControlOutputStatus_Object = MibTableColumn
controlOutputStatus = _ControlOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 10, 2, 1, 3),
    _ControlOutputStatus_Type()
)
controlOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlOutputStatus.setStatus("current")
_Eth_ObjectIdentity = ObjectIdentity
eth = _Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 11)
)
_EthMonitoringTable_Object = MibTable
ethMonitoringTable = _EthMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 11, 1)
)
if mibBuilder.loadTexts:
    ethMonitoringTable.setStatus("current")
_EthMonitoringEntry_Object = MibTableRow
ethMonitoringEntry = _EthMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 11, 1, 1)
)
ethMonitoringEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "ethMonitoringIndex"),
)
if mibBuilder.loadTexts:
    ethMonitoringEntry.setStatus("current")


class _EthMonitoringIndex_Type(Integer32):
    """Custom type ethMonitoringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EthMonitoringIndex_Type.__name__ = "Integer32"
_EthMonitoringIndex_Object = MibTableColumn
ethMonitoringIndex = _EthMonitoringIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 11, 1, 1, 1),
    _EthMonitoringIndex_Type()
)
ethMonitoringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethMonitoringIndex.setStatus("current")


class _EthMonitoringString_Type(DisplayString):
    """Custom type ethMonitoringString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_EthMonitoringString_Type.__name__ = "DisplayString"
_EthMonitoringString_Object = MibTableColumn
ethMonitoringString = _EthMonitoringString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 11, 1, 1, 2),
    _EthMonitoringString_Type()
)
ethMonitoringString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethMonitoringString.setStatus("current")


class _EthMonitoringState_Type(Integer32):
    """Custom type ethMonitoringState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notMonitored", 2),
          ("monitored", 3))
    )


_EthMonitoringState_Type.__name__ = "Integer32"
_EthMonitoringState_Object = MibTableColumn
ethMonitoringState = _EthMonitoringState_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 11, 1, 1, 3),
    _EthMonitoringState_Type()
)
ethMonitoringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethMonitoringState.setStatus("current")
_Relay_ObjectIdentity = ObjectIdentity
relay = _Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 3, 12)
)
_RelayTable_Object = MibTable
relayTable = _RelayTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 12, 1)
)
if mibBuilder.loadTexts:
    relayTable.setStatus("current")
_RelayEntry_Object = MibTableRow
relayEntry = _RelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 12, 1, 1)
)
relayEntry.setIndexNames(
    (0, "VS-DEVICE-MIB", "relayIndex"),
)
if mibBuilder.loadTexts:
    relayEntry.setStatus("current")


class _RelayIndex_Type(Integer32):
    """Custom type relayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RelayIndex_Type.__name__ = "Integer32"
_RelayIndex_Object = MibTableColumn
relayIndex = _RelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 12, 1, 1, 1),
    _RelayIndex_Type()
)
relayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    relayIndex.setStatus("current")


class _RelayString_Type(DisplayString):
    """Custom type relayString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_RelayString_Type.__name__ = "DisplayString"
_RelayString_Object = MibTableColumn
relayString = _RelayString_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 12, 1, 1, 2),
    _RelayString_Type()
)
relayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayString.setStatus("current")


class _RelayIdleMode_Type(Integer32):
    """Custom type relayIdleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("normallyClosed", 2),
          ("normallyOpen", 3))
    )


_RelayIdleMode_Type.__name__ = "Integer32"
_RelayIdleMode_Object = MibTableColumn
relayIdleMode = _RelayIdleMode_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 12, 1, 1, 3),
    _RelayIdleMode_Type()
)
relayIdleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayIdleMode.setStatus("current")


class _RelayDelay_Type(Integer32):
    """Custom type relayDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RelayDelay_Type.__name__ = "Integer32"
_RelayDelay_Object = MibTableColumn
relayDelay = _RelayDelay_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 12, 1, 1, 4),
    _RelayDelay_Type()
)
relayDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayDelay.setStatus("current")


class _RelayState_Type(Integer32):
    """Custom type relayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notActive", 2),
          ("active", 3))
    )


_RelayState_Type.__name__ = "Integer32"
_RelayState_Object = MibTableColumn
relayState = _RelayState_Object(
    (1, 3, 6, 1, 4, 1, 26122, 3, 12, 1, 1, 5),
    _RelayState_Type()
)
relayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayState.setStatus("current")
_StentofonMIBConformance_ObjectIdentity = ObjectIdentity
stentofonMIBConformance = _StentofonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 4)
)
_StentofonMIBCompliances_ObjectIdentity = ObjectIdentity
stentofonMIBCompliances = _StentofonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 4, 1)
)
_StentofonMIBGroups_ObjectIdentity = ObjectIdentity
stentofonMIBGroups = _StentofonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2)
)

# Managed Objects groups

sipRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 1)
)
sipRegistrationGroup.setObjects(
      *(("VS-DEVICE-MIB", "serverType"),
        ("VS-DEVICE-MIB", "serverAddress"),
        ("VS-DEVICE-MIB", "isRegistered"),
        ("VS-DEVICE-MIB", "lastRegistration"))
)
if mibBuilder.loadTexts:
    sipRegistrationGroup.setStatus("current")

sipCallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 2)
)
sipCallGroup.setObjects(
      *(("VS-DEVICE-MIB", "callState"),
        ("VS-DEVICE-MIB", "callRemoteId"),
        ("VS-DEVICE-MIB", "incomingCallAttempts"),
        ("VS-DEVICE-MIB", "incomingCallsSuccess"),
        ("VS-DEVICE-MIB", "incomingCallsFailed"),
        ("VS-DEVICE-MIB", "outgoingCallAttempts"),
        ("VS-DEVICE-MIB", "outgoingCallsSuccess"),
        ("VS-DEVICE-MIB", "outgoingCallsFailed"))
)
if mibBuilder.loadTexts:
    sipCallGroup.setStatus("current")

sipGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 3)
)
sipGeneralGroup.setObjects(
      *(("VS-DEVICE-MIB", "softwareVersion"),
        ("VS-DEVICE-MIB", "buttonHangingStatus"),
        ("VS-DEVICE-MIB", "buttonHangingCounter"),
        ("VS-DEVICE-MIB", "soundTestLastResult"),
        ("VS-DEVICE-MIB", "soundTestFailedCounter"),
        ("VS-DEVICE-MIB", "soundTestErrorCounter"),
        ("VS-DEVICE-MIB", "soundTestSuccessCounter"))
)
if mibBuilder.loadTexts:
    sipGeneralGroup.setStatus("current")

alarmObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 4)
)
alarmObjectsGroup.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    alarmObjectsGroup.setStatus("current")

deviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 7)
)
deviceInfoGroup.setObjects(
      *(("VS-DEVICE-MIB", "infoPackageVersion"),
        ("VS-DEVICE-MIB", "infoModelType"),
        ("VS-DEVICE-MIB", "infoModelNumber"),
        ("VS-DEVICE-MIB", "infoAmplifierType"),
        ("VS-DEVICE-MIB", "infoKernelVersion"),
        ("VS-DEVICE-MIB", "infoDeviceTreeVersion"),
        ("VS-DEVICE-MIB", "infoDisablement"))
)
if mibBuilder.loadTexts:
    deviceInfoGroup.setStatus("current")

deviceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 8)
)
deviceStatusGroup.setObjects(
      *(("VS-DEVICE-MIB", "tempTableCount"),
        ("VS-DEVICE-MIB", "tempSensorName"),
        ("VS-DEVICE-MIB", "tempCurrentString"),
        ("VS-DEVICE-MIB", "tempCurrentValue"),
        ("VS-DEVICE-MIB", "tempPeakString"),
        ("VS-DEVICE-MIB", "tempPeakValue"),
        ("VS-DEVICE-MIB", "tempAverageString"),
        ("VS-DEVICE-MIB", "tempAverageValue"),
        ("VS-DEVICE-MIB", "fanTableCount"),
        ("VS-DEVICE-MIB", "fanString"),
        ("VS-DEVICE-MIB", "fanValue"),
        ("VS-DEVICE-MIB", "voltageTableCount"),
        ("VS-DEVICE-MIB", "voltageString"),
        ("VS-DEVICE-MIB", "voltageValue"),
        ("VS-DEVICE-MIB", "powerType"),
        ("VS-DEVICE-MIB", "powerString"),
        ("VS-DEVICE-MIB", "powerMonitoring"),
        ("VS-DEVICE-MIB", "powerStatus"))
)
if mibBuilder.loadTexts:
    deviceStatusGroup.setStatus("current")

audioInputsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 9)
)
audioInputsGroup.setObjects(
      *(("VS-DEVICE-MIB", "lineInMonitoringState"),
        ("VS-DEVICE-MIB", "lineInType"),
        ("VS-DEVICE-MIB", "lineInString"),
        ("VS-DEVICE-MIB", "lineInStatus"))
)
if mibBuilder.loadTexts:
    audioInputsGroup.setStatus("current")

controlIOGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 10)
)
controlIOGroup.setObjects(
      *(("VS-DEVICE-MIB", "controlInputCount"),
        ("VS-DEVICE-MIB", "controlInputString"),
        ("VS-DEVICE-MIB", "controlInputStatus"),
        ("VS-DEVICE-MIB", "controlInputMonitored"),
        ("VS-DEVICE-MIB", "controlOutputCount"),
        ("VS-DEVICE-MIB", "controlOutputString"),
        ("VS-DEVICE-MIB", "controlOutputStatus"),
        ("VS-DEVICE-MIB", "relayString"),
        ("VS-DEVICE-MIB", "relayIdleMode"),
        ("VS-DEVICE-MIB", "relayDelay"),
        ("VS-DEVICE-MIB", "relayState"))
)
if mibBuilder.loadTexts:
    controlIOGroup.setStatus("current")

ethernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 11)
)
ethernetGroup.setObjects(
      *(("VS-DEVICE-MIB", "ethMonitoringString"),
        ("VS-DEVICE-MIB", "ethMonitoringState"))
)
if mibBuilder.loadTexts:
    ethernetGroup.setStatus("current")

amplifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 12)
)
amplifierGroup.setObjects(
      *(("VS-DEVICE-MIB", "ampChannelCount"),
        ("VS-DEVICE-MIB", "ampType"),
        ("VS-DEVICE-MIB", "ampChannelString"),
        ("VS-DEVICE-MIB", "ampChannelStatus"),
        ("VS-DEVICE-MIB", "ampChannelMonitorStatus"))
)
if mibBuilder.loadTexts:
    amplifierGroup.setStatus("current")

letsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 13)
)
letsGroup.setObjects(
      *(("VS-DEVICE-MIB", "letChannel1Count"),
        ("VS-DEVICE-MIB", "letChannel1Description"),
        ("VS-DEVICE-MIB", "letChannel1OperativeStatus"),
        ("VS-DEVICE-MIB", "letChannel1SoftwareVersion"),
        ("VS-DEVICE-MIB", "letChannel1HardwareVersion"),
        ("VS-DEVICE-MIB", "letChannel1Voltage"),
        ("VS-DEVICE-MIB", "letChannel2Count"),
        ("VS-DEVICE-MIB", "letChannel2Description"),
        ("VS-DEVICE-MIB", "letChannel2OperativeStatus"),
        ("VS-DEVICE-MIB", "letChannel2SoftwareVersion"),
        ("VS-DEVICE-MIB", "letChannel2HardwareVersion"),
        ("VS-DEVICE-MIB", "letChannel2Voltage"))
)
if mibBuilder.loadTexts:
    letsGroup.setStatus("current")


# Notification objects

ipsStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 1)
)
ipsStarted.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    ipsStarted.setStatus(
        "current"
    )

ipsShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 2)
)
ipsShutdown.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    ipsShutdown.setStatus(
        "current"
    )

sipRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 3)
)
sipRegistered.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    sipRegistered.setStatus(
        "current"
    )

sipUnregistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 4)
)
sipUnregistered.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    sipUnregistered.setStatus(
        "current"
    )

sipRegisterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 5)
)
sipRegisterFailed.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    sipRegisterFailed.setStatus(
        "current"
    )

callConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 6)
)
callConnect.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    callConnect.setStatus(
        "current"
    )

callConnectFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 7)
)
callConnectFailed.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    callConnectFailed.setStatus(
        "current"
    )

callDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 8)
)
callDisconnect.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    callDisconnect.setStatus(
        "current"
    )

callAbnormalDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 9)
)
callAbnormalDisconnect.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    callAbnormalDisconnect.setStatus(
        "current"
    )

soundTestSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 10)
)
soundTestSuccess.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    soundTestSuccess.setStatus(
        "current"
    )

soundTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 11)
)
soundTestFailed.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    soundTestFailed.setStatus(
        "current"
    )

soundTestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 12)
)
soundTestError.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    soundTestError.setStatus(
        "current"
    )

buttonHanging = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 13)
)
buttonHanging.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    buttonHanging.setStatus(
        "current"
    )

buttonPressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 14)
)
buttonPressed.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    buttonPressed.setStatus(
        "current"
    )

buttonReleased = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 15)
)
buttonReleased.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    buttonReleased.setStatus(
        "current"
    )

relayActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 16)
)
relayActivated.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    relayActivated.setStatus(
        "current"
    )

relayDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 17)
)
relayDeactivated.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    relayDeactivated.setStatus(
        "current"
    )

dakPressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 18)
)
dakPressed.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    dakPressed.setStatus(
        "current"
    )

dakReleased = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 5, 19)
)
dakReleased.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    dakReleased.setStatus(
        "current"
    )

coolingFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 1)
)
coolingFanFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    coolingFanFault.setStatus(
        "current"
    )

missingAmpModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 2)
)
missingAmpModule.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    missingAmpModule.setStatus(
        "current"
    )

psuVoltageFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 3)
)
psuVoltageFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    psuVoltageFault.setStatus(
        "current"
    )

lineVoltageFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 4)
)
lineVoltageFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    lineVoltageFault.setStatus(
        "current"
    )

letFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 5)
)
letFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    letFault.setStatus(
        "current"
    )

ampShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 6)
)
ampShutdown.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    ampShutdown.setStatus(
        "current"
    )

slmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 7)
)
slmFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    slmFault.setStatus(
        "current"
    )

fuseBroken = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 8)
)
fuseBroken.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    fuseBroken.setStatus(
        "current"
    )

ampDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 9)
)
ampDisabled.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    ampDisabled.setStatus(
        "current"
    )

lineInFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 10)
)
lineInFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    lineInFault.setStatus(
        "current"
    )

rcoFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 11)
)
rcoFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    rcoFault.setStatus(
        "current"
    )

rciFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 12)
)
rciFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    rciFault.setStatus(
        "current"
    )

dcPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 13)
)
dcPowerFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    dcPowerFault.setStatus(
        "current"
    )

acPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 14)
)
acPowerFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    acPowerFault.setStatus(
        "current"
    )

ethPortDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 15)
)
ethPortDisconnected.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    ethPortDisconnected.setStatus(
        "current"
    )

micFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 16)
)
micFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    micFault.setStatus(
        "current"
    )

missingEmbdr = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 17)
)
missingEmbdr.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    missingEmbdr.setStatus(
        "current"
    )

swFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 18)
)
swFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    swFault.setStatus(
        "current"
    )

tempFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 19)
)
tempFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    tempFault.setStatus(
        "current"
    )

customFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 2, 8, 20)
)
customFault.setObjects(
      *(("VS-DEVICE-MIB", "managedObjectClass"),
        ("VS-DEVICE-MIB", "managedObjectInstance"),
        ("VS-DEVICE-MIB", "severity"),
        ("VS-DEVICE-MIB", "time"),
        ("VS-DEVICE-MIB", "description"))
)
if mibBuilder.loadTexts:
    customFault.setStatus(
        "current"
    )


# Notifications groups

sipNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 5)
)
sipNotificationsGroup.setObjects(
      *(("VS-DEVICE-MIB", "ipsStarted"),
        ("VS-DEVICE-MIB", "ipsShutdown"),
        ("VS-DEVICE-MIB", "sipRegistered"),
        ("VS-DEVICE-MIB", "sipUnregistered"),
        ("VS-DEVICE-MIB", "sipRegisterFailed"),
        ("VS-DEVICE-MIB", "callConnect"),
        ("VS-DEVICE-MIB", "callConnectFailed"),
        ("VS-DEVICE-MIB", "callDisconnect"),
        ("VS-DEVICE-MIB", "callAbnormalDisconnect"),
        ("VS-DEVICE-MIB", "soundTestSuccess"),
        ("VS-DEVICE-MIB", "soundTestFailed"),
        ("VS-DEVICE-MIB", "soundTestError"),
        ("VS-DEVICE-MIB", "buttonHanging"),
        ("VS-DEVICE-MIB", "buttonPressed"),
        ("VS-DEVICE-MIB", "buttonReleased"),
        ("VS-DEVICE-MIB", "relayActivated"),
        ("VS-DEVICE-MIB", "relayDeactivated"),
        ("VS-DEVICE-MIB", "dakPressed"),
        ("VS-DEVICE-MIB", "dakReleased"))
)
if mibBuilder.loadTexts:
    sipNotificationsGroup.setStatus(
        "current"
    )

faultNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 26122, 4, 2, 6)
)
faultNotificationsGroup.setObjects(
      *(("VS-DEVICE-MIB", "coolingFanFault"),
        ("VS-DEVICE-MIB", "missingAmpModule"),
        ("VS-DEVICE-MIB", "psuVoltageFault"),
        ("VS-DEVICE-MIB", "lineVoltageFault"),
        ("VS-DEVICE-MIB", "letFault"),
        ("VS-DEVICE-MIB", "ampShutdown"),
        ("VS-DEVICE-MIB", "slmFault"),
        ("VS-DEVICE-MIB", "fuseBroken"),
        ("VS-DEVICE-MIB", "ampDisabled"),
        ("VS-DEVICE-MIB", "lineInFault"),
        ("VS-DEVICE-MIB", "rcoFault"),
        ("VS-DEVICE-MIB", "rciFault"),
        ("VS-DEVICE-MIB", "dcPowerFault"),
        ("VS-DEVICE-MIB", "acPowerFault"),
        ("VS-DEVICE-MIB", "ethPortDisconnected"),
        ("VS-DEVICE-MIB", "micFault"),
        ("VS-DEVICE-MIB", "missingEmbdr"),
        ("VS-DEVICE-MIB", "swFault"),
        ("VS-DEVICE-MIB", "tempFault"),
        ("VS-DEVICE-MIB", "customFault"))
)
if mibBuilder.loadTexts:
    faultNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

stentofonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 26122, 4, 1, 1)
)
stentofonCompliance.setObjects(
      *(("VS-DEVICE-MIB", "alarmObjectsGroup"),
        ("VS-DEVICE-MIB", "sipNotificationsGroup"),
        ("VS-DEVICE-MIB", "faultNotificationsGroup"),
        ("VS-DEVICE-MIB", "deviceInfoGroup"),
        ("VS-DEVICE-MIB", "sipGeneralGroup"),
        ("VS-DEVICE-MIB", "sipRegistrationGroup"),
        ("VS-DEVICE-MIB", "sipCallGroup"),
        ("VS-DEVICE-MIB", "deviceStatusGroup"),
        ("VS-DEVICE-MIB", "audioInputsGroup"),
        ("VS-DEVICE-MIB", "controlIOGroup"),
        ("VS-DEVICE-MIB", "ethernetGroup"),
        ("VS-DEVICE-MIB", "amplifierGroup"),
        ("VS-DEVICE-MIB", "letsGroup"))
)
if mibBuilder.loadTexts:
    stentofonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VS-DEVICE-MIB",
    **{"stentofon": stentofon,
       "ipstation": ipstation,
       "general": general,
       "softwareVersion": softwareVersion,
       "buttonHangingStatus": buttonHangingStatus,
       "buttonHangingCounter": buttonHangingCounter,
       "soundTestLastResult": soundTestLastResult,
       "soundTestFailedCounter": soundTestFailedCounter,
       "soundTestErrorCounter": soundTestErrorCounter,
       "soundTestSuccessCounter": soundTestSuccessCounter,
       "registration": registration,
       "registrationTable": registrationTable,
       "registrationEntry": registrationEntry,
       "regIndex": regIndex,
       "serverType": serverType,
       "serverAddress": serverAddress,
       "isRegistered": isRegistered,
       "lastRegistration": lastRegistration,
       "call": call,
       "callState": callState,
       "callRemoteId": callRemoteId,
       "incomingCallAttempts": incomingCallAttempts,
       "incomingCallsSuccess": incomingCallsSuccess,
       "incomingCallsFailed": incomingCallsFailed,
       "outgoingCallAttempts": outgoingCallAttempts,
       "outgoingCallsSuccess": outgoingCallsSuccess,
       "outgoingCallsFailed": outgoingCallsFailed,
       "alarmObjects": alarmObjects,
       "managedObjectClass": managedObjectClass,
       "managedObjectInstance": managedObjectInstance,
       "severity": severity,
       "time": time,
       "description": description,
       "alarmNotifications": alarmNotifications,
       "ipsStarted": ipsStarted,
       "ipsShutdown": ipsShutdown,
       "sipRegistered": sipRegistered,
       "sipUnregistered": sipUnregistered,
       "sipRegisterFailed": sipRegisterFailed,
       "callConnect": callConnect,
       "callConnectFailed": callConnectFailed,
       "callDisconnect": callDisconnect,
       "callAbnormalDisconnect": callAbnormalDisconnect,
       "soundTestSuccess": soundTestSuccess,
       "soundTestFailed": soundTestFailed,
       "soundTestError": soundTestError,
       "buttonHanging": buttonHanging,
       "buttonPressed": buttonPressed,
       "buttonReleased": buttonReleased,
       "relayActivated": relayActivated,
       "relayDeactivated": relayDeactivated,
       "dakPressed": dakPressed,
       "dakReleased": dakReleased,
       "faultNotifications": faultNotifications,
       "coolingFanFault": coolingFanFault,
       "missingAmpModule": missingAmpModule,
       "psuVoltageFault": psuVoltageFault,
       "lineVoltageFault": lineVoltageFault,
       "letFault": letFault,
       "ampShutdown": ampShutdown,
       "slmFault": slmFault,
       "fuseBroken": fuseBroken,
       "ampDisabled": ampDisabled,
       "lineInFault": lineInFault,
       "rcoFault": rcoFault,
       "rciFault": rciFault,
       "dcPowerFault": dcPowerFault,
       "acPowerFault": acPowerFault,
       "ethPortDisconnected": ethPortDisconnected,
       "micFault": micFault,
       "missingEmbdr": missingEmbdr,
       "swFault": swFault,
       "tempFault": tempFault,
       "customFault": customFault,
       "vsDevice": vsDevice,
       "info": info,
       "infoPackageVersion": infoPackageVersion,
       "infoModelType": infoModelType,
       "infoModelNumber": infoModelNumber,
       "infoAmplifierType": infoAmplifierType,
       "infoKernelVersion": infoKernelVersion,
       "infoDeviceTreeVersion": infoDeviceTreeVersion,
       "infoDisablement": infoDisablement,
       "temp": temp,
       "tempTableCount": tempTableCount,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempSensorName": tempSensorName,
       "tempCurrentString": tempCurrentString,
       "tempCurrentValue": tempCurrentValue,
       "tempPeakString": tempPeakString,
       "tempPeakValue": tempPeakValue,
       "tempAverageString": tempAverageString,
       "tempAverageValue": tempAverageValue,
       "fan": fan,
       "fanTableCount": fanTableCount,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanString": fanString,
       "fanValue": fanValue,
       "voltage": voltage,
       "voltageTableCount": voltageTableCount,
       "voltageTable": voltageTable,
       "voltageEntry": voltageEntry,
       "voltageIndex": voltageIndex,
       "voltageString": voltageString,
       "voltageValue": voltageValue,
       "power": power,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "powerIndex": powerIndex,
       "powerType": powerType,
       "powerString": powerString,
       "powerMonitoring": powerMonitoring,
       "powerStatus": powerStatus,
       "lineIn": lineIn,
       "lineInTable": lineInTable,
       "lineInEntry": lineInEntry,
       "lineInIndex": lineInIndex,
       "lineInMonitoringState": lineInMonitoringState,
       "lineInType": lineInType,
       "lineInString": lineInString,
       "lineInStatus": lineInStatus,
       "ampChannel": ampChannel,
       "ampChannelCount": ampChannelCount,
       "ampType": ampType,
       "ampChannelTable": ampChannelTable,
       "ampChannelEntry": ampChannelEntry,
       "ampChannelIndex": ampChannelIndex,
       "ampChannelString": ampChannelString,
       "ampChannelStatus": ampChannelStatus,
       "ampChannelMonitorStatus": ampChannelMonitorStatus,
       "letStatus": letStatus,
       "letChannel1": letChannel1,
       "letChannel1Count": letChannel1Count,
       "letChannel1Table": letChannel1Table,
       "letChannel1Entry": letChannel1Entry,
       "letChannel1Index": letChannel1Index,
       "letChannel1Description": letChannel1Description,
       "letChannel1OperativeStatus": letChannel1OperativeStatus,
       "letChannel1SoftwareVersion": letChannel1SoftwareVersion,
       "letChannel1HardwareVersion": letChannel1HardwareVersion,
       "letChannel1Voltage": letChannel1Voltage,
       "letChannel2": letChannel2,
       "letChannel2Count": letChannel2Count,
       "letChannel2Table": letChannel2Table,
       "letChannel2Entry": letChannel2Entry,
       "letChannel2Index": letChannel2Index,
       "letChannel2Description": letChannel2Description,
       "letChannel2OperativeStatus": letChannel2OperativeStatus,
       "letChannel2SoftwareVersion": letChannel2SoftwareVersion,
       "letChannel2HardwareVersion": letChannel2HardwareVersion,
       "letChannel2Voltage": letChannel2Voltage,
       "controlInput": controlInput,
       "controlInputCount": controlInputCount,
       "controlInputTable": controlInputTable,
       "controlInputEntry": controlInputEntry,
       "controlInputIndex": controlInputIndex,
       "controlInputString": controlInputString,
       "controlInputStatus": controlInputStatus,
       "controlInputMonitored": controlInputMonitored,
       "controlOutput": controlOutput,
       "controlOutputCount": controlOutputCount,
       "controlOutputTable": controlOutputTable,
       "controlOutputEntry": controlOutputEntry,
       "controlOutputIndex": controlOutputIndex,
       "controlOutputString": controlOutputString,
       "controlOutputStatus": controlOutputStatus,
       "eth": eth,
       "ethMonitoringTable": ethMonitoringTable,
       "ethMonitoringEntry": ethMonitoringEntry,
       "ethMonitoringIndex": ethMonitoringIndex,
       "ethMonitoringString": ethMonitoringString,
       "ethMonitoringState": ethMonitoringState,
       "relay": relay,
       "relayTable": relayTable,
       "relayEntry": relayEntry,
       "relayIndex": relayIndex,
       "relayString": relayString,
       "relayIdleMode": relayIdleMode,
       "relayDelay": relayDelay,
       "relayState": relayState,
       "stentofonMIBConformance": stentofonMIBConformance,
       "stentofonMIBCompliances": stentofonMIBCompliances,
       "stentofonCompliance": stentofonCompliance,
       "stentofonMIBGroups": stentofonMIBGroups,
       "sipRegistrationGroup": sipRegistrationGroup,
       "sipCallGroup": sipCallGroup,
       "sipGeneralGroup": sipGeneralGroup,
       "alarmObjectsGroup": alarmObjectsGroup,
       "sipNotificationsGroup": sipNotificationsGroup,
       "faultNotificationsGroup": faultNotificationsGroup,
       "deviceInfoGroup": deviceInfoGroup,
       "deviceStatusGroup": deviceStatusGroup,
       "audioInputsGroup": audioInputsGroup,
       "controlIOGroup": controlIOGroup,
       "ethernetGroup": ethernetGroup,
       "amplifierGroup": amplifierGroup,
       "letsGroup": letsGroup}
)
