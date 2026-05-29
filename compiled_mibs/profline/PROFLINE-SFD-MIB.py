# SNMP MIB module (PROFLINE-SFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\profline\PROFLINE-SFD-MIB

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

(demodulators,) = mibBuilder.importSymbols(
    "PROFLINE-MIB",
    "demodulators")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTrapOID,
 sysDescr,
 sysLocation,
 sysName,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTrapOID",
    "sysDescr",
    "sysLocation",
    "sysName",
    "sysUpTime")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sfd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sfd.setRevisions(
        ("2010-10-18 07:49",
         "2010-09-22 08:30",
         "2010-05-27 15:00",
         "2010-04-08 12:00",
         "2009-12-02 08:47",
         "2009-10-07 14:40",
         "2009-02-28 07:30",
         "2008-12-10 08:02",
         "2008-09-12 10:50",
         "2008-07-30 13:50",
         "2008-04-16 11:19")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LockToSourceModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("rds", 2),
          ("sntp", 3))
    )



class RfInInputModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )



class FilterIfMpxModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mono", 1),
          ("narrow", 2),
          ("wide", 3))
    )



class MpxPreEmphaseModes(TextualConvention, Integer32):
    status = "current"
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



class MpxSourceModes(TextualConvention, Integer32):
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
        *(("internal", 1),
          ("externalAuto", 2),
          ("external15kHz", 3),
          ("external100kHz", 4))
    )



class MpxRdsModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rds", 1),
          ("rbds", 2))
    )



class AudioTesttoneModes(TextualConvention, Integer32):
    status = "current"
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



class AudioDeEmphaseModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d0uS", 1),
          ("d50uS", 2),
          ("d75uS", 3))
    )



class AlarmModes(TextualConvention, Integer32):
    status = "current"
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
        *(("off", 1),
          ("warningOnly", 2),
          ("warningPlusRelayA", 3),
          ("warningPlusRelayB", 4),
          ("warningPlusRelayC", 5))
    )



class InputModes(TextualConvention, Integer32):
    status = "current"
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
              72)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 1),
          ("inputAB", 2),
          ("frequencyPlus10kHz", 3),
          ("frequencyPlus100kHz", 4),
          ("frequencyMinus10kHz", 5),
          ("frequencyMinus100kHz", 6),
          ("presetNext", 7),
          ("presetPrevious", 8),
          ("preset1", 9),
          ("preset2", 10),
          ("preset3", 11),
          ("preset4", 12),
          ("preset5", 13),
          ("preset6", 14),
          ("preset7", 15),
          ("preset8", 16),
          ("preset9", 17),
          ("preset10", 18),
          ("preset11", 19),
          ("preset12", 20),
          ("preset13", 21),
          ("preset14", 22),
          ("preset15", 23),
          ("preset16", 24),
          ("preset17", 25),
          ("preset18", 26),
          ("preset19", 27),
          ("preset20", 28),
          ("preset21", 29),
          ("preset22", 30),
          ("preset23", 31),
          ("preset24", 32),
          ("preset25", 33),
          ("preset26", 34),
          ("preset27", 35),
          ("preset28", 36),
          ("preset29", 37),
          ("preset30", 38),
          ("preset31", 39),
          ("preset32", 40),
          ("preset33", 41),
          ("preset34", 42),
          ("preset35", 43),
          ("preset36", 44),
          ("preset37", 45),
          ("preset38", 46),
          ("preset39", 47),
          ("preset40", 48),
          ("preset41", 49),
          ("preset42", 50),
          ("preset43", 51),
          ("preset44", 52),
          ("preset45", 53),
          ("preset46", 54),
          ("preset47", 55),
          ("preset48", 56),
          ("preset49", 57),
          ("preset50", 58),
          ("preset51", 59),
          ("preset52", 60),
          ("preset53", 61),
          ("preset54", 62),
          ("preset55", 63),
          ("preset56", 64),
          ("preset57", 65),
          ("preset58", 66),
          ("preset59", 67),
          ("preset60", 68),
          ("preset61", 69),
          ("preset62", 70),
          ("preset63", 71),
          ("preset64", 72))
    )



class OutputModes(TextualConvention, Integer32):
    status = "current"
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
        *(("notUsed", 1),
          ("rdsTA", 2),
          ("rdsTP", 3),
          ("rdsTAAndTp", 4),
          ("rdsMS", 5),
          ("rdsPTYnews", 6),
          ("rdsPTYalarm", 7),
          ("mpxMonoOrStereo", 8))
    )



class RdsTAModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )



class RdsTPModes(TextualConvention, Integer32):
    status = "current"
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



class RdsDIModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mono", 1),
          ("stereo", 2))
    )



class RdsMSModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speech", 1),
          ("music", 2))
    )



class RdsPTYModes(TextualConvention, Integer32):
    status = "current"
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
              64)
        )
    )
    namedValues = NamedValues(
        *(("rdsNone", 1),
          ("rdsNews", 2),
          ("rdsCurrentAffairs", 3),
          ("rdsInformation", 4),
          ("rdsSport", 5),
          ("rdsEducation", 6),
          ("rdsDrama", 7),
          ("rdsCultures", 8),
          ("rdsScience", 9),
          ("rdsVariedSpeech", 10),
          ("rdsPopMusic", 11),
          ("rdsRockMusic", 12),
          ("rdsEasyListening", 13),
          ("rdsLightClassics", 14),
          ("rdsSeriousClassics", 15),
          ("rdsOtherMusic", 16),
          ("rdsWeatherMetr", 17),
          ("rdsFinance", 18),
          ("rdsChildrensProgs", 19),
          ("rdsSocialAffairs", 20),
          ("rdsReligion", 21),
          ("rdsPhoneIn", 22),
          ("rdsTravelTouring", 23),
          ("rdsLeisureHobby", 24),
          ("rdsJazzMusic", 25),
          ("rdsCountryMusic", 26),
          ("rdsNationalMusic", 27),
          ("rdsOldiesMusic", 28),
          ("rdsFolkMusic", 29),
          ("rdsDocumentary", 30),
          ("rdsAlarmTest", 31),
          ("rdsAlarmAlarm", 32),
          ("rbdsNone", 33),
          ("rbdsNews", 34),
          ("rbdsInformation", 35),
          ("rbdsSports", 36),
          ("rbdsTalk", 37),
          ("rbdsRock", 38),
          ("rbdsClassicRock", 39),
          ("rbdsAdultHits", 40),
          ("rbdsSoftRock", 41),
          ("rbdsTop40", 42),
          ("rbdsCountry", 43),
          ("rbdsOldies", 44),
          ("rbdsSoft", 45),
          ("rbdsNostalgia", 46),
          ("rbdsJazz", 47),
          ("rbdsClassical", 48),
          ("rbdsRhythmAndBlues", 49),
          ("rbdsSoftRhythmAndBlues", 50),
          ("rbdsLanguage", 51),
          ("rbdsReligiousMusic", 52),
          ("rbdsReligiousTalk", 53),
          ("rbdsPersonality", 54),
          ("rbdsPublic", 55),
          ("rbdsCollege", 56),
          ("rbdsUnassigned1", 57),
          ("rbdsUnassigned2", 58),
          ("rbdsUnassigned3", 59),
          ("rbdsUnassigned4", 60),
          ("rbdsUnassigned5", 61),
          ("rbdsWeather", 62),
          ("rbdsEmergencyTest", 63),
          ("rbdsEmergency", 64))
    )



class ControlMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2),
          ("localPlusRemote", 3))
    )



class NotificationOffOn(TextualConvention, Integer32):
    status = "current"
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



class NotificationSettingChangedFrom(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("web", 2),
          ("local", 3))
    )



class AlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noProblem", 1),
          ("warning", 3),
          ("alarm", 5))
    )



class NotificationModes(TextualConvention, Integer32):
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
        *(("off", 1),
          ("warning", 2),
          ("warningAndAlarm", 3),
          ("alarm", 4))
    )



class TimezoneModes(TextualConvention, Integer32):
    status = "current"
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
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87)
        )
    )
    namedValues = NamedValues(
        *(("tzUTCminus12h00Internationaldatelinewest", 1),
          ("tzUTCminus11h00MidwayislandSamoa", 2),
          ("tzUTCminus10h00Hawaii", 3),
          ("tzUTCminus09h00Alaska", 4),
          ("tzUTCminus08h00Pacifictimeusandcanada", 5),
          ("tzUTCminus08h00TijuanaBajacalifornia", 6),
          ("tzUTCminus07h00Arizona", 7),
          ("tzUTCminus07h00ChihuahuaLapazMazatlan", 8),
          ("tzUTCminus07h00Mountaintimeusandcanada", 9),
          ("tzUTCminus06h00Centralamerica", 10),
          ("tzUTCminus06h00Centraltimeusandcanada", 11),
          ("tzUTCminus06h00GuadalajaraMexicocityMonterrey", 12),
          ("tzUTCminus06h00Saskatchewan", 13),
          ("tzUTCminus05h00BogotaLimaQuitoRiobranco", 14),
          ("tzUTCminus05h00Easterntimeusandcanada", 15),
          ("tzUTCminus05h00Indianaeast", 16),
          ("tzUTCminus04h30Caracas", 17),
          ("tzUTCminus04h00Atlantictimecanada", 18),
          ("tzUTCminus04h00Lapaz", 19),
          ("tzUTCminus04h00Manaus", 20),
          ("tzUTCminus04h00Santiago", 21),
          ("tzUTCminus03h30Newfoundland", 22),
          ("tzUTCminus03h00Brasilia", 23),
          ("tzUTCminus03h00BuenosAires", 24),
          ("tzUTCminus03h00Georgetown", 25),
          ("tzUTCminus03h00Greenland", 26),
          ("tzUTCminus03h00Montevideo", 27),
          ("tzUTCminus02h00Midatlantic", 28),
          ("tzUTCminus01h00Azores", 29),
          ("tzUTCminus01h00Capeverdeis", 30),
          ("tzUTCplus00h00Casablanca", 31),
          ("tzUTCplus00h00DublinEdinburghLisbonLondon", 32),
          ("tzUTCplus00h00UTCMonroviaReykjavik", 33),
          ("tzUTCplus01h00AmsterdamBerlinBernRomeStockholmVienna", 34),
          ("tzUTCplus01h00BelgradeBratislavaBudapestLjubljanaPrague", 35),
          ("tzUTCplus01h00BrusselsCopenhagenMadridParis", 36),
          ("tzUTCplus01h00SarajevoSkopjeWarsawZagreb", 37),
          ("tzUTCplus01h00Westcentralafrica", 38),
          ("tzUTCplus02h00Amman", 39),
          ("tzUTCplus02h00AthensBucharestIstanbul", 40),
          ("tzUTCplus02h00Beirut", 41),
          ("tzUTCplus02h00Cairo", 42),
          ("tzUTCplus02h00HararePretoria", 43),
          ("tzUTCplus02h00HelsinkiKyivRigaSofiaTallinnVilnius", 44),
          ("tzUTCplus02h00Jerusalem", 45),
          ("tzUTCplus02h00Minsk", 46),
          ("tzUTCplus02h00Windhoek", 47),
          ("tzUTCplus03h00Baghdad", 48),
          ("tzUTCplus03h00KuwaitRiyadh", 49),
          ("tzUTCplus03h00MoscowStpetersburgVolgograd", 50),
          ("tzUTCplus03h00Nairobi", 51),
          ("tzUTCplus03h00Tbilisi", 52),
          ("tzUTCplus03h30Tehran", 53),
          ("tzUTCplus04h00AbudhabiMuscat", 54),
          ("tzUTCplus04h00Baku", 55),
          ("tzUTCplus04h00Yerevan", 56),
          ("tzUTCplus04h30Kabul", 57),
          ("tzUTCplus05h00Ekaterinburg", 58),
          ("tzUTCplus05h00IslamabadKarachi", 59),
          ("tzUTCplus05h00Tashkent", 60),
          ("tzUTCplus05h30ChennaiKolkataMumbaiNewdelhi", 61),
          ("tzUTCplus05h30Srijayawardenepura", 62),
          ("tzUTCplus05h45Kathmandu", 63),
          ("tzUTCplus06h00AlmatyNovosibirsk", 64),
          ("tzUTCplus06h00AstanaDhaka", 65),
          ("tzUTCplus06h30Yangonrangoon", 66),
          ("tzUTCplus07h00BangkokHanoiJakarta", 67),
          ("tzUTCplus07h00Krasnoyarsk", 68),
          ("tzUTCplus08h00BeijingChongqingHongkongUrumqi", 69),
          ("tzUTCplus08h00IrkutskUlaanbataar", 70),
          ("tzUTCplus08h00KualalumpurSingapore", 71),
          ("tzUTCplus08h00Perth", 72),
          ("tzUTCplus08h00Taipei", 73),
          ("tzUTCplus09h00OsakaSapporoTokyo", 74),
          ("tzUTCplus09h00Seoul", 75),
          ("tzUTCplus09h00Yakutsk", 76),
          ("tzUTCplus09h30Adelaide", 77),
          ("tzUTCplus09h30Darwin", 78),
          ("tzUTCplus10h00Brisbane", 79),
          ("tzUTCplus10h00CanberraMelbourneSydney", 80),
          ("tzUTCplus10h00GuamPortmoresby", 81),
          ("tzUTCplus10h00Hobart", 82),
          ("tzUTCplus10h00Vladivostok", 83),
          ("tzUTCplus11h00MagadanSolomonisNewcaledonia", 84),
          ("tzUTCplus12h00AucklandWellington", 85),
          ("tzUTCplus12h00FijiKamchatkaMarshallis", 86),
          ("tzUTCplus13h00Nukualofa", 87))
    )



class DSTOffOn(TextualConvention, Integer32):
    status = "current"
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



class RfInMuted(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMuted", 1),
          ("muted", 2))
    )



# MIB Managed Objects in the order of their OIDs

_SfdNotifications_ObjectIdentity = ObjectIdentity
sfdNotifications = _SfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 0)
)
_SfdIdentity_ObjectIdentity = ObjectIdentity
sfdIdentity = _SfdIdentity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1)
)
_SfdIdnOptions_Type = OctetString
_SfdIdnOptions_Object = MibScalar
sfdIdnOptions = _SfdIdnOptions_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 1),
    _SfdIdnOptions_Type()
)
sfdIdnOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdIdnOptions.setStatus("current")


class _SfdIdnSerialNumber_Type(OctetString):
    """Custom type sfdIdnSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )
    fixed_length = 9


_SfdIdnSerialNumber_Type.__name__ = "OctetString"
_SfdIdnSerialNumber_Object = MibScalar
sfdIdnSerialNumber = _SfdIdnSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 2),
    _SfdIdnSerialNumber_Type()
)
sfdIdnSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdIdnSerialNumber.setStatus("current")
_SfdIdnFirmwareVersionTable_Object = MibTable
sfdIdnFirmwareVersionTable = _SfdIdnFirmwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sfdIdnFirmwareVersionTable.setStatus("current")
_SfdIdnFirmwareVersionEntry_Object = MibTableRow
sfdIdnFirmwareVersionEntry = _SfdIdnFirmwareVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 3, 1)
)
sfdIdnFirmwareVersionEntry.setIndexNames(
    (0, "PROFLINE-SFD-MIB", "sfdIdnFirmwareIndex"),
)
if mibBuilder.loadTexts:
    sfdIdnFirmwareVersionEntry.setStatus("current")


class _SfdIdnFirmwareIndex_Type(Integer32):
    """Custom type sfdIdnFirmwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SfdIdnFirmwareIndex_Type.__name__ = "Integer32"
_SfdIdnFirmwareIndex_Object = MibTableColumn
sfdIdnFirmwareIndex = _SfdIdnFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 3, 1, 1),
    _SfdIdnFirmwareIndex_Type()
)
sfdIdnFirmwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sfdIdnFirmwareIndex.setStatus("current")


class _SfdIdnFirmwareType_Type(OctetString):
    """Custom type sfdIdnFirmwareType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfdIdnFirmwareType_Type.__name__ = "OctetString"
_SfdIdnFirmwareType_Object = MibTableColumn
sfdIdnFirmwareType = _SfdIdnFirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 3, 1, 2),
    _SfdIdnFirmwareType_Type()
)
sfdIdnFirmwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdIdnFirmwareType.setStatus("current")


class _SfdIdnFirmwareVersion_Type(OctetString):
    """Custom type sfdIdnFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 8),
    )


_SfdIdnFirmwareVersion_Type.__name__ = "OctetString"
_SfdIdnFirmwareVersion_Object = MibTableColumn
sfdIdnFirmwareVersion = _SfdIdnFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 3, 1, 3),
    _SfdIdnFirmwareVersion_Type()
)
sfdIdnFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdIdnFirmwareVersion.setStatus("current")


class _SfdIdnDeviceInfo1_Type(OctetString):
    """Custom type sfdIdnDeviceInfo1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo1_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo1_Object = MibScalar
sfdIdnDeviceInfo1 = _SfdIdnDeviceInfo1_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 7),
    _SfdIdnDeviceInfo1_Type()
)
sfdIdnDeviceInfo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo1.setStatus("current")


class _SfdIdnDeviceInfo2_Type(OctetString):
    """Custom type sfdIdnDeviceInfo2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo2_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo2_Object = MibScalar
sfdIdnDeviceInfo2 = _SfdIdnDeviceInfo2_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 8),
    _SfdIdnDeviceInfo2_Type()
)
sfdIdnDeviceInfo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo2.setStatus("current")


class _SfdIdnDeviceInfo3_Type(OctetString):
    """Custom type sfdIdnDeviceInfo3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo3_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo3_Object = MibScalar
sfdIdnDeviceInfo3 = _SfdIdnDeviceInfo3_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 9),
    _SfdIdnDeviceInfo3_Type()
)
sfdIdnDeviceInfo3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo3.setStatus("current")


class _SfdIdnDeviceInfo4_Type(OctetString):
    """Custom type sfdIdnDeviceInfo4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo4_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo4_Object = MibScalar
sfdIdnDeviceInfo4 = _SfdIdnDeviceInfo4_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 10),
    _SfdIdnDeviceInfo4_Type()
)
sfdIdnDeviceInfo4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo4.setStatus("current")


class _SfdIdnDeviceInfo5_Type(OctetString):
    """Custom type sfdIdnDeviceInfo5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo5_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo5_Object = MibScalar
sfdIdnDeviceInfo5 = _SfdIdnDeviceInfo5_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 11),
    _SfdIdnDeviceInfo5_Type()
)
sfdIdnDeviceInfo5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo5.setStatus("current")


class _SfdIdnDeviceInfo6_Type(OctetString):
    """Custom type sfdIdnDeviceInfo6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo6_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo6_Object = MibScalar
sfdIdnDeviceInfo6 = _SfdIdnDeviceInfo6_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 12),
    _SfdIdnDeviceInfo6_Type()
)
sfdIdnDeviceInfo6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo6.setStatus("current")


class _SfdIdnDeviceInfo7_Type(OctetString):
    """Custom type sfdIdnDeviceInfo7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo7_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo7_Object = MibScalar
sfdIdnDeviceInfo7 = _SfdIdnDeviceInfo7_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 13),
    _SfdIdnDeviceInfo7_Type()
)
sfdIdnDeviceInfo7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo7.setStatus("current")


class _SfdIdnDeviceInfo8_Type(OctetString):
    """Custom type sfdIdnDeviceInfo8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo8_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo8_Object = MibScalar
sfdIdnDeviceInfo8 = _SfdIdnDeviceInfo8_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 14),
    _SfdIdnDeviceInfo8_Type()
)
sfdIdnDeviceInfo8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo8.setStatus("current")


class _SfdIdnDeviceInfo9_Type(OctetString):
    """Custom type sfdIdnDeviceInfo9 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo9_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo9_Object = MibScalar
sfdIdnDeviceInfo9 = _SfdIdnDeviceInfo9_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 15),
    _SfdIdnDeviceInfo9_Type()
)
sfdIdnDeviceInfo9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo9.setStatus("current")


class _SfdIdnDeviceInfo10_Type(OctetString):
    """Custom type sfdIdnDeviceInfo10 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo10_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo10_Object = MibScalar
sfdIdnDeviceInfo10 = _SfdIdnDeviceInfo10_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 16),
    _SfdIdnDeviceInfo10_Type()
)
sfdIdnDeviceInfo10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo10.setStatus("current")


class _SfdIdnDeviceInfo11_Type(OctetString):
    """Custom type sfdIdnDeviceInfo11 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo11_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo11_Object = MibScalar
sfdIdnDeviceInfo11 = _SfdIdnDeviceInfo11_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 17),
    _SfdIdnDeviceInfo11_Type()
)
sfdIdnDeviceInfo11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo11.setStatus("current")


class _SfdIdnDeviceInfo12_Type(OctetString):
    """Custom type sfdIdnDeviceInfo12 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SfdIdnDeviceInfo12_Type.__name__ = "OctetString"
_SfdIdnDeviceInfo12_Object = MibScalar
sfdIdnDeviceInfo12 = _SfdIdnDeviceInfo12_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 18),
    _SfdIdnDeviceInfo12_Type()
)
sfdIdnDeviceInfo12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceInfo12.setStatus("current")


class _SfdIdnDeviceManualLink_Type(OctetString):
    """Custom type sfdIdnDeviceManualLink based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SfdIdnDeviceManualLink_Type.__name__ = "OctetString"
_SfdIdnDeviceManualLink_Object = MibScalar
sfdIdnDeviceManualLink = _SfdIdnDeviceManualLink_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 1, 19),
    _SfdIdnDeviceManualLink_Type()
)
sfdIdnDeviceManualLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdIdnDeviceManualLink.setStatus("current")
_SfdSettings_ObjectIdentity = ObjectIdentity
sfdSettings = _SfdSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2)
)
_SfdSet_ObjectIdentity = ObjectIdentity
sfdSet = _SfdSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 1)
)


class _SfdSetReboot_Type(Integer32):
    """Custom type sfdSetReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SfdSetReboot_Type.__name__ = "Integer32"
_SfdSetReboot_Object = MibScalar
sfdSetReboot = _SfdSetReboot_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 1, 1),
    _SfdSetReboot_Type()
)
sfdSetReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetReboot.setStatus("current")


class _SfdSetAsPowerOnDefault_Type(Integer32):
    """Custom type sfdSetAsPowerOnDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SfdSetAsPowerOnDefault_Type.__name__ = "Integer32"
_SfdSetAsPowerOnDefault_Object = MibScalar
sfdSetAsPowerOnDefault = _SfdSetAsPowerOnDefault_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 1, 3),
    _SfdSetAsPowerOnDefault_Type()
)
sfdSetAsPowerOnDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAsPowerOnDefault.setStatus("current")
_SfdSetClock_ObjectIdentity = ObjectIdentity
sfdSetClock = _SfdSetClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 2)
)


class _SfdSetClockDateTime_Type(OctetString):
    """Custom type sfdSetClockDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_SfdSetClockDateTime_Type.__name__ = "OctetString"
_SfdSetClockDateTime_Object = MibScalar
sfdSetClockDateTime = _SfdSetClockDateTime_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 2, 1),
    _SfdSetClockDateTime_Type()
)
sfdSetClockDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetClockDateTime.setStatus("current")


class _SfdSetClockOffset_Type(Integer32):
    """Custom type sfdSetClockOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 120),
    )


_SfdSetClockOffset_Type.__name__ = "Integer32"
_SfdSetClockOffset_Object = MibScalar
sfdSetClockOffset = _SfdSetClockOffset_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 2, 2),
    _SfdSetClockOffset_Type()
)
sfdSetClockOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetClockOffset.setStatus("obsolete")
_SfdSetClockLockTo_Type = LockToSourceModes
_SfdSetClockLockTo_Object = MibScalar
sfdSetClockLockTo = _SfdSetClockLockTo_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 2, 3),
    _SfdSetClockLockTo_Type()
)
sfdSetClockLockTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetClockLockTo.setStatus("current")
_SfdSetClockTimezone_Type = TimezoneModes
_SfdSetClockTimezone_Object = MibScalar
sfdSetClockTimezone = _SfdSetClockTimezone_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 2, 4),
    _SfdSetClockTimezone_Type()
)
sfdSetClockTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetClockTimezone.setStatus("current")
_SfdSetClockDST_Type = DSTOffOn
_SfdSetClockDST_Object = MibScalar
sfdSetClockDST = _SfdSetClockDST_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 2, 5),
    _SfdSetClockDST_Type()
)
sfdSetClockDST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetClockDST.setStatus("current")
_SfdSetRfIn_ObjectIdentity = ObjectIdentity
sfdSetRfIn = _SfdSetRfIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 3)
)


class _SfdSetRfInFrequency_Type(Integer32):
    """Custom type sfdSetRfInFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8500, 11050),
    )


_SfdSetRfInFrequency_Type.__name__ = "Integer32"
_SfdSetRfInFrequency_Object = MibScalar
sfdSetRfInFrequency = _SfdSetRfInFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 3, 1),
    _SfdSetRfInFrequency_Type()
)
sfdSetRfInFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetRfInFrequency.setStatus("current")
_SfdSetRfInInput_Type = RfInInputModes
_SfdSetRfInInput_Object = MibScalar
sfdSetRfInInput = _SfdSetRfInInput_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 3, 2),
    _SfdSetRfInInput_Type()
)
sfdSetRfInInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetRfInInput.setStatus("current")


class _SfdSetRfInAttenuator_Type(Integer32):
    """Custom type sfdSetRfInAttenuator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_SfdSetRfInAttenuator_Type.__name__ = "Integer32"
_SfdSetRfInAttenuator_Object = MibScalar
sfdSetRfInAttenuator = _SfdSetRfInAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 3, 3),
    _SfdSetRfInAttenuator_Type()
)
sfdSetRfInAttenuator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetRfInAttenuator.setStatus("current")


class _SfdSetRfInMute_Type(Integer32):
    """Custom type sfdSetRfInMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 61),
    )


_SfdSetRfInMute_Type.__name__ = "Integer32"
_SfdSetRfInMute_Object = MibScalar
sfdSetRfInMute = _SfdSetRfInMute_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 3, 4),
    _SfdSetRfInMute_Type()
)
sfdSetRfInMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetRfInMute.setStatus("current")
_SfdSetFilter_ObjectIdentity = ObjectIdentity
sfdSetFilter = _SfdSetFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 4)
)
_SfdSetFilterIfMpx_Type = FilterIfMpxModes
_SfdSetFilterIfMpx_Object = MibScalar
sfdSetFilterIfMpx = _SfdSetFilterIfMpx_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 4, 1),
    _SfdSetFilterIfMpx_Type()
)
sfdSetFilterIfMpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetFilterIfMpx.setStatus("current")


class _SfdSetFilterStereoThreshold_Type(Integer32):
    """Custom type sfdSetFilterStereoThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 50),
    )


_SfdSetFilterStereoThreshold_Type.__name__ = "Integer32"
_SfdSetFilterStereoThreshold_Object = MibScalar
sfdSetFilterStereoThreshold = _SfdSetFilterStereoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 4, 2),
    _SfdSetFilterStereoThreshold_Type()
)
sfdSetFilterStereoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetFilterStereoThreshold.setStatus("current")
_SfdSetMpx_ObjectIdentity = ObjectIdentity
sfdSetMpx = _SfdSetMpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 5)
)


class _SfdSetMpxGain_Type(Integer32):
    """Custom type sfdSetMpxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 110),
    )


_SfdSetMpxGain_Type.__name__ = "Integer32"
_SfdSetMpxGain_Object = MibScalar
sfdSetMpxGain = _SfdSetMpxGain_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 5, 1),
    _SfdSetMpxGain_Type()
)
sfdSetMpxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetMpxGain.setStatus("current")
_SfdSetMpxPreEmphase_Type = MpxPreEmphaseModes
_SfdSetMpxPreEmphase_Object = MibScalar
sfdSetMpxPreEmphase = _SfdSetMpxPreEmphase_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 5, 2),
    _SfdSetMpxPreEmphase_Type()
)
sfdSetMpxPreEmphase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetMpxPreEmphase.setStatus("current")
_SfdSetMpxSource_Type = MpxSourceModes
_SfdSetMpxSource_Object = MibScalar
sfdSetMpxSource = _SfdSetMpxSource_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 5, 3),
    _SfdSetMpxSource_Type()
)
sfdSetMpxSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetMpxSource.setStatus("current")
_SfdSetMpxRdsMode_Type = MpxRdsModes
_SfdSetMpxRdsMode_Object = MibScalar
sfdSetMpxRdsMode = _SfdSetMpxRdsMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 5, 4),
    _SfdSetMpxRdsMode_Type()
)
sfdSetMpxRdsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetMpxRdsMode.setStatus("current")


class _SfdSetMpxResetMaxDeviation_Type(Integer32):
    """Custom type sfdSetMpxResetMaxDeviation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SfdSetMpxResetMaxDeviation_Type.__name__ = "Integer32"
_SfdSetMpxResetMaxDeviation_Object = MibScalar
sfdSetMpxResetMaxDeviation = _SfdSetMpxResetMaxDeviation_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 5, 5),
    _SfdSetMpxResetMaxDeviation_Type()
)
sfdSetMpxResetMaxDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetMpxResetMaxDeviation.setStatus("current")
_SfdSetAudio_ObjectIdentity = ObjectIdentity
sfdSetAudio = _SfdSetAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 6)
)


class _SfdSetAudioAnalogXlrGain_Type(Integer32):
    """Custom type sfdSetAudioAnalogXlrGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-960, 150),
    )


_SfdSetAudioAnalogXlrGain_Type.__name__ = "Integer32"
_SfdSetAudioAnalogXlrGain_Object = MibScalar
sfdSetAudioAnalogXlrGain = _SfdSetAudioAnalogXlrGain_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 6, 1),
    _SfdSetAudioAnalogXlrGain_Type()
)
sfdSetAudioAnalogXlrGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAudioAnalogXlrGain.setStatus("current")
_SfdSetAudioTesttone_Type = AudioTesttoneModes
_SfdSetAudioTesttone_Object = MibScalar
sfdSetAudioTesttone = _SfdSetAudioTesttone_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 6, 2),
    _SfdSetAudioTesttone_Type()
)
sfdSetAudioTesttone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAudioTesttone.setStatus("current")
_SfdSetAudioDeEmphase_Type = AudioDeEmphaseModes
_SfdSetAudioDeEmphase_Object = MibScalar
sfdSetAudioDeEmphase = _SfdSetAudioDeEmphase_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 6, 3),
    _SfdSetAudioDeEmphase_Type()
)
sfdSetAudioDeEmphase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAudioDeEmphase.setStatus("current")
_SfdSetName_ObjectIdentity = ObjectIdentity
sfdSetName = _SfdSetName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 7)
)


class _SfdSetNameUnit_Type(OctetString):
    """Custom type sfdSetNameUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SfdSetNameUnit_Type.__name__ = "OctetString"
_SfdSetNameUnit_Object = MibScalar
sfdSetNameUnit = _SfdSetNameUnit_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 7, 1),
    _SfdSetNameUnit_Type()
)
sfdSetNameUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNameUnit.setStatus("obsolete")
_SfdSetAlarm_ObjectIdentity = ObjectIdentity
sfdSetAlarm = _SfdSetAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8)
)
_SfdSetAlarmRfIn_ObjectIdentity = ObjectIdentity
sfdSetAlarmRfIn = _SfdSetAlarmRfIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1)
)
_SfdSetAlarmRfInLow_ObjectIdentity = ObjectIdentity
sfdSetAlarmRfInLow = _SfdSetAlarmRfInLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 1)
)
_SfdSetAlarmRfInLowMode_Type = AlarmModes
_SfdSetAlarmRfInLowMode_Object = MibScalar
sfdSetAlarmRfInLowMode = _SfdSetAlarmRfInLowMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 1, 1),
    _SfdSetAlarmRfInLowMode_Type()
)
sfdSetAlarmRfInLowMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRfInLowMode.setStatus("current")


class _SfdSetAlarmRfInLowLevel_Type(Integer32):
    """Custom type sfdSetAlarmRfInLowLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SfdSetAlarmRfInLowLevel_Type.__name__ = "Integer32"
_SfdSetAlarmRfInLowLevel_Object = MibScalar
sfdSetAlarmRfInLowLevel = _SfdSetAlarmRfInLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 1, 2),
    _SfdSetAlarmRfInLowLevel_Type()
)
sfdSetAlarmRfInLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRfInLowLevel.setStatus("current")


class _SfdSetAlarmRfInLowWarningDelay_Type(Integer32):
    """Custom type sfdSetAlarmRfInLowWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 599),
    )


_SfdSetAlarmRfInLowWarningDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRfInLowWarningDelay_Object = MibScalar
sfdSetAlarmRfInLowWarningDelay = _SfdSetAlarmRfInLowWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 1, 3),
    _SfdSetAlarmRfInLowWarningDelay_Type()
)
sfdSetAlarmRfInLowWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRfInLowWarningDelay.setStatus("current")


class _SfdSetAlarmRfInLowAlarmDelay_Type(Integer32):
    """Custom type sfdSetAlarmRfInLowAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfdSetAlarmRfInLowAlarmDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRfInLowAlarmDelay_Object = MibScalar
sfdSetAlarmRfInLowAlarmDelay = _SfdSetAlarmRfInLowAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 1, 4),
    _SfdSetAlarmRfInLowAlarmDelay_Type()
)
sfdSetAlarmRfInLowAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRfInLowAlarmDelay.setStatus("current")
_SfdSetAlarmRfInHigh_ObjectIdentity = ObjectIdentity
sfdSetAlarmRfInHigh = _SfdSetAlarmRfInHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 2)
)
_SfdSetAlarmRfInHighMode_Type = AlarmModes
_SfdSetAlarmRfInHighMode_Object = MibScalar
sfdSetAlarmRfInHighMode = _SfdSetAlarmRfInHighMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 2, 1),
    _SfdSetAlarmRfInHighMode_Type()
)
sfdSetAlarmRfInHighMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRfInHighMode.setStatus("current")


class _SfdSetAlarmRfInHighLevel_Type(Integer32):
    """Custom type sfdSetAlarmRfInHighLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SfdSetAlarmRfInHighLevel_Type.__name__ = "Integer32"
_SfdSetAlarmRfInHighLevel_Object = MibScalar
sfdSetAlarmRfInHighLevel = _SfdSetAlarmRfInHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 2, 2),
    _SfdSetAlarmRfInHighLevel_Type()
)
sfdSetAlarmRfInHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRfInHighLevel.setStatus("current")


class _SfdSetAlarmRfInHighWarningDelay_Type(Integer32):
    """Custom type sfdSetAlarmRfInHighWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 599),
    )


_SfdSetAlarmRfInHighWarningDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRfInHighWarningDelay_Object = MibScalar
sfdSetAlarmRfInHighWarningDelay = _SfdSetAlarmRfInHighWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 2, 3),
    _SfdSetAlarmRfInHighWarningDelay_Type()
)
sfdSetAlarmRfInHighWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRfInHighWarningDelay.setStatus("current")


class _SfdSetAlarmRfInHighAlarmDelay_Type(Integer32):
    """Custom type sfdSetAlarmRfInHighAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfdSetAlarmRfInHighAlarmDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRfInHighAlarmDelay_Object = MibScalar
sfdSetAlarmRfInHighAlarmDelay = _SfdSetAlarmRfInHighAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 1, 2, 4),
    _SfdSetAlarmRfInHighAlarmDelay_Type()
)
sfdSetAlarmRfInHighAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRfInHighAlarmDelay.setStatus("current")
_SfdSetAlarmPilot_ObjectIdentity = ObjectIdentity
sfdSetAlarmPilot = _SfdSetAlarmPilot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 2)
)
_SfdSetAlarmPilotMode_Type = AlarmModes
_SfdSetAlarmPilotMode_Object = MibScalar
sfdSetAlarmPilotMode = _SfdSetAlarmPilotMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 2, 1),
    _SfdSetAlarmPilotMode_Type()
)
sfdSetAlarmPilotMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmPilotMode.setStatus("current")


class _SfdSetAlarmPilotLevelKhz_Type(Integer32):
    """Custom type sfdSetAlarmPilotLevelKhz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_SfdSetAlarmPilotLevelKhz_Type.__name__ = "Integer32"
_SfdSetAlarmPilotLevelKhz_Object = MibScalar
sfdSetAlarmPilotLevelKhz = _SfdSetAlarmPilotLevelKhz_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 2, 2),
    _SfdSetAlarmPilotLevelKhz_Type()
)
sfdSetAlarmPilotLevelKhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmPilotLevelKhz.setStatus("current")


class _SfdSetAlarmPilotWarningDelay_Type(Integer32):
    """Custom type sfdSetAlarmPilotWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 599),
    )


_SfdSetAlarmPilotWarningDelay_Type.__name__ = "Integer32"
_SfdSetAlarmPilotWarningDelay_Object = MibScalar
sfdSetAlarmPilotWarningDelay = _SfdSetAlarmPilotWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 2, 3),
    _SfdSetAlarmPilotWarningDelay_Type()
)
sfdSetAlarmPilotWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmPilotWarningDelay.setStatus("current")


class _SfdSetAlarmPilotAlarmDelay_Type(Integer32):
    """Custom type sfdSetAlarmPilotAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfdSetAlarmPilotAlarmDelay_Type.__name__ = "Integer32"
_SfdSetAlarmPilotAlarmDelay_Object = MibScalar
sfdSetAlarmPilotAlarmDelay = _SfdSetAlarmPilotAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 2, 4),
    _SfdSetAlarmPilotAlarmDelay_Type()
)
sfdSetAlarmPilotAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmPilotAlarmDelay.setStatus("current")


class _SfdSetAlarmPilotLevelDbu_Type(Integer32):
    """Custom type sfdSetAlarmPilotLevelDbu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, -25),
    )


_SfdSetAlarmPilotLevelDbu_Type.__name__ = "Integer32"
_SfdSetAlarmPilotLevelDbu_Object = MibScalar
sfdSetAlarmPilotLevelDbu = _SfdSetAlarmPilotLevelDbu_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 2, 5),
    _SfdSetAlarmPilotLevelDbu_Type()
)
sfdSetAlarmPilotLevelDbu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmPilotLevelDbu.setStatus("current")
_SfdSetAlarmRds_ObjectIdentity = ObjectIdentity
sfdSetAlarmRds = _SfdSetAlarmRds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3)
)
_SfdSetAlarmRdsLevel_ObjectIdentity = ObjectIdentity
sfdSetAlarmRdsLevel = _SfdSetAlarmRdsLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 1)
)
_SfdSetAlarmRdsLevelMode_Type = AlarmModes
_SfdSetAlarmRdsLevelMode_Object = MibScalar
sfdSetAlarmRdsLevelMode = _SfdSetAlarmRdsLevelMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 1, 1),
    _SfdSetAlarmRdsLevelMode_Type()
)
sfdSetAlarmRdsLevelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsLevelMode.setStatus("current")


class _SfdSetAlarmRdsLevelLevelKhz_Type(Integer32):
    """Custom type sfdSetAlarmRdsLevelLevelKhz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SfdSetAlarmRdsLevelLevelKhz_Type.__name__ = "Integer32"
_SfdSetAlarmRdsLevelLevelKhz_Object = MibScalar
sfdSetAlarmRdsLevelLevelKhz = _SfdSetAlarmRdsLevelLevelKhz_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 1, 2),
    _SfdSetAlarmRdsLevelLevelKhz_Type()
)
sfdSetAlarmRdsLevelLevelKhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsLevelLevelKhz.setStatus("current")


class _SfdSetAlarmRdsLevelWarningDelay_Type(Integer32):
    """Custom type sfdSetAlarmRdsLevelWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 599),
    )


_SfdSetAlarmRdsLevelWarningDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRdsLevelWarningDelay_Object = MibScalar
sfdSetAlarmRdsLevelWarningDelay = _SfdSetAlarmRdsLevelWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 1, 3),
    _SfdSetAlarmRdsLevelWarningDelay_Type()
)
sfdSetAlarmRdsLevelWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsLevelWarningDelay.setStatus("current")


class _SfdSetAlarmRdsLevelAlarmDelay_Type(Integer32):
    """Custom type sfdSetAlarmRdsLevelAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfdSetAlarmRdsLevelAlarmDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRdsLevelAlarmDelay_Object = MibScalar
sfdSetAlarmRdsLevelAlarmDelay = _SfdSetAlarmRdsLevelAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 1, 4),
    _SfdSetAlarmRdsLevelAlarmDelay_Type()
)
sfdSetAlarmRdsLevelAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsLevelAlarmDelay.setStatus("current")


class _SfdSetAlarmRdsLevelLevelDbu_Type(Integer32):
    """Custom type sfdSetAlarmRdsLevelLevelDbu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, -105),
    )


_SfdSetAlarmRdsLevelLevelDbu_Type.__name__ = "Integer32"
_SfdSetAlarmRdsLevelLevelDbu_Object = MibScalar
sfdSetAlarmRdsLevelLevelDbu = _SfdSetAlarmRdsLevelLevelDbu_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 1, 5),
    _SfdSetAlarmRdsLevelLevelDbu_Type()
)
sfdSetAlarmRdsLevelLevelDbu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsLevelLevelDbu.setStatus("current")
_SfdSetAlarmRdsBer_ObjectIdentity = ObjectIdentity
sfdSetAlarmRdsBer = _SfdSetAlarmRdsBer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 2)
)
_SfdSetAlarmRdsBerMode_Type = AlarmModes
_SfdSetAlarmRdsBerMode_Object = MibScalar
sfdSetAlarmRdsBerMode = _SfdSetAlarmRdsBerMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 2, 1),
    _SfdSetAlarmRdsBerMode_Type()
)
sfdSetAlarmRdsBerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsBerMode.setStatus("current")


class _SfdSetAlarmRdsBerLevel_Type(Integer32):
    """Custom type sfdSetAlarmRdsBerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SfdSetAlarmRdsBerLevel_Type.__name__ = "Integer32"
_SfdSetAlarmRdsBerLevel_Object = MibScalar
sfdSetAlarmRdsBerLevel = _SfdSetAlarmRdsBerLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 2, 2),
    _SfdSetAlarmRdsBerLevel_Type()
)
sfdSetAlarmRdsBerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsBerLevel.setStatus("current")


class _SfdSetAlarmRdsBerWarningDelay_Type(Integer32):
    """Custom type sfdSetAlarmRdsBerWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 599),
    )


_SfdSetAlarmRdsBerWarningDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRdsBerWarningDelay_Object = MibScalar
sfdSetAlarmRdsBerWarningDelay = _SfdSetAlarmRdsBerWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 2, 3),
    _SfdSetAlarmRdsBerWarningDelay_Type()
)
sfdSetAlarmRdsBerWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsBerWarningDelay.setStatus("current")


class _SfdSetAlarmRdsBerAlarmDelay_Type(Integer32):
    """Custom type sfdSetAlarmRdsBerAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfdSetAlarmRdsBerAlarmDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRdsBerAlarmDelay_Object = MibScalar
sfdSetAlarmRdsBerAlarmDelay = _SfdSetAlarmRdsBerAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 2, 4),
    _SfdSetAlarmRdsBerAlarmDelay_Type()
)
sfdSetAlarmRdsBerAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsBerAlarmDelay.setStatus("current")
_SfdSetAlarmRdsPi_ObjectIdentity = ObjectIdentity
sfdSetAlarmRdsPi = _SfdSetAlarmRdsPi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 3)
)
_SfdSetAlarmRdsPiMode_Type = AlarmModes
_SfdSetAlarmRdsPiMode_Object = MibScalar
sfdSetAlarmRdsPiMode = _SfdSetAlarmRdsPiMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 3, 1),
    _SfdSetAlarmRdsPiMode_Type()
)
sfdSetAlarmRdsPiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsPiMode.setStatus("current")


class _SfdSetAlarmRdsPiPi_Type(Integer32):
    """Custom type sfdSetAlarmRdsPiPi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfdSetAlarmRdsPiPi_Type.__name__ = "Integer32"
_SfdSetAlarmRdsPiPi_Object = MibScalar
sfdSetAlarmRdsPiPi = _SfdSetAlarmRdsPiPi_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 3, 2),
    _SfdSetAlarmRdsPiPi_Type()
)
sfdSetAlarmRdsPiPi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsPiPi.setStatus("current")


class _SfdSetAlarmRdsPiWarningDelay_Type(Integer32):
    """Custom type sfdSetAlarmRdsPiWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 599),
    )


_SfdSetAlarmRdsPiWarningDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRdsPiWarningDelay_Object = MibScalar
sfdSetAlarmRdsPiWarningDelay = _SfdSetAlarmRdsPiWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 3, 3),
    _SfdSetAlarmRdsPiWarningDelay_Type()
)
sfdSetAlarmRdsPiWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsPiWarningDelay.setStatus("current")


class _SfdSetAlarmRdsPiAlarmDelay_Type(Integer32):
    """Custom type sfdSetAlarmRdsPiAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfdSetAlarmRdsPiAlarmDelay_Type.__name__ = "Integer32"
_SfdSetAlarmRdsPiAlarmDelay_Object = MibScalar
sfdSetAlarmRdsPiAlarmDelay = _SfdSetAlarmRdsPiAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 3, 3, 4),
    _SfdSetAlarmRdsPiAlarmDelay_Type()
)
sfdSetAlarmRdsPiAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmRdsPiAlarmDelay.setStatus("current")
_SfdSetAlarmMpxDeviation_ObjectIdentity = ObjectIdentity
sfdSetAlarmMpxDeviation = _SfdSetAlarmMpxDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 4)
)
_SfdSetAlarmMpxDeviationMode_Type = AlarmModes
_SfdSetAlarmMpxDeviationMode_Object = MibScalar
sfdSetAlarmMpxDeviationMode = _SfdSetAlarmMpxDeviationMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 4, 1),
    _SfdSetAlarmMpxDeviationMode_Type()
)
sfdSetAlarmMpxDeviationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmMpxDeviationMode.setStatus("current")


class _SfdSetAlarmMpxDeviationLevel_Type(Integer32):
    """Custom type sfdSetAlarmMpxDeviationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 159),
    )


_SfdSetAlarmMpxDeviationLevel_Type.__name__ = "Integer32"
_SfdSetAlarmMpxDeviationLevel_Object = MibScalar
sfdSetAlarmMpxDeviationLevel = _SfdSetAlarmMpxDeviationLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 4, 2),
    _SfdSetAlarmMpxDeviationLevel_Type()
)
sfdSetAlarmMpxDeviationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmMpxDeviationLevel.setStatus("current")


class _SfdSetAlarmMpxDeviationOffDelay_Type(Integer32):
    """Custom type sfdSetAlarmMpxDeviationOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_SfdSetAlarmMpxDeviationOffDelay_Type.__name__ = "Integer32"
_SfdSetAlarmMpxDeviationOffDelay_Object = MibScalar
sfdSetAlarmMpxDeviationOffDelay = _SfdSetAlarmMpxDeviationOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 4, 3),
    _SfdSetAlarmMpxDeviationOffDelay_Type()
)
sfdSetAlarmMpxDeviationOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmMpxDeviationOffDelay.setStatus("current")
_SfdSetAlarmAudio_ObjectIdentity = ObjectIdentity
sfdSetAlarmAudio = _SfdSetAlarmAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5)
)
_SfdSetAlarmAudioLeft_ObjectIdentity = ObjectIdentity
sfdSetAlarmAudioLeft = _SfdSetAlarmAudioLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 1)
)
_SfdSetAlarmAudioLeftMode_Type = AlarmModes
_SfdSetAlarmAudioLeftMode_Object = MibScalar
sfdSetAlarmAudioLeftMode = _SfdSetAlarmAudioLeftMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 1, 1),
    _SfdSetAlarmAudioLeftMode_Type()
)
sfdSetAlarmAudioLeftMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioLeftMode.setStatus("current")


class _SfdSetAlarmAudioLeftLevel_Type(Integer32):
    """Custom type sfdSetAlarmAudioLeftLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 6),
    )


_SfdSetAlarmAudioLeftLevel_Type.__name__ = "Integer32"
_SfdSetAlarmAudioLeftLevel_Object = MibScalar
sfdSetAlarmAudioLeftLevel = _SfdSetAlarmAudioLeftLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 1, 2),
    _SfdSetAlarmAudioLeftLevel_Type()
)
sfdSetAlarmAudioLeftLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioLeftLevel.setStatus("current")


class _SfdSetAlarmAudioLeftWarningDelay_Type(Integer32):
    """Custom type sfdSetAlarmAudioLeftWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 599),
    )


_SfdSetAlarmAudioLeftWarningDelay_Type.__name__ = "Integer32"
_SfdSetAlarmAudioLeftWarningDelay_Object = MibScalar
sfdSetAlarmAudioLeftWarningDelay = _SfdSetAlarmAudioLeftWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 1, 3),
    _SfdSetAlarmAudioLeftWarningDelay_Type()
)
sfdSetAlarmAudioLeftWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioLeftWarningDelay.setStatus("current")


class _SfdSetAlarmAudioLeftAlarmDelay_Type(Integer32):
    """Custom type sfdSetAlarmAudioLeftAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfdSetAlarmAudioLeftAlarmDelay_Type.__name__ = "Integer32"
_SfdSetAlarmAudioLeftAlarmDelay_Object = MibScalar
sfdSetAlarmAudioLeftAlarmDelay = _SfdSetAlarmAudioLeftAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 1, 4),
    _SfdSetAlarmAudioLeftAlarmDelay_Type()
)
sfdSetAlarmAudioLeftAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioLeftAlarmDelay.setStatus("current")
_SfdSetAlarmAudioRight_ObjectIdentity = ObjectIdentity
sfdSetAlarmAudioRight = _SfdSetAlarmAudioRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 2)
)
_SfdSetAlarmAudioRightMode_Type = AlarmModes
_SfdSetAlarmAudioRightMode_Object = MibScalar
sfdSetAlarmAudioRightMode = _SfdSetAlarmAudioRightMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 2, 1),
    _SfdSetAlarmAudioRightMode_Type()
)
sfdSetAlarmAudioRightMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioRightMode.setStatus("current")


class _SfdSetAlarmAudioRightLevel_Type(Integer32):
    """Custom type sfdSetAlarmAudioRightLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 6),
    )


_SfdSetAlarmAudioRightLevel_Type.__name__ = "Integer32"
_SfdSetAlarmAudioRightLevel_Object = MibScalar
sfdSetAlarmAudioRightLevel = _SfdSetAlarmAudioRightLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 2, 2),
    _SfdSetAlarmAudioRightLevel_Type()
)
sfdSetAlarmAudioRightLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioRightLevel.setStatus("current")


class _SfdSetAlarmAudioRightWarningDelay_Type(Integer32):
    """Custom type sfdSetAlarmAudioRightWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 599),
    )


_SfdSetAlarmAudioRightWarningDelay_Type.__name__ = "Integer32"
_SfdSetAlarmAudioRightWarningDelay_Object = MibScalar
sfdSetAlarmAudioRightWarningDelay = _SfdSetAlarmAudioRightWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 2, 3),
    _SfdSetAlarmAudioRightWarningDelay_Type()
)
sfdSetAlarmAudioRightWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioRightWarningDelay.setStatus("current")


class _SfdSetAlarmAudioRightAlarmDelay_Type(Integer32):
    """Custom type sfdSetAlarmAudioRightAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfdSetAlarmAudioRightAlarmDelay_Type.__name__ = "Integer32"
_SfdSetAlarmAudioRightAlarmDelay_Object = MibScalar
sfdSetAlarmAudioRightAlarmDelay = _SfdSetAlarmAudioRightAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 2, 4),
    _SfdSetAlarmAudioRightAlarmDelay_Type()
)
sfdSetAlarmAudioRightAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioRightAlarmDelay.setStatus("current")
_SfdSetAlarmAudioBoth_ObjectIdentity = ObjectIdentity
sfdSetAlarmAudioBoth = _SfdSetAlarmAudioBoth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 3)
)
_SfdSetAlarmAudioBothMode_Type = AlarmModes
_SfdSetAlarmAudioBothMode_Object = MibScalar
sfdSetAlarmAudioBothMode = _SfdSetAlarmAudioBothMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 3, 1),
    _SfdSetAlarmAudioBothMode_Type()
)
sfdSetAlarmAudioBothMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioBothMode.setStatus("current")


class _SfdSetAlarmAudioBothLevel_Type(Integer32):
    """Custom type sfdSetAlarmAudioBothLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 6),
    )


_SfdSetAlarmAudioBothLevel_Type.__name__ = "Integer32"
_SfdSetAlarmAudioBothLevel_Object = MibScalar
sfdSetAlarmAudioBothLevel = _SfdSetAlarmAudioBothLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 3, 2),
    _SfdSetAlarmAudioBothLevel_Type()
)
sfdSetAlarmAudioBothLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioBothLevel.setStatus("current")


class _SfdSetAlarmAudioBothWarningDelay_Type(Integer32):
    """Custom type sfdSetAlarmAudioBothWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 599),
    )


_SfdSetAlarmAudioBothWarningDelay_Type.__name__ = "Integer32"
_SfdSetAlarmAudioBothWarningDelay_Object = MibScalar
sfdSetAlarmAudioBothWarningDelay = _SfdSetAlarmAudioBothWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 3, 3),
    _SfdSetAlarmAudioBothWarningDelay_Type()
)
sfdSetAlarmAudioBothWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioBothWarningDelay.setStatus("current")


class _SfdSetAlarmAudioBothAlarmDelay_Type(Integer32):
    """Custom type sfdSetAlarmAudioBothAlarmDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SfdSetAlarmAudioBothAlarmDelay_Type.__name__ = "Integer32"
_SfdSetAlarmAudioBothAlarmDelay_Object = MibScalar
sfdSetAlarmAudioBothAlarmDelay = _SfdSetAlarmAudioBothAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 8, 5, 3, 4),
    _SfdSetAlarmAudioBothAlarmDelay_Type()
)
sfdSetAlarmAudioBothAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetAlarmAudioBothAlarmDelay.setStatus("current")
_SfdSetControlIO_ObjectIdentity = ObjectIdentity
sfdSetControlIO = _SfdSetControlIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9)
)
_SfdSetControlIOInput_ObjectIdentity = ObjectIdentity
sfdSetControlIOInput = _SfdSetControlIOInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 1)
)
_SfdSetControlIOInput0_Type = InputModes
_SfdSetControlIOInput0_Object = MibScalar
sfdSetControlIOInput0 = _SfdSetControlIOInput0_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 1, 1),
    _SfdSetControlIOInput0_Type()
)
sfdSetControlIOInput0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetControlIOInput0.setStatus("current")
_SfdSetControlIOInput1_Type = InputModes
_SfdSetControlIOInput1_Object = MibScalar
sfdSetControlIOInput1 = _SfdSetControlIOInput1_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 1, 2),
    _SfdSetControlIOInput1_Type()
)
sfdSetControlIOInput1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetControlIOInput1.setStatus("current")
_SfdSetControlIOInput2_Type = InputModes
_SfdSetControlIOInput2_Object = MibScalar
sfdSetControlIOInput2 = _SfdSetControlIOInput2_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 1, 3),
    _SfdSetControlIOInput2_Type()
)
sfdSetControlIOInput2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetControlIOInput2.setStatus("current")
_SfdSetControlIOInput3_Type = InputModes
_SfdSetControlIOInput3_Object = MibScalar
sfdSetControlIOInput3 = _SfdSetControlIOInput3_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 1, 4),
    _SfdSetControlIOInput3_Type()
)
sfdSetControlIOInput3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetControlIOInput3.setStatus("current")
_SfdSetControlIOOutput_ObjectIdentity = ObjectIdentity
sfdSetControlIOOutput = _SfdSetControlIOOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 2)
)
_SfdSetControlIOOutput0_Type = OutputModes
_SfdSetControlIOOutput0_Object = MibScalar
sfdSetControlIOOutput0 = _SfdSetControlIOOutput0_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 2, 1),
    _SfdSetControlIOOutput0_Type()
)
sfdSetControlIOOutput0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetControlIOOutput0.setStatus("current")
_SfdSetControlIOOutput1_Type = OutputModes
_SfdSetControlIOOutput1_Object = MibScalar
sfdSetControlIOOutput1 = _SfdSetControlIOOutput1_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 2, 2),
    _SfdSetControlIOOutput1_Type()
)
sfdSetControlIOOutput1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetControlIOOutput1.setStatus("current")
_SfdSetControlIOOutput2_Type = OutputModes
_SfdSetControlIOOutput2_Object = MibScalar
sfdSetControlIOOutput2 = _SfdSetControlIOOutput2_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 2, 3),
    _SfdSetControlIOOutput2_Type()
)
sfdSetControlIOOutput2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetControlIOOutput2.setStatus("current")
_SfdSetControlIOOutput3_Type = OutputModes
_SfdSetControlIOOutput3_Object = MibScalar
sfdSetControlIOOutput3 = _SfdSetControlIOOutput3_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 9, 2, 4),
    _SfdSetControlIOOutput3_Type()
)
sfdSetControlIOOutput3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetControlIOOutput3.setStatus("current")
_SfdSetNotification_ObjectIdentity = ObjectIdentity
sfdSetNotification = _SfdSetNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10)
)
_SfdSetNotificationMode_ObjectIdentity = ObjectIdentity
sfdSetNotificationMode = _SfdSetNotificationMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 1)
)
_SfdSetNotificationModeAll_Type = NotificationOffOn
_SfdSetNotificationModeAll_Object = MibScalar
sfdSetNotificationModeAll = _SfdSetNotificationModeAll_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 1, 1),
    _SfdSetNotificationModeAll_Type()
)
sfdSetNotificationModeAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAll.setStatus("current")
_SfdSetNotificationModeHeartbeat_Type = NotificationOffOn
_SfdSetNotificationModeHeartbeat_Object = MibScalar
sfdSetNotificationModeHeartbeat = _SfdSetNotificationModeHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 1, 2),
    _SfdSetNotificationModeHeartbeat_Type()
)
sfdSetNotificationModeHeartbeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeHeartbeat.setStatus("current")
_SfdSetNotificationModeSettingChanged_Type = NotificationOffOn
_SfdSetNotificationModeSettingChanged_Object = MibScalar
sfdSetNotificationModeSettingChanged = _SfdSetNotificationModeSettingChanged_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 1, 3),
    _SfdSetNotificationModeSettingChanged_Type()
)
sfdSetNotificationModeSettingChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeSettingChanged.setStatus("current")
_SfdSetNotificationModeControlMode_Type = NotificationOffOn
_SfdSetNotificationModeControlMode_Object = MibScalar
sfdSetNotificationModeControlMode = _SfdSetNotificationModeControlMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 1, 4),
    _SfdSetNotificationModeControlMode_Type()
)
sfdSetNotificationModeControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeControlMode.setStatus("current")
_SfdSetNotificationModeControlModeLocalSuppress_Type = NotificationOffOn
_SfdSetNotificationModeControlModeLocalSuppress_Object = MibScalar
sfdSetNotificationModeControlModeLocalSuppress = _SfdSetNotificationModeControlModeLocalSuppress_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 1, 5),
    _SfdSetNotificationModeControlModeLocalSuppress_Type()
)
sfdSetNotificationModeControlModeLocalSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeControlModeLocalSuppress.setStatus("current")
_SfdSetNotificationModeAlarm_ObjectIdentity = ObjectIdentity
sfdSetNotificationModeAlarm = _SfdSetNotificationModeAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2)
)
_SfdSetNotificationModeAlarmRfInLevelLow_Type = NotificationModes
_SfdSetNotificationModeAlarmRfInLevelLow_Object = MibScalar
sfdSetNotificationModeAlarmRfInLevelLow = _SfdSetNotificationModeAlarmRfInLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 1),
    _SfdSetNotificationModeAlarmRfInLevelLow_Type()
)
sfdSetNotificationModeAlarmRfInLevelLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmRfInLevelLow.setStatus("current")
_SfdSetNotificationModeAlarmRfInLevelHigh_Type = NotificationModes
_SfdSetNotificationModeAlarmRfInLevelHigh_Object = MibScalar
sfdSetNotificationModeAlarmRfInLevelHigh = _SfdSetNotificationModeAlarmRfInLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 2),
    _SfdSetNotificationModeAlarmRfInLevelHigh_Type()
)
sfdSetNotificationModeAlarmRfInLevelHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmRfInLevelHigh.setStatus("current")
_SfdSetNotificationModeAlarmPilotLevel_Type = NotificationModes
_SfdSetNotificationModeAlarmPilotLevel_Object = MibScalar
sfdSetNotificationModeAlarmPilotLevel = _SfdSetNotificationModeAlarmPilotLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 3),
    _SfdSetNotificationModeAlarmPilotLevel_Type()
)
sfdSetNotificationModeAlarmPilotLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmPilotLevel.setStatus("current")
_SfdSetNotificationModeAlarmMpxDeviation_Type = NotificationModes
_SfdSetNotificationModeAlarmMpxDeviation_Object = MibScalar
sfdSetNotificationModeAlarmMpxDeviation = _SfdSetNotificationModeAlarmMpxDeviation_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 4),
    _SfdSetNotificationModeAlarmMpxDeviation_Type()
)
sfdSetNotificationModeAlarmMpxDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmMpxDeviation.setStatus("current")
_SfdSetNotificationModeAlarmRdsBer_Type = NotificationModes
_SfdSetNotificationModeAlarmRdsBer_Object = MibScalar
sfdSetNotificationModeAlarmRdsBer = _SfdSetNotificationModeAlarmRdsBer_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 5),
    _SfdSetNotificationModeAlarmRdsBer_Type()
)
sfdSetNotificationModeAlarmRdsBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmRdsBer.setStatus("current")
_SfdSetNotificationModeAlarmRdsLevel_Type = NotificationModes
_SfdSetNotificationModeAlarmRdsLevel_Object = MibScalar
sfdSetNotificationModeAlarmRdsLevel = _SfdSetNotificationModeAlarmRdsLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 6),
    _SfdSetNotificationModeAlarmRdsLevel_Type()
)
sfdSetNotificationModeAlarmRdsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmRdsLevel.setStatus("current")
_SfdSetNotificationModeAlarmAudioLevelLeft_Type = NotificationModes
_SfdSetNotificationModeAlarmAudioLevelLeft_Object = MibScalar
sfdSetNotificationModeAlarmAudioLevelLeft = _SfdSetNotificationModeAlarmAudioLevelLeft_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 7),
    _SfdSetNotificationModeAlarmAudioLevelLeft_Type()
)
sfdSetNotificationModeAlarmAudioLevelLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmAudioLevelLeft.setStatus("current")
_SfdSetNotificationModeAlarmAudioLevelRight_Type = NotificationModes
_SfdSetNotificationModeAlarmAudioLevelRight_Object = MibScalar
sfdSetNotificationModeAlarmAudioLevelRight = _SfdSetNotificationModeAlarmAudioLevelRight_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 8),
    _SfdSetNotificationModeAlarmAudioLevelRight_Type()
)
sfdSetNotificationModeAlarmAudioLevelRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmAudioLevelRight.setStatus("current")
_SfdSetNotificationModeAlarmAudioLevelBoth_Type = NotificationModes
_SfdSetNotificationModeAlarmAudioLevelBoth_Object = MibScalar
sfdSetNotificationModeAlarmAudioLevelBoth = _SfdSetNotificationModeAlarmAudioLevelBoth_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 9),
    _SfdSetNotificationModeAlarmAudioLevelBoth_Type()
)
sfdSetNotificationModeAlarmAudioLevelBoth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmAudioLevelBoth.setStatus("current")
_SfdSetNotificationModeAlarmRdsPi_Type = NotificationModes
_SfdSetNotificationModeAlarmRdsPi_Object = MibScalar
sfdSetNotificationModeAlarmRdsPi = _SfdSetNotificationModeAlarmRdsPi_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 2, 10),
    _SfdSetNotificationModeAlarmRdsPi_Type()
)
sfdSetNotificationModeAlarmRdsPi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeAlarmRdsPi.setStatus("current")
_SfdSetNotificationPriority_ObjectIdentity = ObjectIdentity
sfdSetNotificationPriority = _SfdSetNotificationPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3)
)
_SfdSetNotificationPriorityHeartbeat_Type = Gauge32
_SfdSetNotificationPriorityHeartbeat_Object = MibScalar
sfdSetNotificationPriorityHeartbeat = _SfdSetNotificationPriorityHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 1),
    _SfdSetNotificationPriorityHeartbeat_Type()
)
sfdSetNotificationPriorityHeartbeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityHeartbeat.setStatus("current")
_SfdSetNotificationPrioritySettingChanged_Type = Gauge32
_SfdSetNotificationPrioritySettingChanged_Object = MibScalar
sfdSetNotificationPrioritySettingChanged = _SfdSetNotificationPrioritySettingChanged_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 2),
    _SfdSetNotificationPrioritySettingChanged_Type()
)
sfdSetNotificationPrioritySettingChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPrioritySettingChanged.setStatus("current")
_SfdSetNotificationPriorityControlMode_Type = Gauge32
_SfdSetNotificationPriorityControlMode_Object = MibScalar
sfdSetNotificationPriorityControlMode = _SfdSetNotificationPriorityControlMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 3),
    _SfdSetNotificationPriorityControlMode_Type()
)
sfdSetNotificationPriorityControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityControlMode.setStatus("current")
_SfdSetNotificationPriorityAlarmRfInLevelLow_Type = Gauge32
_SfdSetNotificationPriorityAlarmRfInLevelLow_Object = MibScalar
sfdSetNotificationPriorityAlarmRfInLevelLow = _SfdSetNotificationPriorityAlarmRfInLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 401),
    _SfdSetNotificationPriorityAlarmRfInLevelLow_Type()
)
sfdSetNotificationPriorityAlarmRfInLevelLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmRfInLevelLow.setStatus("current")
_SfdSetNotificationPriorityAlarmRfInLevelHigh_Type = Gauge32
_SfdSetNotificationPriorityAlarmRfInLevelHigh_Object = MibScalar
sfdSetNotificationPriorityAlarmRfInLevelHigh = _SfdSetNotificationPriorityAlarmRfInLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 402),
    _SfdSetNotificationPriorityAlarmRfInLevelHigh_Type()
)
sfdSetNotificationPriorityAlarmRfInLevelHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmRfInLevelHigh.setStatus("current")
_SfdSetNotificationPriorityAlarmPilotLevel_Type = Gauge32
_SfdSetNotificationPriorityAlarmPilotLevel_Object = MibScalar
sfdSetNotificationPriorityAlarmPilotLevel = _SfdSetNotificationPriorityAlarmPilotLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 403),
    _SfdSetNotificationPriorityAlarmPilotLevel_Type()
)
sfdSetNotificationPriorityAlarmPilotLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmPilotLevel.setStatus("current")
_SfdSetNotificationPriorityAlarmMpxDeviation_Type = Gauge32
_SfdSetNotificationPriorityAlarmMpxDeviation_Object = MibScalar
sfdSetNotificationPriorityAlarmMpxDeviation = _SfdSetNotificationPriorityAlarmMpxDeviation_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 404),
    _SfdSetNotificationPriorityAlarmMpxDeviation_Type()
)
sfdSetNotificationPriorityAlarmMpxDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmMpxDeviation.setStatus("current")
_SfdSetNotificationPriorityAlarmRdsBer_Type = Gauge32
_SfdSetNotificationPriorityAlarmRdsBer_Object = MibScalar
sfdSetNotificationPriorityAlarmRdsBer = _SfdSetNotificationPriorityAlarmRdsBer_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 405),
    _SfdSetNotificationPriorityAlarmRdsBer_Type()
)
sfdSetNotificationPriorityAlarmRdsBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmRdsBer.setStatus("current")
_SfdSetNotificationPriorityAlarmRdsLevel_Type = Gauge32
_SfdSetNotificationPriorityAlarmRdsLevel_Object = MibScalar
sfdSetNotificationPriorityAlarmRdsLevel = _SfdSetNotificationPriorityAlarmRdsLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 406),
    _SfdSetNotificationPriorityAlarmRdsLevel_Type()
)
sfdSetNotificationPriorityAlarmRdsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmRdsLevel.setStatus("current")
_SfdSetNotificationPriorityAlarmAudioLevelLeft_Type = Gauge32
_SfdSetNotificationPriorityAlarmAudioLevelLeft_Object = MibScalar
sfdSetNotificationPriorityAlarmAudioLevelLeft = _SfdSetNotificationPriorityAlarmAudioLevelLeft_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 407),
    _SfdSetNotificationPriorityAlarmAudioLevelLeft_Type()
)
sfdSetNotificationPriorityAlarmAudioLevelLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmAudioLevelLeft.setStatus("current")
_SfdSetNotificationPriorityAlarmAudioLevelRight_Type = Gauge32
_SfdSetNotificationPriorityAlarmAudioLevelRight_Object = MibScalar
sfdSetNotificationPriorityAlarmAudioLevelRight = _SfdSetNotificationPriorityAlarmAudioLevelRight_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 408),
    _SfdSetNotificationPriorityAlarmAudioLevelRight_Type()
)
sfdSetNotificationPriorityAlarmAudioLevelRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmAudioLevelRight.setStatus("current")
_SfdSetNotificationPriorityAlarmAudioLevelBoth_Type = Gauge32
_SfdSetNotificationPriorityAlarmAudioLevelBoth_Object = MibScalar
sfdSetNotificationPriorityAlarmAudioLevelBoth = _SfdSetNotificationPriorityAlarmAudioLevelBoth_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 409),
    _SfdSetNotificationPriorityAlarmAudioLevelBoth_Type()
)
sfdSetNotificationPriorityAlarmAudioLevelBoth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmAudioLevelBoth.setStatus("current")
_SfdSetNotificationPriorityAlarmRdsPi_Type = Gauge32
_SfdSetNotificationPriorityAlarmRdsPi_Object = MibScalar
sfdSetNotificationPriorityAlarmRdsPi = _SfdSetNotificationPriorityAlarmRdsPi_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 410),
    _SfdSetNotificationPriorityAlarmRdsPi_Type()
)
sfdSetNotificationPriorityAlarmRdsPi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityAlarmRdsPi.setStatus("current")
_SfdSetNotificationPriorityStatusRfInFrequency_Type = Gauge32
_SfdSetNotificationPriorityStatusRfInFrequency_Object = MibScalar
sfdSetNotificationPriorityStatusRfInFrequency = _SfdSetNotificationPriorityStatusRfInFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 451),
    _SfdSetNotificationPriorityStatusRfInFrequency_Type()
)
sfdSetNotificationPriorityStatusRfInFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityStatusRfInFrequency.setStatus("current")
_SfdSetNotificationPriorityStatusRfInInput_Type = Gauge32
_SfdSetNotificationPriorityStatusRfInInput_Object = MibScalar
sfdSetNotificationPriorityStatusRfInInput = _SfdSetNotificationPriorityStatusRfInInput_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 452),
    _SfdSetNotificationPriorityStatusRfInInput_Type()
)
sfdSetNotificationPriorityStatusRfInInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityStatusRfInInput.setStatus("current")
_SfdSetNotificationPriorityStatusRfInMuted_Type = Gauge32
_SfdSetNotificationPriorityStatusRfInMuted_Object = MibScalar
sfdSetNotificationPriorityStatusRfInMuted = _SfdSetNotificationPriorityStatusRfInMuted_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 453),
    _SfdSetNotificationPriorityStatusRfInMuted_Type()
)
sfdSetNotificationPriorityStatusRfInMuted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityStatusRfInMuted.setStatus("current")
_SfdSetNotificationPriorityStatusRfInFilter_Type = Gauge32
_SfdSetNotificationPriorityStatusRfInFilter_Object = MibScalar
sfdSetNotificationPriorityStatusRfInFilter = _SfdSetNotificationPriorityStatusRfInFilter_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 454),
    _SfdSetNotificationPriorityStatusRfInFilter_Type()
)
sfdSetNotificationPriorityStatusRfInFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityStatusRfInFilter.setStatus("current")
_SfdSetNotificationPriorityStatusMpxSource_Type = Gauge32
_SfdSetNotificationPriorityStatusMpxSource_Object = MibScalar
sfdSetNotificationPriorityStatusMpxSource = _SfdSetNotificationPriorityStatusMpxSource_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 455),
    _SfdSetNotificationPriorityStatusMpxSource_Type()
)
sfdSetNotificationPriorityStatusMpxSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityStatusMpxSource.setStatus("current")
_SfdSetNotificationPriorityStatusAudioTestTone_Type = Gauge32
_SfdSetNotificationPriorityStatusAudioTestTone_Object = MibScalar
sfdSetNotificationPriorityStatusAudioTestTone = _SfdSetNotificationPriorityStatusAudioTestTone_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 456),
    _SfdSetNotificationPriorityStatusAudioTestTone_Type()
)
sfdSetNotificationPriorityStatusAudioTestTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityStatusAudioTestTone.setStatus("current")
_SfdSetNotificationPriorityStatusAudioDeEmphase_Type = Gauge32
_SfdSetNotificationPriorityStatusAudioDeEmphase_Object = MibScalar
sfdSetNotificationPriorityStatusAudioDeEmphase = _SfdSetNotificationPriorityStatusAudioDeEmphase_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 3, 457),
    _SfdSetNotificationPriorityStatusAudioDeEmphase_Type()
)
sfdSetNotificationPriorityStatusAudioDeEmphase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationPriorityStatusAudioDeEmphase.setStatus("current")
_SfdSetNotificationModeStatus_ObjectIdentity = ObjectIdentity
sfdSetNotificationModeStatus = _SfdSetNotificationModeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 4)
)
_SfdSetNotificationModeStatusRfInFrequency_Type = NotificationOffOn
_SfdSetNotificationModeStatusRfInFrequency_Object = MibScalar
sfdSetNotificationModeStatusRfInFrequency = _SfdSetNotificationModeStatusRfInFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 4, 1),
    _SfdSetNotificationModeStatusRfInFrequency_Type()
)
sfdSetNotificationModeStatusRfInFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeStatusRfInFrequency.setStatus("current")
_SfdSetNotificationModeStatusRfInInput_Type = NotificationOffOn
_SfdSetNotificationModeStatusRfInInput_Object = MibScalar
sfdSetNotificationModeStatusRfInInput = _SfdSetNotificationModeStatusRfInInput_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 4, 2),
    _SfdSetNotificationModeStatusRfInInput_Type()
)
sfdSetNotificationModeStatusRfInInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeStatusRfInInput.setStatus("current")
_SfdSetNotificationModeStatusRfInMuted_Type = NotificationOffOn
_SfdSetNotificationModeStatusRfInMuted_Object = MibScalar
sfdSetNotificationModeStatusRfInMuted = _SfdSetNotificationModeStatusRfInMuted_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 4, 3),
    _SfdSetNotificationModeStatusRfInMuted_Type()
)
sfdSetNotificationModeStatusRfInMuted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeStatusRfInMuted.setStatus("current")
_SfdSetNotificationModeStatusRfInFilter_Type = NotificationOffOn
_SfdSetNotificationModeStatusRfInFilter_Object = MibScalar
sfdSetNotificationModeStatusRfInFilter = _SfdSetNotificationModeStatusRfInFilter_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 4, 4),
    _SfdSetNotificationModeStatusRfInFilter_Type()
)
sfdSetNotificationModeStatusRfInFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeStatusRfInFilter.setStatus("current")
_SfdSetNotificationModeStatusMpxSource_Type = NotificationOffOn
_SfdSetNotificationModeStatusMpxSource_Object = MibScalar
sfdSetNotificationModeStatusMpxSource = _SfdSetNotificationModeStatusMpxSource_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 4, 5),
    _SfdSetNotificationModeStatusMpxSource_Type()
)
sfdSetNotificationModeStatusMpxSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeStatusMpxSource.setStatus("current")
_SfdSetNotificationModeStatusAudioTestTone_Type = NotificationOffOn
_SfdSetNotificationModeStatusAudioTestTone_Object = MibScalar
sfdSetNotificationModeStatusAudioTestTone = _SfdSetNotificationModeStatusAudioTestTone_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 4, 6),
    _SfdSetNotificationModeStatusAudioTestTone_Type()
)
sfdSetNotificationModeStatusAudioTestTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeStatusAudioTestTone.setStatus("current")
_SfdSetNotificationModeStatusAudioDeEmphase_Type = NotificationOffOn
_SfdSetNotificationModeStatusAudioDeEmphase_Object = MibScalar
sfdSetNotificationModeStatusAudioDeEmphase = _SfdSetNotificationModeStatusAudioDeEmphase_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 10, 4, 7),
    _SfdSetNotificationModeStatusAudioDeEmphase_Type()
)
sfdSetNotificationModeStatusAudioDeEmphase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetNotificationModeStatusAudioDeEmphase.setStatus("current")
_SfdSetPreset_ObjectIdentity = ObjectIdentity
sfdSetPreset = _SfdSetPreset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 11)
)


class _SfdSetPresetRecall_Type(Integer32):
    """Custom type sfdSetPresetRecall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SfdSetPresetRecall_Type.__name__ = "Integer32"
_SfdSetPresetRecall_Object = MibScalar
sfdSetPresetRecall = _SfdSetPresetRecall_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 11, 1),
    _SfdSetPresetRecall_Type()
)
sfdSetPresetRecall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetPresetRecall.setStatus("current")


class _SfdSetPresetSaveAs_Type(Integer32):
    """Custom type sfdSetPresetSaveAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SfdSetPresetSaveAs_Type.__name__ = "Integer32"
_SfdSetPresetSaveAs_Object = MibScalar
sfdSetPresetSaveAs = _SfdSetPresetSaveAs_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 11, 2),
    _SfdSetPresetSaveAs_Type()
)
sfdSetPresetSaveAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetPresetSaveAs.setStatus("current")


class _SfdSetPresetActiveDefaults_Type(Integer32):
    """Custom type sfdSetPresetActiveDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SfdSetPresetActiveDefaults_Type.__name__ = "Integer32"
_SfdSetPresetActiveDefaults_Object = MibScalar
sfdSetPresetActiveDefaults = _SfdSetPresetActiveDefaults_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 11, 3),
    _SfdSetPresetActiveDefaults_Type()
)
sfdSetPresetActiveDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetPresetActiveDefaults.setStatus("current")


class _SfdSetPresetActiveName_Type(OctetString):
    """Custom type sfdSetPresetActiveName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SfdSetPresetActiveName_Type.__name__ = "OctetString"
_SfdSetPresetActiveName_Object = MibScalar
sfdSetPresetActiveName = _SfdSetPresetActiveName_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 2, 11, 4),
    _SfdSetPresetActiveName_Type()
)
sfdSetPresetActiveName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfdSetPresetActiveName.setStatus("current")
_SfdMeasurements_ObjectIdentity = ObjectIdentity
sfdMeasurements = _SfdMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3)
)
_SfdMsrAlarm_ObjectIdentity = ObjectIdentity
sfdMsrAlarm = _SfdMsrAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1)
)
_SfdMsrAlarmRfInLevelLow_Type = AlarmStatus
_SfdMsrAlarmRfInLevelLow_Object = MibScalar
sfdMsrAlarmRfInLevelLow = _SfdMsrAlarmRfInLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 1),
    _SfdMsrAlarmRfInLevelLow_Type()
)
sfdMsrAlarmRfInLevelLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmRfInLevelLow.setStatus("current")
_SfdMsrAlarmRfInLevelHigh_Type = AlarmStatus
_SfdMsrAlarmRfInLevelHigh_Object = MibScalar
sfdMsrAlarmRfInLevelHigh = _SfdMsrAlarmRfInLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 2),
    _SfdMsrAlarmRfInLevelHigh_Type()
)
sfdMsrAlarmRfInLevelHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmRfInLevelHigh.setStatus("current")
_SfdMsrAlarmPilotLevel_Type = AlarmStatus
_SfdMsrAlarmPilotLevel_Object = MibScalar
sfdMsrAlarmPilotLevel = _SfdMsrAlarmPilotLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 3),
    _SfdMsrAlarmPilotLevel_Type()
)
sfdMsrAlarmPilotLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmPilotLevel.setStatus("current")
_SfdMsrAlarmMpxDeviation_Type = AlarmStatus
_SfdMsrAlarmMpxDeviation_Object = MibScalar
sfdMsrAlarmMpxDeviation = _SfdMsrAlarmMpxDeviation_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 4),
    _SfdMsrAlarmMpxDeviation_Type()
)
sfdMsrAlarmMpxDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmMpxDeviation.setStatus("current")
_SfdMsrAlarmRdsBer_Type = AlarmStatus
_SfdMsrAlarmRdsBer_Object = MibScalar
sfdMsrAlarmRdsBer = _SfdMsrAlarmRdsBer_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 5),
    _SfdMsrAlarmRdsBer_Type()
)
sfdMsrAlarmRdsBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmRdsBer.setStatus("current")
_SfdMsrAlarmRdsLevel_Type = AlarmStatus
_SfdMsrAlarmRdsLevel_Object = MibScalar
sfdMsrAlarmRdsLevel = _SfdMsrAlarmRdsLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 6),
    _SfdMsrAlarmRdsLevel_Type()
)
sfdMsrAlarmRdsLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmRdsLevel.setStatus("current")
_SfdMsrAlarmAudioLevelLeft_Type = AlarmStatus
_SfdMsrAlarmAudioLevelLeft_Object = MibScalar
sfdMsrAlarmAudioLevelLeft = _SfdMsrAlarmAudioLevelLeft_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 7),
    _SfdMsrAlarmAudioLevelLeft_Type()
)
sfdMsrAlarmAudioLevelLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmAudioLevelLeft.setStatus("current")
_SfdMsrAlarmAudioLevelRight_Type = AlarmStatus
_SfdMsrAlarmAudioLevelRight_Object = MibScalar
sfdMsrAlarmAudioLevelRight = _SfdMsrAlarmAudioLevelRight_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 8),
    _SfdMsrAlarmAudioLevelRight_Type()
)
sfdMsrAlarmAudioLevelRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmAudioLevelRight.setStatus("current")
_SfdMsrAlarmAudioLevelBoth_Type = AlarmStatus
_SfdMsrAlarmAudioLevelBoth_Object = MibScalar
sfdMsrAlarmAudioLevelBoth = _SfdMsrAlarmAudioLevelBoth_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 9),
    _SfdMsrAlarmAudioLevelBoth_Type()
)
sfdMsrAlarmAudioLevelBoth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmAudioLevelBoth.setStatus("current")
_SfdMsrAlarmRdsPi_Type = AlarmStatus
_SfdMsrAlarmRdsPi_Object = MibScalar
sfdMsrAlarmRdsPi = _SfdMsrAlarmRdsPi_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 1, 10),
    _SfdMsrAlarmRdsPi_Type()
)
sfdMsrAlarmRdsPi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAlarmRdsPi.setStatus("current")
_SfdMsrNotification_ObjectIdentity = ObjectIdentity
sfdMsrNotification = _SfdMsrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 2)
)
_SfdMsrNotificationCounter_Type = Counter32
_SfdMsrNotificationCounter_Object = MibScalar
sfdMsrNotificationCounter = _SfdMsrNotificationCounter_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 2, 1),
    _SfdMsrNotificationCounter_Type()
)
sfdMsrNotificationCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrNotificationCounter.setStatus("current")
_SfdMsrNotificationTimeStamp_Type = DateAndTime
_SfdMsrNotificationTimeStamp_Object = MibScalar
sfdMsrNotificationTimeStamp = _SfdMsrNotificationTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 2, 2),
    _SfdMsrNotificationTimeStamp_Type()
)
sfdMsrNotificationTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrNotificationTimeStamp.setStatus("current")
_SfdMsrNotificationLastSettingChanged_Type = ObjectIdentifier
_SfdMsrNotificationLastSettingChanged_Object = MibScalar
sfdMsrNotificationLastSettingChanged = _SfdMsrNotificationLastSettingChanged_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 2, 3),
    _SfdMsrNotificationLastSettingChanged_Type()
)
sfdMsrNotificationLastSettingChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrNotificationLastSettingChanged.setStatus("current")
_SfdMsrNotificationLastSettingChangedFrom_Type = NotificationSettingChangedFrom
_SfdMsrNotificationLastSettingChangedFrom_Object = MibScalar
sfdMsrNotificationLastSettingChangedFrom = _SfdMsrNotificationLastSettingChangedFrom_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 2, 4),
    _SfdMsrNotificationLastSettingChangedFrom_Type()
)
sfdMsrNotificationLastSettingChangedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrNotificationLastSettingChangedFrom.setStatus("current")
_SfdMsrNotificationPriority_Type = Gauge32
_SfdMsrNotificationPriority_Object = MibScalar
sfdMsrNotificationPriority = _SfdMsrNotificationPriority_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 2, 5),
    _SfdMsrNotificationPriority_Type()
)
sfdMsrNotificationPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrNotificationPriority.setStatus("current")
_SfdMsrRfIn_ObjectIdentity = ObjectIdentity
sfdMsrRfIn = _SfdMsrRfIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 3)
)
_SfdMsrRfInFilter_Type = FilterIfMpxModes
_SfdMsrRfInFilter_Object = MibScalar
sfdMsrRfInFilter = _SfdMsrRfInFilter_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 3, 1),
    _SfdMsrRfInFilter_Type()
)
sfdMsrRfInFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRfInFilter.setStatus("current")
_SfdMsrRfInSignalStrength_Type = Integer32
_SfdMsrRfInSignalStrength_Object = MibScalar
sfdMsrRfInSignalStrength = _SfdMsrRfInSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 3, 2),
    _SfdMsrRfInSignalStrength_Type()
)
sfdMsrRfInSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRfInSignalStrength.setStatus("current")
_SfdMsrRfInMuted_Type = RfInMuted
_SfdMsrRfInMuted_Object = MibScalar
sfdMsrRfInMuted = _SfdMsrRfInMuted_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 3, 3),
    _SfdMsrRfInMuted_Type()
)
sfdMsrRfInMuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRfInMuted.setStatus("current")
_SfdMsrMpx_ObjectIdentity = ObjectIdentity
sfdMsrMpx = _SfdMsrMpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 4)
)
_SfdMsrMpxPilotLevelKhz_Type = Integer32
_SfdMsrMpxPilotLevelKhz_Object = MibScalar
sfdMsrMpxPilotLevelKhz = _SfdMsrMpxPilotLevelKhz_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 4, 1),
    _SfdMsrMpxPilotLevelKhz_Type()
)
sfdMsrMpxPilotLevelKhz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrMpxPilotLevelKhz.setStatus("current")
_SfdMsrMpxRdsLevelKhz_Type = Integer32
_SfdMsrMpxRdsLevelKhz_Object = MibScalar
sfdMsrMpxRdsLevelKhz = _SfdMsrMpxRdsLevelKhz_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 4, 2),
    _SfdMsrMpxRdsLevelKhz_Type()
)
sfdMsrMpxRdsLevelKhz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrMpxRdsLevelKhz.setStatus("current")
_SfdMsrMpxRdsBer_Type = Integer32
_SfdMsrMpxRdsBer_Object = MibScalar
sfdMsrMpxRdsBer = _SfdMsrMpxRdsBer_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 4, 3),
    _SfdMsrMpxRdsBer_Type()
)
sfdMsrMpxRdsBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrMpxRdsBer.setStatus("current")
_SfdMsrMpxMaxDeviation_Type = Integer32
_SfdMsrMpxMaxDeviation_Object = MibScalar
sfdMsrMpxMaxDeviation = _SfdMsrMpxMaxDeviation_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 4, 4),
    _SfdMsrMpxMaxDeviation_Type()
)
sfdMsrMpxMaxDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrMpxMaxDeviation.setStatus("current")
_SfdMsrMpxDeviation_Type = Integer32
_SfdMsrMpxDeviation_Object = MibScalar
sfdMsrMpxDeviation = _SfdMsrMpxDeviation_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 4, 5),
    _SfdMsrMpxDeviation_Type()
)
sfdMsrMpxDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrMpxDeviation.setStatus("current")
_SfdMsrMpxPilotLevelDbu_Type = Integer32
_SfdMsrMpxPilotLevelDbu_Object = MibScalar
sfdMsrMpxPilotLevelDbu = _SfdMsrMpxPilotLevelDbu_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 4, 6),
    _SfdMsrMpxPilotLevelDbu_Type()
)
sfdMsrMpxPilotLevelDbu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrMpxPilotLevelDbu.setStatus("current")
_SfdMsrMpxRdsLevelDbu_Type = Integer32
_SfdMsrMpxRdsLevelDbu_Object = MibScalar
sfdMsrMpxRdsLevelDbu = _SfdMsrMpxRdsLevelDbu_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 4, 7),
    _SfdMsrMpxRdsLevelDbu_Type()
)
sfdMsrMpxRdsLevelDbu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrMpxRdsLevelDbu.setStatus("current")
_SfdMsrAudio_ObjectIdentity = ObjectIdentity
sfdMsrAudio = _SfdMsrAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 5)
)
_SfdMsrAudioLeftLevel_Type = Integer32
_SfdMsrAudioLeftLevel_Object = MibScalar
sfdMsrAudioLeftLevel = _SfdMsrAudioLeftLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 5, 1),
    _SfdMsrAudioLeftLevel_Type()
)
sfdMsrAudioLeftLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAudioLeftLevel.setStatus("current")
_SfdMsrAudioRightLevel_Type = Integer32
_SfdMsrAudioRightLevel_Object = MibScalar
sfdMsrAudioRightLevel = _SfdMsrAudioRightLevel_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 5, 2),
    _SfdMsrAudioRightLevel_Type()
)
sfdMsrAudioRightLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrAudioRightLevel.setStatus("current")
_SfdMsrRds_ObjectIdentity = ObjectIdentity
sfdMsrRds = _SfdMsrRds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6)
)
_SfdMsrRdsTA_Type = RdsTAModes
_SfdMsrRdsTA_Object = MibScalar
sfdMsrRdsTA = _SfdMsrRdsTA_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 1),
    _SfdMsrRdsTA_Type()
)
sfdMsrRdsTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsTA.setStatus("current")
_SfdMsrRdsTP_Type = RdsTPModes
_SfdMsrRdsTP_Object = MibScalar
sfdMsrRdsTP = _SfdMsrRdsTP_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 2),
    _SfdMsrRdsTP_Type()
)
sfdMsrRdsTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsTP.setStatus("current")
_SfdMsrRdsPI_Type = Integer32
_SfdMsrRdsPI_Object = MibScalar
sfdMsrRdsPI = _SfdMsrRdsPI_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 3),
    _SfdMsrRdsPI_Type()
)
sfdMsrRdsPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsPI.setStatus("current")
_SfdMsrRdsDI_Type = RdsDIModes
_SfdMsrRdsDI_Object = MibScalar
sfdMsrRdsDI = _SfdMsrRdsDI_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 4),
    _SfdMsrRdsDI_Type()
)
sfdMsrRdsDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsDI.setStatus("current")
_SfdMsrRdsPS_Type = OctetString
_SfdMsrRdsPS_Object = MibScalar
sfdMsrRdsPS = _SfdMsrRdsPS_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 5),
    _SfdMsrRdsPS_Type()
)
sfdMsrRdsPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsPS.setStatus("current")
_SfdMsrRdsMS_Type = RdsMSModes
_SfdMsrRdsMS_Object = MibScalar
sfdMsrRdsMS = _SfdMsrRdsMS_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 6),
    _SfdMsrRdsMS_Type()
)
sfdMsrRdsMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsMS.setStatus("current")
_SfdMsrRdsPTY_Type = RdsPTYModes
_SfdMsrRdsPTY_Object = MibScalar
sfdMsrRdsPTY = _SfdMsrRdsPTY_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 7),
    _SfdMsrRdsPTY_Type()
)
sfdMsrRdsPTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsPTY.setStatus("current")
_SfdMsrRdsRT_Type = OctetString
_SfdMsrRdsRT_Object = MibScalar
sfdMsrRdsRT = _SfdMsrRdsRT_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 8),
    _SfdMsrRdsRT_Type()
)
sfdMsrRdsRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsRT.setStatus("current")
_SfdMsrRdsCTTime_Type = OctetString
_SfdMsrRdsCTTime_Object = MibScalar
sfdMsrRdsCTTime = _SfdMsrRdsCTTime_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 9),
    _SfdMsrRdsCTTime_Type()
)
sfdMsrRdsCTTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsCTTime.setStatus("current")
_SfdMsrRdsCTDate_Type = OctetString
_SfdMsrRdsCTDate_Object = MibScalar
sfdMsrRdsCTDate = _SfdMsrRdsCTDate_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 6, 10),
    _SfdMsrRdsCTDate_Type()
)
sfdMsrRdsCTDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrRdsCTDate.setStatus("current")
_SfdMsr_ObjectIdentity = ObjectIdentity
sfdMsr = _SfdMsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 7)
)
_SfdMsrControlMode_Type = ControlMode
_SfdMsrControlMode_Object = MibScalar
sfdMsrControlMode = _SfdMsrControlMode_Object(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 3, 7, 1),
    _SfdMsrControlMode_Type()
)
sfdMsrControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfdMsrControlMode.setStatus("current")
_SfdGroups_ObjectIdentity = ObjectIdentity
sfdGroups = _SfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4)
)

# Managed Objects groups

sfdGrpIdentity = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 1)
)
sfdGrpIdentity.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdIdnOptions"),
        ("PROFLINE-SFD-MIB", "sfdIdnSerialNumber"),
        ("PROFLINE-SFD-MIB", "sfdIdnFirmwareType"),
        ("PROFLINE-SFD-MIB", "sfdIdnFirmwareVersion"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo1"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo2"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo3"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo4"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo5"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo6"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo7"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo8"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo9"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo10"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo11"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceInfo12"),
        ("PROFLINE-SFD-MIB", "sfdIdnDeviceManualLink"))
)
if mibBuilder.loadTexts:
    sfdGrpIdentity.setStatus("current")

sfdGrpSet = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 2)
)
sfdGrpSet.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetReboot"),
        ("PROFLINE-SFD-MIB", "sfdSetAsPowerOnDefault"))
)
if mibBuilder.loadTexts:
    sfdGrpSet.setStatus("current")

sfdGrpSetClock = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 3)
)
sfdGrpSetClock.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetClockDateTime"),
        ("PROFLINE-SFD-MIB", "sfdSetClockLockTo"),
        ("PROFLINE-SFD-MIB", "sfdSetClockTimezone"),
        ("PROFLINE-SFD-MIB", "sfdSetClockDST"))
)
if mibBuilder.loadTexts:
    sfdGrpSetClock.setStatus("current")

sfdGrpSetRfIn = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 4)
)
sfdGrpSetRfIn.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetRfInFrequency"),
        ("PROFLINE-SFD-MIB", "sfdSetRfInInput"),
        ("PROFLINE-SFD-MIB", "sfdSetRfInAttenuator"),
        ("PROFLINE-SFD-MIB", "sfdSetRfInMute"))
)
if mibBuilder.loadTexts:
    sfdGrpSetRfIn.setStatus("current")

sfdGrpSetFilter = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 5)
)
sfdGrpSetFilter.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetFilterIfMpx"),
        ("PROFLINE-SFD-MIB", "sfdSetFilterStereoThreshold"))
)
if mibBuilder.loadTexts:
    sfdGrpSetFilter.setStatus("current")

sfdGrpSetMpx = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 6)
)
sfdGrpSetMpx.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetMpxGain"),
        ("PROFLINE-SFD-MIB", "sfdSetMpxPreEmphase"),
        ("PROFLINE-SFD-MIB", "sfdSetMpxSource"),
        ("PROFLINE-SFD-MIB", "sfdSetMpxRdsMode"),
        ("PROFLINE-SFD-MIB", "sfdSetMpxResetMaxDeviation"))
)
if mibBuilder.loadTexts:
    sfdGrpSetMpx.setStatus("current")

sfdGrpSetAudio = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 7)
)
sfdGrpSetAudio.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAudioAnalogXlrGain"),
        ("PROFLINE-SFD-MIB", "sfdSetAudioTesttone"),
        ("PROFLINE-SFD-MIB", "sfdSetAudioDeEmphase"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAudio.setStatus("current")

sfdGrpSetName = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 8)
)
sfdGrpSetName.setObjects(
    ("PROFLINE-SFD-MIB", "sfdSetNameUnit")
)
if mibBuilder.loadTexts:
    sfdGrpSetName.setStatus("obsolete")

sfdGrpSetAlarmRfInLow = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 9)
)
sfdGrpSetAlarmRfInLow.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmRfInLowMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRfInLowLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRfInLowWarningDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRfInLowAlarmDelay"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmRfInLow.setStatus("current")

sfdGrpSetAlarmRfInHigh = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 10)
)
sfdGrpSetAlarmRfInHigh.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmRfInHighMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRfInHighLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRfInHighWarningDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRfInHighAlarmDelay"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmRfInHigh.setStatus("current")

sfdGrpSetAlarmPilot = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 11)
)
sfdGrpSetAlarmPilot.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmPilotMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmPilotLevelKhz"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmPilotWarningDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmPilotAlarmDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmPilotLevelDbu"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmPilot.setStatus("current")

sfdGrpSetAlarmRdsLevel = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 12)
)
sfdGrpSetAlarmRdsLevel.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmRdsLevelMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsLevelLevelKhz"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsLevelWarningDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsLevelAlarmDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsLevelLevelDbu"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmRdsLevel.setStatus("current")

sfdGrpSetAlarmRdsBer = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 13)
)
sfdGrpSetAlarmRdsBer.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmRdsBerMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsBerLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsBerWarningDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsBerAlarmDelay"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmRdsBer.setStatus("current")

sfdGrpSetAlarmMpxDeviation = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 14)
)
sfdGrpSetAlarmMpxDeviation.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmMpxDeviationMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmMpxDeviationLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmMpxDeviationOffDelay"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmMpxDeviation.setStatus("current")

sfdGrpSetAlarmAudioLeft = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 15)
)
sfdGrpSetAlarmAudioLeft.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmAudioLeftMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmAudioLeftLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmAudioLeftWarningDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmAudioLeftAlarmDelay"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmAudioLeft.setStatus("current")

sfdGrpSetAlarmAudioRight = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 16)
)
sfdGrpSetAlarmAudioRight.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmAudioRightMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmAudioRightLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmAudioRightWarningDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmAudioRightAlarmDelay"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmAudioRight.setStatus("current")

sfdGrpSetAlarmAudioBoth = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 17)
)
sfdGrpSetAlarmAudioBoth.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmAudioBothMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmAudioBothLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmAudioBothWarningDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmAudioBothAlarmDelay"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmAudioBoth.setStatus("current")

sfdGrpSetIOInput = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 18)
)
sfdGrpSetIOInput.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetControlIOInput0"),
        ("PROFLINE-SFD-MIB", "sfdSetControlIOInput1"),
        ("PROFLINE-SFD-MIB", "sfdSetControlIOInput2"),
        ("PROFLINE-SFD-MIB", "sfdSetControlIOInput3"))
)
if mibBuilder.loadTexts:
    sfdGrpSetIOInput.setStatus("current")

sfdGrpSetIOOutput = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 19)
)
sfdGrpSetIOOutput.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetControlIOOutput0"),
        ("PROFLINE-SFD-MIB", "sfdSetControlIOOutput1"),
        ("PROFLINE-SFD-MIB", "sfdSetControlIOOutput2"),
        ("PROFLINE-SFD-MIB", "sfdSetControlIOOutput3"))
)
if mibBuilder.loadTexts:
    sfdGrpSetIOOutput.setStatus("current")

sfdGrpSetNotificationMode = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 20)
)
sfdGrpSetNotificationMode.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetNotificationModeAll"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeHeartbeat"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeSettingChanged"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeControlMode"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeControlModeLocalSuppress"))
)
if mibBuilder.loadTexts:
    sfdGrpSetNotificationMode.setStatus("current")

sfdGrpSetNotificationModeAlarm = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 21)
)
sfdGrpSetNotificationModeAlarm.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmRfInLevelLow"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmRfInLevelHigh"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmPilotLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmMpxDeviation"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmRdsBer"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmRdsLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmAudioLevelLeft"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmAudioLevelRight"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmAudioLevelBoth"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeAlarmRdsPi"))
)
if mibBuilder.loadTexts:
    sfdGrpSetNotificationModeAlarm.setStatus("current")

sfdGrpMsrAlarm = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 22)
)
sfdGrpMsrAlarm.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdMsrAlarmRfInLevelLow"),
        ("PROFLINE-SFD-MIB", "sfdMsrAlarmRfInLevelHigh"),
        ("PROFLINE-SFD-MIB", "sfdMsrAlarmPilotLevel"),
        ("PROFLINE-SFD-MIB", "sfdMsrAlarmMpxDeviation"),
        ("PROFLINE-SFD-MIB", "sfdMsrAlarmRdsBer"),
        ("PROFLINE-SFD-MIB", "sfdMsrAlarmRdsLevel"),
        ("PROFLINE-SFD-MIB", "sfdMsrAlarmAudioLevelLeft"),
        ("PROFLINE-SFD-MIB", "sfdMsrAlarmAudioLevelRight"),
        ("PROFLINE-SFD-MIB", "sfdMsrAlarmAudioLevelBoth"),
        ("PROFLINE-SFD-MIB", "sfdMsrAlarmRdsPi"))
)
if mibBuilder.loadTexts:
    sfdGrpMsrAlarm.setStatus("current")

sfdGrpMsrNotification = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 23)
)
sfdGrpMsrNotification.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdMsrNotificationCounter"),
        ("PROFLINE-SFD-MIB", "sfdMsrNotificationTimeStamp"),
        ("PROFLINE-SFD-MIB", "sfdMsrNotificationLastSettingChanged"),
        ("PROFLINE-SFD-MIB", "sfdMsrNotificationLastSettingChangedFrom"),
        ("PROFLINE-SFD-MIB", "sfdMsrNotificationPriority"))
)
if mibBuilder.loadTexts:
    sfdGrpMsrNotification.setStatus("current")

sfdGrpMsrRfin = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 24)
)
sfdGrpMsrRfin.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdMsrRfInFilter"),
        ("PROFLINE-SFD-MIB", "sfdMsrRfInSignalStrength"),
        ("PROFLINE-SFD-MIB", "sfdMsrRfInMuted"))
)
if mibBuilder.loadTexts:
    sfdGrpMsrRfin.setStatus("current")

sfdGrpMsrMpx = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 25)
)
sfdGrpMsrMpx.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdMsrMpxPilotLevelKhz"),
        ("PROFLINE-SFD-MIB", "sfdMsrMpxRdsLevelKhz"),
        ("PROFLINE-SFD-MIB", "sfdMsrMpxRdsBer"),
        ("PROFLINE-SFD-MIB", "sfdMsrMpxMaxDeviation"),
        ("PROFLINE-SFD-MIB", "sfdMsrMpxDeviation"),
        ("PROFLINE-SFD-MIB", "sfdMsrMpxPilotLevelDbu"),
        ("PROFLINE-SFD-MIB", "sfdMsrMpxRdsLevelDbu"))
)
if mibBuilder.loadTexts:
    sfdGrpMsrMpx.setStatus("current")

sfdGrpMsrAudio = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 26)
)
sfdGrpMsrAudio.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdMsrAudioLeftLevel"),
        ("PROFLINE-SFD-MIB", "sfdMsrAudioRightLevel"))
)
if mibBuilder.loadTexts:
    sfdGrpMsrAudio.setStatus("current")

sfdGrpMsrRds = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 27)
)
sfdGrpMsrRds.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdMsrRdsTA"),
        ("PROFLINE-SFD-MIB", "sfdMsrRdsTP"),
        ("PROFLINE-SFD-MIB", "sfdMsrRdsPI"),
        ("PROFLINE-SFD-MIB", "sfdMsrRdsDI"),
        ("PROFLINE-SFD-MIB", "sfdMsrRdsPS"),
        ("PROFLINE-SFD-MIB", "sfdMsrRdsMS"),
        ("PROFLINE-SFD-MIB", "sfdMsrRdsPTY"),
        ("PROFLINE-SFD-MIB", "sfdMsrRdsRT"),
        ("PROFLINE-SFD-MIB", "sfdMsrRdsCTTime"),
        ("PROFLINE-SFD-MIB", "sfdMsrRdsCTDate"))
)
if mibBuilder.loadTexts:
    sfdGrpMsrRds.setStatus("current")

sfdGrpMsr = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 30)
)
sfdGrpMsr.setObjects(
    ("PROFLINE-SFD-MIB", "sfdMsrControlMode")
)
if mibBuilder.loadTexts:
    sfdGrpMsr.setStatus("current")

sfdGrpSetNotificationPriority = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 31)
)
sfdGrpSetNotificationPriority.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityHeartbeat"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPrioritySettingChanged"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityControlMode"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmRfInLevelLow"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmRfInLevelHigh"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmPilotLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmMpxDeviation"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmRdsBer"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmRdsLevel"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmAudioLevelLeft"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmAudioLevelRight"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmAudioLevelBoth"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityAlarmRdsPi"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityStatusRfInFrequency"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityStatusRfInInput"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityStatusRfInMuted"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityStatusRfInFilter"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityStatusMpxSource"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityStatusAudioTestTone"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationPriorityStatusAudioDeEmphase"))
)
if mibBuilder.loadTexts:
    sfdGrpSetNotificationPriority.setStatus("current")

sfdGrpSetObsoletedItems = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 32)
)
sfdGrpSetObsoletedItems.setObjects(
    ("PROFLINE-SFD-MIB", "sfdSetClockOffset")
)
if mibBuilder.loadTexts:
    sfdGrpSetObsoletedItems.setStatus("obsolete")

sfdGrpSetAlarmRdsPi = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 33)
)
sfdGrpSetAlarmRdsPi.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetAlarmRdsPiMode"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsPiPi"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsPiWarningDelay"),
        ("PROFLINE-SFD-MIB", "sfdSetAlarmRdsPiAlarmDelay"))
)
if mibBuilder.loadTexts:
    sfdGrpSetAlarmRdsPi.setStatus("current")

sfdGrpSetNotificationModeStatus = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 4, 34)
)
sfdGrpSetNotificationModeStatus.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdSetNotificationModeStatusRfInFrequency"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeStatusRfInInput"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeStatusRfInMuted"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeStatusRfInFilter"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeStatusMpxSource"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeStatusAudioTestTone"),
        ("PROFLINE-SFD-MIB", "sfdSetNotificationModeStatusAudioDeEmphase"))
)
if mibBuilder.loadTexts:
    sfdGrpSetNotificationModeStatus.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sfdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4, 1, 5)
)
sfdCompliance.setObjects(
      *(("PROFLINE-SFD-MIB", "sfdGrpIdentity"),
        ("PROFLINE-SFD-MIB", "sfdGrpSet"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetClock"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetRfIn"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetFilter"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetMpx"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAudio"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmRfInLow"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmRfInHigh"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmPilot"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmRdsLevel"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmRdsBer"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmRdsPi"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmMpxDeviation"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmAudioLeft"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmAudioRight"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetAlarmAudioBoth"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetIOInput"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetIOOutput"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetNotificationMode"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetNotificationModeAlarm"),
        ("PROFLINE-SFD-MIB", "sfdGrpMsrAlarm"),
        ("PROFLINE-SFD-MIB", "sfdGrpMsrNotification"),
        ("PROFLINE-SFD-MIB", "sfdGrpMsrRfin"),
        ("PROFLINE-SFD-MIB", "sfdGrpMsrMpx"),
        ("PROFLINE-SFD-MIB", "sfdGrpMsrAudio"),
        ("PROFLINE-SFD-MIB", "sfdGrpMsrRds"),
        ("PROFLINE-SFD-MIB", "sfdGrpMsr"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetNotificationPriority"),
        ("PROFLINE-SFD-MIB", "sfdGrpSetNotificationModeStatus"))
)
if mibBuilder.loadTexts:
    sfdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROFLINE-SFD-MIB",
    **{"LockToSourceModes": LockToSourceModes,
       "RfInInputModes": RfInInputModes,
       "FilterIfMpxModes": FilterIfMpxModes,
       "MpxPreEmphaseModes": MpxPreEmphaseModes,
       "MpxSourceModes": MpxSourceModes,
       "MpxRdsModes": MpxRdsModes,
       "AudioTesttoneModes": AudioTesttoneModes,
       "AudioDeEmphaseModes": AudioDeEmphaseModes,
       "AlarmModes": AlarmModes,
       "InputModes": InputModes,
       "OutputModes": OutputModes,
       "RdsTAModes": RdsTAModes,
       "RdsTPModes": RdsTPModes,
       "RdsDIModes": RdsDIModes,
       "RdsMSModes": RdsMSModes,
       "RdsPTYModes": RdsPTYModes,
       "ControlMode": ControlMode,
       "NotificationOffOn": NotificationOffOn,
       "NotificationSettingChangedFrom": NotificationSettingChangedFrom,
       "AlarmStatus": AlarmStatus,
       "NotificationModes": NotificationModes,
       "TimezoneModes": TimezoneModes,
       "DSTOffOn": DSTOffOn,
       "RfInMuted": RfInMuted,
       "sfd": sfd,
       "sfdNotifications": sfdNotifications,
       "sfdIdentity": sfdIdentity,
       "sfdIdnOptions": sfdIdnOptions,
       "sfdIdnSerialNumber": sfdIdnSerialNumber,
       "sfdIdnFirmwareVersionTable": sfdIdnFirmwareVersionTable,
       "sfdIdnFirmwareVersionEntry": sfdIdnFirmwareVersionEntry,
       "sfdIdnFirmwareIndex": sfdIdnFirmwareIndex,
       "sfdIdnFirmwareType": sfdIdnFirmwareType,
       "sfdIdnFirmwareVersion": sfdIdnFirmwareVersion,
       "sfdIdnDeviceInfo1": sfdIdnDeviceInfo1,
       "sfdIdnDeviceInfo2": sfdIdnDeviceInfo2,
       "sfdIdnDeviceInfo3": sfdIdnDeviceInfo3,
       "sfdIdnDeviceInfo4": sfdIdnDeviceInfo4,
       "sfdIdnDeviceInfo5": sfdIdnDeviceInfo5,
       "sfdIdnDeviceInfo6": sfdIdnDeviceInfo6,
       "sfdIdnDeviceInfo7": sfdIdnDeviceInfo7,
       "sfdIdnDeviceInfo8": sfdIdnDeviceInfo8,
       "sfdIdnDeviceInfo9": sfdIdnDeviceInfo9,
       "sfdIdnDeviceInfo10": sfdIdnDeviceInfo10,
       "sfdIdnDeviceInfo11": sfdIdnDeviceInfo11,
       "sfdIdnDeviceInfo12": sfdIdnDeviceInfo12,
       "sfdIdnDeviceManualLink": sfdIdnDeviceManualLink,
       "sfdSettings": sfdSettings,
       "sfdSet": sfdSet,
       "sfdSetReboot": sfdSetReboot,
       "sfdSetAsPowerOnDefault": sfdSetAsPowerOnDefault,
       "sfdSetClock": sfdSetClock,
       "sfdSetClockDateTime": sfdSetClockDateTime,
       "sfdSetClockOffset": sfdSetClockOffset,
       "sfdSetClockLockTo": sfdSetClockLockTo,
       "sfdSetClockTimezone": sfdSetClockTimezone,
       "sfdSetClockDST": sfdSetClockDST,
       "sfdSetRfIn": sfdSetRfIn,
       "sfdSetRfInFrequency": sfdSetRfInFrequency,
       "sfdSetRfInInput": sfdSetRfInInput,
       "sfdSetRfInAttenuator": sfdSetRfInAttenuator,
       "sfdSetRfInMute": sfdSetRfInMute,
       "sfdSetFilter": sfdSetFilter,
       "sfdSetFilterIfMpx": sfdSetFilterIfMpx,
       "sfdSetFilterStereoThreshold": sfdSetFilterStereoThreshold,
       "sfdSetMpx": sfdSetMpx,
       "sfdSetMpxGain": sfdSetMpxGain,
       "sfdSetMpxPreEmphase": sfdSetMpxPreEmphase,
       "sfdSetMpxSource": sfdSetMpxSource,
       "sfdSetMpxRdsMode": sfdSetMpxRdsMode,
       "sfdSetMpxResetMaxDeviation": sfdSetMpxResetMaxDeviation,
       "sfdSetAudio": sfdSetAudio,
       "sfdSetAudioAnalogXlrGain": sfdSetAudioAnalogXlrGain,
       "sfdSetAudioTesttone": sfdSetAudioTesttone,
       "sfdSetAudioDeEmphase": sfdSetAudioDeEmphase,
       "sfdSetName": sfdSetName,
       "sfdSetNameUnit": sfdSetNameUnit,
       "sfdSetAlarm": sfdSetAlarm,
       "sfdSetAlarmRfIn": sfdSetAlarmRfIn,
       "sfdSetAlarmRfInLow": sfdSetAlarmRfInLow,
       "sfdSetAlarmRfInLowMode": sfdSetAlarmRfInLowMode,
       "sfdSetAlarmRfInLowLevel": sfdSetAlarmRfInLowLevel,
       "sfdSetAlarmRfInLowWarningDelay": sfdSetAlarmRfInLowWarningDelay,
       "sfdSetAlarmRfInLowAlarmDelay": sfdSetAlarmRfInLowAlarmDelay,
       "sfdSetAlarmRfInHigh": sfdSetAlarmRfInHigh,
       "sfdSetAlarmRfInHighMode": sfdSetAlarmRfInHighMode,
       "sfdSetAlarmRfInHighLevel": sfdSetAlarmRfInHighLevel,
       "sfdSetAlarmRfInHighWarningDelay": sfdSetAlarmRfInHighWarningDelay,
       "sfdSetAlarmRfInHighAlarmDelay": sfdSetAlarmRfInHighAlarmDelay,
       "sfdSetAlarmPilot": sfdSetAlarmPilot,
       "sfdSetAlarmPilotMode": sfdSetAlarmPilotMode,
       "sfdSetAlarmPilotLevelKhz": sfdSetAlarmPilotLevelKhz,
       "sfdSetAlarmPilotWarningDelay": sfdSetAlarmPilotWarningDelay,
       "sfdSetAlarmPilotAlarmDelay": sfdSetAlarmPilotAlarmDelay,
       "sfdSetAlarmPilotLevelDbu": sfdSetAlarmPilotLevelDbu,
       "sfdSetAlarmRds": sfdSetAlarmRds,
       "sfdSetAlarmRdsLevel": sfdSetAlarmRdsLevel,
       "sfdSetAlarmRdsLevelMode": sfdSetAlarmRdsLevelMode,
       "sfdSetAlarmRdsLevelLevelKhz": sfdSetAlarmRdsLevelLevelKhz,
       "sfdSetAlarmRdsLevelWarningDelay": sfdSetAlarmRdsLevelWarningDelay,
       "sfdSetAlarmRdsLevelAlarmDelay": sfdSetAlarmRdsLevelAlarmDelay,
       "sfdSetAlarmRdsLevelLevelDbu": sfdSetAlarmRdsLevelLevelDbu,
       "sfdSetAlarmRdsBer": sfdSetAlarmRdsBer,
       "sfdSetAlarmRdsBerMode": sfdSetAlarmRdsBerMode,
       "sfdSetAlarmRdsBerLevel": sfdSetAlarmRdsBerLevel,
       "sfdSetAlarmRdsBerWarningDelay": sfdSetAlarmRdsBerWarningDelay,
       "sfdSetAlarmRdsBerAlarmDelay": sfdSetAlarmRdsBerAlarmDelay,
       "sfdSetAlarmRdsPi": sfdSetAlarmRdsPi,
       "sfdSetAlarmRdsPiMode": sfdSetAlarmRdsPiMode,
       "sfdSetAlarmRdsPiPi": sfdSetAlarmRdsPiPi,
       "sfdSetAlarmRdsPiWarningDelay": sfdSetAlarmRdsPiWarningDelay,
       "sfdSetAlarmRdsPiAlarmDelay": sfdSetAlarmRdsPiAlarmDelay,
       "sfdSetAlarmMpxDeviation": sfdSetAlarmMpxDeviation,
       "sfdSetAlarmMpxDeviationMode": sfdSetAlarmMpxDeviationMode,
       "sfdSetAlarmMpxDeviationLevel": sfdSetAlarmMpxDeviationLevel,
       "sfdSetAlarmMpxDeviationOffDelay": sfdSetAlarmMpxDeviationOffDelay,
       "sfdSetAlarmAudio": sfdSetAlarmAudio,
       "sfdSetAlarmAudioLeft": sfdSetAlarmAudioLeft,
       "sfdSetAlarmAudioLeftMode": sfdSetAlarmAudioLeftMode,
       "sfdSetAlarmAudioLeftLevel": sfdSetAlarmAudioLeftLevel,
       "sfdSetAlarmAudioLeftWarningDelay": sfdSetAlarmAudioLeftWarningDelay,
       "sfdSetAlarmAudioLeftAlarmDelay": sfdSetAlarmAudioLeftAlarmDelay,
       "sfdSetAlarmAudioRight": sfdSetAlarmAudioRight,
       "sfdSetAlarmAudioRightMode": sfdSetAlarmAudioRightMode,
       "sfdSetAlarmAudioRightLevel": sfdSetAlarmAudioRightLevel,
       "sfdSetAlarmAudioRightWarningDelay": sfdSetAlarmAudioRightWarningDelay,
       "sfdSetAlarmAudioRightAlarmDelay": sfdSetAlarmAudioRightAlarmDelay,
       "sfdSetAlarmAudioBoth": sfdSetAlarmAudioBoth,
       "sfdSetAlarmAudioBothMode": sfdSetAlarmAudioBothMode,
       "sfdSetAlarmAudioBothLevel": sfdSetAlarmAudioBothLevel,
       "sfdSetAlarmAudioBothWarningDelay": sfdSetAlarmAudioBothWarningDelay,
       "sfdSetAlarmAudioBothAlarmDelay": sfdSetAlarmAudioBothAlarmDelay,
       "sfdSetControlIO": sfdSetControlIO,
       "sfdSetControlIOInput": sfdSetControlIOInput,
       "sfdSetControlIOInput0": sfdSetControlIOInput0,
       "sfdSetControlIOInput1": sfdSetControlIOInput1,
       "sfdSetControlIOInput2": sfdSetControlIOInput2,
       "sfdSetControlIOInput3": sfdSetControlIOInput3,
       "sfdSetControlIOOutput": sfdSetControlIOOutput,
       "sfdSetControlIOOutput0": sfdSetControlIOOutput0,
       "sfdSetControlIOOutput1": sfdSetControlIOOutput1,
       "sfdSetControlIOOutput2": sfdSetControlIOOutput2,
       "sfdSetControlIOOutput3": sfdSetControlIOOutput3,
       "sfdSetNotification": sfdSetNotification,
       "sfdSetNotificationMode": sfdSetNotificationMode,
       "sfdSetNotificationModeAll": sfdSetNotificationModeAll,
       "sfdSetNotificationModeHeartbeat": sfdSetNotificationModeHeartbeat,
       "sfdSetNotificationModeSettingChanged": sfdSetNotificationModeSettingChanged,
       "sfdSetNotificationModeControlMode": sfdSetNotificationModeControlMode,
       "sfdSetNotificationModeControlModeLocalSuppress": sfdSetNotificationModeControlModeLocalSuppress,
       "sfdSetNotificationModeAlarm": sfdSetNotificationModeAlarm,
       "sfdSetNotificationModeAlarmRfInLevelLow": sfdSetNotificationModeAlarmRfInLevelLow,
       "sfdSetNotificationModeAlarmRfInLevelHigh": sfdSetNotificationModeAlarmRfInLevelHigh,
       "sfdSetNotificationModeAlarmPilotLevel": sfdSetNotificationModeAlarmPilotLevel,
       "sfdSetNotificationModeAlarmMpxDeviation": sfdSetNotificationModeAlarmMpxDeviation,
       "sfdSetNotificationModeAlarmRdsBer": sfdSetNotificationModeAlarmRdsBer,
       "sfdSetNotificationModeAlarmRdsLevel": sfdSetNotificationModeAlarmRdsLevel,
       "sfdSetNotificationModeAlarmAudioLevelLeft": sfdSetNotificationModeAlarmAudioLevelLeft,
       "sfdSetNotificationModeAlarmAudioLevelRight": sfdSetNotificationModeAlarmAudioLevelRight,
       "sfdSetNotificationModeAlarmAudioLevelBoth": sfdSetNotificationModeAlarmAudioLevelBoth,
       "sfdSetNotificationModeAlarmRdsPi": sfdSetNotificationModeAlarmRdsPi,
       "sfdSetNotificationPriority": sfdSetNotificationPriority,
       "sfdSetNotificationPriorityHeartbeat": sfdSetNotificationPriorityHeartbeat,
       "sfdSetNotificationPrioritySettingChanged": sfdSetNotificationPrioritySettingChanged,
       "sfdSetNotificationPriorityControlMode": sfdSetNotificationPriorityControlMode,
       "sfdSetNotificationPriorityAlarmRfInLevelLow": sfdSetNotificationPriorityAlarmRfInLevelLow,
       "sfdSetNotificationPriorityAlarmRfInLevelHigh": sfdSetNotificationPriorityAlarmRfInLevelHigh,
       "sfdSetNotificationPriorityAlarmPilotLevel": sfdSetNotificationPriorityAlarmPilotLevel,
       "sfdSetNotificationPriorityAlarmMpxDeviation": sfdSetNotificationPriorityAlarmMpxDeviation,
       "sfdSetNotificationPriorityAlarmRdsBer": sfdSetNotificationPriorityAlarmRdsBer,
       "sfdSetNotificationPriorityAlarmRdsLevel": sfdSetNotificationPriorityAlarmRdsLevel,
       "sfdSetNotificationPriorityAlarmAudioLevelLeft": sfdSetNotificationPriorityAlarmAudioLevelLeft,
       "sfdSetNotificationPriorityAlarmAudioLevelRight": sfdSetNotificationPriorityAlarmAudioLevelRight,
       "sfdSetNotificationPriorityAlarmAudioLevelBoth": sfdSetNotificationPriorityAlarmAudioLevelBoth,
       "sfdSetNotificationPriorityAlarmRdsPi": sfdSetNotificationPriorityAlarmRdsPi,
       "sfdSetNotificationPriorityStatusRfInFrequency": sfdSetNotificationPriorityStatusRfInFrequency,
       "sfdSetNotificationPriorityStatusRfInInput": sfdSetNotificationPriorityStatusRfInInput,
       "sfdSetNotificationPriorityStatusRfInMuted": sfdSetNotificationPriorityStatusRfInMuted,
       "sfdSetNotificationPriorityStatusRfInFilter": sfdSetNotificationPriorityStatusRfInFilter,
       "sfdSetNotificationPriorityStatusMpxSource": sfdSetNotificationPriorityStatusMpxSource,
       "sfdSetNotificationPriorityStatusAudioTestTone": sfdSetNotificationPriorityStatusAudioTestTone,
       "sfdSetNotificationPriorityStatusAudioDeEmphase": sfdSetNotificationPriorityStatusAudioDeEmphase,
       "sfdSetNotificationModeStatus": sfdSetNotificationModeStatus,
       "sfdSetNotificationModeStatusRfInFrequency": sfdSetNotificationModeStatusRfInFrequency,
       "sfdSetNotificationModeStatusRfInInput": sfdSetNotificationModeStatusRfInInput,
       "sfdSetNotificationModeStatusRfInMuted": sfdSetNotificationModeStatusRfInMuted,
       "sfdSetNotificationModeStatusRfInFilter": sfdSetNotificationModeStatusRfInFilter,
       "sfdSetNotificationModeStatusMpxSource": sfdSetNotificationModeStatusMpxSource,
       "sfdSetNotificationModeStatusAudioTestTone": sfdSetNotificationModeStatusAudioTestTone,
       "sfdSetNotificationModeStatusAudioDeEmphase": sfdSetNotificationModeStatusAudioDeEmphase,
       "sfdSetPreset": sfdSetPreset,
       "sfdSetPresetRecall": sfdSetPresetRecall,
       "sfdSetPresetSaveAs": sfdSetPresetSaveAs,
       "sfdSetPresetActiveDefaults": sfdSetPresetActiveDefaults,
       "sfdSetPresetActiveName": sfdSetPresetActiveName,
       "sfdMeasurements": sfdMeasurements,
       "sfdMsrAlarm": sfdMsrAlarm,
       "sfdMsrAlarmRfInLevelLow": sfdMsrAlarmRfInLevelLow,
       "sfdMsrAlarmRfInLevelHigh": sfdMsrAlarmRfInLevelHigh,
       "sfdMsrAlarmPilotLevel": sfdMsrAlarmPilotLevel,
       "sfdMsrAlarmMpxDeviation": sfdMsrAlarmMpxDeviation,
       "sfdMsrAlarmRdsBer": sfdMsrAlarmRdsBer,
       "sfdMsrAlarmRdsLevel": sfdMsrAlarmRdsLevel,
       "sfdMsrAlarmAudioLevelLeft": sfdMsrAlarmAudioLevelLeft,
       "sfdMsrAlarmAudioLevelRight": sfdMsrAlarmAudioLevelRight,
       "sfdMsrAlarmAudioLevelBoth": sfdMsrAlarmAudioLevelBoth,
       "sfdMsrAlarmRdsPi": sfdMsrAlarmRdsPi,
       "sfdMsrNotification": sfdMsrNotification,
       "sfdMsrNotificationCounter": sfdMsrNotificationCounter,
       "sfdMsrNotificationTimeStamp": sfdMsrNotificationTimeStamp,
       "sfdMsrNotificationLastSettingChanged": sfdMsrNotificationLastSettingChanged,
       "sfdMsrNotificationLastSettingChangedFrom": sfdMsrNotificationLastSettingChangedFrom,
       "sfdMsrNotificationPriority": sfdMsrNotificationPriority,
       "sfdMsrRfIn": sfdMsrRfIn,
       "sfdMsrRfInFilter": sfdMsrRfInFilter,
       "sfdMsrRfInSignalStrength": sfdMsrRfInSignalStrength,
       "sfdMsrRfInMuted": sfdMsrRfInMuted,
       "sfdMsrMpx": sfdMsrMpx,
       "sfdMsrMpxPilotLevelKhz": sfdMsrMpxPilotLevelKhz,
       "sfdMsrMpxRdsLevelKhz": sfdMsrMpxRdsLevelKhz,
       "sfdMsrMpxRdsBer": sfdMsrMpxRdsBer,
       "sfdMsrMpxMaxDeviation": sfdMsrMpxMaxDeviation,
       "sfdMsrMpxDeviation": sfdMsrMpxDeviation,
       "sfdMsrMpxPilotLevelDbu": sfdMsrMpxPilotLevelDbu,
       "sfdMsrMpxRdsLevelDbu": sfdMsrMpxRdsLevelDbu,
       "sfdMsrAudio": sfdMsrAudio,
       "sfdMsrAudioLeftLevel": sfdMsrAudioLeftLevel,
       "sfdMsrAudioRightLevel": sfdMsrAudioRightLevel,
       "sfdMsrRds": sfdMsrRds,
       "sfdMsrRdsTA": sfdMsrRdsTA,
       "sfdMsrRdsTP": sfdMsrRdsTP,
       "sfdMsrRdsPI": sfdMsrRdsPI,
       "sfdMsrRdsDI": sfdMsrRdsDI,
       "sfdMsrRdsPS": sfdMsrRdsPS,
       "sfdMsrRdsMS": sfdMsrRdsMS,
       "sfdMsrRdsPTY": sfdMsrRdsPTY,
       "sfdMsrRdsRT": sfdMsrRdsRT,
       "sfdMsrRdsCTTime": sfdMsrRdsCTTime,
       "sfdMsrRdsCTDate": sfdMsrRdsCTDate,
       "sfdMsr": sfdMsr,
       "sfdMsrControlMode": sfdMsrControlMode,
       "sfdGroups": sfdGroups,
       "sfdGrpIdentity": sfdGrpIdentity,
       "sfdGrpSet": sfdGrpSet,
       "sfdGrpSetClock": sfdGrpSetClock,
       "sfdGrpSetRfIn": sfdGrpSetRfIn,
       "sfdGrpSetFilter": sfdGrpSetFilter,
       "sfdGrpSetMpx": sfdGrpSetMpx,
       "sfdGrpSetAudio": sfdGrpSetAudio,
       "sfdGrpSetName": sfdGrpSetName,
       "sfdGrpSetAlarmRfInLow": sfdGrpSetAlarmRfInLow,
       "sfdGrpSetAlarmRfInHigh": sfdGrpSetAlarmRfInHigh,
       "sfdGrpSetAlarmPilot": sfdGrpSetAlarmPilot,
       "sfdGrpSetAlarmRdsLevel": sfdGrpSetAlarmRdsLevel,
       "sfdGrpSetAlarmRdsBer": sfdGrpSetAlarmRdsBer,
       "sfdGrpSetAlarmMpxDeviation": sfdGrpSetAlarmMpxDeviation,
       "sfdGrpSetAlarmAudioLeft": sfdGrpSetAlarmAudioLeft,
       "sfdGrpSetAlarmAudioRight": sfdGrpSetAlarmAudioRight,
       "sfdGrpSetAlarmAudioBoth": sfdGrpSetAlarmAudioBoth,
       "sfdGrpSetIOInput": sfdGrpSetIOInput,
       "sfdGrpSetIOOutput": sfdGrpSetIOOutput,
       "sfdGrpSetNotificationMode": sfdGrpSetNotificationMode,
       "sfdGrpSetNotificationModeAlarm": sfdGrpSetNotificationModeAlarm,
       "sfdGrpMsrAlarm": sfdGrpMsrAlarm,
       "sfdGrpMsrNotification": sfdGrpMsrNotification,
       "sfdGrpMsrRfin": sfdGrpMsrRfin,
       "sfdGrpMsrMpx": sfdGrpMsrMpx,
       "sfdGrpMsrAudio": sfdGrpMsrAudio,
       "sfdGrpMsrRds": sfdGrpMsrRds,
       "sfdGrpMsr": sfdGrpMsr,
       "sfdGrpSetNotificationPriority": sfdGrpSetNotificationPriority,
       "sfdGrpSetObsoletedItems": sfdGrpSetObsoletedItems,
       "sfdGrpSetAlarmRdsPi": sfdGrpSetAlarmRdsPi,
       "sfdGrpSetNotificationModeStatus": sfdGrpSetNotificationModeStatus,
       "sfdCompliance": sfdCompliance}
)
