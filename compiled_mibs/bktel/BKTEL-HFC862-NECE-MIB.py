# SNMP MIB module (BKTEL-HFC862-NECE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bktel\BKTEL-HFC862-NECE-MIB

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



class GpioType(Integer32):
    """Custom type GpioType based on Integer32"""
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
        *(("gpioTypeNotSupported", 1),
          ("gpioTypeInputOnly", 2),
          ("gpioTypeInputOrOutput", 3),
          ("gpioTypeOutputOnly", 4))
    )





class GpioMode(Integer32):
    """Custom type GpioMode based on Integer32"""
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
        *(("gpioModeInput", 1),
          ("gpioModeInputIsNotify", 2),
          ("gpioModeInputIsWarning", 3),
          ("gpioModeInputIsAlarm", 4),
          ("gpioModeOutputOnAnyAlarm", 5),
          ("gpioModeOutputOnAnyWarning", 6))
    )





class GpioLogicLevel(Integer32):
    """Custom type GpioLogicLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gpioLevelActiveHigh", 1),
          ("gpioLevelActiveLow", 2))
    )





class HmsTrapsComplianceValue(Integer32):
    """Custom type HmsTrapsComplianceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullCompliant", 1),
          ("minorCompliant", 2))
    )





class HfcInventoryFormatValue(Integer32):
    """Custom type HfcInventoryFormatValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("format_DKS_T12_9", 1),
          ("format_T_Nova_E531i", 2))
    )





class TrapVerifyTimeoutValue(Integer32):
    """Custom type TrapVerifyTimeoutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )





class TrapAccumulationTimeValue(Integer32):
    """Custom type TrapAccumulationTimeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )





class NESlotWriteValue(Integer32):
    """Custom type NESlotWriteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nece_ObjectIdentity = ObjectIdentity
nece = _Nece_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100)
)
_NeceCommon_ObjectIdentity = ObjectIdentity
neceCommon = _NeceCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1)
)
_NeceCommonNumberOfModules_Type = Integer32
_NeceCommonNumberOfModules_Object = MibScalar
neceCommonNumberOfModules = _NeceCommonNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 1),
    _NeceCommonNumberOfModules_Type()
)
neceCommonNumberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceCommonNumberOfModules.setStatus("mandatory")
_NeceCommonTable_Object = MibTable
neceCommonTable = _NeceCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2)
)
if mibBuilder.loadTexts:
    neceCommonTable.setStatus("mandatory")
_NeceCommonEntry_Object = MibTableRow
neceCommonEntry = _NeceCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1)
)
neceCommonEntry.setIndexNames(
    (0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"),
)
if mibBuilder.loadTexts:
    neceCommonEntry.setStatus("mandatory")
_NeceNESlot_Type = NESlotValue
_NeceNESlot_Object = MibTableColumn
neceNESlot = _NeceNESlot_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 1),
    _NeceNESlot_Type()
)
neceNESlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceNESlot.setStatus("mandatory")


class _NeceCommonType_Type(DisplayString):
    """Custom type neceCommonType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NeceCommonType_Type.__name__ = "DisplayString"
_NeceCommonType_Object = MibTableColumn
neceCommonType = _NeceCommonType_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 2),
    _NeceCommonType_Type()
)
neceCommonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceCommonType.setStatus("mandatory")
_NeceCommonDescr_Type = DisplayString
_NeceCommonDescr_Object = MibTableColumn
neceCommonDescr = _NeceCommonDescr_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 3),
    _NeceCommonDescr_Type()
)
neceCommonDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceCommonDescr.setStatus("mandatory")


class _NeceCommonFirmwareId_Type(DisplayString):
    """Custom type neceCommonFirmwareId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NeceCommonFirmwareId_Type.__name__ = "DisplayString"
_NeceCommonFirmwareId_Object = MibTableColumn
neceCommonFirmwareId = _NeceCommonFirmwareId_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 4),
    _NeceCommonFirmwareId_Type()
)
neceCommonFirmwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceCommonFirmwareId.setStatus("mandatory")
_NeceCommonModuleWidth_Type = ModuleWidthValue
_NeceCommonModuleWidth_Object = MibTableColumn
neceCommonModuleWidth = _NeceCommonModuleWidth_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 5),
    _NeceCommonModuleWidth_Type()
)
neceCommonModuleWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceCommonModuleWidth.setStatus("optional")
_NeceStates_ObjectIdentity = ObjectIdentity
neceStates = _NeceStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2)
)
_NeceStatesTable_Object = MibTable
neceStatesTable = _NeceStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1)
)
if mibBuilder.loadTexts:
    neceStatesTable.setStatus("mandatory")
_NeceStatesEntry_Object = MibTableRow
neceStatesEntry = _NeceStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1)
)
neceStatesEntry.setIndexNames(
    (0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"),
)
if mibBuilder.loadTexts:
    neceStatesEntry.setStatus("mandatory")
_NeceStatesGpInput1_Type = PerceivedSeverityValue
_NeceStatesGpInput1_Object = MibTableColumn
neceStatesGpInput1 = _NeceStatesGpInput1_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 1),
    _NeceStatesGpInput1_Type()
)
neceStatesGpInput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput1.setStatus("mandatory")
_NeceStatesGpInput2_Type = PerceivedSeverityValue
_NeceStatesGpInput2_Object = MibTableColumn
neceStatesGpInput2 = _NeceStatesGpInput2_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 2),
    _NeceStatesGpInput2_Type()
)
neceStatesGpInput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput2.setStatus("mandatory")
_NeceStatesGpInput3_Type = PerceivedSeverityValue
_NeceStatesGpInput3_Object = MibTableColumn
neceStatesGpInput3 = _NeceStatesGpInput3_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 3),
    _NeceStatesGpInput3_Type()
)
neceStatesGpInput3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput3.setStatus("mandatory")
_NeceStatesGpInput4_Type = PerceivedSeverityValue
_NeceStatesGpInput4_Object = MibTableColumn
neceStatesGpInput4 = _NeceStatesGpInput4_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 4),
    _NeceStatesGpInput4_Type()
)
neceStatesGpInput4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput4.setStatus("mandatory")
_NeceStatesGpInput5_Type = PerceivedSeverityValue
_NeceStatesGpInput5_Object = MibTableColumn
neceStatesGpInput5 = _NeceStatesGpInput5_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 5),
    _NeceStatesGpInput5_Type()
)
neceStatesGpInput5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput5.setStatus("mandatory")
_NeceStatesGpInput6_Type = PerceivedSeverityValue
_NeceStatesGpInput6_Object = MibTableColumn
neceStatesGpInput6 = _NeceStatesGpInput6_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 6),
    _NeceStatesGpInput6_Type()
)
neceStatesGpInput6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput6.setStatus("mandatory")
_NeceStatesGpInput7_Type = PerceivedSeverityValue
_NeceStatesGpInput7_Object = MibTableColumn
neceStatesGpInput7 = _NeceStatesGpInput7_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 7),
    _NeceStatesGpInput7_Type()
)
neceStatesGpInput7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput7.setStatus("mandatory")
_NeceStatesGpInput8_Type = PerceivedSeverityValue
_NeceStatesGpInput8_Object = MibTableColumn
neceStatesGpInput8 = _NeceStatesGpInput8_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 8),
    _NeceStatesGpInput8_Type()
)
neceStatesGpInput8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput8.setStatus("mandatory")
_NeceStatesGpInput9_Type = PerceivedSeverityValue
_NeceStatesGpInput9_Object = MibTableColumn
neceStatesGpInput9 = _NeceStatesGpInput9_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 9),
    _NeceStatesGpInput9_Type()
)
neceStatesGpInput9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput9.setStatus("mandatory")
_NeceStatesGpInput10_Type = PerceivedSeverityValue
_NeceStatesGpInput10_Object = MibTableColumn
neceStatesGpInput10 = _NeceStatesGpInput10_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 10),
    _NeceStatesGpInput10_Type()
)
neceStatesGpInput10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput10.setStatus("mandatory")
_NeceStatesGpInput11_Type = PerceivedSeverityValue
_NeceStatesGpInput11_Object = MibTableColumn
neceStatesGpInput11 = _NeceStatesGpInput11_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 11),
    _NeceStatesGpInput11_Type()
)
neceStatesGpInput11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput11.setStatus("mandatory")
_NeceStatesGpInput12_Type = PerceivedSeverityValue
_NeceStatesGpInput12_Object = MibTableColumn
neceStatesGpInput12 = _NeceStatesGpInput12_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 12),
    _NeceStatesGpInput12_Type()
)
neceStatesGpInput12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesGpInput12.setStatus("mandatory")
_NeceStatesPowerSupplyLeft_Type = PerceivedSeverityValue
_NeceStatesPowerSupplyLeft_Object = MibTableColumn
neceStatesPowerSupplyLeft = _NeceStatesPowerSupplyLeft_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 13),
    _NeceStatesPowerSupplyLeft_Type()
)
neceStatesPowerSupplyLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesPowerSupplyLeft.setStatus("mandatory")
_NeceStatesPowerSupplyRight_Type = PerceivedSeverityValue
_NeceStatesPowerSupplyRight_Object = MibTableColumn
neceStatesPowerSupplyRight = _NeceStatesPowerSupplyRight_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 14),
    _NeceStatesPowerSupplyRight_Type()
)
neceStatesPowerSupplyRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesPowerSupplyRight.setStatus("mandatory")
_NeceStatesFanLeft_Type = PerceivedSeverityValue
_NeceStatesFanLeft_Object = MibTableColumn
neceStatesFanLeft = _NeceStatesFanLeft_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 15),
    _NeceStatesFanLeft_Type()
)
neceStatesFanLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesFanLeft.setStatus("mandatory")
_NeceStatesFanRight_Type = PerceivedSeverityValue
_NeceStatesFanRight_Object = MibTableColumn
neceStatesFanRight = _NeceStatesFanRight_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 16),
    _NeceStatesFanRight_Type()
)
neceStatesFanRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceStatesFanRight.setStatus("mandatory")
_NeceConfiguration_ObjectIdentity = ObjectIdentity
neceConfiguration = _NeceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3)
)
_NeceConfigurationTable_Object = MibTable
neceConfigurationTable = _NeceConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1)
)
if mibBuilder.loadTexts:
    neceConfigurationTable.setStatus("mandatory")
_NeceConfigurationEntry_Object = MibTableRow
neceConfigurationEntry = _NeceConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1)
)
neceConfigurationEntry.setIndexNames(
    (0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"),
)
if mibBuilder.loadTexts:
    neceConfigurationEntry.setStatus("mandatory")
_NeceConfigGpio1Type_Type = GpioType
_NeceConfigGpio1Type_Object = MibTableColumn
neceConfigGpio1Type = _NeceConfigGpio1Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 1),
    _NeceConfigGpio1Type_Type()
)
neceConfigGpio1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio1Type.setStatus("mandatory")
_NeceConfigGpio1Mode_Type = GpioMode
_NeceConfigGpio1Mode_Object = MibTableColumn
neceConfigGpio1Mode = _NeceConfigGpio1Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 2),
    _NeceConfigGpio1Mode_Type()
)
neceConfigGpio1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio1Mode.setStatus("mandatory")
_NeceConfigGpio1LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio1LogicLevel_Object = MibTableColumn
neceConfigGpio1LogicLevel = _NeceConfigGpio1LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 3),
    _NeceConfigGpio1LogicLevel_Type()
)
neceConfigGpio1LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio1LogicLevel.setStatus("mandatory")


class _NeceConfigGpio1Description_Type(DisplayString):
    """Custom type neceConfigGpio1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio1Description_Type.__name__ = "DisplayString"
_NeceConfigGpio1Description_Object = MibTableColumn
neceConfigGpio1Description = _NeceConfigGpio1Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 4),
    _NeceConfigGpio1Description_Type()
)
neceConfigGpio1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio1Description.setStatus("mandatory")
_NeceConfigGpio2Type_Type = GpioType
_NeceConfigGpio2Type_Object = MibTableColumn
neceConfigGpio2Type = _NeceConfigGpio2Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 5),
    _NeceConfigGpio2Type_Type()
)
neceConfigGpio2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio2Type.setStatus("mandatory")
_NeceConfigGpio2Mode_Type = GpioMode
_NeceConfigGpio2Mode_Object = MibTableColumn
neceConfigGpio2Mode = _NeceConfigGpio2Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 6),
    _NeceConfigGpio2Mode_Type()
)
neceConfigGpio2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio2Mode.setStatus("mandatory")
_NeceConfigGpio2LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio2LogicLevel_Object = MibTableColumn
neceConfigGpio2LogicLevel = _NeceConfigGpio2LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 7),
    _NeceConfigGpio2LogicLevel_Type()
)
neceConfigGpio2LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio2LogicLevel.setStatus("mandatory")


class _NeceConfigGpio2Description_Type(DisplayString):
    """Custom type neceConfigGpio2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio2Description_Type.__name__ = "DisplayString"
_NeceConfigGpio2Description_Object = MibTableColumn
neceConfigGpio2Description = _NeceConfigGpio2Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 8),
    _NeceConfigGpio2Description_Type()
)
neceConfigGpio2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio2Description.setStatus("mandatory")
_NeceConfigGpio3Type_Type = GpioType
_NeceConfigGpio3Type_Object = MibTableColumn
neceConfigGpio3Type = _NeceConfigGpio3Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 9),
    _NeceConfigGpio3Type_Type()
)
neceConfigGpio3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio3Type.setStatus("mandatory")
_NeceConfigGpio3Mode_Type = GpioMode
_NeceConfigGpio3Mode_Object = MibTableColumn
neceConfigGpio3Mode = _NeceConfigGpio3Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 10),
    _NeceConfigGpio3Mode_Type()
)
neceConfigGpio3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio3Mode.setStatus("mandatory")
_NeceConfigGpio3LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio3LogicLevel_Object = MibTableColumn
neceConfigGpio3LogicLevel = _NeceConfigGpio3LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 11),
    _NeceConfigGpio3LogicLevel_Type()
)
neceConfigGpio3LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio3LogicLevel.setStatus("mandatory")


class _NeceConfigGpio3Description_Type(DisplayString):
    """Custom type neceConfigGpio3Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio3Description_Type.__name__ = "DisplayString"
_NeceConfigGpio3Description_Object = MibTableColumn
neceConfigGpio3Description = _NeceConfigGpio3Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 12),
    _NeceConfigGpio3Description_Type()
)
neceConfigGpio3Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio3Description.setStatus("mandatory")
_NeceConfigGpio4Type_Type = GpioType
_NeceConfigGpio4Type_Object = MibTableColumn
neceConfigGpio4Type = _NeceConfigGpio4Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 13),
    _NeceConfigGpio4Type_Type()
)
neceConfigGpio4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio4Type.setStatus("mandatory")
_NeceConfigGpio4Mode_Type = GpioMode
_NeceConfigGpio4Mode_Object = MibTableColumn
neceConfigGpio4Mode = _NeceConfigGpio4Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 14),
    _NeceConfigGpio4Mode_Type()
)
neceConfigGpio4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio4Mode.setStatus("mandatory")
_NeceConfigGpio4LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio4LogicLevel_Object = MibTableColumn
neceConfigGpio4LogicLevel = _NeceConfigGpio4LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 15),
    _NeceConfigGpio4LogicLevel_Type()
)
neceConfigGpio4LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio4LogicLevel.setStatus("mandatory")


class _NeceConfigGpio4Description_Type(DisplayString):
    """Custom type neceConfigGpio4Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio4Description_Type.__name__ = "DisplayString"
_NeceConfigGpio4Description_Object = MibTableColumn
neceConfigGpio4Description = _NeceConfigGpio4Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 16),
    _NeceConfigGpio4Description_Type()
)
neceConfigGpio4Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio4Description.setStatus("mandatory")
_NeceConfigGpio5Type_Type = GpioType
_NeceConfigGpio5Type_Object = MibTableColumn
neceConfigGpio5Type = _NeceConfigGpio5Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 17),
    _NeceConfigGpio5Type_Type()
)
neceConfigGpio5Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio5Type.setStatus("mandatory")
_NeceConfigGpio5Mode_Type = GpioMode
_NeceConfigGpio5Mode_Object = MibTableColumn
neceConfigGpio5Mode = _NeceConfigGpio5Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 18),
    _NeceConfigGpio5Mode_Type()
)
neceConfigGpio5Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio5Mode.setStatus("mandatory")
_NeceConfigGpio5LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio5LogicLevel_Object = MibTableColumn
neceConfigGpio5LogicLevel = _NeceConfigGpio5LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 19),
    _NeceConfigGpio5LogicLevel_Type()
)
neceConfigGpio5LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio5LogicLevel.setStatus("mandatory")


class _NeceConfigGpio5Description_Type(DisplayString):
    """Custom type neceConfigGpio5Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio5Description_Type.__name__ = "DisplayString"
_NeceConfigGpio5Description_Object = MibTableColumn
neceConfigGpio5Description = _NeceConfigGpio5Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 20),
    _NeceConfigGpio5Description_Type()
)
neceConfigGpio5Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio5Description.setStatus("mandatory")
_NeceConfigGpio6Type_Type = GpioType
_NeceConfigGpio6Type_Object = MibTableColumn
neceConfigGpio6Type = _NeceConfigGpio6Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 21),
    _NeceConfigGpio6Type_Type()
)
neceConfigGpio6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio6Type.setStatus("mandatory")
_NeceConfigGpio6Mode_Type = GpioMode
_NeceConfigGpio6Mode_Object = MibTableColumn
neceConfigGpio6Mode = _NeceConfigGpio6Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 22),
    _NeceConfigGpio6Mode_Type()
)
neceConfigGpio6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio6Mode.setStatus("mandatory")
_NeceConfigGpio6LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio6LogicLevel_Object = MibTableColumn
neceConfigGpio6LogicLevel = _NeceConfigGpio6LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 23),
    _NeceConfigGpio6LogicLevel_Type()
)
neceConfigGpio6LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio6LogicLevel.setStatus("mandatory")


class _NeceConfigGpio6Description_Type(DisplayString):
    """Custom type neceConfigGpio6Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio6Description_Type.__name__ = "DisplayString"
_NeceConfigGpio6Description_Object = MibTableColumn
neceConfigGpio6Description = _NeceConfigGpio6Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 24),
    _NeceConfigGpio6Description_Type()
)
neceConfigGpio6Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio6Description.setStatus("mandatory")
_NeceConfigGpio7Type_Type = GpioType
_NeceConfigGpio7Type_Object = MibTableColumn
neceConfigGpio7Type = _NeceConfigGpio7Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 25),
    _NeceConfigGpio7Type_Type()
)
neceConfigGpio7Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio7Type.setStatus("mandatory")
_NeceConfigGpio7Mode_Type = GpioMode
_NeceConfigGpio7Mode_Object = MibTableColumn
neceConfigGpio7Mode = _NeceConfigGpio7Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 26),
    _NeceConfigGpio7Mode_Type()
)
neceConfigGpio7Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio7Mode.setStatus("mandatory")
_NeceConfigGpio7LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio7LogicLevel_Object = MibTableColumn
neceConfigGpio7LogicLevel = _NeceConfigGpio7LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 27),
    _NeceConfigGpio7LogicLevel_Type()
)
neceConfigGpio7LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio7LogicLevel.setStatus("mandatory")


class _NeceConfigGpio7Description_Type(DisplayString):
    """Custom type neceConfigGpio7Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio7Description_Type.__name__ = "DisplayString"
_NeceConfigGpio7Description_Object = MibTableColumn
neceConfigGpio7Description = _NeceConfigGpio7Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 28),
    _NeceConfigGpio7Description_Type()
)
neceConfigGpio7Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio7Description.setStatus("mandatory")
_NeceConfigGpio8Type_Type = GpioType
_NeceConfigGpio8Type_Object = MibTableColumn
neceConfigGpio8Type = _NeceConfigGpio8Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 29),
    _NeceConfigGpio8Type_Type()
)
neceConfigGpio8Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio8Type.setStatus("mandatory")
_NeceConfigGpio8Mode_Type = GpioMode
_NeceConfigGpio8Mode_Object = MibTableColumn
neceConfigGpio8Mode = _NeceConfigGpio8Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 30),
    _NeceConfigGpio8Mode_Type()
)
neceConfigGpio8Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio8Mode.setStatus("mandatory")
_NeceConfigGpio8LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio8LogicLevel_Object = MibTableColumn
neceConfigGpio8LogicLevel = _NeceConfigGpio8LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 31),
    _NeceConfigGpio8LogicLevel_Type()
)
neceConfigGpio8LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio8LogicLevel.setStatus("mandatory")


class _NeceConfigGpio8Description_Type(DisplayString):
    """Custom type neceConfigGpio8Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio8Description_Type.__name__ = "DisplayString"
_NeceConfigGpio8Description_Object = MibTableColumn
neceConfigGpio8Description = _NeceConfigGpio8Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 32),
    _NeceConfigGpio8Description_Type()
)
neceConfigGpio8Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio8Description.setStatus("mandatory")
_NeceConfigGpio9Type_Type = GpioType
_NeceConfigGpio9Type_Object = MibTableColumn
neceConfigGpio9Type = _NeceConfigGpio9Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 33),
    _NeceConfigGpio9Type_Type()
)
neceConfigGpio9Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio9Type.setStatus("mandatory")
_NeceConfigGpio9Mode_Type = GpioMode
_NeceConfigGpio9Mode_Object = MibTableColumn
neceConfigGpio9Mode = _NeceConfigGpio9Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 34),
    _NeceConfigGpio9Mode_Type()
)
neceConfigGpio9Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio9Mode.setStatus("mandatory")
_NeceConfigGpio9LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio9LogicLevel_Object = MibTableColumn
neceConfigGpio9LogicLevel = _NeceConfigGpio9LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 35),
    _NeceConfigGpio9LogicLevel_Type()
)
neceConfigGpio9LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio9LogicLevel.setStatus("mandatory")


class _NeceConfigGpio9Description_Type(DisplayString):
    """Custom type neceConfigGpio9Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio9Description_Type.__name__ = "DisplayString"
_NeceConfigGpio9Description_Object = MibTableColumn
neceConfigGpio9Description = _NeceConfigGpio9Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 36),
    _NeceConfigGpio9Description_Type()
)
neceConfigGpio9Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio9Description.setStatus("mandatory")
_NeceConfigGpio10Type_Type = GpioType
_NeceConfigGpio10Type_Object = MibTableColumn
neceConfigGpio10Type = _NeceConfigGpio10Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 37),
    _NeceConfigGpio10Type_Type()
)
neceConfigGpio10Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio10Type.setStatus("mandatory")
_NeceConfigGpio10Mode_Type = GpioMode
_NeceConfigGpio10Mode_Object = MibTableColumn
neceConfigGpio10Mode = _NeceConfigGpio10Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 38),
    _NeceConfigGpio10Mode_Type()
)
neceConfigGpio10Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio10Mode.setStatus("mandatory")
_NeceConfigGpio10LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio10LogicLevel_Object = MibTableColumn
neceConfigGpio10LogicLevel = _NeceConfigGpio10LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 39),
    _NeceConfigGpio10LogicLevel_Type()
)
neceConfigGpio10LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio10LogicLevel.setStatus("mandatory")


class _NeceConfigGpio10Description_Type(DisplayString):
    """Custom type neceConfigGpio10Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio10Description_Type.__name__ = "DisplayString"
_NeceConfigGpio10Description_Object = MibTableColumn
neceConfigGpio10Description = _NeceConfigGpio10Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 40),
    _NeceConfigGpio10Description_Type()
)
neceConfigGpio10Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio10Description.setStatus("mandatory")
_NeceConfigGpio11Type_Type = GpioType
_NeceConfigGpio11Type_Object = MibTableColumn
neceConfigGpio11Type = _NeceConfigGpio11Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 41),
    _NeceConfigGpio11Type_Type()
)
neceConfigGpio11Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio11Type.setStatus("mandatory")
_NeceConfigGpio11Mode_Type = GpioMode
_NeceConfigGpio11Mode_Object = MibTableColumn
neceConfigGpio11Mode = _NeceConfigGpio11Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 42),
    _NeceConfigGpio11Mode_Type()
)
neceConfigGpio11Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio11Mode.setStatus("mandatory")
_NeceConfigGpio11LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio11LogicLevel_Object = MibTableColumn
neceConfigGpio11LogicLevel = _NeceConfigGpio11LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 43),
    _NeceConfigGpio11LogicLevel_Type()
)
neceConfigGpio11LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio11LogicLevel.setStatus("mandatory")


class _NeceConfigGpio11Description_Type(DisplayString):
    """Custom type neceConfigGpio11Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio11Description_Type.__name__ = "DisplayString"
_NeceConfigGpio11Description_Object = MibTableColumn
neceConfigGpio11Description = _NeceConfigGpio11Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 44),
    _NeceConfigGpio11Description_Type()
)
neceConfigGpio11Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio11Description.setStatus("mandatory")
_NeceConfigGpio12Type_Type = GpioType
_NeceConfigGpio12Type_Object = MibTableColumn
neceConfigGpio12Type = _NeceConfigGpio12Type_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 45),
    _NeceConfigGpio12Type_Type()
)
neceConfigGpio12Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigGpio12Type.setStatus("mandatory")
_NeceConfigGpio12Mode_Type = GpioMode
_NeceConfigGpio12Mode_Object = MibTableColumn
neceConfigGpio12Mode = _NeceConfigGpio12Mode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 46),
    _NeceConfigGpio12Mode_Type()
)
neceConfigGpio12Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio12Mode.setStatus("mandatory")
_NeceConfigGpio12LogicLevel_Type = GpioLogicLevel
_NeceConfigGpio12LogicLevel_Object = MibTableColumn
neceConfigGpio12LogicLevel = _NeceConfigGpio12LogicLevel_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 47),
    _NeceConfigGpio12LogicLevel_Type()
)
neceConfigGpio12LogicLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio12LogicLevel.setStatus("mandatory")


class _NeceConfigGpio12Description_Type(DisplayString):
    """Custom type neceConfigGpio12Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NeceConfigGpio12Description_Type.__name__ = "DisplayString"
_NeceConfigGpio12Description_Object = MibTableColumn
neceConfigGpio12Description = _NeceConfigGpio12Description_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 48),
    _NeceConfigGpio12Description_Type()
)
neceConfigGpio12Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGpio12Description.setStatus("mandatory")
_NeceConfigNESlotWrite_Type = NESlotWriteValue
_NeceConfigNESlotWrite_Object = MibTableColumn
neceConfigNESlotWrite = _NeceConfigNESlotWrite_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 49),
    _NeceConfigNESlotWrite_Type()
)
neceConfigNESlotWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigNESlotWrite.setStatus("optional")
_NeceConfigIpAddress_Type = IpAddress
_NeceConfigIpAddress_Object = MibTableColumn
neceConfigIpAddress = _NeceConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 50),
    _NeceConfigIpAddress_Type()
)
neceConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigIpAddress.setStatus("mandatory")
_NeceConfigNetmask_Type = IpAddress
_NeceConfigNetmask_Object = MibTableColumn
neceConfigNetmask = _NeceConfigNetmask_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 51),
    _NeceConfigNetmask_Type()
)
neceConfigNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigNetmask.setStatus("mandatory")
_NeceConfigDefaultrouter_Type = IpAddress
_NeceConfigDefaultrouter_Object = MibTableColumn
neceConfigDefaultrouter = _NeceConfigDefaultrouter_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 52),
    _NeceConfigDefaultrouter_Type()
)
neceConfigDefaultrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigDefaultrouter.setStatus("mandatory")
_NeceConfigTrapReceiver1HostIp_Type = IpAddress
_NeceConfigTrapReceiver1HostIp_Object = MibTableColumn
neceConfigTrapReceiver1HostIp = _NeceConfigTrapReceiver1HostIp_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 53),
    _NeceConfigTrapReceiver1HostIp_Type()
)
neceConfigTrapReceiver1HostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapReceiver1HostIp.setStatus("mandatory")


class _NeceConfigTrapReceiver1Community_Type(DisplayString):
    """Custom type neceConfigTrapReceiver1Community based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 31),
    )


_NeceConfigTrapReceiver1Community_Type.__name__ = "DisplayString"
_NeceConfigTrapReceiver1Community_Object = MibTableColumn
neceConfigTrapReceiver1Community = _NeceConfigTrapReceiver1Community_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 54),
    _NeceConfigTrapReceiver1Community_Type()
)
neceConfigTrapReceiver1Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapReceiver1Community.setStatus("mandatory")
_NeceConfigTrapReceiver2HostIp_Type = IpAddress
_NeceConfigTrapReceiver2HostIp_Object = MibTableColumn
neceConfigTrapReceiver2HostIp = _NeceConfigTrapReceiver2HostIp_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 55),
    _NeceConfigTrapReceiver2HostIp_Type()
)
neceConfigTrapReceiver2HostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapReceiver2HostIp.setStatus("mandatory")


class _NeceConfigTrapReceiver2to4Community_Type(DisplayString):
    """Custom type neceConfigTrapReceiver2to4Community based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 31),
    )


_NeceConfigTrapReceiver2to4Community_Type.__name__ = "DisplayString"
_NeceConfigTrapReceiver2to4Community_Object = MibTableColumn
neceConfigTrapReceiver2to4Community = _NeceConfigTrapReceiver2to4Community_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 56),
    _NeceConfigTrapReceiver2to4Community_Type()
)
neceConfigTrapReceiver2to4Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapReceiver2to4Community.setStatus("mandatory")
_NeceConfigTrapReceiver3HostIp_Type = IpAddress
_NeceConfigTrapReceiver3HostIp_Object = MibTableColumn
neceConfigTrapReceiver3HostIp = _NeceConfigTrapReceiver3HostIp_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 57),
    _NeceConfigTrapReceiver3HostIp_Type()
)
neceConfigTrapReceiver3HostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapReceiver3HostIp.setStatus("mandatory")
_NeceConfigTrapReceiver4HostIp_Type = IpAddress
_NeceConfigTrapReceiver4HostIp_Object = MibTableColumn
neceConfigTrapReceiver4HostIp = _NeceConfigTrapReceiver4HostIp_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 58),
    _NeceConfigTrapReceiver4HostIp_Type()
)
neceConfigTrapReceiver4HostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapReceiver4HostIp.setStatus("mandatory")


class _NeceConfigGetCommunity_Type(DisplayString):
    """Custom type neceConfigGetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NeceConfigGetCommunity_Type.__name__ = "DisplayString"
_NeceConfigGetCommunity_Object = MibTableColumn
neceConfigGetCommunity = _NeceConfigGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 59),
    _NeceConfigGetCommunity_Type()
)
neceConfigGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigGetCommunity.setStatus("mandatory")


class _NeceConfigSetCommunity_Type(DisplayString):
    """Custom type neceConfigSetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NeceConfigSetCommunity_Type.__name__ = "DisplayString"
_NeceConfigSetCommunity_Object = MibTableColumn
neceConfigSetCommunity = _NeceConfigSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 60),
    _NeceConfigSetCommunity_Type()
)
neceConfigSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigSetCommunity.setStatus("mandatory")
_NeceConfigTrapReceiverVerify_Type = TruthValue
_NeceConfigTrapReceiverVerify_Object = MibTableColumn
neceConfigTrapReceiverVerify = _NeceConfigTrapReceiverVerify_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 61),
    _NeceConfigTrapReceiverVerify_Type()
)
neceConfigTrapReceiverVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapReceiverVerify.setStatus("mandatory")
_NeceConfigTrapVerifyReceiverIp_Type = IpAddress
_NeceConfigTrapVerifyReceiverIp_Object = MibTableColumn
neceConfigTrapVerifyReceiverIp = _NeceConfigTrapVerifyReceiverIp_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 62),
    _NeceConfigTrapVerifyReceiverIp_Type()
)
neceConfigTrapVerifyReceiverIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapVerifyReceiverIp.setStatus("mandatory")
_NeceConfigTrapVerifyTimeout_Type = TrapVerifyTimeoutValue
_NeceConfigTrapVerifyTimeout_Object = MibTableColumn
neceConfigTrapVerifyTimeout = _NeceConfigTrapVerifyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 63),
    _NeceConfigTrapVerifyTimeout_Type()
)
neceConfigTrapVerifyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapVerifyTimeout.setStatus("mandatory")
_NeceConfigTrapAccumulationTime_Type = TrapAccumulationTimeValue
_NeceConfigTrapAccumulationTime_Object = MibTableColumn
neceConfigTrapAccumulationTime = _NeceConfigTrapAccumulationTime_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 64),
    _NeceConfigTrapAccumulationTime_Type()
)
neceConfigTrapAccumulationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTrapAccumulationTime.setStatus("mandatory")
_NeceConfigCableWatchUsed_Type = TruthValue
_NeceConfigCableWatchUsed_Object = MibTableColumn
neceConfigCableWatchUsed = _NeceConfigCableWatchUsed_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 65),
    _NeceConfigCableWatchUsed_Type()
)
neceConfigCableWatchUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigCableWatchUsed.setStatus("mandatory")
_NeceConfigHmsTrapsCompliance_Type = HmsTrapsComplianceValue
_NeceConfigHmsTrapsCompliance_Object = MibTableColumn
neceConfigHmsTrapsCompliance = _NeceConfigHmsTrapsCompliance_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 66),
    _NeceConfigHmsTrapsCompliance_Type()
)
neceConfigHmsTrapsCompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigHmsTrapsCompliance.setStatus("mandatory")
_NeceConfigHmsNotificationsEnable_Type = TruthValue
_NeceConfigHmsNotificationsEnable_Object = MibTableColumn
neceConfigHmsNotificationsEnable = _NeceConfigHmsNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 67),
    _NeceConfigHmsNotificationsEnable_Type()
)
neceConfigHmsNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigHmsNotificationsEnable.setStatus("mandatory")
_NeceConfigHfcInventoryFormat_Type = HfcInventoryFormatValue
_NeceConfigHfcInventoryFormat_Object = MibTableColumn
neceConfigHfcInventoryFormat = _NeceConfigHfcInventoryFormat_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 68),
    _NeceConfigHfcInventoryFormat_Type()
)
neceConfigHfcInventoryFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceConfigHfcInventoryFormat.setStatus("mandatory")


class _NeceConfigTimezone_Type(Integer32):
    """Custom type neceConfigTimezone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )


_NeceConfigTimezone_Type.__name__ = "Integer32"
_NeceConfigTimezone_Object = MibTableColumn
neceConfigTimezone = _NeceConfigTimezone_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 69),
    _NeceConfigTimezone_Type()
)
neceConfigTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigTimezone.setStatus("mandatory")
_NeceConfigNtpServerIp_Type = IpAddress
_NeceConfigNtpServerIp_Object = MibTableColumn
neceConfigNtpServerIp = _NeceConfigNtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 70),
    _NeceConfigNtpServerIp_Type()
)
neceConfigNtpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigNtpServerIp.setStatus("mandatory")
_NeceConfigFactoryCommandLine_Type = OctetString
_NeceConfigFactoryCommandLine_Object = MibTableColumn
neceConfigFactoryCommandLine = _NeceConfigFactoryCommandLine_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 71),
    _NeceConfigFactoryCommandLine_Type()
)
neceConfigFactoryCommandLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigFactoryCommandLine.setStatus("mandatory")
_NeceConfigDaylightSavingFrom_Type = DisplayString
_NeceConfigDaylightSavingFrom_Object = MibTableColumn
neceConfigDaylightSavingFrom = _NeceConfigDaylightSavingFrom_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 72),
    _NeceConfigDaylightSavingFrom_Type()
)
neceConfigDaylightSavingFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigDaylightSavingFrom.setStatus("mandatory")
_NeceConfigDaylightSavingTo_Type = DisplayString
_NeceConfigDaylightSavingTo_Object = MibTableColumn
neceConfigDaylightSavingTo = _NeceConfigDaylightSavingTo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 73),
    _NeceConfigDaylightSavingTo_Type()
)
neceConfigDaylightSavingTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceConfigDaylightSavingTo.setStatus("mandatory")
_NeceControl_ObjectIdentity = ObjectIdentity
neceControl = _NeceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 4)
)
_NeceControlTable_Object = MibTable
neceControlTable = _NeceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 4, 1)
)
if mibBuilder.loadTexts:
    neceControlTable.setStatus("mandatory")
_NeceControlEntry_Object = MibTableRow
neceControlEntry = _NeceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 4, 1, 1)
)
neceControlEntry.setIndexNames(
    (0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"),
)
if mibBuilder.loadTexts:
    neceControlEntry.setStatus("mandatory")
_NeceControlReset_Type = TruthValue
_NeceControlReset_Object = MibTableColumn
neceControlReset = _NeceControlReset_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 4, 1, 1, 1),
    _NeceControlReset_Type()
)
neceControlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neceControlReset.setStatus("mandatory")
_NeceMeasuringValues_ObjectIdentity = ObjectIdentity
neceMeasuringValues = _NeceMeasuringValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5)
)
_NeceMeasuringValuesTable_Object = MibTable
neceMeasuringValuesTable = _NeceMeasuringValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1)
)
if mibBuilder.loadTexts:
    neceMeasuringValuesTable.setStatus("mandatory")
_NeceMeasuringValuesEntry_Object = MibTableRow
neceMeasuringValuesEntry = _NeceMeasuringValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1)
)
neceMeasuringValuesEntry.setIndexNames(
    (0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"),
)
if mibBuilder.loadTexts:
    neceMeasuringValuesEntry.setStatus("mandatory")
_NeceTemperatureLoLo_Type = Integer32
_NeceTemperatureLoLo_Object = MibTableColumn
neceTemperatureLoLo = _NeceTemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 1),
    _NeceTemperatureLoLo_Type()
)
neceTemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceTemperatureLoLo.setStatus("mandatory")
_NeceTemperatureLo_Type = Integer32
_NeceTemperatureLo_Object = MibTableColumn
neceTemperatureLo = _NeceTemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 2),
    _NeceTemperatureLo_Type()
)
neceTemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceTemperatureLo.setStatus("mandatory")
_NeceTemperatureValue_Type = Integer32
_NeceTemperatureValue_Object = MibTableColumn
neceTemperatureValue = _NeceTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 3),
    _NeceTemperatureValue_Type()
)
neceTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceTemperatureValue.setStatus("mandatory")
_NeceTemperatureHi_Type = Integer32
_NeceTemperatureHi_Object = MibTableColumn
neceTemperatureHi = _NeceTemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 4),
    _NeceTemperatureHi_Type()
)
neceTemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceTemperatureHi.setStatus("mandatory")
_NeceTemperatureHiHi_Type = Integer32
_NeceTemperatureHiHi_Object = MibTableColumn
neceTemperatureHiHi = _NeceTemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 5),
    _NeceTemperatureHiHi_Type()
)
neceTemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceTemperatureHiHi.setStatus("mandatory")
_NeceDisplay_ObjectIdentity = ObjectIdentity
neceDisplay = _NeceDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6)
)
_NeceDisplayTable_Object = MibTable
neceDisplayTable = _NeceDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6, 1)
)
if mibBuilder.loadTexts:
    neceDisplayTable.setStatus("mandatory")
_NeceDisplayEntry_Object = MibTableRow
neceDisplayEntry = _NeceDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6, 1, 1)
)
neceDisplayEntry.setIndexNames(
    (0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"),
)
if mibBuilder.loadTexts:
    neceDisplayEntry.setStatus("mandatory")
_NeceDisplayTrapsSent_Type = Integer32
_NeceDisplayTrapsSent_Object = MibTableColumn
neceDisplayTrapsSent = _NeceDisplayTrapsSent_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6, 1, 1, 1),
    _NeceDisplayTrapsSent_Type()
)
neceDisplayTrapsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceDisplayTrapsSent.setStatus("mandatory")
_NeceDisplayTrapsDiscarded_Type = Integer32
_NeceDisplayTrapsDiscarded_Object = MibTableColumn
neceDisplayTrapsDiscarded = _NeceDisplayTrapsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6, 1, 1, 2),
    _NeceDisplayTrapsDiscarded_Type()
)
neceDisplayTrapsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neceDisplayTrapsDiscarded.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BKTEL-HFC862-NECE-MIB",
    **{"GpioType": GpioType,
       "GpioMode": GpioMode,
       "GpioLogicLevel": GpioLogicLevel,
       "HmsTrapsComplianceValue": HmsTrapsComplianceValue,
       "HfcInventoryFormatValue": HfcInventoryFormatValue,
       "TrapVerifyTimeoutValue": TrapVerifyTimeoutValue,
       "TrapAccumulationTimeValue": TrapAccumulationTimeValue,
       "NESlotWriteValue": NESlotWriteValue,
       "nece": nece,
       "neceCommon": neceCommon,
       "neceCommonNumberOfModules": neceCommonNumberOfModules,
       "neceCommonTable": neceCommonTable,
       "neceCommonEntry": neceCommonEntry,
       "neceNESlot": neceNESlot,
       "neceCommonType": neceCommonType,
       "neceCommonDescr": neceCommonDescr,
       "neceCommonFirmwareId": neceCommonFirmwareId,
       "neceCommonModuleWidth": neceCommonModuleWidth,
       "neceStates": neceStates,
       "neceStatesTable": neceStatesTable,
       "neceStatesEntry": neceStatesEntry,
       "neceStatesGpInput1": neceStatesGpInput1,
       "neceStatesGpInput2": neceStatesGpInput2,
       "neceStatesGpInput3": neceStatesGpInput3,
       "neceStatesGpInput4": neceStatesGpInput4,
       "neceStatesGpInput5": neceStatesGpInput5,
       "neceStatesGpInput6": neceStatesGpInput6,
       "neceStatesGpInput7": neceStatesGpInput7,
       "neceStatesGpInput8": neceStatesGpInput8,
       "neceStatesGpInput9": neceStatesGpInput9,
       "neceStatesGpInput10": neceStatesGpInput10,
       "neceStatesGpInput11": neceStatesGpInput11,
       "neceStatesGpInput12": neceStatesGpInput12,
       "neceStatesPowerSupplyLeft": neceStatesPowerSupplyLeft,
       "neceStatesPowerSupplyRight": neceStatesPowerSupplyRight,
       "neceStatesFanLeft": neceStatesFanLeft,
       "neceStatesFanRight": neceStatesFanRight,
       "neceConfiguration": neceConfiguration,
       "neceConfigurationTable": neceConfigurationTable,
       "neceConfigurationEntry": neceConfigurationEntry,
       "neceConfigGpio1Type": neceConfigGpio1Type,
       "neceConfigGpio1Mode": neceConfigGpio1Mode,
       "neceConfigGpio1LogicLevel": neceConfigGpio1LogicLevel,
       "neceConfigGpio1Description": neceConfigGpio1Description,
       "neceConfigGpio2Type": neceConfigGpio2Type,
       "neceConfigGpio2Mode": neceConfigGpio2Mode,
       "neceConfigGpio2LogicLevel": neceConfigGpio2LogicLevel,
       "neceConfigGpio2Description": neceConfigGpio2Description,
       "neceConfigGpio3Type": neceConfigGpio3Type,
       "neceConfigGpio3Mode": neceConfigGpio3Mode,
       "neceConfigGpio3LogicLevel": neceConfigGpio3LogicLevel,
       "neceConfigGpio3Description": neceConfigGpio3Description,
       "neceConfigGpio4Type": neceConfigGpio4Type,
       "neceConfigGpio4Mode": neceConfigGpio4Mode,
       "neceConfigGpio4LogicLevel": neceConfigGpio4LogicLevel,
       "neceConfigGpio4Description": neceConfigGpio4Description,
       "neceConfigGpio5Type": neceConfigGpio5Type,
       "neceConfigGpio5Mode": neceConfigGpio5Mode,
       "neceConfigGpio5LogicLevel": neceConfigGpio5LogicLevel,
       "neceConfigGpio5Description": neceConfigGpio5Description,
       "neceConfigGpio6Type": neceConfigGpio6Type,
       "neceConfigGpio6Mode": neceConfigGpio6Mode,
       "neceConfigGpio6LogicLevel": neceConfigGpio6LogicLevel,
       "neceConfigGpio6Description": neceConfigGpio6Description,
       "neceConfigGpio7Type": neceConfigGpio7Type,
       "neceConfigGpio7Mode": neceConfigGpio7Mode,
       "neceConfigGpio7LogicLevel": neceConfigGpio7LogicLevel,
       "neceConfigGpio7Description": neceConfigGpio7Description,
       "neceConfigGpio8Type": neceConfigGpio8Type,
       "neceConfigGpio8Mode": neceConfigGpio8Mode,
       "neceConfigGpio8LogicLevel": neceConfigGpio8LogicLevel,
       "neceConfigGpio8Description": neceConfigGpio8Description,
       "neceConfigGpio9Type": neceConfigGpio9Type,
       "neceConfigGpio9Mode": neceConfigGpio9Mode,
       "neceConfigGpio9LogicLevel": neceConfigGpio9LogicLevel,
       "neceConfigGpio9Description": neceConfigGpio9Description,
       "neceConfigGpio10Type": neceConfigGpio10Type,
       "neceConfigGpio10Mode": neceConfigGpio10Mode,
       "neceConfigGpio10LogicLevel": neceConfigGpio10LogicLevel,
       "neceConfigGpio10Description": neceConfigGpio10Description,
       "neceConfigGpio11Type": neceConfigGpio11Type,
       "neceConfigGpio11Mode": neceConfigGpio11Mode,
       "neceConfigGpio11LogicLevel": neceConfigGpio11LogicLevel,
       "neceConfigGpio11Description": neceConfigGpio11Description,
       "neceConfigGpio12Type": neceConfigGpio12Type,
       "neceConfigGpio12Mode": neceConfigGpio12Mode,
       "neceConfigGpio12LogicLevel": neceConfigGpio12LogicLevel,
       "neceConfigGpio12Description": neceConfigGpio12Description,
       "neceConfigNESlotWrite": neceConfigNESlotWrite,
       "neceConfigIpAddress": neceConfigIpAddress,
       "neceConfigNetmask": neceConfigNetmask,
       "neceConfigDefaultrouter": neceConfigDefaultrouter,
       "neceConfigTrapReceiver1HostIp": neceConfigTrapReceiver1HostIp,
       "neceConfigTrapReceiver1Community": neceConfigTrapReceiver1Community,
       "neceConfigTrapReceiver2HostIp": neceConfigTrapReceiver2HostIp,
       "neceConfigTrapReceiver2to4Community": neceConfigTrapReceiver2to4Community,
       "neceConfigTrapReceiver3HostIp": neceConfigTrapReceiver3HostIp,
       "neceConfigTrapReceiver4HostIp": neceConfigTrapReceiver4HostIp,
       "neceConfigGetCommunity": neceConfigGetCommunity,
       "neceConfigSetCommunity": neceConfigSetCommunity,
       "neceConfigTrapReceiverVerify": neceConfigTrapReceiverVerify,
       "neceConfigTrapVerifyReceiverIp": neceConfigTrapVerifyReceiverIp,
       "neceConfigTrapVerifyTimeout": neceConfigTrapVerifyTimeout,
       "neceConfigTrapAccumulationTime": neceConfigTrapAccumulationTime,
       "neceConfigCableWatchUsed": neceConfigCableWatchUsed,
       "neceConfigHmsTrapsCompliance": neceConfigHmsTrapsCompliance,
       "neceConfigHmsNotificationsEnable": neceConfigHmsNotificationsEnable,
       "neceConfigHfcInventoryFormat": neceConfigHfcInventoryFormat,
       "neceConfigTimezone": neceConfigTimezone,
       "neceConfigNtpServerIp": neceConfigNtpServerIp,
       "neceConfigFactoryCommandLine": neceConfigFactoryCommandLine,
       "neceConfigDaylightSavingFrom": neceConfigDaylightSavingFrom,
       "neceConfigDaylightSavingTo": neceConfigDaylightSavingTo,
       "neceControl": neceControl,
       "neceControlTable": neceControlTable,
       "neceControlEntry": neceControlEntry,
       "neceControlReset": neceControlReset,
       "neceMeasuringValues": neceMeasuringValues,
       "neceMeasuringValuesTable": neceMeasuringValuesTable,
       "neceMeasuringValuesEntry": neceMeasuringValuesEntry,
       "neceTemperatureLoLo": neceTemperatureLoLo,
       "neceTemperatureLo": neceTemperatureLo,
       "neceTemperatureValue": neceTemperatureValue,
       "neceTemperatureHi": neceTemperatureHi,
       "neceTemperatureHiHi": neceTemperatureHiHi,
       "neceDisplay": neceDisplay,
       "neceDisplayTable": neceDisplayTable,
       "neceDisplayEntry": neceDisplayEntry,
       "neceDisplayTrapsSent": neceDisplayTrapsSent,
       "neceDisplayTrapsDiscarded": neceDisplayTrapsDiscarded}
)
