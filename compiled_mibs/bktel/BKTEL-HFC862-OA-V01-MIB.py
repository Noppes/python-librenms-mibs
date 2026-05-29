# SNMP MIB module (BKTEL-HFC862-OA-V01-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bktel\BKTEL-HFC862-OA-V01-MIB

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

(DisplayString,
 ModuleWidthValue,
 NESlotValue,
 PerceivedSeverityValue,
 TruthValue,
 modules) = mibBuilder.importSymbols(
    "BKTEL-HFC862-BASE-MIB",
    "DisplayString",
    "ModuleWidthValue",
    "NESlotValue",
    "PerceivedSeverityValue",
    "TruthValue",
    "modules")

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


# Types definitions



class RegulationMode(Integer32):
    """Custom type RegulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regModeConstantOutputPower", 1),
          ("regModeConstantGain", 2))
    )





class SbsEvaluationMode(Integer32):
    """Custom type SbsEvaluationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("evalModeDefault", 1),
          ("evalModeFullScan", 2))
    )





class SbsEvaluationState(Integer32):
    """Custom type SbsEvaluationState based on Integer32"""
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
        *(("evaluationNotSupported", 1),
          ("evaluationDone", 2),
          ("evaluationInProgress", 3),
          ("evaluationFailed", 4))
    )





class ExtIOmode(Integer32):
    """Custom type ExtIOmode based on Integer32"""
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
        *(("modeActiveLowOutput", 1),
          ("modeActiveHighOutput", 2),
          ("modeRedundantMasterIrreversible", 3),
          ("modeRedundantMasterFallback", 4),
          ("modeRedundantSlave", 5))
    )





class ExtIOmask(Integer32):
    """Custom type ExtIOmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("maskAlarmsOnly", 1),
          ("maskAlarmsAndWarnings", 2),
          ("maskSpecial", 3))
    )





class LaserFeatures(Integer32):
    """Custom type LaserFeatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              7,
              9,
              11,
              13,
              15,
              17,
              19,
              21,
              23,
              25,
              27,
              29,
              31)
        )
    )
    namedValues = NamedValues(
        *(("lasNonExistent", 0),
          ("lasCurrent", 1),
          ("lasCurrentLasTec", 3),
          ("lasCurrentLasTemperature", 5),
          ("lasCurrentLasTecLasTemperature", 7),
          ("lasCurrentLasVoltage", 9),
          ("lasCurrentLasTecLasVoltage", 11),
          ("lasCurrentLasTemperatureLasVoltage", 13),
          ("lasCurrentLasTecLasTemperatureLasVoltage", 15),
          ("lasCurrentLasPumpPower", 17),
          ("lasCurrentLasTecLasPumpPower", 19),
          ("lasCurrentLasTemperatureLasPumpPower", 21),
          ("lasCurrentLasTecLasTemperatureLasPumpPower", 23),
          ("lasCurrentLasVoltageLasPumpPower", 25),
          ("lasCurrentLasTecLasVoltageLasPumpPower", 27),
          ("lasCurrentLasTemperatureLasVoltageLasPumpPower", 29),
          ("lasCurrentLasTecLasTemperatureLasVoltageLasPumpPower", 31))
    )





class NESlotWriteValue(Integer32):
    """Custom type NESlotWriteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oa_ObjectIdentity = ObjectIdentity
oa = _Oa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116)
)
_OaCommon_ObjectIdentity = ObjectIdentity
oaCommon = _OaCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 1)
)


class _OaCommonNumberOfModules_Type(Integer32):
    """Custom type oaCommonNumberOfModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_OaCommonNumberOfModules_Type.__name__ = "Integer32"
_OaCommonNumberOfModules_Object = MibScalar
oaCommonNumberOfModules = _OaCommonNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 1, 1),
    _OaCommonNumberOfModules_Type()
)
oaCommonNumberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaCommonNumberOfModules.setStatus("mandatory")
_OaCommonTable_Object = MibTable
oaCommonTable = _OaCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 1, 2)
)
if mibBuilder.loadTexts:
    oaCommonTable.setStatus("mandatory")
_OaCommonEntry_Object = MibTableRow
oaCommonEntry = _OaCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 1, 2, 1)
)
oaCommonEntry.setIndexNames(
    (0, "BKTEL-HFC862-OA-V01-MIB", "oaNESlot"),
)
if mibBuilder.loadTexts:
    oaCommonEntry.setStatus("mandatory")
_OaNESlot_Type = NESlotValue
_OaNESlot_Object = MibTableColumn
oaNESlot = _OaNESlot_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 1, 2, 1, 1),
    _OaNESlot_Type()
)
oaNESlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaNESlot.setStatus("mandatory")


class _OaCommonType_Type(DisplayString):
    """Custom type oaCommonType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OaCommonType_Type.__name__ = "DisplayString"
_OaCommonType_Object = MibTableColumn
oaCommonType = _OaCommonType_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 1, 2, 1, 2),
    _OaCommonType_Type()
)
oaCommonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaCommonType.setStatus("mandatory")
_OaCommonDescr_Type = DisplayString
_OaCommonDescr_Object = MibTableColumn
oaCommonDescr = _OaCommonDescr_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 1, 2, 1, 3),
    _OaCommonDescr_Type()
)
oaCommonDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaCommonDescr.setStatus("mandatory")


class _OaCommonFirmwareId_Type(DisplayString):
    """Custom type oaCommonFirmwareId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OaCommonFirmwareId_Type.__name__ = "DisplayString"
_OaCommonFirmwareId_Object = MibTableColumn
oaCommonFirmwareId = _OaCommonFirmwareId_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 1, 2, 1, 4),
    _OaCommonFirmwareId_Type()
)
oaCommonFirmwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaCommonFirmwareId.setStatus("mandatory")
_OaCommonModuleWidth_Type = ModuleWidthValue
_OaCommonModuleWidth_Object = MibTableColumn
oaCommonModuleWidth = _OaCommonModuleWidth_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 1, 2, 1, 5),
    _OaCommonModuleWidth_Type()
)
oaCommonModuleWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaCommonModuleWidth.setStatus("optional")
_OaStates_ObjectIdentity = ObjectIdentity
oaStates = _OaStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2)
)
_OaStatesTable_Object = MibTable
oaStatesTable = _OaStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1)
)
if mibBuilder.loadTexts:
    oaStatesTable.setStatus("mandatory")
_OaStatesEntry_Object = MibTableRow
oaStatesEntry = _OaStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1)
)
oaStatesEntry.setIndexNames(
    (0, "BKTEL-HFC862-OA-V01-MIB", "oaNESlot"),
)
if mibBuilder.loadTexts:
    oaStatesEntry.setStatus("mandatory")
_OaStatesBootloader_Type = PerceivedSeverityValue
_OaStatesBootloader_Object = MibTableColumn
oaStatesBootloader = _OaStatesBootloader_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 1),
    _OaStatesBootloader_Type()
)
oaStatesBootloader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesBootloader.setStatus("mandatory")
_OaStatesCommLoss_Type = PerceivedSeverityValue
_OaStatesCommLoss_Object = MibTableColumn
oaStatesCommLoss = _OaStatesCommLoss_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 2),
    _OaStatesCommLoss_Type()
)
oaStatesCommLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesCommLoss.setStatus("mandatory")
_OaStatesInitializing_Type = PerceivedSeverityValue
_OaStatesInitializing_Object = MibTableColumn
oaStatesInitializing = _OaStatesInitializing_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 3),
    _OaStatesInitializing_Type()
)
oaStatesInitializing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesInitializing.setStatus("mandatory")
_OaStatesLaserShutdown_Type = PerceivedSeverityValue
_OaStatesLaserShutdown_Object = MibTableColumn
oaStatesLaserShutdown = _OaStatesLaserShutdown_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 4),
    _OaStatesLaserShutdown_Type()
)
oaStatesLaserShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesLaserShutdown.setStatus("mandatory")
_OaStatesTemperatureLow_Type = PerceivedSeverityValue
_OaStatesTemperatureLow_Object = MibTableColumn
oaStatesTemperatureLow = _OaStatesTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 5),
    _OaStatesTemperatureLow_Type()
)
oaStatesTemperatureLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesTemperatureLow.setStatus("mandatory")
_OaStatesTemperatureHigh_Type = PerceivedSeverityValue
_OaStatesTemperatureHigh_Object = MibTableColumn
oaStatesTemperatureHigh = _OaStatesTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 6),
    _OaStatesTemperatureHigh_Type()
)
oaStatesTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesTemperatureHigh.setStatus("mandatory")
_OaStatesSystem_Type = PerceivedSeverityValue
_OaStatesSystem_Object = MibTableColumn
oaStatesSystem = _OaStatesSystem_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 7),
    _OaStatesSystem_Type()
)
oaStatesSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesSystem.setStatus("mandatory")
_OaStatesInputPwrLow_Type = PerceivedSeverityValue
_OaStatesInputPwrLow_Object = MibTableColumn
oaStatesInputPwrLow = _OaStatesInputPwrLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 8),
    _OaStatesInputPwrLow_Type()
)
oaStatesInputPwrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesInputPwrLow.setStatus("mandatory")
_OaStatesInputPwrHigh_Type = PerceivedSeverityValue
_OaStatesInputPwrHigh_Object = MibTableColumn
oaStatesInputPwrHigh = _OaStatesInputPwrHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 9),
    _OaStatesInputPwrHigh_Type()
)
oaStatesInputPwrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesInputPwrHigh.setStatus("mandatory")
_OaStatesOutputPwrOrGainLow_Type = PerceivedSeverityValue
_OaStatesOutputPwrOrGainLow_Object = MibTableColumn
oaStatesOutputPwrOrGainLow = _OaStatesOutputPwrOrGainLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 10),
    _OaStatesOutputPwrOrGainLow_Type()
)
oaStatesOutputPwrOrGainLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesOutputPwrOrGainLow.setStatus("mandatory")
_OaStatesOutputPwrOrGainHigh_Type = PerceivedSeverityValue
_OaStatesOutputPwrOrGainHigh_Object = MibTableColumn
oaStatesOutputPwrOrGainHigh = _OaStatesOutputPwrOrGainHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 11),
    _OaStatesOutputPwrOrGainHigh_Type()
)
oaStatesOutputPwrOrGainHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesOutputPwrOrGainHigh.setStatus("mandatory")
_OaStatesReturnLossLow_Type = PerceivedSeverityValue
_OaStatesReturnLossLow_Object = MibTableColumn
oaStatesReturnLossLow = _OaStatesReturnLossLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 12),
    _OaStatesReturnLossLow_Type()
)
oaStatesReturnLossLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesReturnLossLow.setStatus("mandatory")
_OaStatesReturnLossHigh_Type = PerceivedSeverityValue
_OaStatesReturnLossHigh_Object = MibTableColumn
oaStatesReturnLossHigh = _OaStatesReturnLossHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 13),
    _OaStatesReturnLossHigh_Type()
)
oaStatesReturnLossHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesReturnLossHigh.setStatus("mandatory")
_OaStatesRedundancySwitch_Type = PerceivedSeverityValue
_OaStatesRedundancySwitch_Object = MibTableColumn
oaStatesRedundancySwitch = _OaStatesRedundancySwitch_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 14),
    _OaStatesRedundancySwitch_Type()
)
oaStatesRedundancySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesRedundancySwitch.setStatus("mandatory")
_OaStatesInputVoltageLow_Type = PerceivedSeverityValue
_OaStatesInputVoltageLow_Object = MibTableColumn
oaStatesInputVoltageLow = _OaStatesInputVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 15),
    _OaStatesInputVoltageLow_Type()
)
oaStatesInputVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesInputVoltageLow.setStatus("mandatory")
_OaStatesInputVoltageHigh_Type = PerceivedSeverityValue
_OaStatesInputVoltageHigh_Object = MibTableColumn
oaStatesInputVoltageHigh = _OaStatesInputVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 16),
    _OaStatesInputVoltageHigh_Type()
)
oaStatesInputVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesInputVoltageHigh.setStatus("mandatory")
_OaStatesPowerSupplyLeft_Type = PerceivedSeverityValue
_OaStatesPowerSupplyLeft_Object = MibTableColumn
oaStatesPowerSupplyLeft = _OaStatesPowerSupplyLeft_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 25),
    _OaStatesPowerSupplyLeft_Type()
)
oaStatesPowerSupplyLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesPowerSupplyLeft.setStatus("mandatory")
_OaStatesPowerSupplyRight_Type = PerceivedSeverityValue
_OaStatesPowerSupplyRight_Object = MibTableColumn
oaStatesPowerSupplyRight = _OaStatesPowerSupplyRight_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 26),
    _OaStatesPowerSupplyRight_Type()
)
oaStatesPowerSupplyRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesPowerSupplyRight.setStatus("mandatory")
_OaStatesFanLeft_Type = PerceivedSeverityValue
_OaStatesFanLeft_Object = MibTableColumn
oaStatesFanLeft = _OaStatesFanLeft_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 27),
    _OaStatesFanLeft_Type()
)
oaStatesFanLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesFanLeft.setStatus("mandatory")
_OaStatesFanRight_Type = PerceivedSeverityValue
_OaStatesFanRight_Object = MibTableColumn
oaStatesFanRight = _OaStatesFanRight_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 28),
    _OaStatesFanRight_Type()
)
oaStatesFanRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesFanRight.setStatus("mandatory")
_OaStatesInternalVoltageLow_Type = PerceivedSeverityValue
_OaStatesInternalVoltageLow_Object = MibTableColumn
oaStatesInternalVoltageLow = _OaStatesInternalVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 29),
    _OaStatesInternalVoltageLow_Type()
)
oaStatesInternalVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesInternalVoltageLow.setStatus("mandatory")
_OaStatesInternalVoltageHigh_Type = PerceivedSeverityValue
_OaStatesInternalVoltageHigh_Object = MibTableColumn
oaStatesInternalVoltageHigh = _OaStatesInternalVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 30),
    _OaStatesInternalVoltageHigh_Type()
)
oaStatesInternalVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesInternalVoltageHigh.setStatus("mandatory")
_OaStatesLaserCurrentLow_Type = PerceivedSeverityValue
_OaStatesLaserCurrentLow_Object = MibTableColumn
oaStatesLaserCurrentLow = _OaStatesLaserCurrentLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 31),
    _OaStatesLaserCurrentLow_Type()
)
oaStatesLaserCurrentLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesLaserCurrentLow.setStatus("mandatory")
_OaStatesLaserCurrentHigh_Type = PerceivedSeverityValue
_OaStatesLaserCurrentHigh_Object = MibTableColumn
oaStatesLaserCurrentHigh = _OaStatesLaserCurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 32),
    _OaStatesLaserCurrentHigh_Type()
)
oaStatesLaserCurrentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesLaserCurrentHigh.setStatus("mandatory")
_OaStatesTecCurrentLow_Type = PerceivedSeverityValue
_OaStatesTecCurrentLow_Object = MibTableColumn
oaStatesTecCurrentLow = _OaStatesTecCurrentLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 33),
    _OaStatesTecCurrentLow_Type()
)
oaStatesTecCurrentLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesTecCurrentLow.setStatus("mandatory")
_OaStatesTecCurrentHigh_Type = PerceivedSeverityValue
_OaStatesTecCurrentHigh_Object = MibTableColumn
oaStatesTecCurrentHigh = _OaStatesTecCurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 34),
    _OaStatesTecCurrentHigh_Type()
)
oaStatesTecCurrentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesTecCurrentHigh.setStatus("mandatory")
_OaStatesLaserTempLow_Type = PerceivedSeverityValue
_OaStatesLaserTempLow_Object = MibTableColumn
oaStatesLaserTempLow = _OaStatesLaserTempLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 35),
    _OaStatesLaserTempLow_Type()
)
oaStatesLaserTempLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesLaserTempLow.setStatus("mandatory")
_OaStatesLaserTempHigh_Type = PerceivedSeverityValue
_OaStatesLaserTempHigh_Object = MibTableColumn
oaStatesLaserTempHigh = _OaStatesLaserTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 36),
    _OaStatesLaserTempHigh_Type()
)
oaStatesLaserTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesLaserTempHigh.setStatus("mandatory")
_OaStatesLaserVoltageLow_Type = PerceivedSeverityValue
_OaStatesLaserVoltageLow_Object = MibTableColumn
oaStatesLaserVoltageLow = _OaStatesLaserVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 37),
    _OaStatesLaserVoltageLow_Type()
)
oaStatesLaserVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesLaserVoltageLow.setStatus("mandatory")
_OaStatesLaserVoltageHigh_Type = PerceivedSeverityValue
_OaStatesLaserVoltageHigh_Object = MibTableColumn
oaStatesLaserVoltageHigh = _OaStatesLaserVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 38),
    _OaStatesLaserVoltageHigh_Type()
)
oaStatesLaserVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesLaserVoltageHigh.setStatus("mandatory")
_OaStatesRamanBackReflectionRatio_Type = PerceivedSeverityValue
_OaStatesRamanBackReflectionRatio_Object = MibTableColumn
oaStatesRamanBackReflectionRatio = _OaStatesRamanBackReflectionRatio_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 39),
    _OaStatesRamanBackReflectionRatio_Type()
)
oaStatesRamanBackReflectionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesRamanBackReflectionRatio.setStatus("mandatory")
_OaStatesRamanOscSignalMissing_Type = PerceivedSeverityValue
_OaStatesRamanOscSignalMissing_Object = MibTableColumn
oaStatesRamanOscSignalMissing = _OaStatesRamanOscSignalMissing_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 2, 1, 1, 40),
    _OaStatesRamanOscSignalMissing_Type()
)
oaStatesRamanOscSignalMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaStatesRamanOscSignalMissing.setStatus("mandatory")
_OaConfiguration_ObjectIdentity = ObjectIdentity
oaConfiguration = _OaConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 3)
)
_OaConfigurationTable_Object = MibTable
oaConfigurationTable = _OaConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 3, 1)
)
if mibBuilder.loadTexts:
    oaConfigurationTable.setStatus("mandatory")
_OaConfigurationEntry_Object = MibTableRow
oaConfigurationEntry = _OaConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 3, 1, 1)
)
oaConfigurationEntry.setIndexNames(
    (0, "BKTEL-HFC862-OA-V01-MIB", "oaNESlot"),
)
if mibBuilder.loadTexts:
    oaConfigurationEntry.setStatus("mandatory")
_OaConfigNESlotWrite_Type = NESlotWriteValue
_OaConfigNESlotWrite_Object = MibTableColumn
oaConfigNESlotWrite = _OaConfigNESlotWrite_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 3, 1, 1, 1),
    _OaConfigNESlotWrite_Type()
)
oaConfigNESlotWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaConfigNESlotWrite.setStatus("optional")
_OaConfigRegulationMode_Type = RegulationMode
_OaConfigRegulationMode_Object = MibTableColumn
oaConfigRegulationMode = _OaConfigRegulationMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 3, 1, 1, 2),
    _OaConfigRegulationMode_Type()
)
oaConfigRegulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaConfigRegulationMode.setStatus("mandatory")
_OaConfigOutputPwrOrGainAdjust_Type = Integer32
_OaConfigOutputPwrOrGainAdjust_Object = MibTableColumn
oaConfigOutputPwrOrGainAdjust = _OaConfigOutputPwrOrGainAdjust_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 3, 1, 1, 3),
    _OaConfigOutputPwrOrGainAdjust_Type()
)
oaConfigOutputPwrOrGainAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaConfigOutputPwrOrGainAdjust.setStatus("mandatory")
_OaConfigModeExtIO_Type = ExtIOmode
_OaConfigModeExtIO_Object = MibTableColumn
oaConfigModeExtIO = _OaConfigModeExtIO_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 3, 1, 1, 4),
    _OaConfigModeExtIO_Type()
)
oaConfigModeExtIO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaConfigModeExtIO.setStatus("mandatory")
_OaConfigMaskExtIO_Type = ExtIOmask
_OaConfigMaskExtIO_Object = MibTableColumn
oaConfigMaskExtIO = _OaConfigMaskExtIO_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 3, 1, 1, 5),
    _OaConfigMaskExtIO_Type()
)
oaConfigMaskExtIO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaConfigMaskExtIO.setStatus("mandatory")
_OaConfigSbsEvaluationMode_Type = SbsEvaluationMode
_OaConfigSbsEvaluationMode_Object = MibTableColumn
oaConfigSbsEvaluationMode = _OaConfigSbsEvaluationMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 3, 1, 1, 6),
    _OaConfigSbsEvaluationMode_Type()
)
oaConfigSbsEvaluationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaConfigSbsEvaluationMode.setStatus("mandatory")
_OaControl_ObjectIdentity = ObjectIdentity
oaControl = _OaControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 4)
)
_OaControlTable_Object = MibTable
oaControlTable = _OaControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 4, 1)
)
if mibBuilder.loadTexts:
    oaControlTable.setStatus("mandatory")
_OaControlEntry_Object = MibTableRow
oaControlEntry = _OaControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 4, 1, 1)
)
oaControlEntry.setIndexNames(
    (0, "BKTEL-HFC862-OA-V01-MIB", "oaNESlot"),
)
if mibBuilder.loadTexts:
    oaControlEntry.setStatus("mandatory")
_OaControlLaserShutdown_Type = TruthValue
_OaControlLaserShutdown_Object = MibTableColumn
oaControlLaserShutdown = _OaControlLaserShutdown_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 4, 1, 1, 1),
    _OaControlLaserShutdown_Type()
)
oaControlLaserShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaControlLaserShutdown.setStatus("mandatory")
_OaControlReset_Type = TruthValue
_OaControlReset_Object = MibTableColumn
oaControlReset = _OaControlReset_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 4, 1, 1, 2),
    _OaControlReset_Type()
)
oaControlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaControlReset.setStatus("mandatory")
_OaControlModuleLedBlink_Type = TruthValue
_OaControlModuleLedBlink_Object = MibTableColumn
oaControlModuleLedBlink = _OaControlModuleLedBlink_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 4, 1, 1, 3),
    _OaControlModuleLedBlink_Type()
)
oaControlModuleLedBlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaControlModuleLedBlink.setStatus("mandatory")
_OaControlSbsEvaluationStart_Type = TruthValue
_OaControlSbsEvaluationStart_Object = MibTableColumn
oaControlSbsEvaluationStart = _OaControlSbsEvaluationStart_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 4, 1, 1, 4),
    _OaControlSbsEvaluationStart_Type()
)
oaControlSbsEvaluationStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaControlSbsEvaluationStart.setStatus("mandatory")
_OaMeasuringValues_ObjectIdentity = ObjectIdentity
oaMeasuringValues = _OaMeasuringValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5)
)
_OaMeasuringValuesTable_Object = MibTable
oaMeasuringValuesTable = _OaMeasuringValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1)
)
if mibBuilder.loadTexts:
    oaMeasuringValuesTable.setStatus("mandatory")
_OaMeasuringValuesEntry_Object = MibTableRow
oaMeasuringValuesEntry = _OaMeasuringValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1)
)
oaMeasuringValuesEntry.setIndexNames(
    (0, "BKTEL-HFC862-OA-V01-MIB", "oaNESlot"),
)
if mibBuilder.loadTexts:
    oaMeasuringValuesEntry.setStatus("mandatory")
_OaTemperatureLoLo_Type = Integer32
_OaTemperatureLoLo_Object = MibTableColumn
oaTemperatureLoLo = _OaTemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 1),
    _OaTemperatureLoLo_Type()
)
oaTemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaTemperatureLoLo.setStatus("mandatory")
_OaTemperatureLo_Type = Integer32
_OaTemperatureLo_Object = MibTableColumn
oaTemperatureLo = _OaTemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 2),
    _OaTemperatureLo_Type()
)
oaTemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaTemperatureLo.setStatus("mandatory")
_OaTemperatureValue_Type = Integer32
_OaTemperatureValue_Object = MibTableColumn
oaTemperatureValue = _OaTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 3),
    _OaTemperatureValue_Type()
)
oaTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaTemperatureValue.setStatus("mandatory")
_OaTemperatureHi_Type = Integer32
_OaTemperatureHi_Object = MibTableColumn
oaTemperatureHi = _OaTemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 4),
    _OaTemperatureHi_Type()
)
oaTemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaTemperatureHi.setStatus("mandatory")
_OaTemperatureHiHi_Type = Integer32
_OaTemperatureHiHi_Object = MibTableColumn
oaTemperatureHiHi = _OaTemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 5),
    _OaTemperatureHiHi_Type()
)
oaTemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaTemperatureHiHi.setStatus("mandatory")
_OaInputPowerLoLo_Type = Integer32
_OaInputPowerLoLo_Object = MibTableColumn
oaInputPowerLoLo = _OaInputPowerLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 6),
    _OaInputPowerLoLo_Type()
)
oaInputPowerLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaInputPowerLoLo.setStatus("mandatory")
_OaInputPowerLo_Type = Integer32
_OaInputPowerLo_Object = MibTableColumn
oaInputPowerLo = _OaInputPowerLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 7),
    _OaInputPowerLo_Type()
)
oaInputPowerLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaInputPowerLo.setStatus("mandatory")
_OaInputPowerValue_Type = Integer32
_OaInputPowerValue_Object = MibTableColumn
oaInputPowerValue = _OaInputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 8),
    _OaInputPowerValue_Type()
)
oaInputPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInputPowerValue.setStatus("mandatory")
_OaInputPowerHi_Type = Integer32
_OaInputPowerHi_Object = MibTableColumn
oaInputPowerHi = _OaInputPowerHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 9),
    _OaInputPowerHi_Type()
)
oaInputPowerHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaInputPowerHi.setStatus("mandatory")
_OaInputPowerHiHi_Type = Integer32
_OaInputPowerHiHi_Object = MibTableColumn
oaInputPowerHiHi = _OaInputPowerHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 10),
    _OaInputPowerHiHi_Type()
)
oaInputPowerHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaInputPowerHiHi.setStatus("mandatory")
_OaOutputPwrOrGainLoLo_Type = Integer32
_OaOutputPwrOrGainLoLo_Object = MibTableColumn
oaOutputPwrOrGainLoLo = _OaOutputPwrOrGainLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 11),
    _OaOutputPwrOrGainLoLo_Type()
)
oaOutputPwrOrGainLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaOutputPwrOrGainLoLo.setStatus("mandatory")
_OaOutputPwrOrGainLo_Type = Integer32
_OaOutputPwrOrGainLo_Object = MibTableColumn
oaOutputPwrOrGainLo = _OaOutputPwrOrGainLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 12),
    _OaOutputPwrOrGainLo_Type()
)
oaOutputPwrOrGainLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaOutputPwrOrGainLo.setStatus("mandatory")
_OaOutputPwrOrGainValue_Type = Integer32
_OaOutputPwrOrGainValue_Object = MibTableColumn
oaOutputPwrOrGainValue = _OaOutputPwrOrGainValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 13),
    _OaOutputPwrOrGainValue_Type()
)
oaOutputPwrOrGainValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaOutputPwrOrGainValue.setStatus("mandatory")
_OaOutputPwrOrGainHi_Type = Integer32
_OaOutputPwrOrGainHi_Object = MibTableColumn
oaOutputPwrOrGainHi = _OaOutputPwrOrGainHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 14),
    _OaOutputPwrOrGainHi_Type()
)
oaOutputPwrOrGainHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaOutputPwrOrGainHi.setStatus("mandatory")
_OaOutputPwrOrGainHiHi_Type = Integer32
_OaOutputPwrOrGainHiHi_Object = MibTableColumn
oaOutputPwrOrGainHiHi = _OaOutputPwrOrGainHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 15),
    _OaOutputPwrOrGainHiHi_Type()
)
oaOutputPwrOrGainHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaOutputPwrOrGainHiHi.setStatus("mandatory")
_OaReturnLossLoLo_Type = Integer32
_OaReturnLossLoLo_Object = MibTableColumn
oaReturnLossLoLo = _OaReturnLossLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 16),
    _OaReturnLossLoLo_Type()
)
oaReturnLossLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaReturnLossLoLo.setStatus("mandatory")
_OaReturnLossLo_Type = Integer32
_OaReturnLossLo_Object = MibTableColumn
oaReturnLossLo = _OaReturnLossLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 17),
    _OaReturnLossLo_Type()
)
oaReturnLossLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaReturnLossLo.setStatus("mandatory")
_OaReturnLossValue_Type = Integer32
_OaReturnLossValue_Object = MibTableColumn
oaReturnLossValue = _OaReturnLossValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 18),
    _OaReturnLossValue_Type()
)
oaReturnLossValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaReturnLossValue.setStatus("mandatory")
_OaReturnLossHi_Type = Integer32
_OaReturnLossHi_Object = MibTableColumn
oaReturnLossHi = _OaReturnLossHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 19),
    _OaReturnLossHi_Type()
)
oaReturnLossHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaReturnLossHi.setStatus("mandatory")
_OaReturnLossHiHi_Type = Integer32
_OaReturnLossHiHi_Object = MibTableColumn
oaReturnLossHiHi = _OaReturnLossHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 20),
    _OaReturnLossHiHi_Type()
)
oaReturnLossHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaReturnLossHiHi.setStatus("mandatory")
_OaInputVoltageLoLo_Type = Integer32
_OaInputVoltageLoLo_Object = MibTableColumn
oaInputVoltageLoLo = _OaInputVoltageLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 21),
    _OaInputVoltageLoLo_Type()
)
oaInputVoltageLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInputVoltageLoLo.setStatus("mandatory")
_OaInputVoltageLo_Type = Integer32
_OaInputVoltageLo_Object = MibTableColumn
oaInputVoltageLo = _OaInputVoltageLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 22),
    _OaInputVoltageLo_Type()
)
oaInputVoltageLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInputVoltageLo.setStatus("mandatory")
_OaInputVoltageValue_Type = Integer32
_OaInputVoltageValue_Object = MibTableColumn
oaInputVoltageValue = _OaInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 23),
    _OaInputVoltageValue_Type()
)
oaInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInputVoltageValue.setStatus("mandatory")
_OaInputVoltageHi_Type = Integer32
_OaInputVoltageHi_Object = MibTableColumn
oaInputVoltageHi = _OaInputVoltageHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 24),
    _OaInputVoltageHi_Type()
)
oaInputVoltageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInputVoltageHi.setStatus("mandatory")
_OaInputVoltageHiHi_Type = Integer32
_OaInputVoltageHiHi_Object = MibTableColumn
oaInputVoltageHiHi = _OaInputVoltageHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 25),
    _OaInputVoltageHiHi_Type()
)
oaInputVoltageHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInputVoltageHiHi.setStatus("mandatory")
_OaInternalVoltage1LoLo_Type = Integer32
_OaInternalVoltage1LoLo_Object = MibTableColumn
oaInternalVoltage1LoLo = _OaInternalVoltage1LoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 46),
    _OaInternalVoltage1LoLo_Type()
)
oaInternalVoltage1LoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage1LoLo.setStatus("optional")
_OaInternalVoltage1Lo_Type = Integer32
_OaInternalVoltage1Lo_Object = MibTableColumn
oaInternalVoltage1Lo = _OaInternalVoltage1Lo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 47),
    _OaInternalVoltage1Lo_Type()
)
oaInternalVoltage1Lo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage1Lo.setStatus("optional")
_OaInternalVoltage1Value_Type = Integer32
_OaInternalVoltage1Value_Object = MibTableColumn
oaInternalVoltage1Value = _OaInternalVoltage1Value_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 48),
    _OaInternalVoltage1Value_Type()
)
oaInternalVoltage1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage1Value.setStatus("optional")
_OaInternalVoltage1Hi_Type = Integer32
_OaInternalVoltage1Hi_Object = MibTableColumn
oaInternalVoltage1Hi = _OaInternalVoltage1Hi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 49),
    _OaInternalVoltage1Hi_Type()
)
oaInternalVoltage1Hi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage1Hi.setStatus("optional")
_OaInternalVoltage1HiHi_Type = Integer32
_OaInternalVoltage1HiHi_Object = MibTableColumn
oaInternalVoltage1HiHi = _OaInternalVoltage1HiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 50),
    _OaInternalVoltage1HiHi_Type()
)
oaInternalVoltage1HiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage1HiHi.setStatus("optional")
_OaInternalVoltage2LoLo_Type = Integer32
_OaInternalVoltage2LoLo_Object = MibTableColumn
oaInternalVoltage2LoLo = _OaInternalVoltage2LoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 51),
    _OaInternalVoltage2LoLo_Type()
)
oaInternalVoltage2LoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage2LoLo.setStatus("optional")
_OaInternalVoltage2Lo_Type = Integer32
_OaInternalVoltage2Lo_Object = MibTableColumn
oaInternalVoltage2Lo = _OaInternalVoltage2Lo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 52),
    _OaInternalVoltage2Lo_Type()
)
oaInternalVoltage2Lo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage2Lo.setStatus("optional")
_OaInternalVoltage2Value_Type = Integer32
_OaInternalVoltage2Value_Object = MibTableColumn
oaInternalVoltage2Value = _OaInternalVoltage2Value_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 53),
    _OaInternalVoltage2Value_Type()
)
oaInternalVoltage2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage2Value.setStatus("optional")
_OaInternalVoltage2Hi_Type = Integer32
_OaInternalVoltage2Hi_Object = MibTableColumn
oaInternalVoltage2Hi = _OaInternalVoltage2Hi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 54),
    _OaInternalVoltage2Hi_Type()
)
oaInternalVoltage2Hi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage2Hi.setStatus("optional")
_OaInternalVoltage2HiHi_Type = Integer32
_OaInternalVoltage2HiHi_Object = MibTableColumn
oaInternalVoltage2HiHi = _OaInternalVoltage2HiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 55),
    _OaInternalVoltage2HiHi_Type()
)
oaInternalVoltage2HiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage2HiHi.setStatus("optional")
_OaInternalVoltage3LoLo_Type = Integer32
_OaInternalVoltage3LoLo_Object = MibTableColumn
oaInternalVoltage3LoLo = _OaInternalVoltage3LoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 56),
    _OaInternalVoltage3LoLo_Type()
)
oaInternalVoltage3LoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage3LoLo.setStatus("optional")
_OaInternalVoltage3Lo_Type = Integer32
_OaInternalVoltage3Lo_Object = MibTableColumn
oaInternalVoltage3Lo = _OaInternalVoltage3Lo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 57),
    _OaInternalVoltage3Lo_Type()
)
oaInternalVoltage3Lo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage3Lo.setStatus("optional")
_OaInternalVoltage3Value_Type = Integer32
_OaInternalVoltage3Value_Object = MibTableColumn
oaInternalVoltage3Value = _OaInternalVoltage3Value_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 58),
    _OaInternalVoltage3Value_Type()
)
oaInternalVoltage3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage3Value.setStatus("optional")
_OaInternalVoltage3Hi_Type = Integer32
_OaInternalVoltage3Hi_Object = MibTableColumn
oaInternalVoltage3Hi = _OaInternalVoltage3Hi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 59),
    _OaInternalVoltage3Hi_Type()
)
oaInternalVoltage3Hi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage3Hi.setStatus("optional")
_OaInternalVoltage3HiHi_Type = Integer32
_OaInternalVoltage3HiHi_Object = MibTableColumn
oaInternalVoltage3HiHi = _OaInternalVoltage3HiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 60),
    _OaInternalVoltage3HiHi_Type()
)
oaInternalVoltage3HiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInternalVoltage3HiHi.setStatus("optional")
_OaLaser1CurrentRelLoLo_Type = Integer32
_OaLaser1CurrentRelLoLo_Object = MibTableColumn
oaLaser1CurrentRelLoLo = _OaLaser1CurrentRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 86),
    _OaLaser1CurrentRelLoLo_Type()
)
oaLaser1CurrentRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1CurrentRelLoLo.setStatus("mandatory")
_OaLaser1CurrentRelLo_Type = Integer32
_OaLaser1CurrentRelLo_Object = MibTableColumn
oaLaser1CurrentRelLo = _OaLaser1CurrentRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 87),
    _OaLaser1CurrentRelLo_Type()
)
oaLaser1CurrentRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1CurrentRelLo.setStatus("mandatory")
_OaLaser1CurrentRelValue_Type = Integer32
_OaLaser1CurrentRelValue_Object = MibTableColumn
oaLaser1CurrentRelValue = _OaLaser1CurrentRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 88),
    _OaLaser1CurrentRelValue_Type()
)
oaLaser1CurrentRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1CurrentRelValue.setStatus("mandatory")
_OaLaser1CurrentRelHi_Type = Integer32
_OaLaser1CurrentRelHi_Object = MibTableColumn
oaLaser1CurrentRelHi = _OaLaser1CurrentRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 89),
    _OaLaser1CurrentRelHi_Type()
)
oaLaser1CurrentRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1CurrentRelHi.setStatus("mandatory")
_OaLaser1CurrentRelHiHi_Type = Integer32
_OaLaser1CurrentRelHiHi_Object = MibTableColumn
oaLaser1CurrentRelHiHi = _OaLaser1CurrentRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 90),
    _OaLaser1CurrentRelHiHi_Type()
)
oaLaser1CurrentRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1CurrentRelHiHi.setStatus("mandatory")
_OaLaser1TecRelLoLo_Type = Integer32
_OaLaser1TecRelLoLo_Object = MibTableColumn
oaLaser1TecRelLoLo = _OaLaser1TecRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 91),
    _OaLaser1TecRelLoLo_Type()
)
oaLaser1TecRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TecRelLoLo.setStatus("mandatory")
_OaLaser1TecRelLo_Type = Integer32
_OaLaser1TecRelLo_Object = MibTableColumn
oaLaser1TecRelLo = _OaLaser1TecRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 92),
    _OaLaser1TecRelLo_Type()
)
oaLaser1TecRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TecRelLo.setStatus("mandatory")
_OaLaser1TecRelValue_Type = Integer32
_OaLaser1TecRelValue_Object = MibTableColumn
oaLaser1TecRelValue = _OaLaser1TecRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 93),
    _OaLaser1TecRelValue_Type()
)
oaLaser1TecRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TecRelValue.setStatus("mandatory")
_OaLaser1TecRelHi_Type = Integer32
_OaLaser1TecRelHi_Object = MibTableColumn
oaLaser1TecRelHi = _OaLaser1TecRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 94),
    _OaLaser1TecRelHi_Type()
)
oaLaser1TecRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TecRelHi.setStatus("mandatory")
_OaLaser1TecRelHiHi_Type = Integer32
_OaLaser1TecRelHiHi_Object = MibTableColumn
oaLaser1TecRelHiHi = _OaLaser1TecRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 95),
    _OaLaser1TecRelHiHi_Type()
)
oaLaser1TecRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TecRelHiHi.setStatus("mandatory")
_OaLaser1TemperatureLoLo_Type = Integer32
_OaLaser1TemperatureLoLo_Object = MibTableColumn
oaLaser1TemperatureLoLo = _OaLaser1TemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 96),
    _OaLaser1TemperatureLoLo_Type()
)
oaLaser1TemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TemperatureLoLo.setStatus("mandatory")
_OaLaser1TemperatureLo_Type = Integer32
_OaLaser1TemperatureLo_Object = MibTableColumn
oaLaser1TemperatureLo = _OaLaser1TemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 97),
    _OaLaser1TemperatureLo_Type()
)
oaLaser1TemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TemperatureLo.setStatus("mandatory")
_OaLaser1TemperatureValue_Type = Integer32
_OaLaser1TemperatureValue_Object = MibTableColumn
oaLaser1TemperatureValue = _OaLaser1TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 98),
    _OaLaser1TemperatureValue_Type()
)
oaLaser1TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TemperatureValue.setStatus("mandatory")
_OaLaser1TemperatureHi_Type = Integer32
_OaLaser1TemperatureHi_Object = MibTableColumn
oaLaser1TemperatureHi = _OaLaser1TemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 99),
    _OaLaser1TemperatureHi_Type()
)
oaLaser1TemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TemperatureHi.setStatus("mandatory")
_OaLaser1TemperatureHiHi_Type = Integer32
_OaLaser1TemperatureHiHi_Object = MibTableColumn
oaLaser1TemperatureHiHi = _OaLaser1TemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 100),
    _OaLaser1TemperatureHiHi_Type()
)
oaLaser1TemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1TemperatureHiHi.setStatus("mandatory")
_OaLaser1VoltageLoLo_Type = Integer32
_OaLaser1VoltageLoLo_Object = MibTableColumn
oaLaser1VoltageLoLo = _OaLaser1VoltageLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 101),
    _OaLaser1VoltageLoLo_Type()
)
oaLaser1VoltageLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1VoltageLoLo.setStatus("optional")
_OaLaser1VoltageLo_Type = Integer32
_OaLaser1VoltageLo_Object = MibTableColumn
oaLaser1VoltageLo = _OaLaser1VoltageLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 102),
    _OaLaser1VoltageLo_Type()
)
oaLaser1VoltageLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1VoltageLo.setStatus("optional")
_OaLaser1VoltageValue_Type = Integer32
_OaLaser1VoltageValue_Object = MibTableColumn
oaLaser1VoltageValue = _OaLaser1VoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 103),
    _OaLaser1VoltageValue_Type()
)
oaLaser1VoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1VoltageValue.setStatus("optional")
_OaLaser1VoltageHi_Type = Integer32
_OaLaser1VoltageHi_Object = MibTableColumn
oaLaser1VoltageHi = _OaLaser1VoltageHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 104),
    _OaLaser1VoltageHi_Type()
)
oaLaser1VoltageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1VoltageHi.setStatus("optional")
_OaLaser1VoltageHiHi_Type = Integer32
_OaLaser1VoltageHiHi_Object = MibTableColumn
oaLaser1VoltageHiHi = _OaLaser1VoltageHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 105),
    _OaLaser1VoltageHiHi_Type()
)
oaLaser1VoltageHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser1VoltageHiHi.setStatus("optional")
_OaLaser2CurrentRelLoLo_Type = Integer32
_OaLaser2CurrentRelLoLo_Object = MibTableColumn
oaLaser2CurrentRelLoLo = _OaLaser2CurrentRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 111),
    _OaLaser2CurrentRelLoLo_Type()
)
oaLaser2CurrentRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2CurrentRelLoLo.setStatus("mandatory")
_OaLaser2CurrentRelLo_Type = Integer32
_OaLaser2CurrentRelLo_Object = MibTableColumn
oaLaser2CurrentRelLo = _OaLaser2CurrentRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 112),
    _OaLaser2CurrentRelLo_Type()
)
oaLaser2CurrentRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2CurrentRelLo.setStatus("mandatory")
_OaLaser2CurrentRelValue_Type = Integer32
_OaLaser2CurrentRelValue_Object = MibTableColumn
oaLaser2CurrentRelValue = _OaLaser2CurrentRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 113),
    _OaLaser2CurrentRelValue_Type()
)
oaLaser2CurrentRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2CurrentRelValue.setStatus("mandatory")
_OaLaser2CurrentRelHi_Type = Integer32
_OaLaser2CurrentRelHi_Object = MibTableColumn
oaLaser2CurrentRelHi = _OaLaser2CurrentRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 114),
    _OaLaser2CurrentRelHi_Type()
)
oaLaser2CurrentRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2CurrentRelHi.setStatus("mandatory")
_OaLaser2CurrentRelHiHi_Type = Integer32
_OaLaser2CurrentRelHiHi_Object = MibTableColumn
oaLaser2CurrentRelHiHi = _OaLaser2CurrentRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 115),
    _OaLaser2CurrentRelHiHi_Type()
)
oaLaser2CurrentRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2CurrentRelHiHi.setStatus("mandatory")
_OaLaser2TecRelLoLo_Type = Integer32
_OaLaser2TecRelLoLo_Object = MibTableColumn
oaLaser2TecRelLoLo = _OaLaser2TecRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 116),
    _OaLaser2TecRelLoLo_Type()
)
oaLaser2TecRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TecRelLoLo.setStatus("mandatory")
_OaLaser2TecRelLo_Type = Integer32
_OaLaser2TecRelLo_Object = MibTableColumn
oaLaser2TecRelLo = _OaLaser2TecRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 117),
    _OaLaser2TecRelLo_Type()
)
oaLaser2TecRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TecRelLo.setStatus("mandatory")
_OaLaser2TecRelValue_Type = Integer32
_OaLaser2TecRelValue_Object = MibTableColumn
oaLaser2TecRelValue = _OaLaser2TecRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 118),
    _OaLaser2TecRelValue_Type()
)
oaLaser2TecRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TecRelValue.setStatus("mandatory")
_OaLaser2TecRelHi_Type = Integer32
_OaLaser2TecRelHi_Object = MibTableColumn
oaLaser2TecRelHi = _OaLaser2TecRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 119),
    _OaLaser2TecRelHi_Type()
)
oaLaser2TecRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TecRelHi.setStatus("mandatory")
_OaLaser2TecRelHiHi_Type = Integer32
_OaLaser2TecRelHiHi_Object = MibTableColumn
oaLaser2TecRelHiHi = _OaLaser2TecRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 120),
    _OaLaser2TecRelHiHi_Type()
)
oaLaser2TecRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TecRelHiHi.setStatus("mandatory")
_OaLaser2TemperatureLoLo_Type = Integer32
_OaLaser2TemperatureLoLo_Object = MibTableColumn
oaLaser2TemperatureLoLo = _OaLaser2TemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 121),
    _OaLaser2TemperatureLoLo_Type()
)
oaLaser2TemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TemperatureLoLo.setStatus("mandatory")
_OaLaser2TemperatureLo_Type = Integer32
_OaLaser2TemperatureLo_Object = MibTableColumn
oaLaser2TemperatureLo = _OaLaser2TemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 122),
    _OaLaser2TemperatureLo_Type()
)
oaLaser2TemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TemperatureLo.setStatus("mandatory")
_OaLaser2TemperatureValue_Type = Integer32
_OaLaser2TemperatureValue_Object = MibTableColumn
oaLaser2TemperatureValue = _OaLaser2TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 123),
    _OaLaser2TemperatureValue_Type()
)
oaLaser2TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TemperatureValue.setStatus("mandatory")
_OaLaser2TemperatureHi_Type = Integer32
_OaLaser2TemperatureHi_Object = MibTableColumn
oaLaser2TemperatureHi = _OaLaser2TemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 124),
    _OaLaser2TemperatureHi_Type()
)
oaLaser2TemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TemperatureHi.setStatus("mandatory")
_OaLaser2TemperatureHiHi_Type = Integer32
_OaLaser2TemperatureHiHi_Object = MibTableColumn
oaLaser2TemperatureHiHi = _OaLaser2TemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 125),
    _OaLaser2TemperatureHiHi_Type()
)
oaLaser2TemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2TemperatureHiHi.setStatus("mandatory")
_OaLaser2VoltageLoLo_Type = Integer32
_OaLaser2VoltageLoLo_Object = MibTableColumn
oaLaser2VoltageLoLo = _OaLaser2VoltageLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 126),
    _OaLaser2VoltageLoLo_Type()
)
oaLaser2VoltageLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2VoltageLoLo.setStatus("optional")
_OaLaser2VoltageLo_Type = Integer32
_OaLaser2VoltageLo_Object = MibTableColumn
oaLaser2VoltageLo = _OaLaser2VoltageLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 127),
    _OaLaser2VoltageLo_Type()
)
oaLaser2VoltageLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2VoltageLo.setStatus("optional")
_OaLaser2VoltageValue_Type = Integer32
_OaLaser2VoltageValue_Object = MibTableColumn
oaLaser2VoltageValue = _OaLaser2VoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 128),
    _OaLaser2VoltageValue_Type()
)
oaLaser2VoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2VoltageValue.setStatus("optional")
_OaLaser2VoltageHi_Type = Integer32
_OaLaser2VoltageHi_Object = MibTableColumn
oaLaser2VoltageHi = _OaLaser2VoltageHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 129),
    _OaLaser2VoltageHi_Type()
)
oaLaser2VoltageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2VoltageHi.setStatus("optional")
_OaLaser2VoltageHiHi_Type = Integer32
_OaLaser2VoltageHiHi_Object = MibTableColumn
oaLaser2VoltageHiHi = _OaLaser2VoltageHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 130),
    _OaLaser2VoltageHiHi_Type()
)
oaLaser2VoltageHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser2VoltageHiHi.setStatus("optional")
_OaLaser3CurrentRelLoLo_Type = Integer32
_OaLaser3CurrentRelLoLo_Object = MibTableColumn
oaLaser3CurrentRelLoLo = _OaLaser3CurrentRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 136),
    _OaLaser3CurrentRelLoLo_Type()
)
oaLaser3CurrentRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3CurrentRelLoLo.setStatus("mandatory")
_OaLaser3CurrentRelLo_Type = Integer32
_OaLaser3CurrentRelLo_Object = MibTableColumn
oaLaser3CurrentRelLo = _OaLaser3CurrentRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 137),
    _OaLaser3CurrentRelLo_Type()
)
oaLaser3CurrentRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3CurrentRelLo.setStatus("mandatory")
_OaLaser3CurrentRelValue_Type = Integer32
_OaLaser3CurrentRelValue_Object = MibTableColumn
oaLaser3CurrentRelValue = _OaLaser3CurrentRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 138),
    _OaLaser3CurrentRelValue_Type()
)
oaLaser3CurrentRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3CurrentRelValue.setStatus("mandatory")
_OaLaser3CurrentRelHi_Type = Integer32
_OaLaser3CurrentRelHi_Object = MibTableColumn
oaLaser3CurrentRelHi = _OaLaser3CurrentRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 139),
    _OaLaser3CurrentRelHi_Type()
)
oaLaser3CurrentRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3CurrentRelHi.setStatus("mandatory")
_OaLaser3CurrentRelHiHi_Type = Integer32
_OaLaser3CurrentRelHiHi_Object = MibTableColumn
oaLaser3CurrentRelHiHi = _OaLaser3CurrentRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 140),
    _OaLaser3CurrentRelHiHi_Type()
)
oaLaser3CurrentRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3CurrentRelHiHi.setStatus("mandatory")
_OaLaser3TecRelLoLo_Type = Integer32
_OaLaser3TecRelLoLo_Object = MibTableColumn
oaLaser3TecRelLoLo = _OaLaser3TecRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 141),
    _OaLaser3TecRelLoLo_Type()
)
oaLaser3TecRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TecRelLoLo.setStatus("mandatory")
_OaLaser3TecRelLo_Type = Integer32
_OaLaser3TecRelLo_Object = MibTableColumn
oaLaser3TecRelLo = _OaLaser3TecRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 142),
    _OaLaser3TecRelLo_Type()
)
oaLaser3TecRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TecRelLo.setStatus("mandatory")
_OaLaser3TecRelValue_Type = Integer32
_OaLaser3TecRelValue_Object = MibTableColumn
oaLaser3TecRelValue = _OaLaser3TecRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 143),
    _OaLaser3TecRelValue_Type()
)
oaLaser3TecRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TecRelValue.setStatus("mandatory")
_OaLaser3TecRelHi_Type = Integer32
_OaLaser3TecRelHi_Object = MibTableColumn
oaLaser3TecRelHi = _OaLaser3TecRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 144),
    _OaLaser3TecRelHi_Type()
)
oaLaser3TecRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TecRelHi.setStatus("mandatory")
_OaLaser3TecRelHiHi_Type = Integer32
_OaLaser3TecRelHiHi_Object = MibTableColumn
oaLaser3TecRelHiHi = _OaLaser3TecRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 145),
    _OaLaser3TecRelHiHi_Type()
)
oaLaser3TecRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TecRelHiHi.setStatus("mandatory")
_OaLaser3TemperatureLoLo_Type = Integer32
_OaLaser3TemperatureLoLo_Object = MibTableColumn
oaLaser3TemperatureLoLo = _OaLaser3TemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 146),
    _OaLaser3TemperatureLoLo_Type()
)
oaLaser3TemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TemperatureLoLo.setStatus("mandatory")
_OaLaser3TemperatureLo_Type = Integer32
_OaLaser3TemperatureLo_Object = MibTableColumn
oaLaser3TemperatureLo = _OaLaser3TemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 147),
    _OaLaser3TemperatureLo_Type()
)
oaLaser3TemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TemperatureLo.setStatus("mandatory")
_OaLaser3TemperatureValue_Type = Integer32
_OaLaser3TemperatureValue_Object = MibTableColumn
oaLaser3TemperatureValue = _OaLaser3TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 148),
    _OaLaser3TemperatureValue_Type()
)
oaLaser3TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TemperatureValue.setStatus("mandatory")
_OaLaser3TemperatureHi_Type = Integer32
_OaLaser3TemperatureHi_Object = MibTableColumn
oaLaser3TemperatureHi = _OaLaser3TemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 149),
    _OaLaser3TemperatureHi_Type()
)
oaLaser3TemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TemperatureHi.setStatus("mandatory")
_OaLaser3TemperatureHiHi_Type = Integer32
_OaLaser3TemperatureHiHi_Object = MibTableColumn
oaLaser3TemperatureHiHi = _OaLaser3TemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 150),
    _OaLaser3TemperatureHiHi_Type()
)
oaLaser3TemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3TemperatureHiHi.setStatus("mandatory")
_OaLaser3VoltageLoLo_Type = Integer32
_OaLaser3VoltageLoLo_Object = MibTableColumn
oaLaser3VoltageLoLo = _OaLaser3VoltageLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 151),
    _OaLaser3VoltageLoLo_Type()
)
oaLaser3VoltageLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3VoltageLoLo.setStatus("optional")
_OaLaser3VoltageLo_Type = Integer32
_OaLaser3VoltageLo_Object = MibTableColumn
oaLaser3VoltageLo = _OaLaser3VoltageLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 152),
    _OaLaser3VoltageLo_Type()
)
oaLaser3VoltageLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3VoltageLo.setStatus("optional")
_OaLaser3VoltageValue_Type = Integer32
_OaLaser3VoltageValue_Object = MibTableColumn
oaLaser3VoltageValue = _OaLaser3VoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 153),
    _OaLaser3VoltageValue_Type()
)
oaLaser3VoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3VoltageValue.setStatus("optional")
_OaLaser3VoltageHi_Type = Integer32
_OaLaser3VoltageHi_Object = MibTableColumn
oaLaser3VoltageHi = _OaLaser3VoltageHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 154),
    _OaLaser3VoltageHi_Type()
)
oaLaser3VoltageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3VoltageHi.setStatus("optional")
_OaLaser3VoltageHiHi_Type = Integer32
_OaLaser3VoltageHiHi_Object = MibTableColumn
oaLaser3VoltageHiHi = _OaLaser3VoltageHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 155),
    _OaLaser3VoltageHiHi_Type()
)
oaLaser3VoltageHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser3VoltageHiHi.setStatus("optional")
_OaLaser4CurrentRelLoLo_Type = Integer32
_OaLaser4CurrentRelLoLo_Object = MibTableColumn
oaLaser4CurrentRelLoLo = _OaLaser4CurrentRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 161),
    _OaLaser4CurrentRelLoLo_Type()
)
oaLaser4CurrentRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4CurrentRelLoLo.setStatus("mandatory")
_OaLaser4CurrentRelLo_Type = Integer32
_OaLaser4CurrentRelLo_Object = MibTableColumn
oaLaser4CurrentRelLo = _OaLaser4CurrentRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 162),
    _OaLaser4CurrentRelLo_Type()
)
oaLaser4CurrentRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4CurrentRelLo.setStatus("mandatory")
_OaLaser4CurrentRelValue_Type = Integer32
_OaLaser4CurrentRelValue_Object = MibTableColumn
oaLaser4CurrentRelValue = _OaLaser4CurrentRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 163),
    _OaLaser4CurrentRelValue_Type()
)
oaLaser4CurrentRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4CurrentRelValue.setStatus("mandatory")
_OaLaser4CurrentRelHi_Type = Integer32
_OaLaser4CurrentRelHi_Object = MibTableColumn
oaLaser4CurrentRelHi = _OaLaser4CurrentRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 164),
    _OaLaser4CurrentRelHi_Type()
)
oaLaser4CurrentRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4CurrentRelHi.setStatus("mandatory")
_OaLaser4CurrentRelHiHi_Type = Integer32
_OaLaser4CurrentRelHiHi_Object = MibTableColumn
oaLaser4CurrentRelHiHi = _OaLaser4CurrentRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 165),
    _OaLaser4CurrentRelHiHi_Type()
)
oaLaser4CurrentRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4CurrentRelHiHi.setStatus("mandatory")
_OaLaser4TecRelLoLo_Type = Integer32
_OaLaser4TecRelLoLo_Object = MibTableColumn
oaLaser4TecRelLoLo = _OaLaser4TecRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 166),
    _OaLaser4TecRelLoLo_Type()
)
oaLaser4TecRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TecRelLoLo.setStatus("mandatory")
_OaLaser4TecRelLo_Type = Integer32
_OaLaser4TecRelLo_Object = MibTableColumn
oaLaser4TecRelLo = _OaLaser4TecRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 167),
    _OaLaser4TecRelLo_Type()
)
oaLaser4TecRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TecRelLo.setStatus("mandatory")
_OaLaser4TecRelValue_Type = Integer32
_OaLaser4TecRelValue_Object = MibTableColumn
oaLaser4TecRelValue = _OaLaser4TecRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 168),
    _OaLaser4TecRelValue_Type()
)
oaLaser4TecRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TecRelValue.setStatus("mandatory")
_OaLaser4TecRelHi_Type = Integer32
_OaLaser4TecRelHi_Object = MibTableColumn
oaLaser4TecRelHi = _OaLaser4TecRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 169),
    _OaLaser4TecRelHi_Type()
)
oaLaser4TecRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TecRelHi.setStatus("mandatory")
_OaLaser4TecRelHiHi_Type = Integer32
_OaLaser4TecRelHiHi_Object = MibTableColumn
oaLaser4TecRelHiHi = _OaLaser4TecRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 170),
    _OaLaser4TecRelHiHi_Type()
)
oaLaser4TecRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TecRelHiHi.setStatus("mandatory")
_OaLaser4TemperatureLoLo_Type = Integer32
_OaLaser4TemperatureLoLo_Object = MibTableColumn
oaLaser4TemperatureLoLo = _OaLaser4TemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 171),
    _OaLaser4TemperatureLoLo_Type()
)
oaLaser4TemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TemperatureLoLo.setStatus("mandatory")
_OaLaser4TemperatureLo_Type = Integer32
_OaLaser4TemperatureLo_Object = MibTableColumn
oaLaser4TemperatureLo = _OaLaser4TemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 172),
    _OaLaser4TemperatureLo_Type()
)
oaLaser4TemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TemperatureLo.setStatus("mandatory")
_OaLaser4TemperatureValue_Type = Integer32
_OaLaser4TemperatureValue_Object = MibTableColumn
oaLaser4TemperatureValue = _OaLaser4TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 173),
    _OaLaser4TemperatureValue_Type()
)
oaLaser4TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TemperatureValue.setStatus("mandatory")
_OaLaser4TemperatureHi_Type = Integer32
_OaLaser4TemperatureHi_Object = MibTableColumn
oaLaser4TemperatureHi = _OaLaser4TemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 174),
    _OaLaser4TemperatureHi_Type()
)
oaLaser4TemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TemperatureHi.setStatus("mandatory")
_OaLaser4TemperatureHiHi_Type = Integer32
_OaLaser4TemperatureHiHi_Object = MibTableColumn
oaLaser4TemperatureHiHi = _OaLaser4TemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 175),
    _OaLaser4TemperatureHiHi_Type()
)
oaLaser4TemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4TemperatureHiHi.setStatus("mandatory")
_OaLaser4VoltageLoLo_Type = Integer32
_OaLaser4VoltageLoLo_Object = MibTableColumn
oaLaser4VoltageLoLo = _OaLaser4VoltageLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 176),
    _OaLaser4VoltageLoLo_Type()
)
oaLaser4VoltageLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4VoltageLoLo.setStatus("optional")
_OaLaser4VoltageLo_Type = Integer32
_OaLaser4VoltageLo_Object = MibTableColumn
oaLaser4VoltageLo = _OaLaser4VoltageLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 177),
    _OaLaser4VoltageLo_Type()
)
oaLaser4VoltageLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4VoltageLo.setStatus("optional")
_OaLaser4VoltageValue_Type = Integer32
_OaLaser4VoltageValue_Object = MibTableColumn
oaLaser4VoltageValue = _OaLaser4VoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 178),
    _OaLaser4VoltageValue_Type()
)
oaLaser4VoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4VoltageValue.setStatus("optional")
_OaLaser4VoltageHi_Type = Integer32
_OaLaser4VoltageHi_Object = MibTableColumn
oaLaser4VoltageHi = _OaLaser4VoltageHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 179),
    _OaLaser4VoltageHi_Type()
)
oaLaser4VoltageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4VoltageHi.setStatus("optional")
_OaLaser4VoltageHiHi_Type = Integer32
_OaLaser4VoltageHiHi_Object = MibTableColumn
oaLaser4VoltageHiHi = _OaLaser4VoltageHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 180),
    _OaLaser4VoltageHiHi_Type()
)
oaLaser4VoltageHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser4VoltageHiHi.setStatus("optional")
_OaLaser5CurrentRelLoLo_Type = Integer32
_OaLaser5CurrentRelLoLo_Object = MibTableColumn
oaLaser5CurrentRelLoLo = _OaLaser5CurrentRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 186),
    _OaLaser5CurrentRelLoLo_Type()
)
oaLaser5CurrentRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5CurrentRelLoLo.setStatus("mandatory")
_OaLaser5CurrentRelLo_Type = Integer32
_OaLaser5CurrentRelLo_Object = MibTableColumn
oaLaser5CurrentRelLo = _OaLaser5CurrentRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 187),
    _OaLaser5CurrentRelLo_Type()
)
oaLaser5CurrentRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5CurrentRelLo.setStatus("mandatory")
_OaLaser5CurrentRelValue_Type = Integer32
_OaLaser5CurrentRelValue_Object = MibTableColumn
oaLaser5CurrentRelValue = _OaLaser5CurrentRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 188),
    _OaLaser5CurrentRelValue_Type()
)
oaLaser5CurrentRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5CurrentRelValue.setStatus("mandatory")
_OaLaser5CurrentRelHi_Type = Integer32
_OaLaser5CurrentRelHi_Object = MibTableColumn
oaLaser5CurrentRelHi = _OaLaser5CurrentRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 189),
    _OaLaser5CurrentRelHi_Type()
)
oaLaser5CurrentRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5CurrentRelHi.setStatus("mandatory")
_OaLaser5CurrentRelHiHi_Type = Integer32
_OaLaser5CurrentRelHiHi_Object = MibTableColumn
oaLaser5CurrentRelHiHi = _OaLaser5CurrentRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 190),
    _OaLaser5CurrentRelHiHi_Type()
)
oaLaser5CurrentRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5CurrentRelHiHi.setStatus("mandatory")
_OaLaser5TecRelLoLo_Type = Integer32
_OaLaser5TecRelLoLo_Object = MibTableColumn
oaLaser5TecRelLoLo = _OaLaser5TecRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 191),
    _OaLaser5TecRelLoLo_Type()
)
oaLaser5TecRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TecRelLoLo.setStatus("mandatory")
_OaLaser5TecRelLo_Type = Integer32
_OaLaser5TecRelLo_Object = MibTableColumn
oaLaser5TecRelLo = _OaLaser5TecRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 192),
    _OaLaser5TecRelLo_Type()
)
oaLaser5TecRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TecRelLo.setStatus("mandatory")
_OaLaser5TecRelValue_Type = Integer32
_OaLaser5TecRelValue_Object = MibTableColumn
oaLaser5TecRelValue = _OaLaser5TecRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 193),
    _OaLaser5TecRelValue_Type()
)
oaLaser5TecRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TecRelValue.setStatus("mandatory")
_OaLaser5TecRelHi_Type = Integer32
_OaLaser5TecRelHi_Object = MibTableColumn
oaLaser5TecRelHi = _OaLaser5TecRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 194),
    _OaLaser5TecRelHi_Type()
)
oaLaser5TecRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TecRelHi.setStatus("mandatory")
_OaLaser5TecRelHiHi_Type = Integer32
_OaLaser5TecRelHiHi_Object = MibTableColumn
oaLaser5TecRelHiHi = _OaLaser5TecRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 195),
    _OaLaser5TecRelHiHi_Type()
)
oaLaser5TecRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TecRelHiHi.setStatus("mandatory")
_OaLaser5TemperatureLoLo_Type = Integer32
_OaLaser5TemperatureLoLo_Object = MibTableColumn
oaLaser5TemperatureLoLo = _OaLaser5TemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 196),
    _OaLaser5TemperatureLoLo_Type()
)
oaLaser5TemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TemperatureLoLo.setStatus("mandatory")
_OaLaser5TemperatureLo_Type = Integer32
_OaLaser5TemperatureLo_Object = MibTableColumn
oaLaser5TemperatureLo = _OaLaser5TemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 197),
    _OaLaser5TemperatureLo_Type()
)
oaLaser5TemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TemperatureLo.setStatus("mandatory")
_OaLaser5TemperatureValue_Type = Integer32
_OaLaser5TemperatureValue_Object = MibTableColumn
oaLaser5TemperatureValue = _OaLaser5TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 198),
    _OaLaser5TemperatureValue_Type()
)
oaLaser5TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TemperatureValue.setStatus("mandatory")
_OaLaser5TemperatureHi_Type = Integer32
_OaLaser5TemperatureHi_Object = MibTableColumn
oaLaser5TemperatureHi = _OaLaser5TemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 199),
    _OaLaser5TemperatureHi_Type()
)
oaLaser5TemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TemperatureHi.setStatus("mandatory")
_OaLaser5TemperatureHiHi_Type = Integer32
_OaLaser5TemperatureHiHi_Object = MibTableColumn
oaLaser5TemperatureHiHi = _OaLaser5TemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 200),
    _OaLaser5TemperatureHiHi_Type()
)
oaLaser5TemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5TemperatureHiHi.setStatus("mandatory")
_OaLaser5VoltageLoLo_Type = Integer32
_OaLaser5VoltageLoLo_Object = MibTableColumn
oaLaser5VoltageLoLo = _OaLaser5VoltageLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 201),
    _OaLaser5VoltageLoLo_Type()
)
oaLaser5VoltageLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5VoltageLoLo.setStatus("optional")
_OaLaser5VoltageLo_Type = Integer32
_OaLaser5VoltageLo_Object = MibTableColumn
oaLaser5VoltageLo = _OaLaser5VoltageLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 202),
    _OaLaser5VoltageLo_Type()
)
oaLaser5VoltageLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5VoltageLo.setStatus("optional")
_OaLaser5VoltageValue_Type = Integer32
_OaLaser5VoltageValue_Object = MibTableColumn
oaLaser5VoltageValue = _OaLaser5VoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 203),
    _OaLaser5VoltageValue_Type()
)
oaLaser5VoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5VoltageValue.setStatus("optional")
_OaLaser5VoltageHi_Type = Integer32
_OaLaser5VoltageHi_Object = MibTableColumn
oaLaser5VoltageHi = _OaLaser5VoltageHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 204),
    _OaLaser5VoltageHi_Type()
)
oaLaser5VoltageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5VoltageHi.setStatus("optional")
_OaLaser5VoltageHiHi_Type = Integer32
_OaLaser5VoltageHiHi_Object = MibTableColumn
oaLaser5VoltageHiHi = _OaLaser5VoltageHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 205),
    _OaLaser5VoltageHiHi_Type()
)
oaLaser5VoltageHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser5VoltageHiHi.setStatus("optional")
_OaLaser6CurrentRelLoLo_Type = Integer32
_OaLaser6CurrentRelLoLo_Object = MibTableColumn
oaLaser6CurrentRelLoLo = _OaLaser6CurrentRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 211),
    _OaLaser6CurrentRelLoLo_Type()
)
oaLaser6CurrentRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6CurrentRelLoLo.setStatus("mandatory")
_OaLaser6CurrentRelLo_Type = Integer32
_OaLaser6CurrentRelLo_Object = MibTableColumn
oaLaser6CurrentRelLo = _OaLaser6CurrentRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 212),
    _OaLaser6CurrentRelLo_Type()
)
oaLaser6CurrentRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6CurrentRelLo.setStatus("mandatory")
_OaLaser6CurrentRelValue_Type = Integer32
_OaLaser6CurrentRelValue_Object = MibTableColumn
oaLaser6CurrentRelValue = _OaLaser6CurrentRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 213),
    _OaLaser6CurrentRelValue_Type()
)
oaLaser6CurrentRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6CurrentRelValue.setStatus("mandatory")
_OaLaser6CurrentRelHi_Type = Integer32
_OaLaser6CurrentRelHi_Object = MibTableColumn
oaLaser6CurrentRelHi = _OaLaser6CurrentRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 214),
    _OaLaser6CurrentRelHi_Type()
)
oaLaser6CurrentRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6CurrentRelHi.setStatus("mandatory")
_OaLaser6CurrentRelHiHi_Type = Integer32
_OaLaser6CurrentRelHiHi_Object = MibTableColumn
oaLaser6CurrentRelHiHi = _OaLaser6CurrentRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 215),
    _OaLaser6CurrentRelHiHi_Type()
)
oaLaser6CurrentRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6CurrentRelHiHi.setStatus("mandatory")
_OaLaser6TecRelLoLo_Type = Integer32
_OaLaser6TecRelLoLo_Object = MibTableColumn
oaLaser6TecRelLoLo = _OaLaser6TecRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 216),
    _OaLaser6TecRelLoLo_Type()
)
oaLaser6TecRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TecRelLoLo.setStatus("mandatory")
_OaLaser6TecRelLo_Type = Integer32
_OaLaser6TecRelLo_Object = MibTableColumn
oaLaser6TecRelLo = _OaLaser6TecRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 217),
    _OaLaser6TecRelLo_Type()
)
oaLaser6TecRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TecRelLo.setStatus("mandatory")
_OaLaser6TecRelValue_Type = Integer32
_OaLaser6TecRelValue_Object = MibTableColumn
oaLaser6TecRelValue = _OaLaser6TecRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 218),
    _OaLaser6TecRelValue_Type()
)
oaLaser6TecRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TecRelValue.setStatus("mandatory")
_OaLaser6TecRelHi_Type = Integer32
_OaLaser6TecRelHi_Object = MibTableColumn
oaLaser6TecRelHi = _OaLaser6TecRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 219),
    _OaLaser6TecRelHi_Type()
)
oaLaser6TecRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TecRelHi.setStatus("mandatory")
_OaLaser6TecRelHiHi_Type = Integer32
_OaLaser6TecRelHiHi_Object = MibTableColumn
oaLaser6TecRelHiHi = _OaLaser6TecRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 220),
    _OaLaser6TecRelHiHi_Type()
)
oaLaser6TecRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TecRelHiHi.setStatus("mandatory")
_OaLaser6TemperatureLoLo_Type = Integer32
_OaLaser6TemperatureLoLo_Object = MibTableColumn
oaLaser6TemperatureLoLo = _OaLaser6TemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 221),
    _OaLaser6TemperatureLoLo_Type()
)
oaLaser6TemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TemperatureLoLo.setStatus("mandatory")
_OaLaser6TemperatureLo_Type = Integer32
_OaLaser6TemperatureLo_Object = MibTableColumn
oaLaser6TemperatureLo = _OaLaser6TemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 222),
    _OaLaser6TemperatureLo_Type()
)
oaLaser6TemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TemperatureLo.setStatus("mandatory")
_OaLaser6TemperatureValue_Type = Integer32
_OaLaser6TemperatureValue_Object = MibTableColumn
oaLaser6TemperatureValue = _OaLaser6TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 223),
    _OaLaser6TemperatureValue_Type()
)
oaLaser6TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TemperatureValue.setStatus("mandatory")
_OaLaser6TemperatureHi_Type = Integer32
_OaLaser6TemperatureHi_Object = MibTableColumn
oaLaser6TemperatureHi = _OaLaser6TemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 224),
    _OaLaser6TemperatureHi_Type()
)
oaLaser6TemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TemperatureHi.setStatus("mandatory")
_OaLaser6TemperatureHiHi_Type = Integer32
_OaLaser6TemperatureHiHi_Object = MibTableColumn
oaLaser6TemperatureHiHi = _OaLaser6TemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 225),
    _OaLaser6TemperatureHiHi_Type()
)
oaLaser6TemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6TemperatureHiHi.setStatus("mandatory")
_OaLaser6VoltageLoLo_Type = Integer32
_OaLaser6VoltageLoLo_Object = MibTableColumn
oaLaser6VoltageLoLo = _OaLaser6VoltageLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 226),
    _OaLaser6VoltageLoLo_Type()
)
oaLaser6VoltageLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6VoltageLoLo.setStatus("optional")
_OaLaser6VoltageLo_Type = Integer32
_OaLaser6VoltageLo_Object = MibTableColumn
oaLaser6VoltageLo = _OaLaser6VoltageLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 227),
    _OaLaser6VoltageLo_Type()
)
oaLaser6VoltageLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6VoltageLo.setStatus("optional")
_OaLaser6VoltageValue_Type = Integer32
_OaLaser6VoltageValue_Object = MibTableColumn
oaLaser6VoltageValue = _OaLaser6VoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 228),
    _OaLaser6VoltageValue_Type()
)
oaLaser6VoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6VoltageValue.setStatus("optional")
_OaLaser6VoltageHi_Type = Integer32
_OaLaser6VoltageHi_Object = MibTableColumn
oaLaser6VoltageHi = _OaLaser6VoltageHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 229),
    _OaLaser6VoltageHi_Type()
)
oaLaser6VoltageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6VoltageHi.setStatus("optional")
_OaLaser6VoltageHiHi_Type = Integer32
_OaLaser6VoltageHiHi_Object = MibTableColumn
oaLaser6VoltageHiHi = _OaLaser6VoltageHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 5, 1, 1, 230),
    _OaLaser6VoltageHiHi_Type()
)
oaLaser6VoltageHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLaser6VoltageHiHi.setStatus("optional")
_OaDisplay_ObjectIdentity = ObjectIdentity
oaDisplay = _OaDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6)
)
_OaDisplayTable_Object = MibTable
oaDisplayTable = _OaDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1)
)
if mibBuilder.loadTexts:
    oaDisplayTable.setStatus("mandatory")
_OaDisplayEntry_Object = MibTableRow
oaDisplayEntry = _OaDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1)
)
oaDisplayEntry.setIndexNames(
    (0, "BKTEL-HFC862-OA-V01-MIB", "oaNESlot"),
)
if mibBuilder.loadTexts:
    oaDisplayEntry.setStatus("mandatory")
_OaDisplayNumberOfLasers_Type = Integer32
_OaDisplayNumberOfLasers_Object = MibTableColumn
oaDisplayNumberOfLasers = _OaDisplayNumberOfLasers_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 1),
    _OaDisplayNumberOfLasers_Type()
)
oaDisplayNumberOfLasers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayNumberOfLasers.setStatus("mandatory")
_OaDisplayNumberOfInternalVoltages_Type = Integer32
_OaDisplayNumberOfInternalVoltages_Object = MibTableColumn
oaDisplayNumberOfInternalVoltages = _OaDisplayNumberOfInternalVoltages_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 2),
    _OaDisplayNumberOfInternalVoltages_Type()
)
oaDisplayNumberOfInternalVoltages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayNumberOfInternalVoltages.setStatus("optional")
_OaDisplayExtIOSupported_Type = TruthValue
_OaDisplayExtIOSupported_Object = MibTableColumn
oaDisplayExtIOSupported = _OaDisplayExtIOSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 3),
    _OaDisplayExtIOSupported_Type()
)
oaDisplayExtIOSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayExtIOSupported.setStatus("mandatory")
_OaDisplaySbsSupported_Type = TruthValue
_OaDisplaySbsSupported_Object = MibTableColumn
oaDisplaySbsSupported = _OaDisplaySbsSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 4),
    _OaDisplaySbsSupported_Type()
)
oaDisplaySbsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplaySbsSupported.setStatus("mandatory")
_OaDisplayReturnLossSupported_Type = TruthValue
_OaDisplayReturnLossSupported_Object = MibTableColumn
oaDisplayReturnLossSupported = _OaDisplayReturnLossSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 5),
    _OaDisplayReturnLossSupported_Type()
)
oaDisplayReturnLossSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayReturnLossSupported.setStatus("mandatory")
_OaDisplaySbsEvaluatedThreshold_Type = Integer32
_OaDisplaySbsEvaluatedThreshold_Object = MibTableColumn
oaDisplaySbsEvaluatedThreshold = _OaDisplaySbsEvaluatedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 6),
    _OaDisplaySbsEvaluatedThreshold_Type()
)
oaDisplaySbsEvaluatedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplaySbsEvaluatedThreshold.setStatus("mandatory")
_OaDisplaySbsLastEvaluationState_Type = SbsEvaluationState
_OaDisplaySbsLastEvaluationState_Object = MibTableColumn
oaDisplaySbsLastEvaluationState = _OaDisplaySbsLastEvaluationState_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 7),
    _OaDisplaySbsLastEvaluationState_Type()
)
oaDisplaySbsLastEvaluationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplaySbsLastEvaluationState.setStatus("mandatory")
_OaDisplaySbsLastEvaluationTime_Type = DisplayString
_OaDisplaySbsLastEvaluationTime_Object = MibTableColumn
oaDisplaySbsLastEvaluationTime = _OaDisplaySbsLastEvaluationTime_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 8),
    _OaDisplaySbsLastEvaluationTime_Type()
)
oaDisplaySbsLastEvaluationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplaySbsLastEvaluationTime.setStatus("mandatory")
_OaDisplayOutputPwrOrGainNominal_Type = Integer32
_OaDisplayOutputPwrOrGainNominal_Object = MibTableColumn
oaDisplayOutputPwrOrGainNominal = _OaDisplayOutputPwrOrGainNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 9),
    _OaDisplayOutputPwrOrGainNominal_Type()
)
oaDisplayOutputPwrOrGainNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayOutputPwrOrGainNominal.setStatus("mandatory")
_OaDisplayOutputPwrOrGainAdjusted_Type = Integer32
_OaDisplayOutputPwrOrGainAdjusted_Object = MibTableColumn
oaDisplayOutputPwrOrGainAdjusted = _OaDisplayOutputPwrOrGainAdjusted_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 10),
    _OaDisplayOutputPwrOrGainAdjusted_Type()
)
oaDisplayOutputPwrOrGainAdjusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayOutputPwrOrGainAdjusted.setStatus("mandatory")
_OaDisplayInputVoltageNominal_Type = Integer32
_OaDisplayInputVoltageNominal_Object = MibTableColumn
oaDisplayInputVoltageNominal = _OaDisplayInputVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 11),
    _OaDisplayInputVoltageNominal_Type()
)
oaDisplayInputVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayInputVoltageNominal.setStatus("optional")
_OaDisplayInternalVoltage1Nominal_Type = Integer32
_OaDisplayInternalVoltage1Nominal_Object = MibTableColumn
oaDisplayInternalVoltage1Nominal = _OaDisplayInternalVoltage1Nominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 12),
    _OaDisplayInternalVoltage1Nominal_Type()
)
oaDisplayInternalVoltage1Nominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayInternalVoltage1Nominal.setStatus("optional")
_OaDisplayInternalVoltage2Nominal_Type = Integer32
_OaDisplayInternalVoltage2Nominal_Object = MibTableColumn
oaDisplayInternalVoltage2Nominal = _OaDisplayInternalVoltage2Nominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 13),
    _OaDisplayInternalVoltage2Nominal_Type()
)
oaDisplayInternalVoltage2Nominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayInternalVoltage2Nominal.setStatus("optional")
_OaDisplayInternalVoltage3Nominal_Type = Integer32
_OaDisplayInternalVoltage3Nominal_Object = MibTableColumn
oaDisplayInternalVoltage3Nominal = _OaDisplayInternalVoltage3Nominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 14),
    _OaDisplayInternalVoltage3Nominal_Type()
)
oaDisplayInternalVoltage3Nominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayInternalVoltage3Nominal.setStatus("optional")
_OaDisplayLaser1VoltageNominal_Type = Integer32
_OaDisplayLaser1VoltageNominal_Object = MibTableColumn
oaDisplayLaser1VoltageNominal = _OaDisplayLaser1VoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 20),
    _OaDisplayLaser1VoltageNominal_Type()
)
oaDisplayLaser1VoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser1VoltageNominal.setStatus("optional")
_OaDisplayLaser2VoltageNominal_Type = Integer32
_OaDisplayLaser2VoltageNominal_Object = MibTableColumn
oaDisplayLaser2VoltageNominal = _OaDisplayLaser2VoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 21),
    _OaDisplayLaser2VoltageNominal_Type()
)
oaDisplayLaser2VoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser2VoltageNominal.setStatus("optional")
_OaDisplayLaser3VoltageNominal_Type = Integer32
_OaDisplayLaser3VoltageNominal_Object = MibTableColumn
oaDisplayLaser3VoltageNominal = _OaDisplayLaser3VoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 22),
    _OaDisplayLaser3VoltageNominal_Type()
)
oaDisplayLaser3VoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser3VoltageNominal.setStatus("optional")
_OaDisplayLaser4VoltageNominal_Type = Integer32
_OaDisplayLaser4VoltageNominal_Object = MibTableColumn
oaDisplayLaser4VoltageNominal = _OaDisplayLaser4VoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 23),
    _OaDisplayLaser4VoltageNominal_Type()
)
oaDisplayLaser4VoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser4VoltageNominal.setStatus("optional")
_OaDisplayLaser5VoltageNominal_Type = Integer32
_OaDisplayLaser5VoltageNominal_Object = MibTableColumn
oaDisplayLaser5VoltageNominal = _OaDisplayLaser5VoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 24),
    _OaDisplayLaser5VoltageNominal_Type()
)
oaDisplayLaser5VoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser5VoltageNominal.setStatus("optional")
_OaDisplayLaser6VoltageNominal_Type = Integer32
_OaDisplayLaser6VoltageNominal_Object = MibTableColumn
oaDisplayLaser6VoltageNominal = _OaDisplayLaser6VoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 25),
    _OaDisplayLaser6VoltageNominal_Type()
)
oaDisplayLaser6VoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser6VoltageNominal.setStatus("optional")
_OaDisplayLaser1PumpPowerRel_Type = Integer32
_OaDisplayLaser1PumpPowerRel_Object = MibTableColumn
oaDisplayLaser1PumpPowerRel = _OaDisplayLaser1PumpPowerRel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 30),
    _OaDisplayLaser1PumpPowerRel_Type()
)
oaDisplayLaser1PumpPowerRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser1PumpPowerRel.setStatus("mandatory")
_OaDisplayLaser2PumpPowerRel_Type = Integer32
_OaDisplayLaser2PumpPowerRel_Object = MibTableColumn
oaDisplayLaser2PumpPowerRel = _OaDisplayLaser2PumpPowerRel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 31),
    _OaDisplayLaser2PumpPowerRel_Type()
)
oaDisplayLaser2PumpPowerRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser2PumpPowerRel.setStatus("mandatory")
_OaDisplayLaser3PumpPowerRel_Type = Integer32
_OaDisplayLaser3PumpPowerRel_Object = MibTableColumn
oaDisplayLaser3PumpPowerRel = _OaDisplayLaser3PumpPowerRel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 32),
    _OaDisplayLaser3PumpPowerRel_Type()
)
oaDisplayLaser3PumpPowerRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser3PumpPowerRel.setStatus("mandatory")
_OaDisplayLaser4PumpPowerRel_Type = Integer32
_OaDisplayLaser4PumpPowerRel_Object = MibTableColumn
oaDisplayLaser4PumpPowerRel = _OaDisplayLaser4PumpPowerRel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 33),
    _OaDisplayLaser4PumpPowerRel_Type()
)
oaDisplayLaser4PumpPowerRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser4PumpPowerRel.setStatus("mandatory")
_OaDisplayLaser5PumpPowerRel_Type = Integer32
_OaDisplayLaser5PumpPowerRel_Object = MibTableColumn
oaDisplayLaser5PumpPowerRel = _OaDisplayLaser5PumpPowerRel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 34),
    _OaDisplayLaser5PumpPowerRel_Type()
)
oaDisplayLaser5PumpPowerRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser5PumpPowerRel.setStatus("mandatory")
_OaDisplayLaser6PumpPowerRel_Type = Integer32
_OaDisplayLaser6PumpPowerRel_Object = MibTableColumn
oaDisplayLaser6PumpPowerRel = _OaDisplayLaser6PumpPowerRel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 35),
    _OaDisplayLaser6PumpPowerRel_Type()
)
oaDisplayLaser6PumpPowerRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser6PumpPowerRel.setStatus("mandatory")
_OaDisplayLaser1FeaturesSupported_Type = LaserFeatures
_OaDisplayLaser1FeaturesSupported_Object = MibTableColumn
oaDisplayLaser1FeaturesSupported = _OaDisplayLaser1FeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 40),
    _OaDisplayLaser1FeaturesSupported_Type()
)
oaDisplayLaser1FeaturesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser1FeaturesSupported.setStatus("mandatory")
_OaDisplayLaser2FeaturesSupported_Type = LaserFeatures
_OaDisplayLaser2FeaturesSupported_Object = MibTableColumn
oaDisplayLaser2FeaturesSupported = _OaDisplayLaser2FeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 41),
    _OaDisplayLaser2FeaturesSupported_Type()
)
oaDisplayLaser2FeaturesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser2FeaturesSupported.setStatus("mandatory")
_OaDisplayLaser3FeaturesSupported_Type = LaserFeatures
_OaDisplayLaser3FeaturesSupported_Object = MibTableColumn
oaDisplayLaser3FeaturesSupported = _OaDisplayLaser3FeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 42),
    _OaDisplayLaser3FeaturesSupported_Type()
)
oaDisplayLaser3FeaturesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser3FeaturesSupported.setStatus("mandatory")
_OaDisplayLaser4FeaturesSupported_Type = LaserFeatures
_OaDisplayLaser4FeaturesSupported_Object = MibTableColumn
oaDisplayLaser4FeaturesSupported = _OaDisplayLaser4FeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 43),
    _OaDisplayLaser4FeaturesSupported_Type()
)
oaDisplayLaser4FeaturesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser4FeaturesSupported.setStatus("mandatory")
_OaDisplayLaser5FeaturesSupported_Type = LaserFeatures
_OaDisplayLaser5FeaturesSupported_Object = MibTableColumn
oaDisplayLaser5FeaturesSupported = _OaDisplayLaser5FeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 44),
    _OaDisplayLaser5FeaturesSupported_Type()
)
oaDisplayLaser5FeaturesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser5FeaturesSupported.setStatus("mandatory")
_OaDisplayLaser6FeaturesSupported_Type = LaserFeatures
_OaDisplayLaser6FeaturesSupported_Object = MibTableColumn
oaDisplayLaser6FeaturesSupported = _OaDisplayLaser6FeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 45),
    _OaDisplayLaser6FeaturesSupported_Type()
)
oaDisplayLaser6FeaturesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayLaser6FeaturesSupported.setStatus("mandatory")
_OaDisplayAmplifierIsRamanType_Type = TruthValue
_OaDisplayAmplifierIsRamanType_Object = MibTableColumn
oaDisplayAmplifierIsRamanType = _OaDisplayAmplifierIsRamanType_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 116, 6, 1, 1, 50),
    _OaDisplayAmplifierIsRamanType_Type()
)
oaDisplayAmplifierIsRamanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDisplayAmplifierIsRamanType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BKTEL-HFC862-OA-V01-MIB",
    **{"RegulationMode": RegulationMode,
       "SbsEvaluationMode": SbsEvaluationMode,
       "SbsEvaluationState": SbsEvaluationState,
       "ExtIOmode": ExtIOmode,
       "ExtIOmask": ExtIOmask,
       "LaserFeatures": LaserFeatures,
       "NESlotWriteValue": NESlotWriteValue,
       "oa": oa,
       "oaCommon": oaCommon,
       "oaCommonNumberOfModules": oaCommonNumberOfModules,
       "oaCommonTable": oaCommonTable,
       "oaCommonEntry": oaCommonEntry,
       "oaNESlot": oaNESlot,
       "oaCommonType": oaCommonType,
       "oaCommonDescr": oaCommonDescr,
       "oaCommonFirmwareId": oaCommonFirmwareId,
       "oaCommonModuleWidth": oaCommonModuleWidth,
       "oaStates": oaStates,
       "oaStatesTable": oaStatesTable,
       "oaStatesEntry": oaStatesEntry,
       "oaStatesBootloader": oaStatesBootloader,
       "oaStatesCommLoss": oaStatesCommLoss,
       "oaStatesInitializing": oaStatesInitializing,
       "oaStatesLaserShutdown": oaStatesLaserShutdown,
       "oaStatesTemperatureLow": oaStatesTemperatureLow,
       "oaStatesTemperatureHigh": oaStatesTemperatureHigh,
       "oaStatesSystem": oaStatesSystem,
       "oaStatesInputPwrLow": oaStatesInputPwrLow,
       "oaStatesInputPwrHigh": oaStatesInputPwrHigh,
       "oaStatesOutputPwrOrGainLow": oaStatesOutputPwrOrGainLow,
       "oaStatesOutputPwrOrGainHigh": oaStatesOutputPwrOrGainHigh,
       "oaStatesReturnLossLow": oaStatesReturnLossLow,
       "oaStatesReturnLossHigh": oaStatesReturnLossHigh,
       "oaStatesRedundancySwitch": oaStatesRedundancySwitch,
       "oaStatesInputVoltageLow": oaStatesInputVoltageLow,
       "oaStatesInputVoltageHigh": oaStatesInputVoltageHigh,
       "oaStatesPowerSupplyLeft": oaStatesPowerSupplyLeft,
       "oaStatesPowerSupplyRight": oaStatesPowerSupplyRight,
       "oaStatesFanLeft": oaStatesFanLeft,
       "oaStatesFanRight": oaStatesFanRight,
       "oaStatesInternalVoltageLow": oaStatesInternalVoltageLow,
       "oaStatesInternalVoltageHigh": oaStatesInternalVoltageHigh,
       "oaStatesLaserCurrentLow": oaStatesLaserCurrentLow,
       "oaStatesLaserCurrentHigh": oaStatesLaserCurrentHigh,
       "oaStatesTecCurrentLow": oaStatesTecCurrentLow,
       "oaStatesTecCurrentHigh": oaStatesTecCurrentHigh,
       "oaStatesLaserTempLow": oaStatesLaserTempLow,
       "oaStatesLaserTempHigh": oaStatesLaserTempHigh,
       "oaStatesLaserVoltageLow": oaStatesLaserVoltageLow,
       "oaStatesLaserVoltageHigh": oaStatesLaserVoltageHigh,
       "oaStatesRamanBackReflectionRatio": oaStatesRamanBackReflectionRatio,
       "oaStatesRamanOscSignalMissing": oaStatesRamanOscSignalMissing,
       "oaConfiguration": oaConfiguration,
       "oaConfigurationTable": oaConfigurationTable,
       "oaConfigurationEntry": oaConfigurationEntry,
       "oaConfigNESlotWrite": oaConfigNESlotWrite,
       "oaConfigRegulationMode": oaConfigRegulationMode,
       "oaConfigOutputPwrOrGainAdjust": oaConfigOutputPwrOrGainAdjust,
       "oaConfigModeExtIO": oaConfigModeExtIO,
       "oaConfigMaskExtIO": oaConfigMaskExtIO,
       "oaConfigSbsEvaluationMode": oaConfigSbsEvaluationMode,
       "oaControl": oaControl,
       "oaControlTable": oaControlTable,
       "oaControlEntry": oaControlEntry,
       "oaControlLaserShutdown": oaControlLaserShutdown,
       "oaControlReset": oaControlReset,
       "oaControlModuleLedBlink": oaControlModuleLedBlink,
       "oaControlSbsEvaluationStart": oaControlSbsEvaluationStart,
       "oaMeasuringValues": oaMeasuringValues,
       "oaMeasuringValuesTable": oaMeasuringValuesTable,
       "oaMeasuringValuesEntry": oaMeasuringValuesEntry,
       "oaTemperatureLoLo": oaTemperatureLoLo,
       "oaTemperatureLo": oaTemperatureLo,
       "oaTemperatureValue": oaTemperatureValue,
       "oaTemperatureHi": oaTemperatureHi,
       "oaTemperatureHiHi": oaTemperatureHiHi,
       "oaInputPowerLoLo": oaInputPowerLoLo,
       "oaInputPowerLo": oaInputPowerLo,
       "oaInputPowerValue": oaInputPowerValue,
       "oaInputPowerHi": oaInputPowerHi,
       "oaInputPowerHiHi": oaInputPowerHiHi,
       "oaOutputPwrOrGainLoLo": oaOutputPwrOrGainLoLo,
       "oaOutputPwrOrGainLo": oaOutputPwrOrGainLo,
       "oaOutputPwrOrGainValue": oaOutputPwrOrGainValue,
       "oaOutputPwrOrGainHi": oaOutputPwrOrGainHi,
       "oaOutputPwrOrGainHiHi": oaOutputPwrOrGainHiHi,
       "oaReturnLossLoLo": oaReturnLossLoLo,
       "oaReturnLossLo": oaReturnLossLo,
       "oaReturnLossValue": oaReturnLossValue,
       "oaReturnLossHi": oaReturnLossHi,
       "oaReturnLossHiHi": oaReturnLossHiHi,
       "oaInputVoltageLoLo": oaInputVoltageLoLo,
       "oaInputVoltageLo": oaInputVoltageLo,
       "oaInputVoltageValue": oaInputVoltageValue,
       "oaInputVoltageHi": oaInputVoltageHi,
       "oaInputVoltageHiHi": oaInputVoltageHiHi,
       "oaInternalVoltage1LoLo": oaInternalVoltage1LoLo,
       "oaInternalVoltage1Lo": oaInternalVoltage1Lo,
       "oaInternalVoltage1Value": oaInternalVoltage1Value,
       "oaInternalVoltage1Hi": oaInternalVoltage1Hi,
       "oaInternalVoltage1HiHi": oaInternalVoltage1HiHi,
       "oaInternalVoltage2LoLo": oaInternalVoltage2LoLo,
       "oaInternalVoltage2Lo": oaInternalVoltage2Lo,
       "oaInternalVoltage2Value": oaInternalVoltage2Value,
       "oaInternalVoltage2Hi": oaInternalVoltage2Hi,
       "oaInternalVoltage2HiHi": oaInternalVoltage2HiHi,
       "oaInternalVoltage3LoLo": oaInternalVoltage3LoLo,
       "oaInternalVoltage3Lo": oaInternalVoltage3Lo,
       "oaInternalVoltage3Value": oaInternalVoltage3Value,
       "oaInternalVoltage3Hi": oaInternalVoltage3Hi,
       "oaInternalVoltage3HiHi": oaInternalVoltage3HiHi,
       "oaLaser1CurrentRelLoLo": oaLaser1CurrentRelLoLo,
       "oaLaser1CurrentRelLo": oaLaser1CurrentRelLo,
       "oaLaser1CurrentRelValue": oaLaser1CurrentRelValue,
       "oaLaser1CurrentRelHi": oaLaser1CurrentRelHi,
       "oaLaser1CurrentRelHiHi": oaLaser1CurrentRelHiHi,
       "oaLaser1TecRelLoLo": oaLaser1TecRelLoLo,
       "oaLaser1TecRelLo": oaLaser1TecRelLo,
       "oaLaser1TecRelValue": oaLaser1TecRelValue,
       "oaLaser1TecRelHi": oaLaser1TecRelHi,
       "oaLaser1TecRelHiHi": oaLaser1TecRelHiHi,
       "oaLaser1TemperatureLoLo": oaLaser1TemperatureLoLo,
       "oaLaser1TemperatureLo": oaLaser1TemperatureLo,
       "oaLaser1TemperatureValue": oaLaser1TemperatureValue,
       "oaLaser1TemperatureHi": oaLaser1TemperatureHi,
       "oaLaser1TemperatureHiHi": oaLaser1TemperatureHiHi,
       "oaLaser1VoltageLoLo": oaLaser1VoltageLoLo,
       "oaLaser1VoltageLo": oaLaser1VoltageLo,
       "oaLaser1VoltageValue": oaLaser1VoltageValue,
       "oaLaser1VoltageHi": oaLaser1VoltageHi,
       "oaLaser1VoltageHiHi": oaLaser1VoltageHiHi,
       "oaLaser2CurrentRelLoLo": oaLaser2CurrentRelLoLo,
       "oaLaser2CurrentRelLo": oaLaser2CurrentRelLo,
       "oaLaser2CurrentRelValue": oaLaser2CurrentRelValue,
       "oaLaser2CurrentRelHi": oaLaser2CurrentRelHi,
       "oaLaser2CurrentRelHiHi": oaLaser2CurrentRelHiHi,
       "oaLaser2TecRelLoLo": oaLaser2TecRelLoLo,
       "oaLaser2TecRelLo": oaLaser2TecRelLo,
       "oaLaser2TecRelValue": oaLaser2TecRelValue,
       "oaLaser2TecRelHi": oaLaser2TecRelHi,
       "oaLaser2TecRelHiHi": oaLaser2TecRelHiHi,
       "oaLaser2TemperatureLoLo": oaLaser2TemperatureLoLo,
       "oaLaser2TemperatureLo": oaLaser2TemperatureLo,
       "oaLaser2TemperatureValue": oaLaser2TemperatureValue,
       "oaLaser2TemperatureHi": oaLaser2TemperatureHi,
       "oaLaser2TemperatureHiHi": oaLaser2TemperatureHiHi,
       "oaLaser2VoltageLoLo": oaLaser2VoltageLoLo,
       "oaLaser2VoltageLo": oaLaser2VoltageLo,
       "oaLaser2VoltageValue": oaLaser2VoltageValue,
       "oaLaser2VoltageHi": oaLaser2VoltageHi,
       "oaLaser2VoltageHiHi": oaLaser2VoltageHiHi,
       "oaLaser3CurrentRelLoLo": oaLaser3CurrentRelLoLo,
       "oaLaser3CurrentRelLo": oaLaser3CurrentRelLo,
       "oaLaser3CurrentRelValue": oaLaser3CurrentRelValue,
       "oaLaser3CurrentRelHi": oaLaser3CurrentRelHi,
       "oaLaser3CurrentRelHiHi": oaLaser3CurrentRelHiHi,
       "oaLaser3TecRelLoLo": oaLaser3TecRelLoLo,
       "oaLaser3TecRelLo": oaLaser3TecRelLo,
       "oaLaser3TecRelValue": oaLaser3TecRelValue,
       "oaLaser3TecRelHi": oaLaser3TecRelHi,
       "oaLaser3TecRelHiHi": oaLaser3TecRelHiHi,
       "oaLaser3TemperatureLoLo": oaLaser3TemperatureLoLo,
       "oaLaser3TemperatureLo": oaLaser3TemperatureLo,
       "oaLaser3TemperatureValue": oaLaser3TemperatureValue,
       "oaLaser3TemperatureHi": oaLaser3TemperatureHi,
       "oaLaser3TemperatureHiHi": oaLaser3TemperatureHiHi,
       "oaLaser3VoltageLoLo": oaLaser3VoltageLoLo,
       "oaLaser3VoltageLo": oaLaser3VoltageLo,
       "oaLaser3VoltageValue": oaLaser3VoltageValue,
       "oaLaser3VoltageHi": oaLaser3VoltageHi,
       "oaLaser3VoltageHiHi": oaLaser3VoltageHiHi,
       "oaLaser4CurrentRelLoLo": oaLaser4CurrentRelLoLo,
       "oaLaser4CurrentRelLo": oaLaser4CurrentRelLo,
       "oaLaser4CurrentRelValue": oaLaser4CurrentRelValue,
       "oaLaser4CurrentRelHi": oaLaser4CurrentRelHi,
       "oaLaser4CurrentRelHiHi": oaLaser4CurrentRelHiHi,
       "oaLaser4TecRelLoLo": oaLaser4TecRelLoLo,
       "oaLaser4TecRelLo": oaLaser4TecRelLo,
       "oaLaser4TecRelValue": oaLaser4TecRelValue,
       "oaLaser4TecRelHi": oaLaser4TecRelHi,
       "oaLaser4TecRelHiHi": oaLaser4TecRelHiHi,
       "oaLaser4TemperatureLoLo": oaLaser4TemperatureLoLo,
       "oaLaser4TemperatureLo": oaLaser4TemperatureLo,
       "oaLaser4TemperatureValue": oaLaser4TemperatureValue,
       "oaLaser4TemperatureHi": oaLaser4TemperatureHi,
       "oaLaser4TemperatureHiHi": oaLaser4TemperatureHiHi,
       "oaLaser4VoltageLoLo": oaLaser4VoltageLoLo,
       "oaLaser4VoltageLo": oaLaser4VoltageLo,
       "oaLaser4VoltageValue": oaLaser4VoltageValue,
       "oaLaser4VoltageHi": oaLaser4VoltageHi,
       "oaLaser4VoltageHiHi": oaLaser4VoltageHiHi,
       "oaLaser5CurrentRelLoLo": oaLaser5CurrentRelLoLo,
       "oaLaser5CurrentRelLo": oaLaser5CurrentRelLo,
       "oaLaser5CurrentRelValue": oaLaser5CurrentRelValue,
       "oaLaser5CurrentRelHi": oaLaser5CurrentRelHi,
       "oaLaser5CurrentRelHiHi": oaLaser5CurrentRelHiHi,
       "oaLaser5TecRelLoLo": oaLaser5TecRelLoLo,
       "oaLaser5TecRelLo": oaLaser5TecRelLo,
       "oaLaser5TecRelValue": oaLaser5TecRelValue,
       "oaLaser5TecRelHi": oaLaser5TecRelHi,
       "oaLaser5TecRelHiHi": oaLaser5TecRelHiHi,
       "oaLaser5TemperatureLoLo": oaLaser5TemperatureLoLo,
       "oaLaser5TemperatureLo": oaLaser5TemperatureLo,
       "oaLaser5TemperatureValue": oaLaser5TemperatureValue,
       "oaLaser5TemperatureHi": oaLaser5TemperatureHi,
       "oaLaser5TemperatureHiHi": oaLaser5TemperatureHiHi,
       "oaLaser5VoltageLoLo": oaLaser5VoltageLoLo,
       "oaLaser5VoltageLo": oaLaser5VoltageLo,
       "oaLaser5VoltageValue": oaLaser5VoltageValue,
       "oaLaser5VoltageHi": oaLaser5VoltageHi,
       "oaLaser5VoltageHiHi": oaLaser5VoltageHiHi,
       "oaLaser6CurrentRelLoLo": oaLaser6CurrentRelLoLo,
       "oaLaser6CurrentRelLo": oaLaser6CurrentRelLo,
       "oaLaser6CurrentRelValue": oaLaser6CurrentRelValue,
       "oaLaser6CurrentRelHi": oaLaser6CurrentRelHi,
       "oaLaser6CurrentRelHiHi": oaLaser6CurrentRelHiHi,
       "oaLaser6TecRelLoLo": oaLaser6TecRelLoLo,
       "oaLaser6TecRelLo": oaLaser6TecRelLo,
       "oaLaser6TecRelValue": oaLaser6TecRelValue,
       "oaLaser6TecRelHi": oaLaser6TecRelHi,
       "oaLaser6TecRelHiHi": oaLaser6TecRelHiHi,
       "oaLaser6TemperatureLoLo": oaLaser6TemperatureLoLo,
       "oaLaser6TemperatureLo": oaLaser6TemperatureLo,
       "oaLaser6TemperatureValue": oaLaser6TemperatureValue,
       "oaLaser6TemperatureHi": oaLaser6TemperatureHi,
       "oaLaser6TemperatureHiHi": oaLaser6TemperatureHiHi,
       "oaLaser6VoltageLoLo": oaLaser6VoltageLoLo,
       "oaLaser6VoltageLo": oaLaser6VoltageLo,
       "oaLaser6VoltageValue": oaLaser6VoltageValue,
       "oaLaser6VoltageHi": oaLaser6VoltageHi,
       "oaLaser6VoltageHiHi": oaLaser6VoltageHiHi,
       "oaDisplay": oaDisplay,
       "oaDisplayTable": oaDisplayTable,
       "oaDisplayEntry": oaDisplayEntry,
       "oaDisplayNumberOfLasers": oaDisplayNumberOfLasers,
       "oaDisplayNumberOfInternalVoltages": oaDisplayNumberOfInternalVoltages,
       "oaDisplayExtIOSupported": oaDisplayExtIOSupported,
       "oaDisplaySbsSupported": oaDisplaySbsSupported,
       "oaDisplayReturnLossSupported": oaDisplayReturnLossSupported,
       "oaDisplaySbsEvaluatedThreshold": oaDisplaySbsEvaluatedThreshold,
       "oaDisplaySbsLastEvaluationState": oaDisplaySbsLastEvaluationState,
       "oaDisplaySbsLastEvaluationTime": oaDisplaySbsLastEvaluationTime,
       "oaDisplayOutputPwrOrGainNominal": oaDisplayOutputPwrOrGainNominal,
       "oaDisplayOutputPwrOrGainAdjusted": oaDisplayOutputPwrOrGainAdjusted,
       "oaDisplayInputVoltageNominal": oaDisplayInputVoltageNominal,
       "oaDisplayInternalVoltage1Nominal": oaDisplayInternalVoltage1Nominal,
       "oaDisplayInternalVoltage2Nominal": oaDisplayInternalVoltage2Nominal,
       "oaDisplayInternalVoltage3Nominal": oaDisplayInternalVoltage3Nominal,
       "oaDisplayLaser1VoltageNominal": oaDisplayLaser1VoltageNominal,
       "oaDisplayLaser2VoltageNominal": oaDisplayLaser2VoltageNominal,
       "oaDisplayLaser3VoltageNominal": oaDisplayLaser3VoltageNominal,
       "oaDisplayLaser4VoltageNominal": oaDisplayLaser4VoltageNominal,
       "oaDisplayLaser5VoltageNominal": oaDisplayLaser5VoltageNominal,
       "oaDisplayLaser6VoltageNominal": oaDisplayLaser6VoltageNominal,
       "oaDisplayLaser1PumpPowerRel": oaDisplayLaser1PumpPowerRel,
       "oaDisplayLaser2PumpPowerRel": oaDisplayLaser2PumpPowerRel,
       "oaDisplayLaser3PumpPowerRel": oaDisplayLaser3PumpPowerRel,
       "oaDisplayLaser4PumpPowerRel": oaDisplayLaser4PumpPowerRel,
       "oaDisplayLaser5PumpPowerRel": oaDisplayLaser5PumpPowerRel,
       "oaDisplayLaser6PumpPowerRel": oaDisplayLaser6PumpPowerRel,
       "oaDisplayLaser1FeaturesSupported": oaDisplayLaser1FeaturesSupported,
       "oaDisplayLaser2FeaturesSupported": oaDisplayLaser2FeaturesSupported,
       "oaDisplayLaser3FeaturesSupported": oaDisplayLaser3FeaturesSupported,
       "oaDisplayLaser4FeaturesSupported": oaDisplayLaser4FeaturesSupported,
       "oaDisplayLaser5FeaturesSupported": oaDisplayLaser5FeaturesSupported,
       "oaDisplayLaser6FeaturesSupported": oaDisplayLaser6FeaturesSupported,
       "oaDisplayAmplifierIsRamanType": oaDisplayAmplifierIsRamanType}
)
