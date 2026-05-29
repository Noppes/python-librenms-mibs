# SNMP MIB module (G6-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsens\G6-SYSTEM-MIB

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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2023-02-14 11:27",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30)
)
_SystemShowTimeDate_Type = DisplayString
_SystemShowTimeDate_Object = MibScalar
systemShowTimeDate = _SystemShowTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 1),
    _SystemShowTimeDate_Type()
)
systemShowTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemShowTimeDate.setStatus("current")
_SystemSetTime_Type = DisplayString
_SystemSetTime_Object = MibScalar
systemSetTime = _SystemSetTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 2),
    _SystemSetTime_Type()
)
systemSetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSetTime.setStatus("current")
_SystemSetDate_Type = DisplayString
_SystemSetDate_Object = MibScalar
systemSetDate = _SystemSetDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 3),
    _SystemSetDate_Type()
)
systemSetDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSetDate.setStatus("current")
_SystemShowUtilization_Type = DisplayString
_SystemShowUtilization_Object = MibScalar
systemShowUtilization = _SystemShowUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 4),
    _SystemShowUtilization_Type()
)
systemShowUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemShowUtilization.setStatus("current")
_SystemRebootDevice_Type = DisplayString
_SystemRebootDevice_Object = MibScalar
systemRebootDevice = _SystemRebootDevice_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 5),
    _SystemRebootDevice_Type()
)
systemRebootDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRebootDevice.setStatus("current")
_SystemCreateSnapshot_Type = DisplayString
_SystemCreateSnapshot_Object = MibScalar
systemCreateSnapshot = _SystemCreateSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 6),
    _SystemCreateSnapshot_Type()
)
systemCreateSnapshot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemCreateSnapshot.setStatus("current")
_SystemSendWakeOnLanPacket_Type = DisplayString
_SystemSendWakeOnLanPacket_Object = MibScalar
systemSendWakeOnLanPacket = _SystemSendWakeOnLanPacket_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 7),
    _SystemSendWakeOnLanPacket_Type()
)
systemSendWakeOnLanPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSendWakeOnLanPacket.setStatus("current")
_SystemAlternativeMacAddress_Type = MacAddress
_SystemAlternativeMacAddress_Object = MibScalar
systemAlternativeMacAddress = _SystemAlternativeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 8),
    _SystemAlternativeMacAddress_Type()
)
systemAlternativeMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAlternativeMacAddress.setStatus("current")


class _SystemBootPreference_Type(Integer32):
    """Custom type systemBootPreference based on Integer32"""
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
        *(("sdCardFirst", 0),
          ("internalFirst", 1),
          ("sdCardOnly", 2),
          ("internalOnly", 3))
    )


_SystemBootPreference_Type.__name__ = "Integer32"
_SystemBootPreference_Object = MibScalar
systemBootPreference = _SystemBootPreference_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 9),
    _SystemBootPreference_Type()
)
systemBootPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemBootPreference.setStatus("current")
_SystemInventory_Type = DisplayString
_SystemInventory_Object = MibScalar
systemInventory = _SystemInventory_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 10),
    _SystemInventory_Type()
)
systemInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemInventory.setStatus("current")
_SystemAutorunCliScript_Type = DisplayString
_SystemAutorunCliScript_Object = MibScalar
systemAutorunCliScript = _SystemAutorunCliScript_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 11),
    _SystemAutorunCliScript_Type()
)
systemAutorunCliScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAutorunCliScript.setStatus("current")


class _SystemSerialPort_Type(Integer32):
    """Custom type systemSerialPort based on Integer32"""
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
        *(("disabled", 0),
          ("console", 1),
          ("appControlled", 2),
          ("terminalServer", 3),
          ("smartSensor", 4))
    )


_SystemSerialPort_Type.__name__ = "Integer32"
_SystemSerialPort_Object = MibScalar
systemSerialPort = _SystemSerialPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 12),
    _SystemSerialPort_Type()
)
systemSerialPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSerialPort.setStatus("current")


class _SystemPermitDebugAccess_Type(Integer32):
    """Custom type systemPermitDebugAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemPermitDebugAccess_Type.__name__ = "Integer32"
_SystemPermitDebugAccess_Object = MibScalar
systemPermitDebugAccess = _SystemPermitDebugAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 13),
    _SystemPermitDebugAccess_Type()
)
systemPermitDebugAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPermitDebugAccess.setStatus("current")


class _SystemPermitIncomingAlerts_Type(Integer32):
    """Custom type systemPermitIncomingAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemPermitIncomingAlerts_Type.__name__ = "Integer32"
_SystemPermitIncomingAlerts_Object = MibScalar
systemPermitIncomingAlerts = _SystemPermitIncomingAlerts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 14),
    _SystemPermitIncomingAlerts_Type()
)
systemPermitIncomingAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPermitIncomingAlerts.setStatus("current")


class _SystemCharacterSet_Type(Integer32):
    """Custom type systemCharacterSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("iso88591", 1),
          ("iso88595", 5))
    )


_SystemCharacterSet_Type.__name__ = "Integer32"
_SystemCharacterSet_Object = MibScalar
systemCharacterSet = _SystemCharacterSet_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15),
    _SystemCharacterSet_Type()
)
systemCharacterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemCharacterSet.setStatus("current")


class _SystemConfigurationSaveMode_Type(Integer32):
    """Custom type systemConfigurationSaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permanently", 0),
          ("temporarily", 1))
    )


_SystemConfigurationSaveMode_Type.__name__ = "Integer32"
_SystemConfigurationSaveMode_Object = MibScalar
systemConfigurationSaveMode = _SystemConfigurationSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 16),
    _SystemConfigurationSaveMode_Type()
)
systemConfigurationSaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigurationSaveMode.setStatus("current")
_CompatibilityTable_Object = MibTable
compatibilityTable = _CompatibilityTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 17)
)
if mibBuilder.loadTexts:
    compatibilityTable.setStatus("current")
_CompatibilityEntry_Object = MibTableRow
compatibilityEntry = _CompatibilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 17, 1)
)
compatibilityEntry.setIndexNames(
    (0, "G6-SYSTEM-MIB", "compatibilityIndex"),
)
if mibBuilder.loadTexts:
    compatibilityEntry.setStatus("current")


class _CompatibilityIndex_Type(Integer32):
    """Custom type compatibilityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_CompatibilityIndex_Type.__name__ = "Integer32"
_CompatibilityIndex_Object = MibTableColumn
compatibilityIndex = _CompatibilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 17, 1, 1),
    _CompatibilityIndex_Type()
)
compatibilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    compatibilityIndex.setStatus("current")


class _CompatibilityLinkDetection_Type(Integer32):
    """Custom type compatibilityLinkDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pollAndInterrupt", 0),
          ("interruptOnly", 1))
    )


_CompatibilityLinkDetection_Type.__name__ = "Integer32"
_CompatibilityLinkDetection_Object = MibTableColumn
compatibilityLinkDetection = _CompatibilityLinkDetection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 17, 1, 2),
    _CompatibilityLinkDetection_Type()
)
compatibilityLinkDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compatibilityLinkDetection.setStatus("current")
_ScriptScheduleTable_Object = MibTable
scriptScheduleTable = _ScriptScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18)
)
if mibBuilder.loadTexts:
    scriptScheduleTable.setStatus("current")
_ScriptScheduleEntry_Object = MibTableRow
scriptScheduleEntry = _ScriptScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1)
)
scriptScheduleEntry.setIndexNames(
    (0, "G6-SYSTEM-MIB", "scriptScheduleIndex"),
)
if mibBuilder.loadTexts:
    scriptScheduleEntry.setStatus("current")


class _ScriptScheduleIndex_Type(Integer32):
    """Custom type scriptScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ScriptScheduleIndex_Type.__name__ = "Integer32"
_ScriptScheduleIndex_Object = MibTableColumn
scriptScheduleIndex = _ScriptScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1, 1),
    _ScriptScheduleIndex_Type()
)
scriptScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scriptScheduleIndex.setStatus("current")
_ScriptScheduleName_Type = DisplayString
_ScriptScheduleName_Object = MibTableColumn
scriptScheduleName = _ScriptScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1, 2),
    _ScriptScheduleName_Type()
)
scriptScheduleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleName.setStatus("current")


class _ScriptScheduleMode_Type(Integer32):
    """Custom type scriptScheduleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ScriptScheduleMode_Type.__name__ = "Integer32"
_ScriptScheduleMode_Object = MibTableColumn
scriptScheduleMode = _ScriptScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1, 3),
    _ScriptScheduleMode_Type()
)
scriptScheduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleMode.setStatus("current")
_ScriptScheduleCliScript_Type = DisplayString
_ScriptScheduleCliScript_Object = MibTableColumn
scriptScheduleCliScript = _ScriptScheduleCliScript_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1, 4),
    _ScriptScheduleCliScript_Type()
)
scriptScheduleCliScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleCliScript.setStatus("current")
_ScriptScheduleMinutes_Type = DisplayString
_ScriptScheduleMinutes_Object = MibTableColumn
scriptScheduleMinutes = _ScriptScheduleMinutes_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1, 5),
    _ScriptScheduleMinutes_Type()
)
scriptScheduleMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleMinutes.setStatus("current")
_ScriptScheduleHours_Type = DisplayString
_ScriptScheduleHours_Object = MibTableColumn
scriptScheduleHours = _ScriptScheduleHours_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1, 6),
    _ScriptScheduleHours_Type()
)
scriptScheduleHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleHours.setStatus("current")
_ScriptScheduleDays_Type = DisplayString
_ScriptScheduleDays_Object = MibTableColumn
scriptScheduleDays = _ScriptScheduleDays_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1, 7),
    _ScriptScheduleDays_Type()
)
scriptScheduleDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleDays.setStatus("current")
_ScriptScheduleMonths_Type = DisplayString
_ScriptScheduleMonths_Object = MibTableColumn
scriptScheduleMonths = _ScriptScheduleMonths_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1, 8),
    _ScriptScheduleMonths_Type()
)
scriptScheduleMonths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleMonths.setStatus("current")
_ScriptScheduleWeekdays_Type = DisplayString
_ScriptScheduleWeekdays_Object = MibTableColumn
scriptScheduleWeekdays = _ScriptScheduleWeekdays_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 18, 1, 9),
    _ScriptScheduleWeekdays_Type()
)
scriptScheduleWeekdays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleWeekdays.setStatus("current")
_SystemLastBootTime_Type = DisplayString
_SystemLastBootTime_Object = MibScalar
systemLastBootTime = _SystemLastBootTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 100),
    _SystemLastBootTime_Type()
)
systemLastBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLastBootTime.setStatus("current")
_SystemUptime_Type = Counter32
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 101),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_SystemUsedMacAddress_Type = MacAddress
_SystemUsedMacAddress_Object = MibScalar
systemUsedMacAddress = _SystemUsedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 102),
    _SystemUsedMacAddress_Type()
)
systemUsedMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUsedMacAddress.setStatus("current")


class _SystemUsedBootMedia_Type(Integer32):
    """Custom type systemUsedBootMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdCard", 0),
          ("internalMemory", 1),
          ("nfs", 2))
    )


_SystemUsedBootMedia_Type.__name__ = "Integer32"
_SystemUsedBootMedia_Object = MibScalar
systemUsedBootMedia = _SystemUsedBootMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 103),
    _SystemUsedBootMedia_Type()
)
systemUsedBootMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUsedBootMedia.setStatus("current")


class _SystemTemperature_Type(Integer32):
    """Custom type systemTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemTemperature_Type.__name__ = "Integer32"
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 104),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")


class _SystemClimateLevel_Type(Integer32):
    """Custom type systemClimateLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("criticalLow", 1),
          ("low", 2),
          ("normal", 3),
          ("increased", 4),
          ("high", 5),
          ("criticalHigh", 6),
          ("shutdown", 7))
    )


_SystemClimateLevel_Type.__name__ = "Integer32"
_SystemClimateLevel_Object = MibScalar
systemClimateLevel = _SystemClimateLevel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 105),
    _SystemClimateLevel_Type()
)
systemClimateLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemClimateLevel.setStatus("current")
_FirmwareTable_Object = MibTable
firmwareTable = _FirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106)
)
if mibBuilder.loadTexts:
    firmwareTable.setStatus("current")
_FirmwareEntry_Object = MibTableRow
firmwareEntry = _FirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1)
)
firmwareEntry.setIndexNames(
    (0, "G6-SYSTEM-MIB", "firmwareIndex"),
)
if mibBuilder.loadTexts:
    firmwareEntry.setStatus("current")


class _FirmwareIndex_Type(Integer32):
    """Custom type firmwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_FirmwareIndex_Type.__name__ = "Integer32"
_FirmwareIndex_Object = MibTableColumn
firmwareIndex = _FirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 1),
    _FirmwareIndex_Type()
)
firmwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    firmwareIndex.setStatus("current")
_FirmwareRunningVersion_Type = DisplayString
_FirmwareRunningVersion_Object = MibTableColumn
firmwareRunningVersion = _FirmwareRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 2),
    _FirmwareRunningVersion_Type()
)
firmwareRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareRunningVersion.setStatus("current")
_FirmwareBuildDate_Type = DisplayString
_FirmwareBuildDate_Object = MibTableColumn
firmwareBuildDate = _FirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 3),
    _FirmwareBuildDate_Type()
)
firmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareBuildDate.setStatus("current")
_FirmwareBuildNumber_Type = DisplayString
_FirmwareBuildNumber_Object = MibTableColumn
firmwareBuildNumber = _FirmwareBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 4),
    _FirmwareBuildNumber_Type()
)
firmwareBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareBuildNumber.setStatus("current")
_FirmwarePatchVersion_Type = DisplayString
_FirmwarePatchVersion_Object = MibTableColumn
firmwarePatchVersion = _FirmwarePatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 5),
    _FirmwarePatchVersion_Type()
)
firmwarePatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwarePatchVersion.setStatus("current")
_SaveInfoTable_Object = MibTable
saveInfoTable = _SaveInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107)
)
if mibBuilder.loadTexts:
    saveInfoTable.setStatus("current")
_SaveInfoEntry_Object = MibTableRow
saveInfoEntry = _SaveInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1)
)
saveInfoEntry.setIndexNames(
    (0, "G6-SYSTEM-MIB", "saveInfoIndex"),
)
if mibBuilder.loadTexts:
    saveInfoEntry.setStatus("current")


class _SaveInfoIndex_Type(Integer32):
    """Custom type saveInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_SaveInfoIndex_Type.__name__ = "Integer32"
_SaveInfoIndex_Object = MibTableColumn
saveInfoIndex = _SaveInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 1),
    _SaveInfoIndex_Type()
)
saveInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saveInfoIndex.setStatus("current")
_SaveInfoLastSavedParameter_Type = DisplayString
_SaveInfoLastSavedParameter_Object = MibTableColumn
saveInfoLastSavedParameter = _SaveInfoLastSavedParameter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 2),
    _SaveInfoLastSavedParameter_Type()
)
saveInfoLastSavedParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saveInfoLastSavedParameter.setStatus("current")


class _SaveInfoSaveMode_Type(Integer32):
    """Custom type saveInfoSaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permanently", 0),
          ("temporarily", 1))
    )


_SaveInfoSaveMode_Type.__name__ = "Integer32"
_SaveInfoSaveMode_Object = MibTableColumn
saveInfoSaveMode = _SaveInfoSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 3),
    _SaveInfoSaveMode_Type()
)
saveInfoSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saveInfoSaveMode.setStatus("current")


class _SaveInfoWriteStatus_Type(Integer32):
    """Custom type saveInfoWriteStatus based on Integer32"""
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
        *(("nothingToSave", 0),
          ("processing", 1),
          ("savedToRam", 2),
          ("savedToSdcard", 3))
    )


_SaveInfoWriteStatus_Type.__name__ = "Integer32"
_SaveInfoWriteStatus_Object = MibTableColumn
saveInfoWriteStatus = _SaveInfoWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 4),
    _SaveInfoWriteStatus_Type()
)
saveInfoWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saveInfoWriteStatus.setStatus("current")
_SaveInfoTimeStamp_Type = Counter32
_SaveInfoTimeStamp_Object = MibTableColumn
saveInfoTimeStamp = _SaveInfoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 5),
    _SaveInfoTimeStamp_Type()
)
saveInfoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saveInfoTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-SYSTEM-MIB",
    **{"device": device,
       "system": system,
       "systemShowTimeDate": systemShowTimeDate,
       "systemSetTime": systemSetTime,
       "systemSetDate": systemSetDate,
       "systemShowUtilization": systemShowUtilization,
       "systemRebootDevice": systemRebootDevice,
       "systemCreateSnapshot": systemCreateSnapshot,
       "systemSendWakeOnLanPacket": systemSendWakeOnLanPacket,
       "systemAlternativeMacAddress": systemAlternativeMacAddress,
       "systemBootPreference": systemBootPreference,
       "systemInventory": systemInventory,
       "systemAutorunCliScript": systemAutorunCliScript,
       "systemSerialPort": systemSerialPort,
       "systemPermitDebugAccess": systemPermitDebugAccess,
       "systemPermitIncomingAlerts": systemPermitIncomingAlerts,
       "systemCharacterSet": systemCharacterSet,
       "systemConfigurationSaveMode": systemConfigurationSaveMode,
       "compatibilityTable": compatibilityTable,
       "compatibilityEntry": compatibilityEntry,
       "compatibilityIndex": compatibilityIndex,
       "compatibilityLinkDetection": compatibilityLinkDetection,
       "scriptScheduleTable": scriptScheduleTable,
       "scriptScheduleEntry": scriptScheduleEntry,
       "scriptScheduleIndex": scriptScheduleIndex,
       "scriptScheduleName": scriptScheduleName,
       "scriptScheduleMode": scriptScheduleMode,
       "scriptScheduleCliScript": scriptScheduleCliScript,
       "scriptScheduleMinutes": scriptScheduleMinutes,
       "scriptScheduleHours": scriptScheduleHours,
       "scriptScheduleDays": scriptScheduleDays,
       "scriptScheduleMonths": scriptScheduleMonths,
       "scriptScheduleWeekdays": scriptScheduleWeekdays,
       "systemLastBootTime": systemLastBootTime,
       "systemUptime": systemUptime,
       "systemUsedMacAddress": systemUsedMacAddress,
       "systemUsedBootMedia": systemUsedBootMedia,
       "systemTemperature": systemTemperature,
       "systemClimateLevel": systemClimateLevel,
       "firmwareTable": firmwareTable,
       "firmwareEntry": firmwareEntry,
       "firmwareIndex": firmwareIndex,
       "firmwareRunningVersion": firmwareRunningVersion,
       "firmwareBuildDate": firmwareBuildDate,
       "firmwareBuildNumber": firmwareBuildNumber,
       "firmwarePatchVersion": firmwarePatchVersion,
       "saveInfoTable": saveInfoTable,
       "saveInfoEntry": saveInfoEntry,
       "saveInfoIndex": saveInfoIndex,
       "saveInfoLastSavedParameter": saveInfoLastSavedParameter,
       "saveInfoSaveMode": saveInfoSaveMode,
       "saveInfoWriteStatus": saveInfoWriteStatus,
       "saveInfoTimeStamp": saveInfoTimeStamp}
)
