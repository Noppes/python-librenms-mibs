# SNMP MIB module (HH3C-ENTITY-VENDORTYPE-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-ENTITY-VENDORTYPE-OID-MIB

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

(hh3c,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3c")

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

hh3cEntityVendorTypeOID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEntityVendortypeObjects_ObjectIdentity = ObjectIdentity
hh3cEntityVendortypeObjects = _Hh3cEntityVendortypeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1)
)
_Hh3cevtOther_ObjectIdentity = ObjectIdentity
hh3cevtOther = _Hh3cevtOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1)
)
_Hh3cevtOtherUnknownCard_ObjectIdentity = ObjectIdentity
hh3cevtOtherUnknownCard = _Hh3cevtOtherUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 1)
)
_Hh3cevtCPU_ObjectIdentity = ObjectIdentity
hh3cevtCPU = _Hh3cevtCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 2)
)
_Hh3cevtGeneralCPU_ObjectIdentity = ObjectIdentity
hh3cevtGeneralCPU = _Hh3cevtGeneralCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 2, 1)
)
_Hh3cevtDOM_ObjectIdentity = ObjectIdentity
hh3cevtDOM = _Hh3cevtDOM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 3)
)
_Hh3cevtCFCard_ObjectIdentity = ObjectIdentity
hh3cevtCFCard = _Hh3cevtCFCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 4)
)
_Hh3cevtHardDisk_ObjectIdentity = ObjectIdentity
hh3cevtHardDisk = _Hh3cevtHardDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 5)
)
_Hh3cevtSDCard_ObjectIdentity = ObjectIdentity
hh3cevtSDCard = _Hh3cevtSDCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 6)
)
_Hh3cevtMEM_ObjectIdentity = ObjectIdentity
hh3cevtMEM = _Hh3cevtMEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 1, 7)
)
_Hh3cevtUnknown_ObjectIdentity = ObjectIdentity
hh3cevtUnknown = _Hh3cevtUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 2)
)
_Hh3cevtChassis_ObjectIdentity = ObjectIdentity
hh3cevtChassis = _Hh3cevtChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 3)
)
_Hh3cevtBackplane_ObjectIdentity = ObjectIdentity
hh3cevtBackplane = _Hh3cevtBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 4)
)
_Hh3cevtContainer_ObjectIdentity = ObjectIdentity
hh3cevtContainer = _Hh3cevtContainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 5)
)
_Hh3cevtPowerSupply_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupply = _Hh3cevtPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6)
)
_Hh3cevtPowerSupplyAC_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyAC = _Hh3cevtPowerSupplyAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 2)
)
_Hh3cevtPowerSupplyDC_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyDC = _Hh3cevtPowerSupplyDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 3)
)
_Hh3cevtPowerSupplySTD130W_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplySTD130W = _Hh3cevtPowerSupplySTD130W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 4)
)
_Hh3cevtPowerSupplySTD180W_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplySTD180W = _Hh3cevtPowerSupplySTD180W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 5)
)
_Hh3cevtPowerSupplyPOE24Port_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyPOE24Port = _Hh3cevtPowerSupplyPOE24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 6)
)
_Hh3cevtPowerSupplyPOE48Port_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyPOE48Port = _Hh3cevtPowerSupplyPOE48Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 7)
)
_Hh3cevtPowerSupplyLSUM1AC2500_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSUM1AC2500 = _Hh3cevtPowerSupplyLSUM1AC2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 8)
)
_Hh3cevtPowerSupplyLSUM2AC2500_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSUM2AC2500 = _Hh3cevtPowerSupplyLSUM2AC2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 9)
)
_Hh3cevtPowerSupplyLSUM1DC2400_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSUM1DC2400 = _Hh3cevtPowerSupplyLSUM1DC2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 10)
)
_Hh3cevtPowerSupplyLSUM1AC1200_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSUM1AC1200 = _Hh3cevtPowerSupplyLSUM1AC1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 11)
)
_Hh3cevtPowerSupplyLSQM1DC2400_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM1DC2400 = _Hh3cevtPowerSupplyLSQM1DC2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 12)
)
_Hh3cevtPowerSupplyLSUM5AC2500_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSUM5AC2500 = _Hh3cevtPowerSupplyLSUM5AC2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 13)
)
_Hh3cevtPowerSupplyLSUM5DC2400_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSUM5DC2400 = _Hh3cevtPowerSupplyLSUM5DC2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 14)
)
_Hh3cevtPowerSupplyLSUM6DC2400_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSUM6DC2400 = _Hh3cevtPowerSupplyLSUM6DC2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 15)
)
_Hh3cevtPowerSupplyLSUM6AC2500_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSUM6AC2500 = _Hh3cevtPowerSupplyLSUM6AC2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 16)
)
_Hh3cevtPowerSupplyLSQM1AC1400_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM1AC1400 = _Hh3cevtPowerSupplyLSQM1AC1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 17)
)
_Hh3cevtPowerSupplyLSQM1DC1400_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM1DC1400 = _Hh3cevtPowerSupplyLSQM1DC1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 18)
)
_Hh3cevtPowerSupplyLSQM1AC2800_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM1AC2800 = _Hh3cevtPowerSupplyLSQM1AC2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 19)
)
_Hh3cevtPowerSupplyLSQM2AC1400_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM2AC1400 = _Hh3cevtPowerSupplyLSQM2AC1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 20)
)
_Hh3cevtPowerSupplyLSQM1AC6000_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM1AC6000 = _Hh3cevtPowerSupplyLSQM1AC6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 21)
)
_Hh3cevtPowerSupplyLSQM2AC6000_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM2AC6000 = _Hh3cevtPowerSupplyLSQM2AC6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 22)
)
_Hh3cevtPowerSupplyLSQM1AC300_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM1AC300 = _Hh3cevtPowerSupplyLSQM1AC300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 23)
)
_Hh3cevtPowerSupplyLSQM1AC650_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM1AC650 = _Hh3cevtPowerSupplyLSQM1AC650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 24)
)
_Hh3cevtPowerSupplyLSQM1DC650_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM1DC650 = _Hh3cevtPowerSupplyLSQM1DC650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 25)
)
_Hh3cevtPowerSupplyLSQM1PWRSPA_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM1PWRSPA = _Hh3cevtPowerSupplyLSQM1PWRSPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 26)
)
_Hh3cevtPowerSupplyLSWM1RPS800_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSWM1RPS800 = _Hh3cevtPowerSupplyLSWM1RPS800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 27)
)
_Hh3cevtPowerSupplyLSQM7AC1400_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM7AC1400 = _Hh3cevtPowerSupplyLSQM7AC1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 28)
)
_Hh3cevtPowerSupplyLSQM7DC1400_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM7DC1400 = _Hh3cevtPowerSupplyLSQM7DC1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 29)
)
_Hh3cevtPowerSupplyLSQM7AC2800_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM7AC2800 = _Hh3cevtPowerSupplyLSQM7AC2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 30)
)
_Hh3cevtPowerSupplyLSQM7AC6000_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM7AC6000 = _Hh3cevtPowerSupplyLSQM7AC6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 31)
)
_Hh3cevtPowerSupplyLSQM7AC300_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM7AC300 = _Hh3cevtPowerSupplyLSQM7AC300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 32)
)
_Hh3cevtPowerSupplyLSQM7AC650_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM7AC650 = _Hh3cevtPowerSupplyLSQM7AC650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 33)
)
_Hh3cevtPowerSupplyLSQM7DC650_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSQM7DC650 = _Hh3cevtPowerSupplyLSQM7DC650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 34)
)
_Hh3cevtPowerSupplyLSWM2RPS800_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplyLSWM2RPS800 = _Hh3cevtPowerSupplyLSWM2RPS800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 35)
)
_Hh3cevtPowerSupplySecPathAC_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplySecPathAC = _Hh3cevtPowerSupplySecPathAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 36)
)
_Hh3cevtPowerSupplySecPathDC_ObjectIdentity = ObjectIdentity
hh3cevtPowerSupplySecPathDC = _Hh3cevtPowerSupplySecPathDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 6, 37)
)
_Hh3cevtFan_ObjectIdentity = ObjectIdentity
hh3cevtFan = _Hh3cevtFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7)
)
_Hh3cevtHotSwapFan_ObjectIdentity = ObjectIdentity
hh3cevtHotSwapFan = _Hh3cevtHotSwapFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 1)
)
_Hh3cevtNonHotSwapFan_ObjectIdentity = ObjectIdentity
hh3cevtNonHotSwapFan = _Hh3cevtNonHotSwapFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 2)
)
_Hh3cevtFanLSUM110504_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM110504 = _Hh3cevtFanLSUM110504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 3)
)
_Hh3cevtFanLSUM110508_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM110508 = _Hh3cevtFanLSUM110508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 4)
)
_Hh3cevtFanLSUM110508V_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM110508V = _Hh3cevtFanLSUM110508V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 5)
)
_Hh3cevtFanLSUM110512_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM110512 = _Hh3cevtFanLSUM110512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 6)
)
_Hh3cevtFanLSUM210512_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM210512 = _Hh3cevtFanLSUM210512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 7)
)
_Hh3cevtFanLSUM510504_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM510504 = _Hh3cevtFanLSUM510504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 8)
)
_Hh3cevtFanLSUM510508_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM510508 = _Hh3cevtFanLSUM510508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 9)
)
_Hh3cevtFanLSUM510508V_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM510508V = _Hh3cevtFanLSUM510508V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 10)
)
_Hh3cevtFanLSUM510512U_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM510512U = _Hh3cevtFanLSUM510512U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 11)
)
_Hh3cevtFanLSUM510512D_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM510512D = _Hh3cevtFanLSUM510512D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 12)
)
_Hh3cevtFanLSUM511908V_ObjectIdentity = ObjectIdentity
hh3cevtFanLSUM511908V = _Hh3cevtFanLSUM511908V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 13)
)
_Hh3cevtFanLSQM17502E_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM17502E = _Hh3cevtFanLSQM17502E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 14)
)
_Hh3cevtFanLSQM17503E_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM17503E = _Hh3cevtFanLSQM17503E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 15)
)
_Hh3cevtFanLSQM17503ES_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM17503ES = _Hh3cevtFanLSQM17503ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 16)
)
_Hh3cevtFanLSQM17506E_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM17506E = _Hh3cevtFanLSQM17506E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 17)
)
_Hh3cevtFanLSQM17506EV_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM17506EV = _Hh3cevtFanLSQM17506EV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 18)
)
_Hh3cevtFanLSQM17510E_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM17510E = _Hh3cevtFanLSQM17510E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 19)
)
_Hh3cevtFanLSQM57503_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM57503 = _Hh3cevtFanLSQM57503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 20)
)
_Hh3cevtFanLSQM57502_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM57502 = _Hh3cevtFanLSQM57502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 21)
)
_Hh3cevtFanLSQM57506_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM57506 = _Hh3cevtFanLSQM57506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 22)
)
_Hh3cevtFanLSQM57510_ObjectIdentity = ObjectIdentity
hh3cevtFanLSQM57510 = _Hh3cevtFanLSQM57510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 23)
)
_Hh3cevtHotSwapFan_NSUM1BFANSC_ObjectIdentity = ObjectIdentity
hh3cevtHotSwapFan_NSUM1BFANSC = _Hh3cevtHotSwapFan_NSUM1BFANSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 24)
)
_Hh3cevtHotSwapFan_NSUM1BFANSCB_ObjectIdentity = ObjectIdentity
hh3cevtHotSwapFan_NSUM1BFANSCB = _Hh3cevtHotSwapFan_NSUM1BFANSCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 7, 25)
)
_Hh3cevtSensor_ObjectIdentity = ObjectIdentity
hh3cevtSensor = _Hh3cevtSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 8)
)
_Hh3cevtSensorTemperature_ObjectIdentity = ObjectIdentity
hh3cevtSensorTemperature = _Hh3cevtSensorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 8, 1)
)
_Hh3cevtSensorVoltage_ObjectIdentity = ObjectIdentity
hh3cevtSensorVoltage = _Hh3cevtSensorVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 8, 2)
)
_Hh3cevtSensorFanSpeed_ObjectIdentity = ObjectIdentity
hh3cevtSensorFanSpeed = _Hh3cevtSensorFanSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 8, 3)
)
_Hh3cevtModule_ObjectIdentity = ObjectIdentity
hh3cevtModule = _Hh3cevtModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9)
)
_Hh3cevtModuleUnknownCard_ObjectIdentity = ObjectIdentity
hh3cevtModuleUnknownCard = _Hh3cevtModuleUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 1)
)
_Hh3cevtModuleCommonCards_ObjectIdentity = ObjectIdentity
hh3cevtModuleCommonCards = _Hh3cevtModuleCommonCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2)
)
_Hh3cevtModuleBoxCEN_ObjectIdentity = ObjectIdentity
hh3cevtModuleBoxCEN = _Hh3cevtModuleBoxCEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2, 1)
)
_Hh3cevtModuleBoxIRF48GE_ObjectIdentity = ObjectIdentity
hh3cevtModuleBoxIRF48GE = _Hh3cevtModuleBoxIRF48GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2, 2)
)
_Hh3cevtModuleBoxIRF24GE24TGE_ObjectIdentity = ObjectIdentity
hh3cevtModuleBoxIRF24GE24TGE = _Hh3cevtModuleBoxIRF24GE24TGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2, 3)
)
_Hh3cevtModuleChassisMpu_ObjectIdentity = ObjectIdentity
hh3cevtModuleChassisMpu = _Hh3cevtModuleChassisMpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2, 4)
)
_Hh3cevtModuleLPU48GE_ObjectIdentity = ObjectIdentity
hh3cevtModuleLPU48GE = _Hh3cevtModuleLPU48GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2, 5)
)
_Hh3cevtModuleLPU4GE4Serial_ObjectIdentity = ObjectIdentity
hh3cevtModuleLPU4GE4Serial = _Hh3cevtModuleLPU4GE4Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2, 6)
)
_Hh3cevtModuleLPU4GE4Pos_ObjectIdentity = ObjectIdentity
hh3cevtModuleLPU4GE4Pos = _Hh3cevtModuleLPU4GE4Pos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2, 7)
)
_Hh3cevtModuleLPU4GE4E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleLPU4GE4E1 = _Hh3cevtModuleLPU4GE4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 2, 8)
)
_Hh3cevtModuleRouterType_ObjectIdentity = ObjectIdentity
hh3cevtModuleRouterType = _Hh3cevtModuleRouterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3)
)
_Hh3cevtModuleRt_As_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_As = _Hh3cevtModuleRt_As_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 2)
)
_Hh3cevtModuleRt_Sa_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sa = _Hh3cevtModuleRt_Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 3)
)
_Hh3cevtModuleRt_Bi_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Bi = _Hh3cevtModuleRt_Bi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 4)
)
_Hh3cevtModuleRt_E12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E12 = _Hh3cevtModuleRt_E12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5)
)
_Hh3cevtModuleRt_E14_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E14 = _Hh3cevtModuleRt_E14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 6)
)
_Hh3cevtModuleRt_Fe1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe1 = _Hh3cevtModuleRt_Fe1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 7)
)
_Hh3cevtModuleRt_E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E1 = _Hh3cevtModuleRt_E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 8)
)
_Hh3cevtModuleRt_Fe2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe2 = _Hh3cevtModuleRt_Fe2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 9)
)
_Hh3cevtModuleRt_Vi2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Vi2 = _Hh3cevtModuleRt_Vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 11)
)
_Hh3cevtModuleRt_Vi4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Vi4 = _Hh3cevtModuleRt_Vi4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 12)
)
_Hh3cevtModuleRt_Vi30_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Vi30 = _Hh3cevtModuleRt_Vi30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 13)
)
_Hh3cevtModuleRt_S1b_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_S1b = _Hh3cevtModuleRt_S1b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 14)
)
_Hh3cevtModuleRt_Sa2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sa2 = _Hh3cevtModuleRt_Sa2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 15)
)
_Hh3cevtModuleRt_As16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_As16 = _Hh3cevtModuleRt_As16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 16)
)
_Hh3cevtModuleRt_New8as_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_New8as = _Hh3cevtModuleRt_New8as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 17)
)
_Hh3cevtModuleRt_Sa1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sa1 = _Hh3cevtModuleRt_Sa1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 18)
)
_Hh3cevtModuleRt_Fxs2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fxs2 = _Hh3cevtModuleRt_Fxs2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 19)
)
_Hh3cevtModuleRt_Fxo2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fxo2 = _Hh3cevtModuleRt_Fxo2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 20)
)
_Hh3cevtModuleRt_Em2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Em2 = _Hh3cevtModuleRt_Em2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 21)
)
_Hh3cevtModuleRt_Fxs4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fxs4 = _Hh3cevtModuleRt_Fxs4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 22)
)
_Hh3cevtModuleRt_Fxo4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fxo4 = _Hh3cevtModuleRt_Fxo4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 23)
)
_Hh3cevtModuleRt_Em4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Em4 = _Hh3cevtModuleRt_Em4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 24)
)
_Hh3cevtModuleRt_Sab_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sab = _Hh3cevtModuleRt_Sab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 25)
)
_Hh3cevtModuleRt_E1vi_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E1vi = _Hh3cevtModuleRt_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 26)
)
_Hh3cevtModuleRt_Am12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Am12 = _Hh3cevtModuleRt_Am12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 27)
)
_Hh3cevtModuleRt_Am6_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Am6 = _Hh3cevtModuleRt_Am6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 28)
)
_Hh3cevtModuleRt_Ndec_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ndec = _Hh3cevtModuleRt_Ndec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 29)
)
_Hh3cevtModuleRt_Newsa2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Newsa2 = _Hh3cevtModuleRt_Newsa2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 30)
)
_Hh3cevtModuleRt_Aux_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Aux = _Hh3cevtModuleRt_Aux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 31)
)
_Hh3cevtModuleRt_Console_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Console = _Hh3cevtModuleRt_Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 32)
)
_Hh3cevtModuleRt_Sic_wan_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_wan = _Hh3cevtModuleRt_Sic_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 33)
)
_Hh3cevtModuleRt_Sic_1fe_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1fe = _Hh3cevtModuleRt_Sic_1fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 34)
)
_Hh3cevtModuleRt_Sic_1sa_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1sa = _Hh3cevtModuleRt_Sic_1sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 35)
)
_Hh3cevtModuleRt_Sic_3as_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_3as = _Hh3cevtModuleRt_Sic_3as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 36)
)
_Hh3cevtModuleRt_Sic_1e1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1e1 = _Hh3cevtModuleRt_Sic_1e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 37)
)
_Hh3cevtModuleRt_Sic_1t1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1t1 = _Hh3cevtModuleRt_Sic_1t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 38)
)
_Hh3cevtModuleRt_Sic_1bu_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1bu = _Hh3cevtModuleRt_Sic_1bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 39)
)
_Hh3cevtModuleRt_Sic_2bu_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2bu = _Hh3cevtModuleRt_Sic_2bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 40)
)
_Hh3cevtModuleRt_Sic_1bs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1bs = _Hh3cevtModuleRt_Sic_1bs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 41)
)
_Hh3cevtModuleRt_Sic_2bs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2bs = _Hh3cevtModuleRt_Sic_2bs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 42)
)
_Hh3cevtModuleRt_Sic_1am_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1am = _Hh3cevtModuleRt_Sic_1am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 43)
)
_Hh3cevtModuleRt_Sic_2am_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2am = _Hh3cevtModuleRt_Sic_2am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 44)
)
_Hh3cevtModuleRt_Sic_1em_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1em = _Hh3cevtModuleRt_Sic_1em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 45)
)
_Hh3cevtModuleRt_Sic_2em_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2em = _Hh3cevtModuleRt_Sic_2em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 46)
)
_Hh3cevtModuleRt_Sic_1fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1fxs = _Hh3cevtModuleRt_Sic_1fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 47)
)
_Hh3cevtModuleRt_Sic_2fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2fxs = _Hh3cevtModuleRt_Sic_2fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 48)
)
_Hh3cevtModuleRt_Sic_1fxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_1fxo = _Hh3cevtModuleRt_Sic_1fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 49)
)
_Hh3cevtModuleRt_Sic_2fxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_2fxo = _Hh3cevtModuleRt_Sic_2fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 50)
)
_Hh3cevtModuleRt_Fcm6_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fcm6 = _Hh3cevtModuleRt_Fcm6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 51)
)
_Hh3cevtModuleRt_Sa8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sa8 = _Hh3cevtModuleRt_Sa8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 52)
)
_Hh3cevtModuleRt_T11_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T11 = _Hh3cevtModuleRt_T11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 53)
)
_Hh3cevtModuleRt_T12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T12 = _Hh3cevtModuleRt_T12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 54)
)
_Hh3cevtModuleRt_T14_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T14 = _Hh3cevtModuleRt_T14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 55)
)
_Hh3cevtModuleRt_T1vi_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T1vi = _Hh3cevtModuleRt_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 56)
)
_Hh3cevtModuleRt_Fcm4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fcm4 = _Hh3cevtModuleRt_Fcm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 57)
)
_Hh3cevtModuleRt_Fcm2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fcm2 = _Hh3cevtModuleRt_Fcm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 58)
)
_Hh3cevtModuleRt_Rtb21ce3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Rtb21ce3 = _Hh3cevtModuleRt_Rtb21ce3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 59)
)
_Hh3cevtModuleRt_Ame6_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ame6 = _Hh3cevtModuleRt_Ame6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 60)
)
_Hh3cevtModuleRt_Ame12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ame12 = _Hh3cevtModuleRt_Ame12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 61)
)
_Hh3cevtModuleRt_E11_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E11_f = _Hh3cevtModuleRt_E11_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 65)
)
_Hh3cevtModuleRt_E12_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E12_f = _Hh3cevtModuleRt_E12_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 66)
)
_Hh3cevtModuleRt_E14_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E14_f = _Hh3cevtModuleRt_E14_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 67)
)
_Hh3cevtModuleRt_T11_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T11_f = _Hh3cevtModuleRt_T11_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 68)
)
_Hh3cevtModuleRt_T12_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T12_f = _Hh3cevtModuleRt_T12_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 69)
)
_Hh3cevtModuleRt_T14_f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T14_f = _Hh3cevtModuleRt_T14_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 70)
)
_Hh3cevtModuleRt_E11_f_17_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_E11_f_17 = _Hh3cevtModuleRt_E11_f_17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 71)
)
_Hh3cevtModuleRt_T11_f_17_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T11_f_17 = _Hh3cevtModuleRt_T11_f_17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 72)
)
_Hh3cevtModuleRt_Rtb21ct3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Rtb21ct3 = _Hh3cevtModuleRt_Rtb21ct3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 73)
)
_Hh3cevtModuleRt_Atmadsl1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmadsl1 = _Hh3cevtModuleRt_Atmadsl1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 74)
)
_Hh3cevtModuleRt_Atmadsl2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmadsl2 = _Hh3cevtModuleRt_Atmadsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 75)
)
_Hh3cevtModuleRt_Atm155m_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm155m = _Hh3cevtModuleRt_Atm155m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 76)
)
_Hh3cevtModuleRt_Ase8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ase8 = _Hh3cevtModuleRt_Ase8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 77)
)
_Hh3cevtModuleRt_Ase16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ase16 = _Hh3cevtModuleRt_Ase16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 78)
)
_Hh3cevtModuleRt_Sae4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sae4 = _Hh3cevtModuleRt_Sae4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 79)
)
_Hh3cevtModuleRt_Sae2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sae2 = _Hh3cevtModuleRt_Sae2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 80)
)
_Hh3cevtModuleRt_Atmshdsl1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmshdsl1 = _Hh3cevtModuleRt_Atmshdsl1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 90)
)
_Hh3cevtModuleRt_Atmshdsl2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmshdsl2 = _Hh3cevtModuleRt_Atmshdsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 91)
)
_Hh3cevtModuleRt_Atmshdsl4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmshdsl4 = _Hh3cevtModuleRt_Atmshdsl4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 92)
)
_Hh3cevtModuleRt_Atm25m_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm25m = _Hh3cevtModuleRt_Atm25m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 93)
)
_Hh3cevtModuleRt_Atme3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atme3 = _Hh3cevtModuleRt_Atme3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 94)
)
_Hh3cevtModuleRt_Atmt3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atmt3 = _Hh3cevtModuleRt_Atmt3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 95)
)
_Hh3cevtModuleRt_Xdsl_fec_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_fec = _Hh3cevtModuleRt_Xdsl_fec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 96)
)
_Hh3cevtModuleRt_Xdsl_adsl_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_adsl = _Hh3cevtModuleRt_Xdsl_adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 97)
)
_Hh3cevtModuleRt_Xdsl_gshdsl_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_gshdsl = _Hh3cevtModuleRt_Xdsl_gshdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 98)
)
_Hh3cevtModuleRt_Xdsl_bri_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_bri = _Hh3cevtModuleRt_Xdsl_bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 99)
)
_Hh3cevtModuleRt_Xdsl_scc_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Xdsl_scc = _Hh3cevtModuleRt_Xdsl_scc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 100)
)
_Hh3cevtModuleRt_Ge1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ge1 = _Hh3cevtModuleRt_Ge1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 101)
)
_Hh3cevtModuleRt_Pos155m_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Pos155m = _Hh3cevtModuleRt_Pos155m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 102)
)
_Hh3cevtModuleRt_Cpos_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Cpos = _Hh3cevtModuleRt_Cpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 103)
)
_Hh3cevtModuleRt_Fe1op_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe1op = _Hh3cevtModuleRt_Fe1op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 104)
)
_Hh3cevtModuleRt_Sae8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sae8 = _Hh3cevtModuleRt_Sae8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 105)
)
_Hh3cevtModuleRt_Atm155m_mm_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm155m_mm = _Hh3cevtModuleRt_Atm155m_mm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 106)
)
_Hh3cevtModuleRt_Atm155m_sm_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm155m_sm = _Hh3cevtModuleRt_Atm155m_sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 107)
)
_Hh3cevtModuleRt_Atm155m_sml_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Atm155m_sml = _Hh3cevtModuleRt_Atm155m_sml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 108)
)
_Hh3cevtModuleRt_Fe1op_sfx_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe1op_sfx = _Hh3cevtModuleRt_Fe1op_sfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 109)
)
_Hh3cevtModuleRt_Fe1op_mfx_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe1op_mfx = _Hh3cevtModuleRt_Fe1op_mfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 110)
)
_Hh3cevtModuleRt_Cpos_t1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Cpos_t1 = _Hh3cevtModuleRt_Cpos_t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 111)
)
_Hh3cevtModuleRt_Ge1op_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ge1op = _Hh3cevtModuleRt_Ge1op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 112)
)
_Hh3cevtModuleRt_Ge2op_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ge2op = _Hh3cevtModuleRt_Ge2op_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 113)
)
_Hh3cevtModuleRt_Ge2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Ge2 = _Hh3cevtModuleRt_Ge2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 114)
)
_Hh3cevtModuleRt_Fix_1wan_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fix_1wan = _Hh3cevtModuleRt_Fix_1wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 115)
)
_Hh3cevtModuleRt_Fix_1sae_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fix_1sae = _Hh3cevtModuleRt_Fix_1sae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 116)
)
_Hh3cevtModuleRt_Cavium_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Cavium = _Hh3cevtModuleRt_Cavium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 117)
)
_Hh3cevtModuleRt_Sic1Eth_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic1Eth = _Hh3cevtModuleRt_Sic1Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 118)
)
_Hh3cevtModuleRt_atm1ADSLI_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_atm1ADSLI = _Hh3cevtModuleRt_atm1ADSLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 119)
)
_Hh3cevtModuleRt_atm2ADSLI_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_atm2ADSLI = _Hh3cevtModuleRt_atm2ADSLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 120)
)
_Hh3cevtModuleRt_fix_e11_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fix_e11 = _Hh3cevtModuleRt_fix_e11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 121)
)
_Hh3cevtModuleRt_fix_t11_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fix_t11 = _Hh3cevtModuleRt_fix_t11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 122)
)
_Hh3cevtModuleRt_e18_75_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_e18_75 = _Hh3cevtModuleRt_e18_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 123)
)
_Hh3cevtModuleRt_e18_120_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_e18_120 = _Hh3cevtModuleRt_e18_120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 124)
)
_Hh3cevtModuleRt_t18_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_t18 = _Hh3cevtModuleRt_t18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 125)
)
_Hh3cevtModuleRt_sic_1vifxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_1vifxs = _Hh3cevtModuleRt_sic_1vifxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 126)
)
_Hh3cevtModuleRt_sic_1vifxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_1vifxo = _Hh3cevtModuleRt_sic_1vifxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 127)
)
_Hh3cevtModuleRt_sic_2vifxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_2vifxs = _Hh3cevtModuleRt_sic_2vifxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 128)
)
_Hh3cevtModuleRt_sic_2vifxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_2vifxo = _Hh3cevtModuleRt_sic_2vifxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 129)
)
_Hh3cevtModuleRt_xdsl_fec_new_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_xdsl_fec_new = _Hh3cevtModuleRt_xdsl_fec_new_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 130)
)
_Hh3cevtModuleRt_xdsl_sa_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_xdsl_sa = _Hh3cevtModuleRt_xdsl_sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 131)
)
_Hh3cevtModuleRt_bs4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_bs4 = _Hh3cevtModuleRt_bs4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 132)
)
_Hh3cevtModuleRt_ima_8e175_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_8e175 = _Hh3cevtModuleRt_ima_8e175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 133)
)
_Hh3cevtModuleRt_ima_8e1120_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_8e1120 = _Hh3cevtModuleRt_ima_8e1120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 134)
)
_Hh3cevtModuleRt_ima_4e175_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_4e175 = _Hh3cevtModuleRt_ima_4e175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 135)
)
_Hh3cevtModuleRt_ima_4e1120_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_4e1120 = _Hh3cevtModuleRt_ima_4e1120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 136)
)
_Hh3cevtModuleRt_ima_8t1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_8t1 = _Hh3cevtModuleRt_ima_8t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 137)
)
_Hh3cevtModuleRt_ima_4t1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ima_4t1 = _Hh3cevtModuleRt_ima_4t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 138)
)
_Hh3cevtModuleRt_sic_1t1f_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_1t1f = _Hh3cevtModuleRt_sic_1t1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 139)
)
_Hh3cevtModuleRT_SIC_1E1F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1E1F = _Hh3cevtModuleRT_SIC_1E1F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 140)
)
_Hh3cevtModuleRt_VG_16fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_16fxs = _Hh3cevtModuleRt_VG_16fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 141)
)
_Hh3cevtModuleRt_VG_32fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_32fxs = _Hh3cevtModuleRt_VG_32fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 142)
)
_Hh3cevtModuleRt_VG_8fxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_8fxo = _Hh3cevtModuleRt_VG_8fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 143)
)
_Hh3cevtModuleRt_VG_2fe_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_2fe = _Hh3cevtModuleRt_VG_2fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 144)
)
_Hh3cevtModuleRt_sib_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sib = _Hh3cevtModuleRt_sib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 145)
)
_Hh3cevtModuleRt_cie32_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cie32 = _Hh3cevtModuleRt_cie32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 146)
)
_Hh3cevtModuleRt_cie64_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cie64 = _Hh3cevtModuleRt_cie64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 147)
)
_Hh3cevtModuleRt_cie96_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cie96 = _Hh3cevtModuleRt_cie96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 148)
)
_Hh3cevtModuleRt_Fe4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Fe4 = _Hh3cevtModuleRt_Fe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 149)
)
_Hh3cevtModuleRt_fxs4fxo1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fxs4fxo1 = _Hh3cevtModuleRt_fxs4fxo1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 150)
)
_Hh3cevtModuleRt_atm1shdsl4wire_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_atm1shdsl4wire = _Hh3cevtModuleRt_atm1shdsl4wire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 151)
)
_Hh3cevtModuleRt_atmIma4shdsl_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_atmIma4shdsl = _Hh3cevtModuleRt_atmIma4shdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 152)
)
_Hh3cevtModuleRt_ls4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ls4 = _Hh3cevtModuleRt_ls4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 153)
)
_Hh3cevtModuleRt_ls8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ls8 = _Hh3cevtModuleRt_ls8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 154)
)
_Hh3cevtModuleRt_ls16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ls16 = _Hh3cevtModuleRt_ls16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 155)
)
_Hh3cevtModuleRt_sic_adls2plus_isdn_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_adls2plus_isdn = _Hh3cevtModuleRt_sic_adls2plus_isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 156)
)
_Hh3cevtModuleRt_sic_adls2plus_pots_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sic_adls2plus_pots = _Hh3cevtModuleRt_sic_adls2plus_pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 157)
)
_Hh3cevtModuleRt_ft3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ft3 = _Hh3cevtModuleRt_ft3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 158)
)
_Hh3cevtModuleRt_ce32_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ce32 = _Hh3cevtModuleRt_ce32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 159)
)
_Hh3cevtModuleRt_bsv2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_bsv2 = _Hh3cevtModuleRt_bsv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 160)
)
_Hh3cevtModuleRt_bsv4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_bsv4 = _Hh3cevtModuleRt_bsv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 161)
)
_Hh3cevtModuleRt_RPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RPU = _Hh3cevtModuleRt_RPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 162)
)
_Hh3cevtModuleRt_ERPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ERPU = _Hh3cevtModuleRt_ERPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 163)
)
_Hh3cevtModuleRt_SSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SSL = _Hh3cevtModuleRt_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 164)
)
_Hh3cevtModuleRt_NSA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSA = _Hh3cevtModuleRt_NSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 165)
)
_Hh3cevtModuleRT_SIC_1GEC_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1GEC = _Hh3cevtModuleRT_SIC_1GEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 200)
)
_Hh3cevtModuleRT_24FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_24FSW = _Hh3cevtModuleRT_24FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 201)
)
_Hh3cevtModuleRT_24FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_24FSWP = _Hh3cevtModuleRT_24FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 202)
)
_Hh3cevtModuleRT_16FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_16FSW = _Hh3cevtModuleRT_16FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 203)
)
_Hh3cevtModuleRT_16FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_16FSWP = _Hh3cevtModuleRT_16FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 204)
)
_Hh3cevtModuleRT_1VE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1VE1 = _Hh3cevtModuleRT_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 205)
)
_Hh3cevtModuleRT_1VT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1VT1 = _Hh3cevtModuleRT_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 206)
)
_Hh3cevtModuleRT_2VE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_2VE1 = _Hh3cevtModuleRT_2VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 207)
)
_Hh3cevtModuleRT_2VT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_2VT1 = _Hh3cevtModuleRT_2VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 208)
)
_Hh3cevtModuleRT_SIC_4FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_4FSW = _Hh3cevtModuleRT_SIC_4FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 209)
)
_Hh3cevtModuleRT_SIC_4FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_4FSWP = _Hh3cevtModuleRT_SIC_4FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 210)
)
_Hh3cevtModuleRT_DSIC_9FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_DSIC_9FSW = _Hh3cevtModuleRT_DSIC_9FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 211)
)
_Hh3cevtModuleRT_DSIC_9FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_DSIC_9FSWP = _Hh3cevtModuleRT_DSIC_9FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 212)
)
_Hh3cevtModuleRT_SIC_1VE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1VE1 = _Hh3cevtModuleRT_SIC_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 213)
)
_Hh3cevtModuleRT_SIC_1VT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1VT1 = _Hh3cevtModuleRT_SIC_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 214)
)
_Hh3cevtModuleRT_VCPM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VCPM = _Hh3cevtModuleRT_VCPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 215)
)
_Hh3cevtModuleRT_VPM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VPM = _Hh3cevtModuleRT_VPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 216)
)
_Hh3cevtModuleRT_VPMA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VPMA = _Hh3cevtModuleRT_VPMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 217)
)
_Hh3cevtModuleRT_VPMB_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VPMB = _Hh3cevtModuleRT_VPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 218)
)
_Hh3cevtModuleRT_VPMC_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VPMC = _Hh3cevtModuleRT_VPMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 219)
)
_Hh3cevtModuleRt_fe18_75_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fe18_75 = _Hh3cevtModuleRt_fe18_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 220)
)
_Hh3cevtModuleRt_fe18_120_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_fe18_120 = _Hh3cevtModuleRt_fe18_120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 221)
)
_Hh3cevtModuleRt_ft18_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ft18 = _Hh3cevtModuleRt_ft18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 222)
)
_Hh3cevtModuleRt_CF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CF = _Hh3cevtModuleRt_CF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 223)
)
_Hh3cevtModuleRt_bsv2_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_bsv2_v2 = _Hh3cevtModuleRt_bsv2_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 224)
)
_Hh3cevtModuleRt_e1vi1_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_e1vi1_v2 = _Hh3cevtModuleRt_e1vi1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 225)
)
_Hh3cevtModuleRt_e1vi2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_e1vi2 = _Hh3cevtModuleRt_e1vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 226)
)
_Hh3cevtModuleRt_t1vi1_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_t1vi1_v2 = _Hh3cevtModuleRt_t1vi1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 227)
)
_Hh3cevtModuleRt_t1vi2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_t1vi2 = _Hh3cevtModuleRt_t1vi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 228)
)
_Hh3cevtModuleRt_osm_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_osm = _Hh3cevtModuleRt_osm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 229)
)
_Hh3cevtModuleRt_sd707_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_sd707 = _Hh3cevtModuleRt_sd707_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 230)
)
_Hh3cevtModuleRt_dm_epri_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_dm_epri = _Hh3cevtModuleRt_dm_epri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 231)
)
_Hh3cevtModuleRt_dm_tpri_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_dm_tpri = _Hh3cevtModuleRt_dm_tpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 232)
)
_Hh3cevtModuleRt_ERPU_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ERPU_H = _Hh3cevtModuleRt_ERPU_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 233)
)
_Hh3cevtModuleRT_SIC_1BSV_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1BSV = _Hh3cevtModuleRT_SIC_1BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 234)
)
_Hh3cevtModuleRT_SIC_2BSV_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_2BSV = _Hh3cevtModuleRT_SIC_2BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 235)
)
_Hh3cevtModuleRt_gbe8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_gbe8 = _Hh3cevtModuleRt_gbe8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 236)
)
_Hh3cevtModuleRt_gbe4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_gbe4 = _Hh3cevtModuleRt_gbe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 237)
)
_Hh3cevtModuleRt_cpos2_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cpos2_v2 = _Hh3cevtModuleRt_cpos2_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 238)
)
_Hh3cevtModuleRt_cpos1_v2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_cpos1_v2 = _Hh3cevtModuleRt_cpos1_v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 239)
)
_Hh3cevtModuleRt_oap_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_oap = _Hh3cevtModuleRt_oap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 240)
)
_Hh3cevtModuleRT_48FSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_48FSWP = _Hh3cevtModuleRT_48FSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 241)
)
_Hh3cevtModuleRT_48FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_48FSW = _Hh3cevtModuleRT_48FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 242)
)
_Hh3cevtModuleRT_ASM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_ASM = _Hh3cevtModuleRT_ASM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 243)
)
_Hh3cevtModuleRT_SIC_1FEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1FEF = _Hh3cevtModuleRT_SIC_1FEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 244)
)
_Hh3cevtModuleRT_XMIM_24FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_XMIM_24FSW = _Hh3cevtModuleRT_XMIM_24FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 245)
)
_Hh3cevtModuleRT_WLAN_AG_1RADIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_WLAN_AG_1RADIO = _Hh3cevtModuleRT_WLAN_AG_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 246)
)
_Hh3cevtModuleRT_1CE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1CE3 = _Hh3cevtModuleRT_1CE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 247)
)
_Hh3cevtModuleRT_XMIM_16FSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_XMIM_16FSW = _Hh3cevtModuleRT_XMIM_16FSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 248)
)
_Hh3cevtModuleRT_OAPS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAPS = _Hh3cevtModuleRT_OAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 249)
)
_Hh3cevtModuleRT_NAM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_NAM = _Hh3cevtModuleRT_NAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 250)
)
_Hh3cevtModuleRT_RPE_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_RPE_X1 = _Hh3cevtModuleRT_RPE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 251)
)
_Hh3cevtModuleRT_FIP_100_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_FIP_100 = _Hh3cevtModuleRT_FIP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 252)
)
_Hh3cevtModuleRT_FIP_200_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_FIP_200 = _Hh3cevtModuleRT_FIP_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 253)
)
_Hh3cevtModuleRT_SIC_8AS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_8AS = _Hh3cevtModuleRT_SIC_8AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 254)
)
_Hh3cevtModuleRT_WAAM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_WAAM = _Hh3cevtModuleRT_WAAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 255)
)
_Hh3cevtModuleRt_msp4p_OC3c_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_msp4p_OC3c = _Hh3cevtModuleRt_msp4p_OC3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 256)
)
_Hh3cevtModuleRt_1pos_oc48_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_1pos_oc48 = _Hh3cevtModuleRt_1pos_oc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 257)
)
_Hh3cevtModuleRt_xgbe_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_xgbe = _Hh3cevtModuleRt_xgbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 258)
)
_Hh3cevtModuleRT_EADM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_EADM = _Hh3cevtModuleRT_EADM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 259)
)
_Hh3cevtModuleRT_VCM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_VCM = _Hh3cevtModuleRT_VCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 260)
)
_Hh3cevtModuleRT_SIC_2FXS1FXO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_2FXS1FXO = _Hh3cevtModuleRT_SIC_2FXS1FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 261)
)
_Hh3cevtModuleRT_8FXS8FXO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_8FXS8FXO = _Hh3cevtModuleRT_8FXS8FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 262)
)
_Hh3cevtModuleRT_16FXS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_16FXS = _Hh3cevtModuleRT_16FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 263)
)
_Hh3cevtModuleRT_OAPS_ICM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAPS_ICM = _Hh3cevtModuleRT_OAPS_ICM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 264)
)
_Hh3cevtModuleRT_OAP_ICM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAP_ICM = _Hh3cevtModuleRT_OAP_ICM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 265)
)
_Hh3cevtModuleRT_8fe_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_8fe = _Hh3cevtModuleRT_8fe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 266)
)
_Hh3cevtModuleRT_4gbp_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_4gbp = _Hh3cevtModuleRT_4gbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 267)
)
_Hh3cevtModuleRT_MPU_G2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MPU_G2 = _Hh3cevtModuleRT_MPU_G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 268)
)
_Hh3cevtModuleRT_OAPS_OCE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAPS_OCE = _Hh3cevtModuleRT_OAPS_OCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 269)
)
_Hh3cevtModuleRT_OAP_OCE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAP_OCE = _Hh3cevtModuleRT_OAP_OCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 270)
)
_Hh3cevtModuleRT_OAPS_ICE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAPS_ICE = _Hh3cevtModuleRT_OAPS_ICE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 271)
)
_Hh3cevtModuleRT_OAP_ICE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_OAP_ICE = _Hh3cevtModuleRT_OAP_ICE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 272)
)
_Hh3cevtModuleRT_SIC_16AS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_16AS = _Hh3cevtModuleRT_SIC_16AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 273)
)
_Hh3cevtModuleRT_SPE_FWM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SPE_FWM = _Hh3cevtModuleRT_SPE_FWM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 274)
)
_Hh3cevtModuleRT_cls2p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_cls2p = _Hh3cevtModuleRT_cls2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 275)
)
_Hh3cevtModuleRT_cls1p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_cls1p = _Hh3cevtModuleRT_cls1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 276)
)
_Hh3cevtModuleRT_SIC_2E1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_2E1_F = _Hh3cevtModuleRT_SIC_2E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 277)
)
_Hh3cevtModuleRT_SIC_1E1_F_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_1E1_F_V2 = _Hh3cevtModuleRT_SIC_1E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 278)
)
_Hh3cevtModuleRT_MCU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MCU = _Hh3cevtModuleRT_MCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 279)
)
_Hh3cevtModuleRT_ACU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_ACU = _Hh3cevtModuleRT_ACU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 280)
)
_Hh3cevtModuleRT_1ATM_OC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1ATM_OC3 = _Hh3cevtModuleRT_1ATM_OC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 281)
)
_Hh3cevtModuleRT_RSE_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_RSE_X1 = _Hh3cevtModuleRT_RSE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 282)
)
_Hh3cevtModuleRT_FIP_210_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_FIP_210 = _Hh3cevtModuleRT_FIP_210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 283)
)
_Hh3cevtModuleRT_1expa_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_1expa = _Hh3cevtModuleRT_1expa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 284)
)
_Hh3cevtModuleRT_WLAN_SIC_N_1RADIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_WLAN_SIC_N_1RADIO = _Hh3cevtModuleRT_WLAN_SIC_N_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 285)
)
_Hh3cevtModuleRT_WLAN_SIC_BG_1RADIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_WLAN_SIC_BG_1RADIO = _Hh3cevtModuleRT_WLAN_SIC_BG_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 286)
)
_Hh3cevtModuleRT_al2p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_al2p = _Hh3cevtModuleRT_al2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 287)
)
_Hh3cevtModuleRT_msp2p_OC3c_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_msp2p_OC3c = _Hh3cevtModuleRT_msp2p_OC3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 288)
)
_Hh3cevtModuleRT_8gbp_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_8gbp = _Hh3cevtModuleRT_8gbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 289)
)
_Hh3cevtModuleRT_SIC_EPON_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_EPON = _Hh3cevtModuleRT_SIC_EPON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 290)
)
_Hh3cevtModuleRT_SIC_3G_GSM_H3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_3G_GSM_H3 = _Hh3cevtModuleRT_SIC_3G_GSM_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 291)
)
_Hh3cevtModuleRT_msp2p_OC12c_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_msp2p_OC12c = _Hh3cevtModuleRT_msp2p_OC12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 292)
)
_Hh3cevtModuleRt_msp4p_OC12c_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_msp4p_OC12c = _Hh3cevtModuleRt_msp4p_OC12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 293)
)
_Hh3cevtModuleRt_al1p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_al1p = _Hh3cevtModuleRt_al1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 294)
)
_Hh3cevtModuleRt_OAP_100_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_OAP_100 = _Hh3cevtModuleRt_OAP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 295)
)
_Hh3cevtModuleRt_FIP_110_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_110 = _Hh3cevtModuleRt_FIP_110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 296)
)
_Hh3cevtModuleRt_OSM_SSM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_OSM_SSM = _Hh3cevtModuleRt_OSM_SSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 297)
)
_Hh3cevtModuleRt_OAP_SSM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_OAP_SSM = _Hh3cevtModuleRt_OAP_SSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 298)
)
_Hh3cevtModuleRt_rs2p_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_rs2p = _Hh3cevtModuleRt_rs2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 299)
)
_Hh3cevtModuleRt_SAP_48GBE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_48GBE = _Hh3cevtModuleRt_SAP_48GBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 300)
)
_Hh3cevtModuleRt_SAP_48GBP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_48GBP = _Hh3cevtModuleRt_SAP_48GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 301)
)
_Hh3cevtModuleRt_SAP_24GBP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_24GBP = _Hh3cevtModuleRt_SAP_24GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 302)
)
_Hh3cevtModuleRt_SPE_SSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPE_SSL = _Hh3cevtModuleRt_SPE_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 303)
)
_Hh3cevtModuleRt_SIC_AUDIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_AUDIO = _Hh3cevtModuleRt_SIC_AUDIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 304)
)
_Hh3cevtModuleRt_FIC_1E1POS_H3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIC_1E1POS_H3 = _Hh3cevtModuleRt_FIC_1E1POS_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 305)
)
_Hh3cevtModuleRt_DSIC_4FXS1FXO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_DSIC_4FXS1FXO = _Hh3cevtModuleRt_DSIC_4FXS1FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 306)
)
_Hh3cevtModuleRt_FIC_CPOS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIC_CPOS = _Hh3cevtModuleRt_FIC_CPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 307)
)
_Hh3cevtModuleRt_DSIC_1SHDSL_8W_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_DSIC_1SHDSL_8W = _Hh3cevtModuleRt_DSIC_1SHDSL_8W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 308)
)
_Hh3cevtModuleRt_SIC_3G_TD_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_3G_TD = _Hh3cevtModuleRt_SIC_3G_TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 309)
)
_Hh3cevtModuleRt_SIC_3G_CDMA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_3G_CDMA = _Hh3cevtModuleRt_SIC_3G_CDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 310)
)
_Hh3cevtModuleRt_SIC_3G_HSPA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_3G_HSPA = _Hh3cevtModuleRt_SIC_3G_HSPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 311)
)
_Hh3cevtModuleRt_FIC_OAP_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIC_OAP_V2 = _Hh3cevtModuleRt_FIC_OAP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 312)
)
_Hh3cevtModuleRt_MIM_OAP_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_OAP_V2 = _Hh3cevtModuleRt_MIM_OAP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 313)
)
_Hh3cevtModuleRt_MIM_OAPS_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_OAPS_V2 = _Hh3cevtModuleRt_MIM_OAPS_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 314)
)
_Hh3cevtModuleRt_HMIM_1CT3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1CT3 = _Hh3cevtModuleRt_HMIM_1CT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 315)
)
_Hh3cevtModuleRt_HMIM_1CE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1CE3 = _Hh3cevtModuleRt_HMIM_1CE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 316)
)
_Hh3cevtModuleRt_HMIM_1POS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1POS = _Hh3cevtModuleRt_HMIM_1POS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 317)
)
_Hh3cevtModuleRt_HMIM_2SAE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2SAE = _Hh3cevtModuleRt_HMIM_2SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 318)
)
_Hh3cevtModuleRt_HMIM_4SAE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4SAE = _Hh3cevtModuleRt_HMIM_4SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 319)
)
_Hh3cevtModuleRt_HMIM_8SAE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8SAE = _Hh3cevtModuleRt_HMIM_8SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 320)
)
_Hh3cevtModuleRt_HMIM_8ASE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8ASE = _Hh3cevtModuleRt_HMIM_8ASE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 321)
)
_Hh3cevtModuleRt_HMIM_16ASE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_16ASE = _Hh3cevtModuleRt_HMIM_16ASE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 322)
)
_Hh3cevtModuleRt_HMIM_1E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1E1 = _Hh3cevtModuleRt_HMIM_1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 323)
)
_Hh3cevtModuleRt_HMIM_2E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2E1 = _Hh3cevtModuleRt_HMIM_2E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 324)
)
_Hh3cevtModuleRt_HMIM_4E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4E1 = _Hh3cevtModuleRt_HMIM_4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 325)
)
_Hh3cevtModuleRt_HMIM_8E1_75_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8E1_75 = _Hh3cevtModuleRt_HMIM_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 326)
)
_Hh3cevtModuleRt_HMIM_1E1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1E1_F = _Hh3cevtModuleRt_HMIM_1E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 327)
)
_Hh3cevtModuleRt_HMIM_2E1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2E1_F = _Hh3cevtModuleRt_HMIM_2E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 328)
)
_Hh3cevtModuleRt_HMIM_4E1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4E1_F = _Hh3cevtModuleRt_HMIM_4E1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 329)
)
_Hh3cevtModuleRt_HMIM_8E1_F_75_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8E1_F_75 = _Hh3cevtModuleRt_HMIM_8E1_F_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 330)
)
_Hh3cevtModuleRt_HMIM_6AM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_6AM = _Hh3cevtModuleRt_HMIM_6AM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 331)
)
_Hh3cevtModuleRt_HMIM_6FCM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_6FCM = _Hh3cevtModuleRt_HMIM_6FCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 332)
)
_Hh3cevtModuleRt_HMIM_2T1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2T1 = _Hh3cevtModuleRt_HMIM_2T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 333)
)
_Hh3cevtModuleRt_HMIM_4T1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4T1_F = _Hh3cevtModuleRt_HMIM_4T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 334)
)
_Hh3cevtModuleRt_HMIM_8T1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8T1 = _Hh3cevtModuleRt_HMIM_8T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 335)
)
_Hh3cevtModuleRt_HMIM_8T1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8T1_F = _Hh3cevtModuleRt_HMIM_8T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 336)
)
_Hh3cevtModuleRt_HMIM_1VE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1VE1 = _Hh3cevtModuleRt_HMIM_1VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 337)
)
_Hh3cevtModuleRt_HMIM_1VT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1VT1 = _Hh3cevtModuleRt_HMIM_1VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 338)
)
_Hh3cevtModuleRt_HMIM_2VE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2VE1 = _Hh3cevtModuleRt_HMIM_2VE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 339)
)
_Hh3cevtModuleRt_HMIM_2VT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2VT1 = _Hh3cevtModuleRt_HMIM_2VT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 340)
)
_Hh3cevtModuleRt_HMIM_8FXS8FXO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8FXS8FXO = _Hh3cevtModuleRt_HMIM_8FXS8FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 341)
)
_Hh3cevtModuleRt_HMIM_16FXS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_16FXS = _Hh3cevtModuleRt_HMIM_16FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 342)
)
_Hh3cevtModuleRt_HMIM_4FXS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4FXS = _Hh3cevtModuleRt_HMIM_4FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 343)
)
_Hh3cevtModuleRt_HMIM_4FXO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4FXO = _Hh3cevtModuleRt_HMIM_4FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 344)
)
_Hh3cevtModuleRt_HMIM_4EM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4EM = _Hh3cevtModuleRt_HMIM_4EM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 345)
)
_Hh3cevtModuleRt_HMIM_4BSV_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4BSV = _Hh3cevtModuleRt_HMIM_4BSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 346)
)
_Hh3cevtModuleRt_SIC_CNDE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_CNDE = _Hh3cevtModuleRt_SIC_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 347)
)
_Hh3cevtModuleRt_ESM_CNDE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ESM_CNDE = _Hh3cevtModuleRt_ESM_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 348)
)
_Hh3cevtModuleRt_ESM_CNDE_M_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ESM_CNDE_M = _Hh3cevtModuleRt_ESM_CNDE_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 349)
)
_Hh3cevtModuleRt_SR6602_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SR6602_X1 = _Hh3cevtModuleRt_SR6602_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 350)
)
_Hh3cevtModuleRt_SR6602_X2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SR6602_X2 = _Hh3cevtModuleRt_SR6602_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 351)
)
_Hh3cevtModuleRt_MCP_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MCP_X1 = _Hh3cevtModuleRt_MCP_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 352)
)
_Hh3cevtModuleRt_MCP_X2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MCP_X2 = _Hh3cevtModuleRt_MCP_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 353)
)
_Hh3cevtModuleRt_FIP_10_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_10 = _Hh3cevtModuleRt_FIP_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 354)
)
_Hh3cevtModuleRt_FIP_20_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_20 = _Hh3cevtModuleRt_FIP_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 355)
)
_Hh3cevtModuleRt_RSE_X2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RSE_X2 = _Hh3cevtModuleRt_RSE_X2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 356)
)
_Hh3cevtModuleRt_FIP_600_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_600 = _Hh3cevtModuleRt_FIP_600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 357)
)
_Hh3cevtModuleRt_SAP_4EXP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_4EXP = _Hh3cevtModuleRt_SAP_4EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 358)
)
_Hh3cevtModuleRt_SFE_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SFE_X1 = _Hh3cevtModuleRt_SFE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 359)
)
_Hh3cevtModuleRt_SFE_A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SFE_A1 = _Hh3cevtModuleRt_SFE_A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 360)
)
_Hh3cevtModuleRt_HMIM_24GSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_24GSW = _Hh3cevtModuleRt_HMIM_24GSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 361)
)
_Hh3cevtModuleRt_HMIM_24GSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_24GSWP = _Hh3cevtModuleRt_HMIM_24GSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 362)
)
_Hh3cevtModuleRt_MPU100_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MPU100 = _Hh3cevtModuleRt_MPU100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 363)
)
_Hh3cevtModuleRt_SPU100_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU100 = _Hh3cevtModuleRt_SPU100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 364)
)
_Hh3cevtModuleRt_SPU200_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU200 = _Hh3cevtModuleRt_SPU200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 365)
)
_Hh3cevtModuleRt_WLAN_N_1RADIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_WLAN_N_1RADIO = _Hh3cevtModuleRt_WLAN_N_1RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 366)
)
_Hh3cevtModuleRt_3G_CDMA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_3G_CDMA = _Hh3cevtModuleRt_3G_CDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 367)
)
_Hh3cevtModuleRt_3G_WCDMA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_3G_WCDMA = _Hh3cevtModuleRt_3G_WCDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 368)
)
_Hh3cevtModuleRt_3G_HSPAPLUS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_3G_HSPAPLUS = _Hh3cevtModuleRt_3G_HSPAPLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 369)
)
_Hh3cevtModuleRt_VPM_128_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VPM_128 = _Hh3cevtModuleRt_VPM_128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 370)
)
_Hh3cevtModuleRt_VPM_256_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VPM_256 = _Hh3cevtModuleRt_VPM_256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 371)
)
_Hh3cevtModuleRt_VPM_512_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VPM_512 = _Hh3cevtModuleRt_VPM_512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 372)
)
_Hh3cevtModuleRt_HMIM_8GEE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8GEE = _Hh3cevtModuleRt_HMIM_8GEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 373)
)
_Hh3cevtModuleRt_HMIM_4GEE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4GEE = _Hh3cevtModuleRt_HMIM_4GEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 374)
)
_Hh3cevtModuleRt_HMIM_2GEE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2GEE = _Hh3cevtModuleRt_HMIM_2GEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 375)
)
_Hh3cevtModuleRt_HMIM_8GEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8GEF = _Hh3cevtModuleRt_HMIM_8GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 376)
)
_Hh3cevtModuleRt_HMIM_4GEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4GEF = _Hh3cevtModuleRt_HMIM_4GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 377)
)
_Hh3cevtModuleRt_HMIM_2GEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2GEF = _Hh3cevtModuleRt_HMIM_2GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 378)
)
_Hh3cevtModuleRt_SPU300_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU300 = _Hh3cevtModuleRt_SPU300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 379)
)
_Hh3cevtModuleRt_HMIM_1CPOS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1CPOS = _Hh3cevtModuleRt_HMIM_1CPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 380)
)
_Hh3cevtModuleRt_HMIM_2CPOS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2CPOS = _Hh3cevtModuleRt_HMIM_2CPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 381)
)
_Hh3cevtModuleRt_SPU100_5080_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU100_5080 = _Hh3cevtModuleRt_SPU100_5080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 382)
)
_Hh3cevtModuleRt_SPU200_5080_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU200_5080 = _Hh3cevtModuleRt_SPU200_5080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 383)
)
_Hh3cevtModuleRt_SPU300_5080_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU300_5080 = _Hh3cevtModuleRt_SPU300_5080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 384)
)
_Hh3cevtModuleRt_4G_LTE_Verizon_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_4G_LTE_Verizon = _Hh3cevtModuleRt_4G_LTE_Verizon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 385)
)
_Hh3cevtModuleRt_4G_LTE_Global_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_4G_LTE_Global = _Hh3cevtModuleRt_4G_LTE_Global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 386)
)
_Hh3cevtModuleRt_HMIM_1ATM_OC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1ATM_OC3 = _Hh3cevtModuleRt_HMIM_1ATM_OC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 387)
)
_Hh3cevtModuleRt_SIC_1E1_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_1E1_V2 = _Hh3cevtModuleRt_SIC_1E1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 388)
)
_Hh3cevtModuleRt_FIP_300_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_300 = _Hh3cevtModuleRt_FIP_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 389)
)
_Hh3cevtModuleRt_FIP_310_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_310 = _Hh3cevtModuleRt_FIP_310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 390)
)
_Hh3cevtModuleRt_TS8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_TS8P = _Hh3cevtModuleRt_TS8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 391)
)
_Hh3cevtModuleRt_4G4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_4G4P = _Hh3cevtModuleRt_4G4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 392)
)
_Hh3cevtModuleRt_SIC_4G_LTE_V_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4G_LTE_V = _Hh3cevtModuleRt_SIC_4G_LTE_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 393)
)
_Hh3cevtModuleRt_SIC_4G_LTE_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4G_LTE_A = _Hh3cevtModuleRt_SIC_4G_LTE_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 394)
)
_Hh3cevtModuleRt_SIC_4G_LTE_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4G_LTE_G = _Hh3cevtModuleRt_SIC_4G_LTE_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 395)
)
_Hh3cevtModuleRt_SIC_2SAE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_2SAE = _Hh3cevtModuleRt_SIC_2SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 396)
)
_Hh3cevtModuleRt_SIC_4SAE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4SAE = _Hh3cevtModuleRt_SIC_4SAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 397)
)
_Hh3cevtModuleRt_HMIM_OAP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_OAP = _Hh3cevtModuleRt_HMIM_OAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 398)
)
_Hh3cevtModuleRt_HMIM_8GSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8GSW = _Hh3cevtModuleRt_HMIM_8GSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 399)
)
_Hh3cevtModuleRt_IPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IPU = _Hh3cevtModuleRt_IPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 400)
)
_Hh3cevtModuleRt_MIM2GEBE_PCIE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM2GEBE_PCIE = _Hh3cevtModuleRt_MIM2GEBE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 401)
)
_Hh3cevtModuleRt_HIM12GE_PCIE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM12GE_PCIE = _Hh3cevtModuleRt_HIM12GE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 402)
)
_Hh3cevtModuleRt_HIM2XGE_PCIE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM2XGE_PCIE = _Hh3cevtModuleRt_HIM2XGE_PCIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 403)
)
_Hh3cevtModuleRt_IPU_T1000_M_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IPU_T1000_M = _Hh3cevtModuleRt_IPU_T1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 404)
)
_Hh3cevtModuleRt_IPU_GX4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IPU_GX4C = _Hh3cevtModuleRt_IPU_GX4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 405)
)
_Hh3cevtModuleRt_IPU_GT4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IPU_GT4C = _Hh3cevtModuleRt_IPU_GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 406)
)
_Hh3cevtModuleRt_RPU_IAG2000_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RPU_IAG2000_A = _Hh3cevtModuleRt_RPU_IAG2000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 407)
)
_Hh3cevtModuleRt_RPU_AFD1000_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RPU_AFD1000_A = _Hh3cevtModuleRt_RPU_AFD1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 408)
)
_Hh3cevtModuleRt_RPU_F5000_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RPU_F5000_A = _Hh3cevtModuleRt_RPU_F5000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 409)
)
_Hh3cevtModuleRt_ACG_8800S3_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_ACG_8800S3_MPU = _Hh3cevtModuleRt_ACG_8800S3_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 410)
)
_Hh3cevtModuleRt_T5000S3_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_T5000S3_MPU = _Hh3cevtModuleRt_T5000S3_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 411)
)
_Hh3cevtModuleRt_NS21S2MSPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS21S2MSPB0 = _Hh3cevtModuleRt_NS21S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 412)
)
_Hh3cevtModuleRt_NS11S2MSPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS11S2MSPB0 = _Hh3cevtModuleRt_NS11S2MSPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 413)
)
_Hh3cevtModuleRt_NSQ1WLAN_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1WLAN = _Hh3cevtModuleRt_NSQ1WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 414)
)
_Hh3cevtModuleRt_NSQ1GP4U0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1GP4U0 = _Hh3cevtModuleRt_NSQ1GP4U0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 415)
)
_Hh3cevtModuleRt_NSQ1GP8C40_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1GP8C40 = _Hh3cevtModuleRt_NSQ1GP8C40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 416)
)
_Hh3cevtModuleRt_NSQ1XS2U0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1XS2U0 = _Hh3cevtModuleRt_NSQ1XS2U0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 417)
)
_Hh3cevtModuleRt_NSQ1G24XS60_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1G24XS60 = _Hh3cevtModuleRt_NSQ1G24XS60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 418)
)
_Hh3cevtModuleRt_NSQ1TGX4EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1TGX4EA0 = _Hh3cevtModuleRt_NSQ1TGX4EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 419)
)
_Hh3cevtModuleRt_NSQ1FAB08D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1FAB08D0 = _Hh3cevtModuleRt_NSQ1FAB08D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 420)
)
_Hh3cevtModuleRt_NSQ1TGS32SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1TGS32SF0 = _Hh3cevtModuleRt_NSQ1TGS32SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 421)
)
_Hh3cevtModuleRt_NSQ1QGS4SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1QGS4SF0 = _Hh3cevtModuleRt_NSQ1QGS4SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 422)
)
_Hh3cevtModuleRt_NSQ1GP24TXEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1GP24TXEA0 = _Hh3cevtModuleRt_NSQ1GP24TXEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 423)
)
_Hh3cevtModuleRt_NSQ1GP48EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1GP48EB0 = _Hh3cevtModuleRt_NSQ1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 424)
)
_Hh3cevtModuleRt_NSQ1FWCEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1FWCEA0 = _Hh3cevtModuleRt_NSQ1FWCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 425)
)
_Hh3cevtModuleRt_NSQ1GT48EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1GT48EA0 = _Hh3cevtModuleRt_NSQ1GT48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 426)
)
_Hh3cevtModuleRt_NSQ1TGS8EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1TGS8EA0 = _Hh3cevtModuleRt_NSQ1TGS8EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 427)
)
_Hh3cevtModuleRt_NSQ1FAB04B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1FAB04B0 = _Hh3cevtModuleRt_NSQ1FAB04B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 428)
)
_Hh3cevtModuleRt_NSQ1FAB12D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1FAB12D0 = _Hh3cevtModuleRt_NSQ1FAB12D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 429)
)
_Hh3cevtModuleRt_NSQ1SUPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1SUPB0 = _Hh3cevtModuleRt_NSQ1SUPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 430)
)
_Hh3cevtModuleRt_VFW1000_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VFW1000 = _Hh3cevtModuleRt_VFW1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 431)
)
_Hh3cevtModuleRt_NSQ1CGC2SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQ1CGC2SE0 = _Hh3cevtModuleRt_NSQ1CGC2SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 432)
)
_Hh3cevtModuleRt_VLB1000_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VLB1000 = _Hh3cevtModuleRt_VLB1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 433)
)
_Hh3cevtModuleRt_NSQM1GT4PFC_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GT4PFC = _Hh3cevtModuleRt_NSQM1GT4PFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 434)
)
_Hh3cevtModuleRt_NSQM1FWDFG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FWDFG0 = _Hh3cevtModuleRt_NSQM1FWDFG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 435)
)
_Hh3cevtModuleRt_NSQM1NATDFGA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1NATDFGA0 = _Hh3cevtModuleRt_NSQM1NATDFGA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 436)
)
_Hh3cevtModuleRt_NSQM1NATDFGB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1NATDFGB0 = _Hh3cevtModuleRt_NSQM1NATDFGB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 437)
)
_Hh3cevtModuleRt_VFW2000_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VFW2000 = _Hh3cevtModuleRt_VFW2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 438)
)
_Hh3cevtModuleRt_VLB2000_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VLB2000 = _Hh3cevtModuleRt_VLB2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 439)
)
_Hh3cevtModuleRt_NSQM1IPSDFG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1IPSDFG0 = _Hh3cevtModuleRt_NSQM1IPSDFG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 440)
)
_Hh3cevtModuleRt_NSQM1FWDFGB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FWDFGB0 = _Hh3cevtModuleRt_NSQM1FWDFGB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 441)
)
_Hh3cevtModuleRt_NSQM1FWDFGC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FWDFGC0 = _Hh3cevtModuleRt_NSQM1FWDFGC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 442)
)
_Hh3cevtModuleRt_NSQM1FWDFGA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FWDFGA1 = _Hh3cevtModuleRt_NSQM1FWDFGA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 443)
)
_Hh3cevtModuleRt_NSQM1FWDFGB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FWDFGB1 = _Hh3cevtModuleRt_NSQM1FWDFGB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 444)
)
_Hh3cevtModuleRt_NSQM1FWDFGC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FWDFGC1 = _Hh3cevtModuleRt_NSQM1FWDFGC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 445)
)
_Hh3cevtModuleRt_NSQM1FWDFGD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FWDFGD1 = _Hh3cevtModuleRt_NSQM1FWDFGD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 446)
)
_Hh3cevtModuleRt_NSQM1SUPC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1SUPC0 = _Hh3cevtModuleRt_NSQM1SUPC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 447)
)
_Hh3cevtModuleRt_NSQM1TG4FBA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1TG4FBA = _Hh3cevtModuleRt_NSQM1TG4FBA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 448)
)
_Hh3cevtModuleRt_NSQM1GP4FBA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GP4FBA = _Hh3cevtModuleRt_NSQM1GP4FBA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 449)
)
_Hh3cevtModuleRt_NSQM2MPUC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2MPUC0 = _Hh3cevtModuleRt_NSQM2MPUC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 450)
)
_Hh3cevtModuleRt_NSQM2TGS16SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2TGS16SF0 = _Hh3cevtModuleRt_NSQM2TGS16SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 451)
)
_Hh3cevtModuleRt_NSQM2QGS4SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2QGS4SC0 = _Hh3cevtModuleRt_NSQM2QGS4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 452)
)
_Hh3cevtModuleRt_NSQM2GP24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2GP24TSSC0 = _Hh3cevtModuleRt_NSQM2GP24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 453)
)
_Hh3cevtModuleRt_NSQM2FWDSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2FWDSC0 = _Hh3cevtModuleRt_NSQM2FWDSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 454)
)
_Hh3cevtModuleRt_NSQM1ADEDFGA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1ADEDFGA0 = _Hh3cevtModuleRt_NSQM1ADEDFGA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 455)
)
_Hh3cevtModuleRt_NSQM2FWDSCA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2FWDSCA0 = _Hh3cevtModuleRt_NSQM2FWDSCA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 456)
)
_Hh3cevtModuleRt_NSQM1TGS32QSSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1TGS32QSSG0 = _Hh3cevtModuleRt_NSQM1TGS32QSSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 457)
)
_Hh3cevtModuleRt_NSQM1GT4PFCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GT4PFCA = _Hh3cevtModuleRt_NSQM1GT4PFCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 458)
)
_Hh3cevtModuleRt_NSQM1TG8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1TG8A = _Hh3cevtModuleRt_NSQM1TG8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 459)
)
_Hh3cevtModuleRt_NSQM1QG2A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1QG2A = _Hh3cevtModuleRt_NSQM1QG2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 460)
)
_Hh3cevtModuleRt_NSQM1GT8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GT8A = _Hh3cevtModuleRt_NSQM1GT8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 461)
)
_Hh3cevtModuleRt_NSQM1GP8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GP8A = _Hh3cevtModuleRt_NSQM1GP8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 462)
)
_Hh3cevtModuleRt_NSQM1MBFE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1MBFE0 = _Hh3cevtModuleRt_NSQM1MBFE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 463)
)
_Hh3cevtModuleRt_NSQM2MBFD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2MBFD0 = _Hh3cevtModuleRt_NSQM2MBFD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 464)
)
_Hh3cevtModuleRt_NSQM2QG2TG8GP40_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2QG2TG8GP40 = _Hh3cevtModuleRt_NSQM2QG2TG8GP40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 465)
)
_Hh3cevtModuleRt_NSQM2QG4GP40_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2QG4GP40 = _Hh3cevtModuleRt_NSQM2QG4GP40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 466)
)
_Hh3cevtModuleRt_NSQM2TG16GP40_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2TG16GP40 = _Hh3cevtModuleRt_NSQM2TG16GP40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 467)
)
_Hh3cevtModuleRt_NSQM1CGQ20_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1CGQ20 = _Hh3cevtModuleRt_NSQM1CGQ20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 468)
)
_Hh3cevtModuleRt_NSQM2FWDFG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2FWDFG0 = _Hh3cevtModuleRt_NSQM2FWDFG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 469)
)
_Hh3cevtModuleRt_NSQM2TMPUC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2TMPUC0 = _Hh3cevtModuleRt_NSQM2TMPUC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 470)
)
_Hh3cevtModuleRt_NSQM2IPSDSCA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2IPSDSCA0 = _Hh3cevtModuleRt_NSQM2IPSDSCA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 471)
)
_Hh3cevtModuleRt_NSQM2AC1400_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2AC1400 = _Hh3cevtModuleRt_NSQM2AC1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 472)
)
_Hh3cevtModuleRt_NSQM2DC1400_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2DC1400 = _Hh3cevtModuleRt_NSQM2DC1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 473)
)
_Hh3cevtModuleRt_NSQM1F1KGM0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1F1KGM0 = _Hh3cevtModuleRt_NSQM1F1KGM0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 474)
)
_Hh3cevtModuleRt_NSQM1F1KGM0_context_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1F1KGM0_context = _Hh3cevtModuleRt_NSQM1F1KGM0_context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 475)
)
_Hh3cevtModuleRt_NSQM1F5KGM0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1F5KGM0 = _Hh3cevtModuleRt_NSQM1F5KGM0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 476)
)
_Hh3cevtModuleRt_NSQM1F5KGM0_context_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1F5KGM0_context = _Hh3cevtModuleRt_NSQM1F5KGM0_context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 477)
)
_Hh3cevtModuleRt_NSQM2QG2GP40_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2QG2GP40 = _Hh3cevtModuleRt_NSQM2QG2GP40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 478)
)
_Hh3cevtModuleRt_NSQM2TG8GP40_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2TG8GP40 = _Hh3cevtModuleRt_NSQM2TG8GP40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 479)
)
_Hh3cevtModuleRt_NSQM2ADEDSCA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2ADEDSCA0 = _Hh3cevtModuleRt_NSQM2ADEDSCA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 482)
)
_Hh3cevtModuleRt_NSQM2IPSDSCB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2IPSDSCB0 = _Hh3cevtModuleRt_NSQM2IPSDSCB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 483)
)
_Hh3cevtModuleRt_NSQM1G4XS4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1G4XS4 = _Hh3cevtModuleRt_NSQM1G4XS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 484)
)
_Hh3cevtModuleRt_NSUM1GT4PFCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSUM1GT4PFCA = _Hh3cevtModuleRt_NSUM1GT4PFCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 485)
)
_Hh3cevtModuleRt_NSUM1TG8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSUM1TG8A = _Hh3cevtModuleRt_NSUM1TG8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 486)
)
_Hh3cevtModuleRt_NSUM1QG2A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSUM1QG2A = _Hh3cevtModuleRt_NSUM1QG2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 487)
)
_Hh3cevtModuleRt_NSUM1GT8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSUM1GT8A = _Hh3cevtModuleRt_NSUM1GT8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 488)
)
_Hh3cevtModuleRt_NSUM1GP8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSUM1GP8A = _Hh3cevtModuleRt_NSUM1GP8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 489)
)
_Hh3cevtModuleRt_NSQM2MPUD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2MPUD0 = _Hh3cevtModuleRt_NSQM2MPUD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 491)
)
_Hh3cevtModuleRt_NSQM1GMDSCA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GMDSCA1 = _Hh3cevtModuleRt_NSQM1GMDSCA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 492)
)
_Hh3cevtModuleRt_NSQM1MPULA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1MPULA = _Hh3cevtModuleRt_NSQM1MPULA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 493)
)
_Hh3cevtModuleRt_NSQM1MPULA2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1MPULA2 = _Hh3cevtModuleRt_NSQM1MPULA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 494)
)
_Hh3cevtModuleRt_NSQM1GT8A2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GT8A2 = _Hh3cevtModuleRt_NSQM1GT8A2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 495)
)
_Hh3cevtModuleRt_NSQM1GP4TG4A2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GP4TG4A2 = _Hh3cevtModuleRt_NSQM1GP4TG4A2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 496)
)
_Hh3cevtModuleRt_NSQM1GP2TG6A2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GP2TG6A2 = _Hh3cevtModuleRt_NSQM1GP2TG6A2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 497)
)
_Hh3cevtModuleRt_NSQM1TG4FBA7_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1TG4FBA7 = _Hh3cevtModuleRt_NSQM1TG4FBA7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 498)
)
_Hh3cevtModuleRt_NSQM1F1KGMB_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1F1KGMB = _Hh3cevtModuleRt_NSQM1F1KGMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 499)
)
_Hh3cevtModuleRt_NSQM1F1KGMC_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1F1KGMC = _Hh3cevtModuleRt_NSQM1F1KGMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 500)
)
_Hh3cevtModuleRt_NSQM1F5KGMC_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1F5KGMC = _Hh3cevtModuleRt_NSQM1F5KGMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 501)
)
_Hh3cevtModuleRt_NSQM5SUP08H0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5SUP08H0 = _Hh3cevtModuleRt_NSQM5SUP08H0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 502)
)
_Hh3cevtModuleRt_NSQM5SUP16C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5SUP16C0 = _Hh3cevtModuleRt_NSQM5SUP16C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 503)
)
_Hh3cevtModuleRt_NS_FWEMPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_FWEMPA0 = _Hh3cevtModuleRt_NS_FWEMPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 504)
)
_Hh3cevtModuleRt_NSQM5MBSHA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5MBSHA0 = _Hh3cevtModuleRt_NSQM5MBSHA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 505)
)
_Hh3cevtModuleRt_NS_C600_CGQ6A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_C600_CGQ6A0 = _Hh3cevtModuleRt_NS_C600_CGQ6A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 506)
)
_Hh3cevtModuleRt_NS_C300_CGQ2TG16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_C300_CGQ2TG16A0 = _Hh3cevtModuleRt_NS_C300_CGQ2TG16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 507)
)
_Hh3cevtModuleRt_NS_C300_TG24A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_C300_TG24A0 = _Hh3cevtModuleRt_NS_C300_TG24A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 508)
)
_Hh3cevtModuleRt_NS_C300_QG4TG16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_C300_QG4TG16A0 = _Hh3cevtModuleRt_NS_C300_QG4TG16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 509)
)
_Hh3cevtModuleRt_NSQM5FAB08A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5FAB08A0 = _Hh3cevtModuleRt_NSQM5FAB08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 510)
)
_Hh3cevtModuleRt_NSQM5FAB16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5FAB16A0 = _Hh3cevtModuleRt_NSQM5FAB16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 511)
)
_Hh3cevtModuleRt_NSQM5SL16UA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5SL16UA0 = _Hh3cevtModuleRt_NSQM5SL16UA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 512)
)
_Hh3cevtModuleRt_NSQM5SL16LA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5SL16LA0 = _Hh3cevtModuleRt_NSQM5SL16LA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 513)
)
_Hh3cevtModuleRt_NSQM2MPU12E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2MPU12E0 = _Hh3cevtModuleRt_NSQM2MPU12E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 514)
)
_Hh3cevtModuleRt_NSQM2MBFEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2MBFEA0 = _Hh3cevtModuleRt_NSQM2MBFEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 515)
)
_Hh3cevtModuleRt_NSQM2AC2500HD_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2AC2500HD = _Hh3cevtModuleRt_NSQM2AC2500HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 516)
)
_Hh3cevtModuleRt_NSQM2DC2500_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2DC2500 = _Hh3cevtModuleRt_NSQM2DC2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 517)
)
_Hh3cevtModuleRt_NSQM1HTIMGMG2A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1HTIMGMG2A = _Hh3cevtModuleRt_NSQM1HTIMGMG2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 518)
)
_Hh3cevtModuleRt_NSQM1HTIMGMG2B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1HTIMGMG2B = _Hh3cevtModuleRt_NSQM1HTIMGMG2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 519)
)
_Hh3cevtModuleRt_NSQM2V6DSCA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2V6DSCA0 = _Hh3cevtModuleRt_NSQM2V6DSCA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 520)
)
_Hh3cevtModuleRt_NSQM1AFC2000GDFGA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1AFC2000GDFGA0 = _Hh3cevtModuleRt_NSQM1AFC2000GDFGA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 521)
)
_Hh3cevtModuleRt_NSQM2AFC2000GDFGA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2AFC2000GDFGA0 = _Hh3cevtModuleRt_NSQM2AFC2000GDFGA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 522)
)
_Hh3cevtModuleRt_NSQM1FWDFGD1_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FWDFGD1_Z = _Hh3cevtModuleRt_NSQM1FWDFGD1_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 523)
)
_Hh3cevtModuleRt_NSQM1FAB12D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FAB12D0 = _Hh3cevtModuleRt_NSQM1FAB12D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 524)
)
_Hh3cevtModuleRt_NSQM1MBFEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1MBFEA0 = _Hh3cevtModuleRt_NSQM1MBFEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 525)
)
_Hh3cevtModuleRt_NSQM2TG16GP40_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2TG16GP40_Z = _Hh3cevtModuleRt_NSQM2TG16GP40_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 526)
)
_Hh3cevtModuleRt_NSQM2QG4GP40_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2QG4GP40_Z = _Hh3cevtModuleRt_NSQM2QG4GP40_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 527)
)
_Hh3cevtModuleRt_NSQM1CGQ20_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1CGQ20_Z = _Hh3cevtModuleRt_NSQM1CGQ20_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 528)
)
_Hh3cevtModuleRt_NSQM1TGS32QSSG0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1TGS32QSSG0_Z = _Hh3cevtModuleRt_NSQM1TGS32QSSG0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 529)
)
_Hh3cevtModuleRt_NSQM1AFC2000GDFGA0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1AFC2000GDFGA0_Z = _Hh3cevtModuleRt_NSQM1AFC2000GDFGA0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 530)
)
_Hh3cevtModuleRt_NSQM5AIASKA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5AIASKA1 = _Hh3cevtModuleRt_NSQM5AIASKA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 531)
)
_Hh3cevtModuleRt_NSQM1FWEFGA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FWEFGA0 = _Hh3cevtModuleRt_NSQM1FWEFGA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 532)
)
_Hh3cevtModuleRt_NS_ADEEMPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_ADEEMPA0 = _Hh3cevtModuleRt_NS_ADEEMPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 533)
)
_Hh3cevtModuleRt_NSQM2QG2TG8A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2QG2TG8A0 = _Hh3cevtModuleRt_NSQM2QG2TG8A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 534)
)
_Hh3cevtModuleRt_NS_ADEEMPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_ADEEMPB0 = _Hh3cevtModuleRt_NS_ADEEMPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 535)
)
_Hh3cevtModuleRt_NSQM2TG16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2TG16A0 = _Hh3cevtModuleRt_NSQM2TG16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 536)
)
_Hh3cevtModuleRt_NSQM6SUP04A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM6SUP04A0 = _Hh3cevtModuleRt_NSQM6SUP04A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 537)
)
_Hh3cevtModuleRt_NSQM2QG4A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2QG4A0 = _Hh3cevtModuleRt_NSQM2QG4A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 538)
)
_Hh3cevtModuleRt_NSQM1SUPD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1SUPD0 = _Hh3cevtModuleRt_NSQM1SUPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 539)
)
_Hh3cevtModuleRt_NSQM1FAB08E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1FAB08E0 = _Hh3cevtModuleRt_NSQM1FAB08E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 540)
)
_Hh3cevtModuleRt_NSQM1CGQ4TG24SHA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1CGQ4TG24SHA0 = _Hh3cevtModuleRt_NSQM1CGQ4TG24SHA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 541)
)
_Hh3cevtModuleRt_NSQM2MPUF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2MPUF0 = _Hh3cevtModuleRt_NSQM2MPUF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 542)
)
_Hh3cevtModuleRt_NSQM2FWDFGD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2FWDFGD0 = _Hh3cevtModuleRt_NSQM2FWDFGD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 543)
)
_Hh3cevtModuleRt_NSQM2MBFDB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2MBFDB0 = _Hh3cevtModuleRt_NSQM2MBFDB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 544)
)
_Hh3cevtModuleRt_NSQM2QG2TG8GP4B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2QG2TG8GP4B0 = _Hh3cevtModuleRt_NSQM2QG2TG8GP4B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 545)
)
_Hh3cevtModuleRt_NSQM2FAN08B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM2FAN08B = _Hh3cevtModuleRt_NSQM2FAN08B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 546)
)
_Hh3cevtModuleRt_NSQM5TSUP08A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5TSUP08A0 = _Hh3cevtModuleRt_NSQM5TSUP08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 547)
)
_Hh3cevtModuleRt_NSQM5TIPSEMPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5TIPSEMPA0 = _Hh3cevtModuleRt_NSQM5TIPSEMPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 548)
)
_Hh3cevtModuleRt_NSQM5AIASKB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5AIASKB1 = _Hh3cevtModuleRt_NSQM5AIASKB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 549)
)
_Hh3cevtModuleRt_NSQM1G4XS4_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1G4XS4_Z = _Hh3cevtModuleRt_NSQM1G4XS4_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 550)
)
_Hh3cevtModuleRt_NSQM5TIPSEMPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5TIPSEMPB0 = _Hh3cevtModuleRt_NSQM5TIPSEMPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 551)
)
_Hh3cevtModuleRt_NSQM5SUP04A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM5SUP04A1 = _Hh3cevtModuleRt_NSQM5SUP04A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 552)
)
_Hh3cevtModuleRt_NS_FWEMPB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_FWEMPB1 = _Hh3cevtModuleRt_NS_FWEMPB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 553)
)
_Hh3cevtModuleRt_NS_AFC2000EMPB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_AFC2000EMPB1 = _Hh3cevtModuleRt_NS_AFC2000EMPB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 554)
)
_Hh3cevtModuleRt_NS_AFC2000EMPA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_AFC2000EMPA1 = _Hh3cevtModuleRt_NS_AFC2000EMPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 555)
)
_Hh3cevtModuleRt_NS_ADEEMPC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_ADEEMPC0 = _Hh3cevtModuleRt_NS_ADEEMPC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 556)
)
_Hh3cevtModuleRt_NSQM1CGQ6SH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1CGQ6SH0 = _Hh3cevtModuleRt_NSQM1CGQ6SH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 557)
)
_Hh3cevtModuleRt_NSQM7SUPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM7SUPB0 = _Hh3cevtModuleRt_NSQM7SUPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 558)
)
_Hh3cevtModuleRt_NSQM7FAB06A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM7FAB06A0 = _Hh3cevtModuleRt_NSQM7FAB06A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 559)
)
_Hh3cevtModuleRt_NSQM7SUPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM7SUPA0 = _Hh3cevtModuleRt_NSQM7SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 560)
)
_Hh3cevtModuleRt_NSQM7FAB10A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM7FAB10A0 = _Hh3cevtModuleRt_NSQM7FAB10A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 561)
)
_Hh3cevtModuleRt_FAN_120B_3_A10_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FAN_120B_3_A10 = _Hh3cevtModuleRt_FAN_120B_3_A10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 562)
)
_Hh3cevtModuleRt_NSQM7MBSHB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM7MBSHB0 = _Hh3cevtModuleRt_NSQM7MBSHB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 563)
)
_Hh3cevtModuleRt_NSQM7MBSHA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM7MBSHA0 = _Hh3cevtModuleRt_NSQM7MBSHA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 564)
)
_Hh3cevtModuleRt_NS_FWFFGA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_FWFFGA0 = _Hh3cevtModuleRt_NS_FWFFGA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 565)
)
_Hh3cevtModuleRt_NS_FWFFGB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_FWFFGB0 = _Hh3cevtModuleRt_NS_FWFFGB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 566)
)
_Hh3cevtModuleRt_VG_8fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_8fxs = _Hh3cevtModuleRt_VG_8fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 600)
)
_Hh3cevtModuleRt_VG_24fxs_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_24fxs = _Hh3cevtModuleRt_VG_24fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 601)
)
_Hh3cevtModuleRt_VG_24fxs24fxo_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_24fxs24fxo = _Hh3cevtModuleRt_VG_24fxs24fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 602)
)
_Hh3cevtModuleRt_VG_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VG_MPU = _Hh3cevtModuleRt_VG_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 603)
)
_Hh3cevtModuleRt_MIM_VCX_CONNECT_P_3C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_VCX_CONNECT_P_3C = _Hh3cevtModuleRt_MIM_VCX_CONNECT_P_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 604)
)
_Hh3cevtModuleRt_MIM_VCX_CONNECT_S_3C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_VCX_CONNECT_S_3C = _Hh3cevtModuleRt_MIM_VCX_CONNECT_S_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 605)
)
_Hh3cevtModuleRt_MIM_VCX_3C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_VCX_3C = _Hh3cevtModuleRt_MIM_VCX_3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 606)
)
_Hh3cevtModuleRt_VNIC_VMXNET3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VNIC_VMXNET3 = _Hh3cevtModuleRt_VNIC_VMXNET3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 607)
)
_Hh3cevtModuleRt_VNIC_E1000_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VNIC_E1000 = _Hh3cevtModuleRt_VNIC_E1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 608)
)
_Hh3cevtModuleRt_VNIC_VIRTIO_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VNIC_VIRTIO = _Hh3cevtModuleRt_VNIC_VIRTIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 609)
)
_Hh3cevtModuleRt_VNIC_RTL8139_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VNIC_RTL8139 = _Hh3cevtModuleRt_VNIC_RTL8139_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 610)
)
_Hh3cevtModuleRt_VNIC_IXGBEVF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VNIC_IXGBEVF = _Hh3cevtModuleRt_VNIC_IXGBEVF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 611)
)
_Hh3cevtModuleRt_IXGBE_2XGE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IXGBE_2XGE = _Hh3cevtModuleRt_IXGBE_2XGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 612)
)
_Hh3cevtModuleRt_TG3_4GE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_TG3_4GE = _Hh3cevtModuleRt_TG3_4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 613)
)
_Hh3cevtModuleRt_MPUV16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MPUV16 = _Hh3cevtModuleRt_MPUV16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 614)
)
_Hh3cevtModuleRt_MPUP6_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MPUP6 = _Hh3cevtModuleRt_MPUP6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 615)
)
_Hh3cevtModuleRt_IGB_1GE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IGB_1GE = _Hh3cevtModuleRt_IGB_1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 616)
)
_Hh3cevtModuleRt_IGB_2GE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IGB_2GE = _Hh3cevtModuleRt_IGB_2GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 617)
)
_Hh3cevtModuleRt_IGB_4GE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_IGB_4GE = _Hh3cevtModuleRt_IGB_4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 618)
)
_Hh3cevtModuleRt_VLNS1000_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VLNS1000 = _Hh3cevtModuleRt_VLNS1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 619)
)
_Hh3cevtModuleRt_VLNS2000_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_VLNS2000 = _Hh3cevtModuleRt_VLNS2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 620)
)
_Hh3cevtModuleRt_NS_MIM_GP4A2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_MIM_GP4A2 = _Hh3cevtModuleRt_NS_MIM_GP4A2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 621)
)
_Hh3cevtModuleRt_NS_MIM_GT4PFCA2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_MIM_GT4PFCA2 = _Hh3cevtModuleRt_NS_MIM_GT4PFCA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 622)
)
_Hh3cevtModuleRt_NS_NIM_TG6A2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_NIM_TG6A2 = _Hh3cevtModuleRt_NS_NIM_TG6A2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 623)
)
_Hh3cevtModuleRt_NS_SIM_GT4PFCA2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_SIM_GT4PFCA2 = _Hh3cevtModuleRt_NS_SIM_GT4PFCA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 624)
)
_Hh3cevtModuleRt_NS_NIM_TG6A_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_NIM_TG6A_Z = _Hh3cevtModuleRt_NS_NIM_TG6A_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 625)
)
_Hh3cevtModuleRt_SIC_4GSW_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4GSW = _Hh3cevtModuleRt_SIC_4GSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 800)
)
_Hh3cevtModuleRt_SIC_4GSWP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4GSWP = _Hh3cevtModuleRt_SIC_4GSWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 801)
)
_Hh3cevtModuleRt_SIC_1GEC_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_1GEC_V2 = _Hh3cevtModuleRt_SIC_1GEC_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 802)
)
_Hh3cevtModuleRt_4G_LTE_ATT_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_4G_LTE_ATT = _Hh3cevtModuleRt_4G_LTE_ATT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 803)
)
_Hh3cevtModuleRt_4G_TD_LTE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_4G_TD_LTE = _Hh3cevtModuleRt_4G_TD_LTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 804)
)
_Hh3cevtModuleRt_FIP_240_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_240 = _Hh3cevtModuleRt_FIP_240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 805)
)
_Hh3cevtModuleRt_8GBP_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_8GBP_V2 = _Hh3cevtModuleRt_8GBP_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 806)
)
_Hh3cevtModuleRt_HMIM_CNDE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_CNDE = _Hh3cevtModuleRt_HMIM_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 807)
)
_Hh3cevtModuleRt_4G_LTE_Mobile_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_4G_LTE_Mobile = _Hh3cevtModuleRt_4G_LTE_Mobile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 808)
)
_Hh3cevtModuleRt_SIC_4G_LTE_M_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4G_LTE_M = _Hh3cevtModuleRt_SIC_4G_LTE_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 809)
)
_Hh3cevtModuleRt_CRSE_X3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CRSE_X3 = _Hh3cevtModuleRt_CRSE_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 810)
)
_Hh3cevtModuleRt_CFIP_300_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CFIP_300 = _Hh3cevtModuleRt_CFIP_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 811)
)
_Hh3cevtModuleRt_CFIP_310_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CFIP_310 = _Hh3cevtModuleRt_CFIP_310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 812)
)
_Hh3cevtModuleRt_CSAP_4EXP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CSAP_4EXP = _Hh3cevtModuleRt_CSAP_4EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 813)
)
_Hh3cevtModuleRt_RSU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RSU = _Hh3cevtModuleRt_RSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 814)
)
_Hh3cevtModuleRt_CFIP_610_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CFIP_610 = _Hh3cevtModuleRt_CFIP_610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 815)
)
_Hh3cevtModuleRt_2EXP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_2EXP = _Hh3cevtModuleRt_2EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 816)
)
_Hh3cevtModuleRt_16GBP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_16GBP = _Hh3cevtModuleRt_16GBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 817)
)
_Hh3cevtModuleRt_CFIP_240_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CFIP_240 = _Hh3cevtModuleRt_CFIP_240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 818)
)
_Hh3cevtModuleRt_RSE_X3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RSE_X3 = _Hh3cevtModuleRt_RSE_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 819)
)
_Hh3cevtModuleRt_SAP_8EXP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_8EXP = _Hh3cevtModuleRt_SAP_8EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 820)
)
_Hh3cevtModuleRt_SAP_16EXP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_16EXP = _Hh3cevtModuleRt_SAP_16EXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 821)
)
_Hh3cevtModuleRt_PU1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_PU1P = _Hh3cevtModuleRt_PU1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 822)
)
_Hh3cevtModuleRt_RSU100_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RSU100 = _Hh3cevtModuleRt_RSU100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 823)
)
_Hh3cevtModuleRt_SAP_2QGP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_2QGP = _Hh3cevtModuleRt_SAP_2QGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 824)
)
_Hh3cevtModuleRt_CSFE_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CSFE_X1 = _Hh3cevtModuleRt_CSFE_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 825)
)
_Hh3cevtModuleRt_RIC_4GEE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RIC_4GEE = _Hh3cevtModuleRt_RIC_4GEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 826)
)
_Hh3cevtModuleRt_RIC_4GEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RIC_4GEF = _Hh3cevtModuleRt_RIC_4GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 827)
)
_Hh3cevtModuleRt_RIC_8GEE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RIC_8GEE = _Hh3cevtModuleRt_RIC_8GEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 828)
)
_Hh3cevtModuleRt_RIC_8GEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RIC_8GEF = _Hh3cevtModuleRt_RIC_8GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 829)
)
_Hh3cevtModuleRt_RIC_1XGEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RIC_1XGEF = _Hh3cevtModuleRt_RIC_1XGEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 830)
)
_Hh3cevtModuleRt_HMIM_1E1POS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1E1POS = _Hh3cevtModuleRt_HMIM_1E1POS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 831)
)
_Hh3cevtModuleRt_DHMIM_1DM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_DHMIM_1DM = _Hh3cevtModuleRt_DHMIM_1DM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 832)
)
_Hh3cevtModuleRt_DHMIM_1E1POS1DM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_DHMIM_1E1POS1DM = _Hh3cevtModuleRt_DHMIM_1E1POS1DM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 833)
)
_Hh3cevtModuleRt_RPE_X3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RPE_X3 = _Hh3cevtModuleRt_RPE_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 834)
)
_Hh3cevtModuleRt_CRPE_X3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CRPE_X3 = _Hh3cevtModuleRt_CRPE_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 835)
)
_Hh3cevtModuleRt_SAP_28GE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_28GE = _Hh3cevtModuleRt_SAP_28GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 836)
)
_Hh3cevtModuleRt_SAP_20GE2XP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SAP_20GE2XP = _Hh3cevtModuleRt_SAP_20GE2XP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 837)
)
_Hh3cevtModuleRt_SFE_L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SFE_L1 = _Hh3cevtModuleRt_SFE_L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 838)
)
_Hh3cevtModuleRt_FIP_640_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_640 = _Hh3cevtModuleRt_FIP_640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 839)
)
_Hh3cevtModuleRt_HMIM_8GSWF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8GSWF = _Hh3cevtModuleRt_HMIM_8GSWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 840)
)
_Hh3cevtModuleRt_HMIM_8E1T1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8E1T1 = _Hh3cevtModuleRt_HMIM_8E1T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 841)
)
_Hh3cevtModuleRt_HMIM_4E1T1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4E1T1 = _Hh3cevtModuleRt_HMIM_4E1T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 842)
)
_Hh3cevtModuleRt_HMIM_2E1T1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2E1T1 = _Hh3cevtModuleRt_HMIM_2E1T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 843)
)
_Hh3cevtModuleRt_HMIM_8E1T1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8E1T1_F = _Hh3cevtModuleRt_HMIM_8E1T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 844)
)
_Hh3cevtModuleRt_HMIM_4E1T1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4E1T1_F = _Hh3cevtModuleRt_HMIM_4E1T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 845)
)
_Hh3cevtModuleRt_HMIM_2E1T1_F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2E1T1_F = _Hh3cevtModuleRt_HMIM_2E1T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 846)
)
_Hh3cevtModuleRt_SIC_3G_HSPA_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_3G_HSPA_V2 = _Hh3cevtModuleRt_SIC_3G_HSPA_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 847)
)
_Hh3cevtModuleRt_SIC_4GSWF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4GSWF = _Hh3cevtModuleRt_SIC_4GSWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 848)
)
_Hh3cevtModuleRt_SIC_4G_LTE_G_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4G_LTE_G_V2 = _Hh3cevtModuleRt_SIC_4G_LTE_G_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 849)
)
_Hh3cevtModuleRt_SIC_4G_LTE_A_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4G_LTE_A_V2 = _Hh3cevtModuleRt_SIC_4G_LTE_A_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 850)
)
_Hh3cevtModuleRt_SIC_4G_LTE_V_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4G_LTE_V_V2 = _Hh3cevtModuleRt_SIC_4G_LTE_V_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 851)
)
_Hh3cevtModuleRt_MPU60_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MPU60 = _Hh3cevtModuleRt_MPU60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 852)
)
_Hh3cevtModuleRt_SPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU = _Hh3cevtModuleRt_SPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 853)
)
_Hh3cevtModuleRt_SIC_1VE1T1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_1VE1T1 = _Hh3cevtModuleRt_SIC_1VE1T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 854)
)
_Hh3cevtModuleRt_CFIP_700_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CFIP_700 = _Hh3cevtModuleRt_CFIP_700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 855)
)
_Hh3cevtModuleRt_HIM_20GBP_H3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM_20GBP_H3 = _Hh3cevtModuleRt_HIM_20GBP_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 856)
)
_Hh3cevtModuleRt_HIM_4EXP_H3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM_4EXP_H3 = _Hh3cevtModuleRt_HIM_4EXP_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 857)
)
_Hh3cevtModuleRt_HIM_2EXP_H3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM_2EXP_H3 = _Hh3cevtModuleRt_HIM_2EXP_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 858)
)
_Hh3cevtModuleRt_HIM_8GBE_V3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM_8GBE_V3 = _Hh3cevtModuleRt_HIM_8GBE_V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 859)
)
_Hh3cevtModuleRt_HIM_4GBE_V3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM_4GBE_V3 = _Hh3cevtModuleRt_HIM_4GBE_V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 860)
)
_Hh3cevtModuleRt_HIM_8GBP_V3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM_8GBP_V3 = _Hh3cevtModuleRt_HIM_8GBP_V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 861)
)
_Hh3cevtModuleRt_HIM_4GBP_V3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM_4GBP_V3 = _Hh3cevtModuleRt_HIM_4GBP_V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 862)
)
_Hh3cevtModuleRt_SIC_AP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_AP = _Hh3cevtModuleRt_SIC_AP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 863)
)
_Hh3cevtModuleRt_CR_MPU_04B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_MPU_04B = _Hh3cevtModuleRt_CR_MPU_04B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 864)
)
_Hh3cevtModuleRt_CR_MPU_16B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_MPU_16B = _Hh3cevtModuleRt_CR_MPU_16B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 865)
)
_Hh3cevtModuleRt_CR_MPU_16E_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_MPU_16E = _Hh3cevtModuleRt_CR_MPU_16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 866)
)
_Hh3cevtModuleRt_CR_SFU_04D_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_SFU_04D_H = _Hh3cevtModuleRt_CR_SFU_04D_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 867)
)
_Hh3cevtModuleRt_CR_SFU_08C_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_SFU_08C_H = _Hh3cevtModuleRt_CR_SFU_08C_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 868)
)
_Hh3cevtModuleRt_CR_SFU_08D_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_SFU_08D_H = _Hh3cevtModuleRt_CR_SFU_08D_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 869)
)
_Hh3cevtModuleRt_CR_SFU_16B_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_SFU_16B_H = _Hh3cevtModuleRt_CR_SFU_16B_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 870)
)
_Hh3cevtModuleRt_CR_SFU_16C_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_SFU_16C_H = _Hh3cevtModuleRt_CR_SFU_16C_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 871)
)
_Hh3cevtModuleRt_CR_LPU_CQ12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_CQ12 = _Hh3cevtModuleRt_CR_LPU_CQ12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 872)
)
_Hh3cevtModuleRt_CR_LPU_4004_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_4004 = _Hh3cevtModuleRt_CR_LPU_4004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 873)
)
_Hh3cevtModuleRt_CR_HIC_PU02_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_PU02 = _Hh3cevtModuleRt_CR_HIC_PU02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 874)
)
_Hh3cevtModuleRt_CR_HIC_XP12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_XP12 = _Hh3cevtModuleRt_CR_HIC_XP12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 875)
)
_Hh3cevtModuleRt_CR_HIC_GP12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_GP12 = _Hh3cevtModuleRt_CR_HIC_GP12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 876)
)
_Hh3cevtModuleRt_CR_HIC_QQ03_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_QQ03 = _Hh3cevtModuleRt_CR_HIC_QQ03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 877)
)
_Hh3cevtModuleRt_CR_HIC_CC01_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_CC01 = _Hh3cevtModuleRt_CR_HIC_CC01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 878)
)
_Hh3cevtModuleRt_CR_HIC_CP01_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_CP01 = _Hh3cevtModuleRt_CR_HIC_CP01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 879)
)
_Hh3cevtModuleRt_CR_MPU_16C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_MPU_16C = _Hh3cevtModuleRt_CR_MPU_16C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 880)
)
_Hh3cevtModuleRt_MPU_100_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MPU_100_X1 = _Hh3cevtModuleRt_MPU_100_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 881)
)
_Hh3cevtModuleRt_SPU_100_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU_100_X1 = _Hh3cevtModuleRt_SPU_100_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 882)
)
_Hh3cevtModuleRt_SPU_200_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU_200_X1 = _Hh3cevtModuleRt_SPU_200_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 883)
)
_Hh3cevtModuleRt_SPU_400_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU_400_X1 = _Hh3cevtModuleRt_SPU_400_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 884)
)
_Hh3cevtModuleRt_HIM_10GB2EXP_H3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM_10GB2EXP_H3 = _Hh3cevtModuleRt_HIM_10GB2EXP_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 885)
)
_Hh3cevtModuleRt_HIM_11GB1EXP_H3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HIM_11GB1EXP_H3 = _Hh3cevtModuleRt_HIM_11GB1EXP_H3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 886)
)
_Hh3cevtModuleRt_HMIM_1E3T3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_1E3T3 = _Hh3cevtModuleRt_HMIM_1E3T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 887)
)
_Hh3cevtModuleRt_SIC_4G_CNDE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4G_CNDE = _Hh3cevtModuleRt_SIC_4G_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 888)
)
_Hh3cevtModuleRt_SIC_D4G_CNDE_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_D4G_CNDE = _Hh3cevtModuleRt_SIC_D4G_CNDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 889)
)
_Hh3cevtModuleRt_CR_LPU_CC08_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_CC08 = _Hh3cevtModuleRt_CR_LPU_CC08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 890)
)
_Hh3cevtModuleRt_CR_LPU_2002_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_2002 = _Hh3cevtModuleRt_CR_LPU_2002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 891)
)
_Hh3cevtModuleRt_CR_LPU_XP20CC02_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_XP20CC02 = _Hh3cevtModuleRt_CR_LPU_XP20CC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 892)
)
_Hh3cevtModuleRt_CR_LPU_XP40_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_XP40 = _Hh3cevtModuleRt_CR_LPU_XP40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 893)
)
_Hh3cevtModuleRt_CR_LPU_CC04_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_CC04 = _Hh3cevtModuleRt_CR_LPU_CC04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 894)
)
_Hh3cevtModuleRt_FIP_680_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_680 = _Hh3cevtModuleRt_FIP_680_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 895)
)
_Hh3cevtModuleRt_MIC_XP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_XP4L = _Hh3cevtModuleRt_MIC_XP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 896)
)
_Hh3cevtModuleRt_MIM_1T3_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIM_1T3_V2 = _Hh3cevtModuleRt_MIM_1T3_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 897)
)
_Hh3cevtModuleRt_MIC_GP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_GP4L = _Hh3cevtModuleRt_MIC_GP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 898)
)
_Hh3cevtModuleRt_MIC_GP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_GP8L = _Hh3cevtModuleRt_MIC_GP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 899)
)
_Hh3cevtModuleRt_CR_19K_MPU_20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MPU_20A = _Hh3cevtModuleRt_CR_19K_MPU_20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 900)
)
_Hh3cevtModuleRt_CR_19K_MPU_20B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MPU_20B = _Hh3cevtModuleRt_CR_19K_MPU_20B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 901)
)
_Hh3cevtModuleRt_CR_19K_SFU_20C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_SFU_20C = _Hh3cevtModuleRt_CR_19K_SFU_20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 902)
)
_Hh3cevtModuleRt_CR_19K_MSFU_20B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MSFU_20B = _Hh3cevtModuleRt_CR_19K_MSFU_20B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 903)
)
_Hh3cevtModuleRt_CR_19K_MSFU_20C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MSFU_20C = _Hh3cevtModuleRt_CR_19K_MSFU_20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 904)
)
_Hh3cevtModuleRt_CR_19K_MCCU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MCCU = _Hh3cevtModuleRt_CR_19K_MCCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 905)
)
_Hh3cevtModuleRt_CR_19K_MFCU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MFCU = _Hh3cevtModuleRt_CR_19K_MFCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 906)
)
_Hh3cevtModuleRt_RIC_8E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RIC_8E1 = _Hh3cevtModuleRt_RIC_8E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 907)
)
_Hh3cevtModuleRt_RIC_1XGEF4GEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RIC_1XGEF4GEF = _Hh3cevtModuleRt_RIC_1XGEF4GEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 908)
)
_Hh3cevtModuleRt_RIC_TU01A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RIC_TU01A = _Hh3cevtModuleRt_RIC_TU01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 909)
)
_Hh3cevtModuleRt_SPE_S1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPE_S1 = _Hh3cevtModuleRt_SPE_S1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 910)
)
_Hh3cevtModuleRt_SPE_S3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPE_S3 = _Hh3cevtModuleRt_SPE_S3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 911)
)
_Hh3cevtModuleRt_SPU_600_X1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU_600_X1 = _Hh3cevtModuleRt_SPU_600_X1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 912)
)
_Hh3cevtModuleRt_RIC_CP08_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RIC_CP08 = _Hh3cevtModuleRt_RIC_CP08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 913)
)
_Hh3cevtModuleRt_MIC_SP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_SP4L = _Hh3cevtModuleRt_MIC_SP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 914)
)
_Hh3cevtModuleRt_MIC_ET16L_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_ET16L = _Hh3cevtModuleRt_MIC_ET16L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 915)
)
_Hh3cevtModuleRt_MIC_CLP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_CLP4L = _Hh3cevtModuleRt_MIC_CLP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 916)
)
_Hh3cevtModuleRt_MIC_CLP2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_CLP2L = _Hh3cevtModuleRt_MIC_CLP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 917)
)
_Hh3cevtModuleRt_MIC_SP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_SP8L = _Hh3cevtModuleRt_MIC_SP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 918)
)
_Hh3cevtModuleRt_HMIM_8EM_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_8EM = _Hh3cevtModuleRt_HMIM_8EM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 919)
)
_Hh3cevtModuleRt_SFU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SFU = _Hh3cevtModuleRt_SFU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 920)
)
_Hh3cevtModuleRt_SFE_L2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SFE_L2 = _Hh3cevtModuleRt_SFE_L2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 921)
)
_Hh3cevtModuleRt_SFU_UNFIXED_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SFU_UNFIXED = _Hh3cevtModuleRt_SFU_UNFIXED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 922)
)
_Hh3cevtModuleRt_FIP_380_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_380 = _Hh3cevtModuleRt_FIP_380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 923)
)
_Hh3cevtModuleRt_CR_19K_MPU_08A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MPU_08A = _Hh3cevtModuleRt_CR_19K_MPU_08A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 924)
)
_Hh3cevtModuleRt_CR_19K_MPU_16A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MPU_16A = _Hh3cevtModuleRt_CR_19K_MPU_16A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 925)
)
_Hh3cevtModuleRt_CR_19K_SFU_08C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_SFU_08C = _Hh3cevtModuleRt_CR_19K_SFU_08C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 926)
)
_Hh3cevtModuleRt_CR_19K_SFU_16C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_SFU_16C = _Hh3cevtModuleRt_CR_19K_SFU_16C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 927)
)
_Hh3cevtModuleRt_CR_19K_LPU_CC08_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_CC08 = _Hh3cevtModuleRt_CR_19K_LPU_CC08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 928)
)
_Hh3cevtModuleRt_CR_19K_LPU_2002_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_2002 = _Hh3cevtModuleRt_CR_19K_LPU_2002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 929)
)
_Hh3cevtModuleRt_CR_19K_LPU_XP20CC02_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_XP20CC02 = _Hh3cevtModuleRt_CR_19K_LPU_XP20CC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 930)
)
_Hh3cevtModuleRt_CR_19K_LPU_XP40_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_XP40 = _Hh3cevtModuleRt_CR_19K_LPU_XP40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 931)
)
_Hh3cevtModuleRt_CR_19K_LPU_CC04_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_CC04 = _Hh3cevtModuleRt_CR_19K_LPU_CC04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 932)
)
_Hh3cevtModuleRt_CR_19K_LPU_CQ12_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_CQ12 = _Hh3cevtModuleRt_CR_19K_LPU_CQ12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 933)
)
_Hh3cevtModuleRt_MIC_X_GT8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_X_GT8 = _Hh3cevtModuleRt_MIC_X_GT8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 934)
)
_Hh3cevtModuleRt_MIC_X_GP4GT4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_X_GP4GT4 = _Hh3cevtModuleRt_MIC_X_GP4GT4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 935)
)
_Hh3cevtModuleRt_MIC_X_GP10_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_X_GP10 = _Hh3cevtModuleRt_MIC_X_GP10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 936)
)
_Hh3cevtModuleRt_MIC_X_GP8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MIC_X_GP8 = _Hh3cevtModuleRt_MIC_X_GP8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 937)
)
_Hh3cevtModuleRt_CR_19K_LPU_4004_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_4004 = _Hh3cevtModuleRt_CR_19K_LPU_4004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 938)
)
_Hh3cevtModuleRt_FIP_260_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_260 = _Hh3cevtModuleRt_FIP_260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 939)
)
_Hh3cevtModuleRt_CR_LPU_XP72_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_XP72 = _Hh3cevtModuleRt_CR_LPU_XP72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 940)
)
_Hh3cevtModuleRt_CR_LPU_XP48_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_XP48 = _Hh3cevtModuleRt_CR_LPU_XP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 941)
)
_Hh3cevtModuleRt_CR_LPU_CC04B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_CC04B = _Hh3cevtModuleRt_CR_LPU_CC04B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 942)
)
_Hh3cevtModuleRt_CR_LPU_2002B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_2002B = _Hh3cevtModuleRt_CR_LPU_2002B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 943)
)
_Hh3cevtModuleRt_LPU_1001B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_LPU_1001B = _Hh3cevtModuleRt_LPU_1001B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 944)
)
_Hh3cevtModuleRt_CR_19K_MSFU_08A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MSFU_08A = _Hh3cevtModuleRt_CR_19K_MSFU_08A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 945)
)
_Hh3cevtModuleRt_Sic_AP220_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_Sic_AP220 = _Hh3cevtModuleRt_Sic_AP220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 946)
)
_Hh3cevtModuleRt_FIP_660_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_660 = _Hh3cevtModuleRt_FIP_660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 947)
)
_Hh3cevtModuleRT_MIC_X_ET16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIC_X_ET16 = _Hh3cevtModuleRT_MIC_X_ET16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 948)
)
_Hh3cevtModuleRT_MIC_X_SP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIC_X_SP4 = _Hh3cevtModuleRT_MIC_X_SP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 949)
)
_Hh3cevtModuleRT_MIC_X_SP8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIC_X_SP8 = _Hh3cevtModuleRT_MIC_X_SP8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 950)
)
_Hh3cevtModuleRT_MIC_X_CLP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIC_X_CLP2 = _Hh3cevtModuleRT_MIC_X_CLP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 951)
)
_Hh3cevtModuleRT_MIC_X_CLP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIC_X_CLP4 = _Hh3cevtModuleRT_MIC_X_CLP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 952)
)
_Hh3cevtModuleRt_SPU_300_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU_300 = _Hh3cevtModuleRt_SPU_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 953)
)
_Hh3cevtModuleRt_CR_19K_LPU_XP72_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_XP72 = _Hh3cevtModuleRt_CR_19K_LPU_XP72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 954)
)
_Hh3cevtModuleRt_CR_19K_LPU_XP48_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_XP48 = _Hh3cevtModuleRt_CR_19K_LPU_XP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 955)
)
_Hh3cevtModuleRt_CR_19K_LPU_2002B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_2002B = _Hh3cevtModuleRt_CR_19K_LPU_2002B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 956)
)
_Hh3cevtModuleRt_CR_19K_LPU_CC04B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_CC04B = _Hh3cevtModuleRt_CR_19K_LPU_CC04B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 957)
)
_Hh3cevtModuleRt_CR_19K_MPU_16B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MPU_16B = _Hh3cevtModuleRt_CR_19K_MPU_16B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 958)
)
_Hh3cevtModuleRT_RPE_X5_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_RPE_X5 = _Hh3cevtModuleRT_RPE_X5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 959)
)
_Hh3cevtModuleRT_RPE_X5E_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_RPE_X5E = _Hh3cevtModuleRT_RPE_X5E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 960)
)
_Hh3cevtModuleRt_CR_HIC_PS04_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_PS04 = _Hh3cevtModuleRt_CR_HIC_PS04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 961)
)
_Hh3cevtModuleRt_CR_HIC_PL08_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_PL08 = _Hh3cevtModuleRt_CR_HIC_PL08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 962)
)
_Hh3cevtModuleRT_MIC_X_XP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIC_X_XP2 = _Hh3cevtModuleRT_MIC_X_XP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 963)
)
_Hh3cevtModuleRT_MIC_X_XP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIC_X_XP4 = _Hh3cevtModuleRT_MIC_X_XP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 964)
)
_Hh3cevtModuleRT_MIC_X_XP4W_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIC_X_XP4W = _Hh3cevtModuleRT_MIC_X_XP4W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 965)
)
_Hh3cevtModuleRT_SIC_CNDE_SJK_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_CNDE_SJK = _Hh3cevtModuleRT_SIC_CNDE_SJK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 966)
)
_Hh3cevtModuleRT_SIC_4G_CNDE_SJK_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_4G_CNDE_SJK = _Hh3cevtModuleRT_SIC_4G_CNDE_SJK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 967)
)
_Hh3cevtModuleRT_SIC_D4G_CNDE_SJK_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_D4G_CNDE_SJK = _Hh3cevtModuleRT_SIC_D4G_CNDE_SJK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 968)
)
_Hh3cevtModuleRt_CR_19K_MSFU_16A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MSFU_16A = _Hh3cevtModuleRt_CR_19K_MSFU_16A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 969)
)
_Hh3cevtModuleRT_HMIM_CNDE_SJK_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_HMIM_CNDE_SJK = _Hh3cevtModuleRT_HMIM_CNDE_SJK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 970)
)
_Hh3cevtModuleRT_MIBIF_MINI_CNDE_SJK_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIBIF_MINI_CNDE_SJK = _Hh3cevtModuleRT_MIBIF_MINI_CNDE_SJK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 971)
)
_Hh3cevtModuleRT_SIC_AP320_FIT_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_AP320_FIT = _Hh3cevtModuleRT_SIC_AP320_FIT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 972)
)
_Hh3cevtModuleRT_SAP_XP4GE32_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SAP_XP4GE32 = _Hh3cevtModuleRT_SAP_XP4GE32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 973)
)
_Hh3cevtModuleRT_SIC_4E1_F_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_SIC_4E1_F_Z = _Hh3cevtModuleRT_SIC_4E1_F_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 974)
)
_Hh3cevtModuleRT_HRIC_CLGQ2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_HRIC_CLGQ2 = _Hh3cevtModuleRT_HRIC_CLGQ2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 975)
)
_Hh3cevtModuleRT_HRIC_YGS4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_HRIC_YGS4 = _Hh3cevtModuleRT_HRIC_YGS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 976)
)
_Hh3cevtModuleRT_HRIC_XP8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_HRIC_XP8 = _Hh3cevtModuleRT_HRIC_XP8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 977)
)
_Hh3cevtModuleRT_HRIC_GP8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_HRIC_GP8 = _Hh3cevtModuleRT_HRIC_GP8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 978)
)
_Hh3cevtModuleRT_HRIC_GT8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_HRIC_GT8 = _Hh3cevtModuleRT_HRIC_GT8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 979)
)
_Hh3cevtModuleRT_MIC_X_CNDE_SJK_ObjectIdentity = ObjectIdentity
hh3cevtModuleRT_MIC_X_CNDE_SJK = _Hh3cevtModuleRT_MIC_X_CNDE_SJK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 980)
)
_Hh3cevtModuleRt_CR_19K_LPU_CQ18_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_CQ18 = _Hh3cevtModuleRt_CR_19K_LPU_CQ18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 981)
)
_Hh3cevtModuleRt_CR_19K_LPU_CQ12B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_CQ12B = _Hh3cevtModuleRt_CR_19K_LPU_CQ12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 982)
)
_Hh3cevtModuleRt_CR_19K_LPU_SP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_SP = _Hh3cevtModuleRt_CR_19K_LPU_SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 983)
)
_Hh3cevtModuleRt_CR_HIC_CQ01_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_CQ01 = _Hh3cevtModuleRt_CR_HIC_CQ01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 984)
)
_Hh3cevtModuleRt_NS_NIM_TG6A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_NIM_TG6A = _Hh3cevtModuleRt_NS_NIM_TG6A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 985)
)
_Hh3cevtModuleRtNS_NIM_TG4A3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNS_NIM_TG4A3 = _Hh3cevtModuleRtNS_NIM_TG4A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 986)
)
_Hh3cevtModuleRtNSQM2CGQ20_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM2CGQ20 = _Hh3cevtModuleRtNSQM2CGQ20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 987)
)
_Hh3cevtModuleRtNSQM2FWDFGC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM2FWDFGC0 = _Hh3cevtModuleRtNSQM2FWDFGC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 988)
)
_Hh3cevtModuleRtNSQM2FWDFGB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM2FWDFGB0 = _Hh3cevtModuleRtNSQM2FWDFGB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 989)
)
_Hh3cevtModuleRt_NS_TIM_TG8A2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NS_TIM_TG8A2 = _Hh3cevtModuleRt_NS_TIM_TG8A2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 990)
)
_Hh3cevtModuleRtNSQM5MBSHA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM5MBSHA1 = _Hh3cevtModuleRtNSQM5MBSHA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 991)
)
_Hh3cevtModuleRtNS_C600_CGQ6A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNS_C600_CGQ6A1 = _Hh3cevtModuleRtNS_C600_CGQ6A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 992)
)
_Hh3cevtModuleRtNSQM5SUP08A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM5SUP08A1 = _Hh3cevtModuleRtNSQM5SUP08A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 993)
)
_Hh3cevtModuleRtNSQ1M9ESL16UA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQ1M9ESL16UA0 = _Hh3cevtModuleRtNSQ1M9ESL16UA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 994)
)
_Hh3cevtModuleRtNS_C300_CGQ2TG16A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNS_C300_CGQ2TG16A1 = _Hh3cevtModuleRtNS_C300_CGQ2TG16A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 995)
)
_Hh3cevtModuleRtNS_FWEMPA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNS_FWEMPA1 = _Hh3cevtModuleRtNS_FWEMPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 996)
)
_Hh3cevtModuleRtNSQM5FAB08A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM5FAB08A1 = _Hh3cevtModuleRtNSQM5FAB08A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 997)
)
_Hh3cevtModuleRtNS_C300_QG4TG16A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNS_C300_QG4TG16A1 = _Hh3cevtModuleRtNS_C300_QG4TG16A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 998)
)
_Hh3cevtModuleRtNSQM5FAB16A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM5FAB16A1 = _Hh3cevtModuleRtNSQM5FAB16A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 999)
)
_Hh3cevtModuleRtNSQM5SUP16A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM5SUP16A1 = _Hh3cevtModuleRtNSQM5SUP16A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1000)
)
_Hh3cevtModuleRtNSQ1M9ESL16LA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQ1M9ESL16LA0 = _Hh3cevtModuleRtNSQ1M9ESL16LA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1001)
)
_Hh3cevtModuleRtNS_C300_TG24A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNS_C300_TG24A1 = _Hh3cevtModuleRtNS_C300_TG24A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1002)
)
_Hh3cevtModuleRtNSQM1SSICASK1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM1SSICASK1 = _Hh3cevtModuleRtNSQM1SSICASK1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1003)
)
_Hh3cevtModuleRtNSQM2AFC2000DGDSCA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM2AFC2000DGDSCA0 = _Hh3cevtModuleRtNSQM2AFC2000DGDSCA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1004)
)
_Hh3cevtModuleRt_MPU_60_WiNet_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MPU_60_WiNet = _Hh3cevtModuleRt_MPU_60_WiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1005)
)
_Hh3cevtModuleRtNSQM2VGDSCA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM2VGDSCA0 = _Hh3cevtModuleRtNSQM2VGDSCA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1006)
)
_Hh3cevtModuleRt_HRIC_YGS2_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HRIC_YGS2 = _Hh3cevtModuleRt_HRIC_YGS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1007)
)
_Hh3cevtModuleRt_HRIC_LGQ1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HRIC_LGQ1 = _Hh3cevtModuleRt_HRIC_LGQ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1008)
)
_Hh3cevtModuleRt_HRIC_XP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HRIC_XP4 = _Hh3cevtModuleRt_HRIC_XP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1009)
)
_Hh3cevtModuleRt_RSU_300_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RSU_300 = _Hh3cevtModuleRt_RSU_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1010)
)
_Hh3cevtModuleRt_CR_19K_LPU_CQ06B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_CQ06B = _Hh3cevtModuleRt_CR_19K_LPU_CQ06B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1011)
)
_Hh3cevtModuleRt_CR_HIC_XP10_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_XP10 = _Hh3cevtModuleRt_CR_HIC_XP10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1012)
)
_Hh3cevtModuleRt_SIC_1SSD_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_1SSD = _Hh3cevtModuleRt_SIC_1SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1013)
)
_Hh3cevtModuleRtNSQM1AFC2000GDFGA0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM1AFC2000GDFGA0_Z = _Hh3cevtModuleRtNSQM1AFC2000GDFGA0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1014)
)
_Hh3cevtModuleRtNSQM2QG4GP40_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM2QG4GP40_Z = _Hh3cevtModuleRtNSQM2QG4GP40_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1015)
)
_Hh3cevtModuleRtNSQM1CGQ20_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM1CGQ20_Z = _Hh3cevtModuleRtNSQM1CGQ20_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1016)
)
_Hh3cevtModuleRtNSQM1FWDFGD1_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM1FWDFGD1_Z = _Hh3cevtModuleRtNSQM1FWDFGD1_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1017)
)
_Hh3cevtModuleRtNSQM1TGS32QSSG0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM1TGS32QSSG0_Z = _Hh3cevtModuleRtNSQM1TGS32QSSG0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1018)
)
_Hh3cevtModuleRtNSQM2TG16GP40_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM2TG16GP40_Z = _Hh3cevtModuleRtNSQM2TG16GP40_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1019)
)
_Hh3cevtModuleRtNSQM2TMPU12E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM2TMPU12E0 = _Hh3cevtModuleRtNSQM2TMPU12E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1020)
)
_Hh3cevtModuleRt_HMIM_4XP_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4XP = _Hh3cevtModuleRt_HMIM_4XP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1021)
)
_Hh3cevtModuleRt_SIC_1POS_STM1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_1POS_STM1 = _Hh3cevtModuleRt_SIC_1POS_STM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1022)
)
_Hh3cevtModuleRt_HMIM_4POS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_4POS = _Hh3cevtModuleRt_HMIM_4POS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1023)
)
_Hh3cevtModuleRt_NSQM1MPULB_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1MPULB = _Hh3cevtModuleRt_NSQM1MPULB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1024)
)
_Hh3cevtModuleRt_CR_LPU_CQ12B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_CQ12B = _Hh3cevtModuleRt_CR_LPU_CQ12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1025)
)
_Hh3cevtModuleRt_CR_LPU_CQ18_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_CQ18 = _Hh3cevtModuleRt_CR_LPU_CQ18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1026)
)
_Hh3cevtModuleRt_CR_MPU_20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_MPU_20A = _Hh3cevtModuleRt_CR_MPU_20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1027)
)
_Hh3cevtModuleRt_CR_HIC_CLP04_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_CLP04 = _Hh3cevtModuleRt_CR_HIC_CLP04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1028)
)
_Hh3cevtModuleRt_CR_SFU_08C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_SFU_08C = _Hh3cevtModuleRt_CR_SFU_08C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1029)
)
_Hh3cevtModuleRt_CR_HIC_PHP08_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_PHP08 = _Hh3cevtModuleRt_CR_HIC_PHP08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1030)
)
_Hh3cevtModuleRt_CR_MPU_08A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_MPU_08A = _Hh3cevtModuleRt_CR_MPU_08A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1031)
)
_Hh3cevtModuleRt_CR_HIC_XP12B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_XP12B = _Hh3cevtModuleRt_CR_HIC_XP12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1032)
)
_Hh3cevtModuleRt_CR_HIC_ET16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_ET16 = _Hh3cevtModuleRt_CR_HIC_ET16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1033)
)
_Hh3cevtModuleRt_CR_MSFU_08A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_MSFU_08A = _Hh3cevtModuleRt_CR_MSFU_08A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1034)
)
_Hh3cevtModuleRt_CR_SFU_20C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_SFU_20C = _Hh3cevtModuleRt_CR_SFU_20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1035)
)
_Hh3cevtModuleRt_SIC_M2_SATA_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_M2_SATA = _Hh3cevtModuleRt_SIC_M2_SATA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1036)
)
_Hh3cevtModuleRtNSQM1MPULC_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtNSQM1MPULC = _Hh3cevtModuleRtNSQM1MPULC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1037)
)
_Hh3cevtModuleRt_NSUM1QG1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSUM1QG1A = _Hh3cevtModuleRt_NSUM1QG1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1038)
)
_Hh3cevtModuleRt_NSUM1TG4A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSUM1TG4A = _Hh3cevtModuleRt_NSUM1TG4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1039)
)
_Hh3cevtModuleRt_NSUM1GP4A_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSUM1GP4A = _Hh3cevtModuleRt_NSUM1GP4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1040)
)
_Hh3cevtModuleRt_FIP_30_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_FIP_30 = _Hh3cevtModuleRt_FIP_30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1041)
)
_Hh3cevtModuleRt_RISER_FHFL_X16_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RISER_FHFL_X16 = _Hh3cevtModuleRt_RISER_FHFL_X16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1042)
)
_Hh3cevtModuleRt_RISER_GPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RISER_GPU = _Hh3cevtModuleRt_RISER_GPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1043)
)
_Hh3cevtModuleRt_RISER_RAID_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RISER_RAID = _Hh3cevtModuleRt_RISER_RAID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1044)
)
_Hh3cevtModuleRt_CR_19K_LPU_8004_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_LPU_8004 = _Hh3cevtModuleRt_CR_19K_LPU_8004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1045)
)
_Hh3cevtModuleRt_CR_19K_MPU_08B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MPU_08B = _Hh3cevtModuleRt_CR_19K_MPU_08B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1046)
)
_Hh3cevtModuleRt_CR_HIC_CQ02_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_CQ02 = _Hh3cevtModuleRt_CR_HIC_CQ02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1047)
)
_Hh3cevtModuleRt_NSQM1ISPAXA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1ISPAXA1 = _Hh3cevtModuleRt_NSQM1ISPAXA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1048)
)
_Hh3cevtModuleRt_NSQM1ISPAXB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1ISPAXB1 = _Hh3cevtModuleRt_NSQM1ISPAXB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1049)
)
_Hh3cevtModuleRt_CR_USBDISK_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_USBDISK = _Hh3cevtModuleRt_CR_USBDISK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1050)
)
_Hh3cevtModuleRt_SIC_4RS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_4RS = _Hh3cevtModuleRt_SIC_4RS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1051)
)
_Hh3cevtModuleRt_NSQM1MPULC_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1MPULC_Z = _Hh3cevtModuleRt_NSQM1MPULC_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1052)
)
_Hh3cevtModuleRt_CR_18K_MPU_16B_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_18K_MPU_16B = _Hh3cevtModuleRt_CR_18K_MPU_16B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1053)
)
_Hh3cevtModuleRt_CR_18K_SFU_16C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_18K_SFU_16C = _Hh3cevtModuleRt_CR_18K_SFU_16C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1054)
)
_Hh3cevtModuleRt_DS_3RH_4T_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_DS_3RH_4T = _Hh3cevtModuleRt_DS_3RH_4T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1055)
)
_Hh3cevtModuleRt_HRIC_CQ1F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HRIC_CQ1F = _Hh3cevtModuleRt_HRIC_CQ1F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1056)
)
_Hh3cevtModuleRt_HRIC_LGQ2F_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HRIC_LGQ2F = _Hh3cevtModuleRt_HRIC_LGQ2F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1057)
)
_Hh3cevtModuleRt_CR_HIC_CLGQ04_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_HIC_CLGQ04 = _Hh3cevtModuleRt_CR_HIC_CLGQ04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1058)
)
_Hh3cevtModuleRt_NSQM1QG1A_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1QG1A_Z = _Hh3cevtModuleRt_NSQM1QG1A_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1059)
)
_Hh3cevtModuleRt_NSQM1TG4A_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1TG4A_Z = _Hh3cevtModuleRt_NSQM1TG4A_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1060)
)
_Hh3cevtModuleRt_NSQM1GP4A_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_NSQM1GP4A_Z = _Hh3cevtModuleRt_NSQM1GP4A_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1061)
)
_Hh3cevtModuleRt_CR_LPU_8004_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_LPU_8004 = _Hh3cevtModuleRt_CR_LPU_8004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1062)
)
_Hh3cevtModuleRt_MPU_100_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_MPU_100_G = _Hh3cevtModuleRt_MPU_100_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1063)
)
_Hh3cevtModuleRt_SPU_300_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SPU_300_G = _Hh3cevtModuleRt_SPU_300_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1064)
)
_Hh3cevtModuleRt_CR_19K_MPU_20C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_19K_MPU_20C = _Hh3cevtModuleRt_CR_19K_MPU_20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1065)
)
_Hh3cevtModuleRt_CR_18K_MPU_16C_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_CR_18K_MPU_16C = _Hh3cevtModuleRt_CR_18K_MPU_16C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1066)
)
_Hh3cevtModuleRt_SIC_5G_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_SIC_5G = _Hh3cevtModuleRt_SIC_5G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1067)
)
_Hh3cevtModuleRt_RSU_400_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_RSU_400 = _Hh3cevtModuleRt_RSU_400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1068)
)
_Hh3cevtModuleRt_HRIC_XP8_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HRIC_XP8_H = _Hh3cevtModuleRt_HRIC_XP8_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1069)
)
_Hh3cevtModuleRt_BBU3120_MCBM2LMCMB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_BBU3120_MCBM2LMCMB1 = _Hh3cevtModuleRt_BBU3120_MCBM2LMCMB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1072)
)
_Hh3cevtModuleRt_BBU3120_MCBM2LBBMB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_BBU3120_MCBM2LBBMB1 = _Hh3cevtModuleRt_BBU3120_MCBM2LBBMB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1073)
)
_Hh3cevtModuleRt_HMIM_2POS_ObjectIdentity = ObjectIdentity
hh3cevtModuleRt_HMIM_2POS = _Hh3cevtModuleRt_HMIM_2POS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 1074)
)
_HpevtModuleRt_SIC_EPRI_ObjectIdentity = ObjectIdentity
hpevtModuleRt_SIC_EPRI = _HpevtModuleRt_SIC_EPRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5000)
)
_HpevtModuleRt_MIM_1E1_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_1E1_V2 = _HpevtModuleRt_MIM_1E1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5001)
)
_HpevtModuleRt_MIM_1E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_1E1_F_V2 = _HpevtModuleRt_MIM_1E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5002)
)
_HpevtModuleRt_MIM_2E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_2E1_F_V2 = _HpevtModuleRt_MIM_2E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5003)
)
_HpevtModuleRt_MIM_4E1_F_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_4E1_F_V2 = _HpevtModuleRt_MIM_4E1_F_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5004)
)
_HpevtModuleRt_MIM_8E1_75_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8E1_75 = _HpevtModuleRt_MIM_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5005)
)
_HpevtModuleRt_MIM_8E1_75_F_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8E1_75_F = _HpevtModuleRt_MIM_8E1_75_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5006)
)
_HpevtModuleRt_MIM_8T1_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8T1 = _HpevtModuleRt_MIM_8T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5007)
)
_HpevtModuleRt_MIM_8T1_F_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_8T1_F = _HpevtModuleRt_MIM_8T1_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5008)
)
_HpevtModuleRt_MIM_IMA_8E1_75_ObjectIdentity = ObjectIdentity
hpevtModuleRt_MIM_IMA_8E1_75 = _HpevtModuleRt_MIM_IMA_8E1_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5009)
)
_HpevtModuleRt_FIC_2E1_V3_ObjectIdentity = ObjectIdentity
hpevtModuleRt_FIC_2E1_V3 = _HpevtModuleRt_FIC_2E1_V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5010)
)
_HpevtModuleRt_FIC_IMA_8T1_V2_ObjectIdentity = ObjectIdentity
hpevtModuleRt_FIC_IMA_8T1_V2 = _HpevtModuleRt_FIC_IMA_8T1_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5011)
)
_Hh3cevtModuleRtCN_MSU_X3_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtCN_MSU_X3 = _Hh3cevtModuleRtCN_MSU_X3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5012)
)
_Hh3cevtModuleRtCN_FSP_660_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtCN_FSP_660 = _Hh3cevtModuleRtCN_FSP_660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5013)
)
_Hh3cevtModuleRtCN_MIC_X_XP4W_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtCN_MIC_X_XP4W = _Hh3cevtModuleRtCN_MIC_X_XP4W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5014)
)
_Hh3cevtModuleRtCN_MIC_X_GP8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtCN_MIC_X_GP8 = _Hh3cevtModuleRtCN_MIC_X_GP8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5015)
)
_Hh3cevtModuleRtCN_MIC_X_GT8_ObjectIdentity = ObjectIdentity
hh3cevtModuleRtCN_MIC_X_GT8 = _Hh3cevtModuleRtCN_MIC_X_GT8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 3, 5016)
)
_Hh3cevtModuleSwitchType_ObjectIdentity = ObjectIdentity
hh3cevtModuleSwitchType = _Hh3cevtModuleSwitchType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4)
)
_Hh3cevtModuleSw_10OR100M_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_10OR100M = _Hh3cevtModuleSw_10OR100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1)
)
_Hh3cevtModuleSw_1000BASE_LX_SM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LX_SM = _Hh3cevtModuleSw_1000BASE_LX_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2)
)
_Hh3cevtModuleSw_1000BASE_SX_MM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_SX_MM = _Hh3cevtModuleSw_1000BASE_SX_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 3)
)
_Hh3cevtModuleSw_1000BASE_TX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_TX = _Hh3cevtModuleSw_1000BASE_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 4)
)
_Hh3cevtModuleSw_100M_SINGLEMODE_FX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_SINGLEMODE_FX = _Hh3cevtModuleSw_100M_SINGLEMODE_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 5)
)
_Hh3cevtModuleSw_100M_MULTIMODE_FX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_MULTIMODE_FX = _Hh3cevtModuleSw_100M_MULTIMODE_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 6)
)
_Hh3cevtModuleSw_100M_100BASE_TX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_100BASE_TX = _Hh3cevtModuleSw_100M_100BASE_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 7)
)
_Hh3cevtModuleSw_100M_HUB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_HUB = _Hh3cevtModuleSw_100M_HUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 8)
)
_Hh3cevtModuleSw_VDSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_VDSL = _Hh3cevtModuleSw_VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 9)
)
_Hh3cevtModuleSw_STACK_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_STACK = _Hh3cevtModuleSw_STACK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 10)
)
_Hh3cevtModuleSw_1000BASE_ZENITH_FX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_ZENITH_FX = _Hh3cevtModuleSw_1000BASE_ZENITH_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 11)
)
_Hh3cevtModuleSw_1000BASE_LONG_FX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LONG_FX = _Hh3cevtModuleSw_1000BASE_LONG_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 12)
)
_Hh3cevtModuleSw_ADSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_ADSL = _Hh3cevtModuleSw_ADSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 13)
)
_Hh3cevtModuleSw_4T10OR100_4FX100SM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_4T10OR100_4FX100SM = _Hh3cevtModuleSw_4T10OR100_4FX100SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 14)
)
_Hh3cevtModuleSw_4T10OR100_4FX100MM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_4T10OR100_4FX100MM = _Hh3cevtModuleSw_4T10OR100_4FX100MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 15)
)
_Hh3cevtModuleSw_VSPL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_VSPL = _Hh3cevtModuleSw_VSPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 16)
)
_Hh3cevtModuleSw_ASPL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_ASPL = _Hh3cevtModuleSw_ASPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 17)
)
_Hh3cevtModuleSw_1000M_SFP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000M_SFP = _Hh3cevtModuleSw_1000M_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 18)
)
_Hh3cevtModuleSw_LS82O2CM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82O2CM = _Hh3cevtModuleSw_LS82O2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 19)
)
_Hh3cevtModuleSw_LS82P2CM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82P2CM = _Hh3cevtModuleSw_LS82P2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 20)
)
_Hh3cevtModuleSw_LS82O4GM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82O4GM = _Hh3cevtModuleSw_LS82O4GM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 21)
)
_Hh3cevtModuleSw_LS82GB4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82GB4C = _Hh3cevtModuleSw_LS82GB4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 22)
)
_Hh3cevtModuleSw_LS82GT4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82GT4C = _Hh3cevtModuleSw_LS82GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 23)
)
_Hh3cevtModuleSw_LS82ST4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82ST4C = _Hh3cevtModuleSw_LS82ST4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 24)
)
_Hh3cevtModuleSw_BOARD_LS82DSPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82DSPU = _Hh3cevtModuleSw_BOARD_LS82DSPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 25)
)
_Hh3cevtModuleSw_BOARD_LS81GP8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81GP8U = _Hh3cevtModuleSw_BOARD_LS81GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 26)
)
_Hh3cevtModuleSw_BOARD_LS82GT20_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82GT20 = _Hh3cevtModuleSw_BOARD_LS82GT20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 27)
)
_Hh3cevtModuleSw_BOARD_LS82FE48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82FE48 = _Hh3cevtModuleSw_BOARD_LS82FE48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 28)
)
_Hh3cevtModuleSw_LS82T24B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82T24B = _Hh3cevtModuleSw_LS82T24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 29)
)
_Hh3cevtModuleSw_LSB1SRPA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRPA = _Hh3cevtModuleSw_LSB1SRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 30)
)
_Hh3cevtModuleSw_LSB1FT48A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FT48A = _Hh3cevtModuleSw_LSB1FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 31)
)
_Hh3cevtModuleSw_LSB1FT48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FT48B = _Hh3cevtModuleSw_LSB1FT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 32)
)
_Hh3cevtModuleSw_LSB1F48GA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F48GA = _Hh3cevtModuleSw_LSB1F48GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 33)
)
_Hh3cevtModuleSw_LSB1F48GB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F48GB = _Hh3cevtModuleSw_LSB1F48GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 34)
)
_Hh3cevtModuleSw_LSB1FP20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FP20A = _Hh3cevtModuleSw_LSB1FP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 35)
)
_Hh3cevtModuleSw_LSB1FP20B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FP20B = _Hh3cevtModuleSw_LSB1FP20B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 36)
)
_Hh3cevtModuleSw_FT48A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_FT48A = _Hh3cevtModuleSw_FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 37)
)
_Hh3cevtModuleSw_GP4U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GP4U = _Hh3cevtModuleSw_GP4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 38)
)
_Hh3cevtModuleSw_GP2U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GP2U = _Hh3cevtModuleSw_GP2U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 39)
)
_Hh3cevtModuleSw_TGX1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_TGX1A = _Hh3cevtModuleSw_TGX1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 40)
)
_Hh3cevtModuleSw_1000BASE_LX_SM_IR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LX_SM_IR_SC = _Hh3cevtModuleSw_1000BASE_LX_SM_IR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 41)
)
_Hh3cevtModuleSw_1000BASE_SX_MM_SR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_SX_MM_SR_SC = _Hh3cevtModuleSw_1000BASE_SX_MM_SR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 42)
)
_Hh3cevtModuleSw_1000BASE_T_RJ45_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_T_RJ45 = _Hh3cevtModuleSw_1000BASE_T_RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 43)
)
_Hh3cevtModuleSw_100BASE_FX_SM_IR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100BASE_FX_SM_IR_SC = _Hh3cevtModuleSw_100BASE_FX_SM_IR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 44)
)
_Hh3cevtModuleSw_100BASE_FX_MM_SR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100BASE_FX_MM_SR_SC = _Hh3cevtModuleSw_100BASE_FX_MM_SR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 45)
)
_Hh3cevtModuleSw_GIGA_STACK_1M_PC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GIGA_STACK_1M_PC = _Hh3cevtModuleSw_GIGA_STACK_1M_PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 46)
)
_Hh3cevtModuleSw_1000BASE_LX_SM_VLR_LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LX_SM_VLR_LC = _Hh3cevtModuleSw_1000BASE_LX_SM_VLR_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 47)
)
_Hh3cevtModuleSw_1000BASE_LX_SM_LR_LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_LX_SM_LR_LC = _Hh3cevtModuleSw_1000BASE_LX_SM_LR_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 48)
)
_Hh3cevtModuleSw_100BASE_FX_SM_LR_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100BASE_FX_SM_LR_SC = _Hh3cevtModuleSw_100BASE_FX_SM_LR_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 49)
)
_Hh3cevtModuleSw_1000BASE_X_GBIC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_X_GBIC = _Hh3cevtModuleSw_1000BASE_X_GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 50)
)
_Hh3cevtModuleSw_100M_SINGLEMODE_FX_LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_SINGLEMODE_FX_LC = _Hh3cevtModuleSw_100M_SINGLEMODE_FX_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 51)
)
_Hh3cevtModuleSw_100M_MULTIMODE_FX_LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_MULTIMODE_FX_LC = _Hh3cevtModuleSw_100M_MULTIMODE_FX_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 52)
)
_Hh3cevtModuleSw_1000BASE_4SFP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_4SFP = _Hh3cevtModuleSw_1000BASE_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 53)
)
_Hh3cevtModuleSw_1000BASE_4GBIC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_4GBIC = _Hh3cevtModuleSw_1000BASE_4GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 54)
)
_Hh3cevtModuleSw_1000BASE_FIXED_4SFP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_FIXED_4SFP = _Hh3cevtModuleSw_1000BASE_FIXED_4SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 55)
)
_Hh3cevtModuleSw_1000BASE_FIXED_4GBIC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_FIXED_4GBIC = _Hh3cevtModuleSw_1000BASE_FIXED_4GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 56)
)
_Hh3cevtModuleSw_LSB1GP12A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12A = _Hh3cevtModuleSw_LSB1GP12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 57)
)
_Hh3cevtModuleSw_LSB1GP12B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12B = _Hh3cevtModuleSw_LSB1GP12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 58)
)
_Hh3cevtModuleSw_LSB1TGX1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1TGX1A = _Hh3cevtModuleSw_LSB1TGX1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 59)
)
_Hh3cevtModuleSw_LSB1TGX1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1TGX1B = _Hh3cevtModuleSw_LSB1TGX1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 60)
)
_Hh3cevtModuleSw_LSB1P4G8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1P4G8A = _Hh3cevtModuleSw_LSB1P4G8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 61)
)
_Hh3cevtModuleSw_LSB1P4G8B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1P4G8B = _Hh3cevtModuleSw_LSB1P4G8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 62)
)
_Hh3cevtModuleSw_LSB1A4G8A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1A4G8A = _Hh3cevtModuleSw_LSB1A4G8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 63)
)
_Hh3cevtModuleSw_LSB1A4G8B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1A4G8B = _Hh3cevtModuleSw_LSB1A4G8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 64)
)
_Hh3cevtModuleSw_FT48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_FT48C = _Hh3cevtModuleSw_FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 65)
)
_Hh3cevtModuleSw_FP20_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_FP20 = _Hh3cevtModuleSw_FP20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 66)
)
_Hh3cevtModuleSw_BOARD_LS81FT48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81FT48 = _Hh3cevtModuleSw_BOARD_LS81FT48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 67)
)
_Hh3cevtModuleSw_BOARD_LS81GB8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81GB8U = _Hh3cevtModuleSw_BOARD_LS81GB8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 68)
)
_Hh3cevtModuleSw_BOARD_LS81GT8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81GT8U = _Hh3cevtModuleSw_BOARD_LS81GT8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 69)
)
_Hh3cevtModuleSw_BOARD_LS81FS24_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81FS24 = _Hh3cevtModuleSw_BOARD_LS81FS24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 70)
)
_Hh3cevtModuleSw_BOARD_LS81FM24_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS81FM24 = _Hh3cevtModuleSw_BOARD_LS81FM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 71)
)
_Hh3cevtModuleSw_BOARD_LS82GP20_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82GP20 = _Hh3cevtModuleSw_BOARD_LS82GP20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 72)
)
_Hh3cevtModuleSw_LSB1SRPB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRPB = _Hh3cevtModuleSw_LSB1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 73)
)
_Hh3cevtModuleSw_LSB1F32GA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F32GA = _Hh3cevtModuleSw_LSB1F32GA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 74)
)
_Hh3cevtModuleSw_LSB1F32GB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F32GB = _Hh3cevtModuleSw_LSB1F32GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 75)
)
_Hh3cevtModuleSw_LSB2FT48A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FT48A = _Hh3cevtModuleSw_LSB2FT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 76)
)
_Hh3cevtModuleSw_LSB2FT48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FT48B = _Hh3cevtModuleSw_LSB2FT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 77)
)
_Hh3cevtModuleSw_LSB1GT12A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12A = _Hh3cevtModuleSw_LSB1GT12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 78)
)
_Hh3cevtModuleSw_LSB1GT12B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12B = _Hh3cevtModuleSw_LSB1GT12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 79)
)
_Hh3cevtModuleSw_PC4U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PC4U = _Hh3cevtModuleSw_PC4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 80)
)
_Hh3cevtModuleSw_FT32A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_FT32A = _Hh3cevtModuleSw_FT32A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 81)
)
_Hh3cevtModuleSw_GT4U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GT4U = _Hh3cevtModuleSw_GT4U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 82)
)
_Hh3cevtModuleSw_BOARD_LS83FP20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS83FP20A = _Hh3cevtModuleSw_BOARD_LS83FP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 83)
)
_Hh3cevtModuleSw_BOARD_LS82HGMU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82HGMU = _Hh3cevtModuleSw_BOARD_LS82HGMU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 84)
)
_Hh3cevtModuleSw_LSB1GP8TB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP8TB = _Hh3cevtModuleSw_LSB1GP8TB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 85)
)
_Hh3cevtModuleSw_LSB1GP8TC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP8TC = _Hh3cevtModuleSw_LSB1GP8TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 86)
)
_Hh3cevtModuleSw_LSB1GT8PB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT8PB = _Hh3cevtModuleSw_LSB1GT8PB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 87)
)
_Hh3cevtModuleSw_LSB1GT8PC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT8PC = _Hh3cevtModuleSw_LSB1GT8PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 88)
)
_Hh3cevtModuleSw_LSB1FT48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FT48C = _Hh3cevtModuleSw_LSB1FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 89)
)
_Hh3cevtModuleSw_LSB1FP20C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FP20C = _Hh3cevtModuleSw_LSB1FP20C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 90)
)
_Hh3cevtModuleSw_LSB1F32GC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F32GC = _Hh3cevtModuleSw_LSB1F32GC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 91)
)
_Hh3cevtModuleSw_LSB1GT12C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12C = _Hh3cevtModuleSw_LSB1GT12C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 92)
)
_Hh3cevtModuleSw_LSB1GP12C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12C = _Hh3cevtModuleSw_LSB1GP12C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 93)
)
_Hh3cevtModuleSw_LSB1P4G8C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1P4G8C = _Hh3cevtModuleSw_LSB1P4G8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 94)
)
_Hh3cevtModuleSw_LSB1TGX1C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1TGX1C = _Hh3cevtModuleSw_LSB1TGX1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 95)
)
_Hh3cevtModuleSw_LSB1GT24B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT24B = _Hh3cevtModuleSw_LSB1GT24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 96)
)
_Hh3cevtModuleSw_LSB1GT24C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT24C = _Hh3cevtModuleSw_LSB1GT24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 97)
)
_Hh3cevtModuleSw_LSB1GP24B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24B = _Hh3cevtModuleSw_LSB1GP24B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 98)
)
_Hh3cevtModuleSw_LSB1GP24C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24C = _Hh3cevtModuleSw_LSB1GP24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 99)
)
_Hh3cevtModuleSw_LSB1XP2B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2B = _Hh3cevtModuleSw_LSB1XP2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 100)
)
_Hh3cevtModuleSw_LSB1XP2C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2C = _Hh3cevtModuleSw_LSB1XP2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 101)
)
_Hh3cevtModuleSw_LSB1GV48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GV48B = _Hh3cevtModuleSw_LSB1GV48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 102)
)
_Hh3cevtModuleSw_LSB1GV48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GV48C = _Hh3cevtModuleSw_LSB1GV48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 103)
)
_Hh3cevtModuleSw_LSB1SRPC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRPC = _Hh3cevtModuleSw_LSB1SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 104)
)
_Hh3cevtModuleSw_LSB1SRP1N0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N0 = _Hh3cevtModuleSw_LSB1SRP1N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 105)
)
_Hh3cevtModuleSw_LSB1SRP1N1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N1 = _Hh3cevtModuleSw_LSB1SRP1N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 106)
)
_Hh3cevtModuleSw_LSB1SRP1N2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N2 = _Hh3cevtModuleSw_LSB1SRP1N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 107)
)
_Hh3cevtModuleSw_GT24_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GT24 = _Hh3cevtModuleSw_GT24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 108)
)
_Hh3cevtModuleSw_GP24_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GP24 = _Hh3cevtModuleSw_GP24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 109)
)
_Hh3cevtModuleSw_XP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_XP2 = _Hh3cevtModuleSw_XP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 110)
)
_Hh3cevtModuleSw_GV48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GV48 = _Hh3cevtModuleSw_GV48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 111)
)
_Hh3cevtModuleSw_LSG1GP8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSG1GP8U = _Hh3cevtModuleSw_LSG1GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 112)
)
_Hh3cevtModuleSw_LSG1GT8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSG1GT8U = _Hh3cevtModuleSw_LSG1GT8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 113)
)
_Hh3cevtModuleSw_LSG1TG1U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSG1TG1U = _Hh3cevtModuleSw_LSG1TG1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 114)
)
_Hh3cevtModuleSw_LSG1TD1U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSG1TD1U = _Hh3cevtModuleSw_LSG1TD1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 115)
)
_Hh3cevtModuleSw_LSB2FT48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FT48C = _Hh3cevtModuleSw_LSB2FT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 116)
)
_Hh3cevtModuleSw_LSB1GT48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT48B = _Hh3cevtModuleSw_LSB1GT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 117)
)
_Hh3cevtModuleSw_LSB1GT48C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT48C = _Hh3cevtModuleSw_LSB1GT48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 118)
)
_Hh3cevtModuleSw_LS81GT48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT48 = _Hh3cevtModuleSw_LS81GT48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 119)
)
_Hh3cevtModuleSw_LS81SRPG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG0 = _Hh3cevtModuleSw_LS81SRPG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 120)
)
_Hh3cevtModuleSw_LS81SRPG1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG1 = _Hh3cevtModuleSw_LS81SRPG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 121)
)
_Hh3cevtModuleSw_LS81SRPG2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG2 = _Hh3cevtModuleSw_LS81SRPG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 122)
)
_Hh3cevtModuleSw_LS81SRPG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG3 = _Hh3cevtModuleSw_LS81SRPG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 123)
)
_Hh3cevtModuleSw_SR01SRPUB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUB = _Hh3cevtModuleSw_SR01SRPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 125)
)
_Hh3cevtModuleSw_SR01SRPUA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUA = _Hh3cevtModuleSw_SR01SRPUA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 126)
)
_Hh3cevtModuleSw_SR01GP12L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP12L = _Hh3cevtModuleSw_SR01GP12L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 127)
)
_Hh3cevtModuleSw_SR01GP12W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP12W = _Hh3cevtModuleSw_SR01GP12W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 128)
)
_Hh3cevtModuleSw_SR01FT48L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FT48L = _Hh3cevtModuleSw_SR01FT48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 129)
)
_Hh3cevtModuleSw_SR01FT48W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FT48W = _Hh3cevtModuleSw_SR01FT48W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 130)
)
_Hh3cevtModuleSw_SR01XK1W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XK1W = _Hh3cevtModuleSw_SR01XK1W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 131)
)
_Hh3cevtModuleSw_SR01FP20W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FP20W = _Hh3cevtModuleSw_SR01FP20W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 132)
)
_Hh3cevtModuleSw_SR01GT12W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT12W = _Hh3cevtModuleSw_SR01GT12W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 133)
)
_Hh3cevtModuleSw_SR01F32GL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01F32GL = _Hh3cevtModuleSw_SR01F32GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 134)
)
_Hh3cevtModuleSw_SR01F32GW_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01F32GW = _Hh3cevtModuleSw_SR01F32GW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 135)
)
_Hh3cevtModuleSw_SR01GT8PL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT8PL = _Hh3cevtModuleSw_SR01GT8PL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 136)
)
_Hh3cevtModuleSw_SR01GT8PW_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT8PW = _Hh3cevtModuleSw_SR01GT8PW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 137)
)
_Hh3cevtModuleSw_SR01P4G8W_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01P4G8W = _Hh3cevtModuleSw_SR01P4G8W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 138)
)
_Hh3cevtModuleSw_LSA1FP8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSA1FP8U = _Hh3cevtModuleSw_LSA1FP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 139)
)
_Hh3cevtModuleSw_LSB1SP4B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SP4B = _Hh3cevtModuleSw_LSB1SP4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 140)
)
_Hh3cevtModuleSw_LSB1SP4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SP4C = _Hh3cevtModuleSw_LSB1SP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 141)
)
_Hh3cevtModuleSw_LSB1UP1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1UP1B = _Hh3cevtModuleSw_LSB1UP1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 142)
)
_Hh3cevtModuleSw_LSB1UP1C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1UP1C = _Hh3cevtModuleSw_LSB1UP1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 143)
)
_Hh3cevtModuleSw_LSB1XP4B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4B = _Hh3cevtModuleSw_LSB1XP4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 144)
)
_Hh3cevtModuleSw_LSB1XP4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4C = _Hh3cevtModuleSw_LSB1XP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 145)
)
_Hh3cevtModuleSw_SP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SP4 = _Hh3cevtModuleSw_SP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 146)
)
_Hh3cevtModuleSw_UP1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_UP1 = _Hh3cevtModuleSw_UP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 147)
)
_Hh3cevtModuleSw_XP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_XP4 = _Hh3cevtModuleSw_XP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 148)
)
_Hh3cevtModuleSw_LS81VSNP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81VSNP = _Hh3cevtModuleSw_LS81VSNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 149)
)
_Hh3cevtModuleSw_LS81T12P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81T12P = _Hh3cevtModuleSw_LS81T12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 150)
)
_Hh3cevtModuleSw_LS81P12T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81P12T = _Hh3cevtModuleSw_LS81P12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 151)
)
_Hh3cevtModuleSw_LS81GP8UB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP8UB = _Hh3cevtModuleSw_LS81GP8UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 152)
)
_Hh3cevtModuleSw_LS81FT48E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FT48E = _Hh3cevtModuleSw_LS81FT48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 153)
)
_Hh3cevtModuleSw_LS81GP4UB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP4UB = _Hh3cevtModuleSw_LS81GP4UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 154)
)
_Hh3cevtModuleSw_LS81GT8UE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT8UE = _Hh3cevtModuleSw_LS81GT8UE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 155)
)
_Hh3cevtModuleSw_LS81GT48A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT48A = _Hh3cevtModuleSw_LS81GT48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 156)
)
_Hh3cevtModuleSw_LS81FP48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FP48 = _Hh3cevtModuleSw_LS81FP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 157)
)
_Hh3cevtModuleSw_LSB1XK1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XK1B = _Hh3cevtModuleSw_LSB1XK1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 158)
)
_Hh3cevtModuleSw_LSB1XK1C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XK1C = _Hh3cevtModuleSw_LSB1XK1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 159)
)
_Hh3cevtModuleSw_SR01SRPUC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUC = _Hh3cevtModuleSw_SR01SRPUC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 160)
)
_Hh3cevtModuleSw_SR01SRPUD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUD = _Hh3cevtModuleSw_SR01SRPUD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 161)
)
_Hh3cevtModuleSw_SR01SRPUE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUE = _Hh3cevtModuleSw_SR01SRPUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 162)
)
_Hh3cevtModuleSw_LSB1SRP1N3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N3 = _Hh3cevtModuleSw_LSB1SRP1N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 163)
)
_Hh3cevtModuleSw_LSB1VP2B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1VP2B = _Hh3cevtModuleSw_LSB1VP2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 164)
)
_Hh3cevtModuleSw_LSB1NATB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1NATB = _Hh3cevtModuleSw_LSB1NATB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 165)
)
_Hh3cevtModuleSw_LSB1VPNB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1VPNB = _Hh3cevtModuleSw_LSB1VPNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 166)
)
_Hh3cevtModuleSw_LSGP8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSGP8P = _Hh3cevtModuleSw_LSGP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 167)
)
_Hh3cevtModuleSw_LSXK1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXK1P = _Hh3cevtModuleSw_LSXK1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 168)
)
_Hh3cevtModuleSw_LSXP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXP2P = _Hh3cevtModuleSw_LSXP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 169)
)
_Hh3cevtModuleSw_LS81FT48F_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FT48F = _Hh3cevtModuleSw_LS81FT48F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 170)
)
_Hh3cevtModuleSw_LS81PT8G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81PT8G = _Hh3cevtModuleSw_LS81PT8G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 171)
)
_Hh3cevtModuleSw_LS81PT4G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81PT4G = _Hh3cevtModuleSw_LS81PT4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 172)
)
_Hh3cevtModuleSw_LSSTK24G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSSTK24G = _Hh3cevtModuleSw_LSSTK24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 173)
)
_Hh3cevtModuleSw_LS82GT20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82GT20A = _Hh3cevtModuleSw_LS82GT20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 174)
)
_Hh3cevtModuleSw_LS82GP20A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82GP20A = _Hh3cevtModuleSw_LS82GP20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 175)
)
_Hh3cevtModuleSw_LS81TGX1C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX1C = _Hh3cevtModuleSw_LS81TGX1C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 176)
)
_Hh3cevtModuleSw_VP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_VP2 = _Hh3cevtModuleSw_VP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 177)
)
_Hh3cevtModuleSw_LSA1FB8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSA1FB8U = _Hh3cevtModuleSw_LSA1FB8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 178)
)
_Hh3cevtModuleSw_LS81T12PE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81T12PE = _Hh3cevtModuleSw_LS81T12PE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 179)
)
_Hh3cevtModuleSw_LS81P12TE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81P12TE = _Hh3cevtModuleSw_LS81P12TE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 180)
)
_Hh3cevtModuleSw_LSB1SRP2N0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N0 = _Hh3cevtModuleSw_LSB1SRP2N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 181)
)
_Hh3cevtModuleSw_LSB1SRP2N3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N3 = _Hh3cevtModuleSw_LSB1SRP2N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 182)
)
_Hh3cevtModuleSw_LSB1GV48DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GV48DB = _Hh3cevtModuleSw_LSB1GV48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 183)
)
_Hh3cevtModuleSw_LSB1FW8B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FW8B = _Hh3cevtModuleSw_LSB1FW8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 184)
)
_Hh3cevtModuleSw_LSB1IPSEC8B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IPSEC8B = _Hh3cevtModuleSw_LSB1IPSEC8B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 185)
)
_Hh3cevtModuleSw_LSB1IDSB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IDSB = _Hh3cevtModuleSw_LSB1IDSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 186)
)
_Hh3cevtModuleSw_LSB1IPSB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IPSB = _Hh3cevtModuleSw_LSB1IPSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 187)
)
_Hh3cevtModuleSw_LSB2FT48CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FT48CA = _Hh3cevtModuleSw_LSB2FT48CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 188)
)
_Hh3cevtModuleSw_LSB1FP20CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FP20CA = _Hh3cevtModuleSw_LSB1FP20CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 189)
)
_Hh3cevtModuleSw_LSB1F32GCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1F32GCA = _Hh3cevtModuleSw_LSB1F32GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 190)
)
_Hh3cevtModuleSw_LSB1P4G8CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1P4G8CA = _Hh3cevtModuleSw_LSB1P4G8CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 191)
)
_Hh3cevtModuleSw_LSB1GT12CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12CA = _Hh3cevtModuleSw_LSB1GT12CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 192)
)
_Hh3cevtModuleSw_LSB1GT24CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT24CA = _Hh3cevtModuleSw_LSB1GT24CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 193)
)
_Hh3cevtModuleSw_LSB1GP12CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12CA = _Hh3cevtModuleSw_LSB1GP12CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 194)
)
_Hh3cevtModuleSw_LSB1GP24CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24CA = _Hh3cevtModuleSw_LSB1GP24CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 195)
)
_Hh3cevtModuleSw_LSB1GT8PCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT8PCA = _Hh3cevtModuleSw_LSB1GT8PCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 196)
)
_Hh3cevtModuleSw_LSB1XP2CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2CA = _Hh3cevtModuleSw_LSB1XP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 197)
)
_Hh3cevtModuleSw_LSB1XK1CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XK1CA = _Hh3cevtModuleSw_LSB1XK1CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 198)
)
_Hh3cevtModuleSw_LSB1XP4CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4CA = _Hh3cevtModuleSw_LSB1XP4CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 199)
)
_Hh3cevtModuleSw_LSB1UP1CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1UP1CA = _Hh3cevtModuleSw_LSB1UP1CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 200)
)
_Hh3cevtModuleSw_LSB1SP4CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SP4CA = _Hh3cevtModuleSw_LSB1SP4CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 201)
)
_Hh3cevtModuleSw_LSB1VP2CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1VP2CA = _Hh3cevtModuleSw_LSB1VP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 202)
)
_Hh3cevtModuleSw_SR01FT48WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FT48WA = _Hh3cevtModuleSw_SR01FT48WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 203)
)
_Hh3cevtModuleSw_SR01FP20WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FP20WA = _Hh3cevtModuleSw_SR01FP20WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 204)
)
_Hh3cevtModuleSw_SR01F32GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01F32GWA = _Hh3cevtModuleSw_SR01F32GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 205)
)
_Hh3cevtModuleSw_SR01P4G8WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01P4G8WA = _Hh3cevtModuleSw_SR01P4G8WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 206)
)
_Hh3cevtModuleSw_SR01GT12WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT12WA = _Hh3cevtModuleSw_SR01GT12WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 207)
)
_Hh3cevtModuleSw_SR01GT24WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT24WA = _Hh3cevtModuleSw_SR01GT24WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 208)
)
_Hh3cevtModuleSw_SR01GP12WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP12WA = _Hh3cevtModuleSw_SR01GP12WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 209)
)
_Hh3cevtModuleSw_SR01GP24WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP24WA = _Hh3cevtModuleSw_SR01GP24WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 210)
)
_Hh3cevtModuleSw_SR01GT8PWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT8PWA = _Hh3cevtModuleSw_SR01GT8PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 211)
)
_Hh3cevtModuleSw_SR01XP2WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XP2WA = _Hh3cevtModuleSw_SR01XP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 212)
)
_Hh3cevtModuleSw_SR01XK1WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XK1WA = _Hh3cevtModuleSw_SR01XK1WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 213)
)
_Hh3cevtModuleSw_SR01UP1WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01UP1WA = _Hh3cevtModuleSw_SR01UP1WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 214)
)
_Hh3cevtModuleSw_SR01SP4WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SP4WA = _Hh3cevtModuleSw_SR01SP4WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 215)
)
_Hh3cevtModuleSw_GP8U_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_GP8U = _Hh3cevtModuleSw_GP8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 216)
)
_Hh3cevtModuleSw_LSEXP1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSEXP1P = _Hh3cevtModuleSw_LSEXP1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 217)
)
_Hh3cevtModuleSw_LSEXK1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSEXK1P = _Hh3cevtModuleSw_LSEXK1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 218)
)
_Hh3cevtModuleSw_LSEXS1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSEXS1P = _Hh3cevtModuleSw_LSEXS1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 219)
)
_Hh3cevtModuleSw_LS81GP48_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP48 = _Hh3cevtModuleSw_LS81GP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 220)
)
_Hh3cevtModuleSw_LS81GT48B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT48B = _Hh3cevtModuleSw_LS81GT48B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 221)
)
_Hh3cevtModuleSw_LS81T16P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81T16P = _Hh3cevtModuleSw_LS81T16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 222)
)
_Hh3cevtModuleSw_LS81T32P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81T32P = _Hh3cevtModuleSw_LS81T32P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 223)
)
_Hh3cevtModuleSw_LS81TGX2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX2 = _Hh3cevtModuleSw_LS81TGX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 224)
)
_Hh3cevtModuleSw_LS81TGX4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX4 = _Hh3cevtModuleSw_LS81TGX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 225)
)
_Hh3cevtModuleSw_LSB1GV48DA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GV48DA = _Hh3cevtModuleSw_LSB1GV48DA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 226)
)
_Hh3cevtModuleSw_SR01GV48VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GV48VB = _Hh3cevtModuleSw_SR01GV48VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 227)
)
_Hh3cevtModuleSw_LSB1GT24DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT24DB = _Hh3cevtModuleSw_LSB1GT24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 228)
)
_Hh3cevtModuleSw_LSB1GP24DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24DB = _Hh3cevtModuleSw_LSB1GP24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 229)
)
_Hh3cevtModuleSw_LSB1GP24DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24DC = _Hh3cevtModuleSw_LSB1GP24DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 230)
)
_Hh3cevtModuleSw_LSB1FW8DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FW8DB = _Hh3cevtModuleSw_LSB1FW8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 231)
)
_Hh3cevtModuleSw_LSB1IPSEC8DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IPSEC8DB = _Hh3cevtModuleSw_LSB1IPSEC8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 232)
)
_Hh3cevtModuleSw_SR01GT24VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GT24VB = _Hh3cevtModuleSw_SR01GT24VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 233)
)
_Hh3cevtModuleSw_SR01GP24VC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP24VC = _Hh3cevtModuleSw_SR01GP24VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 234)
)
_Hh3cevtModuleSw_SR01VP2WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01VP2WA = _Hh3cevtModuleSw_SR01VP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 235)
)
_Hh3cevtModuleSw_SR01FW8VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01FW8VB = _Hh3cevtModuleSw_SR01FW8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 236)
)
_Hh3cevtModuleSw_SR01IPSEC8VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01IPSEC8VB = _Hh3cevtModuleSw_SR01IPSEC8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 237)
)
_Hh3cevtModuleSw_SR01NATL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01NATL = _Hh3cevtModuleSw_SR01NATL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 238)
)
_Hh3cevtModuleSw_SR01VPNL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01VPNL = _Hh3cevtModuleSw_SR01VPNL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 239)
)
_Hh3cevtModuleSw_LSB1GP24CB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP24CB = _Hh3cevtModuleSw_LSB1GP24CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 240)
)
_Hh3cevtModuleSw_LSB1GP48DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP48DB = _Hh3cevtModuleSw_LSB1GP48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 241)
)
_Hh3cevtModuleSw_LSB1XP2CB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2CB = _Hh3cevtModuleSw_LSB1XP2CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 242)
)
_Hh3cevtModuleSw_XP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_XP4L = _Hh3cevtModuleSw_XP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 243)
)
_Hh3cevtModuleSw_LSB1XP4LDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4LDB = _Hh3cevtModuleSw_LSB1XP4LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 244)
)
_Hh3cevtModuleSw_LSB1XP4LDC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4LDC = _Hh3cevtModuleSw_LSB1XP4LDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 245)
)
_Hh3cevtModuleSw_AHP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_AHP4 = _Hh3cevtModuleSw_AHP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 246)
)
_Hh3cevtModuleSw_LSB1AHP4GCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1AHP4GCA = _Hh3cevtModuleSw_LSB1AHP4GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 247)
)
_Hh3cevtModuleSw_CLP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CLP4 = _Hh3cevtModuleSw_CLP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 248)
)
_Hh3cevtModuleSw_LSB1CLP4GCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1CLP4GCA = _Hh3cevtModuleSw_LSB1CLP4GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 249)
)
_Hh3cevtModuleSw_ET32_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_ET32 = _Hh3cevtModuleSw_ET32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 250)
)
_Hh3cevtModuleSw_LSB1ET32GCA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1ET32GCA = _Hh3cevtModuleSw_LSB1ET32GCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 251)
)
_Hh3cevtModuleSw_LSB1IDSDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IDSDB = _Hh3cevtModuleSw_LSB1IDSDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 252)
)
_Hh3cevtModuleSw_LSB1SRP2N1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N1 = _Hh3cevtModuleSw_LSB1SRP2N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 253)
)
_Hh3cevtModuleSw_BOARD_LS82SRPB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BOARD_LS82SRPB = _Hh3cevtModuleSw_BOARD_LS82SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 254)
)
_Hh3cevtModuleSw_BORAD_LS83SRPC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_BORAD_LS83SRPC = _Hh3cevtModuleSw_BORAD_LS83SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 255)
)
_Hh3cevtModuleSw_Main_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_Main = _Hh3cevtModuleSw_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 256)
)
_Hh3cevtModuleSw_LSB1SRP2N2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N2 = _Hh3cevtModuleSw_LSB1SRP2N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 257)
)
_Hh3cevtModuleSw_LSB1NAMB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1NAMB = _Hh3cevtModuleSw_LSB1NAMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 258)
)
_Hh3cevtModuleSw_RSP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RSP2 = _Hh3cevtModuleSw_RSP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 259)
)
_Hh3cevtModuleSw_LSB1RSP2CA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1RSP2CA = _Hh3cevtModuleSw_LSB1RSP2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 260)
)
_Hh3cevtModuleSw_SR01XP4LVC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XP4LVC = _Hh3cevtModuleSw_SR01XP4LVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 261)
)
_Hh3cevtModuleSw_SR01AHP4GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01AHP4GWA = _Hh3cevtModuleSw_SR01AHP4GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 262)
)
_Hh3cevtModuleSw_SR01CLP4GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01CLP4GWA = _Hh3cevtModuleSw_SR01CLP4GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 263)
)
_Hh3cevtModuleSw_SR01ET32GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01ET32GWA = _Hh3cevtModuleSw_SR01ET32GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 264)
)
_Hh3cevtModuleSw_SR01IDSVB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01IDSVB = _Hh3cevtModuleSw_SR01IDSVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 265)
)
_Hh3cevtModuleSw_SR01SRPUF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUF = _Hh3cevtModuleSw_SR01SRPUF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 266)
)
_Hh3cevtModuleSw_SR01NAML_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01NAML = _Hh3cevtModuleSw_SR01NAML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 267)
)
_Hh3cevtModuleSw_SR01RSP2WA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01RSP2WA = _Hh3cevtModuleSw_SR01RSP2WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 268)
)
_Hh3cevtModuleSw_LSPM1XP1P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM1XP1P = _Hh3cevtModuleSw_LSPM1XP1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 269)
)
_Hh3cevtModuleSw_LSPM1XP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM1XP2P = _Hh3cevtModuleSw_LSPM1XP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 270)
)
_Hh3cevtModuleSw_LSPM1CX2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM1CX2P = _Hh3cevtModuleSw_LSPM1CX2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 271)
)
_Hh3cevtModuleSw_STK_1000BASE_T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_STK_1000BASE_T = _Hh3cevtModuleSw_STK_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 272)
)
_Hh3cevtModuleSw_LSB1SRP1M0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1M0 = _Hh3cevtModuleSw_LSB1SRP1M0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 300)
)
_Hh3cevtModuleSw_LSB1SRP1M1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1M1 = _Hh3cevtModuleSw_LSB1SRP1M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 301)
)
_Hh3cevtModuleSw_LSB1GP12DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP12DB = _Hh3cevtModuleSw_LSB1GP12DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 302)
)
_Hh3cevtModuleSw_LSB1GT12DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT12DB = _Hh3cevtModuleSw_LSB1GT12DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 303)
)
_Hh3cevtModuleSw_LSB1XK1DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XK1DB = _Hh3cevtModuleSw_LSB1XK1DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 304)
)
_Hh3cevtModuleSw_LSB1XP2DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2DB = _Hh3cevtModuleSw_LSB1XP2DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 305)
)
_Hh3cevtModuleSw_LSB1XP2DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP2DC = _Hh3cevtModuleSw_LSB1XP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 306)
)
_Hh3cevtModuleSw_LSB1GT48LDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GT48LDB = _Hh3cevtModuleSw_LSB1GT48LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 307)
)
_Hh3cevtModuleSw_LSB1XP4TDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4TDB = _Hh3cevtModuleSw_LSB1XP4TDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 308)
)
_Hh3cevtModuleSw_LSB1XP4TDC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4TDC = _Hh3cevtModuleSw_LSB1XP4TDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 309)
)
_Hh3cevtModuleSw_LSB1RSP2DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1RSP2DC = _Hh3cevtModuleSw_LSB1RSP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 310)
)
_Hh3cevtModuleSw_LSB1VP2DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1VP2DC = _Hh3cevtModuleSw_LSB1VP2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 311)
)
_Hh3cevtModuleSw_LSB1XP4DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1XP4DB = _Hh3cevtModuleSw_LSB1XP4DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 312)
)
_Hh3cevtModuleSw_LSB1SRP2E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2E0 = _Hh3cevtModuleSw_LSB1SRP2E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 313)
)
_Hh3cevtModuleSw_LSB1SRP2E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2E1 = _Hh3cevtModuleSw_LSB1SRP2E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 314)
)
_Hh3cevtModuleSw_LSB1SRP2E2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2E2 = _Hh3cevtModuleSw_LSB1SRP2E2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 315)
)
_Hh3cevtModuleSw_LSB1SRP2E3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2E3 = _Hh3cevtModuleSw_LSB1SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 316)
)
_Hh3cevtModuleSw_SR01SRPUQ_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUQ = _Hh3cevtModuleSw_SR01SRPUQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 317)
)
_Hh3cevtModuleSw_AHP1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_AHP1 = _Hh3cevtModuleSw_AHP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 318)
)
_Hh3cevtModuleSw_AHP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_AHP2 = _Hh3cevtModuleSw_AHP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 319)
)
_Hh3cevtModuleSw_CLP1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CLP1 = _Hh3cevtModuleSw_CLP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 320)
)
_Hh3cevtModuleSw_CLP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CLP2 = _Hh3cevtModuleSw_CLP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 321)
)
_Hh3cevtModuleSw_ET16_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_ET16 = _Hh3cevtModuleSw_ET16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 322)
)
_Hh3cevtModuleSw_LSB1SRP1NA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA0 = _Hh3cevtModuleSw_LSB1SRP1NA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 323)
)
_Hh3cevtModuleSw_LSB1SRP1NA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA1 = _Hh3cevtModuleSw_LSB1SRP1NA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 324)
)
_Hh3cevtModuleSw_LSB1SRP1NA2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA2 = _Hh3cevtModuleSw_LSB1SRP1NA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 325)
)
_Hh3cevtModuleSw_LSB1SRP1NA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA3 = _Hh3cevtModuleSw_LSB1SRP1NA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 326)
)
_Hh3cevtModuleSw_SR01AHP1GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01AHP1GWA = _Hh3cevtModuleSw_SR01AHP1GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 327)
)
_Hh3cevtModuleSw_SR01AHP2GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01AHP2GWA = _Hh3cevtModuleSw_SR01AHP2GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 328)
)
_Hh3cevtModuleSw_SR01CLP1GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01CLP1GWA = _Hh3cevtModuleSw_SR01CLP1GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 329)
)
_Hh3cevtModuleSw_SR01CLP2GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01CLP2GWA = _Hh3cevtModuleSw_SR01CLP2GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 330)
)
_Hh3cevtModuleSw_SR01ET16GWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01ET16GWA = _Hh3cevtModuleSw_SR01ET16GWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 331)
)
_Hh3cevtModuleSw_SR01GP12VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01GP12VB = _Hh3cevtModuleSw_SR01GP12VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 332)
)
_Hh3cevtModuleSw_SR01XK1VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XK1VB = _Hh3cevtModuleSw_SR01XK1VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 333)
)
_Hh3cevtModuleSw_SR01XP2VC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XP2VC = _Hh3cevtModuleSw_SR01XP2VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 334)
)
_Hh3cevtModuleSw_SR01XP4LVB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01XP4LVB = _Hh3cevtModuleSw_SR01XP4LVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 335)
)
_Hh3cevtModuleSw_SR01SRPUEA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01SRPUEA = _Hh3cevtModuleSw_SR01SRPUEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 336)
)
_Hh3cevtModuleSw_LSB1SRP1N4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N4 = _Hh3cevtModuleSw_LSB1SRP1N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 337)
)
_Hh3cevtModuleSw_LSB1SRP1N5_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N5 = _Hh3cevtModuleSw_LSB1SRP1N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 338)
)
_Hh3cevtModuleSw_LSB1SRP1N6_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N6 = _Hh3cevtModuleSw_LSB1SRP1N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 339)
)
_Hh3cevtModuleSw_LSB1SRP1N7_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1N7 = _Hh3cevtModuleSw_LSB1SRP1N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 340)
)
_Hh3cevtModuleSw_LSB1SRP2N4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N4 = _Hh3cevtModuleSw_LSB1SRP2N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 341)
)
_Hh3cevtModuleSw_LSB1SRP2N5_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N5 = _Hh3cevtModuleSw_LSB1SRP2N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 342)
)
_Hh3cevtModuleSw_LSB1SRP2N6_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N6 = _Hh3cevtModuleSw_LSB1SRP2N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 343)
)
_Hh3cevtModuleSw_LSB1SRP2N7_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP2N7 = _Hh3cevtModuleSw_LSB1SRP2N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 344)
)
_Hh3cevtModuleSw_LSB1SRP1NA4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA4 = _Hh3cevtModuleSw_LSB1SRP1NA4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 345)
)
_Hh3cevtModuleSw_LSB1SRP1NA5_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA5 = _Hh3cevtModuleSw_LSB1SRP1NA5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 346)
)
_Hh3cevtModuleSw_LSB1SRP1NA6_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA6 = _Hh3cevtModuleSw_LSB1SRP1NA6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 347)
)
_Hh3cevtModuleSw_LSB1SRP1NA7_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SRP1NA7 = _Hh3cevtModuleSw_LSB1SRP1NA7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 348)
)
_Hh3cevtModuleSw_LSB2GV48DA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GV48DA = _Hh3cevtModuleSw_LSB2GV48DA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 349)
)
_Hh3cevtModuleSw_LSB1RGP2GDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1RGP2GDB = _Hh3cevtModuleSw_LSB1RGP2GDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 350)
)
_Hh3cevtModuleSw_LSB1RGP4GDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1RGP4GDB = _Hh3cevtModuleSw_LSB1RGP4GDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 351)
)
_Hh3cevtModuleSw_LSB2GP24DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GP24DB = _Hh3cevtModuleSw_LSB2GP24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 352)
)
_Hh3cevtModuleSw_LSB2GP24DC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GP24DC = _Hh3cevtModuleSw_LSB2GP24DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 353)
)
_Hh3cevtModuleSw_LSB2GT24DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GT24DB = _Hh3cevtModuleSw_LSB2GT24DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 354)
)
_Hh3cevtModuleSw_LSB2FW8DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2FW8DB = _Hh3cevtModuleSw_LSB2FW8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 355)
)
_Hh3cevtModuleSw_LSB2IPSEC8DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2IPSEC8DB = _Hh3cevtModuleSw_LSB2IPSEC8DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 356)
)
_Hh3cevtModuleSw_LSB2GV48DB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2GV48DB = _Hh3cevtModuleSw_LSB2GV48DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 357)
)
_Hh3cevtModuleSw_RGP2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RGP2 = _Hh3cevtModuleSw_RGP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 358)
)
_Hh3cevtModuleSw_RGP4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RGP4 = _Hh3cevtModuleSw_RGP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 359)
)
_Hh3cevtModuleSw_SR02FW8VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02FW8VB = _Hh3cevtModuleSw_SR02FW8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 360)
)
_Hh3cevtModuleSw_SR02IPSEC8VB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02IPSEC8VB = _Hh3cevtModuleSw_SR02IPSEC8VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 361)
)
_Hh3cevtModuleSw_LSB2SRP1N0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N0 = _Hh3cevtModuleSw_LSB2SRP1N0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 362)
)
_Hh3cevtModuleSw_LSB2SRP1N1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N1 = _Hh3cevtModuleSw_LSB2SRP1N1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 363)
)
_Hh3cevtModuleSw_LSB2SRP1N2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N2 = _Hh3cevtModuleSw_LSB2SRP1N2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 364)
)
_Hh3cevtModuleSw_LSB2SRP1N3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N3 = _Hh3cevtModuleSw_LSB2SRP1N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 365)
)
_Hh3cevtModuleSw_LSB2SRP1N4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N4 = _Hh3cevtModuleSw_LSB2SRP1N4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 366)
)
_Hh3cevtModuleSw_LSB2SRP1N5_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N5 = _Hh3cevtModuleSw_LSB2SRP1N5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 367)
)
_Hh3cevtModuleSw_LSB2SRP1N6_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N6 = _Hh3cevtModuleSw_LSB2SRP1N6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 368)
)
_Hh3cevtModuleSw_LSB2SRP1N7_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB2SRP1N7 = _Hh3cevtModuleSw_LSB2SRP1N7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 369)
)
_Hh3cevtModuleSw_SR02SRPUE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRPUE = _Hh3cevtModuleSw_SR02SRPUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 370)
)
_Hh3cevtModuleSw_SR01LN1BQH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01LN1BQH0 = _Hh3cevtModuleSw_SR01LN1BQH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 371)
)
_Hh3cevtModuleSw_SR01DXP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DXP1L = _Hh3cevtModuleSw_SR01DXP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 372)
)
_Hh3cevtModuleSw_SR01DGP10L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DGP10L = _Hh3cevtModuleSw_SR01DGP10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 373)
)
_Hh3cevtModuleSw_SR01DRSP2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DRSP2L = _Hh3cevtModuleSw_SR01DRSP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 374)
)
_Hh3cevtModuleSw_SR01DRUP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DRUP1L = _Hh3cevtModuleSw_SR01DRUP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 375)
)
_Hh3cevtModuleSw_SR01DGP20R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DGP20R = _Hh3cevtModuleSw_SR01DGP20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 376)
)
_Hh3cevtModuleSw_SR01DPLP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPLP8L = _Hh3cevtModuleSw_SR01DPLP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 377)
)
_Hh3cevtModuleSw_SR01DXP2R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DXP2R = _Hh3cevtModuleSw_SR01DXP2R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 378)
)
_Hh3cevtModuleSw_LSB1FW2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1FW2A0 = _Hh3cevtModuleSw_LSB1FW2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 379)
)
_Hh3cevtModuleSw_LSB1GP48LDB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1GP48LDB = _Hh3cevtModuleSw_LSB1GP48LDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 380)
)
_Hh3cevtModuleSw_SR01LN1BNA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01LN1BNA0 = _Hh3cevtModuleSw_SR01LN1BNA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 381)
)
_Hh3cevtModuleSw_SR01LN2BQH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01LN2BQH0 = _Hh3cevtModuleSw_SR01LN2BQH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 382)
)
_Hh3cevtModuleSw_SR01LN2BNA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01LN2BNA0 = _Hh3cevtModuleSw_SR01LN2BNA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 383)
)
_Hh3cevtModuleSw_SR01DGT20R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DGT20R = _Hh3cevtModuleSw_SR01DGT20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 384)
)
_Hh3cevtModuleSw_SR01DPSP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPSP4L = _Hh3cevtModuleSw_SR01DPSP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 385)
)
_Hh3cevtModuleSw_SR01DPUP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPUP1L = _Hh3cevtModuleSw_SR01DPUP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 386)
)
_Hh3cevtModuleSw_SR01DPL2G6L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPL2G6L = _Hh3cevtModuleSw_SR01DPL2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 387)
)
_Hh3cevtModuleSw_SR01DPH2G6L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPH2G6L = _Hh3cevtModuleSw_SR01DPH2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 388)
)
_Hh3cevtModuleSw_SR01DPS2G4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DPS2G4L = _Hh3cevtModuleSw_SR01DPS2G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 389)
)
_Hh3cevtModuleSw_SR01DCL1G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DCL1G8L = _Hh3cevtModuleSw_SR01DCL1G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 390)
)
_Hh3cevtModuleSw_SR01DCL2G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DCL2G8L = _Hh3cevtModuleSw_SR01DCL2G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 391)
)
_Hh3cevtModuleSw_SR01DET8G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DET8G8L = _Hh3cevtModuleSw_SR01DET8G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 392)
)
_Hh3cevtModuleSw_SR02SRP2E3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP2E3 = _Hh3cevtModuleSw_SR02SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 393)
)
_Hh3cevtModuleSw_SR02SRP1E3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP1E3 = _Hh3cevtModuleSw_SR02SRP1E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 394)
)
_Hh3cevtModuleSw_SR02SRP1M3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP1M3 = _Hh3cevtModuleSw_SR02SRP1M3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 395)
)
_Hh3cevtModuleSw_SR01DQCP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DQCP4L = _Hh3cevtModuleSw_SR01DQCP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 396)
)
_Hh3cevtModuleSw_SR01DTCP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DTCP8L = _Hh3cevtModuleSw_SR01DTCP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 397)
)
_Hh3cevtModuleSw_LSB1AFC1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1AFC1A0 = _Hh3cevtModuleSw_LSB1AFC1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 398)
)
_Hh3cevtModuleSw_LSB1SSL1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1SSL1A0 = _Hh3cevtModuleSw_LSB1SSL1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 399)
)
_Hh3cevtModuleSw_IMNAM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IMNAM = _Hh3cevtModuleSw_IMNAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 400)
)
_Hh3cevtModuleSw_IMNAT_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IMNAT = _Hh3cevtModuleSw_IMNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 401)
)
_Hh3cevtModuleSw_PICAHP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICAHP1L = _Hh3cevtModuleSw_PICAHP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 402)
)
_Hh3cevtModuleSw_PICALP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICALP4L = _Hh3cevtModuleSw_PICALP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 403)
)
_Hh3cevtModuleSw_PICCHP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICCHP4L = _Hh3cevtModuleSw_PICCHP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 404)
)
_Hh3cevtModuleSw_PICCHS1G4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICCHS1G4L = _Hh3cevtModuleSw_PICCHS1G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 405)
)
_Hh3cevtModuleSw_PICCLS4G4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICCLS4G4L = _Hh3cevtModuleSw_PICCLS4G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 406)
)
_Hh3cevtModuleSw_PICCSP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PICCSP1L = _Hh3cevtModuleSw_PICCSP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 407)
)
_Hh3cevtModuleSw_LSB1ACG1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1ACG1A0 = _Hh3cevtModuleSw_LSB1ACG1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 408)
)
_Hh3cevtModuleSw_LST1MRPNC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1MRPNC1 = _Hh3cevtModuleSw_LST1MRPNC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 409)
)
_Hh3cevtModuleSw_LST1SF18B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF18B1 = _Hh3cevtModuleSw_LST1SF18B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 410)
)
_Hh3cevtModuleSw_LST1SF08B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF08B1 = _Hh3cevtModuleSw_LST1SF08B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 411)
)
_Hh3cevtModuleSw_LST1GT48LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GT48LEC1 = _Hh3cevtModuleSw_LST1GT48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 412)
)
_Hh3cevtModuleSw_LST1GP48LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEC1 = _Hh3cevtModuleSw_LST1GP48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 413)
)
_Hh3cevtModuleSw_LST1XP4LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP4LEC1 = _Hh3cevtModuleSw_LST1XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 414)
)
_Hh3cevtModuleSw_LST1XP8LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEC1 = _Hh3cevtModuleSw_LST1XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 415)
)
_Hh3cevtModuleSw_LSR1SRP2B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2B1 = _Hh3cevtModuleSw_LSR1SRP2B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 416)
)
_Hh3cevtModuleSw_LSR1SRP2C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2C1 = _Hh3cevtModuleSw_LSR1SRP2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 417)
)
_Hh3cevtModuleSw_LSR1SRP2B2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2B2 = _Hh3cevtModuleSw_LSR1SRP2B2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 418)
)
_Hh3cevtModuleSw_LSR1SRP2C2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2C2 = _Hh3cevtModuleSw_LSR1SRP2C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 419)
)
_Hh3cevtModuleSw_LSR1GT24LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GT24LEC1 = _Hh3cevtModuleSw_LSR1GT24LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 420)
)
_Hh3cevtModuleSw_LSR1GP24LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP24LEB1 = _Hh3cevtModuleSw_LSR1GP24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 421)
)
_Hh3cevtModuleSw_LSR1GP24LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP24LEC1 = _Hh3cevtModuleSw_LSR1GP24LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 422)
)
_Hh3cevtModuleSw_LSR1GT48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GT48LEB1 = _Hh3cevtModuleSw_LSR1GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 423)
)
_Hh3cevtModuleSw_LSR1GT48LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GT48LEC1 = _Hh3cevtModuleSw_LSR1GT48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 424)
)
_Hh3cevtModuleSw_LSR1GP48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP48LEB1 = _Hh3cevtModuleSw_LSR1GP48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 425)
)
_Hh3cevtModuleSw_LSR1GP48LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP48LEC1 = _Hh3cevtModuleSw_LSR1GP48LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 426)
)
_Hh3cevtModuleSw_LSR2GV48REB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2GV48REB1 = _Hh3cevtModuleSw_LSR2GV48REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 427)
)
_Hh3cevtModuleSw_LSR1XP2LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP2LEB1 = _Hh3cevtModuleSw_LSR1XP2LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 428)
)
_Hh3cevtModuleSw_LSR1XP2LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP2LEC1 = _Hh3cevtModuleSw_LSR1XP2LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 429)
)
_Hh3cevtModuleSw_LSR1XP4LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP4LEB1 = _Hh3cevtModuleSw_LSR1XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 430)
)
_Hh3cevtModuleSw_LSR1XP4LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP4LEC1 = _Hh3cevtModuleSw_LSR1XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 431)
)
_Hh3cevtModuleSw_IMFW_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IMFW = _Hh3cevtModuleSw_IMFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 432)
)
_Hh3cevtModuleSw_LSB1LB1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1LB1A0 = _Hh3cevtModuleSw_LSB1LB1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 433)
)
_Hh3cevtModuleSw_LSB1IPS1A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1IPS1A0 = _Hh3cevtModuleSw_LSB1IPS1A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 434)
)
_Hh3cevtModuleSw_LST1GT48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GT48LEB1 = _Hh3cevtModuleSw_LST1GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 435)
)
_Hh3cevtModuleSw_LST1GP48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEB1 = _Hh3cevtModuleSw_LST1GP48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 436)
)
_Hh3cevtModuleSw_LST1XP4LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP4LEB1 = _Hh3cevtModuleSw_LST1XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 437)
)
_Hh3cevtModuleSw_LST1XP8LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEB1 = _Hh3cevtModuleSw_LST1XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 438)
)
_Hh3cevtModuleSw_LST1XP32REB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP32REB1 = _Hh3cevtModuleSw_LST1XP32REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 439)
)
_Hh3cevtModuleSw_LST1XP32REC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP32REC1 = _Hh3cevtModuleSw_LST1XP32REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 440)
)
_Hh3cevtModuleSw_LSR1FW2A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1FW2A1 = _Hh3cevtModuleSw_LSR1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 441)
)
_Hh3cevtModuleSw_LSR1SSL1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SSL1A1 = _Hh3cevtModuleSw_LSR1SSL1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 442)
)
_Hh3cevtModuleSw_SR01DET32G2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR01DET32G2L = _Hh3cevtModuleSw_SR01DET32G2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 443)
)
_Hh3cevtModuleSw_LSR1GP24LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP24LEF1 = _Hh3cevtModuleSw_LSR1GP24LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 444)
)
_Hh3cevtModuleSw_LSR1XP4LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP4LEF1 = _Hh3cevtModuleSw_LSR1XP4LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 445)
)
_Hh3cevtModuleSw_LSR1LB1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1LB1A1 = _Hh3cevtModuleSw_LSR1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 446)
)
_Hh3cevtModuleSw_LSR1NSM1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1NSM1A1 = _Hh3cevtModuleSw_LSR1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 447)
)
_Hh3cevtModuleSw_LSR1ACG1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1ACG1A1 = _Hh3cevtModuleSw_LSR1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 448)
)
_Hh3cevtModuleSw_LSR1IPS1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1IPS1A1 = _Hh3cevtModuleSw_LSR1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 449)
)
_Hh3cevtModuleSw_LSR2GP24LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2GP24LEB1 = _Hh3cevtModuleSw_LSR2GP24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 450)
)
_Hh3cevtModuleSw_LSR2GT24LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2GT24LEB1 = _Hh3cevtModuleSw_LSR2GT24LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 451)
)
_Hh3cevtModuleSw_LSR2GT48LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2GT48LEB1 = _Hh3cevtModuleSw_LSR2GT48LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 452)
)
_Hh3cevtModuleSw_SPC_GP24L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP24L = _Hh3cevtModuleSw_SPC_GP24L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 453)
)
_Hh3cevtModuleSw_SPC_GT48L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GT48L = _Hh3cevtModuleSw_SPC_GT48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 454)
)
_Hh3cevtModuleSw_SPC_GP48L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP48L = _Hh3cevtModuleSw_SPC_GP48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 455)
)
_Hh3cevtModuleSw_SPC_XP2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP2L = _Hh3cevtModuleSw_SPC_XP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 456)
)
_Hh3cevtModuleSw_SPC_XP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP4L = _Hh3cevtModuleSw_SPC_XP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 457)
)
_Hh3cevtModuleSw_SR06SRP2E3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR06SRP2E3 = _Hh3cevtModuleSw_SR06SRP2E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 458)
)
_Hh3cevtModuleSw_SPE_2010_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_2010_E = _Hh3cevtModuleSw_SPE_2010_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 459)
)
_Hh3cevtModuleSw_SPE_2020_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_2020_E = _Hh3cevtModuleSw_SPE_2020_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 460)
)
_Hh3cevtModuleSw_SPC_XP4L_S_SDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP4L_S_SDI = _Hh3cevtModuleSw_SPC_XP4L_S_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 461)
)
_Hh3cevtModuleSw_SPC_GT48L_SDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GT48L_SDI = _Hh3cevtModuleSw_SPC_GT48L_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 462)
)
_Hh3cevtModuleSw_SPC_GP48L_S_SDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP48L_S_SDI = _Hh3cevtModuleSw_SPC_GP48L_S_SDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 463)
)
_Hh3cevtModuleSw_SPC_SR02OPMA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_SR02OPMA0 = _Hh3cevtModuleSw_SPC_SR02OPMA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 464)
)
_Hh3cevtModuleSw_LSR1XP16REB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP16REB1 = _Hh3cevtModuleSw_LSR1XP16REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 465)
)
_Hh3cevtModuleSw_LSR1GP48LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1GP48LEF1 = _Hh3cevtModuleSw_LSR1GP48LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 466)
)
_Hh3cevtModuleSw_LST1GP48LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEF1 = _Hh3cevtModuleSw_LST1GP48LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 467)
)
_Hh3cevtModuleSw_LST1XP8LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEF1 = _Hh3cevtModuleSw_LST1XP8LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 468)
)
_Hh3cevtModuleSw_SPE_1010_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_1010_II = _Hh3cevtModuleSw_SPE_1010_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 469)
)
_Hh3cevtModuleSw_SPE_1010_E_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_1010_E_II = _Hh3cevtModuleSw_SPE_1010_E_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 470)
)
_Hh3cevtModuleSw_SPE_1020_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_1020_II = _Hh3cevtModuleSw_SPE_1020_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 471)
)
_Hh3cevtModuleSw_SPE_1020_E_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPE_1020_E_II = _Hh3cevtModuleSw_SPE_1020_E_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 472)
)
_Hh3cevtModuleSw_LST1FW2A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1FW2A1 = _Hh3cevtModuleSw_LST1FW2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 473)
)
_Hh3cevtModuleSw_LST1NSM1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1NSM1A1 = _Hh3cevtModuleSw_LST1NSM1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 474)
)
_Hh3cevtModuleSw_LST1LB1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1LB1A1 = _Hh3cevtModuleSw_LST1LB1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 475)
)
_Hh3cevtModuleSw_LST1ACG1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1ACG1A1 = _Hh3cevtModuleSw_LST1ACG1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 476)
)
_Hh3cevtModuleSw_LST1IPS1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1IPS1A1 = _Hh3cevtModuleSw_LST1IPS1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 477)
)
_Hh3cevtModuleSw_LSR1DRUP1L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DRUP1L1 = _Hh3cevtModuleSw_LSR1DRUP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 478)
)
_Hh3cevtModuleSw_LSR1DPUP1L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DPUP1L1 = _Hh3cevtModuleSw_LSR1DPUP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 479)
)
_Hh3cevtModuleSw_LSR1DPSP4L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DPSP4L1 = _Hh3cevtModuleSw_LSR1DPSP4L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 480)
)
_Hh3cevtModuleSw_LSR1DTCP8L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DTCP8L1 = _Hh3cevtModuleSw_LSR1DTCP8L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 481)
)
_Hh3cevtModuleSw_LSR1DXP1L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DXP1L1 = _Hh3cevtModuleSw_LSR1DXP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 482)
)
_Hh3cevtModuleSw_LSR1DGP10L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DGP10L1 = _Hh3cevtModuleSw_LSR1DGP10L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 483)
)
_Hh3cevtModuleSw_LSR1LN1BNL1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1LN1BNL1 = _Hh3cevtModuleSw_LSR1LN1BNL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 484)
)
_Hh3cevtModuleSw_LSR1LN2BL1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1LN2BL1 = _Hh3cevtModuleSw_LSR1LN2BL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 485)
)
_Hh3cevtModuleSw_LSR1SRP2D1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1SRP2D1 = _Hh3cevtModuleSw_LSR1SRP2D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 486)
)
_Hh3cevtModuleSw_IM_NAT_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_NAT_II = _Hh3cevtModuleSw_IM_NAT_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 487)
)
_Hh3cevtModuleSw_IM_NAM_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_NAM_II = _Hh3cevtModuleSw_IM_NAM_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 488)
)
_Hh3cevtModuleSw_CR_MRP_I_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_MRP_I = _Hh3cevtModuleSw_CR_MRP_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 489)
)
_Hh3cevtModuleSw_CR_SF18C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SF18C = _Hh3cevtModuleSw_CR_SF18C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 490)
)
_Hh3cevtModuleSw_CR_SF08C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SF08C = _Hh3cevtModuleSw_CR_SF08C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 491)
)
_Hh3cevtModuleSw_CR_SPC_XP8LEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP8LEF = _Hh3cevtModuleSw_CR_SPC_XP8LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 492)
)
_Hh3cevtModuleSw_CR_SPC_XP4LEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP4LEF = _Hh3cevtModuleSw_CR_SPC_XP4LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 493)
)
_Hh3cevtModuleSw_CR_SPC_GP48LEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_GP48LEF = _Hh3cevtModuleSw_CR_SPC_GP48LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 494)
)
_Hh3cevtModuleSw_CR_SPC_GT48LEF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_GT48LEF = _Hh3cevtModuleSw_CR_SPC_GT48LEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 495)
)
_Hh3cevtModuleSw_CR_SPE_3020_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPE_3020_E = _Hh3cevtModuleSw_CR_SPE_3020_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 496)
)
_Hh3cevtModuleSw_CR_SPC_PUP4L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_PUP4L_E = _Hh3cevtModuleSw_CR_SPC_PUP4L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 497)
)
_Hh3cevtModuleSw_LST1SF08C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF08C1 = _Hh3cevtModuleSw_LST1SF08C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 498)
)
_Hh3cevtModuleSw_LST1SF18C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF18C1 = _Hh3cevtModuleSw_LST1SF18C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 499)
)
_Hh3cevtModuleSw_LS81GP16TM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP16TM = _Hh3cevtModuleSw_LS81GP16TM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 500)
)
_Hh3cevtModuleSw_LS81VP4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81VP4C = _Hh3cevtModuleSw_LS81VP4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 501)
)
_Hh3cevtModuleSw_LS8M1PT8P0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS8M1PT8P0 = _Hh3cevtModuleSw_LS8M1PT8P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 502)
)
_Hh3cevtModuleSw_LS8M1PT8GB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS8M1PT8GB0 = _Hh3cevtModuleSw_LS8M1PT8GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 503)
)
_Hh3cevtModuleSw_LS8M1PT4GB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS8M1PT4GB0 = _Hh3cevtModuleSw_LS8M1PT4GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 504)
)
_Hh3cevtModuleSw_LS81GP2R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP2R = _Hh3cevtModuleSw_LS81GP2R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 505)
)
_Hh3cevtModuleSw_LS81GP4R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP4R = _Hh3cevtModuleSw_LS81GP4R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 506)
)
_Hh3cevtModuleSw_LS81IPSECA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81IPSECA = _Hh3cevtModuleSw_LS81IPSECA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 507)
)
_Hh3cevtModuleSw_LS81FWA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FWA = _Hh3cevtModuleSw_LS81FWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 508)
)
_Hh3cevtModuleSw_LS82VSNP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS82VSNP = _Hh3cevtModuleSw_LS82VSNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 509)
)
_Hh3cevtModuleSw_LSQ1GV48SA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SA = _Hh3cevtModuleSw_LSQ1GV48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 510)
)
_Hh3cevtModuleSw_LSQ1SRPB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPB = _Hh3cevtModuleSw_LSQ1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 511)
)
_Hh3cevtModuleSw_LSQ1SRP2XB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP2XB = _Hh3cevtModuleSw_LSQ1SRP2XB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 512)
)
_Hh3cevtModuleSw_LSQ1SRP1CB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP1CB = _Hh3cevtModuleSw_LSQ1SRP1CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 513)
)
_Hh3cevtModuleSw_LSQ1FV48SA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FV48SA = _Hh3cevtModuleSw_LSQ1FV48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 514)
)
_Hh3cevtModuleSw_LSD1MPUA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1MPUA = _Hh3cevtModuleSw_LSD1MPUA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 515)
)
_Hh3cevtModuleSw_LSD1GP20A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20A0 = _Hh3cevtModuleSw_LSD1GP20A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 516)
)
_Hh3cevtModuleSw_LSD1GP20TA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20TA0 = _Hh3cevtModuleSw_LSD1GP20TA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 517)
)
_Hh3cevtModuleSw_LSD1GP36A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP36A0 = _Hh3cevtModuleSw_LSD1GP36A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 518)
)
_Hh3cevtModuleSw_LSD1GP20XA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20XA0 = _Hh3cevtModuleSw_LSD1GP20XA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 519)
)
_Hh3cevtModuleSw_LSD1GP20EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20EA0 = _Hh3cevtModuleSw_LSD1GP20EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 520)
)
_Hh3cevtModuleSw_LSD1GP20RA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP20RA0 = _Hh3cevtModuleSw_LSD1GP20RA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 521)
)
_Hh3cevtModuleSw_LSD1GP16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP16A0 = _Hh3cevtModuleSw_LSD1GP16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 522)
)
_Hh3cevtModuleSw_LSD1GT16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GT16A0 = _Hh3cevtModuleSw_LSD1GT16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 523)
)
_Hh3cevtModuleSw_LSD1XP2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1XP2A0 = _Hh3cevtModuleSw_LSD1XP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 524)
)
_Hh3cevtModuleSw_LSD1EP2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1EP2A0 = _Hh3cevtModuleSw_LSD1EP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 525)
)
_Hh3cevtModuleSw_LSD1RP2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1RP2A0 = _Hh3cevtModuleSw_LSD1RP2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 526)
)
_Hh3cevtModuleSw_LSQ1GV48SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SC = _Hh3cevtModuleSw_LSQ1GV48SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 527)
)
_Hh3cevtModuleSw_LSQ1FP48SA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FP48SA = _Hh3cevtModuleSw_LSQ1FP48SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 528)
)
_Hh3cevtModuleSw_LSQ1GP24SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24SC = _Hh3cevtModuleSw_LSQ1GP24SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 529)
)
_Hh3cevtModuleSw_LSQ1GT24SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GT24SC = _Hh3cevtModuleSw_LSQ1GT24SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 530)
)
_Hh3cevtModuleSw_LSQ1TGX2SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2SC = _Hh3cevtModuleSw_LSQ1TGX2SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 531)
)
_Hh3cevtModuleSw_LSQ1GP12EA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP12EA = _Hh3cevtModuleSw_LSQ1GP12EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 532)
)
_Hh3cevtModuleSw_LSQ1TGX1EA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX1EA = _Hh3cevtModuleSw_LSQ1TGX1EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 533)
)
_Hh3cevtModuleSw_LSQ1P24XGSC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1P24XGSC = _Hh3cevtModuleSw_LSQ1P24XGSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 534)
)
_Hh3cevtModuleSw_LSQ1T24XGSC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1T24XGSC = _Hh3cevtModuleSw_LSQ1T24XGSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 535)
)
_Hh3cevtModuleSw_LS81TGX1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX1B = _Hh3cevtModuleSw_LS81TGX1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 536)
)
_Hh3cevtModuleSw_LSQ1PT4PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT4PSC0 = _Hh3cevtModuleSw_LSQ1PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 537)
)
_Hh3cevtModuleSw_LS81SRPG13_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG13 = _Hh3cevtModuleSw_LS81SRPG13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 538)
)
_Hh3cevtModuleSw_LS81SRPG14_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG14 = _Hh3cevtModuleSw_LS81SRPG14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 539)
)
_Hh3cevtModuleSw_LS81SRPG15_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81SRPG15 = _Hh3cevtModuleSw_LS81SRPG15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 540)
)
_Hh3cevtModuleSw_LSQ1GP48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SC0 = _Hh3cevtModuleSw_LSQ1GP48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 541)
)
_Hh3cevtModuleSw_LSQ1GP12SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP12SC0 = _Hh3cevtModuleSw_LSQ1GP12SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 542)
)
_Hh3cevtModuleSw_LSD1SRPA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1SRPA = _Hh3cevtModuleSw_LSD1SRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 543)
)
_Hh3cevtModuleSw_LSD1SRPB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1SRPB = _Hh3cevtModuleSw_LSD1SRPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 544)
)
_Hh3cevtModuleSw_LSD1SRPC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1SRPC = _Hh3cevtModuleSw_LSD1SRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 545)
)
_Hh3cevtModuleSw_LSD1GT16PES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GT16PES0 = _Hh3cevtModuleSw_LSD1GT16PES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 546)
)
_Hh3cevtModuleSw_LSD1GP24ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP24ES0 = _Hh3cevtModuleSw_LSD1GP24ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 547)
)
_Hh3cevtModuleSw_LSD1GT24XES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GT24XES0 = _Hh3cevtModuleSw_LSD1GT24XES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 548)
)
_Hh3cevtModuleSw_LSD1GP24XES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP24XES0 = _Hh3cevtModuleSw_LSD1GP24XES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 549)
)
_Hh3cevtModuleSw_LSD1XP2ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1XP2ES0 = _Hh3cevtModuleSw_LSD1XP2ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 550)
)
_Hh3cevtModuleSw_LSD1GP48ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP48ES0 = _Hh3cevtModuleSw_LSD1GP48ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 551)
)
_Hh3cevtModuleSw_LSQ1MPUA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUA0 = _Hh3cevtModuleSw_LSQ1MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 552)
)
_Hh3cevtModuleSw_LSQ1MPUA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUA1 = _Hh3cevtModuleSw_LSQ1MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 553)
)
_Hh3cevtModuleSw_LSQ1FWBSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FWBSC0 = _Hh3cevtModuleSw_LSQ1FWBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 554)
)
_Hh3cevtModuleSw_LSQ1PT8PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT8PSC0 = _Hh3cevtModuleSw_LSQ1PT8PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 555)
)
_Hh3cevtModuleSw_LSQ1PT16PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT16PSC0 = _Hh3cevtModuleSw_LSQ1PT16PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 556)
)
_Hh3cevtModuleSw_SA11MPUA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SA11MPUA0 = _Hh3cevtModuleSw_SA11MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 557)
)
_Hh3cevtModuleSw_SA11MPUB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SA11MPUB0 = _Hh3cevtModuleSw_SA11MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 558)
)
_Hh3cevtModuleSw_LSQ1AFCBSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1AFCBSC0 = _Hh3cevtModuleSw_LSQ1AFCBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 559)
)
_Hh3cevtModuleSw_LSQ1MPUB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUB0 = _Hh3cevtModuleSw_LSQ1MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 560)
)
_Hh3cevtModuleSw_LSQ1MPUB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUB1 = _Hh3cevtModuleSw_LSQ1MPUB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 561)
)
_Hh3cevtModuleSw_LSQ1PT4PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT4PSC1 = _Hh3cevtModuleSw_LSQ1PT4PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 562)
)
_Hh3cevtModuleSw_LSQ1PT8PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT8PSC1 = _Hh3cevtModuleSw_LSQ1PT8PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 563)
)
_Hh3cevtModuleSw_LSQ1PT16PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1PT16PSC1 = _Hh3cevtModuleSw_LSQ1PT16PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 564)
)
_Hh3cevtModuleSw_LSQ1FP48USA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FP48USA0 = _Hh3cevtModuleSw_LSQ1FP48USA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 565)
)
_Hh3cevtModuleSw_LSQ1FP48USA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FP48USA1 = _Hh3cevtModuleSw_LSQ1FP48USA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 566)
)
_Hh3cevtModuleSw_LSQ1FV48USA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FV48USA0 = _Hh3cevtModuleSw_LSQ1FV48USA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 567)
)
_Hh3cevtModuleSw_LSQ1FV48USA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FV48USA1 = _Hh3cevtModuleSw_LSQ1FV48USA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 568)
)
_Hh3cevtModuleSw_LSQ1SRPD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPD0 = _Hh3cevtModuleSw_LSQ1SRPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 569)
)
_Hh3cevtModuleSw_LSQ1CGP24TSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGP24TSC0 = _Hh3cevtModuleSw_LSQ1CGP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 570)
)
_Hh3cevtModuleSw_LSQ1GP24TSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSC0 = _Hh3cevtModuleSw_LSQ1GP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 571)
)
_Hh3cevtModuleSw_LSQ1ACGASC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1ACGASC0 = _Hh3cevtModuleSw_LSQ1ACGASC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 572)
)
_Hh3cevtModuleSw_LSD1XP1ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1XP1ES0 = _Hh3cevtModuleSw_LSD1XP1ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 573)
)
_Hh3cevtModuleSw_LSD1GP12ES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSD1GP12ES0 = _Hh3cevtModuleSw_LSD1GP12ES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 574)
)
_Hh3cevtModuleSw_LSQ1SRP12GB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP12GB0 = _Hh3cevtModuleSw_LSQ1SRP12GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 575)
)
_Hh3cevtModuleSw_LSQ1GV40PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV40PSC0 = _Hh3cevtModuleSw_LSQ1GV40PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 576)
)
_Hh3cevtModuleSw_LSQ1FWBSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FWBSC1 = _Hh3cevtModuleSw_LSQ1FWBSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 577)
)
_Hh3cevtModuleSw_LSQ1NSMSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1NSMSC0 = _Hh3cevtModuleSw_LSQ1NSMSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 578)
)
_Hh3cevtModuleSw_LSQ1NSMSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1NSMSC1 = _Hh3cevtModuleSw_LSQ1NSMSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 579)
)
_Hh3cevtModuleSw_LSQ1AFDBSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1AFDBSC0 = _Hh3cevtModuleSw_LSQ1AFDBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 580)
)
_Hh3cevtModuleSw_LS81MPUB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81MPUB = _Hh3cevtModuleSw_LS81MPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 581)
)
_Hh3cevtModuleSw_LS81FP48XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FP48XL = _Hh3cevtModuleSw_LS81FP48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 582)
)
_Hh3cevtModuleSw_LS81FT48XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81FT48XL = _Hh3cevtModuleSw_LS81FT48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 583)
)
_Hh3cevtModuleSw_LS81GP12XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP12XL = _Hh3cevtModuleSw_LS81GP12XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 584)
)
_Hh3cevtModuleSw_LS81GP24XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP24XL = _Hh3cevtModuleSw_LS81GP24XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 585)
)
_Hh3cevtModuleSw_LS81GP48XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GP48XL = _Hh3cevtModuleSw_LS81GP48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 586)
)
_Hh3cevtModuleSw_LS81GT24XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT24XL = _Hh3cevtModuleSw_LS81GT24XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 587)
)
_Hh3cevtModuleSw_LS81GT48XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81GT48XL = _Hh3cevtModuleSw_LS81GT48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 588)
)
_Hh3cevtModuleSw_LS81TGX2XL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS81TGX2XL = _Hh3cevtModuleSw_LS81TGX2XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 589)
)
_Hh3cevtModuleSw_LSQ1GV48SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SD0 = _Hh3cevtModuleSw_LSQ1GV48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 590)
)
_Hh3cevtModuleSw_LSQ1GP48EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48EB0 = _Hh3cevtModuleSw_LSQ1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 591)
)
_Hh3cevtModuleSw_LSQ1IPSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1IPSSC0 = _Hh3cevtModuleSw_LSQ1IPSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 592)
)
_Hh3cevtModuleSw_LSQ1GV48SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SD1 = _Hh3cevtModuleSw_LSQ1GV48SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 593)
)
_Hh3cevtModuleSw_LSQ1GP48SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SD0 = _Hh3cevtModuleSw_LSQ1GP48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 594)
)
_Hh3cevtModuleSw_LSQ1GP48SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SD1 = _Hh3cevtModuleSw_LSQ1GP48SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 595)
)
_Hh3cevtModuleSw_LSQ1SRPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPA0 = _Hh3cevtModuleSw_LSQ1SRPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 596)
)
_Hh3cevtModuleSw_LSQ1SRPA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPA1 = _Hh3cevtModuleSw_LSQ1SRPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 597)
)
_Hh3cevtModuleSw_LSQ2FP48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FP48SA0 = _Hh3cevtModuleSw_LSQ2FP48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 598)
)
_Hh3cevtModuleSw_LSQ2FP48SA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FP48SA1 = _Hh3cevtModuleSw_LSQ2FP48SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 599)
)
_Hh3cevtModuleSw_LSQ2FT48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FT48SA0 = _Hh3cevtModuleSw_LSQ2FT48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 600)
)
_Hh3cevtModuleSw_LSQ2FT48SA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FT48SA1 = _Hh3cevtModuleSw_LSQ2FT48SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 601)
)
_Hh3cevtModuleSw_LSQ1GV24PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV24PSC0 = _Hh3cevtModuleSw_LSQ1GV24PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 602)
)
_Hh3cevtModuleSw_LSQ1GV24PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV24PSC1 = _Hh3cevtModuleSw_LSQ1GV24PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 603)
)
_Hh3cevtModuleSw_LSQ1CGV24PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGV24PSC0 = _Hh3cevtModuleSw_LSQ1CGV24PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 604)
)
_Hh3cevtModuleSw_LSQ1CGV24PSC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGV24PSC1 = _Hh3cevtModuleSw_LSQ1CGV24PSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 605)
)
_Hh3cevtModuleSw_LSQ1GP24TEB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TEB0 = _Hh3cevtModuleSw_LSQ1GP24TEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 606)
)
_Hh3cevtModuleSw_LSQ1GP24TEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TEB1 = _Hh3cevtModuleSw_LSQ1GP24TEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 607)
)
_Hh3cevtModuleSw_LSQ1GP24TSD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSD0 = _Hh3cevtModuleSw_LSQ1GP24TSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 608)
)
_Hh3cevtModuleSw_LSQ1GP24TSD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSD1 = _Hh3cevtModuleSw_LSQ1GP24TSD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 609)
)
_Hh3cevtModuleSw_LSQ1GP24TXSD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TXSD0 = _Hh3cevtModuleSw_LSQ1GP24TXSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 610)
)
_Hh3cevtModuleSw_LSQ1GP24TXSD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TXSD1 = _Hh3cevtModuleSw_LSQ1GP24TXSD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 611)
)
_Hh3cevtModuleSw_LSQ1TGX2EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2EB0 = _Hh3cevtModuleSw_LSQ1TGX2EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 612)
)
_Hh3cevtModuleSw_LSQ1TGX2EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2EB1 = _Hh3cevtModuleSw_LSQ1TGX2EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 613)
)
_Hh3cevtModuleSw_LSQ1TGX2SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2SD0 = _Hh3cevtModuleSw_LSQ1TGX2SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 614)
)
_Hh3cevtModuleSw_LSQ1TGX2SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2SD1 = _Hh3cevtModuleSw_LSQ1TGX2SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 615)
)
_Hh3cevtModuleSw_LSQ1TGX4SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX4SD0 = _Hh3cevtModuleSw_LSQ1TGX4SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 616)
)
_Hh3cevtModuleSw_LSQ1TGX4SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX4SD1 = _Hh3cevtModuleSw_LSQ1TGX4SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 617)
)
_Hh3cevtModuleSw_LSQ1TGX8SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX8SD0 = _Hh3cevtModuleSw_LSQ1TGX8SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 618)
)
_Hh3cevtModuleSw_LSQ1TGX8SD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX8SD1 = _Hh3cevtModuleSw_LSQ1TGX8SD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 619)
)
_Hh3cevtModuleSw_LSQ1GP48EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48EB1 = _Hh3cevtModuleSw_LSQ1GP48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 620)
)
_Hh3cevtModuleSw_LSQ1TGX4EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX4EB0 = _Hh3cevtModuleSw_LSQ1TGX4EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 621)
)
_Hh3cevtModuleSw_LSQ1TGX4EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX4EB1 = _Hh3cevtModuleSw_LSQ1TGX4EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 622)
)
_Hh3cevtModuleSw_LSQ1GP12SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP12SC3 = _Hh3cevtModuleSw_LSQ1GP12SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 623)
)
_Hh3cevtModuleSw_LSQ1GP24TSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSC3 = _Hh3cevtModuleSw_LSQ1GP24TSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 624)
)
_Hh3cevtModuleSw_LSQ1GP48SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SC3 = _Hh3cevtModuleSw_LSQ1GP48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 625)
)
_Hh3cevtModuleSw_LSQ1GV48SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV48SC3 = _Hh3cevtModuleSw_LSQ1GV48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 626)
)
_Hh3cevtModuleSw_LSQ1MPUA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUA3 = _Hh3cevtModuleSw_LSQ1MPUA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 627)
)
_Hh3cevtModuleSw_LSQ1SRP1CB3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP1CB3 = _Hh3cevtModuleSw_LSQ1SRP1CB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 628)
)
_Hh3cevtModuleSw_LSQ1SRPA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPA3 = _Hh3cevtModuleSw_LSQ1SRPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 629)
)
_Hh3cevtModuleSw_LSQ2FP48SA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FP48SA3 = _Hh3cevtModuleSw_LSQ2FP48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 630)
)
_Hh3cevtModuleSw_LSQ2FT48SA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FT48SA3 = _Hh3cevtModuleSw_LSQ2FT48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 631)
)
_Hh3cevtModuleSw_LSQ1MPUB3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUB3 = _Hh3cevtModuleSw_LSQ1MPUB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 632)
)
_Hh3cevtModuleSw_LSQ1CGP24TSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGP24TSC3 = _Hh3cevtModuleSw_LSQ1CGP24TSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 633)
)
_Hh3cevtModuleSw_LSQ1MPUB4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1MPUB4 = _Hh3cevtModuleSw_LSQ1MPUB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 634)
)
_Hh3cevtModuleSw_LSQ1SRPD4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPD4 = _Hh3cevtModuleSw_LSQ1SRPD4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 635)
)
_Hh3cevtModuleSw_LSQ1SSLSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SSLSC0 = _Hh3cevtModuleSw_LSQ1SSLSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 636)
)
_Hh3cevtModuleSw_LSQ1LBSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1LBSC0 = _Hh3cevtModuleSw_LSQ1LBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 637)
)
_Hh3cevtModuleSw_LSQ1NAT24SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1NAT24SC0 = _Hh3cevtModuleSw_LSQ1NAT24SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 638)
)
_Hh3cevtModuleSw_LSQ1SRP12GB4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRP12GB4 = _Hh3cevtModuleSw_LSQ1SRP12GB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 639)
)
_Hh3cevtModuleSw_LSQ1TGS8SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS8SC0 = _Hh3cevtModuleSw_LSQ1TGS8SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 640)
)
_Hh3cevtModuleSw_LSQ3PT4PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ3PT4PSC0 = _Hh3cevtModuleSw_LSQ3PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 641)
)
_Hh3cevtModuleSw_EWPXM2MPUB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2MPUB0 = _Hh3cevtModuleSw_EWPXM2MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 642)
)
_Hh3cevtModuleSw_EWPXM2SRP12GB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2SRP12GB0 = _Hh3cevtModuleSw_EWPXM2SRP12GB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 643)
)
_Hh3cevtModuleSw_EWPXM2SRPD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2SRPD0 = _Hh3cevtModuleSw_EWPXM2SRPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 644)
)
_Hh3cevtModuleSw_EWPXM2GP24TSD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP24TSD0 = _Hh3cevtModuleSw_EWPXM2GP24TSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 645)
)
_Hh3cevtModuleSw_EWPXM2GP24TXSD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP24TXSD0 = _Hh3cevtModuleSw_EWPXM2GP24TXSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 646)
)
_Hh3cevtModuleSw_EWPXM2TGX4SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2TGX4SD0 = _Hh3cevtModuleSw_EWPXM2TGX4SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 647)
)
_Hh3cevtModuleSw_EWPXM2GP48SD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP48SD0 = _Hh3cevtModuleSw_EWPXM2GP48SD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 648)
)
_Hh3cevtModuleSw_EWPXM2GP24TSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP24TSC0 = _Hh3cevtModuleSw_EWPXM2GP24TSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 649)
)
_Hh3cevtModuleSw_EWPXM2TGX2SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2TGX2SC0 = _Hh3cevtModuleSw_EWPXM2TGX2SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 650)
)
_Hh3cevtModuleSw_EWPXM2GP48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP48SC0 = _Hh3cevtModuleSw_EWPXM2GP48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 651)
)
_Hh3cevtModuleSw_LS7500_GP48_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_GP48_SC = _Hh3cevtModuleSw_LS7500_GP48_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 652)
)
_Hh3cevtModuleSw_LS7500_GP48_SD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_GP48_SD = _Hh3cevtModuleSw_LS7500_GP48_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 653)
)
_Hh3cevtModuleSw_LS7500_GT48_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_GT48_SC = _Hh3cevtModuleSw_LS7500_GT48_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 654)
)
_Hh3cevtModuleSw_LS7500_GT48_SD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_GT48_SD = _Hh3cevtModuleSw_LS7500_GT48_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 655)
)
_Hh3cevtModuleSw_LS7500_SRPG1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_SRPG1 = _Hh3cevtModuleSw_LS7500_SRPG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 656)
)
_Hh3cevtModuleSw_LS7500_SRPG2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_SRPG2 = _Hh3cevtModuleSw_LS7500_SRPG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 657)
)
_Hh3cevtModuleSw_LS7500_XP4_SD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_XP4_SD = _Hh3cevtModuleSw_LS7500_XP4_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 658)
)
_Hh3cevtModuleSw_LS7500_XP8_SD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS7500_XP8_SD = _Hh3cevtModuleSw_LS7500_XP8_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 659)
)
_Hh3cevtModuleSw_LSQ4PT4PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ4PT4PSC0 = _Hh3cevtModuleSw_LSQ4PT4PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 660)
)
_Hh3cevtModuleSw_LSQ4PT8PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ4PT8PSC0 = _Hh3cevtModuleSw_LSQ4PT8PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 661)
)
_Hh3cevtModuleSw_LSQ4PT16PSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ4PT16PSC0 = _Hh3cevtModuleSw_LSQ4PT16PSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 662)
)
_Hh3cevtModuleSw_LSQ1GP24TSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSA0 = _Hh3cevtModuleSw_LSQ1GP24TSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 663)
)
_Hh3cevtModuleSw_LSQ1GV24PSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GV24PSA0 = _Hh3cevtModuleSw_LSQ1GV24PSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 664)
)
_Hh3cevtModuleSw_LSQ1SRPD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPD3 = _Hh3cevtModuleSw_LSQ1SRPD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 665)
)
_Hh3cevtModuleSw_LSQ1SUPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SUPA0 = _Hh3cevtModuleSw_LSQ1SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 666)
)
_Hh3cevtModuleSw_LSU1FAB04A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB04A0 = _Hh3cevtModuleSw_LSU1FAB04A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 667)
)
_Hh3cevtModuleSw_LSU1FAB08A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB08A0 = _Hh3cevtModuleSw_LSU1FAB08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 668)
)
_Hh3cevtModuleSw_LSU1TGS8EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS8EA0 = _Hh3cevtModuleSw_LSU1TGS8EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 669)
)
_Hh3cevtModuleSw_LSU1TGS8EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS8EB0 = _Hh3cevtModuleSw_LSU1TGS8EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 670)
)
_Hh3cevtModuleSw_LSU1TGS8SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS8SE0 = _Hh3cevtModuleSw_LSU1TGS8SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 671)
)
_Hh3cevtModuleSw_LSUTGS16SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUTGS16SC0 = _Hh3cevtModuleSw_LSUTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 672)
)
_Hh3cevtModuleSw_LSU1SUPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1SUPA0 = _Hh3cevtModuleSw_LSU1SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 673)
)
_Hh3cevtModuleSw_LSU1GP24TXEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24TXEA0 = _Hh3cevtModuleSw_LSU1GP24TXEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 674)
)
_Hh3cevtModuleSw_LSU1GP24TXEB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24TXEB0 = _Hh3cevtModuleSw_LSU1GP24TXEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 675)
)
_Hh3cevtModuleSw_LSU1GP24TXSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24TXSE0 = _Hh3cevtModuleSw_LSU1GP24TXSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 676)
)
_Hh3cevtModuleSw_LSU1GP48EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP48EA0 = _Hh3cevtModuleSw_LSU1GP48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 677)
)
_Hh3cevtModuleSw_LSU1GP48EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP48EB0 = _Hh3cevtModuleSw_LSU1GP48EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 678)
)
_Hh3cevtModuleSw_LSU1GP48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP48SE0 = _Hh3cevtModuleSw_LSU1GP48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 679)
)
_Hh3cevtModuleSw_LSU1GT48EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GT48EA0 = _Hh3cevtModuleSw_LSU1GT48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 680)
)
_Hh3cevtModuleSw_LSU1GT48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GT48SE0 = _Hh3cevtModuleSw_LSU1GT48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 681)
)
_Hh3cevtModuleSw_LSU1TGX4EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGX4EA0 = _Hh3cevtModuleSw_LSU1TGX4EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 682)
)
_Hh3cevtModuleSw_LSU1TGX4EB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGX4EB0 = _Hh3cevtModuleSw_LSU1TGX4EB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 683)
)
_Hh3cevtModuleSw_LSU1TGX4SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGX4SE0 = _Hh3cevtModuleSw_LSU1TGX4SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 684)
)
_Hh3cevtModuleSw_LSQ1FAB08A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB08A0 = _Hh3cevtModuleSw_LSQ1FAB08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 685)
)
_Hh3cevtModuleSw_EWPX2WCMD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX2WCMD0 = _Hh3cevtModuleSw_EWPX2WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 686)
)
_Hh3cevtModuleSw_LSQ1WCMD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1WCMD0 = _Hh3cevtModuleSw_LSQ1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 687)
)
_Hh3cevtModuleSw_LSQ1IAGSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1IAGSC0 = _Hh3cevtModuleSw_LSQ1IAGSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 688)
)
_Hh3cevtModuleSw_LSU1GP24TSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24TSE0 = _Hh3cevtModuleSw_LSU1GP24TSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 689)
)
_Hh3cevtModuleSw_LSQ1TGS16SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS16SC0 = _Hh3cevtModuleSw_LSQ1TGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 690)
)
_Hh3cevtModuleSw_EWPX2TGS16SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX2TGS16SC0 = _Hh3cevtModuleSw_EWPX2TGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 691)
)
_Hh3cevtModuleSw_LSQ1SUPA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SUPA3 = _Hh3cevtModuleSw_LSQ1SUPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 692)
)
_Hh3cevtModuleSw_LSQ1FAB04A3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB04A3 = _Hh3cevtModuleSw_LSQ1FAB04A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 693)
)
_Hh3cevtModuleSw_LSQ1FAB08A3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB08A3 = _Hh3cevtModuleSw_LSQ1FAB08A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 694)
)
_Hh3cevtModuleSw_LSQ1GT48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GT48SC0 = _Hh3cevtModuleSw_LSQ1GT48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 695)
)
_Hh3cevtModuleSw_LSR2SRP2C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2SRP2C1 = _Hh3cevtModuleSw_LSR2SRP2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 696)
)
_Hh3cevtModuleSw_LSR2SRP2C2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2SRP2C2 = _Hh3cevtModuleSw_LSR2SRP2C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 697)
)
_Hh3cevtModuleSw_1000BASE_X_COMBO_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_X_COMBO = _Hh3cevtModuleSw_1000BASE_X_COMBO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 701)
)
_Hh3cevtModuleSw_EPON_1000M_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EPON_1000M = _Hh3cevtModuleSw_EPON_1000M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 702)
)
_Hh3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45 = _Hh3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 703)
)
_Hh3cevtModuleSw_100M_1550_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_1550_BIDI = _Hh3cevtModuleSw_100M_1550_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 704)
)
_Hh3cevtModuleSw_100M_1310_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_100M_1310_BIDI = _Hh3cevtModuleSw_100M_1310_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 705)
)
_Hh3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO = _Hh3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 706)
)
_Hh3cevtModuleSw_LSH1PK2T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSH1PK2T = _Hh3cevtModuleSw_LSH1PK2T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 707)
)
_Hh3cevtModuleSw_LSPM2GP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM2GP2P = _Hh3cevtModuleSw_LSPM2GP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 708)
)
_Hh3cevtModuleSw_LSWM1GT16P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1GT16P = _Hh3cevtModuleSw_LSWM1GT16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 709)
)
_Hh3cevtModuleSw_LSWM1GP16P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1GP16P = _Hh3cevtModuleSw_LSWM1GP16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 710)
)
_Hh3cevtModuleSw_LSWM1XP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1XP2P = _Hh3cevtModuleSw_LSWM1XP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 711)
)
_Hh3cevtModuleSw_LSWM1XP4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1XP4P = _Hh3cevtModuleSw_LSWM1XP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 712)
)
_Hh3cevtModuleSw_LSWM1SP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1SP2P = _Hh3cevtModuleSw_LSWM1SP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 713)
)
_Hh3cevtModuleSw_LSWM1SP4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1SP4P = _Hh3cevtModuleSw_LSWM1SP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 714)
)
_Hh3cevtModuleSw_LSWM148POEM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM148POEM = _Hh3cevtModuleSw_LSWM148POEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 715)
)
_Hh3cevtModuleSw_LSWM1FW10_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1FW10 = _Hh3cevtModuleSw_LSWM1FW10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 716)
)
_Hh3cevtModuleSw_LSWM1WCM10_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1WCM10 = _Hh3cevtModuleSw_LSWM1WCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 717)
)
_Hh3cevtModuleSw_LSWM1IPS10_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1IPS10 = _Hh3cevtModuleSw_LSWM1IPS10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 718)
)
_Hh3cevtModuleSw_LSWM1WCM20_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1WCM20 = _Hh3cevtModuleSw_LSWM1WCM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 719)
)
_Hh3cevtModuleSw_IPS_T1000_M_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_T1000_M = _Hh3cevtModuleSw_IPS_T1000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 720)
)
_Hh3cevtModuleSw_IPS_T1000_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_T1000_A = _Hh3cevtModuleSw_IPS_T1000_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 721)
)
_Hh3cevtModuleSw_IPS_T1000_S_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_T1000_S = _Hh3cevtModuleSw_IPS_T1000_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 722)
)
_Hh3cevtModuleSw_IPS_GX4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_GX4C = _Hh3cevtModuleSw_IPS_GX4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 723)
)
_Hh3cevtModuleSw_IPS_GT4C_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IPS_GT4C = _Hh3cevtModuleSw_IPS_GT4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 724)
)
_Hh3cevtModuleSw_LSPM2SP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM2SP2P = _Hh3cevtModuleSw_LSPM2SP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 725)
)
_Hh3cevtModuleSw_LSPM2SP2PA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM2SP2PA = _Hh3cevtModuleSw_LSPM2SP2PA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 726)
)
_Hh3cevtModuleSw_LSP5GP8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSP5GP8P = _Hh3cevtModuleSw_LSP5GP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 727)
)
_Hh3cevtModuleSw_LSP5GT8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSP5GT8P = _Hh3cevtModuleSw_LSP5GT8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 728)
)
_Hh3cevtModuleSw_LSWM1FC4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1FC4P = _Hh3cevtModuleSw_LSWM1FC4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 729)
)
_Hh3cevtModuleSw_LSW1XGT4P0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSW1XGT4P0 = _Hh3cevtModuleSw_LSW1XGT4P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 730)
)
_Hh3cevtModuleSw_LSW1XGT2P0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSW1XGT2P0 = _Hh3cevtModuleSw_LSW1XGT2P0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 731)
)
_Hh3cevtModuleSw_LSP1XGT2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSP1XGT2P = _Hh3cevtModuleSw_LSP1XGT2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 732)
)
_Hh3cevtModuleSw_LSPM3XGT2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM3XGT2P = _Hh3cevtModuleSw_LSPM3XGT2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 733)
)
_Hh3cevtModuleSw_LSWM2QP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2QP2P = _Hh3cevtModuleSw_LSWM2QP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 734)
)
_Hh3cevtModuleSw_LSWM2XGT2PM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2XGT2PM = _Hh3cevtModuleSw_LSWM2XGT2PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 735)
)
_Hh3cevtModuleSw_LSWM2SP2PM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP2PM = _Hh3cevtModuleSw_LSWM2SP2PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 736)
)
_Hh3cevtModuleSw_LSWM2SP8PM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP8PM = _Hh3cevtModuleSw_LSWM2SP8PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 737)
)
_Hh3cevtModuleSw_LSWM2SP8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP8P = _Hh3cevtModuleSw_LSWM2SP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 738)
)
_Hh3cevtModuleSw_LSWM2XGT8PM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2XGT8PM = _Hh3cevtModuleSw_LSWM2XGT8PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 739)
)
_Hh3cevtModuleSw_LSWM18QC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM18QC = _Hh3cevtModuleSw_LSWM18QC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 740)
)
_Hh3cevtModuleSw_LSWM124XG2Q_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM124XG2Q = _Hh3cevtModuleSw_LSWM124XG2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 741)
)
_Hh3cevtModuleSw_LSWM124XGT2Q_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM124XGT2Q = _Hh3cevtModuleSw_LSWM124XGT2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 742)
)
_Hh3cevtModuleSw_LSWM124XG2QL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM124XG2QL = _Hh3cevtModuleSw_LSWM124XG2QL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 743)
)
_Hh3cevtModuleSw_LSWM124XG2QFC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM124XG2QFC = _Hh3cevtModuleSw_LSWM124XG2QFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 744)
)
_Hh3cevtModuleSw_LSWM18QC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM18QC0 = _Hh3cevtModuleSw_LSWM18QC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 745)
)
_Hh3cevtModuleSw_LSWM124XGT2Q0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM124XGT2Q0 = _Hh3cevtModuleSw_LSWM124XGT2Q0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 746)
)
_Hh3cevtModuleSw_LSWM124XG2QL0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM124XG2QL0 = _Hh3cevtModuleSw_LSWM124XG2QL0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 747)
)
_Hh3cevtModuleSw_LSP6G4T6P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSP6G4T6P = _Hh3cevtModuleSw_LSP6G4T6P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 748)
)
_Hh3cevtModuleSw_LSPM6QP2PS_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM6QP2PS = _Hh3cevtModuleSw_LSPM6QP2PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 749)
)
_Hh3cevtModuleSw_LSWM12H2Q_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM12H2Q = _Hh3cevtModuleSw_LSWM12H2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 750)
)
_Hh3cevtModuleSw_LSWM18CQ_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM18CQ = _Hh3cevtModuleSw_LSWM18CQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 751)
)
_Hh3cevtModuleSw_LSWM116Q_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM116Q = _Hh3cevtModuleSw_LSWM116Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 752)
)
_Hh3cevtModuleSw_LSPM6FWD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM6FWD = _Hh3cevtModuleSw_LSPM6FWD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 753)
)
_Hh3cevtModuleSw_DS_3E_2XT_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E_2XT_H = _Hh3cevtModuleSw_DS_3E_2XT_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 754)
)
_Hh3cevtModuleSw_DS_3E_2XF_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E_2XF_H = _Hh3cevtModuleSw_DS_3E_2XF_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 755)
)
_Hh3cevtModuleSw_DS_3E_2QX_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E_2QX_H = _Hh3cevtModuleSw_DS_3E_2QX_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 756)
)
_Hh3cevtModuleSw_LSPM4G4T6P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSPM4G4T6P = _Hh3cevtModuleSw_LSPM4G4T6P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 757)
)
_Hh3cevtModuleSw_LSWM4SP8PM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM4SP8PM = _Hh3cevtModuleSw_LSWM4SP8PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 758)
)
_Hh3cevtModuleSw_LSWM124TG2H_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM124TG2H = _Hh3cevtModuleSw_LSWM124TG2H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 759)
)
_Hh3cevtModuleSw_LSWM18CQ0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM18CQ0 = _Hh3cevtModuleSw_LSWM18CQ0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 760)
)
_Hh3cevtModuleSw_LSWM116Q0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM116Q0 = _Hh3cevtModuleSw_LSWM116Q0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 761)
)
_Hh3cevtModuleSw_LSWM124TG2H0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM124TG2H0 = _Hh3cevtModuleSw_LSWM124TG2H0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 762)
)
_Hh3cevtModuleSw_LSWM2ZQP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2ZQP2P = _Hh3cevtModuleSw_LSWM2ZQP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 763)
)
_Hh3cevtModuleSw_LSWM2ZSP8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2ZSP8P = _Hh3cevtModuleSw_LSWM2ZSP8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 764)
)
_Hh3cevtModuleSw_LSWM18CQMSEC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM18CQMSEC = _Hh3cevtModuleSw_LSWM18CQMSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 765)
)
_Hh3cevtModuleSw_LSWM2MGT8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2MGT8P = _Hh3cevtModuleSw_LSWM2MGT8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 766)
)
_Hh3cevtModuleSw_LSWM2XMGT8P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2XMGT8P = _Hh3cevtModuleSw_LSWM2XMGT8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 767)
)
_Hh3cevtModuleSw_LSWM2ZSP2P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2ZSP2P = _Hh3cevtModuleSw_LSWM2ZSP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 768)
)
_Hh3cevtModuleSw_LSWM116FC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM116FC = _Hh3cevtModuleSw_LSWM116FC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 769)
)
_Hh3cevtModuleSw_LSWM216FC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM216FC = _Hh3cevtModuleSw_LSWM216FC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 770)
)
_Hh3cevtModuleSw_LSWM2SP2PB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP2PB = _Hh3cevtModuleSw_LSWM2SP2PB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 771)
)
_Hh3cevtModuleSw_LSWM2SP4PB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP4PB = _Hh3cevtModuleSw_LSWM2SP4PB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 772)
)
_Hh3cevtModuleSw_LSWM2SP24P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP24P = _Hh3cevtModuleSw_LSWM2SP24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 773)
)
_Hh3cevtModuleSw_LSWM2SP12P2Q_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP12P2Q = _Hh3cevtModuleSw_LSWM2SP12P2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 774)
)
_Hh3cevtModuleSw_LSWM2SP12P2QA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP12P2QA = _Hh3cevtModuleSw_LSWM2SP12P2QA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 775)
)
_Hh3cevtModuleSw_DS_3E_2QX_HB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E_2QX_HB = _Hh3cevtModuleSw_DS_3E_2QX_HB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 776)
)
_Hh3cevtModuleSw_DS_3E_8XF_H_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E_8XF_H = _Hh3cevtModuleSw_DS_3E_8XF_H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 777)
)
_Hh3cevtModuleSw_LSWM116HC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM116HC = _Hh3cevtModuleSw_LSWM116HC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 781)
)
_Hh3cevtModuleSw_WX5002MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_WX5002MPU = _Hh3cevtModuleSw_WX5002MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 800)
)
_Hh3cevtModuleSw_LS8M1WCMA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LS8M1WCMA = _Hh3cevtModuleSw_LS8M1WCMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 801)
)
_Hh3cevtModuleSw_EWPX1G24XA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1G24XA0 = _Hh3cevtModuleSw_EWPX1G24XA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 802)
)
_Hh3cevtModuleSw_LSQ1WCMB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1WCMB0 = _Hh3cevtModuleSw_LSQ1WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 803)
)
_Hh3cevtModuleSw_LSB1WCM2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSB1WCM2A0 = _Hh3cevtModuleSw_LSB1WCM2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 804)
)
_Hh3cevtModuleSw_EWPX1WCMB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCMB0 = _Hh3cevtModuleSw_EWPX1WCMB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 805)
)
_Hh3cevtModuleSw_EWPX1G24XC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1G24XC0 = _Hh3cevtModuleSw_EWPX1G24XC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 806)
)
_Hh3cevtModuleSw_EWPX1WCMC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCMC0 = _Hh3cevtModuleSw_EWPX1WCMC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 807)
)
_Hh3cevtModuleSw_EWPX1FWA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1FWA0 = _Hh3cevtModuleSw_EWPX1FWA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 808)
)
_Hh3cevtModuleSw_EWPX1G10XC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1G10XC0 = _Hh3cevtModuleSw_EWPX1G10XC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 809)
)
_Hh3cevtModuleSw_EWPX1WCM10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCM10C0 = _Hh3cevtModuleSw_EWPX1WCM10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 810)
)
_Hh3cevtModuleSw_LSR1WCM2A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1WCM2A1 = _Hh3cevtModuleSw_LSR1WCM2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 811)
)
_Hh3cevtModuleSw_EWPX1WAP0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WAP0 = _Hh3cevtModuleSw_EWPX1WAP0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 812)
)
_Hh3cevtModuleSw_EWPX1WCMD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCMD0 = _Hh3cevtModuleSw_EWPX1WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 813)
)
_Hh3cevtModuleSw_EWPX1G24XCE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1G24XCE0 = _Hh3cevtModuleSw_EWPX1G24XCE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 814)
)
_Hh3cevtModuleSw_EWPX1WCMCE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCMCE0 = _Hh3cevtModuleSw_EWPX1WCMCE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 815)
)
_Hh3cevtModuleSw_EWPX1G24XD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1G24XD0 = _Hh3cevtModuleSw_EWPX1G24XD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 816)
)
_Hh3cevtModuleSw_EWPXM1XG03_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM1XG03 = _Hh3cevtModuleSw_EWPXM1XG03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 817)
)
_Hh3cevtModuleSw_EWPXM2X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2X = _Hh3cevtModuleSw_EWPXM2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 818)
)
_Hh3cevtModuleSw_EWPXM8G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM8G = _Hh3cevtModuleSw_EWPXM8G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 819)
)
_Hh3cevtModuleSw_IOT_CARD_C1K_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IOT_CARD_C1K = _Hh3cevtModuleSw_IOT_CARD_C1K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 820)
)
_Hh3cevtModuleSw_EWPXM1BSTX80_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM1BSTX80 = _Hh3cevtModuleSw_EWPXM1BSTX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 821)
)
_Hh3cevtModuleSw_LSR1DRSP2L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1DRSP2L1 = _Hh3cevtModuleSw_LSR1DRSP2L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 900)
)
_Hh3cevtModuleSw_PIC_CLF2G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_CLF2G8L = _Hh3cevtModuleSw_PIC_CLF2G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 901)
)
_Hh3cevtModuleSw_PIC_CLF4G8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_CLF4G8L = _Hh3cevtModuleSw_PIC_CLF4G8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 902)
)
_Hh3cevtModuleSw_SR02SRP2F3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP2F3 = _Hh3cevtModuleSw_SR02SRP2F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 903)
)
_Hh3cevtModuleSw_SR02SRP1F3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP1F3 = _Hh3cevtModuleSw_SR02SRP1F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 904)
)
_Hh3cevtModuleSw_LST1GT48LEA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GT48LEA1 = _Hh3cevtModuleSw_LST1GT48LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 905)
)
_Hh3cevtModuleSw_LST1GP48LEA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEA1 = _Hh3cevtModuleSw_LST1GP48LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 906)
)
_Hh3cevtModuleSw_LST2XP8LEA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP8LEA1 = _Hh3cevtModuleSw_LST2XP8LEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 907)
)
_Hh3cevtModuleSw_LST1GT48LEY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GT48LEY1 = _Hh3cevtModuleSw_LST1GT48LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 908)
)
_Hh3cevtModuleSw_LST1GP48LEY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEY1 = _Hh3cevtModuleSw_LST1GP48LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 909)
)
_Hh3cevtModuleSw_LST1XP32REY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP32REY1 = _Hh3cevtModuleSw_LST1XP32REY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 910)
)
_Hh3cevtModuleSw_LST1XP8LEY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEY1 = _Hh3cevtModuleSw_LST1XP8LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 911)
)
_Hh3cevtModuleSw_LST1GP48LEZ1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEZ1 = _Hh3cevtModuleSw_LST1GP48LEZ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 912)
)
_Hh3cevtModuleSw_LST1XP8LEZ1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP8LEZ1 = _Hh3cevtModuleSw_LST1XP8LEZ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 913)
)
_Hh3cevtModuleSw_IM_FW_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_FW_II = _Hh3cevtModuleSw_IM_FW_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 914)
)
_Hh3cevtModuleSw_IM_IPS_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_IPS = _Hh3cevtModuleSw_IM_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 915)
)
_Hh3cevtModuleSw_IM_SSL_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_SSL = _Hh3cevtModuleSw_IM_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 916)
)
_Hh3cevtModuleSw_IM_LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_LB = _Hh3cevtModuleSw_IM_LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 917)
)
_Hh3cevtModuleSw_IM_ACG_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_ACG = _Hh3cevtModuleSw_IM_ACG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 918)
)
_Hh3cevtModuleSw_LSR1XP16REC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1XP16REC1 = _Hh3cevtModuleSw_LSR1XP16REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 919)
)
_Hh3cevtModuleSw_LST2XP8LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP8LEB1 = _Hh3cevtModuleSw_LST2XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 920)
)
_Hh3cevtModuleSw_LST2XP8LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP8LEC1 = _Hh3cevtModuleSw_LST2XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 921)
)
_Hh3cevtModuleSw_LST2XP8LEF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP8LEF1 = _Hh3cevtModuleSw_LST2XP8LEF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 922)
)
_Hh3cevtModuleSw_LSR2XP4LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2XP4LEB1 = _Hh3cevtModuleSw_LSR2XP4LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 923)
)
_Hh3cevtModuleSw_LSR2XP4LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2XP4LEC1 = _Hh3cevtModuleSw_LSR2XP4LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 924)
)
_Hh3cevtModuleSw_LST2XP32REB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP32REB1 = _Hh3cevtModuleSw_LST2XP32REB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 925)
)
_Hh3cevtModuleSw_LST2XP32REC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP32REC1 = _Hh3cevtModuleSw_LST2XP32REC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 926)
)
_Hh3cevtModuleSw_LSR1WCM3A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR1WCM3A1 = _Hh3cevtModuleSw_LSR1WCM3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 927)
)
_Hh3cevtModuleSw_LST1XP16LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP16LEB1 = _Hh3cevtModuleSw_LST1XP16LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 928)
)
_Hh3cevtModuleSw_LST1XP16LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP16LEC1 = _Hh3cevtModuleSw_LST1XP16LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 929)
)
_Hh3cevtModuleSw_CR_SPC_XP4L_E_I_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP4L_E_I = _Hh3cevtModuleSw_CR_SPC_XP4L_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 930)
)
_Hh3cevtModuleSw_LST2MRPNC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2MRPNC1 = _Hh3cevtModuleSw_LST2MRPNC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 931)
)
_Hh3cevtModuleSw_LST2SF08C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2SF08C1 = _Hh3cevtModuleSw_LST2SF08C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 932)
)
_Hh3cevtModuleSw_LST2SF18C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2SF18C1 = _Hh3cevtModuleSw_LST2SF18C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 933)
)
_Hh3cevtModuleSw_SR02SRP2G3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR02SRP2G3 = _Hh3cevtModuleSw_SR02SRP2G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 934)
)
_Hh3cevtModuleSw_CR_SPE_3020_E_I_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPE_3020_E_I = _Hh3cevtModuleSw_CR_SPE_3020_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 935)
)
_Hh3cevtModuleSw_CR_SPC_PUP4L_E_I_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_PUP4L_E_I = _Hh3cevtModuleSw_CR_SPC_PUP4L_E_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 936)
)
_Hh3cevtModuleSw_CR_SPC_XP4LEF_I_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP4LEF_I = _Hh3cevtModuleSw_CR_SPC_XP4LEF_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 937)
)
_Hh3cevtModuleSw_CR_SPC_XP8LEF_I_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP8LEF_I = _Hh3cevtModuleSw_CR_SPC_XP8LEF_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 938)
)
_Hh3cevtModuleSw_LST3XP8LEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST3XP8LEB1 = _Hh3cevtModuleSw_LST3XP8LEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 939)
)
_Hh3cevtModuleSw_LST3XP8LEC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST3XP8LEC1 = _Hh3cevtModuleSw_LST3XP8LEC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 940)
)
_Hh3cevtModuleSw_LST1FW3A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1FW3A1 = _Hh3cevtModuleSw_LST1FW3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 941)
)
_Hh3cevtModuleSw_CR_IM_NAM1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_IM_NAM1A = _Hh3cevtModuleSw_CR_IM_NAM1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 942)
)
_Hh3cevtModuleSw_LSR2SRP2B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2SRP2B1 = _Hh3cevtModuleSw_LSR2SRP2B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 943)
)
_Hh3cevtModuleSw_LSR2SRP2B2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2SRP2B2 = _Hh3cevtModuleSw_LSR2SRP2B2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 944)
)
_Hh3cevtModuleSw_LSR2SRP2D1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSR2SRP2D1 = _Hh3cevtModuleSw_LSR2SRP2D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 945)
)
_Hh3cevtModuleSw_LST3XP8LEY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST3XP8LEY1 = _Hh3cevtModuleSw_LST3XP8LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 946)
)
_Hh3cevtModuleSw_LST2XP32REY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP32REY1 = _Hh3cevtModuleSw_LST2XP32REY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 947)
)
_Hh3cevtModuleSw_LST1XP16LEY1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP16LEY1 = _Hh3cevtModuleSw_LST1XP16LEY1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 948)
)
_Hh3cevtModuleSw_SR0M2SRP2G3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR0M2SRP2G3 = _Hh3cevtModuleSw_SR0M2SRP2G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 949)
)
_Hh3cevtModuleSw_SR0M2SRP1G3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR0M2SRP1G3 = _Hh3cevtModuleSw_SR0M2SRP1G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 950)
)
_Hh3cevtModuleSw_SPC_GP48LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP48LA = _Hh3cevtModuleSw_SPC_GP48LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 951)
)
_Hh3cevtModuleSw_SPC_GT48LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GT48LA = _Hh3cevtModuleSw_SPC_GT48LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 952)
)
_Hh3cevtModuleSw_SPC_XP4LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP4LA = _Hh3cevtModuleSw_SPC_XP4LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 953)
)
_Hh3cevtModuleSw_SPC_XP2LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP2LA = _Hh3cevtModuleSw_SPC_XP2LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 954)
)
_Hh3cevtModuleSw_SPC_GP24LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP24LA = _Hh3cevtModuleSw_SPC_GP24LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 955)
)
_Hh3cevtModuleSw_SPC_XP16RA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP16RA = _Hh3cevtModuleSw_SPC_XP16RA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 956)
)
_Hh3cevtModuleSw_CR_IM_FW1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_IM_FW1A = _Hh3cevtModuleSw_CR_IM_FW1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 957)
)
_Hh3cevtModuleSw_SPC_XP16R_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP16R = _Hh3cevtModuleSw_SPC_XP16R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 958)
)
_Hh3cevtModuleSw_CR_IM_LB1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_IM_LB1A = _Hh3cevtModuleSw_CR_IM_LB1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 959)
)
_Hh3cevtModuleSw_LST1GT48LEC2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GT48LEC2 = _Hh3cevtModuleSw_LST1GT48LEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 960)
)
_Hh3cevtModuleSw_LST1GP48LEC2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1GP48LEC2 = _Hh3cevtModuleSw_LST1GP48LEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 961)
)
_Hh3cevtModuleSw_LST1XP16LEC2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP16LEC2 = _Hh3cevtModuleSw_LST1XP16LEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 962)
)
_Hh3cevtModuleSw_LST2XP8LEC2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP8LEC2 = _Hh3cevtModuleSw_LST2XP8LEC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 963)
)
_Hh3cevtModuleSw_LST2XP32REC2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2XP32REC2 = _Hh3cevtModuleSw_LST2XP32REC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 964)
)
_Hh3cevtModuleSw_CR_IM_MAC1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_IM_MAC1A = _Hh3cevtModuleSw_CR_IM_MAC1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 965)
)
_Hh3cevtModuleSw_LST1XP48LFD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP48LFD1 = _Hh3cevtModuleSw_LST1XP48LFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 966)
)
_Hh3cevtModuleSw_LST1XP40RFD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP40RFD1 = _Hh3cevtModuleSw_LST1XP40RFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 967)
)
_Hh3cevtModuleSw_LST1XP40RFG1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP40RFG1 = _Hh3cevtModuleSw_LST1XP40RFG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 968)
)
_Hh3cevtModuleSw_LST1XLP16RFD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XLP16RFD1 = _Hh3cevtModuleSw_LST1XLP16RFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 969)
)
_Hh3cevtModuleSw_LST1CP4RFD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1CP4RFD1 = _Hh3cevtModuleSw_LST1CP4RFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 970)
)
_Hh3cevtModuleSw_LST1CP4RFG1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1CP4RFG1 = _Hh3cevtModuleSw_LST1CP4RFG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 971)
)
_Hh3cevtModuleSw_LST1SF08E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF08E1 = _Hh3cevtModuleSw_LST1SF08E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 972)
)
_Hh3cevtModuleSw_LST1SF18E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1SF18E1 = _Hh3cevtModuleSw_LST1SF18E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 973)
)
_Hh3cevtModuleSw_LST1MRPNE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1MRPNE1 = _Hh3cevtModuleSw_LST1MRPNE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 974)
)
_Hh3cevtModuleSw_LSX1CGX8FC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1CGX8FC0 = _Hh3cevtModuleSw_LSX1CGX8FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 975)
)
_Hh3cevtModuleSw_LSX1CGX8FC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1CGX8FC1 = _Hh3cevtModuleSw_LSX1CGX8FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 976)
)
_Hh3cevtModuleSw_LSX1QGS24FC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS24FC0 = _Hh3cevtModuleSw_LSX1QGS24FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 977)
)
_Hh3cevtModuleSw_LSX1QGS24FC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS24FC1 = _Hh3cevtModuleSw_LSX1QGS24FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 978)
)
_Hh3cevtModuleSw_LSX1TGS24FC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS24FC0 = _Hh3cevtModuleSw_LSX1TGS24FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 979)
)
_Hh3cevtModuleSw_LSX1TGS24FC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS24FC1 = _Hh3cevtModuleSw_LSX1TGS24FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 980)
)
_Hh3cevtModuleSw_LSX1TGS48FC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS48FC0 = _Hh3cevtModuleSw_LSX1TGS48FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 981)
)
_Hh3cevtModuleSw_LSX1TGS48FC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS48FC1 = _Hh3cevtModuleSw_LSX1TGS48FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 982)
)
_Hh3cevtModuleSw_LST1XP48LFD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP48LFD2 = _Hh3cevtModuleSw_LST1XP48LFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 983)
)
_Hh3cevtModuleSw_LST1XP40RFD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP40RFD2 = _Hh3cevtModuleSw_LST1XP40RFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 984)
)
_Hh3cevtModuleSw_LST1XP40RFG2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP40RFG2 = _Hh3cevtModuleSw_LST1XP40RFG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 985)
)
_Hh3cevtModuleSw_LST1XLP16RFD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XLP16RFD2 = _Hh3cevtModuleSw_LST1XLP16RFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 986)
)
_Hh3cevtModuleSw_LST1CP4RFD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1CP4RFD2 = _Hh3cevtModuleSw_LST1CP4RFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 987)
)
_Hh3cevtModuleSw_LST1CP4RFG2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1CP4RFG2 = _Hh3cevtModuleSw_LST1CP4RFG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 988)
)
_Hh3cevtModuleSw_MPE_1004_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MPE_1004 = _Hh3cevtModuleSw_MPE_1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 989)
)
_Hh3cevtModuleSw_MIC_GP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GP4L = _Hh3cevtModuleSw_MIC_GP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 990)
)
_Hh3cevtModuleSw_MIC_GP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GP8L = _Hh3cevtModuleSw_MIC_GP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 991)
)
_Hh3cevtModuleSw_MIC_SP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_SP4L = _Hh3cevtModuleSw_MIC_SP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 992)
)
_Hh3cevtModuleSw_MIC_ET16L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_ET16L = _Hh3cevtModuleSw_MIC_ET16L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 993)
)
_Hh3cevtModuleSw_MIC_CLP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CLP4L = _Hh3cevtModuleSw_MIC_CLP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 994)
)
_Hh3cevtModuleSw_MIC_CLP2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CLP2L = _Hh3cevtModuleSw_MIC_CLP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 995)
)
_Hh3cevtModuleSw_LST1IPS2A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1IPS2A1 = _Hh3cevtModuleSw_LST1IPS2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 996)
)
_Hh3cevtModuleSw_SFC_04B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_04B = _Hh3cevtModuleSw_SFC_04B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 997)
)
_Hh3cevtModuleSw_SFC_04D_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_04D = _Hh3cevtModuleSw_SFC_04D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 998)
)
_Hh3cevtModuleSw_SFC_08B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_08B = _Hh3cevtModuleSw_SFC_08B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 999)
)
_Hh3cevtModuleSw_SFC_08D_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_08D = _Hh3cevtModuleSw_SFC_08D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1000)
)
_Hh3cevtModuleSw_SFC_12B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_12B = _Hh3cevtModuleSw_SFC_12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1001)
)
_Hh3cevtModuleSw_SFC_12D_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_12D = _Hh3cevtModuleSw_SFC_12D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1002)
)
_Hh3cevtModuleSw_SR05SRP1H1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR05SRP1H1 = _Hh3cevtModuleSw_SR05SRP1H1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1003)
)
_Hh3cevtModuleSw_SPC_GP24LA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP24LA1 = _Hh3cevtModuleSw_SPC_GP24LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1004)
)
_Hh3cevtModuleSw_SPC_GP24XP2LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP24XP2LA = _Hh3cevtModuleSw_SPC_GP24XP2LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1005)
)
_Hh3cevtModuleSw_SPC_GP48LA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP48LA1 = _Hh3cevtModuleSw_SPC_GP48LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1006)
)
_Hh3cevtModuleSw_SPC_GP48LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP48LB = _Hh3cevtModuleSw_SPC_GP48LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1007)
)
_Hh3cevtModuleSw_SPC_XP2LA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP2LA1 = _Hh3cevtModuleSw_SPC_XP2LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1008)
)
_Hh3cevtModuleSw_SPC_XP4LA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP4LA1 = _Hh3cevtModuleSw_SPC_XP4LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1009)
)
_Hh3cevtModuleSw_SPC_XP4LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP4LB = _Hh3cevtModuleSw_SPC_XP4LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1010)
)
_Hh3cevtModuleSw_SPC_XP8LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP8LA = _Hh3cevtModuleSw_SPC_XP8LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1011)
)
_Hh3cevtModuleSw_SPC_XP8LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP8LB = _Hh3cevtModuleSw_SPC_XP8LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1012)
)
_Hh3cevtModuleSw_SPC_XP48LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP48LA = _Hh3cevtModuleSw_SPC_XP48LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1013)
)
_Hh3cevtModuleSw_SPC_XLP8LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XLP8LA = _Hh3cevtModuleSw_SPC_XLP8LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1014)
)
_Hh3cevtModuleSw_SPC_GP24XP2LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP24XP2LB = _Hh3cevtModuleSw_SPC_GP24XP2LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1015)
)
_Hh3cevtModuleSw_LST1MRPNE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1MRPNE2 = _Hh3cevtModuleSw_LST1MRPNE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1016)
)
_Hh3cevtModuleSw_LST2FW3A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST2FW3A1 = _Hh3cevtModuleSw_LST2FW3A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1017)
)
_Hh3cevtModuleSw_LST1ADE1A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1ADE1A1 = _Hh3cevtModuleSw_LST1ADE1A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1018)
)
_Hh3cevtModuleSw_CR_MRP_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_MRP_II = _Hh3cevtModuleSw_CR_MRP_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1019)
)
_Hh3cevtModuleSw_CR_SF08E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SF08E = _Hh3cevtModuleSw_CR_SF08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1020)
)
_Hh3cevtModuleSw_CR_SF18E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SF18E = _Hh3cevtModuleSw_CR_SF18E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1021)
)
_Hh3cevtModuleSw_CR_SPC_XP40RC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP40RC = _Hh3cevtModuleSw_CR_SPC_XP40RC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1022)
)
_Hh3cevtModuleSw_CR_SPC_XP40RB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP40RB = _Hh3cevtModuleSw_CR_SPC_XP40RB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1023)
)
_Hh3cevtModuleSw_CR_SPC_CP4RC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_CP4RC = _Hh3cevtModuleSw_CR_SPC_CP4RC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1024)
)
_Hh3cevtModuleSw_LST1FW3C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1FW3C1 = _Hh3cevtModuleSw_LST1FW3C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1025)
)
_Hh3cevtModuleSw_LSU1FWCEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FWCEA0 = _Hh3cevtModuleSw_LSU1FWCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1026)
)
_Hh3cevtModuleSw_SPC_GT48LA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GT48LA1 = _Hh3cevtModuleSw_SPC_GT48LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1027)
)
_Hh3cevtModuleSw_LST1XP20RFD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP20RFD1 = _Hh3cevtModuleSw_LST1XP20RFD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1028)
)
_Hh3cevtModuleSw_LST1XP20RFD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1XP20RFD2 = _Hh3cevtModuleSw_LST1XP20RFD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1029)
)
_Hh3cevtModuleSw_MPE_1104_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MPE_1104 = _Hh3cevtModuleSw_MPE_1104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1030)
)
_Hh3cevtModuleSw_SPEX_1204_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPEX_1204 = _Hh3cevtModuleSw_SPEX_1204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1031)
)
_Hh3cevtModuleSw_SPC_GP44XP4LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP44XP4LCX = _Hh3cevtModuleSw_SPC_GP44XP4LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1032)
)
_Hh3cevtModuleSw_SPC_GP44XP4LAX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP44XP4LAX = _Hh3cevtModuleSw_SPC_GP44XP4LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1033)
)
_Hh3cevtModuleSw_SPC_XP24LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP24LCX = _Hh3cevtModuleSw_SPC_XP24LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1034)
)
_Hh3cevtModuleSw_SPC_XP24LAX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP24LAX = _Hh3cevtModuleSw_SPC_XP24LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1035)
)
_Hh3cevtModuleSw_SPC_XP12LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP12LCX = _Hh3cevtModuleSw_SPC_XP12LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1036)
)
_Hh3cevtModuleSw_SPC_XP12LAX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP12LAX = _Hh3cevtModuleSw_SPC_XP12LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1037)
)
_Hh3cevtModuleSw_SPC_XLP6LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XLP6LCX = _Hh3cevtModuleSw_SPC_XLP6LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1038)
)
_Hh3cevtModuleSw_SPC_XLP6LAX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XLP6LAX = _Hh3cevtModuleSw_SPC_XLP6LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1039)
)
_Hh3cevtModuleSw_SPC_CP1LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_CP1LCX = _Hh3cevtModuleSw_SPC_CP1LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1040)
)
_Hh3cevtModuleSw_SPC_CP1LAX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_CP1LAX = _Hh3cevtModuleSw_SPC_CP1LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1041)
)
_Hh3cevtModuleSw_SPC_CP2LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_CP2LB = _Hh3cevtModuleSw_SPC_CP2LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1042)
)
_Hh3cevtModuleSw_SPC_CP2LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_CP2LA = _Hh3cevtModuleSw_SPC_CP2LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1043)
)
_Hh3cevtModuleSw_SR05SRP1L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR05SRP1L1 = _Hh3cevtModuleSw_SR05SRP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1044)
)
_Hh3cevtModuleSw_SR05SRP1L3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR05SRP1L3 = _Hh3cevtModuleSw_SR05SRP1L3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1045)
)
_Hh3cevtModuleSw_SFC_04_4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_04_4 = _Hh3cevtModuleSw_SFC_04_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1046)
)
_Hh3cevtModuleSw_SFC_04_3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_04_3 = _Hh3cevtModuleSw_SFC_04_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1047)
)
_Hh3cevtModuleSw_SFC_04_2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_04_2 = _Hh3cevtModuleSw_SFC_04_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1048)
)
_Hh3cevtModuleSw_SFC_04_1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_04_1 = _Hh3cevtModuleSw_SFC_04_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1049)
)
_Hh3cevtModuleSw_LST1NSM2C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1NSM2C1 = _Hh3cevtModuleSw_LST1NSM2C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1050)
)
_Hh3cevtModuleSw_CR_SPC_XP20RB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CR_SPC_XP20RB = _Hh3cevtModuleSw_CR_SPC_XP20RB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1051)
)
_Hh3cevtModuleSw_SR07SRPUA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07SRPUA1 = _Hh3cevtModuleSw_SR07SRPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1052)
)
_Hh3cevtModuleSw_SR07SRPUB3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07SRPUB3 = _Hh3cevtModuleSw_SR07SRPUB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1053)
)
_Hh3cevtModuleSw_SR07SRPUC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07SRPUC3 = _Hh3cevtModuleSw_SR07SRPUC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1054)
)
_Hh3cevtModuleSw_SR07MPUA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07MPUA1 = _Hh3cevtModuleSw_SR07MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1055)
)
_Hh3cevtModuleSw_SR07SRPUB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07SRPUB1 = _Hh3cevtModuleSw_SR07SRPUB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1056)
)
_Hh3cevtModuleSw_SR07SRPUC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07SRPUC1 = _Hh3cevtModuleSw_SR07SRPUC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1057)
)
_Hh3cevtModuleSw_MIC_MS4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_MS4L = _Hh3cevtModuleSw_MIC_MS4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1058)
)
_Hh3cevtModuleSw_SPC_GP44XP4LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP44XP4LC = _Hh3cevtModuleSw_SPC_GP44XP4LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1059)
)
_Hh3cevtModuleSw_SPC_GP44XP4LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_GP44XP4LA = _Hh3cevtModuleSw_SPC_GP44XP4LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1060)
)
_Hh3cevtModuleSw_SPC_XLP2XP4LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XLP2XP4LC = _Hh3cevtModuleSw_SPC_XLP2XP4LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1061)
)
_Hh3cevtModuleSw_SPC_XP12LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP12LC = _Hh3cevtModuleSw_SPC_XP12LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1062)
)
_Hh3cevtModuleSw_SPC_CP1LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_CP1LC = _Hh3cevtModuleSw_SPC_CP1LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1063)
)
_Hh3cevtModuleSw_SPC_XP24LC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPC_XP24LC = _Hh3cevtModuleSw_SPC_XP24LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1064)
)
_Hh3cevtModuleSw_SR07SRPUD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07SRPUD3 = _Hh3cevtModuleSw_SR07SRPUD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1065)
)
_Hh3cevtModuleSw_SR07MPUA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07MPUA3 = _Hh3cevtModuleSw_SR07MPUA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1066)
)
_Hh3cevtModuleSw_MPEX_1304_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MPEX_1304 = _Hh3cevtModuleSw_MPEX_1304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1067)
)
_Hh3cevtModuleSw_MIC_GP10L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GP10L1 = _Hh3cevtModuleSw_MIC_GP10L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1068)
)
_Hh3cevtModuleSw_SR07SRPUB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07SRPUB = _Hh3cevtModuleSw_SR07SRPUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1069)
)
_Hh3cevtModuleSw_CMPE_1104_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CMPE_1104 = _Hh3cevtModuleSw_CMPE_1104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1070)
)
_Hh3cevtModuleSw_CSFC_04_1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_04_1 = _Hh3cevtModuleSw_CSFC_04_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1071)
)
_Hh3cevtModuleSw_CSFC_04_2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_04_2 = _Hh3cevtModuleSw_CSFC_04_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1072)
)
_Hh3cevtModuleSw_CSFC_04_3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_04_3 = _Hh3cevtModuleSw_CSFC_04_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1073)
)
_Hh3cevtModuleSw_CSFC_04_4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_04_4 = _Hh3cevtModuleSw_CSFC_04_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1074)
)
_Hh3cevtModuleSw_CSFC_04B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_04B = _Hh3cevtModuleSw_CSFC_04B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1075)
)
_Hh3cevtModuleSw_CSFC_04D_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_04D = _Hh3cevtModuleSw_CSFC_04D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1076)
)
_Hh3cevtModuleSw_CSFC_08B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_08B = _Hh3cevtModuleSw_CSFC_08B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1077)
)
_Hh3cevtModuleSw_CSFC_08D_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_08D = _Hh3cevtModuleSw_CSFC_08D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1078)
)
_Hh3cevtModuleSw_CSFC_12B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_12B = _Hh3cevtModuleSw_CSFC_12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1079)
)
_Hh3cevtModuleSw_CSFC_12D_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_12D = _Hh3cevtModuleSw_CSFC_12D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1080)
)
_Hh3cevtModuleSw_CSPC_CP1LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_CP1LCX = _Hh3cevtModuleSw_CSPC_CP1LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1081)
)
_Hh3cevtModuleSw_CSPC_CP2LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_CP2LB = _Hh3cevtModuleSw_CSPC_CP2LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1082)
)
_Hh3cevtModuleSw_CSPC_GP24LA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_GP24LA1 = _Hh3cevtModuleSw_CSPC_GP24LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1083)
)
_Hh3cevtModuleSw_CSPC_GP24XP2LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_GP24XP2LB = _Hh3cevtModuleSw_CSPC_GP24XP2LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1084)
)
_Hh3cevtModuleSw_CSPC_GP44XP4LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_GP44XP4LCX = _Hh3cevtModuleSw_CSPC_GP44XP4LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1085)
)
_Hh3cevtModuleSw_CSPC_GP48LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_GP48LB = _Hh3cevtModuleSw_CSPC_GP48LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1086)
)
_Hh3cevtModuleSw_CSPC_GT48LA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_GT48LA1 = _Hh3cevtModuleSw_CSPC_GT48LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1087)
)
_Hh3cevtModuleSw_CSPC_XLP6LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_XLP6LCX = _Hh3cevtModuleSw_CSPC_XLP6LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1088)
)
_Hh3cevtModuleSw_CSPC_XP2LA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_XP2LA1 = _Hh3cevtModuleSw_CSPC_XP2LA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1089)
)
_Hh3cevtModuleSw_CSPC_XP4LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_XP4LB = _Hh3cevtModuleSw_CSPC_XP4LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1090)
)
_Hh3cevtModuleSw_CSPC_XP8LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_XP8LB = _Hh3cevtModuleSw_CSPC_XP8LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1091)
)
_Hh3cevtModuleSw_CSPC_XP12LAX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_XP12LAX = _Hh3cevtModuleSw_CSPC_XP12LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1092)
)
_Hh3cevtModuleSw_CSPC_XP12LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_XP12LCX = _Hh3cevtModuleSw_CSPC_XP12LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1093)
)
_Hh3cevtModuleSw_CSPC_XP24LAX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_XP24LAX = _Hh3cevtModuleSw_CSPC_XP24LAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1094)
)
_Hh3cevtModuleSw_CSPC_XP24LCX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_XP24LCX = _Hh3cevtModuleSw_CSPC_XP24LCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1095)
)
_Hh3cevtModuleSw_CSPC_CSPEX_1204_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_CSPEX_1204 = _Hh3cevtModuleSw_CSPC_CSPEX_1204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1096)
)
_Hh3cevtModuleSw_CSR05SRP1L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR05SRP1L1 = _Hh3cevtModuleSw_CSR05SRP1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1097)
)
_Hh3cevtModuleSw_CSR05SRP1L3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR05SRP1L3 = _Hh3cevtModuleSw_CSR05SRP1L3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1098)
)
_Hh3cevtModuleSw_CSR07MPUA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR07MPUA1 = _Hh3cevtModuleSw_CSR07MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1099)
)
_Hh3cevtModuleSw_CSR07SRPUA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR07SRPUA1 = _Hh3cevtModuleSw_CSR07SRPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1100)
)
_Hh3cevtModuleSw_CSR07SRPUB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR07SRPUB1 = _Hh3cevtModuleSw_CSR07SRPUB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1101)
)
_Hh3cevtModuleSw_CSR07SRPUC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR07SRPUC1 = _Hh3cevtModuleSw_CSR07SRPUC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1102)
)
_Hh3cevtModuleSw_LSXM1CGX8FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGX8FX1 = _Hh3cevtModuleSw_LSXM1CGX8FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1103)
)
_Hh3cevtModuleSw_LSXM1QGS24FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24FX1 = _Hh3cevtModuleSw_LSXM1QGS24FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1104)
)
_Hh3cevtModuleSw_LSXM1TGS48FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48FX1 = _Hh3cevtModuleSw_LSXM1TGS48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1105)
)
_Hh3cevtModuleSw_LSXM1QGS12FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS12FX1 = _Hh3cevtModuleSw_LSXM1QGS12FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1106)
)
_Hh3cevtModuleSw_LSXM1TGT48FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGT48FX1 = _Hh3cevtModuleSw_LSXM1TGT48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1107)
)
_Hh3cevtModuleSw_LSU1IPSBEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1IPSBEA0 = _Hh3cevtModuleSw_LSU1IPSBEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1108)
)
_Hh3cevtModuleSw_PIC_GP10L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_GP10L = _Hh3cevtModuleSw_PIC_GP10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1109)
)
_Hh3cevtModuleSw_PIC_XP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_XP1L = _Hh3cevtModuleSw_PIC_XP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1110)
)
_Hh3cevtModuleSw_PIC_PUP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_PUP1L = _Hh3cevtModuleSw_PIC_PUP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1111)
)
_Hh3cevtModuleSw_PIC_PSP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_PSP4L = _Hh3cevtModuleSw_PIC_PSP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1112)
)
_Hh3cevtModuleSw_PIC_PS2G4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_PS2G4L = _Hh3cevtModuleSw_PIC_PS2G4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1113)
)
_Hh3cevtModuleSw_PIC_PL2G6L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_PL2G6L = _Hh3cevtModuleSw_PIC_PL2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1114)
)
_Hh3cevtModuleSw_PIC_TCP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_TCP8L = _Hh3cevtModuleSw_PIC_TCP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1115)
)
_Hh3cevtModuleSw_PIC_CSP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_CSP1L = _Hh3cevtModuleSw_PIC_CSP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1116)
)
_Hh3cevtModuleSw_PIC_PH2G6L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_PIC_PH2G6L = _Hh3cevtModuleSw_PIC_PH2G6L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1117)
)
_Hh3cevtModuleSw_LSXM1CGP12FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGP12FX1 = _Hh3cevtModuleSw_LSXM1CGP12FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1118)
)
_Hh3cevtModuleSw_LSXM1CGP8FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGP8FX1 = _Hh3cevtModuleSw_LSXM1CGP8FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1119)
)
_Hh3cevtModuleSw_LSXM1GT48FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GT48FX1 = _Hh3cevtModuleSw_LSXM1GT48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1120)
)
_Hh3cevtModuleSw_LSXM1GT48FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GT48FX0 = _Hh3cevtModuleSw_LSXM1GT48FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1121)
)
_Hh3cevtModuleSw_LSXM1GP48FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP48FX1 = _Hh3cevtModuleSw_LSXM1GP48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1122)
)
_Hh3cevtModuleSw_LSXM1GP48FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP48FX0 = _Hh3cevtModuleSw_LSXM1GP48FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1123)
)
_Hh3cevtModuleSw_LSXM1TGS24FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS24FX0 = _Hh3cevtModuleSw_LSXM1TGS24FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1124)
)
_Hh3cevtModuleSw_LSXM1TGS24FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS24FX1 = _Hh3cevtModuleSw_LSXM1TGS24FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1125)
)
_Hh3cevtModuleSw_MIC_SP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_SP8L = _Hh3cevtModuleSw_MIC_SP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1126)
)
_Hh3cevtModuleSw_LSXM1TGS48FE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48FE1 = _Hh3cevtModuleSw_LSXM1TGS48FE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1127)
)
_Hh3cevtModuleSw_LSXM1QGS24FE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24FE1 = _Hh3cevtModuleSw_LSXM1QGS24FE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1128)
)
_Hh3cevtModuleSw_CSPEX_1504S_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1504S = _Hh3cevtModuleSw_CSPEX_1504S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1129)
)
_Hh3cevtModuleSw_CSPEX_1504X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1504X = _Hh3cevtModuleSw_CSPEX_1504X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1130)
)
_Hh3cevtModuleSw_CSPEX_1404S_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1404S = _Hh3cevtModuleSw_CSPEX_1404S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1131)
)
_Hh3cevtModuleSw_CSPEX_1304S_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1304S = _Hh3cevtModuleSw_CSPEX_1304S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1132)
)
_Hh3cevtModuleSw_CSPEX_1404X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1404X = _Hh3cevtModuleSw_CSPEX_1404X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1133)
)
_Hh3cevtModuleSw_CSPEX_1304X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1304X = _Hh3cevtModuleSw_CSPEX_1304X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1134)
)
_Hh3cevtModuleSw_MIC_XP5L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP5L = _Hh3cevtModuleSw_MIC_XP5L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1135)
)
_Hh3cevtModuleSw_MIC_XP2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP2L = _Hh3cevtModuleSw_MIC_XP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1136)
)
_Hh3cevtModuleSw_MIC_CP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CP1L = _Hh3cevtModuleSw_MIC_CP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1137)
)
_Hh3cevtModuleSw_MIC_GP20L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GP20L = _Hh3cevtModuleSw_MIC_GP20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1138)
)
_Hh3cevtModuleSw_MIC_GT20L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GT20L = _Hh3cevtModuleSw_MIC_GT20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1139)
)
_Hh3cevtModuleSw_CEPC_XP48RX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_XP48RX = _Hh3cevtModuleSw_CEPC_XP48RX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1140)
)
_Hh3cevtModuleSw_CEPC_CP4RX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_CP4RX = _Hh3cevtModuleSw_CEPC_CP4RX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1141)
)
_Hh3cevtModuleSw_MIC_GP10L_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GP10L_V2 = _Hh3cevtModuleSw_MIC_GP10L_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1142)
)
_Hh3cevtModuleSw_CSR07SRPUD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR07SRPUD3 = _Hh3cevtModuleSw_CSR07SRPUD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1143)
)
_Hh3cevtModuleSw_MIC_XP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP1L = _Hh3cevtModuleSw_MIC_XP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1144)
)
_Hh3cevtModuleSw_CSFC_12E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_12E = _Hh3cevtModuleSw_CSFC_12E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1145)
)
_Hh3cevtModuleSw_CEPC_XP24LX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_XP24LX = _Hh3cevtModuleSw_CEPC_XP24LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1146)
)
_Hh3cevtModuleSw_IM_MSUX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_MSUX = _Hh3cevtModuleSw_IM_MSUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1147)
)
_Hh3cevtModuleSw_CSFC_12F_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_12F = _Hh3cevtModuleSw_CSFC_12F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1148)
)
_Hh3cevtModuleSw_CSR05SRP1N3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR05SRP1N3 = _Hh3cevtModuleSw_CSR05SRP1N3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1149)
)
_Hh3cevtModuleSw_CSPEX_1602X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1602X = _Hh3cevtModuleSw_CSPEX_1602X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1150)
)
_Hh3cevtModuleSw_MIC_XP20L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP20L = _Hh3cevtModuleSw_MIC_XP20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1151)
)
_Hh3cevtModuleSw_MIC_CP2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CP2L = _Hh3cevtModuleSw_MIC_CP2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1152)
)
_Hh3cevtModuleSw_IM_NGFWX_IV_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_NGFWX_IV = _Hh3cevtModuleSw_IM_NGFWX_IV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1153)
)
_Hh3cevtModuleSw_SFC_12E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_12E = _Hh3cevtModuleSw_SFC_12E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1154)
)
_Hh3cevtModuleSw_SPEX_1602X_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPEX_1602X_E = _Hh3cevtModuleSw_SPEX_1602X_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1155)
)
_Hh3cevtModuleSw_SPEX_1602X_L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPEX_1602X_L = _Hh3cevtModuleSw_SPEX_1602X_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1156)
)
_Hh3cevtModuleSw_EPC_XP24LX_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EPC_XP24LX_E = _Hh3cevtModuleSw_EPC_XP24LX_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1157)
)
_Hh3cevtModuleSw_EPC_XP24LX_L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EPC_XP24LX_L = _Hh3cevtModuleSw_EPC_XP24LX_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1158)
)
_Hh3cevtModuleSw_EPC_CP4RX_L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EPC_CP4RX_L = _Hh3cevtModuleSw_EPC_CP4RX_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1159)
)
_Hh3cevtModuleSw_SPEX_1504X_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPEX_1504X_E = _Hh3cevtModuleSw_SPEX_1504X_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1160)
)
_Hh3cevtModuleSw_SPEX_1504X_L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SPEX_1504X_L = _Hh3cevtModuleSw_SPEX_1504X_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1161)
)
_Hh3cevtModuleSw_CSPEX_1602X_L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1602X_L = _Hh3cevtModuleSw_CSPEX_1602X_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1162)
)
_Hh3cevtModuleSw_CEPC_XP24LX_L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_XP24LX_L = _Hh3cevtModuleSw_CEPC_XP24LX_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1163)
)
_Hh3cevtModuleSw_CEPC_CP4RX_L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_CP4RX_L = _Hh3cevtModuleSw_CEPC_CP4RX_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1164)
)
_Hh3cevtModuleSw_MIC_CP1L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CP1L_E = _Hh3cevtModuleSw_MIC_CP1L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1165)
)
_Hh3cevtModuleSw_MIC_XP4L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP4L_E = _Hh3cevtModuleSw_MIC_XP4L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1166)
)
_Hh3cevtModuleSw_MIC_XP16L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP16L_E = _Hh3cevtModuleSw_MIC_XP16L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1167)
)
_Hh3cevtModuleSw_MIC_GP20L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GP20L_E = _Hh3cevtModuleSw_MIC_GP20L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1168)
)
_Hh3cevtModuleSw_MIC_GP10L_V2_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GP10L_V2_E = _Hh3cevtModuleSw_MIC_GP10L_V2_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1169)
)
_Hh3cevtModuleSw_MIC_GT20L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GT20L_E = _Hh3cevtModuleSw_MIC_GT20L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1170)
)
_Hh3cevtModuleSw_CSR05SRP1P3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR05SRP1P3 = _Hh3cevtModuleSw_CSR05SRP1P3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1171)
)
_Hh3cevtModuleSw_SR05SRP1P3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR05SRP1P3 = _Hh3cevtModuleSw_SR05SRP1P3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1172)
)
_Hh3cevtModuleSw_CSFC_16E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_16E = _Hh3cevtModuleSw_CSFC_16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1173)
)
_Hh3cevtModuleSw_SFC_16E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_16E = _Hh3cevtModuleSw_SFC_16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1174)
)
_Hh3cevtModuleSw_CSFC_08E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_08E = _Hh3cevtModuleSw_CSFC_08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1175)
)
_Hh3cevtModuleSw_SFC_08E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_08E = _Hh3cevtModuleSw_SFC_08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1176)
)
_Hh3cevtModuleSw_IM_SMUX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_SMUX = _Hh3cevtModuleSw_IM_SMUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1177)
)
_Hh3cevtModuleSw_IM_IPSX_IV_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_IPSX_IV = _Hh3cevtModuleSw_IM_IPSX_IV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1178)
)
_Hh3cevtModuleSw_IM_ACGX_IV_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_ACGX_IV = _Hh3cevtModuleSw_IM_ACGX_IV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1179)
)
_Hh3cevtModuleSw_SFC_08E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_08E1 = _Hh3cevtModuleSw_SFC_08E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1180)
)
_Hh3cevtModuleSw_CSFC_08E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_08E1 = _Hh3cevtModuleSw_CSFC_08E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1181)
)
_Hh3cevtModuleSw_IM_ACG1000X_IV_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_ACG1000X_IV = _Hh3cevtModuleSw_IM_ACG1000X_IV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1182)
)
_Hh3cevtModuleSw_MIC_QP1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_QP1L = _Hh3cevtModuleSw_MIC_QP1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1183)
)
_Hh3cevtModuleSw_CSPEX_1804X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1804X = _Hh3cevtModuleSw_CSPEX_1804X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1184)
)
_Hh3cevtModuleSw_MIC_CP2L_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CP2L_V2 = _Hh3cevtModuleSw_MIC_CP2L_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1185)
)
_Hh3cevtModuleSw_MIC_XP4L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP4L1 = _Hh3cevtModuleSw_MIC_XP4L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1186)
)
_Hh3cevtModuleSw_SFC_16T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_16T = _Hh3cevtModuleSw_SFC_16T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1187)
)
_Hh3cevtModuleSw_CSFC_16T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_16T = _Hh3cevtModuleSw_CSFC_16T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1188)
)
_Hh3cevtModuleSw_SFC_08T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_08T = _Hh3cevtModuleSw_SFC_08T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1189)
)
_Hh3cevtModuleSw_CSFC_08T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_08T = _Hh3cevtModuleSw_CSFC_08T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1190)
)
_Hh3cevtModuleSw_MIC_XP2L_LAN_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP2L_LAN = _Hh3cevtModuleSw_MIC_XP2L_LAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1191)
)
_Hh3cevtModuleSw_MIC_XP5L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP5L1 = _Hh3cevtModuleSw_MIC_XP5L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1192)
)
_Hh3cevtModuleSw_MIC_CP1L_V2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CP1L_V2 = _Hh3cevtModuleSw_MIC_CP1L_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1193)
)
_Hh3cevtModuleSw_CEPC_XP40LX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_XP40LX = _Hh3cevtModuleSw_CEPC_XP40LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1194)
)
_Hh3cevtModuleSw_CEPC_CQ4LX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_CQ4LX = _Hh3cevtModuleSw_CEPC_CQ4LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1195)
)
_Hh3cevtModuleSw_LSU1QGC4SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1QGC4SF0 = _Hh3cevtModuleSw_LSU1QGC4SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1201)
)
_Hh3cevtModuleSw_LSU1QGS8SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1QGS8SF0 = _Hh3cevtModuleSw_LSU1QGS8SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1202)
)
_Hh3cevtModuleSw_LSU1TGS48SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS48SF0 = _Hh3cevtModuleSw_LSU1TGS48SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1203)
)
_Hh3cevtModuleSw_LSU1QGS4SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1QGS4SF0 = _Hh3cevtModuleSw_LSU1QGS4SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1204)
)
_Hh3cevtModuleSw_LSU1TGS32SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS32SF0 = _Hh3cevtModuleSw_LSU1TGS32SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1205)
)
_Hh3cevtModuleSw_LSU1FAB08D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB08D0 = _Hh3cevtModuleSw_LSU1FAB08D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1206)
)
_Hh3cevtModuleSw_LSU1FAB04B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB04B0 = _Hh3cevtModuleSw_LSU1FAB04B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1207)
)
_Hh3cevtModuleSw_LSU1FAB08B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB08B0 = _Hh3cevtModuleSw_LSU1FAB08B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1208)
)
_Hh3cevtModuleSw_LSU1FAB12D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB12D0 = _Hh3cevtModuleSw_LSU1FAB12D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1209)
)
_Hh3cevtModuleSw_LSU1FAB12B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB12B0 = _Hh3cevtModuleSw_LSU1FAB12B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1210)
)
_Hh3cevtModuleSw_LSU1FAB04D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB04D0 = _Hh3cevtModuleSw_LSU1FAB04D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1211)
)
_Hh3cevtModuleSw_LSQ1CTGS16SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CTGS16SC0 = _Hh3cevtModuleSw_LSQ1CTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1212)
)
_Hh3cevtModuleSw_EWPX2CTGS16SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX2CTGS16SC0 = _Hh3cevtModuleSw_EWPX2CTGS16SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1213)
)
_Hh3cevtModuleSw_LSU3WCMD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU3WCMD0 = _Hh3cevtModuleSw_LSU3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1214)
)
_Hh3cevtModuleSw_EWPX3WCMD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX3WCMD0 = _Hh3cevtModuleSw_EWPX3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1215)
)
_Hh3cevtModuleSw_LSQ1QGS4SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1QGS4SC0 = _Hh3cevtModuleSw_LSQ1QGS4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1216)
)
_Hh3cevtModuleSw_LSQ1QGC4SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1QGC4SC0 = _Hh3cevtModuleSw_LSQ1QGC4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1217)
)
_Hh3cevtModuleSw_LSU1TGT24SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGT24SF0 = _Hh3cevtModuleSw_LSU1TGT24SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1218)
)
_Hh3cevtModuleSw_LSQ1QGS8SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1QGS8SC3 = _Hh3cevtModuleSw_LSQ1QGS8SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1219)
)
_Hh3cevtModuleSw_LSQ1TGS32SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS32SC3 = _Hh3cevtModuleSw_LSQ1TGS32SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1220)
)
_Hh3cevtModuleSw_LSQ1QGS4SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1QGS4SC3 = _Hh3cevtModuleSw_LSQ1QGS4SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1221)
)
_Hh3cevtModuleSw_LSQ1TGS48SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS48SC3 = _Hh3cevtModuleSw_LSQ1TGS48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1222)
)
_Hh3cevtModuleSw_LSQ1QGC4SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1QGC4SC3 = _Hh3cevtModuleSw_LSQ1QGC4SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1223)
)
_Hh3cevtModuleSw_LSQ1FAB12D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB12D3 = _Hh3cevtModuleSw_LSQ1FAB12D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1224)
)
_Hh3cevtModuleSw_LSQ1FAB08D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB08D3 = _Hh3cevtModuleSw_LSQ1FAB08D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1225)
)
_Hh3cevtModuleSw_LSQ1FAB04D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB04D3 = _Hh3cevtModuleSw_LSQ1FAB04D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1226)
)
_Hh3cevtModuleSw_LSQ1TGS8EB3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS8EB3 = _Hh3cevtModuleSw_LSQ1TGS8EB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1227)
)
_Hh3cevtModuleSw_LSQ1TGT24SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGT24SC3 = _Hh3cevtModuleSw_LSQ1TGT24SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1228)
)
_Hh3cevtModuleSw_LSQ1FAB08B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1FAB08B0 = _Hh3cevtModuleSw_LSQ1FAB08B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1229)
)
_Hh3cevtModuleSw_EWPX2CTGS16SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX2CTGS16SC = _Hh3cevtModuleSw_EWPX2CTGS16SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1230)
)
_Hh3cevtModuleSw_LSU1SUPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1SUPB0 = _Hh3cevtModuleSw_LSU1SUPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1231)
)
_Hh3cevtModuleSw_LSQ1GP48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SA0 = _Hh3cevtModuleSw_LSQ1GP48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1232)
)
_Hh3cevtModuleSw_LSQ1TGX2SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGX2SA0 = _Hh3cevtModuleSw_LSQ1TGX2SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1233)
)
_Hh3cevtModuleSw_LSV1SRPUA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSV1SRPUA1 = _Hh3cevtModuleSw_LSV1SRPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1234)
)
_Hh3cevtModuleSw_LSV1QGS12SA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSV1QGS12SA1 = _Hh3cevtModuleSw_LSV1QGS12SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1235)
)
_Hh3cevtModuleSw_LSV1MPUA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSV1MPUA1 = _Hh3cevtModuleSw_LSV1MPUA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1236)
)
_Hh3cevtModuleSw_LSX1SUP10A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP10A0 = _Hh3cevtModuleSw_LSX1SUP10A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1237)
)
_Hh3cevtModuleSw_LSX1SUP16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP16A0 = _Hh3cevtModuleSw_LSX1SUP16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1238)
)
_Hh3cevtModuleSw_LSX1SUP10A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP10A1 = _Hh3cevtModuleSw_LSX1SUP10A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1239)
)
_Hh3cevtModuleSw_LSX1SUP16A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP16A1 = _Hh3cevtModuleSw_LSX1SUP16A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1240)
)
_Hh3cevtModuleSw_LSX1FAB10B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FAB10B0 = _Hh3cevtModuleSw_LSX1FAB10B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1241)
)
_Hh3cevtModuleSw_LSX1FAB16B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FAB16B0 = _Hh3cevtModuleSw_LSX1FAB16B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1242)
)
_Hh3cevtModuleSw_LSX1FAB10B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FAB10B1 = _Hh3cevtModuleSw_LSX1FAB10B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1243)
)
_Hh3cevtModuleSw_LSX1FAB16B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FAB16B1 = _Hh3cevtModuleSw_LSX1FAB16B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1244)
)
_Hh3cevtModuleSw_LSX1QGS16EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS16EA0 = _Hh3cevtModuleSw_LSX1QGS16EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1245)
)
_Hh3cevtModuleSw_LSX1TGS48EA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS48EA0 = _Hh3cevtModuleSw_LSX1TGS48EA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1246)
)
_Hh3cevtModuleSw_LSX1QGS16EA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS16EA1 = _Hh3cevtModuleSw_LSX1QGS16EA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1247)
)
_Hh3cevtModuleSw_LSX1TGS48EA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS48EA1 = _Hh3cevtModuleSw_LSX1TGS48EA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1248)
)
_Hh3cevtModuleSw_LSU1TGT24SF9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGT24SF9 = _Hh3cevtModuleSw_LSU1TGT24SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1249)
)
_Hh3cevtModuleSw_LSU1QGS8SF9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1QGS8SF9 = _Hh3cevtModuleSw_LSU1QGS8SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1250)
)
_Hh3cevtModuleSw_LSU1QGS4SF9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1QGS4SF9 = _Hh3cevtModuleSw_LSU1QGS4SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1251)
)
_Hh3cevtModuleSw_LSU1TGS48SF9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS48SF9 = _Hh3cevtModuleSw_LSU1TGS48SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1252)
)
_Hh3cevtModuleSw_LSU1TGS32SF9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS32SF9 = _Hh3cevtModuleSw_LSU1TGS32SF9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1253)
)
_Hh3cevtModuleSw_LSU1FAB08D9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1FAB08D9 = _Hh3cevtModuleSw_LSU1FAB08D9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1254)
)
_Hh3cevtModuleSw_LSU1SUPB9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1SUPB9 = _Hh3cevtModuleSw_LSU1SUPB9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1255)
)
_Hh3cevtModuleSw_LSQ3GV48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ3GV48SC0 = _Hh3cevtModuleSw_LSQ3GV48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1256)
)
_Hh3cevtModuleSw_LSX1QGS12EC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS12EC1 = _Hh3cevtModuleSw_LSX1QGS12EC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1257)
)
_Hh3cevtModuleSw_LSX1QGS12EC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS12EC0 = _Hh3cevtModuleSw_LSX1QGS12EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1258)
)
_Hh3cevtModuleSw_LSX1TGS48EC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS48EC0 = _Hh3cevtModuleSw_LSX1TGS48EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1259)
)
_Hh3cevtModuleSw_LSX1TGS48EC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS48EC1 = _Hh3cevtModuleSw_LSX1TGS48EC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1260)
)
_Hh3cevtModuleSw_LSX1TGS24EC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS24EC0 = _Hh3cevtModuleSw_LSX1TGS24EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1261)
)
_Hh3cevtModuleSw_LSX1TGS24EC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS24EC1 = _Hh3cevtModuleSw_LSX1TGS24EC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1262)
)
_Hh3cevtModuleSw_LSX1FAB10A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FAB10A0 = _Hh3cevtModuleSw_LSX1FAB10A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1263)
)
_Hh3cevtModuleSw_LSX1FAB16A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FAB16A1 = _Hh3cevtModuleSw_LSX1FAB16A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1264)
)
_Hh3cevtModuleSw_LSX1QGS12FB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS12FB0 = _Hh3cevtModuleSw_LSX1QGS12FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1265)
)
_Hh3cevtModuleSw_LSX1TGS24FB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS24FB0 = _Hh3cevtModuleSw_LSX1TGS24FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1266)
)
_Hh3cevtModuleSw_LSX1TGS48FB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS48FB0 = _Hh3cevtModuleSw_LSX1TGS48FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1267)
)
_Hh3cevtModuleSw_LSX1QGS12EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS12EB1 = _Hh3cevtModuleSw_LSX1QGS12EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1268)
)
_Hh3cevtModuleSw_LSX1TGS24EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS24EB1 = _Hh3cevtModuleSw_LSX1TGS24EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1269)
)
_Hh3cevtModuleSw_LSX1FAB10A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FAB10A1 = _Hh3cevtModuleSw_LSX1FAB10A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1270)
)
_Hh3cevtModuleSw_LSX1TGS48EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1TGS48EB1 = _Hh3cevtModuleSw_LSX1TGS48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1271)
)
_Hh3cevtModuleSw_LSX1GP48EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1GP48EB1 = _Hh3cevtModuleSw_LSX1GP48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1272)
)
_Hh3cevtModuleSw_LSX1GP48FB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1GP48FB0 = _Hh3cevtModuleSw_LSX1GP48FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1273)
)
_Hh3cevtModuleSw_LSX1GT48FC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1GT48FC0 = _Hh3cevtModuleSw_LSX1GT48FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1274)
)
_Hh3cevtModuleSw_LSX1GT48FC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1GT48FC1 = _Hh3cevtModuleSw_LSX1GT48FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1275)
)
_Hh3cevtModuleSw_LSX1GP48FC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1GP48FC0 = _Hh3cevtModuleSw_LSX1GP48FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1276)
)
_Hh3cevtModuleSw_LSX1GP48FC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1GP48FC1 = _Hh3cevtModuleSw_LSX1GP48FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1277)
)
_Hh3cevtModuleSw_LSX1QGS12FC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS12FC0 = _Hh3cevtModuleSw_LSX1QGS12FC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1278)
)
_Hh3cevtModuleSw_LSX1QGS12FC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1QGS12FC1 = _Hh3cevtModuleSw_LSX1QGS12FC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1279)
)
_Hh3cevtModuleSw_LSX2TGS48EA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX2TGS48EA1 = _Hh3cevtModuleSw_LSX2TGS48EA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1280)
)
_Hh3cevtModuleSw_LSX1CGC4EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1CGC4EB1 = _Hh3cevtModuleSw_LSX1CGC4EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1281)
)
_Hh3cevtModuleSw_LSX1CGC4EC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1CGC4EC0 = _Hh3cevtModuleSw_LSX1CGC4EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1282)
)
_Hh3cevtModuleSw_LSX1GT48EB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1GT48EB1 = _Hh3cevtModuleSw_LSX1GT48EB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1283)
)
_Hh3cevtModuleSw_LSX1GT48FB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1GT48FB0 = _Hh3cevtModuleSw_LSX1GT48FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1284)
)
_Hh3cevtModuleSw_LSX1FAB16S1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FAB16S1 = _Hh3cevtModuleSw_LSX1FAB16S1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1285)
)
_Hh3cevtModuleSw_LSQ1SUPB3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SUPB3 = _Hh3cevtModuleSw_LSQ1SUPB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1286)
)
_Hh3cevtModuleSw_LSU1CGC2SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1CGC2SE0 = _Hh3cevtModuleSw_LSU1CGC2SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1287)
)
_Hh3cevtModuleSw_LSU1TGS16SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS16SF0 = _Hh3cevtModuleSw_LSU1TGS16SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1288)
)
_Hh3cevtModuleSw_LSU1TGS8SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1TGS8SF0 = _Hh3cevtModuleSw_LSU1TGS8SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1289)
)
_Hh3cevtModuleSw_LSQ1TGS4SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS4SC0 = _Hh3cevtModuleSw_LSQ1TGS4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1290)
)
_Hh3cevtModuleSw_LSU1GT48SE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GT48SE3 = _Hh3cevtModuleSw_LSU1GT48SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1291)
)
_Hh3cevtModuleSw_LSU1GP48SE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP48SE3 = _Hh3cevtModuleSw_LSU1GP48SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1292)
)
_Hh3cevtModuleSw_LSX1SUP10B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP10B0 = _Hh3cevtModuleSw_LSX1SUP10B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1293)
)
_Hh3cevtModuleSw_LSX1SUP16B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP16B0 = _Hh3cevtModuleSw_LSX1SUP16B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1294)
)
_Hh3cevtModuleSw_LSX1SUP10B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP10B1 = _Hh3cevtModuleSw_LSX1SUP10B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1295)
)
_Hh3cevtModuleSw_LSX1SUP16B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP16B1 = _Hh3cevtModuleSw_LSX1SUP16B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1296)
)
_Hh3cevtModuleSw_LSQ1CGV24PSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGV24PSC3 = _Hh3cevtModuleSw_LSQ1CGV24PSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1297)
)
_Hh3cevtModuleSw_LSQ1SRPA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1SRPA8 = _Hh3cevtModuleSw_LSQ1SRPA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1298)
)
_Hh3cevtModuleSw_LSQ1CGP24TSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGP24TSC8 = _Hh3cevtModuleSw_LSQ1CGP24TSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1299)
)
_Hh3cevtModuleSw_LSQ1CGT24PSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1CGT24PSC8 = _Hh3cevtModuleSw_LSQ1CGT24PSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1300)
)
_Hh3cevtModuleSw_LSQ1GT24PSA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GT24PSA8 = _Hh3cevtModuleSw_LSQ1GT24PSA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1301)
)
_Hh3cevtModuleSw_LSQ1GP24TSA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP24TSA8 = _Hh3cevtModuleSw_LSQ1GP24TSA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1302)
)
_Hh3cevtModuleSw_LSQ1GT48SA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GT48SA8 = _Hh3cevtModuleSw_LSQ1GT48SA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1303)
)
_Hh3cevtModuleSw_LSQ1GP48SA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1GP48SA8 = _Hh3cevtModuleSw_LSQ1GP48SA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1304)
)
_Hh3cevtModuleSw_LSQ1TGS4SC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS4SC8 = _Hh3cevtModuleSw_LSQ1TGS4SC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1305)
)
_Hh3cevtModuleSw_LSQ1TGS8SC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ1TGS8SC8 = _Hh3cevtModuleSw_LSQ1TGS8SC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1306)
)
_Hh3cevtModuleSw_LSU1GT24SE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GT24SE3 = _Hh3cevtModuleSw_LSU1GT24SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1307)
)
_Hh3cevtModuleSw_LSU1GP12SE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP12SE3 = _Hh3cevtModuleSw_LSU1GP12SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1308)
)
_Hh3cevtModuleSw_LSU1GP24SE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24SE3 = _Hh3cevtModuleSw_LSU1GP24SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1309)
)
_Hh3cevtModuleSw_LSU1T24XGSE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1T24XGSE3 = _Hh3cevtModuleSw_LSU1T24XGSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1310)
)
_Hh3cevtModuleSw_LSU1P24XGSE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1P24XGSE3 = _Hh3cevtModuleSw_LSU1P24XGSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1311)
)
_Hh3cevtModuleSw_LSU1GP24TSE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GP24TSE3 = _Hh3cevtModuleSw_LSU1GP24TSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1312)
)
_Hh3cevtModuleSw_LSU1GT40PSE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1GT40PSE3 = _Hh3cevtModuleSw_LSU1GT40PSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1313)
)
_Hh3cevtModuleSw_LSV1TGS24SA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSV1TGS24SA1 = _Hh3cevtModuleSw_LSV1TGS24SA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1314)
)
_Hh3cevtModuleSw_LSVM1SRPA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1SRPA1 = _Hh3cevtModuleSw_LSVM1SRPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1315)
)
_Hh3cevtModuleSw_LSVM1SRPC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1SRPC1 = _Hh3cevtModuleSw_LSVM1SRPC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1316)
)
_Hh3cevtModuleSw_LSX1FAB16S0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FAB16S0 = _Hh3cevtModuleSw_LSX1FAB16S0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1317)
)
_Hh3cevtModuleSw_LSU1WCME0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1WCME0 = _Hh3cevtModuleSw_LSU1WCME0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1318)
)
_Hh3cevtModuleSw_EWPX1WCME0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPX1WCME0 = _Hh3cevtModuleSw_EWPX1WCME0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1319)
)
_Hh3cevtModuleSw_LSUM1TGS48SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS48SG0 = _Hh3cevtModuleSw_LSUM1TGS48SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1320)
)
_Hh3cevtModuleSw_LSUM1QGS12SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1QGS12SG0 = _Hh3cevtModuleSw_LSUM1QGS12SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1321)
)
_Hh3cevtModuleSw_LSUM1GP44TSEC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GP44TSEC0 = _Hh3cevtModuleSw_LSUM1GP44TSEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1322)
)
_Hh3cevtModuleSw_LSUM1TGS24EC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS24EC0 = _Hh3cevtModuleSw_LSUM1TGS24EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1323)
)
_Hh3cevtModuleSw_LSUM1QGS6EC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1QGS6EC0 = _Hh3cevtModuleSw_LSUM1QGS6EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1324)
)
_Hh3cevtModuleSw_LSUM1CGC2EC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGC2EC0 = _Hh3cevtModuleSw_LSUM1CGC2EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1325)
)
_Hh3cevtModuleSw_LSU1CGC2SE9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1CGC2SE9 = _Hh3cevtModuleSw_LSU1CGC2SE9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1326)
)
_Hh3cevtModuleSw_LSXM1QGS24EX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24EX1 = _Hh3cevtModuleSw_LSXM1QGS24EX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1327)
)
_Hh3cevtModuleSw_LSXM1QGS24FB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24FB0 = _Hh3cevtModuleSw_LSXM1QGS24FB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1328)
)
_Hh3cevtModuleSw_LSVM1QGS12FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1QGS12FX1 = _Hh3cevtModuleSw_LSVM1QGS12FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1329)
)
_Hh3cevtModuleSw_LSVM1TGS24FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1TGS24FX1 = _Hh3cevtModuleSw_LSVM1TGS24FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1330)
)
_Hh3cevtModuleSw_LSVM1QGS6C2FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1QGS6C2FX1 = _Hh3cevtModuleSw_LSVM1QGS6C2FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1331)
)
_Hh3cevtModuleSw_LSQM2GP44TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP44TSSC0 = _Hh3cevtModuleSw_LSQM2GP44TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1332)
)
_Hh3cevtModuleSw_LSQM2GP44TSSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP44TSSC3 = _Hh3cevtModuleSw_LSQM2GP44TSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1333)
)
_Hh3cevtModuleSw_LSQM2GP24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP24TSSC0 = _Hh3cevtModuleSw_LSQM2GP24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1334)
)
_Hh3cevtModuleSw_LSQM2GP24TSSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP24TSSC3 = _Hh3cevtModuleSw_LSQM2GP24TSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1335)
)
_Hh3cevtModuleSw_LSQM2GT24PTSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT24PTSSC0 = _Hh3cevtModuleSw_LSQM2GT24PTSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1336)
)
_Hh3cevtModuleSw_LSQM2GT24PTSSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT24PTSSC3 = _Hh3cevtModuleSw_LSQM2GT24PTSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1337)
)
_Hh3cevtModuleSw_LSQM2GT24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT24TSSC0 = _Hh3cevtModuleSw_LSQM2GT24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1338)
)
_Hh3cevtModuleSw_LSQM2GT24TSSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT24TSSC3 = _Hh3cevtModuleSw_LSQM2GT24TSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1339)
)
_Hh3cevtModuleSw_LSQM2GT48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT48SC0 = _Hh3cevtModuleSw_LSQM2GT48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1340)
)
_Hh3cevtModuleSw_LSQM2GT48SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT48SC3 = _Hh3cevtModuleSw_LSQM2GT48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1341)
)
_Hh3cevtModuleSw_LSQM4GV48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM4GV48SC0 = _Hh3cevtModuleSw_LSQM4GV48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1342)
)
_Hh3cevtModuleSw_LSQM4GV48SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM4GV48SC3 = _Hh3cevtModuleSw_LSQM4GV48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1343)
)
_Hh3cevtModuleSw_LSQM2TGS16SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2TGS16SF0 = _Hh3cevtModuleSw_LSQM2TGS16SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1344)
)
_Hh3cevtModuleSw_LSQM2TGS16SF3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2TGS16SF3 = _Hh3cevtModuleSw_LSQM2TGS16SF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1345)
)
_Hh3cevtModuleSw_LSQM2MPUD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2MPUD0 = _Hh3cevtModuleSw_LSQM2MPUD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1346)
)
_Hh3cevtModuleSw_LSQM2MPUD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2MPUD3 = _Hh3cevtModuleSw_LSQM2MPUD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1347)
)
_Hh3cevtModuleSw_LSQM3MPUA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM3MPUA0 = _Hh3cevtModuleSw_LSQM3MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1348)
)
_Hh3cevtModuleSw_LSQM3MPUA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM3MPUA3 = _Hh3cevtModuleSw_LSQM3MPUA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1349)
)
_Hh3cevtModuleSw_LSUM2GP44TSSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GP44TSSE0 = _Hh3cevtModuleSw_LSUM2GP44TSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1350)
)
_Hh3cevtModuleSw_LSUM2GP44TSSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GP44TSSC3 = _Hh3cevtModuleSw_LSUM2GP44TSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1351)
)
_Hh3cevtModuleSw_LSUM2GP24TSSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GP24TSSE0 = _Hh3cevtModuleSw_LSUM2GP24TSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1352)
)
_Hh3cevtModuleSw_LSUM2GP24TSSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GP24TSSC3 = _Hh3cevtModuleSw_LSUM2GP24TSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1353)
)
_Hh3cevtModuleSw_LSUM2GT24PTSSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GT24PTSSE0 = _Hh3cevtModuleSw_LSUM2GT24PTSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1354)
)
_Hh3cevtModuleSw_LSUM2GT24PTSSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GT24PTSSC3 = _Hh3cevtModuleSw_LSUM2GT24PTSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1355)
)
_Hh3cevtModuleSw_LSUM2GT24TSSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GT24TSSE0 = _Hh3cevtModuleSw_LSUM2GT24TSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1356)
)
_Hh3cevtModuleSw_LSUM2GT24TSSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GT24TSSC3 = _Hh3cevtModuleSw_LSUM2GT24TSSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1357)
)
_Hh3cevtModuleSw_LSUM2GT48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GT48SE0 = _Hh3cevtModuleSw_LSUM2GT48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1358)
)
_Hh3cevtModuleSw_LSUM2GT48SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GT48SC3 = _Hh3cevtModuleSw_LSUM2GT48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1359)
)
_Hh3cevtModuleSw_LSUM2GV48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GV48SE0 = _Hh3cevtModuleSw_LSUM2GV48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1360)
)
_Hh3cevtModuleSw_LSUM2GV48SC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GV48SC3 = _Hh3cevtModuleSw_LSUM2GV48SC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1361)
)
_Hh3cevtModuleSw_LSUM2TGS16SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2TGS16SF0 = _Hh3cevtModuleSw_LSUM2TGS16SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1362)
)
_Hh3cevtModuleSw_LSUM2TGS16SF3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2TGS16SF3 = _Hh3cevtModuleSw_LSUM2TGS16SF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1363)
)
_Hh3cevtModuleSw_LSUM1MPU06B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPU06B0 = _Hh3cevtModuleSw_LSUM1MPU06B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1364)
)
_Hh3cevtModuleSw_LSUM1MPU06B3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPU06B3 = _Hh3cevtModuleSw_LSUM1MPU06B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1365)
)
_Hh3cevtModuleSw_LSUM1MPU10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPU10C0 = _Hh3cevtModuleSw_LSUM1MPU10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1366)
)
_Hh3cevtModuleSw_LSUM1MPU10C3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPU10C3 = _Hh3cevtModuleSw_LSUM1MPU10C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1367)
)
_Hh3cevtModuleSw_LSUM1FAB06C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB06C0 = _Hh3cevtModuleSw_LSUM1FAB06C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1368)
)
_Hh3cevtModuleSw_LSUM1FAB06C3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB06C3 = _Hh3cevtModuleSw_LSUM1FAB06C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1369)
)
_Hh3cevtModuleSw_LSUM1FAB10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10C0 = _Hh3cevtModuleSw_LSUM1FAB10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1370)
)
_Hh3cevtModuleSw_LSUM1FAB10C3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10C3 = _Hh3cevtModuleSw_LSUM1FAB10C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1371)
)
_Hh3cevtModuleSw_LSXM1SUPA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPA1 = _Hh3cevtModuleSw_LSXM1SUPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1372)
)
_Hh3cevtModuleSw_LSXM1SFF16B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF16B1 = _Hh3cevtModuleSw_LSXM1SFF16B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1373)
)
_Hh3cevtModuleSw_LSUM1SPMAEC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1SPMAEC0 = _Hh3cevtModuleSw_LSUM1SPMAEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1374)
)
_Hh3cevtModuleSw_LSXM1SUPB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPB1 = _Hh3cevtModuleSw_LSXM1SUPB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1375)
)
_Hh3cevtModuleSw_LSXM1SFF08B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF08B1 = _Hh3cevtModuleSw_LSXM1SFF08B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1376)
)
_Hh3cevtModuleSw_LSXM1TGS4GPEB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS4GPEB1 = _Hh3cevtModuleSw_LSXM1TGS4GPEB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1377)
)
_Hh3cevtModuleSw_LSXM1TGS16EA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS16EA1 = _Hh3cevtModuleSw_LSXM1TGS16EA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1378)
)
_Hh3cevtModuleSw_LSXM1TGS8EA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS8EA1 = _Hh3cevtModuleSw_LSXM1TGS8EA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1379)
)
_Hh3cevtModuleSw_LSXM1QGS36FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS36FX1 = _Hh3cevtModuleSw_LSXM1QGS36FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1380)
)
_Hh3cevtModuleSw_LSXM1SFF16C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF16C1 = _Hh3cevtModuleSw_LSXM1SFF16C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1381)
)
_Hh3cevtModuleSw_LSQM3MPUB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM3MPUB0 = _Hh3cevtModuleSw_LSQM3MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1382)
)
_Hh3cevtModuleSw_LSQM3MPUB3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM3MPUB3 = _Hh3cevtModuleSw_LSQM3MPUB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1383)
)
_Hh3cevtModuleSw_LSQM2MPUC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2MPUC0 = _Hh3cevtModuleSw_LSQM2MPUC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1384)
)
_Hh3cevtModuleSw_LSQM2MPUC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2MPUC3 = _Hh3cevtModuleSw_LSQM2MPUC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1385)
)
_Hh3cevtModuleSw_LST1FW3B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LST1FW3B1 = _Hh3cevtModuleSw_LST1FW3B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1386)
)
_Hh3cevtModuleSw_LSX1NSCEA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1NSCEA1 = _Hh3cevtModuleSw_LSX1NSCEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1387)
)
_Hh3cevtModuleSw_LSX1FWCEA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1FWCEA1 = _Hh3cevtModuleSw_LSX1FWCEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1388)
)
_Hh3cevtModuleSw_LSXM1ADECEA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1ADECEA1 = _Hh3cevtModuleSw_LSXM1ADECEA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1389)
)
_Hh3cevtModuleSw_LSXM1SFF16A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF16A1 = _Hh3cevtModuleSw_LSXM1SFF16A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1390)
)
_Hh3cevtModuleSw_LSV1MPUA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSV1MPUA0 = _Hh3cevtModuleSw_LSV1MPUA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1391)
)
_Hh3cevtModuleSw_LSVM1SRPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1SRPA0 = _Hh3cevtModuleSw_LSVM1SRPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1392)
)
_Hh3cevtModuleSw_LSVM1SRPC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1SRPC0 = _Hh3cevtModuleSw_LSVM1SRPC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1393)
)
_Hh3cevtModuleSw_LSV1QGS12SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSV1QGS12SA0 = _Hh3cevtModuleSw_LSV1QGS12SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1394)
)
_Hh3cevtModuleSw_LSVM1QGS12FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1QGS12FX0 = _Hh3cevtModuleSw_LSVM1QGS12FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1395)
)
_Hh3cevtModuleSw_LSVM1TGS24FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1TGS24FX0 = _Hh3cevtModuleSw_LSVM1TGS24FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1396)
)
_Hh3cevtModuleSw_LSVM1QGS6C2FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1QGS6C2FX0 = _Hh3cevtModuleSw_LSVM1QGS6C2FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1397)
)
_Hh3cevtModuleSw_LSQ2FWBSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQ2FWBSC0 = _Hh3cevtModuleSw_LSQ2FWBSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1398)
)
_Hh3cevtModuleSw_LSQM1SRP8X2QE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1SRP8X2QE0 = _Hh3cevtModuleSw_LSQM1SRP8X2QE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1399)
)
_Hh3cevtModulesw_PEX_Common_ObjectIdentity = ObjectIdentity
hh3cevtModulesw_PEX_Common = _Hh3cevtModulesw_PEX_Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1400)
)
_Hh3cevtModuleSw_CSPEX_1812X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1812X = _Hh3cevtModuleSw_CSPEX_1812X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1401)
)
_Hh3cevtModuleSw_CSPEX_1612X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1612X = _Hh3cevtModuleSw_CSPEX_1612X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1402)
)
_Hh3cevtModuleSw_CSPEX_1512X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1512X = _Hh3cevtModuleSw_CSPEX_1512X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1403)
)
_Hh3cevtModuleSw_NIC_XP20L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_XP20L = _Hh3cevtModuleSw_NIC_XP20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1404)
)
_Hh3cevtModuleSw_NIC_XP10L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_XP10L = _Hh3cevtModuleSw_NIC_XP10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1405)
)
_Hh3cevtModuleSw_NIC_CC2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_CC2L = _Hh3cevtModuleSw_NIC_CC2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1406)
)
_Hh3cevtModuleSw_NIC_CC1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_CC1L = _Hh3cevtModuleSw_NIC_CC1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1407)
)
_Hh3cevtModuleSw_NIC_XP5L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_XP5L = _Hh3cevtModuleSw_NIC_XP5L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1408)
)
_Hh3cevtModuleSw_NIC_GP20L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_GP20L = _Hh3cevtModuleSw_NIC_GP20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1409)
)
_Hh3cevtModuleSw_NIC_GT20L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_GT20L = _Hh3cevtModuleSw_NIC_GT20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1410)
)
_Hh3cevtModuleSw_MIC_CQ1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CQ1L = _Hh3cevtModuleSw_MIC_CQ1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1411)
)
_Hh3cevtModuleSw_MIC_XP10CQ1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP10CQ1L = _Hh3cevtModuleSw_MIC_XP10CQ1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1412)
)
_Hh3cevtModuleSw_CSPEX_1502X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1502X = _Hh3cevtModuleSw_CSPEX_1502X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1413)
)
_Hh3cevtModuleSw_EPC_CP4RX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EPC_CP4RX = _Hh3cevtModuleSw_EPC_CP4RX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1414)
)
_Hh3cevtModuleSw_EPC_CQ4LX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EPC_CQ4LX = _Hh3cevtModuleSw_EPC_CQ4LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1415)
)
_Hh3cevtModuleSw_MIC_XP4L1_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP4L1_E = _Hh3cevtModuleSw_MIC_XP4L1_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1416)
)
_Hh3cevtModuleSw_MIC_CQ1L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CQ1L_E = _Hh3cevtModuleSw_MIC_CQ1L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1417)
)
_Hh3cevtModuleSw_MIC_XP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP8L = _Hh3cevtModuleSw_MIC_XP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1418)
)
_Hh3cevtModuleSw_IM_OAPX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_OAPX = _Hh3cevtModuleSw_IM_OAPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1419)
)
_Hh3cevtModuleSw_MIC_GP20L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GP20L1 = _Hh3cevtModuleSw_MIC_GP20L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1420)
)
_Hh3cevtModuleSw_CSPEX_1802X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1802X = _Hh3cevtModuleSw_CSPEX_1802X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1421)
)
_Hh3cevtModuleSw_MIC_CQ2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CQ2L = _Hh3cevtModuleSw_MIC_CQ2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1422)
)
_Hh3cevtModuleSw_IMMSUX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IMMSUX = _Hh3cevtModuleSw_IMMSUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1423)
)
_Hh3cevtModuleSw_CSPEX_1104_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1104_E = _Hh3cevtModuleSw_CSPEX_1104_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1424)
)
_Hh3cevtModuleSw_IMSMUX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IMSMUX = _Hh3cevtModuleSw_IMSMUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1425)
)
_Hh3cevtModuleSw_MIC_XP10L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP10L = _Hh3cevtModuleSw_MIC_XP10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1426)
)
_Hh3cevtModuleSw_RX_SRP1P3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SRP1P3 = _Hh3cevtModuleSw_RX_SRP1P3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1427)
)
_Hh3cevtModuleSw_RX_SFC_08T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SFC_08T = _Hh3cevtModuleSw_RX_SFC_08T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1428)
)
_Hh3cevtModuleSw_RX_SFC_16T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SFC_16T = _Hh3cevtModuleSw_RX_SFC_16T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1429)
)
_Hh3cevtModuleSw_RX_SPE100_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SPE100 = _Hh3cevtModuleSw_RX_SPE100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1430)
)
_Hh3cevtModuleSw_RX_SPE200_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SPE200 = _Hh3cevtModuleSw_RX_SPE200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1431)
)
_Hh3cevtModuleSw_RX_SPE400_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SPE400 = _Hh3cevtModuleSw_RX_SPE400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1432)
)
_Hh3cevtModuleSw_RX_NIC_GP20L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_GP20L = _Hh3cevtModuleSw_RX_NIC_GP20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1433)
)
_Hh3cevtModuleSw_RX_NIC_XP5L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_XP5L = _Hh3cevtModuleSw_RX_NIC_XP5L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1434)
)
_Hh3cevtModuleSw_RX_NIC_XP10L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_XP10L = _Hh3cevtModuleSw_RX_NIC_XP10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1435)
)
_Hh3cevtModuleSw_RX_NIC_CC1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_CC1L = _Hh3cevtModuleSw_RX_NIC_CC1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1436)
)
_Hh3cevtModuleSw_RX_NIC_CC2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_CC2L = _Hh3cevtModuleSw_RX_NIC_CC2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1437)
)
_Hh3cevtModuleSw_RX_NIC_XP20L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_XP20L = _Hh3cevtModuleSw_RX_NIC_XP20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1438)
)
_Hh3cevtModuleSw_CSPC_GE24L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_GE24L_E = _Hh3cevtModuleSw_CSPC_GE24L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1439)
)
_Hh3cevtModuleSw_CSPC_GP24GE8XP2L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_GP24GE8XP2L_E = _Hh3cevtModuleSw_CSPC_GP24GE8XP2L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1440)
)
_Hh3cevtModuleSw_CSPC_GE16XP4L_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPC_GE16XP4L_E = _Hh3cevtModuleSw_CSPC_GE16XP4L_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1441)
)
_Hh3cevtModuleSw_CSFC_04E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_04E = _Hh3cevtModuleSw_CSFC_04E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1442)
)
_Hh3cevtModuleSw_SFC_04E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFC_04E = _Hh3cevtModuleSw_SFC_04E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1443)
)
_Hh3cevtModuleSw_IM_MSUX_II_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_MSUX_II = _Hh3cevtModuleSw_IM_MSUX_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1444)
)
_Hh3cevtModuleSw_RX_NIC_YGS4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_YGS4L = _Hh3cevtModuleSw_RX_NIC_YGS4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1445)
)
_Hh3cevtModuleSw_RX_NIC_CQ2LF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_CQ2LF = _Hh3cevtModuleSw_RX_NIC_CQ2LF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1446)
)
_Hh3cevtModuleSw_RX_SRP1Q3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SRP1Q3 = _Hh3cevtModuleSw_RX_SRP1Q3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1447)
)
_Hh3cevtModuleSw_RX_SFC_08E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SFC_08E = _Hh3cevtModuleSw_RX_SFC_08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1448)
)
_Hh3cevtModuleSw_RX_SFC_16E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SFC_16E = _Hh3cevtModuleSw_RX_SFC_16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1449)
)
_Hh3cevtModuleSw_RX_NIC_LGQ2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_LGQ2L = _Hh3cevtModuleSw_RX_NIC_LGQ2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1450)
)
_Hh3cevtModuleSw_RX_NIC_CQ1LF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_CQ1LF = _Hh3cevtModuleSw_RX_NIC_CQ1LF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1452)
)
_Hh3cevtModuleSw_IM_SFMX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_SFMX = _Hh3cevtModuleSw_IM_SFMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1453)
)
_Hh3cevtModuleSw_MIC_SM_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_SM = _Hh3cevtModuleSw_MIC_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1454)
)
_Hh3cevtModuleSw_RX_NIC_CQ1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_CQ1L = _Hh3cevtModuleSw_RX_NIC_CQ1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1455)
)
_Hh3cevtModuleSw_RX_NIC_CQ2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_CQ2L = _Hh3cevtModuleSw_RX_NIC_CQ2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1456)
)
_Hh3cevtModuleSw_NIC_GP24L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_GP24L = _Hh3cevtModuleSw_NIC_GP24L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1457)
)
_Hh3cevtModuleSw_NIC_CQ1L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_CQ1L = _Hh3cevtModuleSw_NIC_CQ1L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1458)
)
_Hh3cevtModuleSw_NIC_CQ2L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_CQ2L = _Hh3cevtModuleSw_NIC_CQ2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1459)
)
_Hh3cevtModuleSw_LSUM2GP44TSSE9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GP44TSSE9 = _Hh3cevtModuleSw_LSUM2GP44TSSE9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1600)
)
_Hh3cevtModuleSw_LSUM2GP24TSSE9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GP24TSSE9 = _Hh3cevtModuleSw_LSUM2GP24TSSE9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1601)
)
_Hh3cevtModuleSw_LSUM2GT24TSSE9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GT24TSSE9 = _Hh3cevtModuleSw_LSUM2GT24TSSE9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1602)
)
_Hh3cevtModuleSw_LSUM2GT48SE9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GT48SE9 = _Hh3cevtModuleSw_LSUM2GT48SE9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1603)
)
_Hh3cevtModuleSw_LSUM1SUPD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1SUPD0 = _Hh3cevtModuleSw_LSUM1SUPD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1604)
)
_Hh3cevtModuleSw_LSUM1SUPD9_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1SUPD9 = _Hh3cevtModuleSw_LSUM1SUPD9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1605)
)
_Hh3cevtModuleSw_LSXM1TGT48FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGT48FX0 = _Hh3cevtModuleSw_LSXM1TGT48FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1606)
)
_Hh3cevtModuleSw_LSXM1TGS48FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48FX0 = _Hh3cevtModuleSw_LSXM1TGS48FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1607)
)
_Hh3cevtModuleSw_LSXM1TGS48FE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48FE0 = _Hh3cevtModuleSw_LSXM1TGS48FE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1608)
)
_Hh3cevtModuleSw_LSXM1QGS36FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS36FX0 = _Hh3cevtModuleSw_LSXM1QGS36FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1609)
)
_Hh3cevtModuleSw_LSXM1QGS24FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24FX0 = _Hh3cevtModuleSw_LSXM1QGS24FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1610)
)
_Hh3cevtModuleSw_LSXM1QGS24FE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24FE0 = _Hh3cevtModuleSw_LSXM1QGS24FE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1611)
)
_Hh3cevtModuleSw_LSXM1CGX8FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGX8FX0 = _Hh3cevtModuleSw_LSXM1CGX8FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1612)
)
_Hh3cevtModuleSw_LSXM1CGP12FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGP12FX0 = _Hh3cevtModuleSw_LSXM1CGP12FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1613)
)
_Hh3cevtModuleSw_LSXM1SUPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPB0 = _Hh3cevtModuleSw_LSXM1SUPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1614)
)
_Hh3cevtModuleSw_LSXM1SFF16C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF16C0 = _Hh3cevtModuleSw_LSXM1SFF16C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1615)
)
_Hh3cevtModuleSw_LSXM1SFF16A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF16A0 = _Hh3cevtModuleSw_LSXM1SFF16A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1616)
)
_Hh3cevtModuleSw_LSXM1SFF08B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF08B0 = _Hh3cevtModuleSw_LSXM1SFF08B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1617)
)
_Hh3cevtModuleSw_LSQM6GV48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM6GV48SC0 = _Hh3cevtModuleSw_LSQM6GV48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1618)
)
_Hh3cevtModuleSw_LSXM1SUP04B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP04B1 = _Hh3cevtModuleSw_LSXM1SUP04B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1619)
)
_Hh3cevtModuleSw_LSXM1SFF04B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF04B1 = _Hh3cevtModuleSw_LSXM1SFF04B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1620)
)
_Hh3cevtModuleSw_LSXM1SUP04B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP04B0 = _Hh3cevtModuleSw_LSXM1SUP04B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1621)
)
_Hh3cevtModuleSw_LSXM1SFF04B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF04B0 = _Hh3cevtModuleSw_LSXM1SFF04B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1622)
)
_Hh3cevtModuleSw_LSU1ADECEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1ADECEA0 = _Hh3cevtModuleSw_LSU1ADECEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1623)
)
_Hh3cevtModuleSw_LSU1NSCEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU1NSCEA0 = _Hh3cevtModuleSw_LSU1NSCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1624)
)
_Hh3cevtModuleSw_LSU3FWCEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSU3FWCEA0 = _Hh3cevtModuleSw_LSU3FWCEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1625)
)
_Hh3cevtModuleSw_LSXM1MPU06B3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1MPU06B3 = _Hh3cevtModuleSw_LSXM1MPU06B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1626)
)
_Hh3cevtModuleSw_LSXM1MPU10C3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1MPU10C3 = _Hh3cevtModuleSw_LSXM1MPU10C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1627)
)
_Hh3cevtModuleSw_LSXM1SUPD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPD3 = _Hh3cevtModuleSw_LSXM1SUPD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1628)
)
_Hh3cevtModuleSw_LSXM1FAB06C3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FAB06C3 = _Hh3cevtModuleSw_LSXM1FAB06C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1629)
)
_Hh3cevtModuleSw_LSXM1FAB10C3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FAB10C3 = _Hh3cevtModuleSw_LSXM1FAB10C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1630)
)
_Hh3cevtModuleSw_LSXM1FAB12D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FAB12D3 = _Hh3cevtModuleSw_LSXM1FAB12D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1631)
)
_Hh3cevtModuleSw_LSXM1FAB04D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FAB04D3 = _Hh3cevtModuleSw_LSXM1FAB04D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1632)
)
_Hh3cevtModuleSw_LSXM1FAB08D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FAB08D3 = _Hh3cevtModuleSw_LSXM1FAB08D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1633)
)
_Hh3cevtModuleSw_LSXM1GP44TSSE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP44TSSE3 = _Hh3cevtModuleSw_LSXM1GP44TSSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1634)
)
_Hh3cevtModuleSw_LSXM1GP24TSSE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP24TSSE3 = _Hh3cevtModuleSw_LSXM1GP24TSSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1635)
)
_Hh3cevtModuleSw_LSXM1GT24PTSSE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GT24PTSSE3 = _Hh3cevtModuleSw_LSXM1GT24PTSSE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1636)
)
_Hh3cevtModuleSw_LSXM1GT48SE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GT48SE3 = _Hh3cevtModuleSw_LSXM1GT48SE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1637)
)
_Hh3cevtModuleSw_LSXM1TGS24EC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS24EC3 = _Hh3cevtModuleSw_LSXM1TGS24EC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1638)
)
_Hh3cevtModuleSw_LSXM1CGC2EC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGC2EC3 = _Hh3cevtModuleSw_LSXM1CGC2EC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1639)
)
_Hh3cevtModuleSw_LSXM1TGT24SF3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGT24SF3 = _Hh3cevtModuleSw_LSXM1TGT24SF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1640)
)
_Hh3cevtModuleSw_LSXM1TGS16SF3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS16SF3 = _Hh3cevtModuleSw_LSXM1TGS16SF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1641)
)
_Hh3cevtModuleSw_LSXM1QGS12SG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS12SG3 = _Hh3cevtModuleSw_LSXM1QGS12SG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1642)
)
_Hh3cevtModuleSw_LSXM1TGS48SG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48SG3 = _Hh3cevtModuleSw_LSXM1TGS48SG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1643)
)
_Hh3cevtModuleSw_LSQM1FAB04B3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1FAB04B3 = _Hh3cevtModuleSw_LSQM1FAB04B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1644)
)
_Hh3cevtModuleSw_LSQM1FAB08B3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1FAB08B3 = _Hh3cevtModuleSw_LSQM1FAB08B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1645)
)
_Hh3cevtModuleSw_LSQM1FAB12B3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1FAB12B3 = _Hh3cevtModuleSw_LSQM1FAB12B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1646)
)
_Hh3cevtModuleSw_LSXM1SFF08A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF08A0 = _Hh3cevtModuleSw_LSXM1SFF08A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1647)
)
_Hh3cevtModuleSw_LSXM1SFF08A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF08A1 = _Hh3cevtModuleSw_LSXM1SFF08A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1648)
)
_Hh3cevtModuleSw_LSXM1FWDF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FWDF1 = _Hh3cevtModuleSw_LSXM1FWDF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1649)
)
_Hh3cevtModuleSw_LSQM1PT8TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1PT8TSSC0 = _Hh3cevtModuleSw_LSQM1PT8TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1650)
)
_Hh3cevtModuleSw_LSQM1PT24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1PT24TSSC0 = _Hh3cevtModuleSw_LSQM1PT24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1651)
)
_Hh3cevtModuleSw_LSQM1TGS12EC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS12EC0 = _Hh3cevtModuleSw_LSQM1TGS12EC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1652)
)
_Hh3cevtModuleSw_LSX1M1CGQ32TB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1M1CGQ32TB1 = _Hh3cevtModuleSw_LSX1M1CGQ32TB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1653)
)
_Hh3cevtModuleSw_LSX1M1CGQ48TB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1M1CGQ48TB1 = _Hh3cevtModuleSw_LSX1M1CGQ48TB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1654)
)
_Hh3cevtModuleSw_LSXM1QGS48TB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS48TB1 = _Hh3cevtModuleSw_LSXM1QGS48TB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1655)
)
_Hh3cevtModuleSw_LSXM1SRT08E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SRT08E1 = _Hh3cevtModuleSw_LSXM1SRT08E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1656)
)
_Hh3cevtModuleSw_LSXM1SRT16E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SRT16E1 = _Hh3cevtModuleSw_LSXM1SRT16E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1657)
)
_Hh3cevtModuleSw_LSXM1SRT02E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SRT02E1 = _Hh3cevtModuleSw_LSXM1SRT02E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1658)
)
_Hh3cevtModuleSw_LSXM1SUP02B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP02B1 = _Hh3cevtModuleSw_LSXM1SUP02B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1659)
)
_Hh3cevtModuleSw_LSUM1SUPC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1SUPC0 = _Hh3cevtModuleSw_LSUM1SUPC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1660)
)
_Hh3cevtModuleSw_LSUM1SUPC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1SUPC3 = _Hh3cevtModuleSw_LSUM1SUPC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1661)
)
_Hh3cevtModuleSw_LSXM1SUPC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPC3 = _Hh3cevtModuleSw_LSXM1SUPC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1662)
)
_Hh3cevtModuleSw_LSQM1GP44TSSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP44TSSE0 = _Hh3cevtModuleSw_LSQM1GP44TSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1663)
)
_Hh3cevtModuleSw_LSQM1GP24TSSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP24TSSE0 = _Hh3cevtModuleSw_LSQM1GP24TSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1664)
)
_Hh3cevtModuleSw_LSQM1GT48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GT48SE0 = _Hh3cevtModuleSw_LSQM1GT48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1665)
)
_Hh3cevtModuleSw_LSQM1GV48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GV48SE0 = _Hh3cevtModuleSw_LSQM1GV48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1666)
)
_Hh3cevtModuleSw_LSXM1QGS12FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS12FX0 = _Hh3cevtModuleSw_LSXM1QGS12FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1667)
)
_Hh3cevtModuleSw_LSXM3QGS24FE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3QGS24FE1 = _Hh3cevtModuleSw_LSXM3QGS24FE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1668)
)
_Hh3cevtModuleSw_LSXM3QGS24FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3QGS24FX1 = _Hh3cevtModuleSw_LSXM3QGS24FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1669)
)
_Hh3cevtModuleSw_LSXM3QGS36FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3QGS36FX1 = _Hh3cevtModuleSw_LSXM3QGS36FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1670)
)
_Hh3cevtModuleSw_LSXM3TGS48FE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3TGS48FE1 = _Hh3cevtModuleSw_LSXM3TGS48FE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1671)
)
_Hh3cevtModuleSw_LSXM3TGS48FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3TGS48FX1 = _Hh3cevtModuleSw_LSXM3TGS48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1672)
)
_Hh3cevtModuleSw_LSXM2TGS48FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2TGS48FX1 = _Hh3cevtModuleSw_LSXM2TGS48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1673)
)
_Hh3cevtModuleSw_LSQM1MPU06B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPU06B0 = _Hh3cevtModuleSw_LSQM1MPU06B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1674)
)
_Hh3cevtModuleSw_LSQM1MPU10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPU10C0 = _Hh3cevtModuleSw_LSQM1MPU10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1675)
)
_Hh3cevtModuleSw_LSQM1FAB06C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1FAB06C0 = _Hh3cevtModuleSw_LSQM1FAB06C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1676)
)
_Hh3cevtModuleSw_LSQM1FAB10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1FAB10C0 = _Hh3cevtModuleSw_LSQM1FAB10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1677)
)
_Hh3cevtModuleSw_LSQM1QGS12SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1QGS12SG0 = _Hh3cevtModuleSw_LSQM1QGS12SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1678)
)
_Hh3cevtModuleSw_LSQM1TGS48SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS48SG0 = _Hh3cevtModuleSw_LSQM1TGS48SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1679)
)
_Hh3cevtModuleSw_LSQM1TGT24SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGT24SF0 = _Hh3cevtModuleSw_LSQM1TGT24SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1680)
)
_Hh3cevtModuleSw_LSQM1QGS8A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1QGS8A0 = _Hh3cevtModuleSw_LSQM1QGS8A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1681)
)
_Hh3cevtModuleSw_LSQM1TGS24QSM0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS24QSM0 = _Hh3cevtModuleSw_LSQM1TGS24QSM0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1682)
)
_Hh3cevtModuleSw_LSQM1TGT24QSM0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGT24QSM0 = _Hh3cevtModuleSw_LSQM1TGT24QSM0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1683)
)
_Hh3cevtModuleSw_LSQM1TGS24QSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS24QSA0 = _Hh3cevtModuleSw_LSQM1TGS24QSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1684)
)
_Hh3cevtModuleSw_LSUM1FWCEAB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FWCEAB0 = _Hh3cevtModuleSw_LSUM1FWCEAB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1685)
)
_Hh3cevtModuleSw_LSQM2GP24TSSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP24TSSA0 = _Hh3cevtModuleSw_LSQM2GP24TSSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1686)
)
_Hh3cevtModuleSw_LSQM2GT48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT48SA0 = _Hh3cevtModuleSw_LSQM2GT48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1687)
)
_Hh3cevtModuleSw_LSQM2GP48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP48SA0 = _Hh3cevtModuleSw_LSQM2GP48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1688)
)
_Hh3cevtModuleSw_LSQM2GP24TSSA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP24TSSA3 = _Hh3cevtModuleSw_LSQM2GP24TSSA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1689)
)
_Hh3cevtModuleSw_LSQM2GT48SA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT48SA3 = _Hh3cevtModuleSw_LSQM2GT48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1690)
)
_Hh3cevtModuleSw_LSQM2GP48SA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP48SA3 = _Hh3cevtModuleSw_LSQM2GP48SA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1691)
)
_Hh3cevtModuleSw_LSUM2GP24TSSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GP24TSSA0 = _Hh3cevtModuleSw_LSUM2GP24TSSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1692)
)
_Hh3cevtModuleSw_LSUM2GT48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GT48SA0 = _Hh3cevtModuleSw_LSUM2GT48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1693)
)
_Hh3cevtModuleSw_LSUM2GP48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GP48SA0 = _Hh3cevtModuleSw_LSUM2GP48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1694)
)
_Hh3cevtModuleSw_LSXM1SUPT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPT1 = _Hh3cevtModuleSw_LSXM1SUPT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1695)
)
_Hh3cevtModuleSw_LSXM1SUP02T1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP02T1 = _Hh3cevtModuleSw_LSXM1SUP02T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1696)
)
_Hh3cevtModuleSw_LSXM1SFF16B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFF16B0 = _Hh3cevtModuleSw_LSXM1SFF16B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1697)
)
_Hh3cevtModuleSw_LSXM4TGS48FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM4TGS48FX1 = _Hh3cevtModuleSw_LSXM4TGS48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1698)
)
_Hh3cevtModuleSw_LSXM4QGS24FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM4QGS24FX1 = _Hh3cevtModuleSw_LSXM4QGS24FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1699)
)
_Hh3cevtModuleSw_LSXM1TGS48FD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48FD1 = _Hh3cevtModuleSw_LSXM1TGS48FD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1700)
)
_Hh3cevtModuleSw_LSXM1QGS24FD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24FD1 = _Hh3cevtModuleSw_LSXM1QGS24FD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1701)
)
_Hh3cevtModuleSw_LSXM2QGS24FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2QGS24FX1 = _Hh3cevtModuleSw_LSXM2QGS24FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1702)
)
_Hh3cevtModuleSw_LSXM1TGS48FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48FD0 = _Hh3cevtModuleSw_LSXM1TGS48FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1703)
)
_Hh3cevtModuleSw_LSXM1QGS24FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24FD0 = _Hh3cevtModuleSw_LSXM1QGS24FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1704)
)
_Hh3cevtModuleSw_LSXM2TGS48FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2TGS48FX0 = _Hh3cevtModuleSw_LSXM2TGS48FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1705)
)
_Hh3cevtModuleSw_LSXM2QGS24FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2QGS24FX0 = _Hh3cevtModuleSw_LSXM2QGS24FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1706)
)
_Hh3cevtModuleSw_LSXM4TGS48FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM4TGS48FX0 = _Hh3cevtModuleSw_LSXM4TGS48FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1707)
)
_Hh3cevtModuleSw_LSXM4QGS24FX0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM4QGS24FX0 = _Hh3cevtModuleSw_LSXM4QGS24FX0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1708)
)
_Hh3cevtModuleSw_LSXM1TGW48FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGW48FX1 = _Hh3cevtModuleSw_LSXM1TGW48FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1709)
)
_Hh3cevtModuleSw_LSUM1MPU10A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPU10A0 = _Hh3cevtModuleSw_LSUM1MPU10A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1710)
)
_Hh3cevtModuleSw_LSUM1FAB10A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10A0 = _Hh3cevtModuleSw_LSUM1FAB10A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1711)
)
_Hh3cevtModuleSw_LSUM2TGS32QSSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2TGS32QSSG0 = _Hh3cevtModuleSw_LSUM2TGS32QSSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1712)
)
_Hh3cevtModuleSw_LSUM2QGS12SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2QGS12SG0 = _Hh3cevtModuleSw_LSUM2QGS12SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1713)
)
_Hh3cevtModuleSw_LSUM2TGS48SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2TGS48SG0 = _Hh3cevtModuleSw_LSUM2TGS48SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1714)
)
_Hh3cevtModuleSw_LSXM2QGS12SG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2QGS12SG3 = _Hh3cevtModuleSw_LSXM2QGS12SG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1715)
)
_Hh3cevtModuleSw_LSXM2TGS48SG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2TGS48SG3 = _Hh3cevtModuleSw_LSXM2TGS48SG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1716)
)
_Hh3cevtModuleSw_LSUM1FWDEC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FWDEC0 = _Hh3cevtModuleSw_LSUM1FWDEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1717)
)
_Hh3cevtModuleSw_LSQM1FWDSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1FWDSC0 = _Hh3cevtModuleSw_LSQM1FWDSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1718)
)
_Hh3cevtModuleSw_LSQM1TGS48RSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS48RSG0 = _Hh3cevtModuleSw_LSQM1TGS48RSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1719)
)
_Hh3cevtModuleSw_LSQM2TGS48XSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2TGS48XSG0 = _Hh3cevtModuleSw_LSQM2TGS48XSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1720)
)
_Hh3cevtModuleSw_LSQM2QGS12XSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2QGS12XSG0 = _Hh3cevtModuleSw_LSQM2QGS12XSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1721)
)
_Hh3cevtModuleSw_LSQM3GP44TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM3GP44TSSC0 = _Hh3cevtModuleSw_LSQM3GP44TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1722)
)
_Hh3cevtModuleSw_LSXM1CGQ36HB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36HB1 = _Hh3cevtModuleSw_LSXM1CGQ36HB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1723)
)
_Hh3cevtModuleSw_LSXM1CGQ36HC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36HC1 = _Hh3cevtModuleSw_LSXM1CGQ36HC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1724)
)
_Hh3cevtModuleSw_LSXM1CGQ18QGHB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18QGHB1 = _Hh3cevtModuleSw_LSXM1CGQ18QGHB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1725)
)
_Hh3cevtModuleSw_LSXM1CGQ18QGHC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18QGHC1 = _Hh3cevtModuleSw_LSXM1CGQ18QGHC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1726)
)
_Hh3cevtModuleSw_LSXM1QGS48HB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS48HB1 = _Hh3cevtModuleSw_LSXM1QGS48HB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1727)
)
_Hh3cevtModuleSw_LSXM1QGS48HC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS48HC1 = _Hh3cevtModuleSw_LSXM1QGS48HC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1728)
)
_Hh3cevtModuleSw_LSXM1TGS48C2HB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48C2HB1 = _Hh3cevtModuleSw_LSXM1TGS48C2HB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1729)
)
_Hh3cevtModuleSw_LSXM1SFH04D1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH04D1 = _Hh3cevtModuleSw_LSXM1SFH04D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1730)
)
_Hh3cevtModuleSw_LSXM1SFH08D1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH08D1 = _Hh3cevtModuleSw_LSXM1SFH08D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1731)
)
_Hh3cevtModuleSw_LSXM1SFH12D1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH12D1 = _Hh3cevtModuleSw_LSXM1SFH12D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1732)
)
_Hh3cevtModuleSw_LSXM1SFH16C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH16C1 = _Hh3cevtModuleSw_LSXM1SFH16C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1733)
)
_Hh3cevtModuleSw_LSXM1GP48FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP48FD0 = _Hh3cevtModuleSw_LSXM1GP48FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1737)
)
_Hh3cevtModuleSw_LSXM1GP48FD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP48FD1 = _Hh3cevtModuleSw_LSXM1GP48FD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1738)
)
_Hh3cevtModuleSw_LSXM1GT48FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GT48FD0 = _Hh3cevtModuleSw_LSXM1GT48FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1739)
)
_Hh3cevtModuleSw_LSXM1GT48FD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GT48FD1 = _Hh3cevtModuleSw_LSXM1GT48FD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1740)
)
_Hh3cevtModuleSw_LSXM1FAB10B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FAB10B0 = _Hh3cevtModuleSw_LSXM1FAB10B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1741)
)
_Hh3cevtModuleSw_LSUM1MPU10A3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPU10A3 = _Hh3cevtModuleSw_LSUM1MPU10A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1742)
)
_Hh3cevtModuleSw_LSUM1FAB10A3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10A3 = _Hh3cevtModuleSw_LSUM1FAB10A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1743)
)
_Hh3cevtModuleSw_LSQM1MPU10A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPU10A0 = _Hh3cevtModuleSw_LSQM1MPU10A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1744)
)
_Hh3cevtModuleSw_LSQM1FAB10A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1FAB10A0 = _Hh3cevtModuleSw_LSQM1FAB10A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1745)
)
_Hh3cevtModuleSw_LSQM2TGS32QSXSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2TGS32QSXSG0 = _Hh3cevtModuleSw_LSQM2TGS32QSXSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1746)
)
_Hh3cevtModuleSw_LSQM1TGS48RSG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS48RSG3 = _Hh3cevtModuleSw_LSQM1TGS48RSG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1747)
)
_Hh3cevtModuleSw_LSXM2TGS32QSSG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2TGS32QSSG3 = _Hh3cevtModuleSw_LSXM2TGS32QSSG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1748)
)
_Hh3cevtModuleSw_LSUM1NSDEC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1NSDEC0 = _Hh3cevtModuleSw_LSUM1NSDEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1749)
)
_Hh3cevtModuleSw_LSQM1NSDSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1NSDSC0 = _Hh3cevtModuleSw_LSQM1NSDSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1750)
)
_Hh3cevtModuleSw_LSQM1QGS4SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1QGS4SC0 = _Hh3cevtModuleSw_LSQM1QGS4SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1751)
)
_Hh3cevtModuleSw_LLSQM2MPUD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LLSQM2MPUD3 = _Hh3cevtModuleSw_LLSQM2MPUD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1752)
)
_Hh3cevtModuleSw_LLSQM3MPUB3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LLSQM3MPUB3 = _Hh3cevtModuleSw_LLSQM3MPUB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1753)
)
_Hh3cevtModuleSw_LSQM3MPUB4_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM3MPUB4 = _Hh3cevtModuleSw_LSQM3MPUB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1754)
)
_Hh3cevtModuleSw_LSQM2MPUDS0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2MPUDS0 = _Hh3cevtModuleSw_LSQM2MPUDS0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1755)
)
_Hh3cevtModuleSw_LSQM4GV48SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM4GV48SA0 = _Hh3cevtModuleSw_LSQM4GV48SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1756)
)
_Hh3cevtModuleSw_LSQM1WCMX20_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1WCMX20 = _Hh3cevtModuleSw_LSQM1WCMX20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1757)
)
_Hh3cevtModuleSw_LSQM1WCMX40_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1WCMX40 = _Hh3cevtModuleSw_LSQM1WCMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1758)
)
_Hh3cevtModuleSw_LSUM1WCMX20RT_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1WCMX20RT = _Hh3cevtModuleSw_LSUM1WCMX20RT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1759)
)
_Hh3cevtModuleSw_LSUM1WCMX40RT_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1WCMX40RT = _Hh3cevtModuleSw_LSUM1WCMX40RT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1760)
)
_Hh3cevtModuleSw_LSXM1CGQ18QGHB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18QGHB0 = _Hh3cevtModuleSw_LSXM1CGQ18QGHB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1761)
)
_Hh3cevtModuleSw_LSXM1SFH08C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH08C0 = _Hh3cevtModuleSw_LSXM1SFH08C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1762)
)
_Hh3cevtModuleSw_LSXM1SFH08C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH08C1 = _Hh3cevtModuleSw_LSXM1SFH08C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1763)
)
_Hh3cevtModuleSw_LSXM2SFH16C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2SFH16C0 = _Hh3cevtModuleSw_LSXM2SFH16C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1764)
)
_Hh3cevtModuleSw_LSXM2SFH16C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2SFH16C1 = _Hh3cevtModuleSw_LSXM2SFH16C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1765)
)
_Hh3cevtModuleSw_LSXM1NSDF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1NSDF1 = _Hh3cevtModuleSw_LSXM1NSDF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1766)
)
_Hh3cevtModuleSw_LSUM2TGS48SG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2TGS48SG3 = _Hh3cevtModuleSw_LSUM2TGS48SG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1767)
)
_Hh3cevtModuleSw_DS_3E7602_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7602_MPU = _Hh3cevtModuleSw_DS_3E7602_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1768)
)
_Hh3cevtModuleSw_DS_3E7606_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7606_MPU = _Hh3cevtModuleSw_DS_3E7606_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1769)
)
_Hh3cevtModuleSw_DS_3E7600_24T4X_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_24T4X_SC = _Hh3cevtModuleSw_DS_3E7600_24T4X_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1770)
)
_Hh3cevtModuleSw_DS_3E7600_24F4X_SA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_24F4X_SA = _Hh3cevtModuleSw_DS_3E7600_24F4X_SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1771)
)
_Hh3cevtModuleSw_DS_3E7600_48T_SA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_48T_SA = _Hh3cevtModuleSw_DS_3E7600_48T_SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1772)
)
_Hh3cevtModuleSw_DS_3E7600_48F_SA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_48F_SA = _Hh3cevtModuleSw_DS_3E7600_48F_SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1773)
)
_Hh3cevtModuleSw_DS_3E7600_24F4X_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_24F4X_SC = _Hh3cevtModuleSw_DS_3E7600_24F4X_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1774)
)
_Hh3cevtModuleSw_DS_3E7600_44F4X_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_44F4X_SC = _Hh3cevtModuleSw_DS_3E7600_44F4X_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1775)
)
_Hh3cevtModuleSw_DS_3E7600_48T_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_48T_SC = _Hh3cevtModuleSw_DS_3E7600_48T_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1776)
)
_Hh3cevtModuleSw_DS_3E7600_16X_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_16X_SC = _Hh3cevtModuleSw_DS_3E7600_16X_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1777)
)
_Hh3cevtModuleSw_S7602_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S7602_MPU = _Hh3cevtModuleSw_S7602_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1778)
)
_Hh3cevtModuleSw_S7606_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S7606_MPU = _Hh3cevtModuleSw_S7606_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1779)
)
_Hh3cevtModuleSw_S76_24GT4XFSC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S76_24GT4XFSC = _Hh3cevtModuleSw_S76_24GT4XFSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1780)
)
_Hh3cevtModuleSw_S76_24GF4XFSA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S76_24GF4XFSA = _Hh3cevtModuleSw_S76_24GF4XFSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1781)
)
_Hh3cevtModuleSw_S76_48GTSA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S76_48GTSA = _Hh3cevtModuleSw_S76_48GTSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1782)
)
_Hh3cevtModuleSw_S76_48GFSA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S76_48GFSA = _Hh3cevtModuleSw_S76_48GFSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1783)
)
_Hh3cevtModuleSw_S76_24GT20GF4XFSC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S76_24GT20GF4XFSC = _Hh3cevtModuleSw_S76_24GT20GF4XFSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1784)
)
_Hh3cevtModuleSw_LSXM1TGS48C2HB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48C2HB0 = _Hh3cevtModuleSw_LSXM1TGS48C2HB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1785)
)
_Hh3cevtModuleSw_LSXM1CGQ18QGHC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18QGHC0 = _Hh3cevtModuleSw_LSXM1CGQ18QGHC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1786)
)
_Hh3cevtModuleSw_LSXM1TGS48HB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48HB1 = _Hh3cevtModuleSw_LSXM1TGS48HB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1787)
)
_Hh3cevtModuleSw_LSXM1TGS48HB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48HB0 = _Hh3cevtModuleSw_LSXM1TGS48HB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1788)
)
_Hh3cevtModuleSw_LSQM1CGP24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGP24TSSC0 = _Hh3cevtModuleSw_LSQM1CGP24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1789)
)
_Hh3cevtModuleSw_LSQM1CGP24TSSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGP24TSSA0 = _Hh3cevtModuleSw_LSQM1CGP24TSSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1790)
)
_Hh3cevtModuleSw_LSQM1CGT24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGT24TSSC0 = _Hh3cevtModuleSw_LSQM1CGT24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1791)
)
_Hh3cevtModuleSw_LSQM1CGT24TSSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGT24TSSA0 = _Hh3cevtModuleSw_LSQM1CGT24TSSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1792)
)
_Hh3cevtModuleSw_LSQM2GP24SA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP24SA0 = _Hh3cevtModuleSw_LSQM2GP24SA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1793)
)
_Hh3cevtModuleSw_LSX1SUPH1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUPH1 = _Hh3cevtModuleSw_LSX1SUPH1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1794)
)
_Hh3cevtModuleSw_LSX1SUPH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUPH0 = _Hh3cevtModuleSw_LSX1SUPH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1795)
)
_Hh3cevtModuleSw_LSX1SUP04H1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP04H1 = _Hh3cevtModuleSw_LSX1SUP04H1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1796)
)
_Hh3cevtModuleSw_LSX1SUP04H0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSX1SUP04H0 = _Hh3cevtModuleSw_LSX1SUP04H0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1797)
)
_Hh3cevtModuleSw_LSXM1SFH08D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH08D0 = _Hh3cevtModuleSw_LSXM1SFH08D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1798)
)
_Hh3cevtModuleSw_LSXM1SFH04D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH04D0 = _Hh3cevtModuleSw_LSXM1SFH04D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1799)
)
_Hh3cevtModuleSw_LSXM1SFH16C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH16C0 = _Hh3cevtModuleSw_LSXM1SFH16C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1800)
)
_Hh3cevtModuleSw_LSXM1SFH12D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH12D0 = _Hh3cevtModuleSw_LSXM1SFH12D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1801)
)
_Hh3cevtModuleSw_LSXM1QGS48HB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS48HB0 = _Hh3cevtModuleSw_LSXM1QGS48HB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1802)
)
_Hh3cevtModuleSw_LSXM1QGS48HC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS48HC0 = _Hh3cevtModuleSw_LSXM1QGS48HC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1803)
)
_Hh3cevtModuleSw_LSXM1CGQ36HB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36HB0 = _Hh3cevtModuleSw_LSXM1CGQ36HB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1804)
)
_Hh3cevtModuleSw_LSXM1TGS48C2HC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48C2HC0 = _Hh3cevtModuleSw_LSXM1TGS48C2HC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1805)
)
_Hh3cevtModuleSw_LSQM2GP44TSSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP44TSSE0 = _Hh3cevtModuleSw_LSQM2GP44TSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1806)
)
_Hh3cevtModuleSw_LSQM2GP24TSSA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP24TSSA8 = _Hh3cevtModuleSw_LSQM2GP24TSSA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1807)
)
_Hh3cevtModuleSw_LSQM2GT48SA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT48SA8 = _Hh3cevtModuleSw_LSQM2GT48SA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1808)
)
_Hh3cevtModuleSw_LSQM2GP48SA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP48SA8 = _Hh3cevtModuleSw_LSQM2GP48SA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1809)
)
_Hh3cevtModuleSw_EWPXM1CGP24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM1CGP24TSSC0 = _Hh3cevtModuleSw_EWPXM1CGP24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1810)
)
_Hh3cevtModuleSw_EWPXM3MPUB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM3MPUB0 = _Hh3cevtModuleSw_EWPXM3MPUB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1811)
)
_Hh3cevtModuleSw_EWPXM2MPUDS0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2MPUDS0 = _Hh3cevtModuleSw_EWPXM2MPUDS0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1812)
)
_Hh3cevtModuleSw_EWPXM2TGS16SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2TGS16SF0 = _Hh3cevtModuleSw_EWPXM2TGS16SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1813)
)
_Hh3cevtModuleSw_EWPXM2GP44TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP44TSSC0 = _Hh3cevtModuleSw_EWPXM2GP44TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1814)
)
_Hh3cevtModuleSw_EWPXM2GP24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2GP24TSSC0 = _Hh3cevtModuleSw_EWPXM2GP24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1815)
)
_Hh3cevtModuleSw_EWPXM1MAC0F_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM1MAC0F = _Hh3cevtModuleSw_EWPXM1MAC0F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1816)
)
_Hh3cevtModuleSw_LSQM1CGP24TSSA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGP24TSSA8 = _Hh3cevtModuleSw_LSQM1CGP24TSSA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1817)
)
_Hh3cevtModuleSw_LSQM1CGT24TSSA8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGT24TSSA8 = _Hh3cevtModuleSw_LSQM1CGT24TSSA8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1818)
)
_Hh3cevtModuleSw_LSWM1FWD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1FWD0 = _Hh3cevtModuleSw_LSWM1FWD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1819)
)
_Hh3cevtModuleSw_LSUM2MPU10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2MPU10C0 = _Hh3cevtModuleSw_LSUM2MPU10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1820)
)
_Hh3cevtModuleSw_LSQM2MPU10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2MPU10C0 = _Hh3cevtModuleSw_LSQM2MPU10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1821)
)
_Hh3cevtModuleSw_LSUM2MPU10C3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2MPU10C3 = _Hh3cevtModuleSw_LSUM2MPU10C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1822)
)
_Hh3cevtModuleSw_LSUM2FAB10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB10C0 = _Hh3cevtModuleSw_LSUM2FAB10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1823)
)
_Hh3cevtModuleSw_LSQM2FAB10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2FAB10C0 = _Hh3cevtModuleSw_LSQM2FAB10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1824)
)
_Hh3cevtModuleSw_LSUM2FAB10C3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB10C3 = _Hh3cevtModuleSw_LSUM2FAB10C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1825)
)
_Hh3cevtModuleSw_LSUM2CQGS12SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2CQGS12SG0 = _Hh3cevtModuleSw_LSUM2CQGS12SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1826)
)
_Hh3cevtModuleSw_LSXM2CQGS12SG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2CQGS12SG3 = _Hh3cevtModuleSw_LSXM2CQGS12SG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1827)
)
_Hh3cevtModuleSw_LSQM2CQGS12XSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2CQGS12XSG0 = _Hh3cevtModuleSw_LSQM2CQGS12XSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1828)
)
_Hh3cevtModuleSw_LSQM1CQGS12SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CQGS12SG0 = _Hh3cevtModuleSw_LSQM1CQGS12SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1829)
)
_Hh3cevtModuleSw_LSXM1CGQ6QGHB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ6QGHB0 = _Hh3cevtModuleSw_LSXM1CGQ6QGHB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1830)
)
_Hh3cevtModuleSw_LSXM1CGQ6QGHB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ6QGHB1 = _Hh3cevtModuleSw_LSXM1CGQ6QGHB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1831)
)
_Hh3cevtModuleSw_LSXM1CGQ6QGHC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ6QGHC0 = _Hh3cevtModuleSw_LSXM1CGQ6QGHC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1832)
)
_Hh3cevtModuleSw_LSXM1QGS36HB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS36HB0 = _Hh3cevtModuleSw_LSXM1QGS36HB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1833)
)
_Hh3cevtModuleSw_LSXM1QGS36HB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS36HB1 = _Hh3cevtModuleSw_LSXM1QGS36HB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1834)
)
_Hh3cevtModuleSw_LSXM1QGS36HC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS36HC0 = _Hh3cevtModuleSw_LSXM1QGS36HC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1835)
)
_Hh3cevtModuleSw_LSXM1SUPC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPC0 = _Hh3cevtModuleSw_LSXM1SUPC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1836)
)
_Hh3cevtModuleSw_LSXM1SUPC1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPC1 = _Hh3cevtModuleSw_LSXM1SUPC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1837)
)
_Hh3cevtModuleSw_LSXM1SUP04H0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP04H0 = _Hh3cevtModuleSw_LSXM1SUP04H0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1838)
)
_Hh3cevtModuleSw_LSXM1SUP04H1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP04H1 = _Hh3cevtModuleSw_LSXM1SUP04H1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1839)
)
_Hh3cevtModuleSw_LSXM1SUPH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPH0 = _Hh3cevtModuleSw_LSXM1SUPH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1840)
)
_Hh3cevtModuleSw_LSXM1SUPH1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPH1 = _Hh3cevtModuleSw_LSXM1SUPH1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1841)
)
_Hh3cevtModuleSw_EWPXM2WCMD0F_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2WCMD0F = _Hh3cevtModuleSw_EWPXM2WCMD0F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1842)
)
_Hh3cevtModuleSw_LSUM2QGS24RSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2QGS24RSG0 = _Hh3cevtModuleSw_LSUM2QGS24RSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1843)
)
_Hh3cevtModuleSw_LSQM1QGS24RSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1QGS24RSG0 = _Hh3cevtModuleSw_LSQM1QGS24RSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1844)
)
_Hh3cevtModuleSw_LSXM2QGS24RSG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2QGS24RSG3 = _Hh3cevtModuleSw_LSXM2QGS24RSG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1845)
)
_Hh3cevtModuleSw_LSQM2QGS24RXSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2QGS24RXSG0 = _Hh3cevtModuleSw_LSQM2QGS24RXSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1846)
)
_Hh3cevtModuleSw_LSQM2TGS48RSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2TGS48RSG0 = _Hh3cevtModuleSw_LSQM2TGS48RSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1847)
)
_Hh3cevtModuleSw_LSXM1X86SUPE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1X86SUPE0 = _Hh3cevtModuleSw_LSXM1X86SUPE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1848)
)
_Hh3cevtModuleSw_LSXM1X86SUPE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1X86SUPE1 = _Hh3cevtModuleSw_LSXM1X86SUPE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1849)
)
_Hh3cevtModuleSw_LSQM1CGS2QSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGS2QSA0 = _Hh3cevtModuleSw_LSQM1CGS2QSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1850)
)
_Hh3cevtModuleSw_LSUM1ACGDEC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1ACGDEC0 = _Hh3cevtModuleSw_LSUM1ACGDEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1851)
)
_Hh3cevtModuleSw_LSQM1ACGDSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1ACGDSC0 = _Hh3cevtModuleSw_LSQM1ACGDSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1852)
)
_Hh3cevtModuleSw_LSXM1CGQ36HF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36HF1 = _Hh3cevtModuleSw_LSXM1CGQ36HF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1853)
)
_Hh3cevtModuleSw_LSXM1QGS48HF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS48HF1 = _Hh3cevtModuleSw_LSXM1QGS48HF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1854)
)
_Hh3cevtModuleSw_LSXM1CGQ18QGHF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18QGHF1 = _Hh3cevtModuleSw_LSXM1CGQ18QGHF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1855)
)
_Hh3cevtModuleSw_LSXM1QGS36HF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS36HF1 = _Hh3cevtModuleSw_LSXM1QGS36HF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1856)
)
_Hh3cevtModuleSw_LSXM1CGQ6QGHF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ6QGHF1 = _Hh3cevtModuleSw_LSXM1CGQ6QGHF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1857)
)
_Hh3cevtModuleSw_LSXM1QGS48HF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS48HF0 = _Hh3cevtModuleSw_LSXM1QGS48HF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1858)
)
_Hh3cevtModuleSw_LSXM1CGQ18QGHF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18QGHF0 = _Hh3cevtModuleSw_LSXM1CGQ18QGHF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1859)
)
_Hh3cevtModuleSw_LSXM1CGQ6QGHF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ6QGHF0 = _Hh3cevtModuleSw_LSXM1CGQ6QGHF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1860)
)
_Hh3cevtModuleSw_LSXM1TGS48HF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48HF0 = _Hh3cevtModuleSw_LSXM1TGS48HF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1861)
)
_Hh3cevtModuleSw_LSXM1TGS48HF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48HF1 = _Hh3cevtModuleSw_LSXM1TGS48HF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1862)
)
_Hh3cevtModuleSw_LSQM1GP24FC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP24FC3 = _Hh3cevtModuleSw_LSQM1GP24FC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1863)
)
_Hh3cevtModuleSw_LSQM1GP24FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP24FD3 = _Hh3cevtModuleSw_LSQM1GP24FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1864)
)
_Hh3cevtModuleSw_LSQM1GP24TSFC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP24TSFC3 = _Hh3cevtModuleSw_LSQM1GP24TSFC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1865)
)
_Hh3cevtModuleSw_LSQM1GP24TSFD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP24TSFD3 = _Hh3cevtModuleSw_LSQM1GP24TSFD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1866)
)
_Hh3cevtModuleSw_LSQM1GP40TS8FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP40TS8FD0 = _Hh3cevtModuleSw_LSQM1GP40TS8FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1867)
)
_Hh3cevtModuleSw_LSQM1GP48FC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP48FC3 = _Hh3cevtModuleSw_LSQM1GP48FC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1868)
)
_Hh3cevtModuleSw_LSQM1GP48FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP48FD0 = _Hh3cevtModuleSw_LSQM1GP48FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1869)
)
_Hh3cevtModuleSw_LSQM1GP48FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP48FD3 = _Hh3cevtModuleSw_LSQM1GP48FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1870)
)
_Hh3cevtModuleSw_LSQM1GT48FC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GT48FC3 = _Hh3cevtModuleSw_LSQM1GT48FC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1871)
)
_Hh3cevtModuleSw_LSQM1GT48FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GT48FD0 = _Hh3cevtModuleSw_LSQM1GT48FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1872)
)
_Hh3cevtModuleSw_LSQM1GT48FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GT48FD3 = _Hh3cevtModuleSw_LSQM1GT48FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1873)
)
_Hh3cevtModuleSw_LSQM1TGS24FC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS24FC3 = _Hh3cevtModuleSw_LSQM1TGS24FC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1874)
)
_Hh3cevtModuleSw_LSQM1TGS24FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS24FD0 = _Hh3cevtModuleSw_LSQM1TGS24FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1875)
)
_Hh3cevtModuleSw_LSQM1TGS24FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS24FD3 = _Hh3cevtModuleSw_LSQM1TGS24FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1876)
)
_Hh3cevtModuleSw_LSQM1TGS24XFD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS24XFD0 = _Hh3cevtModuleSw_LSQM1TGS24XFD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1877)
)
_Hh3cevtModuleSw_LSQM1TGS48RFE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS48RFE0 = _Hh3cevtModuleSw_LSQM1TGS48RFE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1878)
)
_Hh3cevtModuleSw_LSQM1TGS8FC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS8FC3 = _Hh3cevtModuleSw_LSQM1TGS8FC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1879)
)
_Hh3cevtModuleSw_LSQM1TGS8FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS8FD3 = _Hh3cevtModuleSw_LSQM1TGS8FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1880)
)
_Hh3cevtModuleSw_LSUM1GP40TS8FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GP40TS8FD0 = _Hh3cevtModuleSw_LSUM1GP40TS8FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1881)
)
_Hh3cevtModuleSw_LSUM1GP48FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GP48FD0 = _Hh3cevtModuleSw_LSUM1GP48FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1882)
)
_Hh3cevtModuleSw_LSUM1GP48FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GP48FD3 = _Hh3cevtModuleSw_LSUM1GP48FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1883)
)
_Hh3cevtModuleSw_LSUM1GT48FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GT48FD0 = _Hh3cevtModuleSw_LSUM1GT48FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1884)
)
_Hh3cevtModuleSw_LSUM1GT48FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GT48FD3 = _Hh3cevtModuleSw_LSUM1GT48FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1885)
)
_Hh3cevtModuleSw_LSUM1TGS24FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS24FD0 = _Hh3cevtModuleSw_LSUM1TGS24FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1886)
)
_Hh3cevtModuleSw_LSUM1TGS24FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS24FD3 = _Hh3cevtModuleSw_LSUM1TGS24FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1887)
)
_Hh3cevtModuleSw_LSXM1GP40TS8FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP40TS8FD0 = _Hh3cevtModuleSw_LSXM1GP40TS8FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1888)
)
_Hh3cevtModuleSw_LSXM1GT48FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GT48FD3 = _Hh3cevtModuleSw_LSXM1GT48FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1889)
)
_Hh3cevtModuleSw_LSXM1TGS24FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS24FD3 = _Hh3cevtModuleSw_LSXM1TGS24FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1890)
)
_Hh3cevtModuleSw_LSQM1MPUS10C3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUS10C3 = _Hh3cevtModuleSw_LSQM1MPUS10C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1891)
)
_Hh3cevtModuleSw_LSQM1MPUSA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUSA3 = _Hh3cevtModuleSw_LSQM1MPUSA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1892)
)
_Hh3cevtModuleSw_LSQM2SUPA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2SUPA3 = _Hh3cevtModuleSw_LSQM2SUPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1893)
)
_Hh3cevtModuleSw_LSXM1SFH16E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH16E1 = _Hh3cevtModuleSw_LSXM1SFH16E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1894)
)
_Hh3cevtModuleSw_LSXM1SFH16E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH16E0 = _Hh3cevtModuleSw_LSXM1SFH16E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1895)
)
_Hh3cevtModuleSw_LSXM1GP40TS8FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP40TS8FD3 = _Hh3cevtModuleSw_LSXM1GP40TS8FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1896)
)
_Hh3cevtModuleSw_LSQM1MPUS10C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUS10C0 = _Hh3cevtModuleSw_LSQM1MPUS10C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1897)
)
_Hh3cevtModuleSw_LSQM1MPUSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUSA0 = _Hh3cevtModuleSw_LSQM1MPUSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1898)
)
_Hh3cevtModuleSw_LSQM2SUPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2SUPA0 = _Hh3cevtModuleSw_LSQM2SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1899)
)
_Hh3cevtModuleSw_LSQM1TGS16FC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS16FC3 = _Hh3cevtModuleSw_LSQM1TGS16FC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1900)
)
_Hh3cevtModuleSw_LSQM1TGS16FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS16FD0 = _Hh3cevtModuleSw_LSQM1TGS16FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1901)
)
_Hh3cevtModuleSw_LSQM1TGS16FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS16FD3 = _Hh3cevtModuleSw_LSQM1TGS16FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1902)
)
_Hh3cevtModuleSw_LSQM2TGS48SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2TGS48SG0 = _Hh3cevtModuleSw_LSQM2TGS48SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1903)
)
_Hh3cevtModuleSw_LSQM2TGS48SG3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2TGS48SG3 = _Hh3cevtModuleSw_LSQM2TGS48SG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1904)
)
_Hh3cevtModuleSw_LSXM1CGQ48HB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ48HB1 = _Hh3cevtModuleSw_LSXM1CGQ48HB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1905)
)
_Hh3cevtModuleSw_LSQM1MPUS06A8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUS06A8 = _Hh3cevtModuleSw_LSQM1MPUS06A8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1906)
)
_Hh3cevtModuleSw_LSQM1TGS16FD8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS16FD8 = _Hh3cevtModuleSw_LSQM1TGS16FD8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1907)
)
_Hh3cevtModuleSw_LSXM1SFH08E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH08E1 = _Hh3cevtModuleSw_LSXM1SFH08E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1908)
)
_Hh3cevtModuleSw_LSXM1SFH08CC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH08CC0 = _Hh3cevtModuleSw_LSXM1SFH08CC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1909)
)
_Hh3cevtModuleSw_LSXM1SUP08C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP08C0 = _Hh3cevtModuleSw_LSXM1SUP08C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1910)
)
_Hh3cevtModuleSw_LSUM2FAB04D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB04D0 = _Hh3cevtModuleSw_LSUM2FAB04D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1911)
)
_Hh3cevtModuleSw_LSUM2FAB04D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB04D3 = _Hh3cevtModuleSw_LSUM2FAB04D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1912)
)
_Hh3cevtModuleSw_LSXM2FAB04D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2FAB04D3 = _Hh3cevtModuleSw_LSXM2FAB04D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1913)
)
_Hh3cevtModuleSw_LSUM2FAB04B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB04B0 = _Hh3cevtModuleSw_LSUM2FAB04B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1914)
)
_Hh3cevtModuleSw_LSUM2FAB04B3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB04B3 = _Hh3cevtModuleSw_LSUM2FAB04B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1915)
)
_Hh3cevtModuleSw_LSUM2FAB08D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB08D0 = _Hh3cevtModuleSw_LSUM2FAB08D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1916)
)
_Hh3cevtModuleSw_LSUM2FAB08D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB08D3 = _Hh3cevtModuleSw_LSUM2FAB08D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1917)
)
_Hh3cevtModuleSw_LSXM2FAB08D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2FAB08D3 = _Hh3cevtModuleSw_LSXM2FAB08D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1918)
)
_Hh3cevtModuleSw_LSUM2FAB08B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB08B0 = _Hh3cevtModuleSw_LSUM2FAB08B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1919)
)
_Hh3cevtModuleSw_LSUM2FAB08B3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB08B3 = _Hh3cevtModuleSw_LSUM2FAB08B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1920)
)
_Hh3cevtModuleSw_LSUM2FAB12D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB12D0 = _Hh3cevtModuleSw_LSUM2FAB12D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1921)
)
_Hh3cevtModuleSw_LSUM2FAB12D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB12D3 = _Hh3cevtModuleSw_LSUM2FAB12D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1922)
)
_Hh3cevtModuleSw_LSXM2FAB12D3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2FAB12D3 = _Hh3cevtModuleSw_LSXM2FAB12D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1923)
)
_Hh3cevtModuleSw_LSUM2FAB12B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB12B0 = _Hh3cevtModuleSw_LSUM2FAB12B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1924)
)
_Hh3cevtModuleSw_LSUM2FAB12B3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2FAB12B3 = _Hh3cevtModuleSw_LSUM2FAB12B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1925)
)
_Hh3cevtModuleSw_LSQM1CGS2FE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGS2FE0 = _Hh3cevtModuleSw_LSQM1CGS2FE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1926)
)
_Hh3cevtModuleSw_LSQM1CGS2FE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGS2FE3 = _Hh3cevtModuleSw_LSQM1CGS2FE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1927)
)
_Hh3cevtModuleSw_LSQM1CGS2XFE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGS2XFE0 = _Hh3cevtModuleSw_LSQM1CGS2XFE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1928)
)
_Hh3cevtModuleSw_LSUM1CGS2FE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS2FE0 = _Hh3cevtModuleSw_LSUM1CGS2FE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1929)
)
_Hh3cevtModuleSw_LSUM1CGS2FE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS2FE3 = _Hh3cevtModuleSw_LSUM1CGS2FE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1930)
)
_Hh3cevtModuleSw_LSXM1CGS2FE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGS2FE3 = _Hh3cevtModuleSw_LSXM1CGS2FE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1931)
)
_Hh3cevtModuleSw_LSUM1TGS16FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS16FD0 = _Hh3cevtModuleSw_LSUM1TGS16FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1932)
)
_Hh3cevtModuleSw_LSUM1TGS16FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS16FD3 = _Hh3cevtModuleSw_LSUM1TGS16FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1933)
)
_Hh3cevtModuleSw_LSQM1TGS16XFD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS16XFD0 = _Hh3cevtModuleSw_LSQM1TGS16XFD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1934)
)
_Hh3cevtModuleSw_LSQM1GP40TS8FC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP40TS8FC3 = _Hh3cevtModuleSw_LSQM1GP40TS8FC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1935)
)
_Hh3cevtModuleSw_S76_16XFSF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S76_16XFSF = _Hh3cevtModuleSw_S76_16XFSF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1936)
)
_Hh3cevtModuleSw_S76_24EP2XFSC_OLT_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S76_24EP2XFSC_OLT = _Hh3cevtModuleSw_S76_24EP2XFSC_OLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1937)
)
_Hh3cevtModuleSw_DS_3E7600_24T20F4X_SC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_24T20F4X_SC = _Hh3cevtModuleSw_DS_3E7600_24T20F4X_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1938)
)
_Hh3cevtModuleSw_LSUM1FAB04E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB04E0 = _Hh3cevtModuleSw_LSUM1FAB04E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1939)
)
_Hh3cevtModuleSw_LSUM1FAB08E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB08E0 = _Hh3cevtModuleSw_LSUM1FAB08E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1940)
)
_Hh3cevtModuleSw_LSUM1FAB12E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB12E0 = _Hh3cevtModuleSw_LSUM1FAB12E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1941)
)
_Hh3cevtModuleSw_LSXM1CGQ8FX1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ8FX1 = _Hh3cevtModuleSw_LSXM1CGQ8FX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1942)
)
_Hh3cevtModuleSw_LSQM1IPSDSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1IPSDSC0 = _Hh3cevtModuleSw_LSQM1IPSDSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1943)
)
_Hh3cevtModuleSw_LSQM2ACGDSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2ACGDSC0 = _Hh3cevtModuleSw_LSQM2ACGDSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1944)
)
_Hh3cevtModuleSw_LSQM1ADEDSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1ADEDSC0 = _Hh3cevtModuleSw_LSQM1ADEDSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1945)
)
_Hh3cevtModuleSw_LSWM1ADED0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1ADED0 = _Hh3cevtModuleSw_LSWM1ADED0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1946)
)
_Hh3cevtModuleSw_LSWM1IPSD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1IPSD0 = _Hh3cevtModuleSw_LSWM1IPSD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1947)
)
_Hh3cevtModuleSw_LSQM1GP40TS8FD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1GP40TS8FD3 = _Hh3cevtModuleSw_LSQM1GP40TS8FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1948)
)
_Hh3cevtModuleSw_LSUM1SUPXD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1SUPXD0 = _Hh3cevtModuleSw_LSUM1SUPXD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1949)
)
_Hh3cevtModuleSw_LSUM1CQGS32SF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CQGS32SF0 = _Hh3cevtModuleSw_LSUM1CQGS32SF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1950)
)
_Hh3cevtModuleSw_LSUM1TGS48XSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS48XSG0 = _Hh3cevtModuleSw_LSUM1TGS48XSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1951)
)
_Hh3cevtModuleSw_LSUM1FAB08XE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB08XE0 = _Hh3cevtModuleSw_LSUM1FAB08XE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1952)
)
_Hh3cevtModuleSw_LSUM1FAB16XD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB16XD0 = _Hh3cevtModuleSw_LSUM1FAB16XD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1953)
)
_Hh3cevtModuleSw_LSXM1SFH02E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH02E0 = _Hh3cevtModuleSw_LSXM1SFH02E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1954)
)
_Hh3cevtModuleSw_LSXM1SFH02E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH02E1 = _Hh3cevtModuleSw_LSXM1SFH02E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1955)
)
_Hh3cevtModuleSw_LSXM1SFH12C0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH12C0 = _Hh3cevtModuleSw_LSXM1SFH12C0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1956)
)
_Hh3cevtModuleSw_LSXM1SFH12C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH12C1 = _Hh3cevtModuleSw_LSXM1SFH12C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1957)
)
_Hh3cevtModuleSw_LSUM1CQGS12XSG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CQGS12XSG0 = _Hh3cevtModuleSw_LSUM1CQGS12XSG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1958)
)
_Hh3cevtModuleSw_LSQM1CTGS24QSFD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CTGS24QSFD0 = _Hh3cevtModuleSw_LSQM1CTGS24QSFD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1959)
)
_Hh3cevtModuleSw_LSQM1TGS24QSFD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS24QSFD0 = _Hh3cevtModuleSw_LSQM1TGS24QSFD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1960)
)
_Hh3cevtModuleSw_LSUM1WBCZ720RT_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1WBCZ720RT = _Hh3cevtModuleSw_LSUM1WBCZ720RT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1961)
)
_Hh3cevtModuleSw_LSQM1WBCZ720_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1WBCZ720 = _Hh3cevtModuleSw_LSQM1WBCZ720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1962)
)
_Hh3cevtModuleSw_DS_3E7610X_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7610X_MPU = _Hh3cevtModuleSw_DS_3E7610X_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1963)
)
_Hh3cevtModuleSw_DS_3E7610X_CLOS_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7610X_CLOS = _Hh3cevtModuleSw_DS_3E7610X_CLOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1964)
)
_Hh3cevtModuleSw_DS_3E7610X_32X4QX_SF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7610X_32X4QX_SF = _Hh3cevtModuleSw_DS_3E7610X_32X4QX_SF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1965)
)
_Hh3cevtModuleSw_DS_3E7610X_16X_SF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7610X_16X_SF = _Hh3cevtModuleSw_DS_3E7610X_16X_SF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1966)
)
_Hh3cevtModuleSw_DS_3E7610X_44F4X_SE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7610X_44F4X_SE = _Hh3cevtModuleSw_DS_3E7610X_44F4X_SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1967)
)
_Hh3cevtModuleSw_DS_3E7610X_48T_SE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7610X_48T_SE = _Hh3cevtModuleSw_DS_3E7610X_48T_SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1968)
)
_Hh3cevtModuleSw_LSQM2GT24PTSSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT24PTSSC8 = _Hh3cevtModuleSw_LSQM2GT24PTSSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1969)
)
_Hh3cevtModuleSw_LSQM1CGP24TSSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGP24TSSC8 = _Hh3cevtModuleSw_LSQM1CGP24TSSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1970)
)
_Hh3cevtModuleSw_LSQM1CGT24TSSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1CGT24TSSC8 = _Hh3cevtModuleSw_LSQM1CGT24TSSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1971)
)
_Hh3cevtModuleSw_LSQM1MPUS06B8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUS06B8 = _Hh3cevtModuleSw_LSQM1MPUS06B8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1972)
)
_Hh3cevtModuleSw_LSVM1MPUB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSVM1MPUB1 = _Hh3cevtModuleSw_LSVM1MPUB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1973)
)
_Hh3cevtModuleSw_LSXM1TGS24QGMODHB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS24QGMODHB0 = _Hh3cevtModuleSw_LSXM1TGS24QGMODHB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1974)
)
_Hh3cevtModuleSw_LSXM1TGS24QGMODHB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS24QGMODHB1 = _Hh3cevtModuleSw_LSXM1TGS24QGMODHB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1975)
)
_Hh3cevtModuleSw_LSXM1TGS48QGHA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48QGHA0 = _Hh3cevtModuleSw_LSXM1TGS48QGHA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1976)
)
_Hh3cevtModuleSw_LSXM1TGS48QGHA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48QGHA1 = _Hh3cevtModuleSw_LSXM1TGS48QGHA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1977)
)
_Hh3cevtModuleSw_LSXM1CGC2A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGC2A0 = _Hh3cevtModuleSw_LSXM1CGC2A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1978)
)
_Hh3cevtModuleSw_LSXM1CGC2A1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGC2A1 = _Hh3cevtModuleSw_LSXM1CGC2A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1979)
)
_Hh3cevtModuleSw_LSQM2FWDSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2FWDSC0 = _Hh3cevtModuleSw_LSQM2FWDSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1980)
)
_Hh3cevtModuleSw_LSQM1XPT12TSFD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1XPT12TSFD0 = _Hh3cevtModuleSw_LSQM1XPT12TSFD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1981)
)
_Hh3cevtModuleSw_LSXM1QGS24HB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24HB0 = _Hh3cevtModuleSw_LSXM1QGS24HB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1982)
)
_Hh3cevtModuleSw_LSXM1QGS24HB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24HB1 = _Hh3cevtModuleSw_LSXM1QGS24HB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1983)
)
_Hh3cevtModuleSw_LSXM1QGS24HC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24HC0 = _Hh3cevtModuleSw_LSXM1QGS24HC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1984)
)
_Hh3cevtModuleSw_LSXM1SUP01B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP01B1 = _Hh3cevtModuleSw_LSXM1SUP01B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1985)
)
_Hh3cevtModuleSw_LSCM1SUP03A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1SUP03A0 = _Hh3cevtModuleSw_LSCM1SUP03A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1986)
)
_Hh3cevtModuleSw_LSCM1SUP03A0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1SUP03A0_Z = _Hh3cevtModuleSw_LSCM1SUP03A0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1987)
)
_Hh3cevtModuleSw_LSCM1MPUS06A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1MPUS06A0 = _Hh3cevtModuleSw_LSCM1MPUS06A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1988)
)
_Hh3cevtModuleSw_LSCM1MPUS06A0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1MPUS06A0_Z = _Hh3cevtModuleSw_LSCM1MPUS06A0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1989)
)
_Hh3cevtModuleSw_LSCM1GT48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1GT48SC0 = _Hh3cevtModuleSw_LSCM1GT48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1990)
)
_Hh3cevtModuleSw_LSCM1GT48SC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1GT48SC0_Z = _Hh3cevtModuleSw_LSCM1GT48SC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1991)
)
_Hh3cevtModuleSw_LSCM1TGS48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1TGS48SE0 = _Hh3cevtModuleSw_LSCM1TGS48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1992)
)
_Hh3cevtModuleSw_LSCM1TGS48SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1TGS48SE0_Z = _Hh3cevtModuleSw_LSCM1TGS48SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1993)
)
_Hh3cevtModuleSw_LSCM1QGS8CSSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1QGS8CSSE0 = _Hh3cevtModuleSw_LSCM1QGS8CSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1994)
)
_Hh3cevtModuleSw_LSCM1QGS8CSSE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1QGS8CSSE0_Z = _Hh3cevtModuleSw_LSCM1QGS8CSSE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1995)
)
_Hh3cevtModuleSw_LSWM2SP4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP4P = _Hh3cevtModuleSw_LSWM2SP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1996)
)
_Hh3cevtModuleSw_LSWM2SP4P_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP4P_Z = _Hh3cevtModuleSw_LSWM2SP4P_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1997)
)
_Hh3cevtModuleSw_LSQM1MPUS10B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUS10B0 = _Hh3cevtModuleSw_LSQM1MPUS10B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1998)
)
_Hh3cevtModuleSw_LSQM1MPUS10B3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUS10B3 = _Hh3cevtModuleSw_LSQM1MPUS10B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 1999)
)
_Hh3cevtModuleSw_LSQM1MPUSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUSC0 = _Hh3cevtModuleSw_LSQM1MPUSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2000)
)
_Hh3cevtModuleSw_LSQM1MPUSC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUSC3 = _Hh3cevtModuleSw_LSQM1MPUSC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2001)
)
_Hh3cevtModuleSw_LSQM2GP24TSSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP24TSSC8 = _Hh3cevtModuleSw_LSQM2GP24TSSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2002)
)
_Hh3cevtModuleSw_LSQM2GT24TSSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT24TSSC8 = _Hh3cevtModuleSw_LSQM2GT24TSSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2003)
)
_Hh3cevtModuleSw_LSXM1TGS24CGMODHD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS24CGMODHD0 = _Hh3cevtModuleSw_LSXM1TGS24CGMODHD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2004)
)
_Hh3cevtModuleSw_LSXM1TGS24CGMODHD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS24CGMODHD1 = _Hh3cevtModuleSw_LSXM1TGS24CGMODHD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2005)
)
_Hh3cevtModuleSw_LSQM1TGS16GPSA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS16GPSA0 = _Hh3cevtModuleSw_LSQM1TGS16GPSA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2006)
)
_Hh3cevtModuleSw_EWPXM2TGS48SG0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM2TGS48SG0 = _Hh3cevtModuleSw_EWPXM2TGS48SG0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2007)
)
_Hh3cevtModuleSw_EWPXM1TGS16FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM1TGS16FD0 = _Hh3cevtModuleSw_EWPXM1TGS16FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2008)
)
_Hh3cevtModuleSw_LSXM1CGQ36HF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36HF0 = _Hh3cevtModuleSw_LSXM1CGQ36HF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2009)
)
_Hh3cevtModuleSw_LSXM2SUPT0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2SUPT0 = _Hh3cevtModuleSw_LSXM2SUPT0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2010)
)
_Hh3cevtModuleSw_LSXM2SUPT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2SUPT1 = _Hh3cevtModuleSw_LSXM2SUPT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2011)
)
_Hh3cevtModuleSw_LSXM1SFT16E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFT16E0 = _Hh3cevtModuleSw_LSXM1SFT16E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2012)
)
_Hh3cevtModuleSw_LSXM1SFT16E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFT16E1 = _Hh3cevtModuleSw_LSXM1SFT16E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2013)
)
_Hh3cevtModuleSw_lsxM1CGQ36TD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_lsxM1CGQ36TD0 = _Hh3cevtModuleSw_lsxM1CGQ36TD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2014)
)
_Hh3cevtModuleSw_lsxM1CGQ36TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_lsxM1CGQ36TD1 = _Hh3cevtModuleSw_lsxM1CGQ36TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2015)
)
_Hh3cevtModuleSw_LSQM1TGT24FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGT24FD0 = _Hh3cevtModuleSw_LSQM1TGT24FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2016)
)
_Hh3cevtModuleSw_LSUM1TGT24FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGT24FD0 = _Hh3cevtModuleSw_LSUM1TGT24FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2017)
)
_Hh3cevtModuleSw_LSXM2SFT08E0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2SFT08E0 = _Hh3cevtModuleSw_LSXM2SFT08E0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2018)
)
_Hh3cevtModuleSw_LSXM2SFT08E1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2SFT08E1 = _Hh3cevtModuleSw_LSXM2SFT08E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2019)
)
_Hh3cevtModuleSw_LSXM1CCP8HF0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CCP8HF0 = _Hh3cevtModuleSw_LSXM1CCP8HF0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2020)
)
_Hh3cevtModuleSw_LSXM1CCP8HF1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CCP8HF1 = _Hh3cevtModuleSw_LSXM1CCP8HF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2021)
)
_Hh3cevtModuleSw_S8610_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S8610_MPU = _Hh3cevtModuleSw_S8610_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2028)
)
_Hh3cevtModuleSw_S8610_NET_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S8610_NET = _Hh3cevtModuleSw_S8610_NET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2029)
)
_Hh3cevtModuleSw_S86_44GF4XFSE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S86_44GF4XFSE = _Hh3cevtModuleSw_S86_44GF4XFSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2030)
)
_Hh3cevtModuleSw_S86_48GTSE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S86_48GTSE = _Hh3cevtModuleSw_S86_48GTSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2031)
)
_Hh3cevtModuleSw_S86_12QFSG_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S86_12QFSG = _Hh3cevtModuleSw_S86_12QFSG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2032)
)
_Hh3cevtModuleSw_S86_48XFSG_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S86_48XFSG = _Hh3cevtModuleSw_S86_48XFSG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2033)
)
_Hh3cevtModuleSw_LSUM1MPUS06XEC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS06XEC0 = _Hh3cevtModuleSw_LSUM1MPUS06XEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2034)
)
_Hh3cevtModuleSw_LSUM1MPUS10XE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS10XE0 = _Hh3cevtModuleSw_LSUM1MPUS10XE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2035)
)
_Hh3cevtModuleSw_LSUM1MPUS10XEB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS10XEB0 = _Hh3cevtModuleSw_LSUM1MPUS10XEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2036)
)
_Hh3cevtModuleSw_LSUM1FAB06XEC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB06XEC0 = _Hh3cevtModuleSw_LSUM1FAB06XEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2037)
)
_Hh3cevtModuleSw_LSUM1FAB10XE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10XE0 = _Hh3cevtModuleSw_LSUM1FAB10XE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2038)
)
_Hh3cevtModuleSw_LSUM1FAB10XEB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10XEB0 = _Hh3cevtModuleSw_LSUM1FAB10XEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2039)
)
_Hh3cevtModuleSw_LSUM1FAB08XEB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB08XEB0 = _Hh3cevtModuleSw_LSUM1FAB08XEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2040)
)
_Hh3cevtModuleSw_LSUM1TGS48SH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS48SH0 = _Hh3cevtModuleSw_LSUM1TGS48SH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2041)
)
_Hh3cevtModuleSw_LSUM1CGS8SH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS8SH0 = _Hh3cevtModuleSw_LSUM1CGS8SH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2042)
)
_Hh3cevtModuleSw_LSUM1YGS24CSSH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1YGS24CSSH0 = _Hh3cevtModuleSw_LSUM1YGS24CSSH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2043)
)
_Hh3cevtModuleSw_LSUM1CGS20XSH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS20XSH0 = _Hh3cevtModuleSw_LSUM1CGS20XSH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2044)
)
_Hh3cevtModuleSw_LSUM1CGS32XSH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS32XSH0 = _Hh3cevtModuleSw_LSUM1CGS32XSH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2045)
)
_Hh3cevtModuleSw_LSUM1CGS8QSSH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS8QSSH0 = _Hh3cevtModuleSw_LSUM1CGS8QSSH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2046)
)
_Hh3cevtModuleSw_LSUM1YGS48XSH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1YGS48XSH0 = _Hh3cevtModuleSw_LSUM1YGS48XSH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2047)
)
_Hh3cevtModuleSw_LSXM3SUPT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3SUPT1 = _Hh3cevtModuleSw_LSXM3SUPT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2048)
)
_Hh3cevtModuleSw_LSXM4SUPT1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM4SUPT1 = _Hh3cevtModuleSw_LSXM4SUPT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2049)
)
_Hh3cevtModuleSw_LSQM2GP24TSSA0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP24TSSA0_Z = _Hh3cevtModuleSw_LSQM2GP24TSSA0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2050)
)
_Hh3cevtModuleSw_LSQM2GT48SA0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GT48SA0_Z = _Hh3cevtModuleSw_LSQM2GT48SA0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2051)
)
_Hh3cevtModuleSw_LSQM2GP48SA0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP48SA0_Z = _Hh3cevtModuleSw_LSQM2GP48SA0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2052)
)
_Hh3cevtModuleSw_LSUM2TGS48SG0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2TGS48SG0_Z = _Hh3cevtModuleSw_LSUM2TGS48SG0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2053)
)
_Hh3cevtModuleSw_LSUM2QGS12SG0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2QGS12SG0_Z = _Hh3cevtModuleSw_LSUM2QGS12SG0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2054)
)
_Hh3cevtModuleSw_LSUM2TGS32QSSG0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2TGS32QSSG0_Z = _Hh3cevtModuleSw_LSUM2TGS32QSSG0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2055)
)
_Hh3cevtModuleSw_LSUM1TGS48RSH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS48RSH0 = _Hh3cevtModuleSw_LSUM1TGS48RSH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2056)
)
_Hh3cevtModuleSw_LSUM1MPUS06XEB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS06XEB0 = _Hh3cevtModuleSw_LSUM1MPUS06XEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2057)
)
_Hh3cevtModuleSw_LSUM1MPUS10XEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS10XEA0 = _Hh3cevtModuleSw_LSUM1MPUS10XEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2058)
)
_Hh3cevtModuleSw_LSUM1FAB06XEB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB06XEB0 = _Hh3cevtModuleSw_LSUM1FAB06XEB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2059)
)
_Hh3cevtModuleSw_LSUM1FAB10XEA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10XEA0 = _Hh3cevtModuleSw_LSUM1FAB10XEA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2060)
)
_Hh3cevtModuleSw_EWPXM1WCMX100_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_EWPXM1WCMX100 = _Hh3cevtModuleSw_EWPXM1WCMX100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2061)
)
_Hh3cevtModuleSw_LSQM1WBCZ720X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1WBCZ720X = _Hh3cevtModuleSw_LSQM1WBCZ720X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2062)
)
_Hh3cevtModuleSw_LSUM1WBCZ720XRT_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1WBCZ720XRT = _Hh3cevtModuleSw_LSUM1WBCZ720XRT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2063)
)
_Hh3cevtModuleSw_LSXM1CGQ8TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ8TD1 = _Hh3cevtModuleSw_LSXM1CGQ8TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2064)
)
_Hh3cevtModuleSw_LSXM1CGQ12TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ12TD1 = _Hh3cevtModuleSw_LSXM1CGQ12TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2065)
)
_Hh3cevtModuleSw_LSXM1CGQ18TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18TD1 = _Hh3cevtModuleSw_LSXM1CGQ18TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2066)
)
_Hh3cevtModuleSw_LSXM1QGS24C6TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24C6TD1 = _Hh3cevtModuleSw_LSXM1QGS24C6TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2067)
)
_Hh3cevtModuleSw_LSXM1QGS36TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS36TD1 = _Hh3cevtModuleSw_LSXM1QGS36TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2068)
)
_Hh3cevtModuleSw_LSXM1QGS48TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS48TD1 = _Hh3cevtModuleSw_LSXM1QGS48TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2069)
)
_Hh3cevtModuleSw_LSXM1TGS48C4TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48C4TD1 = _Hh3cevtModuleSw_LSXM1TGS48C4TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2070)
)
_Hh3cevtModuleSw_LSXM1GP48TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP48TD1 = _Hh3cevtModuleSw_LSXM1GP48TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2071)
)
_Hh3cevtModuleSw_LSXM1TGS48TD1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48TD1 = _Hh3cevtModuleSw_LSXM1TGS48TD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2072)
)
_Hh3cevtModuleSw_LSWM124TG2H1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM124TG2H1 = _Hh3cevtModuleSw_LSWM124TG2H1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2076)
)
_Hh3cevtModuleSw_LSQM2FWDSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2FWDSC8 = _Hh3cevtModuleSw_LSQM2FWDSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2077)
)
_Hh3cevtModuleSw_IM_MSEX_B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_MSEX_B = _Hh3cevtModuleSw_IM_MSEX_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2080)
)
_Hh3cevtModuleSw_IM_MSEX_B_IM_SP_B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_IM_MSEX_B_IM_SP_B = _Hh3cevtModuleSw_IM_MSEX_B_IM_SP_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2081)
)
_Hh3cevtModuleSw_LSUM1MPUS06XEC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS06XEC0_Z = _Hh3cevtModuleSw_LSUM1MPUS06XEC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2082)
)
_Hh3cevtModuleSw_LSUM1CGS8SH0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS8SH0_Z = _Hh3cevtModuleSw_LSUM1CGS8SH0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2083)
)
_Hh3cevtModuleSw_LSUM1SUPXD0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1SUPXD0_Z = _Hh3cevtModuleSw_LSUM1SUPXD0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2084)
)
_Hh3cevtModuleSw_LSUM1FAB08XE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB08XE0_Z = _Hh3cevtModuleSw_LSUM1FAB08XE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2085)
)
_Hh3cevtModuleSw_LSUM1CGS20XSH0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS20XSH0_Z = _Hh3cevtModuleSw_LSUM1CGS20XSH0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2086)
)
_Hh3cevtModuleSw_LSUM1FAB06XEC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB06XEC0_Z = _Hh3cevtModuleSw_LSUM1FAB06XEC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2087)
)
_Hh3cevtModuleSw_LSUM1CQGS32SF0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CQGS32SF0_Z = _Hh3cevtModuleSw_LSUM1CQGS32SF0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2088)
)
_Hh3cevtModuleSw_LSXM1FAB10XE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FAB10XE3 = _Hh3cevtModuleSw_LSXM1FAB10XE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2089)
)
_Hh3cevtModuleSw_LSXM1FAB08XE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FAB08XE3 = _Hh3cevtModuleSw_LSXM1FAB08XE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2090)
)
_Hh3cevtModuleSw_LSXM1YGS48XSH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1YGS48XSH3 = _Hh3cevtModuleSw_LSXM1YGS48XSH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2091)
)
_Hh3cevtModuleSw_LSXM1YGS24CSSH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1YGS24CSSH3 = _Hh3cevtModuleSw_LSXM1YGS24CSSH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2092)
)
_Hh3cevtModuleSw_LSXM1CGS8QSSH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGS8QSSH3 = _Hh3cevtModuleSw_LSXM1CGS8QSSH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2093)
)
_Hh3cevtModuleSw_LSXM1TGS48SH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48SH3 = _Hh3cevtModuleSw_LSXM1TGS48SH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2094)
)
_Hh3cevtModuleSw_LSXM1MPUS10XE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1MPUS10XE3 = _Hh3cevtModuleSw_LSXM1MPUS10XE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2095)
)
_Hh3cevtModuleSw_LSXM1FAB06XEC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1FAB06XEC3 = _Hh3cevtModuleSw_LSXM1FAB06XEC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2096)
)
_Hh3cevtModuleSw_LSXM1MPUS06XEC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1MPUS06XEC3 = _Hh3cevtModuleSw_LSXM1MPUS06XEC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2097)
)
_Hh3cevtModuleSw_LSXM1CGS8SH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGS8SH3 = _Hh3cevtModuleSw_LSXM1CGS8SH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2098)
)
_Hh3cevtModuleSw_LSXM1SUPXD3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPXD3 = _Hh3cevtModuleSw_LSXM1SUPXD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2099)
)
_Hh3cevtModuleSw_LSXM1CGS20XSH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGS20XSH3 = _Hh3cevtModuleSw_LSXM1CGS20XSH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2100)
)
_Hh3cevtModuleSw_LSUM1GP48FD0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GP48FD0_Z = _Hh3cevtModuleSw_LSUM1GP48FD0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2101)
)
_Hh3cevtModuleSw_LSQM1TGS48RFE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS48RFE0_Z = _Hh3cevtModuleSw_LSQM1TGS48RFE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2102)
)
_Hh3cevtModuleSw_LSXM1CGS32XSH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGS32XSH3 = _Hh3cevtModuleSw_LSXM1CGS32XSH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2103)
)
_Hh3cevtModuleSw_LSQM2GP40TS8FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2GP40TS8FD0 = _Hh3cevtModuleSw_LSQM2GP40TS8FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2104)
)
_Hh3cevtModuleSw_LSUM1SUPXES0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1SUPXES0 = _Hh3cevtModuleSw_LSUM1SUPXES0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2105)
)
_Hh3cevtModuleSw_LSQM2SUPB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2SUPB0 = _Hh3cevtModuleSw_LSQM2SUPB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2106)
)
_Hh3cevtModuleSw_LSUM2GP40TS8FD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2GP40TS8FD0 = _Hh3cevtModuleSw_LSUM2GP40TS8FD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2107)
)
_Hh3cevtModuleSw_LSXM1YGS48XXSH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1YGS48XXSH3 = _Hh3cevtModuleSw_LSXM1YGS48XXSH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2108)
)
_Hh3cevtModuleSw_LSXM2SFT08E2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2SFT08E2 = _Hh3cevtModuleSw_LSXM2SFT08E2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2109)
)
_Hh3cevtModuleSw_LSXM1TGS48TD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48TD2 = _Hh3cevtModuleSw_LSXM1TGS48TD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2110)
)
_Hh3cevtModuleSw_LSXM1CGQ36TD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36TD2 = _Hh3cevtModuleSw_LSXM1CGQ36TD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2111)
)
_Hh3cevtModuleSw_RX_NIC_LGQ4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_LGQ4L = _Hh3cevtModuleSw_RX_NIC_LGQ4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2112)
)
_Hh3cevtModuleSw_LSXM1CDQ24KB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CDQ24KB1 = _Hh3cevtModuleSw_LSXM1CDQ24KB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2113)
)
_Hh3cevtModuleSw_LSXM1SUP02L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP02L1 = _Hh3cevtModuleSw_LSXM1SUP02L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2114)
)
_Hh3cevtModuleSw_LSXM1CGQ48KB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ48KB1 = _Hh3cevtModuleSw_LSXM1CGQ48KB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2115)
)
_Hh3cevtModuleSw_LSXM1SFK08F1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFK08F1 = _Hh3cevtModuleSw_LSXM1SFK08F1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2116)
)
_Hh3cevtModuleSw_CSPEX_1214X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1214X = _Hh3cevtModuleSw_CSPEX_1214X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2117)
)
_Hh3cevtModuleSw_MIC_CQ1L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CQ1L1 = _Hh3cevtModuleSw_MIC_CQ1L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2118)
)
_Hh3cevtModuleSw_DS_3E7600_16X_SCB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7600_16X_SCB = _Hh3cevtModuleSw_DS_3E7600_16X_SCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2119)
)
_Hh3cevtModuleSw_DS_3E12508_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E12508_MPU = _Hh3cevtModuleSw_DS_3E12508_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2120)
)
_Hh3cevtModuleSw_DS_3E12500_7610_48T_SE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E12500_7610_48T_SE = _Hh3cevtModuleSw_DS_3E12500_7610_48T_SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2121)
)
_Hh3cevtModuleSw_DS_3E7603_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E7603_MPU = _Hh3cevtModuleSw_DS_3E7603_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2122)
)
_Hh3cevtModuleSw_DS_3E12500_7610_16X_SF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E12500_7610_16X_SF = _Hh3cevtModuleSw_DS_3E12500_7610_16X_SF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2123)
)
_Hh3cevtModuleSw_DS_3E12500_24T20F4X_SE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E12500_24T20F4X_SE = _Hh3cevtModuleSw_DS_3E12500_24T20F4X_SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2124)
)
_Hh3cevtModuleSw_DS_3E12500_12Q_SG_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E12500_12Q_SG = _Hh3cevtModuleSw_DS_3E12500_12Q_SG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2125)
)
_Hh3cevtModuleSw_DS_3E12500_48X_SG_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E12500_48X_SG = _Hh3cevtModuleSw_DS_3E12500_48X_SG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2126)
)
_Hh3cevtModuleSw_DS_3E12500_7610_32X4QX_SF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E12500_7610_32X4QX_SF = _Hh3cevtModuleSw_DS_3E12500_7610_32X4QX_SF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2127)
)
_Hh3cevtModuleSw_DS_3E12500_7610_44F4X_SE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E12500_7610_44F4X_SE = _Hh3cevtModuleSw_DS_3E12500_7610_44F4X_SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2128)
)
_Hh3cevtModuleSw_DS_3E12508_CLOS_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DS_3E12508_CLOS = _Hh3cevtModuleSw_DS_3E12508_CLOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2129)
)
_Hh3cevtModuleSw_LSXM2SUPT2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2SUPT2 = _Hh3cevtModuleSw_LSXM2SUPT2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2130)
)
_Hh3cevtModuleSw_CSR05SRP1P3A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR05SRP1P3A = _Hh3cevtModuleSw_CSR05SRP1P3A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2131)
)
_Hh3cevtModuleSw_CSFC_08E1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_08E1A = _Hh3cevtModuleSw_CSFC_08E1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2132)
)
_Hh3cevtModuleSw_CSFC_16EA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_16EA = _Hh3cevtModuleSw_CSFC_16EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2133)
)
_Hh3cevtModuleSw_CSPEX_1602XA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1602XA = _Hh3cevtModuleSw_CSPEX_1602XA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2134)
)
_Hh3cevtModuleSw_CEPC_CP4RXA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_CP4RXA = _Hh3cevtModuleSw_CEPC_CP4RXA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2135)
)
_Hh3cevtModuleSw_CSPEX_1504XA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1504XA = _Hh3cevtModuleSw_CSPEX_1504XA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2136)
)
_Hh3cevtModuleSw_CSPEX_1804XA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1804XA = _Hh3cevtModuleSw_CSPEX_1804XA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2137)
)
_Hh3cevtModuleSw_MIC_GP10LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GP10LA = _Hh3cevtModuleSw_MIC_GP10LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2138)
)
_Hh3cevtModuleSw_MIC_GT20LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_GT20LA = _Hh3cevtModuleSw_MIC_GT20LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2139)
)
_Hh3cevtModuleSw_MIC_XP20LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_XP20LA = _Hh3cevtModuleSw_MIC_XP20LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2140)
)
_Hh3cevtModuleSw_LSDM1QGS12SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1QGS12SE0_Z = _Hh3cevtModuleSw_LSDM1QGS12SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2142)
)
_Hh3cevtModuleSw_LSDM1TGS48SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1TGS48SE0_Z = _Hh3cevtModuleSw_LSDM1TGS48SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2143)
)
_Hh3cevtModuleSw_LSDM1SUPA0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1SUPA0_Z = _Hh3cevtModuleSw_LSDM1SUPA0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2144)
)
_Hh3cevtModuleSw_LSDM1FAB08D0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1FAB08D0_Z = _Hh3cevtModuleSw_LSDM1FAB08D0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2145)
)
_Hh3cevtModuleSw_LSDM1GT24GPSE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1GT24GPSE0_Z = _Hh3cevtModuleSw_LSDM1GT24GPSE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2146)
)
_Hh3cevtModuleSw_LSXM1CGQ18TD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18TD2 = _Hh3cevtModuleSw_LSXM1CGQ18TD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2147)
)
_Hh3cevtModuleSw_LSXM1QGS36TD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS36TD2 = _Hh3cevtModuleSw_LSXM1QGS36TD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2148)
)
_Hh3cevtModuleSw_RP_S_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RP_S_G = _Hh3cevtModuleSw_RP_S_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2149)
)
_Hh3cevtModuleSw_MOD20_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MOD20_G = _Hh3cevtModuleSw_MOD20_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2150)
)
_Hh3cevtModuleSw_MPA_PSP4L_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MPA_PSP4L_G = _Hh3cevtModuleSw_MPA_PSP4L_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2151)
)
_Hh3cevtModuleSw_MPA_TCP8L_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MPA_TCP8L_G = _Hh3cevtModuleSw_MPA_TCP8L_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2152)
)
_Hh3cevtModuleSw_MPA_ET16L_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MPA_ET16L_G = _Hh3cevtModuleSw_MPA_ET16L_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2153)
)
_Hh3cevtModuleSw_MPA_GP10L_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MPA_GP10L_G = _Hh3cevtModuleSw_MPA_GP10L_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2154)
)
_Hh3cevtModuleSw_MPA_XP4L_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MPA_XP4L_G = _Hh3cevtModuleSw_MPA_XP4L_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2155)
)
_Hh3cevtModuleSw_LSXM1SFH04DR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH04DR1 = _Hh3cevtModuleSw_LSXM1SFH04DR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2156)
)
_Hh3cevtModuleSw_LSXM1SFH08CR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH08CR1 = _Hh3cevtModuleSw_LSXM1SFH08CR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2157)
)
_Hh3cevtModuleSw_LSXM1SFH08DR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH08DR1 = _Hh3cevtModuleSw_LSXM1SFH08DR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2158)
)
_Hh3cevtModuleSw_LSXM1SFH16CR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH16CR1 = _Hh3cevtModuleSw_LSXM1SFH16CR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2159)
)
_Hh3cevtModuleSw_LSXM1SFH16ER1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFH16ER1 = _Hh3cevtModuleSw_LSXM1SFH16ER1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2160)
)
_Hh3cevtModuleSw_LSXM1TGS48HFR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48HFR1 = _Hh3cevtModuleSw_LSXM1TGS48HFR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2161)
)
_Hh3cevtModuleSw_LSXM1CGQ18QGHFR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18QGHFR1 = _Hh3cevtModuleSw_LSXM1CGQ18QGHFR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2162)
)
_Hh3cevtModuleSw_LSXM1SUP04TR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP04TR1 = _Hh3cevtModuleSw_LSXM1SUP04TR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2163)
)
_Hh3cevtModuleSw_LSXM1CGQ36HBR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36HBR1 = _Hh3cevtModuleSw_LSXM1CGQ36HBR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2164)
)
_Hh3cevtModuleSw_LSXM1CGQ36HFR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36HFR1 = _Hh3cevtModuleSw_LSXM1CGQ36HFR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2165)
)
_Hh3cevtModuleSw_LSXM1CGQ6QGHFR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ6QGHFR1 = _Hh3cevtModuleSw_LSXM1CGQ6QGHFR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2166)
)
_Hh3cevtModuleSw_LSXM1TGS48HBR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48HBR1 = _Hh3cevtModuleSw_LSXM1TGS48HBR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2167)
)
_Hh3cevtModuleSw_LSXM1CGQ18QGHBR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18QGHBR1 = _Hh3cevtModuleSw_LSXM1CGQ18QGHBR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2168)
)
_Hh3cevtModuleSw_LSXM1SUPER1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPER1 = _Hh3cevtModuleSw_LSXM1SUPER1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2169)
)
_Hh3cevtModuleSw_LSQM1SDNB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1SDNB0 = _Hh3cevtModuleSw_LSQM1SDNB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2170)
)
_Hh3cevtModuleSw_LSUM1SDNB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1SDNB0 = _Hh3cevtModuleSw_LSUM1SDNB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2171)
)
_Hh3cevtModuleSw_LSQM1EPSB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1EPSB0 = _Hh3cevtModuleSw_LSQM1EPSB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2172)
)
_Hh3cevtModuleSw_LSUM1EPSB0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1EPSB0 = _Hh3cevtModuleSw_LSUM1EPSB0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2173)
)
_Hh3cevtModuleSw_LSXM2TGS48HB2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2TGS48HB2 = _Hh3cevtModuleSw_LSXM2TGS48HB2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2174)
)
_Hh3cevtModuleSw_LSXM2CGQ18QGHB2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2CGQ18QGHB2 = _Hh3cevtModuleSw_LSXM2CGQ18QGHB2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2175)
)
_Hh3cevtModuleSw_LSUM1CGS8SH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS8SH3 = _Hh3cevtModuleSw_LSUM1CGS8SH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2176)
)
_Hh3cevtModuleSw_LSUM1GT48FC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GT48FC3 = _Hh3cevtModuleSw_LSUM1GT48FC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2177)
)
_Hh3cevtModuleSw_LSUM1FAB10XEA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10XEA3 = _Hh3cevtModuleSw_LSUM1FAB10XEA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2178)
)
_Hh3cevtModuleSw_LSUM1TGS48SH3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS48SH3 = _Hh3cevtModuleSw_LSUM1TGS48SH3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2179)
)
_Hh3cevtModuleSw_LSUM1MPUS10XE3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS10XE3 = _Hh3cevtModuleSw_LSUM1MPUS10XE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2180)
)
_Hh3cevtModuleSw_LSUM1GP48FC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GP48FC3 = _Hh3cevtModuleSw_LSUM1GP48FC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2181)
)
_Hh3cevtModuleSw_LSQM1TGS16FD0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1TGS16FD0_Z = _Hh3cevtModuleSw_LSQM1TGS16FD0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2182)
)
_Hh3cevtModuleSw_LSQM2SUPA0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2SUPA0_Z = _Hh3cevtModuleSw_LSQM2SUPA0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2183)
)
_Hh3cevtModuleSw_LSUM1TGS16FD0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS16FD0_Z = _Hh3cevtModuleSw_LSUM1TGS16FD0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2184)
)
_Hh3cevtModuleSw_LSWM2FPGAB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2FPGAB = _Hh3cevtModuleSw_LSWM2FPGAB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2185)
)
_Hh3cevtModuleSw_LSWM2EC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2EC = _Hh3cevtModuleSw_LSWM2EC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2186)
)
_Hh3cevtModuleSw_LSWM2FPGA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2FPGA = _Hh3cevtModuleSw_LSWM2FPGA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2187)
)
_Hh3cevtModuleSw_LSWM2ZSP4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2ZSP4P = _Hh3cevtModuleSw_LSWM2ZSP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2188)
)
_Hh3cevtModuleSw_LSXM1CGQ8TD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ8TD2 = _Hh3cevtModuleSw_LSXM1CGQ8TD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2189)
)
_Hh3cevtModuleSw_LSXM1TGS48C4TD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48C4TD2 = _Hh3cevtModuleSw_LSXM1TGS48C4TD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2190)
)
_Hh3cevtModuleSw_LSXM1QGS24C6TD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS24C6TD2 = _Hh3cevtModuleSw_LSXM1QGS24C6TD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2191)
)
_Hh3cevtModuleSw_LSCM1MPUS06A8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1MPUS06A8 = _Hh3cevtModuleSw_LSCM1MPUS06A8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2192)
)
_Hh3cevtModuleSw_LSCM1TGS48SC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM1TGS48SC8 = _Hh3cevtModuleSw_LSCM1TGS48SC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2193)
)
_Hh3cevtModuleSw_LSQM1MPUS06S0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1MPUS06S0 = _Hh3cevtModuleSw_LSQM1MPUS06S0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2194)
)
_Hh3cevtModuleSw_LSQM1SRP4Y06A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM1SRP4Y06A0 = _Hh3cevtModuleSw_LSQM1SRP4Y06A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2195)
)
_Hh3cevtModuleSw_S76_16XFSF_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S76_16XFSF_E = _Hh3cevtModuleSw_S76_16XFSF_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2196)
)
_Hh3cevtModuleSw_S7603_MPU_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_S7603_MPU = _Hh3cevtModuleSw_S7603_MPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2197)
)
_Hh3cevtModuleSw_LSCM2MPUS06AS8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2MPUS06AS8 = _Hh3cevtModuleSw_LSCM2MPUS06AS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2198)
)
_Hh3cevtModuleSw_LSCM2CGT24TSSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CGT24TSSC8 = _Hh3cevtModuleSw_LSCM2CGT24TSSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2199)
)
_Hh3cevtModuleSw_LSCM2CGP24TSSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CGP24TSSC8 = _Hh3cevtModuleSw_LSCM2CGP24TSSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2200)
)
_Hh3cevtModuleSw_LSCM2CTGS12GTSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CTGS12GTSC8 = _Hh3cevtModuleSw_LSCM2CTGS12GTSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2201)
)
_Hh3cevtModuleSw_LSCM2CTGS12GPSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CTGS12GPSC8 = _Hh3cevtModuleSw_LSCM2CTGS12GPSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2202)
)
_Hh3cevtModuleSw_LSCM2GT24GPTSSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GT24GPTSSC8 = _Hh3cevtModuleSw_LSCM2GT24GPTSSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2203)
)
_Hh3cevtModuleSw_LSCM2GT24GPSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GT24GPSC8 = _Hh3cevtModuleSw_LSCM2GT24GPSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2204)
)
_Hh3cevtModuleSw_LSCM2GP24GTSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GP24GTSC8 = _Hh3cevtModuleSw_LSCM2GP24GTSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2205)
)
_Hh3cevtModuleSw_LSCM2GT48SC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GT48SC8 = _Hh3cevtModuleSw_LSCM2GT48SC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2206)
)
_Hh3cevtModuleSw_LSCM2GP48SC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GP48SC8 = _Hh3cevtModuleSw_LSCM2GP48SC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2207)
)
_Hh3cevtModuleSw_LSCM2TGS16GPSC8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2TGS16GPSC8 = _Hh3cevtModuleSw_LSCM2TGS16GPSC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2208)
)
_Hh3cevtModuleSw_LSXM2SFH16CR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM2SFH16CR1 = _Hh3cevtModuleSw_LSXM2SFH16CR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2209)
)
_Hh3cevtModuleSw_LSXM1SEERBXC2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SEERBXC2 = _Hh3cevtModuleSw_LSXM1SEERBXC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2210)
)
_Hh3cevtModuleSw_LSXM1SEERBG2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SEERBG2 = _Hh3cevtModuleSw_LSXM1SEERBG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2211)
)
_Hh3cevtModuleSw_LSXM1SEERBXD2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SEERBXD2 = _Hh3cevtModuleSw_LSXM1SEERBXD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2212)
)
_Hh3cevtModuleSw_LSXM1SFK08FR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFK08FR1 = _Hh3cevtModuleSw_LSXM1SFK08FR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2213)
)
_Hh3cevtModuleSw_LSXM1CDQ24KBR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CDQ24KBR1 = _Hh3cevtModuleSw_LSXM1CDQ24KBR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2214)
)
_Hh3cevtModuleSw_LSXM1SUP02LR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP02LR1 = _Hh3cevtModuleSw_LSXM1SUP02LR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2215)
)
_Hh3cevtModuleSw_LSXM1CGQ48KBR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ48KBR1 = _Hh3cevtModuleSw_LSXM1CGQ48KBR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2216)
)
_Hh3cevtModuleSw_LSXM1CGQ36HC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36HC0 = _Hh3cevtModuleSw_LSXM1CGQ36HC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2217)
)
_Hh3cevtModuleSw_LSXM1TGS48TE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48TE2 = _Hh3cevtModuleSw_LSXM1TGS48TE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2218)
)
_Hh3cevtModuleSw_LSXM1CGQ36TE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ36TE2 = _Hh3cevtModuleSw_LSXM1CGQ36TE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2219)
)
_Hh3cevtModuleSw_LSXM1SFT16F1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFT16F1 = _Hh3cevtModuleSw_LSXM1SFT16F1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2220)
)
_Hh3cevtModuleSw_LSXM1CGQ18TE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18TE2 = _Hh3cevtModuleSw_LSXM1CGQ18TE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2221)
)
_Hh3cevtModuleSw_LSXM1CGQ8TE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ8TE2 = _Hh3cevtModuleSw_LSXM1CGQ8TE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2222)
)
_Hh3cevtModuleSw_LSWM116H_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM116H = _Hh3cevtModuleSw_LSWM116H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2223)
)
_Hh3cevtModuleSw_LSWM1M4CD_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM1M4CD = _Hh3cevtModuleSw_LSWM1M4CD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2224)
)
_Hh3cevtModuleSw_LSXM1QGS36TE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1QGS36TE2 = _Hh3cevtModuleSw_LSXM1QGS36TE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2225)
)
_Hh3cevtModuleSw_LSXM1SFT16F2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFT16F2 = _Hh3cevtModuleSw_LSXM1SFT16F2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2226)
)
_Hh3cevtModuleSw_CSPEX_1812X_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1812X_E = _Hh3cevtModuleSw_CSPEX_1812X_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2227)
)
_Hh3cevtModuleSw_MOD20_A3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MOD20_A3 = _Hh3cevtModuleSw_MOD20_A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2228)
)
_Hh3cevtModuleSw_RP_S_G_A3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RP_S_G_A3 = _Hh3cevtModuleSw_RP_S_G_A3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2229)
)
_Hh3cevtModuleSw_LSXM1SFT16EA1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFT16EA1 = _Hh3cevtModuleSw_LSXM1SFT16EA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2230)
)
_Hh3cevtModuleSw_RP1_S_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RP1_S_G = _Hh3cevtModuleSw_RP1_S_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2231)
)
_Hh3cevtModuleSw_MOD21_G_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MOD21_G = _Hh3cevtModuleSw_MOD21_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2232)
)
_Hh3cevtModuleSw_LSXM1SUPKR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPKR1 = _Hh3cevtModuleSw_LSXM1SUPKR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2233)
)
_Hh3cevtModuleSw_LSXM1CDQ36KBR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CDQ36KBR1 = _Hh3cevtModuleSw_LSXM1CDQ36KBR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2234)
)
_Hh3cevtModuleSw_LSXM1CMUR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CMUR1 = _Hh3cevtModuleSw_LSXM1CMUR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2235)
)
_Hh3cevtModuleSw_LSXM1SFK16GR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFK16GR1 = _Hh3cevtModuleSw_LSXM1SFK16GR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2236)
)
_Hh3cevtModuleSw_CSR05SRP1R3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR05SRP1R3 = _Hh3cevtModuleSw_CSR05SRP1R3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2237)
)
_Hh3cevtModuleSw_MIC_TCP8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_TCP8L = _Hh3cevtModuleSw_MIC_TCP8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2238)
)
_Hh3cevtModuleSw_MIC_PSP4L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_PSP4L = _Hh3cevtModuleSw_MIC_PSP4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2239)
)
_Hh3cevtModuleSw_LSUM1MPU06B8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPU06B8 = _Hh3cevtModuleSw_LSUM1MPU06B8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2240)
)
_Hh3cevtModuleSw_LSUM1MPU10C8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPU10C8 = _Hh3cevtModuleSw_LSUM1MPU10C8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2241)
)
_Hh3cevtModuleSw_LSUM1FAB06C8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB06C8 = _Hh3cevtModuleSw_LSUM1FAB06C8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2242)
)
_Hh3cevtModuleSw_LSUM1FAB10C8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10C8 = _Hh3cevtModuleSw_LSUM1FAB10C8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2243)
)
_Hh3cevtModuleSw_LSUM1MPU10A8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPU10A8 = _Hh3cevtModuleSw_LSUM1MPU10A8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2244)
)
_Hh3cevtModuleSw_LSUM1FAB10A8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10A8 = _Hh3cevtModuleSw_LSUM1FAB10A8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2245)
)
_Hh3cevtModuleSw_LSUM1TGS16FD8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS16FD8 = _Hh3cevtModuleSw_LSUM1TGS16FD8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2246)
)
_Hh3cevtModuleSw_LSUM1GP48FD8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GP48FD8 = _Hh3cevtModuleSw_LSUM1GP48FD8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2247)
)
_Hh3cevtModuleSw_LSUM1GT48FD8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GT48FD8 = _Hh3cevtModuleSw_LSUM1GT48FD8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2248)
)
_Hh3cevtModuleSw_LSUM1GP40TS8FD8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1GP40TS8FD8 = _Hh3cevtModuleSw_LSUM1GP40TS8FD8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2249)
)
_Hh3cevtModuleSw_LSUM1TGS48RSH8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS48RSH8 = _Hh3cevtModuleSw_LSUM1TGS48RSH8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2250)
)
_Hh3cevtModuleSw_LSDM1GP48SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1GP48SE0_Z = _Hh3cevtModuleSw_LSDM1GP48SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2251)
)
_Hh3cevtModuleSw_LSDM1GT48SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1GT48SE0_Z = _Hh3cevtModuleSw_LSDM1GT48SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2252)
)
_Hh3cevtModuleSw_LSDM1CGS8SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1CGS8SE0_Z = _Hh3cevtModuleSw_LSDM1CGS8SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2253)
)
_Hh3cevtModuleSw_LSXM1SUP04T2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP04T2 = _Hh3cevtModuleSw_LSXM1SUP04T2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2254)
)
_Hh3cevtModuleSw_LSXM1SFT04F2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFT04F2 = _Hh3cevtModuleSw_LSXM1SFT04F2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2255)
)
_Hh3cevtModuleSw_LSXM1SFT08F2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFT08F2 = _Hh3cevtModuleSw_LSXM1SFT08F2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2256)
)
_Hh3cevtModuleSw_RX_NIC_CQ2LF_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_CQ2LF_E = _Hh3cevtModuleSw_RX_NIC_CQ2LF_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2257)
)
_Hh3cevtModuleSw_LSUM1TGS24FD8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1TGS24FD8 = _Hh3cevtModuleSw_LSUM1TGS24FD8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2258)
)
_Hh3cevtModuleSw_RX_SPE400_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SPE400_E = _Hh3cevtModuleSw_RX_SPE400_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2259)
)
_Hh3cevtModuleSw_LSXM1SFK08GR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFK08GR1 = _Hh3cevtModuleSw_LSXM1SFK08GR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2260)
)
_Hh3cevtModuleSw_RX_SFC_16T1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SFC_16T1 = _Hh3cevtModuleSw_RX_SFC_16T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2261)
)
_Hh3cevtModuleSw_LSCM3SUP03A0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3SUP03A0_Z = _Hh3cevtModuleSw_LSCM3SUP03A0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2262)
)
_Hh3cevtModuleSw_LSCM3MPUS06A0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3MPUS06A0_Z = _Hh3cevtModuleSw_LSCM3MPUS06A0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2263)
)
_Hh3cevtModuleSw_LSCM3GT48SC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3GT48SC0_Z = _Hh3cevtModuleSw_LSCM3GT48SC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2264)
)
_Hh3cevtModuleSw_LSCM3TGS48SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3TGS48SE0_Z = _Hh3cevtModuleSw_LSCM3TGS48SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2265)
)
_Hh3cevtModuleSw_LSCM3QGS8CSSE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3QGS8CSSE0_Z = _Hh3cevtModuleSw_LSCM3QGS8CSSE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2266)
)
_Hh3cevtModuleSw_LSDM3QGS12SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3QGS12SE0_Z = _Hh3cevtModuleSw_LSDM3QGS12SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2267)
)
_Hh3cevtModuleSw_LSDM3TGS48SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3TGS48SE0_Z = _Hh3cevtModuleSw_LSDM3TGS48SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2268)
)
_Hh3cevtModuleSw_LSDM3SUPA0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3SUPA0_Z = _Hh3cevtModuleSw_LSDM3SUPA0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2269)
)
_Hh3cevtModuleSw_LSDM3FAB08D0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3FAB08D0_Z = _Hh3cevtModuleSw_LSDM3FAB08D0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2270)
)
_Hh3cevtModuleSw_LSDM3GT24GPSE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3GT24GPSE0_Z = _Hh3cevtModuleSw_LSDM3GT24GPSE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2271)
)
_Hh3cevtModuleSw_LSDM3GP48SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3GP48SE0_Z = _Hh3cevtModuleSw_LSDM3GP48SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2272)
)
_Hh3cevtModuleSw_LSDM3GT48SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3GT48SE0_Z = _Hh3cevtModuleSw_LSDM3GT48SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2273)
)
_Hh3cevtModuleSw_LSDM3CGS8SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3CGS8SE0_Z = _Hh3cevtModuleSw_LSDM3CGS8SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2274)
)
_Hh3cevtModuleSw_RX_CEPC_CQ8LF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_CEPC_CQ8LF = _Hh3cevtModuleSw_RX_CEPC_CQ8LF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2275)
)
_Hh3cevtModuleSw_RX_SPE200_E_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_SPE200_E = _Hh3cevtModuleSw_RX_SPE200_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2276)
)
_Hh3cevtModuleSw_DSH7503_MP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7503_MP = _Hh3cevtModuleSw_DSH7503_MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2277)
)
_Hh3cevtModuleSw_DSH7506_MP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7506_MP = _Hh3cevtModuleSw_DSH7506_MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2278)
)
_Hh3cevtModuleSw_DSH7510_MP_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7510_MP = _Hh3cevtModuleSw_DSH7510_MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2279)
)
_Hh3cevtModuleSw_DSH7500_48T_P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_48T_P = _Hh3cevtModuleSw_DSH7500_48T_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2280)
)
_Hh3cevtModuleSw_DSH7500_16X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_16X = _Hh3cevtModuleSw_DSH7500_16X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2281)
)
_Hh3cevtModuleSw_DSH7500_48F_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_48F = _Hh3cevtModuleSw_DSH7500_48F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2282)
)
_Hh3cevtModuleSw_DSH7500_12QX4Q28_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_12QX4Q28 = _Hh3cevtModuleSw_DSH7500_12QX4Q28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2283)
)
_Hh3cevtModuleSw_DSH7500_24F4X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_24F4X = _Hh3cevtModuleSw_DSH7500_24F4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2284)
)
_Hh3cevtModuleSw_DSH7500_24QX_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_24QX = _Hh3cevtModuleSw_DSH7500_24QX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2285)
)
_Hh3cevtModuleSw_DSH7500_24T4X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_24T4X = _Hh3cevtModuleSw_DSH7500_24T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2286)
)
_Hh3cevtModuleSw_DSH7500_24X2QX1Q28_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_24X2QX1Q28 = _Hh3cevtModuleSw_DSH7500_24X2QX1Q28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2287)
)
_Hh3cevtModuleSw_DSH7500_2Q28_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_2Q28 = _Hh3cevtModuleSw_DSH7500_2Q28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2288)
)
_Hh3cevtModuleSw_DSH7500_44F4X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_44F4X = _Hh3cevtModuleSw_DSH7500_44F4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2289)
)
_Hh3cevtModuleSw_DSH7500_48T_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_48T = _Hh3cevtModuleSw_DSH7500_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2290)
)
_Hh3cevtModuleSw_DSH7500_48X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_DSH7500_48X = _Hh3cevtModuleSw_DSH7500_48X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2291)
)
_Hh3cevtModuleSw_LSWM2_iMC_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2_iMC = _Hh3cevtModuleSw_LSWM2_iMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2292)
)
_Hh3cevtModuleSw_LSWM2ZQP2P_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2ZQP2P_Z = _Hh3cevtModuleSw_LSWM2ZQP2P_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2293)
)
_Hh3cevtModuleSw_LSWM2ZSP4P_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2ZSP4P_Z = _Hh3cevtModuleSw_LSWM2ZSP4P_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2294)
)
_Hh3cevtModuleSw_LSWM2ZSP8P_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2ZSP8P_Z = _Hh3cevtModuleSw_LSWM2ZSP8P_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2295)
)
_Hh3cevtModuleSw_LSDM3SUP04A0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3SUP04A0_Z = _Hh3cevtModuleSw_LSDM3SUP04A0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2296)
)
_Hh3cevtModuleSw_LSDM3FAB04E0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3FAB04E0_Z = _Hh3cevtModuleSw_LSDM3FAB04E0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2297)
)
_Hh3cevtModuleSw_LSDM3FAB08E0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3FAB08E0_Z = _Hh3cevtModuleSw_LSDM3FAB08E0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2298)
)
_Hh3cevtModuleSw_LSDM3QGS36SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3QGS36SE0_Z = _Hh3cevtModuleSw_LSDM3QGS36SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2299)
)
_Hh3cevtModuleSw_LSDM3CGS12SE0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3CGS12SE0_Z = _Hh3cevtModuleSw_LSDM3CGS12SE0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2300)
)
_Hh3cevtModuleSw_LSQM2XPT12TSFD0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM2XPT12TSFD0 = _Hh3cevtModuleSw_LSQM2XPT12TSFD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2301)
)
_Hh3cevtModuleSw_CSPEX_1702X_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1702X = _Hh3cevtModuleSw_CSPEX_1702X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2302)
)
_Hh3cevtModuleSw_CSR05SRP1P1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR05SRP1P1 = _Hh3cevtModuleSw_CSR05SRP1P1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2303)
)
_Hh3cevtModuleSw_NIC_GP24L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_GP24L1 = _Hh3cevtModuleSw_NIC_GP24L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2304)
)
_Hh3cevtModuleSw_NIC_GP24LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_GP24LA = _Hh3cevtModuleSw_NIC_GP24LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2305)
)
_Hh3cevtModuleSw_NIC_XP20L1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_XP20L1 = _Hh3cevtModuleSw_NIC_XP20L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2306)
)
_Hh3cevtModuleSw_NIC_XP20LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_XP20LA = _Hh3cevtModuleSw_NIC_XP20LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2307)
)
_Hh3cevtModuleSw_RX_NIC_LGQ4LF_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_RX_NIC_LGQ4LF = _Hh3cevtModuleSw_RX_NIC_LGQ4LF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2308)
)
_Hh3cevtModuleSw_CSR05SRP1R3A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSR05SRP1R3A = _Hh3cevtModuleSw_CSR05SRP1R3A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2309)
)
_Hh3cevtModuleSw_CEPC_CQ8L_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_CQ8L = _Hh3cevtModuleSw_CEPC_CQ8L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2310)
)
_Hh3cevtModuleSw_CEPC_CQ8LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CEPC_CQ8LA = _Hh3cevtModuleSw_CEPC_CQ8LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2311)
)
_Hh3cevtModuleSw_CSPEX_1802XA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1802XA = _Hh3cevtModuleSw_CSPEX_1802XA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2312)
)
_Hh3cevtModuleSw_CSPEX_1802XB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1802XB = _Hh3cevtModuleSw_CSPEX_1802XB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2313)
)
_Hh3cevtModuleSw_CSPEX_1502XA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1502XA = _Hh3cevtModuleSw_CSPEX_1502XA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2314)
)
_Hh3cevtModuleSw_CSPEX_1512XB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSPEX_1512XB = _Hh3cevtModuleSw_CSPEX_1512XB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2315)
)
_Hh3cevtModuleSw_NIC_XP20L1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_XP20L1A = _Hh3cevtModuleSw_NIC_XP20L1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2317)
)
_Hh3cevtModuleSw_NIC_XP20L1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_XP20L1B = _Hh3cevtModuleSw_NIC_XP20L1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2318)
)
_Hh3cevtModuleSw_NIC_GP24L1A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_GP24L1A = _Hh3cevtModuleSw_NIC_GP24L1A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2320)
)
_Hh3cevtModuleSw_NIC_GP24L1B_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_GP24L1B = _Hh3cevtModuleSw_NIC_GP24L1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2321)
)
_Hh3cevtModuleSw_NIC_CQ2LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_CQ2LA = _Hh3cevtModuleSw_NIC_CQ2LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2322)
)
_Hh3cevtModuleSw_NIC_CQ2LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_CQ2LB = _Hh3cevtModuleSw_NIC_CQ2LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2323)
)
_Hh3cevtModuleSw_NIC_XP5LA_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_XP5LA = _Hh3cevtModuleSw_NIC_XP5LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2324)
)
_Hh3cevtModuleSw_NIC_XP5LB_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_NIC_XP5LB = _Hh3cevtModuleSw_NIC_XP5LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2325)
)
_Hh3cevtModuleSw_CSFC_16T1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_CSFC_16T1 = _Hh3cevtModuleSw_CSFC_16T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2326)
)
_Hh3cevtModuleSw_LSUM1MPUS10XEC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS10XEC0 = _Hh3cevtModuleSw_LSUM1MPUS10XEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2327)
)
_Hh3cevtModuleSw_LSUM1MPUS10XEC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS10XEC3 = _Hh3cevtModuleSw_LSUM1MPUS10XEC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2328)
)
_Hh3cevtModuleSw_LSUM1MPUS06XEC3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1MPUS06XEC3 = _Hh3cevtModuleSw_LSUM1MPUS06XEC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2329)
)
_Hh3cevtModuleSw_LSUM1FAB10XEC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1FAB10XEC0 = _Hh3cevtModuleSw_LSUM1FAB10XEC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2330)
)
_Hh3cevtModuleSw_LSCM2MPUS06AS0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2MPUS06AS0_Z = _Hh3cevtModuleSw_LSCM2MPUS06AS0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2331)
)
_Hh3cevtModuleSw_LSCM2CGT24TSSC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CGT24TSSC0_Z = _Hh3cevtModuleSw_LSCM2CGT24TSSC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2332)
)
_Hh3cevtModuleSw_LSCM2CGP24TSSC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CGP24TSSC0_Z = _Hh3cevtModuleSw_LSCM2CGP24TSSC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2333)
)
_Hh3cevtModuleSw_LSCM2CTGS12GTSC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CTGS12GTSC0_Z = _Hh3cevtModuleSw_LSCM2CTGS12GTSC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2334)
)
_Hh3cevtModuleSw_LSCM2CTGS12GPSC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CTGS12GPSC0_Z = _Hh3cevtModuleSw_LSCM2CTGS12GPSC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2335)
)
_Hh3cevtModuleSw_LSCM2GT24GPTSSC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GT24GPTSSC0_Z = _Hh3cevtModuleSw_LSCM2GT24GPTSSC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2336)
)
_Hh3cevtModuleSw_LSCM2GT24GPSC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GT24GPSC0_Z = _Hh3cevtModuleSw_LSCM2GT24GPSC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2337)
)
_Hh3cevtModuleSw_LSCM2GP24GTSC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GP24GTSC0_Z = _Hh3cevtModuleSw_LSCM2GP24GTSC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2338)
)
_Hh3cevtModuleSw_LSCM2GT48SC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GT48SC0_Z = _Hh3cevtModuleSw_LSCM2GT48SC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2339)
)
_Hh3cevtModuleSw_LSCM2GP48SC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GP48SC0_Z = _Hh3cevtModuleSw_LSCM2GP48SC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2340)
)
_Hh3cevtModuleSw_LSCM2TGS16GPSC0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2TGS16GPSC0_Z = _Hh3cevtModuleSw_LSCM2TGS16GPSC0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2341)
)
_Hh3cevtModuleSw_LSWM2SP2PM_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP2PM_Z = _Hh3cevtModuleSw_LSWM2SP2PM_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2342)
)
_Hh3cevtModuleSw_LSWM2QP2P_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2QP2P_Z = _Hh3cevtModuleSw_LSWM2QP2P_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2343)
)
_Hh3cevtModuleSw_LSWM2SP8P_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2SP8P_Z = _Hh3cevtModuleSw_LSWM2SP8P_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2344)
)
_Hh3cevtModuleSw_LSCM2MPUS06AS0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2MPUS06AS0 = _Hh3cevtModuleSw_LSCM2MPUS06AS0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2345)
)
_Hh3cevtModuleSw_LSCM2CGT24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CGT24TSSC0 = _Hh3cevtModuleSw_LSCM2CGT24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2346)
)
_Hh3cevtModuleSw_LSCM2CGP24TSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CGP24TSSC0 = _Hh3cevtModuleSw_LSCM2CGP24TSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2347)
)
_Hh3cevtModuleSw_LSCM2CTGS12GTSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CTGS12GTSC0 = _Hh3cevtModuleSw_LSCM2CTGS12GTSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2348)
)
_Hh3cevtModuleSw_LSCM2CTGS12GPSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2CTGS12GPSC0 = _Hh3cevtModuleSw_LSCM2CTGS12GPSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2349)
)
_Hh3cevtModuleSw_LSCM2GT24GPTSSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GT24GPTSSC0 = _Hh3cevtModuleSw_LSCM2GT24GPTSSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2350)
)
_Hh3cevtModuleSw_LSCM2GT24GPSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GT24GPSC0 = _Hh3cevtModuleSw_LSCM2GT24GPSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2351)
)
_Hh3cevtModuleSw_LSCM2GP24GTSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GP24GTSC0 = _Hh3cevtModuleSw_LSCM2GP24GTSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2352)
)
_Hh3cevtModuleSw_LSCM2GT48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GT48SC0 = _Hh3cevtModuleSw_LSCM2GT48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2353)
)
_Hh3cevtModuleSw_LSCM2GP48SC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2GP48SC0 = _Hh3cevtModuleSw_LSCM2GP48SC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2354)
)
_Hh3cevtModuleSw_LSCM2TGS16GPSC0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2TGS16GPSC0 = _Hh3cevtModuleSw_LSCM2TGS16GPSC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2355)
)
_Hh3cevtModuleSw_LSXM1SFK04FR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFK04FR1 = _Hh3cevtModuleSw_LSXM1SFK04FR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2356)
)
_Hh3cevtModuleSw_LSXM1SFK08ER1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFK08ER1 = _Hh3cevtModuleSw_LSXM1SFK08ER1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2357)
)
_Hh3cevtModuleSw_LSXM1SFK16ER1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFK16ER1 = _Hh3cevtModuleSw_LSXM1SFK16ER1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2358)
)
_Hh3cevtModuleSw_LSXM1CCQ48KBR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CCQ48KBR1 = _Hh3cevtModuleSw_LSXM1CCQ48KBR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2359)
)
_Hh3cevtModuleSw_LSQM3SUPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM3SUPA0 = _Hh3cevtModuleSw_LSQM3SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2360)
)
_Hh3cevtModuleSw_LSQM3SUPA3_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSQM3SUPA3 = _Hh3cevtModuleSw_LSQM3SUPA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2361)
)
_Hh3cevtModuleSw_LSXM1YGS24CGMODTE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1YGS24CGMODTE2 = _Hh3cevtModuleSw_LSXM1YGS24CGMODTE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2362)
)
_Hh3cevtModuleSw_LSXM1SUPE1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPE1 = _Hh3cevtModuleSw_LSXM1SUPE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2363)
)
_Hh3cevtModuleSw_LSUM2TGS48SH0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM2TGS48SH0 = _Hh3cevtModuleSw_LSUM2TGS48SH0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2364)
)
_Hh3cevtModuleSw_LSCM3SUP03A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3SUP03A0 = _Hh3cevtModuleSw_LSCM3SUP03A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2365)
)
_Hh3cevtModuleSw_LSCM3MPUS06A0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3MPUS06A0 = _Hh3cevtModuleSw_LSCM3MPUS06A0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2366)
)
_Hh3cevtModuleSw_LSCM3TGS48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3TGS48SE0 = _Hh3cevtModuleSw_LSCM3TGS48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2367)
)
_Hh3cevtModuleSw_LSCM3QGS8CSSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3QGS8CSSE0 = _Hh3cevtModuleSw_LSCM3QGS8CSSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2368)
)
_Hh3cevtModuleSw_LSCM3SUP03A0_ZE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3SUP03A0_ZE = _Hh3cevtModuleSw_LSCM3SUP03A0_ZE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2369)
)
_Hh3cevtModuleSw_LSCM3GT48SC0_ZE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3GT48SC0_ZE = _Hh3cevtModuleSw_LSCM3GT48SC0_ZE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2370)
)
_Hh3cevtModuleSw_LSCM3TGS48SE0_ZE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3TGS48SE0_ZE = _Hh3cevtModuleSw_LSCM3TGS48SE0_ZE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2371)
)
_Hh3cevtModuleSw_LSCM3QGS8CSSE0_ZE_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3QGS8CSSE0_ZE = _Hh3cevtModuleSw_LSCM3QGS8CSSE0_ZE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2372)
)
_Hh3cevtModuleSw_LSDM3FAB04G0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3FAB04G0_Z = _Hh3cevtModuleSw_LSDM3FAB04G0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2373)
)
_Hh3cevtModuleSw_LSDM3FAB08G0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3FAB08G0_Z = _Hh3cevtModuleSw_LSDM3FAB08G0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2374)
)
_Hh3cevtModuleSw_LSDM3FAB16G0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3FAB16G0_Z = _Hh3cevtModuleSw_LSDM3FAB16G0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2375)
)
_Hh3cevtModuleSw_LSDM3CGS36SF0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3CGS36SF0_Z = _Hh3cevtModuleSw_LSDM3CGS36SF0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2376)
)
_Hh3cevtModuleSw_LSDM3YGS48SF0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3YGS48SF0_Z = _Hh3cevtModuleSw_LSDM3YGS48SF0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2377)
)
_Hh3cevtModuleSw_LSCM3MPUS10B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3MPUS10B0 = _Hh3cevtModuleSw_LSCM3MPUS10B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2378)
)
_Hh3cevtModuleSw_LSCM3MPUS10B0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM3MPUS10B0_Z = _Hh3cevtModuleSw_LSCM3MPUS10B0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2379)
)
_Hh3cevtModuleSw_LSUM1CGS8QSSH8_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSUM1CGS8QSSH8 = _Hh3cevtModuleSw_LSUM1CGS8QSSH8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2380)
)
_Hh3cevtModuleSw_LSDM3TGS48SF0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3TGS48SF0_Z = _Hh3cevtModuleSw_LSDM3TGS48SF0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2381)
)
_Hh3cevtModuleSw_LSDM1SUPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1SUPA0 = _Hh3cevtModuleSw_LSDM1SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2382)
)
_Hh3cevtModuleSw_LSDM1FAB08D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1FAB08D0 = _Hh3cevtModuleSw_LSDM1FAB08D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2383)
)
_Hh3cevtModuleSw_LSDM1TGS48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1TGS48SE0 = _Hh3cevtModuleSw_LSDM1TGS48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2384)
)
_Hh3cevtModuleSw_LSDM1GT24GPSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1GT24GPSE0 = _Hh3cevtModuleSw_LSDM1GT24GPSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2385)
)
_Hh3cevtModuleSw_LSDM1GT48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1GT48SE0 = _Hh3cevtModuleSw_LSDM1GT48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2386)
)
_Hh3cevtModuleSw_LSDM1GP48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM1GP48SE0 = _Hh3cevtModuleSw_LSDM1GP48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2387)
)
_Hh3cevtModuleSw_LSDM3SUPA0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3SUPA0 = _Hh3cevtModuleSw_LSDM3SUPA0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2388)
)
_Hh3cevtModuleSw_LSDM3FAB08D0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3FAB08D0 = _Hh3cevtModuleSw_LSDM3FAB08D0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2389)
)
_Hh3cevtModuleSw_LSDM3TGS48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3TGS48SE0 = _Hh3cevtModuleSw_LSDM3TGS48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2390)
)
_Hh3cevtModuleSw_LSDM3GT24GPSE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3GT24GPSE0 = _Hh3cevtModuleSw_LSDM3GT24GPSE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2391)
)
_Hh3cevtModuleSw_LSDM3GT48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3GT48SE0 = _Hh3cevtModuleSw_LSDM3GT48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2392)
)
_Hh3cevtModuleSw_LSDM3GP48SE0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSDM3GP48SE0 = _Hh3cevtModuleSw_LSDM3GP48SE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2393)
)
_Hh3cevtModuleSw_SR07MPUA3_M_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SR07MPUA3_M = _Hh3cevtModuleSw_SR07MPUA3_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2394)
)
_Hh3cevtModuleSw_SFE_A_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_SFE_A = _Hh3cevtModuleSw_SFE_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2395)
)
_Hh3cevtModuleSw_MIC_CQ1L_M_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CQ1L_M = _Hh3cevtModuleSw_MIC_CQ1L_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2396)
)
_Hh3cevtModuleSw_MIC_CQ2L_M_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_MIC_CQ2L_M = _Hh3cevtModuleSw_MIC_CQ2L_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2397)
)
_Hh3cevtModuleSw_LSXM1CGQ18C1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQ18C1 = _Hh3cevtModuleSw_LSXM1CGQ18C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2398)
)
_Hh3cevtModuleSw_LSXM1CGQMS18B1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CGQMS18B1 = _Hh3cevtModuleSw_LSXM1CGQMS18B1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2399)
)
_Hh3cevtModuleSw_LSXM1MOD48KBR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1MOD48KBR1 = _Hh3cevtModuleSw_LSXM1MOD48KBR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2400)
)
_Hh3cevtModuleSw_LSXM1CDQ36KB1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1CDQ36KB1 = _Hh3cevtModuleSw_LSXM1CDQ36KB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2401)
)
_Hh3cevtModuleSw_LSXM1SUP02TR1_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUP02TR1 = _Hh3cevtModuleSw_LSXM1SUP02TR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2402)
)
_Hh3cevtModuleSw_LSCM2SUP03B0_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2SUP03B0 = _Hh3cevtModuleSw_LSCM2SUP03B0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2407)
)
_Hh3cevtModuleSw_LSCM2SUP03B0_Z_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSCM2SUP03B0_Z = _Hh3cevtModuleSw_LSCM2SUP03B0_Z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2408)
)
_Hh3cevtModuleSw_LSWM2QP4P_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSWM2QP4P = _Hh3cevtModuleSw_LSWM2QP4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2409)
)
_Hh3cevtModuleSw_LSXM1SUPS2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SUPS2 = _Hh3cevtModuleSw_LSXM1SUPS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2410)
)
_Hh3cevtModuleSw_LSXM1SFS08D2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1SFS08D2 = _Hh3cevtModuleSw_LSXM1SFS08D2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2411)
)
_Hh3cevtModuleSw_LSXM1TGS48SE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1TGS48SE2 = _Hh3cevtModuleSw_LSXM1TGS48SE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2412)
)
_Hh3cevtModuleSw_LSXM1GT24GPSE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GT24GPSE2 = _Hh3cevtModuleSw_LSXM1GT24GPSE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2413)
)
_Hh3cevtModuleSw_LSXM1GT48SE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GT48SE2 = _Hh3cevtModuleSw_LSXM1GT48SE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2414)
)
_Hh3cevtModuleSw_LSXM1GP48SE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM1GP48SE2 = _Hh3cevtModuleSw_LSXM1GP48SE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2415)
)
_Hh3cevtModuleSw_LSXM3SUPS2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3SUPS2 = _Hh3cevtModuleSw_LSXM3SUPS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2416)
)
_Hh3cevtModuleSw_LSXM3SFS08D2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3SFS08D2 = _Hh3cevtModuleSw_LSXM3SFS08D2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2417)
)
_Hh3cevtModuleSw_LSXM3TGS48SE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3TGS48SE2 = _Hh3cevtModuleSw_LSXM3TGS48SE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2418)
)
_Hh3cevtModuleSw_LSXM3GT24GPSE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3GT24GPSE2 = _Hh3cevtModuleSw_LSXM3GT24GPSE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2419)
)
_Hh3cevtModuleSw_LSXM3GT48SE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3GT48SE2 = _Hh3cevtModuleSw_LSXM3GT48SE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2420)
)
_Hh3cevtModuleSw_LSXM3GP48SE2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3GP48SE2 = _Hh3cevtModuleSw_LSXM3GP48SE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2421)
)
_Hh3cevtModuleSw_LSXM3SUP04S2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3SUP04S2 = _Hh3cevtModuleSw_LSXM3SUP04S2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2422)
)
_Hh3cevtModuleSw_LSXM3SFS04G2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3SFS04G2 = _Hh3cevtModuleSw_LSXM3SFS04G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2423)
)
_Hh3cevtModuleSw_LSXM3SFS08G2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3SFS08G2 = _Hh3cevtModuleSw_LSXM3SFS08G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2424)
)
_Hh3cevtModuleSw_LSXM3SFS16G2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3SFS16G2 = _Hh3cevtModuleSw_LSXM3SFS16G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2425)
)
_Hh3cevtModuleSw_LSXM3CGQ36SF2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3CGQ36SF2 = _Hh3cevtModuleSw_LSXM3CGQ36SF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2426)
)
_Hh3cevtModuleSw_LSXM3YGS48SF2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3YGS48SF2 = _Hh3cevtModuleSw_LSXM3YGS48SF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2427)
)
_Hh3cevtModuleSw_LSXM3TGS48SF2_ObjectIdentity = ObjectIdentity
hh3cevtModuleSw_LSXM3TGS48SF2 = _Hh3cevtModuleSw_LSXM3TGS48SF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 4, 2428)
)
_Hh3cevtSubModuleRouter_ObjectIdentity = ObjectIdentity
hh3cevtSubModuleRouter = _Hh3cevtSubModuleRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 5)
)
_Hh3cevtSubModuleSwitch_ObjectIdentity = ObjectIdentity
hh3cevtSubModuleSwitch = _Hh3cevtSubModuleSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 6)
)
_Hh3cevtModuleCFCard_ObjectIdentity = ObjectIdentity
hh3cevtModuleCFCard = _Hh3cevtModuleCFCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 7)
)
_Hh3cevtModuleSDCard_ObjectIdentity = ObjectIdentity
hh3cevtModuleSDCard = _Hh3cevtModuleSDCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 9, 8)
)
_Hh3cevtPort_ObjectIdentity = ObjectIdentity
hh3cevtPort = _Hh3cevtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10)
)
_Hh3cevtPortUnknownPorts_ObjectIdentity = ObjectIdentity
hh3cevtPortUnknownPorts = _Hh3cevtPortUnknownPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 1)
)
_Hh3cevtPortCommonPorts_ObjectIdentity = ObjectIdentity
hh3cevtPortCommonPorts = _Hh3cevtPortCommonPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 2)
)
_Hh3cevtPortRouterType_ObjectIdentity = ObjectIdentity
hh3cevtPortRouterType = _Hh3cevtPortRouterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3)
)
_Hh3cevtPortRt_Async_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Async = _Hh3cevtPortRt_Async_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 1)
)
_Hh3cevtPortRt_Analogmodem_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Analogmodem = _Hh3cevtPortRt_Analogmodem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 2)
)
_Hh3cevtPortRt_Atm_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Atm = _Hh3cevtPortRt_Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 3)
)
_Hh3cevtPortRt_AtmAdsl_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmAdsl = _Hh3cevtPortRt_AtmAdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 4)
)
_Hh3cevtPortRt_AtmShdsl_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmShdsl = _Hh3cevtPortRt_AtmShdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 5)
)
_Hh3cevtPortRt_AtmE1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmE1 = _Hh3cevtPortRt_AtmE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 6)
)
_Hh3cevtPortRt_AtmT1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmT1 = _Hh3cevtPortRt_AtmT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 7)
)
_Hh3cevtPortRt_AtmE3_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmE3 = _Hh3cevtPortRt_AtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 8)
)
_Hh3cevtPortRt_AtmT3_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmT3 = _Hh3cevtPortRt_AtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 9)
)
_Hh3cevtPortRt_Atm622M_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Atm622M = _Hh3cevtPortRt_Atm622M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 10)
)
_Hh3cevtPortRt_AtmImaE1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmImaE1 = _Hh3cevtPortRt_AtmImaE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 11)
)
_Hh3cevtPortRt_AtmImaT1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_AtmImaT1 = _Hh3cevtPortRt_AtmImaT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 12)
)
_Hh3cevtPortRt_Atm25M_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Atm25M = _Hh3cevtPortRt_Atm25M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 13)
)
_Hh3cevtPortRt_Bri_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Bri = _Hh3cevtPortRt_Bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 14)
)
_Hh3cevtPortRt_Console_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Console = _Hh3cevtPortRt_Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 15)
)
_Hh3cevtPortRt_E1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_E1 = _Hh3cevtPortRt_E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 16)
)
_Hh3cevtPortRt_E3_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_E3 = _Hh3cevtPortRt_E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 17)
)
_Hh3cevtPortRt_T1_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_T1 = _Hh3cevtPortRt_T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 18)
)
_Hh3cevtPortRt_T3_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_T3 = _Hh3cevtPortRt_T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 19)
)
_Hh3cevtPortRt_Cpos_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Cpos = _Hh3cevtPortRt_Cpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 20)
)
_Hh3cevtPortRt_Ethernet_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Ethernet = _Hh3cevtPortRt_Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 21)
)
_Hh3cevtPortRt_Serial_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Serial = _Hh3cevtPortRt_Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 22)
)
_Hh3cevtPortRt_E1f_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_E1f = _Hh3cevtPortRt_E1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 23)
)
_Hh3cevtPortRt_T1f_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_T1f = _Hh3cevtPortRt_T1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 24)
)
_Hh3cevtPortRt_Pos_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Pos = _Hh3cevtPortRt_Pos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 25)
)
_Hh3cevtPortRt_Ge_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Ge = _Hh3cevtPortRt_Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 26)
)
_Hh3cevtPortRt_Aux_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Aux = _Hh3cevtPortRt_Aux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 27)
)
_Hh3cevtPortRt_VG_Fxs_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VG_Fxs = _Hh3cevtPortRt_VG_Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 30)
)
_Hh3cevtPortRt_VG_Fxo_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VG_Fxo = _Hh3cevtPortRt_VG_Fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 31)
)
_Hh3cevtPortRt_VG_E1vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VG_E1vi = _Hh3cevtPortRt_VG_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 32)
)
_Hh3cevtPortRt_VG_T1vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VG_T1vi = _Hh3cevtPortRt_VG_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 33)
)
_Hh3cevtPortRt_Usb_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Usb = _Hh3cevtPortRt_Usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 34)
)
_Hh3cevtPortRt_Ndec_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Ndec = _Hh3cevtPortRt_Ndec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 35)
)
_Hh3cevtPortRt_Cavium_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Cavium = _Hh3cevtPortRt_Cavium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 36)
)
_Hh3cevtPortRt_Fcm_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Fcm = _Hh3cevtPortRt_Fcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 37)
)
_Hh3cevtPortRt_E1vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_E1vi = _Hh3cevtPortRt_E1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 38)
)
_Hh3cevtPortRt_T1vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_T1vi = _Hh3cevtPortRt_T1vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 39)
)
_Hh3cevtPortRt_Vi_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Vi = _Hh3cevtPortRt_Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 40)
)
_Hh3cevtPortRt_Adls2Plus_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Adls2Plus = _Hh3cevtPortRt_Adls2Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 41)
)
_Hh3cevtPortRt_RADIO_AG_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_RADIO_AG = _Hh3cevtPortRt_RADIO_AG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 42)
)
_Hh3cevtPortRt_1exp_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_1exp = _Hh3cevtPortRt_1exp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 43)
)
_Hh3cevtPortRt_G_SHDSL_BIS_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_G_SHDSL_BIS = _Hh3cevtPortRt_G_SHDSL_BIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 44)
)
_Hh3cevtPortRt_ONU_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_ONU_1000BASE_BX_SFF_SC = _Hh3cevtPortRt_ONU_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 45)
)
_Hh3cevtPortRt_CELLULAR_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_CELLULAR = _Hh3cevtPortRt_CELLULAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 46)
)
_Hh3cevtPortRt_CELLULAR_ETHERNET_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_CELLULAR_ETHERNET = _Hh3cevtPortRt_CELLULAR_ETHERNET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 47)
)
_Hh3cevtPortRt_VGe_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VGe = _Hh3cevtPortRt_VGe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 48)
)
_Hh3cevtPortRt_VXGe_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VXGe = _Hh3cevtPortRt_VXGe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 49)
)
_Hh3cevtPortRt_Xpos_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Xpos = _Hh3cevtPortRt_Xpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 50)
)
_Hh3cevtPortRt_Fge_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Fge = _Hh3cevtPortRt_Fge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 51)
)
_Hh3cevtPortRt_XGe_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_XGe = _Hh3cevtPortRt_XGe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 52)
)
_Hh3cevtPortRt_HgeQsfp28Lc_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_HgeQsfp28Lc = _Hh3cevtPortRt_HgeQsfp28Lc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 53)
)
_Hh3cevtPortRt_HgeCfp2Lc_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_HgeCfp2Lc = _Hh3cevtPortRt_HgeCfp2Lc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 54)
)
_Hh3cevtPortRt_HgeCfpLc_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_HgeCfpLc = _Hh3cevtPortRt_HgeCfpLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 55)
)
_Hh3cevtPortRt_GeM12_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_GeM12 = _Hh3cevtPortRt_GeM12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 56)
)
_Hh3cevtPortRt_VMEth_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_VMEth = _Hh3cevtPortRt_VMEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 57)
)
_Hh3cevtPortRt_FiberGe_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_FiberGe = _Hh3cevtPortRt_FiberGe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 58)
)
_Hh3cevtPortRt_GeOptic_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_GeOptic = _Hh3cevtPortRt_GeOptic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 59)
)
_Hh3cevtPortRt_25Ge_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_25Ge = _Hh3cevtPortRt_25Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 60)
)
_Hh3cevtPortRt_50Ge_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_50Ge = _Hh3cevtPortRt_50Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 61)
)
_Hh3cevtPortRt_FlexE_50_100G_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_FlexE_50_100G = _Hh3cevtPortRt_FlexE_50_100G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 62)
)
_Hh3cevtPortRt_50_100Ge_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_50_100Ge = _Hh3cevtPortRt_50_100Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 63)
)
_Hh3cevtPortRt_FlexE_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_FlexE = _Hh3cevtPortRt_FlexE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 64)
)
_Hh3cevtPortRt_100Ge_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_100Ge = _Hh3cevtPortRt_100Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 65)
)
_Hh3cevtPortRt_FlexE_50G_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_FlexE_50G = _Hh3cevtPortRt_FlexE_50G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 66)
)
_Hh3cevtPortRt_Async_Phoenix_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_Async_Phoenix = _Hh3cevtPortRt_Async_Phoenix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 67)
)
_Hh3cevtPortRt_FlexE_100G_ObjectIdentity = ObjectIdentity
hh3cevtPortRt_FlexE_100G = _Hh3cevtPortRt_FlexE_100G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 3, 68)
)
_Hh3cevtPortSwitchType_ObjectIdentity = ObjectIdentity
hh3cevtPortSwitchType = _Hh3cevtPortSwitchType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4)
)
_Hh3cevtPortSw_10or100M_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10or100M = _Hh3cevtPortSw_10or100M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 1)
)
_Hh3cevtPortSw_1000BaseLxSm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseLxSm = _Hh3cevtPortSw_1000BaseLxSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 2)
)
_Hh3cevtPortSw_1000BaseSxMm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseSxMm = _Hh3cevtPortSw_1000BaseSxMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 3)
)
_Hh3cevtPortSw_1000BaseTx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseTx = _Hh3cevtPortSw_1000BaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 4)
)
_Hh3cevtPortSw_100MSinglemodeFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MSinglemodeFx = _Hh3cevtPortSw_100MSinglemodeFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 5)
)
_Hh3cevtPortSw_100MMultimodeFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MMultimodeFx = _Hh3cevtPortSw_100MMultimodeFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 6)
)
_Hh3cevtPortSw_100M100BaseTx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100M100BaseTx = _Hh3cevtPortSw_100M100BaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 7)
)
_Hh3cevtPortSw_100MHub_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MHub = _Hh3cevtPortSw_100MHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 8)
)
_Hh3cevtPortSw_Vdsl_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Vdsl = _Hh3cevtPortSw_Vdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 9)
)
_Hh3cevtPortSw_Stack_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Stack = _Hh3cevtPortSw_Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 10)
)
_Hh3cevtPortSw_1000BaseZenithFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseZenithFx = _Hh3cevtPortSw_1000BaseZenithFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 11)
)
_Hh3cevtPortSw_1000BaseLongFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseLongFx = _Hh3cevtPortSw_1000BaseLongFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 12)
)
_Hh3cevtPortSw_Adsl_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Adsl = _Hh3cevtPortSw_Adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 13)
)
_Hh3cevtPortSw_10or100MDb_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10or100MDb = _Hh3cevtPortSw_10or100MDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 14)
)
_Hh3cevtPortSw_10GBaseLrSm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBaseLrSm = _Hh3cevtPortSw_10GBaseLrSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 15)
)
_Hh3cevtPortSw_10GBaseLx4Mm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBaseLx4Mm = _Hh3cevtPortSw_10GBaseLx4Mm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 16)
)
_Hh3cevtPortSw_10GBaseLx4Sm_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBaseLx4Sm = _Hh3cevtPortSw_10GBaseLx4Sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 17)
)
_Hh3cevtPortSw_100MLongFx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MLongFx = _Hh3cevtPortSw_100MLongFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 18)
)
_Hh3cevtPortSw_1000BaseCx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseCx = _Hh3cevtPortSw_1000BaseCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 19)
)
_Hh3cevtPortSw_1000BaseZenithFxLc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseZenithFxLc = _Hh3cevtPortSw_1000BaseZenithFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 20)
)
_Hh3cevtPortSw_1000BaseLongFxLc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BaseLongFxLc = _Hh3cevtPortSw_1000BaseLongFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 21)
)
_Hh3cevtPortSw_100MSmFxSc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MSmFxSc = _Hh3cevtPortSw_100MSmFxSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 22)
)
_Hh3cevtPortSw_100MMmFxSc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MMmFxSc = _Hh3cevtPortSw_100MMmFxSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 23)
)
_Hh3cevtPortSw_100MSmFxLc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MSmFxLc = _Hh3cevtPortSw_100MSmFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 24)
)
_Hh3cevtPortSw_100MMmFxLc_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100MMmFxLc = _Hh3cevtPortSw_100MMmFxLc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 25)
)
_Hh3cevtPortSw_GbicNoConnector_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_GbicNoConnector = _Hh3cevtPortSw_GbicNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 26)
)
_Hh3cevtPortSw_Gbic1000BaseT_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Gbic1000BaseT = _Hh3cevtPortSw_Gbic1000BaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 27)
)
_Hh3cevtPortSw_Gbic1000BaseLx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Gbic1000BaseLx = _Hh3cevtPortSw_Gbic1000BaseLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 28)
)
_Hh3cevtPortSw_Gbic1000BaseSx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Gbic1000BaseSx = _Hh3cevtPortSw_Gbic1000BaseSx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 29)
)
_Hh3cevtPortSw_Gbic1000BaseZx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Gbic1000BaseZx = _Hh3cevtPortSw_Gbic1000BaseZx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 30)
)
_Hh3cevtPortSw_ComboNoConnector_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_ComboNoConnector = _Hh3cevtPortSw_ComboNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 31)
)
_Hh3cevtPortSw_Combo1000BaseLx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseLx = _Hh3cevtPortSw_Combo1000BaseLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 32)
)
_Hh3cevtPortSw_Combo1000BaseLxFiber_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseLxFiber = _Hh3cevtPortSw_Combo1000BaseLxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 33)
)
_Hh3cevtPortSw_Combo1000BaseLxCopper_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseLxCopper = _Hh3cevtPortSw_Combo1000BaseLxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 34)
)
_Hh3cevtPortSw_Combo1000BaseSx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseSx = _Hh3cevtPortSw_Combo1000BaseSx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 35)
)
_Hh3cevtPortSw_Combo1000BaseSxFiber_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseSxFiber = _Hh3cevtPortSw_Combo1000BaseSxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 36)
)
_Hh3cevtPortSw_Combo1000BaseSxCopper_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseSxCopper = _Hh3cevtPortSw_Combo1000BaseSxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 37)
)
_Hh3cevtPortSw_Combo1000BaseZx_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseZx = _Hh3cevtPortSw_Combo1000BaseZx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 38)
)
_Hh3cevtPortSw_Combo1000BaseZxFiber_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseZxFiber = _Hh3cevtPortSw_Combo1000BaseZxFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 39)
)
_Hh3cevtPortSw_Combo1000BaseZxCopper_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_Combo1000BaseZxCopper = _Hh3cevtPortSw_Combo1000BaseZxCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 40)
)
_Hh3cevtPortSw_155PosSxMmf_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155PosSxMmf = _Hh3cevtPortSw_155PosSxMmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 41)
)
_Hh3cevtPortSw_155PosLxSmf_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155PosLxSmf = _Hh3cevtPortSw_155PosLxSmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 42)
)
_Hh3cevtPortSw_1000BASE_T_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_T = _Hh3cevtPortSw_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 43)
)
_Hh3cevtPortSw_1000BASE_SX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_SX_SFP = _Hh3cevtPortSw_1000BASE_SX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 44)
)
_Hh3cevtPortSw_1000BASE_LX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_LX_SFP = _Hh3cevtPortSw_1000BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 45)
)
_Hh3cevtPortSw_1000BASE_T_AN_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_T_AN_SFP = _Hh3cevtPortSw_1000BASE_T_AN_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 46)
)
_Hh3cevtPortSw_10GBASE_LX4_XENPAK_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_LX4_XENPAK = _Hh3cevtPortSw_10GBASE_LX4_XENPAK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 47)
)
_Hh3cevtPortSw_10GBASE_LR_XENPAK_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_LR_XENPAK = _Hh3cevtPortSw_10GBASE_LR_XENPAK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 48)
)
_Hh3cevtPortSw_10GBASE_CX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_CX4 = _Hh3cevtPortSw_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 49)
)
_Hh3cevtPortSw_1000BASE_ZX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_ZX_SFP = _Hh3cevtPortSw_1000BASE_ZX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 50)
)
_Hh3cevtPortSw_1000BASE_MM_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_MM_SFP = _Hh3cevtPortSw_1000BASE_MM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 51)
)
_Hh3cevtPortSw_100BASE_SX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_SX_SFP = _Hh3cevtPortSw_100BASE_SX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 52)
)
_Hh3cevtPortSw_100BASE_LX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_LX_SFP = _Hh3cevtPortSw_100BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 53)
)
_Hh3cevtPortSw_100BASE_T_AN_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_T_AN_SFP = _Hh3cevtPortSw_100BASE_T_AN_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 54)
)
_Hh3cevtPortSw_100BASE_ZX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_ZX_SFP = _Hh3cevtPortSw_100BASE_ZX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 55)
)
_Hh3cevtPortSw_100BASE_MM_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_MM_SFP = _Hh3cevtPortSw_100BASE_MM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 56)
)
_Hh3cevtPortSw_SFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_NO_CONNECTOR = _Hh3cevtPortSw_SFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 57)
)
_Hh3cevtPortSw_SFP_UNKNOWN_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_UNKNOWN_CONNECTOR = _Hh3cevtPortSw_SFP_UNKNOWN_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 58)
)
_Hh3cevtPortSw_POS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_NO_CONNECTOR = _Hh3cevtPortSw_POS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 59)
)
_Hh3cevtPortSw_10G_BASE_SR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_SR = _Hh3cevtPortSw_10G_BASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 60)
)
_Hh3cevtPortSw_10G_BASE_ER_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_ER = _Hh3cevtPortSw_10G_BASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 61)
)
_Hh3cevtPortSw_10G_BASE_LX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_LX4 = _Hh3cevtPortSw_10G_BASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 62)
)
_Hh3cevtPortSw_10G_BASE_SW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_SW = _Hh3cevtPortSw_10G_BASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 63)
)
_Hh3cevtPortSw_10G_BASE_LW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_LW = _Hh3cevtPortSw_10G_BASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 64)
)
_Hh3cevtPortSw_10G_BASE_EW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_EW = _Hh3cevtPortSw_10G_BASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 65)
)
_Hh3cevtPortSw_10G_LR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_LR_SM_LC = _Hh3cevtPortSw_10G_LR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 66)
)
_Hh3cevtPortSw_10G_SR_MM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_SR_MM_LC = _Hh3cevtPortSw_10G_SR_MM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 67)
)
_Hh3cevtPortSw_10G_ER_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_ER_SM_LC = _Hh3cevtPortSw_10G_ER_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 68)
)
_Hh3cevtPortSw_10G_LW_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_LW_SM_LC = _Hh3cevtPortSw_10G_LW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 69)
)
_Hh3cevtPortSw_10G_SW_MM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_SW_MM_LC = _Hh3cevtPortSw_10G_SW_MM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 70)
)
_Hh3cevtPortSw_10G_EW_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_EW_SM_LC = _Hh3cevtPortSw_10G_EW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 71)
)
_Hh3cevtPortSw_100BASE_SM_MTRJ_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_SM_MTRJ = _Hh3cevtPortSw_100BASE_SM_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 72)
)
_Hh3cevtPortSw_100BASE_MM_MTRJ_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_MM_MTRJ = _Hh3cevtPortSw_100BASE_MM_MTRJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 73)
)
_Hh3cevtPortSw_XFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_NO_CONNECTOR = _Hh3cevtPortSw_XFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 74)
)
_Hh3cevtPortSw_XFP_10GBASE_SR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_SR = _Hh3cevtPortSw_XFP_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 75)
)
_Hh3cevtPortSw_XFP_10GBASE_LR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_LR = _Hh3cevtPortSw_XFP_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 76)
)
_Hh3cevtPortSw_XFP_10GBASE_ER_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_ER = _Hh3cevtPortSw_XFP_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 77)
)
_Hh3cevtPortSw_XFP_10GBASE_SW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_SW = _Hh3cevtPortSw_XFP_10GBASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 78)
)
_Hh3cevtPortSw_XFP_10GBASE_LW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_LW = _Hh3cevtPortSw_XFP_10GBASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 79)
)
_Hh3cevtPortSw_XFP_10GBASE_EW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_EW = _Hh3cevtPortSw_XFP_10GBASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 80)
)
_Hh3cevtPortSw_XFP_10GBASE_CX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_CX4 = _Hh3cevtPortSw_XFP_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 81)
)
_Hh3cevtPortSw_XFP_10GBASE_LX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_LX4 = _Hh3cevtPortSw_XFP_10GBASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 82)
)
_Hh3cevtPortSw_XFP_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_UNKNOWN = _Hh3cevtPortSw_XFP_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 83)
)
_Hh3cevtPortSw_XPK_NOCONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_NOCONNECTOR = _Hh3cevtPortSw_XPK_NOCONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 84)
)
_Hh3cevtPortSw_XPK_10GBASE_SR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_SR = _Hh3cevtPortSw_XPK_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 85)
)
_Hh3cevtPortSw_XPK_10GBASE_LR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_LR = _Hh3cevtPortSw_XPK_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 86)
)
_Hh3cevtPortSw_XPK_10GBASE_ER_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_ER = _Hh3cevtPortSw_XPK_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 87)
)
_Hh3cevtPortSw_XPK_10GBASE_SW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_SW = _Hh3cevtPortSw_XPK_10GBASE_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 88)
)
_Hh3cevtPortSw_XPK_10GBASE_LW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_LW = _Hh3cevtPortSw_XPK_10GBASE_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 89)
)
_Hh3cevtPortSw_XPK_10GBASE_EW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_EW = _Hh3cevtPortSw_XPK_10GBASE_EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 90)
)
_Hh3cevtPortSw_XPK_10GBASE_CX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_CX4 = _Hh3cevtPortSw_XPK_10GBASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 91)
)
_Hh3cevtPortSw_XPK_10GBASE_LX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_LX4 = _Hh3cevtPortSw_XPK_10GBASE_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 92)
)
_Hh3cevtPortSw_XPK_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_UNKNOWN = _Hh3cevtPortSw_XPK_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 93)
)
_Hh3cevtPortSw_POS_OC48_SR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_SR_SM_LC = _Hh3cevtPortSw_POS_OC48_SR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 94)
)
_Hh3cevtPortSw_POS_OC48_IR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_IR_SM_LC = _Hh3cevtPortSw_POS_OC48_IR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 95)
)
_Hh3cevtPortSw_POS_OC48_LR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_SM_LC = _Hh3cevtPortSw_POS_OC48_LR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 96)
)
_Hh3cevtPortSw_10G_BASE_CX4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_BASE_CX4 = _Hh3cevtPortSw_10G_BASE_CX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 97)
)
_Hh3cevtPortSw_OLT_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_OLT_1000BASE_BX_SFF_SC = _Hh3cevtPortSw_OLT_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 98)
)
_Hh3cevtPortSw_ONU_1000BASE_BX_SFF_SC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_ONU_1000BASE_BX_SFF_SC = _Hh3cevtPortSw_ONU_1000BASE_BX_SFF_SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 99)
)
_Hh3cevtPortSw_24G_CASCADE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_24G_CASCADE = _Hh3cevtPortSw_24G_CASCADE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 100)
)
_Hh3cevtPortSw_POS_OC3_SR_MM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_SR_MM = _Hh3cevtPortSw_POS_OC3_SR_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 101)
)
_Hh3cevtPortSw_POS_OC3_IR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_IR_SM = _Hh3cevtPortSw_POS_OC3_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 102)
)
_Hh3cevtPortSw_POS_OC3_IR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_IR_1_SM = _Hh3cevtPortSw_POS_OC3_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 103)
)
_Hh3cevtPortSw_POS_OC3_IR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_IR_2_SM = _Hh3cevtPortSw_POS_OC3_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 104)
)
_Hh3cevtPortSw_POS_OC3_LR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_LR_SM = _Hh3cevtPortSw_POS_OC3_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 105)
)
_Hh3cevtPortSw_POS_OC3_LR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_LR_1_SM = _Hh3cevtPortSw_POS_OC3_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 106)
)
_Hh3cevtPortSw_POS_OC3_LR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_LR_2_SM = _Hh3cevtPortSw_POS_OC3_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 107)
)
_Hh3cevtPortSw_POS_OC3_LR_3_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC3_LR_3_SM = _Hh3cevtPortSw_POS_OC3_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 108)
)
_Hh3cevtPortSw_POS_OC12_SR_MM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_SR_MM = _Hh3cevtPortSw_POS_OC12_SR_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 109)
)
_Hh3cevtPortSw_POS_OC12_IR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_IR_SM = _Hh3cevtPortSw_POS_OC12_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 110)
)
_Hh3cevtPortSw_POS_OC12_IR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_IR_1_SM = _Hh3cevtPortSw_POS_OC12_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 111)
)
_Hh3cevtPortSw_POS_OC12_IR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_IR_2_SM = _Hh3cevtPortSw_POS_OC12_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 112)
)
_Hh3cevtPortSw_POS_OC12_LR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_LR_SM = _Hh3cevtPortSw_POS_OC12_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 113)
)
_Hh3cevtPortSw_POS_OC12_LR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_LR_1_SM = _Hh3cevtPortSw_POS_OC12_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 114)
)
_Hh3cevtPortSw_POS_OC12_LR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_LR_2_SM = _Hh3cevtPortSw_POS_OC12_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 115)
)
_Hh3cevtPortSw_POS_OC12_LR_3_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC12_LR_3_SM = _Hh3cevtPortSw_POS_OC12_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 116)
)
_Hh3cevtPortSw_POS_OC48_SR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_SR_SM = _Hh3cevtPortSw_POS_OC48_SR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 117)
)
_Hh3cevtPortSw_POS_OC48_IR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_IR_SM = _Hh3cevtPortSw_POS_OC48_IR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 118)
)
_Hh3cevtPortSw_POS_OC48_IR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_IR_1_SM = _Hh3cevtPortSw_POS_OC48_IR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 119)
)
_Hh3cevtPortSw_POS_OC48_IR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_IR_2_SM = _Hh3cevtPortSw_POS_OC48_IR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 120)
)
_Hh3cevtPortSw_POS_OC48_LR_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_SM = _Hh3cevtPortSw_POS_OC48_LR_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 121)
)
_Hh3cevtPortSw_POS_OC48_LR_1_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_1_SM = _Hh3cevtPortSw_POS_OC48_LR_1_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 122)
)
_Hh3cevtPortSw_POS_OC48_LR_2_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_2_SM = _Hh3cevtPortSw_POS_OC48_LR_2_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 123)
)
_Hh3cevtPortSw_POS_OC48_LR_3_SM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_OC48_LR_3_SM = _Hh3cevtPortSw_POS_OC48_LR_3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 124)
)
_Hh3cevtPortSw_POS_I_64_1_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_I_64_1 = _Hh3cevtPortSw_POS_I_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 125)
)
_Hh3cevtPortSw_POS_I_64_2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_I_64_2 = _Hh3cevtPortSw_POS_I_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 126)
)
_Hh3cevtPortSw_POS_I_64_3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_I_64_3 = _Hh3cevtPortSw_POS_I_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 127)
)
_Hh3cevtPortSw_POS_I_64_5_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_I_64_5 = _Hh3cevtPortSw_POS_I_64_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 128)
)
_Hh3cevtPortSw_POS_S_64_1_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_S_64_1 = _Hh3cevtPortSw_POS_S_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 129)
)
_Hh3cevtPortSw_POS_S_64_2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_S_64_2 = _Hh3cevtPortSw_POS_S_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 130)
)
_Hh3cevtPortSw_POS_S_64_3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_S_64_3 = _Hh3cevtPortSw_POS_S_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 131)
)
_Hh3cevtPortSw_POS_S_64_5_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_S_64_5 = _Hh3cevtPortSw_POS_S_64_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 132)
)
_Hh3cevtPortSw_POS_L_64_1_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_L_64_1 = _Hh3cevtPortSw_POS_L_64_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 133)
)
_Hh3cevtPortSw_POS_L_64_2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_L_64_2 = _Hh3cevtPortSw_POS_L_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 134)
)
_Hh3cevtPortSw_POS_L_64_3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_L_64_3 = _Hh3cevtPortSw_POS_L_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 135)
)
_Hh3cevtPortSw_POS_V_64_2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_V_64_2 = _Hh3cevtPortSw_POS_V_64_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 136)
)
_Hh3cevtPortSw_POS_V_64_3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_V_64_3 = _Hh3cevtPortSw_POS_V_64_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 137)
)
_Hh3cevtPortSw_100BASE_FX_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_FX_BIDI = _Hh3cevtPortSw_100BASE_FX_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 138)
)
_Hh3cevtPortSw_100BASE_BX10_U_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_BX10_U_SFP = _Hh3cevtPortSw_100BASE_BX10_U_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 139)
)
_Hh3cevtPortSw_100BASE_BX10_D_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_BX10_D_SFP = _Hh3cevtPortSw_100BASE_BX10_D_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 140)
)
_Hh3cevtPortSw_1000BASE_BX10_U_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_BX10_U_SFP = _Hh3cevtPortSw_1000BASE_BX10_U_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 141)
)
_Hh3cevtPortSw_1000BASE_BX10_D_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_BX10_D_SFP = _Hh3cevtPortSw_1000BASE_BX10_D_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 142)
)
_Hh3cevtPortSw_STK_1000BASE_T_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_STK_1000BASE_T = _Hh3cevtPortSw_STK_1000BASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 143)
)
_Hh3cevtPortSw_RPR_PHYPOS_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_PHYPOS_CONNECTOR = _Hh3cevtPortSw_RPR_PHYPOS_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 144)
)
_Hh3cevtPortSw_RPR_PHY10GE_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_PHY10GE_CONNECTOR = _Hh3cevtPortSw_RPR_PHY10GE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 145)
)
_Hh3cevtPortSw_RPR_LOGICPOS_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_LOGICPOS_CONNECTOR = _Hh3cevtPortSw_RPR_LOGICPOS_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 146)
)
_Hh3cevtPortSw_RPR_LOGIC10GE_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_LOGIC10GE_CONNECTOR = _Hh3cevtPortSw_RPR_LOGIC10GE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 147)
)
_Hh3cevtPortSw_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_ZR = _Hh3cevtPortSw_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 148)
)
_Hh3cevtPortSw_TYPE_ERROR_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_TYPE_ERROR_CONNECTOR = _Hh3cevtPortSw_TYPE_ERROR_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 149)
)
_Hh3cevtPortSw_10G_STACK_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_STACK = _Hh3cevtPortSw_10G_STACK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 150)
)
_Hh3cevtPortSw_155_ATM_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_ATM_SX_MMF = _Hh3cevtPortSw_155_ATM_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 151)
)
_Hh3cevtPortSw_155_ATM_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_ATM_LX_SMF = _Hh3cevtPortSw_155_ATM_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 152)
)
_Hh3cevtPortSw_622_ATM_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_ATM_SX_MMF = _Hh3cevtPortSw_622_ATM_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 153)
)
_Hh3cevtPortSw_622_ATM_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_ATM_LX_SMF = _Hh3cevtPortSw_622_ATM_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 154)
)
_Hh3cevtPortSw_155_ATM_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_ATM_NO_CONNECTOR = _Hh3cevtPortSw_155_ATM_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 155)
)
_Hh3cevtPortSw_622_ATM_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_ATM_NO_CONNECTOR = _Hh3cevtPortSw_622_ATM_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 156)
)
_Hh3cevtPortSw_155_CPOS_E1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_E1_NO_CONNECTOR = _Hh3cevtPortSw_155_CPOS_E1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 157)
)
_Hh3cevtPortSw_155_CPOS_T1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_T1_NO_CONNECTOR = _Hh3cevtPortSw_155_CPOS_T1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 158)
)
_Hh3cevtPortSw_622_CPOS_E1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_E1_NO_CONNECTOR = _Hh3cevtPortSw_622_CPOS_E1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 159)
)
_Hh3cevtPortSw_622_CPOS_T1_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_T1_NO_CONNECTOR = _Hh3cevtPortSw_622_CPOS_T1_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 160)
)
_Hh3cevtPortSw_155_CPOS_E1_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_E1_SX_MMF = _Hh3cevtPortSw_155_CPOS_E1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 161)
)
_Hh3cevtPortSw_155_CPOS_T1_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_T1_SX_MMF = _Hh3cevtPortSw_155_CPOS_T1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 162)
)
_Hh3cevtPortSw_155_CPOS_E1_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_E1_LX_SMF = _Hh3cevtPortSw_155_CPOS_E1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 163)
)
_Hh3cevtPortSw_155_CPOS_T1_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_155_CPOS_T1_LX_SMF = _Hh3cevtPortSw_155_CPOS_T1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 164)
)
_Hh3cevtPortSw_622_CPOS_E1_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_E1_SX_MMF = _Hh3cevtPortSw_622_CPOS_E1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 165)
)
_Hh3cevtPortSw_622_CPOS_T1_SX_MMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_T1_SX_MMF = _Hh3cevtPortSw_622_CPOS_T1_SX_MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 166)
)
_Hh3cevtPortSw_622_CPOS_E1_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_E1_LX_SMF = _Hh3cevtPortSw_622_CPOS_E1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 167)
)
_Hh3cevtPortSw_622_CPOS_T1_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_622_CPOS_T1_LX_SMF = _Hh3cevtPortSw_622_CPOS_T1_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 168)
)
_Hh3cevtPortSw_E1_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_E1_CONNECTOR = _Hh3cevtPortSw_E1_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 169)
)
_Hh3cevtPortSw_T1_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_T1_CONNECTOR = _Hh3cevtPortSw_T1_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 170)
)
_Hh3cevtPortSw_1000BASE_STK_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_STK_SFP = _Hh3cevtPortSw_1000BASE_STK_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 171)
)
_Hh3cevtPortSw_1000BASE_BIDI_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_BIDI_SFP = _Hh3cevtPortSw_1000BASE_BIDI_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 172)
)
_Hh3cevtPortSw_1000BASE_CWDM_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_1000BASE_CWDM_SFP = _Hh3cevtPortSw_1000BASE_CWDM_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 173)
)
_Hh3cevtPortSw_100BASE_BIDI_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100BASE_BIDI_SFP = _Hh3cevtPortSw_100BASE_BIDI_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 174)
)
_Hh3cevtPortSw_OLT_1000BASE_PX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_OLT_1000BASE_PX_SFP = _Hh3cevtPortSw_OLT_1000BASE_PX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 175)
)
_Hh3cevtPortSw_OLT_1000BASE_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_OLT_1000BASE_NO_CONNECTOR = _Hh3cevtPortSw_OLT_1000BASE_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 176)
)
_Hh3cevtPortSw_RPR_PHYGE_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_PHYGE_CONNECTOR = _Hh3cevtPortSw_RPR_PHYGE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 177)
)
_Hh3cevtPortSw_RPR_LOGICGE_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_LOGICGE_CONNECTOR = _Hh3cevtPortSw_RPR_LOGICGE_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 178)
)
_Hh3cevtPortSw_100M_1550_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100M_1550_BIDI = _Hh3cevtPortSw_100M_1550_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 179)
)
_Hh3cevtPortSw_100M_1310_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100M_1310_BIDI = _Hh3cevtPortSw_100M_1310_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 180)
)
_Hh3cevtPortSw_RPR_PHYOC48_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_PHYOC48_CONNECTOR = _Hh3cevtPortSw_RPR_PHYOC48_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 181)
)
_Hh3cevtPortSw_RPR_LOGICOC48_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RPR_LOGICOC48_CONNECTOR = _Hh3cevtPortSw_RPR_LOGICOC48_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 182)
)
_Hh3cevtPortSw_100_1000_BASE_LX_SMF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_100_1000_BASE_LX_SMF = _Hh3cevtPortSw_100_1000_BASE_LX_SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 183)
)
_Hh3cevtPortSw_10G_ZW_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_ZW_SM_LC = _Hh3cevtPortSw_10G_ZW_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 184)
)
_Hh3cevtPortSw_10G_ZR_SM_LC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10G_ZR_SM_LC = _Hh3cevtPortSw_10G_ZR_SM_LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 185)
)
_Hh3cevtPortSw_XPK_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XPK_10GBASE_ZR = _Hh3cevtPortSw_XPK_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 186)
)
_Hh3cevtPortSw_SGMII_100_BASE_LX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SGMII_100_BASE_LX_SFP = _Hh3cevtPortSw_SGMII_100_BASE_LX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 187)
)
_Hh3cevtPortSw_SGMII_100_BASE_FX_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SGMII_100_BASE_FX_SFP = _Hh3cevtPortSw_SGMII_100_BASE_FX_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 188)
)
_Hh3cevtPortSw_WLAN_RADIO_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_WLAN_RADIO = _Hh3cevtPortSw_WLAN_RADIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 189)
)
_Hh3cevtPortSw_CABLE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CABLE = _Hh3cevtPortSw_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 190)
)
_Hh3cevtPortSw_SFP_PLUS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_NO_CONNECTOR = _Hh3cevtPortSw_SFP_PLUS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 191)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_SR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_SR = _Hh3cevtPortSw_SFP_PLUS_10GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 192)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_LR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_LR = _Hh3cevtPortSw_SFP_PLUS_10GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 193)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_LRM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_LRM = _Hh3cevtPortSw_SFP_PLUS_10GBASE_LRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 194)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_Cu_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_Cu = _Hh3cevtPortSw_SFP_PLUS_10GBASE_Cu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 195)
)
_Hh3cevtPortSw_SFP_PLUS_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_UNKNOWN = _Hh3cevtPortSw_SFP_PLUS_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 196)
)
_Hh3cevtPortSw_SFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_STACK_CONNECTOR = _Hh3cevtPortSw_SFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 197)
)
_Hh3cevtPortSw_POS_L_64_4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_POS_L_64_4 = _Hh3cevtPortSw_POS_L_64_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 198)
)
_Hh3cevtPortSw_MINISAS_HD_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_MINISAS_HD_STACK_CONNECTOR = _Hh3cevtPortSw_MINISAS_HD_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 199)
)
_Hh3cevtPortSw_ONU_1000BASE_PX_SFF_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_ONU_1000BASE_PX_SFF = _Hh3cevtPortSw_ONU_1000BASE_PX_SFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 200)
)
_Hh3cevtPortSw_RS485_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_RS485 = _Hh3cevtPortSw_RS485_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 201)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_ER_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_ER = _Hh3cevtPortSw_SFP_PLUS_10GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 202)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_ZR = _Hh3cevtPortSw_SFP_PLUS_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 203)
)
_Hh3cevtPortSw_XFP_10GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_ZR = _Hh3cevtPortSw_XFP_10GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 204)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_SR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_SR4 = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_SR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 205)
)
_Hh3cevtPortSw_QSFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_STACK_CONNECTOR = _Hh3cevtPortSw_QSFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 206)
)
_Hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR = _Hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 207)
)
_Hh3cevtPortSw_SFP_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_STACK_CONNECTOR = _Hh3cevtPortSw_SFP_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 208)
)
_Hh3cevtPortSw_QSFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_NO_CONNECTOR = _Hh3cevtPortSw_QSFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 209)
)
_Hh3cevtPortSw_10GBase_T_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBase_T = _Hh3cevtPortSw_10GBase_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 210)
)
_Hh3cevtPortSw_CFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP_NO_CONNECTOR = _Hh3cevtPortSw_CFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 211)
)
_Hh3cevtPortSw_CFP_40GBASE_LR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP_40GBASE_LR4 = _Hh3cevtPortSw_CFP_40GBASE_LR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 212)
)
_Hh3cevtPortSw_QSFP_PLUS_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_NO_CONNECTOR = _Hh3cevtPortSw_QSFP_PLUS_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 213)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_LR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_LR4 = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_LR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 214)
)
_Hh3cevtPortSw_CFP_40GBASE_SR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP_40GBASE_SR4 = _Hh3cevtPortSw_CFP_40GBASE_SR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 215)
)
_Hh3cevtPortSw_CFP_100GBASE_LR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP_100GBASE_LR4 = _Hh3cevtPortSw_CFP_100GBASE_LR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 216)
)
_Hh3cevtPortSw_CFP_100GBASE_SR10_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP_100GBASE_SR10 = _Hh3cevtPortSw_CFP_100GBASE_SR10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 217)
)
_Hh3cevtPortSw_CXP_100GBASE_SR10_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CXP_100GBASE_SR10 = _Hh3cevtPortSw_CXP_100GBASE_SR10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 218)
)
_Hh3cevtPortSw_CXP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CXP_NO_CONNECTOR = _Hh3cevtPortSw_CXP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 219)
)
_Hh3cevtPortSw_TRANSCEIVER_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_TRANSCEIVER_UNKNOWN = _Hh3cevtPortSw_TRANSCEIVER_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 220)
)
_Hh3cevtPortSw_QSFP_PLUS_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_UNKNOWN = _Hh3cevtPortSw_QSFP_PLUS_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 221)
)
_Hh3cevtPortSw_CFP_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP_UNKNOWN = _Hh3cevtPortSw_CFP_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 222)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_CSR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_CSR4 = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_CSR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 223)
)
_Hh3cevtPortSw_CFP_40GBASE_ER4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP_40GBASE_ER4 = _Hh3cevtPortSw_CFP_40GBASE_ER4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 224)
)
_Hh3cevtPortSw_SFP_1000BASE_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_1000BASE_BIDI = _Hh3cevtPortSw_SFP_1000BASE_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 225)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_ZR_DWDM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_ZR_DWDM = _Hh3cevtPortSw_SFP_PLUS_10GBASE_ZR_DWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 226)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_PSM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_PSM = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 227)
)
_Hh3cevtPortSw_SFP_8GFC_SW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_8GFC_SW = _Hh3cevtPortSw_SFP_8GFC_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 228)
)
_Hh3cevtPortSw_SFP_8GFC_LW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_8GFC_LW = _Hh3cevtPortSw_SFP_8GFC_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 229)
)
_Hh3cevtPortSw_CXP_100GBASE_AOC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CXP_100GBASE_AOC = _Hh3cevtPortSw_CXP_100GBASE_AOC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 230)
)
_Hh3cevtPortSw_QSFP_PLUS_ACTIVE_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_ACTIVE_STACK_CONNECTOR = _Hh3cevtPortSw_QSFP_PLUS_ACTIVE_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 231)
)
_Hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_STACK_CONNECTOR = _Hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 232)
)
_Hh3cevtPortSw_CFP2_100GBASE_LR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP2_100GBASE_LR4 = _Hh3cevtPortSw_CFP2_100GBASE_LR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 233)
)
_Hh3cevtPortSw_CFP2_100GBASE_SR10_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP2_100GBASE_SR10 = _Hh3cevtPortSw_CFP2_100GBASE_SR10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 234)
)
_Hh3cevtPortSw_QSFP_PLUS_ACTIVE_OPTICAL_CABLE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_ACTIVE_OPTICAL_CABLE = _Hh3cevtPortSw_QSFP_PLUS_ACTIVE_OPTICAL_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 235)
)
_Hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_OPTICAL_CABLE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_OPTICAL_CABLE = _Hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_OPTICAL_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 236)
)
_Hh3cevtPortSw_SFP_PLUS_ACTIVE_OPTICAL_CABLE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_ACTIVE_OPTICAL_CABLE = _Hh3cevtPortSw_SFP_PLUS_ACTIVE_OPTICAL_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 237)
)
_Hh3cevtPortSw_CFP2_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP2_NO_CONNECTOR = _Hh3cevtPortSw_CFP2_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 238)
)
_Hh3cevtPortSw_QSFP28_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_NO_CONNECTOR = _Hh3cevtPortSw_QSFP28_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 239)
)
_Hh3cevtPortSw_QSFP28_100GBASE_SR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_SR4 = _Hh3cevtPortSw_QSFP28_100GBASE_SR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 240)
)
_Hh3cevtPortSw_QSFP28_100GBASE_LR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_LR4 = _Hh3cevtPortSw_QSFP28_100GBASE_LR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 241)
)
_Hh3cevtPortSw_QSFP28_100GBASE_ER4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_ER4 = _Hh3cevtPortSw_QSFP28_100GBASE_ER4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 242)
)
_Hh3cevtPortSw_QSFP28_100GBASE_PSM4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_PSM4 = _Hh3cevtPortSw_QSFP28_100GBASE_PSM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 243)
)
_Hh3cevtPortSw_QSFP28_100GBASE_CWDM4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_CWDM4 = _Hh3cevtPortSw_QSFP28_100GBASE_CWDM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 244)
)
_Hh3cevtPortSw_QSFP28_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_STACK_CONNECTOR = _Hh3cevtPortSw_QSFP28_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 245)
)
_Hh3cevtPortSw_QSFP28_TO_4SFP28_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_TO_4SFP28_STACK_CONNECTOR = _Hh3cevtPortSw_QSFP28_TO_4SFP28_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 246)
)
_Hh3cevtPortSw_QSFP28_ACTIVE_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_ACTIVE_STACK_CONNECTOR = _Hh3cevtPortSw_QSFP28_ACTIVE_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 247)
)
_Hh3cevtPortSw_QSFP28_TO_4SFP28_ACTIVE_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_TO_4SFP28_ACTIVE_STACK_CONNECTOR = _Hh3cevtPortSw_QSFP28_TO_4SFP28_ACTIVE_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 248)
)
_Hh3cevtPortSw_QSFP28_ACTIVE_OPTICAL_CABLE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_ACTIVE_OPTICAL_CABLE = _Hh3cevtPortSw_QSFP28_ACTIVE_OPTICAL_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 249)
)
_Hh3cevtPortSw_QSFP28_TO_4SFP28_ACTIVE_OPTICAL_CABLE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_TO_4SFP28_ACTIVE_OPTICAL_CABLE = _Hh3cevtPortSw_QSFP28_TO_4SFP28_ACTIVE_OPTICAL_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 250)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_LM4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_LM4 = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_LM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 251)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_SWDM4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_SWDM4 = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_SWDM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 252)
)
_Hh3cevtPortSw_CFP_100GBASE_ER4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP_100GBASE_ER4 = _Hh3cevtPortSw_CFP_100GBASE_ER4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 253)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_ER4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_ER4 = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_ER4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 254)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_ER4L_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_ER4L = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_ER4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 255)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_BIDI = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 256)
)
_Hh3cevtPortSw_QSFP_PLUS_40GBASE_LR4L_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP_PLUS_40GBASE_LR4L = _Hh3cevtPortSw_QSFP_PLUS_40GBASE_LR4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 257)
)
_Hh3cevtPortSw_CFP2_100GBASE_eSR10_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP2_100GBASE_eSR10 = _Hh3cevtPortSw_CFP2_100GBASE_eSR10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 258)
)
_Hh3cevtPortSw_TUNABLE_SFP_PLUS_10GBASE_ZR_DWDM_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_TUNABLE_SFP_PLUS_10GBASE_ZR_DWDM = _Hh3cevtPortSw_TUNABLE_SFP_PLUS_10GBASE_ZR_DWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 259)
)
_Hh3cevtPortSw_SFP28_25GBASE_SR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP28_25GBASE_SR = _Hh3cevtPortSw_SFP28_25GBASE_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 260)
)
_Hh3cevtPortSw_SFP28_ACTIVE_OPTICAL_CABLE_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP28_ACTIVE_OPTICAL_CABLE = _Hh3cevtPortSw_SFP28_ACTIVE_OPTICAL_CABLE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 261)
)
_Hh3cevtPortSw_SFP28_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP28_STACK_CONNECTOR = _Hh3cevtPortSw_SFP28_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 262)
)
_Hh3cevtPortSw_2DOT5GBASE_T_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_2DOT5GBASE_T = _Hh3cevtPortSw_2DOT5GBASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 263)
)
_Hh3cevtPortSw_QSFP28_100GBASE_SWDM4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_SWDM4 = _Hh3cevtPortSw_QSFP28_100GBASE_SWDM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 264)
)
_Hh3cevtPortSw_QSFP28_100GBASE_eSWDM4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_eSWDM4 = _Hh3cevtPortSw_QSFP28_100GBASE_eSWDM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 265)
)
_Hh3cevtPortSw_SFP_PLUS_10GBASE_T_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_10GBASE_T = _Hh3cevtPortSw_SFP_PLUS_10GBASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 266)
)
_Hh3cevtPortSw_QSFP28_100GBASE_eSR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_eSR4 = _Hh3cevtPortSw_QSFP28_100GBASE_eSR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 267)
)
_Hh3cevtPortSw_QSFP28_100GBASE_BIDI_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_BIDI = _Hh3cevtPortSw_QSFP28_100GBASE_BIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 268)
)
_Hh3cevtPortSw_QSFP28_100GBASE_WDM2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_WDM2 = _Hh3cevtPortSw_QSFP28_100GBASE_WDM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 269)
)
_Hh3cevtPortSw_SFP28_25GBASE_LR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP28_25GBASE_LR = _Hh3cevtPortSw_SFP28_25GBASE_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 270)
)
_Hh3cevtPortSw_CFP2_100GBASE_ER4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP2_100GBASE_ER4 = _Hh3cevtPortSw_CFP2_100GBASE_ER4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 271)
)
_Hh3cevtPortSw_CFP2_DCO_200GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP2_DCO_200GBASE_ZR = _Hh3cevtPortSw_CFP2_DCO_200GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 272)
)
_Hh3cevtPortSw_CFP2_100GBASE_ER4L_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_CFP2_100GBASE_ER4L = _Hh3cevtPortSw_CFP2_100GBASE_ER4L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 273)
)
_Hh3cevtPortSw_SFP_16GFC_SW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_16GFC_SW = _Hh3cevtPortSw_SFP_16GFC_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 274)
)
_Hh3cevtPortSw_SFP_16GFC_LW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_16GFC_LW = _Hh3cevtPortSw_SFP_16GFC_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 275)
)
_Hh3cevtPortSw_SFP_32GFC_SW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_32GFC_SW = _Hh3cevtPortSw_SFP_32GFC_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 276)
)
_Hh3cevtPortSw_SFP_32GFC_LW_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_32GFC_LW = _Hh3cevtPortSw_SFP_32GFC_LW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 277)
)
_Hh3cevtPortSw_XFP_10GBASE_PR_D3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_PR_D3 = _Hh3cevtPortSw_XFP_10GBASE_PR_D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 278)
)
_Hh3cevtPortSw_XFP_10GBASE_PRX_D3_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_XFP_10GBASE_PRX_D3 = _Hh3cevtPortSw_XFP_10GBASE_PRX_D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 279)
)
_Hh3cevtPortSw_5GBASE_T_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_5GBASE_T = _Hh3cevtPortSw_5GBASE_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 280)
)
_Hh3cevtPortSw_QSFP28_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_UNKNOWN = _Hh3cevtPortSw_QSFP28_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 281)
)
_Hh3cevtPortSw_SFP28_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP28_UNKNOWN = _Hh3cevtPortSw_SFP28_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 282)
)
_Hh3cevtPortSw_SFP28_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP28_NO_CONNECTOR = _Hh3cevtPortSw_SFP28_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 283)
)
_Hh3cevtPortSw_SFP_PLUS_9_8GCRPI_IR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_9_8GCRPI_IR = _Hh3cevtPortSw_SFP_PLUS_9_8GCRPI_IR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 284)
)
_Hh3cevtPortSw_SFP_PLUS_9_8GCRPI_LR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP_PLUS_9_8GCRPI_LR = _Hh3cevtPortSw_SFP_PLUS_9_8GCRPI_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 285)
)
_Hh3cevtPortSw_50GBase_F_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_50GBase_F = _Hh3cevtPortSw_50GBase_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 286)
)
_Hh3cevtPortSw_QSFP28_50GBASE_PAM4_LR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_50GBASE_PAM4_LR = _Hh3cevtPortSw_QSFP28_50GBASE_PAM4_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 287)
)
_Hh3cevtPortSw_10GBASE_BIDI_SFP_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_BIDI_SFP = _Hh3cevtPortSw_10GBASE_BIDI_SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 288)
)
_Hh3cevtPortSw_10GBASE_BIDI_U_SFP_PLUS_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_BIDI_U_SFP_PLUS = _Hh3cevtPortSw_10GBASE_BIDI_U_SFP_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 291)
)
_Hh3cevtPortSw_10GBASE_BIDI_D_SFP_PLUS_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_10GBASE_BIDI_D_SFP_PLUS = _Hh3cevtPortSw_10GBASE_BIDI_D_SFP_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 292)
)
_Hh3cevtPortSw_QSFPDD_STACK_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFPDD_STACK_CONNECTOR = _Hh3cevtPortSw_QSFPDD_STACK_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 293)
)
_Hh3cevtPortSw_QSFPDD_400GBASE_SR8_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFPDD_400GBASE_SR8 = _Hh3cevtPortSw_QSFPDD_400GBASE_SR8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 294)
)
_Hh3cevtPortSw_QSFP28_100GBASE_ZR2_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_ZR2 = _Hh3cevtPortSw_QSFP28_100GBASE_ZR2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 295)
)
_Hh3cevtPortSw_QSFP28_50GBASE_ER_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_50GBASE_ER = _Hh3cevtPortSw_QSFP28_50GBASE_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 296)
)
_Hh3cevtPortSw_SFP28_25GBASE_eLR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP28_25GBASE_eLR = _Hh3cevtPortSw_SFP28_25GBASE_eLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 297)
)
_Hh3cevtPortSw_QSFP28_100GBASE_ER4_NO_FEC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_ER4_NO_FEC = _Hh3cevtPortSw_QSFP28_100GBASE_ER4_NO_FEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 298)
)
_Hh3cevtPortSw_QSFP28_100GBASE_ZR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP28_100GBASE_ZR4 = _Hh3cevtPortSw_QSFP28_100GBASE_ZR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 299)
)
_Hh3cevtPortSw_QSFPDD_400GBASE_FR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFPDD_400GBASE_FR4 = _Hh3cevtPortSw_QSFPDD_400GBASE_FR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 300)
)
_Hh3cevtPortSw_QSFP56_200GBASE_FR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP56_200GBASE_FR4 = _Hh3cevtPortSw_QSFP56_200GBASE_FR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 301)
)
_Hh3cevtPortSw_QSFP56_200GBASE_SR4_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP56_200GBASE_SR4 = _Hh3cevtPortSw_QSFP56_200GBASE_SR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 302)
)
_Hh3cevtPortSw_QSFP56_200GBASE_AOC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFP56_200GBASE_AOC = _Hh3cevtPortSw_QSFP56_200GBASE_AOC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 303)
)
_Hh3cevtPortSw_DSFP_100GBASE_AOC_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_DSFP_100GBASE_AOC = _Hh3cevtPortSw_DSFP_100GBASE_AOC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 304)
)
_Hh3cevtPortSw_SFP28_25GBASE_CSR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_SFP28_25GBASE_CSR = _Hh3cevtPortSw_SFP28_25GBASE_CSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 305)
)
_Hh3cevtPortSw_QSFPDD_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFPDD_UNKNOWN = _Hh3cevtPortSw_QSFPDD_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 306)
)
_Hh3cevtPortSw_QSFPDD_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFPDD_NO_CONNECTOR = _Hh3cevtPortSw_QSFPDD_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 307)
)
_Hh3cevtPortSw_DSFP_UNKNOWN_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_DSFP_UNKNOWN = _Hh3cevtPortSw_DSFP_UNKNOWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 308)
)
_Hh3cevtPortSw_DSFP_NO_CONNECTOR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_DSFP_NO_CONNECTOR = _Hh3cevtPortSw_DSFP_NO_CONNECTOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 309)
)
_Hh3cevtPortSw_QSFPDD_400GBASE_ZR_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFPDD_400GBASE_ZR = _Hh3cevtPortSw_QSFPDD_400GBASE_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 310)
)
_Hh3cevtPortSw_QSFPDD_400GBASE_LR8_ObjectIdentity = ObjectIdentity
hh3cevtPortSw_QSFPDD_400GBASE_LR8 = _Hh3cevtPortSw_QSFPDD_400GBASE_LR8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 10, 4, 311)
)
_Hh3cevtStack_ObjectIdentity = ObjectIdentity
hh3cevtStack = _Hh3cevtStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3, 1, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ENTITY-VENDORTYPE-OID-MIB",
    **{"hh3cEntityVendorTypeOID": hh3cEntityVendorTypeOID,
       "hh3cEntityVendortypeObjects": hh3cEntityVendortypeObjects,
       "hh3cevtOther": hh3cevtOther,
       "hh3cevtOtherUnknownCard": hh3cevtOtherUnknownCard,
       "hh3cevtCPU": hh3cevtCPU,
       "hh3cevtGeneralCPU": hh3cevtGeneralCPU,
       "hh3cevtDOM": hh3cevtDOM,
       "hh3cevtCFCard": hh3cevtCFCard,
       "hh3cevtHardDisk": hh3cevtHardDisk,
       "hh3cevtSDCard": hh3cevtSDCard,
       "hh3cevtMEM": hh3cevtMEM,
       "hh3cevtUnknown": hh3cevtUnknown,
       "hh3cevtChassis": hh3cevtChassis,
       "hh3cevtBackplane": hh3cevtBackplane,
       "hh3cevtContainer": hh3cevtContainer,
       "hh3cevtPowerSupply": hh3cevtPowerSupply,
       "hh3cevtPowerSupplyAC": hh3cevtPowerSupplyAC,
       "hh3cevtPowerSupplyDC": hh3cevtPowerSupplyDC,
       "hh3cevtPowerSupplySTD130W": hh3cevtPowerSupplySTD130W,
       "hh3cevtPowerSupplySTD180W": hh3cevtPowerSupplySTD180W,
       "hh3cevtPowerSupplyPOE24Port": hh3cevtPowerSupplyPOE24Port,
       "hh3cevtPowerSupplyPOE48Port": hh3cevtPowerSupplyPOE48Port,
       "hh3cevtPowerSupplyLSUM1AC2500": hh3cevtPowerSupplyLSUM1AC2500,
       "hh3cevtPowerSupplyLSUM2AC2500": hh3cevtPowerSupplyLSUM2AC2500,
       "hh3cevtPowerSupplyLSUM1DC2400": hh3cevtPowerSupplyLSUM1DC2400,
       "hh3cevtPowerSupplyLSUM1AC1200": hh3cevtPowerSupplyLSUM1AC1200,
       "hh3cevtPowerSupplyLSQM1DC2400": hh3cevtPowerSupplyLSQM1DC2400,
       "hh3cevtPowerSupplyLSUM5AC2500": hh3cevtPowerSupplyLSUM5AC2500,
       "hh3cevtPowerSupplyLSUM5DC2400": hh3cevtPowerSupplyLSUM5DC2400,
       "hh3cevtPowerSupplyLSUM6DC2400": hh3cevtPowerSupplyLSUM6DC2400,
       "hh3cevtPowerSupplyLSUM6AC2500": hh3cevtPowerSupplyLSUM6AC2500,
       "hh3cevtPowerSupplyLSQM1AC1400": hh3cevtPowerSupplyLSQM1AC1400,
       "hh3cevtPowerSupplyLSQM1DC1400": hh3cevtPowerSupplyLSQM1DC1400,
       "hh3cevtPowerSupplyLSQM1AC2800": hh3cevtPowerSupplyLSQM1AC2800,
       "hh3cevtPowerSupplyLSQM2AC1400": hh3cevtPowerSupplyLSQM2AC1400,
       "hh3cevtPowerSupplyLSQM1AC6000": hh3cevtPowerSupplyLSQM1AC6000,
       "hh3cevtPowerSupplyLSQM2AC6000": hh3cevtPowerSupplyLSQM2AC6000,
       "hh3cevtPowerSupplyLSQM1AC300": hh3cevtPowerSupplyLSQM1AC300,
       "hh3cevtPowerSupplyLSQM1AC650": hh3cevtPowerSupplyLSQM1AC650,
       "hh3cevtPowerSupplyLSQM1DC650": hh3cevtPowerSupplyLSQM1DC650,
       "hh3cevtPowerSupplyLSQM1PWRSPA": hh3cevtPowerSupplyLSQM1PWRSPA,
       "hh3cevtPowerSupplyLSWM1RPS800": hh3cevtPowerSupplyLSWM1RPS800,
       "hh3cevtPowerSupplyLSQM7AC1400": hh3cevtPowerSupplyLSQM7AC1400,
       "hh3cevtPowerSupplyLSQM7DC1400": hh3cevtPowerSupplyLSQM7DC1400,
       "hh3cevtPowerSupplyLSQM7AC2800": hh3cevtPowerSupplyLSQM7AC2800,
       "hh3cevtPowerSupplyLSQM7AC6000": hh3cevtPowerSupplyLSQM7AC6000,
       "hh3cevtPowerSupplyLSQM7AC300": hh3cevtPowerSupplyLSQM7AC300,
       "hh3cevtPowerSupplyLSQM7AC650": hh3cevtPowerSupplyLSQM7AC650,
       "hh3cevtPowerSupplyLSQM7DC650": hh3cevtPowerSupplyLSQM7DC650,
       "hh3cevtPowerSupplyLSWM2RPS800": hh3cevtPowerSupplyLSWM2RPS800,
       "hh3cevtPowerSupplySecPathAC": hh3cevtPowerSupplySecPathAC,
       "hh3cevtPowerSupplySecPathDC": hh3cevtPowerSupplySecPathDC,
       "hh3cevtFan": hh3cevtFan,
       "hh3cevtHotSwapFan": hh3cevtHotSwapFan,
       "hh3cevtNonHotSwapFan": hh3cevtNonHotSwapFan,
       "hh3cevtFanLSUM110504": hh3cevtFanLSUM110504,
       "hh3cevtFanLSUM110508": hh3cevtFanLSUM110508,
       "hh3cevtFanLSUM110508V": hh3cevtFanLSUM110508V,
       "hh3cevtFanLSUM110512": hh3cevtFanLSUM110512,
       "hh3cevtFanLSUM210512": hh3cevtFanLSUM210512,
       "hh3cevtFanLSUM510504": hh3cevtFanLSUM510504,
       "hh3cevtFanLSUM510508": hh3cevtFanLSUM510508,
       "hh3cevtFanLSUM510508V": hh3cevtFanLSUM510508V,
       "hh3cevtFanLSUM510512U": hh3cevtFanLSUM510512U,
       "hh3cevtFanLSUM510512D": hh3cevtFanLSUM510512D,
       "hh3cevtFanLSUM511908V": hh3cevtFanLSUM511908V,
       "hh3cevtFanLSQM17502E": hh3cevtFanLSQM17502E,
       "hh3cevtFanLSQM17503E": hh3cevtFanLSQM17503E,
       "hh3cevtFanLSQM17503ES": hh3cevtFanLSQM17503ES,
       "hh3cevtFanLSQM17506E": hh3cevtFanLSQM17506E,
       "hh3cevtFanLSQM17506EV": hh3cevtFanLSQM17506EV,
       "hh3cevtFanLSQM17510E": hh3cevtFanLSQM17510E,
       "hh3cevtFanLSQM57503": hh3cevtFanLSQM57503,
       "hh3cevtFanLSQM57502": hh3cevtFanLSQM57502,
       "hh3cevtFanLSQM57506": hh3cevtFanLSQM57506,
       "hh3cevtFanLSQM57510": hh3cevtFanLSQM57510,
       "hh3cevtHotSwapFan-NSUM1BFANSC": hh3cevtHotSwapFan_NSUM1BFANSC,
       "hh3cevtHotSwapFan-NSUM1BFANSCB": hh3cevtHotSwapFan_NSUM1BFANSCB,
       "hh3cevtSensor": hh3cevtSensor,
       "hh3cevtSensorTemperature": hh3cevtSensorTemperature,
       "hh3cevtSensorVoltage": hh3cevtSensorVoltage,
       "hh3cevtSensorFanSpeed": hh3cevtSensorFanSpeed,
       "hh3cevtModule": hh3cevtModule,
       "hh3cevtModuleUnknownCard": hh3cevtModuleUnknownCard,
       "hh3cevtModuleCommonCards": hh3cevtModuleCommonCards,
       "hh3cevtModuleBoxCEN": hh3cevtModuleBoxCEN,
       "hh3cevtModuleBoxIRF48GE": hh3cevtModuleBoxIRF48GE,
       "hh3cevtModuleBoxIRF24GE24TGE": hh3cevtModuleBoxIRF24GE24TGE,
       "hh3cevtModuleChassisMpu": hh3cevtModuleChassisMpu,
       "hh3cevtModuleLPU48GE": hh3cevtModuleLPU48GE,
       "hh3cevtModuleLPU4GE4Serial": hh3cevtModuleLPU4GE4Serial,
       "hh3cevtModuleLPU4GE4Pos": hh3cevtModuleLPU4GE4Pos,
       "hh3cevtModuleLPU4GE4E1": hh3cevtModuleLPU4GE4E1,
       "hh3cevtModuleRouterType": hh3cevtModuleRouterType,
       "hh3cevtModuleRt-As": hh3cevtModuleRt_As,
       "hh3cevtModuleRt-Sa": hh3cevtModuleRt_Sa,
       "hh3cevtModuleRt-Bi": hh3cevtModuleRt_Bi,
       "hh3cevtModuleRt-E12": hh3cevtModuleRt_E12,
       "hh3cevtModuleRt-E14": hh3cevtModuleRt_E14,
       "hh3cevtModuleRt-Fe1": hh3cevtModuleRt_Fe1,
       "hh3cevtModuleRt-E1": hh3cevtModuleRt_E1,
       "hh3cevtModuleRt-Fe2": hh3cevtModuleRt_Fe2,
       "hh3cevtModuleRt-Vi2": hh3cevtModuleRt_Vi2,
       "hh3cevtModuleRt-Vi4": hh3cevtModuleRt_Vi4,
       "hh3cevtModuleRt-Vi30": hh3cevtModuleRt_Vi30,
       "hh3cevtModuleRt-S1b": hh3cevtModuleRt_S1b,
       "hh3cevtModuleRt-Sa2": hh3cevtModuleRt_Sa2,
       "hh3cevtModuleRt-As16": hh3cevtModuleRt_As16,
       "hh3cevtModuleRt-New8as": hh3cevtModuleRt_New8as,
       "hh3cevtModuleRt-Sa1": hh3cevtModuleRt_Sa1,
       "hh3cevtModuleRt-Fxs2": hh3cevtModuleRt_Fxs2,
       "hh3cevtModuleRt-Fxo2": hh3cevtModuleRt_Fxo2,
       "hh3cevtModuleRt-Em2": hh3cevtModuleRt_Em2,
       "hh3cevtModuleRt-Fxs4": hh3cevtModuleRt_Fxs4,
       "hh3cevtModuleRt-Fxo4": hh3cevtModuleRt_Fxo4,
       "hh3cevtModuleRt-Em4": hh3cevtModuleRt_Em4,
       "hh3cevtModuleRt-Sab": hh3cevtModuleRt_Sab,
       "hh3cevtModuleRt-E1vi": hh3cevtModuleRt_E1vi,
       "hh3cevtModuleRt-Am12": hh3cevtModuleRt_Am12,
       "hh3cevtModuleRt-Am6": hh3cevtModuleRt_Am6,
       "hh3cevtModuleRt-Ndec": hh3cevtModuleRt_Ndec,
       "hh3cevtModuleRt-Newsa2": hh3cevtModuleRt_Newsa2,
       "hh3cevtModuleRt-Aux": hh3cevtModuleRt_Aux,
       "hh3cevtModuleRt-Console": hh3cevtModuleRt_Console,
       "hh3cevtModuleRt-Sic-wan": hh3cevtModuleRt_Sic_wan,
       "hh3cevtModuleRt-Sic-1fe": hh3cevtModuleRt_Sic_1fe,
       "hh3cevtModuleRt-Sic-1sa": hh3cevtModuleRt_Sic_1sa,
       "hh3cevtModuleRt-Sic-3as": hh3cevtModuleRt_Sic_3as,
       "hh3cevtModuleRt-Sic-1e1": hh3cevtModuleRt_Sic_1e1,
       "hh3cevtModuleRt-Sic-1t1": hh3cevtModuleRt_Sic_1t1,
       "hh3cevtModuleRt-Sic-1bu": hh3cevtModuleRt_Sic_1bu,
       "hh3cevtModuleRt-Sic-2bu": hh3cevtModuleRt_Sic_2bu,
       "hh3cevtModuleRt-Sic-1bs": hh3cevtModuleRt_Sic_1bs,
       "hh3cevtModuleRt-Sic-2bs": hh3cevtModuleRt_Sic_2bs,
       "hh3cevtModuleRt-Sic-1am": hh3cevtModuleRt_Sic_1am,
       "hh3cevtModuleRt-Sic-2am": hh3cevtModuleRt_Sic_2am,
       "hh3cevtModuleRt-Sic-1em": hh3cevtModuleRt_Sic_1em,
       "hh3cevtModuleRt-Sic-2em": hh3cevtModuleRt_Sic_2em,
       "hh3cevtModuleRt-Sic-1fxs": hh3cevtModuleRt_Sic_1fxs,
       "hh3cevtModuleRt-Sic-2fxs": hh3cevtModuleRt_Sic_2fxs,
       "hh3cevtModuleRt-Sic-1fxo": hh3cevtModuleRt_Sic_1fxo,
       "hh3cevtModuleRt-Sic-2fxo": hh3cevtModuleRt_Sic_2fxo,
       "hh3cevtModuleRt-Fcm6": hh3cevtModuleRt_Fcm6,
       "hh3cevtModuleRt-Sa8": hh3cevtModuleRt_Sa8,
       "hh3cevtModuleRt-T11": hh3cevtModuleRt_T11,
       "hh3cevtModuleRt-T12": hh3cevtModuleRt_T12,
       "hh3cevtModuleRt-T14": hh3cevtModuleRt_T14,
       "hh3cevtModuleRt-T1vi": hh3cevtModuleRt_T1vi,
       "hh3cevtModuleRt-Fcm4": hh3cevtModuleRt_Fcm4,
       "hh3cevtModuleRt-Fcm2": hh3cevtModuleRt_Fcm2,
       "hh3cevtModuleRt-Rtb21ce3": hh3cevtModuleRt_Rtb21ce3,
       "hh3cevtModuleRt-Ame6": hh3cevtModuleRt_Ame6,
       "hh3cevtModuleRt-Ame12": hh3cevtModuleRt_Ame12,
       "hh3cevtModuleRt-E11-f": hh3cevtModuleRt_E11_f,
       "hh3cevtModuleRt-E12-f": hh3cevtModuleRt_E12_f,
       "hh3cevtModuleRt-E14-f": hh3cevtModuleRt_E14_f,
       "hh3cevtModuleRt-T11-f": hh3cevtModuleRt_T11_f,
       "hh3cevtModuleRt-T12-f": hh3cevtModuleRt_T12_f,
       "hh3cevtModuleRt-T14-f": hh3cevtModuleRt_T14_f,
       "hh3cevtModuleRt-E11-f-17": hh3cevtModuleRt_E11_f_17,
       "hh3cevtModuleRt-T11-f-17": hh3cevtModuleRt_T11_f_17,
       "hh3cevtModuleRt-Rtb21ct3": hh3cevtModuleRt_Rtb21ct3,
       "hh3cevtModuleRt-Atmadsl1": hh3cevtModuleRt_Atmadsl1,
       "hh3cevtModuleRt-Atmadsl2": hh3cevtModuleRt_Atmadsl2,
       "hh3cevtModuleRt-Atm155m": hh3cevtModuleRt_Atm155m,
       "hh3cevtModuleRt-Ase8": hh3cevtModuleRt_Ase8,
       "hh3cevtModuleRt-Ase16": hh3cevtModuleRt_Ase16,
       "hh3cevtModuleRt-Sae4": hh3cevtModuleRt_Sae4,
       "hh3cevtModuleRt-Sae2": hh3cevtModuleRt_Sae2,
       "hh3cevtModuleRt-Atmshdsl1": hh3cevtModuleRt_Atmshdsl1,
       "hh3cevtModuleRt-Atmshdsl2": hh3cevtModuleRt_Atmshdsl2,
       "hh3cevtModuleRt-Atmshdsl4": hh3cevtModuleRt_Atmshdsl4,
       "hh3cevtModuleRt-Atm25m": hh3cevtModuleRt_Atm25m,
       "hh3cevtModuleRt-Atme3": hh3cevtModuleRt_Atme3,
       "hh3cevtModuleRt-Atmt3": hh3cevtModuleRt_Atmt3,
       "hh3cevtModuleRt-Xdsl-fec": hh3cevtModuleRt_Xdsl_fec,
       "hh3cevtModuleRt-Xdsl-adsl": hh3cevtModuleRt_Xdsl_adsl,
       "hh3cevtModuleRt-Xdsl-gshdsl": hh3cevtModuleRt_Xdsl_gshdsl,
       "hh3cevtModuleRt-Xdsl-bri": hh3cevtModuleRt_Xdsl_bri,
       "hh3cevtModuleRt-Xdsl-scc": hh3cevtModuleRt_Xdsl_scc,
       "hh3cevtModuleRt-Ge1": hh3cevtModuleRt_Ge1,
       "hh3cevtModuleRt-Pos155m": hh3cevtModuleRt_Pos155m,
       "hh3cevtModuleRt-Cpos": hh3cevtModuleRt_Cpos,
       "hh3cevtModuleRt-Fe1op": hh3cevtModuleRt_Fe1op,
       "hh3cevtModuleRt-Sae8": hh3cevtModuleRt_Sae8,
       "hh3cevtModuleRt-Atm155m-mm": hh3cevtModuleRt_Atm155m_mm,
       "hh3cevtModuleRt-Atm155m-sm": hh3cevtModuleRt_Atm155m_sm,
       "hh3cevtModuleRt-Atm155m-sml": hh3cevtModuleRt_Atm155m_sml,
       "hh3cevtModuleRt-Fe1op-sfx": hh3cevtModuleRt_Fe1op_sfx,
       "hh3cevtModuleRt-Fe1op-mfx": hh3cevtModuleRt_Fe1op_mfx,
       "hh3cevtModuleRt-Cpos-t1": hh3cevtModuleRt_Cpos_t1,
       "hh3cevtModuleRt-Ge1op": hh3cevtModuleRt_Ge1op,
       "hh3cevtModuleRt-Ge2op": hh3cevtModuleRt_Ge2op,
       "hh3cevtModuleRt-Ge2": hh3cevtModuleRt_Ge2,
       "hh3cevtModuleRt-Fix-1wan": hh3cevtModuleRt_Fix_1wan,
       "hh3cevtModuleRt-Fix-1sae": hh3cevtModuleRt_Fix_1sae,
       "hh3cevtModuleRt-Cavium": hh3cevtModuleRt_Cavium,
       "hh3cevtModuleRt-Sic1Eth": hh3cevtModuleRt_Sic1Eth,
       "hh3cevtModuleRt-atm1ADSLI": hh3cevtModuleRt_atm1ADSLI,
       "hh3cevtModuleRt-atm2ADSLI": hh3cevtModuleRt_atm2ADSLI,
       "hh3cevtModuleRt-fix-e11": hh3cevtModuleRt_fix_e11,
       "hh3cevtModuleRt-fix-t11": hh3cevtModuleRt_fix_t11,
       "hh3cevtModuleRt-e18-75": hh3cevtModuleRt_e18_75,
       "hh3cevtModuleRt-e18-120": hh3cevtModuleRt_e18_120,
       "hh3cevtModuleRt-t18": hh3cevtModuleRt_t18,
       "hh3cevtModuleRt-sic-1vifxs": hh3cevtModuleRt_sic_1vifxs,
       "hh3cevtModuleRt-sic-1vifxo": hh3cevtModuleRt_sic_1vifxo,
       "hh3cevtModuleRt-sic-2vifxs": hh3cevtModuleRt_sic_2vifxs,
       "hh3cevtModuleRt-sic-2vifxo": hh3cevtModuleRt_sic_2vifxo,
       "hh3cevtModuleRt-xdsl-fec-new": hh3cevtModuleRt_xdsl_fec_new,
       "hh3cevtModuleRt-xdsl-sa": hh3cevtModuleRt_xdsl_sa,
       "hh3cevtModuleRt-bs4": hh3cevtModuleRt_bs4,
       "hh3cevtModuleRt-ima-8e175": hh3cevtModuleRt_ima_8e175,
       "hh3cevtModuleRt-ima-8e1120": hh3cevtModuleRt_ima_8e1120,
       "hh3cevtModuleRt-ima-4e175": hh3cevtModuleRt_ima_4e175,
       "hh3cevtModuleRt-ima-4e1120": hh3cevtModuleRt_ima_4e1120,
       "hh3cevtModuleRt-ima-8t1": hh3cevtModuleRt_ima_8t1,
       "hh3cevtModuleRt-ima-4t1": hh3cevtModuleRt_ima_4t1,
       "hh3cevtModuleRt-sic-1t1f": hh3cevtModuleRt_sic_1t1f,
       "hh3cevtModuleRT-SIC-1E1F": hh3cevtModuleRT_SIC_1E1F,
       "hh3cevtModuleRt-VG-16fxs": hh3cevtModuleRt_VG_16fxs,
       "hh3cevtModuleRt-VG-32fxs": hh3cevtModuleRt_VG_32fxs,
       "hh3cevtModuleRt-VG-8fxo": hh3cevtModuleRt_VG_8fxo,
       "hh3cevtModuleRt-VG-2fe": hh3cevtModuleRt_VG_2fe,
       "hh3cevtModuleRt-sib": hh3cevtModuleRt_sib,
       "hh3cevtModuleRt-cie32": hh3cevtModuleRt_cie32,
       "hh3cevtModuleRt-cie64": hh3cevtModuleRt_cie64,
       "hh3cevtModuleRt-cie96": hh3cevtModuleRt_cie96,
       "hh3cevtModuleRt-Fe4": hh3cevtModuleRt_Fe4,
       "hh3cevtModuleRt-fxs4fxo1": hh3cevtModuleRt_fxs4fxo1,
       "hh3cevtModuleRt-atm1shdsl4wire": hh3cevtModuleRt_atm1shdsl4wire,
       "hh3cevtModuleRt-atmIma4shdsl": hh3cevtModuleRt_atmIma4shdsl,
       "hh3cevtModuleRt-ls4": hh3cevtModuleRt_ls4,
       "hh3cevtModuleRt-ls8": hh3cevtModuleRt_ls8,
       "hh3cevtModuleRt-ls16": hh3cevtModuleRt_ls16,
       "hh3cevtModuleRt-sic-adls2plus-isdn": hh3cevtModuleRt_sic_adls2plus_isdn,
       "hh3cevtModuleRt-sic-adls2plus-pots": hh3cevtModuleRt_sic_adls2plus_pots,
       "hh3cevtModuleRt-ft3": hh3cevtModuleRt_ft3,
       "hh3cevtModuleRt-ce32": hh3cevtModuleRt_ce32,
       "hh3cevtModuleRt-bsv2": hh3cevtModuleRt_bsv2,
       "hh3cevtModuleRt-bsv4": hh3cevtModuleRt_bsv4,
       "hh3cevtModuleRt-RPU": hh3cevtModuleRt_RPU,
       "hh3cevtModuleRt-ERPU": hh3cevtModuleRt_ERPU,
       "hh3cevtModuleRt-SSL": hh3cevtModuleRt_SSL,
       "hh3cevtModuleRt-NSA": hh3cevtModuleRt_NSA,
       "hh3cevtModuleRT-SIC-1GEC": hh3cevtModuleRT_SIC_1GEC,
       "hh3cevtModuleRT-24FSW": hh3cevtModuleRT_24FSW,
       "hh3cevtModuleRT-24FSWP": hh3cevtModuleRT_24FSWP,
       "hh3cevtModuleRT-16FSW": hh3cevtModuleRT_16FSW,
       "hh3cevtModuleRT-16FSWP": hh3cevtModuleRT_16FSWP,
       "hh3cevtModuleRT-1VE1": hh3cevtModuleRT_1VE1,
       "hh3cevtModuleRT-1VT1": hh3cevtModuleRT_1VT1,
       "hh3cevtModuleRT-2VE1": hh3cevtModuleRT_2VE1,
       "hh3cevtModuleRT-2VT1": hh3cevtModuleRT_2VT1,
       "hh3cevtModuleRT-SIC-4FSW": hh3cevtModuleRT_SIC_4FSW,
       "hh3cevtModuleRT-SIC-4FSWP": hh3cevtModuleRT_SIC_4FSWP,
       "hh3cevtModuleRT-DSIC-9FSW": hh3cevtModuleRT_DSIC_9FSW,
       "hh3cevtModuleRT-DSIC-9FSWP": hh3cevtModuleRT_DSIC_9FSWP,
       "hh3cevtModuleRT-SIC-1VE1": hh3cevtModuleRT_SIC_1VE1,
       "hh3cevtModuleRT-SIC-1VT1": hh3cevtModuleRT_SIC_1VT1,
       "hh3cevtModuleRT-VCPM": hh3cevtModuleRT_VCPM,
       "hh3cevtModuleRT-VPM": hh3cevtModuleRT_VPM,
       "hh3cevtModuleRT-VPMA": hh3cevtModuleRT_VPMA,
       "hh3cevtModuleRT-VPMB": hh3cevtModuleRT_VPMB,
       "hh3cevtModuleRT-VPMC": hh3cevtModuleRT_VPMC,
       "hh3cevtModuleRt-fe18-75": hh3cevtModuleRt_fe18_75,
       "hh3cevtModuleRt-fe18-120": hh3cevtModuleRt_fe18_120,
       "hh3cevtModuleRt-ft18": hh3cevtModuleRt_ft18,
       "hh3cevtModuleRt-CF": hh3cevtModuleRt_CF,
       "hh3cevtModuleRt-bsv2-v2": hh3cevtModuleRt_bsv2_v2,
       "hh3cevtModuleRt-e1vi1-v2": hh3cevtModuleRt_e1vi1_v2,
       "hh3cevtModuleRt-e1vi2": hh3cevtModuleRt_e1vi2,
       "hh3cevtModuleRt-t1vi1-v2": hh3cevtModuleRt_t1vi1_v2,
       "hh3cevtModuleRt-t1vi2": hh3cevtModuleRt_t1vi2,
       "hh3cevtModuleRt-osm": hh3cevtModuleRt_osm,
       "hh3cevtModuleRt-sd707": hh3cevtModuleRt_sd707,
       "hh3cevtModuleRt-dm-epri": hh3cevtModuleRt_dm_epri,
       "hh3cevtModuleRt-dm-tpri": hh3cevtModuleRt_dm_tpri,
       "hh3cevtModuleRt-ERPU-H": hh3cevtModuleRt_ERPU_H,
       "hh3cevtModuleRT-SIC-1BSV": hh3cevtModuleRT_SIC_1BSV,
       "hh3cevtModuleRT-SIC-2BSV": hh3cevtModuleRT_SIC_2BSV,
       "hh3cevtModuleRt-gbe8": hh3cevtModuleRt_gbe8,
       "hh3cevtModuleRt-gbe4": hh3cevtModuleRt_gbe4,
       "hh3cevtModuleRt-cpos2-v2": hh3cevtModuleRt_cpos2_v2,
       "hh3cevtModuleRt-cpos1-v2": hh3cevtModuleRt_cpos1_v2,
       "hh3cevtModuleRt-oap": hh3cevtModuleRt_oap,
       "hh3cevtModuleRT-48FSWP": hh3cevtModuleRT_48FSWP,
       "hh3cevtModuleRT-48FSW": hh3cevtModuleRT_48FSW,
       "hh3cevtModuleRT-ASM": hh3cevtModuleRT_ASM,
       "hh3cevtModuleRT-SIC-1FEF": hh3cevtModuleRT_SIC_1FEF,
       "hh3cevtModuleRT-XMIM-24FSW": hh3cevtModuleRT_XMIM_24FSW,
       "hh3cevtModuleRT-WLAN-AG-1RADIO": hh3cevtModuleRT_WLAN_AG_1RADIO,
       "hh3cevtModuleRT-1CE3": hh3cevtModuleRT_1CE3,
       "hh3cevtModuleRT-XMIM-16FSW": hh3cevtModuleRT_XMIM_16FSW,
       "hh3cevtModuleRT-OAPS": hh3cevtModuleRT_OAPS,
       "hh3cevtModuleRT-NAM": hh3cevtModuleRT_NAM,
       "hh3cevtModuleRT-RPE-X1": hh3cevtModuleRT_RPE_X1,
       "hh3cevtModuleRT-FIP-100": hh3cevtModuleRT_FIP_100,
       "hh3cevtModuleRT-FIP-200": hh3cevtModuleRT_FIP_200,
       "hh3cevtModuleRT-SIC-8AS": hh3cevtModuleRT_SIC_8AS,
       "hh3cevtModuleRT-WAAM": hh3cevtModuleRT_WAAM,
       "hh3cevtModuleRt-msp4p-OC3c": hh3cevtModuleRt_msp4p_OC3c,
       "hh3cevtModuleRt-1pos-oc48": hh3cevtModuleRt_1pos_oc48,
       "hh3cevtModuleRt-xgbe": hh3cevtModuleRt_xgbe,
       "hh3cevtModuleRT-EADM": hh3cevtModuleRT_EADM,
       "hh3cevtModuleRT-VCM": hh3cevtModuleRT_VCM,
       "hh3cevtModuleRT-SIC-2FXS1FXO": hh3cevtModuleRT_SIC_2FXS1FXO,
       "hh3cevtModuleRT-8FXS8FXO": hh3cevtModuleRT_8FXS8FXO,
       "hh3cevtModuleRT-16FXS": hh3cevtModuleRT_16FXS,
       "hh3cevtModuleRT-OAPS-ICM": hh3cevtModuleRT_OAPS_ICM,
       "hh3cevtModuleRT-OAP-ICM": hh3cevtModuleRT_OAP_ICM,
       "hh3cevtModuleRT-8fe": hh3cevtModuleRT_8fe,
       "hh3cevtModuleRT-4gbp": hh3cevtModuleRT_4gbp,
       "hh3cevtModuleRT-MPU-G2": hh3cevtModuleRT_MPU_G2,
       "hh3cevtModuleRT-OAPS-OCE": hh3cevtModuleRT_OAPS_OCE,
       "hh3cevtModuleRT-OAP-OCE": hh3cevtModuleRT_OAP_OCE,
       "hh3cevtModuleRT-OAPS-ICE": hh3cevtModuleRT_OAPS_ICE,
       "hh3cevtModuleRT-OAP-ICE": hh3cevtModuleRT_OAP_ICE,
       "hh3cevtModuleRT-SIC-16AS": hh3cevtModuleRT_SIC_16AS,
       "hh3cevtModuleRT-SPE-FWM": hh3cevtModuleRT_SPE_FWM,
       "hh3cevtModuleRT-cls2p": hh3cevtModuleRT_cls2p,
       "hh3cevtModuleRT-cls1p": hh3cevtModuleRT_cls1p,
       "hh3cevtModuleRT-SIC-2E1-F": hh3cevtModuleRT_SIC_2E1_F,
       "hh3cevtModuleRT-SIC-1E1-F-V2": hh3cevtModuleRT_SIC_1E1_F_V2,
       "hh3cevtModuleRT-MCU": hh3cevtModuleRT_MCU,
       "hh3cevtModuleRT-ACU": hh3cevtModuleRT_ACU,
       "hh3cevtModuleRT-1ATM-OC3": hh3cevtModuleRT_1ATM_OC3,
       "hh3cevtModuleRT-RSE-X1": hh3cevtModuleRT_RSE_X1,
       "hh3cevtModuleRT-FIP-210": hh3cevtModuleRT_FIP_210,
       "hh3cevtModuleRT-1expa": hh3cevtModuleRT_1expa,
       "hh3cevtModuleRT-WLAN-SIC-N-1RADIO": hh3cevtModuleRT_WLAN_SIC_N_1RADIO,
       "hh3cevtModuleRT-WLAN-SIC-BG-1RADIO": hh3cevtModuleRT_WLAN_SIC_BG_1RADIO,
       "hh3cevtModuleRT-al2p": hh3cevtModuleRT_al2p,
       "hh3cevtModuleRT-msp2p-OC3c": hh3cevtModuleRT_msp2p_OC3c,
       "hh3cevtModuleRT-8gbp": hh3cevtModuleRT_8gbp,
       "hh3cevtModuleRT-SIC-EPON": hh3cevtModuleRT_SIC_EPON,
       "hh3cevtModuleRT-SIC-3G-GSM-H3": hh3cevtModuleRT_SIC_3G_GSM_H3,
       "hh3cevtModuleRT-msp2p-OC12c": hh3cevtModuleRT_msp2p_OC12c,
       "hh3cevtModuleRt-msp4p-OC12c": hh3cevtModuleRt_msp4p_OC12c,
       "hh3cevtModuleRt-al1p": hh3cevtModuleRt_al1p,
       "hh3cevtModuleRt-OAP-100": hh3cevtModuleRt_OAP_100,
       "hh3cevtModuleRt-FIP-110": hh3cevtModuleRt_FIP_110,
       "hh3cevtModuleRt-OSM-SSM": hh3cevtModuleRt_OSM_SSM,
       "hh3cevtModuleRt-OAP-SSM": hh3cevtModuleRt_OAP_SSM,
       "hh3cevtModuleRt-rs2p": hh3cevtModuleRt_rs2p,
       "hh3cevtModuleRt-SAP-48GBE": hh3cevtModuleRt_SAP_48GBE,
       "hh3cevtModuleRt-SAP-48GBP": hh3cevtModuleRt_SAP_48GBP,
       "hh3cevtModuleRt-SAP-24GBP": hh3cevtModuleRt_SAP_24GBP,
       "hh3cevtModuleRt-SPE-SSL": hh3cevtModuleRt_SPE_SSL,
       "hh3cevtModuleRt-SIC-AUDIO": hh3cevtModuleRt_SIC_AUDIO,
       "hh3cevtModuleRt-FIC-1E1POS-H3": hh3cevtModuleRt_FIC_1E1POS_H3,
       "hh3cevtModuleRt-DSIC-4FXS1FXO": hh3cevtModuleRt_DSIC_4FXS1FXO,
       "hh3cevtModuleRt-FIC-CPOS": hh3cevtModuleRt_FIC_CPOS,
       "hh3cevtModuleRt-DSIC-1SHDSL-8W": hh3cevtModuleRt_DSIC_1SHDSL_8W,
       "hh3cevtModuleRt-SIC-3G-TD": hh3cevtModuleRt_SIC_3G_TD,
       "hh3cevtModuleRt-SIC-3G-CDMA": hh3cevtModuleRt_SIC_3G_CDMA,
       "hh3cevtModuleRt-SIC-3G-HSPA": hh3cevtModuleRt_SIC_3G_HSPA,
       "hh3cevtModuleRt-FIC-OAP-V2": hh3cevtModuleRt_FIC_OAP_V2,
       "hh3cevtModuleRt-MIM-OAP-V2": hh3cevtModuleRt_MIM_OAP_V2,
       "hh3cevtModuleRt-MIM-OAPS-V2": hh3cevtModuleRt_MIM_OAPS_V2,
       "hh3cevtModuleRt-HMIM-1CT3": hh3cevtModuleRt_HMIM_1CT3,
       "hh3cevtModuleRt-HMIM-1CE3": hh3cevtModuleRt_HMIM_1CE3,
       "hh3cevtModuleRt-HMIM-1POS": hh3cevtModuleRt_HMIM_1POS,
       "hh3cevtModuleRt-HMIM-2SAE": hh3cevtModuleRt_HMIM_2SAE,
       "hh3cevtModuleRt-HMIM-4SAE": hh3cevtModuleRt_HMIM_4SAE,
       "hh3cevtModuleRt-HMIM-8SAE": hh3cevtModuleRt_HMIM_8SAE,
       "hh3cevtModuleRt-HMIM-8ASE": hh3cevtModuleRt_HMIM_8ASE,
       "hh3cevtModuleRt-HMIM-16ASE": hh3cevtModuleRt_HMIM_16ASE,
       "hh3cevtModuleRt-HMIM-1E1": hh3cevtModuleRt_HMIM_1E1,
       "hh3cevtModuleRt-HMIM-2E1": hh3cevtModuleRt_HMIM_2E1,
       "hh3cevtModuleRt-HMIM-4E1": hh3cevtModuleRt_HMIM_4E1,
       "hh3cevtModuleRt-HMIM-8E1-75": hh3cevtModuleRt_HMIM_8E1_75,
       "hh3cevtModuleRt-HMIM-1E1-F": hh3cevtModuleRt_HMIM_1E1_F,
       "hh3cevtModuleRt-HMIM-2E1-F": hh3cevtModuleRt_HMIM_2E1_F,
       "hh3cevtModuleRt-HMIM-4E1-F": hh3cevtModuleRt_HMIM_4E1_F,
       "hh3cevtModuleRt-HMIM-8E1-F-75": hh3cevtModuleRt_HMIM_8E1_F_75,
       "hh3cevtModuleRt-HMIM-6AM": hh3cevtModuleRt_HMIM_6AM,
       "hh3cevtModuleRt-HMIM-6FCM": hh3cevtModuleRt_HMIM_6FCM,
       "hh3cevtModuleRt-HMIM-2T1": hh3cevtModuleRt_HMIM_2T1,
       "hh3cevtModuleRt-HMIM-4T1-F": hh3cevtModuleRt_HMIM_4T1_F,
       "hh3cevtModuleRt-HMIM-8T1": hh3cevtModuleRt_HMIM_8T1,
       "hh3cevtModuleRt-HMIM-8T1-F": hh3cevtModuleRt_HMIM_8T1_F,
       "hh3cevtModuleRt-HMIM-1VE1": hh3cevtModuleRt_HMIM_1VE1,
       "hh3cevtModuleRt-HMIM-1VT1": hh3cevtModuleRt_HMIM_1VT1,
       "hh3cevtModuleRt-HMIM-2VE1": hh3cevtModuleRt_HMIM_2VE1,
       "hh3cevtModuleRt-HMIM-2VT1": hh3cevtModuleRt_HMIM_2VT1,
       "hh3cevtModuleRt-HMIM-8FXS8FXO": hh3cevtModuleRt_HMIM_8FXS8FXO,
       "hh3cevtModuleRt-HMIM-16FXS": hh3cevtModuleRt_HMIM_16FXS,
       "hh3cevtModuleRt-HMIM-4FXS": hh3cevtModuleRt_HMIM_4FXS,
       "hh3cevtModuleRt-HMIM-4FXO": hh3cevtModuleRt_HMIM_4FXO,
       "hh3cevtModuleRt-HMIM-4EM": hh3cevtModuleRt_HMIM_4EM,
       "hh3cevtModuleRt-HMIM-4BSV": hh3cevtModuleRt_HMIM_4BSV,
       "hh3cevtModuleRt-SIC-CNDE": hh3cevtModuleRt_SIC_CNDE,
       "hh3cevtModuleRt-ESM-CNDE": hh3cevtModuleRt_ESM_CNDE,
       "hh3cevtModuleRt-ESM-CNDE-M": hh3cevtModuleRt_ESM_CNDE_M,
       "hh3cevtModuleRt-SR6602-X1": hh3cevtModuleRt_SR6602_X1,
       "hh3cevtModuleRt-SR6602-X2": hh3cevtModuleRt_SR6602_X2,
       "hh3cevtModuleRt-MCP-X1": hh3cevtModuleRt_MCP_X1,
       "hh3cevtModuleRt-MCP-X2": hh3cevtModuleRt_MCP_X2,
       "hh3cevtModuleRt-FIP-10": hh3cevtModuleRt_FIP_10,
       "hh3cevtModuleRt-FIP-20": hh3cevtModuleRt_FIP_20,
       "hh3cevtModuleRt-RSE-X2": hh3cevtModuleRt_RSE_X2,
       "hh3cevtModuleRt-FIP-600": hh3cevtModuleRt_FIP_600,
       "hh3cevtModuleRt-SAP-4EXP": hh3cevtModuleRt_SAP_4EXP,
       "hh3cevtModuleRt-SFE-X1": hh3cevtModuleRt_SFE_X1,
       "hh3cevtModuleRt-SFE-A1": hh3cevtModuleRt_SFE_A1,
       "hh3cevtModuleRt-HMIM-24GSW": hh3cevtModuleRt_HMIM_24GSW,
       "hh3cevtModuleRt-HMIM-24GSWP": hh3cevtModuleRt_HMIM_24GSWP,
       "hh3cevtModuleRt-MPU100": hh3cevtModuleRt_MPU100,
       "hh3cevtModuleRt-SPU100": hh3cevtModuleRt_SPU100,
       "hh3cevtModuleRt-SPU200": hh3cevtModuleRt_SPU200,
       "hh3cevtModuleRt-WLAN-N-1RADIO": hh3cevtModuleRt_WLAN_N_1RADIO,
       "hh3cevtModuleRt-3G-CDMA": hh3cevtModuleRt_3G_CDMA,
       "hh3cevtModuleRt-3G-WCDMA": hh3cevtModuleRt_3G_WCDMA,
       "hh3cevtModuleRt-3G-HSPAPLUS": hh3cevtModuleRt_3G_HSPAPLUS,
       "hh3cevtModuleRt-VPM-128": hh3cevtModuleRt_VPM_128,
       "hh3cevtModuleRt-VPM-256": hh3cevtModuleRt_VPM_256,
       "hh3cevtModuleRt-VPM-512": hh3cevtModuleRt_VPM_512,
       "hh3cevtModuleRt-HMIM-8GEE": hh3cevtModuleRt_HMIM_8GEE,
       "hh3cevtModuleRt-HMIM-4GEE": hh3cevtModuleRt_HMIM_4GEE,
       "hh3cevtModuleRt-HMIM-2GEE": hh3cevtModuleRt_HMIM_2GEE,
       "hh3cevtModuleRt-HMIM-8GEF": hh3cevtModuleRt_HMIM_8GEF,
       "hh3cevtModuleRt-HMIM-4GEF": hh3cevtModuleRt_HMIM_4GEF,
       "hh3cevtModuleRt-HMIM-2GEF": hh3cevtModuleRt_HMIM_2GEF,
       "hh3cevtModuleRt-SPU300": hh3cevtModuleRt_SPU300,
       "hh3cevtModuleRt-HMIM-1CPOS": hh3cevtModuleRt_HMIM_1CPOS,
       "hh3cevtModuleRt-HMIM-2CPOS": hh3cevtModuleRt_HMIM_2CPOS,
       "hh3cevtModuleRt-SPU100-5080": hh3cevtModuleRt_SPU100_5080,
       "hh3cevtModuleRt-SPU200-5080": hh3cevtModuleRt_SPU200_5080,
       "hh3cevtModuleRt-SPU300-5080": hh3cevtModuleRt_SPU300_5080,
       "hh3cevtModuleRt-4G-LTE-Verizon": hh3cevtModuleRt_4G_LTE_Verizon,
       "hh3cevtModuleRt-4G-LTE-Global": hh3cevtModuleRt_4G_LTE_Global,
       "hh3cevtModuleRt-HMIM-1ATM-OC3": hh3cevtModuleRt_HMIM_1ATM_OC3,
       "hh3cevtModuleRt-SIC-1E1-V2": hh3cevtModuleRt_SIC_1E1_V2,
       "hh3cevtModuleRt-FIP-300": hh3cevtModuleRt_FIP_300,
       "hh3cevtModuleRt-FIP-310": hh3cevtModuleRt_FIP_310,
       "hh3cevtModuleRt-TS8P": hh3cevtModuleRt_TS8P,
       "hh3cevtModuleRt-4G4P": hh3cevtModuleRt_4G4P,
       "hh3cevtModuleRt-SIC-4G-LTE-V": hh3cevtModuleRt_SIC_4G_LTE_V,
       "hh3cevtModuleRt-SIC-4G-LTE-A": hh3cevtModuleRt_SIC_4G_LTE_A,
       "hh3cevtModuleRt-SIC-4G-LTE-G": hh3cevtModuleRt_SIC_4G_LTE_G,
       "hh3cevtModuleRt-SIC-2SAE": hh3cevtModuleRt_SIC_2SAE,
       "hh3cevtModuleRt-SIC-4SAE": hh3cevtModuleRt_SIC_4SAE,
       "hh3cevtModuleRt-HMIM-OAP": hh3cevtModuleRt_HMIM_OAP,
       "hh3cevtModuleRt-HMIM-8GSW": hh3cevtModuleRt_HMIM_8GSW,
       "hh3cevtModuleRt-IPU": hh3cevtModuleRt_IPU,
       "hh3cevtModuleRt-MIM2GEBE-PCIE": hh3cevtModuleRt_MIM2GEBE_PCIE,
       "hh3cevtModuleRt-HIM12GE-PCIE": hh3cevtModuleRt_HIM12GE_PCIE,
       "hh3cevtModuleRt-HIM2XGE-PCIE": hh3cevtModuleRt_HIM2XGE_PCIE,
       "hh3cevtModuleRt-IPU-T1000-M": hh3cevtModuleRt_IPU_T1000_M,
       "hh3cevtModuleRt-IPU-GX4C": hh3cevtModuleRt_IPU_GX4C,
       "hh3cevtModuleRt-IPU-GT4C": hh3cevtModuleRt_IPU_GT4C,
       "hh3cevtModuleRt-RPU-IAG2000-A": hh3cevtModuleRt_RPU_IAG2000_A,
       "hh3cevtModuleRt-RPU-AFD1000-A": hh3cevtModuleRt_RPU_AFD1000_A,
       "hh3cevtModuleRt-RPU-F5000-A": hh3cevtModuleRt_RPU_F5000_A,
       "hh3cevtModuleRt-ACG-8800S3-MPU": hh3cevtModuleRt_ACG_8800S3_MPU,
       "hh3cevtModuleRt-T5000S3-MPU": hh3cevtModuleRt_T5000S3_MPU,
       "hh3cevtModuleRt-NS21S2MSPB0": hh3cevtModuleRt_NS21S2MSPB0,
       "hh3cevtModuleRt-NS11S2MSPB0": hh3cevtModuleRt_NS11S2MSPB0,
       "hh3cevtModuleRt-NSQ1WLAN": hh3cevtModuleRt_NSQ1WLAN,
       "hh3cevtModuleRt-NSQ1GP4U0": hh3cevtModuleRt_NSQ1GP4U0,
       "hh3cevtModuleRt-NSQ1GP8C40": hh3cevtModuleRt_NSQ1GP8C40,
       "hh3cevtModuleRt-NSQ1XS2U0": hh3cevtModuleRt_NSQ1XS2U0,
       "hh3cevtModuleRt-NSQ1G24XS60": hh3cevtModuleRt_NSQ1G24XS60,
       "hh3cevtModuleRt-NSQ1TGX4EA0": hh3cevtModuleRt_NSQ1TGX4EA0,
       "hh3cevtModuleRt-NSQ1FAB08D0": hh3cevtModuleRt_NSQ1FAB08D0,
       "hh3cevtModuleRt-NSQ1TGS32SF0": hh3cevtModuleRt_NSQ1TGS32SF0,
       "hh3cevtModuleRt-NSQ1QGS4SF0": hh3cevtModuleRt_NSQ1QGS4SF0,
       "hh3cevtModuleRt-NSQ1GP24TXEA0": hh3cevtModuleRt_NSQ1GP24TXEA0,
       "hh3cevtModuleRt-NSQ1GP48EB0": hh3cevtModuleRt_NSQ1GP48EB0,
       "hh3cevtModuleRt-NSQ1FWCEA0": hh3cevtModuleRt_NSQ1FWCEA0,
       "hh3cevtModuleRt-NSQ1GT48EA0": hh3cevtModuleRt_NSQ1GT48EA0,
       "hh3cevtModuleRt-NSQ1TGS8EA0": hh3cevtModuleRt_NSQ1TGS8EA0,
       "hh3cevtModuleRt-NSQ1FAB04B0": hh3cevtModuleRt_NSQ1FAB04B0,
       "hh3cevtModuleRt-NSQ1FAB12D0": hh3cevtModuleRt_NSQ1FAB12D0,
       "hh3cevtModuleRt-NSQ1SUPB0": hh3cevtModuleRt_NSQ1SUPB0,
       "hh3cevtModuleRt-VFW1000": hh3cevtModuleRt_VFW1000,
       "hh3cevtModuleRt-NSQ1CGC2SE0": hh3cevtModuleRt_NSQ1CGC2SE0,
       "hh3cevtModuleRt-VLB1000": hh3cevtModuleRt_VLB1000,
       "hh3cevtModuleRt-NSQM1GT4PFC": hh3cevtModuleRt_NSQM1GT4PFC,
       "hh3cevtModuleRt-NSQM1FWDFG0": hh3cevtModuleRt_NSQM1FWDFG0,
       "hh3cevtModuleRt-NSQM1NATDFGA0": hh3cevtModuleRt_NSQM1NATDFGA0,
       "hh3cevtModuleRt-NSQM1NATDFGB0": hh3cevtModuleRt_NSQM1NATDFGB0,
       "hh3cevtModuleRt-VFW2000": hh3cevtModuleRt_VFW2000,
       "hh3cevtModuleRt-VLB2000": hh3cevtModuleRt_VLB2000,
       "hh3cevtModuleRt-NSQM1IPSDFG0": hh3cevtModuleRt_NSQM1IPSDFG0,
       "hh3cevtModuleRt-NSQM1FWDFGB0": hh3cevtModuleRt_NSQM1FWDFGB0,
       "hh3cevtModuleRt-NSQM1FWDFGC0": hh3cevtModuleRt_NSQM1FWDFGC0,
       "hh3cevtModuleRt-NSQM1FWDFGA1": hh3cevtModuleRt_NSQM1FWDFGA1,
       "hh3cevtModuleRt-NSQM1FWDFGB1": hh3cevtModuleRt_NSQM1FWDFGB1,
       "hh3cevtModuleRt-NSQM1FWDFGC1": hh3cevtModuleRt_NSQM1FWDFGC1,
       "hh3cevtModuleRt-NSQM1FWDFGD1": hh3cevtModuleRt_NSQM1FWDFGD1,
       "hh3cevtModuleRt-NSQM1SUPC0": hh3cevtModuleRt_NSQM1SUPC0,
       "hh3cevtModuleRt-NSQM1TG4FBA": hh3cevtModuleRt_NSQM1TG4FBA,
       "hh3cevtModuleRt-NSQM1GP4FBA": hh3cevtModuleRt_NSQM1GP4FBA,
       "hh3cevtModuleRt-NSQM2MPUC0": hh3cevtModuleRt_NSQM2MPUC0,
       "hh3cevtModuleRt-NSQM2TGS16SF0": hh3cevtModuleRt_NSQM2TGS16SF0,
       "hh3cevtModuleRt-NSQM2QGS4SC0": hh3cevtModuleRt_NSQM2QGS4SC0,
       "hh3cevtModuleRt-NSQM2GP24TSSC0": hh3cevtModuleRt_NSQM2GP24TSSC0,
       "hh3cevtModuleRt-NSQM2FWDSC0": hh3cevtModuleRt_NSQM2FWDSC0,
       "hh3cevtModuleRt-NSQM1ADEDFGA0": hh3cevtModuleRt_NSQM1ADEDFGA0,
       "hh3cevtModuleRt-NSQM2FWDSCA0": hh3cevtModuleRt_NSQM2FWDSCA0,
       "hh3cevtModuleRt-NSQM1TGS32QSSG0": hh3cevtModuleRt_NSQM1TGS32QSSG0,
       "hh3cevtModuleRt-NSQM1GT4PFCA": hh3cevtModuleRt_NSQM1GT4PFCA,
       "hh3cevtModuleRt-NSQM1TG8A": hh3cevtModuleRt_NSQM1TG8A,
       "hh3cevtModuleRt-NSQM1QG2A": hh3cevtModuleRt_NSQM1QG2A,
       "hh3cevtModuleRt-NSQM1GT8A": hh3cevtModuleRt_NSQM1GT8A,
       "hh3cevtModuleRt-NSQM1GP8A": hh3cevtModuleRt_NSQM1GP8A,
       "hh3cevtModuleRt-NSQM1MBFE0": hh3cevtModuleRt_NSQM1MBFE0,
       "hh3cevtModuleRt-NSQM2MBFD0": hh3cevtModuleRt_NSQM2MBFD0,
       "hh3cevtModuleRt-NSQM2QG2TG8GP40": hh3cevtModuleRt_NSQM2QG2TG8GP40,
       "hh3cevtModuleRt-NSQM2QG4GP40": hh3cevtModuleRt_NSQM2QG4GP40,
       "hh3cevtModuleRt-NSQM2TG16GP40": hh3cevtModuleRt_NSQM2TG16GP40,
       "hh3cevtModuleRt-NSQM1CGQ20": hh3cevtModuleRt_NSQM1CGQ20,
       "hh3cevtModuleRt-NSQM2FWDFG0": hh3cevtModuleRt_NSQM2FWDFG0,
       "hh3cevtModuleRt-NSQM2TMPUC0": hh3cevtModuleRt_NSQM2TMPUC0,
       "hh3cevtModuleRt-NSQM2IPSDSCA0": hh3cevtModuleRt_NSQM2IPSDSCA0,
       "hh3cevtModuleRt-NSQM2AC1400": hh3cevtModuleRt_NSQM2AC1400,
       "hh3cevtModuleRt-NSQM2DC1400": hh3cevtModuleRt_NSQM2DC1400,
       "hh3cevtModuleRt-NSQM1F1KGM0": hh3cevtModuleRt_NSQM1F1KGM0,
       "hh3cevtModuleRt-NSQM1F1KGM0-context": hh3cevtModuleRt_NSQM1F1KGM0_context,
       "hh3cevtModuleRt-NSQM1F5KGM0": hh3cevtModuleRt_NSQM1F5KGM0,
       "hh3cevtModuleRt-NSQM1F5KGM0-context": hh3cevtModuleRt_NSQM1F5KGM0_context,
       "hh3cevtModuleRt-NSQM2QG2GP40": hh3cevtModuleRt_NSQM2QG2GP40,
       "hh3cevtModuleRt-NSQM2TG8GP40": hh3cevtModuleRt_NSQM2TG8GP40,
       "hh3cevtModuleRt-NSQM2ADEDSCA0": hh3cevtModuleRt_NSQM2ADEDSCA0,
       "hh3cevtModuleRt-NSQM2IPSDSCB0": hh3cevtModuleRt_NSQM2IPSDSCB0,
       "hh3cevtModuleRt-NSQM1G4XS4": hh3cevtModuleRt_NSQM1G4XS4,
       "hh3cevtModuleRt-NSUM1GT4PFCA": hh3cevtModuleRt_NSUM1GT4PFCA,
       "hh3cevtModuleRt-NSUM1TG8A": hh3cevtModuleRt_NSUM1TG8A,
       "hh3cevtModuleRt-NSUM1QG2A": hh3cevtModuleRt_NSUM1QG2A,
       "hh3cevtModuleRt-NSUM1GT8A": hh3cevtModuleRt_NSUM1GT8A,
       "hh3cevtModuleRt-NSUM1GP8A": hh3cevtModuleRt_NSUM1GP8A,
       "hh3cevtModuleRt-NSQM2MPUD0": hh3cevtModuleRt_NSQM2MPUD0,
       "hh3cevtModuleRt-NSQM1GMDSCA1": hh3cevtModuleRt_NSQM1GMDSCA1,
       "hh3cevtModuleRt-NSQM1MPULA": hh3cevtModuleRt_NSQM1MPULA,
       "hh3cevtModuleRt-NSQM1MPULA2": hh3cevtModuleRt_NSQM1MPULA2,
       "hh3cevtModuleRt-NSQM1GT8A2": hh3cevtModuleRt_NSQM1GT8A2,
       "hh3cevtModuleRt-NSQM1GP4TG4A2": hh3cevtModuleRt_NSQM1GP4TG4A2,
       "hh3cevtModuleRt-NSQM1GP2TG6A2": hh3cevtModuleRt_NSQM1GP2TG6A2,
       "hh3cevtModuleRt-NSQM1TG4FBA7": hh3cevtModuleRt_NSQM1TG4FBA7,
       "hh3cevtModuleRt-NSQM1F1KGMB": hh3cevtModuleRt_NSQM1F1KGMB,
       "hh3cevtModuleRt-NSQM1F1KGMC": hh3cevtModuleRt_NSQM1F1KGMC,
       "hh3cevtModuleRt-NSQM1F5KGMC": hh3cevtModuleRt_NSQM1F5KGMC,
       "hh3cevtModuleRt-NSQM5SUP08H0": hh3cevtModuleRt_NSQM5SUP08H0,
       "hh3cevtModuleRt-NSQM5SUP16C0": hh3cevtModuleRt_NSQM5SUP16C0,
       "hh3cevtModuleRt-NS-FWEMPA0": hh3cevtModuleRt_NS_FWEMPA0,
       "hh3cevtModuleRt-NSQM5MBSHA0": hh3cevtModuleRt_NSQM5MBSHA0,
       "hh3cevtModuleRt-NS-C600-CGQ6A0": hh3cevtModuleRt_NS_C600_CGQ6A0,
       "hh3cevtModuleRt-NS-C300-CGQ2TG16A0": hh3cevtModuleRt_NS_C300_CGQ2TG16A0,
       "hh3cevtModuleRt-NS-C300-TG24A0": hh3cevtModuleRt_NS_C300_TG24A0,
       "hh3cevtModuleRt-NS-C300-QG4TG16A0": hh3cevtModuleRt_NS_C300_QG4TG16A0,
       "hh3cevtModuleRt-NSQM5FAB08A0": hh3cevtModuleRt_NSQM5FAB08A0,
       "hh3cevtModuleRt-NSQM5FAB16A0": hh3cevtModuleRt_NSQM5FAB16A0,
       "hh3cevtModuleRt-NSQM5SL16UA0": hh3cevtModuleRt_NSQM5SL16UA0,
       "hh3cevtModuleRt-NSQM5SL16LA0": hh3cevtModuleRt_NSQM5SL16LA0,
       "hh3cevtModuleRt-NSQM2MPU12E0": hh3cevtModuleRt_NSQM2MPU12E0,
       "hh3cevtModuleRt-NSQM2MBFEA0": hh3cevtModuleRt_NSQM2MBFEA0,
       "hh3cevtModuleRt-NSQM2AC2500HD": hh3cevtModuleRt_NSQM2AC2500HD,
       "hh3cevtModuleRt-NSQM2DC2500": hh3cevtModuleRt_NSQM2DC2500,
       "hh3cevtModuleRt-NSQM1HTIMGMG2A": hh3cevtModuleRt_NSQM1HTIMGMG2A,
       "hh3cevtModuleRt-NSQM1HTIMGMG2B": hh3cevtModuleRt_NSQM1HTIMGMG2B,
       "hh3cevtModuleRt-NSQM2V6DSCA0": hh3cevtModuleRt_NSQM2V6DSCA0,
       "hh3cevtModuleRt-NSQM1AFC2000GDFGA0": hh3cevtModuleRt_NSQM1AFC2000GDFGA0,
       "hh3cevtModuleRt-NSQM2AFC2000GDFGA0": hh3cevtModuleRt_NSQM2AFC2000GDFGA0,
       "hh3cevtModuleRt-NSQM1FWDFGD1-Z": hh3cevtModuleRt_NSQM1FWDFGD1_Z,
       "hh3cevtModuleRt-NSQM1FAB12D0": hh3cevtModuleRt_NSQM1FAB12D0,
       "hh3cevtModuleRt-NSQM1MBFEA0": hh3cevtModuleRt_NSQM1MBFEA0,
       "hh3cevtModuleRt-NSQM2TG16GP40-Z": hh3cevtModuleRt_NSQM2TG16GP40_Z,
       "hh3cevtModuleRt-NSQM2QG4GP40-Z": hh3cevtModuleRt_NSQM2QG4GP40_Z,
       "hh3cevtModuleRt-NSQM1CGQ20-Z": hh3cevtModuleRt_NSQM1CGQ20_Z,
       "hh3cevtModuleRt-NSQM1TGS32QSSG0-Z": hh3cevtModuleRt_NSQM1TGS32QSSG0_Z,
       "hh3cevtModuleRt-NSQM1AFC2000GDFGA0-Z": hh3cevtModuleRt_NSQM1AFC2000GDFGA0_Z,
       "hh3cevtModuleRt-NSQM5AIASKA1": hh3cevtModuleRt_NSQM5AIASKA1,
       "hh3cevtModuleRt-NSQM1FWEFGA0": hh3cevtModuleRt_NSQM1FWEFGA0,
       "hh3cevtModuleRt-NS-ADEEMPA0": hh3cevtModuleRt_NS_ADEEMPA0,
       "hh3cevtModuleRt-NSQM2QG2TG8A0": hh3cevtModuleRt_NSQM2QG2TG8A0,
       "hh3cevtModuleRt-NS-ADEEMPB0": hh3cevtModuleRt_NS_ADEEMPB0,
       "hh3cevtModuleRt-NSQM2TG16A0": hh3cevtModuleRt_NSQM2TG16A0,
       "hh3cevtModuleRt-NSQM6SUP04A0": hh3cevtModuleRt_NSQM6SUP04A0,
       "hh3cevtModuleRt-NSQM2QG4A0": hh3cevtModuleRt_NSQM2QG4A0,
       "hh3cevtModuleRt-NSQM1SUPD0": hh3cevtModuleRt_NSQM1SUPD0,
       "hh3cevtModuleRt-NSQM1FAB08E0": hh3cevtModuleRt_NSQM1FAB08E0,
       "hh3cevtModuleRt-NSQM1CGQ4TG24SHA0": hh3cevtModuleRt_NSQM1CGQ4TG24SHA0,
       "hh3cevtModuleRt-NSQM2MPUF0": hh3cevtModuleRt_NSQM2MPUF0,
       "hh3cevtModuleRt-NSQM2FWDFGD0": hh3cevtModuleRt_NSQM2FWDFGD0,
       "hh3cevtModuleRt-NSQM2MBFDB0": hh3cevtModuleRt_NSQM2MBFDB0,
       "hh3cevtModuleRt-NSQM2QG2TG8GP4B0": hh3cevtModuleRt_NSQM2QG2TG8GP4B0,
       "hh3cevtModuleRt-NSQM2FAN08B": hh3cevtModuleRt_NSQM2FAN08B,
       "hh3cevtModuleRt-NSQM5TSUP08A0": hh3cevtModuleRt_NSQM5TSUP08A0,
       "hh3cevtModuleRt-NSQM5TIPSEMPA0": hh3cevtModuleRt_NSQM5TIPSEMPA0,
       "hh3cevtModuleRt-NSQM5AIASKB1": hh3cevtModuleRt_NSQM5AIASKB1,
       "hh3cevtModuleRt-NSQM1G4XS4-Z": hh3cevtModuleRt_NSQM1G4XS4_Z,
       "hh3cevtModuleRt-NSQM5TIPSEMPB0": hh3cevtModuleRt_NSQM5TIPSEMPB0,
       "hh3cevtModuleRt-NSQM5SUP04A1": hh3cevtModuleRt_NSQM5SUP04A1,
       "hh3cevtModuleRt-NS-FWEMPB1": hh3cevtModuleRt_NS_FWEMPB1,
       "hh3cevtModuleRt-NS-AFC2000EMPB1": hh3cevtModuleRt_NS_AFC2000EMPB1,
       "hh3cevtModuleRt-NS-AFC2000EMPA1": hh3cevtModuleRt_NS_AFC2000EMPA1,
       "hh3cevtModuleRt-NS-ADEEMPC0": hh3cevtModuleRt_NS_ADEEMPC0,
       "hh3cevtModuleRt-NSQM1CGQ6SH0": hh3cevtModuleRt_NSQM1CGQ6SH0,
       "hh3cevtModuleRt-NSQM7SUPB0": hh3cevtModuleRt_NSQM7SUPB0,
       "hh3cevtModuleRt-NSQM7FAB06A0": hh3cevtModuleRt_NSQM7FAB06A0,
       "hh3cevtModuleRt-NSQM7SUPA0": hh3cevtModuleRt_NSQM7SUPA0,
       "hh3cevtModuleRt-NSQM7FAB10A0": hh3cevtModuleRt_NSQM7FAB10A0,
       "hh3cevtModuleRt-FAN-120B-3-A10": hh3cevtModuleRt_FAN_120B_3_A10,
       "hh3cevtModuleRt-NSQM7MBSHB0": hh3cevtModuleRt_NSQM7MBSHB0,
       "hh3cevtModuleRt-NSQM7MBSHA0": hh3cevtModuleRt_NSQM7MBSHA0,
       "hh3cevtModuleRt-NS-FWFFGA0": hh3cevtModuleRt_NS_FWFFGA0,
       "hh3cevtModuleRt-NS-FWFFGB0": hh3cevtModuleRt_NS_FWFFGB0,
       "hh3cevtModuleRt-VG-8fxs": hh3cevtModuleRt_VG_8fxs,
       "hh3cevtModuleRt-VG-24fxs": hh3cevtModuleRt_VG_24fxs,
       "hh3cevtModuleRt-VG-24fxs24fxo": hh3cevtModuleRt_VG_24fxs24fxo,
       "hh3cevtModuleRt-VG-MPU": hh3cevtModuleRt_VG_MPU,
       "hh3cevtModuleRt-MIM-VCX-CONNECT-P-3C": hh3cevtModuleRt_MIM_VCX_CONNECT_P_3C,
       "hh3cevtModuleRt-MIM-VCX-CONNECT-S-3C": hh3cevtModuleRt_MIM_VCX_CONNECT_S_3C,
       "hh3cevtModuleRt-MIM-VCX-3C": hh3cevtModuleRt_MIM_VCX_3C,
       "hh3cevtModuleRt-VNIC-VMXNET3": hh3cevtModuleRt_VNIC_VMXNET3,
       "hh3cevtModuleRt-VNIC-E1000": hh3cevtModuleRt_VNIC_E1000,
       "hh3cevtModuleRt-VNIC-VIRTIO": hh3cevtModuleRt_VNIC_VIRTIO,
       "hh3cevtModuleRt-VNIC-RTL8139": hh3cevtModuleRt_VNIC_RTL8139,
       "hh3cevtModuleRt-VNIC-IXGBEVF": hh3cevtModuleRt_VNIC_IXGBEVF,
       "hh3cevtModuleRt-IXGBE-2XGE": hh3cevtModuleRt_IXGBE_2XGE,
       "hh3cevtModuleRt-TG3-4GE": hh3cevtModuleRt_TG3_4GE,
       "hh3cevtModuleRt-MPUV16": hh3cevtModuleRt_MPUV16,
       "hh3cevtModuleRt-MPUP6": hh3cevtModuleRt_MPUP6,
       "hh3cevtModuleRt-IGB-1GE": hh3cevtModuleRt_IGB_1GE,
       "hh3cevtModuleRt-IGB-2GE": hh3cevtModuleRt_IGB_2GE,
       "hh3cevtModuleRt-IGB-4GE": hh3cevtModuleRt_IGB_4GE,
       "hh3cevtModuleRt-VLNS1000": hh3cevtModuleRt_VLNS1000,
       "hh3cevtModuleRt-VLNS2000": hh3cevtModuleRt_VLNS2000,
       "hh3cevtModuleRt-NS-MIM-GP4A2": hh3cevtModuleRt_NS_MIM_GP4A2,
       "hh3cevtModuleRt-NS-MIM-GT4PFCA2": hh3cevtModuleRt_NS_MIM_GT4PFCA2,
       "hh3cevtModuleRt-NS-NIM-TG6A2": hh3cevtModuleRt_NS_NIM_TG6A2,
       "hh3cevtModuleRt-NS-SIM-GT4PFCA2": hh3cevtModuleRt_NS_SIM_GT4PFCA2,
       "hh3cevtModuleRt-NS-NIM-TG6A-Z": hh3cevtModuleRt_NS_NIM_TG6A_Z,
       "hh3cevtModuleRt-SIC-4GSW": hh3cevtModuleRt_SIC_4GSW,
       "hh3cevtModuleRt-SIC-4GSWP": hh3cevtModuleRt_SIC_4GSWP,
       "hh3cevtModuleRt-SIC-1GEC-V2": hh3cevtModuleRt_SIC_1GEC_V2,
       "hh3cevtModuleRt-4G-LTE-ATT": hh3cevtModuleRt_4G_LTE_ATT,
       "hh3cevtModuleRt-4G-TD-LTE": hh3cevtModuleRt_4G_TD_LTE,
       "hh3cevtModuleRt-FIP-240": hh3cevtModuleRt_FIP_240,
       "hh3cevtModuleRt-8GBP-V2": hh3cevtModuleRt_8GBP_V2,
       "hh3cevtModuleRt-HMIM-CNDE": hh3cevtModuleRt_HMIM_CNDE,
       "hh3cevtModuleRt-4G-LTE-Mobile": hh3cevtModuleRt_4G_LTE_Mobile,
       "hh3cevtModuleRt-SIC-4G-LTE-M": hh3cevtModuleRt_SIC_4G_LTE_M,
       "hh3cevtModuleRt-CRSE-X3": hh3cevtModuleRt_CRSE_X3,
       "hh3cevtModuleRt-CFIP-300": hh3cevtModuleRt_CFIP_300,
       "hh3cevtModuleRt-CFIP-310": hh3cevtModuleRt_CFIP_310,
       "hh3cevtModuleRt-CSAP-4EXP": hh3cevtModuleRt_CSAP_4EXP,
       "hh3cevtModuleRt-RSU": hh3cevtModuleRt_RSU,
       "hh3cevtModuleRt-CFIP-610": hh3cevtModuleRt_CFIP_610,
       "hh3cevtModuleRt-2EXP": hh3cevtModuleRt_2EXP,
       "hh3cevtModuleRt-16GBP": hh3cevtModuleRt_16GBP,
       "hh3cevtModuleRt-CFIP-240": hh3cevtModuleRt_CFIP_240,
       "hh3cevtModuleRt-RSE-X3": hh3cevtModuleRt_RSE_X3,
       "hh3cevtModuleRt-SAP-8EXP": hh3cevtModuleRt_SAP_8EXP,
       "hh3cevtModuleRt-SAP-16EXP": hh3cevtModuleRt_SAP_16EXP,
       "hh3cevtModuleRt-PU1P": hh3cevtModuleRt_PU1P,
       "hh3cevtModuleRt-RSU100": hh3cevtModuleRt_RSU100,
       "hh3cevtModuleRt-SAP-2QGP": hh3cevtModuleRt_SAP_2QGP,
       "hh3cevtModuleRt-CSFE-X1": hh3cevtModuleRt_CSFE_X1,
       "hh3cevtModuleRt-RIC-4GEE": hh3cevtModuleRt_RIC_4GEE,
       "hh3cevtModuleRt-RIC-4GEF": hh3cevtModuleRt_RIC_4GEF,
       "hh3cevtModuleRt-RIC-8GEE": hh3cevtModuleRt_RIC_8GEE,
       "hh3cevtModuleRt-RIC-8GEF": hh3cevtModuleRt_RIC_8GEF,
       "hh3cevtModuleRt-RIC-1XGEF": hh3cevtModuleRt_RIC_1XGEF,
       "hh3cevtModuleRt-HMIM-1E1POS": hh3cevtModuleRt_HMIM_1E1POS,
       "hh3cevtModuleRt-DHMIM-1DM": hh3cevtModuleRt_DHMIM_1DM,
       "hh3cevtModuleRt-DHMIM-1E1POS1DM": hh3cevtModuleRt_DHMIM_1E1POS1DM,
       "hh3cevtModuleRt-RPE-X3": hh3cevtModuleRt_RPE_X3,
       "hh3cevtModuleRt-CRPE-X3": hh3cevtModuleRt_CRPE_X3,
       "hh3cevtModuleRt-SAP-28GE": hh3cevtModuleRt_SAP_28GE,
       "hh3cevtModuleRt-SAP-20GE2XP": hh3cevtModuleRt_SAP_20GE2XP,
       "hh3cevtModuleRt-SFE-L1": hh3cevtModuleRt_SFE_L1,
       "hh3cevtModuleRt-FIP-640": hh3cevtModuleRt_FIP_640,
       "hh3cevtModuleRt-HMIM-8GSWF": hh3cevtModuleRt_HMIM_8GSWF,
       "hh3cevtModuleRt-HMIM-8E1T1": hh3cevtModuleRt_HMIM_8E1T1,
       "hh3cevtModuleRt-HMIM-4E1T1": hh3cevtModuleRt_HMIM_4E1T1,
       "hh3cevtModuleRt-HMIM-2E1T1": hh3cevtModuleRt_HMIM_2E1T1,
       "hh3cevtModuleRt-HMIM-8E1T1-F": hh3cevtModuleRt_HMIM_8E1T1_F,
       "hh3cevtModuleRt-HMIM-4E1T1-F": hh3cevtModuleRt_HMIM_4E1T1_F,
       "hh3cevtModuleRt-HMIM-2E1T1-F": hh3cevtModuleRt_HMIM_2E1T1_F,
       "hh3cevtModuleRt-SIC-3G-HSPA-V2": hh3cevtModuleRt_SIC_3G_HSPA_V2,
       "hh3cevtModuleRt-SIC-4GSWF": hh3cevtModuleRt_SIC_4GSWF,
       "hh3cevtModuleRt-SIC-4G-LTE-G-V2": hh3cevtModuleRt_SIC_4G_LTE_G_V2,
       "hh3cevtModuleRt-SIC-4G-LTE-A-V2": hh3cevtModuleRt_SIC_4G_LTE_A_V2,
       "hh3cevtModuleRt-SIC-4G-LTE-V-V2": hh3cevtModuleRt_SIC_4G_LTE_V_V2,
       "hh3cevtModuleRt-MPU60": hh3cevtModuleRt_MPU60,
       "hh3cevtModuleRt-SPU": hh3cevtModuleRt_SPU,
       "hh3cevtModuleRt-SIC-1VE1T1": hh3cevtModuleRt_SIC_1VE1T1,
       "hh3cevtModuleRt-CFIP-700": hh3cevtModuleRt_CFIP_700,
       "hh3cevtModuleRt-HIM-20GBP-H3": hh3cevtModuleRt_HIM_20GBP_H3,
       "hh3cevtModuleRt-HIM-4EXP-H3": hh3cevtModuleRt_HIM_4EXP_H3,
       "hh3cevtModuleRt-HIM-2EXP-H3": hh3cevtModuleRt_HIM_2EXP_H3,
       "hh3cevtModuleRt-HIM-8GBE-V3": hh3cevtModuleRt_HIM_8GBE_V3,
       "hh3cevtModuleRt-HIM-4GBE-V3": hh3cevtModuleRt_HIM_4GBE_V3,
       "hh3cevtModuleRt-HIM-8GBP-V3": hh3cevtModuleRt_HIM_8GBP_V3,
       "hh3cevtModuleRt-HIM-4GBP-V3": hh3cevtModuleRt_HIM_4GBP_V3,
       "hh3cevtModuleRt-SIC-AP": hh3cevtModuleRt_SIC_AP,
       "hh3cevtModuleRt-CR-MPU-04B": hh3cevtModuleRt_CR_MPU_04B,
       "hh3cevtModuleRt-CR-MPU-16B": hh3cevtModuleRt_CR_MPU_16B,
       "hh3cevtModuleRt-CR-MPU-16E": hh3cevtModuleRt_CR_MPU_16E,
       "hh3cevtModuleRt-CR-SFU-04D-H": hh3cevtModuleRt_CR_SFU_04D_H,
       "hh3cevtModuleRt-CR-SFU-08C-H": hh3cevtModuleRt_CR_SFU_08C_H,
       "hh3cevtModuleRt-CR-SFU-08D-H": hh3cevtModuleRt_CR_SFU_08D_H,
       "hh3cevtModuleRt-CR-SFU-16B-H": hh3cevtModuleRt_CR_SFU_16B_H,
       "hh3cevtModuleRt-CR-SFU-16C-H": hh3cevtModuleRt_CR_SFU_16C_H,
       "hh3cevtModuleRt-CR-LPU-CQ12": hh3cevtModuleRt_CR_LPU_CQ12,
       "hh3cevtModuleRt-CR-LPU-4004": hh3cevtModuleRt_CR_LPU_4004,
       "hh3cevtModuleRt-CR-HIC-PU02": hh3cevtModuleRt_CR_HIC_PU02,
       "hh3cevtModuleRt-CR-HIC-XP12": hh3cevtModuleRt_CR_HIC_XP12,
       "hh3cevtModuleRt-CR-HIC-GP12": hh3cevtModuleRt_CR_HIC_GP12,
       "hh3cevtModuleRt-CR-HIC-QQ03": hh3cevtModuleRt_CR_HIC_QQ03,
       "hh3cevtModuleRt-CR-HIC-CC01": hh3cevtModuleRt_CR_HIC_CC01,
       "hh3cevtModuleRt-CR-HIC-CP01": hh3cevtModuleRt_CR_HIC_CP01,
       "hh3cevtModuleRt-CR-MPU-16C": hh3cevtModuleRt_CR_MPU_16C,
       "hh3cevtModuleRt-MPU-100-X1": hh3cevtModuleRt_MPU_100_X1,
       "hh3cevtModuleRt-SPU-100-X1": hh3cevtModuleRt_SPU_100_X1,
       "hh3cevtModuleRt-SPU-200-X1": hh3cevtModuleRt_SPU_200_X1,
       "hh3cevtModuleRt-SPU-400-X1": hh3cevtModuleRt_SPU_400_X1,
       "hh3cevtModuleRt-HIM-10GB2EXP-H3": hh3cevtModuleRt_HIM_10GB2EXP_H3,
       "hh3cevtModuleRt-HIM-11GB1EXP-H3": hh3cevtModuleRt_HIM_11GB1EXP_H3,
       "hh3cevtModuleRt-HMIM-1E3T3": hh3cevtModuleRt_HMIM_1E3T3,
       "hh3cevtModuleRt-SIC-4G-CNDE": hh3cevtModuleRt_SIC_4G_CNDE,
       "hh3cevtModuleRt-SIC-D4G-CNDE": hh3cevtModuleRt_SIC_D4G_CNDE,
       "hh3cevtModuleRt-CR-LPU-CC08": hh3cevtModuleRt_CR_LPU_CC08,
       "hh3cevtModuleRt-CR-LPU-2002": hh3cevtModuleRt_CR_LPU_2002,
       "hh3cevtModuleRt-CR-LPU-XP20CC02": hh3cevtModuleRt_CR_LPU_XP20CC02,
       "hh3cevtModuleRt-CR-LPU-XP40": hh3cevtModuleRt_CR_LPU_XP40,
       "hh3cevtModuleRt-CR-LPU-CC04": hh3cevtModuleRt_CR_LPU_CC04,
       "hh3cevtModuleRt-FIP-680": hh3cevtModuleRt_FIP_680,
       "hh3cevtModuleRt-MIC-XP4L": hh3cevtModuleRt_MIC_XP4L,
       "hh3cevtModuleRt-MIM-1T3-V2": hh3cevtModuleRt_MIM_1T3_V2,
       "hh3cevtModuleRt-MIC-GP4L": hh3cevtModuleRt_MIC_GP4L,
       "hh3cevtModuleRt-MIC-GP8L": hh3cevtModuleRt_MIC_GP8L,
       "hh3cevtModuleRt-CR-19K-MPU-20A": hh3cevtModuleRt_CR_19K_MPU_20A,
       "hh3cevtModuleRt-CR-19K-MPU-20B": hh3cevtModuleRt_CR_19K_MPU_20B,
       "hh3cevtModuleRt-CR-19K-SFU-20C": hh3cevtModuleRt_CR_19K_SFU_20C,
       "hh3cevtModuleRt-CR-19K-MSFU-20B": hh3cevtModuleRt_CR_19K_MSFU_20B,
       "hh3cevtModuleRt-CR-19K-MSFU-20C": hh3cevtModuleRt_CR_19K_MSFU_20C,
       "hh3cevtModuleRt-CR-19K-MCCU": hh3cevtModuleRt_CR_19K_MCCU,
       "hh3cevtModuleRt-CR-19K-MFCU": hh3cevtModuleRt_CR_19K_MFCU,
       "hh3cevtModuleRt-RIC-8E1": hh3cevtModuleRt_RIC_8E1,
       "hh3cevtModuleRt-RIC-1XGEF4GEF": hh3cevtModuleRt_RIC_1XGEF4GEF,
       "hh3cevtModuleRt-RIC-TU01A": hh3cevtModuleRt_RIC_TU01A,
       "hh3cevtModuleRt-SPE-S1": hh3cevtModuleRt_SPE_S1,
       "hh3cevtModuleRt-SPE-S3": hh3cevtModuleRt_SPE_S3,
       "hh3cevtModuleRt-SPU-600-X1": hh3cevtModuleRt_SPU_600_X1,
       "hh3cevtModuleRt-RIC-CP08": hh3cevtModuleRt_RIC_CP08,
       "hh3cevtModuleRt-MIC-SP4L": hh3cevtModuleRt_MIC_SP4L,
       "hh3cevtModuleRt-MIC-ET16L": hh3cevtModuleRt_MIC_ET16L,
       "hh3cevtModuleRt-MIC-CLP4L": hh3cevtModuleRt_MIC_CLP4L,
       "hh3cevtModuleRt-MIC-CLP2L": hh3cevtModuleRt_MIC_CLP2L,
       "hh3cevtModuleRt-MIC-SP8L": hh3cevtModuleRt_MIC_SP8L,
       "hh3cevtModuleRt-HMIM-8EM": hh3cevtModuleRt_HMIM_8EM,
       "hh3cevtModuleRt-SFU": hh3cevtModuleRt_SFU,
       "hh3cevtModuleRt-SFE-L2": hh3cevtModuleRt_SFE_L2,
       "hh3cevtModuleRt-SFU-UNFIXED": hh3cevtModuleRt_SFU_UNFIXED,
       "hh3cevtModuleRt-FIP-380": hh3cevtModuleRt_FIP_380,
       "hh3cevtModuleRt-CR-19K-MPU-08A": hh3cevtModuleRt_CR_19K_MPU_08A,
       "hh3cevtModuleRt-CR-19K-MPU-16A": hh3cevtModuleRt_CR_19K_MPU_16A,
       "hh3cevtModuleRt-CR-19K-SFU-08C": hh3cevtModuleRt_CR_19K_SFU_08C,
       "hh3cevtModuleRt-CR-19K-SFU-16C": hh3cevtModuleRt_CR_19K_SFU_16C,
       "hh3cevtModuleRt-CR-19K-LPU-CC08": hh3cevtModuleRt_CR_19K_LPU_CC08,
       "hh3cevtModuleRt-CR-19K-LPU-2002": hh3cevtModuleRt_CR_19K_LPU_2002,
       "hh3cevtModuleRt-CR-19K-LPU-XP20CC02": hh3cevtModuleRt_CR_19K_LPU_XP20CC02,
       "hh3cevtModuleRt-CR-19K-LPU-XP40": hh3cevtModuleRt_CR_19K_LPU_XP40,
       "hh3cevtModuleRt-CR-19K-LPU-CC04": hh3cevtModuleRt_CR_19K_LPU_CC04,
       "hh3cevtModuleRt-CR-19K-LPU-CQ12": hh3cevtModuleRt_CR_19K_LPU_CQ12,
       "hh3cevtModuleRt-MIC-X-GT8": hh3cevtModuleRt_MIC_X_GT8,
       "hh3cevtModuleRt-MIC-X-GP4GT4": hh3cevtModuleRt_MIC_X_GP4GT4,
       "hh3cevtModuleRt-MIC-X-GP10": hh3cevtModuleRt_MIC_X_GP10,
       "hh3cevtModuleRt-MIC-X-GP8": hh3cevtModuleRt_MIC_X_GP8,
       "hh3cevtModuleRt-CR-19K-LPU-4004": hh3cevtModuleRt_CR_19K_LPU_4004,
       "hh3cevtModuleRt-FIP-260": hh3cevtModuleRt_FIP_260,
       "hh3cevtModuleRt-CR-LPU-XP72": hh3cevtModuleRt_CR_LPU_XP72,
       "hh3cevtModuleRt-CR-LPU-XP48": hh3cevtModuleRt_CR_LPU_XP48,
       "hh3cevtModuleRt-CR-LPU-CC04B": hh3cevtModuleRt_CR_LPU_CC04B,
       "hh3cevtModuleRt-CR-LPU-2002B": hh3cevtModuleRt_CR_LPU_2002B,
       "hh3cevtModuleRt-LPU-1001B": hh3cevtModuleRt_LPU_1001B,
       "hh3cevtModuleRt-CR-19K-MSFU-08A": hh3cevtModuleRt_CR_19K_MSFU_08A,
       "hh3cevtModuleRt-Sic-AP220": hh3cevtModuleRt_Sic_AP220,
       "hh3cevtModuleRt-FIP-660": hh3cevtModuleRt_FIP_660,
       "hh3cevtModuleRT-MIC-X-ET16": hh3cevtModuleRT_MIC_X_ET16,
       "hh3cevtModuleRT-MIC-X-SP4": hh3cevtModuleRT_MIC_X_SP4,
       "hh3cevtModuleRT-MIC-X-SP8": hh3cevtModuleRT_MIC_X_SP8,
       "hh3cevtModuleRT-MIC-X-CLP2": hh3cevtModuleRT_MIC_X_CLP2,
       "hh3cevtModuleRT-MIC-X-CLP4": hh3cevtModuleRT_MIC_X_CLP4,
       "hh3cevtModuleRt-SPU-300": hh3cevtModuleRt_SPU_300,
       "hh3cevtModuleRt-CR-19K-LPU-XP72": hh3cevtModuleRt_CR_19K_LPU_XP72,
       "hh3cevtModuleRt-CR-19K-LPU-XP48": hh3cevtModuleRt_CR_19K_LPU_XP48,
       "hh3cevtModuleRt-CR-19K-LPU-2002B": hh3cevtModuleRt_CR_19K_LPU_2002B,
       "hh3cevtModuleRt-CR-19K-LPU-CC04B": hh3cevtModuleRt_CR_19K_LPU_CC04B,
       "hh3cevtModuleRt-CR-19K-MPU-16B": hh3cevtModuleRt_CR_19K_MPU_16B,
       "hh3cevtModuleRT-RPE-X5": hh3cevtModuleRT_RPE_X5,
       "hh3cevtModuleRT-RPE-X5E": hh3cevtModuleRT_RPE_X5E,
       "hh3cevtModuleRt-CR-HIC-PS04": hh3cevtModuleRt_CR_HIC_PS04,
       "hh3cevtModuleRt-CR-HIC-PL08": hh3cevtModuleRt_CR_HIC_PL08,
       "hh3cevtModuleRT-MIC-X-XP2": hh3cevtModuleRT_MIC_X_XP2,
       "hh3cevtModuleRT-MIC-X-XP4": hh3cevtModuleRT_MIC_X_XP4,
       "hh3cevtModuleRT-MIC-X-XP4W": hh3cevtModuleRT_MIC_X_XP4W,
       "hh3cevtModuleRT-SIC-CNDE-SJK": hh3cevtModuleRT_SIC_CNDE_SJK,
       "hh3cevtModuleRT-SIC-4G-CNDE-SJK": hh3cevtModuleRT_SIC_4G_CNDE_SJK,
       "hh3cevtModuleRT-SIC-D4G-CNDE-SJK": hh3cevtModuleRT_SIC_D4G_CNDE_SJK,
       "hh3cevtModuleRt-CR-19K-MSFU-16A": hh3cevtModuleRt_CR_19K_MSFU_16A,
       "hh3cevtModuleRT-HMIM-CNDE-SJK": hh3cevtModuleRT_HMIM_CNDE_SJK,
       "hh3cevtModuleRT-MIBIF-MINI-CNDE-SJK": hh3cevtModuleRT_MIBIF_MINI_CNDE_SJK,
       "hh3cevtModuleRT-SIC-AP320-FIT": hh3cevtModuleRT_SIC_AP320_FIT,
       "hh3cevtModuleRT-SAP-XP4GE32": hh3cevtModuleRT_SAP_XP4GE32,
       "hh3cevtModuleRT-SIC-4E1-F-Z": hh3cevtModuleRT_SIC_4E1_F_Z,
       "hh3cevtModuleRT-HRIC-CLGQ2": hh3cevtModuleRT_HRIC_CLGQ2,
       "hh3cevtModuleRT-HRIC-YGS4": hh3cevtModuleRT_HRIC_YGS4,
       "hh3cevtModuleRT-HRIC-XP8": hh3cevtModuleRT_HRIC_XP8,
       "hh3cevtModuleRT-HRIC-GP8": hh3cevtModuleRT_HRIC_GP8,
       "hh3cevtModuleRT-HRIC-GT8": hh3cevtModuleRT_HRIC_GT8,
       "hh3cevtModuleRT-MIC-X-CNDE-SJK": hh3cevtModuleRT_MIC_X_CNDE_SJK,
       "hh3cevtModuleRt-CR-19K-LPU-CQ18": hh3cevtModuleRt_CR_19K_LPU_CQ18,
       "hh3cevtModuleRt-CR-19K-LPU-CQ12B": hh3cevtModuleRt_CR_19K_LPU_CQ12B,
       "hh3cevtModuleRt-CR-19K-LPU-SP": hh3cevtModuleRt_CR_19K_LPU_SP,
       "hh3cevtModuleRt-CR-HIC-CQ01": hh3cevtModuleRt_CR_HIC_CQ01,
       "hh3cevtModuleRt-NS-NIM-TG6A": hh3cevtModuleRt_NS_NIM_TG6A,
       "hh3cevtModuleRtNS-NIM-TG4A3": hh3cevtModuleRtNS_NIM_TG4A3,
       "hh3cevtModuleRtNSQM2CGQ20": hh3cevtModuleRtNSQM2CGQ20,
       "hh3cevtModuleRtNSQM2FWDFGC0": hh3cevtModuleRtNSQM2FWDFGC0,
       "hh3cevtModuleRtNSQM2FWDFGB0": hh3cevtModuleRtNSQM2FWDFGB0,
       "hh3cevtModuleRt-NS-TIM-TG8A2": hh3cevtModuleRt_NS_TIM_TG8A2,
       "hh3cevtModuleRtNSQM5MBSHA1": hh3cevtModuleRtNSQM5MBSHA1,
       "hh3cevtModuleRtNS-C600-CGQ6A1": hh3cevtModuleRtNS_C600_CGQ6A1,
       "hh3cevtModuleRtNSQM5SUP08A1": hh3cevtModuleRtNSQM5SUP08A1,
       "hh3cevtModuleRtNSQ1M9ESL16UA0": hh3cevtModuleRtNSQ1M9ESL16UA0,
       "hh3cevtModuleRtNS-C300-CGQ2TG16A1": hh3cevtModuleRtNS_C300_CGQ2TG16A1,
       "hh3cevtModuleRtNS-FWEMPA1": hh3cevtModuleRtNS_FWEMPA1,
       "hh3cevtModuleRtNSQM5FAB08A1": hh3cevtModuleRtNSQM5FAB08A1,
       "hh3cevtModuleRtNS-C300-QG4TG16A1": hh3cevtModuleRtNS_C300_QG4TG16A1,
       "hh3cevtModuleRtNSQM5FAB16A1": hh3cevtModuleRtNSQM5FAB16A1,
       "hh3cevtModuleRtNSQM5SUP16A1": hh3cevtModuleRtNSQM5SUP16A1,
       "hh3cevtModuleRtNSQ1M9ESL16LA0": hh3cevtModuleRtNSQ1M9ESL16LA0,
       "hh3cevtModuleRtNS-C300-TG24A1": hh3cevtModuleRtNS_C300_TG24A1,
       "hh3cevtModuleRtNSQM1SSICASK1": hh3cevtModuleRtNSQM1SSICASK1,
       "hh3cevtModuleRtNSQM2AFC2000DGDSCA0": hh3cevtModuleRtNSQM2AFC2000DGDSCA0,
       "hh3cevtModuleRt-MPU-60-WiNet": hh3cevtModuleRt_MPU_60_WiNet,
       "hh3cevtModuleRtNSQM2VGDSCA0": hh3cevtModuleRtNSQM2VGDSCA0,
       "hh3cevtModuleRt-HRIC-YGS2": hh3cevtModuleRt_HRIC_YGS2,
       "hh3cevtModuleRt-HRIC-LGQ1": hh3cevtModuleRt_HRIC_LGQ1,
       "hh3cevtModuleRt-HRIC-XP4": hh3cevtModuleRt_HRIC_XP4,
       "hh3cevtModuleRt-RSU-300": hh3cevtModuleRt_RSU_300,
       "hh3cevtModuleRt-CR-19K-LPU-CQ06B": hh3cevtModuleRt_CR_19K_LPU_CQ06B,
       "hh3cevtModuleRt-CR-HIC-XP10": hh3cevtModuleRt_CR_HIC_XP10,
       "hh3cevtModuleRt-SIC-1SSD": hh3cevtModuleRt_SIC_1SSD,
       "hh3cevtModuleRtNSQM1AFC2000GDFGA0-Z": hh3cevtModuleRtNSQM1AFC2000GDFGA0_Z,
       "hh3cevtModuleRtNSQM2QG4GP40-Z": hh3cevtModuleRtNSQM2QG4GP40_Z,
       "hh3cevtModuleRtNSQM1CGQ20-Z": hh3cevtModuleRtNSQM1CGQ20_Z,
       "hh3cevtModuleRtNSQM1FWDFGD1-Z": hh3cevtModuleRtNSQM1FWDFGD1_Z,
       "hh3cevtModuleRtNSQM1TGS32QSSG0-Z": hh3cevtModuleRtNSQM1TGS32QSSG0_Z,
       "hh3cevtModuleRtNSQM2TG16GP40-Z": hh3cevtModuleRtNSQM2TG16GP40_Z,
       "hh3cevtModuleRtNSQM2TMPU12E0": hh3cevtModuleRtNSQM2TMPU12E0,
       "hh3cevtModuleRt-HMIM-4XP": hh3cevtModuleRt_HMIM_4XP,
       "hh3cevtModuleRt-SIC-1POS-STM1": hh3cevtModuleRt_SIC_1POS_STM1,
       "hh3cevtModuleRt-HMIM-4POS": hh3cevtModuleRt_HMIM_4POS,
       "hh3cevtModuleRt-NSQM1MPULB": hh3cevtModuleRt_NSQM1MPULB,
       "hh3cevtModuleRt-CR-LPU-CQ12B": hh3cevtModuleRt_CR_LPU_CQ12B,
       "hh3cevtModuleRt-CR-LPU-CQ18": hh3cevtModuleRt_CR_LPU_CQ18,
       "hh3cevtModuleRt-CR-MPU-20A": hh3cevtModuleRt_CR_MPU_20A,
       "hh3cevtModuleRt-CR-HIC-CLP04": hh3cevtModuleRt_CR_HIC_CLP04,
       "hh3cevtModuleRt-CR-SFU-08C": hh3cevtModuleRt_CR_SFU_08C,
       "hh3cevtModuleRt-CR-HIC-PHP08": hh3cevtModuleRt_CR_HIC_PHP08,
       "hh3cevtModuleRt-CR-MPU-08A": hh3cevtModuleRt_CR_MPU_08A,
       "hh3cevtModuleRt-CR-HIC-XP12B": hh3cevtModuleRt_CR_HIC_XP12B,
       "hh3cevtModuleRt-CR-HIC-ET16": hh3cevtModuleRt_CR_HIC_ET16,
       "hh3cevtModuleRt-CR-MSFU-08A": hh3cevtModuleRt_CR_MSFU_08A,
       "hh3cevtModuleRt-CR-SFU-20C": hh3cevtModuleRt_CR_SFU_20C,
       "hh3cevtModuleRt-SIC-M2-SATA": hh3cevtModuleRt_SIC_M2_SATA,
       "hh3cevtModuleRtNSQM1MPULC": hh3cevtModuleRtNSQM1MPULC,
       "hh3cevtModuleRt-NSUM1QG1A": hh3cevtModuleRt_NSUM1QG1A,
       "hh3cevtModuleRt-NSUM1TG4A": hh3cevtModuleRt_NSUM1TG4A,
       "hh3cevtModuleRt-NSUM1GP4A": hh3cevtModuleRt_NSUM1GP4A,
       "hh3cevtModuleRt-FIP-30": hh3cevtModuleRt_FIP_30,
       "hh3cevtModuleRt-RISER-FHFL-X16": hh3cevtModuleRt_RISER_FHFL_X16,
       "hh3cevtModuleRt-RISER-GPU": hh3cevtModuleRt_RISER_GPU,
       "hh3cevtModuleRt-RISER-RAID": hh3cevtModuleRt_RISER_RAID,
       "hh3cevtModuleRt-CR-19K-LPU-8004": hh3cevtModuleRt_CR_19K_LPU_8004,
       "hh3cevtModuleRt-CR-19K-MPU-08B": hh3cevtModuleRt_CR_19K_MPU_08B,
       "hh3cevtModuleRt-CR-HIC-CQ02": hh3cevtModuleRt_CR_HIC_CQ02,
       "hh3cevtModuleRt-NSQM1ISPAXA1": hh3cevtModuleRt_NSQM1ISPAXA1,
       "hh3cevtModuleRt-NSQM1ISPAXB1": hh3cevtModuleRt_NSQM1ISPAXB1,
       "hh3cevtModuleRt-CR-USBDISK": hh3cevtModuleRt_CR_USBDISK,
       "hh3cevtModuleRt-SIC-4RS": hh3cevtModuleRt_SIC_4RS,
       "hh3cevtModuleRt-NSQM1MPULC-Z": hh3cevtModuleRt_NSQM1MPULC_Z,
       "hh3cevtModuleRt-CR-18K-MPU-16B": hh3cevtModuleRt_CR_18K_MPU_16B,
       "hh3cevtModuleRt-CR-18K-SFU-16C": hh3cevtModuleRt_CR_18K_SFU_16C,
       "hh3cevtModuleRt-DS-3RH-4T": hh3cevtModuleRt_DS_3RH_4T,
       "hh3cevtModuleRt-HRIC-CQ1F": hh3cevtModuleRt_HRIC_CQ1F,
       "hh3cevtModuleRt-HRIC-LGQ2F": hh3cevtModuleRt_HRIC_LGQ2F,
       "hh3cevtModuleRt-CR-HIC-CLGQ04": hh3cevtModuleRt_CR_HIC_CLGQ04,
       "hh3cevtModuleRt-NSQM1QG1A-Z": hh3cevtModuleRt_NSQM1QG1A_Z,
       "hh3cevtModuleRt-NSQM1TG4A-Z": hh3cevtModuleRt_NSQM1TG4A_Z,
       "hh3cevtModuleRt-NSQM1GP4A-Z": hh3cevtModuleRt_NSQM1GP4A_Z,
       "hh3cevtModuleRt-CR-LPU-8004": hh3cevtModuleRt_CR_LPU_8004,
       "hh3cevtModuleRt-MPU-100-G": hh3cevtModuleRt_MPU_100_G,
       "hh3cevtModuleRt-SPU-300-G": hh3cevtModuleRt_SPU_300_G,
       "hh3cevtModuleRt-CR-19K-MPU-20C": hh3cevtModuleRt_CR_19K_MPU_20C,
       "hh3cevtModuleRt-CR-18K-MPU-16C": hh3cevtModuleRt_CR_18K_MPU_16C,
       "hh3cevtModuleRt-SIC-5G": hh3cevtModuleRt_SIC_5G,
       "hh3cevtModuleRt-RSU-400": hh3cevtModuleRt_RSU_400,
       "hh3cevtModuleRt-HRIC-XP8-H": hh3cevtModuleRt_HRIC_XP8_H,
       "hh3cevtModuleRt-BBU3120-MCBM2LMCMB1": hh3cevtModuleRt_BBU3120_MCBM2LMCMB1,
       "hh3cevtModuleRt-BBU3120-MCBM2LBBMB1": hh3cevtModuleRt_BBU3120_MCBM2LBBMB1,
       "hh3cevtModuleRt-HMIM-2POS": hh3cevtModuleRt_HMIM_2POS,
       "hpevtModuleRt-SIC-EPRI": hpevtModuleRt_SIC_EPRI,
       "hpevtModuleRt-MIM-1E1-V2": hpevtModuleRt_MIM_1E1_V2,
       "hpevtModuleRt-MIM-1E1-F-V2": hpevtModuleRt_MIM_1E1_F_V2,
       "hpevtModuleRt-MIM-2E1-F-V2": hpevtModuleRt_MIM_2E1_F_V2,
       "hpevtModuleRt-MIM-4E1-F-V2": hpevtModuleRt_MIM_4E1_F_V2,
       "hpevtModuleRt-MIM-8E1-75": hpevtModuleRt_MIM_8E1_75,
       "hpevtModuleRt-MIM-8E1-75-F": hpevtModuleRt_MIM_8E1_75_F,
       "hpevtModuleRt-MIM-8T1": hpevtModuleRt_MIM_8T1,
       "hpevtModuleRt-MIM-8T1-F": hpevtModuleRt_MIM_8T1_F,
       "hpevtModuleRt-MIM-IMA-8E1-75": hpevtModuleRt_MIM_IMA_8E1_75,
       "hpevtModuleRt-FIC-2E1-V3": hpevtModuleRt_FIC_2E1_V3,
       "hpevtModuleRt-FIC-IMA-8T1-V2": hpevtModuleRt_FIC_IMA_8T1_V2,
       "hh3cevtModuleRtCN-MSU-X3": hh3cevtModuleRtCN_MSU_X3,
       "hh3cevtModuleRtCN-FSP-660": hh3cevtModuleRtCN_FSP_660,
       "hh3cevtModuleRtCN-MIC-X-XP4W": hh3cevtModuleRtCN_MIC_X_XP4W,
       "hh3cevtModuleRtCN-MIC-X-GP8": hh3cevtModuleRtCN_MIC_X_GP8,
       "hh3cevtModuleRtCN-MIC-X-GT8": hh3cevtModuleRtCN_MIC_X_GT8,
       "hh3cevtModuleSwitchType": hh3cevtModuleSwitchType,
       "hh3cevtModuleSw-10OR100M": hh3cevtModuleSw_10OR100M,
       "hh3cevtModuleSw-1000BASE-LX-SM": hh3cevtModuleSw_1000BASE_LX_SM,
       "hh3cevtModuleSw-1000BASE-SX-MM": hh3cevtModuleSw_1000BASE_SX_MM,
       "hh3cevtModuleSw-1000BASE-TX": hh3cevtModuleSw_1000BASE_TX,
       "hh3cevtModuleSw-100M-SINGLEMODE-FX": hh3cevtModuleSw_100M_SINGLEMODE_FX,
       "hh3cevtModuleSw-100M-MULTIMODE-FX": hh3cevtModuleSw_100M_MULTIMODE_FX,
       "hh3cevtModuleSw-100M-100BASE-TX": hh3cevtModuleSw_100M_100BASE_TX,
       "hh3cevtModuleSw-100M-HUB": hh3cevtModuleSw_100M_HUB,
       "hh3cevtModuleSw-VDSL": hh3cevtModuleSw_VDSL,
       "hh3cevtModuleSw-STACK": hh3cevtModuleSw_STACK,
       "hh3cevtModuleSw-1000BASE-ZENITH-FX": hh3cevtModuleSw_1000BASE_ZENITH_FX,
       "hh3cevtModuleSw-1000BASE-LONG-FX": hh3cevtModuleSw_1000BASE_LONG_FX,
       "hh3cevtModuleSw-ADSL": hh3cevtModuleSw_ADSL,
       "hh3cevtModuleSw-4T10OR100-4FX100SM": hh3cevtModuleSw_4T10OR100_4FX100SM,
       "hh3cevtModuleSw-4T10OR100-4FX100MM": hh3cevtModuleSw_4T10OR100_4FX100MM,
       "hh3cevtModuleSw-VSPL": hh3cevtModuleSw_VSPL,
       "hh3cevtModuleSw-ASPL": hh3cevtModuleSw_ASPL,
       "hh3cevtModuleSw-1000M-SFP": hh3cevtModuleSw_1000M_SFP,
       "hh3cevtModuleSw-LS82O2CM": hh3cevtModuleSw_LS82O2CM,
       "hh3cevtModuleSw-LS82P2CM": hh3cevtModuleSw_LS82P2CM,
       "hh3cevtModuleSw-LS82O4GM": hh3cevtModuleSw_LS82O4GM,
       "hh3cevtModuleSw-LS82GB4C": hh3cevtModuleSw_LS82GB4C,
       "hh3cevtModuleSw-LS82GT4C": hh3cevtModuleSw_LS82GT4C,
       "hh3cevtModuleSw-LS82ST4C": hh3cevtModuleSw_LS82ST4C,
       "hh3cevtModuleSw-BOARD-LS82DSPU": hh3cevtModuleSw_BOARD_LS82DSPU,
       "hh3cevtModuleSw-BOARD-LS81GP8U": hh3cevtModuleSw_BOARD_LS81GP8U,
       "hh3cevtModuleSw-BOARD-LS82GT20": hh3cevtModuleSw_BOARD_LS82GT20,
       "hh3cevtModuleSw-BOARD-LS82FE48": hh3cevtModuleSw_BOARD_LS82FE48,
       "hh3cevtModuleSw-LS82T24B": hh3cevtModuleSw_LS82T24B,
       "hh3cevtModuleSw-LSB1SRPA": hh3cevtModuleSw_LSB1SRPA,
       "hh3cevtModuleSw-LSB1FT48A": hh3cevtModuleSw_LSB1FT48A,
       "hh3cevtModuleSw-LSB1FT48B": hh3cevtModuleSw_LSB1FT48B,
       "hh3cevtModuleSw-LSB1F48GA": hh3cevtModuleSw_LSB1F48GA,
       "hh3cevtModuleSw-LSB1F48GB": hh3cevtModuleSw_LSB1F48GB,
       "hh3cevtModuleSw-LSB1FP20A": hh3cevtModuleSw_LSB1FP20A,
       "hh3cevtModuleSw-LSB1FP20B": hh3cevtModuleSw_LSB1FP20B,
       "hh3cevtModuleSw-FT48A": hh3cevtModuleSw_FT48A,
       "hh3cevtModuleSw-GP4U": hh3cevtModuleSw_GP4U,
       "hh3cevtModuleSw-GP2U": hh3cevtModuleSw_GP2U,
       "hh3cevtModuleSw-TGX1A": hh3cevtModuleSw_TGX1A,
       "hh3cevtModuleSw-1000BASE-LX-SM-IR-SC": hh3cevtModuleSw_1000BASE_LX_SM_IR_SC,
       "hh3cevtModuleSw-1000BASE-SX-MM-SR-SC": hh3cevtModuleSw_1000BASE_SX_MM_SR_SC,
       "hh3cevtModuleSw-1000BASE-T-RJ45": hh3cevtModuleSw_1000BASE_T_RJ45,
       "hh3cevtModuleSw-100BASE-FX-SM-IR-SC": hh3cevtModuleSw_100BASE_FX_SM_IR_SC,
       "hh3cevtModuleSw-100BASE-FX-MM-SR-SC": hh3cevtModuleSw_100BASE_FX_MM_SR_SC,
       "hh3cevtModuleSw-GIGA-STACK-1M-PC": hh3cevtModuleSw_GIGA_STACK_1M_PC,
       "hh3cevtModuleSw-1000BASE-LX-SM-VLR-LC": hh3cevtModuleSw_1000BASE_LX_SM_VLR_LC,
       "hh3cevtModuleSw-1000BASE-LX-SM-LR-LC": hh3cevtModuleSw_1000BASE_LX_SM_LR_LC,
       "hh3cevtModuleSw-100BASE-FX-SM-LR-SC": hh3cevtModuleSw_100BASE_FX_SM_LR_SC,
       "hh3cevtModuleSw-1000BASE-X-GBIC": hh3cevtModuleSw_1000BASE_X_GBIC,
       "hh3cevtModuleSw-100M-SINGLEMODE-FX-LC": hh3cevtModuleSw_100M_SINGLEMODE_FX_LC,
       "hh3cevtModuleSw-100M-MULTIMODE-FX-LC": hh3cevtModuleSw_100M_MULTIMODE_FX_LC,
       "hh3cevtModuleSw-1000BASE-4SFP": hh3cevtModuleSw_1000BASE_4SFP,
       "hh3cevtModuleSw-1000BASE-4GBIC": hh3cevtModuleSw_1000BASE_4GBIC,
       "hh3cevtModuleSw-1000BASE-FIXED-4SFP": hh3cevtModuleSw_1000BASE_FIXED_4SFP,
       "hh3cevtModuleSw-1000BASE-FIXED-4GBIC": hh3cevtModuleSw_1000BASE_FIXED_4GBIC,
       "hh3cevtModuleSw-LSB1GP12A": hh3cevtModuleSw_LSB1GP12A,
       "hh3cevtModuleSw-LSB1GP12B": hh3cevtModuleSw_LSB1GP12B,
       "hh3cevtModuleSw-LSB1TGX1A": hh3cevtModuleSw_LSB1TGX1A,
       "hh3cevtModuleSw-LSB1TGX1B": hh3cevtModuleSw_LSB1TGX1B,
       "hh3cevtModuleSw-LSB1P4G8A": hh3cevtModuleSw_LSB1P4G8A,
       "hh3cevtModuleSw-LSB1P4G8B": hh3cevtModuleSw_LSB1P4G8B,
       "hh3cevtModuleSw-LSB1A4G8A": hh3cevtModuleSw_LSB1A4G8A,
       "hh3cevtModuleSw-LSB1A4G8B": hh3cevtModuleSw_LSB1A4G8B,
       "hh3cevtModuleSw-FT48C": hh3cevtModuleSw_FT48C,
       "hh3cevtModuleSw-FP20": hh3cevtModuleSw_FP20,
       "hh3cevtModuleSw-BOARD-LS81FT48": hh3cevtModuleSw_BOARD_LS81FT48,
       "hh3cevtModuleSw-BOARD-LS81GB8U": hh3cevtModuleSw_BOARD_LS81GB8U,
       "hh3cevtModuleSw-BOARD-LS81GT8U": hh3cevtModuleSw_BOARD_LS81GT8U,
       "hh3cevtModuleSw-BOARD-LS81FS24": hh3cevtModuleSw_BOARD_LS81FS24,
       "hh3cevtModuleSw-BOARD-LS81FM24": hh3cevtModuleSw_BOARD_LS81FM24,
       "hh3cevtModuleSw-BOARD-LS82GP20": hh3cevtModuleSw_BOARD_LS82GP20,
       "hh3cevtModuleSw-LSB1SRPB": hh3cevtModuleSw_LSB1SRPB,
       "hh3cevtModuleSw-LSB1F32GA": hh3cevtModuleSw_LSB1F32GA,
       "hh3cevtModuleSw-LSB1F32GB": hh3cevtModuleSw_LSB1F32GB,
       "hh3cevtModuleSw-LSB2FT48A": hh3cevtModuleSw_LSB2FT48A,
       "hh3cevtModuleSw-LSB2FT48B": hh3cevtModuleSw_LSB2FT48B,
       "hh3cevtModuleSw-LSB1GT12A": hh3cevtModuleSw_LSB1GT12A,
       "hh3cevtModuleSw-LSB1GT12B": hh3cevtModuleSw_LSB1GT12B,
       "hh3cevtModuleSw-PC4U": hh3cevtModuleSw_PC4U,
       "hh3cevtModuleSw-FT32A": hh3cevtModuleSw_FT32A,
       "hh3cevtModuleSw-GT4U": hh3cevtModuleSw_GT4U,
       "hh3cevtModuleSw-BOARD-LS83FP20A": hh3cevtModuleSw_BOARD_LS83FP20A,
       "hh3cevtModuleSw-BOARD-LS82HGMU": hh3cevtModuleSw_BOARD_LS82HGMU,
       "hh3cevtModuleSw-LSB1GP8TB": hh3cevtModuleSw_LSB1GP8TB,
       "hh3cevtModuleSw-LSB1GP8TC": hh3cevtModuleSw_LSB1GP8TC,
       "hh3cevtModuleSw-LSB1GT8PB": hh3cevtModuleSw_LSB1GT8PB,
       "hh3cevtModuleSw-LSB1GT8PC": hh3cevtModuleSw_LSB1GT8PC,
       "hh3cevtModuleSw-LSB1FT48C": hh3cevtModuleSw_LSB1FT48C,
       "hh3cevtModuleSw-LSB1FP20C": hh3cevtModuleSw_LSB1FP20C,
       "hh3cevtModuleSw-LSB1F32GC": hh3cevtModuleSw_LSB1F32GC,
       "hh3cevtModuleSw-LSB1GT12C": hh3cevtModuleSw_LSB1GT12C,
       "hh3cevtModuleSw-LSB1GP12C": hh3cevtModuleSw_LSB1GP12C,
       "hh3cevtModuleSw-LSB1P4G8C": hh3cevtModuleSw_LSB1P4G8C,
       "hh3cevtModuleSw-LSB1TGX1C": hh3cevtModuleSw_LSB1TGX1C,
       "hh3cevtModuleSw-LSB1GT24B": hh3cevtModuleSw_LSB1GT24B,
       "hh3cevtModuleSw-LSB1GT24C": hh3cevtModuleSw_LSB1GT24C,
       "hh3cevtModuleSw-LSB1GP24B": hh3cevtModuleSw_LSB1GP24B,
       "hh3cevtModuleSw-LSB1GP24C": hh3cevtModuleSw_LSB1GP24C,
       "hh3cevtModuleSw-LSB1XP2B": hh3cevtModuleSw_LSB1XP2B,
       "hh3cevtModuleSw-LSB1XP2C": hh3cevtModuleSw_LSB1XP2C,
       "hh3cevtModuleSw-LSB1GV48B": hh3cevtModuleSw_LSB1GV48B,
       "hh3cevtModuleSw-LSB1GV48C": hh3cevtModuleSw_LSB1GV48C,
       "hh3cevtModuleSw-LSB1SRPC": hh3cevtModuleSw_LSB1SRPC,
       "hh3cevtModuleSw-LSB1SRP1N0": hh3cevtModuleSw_LSB1SRP1N0,
       "hh3cevtModuleSw-LSB1SRP1N1": hh3cevtModuleSw_LSB1SRP1N1,
       "hh3cevtModuleSw-LSB1SRP1N2": hh3cevtModuleSw_LSB1SRP1N2,
       "hh3cevtModuleSw-GT24": hh3cevtModuleSw_GT24,
       "hh3cevtModuleSw-GP24": hh3cevtModuleSw_GP24,
       "hh3cevtModuleSw-XP2": hh3cevtModuleSw_XP2,
       "hh3cevtModuleSw-GV48": hh3cevtModuleSw_GV48,
       "hh3cevtModuleSw-LSG1GP8U": hh3cevtModuleSw_LSG1GP8U,
       "hh3cevtModuleSw-LSG1GT8U": hh3cevtModuleSw_LSG1GT8U,
       "hh3cevtModuleSw-LSG1TG1U": hh3cevtModuleSw_LSG1TG1U,
       "hh3cevtModuleSw-LSG1TD1U": hh3cevtModuleSw_LSG1TD1U,
       "hh3cevtModuleSw-LSB2FT48C": hh3cevtModuleSw_LSB2FT48C,
       "hh3cevtModuleSw-LSB1GT48B": hh3cevtModuleSw_LSB1GT48B,
       "hh3cevtModuleSw-LSB1GT48C": hh3cevtModuleSw_LSB1GT48C,
       "hh3cevtModuleSw-LS81GT48": hh3cevtModuleSw_LS81GT48,
       "hh3cevtModuleSw-LS81SRPG0": hh3cevtModuleSw_LS81SRPG0,
       "hh3cevtModuleSw-LS81SRPG1": hh3cevtModuleSw_LS81SRPG1,
       "hh3cevtModuleSw-LS81SRPG2": hh3cevtModuleSw_LS81SRPG2,
       "hh3cevtModuleSw-LS81SRPG3": hh3cevtModuleSw_LS81SRPG3,
       "hh3cevtModuleSw-SR01SRPUB": hh3cevtModuleSw_SR01SRPUB,
       "hh3cevtModuleSw-SR01SRPUA": hh3cevtModuleSw_SR01SRPUA,
       "hh3cevtModuleSw-SR01GP12L": hh3cevtModuleSw_SR01GP12L,
       "hh3cevtModuleSw-SR01GP12W": hh3cevtModuleSw_SR01GP12W,
       "hh3cevtModuleSw-SR01FT48L": hh3cevtModuleSw_SR01FT48L,
       "hh3cevtModuleSw-SR01FT48W": hh3cevtModuleSw_SR01FT48W,
       "hh3cevtModuleSw-SR01XK1W": hh3cevtModuleSw_SR01XK1W,
       "hh3cevtModuleSw-SR01FP20W": hh3cevtModuleSw_SR01FP20W,
       "hh3cevtModuleSw-SR01GT12W": hh3cevtModuleSw_SR01GT12W,
       "hh3cevtModuleSw-SR01F32GL": hh3cevtModuleSw_SR01F32GL,
       "hh3cevtModuleSw-SR01F32GW": hh3cevtModuleSw_SR01F32GW,
       "hh3cevtModuleSw-SR01GT8PL": hh3cevtModuleSw_SR01GT8PL,
       "hh3cevtModuleSw-SR01GT8PW": hh3cevtModuleSw_SR01GT8PW,
       "hh3cevtModuleSw-SR01P4G8W": hh3cevtModuleSw_SR01P4G8W,
       "hh3cevtModuleSw-LSA1FP8U": hh3cevtModuleSw_LSA1FP8U,
       "hh3cevtModuleSw-LSB1SP4B": hh3cevtModuleSw_LSB1SP4B,
       "hh3cevtModuleSw-LSB1SP4C": hh3cevtModuleSw_LSB1SP4C,
       "hh3cevtModuleSw-LSB1UP1B": hh3cevtModuleSw_LSB1UP1B,
       "hh3cevtModuleSw-LSB1UP1C": hh3cevtModuleSw_LSB1UP1C,
       "hh3cevtModuleSw-LSB1XP4B": hh3cevtModuleSw_LSB1XP4B,
       "hh3cevtModuleSw-LSB1XP4C": hh3cevtModuleSw_LSB1XP4C,
       "hh3cevtModuleSw-SP4": hh3cevtModuleSw_SP4,
       "hh3cevtModuleSw-UP1": hh3cevtModuleSw_UP1,
       "hh3cevtModuleSw-XP4": hh3cevtModuleSw_XP4,
       "hh3cevtModuleSw-LS81VSNP": hh3cevtModuleSw_LS81VSNP,
       "hh3cevtModuleSw-LS81T12P": hh3cevtModuleSw_LS81T12P,
       "hh3cevtModuleSw-LS81P12T": hh3cevtModuleSw_LS81P12T,
       "hh3cevtModuleSw-LS81GP8UB": hh3cevtModuleSw_LS81GP8UB,
       "hh3cevtModuleSw-LS81FT48E": hh3cevtModuleSw_LS81FT48E,
       "hh3cevtModuleSw-LS81GP4UB": hh3cevtModuleSw_LS81GP4UB,
       "hh3cevtModuleSw-LS81GT8UE": hh3cevtModuleSw_LS81GT8UE,
       "hh3cevtModuleSw-LS81GT48A": hh3cevtModuleSw_LS81GT48A,
       "hh3cevtModuleSw-LS81FP48": hh3cevtModuleSw_LS81FP48,
       "hh3cevtModuleSw-LSB1XK1B": hh3cevtModuleSw_LSB1XK1B,
       "hh3cevtModuleSw-LSB1XK1C": hh3cevtModuleSw_LSB1XK1C,
       "hh3cevtModuleSw-SR01SRPUC": hh3cevtModuleSw_SR01SRPUC,
       "hh3cevtModuleSw-SR01SRPUD": hh3cevtModuleSw_SR01SRPUD,
       "hh3cevtModuleSw-SR01SRPUE": hh3cevtModuleSw_SR01SRPUE,
       "hh3cevtModuleSw-LSB1SRP1N3": hh3cevtModuleSw_LSB1SRP1N3,
       "hh3cevtModuleSw-LSB1VP2B": hh3cevtModuleSw_LSB1VP2B,
       "hh3cevtModuleSw-LSB1NATB": hh3cevtModuleSw_LSB1NATB,
       "hh3cevtModuleSw-LSB1VPNB": hh3cevtModuleSw_LSB1VPNB,
       "hh3cevtModuleSw-LSGP8P": hh3cevtModuleSw_LSGP8P,
       "hh3cevtModuleSw-LSXK1P": hh3cevtModuleSw_LSXK1P,
       "hh3cevtModuleSw-LSXP2P": hh3cevtModuleSw_LSXP2P,
       "hh3cevtModuleSw-LS81FT48F": hh3cevtModuleSw_LS81FT48F,
       "hh3cevtModuleSw-LS81PT8G": hh3cevtModuleSw_LS81PT8G,
       "hh3cevtModuleSw-LS81PT4G": hh3cevtModuleSw_LS81PT4G,
       "hh3cevtModuleSw-LSSTK24G": hh3cevtModuleSw_LSSTK24G,
       "hh3cevtModuleSw-LS82GT20A": hh3cevtModuleSw_LS82GT20A,
       "hh3cevtModuleSw-LS82GP20A": hh3cevtModuleSw_LS82GP20A,
       "hh3cevtModuleSw-LS81TGX1C": hh3cevtModuleSw_LS81TGX1C,
       "hh3cevtModuleSw-VP2": hh3cevtModuleSw_VP2,
       "hh3cevtModuleSw-LSA1FB8U": hh3cevtModuleSw_LSA1FB8U,
       "hh3cevtModuleSw-LS81T12PE": hh3cevtModuleSw_LS81T12PE,
       "hh3cevtModuleSw-LS81P12TE": hh3cevtModuleSw_LS81P12TE,
       "hh3cevtModuleSw-LSB1SRP2N0": hh3cevtModuleSw_LSB1SRP2N0,
       "hh3cevtModuleSw-LSB1SRP2N3": hh3cevtModuleSw_LSB1SRP2N3,
       "hh3cevtModuleSw-LSB1GV48DB": hh3cevtModuleSw_LSB1GV48DB,
       "hh3cevtModuleSw-LSB1FW8B": hh3cevtModuleSw_LSB1FW8B,
       "hh3cevtModuleSw-LSB1IPSEC8B": hh3cevtModuleSw_LSB1IPSEC8B,
       "hh3cevtModuleSw-LSB1IDSB": hh3cevtModuleSw_LSB1IDSB,
       "hh3cevtModuleSw-LSB1IPSB": hh3cevtModuleSw_LSB1IPSB,
       "hh3cevtModuleSw-LSB2FT48CA": hh3cevtModuleSw_LSB2FT48CA,
       "hh3cevtModuleSw-LSB1FP20CA": hh3cevtModuleSw_LSB1FP20CA,
       "hh3cevtModuleSw-LSB1F32GCA": hh3cevtModuleSw_LSB1F32GCA,
       "hh3cevtModuleSw-LSB1P4G8CA": hh3cevtModuleSw_LSB1P4G8CA,
       "hh3cevtModuleSw-LSB1GT12CA": hh3cevtModuleSw_LSB1GT12CA,
       "hh3cevtModuleSw-LSB1GT24CA": hh3cevtModuleSw_LSB1GT24CA,
       "hh3cevtModuleSw-LSB1GP12CA": hh3cevtModuleSw_LSB1GP12CA,
       "hh3cevtModuleSw-LSB1GP24CA": hh3cevtModuleSw_LSB1GP24CA,
       "hh3cevtModuleSw-LSB1GT8PCA": hh3cevtModuleSw_LSB1GT8PCA,
       "hh3cevtModuleSw-LSB1XP2CA": hh3cevtModuleSw_LSB1XP2CA,
       "hh3cevtModuleSw-LSB1XK1CA": hh3cevtModuleSw_LSB1XK1CA,
       "hh3cevtModuleSw-LSB1XP4CA": hh3cevtModuleSw_LSB1XP4CA,
       "hh3cevtModuleSw-LSB1UP1CA": hh3cevtModuleSw_LSB1UP1CA,
       "hh3cevtModuleSw-LSB1SP4CA": hh3cevtModuleSw_LSB1SP4CA,
       "hh3cevtModuleSw-LSB1VP2CA": hh3cevtModuleSw_LSB1VP2CA,
       "hh3cevtModuleSw-SR01FT48WA": hh3cevtModuleSw_SR01FT48WA,
       "hh3cevtModuleSw-SR01FP20WA": hh3cevtModuleSw_SR01FP20WA,
       "hh3cevtModuleSw-SR01F32GWA": hh3cevtModuleSw_SR01F32GWA,
       "hh3cevtModuleSw-SR01P4G8WA": hh3cevtModuleSw_SR01P4G8WA,
       "hh3cevtModuleSw-SR01GT12WA": hh3cevtModuleSw_SR01GT12WA,
       "hh3cevtModuleSw-SR01GT24WA": hh3cevtModuleSw_SR01GT24WA,
       "hh3cevtModuleSw-SR01GP12WA": hh3cevtModuleSw_SR01GP12WA,
       "hh3cevtModuleSw-SR01GP24WA": hh3cevtModuleSw_SR01GP24WA,
       "hh3cevtModuleSw-SR01GT8PWA": hh3cevtModuleSw_SR01GT8PWA,
       "hh3cevtModuleSw-SR01XP2WA": hh3cevtModuleSw_SR01XP2WA,
       "hh3cevtModuleSw-SR01XK1WA": hh3cevtModuleSw_SR01XK1WA,
       "hh3cevtModuleSw-SR01UP1WA": hh3cevtModuleSw_SR01UP1WA,
       "hh3cevtModuleSw-SR01SP4WA": hh3cevtModuleSw_SR01SP4WA,
       "hh3cevtModuleSw-GP8U": hh3cevtModuleSw_GP8U,
       "hh3cevtModuleSw-LSEXP1P": hh3cevtModuleSw_LSEXP1P,
       "hh3cevtModuleSw-LSEXK1P": hh3cevtModuleSw_LSEXK1P,
       "hh3cevtModuleSw-LSEXS1P": hh3cevtModuleSw_LSEXS1P,
       "hh3cevtModuleSw-LS81GP48": hh3cevtModuleSw_LS81GP48,
       "hh3cevtModuleSw-LS81GT48B": hh3cevtModuleSw_LS81GT48B,
       "hh3cevtModuleSw-LS81T16P": hh3cevtModuleSw_LS81T16P,
       "hh3cevtModuleSw-LS81T32P": hh3cevtModuleSw_LS81T32P,
       "hh3cevtModuleSw-LS81TGX2": hh3cevtModuleSw_LS81TGX2,
       "hh3cevtModuleSw-LS81TGX4": hh3cevtModuleSw_LS81TGX4,
       "hh3cevtModuleSw-LSB1GV48DA": hh3cevtModuleSw_LSB1GV48DA,
       "hh3cevtModuleSw-SR01GV48VB": hh3cevtModuleSw_SR01GV48VB,
       "hh3cevtModuleSw-LSB1GT24DB": hh3cevtModuleSw_LSB1GT24DB,
       "hh3cevtModuleSw-LSB1GP24DB": hh3cevtModuleSw_LSB1GP24DB,
       "hh3cevtModuleSw-LSB1GP24DC": hh3cevtModuleSw_LSB1GP24DC,
       "hh3cevtModuleSw-LSB1FW8DB": hh3cevtModuleSw_LSB1FW8DB,
       "hh3cevtModuleSw-LSB1IPSEC8DB": hh3cevtModuleSw_LSB1IPSEC8DB,
       "hh3cevtModuleSw-SR01GT24VB": hh3cevtModuleSw_SR01GT24VB,
       "hh3cevtModuleSw-SR01GP24VC": hh3cevtModuleSw_SR01GP24VC,
       "hh3cevtModuleSw-SR01VP2WA": hh3cevtModuleSw_SR01VP2WA,
       "hh3cevtModuleSw-SR01FW8VB": hh3cevtModuleSw_SR01FW8VB,
       "hh3cevtModuleSw-SR01IPSEC8VB": hh3cevtModuleSw_SR01IPSEC8VB,
       "hh3cevtModuleSw-SR01NATL": hh3cevtModuleSw_SR01NATL,
       "hh3cevtModuleSw-SR01VPNL": hh3cevtModuleSw_SR01VPNL,
       "hh3cevtModuleSw-LSB1GP24CB": hh3cevtModuleSw_LSB1GP24CB,
       "hh3cevtModuleSw-LSB1GP48DB": hh3cevtModuleSw_LSB1GP48DB,
       "hh3cevtModuleSw-LSB1XP2CB": hh3cevtModuleSw_LSB1XP2CB,
       "hh3cevtModuleSw-XP4L": hh3cevtModuleSw_XP4L,
       "hh3cevtModuleSw-LSB1XP4LDB": hh3cevtModuleSw_LSB1XP4LDB,
       "hh3cevtModuleSw-LSB1XP4LDC": hh3cevtModuleSw_LSB1XP4LDC,
       "hh3cevtModuleSw-AHP4": hh3cevtModuleSw_AHP4,
       "hh3cevtModuleSw-LSB1AHP4GCA": hh3cevtModuleSw_LSB1AHP4GCA,
       "hh3cevtModuleSw-CLP4": hh3cevtModuleSw_CLP4,
       "hh3cevtModuleSw-LSB1CLP4GCA": hh3cevtModuleSw_LSB1CLP4GCA,
       "hh3cevtModuleSw-ET32": hh3cevtModuleSw_ET32,
       "hh3cevtModuleSw-LSB1ET32GCA": hh3cevtModuleSw_LSB1ET32GCA,
       "hh3cevtModuleSw-LSB1IDSDB": hh3cevtModuleSw_LSB1IDSDB,
       "hh3cevtModuleSw-LSB1SRP2N1": hh3cevtModuleSw_LSB1SRP2N1,
       "hh3cevtModuleSw-BOARD-LS82SRPB": hh3cevtModuleSw_BOARD_LS82SRPB,
       "hh3cevtModuleSw-BORAD-LS83SRPC": hh3cevtModuleSw_BORAD_LS83SRPC,
       "hh3cevtModuleSw-Main": hh3cevtModuleSw_Main,
       "hh3cevtModuleSw-LSB1SRP2N2": hh3cevtModuleSw_LSB1SRP2N2,
       "hh3cevtModuleSw-LSB1NAMB": hh3cevtModuleSw_LSB1NAMB,
       "hh3cevtModuleSw-RSP2": hh3cevtModuleSw_RSP2,
       "hh3cevtModuleSw-LSB1RSP2CA": hh3cevtModuleSw_LSB1RSP2CA,
       "hh3cevtModuleSw-SR01XP4LVC": hh3cevtModuleSw_SR01XP4LVC,
       "hh3cevtModuleSw-SR01AHP4GWA": hh3cevtModuleSw_SR01AHP4GWA,
       "hh3cevtModuleSw-SR01CLP4GWA": hh3cevtModuleSw_SR01CLP4GWA,
       "hh3cevtModuleSw-SR01ET32GWA": hh3cevtModuleSw_SR01ET32GWA,
       "hh3cevtModuleSw-SR01IDSVB": hh3cevtModuleSw_SR01IDSVB,
       "hh3cevtModuleSw-SR01SRPUF": hh3cevtModuleSw_SR01SRPUF,
       "hh3cevtModuleSw-SR01NAML": hh3cevtModuleSw_SR01NAML,
       "hh3cevtModuleSw-SR01RSP2WA": hh3cevtModuleSw_SR01RSP2WA,
       "hh3cevtModuleSw-LSPM1XP1P": hh3cevtModuleSw_LSPM1XP1P,
       "hh3cevtModuleSw-LSPM1XP2P": hh3cevtModuleSw_LSPM1XP2P,
       "hh3cevtModuleSw-LSPM1CX2P": hh3cevtModuleSw_LSPM1CX2P,
       "hh3cevtModuleSw-STK-1000BASE-T": hh3cevtModuleSw_STK_1000BASE_T,
       "hh3cevtModuleSw-LSB1SRP1M0": hh3cevtModuleSw_LSB1SRP1M0,
       "hh3cevtModuleSw-LSB1SRP1M1": hh3cevtModuleSw_LSB1SRP1M1,
       "hh3cevtModuleSw-LSB1GP12DB": hh3cevtModuleSw_LSB1GP12DB,
       "hh3cevtModuleSw-LSB1GT12DB": hh3cevtModuleSw_LSB1GT12DB,
       "hh3cevtModuleSw-LSB1XK1DB": hh3cevtModuleSw_LSB1XK1DB,
       "hh3cevtModuleSw-LSB1XP2DB": hh3cevtModuleSw_LSB1XP2DB,
       "hh3cevtModuleSw-LSB1XP2DC": hh3cevtModuleSw_LSB1XP2DC,
       "hh3cevtModuleSw-LSB1GT48LDB": hh3cevtModuleSw_LSB1GT48LDB,
       "hh3cevtModuleSw-LSB1XP4TDB": hh3cevtModuleSw_LSB1XP4TDB,
       "hh3cevtModuleSw-LSB1XP4TDC": hh3cevtModuleSw_LSB1XP4TDC,
       "hh3cevtModuleSw-LSB1RSP2DC": hh3cevtModuleSw_LSB1RSP2DC,
       "hh3cevtModuleSw-LSB1VP2DC": hh3cevtModuleSw_LSB1VP2DC,
       "hh3cevtModuleSw-LSB1XP4DB": hh3cevtModuleSw_LSB1XP4DB,
       "hh3cevtModuleSw-LSB1SRP2E0": hh3cevtModuleSw_LSB1SRP2E0,
       "hh3cevtModuleSw-LSB1SRP2E1": hh3cevtModuleSw_LSB1SRP2E1,
       "hh3cevtModuleSw-LSB1SRP2E2": hh3cevtModuleSw_LSB1SRP2E2,
       "hh3cevtModuleSw-LSB1SRP2E3": hh3cevtModuleSw_LSB1SRP2E3,
       "hh3cevtModuleSw-SR01SRPUQ": hh3cevtModuleSw_SR01SRPUQ,
       "hh3cevtModuleSw-AHP1": hh3cevtModuleSw_AHP1,
       "hh3cevtModuleSw-AHP2": hh3cevtModuleSw_AHP2,
       "hh3cevtModuleSw-CLP1": hh3cevtModuleSw_CLP1,
       "hh3cevtModuleSw-CLP2": hh3cevtModuleSw_CLP2,
       "hh3cevtModuleSw-ET16": hh3cevtModuleSw_ET16,
       "hh3cevtModuleSw-LSB1SRP1NA0": hh3cevtModuleSw_LSB1SRP1NA0,
       "hh3cevtModuleSw-LSB1SRP1NA1": hh3cevtModuleSw_LSB1SRP1NA1,
       "hh3cevtModuleSw-LSB1SRP1NA2": hh3cevtModuleSw_LSB1SRP1NA2,
       "hh3cevtModuleSw-LSB1SRP1NA3": hh3cevtModuleSw_LSB1SRP1NA3,
       "hh3cevtModuleSw-SR01AHP1GWA": hh3cevtModuleSw_SR01AHP1GWA,
       "hh3cevtModuleSw-SR01AHP2GWA": hh3cevtModuleSw_SR01AHP2GWA,
       "hh3cevtModuleSw-SR01CLP1GWA": hh3cevtModuleSw_SR01CLP1GWA,
       "hh3cevtModuleSw-SR01CLP2GWA": hh3cevtModuleSw_SR01CLP2GWA,
       "hh3cevtModuleSw-SR01ET16GWA": hh3cevtModuleSw_SR01ET16GWA,
       "hh3cevtModuleSw-SR01GP12VB": hh3cevtModuleSw_SR01GP12VB,
       "hh3cevtModuleSw-SR01XK1VB": hh3cevtModuleSw_SR01XK1VB,
       "hh3cevtModuleSw-SR01XP2VC": hh3cevtModuleSw_SR01XP2VC,
       "hh3cevtModuleSw-SR01XP4LVB": hh3cevtModuleSw_SR01XP4LVB,
       "hh3cevtModuleSw-SR01SRPUEA": hh3cevtModuleSw_SR01SRPUEA,
       "hh3cevtModuleSw-LSB1SRP1N4": hh3cevtModuleSw_LSB1SRP1N4,
       "hh3cevtModuleSw-LSB1SRP1N5": hh3cevtModuleSw_LSB1SRP1N5,
       "hh3cevtModuleSw-LSB1SRP1N6": hh3cevtModuleSw_LSB1SRP1N6,
       "hh3cevtModuleSw-LSB1SRP1N7": hh3cevtModuleSw_LSB1SRP1N7,
       "hh3cevtModuleSw-LSB1SRP2N4": hh3cevtModuleSw_LSB1SRP2N4,
       "hh3cevtModuleSw-LSB1SRP2N5": hh3cevtModuleSw_LSB1SRP2N5,
       "hh3cevtModuleSw-LSB1SRP2N6": hh3cevtModuleSw_LSB1SRP2N6,
       "hh3cevtModuleSw-LSB1SRP2N7": hh3cevtModuleSw_LSB1SRP2N7,
       "hh3cevtModuleSw-LSB1SRP1NA4": hh3cevtModuleSw_LSB1SRP1NA4,
       "hh3cevtModuleSw-LSB1SRP1NA5": hh3cevtModuleSw_LSB1SRP1NA5,
       "hh3cevtModuleSw-LSB1SRP1NA6": hh3cevtModuleSw_LSB1SRP1NA6,
       "hh3cevtModuleSw-LSB1SRP1NA7": hh3cevtModuleSw_LSB1SRP1NA7,
       "hh3cevtModuleSw-LSB2GV48DA": hh3cevtModuleSw_LSB2GV48DA,
       "hh3cevtModuleSw-LSB1RGP2GDB": hh3cevtModuleSw_LSB1RGP2GDB,
       "hh3cevtModuleSw-LSB1RGP4GDB": hh3cevtModuleSw_LSB1RGP4GDB,
       "hh3cevtModuleSw-LSB2GP24DB": hh3cevtModuleSw_LSB2GP24DB,
       "hh3cevtModuleSw-LSB2GP24DC": hh3cevtModuleSw_LSB2GP24DC,
       "hh3cevtModuleSw-LSB2GT24DB": hh3cevtModuleSw_LSB2GT24DB,
       "hh3cevtModuleSw-LSB2FW8DB": hh3cevtModuleSw_LSB2FW8DB,
       "hh3cevtModuleSw-LSB2IPSEC8DB": hh3cevtModuleSw_LSB2IPSEC8DB,
       "hh3cevtModuleSw-LSB2GV48DB": hh3cevtModuleSw_LSB2GV48DB,
       "hh3cevtModuleSw-RGP2": hh3cevtModuleSw_RGP2,
       "hh3cevtModuleSw-RGP4": hh3cevtModuleSw_RGP4,
       "hh3cevtModuleSw-SR02FW8VB": hh3cevtModuleSw_SR02FW8VB,
       "hh3cevtModuleSw-SR02IPSEC8VB": hh3cevtModuleSw_SR02IPSEC8VB,
       "hh3cevtModuleSw-LSB2SRP1N0": hh3cevtModuleSw_LSB2SRP1N0,
       "hh3cevtModuleSw-LSB2SRP1N1": hh3cevtModuleSw_LSB2SRP1N1,
       "hh3cevtModuleSw-LSB2SRP1N2": hh3cevtModuleSw_LSB2SRP1N2,
       "hh3cevtModuleSw-LSB2SRP1N3": hh3cevtModuleSw_LSB2SRP1N3,
       "hh3cevtModuleSw-LSB2SRP1N4": hh3cevtModuleSw_LSB2SRP1N4,
       "hh3cevtModuleSw-LSB2SRP1N5": hh3cevtModuleSw_LSB2SRP1N5,
       "hh3cevtModuleSw-LSB2SRP1N6": hh3cevtModuleSw_LSB2SRP1N6,
       "hh3cevtModuleSw-LSB2SRP1N7": hh3cevtModuleSw_LSB2SRP1N7,
       "hh3cevtModuleSw-SR02SRPUE": hh3cevtModuleSw_SR02SRPUE,
       "hh3cevtModuleSw-SR01LN1BQH0": hh3cevtModuleSw_SR01LN1BQH0,
       "hh3cevtModuleSw-SR01DXP1L": hh3cevtModuleSw_SR01DXP1L,
       "hh3cevtModuleSw-SR01DGP10L": hh3cevtModuleSw_SR01DGP10L,
       "hh3cevtModuleSw-SR01DRSP2L": hh3cevtModuleSw_SR01DRSP2L,
       "hh3cevtModuleSw-SR01DRUP1L": hh3cevtModuleSw_SR01DRUP1L,
       "hh3cevtModuleSw-SR01DGP20R": hh3cevtModuleSw_SR01DGP20R,
       "hh3cevtModuleSw-SR01DPLP8L": hh3cevtModuleSw_SR01DPLP8L,
       "hh3cevtModuleSw-SR01DXP2R": hh3cevtModuleSw_SR01DXP2R,
       "hh3cevtModuleSw-LSB1FW2A0": hh3cevtModuleSw_LSB1FW2A0,
       "hh3cevtModuleSw-LSB1GP48LDB": hh3cevtModuleSw_LSB1GP48LDB,
       "hh3cevtModuleSw-SR01LN1BNA0": hh3cevtModuleSw_SR01LN1BNA0,
       "hh3cevtModuleSw-SR01LN2BQH0": hh3cevtModuleSw_SR01LN2BQH0,
       "hh3cevtModuleSw-SR01LN2BNA0": hh3cevtModuleSw_SR01LN2BNA0,
       "hh3cevtModuleSw-SR01DGT20R": hh3cevtModuleSw_SR01DGT20R,
       "hh3cevtModuleSw-SR01DPSP4L": hh3cevtModuleSw_SR01DPSP4L,
       "hh3cevtModuleSw-SR01DPUP1L": hh3cevtModuleSw_SR01DPUP1L,
       "hh3cevtModuleSw-SR01DPL2G6L": hh3cevtModuleSw_SR01DPL2G6L,
       "hh3cevtModuleSw-SR01DPH2G6L": hh3cevtModuleSw_SR01DPH2G6L,
       "hh3cevtModuleSw-SR01DPS2G4L": hh3cevtModuleSw_SR01DPS2G4L,
       "hh3cevtModuleSw-SR01DCL1G8L": hh3cevtModuleSw_SR01DCL1G8L,
       "hh3cevtModuleSw-SR01DCL2G8L": hh3cevtModuleSw_SR01DCL2G8L,
       "hh3cevtModuleSw-SR01DET8G8L": hh3cevtModuleSw_SR01DET8G8L,
       "hh3cevtModuleSw-SR02SRP2E3": hh3cevtModuleSw_SR02SRP2E3,
       "hh3cevtModuleSw-SR02SRP1E3": hh3cevtModuleSw_SR02SRP1E3,
       "hh3cevtModuleSw-SR02SRP1M3": hh3cevtModuleSw_SR02SRP1M3,
       "hh3cevtModuleSw-SR01DQCP4L": hh3cevtModuleSw_SR01DQCP4L,
       "hh3cevtModuleSw-SR01DTCP8L": hh3cevtModuleSw_SR01DTCP8L,
       "hh3cevtModuleSw-LSB1AFC1A0": hh3cevtModuleSw_LSB1AFC1A0,
       "hh3cevtModuleSw-LSB1SSL1A0": hh3cevtModuleSw_LSB1SSL1A0,
       "hh3cevtModuleSw-IMNAM": hh3cevtModuleSw_IMNAM,
       "hh3cevtModuleSw-IMNAT": hh3cevtModuleSw_IMNAT,
       "hh3cevtModuleSw-PICAHP1L": hh3cevtModuleSw_PICAHP1L,
       "hh3cevtModuleSw-PICALP4L": hh3cevtModuleSw_PICALP4L,
       "hh3cevtModuleSw-PICCHP4L": hh3cevtModuleSw_PICCHP4L,
       "hh3cevtModuleSw-PICCHS1G4L": hh3cevtModuleSw_PICCHS1G4L,
       "hh3cevtModuleSw-PICCLS4G4L": hh3cevtModuleSw_PICCLS4G4L,
       "hh3cevtModuleSw-PICCSP1L": hh3cevtModuleSw_PICCSP1L,
       "hh3cevtModuleSw-LSB1ACG1A0": hh3cevtModuleSw_LSB1ACG1A0,
       "hh3cevtModuleSw-LST1MRPNC1": hh3cevtModuleSw_LST1MRPNC1,
       "hh3cevtModuleSw-LST1SF18B1": hh3cevtModuleSw_LST1SF18B1,
       "hh3cevtModuleSw-LST1SF08B1": hh3cevtModuleSw_LST1SF08B1,
       "hh3cevtModuleSw-LST1GT48LEC1": hh3cevtModuleSw_LST1GT48LEC1,
       "hh3cevtModuleSw-LST1GP48LEC1": hh3cevtModuleSw_LST1GP48LEC1,
       "hh3cevtModuleSw-LST1XP4LEC1": hh3cevtModuleSw_LST1XP4LEC1,
       "hh3cevtModuleSw-LST1XP8LEC1": hh3cevtModuleSw_LST1XP8LEC1,
       "hh3cevtModuleSw-LSR1SRP2B1": hh3cevtModuleSw_LSR1SRP2B1,
       "hh3cevtModuleSw-LSR1SRP2C1": hh3cevtModuleSw_LSR1SRP2C1,
       "hh3cevtModuleSw-LSR1SRP2B2": hh3cevtModuleSw_LSR1SRP2B2,
       "hh3cevtModuleSw-LSR1SRP2C2": hh3cevtModuleSw_LSR1SRP2C2,
       "hh3cevtModuleSw-LSR1GT24LEC1": hh3cevtModuleSw_LSR1GT24LEC1,
       "hh3cevtModuleSw-LSR1GP24LEB1": hh3cevtModuleSw_LSR1GP24LEB1,
       "hh3cevtModuleSw-LSR1GP24LEC1": hh3cevtModuleSw_LSR1GP24LEC1,
       "hh3cevtModuleSw-LSR1GT48LEB1": hh3cevtModuleSw_LSR1GT48LEB1,
       "hh3cevtModuleSw-LSR1GT48LEC1": hh3cevtModuleSw_LSR1GT48LEC1,
       "hh3cevtModuleSw-LSR1GP48LEB1": hh3cevtModuleSw_LSR1GP48LEB1,
       "hh3cevtModuleSw-LSR1GP48LEC1": hh3cevtModuleSw_LSR1GP48LEC1,
       "hh3cevtModuleSw-LSR2GV48REB1": hh3cevtModuleSw_LSR2GV48REB1,
       "hh3cevtModuleSw-LSR1XP2LEB1": hh3cevtModuleSw_LSR1XP2LEB1,
       "hh3cevtModuleSw-LSR1XP2LEC1": hh3cevtModuleSw_LSR1XP2LEC1,
       "hh3cevtModuleSw-LSR1XP4LEB1": hh3cevtModuleSw_LSR1XP4LEB1,
       "hh3cevtModuleSw-LSR1XP4LEC1": hh3cevtModuleSw_LSR1XP4LEC1,
       "hh3cevtModuleSw-IMFW": hh3cevtModuleSw_IMFW,
       "hh3cevtModuleSw-LSB1LB1A0": hh3cevtModuleSw_LSB1LB1A0,
       "hh3cevtModuleSw-LSB1IPS1A0": hh3cevtModuleSw_LSB1IPS1A0,
       "hh3cevtModuleSw-LST1GT48LEB1": hh3cevtModuleSw_LST1GT48LEB1,
       "hh3cevtModuleSw-LST1GP48LEB1": hh3cevtModuleSw_LST1GP48LEB1,
       "hh3cevtModuleSw-LST1XP4LEB1": hh3cevtModuleSw_LST1XP4LEB1,
       "hh3cevtModuleSw-LST1XP8LEB1": hh3cevtModuleSw_LST1XP8LEB1,
       "hh3cevtModuleSw-LST1XP32REB1": hh3cevtModuleSw_LST1XP32REB1,
       "hh3cevtModuleSw-LST1XP32REC1": hh3cevtModuleSw_LST1XP32REC1,
       "hh3cevtModuleSw-LSR1FW2A1": hh3cevtModuleSw_LSR1FW2A1,
       "hh3cevtModuleSw-LSR1SSL1A1": hh3cevtModuleSw_LSR1SSL1A1,
       "hh3cevtModuleSw-SR01DET32G2L": hh3cevtModuleSw_SR01DET32G2L,
       "hh3cevtModuleSw-LSR1GP24LEF1": hh3cevtModuleSw_LSR1GP24LEF1,
       "hh3cevtModuleSw-LSR1XP4LEF1": hh3cevtModuleSw_LSR1XP4LEF1,
       "hh3cevtModuleSw-LSR1LB1A1": hh3cevtModuleSw_LSR1LB1A1,
       "hh3cevtModuleSw-LSR1NSM1A1": hh3cevtModuleSw_LSR1NSM1A1,
       "hh3cevtModuleSw-LSR1ACG1A1": hh3cevtModuleSw_LSR1ACG1A1,
       "hh3cevtModuleSw-LSR1IPS1A1": hh3cevtModuleSw_LSR1IPS1A1,
       "hh3cevtModuleSw-LSR2GP24LEB1": hh3cevtModuleSw_LSR2GP24LEB1,
       "hh3cevtModuleSw-LSR2GT24LEB1": hh3cevtModuleSw_LSR2GT24LEB1,
       "hh3cevtModuleSw-LSR2GT48LEB1": hh3cevtModuleSw_LSR2GT48LEB1,
       "hh3cevtModuleSw-SPC-GP24L": hh3cevtModuleSw_SPC_GP24L,
       "hh3cevtModuleSw-SPC-GT48L": hh3cevtModuleSw_SPC_GT48L,
       "hh3cevtModuleSw-SPC-GP48L": hh3cevtModuleSw_SPC_GP48L,
       "hh3cevtModuleSw-SPC-XP2L": hh3cevtModuleSw_SPC_XP2L,
       "hh3cevtModuleSw-SPC-XP4L": hh3cevtModuleSw_SPC_XP4L,
       "hh3cevtModuleSw-SR06SRP2E3": hh3cevtModuleSw_SR06SRP2E3,
       "hh3cevtModuleSw-SPE-2010-E": hh3cevtModuleSw_SPE_2010_E,
       "hh3cevtModuleSw-SPE-2020-E": hh3cevtModuleSw_SPE_2020_E,
       "hh3cevtModuleSw-SPC-XP4L-S-SDI": hh3cevtModuleSw_SPC_XP4L_S_SDI,
       "hh3cevtModuleSw-SPC-GT48L-SDI": hh3cevtModuleSw_SPC_GT48L_SDI,
       "hh3cevtModuleSw-SPC-GP48L-S-SDI": hh3cevtModuleSw_SPC_GP48L_S_SDI,
       "hh3cevtModuleSw-SPC-SR02OPMA0": hh3cevtModuleSw_SPC_SR02OPMA0,
       "hh3cevtModuleSw-LSR1XP16REB1": hh3cevtModuleSw_LSR1XP16REB1,
       "hh3cevtModuleSw-LSR1GP48LEF1": hh3cevtModuleSw_LSR1GP48LEF1,
       "hh3cevtModuleSw-LST1GP48LEF1": hh3cevtModuleSw_LST1GP48LEF1,
       "hh3cevtModuleSw-LST1XP8LEF1": hh3cevtModuleSw_LST1XP8LEF1,
       "hh3cevtModuleSw-SPE-1010-II": hh3cevtModuleSw_SPE_1010_II,
       "hh3cevtModuleSw-SPE-1010-E-II": hh3cevtModuleSw_SPE_1010_E_II,
       "hh3cevtModuleSw-SPE-1020-II": hh3cevtModuleSw_SPE_1020_II,
       "hh3cevtModuleSw-SPE-1020-E-II": hh3cevtModuleSw_SPE_1020_E_II,
       "hh3cevtModuleSw-LST1FW2A1": hh3cevtModuleSw_LST1FW2A1,
       "hh3cevtModuleSw-LST1NSM1A1": hh3cevtModuleSw_LST1NSM1A1,
       "hh3cevtModuleSw-LST1LB1A1": hh3cevtModuleSw_LST1LB1A1,
       "hh3cevtModuleSw-LST1ACG1A1": hh3cevtModuleSw_LST1ACG1A1,
       "hh3cevtModuleSw-LST1IPS1A1": hh3cevtModuleSw_LST1IPS1A1,
       "hh3cevtModuleSw-LSR1DRUP1L1": hh3cevtModuleSw_LSR1DRUP1L1,
       "hh3cevtModuleSw-LSR1DPUP1L1": hh3cevtModuleSw_LSR1DPUP1L1,
       "hh3cevtModuleSw-LSR1DPSP4L1": hh3cevtModuleSw_LSR1DPSP4L1,
       "hh3cevtModuleSw-LSR1DTCP8L1": hh3cevtModuleSw_LSR1DTCP8L1,
       "hh3cevtModuleSw-LSR1DXP1L1": hh3cevtModuleSw_LSR1DXP1L1,
       "hh3cevtModuleSw-LSR1DGP10L1": hh3cevtModuleSw_LSR1DGP10L1,
       "hh3cevtModuleSw-LSR1LN1BNL1": hh3cevtModuleSw_LSR1LN1BNL1,
       "hh3cevtModuleSw-LSR1LN2BL1": hh3cevtModuleSw_LSR1LN2BL1,
       "hh3cevtModuleSw-LSR1SRP2D1": hh3cevtModuleSw_LSR1SRP2D1,
       "hh3cevtModuleSw-IM-NAT-II": hh3cevtModuleSw_IM_NAT_II,
       "hh3cevtModuleSw-IM-NAM-II": hh3cevtModuleSw_IM_NAM_II,
       "hh3cevtModuleSw-CR-MRP-I": hh3cevtModuleSw_CR_MRP_I,
       "hh3cevtModuleSw-CR-SF18C": hh3cevtModuleSw_CR_SF18C,
       "hh3cevtModuleSw-CR-SF08C": hh3cevtModuleSw_CR_SF08C,
       "hh3cevtModuleSw-CR-SPC-XP8LEF": hh3cevtModuleSw_CR_SPC_XP8LEF,
       "hh3cevtModuleSw-CR-SPC-XP4LEF": hh3cevtModuleSw_CR_SPC_XP4LEF,
       "hh3cevtModuleSw-CR-SPC-GP48LEF": hh3cevtModuleSw_CR_SPC_GP48LEF,
       "hh3cevtModuleSw-CR-SPC-GT48LEF": hh3cevtModuleSw_CR_SPC_GT48LEF,
       "hh3cevtModuleSw-CR-SPE-3020-E": hh3cevtModuleSw_CR_SPE_3020_E,
       "hh3cevtModuleSw-CR-SPC-PUP4L-E": hh3cevtModuleSw_CR_SPC_PUP4L_E,
       "hh3cevtModuleSw-LST1SF08C1": hh3cevtModuleSw_LST1SF08C1,
       "hh3cevtModuleSw-LST1SF18C1": hh3cevtModuleSw_LST1SF18C1,
       "hh3cevtModuleSw-LS81GP16TM": hh3cevtModuleSw_LS81GP16TM,
       "hh3cevtModuleSw-LS81VP4C": hh3cevtModuleSw_LS81VP4C,
       "hh3cevtModuleSw-LS8M1PT8P0": hh3cevtModuleSw_LS8M1PT8P0,
       "hh3cevtModuleSw-LS8M1PT8GB0": hh3cevtModuleSw_LS8M1PT8GB0,
       "hh3cevtModuleSw-LS8M1PT4GB0": hh3cevtModuleSw_LS8M1PT4GB0,
       "hh3cevtModuleSw-LS81GP2R": hh3cevtModuleSw_LS81GP2R,
       "hh3cevtModuleSw-LS81GP4R": hh3cevtModuleSw_LS81GP4R,
       "hh3cevtModuleSw-LS81IPSECA": hh3cevtModuleSw_LS81IPSECA,
       "hh3cevtModuleSw-LS81FWA": hh3cevtModuleSw_LS81FWA,
       "hh3cevtModuleSw-LS82VSNP": hh3cevtModuleSw_LS82VSNP,
       "hh3cevtModuleSw-LSQ1GV48SA": hh3cevtModuleSw_LSQ1GV48SA,
       "hh3cevtModuleSw-LSQ1SRPB": hh3cevtModuleSw_LSQ1SRPB,
       "hh3cevtModuleSw-LSQ1SRP2XB": hh3cevtModuleSw_LSQ1SRP2XB,
       "hh3cevtModuleSw-LSQ1SRP1CB": hh3cevtModuleSw_LSQ1SRP1CB,
       "hh3cevtModuleSw-LSQ1FV48SA": hh3cevtModuleSw_LSQ1FV48SA,
       "hh3cevtModuleSw-LSD1MPUA": hh3cevtModuleSw_LSD1MPUA,
       "hh3cevtModuleSw-LSD1GP20A0": hh3cevtModuleSw_LSD1GP20A0,
       "hh3cevtModuleSw-LSD1GP20TA0": hh3cevtModuleSw_LSD1GP20TA0,
       "hh3cevtModuleSw-LSD1GP36A0": hh3cevtModuleSw_LSD1GP36A0,
       "hh3cevtModuleSw-LSD1GP20XA0": hh3cevtModuleSw_LSD1GP20XA0,
       "hh3cevtModuleSw-LSD1GP20EA0": hh3cevtModuleSw_LSD1GP20EA0,
       "hh3cevtModuleSw-LSD1GP20RA0": hh3cevtModuleSw_LSD1GP20RA0,
       "hh3cevtModuleSw-LSD1GP16A0": hh3cevtModuleSw_LSD1GP16A0,
       "hh3cevtModuleSw-LSD1GT16A0": hh3cevtModuleSw_LSD1GT16A0,
       "hh3cevtModuleSw-LSD1XP2A0": hh3cevtModuleSw_LSD1XP2A0,
       "hh3cevtModuleSw-LSD1EP2A0": hh3cevtModuleSw_LSD1EP2A0,
       "hh3cevtModuleSw-LSD1RP2A0": hh3cevtModuleSw_LSD1RP2A0,
       "hh3cevtModuleSw-LSQ1GV48SC": hh3cevtModuleSw_LSQ1GV48SC,
       "hh3cevtModuleSw-LSQ1FP48SA": hh3cevtModuleSw_LSQ1FP48SA,
       "hh3cevtModuleSw-LSQ1GP24SC": hh3cevtModuleSw_LSQ1GP24SC,
       "hh3cevtModuleSw-LSQ1GT24SC": hh3cevtModuleSw_LSQ1GT24SC,
       "hh3cevtModuleSw-LSQ1TGX2SC": hh3cevtModuleSw_LSQ1TGX2SC,
       "hh3cevtModuleSw-LSQ1GP12EA": hh3cevtModuleSw_LSQ1GP12EA,
       "hh3cevtModuleSw-LSQ1TGX1EA": hh3cevtModuleSw_LSQ1TGX1EA,
       "hh3cevtModuleSw-LSQ1P24XGSC": hh3cevtModuleSw_LSQ1P24XGSC,
       "hh3cevtModuleSw-LSQ1T24XGSC": hh3cevtModuleSw_LSQ1T24XGSC,
       "hh3cevtModuleSw-LS81TGX1B": hh3cevtModuleSw_LS81TGX1B,
       "hh3cevtModuleSw-LSQ1PT4PSC0": hh3cevtModuleSw_LSQ1PT4PSC0,
       "hh3cevtModuleSw-LS81SRPG13": hh3cevtModuleSw_LS81SRPG13,
       "hh3cevtModuleSw-LS81SRPG14": hh3cevtModuleSw_LS81SRPG14,
       "hh3cevtModuleSw-LS81SRPG15": hh3cevtModuleSw_LS81SRPG15,
       "hh3cevtModuleSw-LSQ1GP48SC0": hh3cevtModuleSw_LSQ1GP48SC0,
       "hh3cevtModuleSw-LSQ1GP12SC0": hh3cevtModuleSw_LSQ1GP12SC0,
       "hh3cevtModuleSw-LSD1SRPA": hh3cevtModuleSw_LSD1SRPA,
       "hh3cevtModuleSw-LSD1SRPB": hh3cevtModuleSw_LSD1SRPB,
       "hh3cevtModuleSw-LSD1SRPC": hh3cevtModuleSw_LSD1SRPC,
       "hh3cevtModuleSw-LSD1GT16PES0": hh3cevtModuleSw_LSD1GT16PES0,
       "hh3cevtModuleSw-LSD1GP24ES0": hh3cevtModuleSw_LSD1GP24ES0,
       "hh3cevtModuleSw-LSD1GT24XES0": hh3cevtModuleSw_LSD1GT24XES0,
       "hh3cevtModuleSw-LSD1GP24XES0": hh3cevtModuleSw_LSD1GP24XES0,
       "hh3cevtModuleSw-LSD1XP2ES0": hh3cevtModuleSw_LSD1XP2ES0,
       "hh3cevtModuleSw-LSD1GP48ES0": hh3cevtModuleSw_LSD1GP48ES0,
       "hh3cevtModuleSw-LSQ1MPUA0": hh3cevtModuleSw_LSQ1MPUA0,
       "hh3cevtModuleSw-LSQ1MPUA1": hh3cevtModuleSw_LSQ1MPUA1,
       "hh3cevtModuleSw-LSQ1FWBSC0": hh3cevtModuleSw_LSQ1FWBSC0,
       "hh3cevtModuleSw-LSQ1PT8PSC0": hh3cevtModuleSw_LSQ1PT8PSC0,
       "hh3cevtModuleSw-LSQ1PT16PSC0": hh3cevtModuleSw_LSQ1PT16PSC0,
       "hh3cevtModuleSw-SA11MPUA0": hh3cevtModuleSw_SA11MPUA0,
       "hh3cevtModuleSw-SA11MPUB0": hh3cevtModuleSw_SA11MPUB0,
       "hh3cevtModuleSw-LSQ1AFCBSC0": hh3cevtModuleSw_LSQ1AFCBSC0,
       "hh3cevtModuleSw-LSQ1MPUB0": hh3cevtModuleSw_LSQ1MPUB0,
       "hh3cevtModuleSw-LSQ1MPUB1": hh3cevtModuleSw_LSQ1MPUB1,
       "hh3cevtModuleSw-LSQ1PT4PSC1": hh3cevtModuleSw_LSQ1PT4PSC1,
       "hh3cevtModuleSw-LSQ1PT8PSC1": hh3cevtModuleSw_LSQ1PT8PSC1,
       "hh3cevtModuleSw-LSQ1PT16PSC1": hh3cevtModuleSw_LSQ1PT16PSC1,
       "hh3cevtModuleSw-LSQ1FP48USA0": hh3cevtModuleSw_LSQ1FP48USA0,
       "hh3cevtModuleSw-LSQ1FP48USA1": hh3cevtModuleSw_LSQ1FP48USA1,
       "hh3cevtModuleSw-LSQ1FV48USA0": hh3cevtModuleSw_LSQ1FV48USA0,
       "hh3cevtModuleSw-LSQ1FV48USA1": hh3cevtModuleSw_LSQ1FV48USA1,
       "hh3cevtModuleSw-LSQ1SRPD0": hh3cevtModuleSw_LSQ1SRPD0,
       "hh3cevtModuleSw-LSQ1CGP24TSC0": hh3cevtModuleSw_LSQ1CGP24TSC0,
       "hh3cevtModuleSw-LSQ1GP24TSC0": hh3cevtModuleSw_LSQ1GP24TSC0,
       "hh3cevtModuleSw-LSQ1ACGASC0": hh3cevtModuleSw_LSQ1ACGASC0,
       "hh3cevtModuleSw-LSD1XP1ES0": hh3cevtModuleSw_LSD1XP1ES0,
       "hh3cevtModuleSw-LSD1GP12ES0": hh3cevtModuleSw_LSD1GP12ES0,
       "hh3cevtModuleSw-LSQ1SRP12GB0": hh3cevtModuleSw_LSQ1SRP12GB0,
       "hh3cevtModuleSw-LSQ1GV40PSC0": hh3cevtModuleSw_LSQ1GV40PSC0,
       "hh3cevtModuleSw-LSQ1FWBSC1": hh3cevtModuleSw_LSQ1FWBSC1,
       "hh3cevtModuleSw-LSQ1NSMSC0": hh3cevtModuleSw_LSQ1NSMSC0,
       "hh3cevtModuleSw-LSQ1NSMSC1": hh3cevtModuleSw_LSQ1NSMSC1,
       "hh3cevtModuleSw-LSQ1AFDBSC0": hh3cevtModuleSw_LSQ1AFDBSC0,
       "hh3cevtModuleSw-LS81MPUB": hh3cevtModuleSw_LS81MPUB,
       "hh3cevtModuleSw-LS81FP48XL": hh3cevtModuleSw_LS81FP48XL,
       "hh3cevtModuleSw-LS81FT48XL": hh3cevtModuleSw_LS81FT48XL,
       "hh3cevtModuleSw-LS81GP12XL": hh3cevtModuleSw_LS81GP12XL,
       "hh3cevtModuleSw-LS81GP24XL": hh3cevtModuleSw_LS81GP24XL,
       "hh3cevtModuleSw-LS81GP48XL": hh3cevtModuleSw_LS81GP48XL,
       "hh3cevtModuleSw-LS81GT24XL": hh3cevtModuleSw_LS81GT24XL,
       "hh3cevtModuleSw-LS81GT48XL": hh3cevtModuleSw_LS81GT48XL,
       "hh3cevtModuleSw-LS81TGX2XL": hh3cevtModuleSw_LS81TGX2XL,
       "hh3cevtModuleSw-LSQ1GV48SD0": hh3cevtModuleSw_LSQ1GV48SD0,
       "hh3cevtModuleSw-LSQ1GP48EB0": hh3cevtModuleSw_LSQ1GP48EB0,
       "hh3cevtModuleSw-LSQ1IPSSC0": hh3cevtModuleSw_LSQ1IPSSC0,
       "hh3cevtModuleSw-LSQ1GV48SD1": hh3cevtModuleSw_LSQ1GV48SD1,
       "hh3cevtModuleSw-LSQ1GP48SD0": hh3cevtModuleSw_LSQ1GP48SD0,
       "hh3cevtModuleSw-LSQ1GP48SD1": hh3cevtModuleSw_LSQ1GP48SD1,
       "hh3cevtModuleSw-LSQ1SRPA0": hh3cevtModuleSw_LSQ1SRPA0,
       "hh3cevtModuleSw-LSQ1SRPA1": hh3cevtModuleSw_LSQ1SRPA1,
       "hh3cevtModuleSw-LSQ2FP48SA0": hh3cevtModuleSw_LSQ2FP48SA0,
       "hh3cevtModuleSw-LSQ2FP48SA1": hh3cevtModuleSw_LSQ2FP48SA1,
       "hh3cevtModuleSw-LSQ2FT48SA0": hh3cevtModuleSw_LSQ2FT48SA0,
       "hh3cevtModuleSw-LSQ2FT48SA1": hh3cevtModuleSw_LSQ2FT48SA1,
       "hh3cevtModuleSw-LSQ1GV24PSC0": hh3cevtModuleSw_LSQ1GV24PSC0,
       "hh3cevtModuleSw-LSQ1GV24PSC1": hh3cevtModuleSw_LSQ1GV24PSC1,
       "hh3cevtModuleSw-LSQ1CGV24PSC0": hh3cevtModuleSw_LSQ1CGV24PSC0,
       "hh3cevtModuleSw-LSQ1CGV24PSC1": hh3cevtModuleSw_LSQ1CGV24PSC1,
       "hh3cevtModuleSw-LSQ1GP24TEB0": hh3cevtModuleSw_LSQ1GP24TEB0,
       "hh3cevtModuleSw-LSQ1GP24TEB1": hh3cevtModuleSw_LSQ1GP24TEB1,
       "hh3cevtModuleSw-LSQ1GP24TSD0": hh3cevtModuleSw_LSQ1GP24TSD0,
       "hh3cevtModuleSw-LSQ1GP24TSD1": hh3cevtModuleSw_LSQ1GP24TSD1,
       "hh3cevtModuleSw-LSQ1GP24TXSD0": hh3cevtModuleSw_LSQ1GP24TXSD0,
       "hh3cevtModuleSw-LSQ1GP24TXSD1": hh3cevtModuleSw_LSQ1GP24TXSD1,
       "hh3cevtModuleSw-LSQ1TGX2EB0": hh3cevtModuleSw_LSQ1TGX2EB0,
       "hh3cevtModuleSw-LSQ1TGX2EB1": hh3cevtModuleSw_LSQ1TGX2EB1,
       "hh3cevtModuleSw-LSQ1TGX2SD0": hh3cevtModuleSw_LSQ1TGX2SD0,
       "hh3cevtModuleSw-LSQ1TGX2SD1": hh3cevtModuleSw_LSQ1TGX2SD1,
       "hh3cevtModuleSw-LSQ1TGX4SD0": hh3cevtModuleSw_LSQ1TGX4SD0,
       "hh3cevtModuleSw-LSQ1TGX4SD1": hh3cevtModuleSw_LSQ1TGX4SD1,
       "hh3cevtModuleSw-LSQ1TGX8SD0": hh3cevtModuleSw_LSQ1TGX8SD0,
       "hh3cevtModuleSw-LSQ1TGX8SD1": hh3cevtModuleSw_LSQ1TGX8SD1,
       "hh3cevtModuleSw-LSQ1GP48EB1": hh3cevtModuleSw_LSQ1GP48EB1,
       "hh3cevtModuleSw-LSQ1TGX4EB0": hh3cevtModuleSw_LSQ1TGX4EB0,
       "hh3cevtModuleSw-LSQ1TGX4EB1": hh3cevtModuleSw_LSQ1TGX4EB1,
       "hh3cevtModuleSw-LSQ1GP12SC3": hh3cevtModuleSw_LSQ1GP12SC3,
       "hh3cevtModuleSw-LSQ1GP24TSC3": hh3cevtModuleSw_LSQ1GP24TSC3,
       "hh3cevtModuleSw-LSQ1GP48SC3": hh3cevtModuleSw_LSQ1GP48SC3,
       "hh3cevtModuleSw-LSQ1GV48SC3": hh3cevtModuleSw_LSQ1GV48SC3,
       "hh3cevtModuleSw-LSQ1MPUA3": hh3cevtModuleSw_LSQ1MPUA3,
       "hh3cevtModuleSw-LSQ1SRP1CB3": hh3cevtModuleSw_LSQ1SRP1CB3,
       "hh3cevtModuleSw-LSQ1SRPA3": hh3cevtModuleSw_LSQ1SRPA3,
       "hh3cevtModuleSw-LSQ2FP48SA3": hh3cevtModuleSw_LSQ2FP48SA3,
       "hh3cevtModuleSw-LSQ2FT48SA3": hh3cevtModuleSw_LSQ2FT48SA3,
       "hh3cevtModuleSw-LSQ1MPUB3": hh3cevtModuleSw_LSQ1MPUB3,
       "hh3cevtModuleSw-LSQ1CGP24TSC3": hh3cevtModuleSw_LSQ1CGP24TSC3,
       "hh3cevtModuleSw-LSQ1MPUB4": hh3cevtModuleSw_LSQ1MPUB4,
       "hh3cevtModuleSw-LSQ1SRPD4": hh3cevtModuleSw_LSQ1SRPD4,
       "hh3cevtModuleSw-LSQ1SSLSC0": hh3cevtModuleSw_LSQ1SSLSC0,
       "hh3cevtModuleSw-LSQ1LBSC0": hh3cevtModuleSw_LSQ1LBSC0,
       "hh3cevtModuleSw-LSQ1NAT24SC0": hh3cevtModuleSw_LSQ1NAT24SC0,
       "hh3cevtModuleSw-LSQ1SRP12GB4": hh3cevtModuleSw_LSQ1SRP12GB4,
       "hh3cevtModuleSw-LSQ1TGS8SC0": hh3cevtModuleSw_LSQ1TGS8SC0,
       "hh3cevtModuleSw-LSQ3PT4PSC0": hh3cevtModuleSw_LSQ3PT4PSC0,
       "hh3cevtModuleSw-EWPXM2MPUB0": hh3cevtModuleSw_EWPXM2MPUB0,
       "hh3cevtModuleSw-EWPXM2SRP12GB0": hh3cevtModuleSw_EWPXM2SRP12GB0,
       "hh3cevtModuleSw-EWPXM2SRPD0": hh3cevtModuleSw_EWPXM2SRPD0,
       "hh3cevtModuleSw-EWPXM2GP24TSD0": hh3cevtModuleSw_EWPXM2GP24TSD0,
       "hh3cevtModuleSw-EWPXM2GP24TXSD0": hh3cevtModuleSw_EWPXM2GP24TXSD0,
       "hh3cevtModuleSw-EWPXM2TGX4SD0": hh3cevtModuleSw_EWPXM2TGX4SD0,
       "hh3cevtModuleSw-EWPXM2GP48SD0": hh3cevtModuleSw_EWPXM2GP48SD0,
       "hh3cevtModuleSw-EWPXM2GP24TSC0": hh3cevtModuleSw_EWPXM2GP24TSC0,
       "hh3cevtModuleSw-EWPXM2TGX2SC0": hh3cevtModuleSw_EWPXM2TGX2SC0,
       "hh3cevtModuleSw-EWPXM2GP48SC0": hh3cevtModuleSw_EWPXM2GP48SC0,
       "hh3cevtModuleSw-LS7500-GP48-SC": hh3cevtModuleSw_LS7500_GP48_SC,
       "hh3cevtModuleSw-LS7500-GP48-SD": hh3cevtModuleSw_LS7500_GP48_SD,
       "hh3cevtModuleSw-LS7500-GT48-SC": hh3cevtModuleSw_LS7500_GT48_SC,
       "hh3cevtModuleSw-LS7500-GT48-SD": hh3cevtModuleSw_LS7500_GT48_SD,
       "hh3cevtModuleSw-LS7500-SRPG1": hh3cevtModuleSw_LS7500_SRPG1,
       "hh3cevtModuleSw-LS7500-SRPG2": hh3cevtModuleSw_LS7500_SRPG2,
       "hh3cevtModuleSw-LS7500-XP4-SD": hh3cevtModuleSw_LS7500_XP4_SD,
       "hh3cevtModuleSw-LS7500-XP8-SD": hh3cevtModuleSw_LS7500_XP8_SD,
       "hh3cevtModuleSw-LSQ4PT4PSC0": hh3cevtModuleSw_LSQ4PT4PSC0,
       "hh3cevtModuleSw-LSQ4PT8PSC0": hh3cevtModuleSw_LSQ4PT8PSC0,
       "hh3cevtModuleSw-LSQ4PT16PSC0": hh3cevtModuleSw_LSQ4PT16PSC0,
       "hh3cevtModuleSw-LSQ1GP24TSA0": hh3cevtModuleSw_LSQ1GP24TSA0,
       "hh3cevtModuleSw-LSQ1GV24PSA0": hh3cevtModuleSw_LSQ1GV24PSA0,
       "hh3cevtModuleSw-LSQ1SRPD3": hh3cevtModuleSw_LSQ1SRPD3,
       "hh3cevtModuleSw-LSQ1SUPA0": hh3cevtModuleSw_LSQ1SUPA0,
       "hh3cevtModuleSw-LSU1FAB04A0": hh3cevtModuleSw_LSU1FAB04A0,
       "hh3cevtModuleSw-LSU1FAB08A0": hh3cevtModuleSw_LSU1FAB08A0,
       "hh3cevtModuleSw-LSU1TGS8EA0": hh3cevtModuleSw_LSU1TGS8EA0,
       "hh3cevtModuleSw-LSU1TGS8EB0": hh3cevtModuleSw_LSU1TGS8EB0,
       "hh3cevtModuleSw-LSU1TGS8SE0": hh3cevtModuleSw_LSU1TGS8SE0,
       "hh3cevtModuleSw-LSUTGS16SC0": hh3cevtModuleSw_LSUTGS16SC0,
       "hh3cevtModuleSw-LSU1SUPA0": hh3cevtModuleSw_LSU1SUPA0,
       "hh3cevtModuleSw-LSU1GP24TXEA0": hh3cevtModuleSw_LSU1GP24TXEA0,
       "hh3cevtModuleSw-LSU1GP24TXEB0": hh3cevtModuleSw_LSU1GP24TXEB0,
       "hh3cevtModuleSw-LSU1GP24TXSE0": hh3cevtModuleSw_LSU1GP24TXSE0,
       "hh3cevtModuleSw-LSU1GP48EA0": hh3cevtModuleSw_LSU1GP48EA0,
       "hh3cevtModuleSw-LSU1GP48EB0": hh3cevtModuleSw_LSU1GP48EB0,
       "hh3cevtModuleSw-LSU1GP48SE0": hh3cevtModuleSw_LSU1GP48SE0,
       "hh3cevtModuleSw-LSU1GT48EA0": hh3cevtModuleSw_LSU1GT48EA0,
       "hh3cevtModuleSw-LSU1GT48SE0": hh3cevtModuleSw_LSU1GT48SE0,
       "hh3cevtModuleSw-LSU1TGX4EA0": hh3cevtModuleSw_LSU1TGX4EA0,
       "hh3cevtModuleSw-LSU1TGX4EB0": hh3cevtModuleSw_LSU1TGX4EB0,
       "hh3cevtModuleSw-LSU1TGX4SE0": hh3cevtModuleSw_LSU1TGX4SE0,
       "hh3cevtModuleSw-LSQ1FAB08A0": hh3cevtModuleSw_LSQ1FAB08A0,
       "hh3cevtModuleSw-EWPX2WCMD0": hh3cevtModuleSw_EWPX2WCMD0,
       "hh3cevtModuleSw-LSQ1WCMD0": hh3cevtModuleSw_LSQ1WCMD0,
       "hh3cevtModuleSw-LSQ1IAGSC0": hh3cevtModuleSw_LSQ1IAGSC0,
       "hh3cevtModuleSw-LSU1GP24TSE0": hh3cevtModuleSw_LSU1GP24TSE0,
       "hh3cevtModuleSw-LSQ1TGS16SC0": hh3cevtModuleSw_LSQ1TGS16SC0,
       "hh3cevtModuleSw-EWPX2TGS16SC0": hh3cevtModuleSw_EWPX2TGS16SC0,
       "hh3cevtModuleSw-LSQ1SUPA3": hh3cevtModuleSw_LSQ1SUPA3,
       "hh3cevtModuleSw-LSQ1FAB04A3": hh3cevtModuleSw_LSQ1FAB04A3,
       "hh3cevtModuleSw-LSQ1FAB08A3": hh3cevtModuleSw_LSQ1FAB08A3,
       "hh3cevtModuleSw-LSQ1GT48SC0": hh3cevtModuleSw_LSQ1GT48SC0,
       "hh3cevtModuleSw-LSR2SRP2C1": hh3cevtModuleSw_LSR2SRP2C1,
       "hh3cevtModuleSw-LSR2SRP2C2": hh3cevtModuleSw_LSR2SRP2C2,
       "hh3cevtModuleSw-1000BASE-X-COMBO": hh3cevtModuleSw_1000BASE_X_COMBO,
       "hh3cevtModuleSw-EPON-1000M": hh3cevtModuleSw_EPON_1000M,
       "hh3cevtModuleSw-1000BASE-FIXED-2SFP-T-2RJ45": hh3cevtModuleSw_1000BASE_FIXED_2SFP_T_2RJ45,
       "hh3cevtModuleSw-100M-1550-BIDI": hh3cevtModuleSw_100M_1550_BIDI,
       "hh3cevtModuleSw-100M-1310-BIDI": hh3cevtModuleSw_100M_1310_BIDI,
       "hh3cevtModuleSw-1000BASE-FIXED-4RJ45-4SFP-COMBO": hh3cevtModuleSw_1000BASE_FIXED_4RJ45_4SFP_COMBO,
       "hh3cevtModuleSw-LSH1PK2T": hh3cevtModuleSw_LSH1PK2T,
       "hh3cevtModuleSw-LSPM2GP2P": hh3cevtModuleSw_LSPM2GP2P,
       "hh3cevtModuleSw-LSWM1GT16P": hh3cevtModuleSw_LSWM1GT16P,
       "hh3cevtModuleSw-LSWM1GP16P": hh3cevtModuleSw_LSWM1GP16P,
       "hh3cevtModuleSw-LSWM1XP2P": hh3cevtModuleSw_LSWM1XP2P,
       "hh3cevtModuleSw-LSWM1XP4P": hh3cevtModuleSw_LSWM1XP4P,
       "hh3cevtModuleSw-LSWM1SP2P": hh3cevtModuleSw_LSWM1SP2P,
       "hh3cevtModuleSw-LSWM1SP4P": hh3cevtModuleSw_LSWM1SP4P,
       "hh3cevtModuleSw-LSWM148POEM": hh3cevtModuleSw_LSWM148POEM,
       "hh3cevtModuleSw-LSWM1FW10": hh3cevtModuleSw_LSWM1FW10,
       "hh3cevtModuleSw-LSWM1WCM10": hh3cevtModuleSw_LSWM1WCM10,
       "hh3cevtModuleSw-LSWM1IPS10": hh3cevtModuleSw_LSWM1IPS10,
       "hh3cevtModuleSw-LSWM1WCM20": hh3cevtModuleSw_LSWM1WCM20,
       "hh3cevtModuleSw-IPS-T1000-M": hh3cevtModuleSw_IPS_T1000_M,
       "hh3cevtModuleSw-IPS-T1000-A": hh3cevtModuleSw_IPS_T1000_A,
       "hh3cevtModuleSw-IPS-T1000-S": hh3cevtModuleSw_IPS_T1000_S,
       "hh3cevtModuleSw-IPS-GX4C": hh3cevtModuleSw_IPS_GX4C,
       "hh3cevtModuleSw-IPS-GT4C": hh3cevtModuleSw_IPS_GT4C,
       "hh3cevtModuleSw-LSPM2SP2P": hh3cevtModuleSw_LSPM2SP2P,
       "hh3cevtModuleSw-LSPM2SP2PA": hh3cevtModuleSw_LSPM2SP2PA,
       "hh3cevtModuleSw-LSP5GP8P": hh3cevtModuleSw_LSP5GP8P,
       "hh3cevtModuleSw-LSP5GT8P": hh3cevtModuleSw_LSP5GT8P,
       "hh3cevtModuleSw-LSWM1FC4P": hh3cevtModuleSw_LSWM1FC4P,
       "hh3cevtModuleSw-LSW1XGT4P0": hh3cevtModuleSw_LSW1XGT4P0,
       "hh3cevtModuleSw-LSW1XGT2P0": hh3cevtModuleSw_LSW1XGT2P0,
       "hh3cevtModuleSw-LSP1XGT2P": hh3cevtModuleSw_LSP1XGT2P,
       "hh3cevtModuleSw-LSPM3XGT2P": hh3cevtModuleSw_LSPM3XGT2P,
       "hh3cevtModuleSw-LSWM2QP2P": hh3cevtModuleSw_LSWM2QP2P,
       "hh3cevtModuleSw-LSWM2XGT2PM": hh3cevtModuleSw_LSWM2XGT2PM,
       "hh3cevtModuleSw-LSWM2SP2PM": hh3cevtModuleSw_LSWM2SP2PM,
       "hh3cevtModuleSw-LSWM2SP8PM": hh3cevtModuleSw_LSWM2SP8PM,
       "hh3cevtModuleSw-LSWM2SP8P": hh3cevtModuleSw_LSWM2SP8P,
       "hh3cevtModuleSw-LSWM2XGT8PM": hh3cevtModuleSw_LSWM2XGT8PM,
       "hh3cevtModuleSw-LSWM18QC": hh3cevtModuleSw_LSWM18QC,
       "hh3cevtModuleSw-LSWM124XG2Q": hh3cevtModuleSw_LSWM124XG2Q,
       "hh3cevtModuleSw-LSWM124XGT2Q": hh3cevtModuleSw_LSWM124XGT2Q,
       "hh3cevtModuleSw-LSWM124XG2QL": hh3cevtModuleSw_LSWM124XG2QL,
       "hh3cevtModuleSw-LSWM124XG2QFC": hh3cevtModuleSw_LSWM124XG2QFC,
       "hh3cevtModuleSw-LSWM18QC0": hh3cevtModuleSw_LSWM18QC0,
       "hh3cevtModuleSw-LSWM124XGT2Q0": hh3cevtModuleSw_LSWM124XGT2Q0,
       "hh3cevtModuleSw-LSWM124XG2QL0": hh3cevtModuleSw_LSWM124XG2QL0,
       "hh3cevtModuleSw-LSP6G4T6P": hh3cevtModuleSw_LSP6G4T6P,
       "hh3cevtModuleSw-LSPM6QP2PS": hh3cevtModuleSw_LSPM6QP2PS,
       "hh3cevtModuleSw-LSWM12H2Q": hh3cevtModuleSw_LSWM12H2Q,
       "hh3cevtModuleSw-LSWM18CQ": hh3cevtModuleSw_LSWM18CQ,
       "hh3cevtModuleSw-LSWM116Q": hh3cevtModuleSw_LSWM116Q,
       "hh3cevtModuleSw-LSPM6FWD": hh3cevtModuleSw_LSPM6FWD,
       "hh3cevtModuleSw-DS-3E-2XT-H": hh3cevtModuleSw_DS_3E_2XT_H,
       "hh3cevtModuleSw-DS-3E-2XF-H": hh3cevtModuleSw_DS_3E_2XF_H,
       "hh3cevtModuleSw-DS-3E-2QX-H": hh3cevtModuleSw_DS_3E_2QX_H,
       "hh3cevtModuleSw-LSPM4G4T6P": hh3cevtModuleSw_LSPM4G4T6P,
       "hh3cevtModuleSw-LSWM4SP8PM": hh3cevtModuleSw_LSWM4SP8PM,
       "hh3cevtModuleSw-LSWM124TG2H": hh3cevtModuleSw_LSWM124TG2H,
       "hh3cevtModuleSw-LSWM18CQ0": hh3cevtModuleSw_LSWM18CQ0,
       "hh3cevtModuleSw-LSWM116Q0": hh3cevtModuleSw_LSWM116Q0,
       "hh3cevtModuleSw-LSWM124TG2H0": hh3cevtModuleSw_LSWM124TG2H0,
       "hh3cevtModuleSw-LSWM2ZQP2P": hh3cevtModuleSw_LSWM2ZQP2P,
       "hh3cevtModuleSw-LSWM2ZSP8P": hh3cevtModuleSw_LSWM2ZSP8P,
       "hh3cevtModuleSw-LSWM18CQMSEC": hh3cevtModuleSw_LSWM18CQMSEC,
       "hh3cevtModuleSw-LSWM2MGT8P": hh3cevtModuleSw_LSWM2MGT8P,
       "hh3cevtModuleSw-LSWM2XMGT8P": hh3cevtModuleSw_LSWM2XMGT8P,
       "hh3cevtModuleSw-LSWM2ZSP2P": hh3cevtModuleSw_LSWM2ZSP2P,
       "hh3cevtModuleSw-LSWM116FC": hh3cevtModuleSw_LSWM116FC,
       "hh3cevtModuleSw-LSWM216FC": hh3cevtModuleSw_LSWM216FC,
       "hh3cevtModuleSw-LSWM2SP2PB": hh3cevtModuleSw_LSWM2SP2PB,
       "hh3cevtModuleSw-LSWM2SP4PB": hh3cevtModuleSw_LSWM2SP4PB,
       "hh3cevtModuleSw-LSWM2SP24P": hh3cevtModuleSw_LSWM2SP24P,
       "hh3cevtModuleSw-LSWM2SP12P2Q": hh3cevtModuleSw_LSWM2SP12P2Q,
       "hh3cevtModuleSw-LSWM2SP12P2QA": hh3cevtModuleSw_LSWM2SP12P2QA,
       "hh3cevtModuleSw-DS-3E-2QX-HB": hh3cevtModuleSw_DS_3E_2QX_HB,
       "hh3cevtModuleSw-DS-3E-8XF-H": hh3cevtModuleSw_DS_3E_8XF_H,
       "hh3cevtModuleSw-LSWM116HC": hh3cevtModuleSw_LSWM116HC,
       "hh3cevtModuleSw-WX5002MPU": hh3cevtModuleSw_WX5002MPU,
       "hh3cevtModuleSw-LS8M1WCMA": hh3cevtModuleSw_LS8M1WCMA,
       "hh3cevtModuleSw-EWPX1G24XA0": hh3cevtModuleSw_EWPX1G24XA0,
       "hh3cevtModuleSw-LSQ1WCMB0": hh3cevtModuleSw_LSQ1WCMB0,
       "hh3cevtModuleSw-LSB1WCM2A0": hh3cevtModuleSw_LSB1WCM2A0,
       "hh3cevtModuleSw-EWPX1WCMB0": hh3cevtModuleSw_EWPX1WCMB0,
       "hh3cevtModuleSw-EWPX1G24XC0": hh3cevtModuleSw_EWPX1G24XC0,
       "hh3cevtModuleSw-EWPX1WCMC0": hh3cevtModuleSw_EWPX1WCMC0,
       "hh3cevtModuleSw-EWPX1FWA0": hh3cevtModuleSw_EWPX1FWA0,
       "hh3cevtModuleSw-EWPX1G10XC0": hh3cevtModuleSw_EWPX1G10XC0,
       "hh3cevtModuleSw-EWPX1WCM10C0": hh3cevtModuleSw_EWPX1WCM10C0,
       "hh3cevtModuleSw-LSR1WCM2A1": hh3cevtModuleSw_LSR1WCM2A1,
       "hh3cevtModuleSw-EWPX1WAP0": hh3cevtModuleSw_EWPX1WAP0,
       "hh3cevtModuleSw-EWPX1WCMD0": hh3cevtModuleSw_EWPX1WCMD0,
       "hh3cevtModuleSw-EWPX1G24XCE0": hh3cevtModuleSw_EWPX1G24XCE0,
       "hh3cevtModuleSw-EWPX1WCMCE0": hh3cevtModuleSw_EWPX1WCMCE0,
       "hh3cevtModuleSw-EWPX1G24XD0": hh3cevtModuleSw_EWPX1G24XD0,
       "hh3cevtModuleSw-EWPXM1XG03": hh3cevtModuleSw_EWPXM1XG03,
       "hh3cevtModuleSw-EWPXM2X": hh3cevtModuleSw_EWPXM2X,
       "hh3cevtModuleSw-EWPXM8G": hh3cevtModuleSw_EWPXM8G,
       "hh3cevtModuleSw-IOT-CARD-C1K": hh3cevtModuleSw_IOT_CARD_C1K,
       "hh3cevtModuleSw-EWPXM1BSTX80": hh3cevtModuleSw_EWPXM1BSTX80,
       "hh3cevtModuleSw-LSR1DRSP2L1": hh3cevtModuleSw_LSR1DRSP2L1,
       "hh3cevtModuleSw-PIC-CLF2G8L": hh3cevtModuleSw_PIC_CLF2G8L,
       "hh3cevtModuleSw-PIC-CLF4G8L": hh3cevtModuleSw_PIC_CLF4G8L,
       "hh3cevtModuleSw-SR02SRP2F3": hh3cevtModuleSw_SR02SRP2F3,
       "hh3cevtModuleSw-SR02SRP1F3": hh3cevtModuleSw_SR02SRP1F3,
       "hh3cevtModuleSw-LST1GT48LEA1": hh3cevtModuleSw_LST1GT48LEA1,
       "hh3cevtModuleSw-LST1GP48LEA1": hh3cevtModuleSw_LST1GP48LEA1,
       "hh3cevtModuleSw-LST2XP8LEA1": hh3cevtModuleSw_LST2XP8LEA1,
       "hh3cevtModuleSw-LST1GT48LEY1": hh3cevtModuleSw_LST1GT48LEY1,
       "hh3cevtModuleSw-LST1GP48LEY1": hh3cevtModuleSw_LST1GP48LEY1,
       "hh3cevtModuleSw-LST1XP32REY1": hh3cevtModuleSw_LST1XP32REY1,
       "hh3cevtModuleSw-LST1XP8LEY1": hh3cevtModuleSw_LST1XP8LEY1,
       "hh3cevtModuleSw-LST1GP48LEZ1": hh3cevtModuleSw_LST1GP48LEZ1,
       "hh3cevtModuleSw-LST1XP8LEZ1": hh3cevtModuleSw_LST1XP8LEZ1,
       "hh3cevtModuleSw-IM-FW-II": hh3cevtModuleSw_IM_FW_II,
       "hh3cevtModuleSw-IM-IPS": hh3cevtModuleSw_IM_IPS,
       "hh3cevtModuleSw-IM-SSL": hh3cevtModuleSw_IM_SSL,
       "hh3cevtModuleSw-IM-LB": hh3cevtModuleSw_IM_LB,
       "hh3cevtModuleSw-IM-ACG": hh3cevtModuleSw_IM_ACG,
       "hh3cevtModuleSw-LSR1XP16REC1": hh3cevtModuleSw_LSR1XP16REC1,
       "hh3cevtModuleSw-LST2XP8LEB1": hh3cevtModuleSw_LST2XP8LEB1,
       "hh3cevtModuleSw-LST2XP8LEC1": hh3cevtModuleSw_LST2XP8LEC1,
       "hh3cevtModuleSw-LST2XP8LEF1": hh3cevtModuleSw_LST2XP8LEF1,
       "hh3cevtModuleSw-LSR2XP4LEB1": hh3cevtModuleSw_LSR2XP4LEB1,
       "hh3cevtModuleSw-LSR2XP4LEC1": hh3cevtModuleSw_LSR2XP4LEC1,
       "hh3cevtModuleSw-LST2XP32REB1": hh3cevtModuleSw_LST2XP32REB1,
       "hh3cevtModuleSw-LST2XP32REC1": hh3cevtModuleSw_LST2XP32REC1,
       "hh3cevtModuleSw-LSR1WCM3A1": hh3cevtModuleSw_LSR1WCM3A1,
       "hh3cevtModuleSw-LST1XP16LEB1": hh3cevtModuleSw_LST1XP16LEB1,
       "hh3cevtModuleSw-LST1XP16LEC1": hh3cevtModuleSw_LST1XP16LEC1,
       "hh3cevtModuleSw-CR-SPC-XP4L-E-I": hh3cevtModuleSw_CR_SPC_XP4L_E_I,
       "hh3cevtModuleSw-LST2MRPNC1": hh3cevtModuleSw_LST2MRPNC1,
       "hh3cevtModuleSw-LST2SF08C1": hh3cevtModuleSw_LST2SF08C1,
       "hh3cevtModuleSw-LST2SF18C1": hh3cevtModuleSw_LST2SF18C1,
       "hh3cevtModuleSw-SR02SRP2G3": hh3cevtModuleSw_SR02SRP2G3,
       "hh3cevtModuleSw-CR-SPE-3020-E-I": hh3cevtModuleSw_CR_SPE_3020_E_I,
       "hh3cevtModuleSw-CR-SPC-PUP4L-E-I": hh3cevtModuleSw_CR_SPC_PUP4L_E_I,
       "hh3cevtModuleSw-CR-SPC-XP4LEF-I": hh3cevtModuleSw_CR_SPC_XP4LEF_I,
       "hh3cevtModuleSw-CR-SPC-XP8LEF-I": hh3cevtModuleSw_CR_SPC_XP8LEF_I,
       "hh3cevtModuleSw-LST3XP8LEB1": hh3cevtModuleSw_LST3XP8LEB1,
       "hh3cevtModuleSw-LST3XP8LEC1": hh3cevtModuleSw_LST3XP8LEC1,
       "hh3cevtModuleSw-LST1FW3A1": hh3cevtModuleSw_LST1FW3A1,
       "hh3cevtModuleSw-CR-IM-NAM1A": hh3cevtModuleSw_CR_IM_NAM1A,
       "hh3cevtModuleSw-LSR2SRP2B1": hh3cevtModuleSw_LSR2SRP2B1,
       "hh3cevtModuleSw-LSR2SRP2B2": hh3cevtModuleSw_LSR2SRP2B2,
       "hh3cevtModuleSw-LSR2SRP2D1": hh3cevtModuleSw_LSR2SRP2D1,
       "hh3cevtModuleSw-LST3XP8LEY1": hh3cevtModuleSw_LST3XP8LEY1,
       "hh3cevtModuleSw-LST2XP32REY1": hh3cevtModuleSw_LST2XP32REY1,
       "hh3cevtModuleSw-LST1XP16LEY1": hh3cevtModuleSw_LST1XP16LEY1,
       "hh3cevtModuleSw-SR0M2SRP2G3": hh3cevtModuleSw_SR0M2SRP2G3,
       "hh3cevtModuleSw-SR0M2SRP1G3": hh3cevtModuleSw_SR0M2SRP1G3,
       "hh3cevtModuleSw-SPC-GP48LA": hh3cevtModuleSw_SPC_GP48LA,
       "hh3cevtModuleSw-SPC-GT48LA": hh3cevtModuleSw_SPC_GT48LA,
       "hh3cevtModuleSw-SPC-XP4LA": hh3cevtModuleSw_SPC_XP4LA,
       "hh3cevtModuleSw-SPC-XP2LA": hh3cevtModuleSw_SPC_XP2LA,
       "hh3cevtModuleSw-SPC-GP24LA": hh3cevtModuleSw_SPC_GP24LA,
       "hh3cevtModuleSw-SPC-XP16RA": hh3cevtModuleSw_SPC_XP16RA,
       "hh3cevtModuleSw-CR-IM-FW1A": hh3cevtModuleSw_CR_IM_FW1A,
       "hh3cevtModuleSw-SPC-XP16R": hh3cevtModuleSw_SPC_XP16R,
       "hh3cevtModuleSw-CR-IM-LB1A": hh3cevtModuleSw_CR_IM_LB1A,
       "hh3cevtModuleSw-LST1GT48LEC2": hh3cevtModuleSw_LST1GT48LEC2,
       "hh3cevtModuleSw-LST1GP48LEC2": hh3cevtModuleSw_LST1GP48LEC2,
       "hh3cevtModuleSw-LST1XP16LEC2": hh3cevtModuleSw_LST1XP16LEC2,
       "hh3cevtModuleSw-LST2XP8LEC2": hh3cevtModuleSw_LST2XP8LEC2,
       "hh3cevtModuleSw-LST2XP32REC2": hh3cevtModuleSw_LST2XP32REC2,
       "hh3cevtModuleSw-CR-IM-MAC1A": hh3cevtModuleSw_CR_IM_MAC1A,
       "hh3cevtModuleSw-LST1XP48LFD1": hh3cevtModuleSw_LST1XP48LFD1,
       "hh3cevtModuleSw-LST1XP40RFD1": hh3cevtModuleSw_LST1XP40RFD1,
       "hh3cevtModuleSw-LST1XP40RFG1": hh3cevtModuleSw_LST1XP40RFG1,
       "hh3cevtModuleSw-LST1XLP16RFD1": hh3cevtModuleSw_LST1XLP16RFD1,
       "hh3cevtModuleSw-LST1CP4RFD1": hh3cevtModuleSw_LST1CP4RFD1,
       "hh3cevtModuleSw-LST1CP4RFG1": hh3cevtModuleSw_LST1CP4RFG1,
       "hh3cevtModuleSw-LST1SF08E1": hh3cevtModuleSw_LST1SF08E1,
       "hh3cevtModuleSw-LST1SF18E1": hh3cevtModuleSw_LST1SF18E1,
       "hh3cevtModuleSw-LST1MRPNE1": hh3cevtModuleSw_LST1MRPNE1,
       "hh3cevtModuleSw-LSX1CGX8FC0": hh3cevtModuleSw_LSX1CGX8FC0,
       "hh3cevtModuleSw-LSX1CGX8FC1": hh3cevtModuleSw_LSX1CGX8FC1,
       "hh3cevtModuleSw-LSX1QGS24FC0": hh3cevtModuleSw_LSX1QGS24FC0,
       "hh3cevtModuleSw-LSX1QGS24FC1": hh3cevtModuleSw_LSX1QGS24FC1,
       "hh3cevtModuleSw-LSX1TGS24FC0": hh3cevtModuleSw_LSX1TGS24FC0,
       "hh3cevtModuleSw-LSX1TGS24FC1": hh3cevtModuleSw_LSX1TGS24FC1,
       "hh3cevtModuleSw-LSX1TGS48FC0": hh3cevtModuleSw_LSX1TGS48FC0,
       "hh3cevtModuleSw-LSX1TGS48FC1": hh3cevtModuleSw_LSX1TGS48FC1,
       "hh3cevtModuleSw-LST1XP48LFD2": hh3cevtModuleSw_LST1XP48LFD2,
       "hh3cevtModuleSw-LST1XP40RFD2": hh3cevtModuleSw_LST1XP40RFD2,
       "hh3cevtModuleSw-LST1XP40RFG2": hh3cevtModuleSw_LST1XP40RFG2,
       "hh3cevtModuleSw-LST1XLP16RFD2": hh3cevtModuleSw_LST1XLP16RFD2,
       "hh3cevtModuleSw-LST1CP4RFD2": hh3cevtModuleSw_LST1CP4RFD2,
       "hh3cevtModuleSw-LST1CP4RFG2": hh3cevtModuleSw_LST1CP4RFG2,
       "hh3cevtModuleSw-MPE-1004": hh3cevtModuleSw_MPE_1004,
       "hh3cevtModuleSw-MIC-GP4L": hh3cevtModuleSw_MIC_GP4L,
       "hh3cevtModuleSw-MIC-GP8L": hh3cevtModuleSw_MIC_GP8L,
       "hh3cevtModuleSw-MIC-SP4L": hh3cevtModuleSw_MIC_SP4L,
       "hh3cevtModuleSw-MIC-ET16L": hh3cevtModuleSw_MIC_ET16L,
       "hh3cevtModuleSw-MIC-CLP4L": hh3cevtModuleSw_MIC_CLP4L,
       "hh3cevtModuleSw-MIC-CLP2L": hh3cevtModuleSw_MIC_CLP2L,
       "hh3cevtModuleSw-LST1IPS2A1": hh3cevtModuleSw_LST1IPS2A1,
       "hh3cevtModuleSw-SFC-04B": hh3cevtModuleSw_SFC_04B,
       "hh3cevtModuleSw-SFC-04D": hh3cevtModuleSw_SFC_04D,
       "hh3cevtModuleSw-SFC-08B": hh3cevtModuleSw_SFC_08B,
       "hh3cevtModuleSw-SFC-08D": hh3cevtModuleSw_SFC_08D,
       "hh3cevtModuleSw-SFC-12B": hh3cevtModuleSw_SFC_12B,
       "hh3cevtModuleSw-SFC-12D": hh3cevtModuleSw_SFC_12D,
       "hh3cevtModuleSw-SR05SRP1H1": hh3cevtModuleSw_SR05SRP1H1,
       "hh3cevtModuleSw-SPC-GP24LA1": hh3cevtModuleSw_SPC_GP24LA1,
       "hh3cevtModuleSw-SPC-GP24XP2LA": hh3cevtModuleSw_SPC_GP24XP2LA,
       "hh3cevtModuleSw-SPC-GP48LA1": hh3cevtModuleSw_SPC_GP48LA1,
       "hh3cevtModuleSw-SPC-GP48LB": hh3cevtModuleSw_SPC_GP48LB,
       "hh3cevtModuleSw-SPC-XP2LA1": hh3cevtModuleSw_SPC_XP2LA1,
       "hh3cevtModuleSw-SPC-XP4LA1": hh3cevtModuleSw_SPC_XP4LA1,
       "hh3cevtModuleSw-SPC-XP4LB": hh3cevtModuleSw_SPC_XP4LB,
       "hh3cevtModuleSw-SPC-XP8LA": hh3cevtModuleSw_SPC_XP8LA,
       "hh3cevtModuleSw-SPC-XP8LB": hh3cevtModuleSw_SPC_XP8LB,
       "hh3cevtModuleSw-SPC-XP48LA": hh3cevtModuleSw_SPC_XP48LA,
       "hh3cevtModuleSw-SPC-XLP8LA": hh3cevtModuleSw_SPC_XLP8LA,
       "hh3cevtModuleSw-SPC-GP24XP2LB": hh3cevtModuleSw_SPC_GP24XP2LB,
       "hh3cevtModuleSw-LST1MRPNE2": hh3cevtModuleSw_LST1MRPNE2,
       "hh3cevtModuleSw-LST2FW3A1": hh3cevtModuleSw_LST2FW3A1,
       "hh3cevtModuleSw-LST1ADE1A1": hh3cevtModuleSw_LST1ADE1A1,
       "hh3cevtModuleSw-CR-MRP-II": hh3cevtModuleSw_CR_MRP_II,
       "hh3cevtModuleSw-CR-SF08E": hh3cevtModuleSw_CR_SF08E,
       "hh3cevtModuleSw-CR-SF18E": hh3cevtModuleSw_CR_SF18E,
       "hh3cevtModuleSw-CR-SPC-XP40RC": hh3cevtModuleSw_CR_SPC_XP40RC,
       "hh3cevtModuleSw-CR-SPC-XP40RB": hh3cevtModuleSw_CR_SPC_XP40RB,
       "hh3cevtModuleSw-CR-SPC-CP4RC": hh3cevtModuleSw_CR_SPC_CP4RC,
       "hh3cevtModuleSw-LST1FW3C1": hh3cevtModuleSw_LST1FW3C1,
       "hh3cevtModuleSw-LSU1FWCEA0": hh3cevtModuleSw_LSU1FWCEA0,
       "hh3cevtModuleSw-SPC-GT48LA1": hh3cevtModuleSw_SPC_GT48LA1,
       "hh3cevtModuleSw-LST1XP20RFD1": hh3cevtModuleSw_LST1XP20RFD1,
       "hh3cevtModuleSw-LST1XP20RFD2": hh3cevtModuleSw_LST1XP20RFD2,
       "hh3cevtModuleSw-MPE-1104": hh3cevtModuleSw_MPE_1104,
       "hh3cevtModuleSw-SPEX-1204": hh3cevtModuleSw_SPEX_1204,
       "hh3cevtModuleSw-SPC-GP44XP4LCX": hh3cevtModuleSw_SPC_GP44XP4LCX,
       "hh3cevtModuleSw-SPC-GP44XP4LAX": hh3cevtModuleSw_SPC_GP44XP4LAX,
       "hh3cevtModuleSw-SPC-XP24LCX": hh3cevtModuleSw_SPC_XP24LCX,
       "hh3cevtModuleSw-SPC-XP24LAX": hh3cevtModuleSw_SPC_XP24LAX,
       "hh3cevtModuleSw-SPC-XP12LCX": hh3cevtModuleSw_SPC_XP12LCX,
       "hh3cevtModuleSw-SPC-XP12LAX": hh3cevtModuleSw_SPC_XP12LAX,
       "hh3cevtModuleSw-SPC-XLP6LCX": hh3cevtModuleSw_SPC_XLP6LCX,
       "hh3cevtModuleSw-SPC-XLP6LAX": hh3cevtModuleSw_SPC_XLP6LAX,
       "hh3cevtModuleSw-SPC-CP1LCX": hh3cevtModuleSw_SPC_CP1LCX,
       "hh3cevtModuleSw-SPC-CP1LAX": hh3cevtModuleSw_SPC_CP1LAX,
       "hh3cevtModuleSw-SPC-CP2LB": hh3cevtModuleSw_SPC_CP2LB,
       "hh3cevtModuleSw-SPC-CP2LA": hh3cevtModuleSw_SPC_CP2LA,
       "hh3cevtModuleSw-SR05SRP1L1": hh3cevtModuleSw_SR05SRP1L1,
       "hh3cevtModuleSw-SR05SRP1L3": hh3cevtModuleSw_SR05SRP1L3,
       "hh3cevtModuleSw-SFC-04-4": hh3cevtModuleSw_SFC_04_4,
       "hh3cevtModuleSw-SFC-04-3": hh3cevtModuleSw_SFC_04_3,
       "hh3cevtModuleSw-SFC-04-2": hh3cevtModuleSw_SFC_04_2,
       "hh3cevtModuleSw-SFC-04-1": hh3cevtModuleSw_SFC_04_1,
       "hh3cevtModuleSw-LST1NSM2C1": hh3cevtModuleSw_LST1NSM2C1,
       "hh3cevtModuleSw-CR-SPC-XP20RB": hh3cevtModuleSw_CR_SPC_XP20RB,
       "hh3cevtModuleSw-SR07SRPUA1": hh3cevtModuleSw_SR07SRPUA1,
       "hh3cevtModuleSw-SR07SRPUB3": hh3cevtModuleSw_SR07SRPUB3,
       "hh3cevtModuleSw-SR07SRPUC3": hh3cevtModuleSw_SR07SRPUC3,
       "hh3cevtModuleSw-SR07MPUA1": hh3cevtModuleSw_SR07MPUA1,
       "hh3cevtModuleSw-SR07SRPUB1": hh3cevtModuleSw_SR07SRPUB1,
       "hh3cevtModuleSw-SR07SRPUC1": hh3cevtModuleSw_SR07SRPUC1,
       "hh3cevtModuleSw-MIC-MS4L": hh3cevtModuleSw_MIC_MS4L,
       "hh3cevtModuleSw-SPC-GP44XP4LC": hh3cevtModuleSw_SPC_GP44XP4LC,
       "hh3cevtModuleSw-SPC-GP44XP4LA": hh3cevtModuleSw_SPC_GP44XP4LA,
       "hh3cevtModuleSw-SPC-XLP2XP4LC": hh3cevtModuleSw_SPC_XLP2XP4LC,
       "hh3cevtModuleSw-SPC-XP12LC": hh3cevtModuleSw_SPC_XP12LC,
       "hh3cevtModuleSw-SPC-CP1LC": hh3cevtModuleSw_SPC_CP1LC,
       "hh3cevtModuleSw-SPC-XP24LC": hh3cevtModuleSw_SPC_XP24LC,
       "hh3cevtModuleSw-SR07SRPUD3": hh3cevtModuleSw_SR07SRPUD3,
       "hh3cevtModuleSw-SR07MPUA3": hh3cevtModuleSw_SR07MPUA3,
       "hh3cevtModuleSw-MPEX-1304": hh3cevtModuleSw_MPEX_1304,
       "hh3cevtModuleSw-MIC-GP10L1": hh3cevtModuleSw_MIC_GP10L1,
       "hh3cevtModuleSw-SR07SRPUB": hh3cevtModuleSw_SR07SRPUB,
       "hh3cevtModuleSw-CMPE-1104": hh3cevtModuleSw_CMPE_1104,
       "hh3cevtModuleSw-CSFC-04-1": hh3cevtModuleSw_CSFC_04_1,
       "hh3cevtModuleSw-CSFC-04-2": hh3cevtModuleSw_CSFC_04_2,
       "hh3cevtModuleSw-CSFC-04-3": hh3cevtModuleSw_CSFC_04_3,
       "hh3cevtModuleSw-CSFC-04-4": hh3cevtModuleSw_CSFC_04_4,
       "hh3cevtModuleSw-CSFC-04B": hh3cevtModuleSw_CSFC_04B,
       "hh3cevtModuleSw-CSFC-04D": hh3cevtModuleSw_CSFC_04D,
       "hh3cevtModuleSw-CSFC-08B": hh3cevtModuleSw_CSFC_08B,
       "hh3cevtModuleSw-CSFC-08D": hh3cevtModuleSw_CSFC_08D,
       "hh3cevtModuleSw-CSFC-12B": hh3cevtModuleSw_CSFC_12B,
       "hh3cevtModuleSw-CSFC-12D": hh3cevtModuleSw_CSFC_12D,
       "hh3cevtModuleSw-CSPC-CP1LCX": hh3cevtModuleSw_CSPC_CP1LCX,
       "hh3cevtModuleSw-CSPC-CP2LB": hh3cevtModuleSw_CSPC_CP2LB,
       "hh3cevtModuleSw-CSPC-GP24LA1": hh3cevtModuleSw_CSPC_GP24LA1,
       "hh3cevtModuleSw-CSPC-GP24XP2LB": hh3cevtModuleSw_CSPC_GP24XP2LB,
       "hh3cevtModuleSw-CSPC-GP44XP4LCX": hh3cevtModuleSw_CSPC_GP44XP4LCX,
       "hh3cevtModuleSw-CSPC-GP48LB": hh3cevtModuleSw_CSPC_GP48LB,
       "hh3cevtModuleSw-CSPC-GT48LA1": hh3cevtModuleSw_CSPC_GT48LA1,
       "hh3cevtModuleSw-CSPC-XLP6LCX": hh3cevtModuleSw_CSPC_XLP6LCX,
       "hh3cevtModuleSw-CSPC-XP2LA1": hh3cevtModuleSw_CSPC_XP2LA1,
       "hh3cevtModuleSw-CSPC-XP4LB": hh3cevtModuleSw_CSPC_XP4LB,
       "hh3cevtModuleSw-CSPC-XP8LB": hh3cevtModuleSw_CSPC_XP8LB,
       "hh3cevtModuleSw-CSPC-XP12LAX": hh3cevtModuleSw_CSPC_XP12LAX,
       "hh3cevtModuleSw-CSPC-XP12LCX": hh3cevtModuleSw_CSPC_XP12LCX,
       "hh3cevtModuleSw-CSPC-XP24LAX": hh3cevtModuleSw_CSPC_XP24LAX,
       "hh3cevtModuleSw-CSPC-XP24LCX": hh3cevtModuleSw_CSPC_XP24LCX,
       "hh3cevtModuleSw-CSPC-CSPEX-1204": hh3cevtModuleSw_CSPC_CSPEX_1204,
       "hh3cevtModuleSw-CSR05SRP1L1": hh3cevtModuleSw_CSR05SRP1L1,
       "hh3cevtModuleSw-CSR05SRP1L3": hh3cevtModuleSw_CSR05SRP1L3,
       "hh3cevtModuleSw-CSR07MPUA1": hh3cevtModuleSw_CSR07MPUA1,
       "hh3cevtModuleSw-CSR07SRPUA1": hh3cevtModuleSw_CSR07SRPUA1,
       "hh3cevtModuleSw-CSR07SRPUB1": hh3cevtModuleSw_CSR07SRPUB1,
       "hh3cevtModuleSw-CSR07SRPUC1": hh3cevtModuleSw_CSR07SRPUC1,
       "hh3cevtModuleSw-LSXM1CGX8FX1": hh3cevtModuleSw_LSXM1CGX8FX1,
       "hh3cevtModuleSw-LSXM1QGS24FX1": hh3cevtModuleSw_LSXM1QGS24FX1,
       "hh3cevtModuleSw-LSXM1TGS48FX1": hh3cevtModuleSw_LSXM1TGS48FX1,
       "hh3cevtModuleSw-LSXM1QGS12FX1": hh3cevtModuleSw_LSXM1QGS12FX1,
       "hh3cevtModuleSw-LSXM1TGT48FX1": hh3cevtModuleSw_LSXM1TGT48FX1,
       "hh3cevtModuleSw-LSU1IPSBEA0": hh3cevtModuleSw_LSU1IPSBEA0,
       "hh3cevtModuleSw-PIC-GP10L": hh3cevtModuleSw_PIC_GP10L,
       "hh3cevtModuleSw-PIC-XP1L": hh3cevtModuleSw_PIC_XP1L,
       "hh3cevtModuleSw-PIC-PUP1L": hh3cevtModuleSw_PIC_PUP1L,
       "hh3cevtModuleSw-PIC-PSP4L": hh3cevtModuleSw_PIC_PSP4L,
       "hh3cevtModuleSw-PIC-PS2G4L": hh3cevtModuleSw_PIC_PS2G4L,
       "hh3cevtModuleSw-PIC-PL2G6L": hh3cevtModuleSw_PIC_PL2G6L,
       "hh3cevtModuleSw-PIC-TCP8L": hh3cevtModuleSw_PIC_TCP8L,
       "hh3cevtModuleSw-PIC-CSP1L": hh3cevtModuleSw_PIC_CSP1L,
       "hh3cevtModuleSw-PIC-PH2G6L": hh3cevtModuleSw_PIC_PH2G6L,
       "hh3cevtModuleSw-LSXM1CGP12FX1": hh3cevtModuleSw_LSXM1CGP12FX1,
       "hh3cevtModuleSw-LSXM1CGP8FX1": hh3cevtModuleSw_LSXM1CGP8FX1,
       "hh3cevtModuleSw-LSXM1GT48FX1": hh3cevtModuleSw_LSXM1GT48FX1,
       "hh3cevtModuleSw-LSXM1GT48FX0": hh3cevtModuleSw_LSXM1GT48FX0,
       "hh3cevtModuleSw-LSXM1GP48FX1": hh3cevtModuleSw_LSXM1GP48FX1,
       "hh3cevtModuleSw-LSXM1GP48FX0": hh3cevtModuleSw_LSXM1GP48FX0,
       "hh3cevtModuleSw-LSXM1TGS24FX0": hh3cevtModuleSw_LSXM1TGS24FX0,
       "hh3cevtModuleSw-LSXM1TGS24FX1": hh3cevtModuleSw_LSXM1TGS24FX1,
       "hh3cevtModuleSw-MIC-SP8L": hh3cevtModuleSw_MIC_SP8L,
       "hh3cevtModuleSw-LSXM1TGS48FE1": hh3cevtModuleSw_LSXM1TGS48FE1,
       "hh3cevtModuleSw-LSXM1QGS24FE1": hh3cevtModuleSw_LSXM1QGS24FE1,
       "hh3cevtModuleSw-CSPEX-1504S": hh3cevtModuleSw_CSPEX_1504S,
       "hh3cevtModuleSw-CSPEX-1504X": hh3cevtModuleSw_CSPEX_1504X,
       "hh3cevtModuleSw-CSPEX-1404S": hh3cevtModuleSw_CSPEX_1404S,
       "hh3cevtModuleSw-CSPEX-1304S": hh3cevtModuleSw_CSPEX_1304S,
       "hh3cevtModuleSw-CSPEX-1404X": hh3cevtModuleSw_CSPEX_1404X,
       "hh3cevtModuleSw-CSPEX-1304X": hh3cevtModuleSw_CSPEX_1304X,
       "hh3cevtModuleSw-MIC-XP5L": hh3cevtModuleSw_MIC_XP5L,
       "hh3cevtModuleSw-MIC-XP2L": hh3cevtModuleSw_MIC_XP2L,
       "hh3cevtModuleSw-MIC-CP1L": hh3cevtModuleSw_MIC_CP1L,
       "hh3cevtModuleSw-MIC-GP20L": hh3cevtModuleSw_MIC_GP20L,
       "hh3cevtModuleSw-MIC-GT20L": hh3cevtModuleSw_MIC_GT20L,
       "hh3cevtModuleSw-CEPC-XP48RX": hh3cevtModuleSw_CEPC_XP48RX,
       "hh3cevtModuleSw-CEPC-CP4RX": hh3cevtModuleSw_CEPC_CP4RX,
       "hh3cevtModuleSw-MIC-GP10L-V2": hh3cevtModuleSw_MIC_GP10L_V2,
       "hh3cevtModuleSw-CSR07SRPUD3": hh3cevtModuleSw_CSR07SRPUD3,
       "hh3cevtModuleSw-MIC-XP1L": hh3cevtModuleSw_MIC_XP1L,
       "hh3cevtModuleSw-CSFC-12E": hh3cevtModuleSw_CSFC_12E,
       "hh3cevtModuleSw-CEPC-XP24LX": hh3cevtModuleSw_CEPC_XP24LX,
       "hh3cevtModuleSw-IM-MSUX": hh3cevtModuleSw_IM_MSUX,
       "hh3cevtModuleSw-CSFC-12F": hh3cevtModuleSw_CSFC_12F,
       "hh3cevtModuleSw-CSR05SRP1N3": hh3cevtModuleSw_CSR05SRP1N3,
       "hh3cevtModuleSw-CSPEX-1602X": hh3cevtModuleSw_CSPEX_1602X,
       "hh3cevtModuleSw-MIC-XP20L": hh3cevtModuleSw_MIC_XP20L,
       "hh3cevtModuleSw-MIC-CP2L": hh3cevtModuleSw_MIC_CP2L,
       "hh3cevtModuleSw-IM-NGFWX-IV": hh3cevtModuleSw_IM_NGFWX_IV,
       "hh3cevtModuleSw-SFC-12E": hh3cevtModuleSw_SFC_12E,
       "hh3cevtModuleSw-SPEX-1602X-E": hh3cevtModuleSw_SPEX_1602X_E,
       "hh3cevtModuleSw-SPEX-1602X-L": hh3cevtModuleSw_SPEX_1602X_L,
       "hh3cevtModuleSw-EPC-XP24LX-E": hh3cevtModuleSw_EPC_XP24LX_E,
       "hh3cevtModuleSw-EPC-XP24LX-L": hh3cevtModuleSw_EPC_XP24LX_L,
       "hh3cevtModuleSw-EPC-CP4RX-L": hh3cevtModuleSw_EPC_CP4RX_L,
       "hh3cevtModuleSw-SPEX-1504X-E": hh3cevtModuleSw_SPEX_1504X_E,
       "hh3cevtModuleSw-SPEX-1504X-L": hh3cevtModuleSw_SPEX_1504X_L,
       "hh3cevtModuleSw-CSPEX-1602X-L": hh3cevtModuleSw_CSPEX_1602X_L,
       "hh3cevtModuleSw-CEPC-XP24LX-L": hh3cevtModuleSw_CEPC_XP24LX_L,
       "hh3cevtModuleSw-CEPC-CP4RX-L": hh3cevtModuleSw_CEPC_CP4RX_L,
       "hh3cevtModuleSw-MIC-CP1L-E": hh3cevtModuleSw_MIC_CP1L_E,
       "hh3cevtModuleSw-MIC-XP4L-E": hh3cevtModuleSw_MIC_XP4L_E,
       "hh3cevtModuleSw-MIC-XP16L-E": hh3cevtModuleSw_MIC_XP16L_E,
       "hh3cevtModuleSw-MIC-GP20L-E": hh3cevtModuleSw_MIC_GP20L_E,
       "hh3cevtModuleSw-MIC-GP10L-V2-E": hh3cevtModuleSw_MIC_GP10L_V2_E,
       "hh3cevtModuleSw-MIC-GT20L-E": hh3cevtModuleSw_MIC_GT20L_E,
       "hh3cevtModuleSw-CSR05SRP1P3": hh3cevtModuleSw_CSR05SRP1P3,
       "hh3cevtModuleSw-SR05SRP1P3": hh3cevtModuleSw_SR05SRP1P3,
       "hh3cevtModuleSw-CSFC-16E": hh3cevtModuleSw_CSFC_16E,
       "hh3cevtModuleSw-SFC-16E": hh3cevtModuleSw_SFC_16E,
       "hh3cevtModuleSw-CSFC-08E": hh3cevtModuleSw_CSFC_08E,
       "hh3cevtModuleSw-SFC-08E": hh3cevtModuleSw_SFC_08E,
       "hh3cevtModuleSw-IM-SMUX": hh3cevtModuleSw_IM_SMUX,
       "hh3cevtModuleSw-IM-IPSX-IV": hh3cevtModuleSw_IM_IPSX_IV,
       "hh3cevtModuleSw-IM-ACGX-IV": hh3cevtModuleSw_IM_ACGX_IV,
       "hh3cevtModuleSw-SFC-08E1": hh3cevtModuleSw_SFC_08E1,
       "hh3cevtModuleSw-CSFC-08E1": hh3cevtModuleSw_CSFC_08E1,
       "hh3cevtModuleSw-IM-ACG1000X-IV": hh3cevtModuleSw_IM_ACG1000X_IV,
       "hh3cevtModuleSw-MIC-QP1L": hh3cevtModuleSw_MIC_QP1L,
       "hh3cevtModuleSw-CSPEX-1804X": hh3cevtModuleSw_CSPEX_1804X,
       "hh3cevtModuleSw-MIC-CP2L-V2": hh3cevtModuleSw_MIC_CP2L_V2,
       "hh3cevtModuleSw-MIC-XP4L1": hh3cevtModuleSw_MIC_XP4L1,
       "hh3cevtModuleSw-SFC-16T": hh3cevtModuleSw_SFC_16T,
       "hh3cevtModuleSw-CSFC-16T": hh3cevtModuleSw_CSFC_16T,
       "hh3cevtModuleSw-SFC-08T": hh3cevtModuleSw_SFC_08T,
       "hh3cevtModuleSw-CSFC-08T": hh3cevtModuleSw_CSFC_08T,
       "hh3cevtModuleSw-MIC-XP2L-LAN": hh3cevtModuleSw_MIC_XP2L_LAN,
       "hh3cevtModuleSw-MIC-XP5L1": hh3cevtModuleSw_MIC_XP5L1,
       "hh3cevtModuleSw-MIC-CP1L-V2": hh3cevtModuleSw_MIC_CP1L_V2,
       "hh3cevtModuleSw-CEPC-XP40LX": hh3cevtModuleSw_CEPC_XP40LX,
       "hh3cevtModuleSw-CEPC-CQ4LX": hh3cevtModuleSw_CEPC_CQ4LX,
       "hh3cevtModuleSw-LSU1QGC4SF0": hh3cevtModuleSw_LSU1QGC4SF0,
       "hh3cevtModuleSw-LSU1QGS8SF0": hh3cevtModuleSw_LSU1QGS8SF0,
       "hh3cevtModuleSw-LSU1TGS48SF0": hh3cevtModuleSw_LSU1TGS48SF0,
       "hh3cevtModuleSw-LSU1QGS4SF0": hh3cevtModuleSw_LSU1QGS4SF0,
       "hh3cevtModuleSw-LSU1TGS32SF0": hh3cevtModuleSw_LSU1TGS32SF0,
       "hh3cevtModuleSw-LSU1FAB08D0": hh3cevtModuleSw_LSU1FAB08D0,
       "hh3cevtModuleSw-LSU1FAB04B0": hh3cevtModuleSw_LSU1FAB04B0,
       "hh3cevtModuleSw-LSU1FAB08B0": hh3cevtModuleSw_LSU1FAB08B0,
       "hh3cevtModuleSw-LSU1FAB12D0": hh3cevtModuleSw_LSU1FAB12D0,
       "hh3cevtModuleSw-LSU1FAB12B0": hh3cevtModuleSw_LSU1FAB12B0,
       "hh3cevtModuleSw-LSU1FAB04D0": hh3cevtModuleSw_LSU1FAB04D0,
       "hh3cevtModuleSw-LSQ1CTGS16SC0": hh3cevtModuleSw_LSQ1CTGS16SC0,
       "hh3cevtModuleSw-EWPX2CTGS16SC0": hh3cevtModuleSw_EWPX2CTGS16SC0,
       "hh3cevtModuleSw-LSU3WCMD0": hh3cevtModuleSw_LSU3WCMD0,
       "hh3cevtModuleSw-EWPX3WCMD0": hh3cevtModuleSw_EWPX3WCMD0,
       "hh3cevtModuleSw-LSQ1QGS4SC0": hh3cevtModuleSw_LSQ1QGS4SC0,
       "hh3cevtModuleSw-LSQ1QGC4SC0": hh3cevtModuleSw_LSQ1QGC4SC0,
       "hh3cevtModuleSw-LSU1TGT24SF0": hh3cevtModuleSw_LSU1TGT24SF0,
       "hh3cevtModuleSw-LSQ1QGS8SC3": hh3cevtModuleSw_LSQ1QGS8SC3,
       "hh3cevtModuleSw-LSQ1TGS32SC3": hh3cevtModuleSw_LSQ1TGS32SC3,
       "hh3cevtModuleSw-LSQ1QGS4SC3": hh3cevtModuleSw_LSQ1QGS4SC3,
       "hh3cevtModuleSw-LSQ1TGS48SC3": hh3cevtModuleSw_LSQ1TGS48SC3,
       "hh3cevtModuleSw-LSQ1QGC4SC3": hh3cevtModuleSw_LSQ1QGC4SC3,
       "hh3cevtModuleSw-LSQ1FAB12D3": hh3cevtModuleSw_LSQ1FAB12D3,
       "hh3cevtModuleSw-LSQ1FAB08D3": hh3cevtModuleSw_LSQ1FAB08D3,
       "hh3cevtModuleSw-LSQ1FAB04D3": hh3cevtModuleSw_LSQ1FAB04D3,
       "hh3cevtModuleSw-LSQ1TGS8EB3": hh3cevtModuleSw_LSQ1TGS8EB3,
       "hh3cevtModuleSw-LSQ1TGT24SC3": hh3cevtModuleSw_LSQ1TGT24SC3,
       "hh3cevtModuleSw-LSQ1FAB08B0": hh3cevtModuleSw_LSQ1FAB08B0,
       "hh3cevtModuleSw-EWPX2CTGS16SC": hh3cevtModuleSw_EWPX2CTGS16SC,
       "hh3cevtModuleSw-LSU1SUPB0": hh3cevtModuleSw_LSU1SUPB0,
       "hh3cevtModuleSw-LSQ1GP48SA0": hh3cevtModuleSw_LSQ1GP48SA0,
       "hh3cevtModuleSw-LSQ1TGX2SA0": hh3cevtModuleSw_LSQ1TGX2SA0,
       "hh3cevtModuleSw-LSV1SRPUA1": hh3cevtModuleSw_LSV1SRPUA1,
       "hh3cevtModuleSw-LSV1QGS12SA1": hh3cevtModuleSw_LSV1QGS12SA1,
       "hh3cevtModuleSw-LSV1MPUA1": hh3cevtModuleSw_LSV1MPUA1,
       "hh3cevtModuleSw-LSX1SUP10A0": hh3cevtModuleSw_LSX1SUP10A0,
       "hh3cevtModuleSw-LSX1SUP16A0": hh3cevtModuleSw_LSX1SUP16A0,
       "hh3cevtModuleSw-LSX1SUP10A1": hh3cevtModuleSw_LSX1SUP10A1,
       "hh3cevtModuleSw-LSX1SUP16A1": hh3cevtModuleSw_LSX1SUP16A1,
       "hh3cevtModuleSw-LSX1FAB10B0": hh3cevtModuleSw_LSX1FAB10B0,
       "hh3cevtModuleSw-LSX1FAB16B0": hh3cevtModuleSw_LSX1FAB16B0,
       "hh3cevtModuleSw-LSX1FAB10B1": hh3cevtModuleSw_LSX1FAB10B1,
       "hh3cevtModuleSw-LSX1FAB16B1": hh3cevtModuleSw_LSX1FAB16B1,
       "hh3cevtModuleSw-LSX1QGS16EA0": hh3cevtModuleSw_LSX1QGS16EA0,
       "hh3cevtModuleSw-LSX1TGS48EA0": hh3cevtModuleSw_LSX1TGS48EA0,
       "hh3cevtModuleSw-LSX1QGS16EA1": hh3cevtModuleSw_LSX1QGS16EA1,
       "hh3cevtModuleSw-LSX1TGS48EA1": hh3cevtModuleSw_LSX1TGS48EA1,
       "hh3cevtModuleSw-LSU1TGT24SF9": hh3cevtModuleSw_LSU1TGT24SF9,
       "hh3cevtModuleSw-LSU1QGS8SF9": hh3cevtModuleSw_LSU1QGS8SF9,
       "hh3cevtModuleSw-LSU1QGS4SF9": hh3cevtModuleSw_LSU1QGS4SF9,
       "hh3cevtModuleSw-LSU1TGS48SF9": hh3cevtModuleSw_LSU1TGS48SF9,
       "hh3cevtModuleSw-LSU1TGS32SF9": hh3cevtModuleSw_LSU1TGS32SF9,
       "hh3cevtModuleSw-LSU1FAB08D9": hh3cevtModuleSw_LSU1FAB08D9,
       "hh3cevtModuleSw-LSU1SUPB9": hh3cevtModuleSw_LSU1SUPB9,
       "hh3cevtModuleSw-LSQ3GV48SC0": hh3cevtModuleSw_LSQ3GV48SC0,
       "hh3cevtModuleSw-LSX1QGS12EC1": hh3cevtModuleSw_LSX1QGS12EC1,
       "hh3cevtModuleSw-LSX1QGS12EC0": hh3cevtModuleSw_LSX1QGS12EC0,
       "hh3cevtModuleSw-LSX1TGS48EC0": hh3cevtModuleSw_LSX1TGS48EC0,
       "hh3cevtModuleSw-LSX1TGS48EC1": hh3cevtModuleSw_LSX1TGS48EC1,
       "hh3cevtModuleSw-LSX1TGS24EC0": hh3cevtModuleSw_LSX1TGS24EC0,
       "hh3cevtModuleSw-LSX1TGS24EC1": hh3cevtModuleSw_LSX1TGS24EC1,
       "hh3cevtModuleSw-LSX1FAB10A0": hh3cevtModuleSw_LSX1FAB10A0,
       "hh3cevtModuleSw-LSX1FAB16A1": hh3cevtModuleSw_LSX1FAB16A1,
       "hh3cevtModuleSw-LSX1QGS12FB0": hh3cevtModuleSw_LSX1QGS12FB0,
       "hh3cevtModuleSw-LSX1TGS24FB0": hh3cevtModuleSw_LSX1TGS24FB0,
       "hh3cevtModuleSw-LSX1TGS48FB0": hh3cevtModuleSw_LSX1TGS48FB0,
       "hh3cevtModuleSw-LSX1QGS12EB1": hh3cevtModuleSw_LSX1QGS12EB1,
       "hh3cevtModuleSw-LSX1TGS24EB1": hh3cevtModuleSw_LSX1TGS24EB1,
       "hh3cevtModuleSw-LSX1FAB10A1": hh3cevtModuleSw_LSX1FAB10A1,
       "hh3cevtModuleSw-LSX1TGS48EB1": hh3cevtModuleSw_LSX1TGS48EB1,
       "hh3cevtModuleSw-LSX1GP48EB1": hh3cevtModuleSw_LSX1GP48EB1,
       "hh3cevtModuleSw-LSX1GP48FB0": hh3cevtModuleSw_LSX1GP48FB0,
       "hh3cevtModuleSw-LSX1GT48FC0": hh3cevtModuleSw_LSX1GT48FC0,
       "hh3cevtModuleSw-LSX1GT48FC1": hh3cevtModuleSw_LSX1GT48FC1,
       "hh3cevtModuleSw-LSX1GP48FC0": hh3cevtModuleSw_LSX1GP48FC0,
       "hh3cevtModuleSw-LSX1GP48FC1": hh3cevtModuleSw_LSX1GP48FC1,
       "hh3cevtModuleSw-LSX1QGS12FC0": hh3cevtModuleSw_LSX1QGS12FC0,
       "hh3cevtModuleSw-LSX1QGS12FC1": hh3cevtModuleSw_LSX1QGS12FC1,
       "hh3cevtModuleSw-LSX2TGS48EA1": hh3cevtModuleSw_LSX2TGS48EA1,
       "hh3cevtModuleSw-LSX1CGC4EB1": hh3cevtModuleSw_LSX1CGC4EB1,
       "hh3cevtModuleSw-LSX1CGC4EC0": hh3cevtModuleSw_LSX1CGC4EC0,
       "hh3cevtModuleSw-LSX1GT48EB1": hh3cevtModuleSw_LSX1GT48EB1,
       "hh3cevtModuleSw-LSX1GT48FB0": hh3cevtModuleSw_LSX1GT48FB0,
       "hh3cevtModuleSw-LSX1FAB16S1": hh3cevtModuleSw_LSX1FAB16S1,
       "hh3cevtModuleSw-LSQ1SUPB3": hh3cevtModuleSw_LSQ1SUPB3,
       "hh3cevtModuleSw-LSU1CGC2SE0": hh3cevtModuleSw_LSU1CGC2SE0,
       "hh3cevtModuleSw-LSU1TGS16SF0": hh3cevtModuleSw_LSU1TGS16SF0,
       "hh3cevtModuleSw-LSU1TGS8SF0": hh3cevtModuleSw_LSU1TGS8SF0,
       "hh3cevtModuleSw-LSQ1TGS4SC0": hh3cevtModuleSw_LSQ1TGS4SC0,
       "hh3cevtModuleSw-LSU1GT48SE3": hh3cevtModuleSw_LSU1GT48SE3,
       "hh3cevtModuleSw-LSU1GP48SE3": hh3cevtModuleSw_LSU1GP48SE3,
       "hh3cevtModuleSw-LSX1SUP10B0": hh3cevtModuleSw_LSX1SUP10B0,
       "hh3cevtModuleSw-LSX1SUP16B0": hh3cevtModuleSw_LSX1SUP16B0,
       "hh3cevtModuleSw-LSX1SUP10B1": hh3cevtModuleSw_LSX1SUP10B1,
       "hh3cevtModuleSw-LSX1SUP16B1": hh3cevtModuleSw_LSX1SUP16B1,
       "hh3cevtModuleSw-LSQ1CGV24PSC3": hh3cevtModuleSw_LSQ1CGV24PSC3,
       "hh3cevtModuleSw-LSQ1SRPA8": hh3cevtModuleSw_LSQ1SRPA8,
       "hh3cevtModuleSw-LSQ1CGP24TSC8": hh3cevtModuleSw_LSQ1CGP24TSC8,
       "hh3cevtModuleSw-LSQ1CGT24PSC8": hh3cevtModuleSw_LSQ1CGT24PSC8,
       "hh3cevtModuleSw-LSQ1GT24PSA8": hh3cevtModuleSw_LSQ1GT24PSA8,
       "hh3cevtModuleSw-LSQ1GP24TSA8": hh3cevtModuleSw_LSQ1GP24TSA8,
       "hh3cevtModuleSw-LSQ1GT48SA8": hh3cevtModuleSw_LSQ1GT48SA8,
       "hh3cevtModuleSw-LSQ1GP48SA8": hh3cevtModuleSw_LSQ1GP48SA8,
       "hh3cevtModuleSw-LSQ1TGS4SC8": hh3cevtModuleSw_LSQ1TGS4SC8,
       "hh3cevtModuleSw-LSQ1TGS8SC8": hh3cevtModuleSw_LSQ1TGS8SC8,
       "hh3cevtModuleSw-LSU1GT24SE3": hh3cevtModuleSw_LSU1GT24SE3,
       "hh3cevtModuleSw-LSU1GP12SE3": hh3cevtModuleSw_LSU1GP12SE3,
       "hh3cevtModuleSw-LSU1GP24SE3": hh3cevtModuleSw_LSU1GP24SE3,
       "hh3cevtModuleSw-LSU1T24XGSE3": hh3cevtModuleSw_LSU1T24XGSE3,
       "hh3cevtModuleSw-LSU1P24XGSE3": hh3cevtModuleSw_LSU1P24XGSE3,
       "hh3cevtModuleSw-LSU1GP24TSE3": hh3cevtModuleSw_LSU1GP24TSE3,
       "hh3cevtModuleSw-LSU1GT40PSE3": hh3cevtModuleSw_LSU1GT40PSE3,
       "hh3cevtModuleSw-LSV1TGS24SA1": hh3cevtModuleSw_LSV1TGS24SA1,
       "hh3cevtModuleSw-LSVM1SRPA1": hh3cevtModuleSw_LSVM1SRPA1,
       "hh3cevtModuleSw-LSVM1SRPC1": hh3cevtModuleSw_LSVM1SRPC1,
       "hh3cevtModuleSw-LSX1FAB16S0": hh3cevtModuleSw_LSX1FAB16S0,
       "hh3cevtModuleSw-LSU1WCME0": hh3cevtModuleSw_LSU1WCME0,
       "hh3cevtModuleSw-EWPX1WCME0": hh3cevtModuleSw_EWPX1WCME0,
       "hh3cevtModuleSw-LSUM1TGS48SG0": hh3cevtModuleSw_LSUM1TGS48SG0,
       "hh3cevtModuleSw-LSUM1QGS12SG0": hh3cevtModuleSw_LSUM1QGS12SG0,
       "hh3cevtModuleSw-LSUM1GP44TSEC0": hh3cevtModuleSw_LSUM1GP44TSEC0,
       "hh3cevtModuleSw-LSUM1TGS24EC0": hh3cevtModuleSw_LSUM1TGS24EC0,
       "hh3cevtModuleSw-LSUM1QGS6EC0": hh3cevtModuleSw_LSUM1QGS6EC0,
       "hh3cevtModuleSw-LSUM1CGC2EC0": hh3cevtModuleSw_LSUM1CGC2EC0,
       "hh3cevtModuleSw-LSU1CGC2SE9": hh3cevtModuleSw_LSU1CGC2SE9,
       "hh3cevtModuleSw-LSXM1QGS24EX1": hh3cevtModuleSw_LSXM1QGS24EX1,
       "hh3cevtModuleSw-LSXM1QGS24FB0": hh3cevtModuleSw_LSXM1QGS24FB0,
       "hh3cevtModuleSw-LSVM1QGS12FX1": hh3cevtModuleSw_LSVM1QGS12FX1,
       "hh3cevtModuleSw-LSVM1TGS24FX1": hh3cevtModuleSw_LSVM1TGS24FX1,
       "hh3cevtModuleSw-LSVM1QGS6C2FX1": hh3cevtModuleSw_LSVM1QGS6C2FX1,
       "hh3cevtModuleSw-LSQM2GP44TSSC0": hh3cevtModuleSw_LSQM2GP44TSSC0,
       "hh3cevtModuleSw-LSQM2GP44TSSC3": hh3cevtModuleSw_LSQM2GP44TSSC3,
       "hh3cevtModuleSw-LSQM2GP24TSSC0": hh3cevtModuleSw_LSQM2GP24TSSC0,
       "hh3cevtModuleSw-LSQM2GP24TSSC3": hh3cevtModuleSw_LSQM2GP24TSSC3,
       "hh3cevtModuleSw-LSQM2GT24PTSSC0": hh3cevtModuleSw_LSQM2GT24PTSSC0,
       "hh3cevtModuleSw-LSQM2GT24PTSSC3": hh3cevtModuleSw_LSQM2GT24PTSSC3,
       "hh3cevtModuleSw-LSQM2GT24TSSC0": hh3cevtModuleSw_LSQM2GT24TSSC0,
       "hh3cevtModuleSw-LSQM2GT24TSSC3": hh3cevtModuleSw_LSQM2GT24TSSC3,
       "hh3cevtModuleSw-LSQM2GT48SC0": hh3cevtModuleSw_LSQM2GT48SC0,
       "hh3cevtModuleSw-LSQM2GT48SC3": hh3cevtModuleSw_LSQM2GT48SC3,
       "hh3cevtModuleSw-LSQM4GV48SC0": hh3cevtModuleSw_LSQM4GV48SC0,
       "hh3cevtModuleSw-LSQM4GV48SC3": hh3cevtModuleSw_LSQM4GV48SC3,
       "hh3cevtModuleSw-LSQM2TGS16SF0": hh3cevtModuleSw_LSQM2TGS16SF0,
       "hh3cevtModuleSw-LSQM2TGS16SF3": hh3cevtModuleSw_LSQM2TGS16SF3,
       "hh3cevtModuleSw-LSQM2MPUD0": hh3cevtModuleSw_LSQM2MPUD0,
       "hh3cevtModuleSw-LSQM2MPUD3": hh3cevtModuleSw_LSQM2MPUD3,
       "hh3cevtModuleSw-LSQM3MPUA0": hh3cevtModuleSw_LSQM3MPUA0,
       "hh3cevtModuleSw-LSQM3MPUA3": hh3cevtModuleSw_LSQM3MPUA3,
       "hh3cevtModuleSw-LSUM2GP44TSSE0": hh3cevtModuleSw_LSUM2GP44TSSE0,
       "hh3cevtModuleSw-LSUM2GP44TSSC3": hh3cevtModuleSw_LSUM2GP44TSSC3,
       "hh3cevtModuleSw-LSUM2GP24TSSE0": hh3cevtModuleSw_LSUM2GP24TSSE0,
       "hh3cevtModuleSw-LSUM2GP24TSSC3": hh3cevtModuleSw_LSUM2GP24TSSC3,
       "hh3cevtModuleSw-LSUM2GT24PTSSE0": hh3cevtModuleSw_LSUM2GT24PTSSE0,
       "hh3cevtModuleSw-LSUM2GT24PTSSC3": hh3cevtModuleSw_LSUM2GT24PTSSC3,
       "hh3cevtModuleSw-LSUM2GT24TSSE0": hh3cevtModuleSw_LSUM2GT24TSSE0,
       "hh3cevtModuleSw-LSUM2GT24TSSC3": hh3cevtModuleSw_LSUM2GT24TSSC3,
       "hh3cevtModuleSw-LSUM2GT48SE0": hh3cevtModuleSw_LSUM2GT48SE0,
       "hh3cevtModuleSw-LSUM2GT48SC3": hh3cevtModuleSw_LSUM2GT48SC3,
       "hh3cevtModuleSw-LSUM2GV48SE0": hh3cevtModuleSw_LSUM2GV48SE0,
       "hh3cevtModuleSw-LSUM2GV48SC3": hh3cevtModuleSw_LSUM2GV48SC3,
       "hh3cevtModuleSw-LSUM2TGS16SF0": hh3cevtModuleSw_LSUM2TGS16SF0,
       "hh3cevtModuleSw-LSUM2TGS16SF3": hh3cevtModuleSw_LSUM2TGS16SF3,
       "hh3cevtModuleSw-LSUM1MPU06B0": hh3cevtModuleSw_LSUM1MPU06B0,
       "hh3cevtModuleSw-LSUM1MPU06B3": hh3cevtModuleSw_LSUM1MPU06B3,
       "hh3cevtModuleSw-LSUM1MPU10C0": hh3cevtModuleSw_LSUM1MPU10C0,
       "hh3cevtModuleSw-LSUM1MPU10C3": hh3cevtModuleSw_LSUM1MPU10C3,
       "hh3cevtModuleSw-LSUM1FAB06C0": hh3cevtModuleSw_LSUM1FAB06C0,
       "hh3cevtModuleSw-LSUM1FAB06C3": hh3cevtModuleSw_LSUM1FAB06C3,
       "hh3cevtModuleSw-LSUM1FAB10C0": hh3cevtModuleSw_LSUM1FAB10C0,
       "hh3cevtModuleSw-LSUM1FAB10C3": hh3cevtModuleSw_LSUM1FAB10C3,
       "hh3cevtModuleSw-LSXM1SUPA1": hh3cevtModuleSw_LSXM1SUPA1,
       "hh3cevtModuleSw-LSXM1SFF16B1": hh3cevtModuleSw_LSXM1SFF16B1,
       "hh3cevtModuleSw-LSUM1SPMAEC0": hh3cevtModuleSw_LSUM1SPMAEC0,
       "hh3cevtModuleSw-LSXM1SUPB1": hh3cevtModuleSw_LSXM1SUPB1,
       "hh3cevtModuleSw-LSXM1SFF08B1": hh3cevtModuleSw_LSXM1SFF08B1,
       "hh3cevtModuleSw-LSXM1TGS4GPEB1": hh3cevtModuleSw_LSXM1TGS4GPEB1,
       "hh3cevtModuleSw-LSXM1TGS16EA1": hh3cevtModuleSw_LSXM1TGS16EA1,
       "hh3cevtModuleSw-LSXM1TGS8EA1": hh3cevtModuleSw_LSXM1TGS8EA1,
       "hh3cevtModuleSw-LSXM1QGS36FX1": hh3cevtModuleSw_LSXM1QGS36FX1,
       "hh3cevtModuleSw-LSXM1SFF16C1": hh3cevtModuleSw_LSXM1SFF16C1,
       "hh3cevtModuleSw-LSQM3MPUB0": hh3cevtModuleSw_LSQM3MPUB0,
       "hh3cevtModuleSw-LSQM3MPUB3": hh3cevtModuleSw_LSQM3MPUB3,
       "hh3cevtModuleSw-LSQM2MPUC0": hh3cevtModuleSw_LSQM2MPUC0,
       "hh3cevtModuleSw-LSQM2MPUC3": hh3cevtModuleSw_LSQM2MPUC3,
       "hh3cevtModuleSw-LST1FW3B1": hh3cevtModuleSw_LST1FW3B1,
       "hh3cevtModuleSw-LSX1NSCEA1": hh3cevtModuleSw_LSX1NSCEA1,
       "hh3cevtModuleSw-LSX1FWCEA1": hh3cevtModuleSw_LSX1FWCEA1,
       "hh3cevtModuleSw-LSXM1ADECEA1": hh3cevtModuleSw_LSXM1ADECEA1,
       "hh3cevtModuleSw-LSXM1SFF16A1": hh3cevtModuleSw_LSXM1SFF16A1,
       "hh3cevtModuleSw-LSV1MPUA0": hh3cevtModuleSw_LSV1MPUA0,
       "hh3cevtModuleSw-LSVM1SRPA0": hh3cevtModuleSw_LSVM1SRPA0,
       "hh3cevtModuleSw-LSVM1SRPC0": hh3cevtModuleSw_LSVM1SRPC0,
       "hh3cevtModuleSw-LSV1QGS12SA0": hh3cevtModuleSw_LSV1QGS12SA0,
       "hh3cevtModuleSw-LSVM1QGS12FX0": hh3cevtModuleSw_LSVM1QGS12FX0,
       "hh3cevtModuleSw-LSVM1TGS24FX0": hh3cevtModuleSw_LSVM1TGS24FX0,
       "hh3cevtModuleSw-LSVM1QGS6C2FX0": hh3cevtModuleSw_LSVM1QGS6C2FX0,
       "hh3cevtModuleSw-LSQ2FWBSC0": hh3cevtModuleSw_LSQ2FWBSC0,
       "hh3cevtModuleSw-LSQM1SRP8X2QE0": hh3cevtModuleSw_LSQM1SRP8X2QE0,
       "hh3cevtModulesw-PEX-Common": hh3cevtModulesw_PEX_Common,
       "hh3cevtModuleSw-CSPEX-1812X": hh3cevtModuleSw_CSPEX_1812X,
       "hh3cevtModuleSw-CSPEX-1612X": hh3cevtModuleSw_CSPEX_1612X,
       "hh3cevtModuleSw-CSPEX-1512X": hh3cevtModuleSw_CSPEX_1512X,
       "hh3cevtModuleSw-NIC-XP20L": hh3cevtModuleSw_NIC_XP20L,
       "hh3cevtModuleSw-NIC-XP10L": hh3cevtModuleSw_NIC_XP10L,
       "hh3cevtModuleSw-NIC-CC2L": hh3cevtModuleSw_NIC_CC2L,
       "hh3cevtModuleSw-NIC-CC1L": hh3cevtModuleSw_NIC_CC1L,
       "hh3cevtModuleSw-NIC-XP5L": hh3cevtModuleSw_NIC_XP5L,
       "hh3cevtModuleSw-NIC-GP20L": hh3cevtModuleSw_NIC_GP20L,
       "hh3cevtModuleSw-NIC-GT20L": hh3cevtModuleSw_NIC_GT20L,
       "hh3cevtModuleSw-MIC-CQ1L": hh3cevtModuleSw_MIC_CQ1L,
       "hh3cevtModuleSw-MIC-XP10CQ1L": hh3cevtModuleSw_MIC_XP10CQ1L,
       "hh3cevtModuleSw-CSPEX-1502X": hh3cevtModuleSw_CSPEX_1502X,
       "hh3cevtModuleSw-EPC-CP4RX": hh3cevtModuleSw_EPC_CP4RX,
       "hh3cevtModuleSw-EPC-CQ4LX": hh3cevtModuleSw_EPC_CQ4LX,
       "hh3cevtModuleSw-MIC-XP4L1-E": hh3cevtModuleSw_MIC_XP4L1_E,
       "hh3cevtModuleSw-MIC-CQ1L-E": hh3cevtModuleSw_MIC_CQ1L_E,
       "hh3cevtModuleSw-MIC-XP8L": hh3cevtModuleSw_MIC_XP8L,
       "hh3cevtModuleSw-IM-OAPX": hh3cevtModuleSw_IM_OAPX,
       "hh3cevtModuleSw-MIC-GP20L1": hh3cevtModuleSw_MIC_GP20L1,
       "hh3cevtModuleSw-CSPEX-1802X": hh3cevtModuleSw_CSPEX_1802X,
       "hh3cevtModuleSw-MIC-CQ2L": hh3cevtModuleSw_MIC_CQ2L,
       "hh3cevtModuleSw-IMMSUX": hh3cevtModuleSw_IMMSUX,
       "hh3cevtModuleSw-CSPEX-1104-E": hh3cevtModuleSw_CSPEX_1104_E,
       "hh3cevtModuleSw-IMSMUX": hh3cevtModuleSw_IMSMUX,
       "hh3cevtModuleSw-MIC-XP10L": hh3cevtModuleSw_MIC_XP10L,
       "hh3cevtModuleSw-RX-SRP1P3": hh3cevtModuleSw_RX_SRP1P3,
       "hh3cevtModuleSw-RX-SFC-08T": hh3cevtModuleSw_RX_SFC_08T,
       "hh3cevtModuleSw-RX-SFC-16T": hh3cevtModuleSw_RX_SFC_16T,
       "hh3cevtModuleSw-RX-SPE100": hh3cevtModuleSw_RX_SPE100,
       "hh3cevtModuleSw-RX-SPE200": hh3cevtModuleSw_RX_SPE200,
       "hh3cevtModuleSw-RX-SPE400": hh3cevtModuleSw_RX_SPE400,
       "hh3cevtModuleSw-RX-NIC-GP20L": hh3cevtModuleSw_RX_NIC_GP20L,
       "hh3cevtModuleSw-RX-NIC-XP5L": hh3cevtModuleSw_RX_NIC_XP5L,
       "hh3cevtModuleSw-RX-NIC-XP10L": hh3cevtModuleSw_RX_NIC_XP10L,
       "hh3cevtModuleSw-RX-NIC-CC1L": hh3cevtModuleSw_RX_NIC_CC1L,
       "hh3cevtModuleSw-RX-NIC-CC2L": hh3cevtModuleSw_RX_NIC_CC2L,
       "hh3cevtModuleSw-RX-NIC-XP20L": hh3cevtModuleSw_RX_NIC_XP20L,
       "hh3cevtModuleSw-CSPC-GE24L-E": hh3cevtModuleSw_CSPC_GE24L_E,
       "hh3cevtModuleSw-CSPC-GP24GE8XP2L-E": hh3cevtModuleSw_CSPC_GP24GE8XP2L_E,
       "hh3cevtModuleSw-CSPC-GE16XP4L-E": hh3cevtModuleSw_CSPC_GE16XP4L_E,
       "hh3cevtModuleSw-CSFC-04E": hh3cevtModuleSw_CSFC_04E,
       "hh3cevtModuleSw-SFC-04E": hh3cevtModuleSw_SFC_04E,
       "hh3cevtModuleSw-IM-MSUX-II": hh3cevtModuleSw_IM_MSUX_II,
       "hh3cevtModuleSw-RX-NIC-YGS4L": hh3cevtModuleSw_RX_NIC_YGS4L,
       "hh3cevtModuleSw-RX-NIC-CQ2LF": hh3cevtModuleSw_RX_NIC_CQ2LF,
       "hh3cevtModuleSw-RX-SRP1Q3": hh3cevtModuleSw_RX_SRP1Q3,
       "hh3cevtModuleSw-RX-SFC-08E": hh3cevtModuleSw_RX_SFC_08E,
       "hh3cevtModuleSw-RX-SFC-16E": hh3cevtModuleSw_RX_SFC_16E,
       "hh3cevtModuleSw-RX-NIC-LGQ2L": hh3cevtModuleSw_RX_NIC_LGQ2L,
       "hh3cevtModuleSw-RX-NIC-CQ1LF": hh3cevtModuleSw_RX_NIC_CQ1LF,
       "hh3cevtModuleSw-IM-SFMX": hh3cevtModuleSw_IM_SFMX,
       "hh3cevtModuleSw-MIC-SM": hh3cevtModuleSw_MIC_SM,
       "hh3cevtModuleSw-RX-NIC-CQ1L": hh3cevtModuleSw_RX_NIC_CQ1L,
       "hh3cevtModuleSw-RX-NIC-CQ2L": hh3cevtModuleSw_RX_NIC_CQ2L,
       "hh3cevtModuleSw-NIC-GP24L": hh3cevtModuleSw_NIC_GP24L,
       "hh3cevtModuleSw-NIC-CQ1L": hh3cevtModuleSw_NIC_CQ1L,
       "hh3cevtModuleSw-NIC-CQ2L": hh3cevtModuleSw_NIC_CQ2L,
       "hh3cevtModuleSw-LSUM2GP44TSSE9": hh3cevtModuleSw_LSUM2GP44TSSE9,
       "hh3cevtModuleSw-LSUM2GP24TSSE9": hh3cevtModuleSw_LSUM2GP24TSSE9,
       "hh3cevtModuleSw-LSUM2GT24TSSE9": hh3cevtModuleSw_LSUM2GT24TSSE9,
       "hh3cevtModuleSw-LSUM2GT48SE9": hh3cevtModuleSw_LSUM2GT48SE9,
       "hh3cevtModuleSw-LSUM1SUPD0": hh3cevtModuleSw_LSUM1SUPD0,
       "hh3cevtModuleSw-LSUM1SUPD9": hh3cevtModuleSw_LSUM1SUPD9,
       "hh3cevtModuleSw-LSXM1TGT48FX0": hh3cevtModuleSw_LSXM1TGT48FX0,
       "hh3cevtModuleSw-LSXM1TGS48FX0": hh3cevtModuleSw_LSXM1TGS48FX0,
       "hh3cevtModuleSw-LSXM1TGS48FE0": hh3cevtModuleSw_LSXM1TGS48FE0,
       "hh3cevtModuleSw-LSXM1QGS36FX0": hh3cevtModuleSw_LSXM1QGS36FX0,
       "hh3cevtModuleSw-LSXM1QGS24FX0": hh3cevtModuleSw_LSXM1QGS24FX0,
       "hh3cevtModuleSw-LSXM1QGS24FE0": hh3cevtModuleSw_LSXM1QGS24FE0,
       "hh3cevtModuleSw-LSXM1CGX8FX0": hh3cevtModuleSw_LSXM1CGX8FX0,
       "hh3cevtModuleSw-LSXM1CGP12FX0": hh3cevtModuleSw_LSXM1CGP12FX0,
       "hh3cevtModuleSw-LSXM1SUPB0": hh3cevtModuleSw_LSXM1SUPB0,
       "hh3cevtModuleSw-LSXM1SFF16C0": hh3cevtModuleSw_LSXM1SFF16C0,
       "hh3cevtModuleSw-LSXM1SFF16A0": hh3cevtModuleSw_LSXM1SFF16A0,
       "hh3cevtModuleSw-LSXM1SFF08B0": hh3cevtModuleSw_LSXM1SFF08B0,
       "hh3cevtModuleSw-LSQM6GV48SC0": hh3cevtModuleSw_LSQM6GV48SC0,
       "hh3cevtModuleSw-LSXM1SUP04B1": hh3cevtModuleSw_LSXM1SUP04B1,
       "hh3cevtModuleSw-LSXM1SFF04B1": hh3cevtModuleSw_LSXM1SFF04B1,
       "hh3cevtModuleSw-LSXM1SUP04B0": hh3cevtModuleSw_LSXM1SUP04B0,
       "hh3cevtModuleSw-LSXM1SFF04B0": hh3cevtModuleSw_LSXM1SFF04B0,
       "hh3cevtModuleSw-LSU1ADECEA0": hh3cevtModuleSw_LSU1ADECEA0,
       "hh3cevtModuleSw-LSU1NSCEA0": hh3cevtModuleSw_LSU1NSCEA0,
       "hh3cevtModuleSw-LSU3FWCEA0": hh3cevtModuleSw_LSU3FWCEA0,
       "hh3cevtModuleSw-LSXM1MPU06B3": hh3cevtModuleSw_LSXM1MPU06B3,
       "hh3cevtModuleSw-LSXM1MPU10C3": hh3cevtModuleSw_LSXM1MPU10C3,
       "hh3cevtModuleSw-LSXM1SUPD3": hh3cevtModuleSw_LSXM1SUPD3,
       "hh3cevtModuleSw-LSXM1FAB06C3": hh3cevtModuleSw_LSXM1FAB06C3,
       "hh3cevtModuleSw-LSXM1FAB10C3": hh3cevtModuleSw_LSXM1FAB10C3,
       "hh3cevtModuleSw-LSXM1FAB12D3": hh3cevtModuleSw_LSXM1FAB12D3,
       "hh3cevtModuleSw-LSXM1FAB04D3": hh3cevtModuleSw_LSXM1FAB04D3,
       "hh3cevtModuleSw-LSXM1FAB08D3": hh3cevtModuleSw_LSXM1FAB08D3,
       "hh3cevtModuleSw-LSXM1GP44TSSE3": hh3cevtModuleSw_LSXM1GP44TSSE3,
       "hh3cevtModuleSw-LSXM1GP24TSSE3": hh3cevtModuleSw_LSXM1GP24TSSE3,
       "hh3cevtModuleSw-LSXM1GT24PTSSE3": hh3cevtModuleSw_LSXM1GT24PTSSE3,
       "hh3cevtModuleSw-LSXM1GT48SE3": hh3cevtModuleSw_LSXM1GT48SE3,
       "hh3cevtModuleSw-LSXM1TGS24EC3": hh3cevtModuleSw_LSXM1TGS24EC3,
       "hh3cevtModuleSw-LSXM1CGC2EC3": hh3cevtModuleSw_LSXM1CGC2EC3,
       "hh3cevtModuleSw-LSXM1TGT24SF3": hh3cevtModuleSw_LSXM1TGT24SF3,
       "hh3cevtModuleSw-LSXM1TGS16SF3": hh3cevtModuleSw_LSXM1TGS16SF3,
       "hh3cevtModuleSw-LSXM1QGS12SG3": hh3cevtModuleSw_LSXM1QGS12SG3,
       "hh3cevtModuleSw-LSXM1TGS48SG3": hh3cevtModuleSw_LSXM1TGS48SG3,
       "hh3cevtModuleSw-LSQM1FAB04B3": hh3cevtModuleSw_LSQM1FAB04B3,
       "hh3cevtModuleSw-LSQM1FAB08B3": hh3cevtModuleSw_LSQM1FAB08B3,
       "hh3cevtModuleSw-LSQM1FAB12B3": hh3cevtModuleSw_LSQM1FAB12B3,
       "hh3cevtModuleSw-LSXM1SFF08A0": hh3cevtModuleSw_LSXM1SFF08A0,
       "hh3cevtModuleSw-LSXM1SFF08A1": hh3cevtModuleSw_LSXM1SFF08A1,
       "hh3cevtModuleSw-LSXM1FWDF1": hh3cevtModuleSw_LSXM1FWDF1,
       "hh3cevtModuleSw-LSQM1PT8TSSC0": hh3cevtModuleSw_LSQM1PT8TSSC0,
       "hh3cevtModuleSw-LSQM1PT24TSSC0": hh3cevtModuleSw_LSQM1PT24TSSC0,
       "hh3cevtModuleSw-LSQM1TGS12EC0": hh3cevtModuleSw_LSQM1TGS12EC0,
       "hh3cevtModuleSw-LSX1M1CGQ32TB1": hh3cevtModuleSw_LSX1M1CGQ32TB1,
       "hh3cevtModuleSw-LSX1M1CGQ48TB1": hh3cevtModuleSw_LSX1M1CGQ48TB1,
       "hh3cevtModuleSw-LSXM1QGS48TB1": hh3cevtModuleSw_LSXM1QGS48TB1,
       "hh3cevtModuleSw-LSXM1SRT08E1": hh3cevtModuleSw_LSXM1SRT08E1,
       "hh3cevtModuleSw-LSXM1SRT16E1": hh3cevtModuleSw_LSXM1SRT16E1,
       "hh3cevtModuleSw-LSXM1SRT02E1": hh3cevtModuleSw_LSXM1SRT02E1,
       "hh3cevtModuleSw-LSXM1SUP02B1": hh3cevtModuleSw_LSXM1SUP02B1,
       "hh3cevtModuleSw-LSUM1SUPC0": hh3cevtModuleSw_LSUM1SUPC0,
       "hh3cevtModuleSw-LSUM1SUPC3": hh3cevtModuleSw_LSUM1SUPC3,
       "hh3cevtModuleSw-LSXM1SUPC3": hh3cevtModuleSw_LSXM1SUPC3,
       "hh3cevtModuleSw-LSQM1GP44TSSE0": hh3cevtModuleSw_LSQM1GP44TSSE0,
       "hh3cevtModuleSw-LSQM1GP24TSSE0": hh3cevtModuleSw_LSQM1GP24TSSE0,
       "hh3cevtModuleSw-LSQM1GT48SE0": hh3cevtModuleSw_LSQM1GT48SE0,
       "hh3cevtModuleSw-LSQM1GV48SE0": hh3cevtModuleSw_LSQM1GV48SE0,
       "hh3cevtModuleSw-LSXM1QGS12FX0": hh3cevtModuleSw_LSXM1QGS12FX0,
       "hh3cevtModuleSw-LSXM3QGS24FE1": hh3cevtModuleSw_LSXM3QGS24FE1,
       "hh3cevtModuleSw-LSXM3QGS24FX1": hh3cevtModuleSw_LSXM3QGS24FX1,
       "hh3cevtModuleSw-LSXM3QGS36FX1": hh3cevtModuleSw_LSXM3QGS36FX1,
       "hh3cevtModuleSw-LSXM3TGS48FE1": hh3cevtModuleSw_LSXM3TGS48FE1,
       "hh3cevtModuleSw-LSXM3TGS48FX1": hh3cevtModuleSw_LSXM3TGS48FX1,
       "hh3cevtModuleSw-LSXM2TGS48FX1": hh3cevtModuleSw_LSXM2TGS48FX1,
       "hh3cevtModuleSw-LSQM1MPU06B0": hh3cevtModuleSw_LSQM1MPU06B0,
       "hh3cevtModuleSw-LSQM1MPU10C0": hh3cevtModuleSw_LSQM1MPU10C0,
       "hh3cevtModuleSw-LSQM1FAB06C0": hh3cevtModuleSw_LSQM1FAB06C0,
       "hh3cevtModuleSw-LSQM1FAB10C0": hh3cevtModuleSw_LSQM1FAB10C0,
       "hh3cevtModuleSw-LSQM1QGS12SG0": hh3cevtModuleSw_LSQM1QGS12SG0,
       "hh3cevtModuleSw-LSQM1TGS48SG0": hh3cevtModuleSw_LSQM1TGS48SG0,
       "hh3cevtModuleSw-LSQM1TGT24SF0": hh3cevtModuleSw_LSQM1TGT24SF0,
       "hh3cevtModuleSw-LSQM1QGS8A0": hh3cevtModuleSw_LSQM1QGS8A0,
       "hh3cevtModuleSw-LSQM1TGS24QSM0": hh3cevtModuleSw_LSQM1TGS24QSM0,
       "hh3cevtModuleSw-LSQM1TGT24QSM0": hh3cevtModuleSw_LSQM1TGT24QSM0,
       "hh3cevtModuleSw-LSQM1TGS24QSA0": hh3cevtModuleSw_LSQM1TGS24QSA0,
       "hh3cevtModuleSw-LSUM1FWCEAB0": hh3cevtModuleSw_LSUM1FWCEAB0,
       "hh3cevtModuleSw-LSQM2GP24TSSA0": hh3cevtModuleSw_LSQM2GP24TSSA0,
       "hh3cevtModuleSw-LSQM2GT48SA0": hh3cevtModuleSw_LSQM2GT48SA0,
       "hh3cevtModuleSw-LSQM2GP48SA0": hh3cevtModuleSw_LSQM2GP48SA0,
       "hh3cevtModuleSw-LSQM2GP24TSSA3": hh3cevtModuleSw_LSQM2GP24TSSA3,
       "hh3cevtModuleSw-LSQM2GT48SA3": hh3cevtModuleSw_LSQM2GT48SA3,
       "hh3cevtModuleSw-LSQM2GP48SA3": hh3cevtModuleSw_LSQM2GP48SA3,
       "hh3cevtModuleSw-LSUM2GP24TSSA0": hh3cevtModuleSw_LSUM2GP24TSSA0,
       "hh3cevtModuleSw-LSUM2GT48SA0": hh3cevtModuleSw_LSUM2GT48SA0,
       "hh3cevtModuleSw-LSUM2GP48SA0": hh3cevtModuleSw_LSUM2GP48SA0,
       "hh3cevtModuleSw-LSXM1SUPT1": hh3cevtModuleSw_LSXM1SUPT1,
       "hh3cevtModuleSw-LSXM1SUP02T1": hh3cevtModuleSw_LSXM1SUP02T1,
       "hh3cevtModuleSw-LSXM1SFF16B0": hh3cevtModuleSw_LSXM1SFF16B0,
       "hh3cevtModuleSw-LSXM4TGS48FX1": hh3cevtModuleSw_LSXM4TGS48FX1,
       "hh3cevtModuleSw-LSXM4QGS24FX1": hh3cevtModuleSw_LSXM4QGS24FX1,
       "hh3cevtModuleSw-LSXM1TGS48FD1": hh3cevtModuleSw_LSXM1TGS48FD1,
       "hh3cevtModuleSw-LSXM1QGS24FD1": hh3cevtModuleSw_LSXM1QGS24FD1,
       "hh3cevtModuleSw-LSXM2QGS24FX1": hh3cevtModuleSw_LSXM2QGS24FX1,
       "hh3cevtModuleSw-LSXM1TGS48FD0": hh3cevtModuleSw_LSXM1TGS48FD0,
       "hh3cevtModuleSw-LSXM1QGS24FD0": hh3cevtModuleSw_LSXM1QGS24FD0,
       "hh3cevtModuleSw-LSXM2TGS48FX0": hh3cevtModuleSw_LSXM2TGS48FX0,
       "hh3cevtModuleSw-LSXM2QGS24FX0": hh3cevtModuleSw_LSXM2QGS24FX0,
       "hh3cevtModuleSw-LSXM4TGS48FX0": hh3cevtModuleSw_LSXM4TGS48FX0,
       "hh3cevtModuleSw-LSXM4QGS24FX0": hh3cevtModuleSw_LSXM4QGS24FX0,
       "hh3cevtModuleSw-LSXM1TGW48FX1": hh3cevtModuleSw_LSXM1TGW48FX1,
       "hh3cevtModuleSw-LSUM1MPU10A0": hh3cevtModuleSw_LSUM1MPU10A0,
       "hh3cevtModuleSw-LSUM1FAB10A0": hh3cevtModuleSw_LSUM1FAB10A0,
       "hh3cevtModuleSw-LSUM2TGS32QSSG0": hh3cevtModuleSw_LSUM2TGS32QSSG0,
       "hh3cevtModuleSw-LSUM2QGS12SG0": hh3cevtModuleSw_LSUM2QGS12SG0,
       "hh3cevtModuleSw-LSUM2TGS48SG0": hh3cevtModuleSw_LSUM2TGS48SG0,
       "hh3cevtModuleSw-LSXM2QGS12SG3": hh3cevtModuleSw_LSXM2QGS12SG3,
       "hh3cevtModuleSw-LSXM2TGS48SG3": hh3cevtModuleSw_LSXM2TGS48SG3,
       "hh3cevtModuleSw-LSUM1FWDEC0": hh3cevtModuleSw_LSUM1FWDEC0,
       "hh3cevtModuleSw-LSQM1FWDSC0": hh3cevtModuleSw_LSQM1FWDSC0,
       "hh3cevtModuleSw-LSQM1TGS48RSG0": hh3cevtModuleSw_LSQM1TGS48RSG0,
       "hh3cevtModuleSw-LSQM2TGS48XSG0": hh3cevtModuleSw_LSQM2TGS48XSG0,
       "hh3cevtModuleSw-LSQM2QGS12XSG0": hh3cevtModuleSw_LSQM2QGS12XSG0,
       "hh3cevtModuleSw-LSQM3GP44TSSC0": hh3cevtModuleSw_LSQM3GP44TSSC0,
       "hh3cevtModuleSw-LSXM1CGQ36HB1": hh3cevtModuleSw_LSXM1CGQ36HB1,
       "hh3cevtModuleSw-LSXM1CGQ36HC1": hh3cevtModuleSw_LSXM1CGQ36HC1,
       "hh3cevtModuleSw-LSXM1CGQ18QGHB1": hh3cevtModuleSw_LSXM1CGQ18QGHB1,
       "hh3cevtModuleSw-LSXM1CGQ18QGHC1": hh3cevtModuleSw_LSXM1CGQ18QGHC1,
       "hh3cevtModuleSw-LSXM1QGS48HB1": hh3cevtModuleSw_LSXM1QGS48HB1,
       "hh3cevtModuleSw-LSXM1QGS48HC1": hh3cevtModuleSw_LSXM1QGS48HC1,
       "hh3cevtModuleSw-LSXM1TGS48C2HB1": hh3cevtModuleSw_LSXM1TGS48C2HB1,
       "hh3cevtModuleSw-LSXM1SFH04D1": hh3cevtModuleSw_LSXM1SFH04D1,
       "hh3cevtModuleSw-LSXM1SFH08D1": hh3cevtModuleSw_LSXM1SFH08D1,
       "hh3cevtModuleSw-LSXM1SFH12D1": hh3cevtModuleSw_LSXM1SFH12D1,
       "hh3cevtModuleSw-LSXM1SFH16C1": hh3cevtModuleSw_LSXM1SFH16C1,
       "hh3cevtModuleSw-LSXM1GP48FD0": hh3cevtModuleSw_LSXM1GP48FD0,
       "hh3cevtModuleSw-LSXM1GP48FD1": hh3cevtModuleSw_LSXM1GP48FD1,
       "hh3cevtModuleSw-LSXM1GT48FD0": hh3cevtModuleSw_LSXM1GT48FD0,
       "hh3cevtModuleSw-LSXM1GT48FD1": hh3cevtModuleSw_LSXM1GT48FD1,
       "hh3cevtModuleSw-LSXM1FAB10B0": hh3cevtModuleSw_LSXM1FAB10B0,
       "hh3cevtModuleSw-LSUM1MPU10A3": hh3cevtModuleSw_LSUM1MPU10A3,
       "hh3cevtModuleSw-LSUM1FAB10A3": hh3cevtModuleSw_LSUM1FAB10A3,
       "hh3cevtModuleSw-LSQM1MPU10A0": hh3cevtModuleSw_LSQM1MPU10A0,
       "hh3cevtModuleSw-LSQM1FAB10A0": hh3cevtModuleSw_LSQM1FAB10A0,
       "hh3cevtModuleSw-LSQM2TGS32QSXSG0": hh3cevtModuleSw_LSQM2TGS32QSXSG0,
       "hh3cevtModuleSw-LSQM1TGS48RSG3": hh3cevtModuleSw_LSQM1TGS48RSG3,
       "hh3cevtModuleSw-LSXM2TGS32QSSG3": hh3cevtModuleSw_LSXM2TGS32QSSG3,
       "hh3cevtModuleSw-LSUM1NSDEC0": hh3cevtModuleSw_LSUM1NSDEC0,
       "hh3cevtModuleSw-LSQM1NSDSC0": hh3cevtModuleSw_LSQM1NSDSC0,
       "hh3cevtModuleSw-LSQM1QGS4SC0": hh3cevtModuleSw_LSQM1QGS4SC0,
       "hh3cevtModuleSw-LLSQM2MPUD3": hh3cevtModuleSw_LLSQM2MPUD3,
       "hh3cevtModuleSw-LLSQM3MPUB3": hh3cevtModuleSw_LLSQM3MPUB3,
       "hh3cevtModuleSw-LSQM3MPUB4": hh3cevtModuleSw_LSQM3MPUB4,
       "hh3cevtModuleSw-LSQM2MPUDS0": hh3cevtModuleSw_LSQM2MPUDS0,
       "hh3cevtModuleSw-LSQM4GV48SA0": hh3cevtModuleSw_LSQM4GV48SA0,
       "hh3cevtModuleSw-LSQM1WCMX20": hh3cevtModuleSw_LSQM1WCMX20,
       "hh3cevtModuleSw-LSQM1WCMX40": hh3cevtModuleSw_LSQM1WCMX40,
       "hh3cevtModuleSw-LSUM1WCMX20RT": hh3cevtModuleSw_LSUM1WCMX20RT,
       "hh3cevtModuleSw-LSUM1WCMX40RT": hh3cevtModuleSw_LSUM1WCMX40RT,
       "hh3cevtModuleSw-LSXM1CGQ18QGHB0": hh3cevtModuleSw_LSXM1CGQ18QGHB0,
       "hh3cevtModuleSw-LSXM1SFH08C0": hh3cevtModuleSw_LSXM1SFH08C0,
       "hh3cevtModuleSw-LSXM1SFH08C1": hh3cevtModuleSw_LSXM1SFH08C1,
       "hh3cevtModuleSw-LSXM2SFH16C0": hh3cevtModuleSw_LSXM2SFH16C0,
       "hh3cevtModuleSw-LSXM2SFH16C1": hh3cevtModuleSw_LSXM2SFH16C1,
       "hh3cevtModuleSw-LSXM1NSDF1": hh3cevtModuleSw_LSXM1NSDF1,
       "hh3cevtModuleSw-LSUM2TGS48SG3": hh3cevtModuleSw_LSUM2TGS48SG3,
       "hh3cevtModuleSw-DS-3E7602-MPU": hh3cevtModuleSw_DS_3E7602_MPU,
       "hh3cevtModuleSw-DS-3E7606-MPU": hh3cevtModuleSw_DS_3E7606_MPU,
       "hh3cevtModuleSw-DS-3E7600-24T4X-SC": hh3cevtModuleSw_DS_3E7600_24T4X_SC,
       "hh3cevtModuleSw-DS-3E7600-24F4X-SA": hh3cevtModuleSw_DS_3E7600_24F4X_SA,
       "hh3cevtModuleSw-DS-3E7600-48T-SA": hh3cevtModuleSw_DS_3E7600_48T_SA,
       "hh3cevtModuleSw-DS-3E7600-48F-SA": hh3cevtModuleSw_DS_3E7600_48F_SA,
       "hh3cevtModuleSw-DS-3E7600-24F4X-SC": hh3cevtModuleSw_DS_3E7600_24F4X_SC,
       "hh3cevtModuleSw-DS-3E7600-44F4X-SC": hh3cevtModuleSw_DS_3E7600_44F4X_SC,
       "hh3cevtModuleSw-DS-3E7600-48T-SC": hh3cevtModuleSw_DS_3E7600_48T_SC,
       "hh3cevtModuleSw-DS-3E7600-16X-SC": hh3cevtModuleSw_DS_3E7600_16X_SC,
       "hh3cevtModuleSw-S7602-MPU": hh3cevtModuleSw_S7602_MPU,
       "hh3cevtModuleSw-S7606-MPU": hh3cevtModuleSw_S7606_MPU,
       "hh3cevtModuleSw-S76-24GT4XFSC": hh3cevtModuleSw_S76_24GT4XFSC,
       "hh3cevtModuleSw-S76-24GF4XFSA": hh3cevtModuleSw_S76_24GF4XFSA,
       "hh3cevtModuleSw-S76-48GTSA": hh3cevtModuleSw_S76_48GTSA,
       "hh3cevtModuleSw-S76-48GFSA": hh3cevtModuleSw_S76_48GFSA,
       "hh3cevtModuleSw-S76-24GT20GF4XFSC": hh3cevtModuleSw_S76_24GT20GF4XFSC,
       "hh3cevtModuleSw-LSXM1TGS48C2HB0": hh3cevtModuleSw_LSXM1TGS48C2HB0,
       "hh3cevtModuleSw-LSXM1CGQ18QGHC0": hh3cevtModuleSw_LSXM1CGQ18QGHC0,
       "hh3cevtModuleSw-LSXM1TGS48HB1": hh3cevtModuleSw_LSXM1TGS48HB1,
       "hh3cevtModuleSw-LSXM1TGS48HB0": hh3cevtModuleSw_LSXM1TGS48HB0,
       "hh3cevtModuleSw-LSQM1CGP24TSSC0": hh3cevtModuleSw_LSQM1CGP24TSSC0,
       "hh3cevtModuleSw-LSQM1CGP24TSSA0": hh3cevtModuleSw_LSQM1CGP24TSSA0,
       "hh3cevtModuleSw-LSQM1CGT24TSSC0": hh3cevtModuleSw_LSQM1CGT24TSSC0,
       "hh3cevtModuleSw-LSQM1CGT24TSSA0": hh3cevtModuleSw_LSQM1CGT24TSSA0,
       "hh3cevtModuleSw-LSQM2GP24SA0": hh3cevtModuleSw_LSQM2GP24SA0,
       "hh3cevtModuleSw-LSX1SUPH1": hh3cevtModuleSw_LSX1SUPH1,
       "hh3cevtModuleSw-LSX1SUPH0": hh3cevtModuleSw_LSX1SUPH0,
       "hh3cevtModuleSw-LSX1SUP04H1": hh3cevtModuleSw_LSX1SUP04H1,
       "hh3cevtModuleSw-LSX1SUP04H0": hh3cevtModuleSw_LSX1SUP04H0,
       "hh3cevtModuleSw-LSXM1SFH08D0": hh3cevtModuleSw_LSXM1SFH08D0,
       "hh3cevtModuleSw-LSXM1SFH04D0": hh3cevtModuleSw_LSXM1SFH04D0,
       "hh3cevtModuleSw-LSXM1SFH16C0": hh3cevtModuleSw_LSXM1SFH16C0,
       "hh3cevtModuleSw-LSXM1SFH12D0": hh3cevtModuleSw_LSXM1SFH12D0,
       "hh3cevtModuleSw-LSXM1QGS48HB0": hh3cevtModuleSw_LSXM1QGS48HB0,
       "hh3cevtModuleSw-LSXM1QGS48HC0": hh3cevtModuleSw_LSXM1QGS48HC0,
       "hh3cevtModuleSw-LSXM1CGQ36HB0": hh3cevtModuleSw_LSXM1CGQ36HB0,
       "hh3cevtModuleSw-LSXM1TGS48C2HC0": hh3cevtModuleSw_LSXM1TGS48C2HC0,
       "hh3cevtModuleSw-LSQM2GP44TSSE0": hh3cevtModuleSw_LSQM2GP44TSSE0,
       "hh3cevtModuleSw-LSQM2GP24TSSA8": hh3cevtModuleSw_LSQM2GP24TSSA8,
       "hh3cevtModuleSw-LSQM2GT48SA8": hh3cevtModuleSw_LSQM2GT48SA8,
       "hh3cevtModuleSw-LSQM2GP48SA8": hh3cevtModuleSw_LSQM2GP48SA8,
       "hh3cevtModuleSw-EWPXM1CGP24TSSC0": hh3cevtModuleSw_EWPXM1CGP24TSSC0,
       "hh3cevtModuleSw-EWPXM3MPUB0": hh3cevtModuleSw_EWPXM3MPUB0,
       "hh3cevtModuleSw-EWPXM2MPUDS0": hh3cevtModuleSw_EWPXM2MPUDS0,
       "hh3cevtModuleSw-EWPXM2TGS16SF0": hh3cevtModuleSw_EWPXM2TGS16SF0,
       "hh3cevtModuleSw-EWPXM2GP44TSSC0": hh3cevtModuleSw_EWPXM2GP44TSSC0,
       "hh3cevtModuleSw-EWPXM2GP24TSSC0": hh3cevtModuleSw_EWPXM2GP24TSSC0,
       "hh3cevtModuleSw-EWPXM1MAC0F": hh3cevtModuleSw_EWPXM1MAC0F,
       "hh3cevtModuleSw-LSQM1CGP24TSSA8": hh3cevtModuleSw_LSQM1CGP24TSSA8,
       "hh3cevtModuleSw-LSQM1CGT24TSSA8": hh3cevtModuleSw_LSQM1CGT24TSSA8,
       "hh3cevtModuleSw-LSWM1FWD0": hh3cevtModuleSw_LSWM1FWD0,
       "hh3cevtModuleSw-LSUM2MPU10C0": hh3cevtModuleSw_LSUM2MPU10C0,
       "hh3cevtModuleSw-LSQM2MPU10C0": hh3cevtModuleSw_LSQM2MPU10C0,
       "hh3cevtModuleSw-LSUM2MPU10C3": hh3cevtModuleSw_LSUM2MPU10C3,
       "hh3cevtModuleSw-LSUM2FAB10C0": hh3cevtModuleSw_LSUM2FAB10C0,
       "hh3cevtModuleSw-LSQM2FAB10C0": hh3cevtModuleSw_LSQM2FAB10C0,
       "hh3cevtModuleSw-LSUM2FAB10C3": hh3cevtModuleSw_LSUM2FAB10C3,
       "hh3cevtModuleSw-LSUM2CQGS12SG0": hh3cevtModuleSw_LSUM2CQGS12SG0,
       "hh3cevtModuleSw-LSXM2CQGS12SG3": hh3cevtModuleSw_LSXM2CQGS12SG3,
       "hh3cevtModuleSw-LSQM2CQGS12XSG0": hh3cevtModuleSw_LSQM2CQGS12XSG0,
       "hh3cevtModuleSw-LSQM1CQGS12SG0": hh3cevtModuleSw_LSQM1CQGS12SG0,
       "hh3cevtModuleSw-LSXM1CGQ6QGHB0": hh3cevtModuleSw_LSXM1CGQ6QGHB0,
       "hh3cevtModuleSw-LSXM1CGQ6QGHB1": hh3cevtModuleSw_LSXM1CGQ6QGHB1,
       "hh3cevtModuleSw-LSXM1CGQ6QGHC0": hh3cevtModuleSw_LSXM1CGQ6QGHC0,
       "hh3cevtModuleSw-LSXM1QGS36HB0": hh3cevtModuleSw_LSXM1QGS36HB0,
       "hh3cevtModuleSw-LSXM1QGS36HB1": hh3cevtModuleSw_LSXM1QGS36HB1,
       "hh3cevtModuleSw-LSXM1QGS36HC0": hh3cevtModuleSw_LSXM1QGS36HC0,
       "hh3cevtModuleSw-LSXM1SUPC0": hh3cevtModuleSw_LSXM1SUPC0,
       "hh3cevtModuleSw-LSXM1SUPC1": hh3cevtModuleSw_LSXM1SUPC1,
       "hh3cevtModuleSw-LSXM1SUP04H0": hh3cevtModuleSw_LSXM1SUP04H0,
       "hh3cevtModuleSw-LSXM1SUP04H1": hh3cevtModuleSw_LSXM1SUP04H1,
       "hh3cevtModuleSw-LSXM1SUPH0": hh3cevtModuleSw_LSXM1SUPH0,
       "hh3cevtModuleSw-LSXM1SUPH1": hh3cevtModuleSw_LSXM1SUPH1,
       "hh3cevtModuleSw-EWPXM2WCMD0F": hh3cevtModuleSw_EWPXM2WCMD0F,
       "hh3cevtModuleSw-LSUM2QGS24RSG0": hh3cevtModuleSw_LSUM2QGS24RSG0,
       "hh3cevtModuleSw-LSQM1QGS24RSG0": hh3cevtModuleSw_LSQM1QGS24RSG0,
       "hh3cevtModuleSw-LSXM2QGS24RSG3": hh3cevtModuleSw_LSXM2QGS24RSG3,
       "hh3cevtModuleSw-LSQM2QGS24RXSG0": hh3cevtModuleSw_LSQM2QGS24RXSG0,
       "hh3cevtModuleSw-LSQM2TGS48RSG0": hh3cevtModuleSw_LSQM2TGS48RSG0,
       "hh3cevtModuleSw-LSXM1X86SUPE0": hh3cevtModuleSw_LSXM1X86SUPE0,
       "hh3cevtModuleSw-LSXM1X86SUPE1": hh3cevtModuleSw_LSXM1X86SUPE1,
       "hh3cevtModuleSw-LSQM1CGS2QSA0": hh3cevtModuleSw_LSQM1CGS2QSA0,
       "hh3cevtModuleSw-LSUM1ACGDEC0": hh3cevtModuleSw_LSUM1ACGDEC0,
       "hh3cevtModuleSw-LSQM1ACGDSC0": hh3cevtModuleSw_LSQM1ACGDSC0,
       "hh3cevtModuleSw-LSXM1CGQ36HF1": hh3cevtModuleSw_LSXM1CGQ36HF1,
       "hh3cevtModuleSw-LSXM1QGS48HF1": hh3cevtModuleSw_LSXM1QGS48HF1,
       "hh3cevtModuleSw-LSXM1CGQ18QGHF1": hh3cevtModuleSw_LSXM1CGQ18QGHF1,
       "hh3cevtModuleSw-LSXM1QGS36HF1": hh3cevtModuleSw_LSXM1QGS36HF1,
       "hh3cevtModuleSw-LSXM1CGQ6QGHF1": hh3cevtModuleSw_LSXM1CGQ6QGHF1,
       "hh3cevtModuleSw-LSXM1QGS48HF0": hh3cevtModuleSw_LSXM1QGS48HF0,
       "hh3cevtModuleSw-LSXM1CGQ18QGHF0": hh3cevtModuleSw_LSXM1CGQ18QGHF0,
       "hh3cevtModuleSw-LSXM1CGQ6QGHF0": hh3cevtModuleSw_LSXM1CGQ6QGHF0,
       "hh3cevtModuleSw-LSXM1TGS48HF0": hh3cevtModuleSw_LSXM1TGS48HF0,
       "hh3cevtModuleSw-LSXM1TGS48HF1": hh3cevtModuleSw_LSXM1TGS48HF1,
       "hh3cevtModuleSw-LSQM1GP24FC3": hh3cevtModuleSw_LSQM1GP24FC3,
       "hh3cevtModuleSw-LSQM1GP24FD3": hh3cevtModuleSw_LSQM1GP24FD3,
       "hh3cevtModuleSw-LSQM1GP24TSFC3": hh3cevtModuleSw_LSQM1GP24TSFC3,
       "hh3cevtModuleSw-LSQM1GP24TSFD3": hh3cevtModuleSw_LSQM1GP24TSFD3,
       "hh3cevtModuleSw-LSQM1GP40TS8FD0": hh3cevtModuleSw_LSQM1GP40TS8FD0,
       "hh3cevtModuleSw-LSQM1GP48FC3": hh3cevtModuleSw_LSQM1GP48FC3,
       "hh3cevtModuleSw-LSQM1GP48FD0": hh3cevtModuleSw_LSQM1GP48FD0,
       "hh3cevtModuleSw-LSQM1GP48FD3": hh3cevtModuleSw_LSQM1GP48FD3,
       "hh3cevtModuleSw-LSQM1GT48FC3": hh3cevtModuleSw_LSQM1GT48FC3,
       "hh3cevtModuleSw-LSQM1GT48FD0": hh3cevtModuleSw_LSQM1GT48FD0,
       "hh3cevtModuleSw-LSQM1GT48FD3": hh3cevtModuleSw_LSQM1GT48FD3,
       "hh3cevtModuleSw-LSQM1TGS24FC3": hh3cevtModuleSw_LSQM1TGS24FC3,
       "hh3cevtModuleSw-LSQM1TGS24FD0": hh3cevtModuleSw_LSQM1TGS24FD0,
       "hh3cevtModuleSw-LSQM1TGS24FD3": hh3cevtModuleSw_LSQM1TGS24FD3,
       "hh3cevtModuleSw-LSQM1TGS24XFD0": hh3cevtModuleSw_LSQM1TGS24XFD0,
       "hh3cevtModuleSw-LSQM1TGS48RFE0": hh3cevtModuleSw_LSQM1TGS48RFE0,
       "hh3cevtModuleSw-LSQM1TGS8FC3": hh3cevtModuleSw_LSQM1TGS8FC3,
       "hh3cevtModuleSw-LSQM1TGS8FD3": hh3cevtModuleSw_LSQM1TGS8FD3,
       "hh3cevtModuleSw-LSUM1GP40TS8FD0": hh3cevtModuleSw_LSUM1GP40TS8FD0,
       "hh3cevtModuleSw-LSUM1GP48FD0": hh3cevtModuleSw_LSUM1GP48FD0,
       "hh3cevtModuleSw-LSUM1GP48FD3": hh3cevtModuleSw_LSUM1GP48FD3,
       "hh3cevtModuleSw-LSUM1GT48FD0": hh3cevtModuleSw_LSUM1GT48FD0,
       "hh3cevtModuleSw-LSUM1GT48FD3": hh3cevtModuleSw_LSUM1GT48FD3,
       "hh3cevtModuleSw-LSUM1TGS24FD0": hh3cevtModuleSw_LSUM1TGS24FD0,
       "hh3cevtModuleSw-LSUM1TGS24FD3": hh3cevtModuleSw_LSUM1TGS24FD3,
       "hh3cevtModuleSw-LSXM1GP40TS8FD0": hh3cevtModuleSw_LSXM1GP40TS8FD0,
       "hh3cevtModuleSw-LSXM1GT48FD3": hh3cevtModuleSw_LSXM1GT48FD3,
       "hh3cevtModuleSw-LSXM1TGS24FD3": hh3cevtModuleSw_LSXM1TGS24FD3,
       "hh3cevtModuleSw-LSQM1MPUS10C3": hh3cevtModuleSw_LSQM1MPUS10C3,
       "hh3cevtModuleSw-LSQM1MPUSA3": hh3cevtModuleSw_LSQM1MPUSA3,
       "hh3cevtModuleSw-LSQM2SUPA3": hh3cevtModuleSw_LSQM2SUPA3,
       "hh3cevtModuleSw-LSXM1SFH16E1": hh3cevtModuleSw_LSXM1SFH16E1,
       "hh3cevtModuleSw-LSXM1SFH16E0": hh3cevtModuleSw_LSXM1SFH16E0,
       "hh3cevtModuleSw-LSXM1GP40TS8FD3": hh3cevtModuleSw_LSXM1GP40TS8FD3,
       "hh3cevtModuleSw-LSQM1MPUS10C0": hh3cevtModuleSw_LSQM1MPUS10C0,
       "hh3cevtModuleSw-LSQM1MPUSA0": hh3cevtModuleSw_LSQM1MPUSA0,
       "hh3cevtModuleSw-LSQM2SUPA0": hh3cevtModuleSw_LSQM2SUPA0,
       "hh3cevtModuleSw-LSQM1TGS16FC3": hh3cevtModuleSw_LSQM1TGS16FC3,
       "hh3cevtModuleSw-LSQM1TGS16FD0": hh3cevtModuleSw_LSQM1TGS16FD0,
       "hh3cevtModuleSw-LSQM1TGS16FD3": hh3cevtModuleSw_LSQM1TGS16FD3,
       "hh3cevtModuleSw-LSQM2TGS48SG0": hh3cevtModuleSw_LSQM2TGS48SG0,
       "hh3cevtModuleSw-LSQM2TGS48SG3": hh3cevtModuleSw_LSQM2TGS48SG3,
       "hh3cevtModuleSw-LSXM1CGQ48HB1": hh3cevtModuleSw_LSXM1CGQ48HB1,
       "hh3cevtModuleSw-LSQM1MPUS06A8": hh3cevtModuleSw_LSQM1MPUS06A8,
       "hh3cevtModuleSw-LSQM1TGS16FD8": hh3cevtModuleSw_LSQM1TGS16FD8,
       "hh3cevtModuleSw-LSXM1SFH08E1": hh3cevtModuleSw_LSXM1SFH08E1,
       "hh3cevtModuleSw-LSXM1SFH08CC0": hh3cevtModuleSw_LSXM1SFH08CC0,
       "hh3cevtModuleSw-LSXM1SUP08C0": hh3cevtModuleSw_LSXM1SUP08C0,
       "hh3cevtModuleSw-LSUM2FAB04D0": hh3cevtModuleSw_LSUM2FAB04D0,
       "hh3cevtModuleSw-LSUM2FAB04D3": hh3cevtModuleSw_LSUM2FAB04D3,
       "hh3cevtModuleSw-LSXM2FAB04D3": hh3cevtModuleSw_LSXM2FAB04D3,
       "hh3cevtModuleSw-LSUM2FAB04B0": hh3cevtModuleSw_LSUM2FAB04B0,
       "hh3cevtModuleSw-LSUM2FAB04B3": hh3cevtModuleSw_LSUM2FAB04B3,
       "hh3cevtModuleSw-LSUM2FAB08D0": hh3cevtModuleSw_LSUM2FAB08D0,
       "hh3cevtModuleSw-LSUM2FAB08D3": hh3cevtModuleSw_LSUM2FAB08D3,
       "hh3cevtModuleSw-LSXM2FAB08D3": hh3cevtModuleSw_LSXM2FAB08D3,
       "hh3cevtModuleSw-LSUM2FAB08B0": hh3cevtModuleSw_LSUM2FAB08B0,
       "hh3cevtModuleSw-LSUM2FAB08B3": hh3cevtModuleSw_LSUM2FAB08B3,
       "hh3cevtModuleSw-LSUM2FAB12D0": hh3cevtModuleSw_LSUM2FAB12D0,
       "hh3cevtModuleSw-LSUM2FAB12D3": hh3cevtModuleSw_LSUM2FAB12D3,
       "hh3cevtModuleSw-LSXM2FAB12D3": hh3cevtModuleSw_LSXM2FAB12D3,
       "hh3cevtModuleSw-LSUM2FAB12B0": hh3cevtModuleSw_LSUM2FAB12B0,
       "hh3cevtModuleSw-LSUM2FAB12B3": hh3cevtModuleSw_LSUM2FAB12B3,
       "hh3cevtModuleSw-LSQM1CGS2FE0": hh3cevtModuleSw_LSQM1CGS2FE0,
       "hh3cevtModuleSw-LSQM1CGS2FE3": hh3cevtModuleSw_LSQM1CGS2FE3,
       "hh3cevtModuleSw-LSQM1CGS2XFE0": hh3cevtModuleSw_LSQM1CGS2XFE0,
       "hh3cevtModuleSw-LSUM1CGS2FE0": hh3cevtModuleSw_LSUM1CGS2FE0,
       "hh3cevtModuleSw-LSUM1CGS2FE3": hh3cevtModuleSw_LSUM1CGS2FE3,
       "hh3cevtModuleSw-LSXM1CGS2FE3": hh3cevtModuleSw_LSXM1CGS2FE3,
       "hh3cevtModuleSw-LSUM1TGS16FD0": hh3cevtModuleSw_LSUM1TGS16FD0,
       "hh3cevtModuleSw-LSUM1TGS16FD3": hh3cevtModuleSw_LSUM1TGS16FD3,
       "hh3cevtModuleSw-LSQM1TGS16XFD0": hh3cevtModuleSw_LSQM1TGS16XFD0,
       "hh3cevtModuleSw-LSQM1GP40TS8FC3": hh3cevtModuleSw_LSQM1GP40TS8FC3,
       "hh3cevtModuleSw-S76-16XFSF": hh3cevtModuleSw_S76_16XFSF,
       "hh3cevtModuleSw-S76-24EP2XFSC-OLT": hh3cevtModuleSw_S76_24EP2XFSC_OLT,
       "hh3cevtModuleSw-DS-3E7600-24T20F4X-SC": hh3cevtModuleSw_DS_3E7600_24T20F4X_SC,
       "hh3cevtModuleSw-LSUM1FAB04E0": hh3cevtModuleSw_LSUM1FAB04E0,
       "hh3cevtModuleSw-LSUM1FAB08E0": hh3cevtModuleSw_LSUM1FAB08E0,
       "hh3cevtModuleSw-LSUM1FAB12E0": hh3cevtModuleSw_LSUM1FAB12E0,
       "hh3cevtModuleSw-LSXM1CGQ8FX1": hh3cevtModuleSw_LSXM1CGQ8FX1,
       "hh3cevtModuleSw-LSQM1IPSDSC0": hh3cevtModuleSw_LSQM1IPSDSC0,
       "hh3cevtModuleSw-LSQM2ACGDSC0": hh3cevtModuleSw_LSQM2ACGDSC0,
       "hh3cevtModuleSw-LSQM1ADEDSC0": hh3cevtModuleSw_LSQM1ADEDSC0,
       "hh3cevtModuleSw-LSWM1ADED0": hh3cevtModuleSw_LSWM1ADED0,
       "hh3cevtModuleSw-LSWM1IPSD0": hh3cevtModuleSw_LSWM1IPSD0,
       "hh3cevtModuleSw-LSQM1GP40TS8FD3": hh3cevtModuleSw_LSQM1GP40TS8FD3,
       "hh3cevtModuleSw-LSUM1SUPXD0": hh3cevtModuleSw_LSUM1SUPXD0,
       "hh3cevtModuleSw-LSUM1CQGS32SF0": hh3cevtModuleSw_LSUM1CQGS32SF0,
       "hh3cevtModuleSw-LSUM1TGS48XSG0": hh3cevtModuleSw_LSUM1TGS48XSG0,
       "hh3cevtModuleSw-LSUM1FAB08XE0": hh3cevtModuleSw_LSUM1FAB08XE0,
       "hh3cevtModuleSw-LSUM1FAB16XD0": hh3cevtModuleSw_LSUM1FAB16XD0,
       "hh3cevtModuleSw-LSXM1SFH02E0": hh3cevtModuleSw_LSXM1SFH02E0,
       "hh3cevtModuleSw-LSXM1SFH02E1": hh3cevtModuleSw_LSXM1SFH02E1,
       "hh3cevtModuleSw-LSXM1SFH12C0": hh3cevtModuleSw_LSXM1SFH12C0,
       "hh3cevtModuleSw-LSXM1SFH12C1": hh3cevtModuleSw_LSXM1SFH12C1,
       "hh3cevtModuleSw-LSUM1CQGS12XSG0": hh3cevtModuleSw_LSUM1CQGS12XSG0,
       "hh3cevtModuleSw-LSQM1CTGS24QSFD0": hh3cevtModuleSw_LSQM1CTGS24QSFD0,
       "hh3cevtModuleSw-LSQM1TGS24QSFD0": hh3cevtModuleSw_LSQM1TGS24QSFD0,
       "hh3cevtModuleSw-LSUM1WBCZ720RT": hh3cevtModuleSw_LSUM1WBCZ720RT,
       "hh3cevtModuleSw-LSQM1WBCZ720": hh3cevtModuleSw_LSQM1WBCZ720,
       "hh3cevtModuleSw-DS-3E7610X-MPU": hh3cevtModuleSw_DS_3E7610X_MPU,
       "hh3cevtModuleSw-DS-3E7610X-CLOS": hh3cevtModuleSw_DS_3E7610X_CLOS,
       "hh3cevtModuleSw-DS-3E7610X-32X4QX-SF": hh3cevtModuleSw_DS_3E7610X_32X4QX_SF,
       "hh3cevtModuleSw-DS-3E7610X-16X-SF": hh3cevtModuleSw_DS_3E7610X_16X_SF,
       "hh3cevtModuleSw-DS-3E7610X-44F4X-SE": hh3cevtModuleSw_DS_3E7610X_44F4X_SE,
       "hh3cevtModuleSw-DS-3E7610X-48T-SE": hh3cevtModuleSw_DS_3E7610X_48T_SE,
       "hh3cevtModuleSw-LSQM2GT24PTSSC8": hh3cevtModuleSw_LSQM2GT24PTSSC8,
       "hh3cevtModuleSw-LSQM1CGP24TSSC8": hh3cevtModuleSw_LSQM1CGP24TSSC8,
       "hh3cevtModuleSw-LSQM1CGT24TSSC8": hh3cevtModuleSw_LSQM1CGT24TSSC8,
       "hh3cevtModuleSw-LSQM1MPUS06B8": hh3cevtModuleSw_LSQM1MPUS06B8,
       "hh3cevtModuleSw-LSVM1MPUB1": hh3cevtModuleSw_LSVM1MPUB1,
       "hh3cevtModuleSw-LSXM1TGS24QGMODHB0": hh3cevtModuleSw_LSXM1TGS24QGMODHB0,
       "hh3cevtModuleSw-LSXM1TGS24QGMODHB1": hh3cevtModuleSw_LSXM1TGS24QGMODHB1,
       "hh3cevtModuleSw-LSXM1TGS48QGHA0": hh3cevtModuleSw_LSXM1TGS48QGHA0,
       "hh3cevtModuleSw-LSXM1TGS48QGHA1": hh3cevtModuleSw_LSXM1TGS48QGHA1,
       "hh3cevtModuleSw-LSXM1CGC2A0": hh3cevtModuleSw_LSXM1CGC2A0,
       "hh3cevtModuleSw-LSXM1CGC2A1": hh3cevtModuleSw_LSXM1CGC2A1,
       "hh3cevtModuleSw-LSQM2FWDSC0": hh3cevtModuleSw_LSQM2FWDSC0,
       "hh3cevtModuleSw-LSQM1XPT12TSFD0": hh3cevtModuleSw_LSQM1XPT12TSFD0,
       "hh3cevtModuleSw-LSXM1QGS24HB0": hh3cevtModuleSw_LSXM1QGS24HB0,
       "hh3cevtModuleSw-LSXM1QGS24HB1": hh3cevtModuleSw_LSXM1QGS24HB1,
       "hh3cevtModuleSw-LSXM1QGS24HC0": hh3cevtModuleSw_LSXM1QGS24HC0,
       "hh3cevtModuleSw-LSXM1SUP01B1": hh3cevtModuleSw_LSXM1SUP01B1,
       "hh3cevtModuleSw-LSCM1SUP03A0": hh3cevtModuleSw_LSCM1SUP03A0,
       "hh3cevtModuleSw-LSCM1SUP03A0-Z": hh3cevtModuleSw_LSCM1SUP03A0_Z,
       "hh3cevtModuleSw-LSCM1MPUS06A0": hh3cevtModuleSw_LSCM1MPUS06A0,
       "hh3cevtModuleSw-LSCM1MPUS06A0-Z": hh3cevtModuleSw_LSCM1MPUS06A0_Z,
       "hh3cevtModuleSw-LSCM1GT48SC0": hh3cevtModuleSw_LSCM1GT48SC0,
       "hh3cevtModuleSw-LSCM1GT48SC0-Z": hh3cevtModuleSw_LSCM1GT48SC0_Z,
       "hh3cevtModuleSw-LSCM1TGS48SE0": hh3cevtModuleSw_LSCM1TGS48SE0,
       "hh3cevtModuleSw-LSCM1TGS48SE0-Z": hh3cevtModuleSw_LSCM1TGS48SE0_Z,
       "hh3cevtModuleSw-LSCM1QGS8CSSE0": hh3cevtModuleSw_LSCM1QGS8CSSE0,
       "hh3cevtModuleSw-LSCM1QGS8CSSE0-Z": hh3cevtModuleSw_LSCM1QGS8CSSE0_Z,
       "hh3cevtModuleSw-LSWM2SP4P": hh3cevtModuleSw_LSWM2SP4P,
       "hh3cevtModuleSw-LSWM2SP4P-Z": hh3cevtModuleSw_LSWM2SP4P_Z,
       "hh3cevtModuleSw-LSQM1MPUS10B0": hh3cevtModuleSw_LSQM1MPUS10B0,
       "hh3cevtModuleSw-LSQM1MPUS10B3": hh3cevtModuleSw_LSQM1MPUS10B3,
       "hh3cevtModuleSw-LSQM1MPUSC0": hh3cevtModuleSw_LSQM1MPUSC0,
       "hh3cevtModuleSw-LSQM1MPUSC3": hh3cevtModuleSw_LSQM1MPUSC3,
       "hh3cevtModuleSw-LSQM2GP24TSSC8": hh3cevtModuleSw_LSQM2GP24TSSC8,
       "hh3cevtModuleSw-LSQM2GT24TSSC8": hh3cevtModuleSw_LSQM2GT24TSSC8,
       "hh3cevtModuleSw-LSXM1TGS24CGMODHD0": hh3cevtModuleSw_LSXM1TGS24CGMODHD0,
       "hh3cevtModuleSw-LSXM1TGS24CGMODHD1": hh3cevtModuleSw_LSXM1TGS24CGMODHD1,
       "hh3cevtModuleSw-LSQM1TGS16GPSA0": hh3cevtModuleSw_LSQM1TGS16GPSA0,
       "hh3cevtModuleSw-EWPXM2TGS48SG0": hh3cevtModuleSw_EWPXM2TGS48SG0,
       "hh3cevtModuleSw-EWPXM1TGS16FD0": hh3cevtModuleSw_EWPXM1TGS16FD0,
       "hh3cevtModuleSw-LSXM1CGQ36HF0": hh3cevtModuleSw_LSXM1CGQ36HF0,
       "hh3cevtModuleSw-LSXM2SUPT0": hh3cevtModuleSw_LSXM2SUPT0,
       "hh3cevtModuleSw-LSXM2SUPT1": hh3cevtModuleSw_LSXM2SUPT1,
       "hh3cevtModuleSw-LSXM1SFT16E0": hh3cevtModuleSw_LSXM1SFT16E0,
       "hh3cevtModuleSw-LSXM1SFT16E1": hh3cevtModuleSw_LSXM1SFT16E1,
       "hh3cevtModuleSw-lsxM1CGQ36TD0": hh3cevtModuleSw_lsxM1CGQ36TD0,
       "hh3cevtModuleSw-lsxM1CGQ36TD1": hh3cevtModuleSw_lsxM1CGQ36TD1,
       "hh3cevtModuleSw-LSQM1TGT24FD0": hh3cevtModuleSw_LSQM1TGT24FD0,
       "hh3cevtModuleSw-LSUM1TGT24FD0": hh3cevtModuleSw_LSUM1TGT24FD0,
       "hh3cevtModuleSw-LSXM2SFT08E0": hh3cevtModuleSw_LSXM2SFT08E0,
       "hh3cevtModuleSw-LSXM2SFT08E1": hh3cevtModuleSw_LSXM2SFT08E1,
       "hh3cevtModuleSw-LSXM1CCP8HF0": hh3cevtModuleSw_LSXM1CCP8HF0,
       "hh3cevtModuleSw-LSXM1CCP8HF1": hh3cevtModuleSw_LSXM1CCP8HF1,
       "hh3cevtModuleSw-S8610-MPU": hh3cevtModuleSw_S8610_MPU,
       "hh3cevtModuleSw-S8610-NET": hh3cevtModuleSw_S8610_NET,
       "hh3cevtModuleSw-S86-44GF4XFSE": hh3cevtModuleSw_S86_44GF4XFSE,
       "hh3cevtModuleSw-S86-48GTSE": hh3cevtModuleSw_S86_48GTSE,
       "hh3cevtModuleSw-S86-12QFSG": hh3cevtModuleSw_S86_12QFSG,
       "hh3cevtModuleSw-S86-48XFSG": hh3cevtModuleSw_S86_48XFSG,
       "hh3cevtModuleSw-LSUM1MPUS06XEC0": hh3cevtModuleSw_LSUM1MPUS06XEC0,
       "hh3cevtModuleSw-LSUM1MPUS10XE0": hh3cevtModuleSw_LSUM1MPUS10XE0,
       "hh3cevtModuleSw-LSUM1MPUS10XEB0": hh3cevtModuleSw_LSUM1MPUS10XEB0,
       "hh3cevtModuleSw-LSUM1FAB06XEC0": hh3cevtModuleSw_LSUM1FAB06XEC0,
       "hh3cevtModuleSw-LSUM1FAB10XE0": hh3cevtModuleSw_LSUM1FAB10XE0,
       "hh3cevtModuleSw-LSUM1FAB10XEB0": hh3cevtModuleSw_LSUM1FAB10XEB0,
       "hh3cevtModuleSw-LSUM1FAB08XEB0": hh3cevtModuleSw_LSUM1FAB08XEB0,
       "hh3cevtModuleSw-LSUM1TGS48SH0": hh3cevtModuleSw_LSUM1TGS48SH0,
       "hh3cevtModuleSw-LSUM1CGS8SH0": hh3cevtModuleSw_LSUM1CGS8SH0,
       "hh3cevtModuleSw-LSUM1YGS24CSSH0": hh3cevtModuleSw_LSUM1YGS24CSSH0,
       "hh3cevtModuleSw-LSUM1CGS20XSH0": hh3cevtModuleSw_LSUM1CGS20XSH0,
       "hh3cevtModuleSw-LSUM1CGS32XSH0": hh3cevtModuleSw_LSUM1CGS32XSH0,
       "hh3cevtModuleSw-LSUM1CGS8QSSH0": hh3cevtModuleSw_LSUM1CGS8QSSH0,
       "hh3cevtModuleSw-LSUM1YGS48XSH0": hh3cevtModuleSw_LSUM1YGS48XSH0,
       "hh3cevtModuleSw-LSXM3SUPT1": hh3cevtModuleSw_LSXM3SUPT1,
       "hh3cevtModuleSw-LSXM4SUPT1": hh3cevtModuleSw_LSXM4SUPT1,
       "hh3cevtModuleSw-LSQM2GP24TSSA0-Z": hh3cevtModuleSw_LSQM2GP24TSSA0_Z,
       "hh3cevtModuleSw-LSQM2GT48SA0-Z": hh3cevtModuleSw_LSQM2GT48SA0_Z,
       "hh3cevtModuleSw-LSQM2GP48SA0-Z": hh3cevtModuleSw_LSQM2GP48SA0_Z,
       "hh3cevtModuleSw-LSUM2TGS48SG0-Z": hh3cevtModuleSw_LSUM2TGS48SG0_Z,
       "hh3cevtModuleSw-LSUM2QGS12SG0-Z": hh3cevtModuleSw_LSUM2QGS12SG0_Z,
       "hh3cevtModuleSw-LSUM2TGS32QSSG0-Z": hh3cevtModuleSw_LSUM2TGS32QSSG0_Z,
       "hh3cevtModuleSw-LSUM1TGS48RSH0": hh3cevtModuleSw_LSUM1TGS48RSH0,
       "hh3cevtModuleSw-LSUM1MPUS06XEB0": hh3cevtModuleSw_LSUM1MPUS06XEB0,
       "hh3cevtModuleSw-LSUM1MPUS10XEA0": hh3cevtModuleSw_LSUM1MPUS10XEA0,
       "hh3cevtModuleSw-LSUM1FAB06XEB0": hh3cevtModuleSw_LSUM1FAB06XEB0,
       "hh3cevtModuleSw-LSUM1FAB10XEA0": hh3cevtModuleSw_LSUM1FAB10XEA0,
       "hh3cevtModuleSw-EWPXM1WCMX100": hh3cevtModuleSw_EWPXM1WCMX100,
       "hh3cevtModuleSw-LSQM1WBCZ720X": hh3cevtModuleSw_LSQM1WBCZ720X,
       "hh3cevtModuleSw-LSUM1WBCZ720XRT": hh3cevtModuleSw_LSUM1WBCZ720XRT,
       "hh3cevtModuleSw-LSXM1CGQ8TD1": hh3cevtModuleSw_LSXM1CGQ8TD1,
       "hh3cevtModuleSw-LSXM1CGQ12TD1": hh3cevtModuleSw_LSXM1CGQ12TD1,
       "hh3cevtModuleSw-LSXM1CGQ18TD1": hh3cevtModuleSw_LSXM1CGQ18TD1,
       "hh3cevtModuleSw-LSXM1QGS24C6TD1": hh3cevtModuleSw_LSXM1QGS24C6TD1,
       "hh3cevtModuleSw-LSXM1QGS36TD1": hh3cevtModuleSw_LSXM1QGS36TD1,
       "hh3cevtModuleSw-LSXM1QGS48TD1": hh3cevtModuleSw_LSXM1QGS48TD1,
       "hh3cevtModuleSw-LSXM1TGS48C4TD1": hh3cevtModuleSw_LSXM1TGS48C4TD1,
       "hh3cevtModuleSw-LSXM1GP48TD1": hh3cevtModuleSw_LSXM1GP48TD1,
       "hh3cevtModuleSw-LSXM1TGS48TD1": hh3cevtModuleSw_LSXM1TGS48TD1,
       "hh3cevtModuleSw-LSWM124TG2H1": hh3cevtModuleSw_LSWM124TG2H1,
       "hh3cevtModuleSw-LSQM2FWDSC8": hh3cevtModuleSw_LSQM2FWDSC8,
       "hh3cevtModuleSw-IM-MSEX-B": hh3cevtModuleSw_IM_MSEX_B,
       "hh3cevtModuleSw-IM-MSEX-B-IM-SP-B": hh3cevtModuleSw_IM_MSEX_B_IM_SP_B,
       "hh3cevtModuleSw-LSUM1MPUS06XEC0-Z": hh3cevtModuleSw_LSUM1MPUS06XEC0_Z,
       "hh3cevtModuleSw-LSUM1CGS8SH0-Z": hh3cevtModuleSw_LSUM1CGS8SH0_Z,
       "hh3cevtModuleSw-LSUM1SUPXD0-Z": hh3cevtModuleSw_LSUM1SUPXD0_Z,
       "hh3cevtModuleSw-LSUM1FAB08XE0-Z": hh3cevtModuleSw_LSUM1FAB08XE0_Z,
       "hh3cevtModuleSw-LSUM1CGS20XSH0-Z": hh3cevtModuleSw_LSUM1CGS20XSH0_Z,
       "hh3cevtModuleSw-LSUM1FAB06XEC0-Z": hh3cevtModuleSw_LSUM1FAB06XEC0_Z,
       "hh3cevtModuleSw-LSUM1CQGS32SF0-Z": hh3cevtModuleSw_LSUM1CQGS32SF0_Z,
       "hh3cevtModuleSw-LSXM1FAB10XE3": hh3cevtModuleSw_LSXM1FAB10XE3,
       "hh3cevtModuleSw-LSXM1FAB08XE3": hh3cevtModuleSw_LSXM1FAB08XE3,
       "hh3cevtModuleSw-LSXM1YGS48XSH3": hh3cevtModuleSw_LSXM1YGS48XSH3,
       "hh3cevtModuleSw-LSXM1YGS24CSSH3": hh3cevtModuleSw_LSXM1YGS24CSSH3,
       "hh3cevtModuleSw-LSXM1CGS8QSSH3": hh3cevtModuleSw_LSXM1CGS8QSSH3,
       "hh3cevtModuleSw-LSXM1TGS48SH3": hh3cevtModuleSw_LSXM1TGS48SH3,
       "hh3cevtModuleSw-LSXM1MPUS10XE3": hh3cevtModuleSw_LSXM1MPUS10XE3,
       "hh3cevtModuleSw-LSXM1FAB06XEC3": hh3cevtModuleSw_LSXM1FAB06XEC3,
       "hh3cevtModuleSw-LSXM1MPUS06XEC3": hh3cevtModuleSw_LSXM1MPUS06XEC3,
       "hh3cevtModuleSw-LSXM1CGS8SH3": hh3cevtModuleSw_LSXM1CGS8SH3,
       "hh3cevtModuleSw-LSXM1SUPXD3": hh3cevtModuleSw_LSXM1SUPXD3,
       "hh3cevtModuleSw-LSXM1CGS20XSH3": hh3cevtModuleSw_LSXM1CGS20XSH3,
       "hh3cevtModuleSw-LSUM1GP48FD0-Z": hh3cevtModuleSw_LSUM1GP48FD0_Z,
       "hh3cevtModuleSw-LSQM1TGS48RFE0-Z": hh3cevtModuleSw_LSQM1TGS48RFE0_Z,
       "hh3cevtModuleSw-LSXM1CGS32XSH3": hh3cevtModuleSw_LSXM1CGS32XSH3,
       "hh3cevtModuleSw-LSQM2GP40TS8FD0": hh3cevtModuleSw_LSQM2GP40TS8FD0,
       "hh3cevtModuleSw-LSUM1SUPXES0": hh3cevtModuleSw_LSUM1SUPXES0,
       "hh3cevtModuleSw-LSQM2SUPB0": hh3cevtModuleSw_LSQM2SUPB0,
       "hh3cevtModuleSw-LSUM2GP40TS8FD0": hh3cevtModuleSw_LSUM2GP40TS8FD0,
       "hh3cevtModuleSw-LSXM1YGS48XXSH3": hh3cevtModuleSw_LSXM1YGS48XXSH3,
       "hh3cevtModuleSw-LSXM2SFT08E2": hh3cevtModuleSw_LSXM2SFT08E2,
       "hh3cevtModuleSw-LSXM1TGS48TD2": hh3cevtModuleSw_LSXM1TGS48TD2,
       "hh3cevtModuleSw-LSXM1CGQ36TD2": hh3cevtModuleSw_LSXM1CGQ36TD2,
       "hh3cevtModuleSw-RX-NIC-LGQ4L": hh3cevtModuleSw_RX_NIC_LGQ4L,
       "hh3cevtModuleSw-LSXM1CDQ24KB1": hh3cevtModuleSw_LSXM1CDQ24KB1,
       "hh3cevtModuleSw-LSXM1SUP02L1": hh3cevtModuleSw_LSXM1SUP02L1,
       "hh3cevtModuleSw-LSXM1CGQ48KB1": hh3cevtModuleSw_LSXM1CGQ48KB1,
       "hh3cevtModuleSw-LSXM1SFK08F1": hh3cevtModuleSw_LSXM1SFK08F1,
       "hh3cevtModuleSw-CSPEX-1214X": hh3cevtModuleSw_CSPEX_1214X,
       "hh3cevtModuleSw-MIC-CQ1L1": hh3cevtModuleSw_MIC_CQ1L1,
       "hh3cevtModuleSw-DS-3E7600-16X-SCB": hh3cevtModuleSw_DS_3E7600_16X_SCB,
       "hh3cevtModuleSw-DS-3E12508-MPU": hh3cevtModuleSw_DS_3E12508_MPU,
       "hh3cevtModuleSw-DS-3E12500-7610-48T-SE": hh3cevtModuleSw_DS_3E12500_7610_48T_SE,
       "hh3cevtModuleSw-DS-3E7603-MPU": hh3cevtModuleSw_DS_3E7603_MPU,
       "hh3cevtModuleSw-DS-3E12500-7610-16X-SF": hh3cevtModuleSw_DS_3E12500_7610_16X_SF,
       "hh3cevtModuleSw-DS-3E12500-24T20F4X-SE": hh3cevtModuleSw_DS_3E12500_24T20F4X_SE,
       "hh3cevtModuleSw-DS-3E12500-12Q-SG": hh3cevtModuleSw_DS_3E12500_12Q_SG,
       "hh3cevtModuleSw-DS-3E12500-48X-SG": hh3cevtModuleSw_DS_3E12500_48X_SG,
       "hh3cevtModuleSw-DS-3E12500-7610-32X4QX-SF": hh3cevtModuleSw_DS_3E12500_7610_32X4QX_SF,
       "hh3cevtModuleSw-DS-3E12500-7610-44F4X-SE": hh3cevtModuleSw_DS_3E12500_7610_44F4X_SE,
       "hh3cevtModuleSw-DS-3E12508-CLOS": hh3cevtModuleSw_DS_3E12508_CLOS,
       "hh3cevtModuleSw-LSXM2SUPT2": hh3cevtModuleSw_LSXM2SUPT2,
       "hh3cevtModuleSw-CSR05SRP1P3A": hh3cevtModuleSw_CSR05SRP1P3A,
       "hh3cevtModuleSw-CSFC-08E1A": hh3cevtModuleSw_CSFC_08E1A,
       "hh3cevtModuleSw-CSFC-16EA": hh3cevtModuleSw_CSFC_16EA,
       "hh3cevtModuleSw-CSPEX-1602XA": hh3cevtModuleSw_CSPEX_1602XA,
       "hh3cevtModuleSw-CEPC-CP4RXA": hh3cevtModuleSw_CEPC_CP4RXA,
       "hh3cevtModuleSw-CSPEX-1504XA": hh3cevtModuleSw_CSPEX_1504XA,
       "hh3cevtModuleSw-CSPEX-1804XA": hh3cevtModuleSw_CSPEX_1804XA,
       "hh3cevtModuleSw-MIC-GP10LA": hh3cevtModuleSw_MIC_GP10LA,
       "hh3cevtModuleSw-MIC-GT20LA": hh3cevtModuleSw_MIC_GT20LA,
       "hh3cevtModuleSw-MIC-XP20LA": hh3cevtModuleSw_MIC_XP20LA,
       "hh3cevtModuleSw-LSDM1QGS12SE0-Z": hh3cevtModuleSw_LSDM1QGS12SE0_Z,
       "hh3cevtModuleSw-LSDM1TGS48SE0-Z": hh3cevtModuleSw_LSDM1TGS48SE0_Z,
       "hh3cevtModuleSw-LSDM1SUPA0-Z": hh3cevtModuleSw_LSDM1SUPA0_Z,
       "hh3cevtModuleSw-LSDM1FAB08D0-Z": hh3cevtModuleSw_LSDM1FAB08D0_Z,
       "hh3cevtModuleSw-LSDM1GT24GPSE0-Z": hh3cevtModuleSw_LSDM1GT24GPSE0_Z,
       "hh3cevtModuleSw-LSXM1CGQ18TD2": hh3cevtModuleSw_LSXM1CGQ18TD2,
       "hh3cevtModuleSw-LSXM1QGS36TD2": hh3cevtModuleSw_LSXM1QGS36TD2,
       "hh3cevtModuleSw-RP-S-G": hh3cevtModuleSw_RP_S_G,
       "hh3cevtModuleSw-MOD20-G": hh3cevtModuleSw_MOD20_G,
       "hh3cevtModuleSw-MPA-PSP4L-G": hh3cevtModuleSw_MPA_PSP4L_G,
       "hh3cevtModuleSw-MPA-TCP8L-G": hh3cevtModuleSw_MPA_TCP8L_G,
       "hh3cevtModuleSw-MPA-ET16L-G": hh3cevtModuleSw_MPA_ET16L_G,
       "hh3cevtModuleSw-MPA-GP10L-G": hh3cevtModuleSw_MPA_GP10L_G,
       "hh3cevtModuleSw-MPA-XP4L-G": hh3cevtModuleSw_MPA_XP4L_G,
       "hh3cevtModuleSw-LSXM1SFH04DR1": hh3cevtModuleSw_LSXM1SFH04DR1,
       "hh3cevtModuleSw-LSXM1SFH08CR1": hh3cevtModuleSw_LSXM1SFH08CR1,
       "hh3cevtModuleSw-LSXM1SFH08DR1": hh3cevtModuleSw_LSXM1SFH08DR1,
       "hh3cevtModuleSw-LSXM1SFH16CR1": hh3cevtModuleSw_LSXM1SFH16CR1,
       "hh3cevtModuleSw-LSXM1SFH16ER1": hh3cevtModuleSw_LSXM1SFH16ER1,
       "hh3cevtModuleSw-LSXM1TGS48HFR1": hh3cevtModuleSw_LSXM1TGS48HFR1,
       "hh3cevtModuleSw-LSXM1CGQ18QGHFR1": hh3cevtModuleSw_LSXM1CGQ18QGHFR1,
       "hh3cevtModuleSw-LSXM1SUP04TR1": hh3cevtModuleSw_LSXM1SUP04TR1,
       "hh3cevtModuleSw-LSXM1CGQ36HBR1": hh3cevtModuleSw_LSXM1CGQ36HBR1,
       "hh3cevtModuleSw-LSXM1CGQ36HFR1": hh3cevtModuleSw_LSXM1CGQ36HFR1,
       "hh3cevtModuleSw-LSXM1CGQ6QGHFR1": hh3cevtModuleSw_LSXM1CGQ6QGHFR1,
       "hh3cevtModuleSw-LSXM1TGS48HBR1": hh3cevtModuleSw_LSXM1TGS48HBR1,
       "hh3cevtModuleSw-LSXM1CGQ18QGHBR1": hh3cevtModuleSw_LSXM1CGQ18QGHBR1,
       "hh3cevtModuleSw-LSXM1SUPER1": hh3cevtModuleSw_LSXM1SUPER1,
       "hh3cevtModuleSw-LSQM1SDNB0": hh3cevtModuleSw_LSQM1SDNB0,
       "hh3cevtModuleSw-LSUM1SDNB0": hh3cevtModuleSw_LSUM1SDNB0,
       "hh3cevtModuleSw-LSQM1EPSB0": hh3cevtModuleSw_LSQM1EPSB0,
       "hh3cevtModuleSw-LSUM1EPSB0": hh3cevtModuleSw_LSUM1EPSB0,
       "hh3cevtModuleSw-LSXM2TGS48HB2": hh3cevtModuleSw_LSXM2TGS48HB2,
       "hh3cevtModuleSw-LSXM2CGQ18QGHB2": hh3cevtModuleSw_LSXM2CGQ18QGHB2,
       "hh3cevtModuleSw-LSUM1CGS8SH3": hh3cevtModuleSw_LSUM1CGS8SH3,
       "hh3cevtModuleSw-LSUM1GT48FC3": hh3cevtModuleSw_LSUM1GT48FC3,
       "hh3cevtModuleSw-LSUM1FAB10XEA3": hh3cevtModuleSw_LSUM1FAB10XEA3,
       "hh3cevtModuleSw-LSUM1TGS48SH3": hh3cevtModuleSw_LSUM1TGS48SH3,
       "hh3cevtModuleSw-LSUM1MPUS10XE3": hh3cevtModuleSw_LSUM1MPUS10XE3,
       "hh3cevtModuleSw-LSUM1GP48FC3": hh3cevtModuleSw_LSUM1GP48FC3,
       "hh3cevtModuleSw-LSQM1TGS16FD0-Z": hh3cevtModuleSw_LSQM1TGS16FD0_Z,
       "hh3cevtModuleSw-LSQM2SUPA0-Z": hh3cevtModuleSw_LSQM2SUPA0_Z,
       "hh3cevtModuleSw-LSUM1TGS16FD0-Z": hh3cevtModuleSw_LSUM1TGS16FD0_Z,
       "hh3cevtModuleSw-LSWM2FPGAB": hh3cevtModuleSw_LSWM2FPGAB,
       "hh3cevtModuleSw-LSWM2EC": hh3cevtModuleSw_LSWM2EC,
       "hh3cevtModuleSw-LSWM2FPGA": hh3cevtModuleSw_LSWM2FPGA,
       "hh3cevtModuleSw-LSWM2ZSP4P": hh3cevtModuleSw_LSWM2ZSP4P,
       "hh3cevtModuleSw-LSXM1CGQ8TD2": hh3cevtModuleSw_LSXM1CGQ8TD2,
       "hh3cevtModuleSw-LSXM1TGS48C4TD2": hh3cevtModuleSw_LSXM1TGS48C4TD2,
       "hh3cevtModuleSw-LSXM1QGS24C6TD2": hh3cevtModuleSw_LSXM1QGS24C6TD2,
       "hh3cevtModuleSw-LSCM1MPUS06A8": hh3cevtModuleSw_LSCM1MPUS06A8,
       "hh3cevtModuleSw-LSCM1TGS48SC8": hh3cevtModuleSw_LSCM1TGS48SC8,
       "hh3cevtModuleSw-LSQM1MPUS06S0": hh3cevtModuleSw_LSQM1MPUS06S0,
       "hh3cevtModuleSw-LSQM1SRP4Y06A0": hh3cevtModuleSw_LSQM1SRP4Y06A0,
       "hh3cevtModuleSw-S76-16XFSF-E": hh3cevtModuleSw_S76_16XFSF_E,
       "hh3cevtModuleSw-S7603-MPU": hh3cevtModuleSw_S7603_MPU,
       "hh3cevtModuleSw-LSCM2MPUS06AS8": hh3cevtModuleSw_LSCM2MPUS06AS8,
       "hh3cevtModuleSw-LSCM2CGT24TSSC8": hh3cevtModuleSw_LSCM2CGT24TSSC8,
       "hh3cevtModuleSw-LSCM2CGP24TSSC8": hh3cevtModuleSw_LSCM2CGP24TSSC8,
       "hh3cevtModuleSw-LSCM2CTGS12GTSC8": hh3cevtModuleSw_LSCM2CTGS12GTSC8,
       "hh3cevtModuleSw-LSCM2CTGS12GPSC8": hh3cevtModuleSw_LSCM2CTGS12GPSC8,
       "hh3cevtModuleSw-LSCM2GT24GPTSSC8": hh3cevtModuleSw_LSCM2GT24GPTSSC8,
       "hh3cevtModuleSw-LSCM2GT24GPSC8": hh3cevtModuleSw_LSCM2GT24GPSC8,
       "hh3cevtModuleSw-LSCM2GP24GTSC8": hh3cevtModuleSw_LSCM2GP24GTSC8,
       "hh3cevtModuleSw-LSCM2GT48SC8": hh3cevtModuleSw_LSCM2GT48SC8,
       "hh3cevtModuleSw-LSCM2GP48SC8": hh3cevtModuleSw_LSCM2GP48SC8,
       "hh3cevtModuleSw-LSCM2TGS16GPSC8": hh3cevtModuleSw_LSCM2TGS16GPSC8,
       "hh3cevtModuleSw-LSXM2SFH16CR1": hh3cevtModuleSw_LSXM2SFH16CR1,
       "hh3cevtModuleSw-LSXM1SEERBXC2": hh3cevtModuleSw_LSXM1SEERBXC2,
       "hh3cevtModuleSw-LSXM1SEERBG2": hh3cevtModuleSw_LSXM1SEERBG2,
       "hh3cevtModuleSw-LSXM1SEERBXD2": hh3cevtModuleSw_LSXM1SEERBXD2,
       "hh3cevtModuleSw-LSXM1SFK08FR1": hh3cevtModuleSw_LSXM1SFK08FR1,
       "hh3cevtModuleSw-LSXM1CDQ24KBR1": hh3cevtModuleSw_LSXM1CDQ24KBR1,
       "hh3cevtModuleSw-LSXM1SUP02LR1": hh3cevtModuleSw_LSXM1SUP02LR1,
       "hh3cevtModuleSw-LSXM1CGQ48KBR1": hh3cevtModuleSw_LSXM1CGQ48KBR1,
       "hh3cevtModuleSw-LSXM1CGQ36HC0": hh3cevtModuleSw_LSXM1CGQ36HC0,
       "hh3cevtModuleSw-LSXM1TGS48TE2": hh3cevtModuleSw_LSXM1TGS48TE2,
       "hh3cevtModuleSw-LSXM1CGQ36TE2": hh3cevtModuleSw_LSXM1CGQ36TE2,
       "hh3cevtModuleSw-LSXM1SFT16F1": hh3cevtModuleSw_LSXM1SFT16F1,
       "hh3cevtModuleSw-LSXM1CGQ18TE2": hh3cevtModuleSw_LSXM1CGQ18TE2,
       "hh3cevtModuleSw-LSXM1CGQ8TE2": hh3cevtModuleSw_LSXM1CGQ8TE2,
       "hh3cevtModuleSw-LSWM116H": hh3cevtModuleSw_LSWM116H,
       "hh3cevtModuleSw-LSWM1M4CD": hh3cevtModuleSw_LSWM1M4CD,
       "hh3cevtModuleSw-LSXM1QGS36TE2": hh3cevtModuleSw_LSXM1QGS36TE2,
       "hh3cevtModuleSw-LSXM1SFT16F2": hh3cevtModuleSw_LSXM1SFT16F2,
       "hh3cevtModuleSw-CSPEX-1812X-E": hh3cevtModuleSw_CSPEX_1812X_E,
       "hh3cevtModuleSw-MOD20-A3": hh3cevtModuleSw_MOD20_A3,
       "hh3cevtModuleSw-RP-S-G-A3": hh3cevtModuleSw_RP_S_G_A3,
       "hh3cevtModuleSw-LSXM1SFT16EA1": hh3cevtModuleSw_LSXM1SFT16EA1,
       "hh3cevtModuleSw-RP1-S-G": hh3cevtModuleSw_RP1_S_G,
       "hh3cevtModuleSw-MOD21-G": hh3cevtModuleSw_MOD21_G,
       "hh3cevtModuleSw-LSXM1SUPKR1": hh3cevtModuleSw_LSXM1SUPKR1,
       "hh3cevtModuleSw-LSXM1CDQ36KBR1": hh3cevtModuleSw_LSXM1CDQ36KBR1,
       "hh3cevtModuleSw-LSXM1CMUR1": hh3cevtModuleSw_LSXM1CMUR1,
       "hh3cevtModuleSw-LSXM1SFK16GR1": hh3cevtModuleSw_LSXM1SFK16GR1,
       "hh3cevtModuleSw-CSR05SRP1R3": hh3cevtModuleSw_CSR05SRP1R3,
       "hh3cevtModuleSw-MIC-TCP8L": hh3cevtModuleSw_MIC_TCP8L,
       "hh3cevtModuleSw-MIC-PSP4L": hh3cevtModuleSw_MIC_PSP4L,
       "hh3cevtModuleSw-LSUM1MPU06B8": hh3cevtModuleSw_LSUM1MPU06B8,
       "hh3cevtModuleSw-LSUM1MPU10C8": hh3cevtModuleSw_LSUM1MPU10C8,
       "hh3cevtModuleSw-LSUM1FAB06C8": hh3cevtModuleSw_LSUM1FAB06C8,
       "hh3cevtModuleSw-LSUM1FAB10C8": hh3cevtModuleSw_LSUM1FAB10C8,
       "hh3cevtModuleSw-LSUM1MPU10A8": hh3cevtModuleSw_LSUM1MPU10A8,
       "hh3cevtModuleSw-LSUM1FAB10A8": hh3cevtModuleSw_LSUM1FAB10A8,
       "hh3cevtModuleSw-LSUM1TGS16FD8": hh3cevtModuleSw_LSUM1TGS16FD8,
       "hh3cevtModuleSw-LSUM1GP48FD8": hh3cevtModuleSw_LSUM1GP48FD8,
       "hh3cevtModuleSw-LSUM1GT48FD8": hh3cevtModuleSw_LSUM1GT48FD8,
       "hh3cevtModuleSw-LSUM1GP40TS8FD8": hh3cevtModuleSw_LSUM1GP40TS8FD8,
       "hh3cevtModuleSw-LSUM1TGS48RSH8": hh3cevtModuleSw_LSUM1TGS48RSH8,
       "hh3cevtModuleSw-LSDM1GP48SE0-Z": hh3cevtModuleSw_LSDM1GP48SE0_Z,
       "hh3cevtModuleSw-LSDM1GT48SE0-Z": hh3cevtModuleSw_LSDM1GT48SE0_Z,
       "hh3cevtModuleSw-LSDM1CGS8SE0-Z": hh3cevtModuleSw_LSDM1CGS8SE0_Z,
       "hh3cevtModuleSw-LSXM1SUP04T2": hh3cevtModuleSw_LSXM1SUP04T2,
       "hh3cevtModuleSw-LSXM1SFT04F2": hh3cevtModuleSw_LSXM1SFT04F2,
       "hh3cevtModuleSw-LSXM1SFT08F2": hh3cevtModuleSw_LSXM1SFT08F2,
       "hh3cevtModuleSw-RX-NIC-CQ2LF-E": hh3cevtModuleSw_RX_NIC_CQ2LF_E,
       "hh3cevtModuleSw-LSUM1TGS24FD8": hh3cevtModuleSw_LSUM1TGS24FD8,
       "hh3cevtModuleSw-RX-SPE400-E": hh3cevtModuleSw_RX_SPE400_E,
       "hh3cevtModuleSw-LSXM1SFK08GR1": hh3cevtModuleSw_LSXM1SFK08GR1,
       "hh3cevtModuleSw-RX-SFC-16T1": hh3cevtModuleSw_RX_SFC_16T1,
       "hh3cevtModuleSw-LSCM3SUP03A0-Z": hh3cevtModuleSw_LSCM3SUP03A0_Z,
       "hh3cevtModuleSw-LSCM3MPUS06A0-Z": hh3cevtModuleSw_LSCM3MPUS06A0_Z,
       "hh3cevtModuleSw-LSCM3GT48SC0-Z": hh3cevtModuleSw_LSCM3GT48SC0_Z,
       "hh3cevtModuleSw-LSCM3TGS48SE0-Z": hh3cevtModuleSw_LSCM3TGS48SE0_Z,
       "hh3cevtModuleSw-LSCM3QGS8CSSE0-Z": hh3cevtModuleSw_LSCM3QGS8CSSE0_Z,
       "hh3cevtModuleSw-LSDM3QGS12SE0-Z": hh3cevtModuleSw_LSDM3QGS12SE0_Z,
       "hh3cevtModuleSw-LSDM3TGS48SE0-Z": hh3cevtModuleSw_LSDM3TGS48SE0_Z,
       "hh3cevtModuleSw-LSDM3SUPA0-Z": hh3cevtModuleSw_LSDM3SUPA0_Z,
       "hh3cevtModuleSw-LSDM3FAB08D0-Z": hh3cevtModuleSw_LSDM3FAB08D0_Z,
       "hh3cevtModuleSw-LSDM3GT24GPSE0-Z": hh3cevtModuleSw_LSDM3GT24GPSE0_Z,
       "hh3cevtModuleSw-LSDM3GP48SE0-Z": hh3cevtModuleSw_LSDM3GP48SE0_Z,
       "hh3cevtModuleSw-LSDM3GT48SE0-Z": hh3cevtModuleSw_LSDM3GT48SE0_Z,
       "hh3cevtModuleSw-LSDM3CGS8SE0-Z": hh3cevtModuleSw_LSDM3CGS8SE0_Z,
       "hh3cevtModuleSw-RX-CEPC-CQ8LF": hh3cevtModuleSw_RX_CEPC_CQ8LF,
       "hh3cevtModuleSw-RX-SPE200-E": hh3cevtModuleSw_RX_SPE200_E,
       "hh3cevtModuleSw-DSH7503-MP": hh3cevtModuleSw_DSH7503_MP,
       "hh3cevtModuleSw-DSH7506-MP": hh3cevtModuleSw_DSH7506_MP,
       "hh3cevtModuleSw-DSH7510-MP": hh3cevtModuleSw_DSH7510_MP,
       "hh3cevtModuleSw-DSH7500-48T-P": hh3cevtModuleSw_DSH7500_48T_P,
       "hh3cevtModuleSw-DSH7500-16X": hh3cevtModuleSw_DSH7500_16X,
       "hh3cevtModuleSw-DSH7500-48F": hh3cevtModuleSw_DSH7500_48F,
       "hh3cevtModuleSw-DSH7500-12QX4Q28": hh3cevtModuleSw_DSH7500_12QX4Q28,
       "hh3cevtModuleSw-DSH7500-24F4X": hh3cevtModuleSw_DSH7500_24F4X,
       "hh3cevtModuleSw-DSH7500-24QX": hh3cevtModuleSw_DSH7500_24QX,
       "hh3cevtModuleSw-DSH7500-24T4X": hh3cevtModuleSw_DSH7500_24T4X,
       "hh3cevtModuleSw-DSH7500-24X2QX1Q28": hh3cevtModuleSw_DSH7500_24X2QX1Q28,
       "hh3cevtModuleSw-DSH7500-2Q28": hh3cevtModuleSw_DSH7500_2Q28,
       "hh3cevtModuleSw-DSH7500-44F4X": hh3cevtModuleSw_DSH7500_44F4X,
       "hh3cevtModuleSw-DSH7500-48T": hh3cevtModuleSw_DSH7500_48T,
       "hh3cevtModuleSw-DSH7500-48X": hh3cevtModuleSw_DSH7500_48X,
       "hh3cevtModuleSw-LSWM2-iMC": hh3cevtModuleSw_LSWM2_iMC,
       "hh3cevtModuleSw-LSWM2ZQP2P-Z": hh3cevtModuleSw_LSWM2ZQP2P_Z,
       "hh3cevtModuleSw-LSWM2ZSP4P-Z": hh3cevtModuleSw_LSWM2ZSP4P_Z,
       "hh3cevtModuleSw-LSWM2ZSP8P-Z": hh3cevtModuleSw_LSWM2ZSP8P_Z,
       "hh3cevtModuleSw-LSDM3SUP04A0-Z": hh3cevtModuleSw_LSDM3SUP04A0_Z,
       "hh3cevtModuleSw-LSDM3FAB04E0-Z": hh3cevtModuleSw_LSDM3FAB04E0_Z,
       "hh3cevtModuleSw-LSDM3FAB08E0-Z": hh3cevtModuleSw_LSDM3FAB08E0_Z,
       "hh3cevtModuleSw-LSDM3QGS36SE0-Z": hh3cevtModuleSw_LSDM3QGS36SE0_Z,
       "hh3cevtModuleSw-LSDM3CGS12SE0-Z": hh3cevtModuleSw_LSDM3CGS12SE0_Z,
       "hh3cevtModuleSw-LSQM2XPT12TSFD0": hh3cevtModuleSw_LSQM2XPT12TSFD0,
       "hh3cevtModuleSw-CSPEX-1702X": hh3cevtModuleSw_CSPEX_1702X,
       "hh3cevtModuleSw-CSR05SRP1P1": hh3cevtModuleSw_CSR05SRP1P1,
       "hh3cevtModuleSw-NIC-GP24L1": hh3cevtModuleSw_NIC_GP24L1,
       "hh3cevtModuleSw-NIC-GP24LA": hh3cevtModuleSw_NIC_GP24LA,
       "hh3cevtModuleSw-NIC-XP20L1": hh3cevtModuleSw_NIC_XP20L1,
       "hh3cevtModuleSw-NIC-XP20LA": hh3cevtModuleSw_NIC_XP20LA,
       "hh3cevtModuleSw-RX-NIC-LGQ4LF": hh3cevtModuleSw_RX_NIC_LGQ4LF,
       "hh3cevtModuleSw-CSR05SRP1R3A": hh3cevtModuleSw_CSR05SRP1R3A,
       "hh3cevtModuleSw-CEPC-CQ8L": hh3cevtModuleSw_CEPC_CQ8L,
       "hh3cevtModuleSw-CEPC-CQ8LA": hh3cevtModuleSw_CEPC_CQ8LA,
       "hh3cevtModuleSw-CSPEX-1802XA": hh3cevtModuleSw_CSPEX_1802XA,
       "hh3cevtModuleSw-CSPEX-1802XB": hh3cevtModuleSw_CSPEX_1802XB,
       "hh3cevtModuleSw-CSPEX-1502XA": hh3cevtModuleSw_CSPEX_1502XA,
       "hh3cevtModuleSw-CSPEX-1512XB": hh3cevtModuleSw_CSPEX_1512XB,
       "hh3cevtModuleSw-NIC-XP20L1A": hh3cevtModuleSw_NIC_XP20L1A,
       "hh3cevtModuleSw-NIC-XP20L1B": hh3cevtModuleSw_NIC_XP20L1B,
       "hh3cevtModuleSw-NIC-GP24L1A": hh3cevtModuleSw_NIC_GP24L1A,
       "hh3cevtModuleSw-NIC-GP24L1B": hh3cevtModuleSw_NIC_GP24L1B,
       "hh3cevtModuleSw-NIC-CQ2LA": hh3cevtModuleSw_NIC_CQ2LA,
       "hh3cevtModuleSw-NIC-CQ2LB": hh3cevtModuleSw_NIC_CQ2LB,
       "hh3cevtModuleSw-NIC-XP5LA": hh3cevtModuleSw_NIC_XP5LA,
       "hh3cevtModuleSw-NIC-XP5LB": hh3cevtModuleSw_NIC_XP5LB,
       "hh3cevtModuleSw-CSFC-16T1": hh3cevtModuleSw_CSFC_16T1,
       "hh3cevtModuleSw-LSUM1MPUS10XEC0": hh3cevtModuleSw_LSUM1MPUS10XEC0,
       "hh3cevtModuleSw-LSUM1MPUS10XEC3": hh3cevtModuleSw_LSUM1MPUS10XEC3,
       "hh3cevtModuleSw-LSUM1MPUS06XEC3": hh3cevtModuleSw_LSUM1MPUS06XEC3,
       "hh3cevtModuleSw-LSUM1FAB10XEC0": hh3cevtModuleSw_LSUM1FAB10XEC0,
       "hh3cevtModuleSw-LSCM2MPUS06AS0-Z": hh3cevtModuleSw_LSCM2MPUS06AS0_Z,
       "hh3cevtModuleSw-LSCM2CGT24TSSC0-Z": hh3cevtModuleSw_LSCM2CGT24TSSC0_Z,
       "hh3cevtModuleSw-LSCM2CGP24TSSC0-Z": hh3cevtModuleSw_LSCM2CGP24TSSC0_Z,
       "hh3cevtModuleSw-LSCM2CTGS12GTSC0-Z": hh3cevtModuleSw_LSCM2CTGS12GTSC0_Z,
       "hh3cevtModuleSw-LSCM2CTGS12GPSC0-Z": hh3cevtModuleSw_LSCM2CTGS12GPSC0_Z,
       "hh3cevtModuleSw-LSCM2GT24GPTSSC0-Z": hh3cevtModuleSw_LSCM2GT24GPTSSC0_Z,
       "hh3cevtModuleSw-LSCM2GT24GPSC0-Z": hh3cevtModuleSw_LSCM2GT24GPSC0_Z,
       "hh3cevtModuleSw-LSCM2GP24GTSC0-Z": hh3cevtModuleSw_LSCM2GP24GTSC0_Z,
       "hh3cevtModuleSw-LSCM2GT48SC0-Z": hh3cevtModuleSw_LSCM2GT48SC0_Z,
       "hh3cevtModuleSw-LSCM2GP48SC0-Z": hh3cevtModuleSw_LSCM2GP48SC0_Z,
       "hh3cevtModuleSw-LSCM2TGS16GPSC0-Z": hh3cevtModuleSw_LSCM2TGS16GPSC0_Z,
       "hh3cevtModuleSw-LSWM2SP2PM-Z": hh3cevtModuleSw_LSWM2SP2PM_Z,
       "hh3cevtModuleSw-LSWM2QP2P-Z": hh3cevtModuleSw_LSWM2QP2P_Z,
       "hh3cevtModuleSw-LSWM2SP8P-Z": hh3cevtModuleSw_LSWM2SP8P_Z,
       "hh3cevtModuleSw-LSCM2MPUS06AS0": hh3cevtModuleSw_LSCM2MPUS06AS0,
       "hh3cevtModuleSw-LSCM2CGT24TSSC0": hh3cevtModuleSw_LSCM2CGT24TSSC0,
       "hh3cevtModuleSw-LSCM2CGP24TSSC0": hh3cevtModuleSw_LSCM2CGP24TSSC0,
       "hh3cevtModuleSw-LSCM2CTGS12GTSC0": hh3cevtModuleSw_LSCM2CTGS12GTSC0,
       "hh3cevtModuleSw-LSCM2CTGS12GPSC0": hh3cevtModuleSw_LSCM2CTGS12GPSC0,
       "hh3cevtModuleSw-LSCM2GT24GPTSSC0": hh3cevtModuleSw_LSCM2GT24GPTSSC0,
       "hh3cevtModuleSw-LSCM2GT24GPSC0": hh3cevtModuleSw_LSCM2GT24GPSC0,
       "hh3cevtModuleSw-LSCM2GP24GTSC0": hh3cevtModuleSw_LSCM2GP24GTSC0,
       "hh3cevtModuleSw-LSCM2GT48SC0": hh3cevtModuleSw_LSCM2GT48SC0,
       "hh3cevtModuleSw-LSCM2GP48SC0": hh3cevtModuleSw_LSCM2GP48SC0,
       "hh3cevtModuleSw-LSCM2TGS16GPSC0": hh3cevtModuleSw_LSCM2TGS16GPSC0,
       "hh3cevtModuleSw-LSXM1SFK04FR1": hh3cevtModuleSw_LSXM1SFK04FR1,
       "hh3cevtModuleSw-LSXM1SFK08ER1": hh3cevtModuleSw_LSXM1SFK08ER1,
       "hh3cevtModuleSw-LSXM1SFK16ER1": hh3cevtModuleSw_LSXM1SFK16ER1,
       "hh3cevtModuleSw-LSXM1CCQ48KBR1": hh3cevtModuleSw_LSXM1CCQ48KBR1,
       "hh3cevtModuleSw-LSQM3SUPA0": hh3cevtModuleSw_LSQM3SUPA0,
       "hh3cevtModuleSw-LSQM3SUPA3": hh3cevtModuleSw_LSQM3SUPA3,
       "hh3cevtModuleSw-LSXM1YGS24CGMODTE2": hh3cevtModuleSw_LSXM1YGS24CGMODTE2,
       "hh3cevtModuleSw-LSXM1SUPE1": hh3cevtModuleSw_LSXM1SUPE1,
       "hh3cevtModuleSw-LSUM2TGS48SH0": hh3cevtModuleSw_LSUM2TGS48SH0,
       "hh3cevtModuleSw-LSCM3SUP03A0": hh3cevtModuleSw_LSCM3SUP03A0,
       "hh3cevtModuleSw-LSCM3MPUS06A0": hh3cevtModuleSw_LSCM3MPUS06A0,
       "hh3cevtModuleSw-LSCM3TGS48SE0": hh3cevtModuleSw_LSCM3TGS48SE0,
       "hh3cevtModuleSw-LSCM3QGS8CSSE0": hh3cevtModuleSw_LSCM3QGS8CSSE0,
       "hh3cevtModuleSw-LSCM3SUP03A0-ZE": hh3cevtModuleSw_LSCM3SUP03A0_ZE,
       "hh3cevtModuleSw-LSCM3GT48SC0-ZE": hh3cevtModuleSw_LSCM3GT48SC0_ZE,
       "hh3cevtModuleSw-LSCM3TGS48SE0-ZE": hh3cevtModuleSw_LSCM3TGS48SE0_ZE,
       "hh3cevtModuleSw-LSCM3QGS8CSSE0-ZE": hh3cevtModuleSw_LSCM3QGS8CSSE0_ZE,
       "hh3cevtModuleSw-LSDM3FAB04G0-Z": hh3cevtModuleSw_LSDM3FAB04G0_Z,
       "hh3cevtModuleSw-LSDM3FAB08G0-Z": hh3cevtModuleSw_LSDM3FAB08G0_Z,
       "hh3cevtModuleSw-LSDM3FAB16G0-Z": hh3cevtModuleSw_LSDM3FAB16G0_Z,
       "hh3cevtModuleSw-LSDM3CGS36SF0-Z": hh3cevtModuleSw_LSDM3CGS36SF0_Z,
       "hh3cevtModuleSw-LSDM3YGS48SF0-Z": hh3cevtModuleSw_LSDM3YGS48SF0_Z,
       "hh3cevtModuleSw-LSCM3MPUS10B0": hh3cevtModuleSw_LSCM3MPUS10B0,
       "hh3cevtModuleSw-LSCM3MPUS10B0-Z": hh3cevtModuleSw_LSCM3MPUS10B0_Z,
       "hh3cevtModuleSw-LSUM1CGS8QSSH8": hh3cevtModuleSw_LSUM1CGS8QSSH8,
       "hh3cevtModuleSw-LSDM3TGS48SF0-Z": hh3cevtModuleSw_LSDM3TGS48SF0_Z,
       "hh3cevtModuleSw-LSDM1SUPA0": hh3cevtModuleSw_LSDM1SUPA0,
       "hh3cevtModuleSw-LSDM1FAB08D0": hh3cevtModuleSw_LSDM1FAB08D0,
       "hh3cevtModuleSw-LSDM1TGS48SE0": hh3cevtModuleSw_LSDM1TGS48SE0,
       "hh3cevtModuleSw-LSDM1GT24GPSE0": hh3cevtModuleSw_LSDM1GT24GPSE0,
       "hh3cevtModuleSw-LSDM1GT48SE0": hh3cevtModuleSw_LSDM1GT48SE0,
       "hh3cevtModuleSw-LSDM1GP48SE0": hh3cevtModuleSw_LSDM1GP48SE0,
       "hh3cevtModuleSw-LSDM3SUPA0": hh3cevtModuleSw_LSDM3SUPA0,
       "hh3cevtModuleSw-LSDM3FAB08D0": hh3cevtModuleSw_LSDM3FAB08D0,
       "hh3cevtModuleSw-LSDM3TGS48SE0": hh3cevtModuleSw_LSDM3TGS48SE0,
       "hh3cevtModuleSw-LSDM3GT24GPSE0": hh3cevtModuleSw_LSDM3GT24GPSE0,
       "hh3cevtModuleSw-LSDM3GT48SE0": hh3cevtModuleSw_LSDM3GT48SE0,
       "hh3cevtModuleSw-LSDM3GP48SE0": hh3cevtModuleSw_LSDM3GP48SE0,
       "hh3cevtModuleSw-SR07MPUA3-M": hh3cevtModuleSw_SR07MPUA3_M,
       "hh3cevtModuleSw-SFE-A": hh3cevtModuleSw_SFE_A,
       "hh3cevtModuleSw-MIC-CQ1L-M": hh3cevtModuleSw_MIC_CQ1L_M,
       "hh3cevtModuleSw-MIC-CQ2L-M": hh3cevtModuleSw_MIC_CQ2L_M,
       "hh3cevtModuleSw-LSXM1CGQ18C1": hh3cevtModuleSw_LSXM1CGQ18C1,
       "hh3cevtModuleSw-LSXM1CGQMS18B1": hh3cevtModuleSw_LSXM1CGQMS18B1,
       "hh3cevtModuleSw-LSXM1MOD48KBR1": hh3cevtModuleSw_LSXM1MOD48KBR1,
       "hh3cevtModuleSw-LSXM1CDQ36KB1": hh3cevtModuleSw_LSXM1CDQ36KB1,
       "hh3cevtModuleSw-LSXM1SUP02TR1": hh3cevtModuleSw_LSXM1SUP02TR1,
       "hh3cevtModuleSw-LSCM2SUP03B0": hh3cevtModuleSw_LSCM2SUP03B0,
       "hh3cevtModuleSw-LSCM2SUP03B0-Z": hh3cevtModuleSw_LSCM2SUP03B0_Z,
       "hh3cevtModuleSw-LSWM2QP4P": hh3cevtModuleSw_LSWM2QP4P,
       "hh3cevtModuleSw-LSXM1SUPS2": hh3cevtModuleSw_LSXM1SUPS2,
       "hh3cevtModuleSw-LSXM1SFS08D2": hh3cevtModuleSw_LSXM1SFS08D2,
       "hh3cevtModuleSw-LSXM1TGS48SE2": hh3cevtModuleSw_LSXM1TGS48SE2,
       "hh3cevtModuleSw-LSXM1GT24GPSE2": hh3cevtModuleSw_LSXM1GT24GPSE2,
       "hh3cevtModuleSw-LSXM1GT48SE2": hh3cevtModuleSw_LSXM1GT48SE2,
       "hh3cevtModuleSw-LSXM1GP48SE2": hh3cevtModuleSw_LSXM1GP48SE2,
       "hh3cevtModuleSw-LSXM3SUPS2": hh3cevtModuleSw_LSXM3SUPS2,
       "hh3cevtModuleSw-LSXM3SFS08D2": hh3cevtModuleSw_LSXM3SFS08D2,
       "hh3cevtModuleSw-LSXM3TGS48SE2": hh3cevtModuleSw_LSXM3TGS48SE2,
       "hh3cevtModuleSw-LSXM3GT24GPSE2": hh3cevtModuleSw_LSXM3GT24GPSE2,
       "hh3cevtModuleSw-LSXM3GT48SE2": hh3cevtModuleSw_LSXM3GT48SE2,
       "hh3cevtModuleSw-LSXM3GP48SE2": hh3cevtModuleSw_LSXM3GP48SE2,
       "hh3cevtModuleSw-LSXM3SUP04S2": hh3cevtModuleSw_LSXM3SUP04S2,
       "hh3cevtModuleSw-LSXM3SFS04G2": hh3cevtModuleSw_LSXM3SFS04G2,
       "hh3cevtModuleSw-LSXM3SFS08G2": hh3cevtModuleSw_LSXM3SFS08G2,
       "hh3cevtModuleSw-LSXM3SFS16G2": hh3cevtModuleSw_LSXM3SFS16G2,
       "hh3cevtModuleSw-LSXM3CGQ36SF2": hh3cevtModuleSw_LSXM3CGQ36SF2,
       "hh3cevtModuleSw-LSXM3YGS48SF2": hh3cevtModuleSw_LSXM3YGS48SF2,
       "hh3cevtModuleSw-LSXM3TGS48SF2": hh3cevtModuleSw_LSXM3TGS48SF2,
       "hh3cevtSubModuleRouter": hh3cevtSubModuleRouter,
       "hh3cevtSubModuleSwitch": hh3cevtSubModuleSwitch,
       "hh3cevtModuleCFCard": hh3cevtModuleCFCard,
       "hh3cevtModuleSDCard": hh3cevtModuleSDCard,
       "hh3cevtPort": hh3cevtPort,
       "hh3cevtPortUnknownPorts": hh3cevtPortUnknownPorts,
       "hh3cevtPortCommonPorts": hh3cevtPortCommonPorts,
       "hh3cevtPortRouterType": hh3cevtPortRouterType,
       "hh3cevtPortRt-Async": hh3cevtPortRt_Async,
       "hh3cevtPortRt-Analogmodem": hh3cevtPortRt_Analogmodem,
       "hh3cevtPortRt-Atm": hh3cevtPortRt_Atm,
       "hh3cevtPortRt-AtmAdsl": hh3cevtPortRt_AtmAdsl,
       "hh3cevtPortRt-AtmShdsl": hh3cevtPortRt_AtmShdsl,
       "hh3cevtPortRt-AtmE1": hh3cevtPortRt_AtmE1,
       "hh3cevtPortRt-AtmT1": hh3cevtPortRt_AtmT1,
       "hh3cevtPortRt-AtmE3": hh3cevtPortRt_AtmE3,
       "hh3cevtPortRt-AtmT3": hh3cevtPortRt_AtmT3,
       "hh3cevtPortRt-Atm622M": hh3cevtPortRt_Atm622M,
       "hh3cevtPortRt-AtmImaE1": hh3cevtPortRt_AtmImaE1,
       "hh3cevtPortRt-AtmImaT1": hh3cevtPortRt_AtmImaT1,
       "hh3cevtPortRt-Atm25M": hh3cevtPortRt_Atm25M,
       "hh3cevtPortRt-Bri": hh3cevtPortRt_Bri,
       "hh3cevtPortRt-Console": hh3cevtPortRt_Console,
       "hh3cevtPortRt-E1": hh3cevtPortRt_E1,
       "hh3cevtPortRt-E3": hh3cevtPortRt_E3,
       "hh3cevtPortRt-T1": hh3cevtPortRt_T1,
       "hh3cevtPortRt-T3": hh3cevtPortRt_T3,
       "hh3cevtPortRt-Cpos": hh3cevtPortRt_Cpos,
       "hh3cevtPortRt-Ethernet": hh3cevtPortRt_Ethernet,
       "hh3cevtPortRt-Serial": hh3cevtPortRt_Serial,
       "hh3cevtPortRt-E1f": hh3cevtPortRt_E1f,
       "hh3cevtPortRt-T1f": hh3cevtPortRt_T1f,
       "hh3cevtPortRt-Pos": hh3cevtPortRt_Pos,
       "hh3cevtPortRt-Ge": hh3cevtPortRt_Ge,
       "hh3cevtPortRt-Aux": hh3cevtPortRt_Aux,
       "hh3cevtPortRt-VG-Fxs": hh3cevtPortRt_VG_Fxs,
       "hh3cevtPortRt-VG-Fxo": hh3cevtPortRt_VG_Fxo,
       "hh3cevtPortRt-VG-E1vi": hh3cevtPortRt_VG_E1vi,
       "hh3cevtPortRt-VG-T1vi": hh3cevtPortRt_VG_T1vi,
       "hh3cevtPortRt-Usb": hh3cevtPortRt_Usb,
       "hh3cevtPortRt-Ndec": hh3cevtPortRt_Ndec,
       "hh3cevtPortRt-Cavium": hh3cevtPortRt_Cavium,
       "hh3cevtPortRt-Fcm": hh3cevtPortRt_Fcm,
       "hh3cevtPortRt-E1vi": hh3cevtPortRt_E1vi,
       "hh3cevtPortRt-T1vi": hh3cevtPortRt_T1vi,
       "hh3cevtPortRt-Vi": hh3cevtPortRt_Vi,
       "hh3cevtPortRt-Adls2Plus": hh3cevtPortRt_Adls2Plus,
       "hh3cevtPortRt-RADIO-AG": hh3cevtPortRt_RADIO_AG,
       "hh3cevtPortRt-1exp": hh3cevtPortRt_1exp,
       "hh3cevtPortRt-G-SHDSL-BIS": hh3cevtPortRt_G_SHDSL_BIS,
       "hh3cevtPortRt-ONU-1000BASE-BX-SFF-SC": hh3cevtPortRt_ONU_1000BASE_BX_SFF_SC,
       "hh3cevtPortRt-CELLULAR": hh3cevtPortRt_CELLULAR,
       "hh3cevtPortRt-CELLULAR-ETHERNET": hh3cevtPortRt_CELLULAR_ETHERNET,
       "hh3cevtPortRt-VGe": hh3cevtPortRt_VGe,
       "hh3cevtPortRt-VXGe": hh3cevtPortRt_VXGe,
       "hh3cevtPortRt-Xpos": hh3cevtPortRt_Xpos,
       "hh3cevtPortRt-Fge": hh3cevtPortRt_Fge,
       "hh3cevtPortRt-XGe": hh3cevtPortRt_XGe,
       "hh3cevtPortRt-HgeQsfp28Lc": hh3cevtPortRt_HgeQsfp28Lc,
       "hh3cevtPortRt-HgeCfp2Lc": hh3cevtPortRt_HgeCfp2Lc,
       "hh3cevtPortRt-HgeCfpLc": hh3cevtPortRt_HgeCfpLc,
       "hh3cevtPortRt-GeM12": hh3cevtPortRt_GeM12,
       "hh3cevtPortRt-VMEth": hh3cevtPortRt_VMEth,
       "hh3cevtPortRt-FiberGe": hh3cevtPortRt_FiberGe,
       "hh3cevtPortRt-GeOptic": hh3cevtPortRt_GeOptic,
       "hh3cevtPortRt-25Ge": hh3cevtPortRt_25Ge,
       "hh3cevtPortRt-50Ge": hh3cevtPortRt_50Ge,
       "hh3cevtPortRt-FlexE-50-100G": hh3cevtPortRt_FlexE_50_100G,
       "hh3cevtPortRt-50-100Ge": hh3cevtPortRt_50_100Ge,
       "hh3cevtPortRt-FlexE": hh3cevtPortRt_FlexE,
       "hh3cevtPortRt-100Ge": hh3cevtPortRt_100Ge,
       "hh3cevtPortRt-FlexE-50G": hh3cevtPortRt_FlexE_50G,
       "hh3cevtPortRt-Async-Phoenix": hh3cevtPortRt_Async_Phoenix,
       "hh3cevtPortRt-FlexE-100G": hh3cevtPortRt_FlexE_100G,
       "hh3cevtPortSwitchType": hh3cevtPortSwitchType,
       "hh3cevtPortSw-10or100M": hh3cevtPortSw_10or100M,
       "hh3cevtPortSw-1000BaseLxSm": hh3cevtPortSw_1000BaseLxSm,
       "hh3cevtPortSw-1000BaseSxMm": hh3cevtPortSw_1000BaseSxMm,
       "hh3cevtPortSw-1000BaseTx": hh3cevtPortSw_1000BaseTx,
       "hh3cevtPortSw-100MSinglemodeFx": hh3cevtPortSw_100MSinglemodeFx,
       "hh3cevtPortSw-100MMultimodeFx": hh3cevtPortSw_100MMultimodeFx,
       "hh3cevtPortSw-100M100BaseTx": hh3cevtPortSw_100M100BaseTx,
       "hh3cevtPortSw-100MHub": hh3cevtPortSw_100MHub,
       "hh3cevtPortSw-Vdsl": hh3cevtPortSw_Vdsl,
       "hh3cevtPortSw-Stack": hh3cevtPortSw_Stack,
       "hh3cevtPortSw-1000BaseZenithFx": hh3cevtPortSw_1000BaseZenithFx,
       "hh3cevtPortSw-1000BaseLongFx": hh3cevtPortSw_1000BaseLongFx,
       "hh3cevtPortSw-Adsl": hh3cevtPortSw_Adsl,
       "hh3cevtPortSw-10or100MDb": hh3cevtPortSw_10or100MDb,
       "hh3cevtPortSw-10GBaseLrSm": hh3cevtPortSw_10GBaseLrSm,
       "hh3cevtPortSw-10GBaseLx4Mm": hh3cevtPortSw_10GBaseLx4Mm,
       "hh3cevtPortSw-10GBaseLx4Sm": hh3cevtPortSw_10GBaseLx4Sm,
       "hh3cevtPortSw-100MLongFx": hh3cevtPortSw_100MLongFx,
       "hh3cevtPortSw-1000BaseCx": hh3cevtPortSw_1000BaseCx,
       "hh3cevtPortSw-1000BaseZenithFxLc": hh3cevtPortSw_1000BaseZenithFxLc,
       "hh3cevtPortSw-1000BaseLongFxLc": hh3cevtPortSw_1000BaseLongFxLc,
       "hh3cevtPortSw-100MSmFxSc": hh3cevtPortSw_100MSmFxSc,
       "hh3cevtPortSw-100MMmFxSc": hh3cevtPortSw_100MMmFxSc,
       "hh3cevtPortSw-100MSmFxLc": hh3cevtPortSw_100MSmFxLc,
       "hh3cevtPortSw-100MMmFxLc": hh3cevtPortSw_100MMmFxLc,
       "hh3cevtPortSw-GbicNoConnector": hh3cevtPortSw_GbicNoConnector,
       "hh3cevtPortSw-Gbic1000BaseT": hh3cevtPortSw_Gbic1000BaseT,
       "hh3cevtPortSw-Gbic1000BaseLx": hh3cevtPortSw_Gbic1000BaseLx,
       "hh3cevtPortSw-Gbic1000BaseSx": hh3cevtPortSw_Gbic1000BaseSx,
       "hh3cevtPortSw-Gbic1000BaseZx": hh3cevtPortSw_Gbic1000BaseZx,
       "hh3cevtPortSw-ComboNoConnector": hh3cevtPortSw_ComboNoConnector,
       "hh3cevtPortSw-Combo1000BaseLx": hh3cevtPortSw_Combo1000BaseLx,
       "hh3cevtPortSw-Combo1000BaseLxFiber": hh3cevtPortSw_Combo1000BaseLxFiber,
       "hh3cevtPortSw-Combo1000BaseLxCopper": hh3cevtPortSw_Combo1000BaseLxCopper,
       "hh3cevtPortSw-Combo1000BaseSx": hh3cevtPortSw_Combo1000BaseSx,
       "hh3cevtPortSw-Combo1000BaseSxFiber": hh3cevtPortSw_Combo1000BaseSxFiber,
       "hh3cevtPortSw-Combo1000BaseSxCopper": hh3cevtPortSw_Combo1000BaseSxCopper,
       "hh3cevtPortSw-Combo1000BaseZx": hh3cevtPortSw_Combo1000BaseZx,
       "hh3cevtPortSw-Combo1000BaseZxFiber": hh3cevtPortSw_Combo1000BaseZxFiber,
       "hh3cevtPortSw-Combo1000BaseZxCopper": hh3cevtPortSw_Combo1000BaseZxCopper,
       "hh3cevtPortSw-155PosSxMmf": hh3cevtPortSw_155PosSxMmf,
       "hh3cevtPortSw-155PosLxSmf": hh3cevtPortSw_155PosLxSmf,
       "hh3cevtPortSw-1000BASE-T": hh3cevtPortSw_1000BASE_T,
       "hh3cevtPortSw-1000BASE-SX-SFP": hh3cevtPortSw_1000BASE_SX_SFP,
       "hh3cevtPortSw-1000BASE-LX-SFP": hh3cevtPortSw_1000BASE_LX_SFP,
       "hh3cevtPortSw-1000BASE-T-AN-SFP": hh3cevtPortSw_1000BASE_T_AN_SFP,
       "hh3cevtPortSw-10GBASE-LX4-XENPAK": hh3cevtPortSw_10GBASE_LX4_XENPAK,
       "hh3cevtPortSw-10GBASE-LR-XENPAK": hh3cevtPortSw_10GBASE_LR_XENPAK,
       "hh3cevtPortSw-10GBASE-CX4": hh3cevtPortSw_10GBASE_CX4,
       "hh3cevtPortSw-1000BASE-ZX-SFP": hh3cevtPortSw_1000BASE_ZX_SFP,
       "hh3cevtPortSw-1000BASE-MM-SFP": hh3cevtPortSw_1000BASE_MM_SFP,
       "hh3cevtPortSw-100BASE-SX-SFP": hh3cevtPortSw_100BASE_SX_SFP,
       "hh3cevtPortSw-100BASE-LX-SFP": hh3cevtPortSw_100BASE_LX_SFP,
       "hh3cevtPortSw-100BASE-T-AN-SFP": hh3cevtPortSw_100BASE_T_AN_SFP,
       "hh3cevtPortSw-100BASE-ZX-SFP": hh3cevtPortSw_100BASE_ZX_SFP,
       "hh3cevtPortSw-100BASE-MM-SFP": hh3cevtPortSw_100BASE_MM_SFP,
       "hh3cevtPortSw-SFP-NO-CONNECTOR": hh3cevtPortSw_SFP_NO_CONNECTOR,
       "hh3cevtPortSw-SFP-UNKNOWN-CONNECTOR": hh3cevtPortSw_SFP_UNKNOWN_CONNECTOR,
       "hh3cevtPortSw-POS-NO-CONNECTOR": hh3cevtPortSw_POS_NO_CONNECTOR,
       "hh3cevtPortSw-10G-BASE-SR": hh3cevtPortSw_10G_BASE_SR,
       "hh3cevtPortSw-10G-BASE-ER": hh3cevtPortSw_10G_BASE_ER,
       "hh3cevtPortSw-10G-BASE-LX4": hh3cevtPortSw_10G_BASE_LX4,
       "hh3cevtPortSw-10G-BASE-SW": hh3cevtPortSw_10G_BASE_SW,
       "hh3cevtPortSw-10G-BASE-LW": hh3cevtPortSw_10G_BASE_LW,
       "hh3cevtPortSw-10G-BASE-EW": hh3cevtPortSw_10G_BASE_EW,
       "hh3cevtPortSw-10G-LR-SM-LC": hh3cevtPortSw_10G_LR_SM_LC,
       "hh3cevtPortSw-10G-SR-MM-LC": hh3cevtPortSw_10G_SR_MM_LC,
       "hh3cevtPortSw-10G-ER-SM-LC": hh3cevtPortSw_10G_ER_SM_LC,
       "hh3cevtPortSw-10G-LW-SM-LC": hh3cevtPortSw_10G_LW_SM_LC,
       "hh3cevtPortSw-10G-SW-MM-LC": hh3cevtPortSw_10G_SW_MM_LC,
       "hh3cevtPortSw-10G-EW-SM-LC": hh3cevtPortSw_10G_EW_SM_LC,
       "hh3cevtPortSw-100BASE-SM-MTRJ": hh3cevtPortSw_100BASE_SM_MTRJ,
       "hh3cevtPortSw-100BASE-MM-MTRJ": hh3cevtPortSw_100BASE_MM_MTRJ,
       "hh3cevtPortSw-XFP-NO-CONNECTOR": hh3cevtPortSw_XFP_NO_CONNECTOR,
       "hh3cevtPortSw-XFP-10GBASE-SR": hh3cevtPortSw_XFP_10GBASE_SR,
       "hh3cevtPortSw-XFP-10GBASE-LR": hh3cevtPortSw_XFP_10GBASE_LR,
       "hh3cevtPortSw-XFP-10GBASE-ER": hh3cevtPortSw_XFP_10GBASE_ER,
       "hh3cevtPortSw-XFP-10GBASE-SW": hh3cevtPortSw_XFP_10GBASE_SW,
       "hh3cevtPortSw-XFP-10GBASE-LW": hh3cevtPortSw_XFP_10GBASE_LW,
       "hh3cevtPortSw-XFP-10GBASE-EW": hh3cevtPortSw_XFP_10GBASE_EW,
       "hh3cevtPortSw-XFP-10GBASE-CX4": hh3cevtPortSw_XFP_10GBASE_CX4,
       "hh3cevtPortSw-XFP-10GBASE-LX4": hh3cevtPortSw_XFP_10GBASE_LX4,
       "hh3cevtPortSw-XFP-UNKNOWN": hh3cevtPortSw_XFP_UNKNOWN,
       "hh3cevtPortSw-XPK-NOCONNECTOR": hh3cevtPortSw_XPK_NOCONNECTOR,
       "hh3cevtPortSw-XPK-10GBASE-SR": hh3cevtPortSw_XPK_10GBASE_SR,
       "hh3cevtPortSw-XPK-10GBASE-LR": hh3cevtPortSw_XPK_10GBASE_LR,
       "hh3cevtPortSw-XPK-10GBASE-ER": hh3cevtPortSw_XPK_10GBASE_ER,
       "hh3cevtPortSw-XPK-10GBASE-SW": hh3cevtPortSw_XPK_10GBASE_SW,
       "hh3cevtPortSw-XPK-10GBASE-LW": hh3cevtPortSw_XPK_10GBASE_LW,
       "hh3cevtPortSw-XPK-10GBASE-EW": hh3cevtPortSw_XPK_10GBASE_EW,
       "hh3cevtPortSw-XPK-10GBASE-CX4": hh3cevtPortSw_XPK_10GBASE_CX4,
       "hh3cevtPortSw-XPK-10GBASE-LX4": hh3cevtPortSw_XPK_10GBASE_LX4,
       "hh3cevtPortSw-XPK-UNKNOWN": hh3cevtPortSw_XPK_UNKNOWN,
       "hh3cevtPortSw-POS-OC48-SR-SM-LC": hh3cevtPortSw_POS_OC48_SR_SM_LC,
       "hh3cevtPortSw-POS-OC48-IR-SM-LC": hh3cevtPortSw_POS_OC48_IR_SM_LC,
       "hh3cevtPortSw-POS-OC48-LR-SM-LC": hh3cevtPortSw_POS_OC48_LR_SM_LC,
       "hh3cevtPortSw-10G-BASE-CX4": hh3cevtPortSw_10G_BASE_CX4,
       "hh3cevtPortSw-OLT-1000BASE-BX-SFF-SC": hh3cevtPortSw_OLT_1000BASE_BX_SFF_SC,
       "hh3cevtPortSw-ONU-1000BASE-BX-SFF-SC": hh3cevtPortSw_ONU_1000BASE_BX_SFF_SC,
       "hh3cevtPortSw-24G-CASCADE": hh3cevtPortSw_24G_CASCADE,
       "hh3cevtPortSw-POS-OC3-SR-MM": hh3cevtPortSw_POS_OC3_SR_MM,
       "hh3cevtPortSw-POS-OC3-IR-SM": hh3cevtPortSw_POS_OC3_IR_SM,
       "hh3cevtPortSw-POS-OC3-IR-1-SM": hh3cevtPortSw_POS_OC3_IR_1_SM,
       "hh3cevtPortSw-POS-OC3-IR-2-SM": hh3cevtPortSw_POS_OC3_IR_2_SM,
       "hh3cevtPortSw-POS-OC3-LR-SM": hh3cevtPortSw_POS_OC3_LR_SM,
       "hh3cevtPortSw-POS-OC3-LR-1-SM": hh3cevtPortSw_POS_OC3_LR_1_SM,
       "hh3cevtPortSw-POS-OC3-LR-2-SM": hh3cevtPortSw_POS_OC3_LR_2_SM,
       "hh3cevtPortSw-POS-OC3-LR-3-SM": hh3cevtPortSw_POS_OC3_LR_3_SM,
       "hh3cevtPortSw-POS-OC12-SR-MM": hh3cevtPortSw_POS_OC12_SR_MM,
       "hh3cevtPortSw-POS-OC12-IR-SM": hh3cevtPortSw_POS_OC12_IR_SM,
       "hh3cevtPortSw-POS-OC12-IR-1-SM": hh3cevtPortSw_POS_OC12_IR_1_SM,
       "hh3cevtPortSw-POS-OC12-IR-2-SM": hh3cevtPortSw_POS_OC12_IR_2_SM,
       "hh3cevtPortSw-POS-OC12-LR-SM": hh3cevtPortSw_POS_OC12_LR_SM,
       "hh3cevtPortSw-POS-OC12-LR-1-SM": hh3cevtPortSw_POS_OC12_LR_1_SM,
       "hh3cevtPortSw-POS-OC12-LR-2-SM": hh3cevtPortSw_POS_OC12_LR_2_SM,
       "hh3cevtPortSw-POS-OC12-LR-3-SM": hh3cevtPortSw_POS_OC12_LR_3_SM,
       "hh3cevtPortSw-POS-OC48-SR-SM": hh3cevtPortSw_POS_OC48_SR_SM,
       "hh3cevtPortSw-POS-OC48-IR-SM": hh3cevtPortSw_POS_OC48_IR_SM,
       "hh3cevtPortSw-POS-OC48-IR-1-SM": hh3cevtPortSw_POS_OC48_IR_1_SM,
       "hh3cevtPortSw-POS-OC48-IR-2-SM": hh3cevtPortSw_POS_OC48_IR_2_SM,
       "hh3cevtPortSw-POS-OC48-LR-SM": hh3cevtPortSw_POS_OC48_LR_SM,
       "hh3cevtPortSw-POS-OC48-LR-1-SM": hh3cevtPortSw_POS_OC48_LR_1_SM,
       "hh3cevtPortSw-POS-OC48-LR-2-SM": hh3cevtPortSw_POS_OC48_LR_2_SM,
       "hh3cevtPortSw-POS-OC48-LR-3-SM": hh3cevtPortSw_POS_OC48_LR_3_SM,
       "hh3cevtPortSw-POS-I-64-1": hh3cevtPortSw_POS_I_64_1,
       "hh3cevtPortSw-POS-I-64-2": hh3cevtPortSw_POS_I_64_2,
       "hh3cevtPortSw-POS-I-64-3": hh3cevtPortSw_POS_I_64_3,
       "hh3cevtPortSw-POS-I-64-5": hh3cevtPortSw_POS_I_64_5,
       "hh3cevtPortSw-POS-S-64-1": hh3cevtPortSw_POS_S_64_1,
       "hh3cevtPortSw-POS-S-64-2": hh3cevtPortSw_POS_S_64_2,
       "hh3cevtPortSw-POS-S-64-3": hh3cevtPortSw_POS_S_64_3,
       "hh3cevtPortSw-POS-S-64-5": hh3cevtPortSw_POS_S_64_5,
       "hh3cevtPortSw-POS-L-64-1": hh3cevtPortSw_POS_L_64_1,
       "hh3cevtPortSw-POS-L-64-2": hh3cevtPortSw_POS_L_64_2,
       "hh3cevtPortSw-POS-L-64-3": hh3cevtPortSw_POS_L_64_3,
       "hh3cevtPortSw-POS-V-64-2": hh3cevtPortSw_POS_V_64_2,
       "hh3cevtPortSw-POS-V-64-3": hh3cevtPortSw_POS_V_64_3,
       "hh3cevtPortSw-100BASE-FX-BIDI": hh3cevtPortSw_100BASE_FX_BIDI,
       "hh3cevtPortSw-100BASE-BX10-U-SFP": hh3cevtPortSw_100BASE_BX10_U_SFP,
       "hh3cevtPortSw-100BASE-BX10-D-SFP": hh3cevtPortSw_100BASE_BX10_D_SFP,
       "hh3cevtPortSw-1000BASE-BX10-U-SFP": hh3cevtPortSw_1000BASE_BX10_U_SFP,
       "hh3cevtPortSw-1000BASE-BX10-D-SFP": hh3cevtPortSw_1000BASE_BX10_D_SFP,
       "hh3cevtPortSw-STK-1000BASE-T": hh3cevtPortSw_STK_1000BASE_T,
       "hh3cevtPortSw-RPR-PHYPOS-CONNECTOR": hh3cevtPortSw_RPR_PHYPOS_CONNECTOR,
       "hh3cevtPortSw-RPR-PHY10GE-CONNECTOR": hh3cevtPortSw_RPR_PHY10GE_CONNECTOR,
       "hh3cevtPortSw-RPR-LOGICPOS-CONNECTOR": hh3cevtPortSw_RPR_LOGICPOS_CONNECTOR,
       "hh3cevtPortSw-RPR-LOGIC10GE-CONNECTOR": hh3cevtPortSw_RPR_LOGIC10GE_CONNECTOR,
       "hh3cevtPortSw-10GBASE-ZR": hh3cevtPortSw_10GBASE_ZR,
       "hh3cevtPortSw-TYPE-ERROR-CONNECTOR": hh3cevtPortSw_TYPE_ERROR_CONNECTOR,
       "hh3cevtPortSw-10G-STACK": hh3cevtPortSw_10G_STACK,
       "hh3cevtPortSw-155-ATM-SX-MMF": hh3cevtPortSw_155_ATM_SX_MMF,
       "hh3cevtPortSw-155-ATM-LX-SMF": hh3cevtPortSw_155_ATM_LX_SMF,
       "hh3cevtPortSw-622-ATM-SX-MMF": hh3cevtPortSw_622_ATM_SX_MMF,
       "hh3cevtPortSw-622-ATM-LX-SMF": hh3cevtPortSw_622_ATM_LX_SMF,
       "hh3cevtPortSw-155-ATM-NO-CONNECTOR": hh3cevtPortSw_155_ATM_NO_CONNECTOR,
       "hh3cevtPortSw-622-ATM-NO-CONNECTOR": hh3cevtPortSw_622_ATM_NO_CONNECTOR,
       "hh3cevtPortSw-155-CPOS-E1-NO-CONNECTOR": hh3cevtPortSw_155_CPOS_E1_NO_CONNECTOR,
       "hh3cevtPortSw-155-CPOS-T1-NO-CONNECTOR": hh3cevtPortSw_155_CPOS_T1_NO_CONNECTOR,
       "hh3cevtPortSw-622-CPOS-E1-NO-CONNECTOR": hh3cevtPortSw_622_CPOS_E1_NO_CONNECTOR,
       "hh3cevtPortSw-622-CPOS-T1-NO-CONNECTOR": hh3cevtPortSw_622_CPOS_T1_NO_CONNECTOR,
       "hh3cevtPortSw-155-CPOS-E1-SX-MMF": hh3cevtPortSw_155_CPOS_E1_SX_MMF,
       "hh3cevtPortSw-155-CPOS-T1-SX-MMF": hh3cevtPortSw_155_CPOS_T1_SX_MMF,
       "hh3cevtPortSw-155-CPOS-E1-LX-SMF": hh3cevtPortSw_155_CPOS_E1_LX_SMF,
       "hh3cevtPortSw-155-CPOS-T1-LX-SMF": hh3cevtPortSw_155_CPOS_T1_LX_SMF,
       "hh3cevtPortSw-622-CPOS-E1-SX-MMF": hh3cevtPortSw_622_CPOS_E1_SX_MMF,
       "hh3cevtPortSw-622-CPOS-T1-SX-MMF": hh3cevtPortSw_622_CPOS_T1_SX_MMF,
       "hh3cevtPortSw-622-CPOS-E1-LX-SMF": hh3cevtPortSw_622_CPOS_E1_LX_SMF,
       "hh3cevtPortSw-622-CPOS-T1-LX-SMF": hh3cevtPortSw_622_CPOS_T1_LX_SMF,
       "hh3cevtPortSw-E1-CONNECTOR": hh3cevtPortSw_E1_CONNECTOR,
       "hh3cevtPortSw-T1-CONNECTOR": hh3cevtPortSw_T1_CONNECTOR,
       "hh3cevtPortSw-1000BASE-STK-SFP": hh3cevtPortSw_1000BASE_STK_SFP,
       "hh3cevtPortSw-1000BASE-BIDI-SFP": hh3cevtPortSw_1000BASE_BIDI_SFP,
       "hh3cevtPortSw-1000BASE-CWDM-SFP": hh3cevtPortSw_1000BASE_CWDM_SFP,
       "hh3cevtPortSw-100BASE-BIDI-SFP": hh3cevtPortSw_100BASE_BIDI_SFP,
       "hh3cevtPortSw-OLT-1000BASE-PX-SFP": hh3cevtPortSw_OLT_1000BASE_PX_SFP,
       "hh3cevtPortSw-OLT-1000BASE-NO-CONNECTOR": hh3cevtPortSw_OLT_1000BASE_NO_CONNECTOR,
       "hh3cevtPortSw-RPR-PHYGE-CONNECTOR": hh3cevtPortSw_RPR_PHYGE_CONNECTOR,
       "hh3cevtPortSw-RPR-LOGICGE-CONNECTOR": hh3cevtPortSw_RPR_LOGICGE_CONNECTOR,
       "hh3cevtPortSw-100M-1550-BIDI": hh3cevtPortSw_100M_1550_BIDI,
       "hh3cevtPortSw-100M-1310-BIDI": hh3cevtPortSw_100M_1310_BIDI,
       "hh3cevtPortSw-RPR-PHYOC48-CONNECTOR": hh3cevtPortSw_RPR_PHYOC48_CONNECTOR,
       "hh3cevtPortSw-RPR-LOGICOC48-CONNECTOR": hh3cevtPortSw_RPR_LOGICOC48_CONNECTOR,
       "hh3cevtPortSw-100-1000-BASE-LX-SMF": hh3cevtPortSw_100_1000_BASE_LX_SMF,
       "hh3cevtPortSw-10G-ZW-SM-LC": hh3cevtPortSw_10G_ZW_SM_LC,
       "hh3cevtPortSw-10G-ZR-SM-LC": hh3cevtPortSw_10G_ZR_SM_LC,
       "hh3cevtPortSw-XPK-10GBASE-ZR": hh3cevtPortSw_XPK_10GBASE_ZR,
       "hh3cevtPortSw-SGMII-100-BASE-LX-SFP": hh3cevtPortSw_SGMII_100_BASE_LX_SFP,
       "hh3cevtPortSw-SGMII-100-BASE-FX-SFP": hh3cevtPortSw_SGMII_100_BASE_FX_SFP,
       "hh3cevtPortSw-WLAN-RADIO": hh3cevtPortSw_WLAN_RADIO,
       "hh3cevtPortSw-CABLE": hh3cevtPortSw_CABLE,
       "hh3cevtPortSw-SFP-PLUS-NO-CONNECTOR": hh3cevtPortSw_SFP_PLUS_NO_CONNECTOR,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-SR": hh3cevtPortSw_SFP_PLUS_10GBASE_SR,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-LR": hh3cevtPortSw_SFP_PLUS_10GBASE_LR,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-LRM": hh3cevtPortSw_SFP_PLUS_10GBASE_LRM,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-Cu": hh3cevtPortSw_SFP_PLUS_10GBASE_Cu,
       "hh3cevtPortSw-SFP-PLUS-UNKNOWN": hh3cevtPortSw_SFP_PLUS_UNKNOWN,
       "hh3cevtPortSw-SFP-PLUS-STACK-CONNECTOR": hh3cevtPortSw_SFP_PLUS_STACK_CONNECTOR,
       "hh3cevtPortSw-POS-L-64-4": hh3cevtPortSw_POS_L_64_4,
       "hh3cevtPortSw-MINISAS-HD-STACK-CONNECTOR": hh3cevtPortSw_MINISAS_HD_STACK_CONNECTOR,
       "hh3cevtPortSw-ONU-1000BASE-PX-SFF": hh3cevtPortSw_ONU_1000BASE_PX_SFF,
       "hh3cevtPortSw-RS485": hh3cevtPortSw_RS485,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-ER": hh3cevtPortSw_SFP_PLUS_10GBASE_ER,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-ZR": hh3cevtPortSw_SFP_PLUS_10GBASE_ZR,
       "hh3cevtPortSw-XFP-10GBASE-ZR": hh3cevtPortSw_XFP_10GBASE_ZR,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-SR4": hh3cevtPortSw_QSFP_PLUS_40GBASE_SR4,
       "hh3cevtPortSw-QSFP-PLUS-STACK-CONNECTOR": hh3cevtPortSw_QSFP_PLUS_STACK_CONNECTOR,
       "hh3cevtPortSw-QSFP-PLUS-TO-4SFP-PLUS-STACK-CONNECTOR": hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_STACK_CONNECTOR,
       "hh3cevtPortSw-SFP-STACK-CONNECTOR": hh3cevtPortSw_SFP_STACK_CONNECTOR,
       "hh3cevtPortSw-QSFP-NO-CONNECTOR": hh3cevtPortSw_QSFP_NO_CONNECTOR,
       "hh3cevtPortSw-10GBase-T": hh3cevtPortSw_10GBase_T,
       "hh3cevtPortSw-CFP-NO-CONNECTOR": hh3cevtPortSw_CFP_NO_CONNECTOR,
       "hh3cevtPortSw-CFP-40GBASE-LR4": hh3cevtPortSw_CFP_40GBASE_LR4,
       "hh3cevtPortSw-QSFP-PLUS-NO-CONNECTOR": hh3cevtPortSw_QSFP_PLUS_NO_CONNECTOR,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-LR4": hh3cevtPortSw_QSFP_PLUS_40GBASE_LR4,
       "hh3cevtPortSw-CFP-40GBASE-SR4": hh3cevtPortSw_CFP_40GBASE_SR4,
       "hh3cevtPortSw-CFP-100GBASE-LR4": hh3cevtPortSw_CFP_100GBASE_LR4,
       "hh3cevtPortSw-CFP-100GBASE-SR10": hh3cevtPortSw_CFP_100GBASE_SR10,
       "hh3cevtPortSw-CXP-100GBASE-SR10": hh3cevtPortSw_CXP_100GBASE_SR10,
       "hh3cevtPortSw-CXP-NO-CONNECTOR": hh3cevtPortSw_CXP_NO_CONNECTOR,
       "hh3cevtPortSw-TRANSCEIVER-UNKNOWN": hh3cevtPortSw_TRANSCEIVER_UNKNOWN,
       "hh3cevtPortSw-QSFP-PLUS-UNKNOWN": hh3cevtPortSw_QSFP_PLUS_UNKNOWN,
       "hh3cevtPortSw-CFP-UNKNOWN": hh3cevtPortSw_CFP_UNKNOWN,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-CSR4": hh3cevtPortSw_QSFP_PLUS_40GBASE_CSR4,
       "hh3cevtPortSw-CFP-40GBASE-ER4": hh3cevtPortSw_CFP_40GBASE_ER4,
       "hh3cevtPortSw-SFP-1000BASE-BIDI": hh3cevtPortSw_SFP_1000BASE_BIDI,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-ZR-DWDM": hh3cevtPortSw_SFP_PLUS_10GBASE_ZR_DWDM,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-PSM": hh3cevtPortSw_QSFP_PLUS_40GBASE_PSM,
       "hh3cevtPortSw-SFP-8GFC-SW": hh3cevtPortSw_SFP_8GFC_SW,
       "hh3cevtPortSw-SFP-8GFC-LW": hh3cevtPortSw_SFP_8GFC_LW,
       "hh3cevtPortSw-CXP-100GBASE-AOC": hh3cevtPortSw_CXP_100GBASE_AOC,
       "hh3cevtPortSw-QSFP-PLUS-ACTIVE-STACK-CONNECTOR": hh3cevtPortSw_QSFP_PLUS_ACTIVE_STACK_CONNECTOR,
       "hh3cevtPortSw-QSFP-PLUS-TO-4SFP-PLUS-ACTIVE-STACK-CONNECTOR": hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_STACK_CONNECTOR,
       "hh3cevtPortSw-CFP2-100GBASE-LR4": hh3cevtPortSw_CFP2_100GBASE_LR4,
       "hh3cevtPortSw-CFP2-100GBASE-SR10": hh3cevtPortSw_CFP2_100GBASE_SR10,
       "hh3cevtPortSw-QSFP-PLUS-ACTIVE-OPTICAL-CABLE": hh3cevtPortSw_QSFP_PLUS_ACTIVE_OPTICAL_CABLE,
       "hh3cevtPortSw-QSFP-PLUS-TO-4SFP-PLUS-ACTIVE-OPTICAL-CABLE": hh3cevtPortSw_QSFP_PLUS_TO_4SFP_PLUS_ACTIVE_OPTICAL_CABLE,
       "hh3cevtPortSw-SFP-PLUS-ACTIVE-OPTICAL-CABLE": hh3cevtPortSw_SFP_PLUS_ACTIVE_OPTICAL_CABLE,
       "hh3cevtPortSw-CFP2-NO-CONNECTOR": hh3cevtPortSw_CFP2_NO_CONNECTOR,
       "hh3cevtPortSw-QSFP28-NO-CONNECTOR": hh3cevtPortSw_QSFP28_NO_CONNECTOR,
       "hh3cevtPortSw-QSFP28-100GBASE-SR4": hh3cevtPortSw_QSFP28_100GBASE_SR4,
       "hh3cevtPortSw-QSFP28-100GBASE-LR4": hh3cevtPortSw_QSFP28_100GBASE_LR4,
       "hh3cevtPortSw-QSFP28-100GBASE-ER4": hh3cevtPortSw_QSFP28_100GBASE_ER4,
       "hh3cevtPortSw-QSFP28-100GBASE-PSM4": hh3cevtPortSw_QSFP28_100GBASE_PSM4,
       "hh3cevtPortSw-QSFP28-100GBASE-CWDM4": hh3cevtPortSw_QSFP28_100GBASE_CWDM4,
       "hh3cevtPortSw-QSFP28-STACK-CONNECTOR": hh3cevtPortSw_QSFP28_STACK_CONNECTOR,
       "hh3cevtPortSw-QSFP28-TO-4SFP28-STACK-CONNECTOR": hh3cevtPortSw_QSFP28_TO_4SFP28_STACK_CONNECTOR,
       "hh3cevtPortSw-QSFP28-ACTIVE-STACK-CONNECTOR": hh3cevtPortSw_QSFP28_ACTIVE_STACK_CONNECTOR,
       "hh3cevtPortSw-QSFP28-TO-4SFP28-ACTIVE-STACK-CONNECTOR": hh3cevtPortSw_QSFP28_TO_4SFP28_ACTIVE_STACK_CONNECTOR,
       "hh3cevtPortSw-QSFP28-ACTIVE-OPTICAL-CABLE": hh3cevtPortSw_QSFP28_ACTIVE_OPTICAL_CABLE,
       "hh3cevtPortSw-QSFP28-TO-4SFP28-ACTIVE-OPTICAL-CABLE": hh3cevtPortSw_QSFP28_TO_4SFP28_ACTIVE_OPTICAL_CABLE,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-LM4": hh3cevtPortSw_QSFP_PLUS_40GBASE_LM4,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-SWDM4": hh3cevtPortSw_QSFP_PLUS_40GBASE_SWDM4,
       "hh3cevtPortSw-CFP-100GBASE-ER4": hh3cevtPortSw_CFP_100GBASE_ER4,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-ER4": hh3cevtPortSw_QSFP_PLUS_40GBASE_ER4,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-ER4L": hh3cevtPortSw_QSFP_PLUS_40GBASE_ER4L,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-BIDI": hh3cevtPortSw_QSFP_PLUS_40GBASE_BIDI,
       "hh3cevtPortSw-QSFP-PLUS-40GBASE-LR4L": hh3cevtPortSw_QSFP_PLUS_40GBASE_LR4L,
       "hh3cevtPortSw-CFP2-100GBASE-eSR10": hh3cevtPortSw_CFP2_100GBASE_eSR10,
       "hh3cevtPortSw-TUNABLE-SFP-PLUS-10GBASE-ZR-DWDM": hh3cevtPortSw_TUNABLE_SFP_PLUS_10GBASE_ZR_DWDM,
       "hh3cevtPortSw-SFP28-25GBASE-SR": hh3cevtPortSw_SFP28_25GBASE_SR,
       "hh3cevtPortSw-SFP28-ACTIVE-OPTICAL-CABLE": hh3cevtPortSw_SFP28_ACTIVE_OPTICAL_CABLE,
       "hh3cevtPortSw-SFP28-STACK-CONNECTOR": hh3cevtPortSw_SFP28_STACK_CONNECTOR,
       "hh3cevtPortSw-2DOT5GBASE-T": hh3cevtPortSw_2DOT5GBASE_T,
       "hh3cevtPortSw-QSFP28-100GBASE-SWDM4": hh3cevtPortSw_QSFP28_100GBASE_SWDM4,
       "hh3cevtPortSw-QSFP28-100GBASE-eSWDM4": hh3cevtPortSw_QSFP28_100GBASE_eSWDM4,
       "hh3cevtPortSw-SFP-PLUS-10GBASE-T": hh3cevtPortSw_SFP_PLUS_10GBASE_T,
       "hh3cevtPortSw-QSFP28-100GBASE-eSR4": hh3cevtPortSw_QSFP28_100GBASE_eSR4,
       "hh3cevtPortSw-QSFP28-100GBASE-BIDI": hh3cevtPortSw_QSFP28_100GBASE_BIDI,
       "hh3cevtPortSw-QSFP28-100GBASE-WDM2": hh3cevtPortSw_QSFP28_100GBASE_WDM2,
       "hh3cevtPortSw-SFP28-25GBASE-LR": hh3cevtPortSw_SFP28_25GBASE_LR,
       "hh3cevtPortSw-CFP2-100GBASE-ER4": hh3cevtPortSw_CFP2_100GBASE_ER4,
       "hh3cevtPortSw-CFP2-DCO-200GBASE-ZR": hh3cevtPortSw_CFP2_DCO_200GBASE_ZR,
       "hh3cevtPortSw-CFP2-100GBASE-ER4L": hh3cevtPortSw_CFP2_100GBASE_ER4L,
       "hh3cevtPortSw-SFP-16GFC-SW": hh3cevtPortSw_SFP_16GFC_SW,
       "hh3cevtPortSw-SFP-16GFC-LW": hh3cevtPortSw_SFP_16GFC_LW,
       "hh3cevtPortSw-SFP-32GFC-SW": hh3cevtPortSw_SFP_32GFC_SW,
       "hh3cevtPortSw-SFP-32GFC-LW": hh3cevtPortSw_SFP_32GFC_LW,
       "hh3cevtPortSw-XFP-10GBASE-PR-D3": hh3cevtPortSw_XFP_10GBASE_PR_D3,
       "hh3cevtPortSw-XFP-10GBASE-PRX-D3": hh3cevtPortSw_XFP_10GBASE_PRX_D3,
       "hh3cevtPortSw-5GBASE-T": hh3cevtPortSw_5GBASE_T,
       "hh3cevtPortSw-QSFP28-UNKNOWN": hh3cevtPortSw_QSFP28_UNKNOWN,
       "hh3cevtPortSw-SFP28-UNKNOWN": hh3cevtPortSw_SFP28_UNKNOWN,
       "hh3cevtPortSw-SFP28-NO-CONNECTOR": hh3cevtPortSw_SFP28_NO_CONNECTOR,
       "hh3cevtPortSw-SFP-PLUS-9-8GCRPI-IR": hh3cevtPortSw_SFP_PLUS_9_8GCRPI_IR,
       "hh3cevtPortSw-SFP-PLUS-9-8GCRPI-LR": hh3cevtPortSw_SFP_PLUS_9_8GCRPI_LR,
       "hh3cevtPortSw-50GBase-F": hh3cevtPortSw_50GBase_F,
       "hh3cevtPortSw-QSFP28-50GBASE-PAM4-LR": hh3cevtPortSw_QSFP28_50GBASE_PAM4_LR,
       "hh3cevtPortSw-10GBASE-BIDI-SFP": hh3cevtPortSw_10GBASE_BIDI_SFP,
       "hh3cevtPortSw-10GBASE-BIDI-U-SFP-PLUS": hh3cevtPortSw_10GBASE_BIDI_U_SFP_PLUS,
       "hh3cevtPortSw-10GBASE-BIDI-D-SFP-PLUS": hh3cevtPortSw_10GBASE_BIDI_D_SFP_PLUS,
       "hh3cevtPortSw-QSFPDD-STACK-CONNECTOR": hh3cevtPortSw_QSFPDD_STACK_CONNECTOR,
       "hh3cevtPortSw-QSFPDD-400GBASE-SR8": hh3cevtPortSw_QSFPDD_400GBASE_SR8,
       "hh3cevtPortSw-QSFP28-100GBASE-ZR2": hh3cevtPortSw_QSFP28_100GBASE_ZR2,
       "hh3cevtPortSw-QSFP28-50GBASE-ER": hh3cevtPortSw_QSFP28_50GBASE_ER,
       "hh3cevtPortSw-SFP28-25GBASE-eLR": hh3cevtPortSw_SFP28_25GBASE_eLR,
       "hh3cevtPortSw-QSFP28-100GBASE-ER4-NO-FEC": hh3cevtPortSw_QSFP28_100GBASE_ER4_NO_FEC,
       "hh3cevtPortSw-QSFP28-100GBASE-ZR4": hh3cevtPortSw_QSFP28_100GBASE_ZR4,
       "hh3cevtPortSw-QSFPDD-400GBASE-FR4": hh3cevtPortSw_QSFPDD_400GBASE_FR4,
       "hh3cevtPortSw-QSFP56-200GBASE-FR4": hh3cevtPortSw_QSFP56_200GBASE_FR4,
       "hh3cevtPortSw-QSFP56-200GBASE-SR4": hh3cevtPortSw_QSFP56_200GBASE_SR4,
       "hh3cevtPortSw-QSFP56-200GBASE-AOC": hh3cevtPortSw_QSFP56_200GBASE_AOC,
       "hh3cevtPortSw-DSFP-100GBASE-AOC": hh3cevtPortSw_DSFP_100GBASE_AOC,
       "hh3cevtPortSw-SFP28-25GBASE-CSR": hh3cevtPortSw_SFP28_25GBASE_CSR,
       "hh3cevtPortSw-QSFPDD-UNKNOWN": hh3cevtPortSw_QSFPDD_UNKNOWN,
       "hh3cevtPortSw-QSFPDD-NO-CONNECTOR": hh3cevtPortSw_QSFPDD_NO_CONNECTOR,
       "hh3cevtPortSw-DSFP-UNKNOWN": hh3cevtPortSw_DSFP_UNKNOWN,
       "hh3cevtPortSw-DSFP-NO-CONNECTOR": hh3cevtPortSw_DSFP_NO_CONNECTOR,
       "hh3cevtPortSw-QSFPDD-400GBASE-ZR": hh3cevtPortSw_QSFPDD_400GBASE_ZR,
       "hh3cevtPortSw-QSFPDD-400GBASE-LR8": hh3cevtPortSw_QSFPDD_400GBASE_LR8,
       "hh3cevtStack": hh3cevtStack}
)
