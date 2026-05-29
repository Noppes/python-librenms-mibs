# SNMP MIB module (ALCATEL-IND1-DA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos7\ALCATEL-IND1-DA-MIB

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

(softentIND1Da,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Da")

(systemServicesDate,
 systemServicesTime) = mibBuilder.importSymbols(
    "ALCATEL-IND1-SYSTEM-MIB",
    "systemServicesDate",
    "systemServicesTime")

(TmnxEncapVal,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "TmnxEncapVal")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1DaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DaMIB.setRevisions(
        ("2019-11-27 00:00",
         "2007-04-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaDaClassificationPolicyType(TextualConvention, Integer32):
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
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339)
        )
    )
    namedValues = NamedValues(
        *(("authPassAltUnp", 1),
          ("authPassDefUnp", 2),
          ("authPassSrvUnp", 3),
          ("noAuthMacRuleUnp", 4),
          ("noAuthMacRangeRuleUnp", 5),
          ("noAuthIpRuleUnp", 6),
          ("authFailDefUnp", 7),
          ("authFailMacRuleUnp", 8),
          ("authFailMacRangeRuleUnp", 9),
          ("authFailIpRuleUnp", 10),
          ("authFailRuleDefUnp", 11),
          ("authFailMacRangeVlanTagRuleUnp", 12),
          ("tagAuthFailMacRuleUnp", 13),
          ("tagAuthFailMacVlanTagRuleUnp", 14),
          ("tagAuthFailMacRangeRuleUnp", 15),
          ("tagAuthFailMacRangeVlanTagRuleUnp", 16),
          ("tagAuthFailIpRuleUnp", 17),
          ("tagAuthFailIpVlanTagRuleUnp", 18),
          ("tagAuthFailVlanTagRuleUnp", 19),
          ("tagAuthPassAltUnp", 20),
          ("tagAuthPassDefUnp", 21),
          ("tagAuthPassSrvUnp", 22),
          ("tagMacRuleUnp", 23),
          ("tagMacVlanTagRuleUnp", 24),
          ("tagMacRangeRuleUnp", 25),
          ("tagMacRangeVlanTagRuleUnp", 26),
          ("tagIpRuleUnp", 27),
          ("tagIpVlanTagRuleUnp", 28),
          ("tagVlanTagRuleUnp", 29),
          ("tagRuleDefUnp", 30),
          ("authPassDefUnpBlk", 31),
          ("authFailDefUnpBlk", 32),
          ("authFailRuleDefUnpBlk", 33),
          ("tagAuthPassDefUnpBlk", 34),
          ("tagRuleDefUnpBlk", 35),
          ("authPassSrvUnpTagMismatchBlk", 36),
          ("authPassAltUnpTagMismatchBlk", 37),
          ("authPassDefUnpTagMismatchBlk", 38),
          ("authFailMacRuleUnpTagMismatchBlk", 39),
          ("authFailMacVlanRuleUnpTagMismatchBlk", 40),
          ("authFailMacRangeRuleUnpTagMismatchBlk", 41),
          ("authFailMacRangeVlanRuleUnpTagMismatchBlk", 42),
          ("authFailIpRuleUnpTagMismatchBlk", 43),
          ("authFailIpVlanRuleUnpTagMismatchBlk", 44),
          ("authFailVlanRuleUnpTagMismatchBlk", 45),
          ("defUnpBlk", 46),
          ("authPassSrvUnpBlk", 47),
          ("authPassAltUnpBlk", 48),
          ("authFailMacRuleUnpBlk", 49),
          ("authFailMacRangeRuleUnpBlk", 50),
          ("authFailIpRuleUnpBlk", 51),
          ("tagMacRuleUnpBlk", 52),
          ("tagMacVlanTagRuleUnpBlk", 53),
          ("tagMacRangeRuleUnpBlk", 54),
          ("tagMacRangeVlanTagRuleUnpBlk", 55),
          ("tagIpRuleUnpBlk", 56),
          ("tagIpVlanTagRuleUnpBlk", 57),
          ("tagVlanTagRuleUnpBlk", 58),
          ("authSrvDownUnpTagMismatchBlk", 59),
          ("noMatchingUnpBlk", 60),
          ("trustTag", 61),
          ("authSrvDownUnp", 62),
          ("defUnp", 63),
          ("lpsUnpBlk", 64),
          ("sysDefSpb", 65),
          ("defSpbProfile", 66),
          ("noSpbResource", 67),
          ("tagAuthPassPortMacIpRuleUnp", 68),
          ("tagAuthPassPortMacRuleUnp", 69),
          ("tagAuthPassPortIpRuleUnp", 70),
          ("tagAuthPassGroupMacIpRuleUnp", 71),
          ("tagAuthPassGroupMacRuleUnp", 72),
          ("tagAuthPassGroupIpRuleUnp", 73),
          ("tagAuthPassPortRuleUnp", 74),
          ("tagAuthPassGroupRuleUnp", 75),
          ("tagAuthPassMacVlanRuleUnp", 76),
          ("tagAuthPassMacRuleUnp", 77),
          ("tagAuthPassMacouiRuleUnp", 78),
          ("tagAuthPassMacrangeVlanRuleUnp", 79),
          ("tagAuthPassMacrangeRuleUnp", 80),
          ("tagAuthPassLldpRuleUnp", 81),
          ("tagAuthPassL2authRuleUnp", 82),
          ("tagAuthPassIpVlanRuleUnp", 83),
          ("tagAuthPassIpRuleUnp", 84),
          ("tagAuthPassVlanRuleUnp", 85),
          ("tagAuthPassDmGroupRuleUnp", 86),
          ("tagAuthFailPortMacIpRuleUnp", 87),
          ("tagAuthFailPortMacRuleUnp", 88),
          ("tagAuthFailPortIpRuleUnp", 89),
          ("tagAuthFailGroupMacIpRuleUnp", 90),
          ("tagAuthFailGroupMacRuleUnp", 91),
          ("tagAuthFailGroupIpRuleUnp", 92),
          ("tagAuthFailPortRuleUnp", 93),
          ("tagAuthFailGroupRuleUnp", 94),
          ("tagAuthFailMacouiRuleUnp", 95),
          ("tagAuthFailLldpRuleUnp", 96),
          ("tagAuthFailL2authRuleUnp", 97),
          ("tagAuthFailDmGroupRuleUnp", 98),
          ("tagPortMacIpRuleUnp", 99),
          ("tagPortMacRuleUnp", 100),
          ("tagPortIpRuleUnp", 101),
          ("tagGroupMacIpRuleUnp", 102),
          ("tagGroupMacRuleUnp", 103),
          ("tagGroupIpRuleUnp", 104),
          ("tagPortRuleUnp", 105),
          ("tagGroupRuleUnp", 106),
          ("tagMacouiRuleUnp", 107),
          ("tagLldpRuleUnp", 108),
          ("tagL2authRuleUnp", 109),
          ("tagDmGroupRuleUnp", 110),
          ("authPassPortMacIpRuleUnp", 111),
          ("authPassPortMacRuleUnp", 112),
          ("authPassPortIpRuleUnp", 113),
          ("authPassGroupMacIpRuleUnp", 114),
          ("authPassGroupMacRuleUnp", 115),
          ("authPassGroupIpRuleUnp", 116),
          ("authPassPortRuleUnp", 117),
          ("authPassGroupRuleUnp", 118),
          ("authPassMacRuleUnp", 119),
          ("authPassMacouiRuleUnp", 120),
          ("authPassMacrangeRuleUnp", 121),
          ("authPassLldpRuleUnp", 122),
          ("authPassL2authRuleUnp", 123),
          ("authPassIpRuleUnp", 124),
          ("authPassDmGroupRuleUnp", 125),
          ("authFailPortMacIpRuleUnp", 126),
          ("authFailPortMacRuleUnp", 127),
          ("authFailPortIpRuleUnp", 128),
          ("authFailGroupMacIpRuleUnp", 129),
          ("authFailGroupMacRuleUnp", 130),
          ("authFailGroupIpRuleUnp", 131),
          ("authFailPortRuleUnp", 132),
          ("authFailGroupRuleUnp", 133),
          ("authFailMacouiRuleUnp", 134),
          ("authFailLldpRuleUnp", 135),
          ("authFailL2authRuleUnp", 136),
          ("authFailDmGroupRuleUnp", 137),
          ("noAuthPortMacIpRuleUnp", 138),
          ("noAuthPortMacRuleUnp", 139),
          ("noAuthPortIpRuleUnp", 140),
          ("noAuthGroupMacIpRuleUnp", 141),
          ("noAuthGroupMacRuleUnp", 142),
          ("noAuthGroupIpRuleUnp", 143),
          ("noAuthPortRuleUnp", 144),
          ("noAuthGroupRuleUnp", 145),
          ("noAuthMacouiRuleUnp", 146),
          ("noAuthLldpRuleUnp", 147),
          ("noAuthL2authRuleUnp", 148),
          ("noAuthDmGroupRuleUnp", 149),
          ("authPassPortMacIpRuleUnpTagMismatchBlk", 150),
          ("authPassPortMacRuleUnpTagMismatchBlk", 151),
          ("authPassPortIpRuleUnpTagMismatchBlk", 152),
          ("authPassGroupMacIpRuleUnpTagMismatchBlk", 153),
          ("authPassGroupMacRuleUnpTagMismatchBlk", 154),
          ("authPassGroupIpRuleUnpTagMismatchBlk", 155),
          ("authPassPortRuleUnpTagMismatchBlk", 156),
          ("authPassGroupRuleUnpTagMismatchBlk", 157),
          ("authPassMacVlanRuleUnpTagMismatchBlk", 158),
          ("authPassMacRuleUnpTagMismatchBlk", 159),
          ("authPassMacouiRuleUnpTagMismatchBlk", 160),
          ("authPassMacrangeVlanRuleUnpTagMismatchBlk", 161),
          ("authPassMacrangeRuleUnpTagMismatchBlk", 162),
          ("authPassLldpRuleUnpTagMismatchBlk", 163),
          ("authPassL2authRuleUnpTagMismatchBlk", 164),
          ("authPassIpVlanRuleUnpTagMismatchBlk", 165),
          ("authPassIpRuleUnpTagMismatchBlk", 166),
          ("authPassVlanRuleUnpTagMismatchBlk", 167),
          ("authPassDmGroupRuleUnpTagMismatchBlk", 168),
          ("authFailPortMacIpRuleUnpTagMismatchBlk", 169),
          ("authFailPortMacRuleUnpTagMismatchBlk", 170),
          ("authFailPortIpRuleUnpTagMismatchBlk", 171),
          ("authFailGroupMacIpRuleUnpTagMismatchBlk", 172),
          ("authFailGroupMacRuleUnpTagMismatchBlk", 173),
          ("authFailGroupIpRuleUnpTagMismatchBlk", 174),
          ("authFailPortRuleUnpTagMismatchBlk", 175),
          ("authFailGroupRuleUnpTagMismatchBlk", 176),
          ("authFailMacouiRuleUnpTagMismatchBlk", 177),
          ("authFailLldpRuleUnpTagMismatchBlk", 178),
          ("authFailL2authRuleUnpTagMismatchBlk", 179),
          ("authFailDmGroupRuleUnpTagMismatchBlk", 180),
          ("portMacIpRuleUnpTagMismatchBlk", 181),
          ("portMacRuleUnpTagMismatchBlk", 182),
          ("portIpRuleUnpTagMismatchBlk", 183),
          ("groupMacIpRuleUnpTagMismatchBlk", 184),
          ("groupMacRuleUnpTagMismatchBlk", 185),
          ("groupIpRuleUnpTagMismatchBlk", 186),
          ("portRuleUnpTagMismatchBlk", 187),
          ("groupRuleUnpTagMismatchBlk", 188),
          ("macouiRuleUnpTagMismatchBlk", 189),
          ("lldpRuleUnpTagMismatchBlk", 190),
          ("l2authRuleUnpTagMismatchBlk", 191),
          ("dmGroupRuleUnpTagMismatchBlk", 192),
          ("tagAuthPassExtendedRuleUnp", 193),
          ("tagAuthFailExtendedRuleUnp", 194),
          ("tagExtendedRuleUnp", 195),
          ("authPassExtendedRuleUnp", 196),
          ("authFailExtendedRuleUnp", 197),
          ("noAuthExtendedRuleUnp", 198),
          ("authPassExtendedRuleUnpTagMismatchBlk", 199),
          ("authFailExtendedRuleUnpTagMismatchBlk", 200),
          ("extendedRuleUnpTagMismatchBlk", 201),
          ("lpsStatic", 202),
          ("lpsPseudoStatic", 203),
          ("lpsDupStatic", 204),
          ("authSrvDownEdgeProfileUnp", 205),
          ("byodPauseTimerFilter", 206),
          ("byodServerUnp", 207),
          ("noVxlanResource", 208),
          ("noVxlanResourceAuthSrvDownUnp", 209),
          ("defVxlanProfile", 210),
          ("sysDefVxlan", 211),
          ("cportalEdgeProfilePolicy", 212),
          ("tagAuthPassPortMacIpVlanRuleUnp", 213),
          ("tagAuthPassPortMacVlanRuleUnp", 214),
          ("tagAuthPassPortIpVlanRuleUnp", 215),
          ("tagAuthPassGroupMacIpVlanRuleUnp", 216),
          ("tagAuthPassGroupMacVlanRuleUnp", 217),
          ("tagAuthPassGroupIpVlanRuleUnp", 218),
          ("tagAuthPassPortVlanRuleUnp", 219),
          ("tagAuthPassGroupVlanRuleUnp", 220),
          ("tagAuthPassMacouiVlanRuleUnp", 221),
          ("tagAuthPassL2authVlanRuleUnp", 222),
          ("tagAuthPassDmGroupVlanRuleUnp", 223),
          ("tagAuthFailPortMacIpVlanRuleUnp", 224),
          ("tagAuthFailPortMacVlanRuleUnp", 225),
          ("tagAuthFailPortIpVlanRuleUnp", 226),
          ("tagAuthFailGroupMacIpVlanRuleUnp", 227),
          ("tagAuthFailGroupMacVlanRuleUnp", 228),
          ("tagAuthFailGroupIpVlanRuleUnp", 229),
          ("tagAuthFailPortVlanRuleUnp", 230),
          ("tagAuthFailGroupVlanRuleUnp", 231),
          ("tagAuthFailMacouiVlanRuleUnp", 232),
          ("tagAuthFailL2authVlanRuleUnp", 233),
          ("tagAuthFailDmGroupVlanRuleUnp", 234),
          ("tagPortMacIpVlanRuleUnp", 235),
          ("tagPortMacVlanRuleUnp", 236),
          ("tagPortIpVlanRuleUnp", 237),
          ("tagGroupMacIpVlanRuleUnp", 238),
          ("tagGroupMacVlanRuleUnp", 239),
          ("tagGroupIpVlanRuleUnp", 240),
          ("tagPortVlanRuleUnp", 241),
          ("tagGroupVlanRuleUnp", 242),
          ("tagMacouiVlanRuleUnp", 243),
          ("tagL2authVlanRuleUnp", 244),
          ("tagDmGroupVlanRuleUnp", 245),
          ("authPassPortMacIpVlanRuleUnp", 246),
          ("authPassPortMacVlanRuleUnp", 247),
          ("authPassPortIpVlanRuleUnp", 248),
          ("authPassGroupMacIpVlanRuleUnp", 249),
          ("authPassGroupMacVlanRuleUnp", 250),
          ("authPassGroupIpVlanRuleUnp", 251),
          ("authPassPortVlanRuleUnp", 252),
          ("authPassGroupVlanRuleUnp", 253),
          ("authPassMacouiVlanRuleUnp", 254),
          ("authPassL2authVlanRuleUnp", 255),
          ("authPassDmGroupVlanRuleUnp", 256),
          ("authFailPortMacIpVlanRuleUnp", 257),
          ("authFailPortMacVlanRuleUnp", 258),
          ("authFailPortIpVlanRuleUnp", 259),
          ("authFailGroupMacIpVlanRuleUnp", 260),
          ("authFailGroupMacVlanRuleUnp", 261),
          ("authFailGroupIpVlanRuleUnp", 262),
          ("authFailPortVlanRuleUnp", 263),
          ("authFailGroupVlanRuleUnp", 264),
          ("authFailMacouiVlanRuleUnp", 265),
          ("authFailL2authVlanRuleUnp", 266),
          ("authFailDmGroupVlanRuleUnp", 267),
          ("noAuthPortMacIpVlanRuleUnp", 268),
          ("noAuthPortMacVlanRuleUnp", 269),
          ("noAuthPortIpVlanRuleUnp", 270),
          ("noAuthGroupMacIpVlanRuleUnp", 271),
          ("noAuthGroupMacVlanRuleUnp", 272),
          ("noAuthGroupIpVlanRuleUnp", 273),
          ("noAuthPortVlanRuleUnp", 274),
          ("noAuthGroupVlanRuleUnp", 275),
          ("noAuthMacouiVlanRuleUnp", 276),
          ("noAuthL2authVlanRuleUnp", 277),
          ("noAuthDmGroupVlanRuleUnp", 278),
          ("authPassPortMacIpVlanRuleUnpTagMismatchBlk", 279),
          ("authPassPortMacVlanRuleUnpTagMismatchBlk", 280),
          ("authPassPortIpVlanRuleUnpTagMismatchBlk", 281),
          ("authPassGroupMacIpVlanRuleUnpTagMismatchBlk", 282),
          ("authPassGroupMacVlanRuleUnpTagMismatchBlk", 283),
          ("authPassGroupIpVlanRuleUnpTagMismatchBlk", 284),
          ("authPassPortVlanRuleUnpTagMismatchBlk", 285),
          ("authPassGroupVlanRuleUnpTagMismatchBlk", 286),
          ("authPassMacouiVlanRuleUnpTagMismatchBlk", 287),
          ("authPassL2authVlanRuleUnpTagMismatchBlk", 288),
          ("authPassDmGroupVlanRuleUnpTagMismatchBlk", 289),
          ("authFailPortMacIpVlanRuleUnpTagMismatchBlk", 290),
          ("authFailPortMacVlanRuleUnpTagMismatchBlk", 291),
          ("authFailPortIpVlanRuleUnpTagMismatchBlk", 292),
          ("authFailGroupMacIpVlanRuleUnpTagMismatchBlk", 293),
          ("authFailGroupMacVlanRuleUnpTagMismatchBlk", 294),
          ("authFailGroupIpVlanRuleUnpTagMismatchBlk", 295),
          ("authFailPortVlanRuleUnpTagMismatchBlk", 296),
          ("authFailGroupVlanRuleUnpTagMismatchBlk", 297),
          ("authFailMacouiVlanRuleUnpTagMismatchBlk", 298),
          ("authFailL2authVlanRuleUnpTagMismatchBlk", 299),
          ("authFailDmGroupVlanRuleUnpTagMismatchBlk", 300),
          ("portMacIpVlanRuleUnpTagMismatchBlk", 301),
          ("portMacVlanRuleUnpTagMismatchBlk", 302),
          ("portIpVlanRuleUnpTagMismatchBlk", 303),
          ("groupMacIpVlanRuleUnpTagMismatchBlk", 304),
          ("groupMacVlanRuleUnpTagMismatchBlk", 305),
          ("groupIpVlanRuleUnpTagMismatchBlk", 306),
          ("portVlanRuleUnpTagMismatchBlk", 307),
          ("groupVlanRuleUnpTagMismatchBlk", 308),
          ("macouiVlanRuleUnpTagMismatchBlk", 309),
          ("l2authVlanRuleUnpTagMismatchBlk", 310),
          ("dmGroupVlanRuleUnpTagMismatchBlk", 311),
          ("cportalPauseTimerFilter", 312),
          ("noSpbResourceAuthSrvDownUnp", 313),
          ("authSrvDowniVoiceUnp", 314),
          ("authSrvDownVoiceUnpTagMismatchBlk", 315),
          ("sysMacCollision", 316),
          ("noGreResource", 317),
          ("ovEnforced", 318),
          ("tcamTtiRuleExhaust", 319),
          ("spbNoControlBvlanBlk", 320),
          ("spbServiceIdMismatchBlk", 321),
          ("vxlanServiceIdMismatchBlk", 322),
          ("l2greServiceIdMismatchBlk", 323),
          ("staticServiceIdMismatchBlk", 324),
          ("spbServiceParamMismatchBlk", 325),
          ("vxlanServiceParamMismatchBlk", 326),
          ("l2greServiceParamMismatchBlk", 327),
          ("staticServiceParamMismatchBlk", 328),
          ("staticServiceIdNotFoundBlk", 329),
          ("serviceInternalErrorBlk", 330),
          ("serviceDisabled", 331),
          ("vpConflict", 332),
          ("noVplsResource", 333),
          ("sysDefVpls", 334),
          ("vplsServiceParamMismatchBlk", 335),
          ("vplsServiceIdMismatchBlk", 336),
          ("noVplsResourceAuthSrvDownUnp", 337),
          ("maxUnpUsersExhaust", 338),
          ("radiusTrustTagVlan", 339))
    )



class AlaDaAuthenticationType(TextualConvention, Integer32):
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
        *(("noAuthentication", 1),
          ("dot1XAuthentication", 2),
          ("macAuthentication", 3),
          ("captivePortal", 4))
    )



class AlaDaAuthenticationResult(TextualConvention, Integer32):
    status = "current"
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
        *(("notApplicable", 0),
          ("inProgress", 1),
          ("success", 2),
          ("fail", 3))
    )



class AlaDaMacLearntState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 0),
          ("filtering", 1))
    )



class AlaMultiChassisConfigStatus(TextualConvention, Integer32):
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
          ("sync", 2),
          ("outOfSync", 3))
    )



class MacOui(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



# MIB Managed Objects in the order of their OIDs

_AlaIND1DaMIBNotifications_ObjectIdentity = ObjectIdentity
alaIND1DaMIBNotifications = _AlaIND1DaMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0)
)
if mibBuilder.loadTexts:
    alaIND1DaMIBNotifications.setStatus("current")
_AlaIND1DaMIBObjects_ObjectIdentity = ObjectIdentity
alaIND1DaMIBObjects = _AlaIND1DaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1)
)
if mibBuilder.loadTexts:
    alaIND1DaMIBObjects.setStatus("current")
_AlaDaUserNetProfileTable_Object = MibTable
alaDaUserNetProfileTable = _AlaDaUserNetProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaDaUserNetProfileTable.setStatus("deprecated")
_AlaDaUserNetProfileEntry_Object = MibTableRow
alaDaUserNetProfileEntry = _AlaDaUserNetProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1)
)
alaDaUserNetProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUserNetProfileEntry.setStatus("deprecated")


class _AlaDaUserNetProfileName_Type(SnmpAdminString):
    """Custom type alaDaUserNetProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUserNetProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUserNetProfileName_Object = MibTableColumn
alaDaUserNetProfileName = _AlaDaUserNetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 1),
    _AlaDaUserNetProfileName_Type()
)
alaDaUserNetProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUserNetProfileName.setStatus("deprecated")


class _AlaDaUserNetProfileVlanID_Type(Integer32):
    """Custom type alaDaUserNetProfileVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUserNetProfileVlanID_Type.__name__ = "Integer32"
_AlaDaUserNetProfileVlanID_Object = MibTableColumn
alaDaUserNetProfileVlanID = _AlaDaUserNetProfileVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 2),
    _AlaDaUserNetProfileVlanID_Type()
)
alaDaUserNetProfileVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileVlanID.setStatus("deprecated")
_AlaDaUserNetProfileRowStatus_Type = RowStatus
_AlaDaUserNetProfileRowStatus_Object = MibTableColumn
alaDaUserNetProfileRowStatus = _AlaDaUserNetProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 3),
    _AlaDaUserNetProfileRowStatus_Type()
)
alaDaUserNetProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileRowStatus.setStatus("deprecated")


class _AlaDaUserNetProfileQosPolicyListName_Type(SnmpAdminString):
    """Custom type alaDaUserNetProfileQosPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUserNetProfileQosPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaDaUserNetProfileQosPolicyListName_Object = MibTableColumn
alaDaUserNetProfileQosPolicyListName = _AlaDaUserNetProfileQosPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 4),
    _AlaDaUserNetProfileQosPolicyListName_Type()
)
alaDaUserNetProfileQosPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileQosPolicyListName.setStatus("deprecated")


class _AlaDaUserNetProfileMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUserNetProfileMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUserNetProfileMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUserNetProfileMCLagConfigStatus_Object = MibTableColumn
alaDaUserNetProfileMCLagConfigStatus = _AlaDaUserNetProfileMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 5),
    _AlaDaUserNetProfileMCLagConfigStatus_Type()
)
alaDaUserNetProfileMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUserNetProfileMCLagConfigStatus.setStatus("deprecated")


class _AlaDaUserNetProfileSaaProfileName_Type(SnmpAdminString):
    """Custom type alaDaUserNetProfileSaaProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUserNetProfileSaaProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUserNetProfileSaaProfileName_Object = MibTableColumn
alaDaUserNetProfileSaaProfileName = _AlaDaUserNetProfileSaaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 6),
    _AlaDaUserNetProfileSaaProfileName_Type()
)
alaDaUserNetProfileSaaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileSaaProfileName.setStatus("deprecated")


class _AlaDaUserNetProfileMobileTag_Type(Integer32):
    """Custom type alaDaUserNetProfileMobileTag based on Integer32"""
    defaultValue = 2

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


_AlaDaUserNetProfileMobileTag_Type.__name__ = "Integer32"
_AlaDaUserNetProfileMobileTag_Object = MibTableColumn
alaDaUserNetProfileMobileTag = _AlaDaUserNetProfileMobileTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 7),
    _AlaDaUserNetProfileMobileTag_Type()
)
alaDaUserNetProfileMobileTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileMobileTag.setStatus("deprecated")


class _AlaDaUserNetProfileMaxIngressBw_Type(Integer32):
    """Custom type alaDaUserNetProfileMaxIngressBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUserNetProfileMaxIngressBw_Type.__name__ = "Integer32"
_AlaDaUserNetProfileMaxIngressBw_Object = MibTableColumn
alaDaUserNetProfileMaxIngressBw = _AlaDaUserNetProfileMaxIngressBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 8),
    _AlaDaUserNetProfileMaxIngressBw_Type()
)
alaDaUserNetProfileMaxIngressBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileMaxIngressBw.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaDaUserNetProfileMaxIngressBw.setUnits("kilobits per second")


class _AlaDaUserNetProfileMaxEgressBw_Type(Integer32):
    """Custom type alaDaUserNetProfileMaxEgressBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUserNetProfileMaxEgressBw_Type.__name__ = "Integer32"
_AlaDaUserNetProfileMaxEgressBw_Object = MibTableColumn
alaDaUserNetProfileMaxEgressBw = _AlaDaUserNetProfileMaxEgressBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 9),
    _AlaDaUserNetProfileMaxEgressBw_Type()
)
alaDaUserNetProfileMaxEgressBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileMaxEgressBw.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaDaUserNetProfileMaxEgressBw.setUnits("kilobits per second")


class _AlaDaUserNetProfileMaxIngressDepth_Type(Integer32):
    """Custom type alaDaUserNetProfileMaxIngressDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16384),
    )


_AlaDaUserNetProfileMaxIngressDepth_Type.__name__ = "Integer32"
_AlaDaUserNetProfileMaxIngressDepth_Object = MibTableColumn
alaDaUserNetProfileMaxIngressDepth = _AlaDaUserNetProfileMaxIngressDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 10),
    _AlaDaUserNetProfileMaxIngressDepth_Type()
)
alaDaUserNetProfileMaxIngressDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileMaxIngressDepth.setStatus("deprecated")


class _AlaDaUserNetProfileMaxEgressDepth_Type(Integer32):
    """Custom type alaDaUserNetProfileMaxEgressDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16384),
    )


_AlaDaUserNetProfileMaxEgressDepth_Type.__name__ = "Integer32"
_AlaDaUserNetProfileMaxEgressDepth_Object = MibTableColumn
alaDaUserNetProfileMaxEgressDepth = _AlaDaUserNetProfileMaxEgressDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 1, 1, 11),
    _AlaDaUserNetProfileMaxEgressDepth_Type()
)
alaDaUserNetProfileMaxEgressDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileMaxEgressDepth.setStatus("deprecated")
_AlaDaUNPIpNetRuleTable_Object = MibTable
alaDaUNPIpNetRuleTable = _AlaDaUNPIpNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleTable.setStatus("deprecated")
_AlaDaUNPIpNetRuleEntry_Object = MibTableRow
alaDaUNPIpNetRuleEntry = _AlaDaUNPIpNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 2, 1)
)
alaDaUNPIpNetRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleMask"),
)
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleEntry.setStatus("deprecated")
_AlaDaUNPIpNetRuleAddrType_Type = InetAddressType
_AlaDaUNPIpNetRuleAddrType_Object = MibTableColumn
alaDaUNPIpNetRuleAddrType = _AlaDaUNPIpNetRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 2, 1, 1),
    _AlaDaUNPIpNetRuleAddrType_Type()
)
alaDaUNPIpNetRuleAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleAddrType.setStatus("deprecated")
_AlaDaUNPIpNetRuleAddr_Type = InetAddress
_AlaDaUNPIpNetRuleAddr_Object = MibTableColumn
alaDaUNPIpNetRuleAddr = _AlaDaUNPIpNetRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 2, 1, 2),
    _AlaDaUNPIpNetRuleAddr_Type()
)
alaDaUNPIpNetRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleAddr.setStatus("deprecated")
_AlaDaUNPIpNetRuleMask_Type = InetAddress
_AlaDaUNPIpNetRuleMask_Object = MibTableColumn
alaDaUNPIpNetRuleMask = _AlaDaUNPIpNetRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 2, 1, 3),
    _AlaDaUNPIpNetRuleMask_Type()
)
alaDaUNPIpNetRuleMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleMask.setStatus("deprecated")


class _AlaDaUNPIpNetRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPIpNetRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPIpNetRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPIpNetRuleProfileName_Object = MibTableColumn
alaDaUNPIpNetRuleProfileName = _AlaDaUNPIpNetRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 2, 1, 4),
    _AlaDaUNPIpNetRuleProfileName_Type()
)
alaDaUNPIpNetRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleProfileName.setStatus("deprecated")


class _AlaDaUNPIpNetRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPIpNetRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPIpNetRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPIpNetRuleVlanTag_Object = MibTableColumn
alaDaUNPIpNetRuleVlanTag = _AlaDaUNPIpNetRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 2, 1, 5),
    _AlaDaUNPIpNetRuleVlanTag_Type()
)
alaDaUNPIpNetRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleVlanTag.setStatus("deprecated")
_AlaDaUNPIpNetRuleRowStatus_Type = RowStatus
_AlaDaUNPIpNetRuleRowStatus_Object = MibTableColumn
alaDaUNPIpNetRuleRowStatus = _AlaDaUNPIpNetRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 2, 1, 6),
    _AlaDaUNPIpNetRuleRowStatus_Type()
)
alaDaUNPIpNetRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPIpNetRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPIpNetRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPIpNetRuleMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPIpNetRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPIpNetRuleMCLagConfigStatus = _AlaDaUNPIpNetRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 2, 1, 7),
    _AlaDaUNPIpNetRuleMCLagConfigStatus_Type()
)
alaDaUNPIpNetRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleMCLagConfigStatus.setStatus("deprecated")
_AlaDaUNPMacRuleTable_Object = MibTable
alaDaUNPMacRuleTable = _AlaDaUNPMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaDaUNPMacRuleTable.setStatus("deprecated")
_AlaDaUNPMacRuleEntry_Object = MibTableRow
alaDaUNPMacRuleEntry = _AlaDaUNPMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 3, 1)
)
alaDaUNPMacRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacRuleEntry.setStatus("deprecated")
_AlaDaUNPMacRuleAddr_Type = MacAddress
_AlaDaUNPMacRuleAddr_Object = MibTableColumn
alaDaUNPMacRuleAddr = _AlaDaUNPMacRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 3, 1, 1),
    _AlaDaUNPMacRuleAddr_Type()
)
alaDaUNPMacRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleAddr.setStatus("deprecated")


class _AlaDaUNPMacRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPMacRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacRuleProfileName_Object = MibTableColumn
alaDaUNPMacRuleProfileName = _AlaDaUNPMacRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 3, 1, 2),
    _AlaDaUNPMacRuleProfileName_Type()
)
alaDaUNPMacRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleProfileName.setStatus("deprecated")


class _AlaDaUNPMacRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacRuleVlanTag_Object = MibTableColumn
alaDaUNPMacRuleVlanTag = _AlaDaUNPMacRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 3, 1, 3),
    _AlaDaUNPMacRuleVlanTag_Type()
)
alaDaUNPMacRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleVlanTag.setStatus("deprecated")
_AlaDaUNPMacRuleRowStatus_Type = RowStatus
_AlaDaUNPMacRuleRowStatus_Object = MibTableColumn
alaDaUNPMacRuleRowStatus = _AlaDaUNPMacRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 3, 1, 4),
    _AlaDaUNPMacRuleRowStatus_Type()
)
alaDaUNPMacRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPMacRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPMacRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPMacRuleMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPMacRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPMacRuleMCLagConfigStatus = _AlaDaUNPMacRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 3, 1, 5),
    _AlaDaUNPMacRuleMCLagConfigStatus_Type()
)
alaDaUNPMacRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleMCLagConfigStatus.setStatus("deprecated")
_AlaDaUNPMacRangeRuleTable_Object = MibTable
alaDaUNPMacRangeRuleTable = _AlaDaUNPMacRangeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleTable.setStatus("deprecated")
_AlaDaUNPMacRangeRuleEntry_Object = MibTableRow
alaDaUNPMacRangeRuleEntry = _AlaDaUNPMacRangeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 4, 1)
)
alaDaUNPMacRangeRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleLoAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleEntry.setStatus("deprecated")
_AlaDaUNPMacRangeRuleLoAddr_Type = MacAddress
_AlaDaUNPMacRangeRuleLoAddr_Object = MibTableColumn
alaDaUNPMacRangeRuleLoAddr = _AlaDaUNPMacRangeRuleLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 4, 1, 1),
    _AlaDaUNPMacRangeRuleLoAddr_Type()
)
alaDaUNPMacRangeRuleLoAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleLoAddr.setStatus("deprecated")
_AlaDaUNPMacRangeRuleHiAddr_Type = MacAddress
_AlaDaUNPMacRangeRuleHiAddr_Object = MibTableColumn
alaDaUNPMacRangeRuleHiAddr = _AlaDaUNPMacRangeRuleHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 4, 1, 2),
    _AlaDaUNPMacRangeRuleHiAddr_Type()
)
alaDaUNPMacRangeRuleHiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleHiAddr.setStatus("deprecated")


class _AlaDaUNPMacRangeRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPMacRangeRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacRangeRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacRangeRuleProfileName_Object = MibTableColumn
alaDaUNPMacRangeRuleProfileName = _AlaDaUNPMacRangeRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 4, 1, 3),
    _AlaDaUNPMacRangeRuleProfileName_Type()
)
alaDaUNPMacRangeRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleProfileName.setStatus("deprecated")


class _AlaDaUNPMacRangeRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacRangeRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacRangeRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacRangeRuleVlanTag_Object = MibTableColumn
alaDaUNPMacRangeRuleVlanTag = _AlaDaUNPMacRangeRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 4, 1, 4),
    _AlaDaUNPMacRangeRuleVlanTag_Type()
)
alaDaUNPMacRangeRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleVlanTag.setStatus("deprecated")
_AlaDaUNPMacRangeRuleRowStatus_Type = RowStatus
_AlaDaUNPMacRangeRuleRowStatus_Object = MibTableColumn
alaDaUNPMacRangeRuleRowStatus = _AlaDaUNPMacRangeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 4, 1, 5),
    _AlaDaUNPMacRangeRuleRowStatus_Type()
)
alaDaUNPMacRangeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPMacRangeRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPMacRangeRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPMacRangeRuleMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPMacRangeRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPMacRangeRuleMCLagConfigStatus = _AlaDaUNPMacRangeRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 4, 1, 6),
    _AlaDaUNPMacRangeRuleMCLagConfigStatus_Type()
)
alaDaUNPMacRangeRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleMCLagConfigStatus.setStatus("deprecated")
_AlaDaUNPVlanTagRuleTable_Object = MibTable
alaDaUNPVlanTagRuleTable = _AlaDaUNPVlanTagRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleTable.setStatus("deprecated")
_AlaDaUNPVlanTagRuleEntry_Object = MibTableRow
alaDaUNPVlanTagRuleEntry = _AlaDaUNPVlanTagRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 5, 1)
)
alaDaUNPVlanTagRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVlanTagRuleVlan"),
)
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleEntry.setStatus("deprecated")


class _AlaDaUNPVlanTagRuleVlan_Type(Integer32):
    """Custom type alaDaUNPVlanTagRuleVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPVlanTagRuleVlan_Type.__name__ = "Integer32"
_AlaDaUNPVlanTagRuleVlan_Object = MibTableColumn
alaDaUNPVlanTagRuleVlan = _AlaDaUNPVlanTagRuleVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 5, 1, 1),
    _AlaDaUNPVlanTagRuleVlan_Type()
)
alaDaUNPVlanTagRuleVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleVlan.setStatus("deprecated")


class _AlaDaUNPVlanTagRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPVlanTagRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPVlanTagRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVlanTagRuleProfileName_Object = MibTableColumn
alaDaUNPVlanTagRuleProfileName = _AlaDaUNPVlanTagRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 5, 1, 2),
    _AlaDaUNPVlanTagRuleProfileName_Type()
)
alaDaUNPVlanTagRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleProfileName.setStatus("deprecated")
_AlaDaUNPVlanTagRuleRowStatus_Type = RowStatus
_AlaDaUNPVlanTagRuleRowStatus_Object = MibTableColumn
alaDaUNPVlanTagRuleRowStatus = _AlaDaUNPVlanTagRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 5, 1, 3),
    _AlaDaUNPVlanTagRuleRowStatus_Type()
)
alaDaUNPVlanTagRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPVlanTagRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPVlanTagRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPVlanTagRuleMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPVlanTagRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPVlanTagRuleMCLagConfigStatus = _AlaDaUNPVlanTagRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 5, 1, 4),
    _AlaDaUNPVlanTagRuleMCLagConfigStatus_Type()
)
alaDaUNPVlanTagRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleMCLagConfigStatus.setStatus("deprecated")
_AlaDaMacUserTable_Object = MibTable
alaDaMacUserTable = _AlaDaMacUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaDaMacUserTable.setStatus("current")
_AlaDaMacUserEntry_Object = MibTableRow
alaDaMacUserEntry = _AlaDaMacUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1)
)
alaDaMacUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacUserIntfNum"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacUserMACAddress"),
)
if mibBuilder.loadTexts:
    alaDaMacUserEntry.setStatus("current")
_AlaDaMacUserIntfNum_Type = InterfaceIndex
_AlaDaMacUserIntfNum_Object = MibTableColumn
alaDaMacUserIntfNum = _AlaDaMacUserIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 1),
    _AlaDaMacUserIntfNum_Type()
)
alaDaMacUserIntfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacUserIntfNum.setStatus("current")
_AlaDaMacUserMACAddress_Type = MacAddress
_AlaDaMacUserMACAddress_Object = MibTableColumn
alaDaMacUserMACAddress = _AlaDaMacUserMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 2),
    _AlaDaMacUserMACAddress_Type()
)
alaDaMacUserMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacUserMACAddress.setStatus("current")


class _AlaDaMacUserVlanID_Type(Integer32):
    """Custom type alaDaMacUserVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDaMacUserVlanID_Type.__name__ = "Integer32"
_AlaDaMacUserVlanID_Object = MibTableColumn
alaDaMacUserVlanID = _AlaDaMacUserVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 3),
    _AlaDaMacUserVlanID_Type()
)
alaDaMacUserVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserVlanID.setStatus("current")


class _AlaDaAuthenticationStatus_Type(Integer32):
    """Custom type alaDaAuthenticationStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("authenticated", 3),
          ("failed", 4),
          ("failedTimeout", 5),
          ("failedNoServer", 6),
          ("failedNoResources", 7))
    )


_AlaDaAuthenticationStatus_Type.__name__ = "Integer32"
_AlaDaAuthenticationStatus_Object = MibTableColumn
alaDaAuthenticationStatus = _AlaDaAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 4),
    _AlaDaAuthenticationStatus_Type()
)
alaDaAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaAuthenticationStatus.setStatus("current")
_AlaDaMacUserIpAddress_Type = IpAddress
_AlaDaMacUserIpAddress_Object = MibTableColumn
alaDaMacUserIpAddress = _AlaDaMacUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 5),
    _AlaDaMacUserIpAddress_Type()
)
alaDaMacUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserIpAddress.setStatus("current")
_AlaDaMacUserUnpUsed_Type = SnmpAdminString
_AlaDaMacUserUnpUsed_Object = MibTableColumn
alaDaMacUserUnpUsed = _AlaDaMacUserUnpUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 6),
    _AlaDaMacUserUnpUsed_Type()
)
alaDaMacUserUnpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserUnpUsed.setStatus("current")
_AlaDaMacUserLoginTimeStamp_Type = DateAndTime
_AlaDaMacUserLoginTimeStamp_Object = MibTableColumn
alaDaMacUserLoginTimeStamp = _AlaDaMacUserLoginTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 7),
    _AlaDaMacUserLoginTimeStamp_Type()
)
alaDaMacUserLoginTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserLoginTimeStamp.setStatus("current")


class _AlaDaMacUserAuthtype_Type(Integer32):
    """Custom type alaDaMacUserAuthtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macAuthentication", 0),
          ("others", 1),
          ("onexAuthentication", 2))
    )


_AlaDaMacUserAuthtype_Type.__name__ = "Integer32"
_AlaDaMacUserAuthtype_Object = MibTableColumn
alaDaMacUserAuthtype = _AlaDaMacUserAuthtype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 8),
    _AlaDaMacUserAuthtype_Type()
)
alaDaMacUserAuthtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserAuthtype.setStatus("current")
_AlaDaMacUserClassificationSource_Type = AlaDaClassificationPolicyType
_AlaDaMacUserClassificationSource_Object = MibTableColumn
alaDaMacUserClassificationSource = _AlaDaMacUserClassificationSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 9),
    _AlaDaMacUserClassificationSource_Type()
)
alaDaMacUserClassificationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserClassificationSource.setStatus("current")
_AlaDaMacUserName_Type = SnmpAdminString
_AlaDaMacUserName_Object = MibTableColumn
alaDaMacUserName = _AlaDaMacUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 6, 1, 10),
    _AlaDaMacUserName_Type()
)
alaDaMacUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserName.setStatus("current")
_AlaDaUNPPortTable_Object = MibTable
alaDaUNPPortTable = _AlaDaUNPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaDaUNPPortTable.setStatus("current")
_AlaDaUNPPortEntry_Object = MibTableRow
alaDaUNPPortEntry = _AlaDaUNPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1)
)
alaDaUNPPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortIfIndex"),
)
if mibBuilder.loadTexts:
    alaDaUNPPortEntry.setStatus("current")
_AlaDaUNPPortIfIndex_Type = InterfaceIndexOrZero
_AlaDaUNPPortIfIndex_Object = MibTableColumn
alaDaUNPPortIfIndex = _AlaDaUNPPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 1),
    _AlaDaUNPPortIfIndex_Type()
)
alaDaUNPPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUNPPortIfIndex.setStatus("current")


class _AlaDaUNPPortDefaultProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortDefaultProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortDefaultProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortDefaultProfileName_Object = MibTableColumn
alaDaUNPPortDefaultProfileName = _AlaDaUNPPortDefaultProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 2),
    _AlaDaUNPPortDefaultProfileName_Type()
)
alaDaUNPPortDefaultProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortDefaultProfileName.setStatus("current")


class _AlaDaUNPPortPassAltProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortPassAltProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortPassAltProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortPassAltProfileName_Object = MibTableColumn
alaDaUNPPortPassAltProfileName = _AlaDaUNPPortPassAltProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 3),
    _AlaDaUNPPortPassAltProfileName_Type()
)
alaDaUNPPortPassAltProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortPassAltProfileName.setStatus("current")
_AlaDaUNPPortRowStatus_Type = RowStatus
_AlaDaUNPPortRowStatus_Object = MibTableColumn
alaDaUNPPortRowStatus = _AlaDaUNPPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 4),
    _AlaDaUNPPortRowStatus_Type()
)
alaDaUNPPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortRowStatus.setStatus("current")


class _AlaDaUNPPortMacAuthFlag_Type(Integer32):
    """Custom type alaDaUNPPortMacAuthFlag based on Integer32"""
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


_AlaDaUNPPortMacAuthFlag_Type.__name__ = "Integer32"
_AlaDaUNPPortMacAuthFlag_Object = MibTableColumn
alaDaUNPPortMacAuthFlag = _AlaDaUNPPortMacAuthFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 5),
    _AlaDaUNPPortMacAuthFlag_Type()
)
alaDaUNPPortMacAuthFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortMacAuthFlag.setStatus("current")


class _AlaDaUNPPortClassificationFlag_Type(Integer32):
    """Custom type alaDaUNPPortClassificationFlag based on Integer32"""
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


_AlaDaUNPPortClassificationFlag_Type.__name__ = "Integer32"
_AlaDaUNPPortClassificationFlag_Object = MibTableColumn
alaDaUNPPortClassificationFlag = _AlaDaUNPPortClassificationFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 6),
    _AlaDaUNPPortClassificationFlag_Type()
)
alaDaUNPPortClassificationFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortClassificationFlag.setStatus("current")


class _AlaDaUNPPortTrustTagStatus_Type(Integer32):
    """Custom type alaDaUNPPortTrustTagStatus based on Integer32"""
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


_AlaDaUNPPortTrustTagStatus_Type.__name__ = "Integer32"
_AlaDaUNPPortTrustTagStatus_Object = MibTableColumn
alaDaUNPPortTrustTagStatus = _AlaDaUNPPortTrustTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 7),
    _AlaDaUNPPortTrustTagStatus_Type()
)
alaDaUNPPortTrustTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTrustTagStatus.setStatus("current")


class _AlaDaUNPPortMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPPortMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPPortMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPPortMCLagConfigStatus_Object = MibTableColumn
alaDaUNPPortMCLagConfigStatus = _AlaDaUNPPortMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 8),
    _AlaDaUNPPortMCLagConfigStatus_Type()
)
alaDaUNPPortMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortMCLagConfigStatus.setStatus("current")


class _AlaDaUNPPortCustomerDomainId_Type(Unsigned32):
    """Custom type alaDaUNPPortCustomerDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPPortCustomerDomainId_Type.__name__ = "Unsigned32"
_AlaDaUNPPortCustomerDomainId_Object = MibTableColumn
alaDaUNPPortCustomerDomainId = _AlaDaUNPPortCustomerDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 9),
    _AlaDaUNPPortCustomerDomainId_Type()
)
alaDaUNPPortCustomerDomainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortCustomerDomainId.setStatus("deprecated")


class _AlaDaUNPPortType_Type(Integer32):
    """Custom type alaDaUNPPortType based on Integer32"""
    defaultValue = 1

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
        *(("bridgePort", 1),
          ("spbAccessPort", 2),
          ("edge", 3),
          ("vxlanAccessPort", 4),
          ("accessPort", 5))
    )


_AlaDaUNPPortType_Type.__name__ = "Integer32"
_AlaDaUNPPortType_Object = MibTableColumn
alaDaUNPPortType = _AlaDaUNPPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 10),
    _AlaDaUNPPortType_Type()
)
alaDaUNPPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortType.setStatus("current")


class _AlaDaUNPPortPassAltSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortPassAltSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortPassAltSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortPassAltSpbProfileName_Object = MibTableColumn
alaDaUNPPortPassAltSpbProfileName = _AlaDaUNPPortPassAltSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 11),
    _AlaDaUNPPortPassAltSpbProfileName_Type()
)
alaDaUNPPortPassAltSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortPassAltSpbProfileName.setStatus("deprecated")


class _AlaDaUNPPortDefaultSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortDefaultSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortDefaultSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortDefaultSpbProfileName_Object = MibTableColumn
alaDaUNPPortDefaultSpbProfileName = _AlaDaUNPPortDefaultSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 12),
    _AlaDaUNPPortDefaultSpbProfileName_Type()
)
alaDaUNPPortDefaultSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortDefaultSpbProfileName.setStatus("deprecated")


class _AlaDaUNPPortDefaultEdgeProfName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortDefaultEdgeProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortDefaultEdgeProfName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortDefaultEdgeProfName_Object = MibTableColumn
alaDaUNPPortDefaultEdgeProfName = _AlaDaUNPPortDefaultEdgeProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 13),
    _AlaDaUNPPortDefaultEdgeProfName_Type()
)
alaDaUNPPortDefaultEdgeProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortDefaultEdgeProfName.setStatus("deprecated")


class _AlaDaUNPPortMacPassEdgeProfName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortMacPassEdgeProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortMacPassEdgeProfName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortMacPassEdgeProfName_Object = MibTableColumn
alaDaUNPPortMacPassEdgeProfName = _AlaDaUNPPortMacPassEdgeProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 14),
    _AlaDaUNPPortMacPassEdgeProfName_Type()
)
alaDaUNPPortMacPassEdgeProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortMacPassEdgeProfName.setStatus("deprecated")


class _AlaDaUNPPort8021XEdgeProfName_Type(SnmpAdminString):
    """Custom type alaDaUNPPort8021XEdgeProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPort8021XEdgeProfName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPort8021XEdgeProfName_Object = MibTableColumn
alaDaUNPPort8021XEdgeProfName = _AlaDaUNPPort8021XEdgeProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 15),
    _AlaDaUNPPort8021XEdgeProfName_Type()
)
alaDaUNPPort8021XEdgeProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XEdgeProfName.setStatus("deprecated")


class _AlaDaUNPPort8021XAuthStatus_Type(Integer32):
    """Custom type alaDaUNPPort8021XAuthStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPort8021XAuthStatus_Type.__name__ = "Integer32"
_AlaDaUNPPort8021XAuthStatus_Object = MibTableColumn
alaDaUNPPort8021XAuthStatus = _AlaDaUNPPort8021XAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 16),
    _AlaDaUNPPort8021XAuthStatus_Type()
)
alaDaUNPPort8021XAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XAuthStatus.setStatus("current")


class _AlaDaUNPPort8021XTxPeriodStatus_Type(Integer32):
    """Custom type alaDaUNPPort8021XTxPeriodStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPort8021XTxPeriodStatus_Type.__name__ = "Integer32"
_AlaDaUNPPort8021XTxPeriodStatus_Object = MibTableColumn
alaDaUNPPort8021XTxPeriodStatus = _AlaDaUNPPort8021XTxPeriodStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 17),
    _AlaDaUNPPort8021XTxPeriodStatus_Type()
)
alaDaUNPPort8021XTxPeriodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XTxPeriodStatus.setStatus("deprecated")


class _AlaDaUNPPort8021XTxPeriod_Type(Integer32):
    """Custom type alaDaUNPPort8021XTxPeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AlaDaUNPPort8021XTxPeriod_Type.__name__ = "Integer32"
_AlaDaUNPPort8021XTxPeriod_Object = MibTableColumn
alaDaUNPPort8021XTxPeriod = _AlaDaUNPPort8021XTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 18),
    _AlaDaUNPPort8021XTxPeriod_Type()
)
alaDaUNPPort8021XTxPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XTxPeriod.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XTxPeriod.setUnits("seconds")


class _AlaDaUNPPort8021XSuppTimeoutStatus_Type(Integer32):
    """Custom type alaDaUNPPort8021XSuppTimeoutStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPort8021XSuppTimeoutStatus_Type.__name__ = "Integer32"
_AlaDaUNPPort8021XSuppTimeoutStatus_Object = MibTableColumn
alaDaUNPPort8021XSuppTimeoutStatus = _AlaDaUNPPort8021XSuppTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 19),
    _AlaDaUNPPort8021XSuppTimeoutStatus_Type()
)
alaDaUNPPort8021XSuppTimeoutStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XSuppTimeoutStatus.setStatus("deprecated")


class _AlaDaUNPPort8021XSuppTimeOut_Type(Integer32):
    """Custom type alaDaUNPPort8021XSuppTimeOut based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AlaDaUNPPort8021XSuppTimeOut_Type.__name__ = "Integer32"
_AlaDaUNPPort8021XSuppTimeOut_Object = MibTableColumn
alaDaUNPPort8021XSuppTimeOut = _AlaDaUNPPort8021XSuppTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 20),
    _AlaDaUNPPort8021XSuppTimeOut_Type()
)
alaDaUNPPort8021XSuppTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XSuppTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XSuppTimeOut.setUnits("seconds")


class _AlaDaUNPPort8021XMaxReqStatus_Type(Integer32):
    """Custom type alaDaUNPPort8021XMaxReqStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPort8021XMaxReqStatus_Type.__name__ = "Integer32"
_AlaDaUNPPort8021XMaxReqStatus_Object = MibTableColumn
alaDaUNPPort8021XMaxReqStatus = _AlaDaUNPPort8021XMaxReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 21),
    _AlaDaUNPPort8021XMaxReqStatus_Type()
)
alaDaUNPPort8021XMaxReqStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XMaxReqStatus.setStatus("deprecated")


class _AlaDaUNPPort8021XMaxReq_Type(Integer32):
    """Custom type alaDaUNPPort8021XMaxReq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaDaUNPPort8021XMaxReq_Type.__name__ = "Integer32"
_AlaDaUNPPort8021XMaxReq_Object = MibTableColumn
alaDaUNPPort8021XMaxReq = _AlaDaUNPPort8021XMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 22),
    _AlaDaUNPPort8021XMaxReq_Type()
)
alaDaUNPPort8021XMaxReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XMaxReq.setStatus("current")


class _AlaDaUNPPortGroupId_Type(Integer32):
    """Custom type alaDaUNPPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDaUNPPortGroupId_Type.__name__ = "Integer32"
_AlaDaUNPPortGroupId_Object = MibTableColumn
alaDaUNPPortGroupId = _AlaDaUNPPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 23),
    _AlaDaUNPPortGroupId_Type()
)
alaDaUNPPortGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortGroupId.setStatus("deprecated")


class _AlaDaUNPPortAaaProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPPortAaaProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortAaaProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortAaaProfile_Object = MibTableColumn
alaDaUNPPortAaaProfile = _AlaDaUNPPortAaaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 24),
    _AlaDaUNPPortAaaProfile_Type()
)
alaDaUNPPortAaaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortAaaProfile.setStatus("current")


class _AlaDaUNPPortEdgeTemplate_Type(SnmpAdminString):
    """Custom type alaDaUNPPortEdgeTemplate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortEdgeTemplate_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortEdgeTemplate_Object = MibTableColumn
alaDaUNPPortEdgeTemplate = _AlaDaUNPPortEdgeTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 25),
    _AlaDaUNPPortEdgeTemplate_Type()
)
alaDaUNPPortEdgeTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortEdgeTemplate.setStatus("deprecated")


class _AlaDaUNPPortRedirectPortBounce_Type(Integer32):
    """Custom type alaDaUNPPortRedirectPortBounce based on Integer32"""
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


_AlaDaUNPPortRedirectPortBounce_Type.__name__ = "Integer32"
_AlaDaUNPPortRedirectPortBounce_Object = MibTableColumn
alaDaUNPPortRedirectPortBounce = _AlaDaUNPPortRedirectPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 26),
    _AlaDaUNPPortRedirectPortBounce_Type()
)
alaDaUNPPortRedirectPortBounce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortRedirectPortBounce.setStatus("current")


class _AlaDaUNPPort8021XFailurePolicy_Type(Integer32):
    """Custom type alaDaUNPPort8021XFailurePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("macAuth", 2))
    )


_AlaDaUNPPort8021XFailurePolicy_Type.__name__ = "Integer32"
_AlaDaUNPPort8021XFailurePolicy_Object = MibTableColumn
alaDaUNPPort8021XFailurePolicy = _AlaDaUNPPort8021XFailurePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 27),
    _AlaDaUNPPort8021XFailurePolicy_Type()
)
alaDaUNPPort8021XFailurePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XFailurePolicy.setStatus("current")


class _AlaDaUNPPort8021XBypassStatus_Type(Integer32):
    """Custom type alaDaUNPPort8021XBypassStatus based on Integer32"""
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


_AlaDaUNPPort8021XBypassStatus_Type.__name__ = "Integer32"
_AlaDaUNPPort8021XBypassStatus_Object = MibTableColumn
alaDaUNPPort8021XBypassStatus = _AlaDaUNPPort8021XBypassStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 28),
    _AlaDaUNPPort8021XBypassStatus_Type()
)
alaDaUNPPort8021XBypassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XBypassStatus.setStatus("current")


class _AlaDaUNPPortMacAllowEap_Type(Integer32):
    """Custom type alaDaUNPPortMacAllowEap based on Integer32"""
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
        *(("pass", 1),
          ("fail", 2),
          ("noauth", 3),
          ("none", 4))
    )


_AlaDaUNPPortMacAllowEap_Type.__name__ = "Integer32"
_AlaDaUNPPortMacAllowEap_Object = MibTableColumn
alaDaUNPPortMacAllowEap = _AlaDaUNPPortMacAllowEap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 29),
    _AlaDaUNPPortMacAllowEap_Type()
)
alaDaUNPPortMacAllowEap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortMacAllowEap.setStatus("current")


class _AlaDaUNPPortAdminControlledDirections_Type(Integer32):
    """Custom type alaDaUNPPortAdminControlledDirections based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("in", 2),
          ("noVal", 3))
    )


_AlaDaUNPPortAdminControlledDirections_Type.__name__ = "Integer32"
_AlaDaUNPPortAdminControlledDirections_Object = MibTableColumn
alaDaUNPPortAdminControlledDirections = _AlaDaUNPPortAdminControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 30),
    _AlaDaUNPPortAdminControlledDirections_Type()
)
alaDaUNPPortAdminControlledDirections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortAdminControlledDirections.setStatus("current")


class _AlaDaUNPPortAdminControlledOperDirections_Type(Integer32):
    """Custom type alaDaUNPPortAdminControlledOperDirections based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("in", 2),
          ("noVal", 3))
    )


_AlaDaUNPPortAdminControlledOperDirections_Type.__name__ = "Integer32"
_AlaDaUNPPortAdminControlledOperDirections_Object = MibTableColumn
alaDaUNPPortAdminControlledOperDirections = _AlaDaUNPPortAdminControlledOperDirections_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 31),
    _AlaDaUNPPortAdminControlledOperDirections_Type()
)
alaDaUNPPortAdminControlledOperDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortAdminControlledOperDirections.setStatus("current")


class _AlaDaUNPPort8021XPassAltUserNetProfName_Type(SnmpAdminString):
    """Custom type alaDaUNPPort8021XPassAltUserNetProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPort8021XPassAltUserNetProfName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPort8021XPassAltUserNetProfName_Object = MibTableColumn
alaDaUNPPort8021XPassAltUserNetProfName = _AlaDaUNPPort8021XPassAltUserNetProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 32),
    _AlaDaUNPPort8021XPassAltUserNetProfName_Type()
)
alaDaUNPPort8021XPassAltUserNetProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XPassAltUserNetProfName.setStatus("deprecated")


class _AlaDaUNPPort8021XPassAltSpbProfName_Type(SnmpAdminString):
    """Custom type alaDaUNPPort8021XPassAltSpbProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPort8021XPassAltSpbProfName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPort8021XPassAltSpbProfName_Object = MibTableColumn
alaDaUNPPort8021XPassAltSpbProfName = _AlaDaUNPPort8021XPassAltSpbProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 33),
    _AlaDaUNPPort8021XPassAltSpbProfName_Type()
)
alaDaUNPPort8021XPassAltSpbProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XPassAltSpbProfName.setStatus("deprecated")


class _AlaDaUNPPort8021XPassAltVxlanProfName_Type(SnmpAdminString):
    """Custom type alaDaUNPPort8021XPassAltVxlanProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPort8021XPassAltVxlanProfName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPort8021XPassAltVxlanProfName_Object = MibTableColumn
alaDaUNPPort8021XPassAltVxlanProfName = _AlaDaUNPPort8021XPassAltVxlanProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 34),
    _AlaDaUNPPort8021XPassAltVxlanProfName_Type()
)
alaDaUNPPort8021XPassAltVxlanProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XPassAltVxlanProfName.setStatus("deprecated")


class _AlaDaUNPPortPassAltVxlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortPassAltVxlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortPassAltVxlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortPassAltVxlanProfileName_Object = MibTableColumn
alaDaUNPPortPassAltVxlanProfileName = _AlaDaUNPPortPassAltVxlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 35),
    _AlaDaUNPPortPassAltVxlanProfileName_Type()
)
alaDaUNPPortPassAltVxlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortPassAltVxlanProfileName.setStatus("deprecated")


class _AlaDaUNPPortDefaultVxlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortDefaultVxlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortDefaultVxlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortDefaultVxlanProfileName_Object = MibTableColumn
alaDaUNPPortDefaultVxlanProfileName = _AlaDaUNPPortDefaultVxlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 36),
    _AlaDaUNPPortDefaultVxlanProfileName_Type()
)
alaDaUNPPortDefaultVxlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortDefaultVxlanProfileName.setStatus("deprecated")


class _AlaDaUNPPortAFDConfig_Type(Integer32):
    """Custom type alaDaUNPPortAFDConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("autoFabric", 2))
    )


_AlaDaUNPPortAFDConfig_Type.__name__ = "Integer32"
_AlaDaUNPPortAFDConfig_Object = MibTableColumn
alaDaUNPPortAFDConfig = _AlaDaUNPPortAFDConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 37),
    _AlaDaUNPPortAFDConfig_Type()
)
alaDaUNPPortAFDConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortAFDConfig.setStatus("current")


class _AlaDaUNPPortMaxIngressBw_Type(Integer32):
    """Custom type alaDaUNPPortMaxIngressBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10485760),
    )


_AlaDaUNPPortMaxIngressBw_Type.__name__ = "Integer32"
_AlaDaUNPPortMaxIngressBw_Object = MibTableColumn
alaDaUNPPortMaxIngressBw = _AlaDaUNPPortMaxIngressBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 38),
    _AlaDaUNPPortMaxIngressBw_Type()
)
alaDaUNPPortMaxIngressBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortMaxIngressBw.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPPortMaxIngressBw.setUnits("kilobits per second")


class _AlaDaUNPPortMaxIngressBwSource_Type(Integer32):
    """Custom type alaDaUNPPortMaxIngressBwSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("unp", 2),
          ("qos", 3))
    )


_AlaDaUNPPortMaxIngressBwSource_Type.__name__ = "Integer32"
_AlaDaUNPPortMaxIngressBwSource_Object = MibTableColumn
alaDaUNPPortMaxIngressBwSource = _AlaDaUNPPortMaxIngressBwSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 39),
    _AlaDaUNPPortMaxIngressBwSource_Type()
)
alaDaUNPPortMaxIngressBwSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortMaxIngressBwSource.setStatus("current")


class _AlaDaUNPPortMaxEgressBw_Type(Integer32):
    """Custom type alaDaUNPPortMaxEgressBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10485760),
    )


_AlaDaUNPPortMaxEgressBw_Type.__name__ = "Integer32"
_AlaDaUNPPortMaxEgressBw_Object = MibTableColumn
alaDaUNPPortMaxEgressBw = _AlaDaUNPPortMaxEgressBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 40),
    _AlaDaUNPPortMaxEgressBw_Type()
)
alaDaUNPPortMaxEgressBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortMaxEgressBw.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPPortMaxEgressBw.setUnits("kilobits per second")


class _AlaDaUNPPortMaxEgressBwSource_Type(Integer32):
    """Custom type alaDaUNPPortMaxEgressBwSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("unp", 2),
          ("qos", 3))
    )


_AlaDaUNPPortMaxEgressBwSource_Type.__name__ = "Integer32"
_AlaDaUNPPortMaxEgressBwSource_Object = MibTableColumn
alaDaUNPPortMaxEgressBwSource = _AlaDaUNPPortMaxEgressBwSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 41),
    _AlaDaUNPPortMaxEgressBwSource_Type()
)
alaDaUNPPortMaxEgressBwSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortMaxEgressBwSource.setStatus("current")


class _AlaDaUNPPortMaxIngressDepth_Type(Integer32):
    """Custom type alaDaUNPPortMaxIngressDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16384),
    )


_AlaDaUNPPortMaxIngressDepth_Type.__name__ = "Integer32"
_AlaDaUNPPortMaxIngressDepth_Object = MibTableColumn
alaDaUNPPortMaxIngressDepth = _AlaDaUNPPortMaxIngressDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 42),
    _AlaDaUNPPortMaxIngressDepth_Type()
)
alaDaUNPPortMaxIngressDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortMaxIngressDepth.setStatus("current")


class _AlaDaUNPPortMaxEgressDepth_Type(Integer32):
    """Custom type alaDaUNPPortMaxEgressDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16384),
    )


_AlaDaUNPPortMaxEgressDepth_Type.__name__ = "Integer32"
_AlaDaUNPPortMaxEgressDepth_Object = MibTableColumn
alaDaUNPPortMaxEgressDepth = _AlaDaUNPPortMaxEgressDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 43),
    _AlaDaUNPPortMaxEgressDepth_Type()
)
alaDaUNPPortMaxEgressDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortMaxEgressDepth.setStatus("current")


class _AlaDaUNPPortIngressSourceProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPPortIngressSourceProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortIngressSourceProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortIngressSourceProfile_Object = MibTableColumn
alaDaUNPPortIngressSourceProfile = _AlaDaUNPPortIngressSourceProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 44),
    _AlaDaUNPPortIngressSourceProfile_Type()
)
alaDaUNPPortIngressSourceProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortIngressSourceProfile.setStatus("current")


class _AlaDaUNPPortEgressSourceProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPPortEgressSourceProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortEgressSourceProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortEgressSourceProfile_Object = MibTableColumn
alaDaUNPPortEgressSourceProfile = _AlaDaUNPPortEgressSourceProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 45),
    _AlaDaUNPPortEgressSourceProfile_Type()
)
alaDaUNPPortEgressSourceProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortEgressSourceProfile.setStatus("current")


class _AlaDaUNPPortForceL3Learning_Type(Integer32):
    """Custom type alaDaUNPPortForceL3Learning based on Integer32"""
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


_AlaDaUNPPortForceL3Learning_Type.__name__ = "Integer32"
_AlaDaUNPPortForceL3Learning_Object = MibTableColumn
alaDaUNPPortForceL3Learning = _AlaDaUNPPortForceL3Learning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 46),
    _AlaDaUNPPortForceL3Learning_Type()
)
alaDaUNPPortForceL3Learning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortForceL3Learning.setStatus("current")


class _AlaDaUNPPortForceL3LearningPortBounce_Type(Integer32):
    """Custom type alaDaUNPPortForceL3LearningPortBounce based on Integer32"""
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


_AlaDaUNPPortForceL3LearningPortBounce_Type.__name__ = "Integer32"
_AlaDaUNPPortForceL3LearningPortBounce_Object = MibTableColumn
alaDaUNPPortForceL3LearningPortBounce = _AlaDaUNPPortForceL3LearningPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 47),
    _AlaDaUNPPortForceL3LearningPortBounce_Type()
)
alaDaUNPPortForceL3LearningPortBounce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortForceL3LearningPortBounce.setStatus("current")


class _AlaDaUNPPort8021XPassAltProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPort8021XPassAltProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPort8021XPassAltProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPort8021XPassAltProfileName_Object = MibTableColumn
alaDaUNPPort8021XPassAltProfileName = _AlaDaUNPPort8021XPassAltProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 48),
    _AlaDaUNPPort8021XPassAltProfileName_Type()
)
alaDaUNPPort8021XPassAltProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPort8021XPassAltProfileName.setStatus("current")


class _AlaDaUNPPortPortTemplateName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortPortTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortPortTemplateName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortPortTemplateName_Object = MibTableColumn
alaDaUNPPortPortTemplateName = _AlaDaUNPPortPortTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 49),
    _AlaDaUNPPortPortTemplateName_Type()
)
alaDaUNPPortPortTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortPortTemplateName.setStatus("current")


class _AlaDaUNPPortDomainID_Type(Unsigned32):
    """Custom type alaDaUNPPortDomainID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPPortDomainID_Type.__name__ = "Unsigned32"
_AlaDaUNPPortDomainID_Object = MibTableColumn
alaDaUNPPortDomainID = _AlaDaUNPPortDomainID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 50),
    _AlaDaUNPPortDomainID_Type()
)
alaDaUNPPortDomainID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortDomainID.setStatus("current")


class _AlaDaUNPPortAdminState_Type(Integer32):
    """Custom type alaDaUNPPortAdminState based on Integer32"""
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


_AlaDaUNPPortAdminState_Type.__name__ = "Integer32"
_AlaDaUNPPortAdminState_Object = MibTableColumn
alaDaUNPPortAdminState = _AlaDaUNPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 51),
    _AlaDaUNPPortAdminState_Type()
)
alaDaUNPPortAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortAdminState.setStatus("current")


class _AlaDaUNPPortDynamicService_Type(Integer32):
    """Custom type alaDaUNPPortDynamicService based on Integer32"""
    defaultValue = 1

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
          ("spb", 2),
          ("vxlan", 3),
          ("vpls", 4))
    )


_AlaDaUNPPortDynamicService_Type.__name__ = "Integer32"
_AlaDaUNPPortDynamicService_Object = MibTableColumn
alaDaUNPPortDynamicService = _AlaDaUNPPortDynamicService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 52),
    _AlaDaUNPPortDynamicService_Type()
)
alaDaUNPPortDynamicService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortDynamicService.setStatus("current")


class _AlaDaUNPPortPVlanPortType_Type(Integer32):
    """Custom type alaDaUNPPortPVlanPortType based on Integer32"""
    defaultValue = 1

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
          ("community", 2),
          ("isolated", 3))
    )


_AlaDaUNPPortPVlanPortType_Type.__name__ = "Integer32"
_AlaDaUNPPortPVlanPortType_Object = MibTableColumn
alaDaUNPPortPVlanPortType = _AlaDaUNPPortPVlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 53),
    _AlaDaUNPPortPVlanPortType_Type()
)
alaDaUNPPortPVlanPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortPVlanPortType.setStatus("current")


class _AlaDaUNPPortL2Profile_Type(SnmpAdminString):
    """Custom type alaDaUNPPortL2Profile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortL2Profile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortL2Profile_Object = MibTableColumn
alaDaUNPPortL2Profile = _AlaDaUNPPortL2Profile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 54),
    _AlaDaUNPPortL2Profile_Type()
)
alaDaUNPPortL2Profile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortL2Profile.setStatus("current")


class _AlaDaUNPPortApMode_Type(Integer32):
    """Custom type alaDaUNPPortApMode based on Integer32"""
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


_AlaDaUNPPortApMode_Type.__name__ = "Integer32"
_AlaDaUNPPortApMode_Object = MibTableColumn
alaDaUNPPortApMode = _AlaDaUNPPortApMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 55),
    _AlaDaUNPPortApMode_Type()
)
alaDaUNPPortApMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortApMode.setStatus("current")


class _AlaDaUNPPortApModeSecurity_Type(Integer32):
    """Custom type alaDaUNPPortApModeSecurity based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPortApModeSecurity_Type.__name__ = "Integer32"
_AlaDaUNPPortApModeSecurity_Object = MibTableColumn
alaDaUNPPortApModeSecurity = _AlaDaUNPPortApModeSecurity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 56),
    _AlaDaUNPPortApModeSecurity_Type()
)
alaDaUNPPortApModeSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortApModeSecurity.setStatus("current")


class _AlaDaUNPPortSwSuppSecureMode_Type(Integer32):
    """Custom type alaDaUNPPortSwSuppSecureMode based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPortSwSuppSecureMode_Type.__name__ = "Integer32"
_AlaDaUNPPortSwSuppSecureMode_Object = MibTableColumn
alaDaUNPPortSwSuppSecureMode = _AlaDaUNPPortSwSuppSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 57),
    _AlaDaUNPPortSwSuppSecureMode_Type()
)
alaDaUNPPortSwSuppSecureMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortSwSuppSecureMode.setStatus("current")


class _AlaDaUNPPortBpduLldpLearn_Type(Integer32):
    """Custom type alaDaUNPPortBpduLldpLearn based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPortBpduLldpLearn_Type.__name__ = "Integer32"
_AlaDaUNPPortBpduLldpLearn_Object = MibTableColumn
alaDaUNPPortBpduLldpLearn = _AlaDaUNPPortBpduLldpLearn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 7, 1, 58),
    _AlaDaUNPPortBpduLldpLearn_Type()
)
alaDaUNPPortBpduLldpLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortBpduLldpLearn.setStatus("current")
_AlaDaUNPGlobalConfiguration_ObjectIdentity = ObjectIdentity
alaDaUNPGlobalConfiguration = _AlaDaUNPGlobalConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8)
)


class _AlaDaUNPDynamicVlanConfigFlag_Type(Integer32):
    """Custom type alaDaUNPDynamicVlanConfigFlag based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPDynamicVlanConfigFlag_Type.__name__ = "Integer32"
_AlaDaUNPDynamicVlanConfigFlag_Object = MibScalar
alaDaUNPDynamicVlanConfigFlag = _AlaDaUNPDynamicVlanConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 1),
    _AlaDaUNPDynamicVlanConfigFlag_Type()
)
alaDaUNPDynamicVlanConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPDynamicVlanConfigFlag.setStatus("current")


class _AlaDaUNPAuthServerDownUnp_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthServerDownUnp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthServerDownUnp_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthServerDownUnp_Object = MibScalar
alaDaUNPAuthServerDownUnp = _AlaDaUNPAuthServerDownUnp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 2),
    _AlaDaUNPAuthServerDownUnp_Type()
)
alaDaUNPAuthServerDownUnp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownUnp.setStatus("deprecated")


class _AlaDaUNPAuthServerDownTimeout_Type(Integer32):
    """Custom type alaDaUNPAuthServerDownTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 43200),
    )


_AlaDaUNPAuthServerDownTimeout_Type.__name__ = "Integer32"
_AlaDaUNPAuthServerDownTimeout_Object = MibScalar
alaDaUNPAuthServerDownTimeout = _AlaDaUNPAuthServerDownTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 3),
    _AlaDaUNPAuthServerDownTimeout_Type()
)
alaDaUNPAuthServerDownTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownTimeout.setUnits("Seconds")


class _AlaDaUNPDynamicVlanMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPDynamicVlanMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPDynamicVlanMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPDynamicVlanMCLagConfigStatus_Object = MibScalar
alaDaUNPDynamicVlanMCLagConfigStatus = _AlaDaUNPDynamicVlanMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 4),
    _AlaDaUNPDynamicVlanMCLagConfigStatus_Type()
)
alaDaUNPDynamicVlanMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPDynamicVlanMCLagConfigStatus.setStatus("current")


class _AlaDaUNPAuthServerDownUNPMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPAuthServerDownUNPMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPAuthServerDownUNPMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPAuthServerDownUNPMCLagConfigStatus_Object = MibScalar
alaDaUNPAuthServerDownUNPMCLagConfigStatus = _AlaDaUNPAuthServerDownUNPMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 5),
    _AlaDaUNPAuthServerDownUNPMCLagConfigStatus_Type()
)
alaDaUNPAuthServerDownUNPMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownUNPMCLagConfigStatus.setStatus("current")


class _AlaDaUNPAuthServerDownTimeoutMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPAuthServerDownTimeoutMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPAuthServerDownTimeoutMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPAuthServerDownTimeoutMCLagConfigStatus_Object = MibScalar
alaDaUNPAuthServerDownTimeoutMCLagConfigStatus = _AlaDaUNPAuthServerDownTimeoutMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 6),
    _AlaDaUNPAuthServerDownTimeoutMCLagConfigStatus_Type()
)
alaDaUNPAuthServerDownTimeoutMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownTimeoutMCLagConfigStatus.setStatus("current")


class _AlaDaUNPDynamicProfileConfigFlag_Type(Integer32):
    """Custom type alaDaUNPDynamicProfileConfigFlag based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPDynamicProfileConfigFlag_Type.__name__ = "Integer32"
_AlaDaUNPDynamicProfileConfigFlag_Object = MibScalar
alaDaUNPDynamicProfileConfigFlag = _AlaDaUNPDynamicProfileConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 7),
    _AlaDaUNPDynamicProfileConfigFlag_Type()
)
alaDaUNPDynamicProfileConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPDynamicProfileConfigFlag.setStatus("current")


class _AlaDaUNPDynamicProfileConfigMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPDynamicProfileConfigMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPDynamicProfileConfigMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPDynamicProfileConfigMCLagConfigStatus_Object = MibScalar
alaDaUNPDynamicProfileConfigMCLagConfigStatus = _AlaDaUNPDynamicProfileConfigMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 8),
    _AlaDaUNPDynamicProfileConfigMCLagConfigStatus_Type()
)
alaDaUNPDynamicProfileConfigMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPDynamicProfileConfigMCLagConfigStatus.setStatus("current")


class _AlaDaUNPReloadVsiTypeDB_Type(Integer32):
    """Custom type alaDaUNPReloadVsiTypeDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("true", 1))
    )


_AlaDaUNPReloadVsiTypeDB_Type.__name__ = "Integer32"
_AlaDaUNPReloadVsiTypeDB_Object = MibScalar
alaDaUNPReloadVsiTypeDB = _AlaDaUNPReloadVsiTypeDB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 9),
    _AlaDaUNPReloadVsiTypeDB_Type()
)
alaDaUNPReloadVsiTypeDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPReloadVsiTypeDB.setStatus("current")


class _AlaDaUNPAuthSrvDownEdgeProfName_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthSrvDownEdgeProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthSrvDownEdgeProfName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthSrvDownEdgeProfName_Object = MibScalar
alaDaUNPAuthSrvDownEdgeProfName = _AlaDaUNPAuthSrvDownEdgeProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 10),
    _AlaDaUNPAuthSrvDownEdgeProfName_Type()
)
alaDaUNPAuthSrvDownEdgeProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthSrvDownEdgeProfName.setStatus("deprecated")


class _AlaDaUNPAuthServerDowneEdgeProfTimeout_Type(Integer32):
    """Custom type alaDaUNPAuthServerDowneEdgeProfTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_AlaDaUNPAuthServerDowneEdgeProfTimeout_Type.__name__ = "Integer32"
_AlaDaUNPAuthServerDowneEdgeProfTimeout_Object = MibScalar
alaDaUNPAuthServerDowneEdgeProfTimeout = _AlaDaUNPAuthServerDowneEdgeProfTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 11),
    _AlaDaUNPAuthServerDowneEdgeProfTimeout_Type()
)
alaDaUNPAuthServerDowneEdgeProfTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDowneEdgeProfTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDowneEdgeProfTimeout.setUnits("Seconds")


class _AlaDaUNPEdgeUserFlush_Type(TruthValue):
    """Custom type alaDaUNPEdgeUserFlush based on TruthValue"""
    defaultValue = 2


_AlaDaUNPEdgeUserFlush_Type.__name__ = "TruthValue"
_AlaDaUNPEdgeUserFlush_Object = MibScalar
alaDaUNPEdgeUserFlush = _AlaDaUNPEdgeUserFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 12),
    _AlaDaUNPEdgeUserFlush_Type()
)
alaDaUNPEdgeUserFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPEdgeUserFlush.setStatus("deprecated")


class _AlaDaUNP8021XEdgeUserFlush_Type(TruthValue):
    """Custom type alaDaUNP8021XEdgeUserFlush based on TruthValue"""
    defaultValue = 2


_AlaDaUNP8021XEdgeUserFlush_Type.__name__ = "TruthValue"
_AlaDaUNP8021XEdgeUserFlush_Object = MibScalar
alaDaUNP8021XEdgeUserFlush = _AlaDaUNP8021XEdgeUserFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 13),
    _AlaDaUNP8021XEdgeUserFlush_Type()
)
alaDaUNP8021XEdgeUserFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNP8021XEdgeUserFlush.setStatus("deprecated")


class _AlaDaUNPMacEdgeUserFlush_Type(TruthValue):
    """Custom type alaDaUNPMacEdgeUserFlush based on TruthValue"""
    defaultValue = 2


_AlaDaUNPMacEdgeUserFlush_Type.__name__ = "TruthValue"
_AlaDaUNPMacEdgeUserFlush_Object = MibScalar
alaDaUNPMacEdgeUserFlush = _AlaDaUNPMacEdgeUserFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 14),
    _AlaDaUNPMacEdgeUserFlush_Type()
)
alaDaUNPMacEdgeUserFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPMacEdgeUserFlush.setStatus("deprecated")


class _AlaDaUNPNoAuthEdgeUserFlush_Type(TruthValue):
    """Custom type alaDaUNPNoAuthEdgeUserFlush based on TruthValue"""
    defaultValue = 2


_AlaDaUNPNoAuthEdgeUserFlush_Type.__name__ = "TruthValue"
_AlaDaUNPNoAuthEdgeUserFlush_Object = MibScalar
alaDaUNPNoAuthEdgeUserFlush = _AlaDaUNPNoAuthEdgeUserFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 15),
    _AlaDaUNPNoAuthEdgeUserFlush_Type()
)
alaDaUNPNoAuthEdgeUserFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPNoAuthEdgeUserFlush.setStatus("deprecated")


class _AlaDaUNPRedirectPortBounce_Type(Integer32):
    """Custom type alaDaUNPRedirectPortBounce based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPRedirectPortBounce_Type.__name__ = "Integer32"
_AlaDaUNPRedirectPortBounce_Object = MibScalar
alaDaUNPRedirectPortBounce = _AlaDaUNPRedirectPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 16),
    _AlaDaUNPRedirectPortBounce_Type()
)
alaDaUNPRedirectPortBounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPRedirectPortBounce.setStatus("current")


class _AlaDaUNPRedirectPauseTimer_Type(Integer32):
    """Custom type alaDaUNPRedirectPauseTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 65535),
    )


_AlaDaUNPRedirectPauseTimer_Type.__name__ = "Integer32"
_AlaDaUNPRedirectPauseTimer_Object = MibScalar
alaDaUNPRedirectPauseTimer = _AlaDaUNPRedirectPauseTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 17),
    _AlaDaUNPRedirectPauseTimer_Type()
)
alaDaUNPRedirectPauseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPRedirectPauseTimer.setStatus("current")


class _AlaDaUNPRedirectProxyServerPort_Type(Integer32):
    """Custom type alaDaUNPRedirectProxyServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1024, 49151),
    )


_AlaDaUNPRedirectProxyServerPort_Type.__name__ = "Integer32"
_AlaDaUNPRedirectProxyServerPort_Object = MibScalar
alaDaUNPRedirectProxyServerPort = _AlaDaUNPRedirectProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 18),
    _AlaDaUNPRedirectProxyServerPort_Type()
)
alaDaUNPRedirectProxyServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPRedirectProxyServerPort.setStatus("current")


class _AlaDaUNPRedirectServerIPType_Type(InetAddressType):
    """Custom type alaDaUNPRedirectServerIPType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("dns", 16))
    )


_AlaDaUNPRedirectServerIPType_Type.__name__ = "InetAddressType"
_AlaDaUNPRedirectServerIPType_Object = MibScalar
alaDaUNPRedirectServerIPType = _AlaDaUNPRedirectServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 19),
    _AlaDaUNPRedirectServerIPType_Type()
)
alaDaUNPRedirectServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPRedirectServerIPType.setStatus("current")
_AlaDaUNPRedirectServerIP_Type = InetAddress
_AlaDaUNPRedirectServerIP_Object = MibScalar
alaDaUNPRedirectServerIP = _AlaDaUNPRedirectServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 20),
    _AlaDaUNPRedirectServerIP_Type()
)
alaDaUNPRedirectServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPRedirectServerIP.setStatus("current")


class _AlaDaUNPAuthSrvDownVxlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthSrvDownVxlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthSrvDownVxlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthSrvDownVxlanProfileName_Object = MibScalar
alaDaUNPAuthSrvDownVxlanProfileName = _AlaDaUNPAuthSrvDownVxlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 21),
    _AlaDaUNPAuthSrvDownVxlanProfileName_Type()
)
alaDaUNPAuthSrvDownVxlanProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthSrvDownVxlanProfileName.setStatus("deprecated")


class _AlaDaUNPAuthSrvDownVxlanProfileTimeout_Type(Integer32):
    """Custom type alaDaUNPAuthSrvDownVxlanProfileTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_AlaDaUNPAuthSrvDownVxlanProfileTimeout_Type.__name__ = "Integer32"
_AlaDaUNPAuthSrvDownVxlanProfileTimeout_Object = MibScalar
alaDaUNPAuthSrvDownVxlanProfileTimeout = _AlaDaUNPAuthSrvDownVxlanProfileTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 22),
    _AlaDaUNPAuthSrvDownVxlanProfileTimeout_Type()
)
alaDaUNPAuthSrvDownVxlanProfileTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthSrvDownVxlanProfileTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaDaUNPAuthSrvDownVxlanProfileTimeout.setUnits("Seconds")


class _AlaDaUNPForceL3Learning_Type(Integer32):
    """Custom type alaDaUNPForceL3Learning based on Integer32"""
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


_AlaDaUNPForceL3Learning_Type.__name__ = "Integer32"
_AlaDaUNPForceL3Learning_Object = MibScalar
alaDaUNPForceL3Learning = _AlaDaUNPForceL3Learning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 23),
    _AlaDaUNPForceL3Learning_Type()
)
alaDaUNPForceL3Learning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPForceL3Learning.setStatus("current")


class _AlaDaUNPForceL3LearningPortBounce_Type(Integer32):
    """Custom type alaDaUNPForceL3LearningPortBounce based on Integer32"""
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


_AlaDaUNPForceL3LearningPortBounce_Type.__name__ = "Integer32"
_AlaDaUNPForceL3LearningPortBounce_Object = MibScalar
alaDaUNPForceL3LearningPortBounce = _AlaDaUNPForceL3LearningPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 24),
    _AlaDaUNPForceL3LearningPortBounce_Type()
)
alaDaUNPForceL3LearningPortBounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPForceL3LearningPortBounce.setStatus("current")


class _AlaDaUNPAuthServerDownProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthServerDownProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthServerDownProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthServerDownProfile1_Object = MibScalar
alaDaUNPAuthServerDownProfile1 = _AlaDaUNPAuthServerDownProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 25),
    _AlaDaUNPAuthServerDownProfile1_Type()
)
alaDaUNPAuthServerDownProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownProfile1.setStatus("current")


class _AlaDaUNPAuthServerDownProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthServerDownProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthServerDownProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthServerDownProfile2_Object = MibScalar
alaDaUNPAuthServerDownProfile2 = _AlaDaUNPAuthServerDownProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 26),
    _AlaDaUNPAuthServerDownProfile2_Type()
)
alaDaUNPAuthServerDownProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownProfile2.setStatus("current")


class _AlaDaUNPAuthServerDownProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthServerDownProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthServerDownProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthServerDownProfile3_Object = MibScalar
alaDaUNPAuthServerDownProfile3 = _AlaDaUNPAuthServerDownProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 27),
    _AlaDaUNPAuthServerDownProfile3_Type()
)
alaDaUNPAuthServerDownProfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownProfile3.setStatus("current")


class _AlaDaUNPVlanUserFlush_Type(TruthValue):
    """Custom type alaDaUNPVlanUserFlush based on TruthValue"""
    defaultValue = 2


_AlaDaUNPVlanUserFlush_Type.__name__ = "TruthValue"
_AlaDaUNPVlanUserFlush_Object = MibScalar
alaDaUNPVlanUserFlush = _AlaDaUNPVlanUserFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 28),
    _AlaDaUNPVlanUserFlush_Type()
)
alaDaUNPVlanUserFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVlanUserFlush.setStatus("deprecated")


class _AlaDaUNP8021XPassThrough_Type(Integer32):
    """Custom type alaDaUNP8021XPassThrough based on Integer32"""
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


_AlaDaUNP8021XPassThrough_Type.__name__ = "Integer32"
_AlaDaUNP8021XPassThrough_Object = MibScalar
alaDaUNP8021XPassThrough = _AlaDaUNP8021XPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 29),
    _AlaDaUNP8021XPassThrough_Type()
)
alaDaUNP8021XPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNP8021XPassThrough.setStatus("current")


class _AlaDaUNPApMode_Type(Integer32):
    """Custom type alaDaUNPApMode based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPApMode_Type.__name__ = "Integer32"
_AlaDaUNPApMode_Object = MibScalar
alaDaUNPApMode = _AlaDaUNPApMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 30),
    _AlaDaUNPApMode_Type()
)
alaDaUNPApMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPApMode.setStatus("current")


class _AlaDaUNPServiceModule_Type(Integer32):
    """Custom type alaDaUNPServiceModule based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDaUNPServiceModule_Type.__name__ = "Integer32"
_AlaDaUNPServiceModule_Object = MibScalar
alaDaUNPServiceModule = _AlaDaUNPServiceModule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 31),
    _AlaDaUNPServiceModule_Type()
)
alaDaUNPServiceModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceModule.setStatus("current")


class _AlaDaUNPServiceBase_Type(Integer32):
    """Custom type alaDaUNPServiceBase based on Integer32"""
    defaultValue = 10000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_AlaDaUNPServiceBase_Type.__name__ = "Integer32"
_AlaDaUNPServiceBase_Object = MibScalar
alaDaUNPServiceBase = _AlaDaUNPServiceBase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 32),
    _AlaDaUNPServiceBase_Type()
)
alaDaUNPServiceBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceBase.setStatus("current")


class _AlaDaUNPServiceMulticastMode_Type(Integer32):
    """Custom type alaDaUNPServiceMulticastMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("headend", 1),
          ("tandem", 2),
          ("hybrid", 3))
    )


_AlaDaUNPServiceMulticastMode_Type.__name__ = "Integer32"
_AlaDaUNPServiceMulticastMode_Object = MibScalar
alaDaUNPServiceMulticastMode = _AlaDaUNPServiceMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 33),
    _AlaDaUNPServiceMulticastMode_Type()
)
alaDaUNPServiceMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceMulticastMode.setStatus("current")


class _AlaDaUNPServiceVlanXlation_Type(Integer32):
    """Custom type alaDaUNPServiceVlanXlation based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPServiceVlanXlation_Type.__name__ = "Integer32"
_AlaDaUNPServiceVlanXlation_Object = MibScalar
alaDaUNPServiceVlanXlation = _AlaDaUNPServiceVlanXlation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 34),
    _AlaDaUNPServiceVlanXlation_Type()
)
alaDaUNPServiceVlanXlation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceVlanXlation.setStatus("current")
_AlaDaUNPServiceMulticastGroup_Type = InetAddress
_AlaDaUNPServiceMulticastGroup_Object = MibScalar
alaDaUNPServiceMulticastGroup = _AlaDaUNPServiceMulticastGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 35),
    _AlaDaUNPServiceMulticastGroup_Type()
)
alaDaUNPServiceMulticastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceMulticastGroup.setStatus("deprecated")
_AlaDaUNPServiceFarEndIpList_Type = SnmpAdminString
_AlaDaUNPServiceFarEndIpList_Object = MibScalar
alaDaUNPServiceFarEndIpList = _AlaDaUNPServiceFarEndIpList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 36),
    _AlaDaUNPServiceFarEndIpList_Type()
)
alaDaUNPServiceFarEndIpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceFarEndIpList.setStatus("current")


class _AlaDaUNPIpv6Drop_Type(Integer32):
    """Custom type alaDaUNPIpv6Drop based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPIpv6Drop_Type.__name__ = "Integer32"
_AlaDaUNPIpv6Drop_Object = MibScalar
alaDaUNPIpv6Drop = _AlaDaUNPIpv6Drop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 37),
    _AlaDaUNPIpv6Drop_Type()
)
alaDaUNPIpv6Drop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPIpv6Drop.setStatus("current")


class _AlaDaUNPAuthServerDownVoiceProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthServerDownVoiceProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthServerDownVoiceProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthServerDownVoiceProfile1_Object = MibScalar
alaDaUNPAuthServerDownVoiceProfile1 = _AlaDaUNPAuthServerDownVoiceProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 38),
    _AlaDaUNPAuthServerDownVoiceProfile1_Type()
)
alaDaUNPAuthServerDownVoiceProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownVoiceProfile1.setStatus("current")


class _AlaDaUNPAuthServerDownVoiceProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthServerDownVoiceProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthServerDownVoiceProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthServerDownVoiceProfile2_Object = MibScalar
alaDaUNPAuthServerDownVoiceProfile2 = _AlaDaUNPAuthServerDownVoiceProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 39),
    _AlaDaUNPAuthServerDownVoiceProfile2_Type()
)
alaDaUNPAuthServerDownVoiceProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownVoiceProfile2.setStatus("current")


class _AlaDaUNPAuthServerDownVoiceProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthServerDownVoiceProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthServerDownVoiceProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthServerDownVoiceProfile3_Object = MibScalar
alaDaUNPAuthServerDownVoiceProfile3 = _AlaDaUNPAuthServerDownVoiceProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 40),
    _AlaDaUNPAuthServerDownVoiceProfile3_Type()
)
alaDaUNPAuthServerDownVoiceProfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownVoiceProfile3.setStatus("current")


class _AlaDaUNPDelayLearning_Type(Integer32):
    """Custom type alaDaUNPDelayLearning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AlaDaUNPDelayLearning_Type.__name__ = "Integer32"
_AlaDaUNPDelayLearning_Object = MibScalar
alaDaUNPDelayLearning = _AlaDaUNPDelayLearning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 41),
    _AlaDaUNPDelayLearning_Type()
)
alaDaUNPDelayLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPDelayLearning.setStatus("current")


class _AlaDaUNPAuthServerDownPortBounce_Type(Integer32):
    """Custom type alaDaUNPAuthServerDownPortBounce based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPAuthServerDownPortBounce_Type.__name__ = "Integer32"
_AlaDaUNPAuthServerDownPortBounce_Object = MibScalar
alaDaUNPAuthServerDownPortBounce = _AlaDaUNPAuthServerDownPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 42),
    _AlaDaUNPAuthServerDownPortBounce_Type()
)
alaDaUNPAuthServerDownPortBounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownPortBounce.setStatus("current")


class _AlaDaUNPMacMobility_Type(Integer32):
    """Custom type alaDaUNPMacMobility based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPMacMobility_Type.__name__ = "Integer32"
_AlaDaUNPMacMobility_Object = MibScalar
alaDaUNPMacMobility = _AlaDaUNPMacMobility_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 43),
    _AlaDaUNPMacMobility_Type()
)
alaDaUNPMacMobility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPMacMobility.setStatus("current")


class _AlaDaUNPEapolVersion_Type(Integer32):
    """Custom type alaDaUNPEapolVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v3", 3))
    )


_AlaDaUNPEapolVersion_Type.__name__ = "Integer32"
_AlaDaUNPEapolVersion_Object = MibScalar
alaDaUNPEapolVersion = _AlaDaUNPEapolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 44),
    _AlaDaUNPEapolVersion_Type()
)
alaDaUNPEapolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPEapolVersion.setStatus("current")


class _AlaDaUNPApModeSecurity_Type(Integer32):
    """Custom type alaDaUNPApModeSecurity based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPApModeSecurity_Type.__name__ = "Integer32"
_AlaDaUNPApModeSecurity_Object = MibScalar
alaDaUNPApModeSecurity = _AlaDaUNPApModeSecurity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 45),
    _AlaDaUNPApModeSecurity_Type()
)
alaDaUNPApModeSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPApModeSecurity.setStatus("current")


class _AlaDaUNPServiceMulticastGroupIPType_Type(InetAddressType):
    """Custom type alaDaUNPServiceMulticastGroupIPType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AlaDaUNPServiceMulticastGroupIPType_Type.__name__ = "InetAddressType"
_AlaDaUNPServiceMulticastGroupIPType_Object = MibScalar
alaDaUNPServiceMulticastGroupIPType = _AlaDaUNPServiceMulticastGroupIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 46),
    _AlaDaUNPServiceMulticastGroupIPType_Type()
)
alaDaUNPServiceMulticastGroupIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceMulticastGroupIPType.setStatus("current")
_AlaDaUNPServiceMulticastGroupIP_Type = InetAddress
_AlaDaUNPServiceMulticastGroupIP_Object = MibScalar
alaDaUNPServiceMulticastGroupIP = _AlaDaUNPServiceMulticastGroupIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 47),
    _AlaDaUNPServiceMulticastGroupIP_Type()
)
alaDaUNPServiceMulticastGroupIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceMulticastGroupIP.setStatus("current")


class _AlaDaUNPMultiUntagSap_Type(Integer32):
    """Custom type alaDaUNPMultiUntagSap based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPMultiUntagSap_Type.__name__ = "Integer32"
_AlaDaUNPMultiUntagSap_Object = MibScalar
alaDaUNPMultiUntagSap = _AlaDaUNPMultiUntagSap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 48),
    _AlaDaUNPMultiUntagSap_Type()
)
alaDaUNPMultiUntagSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPMultiUntagSap.setStatus("current")


class _AlaDaUNPRedirectAllowedWebServerPollingInterval_Type(Integer32):
    """Custom type alaDaUNPRedirectAllowedWebServerPollingInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_AlaDaUNPRedirectAllowedWebServerPollingInterval_Type.__name__ = "Integer32"
_AlaDaUNPRedirectAllowedWebServerPollingInterval_Object = MibScalar
alaDaUNPRedirectAllowedWebServerPollingInterval = _AlaDaUNPRedirectAllowedWebServerPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 49),
    _AlaDaUNPRedirectAllowedWebServerPollingInterval_Type()
)
alaDaUNPRedirectAllowedWebServerPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerPollingInterval.setStatus("current")


class _AlaDaUNPRedirectAllowedWebServerRefresh_Type(Integer32):
    """Custom type alaDaUNPRedirectAllowedWebServerRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("refresh", 1)
    )


_AlaDaUNPRedirectAllowedWebServerRefresh_Type.__name__ = "Integer32"
_AlaDaUNPRedirectAllowedWebServerRefresh_Object = MibScalar
alaDaUNPRedirectAllowedWebServerRefresh = _AlaDaUNPRedirectAllowedWebServerRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 50),
    _AlaDaUNPRedirectAllowedWebServerRefresh_Type()
)
alaDaUNPRedirectAllowedWebServerRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerRefresh.setStatus("current")


class _AlaDaUNPServiceVplsSignaling_Type(Integer32):
    """Custom type alaDaUNPServiceVplsSignaling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ldp", 1),
          ("bgp", 2))
    )


_AlaDaUNPServiceVplsSignaling_Type.__name__ = "Integer32"
_AlaDaUNPServiceVplsSignaling_Object = MibScalar
alaDaUNPServiceVplsSignaling = _AlaDaUNPServiceVplsSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 51),
    _AlaDaUNPServiceVplsSignaling_Type()
)
alaDaUNPServiceVplsSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceVplsSignaling.setStatus("current")


class _AlaDaUNPServiceVplsLdpFarEndIPList_Type(SnmpAdminString):
    """Custom type alaDaUNPServiceVplsLdpFarEndIPList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPServiceVplsLdpFarEndIPList_Type.__name__ = "SnmpAdminString"
_AlaDaUNPServiceVplsLdpFarEndIPList_Object = MibScalar
alaDaUNPServiceVplsLdpFarEndIPList = _AlaDaUNPServiceVplsLdpFarEndIPList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 52),
    _AlaDaUNPServiceVplsLdpFarEndIPList_Type()
)
alaDaUNPServiceVplsLdpFarEndIPList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceVplsLdpFarEndIPList.setStatus("current")


class _AlaDaUNPServiceVplsBgpVeID_Type(Unsigned32):
    """Custom type alaDaUNPServiceVplsBgpVeID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_AlaDaUNPServiceVplsBgpVeID_Type.__name__ = "Unsigned32"
_AlaDaUNPServiceVplsBgpVeID_Object = MibScalar
alaDaUNPServiceVplsBgpVeID = _AlaDaUNPServiceVplsBgpVeID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 53),
    _AlaDaUNPServiceVplsBgpVeID_Type()
)
alaDaUNPServiceVplsBgpVeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceVplsBgpVeID.setStatus("current")


class _AlaDaUNPServiceBvlanModulo_Type(Integer32):
    """Custom type alaDaUNPServiceBvlanModulo based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaDaUNPServiceBvlanModulo_Type.__name__ = "Integer32"
_AlaDaUNPServiceBvlanModulo_Object = MibScalar
alaDaUNPServiceBvlanModulo = _AlaDaUNPServiceBvlanModulo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 54),
    _AlaDaUNPServiceBvlanModulo_Type()
)
alaDaUNPServiceBvlanModulo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPServiceBvlanModulo.setStatus("current")


class _AlaDaUNPApModeType_Type(Integer32):
    """Custom type alaDaUNPApModeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stellar", 1),
          ("all", 2))
    )


_AlaDaUNPApModeType_Type.__name__ = "Integer32"
_AlaDaUNPApModeType_Object = MibScalar
alaDaUNPApModeType = _AlaDaUNPApModeType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 8, 55),
    _AlaDaUNPApModeType_Type()
)
alaDaUNPApModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPApModeType.setStatus("current")
_AlaDaMacVlanUserTable_Object = MibTable
alaDaMacVlanUserTable = _AlaDaMacVlanUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaDaMacVlanUserTable.setStatus("current")
_AlaDaMacVlanUserEntry_Object = MibTableRow
alaDaMacVlanUserEntry = _AlaDaMacVlanUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1)
)
alaDaMacVlanUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserIntfNum"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserMACAddress"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserVlanID"),
)
if mibBuilder.loadTexts:
    alaDaMacVlanUserEntry.setStatus("current")
_AlaDaMacVlanUserIntfNum_Type = InterfaceIndex
_AlaDaMacVlanUserIntfNum_Object = MibTableColumn
alaDaMacVlanUserIntfNum = _AlaDaMacVlanUserIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 1),
    _AlaDaMacVlanUserIntfNum_Type()
)
alaDaMacVlanUserIntfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserIntfNum.setStatus("current")
_AlaDaMacVlanUserMACAddress_Type = MacAddress
_AlaDaMacVlanUserMACAddress_Object = MibTableColumn
alaDaMacVlanUserMACAddress = _AlaDaMacVlanUserMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 2),
    _AlaDaMacVlanUserMACAddress_Type()
)
alaDaMacVlanUserMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserMACAddress.setStatus("current")


class _AlaDaMacVlanUserVlanID_Type(Integer32):
    """Custom type alaDaMacVlanUserVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDaMacVlanUserVlanID_Type.__name__ = "Integer32"
_AlaDaMacVlanUserVlanID_Object = MibTableColumn
alaDaMacVlanUserVlanID = _AlaDaMacVlanUserVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 3),
    _AlaDaMacVlanUserVlanID_Type()
)
alaDaMacVlanUserVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserVlanID.setStatus("current")


class _AlaDaMacVlanUserAuthStatus_Type(Integer32):
    """Custom type alaDaMacVlanUserAuthStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("authenticated", 3),
          ("failed", 4),
          ("failedTimeout", 5),
          ("failedNoServer", 6),
          ("failedNoResources", 7))
    )


_AlaDaMacVlanUserAuthStatus_Type.__name__ = "Integer32"
_AlaDaMacVlanUserAuthStatus_Object = MibTableColumn
alaDaMacVlanUserAuthStatus = _AlaDaMacVlanUserAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 4),
    _AlaDaMacVlanUserAuthStatus_Type()
)
alaDaMacVlanUserAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserAuthStatus.setStatus("current")
_AlaDaMacVlanUserIpAddressType_Type = InetAddressType
_AlaDaMacVlanUserIpAddressType_Object = MibTableColumn
alaDaMacVlanUserIpAddressType = _AlaDaMacVlanUserIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 5),
    _AlaDaMacVlanUserIpAddressType_Type()
)
alaDaMacVlanUserIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserIpAddressType.setStatus("current")
_AlaDaMacVlanUserIpAddress_Type = InetAddress
_AlaDaMacVlanUserIpAddress_Object = MibTableColumn
alaDaMacVlanUserIpAddress = _AlaDaMacVlanUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 6),
    _AlaDaMacVlanUserIpAddress_Type()
)
alaDaMacVlanUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserIpAddress.setStatus("current")
_AlaDaMacVlanUserUnpUsed_Type = SnmpAdminString
_AlaDaMacVlanUserUnpUsed_Object = MibTableColumn
alaDaMacVlanUserUnpUsed = _AlaDaMacVlanUserUnpUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 7),
    _AlaDaMacVlanUserUnpUsed_Type()
)
alaDaMacVlanUserUnpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserUnpUsed.setStatus("current")
_AlaDaMacVlanUserLoginTimeStamp_Type = DateAndTime
_AlaDaMacVlanUserLoginTimeStamp_Object = MibTableColumn
alaDaMacVlanUserLoginTimeStamp = _AlaDaMacVlanUserLoginTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 8),
    _AlaDaMacVlanUserLoginTimeStamp_Type()
)
alaDaMacVlanUserLoginTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserLoginTimeStamp.setStatus("current")


class _AlaDaMacVlanUserAuthtype_Type(Integer32):
    """Custom type alaDaMacVlanUserAuthtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macAuthentication", 0),
          ("others", 1),
          ("onexAuthentication", 2))
    )


_AlaDaMacVlanUserAuthtype_Type.__name__ = "Integer32"
_AlaDaMacVlanUserAuthtype_Object = MibTableColumn
alaDaMacVlanUserAuthtype = _AlaDaMacVlanUserAuthtype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 9),
    _AlaDaMacVlanUserAuthtype_Type()
)
alaDaMacVlanUserAuthtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserAuthtype.setStatus("current")
_AlaDaMacVlanUserClassificationSource_Type = AlaDaClassificationPolicyType
_AlaDaMacVlanUserClassificationSource_Object = MibTableColumn
alaDaMacVlanUserClassificationSource = _AlaDaMacVlanUserClassificationSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 10),
    _AlaDaMacVlanUserClassificationSource_Type()
)
alaDaMacVlanUserClassificationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserClassificationSource.setStatus("current")


class _AlaDaMacVlanUserMCLagLearningLoc_Type(Integer32):
    """Custom type alaDaMacVlanUserMCLagLearningLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_AlaDaMacVlanUserMCLagLearningLoc_Type.__name__ = "Integer32"
_AlaDaMacVlanUserMCLagLearningLoc_Object = MibTableColumn
alaDaMacVlanUserMCLagLearningLoc = _AlaDaMacVlanUserMCLagLearningLoc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 11),
    _AlaDaMacVlanUserMCLagLearningLoc_Type()
)
alaDaMacVlanUserMCLagLearningLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserMCLagLearningLoc.setStatus("current")
_AlaDaMacVlanUserName_Type = SnmpAdminString
_AlaDaMacVlanUserName_Object = MibTableColumn
alaDaMacVlanUserName = _AlaDaMacVlanUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 12),
    _AlaDaMacVlanUserName_Type()
)
alaDaMacVlanUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserName.setStatus("current")


class _AlaDaMacVlanUserRole_Type(SnmpAdminString):
    """Custom type alaDaMacVlanUserRole based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaMacVlanUserRole_Type.__name__ = "SnmpAdminString"
_AlaDaMacVlanUserRole_Object = MibTableColumn
alaDaMacVlanUserRole = _AlaDaMacVlanUserRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 13),
    _AlaDaMacVlanUserRole_Type()
)
alaDaMacVlanUserRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserRole.setStatus("current")


class _AlaDaMacVlanUserRoleSource_Type(SnmpAdminString):
    """Custom type alaDaMacVlanUserRoleSource based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaMacVlanUserRoleSource_Type.__name__ = "SnmpAdminString"
_AlaDaMacVlanUserRoleSource_Object = MibTableColumn
alaDaMacVlanUserRoleSource = _AlaDaMacVlanUserRoleSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 14),
    _AlaDaMacVlanUserRoleSource_Type()
)
alaDaMacVlanUserRoleSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserRoleSource.setStatus("current")


class _AlaDaMacVlanUserAuthFailReason_Type(SnmpAdminString):
    """Custom type alaDaMacVlanUserAuthFailReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaMacVlanUserAuthFailReason_Type.__name__ = "SnmpAdminString"
_AlaDaMacVlanUserAuthFailReason_Object = MibTableColumn
alaDaMacVlanUserAuthFailReason = _AlaDaMacVlanUserAuthFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 15),
    _AlaDaMacVlanUserAuthFailReason_Type()
)
alaDaMacVlanUserAuthFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserAuthFailReason.setStatus("current")


class _AlaDaMacVlanUserAuthRetryCount_Type(Integer32):
    """Custom type alaDaMacVlanUserAuthRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaDaMacVlanUserAuthRetryCount_Type.__name__ = "Integer32"
_AlaDaMacVlanUserAuthRetryCount_Object = MibTableColumn
alaDaMacVlanUserAuthRetryCount = _AlaDaMacVlanUserAuthRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 16),
    _AlaDaMacVlanUserAuthRetryCount_Type()
)
alaDaMacVlanUserAuthRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserAuthRetryCount.setStatus("current")


class _AlaDaMacVlanUserClassifProfRule_Type(SnmpAdminString):
    """Custom type alaDaMacVlanUserClassifProfRule based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaMacVlanUserClassifProfRule_Type.__name__ = "SnmpAdminString"
_AlaDaMacVlanUserClassifProfRule_Object = MibTableColumn
alaDaMacVlanUserClassifProfRule = _AlaDaMacVlanUserClassifProfRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 17),
    _AlaDaMacVlanUserClassifProfRule_Type()
)
alaDaMacVlanUserClassifProfRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserClassifProfRule.setStatus("current")


class _AlaDaMacVlanUserRoleRule_Type(SnmpAdminString):
    """Custom type alaDaMacVlanUserRoleRule based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaMacVlanUserRoleRule_Type.__name__ = "SnmpAdminString"
_AlaDaMacVlanUserRoleRule_Object = MibTableColumn
alaDaMacVlanUserRoleRule = _AlaDaMacVlanUserRoleRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 18),
    _AlaDaMacVlanUserRoleRule_Type()
)
alaDaMacVlanUserRoleRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserRoleRule.setStatus("current")


class _AlaDaMacVlanUserRestAccessStatus_Type(Integer32):
    """Custom type alaDaMacVlanUserRestAccessStatus based on Integer32"""
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


_AlaDaMacVlanUserRestAccessStatus_Type.__name__ = "Integer32"
_AlaDaMacVlanUserRestAccessStatus_Object = MibTableColumn
alaDaMacVlanUserRestAccessStatus = _AlaDaMacVlanUserRestAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 19),
    _AlaDaMacVlanUserRestAccessStatus_Type()
)
alaDaMacVlanUserRestAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserRestAccessStatus.setStatus("current")


class _AlaDaMacVlanUserLocPolicyStatus_Type(Integer32):
    """Custom type alaDaMacVlanUserLocPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("pass", 2),
          ("fail", 3))
    )


_AlaDaMacVlanUserLocPolicyStatus_Type.__name__ = "Integer32"
_AlaDaMacVlanUserLocPolicyStatus_Object = MibTableColumn
alaDaMacVlanUserLocPolicyStatus = _AlaDaMacVlanUserLocPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 20),
    _AlaDaMacVlanUserLocPolicyStatus_Type()
)
alaDaMacVlanUserLocPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserLocPolicyStatus.setStatus("current")


class _AlaDaMacVlanUserTimePolicyStatus_Type(Integer32):
    """Custom type alaDaMacVlanUserTimePolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("pass", 2),
          ("fail", 3))
    )


_AlaDaMacVlanUserTimePolicyStatus_Type.__name__ = "Integer32"
_AlaDaMacVlanUserTimePolicyStatus_Object = MibTableColumn
alaDaMacVlanUserTimePolicyStatus = _AlaDaMacVlanUserTimePolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 21),
    _AlaDaMacVlanUserTimePolicyStatus_Type()
)
alaDaMacVlanUserTimePolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserTimePolicyStatus.setStatus("current")


class _AlaDaMacVlanUserCapPortalStatus_Type(Integer32):
    """Custom type alaDaMacVlanUserCapPortalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("pass", 2),
          ("fail", 3))
    )


_AlaDaMacVlanUserCapPortalStatus_Type.__name__ = "Integer32"
_AlaDaMacVlanUserCapPortalStatus_Object = MibTableColumn
alaDaMacVlanUserCapPortalStatus = _AlaDaMacVlanUserCapPortalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 22),
    _AlaDaMacVlanUserCapPortalStatus_Type()
)
alaDaMacVlanUserCapPortalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserCapPortalStatus.setStatus("current")


class _AlaDaMacVlanUserQMRStatus_Type(Integer32):
    """Custom type alaDaMacVlanUserQMRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("pass", 2),
          ("fail", 3))
    )


_AlaDaMacVlanUserQMRStatus_Type.__name__ = "Integer32"
_AlaDaMacVlanUserQMRStatus_Object = MibTableColumn
alaDaMacVlanUserQMRStatus = _AlaDaMacVlanUserQMRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 23),
    _AlaDaMacVlanUserQMRStatus_Type()
)
alaDaMacVlanUserQMRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserQMRStatus.setStatus("current")
_AlaDaMacVlanUserAuthServerIpType_Type = InetAddressType
_AlaDaMacVlanUserAuthServerIpType_Object = MibTableColumn
alaDaMacVlanUserAuthServerIpType = _AlaDaMacVlanUserAuthServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 24),
    _AlaDaMacVlanUserAuthServerIpType_Type()
)
alaDaMacVlanUserAuthServerIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserAuthServerIpType.setStatus("current")
_AlaDaMacVlanUserAuthServerIpUsed_Type = InetAddress
_AlaDaMacVlanUserAuthServerIpUsed_Object = MibTableColumn
alaDaMacVlanUserAuthServerIpUsed = _AlaDaMacVlanUserAuthServerIpUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 25),
    _AlaDaMacVlanUserAuthServerIpUsed_Type()
)
alaDaMacVlanUserAuthServerIpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserAuthServerIpUsed.setStatus("current")


class _AlaDaMacVlanUserAuthServerUsed_Type(SnmpAdminString):
    """Custom type alaDaMacVlanUserAuthServerUsed based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaMacVlanUserAuthServerUsed_Type.__name__ = "SnmpAdminString"
_AlaDaMacVlanUserAuthServerUsed_Object = MibTableColumn
alaDaMacVlanUserAuthServerUsed = _AlaDaMacVlanUserAuthServerUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 26),
    _AlaDaMacVlanUserAuthServerUsed_Type()
)
alaDaMacVlanUserAuthServerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserAuthServerUsed.setStatus("current")
_AlaDaMacVlanUserServerMessage_Type = SnmpAdminString
_AlaDaMacVlanUserServerMessage_Object = MibTableColumn
alaDaMacVlanUserServerMessage = _AlaDaMacVlanUserServerMessage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 27),
    _AlaDaMacVlanUserServerMessage_Type()
)
alaDaMacVlanUserServerMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserServerMessage.setStatus("current")
_AlaDaMacVlanUserRedirectionUrl_Type = SnmpAdminString
_AlaDaMacVlanUserRedirectionUrl_Object = MibTableColumn
alaDaMacVlanUserRedirectionUrl = _AlaDaMacVlanUserRedirectionUrl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 28),
    _AlaDaMacVlanUserRedirectionUrl_Type()
)
alaDaMacVlanUserRedirectionUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserRedirectionUrl.setStatus("current")


class _AlaDaMacVlanUserSIPCallType_Type(Integer32):
    """Custom type alaDaMacVlanUserSIPCallType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normalCall", 1),
          ("emergencyCall", 2),
          ("notInCall", 3))
    )


_AlaDaMacVlanUserSIPCallType_Type.__name__ = "Integer32"
_AlaDaMacVlanUserSIPCallType_Object = MibTableColumn
alaDaMacVlanUserSIPCallType = _AlaDaMacVlanUserSIPCallType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 29),
    _AlaDaMacVlanUserSIPCallType_Type()
)
alaDaMacVlanUserSIPCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserSIPCallType.setStatus("current")


class _AlaDaMacVlanUserSIPMediaType_Type(Integer32):
    """Custom type alaDaMacVlanUserSIPMediaType based on Integer32"""
    defaultValue = 4

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
        *(("other", 1),
          ("audio", 2),
          ("video", 3),
          ("none", 4))
    )


_AlaDaMacVlanUserSIPMediaType_Type.__name__ = "Integer32"
_AlaDaMacVlanUserSIPMediaType_Object = MibTableColumn
alaDaMacVlanUserSIPMediaType = _AlaDaMacVlanUserSIPMediaType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 30),
    _AlaDaMacVlanUserSIPMediaType_Type()
)
alaDaMacVlanUserSIPMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserSIPMediaType.setStatus("current")
_AlaDaMacVlanUserUnpFromAuthServer_Type = SnmpAdminString
_AlaDaMacVlanUserUnpFromAuthServer_Object = MibTableColumn
alaDaMacVlanUserUnpFromAuthServer = _AlaDaMacVlanUserUnpFromAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 31),
    _AlaDaMacVlanUserUnpFromAuthServer_Type()
)
alaDaMacVlanUserUnpFromAuthServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserUnpFromAuthServer.setStatus("current")


class _AlaDaMacVlanUserType_Type(Integer32):
    """Custom type alaDaMacVlanUserType based on Integer32"""
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
        *(("bridge", 1),
          ("spbAccess", 2),
          ("edge", 3),
          ("vxlanAccess", 4),
          ("l2greAccess", 5))
    )


_AlaDaMacVlanUserType_Type.__name__ = "Integer32"
_AlaDaMacVlanUserType_Object = MibTableColumn
alaDaMacVlanUserType = _AlaDaMacVlanUserType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 32),
    _AlaDaMacVlanUserType_Type()
)
alaDaMacVlanUserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserType.setStatus("current")
_AlaDaMacVlanUserServiceID_Type = Unsigned32
_AlaDaMacVlanUserServiceID_Object = MibTableColumn
alaDaMacVlanUserServiceID = _AlaDaMacVlanUserServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 33),
    _AlaDaMacVlanUserServiceID_Type()
)
alaDaMacVlanUserServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserServiceID.setStatus("current")
_AlaDaMacVlanUserServiceSapIDIfIndex_Type = InterfaceIndex
_AlaDaMacVlanUserServiceSapIDIfIndex_Object = MibTableColumn
alaDaMacVlanUserServiceSapIDIfIndex = _AlaDaMacVlanUserServiceSapIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 34),
    _AlaDaMacVlanUserServiceSapIDIfIndex_Type()
)
alaDaMacVlanUserServiceSapIDIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserServiceSapIDIfIndex.setStatus("current")
_AlaDaMacVlanUserServiceSapIDEncapVal_Type = TmnxEncapVal
_AlaDaMacVlanUserServiceSapIDEncapVal_Object = MibTableColumn
alaDaMacVlanUserServiceSapIDEncapVal = _AlaDaMacVlanUserServiceSapIDEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 35),
    _AlaDaMacVlanUserServiceSapIDEncapVal_Type()
)
alaDaMacVlanUserServiceSapIDEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserServiceSapIDEncapVal.setStatus("current")
_AlaDaMacVlanUserVxlanVnid_Type = Unsigned32
_AlaDaMacVlanUserVxlanVnid_Object = MibTableColumn
alaDaMacVlanUserVxlanVnid = _AlaDaMacVlanUserVxlanVnid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 36),
    _AlaDaMacVlanUserVxlanVnid_Type()
)
alaDaMacVlanUserVxlanVnid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserVxlanVnid.setStatus("current")
_AlaDaMacVlanUserSpbIsid_Type = Unsigned32
_AlaDaMacVlanUserSpbIsid_Object = MibTableColumn
alaDaMacVlanUserSpbIsid = _AlaDaMacVlanUserSpbIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 37),
    _AlaDaMacVlanUserSpbIsid_Type()
)
alaDaMacVlanUserSpbIsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserSpbIsid.setStatus("current")
_AlaDaMacVlanUserSpbBVlan_Type = Unsigned32
_AlaDaMacVlanUserSpbBVlan_Object = MibTableColumn
alaDaMacVlanUserSpbBVlan = _AlaDaMacVlanUserSpbBVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 38),
    _AlaDaMacVlanUserSpbBVlan_Type()
)
alaDaMacVlanUserSpbBVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserSpbBVlan.setStatus("current")


class _AlaDaMacVlanUserKerberosStatus_Type(Integer32):
    """Custom type alaDaMacVlanUserKerberosStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("pass", 2),
          ("fail", 3))
    )


_AlaDaMacVlanUserKerberosStatus_Type.__name__ = "Integer32"
_AlaDaMacVlanUserKerberosStatus_Object = MibTableColumn
alaDaMacVlanUserKerberosStatus = _AlaDaMacVlanUserKerberosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 39),
    _AlaDaMacVlanUserKerberosStatus_Type()
)
alaDaMacVlanUserKerberosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserKerberosStatus.setStatus("current")
_AlaDaMacVlanUserL2greVpnid_Type = Unsigned32
_AlaDaMacVlanUserL2greVpnid_Object = MibTableColumn
alaDaMacVlanUserL2greVpnid = _AlaDaMacVlanUserL2greVpnid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 40),
    _AlaDaMacVlanUserL2greVpnid_Type()
)
alaDaMacVlanUserL2greVpnid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserL2greVpnid.setStatus("current")


class _AlaDaMacVlanUserImplicitTrustTagSource_Type(Integer32):
    """Custom type alaDaMacVlanUserImplicitTrustTagSource based on Integer32"""
    defaultValue = 1

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
          ("unpProfile", 2),
          ("radius", 3))
    )


_AlaDaMacVlanUserImplicitTrustTagSource_Type.__name__ = "Integer32"
_AlaDaMacVlanUserImplicitTrustTagSource_Object = MibTableColumn
alaDaMacVlanUserImplicitTrustTagSource = _AlaDaMacVlanUserImplicitTrustTagSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 41),
    _AlaDaMacVlanUserImplicitTrustTagSource_Type()
)
alaDaMacVlanUserImplicitTrustTagSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserImplicitTrustTagSource.setStatus("current")


class _AlaDaMacVlanUserRadiusTrustVlanStr_Type(SnmpAdminString):
    """Custom type alaDaMacVlanUserRadiusTrustVlanStr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaDaMacVlanUserRadiusTrustVlanStr_Type.__name__ = "SnmpAdminString"
_AlaDaMacVlanUserRadiusTrustVlanStr_Object = MibTableColumn
alaDaMacVlanUserRadiusTrustVlanStr = _AlaDaMacVlanUserRadiusTrustVlanStr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 9, 1, 42),
    _AlaDaMacVlanUserRadiusTrustVlanStr_Type()
)
alaDaMacVlanUserRadiusTrustVlanStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserRadiusTrustVlanStr.setStatus("current")
_AlaDaUNPNotificationObjects_ObjectIdentity = ObjectIdentity
alaDaUNPNotificationObjects = _AlaDaUNPNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10)
)
_AlaDaUnpMacAddr_Type = MacAddress
_AlaDaUnpMacAddr_Object = MibScalar
alaDaUnpMacAddr = _AlaDaUnpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 1),
    _AlaDaUnpMacAddr_Type()
)
alaDaUnpMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMacAddr.setStatus("current")
_AlaDaUnpSourceIpAddr_Type = IpAddress
_AlaDaUnpSourceIpAddr_Object = MibScalar
alaDaUnpSourceIpAddr = _AlaDaUnpSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 2),
    _AlaDaUnpSourceIpAddr_Type()
)
alaDaUnpSourceIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpSourceIpAddr.setStatus("current")
_AlaDaUnpNativeVlan_Type = Integer32
_AlaDaUnpNativeVlan_Object = MibScalar
alaDaUnpNativeVlan = _AlaDaUnpNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 3),
    _AlaDaUnpNativeVlan_Type()
)
alaDaUnpNativeVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpNativeVlan.setStatus("current")


class _AlaDaUnpVlan_Type(Integer32):
    """Custom type alaDaUnpVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUnpVlan_Type.__name__ = "Integer32"
_AlaDaUnpVlan_Object = MibScalar
alaDaUnpVlan = _AlaDaUnpVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 4),
    _AlaDaUnpVlan_Type()
)
alaDaUnpVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpVlan.setStatus("current")
_AlaDaUnpMCLAGId_Type = Integer32
_AlaDaUnpMCLAGId_Object = MibScalar
alaDaUnpMCLAGId = _AlaDaUnpMCLAGId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 5),
    _AlaDaUnpMCLAGId_Type()
)
alaDaUnpMCLAGId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMCLAGId.setStatus("current")


class _AlaDaUnpCommandType_Type(Integer32):
    """Custom type alaDaUnpCommandType based on Integer32"""
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
        *(("unpConfigCmd", 1),
          ("macRuleConfigCmd", 2),
          ("macRangeRuleConfigCmd", 3),
          ("ipRuleConfigCmd", 4),
          ("vlanTagRuleConfigCmd", 5),
          ("authServerUnpConfigCmd", 6),
          ("authServerTimerConfigCmd", 7),
          ("dynamicVlanConfigCmd", 8),
          ("lagConfigCmd", 9),
          ("dynamicProfileConfigCmd", 10))
    )


_AlaDaUnpCommandType_Type.__name__ = "Integer32"
_AlaDaUnpCommandType_Object = MibScalar
alaDaUnpCommandType = _AlaDaUnpCommandType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 6),
    _AlaDaUnpCommandType_Type()
)
alaDaUnpCommandType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpCommandType.setStatus("current")


class _AlaDaUnpName_Type(SnmpAdminString):
    """Custom type alaDaUnpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUnpName_Type.__name__ = "SnmpAdminString"
_AlaDaUnpName_Object = MibScalar
alaDaUnpName = _AlaDaUnpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 7),
    _AlaDaUnpName_Type()
)
alaDaUnpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpName.setStatus("current")
_AlaDaUnpMacAddr1_Type = MacAddress
_AlaDaUnpMacAddr1_Object = MibScalar
alaDaUnpMacAddr1 = _AlaDaUnpMacAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 8),
    _AlaDaUnpMacAddr1_Type()
)
alaDaUnpMacAddr1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMacAddr1.setStatus("current")
_AlaDaUnpMacAddr2_Type = MacAddress
_AlaDaUnpMacAddr2_Object = MibScalar
alaDaUnpMacAddr2 = _AlaDaUnpMacAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 9),
    _AlaDaUnpMacAddr2_Type()
)
alaDaUnpMacAddr2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMacAddr2.setStatus("current")
_AlaDaUnpIpAddr_Type = IpAddress
_AlaDaUnpIpAddr_Object = MibScalar
alaDaUnpIpAddr = _AlaDaUnpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 10),
    _AlaDaUnpIpAddr_Type()
)
alaDaUnpIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpIpAddr.setStatus("current")
_AlaDaUnpIpMask_Type = IpAddress
_AlaDaUnpIpMask_Object = MibScalar
alaDaUnpIpMask = _AlaDaUnpIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 11),
    _AlaDaUnpIpMask_Type()
)
alaDaUnpIpMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpIpMask.setStatus("current")


class _AlaDaUnpVlanTag_Type(Integer32):
    """Custom type alaDaUnpVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUnpVlanTag_Type.__name__ = "Integer32"
_AlaDaUnpVlanTag_Object = MibScalar
alaDaUnpVlanTag = _AlaDaUnpVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 12),
    _AlaDaUnpVlanTag_Type()
)
alaDaUnpVlanTag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpVlanTag.setStatus("current")


class _AlaDaKerberosRateLimitString_Type(SnmpAdminString):
    """Custom type alaDaKerberosRateLimitString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaKerberosRateLimitString_Type.__name__ = "SnmpAdminString"
_AlaDaKerberosRateLimitString_Object = MibScalar
alaDaKerberosRateLimitString = _AlaDaKerberosRateLimitString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 13),
    _AlaDaKerberosRateLimitString_Type()
)
alaDaKerberosRateLimitString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaKerberosRateLimitString.setStatus("current")
_AlaDaRouterAuthNumberOfUsersPassedAuthentication_Type = Unsigned32
_AlaDaRouterAuthNumberOfUsersPassedAuthentication_Object = MibScalar
alaDaRouterAuthNumberOfUsersPassedAuthentication = _AlaDaRouterAuthNumberOfUsersPassedAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 14),
    _AlaDaRouterAuthNumberOfUsersPassedAuthentication_Type()
)
alaDaRouterAuthNumberOfUsersPassedAuthentication.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthNumberOfUsersPassedAuthentication.setStatus("current")
_AlaDaRouterAuthUserSourceIpAddressType_Type = InetAddressType
_AlaDaRouterAuthUserSourceIpAddressType_Object = MibScalar
alaDaRouterAuthUserSourceIpAddressType = _AlaDaRouterAuthUserSourceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 15),
    _AlaDaRouterAuthUserSourceIpAddressType_Type()
)
alaDaRouterAuthUserSourceIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthUserSourceIpAddressType.setStatus("current")
_AlaDaRouterAuthUserSourceIpAddress_Type = InetAddress
_AlaDaRouterAuthUserSourceIpAddress_Object = MibScalar
alaDaRouterAuthUserSourceIpAddress = _AlaDaRouterAuthUserSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 16),
    _AlaDaRouterAuthUserSourceIpAddress_Type()
)
alaDaRouterAuthUserSourceIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthUserSourceIpAddress.setStatus("current")
_AlaDaRouterAuthUserDestinationIpAddressType_Type = InetAddressType
_AlaDaRouterAuthUserDestinationIpAddressType_Object = MibScalar
alaDaRouterAuthUserDestinationIpAddressType = _AlaDaRouterAuthUserDestinationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 17),
    _AlaDaRouterAuthUserDestinationIpAddressType_Type()
)
alaDaRouterAuthUserDestinationIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthUserDestinationIpAddressType.setStatus("current")
_AlaDaRouterAuthUserDestinationIpAddress_Type = InetAddress
_AlaDaRouterAuthUserDestinationIpAddress_Object = MibScalar
alaDaRouterAuthUserDestinationIpAddress = _AlaDaRouterAuthUserDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 18),
    _AlaDaRouterAuthUserDestinationIpAddress_Type()
)
alaDaRouterAuthUserDestinationIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthUserDestinationIpAddress.setStatus("current")
_AlaDaRouterAuthUserName_Type = SnmpAdminString
_AlaDaRouterAuthUserName_Object = MibScalar
alaDaRouterAuthUserName = _AlaDaRouterAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 19),
    _AlaDaRouterAuthUserName_Type()
)
alaDaRouterAuthUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthUserName.setStatus("current")
_AlaDaRouterAuthUserAttempts_Type = Unsigned32
_AlaDaRouterAuthUserAttempts_Object = MibScalar
alaDaRouterAuthUserAttempts = _AlaDaRouterAuthUserAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 20),
    _AlaDaRouterAuthUserAttempts_Type()
)
alaDaRouterAuthUserAttempts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthUserAttempts.setStatus("current")
_AlaDaRouterAuthNumberOfUsersFailedAuthentication_Type = Unsigned32
_AlaDaRouterAuthNumberOfUsersFailedAuthentication_Object = MibScalar
alaDaRouterAuthNumberOfUsersFailedAuthentication = _AlaDaRouterAuthNumberOfUsersFailedAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 21),
    _AlaDaRouterAuthNumberOfUsersFailedAuthentication_Type()
)
alaDaRouterAuthNumberOfUsersFailedAuthentication.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthNumberOfUsersFailedAuthentication.setStatus("current")
_AlaDaRouterAuthNumberOfAuthenticatedUsers_Type = Unsigned32
_AlaDaRouterAuthNumberOfAuthenticatedUsers_Object = MibScalar
alaDaRouterAuthNumberOfAuthenticatedUsers = _AlaDaRouterAuthNumberOfAuthenticatedUsers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 22),
    _AlaDaRouterAuthNumberOfAuthenticatedUsers_Type()
)
alaDaRouterAuthNumberOfAuthenticatedUsers.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthNumberOfAuthenticatedUsers.setStatus("current")
_AlaDaRouterAuthNumberOfConfigUsed_Type = Unsigned32
_AlaDaRouterAuthNumberOfConfigUsed_Object = MibScalar
alaDaRouterAuthNumberOfConfigUsed = _AlaDaRouterAuthNumberOfConfigUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 23),
    _AlaDaRouterAuthNumberOfConfigUsed_Type()
)
alaDaRouterAuthNumberOfConfigUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaRouterAuthNumberOfConfigUsed.setStatus("current")
_AlaDaUnpMaxUserSupported_Type = Integer32
_AlaDaUnpMaxUserSupported_Object = MibScalar
alaDaUnpMaxUserSupported = _AlaDaUnpMaxUserSupported_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 24),
    _AlaDaUnpMaxUserSupported_Type()
)
alaDaUnpMaxUserSupported.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMaxUserSupported.setStatus("current")
_AlaDaUnpMaxUserCurrentNumberOfUsers_Type = Integer32
_AlaDaUnpMaxUserCurrentNumberOfUsers_Object = MibScalar
alaDaUnpMaxUserCurrentNumberOfUsers = _AlaDaUnpMaxUserCurrentNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 25),
    _AlaDaUnpMaxUserCurrentNumberOfUsers_Type()
)
alaDaUnpMaxUserCurrentNumberOfUsers.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMaxUserCurrentNumberOfUsers.setStatus("current")
_AlaDaUnpHWResourceChassisId_Type = Integer32
_AlaDaUnpHWResourceChassisId_Object = MibScalar
alaDaUnpHWResourceChassisId = _AlaDaUnpHWResourceChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 26),
    _AlaDaUnpHWResourceChassisId_Type()
)
alaDaUnpHWResourceChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpHWResourceChassisId.setStatus("current")
_AlaDaUnpHWResourceSlot_Type = Integer32
_AlaDaUnpHWResourceSlot_Object = MibScalar
alaDaUnpHWResourceSlot = _AlaDaUnpHWResourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 27),
    _AlaDaUnpHWResourceSlot_Type()
)
alaDaUnpHWResourceSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpHWResourceSlot.setStatus("current")
_AlaDaUnpHWResourceTtiAllocated_Type = Integer32
_AlaDaUnpHWResourceTtiAllocated_Object = MibScalar
alaDaUnpHWResourceTtiAllocated = _AlaDaUnpHWResourceTtiAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 28),
    _AlaDaUnpHWResourceTtiAllocated_Type()
)
alaDaUnpHWResourceTtiAllocated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpHWResourceTtiAllocated.setStatus("current")
_AlaDaUnpAuthMACAddress_Type = MacAddress
_AlaDaUnpAuthMACAddress_Object = MibScalar
alaDaUnpAuthMACAddress = _AlaDaUnpAuthMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 29),
    _AlaDaUnpAuthMACAddress_Type()
)
alaDaUnpAuthMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpAuthMACAddress.setStatus("current")


class _AlaDaUnpAuthStatus_Type(Integer32):
    """Custom type alaDaUnpAuthStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("authenticated", 3),
          ("failed", 4),
          ("failedTimeout", 5),
          ("failedNoServer", 6),
          ("failedNoResources", 7))
    )


_AlaDaUnpAuthStatus_Type.__name__ = "Integer32"
_AlaDaUnpAuthStatus_Object = MibScalar
alaDaUnpAuthStatus = _AlaDaUnpAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 30),
    _AlaDaUnpAuthStatus_Type()
)
alaDaUnpAuthStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpAuthStatus.setStatus("current")
_AlaDaUnpAuthRADIUSServerIPType_Type = InetAddressType
_AlaDaUnpAuthRADIUSServerIPType_Object = MibScalar
alaDaUnpAuthRADIUSServerIPType = _AlaDaUnpAuthRADIUSServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 31),
    _AlaDaUnpAuthRADIUSServerIPType_Type()
)
alaDaUnpAuthRADIUSServerIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpAuthRADIUSServerIPType.setStatus("current")
_AlaDaUnpAuthRADIUSServerIP_Type = InetAddress
_AlaDaUnpAuthRADIUSServerIP_Object = MibScalar
alaDaUnpAuthRADIUSServerIP = _AlaDaUnpAuthRADIUSServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 32),
    _AlaDaUnpAuthRADIUSServerIP_Type()
)
alaDaUnpAuthRADIUSServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpAuthRADIUSServerIP.setStatus("current")


class _AlaDaUnpAuthServerReplyMsg_Type(SnmpAdminString):
    """Custom type alaDaUnpAuthServerReplyMsg based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaDaUnpAuthServerReplyMsg_Type.__name__ = "SnmpAdminString"
_AlaDaUnpAuthServerReplyMsg_Object = MibScalar
alaDaUnpAuthServerReplyMsg = _AlaDaUnpAuthServerReplyMsg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 33),
    _AlaDaUnpAuthServerReplyMsg_Type()
)
alaDaUnpAuthServerReplyMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpAuthServerReplyMsg.setStatus("current")


class _AlaDaUnpAuthFailureReason_Type(SnmpAdminString):
    """Custom type alaDaUnpAuthFailureReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaDaUnpAuthFailureReason_Type.__name__ = "SnmpAdminString"
_AlaDaUnpAuthFailureReason_Object = MibScalar
alaDaUnpAuthFailureReason = _AlaDaUnpAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 10, 34),
    _AlaDaUnpAuthFailureReason_Type()
)
alaDaUnpAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpAuthFailureReason.setStatus("current")
_AlaDaUnpCustomerDomainTable_Object = MibTable
alaDaUnpCustomerDomainTable = _AlaDaUnpCustomerDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainTable.setStatus("current")
_AlaDaUnpCustomerDomainEntry_Object = MibTableRow
alaDaUnpCustomerDomainEntry = _AlaDaUnpCustomerDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 11, 1)
)
alaDaUnpCustomerDomainEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUnpCustomerDomainId"),
)
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainEntry.setStatus("current")


class _AlaDaUnpCustomerDomainId_Type(Unsigned32):
    """Custom type alaDaUnpCustomerDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUnpCustomerDomainId_Type.__name__ = "Unsigned32"
_AlaDaUnpCustomerDomainId_Object = MibTableColumn
alaDaUnpCustomerDomainId = _AlaDaUnpCustomerDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 11, 1, 1),
    _AlaDaUnpCustomerDomainId_Type()
)
alaDaUnpCustomerDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainId.setStatus("current")


class _AlaDaUnpCustomerDomainDesc_Type(SnmpAdminString):
    """Custom type alaDaUnpCustomerDomainDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AlaDaUnpCustomerDomainDesc_Type.__name__ = "SnmpAdminString"
_AlaDaUnpCustomerDomainDesc_Object = MibTableColumn
alaDaUnpCustomerDomainDesc = _AlaDaUnpCustomerDomainDesc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 11, 1, 2),
    _AlaDaUnpCustomerDomainDesc_Type()
)
alaDaUnpCustomerDomainDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainDesc.setStatus("current")
_AlaDaUnpCustomerDomainRowStatus_Type = RowStatus
_AlaDaUnpCustomerDomainRowStatus_Object = MibTableColumn
alaDaUnpCustomerDomainRowStatus = _AlaDaUnpCustomerDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 11, 1, 3),
    _AlaDaUnpCustomerDomainRowStatus_Type()
)
alaDaUnpCustomerDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainRowStatus.setStatus("current")
_AlaDaSpbProfileTable_Object = MibTable
alaDaSpbProfileTable = _AlaDaSpbProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaDaSpbProfileTable.setStatus("obsolete")
_AlaDaSpbProfileEntry_Object = MibTableRow
alaDaSpbProfileEntry = _AlaDaSpbProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1)
)
alaDaSpbProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaSpbProfileName"),
)
if mibBuilder.loadTexts:
    alaDaSpbProfileEntry.setStatus("obsolete")


class _AlaDaSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaSpbProfileName_Object = MibTableColumn
alaDaSpbProfileName = _AlaDaSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 1),
    _AlaDaSpbProfileName_Type()
)
alaDaSpbProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaSpbProfileName.setStatus("obsolete")
_AlaDaSpbProfileEncapVal_Type = TmnxEncapVal
_AlaDaSpbProfileEncapVal_Object = MibTableColumn
alaDaSpbProfileEncapVal = _AlaDaSpbProfileEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 2),
    _AlaDaSpbProfileEncapVal_Type()
)
alaDaSpbProfileEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileEncapVal.setStatus("obsolete")


class _AlaDaSpbProfileQosPolicyListName_Type(SnmpAdminString):
    """Custom type alaDaSpbProfileQosPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaSpbProfileQosPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaDaSpbProfileQosPolicyListName_Object = MibTableColumn
alaDaSpbProfileQosPolicyListName = _AlaDaSpbProfileQosPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 3),
    _AlaDaSpbProfileQosPolicyListName_Type()
)
alaDaSpbProfileQosPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileQosPolicyListName.setStatus("obsolete")


class _AlaDaSpbProfileIsid_Type(Unsigned32):
    """Custom type alaDaSpbProfileIsid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_AlaDaSpbProfileIsid_Type.__name__ = "Unsigned32"
_AlaDaSpbProfileIsid_Object = MibTableColumn
alaDaSpbProfileIsid = _AlaDaSpbProfileIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 4),
    _AlaDaSpbProfileIsid_Type()
)
alaDaSpbProfileIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileIsid.setStatus("obsolete")


class _AlaDaSpbProfileBVlan_Type(Unsigned32):
    """Custom type alaDaSpbProfileBVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaSpbProfileBVlan_Type.__name__ = "Unsigned32"
_AlaDaSpbProfileBVlan_Object = MibTableColumn
alaDaSpbProfileBVlan = _AlaDaSpbProfileBVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 5),
    _AlaDaSpbProfileBVlan_Type()
)
alaDaSpbProfileBVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileBVlan.setStatus("obsolete")
_AlaDaSpbProfileRowStatus_Type = RowStatus
_AlaDaSpbProfileRowStatus_Object = MibTableColumn
alaDaSpbProfileRowStatus = _AlaDaSpbProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 6),
    _AlaDaSpbProfileRowStatus_Type()
)
alaDaSpbProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileRowStatus.setStatus("obsolete")


class _AlaDaSpbProfileMulticastMode_Type(Integer32):
    """Custom type alaDaSpbProfileMulticastMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("headend", 1),
          ("tandem", 2))
    )


_AlaDaSpbProfileMulticastMode_Type.__name__ = "Integer32"
_AlaDaSpbProfileMulticastMode_Object = MibTableColumn
alaDaSpbProfileMulticastMode = _AlaDaSpbProfileMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 7),
    _AlaDaSpbProfileMulticastMode_Type()
)
alaDaSpbProfileMulticastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileMulticastMode.setStatus("obsolete")


class _AlaDaSpbProfileSapVlanXlation_Type(Integer32):
    """Custom type alaDaSpbProfileSapVlanXlation based on Integer32"""
    defaultValue = 1

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


_AlaDaSpbProfileSapVlanXlation_Type.__name__ = "Integer32"
_AlaDaSpbProfileSapVlanXlation_Object = MibTableColumn
alaDaSpbProfileSapVlanXlation = _AlaDaSpbProfileSapVlanXlation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 8),
    _AlaDaSpbProfileSapVlanXlation_Type()
)
alaDaSpbProfileSapVlanXlation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileSapVlanXlation.setStatus("obsolete")


class _AlaDaSpbProfileMobileTag_Type(Integer32):
    """Custom type alaDaSpbProfileMobileTag based on Integer32"""
    defaultValue = 2

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


_AlaDaSpbProfileMobileTag_Type.__name__ = "Integer32"
_AlaDaSpbProfileMobileTag_Object = MibTableColumn
alaDaSpbProfileMobileTag = _AlaDaSpbProfileMobileTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 9),
    _AlaDaSpbProfileMobileTag_Type()
)
alaDaSpbProfileMobileTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileMobileTag.setStatus("obsolete")


class _AlaDaSpbProfileAFDConfig_Type(Integer32):
    """Custom type alaDaSpbProfileAFDConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("autoFabric", 2))
    )


_AlaDaSpbProfileAFDConfig_Type.__name__ = "Integer32"
_AlaDaSpbProfileAFDConfig_Object = MibTableColumn
alaDaSpbProfileAFDConfig = _AlaDaSpbProfileAFDConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 12, 1, 10),
    _AlaDaSpbProfileAFDConfig_Type()
)
alaDaSpbProfileAFDConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaSpbProfileAFDConfig.setStatus("obsolete")
_AlaDaUNPCustDomainEvbGpIdRuleTable_Object = MibTable
alaDaUNPCustDomainEvbGpIdRuleTable = _AlaDaUNPCustDomainEvbGpIdRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleTable.setStatus("current")
_AlaDaUNPCustDomainEvbGpIdRuleEntry_Object = MibTableRow
alaDaUNPCustDomainEvbGpIdRuleEntry = _AlaDaUNPCustDomainEvbGpIdRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 13, 1)
)
alaDaUNPCustDomainEvbGpIdRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleGroupId"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Type(Unsigned32):
    """Custom type alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Type.__name__ = "Unsigned32"
_AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId = _AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 13, 1, 1),
    _AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Type()
)
alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId.setStatus("current")


class _AlaDaUNPCustDomainEvbGpIdRuleGroupId_Type(Unsigned32):
    """Custom type alaDaUNPCustDomainEvbGpIdRuleGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPCustDomainEvbGpIdRuleGroupId_Type.__name__ = "Unsigned32"
_AlaDaUNPCustDomainEvbGpIdRuleGroupId_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleGroupId = _AlaDaUNPCustDomainEvbGpIdRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 13, 1, 2),
    _AlaDaUNPCustDomainEvbGpIdRuleGroupId_Type()
)
alaDaUNPCustDomainEvbGpIdRuleGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleGroupId.setStatus("current")


class _AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainEvbGpIdRuleVlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleVlanProfileName = _AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 13, 1, 3),
    _AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Type()
)
alaDaUNPCustDomainEvbGpIdRuleVlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleVlanProfileName.setStatus("current")


class _AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainEvbGpIdRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleSpbProfileName = _AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 13, 1, 4),
    _AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Type()
)
alaDaUNPCustDomainEvbGpIdRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleSpbProfileName.setStatus("current")
_AlaDaUNPCustDomainEvbGpIdRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainEvbGpIdRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleRowStatus = _AlaDaUNPCustDomainEvbGpIdRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 13, 1, 5),
    _AlaDaUNPCustDomainEvbGpIdRuleRowStatus_Type()
)
alaDaUNPCustDomainEvbGpIdRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainEvbGpIdRuleVxlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainEvbGpIdRuleVxlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainEvbGpIdRuleVxlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainEvbGpIdRuleVxlanProfileName_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleVxlanProfileName = _AlaDaUNPCustDomainEvbGpIdRuleVxlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 13, 1, 6),
    _AlaDaUNPCustDomainEvbGpIdRuleVxlanProfileName_Type()
)
alaDaUNPCustDomainEvbGpIdRuleVxlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleVxlanProfileName.setStatus("current")
_AlaDaUNPCustDomainVlanTagRuleTable_Object = MibTable
alaDaUNPCustDomainVlanTagRuleTable = _AlaDaUNPCustDomainVlanTagRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleTable.setStatus("current")
_AlaDaUNPCustDomainVlanTagRuleEntry_Object = MibTableRow
alaDaUNPCustDomainVlanTagRuleEntry = _AlaDaUNPCustDomainVlanTagRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1)
)
alaDaUNPCustDomainVlanTagRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleVlan"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleDomainId_Type(Integer32):
    """Custom type alaDaUNPCustDomainVlanTagRuleDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUNPCustDomainVlanTagRuleDomainId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainVlanTagRuleDomainId_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleDomainId = _AlaDaUNPCustDomainVlanTagRuleDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 1),
    _AlaDaUNPCustDomainVlanTagRuleDomainId_Type()
)
alaDaUNPCustDomainVlanTagRuleDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleDomainId.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleVlan_Type(Integer32):
    """Custom type alaDaUNPCustDomainVlanTagRuleVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPCustDomainVlanTagRuleVlan_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainVlanTagRuleVlan_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleVlan = _AlaDaUNPCustDomainVlanTagRuleVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 2),
    _AlaDaUNPCustDomainVlanTagRuleVlan_Type()
)
alaDaUNPCustDomainVlanTagRuleVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleVlan.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainVlanTagRuleVlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleVlanProfileName = _AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 3),
    _AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Type()
)
alaDaUNPCustDomainVlanTagRuleVlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleVlanProfileName.setStatus("deprecated")
_AlaDaUNPCustDomainVlanTagRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainVlanTagRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleRowStatus = _AlaDaUNPCustDomainVlanTagRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 4),
    _AlaDaUNPCustDomainVlanTagRuleRowStatus_Type()
)
alaDaUNPCustDomainVlanTagRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPCustDomainVlanTagRuleMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPCustDomainVlanTagRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus = _AlaDaUNPCustDomainVlanTagRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 5),
    _AlaDaUNPCustDomainVlanTagRuleMCLagConfigStatus_Type()
)
alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainVlanTagRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleSpbProfileName = _AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 6),
    _AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Type()
)
alaDaUNPCustDomainVlanTagRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleSpbProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainVlanTagRuleTagPosition_Type(Integer32):
    """Custom type alaDaUNPCustDomainVlanTagRuleTagPosition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("outerTag", 1),
          ("innerTag", 2))
    )


_AlaDaUNPCustDomainVlanTagRuleTagPosition_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainVlanTagRuleTagPosition_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleTagPosition = _AlaDaUNPCustDomainVlanTagRuleTagPosition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 7),
    _AlaDaUNPCustDomainVlanTagRuleTagPosition_Type()
)
alaDaUNPCustDomainVlanTagRuleTagPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleTagPosition.setStatus("deprecated")


class _AlaDaUNPCustDomainVlanTagRuleVxlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainVlanTagRuleVxlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainVlanTagRuleVxlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainVlanTagRuleVxlanProfileName_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleVxlanProfileName = _AlaDaUNPCustDomainVlanTagRuleVxlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 8),
    _AlaDaUNPCustDomainVlanTagRuleVxlanProfileName_Type()
)
alaDaUNPCustDomainVlanTagRuleVxlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleVxlanProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainVlanTagRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainVlanTagRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainVlanTagRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainVlanTagRuleProfile1_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleProfile1 = _AlaDaUNPCustDomainVlanTagRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 9),
    _AlaDaUNPCustDomainVlanTagRuleProfile1_Type()
)
alaDaUNPCustDomainVlanTagRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleProfile1.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainVlanTagRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainVlanTagRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainVlanTagRuleProfile2_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleProfile2 = _AlaDaUNPCustDomainVlanTagRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 10),
    _AlaDaUNPCustDomainVlanTagRuleProfile2_Type()
)
alaDaUNPCustDomainVlanTagRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleProfile2.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainVlanTagRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainVlanTagRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainVlanTagRuleProfile3_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleProfile3 = _AlaDaUNPCustDomainVlanTagRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 14, 1, 11),
    _AlaDaUNPCustDomainVlanTagRuleProfile3_Type()
)
alaDaUNPCustDomainVlanTagRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleProfile3.setStatus("current")
_AlaDaUNPCustDomainIpNetRuleTable_Object = MibTable
alaDaUNPCustDomainIpNetRuleTable = _AlaDaUNPCustDomainIpNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleTable.setStatus("current")
_AlaDaUNPCustDomainIpNetRuleEntry_Object = MibTableRow
alaDaUNPCustDomainIpNetRuleEntry = _AlaDaUNPCustDomainIpNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1)
)
alaDaUNPCustDomainIpNetRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleMask"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleDomainId_Type(Integer32):
    """Custom type alaDaUNPCustDomainIpNetRuleDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUNPCustDomainIpNetRuleDomainId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainIpNetRuleDomainId_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleDomainId = _AlaDaUNPCustDomainIpNetRuleDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 1),
    _AlaDaUNPCustDomainIpNetRuleDomainId_Type()
)
alaDaUNPCustDomainIpNetRuleDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleDomainId.setStatus("current")
_AlaDaUNPCustDomainIpNetRuleAddrType_Type = InetAddressType
_AlaDaUNPCustDomainIpNetRuleAddrType_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleAddrType = _AlaDaUNPCustDomainIpNetRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 2),
    _AlaDaUNPCustDomainIpNetRuleAddrType_Type()
)
alaDaUNPCustDomainIpNetRuleAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleAddrType.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleAddr_Type(InetAddress):
    """Custom type alaDaUNPCustDomainIpNetRuleAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPCustDomainIpNetRuleAddr_Type.__name__ = "InetAddress"
_AlaDaUNPCustDomainIpNetRuleAddr_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleAddr = _AlaDaUNPCustDomainIpNetRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 3),
    _AlaDaUNPCustDomainIpNetRuleAddr_Type()
)
alaDaUNPCustDomainIpNetRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleAddr.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleMask_Type(InetAddress):
    """Custom type alaDaUNPCustDomainIpNetRuleMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPCustDomainIpNetRuleMask_Type.__name__ = "InetAddress"
_AlaDaUNPCustDomainIpNetRuleMask_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleMask = _AlaDaUNPCustDomainIpNetRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 4),
    _AlaDaUNPCustDomainIpNetRuleMask_Type()
)
alaDaUNPCustDomainIpNetRuleMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleMask.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainIpNetRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainIpNetRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainIpNetRuleProfileName_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleProfileName = _AlaDaUNPCustDomainIpNetRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 5),
    _AlaDaUNPCustDomainIpNetRuleProfileName_Type()
)
alaDaUNPCustDomainIpNetRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainIpNetRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPCustDomainIpNetRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPCustDomainIpNetRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainIpNetRuleVlanTag_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleVlanTag = _AlaDaUNPCustDomainIpNetRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 6),
    _AlaDaUNPCustDomainIpNetRuleVlanTag_Type()
)
alaDaUNPCustDomainIpNetRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleVlanTag.setStatus("current")
_AlaDaUNPCustDomainIpNetRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainIpNetRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleRowStatus = _AlaDaUNPCustDomainIpNetRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 7),
    _AlaDaUNPCustDomainIpNetRuleRowStatus_Type()
)
alaDaUNPCustDomainIpNetRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPCustDomainIpNetRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPCustDomainIpNetRuleMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPCustDomainIpNetRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleMCLagConfigStatus = _AlaDaUNPCustDomainIpNetRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 8),
    _AlaDaUNPCustDomainIpNetRuleMCLagConfigStatus_Type()
)
alaDaUNPCustDomainIpNetRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleMCLagConfigStatus.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainIpNetRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainIpNetRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainIpNetRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleSpbProfileName = _AlaDaUNPCustDomainIpNetRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 9),
    _AlaDaUNPCustDomainIpNetRuleSpbProfileName_Type()
)
alaDaUNPCustDomainIpNetRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleSpbProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainIpNetRuleEdgeProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainIpNetRuleEdgeProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainIpNetRuleEdgeProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainIpNetRuleEdgeProfile_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleEdgeProfile = _AlaDaUNPCustDomainIpNetRuleEdgeProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 10),
    _AlaDaUNPCustDomainIpNetRuleEdgeProfile_Type()
)
alaDaUNPCustDomainIpNetRuleEdgeProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleEdgeProfile.setStatus("deprecated")


class _AlaDaUNPCustDomainIpNetRuleVxlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainIpNetRuleVxlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainIpNetRuleVxlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainIpNetRuleVxlanProfileName_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleVxlanProfileName = _AlaDaUNPCustDomainIpNetRuleVxlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 11),
    _AlaDaUNPCustDomainIpNetRuleVxlanProfileName_Type()
)
alaDaUNPCustDomainIpNetRuleVxlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleVxlanProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainIpNetRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainIpNetRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainIpNetRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainIpNetRuleProfile1_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleProfile1 = _AlaDaUNPCustDomainIpNetRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 12),
    _AlaDaUNPCustDomainIpNetRuleProfile1_Type()
)
alaDaUNPCustDomainIpNetRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleProfile1.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainIpNetRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainIpNetRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainIpNetRuleProfile2_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleProfile2 = _AlaDaUNPCustDomainIpNetRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 13),
    _AlaDaUNPCustDomainIpNetRuleProfile2_Type()
)
alaDaUNPCustDomainIpNetRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleProfile2.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainIpNetRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainIpNetRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainIpNetRuleProfile3_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleProfile3 = _AlaDaUNPCustDomainIpNetRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 15, 1, 14),
    _AlaDaUNPCustDomainIpNetRuleProfile3_Type()
)
alaDaUNPCustDomainIpNetRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleProfile3.setStatus("current")
_AlaDaUNPCustDomainMacRuleTable_Object = MibTable
alaDaUNPCustDomainMacRuleTable = _AlaDaUNPCustDomainMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleTable.setStatus("current")
_AlaDaUNPCustDomainMacRuleEntry_Object = MibTableRow
alaDaUNPCustDomainMacRuleEntry = _AlaDaUNPCustDomainMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1)
)
alaDaUNPCustDomainMacRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainMacRuleDomainId_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacRuleDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUNPCustDomainMacRuleDomainId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacRuleDomainId_Object = MibTableColumn
alaDaUNPCustDomainMacRuleDomainId = _AlaDaUNPCustDomainMacRuleDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 1),
    _AlaDaUNPCustDomainMacRuleDomainId_Type()
)
alaDaUNPCustDomainMacRuleDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleDomainId.setStatus("current")
_AlaDaUNPCustDomainMacRuleAddr_Type = MacAddress
_AlaDaUNPCustDomainMacRuleAddr_Object = MibTableColumn
alaDaUNPCustDomainMacRuleAddr = _AlaDaUNPCustDomainMacRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 2),
    _AlaDaUNPCustDomainMacRuleAddr_Type()
)
alaDaUNPCustDomainMacRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleAddr.setStatus("current")


class _AlaDaUNPCustDomainMacRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainMacRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRuleProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRuleProfileName = _AlaDaUNPCustDomainMacRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 3),
    _AlaDaUNPCustDomainMacRuleProfileName_Type()
)
alaDaUNPCustDomainMacRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainMacRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPCustDomainMacRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacRuleVlanTag_Object = MibTableColumn
alaDaUNPCustDomainMacRuleVlanTag = _AlaDaUNPCustDomainMacRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 4),
    _AlaDaUNPCustDomainMacRuleVlanTag_Type()
)
alaDaUNPCustDomainMacRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleVlanTag.setStatus("current")
_AlaDaUNPCustDomainMacRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainMacRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainMacRuleRowStatus = _AlaDaUNPCustDomainMacRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 5),
    _AlaDaUNPCustDomainMacRuleRowStatus_Type()
)
alaDaUNPCustDomainMacRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainMacRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPCustDomainMacRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPCustDomainMacRuleMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPCustDomainMacRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPCustDomainMacRuleMCLagConfigStatus = _AlaDaUNPCustDomainMacRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 6),
    _AlaDaUNPCustDomainMacRuleMCLagConfigStatus_Type()
)
alaDaUNPCustDomainMacRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleMCLagConfigStatus.setStatus("current")


class _AlaDaUNPCustDomainMacRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainMacRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRuleSpbProfileName = _AlaDaUNPCustDomainMacRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 7),
    _AlaDaUNPCustDomainMacRuleSpbProfileName_Type()
)
alaDaUNPCustDomainMacRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleSpbProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainMacRuleEdgeProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRuleEdgeProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainMacRuleEdgeProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRuleEdgeProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRuleEdgeProfileName = _AlaDaUNPCustDomainMacRuleEdgeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 8),
    _AlaDaUNPCustDomainMacRuleEdgeProfileName_Type()
)
alaDaUNPCustDomainMacRuleEdgeProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleEdgeProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainMacRuleVxlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRuleVxlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRuleVxlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRuleVxlanProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRuleVxlanProfileName = _AlaDaUNPCustDomainMacRuleVxlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 9),
    _AlaDaUNPCustDomainMacRuleVxlanProfileName_Type()
)
alaDaUNPCustDomainMacRuleVxlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleVxlanProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainMacRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRuleProfile1_Object = MibTableColumn
alaDaUNPCustDomainMacRuleProfile1 = _AlaDaUNPCustDomainMacRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 10),
    _AlaDaUNPCustDomainMacRuleProfile1_Type()
)
alaDaUNPCustDomainMacRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleProfile1.setStatus("current")


class _AlaDaUNPCustDomainMacRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRuleProfile2_Object = MibTableColumn
alaDaUNPCustDomainMacRuleProfile2 = _AlaDaUNPCustDomainMacRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 11),
    _AlaDaUNPCustDomainMacRuleProfile2_Type()
)
alaDaUNPCustDomainMacRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleProfile2.setStatus("current")


class _AlaDaUNPCustDomainMacRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRuleProfile3_Object = MibTableColumn
alaDaUNPCustDomainMacRuleProfile3 = _AlaDaUNPCustDomainMacRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 16, 1, 12),
    _AlaDaUNPCustDomainMacRuleProfile3_Type()
)
alaDaUNPCustDomainMacRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleProfile3.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleTable_Object = MibTable
alaDaUNPCustDomainMacRangeRuleTable = _AlaDaUNPCustDomainMacRangeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleTable.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleEntry_Object = MibTableRow
alaDaUNPCustDomainMacRangeRuleEntry = _AlaDaUNPCustDomainMacRangeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1)
)
alaDaUNPCustDomainMacRangeRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleLoAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleDomainId_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacRangeRuleDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUNPCustDomainMacRangeRuleDomainId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacRangeRuleDomainId_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleDomainId = _AlaDaUNPCustDomainMacRangeRuleDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 1),
    _AlaDaUNPCustDomainMacRangeRuleDomainId_Type()
)
alaDaUNPCustDomainMacRangeRuleDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleDomainId.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleLoAddr_Type = MacAddress
_AlaDaUNPCustDomainMacRangeRuleLoAddr_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleLoAddr = _AlaDaUNPCustDomainMacRangeRuleLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 2),
    _AlaDaUNPCustDomainMacRangeRuleLoAddr_Type()
)
alaDaUNPCustDomainMacRangeRuleLoAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleLoAddr.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleHiAddr_Type = MacAddress
_AlaDaUNPCustDomainMacRangeRuleHiAddr_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleHiAddr = _AlaDaUNPCustDomainMacRangeRuleHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 3),
    _AlaDaUNPCustDomainMacRangeRuleHiAddr_Type()
)
alaDaUNPCustDomainMacRangeRuleHiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleHiAddr.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRangeRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRangeRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRangeRuleProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleProfileName = _AlaDaUNPCustDomainMacRangeRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 4),
    _AlaDaUNPCustDomainMacRangeRuleProfileName_Type()
)
alaDaUNPCustDomainMacRangeRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainMacRangeRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacRangeRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPCustDomainMacRangeRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacRangeRuleVlanTag_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleVlanTag = _AlaDaUNPCustDomainMacRangeRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 5),
    _AlaDaUNPCustDomainMacRangeRuleVlanTag_Type()
)
alaDaUNPCustDomainMacRangeRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleVlanTag.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainMacRangeRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleRowStatus = _AlaDaUNPCustDomainMacRangeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 6),
    _AlaDaUNPCustDomainMacRangeRuleRowStatus_Type()
)
alaDaUNPCustDomainMacRangeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""
    defaultValue = 1


_AlaDaUNPCustDomainMacRangeRuleMCLagConfigStatus_Type.__name__ = "AlaMultiChassisConfigStatus"
_AlaDaUNPCustDomainMacRangeRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus = _AlaDaUNPCustDomainMacRangeRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 7),
    _AlaDaUNPCustDomainMacRangeRuleMCLagConfigStatus_Type()
)
alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRangeRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleSpbProfileName = _AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 8),
    _AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Type()
)
alaDaUNPCustDomainMacRangeRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleSpbProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainMacRangeRuleEdgeProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRangeRuleEdgeProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRangeRuleEdgeProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRangeRuleEdgeProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleEdgeProfileName = _AlaDaUNPCustDomainMacRangeRuleEdgeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 9),
    _AlaDaUNPCustDomainMacRangeRuleEdgeProfileName_Type()
)
alaDaUNPCustDomainMacRangeRuleEdgeProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleEdgeProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainMacRangeRuleVxlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRangeRuleVxlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRangeRuleVxlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRangeRuleVxlanProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleVxlanProfileName = _AlaDaUNPCustDomainMacRangeRuleVxlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 10),
    _AlaDaUNPCustDomainMacRangeRuleVxlanProfileName_Type()
)
alaDaUNPCustDomainMacRangeRuleVxlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleVxlanProfileName.setStatus("deprecated")


class _AlaDaUNPCustDomainMacRangeRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRangeRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRangeRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRangeRuleProfile1_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleProfile1 = _AlaDaUNPCustDomainMacRangeRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 11),
    _AlaDaUNPCustDomainMacRangeRuleProfile1_Type()
)
alaDaUNPCustDomainMacRangeRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleProfile1.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRangeRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRangeRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRangeRuleProfile2_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleProfile2 = _AlaDaUNPCustDomainMacRangeRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 12),
    _AlaDaUNPCustDomainMacRangeRuleProfile2_Type()
)
alaDaUNPCustDomainMacRangeRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleProfile2.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRangeRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRangeRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRangeRuleProfile3_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleProfile3 = _AlaDaUNPCustDomainMacRangeRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 17, 1, 13),
    _AlaDaUNPCustDomainMacRangeRuleProfile3_Type()
)
alaDaUNPCustDomainMacRangeRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleProfile3.setStatus("current")
_AlaDaSaaProfileTable_Object = MibTable
alaDaSaaProfileTable = _AlaDaSaaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 18)
)
if mibBuilder.loadTexts:
    alaDaSaaProfileTable.setStatus("current")
_AlaDaSaaProfileEntry_Object = MibTableRow
alaDaSaaProfileEntry = _AlaDaSaaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 18, 1)
)
alaDaSaaProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaSaaProfileName"),
)
if mibBuilder.loadTexts:
    alaDaSaaProfileEntry.setStatus("current")


class _AlaDaSaaProfileName_Type(SnmpAdminString):
    """Custom type alaDaSaaProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaSaaProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaSaaProfileName_Object = MibTableColumn
alaDaSaaProfileName = _AlaDaSaaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 18, 1, 1),
    _AlaDaSaaProfileName_Type()
)
alaDaSaaProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaSaaProfileName.setStatus("current")


class _AlaDaSaaProfileLatencyThreshold_Type(Integer32):
    """Custom type alaDaSaaProfileLatencyThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_AlaDaSaaProfileLatencyThreshold_Type.__name__ = "Integer32"
_AlaDaSaaProfileLatencyThreshold_Object = MibTableColumn
alaDaSaaProfileLatencyThreshold = _AlaDaSaaProfileLatencyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 18, 1, 4),
    _AlaDaSaaProfileLatencyThreshold_Type()
)
alaDaSaaProfileLatencyThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSaaProfileLatencyThreshold.setStatus("current")


class _AlaDaSaaProfileJitterThreshold_Type(Integer32):
    """Custom type alaDaSaaProfileJitterThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_AlaDaSaaProfileJitterThreshold_Type.__name__ = "Integer32"
_AlaDaSaaProfileJitterThreshold_Object = MibTableColumn
alaDaSaaProfileJitterThreshold = _AlaDaSaaProfileJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 18, 1, 5),
    _AlaDaSaaProfileJitterThreshold_Type()
)
alaDaSaaProfileJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSaaProfileJitterThreshold.setStatus("current")
_AlaDaSaaProfileRowStatus_Type = RowStatus
_AlaDaSaaProfileRowStatus_Object = MibTableColumn
alaDaSaaProfileRowStatus = _AlaDaSaaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 18, 1, 6),
    _AlaDaSaaProfileRowStatus_Type()
)
alaDaSaaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSaaProfileRowStatus.setStatus("current")
_AlaDaCPortalMIBObjects_ObjectIdentity = ObjectIdentity
alaDaCPortalMIBObjects = _AlaDaCPortalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19)
)
_AlaDaCPortalGlobalConfig_ObjectIdentity = ObjectIdentity
alaDaCPortalGlobalConfig = _AlaDaCPortalGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1)
)


class _AlaDaCPortalRedirectUrlName_Type(SnmpAdminString):
    """Custom type alaDaCPortalRedirectUrlName based on SnmpAdminString"""
    defaultValue = OctetString("captive-portal")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaCPortalRedirectUrlName_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalRedirectUrlName_Object = MibScalar
alaDaCPortalRedirectUrlName = _AlaDaCPortalRedirectUrlName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 1),
    _AlaDaCPortalRedirectUrlName_Type()
)
alaDaCPortalRedirectUrlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalRedirectUrlName.setStatus("current")


class _AlaDaCPortalIpAddressType_Type(InetAddressType):
    """Custom type alaDaCPortalIpAddressType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaCPortalIpAddressType_Type.__name__ = "InetAddressType"
_AlaDaCPortalIpAddressType_Object = MibScalar
alaDaCPortalIpAddressType = _AlaDaCPortalIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 2),
    _AlaDaCPortalIpAddressType_Type()
)
alaDaCPortalIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalIpAddressType.setStatus("current")


class _AlaDaCPortalIpAddress_Type(InetAddress):
    """Custom type alaDaCPortalIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaCPortalIpAddress_Type.__name__ = "InetAddress"
_AlaDaCPortalIpAddress_Object = MibScalar
alaDaCPortalIpAddress = _AlaDaCPortalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 3),
    _AlaDaCPortalIpAddress_Type()
)
alaDaCPortalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalIpAddress.setStatus("current")


class _AlaDaCPortalMode_Type(Integer32):
    """Custom type alaDaCPortalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2),
          ("internalDhcp", 3))
    )


_AlaDaCPortalMode_Type.__name__ = "Integer32"
_AlaDaCPortalMode_Object = MibScalar
alaDaCPortalMode = _AlaDaCPortalMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 4),
    _AlaDaCPortalMode_Type()
)
alaDaCPortalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalMode.setStatus("current")


class _AlaDaCPortalSuccRedirectUrl_Type(SnmpAdminString):
    """Custom type alaDaCPortalSuccRedirectUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDaCPortalSuccRedirectUrl_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalSuccRedirectUrl_Object = MibScalar
alaDaCPortalSuccRedirectUrl = _AlaDaCPortalSuccRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 5),
    _AlaDaCPortalSuccRedirectUrl_Type()
)
alaDaCPortalSuccRedirectUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalSuccRedirectUrl.setStatus("current")


class _AlaDaCPortalProxyPort_Type(Integer32):
    """Custom type alaDaCPortalProxyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1024, 49151),
    )


_AlaDaCPortalProxyPort_Type.__name__ = "Integer32"
_AlaDaCPortalProxyPort_Object = MibScalar
alaDaCPortalProxyPort = _AlaDaCPortalProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 6),
    _AlaDaCPortalProxyPort_Type()
)
alaDaCPortalProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalProxyPort.setStatus("current")


class _AlaDaCPortalRetryCnt_Type(Integer32):
    """Custom type alaDaCPortalRetryCnt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AlaDaCPortalRetryCnt_Type.__name__ = "Integer32"
_AlaDaCPortalRetryCnt_Object = MibScalar
alaDaCPortalRetryCnt = _AlaDaCPortalRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 7),
    _AlaDaCPortalRetryCnt_Type()
)
alaDaCPortalRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalRetryCnt.setStatus("current")


class _AlaDaCPortalPolicyListName_Type(SnmpAdminString):
    """Custom type alaDaCPortalPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaCPortalPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalPolicyListName_Object = MibScalar
alaDaCPortalPolicyListName = _AlaDaCPortalPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 8),
    _AlaDaCPortalPolicyListName_Type()
)
alaDaCPortalPolicyListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalPolicyListName.setStatus("current")


class _AlaDaCPortalCustomization_Type(Integer32):
    """Custom type alaDaCPortalCustomization based on Integer32"""
    defaultValue = 2

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


_AlaDaCPortalCustomization_Type.__name__ = "Integer32"
_AlaDaCPortalCustomization_Object = MibScalar
alaDaCPortalCustomization = _AlaDaCPortalCustomization_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 9),
    _AlaDaCPortalCustomization_Type()
)
alaDaCPortalCustomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalCustomization.setStatus("current")


class _AlaDaCPortalUNPProfile_Type(SnmpAdminString):
    """Custom type alaDaCPortalUNPProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaCPortalUNPProfile_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalUNPProfile_Object = MibScalar
alaDaCPortalUNPProfile = _AlaDaCPortalUNPProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 10),
    _AlaDaCPortalUNPProfile_Type()
)
alaDaCPortalUNPProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalUNPProfile.setStatus("current")


class _AlaDaCPortalUNPProfileChange_Type(Integer32):
    """Custom type alaDaCPortalUNPProfileChange based on Integer32"""
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


_AlaDaCPortalUNPProfileChange_Type.__name__ = "Integer32"
_AlaDaCPortalUNPProfileChange_Object = MibScalar
alaDaCPortalUNPProfileChange = _AlaDaCPortalUNPProfileChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 11),
    _AlaDaCPortalUNPProfileChange_Type()
)
alaDaCPortalUNPProfileChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalUNPProfileChange.setStatus("current")


class _AlaDaCPortalDHCPLeaseTime_Type(Integer32):
    """Custom type alaDaCPortalDHCPLeaseTime based on Integer32"""
    defaultValue = 30


_AlaDaCPortalDHCPLeaseTime_Type.__name__ = "Integer32"
_AlaDaCPortalDHCPLeaseTime_Object = MibScalar
alaDaCPortalDHCPLeaseTime = _AlaDaCPortalDHCPLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 12),
    _AlaDaCPortalDHCPLeaseTime_Type()
)
alaDaCPortalDHCPLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalDHCPLeaseTime.setStatus("current")


class _AlaDaCPortalDHCPRenewTime_Type(Integer32):
    """Custom type alaDaCPortalDHCPRenewTime based on Integer32"""
    defaultValue = 15


_AlaDaCPortalDHCPRenewTime_Type.__name__ = "Integer32"
_AlaDaCPortalDHCPRenewTime_Object = MibScalar
alaDaCPortalDHCPRenewTime = _AlaDaCPortalDHCPRenewTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 13),
    _AlaDaCPortalDHCPRenewTime_Type()
)
alaDaCPortalDHCPRenewTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalDHCPRenewTime.setStatus("current")


class _AlaDaCPortalDHCPRebindingTime_Type(Integer32):
    """Custom type alaDaCPortalDHCPRebindingTime based on Integer32"""
    defaultValue = 22


_AlaDaCPortalDHCPRebindingTime_Type.__name__ = "Integer32"
_AlaDaCPortalDHCPRebindingTime_Object = MibScalar
alaDaCPortalDHCPRebindingTime = _AlaDaCPortalDHCPRebindingTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 1, 14),
    _AlaDaCPortalDHCPRebindingTime_Type()
)
alaDaCPortalDHCPRebindingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaCPortalDHCPRebindingTime.setStatus("current")
_AlaDaCPortalAuthPassTable_Object = MibTable
alaDaCPortalAuthPassTable = _AlaDaCPortalAuthPassTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 2)
)
if mibBuilder.loadTexts:
    alaDaCPortalAuthPassTable.setStatus("current")
_AlaDaCPortalAuthPassEntry_Object = MibTableRow
alaDaCPortalAuthPassEntry = _AlaDaCPortalAuthPassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 2, 1)
)
alaDaCPortalAuthPassEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaCPortalAuthDomainName"),
)
if mibBuilder.loadTexts:
    alaDaCPortalAuthPassEntry.setStatus("current")


class _AlaDaCPortalAuthDomainName_Type(SnmpAdminString):
    """Custom type alaDaCPortalAuthDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaCPortalAuthDomainName_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalAuthDomainName_Object = MibTableColumn
alaDaCPortalAuthDomainName = _AlaDaCPortalAuthDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 2, 1, 1),
    _AlaDaCPortalAuthDomainName_Type()
)
alaDaCPortalAuthDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaCPortalAuthDomainName.setStatus("current")


class _AlaDaCPortalAuthRealm_Type(Integer32):
    """Custom type alaDaCPortalAuthRealm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prefix", 1),
          ("suffix", 2))
    )


_AlaDaCPortalAuthRealm_Type.__name__ = "Integer32"
_AlaDaCPortalAuthRealm_Object = MibTableColumn
alaDaCPortalAuthRealm = _AlaDaCPortalAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 2, 1, 2),
    _AlaDaCPortalAuthRealm_Type()
)
alaDaCPortalAuthRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalAuthRealm.setStatus("current")


class _AlaDaCPortalAuthPolicyListName_Type(SnmpAdminString):
    """Custom type alaDaCPortalAuthPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaCPortalAuthPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalAuthPolicyListName_Object = MibTableColumn
alaDaCPortalAuthPolicyListName = _AlaDaCPortalAuthPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 2, 1, 3),
    _AlaDaCPortalAuthPolicyListName_Type()
)
alaDaCPortalAuthPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalAuthPolicyListName.setStatus("current")
_AlaDaCPortalAuthRowStatus_Type = RowStatus
_AlaDaCPortalAuthRowStatus_Object = MibTableColumn
alaDaCPortalAuthRowStatus = _AlaDaCPortalAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 2, 1, 4),
    _AlaDaCPortalAuthRowStatus_Type()
)
alaDaCPortalAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalAuthRowStatus.setStatus("current")


class _AlaDaCPortalAuthUNPProfile_Type(SnmpAdminString):
    """Custom type alaDaCPortalAuthUNPProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaCPortalAuthUNPProfile_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalAuthUNPProfile_Object = MibTableColumn
alaDaCPortalAuthUNPProfile = _AlaDaCPortalAuthUNPProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 2, 1, 5),
    _AlaDaCPortalAuthUNPProfile_Type()
)
alaDaCPortalAuthUNPProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalAuthUNPProfile.setStatus("current")


class _AlaDaCPortalAuthUNPProfileChange_Type(Integer32):
    """Custom type alaDaCPortalAuthUNPProfileChange based on Integer32"""
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


_AlaDaCPortalAuthUNPProfileChange_Type.__name__ = "Integer32"
_AlaDaCPortalAuthUNPProfileChange_Object = MibTableColumn
alaDaCPortalAuthUNPProfileChange = _AlaDaCPortalAuthUNPProfileChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 2, 1, 6),
    _AlaDaCPortalAuthUNPProfileChange_Type()
)
alaDaCPortalAuthUNPProfileChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalAuthUNPProfileChange.setStatus("current")
_AlaDaCPortalProfTable_Object = MibTable
alaDaCPortalProfTable = _AlaDaCPortalProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3)
)
if mibBuilder.loadTexts:
    alaDaCPortalProfTable.setStatus("current")
_AlaDaCPortalProfEntry_Object = MibTableRow
alaDaCPortalProfEntry = _AlaDaCPortalProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1)
)
alaDaCPortalProfEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaCPortalProfName"),
)
if mibBuilder.loadTexts:
    alaDaCPortalProfEntry.setStatus("current")


class _AlaDaCPortalProfName_Type(SnmpAdminString):
    """Custom type alaDaCPortalProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaCPortalProfName_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalProfName_Object = MibTableColumn
alaDaCPortalProfName = _AlaDaCPortalProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1, 1),
    _AlaDaCPortalProfName_Type()
)
alaDaCPortalProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaCPortalProfName.setStatus("current")


class _AlaDaCPortalProfMode_Type(Integer32):
    """Custom type alaDaCPortalProfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_AlaDaCPortalProfMode_Type.__name__ = "Integer32"
_AlaDaCPortalProfMode_Object = MibTableColumn
alaDaCPortalProfMode = _AlaDaCPortalProfMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1, 2),
    _AlaDaCPortalProfMode_Type()
)
alaDaCPortalProfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfMode.setStatus("current")


class _AlaDaCPortalProfSuccRedirectUrl_Type(SnmpAdminString):
    """Custom type alaDaCPortalProfSuccRedirectUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDaCPortalProfSuccRedirectUrl_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalProfSuccRedirectUrl_Object = MibTableColumn
alaDaCPortalProfSuccRedirectUrl = _AlaDaCPortalProfSuccRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1, 3),
    _AlaDaCPortalProfSuccRedirectUrl_Type()
)
alaDaCPortalProfSuccRedirectUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfSuccRedirectUrl.setStatus("current")


class _AlaDaCPortalProfRetryCnt_Type(Integer32):
    """Custom type alaDaCPortalProfRetryCnt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AlaDaCPortalProfRetryCnt_Type.__name__ = "Integer32"
_AlaDaCPortalProfRetryCnt_Object = MibTableColumn
alaDaCPortalProfRetryCnt = _AlaDaCPortalProfRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1, 4),
    _AlaDaCPortalProfRetryCnt_Type()
)
alaDaCPortalProfRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfRetryCnt.setStatus("current")


class _AlaDaCPortalProfAuthPolicyListName_Type(SnmpAdminString):
    """Custom type alaDaCPortalProfAuthPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaCPortalProfAuthPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalProfAuthPolicyListName_Object = MibTableColumn
alaDaCPortalProfAuthPolicyListName = _AlaDaCPortalProfAuthPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1, 5),
    _AlaDaCPortalProfAuthPolicyListName_Type()
)
alaDaCPortalProfAuthPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfAuthPolicyListName.setStatus("current")


class _AlaDaCPortalProfAaaProf_Type(SnmpAdminString):
    """Custom type alaDaCPortalProfAaaProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaCPortalProfAaaProf_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalProfAaaProf_Object = MibTableColumn
alaDaCPortalProfAaaProf = _AlaDaCPortalProfAaaProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1, 6),
    _AlaDaCPortalProfAaaProf_Type()
)
alaDaCPortalProfAaaProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfAaaProf.setStatus("current")
_AlaDaCPortalProfRowStatus_Type = RowStatus
_AlaDaCPortalProfRowStatus_Object = MibTableColumn
alaDaCPortalProfRowStatus = _AlaDaCPortalProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1, 7),
    _AlaDaCPortalProfRowStatus_Type()
)
alaDaCPortalProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfRowStatus.setStatus("current")


class _AlaDaCPortalProfUNPProfile_Type(SnmpAdminString):
    """Custom type alaDaCPortalProfUNPProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaCPortalProfUNPProfile_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalProfUNPProfile_Object = MibTableColumn
alaDaCPortalProfUNPProfile = _AlaDaCPortalProfUNPProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1, 8),
    _AlaDaCPortalProfUNPProfile_Type()
)
alaDaCPortalProfUNPProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfUNPProfile.setStatus("current")


class _AlaDaCPortalProfUNPProfileChange_Type(Integer32):
    """Custom type alaDaCPortalProfUNPProfileChange based on Integer32"""
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


_AlaDaCPortalProfUNPProfileChange_Type.__name__ = "Integer32"
_AlaDaCPortalProfUNPProfileChange_Object = MibTableColumn
alaDaCPortalProfUNPProfileChange = _AlaDaCPortalProfUNPProfileChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 3, 1, 9),
    _AlaDaCPortalProfUNPProfileChange_Type()
)
alaDaCPortalProfUNPProfileChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfUNPProfileChange.setStatus("current")
_AlaDaCPortalProfDomainTable_Object = MibTable
alaDaCPortalProfDomainTable = _AlaDaCPortalProfDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 4)
)
if mibBuilder.loadTexts:
    alaDaCPortalProfDomainTable.setStatus("current")
_AlaDaCPortalProfDomainEntry_Object = MibTableRow
alaDaCPortalProfDomainEntry = _AlaDaCPortalProfDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 4, 1)
)
alaDaCPortalProfDomainEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaCPortalProfName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaCPortalProfDomainAuthDomainName"),
)
if mibBuilder.loadTexts:
    alaDaCPortalProfDomainEntry.setStatus("current")


class _AlaDaCPortalProfDomainAuthDomainName_Type(SnmpAdminString):
    """Custom type alaDaCPortalProfDomainAuthDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaCPortalProfDomainAuthDomainName_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalProfDomainAuthDomainName_Object = MibTableColumn
alaDaCPortalProfDomainAuthDomainName = _AlaDaCPortalProfDomainAuthDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 4, 1, 1),
    _AlaDaCPortalProfDomainAuthDomainName_Type()
)
alaDaCPortalProfDomainAuthDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaCPortalProfDomainAuthDomainName.setStatus("current")


class _AlaDaCPortalProfDomainAuthPolicyListName_Type(SnmpAdminString):
    """Custom type alaDaCPortalProfDomainAuthPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaCPortalProfDomainAuthPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalProfDomainAuthPolicyListName_Object = MibTableColumn
alaDaCPortalProfDomainAuthPolicyListName = _AlaDaCPortalProfDomainAuthPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 4, 1, 2),
    _AlaDaCPortalProfDomainAuthPolicyListName_Type()
)
alaDaCPortalProfDomainAuthPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfDomainAuthPolicyListName.setStatus("current")


class _AlaDaCPortalProfDomainAuthRealm_Type(Integer32):
    """Custom type alaDaCPortalProfDomainAuthRealm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prefix", 1),
          ("suffix", 2))
    )


_AlaDaCPortalProfDomainAuthRealm_Type.__name__ = "Integer32"
_AlaDaCPortalProfDomainAuthRealm_Object = MibTableColumn
alaDaCPortalProfDomainAuthRealm = _AlaDaCPortalProfDomainAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 4, 1, 3),
    _AlaDaCPortalProfDomainAuthRealm_Type()
)
alaDaCPortalProfDomainAuthRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfDomainAuthRealm.setStatus("current")
_AlaDaCPortalProfDomainRowStatus_Type = RowStatus
_AlaDaCPortalProfDomainRowStatus_Object = MibTableColumn
alaDaCPortalProfDomainRowStatus = _AlaDaCPortalProfDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 4, 1, 4),
    _AlaDaCPortalProfDomainRowStatus_Type()
)
alaDaCPortalProfDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfDomainRowStatus.setStatus("current")


class _AlaDaCPortalProfDomainUNPProfile_Type(SnmpAdminString):
    """Custom type alaDaCPortalProfDomainUNPProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaCPortalProfDomainUNPProfile_Type.__name__ = "SnmpAdminString"
_AlaDaCPortalProfDomainUNPProfile_Object = MibTableColumn
alaDaCPortalProfDomainUNPProfile = _AlaDaCPortalProfDomainUNPProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 4, 1, 5),
    _AlaDaCPortalProfDomainUNPProfile_Type()
)
alaDaCPortalProfDomainUNPProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfDomainUNPProfile.setStatus("current")


class _AlaDaCPortalProfDomainUNPProfileChange_Type(Integer32):
    """Custom type alaDaCPortalProfDomainUNPProfileChange based on Integer32"""
    defaultValue = 1

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


_AlaDaCPortalProfDomainUNPProfileChange_Type.__name__ = "Integer32"
_AlaDaCPortalProfDomainUNPProfileChange_Object = MibTableColumn
alaDaCPortalProfDomainUNPProfileChange = _AlaDaCPortalProfDomainUNPProfileChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 19, 4, 1, 6),
    _AlaDaCPortalProfDomainUNPProfileChange_Type()
)
alaDaCPortalProfDomainUNPProfileChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaCPortalProfDomainUNPProfileChange.setStatus("current")
_AlaDaHICMIBObjects_ObjectIdentity = ObjectIdentity
alaDaHICMIBObjects = _AlaDaHICMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20)
)
_AlaDaHICGlobalConfig_ObjectIdentity = ObjectIdentity
alaDaHICGlobalConfig = _AlaDaHICGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 1)
)


class _AlaDaHICStatus_Type(Integer32):
    """Custom type alaDaHICStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaHICStatus_Type.__name__ = "Integer32"
_AlaDaHICStatus_Object = MibScalar
alaDaHICStatus = _AlaDaHICStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 1, 1),
    _AlaDaHICStatus_Type()
)
alaDaHICStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaHICStatus.setStatus("current")


class _AlaDaHICWebAgentDownloadUrl_Type(SnmpAdminString):
    """Custom type alaDaHICWebAgentDownloadUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDaHICWebAgentDownloadUrl_Type.__name__ = "SnmpAdminString"
_AlaDaHICWebAgentDownloadUrl_Object = MibScalar
alaDaHICWebAgentDownloadUrl = _AlaDaHICWebAgentDownloadUrl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 1, 2),
    _AlaDaHICWebAgentDownloadUrl_Type()
)
alaDaHICWebAgentDownloadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaHICWebAgentDownloadUrl.setStatus("current")


class _AlaDaHICCustomHttpProxyPort_Type(Integer32):
    """Custom type alaDaHICCustomHttpProxyPort based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_AlaDaHICCustomHttpProxyPort_Type.__name__ = "Integer32"
_AlaDaHICCustomHttpProxyPort_Object = MibScalar
alaDaHICCustomHttpProxyPort = _AlaDaHICCustomHttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 1, 3),
    _AlaDaHICCustomHttpProxyPort_Type()
)
alaDaHICCustomHttpProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaHICCustomHttpProxyPort.setStatus("current")


class _AlaDaHICBgPollInterval_Type(Integer32):
    """Custom type alaDaHICBgPollInterval based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(176, 176),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(256, 256),
    )


_AlaDaHICBgPollInterval_Type.__name__ = "Integer32"
_AlaDaHICBgPollInterval_Object = MibScalar
alaDaHICBgPollInterval = _AlaDaHICBgPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 1, 4),
    _AlaDaHICBgPollInterval_Type()
)
alaDaHICBgPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaHICBgPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaDaHICBgPollInterval.setUnits("seconds")


class _AlaDaHICSvrFailMode_Type(Integer32):
    """Custom type alaDaHICSvrFailMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hold", 1),
          ("passthrough", 2))
    )


_AlaDaHICSvrFailMode_Type.__name__ = "Integer32"
_AlaDaHICSvrFailMode_Object = MibScalar
alaDaHICSvrFailMode = _AlaDaHICSvrFailMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 1, 5),
    _AlaDaHICSvrFailMode_Type()
)
alaDaHICSvrFailMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaHICSvrFailMode.setStatus("current")
_AlaDaHICSvrTable_Object = MibTable
alaDaHICSvrTable = _AlaDaHICSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    alaDaHICSvrTable.setStatus("current")
_AlaDaHICSvrEntry_Object = MibTableRow
alaDaHICSvrEntry = _AlaDaHICSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1)
)
alaDaHICSvrEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaHICSvrName"),
)
if mibBuilder.loadTexts:
    alaDaHICSvrEntry.setStatus("current")


class _AlaDaHICSvrName_Type(SnmpAdminString):
    """Custom type alaDaHICSvrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaDaHICSvrName_Type.__name__ = "SnmpAdminString"
_AlaDaHICSvrName_Object = MibTableColumn
alaDaHICSvrName = _AlaDaHICSvrName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1, 1),
    _AlaDaHICSvrName_Type()
)
alaDaHICSvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaHICSvrName.setStatus("current")


class _AlaDaHICSvrIpAddrType_Type(InetAddressType):
    """Custom type alaDaHICSvrIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaHICSvrIpAddrType_Type.__name__ = "InetAddressType"
_AlaDaHICSvrIpAddrType_Object = MibTableColumn
alaDaHICSvrIpAddrType = _AlaDaHICSvrIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1, 2),
    _AlaDaHICSvrIpAddrType_Type()
)
alaDaHICSvrIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICSvrIpAddrType.setStatus("current")


class _AlaDaHICSvrIpAddr_Type(InetAddress):
    """Custom type alaDaHICSvrIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaHICSvrIpAddr_Type.__name__ = "InetAddress"
_AlaDaHICSvrIpAddr_Object = MibTableColumn
alaDaHICSvrIpAddr = _AlaDaHICSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1, 3),
    _AlaDaHICSvrIpAddr_Type()
)
alaDaHICSvrIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICSvrIpAddr.setStatus("current")


class _AlaDaHICSvrPort_Type(Integer32):
    """Custom type alaDaHICSvrPort based on Integer32"""
    defaultValue = 11707

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_AlaDaHICSvrPort_Type.__name__ = "Integer32"
_AlaDaHICSvrPort_Object = MibTableColumn
alaDaHICSvrPort = _AlaDaHICSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1, 4),
    _AlaDaHICSvrPort_Type()
)
alaDaHICSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICSvrPort.setStatus("current")


class _AlaDaHICSvrKey_Type(SnmpAdminString):
    """Custom type alaDaHICSvrKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaDaHICSvrKey_Type.__name__ = "SnmpAdminString"
_AlaDaHICSvrKey_Object = MibTableColumn
alaDaHICSvrKey = _AlaDaHICSvrKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1, 5),
    _AlaDaHICSvrKey_Type()
)
alaDaHICSvrKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICSvrKey.setStatus("current")


class _AlaDaHICSvrStatus_Type(Integer32):
    """Custom type alaDaHICSvrStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_AlaDaHICSvrStatus_Type.__name__ = "Integer32"
_AlaDaHICSvrStatus_Object = MibTableColumn
alaDaHICSvrStatus = _AlaDaHICSvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1, 6),
    _AlaDaHICSvrStatus_Type()
)
alaDaHICSvrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaHICSvrStatus.setStatus("current")


class _AlaDaHICSvrRole_Type(Integer32):
    """Custom type alaDaHICSvrRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_AlaDaHICSvrRole_Type.__name__ = "Integer32"
_AlaDaHICSvrRole_Object = MibTableColumn
alaDaHICSvrRole = _AlaDaHICSvrRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1, 7),
    _AlaDaHICSvrRole_Type()
)
alaDaHICSvrRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaHICSvrRole.setStatus("current")


class _AlaDaHICSvrConnection_Type(Integer32):
    """Custom type alaDaHICSvrConnection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlaDaHICSvrConnection_Type.__name__ = "Integer32"
_AlaDaHICSvrConnection_Object = MibTableColumn
alaDaHICSvrConnection = _AlaDaHICSvrConnection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1, 8),
    _AlaDaHICSvrConnection_Type()
)
alaDaHICSvrConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaHICSvrConnection.setStatus("current")
_AlaDaHICSvrRowStatus_Type = RowStatus
_AlaDaHICSvrRowStatus_Object = MibTableColumn
alaDaHICSvrRowStatus = _AlaDaHICSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 2, 1, 9),
    _AlaDaHICSvrRowStatus_Type()
)
alaDaHICSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICSvrRowStatus.setStatus("current")
_AlaDaHICAllowedTable_Object = MibTable
alaDaHICAllowedTable = _AlaDaHICAllowedTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 3)
)
if mibBuilder.loadTexts:
    alaDaHICAllowedTable.setStatus("current")
_AlaDaHICAllowedEntry_Object = MibTableRow
alaDaHICAllowedEntry = _AlaDaHICAllowedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 3, 1)
)
alaDaHICAllowedEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaHICAllowedName"),
)
if mibBuilder.loadTexts:
    alaDaHICAllowedEntry.setStatus("current")


class _AlaDaHICAllowedName_Type(SnmpAdminString):
    """Custom type alaDaHICAllowedName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaDaHICAllowedName_Type.__name__ = "SnmpAdminString"
_AlaDaHICAllowedName_Object = MibTableColumn
alaDaHICAllowedName = _AlaDaHICAllowedName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 3, 1, 1),
    _AlaDaHICAllowedName_Type()
)
alaDaHICAllowedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaHICAllowedName.setStatus("current")


class _AlaDaHICAllowedIpAddrType_Type(InetAddressType):
    """Custom type alaDaHICAllowedIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaHICAllowedIpAddrType_Type.__name__ = "InetAddressType"
_AlaDaHICAllowedIpAddrType_Object = MibTableColumn
alaDaHICAllowedIpAddrType = _AlaDaHICAllowedIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 3, 1, 2),
    _AlaDaHICAllowedIpAddrType_Type()
)
alaDaHICAllowedIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICAllowedIpAddrType.setStatus("current")


class _AlaDaHICAllowedIpAddr_Type(InetAddress):
    """Custom type alaDaHICAllowedIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaHICAllowedIpAddr_Type.__name__ = "InetAddress"
_AlaDaHICAllowedIpAddr_Object = MibTableColumn
alaDaHICAllowedIpAddr = _AlaDaHICAllowedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 3, 1, 3),
    _AlaDaHICAllowedIpAddr_Type()
)
alaDaHICAllowedIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICAllowedIpAddr.setStatus("current")


class _AlaDaHICAllowedIpMaskType_Type(InetAddressType):
    """Custom type alaDaHICAllowedIpMaskType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaHICAllowedIpMaskType_Type.__name__ = "InetAddressType"
_AlaDaHICAllowedIpMaskType_Object = MibTableColumn
alaDaHICAllowedIpMaskType = _AlaDaHICAllowedIpMaskType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 3, 1, 4),
    _AlaDaHICAllowedIpMaskType_Type()
)
alaDaHICAllowedIpMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICAllowedIpMaskType.setStatus("current")


class _AlaDaHICAllowedIpMask_Type(InetAddress):
    """Custom type alaDaHICAllowedIpMask based on InetAddress"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaHICAllowedIpMask_Type.__name__ = "InetAddress"
_AlaDaHICAllowedIpMask_Object = MibTableColumn
alaDaHICAllowedIpMask = _AlaDaHICAllowedIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 3, 1, 5),
    _AlaDaHICAllowedIpMask_Type()
)
alaDaHICAllowedIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICAllowedIpMask.setStatus("current")
_AlaDaHICAllowedRowStatus_Type = RowStatus
_AlaDaHICAllowedRowStatus_Object = MibTableColumn
alaDaHICAllowedRowStatus = _AlaDaHICAllowedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 3, 1, 6),
    _AlaDaHICAllowedRowStatus_Type()
)
alaDaHICAllowedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICAllowedRowStatus.setStatus("current")
_AlaDaHICSvrFailPolicyTable_Object = MibTable
alaDaHICSvrFailPolicyTable = _AlaDaHICSvrFailPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 4)
)
if mibBuilder.loadTexts:
    alaDaHICSvrFailPolicyTable.setStatus("current")
_AlaDaHICSvrFailPolicyEntry_Object = MibTableRow
alaDaHICSvrFailPolicyEntry = _AlaDaHICSvrFailPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 4, 1)
)
alaDaHICSvrFailPolicyEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaHICSvrFailPolicyName"),
)
if mibBuilder.loadTexts:
    alaDaHICSvrFailPolicyEntry.setStatus("current")


class _AlaDaHICSvrFailPolicyName_Type(SnmpAdminString):
    """Custom type alaDaHICSvrFailPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaHICSvrFailPolicyName_Type.__name__ = "SnmpAdminString"
_AlaDaHICSvrFailPolicyName_Object = MibTableColumn
alaDaHICSvrFailPolicyName = _AlaDaHICSvrFailPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 4, 1, 1),
    _AlaDaHICSvrFailPolicyName_Type()
)
alaDaHICSvrFailPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaHICSvrFailPolicyName.setStatus("current")


class _AlaDaHICSvrFailChangedPolicyName_Type(SnmpAdminString):
    """Custom type alaDaHICSvrFailChangedPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaHICSvrFailChangedPolicyName_Type.__name__ = "SnmpAdminString"
_AlaDaHICSvrFailChangedPolicyName_Object = MibTableColumn
alaDaHICSvrFailChangedPolicyName = _AlaDaHICSvrFailChangedPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 4, 1, 2),
    _AlaDaHICSvrFailChangedPolicyName_Type()
)
alaDaHICSvrFailChangedPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICSvrFailChangedPolicyName.setStatus("current")
_AlaDaHICSvrFailRowStatus_Type = RowStatus
_AlaDaHICSvrFailRowStatus_Object = MibTableColumn
alaDaHICSvrFailRowStatus = _AlaDaHICSvrFailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 4, 1, 3),
    _AlaDaHICSvrFailRowStatus_Type()
)
alaDaHICSvrFailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaHICSvrFailRowStatus.setStatus("current")
_AlaDaHICHostTable_Object = MibTable
alaDaHICHostTable = _AlaDaHICHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 5)
)
if mibBuilder.loadTexts:
    alaDaHICHostTable.setStatus("current")
_AlaDaHICHostEntry_Object = MibTableRow
alaDaHICHostEntry = _AlaDaHICHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 5, 1)
)
alaDaHICHostEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaHICHostMac"),
)
if mibBuilder.loadTexts:
    alaDaHICHostEntry.setStatus("current")
_AlaDaHICHostMac_Type = MacAddress
_AlaDaHICHostMac_Object = MibTableColumn
alaDaHICHostMac = _AlaDaHICHostMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 5, 1, 1),
    _AlaDaHICHostMac_Type()
)
alaDaHICHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaHICHostMac.setStatus("current")


class _AlaDaHICHostStatus_Type(Integer32):
    """Custom type alaDaHICHostStatus based on Integer32"""
    defaultValue = 3

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
        *(("inprogress", 1),
          ("success", 2),
          ("fail", 3),
          ("timeout", 4))
    )


_AlaDaHICHostStatus_Type.__name__ = "Integer32"
_AlaDaHICHostStatus_Object = MibTableColumn
alaDaHICHostStatus = _AlaDaHICHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 20, 5, 1, 2),
    _AlaDaHICHostStatus_Type()
)
alaDaHICHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaHICHostStatus.setStatus("current")
_AlaDaUNPETmplTable_Object = MibTable
alaDaUNPETmplTable = _AlaDaUNPETmplTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21)
)
if mibBuilder.loadTexts:
    alaDaUNPETmplTable.setStatus("deprecated")
_AlaDaUNPETmplEntry_Object = MibTableRow
alaDaUNPETmplEntry = _AlaDaUNPETmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1)
)
alaDaUNPETmplEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPETmplName"),
)
if mibBuilder.loadTexts:
    alaDaUNPETmplEntry.setStatus("deprecated")


class _AlaDaUNPETmplName_Type(SnmpAdminString):
    """Custom type alaDaUNPETmplName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPETmplName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPETmplName_Object = MibTableColumn
alaDaUNPETmplName = _AlaDaUNPETmplName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 1),
    _AlaDaUNPETmplName_Type()
)
alaDaUNPETmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPETmplName.setStatus("deprecated")


class _AlaDaUNPETmpl8021XAuthStatus_Type(Integer32):
    """Custom type alaDaUNPETmpl8021XAuthStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPETmpl8021XAuthStatus_Type.__name__ = "Integer32"
_AlaDaUNPETmpl8021XAuthStatus_Object = MibTableColumn
alaDaUNPETmpl8021XAuthStatus = _AlaDaUNPETmpl8021XAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 2),
    _AlaDaUNPETmpl8021XAuthStatus_Type()
)
alaDaUNPETmpl8021XAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XAuthStatus.setStatus("deprecated")


class _AlaDaUNPETmpl8021XTxPeriodStatus_Type(Integer32):
    """Custom type alaDaUNPETmpl8021XTxPeriodStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPETmpl8021XTxPeriodStatus_Type.__name__ = "Integer32"
_AlaDaUNPETmpl8021XTxPeriodStatus_Object = MibTableColumn
alaDaUNPETmpl8021XTxPeriodStatus = _AlaDaUNPETmpl8021XTxPeriodStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 3),
    _AlaDaUNPETmpl8021XTxPeriodStatus_Type()
)
alaDaUNPETmpl8021XTxPeriodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XTxPeriodStatus.setStatus("deprecated")


class _AlaDaUNPETmpl8021XTxPeriod_Type(Integer32):
    """Custom type alaDaUNPETmpl8021XTxPeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AlaDaUNPETmpl8021XTxPeriod_Type.__name__ = "Integer32"
_AlaDaUNPETmpl8021XTxPeriod_Object = MibTableColumn
alaDaUNPETmpl8021XTxPeriod = _AlaDaUNPETmpl8021XTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 4),
    _AlaDaUNPETmpl8021XTxPeriod_Type()
)
alaDaUNPETmpl8021XTxPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XTxPeriod.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XTxPeriod.setUnits("seconds")


class _AlaDaUNPETmpl8021XSuppTimeoutStatus_Type(Integer32):
    """Custom type alaDaUNPETmpl8021XSuppTimeoutStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPETmpl8021XSuppTimeoutStatus_Type.__name__ = "Integer32"
_AlaDaUNPETmpl8021XSuppTimeoutStatus_Object = MibTableColumn
alaDaUNPETmpl8021XSuppTimeoutStatus = _AlaDaUNPETmpl8021XSuppTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 5),
    _AlaDaUNPETmpl8021XSuppTimeoutStatus_Type()
)
alaDaUNPETmpl8021XSuppTimeoutStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XSuppTimeoutStatus.setStatus("deprecated")


class _AlaDaUNPETmpl8021XSuppTimeOut_Type(Integer32):
    """Custom type alaDaUNPETmpl8021XSuppTimeOut based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AlaDaUNPETmpl8021XSuppTimeOut_Type.__name__ = "Integer32"
_AlaDaUNPETmpl8021XSuppTimeOut_Object = MibTableColumn
alaDaUNPETmpl8021XSuppTimeOut = _AlaDaUNPETmpl8021XSuppTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 6),
    _AlaDaUNPETmpl8021XSuppTimeOut_Type()
)
alaDaUNPETmpl8021XSuppTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XSuppTimeOut.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XSuppTimeOut.setUnits("seconds")


class _AlaDaUNPETmpl8021XMaxReqStatus_Type(Integer32):
    """Custom type alaDaUNPETmpl8021XMaxReqStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPETmpl8021XMaxReqStatus_Type.__name__ = "Integer32"
_AlaDaUNPETmpl8021XMaxReqStatus_Object = MibTableColumn
alaDaUNPETmpl8021XMaxReqStatus = _AlaDaUNPETmpl8021XMaxReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 7),
    _AlaDaUNPETmpl8021XMaxReqStatus_Type()
)
alaDaUNPETmpl8021XMaxReqStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XMaxReqStatus.setStatus("deprecated")


class _AlaDaUNPETmpl8021XMaxReq_Type(Integer32):
    """Custom type alaDaUNPETmpl8021XMaxReq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaDaUNPETmpl8021XMaxReq_Type.__name__ = "Integer32"
_AlaDaUNPETmpl8021XMaxReq_Object = MibTableColumn
alaDaUNPETmpl8021XMaxReq = _AlaDaUNPETmpl8021XMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 8),
    _AlaDaUNPETmpl8021XMaxReq_Type()
)
alaDaUNPETmpl8021XMaxReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XMaxReq.setStatus("deprecated")


class _AlaDaUNPETmpl8021XPassAltEProf_Type(SnmpAdminString):
    """Custom type alaDaUNPETmpl8021XPassAltEProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPETmpl8021XPassAltEProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPETmpl8021XPassAltEProf_Object = MibTableColumn
alaDaUNPETmpl8021XPassAltEProf = _AlaDaUNPETmpl8021XPassAltEProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 9),
    _AlaDaUNPETmpl8021XPassAltEProf_Type()
)
alaDaUNPETmpl8021XPassAltEProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmpl8021XPassAltEProf.setStatus("deprecated")


class _AlaDaUNPETmplMacAuthStatus_Type(Integer32):
    """Custom type alaDaUNPETmplMacAuthStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPETmplMacAuthStatus_Type.__name__ = "Integer32"
_AlaDaUNPETmplMacAuthStatus_Object = MibTableColumn
alaDaUNPETmplMacAuthStatus = _AlaDaUNPETmplMacAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 10),
    _AlaDaUNPETmplMacAuthStatus_Type()
)
alaDaUNPETmplMacAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplMacAuthStatus.setStatus("deprecated")


class _AlaDaUNPETmplMacPassAltEProf_Type(SnmpAdminString):
    """Custom type alaDaUNPETmplMacPassAltEProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPETmplMacPassAltEProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPETmplMacPassAltEProf_Object = MibTableColumn
alaDaUNPETmplMacPassAltEProf = _AlaDaUNPETmplMacPassAltEProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 11),
    _AlaDaUNPETmplMacPassAltEProf_Type()
)
alaDaUNPETmplMacPassAltEProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplMacPassAltEProf.setStatus("deprecated")


class _AlaDaUNPETmplClassifStatus_Type(Integer32):
    """Custom type alaDaUNPETmplClassifStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPETmplClassifStatus_Type.__name__ = "Integer32"
_AlaDaUNPETmplClassifStatus_Object = MibTableColumn
alaDaUNPETmplClassifStatus = _AlaDaUNPETmplClassifStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 12),
    _AlaDaUNPETmplClassifStatus_Type()
)
alaDaUNPETmplClassifStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplClassifStatus.setStatus("deprecated")


class _AlaDaUNPETmplDefEProf_Type(SnmpAdminString):
    """Custom type alaDaUNPETmplDefEProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPETmplDefEProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPETmplDefEProf_Object = MibTableColumn
alaDaUNPETmplDefEProf = _AlaDaUNPETmplDefEProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 13),
    _AlaDaUNPETmplDefEProf_Type()
)
alaDaUNPETmplDefEProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplDefEProf.setStatus("deprecated")


class _AlaDaUNPETmplGroupId_Type(Integer32):
    """Custom type alaDaUNPETmplGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDaUNPETmplGroupId_Type.__name__ = "Integer32"
_AlaDaUNPETmplGroupId_Object = MibTableColumn
alaDaUNPETmplGroupId = _AlaDaUNPETmplGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 14),
    _AlaDaUNPETmplGroupId_Type()
)
alaDaUNPETmplGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplGroupId.setStatus("deprecated")


class _AlaDaUNPETmplAaaProf_Type(SnmpAdminString):
    """Custom type alaDaUNPETmplAaaProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPETmplAaaProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPETmplAaaProf_Object = MibTableColumn
alaDaUNPETmplAaaProf = _AlaDaUNPETmplAaaProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 15),
    _AlaDaUNPETmplAaaProf_Type()
)
alaDaUNPETmplAaaProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplAaaProf.setStatus("deprecated")
_AlaDaUNPETmplRowStatus_Type = RowStatus
_AlaDaUNPETmplRowStatus_Object = MibTableColumn
alaDaUNPETmplRowStatus = _AlaDaUNPETmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 16),
    _AlaDaUNPETmplRowStatus_Type()
)
alaDaUNPETmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplRowStatus.setStatus("deprecated")


class _AlaDaUNPETmplRedirectPortBounce_Type(Integer32):
    """Custom type alaDaUNPETmplRedirectPortBounce based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPETmplRedirectPortBounce_Type.__name__ = "Integer32"
_AlaDaUNPETmplRedirectPortBounce_Object = MibTableColumn
alaDaUNPETmplRedirectPortBounce = _AlaDaUNPETmplRedirectPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 17),
    _AlaDaUNPETmplRedirectPortBounce_Type()
)
alaDaUNPETmplRedirectPortBounce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplRedirectPortBounce.setStatus("deprecated")


class _AlaDaUNPETmplFailurePolicy_Type(Integer32):
    """Custom type alaDaUNPETmplFailurePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("macAuth", 2))
    )


_AlaDaUNPETmplFailurePolicy_Type.__name__ = "Integer32"
_AlaDaUNPETmplFailurePolicy_Object = MibTableColumn
alaDaUNPETmplFailurePolicy = _AlaDaUNPETmplFailurePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 18),
    _AlaDaUNPETmplFailurePolicy_Type()
)
alaDaUNPETmplFailurePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplFailurePolicy.setStatus("deprecated")


class _AlaDaUNPETmplBypassStatus_Type(Integer32):
    """Custom type alaDaUNPETmplBypassStatus based on Integer32"""
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


_AlaDaUNPETmplBypassStatus_Type.__name__ = "Integer32"
_AlaDaUNPETmplBypassStatus_Object = MibTableColumn
alaDaUNPETmplBypassStatus = _AlaDaUNPETmplBypassStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 19),
    _AlaDaUNPETmplBypassStatus_Type()
)
alaDaUNPETmplBypassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplBypassStatus.setStatus("deprecated")


class _AlaDaUNPETmplMacAllowEap_Type(Integer32):
    """Custom type alaDaUNPETmplMacAllowEap based on Integer32"""
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
        *(("pass", 1),
          ("fail", 2),
          ("noauth", 3),
          ("none", 4))
    )


_AlaDaUNPETmplMacAllowEap_Type.__name__ = "Integer32"
_AlaDaUNPETmplMacAllowEap_Object = MibTableColumn
alaDaUNPETmplMacAllowEap = _AlaDaUNPETmplMacAllowEap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 20),
    _AlaDaUNPETmplMacAllowEap_Type()
)
alaDaUNPETmplMacAllowEap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplMacAllowEap.setStatus("deprecated")


class _AlaDaUNPETmplAdminControlledDirections_Type(Integer32):
    """Custom type alaDaUNPETmplAdminControlledDirections based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("in", 2),
          ("noVal", 3))
    )


_AlaDaUNPETmplAdminControlledDirections_Type.__name__ = "Integer32"
_AlaDaUNPETmplAdminControlledDirections_Object = MibTableColumn
alaDaUNPETmplAdminControlledDirections = _AlaDaUNPETmplAdminControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 21),
    _AlaDaUNPETmplAdminControlledDirections_Type()
)
alaDaUNPETmplAdminControlledDirections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplAdminControlledDirections.setStatus("deprecated")


class _AlaDaUNPETmplTrustTagStatus_Type(Integer32):
    """Custom type alaDaUNPETmplTrustTagStatus based on Integer32"""
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


_AlaDaUNPETmplTrustTagStatus_Type.__name__ = "Integer32"
_AlaDaUNPETmplTrustTagStatus_Object = MibTableColumn
alaDaUNPETmplTrustTagStatus = _AlaDaUNPETmplTrustTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 22),
    _AlaDaUNPETmplTrustTagStatus_Type()
)
alaDaUNPETmplTrustTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplTrustTagStatus.setStatus("deprecated")


class _AlaDaUNPETmplForceL3Learning_Type(Integer32):
    """Custom type alaDaUNPETmplForceL3Learning based on Integer32"""
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


_AlaDaUNPETmplForceL3Learning_Type.__name__ = "Integer32"
_AlaDaUNPETmplForceL3Learning_Object = MibTableColumn
alaDaUNPETmplForceL3Learning = _AlaDaUNPETmplForceL3Learning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 23),
    _AlaDaUNPETmplForceL3Learning_Type()
)
alaDaUNPETmplForceL3Learning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplForceL3Learning.setStatus("deprecated")


class _AlaDaUNPETmplForceL3LearningPortBounce_Type(Integer32):
    """Custom type alaDaUNPETmplForceL3LearningPortBounce based on Integer32"""
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


_AlaDaUNPETmplForceL3LearningPortBounce_Type.__name__ = "Integer32"
_AlaDaUNPETmplForceL3LearningPortBounce_Object = MibTableColumn
alaDaUNPETmplForceL3LearningPortBounce = _AlaDaUNPETmplForceL3LearningPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 21, 1, 24),
    _AlaDaUNPETmplForceL3LearningPortBounce_Type()
)
alaDaUNPETmplForceL3LearningPortBounce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplForceL3LearningPortBounce.setStatus("deprecated")
_AlaDaUNPEdgeProfTable_Object = MibTable
alaDaUNPEdgeProfTable = _AlaDaUNPEdgeProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22)
)
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfTable.setStatus("deprecated")
_AlaDaUNPEdgeProfEntry_Object = MibTableRow
alaDaUNPEdgeProfEntry = _AlaDaUNPEdgeProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1)
)
alaDaUNPEdgeProfEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfName"),
)
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfEntry.setStatus("deprecated")


class _AlaDaUNPEdgeProfName_Type(SnmpAdminString):
    """Custom type alaDaUNPEdgeProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPEdgeProfName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEdgeProfName_Object = MibTableColumn
alaDaUNPEdgeProfName = _AlaDaUNPEdgeProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 1),
    _AlaDaUNPEdgeProfName_Type()
)
alaDaUNPEdgeProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfName.setStatus("deprecated")


class _AlaDaUNPEdgeProfQosPolicyList_Type(SnmpAdminString):
    """Custom type alaDaUNPEdgeProfQosPolicyList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPEdgeProfQosPolicyList_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEdgeProfQosPolicyList_Object = MibTableColumn
alaDaUNPEdgeProfQosPolicyList = _AlaDaUNPEdgeProfQosPolicyList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 2),
    _AlaDaUNPEdgeProfQosPolicyList_Type()
)
alaDaUNPEdgeProfQosPolicyList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfQosPolicyList.setStatus("deprecated")


class _AlaDaUNPEdgeProfLocationPolicy_Type(SnmpAdminString):
    """Custom type alaDaUNPEdgeProfLocationPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPEdgeProfLocationPolicy_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEdgeProfLocationPolicy_Object = MibTableColumn
alaDaUNPEdgeProfLocationPolicy = _AlaDaUNPEdgeProfLocationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 3),
    _AlaDaUNPEdgeProfLocationPolicy_Type()
)
alaDaUNPEdgeProfLocationPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfLocationPolicy.setStatus("deprecated")


class _AlaDaUNPEdgeProfPeriodPolicy_Type(SnmpAdminString):
    """Custom type alaDaUNPEdgeProfPeriodPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPEdgeProfPeriodPolicy_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEdgeProfPeriodPolicy_Object = MibTableColumn
alaDaUNPEdgeProfPeriodPolicy = _AlaDaUNPEdgeProfPeriodPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 4),
    _AlaDaUNPEdgeProfPeriodPolicy_Type()
)
alaDaUNPEdgeProfPeriodPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfPeriodPolicy.setStatus("deprecated")


class _AlaDaUNPEdgeProfHICStatus_Type(Integer32):
    """Custom type alaDaUNPEdgeProfHICStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPEdgeProfHICStatus_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfHICStatus_Object = MibTableColumn
alaDaUNPEdgeProfHICStatus = _AlaDaUNPEdgeProfHICStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 5),
    _AlaDaUNPEdgeProfHICStatus_Type()
)
alaDaUNPEdgeProfHICStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfHICStatus.setStatus("deprecated")


class _AlaDaUNPEdgeProfCPortalAuth_Type(Integer32):
    """Custom type alaDaUNPEdgeProfCPortalAuth based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPEdgeProfCPortalAuth_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfCPortalAuth_Object = MibTableColumn
alaDaUNPEdgeProfCPortalAuth = _AlaDaUNPEdgeProfCPortalAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 6),
    _AlaDaUNPEdgeProfCPortalAuth_Type()
)
alaDaUNPEdgeProfCPortalAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfCPortalAuth.setStatus("deprecated")


class _AlaDaUNPEdgeProfAuthStatus_Type(Integer32):
    """Custom type alaDaUNPEdgeProfAuthStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPEdgeProfAuthStatus_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfAuthStatus_Object = MibTableColumn
alaDaUNPEdgeProfAuthStatus = _AlaDaUNPEdgeProfAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 7),
    _AlaDaUNPEdgeProfAuthStatus_Type()
)
alaDaUNPEdgeProfAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfAuthStatus.setStatus("deprecated")


class _AlaDaUNPEdgeProfMobileTag_Type(Integer32):
    """Custom type alaDaUNPEdgeProfMobileTag based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPEdgeProfMobileTag_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfMobileTag_Object = MibTableColumn
alaDaUNPEdgeProfMobileTag = _AlaDaUNPEdgeProfMobileTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 8),
    _AlaDaUNPEdgeProfMobileTag_Type()
)
alaDaUNPEdgeProfMobileTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfMobileTag.setStatus("deprecated")


class _AlaDaUNPEdgeProfDHCPEnforcment_Type(Integer32):
    """Custom type alaDaUNPEdgeProfDHCPEnforcment based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPEdgeProfDHCPEnforcment_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfDHCPEnforcment_Object = MibTableColumn
alaDaUNPEdgeProfDHCPEnforcment = _AlaDaUNPEdgeProfDHCPEnforcment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 9),
    _AlaDaUNPEdgeProfDHCPEnforcment_Type()
)
alaDaUNPEdgeProfDHCPEnforcment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfDHCPEnforcment.setStatus("deprecated")


class _AlaDaUNPEdgeProfCPortalProf_Type(SnmpAdminString):
    """Custom type alaDaUNPEdgeProfCPortalProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPEdgeProfCPortalProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEdgeProfCPortalProf_Object = MibTableColumn
alaDaUNPEdgeProfCPortalProf = _AlaDaUNPEdgeProfCPortalProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 10),
    _AlaDaUNPEdgeProfCPortalProf_Type()
)
alaDaUNPEdgeProfCPortalProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfCPortalProf.setStatus("deprecated")
_AlaDaUNPEdgeProfRowStatus_Type = RowStatus
_AlaDaUNPEdgeProfRowStatus_Object = MibTableColumn
alaDaUNPEdgeProfRowStatus = _AlaDaUNPEdgeProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 11),
    _AlaDaUNPEdgeProfRowStatus_Type()
)
alaDaUNPEdgeProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfRowStatus.setStatus("deprecated")


class _AlaDaUNPEdgeProfRedirectStatus_Type(Integer32):
    """Custom type alaDaUNPEdgeProfRedirectStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPEdgeProfRedirectStatus_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfRedirectStatus_Object = MibTableColumn
alaDaUNPEdgeProfRedirectStatus = _AlaDaUNPEdgeProfRedirectStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 12),
    _AlaDaUNPEdgeProfRedirectStatus_Type()
)
alaDaUNPEdgeProfRedirectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfRedirectStatus.setStatus("deprecated")


class _AlaDaUNPEdgeProfKerberosStatus_Type(Integer32):
    """Custom type alaDaUNPEdgeProfKerberosStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPEdgeProfKerberosStatus_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfKerberosStatus_Object = MibTableColumn
alaDaUNPEdgeProfKerberosStatus = _AlaDaUNPEdgeProfKerberosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 13),
    _AlaDaUNPEdgeProfKerberosStatus_Type()
)
alaDaUNPEdgeProfKerberosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfKerberosStatus.setStatus("deprecated")


class _AlaDaUNPEdgeProfMaxIngressBw_Type(Integer32):
    """Custom type alaDaUNPEdgeProfMaxIngressBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUNPEdgeProfMaxIngressBw_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfMaxIngressBw_Object = MibTableColumn
alaDaUNPEdgeProfMaxIngressBw = _AlaDaUNPEdgeProfMaxIngressBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 14),
    _AlaDaUNPEdgeProfMaxIngressBw_Type()
)
alaDaUNPEdgeProfMaxIngressBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfMaxIngressBw.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfMaxIngressBw.setUnits("kilobits per second")


class _AlaDaUNPEdgeProfMaxEgressBw_Type(Integer32):
    """Custom type alaDaUNPEdgeProfMaxEgressBw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUNPEdgeProfMaxEgressBw_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfMaxEgressBw_Object = MibTableColumn
alaDaUNPEdgeProfMaxEgressBw = _AlaDaUNPEdgeProfMaxEgressBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 15),
    _AlaDaUNPEdgeProfMaxEgressBw_Type()
)
alaDaUNPEdgeProfMaxEgressBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfMaxEgressBw.setStatus("deprecated")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfMaxEgressBw.setUnits("kilobits per second")


class _AlaDaUNPEdgeProfMaxIngressDepth_Type(Integer32):
    """Custom type alaDaUNPEdgeProfMaxIngressDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16384),
    )


_AlaDaUNPEdgeProfMaxIngressDepth_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfMaxIngressDepth_Object = MibTableColumn
alaDaUNPEdgeProfMaxIngressDepth = _AlaDaUNPEdgeProfMaxIngressDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 16),
    _AlaDaUNPEdgeProfMaxIngressDepth_Type()
)
alaDaUNPEdgeProfMaxIngressDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfMaxIngressDepth.setStatus("deprecated")


class _AlaDaUNPEdgeProfMaxEgressDepth_Type(Integer32):
    """Custom type alaDaUNPEdgeProfMaxEgressDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16384),
    )


_AlaDaUNPEdgeProfMaxEgressDepth_Type.__name__ = "Integer32"
_AlaDaUNPEdgeProfMaxEgressDepth_Object = MibTableColumn
alaDaUNPEdgeProfMaxEgressDepth = _AlaDaUNPEdgeProfMaxEgressDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 22, 1, 17),
    _AlaDaUNPEdgeProfMaxEgressDepth_Type()
)
alaDaUNPEdgeProfMaxEgressDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfMaxEgressDepth.setStatus("deprecated")
_AlaDaUNPPortRuleTable_Object = MibTable
alaDaUNPPortRuleTable = _AlaDaUNPPortRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 23)
)
if mibBuilder.loadTexts:
    alaDaUNPPortRuleTable.setStatus("current")
_AlaDaUNPPortRuleEntry_Object = MibTableRow
alaDaUNPPortRuleEntry = _AlaDaUNPPortRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 23, 1)
)
alaDaUNPPortRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortRuleNum"),
)
if mibBuilder.loadTexts:
    alaDaUNPPortRuleEntry.setStatus("current")
_AlaDaUNPPortRuleNum_Type = InterfaceIndex
_AlaDaUNPPortRuleNum_Object = MibTableColumn
alaDaUNPPortRuleNum = _AlaDaUNPPortRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 23, 1, 1),
    _AlaDaUNPPortRuleNum_Type()
)
alaDaUNPPortRuleNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPPortRuleNum.setStatus("current")


class _AlaDaUNPPortRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPPortRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortRuleEdgeProf_Object = MibTableColumn
alaDaUNPPortRuleEdgeProf = _AlaDaUNPPortRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 23, 1, 2),
    _AlaDaUNPPortRuleEdgeProf_Type()
)
alaDaUNPPortRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortRuleEdgeProf.setStatus("deprecated")
_AlaDaUNPPortRuleRowStatus_Type = RowStatus
_AlaDaUNPPortRuleRowStatus_Object = MibTableColumn
alaDaUNPPortRuleRowStatus = _AlaDaUNPPortRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 23, 1, 3),
    _AlaDaUNPPortRuleRowStatus_Type()
)
alaDaUNPPortRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortRuleRowStatus.setStatus("current")


class _AlaDaUNPPortRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPPortRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPPortRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPPortRuleVlanTag_Object = MibTableColumn
alaDaUNPPortRuleVlanTag = _AlaDaUNPPortRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 23, 1, 4),
    _AlaDaUNPPortRuleVlanTag_Type()
)
alaDaUNPPortRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortRuleVlanTag.setStatus("current")


class _AlaDaUNPPortRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPPortRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortRuleProfile1_Object = MibTableColumn
alaDaUNPPortRuleProfile1 = _AlaDaUNPPortRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 23, 1, 5),
    _AlaDaUNPPortRuleProfile1_Type()
)
alaDaUNPPortRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortRuleProfile1.setStatus("current")


class _AlaDaUNPPortRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPPortRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortRuleProfile2_Object = MibTableColumn
alaDaUNPPortRuleProfile2 = _AlaDaUNPPortRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 23, 1, 6),
    _AlaDaUNPPortRuleProfile2_Type()
)
alaDaUNPPortRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortRuleProfile2.setStatus("current")


class _AlaDaUNPPortRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPPortRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortRuleProfile3_Object = MibTableColumn
alaDaUNPPortRuleProfile3 = _AlaDaUNPPortRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 23, 1, 7),
    _AlaDaUNPPortRuleProfile3_Type()
)
alaDaUNPPortRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortRuleProfile3.setStatus("current")
_AlaDaUNPGroupRuleTable_Object = MibTable
alaDaUNPGroupRuleTable = _AlaDaUNPGroupRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 24)
)
if mibBuilder.loadTexts:
    alaDaUNPGroupRuleTable.setStatus("deprecated")
_AlaDaUNPGroupRuleEntry_Object = MibTableRow
alaDaUNPGroupRuleEntry = _AlaDaUNPGroupRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 24, 1)
)
alaDaUNPGroupRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPGroupRuleId"),
)
if mibBuilder.loadTexts:
    alaDaUNPGroupRuleEntry.setStatus("deprecated")


class _AlaDaUNPGroupRuleId_Type(Integer32):
    """Custom type alaDaUNPGroupRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaDaUNPGroupRuleId_Type.__name__ = "Integer32"
_AlaDaUNPGroupRuleId_Object = MibTableColumn
alaDaUNPGroupRuleId = _AlaDaUNPGroupRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 24, 1, 1),
    _AlaDaUNPGroupRuleId_Type()
)
alaDaUNPGroupRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPGroupRuleId.setStatus("deprecated")


class _AlaDaUNPGroupRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPGroupRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPGroupRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPGroupRuleEdgeProf_Object = MibTableColumn
alaDaUNPGroupRuleEdgeProf = _AlaDaUNPGroupRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 24, 1, 2),
    _AlaDaUNPGroupRuleEdgeProf_Type()
)
alaDaUNPGroupRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPGroupRuleEdgeProf.setStatus("deprecated")
_AlaDaUNPGroupRuleRowStatus_Type = RowStatus
_AlaDaUNPGroupRuleRowStatus_Object = MibTableColumn
alaDaUNPGroupRuleRowStatus = _AlaDaUNPGroupRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 24, 1, 3),
    _AlaDaUNPGroupRuleRowStatus_Type()
)
alaDaUNPGroupRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPGroupRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPGroupRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPGroupRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPGroupRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPGroupRuleVlanTag_Object = MibTableColumn
alaDaUNPGroupRuleVlanTag = _AlaDaUNPGroupRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 24, 1, 4),
    _AlaDaUNPGroupRuleVlanTag_Type()
)
alaDaUNPGroupRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPGroupRuleVlanTag.setStatus("deprecated")
_AlaDaUNPMacOuiRuleTable_Object = MibTable
alaDaUNPMacOuiRuleTable = _AlaDaUNPMacOuiRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 25)
)
if mibBuilder.loadTexts:
    alaDaUNPMacOuiRuleTable.setStatus("current")
_AlaDaUNPMacOuiRuleEntry_Object = MibTableRow
alaDaUNPMacOuiRuleEntry = _AlaDaUNPMacOuiRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 25, 1)
)
alaDaUNPMacOuiRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacOuiRuleAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacOuiRuleEntry.setStatus("current")
_AlaDaUNPMacOuiRuleAddr_Type = MacOui
_AlaDaUNPMacOuiRuleAddr_Object = MibTableColumn
alaDaUNPMacOuiRuleAddr = _AlaDaUNPMacOuiRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 25, 1, 1),
    _AlaDaUNPMacOuiRuleAddr_Type()
)
alaDaUNPMacOuiRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacOuiRuleAddr.setStatus("current")


class _AlaDaUNPMacOuiRuleEdgeProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPMacOuiRuleEdgeProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacOuiRuleEdgeProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacOuiRuleEdgeProfile_Object = MibTableColumn
alaDaUNPMacOuiRuleEdgeProfile = _AlaDaUNPMacOuiRuleEdgeProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 25, 1, 2),
    _AlaDaUNPMacOuiRuleEdgeProfile_Type()
)
alaDaUNPMacOuiRuleEdgeProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacOuiRuleEdgeProfile.setStatus("deprecated")
_AlaDaUNPMacOuiRuleRowStatus_Type = RowStatus
_AlaDaUNPMacOuiRuleRowStatus_Object = MibTableColumn
alaDaUNPMacOuiRuleRowStatus = _AlaDaUNPMacOuiRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 25, 1, 3),
    _AlaDaUNPMacOuiRuleRowStatus_Type()
)
alaDaUNPMacOuiRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacOuiRuleRowStatus.setStatus("current")


class _AlaDaUNPMacOuiRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacOuiRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacOuiRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacOuiRuleVlanTag_Object = MibTableColumn
alaDaUNPMacOuiRuleVlanTag = _AlaDaUNPMacOuiRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 25, 1, 4),
    _AlaDaUNPMacOuiRuleVlanTag_Type()
)
alaDaUNPMacOuiRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacOuiRuleVlanTag.setStatus("current")


class _AlaDaUNPMacOuiRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPMacOuiRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPMacOuiRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacOuiRuleProfile1_Object = MibTableColumn
alaDaUNPMacOuiRuleProfile1 = _AlaDaUNPMacOuiRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 25, 1, 5),
    _AlaDaUNPMacOuiRuleProfile1_Type()
)
alaDaUNPMacOuiRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacOuiRuleProfile1.setStatus("current")


class _AlaDaUNPMacOuiRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPMacOuiRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPMacOuiRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacOuiRuleProfile2_Object = MibTableColumn
alaDaUNPMacOuiRuleProfile2 = _AlaDaUNPMacOuiRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 25, 1, 6),
    _AlaDaUNPMacOuiRuleProfile2_Type()
)
alaDaUNPMacOuiRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacOuiRuleProfile2.setStatus("current")


class _AlaDaUNPMacOuiRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPMacOuiRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPMacOuiRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacOuiRuleProfile3_Object = MibTableColumn
alaDaUNPMacOuiRuleProfile3 = _AlaDaUNPMacOuiRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 25, 1, 7),
    _AlaDaUNPMacOuiRuleProfile3_Type()
)
alaDaUNPMacOuiRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacOuiRuleProfile3.setStatus("current")
_AlaDaUNPEndPoinRuleTable_Object = MibTable
alaDaUNPEndPoinRuleTable = _AlaDaUNPEndPoinRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 26)
)
if mibBuilder.loadTexts:
    alaDaUNPEndPoinRuleTable.setStatus("current")
_AlaDaUNPEndPoinRuleEntry_Object = MibTableRow
alaDaUNPEndPoinRuleEntry = _AlaDaUNPEndPoinRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 26, 1)
)
alaDaUNPEndPoinRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPEndPoinRuleId"),
)
if mibBuilder.loadTexts:
    alaDaUNPEndPoinRuleEntry.setStatus("current")


class _AlaDaUNPEndPoinRuleId_Type(Integer32):
    """Custom type alaDaUNPEndPoinRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipPhone", 1),
          ("accessPoint", 2))
    )


_AlaDaUNPEndPoinRuleId_Type.__name__ = "Integer32"
_AlaDaUNPEndPoinRuleId_Object = MibTableColumn
alaDaUNPEndPoinRuleId = _AlaDaUNPEndPoinRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 26, 1, 1),
    _AlaDaUNPEndPoinRuleId_Type()
)
alaDaUNPEndPoinRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPEndPoinRuleId.setStatus("current")


class _AlaDaUNPEndPoinEdgeProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPEndPoinEdgeProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPEndPoinEdgeProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEndPoinEdgeProfile_Object = MibTableColumn
alaDaUNPEndPoinEdgeProfile = _AlaDaUNPEndPoinEdgeProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 26, 1, 2),
    _AlaDaUNPEndPoinEdgeProfile_Type()
)
alaDaUNPEndPoinEdgeProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEndPoinEdgeProfile.setStatus("deprecated")
_AlaDaUNPEndPoinRuleRowStatus_Type = RowStatus
_AlaDaUNPEndPoinRuleRowStatus_Object = MibTableColumn
alaDaUNPEndPoinRuleRowStatus = _AlaDaUNPEndPoinRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 26, 1, 3),
    _AlaDaUNPEndPoinRuleRowStatus_Type()
)
alaDaUNPEndPoinRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEndPoinRuleRowStatus.setStatus("current")


class _AlaDaUNPEndPoinProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPEndPoinProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPEndPoinProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEndPoinProfile1_Object = MibTableColumn
alaDaUNPEndPoinProfile1 = _AlaDaUNPEndPoinProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 26, 1, 4),
    _AlaDaUNPEndPoinProfile1_Type()
)
alaDaUNPEndPoinProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEndPoinProfile1.setStatus("current")


class _AlaDaUNPEndPoinProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPEndPoinProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPEndPoinProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEndPoinProfile2_Object = MibTableColumn
alaDaUNPEndPoinProfile2 = _AlaDaUNPEndPoinProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 26, 1, 5),
    _AlaDaUNPEndPoinProfile2_Type()
)
alaDaUNPEndPoinProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEndPoinProfile2.setStatus("current")


class _AlaDaUNPEndPoinProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPEndPoinProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPEndPoinProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEndPoinProfile3_Object = MibTableColumn
alaDaUNPEndPoinProfile3 = _AlaDaUNPEndPoinProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 26, 1, 6),
    _AlaDaUNPEndPoinProfile3_Type()
)
alaDaUNPEndPoinProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEndPoinProfile3.setStatus("current")


class _AlaDaUNPEndPoinVlanTag_Type(Integer32):
    """Custom type alaDaUNPEndPoinVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPEndPoinVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPEndPoinVlanTag_Object = MibTableColumn
alaDaUNPEndPoinVlanTag = _AlaDaUNPEndPoinVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 26, 1, 7),
    _AlaDaUNPEndPoinVlanTag_Type()
)
alaDaUNPEndPoinVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPEndPoinVlanTag.setStatus("current")
_AlaDaUNPAuthRuleTable_Object = MibTable
alaDaUNPAuthRuleTable = _AlaDaUNPAuthRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 27)
)
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleTable.setStatus("current")
_AlaDaUNPAuthRuleEntry_Object = MibTableRow
alaDaUNPAuthRuleEntry = _AlaDaUNPAuthRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 27, 1)
)
alaDaUNPAuthRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPAuthRuleType"),
)
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleEntry.setStatus("current")


class _AlaDaUNPAuthRuleType_Type(Integer32):
    """Custom type alaDaUNPAuthRuleType based on Integer32"""
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
        *(("none", 1),
          ("dot1x", 2),
          ("mac", 3),
          ("dot1xFail", 4),
          ("macFail", 5),
          ("noAuth", 6))
    )


_AlaDaUNPAuthRuleType_Type.__name__ = "Integer32"
_AlaDaUNPAuthRuleType_Object = MibTableColumn
alaDaUNPAuthRuleType = _AlaDaUNPAuthRuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 27, 1, 1),
    _AlaDaUNPAuthRuleType_Type()
)
alaDaUNPAuthRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleType.setStatus("current")


class _AlaDaUNPAuthRuleEdgeProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthRuleEdgeProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPAuthRuleEdgeProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthRuleEdgeProfile_Object = MibTableColumn
alaDaUNPAuthRuleEdgeProfile = _AlaDaUNPAuthRuleEdgeProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 27, 1, 2),
    _AlaDaUNPAuthRuleEdgeProfile_Type()
)
alaDaUNPAuthRuleEdgeProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleEdgeProfile.setStatus("deprecated")
_AlaDaUNPAuthRuleRowStatus_Type = RowStatus
_AlaDaUNPAuthRuleRowStatus_Object = MibTableColumn
alaDaUNPAuthRuleRowStatus = _AlaDaUNPAuthRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 27, 1, 3),
    _AlaDaUNPAuthRuleRowStatus_Type()
)
alaDaUNPAuthRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleRowStatus.setStatus("current")


class _AlaDaUNPAuthRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPAuthRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPAuthRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPAuthRuleVlanTag_Object = MibTableColumn
alaDaUNPAuthRuleVlanTag = _AlaDaUNPAuthRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 27, 1, 4),
    _AlaDaUNPAuthRuleVlanTag_Type()
)
alaDaUNPAuthRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleVlanTag.setStatus("current")


class _AlaDaUNPAuthRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPAuthRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthRuleProfile1_Object = MibTableColumn
alaDaUNPAuthRuleProfile1 = _AlaDaUNPAuthRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 27, 1, 5),
    _AlaDaUNPAuthRuleProfile1_Type()
)
alaDaUNPAuthRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleProfile1.setStatus("current")


class _AlaDaUNPAuthRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPAuthRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthRuleProfile2_Object = MibTableColumn
alaDaUNPAuthRuleProfile2 = _AlaDaUNPAuthRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 27, 1, 6),
    _AlaDaUNPAuthRuleProfile2_Type()
)
alaDaUNPAuthRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleProfile2.setStatus("current")


class _AlaDaUNPAuthRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPAuthRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthRuleProfile3_Object = MibTableColumn
alaDaUNPAuthRuleProfile3 = _AlaDaUNPAuthRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 27, 1, 7),
    _AlaDaUNPAuthRuleProfile3_Type()
)
alaDaUNPAuthRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleProfile3.setStatus("current")
_AlaDaUNPClassifRuleTable_Object = MibTable
alaDaUNPClassifRuleTable = _AlaDaUNPClassifRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28)
)
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleTable.setStatus("current")
_AlaDaUNPClassifRuleEntry_Object = MibTableRow
alaDaUNPClassifRuleEntry = _AlaDaUNPClassifRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1)
)
alaDaUNPClassifRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleName"),
)
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleEntry.setStatus("current")


class _AlaDaUNPClassifRuleName_Type(SnmpAdminString):
    """Custom type alaDaUNPClassifRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPClassifRuleName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPClassifRuleName_Object = MibTableColumn
alaDaUNPClassifRuleName = _AlaDaUNPClassifRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 1),
    _AlaDaUNPClassifRuleName_Type()
)
alaDaUNPClassifRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleName.setStatus("current")


class _AlaDaUNPClassifRulePrecedenceNum_Type(Integer32):
    """Custom type alaDaUNPClassifRulePrecedenceNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaDaUNPClassifRulePrecedenceNum_Type.__name__ = "Integer32"
_AlaDaUNPClassifRulePrecedenceNum_Object = MibTableColumn
alaDaUNPClassifRulePrecedenceNum = _AlaDaUNPClassifRulePrecedenceNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 2),
    _AlaDaUNPClassifRulePrecedenceNum_Type()
)
alaDaUNPClassifRulePrecedenceNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRulePrecedenceNum.setStatus("current")


class _AlaDaUNPClassifRuleEdgeProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPClassifRuleEdgeProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPClassifRuleEdgeProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPClassifRuleEdgeProfile_Object = MibTableColumn
alaDaUNPClassifRuleEdgeProfile = _AlaDaUNPClassifRuleEdgeProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 3),
    _AlaDaUNPClassifRuleEdgeProfile_Type()
)
alaDaUNPClassifRuleEdgeProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleEdgeProfile.setStatus("deprecated")
_AlaDaUNPClassifRulePort_Type = InterfaceIndexOrZero
_AlaDaUNPClassifRulePort_Object = MibTableColumn
alaDaUNPClassifRulePort = _AlaDaUNPClassifRulePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 4),
    _AlaDaUNPClassifRulePort_Type()
)
alaDaUNPClassifRulePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRulePort.setStatus("current")
_AlaDaUNPClassifRulePortHigh_Type = InterfaceIndexOrZero
_AlaDaUNPClassifRulePortHigh_Object = MibTableColumn
alaDaUNPClassifRulePortHigh = _AlaDaUNPClassifRulePortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 5),
    _AlaDaUNPClassifRulePortHigh_Type()
)
alaDaUNPClassifRulePortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRulePortHigh.setStatus("current")


class _AlaDaUNPClassifRuleGroupId_Type(Integer32):
    """Custom type alaDaUNPClassifRuleGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AlaDaUNPClassifRuleGroupId_Type.__name__ = "Integer32"
_AlaDaUNPClassifRuleGroupId_Object = MibTableColumn
alaDaUNPClassifRuleGroupId = _AlaDaUNPClassifRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 6),
    _AlaDaUNPClassifRuleGroupId_Type()
)
alaDaUNPClassifRuleGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleGroupId.setStatus("deprecated")
_AlaDaUNPClassifRuleMacAddr_Type = MacAddress
_AlaDaUNPClassifRuleMacAddr_Object = MibTableColumn
alaDaUNPClassifRuleMacAddr = _AlaDaUNPClassifRuleMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 7),
    _AlaDaUNPClassifRuleMacAddr_Type()
)
alaDaUNPClassifRuleMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleMacAddr.setStatus("current")
_AlaDaUNPClassifRuleMacRngLoaddr_Type = MacAddress
_AlaDaUNPClassifRuleMacRngLoaddr_Object = MibTableColumn
alaDaUNPClassifRuleMacRngLoaddr = _AlaDaUNPClassifRuleMacRngLoaddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 8),
    _AlaDaUNPClassifRuleMacRngLoaddr_Type()
)
alaDaUNPClassifRuleMacRngLoaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleMacRngLoaddr.setStatus("current")
_AlaDaUNPClassifRuleMacRngHiaddr_Type = MacAddress
_AlaDaUNPClassifRuleMacRngHiaddr_Object = MibTableColumn
alaDaUNPClassifRuleMacRngHiaddr = _AlaDaUNPClassifRuleMacRngHiaddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 9),
    _AlaDaUNPClassifRuleMacRngHiaddr_Type()
)
alaDaUNPClassifRuleMacRngHiaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleMacRngHiaddr.setStatus("current")


class _AlaDaUNPClassifRuleMacOuiAddr_Type(OctetString):
    """Custom type alaDaUNPClassifRuleMacOuiAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
    )


_AlaDaUNPClassifRuleMacOuiAddr_Type.__name__ = "OctetString"
_AlaDaUNPClassifRuleMacOuiAddr_Object = MibTableColumn
alaDaUNPClassifRuleMacOuiAddr = _AlaDaUNPClassifRuleMacOuiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 10),
    _AlaDaUNPClassifRuleMacOuiAddr_Type()
)
alaDaUNPClassifRuleMacOuiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleMacOuiAddr.setStatus("current")


class _AlaDaUNPClassifRuleEndPoin_Type(Integer32):
    """Custom type alaDaUNPClassifRuleEndPoin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ipPhone", 1),
          ("accessPoint", 2))
    )


_AlaDaUNPClassifRuleEndPoin_Type.__name__ = "Integer32"
_AlaDaUNPClassifRuleEndPoin_Object = MibTableColumn
alaDaUNPClassifRuleEndPoin = _AlaDaUNPClassifRuleEndPoin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 11),
    _AlaDaUNPClassifRuleEndPoin_Type()
)
alaDaUNPClassifRuleEndPoin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleEndPoin.setStatus("current")


class _AlaDaUNPClassifRuleAuthType_Type(Integer32):
    """Custom type alaDaUNPClassifRuleAuthType based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("noAuth", 1),
          ("dot1x", 2),
          ("mac", 3),
          ("dot1xFail", 4),
          ("macFail", 5))
    )


_AlaDaUNPClassifRuleAuthType_Type.__name__ = "Integer32"
_AlaDaUNPClassifRuleAuthType_Object = MibTableColumn
alaDaUNPClassifRuleAuthType = _AlaDaUNPClassifRuleAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 12),
    _AlaDaUNPClassifRuleAuthType_Type()
)
alaDaUNPClassifRuleAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleAuthType.setStatus("current")
_AlaDaUNPClassifRuleIpAddressType_Type = InetAddressType
_AlaDaUNPClassifRuleIpAddressType_Object = MibTableColumn
alaDaUNPClassifRuleIpAddressType = _AlaDaUNPClassifRuleIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 13),
    _AlaDaUNPClassifRuleIpAddressType_Type()
)
alaDaUNPClassifRuleIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleIpAddressType.setStatus("current")
_AlaDaUNPClassifRuleIpAddress_Type = InetAddress
_AlaDaUNPClassifRuleIpAddress_Object = MibTableColumn
alaDaUNPClassifRuleIpAddress = _AlaDaUNPClassifRuleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 14),
    _AlaDaUNPClassifRuleIpAddress_Type()
)
alaDaUNPClassifRuleIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleIpAddress.setStatus("current")
_AlaDaUNPClassifRuleIpMaskType_Type = InetAddressType
_AlaDaUNPClassifRuleIpMaskType_Object = MibTableColumn
alaDaUNPClassifRuleIpMaskType = _AlaDaUNPClassifRuleIpMaskType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 15),
    _AlaDaUNPClassifRuleIpMaskType_Type()
)
alaDaUNPClassifRuleIpMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleIpMaskType.setStatus("current")
_AlaDaUNPClassifRuleIpMask_Type = InetAddress
_AlaDaUNPClassifRuleIpMask_Object = MibTableColumn
alaDaUNPClassifRuleIpMask = _AlaDaUNPClassifRuleIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 16),
    _AlaDaUNPClassifRuleIpMask_Type()
)
alaDaUNPClassifRuleIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleIpMask.setStatus("current")
_AlaDaUNPClassifRowStatus_Type = RowStatus
_AlaDaUNPClassifRowStatus_Object = MibTableColumn
alaDaUNPClassifRowStatus = _AlaDaUNPClassifRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 17),
    _AlaDaUNPClassifRowStatus_Type()
)
alaDaUNPClassifRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRowStatus.setStatus("current")


class _AlaDaUNPClassifRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPClassifRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPClassifRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPClassifRuleVlanTag_Object = MibTableColumn
alaDaUNPClassifRuleVlanTag = _AlaDaUNPClassifRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 18),
    _AlaDaUNPClassifRuleVlanTag_Type()
)
alaDaUNPClassifRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleVlanTag.setStatus("current")


class _AlaDaUNPClassifRuleCustomerDomain_Type(Integer32):
    """Custom type alaDaUNPClassifRuleCustomerDomain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUNPClassifRuleCustomerDomain_Type.__name__ = "Integer32"
_AlaDaUNPClassifRuleCustomerDomain_Object = MibTableColumn
alaDaUNPClassifRuleCustomerDomain = _AlaDaUNPClassifRuleCustomerDomain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 19),
    _AlaDaUNPClassifRuleCustomerDomain_Type()
)
alaDaUNPClassifRuleCustomerDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleCustomerDomain.setStatus("current")


class _AlaDaUNPClassifRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPClassifRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPClassifRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPClassifRuleProfile1_Object = MibTableColumn
alaDaUNPClassifRuleProfile1 = _AlaDaUNPClassifRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 20),
    _AlaDaUNPClassifRuleProfile1_Type()
)
alaDaUNPClassifRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleProfile1.setStatus("current")


class _AlaDaUNPClassifRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPClassifRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPClassifRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPClassifRuleProfile2_Object = MibTableColumn
alaDaUNPClassifRuleProfile2 = _AlaDaUNPClassifRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 21),
    _AlaDaUNPClassifRuleProfile2_Type()
)
alaDaUNPClassifRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleProfile2.setStatus("current")


class _AlaDaUNPClassifRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPClassifRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPClassifRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPClassifRuleProfile3_Object = MibTableColumn
alaDaUNPClassifRuleProfile3 = _AlaDaUNPClassifRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 22),
    _AlaDaUNPClassifRuleProfile3_Type()
)
alaDaUNPClassifRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleProfile3.setStatus("current")


class _AlaDaUNPClassifRuleDeviceType_Type(SnmpAdminString):
    """Custom type alaDaUNPClassifRuleDeviceType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPClassifRuleDeviceType_Type.__name__ = "SnmpAdminString"
_AlaDaUNPClassifRuleDeviceType_Object = MibTableColumn
alaDaUNPClassifRuleDeviceType = _AlaDaUNPClassifRuleDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 28, 1, 23),
    _AlaDaUNPClassifRuleDeviceType_Type()
)
alaDaUNPClassifRuleDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPClassifRuleDeviceType.setStatus("current")
_AlaDaUNPMacPortRuleTable_Object = MibTable
alaDaUNPMacPortRuleTable = _AlaDaUNPMacPortRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29)
)
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleTable.setStatus("current")
_AlaDaUNPMacPortRuleEntry_Object = MibTableRow
alaDaUNPMacPortRuleEntry = _AlaDaUNPMacPortRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29, 1)
)
alaDaUNPMacPortRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacPortRuleMacAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacPortRuleNum"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleEntry.setStatus("current")


class _AlaDaUNPMacPortRuleMacAddr_Type(MacAddress):
    """Custom type alaDaUNPMacPortRuleMacAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPMacPortRuleMacAddr_Type.__name__ = "MacAddress"
_AlaDaUNPMacPortRuleMacAddr_Object = MibTableColumn
alaDaUNPMacPortRuleMacAddr = _AlaDaUNPMacPortRuleMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29, 1, 1),
    _AlaDaUNPMacPortRuleMacAddr_Type()
)
alaDaUNPMacPortRuleMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleMacAddr.setStatus("current")


class _AlaDaUNPMacPortRuleNum_Type(InterfaceIndex):
    """Custom type alaDaUNPMacPortRuleNum based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaDaUNPMacPortRuleNum_Type.__name__ = "InterfaceIndex"
_AlaDaUNPMacPortRuleNum_Object = MibTableColumn
alaDaUNPMacPortRuleNum = _AlaDaUNPMacPortRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29, 1, 2),
    _AlaDaUNPMacPortRuleNum_Type()
)
alaDaUNPMacPortRuleNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleNum.setStatus("current")


class _AlaDaUNPMacPortRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPMacPortRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacPortRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacPortRuleEdgeProf_Object = MibTableColumn
alaDaUNPMacPortRuleEdgeProf = _AlaDaUNPMacPortRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29, 1, 3),
    _AlaDaUNPMacPortRuleEdgeProf_Type()
)
alaDaUNPMacPortRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleEdgeProf.setStatus("deprecated")
_AlaDaUNPMacPortRuleRowStatus_Type = RowStatus
_AlaDaUNPMacPortRuleRowStatus_Object = MibTableColumn
alaDaUNPMacPortRuleRowStatus = _AlaDaUNPMacPortRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29, 1, 4),
    _AlaDaUNPMacPortRuleRowStatus_Type()
)
alaDaUNPMacPortRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleRowStatus.setStatus("current")


class _AlaDaUNPMacPortRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacPortRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacPortRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacPortRuleVlanTag_Object = MibTableColumn
alaDaUNPMacPortRuleVlanTag = _AlaDaUNPMacPortRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29, 1, 5),
    _AlaDaUNPMacPortRuleVlanTag_Type()
)
alaDaUNPMacPortRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleVlanTag.setStatus("current")


class _AlaDaUNPMacPortRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPMacPortRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacPortRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacPortRuleProfile1_Object = MibTableColumn
alaDaUNPMacPortRuleProfile1 = _AlaDaUNPMacPortRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29, 1, 6),
    _AlaDaUNPMacPortRuleProfile1_Type()
)
alaDaUNPMacPortRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleProfile1.setStatus("current")


class _AlaDaUNPMacPortRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPMacPortRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacPortRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacPortRuleProfile2_Object = MibTableColumn
alaDaUNPMacPortRuleProfile2 = _AlaDaUNPMacPortRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29, 1, 7),
    _AlaDaUNPMacPortRuleProfile2_Type()
)
alaDaUNPMacPortRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleProfile2.setStatus("current")


class _AlaDaUNPMacPortRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPMacPortRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacPortRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacPortRuleProfile3_Object = MibTableColumn
alaDaUNPMacPortRuleProfile3 = _AlaDaUNPMacPortRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 29, 1, 8),
    _AlaDaUNPMacPortRuleProfile3_Type()
)
alaDaUNPMacPortRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacPortRuleProfile3.setStatus("current")
_AlaDaUNPIpPortRuleTable_Object = MibTable
alaDaUNPIpPortRuleTable = _AlaDaUNPIpPortRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30)
)
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleTable.setStatus("current")
_AlaDaUNPIpPortRuleEntry_Object = MibTableRow
alaDaUNPIpPortRuleEntry = _AlaDaUNPIpPortRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1)
)
alaDaUNPIpPortRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleNum"),
)
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleEntry.setStatus("current")
_AlaDaUNPIpPortRuleAddrType_Type = InetAddressType
_AlaDaUNPIpPortRuleAddrType_Object = MibTableColumn
alaDaUNPIpPortRuleAddrType = _AlaDaUNPIpPortRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 1),
    _AlaDaUNPIpPortRuleAddrType_Type()
)
alaDaUNPIpPortRuleAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleAddrType.setStatus("current")
_AlaDaUNPIpPortRuleAddr_Type = InetAddress
_AlaDaUNPIpPortRuleAddr_Object = MibTableColumn
alaDaUNPIpPortRuleAddr = _AlaDaUNPIpPortRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 2),
    _AlaDaUNPIpPortRuleAddr_Type()
)
alaDaUNPIpPortRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleAddr.setStatus("current")


class _AlaDaUNPIpPortRuleNum_Type(InterfaceIndex):
    """Custom type alaDaUNPIpPortRuleNum based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaDaUNPIpPortRuleNum_Type.__name__ = "InterfaceIndex"
_AlaDaUNPIpPortRuleNum_Object = MibTableColumn
alaDaUNPIpPortRuleNum = _AlaDaUNPIpPortRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 3),
    _AlaDaUNPIpPortRuleNum_Type()
)
alaDaUNPIpPortRuleNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleNum.setStatus("current")


class _AlaDaUNPIpPortRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPIpPortRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPIpPortRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPIpPortRuleEdgeProf_Object = MibTableColumn
alaDaUNPIpPortRuleEdgeProf = _AlaDaUNPIpPortRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 4),
    _AlaDaUNPIpPortRuleEdgeProf_Type()
)
alaDaUNPIpPortRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleEdgeProf.setStatus("deprecated")
_AlaDaUNPIpPortRuleRowStatus_Type = RowStatus
_AlaDaUNPIpPortRuleRowStatus_Object = MibTableColumn
alaDaUNPIpPortRuleRowStatus = _AlaDaUNPIpPortRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 5),
    _AlaDaUNPIpPortRuleRowStatus_Type()
)
alaDaUNPIpPortRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleRowStatus.setStatus("current")


class _AlaDaUNPIpPortRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPIpPortRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPIpPortRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPIpPortRuleVlanTag_Object = MibTableColumn
alaDaUNPIpPortRuleVlanTag = _AlaDaUNPIpPortRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 6),
    _AlaDaUNPIpPortRuleVlanTag_Type()
)
alaDaUNPIpPortRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleVlanTag.setStatus("current")


class _AlaDaUNPIpPortRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPIpPortRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPIpPortRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPIpPortRuleProfile1_Object = MibTableColumn
alaDaUNPIpPortRuleProfile1 = _AlaDaUNPIpPortRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 7),
    _AlaDaUNPIpPortRuleProfile1_Type()
)
alaDaUNPIpPortRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleProfile1.setStatus("current")


class _AlaDaUNPIpPortRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPIpPortRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPIpPortRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPIpPortRuleProfile2_Object = MibTableColumn
alaDaUNPIpPortRuleProfile2 = _AlaDaUNPIpPortRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 8),
    _AlaDaUNPIpPortRuleProfile2_Type()
)
alaDaUNPIpPortRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleProfile2.setStatus("current")


class _AlaDaUNPIpPortRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPIpPortRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPIpPortRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPIpPortRuleProfile3_Object = MibTableColumn
alaDaUNPIpPortRuleProfile3 = _AlaDaUNPIpPortRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 9),
    _AlaDaUNPIpPortRuleProfile3_Type()
)
alaDaUNPIpPortRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleProfile3.setStatus("current")


class _AlaDaUNPIpPortRuleMaskType_Type(InetAddressType):
    """Custom type alaDaUNPIpPortRuleMaskType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaUNPIpPortRuleMaskType_Type.__name__ = "InetAddressType"
_AlaDaUNPIpPortRuleMaskType_Object = MibTableColumn
alaDaUNPIpPortRuleMaskType = _AlaDaUNPIpPortRuleMaskType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 10),
    _AlaDaUNPIpPortRuleMaskType_Type()
)
alaDaUNPIpPortRuleMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleMaskType.setStatus("current")


class _AlaDaUNPIpPortRuleMask_Type(InetAddress):
    """Custom type alaDaUNPIpPortRuleMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPIpPortRuleMask_Type.__name__ = "InetAddress"
_AlaDaUNPIpPortRuleMask_Object = MibTableColumn
alaDaUNPIpPortRuleMask = _AlaDaUNPIpPortRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 30, 1, 11),
    _AlaDaUNPIpPortRuleMask_Type()
)
alaDaUNPIpPortRuleMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpPortRuleMask.setStatus("current")
_AlaDaUNPMacIpPortRuleTable_Object = MibTable
alaDaUNPMacIpPortRuleTable = _AlaDaUNPMacIpPortRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31)
)
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleTable.setStatus("current")
_AlaDaUNPMacIpPortRuleEntry_Object = MibTableRow
alaDaUNPMacIpPortRuleEntry = _AlaDaUNPMacIpPortRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1)
)
alaDaUNPMacIpPortRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleMacAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleAddrIpType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleIpAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleNum"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleEntry.setStatus("current")


class _AlaDaUNPMacIpPortRuleMacAddr_Type(MacAddress):
    """Custom type alaDaUNPMacIpPortRuleMacAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPMacIpPortRuleMacAddr_Type.__name__ = "MacAddress"
_AlaDaUNPMacIpPortRuleMacAddr_Object = MibTableColumn
alaDaUNPMacIpPortRuleMacAddr = _AlaDaUNPMacIpPortRuleMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 1),
    _AlaDaUNPMacIpPortRuleMacAddr_Type()
)
alaDaUNPMacIpPortRuleMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleMacAddr.setStatus("current")
_AlaDaUNPMacIpPortRuleAddrIpType_Type = InetAddressType
_AlaDaUNPMacIpPortRuleAddrIpType_Object = MibTableColumn
alaDaUNPMacIpPortRuleAddrIpType = _AlaDaUNPMacIpPortRuleAddrIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 2),
    _AlaDaUNPMacIpPortRuleAddrIpType_Type()
)
alaDaUNPMacIpPortRuleAddrIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleAddrIpType.setStatus("current")
_AlaDaUNPMacIpPortRuleIpAddr_Type = InetAddress
_AlaDaUNPMacIpPortRuleIpAddr_Object = MibTableColumn
alaDaUNPMacIpPortRuleIpAddr = _AlaDaUNPMacIpPortRuleIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 3),
    _AlaDaUNPMacIpPortRuleIpAddr_Type()
)
alaDaUNPMacIpPortRuleIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleIpAddr.setStatus("current")


class _AlaDaUNPMacIpPortRuleNum_Type(InterfaceIndex):
    """Custom type alaDaUNPMacIpPortRuleNum based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaDaUNPMacIpPortRuleNum_Type.__name__ = "InterfaceIndex"
_AlaDaUNPMacIpPortRuleNum_Object = MibTableColumn
alaDaUNPMacIpPortRuleNum = _AlaDaUNPMacIpPortRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 4),
    _AlaDaUNPMacIpPortRuleNum_Type()
)
alaDaUNPMacIpPortRuleNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleNum.setStatus("current")


class _AlaDaUNPMacIpPortRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPMacIpPortRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacIpPortRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacIpPortRuleEdgeProf_Object = MibTableColumn
alaDaUNPMacIpPortRuleEdgeProf = _AlaDaUNPMacIpPortRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 5),
    _AlaDaUNPMacIpPortRuleEdgeProf_Type()
)
alaDaUNPMacIpPortRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleEdgeProf.setStatus("deprecated")
_AlaDaUNPMacIpPortRuleRowStatus_Type = RowStatus
_AlaDaUNPMacIpPortRuleRowStatus_Object = MibTableColumn
alaDaUNPMacIpPortRuleRowStatus = _AlaDaUNPMacIpPortRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 6),
    _AlaDaUNPMacIpPortRuleRowStatus_Type()
)
alaDaUNPMacIpPortRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleRowStatus.setStatus("current")


class _AlaDaUNPMacIpPortRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacIpPortRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacIpPortRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacIpPortRuleVlanTag_Object = MibTableColumn
alaDaUNPMacIpPortRuleVlanTag = _AlaDaUNPMacIpPortRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 7),
    _AlaDaUNPMacIpPortRuleVlanTag_Type()
)
alaDaUNPMacIpPortRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleVlanTag.setStatus("current")


class _AlaDaUNPMacIpPortRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPMacIpPortRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPMacIpPortRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacIpPortRuleProfile1_Object = MibTableColumn
alaDaUNPMacIpPortRuleProfile1 = _AlaDaUNPMacIpPortRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 8),
    _AlaDaUNPMacIpPortRuleProfile1_Type()
)
alaDaUNPMacIpPortRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleProfile1.setStatus("current")


class _AlaDaUNPMacIpPortRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPMacIpPortRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPMacIpPortRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacIpPortRuleProfile2_Object = MibTableColumn
alaDaUNPMacIpPortRuleProfile2 = _AlaDaUNPMacIpPortRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 9),
    _AlaDaUNPMacIpPortRuleProfile2_Type()
)
alaDaUNPMacIpPortRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleProfile2.setStatus("current")


class _AlaDaUNPMacIpPortRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPMacIpPortRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPMacIpPortRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacIpPortRuleProfile3_Object = MibTableColumn
alaDaUNPMacIpPortRuleProfile3 = _AlaDaUNPMacIpPortRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 10),
    _AlaDaUNPMacIpPortRuleProfile3_Type()
)
alaDaUNPMacIpPortRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleProfile3.setStatus("current")


class _AlaDaUNPMacIpPortRuleIpMaskType_Type(InetAddressType):
    """Custom type alaDaUNPMacIpPortRuleIpMaskType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaUNPMacIpPortRuleIpMaskType_Type.__name__ = "InetAddressType"
_AlaDaUNPMacIpPortRuleIpMaskType_Object = MibTableColumn
alaDaUNPMacIpPortRuleIpMaskType = _AlaDaUNPMacIpPortRuleIpMaskType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 11),
    _AlaDaUNPMacIpPortRuleIpMaskType_Type()
)
alaDaUNPMacIpPortRuleIpMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleIpMaskType.setStatus("current")


class _AlaDaUNPMacIpPortRuleIpMask_Type(InetAddress):
    """Custom type alaDaUNPMacIpPortRuleIpMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPMacIpPortRuleIpMask_Type.__name__ = "InetAddress"
_AlaDaUNPMacIpPortRuleIpMask_Object = MibTableColumn
alaDaUNPMacIpPortRuleIpMask = _AlaDaUNPMacIpPortRuleIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 31, 1, 12),
    _AlaDaUNPMacIpPortRuleIpMask_Type()
)
alaDaUNPMacIpPortRuleIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpPortRuleIpMask.setStatus("current")
_AlaDaUNPMacGroupRuleTable_Object = MibTable
alaDaUNPMacGroupRuleTable = _AlaDaUNPMacGroupRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 32)
)
if mibBuilder.loadTexts:
    alaDaUNPMacGroupRuleTable.setStatus("deprecated")
_AlaDaUNPMacGroupRuleEntry_Object = MibTableRow
alaDaUNPMacGroupRuleEntry = _AlaDaUNPMacGroupRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 32, 1)
)
alaDaUNPMacGroupRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacGroupRuleAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacGroupRuleId"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacGroupRuleEntry.setStatus("deprecated")


class _AlaDaUNPMacGroupRuleAddr_Type(MacAddress):
    """Custom type alaDaUNPMacGroupRuleAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPMacGroupRuleAddr_Type.__name__ = "MacAddress"
_AlaDaUNPMacGroupRuleAddr_Object = MibTableColumn
alaDaUNPMacGroupRuleAddr = _AlaDaUNPMacGroupRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 32, 1, 1),
    _AlaDaUNPMacGroupRuleAddr_Type()
)
alaDaUNPMacGroupRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacGroupRuleAddr.setStatus("deprecated")


class _AlaDaUNPMacGroupRuleId_Type(Integer32):
    """Custom type alaDaUNPMacGroupRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDaUNPMacGroupRuleId_Type.__name__ = "Integer32"
_AlaDaUNPMacGroupRuleId_Object = MibTableColumn
alaDaUNPMacGroupRuleId = _AlaDaUNPMacGroupRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 32, 1, 2),
    _AlaDaUNPMacGroupRuleId_Type()
)
alaDaUNPMacGroupRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacGroupRuleId.setStatus("deprecated")


class _AlaDaUNPMacGroupRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPMacGroupRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacGroupRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacGroupRuleEdgeProf_Object = MibTableColumn
alaDaUNPMacGroupRuleEdgeProf = _AlaDaUNPMacGroupRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 32, 1, 3),
    _AlaDaUNPMacGroupRuleEdgeProf_Type()
)
alaDaUNPMacGroupRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacGroupRuleEdgeProf.setStatus("deprecated")
_AlaDaUNPMacGroupRuleRowStatus_Type = RowStatus
_AlaDaUNPMacGroupRuleRowStatus_Object = MibTableColumn
alaDaUNPMacGroupRuleRowStatus = _AlaDaUNPMacGroupRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 32, 1, 4),
    _AlaDaUNPMacGroupRuleRowStatus_Type()
)
alaDaUNPMacGroupRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacGroupRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPMacGroupRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacGroupRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacGroupRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacGroupRuleVlanTag_Object = MibTableColumn
alaDaUNPMacGroupRuleVlanTag = _AlaDaUNPMacGroupRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 32, 1, 5),
    _AlaDaUNPMacGroupRuleVlanTag_Type()
)
alaDaUNPMacGroupRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacGroupRuleVlanTag.setStatus("deprecated")
_AlaDaUNPIpGroupRuleTable_Object = MibTable
alaDaUNPIpGroupRuleTable = _AlaDaUNPIpGroupRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 33)
)
if mibBuilder.loadTexts:
    alaDaUNPIpGroupRuleTable.setStatus("deprecated")
_AlaDaUNPIpGroupRuleEntry_Object = MibTableRow
alaDaUNPIpGroupRuleEntry = _AlaDaUNPIpGroupRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 33, 1)
)
alaDaUNPIpGroupRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpGroupRuleAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpGroupRuleAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpGroupRuleNum"),
)
if mibBuilder.loadTexts:
    alaDaUNPIpGroupRuleEntry.setStatus("deprecated")
_AlaDaUNPIpGroupRuleAddrType_Type = InetAddressType
_AlaDaUNPIpGroupRuleAddrType_Object = MibTableColumn
alaDaUNPIpGroupRuleAddrType = _AlaDaUNPIpGroupRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 33, 1, 1),
    _AlaDaUNPIpGroupRuleAddrType_Type()
)
alaDaUNPIpGroupRuleAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpGroupRuleAddrType.setStatus("deprecated")
_AlaDaUNPIpGroupRuleAddr_Type = InetAddress
_AlaDaUNPIpGroupRuleAddr_Object = MibTableColumn
alaDaUNPIpGroupRuleAddr = _AlaDaUNPIpGroupRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 33, 1, 2),
    _AlaDaUNPIpGroupRuleAddr_Type()
)
alaDaUNPIpGroupRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpGroupRuleAddr.setStatus("deprecated")


class _AlaDaUNPIpGroupRuleNum_Type(Integer32):
    """Custom type alaDaUNPIpGroupRuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDaUNPIpGroupRuleNum_Type.__name__ = "Integer32"
_AlaDaUNPIpGroupRuleNum_Object = MibTableColumn
alaDaUNPIpGroupRuleNum = _AlaDaUNPIpGroupRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 33, 1, 3),
    _AlaDaUNPIpGroupRuleNum_Type()
)
alaDaUNPIpGroupRuleNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpGroupRuleNum.setStatus("deprecated")


class _AlaDaUNPIpGroupRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPIpGroupRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPIpGroupRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPIpGroupRuleEdgeProf_Object = MibTableColumn
alaDaUNPIpGroupRuleEdgeProf = _AlaDaUNPIpGroupRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 33, 1, 4),
    _AlaDaUNPIpGroupRuleEdgeProf_Type()
)
alaDaUNPIpGroupRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpGroupRuleEdgeProf.setStatus("deprecated")
_AlaDaUNPIpGroupRuleRowStatus_Type = RowStatus
_AlaDaUNPIpGroupRuleRowStatus_Object = MibTableColumn
alaDaUNPIpGroupRuleRowStatus = _AlaDaUNPIpGroupRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 33, 1, 5),
    _AlaDaUNPIpGroupRuleRowStatus_Type()
)
alaDaUNPIpGroupRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpGroupRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPIpGroupRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPIpGroupRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPIpGroupRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPIpGroupRuleVlanTag_Object = MibTableColumn
alaDaUNPIpGroupRuleVlanTag = _AlaDaUNPIpGroupRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 33, 1, 6),
    _AlaDaUNPIpGroupRuleVlanTag_Type()
)
alaDaUNPIpGroupRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpGroupRuleVlanTag.setStatus("deprecated")
_AlaDaUNPMacIpGroupRuleTable_Object = MibTable
alaDaUNPMacIpGroupRuleTable = _AlaDaUNPMacIpGroupRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 34)
)
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroupRuleTable.setStatus("deprecated")
_AlaDaUNPMacIpGroupRuleEntry_Object = MibTableRow
alaDaUNPMacIpGroupRuleEntry = _AlaDaUNPMacIpGroupRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 34, 1)
)
alaDaUNPMacIpGroupRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpGroupRuleMacAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpGroupRuleIpAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpGroupRuleIpAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpGroupRuleId"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroupRuleEntry.setStatus("deprecated")


class _AlaDaUNPMacIpGroupRuleMacAddr_Type(MacAddress):
    """Custom type alaDaUNPMacIpGroupRuleMacAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPMacIpGroupRuleMacAddr_Type.__name__ = "MacAddress"
_AlaDaUNPMacIpGroupRuleMacAddr_Object = MibTableColumn
alaDaUNPMacIpGroupRuleMacAddr = _AlaDaUNPMacIpGroupRuleMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 34, 1, 1),
    _AlaDaUNPMacIpGroupRuleMacAddr_Type()
)
alaDaUNPMacIpGroupRuleMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroupRuleMacAddr.setStatus("deprecated")
_AlaDaUNPMacIpGroupRuleIpAddrType_Type = InetAddressType
_AlaDaUNPMacIpGroupRuleIpAddrType_Object = MibTableColumn
alaDaUNPMacIpGroupRuleIpAddrType = _AlaDaUNPMacIpGroupRuleIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 34, 1, 2),
    _AlaDaUNPMacIpGroupRuleIpAddrType_Type()
)
alaDaUNPMacIpGroupRuleIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroupRuleIpAddrType.setStatus("deprecated")
_AlaDaUNPMacIpGroupRuleIpAddr_Type = InetAddress
_AlaDaUNPMacIpGroupRuleIpAddr_Object = MibTableColumn
alaDaUNPMacIpGroupRuleIpAddr = _AlaDaUNPMacIpGroupRuleIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 34, 1, 3),
    _AlaDaUNPMacIpGroupRuleIpAddr_Type()
)
alaDaUNPMacIpGroupRuleIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroupRuleIpAddr.setStatus("deprecated")


class _AlaDaUNPMacIpGroupRuleId_Type(Integer32):
    """Custom type alaDaUNPMacIpGroupRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDaUNPMacIpGroupRuleId_Type.__name__ = "Integer32"
_AlaDaUNPMacIpGroupRuleId_Object = MibTableColumn
alaDaUNPMacIpGroupRuleId = _AlaDaUNPMacIpGroupRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 34, 1, 4),
    _AlaDaUNPMacIpGroupRuleId_Type()
)
alaDaUNPMacIpGroupRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroupRuleId.setStatus("deprecated")


class _AlaDaUNPMacIpGroupRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPMacIpGroupRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacIpGroupRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacIpGroupRuleEdgeProf_Object = MibTableColumn
alaDaUNPMacIpGroupRuleEdgeProf = _AlaDaUNPMacIpGroupRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 34, 1, 5),
    _AlaDaUNPMacIpGroupRuleEdgeProf_Type()
)
alaDaUNPMacIpGroupRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroupRuleEdgeProf.setStatus("deprecated")
_AlaDaUNPMacIpGroupRuleRowStatus_Type = RowStatus
_AlaDaUNPMacIpGroupRuleRowStatus_Object = MibTableColumn
alaDaUNPMacIpGroupRuleRowStatus = _AlaDaUNPMacIpGroupRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 34, 1, 6),
    _AlaDaUNPMacIpGroupRuleRowStatus_Type()
)
alaDaUNPMacIpGroupRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroupRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPMacIpGroupRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacIpGroupRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacIpGroupRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacIpGroupRuleVlanTag_Object = MibTableColumn
alaDaUNPMacIpGroupRuleVlanTag = _AlaDaUNPMacIpGroupRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 34, 1, 7),
    _AlaDaUNPMacIpGroupRuleVlanTag_Type()
)
alaDaUNPMacIpGroupRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroupRuleVlanTag.setStatus("deprecated")
_AlaDaUNPUserRoleTable_Object = MibTable
alaDaUNPUserRoleTable = _AlaDaUNPUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35)
)
if mibBuilder.loadTexts:
    alaDaUNPUserRoleTable.setStatus("current")
_AlaDaUNPUserRoleEntry_Object = MibTableRow
alaDaUNPUserRoleEntry = _AlaDaUNPUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1)
)
alaDaUNPUserRoleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPUserRoleName"),
)
if mibBuilder.loadTexts:
    alaDaUNPUserRoleEntry.setStatus("current")


class _AlaDaUNPUserRoleName_Type(SnmpAdminString):
    """Custom type alaDaUNPUserRoleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPUserRoleName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPUserRoleName_Object = MibTableColumn
alaDaUNPUserRoleName = _AlaDaUNPUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 1),
    _AlaDaUNPUserRoleName_Type()
)
alaDaUNPUserRoleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPUserRoleName.setStatus("current")


class _AlaDaUNPUserRolePrecedenceNum_Type(Integer32):
    """Custom type alaDaUNPUserRolePrecedenceNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaDaUNPUserRolePrecedenceNum_Type.__name__ = "Integer32"
_AlaDaUNPUserRolePrecedenceNum_Object = MibTableColumn
alaDaUNPUserRolePrecedenceNum = _AlaDaUNPUserRolePrecedenceNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 2),
    _AlaDaUNPUserRolePrecedenceNum_Type()
)
alaDaUNPUserRolePrecedenceNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRolePrecedenceNum.setStatus("current")


class _AlaDaUNPUserRolePolicyList_Type(SnmpAdminString):
    """Custom type alaDaUNPUserRolePolicyList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPUserRolePolicyList_Type.__name__ = "SnmpAdminString"
_AlaDaUNPUserRolePolicyList_Object = MibTableColumn
alaDaUNPUserRolePolicyList = _AlaDaUNPUserRolePolicyList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 3),
    _AlaDaUNPUserRolePolicyList_Type()
)
alaDaUNPUserRolePolicyList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRolePolicyList.setStatus("current")


class _AlaDaUNPUserRoleEdgeProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPUserRoleEdgeProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPUserRoleEdgeProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPUserRoleEdgeProfile_Object = MibTableColumn
alaDaUNPUserRoleEdgeProfile = _AlaDaUNPUserRoleEdgeProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 4),
    _AlaDaUNPUserRoleEdgeProfile_Type()
)
alaDaUNPUserRoleEdgeProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRoleEdgeProfile.setStatus("deprecated")


class _AlaDaUNPUserRoleAuthType_Type(Integer32):
    """Custom type alaDaUNPUserRoleAuthType based on Integer32"""
    defaultValue = 1

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
        *(("noAuth", 0),
          ("none", 1),
          ("dot1x", 2),
          ("mac", 3),
          ("dot1xFail", 4),
          ("macFail", 5))
    )


_AlaDaUNPUserRoleAuthType_Type.__name__ = "Integer32"
_AlaDaUNPUserRoleAuthType_Object = MibTableColumn
alaDaUNPUserRoleAuthType = _AlaDaUNPUserRoleAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 5),
    _AlaDaUNPUserRoleAuthType_Type()
)
alaDaUNPUserRoleAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRoleAuthType.setStatus("current")


class _AlaDaUNPUserRolePostLoginStatus_Type(Integer32):
    """Custom type alaDaUNPUserRolePostLoginStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPUserRolePostLoginStatus_Type.__name__ = "Integer32"
_AlaDaUNPUserRolePostLoginStatus_Object = MibTableColumn
alaDaUNPUserRolePostLoginStatus = _AlaDaUNPUserRolePostLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 6),
    _AlaDaUNPUserRolePostLoginStatus_Type()
)
alaDaUNPUserRolePostLoginStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRolePostLoginStatus.setStatus("current")
_AlaDaUNPUserRoleRowStatus_Type = RowStatus
_AlaDaUNPUserRoleRowStatus_Object = MibTableColumn
alaDaUNPUserRoleRowStatus = _AlaDaUNPUserRoleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 7),
    _AlaDaUNPUserRoleRowStatus_Type()
)
alaDaUNPUserRoleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRoleRowStatus.setStatus("current")


class _AlaDaUNPUserRoleKerberosPostLoginStatus_Type(Integer32):
    """Custom type alaDaUNPUserRoleKerberosPostLoginStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPUserRoleKerberosPostLoginStatus_Type.__name__ = "Integer32"
_AlaDaUNPUserRoleKerberosPostLoginStatus_Object = MibTableColumn
alaDaUNPUserRoleKerberosPostLoginStatus = _AlaDaUNPUserRoleKerberosPostLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 8),
    _AlaDaUNPUserRoleKerberosPostLoginStatus_Type()
)
alaDaUNPUserRoleKerberosPostLoginStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRoleKerberosPostLoginStatus.setStatus("current")


class _AlaDaUNPUserRoleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPUserRoleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPUserRoleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPUserRoleProfile1_Object = MibTableColumn
alaDaUNPUserRoleProfile1 = _AlaDaUNPUserRoleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 9),
    _AlaDaUNPUserRoleProfile1_Type()
)
alaDaUNPUserRoleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRoleProfile1.setStatus("current")


class _AlaDaUNPUserRoleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPUserRoleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPUserRoleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPUserRoleProfile2_Object = MibTableColumn
alaDaUNPUserRoleProfile2 = _AlaDaUNPUserRoleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 10),
    _AlaDaUNPUserRoleProfile2_Type()
)
alaDaUNPUserRoleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRoleProfile2.setStatus("current")


class _AlaDaUNPUserRoleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPUserRoleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPUserRoleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPUserRoleProfile3_Object = MibTableColumn
alaDaUNPUserRoleProfile3 = _AlaDaUNPUserRoleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 35, 1, 11),
    _AlaDaUNPUserRoleProfile3_Type()
)
alaDaUNPUserRoleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPUserRoleProfile3.setStatus("current")
_AlaDaUNPRstrctedRoleTable_Object = MibTable
alaDaUNPRstrctedRoleTable = _AlaDaUNPRstrctedRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 36)
)
if mibBuilder.loadTexts:
    alaDaUNPRstrctedRoleTable.setStatus("current")
_AlaDaUNPRstrctedRoleEntry_Object = MibTableRow
alaDaUNPRstrctedRoleEntry = _AlaDaUNPRstrctedRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 36, 1)
)
alaDaUNPRstrctedRoleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPRstrctedRoleType"),
)
if mibBuilder.loadTexts:
    alaDaUNPRstrctedRoleEntry.setStatus("current")


class _AlaDaUNPRstrctedRoleType_Type(Integer32):
    """Custom type alaDaUNPRstrctedRoleType based on Integer32"""
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
        *(("unauthorized", 1),
          ("hic", 2),
          ("qmr", 3),
          ("blacklist", 4),
          ("cpPreLogin", 5),
          ("kerberosPreLogin", 6))
    )


_AlaDaUNPRstrctedRoleType_Type.__name__ = "Integer32"
_AlaDaUNPRstrctedRoleType_Object = MibTableColumn
alaDaUNPRstrctedRoleType = _AlaDaUNPRstrctedRoleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 36, 1, 1),
    _AlaDaUNPRstrctedRoleType_Type()
)
alaDaUNPRstrctedRoleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPRstrctedRoleType.setStatus("current")


class _AlaDaUNPRstrctedRolePolicyList_Type(SnmpAdminString):
    """Custom type alaDaUNPRstrctedRolePolicyList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPRstrctedRolePolicyList_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRstrctedRolePolicyList_Object = MibTableColumn
alaDaUNPRstrctedRolePolicyList = _AlaDaUNPRstrctedRolePolicyList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 36, 1, 2),
    _AlaDaUNPRstrctedRolePolicyList_Type()
)
alaDaUNPRstrctedRolePolicyList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRstrctedRolePolicyList.setStatus("current")
_AlaDaUNPRstrctedRoleRowStatus_Type = RowStatus
_AlaDaUNPRstrctedRoleRowStatus_Object = MibTableColumn
alaDaUNPRstrctedRoleRowStatus = _AlaDaUNPRstrctedRoleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 36, 1, 3),
    _AlaDaUNPRstrctedRoleRowStatus_Type()
)
alaDaUNPRstrctedRoleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRstrctedRoleRowStatus.setStatus("current")
_AlaDaUNPVlanMapTable_Object = MibTable
alaDaUNPVlanMapTable = _AlaDaUNPVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 37)
)
if mibBuilder.loadTexts:
    alaDaUNPVlanMapTable.setStatus("deprecated")
_AlaDaUNPVlanMapEntry_Object = MibTableRow
alaDaUNPVlanMapEntry = _AlaDaUNPVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 37, 1)
)
alaDaUNPVlanMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVlanMapEdgeProf"),
)
if mibBuilder.loadTexts:
    alaDaUNPVlanMapEntry.setStatus("deprecated")


class _AlaDaUNPVlanMapEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPVlanMapEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPVlanMapEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVlanMapEdgeProf_Object = MibTableColumn
alaDaUNPVlanMapEdgeProf = _AlaDaUNPVlanMapEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 37, 1, 1),
    _AlaDaUNPVlanMapEdgeProf_Type()
)
alaDaUNPVlanMapEdgeProf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVlanMapEdgeProf.setStatus("deprecated")


class _AlaDaUNPVlanMapIdent_Type(Integer32):
    """Custom type alaDaUNPVlanMapIdent based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPVlanMapIdent_Type.__name__ = "Integer32"
_AlaDaUNPVlanMapIdent_Object = MibTableColumn
alaDaUNPVlanMapIdent = _AlaDaUNPVlanMapIdent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 37, 1, 2),
    _AlaDaUNPVlanMapIdent_Type()
)
alaDaUNPVlanMapIdent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVlanMapIdent.setStatus("deprecated")
_AlaDaUNPVlanMapRowStatus_Type = RowStatus
_AlaDaUNPVlanMapRowStatus_Object = MibTableColumn
alaDaUNPVlanMapRowStatus = _AlaDaUNPVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 37, 1, 3),
    _AlaDaUNPVlanMapRowStatus_Type()
)
alaDaUNPVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVlanMapRowStatus.setStatus("deprecated")
_AlaDaUnpGroupIdTable_Object = MibTable
alaDaUnpGroupIdTable = _AlaDaUnpGroupIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 38)
)
if mibBuilder.loadTexts:
    alaDaUnpGroupIdTable.setStatus("deprecated")
_AlaDaUnpGroupIdEntry_Object = MibTableRow
alaDaUnpGroupIdEntry = _AlaDaUnpGroupIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 38, 1)
)
alaDaUnpGroupIdEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUnpGroupId"),
)
if mibBuilder.loadTexts:
    alaDaUnpGroupIdEntry.setStatus("deprecated")


class _AlaDaUnpGroupId_Type(Integer32):
    """Custom type alaDaUnpGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDaUnpGroupId_Type.__name__ = "Integer32"
_AlaDaUnpGroupId_Object = MibTableColumn
alaDaUnpGroupId = _AlaDaUnpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 38, 1, 1),
    _AlaDaUnpGroupId_Type()
)
alaDaUnpGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUnpGroupId.setStatus("deprecated")


class _AlaDaUnpGroupDescription_Type(SnmpAdminString):
    """Custom type alaDaUnpGroupDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AlaDaUnpGroupDescription_Type.__name__ = "SnmpAdminString"
_AlaDaUnpGroupDescription_Object = MibTableColumn
alaDaUnpGroupDescription = _AlaDaUnpGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 38, 1, 2),
    _AlaDaUnpGroupDescription_Type()
)
alaDaUnpGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUnpGroupDescription.setStatus("deprecated")
_AlaDaUnpGroupIdRowStatus_Type = RowStatus
_AlaDaUnpGroupIdRowStatus_Object = MibTableColumn
alaDaUnpGroupIdRowStatus = _AlaDaUnpGroupIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 38, 1, 3),
    _AlaDaUnpGroupIdRowStatus_Type()
)
alaDaUnpGroupIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUnpGroupIdRowStatus.setStatus("deprecated")
_AlaDaUNPEdgeFlushTable_Object = MibTable
alaDaUNPEdgeFlushTable = _AlaDaUNPEdgeFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 39)
)
if mibBuilder.loadTexts:
    alaDaUNPEdgeFlushTable.setStatus("current")
_AlaDaUNPEdgeFlushEntry_Object = MibTableRow
alaDaUNPEdgeFlushEntry = _AlaDaUNPEdgeFlushEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 39, 1)
)
alaDaUNPEdgeFlushEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeFlushIndex"),
)
if mibBuilder.loadTexts:
    alaDaUNPEdgeFlushEntry.setStatus("current")


class _AlaDaUNPEdgeFlushIndex_Type(Integer32):
    """Custom type alaDaUNPEdgeFlushIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaDaUNPEdgeFlushIndex_Type.__name__ = "Integer32"
_AlaDaUNPEdgeFlushIndex_Object = MibTableColumn
alaDaUNPEdgeFlushIndex = _AlaDaUNPEdgeFlushIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 39, 1, 1),
    _AlaDaUNPEdgeFlushIndex_Type()
)
alaDaUNPEdgeFlushIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPEdgeFlushIndex.setStatus("current")
_AlaDaUNPEdgeFlushPortLow_Type = InterfaceIndex
_AlaDaUNPEdgeFlushPortLow_Object = MibTableColumn
alaDaUNPEdgeFlushPortLow = _AlaDaUNPEdgeFlushPortLow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 39, 1, 2),
    _AlaDaUNPEdgeFlushPortLow_Type()
)
alaDaUNPEdgeFlushPortLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPEdgeFlushPortLow.setStatus("current")
_AlaDaUNPEdgeFlushPortHigh_Type = InterfaceIndex
_AlaDaUNPEdgeFlushPortHigh_Object = MibTableColumn
alaDaUNPEdgeFlushPortHigh = _AlaDaUNPEdgeFlushPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 39, 1, 3),
    _AlaDaUNPEdgeFlushPortHigh_Type()
)
alaDaUNPEdgeFlushPortHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPEdgeFlushPortHigh.setStatus("current")


class _AlaDaUNPEdgeFlushType_Type(Integer32):
    """Custom type alaDaUNPEdgeFlushType based on Integer32"""
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
        *(("noAuth", 1),
          ("onex", 2),
          ("mac", 3),
          ("none", 4))
    )


_AlaDaUNPEdgeFlushType_Type.__name__ = "Integer32"
_AlaDaUNPEdgeFlushType_Object = MibTableColumn
alaDaUNPEdgeFlushType = _AlaDaUNPEdgeFlushType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 39, 1, 4),
    _AlaDaUNPEdgeFlushType_Type()
)
alaDaUNPEdgeFlushType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPEdgeFlushType.setStatus("current")


class _AlaDaUNPEdgrFlushMac_Type(MacAddress):
    """Custom type alaDaUNPEdgrFlushMac based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPEdgrFlushMac_Type.__name__ = "MacAddress"
_AlaDaUNPEdgrFlushMac_Object = MibTableColumn
alaDaUNPEdgrFlushMac = _AlaDaUNPEdgrFlushMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 39, 1, 5),
    _AlaDaUNPEdgrFlushMac_Type()
)
alaDaUNPEdgrFlushMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPEdgrFlushMac.setStatus("current")


class _AlaDaUNPEdgeFlushComplete_Type(Integer32):
    """Custom type alaDaUNPEdgeFlushComplete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("all", 2))
    )


_AlaDaUNPEdgeFlushComplete_Type.__name__ = "Integer32"
_AlaDaUNPEdgeFlushComplete_Object = MibTableColumn
alaDaUNPEdgeFlushComplete = _AlaDaUNPEdgeFlushComplete_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 39, 1, 6),
    _AlaDaUNPEdgeFlushComplete_Type()
)
alaDaUNPEdgeFlushComplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPEdgeFlushComplete.setStatus("current")


class _AlaDaUNPEdgeFlushProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPEdgeFlushProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPEdgeFlushProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPEdgeFlushProfile_Object = MibTableColumn
alaDaUNPEdgeFlushProfile = _AlaDaUNPEdgeFlushProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 39, 1, 7),
    _AlaDaUNPEdgeFlushProfile_Type()
)
alaDaUNPEdgeFlushProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPEdgeFlushProfile.setStatus("current")
_AlaDaUNPMacRulesTable_Object = MibTable
alaDaUNPMacRulesTable = _AlaDaUNPMacRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 40)
)
if mibBuilder.loadTexts:
    alaDaUNPMacRulesTable.setStatus("deprecated")
_AlaDaUNPMacRulesEntry_Object = MibTableRow
alaDaUNPMacRulesEntry = _AlaDaUNPMacRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 40, 1)
)
alaDaUNPMacRulesEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacRulesMacAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacRulesEntry.setStatus("deprecated")


class _AlaDaUNPMacRulesMacAddr_Type(MacAddress):
    """Custom type alaDaUNPMacRulesMacAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPMacRulesMacAddr_Type.__name__ = "MacAddress"
_AlaDaUNPMacRulesMacAddr_Object = MibTableColumn
alaDaUNPMacRulesMacAddr = _AlaDaUNPMacRulesMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 40, 1, 1),
    _AlaDaUNPMacRulesMacAddr_Type()
)
alaDaUNPMacRulesMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacRulesMacAddr.setStatus("deprecated")


class _AlaDaUNPMacRulesEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPMacRulesEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacRulesEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacRulesEdgeProf_Object = MibTableColumn
alaDaUNPMacRulesEdgeProf = _AlaDaUNPMacRulesEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 40, 1, 2),
    _AlaDaUNPMacRulesEdgeProf_Type()
)
alaDaUNPMacRulesEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRulesEdgeProf.setStatus("deprecated")
_AlaDaUNPMacRulesRowStatus_Type = RowStatus
_AlaDaUNPMacRulesRowStatus_Object = MibTableColumn
alaDaUNPMacRulesRowStatus = _AlaDaUNPMacRulesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 40, 1, 3),
    _AlaDaUNPMacRulesRowStatus_Type()
)
alaDaUNPMacRulesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRulesRowStatus.setStatus("deprecated")


class _AlaDaUNPMacRulesVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacRulesVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacRulesVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacRulesVlanTag_Object = MibTableColumn
alaDaUNPMacRulesVlanTag = _AlaDaUNPMacRulesVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 40, 1, 4),
    _AlaDaUNPMacRulesVlanTag_Type()
)
alaDaUNPMacRulesVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRulesVlanTag.setStatus("deprecated")
_AlaDaUNPMacRangeTable_Object = MibTable
alaDaUNPMacRangeTable = _AlaDaUNPMacRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 41)
)
if mibBuilder.loadTexts:
    alaDaUNPMacRangeTable.setStatus("deprecated")
_AlaDaUNPMacRangeEntry_Object = MibTableRow
alaDaUNPMacRangeEntry = _AlaDaUNPMacRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 41, 1)
)
alaDaUNPMacRangeEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeStartMacAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacRangeEntry.setStatus("deprecated")


class _AlaDaUNPMacRangeStartMacAddr_Type(MacAddress):
    """Custom type alaDaUNPMacRangeStartMacAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPMacRangeStartMacAddr_Type.__name__ = "MacAddress"
_AlaDaUNPMacRangeStartMacAddr_Object = MibTableColumn
alaDaUNPMacRangeStartMacAddr = _AlaDaUNPMacRangeStartMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 41, 1, 1),
    _AlaDaUNPMacRangeStartMacAddr_Type()
)
alaDaUNPMacRangeStartMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeStartMacAddr.setStatus("deprecated")


class _AlaDaUNPMacRangeEndMacAddr_Type(MacAddress):
    """Custom type alaDaUNPMacRangeEndMacAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPMacRangeEndMacAddr_Type.__name__ = "MacAddress"
_AlaDaUNPMacRangeEndMacAddr_Object = MibTableColumn
alaDaUNPMacRangeEndMacAddr = _AlaDaUNPMacRangeEndMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 41, 1, 2),
    _AlaDaUNPMacRangeEndMacAddr_Type()
)
alaDaUNPMacRangeEndMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeEndMacAddr.setStatus("deprecated")


class _AlaDaUNPMacRangeEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPMacRangeEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacRangeEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacRangeEdgeProf_Object = MibTableColumn
alaDaUNPMacRangeEdgeProf = _AlaDaUNPMacRangeEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 41, 1, 3),
    _AlaDaUNPMacRangeEdgeProf_Type()
)
alaDaUNPMacRangeEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeEdgeProf.setStatus("deprecated")
_AlaDaUNPMacRangeRowStatus_Type = RowStatus
_AlaDaUNPMacRangeRowStatus_Object = MibTableColumn
alaDaUNPMacRangeRowStatus = _AlaDaUNPMacRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 41, 1, 4),
    _AlaDaUNPMacRangeRowStatus_Type()
)
alaDaUNPMacRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRowStatus.setStatus("deprecated")


class _AlaDaUNPMacRangeVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacRangeVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacRangeVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacRangeVlanTag_Object = MibTableColumn
alaDaUNPMacRangeVlanTag = _AlaDaUNPMacRangeVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 41, 1, 5),
    _AlaDaUNPMacRangeVlanTag_Type()
)
alaDaUNPMacRangeVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeVlanTag.setStatus("deprecated")
_AlaDaUNPIpMaskRuleTable_Object = MibTable
alaDaUNPIpMaskRuleTable = _AlaDaUNPIpMaskRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 42)
)
if mibBuilder.loadTexts:
    alaDaUNPIpMaskRuleTable.setStatus("deprecated")
_AlaDaUNPIpMaskRuleEntry_Object = MibTableRow
alaDaUNPIpMaskRuleEntry = _AlaDaUNPIpMaskRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 42, 1)
)
alaDaUNPIpMaskRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpMaskRuleAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpMaskRuleAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpMaskRuleMaskType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpMaskRuleMask"),
)
if mibBuilder.loadTexts:
    alaDaUNPIpMaskRuleEntry.setStatus("deprecated")
_AlaDaUNPIpMaskRuleAddrType_Type = InetAddressType
_AlaDaUNPIpMaskRuleAddrType_Object = MibTableColumn
alaDaUNPIpMaskRuleAddrType = _AlaDaUNPIpMaskRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 42, 1, 1),
    _AlaDaUNPIpMaskRuleAddrType_Type()
)
alaDaUNPIpMaskRuleAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpMaskRuleAddrType.setStatus("deprecated")
_AlaDaUNPIpMaskRuleAddr_Type = InetAddress
_AlaDaUNPIpMaskRuleAddr_Object = MibTableColumn
alaDaUNPIpMaskRuleAddr = _AlaDaUNPIpMaskRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 42, 1, 2),
    _AlaDaUNPIpMaskRuleAddr_Type()
)
alaDaUNPIpMaskRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpMaskRuleAddr.setStatus("deprecated")
_AlaDaUNPIpMaskRuleMaskType_Type = InetAddressType
_AlaDaUNPIpMaskRuleMaskType_Object = MibTableColumn
alaDaUNPIpMaskRuleMaskType = _AlaDaUNPIpMaskRuleMaskType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 42, 1, 3),
    _AlaDaUNPIpMaskRuleMaskType_Type()
)
alaDaUNPIpMaskRuleMaskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpMaskRuleMaskType.setStatus("deprecated")
_AlaDaUNPIpMaskRuleMask_Type = InetAddress
_AlaDaUNPIpMaskRuleMask_Object = MibTableColumn
alaDaUNPIpMaskRuleMask = _AlaDaUNPIpMaskRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 42, 1, 4),
    _AlaDaUNPIpMaskRuleMask_Type()
)
alaDaUNPIpMaskRuleMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpMaskRuleMask.setStatus("deprecated")


class _AlaDaUNPIpMaskRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPIpMaskRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPIpMaskRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPIpMaskRuleEdgeProf_Object = MibTableColumn
alaDaUNPIpMaskRuleEdgeProf = _AlaDaUNPIpMaskRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 42, 1, 5),
    _AlaDaUNPIpMaskRuleEdgeProf_Type()
)
alaDaUNPIpMaskRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpMaskRuleEdgeProf.setStatus("deprecated")
_AlaDaUNPIpMaskRuleRowStatus_Type = RowStatus
_AlaDaUNPIpMaskRuleRowStatus_Object = MibTableColumn
alaDaUNPIpMaskRuleRowStatus = _AlaDaUNPIpMaskRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 42, 1, 6),
    _AlaDaUNPIpMaskRuleRowStatus_Type()
)
alaDaUNPIpMaskRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpMaskRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPIpMaskRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPIpMaskRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPIpMaskRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPIpMaskRuleVlanTag_Object = MibTableColumn
alaDaUNPIpMaskRuleVlanTag = _AlaDaUNPIpMaskRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 42, 1, 7),
    _AlaDaUNPIpMaskRuleVlanTag_Type()
)
alaDaUNPIpMaskRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpMaskRuleVlanTag.setStatus("deprecated")
_AlaDaQMRMIBObjects_ObjectIdentity = ObjectIdentity
alaDaQMRMIBObjects = _AlaDaQMRMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43)
)
_AlaDaQMRGlobalConfig_ObjectIdentity = ObjectIdentity
alaDaQMRGlobalConfig = _AlaDaQMRGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 1)
)


class _AlaDaQMRPage_Type(Integer32):
    """Custom type alaDaQMRPage based on Integer32"""
    defaultValue = 2

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


_AlaDaQMRPage_Type.__name__ = "Integer32"
_AlaDaQMRPage_Object = MibScalar
alaDaQMRPage = _AlaDaQMRPage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 1, 1),
    _AlaDaQMRPage_Type()
)
alaDaQMRPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaQMRPage.setStatus("current")


class _AlaDaQMRPath_Type(SnmpAdminString):
    """Custom type alaDaQMRPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaDaQMRPath_Type.__name__ = "SnmpAdminString"
_AlaDaQMRPath_Object = MibScalar
alaDaQMRPath = _AlaDaQMRPath_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 1, 2),
    _AlaDaQMRPath_Type()
)
alaDaQMRPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaQMRPath.setStatus("current")


class _AlaDaQMRCustomHttpProxyPort_Type(Integer32):
    """Custom type alaDaQMRCustomHttpProxyPort based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1025, 65535),
    )


_AlaDaQMRCustomHttpProxyPort_Type.__name__ = "Integer32"
_AlaDaQMRCustomHttpProxyPort_Object = MibScalar
alaDaQMRCustomHttpProxyPort = _AlaDaQMRCustomHttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 1, 3),
    _AlaDaQMRCustomHttpProxyPort_Type()
)
alaDaQMRCustomHttpProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaQMRCustomHttpProxyPort.setStatus("current")


class _AlaDaQMRPolicyList_Type(SnmpAdminString):
    """Custom type alaDaQMRPolicyList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaQMRPolicyList_Type.__name__ = "SnmpAdminString"
_AlaDaQMRPolicyList_Object = MibScalar
alaDaQMRPolicyList = _AlaDaQMRPolicyList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 1, 4),
    _AlaDaQMRPolicyList_Type()
)
alaDaQMRPolicyList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaQMRPolicyList.setStatus("current")
_AlaDaQMRAllowedTable_Object = MibTable
alaDaQMRAllowedTable = _AlaDaQMRAllowedTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 2)
)
if mibBuilder.loadTexts:
    alaDaQMRAllowedTable.setStatus("current")
_AlaDaQMRAllowedEntry_Object = MibTableRow
alaDaQMRAllowedEntry = _AlaDaQMRAllowedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 2, 1)
)
alaDaQMRAllowedEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaQMRAllowedName"),
)
if mibBuilder.loadTexts:
    alaDaQMRAllowedEntry.setStatus("current")


class _AlaDaQMRAllowedName_Type(SnmpAdminString):
    """Custom type alaDaQMRAllowedName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaQMRAllowedName_Type.__name__ = "SnmpAdminString"
_AlaDaQMRAllowedName_Object = MibTableColumn
alaDaQMRAllowedName = _AlaDaQMRAllowedName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 2, 1, 1),
    _AlaDaQMRAllowedName_Type()
)
alaDaQMRAllowedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaQMRAllowedName.setStatus("current")
_AlaDaQMRAllowedIpAddrType_Type = InetAddressType
_AlaDaQMRAllowedIpAddrType_Object = MibTableColumn
alaDaQMRAllowedIpAddrType = _AlaDaQMRAllowedIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 2, 1, 2),
    _AlaDaQMRAllowedIpAddrType_Type()
)
alaDaQMRAllowedIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaQMRAllowedIpAddrType.setStatus("current")


class _AlaDaQMRAllowedIpAddr_Type(InetAddress):
    """Custom type alaDaQMRAllowedIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaQMRAllowedIpAddr_Type.__name__ = "InetAddress"
_AlaDaQMRAllowedIpAddr_Object = MibTableColumn
alaDaQMRAllowedIpAddr = _AlaDaQMRAllowedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 2, 1, 3),
    _AlaDaQMRAllowedIpAddr_Type()
)
alaDaQMRAllowedIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaQMRAllowedIpAddr.setStatus("current")
_AlaDaQMRAllowedIpMaskType_Type = InetAddressType
_AlaDaQMRAllowedIpMaskType_Object = MibTableColumn
alaDaQMRAllowedIpMaskType = _AlaDaQMRAllowedIpMaskType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 2, 1, 4),
    _AlaDaQMRAllowedIpMaskType_Type()
)
alaDaQMRAllowedIpMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaQMRAllowedIpMaskType.setStatus("current")


class _AlaDaQMRAllowedIpMask_Type(InetAddress):
    """Custom type alaDaQMRAllowedIpMask based on InetAddress"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaQMRAllowedIpMask_Type.__name__ = "InetAddress"
_AlaDaQMRAllowedIpMask_Object = MibTableColumn
alaDaQMRAllowedIpMask = _AlaDaQMRAllowedIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 2, 1, 5),
    _AlaDaQMRAllowedIpMask_Type()
)
alaDaQMRAllowedIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaQMRAllowedIpMask.setStatus("current")
_AlaDaQMRAllowedRowStatus_Type = RowStatus
_AlaDaQMRAllowedRowStatus_Object = MibTableColumn
alaDaQMRAllowedRowStatus = _AlaDaQMRAllowedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 43, 2, 1, 6),
    _AlaDaQMRAllowedRowStatus_Type()
)
alaDaQMRAllowedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaQMRAllowedRowStatus.setStatus("current")
_AlaDaUNPValidityPeriodTable_Object = MibTable
alaDaUNPValidityPeriodTable = _AlaDaUNPValidityPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44)
)
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodTable.setStatus("current")
_AlaDaUNPValidityPeriodEntry_Object = MibTableRow
alaDaUNPValidityPeriodEntry = _AlaDaUNPValidityPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1)
)
alaDaUNPValidityPeriodEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodName"),
)
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodEntry.setStatus("current")


class _AlaDaUNPValidityPeriodName_Type(SnmpAdminString):
    """Custom type alaDaUNPValidityPeriodName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPValidityPeriodName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPValidityPeriodName_Object = MibTableColumn
alaDaUNPValidityPeriodName = _AlaDaUNPValidityPeriodName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 1),
    _AlaDaUNPValidityPeriodName_Type()
)
alaDaUNPValidityPeriodName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodName.setStatus("current")
_AlaDaUNPValidityPeriodDays_Type = Integer32
_AlaDaUNPValidityPeriodDays_Object = MibTableColumn
alaDaUNPValidityPeriodDays = _AlaDaUNPValidityPeriodDays_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 2),
    _AlaDaUNPValidityPeriodDays_Type()
)
alaDaUNPValidityPeriodDays.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodDays.setStatus("current")


class _AlaDaUNPValidityPeriodDaysStatus_Type(Integer32):
    """Custom type alaDaUNPValidityPeriodDaysStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPValidityPeriodDaysStatus_Type.__name__ = "Integer32"
_AlaDaUNPValidityPeriodDaysStatus_Object = MibTableColumn
alaDaUNPValidityPeriodDaysStatus = _AlaDaUNPValidityPeriodDaysStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 3),
    _AlaDaUNPValidityPeriodDaysStatus_Type()
)
alaDaUNPValidityPeriodDaysStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodDaysStatus.setStatus("current")
_AlaDaUNPValidityPeriodMonths_Type = Integer32
_AlaDaUNPValidityPeriodMonths_Object = MibTableColumn
alaDaUNPValidityPeriodMonths = _AlaDaUNPValidityPeriodMonths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 4),
    _AlaDaUNPValidityPeriodMonths_Type()
)
alaDaUNPValidityPeriodMonths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodMonths.setStatus("current")


class _AlaDaUNPValidityPeriodMonthsStatus_Type(Integer32):
    """Custom type alaDaUNPValidityPeriodMonthsStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPValidityPeriodMonthsStatus_Type.__name__ = "Integer32"
_AlaDaUNPValidityPeriodMonthsStatus_Object = MibTableColumn
alaDaUNPValidityPeriodMonthsStatus = _AlaDaUNPValidityPeriodMonthsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 5),
    _AlaDaUNPValidityPeriodMonthsStatus_Type()
)
alaDaUNPValidityPeriodMonthsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodMonthsStatus.setStatus("current")


class _AlaDaUNPValidityPeriodHour_Type(SnmpAdminString):
    """Custom type alaDaUNPValidityPeriodHour based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaDaUNPValidityPeriodHour_Type.__name__ = "SnmpAdminString"
_AlaDaUNPValidityPeriodHour_Object = MibTableColumn
alaDaUNPValidityPeriodHour = _AlaDaUNPValidityPeriodHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 6),
    _AlaDaUNPValidityPeriodHour_Type()
)
alaDaUNPValidityPeriodHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodHour.setStatus("current")


class _AlaDaUNPValidityPeriodHourStatus_Type(Integer32):
    """Custom type alaDaUNPValidityPeriodHourStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPValidityPeriodHourStatus_Type.__name__ = "Integer32"
_AlaDaUNPValidityPeriodHourStatus_Object = MibTableColumn
alaDaUNPValidityPeriodHourStatus = _AlaDaUNPValidityPeriodHourStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 7),
    _AlaDaUNPValidityPeriodHourStatus_Type()
)
alaDaUNPValidityPeriodHourStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodHourStatus.setStatus("current")


class _AlaDaUNPValidityPeriodEndHour_Type(SnmpAdminString):
    """Custom type alaDaUNPValidityPeriodEndHour based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaDaUNPValidityPeriodEndHour_Type.__name__ = "SnmpAdminString"
_AlaDaUNPValidityPeriodEndHour_Object = MibTableColumn
alaDaUNPValidityPeriodEndHour = _AlaDaUNPValidityPeriodEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 8),
    _AlaDaUNPValidityPeriodEndHour_Type()
)
alaDaUNPValidityPeriodEndHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodEndHour.setStatus("current")


class _AlaDaUNPValidityPeriodInterval_Type(SnmpAdminString):
    """Custom type alaDaUNPValidityPeriodInterval based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaDaUNPValidityPeriodInterval_Type.__name__ = "SnmpAdminString"
_AlaDaUNPValidityPeriodInterval_Object = MibTableColumn
alaDaUNPValidityPeriodInterval = _AlaDaUNPValidityPeriodInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 9),
    _AlaDaUNPValidityPeriodInterval_Type()
)
alaDaUNPValidityPeriodInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodInterval.setStatus("current")


class _AlaDaUNPValidityPeriodIntervalStatus_Type(Integer32):
    """Custom type alaDaUNPValidityPeriodIntervalStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPValidityPeriodIntervalStatus_Type.__name__ = "Integer32"
_AlaDaUNPValidityPeriodIntervalStatus_Object = MibTableColumn
alaDaUNPValidityPeriodIntervalStatus = _AlaDaUNPValidityPeriodIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 10),
    _AlaDaUNPValidityPeriodIntervalStatus_Type()
)
alaDaUNPValidityPeriodIntervalStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodIntervalStatus.setStatus("current")


class _AlaDaUNPValidityPeriodEndInterval_Type(SnmpAdminString):
    """Custom type alaDaUNPValidityPeriodEndInterval based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaDaUNPValidityPeriodEndInterval_Type.__name__ = "SnmpAdminString"
_AlaDaUNPValidityPeriodEndInterval_Object = MibTableColumn
alaDaUNPValidityPeriodEndInterval = _AlaDaUNPValidityPeriodEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 11),
    _AlaDaUNPValidityPeriodEndInterval_Type()
)
alaDaUNPValidityPeriodEndInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodEndInterval.setStatus("current")


class _AlaDaUNPValidityPeriodTimezone_Type(Integer32):
    """Custom type alaDaUNPValidityPeriodTimezone based on Integer32"""
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
              39)
        )
    )
    namedValues = NamedValues(
        *(("nzst", 1),
          ("zp11", 2),
          ("aest", 3),
          ("gst", 4),
          ("acst", 5),
          ("kst", 6),
          ("jst", 7),
          ("awst", 8),
          ("zp8", 9),
          ("zp7", 10),
          ("zp6", 11),
          ("ist", 12),
          ("zp5", 13),
          ("zp4", 14),
          ("msk", 15),
          ("eet", 16),
          ("cet", 17),
          ("met", 18),
          ("bst", 19),
          ("wat", 20),
          ("utc", 21),
          ("gmt", 22),
          ("wet", 23),
          ("zm2", 24),
          ("zm3", 25),
          ("nst", 26),
          ("ast", 27),
          ("astcam", 28),
          ("est", 29),
          ("estcam", 30),
          ("cst", 31),
          ("cstcam", 32),
          ("mst", 33),
          ("mstcam", 34),
          ("pst", 35),
          ("pstcam", 36),
          ("akst", 37),
          ("hst", 38),
          ("zm11", 39))
    )


_AlaDaUNPValidityPeriodTimezone_Type.__name__ = "Integer32"
_AlaDaUNPValidityPeriodTimezone_Object = MibTableColumn
alaDaUNPValidityPeriodTimezone = _AlaDaUNPValidityPeriodTimezone_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 12),
    _AlaDaUNPValidityPeriodTimezone_Type()
)
alaDaUNPValidityPeriodTimezone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodTimezone.setStatus("current")


class _AlaDaUNPValidityPeriodTimezoneStatus_Type(Integer32):
    """Custom type alaDaUNPValidityPeriodTimezoneStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPValidityPeriodTimezoneStatus_Type.__name__ = "Integer32"
_AlaDaUNPValidityPeriodTimezoneStatus_Object = MibTableColumn
alaDaUNPValidityPeriodTimezoneStatus = _AlaDaUNPValidityPeriodTimezoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 13),
    _AlaDaUNPValidityPeriodTimezoneStatus_Type()
)
alaDaUNPValidityPeriodTimezoneStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodTimezoneStatus.setStatus("current")


class _AlaDaUNPValidityPeriodActiveStatus_Type(Integer32):
    """Custom type alaDaUNPValidityPeriodActiveStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlaDaUNPValidityPeriodActiveStatus_Type.__name__ = "Integer32"
_AlaDaUNPValidityPeriodActiveStatus_Object = MibTableColumn
alaDaUNPValidityPeriodActiveStatus = _AlaDaUNPValidityPeriodActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 14),
    _AlaDaUNPValidityPeriodActiveStatus_Type()
)
alaDaUNPValidityPeriodActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodActiveStatus.setStatus("current")
_AlaDaUNPValidityPeriodRowStatus_Type = RowStatus
_AlaDaUNPValidityPeriodRowStatus_Object = MibTableColumn
alaDaUNPValidityPeriodRowStatus = _AlaDaUNPValidityPeriodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 44, 1, 15),
    _AlaDaUNPValidityPeriodRowStatus_Type()
)
alaDaUNPValidityPeriodRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodRowStatus.setStatus("current")
_AlaDaUNPLocationPolicyTable_Object = MibTable
alaDaUNPLocationPolicyTable = _AlaDaUNPLocationPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45)
)
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicyTable.setStatus("current")
_AlaDaUNPLocationPolicyEntry_Object = MibTableRow
alaDaUNPLocationPolicyEntry = _AlaDaUNPLocationPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45, 1)
)
alaDaUNPLocationPolicyEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPLocationPolicyName"),
)
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicyEntry.setStatus("current")


class _AlaDaUNPLocationPolicyName_Type(SnmpAdminString):
    """Custom type alaDaUNPLocationPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPLocationPolicyName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPLocationPolicyName_Object = MibTableColumn
alaDaUNPLocationPolicyName = _AlaDaUNPLocationPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45, 1, 1),
    _AlaDaUNPLocationPolicyName_Type()
)
alaDaUNPLocationPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicyName.setStatus("current")
_AlaDaUNPLocationPolicyPort_Type = InterfaceIndex
_AlaDaUNPLocationPolicyPort_Object = MibTableColumn
alaDaUNPLocationPolicyPort = _AlaDaUNPLocationPolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45, 1, 2),
    _AlaDaUNPLocationPolicyPort_Type()
)
alaDaUNPLocationPolicyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicyPort.setStatus("current")
_AlaDaUNPLocationPolicyPortHigh_Type = InterfaceIndex
_AlaDaUNPLocationPolicyPortHigh_Object = MibTableColumn
alaDaUNPLocationPolicyPortHigh = _AlaDaUNPLocationPolicyPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45, 1, 3),
    _AlaDaUNPLocationPolicyPortHigh_Type()
)
alaDaUNPLocationPolicyPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicyPortHigh.setStatus("current")


class _AlaDaUNPLocationPolicyPortStatus_Type(Integer32):
    """Custom type alaDaUNPLocationPolicyPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPLocationPolicyPortStatus_Type.__name__ = "Integer32"
_AlaDaUNPLocationPolicyPortStatus_Object = MibTableColumn
alaDaUNPLocationPolicyPortStatus = _AlaDaUNPLocationPolicyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45, 1, 4),
    _AlaDaUNPLocationPolicyPortStatus_Type()
)
alaDaUNPLocationPolicyPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicyPortStatus.setStatus("current")


class _AlaDaUNPLocationPolicySystemName_Type(SnmpAdminString):
    """Custom type alaDaUNPLocationPolicySystemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlaDaUNPLocationPolicySystemName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPLocationPolicySystemName_Object = MibTableColumn
alaDaUNPLocationPolicySystemName = _AlaDaUNPLocationPolicySystemName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45, 1, 5),
    _AlaDaUNPLocationPolicySystemName_Type()
)
alaDaUNPLocationPolicySystemName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicySystemName.setStatus("current")


class _AlaDaUNPLocationPolicySystemLocation_Type(SnmpAdminString):
    """Custom type alaDaUNPLocationPolicySystemLocation based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaDaUNPLocationPolicySystemLocation_Type.__name__ = "SnmpAdminString"
_AlaDaUNPLocationPolicySystemLocation_Object = MibTableColumn
alaDaUNPLocationPolicySystemLocation = _AlaDaUNPLocationPolicySystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45, 1, 6),
    _AlaDaUNPLocationPolicySystemLocation_Type()
)
alaDaUNPLocationPolicySystemLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicySystemLocation.setStatus("current")
_AlaDaUNPLocationPolicyRowStatus_Type = RowStatus
_AlaDaUNPLocationPolicyRowStatus_Object = MibTableColumn
alaDaUNPLocationPolicyRowStatus = _AlaDaUNPLocationPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45, 1, 7),
    _AlaDaUNPLocationPolicyRowStatus_Type()
)
alaDaUNPLocationPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicyRowStatus.setStatus("current")


class _AlaDaUNPLocationPolicyDomainId_Type(Integer32):
    """Custom type alaDaUNPLocationPolicyDomainId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 511),
    )


_AlaDaUNPLocationPolicyDomainId_Type.__name__ = "Integer32"
_AlaDaUNPLocationPolicyDomainId_Object = MibTableColumn
alaDaUNPLocationPolicyDomainId = _AlaDaUNPLocationPolicyDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 45, 1, 8),
    _AlaDaUNPLocationPolicyDomainId_Type()
)
alaDaUNPLocationPolicyDomainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicyDomainId.setStatus("current")
_AlaDaUNPRedirectAllowedServerTable_Object = MibTable
alaDaUNPRedirectAllowedServerTable = _AlaDaUNPRedirectAllowedServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 46)
)
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedServerTable.setStatus("current")
_AlaDaUNPRedirectAllowedServerEntry_Object = MibTableRow
alaDaUNPRedirectAllowedServerEntry = _AlaDaUNPRedirectAllowedServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 46, 1)
)
alaDaUNPRedirectAllowedServerEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedServerName"),
)
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedServerEntry.setStatus("current")


class _AlaDaUNPRedirectAllowedServerName_Type(SnmpAdminString):
    """Custom type alaDaUNPRedirectAllowedServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPRedirectAllowedServerName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRedirectAllowedServerName_Object = MibTableColumn
alaDaUNPRedirectAllowedServerName = _AlaDaUNPRedirectAllowedServerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 46, 1, 1),
    _AlaDaUNPRedirectAllowedServerName_Type()
)
alaDaUNPRedirectAllowedServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedServerName.setStatus("current")
_AlaDaUNPRedirectAllowedServerIPType_Type = InetAddressType
_AlaDaUNPRedirectAllowedServerIPType_Object = MibTableColumn
alaDaUNPRedirectAllowedServerIPType = _AlaDaUNPRedirectAllowedServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 46, 1, 2),
    _AlaDaUNPRedirectAllowedServerIPType_Type()
)
alaDaUNPRedirectAllowedServerIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedServerIPType.setStatus("current")
_AlaDaUNPRedirectAllowedServerIP_Type = InetAddress
_AlaDaUNPRedirectAllowedServerIP_Object = MibTableColumn
alaDaUNPRedirectAllowedServerIP = _AlaDaUNPRedirectAllowedServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 46, 1, 3),
    _AlaDaUNPRedirectAllowedServerIP_Type()
)
alaDaUNPRedirectAllowedServerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedServerIP.setStatus("current")
_AlaDaUNPRedirectAllowedMaskIPType_Type = InetAddressType
_AlaDaUNPRedirectAllowedMaskIPType_Object = MibTableColumn
alaDaUNPRedirectAllowedMaskIPType = _AlaDaUNPRedirectAllowedMaskIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 46, 1, 4),
    _AlaDaUNPRedirectAllowedMaskIPType_Type()
)
alaDaUNPRedirectAllowedMaskIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedMaskIPType.setStatus("current")
_AlaDaUNPRedirectAllowedMaskIP_Type = InetAddress
_AlaDaUNPRedirectAllowedMaskIP_Object = MibTableColumn
alaDaUNPRedirectAllowedMaskIP = _AlaDaUNPRedirectAllowedMaskIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 46, 1, 5),
    _AlaDaUNPRedirectAllowedMaskIP_Type()
)
alaDaUNPRedirectAllowedMaskIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedMaskIP.setStatus("current")
_AlaDaUNPRedirectAllowedRowStatus_Type = RowStatus
_AlaDaUNPRedirectAllowedRowStatus_Object = MibTableColumn
alaDaUNPRedirectAllowedRowStatus = _AlaDaUNPRedirectAllowedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 46, 1, 6),
    _AlaDaUNPRedirectAllowedRowStatus_Type()
)
alaDaUNPRedirectAllowedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedRowStatus.setStatus("current")
_AlaDaMacVlanUserExtTable_Object = MibTable
alaDaMacVlanUserExtTable = _AlaDaMacVlanUserExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 47)
)
if mibBuilder.loadTexts:
    alaDaMacVlanUserExtTable.setStatus("current")
_AlaDaMacVlanUserExtEntry_Object = MibTableRow
alaDaMacVlanUserExtEntry = _AlaDaMacVlanUserExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 47, 1)
)
alaDaMacVlanUserExtEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserExtIntfNum"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserExtMACAddress"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserExtVlanID"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserExtAppID"),
)
if mibBuilder.loadTexts:
    alaDaMacVlanUserExtEntry.setStatus("current")
_AlaDaMacVlanUserExtIntfNum_Type = InterfaceIndex
_AlaDaMacVlanUserExtIntfNum_Object = MibTableColumn
alaDaMacVlanUserExtIntfNum = _AlaDaMacVlanUserExtIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 47, 1, 1),
    _AlaDaMacVlanUserExtIntfNum_Type()
)
alaDaMacVlanUserExtIntfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserExtIntfNum.setStatus("current")
_AlaDaMacVlanUserExtMACAddress_Type = MacAddress
_AlaDaMacVlanUserExtMACAddress_Object = MibTableColumn
alaDaMacVlanUserExtMACAddress = _AlaDaMacVlanUserExtMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 47, 1, 2),
    _AlaDaMacVlanUserExtMACAddress_Type()
)
alaDaMacVlanUserExtMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserExtMACAddress.setStatus("current")


class _AlaDaMacVlanUserExtVlanID_Type(Integer32):
    """Custom type alaDaMacVlanUserExtVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDaMacVlanUserExtVlanID_Type.__name__ = "Integer32"
_AlaDaMacVlanUserExtVlanID_Object = MibTableColumn
alaDaMacVlanUserExtVlanID = _AlaDaMacVlanUserExtVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 47, 1, 3),
    _AlaDaMacVlanUserExtVlanID_Type()
)
alaDaMacVlanUserExtVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserExtVlanID.setStatus("current")


class _AlaDaMacVlanUserExtAppID_Type(Unsigned32):
    """Custom type alaDaMacVlanUserExtAppID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AlaDaMacVlanUserExtAppID_Type.__name__ = "Unsigned32"
_AlaDaMacVlanUserExtAppID_Object = MibTableColumn
alaDaMacVlanUserExtAppID = _AlaDaMacVlanUserExtAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 47, 1, 4),
    _AlaDaMacVlanUserExtAppID_Type()
)
alaDaMacVlanUserExtAppID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserExtAppID.setStatus("current")
_AlaDaMacVlanUserExtAppName_Type = SnmpAdminString
_AlaDaMacVlanUserExtAppName_Object = MibTableColumn
alaDaMacVlanUserExtAppName = _AlaDaMacVlanUserExtAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 47, 1, 5),
    _AlaDaMacVlanUserExtAppName_Type()
)
alaDaMacVlanUserExtAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserExtAppName.setStatus("current")
_AlaDaUNPVxlanProfileTable_Object = MibTable
alaDaUNPVxlanProfileTable = _AlaDaUNPVxlanProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48)
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileTable.setStatus("obsolete")
_AlaDaUNPVxlanProfileEntry_Object = MibTableRow
alaDaUNPVxlanProfileEntry = _AlaDaUNPVxlanProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1)
)
alaDaUNPVxlanProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileEntry.setStatus("obsolete")


class _AlaDaUNPVxlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPVxlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPVxlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVxlanProfileName_Object = MibTableColumn
alaDaUNPVxlanProfileName = _AlaDaUNPVxlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 1),
    _AlaDaUNPVxlanProfileName_Type()
)
alaDaUNPVxlanProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileName.setStatus("obsolete")
_AlaDaUNPVxlanProfileEncapVal_Type = TmnxEncapVal
_AlaDaUNPVxlanProfileEncapVal_Object = MibTableColumn
alaDaUNPVxlanProfileEncapVal = _AlaDaUNPVxlanProfileEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 2),
    _AlaDaUNPVxlanProfileEncapVal_Type()
)
alaDaUNPVxlanProfileEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileEncapVal.setStatus("obsolete")


class _AlaDaUNPVxlanProfileVnid_Type(Unsigned32):
    """Custom type alaDaUNPVxlanProfileVnid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_AlaDaUNPVxlanProfileVnid_Type.__name__ = "Unsigned32"
_AlaDaUNPVxlanProfileVnid_Object = MibTableColumn
alaDaUNPVxlanProfileVnid = _AlaDaUNPVxlanProfileVnid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 3),
    _AlaDaUNPVxlanProfileVnid_Type()
)
alaDaUNPVxlanProfileVnid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileVnid.setStatus("obsolete")


class _AlaDaUNPVxlanProfileQosPolicyListName_Type(SnmpAdminString):
    """Custom type alaDaUNPVxlanProfileQosPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPVxlanProfileQosPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVxlanProfileQosPolicyListName_Object = MibTableColumn
alaDaUNPVxlanProfileQosPolicyListName = _AlaDaUNPVxlanProfileQosPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 4),
    _AlaDaUNPVxlanProfileQosPolicyListName_Type()
)
alaDaUNPVxlanProfileQosPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileQosPolicyListName.setStatus("obsolete")


class _AlaDaUNPVxlanProfileFarEndIPListName_Type(SnmpAdminString):
    """Custom type alaDaUNPVxlanProfileFarEndIPListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPVxlanProfileFarEndIPListName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVxlanProfileFarEndIPListName_Object = MibTableColumn
alaDaUNPVxlanProfileFarEndIPListName = _AlaDaUNPVxlanProfileFarEndIPListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 5),
    _AlaDaUNPVxlanProfileFarEndIPListName_Type()
)
alaDaUNPVxlanProfileFarEndIPListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileFarEndIPListName.setStatus("obsolete")
_AlaDaUNPVxlanProfileMulticastIPAddressType_Type = InetAddressType
_AlaDaUNPVxlanProfileMulticastIPAddressType_Object = MibTableColumn
alaDaUNPVxlanProfileMulticastIPAddressType = _AlaDaUNPVxlanProfileMulticastIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 6),
    _AlaDaUNPVxlanProfileMulticastIPAddressType_Type()
)
alaDaUNPVxlanProfileMulticastIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileMulticastIPAddressType.setStatus("obsolete")
_AlaDaUNPVxlanProfileMulticastIPAddress_Type = InetAddress
_AlaDaUNPVxlanProfileMulticastIPAddress_Object = MibTableColumn
alaDaUNPVxlanProfileMulticastIPAddress = _AlaDaUNPVxlanProfileMulticastIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 7),
    _AlaDaUNPVxlanProfileMulticastIPAddress_Type()
)
alaDaUNPVxlanProfileMulticastIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileMulticastIPAddress.setStatus("obsolete")


class _AlaDaUNPVxlanProfileSapVlanXlation_Type(Integer32):
    """Custom type alaDaUNPVxlanProfileSapVlanXlation based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPVxlanProfileSapVlanXlation_Type.__name__ = "Integer32"
_AlaDaUNPVxlanProfileSapVlanXlation_Object = MibTableColumn
alaDaUNPVxlanProfileSapVlanXlation = _AlaDaUNPVxlanProfileSapVlanXlation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 8),
    _AlaDaUNPVxlanProfileSapVlanXlation_Type()
)
alaDaUNPVxlanProfileSapVlanXlation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileSapVlanXlation.setStatus("obsolete")


class _AlaDaUNPVxlanProfileMobileTagStatus_Type(Integer32):
    """Custom type alaDaUNPVxlanProfileMobileTagStatus based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPVxlanProfileMobileTagStatus_Type.__name__ = "Integer32"
_AlaDaUNPVxlanProfileMobileTagStatus_Object = MibTableColumn
alaDaUNPVxlanProfileMobileTagStatus = _AlaDaUNPVxlanProfileMobileTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 9),
    _AlaDaUNPVxlanProfileMobileTagStatus_Type()
)
alaDaUNPVxlanProfileMobileTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileMobileTagStatus.setStatus("obsolete")


class _AlaDaUNPVxlanProfileMulticastMode_Type(Integer32):
    """Custom type alaDaUNPVxlanProfileMulticastMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("headend", 1),
          ("tandem", 2),
          ("hybrid", 3))
    )


_AlaDaUNPVxlanProfileMulticastMode_Type.__name__ = "Integer32"
_AlaDaUNPVxlanProfileMulticastMode_Object = MibTableColumn
alaDaUNPVxlanProfileMulticastMode = _AlaDaUNPVxlanProfileMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 10),
    _AlaDaUNPVxlanProfileMulticastMode_Type()
)
alaDaUNPVxlanProfileMulticastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileMulticastMode.setStatus("obsolete")
_AlaDaUNPVxlanProfileRowStatus_Type = RowStatus
_AlaDaUNPVxlanProfileRowStatus_Object = MibTableColumn
alaDaUNPVxlanProfileRowStatus = _AlaDaUNPVxlanProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 48, 1, 11),
    _AlaDaUNPVxlanProfileRowStatus_Type()
)
alaDaUNPVxlanProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileRowStatus.setStatus("obsolete")
_AlaDaUNPVxlanFlushTable_Object = MibTable
alaDaUNPVxlanFlushTable = _AlaDaUNPVxlanFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49)
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushTable.setStatus("obsolete")
_AlaDaUNPVxlanFlushEntry_Object = MibTableRow
alaDaUNPVxlanFlushEntry = _AlaDaUNPVxlanFlushEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49, 1)
)
alaDaUNPVxlanFlushEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFlushIndex"),
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushEntry.setStatus("obsolete")
_AlaDaUNPVxlanFlushIndex_Type = Unsigned32
_AlaDaUNPVxlanFlushIndex_Object = MibTableColumn
alaDaUNPVxlanFlushIndex = _AlaDaUNPVxlanFlushIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49, 1, 1),
    _AlaDaUNPVxlanFlushIndex_Type()
)
alaDaUNPVxlanFlushIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushIndex.setStatus("obsolete")


class _AlaDaUNPVxlanFlushComplete_Type(Integer32):
    """Custom type alaDaUNPVxlanFlushComplete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("all", 2))
    )


_AlaDaUNPVxlanFlushComplete_Type.__name__ = "Integer32"
_AlaDaUNPVxlanFlushComplete_Object = MibTableColumn
alaDaUNPVxlanFlushComplete = _AlaDaUNPVxlanFlushComplete_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49, 1, 2),
    _AlaDaUNPVxlanFlushComplete_Type()
)
alaDaUNPVxlanFlushComplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushComplete.setStatus("obsolete")


class _AlaDaUNPVxlanFlushAuthType_Type(Integer32):
    """Custom type alaDaUNPVxlanFlushAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("onex", 2),
          ("mac", 3))
    )


_AlaDaUNPVxlanFlushAuthType_Type.__name__ = "Integer32"
_AlaDaUNPVxlanFlushAuthType_Object = MibTableColumn
alaDaUNPVxlanFlushAuthType = _AlaDaUNPVxlanFlushAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49, 1, 3),
    _AlaDaUNPVxlanFlushAuthType_Type()
)
alaDaUNPVxlanFlushAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushAuthType.setStatus("obsolete")


class _AlaDaUNPVxlanFlushMacAddress_Type(MacAddress):
    """Custom type alaDaUNPVxlanFlushMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPVxlanFlushMacAddress_Type.__name__ = "MacAddress"
_AlaDaUNPVxlanFlushMacAddress_Object = MibTableColumn
alaDaUNPVxlanFlushMacAddress = _AlaDaUNPVxlanFlushMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49, 1, 4),
    _AlaDaUNPVxlanFlushMacAddress_Type()
)
alaDaUNPVxlanFlushMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushMacAddress.setStatus("obsolete")
_AlaDaUNPVxlanFlushSapIDIfIndex_Type = InterfaceIndex
_AlaDaUNPVxlanFlushSapIDIfIndex_Object = MibTableColumn
alaDaUNPVxlanFlushSapIDIfIndex = _AlaDaUNPVxlanFlushSapIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49, 1, 5),
    _AlaDaUNPVxlanFlushSapIDIfIndex_Type()
)
alaDaUNPVxlanFlushSapIDIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushSapIDIfIndex.setStatus("obsolete")
_AlaDaUNPVxlanFlushSapIDEncapVal_Type = TmnxEncapVal
_AlaDaUNPVxlanFlushSapIDEncapVal_Object = MibTableColumn
alaDaUNPVxlanFlushSapIDEncapVal = _AlaDaUNPVxlanFlushSapIDEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49, 1, 6),
    _AlaDaUNPVxlanFlushSapIDEncapVal_Type()
)
alaDaUNPVxlanFlushSapIDEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushSapIDEncapVal.setStatus("obsolete")
_AlaDaUNPVxlanFlushServiceID_Type = Unsigned32
_AlaDaUNPVxlanFlushServiceID_Object = MibTableColumn
alaDaUNPVxlanFlushServiceID = _AlaDaUNPVxlanFlushServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49, 1, 7),
    _AlaDaUNPVxlanFlushServiceID_Type()
)
alaDaUNPVxlanFlushServiceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushServiceID.setStatus("obsolete")


class _AlaDaUNPVxlanFlushVxlanProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPVxlanFlushVxlanProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPVxlanFlushVxlanProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVxlanFlushVxlanProfile_Object = MibTableColumn
alaDaUNPVxlanFlushVxlanProfile = _AlaDaUNPVxlanFlushVxlanProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 49, 1, 8),
    _AlaDaUNPVxlanFlushVxlanProfile_Type()
)
alaDaUNPVxlanFlushVxlanProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushVxlanProfile.setStatus("obsolete")
_AlaDaUNPVxlanFarEndIPListTable_Object = MibTable
alaDaUNPVxlanFarEndIPListTable = _AlaDaUNPVxlanFarEndIPListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 50)
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPListTable.setStatus("current")
_AlaDaUNPVxlanFarEndIPListEntry_Object = MibTableRow
alaDaUNPVxlanFarEndIPListEntry = _AlaDaUNPVxlanFarEndIPListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 50, 1)
)
alaDaUNPVxlanFarEndIPListEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFarEndIPListName"),
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPListEntry.setStatus("current")


class _AlaDaUNPVxlanFarEndIPListName_Type(SnmpAdminString):
    """Custom type alaDaUNPVxlanFarEndIPListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPVxlanFarEndIPListName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVxlanFarEndIPListName_Object = MibTableColumn
alaDaUNPVxlanFarEndIPListName = _AlaDaUNPVxlanFarEndIPListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 50, 1, 1),
    _AlaDaUNPVxlanFarEndIPListName_Type()
)
alaDaUNPVxlanFarEndIPListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPListName.setStatus("current")
_AlaDaUNPVxlanFarEndIPListIPAddressCount_Type = Unsigned32
_AlaDaUNPVxlanFarEndIPListIPAddressCount_Object = MibTableColumn
alaDaUNPVxlanFarEndIPListIPAddressCount = _AlaDaUNPVxlanFarEndIPListIPAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 50, 1, 2),
    _AlaDaUNPVxlanFarEndIPListIPAddressCount_Type()
)
alaDaUNPVxlanFarEndIPListIPAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPListIPAddressCount.setStatus("current")


class _AlaDaUNPVxlanFarEndIPListRemove_Type(Integer32):
    """Custom type alaDaUNPVxlanFarEndIPListRemove based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPVxlanFarEndIPListRemove_Type.__name__ = "Integer32"
_AlaDaUNPVxlanFarEndIPListRemove_Object = MibTableColumn
alaDaUNPVxlanFarEndIPListRemove = _AlaDaUNPVxlanFarEndIPListRemove_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 50, 1, 3),
    _AlaDaUNPVxlanFarEndIPListRemove_Type()
)
alaDaUNPVxlanFarEndIPListRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPListRemove.setStatus("current")
_AlaDaUNPVxlanFarEndIPAddressListTable_Object = MibTable
alaDaUNPVxlanFarEndIPAddressListTable = _AlaDaUNPVxlanFarEndIPAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 51)
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPAddressListTable.setStatus("current")
_AlaDaUNPVxlanFarEndIPAddressListEntry_Object = MibTableRow
alaDaUNPVxlanFarEndIPAddressListEntry = _AlaDaUNPVxlanFarEndIPAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 51, 1)
)
alaDaUNPVxlanFarEndIPAddressListEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFarEndIPListName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFarEndIPAddressListIPType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFarEndIPAddressListIP"),
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPAddressListEntry.setStatus("current")


class _AlaDaUNPVxlanFarEndIPAddressListIPType_Type(InetAddressType):
    """Custom type alaDaUNPVxlanFarEndIPAddressListIPType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaUNPVxlanFarEndIPAddressListIPType_Type.__name__ = "InetAddressType"
_AlaDaUNPVxlanFarEndIPAddressListIPType_Object = MibTableColumn
alaDaUNPVxlanFarEndIPAddressListIPType = _AlaDaUNPVxlanFarEndIPAddressListIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 51, 1, 1),
    _AlaDaUNPVxlanFarEndIPAddressListIPType_Type()
)
alaDaUNPVxlanFarEndIPAddressListIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPAddressListIPType.setStatus("current")


class _AlaDaUNPVxlanFarEndIPAddressListIP_Type(InetAddress):
    """Custom type alaDaUNPVxlanFarEndIPAddressListIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPVxlanFarEndIPAddressListIP_Type.__name__ = "InetAddress"
_AlaDaUNPVxlanFarEndIPAddressListIP_Object = MibTableColumn
alaDaUNPVxlanFarEndIPAddressListIP = _AlaDaUNPVxlanFarEndIPAddressListIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 51, 1, 2),
    _AlaDaUNPVxlanFarEndIPAddressListIP_Type()
)
alaDaUNPVxlanFarEndIPAddressListIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPAddressListIP.setStatus("current")
_AlaDaUNPVxlanFarEndIPAddressListRowStatus_Type = RowStatus
_AlaDaUNPVxlanFarEndIPAddressListRowStatus_Object = MibTableColumn
alaDaUNPVxlanFarEndIPAddressListRowStatus = _AlaDaUNPVxlanFarEndIPAddressListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 51, 1, 3),
    _AlaDaUNPVxlanFarEndIPAddressListRowStatus_Type()
)
alaDaUNPVxlanFarEndIPAddressListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPAddressListRowStatus.setStatus("current")
_AlaDaUNPSpbFlushTable_Object = MibTable
alaDaUNPSpbFlushTable = _AlaDaUNPSpbFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52)
)
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushTable.setStatus("obsolete")
_AlaDaUNPSpbFlushEntry_Object = MibTableRow
alaDaUNPSpbFlushEntry = _AlaDaUNPSpbFlushEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52, 1)
)
alaDaUNPSpbFlushEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPSpbFlushIndex"),
)
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushEntry.setStatus("obsolete")


class _AlaDaUNPSpbFlushIndex_Type(Integer32):
    """Custom type alaDaUNPSpbFlushIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaDaUNPSpbFlushIndex_Type.__name__ = "Integer32"
_AlaDaUNPSpbFlushIndex_Object = MibTableColumn
alaDaUNPSpbFlushIndex = _AlaDaUNPSpbFlushIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52, 1, 1),
    _AlaDaUNPSpbFlushIndex_Type()
)
alaDaUNPSpbFlushIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushIndex.setStatus("obsolete")


class _AlaDaUNPSpbFlushComplete_Type(Integer32):
    """Custom type alaDaUNPSpbFlushComplete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("all", 2))
    )


_AlaDaUNPSpbFlushComplete_Type.__name__ = "Integer32"
_AlaDaUNPSpbFlushComplete_Object = MibTableColumn
alaDaUNPSpbFlushComplete = _AlaDaUNPSpbFlushComplete_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52, 1, 2),
    _AlaDaUNPSpbFlushComplete_Type()
)
alaDaUNPSpbFlushComplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushComplete.setStatus("obsolete")


class _AlaDaUNPSpbFlushAuthType_Type(Integer32):
    """Custom type alaDaUNPSpbFlushAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("onex", 2),
          ("mac", 3))
    )


_AlaDaUNPSpbFlushAuthType_Type.__name__ = "Integer32"
_AlaDaUNPSpbFlushAuthType_Object = MibTableColumn
alaDaUNPSpbFlushAuthType = _AlaDaUNPSpbFlushAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52, 1, 3),
    _AlaDaUNPSpbFlushAuthType_Type()
)
alaDaUNPSpbFlushAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushAuthType.setStatus("obsolete")


class _AlaDaUNPSpbFlushMacAddress_Type(MacAddress):
    """Custom type alaDaUNPSpbFlushMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPSpbFlushMacAddress_Type.__name__ = "MacAddress"
_AlaDaUNPSpbFlushMacAddress_Object = MibTableColumn
alaDaUNPSpbFlushMacAddress = _AlaDaUNPSpbFlushMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52, 1, 4),
    _AlaDaUNPSpbFlushMacAddress_Type()
)
alaDaUNPSpbFlushMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushMacAddress.setStatus("obsolete")
_AlaDaUNPSpbFlushSapIDIfIndex_Type = InterfaceIndex
_AlaDaUNPSpbFlushSapIDIfIndex_Object = MibTableColumn
alaDaUNPSpbFlushSapIDIfIndex = _AlaDaUNPSpbFlushSapIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52, 1, 5),
    _AlaDaUNPSpbFlushSapIDIfIndex_Type()
)
alaDaUNPSpbFlushSapIDIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushSapIDIfIndex.setStatus("obsolete")
_AlaDaUNPSpbFlushSapIDEncapVal_Type = TmnxEncapVal
_AlaDaUNPSpbFlushSapIDEncapVal_Object = MibTableColumn
alaDaUNPSpbFlushSapIDEncapVal = _AlaDaUNPSpbFlushSapIDEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52, 1, 6),
    _AlaDaUNPSpbFlushSapIDEncapVal_Type()
)
alaDaUNPSpbFlushSapIDEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushSapIDEncapVal.setStatus("obsolete")
_AlaDaUNPSpbFlushServiceID_Type = Unsigned32
_AlaDaUNPSpbFlushServiceID_Object = MibTableColumn
alaDaUNPSpbFlushServiceID = _AlaDaUNPSpbFlushServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52, 1, 7),
    _AlaDaUNPSpbFlushServiceID_Type()
)
alaDaUNPSpbFlushServiceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushServiceID.setStatus("obsolete")


class _AlaDaUNPSpbFlushSpbProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPSpbFlushSpbProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPSpbFlushSpbProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPSpbFlushSpbProfile_Object = MibTableColumn
alaDaUNPSpbFlushSpbProfile = _AlaDaUNPSpbFlushSpbProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 52, 1, 8),
    _AlaDaUNPSpbFlushSpbProfile_Type()
)
alaDaUNPSpbFlushSpbProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushSpbProfile.setStatus("obsolete")
_AlaDaKerberosMIBObjects_ObjectIdentity = ObjectIdentity
alaDaKerberosMIBObjects = _AlaDaKerberosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53)
)
_AlaDaKerberosGlobalConfig_ObjectIdentity = ObjectIdentity
alaDaKerberosGlobalConfig = _AlaDaKerberosGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1)
)


class _AlaDaKerberosGlobalMacMoveStatus_Type(Integer32):
    """Custom type alaDaKerberosGlobalMacMoveStatus based on Integer32"""
    defaultValue = 1

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


_AlaDaKerberosGlobalMacMoveStatus_Type.__name__ = "Integer32"
_AlaDaKerberosGlobalMacMoveStatus_Object = MibScalar
alaDaKerberosGlobalMacMoveStatus = _AlaDaKerberosGlobalMacMoveStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 1),
    _AlaDaKerberosGlobalMacMoveStatus_Type()
)
alaDaKerberosGlobalMacMoveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaKerberosGlobalMacMoveStatus.setStatus("current")


class _AlaDaKerberosGlobalInactivityTimer_Type(Integer32):
    """Custom type alaDaKerberosGlobalInactivityTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_AlaDaKerberosGlobalInactivityTimer_Type.__name__ = "Integer32"
_AlaDaKerberosGlobalInactivityTimer_Object = MibScalar
alaDaKerberosGlobalInactivityTimer = _AlaDaKerberosGlobalInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 2),
    _AlaDaKerberosGlobalInactivityTimer_Type()
)
alaDaKerberosGlobalInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaKerberosGlobalInactivityTimer.setStatus("current")


class _AlaDaKerberosGlobalPolicy_Type(SnmpAdminString):
    """Custom type alaDaKerberosGlobalPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaDaKerberosGlobalPolicy_Type.__name__ = "SnmpAdminString"
_AlaDaKerberosGlobalPolicy_Object = MibScalar
alaDaKerberosGlobalPolicy = _AlaDaKerberosGlobalPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 3),
    _AlaDaKerberosGlobalPolicy_Type()
)
alaDaKerberosGlobalPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaKerberosGlobalPolicy.setStatus("current")


class _AlaDaKerberosGlobalPolicyStatus_Type(Integer32):
    """Custom type alaDaKerberosGlobalPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlaDaKerberosGlobalPolicyStatus_Type.__name__ = "Integer32"
_AlaDaKerberosGlobalPolicyStatus_Object = MibScalar
alaDaKerberosGlobalPolicyStatus = _AlaDaKerberosGlobalPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 4),
    _AlaDaKerberosGlobalPolicyStatus_Type()
)
alaDaKerberosGlobalPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosGlobalPolicyStatus.setStatus("current")
_AlaDaKerberosClientPktHwDiscardStats_Type = Counter32
_AlaDaKerberosClientPktHwDiscardStats_Object = MibScalar
alaDaKerberosClientPktHwDiscardStats = _AlaDaKerberosClientPktHwDiscardStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 5),
    _AlaDaKerberosClientPktHwDiscardStats_Type()
)
alaDaKerberosClientPktHwDiscardStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosClientPktHwDiscardStats.setStatus("deprecated")
_AlaDaKerberosServerPktHwDiscardStats_Type = Counter32
_AlaDaKerberosServerPktHwDiscardStats_Object = MibScalar
alaDaKerberosServerPktHwDiscardStats = _AlaDaKerberosServerPktHwDiscardStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 6),
    _AlaDaKerberosServerPktHwDiscardStats_Type()
)
alaDaKerberosServerPktHwDiscardStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosServerPktHwDiscardStats.setStatus("deprecated")
_AlaDaKerberosTotalClientPktRxStats_Type = Counter32
_AlaDaKerberosTotalClientPktRxStats_Object = MibScalar
alaDaKerberosTotalClientPktRxStats = _AlaDaKerberosTotalClientPktRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 7),
    _AlaDaKerberosTotalClientPktRxStats_Type()
)
alaDaKerberosTotalClientPktRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosTotalClientPktRxStats.setStatus("current")
_AlaDaKerberosTotalServerPktRxStats_Type = Counter32
_AlaDaKerberosTotalServerPktRxStats_Object = MibScalar
alaDaKerberosTotalServerPktRxStats = _AlaDaKerberosTotalServerPktRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 8),
    _AlaDaKerberosTotalServerPktRxStats_Type()
)
alaDaKerberosTotalServerPktRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosTotalServerPktRxStats.setStatus("current")
_AlaDaKerberosClientPktSwDiscardStats_Type = Counter32
_AlaDaKerberosClientPktSwDiscardStats_Object = MibScalar
alaDaKerberosClientPktSwDiscardStats = _AlaDaKerberosClientPktSwDiscardStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 9),
    _AlaDaKerberosClientPktSwDiscardStats_Type()
)
alaDaKerberosClientPktSwDiscardStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosClientPktSwDiscardStats.setStatus("deprecated")
_AlaDaKerberosServerPktSwDiscardStats_Type = Counter32
_AlaDaKerberosServerPktSwDiscardStats_Object = MibScalar
alaDaKerberosServerPktSwDiscardStats = _AlaDaKerberosServerPktSwDiscardStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 10),
    _AlaDaKerberosServerPktSwDiscardStats_Type()
)
alaDaKerberosServerPktSwDiscardStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosServerPktSwDiscardStats.setStatus("deprecated")
_AlaDaKerberosTotalASREQRxStats_Type = Counter32
_AlaDaKerberosTotalASREQRxStats_Object = MibScalar
alaDaKerberosTotalASREQRxStats = _AlaDaKerberosTotalASREQRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 11),
    _AlaDaKerberosTotalASREQRxStats_Type()
)
alaDaKerberosTotalASREQRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosTotalASREQRxStats.setStatus("current")
_AlaDaKerberosTotalASREPRxStats_Type = Counter32
_AlaDaKerberosTotalASREPRxStats_Object = MibScalar
alaDaKerberosTotalASREPRxStats = _AlaDaKerberosTotalASREPRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 12),
    _AlaDaKerberosTotalASREPRxStats_Type()
)
alaDaKerberosTotalASREPRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosTotalASREPRxStats.setStatus("current")
_AlaDaKerberosTotalTGSREQRxStats_Type = Counter32
_AlaDaKerberosTotalTGSREQRxStats_Object = MibScalar
alaDaKerberosTotalTGSREQRxStats = _AlaDaKerberosTotalTGSREQRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 13),
    _AlaDaKerberosTotalTGSREQRxStats_Type()
)
alaDaKerberosTotalTGSREQRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosTotalTGSREQRxStats.setStatus("current")
_AlaDaKerberosTotalTGSREPRxStats_Type = Counter32
_AlaDaKerberosTotalTGSREPRxStats_Object = MibScalar
alaDaKerberosTotalTGSREPRxStats = _AlaDaKerberosTotalTGSREPRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 14),
    _AlaDaKerberosTotalTGSREPRxStats_Type()
)
alaDaKerberosTotalTGSREPRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosTotalTGSREPRxStats.setStatus("current")
_AlaDaKerberosTotalErrorRxStats_Type = Counter32
_AlaDaKerberosTotalErrorRxStats_Object = MibScalar
alaDaKerberosTotalErrorRxStats = _AlaDaKerberosTotalErrorRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 15),
    _AlaDaKerberosTotalErrorRxStats_Type()
)
alaDaKerberosTotalErrorRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosTotalErrorRxStats.setStatus("current")


class _AlaDaKerberosGlobalClearStats_Type(Integer32):
    """Custom type alaDaKerberosGlobalClearStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaDaKerberosGlobalClearStats_Type.__name__ = "Integer32"
_AlaDaKerberosGlobalClearStats_Object = MibScalar
alaDaKerberosGlobalClearStats = _AlaDaKerberosGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 16),
    _AlaDaKerberosGlobalClearStats_Type()
)
alaDaKerberosGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaKerberosGlobalClearStats.setStatus("current")


class _AlaDaKerberosGlobalClearPortStats_Type(Integer32):
    """Custom type alaDaKerberosGlobalClearPortStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaDaKerberosGlobalClearPortStats_Type.__name__ = "Integer32"
_AlaDaKerberosGlobalClearPortStats_Object = MibScalar
alaDaKerberosGlobalClearPortStats = _AlaDaKerberosGlobalClearPortStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 17),
    _AlaDaKerberosGlobalClearPortStats_Type()
)
alaDaKerberosGlobalClearPortStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaKerberosGlobalClearPortStats.setStatus("current")


class _AlaDaKerberosGlobalServerTimeoutTimer_Type(Integer32):
    """Custom type alaDaKerberosGlobalServerTimeoutTimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AlaDaKerberosGlobalServerTimeoutTimer_Type.__name__ = "Integer32"
_AlaDaKerberosGlobalServerTimeoutTimer_Object = MibScalar
alaDaKerberosGlobalServerTimeoutTimer = _AlaDaKerberosGlobalServerTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 1, 18),
    _AlaDaKerberosGlobalServerTimeoutTimer_Type()
)
alaDaKerberosGlobalServerTimeoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaKerberosGlobalServerTimeoutTimer.setStatus("current")
_AlaDaKerberosPolicyConfigTable_Object = MibTable
alaDaKerberosPolicyConfigTable = _AlaDaKerberosPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 2)
)
if mibBuilder.loadTexts:
    alaDaKerberosPolicyConfigTable.setStatus("current")
_AlaDaKerberosPolicyConfigEntry_Object = MibTableRow
alaDaKerberosPolicyConfigEntry = _AlaDaKerberosPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 2, 1)
)
alaDaKerberosPolicyConfigEntry.setIndexNames(
    (1, "ALCATEL-IND1-DA-MIB", "alaDaKerberosPolicyDomainName"),
)
if mibBuilder.loadTexts:
    alaDaKerberosPolicyConfigEntry.setStatus("current")


class _AlaDaKerberosPolicyDomainName_Type(SnmpAdminString):
    """Custom type alaDaKerberosPolicyDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaKerberosPolicyDomainName_Type.__name__ = "SnmpAdminString"
_AlaDaKerberosPolicyDomainName_Object = MibTableColumn
alaDaKerberosPolicyDomainName = _AlaDaKerberosPolicyDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 2, 1, 1),
    _AlaDaKerberosPolicyDomainName_Type()
)
alaDaKerberosPolicyDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaKerberosPolicyDomainName.setStatus("current")


class _AlaDaKerberosPolicyName_Type(SnmpAdminString):
    """Custom type alaDaKerberosPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaDaKerberosPolicyName_Type.__name__ = "SnmpAdminString"
_AlaDaKerberosPolicyName_Object = MibTableColumn
alaDaKerberosPolicyName = _AlaDaKerberosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 2, 1, 2),
    _AlaDaKerberosPolicyName_Type()
)
alaDaKerberosPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaKerberosPolicyName.setStatus("current")


class _AlaDaKerberosPolicyStatus_Type(Integer32):
    """Custom type alaDaKerberosPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlaDaKerberosPolicyStatus_Type.__name__ = "Integer32"
_AlaDaKerberosPolicyStatus_Object = MibTableColumn
alaDaKerberosPolicyStatus = _AlaDaKerberosPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 2, 1, 3),
    _AlaDaKerberosPolicyStatus_Type()
)
alaDaKerberosPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPolicyStatus.setStatus("current")
_AlaDaKerberosPolicyRowStatus_Type = RowStatus
_AlaDaKerberosPolicyRowStatus_Object = MibTableColumn
alaDaKerberosPolicyRowStatus = _AlaDaKerberosPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 2, 1, 4),
    _AlaDaKerberosPolicyRowStatus_Type()
)
alaDaKerberosPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaKerberosPolicyRowStatus.setStatus("current")
_AlaDaKerberosUserTable_Object = MibTable
alaDaKerberosUserTable = _AlaDaKerberosUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3)
)
if mibBuilder.loadTexts:
    alaDaKerberosUserTable.setStatus("current")
_AlaDaKerberosUserEntry_Object = MibTableRow
alaDaKerberosUserEntry = _AlaDaKerberosUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3, 1)
)
alaDaKerberosUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaKerberosUserMac"),
)
if mibBuilder.loadTexts:
    alaDaKerberosUserEntry.setStatus("current")
_AlaDaKerberosUserMac_Type = MacAddress
_AlaDaKerberosUserMac_Object = MibTableColumn
alaDaKerberosUserMac = _AlaDaKerberosUserMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3, 1, 1),
    _AlaDaKerberosUserMac_Type()
)
alaDaKerberosUserMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaKerberosUserMac.setStatus("current")
_AlaDaKerberosUserPort_Type = InterfaceIndex
_AlaDaKerberosUserPort_Object = MibTableColumn
alaDaKerberosUserPort = _AlaDaKerberosUserPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3, 1, 2),
    _AlaDaKerberosUserPort_Type()
)
alaDaKerberosUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosUserPort.setStatus("current")


class _AlaDaKerberosUserName_Type(SnmpAdminString):
    """Custom type alaDaKerberosUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaKerberosUserName_Type.__name__ = "SnmpAdminString"
_AlaDaKerberosUserName_Object = MibTableColumn
alaDaKerberosUserName = _AlaDaKerberosUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3, 1, 3),
    _AlaDaKerberosUserName_Type()
)
alaDaKerberosUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosUserName.setStatus("current")


class _AlaDaKerberosUserDomain_Type(SnmpAdminString):
    """Custom type alaDaKerberosUserDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaKerberosUserDomain_Type.__name__ = "SnmpAdminString"
_AlaDaKerberosUserDomain_Object = MibTableColumn
alaDaKerberosUserDomain = _AlaDaKerberosUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3, 1, 4),
    _AlaDaKerberosUserDomain_Type()
)
alaDaKerberosUserDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosUserDomain.setStatus("current")


class _AlaDaKerberosUserAuthState_Type(Integer32):
    """Custom type alaDaKerberosUserAuthState based on Integer32"""
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
        *(("asAuthenticating", 1),
          ("asAuthenticated", 2),
          ("asFailed", 3),
          ("asTimeout", 4),
          ("tgsAuthenticating", 5),
          ("tgsAuthenticated", 6),
          ("tgsFailed", 7),
          ("tgsTimeout", 8))
    )


_AlaDaKerberosUserAuthState_Type.__name__ = "Integer32"
_AlaDaKerberosUserAuthState_Object = MibTableColumn
alaDaKerberosUserAuthState = _AlaDaKerberosUserAuthState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3, 1, 5),
    _AlaDaKerberosUserAuthState_Type()
)
alaDaKerberosUserAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosUserAuthState.setStatus("current")


class _AlaDaKerberosUserPolicy_Type(SnmpAdminString):
    """Custom type alaDaKerberosUserPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaKerberosUserPolicy_Type.__name__ = "SnmpAdminString"
_AlaDaKerberosUserPolicy_Object = MibTableColumn
alaDaKerberosUserPolicy = _AlaDaKerberosUserPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3, 1, 6),
    _AlaDaKerberosUserPolicy_Type()
)
alaDaKerberosUserPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosUserPolicy.setStatus("current")
_AlaDaKerberosUserLeftTime_Type = Integer32
_AlaDaKerberosUserLeftTime_Object = MibTableColumn
alaDaKerberosUserLeftTime = _AlaDaKerberosUserLeftTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3, 1, 7),
    _AlaDaKerberosUserLeftTime_Type()
)
alaDaKerberosUserLeftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosUserLeftTime.setStatus("current")


class _AlaDaKerberosUserState_Type(Integer32):
    """Custom type alaDaKerberosUserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("active", 2))
    )


_AlaDaKerberosUserState_Type.__name__ = "Integer32"
_AlaDaKerberosUserState_Object = MibTableColumn
alaDaKerberosUserState = _AlaDaKerberosUserState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 3, 1, 8),
    _AlaDaKerberosUserState_Type()
)
alaDaKerberosUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosUserState.setStatus("current")
_AlaDaKerberosPortStatsTable_Object = MibTable
alaDaKerberosPortStatsTable = _AlaDaKerberosPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4)
)
if mibBuilder.loadTexts:
    alaDaKerberosPortStatsTable.setStatus("deprecated")
_AlaDaKerberosPortStatsEntry_Object = MibTableRow
alaDaKerberosPortStatsEntry = _AlaDaKerberosPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1)
)
alaDaKerberosPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaKerberosStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaDaKerberosPortStatsEntry.setStatus("deprecated")
_AlaDaKerberosStatsIfIndex_Type = InterfaceIndex
_AlaDaKerberosStatsIfIndex_Object = MibTableColumn
alaDaKerberosStatsIfIndex = _AlaDaKerberosStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 1),
    _AlaDaKerberosStatsIfIndex_Type()
)
alaDaKerberosStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaKerberosStatsIfIndex.setStatus("deprecated")


class _AlaDaKerberosPortClearStats_Type(Integer32):
    """Custom type alaDaKerberosPortClearStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaDaKerberosPortClearStats_Type.__name__ = "Integer32"
_AlaDaKerberosPortClearStats_Object = MibTableColumn
alaDaKerberosPortClearStats = _AlaDaKerberosPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 2),
    _AlaDaKerberosPortClearStats_Type()
)
alaDaKerberosPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaKerberosPortClearStats.setStatus("deprecated")
_AlaDaKerberosPortClientPktRxStats_Type = Counter32
_AlaDaKerberosPortClientPktRxStats_Object = MibTableColumn
alaDaKerberosPortClientPktRxStats = _AlaDaKerberosPortClientPktRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 3),
    _AlaDaKerberosPortClientPktRxStats_Type()
)
alaDaKerberosPortClientPktRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPortClientPktRxStats.setStatus("deprecated")
_AlaDaKerberosPortServerPktRxStats_Type = Counter32
_AlaDaKerberosPortServerPktRxStats_Object = MibTableColumn
alaDaKerberosPortServerPktRxStats = _AlaDaKerberosPortServerPktRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 4),
    _AlaDaKerberosPortServerPktRxStats_Type()
)
alaDaKerberosPortServerPktRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPortServerPktRxStats.setStatus("deprecated")
_AlaDaKerberosPortClientPktSwDiscardStats_Type = Counter32
_AlaDaKerberosPortClientPktSwDiscardStats_Object = MibTableColumn
alaDaKerberosPortClientPktSwDiscardStats = _AlaDaKerberosPortClientPktSwDiscardStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 5),
    _AlaDaKerberosPortClientPktSwDiscardStats_Type()
)
alaDaKerberosPortClientPktSwDiscardStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPortClientPktSwDiscardStats.setStatus("deprecated")
_AlaDaKerberosPortServerPktSwDiscardStats_Type = Counter32
_AlaDaKerberosPortServerPktSwDiscardStats_Object = MibTableColumn
alaDaKerberosPortServerPktSwDiscardStats = _AlaDaKerberosPortServerPktSwDiscardStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 6),
    _AlaDaKerberosPortServerPktSwDiscardStats_Type()
)
alaDaKerberosPortServerPktSwDiscardStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPortServerPktSwDiscardStats.setStatus("deprecated")
_AlaDaKerberosPortASREQRxStats_Type = Counter32
_AlaDaKerberosPortASREQRxStats_Object = MibTableColumn
alaDaKerberosPortASREQRxStats = _AlaDaKerberosPortASREQRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 7),
    _AlaDaKerberosPortASREQRxStats_Type()
)
alaDaKerberosPortASREQRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPortASREQRxStats.setStatus("deprecated")
_AlaDaKerberosPortASREPRxStats_Type = Counter32
_AlaDaKerberosPortASREPRxStats_Object = MibTableColumn
alaDaKerberosPortASREPRxStats = _AlaDaKerberosPortASREPRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 8),
    _AlaDaKerberosPortASREPRxStats_Type()
)
alaDaKerberosPortASREPRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPortASREPRxStats.setStatus("deprecated")
_AlaDaKerberosPortTGSREQRxStats_Type = Counter32
_AlaDaKerberosPortTGSREQRxStats_Object = MibTableColumn
alaDaKerberosPortTGSREQRxStats = _AlaDaKerberosPortTGSREQRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 9),
    _AlaDaKerberosPortTGSREQRxStats_Type()
)
alaDaKerberosPortTGSREQRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPortTGSREQRxStats.setStatus("deprecated")
_AlaDaKerberosPortTGSREPRxStats_Type = Counter32
_AlaDaKerberosPortTGSREPRxStats_Object = MibTableColumn
alaDaKerberosPortTGSREPRxStats = _AlaDaKerberosPortTGSREPRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 10),
    _AlaDaKerberosPortTGSREPRxStats_Type()
)
alaDaKerberosPortTGSREPRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPortTGSREPRxStats.setStatus("deprecated")
_AlaDaKerberosPortErrorRxStats_Type = Counter32
_AlaDaKerberosPortErrorRxStats_Object = MibTableColumn
alaDaKerberosPortErrorRxStats = _AlaDaKerberosPortErrorRxStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 4, 1, 11),
    _AlaDaKerberosPortErrorRxStats_Type()
)
alaDaKerberosPortErrorRxStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaKerberosPortErrorRxStats.setStatus("deprecated")
_AlaDaKerberosServerTable_Object = MibTable
alaDaKerberosServerTable = _AlaDaKerberosServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 5)
)
if mibBuilder.loadTexts:
    alaDaKerberosServerTable.setStatus("current")
_AlaDaKerberosServerEntry_Object = MibTableRow
alaDaKerberosServerEntry = _AlaDaKerberosServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 5, 1)
)
alaDaKerberosServerEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaKerberosIpAddressType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaKerberosIpAddress"),
)
if mibBuilder.loadTexts:
    alaDaKerberosServerEntry.setStatus("current")
_AlaDaKerberosIpAddressType_Type = InetAddressType
_AlaDaKerberosIpAddressType_Object = MibTableColumn
alaDaKerberosIpAddressType = _AlaDaKerberosIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 5, 1, 1),
    _AlaDaKerberosIpAddressType_Type()
)
alaDaKerberosIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaKerberosIpAddressType.setStatus("current")
_AlaDaKerberosIpAddress_Type = InetAddress
_AlaDaKerberosIpAddress_Object = MibTableColumn
alaDaKerberosIpAddress = _AlaDaKerberosIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 5, 1, 2),
    _AlaDaKerberosIpAddress_Type()
)
alaDaKerberosIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaKerberosIpAddress.setStatus("current")


class _AlaDaKerberosUdpPort_Type(Integer32):
    """Custom type alaDaKerberosUdpPort based on Integer32"""
    defaultValue = 88

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaDaKerberosUdpPort_Type.__name__ = "Integer32"
_AlaDaKerberosUdpPort_Object = MibTableColumn
alaDaKerberosUdpPort = _AlaDaKerberosUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 5, 1, 3),
    _AlaDaKerberosUdpPort_Type()
)
alaDaKerberosUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaKerberosUdpPort.setStatus("current")


class _AlaDaKerberosRowStatus_Type(RowStatus):
    """Custom type alaDaKerberosRowStatus based on RowStatus"""
    defaultValue = 2


_AlaDaKerberosRowStatus_Type.__name__ = "RowStatus"
_AlaDaKerberosRowStatus_Object = MibTableColumn
alaDaKerberosRowStatus = _AlaDaKerberosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 53, 5, 1, 4),
    _AlaDaKerberosRowStatus_Type()
)
alaDaKerberosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaKerberosRowStatus.setStatus("current")
_AlaDaUNPPortVlanTable_Object = MibTable
alaDaUNPPortVlanTable = _AlaDaUNPPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 54)
)
if mibBuilder.loadTexts:
    alaDaUNPPortVlanTable.setStatus("current")
_AlaDaUNPPortVlanEntry_Object = MibTableRow
alaDaUNPPortVlanEntry = _AlaDaUNPPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 54, 1)
)
alaDaUNPPortVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortIfIndex"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortVlanVID"),
)
if mibBuilder.loadTexts:
    alaDaUNPPortVlanEntry.setStatus("current")


class _AlaDaUNPPortVlanVID_Type(Unsigned32):
    """Custom type alaDaUNPPortVlanVID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPPortVlanVID_Type.__name__ = "Unsigned32"
_AlaDaUNPPortVlanVID_Object = MibTableColumn
alaDaUNPPortVlanVID = _AlaDaUNPPortVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 54, 1, 1),
    _AlaDaUNPPortVlanVID_Type()
)
alaDaUNPPortVlanVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPPortVlanVID.setStatus("current")
_AlaDaUNPPortVlanRowStatus_Type = RowStatus
_AlaDaUNPPortVlanRowStatus_Object = MibTableColumn
alaDaUNPPortVlanRowStatus = _AlaDaUNPPortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 54, 1, 2),
    _AlaDaUNPPortVlanRowStatus_Type()
)
alaDaUNPPortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortVlanRowStatus.setStatus("current")


class _AlaDaUNPPortVlanType_Type(Integer32):
    """Custom type alaDaUNPPortVlanType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unpQtag", 1),
          ("unpUntag", 2))
    )


_AlaDaUNPPortVlanType_Type.__name__ = "Integer32"
_AlaDaUNPPortVlanType_Object = MibTableColumn
alaDaUNPPortVlanType = _AlaDaUNPPortVlanType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 54, 1, 3),
    _AlaDaUNPPortVlanType_Type()
)
alaDaUNPPortVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortVlanType.setStatus("current")
_AlaDaUNPVlanRuleTable_Object = MibTable
alaDaUNPVlanRuleTable = _AlaDaUNPVlanRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 55)
)
if mibBuilder.loadTexts:
    alaDaUNPVlanRuleTable.setStatus("current")
_AlaDaUNPVlanRuleEntry_Object = MibTableRow
alaDaUNPVlanRuleEntry = _AlaDaUNPVlanRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 55, 1)
)
alaDaUNPVlanRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVlanRuleVlanTag"),
)
if mibBuilder.loadTexts:
    alaDaUNPVlanRuleEntry.setStatus("current")


class _AlaDaUNPVlanRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPVlanRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPVlanRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPVlanRuleVlanTag_Object = MibTableColumn
alaDaUNPVlanRuleVlanTag = _AlaDaUNPVlanRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 55, 1, 1),
    _AlaDaUNPVlanRuleVlanTag_Type()
)
alaDaUNPVlanRuleVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVlanRuleVlanTag.setStatus("current")


class _AlaDaUNPVlanRuleVlanTagPosition_Type(Integer32):
    """Custom type alaDaUNPVlanRuleVlanTagPosition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outerTag", 1),
          ("innerTag", 2))
    )


_AlaDaUNPVlanRuleVlanTagPosition_Type.__name__ = "Integer32"
_AlaDaUNPVlanRuleVlanTagPosition_Object = MibTableColumn
alaDaUNPVlanRuleVlanTagPosition = _AlaDaUNPVlanRuleVlanTagPosition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 55, 1, 2),
    _AlaDaUNPVlanRuleVlanTagPosition_Type()
)
alaDaUNPVlanRuleVlanTagPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVlanRuleVlanTagPosition.setStatus("current")


class _AlaDaUNPVlanRuleEdgeProf_Type(SnmpAdminString):
    """Custom type alaDaUNPVlanRuleEdgeProf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPVlanRuleEdgeProf_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVlanRuleEdgeProf_Object = MibTableColumn
alaDaUNPVlanRuleEdgeProf = _AlaDaUNPVlanRuleEdgeProf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 55, 1, 3),
    _AlaDaUNPVlanRuleEdgeProf_Type()
)
alaDaUNPVlanRuleEdgeProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVlanRuleEdgeProf.setStatus("current")
_AlaDaUNPVlanRuleRowStatus_Type = RowStatus
_AlaDaUNPVlanRuleRowStatus_Object = MibTableColumn
alaDaUNPVlanRuleRowStatus = _AlaDaUNPVlanRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 55, 1, 4),
    _AlaDaUNPVlanRuleRowStatus_Type()
)
alaDaUNPVlanRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVlanRuleRowStatus.setStatus("current")
_AlaDaUNPETmplVlanTable_Object = MibTable
alaDaUNPETmplVlanTable = _AlaDaUNPETmplVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 56)
)
if mibBuilder.loadTexts:
    alaDaUNPETmplVlanTable.setStatus("current")
_AlaDaUNPETmplVlanEntry_Object = MibTableRow
alaDaUNPETmplVlanEntry = _AlaDaUNPETmplVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 56, 1)
)
alaDaUNPETmplVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPETmplName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPETmplVlanVID"),
)
if mibBuilder.loadTexts:
    alaDaUNPETmplVlanEntry.setStatus("current")


class _AlaDaUNPETmplVlanVID_Type(Unsigned32):
    """Custom type alaDaUNPETmplVlanVID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPETmplVlanVID_Type.__name__ = "Unsigned32"
_AlaDaUNPETmplVlanVID_Object = MibTableColumn
alaDaUNPETmplVlanVID = _AlaDaUNPETmplVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 56, 1, 1),
    _AlaDaUNPETmplVlanVID_Type()
)
alaDaUNPETmplVlanVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPETmplVlanVID.setStatus("current")
_AlaDaUNPETmplVlanRowStatus_Type = RowStatus
_AlaDaUNPETmplVlanRowStatus_Object = MibTableColumn
alaDaUNPETmplVlanRowStatus = _AlaDaUNPETmplVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 56, 1, 2),
    _AlaDaUNPETmplVlanRowStatus_Type()
)
alaDaUNPETmplVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPETmplVlanRowStatus.setStatus("current")
_AlaDaUNPUserFlushTable_Object = MibTable
alaDaUNPUserFlushTable = _AlaDaUNPUserFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57)
)
if mibBuilder.loadTexts:
    alaDaUNPUserFlushTable.setStatus("current")
_AlaDaUNPUserFlushEntry_Object = MibTableRow
alaDaUNPUserFlushEntry = _AlaDaUNPUserFlushEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1)
)
alaDaUNPUserFlushEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushIndex"),
)
if mibBuilder.loadTexts:
    alaDaUNPUserFlushEntry.setStatus("current")


class _AlaDaUNPUserFlushIndex_Type(Integer32):
    """Custom type alaDaUNPUserFlushIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaDaUNPUserFlushIndex_Type.__name__ = "Integer32"
_AlaDaUNPUserFlushIndex_Object = MibTableColumn
alaDaUNPUserFlushIndex = _AlaDaUNPUserFlushIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 1),
    _AlaDaUNPUserFlushIndex_Type()
)
alaDaUNPUserFlushIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushIndex.setStatus("current")


class _AlaDaUNPUserFlushComplete_Type(Integer32):
    """Custom type alaDaUNPUserFlushComplete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("all", 2))
    )


_AlaDaUNPUserFlushComplete_Type.__name__ = "Integer32"
_AlaDaUNPUserFlushComplete_Object = MibTableColumn
alaDaUNPUserFlushComplete = _AlaDaUNPUserFlushComplete_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 2),
    _AlaDaUNPUserFlushComplete_Type()
)
alaDaUNPUserFlushComplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushComplete.setStatus("current")


class _AlaDaUNPUserFlushAuthType_Type(Integer32):
    """Custom type alaDaUNPUserFlushAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("onex", 2),
          ("mac", 3))
    )


_AlaDaUNPUserFlushAuthType_Type.__name__ = "Integer32"
_AlaDaUNPUserFlushAuthType_Object = MibTableColumn
alaDaUNPUserFlushAuthType = _AlaDaUNPUserFlushAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 3),
    _AlaDaUNPUserFlushAuthType_Type()
)
alaDaUNPUserFlushAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushAuthType.setStatus("current")


class _AlaDaUNPUserFlushMacAddress_Type(MacAddress):
    """Custom type alaDaUNPUserFlushMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPUserFlushMacAddress_Type.__name__ = "MacAddress"
_AlaDaUNPUserFlushMacAddress_Object = MibTableColumn
alaDaUNPUserFlushMacAddress = _AlaDaUNPUserFlushMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 4),
    _AlaDaUNPUserFlushMacAddress_Type()
)
alaDaUNPUserFlushMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushMacAddress.setStatus("current")


class _AlaDaUNPUserFlushProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPUserFlushProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPUserFlushProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPUserFlushProfile_Object = MibTableColumn
alaDaUNPUserFlushProfile = _AlaDaUNPUserFlushProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 5),
    _AlaDaUNPUserFlushProfile_Type()
)
alaDaUNPUserFlushProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushProfile.setStatus("current")
_AlaDaUNPUserFlushPortStart_Type = InterfaceIndex
_AlaDaUNPUserFlushPortStart_Object = MibTableColumn
alaDaUNPUserFlushPortStart = _AlaDaUNPUserFlushPortStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 6),
    _AlaDaUNPUserFlushPortStart_Type()
)
alaDaUNPUserFlushPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushPortStart.setStatus("current")
_AlaDaUNPUserFlushPortEnd_Type = InterfaceIndex
_AlaDaUNPUserFlushPortEnd_Object = MibTableColumn
alaDaUNPUserFlushPortEnd = _AlaDaUNPUserFlushPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 7),
    _AlaDaUNPUserFlushPortEnd_Type()
)
alaDaUNPUserFlushPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushPortEnd.setStatus("current")
_AlaDaUNPUserFlushSapIDIfIndex_Type = InterfaceIndex
_AlaDaUNPUserFlushSapIDIfIndex_Object = MibTableColumn
alaDaUNPUserFlushSapIDIfIndex = _AlaDaUNPUserFlushSapIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 8),
    _AlaDaUNPUserFlushSapIDIfIndex_Type()
)
alaDaUNPUserFlushSapIDIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushSapIDIfIndex.setStatus("current")
_AlaDaUNPUserFlushSapIDEncapVal_Type = TmnxEncapVal
_AlaDaUNPUserFlushSapIDEncapVal_Object = MibTableColumn
alaDaUNPUserFlushSapIDEncapVal = _AlaDaUNPUserFlushSapIDEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 9),
    _AlaDaUNPUserFlushSapIDEncapVal_Type()
)
alaDaUNPUserFlushSapIDEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushSapIDEncapVal.setStatus("current")
_AlaDaUNPUserFlushServiceID_Type = Unsigned32
_AlaDaUNPUserFlushServiceID_Object = MibTableColumn
alaDaUNPUserFlushServiceID = _AlaDaUNPUserFlushServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 57, 1, 10),
    _AlaDaUNPUserFlushServiceID_Type()
)
alaDaUNPUserFlushServiceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPUserFlushServiceID.setStatus("current")
_AlaDaUNPCustDomainRuleTable_Object = MibTable
alaDaUNPCustDomainRuleTable = _AlaDaUNPCustDomainRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 58)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainRuleTable.setStatus("current")
_AlaDaUNPCustDomainRuleEntry_Object = MibTableRow
alaDaUNPCustDomainRuleEntry = _AlaDaUNPCustDomainRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 58, 1)
)
alaDaUNPCustDomainRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainRuleId"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainRuleId_Type(Integer32):
    """Custom type alaDaUNPCustDomainRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaDaUNPCustDomainRuleId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainRuleId_Object = MibTableColumn
alaDaUNPCustDomainRuleId = _AlaDaUNPCustDomainRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 58, 1, 1),
    _AlaDaUNPCustDomainRuleId_Type()
)
alaDaUNPCustDomainRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainRuleId.setStatus("current")


class _AlaDaUNPCustDomainRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPCustDomainRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPCustDomainRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainRuleVlanTag_Object = MibTableColumn
alaDaUNPCustDomainRuleVlanTag = _AlaDaUNPCustDomainRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 58, 1, 2),
    _AlaDaUNPCustDomainRuleVlanTag_Type()
)
alaDaUNPCustDomainRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainRuleVlanTag.setStatus("current")


class _AlaDaUNPCustDomainRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainRuleProfile1_Object = MibTableColumn
alaDaUNPCustDomainRuleProfile1 = _AlaDaUNPCustDomainRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 58, 1, 3),
    _AlaDaUNPCustDomainRuleProfile1_Type()
)
alaDaUNPCustDomainRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainRuleProfile1.setStatus("current")


class _AlaDaUNPCustDomainRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainRuleProfile2_Object = MibTableColumn
alaDaUNPCustDomainRuleProfile2 = _AlaDaUNPCustDomainRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 58, 1, 4),
    _AlaDaUNPCustDomainRuleProfile2_Type()
)
alaDaUNPCustDomainRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainRuleProfile2.setStatus("current")


class _AlaDaUNPCustDomainRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainRuleProfile3_Object = MibTableColumn
alaDaUNPCustDomainRuleProfile3 = _AlaDaUNPCustDomainRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 58, 1, 5),
    _AlaDaUNPCustDomainRuleProfile3_Type()
)
alaDaUNPCustDomainRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainRuleProfile3.setStatus("current")
_AlaDaUNPCustDomainRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainRuleRowStatus = _AlaDaUNPCustDomainRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 58, 1, 6),
    _AlaDaUNPCustDomainRuleRowStatus_Type()
)
alaDaUNPCustDomainRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainRuleRowStatus.setStatus("current")
_AlaDaUNPPortTemplateTable_Object = MibTable
alaDaUNPPortTemplateTable = _AlaDaUNPPortTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59)
)
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateTable.setStatus("current")
_AlaDaUNPPortTemplateEntry_Object = MibTableRow
alaDaUNPPortTemplateEntry = _AlaDaUNPPortTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1)
)
alaDaUNPPortTemplateEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateName"),
)
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateEntry.setStatus("current")


class _AlaDaUNPPortTemplateName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPPortTemplateName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortTemplateName_Object = MibTableColumn
alaDaUNPPortTemplateName = _AlaDaUNPPortTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 1),
    _AlaDaUNPPortTemplateName_Type()
)
alaDaUNPPortTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateName.setStatus("current")


class _AlaDaUNPPortTemplateAdminState_Type(Integer32):
    """Custom type alaDaUNPPortTemplateAdminState based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPPortTemplateAdminState_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateAdminState_Object = MibTableColumn
alaDaUNPPortTemplateAdminState = _AlaDaUNPPortTemplateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 2),
    _AlaDaUNPPortTemplateAdminState_Type()
)
alaDaUNPPortTemplateAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateAdminState.setStatus("current")


class _AlaDaUNPPortTemplateDirection_Type(Integer32):
    """Custom type alaDaUNPPortTemplateDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("in", 2),
          ("noVal", 3))
    )


_AlaDaUNPPortTemplateDirection_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateDirection_Object = MibTableColumn
alaDaUNPPortTemplateDirection = _AlaDaUNPPortTemplateDirection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 3),
    _AlaDaUNPPortTemplateDirection_Type()
)
alaDaUNPPortTemplateDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateDirection.setStatus("current")


class _AlaDaUNPPortTemplateDomainID_Type(Unsigned32):
    """Custom type alaDaUNPPortTemplateDomainID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPPortTemplateDomainID_Type.__name__ = "Unsigned32"
_AlaDaUNPPortTemplateDomainID_Object = MibTableColumn
alaDaUNPPortTemplateDomainID = _AlaDaUNPPortTemplateDomainID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 4),
    _AlaDaUNPPortTemplateDomainID_Type()
)
alaDaUNPPortTemplateDomainID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateDomainID.setStatus("current")


class _AlaDaUNPPortTemplateClassification_Type(Integer32):
    """Custom type alaDaUNPPortTemplateClassification based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPPortTemplateClassification_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateClassification_Object = MibTableColumn
alaDaUNPPortTemplateClassification = _AlaDaUNPPortTemplateClassification_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 5),
    _AlaDaUNPPortTemplateClassification_Type()
)
alaDaUNPPortTemplateClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateClassification.setStatus("current")


class _AlaDaUNPPortTemplateTrustTag_Type(Integer32):
    """Custom type alaDaUNPPortTemplateTrustTag based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPPortTemplateTrustTag_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateTrustTag_Object = MibTableColumn
alaDaUNPPortTemplateTrustTag = _AlaDaUNPPortTemplateTrustTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 6),
    _AlaDaUNPPortTemplateTrustTag_Type()
)
alaDaUNPPortTemplateTrustTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateTrustTag.setStatus("current")


class _AlaDaUNPPortTemplateDynamicService_Type(Integer32):
    """Custom type alaDaUNPPortTemplateDynamicService based on Integer32"""
    defaultValue = 1

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
          ("spb", 2),
          ("vxlan", 3))
    )


_AlaDaUNPPortTemplateDynamicService_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateDynamicService_Object = MibTableColumn
alaDaUNPPortTemplateDynamicService = _AlaDaUNPPortTemplateDynamicService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 7),
    _AlaDaUNPPortTemplateDynamicService_Type()
)
alaDaUNPPortTemplateDynamicService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateDynamicService.setStatus("current")


class _AlaDaUNPPortTemplateDefaultProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPPortTemplateDefaultProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortTemplateDefaultProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortTemplateDefaultProfile_Object = MibTableColumn
alaDaUNPPortTemplateDefaultProfile = _AlaDaUNPPortTemplateDefaultProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 8),
    _AlaDaUNPPortTemplateDefaultProfile_Type()
)
alaDaUNPPortTemplateDefaultProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateDefaultProfile.setStatus("current")


class _AlaDaUNPPortTemplateAAAProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPPortTemplateAAAProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortTemplateAAAProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortTemplateAAAProfile_Object = MibTableColumn
alaDaUNPPortTemplateAAAProfile = _AlaDaUNPPortTemplateAAAProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 9),
    _AlaDaUNPPortTemplateAAAProfile_Type()
)
alaDaUNPPortTemplateAAAProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateAAAProfile.setStatus("current")


class _AlaDaUNPPortTemplateRedirectPortBounce_Type(Integer32):
    """Custom type alaDaUNPPortTemplateRedirectPortBounce based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPortTemplateRedirectPortBounce_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateRedirectPortBounce_Object = MibTableColumn
alaDaUNPPortTemplateRedirectPortBounce = _AlaDaUNPPortTemplateRedirectPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 10),
    _AlaDaUNPPortTemplateRedirectPortBounce_Type()
)
alaDaUNPPortTemplateRedirectPortBounce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateRedirectPortBounce.setStatus("current")


class _AlaDaUNPPortTemplate8021XAuth_Type(Integer32):
    """Custom type alaDaUNPPortTemplate8021XAuth based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPPortTemplate8021XAuth_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplate8021XAuth_Object = MibTableColumn
alaDaUNPPortTemplate8021XAuth = _AlaDaUNPPortTemplate8021XAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 11),
    _AlaDaUNPPortTemplate8021XAuth_Type()
)
alaDaUNPPortTemplate8021XAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplate8021XAuth.setStatus("current")


class _AlaDaUNPPortTemplate8021XAuthPassAlternate_Type(SnmpAdminString):
    """Custom type alaDaUNPPortTemplate8021XAuthPassAlternate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortTemplate8021XAuthPassAlternate_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortTemplate8021XAuthPassAlternate_Object = MibTableColumn
alaDaUNPPortTemplate8021XAuthPassAlternate = _AlaDaUNPPortTemplate8021XAuthPassAlternate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 12),
    _AlaDaUNPPortTemplate8021XAuthPassAlternate_Type()
)
alaDaUNPPortTemplate8021XAuthPassAlternate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplate8021XAuthPassAlternate.setStatus("current")


class _AlaDaUNPPortTemplate8021XAuthBypass_Type(Integer32):
    """Custom type alaDaUNPPortTemplate8021XAuthBypass based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPPortTemplate8021XAuthBypass_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplate8021XAuthBypass_Object = MibTableColumn
alaDaUNPPortTemplate8021XAuthBypass = _AlaDaUNPPortTemplate8021XAuthBypass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 13),
    _AlaDaUNPPortTemplate8021XAuthBypass_Type()
)
alaDaUNPPortTemplate8021XAuthBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplate8021XAuthBypass.setStatus("current")


class _AlaDaUNPPortTemplate8021XAuthFailPolicy_Type(Integer32):
    """Custom type alaDaUNPPortTemplate8021XAuthFailPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mac", 2))
    )


_AlaDaUNPPortTemplate8021XAuthFailPolicy_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplate8021XAuthFailPolicy_Object = MibTableColumn
alaDaUNPPortTemplate8021XAuthFailPolicy = _AlaDaUNPPortTemplate8021XAuthFailPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 14),
    _AlaDaUNPPortTemplate8021XAuthFailPolicy_Type()
)
alaDaUNPPortTemplate8021XAuthFailPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplate8021XAuthFailPolicy.setStatus("current")


class _AlaDaUNPPortTemplate8021XAuthTxPeriod_Type(Unsigned32):
    """Custom type alaDaUNPPortTemplate8021XAuthTxPeriod based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AlaDaUNPPortTemplate8021XAuthTxPeriod_Type.__name__ = "Unsigned32"
_AlaDaUNPPortTemplate8021XAuthTxPeriod_Object = MibTableColumn
alaDaUNPPortTemplate8021XAuthTxPeriod = _AlaDaUNPPortTemplate8021XAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 15),
    _AlaDaUNPPortTemplate8021XAuthTxPeriod_Type()
)
alaDaUNPPortTemplate8021XAuthTxPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplate8021XAuthTxPeriod.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplate8021XAuthTxPeriod.setUnits("seconds")


class _AlaDaUNPPortTemplate8021XAuthSuppTimeout_Type(Unsigned32):
    """Custom type alaDaUNPPortTemplate8021XAuthSuppTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AlaDaUNPPortTemplate8021XAuthSuppTimeout_Type.__name__ = "Unsigned32"
_AlaDaUNPPortTemplate8021XAuthSuppTimeout_Object = MibTableColumn
alaDaUNPPortTemplate8021XAuthSuppTimeout = _AlaDaUNPPortTemplate8021XAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 16),
    _AlaDaUNPPortTemplate8021XAuthSuppTimeout_Type()
)
alaDaUNPPortTemplate8021XAuthSuppTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplate8021XAuthSuppTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplate8021XAuthSuppTimeout.setUnits("seconds")


class _AlaDaUNPPortTemplate8021XAuthMaxReq_Type(Unsigned32):
    """Custom type alaDaUNPPortTemplate8021XAuthMaxReq based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AlaDaUNPPortTemplate8021XAuthMaxReq_Type.__name__ = "Unsigned32"
_AlaDaUNPPortTemplate8021XAuthMaxReq_Object = MibTableColumn
alaDaUNPPortTemplate8021XAuthMaxReq = _AlaDaUNPPortTemplate8021XAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 17),
    _AlaDaUNPPortTemplate8021XAuthMaxReq_Type()
)
alaDaUNPPortTemplate8021XAuthMaxReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplate8021XAuthMaxReq.setStatus("current")


class _AlaDaUNPPortTemplateMACAuth_Type(Integer32):
    """Custom type alaDaUNPPortTemplateMACAuth based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPPortTemplateMACAuth_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateMACAuth_Object = MibTableColumn
alaDaUNPPortTemplateMACAuth = _AlaDaUNPPortTemplateMACAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 18),
    _AlaDaUNPPortTemplateMACAuth_Type()
)
alaDaUNPPortTemplateMACAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateMACAuth.setStatus("current")


class _AlaDaUNPPortTemplateMACAuthPassAlternate_Type(SnmpAdminString):
    """Custom type alaDaUNPPortTemplateMACAuthPassAlternate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortTemplateMACAuthPassAlternate_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortTemplateMACAuthPassAlternate_Object = MibTableColumn
alaDaUNPPortTemplateMACAuthPassAlternate = _AlaDaUNPPortTemplateMACAuthPassAlternate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 19),
    _AlaDaUNPPortTemplateMACAuthPassAlternate_Type()
)
alaDaUNPPortTemplateMACAuthPassAlternate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateMACAuthPassAlternate.setStatus("current")


class _AlaDaUNPPortTemplateMACAuthAllowEAP_Type(Integer32):
    """Custom type alaDaUNPPortTemplateMACAuthAllowEAP based on Integer32"""
    defaultValue = 4

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
        *(("pass", 1),
          ("fail", 2),
          ("noAuth", 3),
          ("none", 4))
    )


_AlaDaUNPPortTemplateMACAuthAllowEAP_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateMACAuthAllowEAP_Object = MibTableColumn
alaDaUNPPortTemplateMACAuthAllowEAP = _AlaDaUNPPortTemplateMACAuthAllowEAP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 20),
    _AlaDaUNPPortTemplateMACAuthAllowEAP_Type()
)
alaDaUNPPortTemplateMACAuthAllowEAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateMACAuthAllowEAP.setStatus("current")


class _AlaDaUNPPortTemplateForceL3Learning_Type(Integer32):
    """Custom type alaDaUNPPortTemplateForceL3Learning based on Integer32"""
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


_AlaDaUNPPortTemplateForceL3Learning_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateForceL3Learning_Object = MibTableColumn
alaDaUNPPortTemplateForceL3Learning = _AlaDaUNPPortTemplateForceL3Learning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 21),
    _AlaDaUNPPortTemplateForceL3Learning_Type()
)
alaDaUNPPortTemplateForceL3Learning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateForceL3Learning.setStatus("current")


class _AlaDaUNPPortTemplateForceL3LearningPortBounce_Type(Integer32):
    """Custom type alaDaUNPPortTemplateForceL3LearningPortBounce based on Integer32"""
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


_AlaDaUNPPortTemplateForceL3LearningPortBounce_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateForceL3LearningPortBounce_Object = MibTableColumn
alaDaUNPPortTemplateForceL3LearningPortBounce = _AlaDaUNPPortTemplateForceL3LearningPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 22),
    _AlaDaUNPPortTemplateForceL3LearningPortBounce_Type()
)
alaDaUNPPortTemplateForceL3LearningPortBounce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateForceL3LearningPortBounce.setStatus("current")
_AlaDaUNPPortTemplateRowStatus_Type = RowStatus
_AlaDaUNPPortTemplateRowStatus_Object = MibTableColumn
alaDaUNPPortTemplateRowStatus = _AlaDaUNPPortTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 23),
    _AlaDaUNPPortTemplateRowStatus_Type()
)
alaDaUNPPortTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateRowStatus.setStatus("current")


class _AlaDaUNPPortTemplateL2Profile_Type(SnmpAdminString):
    """Custom type alaDaUNPPortTemplateL2Profile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortTemplateL2Profile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortTemplateL2Profile_Object = MibTableColumn
alaDaUNPPortTemplateL2Profile = _AlaDaUNPPortTemplateL2Profile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 24),
    _AlaDaUNPPortTemplateL2Profile_Type()
)
alaDaUNPPortTemplateL2Profile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateL2Profile.setStatus("current")


class _AlaDaUNPPortTemplateApMode_Type(Integer32):
    """Custom type alaDaUNPPortTemplateApMode based on Integer32"""
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


_AlaDaUNPPortTemplateApMode_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateApMode_Object = MibTableColumn
alaDaUNPPortTemplateApMode = _AlaDaUNPPortTemplateApMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 25),
    _AlaDaUNPPortTemplateApMode_Type()
)
alaDaUNPPortTemplateApMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateApMode.setStatus("current")


class _AlaDaUNPPortTemplateApModeSecurity_Type(Integer32):
    """Custom type alaDaUNPPortTemplateApModeSecurity based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPortTemplateApModeSecurity_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateApModeSecurity_Object = MibTableColumn
alaDaUNPPortTemplateApModeSecurity = _AlaDaUNPPortTemplateApModeSecurity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 26),
    _AlaDaUNPPortTemplateApModeSecurity_Type()
)
alaDaUNPPortTemplateApModeSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateApModeSecurity.setStatus("current")


class _AlaDaUNPPortTemplateSwSuppSecureMode_Type(Integer32):
    """Custom type alaDaUNPPortTemplateSwSuppSecureMode based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPortTemplateSwSuppSecureMode_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateSwSuppSecureMode_Object = MibTableColumn
alaDaUNPPortTemplateSwSuppSecureMode = _AlaDaUNPPortTemplateSwSuppSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 27),
    _AlaDaUNPPortTemplateSwSuppSecureMode_Type()
)
alaDaUNPPortTemplateSwSuppSecureMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateSwSuppSecureMode.setStatus("current")


class _AlaDaUNPPortTemplateBpduLldpLearn_Type(Integer32):
    """Custom type alaDaUNPPortTemplateBpduLldpLearn based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPPortTemplateBpduLldpLearn_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateBpduLldpLearn_Object = MibTableColumn
alaDaUNPPortTemplateBpduLldpLearn = _AlaDaUNPPortTemplateBpduLldpLearn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 59, 1, 28),
    _AlaDaUNPPortTemplateBpduLldpLearn_Type()
)
alaDaUNPPortTemplateBpduLldpLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateBpduLldpLearn.setStatus("current")
_AlaDaUNPProfileTable_Object = MibTable
alaDaUNPProfileTable = _AlaDaUNPProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60)
)
if mibBuilder.loadTexts:
    alaDaUNPProfileTable.setStatus("current")
_AlaDaUNPProfileEntry_Object = MibTableRow
alaDaUNPProfileEntry = _AlaDaUNPProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1)
)
alaDaUNPProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPProfileEntry.setStatus("current")


class _AlaDaUNPProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileName_Object = MibTableColumn
alaDaUNPProfileName = _AlaDaUNPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 1),
    _AlaDaUNPProfileName_Type()
)
alaDaUNPProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPProfileName.setStatus("current")


class _AlaDaUNPProfileAuthenticationFlag_Type(Integer32):
    """Custom type alaDaUNPProfileAuthenticationFlag based on Integer32"""
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


_AlaDaUNPProfileAuthenticationFlag_Type.__name__ = "Integer32"
_AlaDaUNPProfileAuthenticationFlag_Object = MibTableColumn
alaDaUNPProfileAuthenticationFlag = _AlaDaUNPProfileAuthenticationFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 2),
    _AlaDaUNPProfileAuthenticationFlag_Type()
)
alaDaUNPProfileAuthenticationFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileAuthenticationFlag.setStatus("current")


class _AlaDaUNPProfileMobileTag_Type(Integer32):
    """Custom type alaDaUNPProfileMobileTag based on Integer32"""
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


_AlaDaUNPProfileMobileTag_Type.__name__ = "Integer32"
_AlaDaUNPProfileMobileTag_Object = MibTableColumn
alaDaUNPProfileMobileTag = _AlaDaUNPProfileMobileTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 3),
    _AlaDaUNPProfileMobileTag_Type()
)
alaDaUNPProfileMobileTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMobileTag.setStatus("current")


class _AlaDaUNPProfileCPortalAuthentication_Type(Integer32):
    """Custom type alaDaUNPProfileCPortalAuthentication based on Integer32"""
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


_AlaDaUNPProfileCPortalAuthentication_Type.__name__ = "Integer32"
_AlaDaUNPProfileCPortalAuthentication_Object = MibTableColumn
alaDaUNPProfileCPortalAuthentication = _AlaDaUNPProfileCPortalAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 4),
    _AlaDaUNPProfileCPortalAuthentication_Type()
)
alaDaUNPProfileCPortalAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileCPortalAuthentication.setStatus("current")


class _AlaDaUNPProfileRedirect_Type(Integer32):
    """Custom type alaDaUNPProfileRedirect based on Integer32"""
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


_AlaDaUNPProfileRedirect_Type.__name__ = "Integer32"
_AlaDaUNPProfileRedirect_Object = MibTableColumn
alaDaUNPProfileRedirect = _AlaDaUNPProfileRedirect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 5),
    _AlaDaUNPProfileRedirect_Type()
)
alaDaUNPProfileRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileRedirect.setStatus("current")


class _AlaDaUNPProfileQoSPolicy_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileQoSPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfileQoSPolicy_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileQoSPolicy_Object = MibTableColumn
alaDaUNPProfileQoSPolicy = _AlaDaUNPProfileQoSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 6),
    _AlaDaUNPProfileQoSPolicy_Type()
)
alaDaUNPProfileQoSPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileQoSPolicy.setStatus("current")


class _AlaDaUNPProfilePeriodPolicy_Type(SnmpAdminString):
    """Custom type alaDaUNPProfilePeriodPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfilePeriodPolicy_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfilePeriodPolicy_Object = MibTableColumn
alaDaUNPProfilePeriodPolicy = _AlaDaUNPProfilePeriodPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 7),
    _AlaDaUNPProfilePeriodPolicy_Type()
)
alaDaUNPProfilePeriodPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfilePeriodPolicy.setStatus("current")


class _AlaDaUNPProfileCPortalProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileCPortalProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfileCPortalProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileCPortalProfile_Object = MibTableColumn
alaDaUNPProfileCPortalProfile = _AlaDaUNPProfileCPortalProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 8),
    _AlaDaUNPProfileCPortalProfile_Type()
)
alaDaUNPProfileCPortalProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileCPortalProfile.setStatus("current")


class _AlaDaUNPProfileLocationPolicy_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileLocationPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfileLocationPolicy_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileLocationPolicy_Object = MibTableColumn
alaDaUNPProfileLocationPolicy = _AlaDaUNPProfileLocationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 9),
    _AlaDaUNPProfileLocationPolicy_Type()
)
alaDaUNPProfileLocationPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileLocationPolicy.setStatus("current")


class _AlaDaUNPProfileSaaProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileSaaProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfileSaaProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileSaaProfile_Object = MibTableColumn
alaDaUNPProfileSaaProfile = _AlaDaUNPProfileSaaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 10),
    _AlaDaUNPProfileSaaProfile_Type()
)
alaDaUNPProfileSaaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileSaaProfile.setStatus("current")


class _AlaDaUNPProfileInactivityInterval_Type(Integer32):
    """Custom type alaDaUNPProfileInactivityInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_AlaDaUNPProfileInactivityInterval_Type.__name__ = "Integer32"
_AlaDaUNPProfileInactivityInterval_Object = MibTableColumn
alaDaUNPProfileInactivityInterval = _AlaDaUNPProfileInactivityInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 11),
    _AlaDaUNPProfileInactivityInterval_Type()
)
alaDaUNPProfileInactivityInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileInactivityInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPProfileInactivityInterval.setUnits("minutes")


class _AlaDaUNPProfileKerberosAuthentication_Type(Integer32):
    """Custom type alaDaUNPProfileKerberosAuthentication based on Integer32"""
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


_AlaDaUNPProfileKerberosAuthentication_Type.__name__ = "Integer32"
_AlaDaUNPProfileKerberosAuthentication_Object = MibTableColumn
alaDaUNPProfileKerberosAuthentication = _AlaDaUNPProfileKerberosAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 12),
    _AlaDaUNPProfileKerberosAuthentication_Type()
)
alaDaUNPProfileKerberosAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileKerberosAuthentication.setStatus("current")


class _AlaDaUNPProfileMaxIngressBandwidth_Type(Integer32):
    """Custom type alaDaUNPProfileMaxIngressBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUNPProfileMaxIngressBandwidth_Type.__name__ = "Integer32"
_AlaDaUNPProfileMaxIngressBandwidth_Object = MibTableColumn
alaDaUNPProfileMaxIngressBandwidth = _AlaDaUNPProfileMaxIngressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 13),
    _AlaDaUNPProfileMaxIngressBandwidth_Type()
)
alaDaUNPProfileMaxIngressBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMaxIngressBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPProfileMaxIngressBandwidth.setUnits("kilobits per second")


class _AlaDaUNPProfileMaxEgressBandwidth_Type(Integer32):
    """Custom type alaDaUNPProfileMaxEgressBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_AlaDaUNPProfileMaxEgressBandwidth_Type.__name__ = "Integer32"
_AlaDaUNPProfileMaxEgressBandwidth_Object = MibTableColumn
alaDaUNPProfileMaxEgressBandwidth = _AlaDaUNPProfileMaxEgressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 14),
    _AlaDaUNPProfileMaxEgressBandwidth_Type()
)
alaDaUNPProfileMaxEgressBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMaxEgressBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPProfileMaxEgressBandwidth.setUnits("kilobits per second")


class _AlaDaUNPProfileMaxIngressDepth_Type(Integer32):
    """Custom type alaDaUNPProfileMaxIngressDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16384),
    )


_AlaDaUNPProfileMaxIngressDepth_Type.__name__ = "Integer32"
_AlaDaUNPProfileMaxIngressDepth_Object = MibTableColumn
alaDaUNPProfileMaxIngressDepth = _AlaDaUNPProfileMaxIngressDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 15),
    _AlaDaUNPProfileMaxIngressDepth_Type()
)
alaDaUNPProfileMaxIngressDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMaxIngressDepth.setStatus("current")


class _AlaDaUNPProfileMaxEgressDepth_Type(Integer32):
    """Custom type alaDaUNPProfileMaxEgressDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16384),
    )


_AlaDaUNPProfileMaxEgressDepth_Type.__name__ = "Integer32"
_AlaDaUNPProfileMaxEgressDepth_Object = MibTableColumn
alaDaUNPProfileMaxEgressDepth = _AlaDaUNPProfileMaxEgressDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 16),
    _AlaDaUNPProfileMaxEgressDepth_Type()
)
alaDaUNPProfileMaxEgressDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMaxEgressDepth.setStatus("current")
_AlaDaUNPProfileRowStatus_Type = RowStatus
_AlaDaUNPProfileRowStatus_Object = MibTableColumn
alaDaUNPProfileRowStatus = _AlaDaUNPProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 17),
    _AlaDaUNPProfileRowStatus_Type()
)
alaDaUNPProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileRowStatus.setStatus("current")


class _AlaDaUNPProfileAFDConfig_Type(Integer32):
    """Custom type alaDaUNPProfileAFDConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("autoFabric", 2))
    )


_AlaDaUNPProfileAFDConfig_Type.__name__ = "Integer32"
_AlaDaUNPProfileAFDConfig_Object = MibTableColumn
alaDaUNPProfileAFDConfig = _AlaDaUNPProfileAFDConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 18),
    _AlaDaUNPProfileAFDConfig_Type()
)
alaDaUNPProfileAFDConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPProfileAFDConfig.setStatus("current")


class _AlaDaUNPProfileMacMobility_Type(Integer32):
    """Custom type alaDaUNPProfileMacMobility based on Integer32"""
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


_AlaDaUNPProfileMacMobility_Type.__name__ = "Integer32"
_AlaDaUNPProfileMacMobility_Object = MibTableColumn
alaDaUNPProfileMacMobility = _AlaDaUNPProfileMacMobility_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 60, 1, 19),
    _AlaDaUNPProfileMacMobility_Type()
)
alaDaUNPProfileMacMobility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMacMobility.setStatus("current")
_AlaDaUNPProfileMapVlanTable_Object = MibTable
alaDaUNPProfileMapVlanTable = _AlaDaUNPProfileMapVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 61)
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVlanTable.setStatus("current")
_AlaDaUNPProfileMapVlanEntry_Object = MibTableRow
alaDaUNPProfileMapVlanEntry = _AlaDaUNPProfileMapVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 61, 1)
)
alaDaUNPProfileMapVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVlanEntry.setStatus("current")


class _AlaDaUNPProfileMapVlanVlanID_Type(Unsigned32):
    """Custom type alaDaUNPProfileMapVlanVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPProfileMapVlanVlanID_Type.__name__ = "Unsigned32"
_AlaDaUNPProfileMapVlanVlanID_Object = MibTableColumn
alaDaUNPProfileMapVlanVlanID = _AlaDaUNPProfileMapVlanVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 61, 1, 1),
    _AlaDaUNPProfileMapVlanVlanID_Type()
)
alaDaUNPProfileMapVlanVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVlanVlanID.setStatus("current")
_AlaDaUNPProfileMapVlanRowStatus_Type = RowStatus
_AlaDaUNPProfileMapVlanRowStatus_Object = MibTableColumn
alaDaUNPProfileMapVlanRowStatus = _AlaDaUNPProfileMapVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 61, 1, 2),
    _AlaDaUNPProfileMapVlanRowStatus_Type()
)
alaDaUNPProfileMapVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVlanRowStatus.setStatus("current")
_AlaDaUNPProfileMapSpbTable_Object = MibTable
alaDaUNPProfileMapSpbTable = _AlaDaUNPProfileMapSpbTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62)
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbTable.setStatus("current")
_AlaDaUNPProfileMapSpbEntry_Object = MibTableRow
alaDaUNPProfileMapSpbEntry = _AlaDaUNPProfileMapSpbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1)
)
alaDaUNPProfileMapSpbEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbEntry.setStatus("current")
_AlaDaUNPProfileMapSpbEncapVal_Type = TmnxEncapVal
_AlaDaUNPProfileMapSpbEncapVal_Object = MibTableColumn
alaDaUNPProfileMapSpbEncapVal = _AlaDaUNPProfileMapSpbEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 1),
    _AlaDaUNPProfileMapSpbEncapVal_Type()
)
alaDaUNPProfileMapSpbEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbEncapVal.setStatus("current")


class _AlaDaUNPProfileMapSpbIsid_Type(Unsigned32):
    """Custom type alaDaUNPProfileMapSpbIsid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_AlaDaUNPProfileMapSpbIsid_Type.__name__ = "Unsigned32"
_AlaDaUNPProfileMapSpbIsid_Object = MibTableColumn
alaDaUNPProfileMapSpbIsid = _AlaDaUNPProfileMapSpbIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 2),
    _AlaDaUNPProfileMapSpbIsid_Type()
)
alaDaUNPProfileMapSpbIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbIsid.setStatus("current")


class _AlaDaUNPProfileMapSpbBVlan_Type(Unsigned32):
    """Custom type alaDaUNPProfileMapSpbBVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPProfileMapSpbBVlan_Type.__name__ = "Unsigned32"
_AlaDaUNPProfileMapSpbBVlan_Object = MibTableColumn
alaDaUNPProfileMapSpbBVlan = _AlaDaUNPProfileMapSpbBVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 3),
    _AlaDaUNPProfileMapSpbBVlan_Type()
)
alaDaUNPProfileMapSpbBVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbBVlan.setStatus("current")


class _AlaDaUNPProfileMapSpbMulticastMode_Type(Integer32):
    """Custom type alaDaUNPProfileMapSpbMulticastMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("headend", 1),
          ("tandem", 2))
    )


_AlaDaUNPProfileMapSpbMulticastMode_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapSpbMulticastMode_Object = MibTableColumn
alaDaUNPProfileMapSpbMulticastMode = _AlaDaUNPProfileMapSpbMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 4),
    _AlaDaUNPProfileMapSpbMulticastMode_Type()
)
alaDaUNPProfileMapSpbMulticastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbMulticastMode.setStatus("current")


class _AlaDaUNPProfileMapSpbVlanXlation_Type(Integer32):
    """Custom type alaDaUNPProfileMapSpbVlanXlation based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPProfileMapSpbVlanXlation_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapSpbVlanXlation_Object = MibTableColumn
alaDaUNPProfileMapSpbVlanXlation = _AlaDaUNPProfileMapSpbVlanXlation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 5),
    _AlaDaUNPProfileMapSpbVlanXlation_Type()
)
alaDaUNPProfileMapSpbVlanXlation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbVlanXlation.setStatus("current")
_AlaDaUNPProfileMapSpbRowStatus_Type = RowStatus
_AlaDaUNPProfileMapSpbRowStatus_Object = MibTableColumn
alaDaUNPProfileMapSpbRowStatus = _AlaDaUNPProfileMapSpbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 6),
    _AlaDaUNPProfileMapSpbRowStatus_Type()
)
alaDaUNPProfileMapSpbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbRowStatus.setStatus("current")


class _AlaDaUNPProfileMapSpbIgmpSnooping_Type(Integer32):
    """Custom type alaDaUNPProfileMapSpbIgmpSnooping based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapSpbIgmpSnooping_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapSpbIgmpSnooping_Object = MibTableColumn
alaDaUNPProfileMapSpbIgmpSnooping = _AlaDaUNPProfileMapSpbIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 7),
    _AlaDaUNPProfileMapSpbIgmpSnooping_Type()
)
alaDaUNPProfileMapSpbIgmpSnooping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbIgmpSnooping.setStatus("current")


class _AlaDaUNPProfileMapSpbIgmpProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileMapSpbIgmpProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfileMapSpbIgmpProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileMapSpbIgmpProfile_Object = MibTableColumn
alaDaUNPProfileMapSpbIgmpProfile = _AlaDaUNPProfileMapSpbIgmpProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 8),
    _AlaDaUNPProfileMapSpbIgmpProfile_Type()
)
alaDaUNPProfileMapSpbIgmpProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbIgmpProfile.setStatus("current")


class _AlaDaUNPProfileMapSpbMldSnooping_Type(Integer32):
    """Custom type alaDaUNPProfileMapSpbMldSnooping based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapSpbMldSnooping_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapSpbMldSnooping_Object = MibTableColumn
alaDaUNPProfileMapSpbMldSnooping = _AlaDaUNPProfileMapSpbMldSnooping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 9),
    _AlaDaUNPProfileMapSpbMldSnooping_Type()
)
alaDaUNPProfileMapSpbMldSnooping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbMldSnooping.setStatus("current")


class _AlaDaUNPProfileMapSpbMldProfile_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileMapSpbMldProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfileMapSpbMldProfile_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileMapSpbMldProfile_Object = MibTableColumn
alaDaUNPProfileMapSpbMldProfile = _AlaDaUNPProfileMapSpbMldProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 10),
    _AlaDaUNPProfileMapSpbMldProfile_Type()
)
alaDaUNPProfileMapSpbMldProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbMldProfile.setStatus("current")


class _AlaDaUNPProfileMapSpbRemoveIngressTag_Type(Integer32):
    """Custom type alaDaUNPProfileMapSpbRemoveIngressTag based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapSpbRemoveIngressTag_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapSpbRemoveIngressTag_Object = MibTableColumn
alaDaUNPProfileMapSpbRemoveIngressTag = _AlaDaUNPProfileMapSpbRemoveIngressTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 11),
    _AlaDaUNPProfileMapSpbRemoveIngressTag_Type()
)
alaDaUNPProfileMapSpbRemoveIngressTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbRemoveIngressTag.setStatus("current")


class _AlaDaUNPProfileMapSpbETree_Type(Integer32):
    """Custom type alaDaUNPProfileMapSpbETree based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapSpbETree_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapSpbETree_Object = MibTableColumn
alaDaUNPProfileMapSpbETree = _AlaDaUNPProfileMapSpbETree_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 62, 1, 12),
    _AlaDaUNPProfileMapSpbETree_Type()
)
alaDaUNPProfileMapSpbETree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbETree.setStatus("current")
_AlaDaUNPProfileMapVxlanTable_Object = MibTable
alaDaUNPProfileMapVxlanTable = _AlaDaUNPProfileMapVxlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63)
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanTable.setStatus("current")
_AlaDaUNPProfileMapVxlanEntry_Object = MibTableRow
alaDaUNPProfileMapVxlanEntry = _AlaDaUNPProfileMapVxlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1)
)
alaDaUNPProfileMapVxlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanEntry.setStatus("current")
_AlaDaUNPProfileMapVxlanEncapVal_Type = TmnxEncapVal
_AlaDaUNPProfileMapVxlanEncapVal_Object = MibTableColumn
alaDaUNPProfileMapVxlanEncapVal = _AlaDaUNPProfileMapVxlanEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 1),
    _AlaDaUNPProfileMapVxlanEncapVal_Type()
)
alaDaUNPProfileMapVxlanEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanEncapVal.setStatus("current")


class _AlaDaUNPProfileMapVxlanVnid_Type(Unsigned32):
    """Custom type alaDaUNPProfileMapVxlanVnid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_AlaDaUNPProfileMapVxlanVnid_Type.__name__ = "Unsigned32"
_AlaDaUNPProfileMapVxlanVnid_Object = MibTableColumn
alaDaUNPProfileMapVxlanVnid = _AlaDaUNPProfileMapVxlanVnid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 2),
    _AlaDaUNPProfileMapVxlanVnid_Type()
)
alaDaUNPProfileMapVxlanVnid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanVnid.setStatus("current")


class _AlaDaUNPProfileMapVxlanFarEndIPList_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileMapVxlanFarEndIPList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfileMapVxlanFarEndIPList_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileMapVxlanFarEndIPList_Object = MibTableColumn
alaDaUNPProfileMapVxlanFarEndIPList = _AlaDaUNPProfileMapVxlanFarEndIPList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 3),
    _AlaDaUNPProfileMapVxlanFarEndIPList_Type()
)
alaDaUNPProfileMapVxlanFarEndIPList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanFarEndIPList.setStatus("current")
_AlaDaUNPProfileMapVxlanMulticastIPAddressType_Type = InetAddressType
_AlaDaUNPProfileMapVxlanMulticastIPAddressType_Object = MibTableColumn
alaDaUNPProfileMapVxlanMulticastIPAddressType = _AlaDaUNPProfileMapVxlanMulticastIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 4),
    _AlaDaUNPProfileMapVxlanMulticastIPAddressType_Type()
)
alaDaUNPProfileMapVxlanMulticastIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanMulticastIPAddressType.setStatus("current")
_AlaDaUNPProfileMapVxlanMulticastIPAddress_Type = InetAddress
_AlaDaUNPProfileMapVxlanMulticastIPAddress_Object = MibTableColumn
alaDaUNPProfileMapVxlanMulticastIPAddress = _AlaDaUNPProfileMapVxlanMulticastIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 5),
    _AlaDaUNPProfileMapVxlanMulticastIPAddress_Type()
)
alaDaUNPProfileMapVxlanMulticastIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanMulticastIPAddress.setStatus("current")


class _AlaDaUNPProfileMapVxlanVlanXlation_Type(Integer32):
    """Custom type alaDaUNPProfileMapVxlanVlanXlation based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPProfileMapVxlanVlanXlation_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapVxlanVlanXlation_Object = MibTableColumn
alaDaUNPProfileMapVxlanVlanXlation = _AlaDaUNPProfileMapVxlanVlanXlation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 6),
    _AlaDaUNPProfileMapVxlanVlanXlation_Type()
)
alaDaUNPProfileMapVxlanVlanXlation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanVlanXlation.setStatus("current")


class _AlaDaUNPProfileMapVxlanMulticastMode_Type(Integer32):
    """Custom type alaDaUNPProfileMapVxlanMulticastMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("headend", 1),
          ("tandem", 2),
          ("hybrid", 3))
    )


_AlaDaUNPProfileMapVxlanMulticastMode_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapVxlanMulticastMode_Object = MibTableColumn
alaDaUNPProfileMapVxlanMulticastMode = _AlaDaUNPProfileMapVxlanMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 7),
    _AlaDaUNPProfileMapVxlanMulticastMode_Type()
)
alaDaUNPProfileMapVxlanMulticastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanMulticastMode.setStatus("current")
_AlaDaUNPProfileMapVxlanRowStatus_Type = RowStatus
_AlaDaUNPProfileMapVxlanRowStatus_Object = MibTableColumn
alaDaUNPProfileMapVxlanRowStatus = _AlaDaUNPProfileMapVxlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 8),
    _AlaDaUNPProfileMapVxlanRowStatus_Type()
)
alaDaUNPProfileMapVxlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanRowStatus.setStatus("current")


class _AlaDaUNPProfileMapVxlanMacOrchestration_Type(Integer32):
    """Custom type alaDaUNPProfileMapVxlanMacOrchestration based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapVxlanMacOrchestration_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapVxlanMacOrchestration_Object = MibTableColumn
alaDaUNPProfileMapVxlanMacOrchestration = _AlaDaUNPProfileMapVxlanMacOrchestration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 9),
    _AlaDaUNPProfileMapVxlanMacOrchestration_Type()
)
alaDaUNPProfileMapVxlanMacOrchestration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanMacOrchestration.setStatus("current")


class _AlaDaUNPProfileMapVxlanRemoveIngressTag_Type(Integer32):
    """Custom type alaDaUNPProfileMapVxlanRemoveIngressTag based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapVxlanRemoveIngressTag_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapVxlanRemoveIngressTag_Object = MibTableColumn
alaDaUNPProfileMapVxlanRemoveIngressTag = _AlaDaUNPProfileMapVxlanRemoveIngressTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 10),
    _AlaDaUNPProfileMapVxlanRemoveIngressTag_Type()
)
alaDaUNPProfileMapVxlanRemoveIngressTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanRemoveIngressTag.setStatus("current")


class _AlaDaUNPProfileMapVxlanTcpMss_Type(Integer32):
    """Custom type alaDaUNPProfileMapVxlanTcpMss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1410),
    )


_AlaDaUNPProfileMapVxlanTcpMss_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapVxlanTcpMss_Object = MibTableColumn
alaDaUNPProfileMapVxlanTcpMss = _AlaDaUNPProfileMapVxlanTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 11),
    _AlaDaUNPProfileMapVxlanTcpMss_Type()
)
alaDaUNPProfileMapVxlanTcpMss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanTcpMss.setStatus("current")
_AlaDaUNPProfileMapVxlanTcpMssOverlayProfile_Type = SnmpAdminString
_AlaDaUNPProfileMapVxlanTcpMssOverlayProfile_Object = MibTableColumn
alaDaUNPProfileMapVxlanTcpMssOverlayProfile = _AlaDaUNPProfileMapVxlanTcpMssOverlayProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 63, 1, 12),
    _AlaDaUNPProfileMapVxlanTcpMssOverlayProfile_Type()
)
alaDaUNPProfileMapVxlanTcpMssOverlayProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanTcpMssOverlayProfile.setStatus("current")
_AlaDaUNPProfileMapStaticTable_Object = MibTable
alaDaUNPProfileMapStaticTable = _AlaDaUNPProfileMapStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 64)
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapStaticTable.setStatus("current")
_AlaDaUNPProfileMapStaticEntry_Object = MibTableRow
alaDaUNPProfileMapStaticEntry = _AlaDaUNPProfileMapStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 64, 1)
)
alaDaUNPProfileMapStaticEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapStaticEntry.setStatus("current")
_AlaDaUNPProfileMapStaticEncapVal_Type = TmnxEncapVal
_AlaDaUNPProfileMapStaticEncapVal_Object = MibTableColumn
alaDaUNPProfileMapStaticEncapVal = _AlaDaUNPProfileMapStaticEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 64, 1, 1),
    _AlaDaUNPProfileMapStaticEncapVal_Type()
)
alaDaUNPProfileMapStaticEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapStaticEncapVal.setStatus("current")
_AlaDaUNPProfileMapStaticServiceID_Type = Unsigned32
_AlaDaUNPProfileMapStaticServiceID_Object = MibTableColumn
alaDaUNPProfileMapStaticServiceID = _AlaDaUNPProfileMapStaticServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 64, 1, 2),
    _AlaDaUNPProfileMapStaticServiceID_Type()
)
alaDaUNPProfileMapStaticServiceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapStaticServiceID.setStatus("current")
_AlaDaUNPProfileMapStaticRowStatus_Type = RowStatus
_AlaDaUNPProfileMapStaticRowStatus_Object = MibTableColumn
alaDaUNPProfileMapStaticRowStatus = _AlaDaUNPProfileMapStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 64, 1, 3),
    _AlaDaUNPProfileMapStaticRowStatus_Type()
)
alaDaUNPProfileMapStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapStaticRowStatus.setStatus("current")
_AlaDaUNPCustDomainMacIpRuleTable_Object = MibTable
alaDaUNPCustDomainMacIpRuleTable = _AlaDaUNPCustDomainMacIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleTable.setStatus("current")
_AlaDaUNPCustDomainMacIpRuleEntry_Object = MibTableRow
alaDaUNPCustDomainMacIpRuleEntry = _AlaDaUNPCustDomainMacIpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1)
)
alaDaUNPCustDomainMacIpRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleMacAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleIpAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleIpAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleDomainId"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainMacIpRuleMacAddr_Type(MacAddress):
    """Custom type alaDaUNPCustDomainMacIpRuleMacAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AlaDaUNPCustDomainMacIpRuleMacAddr_Type.__name__ = "MacAddress"
_AlaDaUNPCustDomainMacIpRuleMacAddr_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleMacAddr = _AlaDaUNPCustDomainMacIpRuleMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 1),
    _AlaDaUNPCustDomainMacIpRuleMacAddr_Type()
)
alaDaUNPCustDomainMacIpRuleMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleMacAddr.setStatus("current")
_AlaDaUNPCustDomainMacIpRuleIpAddrType_Type = InetAddressType
_AlaDaUNPCustDomainMacIpRuleIpAddrType_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleIpAddrType = _AlaDaUNPCustDomainMacIpRuleIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 2),
    _AlaDaUNPCustDomainMacIpRuleIpAddrType_Type()
)
alaDaUNPCustDomainMacIpRuleIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleIpAddrType.setStatus("current")
_AlaDaUNPCustDomainMacIpRuleIpAddr_Type = InetAddress
_AlaDaUNPCustDomainMacIpRuleIpAddr_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleIpAddr = _AlaDaUNPCustDomainMacIpRuleIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 3),
    _AlaDaUNPCustDomainMacIpRuleIpAddr_Type()
)
alaDaUNPCustDomainMacIpRuleIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleIpAddr.setStatus("current")


class _AlaDaUNPCustDomainMacIpRuleDomainId_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacIpRuleDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDaUNPCustDomainMacIpRuleDomainId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacIpRuleDomainId_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleDomainId = _AlaDaUNPCustDomainMacIpRuleDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 4),
    _AlaDaUNPCustDomainMacIpRuleDomainId_Type()
)
alaDaUNPCustDomainMacIpRuleDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleDomainId.setStatus("current")


class _AlaDaUNPCustDomainMacIpRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacIpRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPCustDomainMacIpRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacIpRuleVlanTag_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleVlanTag = _AlaDaUNPCustDomainMacIpRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 5),
    _AlaDaUNPCustDomainMacIpRuleVlanTag_Type()
)
alaDaUNPCustDomainMacIpRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleVlanTag.setStatus("current")


class _AlaDaUNPCustDomainMacIpRuleProfile1_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacIpRuleProfile1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainMacIpRuleProfile1_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacIpRuleProfile1_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleProfile1 = _AlaDaUNPCustDomainMacIpRuleProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 6),
    _AlaDaUNPCustDomainMacIpRuleProfile1_Type()
)
alaDaUNPCustDomainMacIpRuleProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleProfile1.setStatus("current")


class _AlaDaUNPCustDomainMacIpRuleProfile2_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacIpRuleProfile2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainMacIpRuleProfile2_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacIpRuleProfile2_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleProfile2 = _AlaDaUNPCustDomainMacIpRuleProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 7),
    _AlaDaUNPCustDomainMacIpRuleProfile2_Type()
)
alaDaUNPCustDomainMacIpRuleProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleProfile2.setStatus("current")


class _AlaDaUNPCustDomainMacIpRuleProfile3_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacIpRuleProfile3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainMacIpRuleProfile3_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacIpRuleProfile3_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleProfile3 = _AlaDaUNPCustDomainMacIpRuleProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 8),
    _AlaDaUNPCustDomainMacIpRuleProfile3_Type()
)
alaDaUNPCustDomainMacIpRuleProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleProfile3.setStatus("current")
_AlaDaUNPCustDomainMacIpRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainMacIpRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleRowStatus = _AlaDaUNPCustDomainMacIpRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 9),
    _AlaDaUNPCustDomainMacIpRuleRowStatus_Type()
)
alaDaUNPCustDomainMacIpRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainMacIpRuleIpMaskType_Type(InetAddressType):
    """Custom type alaDaUNPCustDomainMacIpRuleIpMaskType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaUNPCustDomainMacIpRuleIpMaskType_Type.__name__ = "InetAddressType"
_AlaDaUNPCustDomainMacIpRuleIpMaskType_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleIpMaskType = _AlaDaUNPCustDomainMacIpRuleIpMaskType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 10),
    _AlaDaUNPCustDomainMacIpRuleIpMaskType_Type()
)
alaDaUNPCustDomainMacIpRuleIpMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleIpMaskType.setStatus("current")


class _AlaDaUNPCustDomainMacIpRuleIpMask_Type(InetAddress):
    """Custom type alaDaUNPCustDomainMacIpRuleIpMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPCustDomainMacIpRuleIpMask_Type.__name__ = "InetAddress"
_AlaDaUNPCustDomainMacIpRuleIpMask_Object = MibTableColumn
alaDaUNPCustDomainMacIpRuleIpMask = _AlaDaUNPCustDomainMacIpRuleIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 65, 1, 11),
    _AlaDaUNPCustDomainMacIpRuleIpMask_Type()
)
alaDaUNPCustDomainMacIpRuleIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleIpMask.setStatus("current")
_AlaDaUNPPortTemplateVlanTable_Object = MibTable
alaDaUNPPortTemplateVlanTable = _AlaDaUNPPortTemplateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 66)
)
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateVlanTable.setStatus("current")
_AlaDaUNPPortTemplateVlanEntry_Object = MibTableRow
alaDaUNPPortTemplateVlanEntry = _AlaDaUNPPortTemplateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 66, 1)
)
alaDaUNPPortTemplateVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateVlanVID"),
)
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateVlanEntry.setStatus("current")


class _AlaDaUNPPortTemplateVlanVID_Type(Unsigned32):
    """Custom type alaDaUNPPortTemplateVlanVID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPPortTemplateVlanVID_Type.__name__ = "Unsigned32"
_AlaDaUNPPortTemplateVlanVID_Object = MibTableColumn
alaDaUNPPortTemplateVlanVID = _AlaDaUNPPortTemplateVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 66, 1, 1),
    _AlaDaUNPPortTemplateVlanVID_Type()
)
alaDaUNPPortTemplateVlanVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateVlanVID.setStatus("current")
_AlaDaUNPPortTemplateVlanRowStatus_Type = RowStatus
_AlaDaUNPPortTemplateVlanRowStatus_Object = MibTableColumn
alaDaUNPPortTemplateVlanRowStatus = _AlaDaUNPPortTemplateVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 66, 1, 2),
    _AlaDaUNPPortTemplateVlanRowStatus_Type()
)
alaDaUNPPortTemplateVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateVlanRowStatus.setStatus("current")


class _AlaDaUNPPortTemplateVlanType_Type(Integer32):
    """Custom type alaDaUNPPortTemplateVlanType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unpQtag", 1),
          ("unpUntag", 2))
    )


_AlaDaUNPPortTemplateVlanType_Type.__name__ = "Integer32"
_AlaDaUNPPortTemplateVlanType_Object = MibTableColumn
alaDaUNPPortTemplateVlanType = _AlaDaUNPPortTemplateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 66, 1, 3),
    _AlaDaUNPPortTemplateVlanType_Type()
)
alaDaUNPPortTemplateVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateVlanType.setStatus("current")
_AlaDaUNPWlanConfiguration_ObjectIdentity = ObjectIdentity
alaDaUNPWlanConfiguration = _AlaDaUNPWlanConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 67)
)


class _AlaDaUNPWlanMode_Type(Integer32):
    """Custom type alaDaUNPWlanMode based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPWlanMode_Type.__name__ = "Integer32"
_AlaDaUNPWlanMode_Object = MibScalar
alaDaUNPWlanMode = _AlaDaUNPWlanMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 67, 1),
    _AlaDaUNPWlanMode_Type()
)
alaDaUNPWlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPWlanMode.setStatus("current")


class _AlaDaUNPWlanManagementVlan_Type(Unsigned32):
    """Custom type alaDaUNPWlanManagementVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPWlanManagementVlan_Type.__name__ = "Unsigned32"
_AlaDaUNPWlanManagementVlan_Object = MibScalar
alaDaUNPWlanManagementVlan = _AlaDaUNPWlanManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 67, 2),
    _AlaDaUNPWlanManagementVlan_Type()
)
alaDaUNPWlanManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPWlanManagementVlan.setStatus("current")


class _AlaDaUNPWlanAuthenticationFlag_Type(Integer32):
    """Custom type alaDaUNPWlanAuthenticationFlag based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPWlanAuthenticationFlag_Type.__name__ = "Integer32"
_AlaDaUNPWlanAuthenticationFlag_Object = MibScalar
alaDaUNPWlanAuthenticationFlag = _AlaDaUNPWlanAuthenticationFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 67, 3),
    _AlaDaUNPWlanAuthenticationFlag_Type()
)
alaDaUNPWlanAuthenticationFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPWlanAuthenticationFlag.setStatus("current")


class _AlaDaUNPWlanForceDefWlanProfile_Type(Integer32):
    """Custom type alaDaUNPWlanForceDefWlanProfile based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPWlanForceDefWlanProfile_Type.__name__ = "Integer32"
_AlaDaUNPWlanForceDefWlanProfile_Object = MibScalar
alaDaUNPWlanForceDefWlanProfile = _AlaDaUNPWlanForceDefWlanProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 67, 4),
    _AlaDaUNPWlanForceDefWlanProfile_Type()
)
alaDaUNPWlanForceDefWlanProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPWlanForceDefWlanProfile.setStatus("current")


class _AlaDaUNPWlanAuthServerDownFallback_Type(Integer32):
    """Custom type alaDaUNPWlanAuthServerDownFallback based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPWlanAuthServerDownFallback_Type.__name__ = "Integer32"
_AlaDaUNPWlanAuthServerDownFallback_Object = MibScalar
alaDaUNPWlanAuthServerDownFallback = _AlaDaUNPWlanAuthServerDownFallback_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 67, 5),
    _AlaDaUNPWlanAuthServerDownFallback_Type()
)
alaDaUNPWlanAuthServerDownFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPWlanAuthServerDownFallback.setStatus("current")


class _AlaDaUNPWlanSecurityLevel_Type(Integer32):
    """Custom type alaDaUNPWlanSecurityLevel based on Integer32"""
    defaultValue = 1

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
          ("macAuth", 2),
          ("dot1X", 3))
    )


_AlaDaUNPWlanSecurityLevel_Type.__name__ = "Integer32"
_AlaDaUNPWlanSecurityLevel_Object = MibScalar
alaDaUNPWlanSecurityLevel = _AlaDaUNPWlanSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 67, 6),
    _AlaDaUNPWlanSecurityLevel_Type()
)
alaDaUNPWlanSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPWlanSecurityLevel.setStatus("current")
_AlaDaUNPProfileMapL2GreTable_Object = MibTable
alaDaUNPProfileMapL2GreTable = _AlaDaUNPProfileMapL2GreTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68)
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreTable.setStatus("current")
_AlaDaUNPProfileL2GreEntry_Object = MibTableRow
alaDaUNPProfileL2GreEntry = _AlaDaUNPProfileL2GreEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68, 1)
)
alaDaUNPProfileL2GreEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPProfileL2GreEntry.setStatus("current")
_AlaDaUNPProfileMapL2GreEncapVal_Type = TmnxEncapVal
_AlaDaUNPProfileMapL2GreEncapVal_Object = MibTableColumn
alaDaUNPProfileMapL2GreEncapVal = _AlaDaUNPProfileMapL2GreEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68, 1, 1),
    _AlaDaUNPProfileMapL2GreEncapVal_Type()
)
alaDaUNPProfileMapL2GreEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreEncapVal.setStatus("current")


class _AlaDaUNPProfileMapL2GreVpnid_Type(Unsigned32):
    """Custom type alaDaUNPProfileMapL2GreVpnid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_AlaDaUNPProfileMapL2GreVpnid_Type.__name__ = "Unsigned32"
_AlaDaUNPProfileMapL2GreVpnid_Object = MibTableColumn
alaDaUNPProfileMapL2GreVpnid = _AlaDaUNPProfileMapL2GreVpnid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68, 1, 2),
    _AlaDaUNPProfileMapL2GreVpnid_Type()
)
alaDaUNPProfileMapL2GreVpnid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreVpnid.setStatus("current")


class _AlaDaUNPProfileMapL2GreFarEndIPAddressType_Type(InetAddressType):
    """Custom type alaDaUNPProfileMapL2GreFarEndIPAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AlaDaUNPProfileMapL2GreFarEndIPAddressType_Type.__name__ = "InetAddressType"
_AlaDaUNPProfileMapL2GreFarEndIPAddressType_Object = MibTableColumn
alaDaUNPProfileMapL2GreFarEndIPAddressType = _AlaDaUNPProfileMapL2GreFarEndIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68, 1, 3),
    _AlaDaUNPProfileMapL2GreFarEndIPAddressType_Type()
)
alaDaUNPProfileMapL2GreFarEndIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreFarEndIPAddressType.setStatus("current")


class _AlaDaUNPProfileMapL2GreFarEndIPAddress_Type(InetAddress):
    """Custom type alaDaUNPProfileMapL2GreFarEndIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_AlaDaUNPProfileMapL2GreFarEndIPAddress_Type.__name__ = "InetAddress"
_AlaDaUNPProfileMapL2GreFarEndIPAddress_Object = MibTableColumn
alaDaUNPProfileMapL2GreFarEndIPAddress = _AlaDaUNPProfileMapL2GreFarEndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68, 1, 4),
    _AlaDaUNPProfileMapL2GreFarEndIPAddress_Type()
)
alaDaUNPProfileMapL2GreFarEndIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreFarEndIPAddress.setStatus("current")


class _AlaDaUNPProfileMapL2GreFarEndIPList_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileMapL2GreFarEndIPList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfileMapL2GreFarEndIPList_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileMapL2GreFarEndIPList_Object = MibTableColumn
alaDaUNPProfileMapL2GreFarEndIPList = _AlaDaUNPProfileMapL2GreFarEndIPList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68, 1, 5),
    _AlaDaUNPProfileMapL2GreFarEndIPList_Type()
)
alaDaUNPProfileMapL2GreFarEndIPList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreFarEndIPList.setStatus("current")
_AlaDaUNPProfileMapL2GreRowStatus_Type = RowStatus
_AlaDaUNPProfileMapL2GreRowStatus_Object = MibTableColumn
alaDaUNPProfileMapL2GreRowStatus = _AlaDaUNPProfileMapL2GreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68, 1, 6),
    _AlaDaUNPProfileMapL2GreRowStatus_Type()
)
alaDaUNPProfileMapL2GreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreRowStatus.setStatus("current")


class _AlaDaUNPProfileMapL2GreVlanXlation_Type(Integer32):
    """Custom type alaDaUNPProfileMapL2GreVlanXlation based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapL2GreVlanXlation_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapL2GreVlanXlation_Object = MibTableColumn
alaDaUNPProfileMapL2GreVlanXlation = _AlaDaUNPProfileMapL2GreVlanXlation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68, 1, 7),
    _AlaDaUNPProfileMapL2GreVlanXlation_Type()
)
alaDaUNPProfileMapL2GreVlanXlation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreVlanXlation.setStatus("current")


class _AlaDaUNPProfileMapL2GreRemoveIngressTag_Type(Integer32):
    """Custom type alaDaUNPProfileMapL2GreRemoveIngressTag based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapL2GreRemoveIngressTag_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapL2GreRemoveIngressTag_Object = MibTableColumn
alaDaUNPProfileMapL2GreRemoveIngressTag = _AlaDaUNPProfileMapL2GreRemoveIngressTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 68, 1, 8),
    _AlaDaUNPProfileMapL2GreRemoveIngressTag_Type()
)
alaDaUNPProfileMapL2GreRemoveIngressTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreRemoveIngressTag.setStatus("current")
_AlaDaUNPL2GreFarEndIPListTable_Object = MibTable
alaDaUNPL2GreFarEndIPListTable = _AlaDaUNPL2GreFarEndIPListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 69)
)
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPListTable.setStatus("current")
_AlaDaUNPL2GreFarEndIPListEntry_Object = MibTableRow
alaDaUNPL2GreFarEndIPListEntry = _AlaDaUNPL2GreFarEndIPListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 69, 1)
)
alaDaUNPL2GreFarEndIPListEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPL2GreFarEndIPListName"),
)
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPListEntry.setStatus("current")


class _AlaDaUNPL2GreFarEndIPListName_Type(SnmpAdminString):
    """Custom type alaDaUNPL2GreFarEndIPListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPL2GreFarEndIPListName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPL2GreFarEndIPListName_Object = MibTableColumn
alaDaUNPL2GreFarEndIPListName = _AlaDaUNPL2GreFarEndIPListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 69, 1, 1),
    _AlaDaUNPL2GreFarEndIPListName_Type()
)
alaDaUNPL2GreFarEndIPListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPListName.setStatus("current")
_AlaDaUNPL2GreFarEndIPListIPAddressCount_Type = Unsigned32
_AlaDaUNPL2GreFarEndIPListIPAddressCount_Object = MibTableColumn
alaDaUNPL2GreFarEndIPListIPAddressCount = _AlaDaUNPL2GreFarEndIPListIPAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 69, 1, 2),
    _AlaDaUNPL2GreFarEndIPListIPAddressCount_Type()
)
alaDaUNPL2GreFarEndIPListIPAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPListIPAddressCount.setStatus("current")


class _AlaDaUNPL2GreFarEndIPListRemove_Type(Integer32):
    """Custom type alaDaUNPL2GreFarEndIPListRemove based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPL2GreFarEndIPListRemove_Type.__name__ = "Integer32"
_AlaDaUNPL2GreFarEndIPListRemove_Object = MibTableColumn
alaDaUNPL2GreFarEndIPListRemove = _AlaDaUNPL2GreFarEndIPListRemove_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 69, 1, 3),
    _AlaDaUNPL2GreFarEndIPListRemove_Type()
)
alaDaUNPL2GreFarEndIPListRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPListRemove.setStatus("current")
_AlaDaUNPL2GreFarEndIPAddressListTable_Object = MibTable
alaDaUNPL2GreFarEndIPAddressListTable = _AlaDaUNPL2GreFarEndIPAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 70)
)
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPAddressListTable.setStatus("current")
_AlaDaUNPL2GreFarEndIPAddressListEntry_Object = MibTableRow
alaDaUNPL2GreFarEndIPAddressListEntry = _AlaDaUNPL2GreFarEndIPAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 70, 1)
)
alaDaUNPL2GreFarEndIPAddressListEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPL2GreFarEndIPListName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPL2GreFarEndIPAddressListIPType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPL2GreFarEndIPAddressListIP"),
)
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPAddressListEntry.setStatus("current")


class _AlaDaUNPL2GreFarEndIPAddressListIPType_Type(InetAddressType):
    """Custom type alaDaUNPL2GreFarEndIPAddressListIPType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AlaDaUNPL2GreFarEndIPAddressListIPType_Type.__name__ = "InetAddressType"
_AlaDaUNPL2GreFarEndIPAddressListIPType_Object = MibTableColumn
alaDaUNPL2GreFarEndIPAddressListIPType = _AlaDaUNPL2GreFarEndIPAddressListIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 70, 1, 1),
    _AlaDaUNPL2GreFarEndIPAddressListIPType_Type()
)
alaDaUNPL2GreFarEndIPAddressListIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPAddressListIPType.setStatus("current")


class _AlaDaUNPL2GreFarEndIPAddressListIP_Type(InetAddress):
    """Custom type alaDaUNPL2GreFarEndIPAddressListIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_AlaDaUNPL2GreFarEndIPAddressListIP_Type.__name__ = "InetAddress"
_AlaDaUNPL2GreFarEndIPAddressListIP_Object = MibTableColumn
alaDaUNPL2GreFarEndIPAddressListIP = _AlaDaUNPL2GreFarEndIPAddressListIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 70, 1, 2),
    _AlaDaUNPL2GreFarEndIPAddressListIP_Type()
)
alaDaUNPL2GreFarEndIPAddressListIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPAddressListIP.setStatus("current")
_AlaDaUNPL2GreFarEndIPAddressListRowStatus_Type = RowStatus
_AlaDaUNPL2GreFarEndIPAddressListRowStatus_Object = MibTableColumn
alaDaUNPL2GreFarEndIPAddressListRowStatus = _AlaDaUNPL2GreFarEndIPAddressListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 70, 1, 3),
    _AlaDaUNPL2GreFarEndIPAddressListRowStatus_Type()
)
alaDaUNPL2GreFarEndIPAddressListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPAddressListRowStatus.setStatus("current")
_AlaDaUNPNetworkGroupTable_Object = MibTable
alaDaUNPNetworkGroupTable = _AlaDaUNPNetworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 71)
)
if mibBuilder.loadTexts:
    alaDaUNPNetworkGroupTable.setStatus("current")
_AlaDaUNPNetworkGroupEntry_Object = MibTableRow
alaDaUNPNetworkGroupEntry = _AlaDaUNPNetworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 71, 1)
)
alaDaUNPNetworkGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPNetworkGroupName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPNetworkGroupIpAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPNetworkGroupIpAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPNetworkGroupIpMask"),
)
if mibBuilder.loadTexts:
    alaDaUNPNetworkGroupEntry.setStatus("current")


class _AlaDaUNPNetworkGroupName_Type(SnmpAdminString):
    """Custom type alaDaUNPNetworkGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPNetworkGroupName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPNetworkGroupName_Object = MibTableColumn
alaDaUNPNetworkGroupName = _AlaDaUNPNetworkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 71, 1, 1),
    _AlaDaUNPNetworkGroupName_Type()
)
alaDaUNPNetworkGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPNetworkGroupName.setStatus("current")


class _AlaDaUNPNetworkGroupIpAddrType_Type(InetAddressType):
    """Custom type alaDaUNPNetworkGroupIpAddrType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaUNPNetworkGroupIpAddrType_Type.__name__ = "InetAddressType"
_AlaDaUNPNetworkGroupIpAddrType_Object = MibTableColumn
alaDaUNPNetworkGroupIpAddrType = _AlaDaUNPNetworkGroupIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 71, 1, 2),
    _AlaDaUNPNetworkGroupIpAddrType_Type()
)
alaDaUNPNetworkGroupIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPNetworkGroupIpAddrType.setStatus("current")


class _AlaDaUNPNetworkGroupIpAddr_Type(InetAddress):
    """Custom type alaDaUNPNetworkGroupIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPNetworkGroupIpAddr_Type.__name__ = "InetAddress"
_AlaDaUNPNetworkGroupIpAddr_Object = MibTableColumn
alaDaUNPNetworkGroupIpAddr = _AlaDaUNPNetworkGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 71, 1, 3),
    _AlaDaUNPNetworkGroupIpAddr_Type()
)
alaDaUNPNetworkGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPNetworkGroupIpAddr.setStatus("current")


class _AlaDaUNPNetworkGroupIpMask_Type(InetAddress):
    """Custom type alaDaUNPNetworkGroupIpMask based on InetAddress"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPNetworkGroupIpMask_Type.__name__ = "InetAddress"
_AlaDaUNPNetworkGroupIpMask_Object = MibTableColumn
alaDaUNPNetworkGroupIpMask = _AlaDaUNPNetworkGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 71, 1, 4),
    _AlaDaUNPNetworkGroupIpMask_Type()
)
alaDaUNPNetworkGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPNetworkGroupIpMask.setStatus("current")
_AlaDaUNPNetworkGroupRowStatus_Type = RowStatus
_AlaDaUNPNetworkGroupRowStatus_Object = MibTableColumn
alaDaUNPNetworkGroupRowStatus = _AlaDaUNPNetworkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 71, 1, 5),
    _AlaDaUNPNetworkGroupRowStatus_Type()
)
alaDaUNPNetworkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPNetworkGroupRowStatus.setStatus("current")
_AlaDaUNPRouterAuthUserGroupTable_Object = MibTable
alaDaUNPRouterAuthUserGroupTable = _AlaDaUNPRouterAuthUserGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 72)
)
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthUserGroupTable.setStatus("current")
_AlaDaUNPRouterAuthUserGroupEntry_Object = MibTableRow
alaDaUNPRouterAuthUserGroupEntry = _AlaDaUNPRouterAuthUserGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 72, 1)
)
alaDaUNPRouterAuthUserGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationName"),
)
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthUserGroupEntry.setStatus("current")


class _AlaDaUNPRouterAuthenticationName_Type(SnmpAdminString):
    """Custom type alaDaUNPRouterAuthenticationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPRouterAuthenticationName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRouterAuthenticationName_Object = MibTableColumn
alaDaUNPRouterAuthenticationName = _AlaDaUNPRouterAuthenticationName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 72, 1, 1),
    _AlaDaUNPRouterAuthenticationName_Type()
)
alaDaUNPRouterAuthenticationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationName.setStatus("current")


class _AlaDaUNPRouterAuthenticationSrcGroup_Type(SnmpAdminString):
    """Custom type alaDaUNPRouterAuthenticationSrcGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPRouterAuthenticationSrcGroup_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRouterAuthenticationSrcGroup_Object = MibTableColumn
alaDaUNPRouterAuthenticationSrcGroup = _AlaDaUNPRouterAuthenticationSrcGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 72, 1, 2),
    _AlaDaUNPRouterAuthenticationSrcGroup_Type()
)
alaDaUNPRouterAuthenticationSrcGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationSrcGroup.setStatus("current")


class _AlaDaUNPRouterAuthenticationDestGroup_Type(SnmpAdminString):
    """Custom type alaDaUNPRouterAuthenticationDestGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPRouterAuthenticationDestGroup_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRouterAuthenticationDestGroup_Object = MibTableColumn
alaDaUNPRouterAuthenticationDestGroup = _AlaDaUNPRouterAuthenticationDestGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 72, 1, 3),
    _AlaDaUNPRouterAuthenticationDestGroup_Type()
)
alaDaUNPRouterAuthenticationDestGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationDestGroup.setStatus("current")
_AlaDaUNPRouterAuthenticationRowStatus_Type = RowStatus
_AlaDaUNPRouterAuthenticationRowStatus_Object = MibTableColumn
alaDaUNPRouterAuthenticationRowStatus = _AlaDaUNPRouterAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 72, 1, 4),
    _AlaDaUNPRouterAuthenticationRowStatus_Type()
)
alaDaUNPRouterAuthenticationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationRowStatus.setStatus("current")
_AlaDaUNPRouterAuthenticationConfig_ObjectIdentity = ObjectIdentity
alaDaUNPRouterAuthenticationConfig = _AlaDaUNPRouterAuthenticationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 73)
)


class _AlaDaUNPRouterAuthCpProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPRouterAuthCpProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaDaUNPRouterAuthCpProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRouterAuthCpProfileName_Object = MibScalar
alaDaUNPRouterAuthCpProfileName = _AlaDaUNPRouterAuthCpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 73, 1),
    _AlaDaUNPRouterAuthCpProfileName_Type()
)
alaDaUNPRouterAuthCpProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthCpProfileName.setStatus("current")
_AlaDaUNPRouterAuthenticationFlushTable_Object = MibTable
alaDaUNPRouterAuthenticationFlushTable = _AlaDaUNPRouterAuthenticationFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 74)
)
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushTable.setStatus("current")
_AlaDaUNPRouterAuthenticationFlushEntry_Object = MibTableRow
alaDaUNPRouterAuthenticationFlushEntry = _AlaDaUNPRouterAuthenticationFlushEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 74, 1)
)
alaDaUNPRouterAuthenticationFlushEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationFlushIndex"),
)
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushEntry.setStatus("current")


class _AlaDaUNPRouterAuthenticationFlushIndex_Type(Integer32):
    """Custom type alaDaUNPRouterAuthenticationFlushIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaDaUNPRouterAuthenticationFlushIndex_Type.__name__ = "Integer32"
_AlaDaUNPRouterAuthenticationFlushIndex_Object = MibTableColumn
alaDaUNPRouterAuthenticationFlushIndex = _AlaDaUNPRouterAuthenticationFlushIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 74, 1, 1),
    _AlaDaUNPRouterAuthenticationFlushIndex_Type()
)
alaDaUNPRouterAuthenticationFlushIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushIndex.setStatus("current")


class _AlaDaUNPRouterAuthenticationFlushComplete_Type(Integer32):
    """Custom type alaDaUNPRouterAuthenticationFlushComplete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("all", 2))
    )


_AlaDaUNPRouterAuthenticationFlushComplete_Type.__name__ = "Integer32"
_AlaDaUNPRouterAuthenticationFlushComplete_Object = MibTableColumn
alaDaUNPRouterAuthenticationFlushComplete = _AlaDaUNPRouterAuthenticationFlushComplete_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 74, 1, 2),
    _AlaDaUNPRouterAuthenticationFlushComplete_Type()
)
alaDaUNPRouterAuthenticationFlushComplete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushComplete.setStatus("current")


class _AlaDaUNPRouterAuthenticationFlushUserGroupName_Type(SnmpAdminString):
    """Custom type alaDaUNPRouterAuthenticationFlushUserGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPRouterAuthenticationFlushUserGroupName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRouterAuthenticationFlushUserGroupName_Object = MibTableColumn
alaDaUNPRouterAuthenticationFlushUserGroupName = _AlaDaUNPRouterAuthenticationFlushUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 74, 1, 3),
    _AlaDaUNPRouterAuthenticationFlushUserGroupName_Type()
)
alaDaUNPRouterAuthenticationFlushUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushUserGroupName.setStatus("current")


class _AlaDaUNPRouterAuthenticationFlushType_Type(Integer32):
    """Custom type alaDaUNPRouterAuthenticationFlushType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cp", 1),
          ("ip", 2))
    )


_AlaDaUNPRouterAuthenticationFlushType_Type.__name__ = "Integer32"
_AlaDaUNPRouterAuthenticationFlushType_Object = MibTableColumn
alaDaUNPRouterAuthenticationFlushType = _AlaDaUNPRouterAuthenticationFlushType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 74, 1, 4),
    _AlaDaUNPRouterAuthenticationFlushType_Type()
)
alaDaUNPRouterAuthenticationFlushType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushType.setStatus("current")


class _AlaDaUNPRouterAuthenticationFlushUserName_Type(SnmpAdminString):
    """Custom type alaDaUNPRouterAuthenticationFlushUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPRouterAuthenticationFlushUserName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRouterAuthenticationFlushUserName_Object = MibTableColumn
alaDaUNPRouterAuthenticationFlushUserName = _AlaDaUNPRouterAuthenticationFlushUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 74, 1, 5),
    _AlaDaUNPRouterAuthenticationFlushUserName_Type()
)
alaDaUNPRouterAuthenticationFlushUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushUserName.setStatus("current")


class _AlaDaUNPRouterAuthenticationFlushIpAddressType_Type(InetAddressType):
    """Custom type alaDaUNPRouterAuthenticationFlushIpAddressType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaUNPRouterAuthenticationFlushIpAddressType_Type.__name__ = "InetAddressType"
_AlaDaUNPRouterAuthenticationFlushIpAddressType_Object = MibTableColumn
alaDaUNPRouterAuthenticationFlushIpAddressType = _AlaDaUNPRouterAuthenticationFlushIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 74, 1, 6),
    _AlaDaUNPRouterAuthenticationFlushIpAddressType_Type()
)
alaDaUNPRouterAuthenticationFlushIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushIpAddressType.setStatus("current")
_AlaDaUNPRouterAuthenticationFlushIpAddress_Type = InetAddress
_AlaDaUNPRouterAuthenticationFlushIpAddress_Object = MibTableColumn
alaDaUNPRouterAuthenticationFlushIpAddress = _AlaDaUNPRouterAuthenticationFlushIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 74, 1, 7),
    _AlaDaUNPRouterAuthenticationFlushIpAddress_Type()
)
alaDaUNPRouterAuthenticationFlushIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushIpAddress.setStatus("current")
_AlaDaUNPPortProfileTable_Object = MibTable
alaDaUNPPortProfileTable = _AlaDaUNPPortProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 75)
)
if mibBuilder.loadTexts:
    alaDaUNPPortProfileTable.setStatus("current")
_AlaDaUNPPortProfileEntry_Object = MibTableRow
alaDaUNPPortProfileEntry = _AlaDaUNPPortProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 75, 1)
)
alaDaUNPPortProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortIfIndex"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPPortProfileEntry.setStatus("current")


class _AlaDaUNPPortProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPPortProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortProfileName_Object = MibTableColumn
alaDaUNPPortProfileName = _AlaDaUNPPortProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 75, 1, 1),
    _AlaDaUNPPortProfileName_Type()
)
alaDaUNPPortProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPPortProfileName.setStatus("current")
_AlaDaUNPPortProfileRowStatus_Type = RowStatus
_AlaDaUNPPortProfileRowStatus_Object = MibTableColumn
alaDaUNPPortProfileRowStatus = _AlaDaUNPPortProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 75, 1, 2),
    _AlaDaUNPPortProfileRowStatus_Type()
)
alaDaUNPPortProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortProfileRowStatus.setStatus("current")
_AlaDaUNPPortTemplateProfileTable_Object = MibTable
alaDaUNPPortTemplateProfileTable = _AlaDaUNPPortTemplateProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 76)
)
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateProfileTable.setStatus("current")
_AlaDaUNPPortTemplateProfileEntry_Object = MibTableRow
alaDaUNPPortTemplateProfileEntry = _AlaDaUNPPortTemplateProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 76, 1)
)
alaDaUNPPortTemplateProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateProfileEntry.setStatus("current")


class _AlaDaUNPPortTemplateProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortTemplateProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPPortTemplateProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortTemplateProfileName_Object = MibTableColumn
alaDaUNPPortTemplateProfileName = _AlaDaUNPPortTemplateProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 76, 1, 1),
    _AlaDaUNPPortTemplateProfileName_Type()
)
alaDaUNPPortTemplateProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateProfileName.setStatus("current")
_AlaDaUNPPortTemplateProfileRowStatus_Type = RowStatus
_AlaDaUNPPortTemplateProfileRowStatus_Object = MibTableColumn
alaDaUNPPortTemplateProfileRowStatus = _AlaDaUNPPortTemplateProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 76, 1, 2),
    _AlaDaUNPPortTemplateProfileRowStatus_Type()
)
alaDaUNPPortTemplateProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateProfileRowStatus.setStatus("current")
_AlaDaUnpRouterAuthenticationUserTable_Object = MibTable
alaDaUnpRouterAuthenticationUserTable = _AlaDaUnpRouterAuthenticationUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77)
)
if mibBuilder.loadTexts:
    alaDaUnpRouterAuthenticationUserTable.setStatus("deprecated")
_AlaDaUnpRouterAuthenticationUserEntry_Object = MibTableRow
alaDaUnpRouterAuthenticationUserEntry = _AlaDaUnpRouterAuthenticationUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1)
)
alaDaUnpRouterAuthenticationUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserIpType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserIpAddress"),
)
if mibBuilder.loadTexts:
    alaDaUnpRouterAuthenticationUserEntry.setStatus("deprecated")


class _AlaDaUNPRouterAuthenticationUserIpType_Type(InetAddressType):
    """Custom type alaDaUNPRouterAuthenticationUserIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDaUNPRouterAuthenticationUserIpType_Type.__name__ = "InetAddressType"
_AlaDaUNPRouterAuthenticationUserIpType_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserIpType = _AlaDaUNPRouterAuthenticationUserIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 1),
    _AlaDaUNPRouterAuthenticationUserIpType_Type()
)
alaDaUNPRouterAuthenticationUserIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserIpType.setStatus("deprecated")


class _AlaDaUNPRouterAuthenticationUserIpAddress_Type(InetAddress):
    """Custom type alaDaUNPRouterAuthenticationUserIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPRouterAuthenticationUserIpAddress_Type.__name__ = "InetAddress"
_AlaDaUNPRouterAuthenticationUserIpAddress_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserIpAddress = _AlaDaUNPRouterAuthenticationUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 2),
    _AlaDaUNPRouterAuthenticationUserIpAddress_Type()
)
alaDaUNPRouterAuthenticationUserIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserIpAddress.setStatus("deprecated")


class _AlaDaUNPRouterAuthenticationUserName_Type(SnmpAdminString):
    """Custom type alaDaUNPRouterAuthenticationUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPRouterAuthenticationUserName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRouterAuthenticationUserName_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserName = _AlaDaUNPRouterAuthenticationUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 3),
    _AlaDaUNPRouterAuthenticationUserName_Type()
)
alaDaUNPRouterAuthenticationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserName.setStatus("deprecated")


class _AlaDaUNPRouterAuthenticationUserDestinationGroup_Type(SnmpAdminString):
    """Custom type alaDaUNPRouterAuthenticationUserDestinationGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPRouterAuthenticationUserDestinationGroup_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRouterAuthenticationUserDestinationGroup_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserDestinationGroup = _AlaDaUNPRouterAuthenticationUserDestinationGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 4),
    _AlaDaUNPRouterAuthenticationUserDestinationGroup_Type()
)
alaDaUNPRouterAuthenticationUserDestinationGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserDestinationGroup.setStatus("deprecated")


class _AlaDaUNPRouterAuthenticationUserInterfaceName_Type(SnmpAdminString):
    """Custom type alaDaUNPRouterAuthenticationUserInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPRouterAuthenticationUserInterfaceName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRouterAuthenticationUserInterfaceName_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserInterfaceName = _AlaDaUNPRouterAuthenticationUserInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 5),
    _AlaDaUNPRouterAuthenticationUserInterfaceName_Type()
)
alaDaUNPRouterAuthenticationUserInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserInterfaceName.setStatus("deprecated")
_AlaDaUNPRouterAuthenticationUserVlan_Type = Unsigned32
_AlaDaUNPRouterAuthenticationUserVlan_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserVlan = _AlaDaUNPRouterAuthenticationUserVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 6),
    _AlaDaUNPRouterAuthenticationUserVlan_Type()
)
alaDaUNPRouterAuthenticationUserVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserVlan.setStatus("deprecated")


class _AlaDaUNPRouterAuthenticationUserAuthType_Type(Integer32):
    """Custom type alaDaUNPRouterAuthenticationUserAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("cp", 2))
    )


_AlaDaUNPRouterAuthenticationUserAuthType_Type.__name__ = "Integer32"
_AlaDaUNPRouterAuthenticationUserAuthType_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserAuthType = _AlaDaUNPRouterAuthenticationUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 7),
    _AlaDaUNPRouterAuthenticationUserAuthType_Type()
)
alaDaUNPRouterAuthenticationUserAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserAuthType.setStatus("deprecated")


class _AlaDaUNPRouterAuthenticationUserAuthStatus_Type(Integer32):
    """Custom type alaDaUNPRouterAuthenticationUserAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_AlaDaUNPRouterAuthenticationUserAuthStatus_Type.__name__ = "Integer32"
_AlaDaUNPRouterAuthenticationUserAuthStatus_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserAuthStatus = _AlaDaUNPRouterAuthenticationUserAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 8),
    _AlaDaUNPRouterAuthenticationUserAuthStatus_Type()
)
alaDaUNPRouterAuthenticationUserAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserAuthStatus.setStatus("deprecated")
_AlaDaUNPRouterAuthenticationUserLoginTime_Type = DateAndTime
_AlaDaUNPRouterAuthenticationUserLoginTime_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserLoginTime = _AlaDaUNPRouterAuthenticationUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 9),
    _AlaDaUNPRouterAuthenticationUserLoginTime_Type()
)
alaDaUNPRouterAuthenticationUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserLoginTime.setStatus("deprecated")
_AlaDaUNPRouterAuthenticationUserSessionRemainingTime_Type = Unsigned32
_AlaDaUNPRouterAuthenticationUserSessionRemainingTime_Object = MibTableColumn
alaDaUNPRouterAuthenticationUserSessionRemainingTime = _AlaDaUNPRouterAuthenticationUserSessionRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 77, 1, 10),
    _AlaDaUNPRouterAuthenticationUserSessionRemainingTime_Type()
)
alaDaUNPRouterAuthenticationUserSessionRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserSessionRemainingTime.setStatus("deprecated")
_AlaDaUNPRedirectAllowedWebServerTable_Object = MibTable
alaDaUNPRedirectAllowedWebServerTable = _AlaDaUNPRedirectAllowedWebServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 78)
)
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerTable.setStatus("current")
_AlaDaUNPRedirectAllowedWebServerEntry_Object = MibTableRow
alaDaUNPRedirectAllowedWebServerEntry = _AlaDaUNPRedirectAllowedWebServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 78, 1)
)
alaDaUNPRedirectAllowedWebServerEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerName"),
)
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerEntry.setStatus("current")


class _AlaDaUNPRedirectAllowedWebServerName_Type(SnmpAdminString):
    """Custom type alaDaUNPRedirectAllowedWebServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPRedirectAllowedWebServerName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRedirectAllowedWebServerName_Object = MibTableColumn
alaDaUNPRedirectAllowedWebServerName = _AlaDaUNPRedirectAllowedWebServerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 78, 1, 1),
    _AlaDaUNPRedirectAllowedWebServerName_Type()
)
alaDaUNPRedirectAllowedWebServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerName.setStatus("current")


class _AlaDaUNPRedirectAllowedWebServerIpAddressType_Type(InetAddressType):
    """Custom type alaDaUNPRedirectAllowedWebServerIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AlaDaUNPRedirectAllowedWebServerIpAddressType_Type.__name__ = "InetAddressType"
_AlaDaUNPRedirectAllowedWebServerIpAddressType_Object = MibTableColumn
alaDaUNPRedirectAllowedWebServerIpAddressType = _AlaDaUNPRedirectAllowedWebServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 78, 1, 2),
    _AlaDaUNPRedirectAllowedWebServerIpAddressType_Type()
)
alaDaUNPRedirectAllowedWebServerIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerIpAddressType.setStatus("current")
_AlaDaUNPRedirectAllowedWebServerIpAddress_Type = InetAddress
_AlaDaUNPRedirectAllowedWebServerIpAddress_Object = MibTableColumn
alaDaUNPRedirectAllowedWebServerIpAddress = _AlaDaUNPRedirectAllowedWebServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 78, 1, 3),
    _AlaDaUNPRedirectAllowedWebServerIpAddress_Type()
)
alaDaUNPRedirectAllowedWebServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerIpAddress.setStatus("current")


class _AlaDaUNPRedirectAllowedWebServerFQDN_Type(SnmpAdminString):
    """Custom type alaDaUNPRedirectAllowedWebServerFQDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlaDaUNPRedirectAllowedWebServerFQDN_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRedirectAllowedWebServerFQDN_Object = MibTableColumn
alaDaUNPRedirectAllowedWebServerFQDN = _AlaDaUNPRedirectAllowedWebServerFQDN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 78, 1, 4),
    _AlaDaUNPRedirectAllowedWebServerFQDN_Type()
)
alaDaUNPRedirectAllowedWebServerFQDN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerFQDN.setStatus("current")


class _AlaDaUNPRedirectAllowedWebServerFQDNResolvedTime_Type(SnmpAdminString):
    """Custom type alaDaUNPRedirectAllowedWebServerFQDNResolvedTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaDaUNPRedirectAllowedWebServerFQDNResolvedTime_Type.__name__ = "SnmpAdminString"
_AlaDaUNPRedirectAllowedWebServerFQDNResolvedTime_Object = MibTableColumn
alaDaUNPRedirectAllowedWebServerFQDNResolvedTime = _AlaDaUNPRedirectAllowedWebServerFQDNResolvedTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 78, 1, 5),
    _AlaDaUNPRedirectAllowedWebServerFQDNResolvedTime_Type()
)
alaDaUNPRedirectAllowedWebServerFQDNResolvedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerFQDNResolvedTime.setStatus("current")
_AlaDaUNPRedirectAllowedWebServerRowStatus_Type = RowStatus
_AlaDaUNPRedirectAllowedWebServerRowStatus_Object = MibTableColumn
alaDaUNPRedirectAllowedWebServerRowStatus = _AlaDaUNPRedirectAllowedWebServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 78, 1, 6),
    _AlaDaUNPRedirectAllowedWebServerRowStatus_Type()
)
alaDaUNPRedirectAllowedWebServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerRowStatus.setStatus("current")


class _AlaDaUNPRedirectAllowedWebServerIpAddrStatus_Type(Integer32):
    """Custom type alaDaUNPRedirectAllowedWebServerIpAddrStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("programmed", 1),
          ("notProgrammed", 2),
          ("notApplicable", 3))
    )


_AlaDaUNPRedirectAllowedWebServerIpAddrStatus_Type.__name__ = "Integer32"
_AlaDaUNPRedirectAllowedWebServerIpAddrStatus_Object = MibTableColumn
alaDaUNPRedirectAllowedWebServerIpAddrStatus = _AlaDaUNPRedirectAllowedWebServerIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 78, 1, 7),
    _AlaDaUNPRedirectAllowedWebServerIpAddrStatus_Type()
)
alaDaUNPRedirectAllowedWebServerIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerIpAddrStatus.setStatus("current")
_AlaDaUNPFQDNResolvedIPTable_Object = MibTable
alaDaUNPFQDNResolvedIPTable = _AlaDaUNPFQDNResolvedIPTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 79)
)
if mibBuilder.loadTexts:
    alaDaUNPFQDNResolvedIPTable.setStatus("current")
_AlaDaUNPFQDNResolvedIPEntry_Object = MibTableRow
alaDaUNPFQDNResolvedIPEntry = _AlaDaUNPFQDNResolvedIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 79, 1)
)
alaDaUNPFQDNResolvedIPEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPFQDNResolvedIPName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPFQDNResolvedIPAddressType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPFQDNResolvedIPAddress"),
)
if mibBuilder.loadTexts:
    alaDaUNPFQDNResolvedIPEntry.setStatus("current")


class _AlaDaUNPFQDNResolvedIPName_Type(SnmpAdminString):
    """Custom type alaDaUNPFQDNResolvedIPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlaDaUNPFQDNResolvedIPName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPFQDNResolvedIPName_Object = MibTableColumn
alaDaUNPFQDNResolvedIPName = _AlaDaUNPFQDNResolvedIPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 79, 1, 1),
    _AlaDaUNPFQDNResolvedIPName_Type()
)
alaDaUNPFQDNResolvedIPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPFQDNResolvedIPName.setStatus("current")


class _AlaDaUNPFQDNResolvedIPAddressType_Type(InetAddressType):
    """Custom type alaDaUNPFQDNResolvedIPAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AlaDaUNPFQDNResolvedIPAddressType_Type.__name__ = "InetAddressType"
_AlaDaUNPFQDNResolvedIPAddressType_Object = MibTableColumn
alaDaUNPFQDNResolvedIPAddressType = _AlaDaUNPFQDNResolvedIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 79, 1, 2),
    _AlaDaUNPFQDNResolvedIPAddressType_Type()
)
alaDaUNPFQDNResolvedIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPFQDNResolvedIPAddressType.setStatus("current")
_AlaDaUNPFQDNResolvedIPAddress_Type = InetAddress
_AlaDaUNPFQDNResolvedIPAddress_Object = MibTableColumn
alaDaUNPFQDNResolvedIPAddress = _AlaDaUNPFQDNResolvedIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 79, 1, 3),
    _AlaDaUNPFQDNResolvedIPAddress_Type()
)
alaDaUNPFQDNResolvedIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPFQDNResolvedIPAddress.setStatus("current")


class _AlaDaUNPFQDNResolvedIPAddressStatus_Type(Integer32):
    """Custom type alaDaUNPFQDNResolvedIPAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("programmed", 1),
          ("notProgrammed", 2))
    )


_AlaDaUNPFQDNResolvedIPAddressStatus_Type.__name__ = "Integer32"
_AlaDaUNPFQDNResolvedIPAddressStatus_Object = MibTableColumn
alaDaUNPFQDNResolvedIPAddressStatus = _AlaDaUNPFQDNResolvedIPAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 79, 1, 4),
    _AlaDaUNPFQDNResolvedIPAddressStatus_Type()
)
alaDaUNPFQDNResolvedIPAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPFQDNResolvedIPAddressStatus.setStatus("current")
_AlaDaUNPProfileMapVplsTable_Object = MibTable
alaDaUNPProfileMapVplsTable = _AlaDaUNPProfileMapVplsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 80)
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVplsTable.setStatus("current")
_AlaDaUNPProfileVplsEntry_Object = MibTableRow
alaDaUNPProfileVplsEntry = _AlaDaUNPProfileVplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 80, 1)
)
alaDaUNPProfileVplsEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUNPProfileVplsEntry.setStatus("current")
_AlaDaUNPProfileMapVplsEncapVal_Type = TmnxEncapVal
_AlaDaUNPProfileMapVplsEncapVal_Object = MibTableColumn
alaDaUNPProfileMapVplsEncapVal = _AlaDaUNPProfileMapVplsEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 80, 1, 1),
    _AlaDaUNPProfileMapVplsEncapVal_Type()
)
alaDaUNPProfileMapVplsEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVplsEncapVal.setStatus("current")


class _AlaDaUNPProfileMapVplsID_Type(Unsigned32):
    """Custom type alaDaUNPProfileMapVplsID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaDaUNPProfileMapVplsID_Type.__name__ = "Unsigned32"
_AlaDaUNPProfileMapVplsID_Object = MibTableColumn
alaDaUNPProfileMapVplsID = _AlaDaUNPProfileMapVplsID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 80, 1, 2),
    _AlaDaUNPProfileMapVplsID_Type()
)
alaDaUNPProfileMapVplsID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVplsID.setStatus("current")


class _AlaDaUNPProfileMapVplsLdpFarEndIPList_Type(SnmpAdminString):
    """Custom type alaDaUNPProfileMapVplsLdpFarEndIPList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPProfileMapVplsLdpFarEndIPList_Type.__name__ = "SnmpAdminString"
_AlaDaUNPProfileMapVplsLdpFarEndIPList_Object = MibTableColumn
alaDaUNPProfileMapVplsLdpFarEndIPList = _AlaDaUNPProfileMapVplsLdpFarEndIPList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 80, 1, 3),
    _AlaDaUNPProfileMapVplsLdpFarEndIPList_Type()
)
alaDaUNPProfileMapVplsLdpFarEndIPList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVplsLdpFarEndIPList.setStatus("current")


class _AlaDaUNPProfileMapVplsBgpVeID_Type(Unsigned32):
    """Custom type alaDaUNPProfileMapVplsBgpVeID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_AlaDaUNPProfileMapVplsBgpVeID_Type.__name__ = "Unsigned32"
_AlaDaUNPProfileMapVplsBgpVeID_Object = MibTableColumn
alaDaUNPProfileMapVplsBgpVeID = _AlaDaUNPProfileMapVplsBgpVeID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 80, 1, 4),
    _AlaDaUNPProfileMapVplsBgpVeID_Type()
)
alaDaUNPProfileMapVplsBgpVeID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVplsBgpVeID.setStatus("current")


class _AlaDaUNPProfileMapVplsVlanXlation_Type(Integer32):
    """Custom type alaDaUNPProfileMapVplsVlanXlation based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapVplsVlanXlation_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapVplsVlanXlation_Object = MibTableColumn
alaDaUNPProfileMapVplsVlanXlation = _AlaDaUNPProfileMapVplsVlanXlation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 80, 1, 5),
    _AlaDaUNPProfileMapVplsVlanXlation_Type()
)
alaDaUNPProfileMapVplsVlanXlation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVplsVlanXlation.setStatus("current")


class _AlaDaUNPProfileMapVplsRemoveIngressTag_Type(Integer32):
    """Custom type alaDaUNPProfileMapVplsRemoveIngressTag based on Integer32"""
    defaultValue = 2

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


_AlaDaUNPProfileMapVplsRemoveIngressTag_Type.__name__ = "Integer32"
_AlaDaUNPProfileMapVplsRemoveIngressTag_Object = MibTableColumn
alaDaUNPProfileMapVplsRemoveIngressTag = _AlaDaUNPProfileMapVplsRemoveIngressTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 80, 1, 6),
    _AlaDaUNPProfileMapVplsRemoveIngressTag_Type()
)
alaDaUNPProfileMapVplsRemoveIngressTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVplsRemoveIngressTag.setStatus("current")
_AlaDaUNPProfileMapVplsRowStatus_Type = RowStatus
_AlaDaUNPProfileMapVplsRowStatus_Object = MibTableColumn
alaDaUNPProfileMapVplsRowStatus = _AlaDaUNPProfileMapVplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 80, 1, 7),
    _AlaDaUNPProfileMapVplsRowStatus_Type()
)
alaDaUNPProfileMapVplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVplsRowStatus.setStatus("current")
_AlaDaUNPVplsFarEndIPListTable_Object = MibTable
alaDaUNPVplsFarEndIPListTable = _AlaDaUNPVplsFarEndIPListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 81)
)
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPListTable.setStatus("current")
_AlaDaUNPVplsFarEndIPListEntry_Object = MibTableRow
alaDaUNPVplsFarEndIPListEntry = _AlaDaUNPVplsFarEndIPListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 81, 1)
)
alaDaUNPVplsFarEndIPListEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVplsFarEndIPListName"),
)
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPListEntry.setStatus("current")


class _AlaDaUNPVplsFarEndIPListName_Type(SnmpAdminString):
    """Custom type alaDaUNPVplsFarEndIPListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPVplsFarEndIPListName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVplsFarEndIPListName_Object = MibTableColumn
alaDaUNPVplsFarEndIPListName = _AlaDaUNPVplsFarEndIPListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 81, 1, 1),
    _AlaDaUNPVplsFarEndIPListName_Type()
)
alaDaUNPVplsFarEndIPListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPListName.setStatus("current")
_AlaDaUNPVplsFarEndIPListIPAddressCount_Type = Unsigned32
_AlaDaUNPVplsFarEndIPListIPAddressCount_Object = MibTableColumn
alaDaUNPVplsFarEndIPListIPAddressCount = _AlaDaUNPVplsFarEndIPListIPAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 81, 1, 2),
    _AlaDaUNPVplsFarEndIPListIPAddressCount_Type()
)
alaDaUNPVplsFarEndIPListIPAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPListIPAddressCount.setStatus("current")


class _AlaDaUNPVplsFarEndIPListRemove_Type(Integer32):
    """Custom type alaDaUNPVplsFarEndIPListRemove based on Integer32"""
    defaultValue = 1

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


_AlaDaUNPVplsFarEndIPListRemove_Type.__name__ = "Integer32"
_AlaDaUNPVplsFarEndIPListRemove_Object = MibTableColumn
alaDaUNPVplsFarEndIPListRemove = _AlaDaUNPVplsFarEndIPListRemove_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 81, 1, 3),
    _AlaDaUNPVplsFarEndIPListRemove_Type()
)
alaDaUNPVplsFarEndIPListRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPListRemove.setStatus("current")
_AlaDaUNPVplsFarEndIPAddressListTable_Object = MibTable
alaDaUNPVplsFarEndIPAddressListTable = _AlaDaUNPVplsFarEndIPAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 82)
)
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPAddressListTable.setStatus("current")
_AlaDaUNPVplsFarEndIPAddressListEntry_Object = MibTableRow
alaDaUNPVplsFarEndIPAddressListEntry = _AlaDaUNPVplsFarEndIPAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 82, 1)
)
alaDaUNPVplsFarEndIPAddressListEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVplsFarEndIPListName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVplsFarEndIPAddressListIPType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVplsFarEndIPAddressListIP"),
)
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPAddressListEntry.setStatus("current")


class _AlaDaUNPVplsFarEndIPAddressListIPType_Type(InetAddressType):
    """Custom type alaDaUNPVplsFarEndIPAddressListIPType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AlaDaUNPVplsFarEndIPAddressListIPType_Type.__name__ = "InetAddressType"
_AlaDaUNPVplsFarEndIPAddressListIPType_Object = MibTableColumn
alaDaUNPVplsFarEndIPAddressListIPType = _AlaDaUNPVplsFarEndIPAddressListIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 82, 1, 1),
    _AlaDaUNPVplsFarEndIPAddressListIPType_Type()
)
alaDaUNPVplsFarEndIPAddressListIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPAddressListIPType.setStatus("current")
_AlaDaUNPVplsFarEndIPAddressListIP_Type = InetAddress
_AlaDaUNPVplsFarEndIPAddressListIP_Object = MibTableColumn
alaDaUNPVplsFarEndIPAddressListIP = _AlaDaUNPVplsFarEndIPAddressListIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 82, 1, 2),
    _AlaDaUNPVplsFarEndIPAddressListIP_Type()
)
alaDaUNPVplsFarEndIPAddressListIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPAddressListIP.setStatus("current")
_AlaDaUNPVplsFarEndIPAddressListRowStatus_Type = RowStatus
_AlaDaUNPVplsFarEndIPAddressListRowStatus_Object = MibTableColumn
alaDaUNPVplsFarEndIPAddressListRowStatus = _AlaDaUNPVplsFarEndIPAddressListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 82, 1, 3),
    _AlaDaUNPVplsFarEndIPAddressListRowStatus_Type()
)
alaDaUNPVplsFarEndIPAddressListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPAddressListRowStatus.setStatus("current")
_AlaDaUNPProfileTrustTaggedVlanTable_Object = MibTable
alaDaUNPProfileTrustTaggedVlanTable = _AlaDaUNPProfileTrustTaggedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 83)
)
if mibBuilder.loadTexts:
    alaDaUNPProfileTrustTaggedVlanTable.setStatus("current")
_AlaDaUNPProfileTrustTaggedVlanEntry_Object = MibTableRow
alaDaUNPProfileTrustTaggedVlanEntry = _AlaDaUNPProfileTrustTaggedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 83, 1)
)
alaDaUNPProfileTrustTaggedVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPProfileName"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPProfileTrustTaggedVlanIDStart"),
)
if mibBuilder.loadTexts:
    alaDaUNPProfileTrustTaggedVlanEntry.setStatus("current")


class _AlaDaUNPProfileTrustTaggedVlanIDStart_Type(Unsigned32):
    """Custom type alaDaUNPProfileTrustTaggedVlanIDStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDaUNPProfileTrustTaggedVlanIDStart_Type.__name__ = "Unsigned32"
_AlaDaUNPProfileTrustTaggedVlanIDStart_Object = MibTableColumn
alaDaUNPProfileTrustTaggedVlanIDStart = _AlaDaUNPProfileTrustTaggedVlanIDStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 83, 1, 1),
    _AlaDaUNPProfileTrustTaggedVlanIDStart_Type()
)
alaDaUNPProfileTrustTaggedVlanIDStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPProfileTrustTaggedVlanIDStart.setStatus("current")


class _AlaDaUNPProfileTrustTaggedVlanIDEnd_Type(Unsigned32):
    """Custom type alaDaUNPProfileTrustTaggedVlanIDEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDaUNPProfileTrustTaggedVlanIDEnd_Type.__name__ = "Unsigned32"
_AlaDaUNPProfileTrustTaggedVlanIDEnd_Object = MibTableColumn
alaDaUNPProfileTrustTaggedVlanIDEnd = _AlaDaUNPProfileTrustTaggedVlanIDEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 83, 1, 2),
    _AlaDaUNPProfileTrustTaggedVlanIDEnd_Type()
)
alaDaUNPProfileTrustTaggedVlanIDEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileTrustTaggedVlanIDEnd.setStatus("current")
_AlaDaUNPProfileTrustTaggedVlanRowStatus_Type = RowStatus
_AlaDaUNPProfileTrustTaggedVlanRowStatus_Object = MibTableColumn
alaDaUNPProfileTrustTaggedVlanRowStatus = _AlaDaUNPProfileTrustTaggedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 83, 1, 3),
    _AlaDaUNPProfileTrustTaggedVlanRowStatus_Type()
)
alaDaUNPProfileTrustTaggedVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPProfileTrustTaggedVlanRowStatus.setStatus("current")
_AlaDaUNPApModeMacOuiTable_Object = MibTable
alaDaUNPApModeMacOuiTable = _AlaDaUNPApModeMacOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 84)
)
if mibBuilder.loadTexts:
    alaDaUNPApModeMacOuiTable.setStatus("current")
_AlaDaUNPApModeMacOuiEntry_Object = MibTableRow
alaDaUNPApModeMacOuiEntry = _AlaDaUNPApModeMacOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 84, 1)
)
alaDaUNPApModeMacOuiEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPApModeMacOui"),
)
if mibBuilder.loadTexts:
    alaDaUNPApModeMacOuiEntry.setStatus("current")
_AlaDaUNPApModeMacOui_Type = MacOui
_AlaDaUNPApModeMacOui_Object = MibTableColumn
alaDaUNPApModeMacOui = _AlaDaUNPApModeMacOui_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 84, 1, 1),
    _AlaDaUNPApModeMacOui_Type()
)
alaDaUNPApModeMacOui.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPApModeMacOui.setStatus("current")
_AlaDaUNPApModeMacOuiRowStatus_Type = RowStatus
_AlaDaUNPApModeMacOuiRowStatus_Object = MibTableColumn
alaDaUNPApModeMacOuiRowStatus = _AlaDaUNPApModeMacOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 1, 84, 1, 2),
    _AlaDaUNPApModeMacOuiRowStatus_Type()
)
alaDaUNPApModeMacOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPApModeMacOuiRowStatus.setStatus("current")
_AlaIND1DaMIBConformance_ObjectIdentity = ObjectIdentity
alaIND1DaMIBConformance = _AlaIND1DaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2)
)
if mibBuilder.loadTexts:
    alaIND1DaMIBConformance.setStatus("current")
_AlaIND1DaMIBGroups_ObjectIdentity = ObjectIdentity
alaIND1DaMIBGroups = _AlaIND1DaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIND1DaMIBGroups.setStatus("current")

# Managed Objects groups

alaDaUserNetProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 1)
)
alaDaUserNetProfileGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileVlanID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileQosPolicyListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileSaaProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileMobileTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileMaxIngressBw"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileMaxEgressBw"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileMaxIngressDepth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileMaxEgressDepth"))
)
if mibBuilder.loadTexts:
    alaDaUserNetProfileGroup.setStatus("deprecated")

alaDaUNPIpNetRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 2)
)
alaDaUNPIpNetRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleGroup.setStatus("current")

alaDaUNPMacRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 3)
)
alaDaUNPMacRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacRuleGroup.setStatus("current")

alaDaUNPMacRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 4)
)
alaDaUNPMacRangeGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleHiAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacRangeGroup.setStatus("current")

alaDaUNPVlanTagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 5)
)
alaDaUNPVlanTagGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanTagRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanTagRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanTagRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPVlanTagGroup.setStatus("current")

alaDaMacUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 6)
)
alaDaMacUserGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaMacUserVlanID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaAuthenticationStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserUnpUsed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserLoginTimeStamp"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserAuthtype"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserClassificationSource"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserName"))
)
if mibBuilder.loadTexts:
    alaDaMacUserGroup.setStatus("current")

alaDaUNPPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 7)
)
alaDaUNPPortGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPPortIfIndex"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortDefaultProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortPassAltProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMacAuthFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortClassificationFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTrustTagStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPPortGroup.setStatus("current")

alaDaUNPGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 8)
)
alaDaUNPGlobalGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPDynamicVlanConfigFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownUnp"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownTimeout"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPDynamicVlanMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownUNPMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownTimeoutMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPDynamicProfileConfigFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPDynamicProfileConfigMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPReloadVsiTypeDB"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthSrvDownEdgeProfName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDowneEdgeProfTimeout"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeUserFlush"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNP8021XEdgeUserFlush"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacEdgeUserFlush"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPNoAuthEdgeUserFlush"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectPortBounce"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectPauseTimer"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectProxyServerPort"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectServerIPType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectServerIP"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthSrvDownVxlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthSrvDownVxlanProfileTimeout"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPForceL3Learning"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPForceL3LearningPortBounce"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownProfile3"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanUserFlush"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNP8021XPassThrough"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPApMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceModule"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceBase"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceMulticastMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceVlanXlation"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceMulticastGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceFarEndIpList"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownVoiceProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownVoiceProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownVoiceProfile3"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpv6Drop"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPDelayLearning"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownPortBounce"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacMobility"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEapolVersion"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPApModeSecurity"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceMulticastGroupIPType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceMulticastGroupIP"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMultiUntagSap"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerPollingInterval"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerRefresh"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceVplsSignaling"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceVplsLdpFarEndIPList"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceVplsBgpVeID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPServiceBvlanModulo"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPApModeType"))
)
if mibBuilder.loadTexts:
    alaDaUNPGlobalGroup.setStatus("current")

alaDaNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 9)
)
alaDaNotificationObjectGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpSourceIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpNativeVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMCLAGId"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpCommandType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpIpMask"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosRateLimitString"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthNumberOfUsersPassedAuthentication"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserSourceIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserSourceIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserDestinationIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserDestinationIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserAttempts"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthNumberOfUsersFailedAuthentication"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthNumberOfAuthenticatedUsers"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthNumberOfConfigUsed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMaxUserSupported"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMaxUserCurrentNumberOfUsers"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpHWResourceChassisId"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpHWResourceSlot"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpHWResourceTtiAllocated"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthMACAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthRADIUSServerIPType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthRADIUSServerIP"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthServerReplyMsg"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthFailureReason"))
)
if mibBuilder.loadTexts:
    alaDaNotificationObjectGroup.setStatus("current")

alaDaMacVlanUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 11)
)
alaDaMacVlanUserGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserAuthStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserUnpUsed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserLoginTimeStamp"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserAuthtype"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserClassificationSource"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserMCLagLearningLoc"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserRole"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserRoleSource"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserAuthFailReason"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserAuthRetryCount"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserClassifProfRule"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserRoleRule"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserRestAccessStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserLocPolicyStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserTimePolicyStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserCapPortalStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserQMRStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserAuthServerIpType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserAuthServerIpUsed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserAuthServerUsed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserServerMessage"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserRedirectionUrl"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserSIPCallType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserSIPMediaType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserUnpFromAuthServer"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserServiceID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserServiceSapIDIfIndex"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserServiceSapIDEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserVxlanVnid"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserSpbIsid"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserSpbBVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserKerberosStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserL2greVpnid"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserImplicitTrustTagSource"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserRadiusTrustVlanStr"))
)
if mibBuilder.loadTexts:
    alaDaMacVlanUserGroup.setStatus("current")

alaDaUnpCustomerDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 12)
)
alaDaUnpCustomerDomainGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUnpCustomerDomainDesc"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpCustomerDomainRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainGroup.setStatus("current")

alaDaSpbProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 13)
)
alaDaSpbProfileGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileQosPolicyListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileIsid"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileBVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileMulticastMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileSapVlanXlation"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileMobileTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileAFDConfig"))
)
if mibBuilder.loadTexts:
    alaDaSpbProfileGroup.setStatus("obsolete")

alaDaUNPCustDomainEvbGpIdRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 14)
)
alaDaUNPCustDomainEvbGpIdRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleVlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleVxlanProfileName"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleGroup.setStatus("current")

alaDaUNPCustDomainVlanTagRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 15)
)
alaDaUNPCustDomainVlanTagRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleVlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleTagPosition"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleVxlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleProfile3"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleGroup.setStatus("current")

alaDaUNPCustDomainIpNetRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 16)
)
alaDaUNPCustDomainIpNetRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleEdgeProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleVxlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleProfile3"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleGroup.setStatus("current")

alaDaUNPCustDomainMacRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 17)
)
alaDaUNPCustDomainMacRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleEdgeProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleVxlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleProfile3"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleGroup.setStatus("current")

alaDaUNPCustDomainMacRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 18)
)
alaDaUNPCustDomainMacRangeGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleHiAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleEdgeProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleVxlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleProfile3"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeGroup.setStatus("current")

alaDaUNPGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 19)
)
alaDaUNPGroupObjects.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPPortCustomerDomainId"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortPassAltSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortDefaultSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortDefaultEdgeProfName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMacPassEdgeProfName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XEdgeProfName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XAuthStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XTxPeriodStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XTxPeriod"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XSuppTimeoutStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XSuppTimeOut"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XMaxReqStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XMaxReq"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortGroupId"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortAaaProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortEdgeTemplate"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortRedirectPortBounce"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XFailurePolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XBypassStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMacAllowEap"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortAdminControlledDirections"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortAdminControlledOperDirections"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XPassAltUserNetProfName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XPassAltSpbProfName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XPassAltVxlanProfName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortPassAltVxlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortDefaultVxlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortAFDConfig"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMaxIngressBw"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMaxIngressBwSource"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMaxEgressBw"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMaxEgressBwSource"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMaxIngressDepth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMaxEgressDepth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortIngressSourceProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortEgressSourceProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortForceL3Learning"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortForceL3LearningPortBounce"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPort8021XPassAltProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortPortTemplateName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortDomainID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortAdminState"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortDynamicService"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortPVlanPortType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortL2Profile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortApMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortApModeSecurity"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortSwSuppSecureMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortBpduLldpLearn"))
)
if mibBuilder.loadTexts:
    alaDaUNPGroupObjects.setStatus("current")

alaDaSaaProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 20)
)
alaDaSaaProfileGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaSaaProfileLatencyThreshold"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSaaProfileJitterThreshold"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSaaProfileRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaSaaProfileGroup.setStatus("current")

alaDaCPortalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 21)
)
alaDaCPortalGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaCPortalRedirectUrlName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalSuccRedirectUrl"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProxyPort"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalPolicyListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalRetryCnt"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalAuthRealm"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalAuthPolicyListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalAuthRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalAuthUNPProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalAuthUNPProfileChange"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfSuccRedirectUrl"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfRetryCnt"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfAuthPolicyListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfAaaProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfDomainAuthPolicyListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfDomainAuthRealm"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfDomainRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalCustomization"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfUNPProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfUNPProfileChange"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalUNPProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalUNPProfileChange"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfDomainUNPProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalProfDomainUNPProfileChange"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalDHCPLeaseTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalDHCPRenewTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalDHCPRebindingTime"))
)
if mibBuilder.loadTexts:
    alaDaCPortalGroup.setStatus("current")

alaDaHICGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 22)
)
alaDaHICGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaHICStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICWebAgentDownloadUrl"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICCustomHttpProxyPort"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICBgPollInterval"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrFailMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrIpAddrType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrPort"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrKey"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrRole"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrConnection"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICAllowedIpAddrType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICAllowedIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICAllowedIpMaskType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICAllowedIpMask"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICAllowedRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrFailChangedPolicyName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICSvrFailRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICHostStatus"))
)
if mibBuilder.loadTexts:
    alaDaHICGroup.setStatus("current")

alaDaUNPEdgeTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 23)
)
alaDaUNPEdgeTemplateGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPETmpl8021XAuthStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmpl8021XTxPeriodStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmpl8021XTxPeriod"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmpl8021XSuppTimeoutStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmpl8021XSuppTimeOut"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmpl8021XMaxReqStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmpl8021XMaxReq"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmpl8021XPassAltEProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplMacAuthStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplMacPassAltEProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplClassifStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplDefEProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplGroupId"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplAaaProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplRedirectPortBounce"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplFailurePolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplBypassStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplMacAllowEap"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplAdminControlledDirections"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplTrustTagStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplForceL3Learning"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplForceL3LearningPortBounce"))
)
if mibBuilder.loadTexts:
    alaDaUNPEdgeTemplateGroup.setStatus("deprecated")

alaDaUNPEdgeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 24)
)
alaDaUNPEdgeProfileGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfQosPolicyList"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfLocationPolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfPeriodPolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfHICStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfCPortalAuth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfAuthStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfMobileTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfDHCPEnforcment"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfCPortalProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfRedirectStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfKerberosStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfMaxIngressBw"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfMaxEgressBw"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfMaxIngressDepth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfMaxEgressDepth"))
)
if mibBuilder.loadTexts:
    alaDaUNPEdgeProfileGroup.setStatus("deprecated")

alaDaUNPClassificationRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 25)
)
alaDaUNPClassificationRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPPortRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortRuleProfile3"))
)
if mibBuilder.loadTexts:
    alaDaUNPClassificationRuleGroup.setStatus("current")

alaDaUNPGroupIdEdgeClassifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 26)
)
alaDaUNPGroupIdEdgeClassifyGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPGroupRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPGroupRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPGroupRuleVlanTag"))
)
if mibBuilder.loadTexts:
    alaDaUNPGroupIdEdgeClassifyGroup.setStatus("deprecated")

alaDaUNPMacOuiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 27)
)
alaDaUNPMacOuiGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacOuiRuleEdgeProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacOuiRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacOuiRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacOuiRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacOuiRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacOuiRuleProfile3"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacOuiGroup.setStatus("current")

alaDaUNPEndPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 28)
)
alaDaUNPEndPointGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPEndPoinEdgeProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEndPoinRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEndPoinProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEndPoinProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEndPoinProfile3"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEndPoinVlanTag"))
)
if mibBuilder.loadTexts:
    alaDaUNPEndPointGroup.setStatus("current")

alaDaUNPAuthRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 29)
)
alaDaUNPAuthRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthRuleEdgeProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthRuleProfile3"))
)
if mibBuilder.loadTexts:
    alaDaUNPAuthRuleGroup.setStatus("current")

alaDaUNPRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 30)
)
alaDaUNPRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRulePrecedenceNum"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleEdgeProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRulePort"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRulePortHigh"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleGroupId"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleMacAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleMacRngLoaddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleMacRngHiaddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleMacOuiAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleEndPoin"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleAuthType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleIpMaskType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleIpMask"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleCustomerDomain"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleProfile3"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassifRuleDeviceType"))
)
if mibBuilder.loadTexts:
    alaDaUNPRuleGroup.setStatus("current")

alaDaUNPMacPortClassifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 31)
)
alaDaUNPMacPortClassifyGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacPortRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacPortRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacPortRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacPortRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacPortRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacPortRuleProfile3"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacPortClassifyGroup.setStatus("current")

alaDaUNPIpPortClassifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 32)
)
alaDaUNPIpPortClassifyGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleProfile3"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleMaskType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortRuleMask"))
)
if mibBuilder.loadTexts:
    alaDaUNPIpPortClassifyGroup.setStatus("current")

alaDaUNPMacIpClassifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 33)
)
alaDaUNPMacIpClassifyGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleProfile3"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleIpMaskType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpPortRuleIpMask"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacIpClassifyGroup.setStatus("current")

alaDaUNPMacClassifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 34)
)
alaDaUNPMacClassifyGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacGroupRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacGroupRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacGroupRuleVlanTag"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacClassifyGroup.setStatus("deprecated")

alaDaUNPIpAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 35)
)
alaDaUNPIpAddressGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPIpGroupRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpGroupRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpGroupRuleVlanTag"))
)
if mibBuilder.loadTexts:
    alaDaUNPIpAddressGroup.setStatus("deprecated")

alaDaUNPMacIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 36)
)
alaDaUNPMacIpGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpGroupRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpGroupRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpGroupRuleVlanTag"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacIpGroup.setStatus("deprecated")

alaDaUNPUserRoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 37)
)
alaDaUNPUserRoleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRolePrecedenceNum"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRolePolicyList"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRoleEdgeProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRoleAuthType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRolePostLoginStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRoleKerberosPostLoginStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRoleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRoleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRoleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRoleProfile3"))
)
if mibBuilder.loadTexts:
    alaDaUNPUserRoleGroup.setStatus("current")

alaDaUNPRestrictedRoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 38)
)
alaDaUNPRestrictedRoleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPRstrctedRolePolicyList"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRstrctedRoleRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPRestrictedRoleGroup.setStatus("current")

alaDaUNPVlanMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 39)
)
alaDaUNPVlanMappingGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanMapIdent"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanMapRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPVlanMappingGroup.setStatus("deprecated")

alaDaUNPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 40)
)
alaDaUNPGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUnpGroupDescription"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpGroupIdRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPGroup.setStatus("deprecated")

alaDaUNPEdgeFlushGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 41)
)
alaDaUNPEdgeFlushGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeFlushPortLow"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeFlushPortHigh"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeFlushType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgrFlushMac"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeFlushComplete"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeFlushProfile"))
)
if mibBuilder.loadTexts:
    alaDaUNPEdgeFlushGroup.setStatus("current")

alaDaUNPMacAddrsRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 42)
)
alaDaUNPMacAddrsRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRulesEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRulesRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRulesVlanTag"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacAddrsRuleGroup.setStatus("deprecated")

alaDaUNPMacRangesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 43)
)
alaDaUNPMacRangesGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeEndMacAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeVlanTag"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacRangesGroup.setStatus("deprecated")

alaDaUNPIpMaskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 44)
)
alaDaUNPIpMaskGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPIpMaskRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpMaskRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpMaskRuleVlanTag"))
)
if mibBuilder.loadTexts:
    alaDaUNPIpMaskGroup.setStatus("deprecated")

alaDaQMRGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 45)
)
alaDaQMRGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaQMRPage"),
        ("ALCATEL-IND1-DA-MIB", "alaDaQMRPath"),
        ("ALCATEL-IND1-DA-MIB", "alaDaQMRCustomHttpProxyPort"),
        ("ALCATEL-IND1-DA-MIB", "alaDaQMRPolicyList"),
        ("ALCATEL-IND1-DA-MIB", "alaDaQMRAllowedIpAddrType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaQMRAllowedIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaQMRAllowedIpMaskType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaQMRAllowedIpMask"),
        ("ALCATEL-IND1-DA-MIB", "alaDaQMRAllowedRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaQMRGroup.setStatus("current")

alaDaUNPValidityPeriodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 46)
)
alaDaUNPValidityPeriodGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodDays"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodDaysStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodMonths"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodMonthsStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodHour"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodHourStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodEndHour"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodInterval"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodIntervalStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodEndInterval"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodTimezone"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodTimezoneStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodActiveStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPValidityPeriodGroup.setStatus("current")

alaDaUNPLocationPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 47)
)
alaDaUNPLocationPolicyGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPLocationPolicyPort"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPLocationPolicyPortHigh"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPLocationPolicyPortStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPLocationPolicySystemName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPLocationPolicySystemLocation"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPLocationPolicyRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPLocationPolicyDomainId"))
)
if mibBuilder.loadTexts:
    alaDaUNPLocationPolicyGroup.setStatus("current")

alaDaUNPRedirectAllowedServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 48)
)
alaDaUNPRedirectAllowedServerGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedServerIPType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedServerIP"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedMaskIPType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedMaskIP"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedServerGroup.setStatus("current")

alaDaMacVlanUserExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 49)
)
alaDaMacVlanUserExtGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserExtAppName")
)
if mibBuilder.loadTexts:
    alaDaMacVlanUserExtGroup.setStatus("current")

alaDaUNPVxlanProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 50)
)
alaDaUNPVxlanProfileGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileVnid"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileQosPolicyListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileFarEndIPListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileMulticastIPAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileMulticastIPAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileSapVlanXlation"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileMobileTagStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileMulticastMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanProfileRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanProfileGroup.setStatus("obsolete")

alaDaUNPVxlanFlushGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 51)
)
alaDaUNPVxlanFlushGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFlushComplete"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFlushAuthType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFlushMacAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFlushSapIDIfIndex"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFlushSapIDEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFlushServiceID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFlushVxlanProfile"))
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanFlushGroup.setStatus("obsolete")

alaDaUNPVxlanFarEndIPListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 52)
)
alaDaUNPVxlanFarEndIPListGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFarEndIPListIPAddressCount"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFarEndIPListRemove"))
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPListGroup.setStatus("current")

alaDaUNPVxlanFarEndIPAddressListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 53)
)
alaDaUNPVxlanFarEndIPAddressListGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPVxlanFarEndIPAddressListRowStatus")
)
if mibBuilder.loadTexts:
    alaDaUNPVxlanFarEndIPAddressListGroup.setStatus("current")

alaDaUNPSpbFlushGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 54)
)
alaDaUNPSpbFlushGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPSpbFlushComplete"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPSpbFlushAuthType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPSpbFlushMacAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPSpbFlushSapIDIfIndex"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPSpbFlushSapIDEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPSpbFlushServiceID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPSpbFlushSpbProfile"))
)
if mibBuilder.loadTexts:
    alaDaUNPSpbFlushGroup.setStatus("obsolete")

alaDaKerberosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 55)
)
alaDaKerberosGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaKerberosGlobalMacMoveStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosGlobalInactivityTimer"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosGlobalPolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosGlobalPolicyStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosClientPktHwDiscardStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosServerPktHwDiscardStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosTotalClientPktRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosTotalServerPktRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosClientPktSwDiscardStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosServerPktSwDiscardStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosTotalASREQRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosTotalASREPRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosTotalTGSREQRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosTotalTGSREPRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosTotalErrorRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosGlobalClearStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosGlobalClearPortStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosGlobalServerTimeoutTimer"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPolicyName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPolicyStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPolicyRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserMac"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserPort"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserDomain"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserAuthState"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserPolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserLeftTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserState"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortClearStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortClientPktRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortServerPktRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortClientPktSwDiscardStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortServerPktSwDiscardStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortASREQRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortASREPRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortTGSREQRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortTGSREPRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosPortErrorRxStats"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUdpPort"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaKerberosGroup.setStatus("current")

alaDaUNPVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 56)
)
alaDaUNPVlanGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanRuleVlanTagPosition"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanRuleEdgeProf"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanRuleRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPVlanGroup.setStatus("current")

alaDaUNPPortVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 57)
)
alaDaUNPPortVlanGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPPortVlanRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortVlanType"))
)
if mibBuilder.loadTexts:
    alaDaUNPPortVlanGroup.setStatus("current")

alaDaUNPETmplVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 58)
)
alaDaUNPETmplVlanGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplVlanRowStatus")
)
if mibBuilder.loadTexts:
    alaDaUNPETmplVlanGroup.setStatus("current")

alaDaUNPUserFlushGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 59)
)
alaDaUNPUserFlushGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushComplete"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushAuthType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushMacAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushPortStart"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushPortEnd"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushSapIDIfIndex"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushSapIDEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushServiceID"))
)
if mibBuilder.loadTexts:
    alaDaUNPUserFlushGroup.setStatus("current")

alaDaUNPCustDomainRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 60)
)
alaDaUNPCustDomainRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainRuleProfile3"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainRuleRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainRuleGroup.setStatus("current")

alaDaUNPPortTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 61)
)
alaDaUNPPortTemplateGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateAdminState"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateDirection"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateDomainID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateClassification"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateTrustTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateDynamicService"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateDefaultProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateAAAProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateRedirectPortBounce"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplate8021XAuth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplate8021XAuthPassAlternate"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplate8021XAuthBypass"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplate8021XAuthFailPolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplate8021XAuthTxPeriod"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplate8021XAuthSuppTimeout"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplate8021XAuthMaxReq"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateMACAuth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateMACAuthPassAlternate"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateMACAuthAllowEAP"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateForceL3Learning"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateForceL3LearningPortBounce"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateL2Profile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateApMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateApModeSecurity"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateSwSuppSecureMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateBpduLldpLearn"))
)
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateGroup.setStatus("current")

alaDaUNPProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 62)
)
alaDaUNPProfileGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileAuthenticationFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMobileTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileCPortalAuthentication"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileRedirect"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileQoSPolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfilePeriodPolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileCPortalProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileLocationPolicy"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileSaaProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileInactivityInterval"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileKerberosAuthentication"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMaxIngressBandwidth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMaxEgressBandwidth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMaxIngressDepth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMaxEgressDepth"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileAFDConfig"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMacMobility"))
)
if mibBuilder.loadTexts:
    alaDaUNPProfileGroup.setStatus("current")

alaDaUNPProfileMapVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 63)
)
alaDaUNPProfileMapVlanGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVlanVlanID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVlanRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVlanGroup.setStatus("current")

alaDaUNPProfileMapSpbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 64)
)
alaDaUNPProfileMapSpbGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbIsid"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbBVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbMulticastMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbVlanXlation"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbIgmpSnooping"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbIgmpProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbMldSnooping"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbMldProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbRemoveIngressTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbETree"))
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapSpbGroup.setStatus("current")

alaDaUNPProfileMapVxlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 65)
)
alaDaUNPProfileMapVxlanGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanVnid"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanFarEndIPList"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanMulticastIPAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanMulticastIPAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanVlanXlation"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanMulticastMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanMacOrchestration"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanRemoveIngressTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanTcpMss"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanTcpMssOverlayProfile"))
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVxlanGroup.setStatus("current")

alaDaUNPProfileMapStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 66)
)
alaDaUNPProfileMapStaticGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapStaticEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapStaticServiceID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapStaticRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapStaticGroup.setStatus("current")

alaDaUNPCustDomainMacIpRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 67)
)
alaDaUNPCustDomainMacIpRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleProfile1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleProfile2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleProfile3"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleIpMaskType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleIpMask"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacIpRuleGroup.setStatus("current")

alaDaUNPPortTemplateVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 68)
)
alaDaUNPPortTemplateVlanGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateVlanRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateVlanType"))
)
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateVlanGroup.setStatus("current")

alaDaUNPWlanConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 69)
)
alaDaUNPWlanConfigurationGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPWlanMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPWlanManagementVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPWlanAuthenticationFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPWlanForceDefWlanProfile"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPWlanAuthServerDownFallback"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPWlanSecurityLevel"))
)
if mibBuilder.loadTexts:
    alaDaUNPWlanConfigurationGroup.setStatus("current")

alaDaUNPProfileMapL2GreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 70)
)
alaDaUNPProfileMapL2GreGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapL2GreEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapL2GreVpnid"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapL2GreFarEndIPAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapL2GreFarEndIPAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapL2GreFarEndIPList"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapL2GreRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapL2GreVlanXlation"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapL2GreRemoveIngressTag"))
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapL2GreGroup.setStatus("current")

alaDaUNPL2GreFarEndIPListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 71)
)
alaDaUNPL2GreFarEndIPListGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPL2GreFarEndIPListIPAddressCount"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPL2GreFarEndIPListRemove"))
)
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPListGroup.setStatus("current")

alaDaUNPL2GreFarEndIPAddressListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 72)
)
alaDaUNPL2GreFarEndIPAddressListGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPL2GreFarEndIPAddressListRowStatus")
)
if mibBuilder.loadTexts:
    alaDaUNPL2GreFarEndIPAddressListGroup.setStatus("current")

alaDaUNPNetworkGroupNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 73)
)
alaDaUNPNetworkGroupNameGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPNetworkGroupRowStatus")
)
if mibBuilder.loadTexts:
    alaDaUNPNetworkGroupNameGroup.setStatus("current")

alaDaUNPRouterAuthUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 74)
)
alaDaUNPRouterAuthUserGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationSrcGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationDestGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthUserGroup.setStatus("current")

alaDaUNPRouterAuthenticationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 75)
)
alaDaUNPRouterAuthenticationConfigGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthCpProfileName")
)
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationConfigGroup.setStatus("current")

alaDaUNPRouterAuthenticationFlushGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 76)
)
alaDaUNPRouterAuthenticationFlushGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationFlushComplete"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationFlushUserGroupName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationFlushType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationFlushUserName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationFlushIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationFlushIpAddress"))
)
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationFlushGroup.setStatus("current")

alaDaUNPPortProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 77)
)
alaDaUNPPortProfileGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortProfileRowStatus")
)
if mibBuilder.loadTexts:
    alaDaUNPPortProfileGroup.setStatus("current")

alaDaUNPPortTemplateProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 78)
)
alaDaUNPPortTemplateProfileGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateProfileRowStatus")
)
if mibBuilder.loadTexts:
    alaDaUNPPortTemplateProfileGroup.setStatus("current")

alaDaUNPRouterAuthenticationUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 79)
)
alaDaUNPRouterAuthenticationUserGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserDestinationGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserInterfaceName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserAuthType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserAuthStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserLoginTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationUserSessionRemainingTime"))
)
if mibBuilder.loadTexts:
    alaDaUNPRouterAuthenticationUserGroup.setStatus("current")

alaDaUNPRedirectAllowedWebServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 80)
)
alaDaUNPRedirectAllowedWebServerGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerFQDN"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerFQDNResolvedTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerIpAddrStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPRedirectAllowedWebServerGroup.setStatus("current")

alaDaUNPFQDNResolvedIPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 81)
)
alaDaUNPFQDNResolvedIPGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPFQDNResolvedIPAddressStatus")
)
if mibBuilder.loadTexts:
    alaDaUNPFQDNResolvedIPGroup.setStatus("current")

alaDaUNPProfileMapVplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 82)
)
alaDaUNPProfileMapVplsGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVplsEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVplsID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVplsLdpFarEndIPList"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVplsBgpVeID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVplsVlanXlation"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVplsRemoveIngressTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVplsRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPProfileMapVplsGroup.setStatus("current")

alaDaUNPVplsFarEndIPListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 83)
)
alaDaUNPVplsFarEndIPListGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPVplsFarEndIPListIPAddressCount"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVplsFarEndIPListRemove"))
)
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPListGroup.setStatus("current")

alaDaUNPVplsFarEndIPAddressListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 84)
)
alaDaUNPVplsFarEndIPAddressListGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPVplsFarEndIPAddressListRowStatus")
)
if mibBuilder.loadTexts:
    alaDaUNPVplsFarEndIPAddressListGroup.setStatus("current")

alaDaUNPProfileTrustTaggedVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 85)
)
alaDaUNPProfileTrustTaggedVlanGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileTrustTaggedVlanIDEnd"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileTrustTaggedVlanRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPProfileTrustTaggedVlanGroup.setStatus("current")

alaDaUNPApModeMacOuiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 86)
)
alaDaUNPApModeMacOuiGroup.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPApModeMacOuiRowStatus")
)
if mibBuilder.loadTexts:
    alaDaUNPApModeMacOuiGroup.setStatus("current")


# Notification objects

unpMcLagMacIgnored = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 1)
)
unpMcLagMacIgnored.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpSourceIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpNativeVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMCLAGId"))
)
if mibBuilder.loadTexts:
    unpMcLagMacIgnored.setStatus(
        "current"
    )

unpMcLagConfigInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 2)
)
unpMcLagConfigInconsistency.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUnpCommandType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpIpMask"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMCLAGId"))
)
if mibBuilder.loadTexts:
    unpMcLagConfigInconsistency.setStatus(
        "current"
    )

alaDaKerberosReqTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 3)
)
alaDaKerberosReqTimeoutTrap.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaKerberosIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserMac"))
)
if mibBuilder.loadTexts:
    alaDaKerberosReqTimeoutTrap.setStatus(
        "current"
    )

alaDaKerberosInactivityTimerExpiryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 4)
)
alaDaKerberosInactivityTimerExpiryTrap.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserMac"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosUserDomain"))
)
if mibBuilder.loadTexts:
    alaDaKerberosInactivityTimerExpiryTrap.setStatus(
        "current"
    )

alaDaKerberosRateLimitExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 5)
)
alaDaKerberosRateLimitExceed.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaKerberosRateLimitString")
)
if mibBuilder.loadTexts:
    alaDaKerberosRateLimitExceed.setStatus(
        "obsolete"
    )

alaDaRouterAuthUserPassedAuthThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 6)
)
alaDaRouterAuthUserPassedAuthThreshold.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthNumberOfUsersPassedAuthentication"))
)
if mibBuilder.loadTexts:
    alaDaRouterAuthUserPassedAuthThreshold.setStatus(
        "current"
    )

alaDaRouterAuthUserMaxRetryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 7)
)
alaDaRouterAuthUserMaxRetryFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserSourceIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserSourceIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserDestinationIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserDestinationIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserAttempts"))
)
if mibBuilder.loadTexts:
    alaDaRouterAuthUserMaxRetryFailed.setStatus(
        "current"
    )

alaDaRouterAuthUserFailedAuthThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 8)
)
alaDaRouterAuthUserFailedAuthThreshold.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthNumberOfUsersFailedAuthentication"))
)
if mibBuilder.loadTexts:
    alaDaRouterAuthUserFailedAuthThreshold.setStatus(
        "current"
    )

alaDaRouterAuthConfigThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 9)
)
alaDaRouterAuthConfigThresholdExceed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthNumberOfConfigUsed"))
)
if mibBuilder.loadTexts:
    alaDaRouterAuthConfigThresholdExceed.setStatus(
        "current"
    )

alaDaRouterAuthMaxCapacityReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 10)
)
alaDaRouterAuthMaxCapacityReached.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthNumberOfAuthenticatedUsers"))
)
if mibBuilder.loadTexts:
    alaDaRouterAuthMaxCapacityReached.setStatus(
        "current"
    )

alaDaUnpMaxUserExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 11)
)
alaDaUnpMaxUserExceeded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMaxUserSupported"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMaxUserCurrentNumberOfUsers"))
)
if mibBuilder.loadTexts:
    alaDaUnpMaxUserExceeded.setStatus(
        "current"
    )

alaDaUnpHWResourceExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 12)
)
alaDaUnpHWResourceExhaust.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpHWResourceChassisId"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpHWResourceSlot"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpHWResourceTtiAllocated"))
)
if mibBuilder.loadTexts:
    alaDaUnpHWResourceExhaust.setStatus(
        "current"
    )

alaDaUnpDnsServerNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 13)
)
alaDaUnpDnsServerNotReachable.setObjects(
    ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerName")
)
if mibBuilder.loadTexts:
    alaDaUnpDnsServerNotReachable.setStatus(
        "current"
    )

alaDaUnpUserAuthSupplicantFails = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 0, 14)
)
alaDaUnpUserAuthSupplicantFails.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortIfIndex"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthMACAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthRADIUSServerIPType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthRADIUSServerIP"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthServerReplyMsg"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpAuthFailureReason"))
)
if mibBuilder.loadTexts:
    alaDaUnpUserAuthSupplicantFails.setStatus(
        "current"
    )


# Notifications groups

alaDaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 1, 10)
)
alaDaNotificationsGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "unpMcLagMacIgnored"),
        ("ALCATEL-IND1-DA-MIB", "unpMcLagConfigInconsistency"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosReqTimeoutTrap"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosInactivityTimerExpiryTrap"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosRateLimitExceed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserPassedAuthThreshold"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserMaxRetryFailed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthUserFailedAuthThreshold"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthConfigThresholdExceed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaRouterAuthMaxCapacityReached"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMaxUserExceeded"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpHWResourceExhaust"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpDnsServerNotReachable"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpUserAuthSupplicantFails"))
)
if mibBuilder.loadTexts:
    alaDaNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaIND1DaMIBCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 68, 1, 2, 2)
)
alaIND1DaMIBCompliances.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanTagGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPGlobalGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaNotificationObjectGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaNotificationsGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpCustomerDomainGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSaaProfileGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaCPortalGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaHICGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeTemplateGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeProfileGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPClassificationRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPGroupIdEdgeClassifyGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacOuiGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEndPointGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacPortClassifyGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpPortClassifyGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpClassifyGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacClassifyGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpAddressGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacIpGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserRoleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRestrictedRoleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanMappingGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPEdgeFlushGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacAddrsRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangesGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpMaskGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaQMRGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPValidityPeriodGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPLocationPolicyGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedServerGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserExtGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaKerberosGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortVlanGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPETmplVlanGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPUserFlushGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVlanGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapSpbGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVxlanGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapStaticGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacIpRuleGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateVlanGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPWlanConfigurationGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapL2GreGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPNetworkGroupNameGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthUserGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationConfigGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRouterAuthenticationFlushGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortProfileGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTemplateProfileGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPRedirectAllowedWebServerGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPFQDNResolvedIPGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileMapVplsGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVplsFarEndIPListGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVplsFarEndIPAddressListGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPProfileTrustTaggedVlanGroup"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPApModeMacOuiGroup"))
)
if mibBuilder.loadTexts:
    alaIND1DaMIBCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DA-MIB",
    **{"AlaDaClassificationPolicyType": AlaDaClassificationPolicyType,
       "AlaDaAuthenticationType": AlaDaAuthenticationType,
       "AlaDaAuthenticationResult": AlaDaAuthenticationResult,
       "AlaDaMacLearntState": AlaDaMacLearntState,
       "AlaMultiChassisConfigStatus": AlaMultiChassisConfigStatus,
       "MacOui": MacOui,
       "alcatelIND1DaMIB": alcatelIND1DaMIB,
       "alaIND1DaMIBNotifications": alaIND1DaMIBNotifications,
       "unpMcLagMacIgnored": unpMcLagMacIgnored,
       "unpMcLagConfigInconsistency": unpMcLagConfigInconsistency,
       "alaDaKerberosReqTimeoutTrap": alaDaKerberosReqTimeoutTrap,
       "alaDaKerberosInactivityTimerExpiryTrap": alaDaKerberosInactivityTimerExpiryTrap,
       "alaDaKerberosRateLimitExceed": alaDaKerberosRateLimitExceed,
       "alaDaRouterAuthUserPassedAuthThreshold": alaDaRouterAuthUserPassedAuthThreshold,
       "alaDaRouterAuthUserMaxRetryFailed": alaDaRouterAuthUserMaxRetryFailed,
       "alaDaRouterAuthUserFailedAuthThreshold": alaDaRouterAuthUserFailedAuthThreshold,
       "alaDaRouterAuthConfigThresholdExceed": alaDaRouterAuthConfigThresholdExceed,
       "alaDaRouterAuthMaxCapacityReached": alaDaRouterAuthMaxCapacityReached,
       "alaDaUnpMaxUserExceeded": alaDaUnpMaxUserExceeded,
       "alaDaUnpHWResourceExhaust": alaDaUnpHWResourceExhaust,
       "alaDaUnpDnsServerNotReachable": alaDaUnpDnsServerNotReachable,
       "alaDaUnpUserAuthSupplicantFails": alaDaUnpUserAuthSupplicantFails,
       "alaIND1DaMIBObjects": alaIND1DaMIBObjects,
       "alaDaUserNetProfileTable": alaDaUserNetProfileTable,
       "alaDaUserNetProfileEntry": alaDaUserNetProfileEntry,
       "alaDaUserNetProfileName": alaDaUserNetProfileName,
       "alaDaUserNetProfileVlanID": alaDaUserNetProfileVlanID,
       "alaDaUserNetProfileRowStatus": alaDaUserNetProfileRowStatus,
       "alaDaUserNetProfileQosPolicyListName": alaDaUserNetProfileQosPolicyListName,
       "alaDaUserNetProfileMCLagConfigStatus": alaDaUserNetProfileMCLagConfigStatus,
       "alaDaUserNetProfileSaaProfileName": alaDaUserNetProfileSaaProfileName,
       "alaDaUserNetProfileMobileTag": alaDaUserNetProfileMobileTag,
       "alaDaUserNetProfileMaxIngressBw": alaDaUserNetProfileMaxIngressBw,
       "alaDaUserNetProfileMaxEgressBw": alaDaUserNetProfileMaxEgressBw,
       "alaDaUserNetProfileMaxIngressDepth": alaDaUserNetProfileMaxIngressDepth,
       "alaDaUserNetProfileMaxEgressDepth": alaDaUserNetProfileMaxEgressDepth,
       "alaDaUNPIpNetRuleTable": alaDaUNPIpNetRuleTable,
       "alaDaUNPIpNetRuleEntry": alaDaUNPIpNetRuleEntry,
       "alaDaUNPIpNetRuleAddrType": alaDaUNPIpNetRuleAddrType,
       "alaDaUNPIpNetRuleAddr": alaDaUNPIpNetRuleAddr,
       "alaDaUNPIpNetRuleMask": alaDaUNPIpNetRuleMask,
       "alaDaUNPIpNetRuleProfileName": alaDaUNPIpNetRuleProfileName,
       "alaDaUNPIpNetRuleVlanTag": alaDaUNPIpNetRuleVlanTag,
       "alaDaUNPIpNetRuleRowStatus": alaDaUNPIpNetRuleRowStatus,
       "alaDaUNPIpNetRuleMCLagConfigStatus": alaDaUNPIpNetRuleMCLagConfigStatus,
       "alaDaUNPMacRuleTable": alaDaUNPMacRuleTable,
       "alaDaUNPMacRuleEntry": alaDaUNPMacRuleEntry,
       "alaDaUNPMacRuleAddr": alaDaUNPMacRuleAddr,
       "alaDaUNPMacRuleProfileName": alaDaUNPMacRuleProfileName,
       "alaDaUNPMacRuleVlanTag": alaDaUNPMacRuleVlanTag,
       "alaDaUNPMacRuleRowStatus": alaDaUNPMacRuleRowStatus,
       "alaDaUNPMacRuleMCLagConfigStatus": alaDaUNPMacRuleMCLagConfigStatus,
       "alaDaUNPMacRangeRuleTable": alaDaUNPMacRangeRuleTable,
       "alaDaUNPMacRangeRuleEntry": alaDaUNPMacRangeRuleEntry,
       "alaDaUNPMacRangeRuleLoAddr": alaDaUNPMacRangeRuleLoAddr,
       "alaDaUNPMacRangeRuleHiAddr": alaDaUNPMacRangeRuleHiAddr,
       "alaDaUNPMacRangeRuleProfileName": alaDaUNPMacRangeRuleProfileName,
       "alaDaUNPMacRangeRuleVlanTag": alaDaUNPMacRangeRuleVlanTag,
       "alaDaUNPMacRangeRuleRowStatus": alaDaUNPMacRangeRuleRowStatus,
       "alaDaUNPMacRangeRuleMCLagConfigStatus": alaDaUNPMacRangeRuleMCLagConfigStatus,
       "alaDaUNPVlanTagRuleTable": alaDaUNPVlanTagRuleTable,
       "alaDaUNPVlanTagRuleEntry": alaDaUNPVlanTagRuleEntry,
       "alaDaUNPVlanTagRuleVlan": alaDaUNPVlanTagRuleVlan,
       "alaDaUNPVlanTagRuleProfileName": alaDaUNPVlanTagRuleProfileName,
       "alaDaUNPVlanTagRuleRowStatus": alaDaUNPVlanTagRuleRowStatus,
       "alaDaUNPVlanTagRuleMCLagConfigStatus": alaDaUNPVlanTagRuleMCLagConfigStatus,
       "alaDaMacUserTable": alaDaMacUserTable,
       "alaDaMacUserEntry": alaDaMacUserEntry,
       "alaDaMacUserIntfNum": alaDaMacUserIntfNum,
       "alaDaMacUserMACAddress": alaDaMacUserMACAddress,
       "alaDaMacUserVlanID": alaDaMacUserVlanID,
       "alaDaAuthenticationStatus": alaDaAuthenticationStatus,
       "alaDaMacUserIpAddress": alaDaMacUserIpAddress,
       "alaDaMacUserUnpUsed": alaDaMacUserUnpUsed,
       "alaDaMacUserLoginTimeStamp": alaDaMacUserLoginTimeStamp,
       "alaDaMacUserAuthtype": alaDaMacUserAuthtype,
       "alaDaMacUserClassificationSource": alaDaMacUserClassificationSource,
       "alaDaMacUserName": alaDaMacUserName,
       "alaDaUNPPortTable": alaDaUNPPortTable,
       "alaDaUNPPortEntry": alaDaUNPPortEntry,
       "alaDaUNPPortIfIndex": alaDaUNPPortIfIndex,
       "alaDaUNPPortDefaultProfileName": alaDaUNPPortDefaultProfileName,
       "alaDaUNPPortPassAltProfileName": alaDaUNPPortPassAltProfileName,
       "alaDaUNPPortRowStatus": alaDaUNPPortRowStatus,
       "alaDaUNPPortMacAuthFlag": alaDaUNPPortMacAuthFlag,
       "alaDaUNPPortClassificationFlag": alaDaUNPPortClassificationFlag,
       "alaDaUNPPortTrustTagStatus": alaDaUNPPortTrustTagStatus,
       "alaDaUNPPortMCLagConfigStatus": alaDaUNPPortMCLagConfigStatus,
       "alaDaUNPPortCustomerDomainId": alaDaUNPPortCustomerDomainId,
       "alaDaUNPPortType": alaDaUNPPortType,
       "alaDaUNPPortPassAltSpbProfileName": alaDaUNPPortPassAltSpbProfileName,
       "alaDaUNPPortDefaultSpbProfileName": alaDaUNPPortDefaultSpbProfileName,
       "alaDaUNPPortDefaultEdgeProfName": alaDaUNPPortDefaultEdgeProfName,
       "alaDaUNPPortMacPassEdgeProfName": alaDaUNPPortMacPassEdgeProfName,
       "alaDaUNPPort8021XEdgeProfName": alaDaUNPPort8021XEdgeProfName,
       "alaDaUNPPort8021XAuthStatus": alaDaUNPPort8021XAuthStatus,
       "alaDaUNPPort8021XTxPeriodStatus": alaDaUNPPort8021XTxPeriodStatus,
       "alaDaUNPPort8021XTxPeriod": alaDaUNPPort8021XTxPeriod,
       "alaDaUNPPort8021XSuppTimeoutStatus": alaDaUNPPort8021XSuppTimeoutStatus,
       "alaDaUNPPort8021XSuppTimeOut": alaDaUNPPort8021XSuppTimeOut,
       "alaDaUNPPort8021XMaxReqStatus": alaDaUNPPort8021XMaxReqStatus,
       "alaDaUNPPort8021XMaxReq": alaDaUNPPort8021XMaxReq,
       "alaDaUNPPortGroupId": alaDaUNPPortGroupId,
       "alaDaUNPPortAaaProfile": alaDaUNPPortAaaProfile,
       "alaDaUNPPortEdgeTemplate": alaDaUNPPortEdgeTemplate,
       "alaDaUNPPortRedirectPortBounce": alaDaUNPPortRedirectPortBounce,
       "alaDaUNPPort8021XFailurePolicy": alaDaUNPPort8021XFailurePolicy,
       "alaDaUNPPort8021XBypassStatus": alaDaUNPPort8021XBypassStatus,
       "alaDaUNPPortMacAllowEap": alaDaUNPPortMacAllowEap,
       "alaDaUNPPortAdminControlledDirections": alaDaUNPPortAdminControlledDirections,
       "alaDaUNPPortAdminControlledOperDirections": alaDaUNPPortAdminControlledOperDirections,
       "alaDaUNPPort8021XPassAltUserNetProfName": alaDaUNPPort8021XPassAltUserNetProfName,
       "alaDaUNPPort8021XPassAltSpbProfName": alaDaUNPPort8021XPassAltSpbProfName,
       "alaDaUNPPort8021XPassAltVxlanProfName": alaDaUNPPort8021XPassAltVxlanProfName,
       "alaDaUNPPortPassAltVxlanProfileName": alaDaUNPPortPassAltVxlanProfileName,
       "alaDaUNPPortDefaultVxlanProfileName": alaDaUNPPortDefaultVxlanProfileName,
       "alaDaUNPPortAFDConfig": alaDaUNPPortAFDConfig,
       "alaDaUNPPortMaxIngressBw": alaDaUNPPortMaxIngressBw,
       "alaDaUNPPortMaxIngressBwSource": alaDaUNPPortMaxIngressBwSource,
       "alaDaUNPPortMaxEgressBw": alaDaUNPPortMaxEgressBw,
       "alaDaUNPPortMaxEgressBwSource": alaDaUNPPortMaxEgressBwSource,
       "alaDaUNPPortMaxIngressDepth": alaDaUNPPortMaxIngressDepth,
       "alaDaUNPPortMaxEgressDepth": alaDaUNPPortMaxEgressDepth,
       "alaDaUNPPortIngressSourceProfile": alaDaUNPPortIngressSourceProfile,
       "alaDaUNPPortEgressSourceProfile": alaDaUNPPortEgressSourceProfile,
       "alaDaUNPPortForceL3Learning": alaDaUNPPortForceL3Learning,
       "alaDaUNPPortForceL3LearningPortBounce": alaDaUNPPortForceL3LearningPortBounce,
       "alaDaUNPPort8021XPassAltProfileName": alaDaUNPPort8021XPassAltProfileName,
       "alaDaUNPPortPortTemplateName": alaDaUNPPortPortTemplateName,
       "alaDaUNPPortDomainID": alaDaUNPPortDomainID,
       "alaDaUNPPortAdminState": alaDaUNPPortAdminState,
       "alaDaUNPPortDynamicService": alaDaUNPPortDynamicService,
       "alaDaUNPPortPVlanPortType": alaDaUNPPortPVlanPortType,
       "alaDaUNPPortL2Profile": alaDaUNPPortL2Profile,
       "alaDaUNPPortApMode": alaDaUNPPortApMode,
       "alaDaUNPPortApModeSecurity": alaDaUNPPortApModeSecurity,
       "alaDaUNPPortSwSuppSecureMode": alaDaUNPPortSwSuppSecureMode,
       "alaDaUNPPortBpduLldpLearn": alaDaUNPPortBpduLldpLearn,
       "alaDaUNPGlobalConfiguration": alaDaUNPGlobalConfiguration,
       "alaDaUNPDynamicVlanConfigFlag": alaDaUNPDynamicVlanConfigFlag,
       "alaDaUNPAuthServerDownUnp": alaDaUNPAuthServerDownUnp,
       "alaDaUNPAuthServerDownTimeout": alaDaUNPAuthServerDownTimeout,
       "alaDaUNPDynamicVlanMCLagConfigStatus": alaDaUNPDynamicVlanMCLagConfigStatus,
       "alaDaUNPAuthServerDownUNPMCLagConfigStatus": alaDaUNPAuthServerDownUNPMCLagConfigStatus,
       "alaDaUNPAuthServerDownTimeoutMCLagConfigStatus": alaDaUNPAuthServerDownTimeoutMCLagConfigStatus,
       "alaDaUNPDynamicProfileConfigFlag": alaDaUNPDynamicProfileConfigFlag,
       "alaDaUNPDynamicProfileConfigMCLagConfigStatus": alaDaUNPDynamicProfileConfigMCLagConfigStatus,
       "alaDaUNPReloadVsiTypeDB": alaDaUNPReloadVsiTypeDB,
       "alaDaUNPAuthSrvDownEdgeProfName": alaDaUNPAuthSrvDownEdgeProfName,
       "alaDaUNPAuthServerDowneEdgeProfTimeout": alaDaUNPAuthServerDowneEdgeProfTimeout,
       "alaDaUNPEdgeUserFlush": alaDaUNPEdgeUserFlush,
       "alaDaUNP8021XEdgeUserFlush": alaDaUNP8021XEdgeUserFlush,
       "alaDaUNPMacEdgeUserFlush": alaDaUNPMacEdgeUserFlush,
       "alaDaUNPNoAuthEdgeUserFlush": alaDaUNPNoAuthEdgeUserFlush,
       "alaDaUNPRedirectPortBounce": alaDaUNPRedirectPortBounce,
       "alaDaUNPRedirectPauseTimer": alaDaUNPRedirectPauseTimer,
       "alaDaUNPRedirectProxyServerPort": alaDaUNPRedirectProxyServerPort,
       "alaDaUNPRedirectServerIPType": alaDaUNPRedirectServerIPType,
       "alaDaUNPRedirectServerIP": alaDaUNPRedirectServerIP,
       "alaDaUNPAuthSrvDownVxlanProfileName": alaDaUNPAuthSrvDownVxlanProfileName,
       "alaDaUNPAuthSrvDownVxlanProfileTimeout": alaDaUNPAuthSrvDownVxlanProfileTimeout,
       "alaDaUNPForceL3Learning": alaDaUNPForceL3Learning,
       "alaDaUNPForceL3LearningPortBounce": alaDaUNPForceL3LearningPortBounce,
       "alaDaUNPAuthServerDownProfile1": alaDaUNPAuthServerDownProfile1,
       "alaDaUNPAuthServerDownProfile2": alaDaUNPAuthServerDownProfile2,
       "alaDaUNPAuthServerDownProfile3": alaDaUNPAuthServerDownProfile3,
       "alaDaUNPVlanUserFlush": alaDaUNPVlanUserFlush,
       "alaDaUNP8021XPassThrough": alaDaUNP8021XPassThrough,
       "alaDaUNPApMode": alaDaUNPApMode,
       "alaDaUNPServiceModule": alaDaUNPServiceModule,
       "alaDaUNPServiceBase": alaDaUNPServiceBase,
       "alaDaUNPServiceMulticastMode": alaDaUNPServiceMulticastMode,
       "alaDaUNPServiceVlanXlation": alaDaUNPServiceVlanXlation,
       "alaDaUNPServiceMulticastGroup": alaDaUNPServiceMulticastGroup,
       "alaDaUNPServiceFarEndIpList": alaDaUNPServiceFarEndIpList,
       "alaDaUNPIpv6Drop": alaDaUNPIpv6Drop,
       "alaDaUNPAuthServerDownVoiceProfile1": alaDaUNPAuthServerDownVoiceProfile1,
       "alaDaUNPAuthServerDownVoiceProfile2": alaDaUNPAuthServerDownVoiceProfile2,
       "alaDaUNPAuthServerDownVoiceProfile3": alaDaUNPAuthServerDownVoiceProfile3,
       "alaDaUNPDelayLearning": alaDaUNPDelayLearning,
       "alaDaUNPAuthServerDownPortBounce": alaDaUNPAuthServerDownPortBounce,
       "alaDaUNPMacMobility": alaDaUNPMacMobility,
       "alaDaUNPEapolVersion": alaDaUNPEapolVersion,
       "alaDaUNPApModeSecurity": alaDaUNPApModeSecurity,
       "alaDaUNPServiceMulticastGroupIPType": alaDaUNPServiceMulticastGroupIPType,
       "alaDaUNPServiceMulticastGroupIP": alaDaUNPServiceMulticastGroupIP,
       "alaDaUNPMultiUntagSap": alaDaUNPMultiUntagSap,
       "alaDaUNPRedirectAllowedWebServerPollingInterval": alaDaUNPRedirectAllowedWebServerPollingInterval,
       "alaDaUNPRedirectAllowedWebServerRefresh": alaDaUNPRedirectAllowedWebServerRefresh,
       "alaDaUNPServiceVplsSignaling": alaDaUNPServiceVplsSignaling,
       "alaDaUNPServiceVplsLdpFarEndIPList": alaDaUNPServiceVplsLdpFarEndIPList,
       "alaDaUNPServiceVplsBgpVeID": alaDaUNPServiceVplsBgpVeID,
       "alaDaUNPServiceBvlanModulo": alaDaUNPServiceBvlanModulo,
       "alaDaUNPApModeType": alaDaUNPApModeType,
       "alaDaMacVlanUserTable": alaDaMacVlanUserTable,
       "alaDaMacVlanUserEntry": alaDaMacVlanUserEntry,
       "alaDaMacVlanUserIntfNum": alaDaMacVlanUserIntfNum,
       "alaDaMacVlanUserMACAddress": alaDaMacVlanUserMACAddress,
       "alaDaMacVlanUserVlanID": alaDaMacVlanUserVlanID,
       "alaDaMacVlanUserAuthStatus": alaDaMacVlanUserAuthStatus,
       "alaDaMacVlanUserIpAddressType": alaDaMacVlanUserIpAddressType,
       "alaDaMacVlanUserIpAddress": alaDaMacVlanUserIpAddress,
       "alaDaMacVlanUserUnpUsed": alaDaMacVlanUserUnpUsed,
       "alaDaMacVlanUserLoginTimeStamp": alaDaMacVlanUserLoginTimeStamp,
       "alaDaMacVlanUserAuthtype": alaDaMacVlanUserAuthtype,
       "alaDaMacVlanUserClassificationSource": alaDaMacVlanUserClassificationSource,
       "alaDaMacVlanUserMCLagLearningLoc": alaDaMacVlanUserMCLagLearningLoc,
       "alaDaMacVlanUserName": alaDaMacVlanUserName,
       "alaDaMacVlanUserRole": alaDaMacVlanUserRole,
       "alaDaMacVlanUserRoleSource": alaDaMacVlanUserRoleSource,
       "alaDaMacVlanUserAuthFailReason": alaDaMacVlanUserAuthFailReason,
       "alaDaMacVlanUserAuthRetryCount": alaDaMacVlanUserAuthRetryCount,
       "alaDaMacVlanUserClassifProfRule": alaDaMacVlanUserClassifProfRule,
       "alaDaMacVlanUserRoleRule": alaDaMacVlanUserRoleRule,
       "alaDaMacVlanUserRestAccessStatus": alaDaMacVlanUserRestAccessStatus,
       "alaDaMacVlanUserLocPolicyStatus": alaDaMacVlanUserLocPolicyStatus,
       "alaDaMacVlanUserTimePolicyStatus": alaDaMacVlanUserTimePolicyStatus,
       "alaDaMacVlanUserCapPortalStatus": alaDaMacVlanUserCapPortalStatus,
       "alaDaMacVlanUserQMRStatus": alaDaMacVlanUserQMRStatus,
       "alaDaMacVlanUserAuthServerIpType": alaDaMacVlanUserAuthServerIpType,
       "alaDaMacVlanUserAuthServerIpUsed": alaDaMacVlanUserAuthServerIpUsed,
       "alaDaMacVlanUserAuthServerUsed": alaDaMacVlanUserAuthServerUsed,
       "alaDaMacVlanUserServerMessage": alaDaMacVlanUserServerMessage,
       "alaDaMacVlanUserRedirectionUrl": alaDaMacVlanUserRedirectionUrl,
       "alaDaMacVlanUserSIPCallType": alaDaMacVlanUserSIPCallType,
       "alaDaMacVlanUserSIPMediaType": alaDaMacVlanUserSIPMediaType,
       "alaDaMacVlanUserUnpFromAuthServer": alaDaMacVlanUserUnpFromAuthServer,
       "alaDaMacVlanUserType": alaDaMacVlanUserType,
       "alaDaMacVlanUserServiceID": alaDaMacVlanUserServiceID,
       "alaDaMacVlanUserServiceSapIDIfIndex": alaDaMacVlanUserServiceSapIDIfIndex,
       "alaDaMacVlanUserServiceSapIDEncapVal": alaDaMacVlanUserServiceSapIDEncapVal,
       "alaDaMacVlanUserVxlanVnid": alaDaMacVlanUserVxlanVnid,
       "alaDaMacVlanUserSpbIsid": alaDaMacVlanUserSpbIsid,
       "alaDaMacVlanUserSpbBVlan": alaDaMacVlanUserSpbBVlan,
       "alaDaMacVlanUserKerberosStatus": alaDaMacVlanUserKerberosStatus,
       "alaDaMacVlanUserL2greVpnid": alaDaMacVlanUserL2greVpnid,
       "alaDaMacVlanUserImplicitTrustTagSource": alaDaMacVlanUserImplicitTrustTagSource,
       "alaDaMacVlanUserRadiusTrustVlanStr": alaDaMacVlanUserRadiusTrustVlanStr,
       "alaDaUNPNotificationObjects": alaDaUNPNotificationObjects,
       "alaDaUnpMacAddr": alaDaUnpMacAddr,
       "alaDaUnpSourceIpAddr": alaDaUnpSourceIpAddr,
       "alaDaUnpNativeVlan": alaDaUnpNativeVlan,
       "alaDaUnpVlan": alaDaUnpVlan,
       "alaDaUnpMCLAGId": alaDaUnpMCLAGId,
       "alaDaUnpCommandType": alaDaUnpCommandType,
       "alaDaUnpName": alaDaUnpName,
       "alaDaUnpMacAddr1": alaDaUnpMacAddr1,
       "alaDaUnpMacAddr2": alaDaUnpMacAddr2,
       "alaDaUnpIpAddr": alaDaUnpIpAddr,
       "alaDaUnpIpMask": alaDaUnpIpMask,
       "alaDaUnpVlanTag": alaDaUnpVlanTag,
       "alaDaKerberosRateLimitString": alaDaKerberosRateLimitString,
       "alaDaRouterAuthNumberOfUsersPassedAuthentication": alaDaRouterAuthNumberOfUsersPassedAuthentication,
       "alaDaRouterAuthUserSourceIpAddressType": alaDaRouterAuthUserSourceIpAddressType,
       "alaDaRouterAuthUserSourceIpAddress": alaDaRouterAuthUserSourceIpAddress,
       "alaDaRouterAuthUserDestinationIpAddressType": alaDaRouterAuthUserDestinationIpAddressType,
       "alaDaRouterAuthUserDestinationIpAddress": alaDaRouterAuthUserDestinationIpAddress,
       "alaDaRouterAuthUserName": alaDaRouterAuthUserName,
       "alaDaRouterAuthUserAttempts": alaDaRouterAuthUserAttempts,
       "alaDaRouterAuthNumberOfUsersFailedAuthentication": alaDaRouterAuthNumberOfUsersFailedAuthentication,
       "alaDaRouterAuthNumberOfAuthenticatedUsers": alaDaRouterAuthNumberOfAuthenticatedUsers,
       "alaDaRouterAuthNumberOfConfigUsed": alaDaRouterAuthNumberOfConfigUsed,
       "alaDaUnpMaxUserSupported": alaDaUnpMaxUserSupported,
       "alaDaUnpMaxUserCurrentNumberOfUsers": alaDaUnpMaxUserCurrentNumberOfUsers,
       "alaDaUnpHWResourceChassisId": alaDaUnpHWResourceChassisId,
       "alaDaUnpHWResourceSlot": alaDaUnpHWResourceSlot,
       "alaDaUnpHWResourceTtiAllocated": alaDaUnpHWResourceTtiAllocated,
       "alaDaUnpAuthMACAddress": alaDaUnpAuthMACAddress,
       "alaDaUnpAuthStatus": alaDaUnpAuthStatus,
       "alaDaUnpAuthRADIUSServerIPType": alaDaUnpAuthRADIUSServerIPType,
       "alaDaUnpAuthRADIUSServerIP": alaDaUnpAuthRADIUSServerIP,
       "alaDaUnpAuthServerReplyMsg": alaDaUnpAuthServerReplyMsg,
       "alaDaUnpAuthFailureReason": alaDaUnpAuthFailureReason,
       "alaDaUnpCustomerDomainTable": alaDaUnpCustomerDomainTable,
       "alaDaUnpCustomerDomainEntry": alaDaUnpCustomerDomainEntry,
       "alaDaUnpCustomerDomainId": alaDaUnpCustomerDomainId,
       "alaDaUnpCustomerDomainDesc": alaDaUnpCustomerDomainDesc,
       "alaDaUnpCustomerDomainRowStatus": alaDaUnpCustomerDomainRowStatus,
       "alaDaSpbProfileTable": alaDaSpbProfileTable,
       "alaDaSpbProfileEntry": alaDaSpbProfileEntry,
       "alaDaSpbProfileName": alaDaSpbProfileName,
       "alaDaSpbProfileEncapVal": alaDaSpbProfileEncapVal,
       "alaDaSpbProfileQosPolicyListName": alaDaSpbProfileQosPolicyListName,
       "alaDaSpbProfileIsid": alaDaSpbProfileIsid,
       "alaDaSpbProfileBVlan": alaDaSpbProfileBVlan,
       "alaDaSpbProfileRowStatus": alaDaSpbProfileRowStatus,
       "alaDaSpbProfileMulticastMode": alaDaSpbProfileMulticastMode,
       "alaDaSpbProfileSapVlanXlation": alaDaSpbProfileSapVlanXlation,
       "alaDaSpbProfileMobileTag": alaDaSpbProfileMobileTag,
       "alaDaSpbProfileAFDConfig": alaDaSpbProfileAFDConfig,
       "alaDaUNPCustDomainEvbGpIdRuleTable": alaDaUNPCustDomainEvbGpIdRuleTable,
       "alaDaUNPCustDomainEvbGpIdRuleEntry": alaDaUNPCustDomainEvbGpIdRuleEntry,
       "alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId": alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId,
       "alaDaUNPCustDomainEvbGpIdRuleGroupId": alaDaUNPCustDomainEvbGpIdRuleGroupId,
       "alaDaUNPCustDomainEvbGpIdRuleVlanProfileName": alaDaUNPCustDomainEvbGpIdRuleVlanProfileName,
       "alaDaUNPCustDomainEvbGpIdRuleSpbProfileName": alaDaUNPCustDomainEvbGpIdRuleSpbProfileName,
       "alaDaUNPCustDomainEvbGpIdRuleRowStatus": alaDaUNPCustDomainEvbGpIdRuleRowStatus,
       "alaDaUNPCustDomainEvbGpIdRuleVxlanProfileName": alaDaUNPCustDomainEvbGpIdRuleVxlanProfileName,
       "alaDaUNPCustDomainVlanTagRuleTable": alaDaUNPCustDomainVlanTagRuleTable,
       "alaDaUNPCustDomainVlanTagRuleEntry": alaDaUNPCustDomainVlanTagRuleEntry,
       "alaDaUNPCustDomainVlanTagRuleDomainId": alaDaUNPCustDomainVlanTagRuleDomainId,
       "alaDaUNPCustDomainVlanTagRuleVlan": alaDaUNPCustDomainVlanTagRuleVlan,
       "alaDaUNPCustDomainVlanTagRuleVlanProfileName": alaDaUNPCustDomainVlanTagRuleVlanProfileName,
       "alaDaUNPCustDomainVlanTagRuleRowStatus": alaDaUNPCustDomainVlanTagRuleRowStatus,
       "alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus": alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus,
       "alaDaUNPCustDomainVlanTagRuleSpbProfileName": alaDaUNPCustDomainVlanTagRuleSpbProfileName,
       "alaDaUNPCustDomainVlanTagRuleTagPosition": alaDaUNPCustDomainVlanTagRuleTagPosition,
       "alaDaUNPCustDomainVlanTagRuleVxlanProfileName": alaDaUNPCustDomainVlanTagRuleVxlanProfileName,
       "alaDaUNPCustDomainVlanTagRuleProfile1": alaDaUNPCustDomainVlanTagRuleProfile1,
       "alaDaUNPCustDomainVlanTagRuleProfile2": alaDaUNPCustDomainVlanTagRuleProfile2,
       "alaDaUNPCustDomainVlanTagRuleProfile3": alaDaUNPCustDomainVlanTagRuleProfile3,
       "alaDaUNPCustDomainIpNetRuleTable": alaDaUNPCustDomainIpNetRuleTable,
       "alaDaUNPCustDomainIpNetRuleEntry": alaDaUNPCustDomainIpNetRuleEntry,
       "alaDaUNPCustDomainIpNetRuleDomainId": alaDaUNPCustDomainIpNetRuleDomainId,
       "alaDaUNPCustDomainIpNetRuleAddrType": alaDaUNPCustDomainIpNetRuleAddrType,
       "alaDaUNPCustDomainIpNetRuleAddr": alaDaUNPCustDomainIpNetRuleAddr,
       "alaDaUNPCustDomainIpNetRuleMask": alaDaUNPCustDomainIpNetRuleMask,
       "alaDaUNPCustDomainIpNetRuleProfileName": alaDaUNPCustDomainIpNetRuleProfileName,
       "alaDaUNPCustDomainIpNetRuleVlanTag": alaDaUNPCustDomainIpNetRuleVlanTag,
       "alaDaUNPCustDomainIpNetRuleRowStatus": alaDaUNPCustDomainIpNetRuleRowStatus,
       "alaDaUNPCustDomainIpNetRuleMCLagConfigStatus": alaDaUNPCustDomainIpNetRuleMCLagConfigStatus,
       "alaDaUNPCustDomainIpNetRuleSpbProfileName": alaDaUNPCustDomainIpNetRuleSpbProfileName,
       "alaDaUNPCustDomainIpNetRuleEdgeProfile": alaDaUNPCustDomainIpNetRuleEdgeProfile,
       "alaDaUNPCustDomainIpNetRuleVxlanProfileName": alaDaUNPCustDomainIpNetRuleVxlanProfileName,
       "alaDaUNPCustDomainIpNetRuleProfile1": alaDaUNPCustDomainIpNetRuleProfile1,
       "alaDaUNPCustDomainIpNetRuleProfile2": alaDaUNPCustDomainIpNetRuleProfile2,
       "alaDaUNPCustDomainIpNetRuleProfile3": alaDaUNPCustDomainIpNetRuleProfile3,
       "alaDaUNPCustDomainMacRuleTable": alaDaUNPCustDomainMacRuleTable,
       "alaDaUNPCustDomainMacRuleEntry": alaDaUNPCustDomainMacRuleEntry,
       "alaDaUNPCustDomainMacRuleDomainId": alaDaUNPCustDomainMacRuleDomainId,
       "alaDaUNPCustDomainMacRuleAddr": alaDaUNPCustDomainMacRuleAddr,
       "alaDaUNPCustDomainMacRuleProfileName": alaDaUNPCustDomainMacRuleProfileName,
       "alaDaUNPCustDomainMacRuleVlanTag": alaDaUNPCustDomainMacRuleVlanTag,
       "alaDaUNPCustDomainMacRuleRowStatus": alaDaUNPCustDomainMacRuleRowStatus,
       "alaDaUNPCustDomainMacRuleMCLagConfigStatus": alaDaUNPCustDomainMacRuleMCLagConfigStatus,
       "alaDaUNPCustDomainMacRuleSpbProfileName": alaDaUNPCustDomainMacRuleSpbProfileName,
       "alaDaUNPCustDomainMacRuleEdgeProfileName": alaDaUNPCustDomainMacRuleEdgeProfileName,
       "alaDaUNPCustDomainMacRuleVxlanProfileName": alaDaUNPCustDomainMacRuleVxlanProfileName,
       "alaDaUNPCustDomainMacRuleProfile1": alaDaUNPCustDomainMacRuleProfile1,
       "alaDaUNPCustDomainMacRuleProfile2": alaDaUNPCustDomainMacRuleProfile2,
       "alaDaUNPCustDomainMacRuleProfile3": alaDaUNPCustDomainMacRuleProfile3,
       "alaDaUNPCustDomainMacRangeRuleTable": alaDaUNPCustDomainMacRangeRuleTable,
       "alaDaUNPCustDomainMacRangeRuleEntry": alaDaUNPCustDomainMacRangeRuleEntry,
       "alaDaUNPCustDomainMacRangeRuleDomainId": alaDaUNPCustDomainMacRangeRuleDomainId,
       "alaDaUNPCustDomainMacRangeRuleLoAddr": alaDaUNPCustDomainMacRangeRuleLoAddr,
       "alaDaUNPCustDomainMacRangeRuleHiAddr": alaDaUNPCustDomainMacRangeRuleHiAddr,
       "alaDaUNPCustDomainMacRangeRuleProfileName": alaDaUNPCustDomainMacRangeRuleProfileName,
       "alaDaUNPCustDomainMacRangeRuleVlanTag": alaDaUNPCustDomainMacRangeRuleVlanTag,
       "alaDaUNPCustDomainMacRangeRuleRowStatus": alaDaUNPCustDomainMacRangeRuleRowStatus,
       "alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus": alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus,
       "alaDaUNPCustDomainMacRangeRuleSpbProfileName": alaDaUNPCustDomainMacRangeRuleSpbProfileName,
       "alaDaUNPCustDomainMacRangeRuleEdgeProfileName": alaDaUNPCustDomainMacRangeRuleEdgeProfileName,
       "alaDaUNPCustDomainMacRangeRuleVxlanProfileName": alaDaUNPCustDomainMacRangeRuleVxlanProfileName,
       "alaDaUNPCustDomainMacRangeRuleProfile1": alaDaUNPCustDomainMacRangeRuleProfile1,
       "alaDaUNPCustDomainMacRangeRuleProfile2": alaDaUNPCustDomainMacRangeRuleProfile2,
       "alaDaUNPCustDomainMacRangeRuleProfile3": alaDaUNPCustDomainMacRangeRuleProfile3,
       "alaDaSaaProfileTable": alaDaSaaProfileTable,
       "alaDaSaaProfileEntry": alaDaSaaProfileEntry,
       "alaDaSaaProfileName": alaDaSaaProfileName,
       "alaDaSaaProfileLatencyThreshold": alaDaSaaProfileLatencyThreshold,
       "alaDaSaaProfileJitterThreshold": alaDaSaaProfileJitterThreshold,
       "alaDaSaaProfileRowStatus": alaDaSaaProfileRowStatus,
       "alaDaCPortalMIBObjects": alaDaCPortalMIBObjects,
       "alaDaCPortalGlobalConfig": alaDaCPortalGlobalConfig,
       "alaDaCPortalRedirectUrlName": alaDaCPortalRedirectUrlName,
       "alaDaCPortalIpAddressType": alaDaCPortalIpAddressType,
       "alaDaCPortalIpAddress": alaDaCPortalIpAddress,
       "alaDaCPortalMode": alaDaCPortalMode,
       "alaDaCPortalSuccRedirectUrl": alaDaCPortalSuccRedirectUrl,
       "alaDaCPortalProxyPort": alaDaCPortalProxyPort,
       "alaDaCPortalRetryCnt": alaDaCPortalRetryCnt,
       "alaDaCPortalPolicyListName": alaDaCPortalPolicyListName,
       "alaDaCPortalCustomization": alaDaCPortalCustomization,
       "alaDaCPortalUNPProfile": alaDaCPortalUNPProfile,
       "alaDaCPortalUNPProfileChange": alaDaCPortalUNPProfileChange,
       "alaDaCPortalDHCPLeaseTime": alaDaCPortalDHCPLeaseTime,
       "alaDaCPortalDHCPRenewTime": alaDaCPortalDHCPRenewTime,
       "alaDaCPortalDHCPRebindingTime": alaDaCPortalDHCPRebindingTime,
       "alaDaCPortalAuthPassTable": alaDaCPortalAuthPassTable,
       "alaDaCPortalAuthPassEntry": alaDaCPortalAuthPassEntry,
       "alaDaCPortalAuthDomainName": alaDaCPortalAuthDomainName,
       "alaDaCPortalAuthRealm": alaDaCPortalAuthRealm,
       "alaDaCPortalAuthPolicyListName": alaDaCPortalAuthPolicyListName,
       "alaDaCPortalAuthRowStatus": alaDaCPortalAuthRowStatus,
       "alaDaCPortalAuthUNPProfile": alaDaCPortalAuthUNPProfile,
       "alaDaCPortalAuthUNPProfileChange": alaDaCPortalAuthUNPProfileChange,
       "alaDaCPortalProfTable": alaDaCPortalProfTable,
       "alaDaCPortalProfEntry": alaDaCPortalProfEntry,
       "alaDaCPortalProfName": alaDaCPortalProfName,
       "alaDaCPortalProfMode": alaDaCPortalProfMode,
       "alaDaCPortalProfSuccRedirectUrl": alaDaCPortalProfSuccRedirectUrl,
       "alaDaCPortalProfRetryCnt": alaDaCPortalProfRetryCnt,
       "alaDaCPortalProfAuthPolicyListName": alaDaCPortalProfAuthPolicyListName,
       "alaDaCPortalProfAaaProf": alaDaCPortalProfAaaProf,
       "alaDaCPortalProfRowStatus": alaDaCPortalProfRowStatus,
       "alaDaCPortalProfUNPProfile": alaDaCPortalProfUNPProfile,
       "alaDaCPortalProfUNPProfileChange": alaDaCPortalProfUNPProfileChange,
       "alaDaCPortalProfDomainTable": alaDaCPortalProfDomainTable,
       "alaDaCPortalProfDomainEntry": alaDaCPortalProfDomainEntry,
       "alaDaCPortalProfDomainAuthDomainName": alaDaCPortalProfDomainAuthDomainName,
       "alaDaCPortalProfDomainAuthPolicyListName": alaDaCPortalProfDomainAuthPolicyListName,
       "alaDaCPortalProfDomainAuthRealm": alaDaCPortalProfDomainAuthRealm,
       "alaDaCPortalProfDomainRowStatus": alaDaCPortalProfDomainRowStatus,
       "alaDaCPortalProfDomainUNPProfile": alaDaCPortalProfDomainUNPProfile,
       "alaDaCPortalProfDomainUNPProfileChange": alaDaCPortalProfDomainUNPProfileChange,
       "alaDaHICMIBObjects": alaDaHICMIBObjects,
       "alaDaHICGlobalConfig": alaDaHICGlobalConfig,
       "alaDaHICStatus": alaDaHICStatus,
       "alaDaHICWebAgentDownloadUrl": alaDaHICWebAgentDownloadUrl,
       "alaDaHICCustomHttpProxyPort": alaDaHICCustomHttpProxyPort,
       "alaDaHICBgPollInterval": alaDaHICBgPollInterval,
       "alaDaHICSvrFailMode": alaDaHICSvrFailMode,
       "alaDaHICSvrTable": alaDaHICSvrTable,
       "alaDaHICSvrEntry": alaDaHICSvrEntry,
       "alaDaHICSvrName": alaDaHICSvrName,
       "alaDaHICSvrIpAddrType": alaDaHICSvrIpAddrType,
       "alaDaHICSvrIpAddr": alaDaHICSvrIpAddr,
       "alaDaHICSvrPort": alaDaHICSvrPort,
       "alaDaHICSvrKey": alaDaHICSvrKey,
       "alaDaHICSvrStatus": alaDaHICSvrStatus,
       "alaDaHICSvrRole": alaDaHICSvrRole,
       "alaDaHICSvrConnection": alaDaHICSvrConnection,
       "alaDaHICSvrRowStatus": alaDaHICSvrRowStatus,
       "alaDaHICAllowedTable": alaDaHICAllowedTable,
       "alaDaHICAllowedEntry": alaDaHICAllowedEntry,
       "alaDaHICAllowedName": alaDaHICAllowedName,
       "alaDaHICAllowedIpAddrType": alaDaHICAllowedIpAddrType,
       "alaDaHICAllowedIpAddr": alaDaHICAllowedIpAddr,
       "alaDaHICAllowedIpMaskType": alaDaHICAllowedIpMaskType,
       "alaDaHICAllowedIpMask": alaDaHICAllowedIpMask,
       "alaDaHICAllowedRowStatus": alaDaHICAllowedRowStatus,
       "alaDaHICSvrFailPolicyTable": alaDaHICSvrFailPolicyTable,
       "alaDaHICSvrFailPolicyEntry": alaDaHICSvrFailPolicyEntry,
       "alaDaHICSvrFailPolicyName": alaDaHICSvrFailPolicyName,
       "alaDaHICSvrFailChangedPolicyName": alaDaHICSvrFailChangedPolicyName,
       "alaDaHICSvrFailRowStatus": alaDaHICSvrFailRowStatus,
       "alaDaHICHostTable": alaDaHICHostTable,
       "alaDaHICHostEntry": alaDaHICHostEntry,
       "alaDaHICHostMac": alaDaHICHostMac,
       "alaDaHICHostStatus": alaDaHICHostStatus,
       "alaDaUNPETmplTable": alaDaUNPETmplTable,
       "alaDaUNPETmplEntry": alaDaUNPETmplEntry,
       "alaDaUNPETmplName": alaDaUNPETmplName,
       "alaDaUNPETmpl8021XAuthStatus": alaDaUNPETmpl8021XAuthStatus,
       "alaDaUNPETmpl8021XTxPeriodStatus": alaDaUNPETmpl8021XTxPeriodStatus,
       "alaDaUNPETmpl8021XTxPeriod": alaDaUNPETmpl8021XTxPeriod,
       "alaDaUNPETmpl8021XSuppTimeoutStatus": alaDaUNPETmpl8021XSuppTimeoutStatus,
       "alaDaUNPETmpl8021XSuppTimeOut": alaDaUNPETmpl8021XSuppTimeOut,
       "alaDaUNPETmpl8021XMaxReqStatus": alaDaUNPETmpl8021XMaxReqStatus,
       "alaDaUNPETmpl8021XMaxReq": alaDaUNPETmpl8021XMaxReq,
       "alaDaUNPETmpl8021XPassAltEProf": alaDaUNPETmpl8021XPassAltEProf,
       "alaDaUNPETmplMacAuthStatus": alaDaUNPETmplMacAuthStatus,
       "alaDaUNPETmplMacPassAltEProf": alaDaUNPETmplMacPassAltEProf,
       "alaDaUNPETmplClassifStatus": alaDaUNPETmplClassifStatus,
       "alaDaUNPETmplDefEProf": alaDaUNPETmplDefEProf,
       "alaDaUNPETmplGroupId": alaDaUNPETmplGroupId,
       "alaDaUNPETmplAaaProf": alaDaUNPETmplAaaProf,
       "alaDaUNPETmplRowStatus": alaDaUNPETmplRowStatus,
       "alaDaUNPETmplRedirectPortBounce": alaDaUNPETmplRedirectPortBounce,
       "alaDaUNPETmplFailurePolicy": alaDaUNPETmplFailurePolicy,
       "alaDaUNPETmplBypassStatus": alaDaUNPETmplBypassStatus,
       "alaDaUNPETmplMacAllowEap": alaDaUNPETmplMacAllowEap,
       "alaDaUNPETmplAdminControlledDirections": alaDaUNPETmplAdminControlledDirections,
       "alaDaUNPETmplTrustTagStatus": alaDaUNPETmplTrustTagStatus,
       "alaDaUNPETmplForceL3Learning": alaDaUNPETmplForceL3Learning,
       "alaDaUNPETmplForceL3LearningPortBounce": alaDaUNPETmplForceL3LearningPortBounce,
       "alaDaUNPEdgeProfTable": alaDaUNPEdgeProfTable,
       "alaDaUNPEdgeProfEntry": alaDaUNPEdgeProfEntry,
       "alaDaUNPEdgeProfName": alaDaUNPEdgeProfName,
       "alaDaUNPEdgeProfQosPolicyList": alaDaUNPEdgeProfQosPolicyList,
       "alaDaUNPEdgeProfLocationPolicy": alaDaUNPEdgeProfLocationPolicy,
       "alaDaUNPEdgeProfPeriodPolicy": alaDaUNPEdgeProfPeriodPolicy,
       "alaDaUNPEdgeProfHICStatus": alaDaUNPEdgeProfHICStatus,
       "alaDaUNPEdgeProfCPortalAuth": alaDaUNPEdgeProfCPortalAuth,
       "alaDaUNPEdgeProfAuthStatus": alaDaUNPEdgeProfAuthStatus,
       "alaDaUNPEdgeProfMobileTag": alaDaUNPEdgeProfMobileTag,
       "alaDaUNPEdgeProfDHCPEnforcment": alaDaUNPEdgeProfDHCPEnforcment,
       "alaDaUNPEdgeProfCPortalProf": alaDaUNPEdgeProfCPortalProf,
       "alaDaUNPEdgeProfRowStatus": alaDaUNPEdgeProfRowStatus,
       "alaDaUNPEdgeProfRedirectStatus": alaDaUNPEdgeProfRedirectStatus,
       "alaDaUNPEdgeProfKerberosStatus": alaDaUNPEdgeProfKerberosStatus,
       "alaDaUNPEdgeProfMaxIngressBw": alaDaUNPEdgeProfMaxIngressBw,
       "alaDaUNPEdgeProfMaxEgressBw": alaDaUNPEdgeProfMaxEgressBw,
       "alaDaUNPEdgeProfMaxIngressDepth": alaDaUNPEdgeProfMaxIngressDepth,
       "alaDaUNPEdgeProfMaxEgressDepth": alaDaUNPEdgeProfMaxEgressDepth,
       "alaDaUNPPortRuleTable": alaDaUNPPortRuleTable,
       "alaDaUNPPortRuleEntry": alaDaUNPPortRuleEntry,
       "alaDaUNPPortRuleNum": alaDaUNPPortRuleNum,
       "alaDaUNPPortRuleEdgeProf": alaDaUNPPortRuleEdgeProf,
       "alaDaUNPPortRuleRowStatus": alaDaUNPPortRuleRowStatus,
       "alaDaUNPPortRuleVlanTag": alaDaUNPPortRuleVlanTag,
       "alaDaUNPPortRuleProfile1": alaDaUNPPortRuleProfile1,
       "alaDaUNPPortRuleProfile2": alaDaUNPPortRuleProfile2,
       "alaDaUNPPortRuleProfile3": alaDaUNPPortRuleProfile3,
       "alaDaUNPGroupRuleTable": alaDaUNPGroupRuleTable,
       "alaDaUNPGroupRuleEntry": alaDaUNPGroupRuleEntry,
       "alaDaUNPGroupRuleId": alaDaUNPGroupRuleId,
       "alaDaUNPGroupRuleEdgeProf": alaDaUNPGroupRuleEdgeProf,
       "alaDaUNPGroupRuleRowStatus": alaDaUNPGroupRuleRowStatus,
       "alaDaUNPGroupRuleVlanTag": alaDaUNPGroupRuleVlanTag,
       "alaDaUNPMacOuiRuleTable": alaDaUNPMacOuiRuleTable,
       "alaDaUNPMacOuiRuleEntry": alaDaUNPMacOuiRuleEntry,
       "alaDaUNPMacOuiRuleAddr": alaDaUNPMacOuiRuleAddr,
       "alaDaUNPMacOuiRuleEdgeProfile": alaDaUNPMacOuiRuleEdgeProfile,
       "alaDaUNPMacOuiRuleRowStatus": alaDaUNPMacOuiRuleRowStatus,
       "alaDaUNPMacOuiRuleVlanTag": alaDaUNPMacOuiRuleVlanTag,
       "alaDaUNPMacOuiRuleProfile1": alaDaUNPMacOuiRuleProfile1,
       "alaDaUNPMacOuiRuleProfile2": alaDaUNPMacOuiRuleProfile2,
       "alaDaUNPMacOuiRuleProfile3": alaDaUNPMacOuiRuleProfile3,
       "alaDaUNPEndPoinRuleTable": alaDaUNPEndPoinRuleTable,
       "alaDaUNPEndPoinRuleEntry": alaDaUNPEndPoinRuleEntry,
       "alaDaUNPEndPoinRuleId": alaDaUNPEndPoinRuleId,
       "alaDaUNPEndPoinEdgeProfile": alaDaUNPEndPoinEdgeProfile,
       "alaDaUNPEndPoinRuleRowStatus": alaDaUNPEndPoinRuleRowStatus,
       "alaDaUNPEndPoinProfile1": alaDaUNPEndPoinProfile1,
       "alaDaUNPEndPoinProfile2": alaDaUNPEndPoinProfile2,
       "alaDaUNPEndPoinProfile3": alaDaUNPEndPoinProfile3,
       "alaDaUNPEndPoinVlanTag": alaDaUNPEndPoinVlanTag,
       "alaDaUNPAuthRuleTable": alaDaUNPAuthRuleTable,
       "alaDaUNPAuthRuleEntry": alaDaUNPAuthRuleEntry,
       "alaDaUNPAuthRuleType": alaDaUNPAuthRuleType,
       "alaDaUNPAuthRuleEdgeProfile": alaDaUNPAuthRuleEdgeProfile,
       "alaDaUNPAuthRuleRowStatus": alaDaUNPAuthRuleRowStatus,
       "alaDaUNPAuthRuleVlanTag": alaDaUNPAuthRuleVlanTag,
       "alaDaUNPAuthRuleProfile1": alaDaUNPAuthRuleProfile1,
       "alaDaUNPAuthRuleProfile2": alaDaUNPAuthRuleProfile2,
       "alaDaUNPAuthRuleProfile3": alaDaUNPAuthRuleProfile3,
       "alaDaUNPClassifRuleTable": alaDaUNPClassifRuleTable,
       "alaDaUNPClassifRuleEntry": alaDaUNPClassifRuleEntry,
       "alaDaUNPClassifRuleName": alaDaUNPClassifRuleName,
       "alaDaUNPClassifRulePrecedenceNum": alaDaUNPClassifRulePrecedenceNum,
       "alaDaUNPClassifRuleEdgeProfile": alaDaUNPClassifRuleEdgeProfile,
       "alaDaUNPClassifRulePort": alaDaUNPClassifRulePort,
       "alaDaUNPClassifRulePortHigh": alaDaUNPClassifRulePortHigh,
       "alaDaUNPClassifRuleGroupId": alaDaUNPClassifRuleGroupId,
       "alaDaUNPClassifRuleMacAddr": alaDaUNPClassifRuleMacAddr,
       "alaDaUNPClassifRuleMacRngLoaddr": alaDaUNPClassifRuleMacRngLoaddr,
       "alaDaUNPClassifRuleMacRngHiaddr": alaDaUNPClassifRuleMacRngHiaddr,
       "alaDaUNPClassifRuleMacOuiAddr": alaDaUNPClassifRuleMacOuiAddr,
       "alaDaUNPClassifRuleEndPoin": alaDaUNPClassifRuleEndPoin,
       "alaDaUNPClassifRuleAuthType": alaDaUNPClassifRuleAuthType,
       "alaDaUNPClassifRuleIpAddressType": alaDaUNPClassifRuleIpAddressType,
       "alaDaUNPClassifRuleIpAddress": alaDaUNPClassifRuleIpAddress,
       "alaDaUNPClassifRuleIpMaskType": alaDaUNPClassifRuleIpMaskType,
       "alaDaUNPClassifRuleIpMask": alaDaUNPClassifRuleIpMask,
       "alaDaUNPClassifRowStatus": alaDaUNPClassifRowStatus,
       "alaDaUNPClassifRuleVlanTag": alaDaUNPClassifRuleVlanTag,
       "alaDaUNPClassifRuleCustomerDomain": alaDaUNPClassifRuleCustomerDomain,
       "alaDaUNPClassifRuleProfile1": alaDaUNPClassifRuleProfile1,
       "alaDaUNPClassifRuleProfile2": alaDaUNPClassifRuleProfile2,
       "alaDaUNPClassifRuleProfile3": alaDaUNPClassifRuleProfile3,
       "alaDaUNPClassifRuleDeviceType": alaDaUNPClassifRuleDeviceType,
       "alaDaUNPMacPortRuleTable": alaDaUNPMacPortRuleTable,
       "alaDaUNPMacPortRuleEntry": alaDaUNPMacPortRuleEntry,
       "alaDaUNPMacPortRuleMacAddr": alaDaUNPMacPortRuleMacAddr,
       "alaDaUNPMacPortRuleNum": alaDaUNPMacPortRuleNum,
       "alaDaUNPMacPortRuleEdgeProf": alaDaUNPMacPortRuleEdgeProf,
       "alaDaUNPMacPortRuleRowStatus": alaDaUNPMacPortRuleRowStatus,
       "alaDaUNPMacPortRuleVlanTag": alaDaUNPMacPortRuleVlanTag,
       "alaDaUNPMacPortRuleProfile1": alaDaUNPMacPortRuleProfile1,
       "alaDaUNPMacPortRuleProfile2": alaDaUNPMacPortRuleProfile2,
       "alaDaUNPMacPortRuleProfile3": alaDaUNPMacPortRuleProfile3,
       "alaDaUNPIpPortRuleTable": alaDaUNPIpPortRuleTable,
       "alaDaUNPIpPortRuleEntry": alaDaUNPIpPortRuleEntry,
       "alaDaUNPIpPortRuleAddrType": alaDaUNPIpPortRuleAddrType,
       "alaDaUNPIpPortRuleAddr": alaDaUNPIpPortRuleAddr,
       "alaDaUNPIpPortRuleNum": alaDaUNPIpPortRuleNum,
       "alaDaUNPIpPortRuleEdgeProf": alaDaUNPIpPortRuleEdgeProf,
       "alaDaUNPIpPortRuleRowStatus": alaDaUNPIpPortRuleRowStatus,
       "alaDaUNPIpPortRuleVlanTag": alaDaUNPIpPortRuleVlanTag,
       "alaDaUNPIpPortRuleProfile1": alaDaUNPIpPortRuleProfile1,
       "alaDaUNPIpPortRuleProfile2": alaDaUNPIpPortRuleProfile2,
       "alaDaUNPIpPortRuleProfile3": alaDaUNPIpPortRuleProfile3,
       "alaDaUNPIpPortRuleMaskType": alaDaUNPIpPortRuleMaskType,
       "alaDaUNPIpPortRuleMask": alaDaUNPIpPortRuleMask,
       "alaDaUNPMacIpPortRuleTable": alaDaUNPMacIpPortRuleTable,
       "alaDaUNPMacIpPortRuleEntry": alaDaUNPMacIpPortRuleEntry,
       "alaDaUNPMacIpPortRuleMacAddr": alaDaUNPMacIpPortRuleMacAddr,
       "alaDaUNPMacIpPortRuleAddrIpType": alaDaUNPMacIpPortRuleAddrIpType,
       "alaDaUNPMacIpPortRuleIpAddr": alaDaUNPMacIpPortRuleIpAddr,
       "alaDaUNPMacIpPortRuleNum": alaDaUNPMacIpPortRuleNum,
       "alaDaUNPMacIpPortRuleEdgeProf": alaDaUNPMacIpPortRuleEdgeProf,
       "alaDaUNPMacIpPortRuleRowStatus": alaDaUNPMacIpPortRuleRowStatus,
       "alaDaUNPMacIpPortRuleVlanTag": alaDaUNPMacIpPortRuleVlanTag,
       "alaDaUNPMacIpPortRuleProfile1": alaDaUNPMacIpPortRuleProfile1,
       "alaDaUNPMacIpPortRuleProfile2": alaDaUNPMacIpPortRuleProfile2,
       "alaDaUNPMacIpPortRuleProfile3": alaDaUNPMacIpPortRuleProfile3,
       "alaDaUNPMacIpPortRuleIpMaskType": alaDaUNPMacIpPortRuleIpMaskType,
       "alaDaUNPMacIpPortRuleIpMask": alaDaUNPMacIpPortRuleIpMask,
       "alaDaUNPMacGroupRuleTable": alaDaUNPMacGroupRuleTable,
       "alaDaUNPMacGroupRuleEntry": alaDaUNPMacGroupRuleEntry,
       "alaDaUNPMacGroupRuleAddr": alaDaUNPMacGroupRuleAddr,
       "alaDaUNPMacGroupRuleId": alaDaUNPMacGroupRuleId,
       "alaDaUNPMacGroupRuleEdgeProf": alaDaUNPMacGroupRuleEdgeProf,
       "alaDaUNPMacGroupRuleRowStatus": alaDaUNPMacGroupRuleRowStatus,
       "alaDaUNPMacGroupRuleVlanTag": alaDaUNPMacGroupRuleVlanTag,
       "alaDaUNPIpGroupRuleTable": alaDaUNPIpGroupRuleTable,
       "alaDaUNPIpGroupRuleEntry": alaDaUNPIpGroupRuleEntry,
       "alaDaUNPIpGroupRuleAddrType": alaDaUNPIpGroupRuleAddrType,
       "alaDaUNPIpGroupRuleAddr": alaDaUNPIpGroupRuleAddr,
       "alaDaUNPIpGroupRuleNum": alaDaUNPIpGroupRuleNum,
       "alaDaUNPIpGroupRuleEdgeProf": alaDaUNPIpGroupRuleEdgeProf,
       "alaDaUNPIpGroupRuleRowStatus": alaDaUNPIpGroupRuleRowStatus,
       "alaDaUNPIpGroupRuleVlanTag": alaDaUNPIpGroupRuleVlanTag,
       "alaDaUNPMacIpGroupRuleTable": alaDaUNPMacIpGroupRuleTable,
       "alaDaUNPMacIpGroupRuleEntry": alaDaUNPMacIpGroupRuleEntry,
       "alaDaUNPMacIpGroupRuleMacAddr": alaDaUNPMacIpGroupRuleMacAddr,
       "alaDaUNPMacIpGroupRuleIpAddrType": alaDaUNPMacIpGroupRuleIpAddrType,
       "alaDaUNPMacIpGroupRuleIpAddr": alaDaUNPMacIpGroupRuleIpAddr,
       "alaDaUNPMacIpGroupRuleId": alaDaUNPMacIpGroupRuleId,
       "alaDaUNPMacIpGroupRuleEdgeProf": alaDaUNPMacIpGroupRuleEdgeProf,
       "alaDaUNPMacIpGroupRuleRowStatus": alaDaUNPMacIpGroupRuleRowStatus,
       "alaDaUNPMacIpGroupRuleVlanTag": alaDaUNPMacIpGroupRuleVlanTag,
       "alaDaUNPUserRoleTable": alaDaUNPUserRoleTable,
       "alaDaUNPUserRoleEntry": alaDaUNPUserRoleEntry,
       "alaDaUNPUserRoleName": alaDaUNPUserRoleName,
       "alaDaUNPUserRolePrecedenceNum": alaDaUNPUserRolePrecedenceNum,
       "alaDaUNPUserRolePolicyList": alaDaUNPUserRolePolicyList,
       "alaDaUNPUserRoleEdgeProfile": alaDaUNPUserRoleEdgeProfile,
       "alaDaUNPUserRoleAuthType": alaDaUNPUserRoleAuthType,
       "alaDaUNPUserRolePostLoginStatus": alaDaUNPUserRolePostLoginStatus,
       "alaDaUNPUserRoleRowStatus": alaDaUNPUserRoleRowStatus,
       "alaDaUNPUserRoleKerberosPostLoginStatus": alaDaUNPUserRoleKerberosPostLoginStatus,
       "alaDaUNPUserRoleProfile1": alaDaUNPUserRoleProfile1,
       "alaDaUNPUserRoleProfile2": alaDaUNPUserRoleProfile2,
       "alaDaUNPUserRoleProfile3": alaDaUNPUserRoleProfile3,
       "alaDaUNPRstrctedRoleTable": alaDaUNPRstrctedRoleTable,
       "alaDaUNPRstrctedRoleEntry": alaDaUNPRstrctedRoleEntry,
       "alaDaUNPRstrctedRoleType": alaDaUNPRstrctedRoleType,
       "alaDaUNPRstrctedRolePolicyList": alaDaUNPRstrctedRolePolicyList,
       "alaDaUNPRstrctedRoleRowStatus": alaDaUNPRstrctedRoleRowStatus,
       "alaDaUNPVlanMapTable": alaDaUNPVlanMapTable,
       "alaDaUNPVlanMapEntry": alaDaUNPVlanMapEntry,
       "alaDaUNPVlanMapEdgeProf": alaDaUNPVlanMapEdgeProf,
       "alaDaUNPVlanMapIdent": alaDaUNPVlanMapIdent,
       "alaDaUNPVlanMapRowStatus": alaDaUNPVlanMapRowStatus,
       "alaDaUnpGroupIdTable": alaDaUnpGroupIdTable,
       "alaDaUnpGroupIdEntry": alaDaUnpGroupIdEntry,
       "alaDaUnpGroupId": alaDaUnpGroupId,
       "alaDaUnpGroupDescription": alaDaUnpGroupDescription,
       "alaDaUnpGroupIdRowStatus": alaDaUnpGroupIdRowStatus,
       "alaDaUNPEdgeFlushTable": alaDaUNPEdgeFlushTable,
       "alaDaUNPEdgeFlushEntry": alaDaUNPEdgeFlushEntry,
       "alaDaUNPEdgeFlushIndex": alaDaUNPEdgeFlushIndex,
       "alaDaUNPEdgeFlushPortLow": alaDaUNPEdgeFlushPortLow,
       "alaDaUNPEdgeFlushPortHigh": alaDaUNPEdgeFlushPortHigh,
       "alaDaUNPEdgeFlushType": alaDaUNPEdgeFlushType,
       "alaDaUNPEdgrFlushMac": alaDaUNPEdgrFlushMac,
       "alaDaUNPEdgeFlushComplete": alaDaUNPEdgeFlushComplete,
       "alaDaUNPEdgeFlushProfile": alaDaUNPEdgeFlushProfile,
       "alaDaUNPMacRulesTable": alaDaUNPMacRulesTable,
       "alaDaUNPMacRulesEntry": alaDaUNPMacRulesEntry,
       "alaDaUNPMacRulesMacAddr": alaDaUNPMacRulesMacAddr,
       "alaDaUNPMacRulesEdgeProf": alaDaUNPMacRulesEdgeProf,
       "alaDaUNPMacRulesRowStatus": alaDaUNPMacRulesRowStatus,
       "alaDaUNPMacRulesVlanTag": alaDaUNPMacRulesVlanTag,
       "alaDaUNPMacRangeTable": alaDaUNPMacRangeTable,
       "alaDaUNPMacRangeEntry": alaDaUNPMacRangeEntry,
       "alaDaUNPMacRangeStartMacAddr": alaDaUNPMacRangeStartMacAddr,
       "alaDaUNPMacRangeEndMacAddr": alaDaUNPMacRangeEndMacAddr,
       "alaDaUNPMacRangeEdgeProf": alaDaUNPMacRangeEdgeProf,
       "alaDaUNPMacRangeRowStatus": alaDaUNPMacRangeRowStatus,
       "alaDaUNPMacRangeVlanTag": alaDaUNPMacRangeVlanTag,
       "alaDaUNPIpMaskRuleTable": alaDaUNPIpMaskRuleTable,
       "alaDaUNPIpMaskRuleEntry": alaDaUNPIpMaskRuleEntry,
       "alaDaUNPIpMaskRuleAddrType": alaDaUNPIpMaskRuleAddrType,
       "alaDaUNPIpMaskRuleAddr": alaDaUNPIpMaskRuleAddr,
       "alaDaUNPIpMaskRuleMaskType": alaDaUNPIpMaskRuleMaskType,
       "alaDaUNPIpMaskRuleMask": alaDaUNPIpMaskRuleMask,
       "alaDaUNPIpMaskRuleEdgeProf": alaDaUNPIpMaskRuleEdgeProf,
       "alaDaUNPIpMaskRuleRowStatus": alaDaUNPIpMaskRuleRowStatus,
       "alaDaUNPIpMaskRuleVlanTag": alaDaUNPIpMaskRuleVlanTag,
       "alaDaQMRMIBObjects": alaDaQMRMIBObjects,
       "alaDaQMRGlobalConfig": alaDaQMRGlobalConfig,
       "alaDaQMRPage": alaDaQMRPage,
       "alaDaQMRPath": alaDaQMRPath,
       "alaDaQMRCustomHttpProxyPort": alaDaQMRCustomHttpProxyPort,
       "alaDaQMRPolicyList": alaDaQMRPolicyList,
       "alaDaQMRAllowedTable": alaDaQMRAllowedTable,
       "alaDaQMRAllowedEntry": alaDaQMRAllowedEntry,
       "alaDaQMRAllowedName": alaDaQMRAllowedName,
       "alaDaQMRAllowedIpAddrType": alaDaQMRAllowedIpAddrType,
       "alaDaQMRAllowedIpAddr": alaDaQMRAllowedIpAddr,
       "alaDaQMRAllowedIpMaskType": alaDaQMRAllowedIpMaskType,
       "alaDaQMRAllowedIpMask": alaDaQMRAllowedIpMask,
       "alaDaQMRAllowedRowStatus": alaDaQMRAllowedRowStatus,
       "alaDaUNPValidityPeriodTable": alaDaUNPValidityPeriodTable,
       "alaDaUNPValidityPeriodEntry": alaDaUNPValidityPeriodEntry,
       "alaDaUNPValidityPeriodName": alaDaUNPValidityPeriodName,
       "alaDaUNPValidityPeriodDays": alaDaUNPValidityPeriodDays,
       "alaDaUNPValidityPeriodDaysStatus": alaDaUNPValidityPeriodDaysStatus,
       "alaDaUNPValidityPeriodMonths": alaDaUNPValidityPeriodMonths,
       "alaDaUNPValidityPeriodMonthsStatus": alaDaUNPValidityPeriodMonthsStatus,
       "alaDaUNPValidityPeriodHour": alaDaUNPValidityPeriodHour,
       "alaDaUNPValidityPeriodHourStatus": alaDaUNPValidityPeriodHourStatus,
       "alaDaUNPValidityPeriodEndHour": alaDaUNPValidityPeriodEndHour,
       "alaDaUNPValidityPeriodInterval": alaDaUNPValidityPeriodInterval,
       "alaDaUNPValidityPeriodIntervalStatus": alaDaUNPValidityPeriodIntervalStatus,
       "alaDaUNPValidityPeriodEndInterval": alaDaUNPValidityPeriodEndInterval,
       "alaDaUNPValidityPeriodTimezone": alaDaUNPValidityPeriodTimezone,
       "alaDaUNPValidityPeriodTimezoneStatus": alaDaUNPValidityPeriodTimezoneStatus,
       "alaDaUNPValidityPeriodActiveStatus": alaDaUNPValidityPeriodActiveStatus,
       "alaDaUNPValidityPeriodRowStatus": alaDaUNPValidityPeriodRowStatus,
       "alaDaUNPLocationPolicyTable": alaDaUNPLocationPolicyTable,
       "alaDaUNPLocationPolicyEntry": alaDaUNPLocationPolicyEntry,
       "alaDaUNPLocationPolicyName": alaDaUNPLocationPolicyName,
       "alaDaUNPLocationPolicyPort": alaDaUNPLocationPolicyPort,
       "alaDaUNPLocationPolicyPortHigh": alaDaUNPLocationPolicyPortHigh,
       "alaDaUNPLocationPolicyPortStatus": alaDaUNPLocationPolicyPortStatus,
       "alaDaUNPLocationPolicySystemName": alaDaUNPLocationPolicySystemName,
       "alaDaUNPLocationPolicySystemLocation": alaDaUNPLocationPolicySystemLocation,
       "alaDaUNPLocationPolicyRowStatus": alaDaUNPLocationPolicyRowStatus,
       "alaDaUNPLocationPolicyDomainId": alaDaUNPLocationPolicyDomainId,
       "alaDaUNPRedirectAllowedServerTable": alaDaUNPRedirectAllowedServerTable,
       "alaDaUNPRedirectAllowedServerEntry": alaDaUNPRedirectAllowedServerEntry,
       "alaDaUNPRedirectAllowedServerName": alaDaUNPRedirectAllowedServerName,
       "alaDaUNPRedirectAllowedServerIPType": alaDaUNPRedirectAllowedServerIPType,
       "alaDaUNPRedirectAllowedServerIP": alaDaUNPRedirectAllowedServerIP,
       "alaDaUNPRedirectAllowedMaskIPType": alaDaUNPRedirectAllowedMaskIPType,
       "alaDaUNPRedirectAllowedMaskIP": alaDaUNPRedirectAllowedMaskIP,
       "alaDaUNPRedirectAllowedRowStatus": alaDaUNPRedirectAllowedRowStatus,
       "alaDaMacVlanUserExtTable": alaDaMacVlanUserExtTable,
       "alaDaMacVlanUserExtEntry": alaDaMacVlanUserExtEntry,
       "alaDaMacVlanUserExtIntfNum": alaDaMacVlanUserExtIntfNum,
       "alaDaMacVlanUserExtMACAddress": alaDaMacVlanUserExtMACAddress,
       "alaDaMacVlanUserExtVlanID": alaDaMacVlanUserExtVlanID,
       "alaDaMacVlanUserExtAppID": alaDaMacVlanUserExtAppID,
       "alaDaMacVlanUserExtAppName": alaDaMacVlanUserExtAppName,
       "alaDaUNPVxlanProfileTable": alaDaUNPVxlanProfileTable,
       "alaDaUNPVxlanProfileEntry": alaDaUNPVxlanProfileEntry,
       "alaDaUNPVxlanProfileName": alaDaUNPVxlanProfileName,
       "alaDaUNPVxlanProfileEncapVal": alaDaUNPVxlanProfileEncapVal,
       "alaDaUNPVxlanProfileVnid": alaDaUNPVxlanProfileVnid,
       "alaDaUNPVxlanProfileQosPolicyListName": alaDaUNPVxlanProfileQosPolicyListName,
       "alaDaUNPVxlanProfileFarEndIPListName": alaDaUNPVxlanProfileFarEndIPListName,
       "alaDaUNPVxlanProfileMulticastIPAddressType": alaDaUNPVxlanProfileMulticastIPAddressType,
       "alaDaUNPVxlanProfileMulticastIPAddress": alaDaUNPVxlanProfileMulticastIPAddress,
       "alaDaUNPVxlanProfileSapVlanXlation": alaDaUNPVxlanProfileSapVlanXlation,
       "alaDaUNPVxlanProfileMobileTagStatus": alaDaUNPVxlanProfileMobileTagStatus,
       "alaDaUNPVxlanProfileMulticastMode": alaDaUNPVxlanProfileMulticastMode,
       "alaDaUNPVxlanProfileRowStatus": alaDaUNPVxlanProfileRowStatus,
       "alaDaUNPVxlanFlushTable": alaDaUNPVxlanFlushTable,
       "alaDaUNPVxlanFlushEntry": alaDaUNPVxlanFlushEntry,
       "alaDaUNPVxlanFlushIndex": alaDaUNPVxlanFlushIndex,
       "alaDaUNPVxlanFlushComplete": alaDaUNPVxlanFlushComplete,
       "alaDaUNPVxlanFlushAuthType": alaDaUNPVxlanFlushAuthType,
       "alaDaUNPVxlanFlushMacAddress": alaDaUNPVxlanFlushMacAddress,
       "alaDaUNPVxlanFlushSapIDIfIndex": alaDaUNPVxlanFlushSapIDIfIndex,
       "alaDaUNPVxlanFlushSapIDEncapVal": alaDaUNPVxlanFlushSapIDEncapVal,
       "alaDaUNPVxlanFlushServiceID": alaDaUNPVxlanFlushServiceID,
       "alaDaUNPVxlanFlushVxlanProfile": alaDaUNPVxlanFlushVxlanProfile,
       "alaDaUNPVxlanFarEndIPListTable": alaDaUNPVxlanFarEndIPListTable,
       "alaDaUNPVxlanFarEndIPListEntry": alaDaUNPVxlanFarEndIPListEntry,
       "alaDaUNPVxlanFarEndIPListName": alaDaUNPVxlanFarEndIPListName,
       "alaDaUNPVxlanFarEndIPListIPAddressCount": alaDaUNPVxlanFarEndIPListIPAddressCount,
       "alaDaUNPVxlanFarEndIPListRemove": alaDaUNPVxlanFarEndIPListRemove,
       "alaDaUNPVxlanFarEndIPAddressListTable": alaDaUNPVxlanFarEndIPAddressListTable,
       "alaDaUNPVxlanFarEndIPAddressListEntry": alaDaUNPVxlanFarEndIPAddressListEntry,
       "alaDaUNPVxlanFarEndIPAddressListIPType": alaDaUNPVxlanFarEndIPAddressListIPType,
       "alaDaUNPVxlanFarEndIPAddressListIP": alaDaUNPVxlanFarEndIPAddressListIP,
       "alaDaUNPVxlanFarEndIPAddressListRowStatus": alaDaUNPVxlanFarEndIPAddressListRowStatus,
       "alaDaUNPSpbFlushTable": alaDaUNPSpbFlushTable,
       "alaDaUNPSpbFlushEntry": alaDaUNPSpbFlushEntry,
       "alaDaUNPSpbFlushIndex": alaDaUNPSpbFlushIndex,
       "alaDaUNPSpbFlushComplete": alaDaUNPSpbFlushComplete,
       "alaDaUNPSpbFlushAuthType": alaDaUNPSpbFlushAuthType,
       "alaDaUNPSpbFlushMacAddress": alaDaUNPSpbFlushMacAddress,
       "alaDaUNPSpbFlushSapIDIfIndex": alaDaUNPSpbFlushSapIDIfIndex,
       "alaDaUNPSpbFlushSapIDEncapVal": alaDaUNPSpbFlushSapIDEncapVal,
       "alaDaUNPSpbFlushServiceID": alaDaUNPSpbFlushServiceID,
       "alaDaUNPSpbFlushSpbProfile": alaDaUNPSpbFlushSpbProfile,
       "alaDaKerberosMIBObjects": alaDaKerberosMIBObjects,
       "alaDaKerberosGlobalConfig": alaDaKerberosGlobalConfig,
       "alaDaKerberosGlobalMacMoveStatus": alaDaKerberosGlobalMacMoveStatus,
       "alaDaKerberosGlobalInactivityTimer": alaDaKerberosGlobalInactivityTimer,
       "alaDaKerberosGlobalPolicy": alaDaKerberosGlobalPolicy,
       "alaDaKerberosGlobalPolicyStatus": alaDaKerberosGlobalPolicyStatus,
       "alaDaKerberosClientPktHwDiscardStats": alaDaKerberosClientPktHwDiscardStats,
       "alaDaKerberosServerPktHwDiscardStats": alaDaKerberosServerPktHwDiscardStats,
       "alaDaKerberosTotalClientPktRxStats": alaDaKerberosTotalClientPktRxStats,
       "alaDaKerberosTotalServerPktRxStats": alaDaKerberosTotalServerPktRxStats,
       "alaDaKerberosClientPktSwDiscardStats": alaDaKerberosClientPktSwDiscardStats,
       "alaDaKerberosServerPktSwDiscardStats": alaDaKerberosServerPktSwDiscardStats,
       "alaDaKerberosTotalASREQRxStats": alaDaKerberosTotalASREQRxStats,
       "alaDaKerberosTotalASREPRxStats": alaDaKerberosTotalASREPRxStats,
       "alaDaKerberosTotalTGSREQRxStats": alaDaKerberosTotalTGSREQRxStats,
       "alaDaKerberosTotalTGSREPRxStats": alaDaKerberosTotalTGSREPRxStats,
       "alaDaKerberosTotalErrorRxStats": alaDaKerberosTotalErrorRxStats,
       "alaDaKerberosGlobalClearStats": alaDaKerberosGlobalClearStats,
       "alaDaKerberosGlobalClearPortStats": alaDaKerberosGlobalClearPortStats,
       "alaDaKerberosGlobalServerTimeoutTimer": alaDaKerberosGlobalServerTimeoutTimer,
       "alaDaKerberosPolicyConfigTable": alaDaKerberosPolicyConfigTable,
       "alaDaKerberosPolicyConfigEntry": alaDaKerberosPolicyConfigEntry,
       "alaDaKerberosPolicyDomainName": alaDaKerberosPolicyDomainName,
       "alaDaKerberosPolicyName": alaDaKerberosPolicyName,
       "alaDaKerberosPolicyStatus": alaDaKerberosPolicyStatus,
       "alaDaKerberosPolicyRowStatus": alaDaKerberosPolicyRowStatus,
       "alaDaKerberosUserTable": alaDaKerberosUserTable,
       "alaDaKerberosUserEntry": alaDaKerberosUserEntry,
       "alaDaKerberosUserMac": alaDaKerberosUserMac,
       "alaDaKerberosUserPort": alaDaKerberosUserPort,
       "alaDaKerberosUserName": alaDaKerberosUserName,
       "alaDaKerberosUserDomain": alaDaKerberosUserDomain,
       "alaDaKerberosUserAuthState": alaDaKerberosUserAuthState,
       "alaDaKerberosUserPolicy": alaDaKerberosUserPolicy,
       "alaDaKerberosUserLeftTime": alaDaKerberosUserLeftTime,
       "alaDaKerberosUserState": alaDaKerberosUserState,
       "alaDaKerberosPortStatsTable": alaDaKerberosPortStatsTable,
       "alaDaKerberosPortStatsEntry": alaDaKerberosPortStatsEntry,
       "alaDaKerberosStatsIfIndex": alaDaKerberosStatsIfIndex,
       "alaDaKerberosPortClearStats": alaDaKerberosPortClearStats,
       "alaDaKerberosPortClientPktRxStats": alaDaKerberosPortClientPktRxStats,
       "alaDaKerberosPortServerPktRxStats": alaDaKerberosPortServerPktRxStats,
       "alaDaKerberosPortClientPktSwDiscardStats": alaDaKerberosPortClientPktSwDiscardStats,
       "alaDaKerberosPortServerPktSwDiscardStats": alaDaKerberosPortServerPktSwDiscardStats,
       "alaDaKerberosPortASREQRxStats": alaDaKerberosPortASREQRxStats,
       "alaDaKerberosPortASREPRxStats": alaDaKerberosPortASREPRxStats,
       "alaDaKerberosPortTGSREQRxStats": alaDaKerberosPortTGSREQRxStats,
       "alaDaKerberosPortTGSREPRxStats": alaDaKerberosPortTGSREPRxStats,
       "alaDaKerberosPortErrorRxStats": alaDaKerberosPortErrorRxStats,
       "alaDaKerberosServerTable": alaDaKerberosServerTable,
       "alaDaKerberosServerEntry": alaDaKerberosServerEntry,
       "alaDaKerberosIpAddressType": alaDaKerberosIpAddressType,
       "alaDaKerberosIpAddress": alaDaKerberosIpAddress,
       "alaDaKerberosUdpPort": alaDaKerberosUdpPort,
       "alaDaKerberosRowStatus": alaDaKerberosRowStatus,
       "alaDaUNPPortVlanTable": alaDaUNPPortVlanTable,
       "alaDaUNPPortVlanEntry": alaDaUNPPortVlanEntry,
       "alaDaUNPPortVlanVID": alaDaUNPPortVlanVID,
       "alaDaUNPPortVlanRowStatus": alaDaUNPPortVlanRowStatus,
       "alaDaUNPPortVlanType": alaDaUNPPortVlanType,
       "alaDaUNPVlanRuleTable": alaDaUNPVlanRuleTable,
       "alaDaUNPVlanRuleEntry": alaDaUNPVlanRuleEntry,
       "alaDaUNPVlanRuleVlanTag": alaDaUNPVlanRuleVlanTag,
       "alaDaUNPVlanRuleVlanTagPosition": alaDaUNPVlanRuleVlanTagPosition,
       "alaDaUNPVlanRuleEdgeProf": alaDaUNPVlanRuleEdgeProf,
       "alaDaUNPVlanRuleRowStatus": alaDaUNPVlanRuleRowStatus,
       "alaDaUNPETmplVlanTable": alaDaUNPETmplVlanTable,
       "alaDaUNPETmplVlanEntry": alaDaUNPETmplVlanEntry,
       "alaDaUNPETmplVlanVID": alaDaUNPETmplVlanVID,
       "alaDaUNPETmplVlanRowStatus": alaDaUNPETmplVlanRowStatus,
       "alaDaUNPUserFlushTable": alaDaUNPUserFlushTable,
       "alaDaUNPUserFlushEntry": alaDaUNPUserFlushEntry,
       "alaDaUNPUserFlushIndex": alaDaUNPUserFlushIndex,
       "alaDaUNPUserFlushComplete": alaDaUNPUserFlushComplete,
       "alaDaUNPUserFlushAuthType": alaDaUNPUserFlushAuthType,
       "alaDaUNPUserFlushMacAddress": alaDaUNPUserFlushMacAddress,
       "alaDaUNPUserFlushProfile": alaDaUNPUserFlushProfile,
       "alaDaUNPUserFlushPortStart": alaDaUNPUserFlushPortStart,
       "alaDaUNPUserFlushPortEnd": alaDaUNPUserFlushPortEnd,
       "alaDaUNPUserFlushSapIDIfIndex": alaDaUNPUserFlushSapIDIfIndex,
       "alaDaUNPUserFlushSapIDEncapVal": alaDaUNPUserFlushSapIDEncapVal,
       "alaDaUNPUserFlushServiceID": alaDaUNPUserFlushServiceID,
       "alaDaUNPCustDomainRuleTable": alaDaUNPCustDomainRuleTable,
       "alaDaUNPCustDomainRuleEntry": alaDaUNPCustDomainRuleEntry,
       "alaDaUNPCustDomainRuleId": alaDaUNPCustDomainRuleId,
       "alaDaUNPCustDomainRuleVlanTag": alaDaUNPCustDomainRuleVlanTag,
       "alaDaUNPCustDomainRuleProfile1": alaDaUNPCustDomainRuleProfile1,
       "alaDaUNPCustDomainRuleProfile2": alaDaUNPCustDomainRuleProfile2,
       "alaDaUNPCustDomainRuleProfile3": alaDaUNPCustDomainRuleProfile3,
       "alaDaUNPCustDomainRuleRowStatus": alaDaUNPCustDomainRuleRowStatus,
       "alaDaUNPPortTemplateTable": alaDaUNPPortTemplateTable,
       "alaDaUNPPortTemplateEntry": alaDaUNPPortTemplateEntry,
       "alaDaUNPPortTemplateName": alaDaUNPPortTemplateName,
       "alaDaUNPPortTemplateAdminState": alaDaUNPPortTemplateAdminState,
       "alaDaUNPPortTemplateDirection": alaDaUNPPortTemplateDirection,
       "alaDaUNPPortTemplateDomainID": alaDaUNPPortTemplateDomainID,
       "alaDaUNPPortTemplateClassification": alaDaUNPPortTemplateClassification,
       "alaDaUNPPortTemplateTrustTag": alaDaUNPPortTemplateTrustTag,
       "alaDaUNPPortTemplateDynamicService": alaDaUNPPortTemplateDynamicService,
       "alaDaUNPPortTemplateDefaultProfile": alaDaUNPPortTemplateDefaultProfile,
       "alaDaUNPPortTemplateAAAProfile": alaDaUNPPortTemplateAAAProfile,
       "alaDaUNPPortTemplateRedirectPortBounce": alaDaUNPPortTemplateRedirectPortBounce,
       "alaDaUNPPortTemplate8021XAuth": alaDaUNPPortTemplate8021XAuth,
       "alaDaUNPPortTemplate8021XAuthPassAlternate": alaDaUNPPortTemplate8021XAuthPassAlternate,
       "alaDaUNPPortTemplate8021XAuthBypass": alaDaUNPPortTemplate8021XAuthBypass,
       "alaDaUNPPortTemplate8021XAuthFailPolicy": alaDaUNPPortTemplate8021XAuthFailPolicy,
       "alaDaUNPPortTemplate8021XAuthTxPeriod": alaDaUNPPortTemplate8021XAuthTxPeriod,
       "alaDaUNPPortTemplate8021XAuthSuppTimeout": alaDaUNPPortTemplate8021XAuthSuppTimeout,
       "alaDaUNPPortTemplate8021XAuthMaxReq": alaDaUNPPortTemplate8021XAuthMaxReq,
       "alaDaUNPPortTemplateMACAuth": alaDaUNPPortTemplateMACAuth,
       "alaDaUNPPortTemplateMACAuthPassAlternate": alaDaUNPPortTemplateMACAuthPassAlternate,
       "alaDaUNPPortTemplateMACAuthAllowEAP": alaDaUNPPortTemplateMACAuthAllowEAP,
       "alaDaUNPPortTemplateForceL3Learning": alaDaUNPPortTemplateForceL3Learning,
       "alaDaUNPPortTemplateForceL3LearningPortBounce": alaDaUNPPortTemplateForceL3LearningPortBounce,
       "alaDaUNPPortTemplateRowStatus": alaDaUNPPortTemplateRowStatus,
       "alaDaUNPPortTemplateL2Profile": alaDaUNPPortTemplateL2Profile,
       "alaDaUNPPortTemplateApMode": alaDaUNPPortTemplateApMode,
       "alaDaUNPPortTemplateApModeSecurity": alaDaUNPPortTemplateApModeSecurity,
       "alaDaUNPPortTemplateSwSuppSecureMode": alaDaUNPPortTemplateSwSuppSecureMode,
       "alaDaUNPPortTemplateBpduLldpLearn": alaDaUNPPortTemplateBpduLldpLearn,
       "alaDaUNPProfileTable": alaDaUNPProfileTable,
       "alaDaUNPProfileEntry": alaDaUNPProfileEntry,
       "alaDaUNPProfileName": alaDaUNPProfileName,
       "alaDaUNPProfileAuthenticationFlag": alaDaUNPProfileAuthenticationFlag,
       "alaDaUNPProfileMobileTag": alaDaUNPProfileMobileTag,
       "alaDaUNPProfileCPortalAuthentication": alaDaUNPProfileCPortalAuthentication,
       "alaDaUNPProfileRedirect": alaDaUNPProfileRedirect,
       "alaDaUNPProfileQoSPolicy": alaDaUNPProfileQoSPolicy,
       "alaDaUNPProfilePeriodPolicy": alaDaUNPProfilePeriodPolicy,
       "alaDaUNPProfileCPortalProfile": alaDaUNPProfileCPortalProfile,
       "alaDaUNPProfileLocationPolicy": alaDaUNPProfileLocationPolicy,
       "alaDaUNPProfileSaaProfile": alaDaUNPProfileSaaProfile,
       "alaDaUNPProfileInactivityInterval": alaDaUNPProfileInactivityInterval,
       "alaDaUNPProfileKerberosAuthentication": alaDaUNPProfileKerberosAuthentication,
       "alaDaUNPProfileMaxIngressBandwidth": alaDaUNPProfileMaxIngressBandwidth,
       "alaDaUNPProfileMaxEgressBandwidth": alaDaUNPProfileMaxEgressBandwidth,
       "alaDaUNPProfileMaxIngressDepth": alaDaUNPProfileMaxIngressDepth,
       "alaDaUNPProfileMaxEgressDepth": alaDaUNPProfileMaxEgressDepth,
       "alaDaUNPProfileRowStatus": alaDaUNPProfileRowStatus,
       "alaDaUNPProfileAFDConfig": alaDaUNPProfileAFDConfig,
       "alaDaUNPProfileMacMobility": alaDaUNPProfileMacMobility,
       "alaDaUNPProfileMapVlanTable": alaDaUNPProfileMapVlanTable,
       "alaDaUNPProfileMapVlanEntry": alaDaUNPProfileMapVlanEntry,
       "alaDaUNPProfileMapVlanVlanID": alaDaUNPProfileMapVlanVlanID,
       "alaDaUNPProfileMapVlanRowStatus": alaDaUNPProfileMapVlanRowStatus,
       "alaDaUNPProfileMapSpbTable": alaDaUNPProfileMapSpbTable,
       "alaDaUNPProfileMapSpbEntry": alaDaUNPProfileMapSpbEntry,
       "alaDaUNPProfileMapSpbEncapVal": alaDaUNPProfileMapSpbEncapVal,
       "alaDaUNPProfileMapSpbIsid": alaDaUNPProfileMapSpbIsid,
       "alaDaUNPProfileMapSpbBVlan": alaDaUNPProfileMapSpbBVlan,
       "alaDaUNPProfileMapSpbMulticastMode": alaDaUNPProfileMapSpbMulticastMode,
       "alaDaUNPProfileMapSpbVlanXlation": alaDaUNPProfileMapSpbVlanXlation,
       "alaDaUNPProfileMapSpbRowStatus": alaDaUNPProfileMapSpbRowStatus,
       "alaDaUNPProfileMapSpbIgmpSnooping": alaDaUNPProfileMapSpbIgmpSnooping,
       "alaDaUNPProfileMapSpbIgmpProfile": alaDaUNPProfileMapSpbIgmpProfile,
       "alaDaUNPProfileMapSpbMldSnooping": alaDaUNPProfileMapSpbMldSnooping,
       "alaDaUNPProfileMapSpbMldProfile": alaDaUNPProfileMapSpbMldProfile,
       "alaDaUNPProfileMapSpbRemoveIngressTag": alaDaUNPProfileMapSpbRemoveIngressTag,
       "alaDaUNPProfileMapSpbETree": alaDaUNPProfileMapSpbETree,
       "alaDaUNPProfileMapVxlanTable": alaDaUNPProfileMapVxlanTable,
       "alaDaUNPProfileMapVxlanEntry": alaDaUNPProfileMapVxlanEntry,
       "alaDaUNPProfileMapVxlanEncapVal": alaDaUNPProfileMapVxlanEncapVal,
       "alaDaUNPProfileMapVxlanVnid": alaDaUNPProfileMapVxlanVnid,
       "alaDaUNPProfileMapVxlanFarEndIPList": alaDaUNPProfileMapVxlanFarEndIPList,
       "alaDaUNPProfileMapVxlanMulticastIPAddressType": alaDaUNPProfileMapVxlanMulticastIPAddressType,
       "alaDaUNPProfileMapVxlanMulticastIPAddress": alaDaUNPProfileMapVxlanMulticastIPAddress,
       "alaDaUNPProfileMapVxlanVlanXlation": alaDaUNPProfileMapVxlanVlanXlation,
       "alaDaUNPProfileMapVxlanMulticastMode": alaDaUNPProfileMapVxlanMulticastMode,
       "alaDaUNPProfileMapVxlanRowStatus": alaDaUNPProfileMapVxlanRowStatus,
       "alaDaUNPProfileMapVxlanMacOrchestration": alaDaUNPProfileMapVxlanMacOrchestration,
       "alaDaUNPProfileMapVxlanRemoveIngressTag": alaDaUNPProfileMapVxlanRemoveIngressTag,
       "alaDaUNPProfileMapVxlanTcpMss": alaDaUNPProfileMapVxlanTcpMss,
       "alaDaUNPProfileMapVxlanTcpMssOverlayProfile": alaDaUNPProfileMapVxlanTcpMssOverlayProfile,
       "alaDaUNPProfileMapStaticTable": alaDaUNPProfileMapStaticTable,
       "alaDaUNPProfileMapStaticEntry": alaDaUNPProfileMapStaticEntry,
       "alaDaUNPProfileMapStaticEncapVal": alaDaUNPProfileMapStaticEncapVal,
       "alaDaUNPProfileMapStaticServiceID": alaDaUNPProfileMapStaticServiceID,
       "alaDaUNPProfileMapStaticRowStatus": alaDaUNPProfileMapStaticRowStatus,
       "alaDaUNPCustDomainMacIpRuleTable": alaDaUNPCustDomainMacIpRuleTable,
       "alaDaUNPCustDomainMacIpRuleEntry": alaDaUNPCustDomainMacIpRuleEntry,
       "alaDaUNPCustDomainMacIpRuleMacAddr": alaDaUNPCustDomainMacIpRuleMacAddr,
       "alaDaUNPCustDomainMacIpRuleIpAddrType": alaDaUNPCustDomainMacIpRuleIpAddrType,
       "alaDaUNPCustDomainMacIpRuleIpAddr": alaDaUNPCustDomainMacIpRuleIpAddr,
       "alaDaUNPCustDomainMacIpRuleDomainId": alaDaUNPCustDomainMacIpRuleDomainId,
       "alaDaUNPCustDomainMacIpRuleVlanTag": alaDaUNPCustDomainMacIpRuleVlanTag,
       "alaDaUNPCustDomainMacIpRuleProfile1": alaDaUNPCustDomainMacIpRuleProfile1,
       "alaDaUNPCustDomainMacIpRuleProfile2": alaDaUNPCustDomainMacIpRuleProfile2,
       "alaDaUNPCustDomainMacIpRuleProfile3": alaDaUNPCustDomainMacIpRuleProfile3,
       "alaDaUNPCustDomainMacIpRuleRowStatus": alaDaUNPCustDomainMacIpRuleRowStatus,
       "alaDaUNPCustDomainMacIpRuleIpMaskType": alaDaUNPCustDomainMacIpRuleIpMaskType,
       "alaDaUNPCustDomainMacIpRuleIpMask": alaDaUNPCustDomainMacIpRuleIpMask,
       "alaDaUNPPortTemplateVlanTable": alaDaUNPPortTemplateVlanTable,
       "alaDaUNPPortTemplateVlanEntry": alaDaUNPPortTemplateVlanEntry,
       "alaDaUNPPortTemplateVlanVID": alaDaUNPPortTemplateVlanVID,
       "alaDaUNPPortTemplateVlanRowStatus": alaDaUNPPortTemplateVlanRowStatus,
       "alaDaUNPPortTemplateVlanType": alaDaUNPPortTemplateVlanType,
       "alaDaUNPWlanConfiguration": alaDaUNPWlanConfiguration,
       "alaDaUNPWlanMode": alaDaUNPWlanMode,
       "alaDaUNPWlanManagementVlan": alaDaUNPWlanManagementVlan,
       "alaDaUNPWlanAuthenticationFlag": alaDaUNPWlanAuthenticationFlag,
       "alaDaUNPWlanForceDefWlanProfile": alaDaUNPWlanForceDefWlanProfile,
       "alaDaUNPWlanAuthServerDownFallback": alaDaUNPWlanAuthServerDownFallback,
       "alaDaUNPWlanSecurityLevel": alaDaUNPWlanSecurityLevel,
       "alaDaUNPProfileMapL2GreTable": alaDaUNPProfileMapL2GreTable,
       "alaDaUNPProfileL2GreEntry": alaDaUNPProfileL2GreEntry,
       "alaDaUNPProfileMapL2GreEncapVal": alaDaUNPProfileMapL2GreEncapVal,
       "alaDaUNPProfileMapL2GreVpnid": alaDaUNPProfileMapL2GreVpnid,
       "alaDaUNPProfileMapL2GreFarEndIPAddressType": alaDaUNPProfileMapL2GreFarEndIPAddressType,
       "alaDaUNPProfileMapL2GreFarEndIPAddress": alaDaUNPProfileMapL2GreFarEndIPAddress,
       "alaDaUNPProfileMapL2GreFarEndIPList": alaDaUNPProfileMapL2GreFarEndIPList,
       "alaDaUNPProfileMapL2GreRowStatus": alaDaUNPProfileMapL2GreRowStatus,
       "alaDaUNPProfileMapL2GreVlanXlation": alaDaUNPProfileMapL2GreVlanXlation,
       "alaDaUNPProfileMapL2GreRemoveIngressTag": alaDaUNPProfileMapL2GreRemoveIngressTag,
       "alaDaUNPL2GreFarEndIPListTable": alaDaUNPL2GreFarEndIPListTable,
       "alaDaUNPL2GreFarEndIPListEntry": alaDaUNPL2GreFarEndIPListEntry,
       "alaDaUNPL2GreFarEndIPListName": alaDaUNPL2GreFarEndIPListName,
       "alaDaUNPL2GreFarEndIPListIPAddressCount": alaDaUNPL2GreFarEndIPListIPAddressCount,
       "alaDaUNPL2GreFarEndIPListRemove": alaDaUNPL2GreFarEndIPListRemove,
       "alaDaUNPL2GreFarEndIPAddressListTable": alaDaUNPL2GreFarEndIPAddressListTable,
       "alaDaUNPL2GreFarEndIPAddressListEntry": alaDaUNPL2GreFarEndIPAddressListEntry,
       "alaDaUNPL2GreFarEndIPAddressListIPType": alaDaUNPL2GreFarEndIPAddressListIPType,
       "alaDaUNPL2GreFarEndIPAddressListIP": alaDaUNPL2GreFarEndIPAddressListIP,
       "alaDaUNPL2GreFarEndIPAddressListRowStatus": alaDaUNPL2GreFarEndIPAddressListRowStatus,
       "alaDaUNPNetworkGroupTable": alaDaUNPNetworkGroupTable,
       "alaDaUNPNetworkGroupEntry": alaDaUNPNetworkGroupEntry,
       "alaDaUNPNetworkGroupName": alaDaUNPNetworkGroupName,
       "alaDaUNPNetworkGroupIpAddrType": alaDaUNPNetworkGroupIpAddrType,
       "alaDaUNPNetworkGroupIpAddr": alaDaUNPNetworkGroupIpAddr,
       "alaDaUNPNetworkGroupIpMask": alaDaUNPNetworkGroupIpMask,
       "alaDaUNPNetworkGroupRowStatus": alaDaUNPNetworkGroupRowStatus,
       "alaDaUNPRouterAuthUserGroupTable": alaDaUNPRouterAuthUserGroupTable,
       "alaDaUNPRouterAuthUserGroupEntry": alaDaUNPRouterAuthUserGroupEntry,
       "alaDaUNPRouterAuthenticationName": alaDaUNPRouterAuthenticationName,
       "alaDaUNPRouterAuthenticationSrcGroup": alaDaUNPRouterAuthenticationSrcGroup,
       "alaDaUNPRouterAuthenticationDestGroup": alaDaUNPRouterAuthenticationDestGroup,
       "alaDaUNPRouterAuthenticationRowStatus": alaDaUNPRouterAuthenticationRowStatus,
       "alaDaUNPRouterAuthenticationConfig": alaDaUNPRouterAuthenticationConfig,
       "alaDaUNPRouterAuthCpProfileName": alaDaUNPRouterAuthCpProfileName,
       "alaDaUNPRouterAuthenticationFlushTable": alaDaUNPRouterAuthenticationFlushTable,
       "alaDaUNPRouterAuthenticationFlushEntry": alaDaUNPRouterAuthenticationFlushEntry,
       "alaDaUNPRouterAuthenticationFlushIndex": alaDaUNPRouterAuthenticationFlushIndex,
       "alaDaUNPRouterAuthenticationFlushComplete": alaDaUNPRouterAuthenticationFlushComplete,
       "alaDaUNPRouterAuthenticationFlushUserGroupName": alaDaUNPRouterAuthenticationFlushUserGroupName,
       "alaDaUNPRouterAuthenticationFlushType": alaDaUNPRouterAuthenticationFlushType,
       "alaDaUNPRouterAuthenticationFlushUserName": alaDaUNPRouterAuthenticationFlushUserName,
       "alaDaUNPRouterAuthenticationFlushIpAddressType": alaDaUNPRouterAuthenticationFlushIpAddressType,
       "alaDaUNPRouterAuthenticationFlushIpAddress": alaDaUNPRouterAuthenticationFlushIpAddress,
       "alaDaUNPPortProfileTable": alaDaUNPPortProfileTable,
       "alaDaUNPPortProfileEntry": alaDaUNPPortProfileEntry,
       "alaDaUNPPortProfileName": alaDaUNPPortProfileName,
       "alaDaUNPPortProfileRowStatus": alaDaUNPPortProfileRowStatus,
       "alaDaUNPPortTemplateProfileTable": alaDaUNPPortTemplateProfileTable,
       "alaDaUNPPortTemplateProfileEntry": alaDaUNPPortTemplateProfileEntry,
       "alaDaUNPPortTemplateProfileName": alaDaUNPPortTemplateProfileName,
       "alaDaUNPPortTemplateProfileRowStatus": alaDaUNPPortTemplateProfileRowStatus,
       "alaDaUnpRouterAuthenticationUserTable": alaDaUnpRouterAuthenticationUserTable,
       "alaDaUnpRouterAuthenticationUserEntry": alaDaUnpRouterAuthenticationUserEntry,
       "alaDaUNPRouterAuthenticationUserIpType": alaDaUNPRouterAuthenticationUserIpType,
       "alaDaUNPRouterAuthenticationUserIpAddress": alaDaUNPRouterAuthenticationUserIpAddress,
       "alaDaUNPRouterAuthenticationUserName": alaDaUNPRouterAuthenticationUserName,
       "alaDaUNPRouterAuthenticationUserDestinationGroup": alaDaUNPRouterAuthenticationUserDestinationGroup,
       "alaDaUNPRouterAuthenticationUserInterfaceName": alaDaUNPRouterAuthenticationUserInterfaceName,
       "alaDaUNPRouterAuthenticationUserVlan": alaDaUNPRouterAuthenticationUserVlan,
       "alaDaUNPRouterAuthenticationUserAuthType": alaDaUNPRouterAuthenticationUserAuthType,
       "alaDaUNPRouterAuthenticationUserAuthStatus": alaDaUNPRouterAuthenticationUserAuthStatus,
       "alaDaUNPRouterAuthenticationUserLoginTime": alaDaUNPRouterAuthenticationUserLoginTime,
       "alaDaUNPRouterAuthenticationUserSessionRemainingTime": alaDaUNPRouterAuthenticationUserSessionRemainingTime,
       "alaDaUNPRedirectAllowedWebServerTable": alaDaUNPRedirectAllowedWebServerTable,
       "alaDaUNPRedirectAllowedWebServerEntry": alaDaUNPRedirectAllowedWebServerEntry,
       "alaDaUNPRedirectAllowedWebServerName": alaDaUNPRedirectAllowedWebServerName,
       "alaDaUNPRedirectAllowedWebServerIpAddressType": alaDaUNPRedirectAllowedWebServerIpAddressType,
       "alaDaUNPRedirectAllowedWebServerIpAddress": alaDaUNPRedirectAllowedWebServerIpAddress,
       "alaDaUNPRedirectAllowedWebServerFQDN": alaDaUNPRedirectAllowedWebServerFQDN,
       "alaDaUNPRedirectAllowedWebServerFQDNResolvedTime": alaDaUNPRedirectAllowedWebServerFQDNResolvedTime,
       "alaDaUNPRedirectAllowedWebServerRowStatus": alaDaUNPRedirectAllowedWebServerRowStatus,
       "alaDaUNPRedirectAllowedWebServerIpAddrStatus": alaDaUNPRedirectAllowedWebServerIpAddrStatus,
       "alaDaUNPFQDNResolvedIPTable": alaDaUNPFQDNResolvedIPTable,
       "alaDaUNPFQDNResolvedIPEntry": alaDaUNPFQDNResolvedIPEntry,
       "alaDaUNPFQDNResolvedIPName": alaDaUNPFQDNResolvedIPName,
       "alaDaUNPFQDNResolvedIPAddressType": alaDaUNPFQDNResolvedIPAddressType,
       "alaDaUNPFQDNResolvedIPAddress": alaDaUNPFQDNResolvedIPAddress,
       "alaDaUNPFQDNResolvedIPAddressStatus": alaDaUNPFQDNResolvedIPAddressStatus,
       "alaDaUNPProfileMapVplsTable": alaDaUNPProfileMapVplsTable,
       "alaDaUNPProfileVplsEntry": alaDaUNPProfileVplsEntry,
       "alaDaUNPProfileMapVplsEncapVal": alaDaUNPProfileMapVplsEncapVal,
       "alaDaUNPProfileMapVplsID": alaDaUNPProfileMapVplsID,
       "alaDaUNPProfileMapVplsLdpFarEndIPList": alaDaUNPProfileMapVplsLdpFarEndIPList,
       "alaDaUNPProfileMapVplsBgpVeID": alaDaUNPProfileMapVplsBgpVeID,
       "alaDaUNPProfileMapVplsVlanXlation": alaDaUNPProfileMapVplsVlanXlation,
       "alaDaUNPProfileMapVplsRemoveIngressTag": alaDaUNPProfileMapVplsRemoveIngressTag,
       "alaDaUNPProfileMapVplsRowStatus": alaDaUNPProfileMapVplsRowStatus,
       "alaDaUNPVplsFarEndIPListTable": alaDaUNPVplsFarEndIPListTable,
       "alaDaUNPVplsFarEndIPListEntry": alaDaUNPVplsFarEndIPListEntry,
       "alaDaUNPVplsFarEndIPListName": alaDaUNPVplsFarEndIPListName,
       "alaDaUNPVplsFarEndIPListIPAddressCount": alaDaUNPVplsFarEndIPListIPAddressCount,
       "alaDaUNPVplsFarEndIPListRemove": alaDaUNPVplsFarEndIPListRemove,
       "alaDaUNPVplsFarEndIPAddressListTable": alaDaUNPVplsFarEndIPAddressListTable,
       "alaDaUNPVplsFarEndIPAddressListEntry": alaDaUNPVplsFarEndIPAddressListEntry,
       "alaDaUNPVplsFarEndIPAddressListIPType": alaDaUNPVplsFarEndIPAddressListIPType,
       "alaDaUNPVplsFarEndIPAddressListIP": alaDaUNPVplsFarEndIPAddressListIP,
       "alaDaUNPVplsFarEndIPAddressListRowStatus": alaDaUNPVplsFarEndIPAddressListRowStatus,
       "alaDaUNPProfileTrustTaggedVlanTable": alaDaUNPProfileTrustTaggedVlanTable,
       "alaDaUNPProfileTrustTaggedVlanEntry": alaDaUNPProfileTrustTaggedVlanEntry,
       "alaDaUNPProfileTrustTaggedVlanIDStart": alaDaUNPProfileTrustTaggedVlanIDStart,
       "alaDaUNPProfileTrustTaggedVlanIDEnd": alaDaUNPProfileTrustTaggedVlanIDEnd,
       "alaDaUNPProfileTrustTaggedVlanRowStatus": alaDaUNPProfileTrustTaggedVlanRowStatus,
       "alaDaUNPApModeMacOuiTable": alaDaUNPApModeMacOuiTable,
       "alaDaUNPApModeMacOuiEntry": alaDaUNPApModeMacOuiEntry,
       "alaDaUNPApModeMacOui": alaDaUNPApModeMacOui,
       "alaDaUNPApModeMacOuiRowStatus": alaDaUNPApModeMacOuiRowStatus,
       "alaIND1DaMIBConformance": alaIND1DaMIBConformance,
       "alaIND1DaMIBGroups": alaIND1DaMIBGroups,
       "alaDaUserNetProfileGroup": alaDaUserNetProfileGroup,
       "alaDaUNPIpNetRuleGroup": alaDaUNPIpNetRuleGroup,
       "alaDaUNPMacRuleGroup": alaDaUNPMacRuleGroup,
       "alaDaUNPMacRangeGroup": alaDaUNPMacRangeGroup,
       "alaDaUNPVlanTagGroup": alaDaUNPVlanTagGroup,
       "alaDaMacUserGroup": alaDaMacUserGroup,
       "alaDaUNPPortGroup": alaDaUNPPortGroup,
       "alaDaUNPGlobalGroup": alaDaUNPGlobalGroup,
       "alaDaNotificationObjectGroup": alaDaNotificationObjectGroup,
       "alaDaNotificationsGroup": alaDaNotificationsGroup,
       "alaDaMacVlanUserGroup": alaDaMacVlanUserGroup,
       "alaDaUnpCustomerDomainGroup": alaDaUnpCustomerDomainGroup,
       "alaDaSpbProfileGroup": alaDaSpbProfileGroup,
       "alaDaUNPCustDomainEvbGpIdRuleGroup": alaDaUNPCustDomainEvbGpIdRuleGroup,
       "alaDaUNPCustDomainVlanTagRuleGroup": alaDaUNPCustDomainVlanTagRuleGroup,
       "alaDaUNPCustDomainIpNetRuleGroup": alaDaUNPCustDomainIpNetRuleGroup,
       "alaDaUNPCustDomainMacRuleGroup": alaDaUNPCustDomainMacRuleGroup,
       "alaDaUNPCustDomainMacRangeGroup": alaDaUNPCustDomainMacRangeGroup,
       "alaDaUNPGroupObjects": alaDaUNPGroupObjects,
       "alaDaSaaProfileGroup": alaDaSaaProfileGroup,
       "alaDaCPortalGroup": alaDaCPortalGroup,
       "alaDaHICGroup": alaDaHICGroup,
       "alaDaUNPEdgeTemplateGroup": alaDaUNPEdgeTemplateGroup,
       "alaDaUNPEdgeProfileGroup": alaDaUNPEdgeProfileGroup,
       "alaDaUNPClassificationRuleGroup": alaDaUNPClassificationRuleGroup,
       "alaDaUNPGroupIdEdgeClassifyGroup": alaDaUNPGroupIdEdgeClassifyGroup,
       "alaDaUNPMacOuiGroup": alaDaUNPMacOuiGroup,
       "alaDaUNPEndPointGroup": alaDaUNPEndPointGroup,
       "alaDaUNPAuthRuleGroup": alaDaUNPAuthRuleGroup,
       "alaDaUNPRuleGroup": alaDaUNPRuleGroup,
       "alaDaUNPMacPortClassifyGroup": alaDaUNPMacPortClassifyGroup,
       "alaDaUNPIpPortClassifyGroup": alaDaUNPIpPortClassifyGroup,
       "alaDaUNPMacIpClassifyGroup": alaDaUNPMacIpClassifyGroup,
       "alaDaUNPMacClassifyGroup": alaDaUNPMacClassifyGroup,
       "alaDaUNPIpAddressGroup": alaDaUNPIpAddressGroup,
       "alaDaUNPMacIpGroup": alaDaUNPMacIpGroup,
       "alaDaUNPUserRoleGroup": alaDaUNPUserRoleGroup,
       "alaDaUNPRestrictedRoleGroup": alaDaUNPRestrictedRoleGroup,
       "alaDaUNPVlanMappingGroup": alaDaUNPVlanMappingGroup,
       "alaDaUNPGroup": alaDaUNPGroup,
       "alaDaUNPEdgeFlushGroup": alaDaUNPEdgeFlushGroup,
       "alaDaUNPMacAddrsRuleGroup": alaDaUNPMacAddrsRuleGroup,
       "alaDaUNPMacRangesGroup": alaDaUNPMacRangesGroup,
       "alaDaUNPIpMaskGroup": alaDaUNPIpMaskGroup,
       "alaDaQMRGroup": alaDaQMRGroup,
       "alaDaUNPValidityPeriodGroup": alaDaUNPValidityPeriodGroup,
       "alaDaUNPLocationPolicyGroup": alaDaUNPLocationPolicyGroup,
       "alaDaUNPRedirectAllowedServerGroup": alaDaUNPRedirectAllowedServerGroup,
       "alaDaMacVlanUserExtGroup": alaDaMacVlanUserExtGroup,
       "alaDaUNPVxlanProfileGroup": alaDaUNPVxlanProfileGroup,
       "alaDaUNPVxlanFlushGroup": alaDaUNPVxlanFlushGroup,
       "alaDaUNPVxlanFarEndIPListGroup": alaDaUNPVxlanFarEndIPListGroup,
       "alaDaUNPVxlanFarEndIPAddressListGroup": alaDaUNPVxlanFarEndIPAddressListGroup,
       "alaDaUNPSpbFlushGroup": alaDaUNPSpbFlushGroup,
       "alaDaKerberosGroup": alaDaKerberosGroup,
       "alaDaUNPVlanGroup": alaDaUNPVlanGroup,
       "alaDaUNPPortVlanGroup": alaDaUNPPortVlanGroup,
       "alaDaUNPETmplVlanGroup": alaDaUNPETmplVlanGroup,
       "alaDaUNPUserFlushGroup": alaDaUNPUserFlushGroup,
       "alaDaUNPCustDomainRuleGroup": alaDaUNPCustDomainRuleGroup,
       "alaDaUNPPortTemplateGroup": alaDaUNPPortTemplateGroup,
       "alaDaUNPProfileGroup": alaDaUNPProfileGroup,
       "alaDaUNPProfileMapVlanGroup": alaDaUNPProfileMapVlanGroup,
       "alaDaUNPProfileMapSpbGroup": alaDaUNPProfileMapSpbGroup,
       "alaDaUNPProfileMapVxlanGroup": alaDaUNPProfileMapVxlanGroup,
       "alaDaUNPProfileMapStaticGroup": alaDaUNPProfileMapStaticGroup,
       "alaDaUNPCustDomainMacIpRuleGroup": alaDaUNPCustDomainMacIpRuleGroup,
       "alaDaUNPPortTemplateVlanGroup": alaDaUNPPortTemplateVlanGroup,
       "alaDaUNPWlanConfigurationGroup": alaDaUNPWlanConfigurationGroup,
       "alaDaUNPProfileMapL2GreGroup": alaDaUNPProfileMapL2GreGroup,
       "alaDaUNPL2GreFarEndIPListGroup": alaDaUNPL2GreFarEndIPListGroup,
       "alaDaUNPL2GreFarEndIPAddressListGroup": alaDaUNPL2GreFarEndIPAddressListGroup,
       "alaDaUNPNetworkGroupNameGroup": alaDaUNPNetworkGroupNameGroup,
       "alaDaUNPRouterAuthUserGroup": alaDaUNPRouterAuthUserGroup,
       "alaDaUNPRouterAuthenticationConfigGroup": alaDaUNPRouterAuthenticationConfigGroup,
       "alaDaUNPRouterAuthenticationFlushGroup": alaDaUNPRouterAuthenticationFlushGroup,
       "alaDaUNPPortProfileGroup": alaDaUNPPortProfileGroup,
       "alaDaUNPPortTemplateProfileGroup": alaDaUNPPortTemplateProfileGroup,
       "alaDaUNPRouterAuthenticationUserGroup": alaDaUNPRouterAuthenticationUserGroup,
       "alaDaUNPRedirectAllowedWebServerGroup": alaDaUNPRedirectAllowedWebServerGroup,
       "alaDaUNPFQDNResolvedIPGroup": alaDaUNPFQDNResolvedIPGroup,
       "alaDaUNPProfileMapVplsGroup": alaDaUNPProfileMapVplsGroup,
       "alaDaUNPVplsFarEndIPListGroup": alaDaUNPVplsFarEndIPListGroup,
       "alaDaUNPVplsFarEndIPAddressListGroup": alaDaUNPVplsFarEndIPAddressListGroup,
       "alaDaUNPProfileTrustTaggedVlanGroup": alaDaUNPProfileTrustTaggedVlanGroup,
       "alaDaUNPApModeMacOuiGroup": alaDaUNPApModeMacOuiGroup,
       "alaIND1DaMIBCompliances": alaIND1DaMIBCompliances}
)
