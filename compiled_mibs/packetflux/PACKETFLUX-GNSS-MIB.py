# SNMP MIB module (PACKETFLUX-GNSS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetflux\PACKETFLUX-GNSS-MIB

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

(packetfluxFeatureSpecific,) = mibBuilder.importSymbols(
    "PACKETFLUX-SMI",
    "packetfluxFeatureSpecific")

(Fixed2DecimalDigits,
 Fixed6DecimalDigits) = mibBuilder.importSymbols(
    "PACKETFLUX-TC",
    "Fixed2DecimalDigits",
    "Fixed6DecimalDigits")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

packetfluxGnss = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4)
)
if mibBuilder.loadTexts:
    packetfluxGnss.setRevisions(
        ("2020-04-12 05:46",
         "2018-07-07 12:57")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class GnssConstellationEnum(TextualConvention, Integer32):
    status = "current"
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
        *(("gps", 1),
          ("glonass", 2),
          ("galileo", 3),
          ("beidou", 4),
          ("irnss", 5),
          ("qzss", 6))
    )



class GnssFixTypeEnum(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("twodimensional", 2),
          ("threedimensional", 3),
          ("differential3d", 4))
    )



# MIB Managed Objects in the order of their OIDs

_GnssReceiverTable_Object = MibTable
gnssReceiverTable = _GnssReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1)
)
if mibBuilder.loadTexts:
    gnssReceiverTable.setStatus("current")
_GnssReceiverEntry_Object = MibTableRow
gnssReceiverEntry = _GnssReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1)
)
gnssReceiverEntry.setIndexNames(
    (0, "PACKETFLUX-GNSS-MIB", "gnssReceiverSlot"),
    (0, "PACKETFLUX-GNSS-MIB", "gnssReceiverPort"),
)
if mibBuilder.loadTexts:
    gnssReceiverEntry.setStatus("current")
_GnssReceiverSlot_Type = Unsigned32
_GnssReceiverSlot_Object = MibTableColumn
gnssReceiverSlot = _GnssReceiverSlot_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 1),
    _GnssReceiverSlot_Type()
)
gnssReceiverSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gnssReceiverSlot.setStatus("current")
_GnssReceiverPort_Type = Unsigned32
_GnssReceiverPort_Object = MibTableColumn
gnssReceiverPort = _GnssReceiverPort_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 2),
    _GnssReceiverPort_Type()
)
gnssReceiverPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gnssReceiverPort.setStatus("current")
_GnssLatitude_Type = Fixed6DecimalDigits
_GnssLatitude_Object = MibTableColumn
gnssLatitude = _GnssLatitude_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 3),
    _GnssLatitude_Type()
)
gnssLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssLatitude.setStatus("current")
if mibBuilder.loadTexts:
    gnssLatitude.setUnits("degrees")
_GnssLongitude_Type = Fixed6DecimalDigits
_GnssLongitude_Object = MibTableColumn
gnssLongitude = _GnssLongitude_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 4),
    _GnssLongitude_Type()
)
gnssLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssLongitude.setStatus("current")
if mibBuilder.loadTexts:
    gnssLongitude.setUnits("degrees")
_GnssAltitude_Type = Fixed2DecimalDigits
_GnssAltitude_Object = MibTableColumn
gnssAltitude = _GnssAltitude_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 5),
    _GnssAltitude_Type()
)
gnssAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssAltitude.setStatus("current")
_GnssDateAndTime_Type = DateAndTime
_GnssDateAndTime_Object = MibTableColumn
gnssDateAndTime = _GnssDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 6),
    _GnssDateAndTime_Type()
)
gnssDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssDateAndTime.setStatus("current")
_GnssSatellitesInView_Type = Gauge32
_GnssSatellitesInView_Object = MibTableColumn
gnssSatellitesInView = _GnssSatellitesInView_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 7),
    _GnssSatellitesInView_Type()
)
gnssSatellitesInView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatellitesInView.setStatus("current")
_GnssSatellitesUsed_Type = Gauge32
_GnssSatellitesUsed_Object = MibTableColumn
gnssSatellitesUsed = _GnssSatellitesUsed_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 8),
    _GnssSatellitesUsed_Type()
)
gnssSatellitesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatellitesUsed.setStatus("current")
_GnssPDOP_Type = Fixed2DecimalDigits
_GnssPDOP_Object = MibTableColumn
gnssPDOP = _GnssPDOP_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 9),
    _GnssPDOP_Type()
)
gnssPDOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssPDOP.setStatus("current")
_GnssHDOP_Type = Fixed2DecimalDigits
_GnssHDOP_Object = MibTableColumn
gnssHDOP = _GnssHDOP_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 10),
    _GnssHDOP_Type()
)
gnssHDOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssHDOP.setStatus("current")
_GnssVDOP_Type = Fixed2DecimalDigits
_GnssVDOP_Object = MibTableColumn
gnssVDOP = _GnssVDOP_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 11),
    _GnssVDOP_Type()
)
gnssVDOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssVDOP.setStatus("current")
_GnssFixType_Type = GnssFixTypeEnum
_GnssFixType_Object = MibTableColumn
gnssFixType = _GnssFixType_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 12),
    _GnssFixType_Type()
)
gnssFixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssFixType.setStatus("current")
_Gnss1PPSCorrectPulses_Type = Counter32
_Gnss1PPSCorrectPulses_Object = MibTableColumn
gnss1PPSCorrectPulses = _Gnss1PPSCorrectPulses_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 13),
    _Gnss1PPSCorrectPulses_Type()
)
gnss1PPSCorrectPulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSCorrectPulses.setStatus("current")
_Gnss1PPSMissingPulses_Type = Counter32
_Gnss1PPSMissingPulses_Object = MibTableColumn
gnss1PPSMissingPulses = _Gnss1PPSMissingPulses_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 14),
    _Gnss1PPSMissingPulses_Type()
)
gnss1PPSMissingPulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSMissingPulses.setStatus("current")
_Gnss1PPSMissingInRowPulses_Type = Counter32
_Gnss1PPSMissingInRowPulses_Object = MibTableColumn
gnss1PPSMissingInRowPulses = _Gnss1PPSMissingInRowPulses_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 15),
    _Gnss1PPSMissingInRowPulses_Type()
)
gnss1PPSMissingInRowPulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSMissingInRowPulses.setStatus("current")
_Gnss1PPSDoublePulses_Type = Counter32
_Gnss1PPSDoublePulses_Object = MibTableColumn
gnss1PPSDoublePulses = _Gnss1PPSDoublePulses_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 16),
    _Gnss1PPSDoublePulses_Type()
)
gnss1PPSDoublePulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSDoublePulses.setStatus("current")
_Gnss1PPSVeryEarlyPulses_Type = Counter32
_Gnss1PPSVeryEarlyPulses_Object = MibTableColumn
gnss1PPSVeryEarlyPulses = _Gnss1PPSVeryEarlyPulses_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 17),
    _Gnss1PPSVeryEarlyPulses_Type()
)
gnss1PPSVeryEarlyPulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSVeryEarlyPulses.setStatus("current")
_Gnss1PPSSlightlyEarlyPulses_Type = Counter32
_Gnss1PPSSlightlyEarlyPulses_Object = MibTableColumn
gnss1PPSSlightlyEarlyPulses = _Gnss1PPSSlightlyEarlyPulses_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 18),
    _Gnss1PPSSlightlyEarlyPulses_Type()
)
gnss1PPSSlightlyEarlyPulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSSlightlyEarlyPulses.setStatus("current")
_Gnss1PPSSlightlyLatePulses_Type = Counter32
_Gnss1PPSSlightlyLatePulses_Object = MibTableColumn
gnss1PPSSlightlyLatePulses = _Gnss1PPSSlightlyLatePulses_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 19),
    _Gnss1PPSSlightlyLatePulses_Type()
)
gnss1PPSSlightlyLatePulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSSlightlyLatePulses.setStatus("current")
_Gnss1PPSVeryLatePulses_Type = Counter32
_Gnss1PPSVeryLatePulses_Object = MibTableColumn
gnss1PPSVeryLatePulses = _Gnss1PPSVeryLatePulses_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 20),
    _Gnss1PPSVeryLatePulses_Type()
)
gnss1PPSVeryLatePulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSVeryLatePulses.setStatus("current")
_Gnss1PPSFailedSeconds_Type = Counter32
_Gnss1PPSFailedSeconds_Object = MibTableColumn
gnss1PPSFailedSeconds = _Gnss1PPSFailedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 21),
    _Gnss1PPSFailedSeconds_Type()
)
gnss1PPSFailedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSFailedSeconds.setStatus("current")
_Gnss1PPSFailed_Type = TruthValue
_Gnss1PPSFailed_Object = MibTableColumn
gnss1PPSFailed = _Gnss1PPSFailed_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 1, 1, 22),
    _Gnss1PPSFailed_Type()
)
gnss1PPSFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnss1PPSFailed.setStatus("current")
_GnssSatelliteTable_Object = MibTable
gnssSatelliteTable = _GnssSatelliteTable_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 2)
)
if mibBuilder.loadTexts:
    gnssSatelliteTable.setStatus("current")
_GnssSatelliteEntry_Object = MibTableRow
gnssSatelliteEntry = _GnssSatelliteEntry_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 2, 1)
)
gnssSatelliteEntry.setIndexNames(
    (0, "PACKETFLUX-GNSS-MIB", "gnssReceiverSlot"),
    (0, "PACKETFLUX-GNSS-MIB", "gnssReceiverPort"),
    (0, "PACKETFLUX-GNSS-MIB", "gnssSatelliteIndex"),
)
if mibBuilder.loadTexts:
    gnssSatelliteEntry.setStatus("current")
_GnssSatelliteIndex_Type = Unsigned32
_GnssSatelliteIndex_Object = MibTableColumn
gnssSatelliteIndex = _GnssSatelliteIndex_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 2, 1, 1),
    _GnssSatelliteIndex_Type()
)
gnssSatelliteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gnssSatelliteIndex.setStatus("current")
_GnssSatelliteConstellation_Type = GnssConstellationEnum
_GnssSatelliteConstellation_Object = MibTableColumn
gnssSatelliteConstellation = _GnssSatelliteConstellation_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 2, 1, 2),
    _GnssSatelliteConstellation_Type()
)
gnssSatelliteConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatelliteConstellation.setStatus("current")
_GnssSatelliteNumber_Type = Unsigned32
_GnssSatelliteNumber_Object = MibTableColumn
gnssSatelliteNumber = _GnssSatelliteNumber_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 2, 1, 3),
    _GnssSatelliteNumber_Type()
)
gnssSatelliteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatelliteNumber.setStatus("current")
_GnssSatelliteAzimuth_Type = Unsigned32
_GnssSatelliteAzimuth_Object = MibTableColumn
gnssSatelliteAzimuth = _GnssSatelliteAzimuth_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 2, 1, 4),
    _GnssSatelliteAzimuth_Type()
)
gnssSatelliteAzimuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatelliteAzimuth.setStatus("current")
_GnssSatelliteElevation_Type = Unsigned32
_GnssSatelliteElevation_Object = MibTableColumn
gnssSatelliteElevation = _GnssSatelliteElevation_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 2, 1, 5),
    _GnssSatelliteElevation_Type()
)
gnssSatelliteElevation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatelliteElevation.setStatus("current")
_GnssSatelliteSNR_Type = Gauge32
_GnssSatelliteSNR_Object = MibTableColumn
gnssSatelliteSNR = _GnssSatelliteSNR_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 2, 1, 6),
    _GnssSatelliteSNR_Type()
)
gnssSatelliteSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatelliteSNR.setStatus("current")
_GnsSatelliteUsedInSolution_Type = TruthValue
_GnsSatelliteUsedInSolution_Object = MibTableColumn
gnsSatelliteUsedInSolution = _GnsSatelliteUsedInSolution_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 2, 1, 7),
    _GnsSatelliteUsedInSolution_Type()
)
gnsSatelliteUsedInSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnsSatelliteUsedInSolution.setStatus("current")
_PacketfluxGnssConformance_ObjectIdentity = ObjectIdentity
packetfluxGnssConformance = _PacketfluxGnssConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 127)
)
_PacketfluxGnssGroups_ObjectIdentity = ObjectIdentity
packetfluxGnssGroups = _PacketfluxGnssGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 127, 1)
)

# Managed Objects groups

packetfluxGnssMibAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32050, 3, 4, 127, 1, 1)
)
packetfluxGnssMibAllObjects.setObjects(
      *(("PACKETFLUX-GNSS-MIB", "gnss1PPSCorrectPulses"),
        ("PACKETFLUX-GNSS-MIB", "gnss1PPSDoublePulses"),
        ("PACKETFLUX-GNSS-MIB", "gnss1PPSFailed"),
        ("PACKETFLUX-GNSS-MIB", "gnss1PPSFailedSeconds"),
        ("PACKETFLUX-GNSS-MIB", "gnss1PPSMissingInRowPulses"),
        ("PACKETFLUX-GNSS-MIB", "gnss1PPSMissingPulses"),
        ("PACKETFLUX-GNSS-MIB", "gnss1PPSSlightlyEarlyPulses"),
        ("PACKETFLUX-GNSS-MIB", "gnss1PPSSlightlyLatePulses"),
        ("PACKETFLUX-GNSS-MIB", "gnss1PPSVeryEarlyPulses"),
        ("PACKETFLUX-GNSS-MIB", "gnss1PPSVeryLatePulses"),
        ("PACKETFLUX-GNSS-MIB", "gnssAltitude"),
        ("PACKETFLUX-GNSS-MIB", "gnsSatelliteUsedInSolution"),
        ("PACKETFLUX-GNSS-MIB", "gnssDateAndTime"),
        ("PACKETFLUX-GNSS-MIB", "gnssFixType"),
        ("PACKETFLUX-GNSS-MIB", "gnssHDOP"),
        ("PACKETFLUX-GNSS-MIB", "gnssLatitude"),
        ("PACKETFLUX-GNSS-MIB", "gnssLongitude"),
        ("PACKETFLUX-GNSS-MIB", "gnssPDOP"),
        ("PACKETFLUX-GNSS-MIB", "gnssSatelliteAzimuth"),
        ("PACKETFLUX-GNSS-MIB", "gnssSatelliteConstellation"),
        ("PACKETFLUX-GNSS-MIB", "gnssSatelliteElevation"),
        ("PACKETFLUX-GNSS-MIB", "gnssSatelliteNumber"),
        ("PACKETFLUX-GNSS-MIB", "gnssSatellitesInView"),
        ("PACKETFLUX-GNSS-MIB", "gnssSatelliteSNR"),
        ("PACKETFLUX-GNSS-MIB", "gnssSatellitesUsed"),
        ("PACKETFLUX-GNSS-MIB", "gnssVDOP"))
)
if mibBuilder.loadTexts:
    packetfluxGnssMibAllObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFLUX-GNSS-MIB",
    **{"GnssConstellationEnum": GnssConstellationEnum,
       "GnssFixTypeEnum": GnssFixTypeEnum,
       "packetfluxGnss": packetfluxGnss,
       "gnssReceiverTable": gnssReceiverTable,
       "gnssReceiverEntry": gnssReceiverEntry,
       "gnssReceiverSlot": gnssReceiverSlot,
       "gnssReceiverPort": gnssReceiverPort,
       "gnssLatitude": gnssLatitude,
       "gnssLongitude": gnssLongitude,
       "gnssAltitude": gnssAltitude,
       "gnssDateAndTime": gnssDateAndTime,
       "gnssSatellitesInView": gnssSatellitesInView,
       "gnssSatellitesUsed": gnssSatellitesUsed,
       "gnssPDOP": gnssPDOP,
       "gnssHDOP": gnssHDOP,
       "gnssVDOP": gnssVDOP,
       "gnssFixType": gnssFixType,
       "gnss1PPSCorrectPulses": gnss1PPSCorrectPulses,
       "gnss1PPSMissingPulses": gnss1PPSMissingPulses,
       "gnss1PPSMissingInRowPulses": gnss1PPSMissingInRowPulses,
       "gnss1PPSDoublePulses": gnss1PPSDoublePulses,
       "gnss1PPSVeryEarlyPulses": gnss1PPSVeryEarlyPulses,
       "gnss1PPSSlightlyEarlyPulses": gnss1PPSSlightlyEarlyPulses,
       "gnss1PPSSlightlyLatePulses": gnss1PPSSlightlyLatePulses,
       "gnss1PPSVeryLatePulses": gnss1PPSVeryLatePulses,
       "gnss1PPSFailedSeconds": gnss1PPSFailedSeconds,
       "gnss1PPSFailed": gnss1PPSFailed,
       "gnssSatelliteTable": gnssSatelliteTable,
       "gnssSatelliteEntry": gnssSatelliteEntry,
       "gnssSatelliteIndex": gnssSatelliteIndex,
       "gnssSatelliteConstellation": gnssSatelliteConstellation,
       "gnssSatelliteNumber": gnssSatelliteNumber,
       "gnssSatelliteAzimuth": gnssSatelliteAzimuth,
       "gnssSatelliteElevation": gnssSatelliteElevation,
       "gnssSatelliteSNR": gnssSatelliteSNR,
       "gnsSatelliteUsedInSolution": gnsSatelliteUsedInSolution,
       "packetfluxGnssConformance": packetfluxGnssConformance,
       "packetfluxGnssGroups": packetfluxGnssGroups,
       "packetfluxGnssMibAllObjects": packetfluxGnssMibAllObjects}
)
