# SNMP MIB module (DASAN-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-PRODUCTS-MIB

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

(dasanModules,
 dasanProducts) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasanModules",
    "dasanProducts")

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

dasanProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 12, 2)
)
if mibBuilder.loadTexts:
    dasanProductsMIB.setRevisions(
        ("1901-04-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DasanRouter_ObjectIdentity = ObjectIdentity
dasanRouter = _DasanRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1)
)
_V1500_ObjectIdentity = ObjectIdentity
v1500 = _V1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 1)
)
_V1501_ObjectIdentity = ObjectIdentity
v1501 = _V1501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 1, 1)
)
_V1502T_ObjectIdentity = ObjectIdentity
v1502T = _V1502T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 1, 2)
)
_V2500_ObjectIdentity = ObjectIdentity
v2500 = _V2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 2)
)
_V2501_ObjectIdentity = ObjectIdentity
v2501 = _V2501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 2, 1)
)
_V2501T_ObjectIdentity = ObjectIdentity
v2501T = _V2501T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 2, 2)
)
_V2502T_ObjectIdentity = ObjectIdentity
v2502T = _V2502T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 2, 3)
)
_V2503_ObjectIdentity = ObjectIdentity
v2503 = _V2503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 2, 4)
)
_V2600_ObjectIdentity = ObjectIdentity
v2600 = _V2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 3)
)
_V2602T_ObjectIdentity = ObjectIdentity
v2602T = _V2602T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 3, 1)
)
_V2602D_ObjectIdentity = ObjectIdentity
v2602D = _V2602D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 3, 2)
)
_V2608T_ObjectIdentity = ObjectIdentity
v2608T = _V2608T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 3, 3)
)
_V2602A_ObjectIdentity = ObjectIdentity
v2602A = _V2602A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 3, 4)
)
_V3100_ObjectIdentity = ObjectIdentity
v3100 = _V3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 4)
)
_V3104_ObjectIdentity = ObjectIdentity
v3104 = _V3104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 4, 1)
)
_V3108_ObjectIdentity = ObjectIdentity
v3108 = _V3108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 4, 2)
)
_V3112_ObjectIdentity = ObjectIdentity
v3112 = _V3112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 4, 3)
)
_V3300_ObjectIdentity = ObjectIdentity
v3300 = _V3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 5)
)
_V3302_ObjectIdentity = ObjectIdentity
v3302 = _V3302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 1, 5, 1)
)
_DasanSwitch_ObjectIdentity = ObjectIdentity
dasanSwitch = _DasanSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2)
)
_V5100_ObjectIdentity = ObjectIdentity
v5100 = _V5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1)
)
_V5124_ObjectIdentity = ObjectIdentity
v5124 = _V5124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 1)
)
_V5108F_ObjectIdentity = ObjectIdentity
v5108F = _V5108F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 2)
)
_V5116F_ObjectIdentity = ObjectIdentity
v5116F = _V5116F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 3)
)
_V5124F_ObjectIdentity = ObjectIdentity
v5124F = _V5124F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 4)
)
_V1724_ObjectIdentity = ObjectIdentity
v1724 = _V1724_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 5)
)
_V1708F_ObjectIdentity = ObjectIdentity
v1708F = _V1708F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 6)
)
_V5224_ObjectIdentity = ObjectIdentity
v5224 = _V5224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 7)
)
_V5216F_ObjectIdentity = ObjectIdentity
v5216F = _V5216F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 8)
)
_V5324_ObjectIdentity = ObjectIdentity
v5324 = _V5324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 9)
)
_V5124E_ObjectIdentity = ObjectIdentity
v5124E = _V5124E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 10)
)
_V1708_ObjectIdentity = ObjectIdentity
v1708 = _V1708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 11)
)
_V1716_ObjectIdentity = ObjectIdentity
v1716 = _V1716_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 12)
)
_V1724plus_ObjectIdentity = ObjectIdentity
v1724plus = _V1724plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 13)
)
_V1624_ObjectIdentity = ObjectIdentity
v1624 = _V1624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 14)
)
_V1616_ObjectIdentity = ObjectIdentity
v1616 = _V1616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 15)
)
_V1608_ObjectIdentity = ObjectIdentity
v1608 = _V1608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 16)
)
_V5216_ObjectIdentity = ObjectIdentity
v5216 = _V5216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 17)
)
_V1624MD_ObjectIdentity = ObjectIdentity
v1624MD = _V1624MD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 18)
)
_V1624CWDM_ObjectIdentity = ObjectIdentity
v1624CWDM = _V1624CWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 19)
)
_V2624_ObjectIdentity = ObjectIdentity
v2624 = _V2624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 20)
)
_V2616_ObjectIdentity = ObjectIdentity
v2616 = _V2616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 21)
)
_V2608_ObjectIdentity = ObjectIdentity
v2608 = _V2608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 1, 22)
)
_V1100_ObjectIdentity = ObjectIdentity
v1100 = _V1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 2)
)
_V1124_ObjectIdentity = ObjectIdentity
v1124 = _V1124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 2, 1)
)
_V1108F_ObjectIdentity = ObjectIdentity
v1108F = _V1108F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 2, 2)
)
_V1224_ObjectIdentity = ObjectIdentity
v1224 = _V1224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 2, 3)
)
_V1124C_ObjectIdentity = ObjectIdentity
v1124C = _V1124C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 2, 4)
)
_V1324_ObjectIdentity = ObjectIdentity
v1324 = _V1324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 2, 5)
)
_V1424G_ObjectIdentity = ObjectIdentity
v1424G = _V1424G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 2, 6)
)
_V1916GR_ObjectIdentity = ObjectIdentity
v1916GR = _V1916GR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 2, 7)
)
_V6100_ObjectIdentity = ObjectIdentity
v6100 = _V6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 3)
)
_V6124_ObjectIdentity = ObjectIdentity
v6124 = _V6124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 3, 1)
)
_V6108_ObjectIdentity = ObjectIdentity
v6108 = _V6108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 3, 2)
)
_V6124F_ObjectIdentity = ObjectIdentity
v6124F = _V6124F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 3, 3)
)
_V6108F_ObjectIdentity = ObjectIdentity
v6108F = _V6108F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 3, 4)
)
_V6216G_ObjectIdentity = ObjectIdentity
v6216G = _V6216G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 3, 5)
)
_V6116G_ObjectIdentity = ObjectIdentity
v6116G = _V6116G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 3, 6)
)
_V6224_ObjectIdentity = ObjectIdentity
v6224 = _V6224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 3, 7)
)
_V6108G_ObjectIdentity = ObjectIdentity
v6108G = _V6108G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 3, 8)
)
_V8000_ObjectIdentity = ObjectIdentity
v8000 = _V8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4)
)
_V8240_ObjectIdentity = ObjectIdentity
v8240 = _V8240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 1)
)
_V8272_ObjectIdentity = ObjectIdentity
v8272 = _V8272_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 2)
)
_V8500_ObjectIdentity = ObjectIdentity
v8500 = _V8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 3)
)
_V8300_ObjectIdentity = ObjectIdentity
v8300 = _V8300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 4)
)
_V8102_ObjectIdentity = ObjectIdentity
v8102 = _V8102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 5)
)
_V8400_ObjectIdentity = ObjectIdentity
v8400 = _V8400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 6)
)
_V8106_ObjectIdentity = ObjectIdentity
v8106 = _V8106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 7)
)
_V8600_ObjectIdentity = ObjectIdentity
v8600 = _V8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8)
)
_V8605_ObjectIdentity = ObjectIdentity
v8605 = _V8605_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 1)
)
_V8607_ObjectIdentity = ObjectIdentity
v8607 = _V8607_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 2)
)
_V8610_ObjectIdentity = ObjectIdentity
v8610 = _V8610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 3)
)
_V8600_IU_ObjectIdentity = ObjectIdentity
v8600_IU = _V8600_IU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101)
)
_V8600_CU_ObjectIdentity = ObjectIdentity
v8600_CU = _V8600_CU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 1)
)
_V8600_IU_GE24_GT8_ObjectIdentity = ObjectIdentity
v8600_IU_GE24_GT8 = _V8600_IU_GE24_GT8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 2)
)
_V8600_IU_GT24_GE8_ObjectIdentity = ObjectIdentity
v8600_IU_GT24_GE8 = _V8600_IU_GT24_GE8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 3)
)
_V8600_IU_GE44_10GE4_ObjectIdentity = ObjectIdentity
v8600_IU_GE44_10GE4 = _V8600_IU_GE44_10GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 4)
)
_V8600_IU_GT48_ObjectIdentity = ObjectIdentity
v8600_IU_GT48 = _V8600_IU_GT48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 5)
)
_V8600_IU_GT24_GE20_10GE4_ObjectIdentity = ObjectIdentity
v8600_IU_GT24_GE20_10GE4 = _V8600_IU_GT24_GE20_10GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 6)
)
_V8600_IU_10GE8_ObjectIdentity = ObjectIdentity
v8600_IU_10GE8 = _V8600_IU_10GE8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 7)
)
_V8600_IU_GT48P_ObjectIdentity = ObjectIdentity
v8600_IU_GT48P = _V8600_IU_GT48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 8)
)
_V8600_IU_10GE8F_ObjectIdentity = ObjectIdentity
v8600_IU_10GE8F = _V8600_IU_10GE8F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 9)
)
_V8600_IU_GE44_10GE4F_ObjectIdentity = ObjectIdentity
v8600_IU_GE44_10GE4F = _V8600_IU_GE44_10GE4F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 10)
)
_V8600_IU_GT48F_ObjectIdentity = ObjectIdentity
v8600_IU_GT48F = _V8600_IU_GT48F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 11)
)
_V8600_IU_10GE48_ObjectIdentity = ObjectIdentity
v8600_IU_10GE48 = _V8600_IU_10GE48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 12)
)
_V8600_IU_40GE12_ObjectIdentity = ObjectIdentity
v8600_IU_40GE12 = _V8600_IU_40GE12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 13)
)
_V8600_IU_10GE24_40GE4_ObjectIdentity = ObjectIdentity
v8600_IU_10GE24_40GE4 = _V8600_IU_10GE24_40GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 14)
)
_Ds_PA600I_ObjectIdentity = ObjectIdentity
ds_PA600I = _Ds_PA600I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 15)
)
_Ds_PD600I_ObjectIdentity = ObjectIdentity
ds_PD600I = _Ds_PD600I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 16)
)
_Ds_PA1600I_ObjectIdentity = ObjectIdentity
ds_PA1600I = _Ds_PA1600I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 17)
)
_Ds_PD1600I_ObjectIdentity = ObjectIdentity
ds_PD1600I = _Ds_PD1600I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 18)
)
_Ds_PA1600I_PL_ObjectIdentity = ObjectIdentity
ds_PA1600I_PL = _Ds_PA1600I_PL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 19)
)
_Ds_PA3000I_PL_ObjectIdentity = ObjectIdentity
ds_PA3000I_PL = _Ds_PA3000I_PL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 4, 8, 101, 20)
)
_V5200_ObjectIdentity = ObjectIdentity
v5200 = _V5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5)
)
_V5208G_ObjectIdentity = ObjectIdentity
v5208G = _V5208G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 1)
)
_V5212G_ObjectIdentity = ObjectIdentity
v5212G = _V5212G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 2)
)
_V5424G_ObjectIdentity = ObjectIdentity
v5424G = _V5424G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 3)
)
_V5224G_ObjectIdentity = ObjectIdentity
v5224G = _V5224G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 4)
)
_V5324G_ObjectIdentity = ObjectIdentity
v5324G = _V5324G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 5)
)
_V5524G_ObjectIdentity = ObjectIdentity
v5524G = _V5524G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 6)
)
_V5548G_ObjectIdentity = ObjectIdentity
v5548G = _V5548G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 7)
)
_V5524XG_ObjectIdentity = ObjectIdentity
v5524XG = _V5524XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 9)
)
_V5848G_ObjectIdentity = ObjectIdentity
v5848G = _V5848G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 10)
)
_V5504XG_ObjectIdentity = ObjectIdentity
v5504XG = _V5504XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 11)
)
_V5812G_ObjectIdentity = ObjectIdentity
v5812G = _V5812G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 12)
)
_V5524GS_ObjectIdentity = ObjectIdentity
v5524GS = _V5524GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 13)
)
_V5806_ObjectIdentity = ObjectIdentity
v5806 = _V5806_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 14)
)
_Gpm4_2G_ObjectIdentity = ObjectIdentity
gpm4_2G = _Gpm4_2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 15)
)
_V5824G_ObjectIdentity = ObjectIdentity
v5824G = _V5824G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 16)
)
_V5648G_ObjectIdentity = ObjectIdentity
v5648G = _V5648G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 17)
)
_V5836G_ObjectIdentity = ObjectIdentity
v5836G = _V5836G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 5, 18)
)
_V2100_ObjectIdentity = ObjectIdentity
v2100 = _V2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6)
)
_V2108_ObjectIdentity = ObjectIdentity
v2108 = _V2108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 1)
)
_V2116_ObjectIdentity = ObjectIdentity
v2116 = _V2116_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 2)
)
_V2124_ObjectIdentity = ObjectIdentity
v2124 = _V2124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 3)
)
_V2308_ObjectIdentity = ObjectIdentity
v2308 = _V2308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 4)
)
_V2316_ObjectIdentity = ObjectIdentity
v2316 = _V2316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 5)
)
_V2324_ObjectIdentity = ObjectIdentity
v2324 = _V2324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 6)
)
_V2116J_ObjectIdentity = ObjectIdentity
v2116J = _V2116J_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 7)
)
_V2124J_ObjectIdentity = ObjectIdentity
v2124J = _V2124J_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 8)
)
_V2424POE_ObjectIdentity = ObjectIdentity
v2424POE = _V2424POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 9)
)
_V2324G_ObjectIdentity = ObjectIdentity
v2324G = _V2324G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 10)
)
_V2348G_ObjectIdentity = ObjectIdentity
v2348G = _V2348G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 11)
)
_V2124G_ObjectIdentity = ObjectIdentity
v2124G = _V2124G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 12)
)
_V2708_ObjectIdentity = ObjectIdentity
v2708 = _V2708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 13)
)
_V2724_ObjectIdentity = ObjectIdentity
v2724 = _V2724_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 14)
)
_V2824_ObjectIdentity = ObjectIdentity
v2824 = _V2824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 15)
)
_V2524G_ObjectIdentity = ObjectIdentity
v2524G = _V2524G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 16)
)
_V2808_ObjectIdentity = ObjectIdentity
v2808 = _V2808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 17)
)
_V2808K_ObjectIdentity = ObjectIdentity
v2808K = _V2808K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 18)
)
_V2724G_ObjectIdentity = ObjectIdentity
v2724G = _V2724G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 19)
)
_V2724GPOE_ObjectIdentity = ObjectIdentity
v2724GPOE = _V2724GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 20)
)
_V2624G_ObjectIdentity = ObjectIdentity
v2624G = _V2624G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 21)
)
_V2624GPOE_ObjectIdentity = ObjectIdentity
v2624GPOE = _V2624GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 22)
)
_V2716GPOE_ObjectIdentity = ObjectIdentity
v2716GPOE = _V2716GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 23)
)
_V2708GPOE_ObjectIdentity = ObjectIdentity
v2708GPOE = _V2708GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 24)
)
_V2716G_ObjectIdentity = ObjectIdentity
v2716G = _V2716G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 26)
)
_V2624GPOES_ObjectIdentity = ObjectIdentity
v2624GPOES = _V2624GPOES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 27)
)
_V2808GPOE_ObjectIdentity = ObjectIdentity
v2808GPOE = _V2808GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 28)
)
_V2814GPOE_ObjectIdentity = ObjectIdentity
v2814GPOE = _V2814GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 29)
)
_V2424G_ObjectIdentity = ObjectIdentity
v2424G = _V2424G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 30)
)
_V2624GPOEK_ObjectIdentity = ObjectIdentity
v2624GPOEK = _V2624GPOEK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 31)
)
_V2724GC_ObjectIdentity = ObjectIdentity
v2724GC = _V2724GC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 32)
)
_V2716GC_ObjectIdentity = ObjectIdentity
v2716GC = _V2716GC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 33)
)
_V2708GC_ObjectIdentity = ObjectIdentity
v2708GC = _V2708GC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 34)
)
_V2809GPOE_ObjectIdentity = ObjectIdentity
v2809GPOE = _V2809GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 35)
)
_V2810P_ObjectIdentity = ObjectIdentity
v2810P = _V2810P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 36)
)
_V2816P_ObjectIdentity = ObjectIdentity
v2816P = _V2816P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 37)
)
_V2824GPOE_ObjectIdentity = ObjectIdentity
v2824GPOE = _V2824GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 38)
)
_V2224G_OP_ObjectIdentity = ObjectIdentity
v2224G_OP = _V2224G_OP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 39)
)
_V2208G_ObjectIdentity = ObjectIdentity
v2208G = _V2208G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 40)
)
_V2216G_ObjectIdentity = ObjectIdentity
v2216G = _V2216G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 41)
)
_V2224GA_ObjectIdentity = ObjectIdentity
v2224GA = _V2224GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 42)
)
_V2724GA_ObjectIdentity = ObjectIdentity
v2724GA = _V2724GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 43)
)
_V2724GB_ObjectIdentity = ObjectIdentity
v2724GB = _V2724GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 44)
)
_V2708GM_ObjectIdentity = ObjectIdentity
v2708GM = _V2708GM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 45)
)
_V2808GV2_ObjectIdentity = ObjectIdentity
v2808GV2 = _V2808GV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 46)
)
_V2708GB_ObjectIdentity = ObjectIdentity
v2708GB = _V2708GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 47)
)
_V2716GB_ObjectIdentity = ObjectIdentity
v2716GB = _V2716GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 48)
)
_V2224GB_ObjectIdentity = ObjectIdentity
v2224GB = _V2224GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 49)
)
_V2824G_ObjectIdentity = ObjectIdentity
v2824G = _V2824G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 6, 50)
)
_V1000_ObjectIdentity = ObjectIdentity
v1000 = _V1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 7)
)
_V1008_ObjectIdentity = ObjectIdentity
v1008 = _V1008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 7, 1)
)
_V5500_ObjectIdentity = ObjectIdentity
v5500 = _V5500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8)
)
_V5524_ObjectIdentity = ObjectIdentity
v5524 = _V5524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 1)
)
_V5516_ObjectIdentity = ObjectIdentity
v5516 = _V5516_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 2)
)
_V5508_ObjectIdentity = ObjectIdentity
v5508 = _V5508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 3)
)
_V5524OP_ObjectIdentity = ObjectIdentity
v5524OP = _V5524OP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 4)
)
_V5524EL_ObjectIdentity = ObjectIdentity
v5524EL = _V5524EL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 5)
)
_V5624F_ObjectIdentity = ObjectIdentity
v5624F = _V5624F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 6)
)
_V1824_ObjectIdentity = ObjectIdentity
v1824 = _V1824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 7)
)
_V1816_ObjectIdentity = ObjectIdentity
v1816 = _V1816_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 8)
)
_V1808_ObjectIdentity = ObjectIdentity
v1808 = _V1808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 9)
)
_V1824EL_ObjectIdentity = ObjectIdentity
v1824EL = _V1824EL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 10)
)
_V5616F_ObjectIdentity = ObjectIdentity
v5616F = _V5616F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 11)
)
_V1824MD_ObjectIdentity = ObjectIdentity
v1824MD = _V1824MD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 12)
)
_V1816MD_ObjectIdentity = ObjectIdentity
v1816MD = _V1816MD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 13)
)
_V1808MD_ObjectIdentity = ObjectIdentity
v1808MD = _V1808MD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 14)
)
_V1824E_ObjectIdentity = ObjectIdentity
v1824E = _V1824E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 15)
)
_V1816EL_ObjectIdentity = ObjectIdentity
v1816EL = _V1816EL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 16)
)
_V1808EL_ObjectIdentity = ObjectIdentity
v1808EL = _V1808EL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 17)
)
_V1816E_ObjectIdentity = ObjectIdentity
v1816E = _V1816E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 18)
)
_V1808E_ObjectIdentity = ObjectIdentity
v1808E = _V1808E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 19)
)
_V1824OP_ObjectIdentity = ObjectIdentity
v1824OP = _V1824OP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 20)
)
_V1816R3_ObjectIdentity = ObjectIdentity
v1816R3 = _V1816R3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 21)
)
_V1816R3MD_ObjectIdentity = ObjectIdentity
v1816R3MD = _V1816R3MD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 22)
)
_V1824R3_ObjectIdentity = ObjectIdentity
v1824R3 = _V1824R3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 23)
)
_V1848_ObjectIdentity = ObjectIdentity
v1848 = _V1848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 24)
)
_V1824R3MD_ObjectIdentity = ObjectIdentity
v1824R3MD = _V1824R3MD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 25)
)
_V1824MDWDM_ObjectIdentity = ObjectIdentity
v1824MDWDM = _V1824MDWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 26)
)
_V1816R4MD_ObjectIdentity = ObjectIdentity
v1816R4MD = _V1816R4MD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 27)
)
_V5624G_ObjectIdentity = ObjectIdentity
v5624G = _V5624G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 8, 28)
)
_V6300_ObjectIdentity = ObjectIdentity
v6300 = _V6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9)
)
_V6324F_ObjectIdentity = ObjectIdentity
v6324F = _V6324F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 1)
)
_V6308F_ObjectIdentity = ObjectIdentity
v6308F = _V6308F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 2)
)
_V6424_ObjectIdentity = ObjectIdentity
v6424 = _V6424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 3)
)
_V6424EL_ObjectIdentity = ObjectIdentity
v6424EL = _V6424EL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 4)
)
_V6424OP_ObjectIdentity = ObjectIdentity
v6424OP = _V6424OP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 5)
)
_V6416F_ObjectIdentity = ObjectIdentity
v6416F = _V6416F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 6)
)
_V6224F_ObjectIdentity = ObjectIdentity
v6224F = _V6224F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 7)
)
_V6024OP_ObjectIdentity = ObjectIdentity
v6024OP = _V6024OP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 8)
)
_V6424F_ObjectIdentity = ObjectIdentity
v6424F = _V6424F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 9)
)
_V6524G_ObjectIdentity = ObjectIdentity
v6524G = _V6524G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 10)
)
_V6424G_ObjectIdentity = ObjectIdentity
v6424G = _V6424G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 11)
)
_V6748XG_ObjectIdentity = ObjectIdentity
v6748XG = _V6748XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 12)
)
_V6744XG_ObjectIdentity = ObjectIdentity
v6744XG = _V6744XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 13)
)
_V6848XG_ObjectIdentity = ObjectIdentity
v6848XG = _V6848XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 14)
)
_V6648XG_ObjectIdentity = ObjectIdentity
v6648XG = _V6648XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 15)
)
_V6824XG_ObjectIdentity = ObjectIdentity
v6824XG = _V6824XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 9, 16)
)
_V5700_ObjectIdentity = ObjectIdentity
v5700 = _V5700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 10)
)
_V5724G_ObjectIdentity = ObjectIdentity
v5724G = _V5724G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 10, 1)
)
_V5700G_ObjectIdentity = ObjectIdentity
v5700G = _V5700G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 10, 2)
)
_V5708_ObjectIdentity = ObjectIdentity
v5708 = _V5708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 10, 3)
)
_V5724G_10G_ObjectIdentity = ObjectIdentity
v5724G_10G = _V5724G_10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 10, 4)
)
_V4200_ObjectIdentity = ObjectIdentity
v4200 = _V4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 11)
)
_V4208_ObjectIdentity = ObjectIdentity
v4208 = _V4208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 11, 1)
)
_Esba_ObjectIdentity = ObjectIdentity
esba = _Esba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 12)
)
_Esb24_d_ObjectIdentity = ObjectIdentity
esb24_d = _Esb24_d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 12, 1)
)
_Esa40_a_ObjectIdentity = ObjectIdentity
esa40_a = _Esa40_a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 12, 2)
)
_HModel_ObjectIdentity = ObjectIdentity
hModel = _HModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 13)
)
_H645s_ObjectIdentity = ObjectIdentity
h645s = _H645s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 13, 1)
)
_AModel_ObjectIdentity = ObjectIdentity
aModel = _AModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 14)
)
_A1100_ObjectIdentity = ObjectIdentity
a1100 = _A1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 14, 1)
)
_A1200_ObjectIdentity = ObjectIdentity
a1200 = _A1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 14, 2)
)
_V3000_ObjectIdentity = ObjectIdentity
v3000 = _V3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 15)
)
_V3208G_ObjectIdentity = ObjectIdentity
v3208G = _V3208G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 15, 1)
)
_V3220G_ObjectIdentity = ObjectIdentity
v3220G = _V3220G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 2, 15, 2)
)
_DasanAccessSDSL_ObjectIdentity = ObjectIdentity
dasanAccessSDSL = _DasanAccessSDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 3)
)
_DasanAccessVDSL_ObjectIdentity = ObjectIdentity
dasanAccessVDSL = _DasanAccessVDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 4)
)
_DasanVERTEX5124_ObjectIdentity = ObjectIdentity
dasanVERTEX5124 = _DasanVERTEX5124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 5)
)
_DasanXDSL_ObjectIdentity = ObjectIdentity
dasanXDSL = _DasanXDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6)
)
_V5900_ObjectIdentity = ObjectIdentity
v5900 = _V5900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1)
)
_V5924LRE_ObjectIdentity = ObjectIdentity
v5924LRE = _V5924LRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 1)
)
_V5924E_ObjectIdentity = ObjectIdentity
v5924E = _V5924E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 2)
)
_V5972_ObjectIdentity = ObjectIdentity
v5972 = _V5972_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 3)
)
_V5972QAM50_ObjectIdentity = ObjectIdentity
v5972QAM50 = _V5972QAM50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 4)
)
_V5972DMT50_ObjectIdentity = ObjectIdentity
v5972DMT50 = _V5972DMT50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 5)
)
_V5924DMT50_ObjectIdentity = ObjectIdentity
v5924DMT50 = _V5924DMT50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 6)
)
_V5916DMT50_ObjectIdentity = ObjectIdentity
v5916DMT50 = _V5916DMT50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 7)
)
_V5916DMT70_ObjectIdentity = ObjectIdentity
v5916DMT70 = _V5916DMT70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 8)
)
_V5916DMT100_ObjectIdentity = ObjectIdentity
v5916DMT100 = _V5916DMT100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 9)
)
_V5908_ObjectIdentity = ObjectIdentity
v5908 = _V5908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 10)
)
_V5908DMT50_ObjectIdentity = ObjectIdentity
v5908DMT50 = _V5908DMT50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 11)
)
_V5908DMT100_ObjectIdentity = ObjectIdentity
v5908DMT100 = _V5908DMT100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 12)
)
_V5924LR50_ObjectIdentity = ObjectIdentity
v5924LR50 = _V5924LR50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 13)
)
_V5924SB_ObjectIdentity = ObjectIdentity
v5924SB = _V5924SB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 15)
)
_V5916B_ObjectIdentity = ObjectIdentity
v5916B = _V5916B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 16)
)
_V5908B_ObjectIdentity = ObjectIdentity
v5908B = _V5908B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 17)
)
_V5924B_ObjectIdentity = ObjectIdentity
v5924B = _V5924B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 18)
)
_V5908L_ObjectIdentity = ObjectIdentity
v5908L = _V5908L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 19)
)
_V5924N_ObjectIdentity = ObjectIdentity
v5924N = _V5924N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 20)
)
_V5924C_ObjectIdentity = ObjectIdentity
v5924C = _V5924C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 21)
)
_V5948_ObjectIdentity = ObjectIdentity
v5948 = _V5948_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 22)
)
_V5924MD_ObjectIdentity = ObjectIdentity
v5924MD = _V5924MD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 23)
)
_V5924P_ObjectIdentity = ObjectIdentity
v5924P = _V5924P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 24)
)
_V5908P_ObjectIdentity = ObjectIdentity
v5908P = _V5908P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 25)
)
_V5924C_R_ObjectIdentity = ObjectIdentity
v5924C_R = _V5924C_R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 26)
)
_Smc7824MVSW_ObjectIdentity = ObjectIdentity
smc7824MVSW = _Smc7824MVSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 27)
)
_V5924O_ObjectIdentity = ObjectIdentity
v5924O = _V5924O_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 28)
)
_V5908O_ObjectIdentity = ObjectIdentity
v5908O = _V5908O_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 29)
)
_V5904_ObjectIdentity = ObjectIdentity
v5904 = _V5904_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 30)
)
_V5906_ObjectIdentity = ObjectIdentity
v5906 = _V5906_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 31)
)
_V5912_ObjectIdentity = ObjectIdentity
v5912 = _V5912_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 32)
)
_V5917_ObjectIdentity = ObjectIdentity
v5917 = _V5917_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 33)
)
_V5916T_ObjectIdentity = ObjectIdentity
v5916T = _V5916T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 1, 34)
)
_V5800_ObjectIdentity = ObjectIdentity
v5800 = _V5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2)
)
_V5809_ObjectIdentity = ObjectIdentity
v5809 = _V5809_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2, 1)
)
_V5824_ObjectIdentity = ObjectIdentity
v5824 = _V5824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2, 2)
)
_V5848_ObjectIdentity = ObjectIdentity
v5848 = _V5848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2, 3)
)
_V5810_ObjectIdentity = ObjectIdentity
v5810 = _V5810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2, 5)
)
_V5817_ObjectIdentity = ObjectIdentity
v5817 = _V5817_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2, 6)
)
_V5804SV_ObjectIdentity = ObjectIdentity
v5804SV = _V5804SV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2, 13)
)
_HiX5630M600_ObjectIdentity = ObjectIdentity
hiX5630M600 = _HiX5630M600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2, 15)
)
_HiX5635M1200_ObjectIdentity = ObjectIdentity
hiX5635M1200 = _HiX5635M1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2, 16)
)
_HiX5625M400_ObjectIdentity = ObjectIdentity
hiX5625M400 = _HiX5625M400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 6, 2, 17)
)
_DasanGEPON_ObjectIdentity = ObjectIdentity
dasanGEPON = _DasanGEPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10)
)
_V6600_ObjectIdentity = ObjectIdentity
v6600 = _V6600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10, 1)
)
_V6608_ObjectIdentity = ObjectIdentity
v6608 = _V6608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10, 1, 1)
)
_V6616_ObjectIdentity = ObjectIdentity
v6616 = _V6616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10, 1, 2)
)
_V6624_ObjectIdentity = ObjectIdentity
v6624 = _V6624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10, 1, 3)
)
_V6500_ObjectIdentity = ObjectIdentity
v6500 = _V6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10, 2)
)
_V6501T_ObjectIdentity = ObjectIdentity
v6501T = _V6501T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10, 2, 1)
)
_V6501P_ObjectIdentity = ObjectIdentity
v6501P = _V6501P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10, 2, 2)
)
_V6504T_ObjectIdentity = ObjectIdentity
v6504T = _V6504T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10, 2, 3)
)
_V6504P_ObjectIdentity = ObjectIdentity
v6504P = _V6504P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 10, 2, 4)
)
_DasanAccessGateway_ObjectIdentity = ObjectIdentity
dasanAccessGateway = _DasanAccessGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 11)
)
_V4600_ObjectIdentity = ObjectIdentity
v4600 = _V4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 11, 1)
)
_V4604S_ObjectIdentity = ObjectIdentity
v4604S = _V4604S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 11, 1, 1)
)
_V4610S_ObjectIdentity = ObjectIdentity
v4610S = _V4610S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 11, 1, 2)
)
_V4664_ObjectIdentity = ObjectIdentity
v4664 = _V4664_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 11, 1, 3)
)
_V4602_ObjectIdentity = ObjectIdentity
v4602 = _V4602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 11, 1, 4)
)
_MSeries_ObjectIdentity = ObjectIdentity
mSeries = _MSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 12)
)
_M3000_ObjectIdentity = ObjectIdentity
m3000 = _M3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 12, 1)
)
_M2200_ObjectIdentity = ObjectIdentity
m2200 = _M2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 12, 2)
)
_M3100_ObjectIdentity = ObjectIdentity
m3100 = _M3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 12, 3)
)
_M3200_ObjectIdentity = ObjectIdentity
m3200 = _M3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 12, 4)
)
_M2400_ObjectIdentity = ObjectIdentity
m2400 = _M2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 12, 5)
)
_M1200_ObjectIdentity = ObjectIdentity
m1200 = _M1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 12, 6)
)
_SSeries_ObjectIdentity = ObjectIdentity
sSeries = _SSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13)
)
_S6804X_ObjectIdentity = ObjectIdentity
s6804X = _S6804X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 1)
)
_S2000_O_8G_ObjectIdentity = ObjectIdentity
s2000_O_8G = _S2000_O_8G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 2)
)
_S2000_8G_ObjectIdentity = ObjectIdentity
s2000_8G = _S2000_8G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 3)
)
_S2228POE_SYD_ObjectIdentity = ObjectIdentity
s2228POE_SYD = _S2228POE_SYD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 4)
)
_S2000_24G_ObjectIdentity = ObjectIdentity
s2000_24G = _S2000_24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 5)
)
_S4424_ObjectIdentity = ObjectIdentity
s4424 = _S4424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 6)
)
_S2224G_ObjectIdentity = ObjectIdentity
s2224G = _S2224G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 7)
)
_S4424G_ObjectIdentity = ObjectIdentity
s4424G = _S4424G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 8)
)
_S4424GP_ObjectIdentity = ObjectIdentity
s4424GP = _S4424GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 9)
)
_S4524G_ObjectIdentity = ObjectIdentity
s4524G = _S4524G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 10)
)
_S4524GP_ObjectIdentity = ObjectIdentity
s4524GP = _S4524GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 11)
)
_S4224G_ObjectIdentity = ObjectIdentity
s4224G = _S4224G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 12)
)
_S4224GP_ObjectIdentity = ObjectIdentity
s4224GP = _S4224GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 13)
)
_S4324G_ObjectIdentity = ObjectIdentity
s4324G = _S4324G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 14)
)
_S4324GP_ObjectIdentity = ObjectIdentity
s4324GP = _S4324GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 13, 15)
)
_Custom_ObjectIdentity = ObjectIdentity
custom = _Custom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 20)
)
_Ds2410_ObjectIdentity = ObjectIdentity
ds2410 = _Ds2410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 20, 1)
)
_Ds2210_ObjectIdentity = ObjectIdentity
ds2210 = _Ds2210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 20, 2)
)
_Ds1610_ObjectIdentity = ObjectIdentity
ds1610 = _Ds1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 20, 3)
)
_Ds0810_ObjectIdentity = ObjectIdentity
ds0810 = _Ds0810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 20, 4)
)
_Fk_OLT_G1040_ObjectIdentity = ObjectIdentity
fk_OLT_G1040 = _Fk_OLT_G1040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 20, 5)
)
_Surpass_ObjectIdentity = ObjectIdentity
surpass = _Surpass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21)
)
_HiD_ObjectIdentity = ObjectIdentity
hiD = _HiD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1)
)
_HiD6610_S212_ObjectIdentity = ObjectIdentity
hiD6610_S212 = _HiD6610_S212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 1)
)
_HiD6610_S213_ObjectIdentity = ObjectIdentity
hiD6610_S213 = _HiD6610_S213_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 2)
)
_HiD6610_S214_ObjectIdentity = ObjectIdentity
hiD6610_S214 = _HiD6610_S214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 3)
)
_HiD6610_S215_ObjectIdentity = ObjectIdentity
hiD6610_S215 = _HiD6610_S215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 4)
)
_HiD6610_S224_ObjectIdentity = ObjectIdentity
hiD6610_S224 = _HiD6610_S224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 5)
)
_HiD6610_S312_ObjectIdentity = ObjectIdentity
hiD6610_S312 = _HiD6610_S312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 6)
)
_HiD6610_S322_ObjectIdentity = ObjectIdentity
hiD6610_S322 = _HiD6610_S322_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 7)
)
_HiD6610_S311_ObjectIdentity = ObjectIdentity
hiD6610_S311 = _HiD6610_S311_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 11)
)
_HiD6610_S321_ObjectIdentity = ObjectIdentity
hiD6610_S321 = _HiD6610_S321_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 12)
)
_HiD6610_S331_ObjectIdentity = ObjectIdentity
hiD6610_S331 = _HiD6610_S331_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 13)
)
_HiD6615_S323_ObjectIdentity = ObjectIdentity
hiD6615_S323 = _HiD6615_S323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 16)
)
_HiD6615_S223_ObjectIdentity = ObjectIdentity
hiD6615_S223 = _HiD6615_S223_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 17)
)
_HiD6615_S324_ObjectIdentity = ObjectIdentity
hiD6615_S324 = _HiD6615_S324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 18)
)
_HiD6615_S411_ObjectIdentity = ObjectIdentity
hiD6615_S411 = _HiD6615_S411_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 19)
)
_HiD6620_S312_ObjectIdentity = ObjectIdentity
hiD6620_S312 = _HiD6620_S312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 21)
)
_HiD6620_S313_ObjectIdentity = ObjectIdentity
hiD6620_S313 = _HiD6620_S313_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 22)
)
_HiD6620_S332_ObjectIdentity = ObjectIdentity
hiD6620_S332 = _HiD6620_S332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 23)
)
_HiD6620_S335_ObjectIdentity = ObjectIdentity
hiD6620_S335 = _HiD6620_S335_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 24)
)
_HiD6620_S336_ObjectIdentity = ObjectIdentity
hiD6620_S336 = _HiD6620_S336_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 25)
)
_HiD6625_S333_ObjectIdentity = ObjectIdentity
hiD6625_S333 = _HiD6625_S333_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 31)
)
_HiD6625_S334_ObjectIdentity = ObjectIdentity
hiD6625_S334 = _HiD6625_S334_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 32)
)
_HiD6615_S331_ObjectIdentity = ObjectIdentity
hiD6615_S331 = _HiD6615_S331_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 33)
)
_HiD6615_S325_ObjectIdentity = ObjectIdentity
hiD6615_S325 = _HiD6615_S325_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 34)
)
_HiD6615_S332_ObjectIdentity = ObjectIdentity
hiD6615_S332 = _HiD6615_S332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 35)
)
_HiD6615_S511_ObjectIdentity = ObjectIdentity
hiD6615_S511 = _HiD6615_S511_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 36)
)
_HiD6608_V5924C_R_ObjectIdentity = ObjectIdentity
hiD6608_V5924C_R = _HiD6608_V5924C_R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 37)
)
_HiD6615_S540_ObjectIdentity = ObjectIdentity
hiD6615_S540 = _HiD6615_S540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 38)
)
_HiD6615_S611_ObjectIdentity = ObjectIdentity
hiD6615_S611 = _HiD6615_S611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 39)
)
_HiD6615_S340_ObjectIdentity = ObjectIdentity
hiD6615_S340 = _HiD6615_S340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 40)
)
_HiD6615_S344_ObjectIdentity = ObjectIdentity
hiD6615_S344 = _HiD6615_S344_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 1, 41)
)
_HiX_ObjectIdentity = ObjectIdentity
hiX = _HiX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 2)
)
_HiX5620_A50_ObjectIdentity = ObjectIdentity
hiX5620_A50 = _HiX5620_A50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 2, 1)
)
_HiX5620_V25_ObjectIdentity = ObjectIdentity
hiX5620_V25 = _HiX5620_V25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 2, 2)
)
_HiX5620_V24_ObjectIdentity = ObjectIdentity
hiX5620_V24 = _HiX5620_V24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 2, 3)
)
_HiX5430_ObjectIdentity = ObjectIdentity
hiX5430 = _HiX5430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 2, 4)
)
_HiX5750_ObjectIdentity = ObjectIdentity
hiX5750 = _HiX5750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 2, 5)
)
_AHub_ObjectIdentity = ObjectIdentity
aHub = _AHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 3)
)
_AHub4A_ObjectIdentity = ObjectIdentity
aHub4A = _AHub4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 3, 1)
)
_AHub3B_ObjectIdentity = ObjectIdentity
aHub3B = _AHub3B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 21, 3, 2)
)
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 22)
)
_WirelessAC_ObjectIdentity = ObjectIdentity
wirelessAC = _WirelessAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 22, 1)
)
_W7200_ObjectIdentity = ObjectIdentity
w7200 = _W7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 22, 1, 1)
)
_W7300_ObjectIdentity = ObjectIdentity
w7300 = _W7300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 22, 1, 2)
)
_WirelessAP_ObjectIdentity = ObjectIdentity
wirelessAP = _WirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 22, 2)
)
_W110_ObjectIdentity = ObjectIdentity
w110 = _W110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 22, 2, 1)
)
_W120_ObjectIdentity = ObjectIdentity
w120 = _W120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 1, 22, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-PRODUCTS-MIB",
    **{"dasanRouter": dasanRouter,
       "v1500": v1500,
       "v1501": v1501,
       "v1502T": v1502T,
       "v2500": v2500,
       "v2501": v2501,
       "v2501T": v2501T,
       "v2502T": v2502T,
       "v2503": v2503,
       "v2600": v2600,
       "v2602T": v2602T,
       "v2602D": v2602D,
       "v2608T": v2608T,
       "v2602A": v2602A,
       "v3100": v3100,
       "v3104": v3104,
       "v3108": v3108,
       "v3112": v3112,
       "v3300": v3300,
       "v3302": v3302,
       "dasanSwitch": dasanSwitch,
       "v5100": v5100,
       "v5124": v5124,
       "v5108F": v5108F,
       "v5116F": v5116F,
       "v5124F": v5124F,
       "v1724": v1724,
       "v1708F": v1708F,
       "v5224": v5224,
       "v5216F": v5216F,
       "v5324": v5324,
       "v5124E": v5124E,
       "v1708": v1708,
       "v1716": v1716,
       "v1724plus": v1724plus,
       "v1624": v1624,
       "v1616": v1616,
       "v1608": v1608,
       "v5216": v5216,
       "v1624MD": v1624MD,
       "v1624CWDM": v1624CWDM,
       "v2624": v2624,
       "v2616": v2616,
       "v2608": v2608,
       "v1100": v1100,
       "v1124": v1124,
       "v1108F": v1108F,
       "v1224": v1224,
       "v1124C": v1124C,
       "v1324": v1324,
       "v1424G": v1424G,
       "v1916GR": v1916GR,
       "v6100": v6100,
       "v6124": v6124,
       "v6108": v6108,
       "v6124F": v6124F,
       "v6108F": v6108F,
       "v6216G": v6216G,
       "v6116G": v6116G,
       "v6224": v6224,
       "v6108G": v6108G,
       "v8000": v8000,
       "v8240": v8240,
       "v8272": v8272,
       "v8500": v8500,
       "v8300": v8300,
       "v8102": v8102,
       "v8400": v8400,
       "v8106": v8106,
       "v8600": v8600,
       "v8605": v8605,
       "v8607": v8607,
       "v8610": v8610,
       "v8600-IU": v8600_IU,
       "v8600-CU": v8600_CU,
       "v8600-IU-GE24-GT8": v8600_IU_GE24_GT8,
       "v8600-IU-GT24-GE8": v8600_IU_GT24_GE8,
       "v8600-IU-GE44-10GE4": v8600_IU_GE44_10GE4,
       "v8600-IU-GT48": v8600_IU_GT48,
       "v8600-IU-GT24-GE20-10GE4": v8600_IU_GT24_GE20_10GE4,
       "v8600-IU-10GE8": v8600_IU_10GE8,
       "v8600-IU-GT48P": v8600_IU_GT48P,
       "v8600-IU-10GE8F": v8600_IU_10GE8F,
       "v8600-IU-GE44-10GE4F": v8600_IU_GE44_10GE4F,
       "v8600-IU-GT48F": v8600_IU_GT48F,
       "v8600-IU-10GE48": v8600_IU_10GE48,
       "v8600-IU-40GE12": v8600_IU_40GE12,
       "v8600-IU-10GE24-40GE4": v8600_IU_10GE24_40GE4,
       "ds-PA600I": ds_PA600I,
       "ds-PD600I": ds_PD600I,
       "ds-PA1600I": ds_PA1600I,
       "ds-PD1600I": ds_PD1600I,
       "ds-PA1600I-PL": ds_PA1600I_PL,
       "ds-PA3000I-PL": ds_PA3000I_PL,
       "v5200": v5200,
       "v5208G": v5208G,
       "v5212G": v5212G,
       "v5424G": v5424G,
       "v5224G": v5224G,
       "v5324G": v5324G,
       "v5524G": v5524G,
       "v5548G": v5548G,
       "v5524XG": v5524XG,
       "v5848G": v5848G,
       "v5504XG": v5504XG,
       "v5812G": v5812G,
       "v5524GS": v5524GS,
       "v5806": v5806,
       "gpm4-2G": gpm4_2G,
       "v5824G": v5824G,
       "v5648G": v5648G,
       "v5836G": v5836G,
       "v2100": v2100,
       "v2108": v2108,
       "v2116": v2116,
       "v2124": v2124,
       "v2308": v2308,
       "v2316": v2316,
       "v2324": v2324,
       "v2116J": v2116J,
       "v2124J": v2124J,
       "v2424POE": v2424POE,
       "v2324G": v2324G,
       "v2348G": v2348G,
       "v2124G": v2124G,
       "v2708": v2708,
       "v2724": v2724,
       "v2824": v2824,
       "v2524G": v2524G,
       "v2808": v2808,
       "v2808K": v2808K,
       "v2724G": v2724G,
       "v2724GPOE": v2724GPOE,
       "v2624G": v2624G,
       "v2624GPOE": v2624GPOE,
       "v2716GPOE": v2716GPOE,
       "v2708GPOE": v2708GPOE,
       "v2716G": v2716G,
       "v2624GPOES": v2624GPOES,
       "v2808GPOE": v2808GPOE,
       "v2814GPOE": v2814GPOE,
       "v2424G": v2424G,
       "v2624GPOEK": v2624GPOEK,
       "v2724GC": v2724GC,
       "v2716GC": v2716GC,
       "v2708GC": v2708GC,
       "v2809GPOE": v2809GPOE,
       "v2810P": v2810P,
       "v2816P": v2816P,
       "v2824GPOE": v2824GPOE,
       "v2224G-OP": v2224G_OP,
       "v2208G": v2208G,
       "v2216G": v2216G,
       "v2224GA": v2224GA,
       "v2724GA": v2724GA,
       "v2724GB": v2724GB,
       "v2708GM": v2708GM,
       "v2808GV2": v2808GV2,
       "v2708GB": v2708GB,
       "v2716GB": v2716GB,
       "v2224GB": v2224GB,
       "v2824G": v2824G,
       "v1000": v1000,
       "v1008": v1008,
       "v5500": v5500,
       "v5524": v5524,
       "v5516": v5516,
       "v5508": v5508,
       "v5524OP": v5524OP,
       "v5524EL": v5524EL,
       "v5624F": v5624F,
       "v1824": v1824,
       "v1816": v1816,
       "v1808": v1808,
       "v1824EL": v1824EL,
       "v5616F": v5616F,
       "v1824MD": v1824MD,
       "v1816MD": v1816MD,
       "v1808MD": v1808MD,
       "v1824E": v1824E,
       "v1816EL": v1816EL,
       "v1808EL": v1808EL,
       "v1816E": v1816E,
       "v1808E": v1808E,
       "v1824OP": v1824OP,
       "v1816R3": v1816R3,
       "v1816R3MD": v1816R3MD,
       "v1824R3": v1824R3,
       "v1848": v1848,
       "v1824R3MD": v1824R3MD,
       "v1824MDWDM": v1824MDWDM,
       "v1816R4MD": v1816R4MD,
       "v5624G": v5624G,
       "v6300": v6300,
       "v6324F": v6324F,
       "v6308F": v6308F,
       "v6424": v6424,
       "v6424EL": v6424EL,
       "v6424OP": v6424OP,
       "v6416F": v6416F,
       "v6224F": v6224F,
       "v6024OP": v6024OP,
       "v6424F": v6424F,
       "v6524G": v6524G,
       "v6424G": v6424G,
       "v6748XG": v6748XG,
       "v6744XG": v6744XG,
       "v6848XG": v6848XG,
       "v6648XG": v6648XG,
       "v6824XG": v6824XG,
       "v5700": v5700,
       "v5724G": v5724G,
       "v5700G": v5700G,
       "v5708": v5708,
       "v5724G-10G": v5724G_10G,
       "v4200": v4200,
       "v4208": v4208,
       "esba": esba,
       "esb24-d": esb24_d,
       "esa40-a": esa40_a,
       "hModel": hModel,
       "h645s": h645s,
       "aModel": aModel,
       "a1100": a1100,
       "a1200": a1200,
       "v3000": v3000,
       "v3208G": v3208G,
       "v3220G": v3220G,
       "dasanAccessSDSL": dasanAccessSDSL,
       "dasanAccessVDSL": dasanAccessVDSL,
       "dasanVERTEX5124": dasanVERTEX5124,
       "dasanXDSL": dasanXDSL,
       "v5900": v5900,
       "v5924LRE": v5924LRE,
       "v5924E": v5924E,
       "v5972": v5972,
       "v5972QAM50": v5972QAM50,
       "v5972DMT50": v5972DMT50,
       "v5924DMT50": v5924DMT50,
       "v5916DMT50": v5916DMT50,
       "v5916DMT70": v5916DMT70,
       "v5916DMT100": v5916DMT100,
       "v5908": v5908,
       "v5908DMT50": v5908DMT50,
       "v5908DMT100": v5908DMT100,
       "v5924LR50": v5924LR50,
       "v5924SB": v5924SB,
       "v5916B": v5916B,
       "v5908B": v5908B,
       "v5924B": v5924B,
       "v5908L": v5908L,
       "v5924N": v5924N,
       "v5924C": v5924C,
       "v5948": v5948,
       "v5924MD": v5924MD,
       "v5924P": v5924P,
       "v5908P": v5908P,
       "v5924C-R": v5924C_R,
       "smc7824MVSW": smc7824MVSW,
       "v5924O": v5924O,
       "v5908O": v5908O,
       "v5904": v5904,
       "v5906": v5906,
       "v5912": v5912,
       "v5917": v5917,
       "v5916T": v5916T,
       "v5800": v5800,
       "v5809": v5809,
       "v5824": v5824,
       "v5848": v5848,
       "v5810": v5810,
       "v5817": v5817,
       "v5804SV": v5804SV,
       "hiX5630M600": hiX5630M600,
       "hiX5635M1200": hiX5635M1200,
       "hiX5625M400": hiX5625M400,
       "dasanGEPON": dasanGEPON,
       "v6600": v6600,
       "v6608": v6608,
       "v6616": v6616,
       "v6624": v6624,
       "v6500": v6500,
       "v6501T": v6501T,
       "v6501P": v6501P,
       "v6504T": v6504T,
       "v6504P": v6504P,
       "dasanAccessGateway": dasanAccessGateway,
       "v4600": v4600,
       "v4604S": v4604S,
       "v4610S": v4610S,
       "v4664": v4664,
       "v4602": v4602,
       "mSeries": mSeries,
       "m3000": m3000,
       "m2200": m2200,
       "m3100": m3100,
       "m3200": m3200,
       "m2400": m2400,
       "m1200": m1200,
       "sSeries": sSeries,
       "s6804X": s6804X,
       "s2000-O-8G": s2000_O_8G,
       "s2000-8G": s2000_8G,
       "s2228POE-SYD": s2228POE_SYD,
       "s2000-24G": s2000_24G,
       "s4424": s4424,
       "s2224G": s2224G,
       "s4424G": s4424G,
       "s4424GP": s4424GP,
       "s4524G": s4524G,
       "s4524GP": s4524GP,
       "s4224G": s4224G,
       "s4224GP": s4224GP,
       "s4324G": s4324G,
       "s4324GP": s4324GP,
       "custom": custom,
       "ds2410": ds2410,
       "ds2210": ds2210,
       "ds1610": ds1610,
       "ds0810": ds0810,
       "fk-OLT-G1040": fk_OLT_G1040,
       "surpass": surpass,
       "hiD": hiD,
       "hiD6610-S212": hiD6610_S212,
       "hiD6610-S213": hiD6610_S213,
       "hiD6610-S214": hiD6610_S214,
       "hiD6610-S215": hiD6610_S215,
       "hiD6610-S224": hiD6610_S224,
       "hiD6610-S312": hiD6610_S312,
       "hiD6610-S322": hiD6610_S322,
       "hiD6610-S311": hiD6610_S311,
       "hiD6610-S321": hiD6610_S321,
       "hiD6610-S331": hiD6610_S331,
       "hiD6615-S323": hiD6615_S323,
       "hiD6615-S223": hiD6615_S223,
       "hiD6615-S324": hiD6615_S324,
       "hiD6615-S411": hiD6615_S411,
       "hiD6620-S312": hiD6620_S312,
       "hiD6620-S313": hiD6620_S313,
       "hiD6620-S332": hiD6620_S332,
       "hiD6620-S335": hiD6620_S335,
       "hiD6620-S336": hiD6620_S336,
       "hiD6625-S333": hiD6625_S333,
       "hiD6625-S334": hiD6625_S334,
       "hiD6615-S331": hiD6615_S331,
       "hiD6615-S325": hiD6615_S325,
       "hiD6615-S332": hiD6615_S332,
       "hiD6615-S511": hiD6615_S511,
       "hiD6608-V5924C-R": hiD6608_V5924C_R,
       "hiD6615-S540": hiD6615_S540,
       "hiD6615-S611": hiD6615_S611,
       "hiD6615-S340": hiD6615_S340,
       "hiD6615-S344": hiD6615_S344,
       "hiX": hiX,
       "hiX5620-A50": hiX5620_A50,
       "hiX5620-V25": hiX5620_V25,
       "hiX5620-V24": hiX5620_V24,
       "hiX5430": hiX5430,
       "hiX5750": hiX5750,
       "aHub": aHub,
       "aHub4A": aHub4A,
       "aHub3B": aHub3B,
       "wireless": wireless,
       "wirelessAC": wirelessAC,
       "w7200": w7200,
       "w7300": w7300,
       "wirelessAP": wirelessAP,
       "w110": w110,
       "w120": w120,
       "dasanProductsMIB": dasanProductsMIB}
)
