# SNMP MIB module (HH3C-PRODUCT-ID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-PRODUCT-ID-MIB

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

(hh3cProductId,
 hpNetworking) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cProductId",
    "hpNetworking")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3c_s5500_28C_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_EI = _Hh3c_s5500_28C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1)
)
_Hh3c_s5500_52C_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_52C_EI = _Hh3c_s5500_52C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 2)
)
_Hh3c_s5500_28C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_PWR_EI = _Hh3c_s5500_28C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 3)
)
_Hh3c_s5500_52C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_52C_PWR_EI = _Hh3c_s5500_52C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 4)
)
_Hh3c_s5500_28F_EI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28F_EI = _Hh3c_s5500_28F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 5)
)
_Hh3c_s5500_28C_EI_DC_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_EI_DC = _Hh3c_s5500_28C_EI_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 6)
)
_Hh3c_s6100_20Q_SI_ObjectIdentity = ObjectIdentity
hh3c_s6100_20Q_SI = _Hh3c_s6100_20Q_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 7)
)
_Hh3c_s5500_28C_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_SI = _Hh3c_s5500_28C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 8)
)
_Hh3c_s5500_52C_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_52C_SI = _Hh3c_s5500_52C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 9)
)
_Hh3c_s5500_28C_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_28C_PWR_SI = _Hh3c_s5500_28C_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 10)
)
_Hh3c_s5500_52C_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_52C_PWR_SI = _Hh3c_s5500_52C_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 11)
)
_Hh3c_s5510_24P_ObjectIdentity = ObjectIdentity
hh3c_s5510_24P = _Hh3c_s5510_24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 12)
)
_Hh3c_s5510_24F_ObjectIdentity = ObjectIdentity
hh3c_s5510_24F = _Hh3c_s5510_24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 13)
)
_Hh3c_s3610_28P_ObjectIdentity = ObjectIdentity
hh3c_s3610_28P = _Hh3c_s3610_28P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 14)
)
_Hh3c_s3610_52P_ObjectIdentity = ObjectIdentity
hh3c_s3610_52P = _Hh3c_s3610_52P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 15)
)
_Hh3c_s3610_28TP_ObjectIdentity = ObjectIdentity
hh3c_s3610_28TP = _Hh3c_s3610_28TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 16)
)
_Hh3c_s3610_28F_ObjectIdentity = ObjectIdentity
hh3c_s3610_28F = _Hh3c_s3610_28F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 17)
)
_Hh3c_e126_ObjectIdentity = ObjectIdentity
hh3c_e126 = _Hh3c_e126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 18)
)
_Hh3c_e328_ObjectIdentity = ObjectIdentity
hh3c_e328 = _Hh3c_e328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 19)
)
_Hh3c_e352_ObjectIdentity = ObjectIdentity
hh3c_e352 = _Hh3c_e352_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 20)
)
_Hh3c_s3100_8C_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_8C_SI = _Hh3c_s3100_8C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 21)
)
_Hh3c_s3100_16C_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16C_SI = _Hh3c_s3100_16C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 22)
)
_Hh3c_s3100_26C_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26C_SI = _Hh3c_s3100_26C_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 23)
)
_Hh3c_s3100_8T_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_8T_SI = _Hh3c_s3100_8T_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 24)
)
_Hh3c_s3100_16T_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16T_SI = _Hh3c_s3100_16T_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 25)
)
_Hh3c_s3100_26T_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26T_SI = _Hh3c_s3100_26T_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 26)
)
_Hh3c_s3100_26TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_SI = _Hh3c_s3100_26TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 27)
)
_Hh3c_s5100_24P_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_24P_EI = _Hh3c_s5100_24P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 28)
)
_Hh3c_s5100_26C_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_26C_EI = _Hh3c_s5100_26C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 29)
)
_Hh3c_s5100_50C_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_50C_EI = _Hh3c_s5100_50C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 30)
)
_Hh3c_s5100_48P_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_48P_EI = _Hh3c_s5100_48P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 31)
)
_Hh3c_s3600_28P_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_SI = _Hh3c_s3600_28P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 32)
)
_Hh3c_s3600_52P_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_SI = _Hh3c_s3600_52P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 33)
)
_Hh3c_s3600_28TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28TP_SI = _Hh3c_s3600_28TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 34)
)
_Hh3c_s3600_28P_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_PWR_SI = _Hh3c_s3600_28P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 35)
)
_Hh3c_s3600_52P_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_PWR_SI = _Hh3c_s3600_52P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 36)
)
_Hh3c_s3600_28P_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_EI = _Hh3c_s3600_28P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 37)
)
_Hh3c_s3600_52P_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_EI = _Hh3c_s3600_52P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 38)
)
_Hh3c_s3600_28P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_PWR_EI = _Hh3c_s3600_28P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 39)
)
_Hh3c_s3600_52P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_PWR_EI = _Hh3c_s3600_52P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 40)
)
_Hh3c_s3600_28F_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28F_EI = _Hh3c_s3600_28F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 41)
)
_Hh3c_s5600_26C_ObjectIdentity = ObjectIdentity
hh3c_s5600_26C = _Hh3c_s5600_26C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 42)
)
_Hh3c_s5600_50C_ObjectIdentity = ObjectIdentity
hh3c_s5600_50C = _Hh3c_s5600_50C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 43)
)
_Hh3c_s5600_26C_PWR_ObjectIdentity = ObjectIdentity
hh3c_s5600_26C_PWR = _Hh3c_s5600_26C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 44)
)
_Hh3c_s5600_50C_PWR_ObjectIdentity = ObjectIdentity
hh3c_s5600_50C_PWR = _Hh3c_s5600_50C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 45)
)
_Hh3c_s5600_26F_ObjectIdentity = ObjectIdentity
hh3c_s5600_26F = _Hh3c_s5600_26F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 46)
)
_Hh3c_s3600_52G_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52G_HI = _Hh3c_s3600_52G_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 47)
)
_Hh3c_s3600_52P_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52P_HI = _Hh3c_s3600_52P_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 48)
)
_Hh3c_s3600_28G_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28G_HI = _Hh3c_s3600_28G_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 49)
)
_Hh3c_s3600_28P_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_28P_HI = _Hh3c_s3600_28P_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 50)
)
_Hh3c_s3600_52M_HI_ObjectIdentity = ObjectIdentity
hh3c_s3600_52M_HI = _Hh3c_s3600_52M_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 51)
)
_Hh3c_s7502_ObjectIdentity = ObjectIdentity
hh3c_s7502 = _Hh3c_s7502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 52)
)
_Hh3c_s7503_ObjectIdentity = ObjectIdentity
hh3c_s7503 = _Hh3c_s7503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 53)
)
_Hh3c_s7506_ObjectIdentity = ObjectIdentity
hh3c_s7506 = _Hh3c_s7506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 54)
)
_Hh3c_s7506R_ObjectIdentity = ObjectIdentity
hh3c_s7506R = _Hh3c_s7506R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 55)
)
_Hh3c_ar28_09_ObjectIdentity = ObjectIdentity
hh3c_ar28_09 = _Hh3c_ar28_09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 57)
)
_Hh3c_ar28_10_ObjectIdentity = ObjectIdentity
hh3c_ar28_10 = _Hh3c_ar28_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 58)
)
_Hh3c_ar28_11_ObjectIdentity = ObjectIdentity
hh3c_ar28_11 = _Hh3c_ar28_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 59)
)
_Hh3c_ar28_12_ObjectIdentity = ObjectIdentity
hh3c_ar28_12 = _Hh3c_ar28_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 60)
)
_Hh3c_ar28_13_ObjectIdentity = ObjectIdentity
hh3c_ar28_13 = _Hh3c_ar28_13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 61)
)
_Hh3c_ar28_14_ObjectIdentity = ObjectIdentity
hh3c_ar28_14 = _Hh3c_ar28_14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 62)
)
_Hh3c_ar28_30_ObjectIdentity = ObjectIdentity
hh3c_ar28_30 = _Hh3c_ar28_30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 63)
)
_Hh3c_ar28_31_ObjectIdentity = ObjectIdentity
hh3c_ar28_31 = _Hh3c_ar28_31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 64)
)
_Hh3c_ar28_40_ObjectIdentity = ObjectIdentity
hh3c_ar28_40 = _Hh3c_ar28_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 65)
)
_Hh3c_ar28_80_ObjectIdentity = ObjectIdentity
hh3c_ar28_80 = _Hh3c_ar28_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 66)
)
_Hh3c_ar46_20_ObjectIdentity = ObjectIdentity
hh3c_ar46_20 = _Hh3c_ar46_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 67)
)
_Hh3c_ar46_40_ObjectIdentity = ObjectIdentity
hh3c_ar46_40 = _Hh3c_ar46_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 68)
)
_Hh3c_ar46_80_ObjectIdentity = ObjectIdentity
hh3c_ar46_80 = _Hh3c_ar46_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 69)
)
_Hh3c_msr20_20_ObjectIdentity = ObjectIdentity
hh3c_msr20_20 = _Hh3c_msr20_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 70)
)
_Hh3c_msr20_21_ObjectIdentity = ObjectIdentity
hh3c_msr20_21 = _Hh3c_msr20_21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 71)
)
_Hh3c_msr20_40_ObjectIdentity = ObjectIdentity
hh3c_msr20_40 = _Hh3c_msr20_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 72)
)
_Hh3c_msr30_20_ObjectIdentity = ObjectIdentity
hh3c_msr30_20 = _Hh3c_msr30_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 73)
)
_Hh3c_msr30_40_ObjectIdentity = ObjectIdentity
hh3c_msr30_40 = _Hh3c_msr30_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 74)
)
_Hh3c_msr30_60_ObjectIdentity = ObjectIdentity
hh3c_msr30_60 = _Hh3c_msr30_60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 75)
)
_Hh3c_msr50_40_ObjectIdentity = ObjectIdentity
hh3c_msr50_40 = _Hh3c_msr50_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 76)
)
_Hh3c_msr50_60_ObjectIdentity = ObjectIdentity
hh3c_msr50_60 = _Hh3c_msr50_60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 77)
)
_Hh3c_ar18_21_ObjectIdentity = ObjectIdentity
hh3c_ar18_21 = _Hh3c_ar18_21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 88)
)
_Hh3c_ar18_21A_ObjectIdentity = ObjectIdentity
hh3c_ar18_21A = _Hh3c_ar18_21A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 89)
)
_Hh3c_ar18_21B_ObjectIdentity = ObjectIdentity
hh3c_ar18_21B = _Hh3c_ar18_21B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 90)
)
_Hh3c_ar18_22_ObjectIdentity = ObjectIdentity
hh3c_ar18_22 = _Hh3c_ar18_22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 91)
)
_Hh3c_ar18_22_8_ObjectIdentity = ObjectIdentity
hh3c_ar18_22_8 = _Hh3c_ar18_22_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 92)
)
_Hh3c_ar18_22S_8_ObjectIdentity = ObjectIdentity
hh3c_ar18_22S_8 = _Hh3c_ar18_22S_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 93)
)
_Hh3c_ar18_22_24_ObjectIdentity = ObjectIdentity
hh3c_ar18_22_24 = _Hh3c_ar18_22_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 94)
)
_Hh3c_ar18_23_1_ObjectIdentity = ObjectIdentity
hh3c_ar18_23_1 = _Hh3c_ar18_23_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 95)
)
_Hh3c_ar18_23S_1_ObjectIdentity = ObjectIdentity
hh3c_ar18_23S_1 = _Hh3c_ar18_23S_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 96)
)
_Hh3c_ar18_30E_ObjectIdentity = ObjectIdentity
hh3c_ar18_30E = _Hh3c_ar18_30E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 98)
)
_Hh3c_ar18_31E_ObjectIdentity = ObjectIdentity
hh3c_ar18_31E = _Hh3c_ar18_31E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 100)
)
_Hh3c_ar18_32E_ObjectIdentity = ObjectIdentity
hh3c_ar18_32E = _Hh3c_ar18_32E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 102)
)
_Hh3c_ar18_33_ObjectIdentity = ObjectIdentity
hh3c_ar18_33 = _Hh3c_ar18_33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 103)
)
_Hh3c_ar18_33E_ObjectIdentity = ObjectIdentity
hh3c_ar18_33E = _Hh3c_ar18_33E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 104)
)
_Hh3c_ar18_34_ObjectIdentity = ObjectIdentity
hh3c_ar18_34 = _Hh3c_ar18_34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 105)
)
_Hh3c_ar18_34E_ObjectIdentity = ObjectIdentity
hh3c_ar18_34E = _Hh3c_ar18_34E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 106)
)
_Hh3c_ar18_35E_ObjectIdentity = ObjectIdentity
hh3c_ar18_35E = _Hh3c_ar18_35E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 108)
)
_Hh3c_ar18_63_1_ObjectIdentity = ObjectIdentity
hh3c_ar18_63_1 = _Hh3c_ar18_63_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 109)
)
_Hh3c_secpathF100_C_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_C = _Hh3c_secpathF100_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 110)
)
_Hh3c_secpathF100_A_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_A = _Hh3c_secpathF100_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 111)
)
_Hh3c_secpathF100_S_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_S = _Hh3c_secpathF100_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 112)
)
_Hh3c_secpathF100_E_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_E = _Hh3c_secpathF100_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 113)
)
_Hh3c_secpathF1000_S_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_S = _Hh3c_secpathF1000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 114)
)
_Hh3c_secpathF1000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_A = _Hh3c_secpathF1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 115)
)
_Hh3c_secpathF1800_A_ObjectIdentity = ObjectIdentity
hh3c_secpathF1800_A = _Hh3c_secpathF1800_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 116)
)
_Hh3c_secpathV100_S_ObjectIdentity = ObjectIdentity
hh3c_secpathV100_S = _Hh3c_secpathV100_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 117)
)
_Hh3c_secpathV1000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathV1000_A = _Hh3c_secpathV1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 118)
)
_Hh3c_secpathF100_AW_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_AW = _Hh3c_secpathF100_AW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 119)
)
_Hh3c_secpathF1800_S_ObjectIdentity = ObjectIdentity
hh3c_secpathF1800_S = _Hh3c_secpathF1800_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 120)
)
_Hh3c_secpathF1800_E_ObjectIdentity = ObjectIdentity
hh3c_secpathF1800_E = _Hh3c_secpathF1800_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 121)
)
_Hh3c_secpoint_ObjectIdentity = ObjectIdentity
hh3c_secpoint = _Hh3c_secpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 122)
)
_Hh3c_vg10_10_ObjectIdentity = ObjectIdentity
hh3c_vg10_10 = _Hh3c_vg10_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 123)
)
_Hh3c_vg10_11_ObjectIdentity = ObjectIdentity
hh3c_vg10_11 = _Hh3c_vg10_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 124)
)
_Hh3c_vg10_40_ObjectIdentity = ObjectIdentity
hh3c_vg10_40 = _Hh3c_vg10_40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 125)
)
_Hh3c_vg10_41_ObjectIdentity = ObjectIdentity
hh3c_vg10_41 = _Hh3c_vg10_41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 126)
)
_Hh3c_vg21_08_ObjectIdentity = ObjectIdentity
hh3c_vg21_08 = _Hh3c_vg21_08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 127)
)
_Hh3c_vg20_16_ObjectIdentity = ObjectIdentity
hh3c_vg20_16 = _Hh3c_vg20_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 128)
)
_Hh3c_vg20_32_ObjectIdentity = ObjectIdentity
hh3c_vg20_32 = _Hh3c_vg20_32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 129)
)
_Hh3c_vg80_20_ObjectIdentity = ObjectIdentity
hh3c_vg80_20 = _Hh3c_vg80_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 130)
)
_Hh3c_xe200_ObjectIdentity = ObjectIdentity
hh3c_xe200 = _Hh3c_xe200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 131)
)
_Hh3c_xe2000_ObjectIdentity = ObjectIdentity
hh3c_xe2000 = _Hh3c_xe2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 132)
)
_Hh3c_xe7200_ObjectIdentity = ObjectIdentity
hh3c_xe7200 = _Hh3c_xe7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 133)
)
_Hh3c_xe7300_ObjectIdentity = ObjectIdentity
hh3c_xe7300 = _Hh3c_xe7300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 134)
)
_Hh3c_xe7500_ObjectIdentity = ObjectIdentity
hh3c_xe7500 = _Hh3c_xe7500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 135)
)
_Hh3c_xe7600_ObjectIdentity = ObjectIdentity
hh3c_xe7600 = _Hh3c_xe7600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 136)
)
_Hh3c_xe7205_ObjectIdentity = ObjectIdentity
hh3c_xe7205 = _Hh3c_xe7205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 137)
)
_Hh3c_xe7305_ObjectIdentity = ObjectIdentity
hh3c_xe7305 = _Hh3c_xe7305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 138)
)
_Hh3c_xe7505_ObjectIdentity = ObjectIdentity
hh3c_xe7505 = _Hh3c_xe7505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 139)
)
_Hh3c_xe7605_ObjectIdentity = ObjectIdentity
hh3c_xe7605 = _Hh3c_xe7605_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 140)
)
_Hh3c_neoceanIX1000_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX1000 = _Hh3c_neoceanIX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 141)
)
_Hh3c_neoceanEX1000_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1000 = _Hh3c_neoceanEX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 142)
)
_Hh3c_neoceanEX800_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX800 = _Hh3c_neoceanEX800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 143)
)
_Hh3c_neoceanIX5000_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX5000 = _Hh3c_neoceanIX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 144)
)
_Hh3c_neoceanIV5100_ObjectIdentity = ObjectIdentity
hh3c_neoceanIV5100 = _Hh3c_neoceanIV5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 145)
)
_Hh3c_neoceanIV5200_ObjectIdentity = ObjectIdentity
hh3c_neoceanIV5200 = _Hh3c_neoceanIV5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 146)
)
_Hh3c_s9502_ObjectIdentity = ObjectIdentity
hh3c_s9502 = _Hh3c_s9502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 147)
)
_Hh3c_s9505_ObjectIdentity = ObjectIdentity
hh3c_s9505 = _Hh3c_s9505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 148)
)
_Hh3c_s9508_ObjectIdentity = ObjectIdentity
hh3c_s9508 = _Hh3c_s9508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 149)
)
_Hh3c_s9508V_ObjectIdentity = ObjectIdentity
hh3c_s9508V = _Hh3c_s9508V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 150)
)
_Hh3c_s9512_ObjectIdentity = ObjectIdentity
hh3c_s9512 = _Hh3c_s9512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 151)
)
_Hh3c_sR8812_ObjectIdentity = ObjectIdentity
hh3c_sR8812 = _Hh3c_sR8812_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 152)
)
_Hh3c_sR8808_ObjectIdentity = ObjectIdentity
hh3c_sR8808 = _Hh3c_sR8808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 153)
)
_Hh3c_sR8805_ObjectIdentity = ObjectIdentity
hh3c_sR8805 = _Hh3c_sR8805_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 154)
)
_Hh3c_sR8802_ObjectIdentity = ObjectIdentity
hh3c_sR8802 = _Hh3c_sR8802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 155)
)
_Hh3c_e126_SI_ObjectIdentity = ObjectIdentity
hh3c_e126_SI = _Hh3c_e126_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 156)
)
_Hh3c_vg31_08_ObjectIdentity = ObjectIdentity
hh3c_vg31_08 = _Hh3c_vg31_08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 157)
)
_Hh3c_dr834_ObjectIdentity = ObjectIdentity
hh3c_dr834 = _Hh3c_dr834_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 158)
)
_Hh3c_s7510E_ObjectIdentity = ObjectIdentity
hh3c_s7510E = _Hh3c_s7510E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 159)
)
_Hh3c_s5100_24P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5100_24P_SI = _Hh3c_s5100_24P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 160)
)
_Hh3c_s5100_48P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5100_48P_SI = _Hh3c_s5100_48P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 161)
)
_Hh3c_s5100_8P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5100_8P_SI = _Hh3c_s5100_8P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 162)
)
_Hh3c_s5100_16P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5100_16P_SI = _Hh3c_s5100_16P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 163)
)
_Hh3c_s5100_8P_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_8P_EI = _Hh3c_s5100_8P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 164)
)
_Hh3c_s5100_16P_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_16P_EI = _Hh3c_s5100_16P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 165)
)
_Hh3c_s5100_8P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_8P_PWR_EI = _Hh3c_s5100_8P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 166)
)
_Hh3c_s5100_16P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_16P_PWR_EI = _Hh3c_s5100_16P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 167)
)
_Hh3c_s5100_26C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_26C_PWR_EI = _Hh3c_s5100_26C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 168)
)
_Hh3c_s5100_50C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s5100_50C_PWR_EI = _Hh3c_s5100_50C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 169)
)
_Hh3c_s3108TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3108TP_EI = _Hh3c_s3108TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 170)
)
_Hh3c_s3116TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3116TP_EI = _Hh3c_s3116TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 171)
)
_Hh3c_s3126TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3126TP_EI = _Hh3c_s3126TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 172)
)
_Hh3c_s3108TP_EI_PWR_ObjectIdentity = ObjectIdentity
hh3c_s3108TP_EI_PWR = _Hh3c_s3108TP_EI_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 173)
)
_Hh3c_s3116TP_EI_PWR_ObjectIdentity = ObjectIdentity
hh3c_s3116TP_EI_PWR = _Hh3c_s3116TP_EI_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 174)
)
_Hh3c_s3126TP_EI_PWR_ObjectIdentity = ObjectIdentity
hh3c_s3126TP_EI_PWR = _Hh3c_s3126TP_EI_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 175)
)
_Hh3c_s5500M_20C_ObjectIdentity = ObjectIdentity
hh3c_s5500M_20C = _Hh3c_s5500M_20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 177)
)
_Hh3c_s5500M_20F_ObjectIdentity = ObjectIdentity
hh3c_s5500M_20F = _Hh3c_s5500M_20F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 178)
)
_Hh3c_bR304plus_ObjectIdentity = ObjectIdentity
hh3c_bR304plus = _Hh3c_bR304plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 179)
)
_Hh3c_s9505_V5_ObjectIdentity = ObjectIdentity
hh3c_s9505_V5 = _Hh3c_s9505_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 180)
)
_Hh3c_s9512_V5_ObjectIdentity = ObjectIdentity
hh3c_s9512_V5 = _Hh3c_s9512_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 181)
)
_Hh3c_s9508_V5_ObjectIdentity = ObjectIdentity
hh3c_s9508_V5 = _Hh3c_s9508_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 182)
)
_Hh3c_s9508V_V5_ObjectIdentity = ObjectIdentity
hh3c_s9508V_V5 = _Hh3c_s9508V_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 183)
)
_Hh3c_s9502_V5_ObjectIdentity = ObjectIdentity
hh3c_s9502_V5 = _Hh3c_s9502_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 184)
)
_Hh3c_sR8802_V5_ObjectIdentity = ObjectIdentity
hh3c_sR8802_V5 = _Hh3c_sR8802_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 185)
)
_Hh3c_sR8805_V5_ObjectIdentity = ObjectIdentity
hh3c_sR8805_V5 = _Hh3c_sR8805_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 186)
)
_Hh3c_sR8812_V5_ObjectIdentity = ObjectIdentity
hh3c_sR8812_V5 = _Hh3c_sR8812_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 187)
)
_Hh3c_sR8808_V5_ObjectIdentity = ObjectIdentity
hh3c_sR8808_V5 = _Hh3c_sR8808_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 188)
)
_Hh3c_s3100_52P_ObjectIdentity = ObjectIdentity
hh3c_s3100_52P = _Hh3c_s3100_52P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 189)
)
_Hh3c_e152_ObjectIdentity = ObjectIdentity
hh3c_e152 = _Hh3c_e152_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 190)
)
_Hh3c_s2008_ObjectIdentity = ObjectIdentity
hh3c_s2008 = _Hh3c_s2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 191)
)
_Hh3c_s2026_ObjectIdentity = ObjectIdentity
hh3c_s2026 = _Hh3c_s2026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 192)
)
_Hh3c_sr6602_ObjectIdentity = ObjectIdentity
hh3c_sr6602 = _Hh3c_sr6602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 193)
)
_Hh3c_sr6608_ObjectIdentity = ObjectIdentity
hh3c_sr6608 = _Hh3c_sr6608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 194)
)
_Hh3c_s3100_08TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_08TP_EI = _Hh3c_s3100_08TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 195)
)
_Hh3c_s3100_08TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_08TP_PWR_EI = _Hh3c_s3100_08TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 196)
)
_Hh3c_s3100_16TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16TP_EI = _Hh3c_s3100_16TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 197)
)
_Hh3c_s3100_16TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16TP_PWR_EI = _Hh3c_s3100_16TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 198)
)
_Hh3c_s3100_26TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_EI = _Hh3c_s3100_26TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 199)
)
_Hh3c_s3100_26TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_PWR_EI = _Hh3c_s3100_26TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 200)
)
_Hh3c_s7502_v5_ObjectIdentity = ObjectIdentity
hh3c_s7502_v5 = _Hh3c_s7502_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 201)
)
_Hh3c_vg80_21_ObjectIdentity = ObjectIdentity
hh3c_vg80_21 = _Hh3c_vg80_21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 202)
)
_Hh3c_vg80_80_ObjectIdentity = ObjectIdentity
hh3c_vg80_80 = _Hh3c_vg80_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 203)
)
_Hh3c_wcm_wx5002_ObjectIdentity = ObjectIdentity
hh3c_wcm_wx5002 = _Hh3c_wcm_wx5002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 204)
)
_Hh3c_wcm_wcma_ObjectIdentity = ObjectIdentity
hh3c_wcm_wcma = _Hh3c_wcm_wcma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 205)
)
_Hh3c_msr30_10_ObjectIdentity = ObjectIdentity
hh3c_msr30_10 = _Hh3c_msr30_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 206)
)
_Hh3c_s7502e_ObjectIdentity = ObjectIdentity
hh3c_s7502e = _Hh3c_s7502e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 207)
)
_Hh3c_s7503E_ObjectIdentity = ObjectIdentity
hh3c_s7503E = _Hh3c_s7503E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 208)
)
_Hh3c_s7506E_ObjectIdentity = ObjectIdentity
hh3c_s7506E = _Hh3c_s7506E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 209)
)
_Hh3c_s7506E_V_ObjectIdentity = ObjectIdentity
hh3c_s7506E_V = _Hh3c_s7506E_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 210)
)
_Hh3c_secBlade_FW_ObjectIdentity = ObjectIdentity
hh3c_secBlade_FW = _Hh3c_secBlade_FW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 211)
)
_Hh3c_secBlade_IPSec_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IPSec = _Hh3c_secBlade_IPSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 212)
)
_Hh3c_s3100_8TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_8TP_SI = _Hh3c_s3100_8TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 213)
)
_Hh3c_s3100_16TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3100_16TP_SI = _Hh3c_s3100_16TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 214)
)
_Hh3c_e126A_ObjectIdentity = ObjectIdentity
hh3c_e126A = _Hh3c_e126A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 215)
)
_Hh3c_s3100_26TP_SI_B_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_SI_B = _Hh3c_s3100_26TP_SI_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 216)
)
_Hh3c_msr30_16_ObjectIdentity = ObjectIdentity
hh3c_msr30_16 = _Hh3c_msr30_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 217)
)
_Hh3cOEMProductID_ObjectIdentity = ObjectIdentity
hh3cOEMProductID = _Hh3cOEMProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 218)
)
_Hh3c_s2126_ei_ObjectIdentity = ObjectIdentity
hh3c_s2126_ei = _Hh3c_s2126_ei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 219)
)
_Hh3c_e150_si_ObjectIdentity = ObjectIdentity
hh3c_e150_si = _Hh3c_e150_si_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 220)
)
_Hh3c_msr30_11_ObjectIdentity = ObjectIdentity
hh3c_msr30_11 = _Hh3c_msr30_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 221)
)
_Hh3c_neoceanIX3040_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3040 = _Hh3c_neoceanIX3040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 222)
)
_Hh3c_neoceanIX3080_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3080 = _Hh3c_neoceanIX3080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 223)
)
_Hh3c_secpathF100_M_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_M = _Hh3c_secpathF100_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 224)
)
_Hh3c_neoceanVX1500_ObjectIdentity = ObjectIdentity
hh3c_neoceanVX1500 = _Hh3c_neoceanVX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 225)
)
_Hh3c_neoceanIX1520_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX1520 = _Hh3c_neoceanIX1520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 226)
)
_Hh3c_neoceanIX1540_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX1540 = _Hh3c_neoceanIX1540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 227)
)
_Hh3c_wcm_wx5002_128ap_ObjectIdentity = ObjectIdentity
hh3c_wcm_wx5002_128ap = _Hh3c_wcm_wx5002_128ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 228)
)
_Hh3c_msr20_10_ObjectIdentity = ObjectIdentity
hh3c_msr20_10 = _Hh3c_msr20_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 229)
)
_Hh3c_msr20_11_ObjectIdentity = ObjectIdentity
hh3c_msr20_11 = _Hh3c_msr20_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 230)
)
_Hh3c_msr20_13_ObjectIdentity = ObjectIdentity
hh3c_msr20_13 = _Hh3c_msr20_13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 231)
)
_Hh3c_msr20_15_ObjectIdentity = ObjectIdentity
hh3c_msr20_15 = _Hh3c_msr20_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 232)
)
_Hh3c_neoceanDL1008_ObjectIdentity = ObjectIdentity
hh3c_neoceanDL1008 = _Hh3c_neoceanDL1008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 233)
)
_Hh3c_neoceanDL1008S_ObjectIdentity = ObjectIdentity
hh3c_neoceanDL1008S = _Hh3c_neoceanDL1008S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 234)
)
_Hh3c_neoceanDL1012_ObjectIdentity = ObjectIdentity
hh3c_neoceanDL1012 = _Hh3c_neoceanDL1012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 235)
)
_Hh3c_s3610_52m_ObjectIdentity = ObjectIdentity
hh3c_s3610_52m = _Hh3c_s3610_52m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 236)
)
_Hh3c_IV5680_ObjectIdentity = ObjectIdentity
hh3c_IV5680 = _Hh3c_IV5680_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 237)
)
_Hh3c_IV5240_ObjectIdentity = ObjectIdentity
hh3c_IV5240 = _Hh3c_IV5240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 238)
)
_Hh3c_F1000_E_ObjectIdentity = ObjectIdentity
hh3c_F1000_E = _Hh3c_F1000_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 239)
)
_Hh3c_S5024P_ObjectIdentity = ObjectIdentity
hh3c_S5024P = _Hh3c_S5024P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 240)
)
_Hh3c_S5016P_ObjectIdentity = ObjectIdentity
hh3c_S5016P = _Hh3c_S5016P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 241)
)
_Hh3c_LSQ1FWBSC0_ObjectIdentity = ObjectIdentity
hh3c_LSQ1FWBSC0 = _Hh3c_LSQ1FWBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 242)
)
_Hh3c_LSB1FW2A0_ObjectIdentity = ObjectIdentity
hh3c_LSB1FW2A0 = _Hh3c_LSB1FW2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 243)
)
_Hh3c_S3100_8TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_8TP_EI = _Hh3c_S3100_8TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 244)
)
_Hh3c_S3100_16TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_16TP_EI = _Hh3c_S3100_16TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 245)
)
_Hh3c_S3100_26TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_26TP_EI = _Hh3c_S3100_26TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 246)
)
_Hh3c_ET704_ObjectIdentity = ObjectIdentity
hh3c_ET704 = _Hh3c_ET704_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 247)
)
_Hh3c_ec1001_ObjectIdentity = ObjectIdentity
hh3c_ec1001 = _Hh3c_ec1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 248)
)
_Hh3c_ec1001_hf_ObjectIdentity = ObjectIdentity
hh3c_ec1001_hf = _Hh3c_ec1001_hf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 249)
)
_Hh3c_ec1004_hc_ObjectIdentity = ObjectIdentity
hh3c_ec1004_hc = _Hh3c_ec1004_hc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 250)
)
_Hh3c_ec2004_hf_ObjectIdentity = ObjectIdentity
hh3c_ec2004_hf = _Hh3c_ec2004_hf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 251)
)
_Hh3c_dc1001_ObjectIdentity = ObjectIdentity
hh3c_dc1001 = _Hh3c_dc1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 252)
)
_Hh3c_dm8000_ObjectIdentity = ObjectIdentity
hh3c_dm8000 = _Hh3c_dm8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 253)
)
_Hh3c_vm8000_ObjectIdentity = ObjectIdentity
hh3c_vm8000 = _Hh3c_vm8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 254)
)
_Hh3c_ms8000_ObjectIdentity = ObjectIdentity
hh3c_ms8000 = _Hh3c_ms8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 255)
)
_Hh3c_S3100_52TP_ObjectIdentity = ObjectIdentity
hh3c_S3100_52TP = _Hh3c_S3100_52TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 256)
)
_Hh3c_msr20_12_ObjectIdentity = ObjectIdentity
hh3c_msr20_12 = _Hh3c_msr20_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 257)
)
_Hh3c_s1550E_ObjectIdentity = ObjectIdentity
hh3c_s1550E = _Hh3c_s1550E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 258)
)
_Hh3c_s1550_ObjectIdentity = ObjectIdentity
hh3c_s1550 = _Hh3c_s1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 259)
)
_Hh3c_s1526_EI_ObjectIdentity = ObjectIdentity
hh3c_s1526_EI = _Hh3c_s1526_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 260)
)
_Hh3c_msr20_12_T_ObjectIdentity = ObjectIdentity
hh3c_msr20_12_T = _Hh3c_msr20_12_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 261)
)
_Hh3c_msr20_15_I_ObjectIdentity = ObjectIdentity
hh3c_msr20_15_I = _Hh3c_msr20_15_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 262)
)
_Hh3c_msr20_15_N_ObjectIdentity = ObjectIdentity
hh3c_msr20_15_N = _Hh3c_msr20_15_N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 263)
)
_Hh3c_wx6100EWPX_ObjectIdentity = ObjectIdentity
hh3c_wx6100EWPX = _Hh3c_wx6100EWPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 264)
)
_Hh3c_wx6100LSQ_ObjectIdentity = ObjectIdentity
hh3c_wx6100LSQ = _Hh3c_wx6100LSQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 265)
)
_Hh3c_wx6100LSB_ObjectIdentity = ObjectIdentity
hh3c_wx6100LSB = _Hh3c_wx6100LSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 266)
)
_Hh3c_wx6100SW_ObjectIdentity = ObjectIdentity
hh3c_wx6100SW = _Hh3c_wx6100SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 267)
)
_Hh3c_dl1000_ObjectIdentity = ObjectIdentity
hh3c_dl1000 = _Hh3c_dl1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 268)
)
_Hh3c_dl1000s_ObjectIdentity = ObjectIdentity
hh3c_dl1000s = _Hh3c_dl1000s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 269)
)
_Hh3c_wa1208e_g_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_g = _Hh3c_wa1208e_g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 270)
)
_Hh3c_wa1208e_dg_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_dg = _Hh3c_wa1208e_dg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 271)
)
_Hh3c_wa1208e_ag_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_ag = _Hh3c_wa1208e_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 272)
)
_Hh3c_wa1208e_agp_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_agp = _Hh3c_wa1208e_agp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 273)
)
_Hh3c_S7501M_24T_ObjectIdentity = ObjectIdentity
hh3c_S7501M_24T = _Hh3c_S7501M_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 274)
)
_Hh3c_s7501M_24TP_ObjectIdentity = ObjectIdentity
hh3c_s7501M_24TP = _Hh3c_s7501M_24TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 275)
)
_Hh3c_s7502M_ObjectIdentity = ObjectIdentity
hh3c_s7502M = _Hh3c_s7502M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 276)
)
_Hh3c_s7503M_ObjectIdentity = ObjectIdentity
hh3c_s7503M = _Hh3c_s7503M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 277)
)
_Hh3c_s7506M_ObjectIdentity = ObjectIdentity
hh3c_s7506M = _Hh3c_s7506M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 278)
)
_Hh3c_s7506M_V_ObjectIdentity = ObjectIdentity
hh3c_s7506M_V = _Hh3c_s7506M_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 279)
)
_Hh3c_s7510M_ObjectIdentity = ObjectIdentity
hh3c_s7510M = _Hh3c_s7510M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 280)
)
_Hh3c_secpathT200_ObjectIdentity = ObjectIdentity
hh3c_secpathT200 = _Hh3c_secpathT200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 281)
)
_Hh3c_secpathT200E_ObjectIdentity = ObjectIdentity
hh3c_secpathT200E = _Hh3c_secpathT200E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 282)
)
_Hh3c_cc600_ObjectIdentity = ObjectIdentity
hh3c_cc600 = _Hh3c_cc600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 283)
)
_Hh3c_wa1208e_gp_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_gp = _Hh3c_wa1208e_gp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 284)
)
_Hh3c_wb2321e_agp_ObjectIdentity = ObjectIdentity
hh3c_wb2321e_agp = _Hh3c_wb2321e_agp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 285)
)
_Hh3c_wh2520e_agp_ObjectIdentity = ObjectIdentity
hh3c_wh2520e_agp = _Hh3c_wh2520e_agp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 286)
)
_Hh3c_ICG2000_ObjectIdentity = ObjectIdentity
hh3c_ICG2000 = _Hh3c_ICG2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 287)
)
_Hh3c_ICG3000_ObjectIdentity = ObjectIdentity
hh3c_ICG3000 = _Hh3c_ICG3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 288)
)
_Hh3c_ICG5000_ObjectIdentity = ObjectIdentity
hh3c_ICG5000 = _Hh3c_ICG5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 289)
)
_Hh3c_S5520TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S5520TP_SI = _Hh3c_S5520TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 290)
)
_Hh3c_wa2210_ag_ObjectIdentity = ObjectIdentity
hh3c_wa2210_ag = _Hh3c_wa2210_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 291)
)
_Hh3c_wa2220_ag_ObjectIdentity = ObjectIdentity
hh3c_wa2220_ag = _Hh3c_wa2220_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 292)
)
_Hh3c_wa2220e_ag_ObjectIdentity = ObjectIdentity
hh3c_wa2220e_ag = _Hh3c_wa2220e_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 293)
)
_Hh3c_wa2210x_g_ObjectIdentity = ObjectIdentity
hh3c_wa2210x_g = _Hh3c_wa2210x_g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 294)
)
_Hh3c_wa2220x_ag_ObjectIdentity = ObjectIdentity
hh3c_wa2220x_ag = _Hh3c_wa2220x_ag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 295)
)
_Hh3c_wa2220x_agp_ObjectIdentity = ObjectIdentity
hh3c_wa2220x_agp = _Hh3c_wa2220x_agp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 296)
)
_Hh3c_S3100_52TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S3100_52TP_SI = _Hh3c_S3100_52TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 297)
)
_Hh3c_secpathASE5000_E_ObjectIdentity = ObjectIdentity
hh3c_secpathASE5000_E = _Hh3c_secpathASE5000_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 298)
)
_Hh3c_secpathASE5000_S_ObjectIdentity = ObjectIdentity
hh3c_secpathASE5000_S = _Hh3c_secpathASE5000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 299)
)
_Hh3c_secpathU200_C_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_C = _Hh3c_secpathU200_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 300)
)
_Hh3c_secpathU200_S_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_S = _Hh3c_secpathU200_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 301)
)
_Hh3c_secpathU200_A_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_A = _Hh3c_secpathU200_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 302)
)
_Hh3c_secpathU200_M_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_M = _Hh3c_secpathU200_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 303)
)
_Hh3c_ec3016_hc_ObjectIdentity = ObjectIdentity
hh3c_ec3016_hc = _Hh3c_ec3016_hc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 304)
)
_Hh3c_dc1001_ff_ObjectIdentity = ObjectIdentity
hh3c_dc1001_ff = _Hh3c_dc1001_ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 305)
)
_Hh3c_ecr3304_hf_ObjectIdentity = ObjectIdentity
hh3c_ecr3304_hf = _Hh3c_ecr3304_hf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 306)
)
_Hh3c_ecr3308_hd_ObjectIdentity = ObjectIdentity
hh3c_ecr3308_hd = _Hh3c_ecr3308_hd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 307)
)
_Hh3c_ecr3316_hc_ObjectIdentity = ObjectIdentity
hh3c_ecr3316_hc = _Hh3c_ecr3316_hc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 308)
)
_Hh3c_isc3000_ObjectIdentity = ObjectIdentity
hh3c_isc3000 = _Hh3c_isc3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 309)
)
_Hh3c_isc3100_ObjectIdentity = ObjectIdentity
hh3c_isc3100 = _Hh3c_isc3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 310)
)
_Hh3c_vm9000_ObjectIdentity = ObjectIdentity
hh3c_vm9000 = _Hh3c_vm9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 311)
)
_Hh3c_vm5000_ObjectIdentity = ObjectIdentity
hh3c_vm5000 = _Hh3c_vm5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 312)
)
_Hh3c_ms9000_vtdu_ObjectIdentity = ObjectIdentity
hh3c_ms9000_vtdu = _Hh3c_ms9000_vtdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 313)
)
_Hh3c_ms9000_nru_ObjectIdentity = ObjectIdentity
hh3c_ms9000_nru = _Hh3c_ms9000_nru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 314)
)
_Hh3c_ums9005_ObjectIdentity = ObjectIdentity
hh3c_ums9005 = _Hh3c_ums9005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 315)
)
_Hh3c_CS2104B_ObjectIdentity = ObjectIdentity
hh3c_CS2104B = _Hh3c_CS2104B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 316)
)
_Hh3c_CS2106B_ObjectIdentity = ObjectIdentity
hh3c_CS2106B = _Hh3c_CS2106B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 317)
)
_Hh3c_S5024E_ObjectIdentity = ObjectIdentity
hh3c_S5024E = _Hh3c_S5024E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 318)
)
_Hh3c_S5048E_ObjectIdentity = ObjectIdentity
hh3c_S5048E = _Hh3c_S5048E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 319)
)
_Hh3c_secpathF5000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathF5000_A = _Hh3c_secpathF5000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 320)
)
_Hh3c_neoceanIX3240_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3240 = _Hh3c_neoceanIX3240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 321)
)
_Hh3c_neoceanIX3620_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3620 = _Hh3c_neoceanIX3620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 322)
)
_Hh3c_MSA7302_ObjectIdentity = ObjectIdentity
hh3c_MSA7302 = _Hh3c_MSA7302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 323)
)
_Hh3c_MSA7306_ObjectIdentity = ObjectIdentity
hh3c_MSA7306 = _Hh3c_MSA7306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 324)
)
_Hh3c_S7501E_ObjectIdentity = ObjectIdentity
hh3c_S7501E = _Hh3c_S7501E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 325)
)
_Hh3c_S3100_8C_EPON_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_8C_EPON_EI = _Hh3c_S3100_8C_EPON_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 326)
)
_Hh3c_S3100_16C_EPON_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_16C_EPON_EI = _Hh3c_S3100_16C_EPON_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 327)
)
_Hh3c_S3100_26C_EPON_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100_26C_EPON_EI = _Hh3c_S3100_26C_EPON_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 328)
)
_Hh3c_secBlade_LSQ1AFCBSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1AFCBSC0 = _Hh3c_secBlade_LSQ1AFCBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 329)
)
_Hh3c_secBlade_LSB1AFC1A0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSB1AFC1A0 = _Hh3c_secBlade_LSB1AFC1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 330)
)
_Hh3c_secpathF1000_C_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_C = _Hh3c_secpathF1000_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 331)
)
_Hh3c_secpathF100_A_SI_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_A_SI = _Hh3c_secpathF100_A_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 332)
)
_Hh3c_secpathV100_E_ObjectIdentity = ObjectIdentity
hh3c_secpathV100_E = _Hh3c_secpathV100_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 333)
)
_Hh3c_S5800_32C_ObjectIdentity = ObjectIdentity
hh3c_S5800_32C = _Hh3c_S5800_32C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 334)
)
_Hh3c_S5800_56C_ObjectIdentity = ObjectIdentity
hh3c_S5800_56C = _Hh3c_S5800_56C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 335)
)
_Hh3c_S5800_32C_PWR_ObjectIdentity = ObjectIdentity
hh3c_S5800_32C_PWR = _Hh3c_S5800_32C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 336)
)
_Hh3c_S5800_56C_PWR_ObjectIdentity = ObjectIdentity
hh3c_S5800_56C_PWR = _Hh3c_S5800_56C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 337)
)
_Hh3c_S5800_60C_PWR_ObjectIdentity = ObjectIdentity
hh3c_S5800_60C_PWR = _Hh3c_S5800_60C_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 338)
)
_Hh3c_S5800_32F_ObjectIdentity = ObjectIdentity
hh3c_S5800_32F = _Hh3c_S5800_32F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 339)
)
_Hh3c_S5820X_28C_ObjectIdentity = ObjectIdentity
hh3c_S5820X_28C = _Hh3c_S5820X_28C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 340)
)
_Hh3c_S5820X_28S_ObjectIdentity = ObjectIdentity
hh3c_S5820X_28S = _Hh3c_S5820X_28S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 341)
)
_Hh3c_cc602_ObjectIdentity = ObjectIdentity
hh3c_cc602 = _Hh3c_cc602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 342)
)
_Hh3c_cr400_ObjectIdentity = ObjectIdentity
hh3c_cr400 = _Hh3c_cr400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 343)
)
_Hh3c_cc600E_ObjectIdentity = ObjectIdentity
hh3c_cc600E = _Hh3c_cc600E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 344)
)
_Hh3c_secpathT1000_M_ObjectIdentity = ObjectIdentity
hh3c_secpathT1000_M = _Hh3c_secpathT1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 345)
)
_Hh3c_neoceanVX1540_ObjectIdentity = ObjectIdentity
hh3c_neoceanVX1540 = _Hh3c_neoceanVX1540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 346)
)
_Hh3c_msr50_06_ObjectIdentity = ObjectIdentity
hh3c_msr50_06 = _Hh3c_msr50_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 347)
)
_Hh3c_secpathACG2000_M_ObjectIdentity = ObjectIdentity
hh3c_secpathACG2000_M = _Hh3c_secpathACG2000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 348)
)
_Hh3c_secBlade_LSQ1ACGASC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1ACGASC0 = _Hh3c_secBlade_LSQ1ACGASC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 349)
)
_Hh3c_secBlade_LSB1ACG1A0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSB1ACG1A0 = _Hh3c_secBlade_LSB1ACG1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 350)
)
_Hh3c_wx3024wcm_ObjectIdentity = ObjectIdentity
hh3c_wx3024wcm = _Hh3c_wx3024wcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 351)
)
_Hh3c_wx3024lsw_ObjectIdentity = ObjectIdentity
hh3c_wx3024lsw = _Hh3c_wx3024lsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 352)
)
_Hh3c_wx5004_ObjectIdentity = ObjectIdentity
hh3c_wx5004 = _Hh3c_wx5004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 353)
)
_Hh3c_sr6604_ObjectIdentity = ObjectIdentity
hh3c_sr6604 = _Hh3c_sr6604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 354)
)
_Hh3c_iag5000_A_ObjectIdentity = ObjectIdentity
hh3c_iag5000_A = _Hh3c_iag5000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 355)
)
_Hh3c_secBlade_SPE_FWM_ObjectIdentity = ObjectIdentity
hh3c_secBlade_SPE_FWM = _Hh3c_secBlade_SPE_FWM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 356)
)
_Hh3c_ICG2200_ObjectIdentity = ObjectIdentity
hh3c_ICG2200 = _Hh3c_ICG2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 357)
)
_Hh3c_S7602_ObjectIdentity = ObjectIdentity
hh3c_S7602 = _Hh3c_S7602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 358)
)
_Hh3c_S7603_ObjectIdentity = ObjectIdentity
hh3c_S7603 = _Hh3c_S7603_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 359)
)
_Hh3c_S7606_ObjectIdentity = ObjectIdentity
hh3c_S7606 = _Hh3c_S7606_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 360)
)
_Hh3c_S7606_V_ObjectIdentity = ObjectIdentity
hh3c_S7606_V = _Hh3c_S7606_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 361)
)
_Hh3c_S7610_ObjectIdentity = ObjectIdentity
hh3c_S7610 = _Hh3c_S7610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 362)
)
_Hh3c_wa2610e_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2610e_agn = _Hh3c_wa2610e_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 363)
)
_Hh3c_wa2620e_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2620e_agn = _Hh3c_wa2620e_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 364)
)
_Hh3c_wa1208e_g_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_g_v5 = _Hh3c_wa1208e_g_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 365)
)
_Hh3c_wa1208e_dg_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_dg_v5 = _Hh3c_wa1208e_dg_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 366)
)
_Hh3c_wa1208e_ag_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_ag_v5 = _Hh3c_wa1208e_ag_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 367)
)
_Hh3c_wa1208e_agp_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_agp_v5 = _Hh3c_wa1208e_agp_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 368)
)
_Hh3c_wa1208e_gp_v5_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_gp_v5 = _Hh3c_wa1208e_gp_v5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 369)
)
_Hh3c_S7503E_S_ObjectIdentity = ObjectIdentity
hh3c_S7503E_S = _Hh3c_S7503E_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 370)
)
_Hh3c_secpathIAG2000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathIAG2000_A = _Hh3c_secpathIAG2000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 371)
)
_Hh3c_secpathT1000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathT1000_A = _Hh3c_secpathT1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 372)
)
_Hh3c_secpathT1000_S_ObjectIdentity = ObjectIdentity
hh3c_secpathT1000_S = _Hh3c_secpathT1000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 373)
)
_Hh3c_secBlade_EWPX1FWA0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_EWPX1FWA0 = _Hh3c_secBlade_EWPX1FWA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 374)
)
_Hh3c_secBlade_LSQ1NSMSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1NSMSC0 = _Hh3c_secBlade_LSQ1NSMSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 375)
)
_Hh3c_secBlade_LSQ1AFDBSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1AFDBSC0 = _Hh3c_secBlade_LSQ1AFDBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 376)
)
_Hh3c_secBlade_LSQ1LBSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1LBSC0 = _Hh3c_secBlade_LSQ1LBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 377)
)
_Hh3c_secBlade_LSB1LB1A0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSB1LB1A0 = _Hh3c_secBlade_LSB1LB1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 378)
)
_Hh3c_neoceanIX1560_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX1560 = _Hh3c_neoceanIX1560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 379)
)
_Hh3c_neoceanEX1500S_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1500S = _Hh3c_neoceanEX1500S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 380)
)
_Hh3c_neoceanEX1520S_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1520S = _Hh3c_neoceanEX1520S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 381)
)
_Hh3c_neoceanEX1540S_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1540S = _Hh3c_neoceanEX1540S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 382)
)
_Hh3c_neoceanEX1560S_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1560S = _Hh3c_neoceanEX1560S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 383)
)
_Hh3c_ET716_ObjectIdentity = ObjectIdentity
hh3c_ET716 = _Hh3c_ET716_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 384)
)
_Hh3c_s3600_2P_OLT_ObjectIdentity = ObjectIdentity
hh3c_s3600_2P_OLT = _Hh3c_s3600_2P_OLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 385)
)
_Hh3c_ER3200_ObjectIdentity = ObjectIdentity
hh3c_ER3200 = _Hh3c_ER3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 386)
)
_Hh3c_ER3100_ObjectIdentity = ObjectIdentity
hh3c_ER3100 = _Hh3c_ER3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 387)
)
_Hh3c_s9505E_ObjectIdentity = ObjectIdentity
hh3c_s9505E = _Hh3c_s9505E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 388)
)
_Hh3c_s9508E_V_ObjectIdentity = ObjectIdentity
hh3c_s9508E_V = _Hh3c_s9508E_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 389)
)
_Hh3c_s9512E_ObjectIdentity = ObjectIdentity
hh3c_s9512E = _Hh3c_s9512E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 390)
)
_Hh3c_s12508_ObjectIdentity = ObjectIdentity
hh3c_s12508 = _Hh3c_s12508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 391)
)
_Hh3c_s12518_ObjectIdentity = ObjectIdentity
hh3c_s12518 = _Hh3c_s12518_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 392)
)
_Hh3c_ET708_ObjectIdentity = ObjectIdentity
hh3c_ET708 = _Hh3c_ET708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 393)
)
_Hh3c_ET724_ObjectIdentity = ObjectIdentity
hh3c_ET724 = _Hh3c_ET724_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 394)
)
_Hh3c_s2008TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s2008TP_EA = _Hh3c_s2008TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 395)
)
_Hh3c_s2016TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s2016TP_EA = _Hh3c_s2016TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 396)
)
_Hh3c_s2403TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s2403TP_EA = _Hh3c_s2403TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 397)
)
_Hh3c_ICG2000_CT_ObjectIdentity = ObjectIdentity
hh3c_ICG2000_CT = _Hh3c_ICG2000_CT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 398)
)
_Hh3c_S3528P_EA_ObjectIdentity = ObjectIdentity
hh3c_S3528P_EA = _Hh3c_S3528P_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 400)
)
_Hh3c_S3552P_EA_ObjectIdentity = ObjectIdentity
hh3c_S3552P_EA = _Hh3c_S3552P_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 401)
)
_Hh3c_S3552F_EA_ObjectIdentity = ObjectIdentity
hh3c_S3552F_EA = _Hh3c_S3552F_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 402)
)
_Hh3c_S3528F_EA_ObjectIdentity = ObjectIdentity
hh3c_S3528F_EA = _Hh3c_S3528F_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 403)
)
_Hh3c_S3528TP_EA_ObjectIdentity = ObjectIdentity
hh3c_S3528TP_EA = _Hh3c_S3528TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 404)
)
_Hh3c_secpathAFD1000_A_ObjectIdentity = ObjectIdentity
hh3c_secpathAFD1000_A = _Hh3c_secpathAFD1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 405)
)
_Hh3c_secpathF100_C_EI_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_C_EI = _Hh3c_secpathF100_C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 406)
)
_Hh3c_ER3260_ObjectIdentity = ObjectIdentity
hh3c_ER3260 = _Hh3c_ER3260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 407)
)
_Hh3c_ICG800_ObjectIdentity = ObjectIdentity
hh3c_ICG800 = _Hh3c_ICG800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 408)
)
_Hh3c_ICG800g_ObjectIdentity = ObjectIdentity
hh3c_ICG800g = _Hh3c_ICG800g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 409)
)
_Hh3c_ICG1000_ObjectIdentity = ObjectIdentity
hh3c_ICG1000 = _Hh3c_ICG1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 410)
)
_Hh3c_ICG1800_ObjectIdentity = ObjectIdentity
hh3c_ICG1800 = _Hh3c_ICG1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 411)
)
_Hh3c_neoceanIX3240E_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3240E = _Hh3c_neoceanIX3240E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 412)
)
_Hh3c_neoceanIX3620E_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3620E = _Hh3c_neoceanIX3620E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 413)
)
_Hh3c_neoceanIX3640E_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3640E = _Hh3c_neoceanIX3640E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 414)
)
_Hh3c_secpathACG8800_S3_ObjectIdentity = ObjectIdentity
hh3c_secpathACG8800_S3 = _Hh3c_secpathACG8800_S3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 415)
)
_Hh3c_secpathT5000_S3_ObjectIdentity = ObjectIdentity
hh3c_secpathT5000_S3 = _Hh3c_secpathT5000_S3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 416)
)
_Hh3c_secpathIAG2000_S_ObjectIdentity = ObjectIdentity
hh3c_secpathIAG2000_S = _Hh3c_secpathIAG2000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 417)
)
_Hh3c_secpathACG8800_S3_NS21S2MSPB0_ObjectIdentity = ObjectIdentity
hh3c_secpathACG8800_S3_NS21S2MSPB0 = _Hh3c_secpathACG8800_S3_NS21S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 418)
)
_Hh3c_secpathT5000_S3_NS11S2MSPB0_ObjectIdentity = ObjectIdentity
hh3c_secpathT5000_S3_NS11S2MSPB0 = _Hh3c_secpathT5000_S3_NS11S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 419)
)
_Hh3c_msr3010_ObjectIdentity = ObjectIdentity
hh3c_msr3010 = _Hh3c_msr3010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 420)
)
_Hh3c_msr3011E_ObjectIdentity = ObjectIdentity
hh3c_msr3011E = _Hh3c_msr3011E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 421)
)
_Hh3c_msr3011F_ObjectIdentity = ObjectIdentity
hh3c_msr3011F = _Hh3c_msr3011F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 422)
)
_Hh3c_secpathT200_A_ObjectIdentity = ObjectIdentity
hh3c_secpathT200_A = _Hh3c_secpathT200_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 423)
)
_Hh3c_secpathT200_M_ObjectIdentity = ObjectIdentity
hh3c_secpathT200_M = _Hh3c_secpathT200_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 424)
)
_Hh3c_secpathF100_C2_ObjectIdentity = ObjectIdentity
hh3c_secpathF100_C2 = _Hh3c_secpathF100_C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 425)
)
_Hh3c_DPtech_FW1000_GE_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_GE = _Hh3c_DPtech_FW1000_GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 426)
)
_Hh3c_DPtech_FW1000_GA_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_GA = _Hh3c_DPtech_FW1000_GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 427)
)
_Hh3c_DPtech_FW1000_GS_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_GS = _Hh3c_DPtech_FW1000_GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 428)
)
_Hh3c_DPtech_FW1000_ME_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_ME = _Hh3c_DPtech_FW1000_ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 429)
)
_Hh3c_DPtech_FW1000_MA_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_MA = _Hh3c_DPtech_FW1000_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 430)
)
_Hh3c_DPtech_FW1000_MM_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_MM = _Hh3c_DPtech_FW1000_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 431)
)
_Hh3c_DPtech_FW1000_MC_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_MC = _Hh3c_DPtech_FW1000_MC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 432)
)
_Hh3c_DPtech_UTM2000_MA_ObjectIdentity = ObjectIdentity
hh3c_DPtech_UTM2000_MA = _Hh3c_DPtech_UTM2000_MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 433)
)
_Hh3c_DPtech_UTM2000_MM_ObjectIdentity = ObjectIdentity
hh3c_DPtech_UTM2000_MM = _Hh3c_DPtech_UTM2000_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 434)
)
_Hh3c_DPtech_UTM2000_MS_ObjectIdentity = ObjectIdentity
hh3c_DPtech_UTM2000_MS = _Hh3c_DPtech_UTM2000_MS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 435)
)
_Hh3c_DPtech_IPS2000_GM_ObjectIdentity = ObjectIdentity
hh3c_DPtech_IPS2000_GM = _Hh3c_DPtech_IPS2000_GM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 436)
)
_Hh3c_DPtech_IPS2000_MM_ObjectIdentity = ObjectIdentity
hh3c_DPtech_IPS2000_MM = _Hh3c_DPtech_IPS2000_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 437)
)
_Hh3c_sr6616_ObjectIdentity = ObjectIdentity
hh3c_sr6616 = _Hh3c_sr6616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 438)
)
_Hh3c_s3620_28TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28TP_EI = _Hh3c_s3620_28TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 439)
)
_Hh3c_s3620_28P_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28P_EI = _Hh3c_s3620_28P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 440)
)
_Hh3c_s3620_52P_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_52P_EI = _Hh3c_s3620_52P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 441)
)
_Hh3c_s3620_28P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28P_PWR_EI = _Hh3c_s3620_28P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 442)
)
_Hh3c_s3620_52P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_52P_PWR_EI = _Hh3c_s3620_52P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 443)
)
_Hh3c_s3620_28F_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28F_EI = _Hh3c_s3620_28F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 444)
)
_Hh3c_s3620_52M_ObjectIdentity = ObjectIdentity
hh3c_s3620_52M = _Hh3c_s3620_52M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 445)
)
_Hh3c_s3620_52M_DC_ObjectIdentity = ObjectIdentity
hh3c_s3620_52M_DC = _Hh3c_s3620_52M_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 446)
)
_Hh3c_s3620_28C_EI_ObjectIdentity = ObjectIdentity
hh3c_s3620_28C_EI = _Hh3c_s3620_28C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 447)
)
_Hh3c_wa2210e_ge_ObjectIdentity = ObjectIdentity
hh3c_wa2210e_ge = _Hh3c_wa2210e_ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 448)
)
_Hh3c_wa2220x_age_ObjectIdentity = ObjectIdentity
hh3c_wa2220x_age = _Hh3c_wa2220x_age_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 449)
)
_Hh3c_wa2210x_ge_ObjectIdentity = ObjectIdentity
hh3c_wa2210x_ge = _Hh3c_wa2210x_ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 450)
)
_Hh3c_wb2320x_age_ObjectIdentity = ObjectIdentity
hh3c_wb2320x_age = _Hh3c_wb2320x_age_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 451)
)
_Hh3c_neoceanEX1540_ObjectIdentity = ObjectIdentity
hh3c_neoceanEX1540 = _Hh3c_neoceanEX1540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 452)
)
_Hh3c_S5810_50S_ObjectIdentity = ObjectIdentity
hh3c_S5810_50S = _Hh3c_S5810_50S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 453)
)
_Hh3c_secBlade_LSQ1IPSSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1IPSSC0 = _Hh3c_secBlade_LSQ1IPSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 454)
)
_Hh3c_secBlade_LSB1IPS1A0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSB1IPS1A0 = _Hh3c_secBlade_LSB1IPS1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 455)
)
_Hh3c_ER5100_ObjectIdentity = ObjectIdentity
hh3c_ER5100 = _Hh3c_ER5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 456)
)
_Hh3c_ER5200_ObjectIdentity = ObjectIdentity
hh3c_ER5200 = _Hh3c_ER5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 457)
)
_Hh3c_wx3010wcm_ObjectIdentity = ObjectIdentity
hh3c_wx3010wcm = _Hh3c_wx3010wcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 458)
)
_Hh3c_wx3010lsw_ObjectIdentity = ObjectIdentity
hh3c_wx3010lsw = _Hh3c_wx3010lsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 459)
)
_Hh3c_cc652E_ObjectIdentity = ObjectIdentity
hh3c_cc652E = _Hh3c_cc652E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 460)
)
_Hh3c_S5120_20P_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_20P_SI = _Hh3c_S5120_20P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 461)
)
_Hh3c_S5120_28P_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_SI = _Hh3c_S5120_28P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 462)
)
_Hh3c_S5120_52P_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52P_SI = _Hh3c_S5120_52P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 463)
)
_Hh3c_S5120_28P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_EI = _Hh3c_S5120_28P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 464)
)
_Hh3c_S5120_52P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52P_EI = _Hh3c_S5120_52P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 465)
)
_Hh3c_S5120_28P_LPWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_LPWR_EI = _Hh3c_S5120_28P_LPWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 466)
)
_Hh3c_S5120_28P_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_PWR_EI = _Hh3c_S5120_28P_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 467)
)
_Hh3c_wx6100LSR_ObjectIdentity = ObjectIdentity
hh3c_wx6100LSR = _Hh3c_wx6100LSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 468)
)
_Hh3c_s7506E_S_ObjectIdentity = ObjectIdentity
hh3c_s7506E_S = _Hh3c_s7506E_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 469)
)
_Hh3c_ICG2000B_ObjectIdentity = ObjectIdentity
hh3c_ICG2000B = _Hh3c_ICG2000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 470)
)
_Hh3c_ICG2000C_ObjectIdentity = ObjectIdentity
hh3c_ICG2000C = _Hh3c_ICG2000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 471)
)
_Hh3c_S1626_ObjectIdentity = ObjectIdentity
hh3c_S1626 = _Hh3c_S1626_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 472)
)
_Hh3c_S1650_ObjectIdentity = ObjectIdentity
hh3c_S1650 = _Hh3c_S1650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 473)
)
_Hh3c_S1626P_ObjectIdentity = ObjectIdentity
hh3c_S1626P = _Hh3c_S1626P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 474)
)
_Hh3c_neoceanIX3620S_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3620S = _Hh3c_neoceanIX3620S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 475)
)
_Hh3c_neoceanIX3080S_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX3080S = _Hh3c_neoceanIX3080S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 476)
)
_Hh3c_ER3280g_ObjectIdentity = ObjectIdentity
hh3c_ER3280g = _Hh3c_ER3280g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 477)
)
_Hh3c_wa2610_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2610_agn = _Hh3c_wa2610_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 478)
)
_Hh3c_wa2612_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2612_agn = _Hh3c_wa2612_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 479)
)
_Hh3c_secpathT200_S_ObjectIdentity = ObjectIdentity
hh3c_secpathT200_S = _Hh3c_secpathT200_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 480)
)
_Hh3c_secpathU200_CS_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_CS = _Hh3c_secpathU200_CS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 481)
)
_Hh3c_secpathU200_CM_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_CM = _Hh3c_secpathU200_CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 482)
)
_Hh3c_secpathU200_CA_ObjectIdentity = ObjectIdentity
hh3c_secpathU200_CA = _Hh3c_secpathU200_CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 483)
)
_Hh3c_secBlade_LSR1AFC2A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1AFC2A1 = _Hh3c_secBlade_LSR1AFC2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 484)
)
_Hh3c_secBlade_LSR1FW2A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1FW2A1 = _Hh3c_secBlade_LSR1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 485)
)
_Hh3c_secBlade_LSR1LB1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1LB1A1 = _Hh3c_secBlade_LSR1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 486)
)
_Hh3c_secBlade_LSR1NSM1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1NSM1A1 = _Hh3c_secBlade_LSR1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 487)
)
_Hh3c_cc650E_ObjectIdentity = ObjectIdentity
hh3c_cc650E = _Hh3c_cc650E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 488)
)
_Hh3c_LSWM1WCM10_ObjectIdentity = ObjectIdentity
hh3c_LSWM1WCM10 = _Hh3c_LSWM1WCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 489)
)
_Hh3c_LSWM1WCM20_ObjectIdentity = ObjectIdentity
hh3c_LSWM1WCM20 = _Hh3c_LSWM1WCM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 490)
)
_Hh3c_EWPXM1WCMC0_ObjectIdentity = ObjectIdentity
hh3c_EWPXM1WCMC0 = _Hh3c_EWPXM1WCMC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 491)
)
_Hh3c_LSWM1IPS10_ObjectIdentity = ObjectIdentity
hh3c_LSWM1IPS10 = _Hh3c_LSWM1IPS10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 492)
)
_Hh3c_LSWM1FW10_ObjectIdentity = ObjectIdentity
hh3c_LSWM1FW10 = _Hh3c_LSWM1FW10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 493)
)
_Hh3c_secpathF1000_S_EI_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_S_EI = _Hh3c_secpathF1000_S_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 494)
)
_Hh3c_secpathF1000_A_EI_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_A_EI = _Hh3c_secpathF1000_A_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 495)
)
_Hh3c_msr50_06_V5_ObjectIdentity = ObjectIdentity
hh3c_msr50_06_V5 = _Hh3c_msr50_06_V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 496)
)
_Hh3c_secBlade_LSR1ACG1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1ACG1A1 = _Hh3c_secBlade_LSR1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 497)
)
_Hh3c_secBlade_LSR1IPS1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSR1IPS1A1 = _Hh3c_secBlade_LSR1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 498)
)
_Hh3c_S7602_S_ObjectIdentity = ObjectIdentity
hh3c_S7602_S = _Hh3c_S7602_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 499)
)
_Hh3c_S7603_S_ObjectIdentity = ObjectIdentity
hh3c_S7603_S = _Hh3c_S7603_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 500)
)
_Hh3c_S7606_S_ObjectIdentity = ObjectIdentity
hh3c_S7606_S = _Hh3c_S7606_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 501)
)
_Hh3c_SSM_s5500G_ObjectIdentity = ObjectIdentity
hh3c_SSM_s5500G = _Hh3c_SSM_s5500G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 502)
)
_Hh3c_SSM_FIC_ObjectIdentity = ObjectIdentity
hh3c_SSM_FIC = _Hh3c_SSM_FIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 503)
)
_Hh3c_SSM_MIM_ObjectIdentity = ObjectIdentity
hh3c_SSM_MIM = _Hh3c_SSM_MIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 504)
)
_Hh3c_ER8300_ObjectIdentity = ObjectIdentity
hh3c_ER8300 = _Hh3c_ER8300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 505)
)
_Hh3c_wa2610x_gnp_ObjectIdentity = ObjectIdentity
hh3c_wa2610x_gnp = _Hh3c_wa2610x_gnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 506)
)
_Hh3c_wb2360x_anp_ObjectIdentity = ObjectIdentity
hh3c_wb2360x_anp = _Hh3c_wb2360x_anp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 507)
)
_Hh3c_wh2530x_dag_ObjectIdentity = ObjectIdentity
hh3c_wh2530x_dag = _Hh3c_wh2530x_dag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 508)
)
_Hh3c_wa2620_agn_ObjectIdentity = ObjectIdentity
hh3c_wa2620_agn = _Hh3c_wa2620_agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 509)
)
_Hh3c_cc610E_ObjectIdentity = ObjectIdentity
hh3c_cc610E = _Hh3c_cc610E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 510)
)
_Hh3c_DPtech_FW1000_GT_ObjectIdentity = ObjectIdentity
hh3c_DPtech_FW1000_GT = _Hh3c_DPtech_FW1000_GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 511)
)
_Hh3c_s2008TP_EA_SI_ObjectIdentity = ObjectIdentity
hh3c_s2008TP_EA_SI = _Hh3c_s2008TP_EA_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 512)
)
_Hh3c_s2016TP_EA_SI_ObjectIdentity = ObjectIdentity
hh3c_s2016TP_EA_SI = _Hh3c_s2016TP_EA_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 513)
)
_Hh3c_s2403TP_EA_SI_ObjectIdentity = ObjectIdentity
hh3c_s2403TP_EA_SI = _Hh3c_s2403TP_EA_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 514)
)
_Hh3c_S5120_24P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_24P_EI = _Hh3c_S5120_24P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 515)
)
_Hh3c_S5120_48P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_48P_EI = _Hh3c_S5120_48P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 516)
)
_Hh3c_S5120_28C_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28C_EI = _Hh3c_S5120_28C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 517)
)
_Hh3c_S5120_52C_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52C_EI = _Hh3c_S5120_52C_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 518)
)
_Hh3c_S5120_28C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28C_PWR_EI = _Hh3c_S5120_28C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 519)
)
_Hh3c_S5120_52C_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52C_PWR_EI = _Hh3c_S5120_52C_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 520)
)
_Hh3c_wx3008wcm_ObjectIdentity = ObjectIdentity
hh3c_wx3008wcm = _Hh3c_wx3008wcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 521)
)
_Hh3c_wx3008lsw_ObjectIdentity = ObjectIdentity
hh3c_wx3008lsw = _Hh3c_wx3008lsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 522)
)
_Hh3c_msr900_ObjectIdentity = ObjectIdentity
hh3c_msr900 = _Hh3c_msr900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 523)
)
_Hh3c_msr920_ObjectIdentity = ObjectIdentity
hh3c_msr920 = _Hh3c_msr920_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 524)
)
_Hh3c_secBlade_LSQ1IAGSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LSQ1IAGSC0 = _Hh3c_secBlade_LSQ1IAGSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 525)
)
_Hh3c_WX7306_ObjectIdentity = ObjectIdentity
hh3c_WX7306 = _Hh3c_WX7306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 526)
)
_Hh3c_WX7310_ObjectIdentity = ObjectIdentity
hh3c_WX7310 = _Hh3c_WX7310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 527)
)
_Hh3c_Blade5310_ObjectIdentity = ObjectIdentity
hh3c_Blade5310 = _Hh3c_Blade5310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 528)
)
_Hh3c_Blade55102_ObjectIdentity = ObjectIdentity
hh3c_Blade55102 = _Hh3c_Blade55102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 529)
)
_Hh3c_Blade5512S_ObjectIdentity = ObjectIdentity
hh3c_Blade5512S = _Hh3c_Blade5512S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 530)
)
_Hh3c_Blade55110X_ObjectIdentity = ObjectIdentity
hh3c_Blade55110X = _Hh3c_Blade55110X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 531)
)
_Hh3c_wa2610e_gnp_ObjectIdentity = ObjectIdentity
hh3c_wa2610e_gnp = _Hh3c_wa2610e_gnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 532)
)
_Hh3c_s3100_26TP_SI_UM_ObjectIdentity = ObjectIdentity
hh3c_s3100_26TP_SI_UM = _Hh3c_s3100_26TP_SI_UM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 533)
)
_Hh3c_s3100_52TP_SI_UM_ObjectIdentity = ObjectIdentity
hh3c_s3100_52TP_SI_UM = _Hh3c_s3100_52TP_SI_UM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 534)
)
_Hh3c_s5500_24P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_24P_SI = _Hh3c_s5500_24P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 535)
)
_Hh3c_s5500_48P_SI_ObjectIdentity = ObjectIdentity
hh3c_s5500_48P_SI = _Hh3c_s5500_48P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 536)
)
_Hh3c_ME8000_ObjectIdentity = ObjectIdentity
hh3c_ME8000 = _Hh3c_ME8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 537)
)
_Hh3c_ME8600_ObjectIdentity = ObjectIdentity
hh3c_ME8600 = _Hh3c_ME8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 538)
)
_Hh3c_ME5000_ObjectIdentity = ObjectIdentity
hh3c_ME5000 = _Hh3c_ME5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 539)
)
_Hh3c_MG6060_ObjectIdentity = ObjectIdentity
hh3c_MG6060 = _Hh3c_MG6060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 540)
)
_Hh3c_MG6050_ObjectIdentity = ObjectIdentity
hh3c_MG6050 = _Hh3c_MG6050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 541)
)
_Hh3c_MG6050S_ObjectIdentity = ObjectIdentity
hh3c_MG6050S = _Hh3c_MG6050S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 542)
)
_Hh3c_MG9010_ObjectIdentity = ObjectIdentity
hh3c_MG9010 = _Hh3c_MG9010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 543)
)
_Hh3c_MG9030_ObjectIdentity = ObjectIdentity
hh3c_MG9030 = _Hh3c_MG9030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 544)
)
_Hh3c_MG9060_ObjectIdentity = ObjectIdentity
hh3c_MG9060 = _Hh3c_MG9060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 545)
)
_Hh3c_neoceanVX1500_DC_ObjectIdentity = ObjectIdentity
hh3c_neoceanVX1500_DC = _Hh3c_neoceanVX1500_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 546)
)
_Hh3c_cc620E_ObjectIdentity = ObjectIdentity
hh3c_cc620E = _Hh3c_cc620E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 547)
)
_Hh3c_SIVX_S3628_ObjectIdentity = ObjectIdentity
hh3c_SIVX_S3628 = _Hh3c_SIVX_S3628_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 548)
)
_Hh3c_SIVX_S5528_ObjectIdentity = ObjectIdentity
hh3c_SIVX_S5528 = _Hh3c_SIVX_S5528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 549)
)
_Hh3c_SIVX_VS1500_ObjectIdentity = ObjectIdentity
hh3c_SIVX_VS1500 = _Hh3c_SIVX_VS1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 550)
)
_Hh3c_neoceanIX2540_ObjectIdentity = ObjectIdentity
hh3c_neoceanIX2540 = _Hh3c_neoceanIX2540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 551)
)
_Hh3c_neoceanVX2500_ObjectIdentity = ObjectIdentity
hh3c_neoceanVX2500 = _Hh3c_neoceanVX2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 552)
)
_Hh3c_S5120_28P_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_PWR_SI = _Hh3c_S5120_28P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 555)
)
_Hh3c_S5120_28P_HPWR_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_HPWR_SI = _Hh3c_S5120_28P_HPWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 556)
)
_Hh3c_F1000_E_DC_ObjectIdentity = ObjectIdentity
hh3c_F1000_E_DC = _Hh3c_F1000_E_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 557)
)
_Hh3c_S5028_ObjectIdentity = ObjectIdentity
hh3c_S5028 = _Hh3c_S5028_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 558)
)
_Hh3c_ET824_ObjectIdentity = ObjectIdentity
hh3c_ET824 = _Hh3c_ET824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 559)
)
_Hh3c_OSM_ObjectIdentity = ObjectIdentity
hh3c_OSM = _Hh3c_OSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 560)
)
_Hh3c_wx5002_v2_ObjectIdentity = ObjectIdentity
hh3c_wx5002_v2 = _Hh3c_wx5002_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 561)
)
_Hh3c_wx5004_v2_ObjectIdentity = ObjectIdentity
hh3c_wx5004_v2 = _Hh3c_wx5004_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 562)
)
_Hh3c_secpathT1000_C_ObjectIdentity = ObjectIdentity
hh3c_secpathT1000_C = _Hh3c_secpathT1000_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 563)
)
_Hh3c_secBlade_LST1IPS1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1IPS1A1 = _Hh3c_secBlade_LST1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 564)
)
_Hh3c_secBlade_LST1FW2A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1FW2A1 = _Hh3c_secBlade_LST1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 565)
)
_Hh3c_secBlade_LST1LB1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1LB1A1 = _Hh3c_secBlade_LST1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 566)
)
_Hh3c_secBlade_LST1NSM1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1NSM1A1 = _Hh3c_secBlade_LST1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 567)
)
_Hh3c_secBlade_EWPX2IAGSC0_ObjectIdentity = ObjectIdentity
hh3c_secBlade_EWPX2IAGSC0 = _Hh3c_secBlade_EWPX2IAGSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 568)
)
_Hh3c_F1000_A_EI_ObjectIdentity = ObjectIdentity
hh3c_F1000_A_EI = _Hh3c_F1000_A_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 569)
)
_Hh3c_wx6108E_ObjectIdentity = ObjectIdentity
hh3c_wx6108E = _Hh3c_wx6108E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 570)
)
_Hh3c_wx6112E_ObjectIdentity = ObjectIdentity
hh3c_wx6112E = _Hh3c_wx6112E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 571)
)
_Hh3c_s5500_34C_HI_ObjectIdentity = ObjectIdentity
hh3c_s5500_34C_HI = _Hh3c_s5500_34C_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 572)
)
_Hh3c_s5500_58C_HI_ObjectIdentity = ObjectIdentity
hh3c_s5500_58C_HI = _Hh3c_s5500_58C_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 573)
)
_Hh3c_wa1208e_gp_h20_ObjectIdentity = ObjectIdentity
hh3c_wa1208e_gp_h20 = _Hh3c_wa1208e_gp_h20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 574)
)
_Hh3c_S5120_9P_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_9P_SI = _Hh3c_S5120_9P_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 575)
)
_Hh3c_S5120_9P_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_9P_PWR_SI = _Hh3c_S5120_9P_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 576)
)
_Hh3c_S5120_9P_HPWR_SI_ObjectIdentity = ObjectIdentity
hh3c_S5120_9P_HPWR_SI = _Hh3c_S5120_9P_HPWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 577)
)
_Hh3c_e528_ObjectIdentity = ObjectIdentity
hh3c_e528 = _Hh3c_e528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 578)
)
_Hh3c_e552_ObjectIdentity = ObjectIdentity
hh3c_e552 = _Hh3c_e552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 579)
)
_Hh3c_s3600V2_28TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28TP_EI = _Hh3c_s3600V2_28TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 580)
)
_Hh3c_s3600V2_52TP_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_52TP_EI = _Hh3c_s3600V2_52TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 581)
)
_Hh3c_s3600V2_28TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28TP_PWR_EI = _Hh3c_s3600V2_28TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 582)
)
_Hh3c_s3600V2_52TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_52TP_PWR_EI = _Hh3c_s3600V2_52TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 583)
)
_Hh3c_s3600V2_28F_EI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28F_EI = _Hh3c_s3600V2_28F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 584)
)
_Hh3c_s3600V2_28TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28TP_SI = _Hh3c_s3600V2_28TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 585)
)
_Hh3c_s3600V2_52TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_52TP_SI = _Hh3c_s3600V2_52TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 586)
)
_Hh3c_s3600V2_28TP_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_28TP_PWR_SI = _Hh3c_s3600V2_28TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 587)
)
_Hh3c_s3600V2_52TP_PWR_SI_ObjectIdentity = ObjectIdentity
hh3c_s3600V2_52TP_PWR_SI = _Hh3c_s3600V2_52TP_PWR_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 588)
)
_Hh3c_s3500V2_28TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_28TP_EA = _Hh3c_s3500V2_28TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 589)
)
_Hh3c_s3500V2_52TP_EA_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_52TP_EA = _Hh3c_s3500V2_52TP_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 590)
)
_Hh3c_s3500V2_28F_EA_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_28F_EA = _Hh3c_s3500V2_28F_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 591)
)
_Hh3c_s3500V2_28TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_28TP_SI = _Hh3c_s3500V2_28TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 592)
)
_Hh3c_s3500V2_52TP_SI_ObjectIdentity = ObjectIdentity
hh3c_s3500V2_52TP_SI = _Hh3c_s3500V2_52TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 593)
)
_Hh3c_s9508E_ObjectIdentity = ObjectIdentity
hh3c_s9508E = _Hh3c_s9508E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 594)
)
_Hh3c_s12504_ObjectIdentity = ObjectIdentity
hh3c_s12504 = _Hh3c_s12504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 595)
)
_Hh3c_ICG2000B_GT_ObjectIdentity = ObjectIdentity
hh3c_ICG2000B_GT = _Hh3c_ICG2000B_GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 596)
)
_Hh3c_ICG3000B_ObjectIdentity = ObjectIdentity
hh3c_ICG3000B = _Hh3c_ICG3000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 597)
)
_Hh3c_ICG3000S_ObjectIdentity = ObjectIdentity
hh3c_ICG3000S = _Hh3c_ICG3000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 598)
)
_Hh3c_ICG5000B_ObjectIdentity = ObjectIdentity
hh3c_ICG5000B = _Hh3c_ICG5000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 599)
)
_Hh3c_wh2640X_agnp_ObjectIdentity = ObjectIdentity
hh3c_wh2640X_agnp = _Hh3c_wh2640X_agnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 600)
)
_Hh3c_wa2620X_agnp_ObjectIdentity = ObjectIdentity
hh3c_wa2620X_agnp = _Hh3c_wa2620X_agnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 601)
)
_Hh3c_s3100_16TP_PWR_EI_F_ObjectIdentity = ObjectIdentity
hh3c_s3100_16TP_PWR_EI_F = _Hh3c_s3100_16TP_PWR_EI_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 602)
)
_Hh3c_cr16018_ObjectIdentity = ObjectIdentity
hh3c_cr16018 = _Hh3c_cr16018_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 603)
)
_Hh3c_cr16008_ObjectIdentity = ObjectIdentity
hh3c_cr16008 = _Hh3c_cr16008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 604)
)
_Hh3c_cr16004_ObjectIdentity = ObjectIdentity
hh3c_cr16004 = _Hh3c_cr16004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 605)
)
_Hh3c_F1000_A_SI_ObjectIdentity = ObjectIdentity
hh3c_F1000_A_SI = _Hh3c_F1000_A_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 606)
)
_Hh3c_F1000_E_SI_ObjectIdentity = ObjectIdentity
hh3c_F1000_E_SI = _Hh3c_F1000_E_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 607)
)
_Hh3c_secBlade_LST1ACG1A1_ObjectIdentity = ObjectIdentity
hh3c_secBlade_LST1ACG1A1 = _Hh3c_secBlade_LST1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 608)
)
_Hh3c_secBlade_SPE_IPS_ObjectIdentity = ObjectIdentity
hh3c_secBlade_SPE_IPS = _Hh3c_secBlade_SPE_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 609)
)
_Hh3c_secBlade_SPE_ACG_ObjectIdentity = ObjectIdentity
hh3c_secBlade_SPE_ACG = _Hh3c_secBlade_SPE_ACG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 610)
)
_Hh3c_wx6103_ObjectIdentity = ObjectIdentity
hh3c_wx6103 = _Hh3c_wx6103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 611)
)
_Hh3c_LSQ1WCMD0_ObjectIdentity = ObjectIdentity
hh3c_LSQ1WCMD0 = _Hh3c_LSQ1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 612)
)
_Hh3c_EWPX2WCMD0_ObjectIdentity = ObjectIdentity
hh3c_EWPX2WCMD0 = _Hh3c_EWPX2WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 613)
)
_Hh3c_LSR1WCM3A1_ObjectIdentity = ObjectIdentity
hh3c_LSR1WCM3A1 = _Hh3c_LSR1WCM3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 614)
)
_Hh3c_S5830_52SC_ObjectIdentity = ObjectIdentity
hh3c_S5830_52SC = _Hh3c_S5830_52SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 615)
)
_Hh3c_S5830_106S_ObjectIdentity = ObjectIdentity
hh3c_S5830_106S = _Hh3c_S5830_106S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 617)
)
_Hh3c_ET814_ObjectIdentity = ObjectIdentity
hh3c_ET814 = _Hh3c_ET814_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 618)
)
_Hh3c_S5120_28P_LI_ObjectIdentity = ObjectIdentity
hh3c_S5120_28P_LI = _Hh3c_S5120_28P_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 619)
)
_Hh3c_S5120_52P_LI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52P_LI = _Hh3c_S5120_52P_LI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 620)
)
_Hh3c_secBlade_IM_FW_II_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_FW_II = _Hh3c_secBlade_IM_FW_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 621)
)
_Hh3c_secBlade_IM_LB_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_LB = _Hh3c_secBlade_IM_LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 622)
)
_Hh3c_secBlade_IM_SSL_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_SSL = _Hh3c_secBlade_IM_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 623)
)
_Hh3c_ER2210C_ObjectIdentity = ObjectIdentity
hh3c_ER2210C = _Hh3c_ER2210C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 625)
)
_Hh3c_VCX_Connect_100_ObjectIdentity = ObjectIdentity
hh3c_VCX_Connect_100 = _Hh3c_VCX_Connect_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 626)
)
_Hh3c_VCX_Connect_200_ObjectIdentity = ObjectIdentity
hh3c_VCX_Connect_200 = _Hh3c_VCX_Connect_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 627)
)
_Hh3c_VCX_V7005_ObjectIdentity = ObjectIdentity
hh3c_VCX_V7005 = _Hh3c_VCX_V7005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 628)
)
_Hh3c_VCX_V7205_ObjectIdentity = ObjectIdentity
hh3c_VCX_V7205 = _Hh3c_VCX_V7205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 629)
)
_Hh3c_VCX_MIM_ObjectIdentity = ObjectIdentity
hh3c_VCX_MIM = _Hh3c_VCX_MIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 630)
)
_Hh3c_VCX_Connect_MIM_Primary_ObjectIdentity = ObjectIdentity
hh3c_VCX_Connect_MIM_Primary = _Hh3c_VCX_Connect_MIM_Primary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 631)
)
_Hh3c_VCX_Connect_MIM_Secondary_ObjectIdentity = ObjectIdentity
hh3c_VCX_Connect_MIM_Secondary = _Hh3c_VCX_Connect_MIM_Secondary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 632)
)
_Hh3c_VCX_V7310_ObjectIdentity = ObjectIdentity
hh3c_VCX_V7310 = _Hh3c_VCX_V7310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 633)
)
_Hh3c_secBlade_IM_IPS_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_IPS = _Hh3c_secBlade_IM_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 634)
)
_Hh3c_secBlade_IM_ACG_ObjectIdentity = ObjectIdentity
hh3c_secBlade_IM_ACG = _Hh3c_secBlade_IM_ACG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 635)
)
_Hh3c_s7508E_X_ObjectIdentity = ObjectIdentity
hh3c_s7508E_X = _Hh3c_s7508E_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 636)
)
_Hh3c_s10504_ObjectIdentity = ObjectIdentity
hh3c_s10504 = _Hh3c_s10504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 637)
)
_Hh3c_s10508_ObjectIdentity = ObjectIdentity
hh3c_s10508 = _Hh3c_s10508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 638)
)
_Hh3c_s10508_V_ObjectIdentity = ObjectIdentity
hh3c_s10508_V = _Hh3c_s10508_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 639)
)
_Hh3c_secBlade_SPE_FWM_200_ObjectIdentity = ObjectIdentity
hh3c_secBlade_SPE_FWM_200 = _Hh3c_secBlade_SPE_FWM_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 640)
)
_Hh3c_secpathF1000_S_AI_ObjectIdentity = ObjectIdentity
hh3c_secpathF1000_S_AI = _Hh3c_secpathF1000_S_AI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 641)
)
_Hh3c_wx3024e_wcm_ObjectIdentity = ObjectIdentity
hh3c_wx3024e_wcm = _Hh3c_wx3024e_wcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 642)
)
_Hh3c_wx3024e_lsw_ObjectIdentity = ObjectIdentity
hh3c_wx3024e_lsw = _Hh3c_wx3024e_lsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 643)
)
_Hh3c_ER2100_ObjectIdentity = ObjectIdentity
hh3c_ER2100 = _Hh3c_ER2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 644)
)
_Hh3c_S5820X_34TC_ObjectIdentity = ObjectIdentity
hh3c_S5820X_34TC = _Hh3c_S5820X_34TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 645)
)
_Hh3c_S5820X_34SC_ObjectIdentity = ObjectIdentity
hh3c_S5820X_34SC = _Hh3c_S5820X_34SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 646)
)
_Hh3c_S5820X_34C_ObjectIdentity = ObjectIdentity
hh3c_S5820X_34C = _Hh3c_S5820X_34C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 647)
)
_Hh3c_S5820X_64SC_ObjectIdentity = ObjectIdentity
hh3c_S5820X_64SC = _Hh3c_S5820X_64SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 648)
)
_Hh3c_cc720E_ObjectIdentity = ObjectIdentity
hh3c_cc720E = _Hh3c_cc720E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 649)
)
_Hh3c_S2126T_ObjectIdentity = ObjectIdentity
hh3c_S2126T = _Hh3c_S2126T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 650)
)
_Hh3c_S5800_54S_ObjectIdentity = ObjectIdentity
hh3c_S5800_54S = _Hh3c_S5800_54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 651)
)
_Hh3c_S5820X_26S_ObjectIdentity = ObjectIdentity
hh3c_S5820X_26S = _Hh3c_S5820X_26S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 652)
)
_Hh3c_S3100V2_8TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_8TP_SI = _Hh3c_S3100V2_8TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 653)
)
_Hh3c_S3100V2_16TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_16TP_SI = _Hh3c_S3100V2_16TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 654)
)
_Hh3c_S3100V2_26TP_SI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_26TP_SI = _Hh3c_S3100V2_26TP_SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 655)
)
_Hh3c_E126B_ObjectIdentity = ObjectIdentity
hh3c_E126B = _Hh3c_E126B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 656)
)
_Hh3c_S3100V2_8TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_8TP_EI = _Hh3c_S3100V2_8TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 657)
)
_Hh3c_S3100V2_16TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_16TP_EI = _Hh3c_S3100V2_16TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 658)
)
_Hh3c_S3100V2_26TP_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_26TP_EI = _Hh3c_S3100V2_26TP_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 659)
)
_Hh3c_S3100V2_8TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_8TP_PWR_EI = _Hh3c_S3100V2_8TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 660)
)
_Hh3c_S3100V2_16TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_16TP_PWR_EI = _Hh3c_S3100V2_16TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 661)
)
_Hh3c_S3100V2_26TP_PWR_EI_ObjectIdentity = ObjectIdentity
hh3c_S3100V2_26TP_PWR_EI = _Hh3c_S3100V2_26TP_PWR_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 662)
)
_Hh3c_S2008TP_EB_ObjectIdentity = ObjectIdentity
hh3c_S2008TP_EB = _Hh3c_S2008TP_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 663)
)
_Hh3c_S2016TP_EB_ObjectIdentity = ObjectIdentity
hh3c_S2016TP_EB = _Hh3c_S2016TP_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 664)
)
_Hh3c_S2403TP_EB_ObjectIdentity = ObjectIdentity
hh3c_S2403TP_EB = _Hh3c_S2403TP_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 665)
)
_Hh3c_S2008TP_PWR_EB_ObjectIdentity = ObjectIdentity
hh3c_S2008TP_PWR_EB = _Hh3c_S2008TP_PWR_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 666)
)
_Hh3c_S2016TP_PWR_EB_ObjectIdentity = ObjectIdentity
hh3c_S2016TP_PWR_EB = _Hh3c_S2016TP_PWR_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 667)
)
_Hh3c_S2403TP_PWR_EB_ObjectIdentity = ObjectIdentity
hh3c_S2403TP_PWR_EB = _Hh3c_S2403TP_PWR_EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 668)
)
_Hh3c_S5800_LSW1FC4P0_ObjectIdentity = ObjectIdentity
hh3c_S5800_LSW1FC4P0 = _Hh3c_S5800_LSW1FC4P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 669)
)
_Hh3c_S2403TP_EA_SI_D_ObjectIdentity = ObjectIdentity
hh3c_S2403TP_EA_SI_D = _Hh3c_S2403TP_EA_SI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 670)
)
_Hh3c_S3528P_EA_D_ObjectIdentity = ObjectIdentity
hh3c_S3528P_EA_D = _Hh3c_S3528P_EA_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 671)
)
_Hh3c_OAP_FIC_V2_ObjectIdentity = ObjectIdentity
hh3c_OAP_FIC_V2 = _Hh3c_OAP_FIC_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 672)
)
_Hh3c_OAP_MIM_V2_ObjectIdentity = ObjectIdentity
hh3c_OAP_MIM_V2 = _Hh3c_OAP_MIM_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 673)
)
_Hh3c_OAPS_MIM_V2_ObjectIdentity = ObjectIdentity
hh3c_OAPS_MIM_V2 = _Hh3c_OAPS_MIM_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 674)
)
_Hh3c_S2008TP_PWR_EA_ObjectIdentity = ObjectIdentity
hh3c_S2008TP_PWR_EA = _Hh3c_S2008TP_PWR_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 675)
)
_Hh3c_S2008TP_PWR_EA_DC_ObjectIdentity = ObjectIdentity
hh3c_S2008TP_PWR_EA_DC = _Hh3c_S2008TP_PWR_EA_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 676)
)
_Hh3c_S2016TP_PWR_EA_ObjectIdentity = ObjectIdentity
hh3c_S2016TP_PWR_EA = _Hh3c_S2016TP_PWR_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 677)
)
_Hh3c_S2403TP_PWR_EA_ObjectIdentity = ObjectIdentity
hh3c_S2403TP_PWR_EA = _Hh3c_S2403TP_PWR_EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 678)
)
_Hh3c_S5120_24P_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5120_24P_EI_D = _Hh3c_S5120_24P_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 679)
)
_Hh3c_S5120_24P_PWR_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5120_24P_PWR_EI_D = _Hh3c_S5120_24P_PWR_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 680)
)
_Hh3c_S5120_48P_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5120_48P_EI_D = _Hh3c_S5120_48P_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 681)
)
_Hh3c_S5024P_EI_ObjectIdentity = ObjectIdentity
hh3c_S5024P_EI = _Hh3c_S5024P_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 682)
)
_Hh3c_S5500_28C_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5500_28C_EI_D = _Hh3c_S5500_28C_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 683)
)
_Hh3c_S5500_52C_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5500_52C_EI_D = _Hh3c_S5500_52C_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 684)
)
_Hh3c_S5500_28F_EI_D_ObjectIdentity = ObjectIdentity
hh3c_S5500_28F_EI_D = _Hh3c_S5500_28F_EI_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 685)
)
_Hh3c_S5500_28C_EI_DC_D_ObjectIdentity = ObjectIdentity
hh3c_S5500_28C_EI_DC_D = _Hh3c_S5500_28C_EI_DC_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 686)
)
_Hh3c_MG9050_ObjectIdentity = ObjectIdentity
hh3c_MG9050 = _Hh3c_MG9050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 687)
)
_Hh3c_S5120_52SC_HI_ObjectIdentity = ObjectIdentity
hh3c_S5120_52SC_HI = _Hh3c_S5120_52SC_HI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 688)
)
_Hh3c_CE3000_32F_EI_ObjectIdentity = ObjectIdentity
hh3c_CE3000_32F_EI = _Hh3c_CE3000_32F_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 689)
)
_Hh3cS5830V224S_ObjectIdentity = ObjectIdentity
hh3cS5830V224S = _Hh3cS5830V224S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 690)
)
_Hh3cDC1801FH_ObjectIdentity = ObjectIdentity
hh3cDC1801FH = _Hh3cDC1801FH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 691)
)
_Hh3cDC2004FF_ObjectIdentity = ObjectIdentity
hh3cDC2004FF = _Hh3cDC2004FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 692)
)
_Hh3cEC1101HF_ObjectIdentity = ObjectIdentity
hh3cEC1101HF = _Hh3cEC1101HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 693)
)
_Hh3cEC1102HF_ObjectIdentity = ObjectIdentity
hh3cEC1102HF = _Hh3cEC1102HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 694)
)
_Hh3cEC1501HF_ObjectIdentity = ObjectIdentity
hh3cEC1501HF = _Hh3cEC1501HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 695)
)
_Hh3cEC1801HH_ObjectIdentity = ObjectIdentity
hh3cEC1801HH = _Hh3cEC1801HH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 696)
)
_Hh3cEC2516HF_ObjectIdentity = ObjectIdentity
hh3cEC2516HF = _Hh3cEC2516HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 697)
)
_Hh3cEC2016HC_ObjectIdentity = ObjectIdentity
hh3cEC2016HC = _Hh3cEC2016HC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 698)
)
_Hh3cEC2016HC8CH_ObjectIdentity = ObjectIdentity
hh3cEC2016HC8CH = _Hh3cEC2016HC8CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 699)
)
_Hh3cEC2016HC4CH_ObjectIdentity = ObjectIdentity
hh3cEC2016HC4CH = _Hh3cEC2016HC4CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 700)
)
_Hh3cEC1504HF_ObjectIdentity = ObjectIdentity
hh3cEC1504HF = _Hh3cEC1504HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 701)
)
_Hh3cHIC5421_ObjectIdentity = ObjectIdentity
hh3cHIC5421 = _Hh3cHIC5421_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 702)
)
_Hh3cHIC5401_ObjectIdentity = ObjectIdentity
hh3cHIC5401 = _Hh3cHIC5401_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 703)
)
_Hh3cHIC5221H_ObjectIdentity = ObjectIdentity
hh3cHIC5221H = _Hh3cHIC5221H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 704)
)
_Hh3cHIC5201H_ObjectIdentity = ObjectIdentity
hh3cHIC5201H = _Hh3cHIC5201H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 705)
)
_Hh3cVM8500_ObjectIdentity = ObjectIdentity
hh3cVM8500 = _Hh3cVM8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 706)
)
_Hh3cMS8500_ObjectIdentity = ObjectIdentity
hh3cMS8500 = _Hh3cMS8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 707)
)
_Hh3cDM8500_ObjectIdentity = ObjectIdentity
hh3cDM8500 = _Hh3cDM8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 708)
)
_Hh3cVX500_ObjectIdentity = ObjectIdentity
hh3cVX500 = _Hh3cVX500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 709)
)
_Hh3cISC3000E_ObjectIdentity = ObjectIdentity
hh3cISC3000E = _Hh3cISC3000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 710)
)
_Hh3cISC3000S_ObjectIdentity = ObjectIdentity
hh3cISC3000S = _Hh3cISC3000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 711)
)
_Hh3cCC700E_ObjectIdentity = ObjectIdentity
hh3cCC700E = _Hh3cCC700E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 712)
)
_Hh3cDC1001FF_ObjectIdentity = ObjectIdentity
hh3cDC1001FF = _Hh3cDC1001FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 713)
)
_Hh3cECR3316HC_ObjectIdentity = ObjectIdentity
hh3cECR3316HC = _Hh3cECR3316HC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 714)
)
_Hh3cECR3308HD_ObjectIdentity = ObjectIdentity
hh3cECR3308HD = _Hh3cECR3308HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 715)
)
_Hh3cECR3316HC8CH_ObjectIdentity = ObjectIdentity
hh3cECR3316HC8CH = _Hh3cECR3316HC8CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 716)
)
_Hh3cECR3316HC4CH_ObjectIdentity = ObjectIdentity
hh3cECR3316HC4CH = _Hh3cECR3316HC4CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 717)
)
_Hh3cECR3308HD4CH_ObjectIdentity = ObjectIdentity
hh3cECR3308HD4CH = _Hh3cECR3308HD4CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 718)
)
_Hh3cHIC65017L_ObjectIdentity = ObjectIdentity
hh3cHIC65017L = _Hh3cHIC65017L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 719)
)
_Hh3cEC2508HF_ObjectIdentity = ObjectIdentity
hh3cEC2508HF = _Hh3cEC2508HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 720)
)
_Hh3cS3528EA_ObjectIdentity = ObjectIdentity
hh3cS3528EA = _Hh3cS3528EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 721)
)
_Hh3cS3552TPEA_ObjectIdentity = ObjectIdentity
hh3cS3552TPEA = _Hh3cS3552TPEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 722)
)
_Hh3cWP3024_ObjectIdentity = ObjectIdentity
hh3cWP3024 = _Hh3cWP3024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 723)
)
_Hh3cWP3048_ObjectIdentity = ObjectIdentity
hh3cWP3048 = _Hh3cWP3048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 724)
)
_Hh3cS3528FPEA_ObjectIdentity = ObjectIdentity
hh3cS3528FPEA = _Hh3cS3528FPEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 725)
)
_Hh3cE328B_ObjectIdentity = ObjectIdentity
hh3cE328B = _Hh3cE328B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 726)
)
_Hh3cE352B_ObjectIdentity = ObjectIdentity
hh3cE352B = _Hh3cE352B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 727)
)
_Hh3cE152B_ObjectIdentity = ObjectIdentity
hh3cE152B = _Hh3cE152B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 728)
)
_Hh3cS3100V252TP_ObjectIdentity = ObjectIdentity
hh3cS3100V252TP = _Hh3cS3100V252TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 729)
)
_Hh3cWP2008_ObjectIdentity = ObjectIdentity
hh3cWP2008 = _Hh3cWP2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 730)
)
_Hh3cWP2016_ObjectIdentity = ObjectIdentity
hh3cWP2016 = _Hh3cWP2016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 731)
)
_Hh3cWP2024_ObjectIdentity = ObjectIdentity
hh3cWP2024 = _Hh3cWP2024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 732)
)
_Hh3cWP5024_ObjectIdentity = ObjectIdentity
hh3cWP5024 = _Hh3cWP5024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 733)
)
_Hh3cWP5048_ObjectIdentity = ObjectIdentity
hh3cWP5048 = _Hh3cWP5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 734)
)
_Hh3cS2052TPEA_ObjectIdentity = ObjectIdentity
hh3cS2052TPEA = _Hh3cS2052TPEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 735)
)
_Hh3cS7604X_ObjectIdentity = ObjectIdentity
hh3cS7604X = _Hh3cS7604X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 736)
)
_Hh3cS7608X_ObjectIdentity = ObjectIdentity
hh3cS7608X = _Hh3cS7608X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 737)
)
_Hh3cS7608XV_ObjectIdentity = ObjectIdentity
hh3cS7608XV = _Hh3cS7608XV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 738)
)
_Hh3cWA3620iAGN_ObjectIdentity = ObjectIdentity
hh3cWA3620iAGN = _Hh3cWA3620iAGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 739)
)
_Hh3cWA3628iAGN_ObjectIdentity = ObjectIdentity
hh3cWA3628iAGN = _Hh3cWA3628iAGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 740)
)
_Hh3cWA3610iGN_ObjectIdentity = ObjectIdentity
hh3cWA3610iGN = _Hh3cWA3610iGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 741)
)
_Hh3cCC750E_ObjectIdentity = ObjectIdentity
hh3cCC750E = _Hh3cCC750E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 742)
)
_Hh3cS5024FSI_ObjectIdentity = ObjectIdentity
hh3cS5024FSI = _Hh3cS5024FSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 743)
)
_Hh3cS5820V252QF_ObjectIdentity = ObjectIdentity
hh3cS5820V252QF = _Hh3cS5820V252QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 744)
)
_Hh3cWA2110GN_ObjectIdentity = ObjectIdentity
hh3cWA2110GN = _Hh3cWA2110GN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 745)
)
_Hh3cMSR2010E_ObjectIdentity = ObjectIdentity
hh3cMSR2010E = _Hh3cMSR2010E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 746)
)
_Hh3cS10512_ObjectIdentity = ObjectIdentity
hh3cS10512 = _Hh3cS10512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 747)
)
_Hh3cS512028SCHI_ObjectIdentity = ObjectIdentity
hh3cS512028SCHI = _Hh3cS512028SCHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 748)
)
_Hh3cWA1208EGNP_ObjectIdentity = ObjectIdentity
hh3cWA1208EGNP = _Hh3cWA1208EGNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 749)
)
_Hh3cWA2610EGNPH20_ObjectIdentity = ObjectIdentity
hh3cWA2610EGNPH20 = _Hh3cWA2610EGNPH20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 750)
)
_Hh3cWA2620iAGN_ObjectIdentity = ObjectIdentity
hh3cWA2620iAGN = _Hh3cWA2620iAGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 751)
)
_Hh3cWA2610iGN_ObjectIdentity = ObjectIdentity
hh3cWA2610iGN = _Hh3cWA2610iGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 752)
)
_Hh3cWA2612_ObjectIdentity = ObjectIdentity
hh3cWA2612 = _Hh3cWA2612_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 753)
)
_Hh3cWA2620_ObjectIdentity = ObjectIdentity
hh3cWA2620 = _Hh3cWA2620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 754)
)
_Hh3cWB524_ObjectIdentity = ObjectIdentity
hh3cWB524 = _Hh3cWB524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 755)
)
_Hh3cSecBladeLST1FW3A1_ObjectIdentity = ObjectIdentity
hh3cSecBladeLST1FW3A1 = _Hh3cSecBladeLST1FW3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 756)
)
_Hh3cSecBladeLSU1FWCEA0_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSU1FWCEA0 = _Hh3cSecBladeLSU1FWCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 757)
)
_Hh3cWX3010eWCM_ObjectIdentity = ObjectIdentity
hh3cWX3010eWCM = _Hh3cWX3010eWCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 758)
)
_Hh3cWX3010eLSW_ObjectIdentity = ObjectIdentity
hh3cWX3010eLSW = _Hh3cWX3010eLSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 759)
)
_Hh3cSR6602X1_ObjectIdentity = ObjectIdentity
hh3cSR6602X1 = _Hh3cSR6602X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 760)
)
_Hh3cSR6602X2_ObjectIdentity = ObjectIdentity
hh3cSR6602X2 = _Hh3cSR6602X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 761)
)
_Hh3cSecBladeCRIMNAM1A_ObjectIdentity = ObjectIdentity
hh3cSecBladeCRIMNAM1A = _Hh3cSecBladeCRIMNAM1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 762)
)
_Hh3cMSR2630_ObjectIdentity = ObjectIdentity
hh3cMSR2630 = _Hh3cMSR2630_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 763)
)
_Hh3cMSR3610AC_ObjectIdentity = ObjectIdentity
hh3cMSR3610AC = _Hh3cMSR3610AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 764)
)
_Hh3cMSR3610DC_ObjectIdentity = ObjectIdentity
hh3cMSR3610DC = _Hh3cMSR3610DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 765)
)
_Hh3cMSR3620AC_ObjectIdentity = ObjectIdentity
hh3cMSR3620AC = _Hh3cMSR3620AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 766)
)
_Hh3cMSR3620DC_ObjectIdentity = ObjectIdentity
hh3cMSR3620DC = _Hh3cMSR3620DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 767)
)
_Hh3cMSR3620POE_ObjectIdentity = ObjectIdentity
hh3cMSR3620POE = _Hh3cMSR3620POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 768)
)
_Hh3cMSR3640_ObjectIdentity = ObjectIdentity
hh3cMSR3640 = _Hh3cMSR3640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 769)
)
_Hh3cMSR3660_ObjectIdentity = ObjectIdentity
hh3cMSR3660 = _Hh3cMSR3660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 770)
)
_Hh3cMSR5660_ObjectIdentity = ObjectIdentity
hh3cMSR5660 = _Hh3cMSR5660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 771)
)
_Hh3cMSR5680_ObjectIdentity = ObjectIdentity
hh3cMSR5680 = _Hh3cMSR5680_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 772)
)
_Hh3cS512058CHI_ObjectIdentity = ObjectIdentity
hh3cS512058CHI = _Hh3cS512058CHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 773)
)
_Hh3cS512034CHI_ObjectIdentity = ObjectIdentity
hh3cS512034CHI = _Hh3cS512034CHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 774)
)
_Hh3cLSU3WCMD0_ObjectIdentity = ObjectIdentity
hh3cLSU3WCMD0 = _Hh3cLSU3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 775)
)
_Hh3cEWPX3WCMD0_ObjectIdentity = ObjectIdentity
hh3cEWPX3WCMD0 = _Hh3cEWPX3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 776)
)
_Hh3cS7612X_ObjectIdentity = ObjectIdentity
hh3cS7612X = _Hh3cS7612X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 777)
)
_Hh3cWX6103E_ObjectIdentity = ObjectIdentity
hh3cWX6103E = _Hh3cWX6103E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 778)
)
_Hh3cSecBladeCRIMFW1A_ObjectIdentity = ObjectIdentity
hh3cSecBladeCRIMFW1A = _Hh3cSecBladeCRIMFW1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 779)
)
_Hh3cHIC66216C_ObjectIdentity = ObjectIdentity
hh3cHIC66216C = _Hh3cHIC66216C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 780)
)
_Hh3cHIC66216L_ObjectIdentity = ObjectIdentity
hh3cHIC66216L = _Hh3cHIC66216L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 781)
)
_Hh3cHIC3401V_ObjectIdentity = ObjectIdentity
hh3cHIC3401V = _Hh3cHIC3401V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 782)
)
_Hh3cHIC3401VIR_ObjectIdentity = ObjectIdentity
hh3cHIC3401VIR = _Hh3cHIC3401VIR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 783)
)
_Hh3cHIC3421V_ObjectIdentity = ObjectIdentity
hh3cHIC3421V = _Hh3cHIC3421V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 784)
)
_Hh3cHIC3421VIR_ObjectIdentity = ObjectIdentity
hh3cHIC3421VIR = _Hh3cHIC3421VIR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 785)
)
_Hh3cSIC235IR1_ObjectIdentity = ObjectIdentity
hh3cSIC235IR1 = _Hh3cSIC235IR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 786)
)
_Hh3cSIC235IR3_ObjectIdentity = ObjectIdentity
hh3cSIC235IR3 = _Hh3cSIC235IR3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 787)
)
_Hh3cSIC335EVIR_ObjectIdentity = ObjectIdentity
hh3cSIC335EVIR = _Hh3cSIC335EVIR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 788)
)
_Hh3cHIC5511I_ObjectIdentity = ObjectIdentity
hh3cHIC5511I = _Hh3cHIC5511I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 789)
)
_Hh3cHIC5521I_ObjectIdentity = ObjectIdentity
hh3cHIC5521I = _Hh3cHIC5521I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 790)
)
_Hh3cHIC5551I_ObjectIdentity = ObjectIdentity
hh3cHIC5551I = _Hh3cHIC5551I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 791)
)
_Hh3cHIC5421E_ObjectIdentity = ObjectIdentity
hh3cHIC5421E = _Hh3cHIC5421E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 792)
)
_Hh3cHIC5401E_ObjectIdentity = ObjectIdentity
hh3cHIC5401E = _Hh3cHIC5401E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 793)
)
_Hh3cHIC5421D_ObjectIdentity = ObjectIdentity
hh3cHIC5421D = _Hh3cHIC5421D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 794)
)
_Hh3cHIC5401D_ObjectIdentity = ObjectIdentity
hh3cHIC5401D = _Hh3cHIC5401D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 795)
)
_Hh3cHIC5621_ObjectIdentity = ObjectIdentity
hh3cHIC5621 = _Hh3cHIC5621_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 796)
)
_Hh3cHIC5601_ObjectIdentity = ObjectIdentity
hh3cHIC5601 = _Hh3cHIC5601_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 797)
)
_Hh3cHIC6501E_ObjectIdentity = ObjectIdentity
hh3cHIC6501E = _Hh3cHIC6501E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 798)
)
_Hh3cHIC6621E_ObjectIdentity = ObjectIdentity
hh3cHIC6621E = _Hh3cHIC6621E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 799)
)
_Hh3cSIC635_ObjectIdentity = ObjectIdentity
hh3cSIC635 = _Hh3cSIC635_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 800)
)
_Hh3cHIC6501IR_ObjectIdentity = ObjectIdentity
hh3cHIC6501IR = _Hh3cHIC6501IR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 801)
)
_Hh3cHIC6621IR_ObjectIdentity = ObjectIdentity
hh3cHIC6621IR = _Hh3cHIC6621IR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 802)
)
_Hh3cSIC635IR_ObjectIdentity = ObjectIdentity
hh3cSIC635IR = _Hh3cSIC635IR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 803)
)
_Hh3cEC2508HF4CH_ObjectIdentity = ObjectIdentity
hh3cEC2508HF4CH = _Hh3cEC2508HF4CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 804)
)
_Hh3cEC2516HF8CH_ObjectIdentity = ObjectIdentity
hh3cEC2516HF8CH = _Hh3cEC2516HF8CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 805)
)
_Hh3cECR3308HF_ObjectIdentity = ObjectIdentity
hh3cECR3308HF = _Hh3cECR3308HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 806)
)
_Hh3cECR3316HF_ObjectIdentity = ObjectIdentity
hh3cECR3316HF = _Hh3cECR3316HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 807)
)
_Hh3cISC3500E_ObjectIdentity = ObjectIdentity
hh3cISC3500E = _Hh3cISC3500E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 808)
)
_Hh3cISC3500S_ObjectIdentity = ObjectIdentity
hh3cISC3500S = _Hh3cISC3500S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 809)
)
_Hh3cECR3304HFE_ObjectIdentity = ObjectIdentity
hh3cECR3304HFE = _Hh3cECR3304HFE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 810)
)
_Hh3cECR3308HFE_ObjectIdentity = ObjectIdentity
hh3cECR3308HFE = _Hh3cECR3308HFE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 811)
)
_Hh3cECR3316HFE_ObjectIdentity = ObjectIdentity
hh3cECR3316HFE = _Hh3cECR3316HFE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 812)
)
_Hh3cISC3600_ObjectIdentity = ObjectIdentity
hh3cISC3600 = _Hh3cISC3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 813)
)
_Hh3cECR3204HW_ObjectIdentity = ObjectIdentity
hh3cECR3204HW = _Hh3cECR3204HW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 814)
)
_Hh3cECR3208HW_ObjectIdentity = ObjectIdentity
hh3cECR3208HW = _Hh3cECR3208HW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 815)
)
_Hh3cECR3216HW_ObjectIdentity = ObjectIdentity
hh3cECR3216HW = _Hh3cECR3216HW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 816)
)
_Hh3cEC2508HW_ObjectIdentity = ObjectIdentity
hh3cEC2508HW = _Hh3cEC2508HW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 817)
)
_Hh3cEC2516HW_ObjectIdentity = ObjectIdentity
hh3cEC2516HW = _Hh3cEC2516HW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 818)
)
_Hh3cISC2600_ObjectIdentity = ObjectIdentity
hh3cISC2600 = _Hh3cISC2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 819)
)
_Hh3cDC2808FH_ObjectIdentity = ObjectIdentity
hh3cDC2808FH = _Hh3cDC2808FH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 820)
)
_Hh3cCE300034C_ObjectIdentity = ObjectIdentity
hh3cCE300034C = _Hh3cCE300034C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 821)
)
_Hh3cCE300058C_ObjectIdentity = ObjectIdentity
hh3cCE300058C = _Hh3cCE300058C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 822)
)
_Hh3cSR6604X_ObjectIdentity = ObjectIdentity
hh3cSR6604X = _Hh3cSR6604X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 823)
)
_Hh3cSR6608X_ObjectIdentity = ObjectIdentity
hh3cSR6608X = _Hh3cSR6608X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 824)
)
_Hh3cSR6616X_ObjectIdentity = ObjectIdentity
hh3cSR6616X = _Hh3cSR6616X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 825)
)
_Hh3csecpathF100AG_ObjectIdentity = ObjectIdentity
hh3csecpathF100AG = _Hh3csecpathF100AG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 826)
)
_Hh3csecpathF100CG_ObjectIdentity = ObjectIdentity
hh3csecpathF100CG = _Hh3csecpathF100CG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 827)
)
_Hh3csecpathF100EG_ObjectIdentity = ObjectIdentity
hh3csecpathF100EG = _Hh3csecpathF100EG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 828)
)
_Hh3csecpathF100MG_ObjectIdentity = ObjectIdentity
hh3csecpathF100MG = _Hh3csecpathF100MG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 829)
)
_Hh3csecpathF100SG_ObjectIdentity = ObjectIdentity
hh3csecpathF100SG = _Hh3csecpathF100SG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 830)
)
_Hh3cS3100V226TPWiNet_ObjectIdentity = ObjectIdentity
hh3cS3100V226TPWiNet = _Hh3cS3100V226TPWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 831)
)
_Hh3cS550024PWiNet_ObjectIdentity = ObjectIdentity
hh3cS550024PWiNet = _Hh3cS550024PWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 832)
)
_Hh3cS512028PPoeWiNet_ObjectIdentity = ObjectIdentity
hh3cS512028PPoeWiNet = _Hh3cS512028PPoeWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 833)
)
_Hh3cS512028PWiNet_ObjectIdentity = ObjectIdentity
hh3cS512028PWiNet = _Hh3cS512028PWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 834)
)
_Hh3cS550034CPWRHI_ObjectIdentity = ObjectIdentity
hh3cS550034CPWRHI = _Hh3cS550034CPWRHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 835)
)
_Hh3cS550058CPWRHI_ObjectIdentity = ObjectIdentity
hh3cS550058CPWRHI = _Hh3cS550058CPWRHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 836)
)
_Hh3cS550034FHI_ObjectIdentity = ObjectIdentity
hh3cS550034FHI = _Hh3cS550034FHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 837)
)
_Hh3cMSR930_ObjectIdentity = ObjectIdentity
hh3cMSR930 = _Hh3cMSR930_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 838)
)
_Hh3cMSV50_ObjectIdentity = ObjectIdentity
hh3cMSV50 = _Hh3cMSV50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 839)
)
_Hh3cMSR930WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR930WiNet = _Hh3cMSR930WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 840)
)
_Hh3cMSR930GU_ObjectIdentity = ObjectIdentity
hh3cMSR930GU = _Hh3cMSR930GU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 841)
)
_Hh3cMSR930sa_ObjectIdentity = ObjectIdentity
hh3cMSR930sa = _Hh3cMSR930sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 842)
)
_Hh3cMSR930GG_ObjectIdentity = ObjectIdentity
hh3cMSR930GG = _Hh3cMSR930GG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 843)
)
_Hh3cS5820V254QSGE_ObjectIdentity = ObjectIdentity
hh3cS5820V254QSGE = _Hh3cS5820V254QSGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 844)
)
_Hh3cS5820V252Q_ObjectIdentity = ObjectIdentity
hh3cS5820V252Q = _Hh3cS5820V252Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 845)
)
_Hh3cCC754E_ObjectIdentity = ObjectIdentity
hh3cCC754E = _Hh3cCC754E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 846)
)
_Hh3cWP5008_ObjectIdentity = ObjectIdentity
hh3cWP5008 = _Hh3cWP5008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 847)
)
_Hh3cSecBladeCRIMLB1A_ObjectIdentity = ObjectIdentity
hh3cSecBladeCRIMLB1A = _Hh3cSecBladeCRIMLB1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 848)
)
_Hh3cS550034CHID_ObjectIdentity = ObjectIdentity
hh3cS550034CHID = _Hh3cS550034CHID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 849)
)
_Hh3cS550058CHID_ObjectIdentity = ObjectIdentity
hh3cS550058CHID = _Hh3cS550058CHID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 850)
)
_Hh3cS9505EV7_ObjectIdentity = ObjectIdentity
hh3cS9505EV7 = _Hh3cS9505EV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 851)
)
_Hh3cS9508EV7_ObjectIdentity = ObjectIdentity
hh3cS9508EV7 = _Hh3cS9508EV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 852)
)
_Hh3cS9508EVV7_ObjectIdentity = ObjectIdentity
hh3cS9508EVV7 = _Hh3cS9508EVV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 853)
)
_Hh3cS9512EV7_ObjectIdentity = ObjectIdentity
hh3cS9512EV7 = _Hh3cS9512EV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 854)
)
_Hh3cS12508V7_ObjectIdentity = ObjectIdentity
hh3cS12508V7 = _Hh3cS12508V7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 855)
)
_Hh3cS12518V7_ObjectIdentity = ObjectIdentity
hh3cS12518V7 = _Hh3cS12518V7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 856)
)
_Hh3cS12504V7_ObjectIdentity = ObjectIdentity
hh3cS12504V7 = _Hh3cS12504V7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 857)
)
_Hh3csecpathF100CAI_ObjectIdentity = ObjectIdentity
hh3csecpathF100CAI = _Hh3csecpathF100CAI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 858)
)
_Hh3csecpathL1000A_ObjectIdentity = ObjectIdentity
hh3csecpathL1000A = _Hh3csecpathL1000A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 859)
)
_Hh3cWA2610E_ObjectIdentity = ObjectIdentity
hh3cWA2610E = _Hh3cWA2610E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 860)
)
_Hh3cWA2620E_ObjectIdentity = ObjectIdentity
hh3cWA2620E = _Hh3cWA2620E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 861)
)
_Hh3cWA2620X_ObjectIdentity = ObjectIdentity
hh3cWA2620X = _Hh3cWA2620X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 862)
)
_Hh3cWA2610X_ObjectIdentity = ObjectIdentity
hh3cWA2610X = _Hh3cWA2610X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 863)
)
_Hh3cS6802_ObjectIdentity = ObjectIdentity
hh3cS6802 = _Hh3cS6802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 864)
)
_Hh3cS9804_ObjectIdentity = ObjectIdentity
hh3cS9804 = _Hh3cS9804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 865)
)
_Hh3cSecBladeLSU1IPSBEA0_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSU1IPSBEA0 = _Hh3cSecBladeLSU1IPSBEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 866)
)
_Hh3cSecBladeLST1IPS2A1_ObjectIdentity = ObjectIdentity
hh3cSecBladeLST1IPS2A1 = _Hh3cSecBladeLST1IPS2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 867)
)
_Hh3cMSR930W_ObjectIdentity = ObjectIdentity
hh3cMSR930W = _Hh3cMSR930W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 868)
)
_Hh3cMSR930WGU_ObjectIdentity = ObjectIdentity
hh3cMSR930WGU = _Hh3cMSR930WGU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 869)
)
_Hh3cSecPathF5000C_ObjectIdentity = ObjectIdentity
hh3cSecPathF5000C = _Hh3cSecPathF5000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 870)
)
_Hh3cSecPathF5000S_ObjectIdentity = ObjectIdentity
hh3cSecPathF5000S = _Hh3cSecPathF5000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 871)
)
_Hh3cS12510FDC_ObjectIdentity = ObjectIdentity
hh3cS12510FDC = _Hh3cS12510FDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 872)
)
_Hh3cS12510FAC_ObjectIdentity = ObjectIdentity
hh3cS12510FAC = _Hh3cS12510FAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 873)
)
_Hh3cS12510XDC_ObjectIdentity = ObjectIdentity
hh3cS12510XDC = _Hh3cS12510XDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 874)
)
_Hh3cS12510XAC_ObjectIdentity = ObjectIdentity
hh3cS12510XAC = _Hh3cS12510XAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 875)
)
_Hh3cS12508_ObjectIdentity = ObjectIdentity
hh3cS12508 = _Hh3cS12508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 876)
)
_Hh3cS12518_ObjectIdentity = ObjectIdentity
hh3cS12518 = _Hh3cS12518_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 877)
)
_Hh3cS12516FDC_ObjectIdentity = ObjectIdentity
hh3cS12516FDC = _Hh3cS12516FDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 878)
)
_Hh3cS12516FAC_ObjectIdentity = ObjectIdentity
hh3cS12516FAC = _Hh3cS12516FAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 879)
)
_Hh3cS12516XDC_ObjectIdentity = ObjectIdentity
hh3cS12516XDC = _Hh3cS12516XDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 880)
)
_Hh3cS12516XAC_ObjectIdentity = ObjectIdentity
hh3cS12516XAC = _Hh3cS12516XAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 881)
)
_Hh3cMSR930GT_ObjectIdentity = ObjectIdentity
hh3cMSR930GT = _Hh3cMSR930GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 882)
)
_Hh3cMSR2600GTC_ObjectIdentity = ObjectIdentity
hh3cMSR2600GTC = _Hh3cMSR2600GTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 883)
)
_Hh3cMSR2600GUC_ObjectIdentity = ObjectIdentity
hh3cMSR2600GUC = _Hh3cMSR2600GUC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 884)
)
_Hh3csecpathF1000AG_ObjectIdentity = ObjectIdentity
hh3csecpathF1000AG = _Hh3csecpathF1000AG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 885)
)
_Hh3csecpathF1000CG_ObjectIdentity = ObjectIdentity
hh3csecpathF1000CG = _Hh3csecpathF1000CG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 886)
)
_Hh3csecpathF1000SG_ObjectIdentity = ObjectIdentity
hh3csecpathF1000SG = _Hh3csecpathF1000SG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 887)
)
_Hh3cSecBladeLSQ2FWBSCO_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSQ2FWBSCO = _Hh3cSecBladeLSQ2FWBSCO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 888)
)
_Hh3cWA2620AGN_ObjectIdentity = ObjectIdentity
hh3cWA2620AGN = _Hh3cWA2620AGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 889)
)
_Hh3cVSR_ObjectIdentity = ObjectIdentity
hh3cVSR = _Hh3cVSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 890)
)
_Hh3cVSR1001_ObjectIdentity = ObjectIdentity
hh3cVSR1001 = _Hh3cVSR1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 891)
)
_Hh3cVSR1004_ObjectIdentity = ObjectIdentity
hh3cVSR1004 = _Hh3cVSR1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 892)
)
_Hh3cVSR1008_ObjectIdentity = ObjectIdentity
hh3cVSR1008 = _Hh3cVSR1008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 893)
)
_Hh3cS5120S28PEI_ObjectIdentity = ObjectIdentity
hh3cS5120S28PEI = _Hh3cS5120S28PEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 894)
)
_Hh3cS5120S52PEI_ObjectIdentity = ObjectIdentity
hh3cS5120S52PEI = _Hh3cS5120S52PEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 895)
)
_Hh3cMSR930WiNetW_ObjectIdentity = ObjectIdentity
hh3cMSR930WiNetW = _Hh3cMSR930WiNetW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 896)
)
_Hh3cWA3628iAGNX_ObjectIdentity = ObjectIdentity
hh3cWA3628iAGNX = _Hh3cWA3628iAGNX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 897)
)
_Hh3cS2110_ObjectIdentity = ObjectIdentity
hh3cS2110 = _Hh3cS2110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 898)
)
_Hh3cS2110PWR_ObjectIdentity = ObjectIdentity
hh3cS2110PWR = _Hh3cS2110PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 899)
)
_Hh3cS2126_ObjectIdentity = ObjectIdentity
hh3cS2126 = _Hh3cS2126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 900)
)
_Hh3cS2126PWR_ObjectIdentity = ObjectIdentity
hh3cS2126PWR = _Hh3cS2126PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 901)
)
_Hh3cS2152_ObjectIdentity = ObjectIdentity
hh3cS2152 = _Hh3cS2152_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 902)
)
_Hh3cWX5540WCM_ObjectIdentity = ObjectIdentity
hh3cWX5540WCM = _Hh3cWX5540WCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 903)
)
_Hh3cWX5540LSW_ObjectIdentity = ObjectIdentity
hh3cWX5540LSW = _Hh3cWX5540LSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 904)
)
_Hh3cWX5520WCM_ObjectIdentity = ObjectIdentity
hh3cWX5520WCM = _Hh3cWX5520WCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 905)
)
_Hh3cWX5520LSW_ObjectIdentity = ObjectIdentity
hh3cWX5520LSW = _Hh3cWX5520LSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 906)
)
_Hh3cMSR930WGT_ObjectIdentity = ObjectIdentity
hh3cMSR930WGT = _Hh3cMSR930WGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 907)
)
_Hh3cICG5000T_ObjectIdentity = ObjectIdentity
hh3cICG5000T = _Hh3cICG5000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 908)
)
_Hh3cICG6000_ObjectIdentity = ObjectIdentity
hh3cICG6000 = _Hh3cICG6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 909)
)
_Hh3cMSR2630WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR2630WiNet = _Hh3cMSR2630WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 910)
)
_Hh3cMSR3610WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR3610WiNet = _Hh3cMSR3610WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 911)
)
_Hh3cMSR3660WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR3660WiNet = _Hh3cMSR3660WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 912)
)
_Hh3cMSR260010_ObjectIdentity = ObjectIdentity
hh3cMSR260010 = _Hh3cMSR260010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 913)
)
_Hh3cMSR260010WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR260010WiNet = _Hh3cMSR260010WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 914)
)
_Hh3cMSR260017_ObjectIdentity = ObjectIdentity
hh3cMSR260017 = _Hh3cMSR260017_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 915)
)
_Hh3cICG3000D_ObjectIdentity = ObjectIdentity
hh3cICG3000D = _Hh3cICG3000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 916)
)
_Hh3cICG3000E_ObjectIdentity = ObjectIdentity
hh3cICG3000E = _Hh3cICG3000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 917)
)
_Hh3cSecBladeLSU1ADECEA0_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSU1ADECEA0 = _Hh3cSecBladeLSU1ADECEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 918)
)
_Hh3cSecBladeLST1ADE1A1_ObjectIdentity = ObjectIdentity
hh3cSecBladeLST1ADE1A1 = _Hh3cSecBladeLST1ADE1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 919)
)
_Hh3cSR8804X_ObjectIdentity = ObjectIdentity
hh3cSR8804X = _Hh3cSR8804X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 920)
)
_Hh3cSR8808X_ObjectIdentity = ObjectIdentity
hh3cSR8808X = _Hh3cSR8808X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 921)
)
_Hh3cSR8812X_ObjectIdentity = ObjectIdentity
hh3cSR8812X = _Hh3cSR8812X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 922)
)
_Hh3cCC710E_ObjectIdentity = ObjectIdentity
hh3cCC710E = _Hh3cCC710E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 923)
)
_Hh3cCC712E_ObjectIdentity = ObjectIdentity
hh3cCC712E = _Hh3cCC712E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 924)
)
_Hh3cS680032Q_ObjectIdentity = ObjectIdentity
hh3cS680032Q = _Hh3cS680032Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 925)
)
_Hh3cS5008PV2EI_ObjectIdentity = ObjectIdentity
hh3cS5008PV2EI = _Hh3cS5008PV2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 926)
)
_Hh3cS5024PV2EI_ObjectIdentity = ObjectIdentity
hh3cS5024PV2EI = _Hh3cS5024PV2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 927)
)
_Hh3cS5048PV2EI_ObjectIdentity = ObjectIdentity
hh3cS5048PV2EI = _Hh3cS5048PV2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 928)
)
_Hh3cS2610_ObjectIdentity = ObjectIdentity
hh3cS2610 = _Hh3cS2610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 929)
)
_Hh3cS2610PWR_ObjectIdentity = ObjectIdentity
hh3cS2610PWR = _Hh3cS2610PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 930)
)
_Hh3cS2626_ObjectIdentity = ObjectIdentity
hh3cS2626 = _Hh3cS2626_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 931)
)
_Hh3cS2626PWR_ObjectIdentity = ObjectIdentity
hh3cS2626PWR = _Hh3cS2626PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 932)
)
_Hh3cS2652_ObjectIdentity = ObjectIdentity
hh3cS2652 = _Hh3cS2652_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 933)
)
_Hh3cSimware7BoxCen_ObjectIdentity = ObjectIdentity
hh3cSimware7BoxCen = _Hh3cSimware7BoxCen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 934)
)
_Hh3cSimware7BoxIRF_ObjectIdentity = ObjectIdentity
hh3cSimware7BoxIRF = _Hh3cSimware7BoxIRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 935)
)
_Hh3cSimware7ChassisDevice_ObjectIdentity = ObjectIdentity
hh3cSimware7ChassisDevice = _Hh3cSimware7ChassisDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 936)
)
_Hh3cVSR1000_ObjectIdentity = ObjectIdentity
hh3cVSR1000 = _Hh3cVSR1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 937)
)
_Hh3csecpathM9000_ObjectIdentity = ObjectIdentity
hh3csecpathM9000 = _Hh3csecpathM9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 938)
)
_Hh3csecpathM9006_ObjectIdentity = ObjectIdentity
hh3csecpathM9006 = _Hh3csecpathM9006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 939)
)
_Hh3csecpathM9010_ObjectIdentity = ObjectIdentity
hh3csecpathM9010 = _Hh3csecpathM9010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 940)
)
_Hh3csecpathM9014_ObjectIdentity = ObjectIdentity
hh3csecpathM9014 = _Hh3csecpathM9014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 941)
)
_Hh3cSecBladeIIINSQM1FWCEA0_ObjectIdentity = ObjectIdentity
hh3cSecBladeIIINSQM1FWCEA0 = _Hh3cSecBladeIIINSQM1FWCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 942)
)
_Hh3cWB521X_ObjectIdentity = ObjectIdentity
hh3cWB521X = _Hh3cWB521X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 943)
)
_Hh3cWB511X_ObjectIdentity = ObjectIdentity
hh3cWB511X = _Hh3cWB511X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 944)
)
_Hh3cER3108G_ObjectIdentity = ObjectIdentity
hh3cER3108G = _Hh3cER3108G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 945)
)
_Hh3cER3108GW_ObjectIdentity = ObjectIdentity
hh3cER3108GW = _Hh3cER3108GW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 946)
)
_Hh3cS513028SEI_ObjectIdentity = ObjectIdentity
hh3cS513028SEI = _Hh3cS513028SEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 947)
)
_Hh3cS513052SEI_ObjectIdentity = ObjectIdentity
hh3cS513052SEI = _Hh3cS513052SEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 948)
)
_Hh3cS513028FEI_ObjectIdentity = ObjectIdentity
hh3cS513028FEI = _Hh3cS513028FEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 949)
)
_Hh3cS513028SPWREI_ObjectIdentity = ObjectIdentity
hh3cS513028SPWREI = _Hh3cS513028SPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 950)
)
_Hh3cS513052SPWREI_ObjectIdentity = ObjectIdentity
hh3cS513052SPWREI = _Hh3cS513052SPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 951)
)
_Hh3cMSR360028_ObjectIdentity = ObjectIdentity
hh3cMSR360028 = _Hh3cMSR360028_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 952)
)
_Hh3cMSR360051_ObjectIdentity = ObjectIdentity
hh3cMSR360051 = _Hh3cMSR360051_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 953)
)
_Hh3cWA2612E_ObjectIdentity = ObjectIdentity
hh3cWA2612E = _Hh3cWA2612E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 954)
)
_Hh3cWA2622_ObjectIdentity = ObjectIdentity
hh3cWA2622 = _Hh3cWA2622_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 955)
)
_Hh3cS511010P_ObjectIdentity = ObjectIdentity
hh3cS511010P = _Hh3cS511010P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 956)
)
_Hh3cS511010PPWR_ObjectIdentity = ObjectIdentity
hh3cS511010PPWR = _Hh3cS511010PPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 957)
)
_Hh3cS511028P_ObjectIdentity = ObjectIdentity
hh3cS511028P = _Hh3cS511028P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 958)
)
_Hh3cS511028PPWR_ObjectIdentity = ObjectIdentity
hh3cS511028PPWR = _Hh3cS511028PPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 959)
)
_Hh3cS511052P_ObjectIdentity = ObjectIdentity
hh3cS511052P = _Hh3cS511052P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 960)
)
_Hh3cS511010PD_ObjectIdentity = ObjectIdentity
hh3cS511010PD = _Hh3cS511010PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 961)
)
_Hh3cS511010PPWRD_ObjectIdentity = ObjectIdentity
hh3cS511010PPWRD = _Hh3cS511010PPWRD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 962)
)
_Hh3cS511028PD_ObjectIdentity = ObjectIdentity
hh3cS511028PD = _Hh3cS511028PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 963)
)
_Hh3cS511028PPWRD_ObjectIdentity = ObjectIdentity
hh3cS511028PPWRD = _Hh3cS511028PPWRD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 964)
)
_Hh3cS511052PD_ObjectIdentity = ObjectIdentity
hh3cS511052PD = _Hh3cS511052PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 965)
)
_Hh3cWX5510_ObjectIdentity = ObjectIdentity
hh3cWX5510 = _Hh3cWX5510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 966)
)
_Hh3cS550028SCHI_ObjectIdentity = ObjectIdentity
hh3cS550028SCHI = _Hh3cS550028SCHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 967)
)
_Hh3cS550052SCHI_ObjectIdentity = ObjectIdentity
hh3cS550052SCHI = _Hh3cS550052SCHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 968)
)
_Hh3cS550028SCHID_ObjectIdentity = ObjectIdentity
hh3cS550028SCHID = _Hh3cS550028SCHID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 969)
)
_Hh3cS550052SCHID_ObjectIdentity = ObjectIdentity
hh3cS550052SCHID = _Hh3cS550052SCHID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 970)
)
_Hh3cLA2608_ObjectIdentity = ObjectIdentity
hh3cLA2608 = _Hh3cLA2608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 971)
)
_Hh3cS311010TP_ObjectIdentity = ObjectIdentity
hh3cS311010TP = _Hh3cS311010TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 972)
)
_Hh3cS311010TPPWR_ObjectIdentity = ObjectIdentity
hh3cS311010TPPWR = _Hh3cS311010TPPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 973)
)
_Hh3cS311026TP_ObjectIdentity = ObjectIdentity
hh3cS311026TP = _Hh3cS311026TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 974)
)
_Hh3cS311026TPPWR_ObjectIdentity = ObjectIdentity
hh3cS311026TPPWR = _Hh3cS311026TPPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 975)
)
_Hh3cS311052TP_ObjectIdentity = ObjectIdentity
hh3cS311052TP = _Hh3cS311052TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 976)
)
_Hh3cWA2610HGN_ObjectIdentity = ObjectIdentity
hh3cWA2610HGN = _Hh3cWA2610HGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 977)
)
_Hh3cWA4620EACN_ObjectIdentity = ObjectIdentity
hh3cWA4620EACN = _Hh3cWA4620EACN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 978)
)
_Hh3cWA4620IACN_ObjectIdentity = ObjectIdentity
hh3cWA4620IACN = _Hh3cWA4620IACN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 979)
)
_Hh3cEWPX1MAC0_ObjectIdentity = ObjectIdentity
hh3cEWPX1MAC0 = _Hh3cEWPX1MAC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 980)
)
_Hh3cCRIMMAC1A_ObjectIdentity = ObjectIdentity
hh3cCRIMMAC1A = _Hh3cCRIMMAC1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 981)
)
_Hh3cSecBladeIIILST1FW3B1_ObjectIdentity = ObjectIdentity
hh3cSecBladeIIILST1FW3B1 = _Hh3cSecBladeIIILST1FW3B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 982)
)
_Hh3cWA2620iAGNX_ObjectIdentity = ObjectIdentity
hh3cWA2620iAGNX = _Hh3cWA2620iAGNX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 983)
)
_Hh3cS311010TPSI_ObjectIdentity = ObjectIdentity
hh3cS311010TPSI = _Hh3cS311010TPSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 984)
)
_Hh3cS311026TPSI_ObjectIdentity = ObjectIdentity
hh3cS311026TPSI = _Hh3cS311026TPSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 985)
)
_Hh3cS311052TPSI_ObjectIdentity = ObjectIdentity
hh3cS311052TPSI = _Hh3cS311052TPSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 986)
)
_Hh3cS511010PSI_ObjectIdentity = ObjectIdentity
hh3cS511010PSI = _Hh3cS511010PSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 987)
)
_Hh3cS511028PSI_ObjectIdentity = ObjectIdentity
hh3cS511028PSI = _Hh3cS511028PSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 988)
)
_Hh3cS511052PSI_ObjectIdentity = ObjectIdentity
hh3cS511052PSI = _Hh3cS511052PSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 989)
)
_Hh3cS3100V252TPWiNet_ObjectIdentity = ObjectIdentity
hh3cS3100V252TPWiNet = _Hh3cS3100V252TPWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 990)
)
_Hh3cS512052PWiNet_ObjectIdentity = ObjectIdentity
hh3cS512052PWiNet = _Hh3cS512052PWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 991)
)
_Hh3cS550048PWiNet_ObjectIdentity = ObjectIdentity
hh3cS550048PWiNet = _Hh3cS550048PWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 992)
)
_Hh3cS550028FWiNet_ObjectIdentity = ObjectIdentity
hh3cS550028FWiNet = _Hh3cS550028FWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 993)
)
_Hh3CWA2620EX_ObjectIdentity = ObjectIdentity
hh3CWA2620EX = _Hh3CWA2620EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 994)
)
_Hh3csecpathL5000S_ObjectIdentity = ObjectIdentity
hh3csecpathL5000S = _Hh3csecpathL5000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 995)
)
_Hh3csecpathL5000C_ObjectIdentity = ObjectIdentity
hh3csecpathL5000C = _Hh3csecpathL5000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 996)
)
_Hh3cCC721E_ObjectIdentity = ObjectIdentity
hh3cCC721E = _Hh3cCC721E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 997)
)
_Hh3cS5820V252QFU_ObjectIdentity = ObjectIdentity
hh3cS5820V252QFU = _Hh3cS5820V252QFU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 998)
)
_Hh3csecpathVFW1000_ObjectIdentity = ObjectIdentity
hh3csecpathVFW1000 = _Hh3csecpathVFW1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 999)
)
_Hh3cS7003_ObjectIdentity = ObjectIdentity
hh3cS7003 = _Hh3cS7003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1000)
)
_Hh3cS7006_ObjectIdentity = ObjectIdentity
hh3cS7006 = _Hh3cS7006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1001)
)
_Hh3csecpathF100CSI_ObjectIdentity = ObjectIdentity
hh3csecpathF100CSI = _Hh3csecpathF100CSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1002)
)
_Hh3cWX3510E_ObjectIdentity = ObjectIdentity
hh3cWX3510E = _Hh3cWX3510E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1003)
)
_Hh3cWX3540E_ObjectIdentity = ObjectIdentity
hh3cWX3540E = _Hh3cWX3540E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1004)
)
_Hh3cSecBladeLSU3FWCEA0_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSU3FWCEA0 = _Hh3cSecBladeLSU3FWCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1005)
)
_Hh3cSecBladeLSU1NSCEA0_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSU1NSCEA0 = _Hh3cSecBladeLSU1NSCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1006)
)
_Hh3cSecBladeLST1FW3C1_ObjectIdentity = ObjectIdentity
hh3cSecBladeLST1FW3C1 = _Hh3cSecBladeLST1FW3C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1007)
)
_Hh3cSecBladeLST1NSM2C1_ObjectIdentity = ObjectIdentity
hh3cSecBladeLST1NSM2C1 = _Hh3cSecBladeLST1NSM2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1008)
)
_Hh3cSecBladeLSX1FWCEA1_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSX1FWCEA1 = _Hh3cSecBladeLSX1FWCEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1009)
)
_Hh3cSecBladeLSX1NSCEA1_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSX1NSCEA1 = _Hh3cSecBladeLSX1NSCEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1010)
)
_Hh3cWA2620AGNC_ObjectIdentity = ObjectIdentity
hh3cWA2620AGNC = _Hh3cWA2620AGNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1011)
)
_Hh3cWA2610GN_ObjectIdentity = ObjectIdentity
hh3cWA2610GN = _Hh3cWA2610GN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1012)
)
_Hh3cWA2610GNE_ObjectIdentity = ObjectIdentity
hh3cWA2610GNE = _Hh3cWA2610GNE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1013)
)
_Hh3cMSR800_ObjectIdentity = ObjectIdentity
hh3cMSR800 = _Hh3cMSR800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1014)
)
_Hh3cMSR800Wlan_ObjectIdentity = ObjectIdentity
hh3cMSR800Wlan = _Hh3cMSR800Wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1015)
)
_Hh3cMSR80010_ObjectIdentity = ObjectIdentity
hh3cMSR80010 = _Hh3cMSR80010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1016)
)
_Hh3cMSR80010Wlan_ObjectIdentity = ObjectIdentity
hh3cMSR80010Wlan = _Hh3cMSR80010Wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1017)
)
_Hh3cMSR830WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR830WiNet = _Hh3cMSR830WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1018)
)
_Hh3cMSR83010WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR83010WiNet = _Hh3cMSR83010WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1019)
)
_Hh3cMSR93010WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR93010WiNet = _Hh3cMSR93010WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1020)
)
_Hh3cS9810_ObjectIdentity = ObjectIdentity
hh3cS9810 = _Hh3cS9810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1021)
)
_Hh3cFlexNetworkB6300XLG_ObjectIdentity = ObjectIdentity
hh3cFlexNetworkB6300XLG = _Hh3cFlexNetworkB6300XLG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1022)
)
_Hh3cFlexNetworkB6300GXG_ObjectIdentity = ObjectIdentity
hh3cFlexNetworkB6300GXG = _Hh3cFlexNetworkB6300GXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1023)
)
_Hh3cMSR900E_ObjectIdentity = ObjectIdentity
hh3cMSR900E = _Hh3cMSR900E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1024)
)
_Hh3cMSR900EWlan_ObjectIdentity = ObjectIdentity
hh3cMSR900EWlan = _Hh3cMSR900EWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1025)
)
_Hh3cS513028SEID_ObjectIdentity = ObjectIdentity
hh3cS513028SEID = _Hh3cS513028SEID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1026)
)
_Hh3cS513052SEID_ObjectIdentity = ObjectIdentity
hh3cS513052SEID = _Hh3cS513052SEID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1027)
)
_Hh3cS513028FEID_ObjectIdentity = ObjectIdentity
hh3cS513028FEID = _Hh3cS513028FEID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1028)
)
_Hh3cS513028SHPWREID_ObjectIdentity = ObjectIdentity
hh3cS513028SHPWREID = _Hh3cS513028SHPWREID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1029)
)
_Hh3cS513052SPWREID_ObjectIdentity = ObjectIdentity
hh3cS513052SPWREID = _Hh3cS513052SPWREID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1030)
)
_Hh3cS513028SHPWREI_ObjectIdentity = ObjectIdentity
hh3cS513028SHPWREI = _Hh3cS513028SHPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1031)
)
_Hh3cE528X_ObjectIdentity = ObjectIdentity
hh3cE528X = _Hh3cE528X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1032)
)
_Hh3cE552X_ObjectIdentity = ObjectIdentity
hh3cE552X = _Hh3cE552X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1033)
)
_Hh3cLSU1WCME0_ObjectIdentity = ObjectIdentity
hh3cLSU1WCME0 = _Hh3cLSU1WCME0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1034)
)
_Hh3cEWPX1WCME0_ObjectIdentity = ObjectIdentity
hh3cEWPX1WCME0 = _Hh3cEWPX1WCME0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1035)
)
_Hh3cSR8810XS_ObjectIdentity = ObjectIdentity
hh3cSR8810XS = _Hh3cSR8810XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1036)
)
_Hh3cSR8806XS_ObjectIdentity = ObjectIdentity
hh3cSR8806XS = _Hh3cSR8806XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1037)
)
_Hh3cSR8803XS_ObjectIdentity = ObjectIdentity
hh3cSR8803XS = _Hh3cSR8803XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1038)
)
_Hh3cSR8802XS_ObjectIdentity = ObjectIdentity
hh3cSR8802XS = _Hh3cSR8802XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1039)
)
_Hh3cSecPathF5020_ObjectIdentity = ObjectIdentity
hh3cSecPathF5020 = _Hh3cSecPathF5020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1040)
)
_Hh3cSecPathF5040_ObjectIdentity = ObjectIdentity
hh3cSecPathF5040 = _Hh3cSecPathF5040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1041)
)
_Hh3cRA100_ObjectIdentity = ObjectIdentity
hh3cRA100 = _Hh3cRA100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1042)
)
_Hh3cMSR930LM_ObjectIdentity = ObjectIdentity
hh3cMSR930LM = _Hh3cMSR930LM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1043)
)
_Hh3cMSR930WLM_ObjectIdentity = ObjectIdentity
hh3cMSR930WLM = _Hh3cMSR930WLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1044)
)
_Hh3cMSR26005LMC_ObjectIdentity = ObjectIdentity
hh3cMSR26005LMC = _Hh3cMSR26005LMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1045)
)
_Hh3cS580032CEI_ObjectIdentity = ObjectIdentity
hh3cS580032CEI = _Hh3cS580032CEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1046)
)
_Hh3cS580056CEI_ObjectIdentity = ObjectIdentity
hh3cS580056CEI = _Hh3cS580056CEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1047)
)
_Hh3cS580032CPWREI_ObjectIdentity = ObjectIdentity
hh3cS580032CPWREI = _Hh3cS580032CPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1048)
)
_Hh3cS580056CPWREI_ObjectIdentity = ObjectIdentity
hh3cS580056CPWREI = _Hh3cS580056CPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1049)
)
_Hh3cS580056CEIM_ObjectIdentity = ObjectIdentity
hh3cS580056CEIM = _Hh3cS580056CEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1050)
)
_Hh3cWB521XE_ObjectIdentity = ObjectIdentity
hh3cWB521XE = _Hh3cWB521XE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1051)
)
_Hh3cWB521XH_ObjectIdentity = ObjectIdentity
hh3cWB521XH = _Hh3cWB521XH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1052)
)
_Hh3cWX2540E_ObjectIdentity = ObjectIdentity
hh3cWX2540E = _Hh3cWX2540E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1053)
)
_Hh3cWX360_ObjectIdentity = ObjectIdentity
hh3cWX360 = _Hh3cWX360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1054)
)
_Hh3cWX361_ObjectIdentity = ObjectIdentity
hh3cWX361 = _Hh3cWX361_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1055)
)
_Hh3cWA2610EGNE_ObjectIdentity = ObjectIdentity
hh3cWA2610EGNE = _Hh3cWA2610EGNE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1056)
)
_Hh3cSR6603F_ObjectIdentity = ObjectIdentity
hh3cSR6603F = _Hh3cSR6603F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1057)
)
_Hh3cSR6605F_ObjectIdentity = ObjectIdentity
hh3cSR6605F = _Hh3cSR6605F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1058)
)
_Hh3cSR6609F_ObjectIdentity = ObjectIdentity
hh3cSR6609F = _Hh3cSR6609F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1059)
)
_Hh3cS556030SEI_ObjectIdentity = ObjectIdentity
hh3cS556030SEI = _Hh3cS556030SEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1060)
)
_Hh3cS556054SEI_ObjectIdentity = ObjectIdentity
hh3cS556054SEI = _Hh3cS556054SEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1061)
)
_Hh3cS556030CEI_ObjectIdentity = ObjectIdentity
hh3cS556030CEI = _Hh3cS556030CEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1062)
)
_Hh3cS556054CEI_ObjectIdentity = ObjectIdentity
hh3cS556054CEI = _Hh3cS556054CEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1063)
)
_Hh3cS556030CPWREI_ObjectIdentity = ObjectIdentity
hh3cS556030CPWREI = _Hh3cS556030CPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1064)
)
_Hh3cS556054CPWREI_ObjectIdentity = ObjectIdentity
hh3cS556054CPWREI = _Hh3cS556054CPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1065)
)
_Hh3cS556054QSEI_ObjectIdentity = ObjectIdentity
hh3cS556054QSEI = _Hh3cS556054QSEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1066)
)
_Hh3cRA200_ObjectIdentity = ObjectIdentity
hh3cRA200 = _Hh3cRA200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1067)
)
_Hh3cF1000CSI_ObjectIdentity = ObjectIdentity
hh3cF1000CSI = _Hh3cF1000CSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1068)
)
_Hh3cF100MSI_ObjectIdentity = ObjectIdentity
hh3cF100MSI = _Hh3cF100MSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1069)
)
_Hh3cF100ASI_ObjectIdentity = ObjectIdentity
hh3cF100ASI = _Hh3cF100ASI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1070)
)
_Hh3cS5820V248S_ObjectIdentity = ObjectIdentity
hh3cS5820V248S = _Hh3cS5820V248S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1071)
)
_Hh3cS630042QT_ObjectIdentity = ObjectIdentity
hh3cS630042QT = _Hh3cS630042QT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1072)
)
_Hh3cS630042QF_ObjectIdentity = ObjectIdentity
hh3cS630042QF = _Hh3cS630042QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1073)
)
_Hh3cS630048S_ObjectIdentity = ObjectIdentity
hh3cS630048S = _Hh3cS630048S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1074)
)
_Hh3cS630052QF_ObjectIdentity = ObjectIdentity
hh3cS630052QF = _Hh3cS630052QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1075)
)
_Hh3cFlexNetworkU830048G_ObjectIdentity = ObjectIdentity
hh3cFlexNetworkU830048G = _Hh3cFlexNetworkU830048G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1076)
)
_Hh3cFlexNetworkU830048XLGU_ObjectIdentity = ObjectIdentity
hh3cFlexNetworkU830048XLGU = _Hh3cFlexNetworkU830048XLGU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1077)
)
_Hh3cS5008PV2EIPWR_ObjectIdentity = ObjectIdentity
hh3cS5008PV2EIPWR = _Hh3cS5008PV2EIPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1078)
)
_Hh3cS5024PV2EIPWR_ObjectIdentity = ObjectIdentity
hh3cS5024PV2EIPWR = _Hh3cS5024PV2EIPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1079)
)
_Hh3cS511052PPWR_ObjectIdentity = ObjectIdentity
hh3cS511052PPWR = _Hh3cS511052PPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1080)
)
_Hh3cS511052PPWRD_ObjectIdentity = ObjectIdentity
hh3cS511052PPWRD = _Hh3cS511052PPWRD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1081)
)
_Hh3cNSC1000_ObjectIdentity = ObjectIdentity
hh3cNSC1000 = _Hh3cNSC1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1082)
)
_Hh3cMS4308_ObjectIdentity = ObjectIdentity
hh3cMS4308 = _Hh3cMS4308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1083)
)
_Hh3cMS4308PWR_ObjectIdentity = ObjectIdentity
hh3cMS4308PWR = _Hh3cMS4308PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1084)
)
_Hh3cS513028TPEI_ObjectIdentity = ObjectIdentity
hh3cS513028TPEI = _Hh3cS513028TPEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1085)
)
_Hh3cS513052TPEI_ObjectIdentity = ObjectIdentity
hh3cS513052TPEI = _Hh3cS513052TPEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1086)
)
_Hh3cS513028TPPWREI_ObjectIdentity = ObjectIdentity
hh3cS513028TPPWREI = _Hh3cS513028TPPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1087)
)
_Hh3cS513052TPPWREI_ObjectIdentity = ObjectIdentity
hh3cS513052TPPWREI = _Hh3cS513052TPPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1088)
)
_Hh3csecpathF1020_ObjectIdentity = ObjectIdentity
hh3csecpathF1020 = _Hh3csecpathF1020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1089)
)
_Hh3csecpathF1030_ObjectIdentity = ObjectIdentity
hh3csecpathF1030 = _Hh3csecpathF1030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1090)
)
_Hh3csecpathF1050_ObjectIdentity = ObjectIdentity
hh3csecpathF1050 = _Hh3csecpathF1050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1091)
)
_Hh3csecpathF1060_ObjectIdentity = ObjectIdentity
hh3csecpathF1060 = _Hh3csecpathF1060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1092)
)
_Hh3csecpathF1070_ObjectIdentity = ObjectIdentity
hh3csecpathF1070 = _Hh3csecpathF1070_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1093)
)
_Hh3csecpathF1080_ObjectIdentity = ObjectIdentity
hh3csecpathF1080 = _Hh3csecpathF1080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1094)
)
_Hh3csecpathVMSGVLB1000_ObjectIdentity = ObjectIdentity
hh3csecpathVMSGVLB1000 = _Hh3csecpathVMSGVLB1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1095)
)
_Hh3cS5864F_ObjectIdentity = ObjectIdentity
hh3cS5864F = _Hh3cS5864F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1096)
)
_Hh3cS5864UF_ObjectIdentity = ObjectIdentity
hh3cS5864UF = _Hh3cS5864UF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1097)
)
_Hh3cS5864TF_ObjectIdentity = ObjectIdentity
hh3cS5864TF = _Hh3cS5864TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1098)
)
_Hh3cS6348F_ObjectIdentity = ObjectIdentity
hh3cS6348F = _Hh3cS6348F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1099)
)
_Hh3cS6348TF_ObjectIdentity = ObjectIdentity
hh3cS6348TF = _Hh3cS6348TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1100)
)
_Hh3cCR16006F_ObjectIdentity = ObjectIdentity
hh3cCR16006F = _Hh3cCR16006F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1101)
)
_Hh3cCR16010F_ObjectIdentity = ObjectIdentity
hh3cCR16010F = _Hh3cCR16010F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1102)
)
_Hh3cCR16014F_ObjectIdentity = ObjectIdentity
hh3cCR16014F = _Hh3cCR16014F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1103)
)
_Hh3cSecPathM9000Context_ObjectIdentity = ObjectIdentity
hh3cSecPathM9000Context = _Hh3cSecPathM9000Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1104)
)
_Hh3cICG3000SE_ObjectIdentity = ObjectIdentity
hh3cICG3000SE = _Hh3cICG3000SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1105)
)
_Hh3cS68004C_ObjectIdentity = ObjectIdentity
hh3cS68004C = _Hh3cS68004C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1106)
)
_Hh3cS68002C_ObjectIdentity = ObjectIdentity
hh3cS68002C = _Hh3cS68002C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1107)
)
_Hh3cSR8803F_ObjectIdentity = ObjectIdentity
hh3cSR8803F = _Hh3cSR8803F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1108)
)
_Hh3cSR8805F_ObjectIdentity = ObjectIdentity
hh3cSR8805F = _Hh3cSR8805F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1109)
)
_Hh3cSR8808F_ObjectIdentity = ObjectIdentity
hh3cSR8808F = _Hh3cSR8808F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1110)
)
_Hh3cSR8812F_ObjectIdentity = ObjectIdentity
hh3cSR8812F = _Hh3cSR8812F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1111)
)
_Hh3cS12516XAF_ObjectIdentity = ObjectIdentity
hh3cS12516XAF = _Hh3cS12516XAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1112)
)
_Hh3cvAC_ObjectIdentity = ObjectIdentity
hh3cvAC = _Hh3cvAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1113)
)
_Hh3cWX8700_ObjectIdentity = ObjectIdentity
hh3cWX8700 = _Hh3cWX8700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1114)
)
_Hh3cS556030FEI_ObjectIdentity = ObjectIdentity
hh3cS556030FEI = _Hh3cS556030FEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1115)
)
_Hh3cS5530CEID_ObjectIdentity = ObjectIdentity
hh3cS5530CEID = _Hh3cS5530CEID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1116)
)
_Hh3cS5554CEID_ObjectIdentity = ObjectIdentity
hh3cS5554CEID = _Hh3cS5554CEID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1117)
)
_Hh3cS5530CPWREID_ObjectIdentity = ObjectIdentity
hh3cS5530CPWREID = _Hh3cS5530CPWREID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1118)
)
_Hh3cS5554CPWREID_ObjectIdentity = ObjectIdentity
hh3cS5554CPWREID = _Hh3cS5554CPWREID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1119)
)
_Hh3cS5530FEID_ObjectIdentity = ObjectIdentity
hh3cS5530FEID = _Hh3cS5530FEID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1120)
)
_Hh3cS513028SSI_ObjectIdentity = ObjectIdentity
hh3cS513028SSI = _Hh3cS513028SSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1121)
)
_Hh3cS513052SSI_ObjectIdentity = ObjectIdentity
hh3cS513052SSI = _Hh3cS513052SSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1122)
)
_Hh3cS513028FSI_ObjectIdentity = ObjectIdentity
hh3cS513028FSI = _Hh3cS513028FSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1123)
)
_Hh3cS556028SSI_ObjectIdentity = ObjectIdentity
hh3cS556028SSI = _Hh3cS556028SSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1124)
)
_Hh3cS556052SSI_ObjectIdentity = ObjectIdentity
hh3cS556052SSI = _Hh3cS556052SSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1125)
)
_Hh3cS556028FSI_ObjectIdentity = ObjectIdentity
hh3cS556028FSI = _Hh3cS556028FSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1126)
)
_Hh3cLA4608E_ObjectIdentity = ObjectIdentity
hh3cLA4608E = _Hh3cLA4608E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1127)
)
_Hh3cWA4320ACN_ObjectIdentity = ObjectIdentity
hh3cWA4320ACN = _Hh3cWA4320ACN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1128)
)
_Hh3cWA4320iACN_ObjectIdentity = ObjectIdentity
hh3cWA4320iACN = _Hh3cWA4320iACN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1129)
)
_Hh3cWA4320iX_ObjectIdentity = ObjectIdentity
hh3cWA4320iX = _Hh3cWA4320iX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1130)
)
_Hh3cWA4320TS_ObjectIdentity = ObjectIdentity
hh3cWA4320TS = _Hh3cWA4320TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1131)
)
_Hh3cWA4320TQ_ObjectIdentity = ObjectIdentity
hh3cWA4320TQ = _Hh3cWA4320TQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1132)
)
_Hh3cWA4320HACN_ObjectIdentity = ObjectIdentity
hh3cWA4320HACN = _Hh3cWA4320HACN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1133)
)
_Hh3cS10506_ObjectIdentity = ObjectIdentity
hh3cS10506 = _Hh3cS10506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1134)
)
_Hh3cS10510_ObjectIdentity = ObjectIdentity
hh3cS10510 = _Hh3cS10510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1135)
)
_Hh3cS7606X_ObjectIdentity = ObjectIdentity
hh3cS7606X = _Hh3cS7606X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1136)
)
_Hh3cS7610X_ObjectIdentity = ObjectIdentity
hh3cS7610X = _Hh3cS7610X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1137)
)
_Hh3cMSR930AC_ObjectIdentity = ObjectIdentity
hh3cMSR930AC = _Hh3cMSR930AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1138)
)
_Hh3cMSR930ACWiNet_ObjectIdentity = ObjectIdentity
hh3cMSR930ACWiNet = _Hh3cMSR930ACWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1139)
)
_Hh3cSecPathACG1000E_ObjectIdentity = ObjectIdentity
hh3cSecPathACG1000E = _Hh3cSecPathACG1000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1140)
)
_Hh3cSecPathACG1000A_ObjectIdentity = ObjectIdentity
hh3cSecPathACG1000A = _Hh3cSecPathACG1000A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1141)
)
_Hh3cSecPathACG1000M_ObjectIdentity = ObjectIdentity
hh3cSecPathACG1000M = _Hh3cSecPathACG1000M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1142)
)
_Hh3cSecPathACG1000S_ObjectIdentity = ObjectIdentity
hh3cSecPathACG1000S = _Hh3cSecPathACG1000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1143)
)
_Hh3cSecPathACG1000C_ObjectIdentity = ObjectIdentity
hh3cSecPathACG1000C = _Hh3cSecPathACG1000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1144)
)
_Hh3cVBRAS1000_ObjectIdentity = ObjectIdentity
hh3cVBRAS1000 = _Hh3cVBRAS1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1145)
)
_Hh3cVSR1000P_ObjectIdentity = ObjectIdentity
hh3cVSR1000P = _Hh3cVSR1000P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1146)
)
_Hh3cBRAS1000P_ObjectIdentity = ObjectIdentity
hh3cBRAS1000P = _Hh3cBRAS1000P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1147)
)
_Hh3cS12508XAF_ObjectIdentity = ObjectIdentity
hh3cS12508XAF = _Hh3cS12508XAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1148)
)
_Hh3cLA3616SGM_ObjectIdentity = ObjectIdentity
hh3cLA3616SGM = _Hh3cLA3616SGM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1149)
)
_Hh3cLA3616SGT_ObjectIdentity = ObjectIdentity
hh3cLA3616SGT = _Hh3cLA3616SGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1150)
)
_Hh3cLA3616EGM_ObjectIdentity = ObjectIdentity
hh3cLA3616EGM = _Hh3cLA3616EGM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1151)
)
_Hh3cWAP722E_ObjectIdentity = ObjectIdentity
hh3cWAP722E = _Hh3cWAP722E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1152)
)
_Hh3cWAP722_ObjectIdentity = ObjectIdentity
hh3cWAP722 = _Hh3cWAP722_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1153)
)
_Hh3cER2100n_ObjectIdentity = ObjectIdentity
hh3cER2100n = _Hh3cER2100n_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1154)
)
_Hh3cER2100V2_ObjectIdentity = ObjectIdentity
hh3cER2100V2 = _Hh3cER2100V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1155)
)
_Hh3cWX5560H_ObjectIdentity = ObjectIdentity
hh3cWX5560H = _Hh3cWX5560H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1156)
)
_Hh3cWX5580H_ObjectIdentity = ObjectIdentity
hh3cWX5580H = _Hh3cWX5580H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1157)
)
_Hh3cWAP621_ObjectIdentity = ObjectIdentity
hh3cWAP621 = _Hh3cWAP621_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1158)
)
_Hh3cMSR810W_ObjectIdentity = ObjectIdentity
hh3cMSR810W = _Hh3cMSR810W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1159)
)
_Hh3cER3260G2_ObjectIdentity = ObjectIdentity
hh3cER3260G2 = _Hh3cER3260G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1160)
)
_Hh3cER5100G2_ObjectIdentity = ObjectIdentity
hh3cER5100G2 = _Hh3cER5100G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1161)
)
_Hh3cER5200G2_ObjectIdentity = ObjectIdentity
hh3cER5200G2 = _Hh3cER5200G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1162)
)
_Hh3cER6300G2_ObjectIdentity = ObjectIdentity
hh3cER6300G2 = _Hh3cER6300G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1163)
)
_Hh3cER8300G2_ObjectIdentity = ObjectIdentity
hh3cER8300G2 = _Hh3cER8300G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1164)
)
_Hh3cER8300G2X_ObjectIdentity = ObjectIdentity
hh3cER8300G2X = _Hh3cER8300G2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1165)
)
_Hh3cS99004F_ObjectIdentity = ObjectIdentity
hh3cS99004F = _Hh3cS99004F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1166)
)
_Hh3cS990010F_ObjectIdentity = ObjectIdentity
hh3cS990010F = _Hh3cS990010F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1167)
)
_Hh3cSecBladeLSU1ADECEA01_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSU1ADECEA01 = _Hh3cSecBladeLSU1ADECEA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1168)
)
_Hh3cSecBladeLSXM1ADECEA1_ObjectIdentity = ObjectIdentity
hh3cSecBladeLSXM1ADECEA1 = _Hh3cSecBladeLSXM1ADECEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1169)
)
_Hh3cS69002F_ObjectIdentity = ObjectIdentity
hh3cS69002F = _Hh3cS69002F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1170)
)
_Hh3cS69004F_ObjectIdentity = ObjectIdentity
hh3cS69004F = _Hh3cS69004F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1171)
)
_Hh3cS6348SF_ObjectIdentity = ObjectIdentity
hh3cS6348SF = _Hh3cS6348SF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1172)
)
_Hh3cS6364F_ObjectIdentity = ObjectIdentity
hh3cS6364F = _Hh3cS6364F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1173)
)
_Hh3cS5848F_ObjectIdentity = ObjectIdentity
hh3cS5848F = _Hh3cS5848F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1174)
)
_Hh3cS1808G_ObjectIdentity = ObjectIdentity
hh3cS1808G = _Hh3cS1808G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1175)
)
_Hh3cS1824G_ObjectIdentity = ObjectIdentity
hh3cS1824G = _Hh3cS1824G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1176)
)
_Hh3cS1848G_ObjectIdentity = ObjectIdentity
hh3cS1848G = _Hh3cS1848G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1177)
)
_Hh3cSecPathACG1010_ObjectIdentity = ObjectIdentity
hh3cSecPathACG1010 = _Hh3cSecPathACG1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1178)
)
_Hh3cSecPathACG1020_ObjectIdentity = ObjectIdentity
hh3cSecPathACG1020 = _Hh3cSecPathACG1020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1179)
)
_Hh3cSecPathACG1030_ObjectIdentity = ObjectIdentity
hh3cSecPathACG1030 = _Hh3cSecPathACG1030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1180)
)
_Hh3cSecPathACG1040_ObjectIdentity = ObjectIdentity
hh3cSecPathACG1040 = _Hh3cSecPathACG1040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1181)
)
_Hh3cWX3510H_ObjectIdentity = ObjectIdentity
hh3cWX3510H = _Hh3cWX3510H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1182)
)
_Hh3cWX3520H_ObjectIdentity = ObjectIdentity
hh3cWX3520H = _Hh3cWX3520H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1183)
)
_Hh3cWX3540H_ObjectIdentity = ObjectIdentity
hh3cWX3540H = _Hh3cWX3540H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1184)
)
_Hh3cWX5540H_ObjectIdentity = ObjectIdentity
hh3cWX5540H = _Hh3cWX5540H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1185)
)
_Hh3cLA3608E_ObjectIdentity = ObjectIdentity
hh3cLA3608E = _Hh3cLA3608E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1186)
)
_Hh3cLA3608EDB_ObjectIdentity = ObjectIdentity
hh3cLA3608EDB = _Hh3cLA3608EDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1187)
)
_Hh3cS513030SHI_ObjectIdentity = ObjectIdentity
hh3cS513030SHI = _Hh3cS513030SHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1188)
)
_Hh3cS513054SHI_ObjectIdentity = ObjectIdentity
hh3cS513054SHI = _Hh3cS513054SHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1189)
)
_Hh3cS513030CHI_ObjectIdentity = ObjectIdentity
hh3cS513030CHI = _Hh3cS513030CHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1190)
)
_Hh3cS513054CHI_ObjectIdentity = ObjectIdentity
hh3cS513054CHI = _Hh3cS513054CHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1191)
)
_Hh3cS513030CPWRHI_ObjectIdentity = ObjectIdentity
hh3cS513030CPWRHI = _Hh3cS513030CPWRHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1192)
)
_Hh3cS513054CPWRHI_ObjectIdentity = ObjectIdentity
hh3cS513054CPWRHI = _Hh3cS513054CPWRHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1193)
)
_Hh3cS513054QSHI_ObjectIdentity = ObjectIdentity
hh3cS513054QSHI = _Hh3cS513054QSHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1194)
)
_Hh3cS513030FHI_ObjectIdentity = ObjectIdentity
hh3cS513030FHI = _Hh3cS513030FHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1195)
)
_Hh3cS12516FAF_ObjectIdentity = ObjectIdentity
hh3cS12516FAF = _Hh3cS12516FAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1196)
)
_Hh3cS12508FAF_ObjectIdentity = ObjectIdentity
hh3cS12508FAF = _Hh3cS12508FAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1197)
)
_Hh3cS12504XAF_ObjectIdentity = ObjectIdentity
hh3cS12504XAF = _Hh3cS12504XAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1198)
)
_Hh3cS12504FAF_ObjectIdentity = ObjectIdentity
hh3cS12504FAF = _Hh3cS12504FAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1199)
)
_Hh3cMS410010TP_ObjectIdentity = ObjectIdentity
hh3cMS410010TP = _Hh3cMS410010TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1200)
)
_Hh3cMS410010TPPWR_ObjectIdentity = ObjectIdentity
hh3cMS410010TPPWR = _Hh3cMS410010TPPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1201)
)
_Hh3cMS410026TP_ObjectIdentity = ObjectIdentity
hh3cMS410026TP = _Hh3cMS410026TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1202)
)
_Hh3cMS410026TPPWR_ObjectIdentity = ObjectIdentity
hh3cMS410026TPPWR = _Hh3cMS410026TPPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1203)
)
_Hh3cMS430052P_ObjectIdentity = ObjectIdentity
hh3cMS430052P = _Hh3cMS430052P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1204)
)
_Hh3cMS430028P_ObjectIdentity = ObjectIdentity
hh3cMS430028P = _Hh3cMS430028P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1205)
)
_Hh3cIE410012TP_ObjectIdentity = ObjectIdentity
hh3cIE410012TP = _Hh3cIE410012TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1206)
)
_Hh3cIE410020TP_ObjectIdentity = ObjectIdentity
hh3cIE410020TP = _Hh3cIE410020TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1207)
)
_Hh3cIE410028F_ObjectIdentity = ObjectIdentity
hh3cIE410028F = _Hh3cIE410028F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1208)
)
_Hh3cIE430028P_ObjectIdentity = ObjectIdentity
hh3cIE430028P = _Hh3cIE430028P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1209)
)
_Hh3cS680054QF_ObjectIdentity = ObjectIdentity
hh3cS680054QF = _Hh3cS680054QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1210)
)
_Hh3cMS432028S_ObjectIdentity = ObjectIdentity
hh3cMS432028S = _Hh3cMS432028S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1211)
)
_Hh3cMS432052S_ObjectIdentity = ObjectIdentity
hh3cMS432052S = _Hh3cMS432052S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1212)
)
_Hh3cMS432028F_ObjectIdentity = ObjectIdentity
hh3cMS432028F = _Hh3cMS432028F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1213)
)
_Hh3cMS432028SPWR_ObjectIdentity = ObjectIdentity
hh3cMS432028SPWR = _Hh3cMS432028SPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1214)
)
_Hh3cMS452028TP_ObjectIdentity = ObjectIdentity
hh3cMS452028TP = _Hh3cMS452028TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1215)
)
_Hh3cMS452030F_ObjectIdentity = ObjectIdentity
hh3cMS452030F = _Hh3cMS452030F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1216)
)
_Hh3cLA4310_ObjectIdentity = ObjectIdentity
hh3cLA4310 = _Hh3cLA4310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1217)
)
_Hh3cLA4310V_ObjectIdentity = ObjectIdentity
hh3cLA4310V = _Hh3cLA4310V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1218)
)
_Hh3cLA4320_ObjectIdentity = ObjectIdentity
hh3cLA4320 = _Hh3cLA4320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1219)
)
_Hh3cLA4320V_ObjectIdentity = ObjectIdentity
hh3cLA4320V = _Hh3cLA4320V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1220)
)
_Hh3cWA4320X_ObjectIdentity = ObjectIdentity
hh3cWA4320X = _Hh3cWA4320X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1221)
)
_Hh3cLA4320X_ObjectIdentity = ObjectIdentity
hh3cLA4320X = _Hh3cLA4320X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1222)
)
_Hh3cSecBlade4NSQM1FWDFG0_ObjectIdentity = ObjectIdentity
hh3cSecBlade4NSQM1FWDFG0 = _Hh3cSecBlade4NSQM1FWDFG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1223)
)
_Hh3cWX5510EV7_ObjectIdentity = ObjectIdentity
hh3cWX5510EV7 = _Hh3cWX5510EV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1224)
)
_Hh3cWX5540EV7_ObjectIdentity = ObjectIdentity
hh3cWX5540EV7 = _Hh3cWX5540EV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1225)
)
_Hh3cSecPathL1000E_ObjectIdentity = ObjectIdentity
hh3cSecPathL1000E = _Hh3cSecPathL1000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1226)
)
_Hh3cSecPathL1000M_ObjectIdentity = ObjectIdentity
hh3cSecPathL1000M = _Hh3cSecPathL1000M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1227)
)
_Hh3cSecPathL1000S_ObjectIdentity = ObjectIdentity
hh3cSecPathL1000S = _Hh3cSecPathL1000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1228)
)
_Hh3cSecPathF5000Context_ObjectIdentity = ObjectIdentity
hh3cSecPathF5000Context = _Hh3cSecPathF5000Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1229)
)
_Hh3cSecPathF1000Context_ObjectIdentity = ObjectIdentity
hh3cSecPathF1000Context = _Hh3cSecPathF1000Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1230)
)
_Hh3cSecPathL5000Context_ObjectIdentity = ObjectIdentity
hh3cSecPathL5000Context = _Hh3cSecPathL5000Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1231)
)
_Hh3cSecPathL1000Context_ObjectIdentity = ObjectIdentity
hh3cSecPathL1000Context = _Hh3cSecPathL1000Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1232)
)
_Hh3cWA4320TQV_ObjectIdentity = ObjectIdentity
hh3cWA4320TQV = _Hh3cWA4320TQV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1233)
)
_Hh3cMSR810WDB_ObjectIdentity = ObjectIdentity
hh3cMSR810WDB = _Hh3cMSR810WDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1234)
)
_Hh3cMSR810LM_ObjectIdentity = ObjectIdentity
hh3cMSR810LM = _Hh3cMSR810LM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1235)
)
_Hh3cMSR810WLM_ObjectIdentity = ObjectIdentity
hh3cMSR810WLM = _Hh3cMSR810WLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1236)
)
_Hh3cS682032H_ObjectIdentity = ObjectIdentity
hh3cS682032H = _Hh3cS682032H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1237)
)
_Hh3cS682054HF_ObjectIdentity = ObjectIdentity
hh3cS682054HF = _Hh3cS682054HF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1238)
)
_Hh3cMSR5620_ObjectIdentity = ObjectIdentity
hh3cMSR5620 = _Hh3cMSR5620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1239)
)
_Hh3cMSR3620DP_ObjectIdentity = ObjectIdentity
hh3cMSR3620DP = _Hh3cMSR3620DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1240)
)
_Hh3cMSR810WWiNet_ObjectIdentity = ObjectIdentity
hh3cMSR810WWiNet = _Hh3cMSR810WWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1241)
)
_Hh3cMSR810LMWiNet_ObjectIdentity = ObjectIdentity
hh3cMSR810LMWiNet = _Hh3cMSR810LMWiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1242)
)
_Hh3cRA100AC_ObjectIdentity = ObjectIdentity
hh3cRA100AC = _Hh3cRA100AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1243)
)
_Hh3cMSR360028WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR360028WiNet = _Hh3cMSR360028WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1244)
)
_Hh3cMSR3620WiNet_ObjectIdentity = ObjectIdentity
hh3cMSR3620WiNet = _Hh3cMSR3620WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1245)
)
_Hh3cS680054QT_ObjectIdentity = ObjectIdentity
hh3cS680054QT = _Hh3cS680054QT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1246)
)
_Hh3cS12504S_ObjectIdentity = ObjectIdentity
hh3cS12504S = _Hh3cS12504S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1247)
)
_Hh3cS12506S_ObjectIdentity = ObjectIdentity
hh3cS12506S = _Hh3cS12506S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1248)
)
_Hh3cS12510S_ObjectIdentity = ObjectIdentity
hh3cS12510S = _Hh3cS12510S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1249)
)
_Hh3cS12508S_ObjectIdentity = ObjectIdentity
hh3cS12508S = _Hh3cS12508S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1250)
)
_Hh3cS12512S_ObjectIdentity = ObjectIdentity
hh3cS12512S = _Hh3cS12512S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1251)
)
_Hh3cS515024SPWREI_ObjectIdentity = ObjectIdentity
hh3cS515024SPWREI = _Hh3cS515024SPWREI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1252)
)
_Hh3cS5150X16SEI_ObjectIdentity = ObjectIdentity
hh3cS5150X16SEI = _Hh3cS5150X16SEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1253)
)
_Hh3cS5150X16STEI_ObjectIdentity = ObjectIdentity
hh3cS5150X16STEI = _Hh3cS5150X16STEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1254)
)
_Hh3cSecPathF100AG2_ObjectIdentity = ObjectIdentity
hh3cSecPathF100AG2 = _Hh3cSecPathF100AG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1255)
)
_Hh3cSecPathF1000CG2_ObjectIdentity = ObjectIdentity
hh3cSecPathF1000CG2 = _Hh3cSecPathF1000CG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1256)
)
_Hh3cUISM831048G_ObjectIdentity = ObjectIdentity
hh3cUISM831048G = _Hh3cUISM831048G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1257)
)
_Hh3cUISM832048XG_ObjectIdentity = ObjectIdentity
hh3cUISM832048XG = _Hh3cUISM832048XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1258)
)
_Hh3cUISM6300XLG_ObjectIdentity = ObjectIdentity
hh3cUISM6300XLG = _Hh3cUISM6300XLG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1259)
)
_Hh3cMSR810_ObjectIdentity = ObjectIdentity
hh3cMSR810 = _Hh3cMSR810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1260)
)
_Hh3cSecPathW2001_ObjectIdentity = ObjectIdentity
hh3cSecPathW2001 = _Hh3cSecPathW2001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1261)
)
_Hh3cSecPathW2005_ObjectIdentity = ObjectIdentity
hh3cSecPathW2005 = _Hh3cSecPathW2005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1262)
)
_Hh3cSecPathW2010_ObjectIdentity = ObjectIdentity
hh3cSecPathW2010 = _Hh3cSecPathW2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1263)
)
_Hh3cSecPathW2020_ObjectIdentity = ObjectIdentity
hh3cSecPathW2020 = _Hh3cSecPathW2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1264)
)
_Hh3cSecPathW2040_ObjectIdentity = ObjectIdentity
hh3cSecPathW2040 = _Hh3cSecPathW2040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1265)
)
_Hh3cSecPathW2080_ObjectIdentity = ObjectIdentity
hh3cSecPathW2080 = _Hh3cSecPathW2080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1266)
)
_Hh3cSecPathW2200_ObjectIdentity = ObjectIdentity
hh3cSecPathW2200 = _Hh3cSecPathW2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1267)
)
_Hh3cSecPathW1020D_ObjectIdentity = ObjectIdentity
hh3cSecPathW1020D = _Hh3cSecPathW1020D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1268)
)
_Hh3cSecPathW1040D_ObjectIdentity = ObjectIdentity
hh3cSecPathW1040D = _Hh3cSecPathW1040D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1269)
)
_Hh3cSecPathW1200D_ObjectIdentity = ObjectIdentity
hh3cSecPathW1200D = _Hh3cSecPathW1200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1270)
)
_Hh3cSecPathA2020_ObjectIdentity = ObjectIdentity
hh3cSecPathA2020 = _Hh3cSecPathA2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1271)
)
_Hh3cSecPathA2100_ObjectIdentity = ObjectIdentity
hh3cSecPathA2100 = _Hh3cSecPathA2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1272)
)
_Hh3cSecPathD2020_ObjectIdentity = ObjectIdentity
hh3cSecPathD2020 = _Hh3cSecPathD2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1273)
)
_Hh3cSecPathD2050_ObjectIdentity = ObjectIdentity
hh3cSecPathD2050 = _Hh3cSecPathD2050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1274)
)
_Hh3cS556034CEI_ObjectIdentity = ObjectIdentity
hh3cS556034CEI = _Hh3cS556034CEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1275)
)
_Hh3cS513034CHI_ObjectIdentity = ObjectIdentity
hh3cS513034CHI = _Hh3cS513034CHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1276)
)
_Hh3cMS412026TP_ObjectIdentity = ObjectIdentity
hh3cMS412026TP = _Hh3cMS412026TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1277)
)
_Hh3cWA4330ACN_ObjectIdentity = ObjectIdentity
hh3cWA4330ACN = _Hh3cWA4330ACN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1278)
)
_Hh3cMS4320S28F_ObjectIdentity = ObjectIdentity
hh3cMS4320S28F = _Hh3cMS4320S28F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1279)
)
_Hh3cMS4320S28P_ObjectIdentity = ObjectIdentity
hh3cMS4320S28P = _Hh3cMS4320S28P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1280)
)
_Hh3cMS452028S_ObjectIdentity = ObjectIdentity
hh3cMS452028S = _Hh3cMS452028S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1281)
)
_Hh3cSecBlade3Context_ObjectIdentity = ObjectIdentity
hh3cSecBlade3Context = _Hh3cSecBlade3Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1282)
)
_Hh3cMSR2630R_ObjectIdentity = ObjectIdentity
hh3cMSR2630R = _Hh3cMSR2630R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1283)
)
_Hh3cMSR3610ACR_ObjectIdentity = ObjectIdentity
hh3cMSR3610ACR = _Hh3cMSR3610ACR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1284)
)
_Hh3cMSR3620ACR_ObjectIdentity = ObjectIdentity
hh3cMSR3620ACR = _Hh3cMSR3620ACR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1285)
)
_Hh3cMSR3640R_ObjectIdentity = ObjectIdentity
hh3cMSR3640R = _Hh3cMSR3640R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1286)
)
_Hh3cMSR3660R_ObjectIdentity = ObjectIdentity
hh3cMSR3660R = _Hh3cMSR3660R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1287)
)
_Hh3cMSR5660R_ObjectIdentity = ObjectIdentity
hh3cMSR5660R = _Hh3cMSR5660R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1288)
)
_Hh3cMSR5680R_ObjectIdentity = ObjectIdentity
hh3cMSR5680R = _Hh3cMSR5680R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1289)
)
_Hh3cMSR930R_ObjectIdentity = ObjectIdentity
hh3cMSR930R = _Hh3cMSR930R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1290)
)
_Hh3cMSR930WR_ObjectIdentity = ObjectIdentity
hh3cMSR930WR = _Hh3cMSR930WR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1291)
)
_Hh3cMSR260010R_ObjectIdentity = ObjectIdentity
hh3cMSR260010R = _Hh3cMSR260010R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1292)
)
_Hh3cWX3010EV7_ObjectIdentity = ObjectIdentity
hh3cWX3010EV7 = _Hh3cWX3010EV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1293)
)
_Hh3cWX3024EV7_ObjectIdentity = ObjectIdentity
hh3cWX3024EV7 = _Hh3cWX3024EV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1294)
)
_Hh3cWCMX20_ObjectIdentity = ObjectIdentity
hh3cWCMX20 = _Hh3cWCMX20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1295)
)
_Hh3cS556032CHI_ObjectIdentity = ObjectIdentity
hh3cS556032CHI = _Hh3cS556032CHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1296)
)
_Hh3cS556056CHI_ObjectIdentity = ObjectIdentity
hh3cS556056CHI = _Hh3cS556056CHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1297)
)
_Hh3cS556056CPWRHI_ObjectIdentity = ObjectIdentity
hh3cS556056CPWRHI = _Hh3cS556056CPWRHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1298)
)
_Hh3cS12502XAF_ObjectIdentity = ObjectIdentity
hh3cS12502XAF = _Hh3cS12502XAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1299)
)
_Hh3cNS228_ObjectIdentity = ObjectIdentity
hh3cNS228 = _Hh3cNS228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1300)
)
_Hh3cNS252_ObjectIdentity = ObjectIdentity
hh3cNS252 = _Hh3cNS252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1301)
)
_Hh3cSecBladeFW_ObjectIdentity = ObjectIdentity
hh3cSecBladeFW = _Hh3cSecBladeFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1302)
)
_Hh3cSecBladeADE_ObjectIdentity = ObjectIdentity
hh3cSecBladeADE = _Hh3cSecBladeADE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1303)
)
_Hh3cSecBladeIIILSUM1FWCEAB0_ObjectIdentity = ObjectIdentity
hh3cSecBladeIIILSUM1FWCEAB0 = _Hh3cSecBladeIIILSUM1FWCEAB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1304)
)
_Hh3cS513028PSEI_ObjectIdentity = ObjectIdentity
hh3cS513028PSEI = _Hh3cS513028PSEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1305)
)
_Hh3cS7506EX_ObjectIdentity = ObjectIdentity
hh3cS7506EX = _Hh3cS7506EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1306)
)
_Hh3cS7510EX_ObjectIdentity = ObjectIdentity
hh3cS7510EX = _Hh3cS7510EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1307)
)
_Hh3cS7504EXS_ObjectIdentity = ObjectIdentity
hh3cS7504EXS = _Hh3cS7504EXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1308)
)
_Hh3cS7502EXS_ObjectIdentity = ObjectIdentity
hh3cS7502EXS = _Hh3cS7502EXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1309)
)
_Hh3cWA4320ACNPI_ObjectIdentity = ObjectIdentity
hh3cWA4320ACNPI = _Hh3cWA4320ACNPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1310)
)
_Hh3cWA4320ACNSI_ObjectIdentity = ObjectIdentity
hh3cWA4320ACNSI = _Hh3cWA4320ACNSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1, 1311)
)
_HpSwitch_ObjectIdentity = ObjectIdentity
hpSwitch = _HpSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1)
)
_Hp7502_ObjectIdentity = ObjectIdentity
hp7502 = _Hp7502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 1)
)
_Hp7503S_ObjectIdentity = ObjectIdentity
hp7503S = _Hp7503S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 2)
)
_Hp7503_ObjectIdentity = ObjectIdentity
hp7503 = _Hp7503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 3)
)
_Hp7506_ObjectIdentity = ObjectIdentity
hp7506 = _Hp7506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 4)
)
_Hp7506V_ObjectIdentity = ObjectIdentity
hp7506V = _Hp7506V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 5)
)
_Hp7510_ObjectIdentity = ObjectIdentity
hp7510 = _Hp7510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 6)
)
_HpA36002POLT_ObjectIdentity = ObjectIdentity
hpA36002POLT = _HpA36002POLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 7)
)
_HpV190524_ObjectIdentity = ObjectIdentity
hpV190524 = _HpV190524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 8)
)
_HpV190524POE_ObjectIdentity = ObjectIdentity
hpV190524POE = _HpV190524POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 9)
)
_HpV190548_ObjectIdentity = ObjectIdentity
hpV190548 = _HpV190548_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 10)
)
_HpA512016GSI_ObjectIdentity = ObjectIdentity
hpA512016GSI = _HpA512016GSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 11)
)
_HpA512024GSI_ObjectIdentity = ObjectIdentity
hpA512024GSI = _HpA512024GSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 12)
)
_HpA512048GSI_ObjectIdentity = ObjectIdentity
hpA512048GSI = _HpA512048GSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 13)
)
_HpA512024GPPOESI_ObjectIdentity = ObjectIdentity
hpA512024GPPOESI = _HpA512024GPPOESI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 14)
)
_HpA512024GPOESI_ObjectIdentity = ObjectIdentity
hpA512024GPOESI = _HpA512024GPOESI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 15)
)
_HpA580024G_ObjectIdentity = ObjectIdentity
hpA580024G = _HpA580024G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 16)
)
_HpA580024GPoEPlus_ObjectIdentity = ObjectIdentity
hpA580024GPoEPlus = _HpA580024GPoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 17)
)
_HpA580048G_ObjectIdentity = ObjectIdentity
hpA580048G = _HpA580048G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 18)
)
_HpA580048GPoEPlus_ObjectIdentity = ObjectIdentity
hpA580048GPoEPlus = _HpA580048GPoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 19)
)
_HpA580024GSFP_ObjectIdentity = ObjectIdentity
hpA580024GSFP = _HpA580024GSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 20)
)
_HpA580048GPoEPlus2SLOT_ObjectIdentity = ObjectIdentity
hpA580048GPoEPlus2SLOT = _HpA580048GPoEPlus2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 21)
)
_HpA5820X14XGSFPPlus2SLOT_ObjectIdentity = ObjectIdentity
hpA5820X14XGSFPPlus2SLOT = _HpA5820X14XGSFPPlus2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 22)
)
_HpA5820X24XGSFPPlus_ObjectIdentity = ObjectIdentity
hpA5820X24XGSFPPlus = _HpA5820X24XGSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 23)
)
_HpA550024GEI2SLOT_ObjectIdentity = ObjectIdentity
hpA550024GEI2SLOT = _HpA550024GEI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 24)
)
_HpA550048GEI2SLOT_ObjectIdentity = ObjectIdentity
hpA550048GEI2SLOT = _HpA550048GEI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 25)
)
_HpA550024GPoEPlusEI2SLOT_ObjectIdentity = ObjectIdentity
hpA550024GPoEPlusEI2SLOT = _HpA550024GPoEPlusEI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 26)
)
_HpA550048GPoEPlusEI2SLOT_ObjectIdentity = ObjectIdentity
hpA550048GPoEPlusEI2SLOT = _HpA550048GPoEPlusEI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 27)
)
_HpA550024GSFPEI2SLOT_ObjectIdentity = ObjectIdentity
hpA550024GSFPEI2SLOT = _HpA550024GSFPEI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 28)
)
_HpA550024GSI2SLOT_ObjectIdentity = ObjectIdentity
hpA550024GSI2SLOT = _HpA550024GSI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 29)
)
_HpA550048GSI2SLOT_ObjectIdentity = ObjectIdentity
hpA550048GSI2SLOT = _HpA550048GSI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 30)
)
_HpA550024GPoEPlusSI2SLOT_ObjectIdentity = ObjectIdentity
hpA550024GPoEPlusSI2SLOT = _HpA550024GPoEPlusSI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 31)
)
_HpA550048GPoEPlusSI2SLOT_ObjectIdentity = ObjectIdentity
hpA550048GPoEPlusSI2SLOT = _HpA550048GPoEPlusSI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 32)
)
_HpA512024GEI2SLOT_ObjectIdentity = ObjectIdentity
hpA512024GEI2SLOT = _HpA512024GEI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 33)
)
_HpA512048GEI2SLOT_ObjectIdentity = ObjectIdentity
hpA512048GEI2SLOT = _HpA512048GEI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 34)
)
_HpA512024GPoEPlusEI2SLOT_ObjectIdentity = ObjectIdentity
hpA512024GPoEPlusEI2SLOT = _HpA512024GPoEPlusEI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 35)
)
_HpA512048GPoEPlusEI2SLOT_ObjectIdentity = ObjectIdentity
hpA512048GPoEPlusEI2SLOT = _HpA512048GPoEPlusEI2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 36)
)
_HpA512024GEI_ObjectIdentity = ObjectIdentity
hpA512024GEI = _HpA512024GEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 37)
)
_HpA512048GEI_ObjectIdentity = ObjectIdentity
hpA512048GEI = _HpA512048GEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 38)
)
_Hp9505_ObjectIdentity = ObjectIdentity
hp9505 = _Hp9505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 39)
)
_Hp9508V_ObjectIdentity = ObjectIdentity
hp9508V = _Hp9508V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 40)
)
_Hp9508_ObjectIdentity = ObjectIdentity
hp9508 = _Hp9508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 41)
)
_Hp9512_ObjectIdentity = ObjectIdentity
hp9512 = _Hp9512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 42)
)
_Hp12508_ObjectIdentity = ObjectIdentity
hp12508 = _Hp12508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 43)
)
_Hp12518_ObjectIdentity = ObjectIdentity
hp12518 = _Hp12518_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 44)
)
_Hp12504AC_ObjectIdentity = ObjectIdentity
hp12504AC = _Hp12504AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 45)
)
_HpA5800AF48G_ObjectIdentity = ObjectIdentity
hpA5800AF48G = _HpA5800AF48G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 46)
)
_HpA5820AF24XG_ObjectIdentity = ObjectIdentity
hpA5820AF24XG = _HpA5820AF24XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 47)
)
_Hp6125GXG_ObjectIdentity = ObjectIdentity
hp6125GXG = _Hp6125GXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 51)
)
_HpA31008SI_ObjectIdentity = ObjectIdentity
hpA31008SI = _HpA31008SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 52)
)
_HpA310016SI_ObjectIdentity = ObjectIdentity
hpA310016SI = _HpA310016SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 53)
)
_HpA310024SI_ObjectIdentity = ObjectIdentity
hpA310024SI = _HpA310024SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 54)
)
_HpA31008EI_ObjectIdentity = ObjectIdentity
hpA31008EI = _HpA31008EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 55)
)
_HpA310016EI_ObjectIdentity = ObjectIdentity
hpA310016EI = _HpA310016EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 56)
)
_HpA310024EI_ObjectIdentity = ObjectIdentity
hpA310024EI = _HpA310024EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 57)
)
_HpA31008POEEI_ObjectIdentity = ObjectIdentity
hpA31008POEEI = _HpA31008POEEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 58)
)
_HpA310016POEEI_ObjectIdentity = ObjectIdentity
hpA310016POEEI = _HpA310016POEEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 59)
)
_HpA310024POEEI_ObjectIdentity = ObjectIdentity
hpA310024POEEI = _HpA310024POEEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 60)
)
_HpA580024GTAA_ObjectIdentity = ObjectIdentity
hpA580024GTAA = _HpA580024GTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 61)
)
_HpA580024GPoEPlusTAA_ObjectIdentity = ObjectIdentity
hpA580024GPoEPlusTAA = _HpA580024GPoEPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 62)
)
_HpA580024GSFPTAA_ObjectIdentity = ObjectIdentity
hpA580024GSFPTAA = _HpA580024GSFPTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 63)
)
_HpA580048GTAA_ObjectIdentity = ObjectIdentity
hpA580048GTAA = _HpA580048GTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 64)
)
_HpA580048GPoEPlusTAA2SLOT_ObjectIdentity = ObjectIdentity
hpA580048GPoEPlusTAA2SLOT = _HpA580048GPoEPlusTAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 65)
)
_HpA580048GPoEPlusTAA_ObjectIdentity = ObjectIdentity
hpA580048GPoEPlusTAA = _HpA580048GPoEPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 66)
)
_HpA5820X14XGSFPPlusTAA2SLOT_ObjectIdentity = ObjectIdentity
hpA5820X14XGSFPPlusTAA2SLOT = _HpA5820X14XGSFPPlusTAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 67)
)
_HpA5820X24XGSFPPlusTAA_ObjectIdentity = ObjectIdentity
hpA5820X24XGSFPPlusTAA = _HpA5820X24XGSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 68)
)
_HpA512024GEITAA2SLOT_ObjectIdentity = ObjectIdentity
hpA512024GEITAA2SLOT = _HpA512024GEITAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 69)
)
_HpA512048GEITAA2SLOT_ObjectIdentity = ObjectIdentity
hpA512048GEITAA2SLOT = _HpA512048GEITAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 70)
)
_HpA512024GPoEPlusEITAA2SLOT_ObjectIdentity = ObjectIdentity
hpA512024GPoEPlusEITAA2SLOT = _HpA512024GPoEPlusEITAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 71)
)
_HpA512048GPoEPlusEITAA2SLOT_ObjectIdentity = ObjectIdentity
hpA512048GPoEPlusEITAA2SLOT = _HpA512048GPoEPlusEITAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 72)
)
_HpA550024GSFPEITAA2SLOT_ObjectIdentity = ObjectIdentity
hpA550024GSFPEITAA2SLOT = _HpA550024GSFPEITAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 73)
)
_HpA550024GEITAA2SLOT_ObjectIdentity = ObjectIdentity
hpA550024GEITAA2SLOT = _HpA550024GEITAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 74)
)
_HpA550048GEITAA2SLOT_ObjectIdentity = ObjectIdentity
hpA550048GEITAA2SLOT = _HpA550048GEITAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 75)
)
_HpA550024GPoEPlusEITAA2SLOT_ObjectIdentity = ObjectIdentity
hpA550024GPoEPlusEITAA2SLOT = _HpA550024GPoEPlusEITAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 76)
)
_HpA550048GPoEPlusEITAA2SLOT_ObjectIdentity = ObjectIdentity
hpA550048GPoEPlusEITAA2SLOT = _HpA550048GPoEPlusEITAA2SLOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 77)
)
_Hp5920AF24XG_ObjectIdentity = ObjectIdentity
hp5920AF24XG = _Hp5920AF24XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 78)
)
_HpA5830AF48G_ObjectIdentity = ObjectIdentity
hpA5830AF48G = _HpA5830AF48G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 79)
)
_HpA5830AF96G_ObjectIdentity = ObjectIdentity
hpA5830AF96G = _HpA5830AF96G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 80)
)
_HpV191016G_ObjectIdentity = ObjectIdentity
hpV191016G = _HpV191016G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 81)
)
_HpV191024G_ObjectIdentity = ObjectIdentity
hpV191024G = _HpV191024G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 82)
)
_HpV191024GPoE365W_ObjectIdentity = ObjectIdentity
hpV191024GPoE365W = _HpV191024GPoE365W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 83)
)
_HpV191024GPoE170W_ObjectIdentity = ObjectIdentity
hpV191024GPoE170W = _HpV191024GPoE170W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 84)
)
_HpV191048G_ObjectIdentity = ObjectIdentity
hpV191048G = _HpV191048G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 85)
)
_Hp10504_ObjectIdentity = ObjectIdentity
hp10504 = _Hp10504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 86)
)
_Hp10508_ObjectIdentity = ObjectIdentity
hp10508 = _Hp10508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 87)
)
_Hp10508V_ObjectIdentity = ObjectIdentity
hp10508V = _Hp10508V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 88)
)
_Hp10512_ObjectIdentity = ObjectIdentity
hp10512 = _Hp10512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 89)
)
_HpA360024V2EI_ObjectIdentity = ObjectIdentity
hpA360024V2EI = _HpA360024V2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 90)
)
_HpA360048V2EI_ObjectIdentity = ObjectIdentity
hpA360048V2EI = _HpA360048V2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 91)
)
_HpA360024PoEPlusV2EI_ObjectIdentity = ObjectIdentity
hpA360024PoEPlusV2EI = _HpA360024PoEPlusV2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 92)
)
_HpA360048PoEPlusV2EI_ObjectIdentity = ObjectIdentity
hpA360048PoEPlusV2EI = _HpA360048PoEPlusV2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 93)
)
_HpA360024SFPV2EI_ObjectIdentity = ObjectIdentity
hpA360024SFPV2EI = _HpA360024SFPV2EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 94)
)
_HpA360024V2SI_ObjectIdentity = ObjectIdentity
hpA360024V2SI = _HpA360024V2SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 95)
)
_HpA360048V2SI_ObjectIdentity = ObjectIdentity
hpA360048V2SI = _HpA360048V2SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 96)
)
_HpA360024PoEPlusV2SI_ObjectIdentity = ObjectIdentity
hpA360024PoEPlusV2SI = _HpA360024PoEPlusV2SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 97)
)
_HpA360048PoEPlusV2SI_ObjectIdentity = ObjectIdentity
hpA360048PoEPlusV2SI = _HpA360048PoEPlusV2SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 98)
)
_HpA310048V2_ObjectIdentity = ObjectIdentity
hpA310048V2 = _HpA310048V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 99)
)
_Hp5900AF48XG4QSFPPlus_ObjectIdentity = ObjectIdentity
hp5900AF48XG4QSFPPlus = _Hp5900AF48XG4QSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 100)
)
_HpA550024G4SFPHI_ObjectIdentity = ObjectIdentity
hpA550024G4SFPHI = _HpA550024G4SFPHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 101)
)
_HpA550048G4SFPHI_ObjectIdentity = ObjectIdentity
hpA550048G4SFPHI = _HpA550048G4SFPHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 102)
)
_Hp6125G_ObjectIdentity = ObjectIdentity
hp6125G = _Hp6125G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 103)
)
_HpA51208GSI_ObjectIdentity = ObjectIdentity
hpA51208GSI = _HpA51208GSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 104)
)
_HpA51208GPoEPlusSI_ObjectIdentity = ObjectIdentity
hpA51208GPoEPlusSI = _HpA51208GPoEPlusSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 105)
)
_HpA51208GPPoEPlusSI_ObjectIdentity = ObjectIdentity
hpA51208GPPoEPlusSI = _HpA51208GPPoEPlusSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 106)
)
_HpA5120AF48GHI_ObjectIdentity = ObjectIdentity
hpA5120AF48GHI = _HpA5120AF48GHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 107)
)
_Hp12504DC_ObjectIdentity = ObjectIdentity
hp12504DC = _Hp12504DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 108)
)
_Hp12508DC_ObjectIdentity = ObjectIdentity
hp12508DC = _Hp12508DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 109)
)
_Hp12518DC_ObjectIdentity = ObjectIdentity
hp12518DC = _Hp12518DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 110)
)
_Hp12508AC_ObjectIdentity = ObjectIdentity
hp12508AC = _Hp12508AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 111)
)
_Hp12518AC_ObjectIdentity = ObjectIdentity
hp12518AC = _Hp12518AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 112)
)
_Hp5900AF48XGT4QSFPPlus_ObjectIdentity = ObjectIdentity
hp5900AF48XGT4QSFPPlus = _Hp5900AF48XGT4QSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 113)
)
_Hp19108G_ObjectIdentity = ObjectIdentity
hp19108G = _Hp19108G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 114)
)
_Hp19108GPoEPlus65W_ObjectIdentity = ObjectIdentity
hp19108GPoEPlus65W = _Hp19108GPoEPlus65W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 115)
)
_Hp19108GPoEPlus180W_ObjectIdentity = ObjectIdentity
hp19108GPoEPlus180W = _Hp19108GPoEPlus180W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 116)
)
_Hp5830AF48GTAA_ObjectIdentity = ObjectIdentity
hp5830AF48GTAA = _Hp5830AF48GTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 117)
)
_Hp5830AF96GTAA_ObjectIdentity = ObjectIdentity
hp5830AF96GTAA = _Hp5830AF96GTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 118)
)
_Hp7508H_ObjectIdentity = ObjectIdentity
hp7508H = _Hp7508H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 119)
)
_Hp5900AF48G4XG2QSFPPlus_ObjectIdentity = ObjectIdentity
hp5900AF48G4XG2QSFPPlus = _Hp5900AF48G4XG2QSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 120)
)
_Hp550048GPoEPlus4SFPHI_ObjectIdentity = ObjectIdentity
hp550048GPoEPlus4SFPHI = _Hp550048GPoEPlus4SFPHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 121)
)
_Hp550024GPoEPlus4SFPHI_ObjectIdentity = ObjectIdentity
hp550024GPoEPlus4SFPHI = _Hp550024GPoEPlus4SFPHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 122)
)
_Hp550024GSFPHI_ObjectIdentity = ObjectIdentity
hp550024GSFPHI = _Hp550024GSFPHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 123)
)
_Hp12504ACV7_ObjectIdentity = ObjectIdentity
hp12504ACV7 = _Hp12504ACV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 124)
)
_Hp12504DCV7_ObjectIdentity = ObjectIdentity
hp12504DCV7 = _Hp12504DCV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 125)
)
_Hp12508ACV7_ObjectIdentity = ObjectIdentity
hp12508ACV7 = _Hp12508ACV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 126)
)
_Hp12508DCV7_ObjectIdentity = ObjectIdentity
hp12508DCV7 = _Hp12508DCV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 127)
)
_Hp12518ACV7_ObjectIdentity = ObjectIdentity
hp12518ACV7 = _Hp12518ACV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 128)
)
_Hp12518DCV7_ObjectIdentity = ObjectIdentity
hp12518DCV7 = _Hp12518DCV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 129)
)
_Hp5900AF48XG4QSFPPlusTAA_ObjectIdentity = ObjectIdentity
hp5900AF48XG4QSFPPlusTAA = _Hp5900AF48XG4QSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 130)
)
_Hp5920AF24XGTAA_ObjectIdentity = ObjectIdentity
hp5920AF24XGTAA = _Hp5920AF24XGTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 131)
)
_HpV19108_ObjectIdentity = ObjectIdentity
hpV19108 = _HpV19108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 132)
)
_HpV19108PoEPlus_ObjectIdentity = ObjectIdentity
hpV19108PoEPlus = _HpV19108PoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 133)
)
_HpV191024_ObjectIdentity = ObjectIdentity
hpV191024 = _HpV191024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 134)
)
_HpV191024PoEPlus_ObjectIdentity = ObjectIdentity
hpV191024PoEPlus = _HpV191024PoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 135)
)
_HpV191048_ObjectIdentity = ObjectIdentity
hpV191048 = _HpV191048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 136)
)
_Hp6125XGXLG_ObjectIdentity = ObjectIdentity
hp6125XGXLG = _Hp6125XGXLG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 137)
)
_Hp11908V_ObjectIdentity = ObjectIdentity
hp11908V = _Hp11908V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 138)
)
_Hp550048GPoEPlus4SFPHITAA2Slot_ObjectIdentity = ObjectIdentity
hp550048GPoEPlus4SFPHITAA2Slot = _Hp550048GPoEPlus4SFPHITAA2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 139)
)
_Hp550024GPoEPlus4SFPHITAA2Slot_ObjectIdentity = ObjectIdentity
hp550024GPoEPlus4SFPHITAA2Slot = _Hp550024GPoEPlus4SFPHITAA2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 140)
)
_Hp550024GSFPHITAA2Slot_ObjectIdentity = ObjectIdentity
hp550024GSFPHITAA2Slot = _Hp550024GSFPHITAA2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 141)
)
_HpMoonshot45XGc_ObjectIdentity = ObjectIdentity
hpMoonshot45XGc = _HpMoonshot45XGc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 142)
)
_Hp12910AC_ObjectIdentity = ObjectIdentity
hp12910AC = _Hp12910AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 143)
)
_HpFF593032QSFPPlus_ObjectIdentity = ObjectIdentity
hpFF593032QSFPPlus = _HpFF593032QSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 144)
)
_HpFF593032QSFPPlusTAA_ObjectIdentity = ObjectIdentity
hpFF593032QSFPPlusTAA = _HpFF593032QSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 145)
)
_HpFF7904_ObjectIdentity = ObjectIdentity
hpFF7904 = _HpFF7904_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 146)
)
_Hp12916AC_ObjectIdentity = ObjectIdentity
hp12916AC = _Hp12916AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 147)
)
_Hp12916DC_ObjectIdentity = ObjectIdentity
hp12916DC = _Hp12916DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 148)
)
_HpFF5900CP48XG4QSFPPlus_ObjectIdentity = ObjectIdentity
hpFF5900CP48XG4QSFPPlus = _HpFF5900CP48XG4QSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 149)
)
_Hp5900CP48XG4QSFPPlus8GbFCBF_ObjectIdentity = ObjectIdentity
hp5900CP48XG4QSFPPlus8GbFCBF = _Hp5900CP48XG4QSFPPlus8GbFCBF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 150)
)
_Hp6125XLGTAA_ObjectIdentity = ObjectIdentity
hp6125XLGTAA = _Hp6125XLGTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 151)
)
_Hp6125GXGTAA_ObjectIdentity = ObjectIdentity
hp6125GXGTAA = _Hp6125GXGTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 152)
)
_Hp6125GTAA_ObjectIdentity = ObjectIdentity
hp6125GTAA = _Hp6125GTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 153)
)
_Hp512024G4SFPXI2Slot_ObjectIdentity = ObjectIdentity
hp512024G4SFPXI2Slot = _Hp512024G4SFPXI2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 154)
)
_Hp512048G4SFPXI2Slot_ObjectIdentity = ObjectIdentity
hp512048G4SFPXI2Slot = _Hp512048G4SFPXI2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 155)
)
_Hp512024GPoEPlus4SFPXI2Slot_ObjectIdentity = ObjectIdentity
hp512024GPoEPlus4SFPXI2Slot = _Hp512024GPoEPlus4SFPXI2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 156)
)
_Hp512048GPoEPlus4SFPXI2Slot_ObjectIdentity = ObjectIdentity
hp512048GPoEPlus4SFPXI2Slot = _Hp512048GPoEPlus4SFPXI2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 157)
)
_Hp512024G4SFPXITAA2Slot_ObjectIdentity = ObjectIdentity
hp512024G4SFPXITAA2Slot = _Hp512024G4SFPXITAA2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 158)
)
_Hp512048G4SFPXITAA2Slot_ObjectIdentity = ObjectIdentity
hp512048G4SFPXITAA2Slot = _Hp512048G4SFPXITAA2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 159)
)
_Hp512024GPoEPlus4SFPXITAA2Slot_ObjectIdentity = ObjectIdentity
hp512024GPoEPlus4SFPXITAA2Slot = _Hp512024GPoEPlus4SFPXITAA2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 160)
)
_Hp512048GPoEPlus4SFPXITAA2Slot_ObjectIdentity = ObjectIdentity
hp512048GPoEPlus4SFPXITAA2Slot = _Hp512048GPoEPlus4SFPXITAA2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 161)
)
_Hp19208G_ObjectIdentity = ObjectIdentity
hp19208G = _Hp19208G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 162)
)
_Hp19208GPoEPlus65W_ObjectIdentity = ObjectIdentity
hp19208GPoEPlus65W = _Hp19208GPoEPlus65W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 163)
)
_Hp19208GPoEPlus180W_ObjectIdentity = ObjectIdentity
hp19208GPoEPlus180W = _Hp19208GPoEPlus180W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 164)
)
_Hp192016G_ObjectIdentity = ObjectIdentity
hp192016G = _Hp192016G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 165)
)
_Hp192024G_ObjectIdentity = ObjectIdentity
hp192024G = _Hp192024G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 166)
)
_Hp192024GPoEPlus180W_ObjectIdentity = ObjectIdentity
hp192024GPoEPlus180W = _Hp192024GPoEPlus180W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 167)
)
_Hp192024GPoEPlus370W_ObjectIdentity = ObjectIdentity
hp192024GPoEPlus370W = _Hp192024GPoEPlus370W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 168)
)
_Hp192048G_ObjectIdentity = ObjectIdentity
hp192048G = _Hp192048G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 169)
)
_Hp192048GPoEPlus370W_ObjectIdentity = ObjectIdentity
hp192048GPoEPlus370W = _Hp192048GPoEPlus370W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 170)
)
_HpFF570040XG2QSFPPlusTAA_ObjectIdentity = ObjectIdentity
hpFF570040XG2QSFPPlusTAA = _HpFF570040XG2QSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 171)
)
_HpFF570040XG2QSFPPlus_ObjectIdentity = ObjectIdentity
hpFF570040XG2QSFPPlus = _HpFF570040XG2QSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 172)
)
_HpFF570032XGT8XG2QSFPPlusTAA_ObjectIdentity = ObjectIdentity
hpFF570032XGT8XG2QSFPPlusTAA = _HpFF570032XGT8XG2QSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 173)
)
_HpFF570032XGT8XG2QSFPPlus_ObjectIdentity = ObjectIdentity
hpFF570032XGT8XG2QSFPPlus = _HpFF570032XGT8XG2QSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 174)
)
_HpFF570048G4XG2QSFPPlusTAA_ObjectIdentity = ObjectIdentity
hpFF570048G4XG2QSFPPlusTAA = _HpFF570048G4XG2QSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 175)
)
_HpFF570048G4XG2QSFPPlus_ObjectIdentity = ObjectIdentity
hpFF570048G4XG2QSFPPlus = _HpFF570048G4XG2QSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 176)
)
_Hp16208G_ObjectIdentity = ObjectIdentity
hp16208G = _Hp16208G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 177)
)
_Hp162024G_ObjectIdentity = ObjectIdentity
hp162024G = _Hp162024G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 178)
)
_Hp162048G_ObjectIdentity = ObjectIdentity
hp162048G = _Hp162048G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 179)
)
_Hp195024G2SFPPlus2XGT_ObjectIdentity = ObjectIdentity
hp195024G2SFPPlus2XGT = _Hp195024G2SFPPlus2XGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 180)
)
_Hp195048G2SFPPlus2XGT_ObjectIdentity = ObjectIdentity
hp195048G2SFPPlus2XGT = _Hp195048G2SFPPlus2XGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 181)
)
_Hp195024G2SFPPlus2XGTPoEPlus_ObjectIdentity = ObjectIdentity
hp195024G2SFPPlus2XGTPoEPlus = _Hp195024G2SFPPlus2XGTPoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 182)
)
_Hp195048G2SFPPlus2XGTPoEPlus_ObjectIdentity = ObjectIdentity
hp195048G2SFPPlus2XGTPoEPlus = _Hp195048G2SFPPlus2XGTPoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 183)
)
_Hp513024G4SFPPlusEI_ObjectIdentity = ObjectIdentity
hp513024G4SFPPlusEI = _Hp513024G4SFPPlusEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 184)
)
_Hp513024GSFP4SFPPlusEI_ObjectIdentity = ObjectIdentity
hp513024GSFP4SFPPlusEI = _Hp513024GSFP4SFPPlusEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 185)
)
_Hp513048G4SFPPlusEI_ObjectIdentity = ObjectIdentity
hp513048G4SFPPlusEI = _Hp513048G4SFPPlusEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 186)
)
_Hp513024GPoEPlus4SFPPlus180WEI_ObjectIdentity = ObjectIdentity
hp513024GPoEPlus4SFPPlus180WEI = _Hp513024GPoEPlus4SFPPlus180WEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 187)
)
_Hp513024GPoEPlus4SFPPlus370WEI_ObjectIdentity = ObjectIdentity
hp513024GPoEPlus4SFPPlus370WEI = _Hp513024GPoEPlus4SFPPlus370WEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 188)
)
_Hp513048GPoEPlus4SFPPlus370WEI_ObjectIdentity = ObjectIdentity
hp513048GPoEPlus4SFPPlus370WEI = _Hp513048GPoEPlus4SFPPlus370WEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 189)
)
_Hp513024G2SFPPlus2XGTEI_ObjectIdentity = ObjectIdentity
hp513024G2SFPPlus2XGTEI = _Hp513024G2SFPPlus2XGTEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 190)
)
_Hp513048G2SFPPlus2XGTEI_ObjectIdentity = ObjectIdentity
hp513048G2SFPPlus2XGTEI = _Hp513048G2SFPPlus2XGTEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 191)
)
_Hp513024GPoEPlus2SFPPlus2XGT370WEI_ObjectIdentity = ObjectIdentity
hp513024GPoEPlus2SFPPlus2XGT370WEI = _Hp513024GPoEPlus2SFPPlus2XGT370WEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 192)
)
_Hp513048GPoEPlus2SFPPlus2XGT370WEI_ObjectIdentity = ObjectIdentity
hp513048GPoEPlus2SFPPlus2XGT370WEI = _Hp513048GPoEPlus2SFPPlus2XGT370WEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 193)
)
_Hp513024G4SFPPlusEITAA_ObjectIdentity = ObjectIdentity
hp513024G4SFPPlusEITAA = _Hp513024G4SFPPlusEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 194)
)
_Hp513024GSFP4SFPPlusEITAA_ObjectIdentity = ObjectIdentity
hp513024GSFP4SFPPlusEITAA = _Hp513024GSFP4SFPPlusEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 195)
)
_Hp513048G4SFPPlusEITAA_ObjectIdentity = ObjectIdentity
hp513048G4SFPPlusEITAA = _Hp513048G4SFPPlusEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 196)
)
_Hp513024GPoEPlus4SFPPlus180WEITAA_ObjectIdentity = ObjectIdentity
hp513024GPoEPlus4SFPPlus180WEITAA = _Hp513024GPoEPlus4SFPPlus180WEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 197)
)
_Hp513024GPoEPlus4SFPPlus370WEITAA_ObjectIdentity = ObjectIdentity
hp513024GPoEPlus4SFPPlus370WEITAA = _Hp513024GPoEPlus4SFPPlus370WEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 198)
)
_Hp513048GPoEPlus4SFPPlus370WEITAA_ObjectIdentity = ObjectIdentity
hp513048GPoEPlus4SFPPlus370WEITAA = _Hp513048GPoEPlus4SFPPlus370WEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 199)
)
_Hp513024G2SFPPlus2XGTEITAA_ObjectIdentity = ObjectIdentity
hp513024G2SFPPlus2XGTEITAA = _Hp513024G2SFPPlus2XGTEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 200)
)
_Hp513048G2SFPPlus2XGTEITAA_ObjectIdentity = ObjectIdentity
hp513048G2SFPPlus2XGTEITAA = _Hp513048G2SFPPlus2XGTEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 201)
)
_Hp513024GPoEPlus2SFPPlus2XGT370WEITAA_ObjectIdentity = ObjectIdentity
hp513024GPoEPlus2SFPPlus2XGT370WEITAA = _Hp513024GPoEPlus2SFPPlus2XGT370WEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 202)
)
_Hp513048GPoEPlus2SFPPlus2XGT370WEITAA_ObjectIdentity = ObjectIdentity
hp513048GPoEPlus2SFPPlus2XGT370WEITAA = _Hp513048GPoEPlus2SFPPlus2XGT370WEITAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 203)
)
_HpFF7910_ObjectIdentity = ObjectIdentity
hpFF7910 = _HpFF7910_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 204)
)
_Hp5900AF48G4XG2QSFPPlusTAA_ObjectIdentity = ObjectIdentity
hp5900AF48G4XG2QSFPPlusTAA = _Hp5900AF48G4XG2QSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 205)
)
_Hp5900AF48XGT4QSFPPlusTAA_ObjectIdentity = ObjectIdentity
hp5900AF48XGT4QSFPPlusTAA = _Hp5900AF48XGT4QSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 206)
)
_HpFF5900CP48XG4QSFPPlusTAA_ObjectIdentity = ObjectIdentity
hpFF5900CP48XG4QSFPPlusTAA = _HpFF5900CP48XG4QSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 207)
)
_Hp513024G4SFPPlusEIBrazil_ObjectIdentity = ObjectIdentity
hp513024G4SFPPlusEIBrazil = _Hp513024G4SFPPlusEIBrazil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 208)
)
_Hp513048G4SFPPlusEIBrazil_ObjectIdentity = ObjectIdentity
hp513048G4SFPPlusEIBrazil = _Hp513048G4SFPPlusEIBrazil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 209)
)
_Hp513024GPoEPlus4SFPPlus370WEIBrazil_ObjectIdentity = ObjectIdentity
hp513024GPoEPlus4SFPPlus370WEIBrazil = _Hp513024GPoEPlus4SFPPlus370WEIBrazil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 210)
)
_Hp513048GPoEPlus4SFPPlus370WEIBrazil_ObjectIdentity = ObjectIdentity
hp513048GPoEPlus4SFPPlus370WEIBrazil = _Hp513048GPoEPlus4SFPPlus370WEIBrazil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 211)
)
_HpThunderBird_ObjectIdentity = ObjectIdentity
hpThunderBird = _HpThunderBird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 212)
)
_HpFF12916E_ObjectIdentity = ObjectIdentity
hpFF12916E = _HpFF12916E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 213)
)
_HpNJ50005GPoEPlusWalljack_ObjectIdentity = ObjectIdentity
hpNJ50005GPoEPlusWalljack = _HpNJ50005GPoEPlusWalljack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 214)
)
_Hp551024G4SFPPlusHI1Slot_ObjectIdentity = ObjectIdentity
hp551024G4SFPPlusHI1Slot = _Hp551024G4SFPPlusHI1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 215)
)
_Hp551048G4SFPPlusHI1Slot_ObjectIdentity = ObjectIdentity
hp551048G4SFPPlusHI1Slot = _Hp551048G4SFPPlusHI1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 216)
)
_Hp551024GPoEPlus4SFPPlusHI1Slot_ObjectIdentity = ObjectIdentity
hp551024GPoEPlus4SFPPlusHI1Slot = _Hp551024GPoEPlus4SFPPlusHI1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 217)
)
_Hp551048GPoEPlus4SFPPlusHI1Slot_ObjectIdentity = ObjectIdentity
hp551048GPoEPlus4SFPPlusHI1Slot = _Hp551048GPoEPlus4SFPPlusHI1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 218)
)
_Hp551024GSFP4SFPPlusHI1Slot_ObjectIdentity = ObjectIdentity
hp551024GSFP4SFPPlusHI1Slot = _Hp551024GSFP4SFPPlusHI1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 219)
)
_Hp551024G4SFPPlusHITAA1Slot_ObjectIdentity = ObjectIdentity
hp551024G4SFPPlusHITAA1Slot = _Hp551024G4SFPPlusHITAA1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 220)
)
_Hp551048G4SFPPlusHITAA1Slot_ObjectIdentity = ObjectIdentity
hp551048G4SFPPlusHITAA1Slot = _Hp551048G4SFPPlusHITAA1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 221)
)
_Hp551024GPoEPlus4SFPPlusHITAA1Slot_ObjectIdentity = ObjectIdentity
hp551024GPoEPlus4SFPPlusHITAA1Slot = _Hp551024GPoEPlus4SFPPlusHITAA1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 222)
)
_Hp551048GPoEPlus4SFPPlusHITAA1Slot_ObjectIdentity = ObjectIdentity
hp551048GPoEPlus4SFPPlusHITAA1Slot = _Hp551048GPoEPlus4SFPPlusHITAA1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 223)
)
_Hp551024GSFP4SFPPlusHITAA1Slot_ObjectIdentity = ObjectIdentity
hp551024GSFP4SFPPlusHITAA1Slot = _Hp551024GSFP4SFPPlusHITAA1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 224)
)
_HpFF12910ACTAA_ObjectIdentity = ObjectIdentity
hpFF12910ACTAA = _HpFF12910ACTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 225)
)
_HpFF7904TAA_ObjectIdentity = ObjectIdentity
hpFF7904TAA = _HpFF7904TAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 226)
)
_HpFF7910TAA_ObjectIdentity = ObjectIdentity
hpFF7910TAA = _HpFF7910TAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 227)
)
_Hp6127XLG_ObjectIdentity = ObjectIdentity
hp6127XLG = _Hp6127XLG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 228)
)
_HpFF59302Slot2QSFPPlus_ObjectIdentity = ObjectIdentity
hpFF59302Slot2QSFPPlus = _HpFF59302Slot2QSFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 229)
)
_HpFF59302Slot2QSFPPlusTAA_ObjectIdentity = ObjectIdentity
hpFF59302Slot2QSFPPlusTAA = _HpFF59302Slot2QSFPPlusTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 230)
)
_HpFF59304Slot_ObjectIdentity = ObjectIdentity
hpFF59304Slot = _HpFF59304Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 231)
)
_HpFF59304SlotTAA_ObjectIdentity = ObjectIdentity
hpFF59304SlotTAA = _HpFF59304SlotTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 232)
)
_Hp6127XLGTAA_ObjectIdentity = ObjectIdentity
hp6127XLGTAA = _Hp6127XLGTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 233)
)
_Hp195012XGT4SFPPlus_ObjectIdentity = ObjectIdentity
hp195012XGT4SFPPlus = _Hp195012XGT4SFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 234)
)
_HpFF12916ETAA_ObjectIdentity = ObjectIdentity
hpFF12916ETAA = _HpFF12916ETAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 235)
)
_HpFF12908E_ObjectIdentity = ObjectIdentity
hpFF12908E = _HpFF12908E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 236)
)
_HpFF12908ETAA_ObjectIdentity = ObjectIdentity
hpFF12908ETAA = _HpFF12908ETAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 237)
)
_HpMoonshot45GcR10_ObjectIdentity = ObjectIdentity
hpMoonshot45GcR10 = _HpMoonshot45GcR10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 238)
)
_HpMoonshot45XGcR16_ObjectIdentity = ObjectIdentity
hpMoonshot45XGcR16 = _HpMoonshot45XGcR16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 239)
)
_HpMoonshot180XGcR16_ObjectIdentity = ObjectIdentity
hpMoonshot180XGcR16 = _HpMoonshot180XGcR16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 240)
)
_HpMoonshot180XGcR40_ObjectIdentity = ObjectIdentity
hpMoonshot180XGcR40 = _HpMoonshot180XGcR40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 1, 241)
)
_HpRouter_ObjectIdentity = ObjectIdentity
hpRouter = _HpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2)
)
_HpAMSR900_ObjectIdentity = ObjectIdentity
hpAMSR900 = _HpAMSR900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 1)
)
_HpAMSR920_ObjectIdentity = ObjectIdentity
hpAMSR920 = _HpAMSR920_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 2)
)
_HpAMSR2010_ObjectIdentity = ObjectIdentity
hpAMSR2010 = _HpAMSR2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 3)
)
_HpAMSR2011_ObjectIdentity = ObjectIdentity
hpAMSR2011 = _HpAMSR2011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 4)
)
_HpAMSR2012_ObjectIdentity = ObjectIdentity
hpAMSR2012 = _HpAMSR2012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 5)
)
_HpAMSR2012T_ObjectIdentity = ObjectIdentity
hpAMSR2012T = _HpAMSR2012T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 6)
)
_HpAMSR2013_ObjectIdentity = ObjectIdentity
hpAMSR2013 = _HpAMSR2013_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 7)
)
_HpAMSR2020_ObjectIdentity = ObjectIdentity
hpAMSR2020 = _HpAMSR2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 8)
)
_HpAMSR2021_ObjectIdentity = ObjectIdentity
hpAMSR2021 = _HpAMSR2021_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 9)
)
_HpAMSR2040_ObjectIdentity = ObjectIdentity
hpAMSR2040 = _HpAMSR2040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 10)
)
_HpAMSR3010_ObjectIdentity = ObjectIdentity
hpAMSR3010 = _HpAMSR3010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 11)
)
_HpAMSR3011E_ObjectIdentity = ObjectIdentity
hpAMSR3011E = _HpAMSR3011E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 12)
)
_HpAMSR3011F_ObjectIdentity = ObjectIdentity
hpAMSR3011F = _HpAMSR3011F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 13)
)
_HpAMSR3016_ObjectIdentity = ObjectIdentity
hpAMSR3016 = _HpAMSR3016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 14)
)
_HpAMSR3020_ObjectIdentity = ObjectIdentity
hpAMSR3020 = _HpAMSR3020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 15)
)
_HpAMSR3040_ObjectIdentity = ObjectIdentity
hpAMSR3040 = _HpAMSR3040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 16)
)
_HpAMSR3060_ObjectIdentity = ObjectIdentity
hpAMSR3060 = _HpAMSR3060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 17)
)
_HpAMSR5040_ObjectIdentity = ObjectIdentity
hpAMSR5040 = _HpAMSR5040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 18)
)
_HpAMSR5060_ObjectIdentity = ObjectIdentity
hpAMSR5060 = _HpAMSR5060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 19)
)
_HpA6602_ObjectIdentity = ObjectIdentity
hpA6602 = _HpA6602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 20)
)
_HpA6604_ObjectIdentity = ObjectIdentity
hpA6604 = _HpA6604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 21)
)
_HpA6608_ObjectIdentity = ObjectIdentity
hpA6608 = _HpA6608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 22)
)
_HpA6616_ObjectIdentity = ObjectIdentity
hpA6616 = _HpA6616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 23)
)
_HpAMSR900W_ObjectIdentity = ObjectIdentity
hpAMSR900W = _HpAMSR900W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 24)
)
_HpAMSR900WNA_ObjectIdentity = ObjectIdentity
hpAMSR900WNA = _HpAMSR900WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 25)
)
_HpAMSR920W_ObjectIdentity = ObjectIdentity
hpAMSR920W = _HpAMSR920W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 26)
)
_HpAMSR920WNA_ObjectIdentity = ObjectIdentity
hpAMSR920WNA = _HpAMSR920WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 27)
)
_HpAMSR2012W_ObjectIdentity = ObjectIdentity
hpAMSR2012W = _HpAMSR2012W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 28)
)
_HpAMSR2012TW_ObjectIdentity = ObjectIdentity
hpAMSR2012TW = _HpAMSR2012TW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 29)
)
_HpAMSR2012TWNA_ObjectIdentity = ObjectIdentity
hpAMSR2012TWNA = _HpAMSR2012TWNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 30)
)
_HpAMSR2013W_ObjectIdentity = ObjectIdentity
hpAMSR2013W = _HpAMSR2013W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 31)
)
_HpAMSR2013WNA_ObjectIdentity = ObjectIdentity
hpAMSR2013WNA = _HpAMSR2013WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 32)
)
_HpAMSR2020S_ObjectIdentity = ObjectIdentity
hpAMSR2020S = _HpAMSR2020S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 33)
)
_HpAMSR2021S_ObjectIdentity = ObjectIdentity
hpAMSR2021S = _HpAMSR2021S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 34)
)
_HpAMSR2040S_ObjectIdentity = ObjectIdentity
hpAMSR2040S = _HpAMSR2040S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 35)
)
_HpAMSR3010DC_ObjectIdentity = ObjectIdentity
hpAMSR3010DC = _HpAMSR3010DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 36)
)
_HpAMSR3016POE_ObjectIdentity = ObjectIdentity
hpAMSR3016POE = _HpAMSR3016POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 37)
)
_HpAMSR3020AS_ObjectIdentity = ObjectIdentity
hpAMSR3020AS = _HpAMSR3020AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 38)
)
_HpAMSR3020POE_ObjectIdentity = ObjectIdentity
hpAMSR3020POE = _HpAMSR3020POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 39)
)
_HpAMSR3020DC_ObjectIdentity = ObjectIdentity
hpAMSR3020DC = _HpAMSR3020DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 40)
)
_HpAMSR3040AS_ObjectIdentity = ObjectIdentity
hpAMSR3040AS = _HpAMSR3040AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 41)
)
_HpAMSR3040POE_ObjectIdentity = ObjectIdentity
hpAMSR3040POE = _HpAMSR3040POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 42)
)
_HpAMSR3040DC_ObjectIdentity = ObjectIdentity
hpAMSR3040DC = _HpAMSR3040DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 43)
)
_HpAMSR3060AS_ObjectIdentity = ObjectIdentity
hpAMSR3060AS = _HpAMSR3060AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 44)
)
_HpAMSR3060POE_ObjectIdentity = ObjectIdentity
hpAMSR3060POE = _HpAMSR3060POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 45)
)
_HpAMSR3060DC_ObjectIdentity = ObjectIdentity
hpAMSR3060DC = _HpAMSR3060DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 46)
)
_HpAMSR5040DC_ObjectIdentity = ObjectIdentity
hpAMSR5040DC = _HpAMSR5040DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 47)
)
_HpAMSR5060DC_ObjectIdentity = ObjectIdentity
hpAMSR5060DC = _HpAMSR5060DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 48)
)
_HpA8805_ObjectIdentity = ObjectIdentity
hpA8805 = _HpA8805_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 49)
)
_HpA8808_ObjectIdentity = ObjectIdentity
hpA8808 = _HpA8808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 50)
)
_HpA8812_ObjectIdentity = ObjectIdentity
hpA8812 = _HpA8812_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 51)
)
_HpAOAPFICV2_ObjectIdentity = ObjectIdentity
hpAOAPFICV2 = _HpAOAPFICV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 52)
)
_HpAOAPMIMV2_ObjectIdentity = ObjectIdentity
hpAOAPMIMV2 = _HpAOAPMIMV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 53)
)
_HpAOAPSMIMV2_ObjectIdentity = ObjectIdentity
hpAOAPSMIMV2 = _HpAOAPSMIMV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 54)
)
_HpMSR2003AC_ObjectIdentity = ObjectIdentity
hpMSR2003AC = _HpMSR2003AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 55)
)
_HpMSR3012AC_ObjectIdentity = ObjectIdentity
hpMSR3012AC = _HpMSR3012AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 56)
)
_HpMSR3012DC_ObjectIdentity = ObjectIdentity
hpMSR3012DC = _HpMSR3012DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 57)
)
_HpMSR3024AC_ObjectIdentity = ObjectIdentity
hpMSR3024AC = _HpMSR3024AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 58)
)
_HpMSR3024DC_ObjectIdentity = ObjectIdentity
hpMSR3024DC = _HpMSR3024DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 59)
)
_HpMSR3024POE_ObjectIdentity = ObjectIdentity
hpMSR3024POE = _HpMSR3024POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 60)
)
_HpMSR3044_ObjectIdentity = ObjectIdentity
hpMSR3044 = _HpMSR3044_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 61)
)
_HpMSR3064_ObjectIdentity = ObjectIdentity
hpMSR3064 = _HpMSR3064_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 62)
)
_HpMSR4060_ObjectIdentity = ObjectIdentity
hpMSR4060 = _HpMSR4060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 63)
)
_HpMSR4080_ObjectIdentity = ObjectIdentity
hpMSR4080 = _HpMSR4080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 64)
)
_HpHSR6602G_ObjectIdentity = ObjectIdentity
hpHSR6602G = _HpHSR6602G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 65)
)
_HpHSR6602XG_ObjectIdentity = ObjectIdentity
hpHSR6602XG = _HpHSR6602XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 66)
)
_HpHSR6802_ObjectIdentity = ObjectIdentity
hpHSR6802 = _HpHSR6802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 67)
)
_HpHSR6804_ObjectIdentity = ObjectIdentity
hpHSR6804 = _HpHSR6804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 68)
)
_HpHSR6808_ObjectIdentity = ObjectIdentity
hpHSR6808 = _HpHSR6808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 69)
)
_HpMSR930_ObjectIdentity = ObjectIdentity
hpMSR930 = _HpMSR930_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 70)
)
_HpMSR930G_ObjectIdentity = ObjectIdentity
hpMSR930G = _HpMSR930G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 71)
)
_HpMSR931_ObjectIdentity = ObjectIdentity
hpMSR931 = _HpMSR931_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 72)
)
_HpMSR931G_ObjectIdentity = ObjectIdentity
hpMSR931G = _HpMSR931G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 73)
)
_HpMSR931GG_ObjectIdentity = ObjectIdentity
hpMSR931GG = _HpMSR931GG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 74)
)
_HpMSR930W_ObjectIdentity = ObjectIdentity
hpMSR930W = _HpMSR930W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 75)
)
_HpMSR9304GLTEV_ObjectIdentity = ObjectIdentity
hpMSR9304GLTEV = _HpMSR9304GLTEV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 76)
)
_HpMSR933_ObjectIdentity = ObjectIdentity
hpMSR933 = _HpMSR933_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 77)
)
_HpMSR933G_ObjectIdentity = ObjectIdentity
hpMSR933G = _HpMSR933G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 78)
)
_HpMSR935_ObjectIdentity = ObjectIdentity
hpMSR935 = _HpMSR935_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 79)
)
_HpMSR935W_ObjectIdentity = ObjectIdentity
hpMSR935W = _HpMSR935W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 80)
)
_HpMSR935G_ObjectIdentity = ObjectIdentity
hpMSR935G = _HpMSR935G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 81)
)
_HpMSR936W_ObjectIdentity = ObjectIdentity
hpMSR936W = _HpMSR936W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 82)
)
_HpMSR9304GLTEG_ObjectIdentity = ObjectIdentity
hpMSR9304GLTEG = _HpMSR9304GLTEG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 83)
)
_HpMSR930LE_ObjectIdentity = ObjectIdentity
hpMSR930LE = _HpMSR930LE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 84)
)
_HpMSR930GLE_ObjectIdentity = ObjectIdentity
hpMSR930GLE = _HpMSR930GLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 85)
)
_HpMSR931LE_ObjectIdentity = ObjectIdentity
hpMSR931LE = _HpMSR931LE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 86)
)
_HpMSR931GLE_ObjectIdentity = ObjectIdentity
hpMSR931GLE = _HpMSR931GLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 87)
)
_HpMSR931DGLE_ObjectIdentity = ObjectIdentity
hpMSR931DGLE = _HpMSR931DGLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 88)
)
_HpMSR930WLE_ObjectIdentity = ObjectIdentity
hpMSR930WLE = _HpMSR930WLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 89)
)
_HpMSR9304GLTEA_ObjectIdentity = ObjectIdentity
hpMSR9304GLTEA = _HpMSR9304GLTEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 90)
)
_HpMSR933GLE_ObjectIdentity = ObjectIdentity
hpMSR933GLE = _HpMSR933GLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 91)
)
_HpMSR935LE_ObjectIdentity = ObjectIdentity
hpMSR935LE = _HpMSR935LE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 92)
)
_HpMSR935WLE_ObjectIdentity = ObjectIdentity
hpMSR935WLE = _HpMSR935WLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 93)
)
_HpMSR935GLE_ObjectIdentity = ObjectIdentity
hpMSR935GLE = _HpMSR935GLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 94)
)
_HpMSR9304GLTEGLE_ObjectIdentity = ObjectIdentity
hpMSR9304GLTEGLE = _HpMSR9304GLTEGLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 95)
)
_HpVSR_ObjectIdentity = ObjectIdentity
hpVSR = _HpVSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 96)
)
_HpVSR1001_ObjectIdentity = ObjectIdentity
hpVSR1001 = _HpVSR1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 97)
)
_HpVSR1004_ObjectIdentity = ObjectIdentity
hpVSR1004 = _HpVSR1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 98)
)
_HpVSR1008_ObjectIdentity = ObjectIdentity
hpVSR1008 = _HpVSR1008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 99)
)
_HpMSR10038_ObjectIdentity = ObjectIdentity
hpMSR10038 = _HpMSR10038_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 100)
)
_HpMSR100414_ObjectIdentity = ObjectIdentity
hpMSR100414 = _HpMSR100414_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 101)
)
_HpVSR1000_ObjectIdentity = ObjectIdentity
hpVSR1000 = _HpVSR1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 102)
)
_HpMSR200424_ObjectIdentity = ObjectIdentity
hpMSR200424 = _HpMSR200424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 103)
)
_HpMSR200448_ObjectIdentity = ObjectIdentity
hpMSR200448 = _HpMSR200448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 104)
)
_HpHSR6602GTAA_ObjectIdentity = ObjectIdentity
hpHSR6602GTAA = _HpHSR6602GTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 105)
)
_HpHSR6602XGTAA_ObjectIdentity = ObjectIdentity
hpHSR6602XGTAA = _HpHSR6602XGTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 106)
)
_HpMSR10024_ObjectIdentity = ObjectIdentity
hpMSR10024 = _HpMSR10024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 107)
)
_HpNSC1000_ObjectIdentity = ObjectIdentity
hpNSC1000 = _HpNSC1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 108)
)
_HpMSR930WNA_ObjectIdentity = ObjectIdentity
hpMSR930WNA = _HpMSR930WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 109)
)
_HpMSR935WNA_ObjectIdentity = ObjectIdentity
hpMSR935WNA = _HpMSR935WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 110)
)
_HpMSR2003TAA_ObjectIdentity = ObjectIdentity
hpMSR2003TAA = _HpMSR2003TAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 111)
)
_HpMSR3024TAA_ObjectIdentity = ObjectIdentity
hpMSR3024TAA = _HpMSR3024TAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 112)
)
_HpMSR3044TAA_ObjectIdentity = ObjectIdentity
hpMSR3044TAA = _HpMSR3044TAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 113)
)
_HpMSR935TI_ObjectIdentity = ObjectIdentity
hpMSR935TI = _HpMSR935TI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 114)
)
_HpMSR933TI_ObjectIdentity = ObjectIdentity
hpMSR933TI = _HpMSR933TI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 115)
)
_HpMSR931TI_ObjectIdentity = ObjectIdentity
hpMSR931TI = _HpMSR931TI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 116)
)
_HpMSR10038S_ObjectIdentity = ObjectIdentity
hpMSR10038S = _HpMSR10038S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 117)
)
_HpMSR932_ObjectIdentity = ObjectIdentity
hpMSR932 = _HpMSR932_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 118)
)
_HpMSR932W_ObjectIdentity = ObjectIdentity
hpMSR932W = _HpMSR932W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 119)
)
_HpMSR932WNA_ObjectIdentity = ObjectIdentity
hpMSR932WNA = _HpMSR932WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 120)
)
_HpMSR9328_ObjectIdentity = ObjectIdentity
hpMSR9328 = _HpMSR9328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 121)
)
_HpMSR9328W_ObjectIdentity = ObjectIdentity
hpMSR9328W = _HpMSR9328W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 122)
)
_HpMSR9328WNA_ObjectIdentity = ObjectIdentity
hpMSR9328WNA = _HpMSR9328WNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 123)
)
_HpVBRAS1000_ObjectIdentity = ObjectIdentity
hpVBRAS1000 = _HpVBRAS1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 124)
)
_HpHSR6802E_ObjectIdentity = ObjectIdentity
hpHSR6802E = _HpHSR6802E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 125)
)
_HpHSR6804E_ObjectIdentity = ObjectIdentity
hpHSR6804E = _HpHSR6804E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 126)
)
_HpHSR6808E_ObjectIdentity = ObjectIdentity
hpHSR6808E = _HpHSR6808E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 127)
)
_HpMSR93204GLTEGV2_ObjectIdentity = ObjectIdentity
hpMSR93204GLTEGV2 = _HpMSR93204GLTEGV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 128)
)
_HpMSR93204GLTEAVS_ObjectIdentity = ObjectIdentity
hpMSR93204GLTEAVS = _HpMSR93204GLTEAVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 129)
)
_HpMSR954_ObjectIdentity = ObjectIdentity
hpMSR954 = _HpMSR954_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 130)
)
_HpMSR954W_ObjectIdentity = ObjectIdentity
hpMSR954W = _HpMSR954W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 131)
)
_HpMSR954WLTEAM_ObjectIdentity = ObjectIdentity
hpMSR954WLTEAM = _HpMSR954WLTEAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 132)
)
_HpMSR954WLTE_ObjectIdentity = ObjectIdentity
hpMSR954WLTE = _HpMSR954WLTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 133)
)
_HpMSR958_ObjectIdentity = ObjectIdentity
hpMSR958 = _HpMSR958_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 134)
)
_HpMSR958POE_ObjectIdentity = ObjectIdentity
hpMSR958POE = _HpMSR958POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 2, 135)
)
_HpWireless_ObjectIdentity = ObjectIdentity
hpWireless = _HpWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3)
)
_HpAWA2610EAGNFAT_ObjectIdentity = ObjectIdentity
hpAWA2610EAGNFAT = _HpAWA2610EAGNFAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 1)
)
_HpAWA2620EAGNFAT_ObjectIdentity = ObjectIdentity
hpAWA2620EAGNFAT = _HpAWA2620EAGNFAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 2)
)
_HpAWA2620AGNFAT_ObjectIdentity = ObjectIdentity
hpAWA2620AGNFAT = _HpAWA2620AGNFAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 3)
)
_HpA7500LSQM3WCMB0_ObjectIdentity = ObjectIdentity
hpA7500LSQM3WCMB0 = _HpA7500LSQM3WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 4)
)
_HpA9500LSRM2WCM2A1_ObjectIdentity = ObjectIdentity
hpA9500LSRM2WCM2A1 = _HpA9500LSRM2WCM2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 5)
)
_HpA5800LSWM2WCM10_ObjectIdentity = ObjectIdentity
hpA5800LSWM2WCM10 = _HpA5800LSWM2WCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 6)
)
_HpA5800LSWM2WCM20_ObjectIdentity = ObjectIdentity
hpA5800LSWM2WCM20 = _HpA5800LSWM2WCM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 7)
)
_HpAWX5004EWPXZ65004_ObjectIdentity = ObjectIdentity
hpAWX5004EWPXZ65004 = _HpAWX5004EWPXZ65004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 8)
)
_HpAWX5002EWPXZ75002_ObjectIdentity = ObjectIdentity
hpAWX5002EWPXZ75002 = _HpAWX5002EWPXZ75002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 9)
)
_HpA3000E_ObjectIdentity = ObjectIdentity
hpA3000E = _HpA3000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 10)
)
_HpA3000ELSW_ObjectIdentity = ObjectIdentity
hpA3000ELSW = _HpA3000ELSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 11)
)
_HpAWA3620AGN_ObjectIdentity = ObjectIdentity
hpAWA3620AGN = _HpAWA3620AGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 12)
)
_HpAWA3622AGN_ObjectIdentity = ObjectIdentity
hpAWA3622AGN = _HpAWA3622AGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 13)
)
_HpAWA3610GN_ObjectIdentity = ObjectIdentity
hpAWA3610GN = _HpAWA3610GN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 14)
)
_HpAWA2620XAGN_ObjectIdentity = ObjectIdentity
hpAWA2620XAGN = _HpAWA2620XAGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 15)
)
_HpLSU3WCMD0_ObjectIdentity = ObjectIdentity
hpLSU3WCMD0 = _HpLSU3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 16)
)
_HpWX3024EWCM_ObjectIdentity = ObjectIdentity
hpWX3024EWCM = _HpWX3024EWCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 17)
)
_HpWX3024ELSW_ObjectIdentity = ObjectIdentity
hpWX3024ELSW = _HpWX3024ELSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 18)
)
_HpWX3010EWCM_ObjectIdentity = ObjectIdentity
hpWX3010EWCM = _HpWX3010EWCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 19)
)
_HpWX3010ELSW_ObjectIdentity = ObjectIdentity
hpWX3010ELSW = _HpWX3010ELSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 20)
)
_HpLSU3WCMD0TAA_ObjectIdentity = ObjectIdentity
hpLSU3WCMD0TAA = _HpLSU3WCMD0TAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 21)
)
_HpWX3024ETAAWCM_ObjectIdentity = ObjectIdentity
hpWX3024ETAAWCM = _HpWX3024ETAAWCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 22)
)
_HpWX3024ETAALSW_ObjectIdentity = ObjectIdentity
hpWX3024ETAALSW = _HpWX3024ETAALSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 23)
)
_HpWX3010ETAAWCM_ObjectIdentity = ObjectIdentity
hpWX3010ETAAWCM = _HpWX3010ETAAWCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 24)
)
_HpWX3010ETAALSW_ObjectIdentity = ObjectIdentity
hpWX3010ETAALSW = _HpWX3010ETAALSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 3, 25)
)
_HpSecurity_ObjectIdentity = ObjectIdentity
hpSecurity = _HpSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4)
)
_HpSecBladeIMFWII_ObjectIdentity = ObjectIdentity
hpSecBladeIMFWII = _HpSecBladeIMFWII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 1)
)
_HpSecBladeIMSSL_ObjectIdentity = ObjectIdentity
hpSecBladeIMSSL = _HpSecBladeIMSSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 2)
)
_HpSecBladeIMLB_ObjectIdentity = ObjectIdentity
hpSecBladeIMLB = _HpSecBladeIMLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 3)
)
_HpSecBladeLSQ1FWBSC0_ObjectIdentity = ObjectIdentity
hpSecBladeLSQ1FWBSC0 = _HpSecBladeLSQ1FWBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 4)
)
_HpSecBladeLSQM1LBC0_ObjectIdentity = ObjectIdentity
hpSecBladeLSQM1LBC0 = _HpSecBladeLSQM1LBC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 5)
)
_HpSecBladeLSQ1NSMSC0_ObjectIdentity = ObjectIdentity
hpSecBladeLSQ1NSMSC0 = _HpSecBladeLSQ1NSMSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 6)
)
_HpSecBladeLSR1FW2A1_ObjectIdentity = ObjectIdentity
hpSecBladeLSR1FW2A1 = _HpSecBladeLSR1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 7)
)
_HpSecBladeLSR1LB1A1_ObjectIdentity = ObjectIdentity
hpSecBladeLSR1LB1A1 = _HpSecBladeLSR1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 8)
)
_HpSecBladeLSR1NSM1A1_ObjectIdentity = ObjectIdentity
hpSecBladeLSR1NSM1A1 = _HpSecBladeLSR1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 9)
)
_HpSecBladeLST1FW2A1_ObjectIdentity = ObjectIdentity
hpSecBladeLST1FW2A1 = _HpSecBladeLST1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 10)
)
_HpSecBladeLST1LB1A1_ObjectIdentity = ObjectIdentity
hpSecBladeLST1LB1A1 = _HpSecBladeLST1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 11)
)
_HpSecBladeLST1NSM1A1_ObjectIdentity = ObjectIdentity
hpSecBladeLST1NSM1A1 = _HpSecBladeLST1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 12)
)
_HpSecBladeLSWM1FW10_ObjectIdentity = ObjectIdentity
hpSecBladeLSWM1FW10 = _HpSecBladeLSWM1FW10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 13)
)
_HpSecBladeSPEFWM200_ObjectIdentity = ObjectIdentity
hpSecBladeSPEFWM200 = _HpSecBladeSPEFWM200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 14)
)
_HpAF5000_ObjectIdentity = ObjectIdentity
hpAF5000 = _HpAF5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 15)
)
_HpAF1000E_ObjectIdentity = ObjectIdentity
hpAF1000E = _HpAF1000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 16)
)
_HpAU200S_ObjectIdentity = ObjectIdentity
hpAU200S = _HpAU200S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 17)
)
_HpAU200A_ObjectIdentity = ObjectIdentity
hpAU200A = _HpAU200A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 18)
)
_HpAF1000SEI_ObjectIdentity = ObjectIdentity
hpAF1000SEI = _HpAF1000SEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 19)
)
_HpAF1000AEI_ObjectIdentity = ObjectIdentity
hpAF1000AEI = _HpAF1000AEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 20)
)
_HpSecBladeLST1FW3A1_ObjectIdentity = ObjectIdentity
hpSecBladeLST1FW3A1 = _HpSecBladeLST1FW3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 21)
)
_HpSecBladeLSU1FWCEA0_ObjectIdentity = ObjectIdentity
hpSecBladeLSU1FWCEA0 = _HpSecBladeLSU1FWCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 22)
)
_HpF5000C_ObjectIdentity = ObjectIdentity
hpF5000C = _HpF5000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 23)
)
_HpF5000S_ObjectIdentity = ObjectIdentity
hpF5000S = _HpF5000S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 24)
)
_HpVFW1000_ObjectIdentity = ObjectIdentity
hpVFW1000 = _HpVFW1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 25)
)
_HpSecBladeLSX1FWCEA1_ObjectIdentity = ObjectIdentity
hpSecBladeLSX1FWCEA1 = _HpSecBladeLSX1FWCEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 26)
)
_HpVMSGVLB1000_ObjectIdentity = ObjectIdentity
hpVMSGVLB1000 = _HpVMSGVLB1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 27)
)
_HpSecBlade3Context_ObjectIdentity = ObjectIdentity
hpSecBlade3Context = _HpSecBlade3Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11, 4, 28)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PRODUCT-ID-MIB",
    **{"hh3c-s5500-28C-EI": hh3c_s5500_28C_EI,
       "hh3c-s5500-52C-EI": hh3c_s5500_52C_EI,
       "hh3c-s5500-28C-PWR-EI": hh3c_s5500_28C_PWR_EI,
       "hh3c-s5500-52C-PWR-EI": hh3c_s5500_52C_PWR_EI,
       "hh3c-s5500-28F-EI": hh3c_s5500_28F_EI,
       "hh3c-s5500-28C-EI-DC": hh3c_s5500_28C_EI_DC,
       "hh3c-s6100-20Q-SI": hh3c_s6100_20Q_SI,
       "hh3c-s5500-28C-SI": hh3c_s5500_28C_SI,
       "hh3c-s5500-52C-SI": hh3c_s5500_52C_SI,
       "hh3c-s5500-28C-PWR-SI": hh3c_s5500_28C_PWR_SI,
       "hh3c-s5500-52C-PWR-SI": hh3c_s5500_52C_PWR_SI,
       "hh3c-s5510-24P": hh3c_s5510_24P,
       "hh3c-s5510-24F": hh3c_s5510_24F,
       "hh3c-s3610-28P": hh3c_s3610_28P,
       "hh3c-s3610-52P": hh3c_s3610_52P,
       "hh3c-s3610-28TP": hh3c_s3610_28TP,
       "hh3c-s3610-28F": hh3c_s3610_28F,
       "hh3c-e126": hh3c_e126,
       "hh3c-e328": hh3c_e328,
       "hh3c-e352": hh3c_e352,
       "hh3c-s3100-8C-SI": hh3c_s3100_8C_SI,
       "hh3c-s3100-16C-SI": hh3c_s3100_16C_SI,
       "hh3c-s3100-26C-SI": hh3c_s3100_26C_SI,
       "hh3c-s3100-8T-SI": hh3c_s3100_8T_SI,
       "hh3c-s3100-16T-SI": hh3c_s3100_16T_SI,
       "hh3c-s3100-26T-SI": hh3c_s3100_26T_SI,
       "hh3c-s3100-26TP-SI": hh3c_s3100_26TP_SI,
       "hh3c-s5100-24P-EI": hh3c_s5100_24P_EI,
       "hh3c-s5100-26C-EI": hh3c_s5100_26C_EI,
       "hh3c-s5100-50C-EI": hh3c_s5100_50C_EI,
       "hh3c-s5100-48P-EI": hh3c_s5100_48P_EI,
       "hh3c-s3600-28P-SI": hh3c_s3600_28P_SI,
       "hh3c-s3600-52P-SI": hh3c_s3600_52P_SI,
       "hh3c-s3600-28TP-SI": hh3c_s3600_28TP_SI,
       "hh3c-s3600-28P-PWR-SI": hh3c_s3600_28P_PWR_SI,
       "hh3c-s3600-52P-PWR-SI": hh3c_s3600_52P_PWR_SI,
       "hh3c-s3600-28P-EI": hh3c_s3600_28P_EI,
       "hh3c-s3600-52P-EI": hh3c_s3600_52P_EI,
       "hh3c-s3600-28P-PWR-EI": hh3c_s3600_28P_PWR_EI,
       "hh3c-s3600-52P-PWR-EI": hh3c_s3600_52P_PWR_EI,
       "hh3c-s3600-28F-EI": hh3c_s3600_28F_EI,
       "hh3c-s5600-26C": hh3c_s5600_26C,
       "hh3c-s5600-50C": hh3c_s5600_50C,
       "hh3c-s5600-26C-PWR": hh3c_s5600_26C_PWR,
       "hh3c-s5600-50C-PWR": hh3c_s5600_50C_PWR,
       "hh3c-s5600-26F": hh3c_s5600_26F,
       "hh3c-s3600-52G-HI": hh3c_s3600_52G_HI,
       "hh3c-s3600-52P-HI": hh3c_s3600_52P_HI,
       "hh3c-s3600-28G-HI": hh3c_s3600_28G_HI,
       "hh3c-s3600-28P-HI": hh3c_s3600_28P_HI,
       "hh3c-s3600-52M-HI": hh3c_s3600_52M_HI,
       "hh3c-s7502": hh3c_s7502,
       "hh3c-s7503": hh3c_s7503,
       "hh3c-s7506": hh3c_s7506,
       "hh3c-s7506R": hh3c_s7506R,
       "hh3c-ar28-09": hh3c_ar28_09,
       "hh3c-ar28-10": hh3c_ar28_10,
       "hh3c-ar28-11": hh3c_ar28_11,
       "hh3c-ar28-12": hh3c_ar28_12,
       "hh3c-ar28-13": hh3c_ar28_13,
       "hh3c-ar28-14": hh3c_ar28_14,
       "hh3c-ar28-30": hh3c_ar28_30,
       "hh3c-ar28-31": hh3c_ar28_31,
       "hh3c-ar28-40": hh3c_ar28_40,
       "hh3c-ar28-80": hh3c_ar28_80,
       "hh3c-ar46-20": hh3c_ar46_20,
       "hh3c-ar46-40": hh3c_ar46_40,
       "hh3c-ar46-80": hh3c_ar46_80,
       "hh3c-msr20-20": hh3c_msr20_20,
       "hh3c-msr20-21": hh3c_msr20_21,
       "hh3c-msr20-40": hh3c_msr20_40,
       "hh3c-msr30-20": hh3c_msr30_20,
       "hh3c-msr30-40": hh3c_msr30_40,
       "hh3c-msr30-60": hh3c_msr30_60,
       "hh3c-msr50-40": hh3c_msr50_40,
       "hh3c-msr50-60": hh3c_msr50_60,
       "hh3c-ar18-21": hh3c_ar18_21,
       "hh3c-ar18-21A": hh3c_ar18_21A,
       "hh3c-ar18-21B": hh3c_ar18_21B,
       "hh3c-ar18-22": hh3c_ar18_22,
       "hh3c-ar18-22-8": hh3c_ar18_22_8,
       "hh3c-ar18-22S-8": hh3c_ar18_22S_8,
       "hh3c-ar18-22-24": hh3c_ar18_22_24,
       "hh3c-ar18-23-1": hh3c_ar18_23_1,
       "hh3c-ar18-23S-1": hh3c_ar18_23S_1,
       "hh3c-ar18-30E": hh3c_ar18_30E,
       "hh3c-ar18-31E": hh3c_ar18_31E,
       "hh3c-ar18-32E": hh3c_ar18_32E,
       "hh3c-ar18-33": hh3c_ar18_33,
       "hh3c-ar18-33E": hh3c_ar18_33E,
       "hh3c-ar18-34": hh3c_ar18_34,
       "hh3c-ar18-34E": hh3c_ar18_34E,
       "hh3c-ar18-35E": hh3c_ar18_35E,
       "hh3c-ar18-63-1": hh3c_ar18_63_1,
       "hh3c-secpathF100-C": hh3c_secpathF100_C,
       "hh3c-secpathF100-A": hh3c_secpathF100_A,
       "hh3c-secpathF100-S": hh3c_secpathF100_S,
       "hh3c-secpathF100-E": hh3c_secpathF100_E,
       "hh3c-secpathF1000-S": hh3c_secpathF1000_S,
       "hh3c-secpathF1000-A": hh3c_secpathF1000_A,
       "hh3c-secpathF1800-A": hh3c_secpathF1800_A,
       "hh3c-secpathV100-S": hh3c_secpathV100_S,
       "hh3c-secpathV1000-A": hh3c_secpathV1000_A,
       "hh3c-secpathF100-AW": hh3c_secpathF100_AW,
       "hh3c-secpathF1800-S": hh3c_secpathF1800_S,
       "hh3c-secpathF1800-E": hh3c_secpathF1800_E,
       "hh3c-secpoint": hh3c_secpoint,
       "hh3c-vg10-10": hh3c_vg10_10,
       "hh3c-vg10-11": hh3c_vg10_11,
       "hh3c-vg10-40": hh3c_vg10_40,
       "hh3c-vg10-41": hh3c_vg10_41,
       "hh3c-vg21-08": hh3c_vg21_08,
       "hh3c-vg20-16": hh3c_vg20_16,
       "hh3c-vg20-32": hh3c_vg20_32,
       "hh3c-vg80-20": hh3c_vg80_20,
       "hh3c-xe200": hh3c_xe200,
       "hh3c-xe2000": hh3c_xe2000,
       "hh3c-xe7200": hh3c_xe7200,
       "hh3c-xe7300": hh3c_xe7300,
       "hh3c-xe7500": hh3c_xe7500,
       "hh3c-xe7600": hh3c_xe7600,
       "hh3c-xe7205": hh3c_xe7205,
       "hh3c-xe7305": hh3c_xe7305,
       "hh3c-xe7505": hh3c_xe7505,
       "hh3c-xe7605": hh3c_xe7605,
       "hh3c-neoceanIX1000": hh3c_neoceanIX1000,
       "hh3c-neoceanEX1000": hh3c_neoceanEX1000,
       "hh3c-neoceanEX800": hh3c_neoceanEX800,
       "hh3c-neoceanIX5000": hh3c_neoceanIX5000,
       "hh3c-neoceanIV5100": hh3c_neoceanIV5100,
       "hh3c-neoceanIV5200": hh3c_neoceanIV5200,
       "hh3c-s9502": hh3c_s9502,
       "hh3c-s9505": hh3c_s9505,
       "hh3c-s9508": hh3c_s9508,
       "hh3c-s9508V": hh3c_s9508V,
       "hh3c-s9512": hh3c_s9512,
       "hh3c-sR8812": hh3c_sR8812,
       "hh3c-sR8808": hh3c_sR8808,
       "hh3c-sR8805": hh3c_sR8805,
       "hh3c-sR8802": hh3c_sR8802,
       "hh3c-e126-SI": hh3c_e126_SI,
       "hh3c-vg31-08": hh3c_vg31_08,
       "hh3c-dr834": hh3c_dr834,
       "hh3c-s7510E": hh3c_s7510E,
       "hh3c-s5100-24P-SI": hh3c_s5100_24P_SI,
       "hh3c-s5100-48P-SI": hh3c_s5100_48P_SI,
       "hh3c-s5100-8P-SI": hh3c_s5100_8P_SI,
       "hh3c-s5100-16P-SI": hh3c_s5100_16P_SI,
       "hh3c-s5100-8P-EI": hh3c_s5100_8P_EI,
       "hh3c-s5100-16P-EI": hh3c_s5100_16P_EI,
       "hh3c-s5100-8P-PWR-EI": hh3c_s5100_8P_PWR_EI,
       "hh3c-s5100-16P-PWR-EI": hh3c_s5100_16P_PWR_EI,
       "hh3c-s5100-26C-PWR-EI": hh3c_s5100_26C_PWR_EI,
       "hh3c-s5100-50C-PWR-EI": hh3c_s5100_50C_PWR_EI,
       "hh3c-s3108TP-EI": hh3c_s3108TP_EI,
       "hh3c-s3116TP-EI": hh3c_s3116TP_EI,
       "hh3c-s3126TP-EI": hh3c_s3126TP_EI,
       "hh3c-s3108TP-EI-PWR": hh3c_s3108TP_EI_PWR,
       "hh3c-s3116TP-EI-PWR": hh3c_s3116TP_EI_PWR,
       "hh3c-s3126TP-EI-PWR": hh3c_s3126TP_EI_PWR,
       "hh3c-s5500M-20C": hh3c_s5500M_20C,
       "hh3c-s5500M-20F": hh3c_s5500M_20F,
       "hh3c-bR304plus": hh3c_bR304plus,
       "hh3c-s9505-V5": hh3c_s9505_V5,
       "hh3c-s9512-V5": hh3c_s9512_V5,
       "hh3c-s9508-V5": hh3c_s9508_V5,
       "hh3c-s9508V-V5": hh3c_s9508V_V5,
       "hh3c-s9502-V5": hh3c_s9502_V5,
       "hh3c-sR8802-V5": hh3c_sR8802_V5,
       "hh3c-sR8805-V5": hh3c_sR8805_V5,
       "hh3c-sR8812-V5": hh3c_sR8812_V5,
       "hh3c-sR8808-V5": hh3c_sR8808_V5,
       "hh3c-s3100-52P": hh3c_s3100_52P,
       "hh3c-e152": hh3c_e152,
       "hh3c-s2008": hh3c_s2008,
       "hh3c-s2026": hh3c_s2026,
       "hh3c-sr6602": hh3c_sr6602,
       "hh3c-sr6608": hh3c_sr6608,
       "hh3c-s3100-08TP-EI": hh3c_s3100_08TP_EI,
       "hh3c-s3100-08TP-PWR-EI": hh3c_s3100_08TP_PWR_EI,
       "hh3c-s3100-16TP-EI": hh3c_s3100_16TP_EI,
       "hh3c-s3100-16TP-PWR-EI": hh3c_s3100_16TP_PWR_EI,
       "hh3c-s3100-26TP-EI": hh3c_s3100_26TP_EI,
       "hh3c-s3100-26TP-PWR-EI": hh3c_s3100_26TP_PWR_EI,
       "hh3c-s7502-v5": hh3c_s7502_v5,
       "hh3c-vg80-21": hh3c_vg80_21,
       "hh3c-vg80-80": hh3c_vg80_80,
       "hh3c-wcm-wx5002": hh3c_wcm_wx5002,
       "hh3c-wcm-wcma": hh3c_wcm_wcma,
       "hh3c-msr30-10": hh3c_msr30_10,
       "hh3c-s7502e": hh3c_s7502e,
       "hh3c-s7503E": hh3c_s7503E,
       "hh3c-s7506E": hh3c_s7506E,
       "hh3c-s7506E-V": hh3c_s7506E_V,
       "hh3c-secBlade-FW": hh3c_secBlade_FW,
       "hh3c-secBlade-IPSec": hh3c_secBlade_IPSec,
       "hh3c-s3100-8TP-SI": hh3c_s3100_8TP_SI,
       "hh3c-s3100-16TP-SI": hh3c_s3100_16TP_SI,
       "hh3c-e126A": hh3c_e126A,
       "hh3c-s3100-26TP-SI-B": hh3c_s3100_26TP_SI_B,
       "hh3c-msr30-16": hh3c_msr30_16,
       "hh3cOEMProductID": hh3cOEMProductID,
       "hh3c-s2126-ei": hh3c_s2126_ei,
       "hh3c-e150-si": hh3c_e150_si,
       "hh3c-msr30-11": hh3c_msr30_11,
       "hh3c-neoceanIX3040": hh3c_neoceanIX3040,
       "hh3c-neoceanIX3080": hh3c_neoceanIX3080,
       "hh3c-secpathF100-M": hh3c_secpathF100_M,
       "hh3c-neoceanVX1500": hh3c_neoceanVX1500,
       "hh3c-neoceanIX1520": hh3c_neoceanIX1520,
       "hh3c-neoceanIX1540": hh3c_neoceanIX1540,
       "hh3c-wcm-wx5002-128ap": hh3c_wcm_wx5002_128ap,
       "hh3c-msr20-10": hh3c_msr20_10,
       "hh3c-msr20-11": hh3c_msr20_11,
       "hh3c-msr20-13": hh3c_msr20_13,
       "hh3c-msr20-15": hh3c_msr20_15,
       "hh3c-neoceanDL1008": hh3c_neoceanDL1008,
       "hh3c-neoceanDL1008S": hh3c_neoceanDL1008S,
       "hh3c-neoceanDL1012": hh3c_neoceanDL1012,
       "hh3c-s3610-52m": hh3c_s3610_52m,
       "hh3c-IV5680": hh3c_IV5680,
       "hh3c-IV5240": hh3c_IV5240,
       "hh3c-F1000-E": hh3c_F1000_E,
       "hh3c-S5024P": hh3c_S5024P,
       "hh3c-S5016P": hh3c_S5016P,
       "hh3c-LSQ1FWBSC0": hh3c_LSQ1FWBSC0,
       "hh3c-LSB1FW2A0": hh3c_LSB1FW2A0,
       "hh3c-S3100-8TP-EI": hh3c_S3100_8TP_EI,
       "hh3c-S3100-16TP-EI": hh3c_S3100_16TP_EI,
       "hh3c-S3100-26TP-EI": hh3c_S3100_26TP_EI,
       "hh3c-ET704": hh3c_ET704,
       "hh3c-ec1001": hh3c_ec1001,
       "hh3c-ec1001-hf": hh3c_ec1001_hf,
       "hh3c-ec1004-hc": hh3c_ec1004_hc,
       "hh3c-ec2004-hf": hh3c_ec2004_hf,
       "hh3c-dc1001": hh3c_dc1001,
       "hh3c-dm8000": hh3c_dm8000,
       "hh3c-vm8000": hh3c_vm8000,
       "hh3c-ms8000": hh3c_ms8000,
       "hh3c-S3100-52TP": hh3c_S3100_52TP,
       "hh3c-msr20-12": hh3c_msr20_12,
       "hh3c-s1550E": hh3c_s1550E,
       "hh3c-s1550": hh3c_s1550,
       "hh3c-s1526-EI": hh3c_s1526_EI,
       "hh3c-msr20-12-T": hh3c_msr20_12_T,
       "hh3c-msr20-15-I": hh3c_msr20_15_I,
       "hh3c-msr20-15-N": hh3c_msr20_15_N,
       "hh3c-wx6100EWPX": hh3c_wx6100EWPX,
       "hh3c-wx6100LSQ": hh3c_wx6100LSQ,
       "hh3c-wx6100LSB": hh3c_wx6100LSB,
       "hh3c-wx6100SW": hh3c_wx6100SW,
       "hh3c-dl1000": hh3c_dl1000,
       "hh3c-dl1000s": hh3c_dl1000s,
       "hh3c-wa1208e-g": hh3c_wa1208e_g,
       "hh3c-wa1208e-dg": hh3c_wa1208e_dg,
       "hh3c-wa1208e-ag": hh3c_wa1208e_ag,
       "hh3c-wa1208e-agp": hh3c_wa1208e_agp,
       "hh3c-S7501M-24T": hh3c_S7501M_24T,
       "hh3c-s7501M-24TP": hh3c_s7501M_24TP,
       "hh3c-s7502M": hh3c_s7502M,
       "hh3c-s7503M": hh3c_s7503M,
       "hh3c-s7506M": hh3c_s7506M,
       "hh3c-s7506M-V": hh3c_s7506M_V,
       "hh3c-s7510M": hh3c_s7510M,
       "hh3c-secpathT200": hh3c_secpathT200,
       "hh3c-secpathT200E": hh3c_secpathT200E,
       "hh3c-cc600": hh3c_cc600,
       "hh3c-wa1208e-gp": hh3c_wa1208e_gp,
       "hh3c-wb2321e-agp": hh3c_wb2321e_agp,
       "hh3c-wh2520e-agp": hh3c_wh2520e_agp,
       "hh3c-ICG2000": hh3c_ICG2000,
       "hh3c-ICG3000": hh3c_ICG3000,
       "hh3c-ICG5000": hh3c_ICG5000,
       "hh3c-S5520TP-SI": hh3c_S5520TP_SI,
       "hh3c-wa2210-ag": hh3c_wa2210_ag,
       "hh3c-wa2220-ag": hh3c_wa2220_ag,
       "hh3c-wa2220e-ag": hh3c_wa2220e_ag,
       "hh3c-wa2210x-g": hh3c_wa2210x_g,
       "hh3c-wa2220x-ag": hh3c_wa2220x_ag,
       "hh3c-wa2220x-agp": hh3c_wa2220x_agp,
       "hh3c-S3100-52TP-SI": hh3c_S3100_52TP_SI,
       "hh3c-secpathASE5000-E": hh3c_secpathASE5000_E,
       "hh3c-secpathASE5000-S": hh3c_secpathASE5000_S,
       "hh3c-secpathU200-C": hh3c_secpathU200_C,
       "hh3c-secpathU200-S": hh3c_secpathU200_S,
       "hh3c-secpathU200-A": hh3c_secpathU200_A,
       "hh3c-secpathU200-M": hh3c_secpathU200_M,
       "hh3c-ec3016-hc": hh3c_ec3016_hc,
       "hh3c-dc1001-ff": hh3c_dc1001_ff,
       "hh3c-ecr3304-hf": hh3c_ecr3304_hf,
       "hh3c-ecr3308-hd": hh3c_ecr3308_hd,
       "hh3c-ecr3316-hc": hh3c_ecr3316_hc,
       "hh3c-isc3000": hh3c_isc3000,
       "hh3c-isc3100": hh3c_isc3100,
       "hh3c-vm9000": hh3c_vm9000,
       "hh3c-vm5000": hh3c_vm5000,
       "hh3c-ms9000-vtdu": hh3c_ms9000_vtdu,
       "hh3c-ms9000-nru": hh3c_ms9000_nru,
       "hh3c-ums9005": hh3c_ums9005,
       "hh3c-CS2104B": hh3c_CS2104B,
       "hh3c-CS2106B": hh3c_CS2106B,
       "hh3c-S5024E": hh3c_S5024E,
       "hh3c-S5048E": hh3c_S5048E,
       "hh3c-secpathF5000-A": hh3c_secpathF5000_A,
       "hh3c-neoceanIX3240": hh3c_neoceanIX3240,
       "hh3c-neoceanIX3620": hh3c_neoceanIX3620,
       "hh3c-MSA7302": hh3c_MSA7302,
       "hh3c-MSA7306": hh3c_MSA7306,
       "hh3c-S7501E": hh3c_S7501E,
       "hh3c-S3100-8C-EPON-EI": hh3c_S3100_8C_EPON_EI,
       "hh3c-S3100-16C-EPON-EI": hh3c_S3100_16C_EPON_EI,
       "hh3c-S3100-26C-EPON-EI": hh3c_S3100_26C_EPON_EI,
       "hh3c-secBlade-LSQ1AFCBSC0": hh3c_secBlade_LSQ1AFCBSC0,
       "hh3c-secBlade-LSB1AFC1A0": hh3c_secBlade_LSB1AFC1A0,
       "hh3c-secpathF1000-C": hh3c_secpathF1000_C,
       "hh3c-secpathF100-A-SI": hh3c_secpathF100_A_SI,
       "hh3c-secpathV100-E": hh3c_secpathV100_E,
       "hh3c-S5800-32C": hh3c_S5800_32C,
       "hh3c-S5800-56C": hh3c_S5800_56C,
       "hh3c-S5800-32C-PWR": hh3c_S5800_32C_PWR,
       "hh3c-S5800-56C-PWR": hh3c_S5800_56C_PWR,
       "hh3c-S5800-60C-PWR": hh3c_S5800_60C_PWR,
       "hh3c-S5800-32F": hh3c_S5800_32F,
       "hh3c-S5820X-28C": hh3c_S5820X_28C,
       "hh3c-S5820X-28S": hh3c_S5820X_28S,
       "hh3c-cc602": hh3c_cc602,
       "hh3c-cr400": hh3c_cr400,
       "hh3c-cc600E": hh3c_cc600E,
       "hh3c-secpathT1000-M": hh3c_secpathT1000_M,
       "hh3c-neoceanVX1540": hh3c_neoceanVX1540,
       "hh3c-msr50-06": hh3c_msr50_06,
       "hh3c-secpathACG2000-M": hh3c_secpathACG2000_M,
       "hh3c-secBlade-LSQ1ACGASC0": hh3c_secBlade_LSQ1ACGASC0,
       "hh3c-secBlade-LSB1ACG1A0": hh3c_secBlade_LSB1ACG1A0,
       "hh3c-wx3024wcm": hh3c_wx3024wcm,
       "hh3c-wx3024lsw": hh3c_wx3024lsw,
       "hh3c-wx5004": hh3c_wx5004,
       "hh3c-sr6604": hh3c_sr6604,
       "hh3c-iag5000-A": hh3c_iag5000_A,
       "hh3c-secBlade-SPE-FWM": hh3c_secBlade_SPE_FWM,
       "hh3c-ICG2200": hh3c_ICG2200,
       "hh3c-S7602": hh3c_S7602,
       "hh3c-S7603": hh3c_S7603,
       "hh3c-S7606": hh3c_S7606,
       "hh3c-S7606-V": hh3c_S7606_V,
       "hh3c-S7610": hh3c_S7610,
       "hh3c-wa2610e-agn": hh3c_wa2610e_agn,
       "hh3c-wa2620e-agn": hh3c_wa2620e_agn,
       "hh3c-wa1208e-g-v5": hh3c_wa1208e_g_v5,
       "hh3c-wa1208e-dg-v5": hh3c_wa1208e_dg_v5,
       "hh3c-wa1208e-ag-v5": hh3c_wa1208e_ag_v5,
       "hh3c-wa1208e-agp-v5": hh3c_wa1208e_agp_v5,
       "hh3c-wa1208e-gp-v5": hh3c_wa1208e_gp_v5,
       "hh3c-S7503E-S": hh3c_S7503E_S,
       "hh3c-secpathIAG2000-A": hh3c_secpathIAG2000_A,
       "hh3c-secpathT1000-A": hh3c_secpathT1000_A,
       "hh3c-secpathT1000-S": hh3c_secpathT1000_S,
       "hh3c-secBlade-EWPX1FWA0": hh3c_secBlade_EWPX1FWA0,
       "hh3c-secBlade-LSQ1NSMSC0": hh3c_secBlade_LSQ1NSMSC0,
       "hh3c-secBlade-LSQ1AFDBSC0": hh3c_secBlade_LSQ1AFDBSC0,
       "hh3c-secBlade-LSQ1LBSC0": hh3c_secBlade_LSQ1LBSC0,
       "hh3c-secBlade-LSB1LB1A0": hh3c_secBlade_LSB1LB1A0,
       "hh3c-neoceanIX1560": hh3c_neoceanIX1560,
       "hh3c-neoceanEX1500S": hh3c_neoceanEX1500S,
       "hh3c-neoceanEX1520S": hh3c_neoceanEX1520S,
       "hh3c-neoceanEX1540S": hh3c_neoceanEX1540S,
       "hh3c-neoceanEX1560S": hh3c_neoceanEX1560S,
       "hh3c-ET716": hh3c_ET716,
       "hh3c-s3600-2P-OLT": hh3c_s3600_2P_OLT,
       "hh3c-ER3200": hh3c_ER3200,
       "hh3c-ER3100": hh3c_ER3100,
       "hh3c-s9505E": hh3c_s9505E,
       "hh3c-s9508E-V": hh3c_s9508E_V,
       "hh3c-s9512E": hh3c_s9512E,
       "hh3c-s12508": hh3c_s12508,
       "hh3c-s12518": hh3c_s12518,
       "hh3c-ET708": hh3c_ET708,
       "hh3c-ET724": hh3c_ET724,
       "hh3c-s2008TP-EA": hh3c_s2008TP_EA,
       "hh3c-s2016TP-EA": hh3c_s2016TP_EA,
       "hh3c-s2403TP-EA": hh3c_s2403TP_EA,
       "hh3c-ICG2000-CT": hh3c_ICG2000_CT,
       "hh3c-S3528P-EA": hh3c_S3528P_EA,
       "hh3c-S3552P-EA": hh3c_S3552P_EA,
       "hh3c-S3552F-EA": hh3c_S3552F_EA,
       "hh3c-S3528F-EA": hh3c_S3528F_EA,
       "hh3c-S3528TP-EA": hh3c_S3528TP_EA,
       "hh3c-secpathAFD1000-A": hh3c_secpathAFD1000_A,
       "hh3c-secpathF100-C-EI": hh3c_secpathF100_C_EI,
       "hh3c-ER3260": hh3c_ER3260,
       "hh3c-ICG800": hh3c_ICG800,
       "hh3c-ICG800g": hh3c_ICG800g,
       "hh3c-ICG1000": hh3c_ICG1000,
       "hh3c-ICG1800": hh3c_ICG1800,
       "hh3c-neoceanIX3240E": hh3c_neoceanIX3240E,
       "hh3c-neoceanIX3620E": hh3c_neoceanIX3620E,
       "hh3c-neoceanIX3640E": hh3c_neoceanIX3640E,
       "hh3c-secpathACG8800-S3": hh3c_secpathACG8800_S3,
       "hh3c-secpathT5000-S3": hh3c_secpathT5000_S3,
       "hh3c-secpathIAG2000-S": hh3c_secpathIAG2000_S,
       "hh3c-secpathACG8800-S3-NS21S2MSPB0": hh3c_secpathACG8800_S3_NS21S2MSPB0,
       "hh3c-secpathT5000-S3-NS11S2MSPB0": hh3c_secpathT5000_S3_NS11S2MSPB0,
       "hh3c-msr3010": hh3c_msr3010,
       "hh3c-msr3011E": hh3c_msr3011E,
       "hh3c-msr3011F": hh3c_msr3011F,
       "hh3c-secpathT200-A": hh3c_secpathT200_A,
       "hh3c-secpathT200-M": hh3c_secpathT200_M,
       "hh3c-secpathF100-C2": hh3c_secpathF100_C2,
       "hh3c-DPtech-FW1000-GE": hh3c_DPtech_FW1000_GE,
       "hh3c-DPtech-FW1000-GA": hh3c_DPtech_FW1000_GA,
       "hh3c-DPtech-FW1000-GS": hh3c_DPtech_FW1000_GS,
       "hh3c-DPtech-FW1000-ME": hh3c_DPtech_FW1000_ME,
       "hh3c-DPtech-FW1000-MA": hh3c_DPtech_FW1000_MA,
       "hh3c-DPtech-FW1000-MM": hh3c_DPtech_FW1000_MM,
       "hh3c-DPtech-FW1000-MC": hh3c_DPtech_FW1000_MC,
       "hh3c-DPtech-UTM2000-MA": hh3c_DPtech_UTM2000_MA,
       "hh3c-DPtech-UTM2000-MM": hh3c_DPtech_UTM2000_MM,
       "hh3c-DPtech-UTM2000-MS": hh3c_DPtech_UTM2000_MS,
       "hh3c-DPtech-IPS2000-GM": hh3c_DPtech_IPS2000_GM,
       "hh3c-DPtech-IPS2000-MM": hh3c_DPtech_IPS2000_MM,
       "hh3c-sr6616": hh3c_sr6616,
       "hh3c-s3620-28TP-EI": hh3c_s3620_28TP_EI,
       "hh3c-s3620-28P-EI": hh3c_s3620_28P_EI,
       "hh3c-s3620-52P-EI": hh3c_s3620_52P_EI,
       "hh3c-s3620-28P-PWR-EI": hh3c_s3620_28P_PWR_EI,
       "hh3c-s3620-52P-PWR-EI": hh3c_s3620_52P_PWR_EI,
       "hh3c-s3620-28F-EI": hh3c_s3620_28F_EI,
       "hh3c-s3620-52M": hh3c_s3620_52M,
       "hh3c-s3620-52M-DC": hh3c_s3620_52M_DC,
       "hh3c-s3620-28C-EI": hh3c_s3620_28C_EI,
       "hh3c-wa2210e-ge": hh3c_wa2210e_ge,
       "hh3c-wa2220x-age": hh3c_wa2220x_age,
       "hh3c-wa2210x-ge": hh3c_wa2210x_ge,
       "hh3c-wb2320x-age": hh3c_wb2320x_age,
       "hh3c-neoceanEX1540": hh3c_neoceanEX1540,
       "hh3c-S5810-50S": hh3c_S5810_50S,
       "hh3c-secBlade-LSQ1IPSSC0": hh3c_secBlade_LSQ1IPSSC0,
       "hh3c-secBlade-LSB1IPS1A0": hh3c_secBlade_LSB1IPS1A0,
       "hh3c-ER5100": hh3c_ER5100,
       "hh3c-ER5200": hh3c_ER5200,
       "hh3c-wx3010wcm": hh3c_wx3010wcm,
       "hh3c-wx3010lsw": hh3c_wx3010lsw,
       "hh3c-cc652E": hh3c_cc652E,
       "hh3c-S5120-20P-SI": hh3c_S5120_20P_SI,
       "hh3c-S5120-28P-SI": hh3c_S5120_28P_SI,
       "hh3c-S5120-52P-SI": hh3c_S5120_52P_SI,
       "hh3c-S5120-28P-EI": hh3c_S5120_28P_EI,
       "hh3c-S5120-52P-EI": hh3c_S5120_52P_EI,
       "hh3c-S5120-28P-LPWR-EI": hh3c_S5120_28P_LPWR_EI,
       "hh3c-S5120-28P-PWR-EI": hh3c_S5120_28P_PWR_EI,
       "hh3c-wx6100LSR": hh3c_wx6100LSR,
       "hh3c-s7506E-S": hh3c_s7506E_S,
       "hh3c-ICG2000B": hh3c_ICG2000B,
       "hh3c-ICG2000C": hh3c_ICG2000C,
       "hh3c-S1626": hh3c_S1626,
       "hh3c-S1650": hh3c_S1650,
       "hh3c-S1626P": hh3c_S1626P,
       "hh3c-neoceanIX3620S": hh3c_neoceanIX3620S,
       "hh3c-neoceanIX3080S": hh3c_neoceanIX3080S,
       "hh3c-ER3280g": hh3c_ER3280g,
       "hh3c-wa2610-agn": hh3c_wa2610_agn,
       "hh3c-wa2612-agn": hh3c_wa2612_agn,
       "hh3c-secpathT200-S": hh3c_secpathT200_S,
       "hh3c-secpathU200-CS": hh3c_secpathU200_CS,
       "hh3c-secpathU200-CM": hh3c_secpathU200_CM,
       "hh3c-secpathU200-CA": hh3c_secpathU200_CA,
       "hh3c-secBlade-LSR1AFC2A1": hh3c_secBlade_LSR1AFC2A1,
       "hh3c-secBlade-LSR1FW2A1": hh3c_secBlade_LSR1FW2A1,
       "hh3c-secBlade-LSR1LB1A1": hh3c_secBlade_LSR1LB1A1,
       "hh3c-secBlade-LSR1NSM1A1": hh3c_secBlade_LSR1NSM1A1,
       "hh3c-cc650E": hh3c_cc650E,
       "hh3c-LSWM1WCM10": hh3c_LSWM1WCM10,
       "hh3c-LSWM1WCM20": hh3c_LSWM1WCM20,
       "hh3c-EWPXM1WCMC0": hh3c_EWPXM1WCMC0,
       "hh3c-LSWM1IPS10": hh3c_LSWM1IPS10,
       "hh3c-LSWM1FW10": hh3c_LSWM1FW10,
       "hh3c-secpathF1000-S-EI": hh3c_secpathF1000_S_EI,
       "hh3c-secpathF1000-A-EI": hh3c_secpathF1000_A_EI,
       "hh3c-msr50-06-V5": hh3c_msr50_06_V5,
       "hh3c-secBlade-LSR1ACG1A1": hh3c_secBlade_LSR1ACG1A1,
       "hh3c-secBlade-LSR1IPS1A1": hh3c_secBlade_LSR1IPS1A1,
       "hh3c-S7602-S": hh3c_S7602_S,
       "hh3c-S7603-S": hh3c_S7603_S,
       "hh3c-S7606-S": hh3c_S7606_S,
       "hh3c-SSM-s5500G": hh3c_SSM_s5500G,
       "hh3c-SSM-FIC": hh3c_SSM_FIC,
       "hh3c-SSM-MIM": hh3c_SSM_MIM,
       "hh3c-ER8300": hh3c_ER8300,
       "hh3c-wa2610x-gnp": hh3c_wa2610x_gnp,
       "hh3c-wb2360x-anp": hh3c_wb2360x_anp,
       "hh3c-wh2530x-dag": hh3c_wh2530x_dag,
       "hh3c-wa2620-agn": hh3c_wa2620_agn,
       "hh3c-cc610E": hh3c_cc610E,
       "hh3c-DPtech-FW1000-GT": hh3c_DPtech_FW1000_GT,
       "hh3c-s2008TP-EA-SI": hh3c_s2008TP_EA_SI,
       "hh3c-s2016TP-EA-SI": hh3c_s2016TP_EA_SI,
       "hh3c-s2403TP-EA-SI": hh3c_s2403TP_EA_SI,
       "hh3c-S5120-24P-EI": hh3c_S5120_24P_EI,
       "hh3c-S5120-48P-EI": hh3c_S5120_48P_EI,
       "hh3c-S5120-28C-EI": hh3c_S5120_28C_EI,
       "hh3c-S5120-52C-EI": hh3c_S5120_52C_EI,
       "hh3c-S5120-28C-PWR-EI": hh3c_S5120_28C_PWR_EI,
       "hh3c-S5120-52C-PWR-EI": hh3c_S5120_52C_PWR_EI,
       "hh3c-wx3008wcm": hh3c_wx3008wcm,
       "hh3c-wx3008lsw": hh3c_wx3008lsw,
       "hh3c-msr900": hh3c_msr900,
       "hh3c-msr920": hh3c_msr920,
       "hh3c-secBlade-LSQ1IAGSC0": hh3c_secBlade_LSQ1IAGSC0,
       "hh3c-WX7306": hh3c_WX7306,
       "hh3c-WX7310": hh3c_WX7310,
       "hh3c-Blade5310": hh3c_Blade5310,
       "hh3c-Blade55102": hh3c_Blade55102,
       "hh3c-Blade5512S": hh3c_Blade5512S,
       "hh3c-Blade55110X": hh3c_Blade55110X,
       "hh3c-wa2610e-gnp": hh3c_wa2610e_gnp,
       "hh3c-s3100-26TP-SI-UM": hh3c_s3100_26TP_SI_UM,
       "hh3c-s3100-52TP-SI-UM": hh3c_s3100_52TP_SI_UM,
       "hh3c-s5500-24P-SI": hh3c_s5500_24P_SI,
       "hh3c-s5500-48P-SI": hh3c_s5500_48P_SI,
       "hh3c-ME8000": hh3c_ME8000,
       "hh3c-ME8600": hh3c_ME8600,
       "hh3c-ME5000": hh3c_ME5000,
       "hh3c-MG6060": hh3c_MG6060,
       "hh3c-MG6050": hh3c_MG6050,
       "hh3c-MG6050S": hh3c_MG6050S,
       "hh3c-MG9010": hh3c_MG9010,
       "hh3c-MG9030": hh3c_MG9030,
       "hh3c-MG9060": hh3c_MG9060,
       "hh3c-neoceanVX1500-DC": hh3c_neoceanVX1500_DC,
       "hh3c-cc620E": hh3c_cc620E,
       "hh3c-SIVX-S3628": hh3c_SIVX_S3628,
       "hh3c-SIVX-S5528": hh3c_SIVX_S5528,
       "hh3c-SIVX-VS1500": hh3c_SIVX_VS1500,
       "hh3c-neoceanIX2540": hh3c_neoceanIX2540,
       "hh3c-neoceanVX2500": hh3c_neoceanVX2500,
       "hh3c-S5120-28P-PWR-SI": hh3c_S5120_28P_PWR_SI,
       "hh3c-S5120-28P-HPWR-SI": hh3c_S5120_28P_HPWR_SI,
       "hh3c-F1000-E-DC": hh3c_F1000_E_DC,
       "hh3c-S5028": hh3c_S5028,
       "hh3c-ET824": hh3c_ET824,
       "hh3c-OSM": hh3c_OSM,
       "hh3c-wx5002-v2": hh3c_wx5002_v2,
       "hh3c-wx5004-v2": hh3c_wx5004_v2,
       "hh3c-secpathT1000-C": hh3c_secpathT1000_C,
       "hh3c-secBlade-LST1IPS1A1": hh3c_secBlade_LST1IPS1A1,
       "hh3c-secBlade-LST1FW2A1": hh3c_secBlade_LST1FW2A1,
       "hh3c-secBlade-LST1LB1A1": hh3c_secBlade_LST1LB1A1,
       "hh3c-secBlade-LST1NSM1A1": hh3c_secBlade_LST1NSM1A1,
       "hh3c-secBlade-EWPX2IAGSC0": hh3c_secBlade_EWPX2IAGSC0,
       "hh3c-F1000-A-EI": hh3c_F1000_A_EI,
       "hh3c-wx6108E": hh3c_wx6108E,
       "hh3c-wx6112E": hh3c_wx6112E,
       "hh3c-s5500-34C-HI": hh3c_s5500_34C_HI,
       "hh3c-s5500-58C-HI": hh3c_s5500_58C_HI,
       "hh3c-wa1208e-gp-h20": hh3c_wa1208e_gp_h20,
       "hh3c-S5120-9P-SI": hh3c_S5120_9P_SI,
       "hh3c-S5120-9P-PWR-SI": hh3c_S5120_9P_PWR_SI,
       "hh3c-S5120-9P-HPWR-SI": hh3c_S5120_9P_HPWR_SI,
       "hh3c-e528": hh3c_e528,
       "hh3c-e552": hh3c_e552,
       "hh3c-s3600V2-28TP-EI": hh3c_s3600V2_28TP_EI,
       "hh3c-s3600V2-52TP-EI": hh3c_s3600V2_52TP_EI,
       "hh3c-s3600V2-28TP-PWR-EI": hh3c_s3600V2_28TP_PWR_EI,
       "hh3c-s3600V2-52TP-PWR-EI": hh3c_s3600V2_52TP_PWR_EI,
       "hh3c-s3600V2-28F-EI": hh3c_s3600V2_28F_EI,
       "hh3c-s3600V2-28TP-SI": hh3c_s3600V2_28TP_SI,
       "hh3c-s3600V2-52TP-SI": hh3c_s3600V2_52TP_SI,
       "hh3c-s3600V2-28TP-PWR-SI": hh3c_s3600V2_28TP_PWR_SI,
       "hh3c-s3600V2-52TP-PWR-SI": hh3c_s3600V2_52TP_PWR_SI,
       "hh3c-s3500V2-28TP-EA": hh3c_s3500V2_28TP_EA,
       "hh3c-s3500V2-52TP-EA": hh3c_s3500V2_52TP_EA,
       "hh3c-s3500V2-28F-EA": hh3c_s3500V2_28F_EA,
       "hh3c-s3500V2-28TP-SI": hh3c_s3500V2_28TP_SI,
       "hh3c-s3500V2-52TP-SI": hh3c_s3500V2_52TP_SI,
       "hh3c-s9508E": hh3c_s9508E,
       "hh3c-s12504": hh3c_s12504,
       "hh3c-ICG2000B-GT": hh3c_ICG2000B_GT,
       "hh3c-ICG3000B": hh3c_ICG3000B,
       "hh3c-ICG3000S": hh3c_ICG3000S,
       "hh3c-ICG5000B": hh3c_ICG5000B,
       "hh3c-wh2640X-agnp": hh3c_wh2640X_agnp,
       "hh3c-wa2620X-agnp": hh3c_wa2620X_agnp,
       "hh3c-s3100-16TP-PWR-EI-F": hh3c_s3100_16TP_PWR_EI_F,
       "hh3c-cr16018": hh3c_cr16018,
       "hh3c-cr16008": hh3c_cr16008,
       "hh3c-cr16004": hh3c_cr16004,
       "hh3c-F1000-A-SI": hh3c_F1000_A_SI,
       "hh3c-F1000-E-SI": hh3c_F1000_E_SI,
       "hh3c-secBlade-LST1ACG1A1": hh3c_secBlade_LST1ACG1A1,
       "hh3c-secBlade-SPE-IPS": hh3c_secBlade_SPE_IPS,
       "hh3c-secBlade-SPE-ACG": hh3c_secBlade_SPE_ACG,
       "hh3c-wx6103": hh3c_wx6103,
       "hh3c-LSQ1WCMD0": hh3c_LSQ1WCMD0,
       "hh3c-EWPX2WCMD0": hh3c_EWPX2WCMD0,
       "hh3c-LSR1WCM3A1": hh3c_LSR1WCM3A1,
       "hh3c-S5830-52SC": hh3c_S5830_52SC,
       "hh3c-S5830-106S": hh3c_S5830_106S,
       "hh3c-ET814": hh3c_ET814,
       "hh3c-S5120-28P-LI": hh3c_S5120_28P_LI,
       "hh3c-S5120-52P-LI": hh3c_S5120_52P_LI,
       "hh3c-secBlade-IM-FW-II": hh3c_secBlade_IM_FW_II,
       "hh3c-secBlade-IM-LB": hh3c_secBlade_IM_LB,
       "hh3c-secBlade-IM-SSL": hh3c_secBlade_IM_SSL,
       "hh3c-ER2210C": hh3c_ER2210C,
       "hh3c-VCX-Connect-100": hh3c_VCX_Connect_100,
       "hh3c-VCX-Connect-200": hh3c_VCX_Connect_200,
       "hh3c-VCX-V7005": hh3c_VCX_V7005,
       "hh3c-VCX-V7205": hh3c_VCX_V7205,
       "hh3c-VCX-MIM": hh3c_VCX_MIM,
       "hh3c-VCX-Connect-MIM-Primary": hh3c_VCX_Connect_MIM_Primary,
       "hh3c-VCX-Connect-MIM-Secondary": hh3c_VCX_Connect_MIM_Secondary,
       "hh3c-VCX-V7310": hh3c_VCX_V7310,
       "hh3c-secBlade-IM-IPS": hh3c_secBlade_IM_IPS,
       "hh3c-secBlade-IM-ACG": hh3c_secBlade_IM_ACG,
       "hh3c-s7508E-X": hh3c_s7508E_X,
       "hh3c-s10504": hh3c_s10504,
       "hh3c-s10508": hh3c_s10508,
       "hh3c-s10508-V": hh3c_s10508_V,
       "hh3c-secBlade-SPE-FWM-200": hh3c_secBlade_SPE_FWM_200,
       "hh3c-secpathF1000-S-AI": hh3c_secpathF1000_S_AI,
       "hh3c-wx3024e-wcm": hh3c_wx3024e_wcm,
       "hh3c-wx3024e-lsw": hh3c_wx3024e_lsw,
       "hh3c-ER2100": hh3c_ER2100,
       "hh3c-S5820X-34TC": hh3c_S5820X_34TC,
       "hh3c-S5820X-34SC": hh3c_S5820X_34SC,
       "hh3c-S5820X-34C": hh3c_S5820X_34C,
       "hh3c-S5820X-64SC": hh3c_S5820X_64SC,
       "hh3c-cc720E": hh3c_cc720E,
       "hh3c-S2126T": hh3c_S2126T,
       "hh3c-S5800-54S": hh3c_S5800_54S,
       "hh3c-S5820X-26S": hh3c_S5820X_26S,
       "hh3c-S3100V2-8TP-SI": hh3c_S3100V2_8TP_SI,
       "hh3c-S3100V2-16TP-SI": hh3c_S3100V2_16TP_SI,
       "hh3c-S3100V2-26TP-SI": hh3c_S3100V2_26TP_SI,
       "hh3c-E126B": hh3c_E126B,
       "hh3c-S3100V2-8TP-EI": hh3c_S3100V2_8TP_EI,
       "hh3c-S3100V2-16TP-EI": hh3c_S3100V2_16TP_EI,
       "hh3c-S3100V2-26TP-EI": hh3c_S3100V2_26TP_EI,
       "hh3c-S3100V2-8TP-PWR-EI": hh3c_S3100V2_8TP_PWR_EI,
       "hh3c-S3100V2-16TP-PWR-EI": hh3c_S3100V2_16TP_PWR_EI,
       "hh3c-S3100V2-26TP-PWR-EI": hh3c_S3100V2_26TP_PWR_EI,
       "hh3c-S2008TP-EB": hh3c_S2008TP_EB,
       "hh3c-S2016TP-EB": hh3c_S2016TP_EB,
       "hh3c-S2403TP-EB": hh3c_S2403TP_EB,
       "hh3c-S2008TP-PWR-EB": hh3c_S2008TP_PWR_EB,
       "hh3c-S2016TP-PWR-EB": hh3c_S2016TP_PWR_EB,
       "hh3c-S2403TP-PWR-EB": hh3c_S2403TP_PWR_EB,
       "hh3c-S5800-LSW1FC4P0": hh3c_S5800_LSW1FC4P0,
       "hh3c-S2403TP-EA-SI-D": hh3c_S2403TP_EA_SI_D,
       "hh3c-S3528P-EA-D": hh3c_S3528P_EA_D,
       "hh3c-OAP-FIC-V2": hh3c_OAP_FIC_V2,
       "hh3c-OAP-MIM-V2": hh3c_OAP_MIM_V2,
       "hh3c-OAPS-MIM-V2": hh3c_OAPS_MIM_V2,
       "hh3c-S2008TP-PWR-EA": hh3c_S2008TP_PWR_EA,
       "hh3c-S2008TP-PWR-EA-DC": hh3c_S2008TP_PWR_EA_DC,
       "hh3c-S2016TP-PWR-EA": hh3c_S2016TP_PWR_EA,
       "hh3c-S2403TP-PWR-EA": hh3c_S2403TP_PWR_EA,
       "hh3c-S5120-24P-EI-D": hh3c_S5120_24P_EI_D,
       "hh3c-S5120-24P-PWR-EI-D": hh3c_S5120_24P_PWR_EI_D,
       "hh3c-S5120-48P-EI-D": hh3c_S5120_48P_EI_D,
       "hh3c-S5024P-EI": hh3c_S5024P_EI,
       "hh3c-S5500-28C-EI-D": hh3c_S5500_28C_EI_D,
       "hh3c-S5500-52C-EI-D": hh3c_S5500_52C_EI_D,
       "hh3c-S5500-28F-EI-D": hh3c_S5500_28F_EI_D,
       "hh3c-S5500-28C-EI-DC-D": hh3c_S5500_28C_EI_DC_D,
       "hh3c-MG9050": hh3c_MG9050,
       "hh3c-S5120-52SC-HI": hh3c_S5120_52SC_HI,
       "hh3c-CE3000-32F-EI": hh3c_CE3000_32F_EI,
       "hh3cS5830V224S": hh3cS5830V224S,
       "hh3cDC1801FH": hh3cDC1801FH,
       "hh3cDC2004FF": hh3cDC2004FF,
       "hh3cEC1101HF": hh3cEC1101HF,
       "hh3cEC1102HF": hh3cEC1102HF,
       "hh3cEC1501HF": hh3cEC1501HF,
       "hh3cEC1801HH": hh3cEC1801HH,
       "hh3cEC2516HF": hh3cEC2516HF,
       "hh3cEC2016HC": hh3cEC2016HC,
       "hh3cEC2016HC8CH": hh3cEC2016HC8CH,
       "hh3cEC2016HC4CH": hh3cEC2016HC4CH,
       "hh3cEC1504HF": hh3cEC1504HF,
       "hh3cHIC5421": hh3cHIC5421,
       "hh3cHIC5401": hh3cHIC5401,
       "hh3cHIC5221H": hh3cHIC5221H,
       "hh3cHIC5201H": hh3cHIC5201H,
       "hh3cVM8500": hh3cVM8500,
       "hh3cMS8500": hh3cMS8500,
       "hh3cDM8500": hh3cDM8500,
       "hh3cVX500": hh3cVX500,
       "hh3cISC3000E": hh3cISC3000E,
       "hh3cISC3000S": hh3cISC3000S,
       "hh3cCC700E": hh3cCC700E,
       "hh3cDC1001FF": hh3cDC1001FF,
       "hh3cECR3316HC": hh3cECR3316HC,
       "hh3cECR3308HD": hh3cECR3308HD,
       "hh3cECR3316HC8CH": hh3cECR3316HC8CH,
       "hh3cECR3316HC4CH": hh3cECR3316HC4CH,
       "hh3cECR3308HD4CH": hh3cECR3308HD4CH,
       "hh3cHIC65017L": hh3cHIC65017L,
       "hh3cEC2508HF": hh3cEC2508HF,
       "hh3cS3528EA": hh3cS3528EA,
       "hh3cS3552TPEA": hh3cS3552TPEA,
       "hh3cWP3024": hh3cWP3024,
       "hh3cWP3048": hh3cWP3048,
       "hh3cS3528FPEA": hh3cS3528FPEA,
       "hh3cE328B": hh3cE328B,
       "hh3cE352B": hh3cE352B,
       "hh3cE152B": hh3cE152B,
       "hh3cS3100V252TP": hh3cS3100V252TP,
       "hh3cWP2008": hh3cWP2008,
       "hh3cWP2016": hh3cWP2016,
       "hh3cWP2024": hh3cWP2024,
       "hh3cWP5024": hh3cWP5024,
       "hh3cWP5048": hh3cWP5048,
       "hh3cS2052TPEA": hh3cS2052TPEA,
       "hh3cS7604X": hh3cS7604X,
       "hh3cS7608X": hh3cS7608X,
       "hh3cS7608XV": hh3cS7608XV,
       "hh3cWA3620iAGN": hh3cWA3620iAGN,
       "hh3cWA3628iAGN": hh3cWA3628iAGN,
       "hh3cWA3610iGN": hh3cWA3610iGN,
       "hh3cCC750E": hh3cCC750E,
       "hh3cS5024FSI": hh3cS5024FSI,
       "hh3cS5820V252QF": hh3cS5820V252QF,
       "hh3cWA2110GN": hh3cWA2110GN,
       "hh3cMSR2010E": hh3cMSR2010E,
       "hh3cS10512": hh3cS10512,
       "hh3cS512028SCHI": hh3cS512028SCHI,
       "hh3cWA1208EGNP": hh3cWA1208EGNP,
       "hh3cWA2610EGNPH20": hh3cWA2610EGNPH20,
       "hh3cWA2620iAGN": hh3cWA2620iAGN,
       "hh3cWA2610iGN": hh3cWA2610iGN,
       "hh3cWA2612": hh3cWA2612,
       "hh3cWA2620": hh3cWA2620,
       "hh3cWB524": hh3cWB524,
       "hh3cSecBladeLST1FW3A1": hh3cSecBladeLST1FW3A1,
       "hh3cSecBladeLSU1FWCEA0": hh3cSecBladeLSU1FWCEA0,
       "hh3cWX3010eWCM": hh3cWX3010eWCM,
       "hh3cWX3010eLSW": hh3cWX3010eLSW,
       "hh3cSR6602X1": hh3cSR6602X1,
       "hh3cSR6602X2": hh3cSR6602X2,
       "hh3cSecBladeCRIMNAM1A": hh3cSecBladeCRIMNAM1A,
       "hh3cMSR2630": hh3cMSR2630,
       "hh3cMSR3610AC": hh3cMSR3610AC,
       "hh3cMSR3610DC": hh3cMSR3610DC,
       "hh3cMSR3620AC": hh3cMSR3620AC,
       "hh3cMSR3620DC": hh3cMSR3620DC,
       "hh3cMSR3620POE": hh3cMSR3620POE,
       "hh3cMSR3640": hh3cMSR3640,
       "hh3cMSR3660": hh3cMSR3660,
       "hh3cMSR5660": hh3cMSR5660,
       "hh3cMSR5680": hh3cMSR5680,
       "hh3cS512058CHI": hh3cS512058CHI,
       "hh3cS512034CHI": hh3cS512034CHI,
       "hh3cLSU3WCMD0": hh3cLSU3WCMD0,
       "hh3cEWPX3WCMD0": hh3cEWPX3WCMD0,
       "hh3cS7612X": hh3cS7612X,
       "hh3cWX6103E": hh3cWX6103E,
       "hh3cSecBladeCRIMFW1A": hh3cSecBladeCRIMFW1A,
       "hh3cHIC66216C": hh3cHIC66216C,
       "hh3cHIC66216L": hh3cHIC66216L,
       "hh3cHIC3401V": hh3cHIC3401V,
       "hh3cHIC3401VIR": hh3cHIC3401VIR,
       "hh3cHIC3421V": hh3cHIC3421V,
       "hh3cHIC3421VIR": hh3cHIC3421VIR,
       "hh3cSIC235IR1": hh3cSIC235IR1,
       "hh3cSIC235IR3": hh3cSIC235IR3,
       "hh3cSIC335EVIR": hh3cSIC335EVIR,
       "hh3cHIC5511I": hh3cHIC5511I,
       "hh3cHIC5521I": hh3cHIC5521I,
       "hh3cHIC5551I": hh3cHIC5551I,
       "hh3cHIC5421E": hh3cHIC5421E,
       "hh3cHIC5401E": hh3cHIC5401E,
       "hh3cHIC5421D": hh3cHIC5421D,
       "hh3cHIC5401D": hh3cHIC5401D,
       "hh3cHIC5621": hh3cHIC5621,
       "hh3cHIC5601": hh3cHIC5601,
       "hh3cHIC6501E": hh3cHIC6501E,
       "hh3cHIC6621E": hh3cHIC6621E,
       "hh3cSIC635": hh3cSIC635,
       "hh3cHIC6501IR": hh3cHIC6501IR,
       "hh3cHIC6621IR": hh3cHIC6621IR,
       "hh3cSIC635IR": hh3cSIC635IR,
       "hh3cEC2508HF4CH": hh3cEC2508HF4CH,
       "hh3cEC2516HF8CH": hh3cEC2516HF8CH,
       "hh3cECR3308HF": hh3cECR3308HF,
       "hh3cECR3316HF": hh3cECR3316HF,
       "hh3cISC3500E": hh3cISC3500E,
       "hh3cISC3500S": hh3cISC3500S,
       "hh3cECR3304HFE": hh3cECR3304HFE,
       "hh3cECR3308HFE": hh3cECR3308HFE,
       "hh3cECR3316HFE": hh3cECR3316HFE,
       "hh3cISC3600": hh3cISC3600,
       "hh3cECR3204HW": hh3cECR3204HW,
       "hh3cECR3208HW": hh3cECR3208HW,
       "hh3cECR3216HW": hh3cECR3216HW,
       "hh3cEC2508HW": hh3cEC2508HW,
       "hh3cEC2516HW": hh3cEC2516HW,
       "hh3cISC2600": hh3cISC2600,
       "hh3cDC2808FH": hh3cDC2808FH,
       "hh3cCE300034C": hh3cCE300034C,
       "hh3cCE300058C": hh3cCE300058C,
       "hh3cSR6604X": hh3cSR6604X,
       "hh3cSR6608X": hh3cSR6608X,
       "hh3cSR6616X": hh3cSR6616X,
       "hh3csecpathF100AG": hh3csecpathF100AG,
       "hh3csecpathF100CG": hh3csecpathF100CG,
       "hh3csecpathF100EG": hh3csecpathF100EG,
       "hh3csecpathF100MG": hh3csecpathF100MG,
       "hh3csecpathF100SG": hh3csecpathF100SG,
       "hh3cS3100V226TPWiNet": hh3cS3100V226TPWiNet,
       "hh3cS550024PWiNet": hh3cS550024PWiNet,
       "hh3cS512028PPoeWiNet": hh3cS512028PPoeWiNet,
       "hh3cS512028PWiNet": hh3cS512028PWiNet,
       "hh3cS550034CPWRHI": hh3cS550034CPWRHI,
       "hh3cS550058CPWRHI": hh3cS550058CPWRHI,
       "hh3cS550034FHI": hh3cS550034FHI,
       "hh3cMSR930": hh3cMSR930,
       "hh3cMSV50": hh3cMSV50,
       "hh3cMSR930WiNet": hh3cMSR930WiNet,
       "hh3cMSR930GU": hh3cMSR930GU,
       "hh3cMSR930sa": hh3cMSR930sa,
       "hh3cMSR930GG": hh3cMSR930GG,
       "hh3cS5820V254QSGE": hh3cS5820V254QSGE,
       "hh3cS5820V252Q": hh3cS5820V252Q,
       "hh3cCC754E": hh3cCC754E,
       "hh3cWP5008": hh3cWP5008,
       "hh3cSecBladeCRIMLB1A": hh3cSecBladeCRIMLB1A,
       "hh3cS550034CHID": hh3cS550034CHID,
       "hh3cS550058CHID": hh3cS550058CHID,
       "hh3cS9505EV7": hh3cS9505EV7,
       "hh3cS9508EV7": hh3cS9508EV7,
       "hh3cS9508EVV7": hh3cS9508EVV7,
       "hh3cS9512EV7": hh3cS9512EV7,
       "hh3cS12508V7": hh3cS12508V7,
       "hh3cS12518V7": hh3cS12518V7,
       "hh3cS12504V7": hh3cS12504V7,
       "hh3csecpathF100CAI": hh3csecpathF100CAI,
       "hh3csecpathL1000A": hh3csecpathL1000A,
       "hh3cWA2610E": hh3cWA2610E,
       "hh3cWA2620E": hh3cWA2620E,
       "hh3cWA2620X": hh3cWA2620X,
       "hh3cWA2610X": hh3cWA2610X,
       "hh3cS6802": hh3cS6802,
       "hh3cS9804": hh3cS9804,
       "hh3cSecBladeLSU1IPSBEA0": hh3cSecBladeLSU1IPSBEA0,
       "hh3cSecBladeLST1IPS2A1": hh3cSecBladeLST1IPS2A1,
       "hh3cMSR930W": hh3cMSR930W,
       "hh3cMSR930WGU": hh3cMSR930WGU,
       "hh3cSecPathF5000C": hh3cSecPathF5000C,
       "hh3cSecPathF5000S": hh3cSecPathF5000S,
       "hh3cS12510FDC": hh3cS12510FDC,
       "hh3cS12510FAC": hh3cS12510FAC,
       "hh3cS12510XDC": hh3cS12510XDC,
       "hh3cS12510XAC": hh3cS12510XAC,
       "hh3cS12508": hh3cS12508,
       "hh3cS12518": hh3cS12518,
       "hh3cS12516FDC": hh3cS12516FDC,
       "hh3cS12516FAC": hh3cS12516FAC,
       "hh3cS12516XDC": hh3cS12516XDC,
       "hh3cS12516XAC": hh3cS12516XAC,
       "hh3cMSR930GT": hh3cMSR930GT,
       "hh3cMSR2600GTC": hh3cMSR2600GTC,
       "hh3cMSR2600GUC": hh3cMSR2600GUC,
       "hh3csecpathF1000AG": hh3csecpathF1000AG,
       "hh3csecpathF1000CG": hh3csecpathF1000CG,
       "hh3csecpathF1000SG": hh3csecpathF1000SG,
       "hh3cSecBladeLSQ2FWBSCO": hh3cSecBladeLSQ2FWBSCO,
       "hh3cWA2620AGN": hh3cWA2620AGN,
       "hh3cVSR": hh3cVSR,
       "hh3cVSR1001": hh3cVSR1001,
       "hh3cVSR1004": hh3cVSR1004,
       "hh3cVSR1008": hh3cVSR1008,
       "hh3cS5120S28PEI": hh3cS5120S28PEI,
       "hh3cS5120S52PEI": hh3cS5120S52PEI,
       "hh3cMSR930WiNetW": hh3cMSR930WiNetW,
       "hh3cWA3628iAGNX": hh3cWA3628iAGNX,
       "hh3cS2110": hh3cS2110,
       "hh3cS2110PWR": hh3cS2110PWR,
       "hh3cS2126": hh3cS2126,
       "hh3cS2126PWR": hh3cS2126PWR,
       "hh3cS2152": hh3cS2152,
       "hh3cWX5540WCM": hh3cWX5540WCM,
       "hh3cWX5540LSW": hh3cWX5540LSW,
       "hh3cWX5520WCM": hh3cWX5520WCM,
       "hh3cWX5520LSW": hh3cWX5520LSW,
       "hh3cMSR930WGT": hh3cMSR930WGT,
       "hh3cICG5000T": hh3cICG5000T,
       "hh3cICG6000": hh3cICG6000,
       "hh3cMSR2630WiNet": hh3cMSR2630WiNet,
       "hh3cMSR3610WiNet": hh3cMSR3610WiNet,
       "hh3cMSR3660WiNet": hh3cMSR3660WiNet,
       "hh3cMSR260010": hh3cMSR260010,
       "hh3cMSR260010WiNet": hh3cMSR260010WiNet,
       "hh3cMSR260017": hh3cMSR260017,
       "hh3cICG3000D": hh3cICG3000D,
       "hh3cICG3000E": hh3cICG3000E,
       "hh3cSecBladeLSU1ADECEA0": hh3cSecBladeLSU1ADECEA0,
       "hh3cSecBladeLST1ADE1A1": hh3cSecBladeLST1ADE1A1,
       "hh3cSR8804X": hh3cSR8804X,
       "hh3cSR8808X": hh3cSR8808X,
       "hh3cSR8812X": hh3cSR8812X,
       "hh3cCC710E": hh3cCC710E,
       "hh3cCC712E": hh3cCC712E,
       "hh3cS680032Q": hh3cS680032Q,
       "hh3cS5008PV2EI": hh3cS5008PV2EI,
       "hh3cS5024PV2EI": hh3cS5024PV2EI,
       "hh3cS5048PV2EI": hh3cS5048PV2EI,
       "hh3cS2610": hh3cS2610,
       "hh3cS2610PWR": hh3cS2610PWR,
       "hh3cS2626": hh3cS2626,
       "hh3cS2626PWR": hh3cS2626PWR,
       "hh3cS2652": hh3cS2652,
       "hh3cSimware7BoxCen": hh3cSimware7BoxCen,
       "hh3cSimware7BoxIRF": hh3cSimware7BoxIRF,
       "hh3cSimware7ChassisDevice": hh3cSimware7ChassisDevice,
       "hh3cVSR1000": hh3cVSR1000,
       "hh3csecpathM9000": hh3csecpathM9000,
       "hh3csecpathM9006": hh3csecpathM9006,
       "hh3csecpathM9010": hh3csecpathM9010,
       "hh3csecpathM9014": hh3csecpathM9014,
       "hh3cSecBladeIIINSQM1FWCEA0": hh3cSecBladeIIINSQM1FWCEA0,
       "hh3cWB521X": hh3cWB521X,
       "hh3cWB511X": hh3cWB511X,
       "hh3cER3108G": hh3cER3108G,
       "hh3cER3108GW": hh3cER3108GW,
       "hh3cS513028SEI": hh3cS513028SEI,
       "hh3cS513052SEI": hh3cS513052SEI,
       "hh3cS513028FEI": hh3cS513028FEI,
       "hh3cS513028SPWREI": hh3cS513028SPWREI,
       "hh3cS513052SPWREI": hh3cS513052SPWREI,
       "hh3cMSR360028": hh3cMSR360028,
       "hh3cMSR360051": hh3cMSR360051,
       "hh3cWA2612E": hh3cWA2612E,
       "hh3cWA2622": hh3cWA2622,
       "hh3cS511010P": hh3cS511010P,
       "hh3cS511010PPWR": hh3cS511010PPWR,
       "hh3cS511028P": hh3cS511028P,
       "hh3cS511028PPWR": hh3cS511028PPWR,
       "hh3cS511052P": hh3cS511052P,
       "hh3cS511010PD": hh3cS511010PD,
       "hh3cS511010PPWRD": hh3cS511010PPWRD,
       "hh3cS511028PD": hh3cS511028PD,
       "hh3cS511028PPWRD": hh3cS511028PPWRD,
       "hh3cS511052PD": hh3cS511052PD,
       "hh3cWX5510": hh3cWX5510,
       "hh3cS550028SCHI": hh3cS550028SCHI,
       "hh3cS550052SCHI": hh3cS550052SCHI,
       "hh3cS550028SCHID": hh3cS550028SCHID,
       "hh3cS550052SCHID": hh3cS550052SCHID,
       "hh3cLA2608": hh3cLA2608,
       "hh3cS311010TP": hh3cS311010TP,
       "hh3cS311010TPPWR": hh3cS311010TPPWR,
       "hh3cS311026TP": hh3cS311026TP,
       "hh3cS311026TPPWR": hh3cS311026TPPWR,
       "hh3cS311052TP": hh3cS311052TP,
       "hh3cWA2610HGN": hh3cWA2610HGN,
       "hh3cWA4620EACN": hh3cWA4620EACN,
       "hh3cWA4620IACN": hh3cWA4620IACN,
       "hh3cEWPX1MAC0": hh3cEWPX1MAC0,
       "hh3cCRIMMAC1A": hh3cCRIMMAC1A,
       "hh3cSecBladeIIILST1FW3B1": hh3cSecBladeIIILST1FW3B1,
       "hh3cWA2620iAGNX": hh3cWA2620iAGNX,
       "hh3cS311010TPSI": hh3cS311010TPSI,
       "hh3cS311026TPSI": hh3cS311026TPSI,
       "hh3cS311052TPSI": hh3cS311052TPSI,
       "hh3cS511010PSI": hh3cS511010PSI,
       "hh3cS511028PSI": hh3cS511028PSI,
       "hh3cS511052PSI": hh3cS511052PSI,
       "hh3cS3100V252TPWiNet": hh3cS3100V252TPWiNet,
       "hh3cS512052PWiNet": hh3cS512052PWiNet,
       "hh3cS550048PWiNet": hh3cS550048PWiNet,
       "hh3cS550028FWiNet": hh3cS550028FWiNet,
       "hh3CWA2620EX": hh3CWA2620EX,
       "hh3csecpathL5000S": hh3csecpathL5000S,
       "hh3csecpathL5000C": hh3csecpathL5000C,
       "hh3cCC721E": hh3cCC721E,
       "hh3cS5820V252QFU": hh3cS5820V252QFU,
       "hh3csecpathVFW1000": hh3csecpathVFW1000,
       "hh3cS7003": hh3cS7003,
       "hh3cS7006": hh3cS7006,
       "hh3csecpathF100CSI": hh3csecpathF100CSI,
       "hh3cWX3510E": hh3cWX3510E,
       "hh3cWX3540E": hh3cWX3540E,
       "hh3cSecBladeLSU3FWCEA0": hh3cSecBladeLSU3FWCEA0,
       "hh3cSecBladeLSU1NSCEA0": hh3cSecBladeLSU1NSCEA0,
       "hh3cSecBladeLST1FW3C1": hh3cSecBladeLST1FW3C1,
       "hh3cSecBladeLST1NSM2C1": hh3cSecBladeLST1NSM2C1,
       "hh3cSecBladeLSX1FWCEA1": hh3cSecBladeLSX1FWCEA1,
       "hh3cSecBladeLSX1NSCEA1": hh3cSecBladeLSX1NSCEA1,
       "hh3cWA2620AGNC": hh3cWA2620AGNC,
       "hh3cWA2610GN": hh3cWA2610GN,
       "hh3cWA2610GNE": hh3cWA2610GNE,
       "hh3cMSR800": hh3cMSR800,
       "hh3cMSR800Wlan": hh3cMSR800Wlan,
       "hh3cMSR80010": hh3cMSR80010,
       "hh3cMSR80010Wlan": hh3cMSR80010Wlan,
       "hh3cMSR830WiNet": hh3cMSR830WiNet,
       "hh3cMSR83010WiNet": hh3cMSR83010WiNet,
       "hh3cMSR93010WiNet": hh3cMSR93010WiNet,
       "hh3cS9810": hh3cS9810,
       "hh3cFlexNetworkB6300XLG": hh3cFlexNetworkB6300XLG,
       "hh3cFlexNetworkB6300GXG": hh3cFlexNetworkB6300GXG,
       "hh3cMSR900E": hh3cMSR900E,
       "hh3cMSR900EWlan": hh3cMSR900EWlan,
       "hh3cS513028SEID": hh3cS513028SEID,
       "hh3cS513052SEID": hh3cS513052SEID,
       "hh3cS513028FEID": hh3cS513028FEID,
       "hh3cS513028SHPWREID": hh3cS513028SHPWREID,
       "hh3cS513052SPWREID": hh3cS513052SPWREID,
       "hh3cS513028SHPWREI": hh3cS513028SHPWREI,
       "hh3cE528X": hh3cE528X,
       "hh3cE552X": hh3cE552X,
       "hh3cLSU1WCME0": hh3cLSU1WCME0,
       "hh3cEWPX1WCME0": hh3cEWPX1WCME0,
       "hh3cSR8810XS": hh3cSR8810XS,
       "hh3cSR8806XS": hh3cSR8806XS,
       "hh3cSR8803XS": hh3cSR8803XS,
       "hh3cSR8802XS": hh3cSR8802XS,
       "hh3cSecPathF5020": hh3cSecPathF5020,
       "hh3cSecPathF5040": hh3cSecPathF5040,
       "hh3cRA100": hh3cRA100,
       "hh3cMSR930LM": hh3cMSR930LM,
       "hh3cMSR930WLM": hh3cMSR930WLM,
       "hh3cMSR26005LMC": hh3cMSR26005LMC,
       "hh3cS580032CEI": hh3cS580032CEI,
       "hh3cS580056CEI": hh3cS580056CEI,
       "hh3cS580032CPWREI": hh3cS580032CPWREI,
       "hh3cS580056CPWREI": hh3cS580056CPWREI,
       "hh3cS580056CEIM": hh3cS580056CEIM,
       "hh3cWB521XE": hh3cWB521XE,
       "hh3cWB521XH": hh3cWB521XH,
       "hh3cWX2540E": hh3cWX2540E,
       "hh3cWX360": hh3cWX360,
       "hh3cWX361": hh3cWX361,
       "hh3cWA2610EGNE": hh3cWA2610EGNE,
       "hh3cSR6603F": hh3cSR6603F,
       "hh3cSR6605F": hh3cSR6605F,
       "hh3cSR6609F": hh3cSR6609F,
       "hh3cS556030SEI": hh3cS556030SEI,
       "hh3cS556054SEI": hh3cS556054SEI,
       "hh3cS556030CEI": hh3cS556030CEI,
       "hh3cS556054CEI": hh3cS556054CEI,
       "hh3cS556030CPWREI": hh3cS556030CPWREI,
       "hh3cS556054CPWREI": hh3cS556054CPWREI,
       "hh3cS556054QSEI": hh3cS556054QSEI,
       "hh3cRA200": hh3cRA200,
       "hh3cF1000CSI": hh3cF1000CSI,
       "hh3cF100MSI": hh3cF100MSI,
       "hh3cF100ASI": hh3cF100ASI,
       "hh3cS5820V248S": hh3cS5820V248S,
       "hh3cS630042QT": hh3cS630042QT,
       "hh3cS630042QF": hh3cS630042QF,
       "hh3cS630048S": hh3cS630048S,
       "hh3cS630052QF": hh3cS630052QF,
       "hh3cFlexNetworkU830048G": hh3cFlexNetworkU830048G,
       "hh3cFlexNetworkU830048XLGU": hh3cFlexNetworkU830048XLGU,
       "hh3cS5008PV2EIPWR": hh3cS5008PV2EIPWR,
       "hh3cS5024PV2EIPWR": hh3cS5024PV2EIPWR,
       "hh3cS511052PPWR": hh3cS511052PPWR,
       "hh3cS511052PPWRD": hh3cS511052PPWRD,
       "hh3cNSC1000": hh3cNSC1000,
       "hh3cMS4308": hh3cMS4308,
       "hh3cMS4308PWR": hh3cMS4308PWR,
       "hh3cS513028TPEI": hh3cS513028TPEI,
       "hh3cS513052TPEI": hh3cS513052TPEI,
       "hh3cS513028TPPWREI": hh3cS513028TPPWREI,
       "hh3cS513052TPPWREI": hh3cS513052TPPWREI,
       "hh3csecpathF1020": hh3csecpathF1020,
       "hh3csecpathF1030": hh3csecpathF1030,
       "hh3csecpathF1050": hh3csecpathF1050,
       "hh3csecpathF1060": hh3csecpathF1060,
       "hh3csecpathF1070": hh3csecpathF1070,
       "hh3csecpathF1080": hh3csecpathF1080,
       "hh3csecpathVMSGVLB1000": hh3csecpathVMSGVLB1000,
       "hh3cS5864F": hh3cS5864F,
       "hh3cS5864UF": hh3cS5864UF,
       "hh3cS5864TF": hh3cS5864TF,
       "hh3cS6348F": hh3cS6348F,
       "hh3cS6348TF": hh3cS6348TF,
       "hh3cCR16006F": hh3cCR16006F,
       "hh3cCR16010F": hh3cCR16010F,
       "hh3cCR16014F": hh3cCR16014F,
       "hh3cSecPathM9000Context": hh3cSecPathM9000Context,
       "hh3cICG3000SE": hh3cICG3000SE,
       "hh3cS68004C": hh3cS68004C,
       "hh3cS68002C": hh3cS68002C,
       "hh3cSR8803F": hh3cSR8803F,
       "hh3cSR8805F": hh3cSR8805F,
       "hh3cSR8808F": hh3cSR8808F,
       "hh3cSR8812F": hh3cSR8812F,
       "hh3cS12516XAF": hh3cS12516XAF,
       "hh3cvAC": hh3cvAC,
       "hh3cWX8700": hh3cWX8700,
       "hh3cS556030FEI": hh3cS556030FEI,
       "hh3cS5530CEID": hh3cS5530CEID,
       "hh3cS5554CEID": hh3cS5554CEID,
       "hh3cS5530CPWREID": hh3cS5530CPWREID,
       "hh3cS5554CPWREID": hh3cS5554CPWREID,
       "hh3cS5530FEID": hh3cS5530FEID,
       "hh3cS513028SSI": hh3cS513028SSI,
       "hh3cS513052SSI": hh3cS513052SSI,
       "hh3cS513028FSI": hh3cS513028FSI,
       "hh3cS556028SSI": hh3cS556028SSI,
       "hh3cS556052SSI": hh3cS556052SSI,
       "hh3cS556028FSI": hh3cS556028FSI,
       "hh3cLA4608E": hh3cLA4608E,
       "hh3cWA4320ACN": hh3cWA4320ACN,
       "hh3cWA4320iACN": hh3cWA4320iACN,
       "hh3cWA4320iX": hh3cWA4320iX,
       "hh3cWA4320TS": hh3cWA4320TS,
       "hh3cWA4320TQ": hh3cWA4320TQ,
       "hh3cWA4320HACN": hh3cWA4320HACN,
       "hh3cS10506": hh3cS10506,
       "hh3cS10510": hh3cS10510,
       "hh3cS7606X": hh3cS7606X,
       "hh3cS7610X": hh3cS7610X,
       "hh3cMSR930AC": hh3cMSR930AC,
       "hh3cMSR930ACWiNet": hh3cMSR930ACWiNet,
       "hh3cSecPathACG1000E": hh3cSecPathACG1000E,
       "hh3cSecPathACG1000A": hh3cSecPathACG1000A,
       "hh3cSecPathACG1000M": hh3cSecPathACG1000M,
       "hh3cSecPathACG1000S": hh3cSecPathACG1000S,
       "hh3cSecPathACG1000C": hh3cSecPathACG1000C,
       "hh3cVBRAS1000": hh3cVBRAS1000,
       "hh3cVSR1000P": hh3cVSR1000P,
       "hh3cBRAS1000P": hh3cBRAS1000P,
       "hh3cS12508XAF": hh3cS12508XAF,
       "hh3cLA3616SGM": hh3cLA3616SGM,
       "hh3cLA3616SGT": hh3cLA3616SGT,
       "hh3cLA3616EGM": hh3cLA3616EGM,
       "hh3cWAP722E": hh3cWAP722E,
       "hh3cWAP722": hh3cWAP722,
       "hh3cER2100n": hh3cER2100n,
       "hh3cER2100V2": hh3cER2100V2,
       "hh3cWX5560H": hh3cWX5560H,
       "hh3cWX5580H": hh3cWX5580H,
       "hh3cWAP621": hh3cWAP621,
       "hh3cMSR810W": hh3cMSR810W,
       "hh3cER3260G2": hh3cER3260G2,
       "hh3cER5100G2": hh3cER5100G2,
       "hh3cER5200G2": hh3cER5200G2,
       "hh3cER6300G2": hh3cER6300G2,
       "hh3cER8300G2": hh3cER8300G2,
       "hh3cER8300G2X": hh3cER8300G2X,
       "hh3cS99004F": hh3cS99004F,
       "hh3cS990010F": hh3cS990010F,
       "hh3cSecBladeLSU1ADECEA01": hh3cSecBladeLSU1ADECEA01,
       "hh3cSecBladeLSXM1ADECEA1": hh3cSecBladeLSXM1ADECEA1,
       "hh3cS69002F": hh3cS69002F,
       "hh3cS69004F": hh3cS69004F,
       "hh3cS6348SF": hh3cS6348SF,
       "hh3cS6364F": hh3cS6364F,
       "hh3cS5848F": hh3cS5848F,
       "hh3cS1808G": hh3cS1808G,
       "hh3cS1824G": hh3cS1824G,
       "hh3cS1848G": hh3cS1848G,
       "hh3cSecPathACG1010": hh3cSecPathACG1010,
       "hh3cSecPathACG1020": hh3cSecPathACG1020,
       "hh3cSecPathACG1030": hh3cSecPathACG1030,
       "hh3cSecPathACG1040": hh3cSecPathACG1040,
       "hh3cWX3510H": hh3cWX3510H,
       "hh3cWX3520H": hh3cWX3520H,
       "hh3cWX3540H": hh3cWX3540H,
       "hh3cWX5540H": hh3cWX5540H,
       "hh3cLA3608E": hh3cLA3608E,
       "hh3cLA3608EDB": hh3cLA3608EDB,
       "hh3cS513030SHI": hh3cS513030SHI,
       "hh3cS513054SHI": hh3cS513054SHI,
       "hh3cS513030CHI": hh3cS513030CHI,
       "hh3cS513054CHI": hh3cS513054CHI,
       "hh3cS513030CPWRHI": hh3cS513030CPWRHI,
       "hh3cS513054CPWRHI": hh3cS513054CPWRHI,
       "hh3cS513054QSHI": hh3cS513054QSHI,
       "hh3cS513030FHI": hh3cS513030FHI,
       "hh3cS12516FAF": hh3cS12516FAF,
       "hh3cS12508FAF": hh3cS12508FAF,
       "hh3cS12504XAF": hh3cS12504XAF,
       "hh3cS12504FAF": hh3cS12504FAF,
       "hh3cMS410010TP": hh3cMS410010TP,
       "hh3cMS410010TPPWR": hh3cMS410010TPPWR,
       "hh3cMS410026TP": hh3cMS410026TP,
       "hh3cMS410026TPPWR": hh3cMS410026TPPWR,
       "hh3cMS430052P": hh3cMS430052P,
       "hh3cMS430028P": hh3cMS430028P,
       "hh3cIE410012TP": hh3cIE410012TP,
       "hh3cIE410020TP": hh3cIE410020TP,
       "hh3cIE410028F": hh3cIE410028F,
       "hh3cIE430028P": hh3cIE430028P,
       "hh3cS680054QF": hh3cS680054QF,
       "hh3cMS432028S": hh3cMS432028S,
       "hh3cMS432052S": hh3cMS432052S,
       "hh3cMS432028F": hh3cMS432028F,
       "hh3cMS432028SPWR": hh3cMS432028SPWR,
       "hh3cMS452028TP": hh3cMS452028TP,
       "hh3cMS452030F": hh3cMS452030F,
       "hh3cLA4310": hh3cLA4310,
       "hh3cLA4310V": hh3cLA4310V,
       "hh3cLA4320": hh3cLA4320,
       "hh3cLA4320V": hh3cLA4320V,
       "hh3cWA4320X": hh3cWA4320X,
       "hh3cLA4320X": hh3cLA4320X,
       "hh3cSecBlade4NSQM1FWDFG0": hh3cSecBlade4NSQM1FWDFG0,
       "hh3cWX5510EV7": hh3cWX5510EV7,
       "hh3cWX5540EV7": hh3cWX5540EV7,
       "hh3cSecPathL1000E": hh3cSecPathL1000E,
       "hh3cSecPathL1000M": hh3cSecPathL1000M,
       "hh3cSecPathL1000S": hh3cSecPathL1000S,
       "hh3cSecPathF5000Context": hh3cSecPathF5000Context,
       "hh3cSecPathF1000Context": hh3cSecPathF1000Context,
       "hh3cSecPathL5000Context": hh3cSecPathL5000Context,
       "hh3cSecPathL1000Context": hh3cSecPathL1000Context,
       "hh3cWA4320TQV": hh3cWA4320TQV,
       "hh3cMSR810WDB": hh3cMSR810WDB,
       "hh3cMSR810LM": hh3cMSR810LM,
       "hh3cMSR810WLM": hh3cMSR810WLM,
       "hh3cS682032H": hh3cS682032H,
       "hh3cS682054HF": hh3cS682054HF,
       "hh3cMSR5620": hh3cMSR5620,
       "hh3cMSR3620DP": hh3cMSR3620DP,
       "hh3cMSR810WWiNet": hh3cMSR810WWiNet,
       "hh3cMSR810LMWiNet": hh3cMSR810LMWiNet,
       "hh3cRA100AC": hh3cRA100AC,
       "hh3cMSR360028WiNet": hh3cMSR360028WiNet,
       "hh3cMSR3620WiNet": hh3cMSR3620WiNet,
       "hh3cS680054QT": hh3cS680054QT,
       "hh3cS12504S": hh3cS12504S,
       "hh3cS12506S": hh3cS12506S,
       "hh3cS12510S": hh3cS12510S,
       "hh3cS12508S": hh3cS12508S,
       "hh3cS12512S": hh3cS12512S,
       "hh3cS515024SPWREI": hh3cS515024SPWREI,
       "hh3cS5150X16SEI": hh3cS5150X16SEI,
       "hh3cS5150X16STEI": hh3cS5150X16STEI,
       "hh3cSecPathF100AG2": hh3cSecPathF100AG2,
       "hh3cSecPathF1000CG2": hh3cSecPathF1000CG2,
       "hh3cUISM831048G": hh3cUISM831048G,
       "hh3cUISM832048XG": hh3cUISM832048XG,
       "hh3cUISM6300XLG": hh3cUISM6300XLG,
       "hh3cMSR810": hh3cMSR810,
       "hh3cSecPathW2001": hh3cSecPathW2001,
       "hh3cSecPathW2005": hh3cSecPathW2005,
       "hh3cSecPathW2010": hh3cSecPathW2010,
       "hh3cSecPathW2020": hh3cSecPathW2020,
       "hh3cSecPathW2040": hh3cSecPathW2040,
       "hh3cSecPathW2080": hh3cSecPathW2080,
       "hh3cSecPathW2200": hh3cSecPathW2200,
       "hh3cSecPathW1020D": hh3cSecPathW1020D,
       "hh3cSecPathW1040D": hh3cSecPathW1040D,
       "hh3cSecPathW1200D": hh3cSecPathW1200D,
       "hh3cSecPathA2020": hh3cSecPathA2020,
       "hh3cSecPathA2100": hh3cSecPathA2100,
       "hh3cSecPathD2020": hh3cSecPathD2020,
       "hh3cSecPathD2050": hh3cSecPathD2050,
       "hh3cS556034CEI": hh3cS556034CEI,
       "hh3cS513034CHI": hh3cS513034CHI,
       "hh3cMS412026TP": hh3cMS412026TP,
       "hh3cWA4330ACN": hh3cWA4330ACN,
       "hh3cMS4320S28F": hh3cMS4320S28F,
       "hh3cMS4320S28P": hh3cMS4320S28P,
       "hh3cMS452028S": hh3cMS452028S,
       "hh3cSecBlade3Context": hh3cSecBlade3Context,
       "hh3cMSR2630R": hh3cMSR2630R,
       "hh3cMSR3610ACR": hh3cMSR3610ACR,
       "hh3cMSR3620ACR": hh3cMSR3620ACR,
       "hh3cMSR3640R": hh3cMSR3640R,
       "hh3cMSR3660R": hh3cMSR3660R,
       "hh3cMSR5660R": hh3cMSR5660R,
       "hh3cMSR5680R": hh3cMSR5680R,
       "hh3cMSR930R": hh3cMSR930R,
       "hh3cMSR930WR": hh3cMSR930WR,
       "hh3cMSR260010R": hh3cMSR260010R,
       "hh3cWX3010EV7": hh3cWX3010EV7,
       "hh3cWX3024EV7": hh3cWX3024EV7,
       "hh3cWCMX20": hh3cWCMX20,
       "hh3cS556032CHI": hh3cS556032CHI,
       "hh3cS556056CHI": hh3cS556056CHI,
       "hh3cS556056CPWRHI": hh3cS556056CPWRHI,
       "hh3cS12502XAF": hh3cS12502XAF,
       "hh3cNS228": hh3cNS228,
       "hh3cNS252": hh3cNS252,
       "hh3cSecBladeFW": hh3cSecBladeFW,
       "hh3cSecBladeADE": hh3cSecBladeADE,
       "hh3cSecBladeIIILSUM1FWCEAB0": hh3cSecBladeIIILSUM1FWCEAB0,
       "hh3cS513028PSEI": hh3cS513028PSEI,
       "hh3cS7506EX": hh3cS7506EX,
       "hh3cS7510EX": hh3cS7510EX,
       "hh3cS7504EXS": hh3cS7504EXS,
       "hh3cS7502EXS": hh3cS7502EXS,
       "hh3cWA4320ACNPI": hh3cWA4320ACNPI,
       "hh3cWA4320ACNSI": hh3cWA4320ACNSI,
       "hpSwitch": hpSwitch,
       "hp7502": hp7502,
       "hp7503S": hp7503S,
       "hp7503": hp7503,
       "hp7506": hp7506,
       "hp7506V": hp7506V,
       "hp7510": hp7510,
       "hpA36002POLT": hpA36002POLT,
       "hpV190524": hpV190524,
       "hpV190524POE": hpV190524POE,
       "hpV190548": hpV190548,
       "hpA512016GSI": hpA512016GSI,
       "hpA512024GSI": hpA512024GSI,
       "hpA512048GSI": hpA512048GSI,
       "hpA512024GPPOESI": hpA512024GPPOESI,
       "hpA512024GPOESI": hpA512024GPOESI,
       "hpA580024G": hpA580024G,
       "hpA580024GPoEPlus": hpA580024GPoEPlus,
       "hpA580048G": hpA580048G,
       "hpA580048GPoEPlus": hpA580048GPoEPlus,
       "hpA580024GSFP": hpA580024GSFP,
       "hpA580048GPoEPlus2SLOT": hpA580048GPoEPlus2SLOT,
       "hpA5820X14XGSFPPlus2SLOT": hpA5820X14XGSFPPlus2SLOT,
       "hpA5820X24XGSFPPlus": hpA5820X24XGSFPPlus,
       "hpA550024GEI2SLOT": hpA550024GEI2SLOT,
       "hpA550048GEI2SLOT": hpA550048GEI2SLOT,
       "hpA550024GPoEPlusEI2SLOT": hpA550024GPoEPlusEI2SLOT,
       "hpA550048GPoEPlusEI2SLOT": hpA550048GPoEPlusEI2SLOT,
       "hpA550024GSFPEI2SLOT": hpA550024GSFPEI2SLOT,
       "hpA550024GSI2SLOT": hpA550024GSI2SLOT,
       "hpA550048GSI2SLOT": hpA550048GSI2SLOT,
       "hpA550024GPoEPlusSI2SLOT": hpA550024GPoEPlusSI2SLOT,
       "hpA550048GPoEPlusSI2SLOT": hpA550048GPoEPlusSI2SLOT,
       "hpA512024GEI2SLOT": hpA512024GEI2SLOT,
       "hpA512048GEI2SLOT": hpA512048GEI2SLOT,
       "hpA512024GPoEPlusEI2SLOT": hpA512024GPoEPlusEI2SLOT,
       "hpA512048GPoEPlusEI2SLOT": hpA512048GPoEPlusEI2SLOT,
       "hpA512024GEI": hpA512024GEI,
       "hpA512048GEI": hpA512048GEI,
       "hp9505": hp9505,
       "hp9508V": hp9508V,
       "hp9508": hp9508,
       "hp9512": hp9512,
       "hp12508": hp12508,
       "hp12518": hp12518,
       "hp12504AC": hp12504AC,
       "hpA5800AF48G": hpA5800AF48G,
       "hpA5820AF24XG": hpA5820AF24XG,
       "hp6125GXG": hp6125GXG,
       "hpA31008SI": hpA31008SI,
       "hpA310016SI": hpA310016SI,
       "hpA310024SI": hpA310024SI,
       "hpA31008EI": hpA31008EI,
       "hpA310016EI": hpA310016EI,
       "hpA310024EI": hpA310024EI,
       "hpA31008POEEI": hpA31008POEEI,
       "hpA310016POEEI": hpA310016POEEI,
       "hpA310024POEEI": hpA310024POEEI,
       "hpA580024GTAA": hpA580024GTAA,
       "hpA580024GPoEPlusTAA": hpA580024GPoEPlusTAA,
       "hpA580024GSFPTAA": hpA580024GSFPTAA,
       "hpA580048GTAA": hpA580048GTAA,
       "hpA580048GPoEPlusTAA2SLOT": hpA580048GPoEPlusTAA2SLOT,
       "hpA580048GPoEPlusTAA": hpA580048GPoEPlusTAA,
       "hpA5820X14XGSFPPlusTAA2SLOT": hpA5820X14XGSFPPlusTAA2SLOT,
       "hpA5820X24XGSFPPlusTAA": hpA5820X24XGSFPPlusTAA,
       "hpA512024GEITAA2SLOT": hpA512024GEITAA2SLOT,
       "hpA512048GEITAA2SLOT": hpA512048GEITAA2SLOT,
       "hpA512024GPoEPlusEITAA2SLOT": hpA512024GPoEPlusEITAA2SLOT,
       "hpA512048GPoEPlusEITAA2SLOT": hpA512048GPoEPlusEITAA2SLOT,
       "hpA550024GSFPEITAA2SLOT": hpA550024GSFPEITAA2SLOT,
       "hpA550024GEITAA2SLOT": hpA550024GEITAA2SLOT,
       "hpA550048GEITAA2SLOT": hpA550048GEITAA2SLOT,
       "hpA550024GPoEPlusEITAA2SLOT": hpA550024GPoEPlusEITAA2SLOT,
       "hpA550048GPoEPlusEITAA2SLOT": hpA550048GPoEPlusEITAA2SLOT,
       "hp5920AF24XG": hp5920AF24XG,
       "hpA5830AF48G": hpA5830AF48G,
       "hpA5830AF96G": hpA5830AF96G,
       "hpV191016G": hpV191016G,
       "hpV191024G": hpV191024G,
       "hpV191024GPoE365W": hpV191024GPoE365W,
       "hpV191024GPoE170W": hpV191024GPoE170W,
       "hpV191048G": hpV191048G,
       "hp10504": hp10504,
       "hp10508": hp10508,
       "hp10508V": hp10508V,
       "hp10512": hp10512,
       "hpA360024V2EI": hpA360024V2EI,
       "hpA360048V2EI": hpA360048V2EI,
       "hpA360024PoEPlusV2EI": hpA360024PoEPlusV2EI,
       "hpA360048PoEPlusV2EI": hpA360048PoEPlusV2EI,
       "hpA360024SFPV2EI": hpA360024SFPV2EI,
       "hpA360024V2SI": hpA360024V2SI,
       "hpA360048V2SI": hpA360048V2SI,
       "hpA360024PoEPlusV2SI": hpA360024PoEPlusV2SI,
       "hpA360048PoEPlusV2SI": hpA360048PoEPlusV2SI,
       "hpA310048V2": hpA310048V2,
       "hp5900AF48XG4QSFPPlus": hp5900AF48XG4QSFPPlus,
       "hpA550024G4SFPHI": hpA550024G4SFPHI,
       "hpA550048G4SFPHI": hpA550048G4SFPHI,
       "hp6125G": hp6125G,
       "hpA51208GSI": hpA51208GSI,
       "hpA51208GPoEPlusSI": hpA51208GPoEPlusSI,
       "hpA51208GPPoEPlusSI": hpA51208GPPoEPlusSI,
       "hpA5120AF48GHI": hpA5120AF48GHI,
       "hp12504DC": hp12504DC,
       "hp12508DC": hp12508DC,
       "hp12518DC": hp12518DC,
       "hp12508AC": hp12508AC,
       "hp12518AC": hp12518AC,
       "hp5900AF48XGT4QSFPPlus": hp5900AF48XGT4QSFPPlus,
       "hp19108G": hp19108G,
       "hp19108GPoEPlus65W": hp19108GPoEPlus65W,
       "hp19108GPoEPlus180W": hp19108GPoEPlus180W,
       "hp5830AF48GTAA": hp5830AF48GTAA,
       "hp5830AF96GTAA": hp5830AF96GTAA,
       "hp7508H": hp7508H,
       "hp5900AF48G4XG2QSFPPlus": hp5900AF48G4XG2QSFPPlus,
       "hp550048GPoEPlus4SFPHI": hp550048GPoEPlus4SFPHI,
       "hp550024GPoEPlus4SFPHI": hp550024GPoEPlus4SFPHI,
       "hp550024GSFPHI": hp550024GSFPHI,
       "hp12504ACV7": hp12504ACV7,
       "hp12504DCV7": hp12504DCV7,
       "hp12508ACV7": hp12508ACV7,
       "hp12508DCV7": hp12508DCV7,
       "hp12518ACV7": hp12518ACV7,
       "hp12518DCV7": hp12518DCV7,
       "hp5900AF48XG4QSFPPlusTAA": hp5900AF48XG4QSFPPlusTAA,
       "hp5920AF24XGTAA": hp5920AF24XGTAA,
       "hpV19108": hpV19108,
       "hpV19108PoEPlus": hpV19108PoEPlus,
       "hpV191024": hpV191024,
       "hpV191024PoEPlus": hpV191024PoEPlus,
       "hpV191048": hpV191048,
       "hp6125XGXLG": hp6125XGXLG,
       "hp11908V": hp11908V,
       "hp550048GPoEPlus4SFPHITAA2Slot": hp550048GPoEPlus4SFPHITAA2Slot,
       "hp550024GPoEPlus4SFPHITAA2Slot": hp550024GPoEPlus4SFPHITAA2Slot,
       "hp550024GSFPHITAA2Slot": hp550024GSFPHITAA2Slot,
       "hpMoonshot45XGc": hpMoonshot45XGc,
       "hp12910AC": hp12910AC,
       "hpFF593032QSFPPlus": hpFF593032QSFPPlus,
       "hpFF593032QSFPPlusTAA": hpFF593032QSFPPlusTAA,
       "hpFF7904": hpFF7904,
       "hp12916AC": hp12916AC,
       "hp12916DC": hp12916DC,
       "hpFF5900CP48XG4QSFPPlus": hpFF5900CP48XG4QSFPPlus,
       "hp5900CP48XG4QSFPPlus8GbFCBF": hp5900CP48XG4QSFPPlus8GbFCBF,
       "hp6125XLGTAA": hp6125XLGTAA,
       "hp6125GXGTAA": hp6125GXGTAA,
       "hp6125GTAA": hp6125GTAA,
       "hp512024G4SFPXI2Slot": hp512024G4SFPXI2Slot,
       "hp512048G4SFPXI2Slot": hp512048G4SFPXI2Slot,
       "hp512024GPoEPlus4SFPXI2Slot": hp512024GPoEPlus4SFPXI2Slot,
       "hp512048GPoEPlus4SFPXI2Slot": hp512048GPoEPlus4SFPXI2Slot,
       "hp512024G4SFPXITAA2Slot": hp512024G4SFPXITAA2Slot,
       "hp512048G4SFPXITAA2Slot": hp512048G4SFPXITAA2Slot,
       "hp512024GPoEPlus4SFPXITAA2Slot": hp512024GPoEPlus4SFPXITAA2Slot,
       "hp512048GPoEPlus4SFPXITAA2Slot": hp512048GPoEPlus4SFPXITAA2Slot,
       "hp19208G": hp19208G,
       "hp19208GPoEPlus65W": hp19208GPoEPlus65W,
       "hp19208GPoEPlus180W": hp19208GPoEPlus180W,
       "hp192016G": hp192016G,
       "hp192024G": hp192024G,
       "hp192024GPoEPlus180W": hp192024GPoEPlus180W,
       "hp192024GPoEPlus370W": hp192024GPoEPlus370W,
       "hp192048G": hp192048G,
       "hp192048GPoEPlus370W": hp192048GPoEPlus370W,
       "hpFF570040XG2QSFPPlusTAA": hpFF570040XG2QSFPPlusTAA,
       "hpFF570040XG2QSFPPlus": hpFF570040XG2QSFPPlus,
       "hpFF570032XGT8XG2QSFPPlusTAA": hpFF570032XGT8XG2QSFPPlusTAA,
       "hpFF570032XGT8XG2QSFPPlus": hpFF570032XGT8XG2QSFPPlus,
       "hpFF570048G4XG2QSFPPlusTAA": hpFF570048G4XG2QSFPPlusTAA,
       "hpFF570048G4XG2QSFPPlus": hpFF570048G4XG2QSFPPlus,
       "hp16208G": hp16208G,
       "hp162024G": hp162024G,
       "hp162048G": hp162048G,
       "hp195024G2SFPPlus2XGT": hp195024G2SFPPlus2XGT,
       "hp195048G2SFPPlus2XGT": hp195048G2SFPPlus2XGT,
       "hp195024G2SFPPlus2XGTPoEPlus": hp195024G2SFPPlus2XGTPoEPlus,
       "hp195048G2SFPPlus2XGTPoEPlus": hp195048G2SFPPlus2XGTPoEPlus,
       "hp513024G4SFPPlusEI": hp513024G4SFPPlusEI,
       "hp513024GSFP4SFPPlusEI": hp513024GSFP4SFPPlusEI,
       "hp513048G4SFPPlusEI": hp513048G4SFPPlusEI,
       "hp513024GPoEPlus4SFPPlus180WEI": hp513024GPoEPlus4SFPPlus180WEI,
       "hp513024GPoEPlus4SFPPlus370WEI": hp513024GPoEPlus4SFPPlus370WEI,
       "hp513048GPoEPlus4SFPPlus370WEI": hp513048GPoEPlus4SFPPlus370WEI,
       "hp513024G2SFPPlus2XGTEI": hp513024G2SFPPlus2XGTEI,
       "hp513048G2SFPPlus2XGTEI": hp513048G2SFPPlus2XGTEI,
       "hp513024GPoEPlus2SFPPlus2XGT370WEI": hp513024GPoEPlus2SFPPlus2XGT370WEI,
       "hp513048GPoEPlus2SFPPlus2XGT370WEI": hp513048GPoEPlus2SFPPlus2XGT370WEI,
       "hp513024G4SFPPlusEITAA": hp513024G4SFPPlusEITAA,
       "hp513024GSFP4SFPPlusEITAA": hp513024GSFP4SFPPlusEITAA,
       "hp513048G4SFPPlusEITAA": hp513048G4SFPPlusEITAA,
       "hp513024GPoEPlus4SFPPlus180WEITAA": hp513024GPoEPlus4SFPPlus180WEITAA,
       "hp513024GPoEPlus4SFPPlus370WEITAA": hp513024GPoEPlus4SFPPlus370WEITAA,
       "hp513048GPoEPlus4SFPPlus370WEITAA": hp513048GPoEPlus4SFPPlus370WEITAA,
       "hp513024G2SFPPlus2XGTEITAA": hp513024G2SFPPlus2XGTEITAA,
       "hp513048G2SFPPlus2XGTEITAA": hp513048G2SFPPlus2XGTEITAA,
       "hp513024GPoEPlus2SFPPlus2XGT370WEITAA": hp513024GPoEPlus2SFPPlus2XGT370WEITAA,
       "hp513048GPoEPlus2SFPPlus2XGT370WEITAA": hp513048GPoEPlus2SFPPlus2XGT370WEITAA,
       "hpFF7910": hpFF7910,
       "hp5900AF48G4XG2QSFPPlusTAA": hp5900AF48G4XG2QSFPPlusTAA,
       "hp5900AF48XGT4QSFPPlusTAA": hp5900AF48XGT4QSFPPlusTAA,
       "hpFF5900CP48XG4QSFPPlusTAA": hpFF5900CP48XG4QSFPPlusTAA,
       "hp513024G4SFPPlusEIBrazil": hp513024G4SFPPlusEIBrazil,
       "hp513048G4SFPPlusEIBrazil": hp513048G4SFPPlusEIBrazil,
       "hp513024GPoEPlus4SFPPlus370WEIBrazil": hp513024GPoEPlus4SFPPlus370WEIBrazil,
       "hp513048GPoEPlus4SFPPlus370WEIBrazil": hp513048GPoEPlus4SFPPlus370WEIBrazil,
       "hpThunderBird": hpThunderBird,
       "hpFF12916E": hpFF12916E,
       "hpNJ50005GPoEPlusWalljack": hpNJ50005GPoEPlusWalljack,
       "hp551024G4SFPPlusHI1Slot": hp551024G4SFPPlusHI1Slot,
       "hp551048G4SFPPlusHI1Slot": hp551048G4SFPPlusHI1Slot,
       "hp551024GPoEPlus4SFPPlusHI1Slot": hp551024GPoEPlus4SFPPlusHI1Slot,
       "hp551048GPoEPlus4SFPPlusHI1Slot": hp551048GPoEPlus4SFPPlusHI1Slot,
       "hp551024GSFP4SFPPlusHI1Slot": hp551024GSFP4SFPPlusHI1Slot,
       "hp551024G4SFPPlusHITAA1Slot": hp551024G4SFPPlusHITAA1Slot,
       "hp551048G4SFPPlusHITAA1Slot": hp551048G4SFPPlusHITAA1Slot,
       "hp551024GPoEPlus4SFPPlusHITAA1Slot": hp551024GPoEPlus4SFPPlusHITAA1Slot,
       "hp551048GPoEPlus4SFPPlusHITAA1Slot": hp551048GPoEPlus4SFPPlusHITAA1Slot,
       "hp551024GSFP4SFPPlusHITAA1Slot": hp551024GSFP4SFPPlusHITAA1Slot,
       "hpFF12910ACTAA": hpFF12910ACTAA,
       "hpFF7904TAA": hpFF7904TAA,
       "hpFF7910TAA": hpFF7910TAA,
       "hp6127XLG": hp6127XLG,
       "hpFF59302Slot2QSFPPlus": hpFF59302Slot2QSFPPlus,
       "hpFF59302Slot2QSFPPlusTAA": hpFF59302Slot2QSFPPlusTAA,
       "hpFF59304Slot": hpFF59304Slot,
       "hpFF59304SlotTAA": hpFF59304SlotTAA,
       "hp6127XLGTAA": hp6127XLGTAA,
       "hp195012XGT4SFPPlus": hp195012XGT4SFPPlus,
       "hpFF12916ETAA": hpFF12916ETAA,
       "hpFF12908E": hpFF12908E,
       "hpFF12908ETAA": hpFF12908ETAA,
       "hpMoonshot45GcR10": hpMoonshot45GcR10,
       "hpMoonshot45XGcR16": hpMoonshot45XGcR16,
       "hpMoonshot180XGcR16": hpMoonshot180XGcR16,
       "hpMoonshot180XGcR40": hpMoonshot180XGcR40,
       "hpRouter": hpRouter,
       "hpAMSR900": hpAMSR900,
       "hpAMSR920": hpAMSR920,
       "hpAMSR2010": hpAMSR2010,
       "hpAMSR2011": hpAMSR2011,
       "hpAMSR2012": hpAMSR2012,
       "hpAMSR2012T": hpAMSR2012T,
       "hpAMSR2013": hpAMSR2013,
       "hpAMSR2020": hpAMSR2020,
       "hpAMSR2021": hpAMSR2021,
       "hpAMSR2040": hpAMSR2040,
       "hpAMSR3010": hpAMSR3010,
       "hpAMSR3011E": hpAMSR3011E,
       "hpAMSR3011F": hpAMSR3011F,
       "hpAMSR3016": hpAMSR3016,
       "hpAMSR3020": hpAMSR3020,
       "hpAMSR3040": hpAMSR3040,
       "hpAMSR3060": hpAMSR3060,
       "hpAMSR5040": hpAMSR5040,
       "hpAMSR5060": hpAMSR5060,
       "hpA6602": hpA6602,
       "hpA6604": hpA6604,
       "hpA6608": hpA6608,
       "hpA6616": hpA6616,
       "hpAMSR900W": hpAMSR900W,
       "hpAMSR900WNA": hpAMSR900WNA,
       "hpAMSR920W": hpAMSR920W,
       "hpAMSR920WNA": hpAMSR920WNA,
       "hpAMSR2012W": hpAMSR2012W,
       "hpAMSR2012TW": hpAMSR2012TW,
       "hpAMSR2012TWNA": hpAMSR2012TWNA,
       "hpAMSR2013W": hpAMSR2013W,
       "hpAMSR2013WNA": hpAMSR2013WNA,
       "hpAMSR2020S": hpAMSR2020S,
       "hpAMSR2021S": hpAMSR2021S,
       "hpAMSR2040S": hpAMSR2040S,
       "hpAMSR3010DC": hpAMSR3010DC,
       "hpAMSR3016POE": hpAMSR3016POE,
       "hpAMSR3020AS": hpAMSR3020AS,
       "hpAMSR3020POE": hpAMSR3020POE,
       "hpAMSR3020DC": hpAMSR3020DC,
       "hpAMSR3040AS": hpAMSR3040AS,
       "hpAMSR3040POE": hpAMSR3040POE,
       "hpAMSR3040DC": hpAMSR3040DC,
       "hpAMSR3060AS": hpAMSR3060AS,
       "hpAMSR3060POE": hpAMSR3060POE,
       "hpAMSR3060DC": hpAMSR3060DC,
       "hpAMSR5040DC": hpAMSR5040DC,
       "hpAMSR5060DC": hpAMSR5060DC,
       "hpA8805": hpA8805,
       "hpA8808": hpA8808,
       "hpA8812": hpA8812,
       "hpAOAPFICV2": hpAOAPFICV2,
       "hpAOAPMIMV2": hpAOAPMIMV2,
       "hpAOAPSMIMV2": hpAOAPSMIMV2,
       "hpMSR2003AC": hpMSR2003AC,
       "hpMSR3012AC": hpMSR3012AC,
       "hpMSR3012DC": hpMSR3012DC,
       "hpMSR3024AC": hpMSR3024AC,
       "hpMSR3024DC": hpMSR3024DC,
       "hpMSR3024POE": hpMSR3024POE,
       "hpMSR3044": hpMSR3044,
       "hpMSR3064": hpMSR3064,
       "hpMSR4060": hpMSR4060,
       "hpMSR4080": hpMSR4080,
       "hpHSR6602G": hpHSR6602G,
       "hpHSR6602XG": hpHSR6602XG,
       "hpHSR6802": hpHSR6802,
       "hpHSR6804": hpHSR6804,
       "hpHSR6808": hpHSR6808,
       "hpMSR930": hpMSR930,
       "hpMSR930G": hpMSR930G,
       "hpMSR931": hpMSR931,
       "hpMSR931G": hpMSR931G,
       "hpMSR931GG": hpMSR931GG,
       "hpMSR930W": hpMSR930W,
       "hpMSR9304GLTEV": hpMSR9304GLTEV,
       "hpMSR933": hpMSR933,
       "hpMSR933G": hpMSR933G,
       "hpMSR935": hpMSR935,
       "hpMSR935W": hpMSR935W,
       "hpMSR935G": hpMSR935G,
       "hpMSR936W": hpMSR936W,
       "hpMSR9304GLTEG": hpMSR9304GLTEG,
       "hpMSR930LE": hpMSR930LE,
       "hpMSR930GLE": hpMSR930GLE,
       "hpMSR931LE": hpMSR931LE,
       "hpMSR931GLE": hpMSR931GLE,
       "hpMSR931DGLE": hpMSR931DGLE,
       "hpMSR930WLE": hpMSR930WLE,
       "hpMSR9304GLTEA": hpMSR9304GLTEA,
       "hpMSR933GLE": hpMSR933GLE,
       "hpMSR935LE": hpMSR935LE,
       "hpMSR935WLE": hpMSR935WLE,
       "hpMSR935GLE": hpMSR935GLE,
       "hpMSR9304GLTEGLE": hpMSR9304GLTEGLE,
       "hpVSR": hpVSR,
       "hpVSR1001": hpVSR1001,
       "hpVSR1004": hpVSR1004,
       "hpVSR1008": hpVSR1008,
       "hpMSR10038": hpMSR10038,
       "hpMSR100414": hpMSR100414,
       "hpVSR1000": hpVSR1000,
       "hpMSR200424": hpMSR200424,
       "hpMSR200448": hpMSR200448,
       "hpHSR6602GTAA": hpHSR6602GTAA,
       "hpHSR6602XGTAA": hpHSR6602XGTAA,
       "hpMSR10024": hpMSR10024,
       "hpNSC1000": hpNSC1000,
       "hpMSR930WNA": hpMSR930WNA,
       "hpMSR935WNA": hpMSR935WNA,
       "hpMSR2003TAA": hpMSR2003TAA,
       "hpMSR3024TAA": hpMSR3024TAA,
       "hpMSR3044TAA": hpMSR3044TAA,
       "hpMSR935TI": hpMSR935TI,
       "hpMSR933TI": hpMSR933TI,
       "hpMSR931TI": hpMSR931TI,
       "hpMSR10038S": hpMSR10038S,
       "hpMSR932": hpMSR932,
       "hpMSR932W": hpMSR932W,
       "hpMSR932WNA": hpMSR932WNA,
       "hpMSR9328": hpMSR9328,
       "hpMSR9328W": hpMSR9328W,
       "hpMSR9328WNA": hpMSR9328WNA,
       "hpVBRAS1000": hpVBRAS1000,
       "hpHSR6802E": hpHSR6802E,
       "hpHSR6804E": hpHSR6804E,
       "hpHSR6808E": hpHSR6808E,
       "hpMSR93204GLTEGV2": hpMSR93204GLTEGV2,
       "hpMSR93204GLTEAVS": hpMSR93204GLTEAVS,
       "hpMSR954": hpMSR954,
       "hpMSR954W": hpMSR954W,
       "hpMSR954WLTEAM": hpMSR954WLTEAM,
       "hpMSR954WLTE": hpMSR954WLTE,
       "hpMSR958": hpMSR958,
       "hpMSR958POE": hpMSR958POE,
       "hpWireless": hpWireless,
       "hpAWA2610EAGNFAT": hpAWA2610EAGNFAT,
       "hpAWA2620EAGNFAT": hpAWA2620EAGNFAT,
       "hpAWA2620AGNFAT": hpAWA2620AGNFAT,
       "hpA7500LSQM3WCMB0": hpA7500LSQM3WCMB0,
       "hpA9500LSRM2WCM2A1": hpA9500LSRM2WCM2A1,
       "hpA5800LSWM2WCM10": hpA5800LSWM2WCM10,
       "hpA5800LSWM2WCM20": hpA5800LSWM2WCM20,
       "hpAWX5004EWPXZ65004": hpAWX5004EWPXZ65004,
       "hpAWX5002EWPXZ75002": hpAWX5002EWPXZ75002,
       "hpA3000E": hpA3000E,
       "hpA3000ELSW": hpA3000ELSW,
       "hpAWA3620AGN": hpAWA3620AGN,
       "hpAWA3622AGN": hpAWA3622AGN,
       "hpAWA3610GN": hpAWA3610GN,
       "hpAWA2620XAGN": hpAWA2620XAGN,
       "hpLSU3WCMD0": hpLSU3WCMD0,
       "hpWX3024EWCM": hpWX3024EWCM,
       "hpWX3024ELSW": hpWX3024ELSW,
       "hpWX3010EWCM": hpWX3010EWCM,
       "hpWX3010ELSW": hpWX3010ELSW,
       "hpLSU3WCMD0TAA": hpLSU3WCMD0TAA,
       "hpWX3024ETAAWCM": hpWX3024ETAAWCM,
       "hpWX3024ETAALSW": hpWX3024ETAALSW,
       "hpWX3010ETAAWCM": hpWX3010ETAAWCM,
       "hpWX3010ETAALSW": hpWX3010ETAALSW,
       "hpSecurity": hpSecurity,
       "hpSecBladeIMFWII": hpSecBladeIMFWII,
       "hpSecBladeIMSSL": hpSecBladeIMSSL,
       "hpSecBladeIMLB": hpSecBladeIMLB,
       "hpSecBladeLSQ1FWBSC0": hpSecBladeLSQ1FWBSC0,
       "hpSecBladeLSQM1LBC0": hpSecBladeLSQM1LBC0,
       "hpSecBladeLSQ1NSMSC0": hpSecBladeLSQ1NSMSC0,
       "hpSecBladeLSR1FW2A1": hpSecBladeLSR1FW2A1,
       "hpSecBladeLSR1LB1A1": hpSecBladeLSR1LB1A1,
       "hpSecBladeLSR1NSM1A1": hpSecBladeLSR1NSM1A1,
       "hpSecBladeLST1FW2A1": hpSecBladeLST1FW2A1,
       "hpSecBladeLST1LB1A1": hpSecBladeLST1LB1A1,
       "hpSecBladeLST1NSM1A1": hpSecBladeLST1NSM1A1,
       "hpSecBladeLSWM1FW10": hpSecBladeLSWM1FW10,
       "hpSecBladeSPEFWM200": hpSecBladeSPEFWM200,
       "hpAF5000": hpAF5000,
       "hpAF1000E": hpAF1000E,
       "hpAU200S": hpAU200S,
       "hpAU200A": hpAU200A,
       "hpAF1000SEI": hpAF1000SEI,
       "hpAF1000AEI": hpAF1000AEI,
       "hpSecBladeLST1FW3A1": hpSecBladeLST1FW3A1,
       "hpSecBladeLSU1FWCEA0": hpSecBladeLSU1FWCEA0,
       "hpF5000C": hpF5000C,
       "hpF5000S": hpF5000S,
       "hpVFW1000": hpVFW1000,
       "hpSecBladeLSX1FWCEA1": hpSecBladeLSX1FWCEA1,
       "hpVMSGVLB1000": hpVMSGVLB1000,
       "hpSecBlade3Context": hpSecBlade3Context}
)
