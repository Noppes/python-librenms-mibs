# SNMP MIB module (ATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ats\ATS-MIB

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
 NotificationType,
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
    "NotificationType",
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

(NonNegativeInteger,
 PositiveInteger) = mibBuilder.importSymbols(
    "UPS-MIB",
    "NonNegativeInteger",
    "PositiveInteger")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ats_ObjectIdentity = ObjectIdentity
ats = _Ats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1)
)
_WebAppliance_ObjectIdentity = ObjectIdentity
webAppliance = _WebAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2)
)
_AtsAgent_ObjectIdentity = ObjectIdentity
atsAgent = _AtsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2)
)
_Single_ObjectIdentity = ObjectIdentity
single = _Single_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1)
)
_AtsObjectGroup_ObjectIdentity = ObjectIdentity
atsObjectGroup = _AtsObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1)
)
_AtsIdentGroup_ObjectIdentity = ObjectIdentity
atsIdentGroup = _AtsIdentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 1)
)
_AtsIdentGroupModel_Type = DisplayString
_AtsIdentGroupModel_Object = MibScalar
atsIdentGroupModel = _AtsIdentGroupModel_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 1, 1),
    _AtsIdentGroupModel_Type()
)
atsIdentGroupModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentGroupModel.setStatus("mandatory")
_AtsIdentGroupSerialNumber_Type = DisplayString
_AtsIdentGroupSerialNumber_Object = MibScalar
atsIdentGroupSerialNumber = _AtsIdentGroupSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 1, 2),
    _AtsIdentGroupSerialNumber_Type()
)
atsIdentGroupSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentGroupSerialNumber.setStatus("mandatory")
_AtsIdentGroupManufacturer_Type = DisplayString
_AtsIdentGroupManufacturer_Object = MibScalar
atsIdentGroupManufacturer = _AtsIdentGroupManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 1, 3),
    _AtsIdentGroupManufacturer_Type()
)
atsIdentGroupManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentGroupManufacturer.setStatus("mandatory")
_AtsIdentGroupFirmwareRevision_Type = DisplayString
_AtsIdentGroupFirmwareRevision_Object = MibScalar
atsIdentGroupFirmwareRevision = _AtsIdentGroupFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 1, 4),
    _AtsIdentGroupFirmwareRevision_Type()
)
atsIdentGroupFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentGroupFirmwareRevision.setStatus("mandatory")
_AtsIdentGroupAgentFirmwareRevision_Type = DisplayString
_AtsIdentGroupAgentFirmwareRevision_Object = MibScalar
atsIdentGroupAgentFirmwareRevision = _AtsIdentGroupAgentFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 1, 5),
    _AtsIdentGroupAgentFirmwareRevision_Type()
)
atsIdentGroupAgentFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentGroupAgentFirmwareRevision.setStatus("mandatory")
_AtsInputGroup_ObjectIdentity = ObjectIdentity
atsInputGroup = _AtsInputGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2)
)
_AtsInputGroupPreference_Type = DisplayString
_AtsInputGroupPreference_Object = MibScalar
atsInputGroupPreference = _AtsInputGroupPreference_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 1),
    _AtsInputGroupPreference_Type()
)
atsInputGroupPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupPreference.setStatus("mandatory")


class _AtsInputGroupSourceAstatus_Type(Integer32):
    """Custom type atsInputGroupSourceAstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("ok", 2))
    )


_AtsInputGroupSourceAstatus_Type.__name__ = "Integer32"
_AtsInputGroupSourceAstatus_Object = MibScalar
atsInputGroupSourceAstatus = _AtsInputGroupSourceAstatus_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 2),
    _AtsInputGroupSourceAstatus_Type()
)
atsInputGroupSourceAstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceAstatus.setStatus("mandatory")
_AtsInputGroupSourceAinputVoltage_Type = Integer32
_AtsInputGroupSourceAinputVoltage_Object = MibScalar
atsInputGroupSourceAinputVoltage = _AtsInputGroupSourceAinputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 3),
    _AtsInputGroupSourceAinputVoltage_Type()
)
atsInputGroupSourceAinputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceAinputVoltage.setStatus("mandatory")
_AtsInputGroupSourceAinputFrequency_Type = Integer32
_AtsInputGroupSourceAinputFrequency_Object = MibScalar
atsInputGroupSourceAinputFrequency = _AtsInputGroupSourceAinputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 4),
    _AtsInputGroupSourceAinputFrequency_Type()
)
atsInputGroupSourceAinputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceAinputFrequency.setStatus("mandatory")


class _AtsInputGroupSourceBstatus_Type(Integer32):
    """Custom type atsInputGroupSourceBstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("ok", 2))
    )


_AtsInputGroupSourceBstatus_Type.__name__ = "Integer32"
_AtsInputGroupSourceBstatus_Object = MibScalar
atsInputGroupSourceBstatus = _AtsInputGroupSourceBstatus_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 5),
    _AtsInputGroupSourceBstatus_Type()
)
atsInputGroupSourceBstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceBstatus.setStatus("mandatory")
_AtsInputGroupSourceBinputVoltage_Type = Integer32
_AtsInputGroupSourceBinputVoltage_Object = MibScalar
atsInputGroupSourceBinputVoltage = _AtsInputGroupSourceBinputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 6),
    _AtsInputGroupSourceBinputVoltage_Type()
)
atsInputGroupSourceBinputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceBinputVoltage.setStatus("mandatory")
_AtsInputGroupSourceBinputFrequency_Type = Integer32
_AtsInputGroupSourceBinputFrequency_Object = MibScalar
atsInputGroupSourceBinputFrequency = _AtsInputGroupSourceBinputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 7),
    _AtsInputGroupSourceBinputFrequency_Type()
)
atsInputGroupSourceBinputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceBinputFrequency.setStatus("mandatory")
_AtsInputGroupSourceAvoltageUpperLimit_Type = Integer32
_AtsInputGroupSourceAvoltageUpperLimit_Object = MibScalar
atsInputGroupSourceAvoltageUpperLimit = _AtsInputGroupSourceAvoltageUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 8),
    _AtsInputGroupSourceAvoltageUpperLimit_Type()
)
atsInputGroupSourceAvoltageUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceAvoltageUpperLimit.setStatus("mandatory")
_AtsInputGroupSourceAvoltageLowerLimit_Type = Integer32
_AtsInputGroupSourceAvoltageLowerLimit_Object = MibScalar
atsInputGroupSourceAvoltageLowerLimit = _AtsInputGroupSourceAvoltageLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 9),
    _AtsInputGroupSourceAvoltageLowerLimit_Type()
)
atsInputGroupSourceAvoltageLowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceAvoltageLowerLimit.setStatus("mandatory")
_AtsInputGroupSourceAfrequencyUpperLimit_Type = Integer32
_AtsInputGroupSourceAfrequencyUpperLimit_Object = MibScalar
atsInputGroupSourceAfrequencyUpperLimit = _AtsInputGroupSourceAfrequencyUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 10),
    _AtsInputGroupSourceAfrequencyUpperLimit_Type()
)
atsInputGroupSourceAfrequencyUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceAfrequencyUpperLimit.setStatus("mandatory")
_AtsInputGroupSourceAfrequencyLowerLimit_Type = Integer32
_AtsInputGroupSourceAfrequencyLowerLimit_Object = MibScalar
atsInputGroupSourceAfrequencyLowerLimit = _AtsInputGroupSourceAfrequencyLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 11),
    _AtsInputGroupSourceAfrequencyLowerLimit_Type()
)
atsInputGroupSourceAfrequencyLowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceAfrequencyLowerLimit.setStatus("mandatory")
_AtsInputGroupSourceBvoltageUpperLimit_Type = Integer32
_AtsInputGroupSourceBvoltageUpperLimit_Object = MibScalar
atsInputGroupSourceBvoltageUpperLimit = _AtsInputGroupSourceBvoltageUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 12),
    _AtsInputGroupSourceBvoltageUpperLimit_Type()
)
atsInputGroupSourceBvoltageUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceBvoltageUpperLimit.setStatus("mandatory")
_AtsInputGroupSourceBvoltageLowerLimit_Type = Integer32
_AtsInputGroupSourceBvoltageLowerLimit_Object = MibScalar
atsInputGroupSourceBvoltageLowerLimit = _AtsInputGroupSourceBvoltageLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 13),
    _AtsInputGroupSourceBvoltageLowerLimit_Type()
)
atsInputGroupSourceBvoltageLowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceBvoltageLowerLimit.setStatus("mandatory")
_AtsInputGroupSourceBfrequencyUpperLimit_Type = Integer32
_AtsInputGroupSourceBfrequencyUpperLimit_Object = MibScalar
atsInputGroupSourceBfrequencyUpperLimit = _AtsInputGroupSourceBfrequencyUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 14),
    _AtsInputGroupSourceBfrequencyUpperLimit_Type()
)
atsInputGroupSourceBfrequencyUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceBfrequencyUpperLimit.setStatus("mandatory")
_AtsInputGroupSourceBfrequencyLowerLimit_Type = Integer32
_AtsInputGroupSourceBfrequencyLowerLimit_Object = MibScalar
atsInputGroupSourceBfrequencyLowerLimit = _AtsInputGroupSourceBfrequencyLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 2, 15),
    _AtsInputGroupSourceBfrequencyLowerLimit_Type()
)
atsInputGroupSourceBfrequencyLowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputGroupSourceBfrequencyLowerLimit.setStatus("mandatory")
_AtsOutputGroup_ObjectIdentity = ObjectIdentity
atsOutputGroup = _AtsOutputGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 3)
)
_AtsOutputGroupOutputSource_Type = DisplayString
_AtsOutputGroupOutputSource_Object = MibScalar
atsOutputGroupOutputSource = _AtsOutputGroupOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 3, 1),
    _AtsOutputGroupOutputSource_Type()
)
atsOutputGroupOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputGroupOutputSource.setStatus("mandatory")
_AtsOutputGroupOutputVoltage_Type = NonNegativeInteger
_AtsOutputGroupOutputVoltage_Object = MibScalar
atsOutputGroupOutputVoltage = _AtsOutputGroupOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 3, 2),
    _AtsOutputGroupOutputVoltage_Type()
)
atsOutputGroupOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputGroupOutputVoltage.setStatus("mandatory")
_AtsOutputGroupOutputFequency_Type = NonNegativeInteger
_AtsOutputGroupOutputFequency_Object = MibScalar
atsOutputGroupOutputFequency = _AtsOutputGroupOutputFequency_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 3, 3),
    _AtsOutputGroupOutputFequency_Type()
)
atsOutputGroupOutputFequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputGroupOutputFequency.setStatus("mandatory")
_AtsOutputGroupOutputCurrent_Type = NonNegativeInteger
_AtsOutputGroupOutputCurrent_Object = MibScalar
atsOutputGroupOutputCurrent = _AtsOutputGroupOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 3, 4),
    _AtsOutputGroupOutputCurrent_Type()
)
atsOutputGroupOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputGroupOutputCurrent.setStatus("mandatory")
_AtsOutputGroupLoad_Type = NonNegativeInteger
_AtsOutputGroupLoad_Object = MibScalar
atsOutputGroupLoad = _AtsOutputGroupLoad_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 3, 5),
    _AtsOutputGroupLoad_Type()
)
atsOutputGroupLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputGroupLoad.setStatus("mandatory")
_AtsHmiSwitchGroup_ObjectIdentity = ObjectIdentity
atsHmiSwitchGroup = _AtsHmiSwitchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 4)
)


class _AtsHmiSwitchGroupBuzzer_Type(Integer32):
    """Custom type atsHmiSwitchGroupBuzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("buzzerDisabled", 1),
          ("buzzerEnabled", 2))
    )


_AtsHmiSwitchGroupBuzzer_Type.__name__ = "Integer32"
_AtsHmiSwitchGroupBuzzer_Object = MibScalar
atsHmiSwitchGroupBuzzer = _AtsHmiSwitchGroupBuzzer_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 4, 1),
    _AtsHmiSwitchGroupBuzzer_Type()
)
atsHmiSwitchGroupBuzzer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsHmiSwitchGroupBuzzer.setStatus("mandatory")


class _AtsHmiSwitchGroupAtsAlarm_Type(Integer32):
    """Custom type atsHmiSwitchGroupAtsAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("atsOccurAlarm", 2))
    )


_AtsHmiSwitchGroupAtsAlarm_Type.__name__ = "Integer32"
_AtsHmiSwitchGroupAtsAlarm_Object = MibScalar
atsHmiSwitchGroupAtsAlarm = _AtsHmiSwitchGroupAtsAlarm_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 4, 2),
    _AtsHmiSwitchGroupAtsAlarm_Type()
)
atsHmiSwitchGroupAtsAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsHmiSwitchGroupAtsAlarm.setStatus("mandatory")


class _AtsHmiSwitchGroupAutoReturn_Type(Integer32):
    """Custom type atsHmiSwitchGroupAutoReturn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtsHmiSwitchGroupAutoReturn_Type.__name__ = "Integer32"
_AtsHmiSwitchGroupAutoReturn_Object = MibScalar
atsHmiSwitchGroupAutoReturn = _AtsHmiSwitchGroupAutoReturn_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 4, 3),
    _AtsHmiSwitchGroupAutoReturn_Type()
)
atsHmiSwitchGroupAutoReturn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsHmiSwitchGroupAutoReturn.setStatus("mandatory")


class _AtsHmiSwitchGroupSourceTransferByLoad_Type(Integer32):
    """Custom type atsHmiSwitchGroupSourceTransferByLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtsHmiSwitchGroupSourceTransferByLoad_Type.__name__ = "Integer32"
_AtsHmiSwitchGroupSourceTransferByLoad_Object = MibScalar
atsHmiSwitchGroupSourceTransferByLoad = _AtsHmiSwitchGroupSourceTransferByLoad_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 4, 4),
    _AtsHmiSwitchGroupSourceTransferByLoad_Type()
)
atsHmiSwitchGroupSourceTransferByLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsHmiSwitchGroupSourceTransferByLoad.setStatus("mandatory")


class _AtsHmiSwitchGroupSourceTransferByPhase_Type(Integer32):
    """Custom type atsHmiSwitchGroupSourceTransferByPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtsHmiSwitchGroupSourceTransferByPhase_Type.__name__ = "Integer32"
_AtsHmiSwitchGroupSourceTransferByPhase_Object = MibScalar
atsHmiSwitchGroupSourceTransferByPhase = _AtsHmiSwitchGroupSourceTransferByPhase_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 4, 5),
    _AtsHmiSwitchGroupSourceTransferByPhase_Type()
)
atsHmiSwitchGroupSourceTransferByPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsHmiSwitchGroupSourceTransferByPhase.setStatus("mandatory")
_AtsMiscellaneousGroup_ObjectIdentity = ObjectIdentity
atsMiscellaneousGroup = _AtsMiscellaneousGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 5)
)
_AtsMiscellaneousGroupAtsSystemTemperture_Type = Integer32
_AtsMiscellaneousGroupAtsSystemTemperture_Object = MibScalar
atsMiscellaneousGroupAtsSystemTemperture = _AtsMiscellaneousGroupAtsSystemTemperture_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 5, 1),
    _AtsMiscellaneousGroupAtsSystemTemperture_Type()
)
atsMiscellaneousGroupAtsSystemTemperture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsMiscellaneousGroupAtsSystemTemperture.setStatus("mandatory")
_AtsMiscellaneousGroupSystemMaxCurrent_Type = Integer32
_AtsMiscellaneousGroupSystemMaxCurrent_Object = MibScalar
atsMiscellaneousGroupSystemMaxCurrent = _AtsMiscellaneousGroupSystemMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 5, 2),
    _AtsMiscellaneousGroupSystemMaxCurrent_Type()
)
atsMiscellaneousGroupSystemMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsMiscellaneousGroupSystemMaxCurrent.setStatus("mandatory")
_AtsControlGroup_ObjectIdentity = ObjectIdentity
atsControlGroup = _AtsControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 6)
)


class _AtsControlGroupBuzzerAlarmControl_Type(Integer32):
    """Custom type atsControlGroupBuzzerAlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("buzzerOff", 1),
          ("buzzerOn", 2))
    )


_AtsControlGroupBuzzerAlarmControl_Type.__name__ = "Integer32"
_AtsControlGroupBuzzerAlarmControl_Object = MibScalar
atsControlGroupBuzzerAlarmControl = _AtsControlGroupBuzzerAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 6, 1),
    _AtsControlGroupBuzzerAlarmControl_Type()
)
atsControlGroupBuzzerAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsControlGroupBuzzerAlarmControl.setStatus("mandatory")
_AtsControlGroupManualTransfer_Type = Integer32
_AtsControlGroupManualTransfer_Object = MibScalar
atsControlGroupManualTransfer = _AtsControlGroupManualTransfer_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 6, 2),
    _AtsControlGroupManualTransfer_Type()
)
atsControlGroupManualTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsControlGroupManualTransfer.setStatus("mandatory")
_AgentConfig_ObjectIdentity = ObjectIdentity
agentConfig = _AgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7)
)
_AgentConfigIpaddress_Type = IpAddress
_AgentConfigIpaddress_Object = MibScalar
agentConfigIpaddress = _AgentConfigIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 1),
    _AgentConfigIpaddress_Type()
)
agentConfigIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigIpaddress.setStatus("mandatory")
_AgentConfigGateway_Type = IpAddress
_AgentConfigGateway_Object = MibScalar
agentConfigGateway = _AgentConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 2),
    _AgentConfigGateway_Type()
)
agentConfigGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigGateway.setStatus("mandatory")
_AgentConfigSubnetMask_Type = IpAddress
_AgentConfigSubnetMask_Object = MibScalar
agentConfigSubnetMask = _AgentConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 3),
    _AgentConfigSubnetMask_Type()
)
agentConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigSubnetMask.setStatus("mandatory")


class _AgentConfigDate_Type(DisplayString):
    """Custom type agentConfigDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_AgentConfigDate_Type.__name__ = "DisplayString"
_AgentConfigDate_Object = MibScalar
agentConfigDate = _AgentConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 4),
    _AgentConfigDate_Type()
)
agentConfigDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigDate.setStatus("mandatory")


class _AgentConfigTime_Type(DisplayString):
    """Custom type agentConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AgentConfigTime_Type.__name__ = "DisplayString"
_AgentConfigTime_Object = MibScalar
agentConfigTime = _AgentConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 5),
    _AgentConfigTime_Type()
)
agentConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTime.setStatus("mandatory")


class _AgentConfigHistoryLogFrequency_Type(Integer32):
    """Custom type agentConfigHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28800),
    )


_AgentConfigHistoryLogFrequency_Type.__name__ = "Integer32"
_AgentConfigHistoryLogFrequency_Object = MibScalar
agentConfigHistoryLogFrequency = _AgentConfigHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 6),
    _AgentConfigHistoryLogFrequency_Type()
)
agentConfigHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigHistoryLogFrequency.setStatus("mandatory")


class _AgentConfigExtHistoryLogFrequency_Type(Integer32):
    """Custom type agentConfigExtHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10080),
    )


_AgentConfigExtHistoryLogFrequency_Type.__name__ = "Integer32"
_AgentConfigExtHistoryLogFrequency_Object = MibScalar
agentConfigExtHistoryLogFrequency = _AgentConfigExtHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 7),
    _AgentConfigExtHistoryLogFrequency_Type()
)
agentConfigExtHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigExtHistoryLogFrequency.setStatus("mandatory")


class _AgentConfigPollRate_Type(Integer32):
    """Custom type agentConfigPollRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AgentConfigPollRate_Type.__name__ = "Integer32"
_AgentConfigPollRate_Object = MibScalar
agentConfigPollRate = _AgentConfigPollRate_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 8),
    _AgentConfigPollRate_Type()
)
agentConfigPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigPollRate.setStatus("mandatory")
_AgentConfigBaudRate_Type = Integer32
_AgentConfigBaudRate_Object = MibScalar
agentConfigBaudRate = _AgentConfigBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 9),
    _AgentConfigBaudRate_Type()
)
agentConfigBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentConfigBaudRate.setStatus("mandatory")


class _AgentConfigDhcpStatue_Type(Integer32):
    """Custom type agentConfigDhcpStatue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AgentConfigDhcpStatue_Type.__name__ = "Integer32"
_AgentConfigDhcpStatue_Object = MibScalar
agentConfigDhcpStatue = _AgentConfigDhcpStatue_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 10),
    _AgentConfigDhcpStatue_Type()
)
agentConfigDhcpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigDhcpStatue.setStatus("mandatory")


class _AgentConfigTelnetStatue_Type(Integer32):
    """Custom type agentConfigTelnetStatue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AgentConfigTelnetStatue_Type.__name__ = "Integer32"
_AgentConfigTelnetStatue_Object = MibScalar
agentConfigTelnetStatue = _AgentConfigTelnetStatue_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 11),
    _AgentConfigTelnetStatue_Type()
)
agentConfigTelnetStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTelnetStatue.setStatus("mandatory")


class _AgentConfigTftpStatue_Type(Integer32):
    """Custom type agentConfigTftpStatue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AgentConfigTftpStatue_Type.__name__ = "Integer32"
_AgentConfigTftpStatue_Object = MibScalar
agentConfigTftpStatue = _AgentConfigTftpStatue_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 12),
    _AgentConfigTftpStatue_Type()
)
agentConfigTftpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTftpStatue.setStatus("mandatory")


class _AgentConfigResetToDefault_Type(Integer32):
    """Custom type agentConfigResetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("nothing", 2))
    )


_AgentConfigResetToDefault_Type.__name__ = "Integer32"
_AgentConfigResetToDefault_Object = MibScalar
agentConfigResetToDefault = _AgentConfigResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 13),
    _AgentConfigResetToDefault_Type()
)
agentConfigResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigResetToDefault.setStatus("mandatory")


class _AgentConfigRestart_Type(Integer32):
    """Custom type agentConfigRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restart", 1),
          ("nothing", 2))
    )


_AgentConfigRestart_Type.__name__ = "Integer32"
_AgentConfigRestart_Object = MibScalar
agentConfigRestart = _AgentConfigRestart_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 14),
    _AgentConfigRestart_Type()
)
agentConfigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigRestart.setStatus("mandatory")


class _AgentConfigClearAgentLog_Type(Integer32):
    """Custom type agentConfigClearAgentLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_AgentConfigClearAgentLog_Type.__name__ = "Integer32"
_AgentConfigClearAgentLog_Object = MibScalar
agentConfigClearAgentLog = _AgentConfigClearAgentLog_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 15),
    _AgentConfigClearAgentLog_Type()
)
agentConfigClearAgentLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigClearAgentLog.setStatus("mandatory")


class _AgentConfigClearEventLog_Type(Integer32):
    """Custom type agentConfigClearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_AgentConfigClearEventLog_Type.__name__ = "Integer32"
_AgentConfigClearEventLog_Object = MibScalar
agentConfigClearEventLog = _AgentConfigClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 16),
    _AgentConfigClearEventLog_Type()
)
agentConfigClearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigClearEventLog.setStatus("mandatory")


class _AgentConfigClearExtHistoryLog_Type(Integer32):
    """Custom type agentConfigClearExtHistoryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_AgentConfigClearExtHistoryLog_Type.__name__ = "Integer32"
_AgentConfigClearExtHistoryLog_Object = MibScalar
agentConfigClearExtHistoryLog = _AgentConfigClearExtHistoryLog_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 17),
    _AgentConfigClearExtHistoryLog_Type()
)
agentConfigClearExtHistoryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigClearExtHistoryLog.setStatus("mandatory")


class _AgentConfigClearHistoryLog_Type(Integer32):
    """Custom type agentConfigClearHistoryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_AgentConfigClearHistoryLog_Type.__name__ = "Integer32"
_AgentConfigClearHistoryLog_Object = MibScalar
agentConfigClearHistoryLog = _AgentConfigClearHistoryLog_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 18),
    _AgentConfigClearHistoryLog_Type()
)
agentConfigClearHistoryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigClearHistoryLog.setStatus("mandatory")
_AgentConfigTrapRetryCount_Type = Integer32
_AgentConfigTrapRetryCount_Object = MibScalar
agentConfigTrapRetryCount = _AgentConfigTrapRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 19),
    _AgentConfigTrapRetryCount_Type()
)
agentConfigTrapRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTrapRetryCount.setStatus("mandatory")
_AgentConfigTrapRetryTime_Type = Integer32
_AgentConfigTrapRetryTime_Object = MibScalar
agentConfigTrapRetryTime = _AgentConfigTrapRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 20),
    _AgentConfigTrapRetryTime_Type()
)
agentConfigTrapRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTrapRetryTime.setStatus("mandatory")
_AgentConfigTrapAckSignature_Type = Integer32
_AgentConfigTrapAckSignature_Object = MibScalar
agentConfigTrapAckSignature = _AgentConfigTrapAckSignature_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 21),
    _AgentConfigTrapAckSignature_Type()
)
agentConfigTrapAckSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTrapAckSignature.setStatus("mandatory")
_AgentConfigMibVersion_Type = Integer32
_AgentConfigMibVersion_Object = MibScalar
agentConfigMibVersion = _AgentConfigMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 22),
    _AgentConfigMibVersion_Type()
)
agentConfigMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentConfigMibVersion.setStatus("mandatory")
_AgentConfigTrapsReceiversTable_Object = MibTable
agentConfigTrapsReceiversTable = _AgentConfigTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 23)
)
if mibBuilder.loadTexts:
    agentConfigTrapsReceiversTable.setStatus("mandatory")
_AgentConfigTrapsReceiversEntry_Object = MibTableRow
agentConfigTrapsReceiversEntry = _AgentConfigTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 23, 1)
)
agentConfigTrapsReceiversEntry.setIndexNames(
    (0, "ATS-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    agentConfigTrapsReceiversEntry.setStatus("mandatory")


class _TrapsIndex_Type(Integer32):
    """Custom type trapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapsIndex_Type.__name__ = "Integer32"
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 23, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")
_TrapsReceiverAddr_Type = DisplayString
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 23, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")


class _ReceiverCommunityString_Type(DisplayString):
    """Custom type receiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ReceiverCommunityString_Type.__name__ = "DisplayString"
_ReceiverCommunityString_Object = MibTableColumn
receiverCommunityString = _ReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 23, 1, 3),
    _ReceiverCommunityString_Type()
)
receiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverCommunityString.setStatus("mandatory")


class _ReceiverNmsType_Type(Integer32):
    """Custom type receiverNmsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ats-trap", 2))
    )


_ReceiverNmsType_Type.__name__ = "Integer32"
_ReceiverNmsType_Object = MibTableColumn
receiverNmsType = _ReceiverNmsType_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 23, 1, 4),
    _ReceiverNmsType_Type()
)
receiverNmsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverNmsType.setStatus("mandatory")


class _ReceiverSeverityLevel_Type(Integer32):
    """Custom type receiverSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 1),
          ("warning", 2),
          ("severe", 3))
    )


_ReceiverSeverityLevel_Type.__name__ = "Integer32"
_ReceiverSeverityLevel_Object = MibTableColumn
receiverSeverityLevel = _ReceiverSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 23, 1, 5),
    _ReceiverSeverityLevel_Type()
)
receiverSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverSeverityLevel.setStatus("mandatory")


class _ReceiverDescription_Type(DisplayString):
    """Custom type receiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReceiverDescription_Type.__name__ = "DisplayString"
_ReceiverDescription_Object = MibTableColumn
receiverDescription = _ReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 23, 1, 6),
    _ReceiverDescription_Type()
)
receiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverDescription.setStatus("mandatory")
_AgentConfigAccessControlTable_Object = MibTable
agentConfigAccessControlTable = _AgentConfigAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 24)
)
if mibBuilder.loadTexts:
    agentConfigAccessControlTable.setStatus("mandatory")
_AgentConfigAccessControlEntry_Object = MibTableRow
agentConfigAccessControlEntry = _AgentConfigAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 24, 1)
)
agentConfigAccessControlEntry.setIndexNames(
    (0, "ATS-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    agentConfigAccessControlEntry.setStatus("mandatory")
_AccessIndex_Type = Integer32
_AccessIndex_Object = MibTableColumn
accessIndex = _AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 24, 1, 1),
    _AccessIndex_Type()
)
accessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessIndex.setStatus("mandatory")
_AccessControlAddr_Type = IpAddress
_AccessControlAddr_Object = MibTableColumn
accessControlAddr = _AccessControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 24, 1, 2),
    _AccessControlAddr_Type()
)
accessControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlAddr.setStatus("mandatory")


class _AccessCommunityString_Type(DisplayString):
    """Custom type accessCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AccessCommunityString_Type.__name__ = "DisplayString"
_AccessCommunityString_Object = MibTableColumn
accessCommunityString = _AccessCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 24, 1, 3),
    _AccessCommunityString_Type()
)
accessCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCommunityString.setStatus("mandatory")


class _AccessControlMode_Type(Integer32):
    """Custom type accessControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2),
          ("notAccess", 3))
    )


_AccessControlMode_Type.__name__ = "Integer32"
_AccessControlMode_Object = MibTableColumn
accessControlMode = _AccessControlMode_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 24, 1, 4),
    _AccessControlMode_Type()
)
accessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlMode.setStatus("mandatory")


class _AgentConfigDefaultLanguage_Type(Integer32):
    """Custom type agentConfigDefaultLanguage based on Integer32"""
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
        *(("auto", 1),
          ("english", 2),
          ("traditionalChinese", 3),
          ("simplifiedChinese", 4))
    )


_AgentConfigDefaultLanguage_Type.__name__ = "Integer32"
_AgentConfigDefaultLanguage_Object = MibScalar
agentConfigDefaultLanguage = _AgentConfigDefaultLanguage_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 25),
    _AgentConfigDefaultLanguage_Type()
)
agentConfigDefaultLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigDefaultLanguage.setStatus("mandatory")


class _AgentConfigIPv6AddrStatus_Type(Integer32):
    """Custom type agentConfigIPv6AddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2),
          ("manualConfiguration", 3))
    )


_AgentConfigIPv6AddrStatus_Type.__name__ = "Integer32"
_AgentConfigIPv6AddrStatus_Object = MibScalar
agentConfigIPv6AddrStatus = _AgentConfigIPv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 26),
    _AgentConfigIPv6AddrStatus_Type()
)
agentConfigIPv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentConfigIPv6AddrStatus.setStatus("mandatory")


class _AgentConfigIPv6AddrAutoConfig_Type(Integer32):
    """Custom type agentConfigIPv6AddrAutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentConfigIPv6AddrAutoConfig_Type.__name__ = "Integer32"
_AgentConfigIPv6AddrAutoConfig_Object = MibScalar
agentConfigIPv6AddrAutoConfig = _AgentConfigIPv6AddrAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 27),
    _AgentConfigIPv6AddrAutoConfig_Type()
)
agentConfigIPv6AddrAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigIPv6AddrAutoConfig.setStatus("mandatory")


class _AgentConfigIPv6LinkLocalAddr_Type(DisplayString):
    """Custom type agentConfigIPv6LinkLocalAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentConfigIPv6LinkLocalAddr_Type.__name__ = "DisplayString"
_AgentConfigIPv6LinkLocalAddr_Object = MibScalar
agentConfigIPv6LinkLocalAddr = _AgentConfigIPv6LinkLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 28),
    _AgentConfigIPv6LinkLocalAddr_Type()
)
agentConfigIPv6LinkLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentConfigIPv6LinkLocalAddr.setStatus("mandatory")


class _AgentConfigIPv6GlobalAddr_Type(DisplayString):
    """Custom type agentConfigIPv6GlobalAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentConfigIPv6GlobalAddr_Type.__name__ = "DisplayString"
_AgentConfigIPv6GlobalAddr_Object = MibScalar
agentConfigIPv6GlobalAddr = _AgentConfigIPv6GlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 29),
    _AgentConfigIPv6GlobalAddr_Type()
)
agentConfigIPv6GlobalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigIPv6GlobalAddr.setStatus("mandatory")


class _AgentConfigIPv6PrefixlLength_Type(Integer32):
    """Custom type agentConfigIPv6PrefixlLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AgentConfigIPv6PrefixlLength_Type.__name__ = "Integer32"
_AgentConfigIPv6PrefixlLength_Object = MibScalar
agentConfigIPv6PrefixlLength = _AgentConfigIPv6PrefixlLength_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 30),
    _AgentConfigIPv6PrefixlLength_Type()
)
agentConfigIPv6PrefixlLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigIPv6PrefixlLength.setStatus("mandatory")


class _AgentConfigIPv6DefaultRouter_Type(DisplayString):
    """Custom type agentConfigIPv6DefaultRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentConfigIPv6DefaultRouter_Type.__name__ = "DisplayString"
_AgentConfigIPv6DefaultRouter_Object = MibScalar
agentConfigIPv6DefaultRouter = _AgentConfigIPv6DefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 7, 31),
    _AgentConfigIPv6DefaultRouter_Type()
)
agentConfigIPv6DefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigIPv6DefaultRouter.setStatus("mandatory")
_EmdStatus_ObjectIdentity = ObjectIdentity
emdStatus = _EmdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 8)
)


class _EmdSatatusEmdType_Type(Integer32):
    """Custom type emdSatatusEmdType based on Integer32"""
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
          ("disabled", 2),
          ("emdHT", 3),
          ("emdT", 4))
    )


_EmdSatatusEmdType_Type.__name__ = "Integer32"
_EmdSatatusEmdType_Object = MibScalar
emdSatatusEmdType = _EmdSatatusEmdType_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 8, 1),
    _EmdSatatusEmdType_Type()
)
emdSatatusEmdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusEmdType.setStatus("mandatory")
_EmdSatatusTemperature_Type = Integer32
_EmdSatatusTemperature_Object = MibScalar
emdSatatusTemperature = _EmdSatatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 8, 2),
    _EmdSatatusTemperature_Type()
)
emdSatatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusTemperature.setStatus("mandatory")
_EmdSatatusHumidity_Type = Integer32
_EmdSatatusHumidity_Object = MibScalar
emdSatatusHumidity = _EmdSatatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 8, 3),
    _EmdSatatusHumidity_Type()
)
emdSatatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusHumidity.setStatus("mandatory")


class _EmdSatatusAlarm1_Type(Integer32):
    """Custom type emdSatatusAlarm1 based on Integer32"""
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
        *(("unknow", 1),
          ("disabled", 2),
          ("active", 3),
          ("inactive", 4))
    )


_EmdSatatusAlarm1_Type.__name__ = "Integer32"
_EmdSatatusAlarm1_Object = MibScalar
emdSatatusAlarm1 = _EmdSatatusAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 8, 4),
    _EmdSatatusAlarm1_Type()
)
emdSatatusAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusAlarm1.setStatus("mandatory")


class _EmdSatatusAlarm2_Type(Integer32):
    """Custom type emdSatatusAlarm2 based on Integer32"""
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
        *(("unknow", 1),
          ("disabled", 2),
          ("active", 3),
          ("inactive", 4))
    )


_EmdSatatusAlarm2_Type.__name__ = "Integer32"
_EmdSatatusAlarm2_Object = MibScalar
emdSatatusAlarm2 = _EmdSatatusAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 8, 5),
    _EmdSatatusAlarm2_Type()
)
emdSatatusAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusAlarm2.setStatus("mandatory")
_EmdConfig_ObjectIdentity = ObjectIdentity
emdConfig = _EmdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9)
)


class _UsahEmdConfigEmdConfig_Type(Integer32):
    """Custom type usahEmdConfigEmdConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("auto", 2))
    )


_UsahEmdConfigEmdConfig_Type.__name__ = "Integer32"
_UsahEmdConfigEmdConfig_Object = MibScalar
usahEmdConfigEmdConfig = _UsahEmdConfigEmdConfig_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 1),
    _UsahEmdConfigEmdConfig_Type()
)
usahEmdConfigEmdConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usahEmdConfigEmdConfig.setStatus("mandatory")


class _EmdConfigEmdName_Type(DisplayString):
    """Custom type emdConfigEmdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigEmdName_Type.__name__ = "DisplayString"
_EmdConfigEmdName_Object = MibScalar
emdConfigEmdName = _EmdConfigEmdName_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 2),
    _EmdConfigEmdName_Type()
)
emdConfigEmdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigEmdName.setStatus("mandatory")
_EmdConfigTemperature_ObjectIdentity = ObjectIdentity
emdConfigTemperature = _EmdConfigTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 3)
)


class _EmdConfigTempName_Type(DisplayString):
    """Custom type emdConfigTempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigTempName_Type.__name__ = "DisplayString"
_EmdConfigTempName_Object = MibScalar
emdConfigTempName = _EmdConfigTempName_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 3, 1),
    _EmdConfigTempName_Type()
)
emdConfigTempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempName.setStatus("mandatory")
_EmdConfigTempHighSetPoint_Type = Integer32
_EmdConfigTempHighSetPoint_Object = MibScalar
emdConfigTempHighSetPoint = _EmdConfigTempHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 3, 2),
    _EmdConfigTempHighSetPoint_Type()
)
emdConfigTempHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempHighSetPoint.setStatus("mandatory")


class _EmdConfigTempHighStatus_Type(Integer32):
    """Custom type emdConfigTempHighStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EmdConfigTempHighStatus_Type.__name__ = "Integer32"
_EmdConfigTempHighStatus_Object = MibScalar
emdConfigTempHighStatus = _EmdConfigTempHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 3, 3),
    _EmdConfigTempHighStatus_Type()
)
emdConfigTempHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempHighStatus.setStatus("mandatory")
_EmdConfigTempLowSetPoint_Type = Integer32
_EmdConfigTempLowSetPoint_Object = MibScalar
emdConfigTempLowSetPoint = _EmdConfigTempLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 3, 4),
    _EmdConfigTempLowSetPoint_Type()
)
emdConfigTempLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempLowSetPoint.setStatus("mandatory")


class _EmdConfigTempLowStatus_Type(Integer32):
    """Custom type emdConfigTempLowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EmdConfigTempLowStatus_Type.__name__ = "Integer32"
_EmdConfigTempLowStatus_Object = MibScalar
emdConfigTempLowStatus = _EmdConfigTempLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 3, 5),
    _EmdConfigTempLowStatus_Type()
)
emdConfigTempLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempLowStatus.setStatus("mandatory")
_EmdConfigTempOffset_Type = Integer32
_EmdConfigTempOffset_Object = MibScalar
emdConfigTempOffset = _EmdConfigTempOffset_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 3, 6),
    _EmdConfigTempOffset_Type()
)
emdConfigTempOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempOffset.setStatus("mandatory")
_EmdConfigHumidity_ObjectIdentity = ObjectIdentity
emdConfigHumidity = _EmdConfigHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 4)
)


class _EmdConfigHumidityName_Type(DisplayString):
    """Custom type emdConfigHumidityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigHumidityName_Type.__name__ = "DisplayString"
_EmdConfigHumidityName_Object = MibScalar
emdConfigHumidityName = _EmdConfigHumidityName_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 4, 1),
    _EmdConfigHumidityName_Type()
)
emdConfigHumidityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityName.setStatus("mandatory")
_EmdConfigHumidityHighSetPoint_Type = Integer32
_EmdConfigHumidityHighSetPoint_Object = MibScalar
emdConfigHumidityHighSetPoint = _EmdConfigHumidityHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 4, 2),
    _EmdConfigHumidityHighSetPoint_Type()
)
emdConfigHumidityHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityHighSetPoint.setStatus("mandatory")


class _EmdConfigHumidityHighStatus_Type(Integer32):
    """Custom type emdConfigHumidityHighStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EmdConfigHumidityHighStatus_Type.__name__ = "Integer32"
_EmdConfigHumidityHighStatus_Object = MibScalar
emdConfigHumidityHighStatus = _EmdConfigHumidityHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 4, 3),
    _EmdConfigHumidityHighStatus_Type()
)
emdConfigHumidityHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityHighStatus.setStatus("mandatory")
_EmdConfigHumidityLowSetPoint_Type = Integer32
_EmdConfigHumidityLowSetPoint_Object = MibScalar
emdConfigHumidityLowSetPoint = _EmdConfigHumidityLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 4, 4),
    _EmdConfigHumidityLowSetPoint_Type()
)
emdConfigHumidityLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityLowSetPoint.setStatus("mandatory")


class _EmdConfigHumidityLowStatus_Type(Integer32):
    """Custom type emdConfigHumidityLowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EmdConfigHumidityLowStatus_Type.__name__ = "Integer32"
_EmdConfigHumidityLowStatus_Object = MibScalar
emdConfigHumidityLowStatus = _EmdConfigHumidityLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 4, 5),
    _EmdConfigHumidityLowStatus_Type()
)
emdConfigHumidityLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityLowStatus.setStatus("mandatory")
_EmdConfigHumidityOffset_Type = Integer32
_EmdConfigHumidityOffset_Object = MibScalar
emdConfigHumidityOffset = _EmdConfigHumidityOffset_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 4, 6),
    _EmdConfigHumidityOffset_Type()
)
emdConfigHumidityOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityOffset.setStatus("mandatory")
_EmdConfigAlarm1_ObjectIdentity = ObjectIdentity
emdConfigAlarm1 = _EmdConfigAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 5)
)


class _EmdConfigAlarm1Name_Type(DisplayString):
    """Custom type emdConfigAlarm1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigAlarm1Name_Type.__name__ = "DisplayString"
_EmdConfigAlarm1Name_Object = MibScalar
emdConfigAlarm1Name = _EmdConfigAlarm1Name_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 5, 1),
    _EmdConfigAlarm1Name_Type()
)
emdConfigAlarm1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigAlarm1Name.setStatus("mandatory")


class _EmdConfigAlarm1Type_Type(Integer32):
    """Custom type emdConfigAlarm1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("nomralOpen", 2),
          ("normalClose", 3))
    )


_EmdConfigAlarm1Type_Type.__name__ = "Integer32"
_EmdConfigAlarm1Type_Object = MibScalar
emdConfigAlarm1Type = _EmdConfigAlarm1Type_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 5, 2),
    _EmdConfigAlarm1Type_Type()
)
emdConfigAlarm1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigAlarm1Type.setStatus("mandatory")
_EmdConfigAlarm2_ObjectIdentity = ObjectIdentity
emdConfigAlarm2 = _EmdConfigAlarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 6)
)


class _EmdConfigAlarm2Name_Type(DisplayString):
    """Custom type emdConfigAlarm2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigAlarm2Name_Type.__name__ = "DisplayString"
_EmdConfigAlarm2Name_Object = MibScalar
emdConfigAlarm2Name = _EmdConfigAlarm2Name_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 6, 1),
    _EmdConfigAlarm2Name_Type()
)
emdConfigAlarm2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigAlarm2Name.setStatus("mandatory")


class _EmdConfigAlarm2Type_Type(Integer32):
    """Custom type emdConfigAlarm2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("nomralOpen", 2),
          ("normalClose", 3))
    )


_EmdConfigAlarm2Type_Type.__name__ = "Integer32"
_EmdConfigAlarm2Type_Object = MibScalar
emdConfigAlarm2Type = _EmdConfigAlarm2Type_Object(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 1, 9, 6, 2),
    _EmdConfigAlarm2Type_Type()
)
emdConfigAlarm2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigAlarm2Type.setStatus("mandatory")
_AtsTrapGroup_ObjectIdentity = ObjectIdentity
atsTrapGroup = _AtsTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2)
)

# Managed Objects groups


# Notification objects

atsAtsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    atsAtsAlarm.setStatus(
        ""
    )

atsSourceAvoltageAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    atsSourceAvoltageAbnormal.setStatus(
        ""
    )

atsSourceBvoltageAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    atsSourceBvoltageAbnormal.setStatus(
        ""
    )

atsSourceAfrequencyAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    atsSourceAfrequencyAbnormal.setStatus(
        ""
    )

atsSourceBfrequencyAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    atsSourceBfrequencyAbnormal.setStatus(
        ""
    )

atsOutputOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    atsOutputOverLoad.setStatus(
        ""
    )

atsWorkPowerAabnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 7)
)
if mibBuilder.loadTexts:
    atsWorkPowerAabnormal.setStatus(
        ""
    )

atsWorkPowerBabnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 8)
)
if mibBuilder.loadTexts:
    atsWorkPowerBabnormal.setStatus(
        ""
    )

atsOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 9)
)
if mibBuilder.loadTexts:
    atsOverTemperature.setStatus(
        ""
    )

atsDcOffsetAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 10)
)
if mibBuilder.loadTexts:
    atsDcOffsetAbnormal.setStatus(
        ""
    )

atsEepromAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 11)
)
if mibBuilder.loadTexts:
    atsEepromAbnormal.setStatus(
        ""
    )

atsLcdNotConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 12)
)
if mibBuilder.loadTexts:
    atsLcdNotConnect.setStatus(
        ""
    )

atsOutputExceedsOverloadTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 13)
)
if mibBuilder.loadTexts:
    atsOutputExceedsOverloadTime.setStatus(
        ""
    )

atsInputPhaseDifference = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 14)
)
if mibBuilder.loadTexts:
    atsInputPhaseDifference.setStatus(
        ""
    )

atsUserSetOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 15)
)
if mibBuilder.loadTexts:
    atsUserSetOverLoad.setStatus(
        ""
    )

atsAtsAlarmToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 16)
)
if mibBuilder.loadTexts:
    atsAtsAlarmToNormal.setStatus(
        ""
    )

atsSourceAvoltageAbnormalToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 17)
)
if mibBuilder.loadTexts:
    atsSourceAvoltageAbnormalToNormal.setStatus(
        ""
    )

atsSourceBvoltageAbnormalToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 18)
)
if mibBuilder.loadTexts:
    atsSourceBvoltageAbnormalToNormal.setStatus(
        ""
    )

atsSourceAfrequencyAbnormalToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 19)
)
if mibBuilder.loadTexts:
    atsSourceAfrequencyAbnormalToNormal.setStatus(
        ""
    )

atsSourceBfrequencyAbnormalToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 20)
)
if mibBuilder.loadTexts:
    atsSourceBfrequencyAbnormalToNormal.setStatus(
        ""
    )

atsOutputOverLoadToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 21)
)
if mibBuilder.loadTexts:
    atsOutputOverLoadToNormal.setStatus(
        ""
    )

atsWorkPowerAabnormalToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 22)
)
if mibBuilder.loadTexts:
    atsWorkPowerAabnormalToNormal.setStatus(
        ""
    )

atsWorkPowerBabnormalToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 23)
)
if mibBuilder.loadTexts:
    atsWorkPowerBabnormalToNormal.setStatus(
        ""
    )

atsOverTemperatureToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 24)
)
if mibBuilder.loadTexts:
    atsOverTemperatureToNormal.setStatus(
        ""
    )

atsDcOffsetAbnormalToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 25)
)
if mibBuilder.loadTexts:
    atsDcOffsetAbnormalToNormal.setStatus(
        ""
    )

atsEepromAbnormalToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 26)
)
if mibBuilder.loadTexts:
    atsEepromAbnormalToNormal.setStatus(
        ""
    )

atsLcdNotConnectToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 27)
)
if mibBuilder.loadTexts:
    atsLcdNotConnectToNormal.setStatus(
        ""
    )

atsOutputExceedsOverloadTimeToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 28)
)
if mibBuilder.loadTexts:
    atsOutputExceedsOverloadTimeToNormal.setStatus(
        ""
    )

atsInputPhaseDifferenceToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 29)
)
if mibBuilder.loadTexts:
    atsInputPhaseDifferenceToNormal.setStatus(
        ""
    )

atsUserSetOverLoadToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 30)
)
if mibBuilder.loadTexts:
    atsUserSetOverLoadToNormal.setStatus(
        ""
    )

atsCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 31)
)
if mibBuilder.loadTexts:
    atsCommunicationLost.setStatus(
        ""
    )

atsCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 32)
)
if mibBuilder.loadTexts:
    atsCommunicationEstablished.setStatus(
        ""
    )

emdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 33)
)
emdTemperatureNotHigh.setObjects(
      *(("ATS-MIB", "emdSatatusTemperature"),
        ("ATS-MIB", "emdConfigTempHighSetPoint"),
        ("ATS-MIB", "emdConfigTempName"))
)
if mibBuilder.loadTexts:
    emdTemperatureNotHigh.setStatus(
        ""
    )

emdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 34)
)
emdTemperatureTooHigh.setObjects(
      *(("ATS-MIB", "emdSatatusTemperature"),
        ("ATS-MIB", "emdConfigTempHighSetPoint"),
        ("ATS-MIB", "emdConfigTempName"))
)
if mibBuilder.loadTexts:
    emdTemperatureTooHigh.setStatus(
        ""
    )

emdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 35)
)
emdTemperatureNotLow.setObjects(
      *(("ATS-MIB", "emdSatatusTemperature"),
        ("ATS-MIB", "emdConfigTempLowSetPoint"),
        ("ATS-MIB", "emdConfigTempName"))
)
if mibBuilder.loadTexts:
    emdTemperatureNotLow.setStatus(
        ""
    )

emdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 36)
)
emdTemperatureTooLow.setObjects(
      *(("ATS-MIB", "emdSatatusTemperature"),
        ("ATS-MIB", "emdConfigTempLowSetPoint"),
        ("ATS-MIB", "emdConfigTempName"))
)
if mibBuilder.loadTexts:
    emdTemperatureTooLow.setStatus(
        ""
    )

emdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 37)
)
emdHumidityNotHigh.setObjects(
      *(("ATS-MIB", "emdSatatusHumidity"),
        ("ATS-MIB", "emdConfigHumidityHighSetPoint"),
        ("ATS-MIB", "emdConfigHumidityName"))
)
if mibBuilder.loadTexts:
    emdHumidityNotHigh.setStatus(
        ""
    )

emdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 38)
)
emdHumidityTooHigh.setObjects(
      *(("ATS-MIB", "emdSatatusHumidity"),
        ("ATS-MIB", "emdConfigHumidityHighSetPoint"),
        ("ATS-MIB", "emdConfigHumidityName"))
)
if mibBuilder.loadTexts:
    emdHumidityTooHigh.setStatus(
        ""
    )

emdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 39)
)
emdHumidityNotLow.setObjects(
      *(("ATS-MIB", "emdSatatusHumidity"),
        ("ATS-MIB", "emdConfigHumidityLowSetPoint"),
        ("ATS-MIB", "emdConfigHumidityName"))
)
if mibBuilder.loadTexts:
    emdHumidityNotLow.setStatus(
        ""
    )

emdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 40)
)
emdHumidityTooLow.setObjects(
      *(("ATS-MIB", "emdSatatusHumidity"),
        ("ATS-MIB", "emdConfigHumidityLowSetPoint"),
        ("ATS-MIB", "emdConfigHumidityName"))
)
if mibBuilder.loadTexts:
    emdHumidityTooLow.setStatus(
        ""
    )

emdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 41)
)
emdAlarm1Normal.setObjects(
      *(("ATS-MIB", "emdConfigAlarm1Type"),
        ("ATS-MIB", "emdConfigAlarm1Name"))
)
if mibBuilder.loadTexts:
    emdAlarm1Normal.setStatus(
        ""
    )

emdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 42)
)
emdAlarm1Active.setObjects(
      *(("ATS-MIB", "emdConfigAlarm1Type"),
        ("ATS-MIB", "emdConfigAlarm1Name"))
)
if mibBuilder.loadTexts:
    emdAlarm1Active.setStatus(
        ""
    )

emdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 43)
)
emdAlarm2Normal.setObjects(
      *(("ATS-MIB", "emdConfigAlarm2Type"),
        ("ATS-MIB", "emdConfigAlarm2Name"))
)
if mibBuilder.loadTexts:
    emdAlarm2Normal.setStatus(
        ""
    )

emdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 37662, 1, 2, 2, 1, 2, 0, 44)
)
emdAlarm2Active.setObjects(
      *(("ATS-MIB", "emdConfigAlarm2Type"),
        ("ATS-MIB", "emdConfigAlarm2Name"))
)
if mibBuilder.loadTexts:
    emdAlarm2Active.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATS-MIB",
    **{"ats": ats,
       "product": product,
       "webAppliance": webAppliance,
       "atsAgent": atsAgent,
       "single": single,
       "atsObjectGroup": atsObjectGroup,
       "atsIdentGroup": atsIdentGroup,
       "atsIdentGroupModel": atsIdentGroupModel,
       "atsIdentGroupSerialNumber": atsIdentGroupSerialNumber,
       "atsIdentGroupManufacturer": atsIdentGroupManufacturer,
       "atsIdentGroupFirmwareRevision": atsIdentGroupFirmwareRevision,
       "atsIdentGroupAgentFirmwareRevision": atsIdentGroupAgentFirmwareRevision,
       "atsInputGroup": atsInputGroup,
       "atsInputGroupPreference": atsInputGroupPreference,
       "atsInputGroupSourceAstatus": atsInputGroupSourceAstatus,
       "atsInputGroupSourceAinputVoltage": atsInputGroupSourceAinputVoltage,
       "atsInputGroupSourceAinputFrequency": atsInputGroupSourceAinputFrequency,
       "atsInputGroupSourceBstatus": atsInputGroupSourceBstatus,
       "atsInputGroupSourceBinputVoltage": atsInputGroupSourceBinputVoltage,
       "atsInputGroupSourceBinputFrequency": atsInputGroupSourceBinputFrequency,
       "atsInputGroupSourceAvoltageUpperLimit": atsInputGroupSourceAvoltageUpperLimit,
       "atsInputGroupSourceAvoltageLowerLimit": atsInputGroupSourceAvoltageLowerLimit,
       "atsInputGroupSourceAfrequencyUpperLimit": atsInputGroupSourceAfrequencyUpperLimit,
       "atsInputGroupSourceAfrequencyLowerLimit": atsInputGroupSourceAfrequencyLowerLimit,
       "atsInputGroupSourceBvoltageUpperLimit": atsInputGroupSourceBvoltageUpperLimit,
       "atsInputGroupSourceBvoltageLowerLimit": atsInputGroupSourceBvoltageLowerLimit,
       "atsInputGroupSourceBfrequencyUpperLimit": atsInputGroupSourceBfrequencyUpperLimit,
       "atsInputGroupSourceBfrequencyLowerLimit": atsInputGroupSourceBfrequencyLowerLimit,
       "atsOutputGroup": atsOutputGroup,
       "atsOutputGroupOutputSource": atsOutputGroupOutputSource,
       "atsOutputGroupOutputVoltage": atsOutputGroupOutputVoltage,
       "atsOutputGroupOutputFequency": atsOutputGroupOutputFequency,
       "atsOutputGroupOutputCurrent": atsOutputGroupOutputCurrent,
       "atsOutputGroupLoad": atsOutputGroupLoad,
       "atsHmiSwitchGroup": atsHmiSwitchGroup,
       "atsHmiSwitchGroupBuzzer": atsHmiSwitchGroupBuzzer,
       "atsHmiSwitchGroupAtsAlarm": atsHmiSwitchGroupAtsAlarm,
       "atsHmiSwitchGroupAutoReturn": atsHmiSwitchGroupAutoReturn,
       "atsHmiSwitchGroupSourceTransferByLoad": atsHmiSwitchGroupSourceTransferByLoad,
       "atsHmiSwitchGroupSourceTransferByPhase": atsHmiSwitchGroupSourceTransferByPhase,
       "atsMiscellaneousGroup": atsMiscellaneousGroup,
       "atsMiscellaneousGroupAtsSystemTemperture": atsMiscellaneousGroupAtsSystemTemperture,
       "atsMiscellaneousGroupSystemMaxCurrent": atsMiscellaneousGroupSystemMaxCurrent,
       "atsControlGroup": atsControlGroup,
       "atsControlGroupBuzzerAlarmControl": atsControlGroupBuzzerAlarmControl,
       "atsControlGroupManualTransfer": atsControlGroupManualTransfer,
       "agentConfig": agentConfig,
       "agentConfigIpaddress": agentConfigIpaddress,
       "agentConfigGateway": agentConfigGateway,
       "agentConfigSubnetMask": agentConfigSubnetMask,
       "agentConfigDate": agentConfigDate,
       "agentConfigTime": agentConfigTime,
       "agentConfigHistoryLogFrequency": agentConfigHistoryLogFrequency,
       "agentConfigExtHistoryLogFrequency": agentConfigExtHistoryLogFrequency,
       "agentConfigPollRate": agentConfigPollRate,
       "agentConfigBaudRate": agentConfigBaudRate,
       "agentConfigDhcpStatue": agentConfigDhcpStatue,
       "agentConfigTelnetStatue": agentConfigTelnetStatue,
       "agentConfigTftpStatue": agentConfigTftpStatue,
       "agentConfigResetToDefault": agentConfigResetToDefault,
       "agentConfigRestart": agentConfigRestart,
       "agentConfigClearAgentLog": agentConfigClearAgentLog,
       "agentConfigClearEventLog": agentConfigClearEventLog,
       "agentConfigClearExtHistoryLog": agentConfigClearExtHistoryLog,
       "agentConfigClearHistoryLog": agentConfigClearHistoryLog,
       "agentConfigTrapRetryCount": agentConfigTrapRetryCount,
       "agentConfigTrapRetryTime": agentConfigTrapRetryTime,
       "agentConfigTrapAckSignature": agentConfigTrapAckSignature,
       "agentConfigMibVersion": agentConfigMibVersion,
       "agentConfigTrapsReceiversTable": agentConfigTrapsReceiversTable,
       "agentConfigTrapsReceiversEntry": agentConfigTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "receiverNmsType": receiverNmsType,
       "receiverSeverityLevel": receiverSeverityLevel,
       "receiverDescription": receiverDescription,
       "agentConfigAccessControlTable": agentConfigAccessControlTable,
       "agentConfigAccessControlEntry": agentConfigAccessControlEntry,
       "accessIndex": accessIndex,
       "accessControlAddr": accessControlAddr,
       "accessCommunityString": accessCommunityString,
       "accessControlMode": accessControlMode,
       "agentConfigDefaultLanguage": agentConfigDefaultLanguage,
       "agentConfigIPv6AddrStatus": agentConfigIPv6AddrStatus,
       "agentConfigIPv6AddrAutoConfig": agentConfigIPv6AddrAutoConfig,
       "agentConfigIPv6LinkLocalAddr": agentConfigIPv6LinkLocalAddr,
       "agentConfigIPv6GlobalAddr": agentConfigIPv6GlobalAddr,
       "agentConfigIPv6PrefixlLength": agentConfigIPv6PrefixlLength,
       "agentConfigIPv6DefaultRouter": agentConfigIPv6DefaultRouter,
       "emdStatus": emdStatus,
       "emdSatatusEmdType": emdSatatusEmdType,
       "emdSatatusTemperature": emdSatatusTemperature,
       "emdSatatusHumidity": emdSatatusHumidity,
       "emdSatatusAlarm1": emdSatatusAlarm1,
       "emdSatatusAlarm2": emdSatatusAlarm2,
       "emdConfig": emdConfig,
       "usahEmdConfigEmdConfig": usahEmdConfigEmdConfig,
       "emdConfigEmdName": emdConfigEmdName,
       "emdConfigTemperature": emdConfigTemperature,
       "emdConfigTempName": emdConfigTempName,
       "emdConfigTempHighSetPoint": emdConfigTempHighSetPoint,
       "emdConfigTempHighStatus": emdConfigTempHighStatus,
       "emdConfigTempLowSetPoint": emdConfigTempLowSetPoint,
       "emdConfigTempLowStatus": emdConfigTempLowStatus,
       "emdConfigTempOffset": emdConfigTempOffset,
       "emdConfigHumidity": emdConfigHumidity,
       "emdConfigHumidityName": emdConfigHumidityName,
       "emdConfigHumidityHighSetPoint": emdConfigHumidityHighSetPoint,
       "emdConfigHumidityHighStatus": emdConfigHumidityHighStatus,
       "emdConfigHumidityLowSetPoint": emdConfigHumidityLowSetPoint,
       "emdConfigHumidityLowStatus": emdConfigHumidityLowStatus,
       "emdConfigHumidityOffset": emdConfigHumidityOffset,
       "emdConfigAlarm1": emdConfigAlarm1,
       "emdConfigAlarm1Name": emdConfigAlarm1Name,
       "emdConfigAlarm1Type": emdConfigAlarm1Type,
       "emdConfigAlarm2": emdConfigAlarm2,
       "emdConfigAlarm2Name": emdConfigAlarm2Name,
       "emdConfigAlarm2Type": emdConfigAlarm2Type,
       "atsTrapGroup": atsTrapGroup,
       "atsAtsAlarm": atsAtsAlarm,
       "atsSourceAvoltageAbnormal": atsSourceAvoltageAbnormal,
       "atsSourceBvoltageAbnormal": atsSourceBvoltageAbnormal,
       "atsSourceAfrequencyAbnormal": atsSourceAfrequencyAbnormal,
       "atsSourceBfrequencyAbnormal": atsSourceBfrequencyAbnormal,
       "atsOutputOverLoad": atsOutputOverLoad,
       "atsWorkPowerAabnormal": atsWorkPowerAabnormal,
       "atsWorkPowerBabnormal": atsWorkPowerBabnormal,
       "atsOverTemperature": atsOverTemperature,
       "atsDcOffsetAbnormal": atsDcOffsetAbnormal,
       "atsEepromAbnormal": atsEepromAbnormal,
       "atsLcdNotConnect": atsLcdNotConnect,
       "atsOutputExceedsOverloadTime": atsOutputExceedsOverloadTime,
       "atsInputPhaseDifference": atsInputPhaseDifference,
       "atsUserSetOverLoad": atsUserSetOverLoad,
       "atsAtsAlarmToNormal": atsAtsAlarmToNormal,
       "atsSourceAvoltageAbnormalToNormal": atsSourceAvoltageAbnormalToNormal,
       "atsSourceBvoltageAbnormalToNormal": atsSourceBvoltageAbnormalToNormal,
       "atsSourceAfrequencyAbnormalToNormal": atsSourceAfrequencyAbnormalToNormal,
       "atsSourceBfrequencyAbnormalToNormal": atsSourceBfrequencyAbnormalToNormal,
       "atsOutputOverLoadToNormal": atsOutputOverLoadToNormal,
       "atsWorkPowerAabnormalToNormal": atsWorkPowerAabnormalToNormal,
       "atsWorkPowerBabnormalToNormal": atsWorkPowerBabnormalToNormal,
       "atsOverTemperatureToNormal": atsOverTemperatureToNormal,
       "atsDcOffsetAbnormalToNormal": atsDcOffsetAbnormalToNormal,
       "atsEepromAbnormalToNormal": atsEepromAbnormalToNormal,
       "atsLcdNotConnectToNormal": atsLcdNotConnectToNormal,
       "atsOutputExceedsOverloadTimeToNormal": atsOutputExceedsOverloadTimeToNormal,
       "atsInputPhaseDifferenceToNormal": atsInputPhaseDifferenceToNormal,
       "atsUserSetOverLoadToNormal": atsUserSetOverLoadToNormal,
       "atsCommunicationLost": atsCommunicationLost,
       "atsCommunicationEstablished": atsCommunicationEstablished,
       "emdTemperatureNotHigh": emdTemperatureNotHigh,
       "emdTemperatureTooHigh": emdTemperatureTooHigh,
       "emdTemperatureNotLow": emdTemperatureNotLow,
       "emdTemperatureTooLow": emdTemperatureTooLow,
       "emdHumidityNotHigh": emdHumidityNotHigh,
       "emdHumidityTooHigh": emdHumidityTooHigh,
       "emdHumidityNotLow": emdHumidityNotLow,
       "emdHumidityTooLow": emdHumidityTooLow,
       "emdAlarm1Normal": emdAlarm1Normal,
       "emdAlarm1Active": emdAlarm1Active,
       "emdAlarm2Normal": emdAlarm2Normal,
       "emdAlarm2Active": emdAlarm2Active}
)
