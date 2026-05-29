# SNMP MIB module (AUDIOCODES-TYPES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\audiocodes\AUDIOCODES-TYPES-MIB

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcRegistrations_ObjectIdentity = ObjectIdentity
acRegistrations = _AcRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 7)
)
_AcGeneric_ObjectIdentity = ObjectIdentity
acGeneric = _AcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8)
)
_AcKnownTypes_ObjectIdentity = ObjectIdentity
acKnownTypes = _AcKnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1)
)
_AcKnownProducts_ObjectIdentity = ObjectIdentity
acKnownProducts = _AcKnownProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1)
)
_AcProductUnknown_ObjectIdentity = ObjectIdentity
acProductUnknown = _AcProductUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 0)
)
_AcProductTrunkPack08_ObjectIdentity = ObjectIdentity
acProductTrunkPack08 = _AcProductTrunkPack08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 1)
)
_AcProductMediaPack108_ObjectIdentity = ObjectIdentity
acProductMediaPack108 = _AcProductMediaPack108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 2)
)
_AcProductMediaPack124_ObjectIdentity = ObjectIdentity
acProductMediaPack124 = _AcProductMediaPack124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 3)
)
_AcProductTrunkPack1600_ObjectIdentity = ObjectIdentity
acProductTrunkPack1600 = _AcProductTrunkPack1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 20)
)
_AcProductTPM1100_ObjectIdentity = ObjectIdentity
acProductTPM1100 = _AcProductTPM1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 22)
)
_AcProductTrunkPack260IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack260IpMedia = _AcProductTrunkPack260IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 23)
)
_AcProductTrunkPack1610_ObjectIdentity = ObjectIdentity
acProductTrunkPack1610 = _AcProductTrunkPack1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 24)
)
_AcProductMediaPack104_ObjectIdentity = ObjectIdentity
acProductMediaPack104 = _AcProductMediaPack104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 25)
)
_AcProductMediaPack102_ObjectIdentity = ObjectIdentity
acProductMediaPack102 = _AcProductMediaPack102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 26)
)
_AcProductTrunkPack1610SB_ObjectIdentity = ObjectIdentity
acProductTrunkPack1610SB = _AcProductTrunkPack1610SB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 29)
)
_AcProductTrunkPack1610IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack1610IpMedia = _AcProductTrunkPack1610IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 30)
)
_AcProductTrunkPackMEDIANT2000_ObjectIdentity = ObjectIdentity
acProductTrunkPackMEDIANT2000 = _AcProductTrunkPackMEDIANT2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 31)
)
_AcProductTrunkPackSTRETTO2000_ObjectIdentity = ObjectIdentity
acProductTrunkPackSTRETTO2000 = _AcProductTrunkPackSTRETTO2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 32)
)
_AcProductTrunkPackIPMServer2000_ObjectIdentity = ObjectIdentity
acProductTrunkPackIPMServer2000 = _AcProductTrunkPackIPMServer2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 33)
)
_AcProductTrunkPack2810_ObjectIdentity = ObjectIdentity
acProductTrunkPack2810 = _AcProductTrunkPack2810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 34)
)
_AcProductTrunkPack260UNIpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack260UNIpMedia = _AcProductTrunkPack260UNIpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 35)
)
_AcProductTrunkPack260IpMedia30Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260IpMedia30Ch = _AcProductTrunkPack260IpMedia30Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 36)
)
_AcProductTrunkPack260IpMedia60Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260IpMedia60Ch = _AcProductTrunkPack260IpMedia60Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 37)
)
_AcProductTrunkPack260IpMedia120Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260IpMedia120Ch = _AcProductTrunkPack260IpMedia120Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 38)
)
_AcProductTrunkPack260RTIpMedia30Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260RTIpMedia30Ch = _AcProductTrunkPack260RTIpMedia30Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 39)
)
_AcProductTrunkPack260RTIpMedia60Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260RTIpMedia60Ch = _AcProductTrunkPack260RTIpMedia60Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 40)
)
_AcProductTrunkPack260RTIpMedia120Ch_ObjectIdentity = ObjectIdentity
acProductTrunkPack260RTIpMedia120Ch = _AcProductTrunkPack260RTIpMedia120Ch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 41)
)
_AcProductTrunkPack260_ObjectIdentity = ObjectIdentity
acProductTrunkPack260 = _AcProductTrunkPack260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 42)
)
_AcProductTrunkPack260UN_ObjectIdentity = ObjectIdentity
acProductTrunkPack260UN = _AcProductTrunkPack260UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 43)
)
_AcProductTPM1100PCM_ObjectIdentity = ObjectIdentity
acProductTPM1100PCM = _AcProductTPM1100PCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 44)
)
_AcProductTrunkPack6310_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310 = _AcProductTrunkPack6310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 45)
)
_AcProductTPM6300_ObjectIdentity = ObjectIdentity
acProductTPM6300 = _AcProductTPM6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 46)
)
_AcProductMediant1000_ObjectIdentity = ObjectIdentity
acProductMediant1000 = _AcProductMediant1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 47)
)
_AcProductIPMedia3000_ObjectIdentity = ObjectIdentity
acProductIPMedia3000 = _AcProductIPMedia3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 48)
)
_AcProductMediant3000_ObjectIdentity = ObjectIdentity
acProductMediant3000 = _AcProductMediant3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 49)
)
_AcProductStretto3000_ObjectIdentity = ObjectIdentity
acProductStretto3000 = _AcProductStretto3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 50)
)
_AcProductTrunkPack6310IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310IpMedia = _AcProductTrunkPack6310IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 51)
)
_AcProductTrunkPack6310SB_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310SB = _AcProductTrunkPack6310SB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 52)
)
_AcProductATP1610_ObjectIdentity = ObjectIdentity
acProductATP1610 = _AcProductATP1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 53)
)
_AcProductATP260_ObjectIdentity = ObjectIdentity
acProductATP260 = _AcProductATP260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 54)
)
_AcProductATP260UN_ObjectIdentity = ObjectIdentity
acProductATP260UN = _AcProductATP260UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 55)
)
_AcProductMediaPack118_ObjectIdentity = ObjectIdentity
acProductMediaPack118 = _AcProductMediaPack118_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 56)
)
_AcProductMediaPack114_ObjectIdentity = ObjectIdentity
acProductMediaPack114 = _AcProductMediaPack114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 57)
)
_AcProductMediaPack112_ObjectIdentity = ObjectIdentity
acProductMediaPack112 = _AcProductMediaPack112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 58)
)
_AcProductTrunkPack6310T3_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310T3 = _AcProductTrunkPack6310T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 59)
)
_AcProductMediant3000T3_ObjectIdentity = ObjectIdentity
acProductMediant3000T3 = _AcProductMediant3000T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 60)
)
_AcProductIPmedia3000T3_ObjectIdentity = ObjectIdentity
acProductIPmedia3000T3 = _AcProductIPmedia3000T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 61)
)
_AcProductTrunkPack6310T3IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack6310T3IpMedia = _AcProductTrunkPack6310T3IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 62)
)
_AcProductTrunkPack8410_ObjectIdentity = ObjectIdentity
acProductTrunkPack8410 = _AcProductTrunkPack8410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 63)
)
_AcProductTrunkPack8410IpMedia_ObjectIdentity = ObjectIdentity
acProductTrunkPack8410IpMedia = _AcProductTrunkPack8410IpMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 64)
)
_AcProductMediant600_ObjectIdentity = ObjectIdentity
acProductMediant600 = _AcProductMediant600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 65)
)
_AcProductTrunkPack12610_ObjectIdentity = ObjectIdentity
acProductTrunkPack12610 = _AcProductTrunkPack12610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 66)
)
_AcProductMediant1000MSBR_ObjectIdentity = ObjectIdentity
acProductMediant1000MSBR = _AcProductMediant1000MSBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 67)
)
_AcProductMediant600MSBR_ObjectIdentity = ObjectIdentity
acProductMediant600MSBR = _AcProductMediant600MSBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 68)
)
_AcProductMediant800MSBR_ObjectIdentity = ObjectIdentity
acProductMediant800MSBR = _AcProductMediant800MSBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 69)
)
_AcProductM4000_ObjectIdentity = ObjectIdentity
acProductM4000 = _AcProductM4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 70)
)
_AcProductMediant1000ESBC_ObjectIdentity = ObjectIdentity
acProductMediant1000ESBC = _AcProductMediant1000ESBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 71)
)
_AcProductMediant800ESBC_ObjectIdentity = ObjectIdentity
acProductMediant800ESBC = _AcProductMediant800ESBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 72)
)
_AcProductHosted_ObjectIdentity = ObjectIdentity
acProductHosted = _AcProductHosted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 73)
)
_AcProductMediant850MSBR_ObjectIdentity = ObjectIdentity
acProductMediant850MSBR = _AcProductMediant850MSBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 74)
)
_AcProductMediant850ESBC_ObjectIdentity = ObjectIdentity
acProductMediant850ESBC = _AcProductMediant850ESBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 75)
)
_AcProductMediant500MSBR_ObjectIdentity = ObjectIdentity
acProductMediant500MSBR = _AcProductMediant500MSBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 76)
)
_AcProductMediant500ESBC_ObjectIdentity = ObjectIdentity
acProductMediant500ESBC = _AcProductMediant500ESBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 77)
)
_AcProductM2600_ObjectIdentity = ObjectIdentity
acProductM2600 = _AcProductM2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 78)
)
_AcProductMediantVeSBC_ObjectIdentity = ObjectIdentity
acProductMediantVeSBC = _AcProductMediantVeSBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 79)
)
_AcProductMediantVeHSBC_ObjectIdentity = ObjectIdentity
acProductMediantVeHSBC = _AcProductMediantVeHSBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 80)
)
_AcProductMediantSeSBC_ObjectIdentity = ObjectIdentity
acProductMediantSeSBC = _AcProductMediantSeSBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 81)
)
_AcProductMediantSeHSBC_ObjectIdentity = ObjectIdentity
acProductMediantSeHSBC = _AcProductMediantSeHSBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 82)
)
_AcProductMediant6000SBC_ObjectIdentity = ObjectIdentity
acProductMediant6000SBC = _AcProductMediant6000SBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 83)
)
_AcProductMediant500LMSBR_ObjectIdentity = ObjectIdentity
acProductMediant500LMSBR = _AcProductMediant500LMSBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 84)
)
_AcProductMediant500LESBC_ObjectIdentity = ObjectIdentity
acProductMediant500LESBC = _AcProductMediant500LESBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 85)
)
_AcProductMediantPack1288_ObjectIdentity = ObjectIdentity
acProductMediantPack1288 = _AcProductMediantPack1288_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 86)
)
_AcProductMediant500LI_ObjectIdentity = ObjectIdentity
acProductMediant500LI = _AcProductMediant500LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 89)
)
_AcProductMediant3100_ObjectIdentity = ObjectIdentity
acProductMediant3100 = _AcProductMediant3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 90)
)
_AcProductMediaPack202B_ObjectIdentity = ObjectIdentity
acProductMediaPack202B = _AcProductMediaPack202B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 200)
)
_AcProductMediaPack202D_ObjectIdentity = ObjectIdentity
acProductMediaPack202D = _AcProductMediaPack202D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 201)
)
_AcProductMediaPack204B_ObjectIdentity = ObjectIdentity
acProductMediaPack204B = _AcProductMediaPack204B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 202)
)
_AcProductMediaPack204D_ObjectIdentity = ObjectIdentity
acProductMediaPack204D = _AcProductMediaPack204D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 203)
)
_AcProductMediaPack202R_ObjectIdentity = ObjectIdentity
acProductMediaPack202R = _AcProductMediaPack202R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 204)
)
_AcProductMediaPack204R_ObjectIdentity = ObjectIdentity
acProductMediaPack204R = _AcProductMediaPack204R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 1, 205)
)
_AcKnownPhysicalTypes_ObjectIdentity = ObjectIdentity
acKnownPhysicalTypes = _AcKnownPhysicalTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2)
)
_AcKnownChassis_ObjectIdentity = ObjectIdentity
acKnownChassis = _AcKnownChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2)
)
_AcM1000Chassis_ObjectIdentity = ObjectIdentity
acM1000Chassis = _AcM1000Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 1)
)
_AcM2000Chassis_ObjectIdentity = ObjectIdentity
acM2000Chassis = _AcM2000Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 2)
)
_AcM3000Chassis_ObjectIdentity = ObjectIdentity
acM3000Chassis = _AcM3000Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 3)
)
_AcM600Chassis_ObjectIdentity = ObjectIdentity
acM600Chassis = _AcM600Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 4)
)
_AcM800Chassis_ObjectIdentity = ObjectIdentity
acM800Chassis = _AcM800Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 5)
)
_AcMP118Chassis_ObjectIdentity = ObjectIdentity
acMP118Chassis = _AcMP118Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 6)
)
_AcM4000Chassis_ObjectIdentity = ObjectIdentity
acM4000Chassis = _AcM4000Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 7)
)
_AcM500Chassis_ObjectIdentity = ObjectIdentity
acM500Chassis = _AcM500Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 8)
)
_AcM850Chassis_ObjectIdentity = ObjectIdentity
acM850Chassis = _AcM850Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 9)
)
_AcM2600Chassis_ObjectIdentity = ObjectIdentity
acM2600Chassis = _AcM2600Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 10)
)
_AcM500LChassis_ObjectIdentity = ObjectIdentity
acM500LChassis = _AcM500LChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 11)
)
_AcMP1288Chassis_ObjectIdentity = ObjectIdentity
acMP1288Chassis = _AcMP1288Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 12)
)
_AcM3100Chassis_ObjectIdentity = ObjectIdentity
acM3100Chassis = _AcM3100Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 2, 13)
)
_AcKnownSlots_ObjectIdentity = ObjectIdentity
acKnownSlots = _AcKnownSlots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 3)
)
_AcKnownModules_ObjectIdentity = ObjectIdentity
acKnownModules = _AcKnownModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 4)
)
_AcModuleUnknown_ObjectIdentity = ObjectIdentity
acModuleUnknown = _AcModuleUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 4, 1)
)
_AcKnownPorts_ObjectIdentity = ObjectIdentity
acKnownPorts = _AcKnownPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5)
)
_AcPortUnknown_ObjectIdentity = ObjectIdentity
acPortUnknown = _AcPortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 1)
)
_AcPortAnalog_ObjectIdentity = ObjectIdentity
acPortAnalog = _AcPortAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 2)
)
_AcPortFxsAnalog_ObjectIdentity = ObjectIdentity
acPortFxsAnalog = _AcPortFxsAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 2, 1)
)
_AcPortFxoAnalog_ObjectIdentity = ObjectIdentity
acPortFxoAnalog = _AcPortFxoAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 2, 2)
)
_AcPortEMAnalog_ObjectIdentity = ObjectIdentity
acPortEMAnalog = _AcPortEMAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 2, 3)
)
_AcPortDigital_ObjectIdentity = ObjectIdentity
acPortDigital = _AcPortDigital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3)
)
_AcPortE1T1Quad_ObjectIdentity = ObjectIdentity
acPortE1T1Quad = _AcPortE1T1Quad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 1)
)
_AcPortE1T1Falc56_ObjectIdentity = ObjectIdentity
acPortE1T1Falc56 = _AcPortE1T1Falc56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 2)
)
_AcPortEthernet_ObjectIdentity = ObjectIdentity
acPortEthernet = _AcPortEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 3)
)
_AcPortPstnOc3Stm1_ObjectIdentity = ObjectIdentity
acPortPstnOc3Stm1 = _AcPortPstnOc3Stm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 4)
)
_AcPortAtmStm1_ObjectIdentity = ObjectIdentity
acPortAtmStm1 = _AcPortAtmStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 5)
)
_AcPortGBEthernet_ObjectIdentity = ObjectIdentity
acPortGBEthernet = _AcPortGBEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 6)
)
_AcPortDs3_ObjectIdentity = ObjectIdentity
acPortDs3 = _AcPortDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 7)
)
_AcPortSonetSdh_ObjectIdentity = ObjectIdentity
acPortSonetSdh = _AcPortSonetSdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 8)
)
_AcPortBRI_ObjectIdentity = ObjectIdentity
acPortBRI = _AcPortBRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 9)
)
_AcPortE1T1OctalFalc_ObjectIdentity = ObjectIdentity
acPortE1T1OctalFalc = _AcPortE1T1OctalFalc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 10)
)
_AcPortWAN_ObjectIdentity = ObjectIdentity
acPortWAN = _AcPortWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 11)
)
_AcPortWireless_ObjectIdentity = ObjectIdentity
acPortWireless = _AcPortWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 12)
)
_AcPortT1WAN_ObjectIdentity = ObjectIdentity
acPortT1WAN = _AcPortT1WAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 13)
)
_AcPortSHDSL_ObjectIdentity = ObjectIdentity
acPortSHDSL = _AcPortSHDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 14)
)
_AcPortADSLVDSL_ObjectIdentity = ObjectIdentity
acPortADSLVDSL = _AcPortADSLVDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 15)
)
_AcPortGPON_ObjectIdentity = ObjectIdentity
acPortGPON = _AcPortGPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 16)
)
_AcPortGESFP_ObjectIdentity = ObjectIdentity
acPortGESFP = _AcPortGESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 3, 17)
)
_AcPortNetwork_ObjectIdentity = ObjectIdentity
acPortNetwork = _AcPortNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 5, 4)
)
_AcKnownFans_ObjectIdentity = ObjectIdentity
acKnownFans = _AcKnownFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 6)
)
_AcFanUnknown_ObjectIdentity = ObjectIdentity
acFanUnknown = _AcFanUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 6, 1)
)
_AcKnownSensors_ObjectIdentity = ObjectIdentity
acKnownSensors = _AcKnownSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 7)
)
_AcTemperatureSensor_ObjectIdentity = ObjectIdentity
acTemperatureSensor = _AcTemperatureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 7, 1)
)
_AcM1000KnownTypes_ObjectIdentity = ObjectIdentity
acM1000KnownTypes = _AcM1000KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20)
)
_AcM1000CpuSlot_ObjectIdentity = ObjectIdentity
acM1000CpuSlot = _AcM1000CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 1)
)
_AcM1000IfsSlot_ObjectIdentity = ObjectIdentity
acM1000IfsSlot = _AcM1000IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 2)
)
_AcM1000PowerSupplySlot_ObjectIdentity = ObjectIdentity
acM1000PowerSupplySlot = _AcM1000PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 3)
)
_AcM1000FanSlot_ObjectIdentity = ObjectIdentity
acM1000FanSlot = _AcM1000FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 4)
)
_AcM600CpuSlot_ObjectIdentity = ObjectIdentity
acM600CpuSlot = _AcM600CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 5)
)
_AcM600IfsSlot_ObjectIdentity = ObjectIdentity
acM600IfsSlot = _AcM600IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 6)
)
_AcM600PowerSupplySlot_ObjectIdentity = ObjectIdentity
acM600PowerSupplySlot = _AcM600PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 7)
)
_AcM600FanSlot_ObjectIdentity = ObjectIdentity
acM600FanSlot = _AcM600FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 8)
)
_AcM1000CpuModule_ObjectIdentity = ObjectIdentity
acM1000CpuModule = _AcM1000CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 11)
)
_AcM1000AnalogIfsModule_ObjectIdentity = ObjectIdentity
acM1000AnalogIfsModule = _AcM1000AnalogIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 12)
)
_AcM1000DigitalIfsModule_ObjectIdentity = ObjectIdentity
acM1000DigitalIfsModule = _AcM1000DigitalIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 13)
)
_AcM1000PowerSupplyModule_ObjectIdentity = ObjectIdentity
acM1000PowerSupplyModule = _AcM1000PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 14)
)
_AcM1000FanModule_ObjectIdentity = ObjectIdentity
acM1000FanModule = _AcM1000FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 15)
)
_AcM1000BRIModule_ObjectIdentity = ObjectIdentity
acM1000BRIModule = _AcM1000BRIModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 16)
)
_AcM1000IPMediaModule_ObjectIdentity = ObjectIdentity
acM1000IPMediaModule = _AcM1000IPMediaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 17)
)
_AcM600CpuModule_ObjectIdentity = ObjectIdentity
acM600CpuModule = _AcM600CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 18)
)
_AcM600AnalogIfsModule_ObjectIdentity = ObjectIdentity
acM600AnalogIfsModule = _AcM600AnalogIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 19)
)
_AcM600DigitalIfsModule_ObjectIdentity = ObjectIdentity
acM600DigitalIfsModule = _AcM600DigitalIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 20)
)
_AcM600PowerSupplyModule_ObjectIdentity = ObjectIdentity
acM600PowerSupplyModule = _AcM600PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 21)
)
_AcM600FanModule_ObjectIdentity = ObjectIdentity
acM600FanModule = _AcM600FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 22)
)
_AcM600BRIModule_ObjectIdentity = ObjectIdentity
acM600BRIModule = _AcM600BRIModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 23)
)
_AcM600IPMediaModule_ObjectIdentity = ObjectIdentity
acM600IPMediaModule = _AcM600IPMediaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 24)
)
_AcM1000EthernetModule_ObjectIdentity = ObjectIdentity
acM1000EthernetModule = _AcM1000EthernetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 25)
)
_AcM600EthernetModule_ObjectIdentity = ObjectIdentity
acM600EthernetModule = _AcM600EthernetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 20, 26)
)
_AcM2000KnownTypes_ObjectIdentity = ObjectIdentity
acM2000KnownTypes = _AcM2000KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 21)
)
_AcM2000CpuSlot_ObjectIdentity = ObjectIdentity
acM2000CpuSlot = _AcM2000CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 21, 1)
)
_AcM2000Module1610_ObjectIdentity = ObjectIdentity
acM2000Module1610 = _AcM2000Module1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 21, 11)
)
_AcM3000KnownTypes_ObjectIdentity = ObjectIdentity
acM3000KnownTypes = _AcM3000KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22)
)
_AcM3000Slot_ObjectIdentity = ObjectIdentity
acM3000Slot = _AcM3000Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 1)
)
_AcM3000PowerSupplySlot_ObjectIdentity = ObjectIdentity
acM3000PowerSupplySlot = _AcM3000PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 2)
)
_AcM3000FanSlot_ObjectIdentity = ObjectIdentity
acM3000FanSlot = _AcM3000FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 3)
)
_AcM3000Module6310_ObjectIdentity = ObjectIdentity
acM3000Module6310 = _AcM3000Module6310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 11)
)
_AcM3000ModuleSat_ObjectIdentity = ObjectIdentity
acM3000ModuleSat = _AcM3000ModuleSat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 12)
)
_AcM3000PowerSupplyModule_ObjectIdentity = ObjectIdentity
acM3000PowerSupplyModule = _AcM3000PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 13)
)
_AcM3000FanModule_ObjectIdentity = ObjectIdentity
acM3000FanModule = _AcM3000FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 14)
)
_AcM3000Module8410_ObjectIdentity = ObjectIdentity
acM3000Module8410 = _AcM3000Module8410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 22, 17)
)
_AcM800KnownTypes_ObjectIdentity = ObjectIdentity
acM800KnownTypes = _AcM800KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23)
)
_AcM800CpuSlot_ObjectIdentity = ObjectIdentity
acM800CpuSlot = _AcM800CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 1)
)
_AcM800IfsSlot_ObjectIdentity = ObjectIdentity
acM800IfsSlot = _AcM800IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 2)
)
_AcM800CpuModule_ObjectIdentity = ObjectIdentity
acM800CpuModule = _AcM800CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 3)
)
_AcM800AnalogIfsModule_ObjectIdentity = ObjectIdentity
acM800AnalogIfsModule = _AcM800AnalogIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 4)
)
_AcM800DigitalIfsModule_ObjectIdentity = ObjectIdentity
acM800DigitalIfsModule = _AcM800DigitalIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 5)
)
_AcM800BRIModule_ObjectIdentity = ObjectIdentity
acM800BRIModule = _AcM800BRIModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 6)
)
_AcM800WANModule_ObjectIdentity = ObjectIdentity
acM800WANModule = _AcM800WANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 7)
)
_AcM800WiFiModule_ObjectIdentity = ObjectIdentity
acM800WiFiModule = _AcM800WiFiModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 8)
)
_AcM800IPMediaModule_ObjectIdentity = ObjectIdentity
acM800IPMediaModule = _AcM800IPMediaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 9)
)
_AcM800EthernetModule_ObjectIdentity = ObjectIdentity
acM800EthernetModule = _AcM800EthernetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 23, 10)
)
_AcMP118KnownTypes_ObjectIdentity = ObjectIdentity
acMP118KnownTypes = _AcMP118KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 24)
)
_AcMP118Slot_ObjectIdentity = ObjectIdentity
acMP118Slot = _AcMP118Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 24, 1)
)
_AcMP118Module_ObjectIdentity = ObjectIdentity
acMP118Module = _AcMP118Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 24, 2)
)
_AcM4000KnownTypes_ObjectIdentity = ObjectIdentity
acM4000KnownTypes = _AcM4000KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 25)
)
_AcM4000CpuSlot_ObjectIdentity = ObjectIdentity
acM4000CpuSlot = _AcM4000CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 25, 1)
)
_AcM4000PowerSupplySlot_ObjectIdentity = ObjectIdentity
acM4000PowerSupplySlot = _AcM4000PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 25, 2)
)
_AcM4000FanSlot_ObjectIdentity = ObjectIdentity
acM4000FanSlot = _AcM4000FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 25, 3)
)
_AcM4000CpuModule_ObjectIdentity = ObjectIdentity
acM4000CpuModule = _AcM4000CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 25, 4)
)
_AcM4000PowerSupplyModule_ObjectIdentity = ObjectIdentity
acM4000PowerSupplyModule = _AcM4000PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 25, 5)
)
_AcM4000FanModule_ObjectIdentity = ObjectIdentity
acM4000FanModule = _AcM4000FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 25, 6)
)
_AcM4000MPModule_ObjectIdentity = ObjectIdentity
acM4000MPModule = _AcM4000MPModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 25, 7)
)
_AcM500KnownTypes_ObjectIdentity = ObjectIdentity
acM500KnownTypes = _AcM500KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26)
)
_AcM500CpuSlot_ObjectIdentity = ObjectIdentity
acM500CpuSlot = _AcM500CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 1)
)
_AcM500IfsSlot_ObjectIdentity = ObjectIdentity
acM500IfsSlot = _AcM500IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 2)
)
_AcM500CpuModule_ObjectIdentity = ObjectIdentity
acM500CpuModule = _AcM500CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 3)
)
_AcM500AnalogIfsModule_ObjectIdentity = ObjectIdentity
acM500AnalogIfsModule = _AcM500AnalogIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 4)
)
_AcM500DigitalIfsModule_ObjectIdentity = ObjectIdentity
acM500DigitalIfsModule = _AcM500DigitalIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 5)
)
_AcM500BRIModule_ObjectIdentity = ObjectIdentity
acM500BRIModule = _AcM500BRIModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 6)
)
_AcM500WANModule_ObjectIdentity = ObjectIdentity
acM500WANModule = _AcM500WANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 7)
)
_AcM500WiFiModule_ObjectIdentity = ObjectIdentity
acM500WiFiModule = _AcM500WiFiModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 8)
)
_AcM500IPMediaModule_ObjectIdentity = ObjectIdentity
acM500IPMediaModule = _AcM500IPMediaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 9)
)
_AcM500EthernetModule_ObjectIdentity = ObjectIdentity
acM500EthernetModule = _AcM500EthernetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 26, 10)
)
_AcM850KnownTypes_ObjectIdentity = ObjectIdentity
acM850KnownTypes = _AcM850KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27)
)
_AcM850CpuSlot_ObjectIdentity = ObjectIdentity
acM850CpuSlot = _AcM850CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 1)
)
_AcM850IfsSlot_ObjectIdentity = ObjectIdentity
acM850IfsSlot = _AcM850IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 2)
)
_AcM850CpuModule_ObjectIdentity = ObjectIdentity
acM850CpuModule = _AcM850CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 3)
)
_AcM850AnalogIfsModule_ObjectIdentity = ObjectIdentity
acM850AnalogIfsModule = _AcM850AnalogIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 4)
)
_AcM850DigitalIfsModule_ObjectIdentity = ObjectIdentity
acM850DigitalIfsModule = _AcM850DigitalIfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 5)
)
_AcM850BRIModule_ObjectIdentity = ObjectIdentity
acM850BRIModule = _AcM850BRIModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 6)
)
_AcM850WANModule_ObjectIdentity = ObjectIdentity
acM850WANModule = _AcM850WANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 7)
)
_AcM850WiFiModule_ObjectIdentity = ObjectIdentity
acM850WiFiModule = _AcM850WiFiModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 8)
)
_AcM850IPMediaModule_ObjectIdentity = ObjectIdentity
acM850IPMediaModule = _AcM850IPMediaModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 9)
)
_AcM850EthernetModule_ObjectIdentity = ObjectIdentity
acM850EthernetModule = _AcM850EthernetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 27, 10)
)
_AcM2600KnownTypes_ObjectIdentity = ObjectIdentity
acM2600KnownTypes = _AcM2600KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 28)
)
_AcM2600CpuSlot_ObjectIdentity = ObjectIdentity
acM2600CpuSlot = _AcM2600CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 28, 1)
)
_AcM2600PowerSupplySlot_ObjectIdentity = ObjectIdentity
acM2600PowerSupplySlot = _AcM2600PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 28, 2)
)
_AcM2600FanSlot_ObjectIdentity = ObjectIdentity
acM2600FanSlot = _AcM2600FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 28, 3)
)
_AcM2600CpuModule_ObjectIdentity = ObjectIdentity
acM2600CpuModule = _AcM2600CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 28, 4)
)
_AcM2600PowerSupplyModule_ObjectIdentity = ObjectIdentity
acM2600PowerSupplyModule = _AcM2600PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 28, 5)
)
_AcM2600FanModule_ObjectIdentity = ObjectIdentity
acM2600FanModule = _AcM2600FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 28, 6)
)
_AcM2600MPModule_ObjectIdentity = ObjectIdentity
acM2600MPModule = _AcM2600MPModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 28, 7)
)
_AcMP1288KnownTypes_ObjectIdentity = ObjectIdentity
acMP1288KnownTypes = _AcMP1288KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 29)
)
_AcMP1288CpuSlot_ObjectIdentity = ObjectIdentity
acMP1288CpuSlot = _AcMP1288CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 29, 1)
)
_AcMP1288PowerSupplySlot_ObjectIdentity = ObjectIdentity
acMP1288PowerSupplySlot = _AcMP1288PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 29, 2)
)
_AcMP1288FanSlot_ObjectIdentity = ObjectIdentity
acMP1288FanSlot = _AcMP1288FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 29, 3)
)
_AcMP1288IfsSlot_ObjectIdentity = ObjectIdentity
acMP1288IfsSlot = _AcMP1288IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 29, 4)
)
_AcMP1288CpuModule_ObjectIdentity = ObjectIdentity
acMP1288CpuModule = _AcMP1288CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 29, 5)
)
_AcMP1288AnalogModule_ObjectIdentity = ObjectIdentity
acMP1288AnalogModule = _AcMP1288AnalogModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 29, 6)
)
_AcMP1288PowerSupplyModule_ObjectIdentity = ObjectIdentity
acMP1288PowerSupplyModule = _AcMP1288PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 29, 7)
)
_AcMP1288FanModule_ObjectIdentity = ObjectIdentity
acMP1288FanModule = _AcMP1288FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 29, 8)
)
_AcM3100KnownTypes_ObjectIdentity = ObjectIdentity
acM3100KnownTypes = _AcM3100KnownTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 30)
)
_AcM3100CpuSlot_ObjectIdentity = ObjectIdentity
acM3100CpuSlot = _AcM3100CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 30, 1)
)
_AcM3100PowerSupplySlot_ObjectIdentity = ObjectIdentity
acM3100PowerSupplySlot = _AcM3100PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 30, 2)
)
_AcM3100FanSlot_ObjectIdentity = ObjectIdentity
acM3100FanSlot = _AcM3100FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 30, 3)
)
_AcM3100IfsSlot_ObjectIdentity = ObjectIdentity
acM3100IfsSlot = _AcM3100IfsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 30, 4)
)
_AcM3100CpuModule_ObjectIdentity = ObjectIdentity
acM3100CpuModule = _AcM3100CpuModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 30, 5)
)
_AcM3100IfsModule_ObjectIdentity = ObjectIdentity
acM3100IfsModule = _AcM3100IfsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 30, 6)
)
_AcM3100PowerSupplyModule_ObjectIdentity = ObjectIdentity
acM3100PowerSupplyModule = _AcM3100PowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 30, 7)
)
_AcM3100FanModule_ObjectIdentity = ObjectIdentity
acM3100FanModule = _AcM3100FanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 2, 30, 8)
)
_AcKnownLogicalTypes_ObjectIdentity = ObjectIdentity
acKnownLogicalTypes = _AcKnownLogicalTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8, 1, 3)
)
_AcProducts_ObjectIdentity = ObjectIdentity
acProducts = _AcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9)
)
_AcBoardMibs_ObjectIdentity = ObjectIdentity
acBoardMibs = _AcBoardMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10)
)
_AcGateway_ObjectIdentity = ObjectIdentity
acGateway = _AcGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3)
)
_GwConfiguration_ObjectIdentity = ObjectIdentity
gwConfiguration = _GwConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1)
)
_AcPerformance_ObjectIdentity = ObjectIdentity
acPerformance = _AcPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10)
)
_AcExperimental_ObjectIdentity = ObjectIdentity
acExperimental = _AcExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AUDIOCODES-TYPES-MIB",
    **{"audioCodes": audioCodes,
       "acRegistrations": acRegistrations,
       "acGeneric": acGeneric,
       "acKnownTypes": acKnownTypes,
       "acKnownProducts": acKnownProducts,
       "acProductUnknown": acProductUnknown,
       "acProductTrunkPack08": acProductTrunkPack08,
       "acProductMediaPack108": acProductMediaPack108,
       "acProductMediaPack124": acProductMediaPack124,
       "acProductTrunkPack1600": acProductTrunkPack1600,
       "acProductTPM1100": acProductTPM1100,
       "acProductTrunkPack260IpMedia": acProductTrunkPack260IpMedia,
       "acProductTrunkPack1610": acProductTrunkPack1610,
       "acProductMediaPack104": acProductMediaPack104,
       "acProductMediaPack102": acProductMediaPack102,
       "acProductTrunkPack1610SB": acProductTrunkPack1610SB,
       "acProductTrunkPack1610IpMedia": acProductTrunkPack1610IpMedia,
       "acProductTrunkPackMEDIANT2000": acProductTrunkPackMEDIANT2000,
       "acProductTrunkPackSTRETTO2000": acProductTrunkPackSTRETTO2000,
       "acProductTrunkPackIPMServer2000": acProductTrunkPackIPMServer2000,
       "acProductTrunkPack2810": acProductTrunkPack2810,
       "acProductTrunkPack260UNIpMedia": acProductTrunkPack260UNIpMedia,
       "acProductTrunkPack260IpMedia30Ch": acProductTrunkPack260IpMedia30Ch,
       "acProductTrunkPack260IpMedia60Ch": acProductTrunkPack260IpMedia60Ch,
       "acProductTrunkPack260IpMedia120Ch": acProductTrunkPack260IpMedia120Ch,
       "acProductTrunkPack260RTIpMedia30Ch": acProductTrunkPack260RTIpMedia30Ch,
       "acProductTrunkPack260RTIpMedia60Ch": acProductTrunkPack260RTIpMedia60Ch,
       "acProductTrunkPack260RTIpMedia120Ch": acProductTrunkPack260RTIpMedia120Ch,
       "acProductTrunkPack260": acProductTrunkPack260,
       "acProductTrunkPack260UN": acProductTrunkPack260UN,
       "acProductTPM1100PCM": acProductTPM1100PCM,
       "acProductTrunkPack6310": acProductTrunkPack6310,
       "acProductTPM6300": acProductTPM6300,
       "acProductMediant1000": acProductMediant1000,
       "acProductIPMedia3000": acProductIPMedia3000,
       "acProductMediant3000": acProductMediant3000,
       "acProductStretto3000": acProductStretto3000,
       "acProductTrunkPack6310IpMedia": acProductTrunkPack6310IpMedia,
       "acProductTrunkPack6310SB": acProductTrunkPack6310SB,
       "acProductATP1610": acProductATP1610,
       "acProductATP260": acProductATP260,
       "acProductATP260UN": acProductATP260UN,
       "acProductMediaPack118": acProductMediaPack118,
       "acProductMediaPack114": acProductMediaPack114,
       "acProductMediaPack112": acProductMediaPack112,
       "acProductTrunkPack6310T3": acProductTrunkPack6310T3,
       "acProductMediant3000T3": acProductMediant3000T3,
       "acProductIPmedia3000T3": acProductIPmedia3000T3,
       "acProductTrunkPack6310T3IpMedia": acProductTrunkPack6310T3IpMedia,
       "acProductTrunkPack8410": acProductTrunkPack8410,
       "acProductTrunkPack8410IpMedia": acProductTrunkPack8410IpMedia,
       "acProductMediant600": acProductMediant600,
       "acProductTrunkPack12610": acProductTrunkPack12610,
       "acProductMediant1000MSBR": acProductMediant1000MSBR,
       "acProductMediant600MSBR": acProductMediant600MSBR,
       "acProductMediant800MSBR": acProductMediant800MSBR,
       "acProductM4000": acProductM4000,
       "acProductMediant1000ESBC": acProductMediant1000ESBC,
       "acProductMediant800ESBC": acProductMediant800ESBC,
       "acProductHosted": acProductHosted,
       "acProductMediant850MSBR": acProductMediant850MSBR,
       "acProductMediant850ESBC": acProductMediant850ESBC,
       "acProductMediant500MSBR": acProductMediant500MSBR,
       "acProductMediant500ESBC": acProductMediant500ESBC,
       "acProductM2600": acProductM2600,
       "acProductMediantVeSBC": acProductMediantVeSBC,
       "acProductMediantVeHSBC": acProductMediantVeHSBC,
       "acProductMediantSeSBC": acProductMediantSeSBC,
       "acProductMediantSeHSBC": acProductMediantSeHSBC,
       "acProductMediant6000SBC": acProductMediant6000SBC,
       "acProductMediant500LMSBR": acProductMediant500LMSBR,
       "acProductMediant500LESBC": acProductMediant500LESBC,
       "acProductMediantPack1288": acProductMediantPack1288,
       "acProductMediant500LI": acProductMediant500LI,
       "acProductMediant3100": acProductMediant3100,
       "acProductMediaPack202B": acProductMediaPack202B,
       "acProductMediaPack202D": acProductMediaPack202D,
       "acProductMediaPack204B": acProductMediaPack204B,
       "acProductMediaPack204D": acProductMediaPack204D,
       "acProductMediaPack202R": acProductMediaPack202R,
       "acProductMediaPack204R": acProductMediaPack204R,
       "acKnownPhysicalTypes": acKnownPhysicalTypes,
       "acKnownChassis": acKnownChassis,
       "acM1000Chassis": acM1000Chassis,
       "acM2000Chassis": acM2000Chassis,
       "acM3000Chassis": acM3000Chassis,
       "acM600Chassis": acM600Chassis,
       "acM800Chassis": acM800Chassis,
       "acMP118Chassis": acMP118Chassis,
       "acM4000Chassis": acM4000Chassis,
       "acM500Chassis": acM500Chassis,
       "acM850Chassis": acM850Chassis,
       "acM2600Chassis": acM2600Chassis,
       "acM500LChassis": acM500LChassis,
       "acMP1288Chassis": acMP1288Chassis,
       "acM3100Chassis": acM3100Chassis,
       "acKnownSlots": acKnownSlots,
       "acKnownModules": acKnownModules,
       "acModuleUnknown": acModuleUnknown,
       "acKnownPorts": acKnownPorts,
       "acPortUnknown": acPortUnknown,
       "acPortAnalog": acPortAnalog,
       "acPortFxsAnalog": acPortFxsAnalog,
       "acPortFxoAnalog": acPortFxoAnalog,
       "acPortEMAnalog": acPortEMAnalog,
       "acPortDigital": acPortDigital,
       "acPortE1T1Quad": acPortE1T1Quad,
       "acPortE1T1Falc56": acPortE1T1Falc56,
       "acPortEthernet": acPortEthernet,
       "acPortPstnOc3Stm1": acPortPstnOc3Stm1,
       "acPortAtmStm1": acPortAtmStm1,
       "acPortGBEthernet": acPortGBEthernet,
       "acPortDs3": acPortDs3,
       "acPortSonetSdh": acPortSonetSdh,
       "acPortBRI": acPortBRI,
       "acPortE1T1OctalFalc": acPortE1T1OctalFalc,
       "acPortWAN": acPortWAN,
       "acPortWireless": acPortWireless,
       "acPortT1WAN": acPortT1WAN,
       "acPortSHDSL": acPortSHDSL,
       "acPortADSLVDSL": acPortADSLVDSL,
       "acPortGPON": acPortGPON,
       "acPortGESFP": acPortGESFP,
       "acPortNetwork": acPortNetwork,
       "acKnownFans": acKnownFans,
       "acFanUnknown": acFanUnknown,
       "acKnownSensors": acKnownSensors,
       "acTemperatureSensor": acTemperatureSensor,
       "acM1000KnownTypes": acM1000KnownTypes,
       "acM1000CpuSlot": acM1000CpuSlot,
       "acM1000IfsSlot": acM1000IfsSlot,
       "acM1000PowerSupplySlot": acM1000PowerSupplySlot,
       "acM1000FanSlot": acM1000FanSlot,
       "acM600CpuSlot": acM600CpuSlot,
       "acM600IfsSlot": acM600IfsSlot,
       "acM600PowerSupplySlot": acM600PowerSupplySlot,
       "acM600FanSlot": acM600FanSlot,
       "acM1000CpuModule": acM1000CpuModule,
       "acM1000AnalogIfsModule": acM1000AnalogIfsModule,
       "acM1000DigitalIfsModule": acM1000DigitalIfsModule,
       "acM1000PowerSupplyModule": acM1000PowerSupplyModule,
       "acM1000FanModule": acM1000FanModule,
       "acM1000BRIModule": acM1000BRIModule,
       "acM1000IPMediaModule": acM1000IPMediaModule,
       "acM600CpuModule": acM600CpuModule,
       "acM600AnalogIfsModule": acM600AnalogIfsModule,
       "acM600DigitalIfsModule": acM600DigitalIfsModule,
       "acM600PowerSupplyModule": acM600PowerSupplyModule,
       "acM600FanModule": acM600FanModule,
       "acM600BRIModule": acM600BRIModule,
       "acM600IPMediaModule": acM600IPMediaModule,
       "acM1000EthernetModule": acM1000EthernetModule,
       "acM600EthernetModule": acM600EthernetModule,
       "acM2000KnownTypes": acM2000KnownTypes,
       "acM2000CpuSlot": acM2000CpuSlot,
       "acM2000Module1610": acM2000Module1610,
       "acM3000KnownTypes": acM3000KnownTypes,
       "acM3000Slot": acM3000Slot,
       "acM3000PowerSupplySlot": acM3000PowerSupplySlot,
       "acM3000FanSlot": acM3000FanSlot,
       "acM3000Module6310": acM3000Module6310,
       "acM3000ModuleSat": acM3000ModuleSat,
       "acM3000PowerSupplyModule": acM3000PowerSupplyModule,
       "acM3000FanModule": acM3000FanModule,
       "acM3000Module8410": acM3000Module8410,
       "acM800KnownTypes": acM800KnownTypes,
       "acM800CpuSlot": acM800CpuSlot,
       "acM800IfsSlot": acM800IfsSlot,
       "acM800CpuModule": acM800CpuModule,
       "acM800AnalogIfsModule": acM800AnalogIfsModule,
       "acM800DigitalIfsModule": acM800DigitalIfsModule,
       "acM800BRIModule": acM800BRIModule,
       "acM800WANModule": acM800WANModule,
       "acM800WiFiModule": acM800WiFiModule,
       "acM800IPMediaModule": acM800IPMediaModule,
       "acM800EthernetModule": acM800EthernetModule,
       "acMP118KnownTypes": acMP118KnownTypes,
       "acMP118Slot": acMP118Slot,
       "acMP118Module": acMP118Module,
       "acM4000KnownTypes": acM4000KnownTypes,
       "acM4000CpuSlot": acM4000CpuSlot,
       "acM4000PowerSupplySlot": acM4000PowerSupplySlot,
       "acM4000FanSlot": acM4000FanSlot,
       "acM4000CpuModule": acM4000CpuModule,
       "acM4000PowerSupplyModule": acM4000PowerSupplyModule,
       "acM4000FanModule": acM4000FanModule,
       "acM4000MPModule": acM4000MPModule,
       "acM500KnownTypes": acM500KnownTypes,
       "acM500CpuSlot": acM500CpuSlot,
       "acM500IfsSlot": acM500IfsSlot,
       "acM500CpuModule": acM500CpuModule,
       "acM500AnalogIfsModule": acM500AnalogIfsModule,
       "acM500DigitalIfsModule": acM500DigitalIfsModule,
       "acM500BRIModule": acM500BRIModule,
       "acM500WANModule": acM500WANModule,
       "acM500WiFiModule": acM500WiFiModule,
       "acM500IPMediaModule": acM500IPMediaModule,
       "acM500EthernetModule": acM500EthernetModule,
       "acM850KnownTypes": acM850KnownTypes,
       "acM850CpuSlot": acM850CpuSlot,
       "acM850IfsSlot": acM850IfsSlot,
       "acM850CpuModule": acM850CpuModule,
       "acM850AnalogIfsModule": acM850AnalogIfsModule,
       "acM850DigitalIfsModule": acM850DigitalIfsModule,
       "acM850BRIModule": acM850BRIModule,
       "acM850WANModule": acM850WANModule,
       "acM850WiFiModule": acM850WiFiModule,
       "acM850IPMediaModule": acM850IPMediaModule,
       "acM850EthernetModule": acM850EthernetModule,
       "acM2600KnownTypes": acM2600KnownTypes,
       "acM2600CpuSlot": acM2600CpuSlot,
       "acM2600PowerSupplySlot": acM2600PowerSupplySlot,
       "acM2600FanSlot": acM2600FanSlot,
       "acM2600CpuModule": acM2600CpuModule,
       "acM2600PowerSupplyModule": acM2600PowerSupplyModule,
       "acM2600FanModule": acM2600FanModule,
       "acM2600MPModule": acM2600MPModule,
       "acMP1288KnownTypes": acMP1288KnownTypes,
       "acMP1288CpuSlot": acMP1288CpuSlot,
       "acMP1288PowerSupplySlot": acMP1288PowerSupplySlot,
       "acMP1288FanSlot": acMP1288FanSlot,
       "acMP1288IfsSlot": acMP1288IfsSlot,
       "acMP1288CpuModule": acMP1288CpuModule,
       "acMP1288AnalogModule": acMP1288AnalogModule,
       "acMP1288PowerSupplyModule": acMP1288PowerSupplyModule,
       "acMP1288FanModule": acMP1288FanModule,
       "acM3100KnownTypes": acM3100KnownTypes,
       "acM3100CpuSlot": acM3100CpuSlot,
       "acM3100PowerSupplySlot": acM3100PowerSupplySlot,
       "acM3100FanSlot": acM3100FanSlot,
       "acM3100IfsSlot": acM3100IfsSlot,
       "acM3100CpuModule": acM3100CpuModule,
       "acM3100IfsModule": acM3100IfsModule,
       "acM3100PowerSupplyModule": acM3100PowerSupplyModule,
       "acM3100FanModule": acM3100FanModule,
       "acKnownLogicalTypes": acKnownLogicalTypes,
       "acProducts": acProducts,
       "acBoardMibs": acBoardMibs,
       "acGateway": acGateway,
       "gwConfiguration": gwConfiguration,
       "acPerformance": acPerformance,
       "acExperimental": acExperimental}
)
