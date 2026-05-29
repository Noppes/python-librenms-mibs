# SNMP MIB module (G6-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsens\G6-SFP-MIB

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

_Sfp_ObjectIdentity = ObjectIdentity
sfp = _Sfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34)
)
_ConfigTable_Object = MibTable
configTable = _ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 1)
)
if mibBuilder.loadTexts:
    configTable.setStatus("current")
_ConfigEntry_Object = MibTableRow
configEntry = _ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 1, 1)
)
configEntry.setIndexNames(
    (0, "G6-SFP-MIB", "configIndex"),
)
if mibBuilder.loadTexts:
    configEntry.setStatus("current")


class _ConfigIndex_Type(Integer32):
    """Custom type configIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ConfigIndex_Type.__name__ = "Integer32"
_ConfigIndex_Object = MibTableColumn
configIndex = _ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 1, 1, 1),
    _ConfigIndex_Type()
)
configIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configIndex.setStatus("current")


class _ConfigLossOfSignalEvent_Type(Integer32):
    """Custom type configLossOfSignalEvent based on Integer32"""
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


_ConfigLossOfSignalEvent_Type.__name__ = "Integer32"
_ConfigLossOfSignalEvent_Object = MibTableColumn
configLossOfSignalEvent = _ConfigLossOfSignalEvent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 1, 1, 2),
    _ConfigLossOfSignalEvent_Type()
)
configLossOfSignalEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLossOfSignalEvent.setStatus("current")


class _ConfigOpticalDeltaDetect_Type(Integer32):
    """Custom type configOpticalDeltaDetect based on Integer32"""
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


_ConfigOpticalDeltaDetect_Type.__name__ = "Integer32"
_ConfigOpticalDeltaDetect_Object = MibTableColumn
configOpticalDeltaDetect = _ConfigOpticalDeltaDetect_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 1, 1, 3),
    _ConfigOpticalDeltaDetect_Type()
)
configOpticalDeltaDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configOpticalDeltaDetect.setStatus("current")


class _ConfigDeltaThreshold_Type(Integer32):
    """Custom type configDeltaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigDeltaThreshold_Type.__name__ = "Integer32"
_ConfigDeltaThreshold_Object = MibTableColumn
configDeltaThreshold = _ConfigDeltaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 1, 1, 4),
    _ConfigDeltaThreshold_Type()
)
configDeltaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDeltaThreshold.setStatus("current")
_InformationTable_Object = MibTable
informationTable = _InformationTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100)
)
if mibBuilder.loadTexts:
    informationTable.setStatus("current")
_InformationEntry_Object = MibTableRow
informationEntry = _InformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1)
)
informationEntry.setIndexNames(
    (0, "G6-SFP-MIB", "informationPortIndex"),
)
if mibBuilder.loadTexts:
    informationEntry.setStatus("current")


class _InformationPortIndex_Type(Integer32):
    """Custom type informationPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_InformationPortIndex_Type.__name__ = "Integer32"
_InformationPortIndex_Object = MibTableColumn
informationPortIndex = _InformationPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 1),
    _InformationPortIndex_Type()
)
informationPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    informationPortIndex.setStatus("current")


class _InformationPort_Type(OctetString):
    """Custom type informationPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_InformationPort_Type.__name__ = "OctetString"
_InformationPort_Object = MibTableColumn
informationPort = _InformationPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 2),
    _InformationPort_Type()
)
informationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationPort.setStatus("current")
_InformationLocation_Type = DisplayString
_InformationLocation_Object = MibTableColumn
informationLocation = _InformationLocation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 3),
    _InformationLocation_Type()
)
informationLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationLocation.setStatus("current")


class _InformationStatus_Type(Bits):
    """Custom type informationStatus based on Bits"""
    namedValues = NamedValues(
        *(("ok", 0),
          ("laserDisabled", 1),
          ("lossOfSignal", 2),
          ("txFailure", 3),
          ("readError", 4))
    )

_InformationStatus_Type.__name__ = "Bits"
_InformationStatus_Object = MibTableColumn
informationStatus = _InformationStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 4),
    _InformationStatus_Type()
)
informationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationStatus.setStatus("current")


class _InformationType_Type(Integer32):
    """Custom type informationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("unknown", 1),
          ("sfp", 2),
          ("gbic", 3),
          ("sff", 4),
          ("dwdmSfp", 5),
          ("xfp", 7),
          ("csfpA", 8),
          ("csfpB", 9),
          ("dwdmXfp", 10),
          ("sfpPlus", 11))
    )


_InformationType_Type.__name__ = "Integer32"
_InformationType_Object = MibTableColumn
informationType = _InformationType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 5),
    _InformationType_Type()
)
informationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationType.setStatus("current")


class _InformationConnector_Type(Integer32):
    """Custom type informationConnector based on Integer32"""
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
        *(("unknown", 0),
          ("lc", 1),
          ("sc", 2),
          ("mtRj", 3),
          ("rj45", 4),
          ("mu", 5))
    )


_InformationConnector_Type.__name__ = "Integer32"
_InformationConnector_Object = MibTableColumn
informationConnector = _InformationConnector_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 6),
    _InformationConnector_Type()
)
informationConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationConnector.setStatus("current")
_InformationWavelength_Type = DisplayString
_InformationWavelength_Object = MibTableColumn
informationWavelength = _InformationWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 7),
    _InformationWavelength_Type()
)
informationWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationWavelength.setStatus("current")
_InformationTxTechnology_Type = DisplayString
_InformationTxTechnology_Object = MibTableColumn
informationTxTechnology = _InformationTxTechnology_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 8),
    _InformationTxTechnology_Type()
)
informationTxTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationTxTechnology.setStatus("current")
_InformationRxTechnology_Type = DisplayString
_InformationRxTechnology_Object = MibTableColumn
informationRxTechnology = _InformationRxTechnology_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 9),
    _InformationRxTechnology_Type()
)
informationRxTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationRxTechnology.setStatus("current")
_InformationNominalBitrate_Type = DisplayString
_InformationNominalBitrate_Object = MibTableColumn
informationNominalBitrate = _InformationNominalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 10),
    _InformationNominalBitrate_Type()
)
informationNominalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationNominalBitrate.setStatus("current")
_InformationManufacturer_Type = DisplayString
_InformationManufacturer_Object = MibTableColumn
informationManufacturer = _InformationManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 11),
    _InformationManufacturer_Type()
)
informationManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationManufacturer.setStatus("current")
_InformationPartNumber_Type = DisplayString
_InformationPartNumber_Object = MibTableColumn
informationPartNumber = _InformationPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 12),
    _InformationPartNumber_Type()
)
informationPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationPartNumber.setStatus("current")
_InformationRevision_Type = DisplayString
_InformationRevision_Object = MibTableColumn
informationRevision = _InformationRevision_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 13),
    _InformationRevision_Type()
)
informationRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationRevision.setStatus("current")
_InformationSerialNumber_Type = DisplayString
_InformationSerialNumber_Object = MibTableColumn
informationSerialNumber = _InformationSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 14),
    _InformationSerialNumber_Type()
)
informationSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationSerialNumber.setStatus("current")
_InformationMfgDateCode_Type = DisplayString
_InformationMfgDateCode_Object = MibTableColumn
informationMfgDateCode = _InformationMfgDateCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 15),
    _InformationMfgDateCode_Type()
)
informationMfgDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationMfgDateCode.setStatus("current")


class _InformationWarnings_Type(Bits):
    """Custom type informationWarnings based on Bits"""
    namedValues = NamedValues(
        *(("txPowerLow", 0),
          ("txPowerHigh", 1),
          ("txBiasLow", 2),
          ("txBiasHigh", 3),
          ("vccLow", 4),
          ("vccHigh", 5),
          ("tempLow", 6),
          ("tempHigh", 7),
          ("rxPowerLow", 8),
          ("rxPowerHigh", 9))
    )

_InformationWarnings_Type.__name__ = "Bits"
_InformationWarnings_Object = MibTableColumn
informationWarnings = _InformationWarnings_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 16),
    _InformationWarnings_Type()
)
informationWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationWarnings.setStatus("current")


class _InformationAlarms_Type(Bits):
    """Custom type informationAlarms based on Bits"""
    namedValues = NamedValues(
        *(("txPowerTooLow", 0),
          ("txPowerTooHigh", 1),
          ("txBiasTooLow", 2),
          ("txBiasTooHigh", 3),
          ("vccTooLow", 4),
          ("vccTooHigh", 5),
          ("tempTooLow", 6),
          ("tempTooHigh", 7),
          ("rxPowerTooLow", 8),
          ("rxPowerTooHigh", 9))
    )

_InformationAlarms_Type.__name__ = "Bits"
_InformationAlarms_Object = MibTableColumn
informationAlarms = _InformationAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 17),
    _InformationAlarms_Type()
)
informationAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationAlarms.setStatus("current")
_InformationTxPower_Type = DisplayString
_InformationTxPower_Object = MibTableColumn
informationTxPower = _InformationTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 18),
    _InformationTxPower_Type()
)
informationTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationTxPower.setStatus("current")
_InformationRxPower_Type = DisplayString
_InformationRxPower_Object = MibTableColumn
informationRxPower = _InformationRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 19),
    _InformationRxPower_Type()
)
informationRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationRxPower.setStatus("current")
_InformationTemperature_Type = DisplayString
_InformationTemperature_Object = MibTableColumn
informationTemperature = _InformationTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 20),
    _InformationTemperature_Type()
)
informationTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationTemperature.setStatus("current")
_InformationMaxLength9Um_Type = DisplayString
_InformationMaxLength9Um_Object = MibTableColumn
informationMaxLength9Um = _InformationMaxLength9Um_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 21),
    _InformationMaxLength9Um_Type()
)
informationMaxLength9Um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationMaxLength9Um.setStatus("current")
_InformationMaxLength50Um_Type = DisplayString
_InformationMaxLength50Um_Object = MibTableColumn
informationMaxLength50Um = _InformationMaxLength50Um_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 22),
    _InformationMaxLength50Um_Type()
)
informationMaxLength50Um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationMaxLength50Um.setStatus("current")
_InformationMaxLength62Um_Type = DisplayString
_InformationMaxLength62Um_Object = MibTableColumn
informationMaxLength62Um = _InformationMaxLength62Um_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 23),
    _InformationMaxLength62Um_Type()
)
informationMaxLength62Um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationMaxLength62Um.setStatus("current")
_InformationMaxLengthCopper_Type = DisplayString
_InformationMaxLengthCopper_Object = MibTableColumn
informationMaxLengthCopper = _InformationMaxLengthCopper_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 24),
    _InformationMaxLengthCopper_Type()
)
informationMaxLengthCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationMaxLengthCopper.setStatus("current")
_InformationTuningRange_Type = DisplayString
_InformationTuningRange_Object = MibTableColumn
informationTuningRange = _InformationTuningRange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 25),
    _InformationTuningRange_Type()
)
informationTuningRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationTuningRange.setStatus("current")
_InformationPowerConsumption_Type = DisplayString
_InformationPowerConsumption_Object = MibTableColumn
informationPowerConsumption = _InformationPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 26),
    _InformationPowerConsumption_Type()
)
informationPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationPowerConsumption.setStatus("current")
_InformationAdditionalInformation_Type = DisplayString
_InformationAdditionalInformation_Object = MibTableColumn
informationAdditionalInformation = _InformationAdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 34, 100, 1, 27),
    _InformationAdditionalInformation_Type()
)
informationAdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationAdditionalInformation.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-SFP-MIB",
    **{"device": device,
       "sfp": sfp,
       "configTable": configTable,
       "configEntry": configEntry,
       "configIndex": configIndex,
       "configLossOfSignalEvent": configLossOfSignalEvent,
       "configOpticalDeltaDetect": configOpticalDeltaDetect,
       "configDeltaThreshold": configDeltaThreshold,
       "informationTable": informationTable,
       "informationEntry": informationEntry,
       "informationPortIndex": informationPortIndex,
       "informationPort": informationPort,
       "informationLocation": informationLocation,
       "informationStatus": informationStatus,
       "informationType": informationType,
       "informationConnector": informationConnector,
       "informationWavelength": informationWavelength,
       "informationTxTechnology": informationTxTechnology,
       "informationRxTechnology": informationRxTechnology,
       "informationNominalBitrate": informationNominalBitrate,
       "informationManufacturer": informationManufacturer,
       "informationPartNumber": informationPartNumber,
       "informationRevision": informationRevision,
       "informationSerialNumber": informationSerialNumber,
       "informationMfgDateCode": informationMfgDateCode,
       "informationWarnings": informationWarnings,
       "informationAlarms": informationAlarms,
       "informationTxPower": informationTxPower,
       "informationRxPower": informationRxPower,
       "informationTemperature": informationTemperature,
       "informationMaxLength9Um": informationMaxLength9Um,
       "informationMaxLength50Um": informationMaxLength50Um,
       "informationMaxLength62Um": informationMaxLength62Um,
       "informationMaxLengthCopper": informationMaxLengthCopper,
       "informationTuningRange": informationTuningRange,
       "informationPowerConsumption": informationPowerConsumption,
       "informationAdditionalInformation": informationAdditionalInformation}
)
