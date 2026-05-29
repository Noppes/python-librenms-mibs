# SNMP MIB module (SOCOMECUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\socomec\SOCOMECUPS-MIB

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class NonNegativeInteger(Integer32):
    """Custom type NonNegativeInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Socomec_ObjectIdentity = ObjectIdentity
socomec = _Socomec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1)
)
_Netvision7_ObjectIdentity = ObjectIdentity
netvision7 = _Netvision7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7)
)
_UpsObjects_ObjectIdentity = ObjectIdentity
upsObjects = _UpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 1)
)


class _UpsIdentModel_Type(DisplayString):
    """Custom type upsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentModel_Type.__name__ = "DisplayString"
_UpsIdentModel_Object = MibScalar
upsIdentModel = _UpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 1, 1),
    _UpsIdentModel_Type()
)
upsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModel.setStatus("mandatory")


class _UpsIdentSerialNumber_Type(DisplayString):
    """Custom type upsIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_UpsIdentSerialNumber_Type.__name__ = "DisplayString"
_UpsIdentSerialNumber_Object = MibScalar
upsIdentSerialNumber = _UpsIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 1, 2),
    _UpsIdentSerialNumber_Type()
)
upsIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentSerialNumber.setStatus("mandatory")


class _UpsIdentUserRef_Type(DisplayString):
    """Custom type upsIdentUserRef based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_UpsIdentUserRef_Type.__name__ = "DisplayString"
_UpsIdentUserRef_Object = MibScalar
upsIdentUserRef = _UpsIdentUserRef_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 1, 3),
    _UpsIdentUserRef_Type()
)
upsIdentUserRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUserRef.setStatus("mandatory")


class _UpsIdentUserLocation_Type(DisplayString):
    """Custom type upsIdentUserLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_UpsIdentUserLocation_Type.__name__ = "DisplayString"
_UpsIdentUserLocation_Object = MibScalar
upsIdentUserLocation = _UpsIdentUserLocation_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 1, 4),
    _UpsIdentUserLocation_Type()
)
upsIdentUserLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUserLocation.setStatus("mandatory")


class _UpsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type upsIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_UpsIdentAgentSoftwareVersion_Object = MibScalar
upsIdentAgentSoftwareVersion = _UpsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 1, 5),
    _UpsIdentAgentSoftwareVersion_Type()
)
upsIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersion.setStatus("mandatory")


class _UpsSystemName_Type(DisplayString):
    """Custom type upsSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UpsSystemName_Type.__name__ = "DisplayString"
_UpsSystemName_Object = MibScalar
upsSystemName = _UpsSystemName_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 1, 6),
    _UpsSystemName_Type()
)
upsSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSystemName.setStatus("mandatory")


class _UpsSystemContact_Type(DisplayString):
    """Custom type upsSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UpsSystemContact_Type.__name__ = "DisplayString"
_UpsSystemContact_Object = MibScalar
upsSystemContact = _UpsSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 1, 7),
    _UpsSystemContact_Type()
)
upsSystemContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSystemContact.setStatus("mandatory")


class _UpsSystemLocation_Type(DisplayString):
    """Custom type upsSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UpsSystemLocation_Type.__name__ = "DisplayString"
_UpsSystemLocation_Object = MibScalar
upsSystemLocation = _UpsSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 1, 8),
    _UpsSystemLocation_Type()
)
upsSystemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSystemLocation.setStatus("mandatory")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2)
)


class _UpsBatteryStatus_Type(Integer32):
    """Custom type upsBatteryStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("batteryNormal", 2),
          ("batteryCharging", 3),
          ("batteryTest", 4),
          ("batteryDischarging", 5),
          ("batteryLow", 6),
          ("batteryDepleted", 7),
          ("batteryFailure", 8),
          ("batteryDisconnected", 9))
    )


_UpsBatteryStatus_Type.__name__ = "Integer32"
_UpsBatteryStatus_Object = MibScalar
upsBatteryStatus = _UpsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2, 1),
    _UpsBatteryStatus_Type()
)
upsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatus.setStatus("mandatory")
_UpsSecondsOnBattery_Type = Integer32
_UpsSecondsOnBattery_Object = MibScalar
upsSecondsOnBattery = _UpsSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2, 2),
    _UpsSecondsOnBattery_Type()
)
upsSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBattery.setStatus("mandatory")
_UpsEstimatedMinutesRemaining_Type = Integer32
_UpsEstimatedMinutesRemaining_Object = MibScalar
upsEstimatedMinutesRemaining = _UpsEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2, 3),
    _UpsEstimatedMinutesRemaining_Type()
)
upsEstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemaining.setStatus("mandatory")
_UpsEstimatedChargeRemaining_Type = Integer32
_UpsEstimatedChargeRemaining_Object = MibScalar
upsEstimatedChargeRemaining = _UpsEstimatedChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2, 4),
    _UpsEstimatedChargeRemaining_Type()
)
upsEstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemaining.setStatus("mandatory")
_UpsBatteryVoltage_Type = Integer32
_UpsBatteryVoltage_Object = MibScalar
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2, 5),
    _UpsBatteryVoltage_Type()
)
upsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setStatus("mandatory")
_UpsBatteryTemperature_Type = Integer32
_UpsBatteryTemperature_Object = MibScalar
upsBatteryTemperature = _UpsBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2, 6),
    _UpsBatteryTemperature_Type()
)
upsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setStatus("mandatory")
_UpsAmbientTemperature_Type = Integer32
_UpsAmbientTemperature_Object = MibScalar
upsAmbientTemperature = _UpsAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2, 7),
    _UpsAmbientTemperature_Type()
)
upsAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientTemperature.setStatus("mandatory")
_UpsBatteryCurrent_Type = Integer32
_UpsBatteryCurrent_Object = MibScalar
upsBatteryCurrent = _UpsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2, 8),
    _UpsBatteryCurrent_Type()
)
upsBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrent.setStatus("mandatory")
_UpsBatterySOC_Type = Integer32
_UpsBatterySOC_Object = MibScalar
upsBatterySOC = _UpsBatterySOC_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 2, 9),
    _UpsBatterySOC_Type()
)
upsBatterySOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatterySOC.setStatus("mandatory")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3)
)
_UpsInputNumLines_Type = Integer32
_UpsInputNumLines_Object = MibScalar
upsInputNumLines = _UpsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3, 1),
    _UpsInputNumLines_Type()
)
upsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLines.setStatus("mandatory")
_UpsInputFrequency_Type = Integer32
_UpsInputFrequency_Object = MibScalar
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3, 2),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("mandatory")
_UpsInputTable_Object = MibTable
upsInputTable = _UpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputTable.setStatus("mandatory")
_UpsInputEntry_Object = MibTableRow
upsInputEntry = _UpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3, 3, 1)
)
upsInputEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsInputLineIndex"),
)
if mibBuilder.loadTexts:
    upsInputEntry.setStatus("mandatory")


class _UpsInputLineIndex_Type(Integer32):
    """Custom type upsInputLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsInputLineIndex_Type.__name__ = "Integer32"
_UpsInputLineIndex_Object = MibTableColumn
upsInputLineIndex = _UpsInputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3, 3, 1, 1),
    _UpsInputLineIndex_Type()
)
upsInputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineIndex.setStatus("mandatory")
_UpsInputVoltage_Type = Integer32
_UpsInputVoltage_Object = MibTableColumn
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3, 3, 1, 2),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("mandatory")
_UpsInputCurrent_Type = Integer32
_UpsInputCurrent_Object = MibTableColumn
upsInputCurrent = _UpsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3, 3, 1, 3),
    _UpsInputCurrent_Type()
)
upsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrent.setStatus("mandatory")
_UpsInputVoltageMax_Type = Integer32
_UpsInputVoltageMax_Object = MibTableColumn
upsInputVoltageMax = _UpsInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3, 3, 1, 4),
    _UpsInputVoltageMax_Type()
)
upsInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMax.setStatus("mandatory")
_UpsInputVoltageMin_Type = Integer32
_UpsInputVoltageMin_Object = MibTableColumn
upsInputVoltageMin = _UpsInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 3, 3, 1, 5),
    _UpsInputVoltageMin_Type()
)
upsInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMin.setStatus("mandatory")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4)
)


class _UpsOutputSource_Type(Integer32):
    """Custom type upsOutputSource based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("onMaintenBypass", 2),
          ("onInverter", 3),
          ("normalMode", 4),
          ("ecoMode", 5),
          ("onBypass", 6),
          ("standby", 7),
          ("upsOff", 8),
          ("lineInteractive", 9),
          ("flexMode", 10))
    )


_UpsOutputSource_Type.__name__ = "Integer32"
_UpsOutputSource_Object = MibScalar
upsOutputSource = _UpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 1),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("mandatory")
_UpsOutputFrequency_Type = Integer32
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 2),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("mandatory")
_UpsOutputNumLines_Type = Integer32
_UpsOutputNumLines_Object = MibScalar
upsOutputNumLines = _UpsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 3),
    _UpsOutputNumLines_Type()
)
upsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLines.setStatus("mandatory")
_UpsOutputTable_Object = MibTable
upsOutputTable = _UpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputTable.setStatus("mandatory")
_UpsOutputEntry_Object = MibTableRow
upsOutputEntry = _UpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 4, 1)
)
upsOutputEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    upsOutputEntry.setStatus("mandatory")


class _UpsOutputLineIndex_Type(Integer32):
    """Custom type upsOutputLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsOutputLineIndex_Type.__name__ = "Integer32"
_UpsOutputLineIndex_Object = MibTableColumn
upsOutputLineIndex = _UpsOutputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 4, 1, 1),
    _UpsOutputLineIndex_Type()
)
upsOutputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputLineIndex.setStatus("mandatory")
_UpsOutputVoltage_Type = Integer32
_UpsOutputVoltage_Object = MibTableColumn
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 4, 1, 2),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("mandatory")
_UpsOutputCurrent_Type = Integer32
_UpsOutputCurrent_Object = MibTableColumn
upsOutputCurrent = _UpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 4, 1, 3),
    _UpsOutputCurrent_Type()
)
upsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent.setStatus("mandatory")
_UpsOutputPercentLoad_Type = Integer32
_UpsOutputPercentLoad_Object = MibTableColumn
upsOutputPercentLoad = _UpsOutputPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 4, 1, 4),
    _UpsOutputPercentLoad_Type()
)
upsOutputPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setStatus("mandatory")
_UpsOutputKva_Type = Integer32
_UpsOutputKva_Object = MibTableColumn
upsOutputKva = _UpsOutputKva_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 4, 1, 5),
    _UpsOutputKva_Type()
)
upsOutputKva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputKva.setStatus("mandatory")
_UpsOutputKw_Type = Integer32
_UpsOutputKw_Object = MibTableColumn
upsOutputKw = _UpsOutputKw_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 4, 1, 6),
    _UpsOutputKw_Type()
)
upsOutputKw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputKw.setStatus("mandatory")
_UpsOutputGlobalkVA_Type = Integer32
_UpsOutputGlobalkVA_Object = MibScalar
upsOutputGlobalkVA = _UpsOutputGlobalkVA_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 5),
    _UpsOutputGlobalkVA_Type()
)
upsOutputGlobalkVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGlobalkVA.setStatus("mandatory")
_UpsOutputGlobalkW_Type = Integer32
_UpsOutputGlobalkW_Object = MibScalar
upsOutputGlobalkW = _UpsOutputGlobalkW_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 6),
    _UpsOutputGlobalkW_Type()
)
upsOutputGlobalkW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGlobalkW.setStatus("mandatory")
_UpsOutputLoadRate_Type = Integer32
_UpsOutputLoadRate_Object = MibScalar
upsOutputLoadRate = _UpsOutputLoadRate_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 4, 7),
    _UpsOutputLoadRate_Type()
)
upsOutputLoadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputLoadRate.setStatus("mandatory")
_UpsBypass_ObjectIdentity = ObjectIdentity
upsBypass = _UpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 5)
)
_UpsBypassFrequency_Type = Integer32
_UpsBypassFrequency_Object = MibScalar
upsBypassFrequency = _UpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 5, 1),
    _UpsBypassFrequency_Type()
)
upsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequency.setStatus("mandatory")
_UpsBypassNumLines_Type = Integer32
_UpsBypassNumLines_Object = MibScalar
upsBypassNumLines = _UpsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 5, 2),
    _UpsBypassNumLines_Type()
)
upsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLines.setStatus("mandatory")
_UpsBypassTable_Object = MibTable
upsBypassTable = _UpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassTable.setStatus("mandatory")
_UpsBypassEntry_Object = MibTableRow
upsBypassEntry = _UpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 5, 3, 1)
)
upsBypassEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsBypassLineIndex"),
)
if mibBuilder.loadTexts:
    upsBypassEntry.setStatus("mandatory")


class _UpsBypassLineIndex_Type(Integer32):
    """Custom type upsBypassLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsBypassLineIndex_Type.__name__ = "Integer32"
_UpsBypassLineIndex_Object = MibTableColumn
upsBypassLineIndex = _UpsBypassLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 5, 3, 1, 1),
    _UpsBypassLineIndex_Type()
)
upsBypassLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassLineIndex.setStatus("mandatory")
_UpsBypassVoltage_Type = Integer32
_UpsBypassVoltage_Object = MibTableColumn
upsBypassVoltage = _UpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 5, 3, 1, 2),
    _UpsBypassVoltage_Type()
)
upsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltage.setStatus("mandatory")
_UpsBypassCurrent_Type = Integer32
_UpsBypassCurrent_Object = MibTableColumn
upsBypassCurrent = _UpsBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 5, 3, 1, 3),
    _UpsBypassCurrent_Type()
)
upsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrent.setStatus("mandatory")
_UpsAlarm_ObjectIdentity = ObjectIdentity
upsAlarm = _UpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6)
)
_UpsAlarmsPresent_Type = Integer32
_UpsAlarmsPresent_Object = MibScalar
upsAlarmsPresent = _UpsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 1),
    _UpsAlarmsPresent_Type()
)
upsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresent.setStatus("mandatory")
_UpsAlarmTable_Object = MibTable
upsAlarmTable = _UpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmTable.setStatus("mandatory")
_UpsAlarmEntry_Object = MibTableRow
upsAlarmEntry = _UpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 2, 1)
)
upsAlarmEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsAlarmId"),
)
if mibBuilder.loadTexts:
    upsAlarmEntry.setStatus("mandatory")
_UpsAlarmId_Type = PositiveInteger
_UpsAlarmId_Object = MibTableColumn
upsAlarmId = _UpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 2, 1, 1),
    _UpsAlarmId_Type()
)
upsAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmId.setStatus("mandatory")
_UpsAlarmDescr_Type = AutonomousType
_UpsAlarmDescr_Object = MibTableColumn
upsAlarmDescr = _UpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 2, 1, 2),
    _UpsAlarmDescr_Type()
)
upsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescr.setStatus("mandatory")
_UpsAlarmTime_Type = TimeStamp
_UpsAlarmTime_Object = MibTableColumn
upsAlarmTime = _UpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 2, 1, 3),
    _UpsAlarmTime_Type()
)
upsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTime.setStatus("mandatory")
_UpsAlarmExtDes_Type = DisplayString
_UpsAlarmExtDes_Object = MibTableColumn
upsAlarmExtDes = _UpsAlarmExtDes_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 2, 1, 4),
    _UpsAlarmExtDes_Type()
)
upsAlarmExtDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExtDes.setStatus("mandatory")
_UpsWellKnownAlarms_ObjectIdentity = ObjectIdentity
upsWellKnownAlarms = _UpsWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3)
)
_UpsAlarmImminentStop_Type = Integer32
_UpsAlarmImminentStop_Object = MibScalar
upsAlarmImminentStop = _UpsAlarmImminentStop_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 1),
    _UpsAlarmImminentStop_Type()
)
upsAlarmImminentStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmImminentStop.setStatus("mandatory")
_UpsAlarmOverload_Type = Integer32
_UpsAlarmOverload_Object = MibScalar
upsAlarmOverload = _UpsAlarmOverload_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 2),
    _UpsAlarmOverload_Type()
)
upsAlarmOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOverload.setStatus("mandatory")
_UpsAlarmTemperature_Type = Integer32
_UpsAlarmTemperature_Object = MibScalar
upsAlarmTemperature = _UpsAlarmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 3),
    _UpsAlarmTemperature_Type()
)
upsAlarmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTemperature.setStatus("mandatory")
_UpsAlarmTransferLock_Type = Integer32
_UpsAlarmTransferLock_Object = MibScalar
upsAlarmTransferLock = _UpsAlarmTransferLock_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 4),
    _UpsAlarmTransferLock_Type()
)
upsAlarmTransferLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTransferLock.setStatus("mandatory")
_UpsAlarmAutoTransferImpossible_Type = Integer32
_UpsAlarmAutoTransferImpossible_Object = MibScalar
upsAlarmAutoTransferImpossible = _UpsAlarmAutoTransferImpossible_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 5),
    _UpsAlarmAutoTransferImpossible_Type()
)
upsAlarmAutoTransferImpossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmAutoTransferImpossible.setStatus("mandatory")
_UpsAlarmInsufficientResources_Type = Integer32
_UpsAlarmInsufficientResources_Object = MibScalar
upsAlarmInsufficientResources = _UpsAlarmInsufficientResources_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 6),
    _UpsAlarmInsufficientResources_Type()
)
upsAlarmInsufficientResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInsufficientResources.setStatus("mandatory")
_UpsAlarmRedundancyLost_Type = Integer32
_UpsAlarmRedundancyLost_Object = MibScalar
upsAlarmRedundancyLost = _UpsAlarmRedundancyLost_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 7),
    _UpsAlarmRedundancyLost_Type()
)
upsAlarmRedundancyLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRedundancyLost.setStatus("mandatory")
_UpsAlarmOutputShortCircuit_Type = Integer32
_UpsAlarmOutputShortCircuit_Object = MibScalar
upsAlarmOutputShortCircuit = _UpsAlarmOutputShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 8),
    _UpsAlarmOutputShortCircuit_Type()
)
upsAlarmOutputShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputShortCircuit.setStatus("mandatory")
_UpsAlarmMaintenance_Type = Integer32
_UpsAlarmMaintenance_Object = MibScalar
upsAlarmMaintenance = _UpsAlarmMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 9),
    _UpsAlarmMaintenance_Type()
)
upsAlarmMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaintenance.setStatus("mandatory")
_UpsAlarmRemoteService_Type = Integer32
_UpsAlarmRemoteService_Object = MibScalar
upsAlarmRemoteService = _UpsAlarmRemoteService_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 10),
    _UpsAlarmRemoteService_Type()
)
upsAlarmRemoteService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRemoteService.setStatus("mandatory")
_UpsAlarmGeneralFault_Type = Integer32
_UpsAlarmGeneralFault_Object = MibScalar
upsAlarmGeneralFault = _UpsAlarmGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 11),
    _UpsAlarmGeneralFault_Type()
)
upsAlarmGeneralFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmGeneralFault.setStatus("mandatory")
_UpsAlarmBatteryCircuitOpen_Type = Integer32
_UpsAlarmBatteryCircuitOpen_Object = MibScalar
upsAlarmBatteryCircuitOpen = _UpsAlarmBatteryCircuitOpen_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 12),
    _UpsAlarmBatteryCircuitOpen_Type()
)
upsAlarmBatteryCircuitOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryCircuitOpen.setStatus("mandatory")
_UpsAlarmBatteryDischarged_Type = Integer32
_UpsAlarmBatteryDischarged_Object = MibScalar
upsAlarmBatteryDischarged = _UpsAlarmBatteryDischarged_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 13),
    _UpsAlarmBatteryDischarged_Type()
)
upsAlarmBatteryDischarged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryDischarged.setStatus("mandatory")
_UpsAlarmLowBattery_Type = Integer32
_UpsAlarmLowBattery_Object = MibScalar
upsAlarmLowBattery = _UpsAlarmLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 14),
    _UpsAlarmLowBattery_Type()
)
upsAlarmLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmLowBattery.setStatus("mandatory")
_UpsAlarmOnBattery_Type = Integer32
_UpsAlarmOnBattery_Object = MibScalar
upsAlarmOnBattery = _UpsAlarmOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 15),
    _UpsAlarmOnBattery_Type()
)
upsAlarmOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOnBattery.setStatus("mandatory")
_UpsAlarmBatteryTemperature_Type = Integer32
_UpsAlarmBatteryTemperature_Object = MibScalar
upsAlarmBatteryTemperature = _UpsAlarmBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 16),
    _UpsAlarmBatteryTemperature_Type()
)
upsAlarmBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryTemperature.setStatus("mandatory")
_UpsAlarmBatteryRoom_Type = Integer32
_UpsAlarmBatteryRoom_Object = MibScalar
upsAlarmBatteryRoom = _UpsAlarmBatteryRoom_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 17),
    _UpsAlarmBatteryRoom_Type()
)
upsAlarmBatteryRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryRoom.setStatus("mandatory")
_UpsAlarmBatteryTest_Type = Integer32
_UpsAlarmBatteryTest_Object = MibScalar
upsAlarmBatteryTest = _UpsAlarmBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 18),
    _UpsAlarmBatteryTest_Type()
)
upsAlarmBatteryTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryTest.setStatus("mandatory")
_UpsAlarmBatteryFault_Type = Integer32
_UpsAlarmBatteryFault_Object = MibScalar
upsAlarmBatteryFault = _UpsAlarmBatteryFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 19),
    _UpsAlarmBatteryFault_Type()
)
upsAlarmBatteryFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryFault.setStatus("mandatory")
_UpsAlarmRectifierFault_Type = Integer32
_UpsAlarmRectifierFault_Object = MibScalar
upsAlarmRectifierFault = _UpsAlarmRectifierFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 20),
    _UpsAlarmRectifierFault_Type()
)
upsAlarmRectifierFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRectifierFault.setStatus("mandatory")
_UpsAlarmRectifierAlarm_Type = Integer32
_UpsAlarmRectifierAlarm_Object = MibScalar
upsAlarmRectifierAlarm = _UpsAlarmRectifierAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 21),
    _UpsAlarmRectifierAlarm_Type()
)
upsAlarmRectifierAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRectifierAlarm.setStatus("mandatory")
_UpsAlarmRecInputBad_Type = Integer32
_UpsAlarmRecInputBad_Object = MibScalar
upsAlarmRecInputBad = _UpsAlarmRecInputBad_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 22),
    _UpsAlarmRecInputBad_Type()
)
upsAlarmRecInputBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRecInputBad.setStatus("mandatory")
_UpsAlarmGenSetGeneral_Type = Integer32
_UpsAlarmGenSetGeneral_Object = MibScalar
upsAlarmGenSetGeneral = _UpsAlarmGenSetGeneral_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 23),
    _UpsAlarmGenSetGeneral_Type()
)
upsAlarmGenSetGeneral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmGenSetGeneral.setStatus("mandatory")
_UpsAlarmBatteryChargerFault_Type = Integer32
_UpsAlarmBatteryChargerFault_Object = MibScalar
upsAlarmBatteryChargerFault = _UpsAlarmBatteryChargerFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 24),
    _UpsAlarmBatteryChargerFault_Type()
)
upsAlarmBatteryChargerFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryChargerFault.setStatus("mandatory")
_UpsAlarmBatteryChargerAlarm_Type = Integer32
_UpsAlarmBatteryChargerAlarm_Object = MibScalar
upsAlarmBatteryChargerAlarm = _UpsAlarmBatteryChargerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 25),
    _UpsAlarmBatteryChargerAlarm_Type()
)
upsAlarmBatteryChargerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryChargerAlarm.setStatus("mandatory")
_UpsAlarmInverterFault_Type = Integer32
_UpsAlarmInverterFault_Object = MibScalar
upsAlarmInverterFault = _UpsAlarmInverterFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 26),
    _UpsAlarmInverterFault_Type()
)
upsAlarmInverterFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInverterFault.setStatus("mandatory")
_UpsAlarmInverterAlarm_Type = Integer32
_UpsAlarmInverterAlarm_Object = MibScalar
upsAlarmInverterAlarm = _UpsAlarmInverterAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 27),
    _UpsAlarmInverterAlarm_Type()
)
upsAlarmInverterAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInverterAlarm.setStatus("mandatory")
_UpsAlarmBypassFault_Type = Integer32
_UpsAlarmBypassFault_Object = MibScalar
upsAlarmBypassFault = _UpsAlarmBypassFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 28),
    _UpsAlarmBypassFault_Type()
)
upsAlarmBypassFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBypassFault.setStatus("mandatory")
_UpsAlarmBypassAlarm_Type = Integer32
_UpsAlarmBypassAlarm_Object = MibScalar
upsAlarmBypassAlarm = _UpsAlarmBypassAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 29),
    _UpsAlarmBypassAlarm_Type()
)
upsAlarmBypassAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBypassAlarm.setStatus("mandatory")
_UpsAlarmBypInputBad_Type = Integer32
_UpsAlarmBypInputBad_Object = MibScalar
upsAlarmBypInputBad = _UpsAlarmBypInputBad_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 30),
    _UpsAlarmBypInputBad_Type()
)
upsAlarmBypInputBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBypInputBad.setStatus("mandatory")
_UpsAlarmPhaseRotationFault_Type = Integer32
_UpsAlarmPhaseRotationFault_Object = MibScalar
upsAlarmPhaseRotationFault = _UpsAlarmPhaseRotationFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 31),
    _UpsAlarmPhaseRotationFault_Type()
)
upsAlarmPhaseRotationFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmPhaseRotationFault.setStatus("mandatory")
_UpsAlarmFansFailure_Type = Integer32
_UpsAlarmFansFailure_Object = MibScalar
upsAlarmFansFailure = _UpsAlarmFansFailure_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 32),
    _UpsAlarmFansFailure_Type()
)
upsAlarmFansFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmFansFailure.setStatus("mandatory")
_UpsAlarmMaintenanceBypass_Type = Integer32
_UpsAlarmMaintenanceBypass_Object = MibScalar
upsAlarmMaintenanceBypass = _UpsAlarmMaintenanceBypass_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 33),
    _UpsAlarmMaintenanceBypass_Type()
)
upsAlarmMaintenanceBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaintenanceBypass.setStatus("mandatory")
_UpsAlarmUPSPowerOffActive_Type = Integer32
_UpsAlarmUPSPowerOffActive_Object = MibScalar
upsAlarmUPSPowerOffActive = _UpsAlarmUPSPowerOffActive_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 34),
    _UpsAlarmUPSPowerOffActive_Type()
)
upsAlarmUPSPowerOffActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUPSPowerOffActive.setStatus("mandatory")
_UpsAlarmWrongConfiguration_Type = Integer32
_UpsAlarmWrongConfiguration_Object = MibScalar
upsAlarmWrongConfiguration = _UpsAlarmWrongConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 35),
    _UpsAlarmWrongConfiguration_Type()
)
upsAlarmWrongConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmWrongConfiguration.setStatus("mandatory")
_UpsAlarmInternalFailure_Type = Integer32
_UpsAlarmInternalFailure_Object = MibScalar
upsAlarmInternalFailure = _UpsAlarmInternalFailure_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 36),
    _UpsAlarmInternalFailure_Type()
)
upsAlarmInternalFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInternalFailure.setStatus("mandatory")
_UpsAlarmOptionalBoards_Type = Integer32
_UpsAlarmOptionalBoards_Object = MibScalar
upsAlarmOptionalBoards = _UpsAlarmOptionalBoards_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 37),
    _UpsAlarmOptionalBoards_Type()
)
upsAlarmOptionalBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOptionalBoards.setStatus("mandatory")
_UpsAlarmExternalAlarm1_Type = Integer32
_UpsAlarmExternalAlarm1_Object = MibScalar
upsAlarmExternalAlarm1 = _UpsAlarmExternalAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 38),
    _UpsAlarmExternalAlarm1_Type()
)
upsAlarmExternalAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExternalAlarm1.setStatus("mandatory")
_UpsAlarmExternalAlarm2_Type = Integer32
_UpsAlarmExternalAlarm2_Object = MibScalar
upsAlarmExternalAlarm2 = _UpsAlarmExternalAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 39),
    _UpsAlarmExternalAlarm2_Type()
)
upsAlarmExternalAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExternalAlarm2.setStatus("mandatory")
_UpsAlarmExternalAlarm3_Type = Integer32
_UpsAlarmExternalAlarm3_Object = MibScalar
upsAlarmExternalAlarm3 = _UpsAlarmExternalAlarm3_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 40),
    _UpsAlarmExternalAlarm3_Type()
)
upsAlarmExternalAlarm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExternalAlarm3.setStatus("mandatory")
_UpsAlarmExternalAlarm4_Type = Integer32
_UpsAlarmExternalAlarm4_Object = MibScalar
upsAlarmExternalAlarm4 = _UpsAlarmExternalAlarm4_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 41),
    _UpsAlarmExternalAlarm4_Type()
)
upsAlarmExternalAlarm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExternalAlarm4.setStatus("mandatory")
_UpsAlarmModule1Alarm_Type = Integer32
_UpsAlarmModule1Alarm_Object = MibScalar
upsAlarmModule1Alarm = _UpsAlarmModule1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 42),
    _UpsAlarmModule1Alarm_Type()
)
upsAlarmModule1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule1Alarm.setStatus("mandatory")
_UpsAlarmModule2Alarm_Type = Integer32
_UpsAlarmModule2Alarm_Object = MibScalar
upsAlarmModule2Alarm = _UpsAlarmModule2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 43),
    _UpsAlarmModule2Alarm_Type()
)
upsAlarmModule2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule2Alarm.setStatus("mandatory")
_UpsAlarmModule3Alarm_Type = Integer32
_UpsAlarmModule3Alarm_Object = MibScalar
upsAlarmModule3Alarm = _UpsAlarmModule3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 44),
    _UpsAlarmModule3Alarm_Type()
)
upsAlarmModule3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule3Alarm.setStatus("mandatory")
_UpsAlarmModule4Alarm_Type = Integer32
_UpsAlarmModule4Alarm_Object = MibScalar
upsAlarmModule4Alarm = _UpsAlarmModule4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 45),
    _UpsAlarmModule4Alarm_Type()
)
upsAlarmModule4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule4Alarm.setStatus("mandatory")
_UpsAlarmModule5Alarm_Type = Integer32
_UpsAlarmModule5Alarm_Object = MibScalar
upsAlarmModule5Alarm = _UpsAlarmModule5Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 46),
    _UpsAlarmModule5Alarm_Type()
)
upsAlarmModule5Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule5Alarm.setStatus("mandatory")
_UpsAlarmModule6Alarm_Type = Integer32
_UpsAlarmModule6Alarm_Object = MibScalar
upsAlarmModule6Alarm = _UpsAlarmModule6Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 47),
    _UpsAlarmModule6Alarm_Type()
)
upsAlarmModule6Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule6Alarm.setStatus("mandatory")
_UpsAlarmModule7Alarm_Type = Integer32
_UpsAlarmModule7Alarm_Object = MibScalar
upsAlarmModule7Alarm = _UpsAlarmModule7Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 48),
    _UpsAlarmModule7Alarm_Type()
)
upsAlarmModule7Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule7Alarm.setStatus("mandatory")
_UpsAlarmModule8Alarm_Type = Integer32
_UpsAlarmModule8Alarm_Object = MibScalar
upsAlarmModule8Alarm = _UpsAlarmModule8Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 49),
    _UpsAlarmModule8Alarm_Type()
)
upsAlarmModule8Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule8Alarm.setStatus("mandatory")
_UpsAlarmModule9Alarm_Type = Integer32
_UpsAlarmModule9Alarm_Object = MibScalar
upsAlarmModule9Alarm = _UpsAlarmModule9Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 50),
    _UpsAlarmModule9Alarm_Type()
)
upsAlarmModule9Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule9Alarm.setStatus("mandatory")
_UpsAlarmModule10Alarm_Type = Integer32
_UpsAlarmModule10Alarm_Object = MibScalar
upsAlarmModule10Alarm = _UpsAlarmModule10Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 51),
    _UpsAlarmModule10Alarm_Type()
)
upsAlarmModule10Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule10Alarm.setStatus("mandatory")
_UpsAlarmModule11Alarm_Type = Integer32
_UpsAlarmModule11Alarm_Object = MibScalar
upsAlarmModule11Alarm = _UpsAlarmModule11Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 52),
    _UpsAlarmModule11Alarm_Type()
)
upsAlarmModule11Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule11Alarm.setStatus("mandatory")
_UpsAlarmModule12Alarm_Type = Integer32
_UpsAlarmModule12Alarm_Object = MibScalar
upsAlarmModule12Alarm = _UpsAlarmModule12Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 53),
    _UpsAlarmModule12Alarm_Type()
)
upsAlarmModule12Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule12Alarm.setStatus("mandatory")
_UpsAlarmAutoTestRunning_Type = Integer32
_UpsAlarmAutoTestRunning_Object = MibScalar
upsAlarmAutoTestRunning = _UpsAlarmAutoTestRunning_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 54),
    _UpsAlarmAutoTestRunning_Type()
)
upsAlarmAutoTestRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmAutoTestRunning.setStatus("mandatory")
_UpsAlarmOnBypass_Type = Integer32
_UpsAlarmOnBypass_Object = MibScalar
upsAlarmOnBypass = _UpsAlarmOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 55),
    _UpsAlarmOnBypass_Type()
)
upsAlarmOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOnBypass.setStatus("mandatory")
_UpsAlarmUpsOutputOff_Type = Integer32
_UpsAlarmUpsOutputOff_Object = MibScalar
upsAlarmUpsOutputOff = _UpsAlarmUpsOutputOff_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 56),
    _UpsAlarmUpsOutputOff_Type()
)
upsAlarmUpsOutputOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOff.setStatus("mandatory")
_UpsAlarmUpsSystemOff_Type = Integer32
_UpsAlarmUpsSystemOff_Object = MibScalar
upsAlarmUpsSystemOff = _UpsAlarmUpsSystemOff_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 57),
    _UpsAlarmUpsSystemOff_Type()
)
upsAlarmUpsSystemOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOff.setStatus("mandatory")
_UpsAlarmCommunicationLost_Type = Integer32
_UpsAlarmCommunicationLost_Object = MibScalar
upsAlarmCommunicationLost = _UpsAlarmCommunicationLost_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 58),
    _UpsAlarmCommunicationLost_Type()
)
upsAlarmCommunicationLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCommunicationLost.setStatus("mandatory")
_UpsAlarmShutdownPending_Type = Integer32
_UpsAlarmShutdownPending_Object = MibScalar
upsAlarmShutdownPending = _UpsAlarmShutdownPending_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 59),
    _UpsAlarmShutdownPending_Type()
)
upsAlarmShutdownPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmShutdownPending.setStatus("mandatory")
_UpsAlarmShutdownRequestt_Type = Integer32
_UpsAlarmShutdownRequestt_Object = MibScalar
upsAlarmShutdownRequestt = _UpsAlarmShutdownRequestt_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 60),
    _UpsAlarmShutdownRequestt_Type()
)
upsAlarmShutdownRequestt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmShutdownRequestt.setStatus("mandatory")
_UpsAlarmShutdownImminent_Type = Integer32
_UpsAlarmShutdownImminent_Object = MibScalar
upsAlarmShutdownImminent = _UpsAlarmShutdownImminent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 61),
    _UpsAlarmShutdownImminent_Type()
)
upsAlarmShutdownImminent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmShutdownImminent.setStatus("mandatory")
_UpsAlarmAwaitingPower_Type = Integer32
_UpsAlarmAwaitingPower_Object = MibScalar
upsAlarmAwaitingPower = _UpsAlarmAwaitingPower_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 6, 3, 62),
    _UpsAlarmAwaitingPower_Type()
)
upsAlarmAwaitingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmAwaitingPower.setStatus("mandatory")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7)
)


class _UpsControlStatusControl_Type(Integer32):
    """Custom type upsControlStatusControl based on Integer32"""
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
        *(("upsStandbyOn", 1),
          ("upsStandbyOff", 2),
          ("upsEcoMode", 3),
          ("upsNormalMode", 4),
          ("upsAlarmReset", 5),
          ("upsOnBypass", 6),
          ("upsOnInverter", 7))
    )


_UpsControlStatusControl_Type.__name__ = "Integer32"
_UpsControlStatusControl_Object = MibScalar
upsControlStatusControl = _UpsControlStatusControl_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 1),
    _UpsControlStatusControl_Type()
)
upsControlStatusControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlStatusControl.setStatus("mandatory")
_UpsShutdownDelay_Type = Integer32
_UpsShutdownDelay_Object = MibScalar
upsShutdownDelay = _UpsShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 2),
    _UpsShutdownDelay_Type()
)
upsShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownDelay.setStatus("mandatory")


class _UpsTurnOffAfterShutdown_Type(Integer32):
    """Custom type upsTurnOffAfterShutdown based on Integer32"""
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


_UpsTurnOffAfterShutdown_Type.__name__ = "Integer32"
_UpsTurnOffAfterShutdown_Object = MibScalar
upsTurnOffAfterShutdown = _UpsTurnOffAfterShutdown_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 3),
    _UpsTurnOffAfterShutdown_Type()
)
upsTurnOffAfterShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTurnOffAfterShutdown.setStatus("mandatory")
_UpsControlShutdownParamTable_Object = MibTable
upsControlShutdownParamTable = _UpsControlShutdownParamTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 4)
)
if mibBuilder.loadTexts:
    upsControlShutdownParamTable.setStatus("mandatory")
_ShutdownParamEntry_Object = MibTableRow
shutdownParamEntry = _ShutdownParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 4, 1)
)
shutdownParamEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsControlEventIndex"),
)
if mibBuilder.loadTexts:
    shutdownParamEntry.setStatus("mandatory")


class _UpsControlEventIndex_Type(Integer32):
    """Custom type upsControlEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsControlEventIndex_Type.__name__ = "Integer32"
_UpsControlEventIndex_Object = MibTableColumn
upsControlEventIndex = _UpsControlEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 4, 1, 1),
    _UpsControlEventIndex_Type()
)
upsControlEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlEventIndex.setStatus("mandatory")


class _UpsControlEventStatus_Type(Integer32):
    """Custom type upsControlEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("warning", 2),
          ("clientShutdown", 3))
    )


_UpsControlEventStatus_Type.__name__ = "Integer32"
_UpsControlEventStatus_Object = MibTableColumn
upsControlEventStatus = _UpsControlEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 4, 1, 2),
    _UpsControlEventStatus_Type()
)
upsControlEventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEventStatus.setStatus("mandatory")


class _UpsControlDelay_Type(Integer32):
    """Custom type upsControlDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_UpsControlDelay_Type.__name__ = "Integer32"
_UpsControlDelay_Object = MibTableColumn
upsControlDelay = _UpsControlDelay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 4, 1, 3),
    _UpsControlDelay_Type()
)
upsControlDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlDelay.setStatus("mandatory")


class _UpsControlFirstWarning_Type(Integer32):
    """Custom type upsControlFirstWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_UpsControlFirstWarning_Type.__name__ = "Integer32"
_UpsControlFirstWarning_Object = MibTableColumn
upsControlFirstWarning = _UpsControlFirstWarning_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 4, 1, 4),
    _UpsControlFirstWarning_Type()
)
upsControlFirstWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlFirstWarning.setStatus("mandatory")


class _UpsControlWarningInterval_Type(Integer32):
    """Custom type upsControlWarningInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_UpsControlWarningInterval_Type.__name__ = "Integer32"
_UpsControlWarningInterval_Object = MibTableColumn
upsControlWarningInterval = _UpsControlWarningInterval_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 4, 1, 5),
    _UpsControlWarningInterval_Type()
)
upsControlWarningInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWarningInterval.setStatus("mandatory")
_UpsControlWeeklyScheduleTable_Object = MibTable
upsControlWeeklyScheduleTable = _UpsControlWeeklyScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 5)
)
if mibBuilder.loadTexts:
    upsControlWeeklyScheduleTable.setStatus("mandatory")
_UpsControlWeeklyScheduleEntry_Object = MibTableRow
upsControlWeeklyScheduleEntry = _UpsControlWeeklyScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 5, 1)
)
upsControlWeeklyScheduleEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsControlWeeklyIndex"),
)
if mibBuilder.loadTexts:
    upsControlWeeklyScheduleEntry.setStatus("mandatory")


class _UpsControlWeeklyIndex_Type(Integer32):
    """Custom type upsControlWeeklyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_UpsControlWeeklyIndex_Type.__name__ = "Integer32"
_UpsControlWeeklyIndex_Object = MibTableColumn
upsControlWeeklyIndex = _UpsControlWeeklyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 5, 1, 1),
    _UpsControlWeeklyIndex_Type()
)
upsControlWeeklyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlWeeklyIndex.setStatus("mandatory")


class _UpsControlWeeklyShutdownDay_Type(Integer32):
    """Custom type upsControlWeeklyShutdownDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7),
          ("none", 8))
    )


_UpsControlWeeklyShutdownDay_Type.__name__ = "Integer32"
_UpsControlWeeklyShutdownDay_Object = MibTableColumn
upsControlWeeklyShutdownDay = _UpsControlWeeklyShutdownDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 5, 1, 2),
    _UpsControlWeeklyShutdownDay_Type()
)
upsControlWeeklyShutdownDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyShutdownDay.setStatus("mandatory")


class _UpsControlWeeklyShutdownTime_Type(DisplayString):
    """Custom type upsControlWeeklyShutdownTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UpsControlWeeklyShutdownTime_Type.__name__ = "DisplayString"
_UpsControlWeeklyShutdownTime_Object = MibTableColumn
upsControlWeeklyShutdownTime = _UpsControlWeeklyShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 5, 1, 3),
    _UpsControlWeeklyShutdownTime_Type()
)
upsControlWeeklyShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyShutdownTime.setStatus("mandatory")


class _UpsControlWeeklyRestartDay_Type(Integer32):
    """Custom type upsControlWeeklyRestartDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7),
          ("none", 8))
    )


_UpsControlWeeklyRestartDay_Type.__name__ = "Integer32"
_UpsControlWeeklyRestartDay_Object = MibTableColumn
upsControlWeeklyRestartDay = _UpsControlWeeklyRestartDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 5, 1, 4),
    _UpsControlWeeklyRestartDay_Type()
)
upsControlWeeklyRestartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyRestartDay.setStatus("mandatory")


class _UpsControlWeeklyRestartTime_Type(DisplayString):
    """Custom type upsControlWeeklyRestartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UpsControlWeeklyRestartTime_Type.__name__ = "DisplayString"
_UpsControlWeeklyRestartTime_Object = MibTableColumn
upsControlWeeklyRestartTime = _UpsControlWeeklyRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 5, 1, 5),
    _UpsControlWeeklyRestartTime_Type()
)
upsControlWeeklyRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyRestartTime.setStatus("mandatory")
_UpsControlSpecialScheduleTable_Object = MibTable
upsControlSpecialScheduleTable = _UpsControlSpecialScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 6)
)
if mibBuilder.loadTexts:
    upsControlSpecialScheduleTable.setStatus("mandatory")
_UpsControlSpecialScheduleEntry_Object = MibTableRow
upsControlSpecialScheduleEntry = _UpsControlSpecialScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 6, 1)
)
upsControlSpecialScheduleEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsControlSpecialIndex"),
)
if mibBuilder.loadTexts:
    upsControlSpecialScheduleEntry.setStatus("mandatory")


class _UpsControlSpecialIndex_Type(Integer32):
    """Custom type upsControlSpecialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_UpsControlSpecialIndex_Type.__name__ = "Integer32"
_UpsControlSpecialIndex_Object = MibTableColumn
upsControlSpecialIndex = _UpsControlSpecialIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 6, 1, 1),
    _UpsControlSpecialIndex_Type()
)
upsControlSpecialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlSpecialIndex.setStatus("mandatory")


class _UpsControlSpecialShutdownDay_Type(DisplayString):
    """Custom type upsControlSpecialShutdownDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_UpsControlSpecialShutdownDay_Type.__name__ = "DisplayString"
_UpsControlSpecialShutdownDay_Object = MibTableColumn
upsControlSpecialShutdownDay = _UpsControlSpecialShutdownDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 6, 1, 2),
    _UpsControlSpecialShutdownDay_Type()
)
upsControlSpecialShutdownDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialShutdownDay.setStatus("mandatory")


class _UpsControlSpecialShutdownTime_Type(DisplayString):
    """Custom type upsControlSpecialShutdownTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UpsControlSpecialShutdownTime_Type.__name__ = "DisplayString"
_UpsControlSpecialShutdownTime_Object = MibTableColumn
upsControlSpecialShutdownTime = _UpsControlSpecialShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 6, 1, 3),
    _UpsControlSpecialShutdownTime_Type()
)
upsControlSpecialShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialShutdownTime.setStatus("mandatory")


class _UpsControlSpecialRestartDay_Type(DisplayString):
    """Custom type upsControlSpecialRestartDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_UpsControlSpecialRestartDay_Type.__name__ = "DisplayString"
_UpsControlSpecialRestartDay_Object = MibTableColumn
upsControlSpecialRestartDay = _UpsControlSpecialRestartDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 6, 1, 4),
    _UpsControlSpecialRestartDay_Type()
)
upsControlSpecialRestartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialRestartDay.setStatus("mandatory")


class _UpsControlSpecialRestartTime_Type(DisplayString):
    """Custom type upsControlSpecialRestartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UpsControlSpecialRestartTime_Type.__name__ = "DisplayString"
_UpsControlSpecialRestartTime_Object = MibTableColumn
upsControlSpecialRestartTime = _UpsControlSpecialRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 6, 1, 5),
    _UpsControlSpecialRestartTime_Type()
)
upsControlSpecialRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialRestartTime.setStatus("mandatory")
_UpsControlEcoModeScheduleTable_Object = MibTable
upsControlEcoModeScheduleTable = _UpsControlEcoModeScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 7)
)
if mibBuilder.loadTexts:
    upsControlEcoModeScheduleTable.setStatus("mandatory")
_UpsControlEcoModeScheduleEntry_Object = MibTableRow
upsControlEcoModeScheduleEntry = _UpsControlEcoModeScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 7, 1)
)
upsControlEcoModeScheduleEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsControlEcoModeIndex"),
)
if mibBuilder.loadTexts:
    upsControlEcoModeScheduleEntry.setStatus("mandatory")


class _UpsControlEcoModeIndex_Type(Integer32):
    """Custom type upsControlEcoModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_UpsControlEcoModeIndex_Type.__name__ = "Integer32"
_UpsControlEcoModeIndex_Object = MibTableColumn
upsControlEcoModeIndex = _UpsControlEcoModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 7, 1, 1),
    _UpsControlEcoModeIndex_Type()
)
upsControlEcoModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlEcoModeIndex.setStatus("mandatory")


class _UpsControlEcoModeStartDay_Type(Integer32):
    """Custom type upsControlEcoModeStartDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7),
          ("none", 8))
    )


_UpsControlEcoModeStartDay_Type.__name__ = "Integer32"
_UpsControlEcoModeStartDay_Object = MibTableColumn
upsControlEcoModeStartDay = _UpsControlEcoModeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 7, 1, 2),
    _UpsControlEcoModeStartDay_Type()
)
upsControlEcoModeStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEcoModeStartDay.setStatus("mandatory")


class _UpsControlEcoModeStartTime_Type(DisplayString):
    """Custom type upsControlEcoModeStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UpsControlEcoModeStartTime_Type.__name__ = "DisplayString"
_UpsControlEcoModeStartTime_Object = MibTableColumn
upsControlEcoModeStartTime = _UpsControlEcoModeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 7, 1, 3),
    _UpsControlEcoModeStartTime_Type()
)
upsControlEcoModeStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEcoModeStartTime.setStatus("mandatory")


class _UpsControlEcoModeEndDay_Type(Integer32):
    """Custom type upsControlEcoModeEndDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7),
          ("none", 8))
    )


_UpsControlEcoModeEndDay_Type.__name__ = "Integer32"
_UpsControlEcoModeEndDay_Object = MibTableColumn
upsControlEcoModeEndDay = _UpsControlEcoModeEndDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 7, 1, 4),
    _UpsControlEcoModeEndDay_Type()
)
upsControlEcoModeEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEcoModeEndDay.setStatus("mandatory")


class _UpsControlEcoModeEndTime_Type(DisplayString):
    """Custom type upsControlEcoModeEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UpsControlEcoModeEndTime_Type.__name__ = "DisplayString"
_UpsControlEcoModeEndTime_Object = MibTableColumn
upsControlEcoModeEndTime = _UpsControlEcoModeEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 7, 7, 1, 5),
    _UpsControlEcoModeEndTime_Type()
)
upsControlEcoModeEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEcoModeEndTime.setStatus("mandatory")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8)
)
_UpsConfigNomKva_Type = Integer32
_UpsConfigNomKva_Object = MibScalar
upsConfigNomKva = _UpsConfigNomKva_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 1),
    _UpsConfigNomKva_Type()
)
upsConfigNomKva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigNomKva.setStatus("mandatory")
_UpsConfigNbrUnit_Type = Integer32
_UpsConfigNbrUnit_Object = MibScalar
upsConfigNbrUnit = _UpsConfigNbrUnit_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 2),
    _UpsConfigNbrUnit_Type()
)
upsConfigNbrUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigNbrUnit.setStatus("mandatory")
_UpsConfigUnitKva_Type = Integer32
_UpsConfigUnitKva_Object = MibScalar
upsConfigUnitKva = _UpsConfigUnitKva_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 3),
    _UpsConfigUnitKva_Type()
)
upsConfigUnitKva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigUnitKva.setStatus("mandatory")
_UpsConfigRemoteCtrl_Type = Integer32
_UpsConfigRemoteCtrl_Object = MibScalar
upsConfigRemoteCtrl = _UpsConfigRemoteCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 4),
    _UpsConfigRemoteCtrl_Type()
)
upsConfigRemoteCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigRemoteCtrl.setStatus("mandatory")
_UpsDevicesTable_Object = MibTable
upsDevicesTable = _UpsDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 5)
)
if mibBuilder.loadTexts:
    upsDevicesTable.setStatus("mandatory")
_UpsDevicesEntry_Object = MibTableRow
upsDevicesEntry = _UpsDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 5, 1)
)
upsDevicesEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "indexOfDevice"),
)
if mibBuilder.loadTexts:
    upsDevicesEntry.setStatus("mandatory")
_IndexOfDevice_Type = NonNegativeInteger
_IndexOfDevice_Object = MibTableColumn
indexOfDevice = _IndexOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 5, 1, 1),
    _IndexOfDevice_Type()
)
indexOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indexOfDevice.setStatus("mandatory")


class _AddrOfDevice_Type(DisplayString):
    """Custom type addrOfDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AddrOfDevice_Type.__name__ = "DisplayString"
_AddrOfDevice_Object = MibTableColumn
addrOfDevice = _AddrOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 5, 1, 2),
    _AddrOfDevice_Type()
)
addrOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrOfDevice.setStatus("mandatory")


class _NameOfDevice_Type(DisplayString):
    """Custom type nameOfDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NameOfDevice_Type.__name__ = "DisplayString"
_NameOfDevice_Object = MibTableColumn
nameOfDevice = _NameOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 5, 1, 3),
    _NameOfDevice_Type()
)
nameOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameOfDevice.setStatus("mandatory")
_TimeOfConnection_Type = DisplayString
_TimeOfConnection_Object = MibTableColumn
timeOfConnection = _TimeOfConnection_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 5, 1, 4),
    _TimeOfConnection_Type()
)
timeOfConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOfConnection.setStatus("mandatory")
_StatusOfConnection_Type = Integer32
_StatusOfConnection_Object = MibTableColumn
statusOfConnection = _StatusOfConnection_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 5, 1, 5),
    _StatusOfConnection_Type()
)
statusOfConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusOfConnection.setStatus("mandatory")
_SeverityOfConnection_Type = Integer32
_SeverityOfConnection_Object = MibTableColumn
severityOfConnection = _SeverityOfConnection_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 8, 5, 1, 6),
    _SeverityOfConnection_Type()
)
severityOfConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severityOfConnection.setStatus("mandatory")
_UpsAgent_ObjectIdentity = ObjectIdentity
upsAgent = _UpsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9)
)
_UpsAgentIpaddress_Type = IpAddress
_UpsAgentIpaddress_Object = MibScalar
upsAgentIpaddress = _UpsAgentIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 1),
    _UpsAgentIpaddress_Type()
)
upsAgentIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentIpaddress.setStatus("mandatory")
_UpsAgentGateway_Type = IpAddress
_UpsAgentGateway_Object = MibScalar
upsAgentGateway = _UpsAgentGateway_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 2),
    _UpsAgentGateway_Type()
)
upsAgentGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentGateway.setStatus("mandatory")
_UpsAgentSubnetMask_Type = IpAddress
_UpsAgentSubnetMask_Object = MibScalar
upsAgentSubnetMask = _UpsAgentSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 3),
    _UpsAgentSubnetMask_Type()
)
upsAgentSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentSubnetMask.setStatus("mandatory")


class _UpsAgentDate_Type(DisplayString):
    """Custom type upsAgentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_UpsAgentDate_Type.__name__ = "DisplayString"
_UpsAgentDate_Object = MibScalar
upsAgentDate = _UpsAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 4),
    _UpsAgentDate_Type()
)
upsAgentDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentDate.setStatus("mandatory")


class _UpsAgentTime_Type(DisplayString):
    """Custom type upsAgentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_UpsAgentTime_Type.__name__ = "DisplayString"
_UpsAgentTime_Object = MibScalar
upsAgentTime = _UpsAgentTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 5),
    _UpsAgentTime_Type()
)
upsAgentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentTime.setStatus("mandatory")
_UpsAgentNtpTimeServer_Type = DisplayString
_UpsAgentNtpTimeServer_Object = MibScalar
upsAgentNtpTimeServer = _UpsAgentNtpTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 6),
    _UpsAgentNtpTimeServer_Type()
)
upsAgentNtpTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentNtpTimeServer.setStatus("mandatory")


class _UpsAgentNtpTimeZone_Type(Integer32):
    """Custom type upsAgentNtpTimeZone based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("gmt1200dateLineWest", 1),
          ("gmt1200kwajalein", 2),
          ("gmt1100samoa", 3),
          ("gmt1000hawaii", 4),
          ("gmt0900alaska", 5),
          ("gmt0800tijuana", 6),
          ("gmt0700arizona", 7),
          ("gmt0700chihuahua", 8),
          ("gmt0700mountain", 9),
          ("gmt0600camerica", 10),
          ("gmt0600ctime", 11),
          ("gmt0600guadalajara", 12),
          ("gmt0600saskatchewan", 13),
          ("gmt0500quito", 14),
          ("gmt0500etime", 15),
          ("gmt0500indiana", 16),
          ("gmt0400atime", 17),
          ("gmt0400caracas", 18),
          ("gmt0400santiago", 19),
          ("gmt0330newfoundland", 20),
          ("gmt0300brasilia", 21),
          ("gmt0300georgetown", 22),
          ("gmt0300greenland", 23),
          ("gmt0200atlantic", 24),
          ("gmt0100azores", 25),
          ("gmt0100cvi", 26),
          ("gmt0000monrovia", 27),
          ("gmt0000london", 28),
          ("gmt0100vienna", 29),
          ("gmt0100prague", 30),
          ("gmt0100paris", 31),
          ("gmt0100zagreb", 32),
          ("gmt0100wcafrica", 33),
          ("gmt0200minsk", 34),
          ("gmt0200bucharest", 35),
          ("gmt0200cairo", 36),
          ("gmt0200pretoria", 37),
          ("gmt0200vilnius", 38),
          ("gmt0200jerusalem", 39),
          ("gmt0300maghdad", 40),
          ("gmt0300riyadh", 41),
          ("gmt0300volgograd", 42),
          ("gmt0300nairobi", 43),
          ("gmt0330tehran", 44),
          ("gmt0400muscat", 45),
          ("gmt0400yerevan", 46),
          ("gmt0430kabul", 47),
          ("gmt0500ekaterinburg", 48),
          ("gmt0500tashkent", 49),
          ("gmt0530calcutta", 50),
          ("gmt0530mumbai", 51),
          ("gmt0545kathmandu", 52),
          ("gmt0600novosibirsk", 53),
          ("gmt0600dhaka", 54),
          ("gmt0600jayawardenepura", 55),
          ("gmt0630rangoon", 56),
          ("gmt0700bangkok", 57),
          ("gmt0700krasnoyarsk", 58),
          ("gmt0800beijing", 59),
          ("gmt0800irkutsk", 60),
          ("gmt0800singapore", 61),
          ("gmt0800perth", 62),
          ("gmt0800taipei", 63),
          ("gmt0900tokyo", 64),
          ("gmt0900seoul", 65),
          ("gmt0900yakutsk", 66),
          ("gmt0930adelaide", 67),
          ("gmt0930darwin", 68),
          ("gmt1000brisbane", 69),
          ("gmt1000canberra", 70),
          ("gmt1000guam", 71),
          ("gmt1000hobart", 72),
          ("gmt1000vladivostok", 73),
          ("gmt1100magadan", 74),
          ("gmt1200auckland", 75),
          ("gmt1200fiji", 76),
          ("gmt1300alofa", 77))
    )


_UpsAgentNtpTimeZone_Type.__name__ = "Integer32"
_UpsAgentNtpTimeZone_Object = MibScalar
upsAgentNtpTimeZone = _UpsAgentNtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 7),
    _UpsAgentNtpTimeZone_Type()
)
upsAgentNtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentNtpTimeZone.setStatus("mandatory")


class _UpsAgentHistoryLogFrequency_Type(Integer32):
    """Custom type upsAgentHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 28800),
    )


_UpsAgentHistoryLogFrequency_Type.__name__ = "Integer32"
_UpsAgentHistoryLogFrequency_Object = MibScalar
upsAgentHistoryLogFrequency = _UpsAgentHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 8),
    _UpsAgentHistoryLogFrequency_Type()
)
upsAgentHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentHistoryLogFrequency.setStatus("mandatory")


class _UpsAgentExtHistoryLogFrequency_Type(Integer32):
    """Custom type upsAgentExtHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10080),
    )


_UpsAgentExtHistoryLogFrequency_Type.__name__ = "Integer32"
_UpsAgentExtHistoryLogFrequency_Object = MibScalar
upsAgentExtHistoryLogFrequency = _UpsAgentExtHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 9),
    _UpsAgentExtHistoryLogFrequency_Type()
)
upsAgentExtHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentExtHistoryLogFrequency.setStatus("mandatory")


class _UpsAgentPollRate_Type(Integer32):
    """Custom type upsAgentPollRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_UpsAgentPollRate_Type.__name__ = "Integer32"
_UpsAgentPollRate_Object = MibScalar
upsAgentPollRate = _UpsAgentPollRate_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 10),
    _UpsAgentPollRate_Type()
)
upsAgentPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentPollRate.setStatus("mandatory")
_UpsAgentBaudRate_Type = Integer32
_UpsAgentBaudRate_Object = MibScalar
upsAgentBaudRate = _UpsAgentBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 11),
    _UpsAgentBaudRate_Type()
)
upsAgentBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAgentBaudRate.setStatus("mandatory")


class _UpsAgentDhcpStatue_Type(Integer32):
    """Custom type upsAgentDhcpStatue based on Integer32"""
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


_UpsAgentDhcpStatue_Type.__name__ = "Integer32"
_UpsAgentDhcpStatue_Object = MibScalar
upsAgentDhcpStatue = _UpsAgentDhcpStatue_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 12),
    _UpsAgentDhcpStatue_Type()
)
upsAgentDhcpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentDhcpStatue.setStatus("mandatory")


class _UpsAgentTelnetStatus_Type(Integer32):
    """Custom type upsAgentTelnetStatus based on Integer32"""
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


_UpsAgentTelnetStatus_Type.__name__ = "Integer32"
_UpsAgentTelnetStatus_Object = MibScalar
upsAgentTelnetStatus = _UpsAgentTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 13),
    _UpsAgentTelnetStatus_Type()
)
upsAgentTelnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentTelnetStatus.setStatus("mandatory")


class _UpsAgentTftpStatus_Type(Integer32):
    """Custom type upsAgentTftpStatus based on Integer32"""
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


_UpsAgentTftpStatus_Type.__name__ = "Integer32"
_UpsAgentTftpStatus_Object = MibScalar
upsAgentTftpStatus = _UpsAgentTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 14),
    _UpsAgentTftpStatus_Type()
)
upsAgentTftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentTftpStatus.setStatus("mandatory")


class _UpsAgentResetToDefault_Type(Integer32):
    """Custom type upsAgentResetToDefault based on Integer32"""
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


_UpsAgentResetToDefault_Type.__name__ = "Integer32"
_UpsAgentResetToDefault_Object = MibScalar
upsAgentResetToDefault = _UpsAgentResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 15),
    _UpsAgentResetToDefault_Type()
)
upsAgentResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentResetToDefault.setStatus("mandatory")


class _UpsAgentRestart_Type(Integer32):
    """Custom type upsAgentRestart based on Integer32"""
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


_UpsAgentRestart_Type.__name__ = "Integer32"
_UpsAgentRestart_Object = MibScalar
upsAgentRestart = _UpsAgentRestart_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 16),
    _UpsAgentRestart_Type()
)
upsAgentRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentRestart.setStatus("mandatory")


class _UpsAgentClearAgentLog_Type(Integer32):
    """Custom type upsAgentClearAgentLog based on Integer32"""
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


_UpsAgentClearAgentLog_Type.__name__ = "Integer32"
_UpsAgentClearAgentLog_Object = MibScalar
upsAgentClearAgentLog = _UpsAgentClearAgentLog_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 17),
    _UpsAgentClearAgentLog_Type()
)
upsAgentClearAgentLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentClearAgentLog.setStatus("mandatory")


class _UpsAgentClearEventLog_Type(Integer32):
    """Custom type upsAgentClearEventLog based on Integer32"""
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


_UpsAgentClearEventLog_Type.__name__ = "Integer32"
_UpsAgentClearEventLog_Object = MibScalar
upsAgentClearEventLog = _UpsAgentClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 18),
    _UpsAgentClearEventLog_Type()
)
upsAgentClearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentClearEventLog.setStatus("mandatory")


class _UpsAgentClearExtHistoryLog_Type(Integer32):
    """Custom type upsAgentClearExtHistoryLog based on Integer32"""
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


_UpsAgentClearExtHistoryLog_Type.__name__ = "Integer32"
_UpsAgentClearExtHistoryLog_Object = MibScalar
upsAgentClearExtHistoryLog = _UpsAgentClearExtHistoryLog_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 19),
    _UpsAgentClearExtHistoryLog_Type()
)
upsAgentClearExtHistoryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentClearExtHistoryLog.setStatus("mandatory")


class _UpsAgentClearHistoryLog_Type(Integer32):
    """Custom type upsAgentClearHistoryLog based on Integer32"""
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


_UpsAgentClearHistoryLog_Type.__name__ = "Integer32"
_UpsAgentClearHistoryLog_Object = MibScalar
upsAgentClearHistoryLog = _UpsAgentClearHistoryLog_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 20),
    _UpsAgentClearHistoryLog_Type()
)
upsAgentClearHistoryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentClearHistoryLog.setStatus("mandatory")
_UpsAgentTrapsReceiversTable_Object = MibTable
upsAgentTrapsReceiversTable = _UpsAgentTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 21)
)
if mibBuilder.loadTexts:
    upsAgentTrapsReceiversTable.setStatus("mandatory")
_UpsAgentTrapsReceiversEntry_Object = MibTableRow
upsAgentTrapsReceiversEntry = _UpsAgentTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 21, 1)
)
upsAgentTrapsReceiversEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    upsAgentTrapsReceiversEntry.setStatus("mandatory")


class _TrapsIndex_Type(Integer32):
    """Custom type trapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TrapsIndex_Type.__name__ = "Integer32"
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 21, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")
_TrapsReceiverAddr_Type = DisplayString
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 21, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")


class _ReceiverCommunityString_Type(DisplayString):
    """Custom type receiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReceiverCommunityString_Type.__name__ = "DisplayString"
_ReceiverCommunityString_Object = MibTableColumn
receiverCommunityString = _ReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 21, 1, 3),
    _ReceiverCommunityString_Type()
)
receiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverCommunityString.setStatus("mandatory")


class _ReceiverNmstype_Type(Integer32):
    """Custom type receiverNmstype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rfc1628-trap", 2),
          ("netVision-trap", 3))
    )


_ReceiverNmstype_Type.__name__ = "Integer32"
_ReceiverNmstype_Object = MibTableColumn
receiverNmstype = _ReceiverNmstype_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 21, 1, 4),
    _ReceiverNmstype_Type()
)
receiverNmstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverNmstype.setStatus("mandatory")
_UpsAgentFirewallControlTable_Object = MibTable
upsAgentFirewallControlTable = _UpsAgentFirewallControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 22)
)
if mibBuilder.loadTexts:
    upsAgentFirewallControlTable.setStatus("mandatory")
_UpsAgentFirewallControlEntry_Object = MibTableRow
upsAgentFirewallControlEntry = _UpsAgentFirewallControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 22, 1)
)
upsAgentFirewallControlEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    upsAgentFirewallControlEntry.setStatus("mandatory")
_FirewallIndex_Type = Integer32
_FirewallIndex_Object = MibTableColumn
firewallIndex = _FirewallIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 22, 1, 1),
    _FirewallIndex_Type()
)
firewallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallIndex.setStatus("mandatory")
_FirewallControlAddr_Type = DisplayString
_FirewallControlAddr_Object = MibTableColumn
firewallControlAddr = _FirewallControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 22, 1, 2),
    _FirewallControlAddr_Type()
)
firewallControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallControlAddr.setStatus("mandatory")


class _FirewallPrefixLength_Type(Integer32):
    """Custom type firewallPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FirewallPrefixLength_Type.__name__ = "Integer32"
_FirewallPrefixLength_Object = MibTableColumn
firewallPrefixLength = _FirewallPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 22, 1, 3),
    _FirewallPrefixLength_Type()
)
firewallPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallPrefixLength.setStatus("mandatory")


class _FirewallActionMode_Type(Integer32):
    """Custom type firewallActionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_FirewallActionMode_Type.__name__ = "Integer32"
_FirewallActionMode_Object = MibTableColumn
firewallActionMode = _FirewallActionMode_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 22, 1, 4),
    _FirewallActionMode_Type()
)
firewallActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallActionMode.setStatus("mandatory")
_UpsAgentMibVersion_Type = Integer32
_UpsAgentMibVersion_Object = MibScalar
upsAgentMibVersion = _UpsAgentMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 9, 23),
    _UpsAgentMibVersion_Type()
)
upsAgentMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAgentMibVersion.setStatus("mandatory")
_EmdStatus_ObjectIdentity = ObjectIdentity
emdStatus = _EmdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 10)
)
_EmdSatatusTemperature_Type = Integer32
_EmdSatatusTemperature_Object = MibScalar
emdSatatusTemperature = _EmdSatatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 10, 1),
    _EmdSatatusTemperature_Type()
)
emdSatatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusTemperature.setStatus("mandatory")
_EmdSatatusHumidity_Type = Integer32
_EmdSatatusHumidity_Object = MibScalar
emdSatatusHumidity = _EmdSatatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 10, 2),
    _EmdSatatusHumidity_Type()
)
emdSatatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusHumidity.setStatus("mandatory")


class _EmdStatusIn1Active_Type(Integer32):
    """Custom type emdStatusIn1Active based on Integer32"""
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
          ("notActived", 2),
          ("actived", 3))
    )


_EmdStatusIn1Active_Type.__name__ = "Integer32"
_EmdStatusIn1Active_Object = MibScalar
emdStatusIn1Active = _EmdStatusIn1Active_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 10, 3),
    _EmdStatusIn1Active_Type()
)
emdStatusIn1Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdStatusIn1Active.setStatus("mandatory")


class _EmdStatusIn2Active_Type(Integer32):
    """Custom type emdStatusIn2Active based on Integer32"""
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
          ("notActived", 2),
          ("actived", 3))
    )


_EmdStatusIn2Active_Type.__name__ = "Integer32"
_EmdStatusIn2Active_Object = MibScalar
emdStatusIn2Active = _EmdStatusIn2Active_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 1, 10, 4),
    _EmdStatusIn2Active_Type()
)
emdStatusIn2Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdStatusIn2Active.setStatus("mandatory")
_UpsTraps_ObjectIdentity = ObjectIdentity
upsTraps = _UpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2)
)

# Managed Objects groups


# Notification objects

upsTrapOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 1)
)
upsTrapOnBattery.setObjects(
      *(("SOCOMECUPS-MIB", "upsEstimatedMinutesRemaining"),
        ("SOCOMECUPS-MIB", "upsSecondsOnBattery"))
)
if mibBuilder.loadTexts:
    upsTrapOnBattery.setStatus(
        ""
    )

upsTrapTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 2)
)
if mibBuilder.loadTexts:
    upsTrapTestCompleted.setStatus(
        ""
    )

upsTrapAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 3)
)
upsTrapAlarmEntryAdded.setObjects(
      *(("SOCOMECUPS-MIB", "upsAlarmId"),
        ("SOCOMECUPS-MIB", "upsAlarmDescr"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmEntryAdded.setStatus(
        ""
    )

upsTrapAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 4)
)
upsTrapAlarmEntryRemoved.setObjects(
      *(("SOCOMECUPS-MIB", "upsAlarmId"),
        ("SOCOMECUPS-MIB", "upsAlarmDescr"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmEntryRemoved.setStatus(
        ""
    )

upsTrapImminentStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 5)
)
if mibBuilder.loadTexts:
    upsTrapImminentStop.setStatus(
        ""
    )

upsTrapOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 6)
)
if mibBuilder.loadTexts:
    upsTrapOverload.setStatus(
        ""
    )

upsTrapRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 7)
)
if mibBuilder.loadTexts:
    upsTrapRedundancyLost.setStatus(
        ""
    )

upsTrapBatteryCircuitOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 8)
)
if mibBuilder.loadTexts:
    upsTrapBatteryCircuitOpen.setStatus(
        ""
    )

upsTrapBatteryDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 9)
)
if mibBuilder.loadTexts:
    upsTrapBatteryDischarged.setStatus(
        ""
    )

upsTrapBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 10)
)
if mibBuilder.loadTexts:
    upsTrapBatteryLow.setStatus(
        ""
    )

upsTrapBatteryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 11)
)
if mibBuilder.loadTexts:
    upsTrapBatteryAlarm.setStatus(
        ""
    )

upsTrapUpsCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 12)
)
if mibBuilder.loadTexts:
    upsTrapUpsCriticalAlarm.setStatus(
        ""
    )

upsTrapLoadOFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 13)
)
if mibBuilder.loadTexts:
    upsTrapLoadOFF.setStatus(
        ""
    )

upsTrapCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 14)
)
if mibBuilder.loadTexts:
    upsTrapCommunicationLost.setStatus(
        ""
    )

upsTrapOnBatteryPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 15)
)
if mibBuilder.loadTexts:
    upsTrapOnBatteryPower.setStatus(
        ""
    )

upsTrapBatteryTestfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 16)
)
if mibBuilder.loadTexts:
    upsTrapBatteryTestfailed.setStatus(
        ""
    )

upsTrapTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 17)
)
if mibBuilder.loadTexts:
    upsTrapTemperatureAlarm.setStatus(
        ""
    )

upsTrapOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 18)
)
if mibBuilder.loadTexts:
    upsTrapOnBypass.setStatus(
        ""
    )

upsTrapUpsPreventiveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 19)
)
if mibBuilder.loadTexts:
    upsTrapUpsPreventiveAlarm.setStatus(
        ""
    )

upsTrapShutdownWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 20)
)
if mibBuilder.loadTexts:
    upsTrapShutdownWarning.setStatus(
        ""
    )

upsTrapShutdownrequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 21)
)
if mibBuilder.loadTexts:
    upsTrapShutdownrequest.setStatus(
        ""
    )

upsTrapUpsNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 22)
)
if mibBuilder.loadTexts:
    upsTrapUpsNormal.setStatus(
        ""
    )

upsTrapPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 23)
)
if mibBuilder.loadTexts:
    upsTrapPowerRestored.setStatus(
        ""
    )

upsTrapAlarmCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 24)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCancelled.setStatus(
        ""
    )

upsTrapComEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 25)
)
if mibBuilder.loadTexts:
    upsTrapComEstablished.setStatus(
        ""
    )

upsTrapShutdwonCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 26)
)
if mibBuilder.loadTexts:
    upsTrapShutdwonCancelled.setStatus(
        ""
    )

upsTrapAgentRestarting = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 27)
)
if mibBuilder.loadTexts:
    upsTrapAgentRestarting.setStatus(
        ""
    )

upsTrapEmdTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 28)
)
if mibBuilder.loadTexts:
    upsTrapEmdTempLow.setStatus(
        ""
    )

upsTrapEmdTempNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 29)
)
if mibBuilder.loadTexts:
    upsTrapEmdTempNotLow.setStatus(
        ""
    )

upsTrapEmdTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 30)
)
if mibBuilder.loadTexts:
    upsTrapEmdTempHigh.setStatus(
        ""
    )

upsTrapEmdTempNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 31)
)
if mibBuilder.loadTexts:
    upsTrapEmdTempNotHigh.setStatus(
        ""
    )

upsTrapEmdHumidityLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 32)
)
if mibBuilder.loadTexts:
    upsTrapEmdHumidityLow.setStatus(
        ""
    )

upsTrapEmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 33)
)
if mibBuilder.loadTexts:
    upsTrapEmdHumidityNotLow.setStatus(
        ""
    )

upsTrapEmdHumidityHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 34)
)
if mibBuilder.loadTexts:
    upsTrapEmdHumidityHigh.setStatus(
        ""
    )

upsTrapEmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 35)
)
if mibBuilder.loadTexts:
    upsTrapEmdHumidityNotHigh.setStatus(
        ""
    )

upsTrapEmdFirstInputActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 36)
)
if mibBuilder.loadTexts:
    upsTrapEmdFirstInputActive.setStatus(
        ""
    )

upsTrapEmdFirstInputRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 37)
)
if mibBuilder.loadTexts:
    upsTrapEmdFirstInputRestored.setStatus(
        ""
    )

upsTrapEmdSecondInputActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 38)
)
if mibBuilder.loadTexts:
    upsTrapEmdSecondInputActive.setStatus(
        ""
    )

upsTrapEmdSecondInputRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 39)
)
if mibBuilder.loadTexts:
    upsTrapEmdSecondInputRestored.setStatus(
        ""
    )

upsTrapSessionLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 40)
)
if mibBuilder.loadTexts:
    upsTrapSessionLogin.setStatus(
        ""
    )

upsTrapLoginUnsuccesfulTentative = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 41)
)
if mibBuilder.loadTexts:
    upsTrapLoginUnsuccesfulTentative.setStatus(
        ""
    )

upsTrapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 7, 2, 0, 42)
)
if mibBuilder.loadTexts:
    upsTrapTest.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SOCOMECUPS-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "socomec": socomec,
       "software": software,
       "network": network,
       "netvision7": netvision7,
       "upsObjects": upsObjects,
       "upsIdent": upsIdent,
       "upsIdentModel": upsIdentModel,
       "upsIdentSerialNumber": upsIdentSerialNumber,
       "upsIdentUserRef": upsIdentUserRef,
       "upsIdentUserLocation": upsIdentUserLocation,
       "upsIdentAgentSoftwareVersion": upsIdentAgentSoftwareVersion,
       "upsSystemName": upsSystemName,
       "upsSystemContact": upsSystemContact,
       "upsSystemLocation": upsSystemLocation,
       "upsBattery": upsBattery,
       "upsBatteryStatus": upsBatteryStatus,
       "upsSecondsOnBattery": upsSecondsOnBattery,
       "upsEstimatedMinutesRemaining": upsEstimatedMinutesRemaining,
       "upsEstimatedChargeRemaining": upsEstimatedChargeRemaining,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryTemperature": upsBatteryTemperature,
       "upsAmbientTemperature": upsAmbientTemperature,
       "upsBatteryCurrent": upsBatteryCurrent,
       "upsBatterySOC": upsBatterySOC,
       "upsInput": upsInput,
       "upsInputNumLines": upsInputNumLines,
       "upsInputFrequency": upsInputFrequency,
       "upsInputTable": upsInputTable,
       "upsInputEntry": upsInputEntry,
       "upsInputLineIndex": upsInputLineIndex,
       "upsInputVoltage": upsInputVoltage,
       "upsInputCurrent": upsInputCurrent,
       "upsInputVoltageMax": upsInputVoltageMax,
       "upsInputVoltageMin": upsInputVoltageMin,
       "upsOutput": upsOutput,
       "upsOutputSource": upsOutputSource,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputNumLines": upsOutputNumLines,
       "upsOutputTable": upsOutputTable,
       "upsOutputEntry": upsOutputEntry,
       "upsOutputLineIndex": upsOutputLineIndex,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputCurrent": upsOutputCurrent,
       "upsOutputPercentLoad": upsOutputPercentLoad,
       "upsOutputKva": upsOutputKva,
       "upsOutputKw": upsOutputKw,
       "upsOutputGlobalkVA": upsOutputGlobalkVA,
       "upsOutputGlobalkW": upsOutputGlobalkW,
       "upsOutputLoadRate": upsOutputLoadRate,
       "upsBypass": upsBypass,
       "upsBypassFrequency": upsBypassFrequency,
       "upsBypassNumLines": upsBypassNumLines,
       "upsBypassTable": upsBypassTable,
       "upsBypassEntry": upsBypassEntry,
       "upsBypassLineIndex": upsBypassLineIndex,
       "upsBypassVoltage": upsBypassVoltage,
       "upsBypassCurrent": upsBypassCurrent,
       "upsAlarm": upsAlarm,
       "upsAlarmsPresent": upsAlarmsPresent,
       "upsAlarmTable": upsAlarmTable,
       "upsAlarmEntry": upsAlarmEntry,
       "upsAlarmId": upsAlarmId,
       "upsAlarmDescr": upsAlarmDescr,
       "upsAlarmTime": upsAlarmTime,
       "upsAlarmExtDes": upsAlarmExtDes,
       "upsWellKnownAlarms": upsWellKnownAlarms,
       "upsAlarmImminentStop": upsAlarmImminentStop,
       "upsAlarmOverload": upsAlarmOverload,
       "upsAlarmTemperature": upsAlarmTemperature,
       "upsAlarmTransferLock": upsAlarmTransferLock,
       "upsAlarmAutoTransferImpossible": upsAlarmAutoTransferImpossible,
       "upsAlarmInsufficientResources": upsAlarmInsufficientResources,
       "upsAlarmRedundancyLost": upsAlarmRedundancyLost,
       "upsAlarmOutputShortCircuit": upsAlarmOutputShortCircuit,
       "upsAlarmMaintenance": upsAlarmMaintenance,
       "upsAlarmRemoteService": upsAlarmRemoteService,
       "upsAlarmGeneralFault": upsAlarmGeneralFault,
       "upsAlarmBatteryCircuitOpen": upsAlarmBatteryCircuitOpen,
       "upsAlarmBatteryDischarged": upsAlarmBatteryDischarged,
       "upsAlarmLowBattery": upsAlarmLowBattery,
       "upsAlarmOnBattery": upsAlarmOnBattery,
       "upsAlarmBatteryTemperature": upsAlarmBatteryTemperature,
       "upsAlarmBatteryRoom": upsAlarmBatteryRoom,
       "upsAlarmBatteryTest": upsAlarmBatteryTest,
       "upsAlarmBatteryFault": upsAlarmBatteryFault,
       "upsAlarmRectifierFault": upsAlarmRectifierFault,
       "upsAlarmRectifierAlarm": upsAlarmRectifierAlarm,
       "upsAlarmRecInputBad": upsAlarmRecInputBad,
       "upsAlarmGenSetGeneral": upsAlarmGenSetGeneral,
       "upsAlarmBatteryChargerFault": upsAlarmBatteryChargerFault,
       "upsAlarmBatteryChargerAlarm": upsAlarmBatteryChargerAlarm,
       "upsAlarmInverterFault": upsAlarmInverterFault,
       "upsAlarmInverterAlarm": upsAlarmInverterAlarm,
       "upsAlarmBypassFault": upsAlarmBypassFault,
       "upsAlarmBypassAlarm": upsAlarmBypassAlarm,
       "upsAlarmBypInputBad": upsAlarmBypInputBad,
       "upsAlarmPhaseRotationFault": upsAlarmPhaseRotationFault,
       "upsAlarmFansFailure": upsAlarmFansFailure,
       "upsAlarmMaintenanceBypass": upsAlarmMaintenanceBypass,
       "upsAlarmUPSPowerOffActive": upsAlarmUPSPowerOffActive,
       "upsAlarmWrongConfiguration": upsAlarmWrongConfiguration,
       "upsAlarmInternalFailure": upsAlarmInternalFailure,
       "upsAlarmOptionalBoards": upsAlarmOptionalBoards,
       "upsAlarmExternalAlarm1": upsAlarmExternalAlarm1,
       "upsAlarmExternalAlarm2": upsAlarmExternalAlarm2,
       "upsAlarmExternalAlarm3": upsAlarmExternalAlarm3,
       "upsAlarmExternalAlarm4": upsAlarmExternalAlarm4,
       "upsAlarmModule1Alarm": upsAlarmModule1Alarm,
       "upsAlarmModule2Alarm": upsAlarmModule2Alarm,
       "upsAlarmModule3Alarm": upsAlarmModule3Alarm,
       "upsAlarmModule4Alarm": upsAlarmModule4Alarm,
       "upsAlarmModule5Alarm": upsAlarmModule5Alarm,
       "upsAlarmModule6Alarm": upsAlarmModule6Alarm,
       "upsAlarmModule7Alarm": upsAlarmModule7Alarm,
       "upsAlarmModule8Alarm": upsAlarmModule8Alarm,
       "upsAlarmModule9Alarm": upsAlarmModule9Alarm,
       "upsAlarmModule10Alarm": upsAlarmModule10Alarm,
       "upsAlarmModule11Alarm": upsAlarmModule11Alarm,
       "upsAlarmModule12Alarm": upsAlarmModule12Alarm,
       "upsAlarmAutoTestRunning": upsAlarmAutoTestRunning,
       "upsAlarmOnBypass": upsAlarmOnBypass,
       "upsAlarmUpsOutputOff": upsAlarmUpsOutputOff,
       "upsAlarmUpsSystemOff": upsAlarmUpsSystemOff,
       "upsAlarmCommunicationLost": upsAlarmCommunicationLost,
       "upsAlarmShutdownPending": upsAlarmShutdownPending,
       "upsAlarmShutdownRequestt": upsAlarmShutdownRequestt,
       "upsAlarmShutdownImminent": upsAlarmShutdownImminent,
       "upsAlarmAwaitingPower": upsAlarmAwaitingPower,
       "upsControl": upsControl,
       "upsControlStatusControl": upsControlStatusControl,
       "upsShutdownDelay": upsShutdownDelay,
       "upsTurnOffAfterShutdown": upsTurnOffAfterShutdown,
       "upsControlShutdownParamTable": upsControlShutdownParamTable,
       "shutdownParamEntry": shutdownParamEntry,
       "upsControlEventIndex": upsControlEventIndex,
       "upsControlEventStatus": upsControlEventStatus,
       "upsControlDelay": upsControlDelay,
       "upsControlFirstWarning": upsControlFirstWarning,
       "upsControlWarningInterval": upsControlWarningInterval,
       "upsControlWeeklyScheduleTable": upsControlWeeklyScheduleTable,
       "upsControlWeeklyScheduleEntry": upsControlWeeklyScheduleEntry,
       "upsControlWeeklyIndex": upsControlWeeklyIndex,
       "upsControlWeeklyShutdownDay": upsControlWeeklyShutdownDay,
       "upsControlWeeklyShutdownTime": upsControlWeeklyShutdownTime,
       "upsControlWeeklyRestartDay": upsControlWeeklyRestartDay,
       "upsControlWeeklyRestartTime": upsControlWeeklyRestartTime,
       "upsControlSpecialScheduleTable": upsControlSpecialScheduleTable,
       "upsControlSpecialScheduleEntry": upsControlSpecialScheduleEntry,
       "upsControlSpecialIndex": upsControlSpecialIndex,
       "upsControlSpecialShutdownDay": upsControlSpecialShutdownDay,
       "upsControlSpecialShutdownTime": upsControlSpecialShutdownTime,
       "upsControlSpecialRestartDay": upsControlSpecialRestartDay,
       "upsControlSpecialRestartTime": upsControlSpecialRestartTime,
       "upsControlEcoModeScheduleTable": upsControlEcoModeScheduleTable,
       "upsControlEcoModeScheduleEntry": upsControlEcoModeScheduleEntry,
       "upsControlEcoModeIndex": upsControlEcoModeIndex,
       "upsControlEcoModeStartDay": upsControlEcoModeStartDay,
       "upsControlEcoModeStartTime": upsControlEcoModeStartTime,
       "upsControlEcoModeEndDay": upsControlEcoModeEndDay,
       "upsControlEcoModeEndTime": upsControlEcoModeEndTime,
       "upsConfig": upsConfig,
       "upsConfigNomKva": upsConfigNomKva,
       "upsConfigNbrUnit": upsConfigNbrUnit,
       "upsConfigUnitKva": upsConfigUnitKva,
       "upsConfigRemoteCtrl": upsConfigRemoteCtrl,
       "upsDevicesTable": upsDevicesTable,
       "upsDevicesEntry": upsDevicesEntry,
       "indexOfDevice": indexOfDevice,
       "addrOfDevice": addrOfDevice,
       "nameOfDevice": nameOfDevice,
       "timeOfConnection": timeOfConnection,
       "statusOfConnection": statusOfConnection,
       "severityOfConnection": severityOfConnection,
       "upsAgent": upsAgent,
       "upsAgentIpaddress": upsAgentIpaddress,
       "upsAgentGateway": upsAgentGateway,
       "upsAgentSubnetMask": upsAgentSubnetMask,
       "upsAgentDate": upsAgentDate,
       "upsAgentTime": upsAgentTime,
       "upsAgentNtpTimeServer": upsAgentNtpTimeServer,
       "upsAgentNtpTimeZone": upsAgentNtpTimeZone,
       "upsAgentHistoryLogFrequency": upsAgentHistoryLogFrequency,
       "upsAgentExtHistoryLogFrequency": upsAgentExtHistoryLogFrequency,
       "upsAgentPollRate": upsAgentPollRate,
       "upsAgentBaudRate": upsAgentBaudRate,
       "upsAgentDhcpStatue": upsAgentDhcpStatue,
       "upsAgentTelnetStatus": upsAgentTelnetStatus,
       "upsAgentTftpStatus": upsAgentTftpStatus,
       "upsAgentResetToDefault": upsAgentResetToDefault,
       "upsAgentRestart": upsAgentRestart,
       "upsAgentClearAgentLog": upsAgentClearAgentLog,
       "upsAgentClearEventLog": upsAgentClearEventLog,
       "upsAgentClearExtHistoryLog": upsAgentClearExtHistoryLog,
       "upsAgentClearHistoryLog": upsAgentClearHistoryLog,
       "upsAgentTrapsReceiversTable": upsAgentTrapsReceiversTable,
       "upsAgentTrapsReceiversEntry": upsAgentTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "receiverNmstype": receiverNmstype,
       "upsAgentFirewallControlTable": upsAgentFirewallControlTable,
       "upsAgentFirewallControlEntry": upsAgentFirewallControlEntry,
       "firewallIndex": firewallIndex,
       "firewallControlAddr": firewallControlAddr,
       "firewallPrefixLength": firewallPrefixLength,
       "firewallActionMode": firewallActionMode,
       "upsAgentMibVersion": upsAgentMibVersion,
       "emdStatus": emdStatus,
       "emdSatatusTemperature": emdSatatusTemperature,
       "emdSatatusHumidity": emdSatatusHumidity,
       "emdStatusIn1Active": emdStatusIn1Active,
       "emdStatusIn2Active": emdStatusIn2Active,
       "upsTraps": upsTraps,
       "upsTrapOnBattery": upsTrapOnBattery,
       "upsTrapTestCompleted": upsTrapTestCompleted,
       "upsTrapAlarmEntryAdded": upsTrapAlarmEntryAdded,
       "upsTrapAlarmEntryRemoved": upsTrapAlarmEntryRemoved,
       "upsTrapImminentStop": upsTrapImminentStop,
       "upsTrapOverload": upsTrapOverload,
       "upsTrapRedundancyLost": upsTrapRedundancyLost,
       "upsTrapBatteryCircuitOpen": upsTrapBatteryCircuitOpen,
       "upsTrapBatteryDischarged": upsTrapBatteryDischarged,
       "upsTrapBatteryLow": upsTrapBatteryLow,
       "upsTrapBatteryAlarm": upsTrapBatteryAlarm,
       "upsTrapUpsCriticalAlarm": upsTrapUpsCriticalAlarm,
       "upsTrapLoadOFF": upsTrapLoadOFF,
       "upsTrapCommunicationLost": upsTrapCommunicationLost,
       "upsTrapOnBatteryPower": upsTrapOnBatteryPower,
       "upsTrapBatteryTestfailed": upsTrapBatteryTestfailed,
       "upsTrapTemperatureAlarm": upsTrapTemperatureAlarm,
       "upsTrapOnBypass": upsTrapOnBypass,
       "upsTrapUpsPreventiveAlarm": upsTrapUpsPreventiveAlarm,
       "upsTrapShutdownWarning": upsTrapShutdownWarning,
       "upsTrapShutdownrequest": upsTrapShutdownrequest,
       "upsTrapUpsNormal": upsTrapUpsNormal,
       "upsTrapPowerRestored": upsTrapPowerRestored,
       "upsTrapAlarmCancelled": upsTrapAlarmCancelled,
       "upsTrapComEstablished": upsTrapComEstablished,
       "upsTrapShutdwonCancelled": upsTrapShutdwonCancelled,
       "upsTrapAgentRestarting": upsTrapAgentRestarting,
       "upsTrapEmdTempLow": upsTrapEmdTempLow,
       "upsTrapEmdTempNotLow": upsTrapEmdTempNotLow,
       "upsTrapEmdTempHigh": upsTrapEmdTempHigh,
       "upsTrapEmdTempNotHigh": upsTrapEmdTempNotHigh,
       "upsTrapEmdHumidityLow": upsTrapEmdHumidityLow,
       "upsTrapEmdHumidityNotLow": upsTrapEmdHumidityNotLow,
       "upsTrapEmdHumidityHigh": upsTrapEmdHumidityHigh,
       "upsTrapEmdHumidityNotHigh": upsTrapEmdHumidityNotHigh,
       "upsTrapEmdFirstInputActive": upsTrapEmdFirstInputActive,
       "upsTrapEmdFirstInputRestored": upsTrapEmdFirstInputRestored,
       "upsTrapEmdSecondInputActive": upsTrapEmdSecondInputActive,
       "upsTrapEmdSecondInputRestored": upsTrapEmdSecondInputRestored,
       "upsTrapSessionLogin": upsTrapSessionLogin,
       "upsTrapLoginUnsuccesfulTentative": upsTrapLoginUnsuccesfulTentative,
       "upsTrapTest": upsTrapTest}
)
