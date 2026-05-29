# SNMP MIB module (VERTIV-ITA2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vertiv\VERTIV-ITA2-MIB

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ita2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(TextualConvention, Integer32):
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
        *(("informational", 0),
          ("warning", 1),
          ("critical", 2))
    )



class StatusChange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activated", 0),
          ("deactivated", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Vertiv_ObjectIdentity = ObjectIdentity
Vertiv = _Vertiv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2)
)
_Ident_ObjectIdentity = ObjectIdentity
ident = _Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 1)
)
_IdentManufacturer_Type = DisplayString
_IdentManufacturer_Object = MibScalar
identManufacturer = _IdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 1, 1),
    _IdentManufacturer_Type()
)
identManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identManufacturer.setStatus("current")
_IdentModel_Type = DisplayString
_IdentModel_Object = MibScalar
identModel = _IdentModel_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 1, 2),
    _IdentModel_Type()
)
identModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identModel.setStatus("current")
_IdentIndex_Type = Integer32
_IdentIndex_Object = MibScalar
identIndex = _IdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 1, 3),
    _IdentIndex_Type()
)
identIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIndex.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 1)
)
_SystemStatus_Type = Status
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 1, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")


class _UpsOutputSource_Type(Integer32):
    """Custom type upsOutputSource based on Integer32"""
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
        *(("UPSNoOutput", 0),
          ("UPSOnMain", 1),
          ("UPSOnBattery", 2),
          ("UPSOnBypass", 3),
          ("UPSonUtilityandBattery", 4))
    )


_UpsOutputSource_Type.__name__ = "Integer32"
_UpsOutputSource_Object = MibScalar
upsOutputSource = _UpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 1, 2),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("current")
_Input_ObjectIdentity = ObjectIdentity
input = _Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 2)
)
_InputPhaseVoltageA_Type = Integer32
_InputPhaseVoltageA_Object = MibScalar
inputPhaseVoltageA = _InputPhaseVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 2, 1),
    _InputPhaseVoltageA_Type()
)
inputPhaseVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseVoltageA.setStatus("current")
_InputPhaseVoltageB_Type = Integer32
_InputPhaseVoltageB_Object = MibScalar
inputPhaseVoltageB = _InputPhaseVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 2, 2),
    _InputPhaseVoltageB_Type()
)
inputPhaseVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseVoltageB.setStatus("current")
_InputPhaseVoltageC_Type = Integer32
_InputPhaseVoltageC_Object = MibScalar
inputPhaseVoltageC = _InputPhaseVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 2, 3),
    _InputPhaseVoltageC_Type()
)
inputPhaseVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseVoltageC.setStatus("current")
_InputFrequency_Type = Integer32
_InputFrequency_Object = MibScalar
inputFrequency = _InputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 2, 4),
    _InputFrequency_Type()
)
inputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputFrequency.setStatus("current")
_InputPhaseCurrentA_Type = Integer32
_InputPhaseCurrentA_Object = MibScalar
inputPhaseCurrentA = _InputPhaseCurrentA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 2, 5),
    _InputPhaseCurrentA_Type()
)
inputPhaseCurrentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseCurrentA.setStatus("current")
_InputPhaseCurrentB_Type = Integer32
_InputPhaseCurrentB_Object = MibScalar
inputPhaseCurrentB = _InputPhaseCurrentB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 2, 6),
    _InputPhaseCurrentB_Type()
)
inputPhaseCurrentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseCurrentB.setStatus("current")
_InputPhaseCurrentC_Type = Integer32
_InputPhaseCurrentC_Object = MibScalar
inputPhaseCurrentC = _InputPhaseCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 2, 7),
    _InputPhaseCurrentC_Type()
)
inputPhaseCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseCurrentC.setStatus("current")
_Output_ObjectIdentity = ObjectIdentity
output = _Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3)
)
_OutputPhaseVoltageA_Type = Integer32
_OutputPhaseVoltageA_Object = MibScalar
outputPhaseVoltageA = _OutputPhaseVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 1),
    _OutputPhaseVoltageA_Type()
)
outputPhaseVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPhaseVoltageA.setStatus("current")
_OutputPhaseVoltageB_Type = Integer32
_OutputPhaseVoltageB_Object = MibScalar
outputPhaseVoltageB = _OutputPhaseVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 2),
    _OutputPhaseVoltageB_Type()
)
outputPhaseVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPhaseVoltageB.setStatus("current")
_OutputPhaseVoltageC_Type = Integer32
_OutputPhaseVoltageC_Object = MibScalar
outputPhaseVoltageC = _OutputPhaseVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 3),
    _OutputPhaseVoltageC_Type()
)
outputPhaseVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPhaseVoltageC.setStatus("current")
_OutputCurrentA_Type = Integer32
_OutputCurrentA_Object = MibScalar
outputCurrentA = _OutputCurrentA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 4),
    _OutputCurrentA_Type()
)
outputCurrentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentA.setStatus("current")
_OutputCurrentB_Type = Integer32
_OutputCurrentB_Object = MibScalar
outputCurrentB = _OutputCurrentB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 5),
    _OutputCurrentB_Type()
)
outputCurrentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentB.setStatus("current")
_OutputCurrentC_Type = Integer32
_OutputCurrentC_Object = MibScalar
outputCurrentC = _OutputCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 6),
    _OutputCurrentC_Type()
)
outputCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentC.setStatus("current")
_OutputFrequency_Type = Integer32
_OutputFrequency_Object = MibScalar
outputFrequency = _OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 7),
    _OutputFrequency_Type()
)
outputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputFrequency.setStatus("current")
_OutputActivePowerA_Type = Integer32
_OutputActivePowerA_Object = MibScalar
outputActivePowerA = _OutputActivePowerA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 8),
    _OutputActivePowerA_Type()
)
outputActivePowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputActivePowerA.setStatus("current")
_OutputActivePowerB_Type = Integer32
_OutputActivePowerB_Object = MibScalar
outputActivePowerB = _OutputActivePowerB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 9),
    _OutputActivePowerB_Type()
)
outputActivePowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputActivePowerB.setStatus("current")
_OutputActivePowerC_Type = Integer32
_OutputActivePowerC_Object = MibScalar
outputActivePowerC = _OutputActivePowerC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 10),
    _OutputActivePowerC_Type()
)
outputActivePowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputActivePowerC.setStatus("current")
_OutputApparentPowerA_Type = Integer32
_OutputApparentPowerA_Object = MibScalar
outputApparentPowerA = _OutputApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 11),
    _OutputApparentPowerA_Type()
)
outputApparentPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputApparentPowerA.setStatus("current")
_OutputApparentPowerB_Type = Integer32
_OutputApparentPowerB_Object = MibScalar
outputApparentPowerB = _OutputApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 12),
    _OutputApparentPowerB_Type()
)
outputApparentPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputApparentPowerB.setStatus("current")
_OutputApparentPowerC_Type = Integer32
_OutputApparentPowerC_Object = MibScalar
outputApparentPowerC = _OutputApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 13),
    _OutputApparentPowerC_Type()
)
outputApparentPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputApparentPowerC.setStatus("current")
_OutputLoadA_Type = Integer32
_OutputLoadA_Object = MibScalar
outputLoadA = _OutputLoadA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 14),
    _OutputLoadA_Type()
)
outputLoadA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputLoadA.setStatus("current")
_OutputLoadB_Type = Integer32
_OutputLoadB_Object = MibScalar
outputLoadB = _OutputLoadB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 15),
    _OutputLoadB_Type()
)
outputLoadB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputLoadB.setStatus("current")
_OutputLoadC_Type = Integer32
_OutputLoadC_Object = MibScalar
outputLoadC = _OutputLoadC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 16),
    _OutputLoadC_Type()
)
outputLoadC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputLoadC.setStatus("current")
_OutputPowerFactorA_Type = Integer32
_OutputPowerFactorA_Object = MibScalar
outputPowerFactorA = _OutputPowerFactorA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 17),
    _OutputPowerFactorA_Type()
)
outputPowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPowerFactorA.setStatus("current")
_OutputPowerFactorB_Type = Integer32
_OutputPowerFactorB_Object = MibScalar
outputPowerFactorB = _OutputPowerFactorB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 18),
    _OutputPowerFactorB_Type()
)
outputPowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPowerFactorB.setStatus("current")
_OutputPowerFactorC_Type = Integer32
_OutputPowerFactorC_Object = MibScalar
outputPowerFactorC = _OutputPowerFactorC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 3, 19),
    _OutputPowerFactorC_Type()
)
outputPowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPowerFactorC.setStatus("current")
_Bypass_ObjectIdentity = ObjectIdentity
bypass = _Bypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 4)
)
_BypassVoltageA_Type = Integer32
_BypassVoltageA_Object = MibScalar
bypassVoltageA = _BypassVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 4, 1),
    _BypassVoltageA_Type()
)
bypassVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassVoltageA.setStatus("current")
_BypassVoltageB_Type = Integer32
_BypassVoltageB_Object = MibScalar
bypassVoltageB = _BypassVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 4, 2),
    _BypassVoltageB_Type()
)
bypassVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassVoltageB.setStatus("current")
_BypassVoltageC_Type = Integer32
_BypassVoltageC_Object = MibScalar
bypassVoltageC = _BypassVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 4, 3),
    _BypassVoltageC_Type()
)
bypassVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassVoltageC.setStatus("current")
_BypassFrequency_Type = Integer32
_BypassFrequency_Object = MibScalar
bypassFrequency = _BypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 4, 4),
    _BypassFrequency_Type()
)
bypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassFrequency.setStatus("current")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5)
)
_PositiveBatteryVoltage_Type = Integer32
_PositiveBatteryVoltage_Object = MibScalar
positiveBatteryVoltage = _PositiveBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 1),
    _PositiveBatteryVoltage_Type()
)
positiveBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    positiveBatteryVoltage.setStatus("current")
_NegativeBatteryVoltage_Type = Integer32
_NegativeBatteryVoltage_Object = MibScalar
negativeBatteryVoltage = _NegativeBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 2),
    _NegativeBatteryVoltage_Type()
)
negativeBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    negativeBatteryVoltage.setStatus("current")
_PositiveBatteryChargingCurrent_Type = Integer32
_PositiveBatteryChargingCurrent_Object = MibScalar
positiveBatteryChargingCurrent = _PositiveBatteryChargingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 3),
    _PositiveBatteryChargingCurrent_Type()
)
positiveBatteryChargingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    positiveBatteryChargingCurrent.setStatus("current")
_PositiveBatteryDischargingCurrent_Type = Integer32
_PositiveBatteryDischargingCurrent_Object = MibScalar
positiveBatteryDischargingCurrent = _PositiveBatteryDischargingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 4),
    _PositiveBatteryDischargingCurrent_Type()
)
positiveBatteryDischargingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    positiveBatteryDischargingCurrent.setStatus("current")
_NegativeBatteryChargingCurrent_Type = Integer32
_NegativeBatteryChargingCurrent_Object = MibScalar
negativeBatteryChargingCurrent = _NegativeBatteryChargingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 5),
    _NegativeBatteryChargingCurrent_Type()
)
negativeBatteryChargingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    negativeBatteryChargingCurrent.setStatus("current")
_NegativeBatteryDischargingCurrent_Type = Integer32
_NegativeBatteryDischargingCurrent_Object = MibScalar
negativeBatteryDischargingCurrent = _NegativeBatteryDischargingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 6),
    _NegativeBatteryDischargingCurrent_Type()
)
negativeBatteryDischargingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    negativeBatteryDischargingCurrent.setStatus("current")
_BatteryRemainsTime_Type = Integer32
_BatteryRemainsTime_Object = MibScalar
batteryRemainsTime = _BatteryRemainsTime_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 7),
    _BatteryRemainsTime_Type()
)
batteryRemainsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRemainsTime.setStatus("current")
_BatteryTemperature_Type = Integer32
_BatteryTemperature_Object = MibScalar
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 8),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("current")
_BatteryEnvironmentTemperature_Type = Integer32
_BatteryEnvironmentTemperature_Object = MibScalar
batteryEnvironmentTemperature = _BatteryEnvironmentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 9),
    _BatteryEnvironmentTemperature_Type()
)
batteryEnvironmentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnvironmentTemperature.setStatus("current")
_BatteryCapacity_Type = Integer32
_BatteryCapacity_Object = MibScalar
batteryCapacity = _BatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 10),
    _BatteryCapacity_Type()
)
batteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCapacity.setStatus("current")
_BatteryDischargeTimes_Type = Integer32
_BatteryDischargeTimes_Object = MibScalar
batteryDischargeTimes = _BatteryDischargeTimes_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 5, 11),
    _BatteryDischargeTimes_Type()
)
batteryDischargeTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryDischargeTimes.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6)
)


class _CtrlBatteryTestStart_Type(Integer32):
    """Custom type ctrlBatteryTestStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlBatteryTestStart_Type.__name__ = "Integer32"
_CtrlBatteryTestStart_Object = MibScalar
ctrlBatteryTestStart = _CtrlBatteryTestStart_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 1),
    _CtrlBatteryTestStart_Type()
)
ctrlBatteryTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlBatteryTestStart.setStatus("current")


class _CtrlBatteryTestEnd_Type(Integer32):
    """Custom type ctrlBatteryTestEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlBatteryTestEnd_Type.__name__ = "Integer32"
_CtrlBatteryTestEnd_Object = MibScalar
ctrlBatteryTestEnd = _CtrlBatteryTestEnd_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 2),
    _CtrlBatteryTestEnd_Type()
)
ctrlBatteryTestEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlBatteryTestEnd.setStatus("current")


class _CtrlTurnOn_Type(Integer32):
    """Custom type ctrlTurnOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlTurnOn_Type.__name__ = "Integer32"
_CtrlTurnOn_Object = MibScalar
ctrlTurnOn = _CtrlTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 3),
    _CtrlTurnOn_Type()
)
ctrlTurnOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlTurnOn.setStatus("current")


class _CtrlTurnOff_Type(Integer32):
    """Custom type ctrlTurnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlTurnOff_Type.__name__ = "Integer32"
_CtrlTurnOff_Object = MibScalar
ctrlTurnOff = _CtrlTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 4),
    _CtrlTurnOff_Type()
)
ctrlTurnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlTurnOff.setStatus("current")


class _CtrlTurnOffOutput_Type(Integer32):
    """Custom type ctrlTurnOffOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlTurnOffOutput_Type.__name__ = "Integer32"
_CtrlTurnOffOutput_Object = MibScalar
ctrlTurnOffOutput = _CtrlTurnOffOutput_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 5),
    _CtrlTurnOffOutput_Type()
)
ctrlTurnOffOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlTurnOffOutput.setStatus("current")


class _CtrlTurnOnDelay_Type(Integer32):
    """Custom type ctrlTurnOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlTurnOnDelay_Type.__name__ = "Integer32"
_CtrlTurnOnDelay_Object = MibScalar
ctrlTurnOnDelay = _CtrlTurnOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 6),
    _CtrlTurnOnDelay_Type()
)
ctrlTurnOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlTurnOnDelay.setStatus("current")


class _CtrlTurnOffOutputDelayStart_Type(Integer32):
    """Custom type ctrlTurnOffOutputDelayStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlTurnOffOutputDelayStart_Type.__name__ = "Integer32"
_CtrlTurnOffOutputDelayStart_Object = MibScalar
ctrlTurnOffOutputDelayStart = _CtrlTurnOffOutputDelayStart_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 7),
    _CtrlTurnOffOutputDelayStart_Type()
)
ctrlTurnOffOutputDelayStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlTurnOffOutputDelayStart.setStatus("current")


class _CtrlTurnOffOutputDelayEnd_Type(Integer32):
    """Custom type ctrlTurnOffOutputDelayEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlTurnOffOutputDelayEnd_Type.__name__ = "Integer32"
_CtrlTurnOffOutputDelayEnd_Object = MibScalar
ctrlTurnOffOutputDelayEnd = _CtrlTurnOffOutputDelayEnd_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 8),
    _CtrlTurnOffOutputDelayEnd_Type()
)
ctrlTurnOffOutputDelayEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlTurnOffOutputDelayEnd.setStatus("current")


class _CtrlBatteryMaintenanceTestStart_Type(Integer32):
    """Custom type ctrlBatteryMaintenanceTestStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlBatteryMaintenanceTestStart_Type.__name__ = "Integer32"
_CtrlBatteryMaintenanceTestStart_Object = MibScalar
ctrlBatteryMaintenanceTestStart = _CtrlBatteryMaintenanceTestStart_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 9),
    _CtrlBatteryMaintenanceTestStart_Type()
)
ctrlBatteryMaintenanceTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlBatteryMaintenanceTestStart.setStatus("current")


class _CtrlBatteryMaintenanceTestEnd_Type(Integer32):
    """Custom type ctrlBatteryMaintenanceTestEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CtrlBatteryMaintenanceTestEnd_Type.__name__ = "Integer32"
_CtrlBatteryMaintenanceTestEnd_Object = MibScalar
ctrlBatteryMaintenanceTestEnd = _CtrlBatteryMaintenanceTestEnd_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 6, 10),
    _CtrlBatteryMaintenanceTestEnd_Type()
)
ctrlBatteryMaintenanceTestEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlBatteryMaintenanceTestEnd.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 7)
)
_ConfSelfStartDelayTime_Type = Integer32
_ConfSelfStartDelayTime_Object = MibScalar
confSelfStartDelayTime = _ConfSelfStartDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 7, 1),
    _ConfSelfStartDelayTime_Type()
)
confSelfStartDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confSelfStartDelayTime.setStatus("current")
_ConfRemoteShutdownDelayTime_Type = Integer32
_ConfRemoteShutdownDelayTime_Object = MibScalar
confRemoteShutdownDelayTime = _ConfRemoteShutdownDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 7, 2),
    _ConfRemoteShutdownDelayTime_Type()
)
confRemoteShutdownDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confRemoteShutdownDelayTime.setStatus("current")


class _ConfBatterySelfTestPeriod_Type(Integer32):
    """Custom type confBatterySelfTestPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("by-8-weeks", 1),
          ("by-12-weeks", 2),
          ("by-16-weeks", 3),
          ("by-20-weeks", 4),
          ("by-26-weeks", 5))
    )


_ConfBatterySelfTestPeriod_Type.__name__ = "Integer32"
_ConfBatterySelfTestPeriod_Object = MibScalar
confBatterySelfTestPeriod = _ConfBatterySelfTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 7, 3),
    _ConfBatterySelfTestPeriod_Type()
)
confBatterySelfTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confBatterySelfTestPeriod.setStatus("current")


class _ConfRunMode_Type(Integer32):
    """Custom type confRunMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("eco", 1))
    )


_ConfRunMode_Type.__name__ = "Integer32"
_ConfRunMode_Object = MibScalar
confRunMode = _ConfRunMode_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 7, 4),
    _ConfRunMode_Type()
)
confRunMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confRunMode.setStatus("current")


class _ConfSelfStart_Type(Integer32):
    """Custom type confSelfStart based on Integer32"""
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


_ConfSelfStart_Type.__name__ = "Integer32"
_ConfSelfStart_Object = MibScalar
confSelfStart = _ConfSelfStart_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 7, 5),
    _ConfSelfStart_Type()
)
confSelfStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confSelfStart.setStatus("current")


class _ConfRedundanceSet_Type(Integer32):
    """Custom type confRedundanceSet based on Integer32"""
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


_ConfRedundanceSet_Type.__name__ = "Integer32"
_ConfRedundanceSet_Object = MibScalar
confRedundanceSet = _ConfRedundanceSet_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 7, 6),
    _ConfRedundanceSet_Type()
)
confRedundanceSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confRedundanceSet.setStatus("current")
_ConfRemotePowerOnDelayTime_Type = Integer32
_ConfRemotePowerOnDelayTime_Object = MibScalar
confRemotePowerOnDelayTime = _ConfRemotePowerOnDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 2, 7, 7),
    _ConfRemotePowerOnDelayTime_Type()
)
confRemotePowerOnDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confRemotePowerOnDelayTime.setStatus("current")
_AlarmTrapTable_Object = MibTable
alarmTrapTable = _AlarmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 3)
)
if mibBuilder.loadTexts:
    alarmTrapTable.setStatus("current")
_AlarmTrapEntry_Object = MibTableRow
alarmTrapEntry = _AlarmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 3, 1)
)
alarmTrapEntry.setIndexNames(
    (0, "VERTIV-ITA2-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmTrapEntry.setStatus("current")
_AlarmIndex_Type = Counter32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 3, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmTime_Type = DisplayString
_AlarmTime_Object = MibTableColumn
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 3, 1, 2),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTime.setStatus("current")
_AlarmStatusChange_Type = StatusChange
_AlarmStatusChange_Object = MibTableColumn
alarmStatusChange = _AlarmStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 3, 1, 3),
    _AlarmStatusChange_Type()
)
alarmStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusChange.setStatus("current")
_AlarmSeverity_Type = Status
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 3, 1, 4),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmDescription_Type = DisplayString
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 3, 1, 5),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")
_AlarmId_Type = Integer32
_AlarmId_Object = MibTableColumn
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 13400, 2, 54, 3, 1, 6),
    _AlarmId_Type()
)
alarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTIV-ITA2-MIB",
    **{"Status": Status,
       "StatusChange": StatusChange,
       "Vertiv": Vertiv,
       "products": products,
       "ita2MIB": ita2MIB,
       "ident": ident,
       "identManufacturer": identManufacturer,
       "identModel": identModel,
       "identIndex": identIndex,
       "system": system,
       "status": status,
       "systemStatus": systemStatus,
       "upsOutputSource": upsOutputSource,
       "input": input,
       "inputPhaseVoltageA": inputPhaseVoltageA,
       "inputPhaseVoltageB": inputPhaseVoltageB,
       "inputPhaseVoltageC": inputPhaseVoltageC,
       "inputFrequency": inputFrequency,
       "inputPhaseCurrentA": inputPhaseCurrentA,
       "inputPhaseCurrentB": inputPhaseCurrentB,
       "inputPhaseCurrentC": inputPhaseCurrentC,
       "output": output,
       "outputPhaseVoltageA": outputPhaseVoltageA,
       "outputPhaseVoltageB": outputPhaseVoltageB,
       "outputPhaseVoltageC": outputPhaseVoltageC,
       "outputCurrentA": outputCurrentA,
       "outputCurrentB": outputCurrentB,
       "outputCurrentC": outputCurrentC,
       "outputFrequency": outputFrequency,
       "outputActivePowerA": outputActivePowerA,
       "outputActivePowerB": outputActivePowerB,
       "outputActivePowerC": outputActivePowerC,
       "outputApparentPowerA": outputApparentPowerA,
       "outputApparentPowerB": outputApparentPowerB,
       "outputApparentPowerC": outputApparentPowerC,
       "outputLoadA": outputLoadA,
       "outputLoadB": outputLoadB,
       "outputLoadC": outputLoadC,
       "outputPowerFactorA": outputPowerFactorA,
       "outputPowerFactorB": outputPowerFactorB,
       "outputPowerFactorC": outputPowerFactorC,
       "bypass": bypass,
       "bypassVoltageA": bypassVoltageA,
       "bypassVoltageB": bypassVoltageB,
       "bypassVoltageC": bypassVoltageC,
       "bypassFrequency": bypassFrequency,
       "battery": battery,
       "positiveBatteryVoltage": positiveBatteryVoltage,
       "negativeBatteryVoltage": negativeBatteryVoltage,
       "positiveBatteryChargingCurrent": positiveBatteryChargingCurrent,
       "positiveBatteryDischargingCurrent": positiveBatteryDischargingCurrent,
       "negativeBatteryChargingCurrent": negativeBatteryChargingCurrent,
       "negativeBatteryDischargingCurrent": negativeBatteryDischargingCurrent,
       "batteryRemainsTime": batteryRemainsTime,
       "batteryTemperature": batteryTemperature,
       "batteryEnvironmentTemperature": batteryEnvironmentTemperature,
       "batteryCapacity": batteryCapacity,
       "batteryDischargeTimes": batteryDischargeTimes,
       "control": control,
       "ctrlBatteryTestStart": ctrlBatteryTestStart,
       "ctrlBatteryTestEnd": ctrlBatteryTestEnd,
       "ctrlTurnOn": ctrlTurnOn,
       "ctrlTurnOff": ctrlTurnOff,
       "ctrlTurnOffOutput": ctrlTurnOffOutput,
       "ctrlTurnOnDelay": ctrlTurnOnDelay,
       "ctrlTurnOffOutputDelayStart": ctrlTurnOffOutputDelayStart,
       "ctrlTurnOffOutputDelayEnd": ctrlTurnOffOutputDelayEnd,
       "ctrlBatteryMaintenanceTestStart": ctrlBatteryMaintenanceTestStart,
       "ctrlBatteryMaintenanceTestEnd": ctrlBatteryMaintenanceTestEnd,
       "config": config,
       "confSelfStartDelayTime": confSelfStartDelayTime,
       "confRemoteShutdownDelayTime": confRemoteShutdownDelayTime,
       "confBatterySelfTestPeriod": confBatterySelfTestPeriod,
       "confRunMode": confRunMode,
       "confSelfStart": confSelfStart,
       "confRedundanceSet": confRedundanceSet,
       "confRemotePowerOnDelayTime": confRemotePowerOnDelayTime,
       "alarmTrapTable": alarmTrapTable,
       "alarmTrapEntry": alarmTrapEntry,
       "alarmIndex": alarmIndex,
       "alarmTime": alarmTime,
       "alarmStatusChange": alarmStatusChange,
       "alarmSeverity": alarmSeverity,
       "alarmDescription": alarmDescription,
       "alarmId": alarmId}
)
