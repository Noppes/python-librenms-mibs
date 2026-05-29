# SNMP MIB module (PROBE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\megatec\PROBE-MIB

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

probe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mega_ObjectIdentity = ObjectIdentity
mega = _Mega_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409)
)
_ProbeStatus_ObjectIdentity = ObjectIdentity
probeStatus = _ProbeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1)
)
_ProbeStatusTemperature_Type = Integer32
_ProbeStatusTemperature_Object = MibScalar
probeStatusTemperature = _ProbeStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 1),
    _ProbeStatusTemperature_Type()
)
probeStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusTemperature.setStatus("current")
if mibBuilder.loadTexts:
    probeStatusTemperature.setUnits("0.1 degrees Centigrade")
_ProbeStatusHumidity_Type = Integer32
_ProbeStatusHumidity_Object = MibScalar
probeStatusHumidity = _ProbeStatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 2),
    _ProbeStatusHumidity_Type()
)
probeStatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusHumidity.setStatus("current")
if mibBuilder.loadTexts:
    probeStatusHumidity.setUnits("percentage")
_ProbeStatusItem1_Type = OctetString
_ProbeStatusItem1_Object = MibScalar
probeStatusItem1 = _ProbeStatusItem1_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 3),
    _ProbeStatusItem1_Type()
)
probeStatusItem1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusItem1.setStatus("current")
_ProbeStatusItem2_Type = OctetString
_ProbeStatusItem2_Object = MibScalar
probeStatusItem2 = _ProbeStatusItem2_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 4),
    _ProbeStatusItem2_Type()
)
probeStatusItem2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusItem2.setStatus("current")
_ProbeStatusItem3_Type = OctetString
_ProbeStatusItem3_Object = MibScalar
probeStatusItem3 = _ProbeStatusItem3_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 5),
    _ProbeStatusItem3_Type()
)
probeStatusItem3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusItem3.setStatus("current")
_ProbeStatusItem4_Type = OctetString
_ProbeStatusItem4_Object = MibScalar
probeStatusItem4 = _ProbeStatusItem4_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 6),
    _ProbeStatusItem4_Type()
)
probeStatusItem4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusItem4.setStatus("current")
_ProbeStatusItem5_Type = OctetString
_ProbeStatusItem5_Object = MibScalar
probeStatusItem5 = _ProbeStatusItem5_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 7),
    _ProbeStatusItem5_Type()
)
probeStatusItem5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusItem5.setStatus("current")
_ProbeStatusItem6_Type = OctetString
_ProbeStatusItem6_Object = MibScalar
probeStatusItem6 = _ProbeStatusItem6_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 8),
    _ProbeStatusItem6_Type()
)
probeStatusItem6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusItem6.setStatus("current")
_ProbeStatusItem7_Type = OctetString
_ProbeStatusItem7_Object = MibScalar
probeStatusItem7 = _ProbeStatusItem7_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 9),
    _ProbeStatusItem7_Type()
)
probeStatusItem7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusItem7.setStatus("current")
_ProbeStatusItem8_Type = OctetString
_ProbeStatusItem8_Object = MibScalar
probeStatusItem8 = _ProbeStatusItem8_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 1, 10),
    _ProbeStatusItem8_Type()
)
probeStatusItem8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeStatusItem8.setStatus("current")
_ProbeSetting_ObjectIdentity = ObjectIdentity
probeSetting = _ProbeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2)
)


class _SignalDetectionType_Type(Integer32):
    """Custom type signalDetectionType based on Integer32"""
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
        *(("analogInput", 1),
          ("differentialSignalInputBipolar", 2),
          ("differentialSignalInputUnipolar", 3),
          ("contactClosureInput", 4))
    )


_SignalDetectionType_Type.__name__ = "Integer32"
_SignalDetectionType_Object = MibScalar
signalDetectionType = _SignalDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 1),
    _SignalDetectionType_Type()
)
signalDetectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalDetectionType.setStatus("current")


class _TemperatureMax_Type(Integer32):
    """Custom type temperatureMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 100),
    )


_TemperatureMax_Type.__name__ = "Integer32"
_TemperatureMax_Object = MibScalar
temperatureMax = _TemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 2),
    _TemperatureMax_Type()
)
temperatureMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureMax.setStatus("current")
if mibBuilder.loadTexts:
    temperatureMax.setUnits("0.1 degrees Centigrade")


class _TemperatureMin_Type(Integer32):
    """Custom type temperatureMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 100),
    )


_TemperatureMin_Type.__name__ = "Integer32"
_TemperatureMin_Object = MibScalar
temperatureMin = _TemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 3),
    _TemperatureMin_Type()
)
temperatureMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureMin.setStatus("current")
if mibBuilder.loadTexts:
    temperatureMin.setUnits("0.1 degrees Centigrade")


class _HumidityMax_Type(Integer32):
    """Custom type humidityMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HumidityMax_Type.__name__ = "Integer32"
_HumidityMax_Object = MibScalar
humidityMax = _HumidityMax_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 4),
    _HumidityMax_Type()
)
humidityMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityMax.setStatus("current")
if mibBuilder.loadTexts:
    humidityMax.setUnits("percentage")


class _HumidityMin_Type(Integer32):
    """Custom type humidityMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HumidityMin_Type.__name__ = "Integer32"
_HumidityMin_Object = MibScalar
humidityMin = _HumidityMin_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 5),
    _HumidityMin_Type()
)
humidityMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityMin.setStatus("current")
if mibBuilder.loadTexts:
    humidityMin.setUnits("percentage")
_AnalogInput_ObjectIdentity = ObjectIdentity
analogInput = _AnalogInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6)
)
_AnalogInputGroup1_ObjectIdentity = ObjectIdentity
analogInputGroup1 = _AnalogInputGroup1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 1)
)


class _AnalogInputGroup1Caption_Type(OctetString):
    """Custom type analogInputGroup1Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AnalogInputGroup1Caption_Type.__name__ = "OctetString"
_AnalogInputGroup1Caption_Object = MibScalar
analogInputGroup1Caption = _AnalogInputGroup1Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 1, 1),
    _AnalogInputGroup1Caption_Type()
)
analogInputGroup1Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup1Caption.setStatus("current")
_AnalogInputGroup1Factor_Type = Integer32
_AnalogInputGroup1Factor_Object = MibScalar
analogInputGroup1Factor = _AnalogInputGroup1Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 1, 2),
    _AnalogInputGroup1Factor_Type()
)
analogInputGroup1Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup1Factor.setStatus("current")
_AnalogInputGroup1Unit_Type = OctetString
_AnalogInputGroup1Unit_Object = MibScalar
analogInputGroup1Unit = _AnalogInputGroup1Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 1, 3),
    _AnalogInputGroup1Unit_Type()
)
analogInputGroup1Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup1Unit.setStatus("current")
_AnalogInputGroup1Max_Type = Integer32
_AnalogInputGroup1Max_Object = MibScalar
analogInputGroup1Max = _AnalogInputGroup1Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 1, 4),
    _AnalogInputGroup1Max_Type()
)
analogInputGroup1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup1Max.setStatus("current")
_AnalogInputGroup1Min_Type = Integer32
_AnalogInputGroup1Min_Object = MibScalar
analogInputGroup1Min = _AnalogInputGroup1Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 1, 5),
    _AnalogInputGroup1Min_Type()
)
analogInputGroup1Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup1Min.setStatus("current")
_AnalogInputGroup2_ObjectIdentity = ObjectIdentity
analogInputGroup2 = _AnalogInputGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 2)
)


class _AnalogInputGroup2Caption_Type(OctetString):
    """Custom type analogInputGroup2Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AnalogInputGroup2Caption_Type.__name__ = "OctetString"
_AnalogInputGroup2Caption_Object = MibScalar
analogInputGroup2Caption = _AnalogInputGroup2Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 2, 1),
    _AnalogInputGroup2Caption_Type()
)
analogInputGroup2Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup2Caption.setStatus("current")
_AnalogInputGroup2Factor_Type = Integer32
_AnalogInputGroup2Factor_Object = MibScalar
analogInputGroup2Factor = _AnalogInputGroup2Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 2, 2),
    _AnalogInputGroup2Factor_Type()
)
analogInputGroup2Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup2Factor.setStatus("current")
_AnalogInputGroup2Unit_Type = OctetString
_AnalogInputGroup2Unit_Object = MibScalar
analogInputGroup2Unit = _AnalogInputGroup2Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 2, 3),
    _AnalogInputGroup2Unit_Type()
)
analogInputGroup2Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup2Unit.setStatus("current")
_AnalogInputGroup2Max_Type = Integer32
_AnalogInputGroup2Max_Object = MibScalar
analogInputGroup2Max = _AnalogInputGroup2Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 2, 4),
    _AnalogInputGroup2Max_Type()
)
analogInputGroup2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup2Max.setStatus("current")
_AnalogInputGroup2Min_Type = Integer32
_AnalogInputGroup2Min_Object = MibScalar
analogInputGroup2Min = _AnalogInputGroup2Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 2, 5),
    _AnalogInputGroup2Min_Type()
)
analogInputGroup2Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup2Min.setStatus("current")
_AnalogInputGroup3_ObjectIdentity = ObjectIdentity
analogInputGroup3 = _AnalogInputGroup3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 3)
)


class _AnalogInputGroup3Caption_Type(OctetString):
    """Custom type analogInputGroup3Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AnalogInputGroup3Caption_Type.__name__ = "OctetString"
_AnalogInputGroup3Caption_Object = MibScalar
analogInputGroup3Caption = _AnalogInputGroup3Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 3, 1),
    _AnalogInputGroup3Caption_Type()
)
analogInputGroup3Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup3Caption.setStatus("current")
_AnalogInputGroup3Factor_Type = Integer32
_AnalogInputGroup3Factor_Object = MibScalar
analogInputGroup3Factor = _AnalogInputGroup3Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 3, 2),
    _AnalogInputGroup3Factor_Type()
)
analogInputGroup3Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup3Factor.setStatus("current")
_AnalogInputGroup3Unit_Type = OctetString
_AnalogInputGroup3Unit_Object = MibScalar
analogInputGroup3Unit = _AnalogInputGroup3Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 3, 3),
    _AnalogInputGroup3Unit_Type()
)
analogInputGroup3Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup3Unit.setStatus("current")
_AnalogInputGroup3Max_Type = Integer32
_AnalogInputGroup3Max_Object = MibScalar
analogInputGroup3Max = _AnalogInputGroup3Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 3, 4),
    _AnalogInputGroup3Max_Type()
)
analogInputGroup3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup3Max.setStatus("current")
_AnalogInputGroup3Min_Type = Integer32
_AnalogInputGroup3Min_Object = MibScalar
analogInputGroup3Min = _AnalogInputGroup3Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 3, 5),
    _AnalogInputGroup3Min_Type()
)
analogInputGroup3Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup3Min.setStatus("current")
_AnalogInputGroup4_ObjectIdentity = ObjectIdentity
analogInputGroup4 = _AnalogInputGroup4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 4)
)


class _AnalogInputGroup4Caption_Type(OctetString):
    """Custom type analogInputGroup4Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AnalogInputGroup4Caption_Type.__name__ = "OctetString"
_AnalogInputGroup4Caption_Object = MibScalar
analogInputGroup4Caption = _AnalogInputGroup4Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 4, 1),
    _AnalogInputGroup4Caption_Type()
)
analogInputGroup4Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup4Caption.setStatus("current")
_AnalogInputGroup4Factor_Type = Integer32
_AnalogInputGroup4Factor_Object = MibScalar
analogInputGroup4Factor = _AnalogInputGroup4Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 4, 2),
    _AnalogInputGroup4Factor_Type()
)
analogInputGroup4Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup4Factor.setStatus("current")
_AnalogInputGroup4Unit_Type = OctetString
_AnalogInputGroup4Unit_Object = MibScalar
analogInputGroup4Unit = _AnalogInputGroup4Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 4, 3),
    _AnalogInputGroup4Unit_Type()
)
analogInputGroup4Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup4Unit.setStatus("current")
_AnalogInputGroup4Max_Type = Integer32
_AnalogInputGroup4Max_Object = MibScalar
analogInputGroup4Max = _AnalogInputGroup4Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 4, 4),
    _AnalogInputGroup4Max_Type()
)
analogInputGroup4Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup4Max.setStatus("current")
_AnalogInputGroup4Min_Type = Integer32
_AnalogInputGroup4Min_Object = MibScalar
analogInputGroup4Min = _AnalogInputGroup4Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 4, 5),
    _AnalogInputGroup4Min_Type()
)
analogInputGroup4Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup4Min.setStatus("current")
_AnalogInputGroup5_ObjectIdentity = ObjectIdentity
analogInputGroup5 = _AnalogInputGroup5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 5)
)


class _AnalogInputGroup5Caption_Type(OctetString):
    """Custom type analogInputGroup5Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AnalogInputGroup5Caption_Type.__name__ = "OctetString"
_AnalogInputGroup5Caption_Object = MibScalar
analogInputGroup5Caption = _AnalogInputGroup5Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 5, 1),
    _AnalogInputGroup5Caption_Type()
)
analogInputGroup5Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup5Caption.setStatus("current")
_AnalogInputGroup5Factor_Type = Integer32
_AnalogInputGroup5Factor_Object = MibScalar
analogInputGroup5Factor = _AnalogInputGroup5Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 5, 2),
    _AnalogInputGroup5Factor_Type()
)
analogInputGroup5Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup5Factor.setStatus("current")
_AnalogInputGroup5Unit_Type = OctetString
_AnalogInputGroup5Unit_Object = MibScalar
analogInputGroup5Unit = _AnalogInputGroup5Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 5, 3),
    _AnalogInputGroup5Unit_Type()
)
analogInputGroup5Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup5Unit.setStatus("current")
_AnalogInputGroup5Max_Type = Integer32
_AnalogInputGroup5Max_Object = MibScalar
analogInputGroup5Max = _AnalogInputGroup5Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 5, 4),
    _AnalogInputGroup5Max_Type()
)
analogInputGroup5Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup5Max.setStatus("current")
_AnalogInputGroup5Min_Type = Integer32
_AnalogInputGroup5Min_Object = MibScalar
analogInputGroup5Min = _AnalogInputGroup5Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 5, 5),
    _AnalogInputGroup5Min_Type()
)
analogInputGroup5Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup5Min.setStatus("current")
_AnalogInputGroup6_ObjectIdentity = ObjectIdentity
analogInputGroup6 = _AnalogInputGroup6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 6)
)


class _AnalogInputGroup6Caption_Type(OctetString):
    """Custom type analogInputGroup6Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AnalogInputGroup6Caption_Type.__name__ = "OctetString"
_AnalogInputGroup6Caption_Object = MibScalar
analogInputGroup6Caption = _AnalogInputGroup6Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 6, 1),
    _AnalogInputGroup6Caption_Type()
)
analogInputGroup6Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup6Caption.setStatus("current")
_AnalogInputGroup6Factor_Type = Integer32
_AnalogInputGroup6Factor_Object = MibScalar
analogInputGroup6Factor = _AnalogInputGroup6Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 6, 2),
    _AnalogInputGroup6Factor_Type()
)
analogInputGroup6Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup6Factor.setStatus("current")
_AnalogInputGroup6Unit_Type = OctetString
_AnalogInputGroup6Unit_Object = MibScalar
analogInputGroup6Unit = _AnalogInputGroup6Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 6, 3),
    _AnalogInputGroup6Unit_Type()
)
analogInputGroup6Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup6Unit.setStatus("current")
_AnalogInputGroup6Max_Type = Integer32
_AnalogInputGroup6Max_Object = MibScalar
analogInputGroup6Max = _AnalogInputGroup6Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 6, 4),
    _AnalogInputGroup6Max_Type()
)
analogInputGroup6Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup6Max.setStatus("current")
_AnalogInputGroup6Min_Type = Integer32
_AnalogInputGroup6Min_Object = MibScalar
analogInputGroup6Min = _AnalogInputGroup6Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 6, 5),
    _AnalogInputGroup6Min_Type()
)
analogInputGroup6Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup6Min.setStatus("current")
_AnalogInputGroup7_ObjectIdentity = ObjectIdentity
analogInputGroup7 = _AnalogInputGroup7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 7)
)


class _AnalogInputGroup7Caption_Type(OctetString):
    """Custom type analogInputGroup7Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AnalogInputGroup7Caption_Type.__name__ = "OctetString"
_AnalogInputGroup7Caption_Object = MibScalar
analogInputGroup7Caption = _AnalogInputGroup7Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 7, 1),
    _AnalogInputGroup7Caption_Type()
)
analogInputGroup7Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup7Caption.setStatus("current")
_AnalogInputGroup7Factor_Type = Integer32
_AnalogInputGroup7Factor_Object = MibScalar
analogInputGroup7Factor = _AnalogInputGroup7Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 7, 2),
    _AnalogInputGroup7Factor_Type()
)
analogInputGroup7Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup7Factor.setStatus("current")
_AnalogInputGroup7Unit_Type = OctetString
_AnalogInputGroup7Unit_Object = MibScalar
analogInputGroup7Unit = _AnalogInputGroup7Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 7, 3),
    _AnalogInputGroup7Unit_Type()
)
analogInputGroup7Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup7Unit.setStatus("current")
_AnalogInputGroup7Max_Type = Integer32
_AnalogInputGroup7Max_Object = MibScalar
analogInputGroup7Max = _AnalogInputGroup7Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 7, 4),
    _AnalogInputGroup7Max_Type()
)
analogInputGroup7Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup7Max.setStatus("current")
_AnalogInputGroup7Min_Type = Integer32
_AnalogInputGroup7Min_Object = MibScalar
analogInputGroup7Min = _AnalogInputGroup7Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 7, 5),
    _AnalogInputGroup7Min_Type()
)
analogInputGroup7Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup7Min.setStatus("current")
_AnalogInputGroup8_ObjectIdentity = ObjectIdentity
analogInputGroup8 = _AnalogInputGroup8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 8)
)


class _AnalogInputGroup8Caption_Type(OctetString):
    """Custom type analogInputGroup8Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AnalogInputGroup8Caption_Type.__name__ = "OctetString"
_AnalogInputGroup8Caption_Object = MibScalar
analogInputGroup8Caption = _AnalogInputGroup8Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 8, 1),
    _AnalogInputGroup8Caption_Type()
)
analogInputGroup8Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup8Caption.setStatus("current")
_AnalogInputGroup8Factor_Type = Integer32
_AnalogInputGroup8Factor_Object = MibScalar
analogInputGroup8Factor = _AnalogInputGroup8Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 8, 2),
    _AnalogInputGroup8Factor_Type()
)
analogInputGroup8Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup8Factor.setStatus("current")
_AnalogInputGroup8Unit_Type = OctetString
_AnalogInputGroup8Unit_Object = MibScalar
analogInputGroup8Unit = _AnalogInputGroup8Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 8, 3),
    _AnalogInputGroup8Unit_Type()
)
analogInputGroup8Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup8Unit.setStatus("current")
_AnalogInputGroup8Max_Type = Integer32
_AnalogInputGroup8Max_Object = MibScalar
analogInputGroup8Max = _AnalogInputGroup8Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 8, 4),
    _AnalogInputGroup8Max_Type()
)
analogInputGroup8Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup8Max.setStatus("current")
_AnalogInputGroup8Min_Type = Integer32
_AnalogInputGroup8Min_Object = MibScalar
analogInputGroup8Min = _AnalogInputGroup8Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 6, 8, 5),
    _AnalogInputGroup8Min_Type()
)
analogInputGroup8Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInputGroup8Min.setStatus("current")
_DifferentialSignalInputBipolar_ObjectIdentity = ObjectIdentity
differentialSignalInputBipolar = _DifferentialSignalInputBipolar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7)
)
_DifferentialSignalInputBipolarGroup1_ObjectIdentity = ObjectIdentity
differentialSignalInputBipolarGroup1 = _DifferentialSignalInputBipolarGroup1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 1)
)


class _DifferentialSignalInputBipolarGroup1Caption_Type(OctetString):
    """Custom type differentialSignalInputBipolarGroup1Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DifferentialSignalInputBipolarGroup1Caption_Type.__name__ = "OctetString"
_DifferentialSignalInputBipolarGroup1Caption_Object = MibScalar
differentialSignalInputBipolarGroup1Caption = _DifferentialSignalInputBipolarGroup1Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 1, 1),
    _DifferentialSignalInputBipolarGroup1Caption_Type()
)
differentialSignalInputBipolarGroup1Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup1Caption.setStatus("current")
_DifferentialSignalInputBipolarGroup1Factor_Type = Integer32
_DifferentialSignalInputBipolarGroup1Factor_Object = MibScalar
differentialSignalInputBipolarGroup1Factor = _DifferentialSignalInputBipolarGroup1Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 1, 2),
    _DifferentialSignalInputBipolarGroup1Factor_Type()
)
differentialSignalInputBipolarGroup1Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup1Factor.setStatus("current")
_DifferentialSignalInputBipolarGroup1Unit_Type = OctetString
_DifferentialSignalInputBipolarGroup1Unit_Object = MibScalar
differentialSignalInputBipolarGroup1Unit = _DifferentialSignalInputBipolarGroup1Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 1, 3),
    _DifferentialSignalInputBipolarGroup1Unit_Type()
)
differentialSignalInputBipolarGroup1Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup1Unit.setStatus("current")
_DifferentialSignalInputBipolarGroup1Max_Type = Integer32
_DifferentialSignalInputBipolarGroup1Max_Object = MibScalar
differentialSignalInputBipolarGroup1Max = _DifferentialSignalInputBipolarGroup1Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 1, 4),
    _DifferentialSignalInputBipolarGroup1Max_Type()
)
differentialSignalInputBipolarGroup1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup1Max.setStatus("current")
_DifferentialSignalInputBipolarGroup1Min_Type = Integer32
_DifferentialSignalInputBipolarGroup1Min_Object = MibScalar
differentialSignalInputBipolarGroup1Min = _DifferentialSignalInputBipolarGroup1Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 1, 5),
    _DifferentialSignalInputBipolarGroup1Min_Type()
)
differentialSignalInputBipolarGroup1Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup1Min.setStatus("current")
_DifferentialSignalInputBipolarGroup2_ObjectIdentity = ObjectIdentity
differentialSignalInputBipolarGroup2 = _DifferentialSignalInputBipolarGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 2)
)


class _DifferentialSignalInputBipolarGroup2Caption_Type(OctetString):
    """Custom type differentialSignalInputBipolarGroup2Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DifferentialSignalInputBipolarGroup2Caption_Type.__name__ = "OctetString"
_DifferentialSignalInputBipolarGroup2Caption_Object = MibScalar
differentialSignalInputBipolarGroup2Caption = _DifferentialSignalInputBipolarGroup2Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 2, 1),
    _DifferentialSignalInputBipolarGroup2Caption_Type()
)
differentialSignalInputBipolarGroup2Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup2Caption.setStatus("current")
_DifferentialSignalInputBipolarGroup2Factor_Type = Integer32
_DifferentialSignalInputBipolarGroup2Factor_Object = MibScalar
differentialSignalInputBipolarGroup2Factor = _DifferentialSignalInputBipolarGroup2Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 2, 2),
    _DifferentialSignalInputBipolarGroup2Factor_Type()
)
differentialSignalInputBipolarGroup2Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup2Factor.setStatus("current")
_DifferentialSignalInputBipolarGroup2Unit_Type = OctetString
_DifferentialSignalInputBipolarGroup2Unit_Object = MibScalar
differentialSignalInputBipolarGroup2Unit = _DifferentialSignalInputBipolarGroup2Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 2, 3),
    _DifferentialSignalInputBipolarGroup2Unit_Type()
)
differentialSignalInputBipolarGroup2Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup2Unit.setStatus("current")
_DifferentialSignalInputBipolarGroup2Max_Type = Integer32
_DifferentialSignalInputBipolarGroup2Max_Object = MibScalar
differentialSignalInputBipolarGroup2Max = _DifferentialSignalInputBipolarGroup2Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 2, 4),
    _DifferentialSignalInputBipolarGroup2Max_Type()
)
differentialSignalInputBipolarGroup2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup2Max.setStatus("current")
_DifferentialSignalInputBipolarGroup2Min_Type = Integer32
_DifferentialSignalInputBipolarGroup2Min_Object = MibScalar
differentialSignalInputBipolarGroup2Min = _DifferentialSignalInputBipolarGroup2Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 2, 5),
    _DifferentialSignalInputBipolarGroup2Min_Type()
)
differentialSignalInputBipolarGroup2Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup2Min.setStatus("current")
_DifferentialSignalInputBipolarGroup3_ObjectIdentity = ObjectIdentity
differentialSignalInputBipolarGroup3 = _DifferentialSignalInputBipolarGroup3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 3)
)


class _DifferentialSignalInputBipolarGroup3Caption_Type(OctetString):
    """Custom type differentialSignalInputBipolarGroup3Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DifferentialSignalInputBipolarGroup3Caption_Type.__name__ = "OctetString"
_DifferentialSignalInputBipolarGroup3Caption_Object = MibScalar
differentialSignalInputBipolarGroup3Caption = _DifferentialSignalInputBipolarGroup3Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 3, 1),
    _DifferentialSignalInputBipolarGroup3Caption_Type()
)
differentialSignalInputBipolarGroup3Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup3Caption.setStatus("current")
_DifferentialSignalInputBipolarGroup3Factor_Type = Integer32
_DifferentialSignalInputBipolarGroup3Factor_Object = MibScalar
differentialSignalInputBipolarGroup3Factor = _DifferentialSignalInputBipolarGroup3Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 3, 2),
    _DifferentialSignalInputBipolarGroup3Factor_Type()
)
differentialSignalInputBipolarGroup3Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup3Factor.setStatus("current")
_DifferentialSignalInputBipolarGroup3Unit_Type = OctetString
_DifferentialSignalInputBipolarGroup3Unit_Object = MibScalar
differentialSignalInputBipolarGroup3Unit = _DifferentialSignalInputBipolarGroup3Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 3, 3),
    _DifferentialSignalInputBipolarGroup3Unit_Type()
)
differentialSignalInputBipolarGroup3Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup3Unit.setStatus("current")
_DifferentialSignalInputBipolarGroup3Max_Type = Integer32
_DifferentialSignalInputBipolarGroup3Max_Object = MibScalar
differentialSignalInputBipolarGroup3Max = _DifferentialSignalInputBipolarGroup3Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 3, 4),
    _DifferentialSignalInputBipolarGroup3Max_Type()
)
differentialSignalInputBipolarGroup3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup3Max.setStatus("current")
_DifferentialSignalInputBipolarGroup3Min_Type = Integer32
_DifferentialSignalInputBipolarGroup3Min_Object = MibScalar
differentialSignalInputBipolarGroup3Min = _DifferentialSignalInputBipolarGroup3Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 3, 5),
    _DifferentialSignalInputBipolarGroup3Min_Type()
)
differentialSignalInputBipolarGroup3Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup3Min.setStatus("current")
_DifferentialSignalInputBipolarGroup4_ObjectIdentity = ObjectIdentity
differentialSignalInputBipolarGroup4 = _DifferentialSignalInputBipolarGroup4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 4)
)


class _DifferentialSignalInputBipolarGroup4Caption_Type(OctetString):
    """Custom type differentialSignalInputBipolarGroup4Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DifferentialSignalInputBipolarGroup4Caption_Type.__name__ = "OctetString"
_DifferentialSignalInputBipolarGroup4Caption_Object = MibScalar
differentialSignalInputBipolarGroup4Caption = _DifferentialSignalInputBipolarGroup4Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 4, 1),
    _DifferentialSignalInputBipolarGroup4Caption_Type()
)
differentialSignalInputBipolarGroup4Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup4Caption.setStatus("current")
_DifferentialSignalInputBipolarGroup4Factor_Type = Integer32
_DifferentialSignalInputBipolarGroup4Factor_Object = MibScalar
differentialSignalInputBipolarGroup4Factor = _DifferentialSignalInputBipolarGroup4Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 4, 2),
    _DifferentialSignalInputBipolarGroup4Factor_Type()
)
differentialSignalInputBipolarGroup4Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup4Factor.setStatus("current")
_DifferentialSignalInputBipolarGroup4Unit_Type = OctetString
_DifferentialSignalInputBipolarGroup4Unit_Object = MibScalar
differentialSignalInputBipolarGroup4Unit = _DifferentialSignalInputBipolarGroup4Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 4, 3),
    _DifferentialSignalInputBipolarGroup4Unit_Type()
)
differentialSignalInputBipolarGroup4Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup4Unit.setStatus("current")
_DifferentialSignalInputBipolarGroup4Max_Type = Integer32
_DifferentialSignalInputBipolarGroup4Max_Object = MibScalar
differentialSignalInputBipolarGroup4Max = _DifferentialSignalInputBipolarGroup4Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 4, 4),
    _DifferentialSignalInputBipolarGroup4Max_Type()
)
differentialSignalInputBipolarGroup4Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup4Max.setStatus("current")
_DifferentialSignalInputBipolarGroup4Min_Type = Integer32
_DifferentialSignalInputBipolarGroup4Min_Object = MibScalar
differentialSignalInputBipolarGroup4Min = _DifferentialSignalInputBipolarGroup4Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 7, 4, 5),
    _DifferentialSignalInputBipolarGroup4Min_Type()
)
differentialSignalInputBipolarGroup4Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup4Min.setStatus("current")
_DifferentialSignalInputUnipolar_ObjectIdentity = ObjectIdentity
differentialSignalInputUnipolar = _DifferentialSignalInputUnipolar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8)
)
_DifferentialSignalInputUnipolarGroup1_ObjectIdentity = ObjectIdentity
differentialSignalInputUnipolarGroup1 = _DifferentialSignalInputUnipolarGroup1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 1)
)


class _DifferentialSignalInputUnipolarGroup1Caption_Type(OctetString):
    """Custom type differentialSignalInputUnipolarGroup1Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DifferentialSignalInputUnipolarGroup1Caption_Type.__name__ = "OctetString"
_DifferentialSignalInputUnipolarGroup1Caption_Object = MibScalar
differentialSignalInputUnipolarGroup1Caption = _DifferentialSignalInputUnipolarGroup1Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 1, 1),
    _DifferentialSignalInputUnipolarGroup1Caption_Type()
)
differentialSignalInputUnipolarGroup1Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup1Caption.setStatus("current")
_DifferentialSignalInputUnipolarGroup1Factor_Type = Integer32
_DifferentialSignalInputUnipolarGroup1Factor_Object = MibScalar
differentialSignalInputUnipolarGroup1Factor = _DifferentialSignalInputUnipolarGroup1Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 1, 2),
    _DifferentialSignalInputUnipolarGroup1Factor_Type()
)
differentialSignalInputUnipolarGroup1Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup1Factor.setStatus("current")
_DifferentialSignalInputUnipolarGroup1Unit_Type = OctetString
_DifferentialSignalInputUnipolarGroup1Unit_Object = MibScalar
differentialSignalInputUnipolarGroup1Unit = _DifferentialSignalInputUnipolarGroup1Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 1, 3),
    _DifferentialSignalInputUnipolarGroup1Unit_Type()
)
differentialSignalInputUnipolarGroup1Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup1Unit.setStatus("current")
_DifferentialSignalInputUnipolarGroup1Max_Type = Integer32
_DifferentialSignalInputUnipolarGroup1Max_Object = MibScalar
differentialSignalInputUnipolarGroup1Max = _DifferentialSignalInputUnipolarGroup1Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 1, 4),
    _DifferentialSignalInputUnipolarGroup1Max_Type()
)
differentialSignalInputUnipolarGroup1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup1Max.setStatus("current")
_DifferentialSignalInputUnipolarGroup1Min_Type = Integer32
_DifferentialSignalInputUnipolarGroup1Min_Object = MibScalar
differentialSignalInputUnipolarGroup1Min = _DifferentialSignalInputUnipolarGroup1Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 1, 5),
    _DifferentialSignalInputUnipolarGroup1Min_Type()
)
differentialSignalInputUnipolarGroup1Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup1Min.setStatus("current")
_DifferentialSignalInputUnipolarGroup2_ObjectIdentity = ObjectIdentity
differentialSignalInputUnipolarGroup2 = _DifferentialSignalInputUnipolarGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 2)
)


class _DifferentialSignalInputUnipolarGroup2Caption_Type(OctetString):
    """Custom type differentialSignalInputUnipolarGroup2Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DifferentialSignalInputUnipolarGroup2Caption_Type.__name__ = "OctetString"
_DifferentialSignalInputUnipolarGroup2Caption_Object = MibScalar
differentialSignalInputUnipolarGroup2Caption = _DifferentialSignalInputUnipolarGroup2Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 2, 1),
    _DifferentialSignalInputUnipolarGroup2Caption_Type()
)
differentialSignalInputUnipolarGroup2Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup2Caption.setStatus("current")
_DifferentialSignalInputUnipolarGroup2Factor_Type = Integer32
_DifferentialSignalInputUnipolarGroup2Factor_Object = MibScalar
differentialSignalInputUnipolarGroup2Factor = _DifferentialSignalInputUnipolarGroup2Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 2, 2),
    _DifferentialSignalInputUnipolarGroup2Factor_Type()
)
differentialSignalInputUnipolarGroup2Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup2Factor.setStatus("current")
_DifferentialSignalInputUnipolarGroup2Unit_Type = OctetString
_DifferentialSignalInputUnipolarGroup2Unit_Object = MibScalar
differentialSignalInputUnipolarGroup2Unit = _DifferentialSignalInputUnipolarGroup2Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 2, 3),
    _DifferentialSignalInputUnipolarGroup2Unit_Type()
)
differentialSignalInputUnipolarGroup2Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup2Unit.setStatus("current")
_DifferentialSignalInputUnipolarGroup2Max_Type = Integer32
_DifferentialSignalInputUnipolarGroup2Max_Object = MibScalar
differentialSignalInputUnipolarGroup2Max = _DifferentialSignalInputUnipolarGroup2Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 2, 4),
    _DifferentialSignalInputUnipolarGroup2Max_Type()
)
differentialSignalInputUnipolarGroup2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup2Max.setStatus("current")
_DifferentialSignalInputUnipolarGroup2Min_Type = Integer32
_DifferentialSignalInputUnipolarGroup2Min_Object = MibScalar
differentialSignalInputUnipolarGroup2Min = _DifferentialSignalInputUnipolarGroup2Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 2, 5),
    _DifferentialSignalInputUnipolarGroup2Min_Type()
)
differentialSignalInputUnipolarGroup2Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup2Min.setStatus("current")
_DifferentialSignalInputUnipolarGroup3_ObjectIdentity = ObjectIdentity
differentialSignalInputUnipolarGroup3 = _DifferentialSignalInputUnipolarGroup3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 3)
)


class _DifferentialSignalInputUnipolarGroup3Caption_Type(OctetString):
    """Custom type differentialSignalInputUnipolarGroup3Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DifferentialSignalInputUnipolarGroup3Caption_Type.__name__ = "OctetString"
_DifferentialSignalInputUnipolarGroup3Caption_Object = MibScalar
differentialSignalInputUnipolarGroup3Caption = _DifferentialSignalInputUnipolarGroup3Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 3, 1),
    _DifferentialSignalInputUnipolarGroup3Caption_Type()
)
differentialSignalInputUnipolarGroup3Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup3Caption.setStatus("current")
_DifferentialSignalInputUnipolarGroup3Factor_Type = Integer32
_DifferentialSignalInputUnipolarGroup3Factor_Object = MibScalar
differentialSignalInputUnipolarGroup3Factor = _DifferentialSignalInputUnipolarGroup3Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 3, 2),
    _DifferentialSignalInputUnipolarGroup3Factor_Type()
)
differentialSignalInputUnipolarGroup3Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup3Factor.setStatus("current")
_DifferentialSignalInputUnipolarGroup3Unit_Type = OctetString
_DifferentialSignalInputUnipolarGroup3Unit_Object = MibScalar
differentialSignalInputUnipolarGroup3Unit = _DifferentialSignalInputUnipolarGroup3Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 3, 3),
    _DifferentialSignalInputUnipolarGroup3Unit_Type()
)
differentialSignalInputUnipolarGroup3Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup3Unit.setStatus("current")
_DifferentialSignalInputUnipolarGroup3Max_Type = Integer32
_DifferentialSignalInputUnipolarGroup3Max_Object = MibScalar
differentialSignalInputUnipolarGroup3Max = _DifferentialSignalInputUnipolarGroup3Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 3, 4),
    _DifferentialSignalInputUnipolarGroup3Max_Type()
)
differentialSignalInputUnipolarGroup3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup3Max.setStatus("current")
_DifferentialSignalInputUnipolarGroup3Min_Type = Integer32
_DifferentialSignalInputUnipolarGroup3Min_Object = MibScalar
differentialSignalInputUnipolarGroup3Min = _DifferentialSignalInputUnipolarGroup3Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 3, 5),
    _DifferentialSignalInputUnipolarGroup3Min_Type()
)
differentialSignalInputUnipolarGroup3Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup3Min.setStatus("current")
_DifferentialSignalInputUnipolarGroup4_ObjectIdentity = ObjectIdentity
differentialSignalInputUnipolarGroup4 = _DifferentialSignalInputUnipolarGroup4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 4)
)


class _DifferentialSignalInputUnipolarGroup4Caption_Type(OctetString):
    """Custom type differentialSignalInputUnipolarGroup4Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DifferentialSignalInputUnipolarGroup4Caption_Type.__name__ = "OctetString"
_DifferentialSignalInputUnipolarGroup4Caption_Object = MibScalar
differentialSignalInputUnipolarGroup4Caption = _DifferentialSignalInputUnipolarGroup4Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 4, 1),
    _DifferentialSignalInputUnipolarGroup4Caption_Type()
)
differentialSignalInputUnipolarGroup4Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup4Caption.setStatus("current")
_DifferentialSignalInputUnipolarGroup4Factor_Type = Integer32
_DifferentialSignalInputUnipolarGroup4Factor_Object = MibScalar
differentialSignalInputUnipolarGroup4Factor = _DifferentialSignalInputUnipolarGroup4Factor_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 4, 2),
    _DifferentialSignalInputUnipolarGroup4Factor_Type()
)
differentialSignalInputUnipolarGroup4Factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup4Factor.setStatus("current")
_DifferentialSignalInputUnipolarGroup4Unit_Type = OctetString
_DifferentialSignalInputUnipolarGroup4Unit_Object = MibScalar
differentialSignalInputUnipolarGroup4Unit = _DifferentialSignalInputUnipolarGroup4Unit_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 4, 3),
    _DifferentialSignalInputUnipolarGroup4Unit_Type()
)
differentialSignalInputUnipolarGroup4Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup4Unit.setStatus("current")
_DifferentialSignalInputUnipolarGroup4Max_Type = Integer32
_DifferentialSignalInputUnipolarGroup4Max_Object = MibScalar
differentialSignalInputUnipolarGroup4Max = _DifferentialSignalInputUnipolarGroup4Max_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 4, 4),
    _DifferentialSignalInputUnipolarGroup4Max_Type()
)
differentialSignalInputUnipolarGroup4Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup4Max.setStatus("current")
_DifferentialSignalInputUnipolarGroup4Min_Type = Integer32
_DifferentialSignalInputUnipolarGroup4Min_Object = MibScalar
differentialSignalInputUnipolarGroup4Min = _DifferentialSignalInputUnipolarGroup4Min_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 8, 4, 5),
    _DifferentialSignalInputUnipolarGroup4Min_Type()
)
differentialSignalInputUnipolarGroup4Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup4Min.setStatus("current")
_ContactClosureInput_ObjectIdentity = ObjectIdentity
contactClosureInput = _ContactClosureInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 9)
)
_ContactClosureInputGroup1_ObjectIdentity = ObjectIdentity
contactClosureInputGroup1 = _ContactClosureInputGroup1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 9, 1)
)


class _ContactClosureInputGroup1Caption_Type(OctetString):
    """Custom type contactClosureInputGroup1Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ContactClosureInputGroup1Caption_Type.__name__ = "OctetString"
_ContactClosureInputGroup1Caption_Object = MibScalar
contactClosureInputGroup1Caption = _ContactClosureInputGroup1Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 9, 1, 1),
    _ContactClosureInputGroup1Caption_Type()
)
contactClosureInputGroup1Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosureInputGroup1Caption.setStatus("current")
_ContactClosureInputGroup2_ObjectIdentity = ObjectIdentity
contactClosureInputGroup2 = _ContactClosureInputGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 9, 2)
)


class _ContactClosureInputGroup2Caption_Type(OctetString):
    """Custom type contactClosureInputGroup2Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ContactClosureInputGroup2Caption_Type.__name__ = "OctetString"
_ContactClosureInputGroup2Caption_Object = MibScalar
contactClosureInputGroup2Caption = _ContactClosureInputGroup2Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 9, 2, 1),
    _ContactClosureInputGroup2Caption_Type()
)
contactClosureInputGroup2Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosureInputGroup2Caption.setStatus("current")
_ContactClosureInputGroup3_ObjectIdentity = ObjectIdentity
contactClosureInputGroup3 = _ContactClosureInputGroup3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 9, 3)
)


class _ContactClosureInputGroup3Caption_Type(OctetString):
    """Custom type contactClosureInputGroup3Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ContactClosureInputGroup3Caption_Type.__name__ = "OctetString"
_ContactClosureInputGroup3Caption_Object = MibScalar
contactClosureInputGroup3Caption = _ContactClosureInputGroup3Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 9, 3, 1),
    _ContactClosureInputGroup3Caption_Type()
)
contactClosureInputGroup3Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosureInputGroup3Caption.setStatus("current")
_ContactClosureInputGroup4_ObjectIdentity = ObjectIdentity
contactClosureInputGroup4 = _ContactClosureInputGroup4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 9, 4)
)


class _ContactClosureInputGroup4Caption_Type(OctetString):
    """Custom type contactClosureInputGroup4Caption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ContactClosureInputGroup4Caption_Type.__name__ = "OctetString"
_ContactClosureInputGroup4Caption_Object = MibScalar
contactClosureInputGroup4Caption = _ContactClosureInputGroup4Caption_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 2, 9, 4, 1),
    _ContactClosureInputGroup4Caption_Type()
)
contactClosureInputGroup4Caption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosureInputGroup4Caption.setStatus("current")
_ProbeTraps_ObjectIdentity = ObjectIdentity
probeTraps = _ProbeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3)
)
_ProbeMgmt_ObjectIdentity = ObjectIdentity
probeMgmt = _ProbeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4)
)
_Mconfig_ObjectIdentity = ObjectIdentity
mconfig = _Mconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4, 1)
)
_MconfigTrapsReceiversNum_Type = Integer32
_MconfigTrapsReceiversNum_Object = MibScalar
mconfigTrapsReceiversNum = _MconfigTrapsReceiversNum_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4, 1, 1),
    _MconfigTrapsReceiversNum_Type()
)
mconfigTrapsReceiversNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mconfigTrapsReceiversNum.setStatus("current")
_MconfigTrapsReceiversTable_Object = MibTable
mconfigTrapsReceiversTable = _MconfigTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mconfigTrapsReceiversTable.setStatus("current")
_MconfigTrapsReceiversEntry_Object = MibTableRow
mconfigTrapsReceiversEntry = _MconfigTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4, 1, 2, 1)
)
mconfigTrapsReceiversEntry.setIndexNames(
    (0, "PROBE-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    mconfigTrapsReceiversEntry.setStatus("current")
_TrapsIndex_Type = Unsigned32
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4, 1, 2, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("current")
_TrapsReceiverAddr_Type = IpAddress
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4, 1, 2, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("current")
_ReceiverCommunityString_Type = DisplayString
_ReceiverCommunityString_Object = MibTableColumn
receiverCommunityString = _ReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4, 1, 2, 1, 3),
    _ReceiverCommunityString_Type()
)
receiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverCommunityString.setStatus("current")


class _SeverityLevel_Type(Integer32):
    """Custom type severityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("information", 1),
          ("warning", 2),
          ("severe", 3))
    )


_SeverityLevel_Type.__name__ = "Integer32"
_SeverityLevel_Object = MibTableColumn
severityLevel = _SeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4, 1, 2, 1, 4),
    _SeverityLevel_Type()
)
severityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityLevel.setStatus("current")


class _ReceiverAccept_Type(Integer32):
    """Custom type receiverAccept based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_ReceiverAccept_Type.__name__ = "Integer32"
_ReceiverAccept_Object = MibTableColumn
receiverAccept = _ReceiverAccept_Object(
    (1, 3, 6, 1, 4, 1, 13409, 1, 4, 1, 2, 1, 5),
    _ReceiverAccept_Type()
)
receiverAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverAccept.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13409, 1, 5)
)

# Managed Objects groups

probeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13409, 1, 5, 1)
)
probeStatusGroup.setObjects(
      *(("PROBE-MIB", "probeStatusTemperature"),
        ("PROBE-MIB", "probeStatusHumidity"),
        ("PROBE-MIB", "probeStatusItem1"),
        ("PROBE-MIB", "probeStatusItem2"),
        ("PROBE-MIB", "probeStatusItem3"),
        ("PROBE-MIB", "probeStatusItem4"),
        ("PROBE-MIB", "probeStatusItem5"),
        ("PROBE-MIB", "probeStatusItem6"),
        ("PROBE-MIB", "probeStatusItem7"),
        ("PROBE-MIB", "probeStatusItem8"))
)
if mibBuilder.loadTexts:
    probeStatusGroup.setStatus("current")

probeSettingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13409, 1, 5, 2)
)
probeSettingGroup.setObjects(
      *(("PROBE-MIB", "signalDetectionType"),
        ("PROBE-MIB", "temperatureMax"),
        ("PROBE-MIB", "temperatureMin"),
        ("PROBE-MIB", "humidityMax"),
        ("PROBE-MIB", "humidityMin"),
        ("PROBE-MIB", "analogInputGroup1Caption"),
        ("PROBE-MIB", "analogInputGroup1Factor"),
        ("PROBE-MIB", "analogInputGroup1Unit"),
        ("PROBE-MIB", "analogInputGroup1Max"),
        ("PROBE-MIB", "analogInputGroup1Min"),
        ("PROBE-MIB", "analogInputGroup2Caption"),
        ("PROBE-MIB", "analogInputGroup2Factor"),
        ("PROBE-MIB", "analogInputGroup2Unit"),
        ("PROBE-MIB", "analogInputGroup2Max"),
        ("PROBE-MIB", "analogInputGroup2Min"),
        ("PROBE-MIB", "analogInputGroup3Caption"),
        ("PROBE-MIB", "analogInputGroup3Factor"),
        ("PROBE-MIB", "analogInputGroup3Unit"),
        ("PROBE-MIB", "analogInputGroup3Max"),
        ("PROBE-MIB", "analogInputGroup3Min"),
        ("PROBE-MIB", "analogInputGroup4Caption"),
        ("PROBE-MIB", "analogInputGroup4Factor"),
        ("PROBE-MIB", "analogInputGroup4Unit"),
        ("PROBE-MIB", "analogInputGroup4Max"),
        ("PROBE-MIB", "analogInputGroup4Min"),
        ("PROBE-MIB", "analogInputGroup5Caption"),
        ("PROBE-MIB", "analogInputGroup5Factor"),
        ("PROBE-MIB", "analogInputGroup5Unit"),
        ("PROBE-MIB", "analogInputGroup5Max"),
        ("PROBE-MIB", "analogInputGroup5Min"),
        ("PROBE-MIB", "analogInputGroup6Caption"),
        ("PROBE-MIB", "analogInputGroup6Factor"),
        ("PROBE-MIB", "analogInputGroup6Unit"),
        ("PROBE-MIB", "analogInputGroup6Max"),
        ("PROBE-MIB", "analogInputGroup6Min"),
        ("PROBE-MIB", "analogInputGroup7Caption"),
        ("PROBE-MIB", "analogInputGroup7Factor"),
        ("PROBE-MIB", "analogInputGroup7Unit"),
        ("PROBE-MIB", "analogInputGroup7Max"),
        ("PROBE-MIB", "analogInputGroup7Min"),
        ("PROBE-MIB", "analogInputGroup8Caption"),
        ("PROBE-MIB", "analogInputGroup8Factor"),
        ("PROBE-MIB", "analogInputGroup8Unit"),
        ("PROBE-MIB", "analogInputGroup8Max"),
        ("PROBE-MIB", "analogInputGroup8Min"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup1Caption"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup1Factor"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup1Unit"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup1Max"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup1Min"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup2Caption"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup2Factor"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup2Unit"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup2Max"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup2Min"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup3Caption"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup3Factor"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup3Unit"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup3Max"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup3Min"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup4Caption"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup4Factor"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup4Unit"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup4Max"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup4Min"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup1Caption"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup1Factor"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup1Unit"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup1Max"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup1Min"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup2Caption"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup2Factor"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup2Unit"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup2Max"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup2Min"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup3Caption"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup3Factor"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup3Unit"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup3Max"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup3Min"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup4Caption"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup4Factor"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup4Unit"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup4Max"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup4Min"),
        ("PROBE-MIB", "contactClosureInputGroup1Caption"),
        ("PROBE-MIB", "contactClosureInputGroup2Caption"),
        ("PROBE-MIB", "contactClosureInputGroup3Caption"),
        ("PROBE-MIB", "contactClosureInputGroup4Caption"))
)
if mibBuilder.loadTexts:
    probeSettingGroup.setStatus("current")

mconfigTrapsReceiversGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13409, 1, 5, 4)
)
mconfigTrapsReceiversGroups.setObjects(
      *(("PROBE-MIB", "mconfigTrapsReceiversNum"),
        ("PROBE-MIB", "trapsIndex"),
        ("PROBE-MIB", "trapsReceiverAddr"),
        ("PROBE-MIB", "receiverCommunityString"),
        ("PROBE-MIB", "severityLevel"),
        ("PROBE-MIB", "receiverAccept"))
)
if mibBuilder.loadTexts:
    mconfigTrapsReceiversGroups.setStatus("current")


# Notification objects

probeTemperatureOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 1)
)
if mibBuilder.loadTexts:
    probeTemperatureOver.setStatus(
        "current"
    )

probeTemperatureDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 2)
)
if mibBuilder.loadTexts:
    probeTemperatureDown.setStatus(
        "current"
    )

probeTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 3)
)
if mibBuilder.loadTexts:
    probeTemperatureNormal.setStatus(
        "current"
    )

probeHumidityOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 4)
)
if mibBuilder.loadTexts:
    probeHumidityOver.setStatus(
        "current"
    )

probeHumidityDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 5)
)
if mibBuilder.loadTexts:
    probeHumidityDown.setStatus(
        "current"
    )

probeHumidityNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 6)
)
if mibBuilder.loadTexts:
    probeHumidityNormal.setStatus(
        "current"
    )

analogInputGroup1Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 7)
)
if mibBuilder.loadTexts:
    analogInputGroup1Over.setStatus(
        "current"
    )

analogInputGroup1Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 8)
)
if mibBuilder.loadTexts:
    analogInputGroup1Down.setStatus(
        "current"
    )

analogInputGroup1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 9)
)
if mibBuilder.loadTexts:
    analogInputGroup1Normal.setStatus(
        "current"
    )

analogInputGroup2Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 10)
)
if mibBuilder.loadTexts:
    analogInputGroup2Over.setStatus(
        "current"
    )

analogInputGroup2Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 11)
)
if mibBuilder.loadTexts:
    analogInputGroup2Down.setStatus(
        "current"
    )

analogInputGroup2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 12)
)
if mibBuilder.loadTexts:
    analogInputGroup2Normal.setStatus(
        "current"
    )

analogInputGroup3Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 13)
)
if mibBuilder.loadTexts:
    analogInputGroup3Over.setStatus(
        "current"
    )

analogInputGroup3Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 14)
)
if mibBuilder.loadTexts:
    analogInputGroup3Down.setStatus(
        "current"
    )

analogInputGroup3Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 15)
)
if mibBuilder.loadTexts:
    analogInputGroup3Normal.setStatus(
        "current"
    )

analogInputGroup4Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 16)
)
if mibBuilder.loadTexts:
    analogInputGroup4Over.setStatus(
        "current"
    )

analogInputGroup4Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 17)
)
if mibBuilder.loadTexts:
    analogInputGroup4Down.setStatus(
        "current"
    )

analogInputGroup4Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 18)
)
if mibBuilder.loadTexts:
    analogInputGroup4Normal.setStatus(
        "current"
    )

analogInputGroup5Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 19)
)
if mibBuilder.loadTexts:
    analogInputGroup5Over.setStatus(
        "current"
    )

analogInputGroup5Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 20)
)
if mibBuilder.loadTexts:
    analogInputGroup5Down.setStatus(
        "current"
    )

analogInputGroup5Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 21)
)
if mibBuilder.loadTexts:
    analogInputGroup5Normal.setStatus(
        "current"
    )

analogInputGroup6Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 22)
)
if mibBuilder.loadTexts:
    analogInputGroup6Over.setStatus(
        "current"
    )

analogInputGroup6Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 23)
)
if mibBuilder.loadTexts:
    analogInputGroup6Down.setStatus(
        "current"
    )

analogInputGroup6Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 24)
)
if mibBuilder.loadTexts:
    analogInputGroup6Normal.setStatus(
        "current"
    )

analogInputGroup7Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 25)
)
if mibBuilder.loadTexts:
    analogInputGroup7Over.setStatus(
        "current"
    )

analogInputGroup7Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 26)
)
if mibBuilder.loadTexts:
    analogInputGroup7Down.setStatus(
        "current"
    )

analogInputGroup7Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 27)
)
if mibBuilder.loadTexts:
    analogInputGroup7Normal.setStatus(
        "current"
    )

analogInputGroup8Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 28)
)
if mibBuilder.loadTexts:
    analogInputGroup8Over.setStatus(
        "current"
    )

analogInputGroup8Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 29)
)
if mibBuilder.loadTexts:
    analogInputGroup8Down.setStatus(
        "current"
    )

analogInputGroup8Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 30)
)
if mibBuilder.loadTexts:
    analogInputGroup8Normal.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup1Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 31)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup1Over.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup1Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 32)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup1Down.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 33)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup1Normal.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup2Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 34)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup2Over.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup2Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 35)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup2Down.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 36)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup2Normal.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup3Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 37)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup3Over.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup3Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 38)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup3Down.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup3Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 39)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup3Normal.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup4Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 40)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup4Over.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup4Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 41)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup4Down.setStatus(
        "current"
    )

differentialSignalInputBipolarGroup4Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 42)
)
if mibBuilder.loadTexts:
    differentialSignalInputBipolarGroup4Normal.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup1Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 43)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup1Over.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup1Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 44)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup1Down.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 45)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup1Normal.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup2Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 46)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup2Over.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup2Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 47)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup2Down.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 48)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup2Normal.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup3Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 49)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup3Over.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup3Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 50)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup3Down.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup3Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 51)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup3Normal.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup4Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 52)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup4Over.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup4Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 53)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup4Down.setStatus(
        "current"
    )

differentialSignalInputUnipolarGroup4Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 54)
)
if mibBuilder.loadTexts:
    differentialSignalInputUnipolarGroup4Normal.setStatus(
        "current"
    )

contactClosureInputGroup1Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 55)
)
if mibBuilder.loadTexts:
    contactClosureInputGroup1Open.setStatus(
        "current"
    )

contactClosureInputGroup1Close = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 56)
)
if mibBuilder.loadTexts:
    contactClosureInputGroup1Close.setStatus(
        "current"
    )

contactClosureInputGroup2Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 57)
)
if mibBuilder.loadTexts:
    contactClosureInputGroup2Open.setStatus(
        "current"
    )

contactClosureInputGroup2Close = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 58)
)
if mibBuilder.loadTexts:
    contactClosureInputGroup2Close.setStatus(
        "current"
    )

contactClosureInputGroup3Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 59)
)
if mibBuilder.loadTexts:
    contactClosureInputGroup3Open.setStatus(
        "current"
    )

contactClosureInputGroup3Close = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 60)
)
if mibBuilder.loadTexts:
    contactClosureInputGroup3Close.setStatus(
        "current"
    )

contactClosureInputGroup4Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 61)
)
if mibBuilder.loadTexts:
    contactClosureInputGroup4Open.setStatus(
        "current"
    )

contactClosureInputGroup4Close = NotificationType(
    (1, 3, 6, 1, 4, 1, 13409, 1, 3, 62)
)
if mibBuilder.loadTexts:
    contactClosureInputGroup4Close.setStatus(
        "current"
    )


# Notifications groups

probeTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13409, 1, 5, 3)
)
probeTrapsGroup.setObjects(
      *(("PROBE-MIB", "analogInputGroup1Over"),
        ("PROBE-MIB", "analogInputGroup1Down"),
        ("PROBE-MIB", "analogInputGroup1Normal"),
        ("PROBE-MIB", "analogInputGroup2Over"),
        ("PROBE-MIB", "analogInputGroup2Down"),
        ("PROBE-MIB", "analogInputGroup2Normal"),
        ("PROBE-MIB", "analogInputGroup3Over"),
        ("PROBE-MIB", "analogInputGroup3Down"),
        ("PROBE-MIB", "analogInputGroup3Normal"),
        ("PROBE-MIB", "analogInputGroup4Over"),
        ("PROBE-MIB", "analogInputGroup4Down"),
        ("PROBE-MIB", "analogInputGroup4Normal"),
        ("PROBE-MIB", "analogInputGroup5Over"),
        ("PROBE-MIB", "analogInputGroup5Down"),
        ("PROBE-MIB", "analogInputGroup5Normal"),
        ("PROBE-MIB", "analogInputGroup6Over"),
        ("PROBE-MIB", "analogInputGroup6Down"),
        ("PROBE-MIB", "analogInputGroup6Normal"),
        ("PROBE-MIB", "analogInputGroup7Over"),
        ("PROBE-MIB", "analogInputGroup7Down"),
        ("PROBE-MIB", "analogInputGroup7Normal"),
        ("PROBE-MIB", "analogInputGroup8Over"),
        ("PROBE-MIB", "analogInputGroup8Down"),
        ("PROBE-MIB", "analogInputGroup8Normal"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup1Over"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup1Down"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup1Normal"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup2Over"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup2Down"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup2Normal"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup3Over"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup3Down"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup3Normal"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup4Over"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup4Down"),
        ("PROBE-MIB", "differentialSignalInputBipolarGroup4Normal"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup1Over"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup1Down"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup1Normal"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup2Over"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup2Down"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup2Normal"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup3Over"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup3Down"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup3Normal"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup4Over"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup4Down"),
        ("PROBE-MIB", "differentialSignalInputUnipolarGroup4Normal"),
        ("PROBE-MIB", "contactClosureInputGroup1Open"),
        ("PROBE-MIB", "contactClosureInputGroup1Close"),
        ("PROBE-MIB", "contactClosureInputGroup2Open"),
        ("PROBE-MIB", "contactClosureInputGroup2Close"),
        ("PROBE-MIB", "contactClosureInputGroup3Open"),
        ("PROBE-MIB", "contactClosureInputGroup3Close"),
        ("PROBE-MIB", "contactClosureInputGroup4Open"),
        ("PROBE-MIB", "contactClosureInputGroup4Close"),
        ("PROBE-MIB", "probeTemperatureOver"),
        ("PROBE-MIB", "probeTemperatureDown"),
        ("PROBE-MIB", "probeTemperatureNormal"),
        ("PROBE-MIB", "probeHumidityOver"),
        ("PROBE-MIB", "probeHumidityDown"),
        ("PROBE-MIB", "probeHumidityNormal"))
)
if mibBuilder.loadTexts:
    probeTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROBE-MIB",
    **{"mega": mega,
       "probe": probe,
       "probeStatus": probeStatus,
       "probeStatusTemperature": probeStatusTemperature,
       "probeStatusHumidity": probeStatusHumidity,
       "probeStatusItem1": probeStatusItem1,
       "probeStatusItem2": probeStatusItem2,
       "probeStatusItem3": probeStatusItem3,
       "probeStatusItem4": probeStatusItem4,
       "probeStatusItem5": probeStatusItem5,
       "probeStatusItem6": probeStatusItem6,
       "probeStatusItem7": probeStatusItem7,
       "probeStatusItem8": probeStatusItem8,
       "probeSetting": probeSetting,
       "signalDetectionType": signalDetectionType,
       "temperatureMax": temperatureMax,
       "temperatureMin": temperatureMin,
       "humidityMax": humidityMax,
       "humidityMin": humidityMin,
       "analogInput": analogInput,
       "analogInputGroup1": analogInputGroup1,
       "analogInputGroup1Caption": analogInputGroup1Caption,
       "analogInputGroup1Factor": analogInputGroup1Factor,
       "analogInputGroup1Unit": analogInputGroup1Unit,
       "analogInputGroup1Max": analogInputGroup1Max,
       "analogInputGroup1Min": analogInputGroup1Min,
       "analogInputGroup2": analogInputGroup2,
       "analogInputGroup2Caption": analogInputGroup2Caption,
       "analogInputGroup2Factor": analogInputGroup2Factor,
       "analogInputGroup2Unit": analogInputGroup2Unit,
       "analogInputGroup2Max": analogInputGroup2Max,
       "analogInputGroup2Min": analogInputGroup2Min,
       "analogInputGroup3": analogInputGroup3,
       "analogInputGroup3Caption": analogInputGroup3Caption,
       "analogInputGroup3Factor": analogInputGroup3Factor,
       "analogInputGroup3Unit": analogInputGroup3Unit,
       "analogInputGroup3Max": analogInputGroup3Max,
       "analogInputGroup3Min": analogInputGroup3Min,
       "analogInputGroup4": analogInputGroup4,
       "analogInputGroup4Caption": analogInputGroup4Caption,
       "analogInputGroup4Factor": analogInputGroup4Factor,
       "analogInputGroup4Unit": analogInputGroup4Unit,
       "analogInputGroup4Max": analogInputGroup4Max,
       "analogInputGroup4Min": analogInputGroup4Min,
       "analogInputGroup5": analogInputGroup5,
       "analogInputGroup5Caption": analogInputGroup5Caption,
       "analogInputGroup5Factor": analogInputGroup5Factor,
       "analogInputGroup5Unit": analogInputGroup5Unit,
       "analogInputGroup5Max": analogInputGroup5Max,
       "analogInputGroup5Min": analogInputGroup5Min,
       "analogInputGroup6": analogInputGroup6,
       "analogInputGroup6Caption": analogInputGroup6Caption,
       "analogInputGroup6Factor": analogInputGroup6Factor,
       "analogInputGroup6Unit": analogInputGroup6Unit,
       "analogInputGroup6Max": analogInputGroup6Max,
       "analogInputGroup6Min": analogInputGroup6Min,
       "analogInputGroup7": analogInputGroup7,
       "analogInputGroup7Caption": analogInputGroup7Caption,
       "analogInputGroup7Factor": analogInputGroup7Factor,
       "analogInputGroup7Unit": analogInputGroup7Unit,
       "analogInputGroup7Max": analogInputGroup7Max,
       "analogInputGroup7Min": analogInputGroup7Min,
       "analogInputGroup8": analogInputGroup8,
       "analogInputGroup8Caption": analogInputGroup8Caption,
       "analogInputGroup8Factor": analogInputGroup8Factor,
       "analogInputGroup8Unit": analogInputGroup8Unit,
       "analogInputGroup8Max": analogInputGroup8Max,
       "analogInputGroup8Min": analogInputGroup8Min,
       "differentialSignalInputBipolar": differentialSignalInputBipolar,
       "differentialSignalInputBipolarGroup1": differentialSignalInputBipolarGroup1,
       "differentialSignalInputBipolarGroup1Caption": differentialSignalInputBipolarGroup1Caption,
       "differentialSignalInputBipolarGroup1Factor": differentialSignalInputBipolarGroup1Factor,
       "differentialSignalInputBipolarGroup1Unit": differentialSignalInputBipolarGroup1Unit,
       "differentialSignalInputBipolarGroup1Max": differentialSignalInputBipolarGroup1Max,
       "differentialSignalInputBipolarGroup1Min": differentialSignalInputBipolarGroup1Min,
       "differentialSignalInputBipolarGroup2": differentialSignalInputBipolarGroup2,
       "differentialSignalInputBipolarGroup2Caption": differentialSignalInputBipolarGroup2Caption,
       "differentialSignalInputBipolarGroup2Factor": differentialSignalInputBipolarGroup2Factor,
       "differentialSignalInputBipolarGroup2Unit": differentialSignalInputBipolarGroup2Unit,
       "differentialSignalInputBipolarGroup2Max": differentialSignalInputBipolarGroup2Max,
       "differentialSignalInputBipolarGroup2Min": differentialSignalInputBipolarGroup2Min,
       "differentialSignalInputBipolarGroup3": differentialSignalInputBipolarGroup3,
       "differentialSignalInputBipolarGroup3Caption": differentialSignalInputBipolarGroup3Caption,
       "differentialSignalInputBipolarGroup3Factor": differentialSignalInputBipolarGroup3Factor,
       "differentialSignalInputBipolarGroup3Unit": differentialSignalInputBipolarGroup3Unit,
       "differentialSignalInputBipolarGroup3Max": differentialSignalInputBipolarGroup3Max,
       "differentialSignalInputBipolarGroup3Min": differentialSignalInputBipolarGroup3Min,
       "differentialSignalInputBipolarGroup4": differentialSignalInputBipolarGroup4,
       "differentialSignalInputBipolarGroup4Caption": differentialSignalInputBipolarGroup4Caption,
       "differentialSignalInputBipolarGroup4Factor": differentialSignalInputBipolarGroup4Factor,
       "differentialSignalInputBipolarGroup4Unit": differentialSignalInputBipolarGroup4Unit,
       "differentialSignalInputBipolarGroup4Max": differentialSignalInputBipolarGroup4Max,
       "differentialSignalInputBipolarGroup4Min": differentialSignalInputBipolarGroup4Min,
       "differentialSignalInputUnipolar": differentialSignalInputUnipolar,
       "differentialSignalInputUnipolarGroup1": differentialSignalInputUnipolarGroup1,
       "differentialSignalInputUnipolarGroup1Caption": differentialSignalInputUnipolarGroup1Caption,
       "differentialSignalInputUnipolarGroup1Factor": differentialSignalInputUnipolarGroup1Factor,
       "differentialSignalInputUnipolarGroup1Unit": differentialSignalInputUnipolarGroup1Unit,
       "differentialSignalInputUnipolarGroup1Max": differentialSignalInputUnipolarGroup1Max,
       "differentialSignalInputUnipolarGroup1Min": differentialSignalInputUnipolarGroup1Min,
       "differentialSignalInputUnipolarGroup2": differentialSignalInputUnipolarGroup2,
       "differentialSignalInputUnipolarGroup2Caption": differentialSignalInputUnipolarGroup2Caption,
       "differentialSignalInputUnipolarGroup2Factor": differentialSignalInputUnipolarGroup2Factor,
       "differentialSignalInputUnipolarGroup2Unit": differentialSignalInputUnipolarGroup2Unit,
       "differentialSignalInputUnipolarGroup2Max": differentialSignalInputUnipolarGroup2Max,
       "differentialSignalInputUnipolarGroup2Min": differentialSignalInputUnipolarGroup2Min,
       "differentialSignalInputUnipolarGroup3": differentialSignalInputUnipolarGroup3,
       "differentialSignalInputUnipolarGroup3Caption": differentialSignalInputUnipolarGroup3Caption,
       "differentialSignalInputUnipolarGroup3Factor": differentialSignalInputUnipolarGroup3Factor,
       "differentialSignalInputUnipolarGroup3Unit": differentialSignalInputUnipolarGroup3Unit,
       "differentialSignalInputUnipolarGroup3Max": differentialSignalInputUnipolarGroup3Max,
       "differentialSignalInputUnipolarGroup3Min": differentialSignalInputUnipolarGroup3Min,
       "differentialSignalInputUnipolarGroup4": differentialSignalInputUnipolarGroup4,
       "differentialSignalInputUnipolarGroup4Caption": differentialSignalInputUnipolarGroup4Caption,
       "differentialSignalInputUnipolarGroup4Factor": differentialSignalInputUnipolarGroup4Factor,
       "differentialSignalInputUnipolarGroup4Unit": differentialSignalInputUnipolarGroup4Unit,
       "differentialSignalInputUnipolarGroup4Max": differentialSignalInputUnipolarGroup4Max,
       "differentialSignalInputUnipolarGroup4Min": differentialSignalInputUnipolarGroup4Min,
       "contactClosureInput": contactClosureInput,
       "contactClosureInputGroup1": contactClosureInputGroup1,
       "contactClosureInputGroup1Caption": contactClosureInputGroup1Caption,
       "contactClosureInputGroup2": contactClosureInputGroup2,
       "contactClosureInputGroup2Caption": contactClosureInputGroup2Caption,
       "contactClosureInputGroup3": contactClosureInputGroup3,
       "contactClosureInputGroup3Caption": contactClosureInputGroup3Caption,
       "contactClosureInputGroup4": contactClosureInputGroup4,
       "contactClosureInputGroup4Caption": contactClosureInputGroup4Caption,
       "probeTraps": probeTraps,
       "probeTemperatureOver": probeTemperatureOver,
       "probeTemperatureDown": probeTemperatureDown,
       "probeTemperatureNormal": probeTemperatureNormal,
       "probeHumidityOver": probeHumidityOver,
       "probeHumidityDown": probeHumidityDown,
       "probeHumidityNormal": probeHumidityNormal,
       "analogInputGroup1Over": analogInputGroup1Over,
       "analogInputGroup1Down": analogInputGroup1Down,
       "analogInputGroup1Normal": analogInputGroup1Normal,
       "analogInputGroup2Over": analogInputGroup2Over,
       "analogInputGroup2Down": analogInputGroup2Down,
       "analogInputGroup2Normal": analogInputGroup2Normal,
       "analogInputGroup3Over": analogInputGroup3Over,
       "analogInputGroup3Down": analogInputGroup3Down,
       "analogInputGroup3Normal": analogInputGroup3Normal,
       "analogInputGroup4Over": analogInputGroup4Over,
       "analogInputGroup4Down": analogInputGroup4Down,
       "analogInputGroup4Normal": analogInputGroup4Normal,
       "analogInputGroup5Over": analogInputGroup5Over,
       "analogInputGroup5Down": analogInputGroup5Down,
       "analogInputGroup5Normal": analogInputGroup5Normal,
       "analogInputGroup6Over": analogInputGroup6Over,
       "analogInputGroup6Down": analogInputGroup6Down,
       "analogInputGroup6Normal": analogInputGroup6Normal,
       "analogInputGroup7Over": analogInputGroup7Over,
       "analogInputGroup7Down": analogInputGroup7Down,
       "analogInputGroup7Normal": analogInputGroup7Normal,
       "analogInputGroup8Over": analogInputGroup8Over,
       "analogInputGroup8Down": analogInputGroup8Down,
       "analogInputGroup8Normal": analogInputGroup8Normal,
       "differentialSignalInputBipolarGroup1Over": differentialSignalInputBipolarGroup1Over,
       "differentialSignalInputBipolarGroup1Down": differentialSignalInputBipolarGroup1Down,
       "differentialSignalInputBipolarGroup1Normal": differentialSignalInputBipolarGroup1Normal,
       "differentialSignalInputBipolarGroup2Over": differentialSignalInputBipolarGroup2Over,
       "differentialSignalInputBipolarGroup2Down": differentialSignalInputBipolarGroup2Down,
       "differentialSignalInputBipolarGroup2Normal": differentialSignalInputBipolarGroup2Normal,
       "differentialSignalInputBipolarGroup3Over": differentialSignalInputBipolarGroup3Over,
       "differentialSignalInputBipolarGroup3Down": differentialSignalInputBipolarGroup3Down,
       "differentialSignalInputBipolarGroup3Normal": differentialSignalInputBipolarGroup3Normal,
       "differentialSignalInputBipolarGroup4Over": differentialSignalInputBipolarGroup4Over,
       "differentialSignalInputBipolarGroup4Down": differentialSignalInputBipolarGroup4Down,
       "differentialSignalInputBipolarGroup4Normal": differentialSignalInputBipolarGroup4Normal,
       "differentialSignalInputUnipolarGroup1Over": differentialSignalInputUnipolarGroup1Over,
       "differentialSignalInputUnipolarGroup1Down": differentialSignalInputUnipolarGroup1Down,
       "differentialSignalInputUnipolarGroup1Normal": differentialSignalInputUnipolarGroup1Normal,
       "differentialSignalInputUnipolarGroup2Over": differentialSignalInputUnipolarGroup2Over,
       "differentialSignalInputUnipolarGroup2Down": differentialSignalInputUnipolarGroup2Down,
       "differentialSignalInputUnipolarGroup2Normal": differentialSignalInputUnipolarGroup2Normal,
       "differentialSignalInputUnipolarGroup3Over": differentialSignalInputUnipolarGroup3Over,
       "differentialSignalInputUnipolarGroup3Down": differentialSignalInputUnipolarGroup3Down,
       "differentialSignalInputUnipolarGroup3Normal": differentialSignalInputUnipolarGroup3Normal,
       "differentialSignalInputUnipolarGroup4Over": differentialSignalInputUnipolarGroup4Over,
       "differentialSignalInputUnipolarGroup4Down": differentialSignalInputUnipolarGroup4Down,
       "differentialSignalInputUnipolarGroup4Normal": differentialSignalInputUnipolarGroup4Normal,
       "contactClosureInputGroup1Open": contactClosureInputGroup1Open,
       "contactClosureInputGroup1Close": contactClosureInputGroup1Close,
       "contactClosureInputGroup2Open": contactClosureInputGroup2Open,
       "contactClosureInputGroup2Close": contactClosureInputGroup2Close,
       "contactClosureInputGroup3Open": contactClosureInputGroup3Open,
       "contactClosureInputGroup3Close": contactClosureInputGroup3Close,
       "contactClosureInputGroup4Open": contactClosureInputGroup4Open,
       "contactClosureInputGroup4Close": contactClosureInputGroup4Close,
       "probeMgmt": probeMgmt,
       "mconfig": mconfig,
       "mconfigTrapsReceiversNum": mconfigTrapsReceiversNum,
       "mconfigTrapsReceiversTable": mconfigTrapsReceiversTable,
       "mconfigTrapsReceiversEntry": mconfigTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "severityLevel": severityLevel,
       "receiverAccept": receiverAccept,
       "conformance": conformance,
       "probeStatusGroup": probeStatusGroup,
       "probeSettingGroup": probeSettingGroup,
       "probeTrapsGroup": probeTrapsGroup,
       "mconfigTrapsReceiversGroups": mconfigTrapsReceiversGroups}
)
