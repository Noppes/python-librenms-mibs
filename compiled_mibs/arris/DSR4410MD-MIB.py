# SNMP MIB module (DSR4410MD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\DSR4410MD-MIB

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

dsr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621)
)
if mibBuilder.loadTexts:
    dsr.setRevisions(
        ("2014-04-23 10:00",
         "2011-08-10 10:00",
         "2011-02-04 10:00",
         "2011-02-02 10:00",
         "2011-01-07 10:00",
         "2010-12-09 10:00",
         "2010-12-08 10:00",
         "2010-11-29 10:00",
         "2010-06-22 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_GiMIB_ObjectIdentity = ObjectIdentity
giMIB = _GiMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166)
)
_Giproducts_ObjectIdentity = ObjectIdentity
giproducts = _Giproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1)
)
_VideoMib_ObjectIdentity = ObjectIdentity
videoMib = _VideoMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 1)
)


class _VideoOutput525Lines_Type(Integer32):
    """Custom type videoOutput525Lines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ntsc", 0),
          ("palm", 1))
    )


_VideoOutput525Lines_Type.__name__ = "Integer32"
_VideoOutput525Lines_Object = MibScalar
videoOutput525Lines = _VideoOutput525Lines_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 1, 1),
    _VideoOutput525Lines_Type()
)
videoOutput525Lines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoOutput525Lines.setStatus("current")


class _VideoOutput625Lines_Type(Integer32):
    """Custom type videoOutput625Lines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pal-d-g-b", 0),
          ("pali", 1),
          ("paln", 2))
    )


_VideoOutput625Lines_Type.__name__ = "Integer32"
_VideoOutput625Lines_Object = MibScalar
videoOutput625Lines = _VideoOutput625Lines_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 1, 2),
    _VideoOutput625Lines_Type()
)
videoOutput625Lines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoOutput625Lines.setStatus("current")


class _AspectRatioInput_Type(Integer32):
    """Custom type aspectRatioInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ar4x3", 0),
          ("ar16x9", 1),
          ("unknown", 2))
    )


_AspectRatioInput_Type.__name__ = "Integer32"
_AspectRatioInput_Object = MibScalar
aspectRatioInput = _AspectRatioInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 1, 3),
    _AspectRatioInput_Type()
)
aspectRatioInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspectRatioInput.setStatus("current")


class _AspectRatioOutput_Type(Integer32):
    """Custom type aspectRatioOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ar4x3-Zoom", 0),
          ("ar4x3-PanScan", 1),
          ("ar4x3-LetterBox", 2))
    )


_AspectRatioOutput_Type.__name__ = "Integer32"
_AspectRatioOutput_Object = MibScalar
aspectRatioOutput = _AspectRatioOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 1, 4),
    _AspectRatioOutput_Type()
)
aspectRatioOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aspectRatioOutput.setStatus("current")
_RfPortsMib_ObjectIdentity = ObjectIdentity
rfPortsMib = _RfPortsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2)
)
_RfPortsSetup_ObjectIdentity = ObjectIdentity
rfPortsSetup = _RfPortsSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 1)
)
_Port1_ObjectIdentity = ObjectIdentity
port1 = _Port1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 1, 1)
)


class _Port1SetupMode_Type(Integer32):
    """Custom type port1SetupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("auto", 1))
    )


_Port1SetupMode_Type.__name__ = "Integer32"
_Port1SetupMode_Object = MibScalar
port1SetupMode = _Port1SetupMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 1, 1, 1),
    _Port1SetupMode_Type()
)
port1SetupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1SetupMode.setStatus("current")


class _Port1Satellite_Type(OctetString):
    """Custom type port1Satellite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_Port1Satellite_Type.__name__ = "OctetString"
_Port1Satellite_Object = MibScalar
port1Satellite = _Port1Satellite_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 1, 1, 2),
    _Port1Satellite_Type()
)
port1Satellite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Satellite.setStatus("current")


class _Port1Polarity_Type(Integer32):
    """Custom type port1Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 0),
          ("vertical", 1),
          ("notDefined", 2))
    )


_Port1Polarity_Type.__name__ = "Integer32"
_Port1Polarity_Object = MibScalar
port1Polarity = _Port1Polarity_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 1, 1, 3),
    _Port1Polarity_Type()
)
port1Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Polarity.setStatus("current")
_Port2_ObjectIdentity = ObjectIdentity
port2 = _Port2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 1, 2)
)


class _Port2SetupMode_Type(Integer32):
    """Custom type port2SetupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("auto", 1))
    )


_Port2SetupMode_Type.__name__ = "Integer32"
_Port2SetupMode_Object = MibScalar
port2SetupMode = _Port2SetupMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 1, 2, 1),
    _Port2SetupMode_Type()
)
port2SetupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2SetupMode.setStatus("current")


class _Port2Satellite_Type(OctetString):
    """Custom type port2Satellite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_Port2Satellite_Type.__name__ = "OctetString"
_Port2Satellite_Object = MibScalar
port2Satellite = _Port2Satellite_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 1, 2, 2),
    _Port2Satellite_Type()
)
port2Satellite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Satellite.setStatus("current")


class _Port2Polarity_Type(Integer32):
    """Custom type port2Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 0),
          ("vertical", 1),
          ("notDefined", 2))
    )


_Port2Polarity_Type.__name__ = "Integer32"
_Port2Polarity_Object = MibScalar
port2Polarity = _Port2Polarity_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 1, 2, 3),
    _Port2Polarity_Type()
)
port2Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Polarity.setStatus("current")
_ManualTune_ObjectIdentity = ObjectIdentity
manualTune = _ManualTune_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2)
)


class _ActivePort_Type(Integer32):
    """Custom type activePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              8)
        )
    )
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("asiInput", 8))
    )


_ActivePort_Type.__name__ = "Integer32"
_ActivePort_Object = MibScalar
activePort = _ActivePort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 1),
    _ActivePort_Type()
)
activePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activePort.setStatus("current")


class _Mode_Type(Integer32):
    """Custom type mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("xpndr", 0),
          ("lfreq", 1))
    )


_Mode_Type.__name__ = "Integer32"
_Mode_Object = MibScalar
mode = _Mode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 2),
    _Mode_Type()
)
mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mode.setStatus("current")


class _TransponderNumber_Type(Integer32):
    """Custom type transponderNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_TransponderNumber_Type.__name__ = "Integer32"
_TransponderNumber_Object = MibScalar
transponderNumber = _TransponderNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 3),
    _TransponderNumber_Type()
)
transponderNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transponderNumber.setStatus("current")


class _Frequency_Type(Integer32):
    """Custom type frequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(950, 2150),
    )


_Frequency_Type.__name__ = "Integer32"
_Frequency_Object = MibScalar
frequency = _Frequency_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 4),
    _Frequency_Type()
)
frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frequency.setStatus("current")


class _DvbSymbolRate_Type(Integer32):
    """Custom type dvbSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_DvbSymbolRate_Type.__name__ = "Integer32"
_DvbSymbolRate_Object = MibScalar
dvbSymbolRate = _DvbSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 5),
    _DvbSymbolRate_Type()
)
dvbSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSymbolRate.setStatus("current")


class _DvbCodeRate_Type(Integer32):
    """Custom type dvbCodeRate based on Integer32"""
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
        *(("cr1-2", 0),
          ("cr2-3", 1),
          ("cr3-4", 2),
          ("cr5-6", 3),
          ("cr7-8", 4))
    )


_DvbCodeRate_Type.__name__ = "Integer32"
_DvbCodeRate_Object = MibScalar
dvbCodeRate = _DvbCodeRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 6),
    _DvbCodeRate_Type()
)
dvbCodeRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbCodeRate.setStatus("current")


class _SymbolCodeBit_Type(Integer32):
    """Custom type symbolCodeBit based on Integer32"""
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
              73)
        )
    )
    namedValues = NamedValues(
        *(("sr29Cm5-11Combined", 0),
          ("sr29Cm1-2Combined", 1),
          ("sr29Cm3-5Combined", 2),
          ("sr29Cm2-3Combined", 3),
          ("sr29Cm3-4Combined", 4),
          ("sr29Cm4-5Combined", 5),
          ("sr29Cm5-6Combined", 6),
          ("sr29Cm7-8Combined", 7),
          ("sr29Cm5-11Split", 8),
          ("sr29Cm1-2Split", 9),
          ("sr29Cm3-5Split", 10),
          ("sr29Cm2-3Split", 11),
          ("sr29Cm3-4Split", 12),
          ("sr29Cm4-5Split", 13),
          ("sr29Cm5-6Split", 14),
          ("sr29Cm7-8Split", 15),
          ("sr19Cm5-11Combined", 16),
          ("sr19Cm1-2Combined", 17),
          ("sr19Cm3-5Combined", 18),
          ("sr19Cm2-3Combined", 19),
          ("sr19Cm3-4Combined", 20),
          ("sr19Cm4-5Combined", 21),
          ("sr19Cm5-6Combined", 22),
          ("sr19Cm7-8Combined", 23),
          ("sr19Cm5-11Split", 24),
          ("sr19Cm1-2Split", 25),
          ("sr19Cm3-5Split", 26),
          ("sr19Cm2-3Split", 27),
          ("sr19Cm3-4Split", 28),
          ("sr19Cm4-5Split", 29),
          ("sr19Cm5-6Split", 30),
          ("sr19Cm7-8Split", 31),
          ("sr14Cm1-2Combined", 32),
          ("sr14Cm3-5Combined", 33),
          ("sr14Cm2-3Combined", 34),
          ("sr14Cm3-4Combined", 35),
          ("sr14Cm4-5Combined", 36),
          ("sr14Cm5-6Combined", 37),
          ("sr14Cm7-8Combined", 38),
          ("sr11Cm1-2Combined", 39),
          ("sr11Cm3-5Combined", 40),
          ("sr11Cm2-3Combined", 41),
          ("sr11Cm3-4Combined", 42),
          ("sr11Cm4-5Combined", 43),
          ("sr11Cm5-6Combined", 44),
          ("sr11Cm7-8Combined", 45),
          ("sr9Cm1-2Combined", 46),
          ("sr9Cm3-5Combined", 47),
          ("sr9Cm2-3Combined", 48),
          ("sr9Cm3-4Combined", 49),
          ("sr9Cm4-5Combined", 50),
          ("sr9Cm5-6Combined", 51),
          ("sr9Cm7-8Combined", 52),
          ("sr7Cm1-2Combined", 53),
          ("sr7Cm3-5Combined", 54),
          ("sr7Cm2-3Combined", 55),
          ("sr7Cm3-4Combined", 56),
          ("sr7Cm4-5Combined", 57),
          ("sr7Cm5-6Combined", 58),
          ("sr7Cm7-8Combined", 59),
          ("sr4Cm1-2Combined", 60),
          ("sr4Cm3-5Combined", 61),
          ("sr4Cm2-3Combined", 62),
          ("sr4Cm3-4Combined", 63),
          ("sr4Cm4-5Combined", 64),
          ("sr4Cm5-6Combined", 65),
          ("sr4Cm7-8Combined", 66),
          ("sr3Cm1-2Combined", 67),
          ("sr3Cm3-5Combined", 68),
          ("sr3Cm2-3Combined", 69),
          ("sr3Cm3-4Combined", 70),
          ("sr3Cm4-5Combined", 71),
          ("sr3Cm5-6Combined", 72),
          ("sr3Cm7-8Combined", 73))
    )


_SymbolCodeBit_Type.__name__ = "Integer32"
_SymbolCodeBit_Object = MibScalar
symbolCodeBit = _SymbolCodeBit_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 8),
    _SymbolCodeBit_Type()
)
symbolCodeBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    symbolCodeBit.setStatus("current")


class _ModulationMode_Type(Integer32):
    """Custom type modulationMode based on Integer32"""
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
        *(("dciiManual", 0),
          ("dvbManual", 1),
          ("dciiAuto", 2),
          ("manual8pskTC", 3),
          ("manual8pskDvbS2", 4))
    )


_ModulationMode_Type.__name__ = "Integer32"
_ModulationMode_Object = MibScalar
modulationMode = _ModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 9),
    _ModulationMode_Type()
)
modulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulationMode.setStatus("current")


class _Psk8SymbolRate_Type(Integer32):
    """Custom type psk8SymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 30000000),
    )


_Psk8SymbolRate_Type.__name__ = "Integer32"
_Psk8SymbolRate_Object = MibScalar
psk8SymbolRate = _Psk8SymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 10),
    _Psk8SymbolRate_Type()
)
psk8SymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psk8SymbolRate.setStatus("current")


class _Psk8CodeRate_Type(Integer32):
    """Custom type psk8CodeRate based on Integer32"""
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
        *(("cr2-3-192", 0),
          ("cr3-4-205", 1),
          ("cr3-4-211", 2),
          ("cr3-4-219", 3),
          ("cr5-6-230", 4),
          ("cr8-9-240", 5))
    )


_Psk8CodeRate_Type.__name__ = "Integer32"
_Psk8CodeRate_Object = MibScalar
psk8CodeRate = _Psk8CodeRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 11),
    _Psk8CodeRate_Type()
)
psk8CodeRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psk8CodeRate.setStatus("current")


class _DvbS2symbolRate_Type(Integer32):
    """Custom type dvbS2symbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 33000000),
    )


_DvbS2symbolRate_Type.__name__ = "Integer32"
_DvbS2symbolRate_Object = MibScalar
dvbS2symbolRate = _DvbS2symbolRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 12),
    _DvbS2symbolRate_Type()
)
dvbS2symbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbS2symbolRate.setStatus("current")


class _DvbS2codeRate_Type(Integer32):
    """Custom type dvbS2codeRate based on Integer32"""
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
        *(("cr3-5", 0),
          ("cr2-3", 1),
          ("cr3-4", 2),
          ("cr5-6", 3),
          ("cr8-9", 4),
          ("cr9-10", 5))
    )


_DvbS2codeRate_Type.__name__ = "Integer32"
_DvbS2codeRate_Object = MibScalar
dvbS2codeRate = _DvbS2codeRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 2, 2, 13),
    _DvbS2codeRate_Type()
)
dvbS2codeRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbS2codeRate.setStatus("current")
_ChannelMib_ObjectIdentity = ObjectIdentity
channelMib = _ChannelMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 3)
)
_ChannelSelect_ObjectIdentity = ObjectIdentity
channelSelect = _ChannelSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 3, 1)
)


class _VctID_Type(Integer32):
    """Custom type vctID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VctID_Type.__name__ = "Integer32"
_VctID_Object = MibScalar
vctID = _VctID_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 3, 1, 1),
    _VctID_Type()
)
vctID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctID.setStatus("current")


class _ChannelNumber_Type(Integer32):
    """Custom type channelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ChannelNumber_Type.__name__ = "Integer32"
_ChannelNumber_Object = MibScalar
channelNumber = _ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 3, 1, 2),
    _ChannelNumber_Type()
)
channelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelNumber.setStatus("current")
_ChannelStatus_ObjectIdentity = ObjectIdentity
channelStatus = _ChannelStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 3, 2)
)


class _Transponder_Type(OctetString):
    """Custom type transponder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Transponder_Type.__name__ = "OctetString"
_Transponder_Object = MibScalar
transponder = _Transponder_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 3, 2, 1),
    _Transponder_Type()
)
transponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transponder.setStatus("current")


class _Source_Type(OctetString):
    """Custom type source based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Source_Type.__name__ = "OctetString"
_Source_Object = MibScalar
source = _Source_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 3, 2, 2),
    _Source_Type()
)
source.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    source.setStatus("current")


class _SatelliteStatus_Type(OctetString):
    """Custom type satelliteStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SatelliteStatus_Type.__name__ = "OctetString"
_SatelliteStatus_Object = MibScalar
satelliteStatus = _SatelliteStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 3, 2, 3),
    _SatelliteStatus_Type()
)
satelliteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteStatus.setStatus("current")
_ServiceSelectionMib_ObjectIdentity = ObjectIdentity
serviceSelectionMib = _ServiceSelectionMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 4)
)


class _MpegServiceNumber_Type(Integer32):
    """Custom type mpegServiceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpegServiceNumber_Type.__name__ = "Integer32"
_MpegServiceNumber_Object = MibScalar
mpegServiceNumber = _MpegServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 4, 1),
    _MpegServiceNumber_Type()
)
mpegServiceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpegServiceNumber.setStatus("current")
_UnitControlMib_ObjectIdentity = ObjectIdentity
unitControlMib = _UnitControlMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 5)
)
_UnitControl_ObjectIdentity = ObjectIdentity
unitControl = _UnitControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 5, 1)
)


class _Contrast_Type(Integer32):
    """Custom type contrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Contrast_Type.__name__ = "Integer32"
_Contrast_Object = MibScalar
contrast = _Contrast_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 5, 1, 1),
    _Contrast_Type()
)
contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contrast.setStatus("current")


class _AsiEnable_Type(Integer32):
    """Custom type asiEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1),
          ("lock-off", 2))
    )


_AsiEnable_Type.__name__ = "Integer32"
_AsiEnable_Object = MibScalar
asiEnable = _AsiEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 5, 1, 3),
    _AsiEnable_Type()
)
asiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asiEnable.setStatus("current")


class _LnbPower_Type(Integer32):
    """Custom type lnbPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_LnbPower_Type.__name__ = "Integer32"
_LnbPower_Object = MibScalar
lnbPower = _LnbPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 5, 1, 6),
    _LnbPower_Type()
)
lnbPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnbPower.setStatus("current")


class _ResetIRD_Type(Integer32):
    """Custom type resetIRD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("powercycle", 1))
    )


_ResetIRD_Type.__name__ = "Integer32"
_ResetIRD_Object = MibScalar
resetIRD = _ResetIRD_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 5, 1, 7),
    _ResetIRD_Type()
)
resetIRD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetIRD.setStatus("current")


class _FormatRate_Type(Integer32):
    """Custom type formatRate based on Integer32"""
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
        *(("byte54", 0),
          ("packet54", 1),
          ("packet81", 2),
          ("packet160", 3),
          ("byte27", 4),
          ("packet27", 5))
    )


_FormatRate_Type.__name__ = "Integer32"
_FormatRate_Object = MibScalar
formatRate = _FormatRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 5, 1, 8),
    _FormatRate_Type()
)
formatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    formatRate.setStatus("current")
_AudioMib_ObjectIdentity = ObjectIdentity
audioMib = _AudioMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6)
)
_AudioConfig_ObjectIdentity = ObjectIdentity
audioConfig = _AudioConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1)
)
_Audio1Config_ObjectIdentity = ObjectIdentity
audio1Config = _Audio1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 1)
)


class _Audio1GainControl_Type(Integer32):
    """Custom type audio1GainControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("joint", 1)
    )


_Audio1GainControl_Type.__name__ = "Integer32"
_Audio1GainControl_Object = MibScalar
audio1GainControl = _Audio1GainControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 1, 1),
    _Audio1GainControl_Type()
)
audio1GainControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audio1GainControl.setStatus("current")


class _Audio1LeftGain_Type(Integer32):
    """Custom type audio1LeftGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 0),
    )


_Audio1LeftGain_Type.__name__ = "Integer32"
_Audio1LeftGain_Object = MibScalar
audio1LeftGain = _Audio1LeftGain_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 1, 2),
    _Audio1LeftGain_Type()
)
audio1LeftGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio1LeftGain.setStatus("current")


class _Audio1RightGain_Type(Integer32):
    """Custom type audio1RightGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 0),
    )


_Audio1RightGain_Type.__name__ = "Integer32"
_Audio1RightGain_Object = MibScalar
audio1RightGain = _Audio1RightGain_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 1, 3),
    _Audio1RightGain_Type()
)
audio1RightGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audio1RightGain.setStatus("current")


class _Audio1DiagNorm_Type(Integer32):
    """Custom type audio1DiagNorm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Audio1DiagNorm_Type.__name__ = "Integer32"
_Audio1DiagNorm_Object = MibScalar
audio1DiagNorm = _Audio1DiagNorm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 1, 4),
    _Audio1DiagNorm_Type()
)
audio1DiagNorm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio1DiagNorm.setStatus("current")


class _Audio1DownMix_Type(Integer32):
    """Custom type audio1DownMix based on Integer32"""
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
        *(("mono", 0),
          ("dualMono", 1),
          ("stereo", 2),
          ("surround", 3))
    )


_Audio1DownMix_Type.__name__ = "Integer32"
_Audio1DownMix_Object = MibScalar
audio1DownMix = _Audio1DownMix_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 1, 5),
    _Audio1DownMix_Type()
)
audio1DownMix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio1DownMix.setStatus("current")


class _Audio1Compression_Type(Integer32):
    """Custom type audio1Compression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("moderate", 1),
          ("heavy", 2))
    )


_Audio1Compression_Type.__name__ = "Integer32"
_Audio1Compression_Object = MibScalar
audio1Compression = _Audio1Compression_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 1, 6),
    _Audio1Compression_Type()
)
audio1Compression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio1Compression.setStatus("current")
_Audio2Config_ObjectIdentity = ObjectIdentity
audio2Config = _Audio2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 2)
)


class _Audio2GainControl_Type(Integer32):
    """Custom type audio2GainControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("joint", 1)
    )


_Audio2GainControl_Type.__name__ = "Integer32"
_Audio2GainControl_Object = MibScalar
audio2GainControl = _Audio2GainControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 2, 1),
    _Audio2GainControl_Type()
)
audio2GainControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audio2GainControl.setStatus("current")


class _Audio2LeftGain_Type(Integer32):
    """Custom type audio2LeftGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 0),
    )


_Audio2LeftGain_Type.__name__ = "Integer32"
_Audio2LeftGain_Object = MibScalar
audio2LeftGain = _Audio2LeftGain_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 2, 2),
    _Audio2LeftGain_Type()
)
audio2LeftGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio2LeftGain.setStatus("current")


class _Audio2RightGain_Type(Integer32):
    """Custom type audio2RightGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 0),
    )


_Audio2RightGain_Type.__name__ = "Integer32"
_Audio2RightGain_Object = MibScalar
audio2RightGain = _Audio2RightGain_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 2, 3),
    _Audio2RightGain_Type()
)
audio2RightGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audio2RightGain.setStatus("current")


class _Audio2DiagNorm_Type(Integer32):
    """Custom type audio2DiagNorm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Audio2DiagNorm_Type.__name__ = "Integer32"
_Audio2DiagNorm_Object = MibScalar
audio2DiagNorm = _Audio2DiagNorm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 2, 4),
    _Audio2DiagNorm_Type()
)
audio2DiagNorm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio2DiagNorm.setStatus("current")


class _Audio2DownMix_Type(Integer32):
    """Custom type audio2DownMix based on Integer32"""
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
        *(("mono", 0),
          ("dualMono", 1),
          ("stereo", 2),
          ("surround", 3))
    )


_Audio2DownMix_Type.__name__ = "Integer32"
_Audio2DownMix_Object = MibScalar
audio2DownMix = _Audio2DownMix_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 2, 5),
    _Audio2DownMix_Type()
)
audio2DownMix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio2DownMix.setStatus("current")


class _Audio2Compression_Type(Integer32):
    """Custom type audio2Compression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("moderate", 1),
          ("heavy", 2))
    )


_Audio2Compression_Type.__name__ = "Integer32"
_Audio2Compression_Object = MibScalar
audio2Compression = _Audio2Compression_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 1, 2, 6),
    _Audio2Compression_Type()
)
audio2Compression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio2Compression.setStatus("current")
_AudioOutput_ObjectIdentity = ObjectIdentity
audioOutput = _AudioOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2)
)
_Audio1Output_ObjectIdentity = ObjectIdentity
audio1Output = _Audio1Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 1)
)


class _Audio1LeftLanguage_Type(OctetString):
    """Custom type audio1LeftLanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_Audio1LeftLanguage_Type.__name__ = "OctetString"
_Audio1LeftLanguage_Object = MibScalar
audio1LeftLanguage = _Audio1LeftLanguage_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 1, 1),
    _Audio1LeftLanguage_Type()
)
audio1LeftLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio1LeftLanguage.setStatus("current")


class _Audio1RightLanguage_Type(OctetString):
    """Custom type audio1RightLanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_Audio1RightLanguage_Type.__name__ = "OctetString"
_Audio1RightLanguage_Object = MibScalar
audio1RightLanguage = _Audio1RightLanguage_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 1, 2),
    _Audio1RightLanguage_Type()
)
audio1RightLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio1RightLanguage.setStatus("current")


class _Audio1LeftLanguageStatus_Type(OctetString):
    """Custom type audio1LeftLanguageStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_Audio1LeftLanguageStatus_Type.__name__ = "OctetString"
_Audio1LeftLanguageStatus_Object = MibScalar
audio1LeftLanguageStatus = _Audio1LeftLanguageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 1, 3),
    _Audio1LeftLanguageStatus_Type()
)
audio1LeftLanguageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audio1LeftLanguageStatus.setStatus("current")


class _Audio1RightLanguageStatus_Type(OctetString):
    """Custom type audio1RightLanguageStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_Audio1RightLanguageStatus_Type.__name__ = "OctetString"
_Audio1RightLanguageStatus_Object = MibScalar
audio1RightLanguageStatus = _Audio1RightLanguageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 1, 4),
    _Audio1RightLanguageStatus_Type()
)
audio1RightLanguageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audio1RightLanguageStatus.setStatus("current")
_Audio2Output_ObjectIdentity = ObjectIdentity
audio2Output = _Audio2Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 2)
)


class _Audio2LeftLanguage_Type(OctetString):
    """Custom type audio2LeftLanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_Audio2LeftLanguage_Type.__name__ = "OctetString"
_Audio2LeftLanguage_Object = MibScalar
audio2LeftLanguage = _Audio2LeftLanguage_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 2, 1),
    _Audio2LeftLanguage_Type()
)
audio2LeftLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio2LeftLanguage.setStatus("current")


class _Audio2RightLanguage_Type(OctetString):
    """Custom type audio2RightLanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_Audio2RightLanguage_Type.__name__ = "OctetString"
_Audio2RightLanguage_Object = MibScalar
audio2RightLanguage = _Audio2RightLanguage_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 2, 2),
    _Audio2RightLanguage_Type()
)
audio2RightLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio2RightLanguage.setStatus("current")


class _Audio2LeftLanguageStatus_Type(OctetString):
    """Custom type audio2LeftLanguageStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_Audio2LeftLanguageStatus_Type.__name__ = "OctetString"
_Audio2LeftLanguageStatus_Object = MibScalar
audio2LeftLanguageStatus = _Audio2LeftLanguageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 2, 3),
    _Audio2LeftLanguageStatus_Type()
)
audio2LeftLanguageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audio2LeftLanguageStatus.setStatus("current")


class _Audio2RightLanguageStatus_Type(OctetString):
    """Custom type audio2RightLanguageStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_Audio2RightLanguageStatus_Type.__name__ = "OctetString"
_Audio2RightLanguageStatus_Object = MibScalar
audio2RightLanguageStatus = _Audio2RightLanguageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 6, 2, 2, 4),
    _Audio2RightLanguageStatus_Type()
)
audio2RightLanguageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audio2RightLanguageStatus.setStatus("current")
_DataMib_ObjectIdentity = ObjectIdentity
dataMib = _DataMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7)
)
_DataStatus_ObjectIdentity = ObjectIdentity
dataStatus = _DataStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 1)
)


class _EthernetIP_Type(Integer32):
    """Custom type ethernetIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defined", 0),
          ("notDefined", 1),
          ("unknown", 2))
    )


_EthernetIP_Type.__name__ = "Integer32"
_EthernetIP_Object = MibScalar
ethernetIP = _EthernetIP_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 1, 1),
    _EthernetIP_Type()
)
ethernetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIP.setStatus("current")
_TextSetup_ObjectIdentity = ObjectIdentity
textSetup = _TextSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 2)
)


class _SubtitleLanguage_Type(OctetString):
    """Custom type subtitleLanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_SubtitleLanguage_Type.__name__ = "OctetString"
_SubtitleLanguage_Object = MibScalar
subtitleLanguage = _SubtitleLanguage_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 2, 1),
    _SubtitleLanguage_Type()
)
subtitleLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitleLanguage.setStatus("current")


class _SubtitleLanguageStatus_Type(OctetString):
    """Custom type subtitleLanguageStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_SubtitleLanguageStatus_Type.__name__ = "OctetString"
_SubtitleLanguageStatus_Object = MibScalar
subtitleLanguageStatus = _SubtitleLanguageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 2, 2),
    _SubtitleLanguageStatus_Type()
)
subtitleLanguageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subtitleLanguageStatus.setStatus("current")


class _SubtitleDisplay_Type(Integer32):
    """Custom type subtitleDisplay based on Integer32"""
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
        *(("all", 0),
          ("avail", 1),
          ("status", 2),
          ("off", 3))
    )


_SubtitleDisplay_Type.__name__ = "Integer32"
_SubtitleDisplay_Object = MibScalar
subtitleDisplay = _SubtitleDisplay_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 2, 3),
    _SubtitleDisplay_Type()
)
subtitleDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtitleDisplay.setStatus("current")
_Ethernet10_100_ObjectIdentity = ObjectIdentity
ethernet10_100 = _Ethernet10_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 3)
)
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 3, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 3, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 3, 3),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")


class _MacAddr_Type(OctetString):
    """Custom type macAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_MacAddr_Type.__name__ = "OctetString"
_MacAddr_Object = MibScalar
macAddr = _MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 3, 4),
    _MacAddr_Type()
)
macAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddr.setStatus("current")
_EthernetGigE_ObjectIdentity = ObjectIdentity
ethernetGigE = _EthernetGigE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 4)
)
_GigEipAddress_Type = IpAddress
_GigEipAddress_Object = MibScalar
gigEipAddress = _GigEipAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 4, 1),
    _GigEipAddress_Type()
)
gigEipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigEipAddress.setStatus("current")
_GigEsubnetMask_Type = IpAddress
_GigEsubnetMask_Object = MibScalar
gigEsubnetMask = _GigEsubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 4, 2),
    _GigEsubnetMask_Type()
)
gigEsubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigEsubnetMask.setStatus("current")
_GigEgateway_Type = IpAddress
_GigEgateway_Object = MibScalar
gigEgateway = _GigEgateway_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 4, 3),
    _GigEgateway_Type()
)
gigEgateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigEgateway.setStatus("current")


class _GigEmacAddr_Type(OctetString):
    """Custom type gigEmacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_GigEmacAddr_Type.__name__ = "OctetString"
_GigEmacAddr_Object = MibScalar
gigEmacAddr = _GigEmacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 4, 4),
    _GigEmacAddr_Type()
)
gigEmacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigEmacAddr.setStatus("current")


class _GigEmode_Type(Integer32):
    """Custom type gigEmode based on Integer32"""
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
        *(("mpts", 0),
          ("disabled", 1),
          ("tsdsmcc", 2),
          ("dsmcc", 3))
    )


_GigEmode_Type.__name__ = "Integer32"
_GigEmode_Object = MibScalar
gigEmode = _GigEmode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 4, 5),
    _GigEmode_Type()
)
gigEmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigEmode.setStatus("current")
_MptsIpAddr_Type = IpAddress
_MptsIpAddr_Object = MibScalar
mptsIpAddr = _MptsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 4, 6),
    _MptsIpAddr_Type()
)
mptsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mptsIpAddr.setStatus("current")


class _MptsPort_Type(Integer32):
    """Custom type mptsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MptsPort_Type.__name__ = "Integer32"
_MptsPort_Object = MibScalar
mptsPort = _MptsPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 7, 4, 7),
    _MptsPort_Type()
)
mptsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mptsPort.setStatus("current")
_ExtHardwareMib_ObjectIdentity = ObjectIdentity
extHardwareMib = _ExtHardwareMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 8)
)
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 8, 1)
)


class _AlarmTrigger_Type(Integer32):
    """Custom type alarmTrigger based on Integer32"""
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
        *(("noSignal", 0),
          ("noVideoPresent", 1),
          ("noAuthorization", 2),
          ("auto", 3),
          ("disabled", 4))
    )


_AlarmTrigger_Type.__name__ = "Integer32"
_AlarmTrigger_Object = MibScalar
alarmTrigger = _AlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 8, 1, 2),
    _AlarmTrigger_Type()
)
alarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrigger.setStatus("current")


class _AlarmTest_Type(Integer32):
    """Custom type alarmTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_AlarmTest_Type.__name__ = "Integer32"
_AlarmTest_Object = MibScalar
alarmTest = _AlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 8, 1, 3),
    _AlarmTest_Type()
)
alarmTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTest.setStatus("current")
_StatusMib_ObjectIdentity = ObjectIdentity
statusMib = _StatusMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 9)
)
_AccessControl_ObjectIdentity = ObjectIdentity
accessControl = _AccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 9, 1)
)


class _UnitAddress_Type(OctetString):
    """Custom type unitAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_UnitAddress_Type.__name__ = "OctetString"
_UnitAddress_Object = MibScalar
unitAddress = _UnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 9, 1, 1),
    _UnitAddress_Type()
)
unitAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAddress.setStatus("current")


class _TvPasscard_Type(OctetString):
    """Custom type tvPasscard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )
    fixed_length = 26


_TvPasscard_Type.__name__ = "OctetString"
_TvPasscard_Object = MibScalar
tvPasscard = _TvPasscard_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 9, 1, 2),
    _TvPasscard_Type()
)
tvPasscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvPasscard.setStatus("current")
_Firmware_ObjectIdentity = ObjectIdentity
firmware = _Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 9, 2)
)


class _BootVersion_Type(OctetString):
    """Custom type bootVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_BootVersion_Type.__name__ = "OctetString"
_BootVersion_Object = MibScalar
bootVersion = _BootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 9, 2, 1),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("current")


class _FpgaVersion_Type(OctetString):
    """Custom type fpgaVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FpgaVersion_Type.__name__ = "OctetString"
_FpgaVersion_Object = MibScalar
fpgaVersion = _FpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 9, 2, 2),
    _FpgaVersion_Type()
)
fpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaVersion.setStatus("current")


class _FirmwareVersion_Type(OctetString):
    """Custom type firmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FirmwareVersion_Type.__name__ = "OctetString"
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 9, 2, 3),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _UpgradeFirmwareVersion_Type(OctetString):
    """Custom type upgradeFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_UpgradeFirmwareVersion_Type.__name__ = "OctetString"
_UpgradeFirmwareVersion_Object = MibScalar
upgradeFirmwareVersion = _UpgradeFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 9, 2, 4),
    _UpgradeFirmwareVersion_Type()
)
upgradeFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFirmwareVersion.setStatus("current")
_DiagnosticMib_ObjectIdentity = ObjectIdentity
diagnosticMib = _DiagnosticMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10)
)
_ScreenDisplay_ObjectIdentity = ObjectIdentity
screenDisplay = _ScreenDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 1)
)


class _DiagnosticScreen_Type(Integer32):
    """Custom type diagnosticScreen based on Integer32"""
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("fastFacts1", 1),
          ("fastFacts2", 2),
          ("fastFacts3", 3),
          ("fastFacts4", 4),
          ("fastFacts5", 5),
          ("diagA", 6),
          ("diagB", 7),
          ("diagBMD", 8),
          ("diagC", 9),
          ("diagD", 10),
          ("diagE", 11))
    )


_DiagnosticScreen_Type.__name__ = "Integer32"
_DiagnosticScreen_Object = MibScalar
diagnosticScreen = _DiagnosticScreen_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 1, 1),
    _DiagnosticScreen_Type()
)
diagnosticScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagnosticScreen.setStatus("current")


class _ClearCounters_Type(Integer32):
    """Custom type clearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("yes", 0),
          ("no", 1))
    )


_ClearCounters_Type.__name__ = "Integer32"
_ClearCounters_Object = MibScalar
clearCounters = _ClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 1, 2),
    _ClearCounters_Type()
)
clearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCounters.setStatus("current")
_TestSignals_ObjectIdentity = ObjectIdentity
testSignals = _TestSignals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 2)
)


class _VideoTestPattern_Type(Integer32):
    """Custom type videoTestPattern based on Integer32"""
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
        *(("off", 0),
          ("colorBar525", 1),
          ("ire100Ramp", 2),
          ("ntsc7Combination", 3),
          ("redField", 4),
          ("ntsc7Composite", 5),
          ("fiveStepStair", 6),
          ("unModulatedYRamp", 7))
    )


_VideoTestPattern_Type.__name__ = "Integer32"
_VideoTestPattern_Object = MibScalar
videoTestPattern = _VideoTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 2, 1),
    _VideoTestPattern_Type()
)
videoTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoTestPattern.setStatus("current")


class _Audio1TestPattern_Type(Integer32):
    """Custom type audio1TestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testToneA-1000", 0),
          ("testToneB-4040-3960", 1),
          ("off", 2))
    )


_Audio1TestPattern_Type.__name__ = "Integer32"
_Audio1TestPattern_Object = MibScalar
audio1TestPattern = _Audio1TestPattern_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 2, 2),
    _Audio1TestPattern_Type()
)
audio1TestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio1TestPattern.setStatus("current")


class _Audio2TestPattern_Type(Integer32):
    """Custom type audio2TestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testToneA-1000", 0),
          ("testToneB-4040-3960", 1),
          ("off", 2))
    )


_Audio2TestPattern_Type.__name__ = "Integer32"
_Audio2TestPattern_Object = MibScalar
audio2TestPattern = _Audio2TestPattern_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 2, 3),
    _Audio2TestPattern_Type()
)
audio2TestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audio2TestPattern.setStatus("current")


class _CueToneSignal_Type(Integer32):
    """Custom type cueToneSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CueToneSignal_Type.__name__ = "Integer32"
_CueToneSignal_Object = MibScalar
cueToneSignal = _CueToneSignal_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 2, 4),
    _CueToneSignal_Type()
)
cueToneSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueToneSignal.setStatus("current")
_Vits_ObjectIdentity = ObjectIdentity
vits = _Vits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 3)
)


class _Waveform_Type(Integer32):
    """Custom type waveform based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("transmitted", 0),
          ("disabled", 1),
          ("colorBar525", 2),
          ("ire100Ramp", 3),
          ("ntsc7Combination", 4),
          ("redField", 5),
          ("ntsc7Composite", 6),
          ("fiveStepStair", 7),
          ("unModulatedYRamp", 8))
    )


_Waveform_Type.__name__ = "Integer32"
_Waveform_Object = MibScalar
waveform = _Waveform_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 3, 1),
    _Waveform_Type()
)
waveform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waveform.setStatus("current")


class _Field_Type(Integer32):
    """Custom type field based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("field1", 0),
          ("field2", 1),
          ("na", 2))
    )


_Field_Type.__name__ = "Integer32"
_Field_Object = MibScalar
field = _Field_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 3, 2),
    _Field_Type()
)
field.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    field.setStatus("current")


class _Line_Type(Integer32):
    """Custom type line based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line17", 0),
          ("line18", 1),
          ("na", 2))
    )


_Line_Type.__name__ = "Integer32"
_Line_Object = MibScalar
line = _Line_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 10, 3, 3),
    _Line_Type()
)
line.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    line.setStatus("current")
_SignalStatus_ObjectIdentity = ObjectIdentity
signalStatus = _SignalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11)
)


class _AcquisitionState_Type(Integer32):
    """Custom type acquisitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unLocked", 1))
    )


_AcquisitionState_Type.__name__ = "Integer32"
_AcquisitionState_Object = MibScalar
acquisitionState = _AcquisitionState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 1),
    _AcquisitionState_Type()
)
acquisitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acquisitionState.setStatus("current")


class _AuthorizationState_Type(Integer32):
    """Custom type authorizationState based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("missingMap", 0),
          ("undefinedChannel", 1),
          ("undefinedService", 2),
          ("notInSync", 3),
          ("noProgramRekey", 4),
          ("noWorkingKey", 5),
          ("noEventBlackOut", 6),
          ("noCategoryKey", 7),
          ("oldCategorySequence", 8),
          ("programBought", 9),
          ("programBoughtWithoutTaping", 10),
          ("subscribedWithTaping", 11),
          ("subscribedWithoutTaping", 12),
          ("subscribedWithTapingPurchasable", 13),
          ("ippvWithTaping", 14),
          ("ippvWithoutTaping", 15),
          ("badSeedChecksum", 16),
          ("badDebitChecksum", 17),
          ("ippvNotEnabled", 18),
          ("insufficientCreditToPurchase", 19),
          ("showCountLimitExceeded", 20),
          ("debitRegisterWillOverflow", 21),
          ("noAnytimeFreePreviewRecordsAvailable", 22),
          ("maximumPackageCostExceeded", 23),
          ("noIPPVOverlayInMessage", 24),
          ("notSubscribed", 25),
          ("regionalBlackout", 26),
          ("eventBlackout", 27),
          ("circulatBlackout", 28),
          ("authorized", 29),
          ("unencrypted", 30),
          ("unknown", 31))
    )


_AuthorizationState_Type.__name__ = "Integer32"
_AuthorizationState_Object = MibScalar
authorizationState = _AuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 2),
    _AuthorizationState_Type()
)
authorizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizationState.setStatus("current")


class _EncryptionMode_Type(Integer32):
    """Custom type encryptionMode based on Integer32"""
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
        *(("encrypted", 0),
          ("fixedWorkingKey", 1),
          ("fixedProgramKey", 2),
          ("unencrypted", 3),
          ("na", 4))
    )


_EncryptionMode_Type.__name__ = "Integer32"
_EncryptionMode_Object = MibScalar
encryptionMode = _EncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 3),
    _EncryptionMode_Type()
)
encryptionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionMode.setStatus("current")


class _UnitAddr_Type(OctetString):
    """Custom type unitAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_UnitAddr_Type.__name__ = "OctetString"
_UnitAddr_Object = MibScalar
unitAddr = _UnitAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 4),
    _UnitAddr_Type()
)
unitAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAddr.setStatus("current")


class _VctIDFast_Type(Integer32):
    """Custom type vctIDFast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VctIDFast_Type.__name__ = "Integer32"
_VctIDFast_Object = MibScalar
vctIDFast = _VctIDFast_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 5),
    _VctIDFast_Type()
)
vctIDFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctIDFast.setStatus("current")


class _ChannelNum_Type(Integer32):
    """Custom type channelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ChannelNum_Type.__name__ = "Integer32"
_ChannelNum_Object = MibScalar
channelNum = _ChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 6),
    _ChannelNum_Type()
)
channelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNum.setStatus("current")


class _ServiceNumber_Type(Integer32):
    """Custom type serviceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ServiceNumber_Type.__name__ = "Integer32"
_ServiceNumber_Object = MibScalar
serviceNumber = _ServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 7),
    _ServiceNumber_Type()
)
serviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceNumber.setStatus("current")


class _SignalQuality_Type(Integer32):
    """Custom type signalQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SignalQuality_Type.__name__ = "Integer32"
_SignalQuality_Object = MibScalar
signalQuality = _SignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 8),
    _SignalQuality_Type()
)
signalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalQuality.setStatus("current")


class _SignalPower_Type(Integer32):
    """Custom type signalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-800, 0),
    )


_SignalPower_Type.__name__ = "Integer32"
_SignalPower_Object = MibScalar
signalPower = _SignalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 9),
    _SignalPower_Type()
)
signalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalPower.setStatus("current")


class _EbNo_Type(Integer32):
    """Custom type ebNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 150),
    )


_EbNo_Type.__name__ = "Integer32"
_EbNo_Object = MibScalar
ebNo = _EbNo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 10),
    _EbNo_Type()
)
ebNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebNo.setStatus("current")


class _SymbolRate_Type(Integer32):
    """Custom type symbolRate based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("sr29Msps", 0),
          ("sr19Msps", 1),
          ("sr14Msps", 2),
          ("sr11Msps", 3),
          ("sr9Msps", 4),
          ("sr7Msps", 5),
          ("sr4Msps", 6),
          ("sr3Msps", 7),
          ("unknown", 8))
    )


_SymbolRate_Type.__name__ = "Integer32"
_SymbolRate_Object = MibScalar
symbolRate = _SymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 11),
    _SymbolRate_Type()
)
symbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symbolRate.setStatus("current")


class _FecRate_Type(Integer32):
    """Custom type fecRate based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("cr5-11", 0),
          ("cr1-2", 1),
          ("cr1-92-8PSK", 2),
          ("cr3-5", 3),
          ("cr2-05-8PSK", 4),
          ("cr2-3", 5),
          ("cr2-11-8PSK", 6),
          ("cr3-4", 7),
          ("cr4-5", 8),
          ("cr5-6", 9),
          ("cr2-19-8PSK", 10),
          ("cr7-8", 11),
          ("cr2-30-8PSK", 12),
          ("cr2-40-8PSK", 13),
          ("unknown", 14))
    )


_FecRate_Type.__name__ = "Integer32"
_FecRate_Object = MibScalar
fecRate = _FecRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 12),
    _FecRate_Type()
)
fecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecRate.setStatus("current")


class _Freq_Type(Integer32):
    """Custom type freq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(950000, 2150000),
    )


_Freq_Type.__name__ = "Integer32"
_Freq_Object = MibScalar
freq = _Freq_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 13),
    _Freq_Type()
)
freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freq.setStatus("current")


class _SatelliteName_Type(OctetString):
    """Custom type satelliteName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_SatelliteName_Type.__name__ = "OctetString"
_SatelliteName_Object = MibScalar
satelliteName = _SatelliteName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 14),
    _SatelliteName_Type()
)
satelliteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteName.setStatus("current")


class _XpndrNumber_Type(Integer32):
    """Custom type xpndrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_XpndrNumber_Type.__name__ = "Integer32"
_XpndrNumber_Object = MibScalar
xpndrNumber = _XpndrNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 15),
    _XpndrNumber_Type()
)
xpndrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpndrNumber.setStatus("current")


class _Polarization_Type(Integer32):
    """Custom type polarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h", 0),
          ("v", 1),
          ("unknown", 2))
    )


_Polarization_Type.__name__ = "Integer32"
_Polarization_Object = MibScalar
polarization = _Polarization_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 16),
    _Polarization_Type()
)
polarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polarization.setStatus("current")


class _MuxStatus_Type(Integer32):
    """Custom type muxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("combined", 0),
          ("split", 1),
          ("unknown", 2))
    )


_MuxStatus_Type.__name__ = "Integer32"
_MuxStatus_Object = MibScalar
muxStatus = _MuxStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 11, 17),
    _MuxStatus_Type()
)
muxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxStatus.setStatus("current")
_LedStatus_ObjectIdentity = ObjectIdentity
ledStatus = _LedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 12)
)


class _SignalLED_Type(Integer32):
    """Custom type signalLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("blink", 2))
    )


_SignalLED_Type.__name__ = "Integer32"
_SignalLED_Object = MibScalar
signalLED = _SignalLED_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 12, 1),
    _SignalLED_Type()
)
signalLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalLED.setStatus("current")


class _AuthorizedLED_Type(Integer32):
    """Custom type authorizedLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("blink", 2))
    )


_AuthorizedLED_Type.__name__ = "Integer32"
_AuthorizedLED_Object = MibScalar
authorizedLED = _AuthorizedLED_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 12, 2),
    _AuthorizedLED_Type()
)
authorizedLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedLED.setStatus("current")


class _AlarmConditionLED_Type(Integer32):
    """Custom type alarmConditionLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("blink", 2))
    )


_AlarmConditionLED_Type.__name__ = "Integer32"
_AlarmConditionLED_Object = MibScalar
alarmConditionLED = _AlarmConditionLED_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 12, 3),
    _AlarmConditionLED_Type()
)
alarmConditionLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmConditionLED.setStatus("current")


class _DownloadLED_Type(Integer32):
    """Custom type downloadLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("blink", 2))
    )


_DownloadLED_Type.__name__ = "Integer32"
_DownloadLED_Object = MibScalar
downloadLED = _DownloadLED_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 12, 8),
    _DownloadLED_Type()
)
downloadLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downloadLED.setStatus("current")
_RetuneMonitorMIB_ObjectIdentity = ObjectIdentity
retuneMonitorMIB = _RetuneMonitorMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 13)
)


class _RetuneMonitorEnable_Type(Integer32):
    """Custom type retuneMonitorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_RetuneMonitorEnable_Type.__name__ = "Integer32"
_RetuneMonitorEnable_Object = MibScalar
retuneMonitorEnable = _RetuneMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 13, 1),
    _RetuneMonitorEnable_Type()
)
retuneMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    retuneMonitorEnable.setStatus("current")


class _RetuneMsgStatistic_Type(Integer32):
    """Custom type retuneMsgStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RetuneMsgStatistic_Type.__name__ = "Integer32"
_RetuneMsgStatistic_Object = MibScalar
retuneMsgStatistic = _RetuneMsgStatistic_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 13, 2),
    _RetuneMsgStatistic_Type()
)
retuneMsgStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retuneMsgStatistic.setStatus("current")


class _RetuneMsgVirtNetworkIDindex_Type(Integer32):
    """Custom type retuneMsgVirtNetworkIDindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RetuneMsgVirtNetworkIDindex_Type.__name__ = "Integer32"
_RetuneMsgVirtNetworkIDindex_Object = MibScalar
retuneMsgVirtNetworkIDindex = _RetuneMsgVirtNetworkIDindex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 13, 3),
    _RetuneMsgVirtNetworkIDindex_Type()
)
retuneMsgVirtNetworkIDindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    retuneMsgVirtNetworkIDindex.setStatus("current")


class _RetuneMsgVCTid_Type(Integer32):
    """Custom type retuneMsgVCTid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RetuneMsgVCTid_Type.__name__ = "Integer32"
_RetuneMsgVCTid_Object = MibScalar
retuneMsgVCTid = _RetuneMsgVCTid_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 13, 4),
    _RetuneMsgVCTid_Type()
)
retuneMsgVCTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retuneMsgVCTid.setStatus("current")


class _RetuneMsgVirtChannel_Type(Integer32):
    """Custom type retuneMsgVirtChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RetuneMsgVirtChannel_Type.__name__ = "Integer32"
_RetuneMsgVirtChannel_Object = MibScalar
retuneMsgVirtChannel = _RetuneMsgVirtChannel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 13, 5),
    _RetuneMsgVirtChannel_Type()
)
retuneMsgVirtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retuneMsgVirtChannel.setStatus("current")


class _RetuneMsgActivationTime_Type(OctetString):
    """Custom type retuneMsgActivationTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_RetuneMsgActivationTime_Type.__name__ = "OctetString"
_RetuneMsgActivationTime_Object = MibScalar
retuneMsgActivationTime = _RetuneMsgActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 13, 6),
    _RetuneMsgActivationTime_Type()
)
retuneMsgActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retuneMsgActivationTime.setStatus("current")


class _RetuneMsgCRC_Type(OctetString):
    """Custom type retuneMsgCRC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_RetuneMsgCRC_Type.__name__ = "OctetString"
_RetuneMsgCRC_Object = MibScalar
retuneMsgCRC = _RetuneMsgCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 13, 7),
    _RetuneMsgCRC_Type()
)
retuneMsgCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retuneMsgCRC.setStatus("current")


class _RetuneMsgCnt_Type(Integer32):
    """Custom type retuneMsgCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RetuneMsgCnt_Type.__name__ = "Integer32"
_RetuneMsgCnt_Object = MibScalar
retuneMsgCnt = _RetuneMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 13, 8),
    _RetuneMsgCnt_Type()
)
retuneMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    retuneMsgCnt.setStatus("current")
_IdentificationGroup_ObjectIdentity = ObjectIdentity
identificationGroup = _IdentificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 14)
)
_IdentMIBVersion_Type = DisplayString
_IdentMIBVersion_Object = MibScalar
identMIBVersion = _IdentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 14, 1),
    _IdentMIBVersion_Type()
)
identMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identMIBVersion.setStatus("current")
_IdentUnitModel_Type = DisplayString
_IdentUnitModel_Object = MibScalar
identUnitModel = _IdentUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 14, 2),
    _IdentUnitModel_Type()
)
identUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identUnitModel.setStatus("current")
_AcpMib_ObjectIdentity = ObjectIdentity
acpMib = _AcpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 15)
)


class _AcpMode_Type(Integer32):
    """Custom type acpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_AcpMode_Type.__name__ = "Integer32"
_AcpMode_Object = MibScalar
acpMode = _AcpMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 15, 1),
    _AcpMode_Type()
)
acpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpMode.setStatus("current")


class _AcpIndex_Type(Integer32):
    """Custom type acpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcpIndex_Type.__name__ = "Integer32"
_AcpIndex_Object = MibScalar
acpIndex = _AcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 15, 2),
    _AcpIndex_Type()
)
acpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpIndex.setStatus("current")


class _AcpProgram_Type(Integer32):
    """Custom type acpProgram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcpProgram_Type.__name__ = "Integer32"
_AcpProgram_Object = MibScalar
acpProgram = _AcpProgram_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 15, 3),
    _AcpProgram_Type()
)
acpProgram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpProgram.setStatus("current")


class _AcpUnitAddress_Type(OctetString):
    """Custom type acpUnitAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_AcpUnitAddress_Type.__name__ = "OctetString"
_AcpUnitAddress_Object = MibScalar
acpUnitAddress = _AcpUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 15, 4),
    _AcpUnitAddress_Type()
)
acpUnitAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpUnitAddress.setStatus("current")


class _AcpKeyStream_Type(Integer32):
    """Custom type acpKeyStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcpKeyStream_Type.__name__ = "Integer32"
_AcpKeyStream_Object = MibScalar
acpKeyStream = _AcpKeyStream_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 15, 5),
    _AcpKeyStream_Type()
)
acpKeyStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpKeyStream.setStatus("current")


class _AcpAuthState_Type(OctetString):
    """Custom type acpAuthState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AcpAuthState_Type.__name__ = "OctetString"
_AcpAuthState_Object = MibScalar
acpAuthState = _AcpAuthState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 15, 6),
    _AcpAuthState_Type()
)
acpAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpAuthState.setStatus("current")


class _AcpEncryptMode_Type(OctetString):
    """Custom type acpEncryptMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AcpEncryptMode_Type.__name__ = "OctetString"
_AcpEncryptMode_Object = MibScalar
acpEncryptMode = _AcpEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 15, 7),
    _AcpEncryptMode_Type()
)
acpEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEncryptMode.setStatus("current")
_TestMib_ObjectIdentity = ObjectIdentity
testMib = _TestMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16)
)
_Audio_ObjectIdentity = ObjectIdentity
audio = _Audio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 1)
)


class _PrimaryAudioLock_Type(Integer32):
    """Custom type primaryAudioLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unLocked", 0),
          ("locked", 1))
    )


_PrimaryAudioLock_Type.__name__ = "Integer32"
_PrimaryAudioLock_Object = MibScalar
primaryAudioLock = _PrimaryAudioLock_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 1, 1),
    _PrimaryAudioLock_Type()
)
primaryAudioLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryAudioLock.setStatus("current")


class _SecondaryAudioLock_Type(Integer32):
    """Custom type secondaryAudioLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unLocked", 0),
          ("locked", 1))
    )


_SecondaryAudioLock_Type.__name__ = "Integer32"
_SecondaryAudioLock_Object = MibScalar
secondaryAudioLock = _SecondaryAudioLock_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 1, 2),
    _SecondaryAudioLock_Type()
)
secondaryAudioLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryAudioLock.setStatus("current")


class _PrimaryAudioPID_Type(Integer32):
    """Custom type primaryAudioPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_PrimaryAudioPID_Type.__name__ = "Integer32"
_PrimaryAudioPID_Object = MibScalar
primaryAudioPID = _PrimaryAudioPID_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 1, 4),
    _PrimaryAudioPID_Type()
)
primaryAudioPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryAudioPID.setStatus("current")


class _SecondaryAudioPID_Type(Integer32):
    """Custom type secondaryAudioPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SecondaryAudioPID_Type.__name__ = "Integer32"
_SecondaryAudioPID_Object = MibScalar
secondaryAudioPID = _SecondaryAudioPID_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 1, 5),
    _SecondaryAudioPID_Type()
)
secondaryAudioPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryAudioPID.setStatus("current")
_Video_ObjectIdentity = ObjectIdentity
video = _Video_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 2)
)


class _VideoLock_Type(Integer32):
    """Custom type videoLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unLocked", 0),
          ("locked", 1))
    )


_VideoLock_Type.__name__ = "Integer32"
_VideoLock_Object = MibScalar
videoLock = _VideoLock_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 2, 1),
    _VideoLock_Type()
)
videoLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoLock.setStatus("current")


class _VideoPID_Type(Integer32):
    """Custom type videoPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_VideoPID_Type.__name__ = "Integer32"
_VideoPID_Object = MibScalar
videoPID = _VideoPID_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 2, 2),
    _VideoPID_Type()
)
videoPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoPID.setStatus("current")
_CodeDownload_ObjectIdentity = ObjectIdentity
codeDownload = _CodeDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 3)
)


class _CodeDownloadBit_Type(Integer32):
    """Custom type codeDownloadBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CodeDownloadBit_Type.__name__ = "Integer32"
_CodeDownloadBit_Object = MibScalar
codeDownloadBit = _CodeDownloadBit_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 3, 1),
    _CodeDownloadBit_Type()
)
codeDownloadBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codeDownloadBit.setStatus("current")
_IrdStatus_ObjectIdentity = ObjectIdentity
irdStatus = _IrdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 4)
)
_FalseLock_ObjectIdentity = ObjectIdentity
falseLock = _FalseLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 4, 1)
)


class _FalseLockStatus_Type(Integer32):
    """Custom type falseLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unLocked", 0),
          ("locked", 1))
    )


_FalseLockStatus_Type.__name__ = "Integer32"
_FalseLockStatus_Object = MibScalar
falseLockStatus = _FalseLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 4, 1, 1),
    _FalseLockStatus_Type()
)
falseLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falseLockStatus.setStatus("current")
_AlarmLedStatus_ObjectIdentity = ObjectIdentity
alarmLedStatus = _AlarmLedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 4, 2)
)


class _AlarmLEDBlinkStatus_Type(Integer32):
    """Custom type alarmLEDBlinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notBlinking", 0),
          ("blinking", 1))
    )


_AlarmLEDBlinkStatus_Type.__name__ = "Integer32"
_AlarmLEDBlinkStatus_Object = MibScalar
alarmLEDBlinkStatus = _AlarmLEDBlinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 4, 2, 1),
    _AlarmLEDBlinkStatus_Type()
)
alarmLEDBlinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLEDBlinkStatus.setStatus("current")
_Messages_ObjectIdentity = ObjectIdentity
messages = _Messages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5)
)


class _PatMsgCount_Type(Integer32):
    """Custom type patMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PatMsgCount_Type.__name__ = "Integer32"
_PatMsgCount_Object = MibScalar
patMsgCount = _PatMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 1),
    _PatMsgCount_Type()
)
patMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    patMsgCount.setStatus("current")


class _CaMsgCount_Type(Integer32):
    """Custom type caMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaMsgCount_Type.__name__ = "Integer32"
_CaMsgCount_Object = MibScalar
caMsgCount = _CaMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 2),
    _CaMsgCount_Type()
)
caMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caMsgCount.setStatus("current")


class _PmtMsgCount_Type(Integer32):
    """Custom type pmtMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmtMsgCount_Type.__name__ = "Integer32"
_PmtMsgCount_Object = MibScalar
pmtMsgCount = _PmtMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 3),
    _PmtMsgCount_Type()
)
pmtMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmtMsgCount.setStatus("current")


class _NiMsgCount_Type(Integer32):
    """Custom type niMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NiMsgCount_Type.__name__ = "Integer32"
_NiMsgCount_Object = MibScalar
niMsgCount = _NiMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 4),
    _NiMsgCount_Type()
)
niMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    niMsgCount.setStatus("current")


class _NetworkTextMsgCount_Type(Integer32):
    """Custom type networkTextMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetworkTextMsgCount_Type.__name__ = "Integer32"
_NetworkTextMsgCount_Object = MibScalar
networkTextMsgCount = _NetworkTextMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 5),
    _NetworkTextMsgCount_Type()
)
networkTextMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkTextMsgCount.setStatus("current")


class _VirtualChannelMsgCount_Type(Integer32):
    """Custom type virtualChannelMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualChannelMsgCount_Type.__name__ = "Integer32"
_VirtualChannelMsgCount_Object = MibScalar
virtualChannelMsgCount = _VirtualChannelMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 6),
    _VirtualChannelMsgCount_Type()
)
virtualChannelMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualChannelMsgCount.setStatus("current")


class _SubtitleMsgCount_Type(Integer32):
    """Custom type subtitleMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SubtitleMsgCount_Type.__name__ = "Integer32"
_SubtitleMsgCount_Object = MibScalar
subtitleMsgCount = _SubtitleMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 7),
    _SubtitleMsgCount_Type()
)
subtitleMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subtitleMsgCount.setStatus("current")


class _CoMsgCount_Type(Integer32):
    """Custom type coMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CoMsgCount_Type.__name__ = "Integer32"
_CoMsgCount_Object = MibScalar
coMsgCount = _CoMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 8),
    _CoMsgCount_Type()
)
coMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coMsgCount.setStatus("current")


class _DwnldPreMsgCount_Type(Integer32):
    """Custom type dwnldPreMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DwnldPreMsgCount_Type.__name__ = "Integer32"
_DwnldPreMsgCount_Object = MibScalar
dwnldPreMsgCount = _DwnldPreMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 9),
    _DwnldPreMsgCount_Type()
)
dwnldPreMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwnldPreMsgCount.setStatus("current")


class _DwnldMsgCount_Type(Integer32):
    """Custom type dwnldMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DwnldMsgCount_Type.__name__ = "Integer32"
_DwnldMsgCount_Object = MibScalar
dwnldMsgCount = _DwnldMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 10),
    _DwnldMsgCount_Type()
)
dwnldMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwnldMsgCount.setStatus("current")


class _EmmMsgCount_Type(Integer32):
    """Custom type emmMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EmmMsgCount_Type.__name__ = "Integer32"
_EmmMsgCount_Object = MibScalar
emmMsgCount = _EmmMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 11),
    _EmmMsgCount_Type()
)
emmMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emmMsgCount.setStatus("current")


class _FingerPrintMessageCount_Type(Integer32):
    """Custom type fingerPrintMessageCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FingerPrintMessageCount_Type.__name__ = "Integer32"
_FingerPrintMessageCount_Object = MibScalar
fingerPrintMessageCount = _FingerPrintMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 12),
    _FingerPrintMessageCount_Type()
)
fingerPrintMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fingerPrintMessageCount.setStatus("current")


class _HcmMsgCount_Type(Integer32):
    """Custom type hcmMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HcmMsgCount_Type.__name__ = "Integer32"
_HcmMsgCount_Object = MibScalar
hcmMsgCount = _HcmMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 13),
    _HcmMsgCount_Type()
)
hcmMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcmMsgCount.setStatus("current")


class _UimMsgCount_Type(Integer32):
    """Custom type uimMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UimMsgCount_Type.__name__ = "Integer32"
_UimMsgCount_Object = MibScalar
uimMsgCount = _UimMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 14),
    _UimMsgCount_Type()
)
uimMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimMsgCount.setStatus("current")


class _EvenBlkoutMsgCount_Type(Integer32):
    """Custom type evenBlkoutMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EvenBlkoutMsgCount_Type.__name__ = "Integer32"
_EvenBlkoutMsgCount_Object = MibScalar
evenBlkoutMsgCount = _EvenBlkoutMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 5, 15),
    _EvenBlkoutMsgCount_Type()
)
evenBlkoutMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evenBlkoutMsgCount.setStatus("current")
_Rf_ObjectIdentity = ObjectIdentity
rf = _Rf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 6)
)


class _FrequencyOffset_Type(Integer32):
    """Custom type frequencyOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_FrequencyOffset_Type.__name__ = "Integer32"
_FrequencyOffset_Object = MibScalar
frequencyOffset = _FrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 6, 1),
    _FrequencyOffset_Type()
)
frequencyOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyOffset.setStatus("current")


class _Ber_Type(Integer32):
    """Custom type ber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ber_Type.__name__ = "Integer32"
_Ber_Object = MibScalar
ber = _Ber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 6, 2),
    _Ber_Type()
)
ber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ber.setStatus("current")


class _Ebno_Type(Integer32):
    """Custom type ebno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 50),
    )


_Ebno_Type.__name__ = "Integer32"
_Ebno_Object = MibScalar
ebno = _Ebno_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 6, 3),
    _Ebno_Type()
)
ebno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebno.setStatus("current")


class _Rserror_Type(Integer32):
    """Custom type rserror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rserror_Type.__name__ = "Integer32"
_Rserror_Object = MibScalar
rserror = _Rserror_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 6, 4),
    _Rserror_Type()
)
rserror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserror.setStatus("current")


class _Lostlockcount_Type(Integer32):
    """Custom type lostlockcount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Lostlockcount_Type.__name__ = "Integer32"
_Lostlockcount_Object = MibScalar
lostlockcount = _Lostlockcount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 6, 5),
    _Lostlockcount_Type()
)
lostlockcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lostlockcount.setStatus("current")


class _Clearrserror_Type(Integer32):
    """Custom type clearrserror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("yes", 0),
          ("no", 1))
    )


_Clearrserror_Type.__name__ = "Integer32"
_Clearrserror_Object = MibScalar
clearrserror = _Clearrserror_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 6, 6),
    _Clearrserror_Type()
)
clearrserror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearrserror.setStatus("current")


class _Clearlostlockcount_Type(Integer32):
    """Custom type clearlostlockcount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("yes", 0),
          ("no", 1))
    )


_Clearlostlockcount_Type.__name__ = "Integer32"
_Clearlostlockcount_Object = MibScalar
clearlostlockcount = _Clearlostlockcount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 6, 7),
    _Clearlostlockcount_Type()
)
clearlostlockcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearlostlockcount.setStatus("current")


class _Snr_Type(Integer32):
    """Custom type snr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Snr_Type.__name__ = "Integer32"
_Snr_Object = MibScalar
snr = _Snr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 1, 621, 16, 6, 8),
    _Snr_Type()
)
snr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSR4410MD-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "giMIB": giMIB,
       "giproducts": giproducts,
       "dsr": dsr,
       "videoMib": videoMib,
       "videoOutput525Lines": videoOutput525Lines,
       "videoOutput625Lines": videoOutput625Lines,
       "aspectRatioInput": aspectRatioInput,
       "aspectRatioOutput": aspectRatioOutput,
       "rfPortsMib": rfPortsMib,
       "rfPortsSetup": rfPortsSetup,
       "port1": port1,
       "port1SetupMode": port1SetupMode,
       "port1Satellite": port1Satellite,
       "port1Polarity": port1Polarity,
       "port2": port2,
       "port2SetupMode": port2SetupMode,
       "port2Satellite": port2Satellite,
       "port2Polarity": port2Polarity,
       "manualTune": manualTune,
       "activePort": activePort,
       "mode": mode,
       "transponderNumber": transponderNumber,
       "frequency": frequency,
       "dvbSymbolRate": dvbSymbolRate,
       "dvbCodeRate": dvbCodeRate,
       "symbolCodeBit": symbolCodeBit,
       "modulationMode": modulationMode,
       "psk8SymbolRate": psk8SymbolRate,
       "psk8CodeRate": psk8CodeRate,
       "dvbS2symbolRate": dvbS2symbolRate,
       "dvbS2codeRate": dvbS2codeRate,
       "channelMib": channelMib,
       "channelSelect": channelSelect,
       "vctID": vctID,
       "channelNumber": channelNumber,
       "channelStatus": channelStatus,
       "transponder": transponder,
       "source": source,
       "satelliteStatus": satelliteStatus,
       "serviceSelectionMib": serviceSelectionMib,
       "mpegServiceNumber": mpegServiceNumber,
       "unitControlMib": unitControlMib,
       "unitControl": unitControl,
       "contrast": contrast,
       "asiEnable": asiEnable,
       "lnbPower": lnbPower,
       "resetIRD": resetIRD,
       "formatRate": formatRate,
       "audioMib": audioMib,
       "audioConfig": audioConfig,
       "audio1Config": audio1Config,
       "audio1GainControl": audio1GainControl,
       "audio1LeftGain": audio1LeftGain,
       "audio1RightGain": audio1RightGain,
       "audio1DiagNorm": audio1DiagNorm,
       "audio1DownMix": audio1DownMix,
       "audio1Compression": audio1Compression,
       "audio2Config": audio2Config,
       "audio2GainControl": audio2GainControl,
       "audio2LeftGain": audio2LeftGain,
       "audio2RightGain": audio2RightGain,
       "audio2DiagNorm": audio2DiagNorm,
       "audio2DownMix": audio2DownMix,
       "audio2Compression": audio2Compression,
       "audioOutput": audioOutput,
       "audio1Output": audio1Output,
       "audio1LeftLanguage": audio1LeftLanguage,
       "audio1RightLanguage": audio1RightLanguage,
       "audio1LeftLanguageStatus": audio1LeftLanguageStatus,
       "audio1RightLanguageStatus": audio1RightLanguageStatus,
       "audio2Output": audio2Output,
       "audio2LeftLanguage": audio2LeftLanguage,
       "audio2RightLanguage": audio2RightLanguage,
       "audio2LeftLanguageStatus": audio2LeftLanguageStatus,
       "audio2RightLanguageStatus": audio2RightLanguageStatus,
       "dataMib": dataMib,
       "dataStatus": dataStatus,
       "ethernetIP": ethernetIP,
       "textSetup": textSetup,
       "subtitleLanguage": subtitleLanguage,
       "subtitleLanguageStatus": subtitleLanguageStatus,
       "subtitleDisplay": subtitleDisplay,
       "ethernet10-100": ethernet10_100,
       "ipAddress": ipAddress,
       "subnetMask": subnetMask,
       "defaultGateway": defaultGateway,
       "macAddr": macAddr,
       "ethernetGigE": ethernetGigE,
       "gigEipAddress": gigEipAddress,
       "gigEsubnetMask": gigEsubnetMask,
       "gigEgateway": gigEgateway,
       "gigEmacAddr": gigEmacAddr,
       "gigEmode": gigEmode,
       "mptsIpAddr": mptsIpAddr,
       "mptsPort": mptsPort,
       "extHardwareMib": extHardwareMib,
       "alarms": alarms,
       "alarmTrigger": alarmTrigger,
       "alarmTest": alarmTest,
       "statusMib": statusMib,
       "accessControl": accessControl,
       "unitAddress": unitAddress,
       "tvPasscard": tvPasscard,
       "firmware": firmware,
       "bootVersion": bootVersion,
       "fpgaVersion": fpgaVersion,
       "firmwareVersion": firmwareVersion,
       "upgradeFirmwareVersion": upgradeFirmwareVersion,
       "diagnosticMib": diagnosticMib,
       "screenDisplay": screenDisplay,
       "diagnosticScreen": diagnosticScreen,
       "clearCounters": clearCounters,
       "testSignals": testSignals,
       "videoTestPattern": videoTestPattern,
       "audio1TestPattern": audio1TestPattern,
       "audio2TestPattern": audio2TestPattern,
       "cueToneSignal": cueToneSignal,
       "vits": vits,
       "waveform": waveform,
       "field": field,
       "line": line,
       "signalStatus": signalStatus,
       "acquisitionState": acquisitionState,
       "authorizationState": authorizationState,
       "encryptionMode": encryptionMode,
       "unitAddr": unitAddr,
       "vctIDFast": vctIDFast,
       "channelNum": channelNum,
       "serviceNumber": serviceNumber,
       "signalQuality": signalQuality,
       "signalPower": signalPower,
       "ebNo": ebNo,
       "symbolRate": symbolRate,
       "fecRate": fecRate,
       "freq": freq,
       "satelliteName": satelliteName,
       "xpndrNumber": xpndrNumber,
       "polarization": polarization,
       "muxStatus": muxStatus,
       "ledStatus": ledStatus,
       "signalLED": signalLED,
       "authorizedLED": authorizedLED,
       "alarmConditionLED": alarmConditionLED,
       "downloadLED": downloadLED,
       "retuneMonitorMIB": retuneMonitorMIB,
       "retuneMonitorEnable": retuneMonitorEnable,
       "retuneMsgStatistic": retuneMsgStatistic,
       "retuneMsgVirtNetworkIDindex": retuneMsgVirtNetworkIDindex,
       "retuneMsgVCTid": retuneMsgVCTid,
       "retuneMsgVirtChannel": retuneMsgVirtChannel,
       "retuneMsgActivationTime": retuneMsgActivationTime,
       "retuneMsgCRC": retuneMsgCRC,
       "retuneMsgCnt": retuneMsgCnt,
       "identificationGroup": identificationGroup,
       "identMIBVersion": identMIBVersion,
       "identUnitModel": identUnitModel,
       "acpMib": acpMib,
       "acpMode": acpMode,
       "acpIndex": acpIndex,
       "acpProgram": acpProgram,
       "acpUnitAddress": acpUnitAddress,
       "acpKeyStream": acpKeyStream,
       "acpAuthState": acpAuthState,
       "acpEncryptMode": acpEncryptMode,
       "testMib": testMib,
       "audio": audio,
       "primaryAudioLock": primaryAudioLock,
       "secondaryAudioLock": secondaryAudioLock,
       "primaryAudioPID": primaryAudioPID,
       "secondaryAudioPID": secondaryAudioPID,
       "video": video,
       "videoLock": videoLock,
       "videoPID": videoPID,
       "codeDownload": codeDownload,
       "codeDownloadBit": codeDownloadBit,
       "irdStatus": irdStatus,
       "falseLock": falseLock,
       "falseLockStatus": falseLockStatus,
       "alarmLedStatus": alarmLedStatus,
       "alarmLEDBlinkStatus": alarmLEDBlinkStatus,
       "messages": messages,
       "patMsgCount": patMsgCount,
       "caMsgCount": caMsgCount,
       "pmtMsgCount": pmtMsgCount,
       "niMsgCount": niMsgCount,
       "networkTextMsgCount": networkTextMsgCount,
       "virtualChannelMsgCount": virtualChannelMsgCount,
       "subtitleMsgCount": subtitleMsgCount,
       "coMsgCount": coMsgCount,
       "dwnldPreMsgCount": dwnldPreMsgCount,
       "dwnldMsgCount": dwnldMsgCount,
       "emmMsgCount": emmMsgCount,
       "fingerPrintMessageCount": fingerPrintMessageCount,
       "hcmMsgCount": hcmMsgCount,
       "uimMsgCount": uimMsgCount,
       "evenBlkoutMsgCount": evenBlkoutMsgCount,
       "rf": rf,
       "frequencyOffset": frequencyOffset,
       "ber": ber,
       "ebno": ebno,
       "rserror": rserror,
       "lostlockcount": lostlockcount,
       "clearrserror": clearrserror,
       "clearlostlockcount": clearlostlockcount,
       "snr": snr}
)
