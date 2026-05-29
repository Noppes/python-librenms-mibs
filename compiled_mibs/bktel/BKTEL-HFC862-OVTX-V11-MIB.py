# SNMP MIB module (BKTEL-HFC862-OVTX-V11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bktel\BKTEL-HFC862-OVTX-V11-MIB

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 experimental,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "experimental",
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



class AGCmode(Integer32):
    """Custom type AGCmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeAgcOff", 1),
          ("modeUnmodulatedAgcOn", 2),
          ("modeModulatedAgcOn", 3))
    )





class SatAGCmode(Integer32):
    """Custom type SatAGCmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("satAgcOff", 1),
          ("satAgcOn", 2))
    )





class RedundancyMode(Integer32):
    """Custom type RedundancyMode based on Integer32"""
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
          ("modeNominalMasterIrreversible", 3),
          ("modeNominalMasterFallback", 4),
          ("modeRedundantSlave", 5))
    )





class RedundancyMask(Integer32):
    """Custom type RedundancyMask based on Integer32"""
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
          ("maskSpecialAdjusted", 3))
    )





class LaserOutputMode(Integer32):
    """Custom type LaserOutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("laserShutdown", 1),
          ("laserActive", 2),
          ("laserShutdownOnMaskedError", 3))
    )





class CsoRegulationMode(Integer32):
    """Custom type CsoRegulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csoRegModeChannelControlled", 1),
          ("csoRegModePilotControlled", 2))
    )





class RegulationState(Integer32):
    """Custom type RegulationState based on Integer32"""
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
        *(("regulationStateUnknownOrNotSupported", 1),
          ("regulationStateOutputpowerBased", 2),
          ("regulationStateCsoBasedRough", 3),
          ("regulationStateCsoBasedFine", 4),
          ("regulationStatePilotBased", 5))
    )





class RfInputCapabilities(Integer32):
    """Custom type RfInputCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfInputCatvOnlySupported", 1),
          ("rfInputSatOnlySupported", 2),
          ("rfInputCatvAndSatSupported", 3))
    )





class RfInputAlarmMode(Integer32):
    """Custom type RfInputAlarmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmEnableAll", 1),
          ("alarmCatvEnableSatDisable", 2),
          ("alarmSatEnableCatvDisable", 3))
    )





class LnbSupplyValue(Integer32):
    """Custom type LnbSupplyValue based on Integer32"""
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
        *(("lnbSupplyOff", 1),
          ("lnbSupply14V", 2),
          ("lnbSupply18V", 3),
          ("lnbSupply14V_22kHz", 4),
          ("lnbSupply18V_22kHz", 5))
    )





class LnbSupplySupportedValue(Integer32):
    """Custom type LnbSupplySupportedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("lnbSupply14V18VSwitchSupported", 2),
          ("lnbSupply14V18VAnd22kHzSwitchSupported", 3))
    )





class SbsSuppressionModeValue(Integer32):
    """Custom type SbsSuppressionModeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modeStandard", 1),
          ("modeCatvOnly", 2))
    )





class SbsFiberTypeValue(Integer32):
    """Custom type SbsFiberTypeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("typeStandardFiber", 1),
          ("typeSbsOptimizedFiber", 2))
    )





class SbsFiberLengthValue(Integer32):
    """Custom type SbsFiberLengthValue based on Integer32"""
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
        *(("length10km", 1),
          ("length25km", 2),
          ("length40km", 3),
          ("length65km", 4))
    )





class NESlotWriteValue(Integer32):
    """Custom type NESlotWriteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ovtx_ObjectIdentity = ObjectIdentity
ovtx = _Ovtx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101)
)
_OvtxCommon_ObjectIdentity = ObjectIdentity
ovtxCommon = _OvtxCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 1)
)


class _OvtxCommonNumberOfModules_Type(Integer32):
    """Custom type ovtxCommonNumberOfModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_OvtxCommonNumberOfModules_Type.__name__ = "Integer32"
_OvtxCommonNumberOfModules_Object = MibScalar
ovtxCommonNumberOfModules = _OvtxCommonNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 1, 1),
    _OvtxCommonNumberOfModules_Type()
)
ovtxCommonNumberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxCommonNumberOfModules.setStatus("mandatory")
_OvtxCommonTable_Object = MibTable
ovtxCommonTable = _OvtxCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 1, 2)
)
if mibBuilder.loadTexts:
    ovtxCommonTable.setStatus("mandatory")
_OvtxCommonEntry_Object = MibTableRow
ovtxCommonEntry = _OvtxCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 1, 2, 1)
)
ovtxCommonEntry.setIndexNames(
    (0, "BKTEL-HFC862-OVTX-V11-MIB", "ovtxNESlot"),
)
if mibBuilder.loadTexts:
    ovtxCommonEntry.setStatus("mandatory")
_OvtxNESlot_Type = NESlotValue
_OvtxNESlot_Object = MibTableColumn
ovtxNESlot = _OvtxNESlot_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 1, 2, 1, 1),
    _OvtxNESlot_Type()
)
ovtxNESlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxNESlot.setStatus("mandatory")


class _OvtxCommonType_Type(DisplayString):
    """Custom type ovtxCommonType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OvtxCommonType_Type.__name__ = "DisplayString"
_OvtxCommonType_Object = MibTableColumn
ovtxCommonType = _OvtxCommonType_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 1, 2, 1, 2),
    _OvtxCommonType_Type()
)
ovtxCommonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxCommonType.setStatus("mandatory")
_OvtxCommonDescr_Type = DisplayString
_OvtxCommonDescr_Object = MibTableColumn
ovtxCommonDescr = _OvtxCommonDescr_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 1, 2, 1, 3),
    _OvtxCommonDescr_Type()
)
ovtxCommonDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxCommonDescr.setStatus("mandatory")


class _OvtxCommonFirmwareId_Type(DisplayString):
    """Custom type ovtxCommonFirmwareId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OvtxCommonFirmwareId_Type.__name__ = "DisplayString"
_OvtxCommonFirmwareId_Object = MibTableColumn
ovtxCommonFirmwareId = _OvtxCommonFirmwareId_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 1, 2, 1, 4),
    _OvtxCommonFirmwareId_Type()
)
ovtxCommonFirmwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxCommonFirmwareId.setStatus("mandatory")
_OvtxCommonModuleWidth_Type = ModuleWidthValue
_OvtxCommonModuleWidth_Object = MibTableColumn
ovtxCommonModuleWidth = _OvtxCommonModuleWidth_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 1, 2, 1, 5),
    _OvtxCommonModuleWidth_Type()
)
ovtxCommonModuleWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxCommonModuleWidth.setStatus("optional")
_OvtxStates_ObjectIdentity = ObjectIdentity
ovtxStates = _OvtxStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2)
)
_OvtxStatesTable_Object = MibTable
ovtxStatesTable = _OvtxStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1)
)
if mibBuilder.loadTexts:
    ovtxStatesTable.setStatus("mandatory")
_OvtxStatesEntry_Object = MibTableRow
ovtxStatesEntry = _OvtxStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1)
)
ovtxStatesEntry.setIndexNames(
    (0, "BKTEL-HFC862-OVTX-V11-MIB", "ovtxNESlot"),
)
if mibBuilder.loadTexts:
    ovtxStatesEntry.setStatus("mandatory")
_OvtxStatesOutputLow_Type = PerceivedSeverityValue
_OvtxStatesOutputLow_Object = MibTableColumn
ovtxStatesOutputLow = _OvtxStatesOutputLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 1),
    _OvtxStatesOutputLow_Type()
)
ovtxStatesOutputLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesOutputLow.setStatus("mandatory")
_OvtxStatesOutputHigh_Type = PerceivedSeverityValue
_OvtxStatesOutputHigh_Object = MibTableColumn
ovtxStatesOutputHigh = _OvtxStatesOutputHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 2),
    _OvtxStatesOutputHigh_Type()
)
ovtxStatesOutputHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesOutputHigh.setStatus("mandatory")
_OvtxStatesInputLow_Type = PerceivedSeverityValue
_OvtxStatesInputLow_Object = MibTableColumn
ovtxStatesInputLow = _OvtxStatesInputLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 3),
    _OvtxStatesInputLow_Type()
)
ovtxStatesInputLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesInputLow.setStatus("mandatory")
_OvtxStatesLaserAging_Type = PerceivedSeverityValue
_OvtxStatesLaserAging_Object = MibTableColumn
ovtxStatesLaserAging = _OvtxStatesLaserAging_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 4),
    _OvtxStatesLaserAging_Type()
)
ovtxStatesLaserAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesLaserAging.setStatus("mandatory")
_OvtxStatesTecHigh_Type = PerceivedSeverityValue
_OvtxStatesTecHigh_Object = MibTableColumn
ovtxStatesTecHigh = _OvtxStatesTecHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 5),
    _OvtxStatesTecHigh_Type()
)
ovtxStatesTecHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesTecHigh.setStatus("mandatory")
_OvtxStatesLaserTempLow_Type = PerceivedSeverityValue
_OvtxStatesLaserTempLow_Object = MibTableColumn
ovtxStatesLaserTempLow = _OvtxStatesLaserTempLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 6),
    _OvtxStatesLaserTempLow_Type()
)
ovtxStatesLaserTempLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesLaserTempLow.setStatus("mandatory")
_OvtxStatesLaserTempHigh_Type = PerceivedSeverityValue
_OvtxStatesLaserTempHigh_Object = MibTableColumn
ovtxStatesLaserTempHigh = _OvtxStatesLaserTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 7),
    _OvtxStatesLaserTempHigh_Type()
)
ovtxStatesLaserTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesLaserTempHigh.setStatus("mandatory")
_OvtxStatesOmiOrRfgainLow_Type = PerceivedSeverityValue
_OvtxStatesOmiOrRfgainLow_Object = MibTableColumn
ovtxStatesOmiOrRfgainLow = _OvtxStatesOmiOrRfgainLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 8),
    _OvtxStatesOmiOrRfgainLow_Type()
)
ovtxStatesOmiOrRfgainLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesOmiOrRfgainLow.setStatus("mandatory")
_OvtxStatesOmiOrRfgainHigh_Type = PerceivedSeverityValue
_OvtxStatesOmiOrRfgainHigh_Object = MibTableColumn
ovtxStatesOmiOrRfgainHigh = _OvtxStatesOmiOrRfgainHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 9),
    _OvtxStatesOmiOrRfgainHigh_Type()
)
ovtxStatesOmiOrRfgainHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesOmiOrRfgainHigh.setStatus("mandatory")
_OvtxStatesPowerSupplyLeft_Type = PerceivedSeverityValue
_OvtxStatesPowerSupplyLeft_Object = MibTableColumn
ovtxStatesPowerSupplyLeft = _OvtxStatesPowerSupplyLeft_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 10),
    _OvtxStatesPowerSupplyLeft_Type()
)
ovtxStatesPowerSupplyLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPowerSupplyLeft.setStatus("mandatory")
_OvtxStatesPowerSupplyRight_Type = PerceivedSeverityValue
_OvtxStatesPowerSupplyRight_Object = MibTableColumn
ovtxStatesPowerSupplyRight = _OvtxStatesPowerSupplyRight_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 11),
    _OvtxStatesPowerSupplyRight_Type()
)
ovtxStatesPowerSupplyRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPowerSupplyRight.setStatus("mandatory")
_OvtxStatesFanLeft_Type = PerceivedSeverityValue
_OvtxStatesFanLeft_Object = MibTableColumn
ovtxStatesFanLeft = _OvtxStatesFanLeft_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 12),
    _OvtxStatesFanLeft_Type()
)
ovtxStatesFanLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesFanLeft.setStatus("mandatory")
_OvtxStatesFanRight_Type = PerceivedSeverityValue
_OvtxStatesFanRight_Object = MibTableColumn
ovtxStatesFanRight = _OvtxStatesFanRight_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 13),
    _OvtxStatesFanRight_Type()
)
ovtxStatesFanRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesFanRight.setStatus("mandatory")
_OvtxStatesTemperatureLow_Type = PerceivedSeverityValue
_OvtxStatesTemperatureLow_Object = MibTableColumn
ovtxStatesTemperatureLow = _OvtxStatesTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 14),
    _OvtxStatesTemperatureLow_Type()
)
ovtxStatesTemperatureLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesTemperatureLow.setStatus("mandatory")
_OvtxStatesTemperatureHigh_Type = PerceivedSeverityValue
_OvtxStatesTemperatureHigh_Object = MibTableColumn
ovtxStatesTemperatureHigh = _OvtxStatesTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 15),
    _OvtxStatesTemperatureHigh_Type()
)
ovtxStatesTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesTemperatureHigh.setStatus("mandatory")
_OvtxStatesPlus3p3VLow_Type = PerceivedSeverityValue
_OvtxStatesPlus3p3VLow_Object = MibTableColumn
ovtxStatesPlus3p3VLow = _OvtxStatesPlus3p3VLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 16),
    _OvtxStatesPlus3p3VLow_Type()
)
ovtxStatesPlus3p3VLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPlus3p3VLow.setStatus("mandatory")
_OvtxStatesPlus3p3VHigh_Type = PerceivedSeverityValue
_OvtxStatesPlus3p3VHigh_Object = MibTableColumn
ovtxStatesPlus3p3VHigh = _OvtxStatesPlus3p3VHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 17),
    _OvtxStatesPlus3p3VHigh_Type()
)
ovtxStatesPlus3p3VHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPlus3p3VHigh.setStatus("mandatory")
_OvtxStatesPlus5VLow_Type = PerceivedSeverityValue
_OvtxStatesPlus5VLow_Object = MibTableColumn
ovtxStatesPlus5VLow = _OvtxStatesPlus5VLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 18),
    _OvtxStatesPlus5VLow_Type()
)
ovtxStatesPlus5VLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPlus5VLow.setStatus("mandatory")
_OvtxStatesPlus5VHigh_Type = PerceivedSeverityValue
_OvtxStatesPlus5VHigh_Object = MibTableColumn
ovtxStatesPlus5VHigh = _OvtxStatesPlus5VHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 19),
    _OvtxStatesPlus5VHigh_Type()
)
ovtxStatesPlus5VHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPlus5VHigh.setStatus("mandatory")
_OvtxStatesPlus12VLow_Type = PerceivedSeverityValue
_OvtxStatesPlus12VLow_Object = MibTableColumn
ovtxStatesPlus12VLow = _OvtxStatesPlus12VLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 20),
    _OvtxStatesPlus12VLow_Type()
)
ovtxStatesPlus12VLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPlus12VLow.setStatus("mandatory")
_OvtxStatesPlus12VHigh_Type = PerceivedSeverityValue
_OvtxStatesPlus12VHigh_Object = MibTableColumn
ovtxStatesPlus12VHigh = _OvtxStatesPlus12VHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 21),
    _OvtxStatesPlus12VHigh_Type()
)
ovtxStatesPlus12VHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPlus12VHigh.setStatus("mandatory")
_OvtxStatesPlus24VLow_Type = PerceivedSeverityValue
_OvtxStatesPlus24VLow_Object = MibTableColumn
ovtxStatesPlus24VLow = _OvtxStatesPlus24VLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 22),
    _OvtxStatesPlus24VLow_Type()
)
ovtxStatesPlus24VLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPlus24VLow.setStatus("mandatory")
_OvtxStatesPlus24VHigh_Type = PerceivedSeverityValue
_OvtxStatesPlus24VHigh_Object = MibTableColumn
ovtxStatesPlus24VHigh = _OvtxStatesPlus24VHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 23),
    _OvtxStatesPlus24VHigh_Type()
)
ovtxStatesPlus24VHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesPlus24VHigh.setStatus("mandatory")
_OvtxStatesMinus5VLow_Type = PerceivedSeverityValue
_OvtxStatesMinus5VLow_Object = MibTableColumn
ovtxStatesMinus5VLow = _OvtxStatesMinus5VLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 24),
    _OvtxStatesMinus5VLow_Type()
)
ovtxStatesMinus5VLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesMinus5VLow.setStatus("mandatory")
_OvtxStatesMinus5VHigh_Type = PerceivedSeverityValue
_OvtxStatesMinus5VHigh_Object = MibTableColumn
ovtxStatesMinus5VHigh = _OvtxStatesMinus5VHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 25),
    _OvtxStatesMinus5VHigh_Type()
)
ovtxStatesMinus5VHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesMinus5VHigh.setStatus("mandatory")
_OvtxStatesMinus12VLow_Type = PerceivedSeverityValue
_OvtxStatesMinus12VLow_Object = MibTableColumn
ovtxStatesMinus12VLow = _OvtxStatesMinus12VLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 26),
    _OvtxStatesMinus12VLow_Type()
)
ovtxStatesMinus12VLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesMinus12VLow.setStatus("mandatory")
_OvtxStatesMinus12VHigh_Type = PerceivedSeverityValue
_OvtxStatesMinus12VHigh_Object = MibTableColumn
ovtxStatesMinus12VHigh = _OvtxStatesMinus12VHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 27),
    _OvtxStatesMinus12VHigh_Type()
)
ovtxStatesMinus12VHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesMinus12VHigh.setStatus("mandatory")
_OvtxStatesLaserShutdown_Type = PerceivedSeverityValue
_OvtxStatesLaserShutdown_Object = MibTableColumn
ovtxStatesLaserShutdown = _OvtxStatesLaserShutdown_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 28),
    _OvtxStatesLaserShutdown_Type()
)
ovtxStatesLaserShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesLaserShutdown.setStatus("mandatory")
_OvtxStatesInitializing_Type = PerceivedSeverityValue
_OvtxStatesInitializing_Object = MibTableColumn
ovtxStatesInitializing = _OvtxStatesInitializing_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 29),
    _OvtxStatesInitializing_Type()
)
ovtxStatesInitializing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesInitializing.setStatus("mandatory")
_OvtxStatesBootloader_Type = PerceivedSeverityValue
_OvtxStatesBootloader_Object = MibTableColumn
ovtxStatesBootloader = _OvtxStatesBootloader_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 30),
    _OvtxStatesBootloader_Type()
)
ovtxStatesBootloader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesBootloader.setStatus("mandatory")
_OvtxStatesCommLoss_Type = PerceivedSeverityValue
_OvtxStatesCommLoss_Object = MibTableColumn
ovtxStatesCommLoss = _OvtxStatesCommLoss_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 31),
    _OvtxStatesCommLoss_Type()
)
ovtxStatesCommLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesCommLoss.setStatus("mandatory")
_OvtxStatesInputHigh_Type = PerceivedSeverityValue
_OvtxStatesInputHigh_Object = MibTableColumn
ovtxStatesInputHigh = _OvtxStatesInputHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 32),
    _OvtxStatesInputHigh_Type()
)
ovtxStatesInputHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesInputHigh.setStatus("mandatory")
_OvtxStatesRedundancySwitch_Type = PerceivedSeverityValue
_OvtxStatesRedundancySwitch_Object = MibTableColumn
ovtxStatesRedundancySwitch = _OvtxStatesRedundancySwitch_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 33),
    _OvtxStatesRedundancySwitch_Type()
)
ovtxStatesRedundancySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesRedundancySwitch.setStatus("mandatory")
_OvtxStatesSatInputLow_Type = PerceivedSeverityValue
_OvtxStatesSatInputLow_Object = MibTableColumn
ovtxStatesSatInputLow = _OvtxStatesSatInputLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 34),
    _OvtxStatesSatInputLow_Type()
)
ovtxStatesSatInputLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesSatInputLow.setStatus("mandatory")
_OvtxStatesSatInputHigh_Type = PerceivedSeverityValue
_OvtxStatesSatInputHigh_Object = MibTableColumn
ovtxStatesSatInputHigh = _OvtxStatesSatInputHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 35),
    _OvtxStatesSatInputHigh_Type()
)
ovtxStatesSatInputHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesSatInputHigh.setStatus("mandatory")
_OvtxStatesSatOmiOrRfgainLow_Type = PerceivedSeverityValue
_OvtxStatesSatOmiOrRfgainLow_Object = MibTableColumn
ovtxStatesSatOmiOrRfgainLow = _OvtxStatesSatOmiOrRfgainLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 36),
    _OvtxStatesSatOmiOrRfgainLow_Type()
)
ovtxStatesSatOmiOrRfgainLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesSatOmiOrRfgainLow.setStatus("mandatory")
_OvtxStatesSatOmiOrRfgainHigh_Type = PerceivedSeverityValue
_OvtxStatesSatOmiOrRfgainHigh_Object = MibTableColumn
ovtxStatesSatOmiOrRfgainHigh = _OvtxStatesSatOmiOrRfgainHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 37),
    _OvtxStatesSatOmiOrRfgainHigh_Type()
)
ovtxStatesSatOmiOrRfgainHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesSatOmiOrRfgainHigh.setStatus("mandatory")
_OvtxStatesSatLnbShortCircuit_Type = PerceivedSeverityValue
_OvtxStatesSatLnbShortCircuit_Object = MibTableColumn
ovtxStatesSatLnbShortCircuit = _OvtxStatesSatLnbShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 38),
    _OvtxStatesSatLnbShortCircuit_Type()
)
ovtxStatesSatLnbShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesSatLnbShortCircuit.setStatus("mandatory")
_OvtxStatesSbs1Level_Type = PerceivedSeverityValue
_OvtxStatesSbs1Level_Object = MibTableColumn
ovtxStatesSbs1Level = _OvtxStatesSbs1Level_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 39),
    _OvtxStatesSbs1Level_Type()
)
ovtxStatesSbs1Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesSbs1Level.setStatus("mandatory")
_OvtxStatesSbs2Level_Type = PerceivedSeverityValue
_OvtxStatesSbs2Level_Object = MibTableColumn
ovtxStatesSbs2Level = _OvtxStatesSbs2Level_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 40),
    _OvtxStatesSbs2Level_Type()
)
ovtxStatesSbs2Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesSbs2Level.setStatus("mandatory")
_OvtxStatesSbs1PllNotLocked_Type = PerceivedSeverityValue
_OvtxStatesSbs1PllNotLocked_Object = MibTableColumn
ovtxStatesSbs1PllNotLocked = _OvtxStatesSbs1PllNotLocked_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 41),
    _OvtxStatesSbs1PllNotLocked_Type()
)
ovtxStatesSbs1PllNotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesSbs1PllNotLocked.setStatus("mandatory")
_OvtxStatesSbs2PllNotLocked_Type = PerceivedSeverityValue
_OvtxStatesSbs2PllNotLocked_Object = MibTableColumn
ovtxStatesSbs2PllNotLocked = _OvtxStatesSbs2PllNotLocked_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 42),
    _OvtxStatesSbs2PllNotLocked_Type()
)
ovtxStatesSbs2PllNotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesSbs2PllNotLocked.setStatus("mandatory")
_OvtxStatesInternalAlarm_Type = PerceivedSeverityValue
_OvtxStatesInternalAlarm_Object = MibTableColumn
ovtxStatesInternalAlarm = _OvtxStatesInternalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 2, 1, 1, 43),
    _OvtxStatesInternalAlarm_Type()
)
ovtxStatesInternalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxStatesInternalAlarm.setStatus("mandatory")
_OvtxConfiguration_ObjectIdentity = ObjectIdentity
ovtxConfiguration = _OvtxConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3)
)
_OvtxConfigurationTable_Object = MibTable
ovtxConfigurationTable = _OvtxConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1)
)
if mibBuilder.loadTexts:
    ovtxConfigurationTable.setStatus("mandatory")
_OvtxConfigurationEntry_Object = MibTableRow
ovtxConfigurationEntry = _OvtxConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1)
)
ovtxConfigurationEntry.setIndexNames(
    (0, "BKTEL-HFC862-OVTX-V11-MIB", "ovtxNESlot"),
)
if mibBuilder.loadTexts:
    ovtxConfigurationEntry.setStatus("mandatory")
_OvtxConfigurationNESlotWrite_Type = NESlotWriteValue
_OvtxConfigurationNESlotWrite_Object = MibTableColumn
ovtxConfigurationNESlotWrite = _OvtxConfigurationNESlotWrite_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 1),
    _OvtxConfigurationNESlotWrite_Type()
)
ovtxConfigurationNESlotWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationNESlotWrite.setStatus("optional")
_OvtxConfigurationModeAGC_Type = AGCmode
_OvtxConfigurationModeAGC_Object = MibTableColumn
ovtxConfigurationModeAGC = _OvtxConfigurationModeAGC_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 2),
    _OvtxConfigurationModeAGC_Type()
)
ovtxConfigurationModeAGC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationModeAGC.setStatus("mandatory")
_OvtxConfigurationOmi_Type = Integer32
_OvtxConfigurationOmi_Object = MibTableColumn
ovtxConfigurationOmi = _OvtxConfigurationOmi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 3),
    _OvtxConfigurationOmi_Type()
)
ovtxConfigurationOmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationOmi.setStatus("mandatory")
_OvtxConfigurationRfGain_Type = Integer32
_OvtxConfigurationRfGain_Object = MibTableColumn
ovtxConfigurationRfGain = _OvtxConfigurationRfGain_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 4),
    _OvtxConfigurationRfGain_Type()
)
ovtxConfigurationRfGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfGain.setStatus("mandatory")
_OvtxConfigurationSbsSuppression_Type = Integer32
_OvtxConfigurationSbsSuppression_Object = MibTableColumn
ovtxConfigurationSbsSuppression = _OvtxConfigurationSbsSuppression_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 5),
    _OvtxConfigurationSbsSuppression_Type()
)
ovtxConfigurationSbsSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSbsSuppression.setStatus("mandatory")
_OvtxConfigurationChannelDistance_Type = Integer32
_OvtxConfigurationChannelDistance_Object = MibTableColumn
ovtxConfigurationChannelDistance = _OvtxConfigurationChannelDistance_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 6),
    _OvtxConfigurationChannelDistance_Type()
)
ovtxConfigurationChannelDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationChannelDistance.setStatus("mandatory")
_OvtxConfigurationLaserFrequency_Type = Integer32
_OvtxConfigurationLaserFrequency_Object = MibTableColumn
ovtxConfigurationLaserFrequency = _OvtxConfigurationLaserFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 7),
    _OvtxConfigurationLaserFrequency_Type()
)
ovtxConfigurationLaserFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationLaserFrequency.setStatus("mandatory")
_OvtxConfigurationRfInputLimitLoLo_Type = Integer32
_OvtxConfigurationRfInputLimitLoLo_Object = MibTableColumn
ovtxConfigurationRfInputLimitLoLo = _OvtxConfigurationRfInputLimitLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 8),
    _OvtxConfigurationRfInputLimitLoLo_Type()
)
ovtxConfigurationRfInputLimitLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfInputLimitLoLo.setStatus("mandatory")
_OvtxConfigurationRfInputLimitLo_Type = Integer32
_OvtxConfigurationRfInputLimitLo_Object = MibTableColumn
ovtxConfigurationRfInputLimitLo = _OvtxConfigurationRfInputLimitLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 9),
    _OvtxConfigurationRfInputLimitLo_Type()
)
ovtxConfigurationRfInputLimitLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfInputLimitLo.setStatus("mandatory")
_OvtxConfigurationRfInputLimitHi_Type = Integer32
_OvtxConfigurationRfInputLimitHi_Object = MibTableColumn
ovtxConfigurationRfInputLimitHi = _OvtxConfigurationRfInputLimitHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 10),
    _OvtxConfigurationRfInputLimitHi_Type()
)
ovtxConfigurationRfInputLimitHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfInputLimitHi.setStatus("mandatory")
_OvtxConfigurationRfInputLimitHiHi_Type = Integer32
_OvtxConfigurationRfInputLimitHiHi_Object = MibTableColumn
ovtxConfigurationRfInputLimitHiHi = _OvtxConfigurationRfInputLimitHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 11),
    _OvtxConfigurationRfInputLimitHiHi_Type()
)
ovtxConfigurationRfInputLimitHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfInputLimitHiHi.setStatus("mandatory")
_OvtxConfigurationRfGainMeasuredLimitLoLo_Type = Integer32
_OvtxConfigurationRfGainMeasuredLimitLoLo_Object = MibTableColumn
ovtxConfigurationRfGainMeasuredLimitLoLo = _OvtxConfigurationRfGainMeasuredLimitLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 12),
    _OvtxConfigurationRfGainMeasuredLimitLoLo_Type()
)
ovtxConfigurationRfGainMeasuredLimitLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfGainMeasuredLimitLoLo.setStatus("mandatory")
_OvtxConfigurationRfGainMeasuredLimitLo_Type = Integer32
_OvtxConfigurationRfGainMeasuredLimitLo_Object = MibTableColumn
ovtxConfigurationRfGainMeasuredLimitLo = _OvtxConfigurationRfGainMeasuredLimitLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 13),
    _OvtxConfigurationRfGainMeasuredLimitLo_Type()
)
ovtxConfigurationRfGainMeasuredLimitLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfGainMeasuredLimitLo.setStatus("mandatory")
_OvtxConfigurationRfGainMeasuredLimitHi_Type = Integer32
_OvtxConfigurationRfGainMeasuredLimitHi_Object = MibTableColumn
ovtxConfigurationRfGainMeasuredLimitHi = _OvtxConfigurationRfGainMeasuredLimitHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 14),
    _OvtxConfigurationRfGainMeasuredLimitHi_Type()
)
ovtxConfigurationRfGainMeasuredLimitHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfGainMeasuredLimitHi.setStatus("mandatory")
_OvtxConfigurationRfGainMeasuredLimitHiHi_Type = Integer32
_OvtxConfigurationRfGainMeasuredLimitHiHi_Object = MibTableColumn
ovtxConfigurationRfGainMeasuredLimitHiHi = _OvtxConfigurationRfGainMeasuredLimitHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 15),
    _OvtxConfigurationRfGainMeasuredLimitHiHi_Type()
)
ovtxConfigurationRfGainMeasuredLimitHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfGainMeasuredLimitHiHi.setStatus("mandatory")
_OvtxConfigurationOmiMeasuredLimitLoLo_Type = Integer32
_OvtxConfigurationOmiMeasuredLimitLoLo_Object = MibTableColumn
ovtxConfigurationOmiMeasuredLimitLoLo = _OvtxConfigurationOmiMeasuredLimitLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 16),
    _OvtxConfigurationOmiMeasuredLimitLoLo_Type()
)
ovtxConfigurationOmiMeasuredLimitLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationOmiMeasuredLimitLoLo.setStatus("mandatory")
_OvtxConfigurationOmiMeasuredLimitLo_Type = Integer32
_OvtxConfigurationOmiMeasuredLimitLo_Object = MibTableColumn
ovtxConfigurationOmiMeasuredLimitLo = _OvtxConfigurationOmiMeasuredLimitLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 17),
    _OvtxConfigurationOmiMeasuredLimitLo_Type()
)
ovtxConfigurationOmiMeasuredLimitLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationOmiMeasuredLimitLo.setStatus("mandatory")
_OvtxConfigurationOmiMeasuredLimitHi_Type = Integer32
_OvtxConfigurationOmiMeasuredLimitHi_Object = MibTableColumn
ovtxConfigurationOmiMeasuredLimitHi = _OvtxConfigurationOmiMeasuredLimitHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 18),
    _OvtxConfigurationOmiMeasuredLimitHi_Type()
)
ovtxConfigurationOmiMeasuredLimitHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationOmiMeasuredLimitHi.setStatus("mandatory")
_OvtxConfigurationOmiMeasuredLimitHiHi_Type = Integer32
_OvtxConfigurationOmiMeasuredLimitHiHi_Object = MibTableColumn
ovtxConfigurationOmiMeasuredLimitHiHi = _OvtxConfigurationOmiMeasuredLimitHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 19),
    _OvtxConfigurationOmiMeasuredLimitHiHi_Type()
)
ovtxConfigurationOmiMeasuredLimitHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationOmiMeasuredLimitHiHi.setStatus("mandatory")
_OvtxConfigurationOutputPwrLimitLoLo_Type = Integer32
_OvtxConfigurationOutputPwrLimitLoLo_Object = MibTableColumn
ovtxConfigurationOutputPwrLimitLoLo = _OvtxConfigurationOutputPwrLimitLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 20),
    _OvtxConfigurationOutputPwrLimitLoLo_Type()
)
ovtxConfigurationOutputPwrLimitLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationOutputPwrLimitLoLo.setStatus("mandatory")
_OvtxConfigurationOutputPwrLimitLo_Type = Integer32
_OvtxConfigurationOutputPwrLimitLo_Object = MibTableColumn
ovtxConfigurationOutputPwrLimitLo = _OvtxConfigurationOutputPwrLimitLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 21),
    _OvtxConfigurationOutputPwrLimitLo_Type()
)
ovtxConfigurationOutputPwrLimitLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationOutputPwrLimitLo.setStatus("mandatory")
_OvtxConfigurationOutputPwrLimitHi_Type = Integer32
_OvtxConfigurationOutputPwrLimitHi_Object = MibTableColumn
ovtxConfigurationOutputPwrLimitHi = _OvtxConfigurationOutputPwrLimitHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 22),
    _OvtxConfigurationOutputPwrLimitHi_Type()
)
ovtxConfigurationOutputPwrLimitHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationOutputPwrLimitHi.setStatus("mandatory")
_OvtxConfigurationOutputPwrLimitHiHi_Type = Integer32
_OvtxConfigurationOutputPwrLimitHiHi_Object = MibTableColumn
ovtxConfigurationOutputPwrLimitHiHi = _OvtxConfigurationOutputPwrLimitHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 23),
    _OvtxConfigurationOutputPwrLimitHiHi_Type()
)
ovtxConfigurationOutputPwrLimitHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationOutputPwrLimitHiHi.setStatus("mandatory")
_OvtxConfigurationRedundancyMode_Type = RedundancyMode
_OvtxConfigurationRedundancyMode_Object = MibTableColumn
ovtxConfigurationRedundancyMode = _OvtxConfigurationRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 24),
    _OvtxConfigurationRedundancyMode_Type()
)
ovtxConfigurationRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRedundancyMode.setStatus("mandatory")
_OvtxConfigurationRedundancyMask_Type = RedundancyMask
_OvtxConfigurationRedundancyMask_Object = MibTableColumn
ovtxConfigurationRedundancyMask = _OvtxConfigurationRedundancyMask_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 25),
    _OvtxConfigurationRedundancyMask_Type()
)
ovtxConfigurationRedundancyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRedundancyMask.setStatus("mandatory")
_OvtxConfigurationCsoRegulationMode_Type = CsoRegulationMode
_OvtxConfigurationCsoRegulationMode_Object = MibTableColumn
ovtxConfigurationCsoRegulationMode = _OvtxConfigurationCsoRegulationMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 26),
    _OvtxConfigurationCsoRegulationMode_Type()
)
ovtxConfigurationCsoRegulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationCsoRegulationMode.setStatus("mandatory")
_OvtxConfigurationSlope_Type = Integer32
_OvtxConfigurationSlope_Object = MibTableColumn
ovtxConfigurationSlope = _OvtxConfigurationSlope_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 27),
    _OvtxConfigurationSlope_Type()
)
ovtxConfigurationSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSlope.setStatus("mandatory")
_OvtxConfigurationFiberLength_Type = Integer32
_OvtxConfigurationFiberLength_Object = MibTableColumn
ovtxConfigurationFiberLength = _OvtxConfigurationFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 28),
    _OvtxConfigurationFiberLength_Type()
)
ovtxConfigurationFiberLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationFiberLength.setStatus("mandatory")
_OvtxConfigurationSatModeAGC_Type = SatAGCmode
_OvtxConfigurationSatModeAGC_Object = MibTableColumn
ovtxConfigurationSatModeAGC = _OvtxConfigurationSatModeAGC_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 29),
    _OvtxConfigurationSatModeAGC_Type()
)
ovtxConfigurationSatModeAGC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSatModeAGC.setStatus("mandatory")
_OvtxConfigurationSatOmi_Type = Integer32
_OvtxConfigurationSatOmi_Object = MibTableColumn
ovtxConfigurationSatOmi = _OvtxConfigurationSatOmi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 30),
    _OvtxConfigurationSatOmi_Type()
)
ovtxConfigurationSatOmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSatOmi.setStatus("mandatory")
_OvtxConfigurationSatRfGain_Type = Integer32
_OvtxConfigurationSatRfGain_Object = MibTableColumn
ovtxConfigurationSatRfGain = _OvtxConfigurationSatRfGain_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 31),
    _OvtxConfigurationSatRfGain_Type()
)
ovtxConfigurationSatRfGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSatRfGain.setStatus("mandatory")
_OvtxConfigurationSatSlope_Type = Integer32
_OvtxConfigurationSatSlope_Object = MibTableColumn
ovtxConfigurationSatSlope = _OvtxConfigurationSatSlope_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 32),
    _OvtxConfigurationSatSlope_Type()
)
ovtxConfigurationSatSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSatSlope.setStatus("mandatory")
_OvtxConfigurationRfInputAlarmMode_Type = RfInputAlarmMode
_OvtxConfigurationRfInputAlarmMode_Object = MibTableColumn
ovtxConfigurationRfInputAlarmMode = _OvtxConfigurationRfInputAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 33),
    _OvtxConfigurationRfInputAlarmMode_Type()
)
ovtxConfigurationRfInputAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationRfInputAlarmMode.setStatus("mandatory")
_OvtxConfigurationSatLnbSupply_Type = LnbSupplyValue
_OvtxConfigurationSatLnbSupply_Object = MibTableColumn
ovtxConfigurationSatLnbSupply = _OvtxConfigurationSatLnbSupply_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 34),
    _OvtxConfigurationSatLnbSupply_Type()
)
ovtxConfigurationSatLnbSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSatLnbSupply.setStatus("mandatory")
_OvtxConfigurationSbsSuppressionMode_Type = SbsSuppressionModeValue
_OvtxConfigurationSbsSuppressionMode_Object = MibTableColumn
ovtxConfigurationSbsSuppressionMode = _OvtxConfigurationSbsSuppressionMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 35),
    _OvtxConfigurationSbsSuppressionMode_Type()
)
ovtxConfigurationSbsSuppressionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSbsSuppressionMode.setStatus("mandatory")
_OvtxConfigurationSbsFiberType_Type = SbsFiberTypeValue
_OvtxConfigurationSbsFiberType_Object = MibTableColumn
ovtxConfigurationSbsFiberType = _OvtxConfigurationSbsFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 36),
    _OvtxConfigurationSbsFiberType_Type()
)
ovtxConfigurationSbsFiberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSbsFiberType.setStatus("mandatory")
_OvtxConfigurationSbsFiberLength_Type = SbsFiberLengthValue
_OvtxConfigurationSbsFiberLength_Object = MibTableColumn
ovtxConfigurationSbsFiberLength = _OvtxConfigurationSbsFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 3, 1, 1, 37),
    _OvtxConfigurationSbsFiberLength_Type()
)
ovtxConfigurationSbsFiberLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxConfigurationSbsFiberLength.setStatus("mandatory")
_OvtxControl_ObjectIdentity = ObjectIdentity
ovtxControl = _OvtxControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 4)
)
_OvtxControlTable_Object = MibTable
ovtxControlTable = _OvtxControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 4, 1)
)
if mibBuilder.loadTexts:
    ovtxControlTable.setStatus("mandatory")
_OvtxControlEntry_Object = MibTableRow
ovtxControlEntry = _OvtxControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 4, 1, 1)
)
ovtxControlEntry.setIndexNames(
    (0, "BKTEL-HFC862-OVTX-V11-MIB", "ovtxNESlot"),
)
if mibBuilder.loadTexts:
    ovtxControlEntry.setStatus("mandatory")
_OvtxControlLaserOutputMode_Type = LaserOutputMode
_OvtxControlLaserOutputMode_Object = MibTableColumn
ovtxControlLaserOutputMode = _OvtxControlLaserOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 4, 1, 1, 1),
    _OvtxControlLaserOutputMode_Type()
)
ovtxControlLaserOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxControlLaserOutputMode.setStatus("mandatory")
_OvtxControlReset_Type = TruthValue
_OvtxControlReset_Object = MibTableColumn
ovtxControlReset = _OvtxControlReset_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 4, 1, 1, 2),
    _OvtxControlReset_Type()
)
ovtxControlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxControlReset.setStatus("mandatory")
_OvtxControlModuleLedBlink_Type = TruthValue
_OvtxControlModuleLedBlink_Object = MibTableColumn
ovtxControlModuleLedBlink = _OvtxControlModuleLedBlink_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 4, 1, 1, 3),
    _OvtxControlModuleLedBlink_Type()
)
ovtxControlModuleLedBlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxControlModuleLedBlink.setStatus("mandatory")
_OvtxMeasuringValues_ObjectIdentity = ObjectIdentity
ovtxMeasuringValues = _OvtxMeasuringValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5)
)
_OvtxMeasuringValuesTable_Object = MibTable
ovtxMeasuringValuesTable = _OvtxMeasuringValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1)
)
if mibBuilder.loadTexts:
    ovtxMeasuringValuesTable.setStatus("mandatory")
_OvtxMeasuringValuesEntry_Object = MibTableRow
ovtxMeasuringValuesEntry = _OvtxMeasuringValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1)
)
ovtxMeasuringValuesEntry.setIndexNames(
    (0, "BKTEL-HFC862-OVTX-V11-MIB", "ovtxNESlot"),
)
if mibBuilder.loadTexts:
    ovtxMeasuringValuesEntry.setStatus("mandatory")
_OvtxOmiMeasuredLoLo_Type = Integer32
_OvtxOmiMeasuredLoLo_Object = MibTableColumn
ovtxOmiMeasuredLoLo = _OvtxOmiMeasuredLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 1),
    _OvtxOmiMeasuredLoLo_Type()
)
ovtxOmiMeasuredLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxOmiMeasuredLoLo.setStatus("mandatory")
_OvtxOmiMeasuredLo_Type = Integer32
_OvtxOmiMeasuredLo_Object = MibTableColumn
ovtxOmiMeasuredLo = _OvtxOmiMeasuredLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 2),
    _OvtxOmiMeasuredLo_Type()
)
ovtxOmiMeasuredLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxOmiMeasuredLo.setStatus("mandatory")
_OvtxOmiMeasuredValue_Type = Integer32
_OvtxOmiMeasuredValue_Object = MibTableColumn
ovtxOmiMeasuredValue = _OvtxOmiMeasuredValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 3),
    _OvtxOmiMeasuredValue_Type()
)
ovtxOmiMeasuredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxOmiMeasuredValue.setStatus("mandatory")
_OvtxOmiMeasuredHi_Type = Integer32
_OvtxOmiMeasuredHi_Object = MibTableColumn
ovtxOmiMeasuredHi = _OvtxOmiMeasuredHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 4),
    _OvtxOmiMeasuredHi_Type()
)
ovtxOmiMeasuredHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxOmiMeasuredHi.setStatus("mandatory")
_OvtxOmiMeasuredHiHi_Type = Integer32
_OvtxOmiMeasuredHiHi_Object = MibTableColumn
ovtxOmiMeasuredHiHi = _OvtxOmiMeasuredHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 5),
    _OvtxOmiMeasuredHiHi_Type()
)
ovtxOmiMeasuredHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxOmiMeasuredHiHi.setStatus("mandatory")
_OvtxRfGainMeasuredLoLo_Type = Integer32
_OvtxRfGainMeasuredLoLo_Object = MibTableColumn
ovtxRfGainMeasuredLoLo = _OvtxRfGainMeasuredLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 6),
    _OvtxRfGainMeasuredLoLo_Type()
)
ovtxRfGainMeasuredLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxRfGainMeasuredLoLo.setStatus("mandatory")
_OvtxRfGainMeasuredLo_Type = Integer32
_OvtxRfGainMeasuredLo_Object = MibTableColumn
ovtxRfGainMeasuredLo = _OvtxRfGainMeasuredLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 7),
    _OvtxRfGainMeasuredLo_Type()
)
ovtxRfGainMeasuredLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxRfGainMeasuredLo.setStatus("mandatory")
_OvtxRfGainMeasuredValue_Type = Integer32
_OvtxRfGainMeasuredValue_Object = MibTableColumn
ovtxRfGainMeasuredValue = _OvtxRfGainMeasuredValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 8),
    _OvtxRfGainMeasuredValue_Type()
)
ovtxRfGainMeasuredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxRfGainMeasuredValue.setStatus("mandatory")
_OvtxRfGainMeasuredHi_Type = Integer32
_OvtxRfGainMeasuredHi_Object = MibTableColumn
ovtxRfGainMeasuredHi = _OvtxRfGainMeasuredHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 9),
    _OvtxRfGainMeasuredHi_Type()
)
ovtxRfGainMeasuredHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxRfGainMeasuredHi.setStatus("mandatory")
_OvtxRfGainMeasuredHiHi_Type = Integer32
_OvtxRfGainMeasuredHiHi_Object = MibTableColumn
ovtxRfGainMeasuredHiHi = _OvtxRfGainMeasuredHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 10),
    _OvtxRfGainMeasuredHiHi_Type()
)
ovtxRfGainMeasuredHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxRfGainMeasuredHiHi.setStatus("mandatory")
_OvtxLaserCurrentRelLoLo_Type = Integer32
_OvtxLaserCurrentRelLoLo_Object = MibTableColumn
ovtxLaserCurrentRelLoLo = _OvtxLaserCurrentRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 11),
    _OvtxLaserCurrentRelLoLo_Type()
)
ovtxLaserCurrentRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxLaserCurrentRelLoLo.setStatus("mandatory")
_OvtxLaserCurrentRelLo_Type = Integer32
_OvtxLaserCurrentRelLo_Object = MibTableColumn
ovtxLaserCurrentRelLo = _OvtxLaserCurrentRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 12),
    _OvtxLaserCurrentRelLo_Type()
)
ovtxLaserCurrentRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxLaserCurrentRelLo.setStatus("mandatory")
_OvtxLaserCurrentRelValue_Type = Integer32
_OvtxLaserCurrentRelValue_Object = MibTableColumn
ovtxLaserCurrentRelValue = _OvtxLaserCurrentRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 13),
    _OvtxLaserCurrentRelValue_Type()
)
ovtxLaserCurrentRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxLaserCurrentRelValue.setStatus("mandatory")
_OvtxLaserCurrentRelHi_Type = Integer32
_OvtxLaserCurrentRelHi_Object = MibTableColumn
ovtxLaserCurrentRelHi = _OvtxLaserCurrentRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 14),
    _OvtxLaserCurrentRelHi_Type()
)
ovtxLaserCurrentRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxLaserCurrentRelHi.setStatus("mandatory")
_OvtxLaserCurrentRelHiHi_Type = Integer32
_OvtxLaserCurrentRelHiHi_Object = MibTableColumn
ovtxLaserCurrentRelHiHi = _OvtxLaserCurrentRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 15),
    _OvtxLaserCurrentRelHiHi_Type()
)
ovtxLaserCurrentRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxLaserCurrentRelHiHi.setStatus("mandatory")
_OvtxTecCurrentRelLoLo_Type = Integer32
_OvtxTecCurrentRelLoLo_Object = MibTableColumn
ovtxTecCurrentRelLoLo = _OvtxTecCurrentRelLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 16),
    _OvtxTecCurrentRelLoLo_Type()
)
ovtxTecCurrentRelLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTecCurrentRelLoLo.setStatus("mandatory")
_OvtxTecCurrentRelLo_Type = Integer32
_OvtxTecCurrentRelLo_Object = MibTableColumn
ovtxTecCurrentRelLo = _OvtxTecCurrentRelLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 17),
    _OvtxTecCurrentRelLo_Type()
)
ovtxTecCurrentRelLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTecCurrentRelLo.setStatus("mandatory")
_OvtxTecCurrentRelValue_Type = Integer32
_OvtxTecCurrentRelValue_Object = MibTableColumn
ovtxTecCurrentRelValue = _OvtxTecCurrentRelValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 18),
    _OvtxTecCurrentRelValue_Type()
)
ovtxTecCurrentRelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTecCurrentRelValue.setStatus("mandatory")
_OvtxTecCurrentRelHi_Type = Integer32
_OvtxTecCurrentRelHi_Object = MibTableColumn
ovtxTecCurrentRelHi = _OvtxTecCurrentRelHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 19),
    _OvtxTecCurrentRelHi_Type()
)
ovtxTecCurrentRelHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTecCurrentRelHi.setStatus("mandatory")
_OvtxTecCurrentRelHiHi_Type = Integer32
_OvtxTecCurrentRelHiHi_Object = MibTableColumn
ovtxTecCurrentRelHiHi = _OvtxTecCurrentRelHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 20),
    _OvtxTecCurrentRelHiHi_Type()
)
ovtxTecCurrentRelHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTecCurrentRelHiHi.setStatus("mandatory")
_OvtxOutputPowerLoLo_Type = Integer32
_OvtxOutputPowerLoLo_Object = MibTableColumn
ovtxOutputPowerLoLo = _OvtxOutputPowerLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 21),
    _OvtxOutputPowerLoLo_Type()
)
ovtxOutputPowerLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxOutputPowerLoLo.setStatus("mandatory")
_OvtxOutputPowerLo_Type = Integer32
_OvtxOutputPowerLo_Object = MibTableColumn
ovtxOutputPowerLo = _OvtxOutputPowerLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 22),
    _OvtxOutputPowerLo_Type()
)
ovtxOutputPowerLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxOutputPowerLo.setStatus("mandatory")
_OvtxOutputPowerValue_Type = Integer32
_OvtxOutputPowerValue_Object = MibTableColumn
ovtxOutputPowerValue = _OvtxOutputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 23),
    _OvtxOutputPowerValue_Type()
)
ovtxOutputPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxOutputPowerValue.setStatus("mandatory")
_OvtxOutputPowerHi_Type = Integer32
_OvtxOutputPowerHi_Object = MibTableColumn
ovtxOutputPowerHi = _OvtxOutputPowerHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 24),
    _OvtxOutputPowerHi_Type()
)
ovtxOutputPowerHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxOutputPowerHi.setStatus("mandatory")
_OvtxOutputPowerHiHi_Type = Integer32
_OvtxOutputPowerHiHi_Object = MibTableColumn
ovtxOutputPowerHiHi = _OvtxOutputPowerHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 25),
    _OvtxOutputPowerHiHi_Type()
)
ovtxOutputPowerHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxOutputPowerHiHi.setStatus("mandatory")
_OvtxPlus3p3VLoLo_Type = Integer32
_OvtxPlus3p3VLoLo_Object = MibTableColumn
ovtxPlus3p3VLoLo = _OvtxPlus3p3VLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 26),
    _OvtxPlus3p3VLoLo_Type()
)
ovtxPlus3p3VLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus3p3VLoLo.setStatus("mandatory")
_OvtxPlus3p3VLo_Type = Integer32
_OvtxPlus3p3VLo_Object = MibTableColumn
ovtxPlus3p3VLo = _OvtxPlus3p3VLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 27),
    _OvtxPlus3p3VLo_Type()
)
ovtxPlus3p3VLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus3p3VLo.setStatus("mandatory")
_OvtxPlus3p3VValue_Type = Integer32
_OvtxPlus3p3VValue_Object = MibTableColumn
ovtxPlus3p3VValue = _OvtxPlus3p3VValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 28),
    _OvtxPlus3p3VValue_Type()
)
ovtxPlus3p3VValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus3p3VValue.setStatus("mandatory")
_OvtxPlus3p3VHi_Type = Integer32
_OvtxPlus3p3VHi_Object = MibTableColumn
ovtxPlus3p3VHi = _OvtxPlus3p3VHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 29),
    _OvtxPlus3p3VHi_Type()
)
ovtxPlus3p3VHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus3p3VHi.setStatus("mandatory")
_OvtxPlus3p3VHiHi_Type = Integer32
_OvtxPlus3p3VHiHi_Object = MibTableColumn
ovtxPlus3p3VHiHi = _OvtxPlus3p3VHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 30),
    _OvtxPlus3p3VHiHi_Type()
)
ovtxPlus3p3VHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus3p3VHiHi.setStatus("mandatory")
_OvtxPlus5VLoLo_Type = Integer32
_OvtxPlus5VLoLo_Object = MibTableColumn
ovtxPlus5VLoLo = _OvtxPlus5VLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 31),
    _OvtxPlus5VLoLo_Type()
)
ovtxPlus5VLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus5VLoLo.setStatus("mandatory")
_OvtxPlus5VLo_Type = Integer32
_OvtxPlus5VLo_Object = MibTableColumn
ovtxPlus5VLo = _OvtxPlus5VLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 32),
    _OvtxPlus5VLo_Type()
)
ovtxPlus5VLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus5VLo.setStatus("mandatory")
_OvtxPlus5VValue_Type = Integer32
_OvtxPlus5VValue_Object = MibTableColumn
ovtxPlus5VValue = _OvtxPlus5VValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 33),
    _OvtxPlus5VValue_Type()
)
ovtxPlus5VValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus5VValue.setStatus("mandatory")
_OvtxPlus5VHi_Type = Integer32
_OvtxPlus5VHi_Object = MibTableColumn
ovtxPlus5VHi = _OvtxPlus5VHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 34),
    _OvtxPlus5VHi_Type()
)
ovtxPlus5VHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus5VHi.setStatus("mandatory")
_OvtxPlus5VHiHi_Type = Integer32
_OvtxPlus5VHiHi_Object = MibTableColumn
ovtxPlus5VHiHi = _OvtxPlus5VHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 35),
    _OvtxPlus5VHiHi_Type()
)
ovtxPlus5VHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus5VHiHi.setStatus("mandatory")
_OvtxPlus12VLoLo_Type = Integer32
_OvtxPlus12VLoLo_Object = MibTableColumn
ovtxPlus12VLoLo = _OvtxPlus12VLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 36),
    _OvtxPlus12VLoLo_Type()
)
ovtxPlus12VLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus12VLoLo.setStatus("mandatory")
_OvtxPlus12VLo_Type = Integer32
_OvtxPlus12VLo_Object = MibTableColumn
ovtxPlus12VLo = _OvtxPlus12VLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 37),
    _OvtxPlus12VLo_Type()
)
ovtxPlus12VLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus12VLo.setStatus("mandatory")
_OvtxPlus12VValue_Type = Integer32
_OvtxPlus12VValue_Object = MibTableColumn
ovtxPlus12VValue = _OvtxPlus12VValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 38),
    _OvtxPlus12VValue_Type()
)
ovtxPlus12VValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus12VValue.setStatus("mandatory")
_OvtxPlus12VHi_Type = Integer32
_OvtxPlus12VHi_Object = MibTableColumn
ovtxPlus12VHi = _OvtxPlus12VHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 39),
    _OvtxPlus12VHi_Type()
)
ovtxPlus12VHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus12VHi.setStatus("mandatory")
_OvtxPlus12VHiHi_Type = Integer32
_OvtxPlus12VHiHi_Object = MibTableColumn
ovtxPlus12VHiHi = _OvtxPlus12VHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 40),
    _OvtxPlus12VHiHi_Type()
)
ovtxPlus12VHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus12VHiHi.setStatus("mandatory")
_OvtxPlus24VLoLo_Type = Integer32
_OvtxPlus24VLoLo_Object = MibTableColumn
ovtxPlus24VLoLo = _OvtxPlus24VLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 41),
    _OvtxPlus24VLoLo_Type()
)
ovtxPlus24VLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus24VLoLo.setStatus("mandatory")
_OvtxPlus24VLo_Type = Integer32
_OvtxPlus24VLo_Object = MibTableColumn
ovtxPlus24VLo = _OvtxPlus24VLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 42),
    _OvtxPlus24VLo_Type()
)
ovtxPlus24VLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus24VLo.setStatus("mandatory")
_OvtxPlus24VValue_Type = Integer32
_OvtxPlus24VValue_Object = MibTableColumn
ovtxPlus24VValue = _OvtxPlus24VValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 43),
    _OvtxPlus24VValue_Type()
)
ovtxPlus24VValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus24VValue.setStatus("mandatory")
_OvtxPlus24VHi_Type = Integer32
_OvtxPlus24VHi_Object = MibTableColumn
ovtxPlus24VHi = _OvtxPlus24VHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 44),
    _OvtxPlus24VHi_Type()
)
ovtxPlus24VHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus24VHi.setStatus("mandatory")
_OvtxPlus24VHiHi_Type = Integer32
_OvtxPlus24VHiHi_Object = MibTableColumn
ovtxPlus24VHiHi = _OvtxPlus24VHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 45),
    _OvtxPlus24VHiHi_Type()
)
ovtxPlus24VHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxPlus24VHiHi.setStatus("mandatory")
_OvtxMinus5VLoLo_Type = Integer32
_OvtxMinus5VLoLo_Object = MibTableColumn
ovtxMinus5VLoLo = _OvtxMinus5VLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 46),
    _OvtxMinus5VLoLo_Type()
)
ovtxMinus5VLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus5VLoLo.setStatus("mandatory")
_OvtxMinus5VLo_Type = Integer32
_OvtxMinus5VLo_Object = MibTableColumn
ovtxMinus5VLo = _OvtxMinus5VLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 47),
    _OvtxMinus5VLo_Type()
)
ovtxMinus5VLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus5VLo.setStatus("mandatory")
_OvtxMinus5VValue_Type = Integer32
_OvtxMinus5VValue_Object = MibTableColumn
ovtxMinus5VValue = _OvtxMinus5VValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 48),
    _OvtxMinus5VValue_Type()
)
ovtxMinus5VValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus5VValue.setStatus("mandatory")
_OvtxMinus5VHi_Type = Integer32
_OvtxMinus5VHi_Object = MibTableColumn
ovtxMinus5VHi = _OvtxMinus5VHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 49),
    _OvtxMinus5VHi_Type()
)
ovtxMinus5VHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus5VHi.setStatus("mandatory")
_OvtxMinus5VHiHi_Type = Integer32
_OvtxMinus5VHiHi_Object = MibTableColumn
ovtxMinus5VHiHi = _OvtxMinus5VHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 50),
    _OvtxMinus5VHiHi_Type()
)
ovtxMinus5VHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus5VHiHi.setStatus("mandatory")
_OvtxMinus12VLoLo_Type = Integer32
_OvtxMinus12VLoLo_Object = MibTableColumn
ovtxMinus12VLoLo = _OvtxMinus12VLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 51),
    _OvtxMinus12VLoLo_Type()
)
ovtxMinus12VLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus12VLoLo.setStatus("mandatory")
_OvtxMinus12VLo_Type = Integer32
_OvtxMinus12VLo_Object = MibTableColumn
ovtxMinus12VLo = _OvtxMinus12VLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 52),
    _OvtxMinus12VLo_Type()
)
ovtxMinus12VLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus12VLo.setStatus("mandatory")
_OvtxMinus12VValue_Type = Integer32
_OvtxMinus12VValue_Object = MibTableColumn
ovtxMinus12VValue = _OvtxMinus12VValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 53),
    _OvtxMinus12VValue_Type()
)
ovtxMinus12VValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus12VValue.setStatus("mandatory")
_OvtxMinus12VHi_Type = Integer32
_OvtxMinus12VHi_Object = MibTableColumn
ovtxMinus12VHi = _OvtxMinus12VHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 54),
    _OvtxMinus12VHi_Type()
)
ovtxMinus12VHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus12VHi.setStatus("mandatory")
_OvtxMinus12VHiHi_Type = Integer32
_OvtxMinus12VHiHi_Object = MibTableColumn
ovtxMinus12VHiHi = _OvtxMinus12VHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 55),
    _OvtxMinus12VHiHi_Type()
)
ovtxMinus12VHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxMinus12VHiHi.setStatus("mandatory")
_OvtxTemperatureLoLo_Type = Integer32
_OvtxTemperatureLoLo_Object = MibTableColumn
ovtxTemperatureLoLo = _OvtxTemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 56),
    _OvtxTemperatureLoLo_Type()
)
ovtxTemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTemperatureLoLo.setStatus("mandatory")
_OvtxTemperatureLo_Type = Integer32
_OvtxTemperatureLo_Object = MibTableColumn
ovtxTemperatureLo = _OvtxTemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 57),
    _OvtxTemperatureLo_Type()
)
ovtxTemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTemperatureLo.setStatus("mandatory")
_OvtxTemperatureValue_Type = Integer32
_OvtxTemperatureValue_Object = MibTableColumn
ovtxTemperatureValue = _OvtxTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 58),
    _OvtxTemperatureValue_Type()
)
ovtxTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTemperatureValue.setStatus("mandatory")
_OvtxTemperatureHi_Type = Integer32
_OvtxTemperatureHi_Object = MibTableColumn
ovtxTemperatureHi = _OvtxTemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 59),
    _OvtxTemperatureHi_Type()
)
ovtxTemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTemperatureHi.setStatus("mandatory")
_OvtxTemperatureHiHi_Type = Integer32
_OvtxTemperatureHiHi_Object = MibTableColumn
ovtxTemperatureHiHi = _OvtxTemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 60),
    _OvtxTemperatureHiHi_Type()
)
ovtxTemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxTemperatureHiHi.setStatus("mandatory")
_OvtxRfInputLoLo_Type = Integer32
_OvtxRfInputLoLo_Object = MibTableColumn
ovtxRfInputLoLo = _OvtxRfInputLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 61),
    _OvtxRfInputLoLo_Type()
)
ovtxRfInputLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxRfInputLoLo.setStatus("mandatory")
_OvtxRfInputLo_Type = Integer32
_OvtxRfInputLo_Object = MibTableColumn
ovtxRfInputLo = _OvtxRfInputLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 62),
    _OvtxRfInputLo_Type()
)
ovtxRfInputLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxRfInputLo.setStatus("mandatory")
_OvtxRfInputValue_Type = Integer32
_OvtxRfInputValue_Object = MibTableColumn
ovtxRfInputValue = _OvtxRfInputValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 63),
    _OvtxRfInputValue_Type()
)
ovtxRfInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxRfInputValue.setStatus("mandatory")
_OvtxRfInputHi_Type = Integer32
_OvtxRfInputHi_Object = MibTableColumn
ovtxRfInputHi = _OvtxRfInputHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 64),
    _OvtxRfInputHi_Type()
)
ovtxRfInputHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxRfInputHi.setStatus("mandatory")
_OvtxRfInputHiHi_Type = Integer32
_OvtxRfInputHiHi_Object = MibTableColumn
ovtxRfInputHiHi = _OvtxRfInputHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 65),
    _OvtxRfInputHiHi_Type()
)
ovtxRfInputHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxRfInputHiHi.setStatus("mandatory")
_OvtxSatRfInputLoLo_Type = Integer32
_OvtxSatRfInputLoLo_Object = MibTableColumn
ovtxSatRfInputLoLo = _OvtxSatRfInputLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 66),
    _OvtxSatRfInputLoLo_Type()
)
ovtxSatRfInputLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatRfInputLoLo.setStatus("mandatory")
_OvtxSatRfInputLo_Type = Integer32
_OvtxSatRfInputLo_Object = MibTableColumn
ovtxSatRfInputLo = _OvtxSatRfInputLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 67),
    _OvtxSatRfInputLo_Type()
)
ovtxSatRfInputLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatRfInputLo.setStatus("mandatory")
_OvtxSatRfInputValue_Type = Integer32
_OvtxSatRfInputValue_Object = MibTableColumn
ovtxSatRfInputValue = _OvtxSatRfInputValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 68),
    _OvtxSatRfInputValue_Type()
)
ovtxSatRfInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxSatRfInputValue.setStatus("mandatory")
_OvtxSatRfInputHi_Type = Integer32
_OvtxSatRfInputHi_Object = MibTableColumn
ovtxSatRfInputHi = _OvtxSatRfInputHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 69),
    _OvtxSatRfInputHi_Type()
)
ovtxSatRfInputHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatRfInputHi.setStatus("mandatory")
_OvtxSatRfInputHiHi_Type = Integer32
_OvtxSatRfInputHiHi_Object = MibTableColumn
ovtxSatRfInputHiHi = _OvtxSatRfInputHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 70),
    _OvtxSatRfInputHiHi_Type()
)
ovtxSatRfInputHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatRfInputHiHi.setStatus("mandatory")
_OvtxSatOmiMeasuredLoLo_Type = Integer32
_OvtxSatOmiMeasuredLoLo_Object = MibTableColumn
ovtxSatOmiMeasuredLoLo = _OvtxSatOmiMeasuredLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 71),
    _OvtxSatOmiMeasuredLoLo_Type()
)
ovtxSatOmiMeasuredLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatOmiMeasuredLoLo.setStatus("mandatory")
_OvtxSatOmiMeasuredLo_Type = Integer32
_OvtxSatOmiMeasuredLo_Object = MibTableColumn
ovtxSatOmiMeasuredLo = _OvtxSatOmiMeasuredLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 72),
    _OvtxSatOmiMeasuredLo_Type()
)
ovtxSatOmiMeasuredLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatOmiMeasuredLo.setStatus("mandatory")
_OvtxSatOmiMeasuredValue_Type = Integer32
_OvtxSatOmiMeasuredValue_Object = MibTableColumn
ovtxSatOmiMeasuredValue = _OvtxSatOmiMeasuredValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 73),
    _OvtxSatOmiMeasuredValue_Type()
)
ovtxSatOmiMeasuredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxSatOmiMeasuredValue.setStatus("mandatory")
_OvtxSatOmiMeasuredHi_Type = Integer32
_OvtxSatOmiMeasuredHi_Object = MibTableColumn
ovtxSatOmiMeasuredHi = _OvtxSatOmiMeasuredHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 74),
    _OvtxSatOmiMeasuredHi_Type()
)
ovtxSatOmiMeasuredHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatOmiMeasuredHi.setStatus("mandatory")
_OvtxSatOmiMeasuredHiHi_Type = Integer32
_OvtxSatOmiMeasuredHiHi_Object = MibTableColumn
ovtxSatOmiMeasuredHiHi = _OvtxSatOmiMeasuredHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 75),
    _OvtxSatOmiMeasuredHiHi_Type()
)
ovtxSatOmiMeasuredHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatOmiMeasuredHiHi.setStatus("mandatory")
_OvtxSatRfGainMeasuredLoLo_Type = Integer32
_OvtxSatRfGainMeasuredLoLo_Object = MibTableColumn
ovtxSatRfGainMeasuredLoLo = _OvtxSatRfGainMeasuredLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 76),
    _OvtxSatRfGainMeasuredLoLo_Type()
)
ovtxSatRfGainMeasuredLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatRfGainMeasuredLoLo.setStatus("mandatory")
_OvtxSatRfGainMeasuredLo_Type = Integer32
_OvtxSatRfGainMeasuredLo_Object = MibTableColumn
ovtxSatRfGainMeasuredLo = _OvtxSatRfGainMeasuredLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 77),
    _OvtxSatRfGainMeasuredLo_Type()
)
ovtxSatRfGainMeasuredLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatRfGainMeasuredLo.setStatus("mandatory")
_OvtxSatRfGainMeasuredValue_Type = Integer32
_OvtxSatRfGainMeasuredValue_Object = MibTableColumn
ovtxSatRfGainMeasuredValue = _OvtxSatRfGainMeasuredValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 78),
    _OvtxSatRfGainMeasuredValue_Type()
)
ovtxSatRfGainMeasuredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxSatRfGainMeasuredValue.setStatus("mandatory")
_OvtxSatRfGainMeasuredHi_Type = Integer32
_OvtxSatRfGainMeasuredHi_Object = MibTableColumn
ovtxSatRfGainMeasuredHi = _OvtxSatRfGainMeasuredHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 79),
    _OvtxSatRfGainMeasuredHi_Type()
)
ovtxSatRfGainMeasuredHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatRfGainMeasuredHi.setStatus("mandatory")
_OvtxSatRfGainMeasuredHiHi_Type = Integer32
_OvtxSatRfGainMeasuredHiHi_Object = MibTableColumn
ovtxSatRfGainMeasuredHiHi = _OvtxSatRfGainMeasuredHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 5, 1, 1, 80),
    _OvtxSatRfGainMeasuredHiHi_Type()
)
ovtxSatRfGainMeasuredHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovtxSatRfGainMeasuredHiHi.setStatus("mandatory")
_OvtxDisplay_ObjectIdentity = ObjectIdentity
ovtxDisplay = _OvtxDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6)
)
_OvtxDisplayTable_Object = MibTable
ovtxDisplayTable = _OvtxDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1)
)
if mibBuilder.loadTexts:
    ovtxDisplayTable.setStatus("mandatory")
_OvtxDisplayEntry_Object = MibTableRow
ovtxDisplayEntry = _OvtxDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1)
)
ovtxDisplayEntry.setIndexNames(
    (0, "BKTEL-HFC862-OVTX-V11-MIB", "ovtxNESlot"),
)
if mibBuilder.loadTexts:
    ovtxDisplayEntry.setStatus("mandatory")
_OvtxDisplayRfInputValue_Type = Integer32
_OvtxDisplayRfInputValue_Object = MibTableColumn
ovtxDisplayRfInputValue = _OvtxDisplayRfInputValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 1),
    _OvtxDisplayRfInputValue_Type()
)
ovtxDisplayRfInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplayRfInputValue.setStatus("mandatory")
_OvtxDisplayLaserFrequencyMin_Type = Integer32
_OvtxDisplayLaserFrequencyMin_Object = MibTableColumn
ovtxDisplayLaserFrequencyMin = _OvtxDisplayLaserFrequencyMin_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 2),
    _OvtxDisplayLaserFrequencyMin_Type()
)
ovtxDisplayLaserFrequencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplayLaserFrequencyMin.setStatus("mandatory")
_OvtxDisplayLaserFrequencyMax_Type = Integer32
_OvtxDisplayLaserFrequencyMax_Object = MibTableColumn
ovtxDisplayLaserFrequencyMax = _OvtxDisplayLaserFrequencyMax_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 3),
    _OvtxDisplayLaserFrequencyMax_Type()
)
ovtxDisplayLaserFrequencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplayLaserFrequencyMax.setStatus("mandatory")
_OvtxDisplayLaserFrequencyStep_Type = Integer32
_OvtxDisplayLaserFrequencyStep_Object = MibTableColumn
ovtxDisplayLaserFrequencyStep = _OvtxDisplayLaserFrequencyStep_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 4),
    _OvtxDisplayLaserFrequencyStep_Type()
)
ovtxDisplayLaserFrequencyStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplayLaserFrequencyStep.setStatus("mandatory")
_OvtxDisplayOmiNominal_Type = Integer32
_OvtxDisplayOmiNominal_Object = MibTableColumn
ovtxDisplayOmiNominal = _OvtxDisplayOmiNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 5),
    _OvtxDisplayOmiNominal_Type()
)
ovtxDisplayOmiNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplayOmiNominal.setStatus("mandatory")
_OvtxDisplaySatOmiNominal_Type = Integer32
_OvtxDisplaySatOmiNominal_Object = MibTableColumn
ovtxDisplaySatOmiNominal = _OvtxDisplaySatOmiNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 6),
    _OvtxDisplaySatOmiNominal_Type()
)
ovtxDisplaySatOmiNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplaySatOmiNominal.setStatus("mandatory")
_OvtxDisplayRegulationState_Type = RegulationState
_OvtxDisplayRegulationState_Object = MibTableColumn
ovtxDisplayRegulationState = _OvtxDisplayRegulationState_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 7),
    _OvtxDisplayRegulationState_Type()
)
ovtxDisplayRegulationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplayRegulationState.setStatus("mandatory")
_OvtxDisplayExtendedCapabilities_Type = TruthValue
_OvtxDisplayExtendedCapabilities_Object = MibTableColumn
ovtxDisplayExtendedCapabilities = _OvtxDisplayExtendedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 8),
    _OvtxDisplayExtendedCapabilities_Type()
)
ovtxDisplayExtendedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplayExtendedCapabilities.setStatus("mandatory")
_OvtxDisplayRfInputCapabilities_Type = RfInputCapabilities
_OvtxDisplayRfInputCapabilities_Object = MibTableColumn
ovtxDisplayRfInputCapabilities = _OvtxDisplayRfInputCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 9),
    _OvtxDisplayRfInputCapabilities_Type()
)
ovtxDisplayRfInputCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplayRfInputCapabilities.setStatus("mandatory")
_OvtxDisplaySatLnbSupplySupported_Type = LnbSupplySupportedValue
_OvtxDisplaySatLnbSupplySupported_Object = MibTableColumn
ovtxDisplaySatLnbSupplySupported = _OvtxDisplaySatLnbSupplySupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 10),
    _OvtxDisplaySatLnbSupplySupported_Type()
)
ovtxDisplaySatLnbSupplySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplaySatLnbSupplySupported.setStatus("mandatory")
_OvtxDisplaySbsExtensionsSupported_Type = TruthValue
_OvtxDisplaySbsExtensionsSupported_Object = MibTableColumn
ovtxDisplaySbsExtensionsSupported = _OvtxDisplaySbsExtensionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 11),
    _OvtxDisplaySbsExtensionsSupported_Type()
)
ovtxDisplaySbsExtensionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplaySbsExtensionsSupported.setStatus("mandatory")
_OvtxDisplaySbsSuppressionModeSupported_Type = TruthValue
_OvtxDisplaySbsSuppressionModeSupported_Object = MibTableColumn
ovtxDisplaySbsSuppressionModeSupported = _OvtxDisplaySbsSuppressionModeSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 12),
    _OvtxDisplaySbsSuppressionModeSupported_Type()
)
ovtxDisplaySbsSuppressionModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplaySbsSuppressionModeSupported.setStatus("mandatory")
_OvtxDisplaySbsFiberParametersSupported_Type = TruthValue
_OvtxDisplaySbsFiberParametersSupported_Object = MibTableColumn
ovtxDisplaySbsFiberParametersSupported = _OvtxDisplaySbsFiberParametersSupported_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 101, 6, 1, 1, 13),
    _OvtxDisplaySbsFiberParametersSupported_Type()
)
ovtxDisplaySbsFiberParametersSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovtxDisplaySbsFiberParametersSupported.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BKTEL-HFC862-OVTX-V11-MIB",
    **{"AGCmode": AGCmode,
       "SatAGCmode": SatAGCmode,
       "RedundancyMode": RedundancyMode,
       "RedundancyMask": RedundancyMask,
       "LaserOutputMode": LaserOutputMode,
       "CsoRegulationMode": CsoRegulationMode,
       "RegulationState": RegulationState,
       "RfInputCapabilities": RfInputCapabilities,
       "RfInputAlarmMode": RfInputAlarmMode,
       "LnbSupplyValue": LnbSupplyValue,
       "LnbSupplySupportedValue": LnbSupplySupportedValue,
       "SbsSuppressionModeValue": SbsSuppressionModeValue,
       "SbsFiberTypeValue": SbsFiberTypeValue,
       "SbsFiberLengthValue": SbsFiberLengthValue,
       "NESlotWriteValue": NESlotWriteValue,
       "ovtx": ovtx,
       "ovtxCommon": ovtxCommon,
       "ovtxCommonNumberOfModules": ovtxCommonNumberOfModules,
       "ovtxCommonTable": ovtxCommonTable,
       "ovtxCommonEntry": ovtxCommonEntry,
       "ovtxNESlot": ovtxNESlot,
       "ovtxCommonType": ovtxCommonType,
       "ovtxCommonDescr": ovtxCommonDescr,
       "ovtxCommonFirmwareId": ovtxCommonFirmwareId,
       "ovtxCommonModuleWidth": ovtxCommonModuleWidth,
       "ovtxStates": ovtxStates,
       "ovtxStatesTable": ovtxStatesTable,
       "ovtxStatesEntry": ovtxStatesEntry,
       "ovtxStatesOutputLow": ovtxStatesOutputLow,
       "ovtxStatesOutputHigh": ovtxStatesOutputHigh,
       "ovtxStatesInputLow": ovtxStatesInputLow,
       "ovtxStatesLaserAging": ovtxStatesLaserAging,
       "ovtxStatesTecHigh": ovtxStatesTecHigh,
       "ovtxStatesLaserTempLow": ovtxStatesLaserTempLow,
       "ovtxStatesLaserTempHigh": ovtxStatesLaserTempHigh,
       "ovtxStatesOmiOrRfgainLow": ovtxStatesOmiOrRfgainLow,
       "ovtxStatesOmiOrRfgainHigh": ovtxStatesOmiOrRfgainHigh,
       "ovtxStatesPowerSupplyLeft": ovtxStatesPowerSupplyLeft,
       "ovtxStatesPowerSupplyRight": ovtxStatesPowerSupplyRight,
       "ovtxStatesFanLeft": ovtxStatesFanLeft,
       "ovtxStatesFanRight": ovtxStatesFanRight,
       "ovtxStatesTemperatureLow": ovtxStatesTemperatureLow,
       "ovtxStatesTemperatureHigh": ovtxStatesTemperatureHigh,
       "ovtxStatesPlus3p3VLow": ovtxStatesPlus3p3VLow,
       "ovtxStatesPlus3p3VHigh": ovtxStatesPlus3p3VHigh,
       "ovtxStatesPlus5VLow": ovtxStatesPlus5VLow,
       "ovtxStatesPlus5VHigh": ovtxStatesPlus5VHigh,
       "ovtxStatesPlus12VLow": ovtxStatesPlus12VLow,
       "ovtxStatesPlus12VHigh": ovtxStatesPlus12VHigh,
       "ovtxStatesPlus24VLow": ovtxStatesPlus24VLow,
       "ovtxStatesPlus24VHigh": ovtxStatesPlus24VHigh,
       "ovtxStatesMinus5VLow": ovtxStatesMinus5VLow,
       "ovtxStatesMinus5VHigh": ovtxStatesMinus5VHigh,
       "ovtxStatesMinus12VLow": ovtxStatesMinus12VLow,
       "ovtxStatesMinus12VHigh": ovtxStatesMinus12VHigh,
       "ovtxStatesLaserShutdown": ovtxStatesLaserShutdown,
       "ovtxStatesInitializing": ovtxStatesInitializing,
       "ovtxStatesBootloader": ovtxStatesBootloader,
       "ovtxStatesCommLoss": ovtxStatesCommLoss,
       "ovtxStatesInputHigh": ovtxStatesInputHigh,
       "ovtxStatesRedundancySwitch": ovtxStatesRedundancySwitch,
       "ovtxStatesSatInputLow": ovtxStatesSatInputLow,
       "ovtxStatesSatInputHigh": ovtxStatesSatInputHigh,
       "ovtxStatesSatOmiOrRfgainLow": ovtxStatesSatOmiOrRfgainLow,
       "ovtxStatesSatOmiOrRfgainHigh": ovtxStatesSatOmiOrRfgainHigh,
       "ovtxStatesSatLnbShortCircuit": ovtxStatesSatLnbShortCircuit,
       "ovtxStatesSbs1Level": ovtxStatesSbs1Level,
       "ovtxStatesSbs2Level": ovtxStatesSbs2Level,
       "ovtxStatesSbs1PllNotLocked": ovtxStatesSbs1PllNotLocked,
       "ovtxStatesSbs2PllNotLocked": ovtxStatesSbs2PllNotLocked,
       "ovtxStatesInternalAlarm": ovtxStatesInternalAlarm,
       "ovtxConfiguration": ovtxConfiguration,
       "ovtxConfigurationTable": ovtxConfigurationTable,
       "ovtxConfigurationEntry": ovtxConfigurationEntry,
       "ovtxConfigurationNESlotWrite": ovtxConfigurationNESlotWrite,
       "ovtxConfigurationModeAGC": ovtxConfigurationModeAGC,
       "ovtxConfigurationOmi": ovtxConfigurationOmi,
       "ovtxConfigurationRfGain": ovtxConfigurationRfGain,
       "ovtxConfigurationSbsSuppression": ovtxConfigurationSbsSuppression,
       "ovtxConfigurationChannelDistance": ovtxConfigurationChannelDistance,
       "ovtxConfigurationLaserFrequency": ovtxConfigurationLaserFrequency,
       "ovtxConfigurationRfInputLimitLoLo": ovtxConfigurationRfInputLimitLoLo,
       "ovtxConfigurationRfInputLimitLo": ovtxConfigurationRfInputLimitLo,
       "ovtxConfigurationRfInputLimitHi": ovtxConfigurationRfInputLimitHi,
       "ovtxConfigurationRfInputLimitHiHi": ovtxConfigurationRfInputLimitHiHi,
       "ovtxConfigurationRfGainMeasuredLimitLoLo": ovtxConfigurationRfGainMeasuredLimitLoLo,
       "ovtxConfigurationRfGainMeasuredLimitLo": ovtxConfigurationRfGainMeasuredLimitLo,
       "ovtxConfigurationRfGainMeasuredLimitHi": ovtxConfigurationRfGainMeasuredLimitHi,
       "ovtxConfigurationRfGainMeasuredLimitHiHi": ovtxConfigurationRfGainMeasuredLimitHiHi,
       "ovtxConfigurationOmiMeasuredLimitLoLo": ovtxConfigurationOmiMeasuredLimitLoLo,
       "ovtxConfigurationOmiMeasuredLimitLo": ovtxConfigurationOmiMeasuredLimitLo,
       "ovtxConfigurationOmiMeasuredLimitHi": ovtxConfigurationOmiMeasuredLimitHi,
       "ovtxConfigurationOmiMeasuredLimitHiHi": ovtxConfigurationOmiMeasuredLimitHiHi,
       "ovtxConfigurationOutputPwrLimitLoLo": ovtxConfigurationOutputPwrLimitLoLo,
       "ovtxConfigurationOutputPwrLimitLo": ovtxConfigurationOutputPwrLimitLo,
       "ovtxConfigurationOutputPwrLimitHi": ovtxConfigurationOutputPwrLimitHi,
       "ovtxConfigurationOutputPwrLimitHiHi": ovtxConfigurationOutputPwrLimitHiHi,
       "ovtxConfigurationRedundancyMode": ovtxConfigurationRedundancyMode,
       "ovtxConfigurationRedundancyMask": ovtxConfigurationRedundancyMask,
       "ovtxConfigurationCsoRegulationMode": ovtxConfigurationCsoRegulationMode,
       "ovtxConfigurationSlope": ovtxConfigurationSlope,
       "ovtxConfigurationFiberLength": ovtxConfigurationFiberLength,
       "ovtxConfigurationSatModeAGC": ovtxConfigurationSatModeAGC,
       "ovtxConfigurationSatOmi": ovtxConfigurationSatOmi,
       "ovtxConfigurationSatRfGain": ovtxConfigurationSatRfGain,
       "ovtxConfigurationSatSlope": ovtxConfigurationSatSlope,
       "ovtxConfigurationRfInputAlarmMode": ovtxConfigurationRfInputAlarmMode,
       "ovtxConfigurationSatLnbSupply": ovtxConfigurationSatLnbSupply,
       "ovtxConfigurationSbsSuppressionMode": ovtxConfigurationSbsSuppressionMode,
       "ovtxConfigurationSbsFiberType": ovtxConfigurationSbsFiberType,
       "ovtxConfigurationSbsFiberLength": ovtxConfigurationSbsFiberLength,
       "ovtxControl": ovtxControl,
       "ovtxControlTable": ovtxControlTable,
       "ovtxControlEntry": ovtxControlEntry,
       "ovtxControlLaserOutputMode": ovtxControlLaserOutputMode,
       "ovtxControlReset": ovtxControlReset,
       "ovtxControlModuleLedBlink": ovtxControlModuleLedBlink,
       "ovtxMeasuringValues": ovtxMeasuringValues,
       "ovtxMeasuringValuesTable": ovtxMeasuringValuesTable,
       "ovtxMeasuringValuesEntry": ovtxMeasuringValuesEntry,
       "ovtxOmiMeasuredLoLo": ovtxOmiMeasuredLoLo,
       "ovtxOmiMeasuredLo": ovtxOmiMeasuredLo,
       "ovtxOmiMeasuredValue": ovtxOmiMeasuredValue,
       "ovtxOmiMeasuredHi": ovtxOmiMeasuredHi,
       "ovtxOmiMeasuredHiHi": ovtxOmiMeasuredHiHi,
       "ovtxRfGainMeasuredLoLo": ovtxRfGainMeasuredLoLo,
       "ovtxRfGainMeasuredLo": ovtxRfGainMeasuredLo,
       "ovtxRfGainMeasuredValue": ovtxRfGainMeasuredValue,
       "ovtxRfGainMeasuredHi": ovtxRfGainMeasuredHi,
       "ovtxRfGainMeasuredHiHi": ovtxRfGainMeasuredHiHi,
       "ovtxLaserCurrentRelLoLo": ovtxLaserCurrentRelLoLo,
       "ovtxLaserCurrentRelLo": ovtxLaserCurrentRelLo,
       "ovtxLaserCurrentRelValue": ovtxLaserCurrentRelValue,
       "ovtxLaserCurrentRelHi": ovtxLaserCurrentRelHi,
       "ovtxLaserCurrentRelHiHi": ovtxLaserCurrentRelHiHi,
       "ovtxTecCurrentRelLoLo": ovtxTecCurrentRelLoLo,
       "ovtxTecCurrentRelLo": ovtxTecCurrentRelLo,
       "ovtxTecCurrentRelValue": ovtxTecCurrentRelValue,
       "ovtxTecCurrentRelHi": ovtxTecCurrentRelHi,
       "ovtxTecCurrentRelHiHi": ovtxTecCurrentRelHiHi,
       "ovtxOutputPowerLoLo": ovtxOutputPowerLoLo,
       "ovtxOutputPowerLo": ovtxOutputPowerLo,
       "ovtxOutputPowerValue": ovtxOutputPowerValue,
       "ovtxOutputPowerHi": ovtxOutputPowerHi,
       "ovtxOutputPowerHiHi": ovtxOutputPowerHiHi,
       "ovtxPlus3p3VLoLo": ovtxPlus3p3VLoLo,
       "ovtxPlus3p3VLo": ovtxPlus3p3VLo,
       "ovtxPlus3p3VValue": ovtxPlus3p3VValue,
       "ovtxPlus3p3VHi": ovtxPlus3p3VHi,
       "ovtxPlus3p3VHiHi": ovtxPlus3p3VHiHi,
       "ovtxPlus5VLoLo": ovtxPlus5VLoLo,
       "ovtxPlus5VLo": ovtxPlus5VLo,
       "ovtxPlus5VValue": ovtxPlus5VValue,
       "ovtxPlus5VHi": ovtxPlus5VHi,
       "ovtxPlus5VHiHi": ovtxPlus5VHiHi,
       "ovtxPlus12VLoLo": ovtxPlus12VLoLo,
       "ovtxPlus12VLo": ovtxPlus12VLo,
       "ovtxPlus12VValue": ovtxPlus12VValue,
       "ovtxPlus12VHi": ovtxPlus12VHi,
       "ovtxPlus12VHiHi": ovtxPlus12VHiHi,
       "ovtxPlus24VLoLo": ovtxPlus24VLoLo,
       "ovtxPlus24VLo": ovtxPlus24VLo,
       "ovtxPlus24VValue": ovtxPlus24VValue,
       "ovtxPlus24VHi": ovtxPlus24VHi,
       "ovtxPlus24VHiHi": ovtxPlus24VHiHi,
       "ovtxMinus5VLoLo": ovtxMinus5VLoLo,
       "ovtxMinus5VLo": ovtxMinus5VLo,
       "ovtxMinus5VValue": ovtxMinus5VValue,
       "ovtxMinus5VHi": ovtxMinus5VHi,
       "ovtxMinus5VHiHi": ovtxMinus5VHiHi,
       "ovtxMinus12VLoLo": ovtxMinus12VLoLo,
       "ovtxMinus12VLo": ovtxMinus12VLo,
       "ovtxMinus12VValue": ovtxMinus12VValue,
       "ovtxMinus12VHi": ovtxMinus12VHi,
       "ovtxMinus12VHiHi": ovtxMinus12VHiHi,
       "ovtxTemperatureLoLo": ovtxTemperatureLoLo,
       "ovtxTemperatureLo": ovtxTemperatureLo,
       "ovtxTemperatureValue": ovtxTemperatureValue,
       "ovtxTemperatureHi": ovtxTemperatureHi,
       "ovtxTemperatureHiHi": ovtxTemperatureHiHi,
       "ovtxRfInputLoLo": ovtxRfInputLoLo,
       "ovtxRfInputLo": ovtxRfInputLo,
       "ovtxRfInputValue": ovtxRfInputValue,
       "ovtxRfInputHi": ovtxRfInputHi,
       "ovtxRfInputHiHi": ovtxRfInputHiHi,
       "ovtxSatRfInputLoLo": ovtxSatRfInputLoLo,
       "ovtxSatRfInputLo": ovtxSatRfInputLo,
       "ovtxSatRfInputValue": ovtxSatRfInputValue,
       "ovtxSatRfInputHi": ovtxSatRfInputHi,
       "ovtxSatRfInputHiHi": ovtxSatRfInputHiHi,
       "ovtxSatOmiMeasuredLoLo": ovtxSatOmiMeasuredLoLo,
       "ovtxSatOmiMeasuredLo": ovtxSatOmiMeasuredLo,
       "ovtxSatOmiMeasuredValue": ovtxSatOmiMeasuredValue,
       "ovtxSatOmiMeasuredHi": ovtxSatOmiMeasuredHi,
       "ovtxSatOmiMeasuredHiHi": ovtxSatOmiMeasuredHiHi,
       "ovtxSatRfGainMeasuredLoLo": ovtxSatRfGainMeasuredLoLo,
       "ovtxSatRfGainMeasuredLo": ovtxSatRfGainMeasuredLo,
       "ovtxSatRfGainMeasuredValue": ovtxSatRfGainMeasuredValue,
       "ovtxSatRfGainMeasuredHi": ovtxSatRfGainMeasuredHi,
       "ovtxSatRfGainMeasuredHiHi": ovtxSatRfGainMeasuredHiHi,
       "ovtxDisplay": ovtxDisplay,
       "ovtxDisplayTable": ovtxDisplayTable,
       "ovtxDisplayEntry": ovtxDisplayEntry,
       "ovtxDisplayRfInputValue": ovtxDisplayRfInputValue,
       "ovtxDisplayLaserFrequencyMin": ovtxDisplayLaserFrequencyMin,
       "ovtxDisplayLaserFrequencyMax": ovtxDisplayLaserFrequencyMax,
       "ovtxDisplayLaserFrequencyStep": ovtxDisplayLaserFrequencyStep,
       "ovtxDisplayOmiNominal": ovtxDisplayOmiNominal,
       "ovtxDisplaySatOmiNominal": ovtxDisplaySatOmiNominal,
       "ovtxDisplayRegulationState": ovtxDisplayRegulationState,
       "ovtxDisplayExtendedCapabilities": ovtxDisplayExtendedCapabilities,
       "ovtxDisplayRfInputCapabilities": ovtxDisplayRfInputCapabilities,
       "ovtxDisplaySatLnbSupplySupported": ovtxDisplaySatLnbSupplySupported,
       "ovtxDisplaySbsExtensionsSupported": ovtxDisplaySbsExtensionsSupported,
       "ovtxDisplaySbsSuppressionModeSupported": ovtxDisplaySbsSuppressionModeSupported,
       "ovtxDisplaySbsFiberParametersSupported": ovtxDisplaySbsFiberParametersSupported}
)
