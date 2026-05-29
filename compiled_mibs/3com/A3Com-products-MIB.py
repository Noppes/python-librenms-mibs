# SNMP MIB module (A3Com-products-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\3com\A3Com-products-MIB

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

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1)
)
_TerminalServer_ObjectIdentity = ObjectIdentity
terminalServer = _TerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1)
)
_Cs2500_ObjectIdentity = ObjectIdentity
cs2500 = _Cs2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 1)
)
_Cs2500to_ObjectIdentity = ObjectIdentity
cs2500to = _Cs2500to_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 1, 1)
)
_Cs2500tlo_ObjectIdentity = ObjectIdentity
cs2500tlo = _Cs2500tlo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 1, 2)
)
_Cs2600_ObjectIdentity = ObjectIdentity
cs2600 = _Cs2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 2)
)
_Cs2600to_ObjectIdentity = ObjectIdentity
cs2600to = _Cs2600to_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 2, 1)
)
_Cs2600tlo_ObjectIdentity = ObjectIdentity
cs2600tlo = _Cs2600tlo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 2, 2)
)
_Cs2000_ObjectIdentity = ObjectIdentity
cs2000 = _Cs2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 3)
)
_Cs2000to_ObjectIdentity = ObjectIdentity
cs2000to = _Cs2000to_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 3, 1)
)
_Cs2000tlo_ObjectIdentity = ObjectIdentity
cs2000tlo = _Cs2000tlo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 3, 2)
)
_Cs1_ObjectIdentity = ObjectIdentity
cs1 = _Cs1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 4)
)
_Cs210_ObjectIdentity = ObjectIdentity
cs210 = _Cs210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 5)
)
_Cs2100_ObjectIdentity = ObjectIdentity
cs2100 = _Cs2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 6)
)
_Cs2100to_ObjectIdentity = ObjectIdentity
cs2100to = _Cs2100to_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 6, 1)
)
_Cs2100tlo_ObjectIdentity = ObjectIdentity
cs2100tlo = _Cs2100tlo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 6, 2)
)
_Cs3000_ObjectIdentity = ObjectIdentity
cs3000 = _Cs3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 7)
)
_Cs3000to_ObjectIdentity = ObjectIdentity
cs3000to = _Cs3000to_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 7, 1)
)
_Cs3000tlo_ObjectIdentity = ObjectIdentity
cs3000tlo = _Cs3000tlo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 7, 2)
)
_Cs3100_ObjectIdentity = ObjectIdentity
cs3100 = _Cs3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 8)
)
_Cs3100to_ObjectIdentity = ObjectIdentity
cs3100to = _Cs3100to_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 8, 1)
)
_Cs3100tlo_ObjectIdentity = ObjectIdentity
cs3100tlo = _Cs3100tlo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 8, 2)
)
_Callisto_ObjectIdentity = ObjectIdentity
callisto = _Callisto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 9)
)
_TermServerPlatform_ObjectIdentity = ObjectIdentity
termServerPlatform = _TermServerPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 10)
)
_Series1_ObjectIdentity = ObjectIdentity
series1 = _Series1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 10, 1)
)
_Series200_ObjectIdentity = ObjectIdentity
series200 = _Series200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 10, 2)
)
_CallistoPlatfor_ObjectIdentity = ObjectIdentity
callistoPlatfor = _CallistoPlatfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 10, 3)
)
_Series2500_ObjectIdentity = ObjectIdentity
series2500 = _Series2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 10, 4)
)
_Series3000_ObjectIdentity = ObjectIdentity
series3000 = _Series3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1, 10, 5)
)
_DedicatedBridgeServer_ObjectIdentity = ObjectIdentity
dedicatedBridgeServer = _DedicatedBridgeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 2)
)
_DedicatedRouteServer_ObjectIdentity = ObjectIdentity
dedicatedRouteServer = _DedicatedRouteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 3)
)
_Brouter_ObjectIdentity = ObjectIdentity
brouter = _Brouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4)
)
_Netbuilder1_ObjectIdentity = ObjectIdentity
netbuilder1 = _Netbuilder1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 1)
)
_Netbuilder2_ObjectIdentity = ObjectIdentity
netbuilder2 = _Netbuilder2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 2)
)
_LBridgeECS_ObjectIdentity = ObjectIdentity
lBridgeECS = _LBridgeECS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 3)
)
_NetbuilderTrRA_ObjectIdentity = ObjectIdentity
netbuilderTrRA = _NetbuilderTrRA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4)
)
_NetbuilderTrRAbp_ObjectIdentity = ObjectIdentity
netbuilderTrRAbp = _NetbuilderTrRAbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 1)
)
_NetbuilderTrRAcp_ObjectIdentity = ObjectIdentity
netbuilderTrRAcp = _NetbuilderTrRAcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 2)
)
_NetbuilderTrRAxw_ObjectIdentity = ObjectIdentity
netbuilderTrRAxw = _NetbuilderTrRAxw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 3)
)
_NetbuilderTrRAcx_ObjectIdentity = ObjectIdentity
netbuilderTrRAcx = _NetbuilderTrRAcx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 4)
)
_NetbuilderTrRAba_ObjectIdentity = ObjectIdentity
netbuilderTrRAba = _NetbuilderTrRAba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 5)
)
_NetbuilderTrRAar_ObjectIdentity = ObjectIdentity
netbuilderTrRAar = _NetbuilderTrRAar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 6)
)
_NetbuilderTrRAsn_ObjectIdentity = ObjectIdentity
netbuilderTrRAsn = _NetbuilderTrRAsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 7)
)
_NetbuilderTrRArb_ObjectIdentity = ObjectIdentity
netbuilderTrRArb = _NetbuilderTrRArb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 8)
)
_NetbuilderTrRAff_ObjectIdentity = ObjectIdentity
netbuilderTrRAff = _NetbuilderTrRAff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 9)
)
_NetbuidlerTrRAcf_ObjectIdentity = ObjectIdentity
netbuidlerTrRAcf = _NetbuidlerTrRAcf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 10)
)
_NetbuilderTrRAbx_ObjectIdentity = ObjectIdentity
netbuilderTrRAbx = _NetbuilderTrRAbx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 11)
)
_NetbuilderTrRAappn_ObjectIdentity = ObjectIdentity
netbuilderTrRAappn = _NetbuilderTrRAappn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 12)
)
_NetbuilderTrRAlm_ObjectIdentity = ObjectIdentity
netbuilderTrRAlm = _NetbuilderTrRAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 13)
)
_NetbuilderTrRAlt_ObjectIdentity = ObjectIdentity
netbuilderTrRAlt = _NetbuilderTrRAlt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 14)
)
_NetbuilderTrRAwm_ObjectIdentity = ObjectIdentity
netbuilderTrRAwm = _NetbuilderTrRAwm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 15)
)
_NetbuilderTrRAwt_ObjectIdentity = ObjectIdentity
netbuilderTrRAwt = _NetbuilderTrRAwt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 16)
)
_NetbuilderTrRAae_ObjectIdentity = ObjectIdentity
netbuilderTrRAae = _NetbuilderTrRAae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 17)
)
_NetbuilderTrRAap_ObjectIdentity = ObjectIdentity
netbuilderTrRAap = _NetbuilderTrRAap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 18)
)
_NetbuilderTrRAan_ObjectIdentity = ObjectIdentity
netbuilderTrRAan = _NetbuilderTrRAan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 19)
)
_NetbuilderTrRAla_ObjectIdentity = ObjectIdentity
netbuilderTrRAla = _NetbuilderTrRAla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 20)
)
_NetbuilderTrRAwa_ObjectIdentity = ObjectIdentity
netbuilderTrRAwa = _NetbuilderTrRAwa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 21)
)
_NetbuilderTrRAaa_ObjectIdentity = ObjectIdentity
netbuilderTrRAaa = _NetbuilderTrRAaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 22)
)
_NetbuilderTrRAab_ObjectIdentity = ObjectIdentity
netbuilderTrRAab = _NetbuilderTrRAab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 23)
)
_NetbuilderTrRAbf_ObjectIdentity = ObjectIdentity
netbuilderTrRAbf = _NetbuilderTrRAbf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 4, 24)
)
_BrouterPlatform_ObjectIdentity = ObjectIdentity
brouterPlatform = _BrouterPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5)
)
_Nb1_ObjectIdentity = ObjectIdentity
nb1 = _Nb1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 1)
)
_Nb2_ObjectIdentity = ObjectIdentity
nb2 = _Nb2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 2)
)
_NbroPlatform_ObjectIdentity = ObjectIdentity
nbroPlatform = _NbroPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 3)
)
_CasperPlatform_ObjectIdentity = ObjectIdentity
casperPlatform = _CasperPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 4)
)
_SpectreIsdnPform_ObjectIdentity = ObjectIdentity
spectreIsdnPform = _SpectreIsdnPform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 5)
)
_SpectreIITr_ObjectIdentity = ObjectIdentity
spectreIITr = _SpectreIITr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 6)
)
_NbroIITrIsdnPform_ObjectIdentity = ObjectIdentity
nbroIITrIsdnPform = _NbroIITrIsdnPform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 7)
)
_NbroIIEthPform_ObjectIdentity = ObjectIdentity
nbroIIEthPform = _NbroIIEthPform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 8)
)
_NbroIIEthIsdnPform_ObjectIdentity = ObjectIdentity
nbroIIEthIsdnPform = _NbroIIEthIsdnPform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 9)
)
_OcGen_ObjectIdentity = ObjectIdentity
ocGen = _OcGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 10)
)
_OcIsdnSt_ObjectIdentity = ObjectIdentity
ocIsdnSt = _OcIsdnSt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 11)
)
_OcIsdnU_ObjectIdentity = ObjectIdentity
ocIsdnU = _OcIsdnU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 12)
)
_OcCsuDsu_ObjectIdentity = ObjectIdentity
ocCsuDsu = _OcCsuDsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 13)
)
_OcWanOnly_ObjectIdentity = ObjectIdentity
ocWanOnly = _OcWanOnly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 14)
)
_OcT1CsuDsu_ObjectIdentity = ObjectIdentity
ocT1CsuDsu = _OcT1CsuDsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 15)
)
_IntrepidGen_ObjectIdentity = ObjectIdentity
intrepidGen = _IntrepidGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 16)
)
_IntrepidIsdnSt_ObjectIdentity = ObjectIdentity
intrepidIsdnSt = _IntrepidIsdnSt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 17)
)
_IntrepidIsdnU_ObjectIdentity = ObjectIdentity
intrepidIsdnU = _IntrepidIsdnU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 18)
)
_Intrepid56kCsuDsu_ObjectIdentity = ObjectIdentity
intrepid56kCsuDsu = _Intrepid56kCsuDsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 19)
)
_IntrepidT1CsuDsu_ObjectIdentity = ObjectIdentity
intrepidT1CsuDsu = _IntrepidT1CsuDsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 20)
)
_Oc1x2_ObjectIdentity = ObjectIdentity
oc1x2 = _Oc1x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 21)
)
_ScorePform_ObjectIdentity = ObjectIdentity
scorePform = _ScorePform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 22)
)
_BlueridgeGen_ObjectIdentity = ObjectIdentity
blueridgeGen = _BlueridgeGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 23)
)
_BlueridgeIsdnSt_ObjectIdentity = ObjectIdentity
blueridgeIsdnSt = _BlueridgeIsdnSt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 24)
)
_BlueridgeIsdnU_ObjectIdentity = ObjectIdentity
blueridgeIsdnU = _BlueridgeIsdnU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 25)
)
_Blueridge56kCsuDsu_ObjectIdentity = ObjectIdentity
blueridge56kCsuDsu = _Blueridge56kCsuDsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 26)
)
_BlueridgeT1CsuCsu_ObjectIdentity = ObjectIdentity
blueridgeT1CsuCsu = _BlueridgeT1CsuCsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 27)
)
_ScoreLanToLan_ObjectIdentity = ObjectIdentity
scoreLanToLan = _ScoreLanToLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 28)
)
_ScoreFlex_ObjectIdentity = ObjectIdentity
scoreFlex = _ScoreFlex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 29)
)
_ScoreFlexPri_ObjectIdentity = ObjectIdentity
scoreFlexPri = _ScoreFlexPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 30)
)
_ScoreDualT3_ObjectIdentity = ObjectIdentity
scoreDualT3 = _ScoreDualT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 31)
)
_ScoreDualE3_ObjectIdentity = ObjectIdentity
scoreDualE3 = _ScoreDualE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 32)
)
_ScoreDualPri_ObjectIdentity = ObjectIdentity
scoreDualPri = _ScoreDualPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 33)
)
_CopperHead_ObjectIdentity = ObjectIdentity
copperHead = _CopperHead_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 34)
)
_ScoreMMATM_ObjectIdentity = ObjectIdentity
scoreMMATM = _ScoreMMATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 35)
)
_ScoreSMATM_ObjectIdentity = ObjectIdentity
scoreSMATM = _ScoreSMATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 36)
)
_ScoreFlexPri2port_ObjectIdentity = ObjectIdentity
scoreFlexPri2port = _ScoreFlexPri2port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 37)
)
_Oc10St_ObjectIdentity = ObjectIdentity
oc10St = _Oc10St_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 38)
)
_Oc10U_ObjectIdentity = ObjectIdentity
oc10U = _Oc10U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 39)
)
_ScorePri4port_ObjectIdentity = ObjectIdentity
scorePri4port = _ScorePri4port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 40)
)
_EasterST_ObjectIdentity = ObjectIdentity
easterST = _EasterST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 41)
)
_EasterU_ObjectIdentity = ObjectIdentity
easterU = _EasterU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 5, 42)
)
_NetbuilderRem_ObjectIdentity = ObjectIdentity
netbuilderRem = _NetbuilderRem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6)
)
_NetbuilderRemBp_ObjectIdentity = ObjectIdentity
netbuilderRemBp = _NetbuilderRemBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 1)
)
_NetbuilderRemCp_ObjectIdentity = ObjectIdentity
netbuilderRemCp = _NetbuilderRemCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 2)
)
_NetbuilderRemXw_ObjectIdentity = ObjectIdentity
netbuilderRemXw = _NetbuilderRemXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 3)
)
_NetbuilderRemCx_ObjectIdentity = ObjectIdentity
netbuilderRemCx = _NetbuilderRemCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 4)
)
_NetbuilderRemBa_ObjectIdentity = ObjectIdentity
netbuilderRemBa = _NetbuilderRemBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 5)
)
_NetbuilderRemAr_ObjectIdentity = ObjectIdentity
netbuilderRemAr = _NetbuilderRemAr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 6)
)
_NetbuilderRemSn_ObjectIdentity = ObjectIdentity
netbuilderRemSn = _NetbuilderRemSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 7)
)
_NetbuilderRemRb_ObjectIdentity = ObjectIdentity
netbuilderRemRb = _NetbuilderRemRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 8)
)
_NetbuilderRemFf_ObjectIdentity = ObjectIdentity
netbuilderRemFf = _NetbuilderRemFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 9)
)
_NetbuilderRemCf_ObjectIdentity = ObjectIdentity
netbuilderRemCf = _NetbuilderRemCf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 10)
)
_NetbuilderRemBx_ObjectIdentity = ObjectIdentity
netbuilderRemBx = _NetbuilderRemBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 11)
)
_NetbuilderRemAppn_ObjectIdentity = ObjectIdentity
netbuilderRemAppn = _NetbuilderRemAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 12)
)
_NetbuilderRemLm_ObjectIdentity = ObjectIdentity
netbuilderRemLm = _NetbuilderRemLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 13)
)
_NetbuilderRemLt_ObjectIdentity = ObjectIdentity
netbuilderRemLt = _NetbuilderRemLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 14)
)
_NetbuilderRemWm_ObjectIdentity = ObjectIdentity
netbuilderRemWm = _NetbuilderRemWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 15)
)
_NetbuilderRemWt_ObjectIdentity = ObjectIdentity
netbuilderRemWt = _NetbuilderRemWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 16)
)
_NetbuilderRemAe_ObjectIdentity = ObjectIdentity
netbuilderRemAe = _NetbuilderRemAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 17)
)
_NetbuilderRemAp_ObjectIdentity = ObjectIdentity
netbuilderRemAp = _NetbuilderRemAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 18)
)
_NetbuilderRemAn_ObjectIdentity = ObjectIdentity
netbuilderRemAn = _NetbuilderRemAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 19)
)
_NetbuilderRemLa_ObjectIdentity = ObjectIdentity
netbuilderRemLa = _NetbuilderRemLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 20)
)
_NetbuilderRemWa_ObjectIdentity = ObjectIdentity
netbuilderRemWa = _NetbuilderRemWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 21)
)
_NetbuilderRemAa_ObjectIdentity = ObjectIdentity
netbuilderRemAa = _NetbuilderRemAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 22)
)
_NetbuilderRemAb_ObjectIdentity = ObjectIdentity
netbuilderRemAb = _NetbuilderRemAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 23)
)
_NetbuilderRemBf_ObjectIdentity = ObjectIdentity
netbuilderRemBf = _NetbuilderRemBf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 6, 24)
)
_NetbuilderRA_ObjectIdentity = ObjectIdentity
netbuilderRA = _NetbuilderRA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7)
)
_NetbuilderRAbp_ObjectIdentity = ObjectIdentity
netbuilderRAbp = _NetbuilderRAbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 1)
)
_NetbuilderRAcp_ObjectIdentity = ObjectIdentity
netbuilderRAcp = _NetbuilderRAcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 2)
)
_NetbuilderRAxw_ObjectIdentity = ObjectIdentity
netbuilderRAxw = _NetbuilderRAxw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 3)
)
_NetbuilderRAcx_ObjectIdentity = ObjectIdentity
netbuilderRAcx = _NetbuilderRAcx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 4)
)
_NetbuilderRAba_ObjectIdentity = ObjectIdentity
netbuilderRAba = _NetbuilderRAba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 5)
)
_NetbuilderRAar_ObjectIdentity = ObjectIdentity
netbuilderRAar = _NetbuilderRAar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 6)
)
_NetbuilderRAsn_ObjectIdentity = ObjectIdentity
netbuilderRAsn = _NetbuilderRAsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 7)
)
_NetbuilderRArb_ObjectIdentity = ObjectIdentity
netbuilderRArb = _NetbuilderRArb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 8)
)
_NetbuilderRAff_ObjectIdentity = ObjectIdentity
netbuilderRAff = _NetbuilderRAff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 9)
)
_NetbuilderRAcf_ObjectIdentity = ObjectIdentity
netbuilderRAcf = _NetbuilderRAcf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 10)
)
_NetbuilderRAbx_ObjectIdentity = ObjectIdentity
netbuilderRAbx = _NetbuilderRAbx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 11)
)
_NetbuilderRAappn_ObjectIdentity = ObjectIdentity
netbuilderRAappn = _NetbuilderRAappn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 12)
)
_NetbuilderRAlm_ObjectIdentity = ObjectIdentity
netbuilderRAlm = _NetbuilderRAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 13)
)
_NetbuilderRAlt_ObjectIdentity = ObjectIdentity
netbuilderRAlt = _NetbuilderRAlt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 14)
)
_NetbuilderRAwm_ObjectIdentity = ObjectIdentity
netbuilderRAwm = _NetbuilderRAwm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 15)
)
_NetbuilderRAwt_ObjectIdentity = ObjectIdentity
netbuilderRAwt = _NetbuilderRAwt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 16)
)
_NetbuilderRAae_ObjectIdentity = ObjectIdentity
netbuilderRAae = _NetbuilderRAae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 17)
)
_NetbuilderRAap_ObjectIdentity = ObjectIdentity
netbuilderRAap = _NetbuilderRAap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 18)
)
_NetbuilderRAan_ObjectIdentity = ObjectIdentity
netbuilderRAan = _NetbuilderRAan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 19)
)
_NetbuilderRAla_ObjectIdentity = ObjectIdentity
netbuilderRAla = _NetbuilderRAla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 20)
)
_NetbuilderRAwa_ObjectIdentity = ObjectIdentity
netbuilderRAwa = _NetbuilderRAwa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 21)
)
_NetbuilderRAaa_ObjectIdentity = ObjectIdentity
netbuilderRAaa = _NetbuilderRAaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 22)
)
_NetbuilderRAab_ObjectIdentity = ObjectIdentity
netbuilderRAab = _NetbuilderRAab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 23)
)
_NetbuilderRAbf_ObjectIdentity = ObjectIdentity
netbuilderRAbf = _NetbuilderRAbf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 7, 24)
)
_NetbuilderRC_ObjectIdentity = ObjectIdentity
netbuilderRC = _NetbuilderRC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8)
)
_NetbuilderRCbp_ObjectIdentity = ObjectIdentity
netbuilderRCbp = _NetbuilderRCbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 1)
)
_NetbuilderRCcp_ObjectIdentity = ObjectIdentity
netbuilderRCcp = _NetbuilderRCcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 2)
)
_NetbuilderRCxw_ObjectIdentity = ObjectIdentity
netbuilderRCxw = _NetbuilderRCxw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 3)
)
_NetbuilderRCcx_ObjectIdentity = ObjectIdentity
netbuilderRCcx = _NetbuilderRCcx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 4)
)
_NetbuilderRCba_ObjectIdentity = ObjectIdentity
netbuilderRCba = _NetbuilderRCba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 5)
)
_NetbuilderRCar_ObjectIdentity = ObjectIdentity
netbuilderRCar = _NetbuilderRCar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 6)
)
_NetbuilderRCsn_ObjectIdentity = ObjectIdentity
netbuilderRCsn = _NetbuilderRCsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 7)
)
_NetbuilderRCrb_ObjectIdentity = ObjectIdentity
netbuilderRCrb = _NetbuilderRCrb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 8)
)
_NetbuilderRCff_ObjectIdentity = ObjectIdentity
netbuilderRCff = _NetbuilderRCff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 9)
)
_NetbuilderRCcf_ObjectIdentity = ObjectIdentity
netbuilderRCcf = _NetbuilderRCcf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 10)
)
_NetbuilderRCbx_ObjectIdentity = ObjectIdentity
netbuilderRCbx = _NetbuilderRCbx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 11)
)
_NetbuilderRCappn_ObjectIdentity = ObjectIdentity
netbuilderRCappn = _NetbuilderRCappn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 12)
)
_NetbuilderRClm_ObjectIdentity = ObjectIdentity
netbuilderRClm = _NetbuilderRClm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 13)
)
_NetbuilderRClt_ObjectIdentity = ObjectIdentity
netbuilderRClt = _NetbuilderRClt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 14)
)
_NetbuilderRCwm_ObjectIdentity = ObjectIdentity
netbuilderRCwm = _NetbuilderRCwm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 15)
)
_NetbuilderRCwt_ObjectIdentity = ObjectIdentity
netbuilderRCwt = _NetbuilderRCwt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 16)
)
_NetbuilderRCae_ObjectIdentity = ObjectIdentity
netbuilderRCae = _NetbuilderRCae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 17)
)
_NetbuilderRCap_ObjectIdentity = ObjectIdentity
netbuilderRCap = _NetbuilderRCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 18)
)
_NetbuilderRCan_ObjectIdentity = ObjectIdentity
netbuilderRCan = _NetbuilderRCan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 19)
)
_NetbuilderRCla_ObjectIdentity = ObjectIdentity
netbuilderRCla = _NetbuilderRCla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 20)
)
_NetbuilderRCwa_ObjectIdentity = ObjectIdentity
netbuilderRCwa = _NetbuilderRCwa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 21)
)
_NetbuilderRCaa_ObjectIdentity = ObjectIdentity
netbuilderRCaa = _NetbuilderRCaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 22)
)
_NetbuilderRCab_ObjectIdentity = ObjectIdentity
netbuilderRCab = _NetbuilderRCab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 23)
)
_NetbuilderRCbf_ObjectIdentity = ObjectIdentity
netbuilderRCbf = _NetbuilderRCbf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 8, 24)
)
_NetbuilderTrRem_ObjectIdentity = ObjectIdentity
netbuilderTrRem = _NetbuilderTrRem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9)
)
_NetbuilderTrRemBp_ObjectIdentity = ObjectIdentity
netbuilderTrRemBp = _NetbuilderTrRemBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 1)
)
_NetbuilderTrRemCp_ObjectIdentity = ObjectIdentity
netbuilderTrRemCp = _NetbuilderTrRemCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 2)
)
_NetbuilderTrRemXw_ObjectIdentity = ObjectIdentity
netbuilderTrRemXw = _NetbuilderTrRemXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 3)
)
_NetbuilderTrRemCx_ObjectIdentity = ObjectIdentity
netbuilderTrRemCx = _NetbuilderTrRemCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 4)
)
_NetbuilderTrRemBa_ObjectIdentity = ObjectIdentity
netbuilderTrRemBa = _NetbuilderTrRemBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 5)
)
_NetbuilderTrRemAr_ObjectIdentity = ObjectIdentity
netbuilderTrRemAr = _NetbuilderTrRemAr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 6)
)
_NetbuilderTrRemSn_ObjectIdentity = ObjectIdentity
netbuilderTrRemSn = _NetbuilderTrRemSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 7)
)
_NetbuilderTrRemRb_ObjectIdentity = ObjectIdentity
netbuilderTrRemRb = _NetbuilderTrRemRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 8)
)
_NetbuilderTrRemFf_ObjectIdentity = ObjectIdentity
netbuilderTrRemFf = _NetbuilderTrRemFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 9)
)
_NetbuilderTrRemCf_ObjectIdentity = ObjectIdentity
netbuilderTrRemCf = _NetbuilderTrRemCf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 10)
)
_NetbuilderTrRemBx_ObjectIdentity = ObjectIdentity
netbuilderTrRemBx = _NetbuilderTrRemBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 11)
)
_NetbuilderTrRemAppn_ObjectIdentity = ObjectIdentity
netbuilderTrRemAppn = _NetbuilderTrRemAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 12)
)
_NetbuilderTrRemLm_ObjectIdentity = ObjectIdentity
netbuilderTrRemLm = _NetbuilderTrRemLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 13)
)
_NetbuilderTrRemLt_ObjectIdentity = ObjectIdentity
netbuilderTrRemLt = _NetbuilderTrRemLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 14)
)
_NetbuilderTrRemWm_ObjectIdentity = ObjectIdentity
netbuilderTrRemWm = _NetbuilderTrRemWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 15)
)
_NetbuilderTrRemWt_ObjectIdentity = ObjectIdentity
netbuilderTrRemWt = _NetbuilderTrRemWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 16)
)
_NetbuilderTrRemAe_ObjectIdentity = ObjectIdentity
netbuilderTrRemAe = _NetbuilderTrRemAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 17)
)
_NetbuilderTrRemAp_ObjectIdentity = ObjectIdentity
netbuilderTrRemAp = _NetbuilderTrRemAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 18)
)
_NetbuilderTrRemAn_ObjectIdentity = ObjectIdentity
netbuilderTrRemAn = _NetbuilderTrRemAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 19)
)
_NetbuilderTrRemLa_ObjectIdentity = ObjectIdentity
netbuilderTrRemLa = _NetbuilderTrRemLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 20)
)
_NetbuilderTrRemWa_ObjectIdentity = ObjectIdentity
netbuilderTrRemWa = _NetbuilderTrRemWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 21)
)
_NetbuilderTrRemAa_ObjectIdentity = ObjectIdentity
netbuilderTrRemAa = _NetbuilderTrRemAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 22)
)
_NetbuilderTrRemAb_ObjectIdentity = ObjectIdentity
netbuilderTrRemAb = _NetbuilderTrRemAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 23)
)
_NetbuilderTrRemBf_ObjectIdentity = ObjectIdentity
netbuilderTrRemBf = _NetbuilderTrRemBf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 9, 24)
)
_NetbuilderTrRC_ObjectIdentity = ObjectIdentity
netbuilderTrRC = _NetbuilderTrRC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10)
)
_NetbuilderTrRCbp_ObjectIdentity = ObjectIdentity
netbuilderTrRCbp = _NetbuilderTrRCbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 1)
)
_NetbuilderTrRCcp_ObjectIdentity = ObjectIdentity
netbuilderTrRCcp = _NetbuilderTrRCcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 2)
)
_NetbuilderTrRCxw_ObjectIdentity = ObjectIdentity
netbuilderTrRCxw = _NetbuilderTrRCxw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 3)
)
_NetbuilderTrRCcx_ObjectIdentity = ObjectIdentity
netbuilderTrRCcx = _NetbuilderTrRCcx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 4)
)
_NetbuilderTrRCba_ObjectIdentity = ObjectIdentity
netbuilderTrRCba = _NetbuilderTrRCba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 5)
)
_NetbuilderTrRCar_ObjectIdentity = ObjectIdentity
netbuilderTrRCar = _NetbuilderTrRCar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 6)
)
_NetbuilderTrRCsn_ObjectIdentity = ObjectIdentity
netbuilderTrRCsn = _NetbuilderTrRCsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 7)
)
_NetbuilderTrRCrb_ObjectIdentity = ObjectIdentity
netbuilderTrRCrb = _NetbuilderTrRCrb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 8)
)
_NetbuilderTrRCff_ObjectIdentity = ObjectIdentity
netbuilderTrRCff = _NetbuilderTrRCff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 9)
)
_NetbuilderTrRCcf_ObjectIdentity = ObjectIdentity
netbuilderTrRCcf = _NetbuilderTrRCcf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 10)
)
_NetbuilderTrRCbx_ObjectIdentity = ObjectIdentity
netbuilderTrRCbx = _NetbuilderTrRCbx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 11)
)
_NetbuilderTrRCappn_ObjectIdentity = ObjectIdentity
netbuilderTrRCappn = _NetbuilderTrRCappn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 12)
)
_NetbuilderTrRClm_ObjectIdentity = ObjectIdentity
netbuilderTrRClm = _NetbuilderTrRClm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 13)
)
_NetbuilderTrRClt_ObjectIdentity = ObjectIdentity
netbuilderTrRClt = _NetbuilderTrRClt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 14)
)
_NetbuilderTrRCwm_ObjectIdentity = ObjectIdentity
netbuilderTrRCwm = _NetbuilderTrRCwm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 15)
)
_NetbuilderTrRCwt_ObjectIdentity = ObjectIdentity
netbuilderTrRCwt = _NetbuilderTrRCwt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 16)
)
_NetbuilderTrRCae_ObjectIdentity = ObjectIdentity
netbuilderTrRCae = _NetbuilderTrRCae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 17)
)
_NetbuilderTrRCap_ObjectIdentity = ObjectIdentity
netbuilderTrRCap = _NetbuilderTrRCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 18)
)
_NetbuilderTrRCan_ObjectIdentity = ObjectIdentity
netbuilderTrRCan = _NetbuilderTrRCan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 19)
)
_NetbuilderTrRCla_ObjectIdentity = ObjectIdentity
netbuilderTrRCla = _NetbuilderTrRCla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 20)
)
_NetbuilderTrRCwa_ObjectIdentity = ObjectIdentity
netbuilderTrRCwa = _NetbuilderTrRCwa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 21)
)
_NetbuilderTrRCaa_ObjectIdentity = ObjectIdentity
netbuilderTrRCaa = _NetbuilderTrRCaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 22)
)
_NetbuilderTrRCab_ObjectIdentity = ObjectIdentity
netbuilderTrRCab = _NetbuilderTrRCab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 23)
)
_NetbuilderTrRCbf_ObjectIdentity = ObjectIdentity
netbuilderTrRCbf = _NetbuilderTrRCbf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 10, 24)
)
_Nb2_4_ObjectIdentity = ObjectIdentity
nb2_4 = _Nb2_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11)
)
_Nb2_4Bp_ObjectIdentity = ObjectIdentity
nb2_4Bp = _Nb2_4Bp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 1)
)
_Nb2_4Cp_ObjectIdentity = ObjectIdentity
nb2_4Cp = _Nb2_4Cp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 2)
)
_Nb2_4Xw_ObjectIdentity = ObjectIdentity
nb2_4Xw = _Nb2_4Xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 3)
)
_Nb2_4Cx_ObjectIdentity = ObjectIdentity
nb2_4Cx = _Nb2_4Cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 4)
)
_Nb2_4Ba_ObjectIdentity = ObjectIdentity
nb2_4Ba = _Nb2_4Ba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 5)
)
_Nb2_4Ar_ObjectIdentity = ObjectIdentity
nb2_4Ar = _Nb2_4Ar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 6)
)
_Nb2_4Sn_ObjectIdentity = ObjectIdentity
nb2_4Sn = _Nb2_4Sn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 7)
)
_Nb2_4Rb_ObjectIdentity = ObjectIdentity
nb2_4Rb = _Nb2_4Rb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 8)
)
_Nb2_4Ff_ObjectIdentity = ObjectIdentity
nb2_4Ff = _Nb2_4Ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 9)
)
_Nb2_4Cf_ObjectIdentity = ObjectIdentity
nb2_4Cf = _Nb2_4Cf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 10)
)
_Nb2_4Bx_ObjectIdentity = ObjectIdentity
nb2_4Bx = _Nb2_4Bx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 11)
)
_Nb2_4Appn_ObjectIdentity = ObjectIdentity
nb2_4Appn = _Nb2_4Appn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 12)
)
_Nb2_4Lm_ObjectIdentity = ObjectIdentity
nb2_4Lm = _Nb2_4Lm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 13)
)
_Nb2_4Lt_ObjectIdentity = ObjectIdentity
nb2_4Lt = _Nb2_4Lt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 14)
)
_Nb2_4Wm_ObjectIdentity = ObjectIdentity
nb2_4Wm = _Nb2_4Wm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 15)
)
_Nb2_4Wt_ObjectIdentity = ObjectIdentity
nb2_4Wt = _Nb2_4Wt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 16)
)
_Nb2_4Ae_ObjectIdentity = ObjectIdentity
nb2_4Ae = _Nb2_4Ae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 17)
)
_Nb2_4Ap_ObjectIdentity = ObjectIdentity
nb2_4Ap = _Nb2_4Ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 18)
)
_Nb2_4An_ObjectIdentity = ObjectIdentity
nb2_4An = _Nb2_4An_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 19)
)
_Nb2_4La_ObjectIdentity = ObjectIdentity
nb2_4La = _Nb2_4La_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 20)
)
_Nb2_4Wa_ObjectIdentity = ObjectIdentity
nb2_4Wa = _Nb2_4Wa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 21)
)
_Nb2_4Aa_ObjectIdentity = ObjectIdentity
nb2_4Aa = _Nb2_4Aa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 22)
)
_Nb2_4Ab_ObjectIdentity = ObjectIdentity
nb2_4Ab = _Nb2_4Ab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 23)
)
_Nb2_4Bf_ObjectIdentity = ObjectIdentity
nb2_4Bf = _Nb2_4Bf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 11, 24)
)
_Nb2_8_ObjectIdentity = ObjectIdentity
nb2_8 = _Nb2_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12)
)
_Nb2_8Bp_ObjectIdentity = ObjectIdentity
nb2_8Bp = _Nb2_8Bp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 1)
)
_Nb2_8Cp_ObjectIdentity = ObjectIdentity
nb2_8Cp = _Nb2_8Cp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 2)
)
_Nb2_8Xw_ObjectIdentity = ObjectIdentity
nb2_8Xw = _Nb2_8Xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 3)
)
_Nb2_8Cx_ObjectIdentity = ObjectIdentity
nb2_8Cx = _Nb2_8Cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 4)
)
_Nb2_8Ba_ObjectIdentity = ObjectIdentity
nb2_8Ba = _Nb2_8Ba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 5)
)
_Nb2_8Ar_ObjectIdentity = ObjectIdentity
nb2_8Ar = _Nb2_8Ar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 6)
)
_Nb2_8Sn_ObjectIdentity = ObjectIdentity
nb2_8Sn = _Nb2_8Sn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 7)
)
_Nb2_8Rb_ObjectIdentity = ObjectIdentity
nb2_8Rb = _Nb2_8Rb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 8)
)
_Nb2_8Ff_ObjectIdentity = ObjectIdentity
nb2_8Ff = _Nb2_8Ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 9)
)
_Nb2_8Cf_ObjectIdentity = ObjectIdentity
nb2_8Cf = _Nb2_8Cf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 10)
)
_Nb2_8Bx_ObjectIdentity = ObjectIdentity
nb2_8Bx = _Nb2_8Bx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 11)
)
_Nb2_8Appn_ObjectIdentity = ObjectIdentity
nb2_8Appn = _Nb2_8Appn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 12)
)
_Nb2_8Lm_ObjectIdentity = ObjectIdentity
nb2_8Lm = _Nb2_8Lm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 13)
)
_Nb2_8Lt_ObjectIdentity = ObjectIdentity
nb2_8Lt = _Nb2_8Lt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 14)
)
_Nb2_8Wm_ObjectIdentity = ObjectIdentity
nb2_8Wm = _Nb2_8Wm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 15)
)
_Nb2_8Wt_ObjectIdentity = ObjectIdentity
nb2_8Wt = _Nb2_8Wt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 16)
)
_Nb2_8Ae_ObjectIdentity = ObjectIdentity
nb2_8Ae = _Nb2_8Ae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 17)
)
_Nb2_8Ap_ObjectIdentity = ObjectIdentity
nb2_8Ap = _Nb2_8Ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 18)
)
_Nb2_8An_ObjectIdentity = ObjectIdentity
nb2_8An = _Nb2_8An_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 19)
)
_Nb2_8La_ObjectIdentity = ObjectIdentity
nb2_8La = _Nb2_8La_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 20)
)
_Nb2_8Wa_ObjectIdentity = ObjectIdentity
nb2_8Wa = _Nb2_8Wa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 21)
)
_Nb2_8Aa_ObjectIdentity = ObjectIdentity
nb2_8Aa = _Nb2_8Aa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 22)
)
_Nb2_8Ab_ObjectIdentity = ObjectIdentity
nb2_8Ab = _Nb2_8Ab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 23)
)
_Nb2_8Bf_ObjectIdentity = ObjectIdentity
nb2_8Bf = _Nb2_8Bf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 12, 24)
)
_Nbro_ObjectIdentity = ObjectIdentity
nbro = _Nbro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13)
)
_NbroBp_ObjectIdentity = ObjectIdentity
nbroBp = _NbroBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 1)
)
_NbroCp_ObjectIdentity = ObjectIdentity
nbroCp = _NbroCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 2)
)
_NbroXw_ObjectIdentity = ObjectIdentity
nbroXw = _NbroXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 3)
)
_NbroCx_ObjectIdentity = ObjectIdentity
nbroCx = _NbroCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 4)
)
_Nbro201_ObjectIdentity = ObjectIdentity
nbro201 = _Nbro201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 5)
)
_NbroAr_ObjectIdentity = ObjectIdentity
nbroAr = _NbroAr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 6)
)
_NbroSn_ObjectIdentity = ObjectIdentity
nbroSn = _NbroSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 7)
)
_Nbro200_ObjectIdentity = ObjectIdentity
nbro200 = _Nbro200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 8)
)
_NbroFf_ObjectIdentity = ObjectIdentity
nbroFf = _NbroFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 9)
)
_NbroCf_ObjectIdentity = ObjectIdentity
nbroCf = _NbroCf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 10)
)
_NbroBx_ObjectIdentity = ObjectIdentity
nbroBx = _NbroBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 11)
)
_NbroAppn_ObjectIdentity = ObjectIdentity
nbroAppn = _NbroAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 12)
)
_NbroLm_ObjectIdentity = ObjectIdentity
nbroLm = _NbroLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 13)
)
_NbroLt_ObjectIdentity = ObjectIdentity
nbroLt = _NbroLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 14)
)
_NbroWm_ObjectIdentity = ObjectIdentity
nbroWm = _NbroWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 15)
)
_NbroWt_ObjectIdentity = ObjectIdentity
nbroWt = _NbroWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 16)
)
_NbroAe_ObjectIdentity = ObjectIdentity
nbroAe = _NbroAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 17)
)
_NbroAp_ObjectIdentity = ObjectIdentity
nbroAp = _NbroAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 18)
)
_NbroAn_ObjectIdentity = ObjectIdentity
nbroAn = _NbroAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 19)
)
_NbroLa_ObjectIdentity = ObjectIdentity
nbroLa = _NbroLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 20)
)
_NbroWa_ObjectIdentity = ObjectIdentity
nbroWa = _NbroWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 21)
)
_Nbro224_ObjectIdentity = ObjectIdentity
nbro224 = _Nbro224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 22)
)
_NbroAb_ObjectIdentity = ObjectIdentity
nbroAb = _NbroAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 23)
)
_Nbro223_ObjectIdentity = ObjectIdentity
nbro223 = _Nbro223_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 13, 24)
)
_BrouterBoards_ObjectIdentity = ObjectIdentity
brouterBoards = _BrouterBoards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 1)
)
_FddiPhy_ObjectIdentity = ObjectIdentity
fddiPhy = _FddiPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 2)
)
_FddiMac_ObjectIdentity = ObjectIdentity
fddiMac = _FddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 3)
)
_Hss_ObjectIdentity = ObjectIdentity
hss = _Hss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 4)
)
_TokenRingBrd_ObjectIdentity = ObjectIdentity
tokenRingBrd = _TokenRingBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 5)
)
_HssG703_ObjectIdentity = ObjectIdentity
hssG703 = _HssG703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 6)
)
_HssRS449_ObjectIdentity = ObjectIdentity
hssRS449 = _HssRS449_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 7)
)
_T3HSSI_ObjectIdentity = ObjectIdentity
t3HSSI = _T3HSSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 8)
)
_DualEth_ObjectIdentity = ObjectIdentity
dualEth = _DualEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 9)
)
_Cec_ObjectIdentity = ObjectIdentity
cec = _Cec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 10)
)
_FddiPhySm_ObjectIdentity = ObjectIdentity
fddiPhySm = _FddiPhySm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 11)
)
_FddiPhyMmSm_ObjectIdentity = ObjectIdentity
fddiPhyMmSm = _FddiPhyMmSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 12)
)
_FddiPhySmMm_ObjectIdentity = ObjectIdentity
fddiPhySmMm = _FddiPhySmMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 13)
)
_Hdwan_ObjectIdentity = ObjectIdentity
hdwan = _Hdwan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 14)
)
_Hdwan449_ObjectIdentity = ObjectIdentity
hdwan449 = _Hdwan449_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 15)
)
_Hdwan232_ObjectIdentity = ObjectIdentity
hdwan232 = _Hdwan232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 16)
)
_Mp6Eth_ObjectIdentity = ObjectIdentity
mp6Eth = _Mp6Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 17)
)
_TrPlus_ObjectIdentity = ObjectIdentity
trPlus = _TrPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 18)
)
_MacPlus_ObjectIdentity = ObjectIdentity
macPlus = _MacPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 19)
)
_CecStar_ObjectIdentity = ObjectIdentity
cecStar = _CecStar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 20)
)
_IsdnBri_ObjectIdentity = ObjectIdentity
isdnBri = _IsdnBri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 21)
)
_IsdnPri_ObjectIdentity = ObjectIdentity
isdnPri = _IsdnPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 22)
)
_MpAtm_ObjectIdentity = ObjectIdentity
mpAtm = _MpAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 23)
)
_HssI431_ObjectIdentity = ObjectIdentity
hssI431 = _HssI431_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 24)
)
_MpFddi_ObjectIdentity = ObjectIdentity
mpFddi = _MpFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 25)
)
_Mp6EthFl_ObjectIdentity = ObjectIdentity
mp6EthFl = _Mp6EthFl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 26)
)
_EthV3_ObjectIdentity = ObjectIdentity
ethV3 = _EthV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 27)
)
_EthV3Fl_ObjectIdentity = ObjectIdentity
ethV3Fl = _EthV3Fl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 28)
)
_NbroBrd_ObjectIdentity = ObjectIdentity
nbroBrd = _NbroBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 29)
)
_MpAtmFiber_ObjectIdentity = ObjectIdentity
mpAtmFiber = _MpAtmFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 30)
)
_Dpe_ObjectIdentity = ObjectIdentity
dpe = _Dpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 31)
)
_FlatFddiMm_ObjectIdentity = ObjectIdentity
flatFddiMm = _FlatFddiMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 32)
)
_FlatFddiSs_ObjectIdentity = ObjectIdentity
flatFddiSs = _FlatFddiSs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 33)
)
_FlatFddiSm_ObjectIdentity = ObjectIdentity
flatFddiSm = _FlatFddiSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 34)
)
_FlatFddiMs_ObjectIdentity = ObjectIdentity
flatFddiMs = _FlatFddiMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 35)
)
_MpAtmFiberMm_ObjectIdentity = ObjectIdentity
mpAtmFiberMm = _MpAtmFiberMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 36)
)
_NbocBrd_ObjectIdentity = ObjectIdentity
nbocBrd = _NbocBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 37)
)
_NbocST_ObjectIdentity = ObjectIdentity
nbocST = _NbocST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 38)
)
_NbocU_ObjectIdentity = ObjectIdentity
nbocU = _NbocU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 39)
)
_Nboc56kCSU_ObjectIdentity = ObjectIdentity
nboc56kCSU = _Nboc56kCSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 40)
)
_NbocT1CSU_ObjectIdentity = ObjectIdentity
nbocT1CSU = _NbocT1CSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 41)
)
_Nboc1x1_ObjectIdentity = ObjectIdentity
nboc1x1 = _Nboc1x1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 42)
)
_Nboc2FlexWAN_ObjectIdentity = ObjectIdentity
nboc2FlexWAN = _Nboc2FlexWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 43)
)
_IntrepidBrd_ObjectIdentity = ObjectIdentity
intrepidBrd = _IntrepidBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 44)
)
_IntrepidST_ObjectIdentity = ObjectIdentity
intrepidST = _IntrepidST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 45)
)
_IntrepidU_ObjectIdentity = ObjectIdentity
intrepidU = _IntrepidU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 46)
)
_Intrepid56kCSU_ObjectIdentity = ObjectIdentity
intrepid56kCSU = _Intrepid56kCSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 47)
)
_IntrepidT1CSU_ObjectIdentity = ObjectIdentity
intrepidT1CSU = _IntrepidT1CSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 48)
)
_MbriSt_ObjectIdentity = ObjectIdentity
mbriSt = _MbriSt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 49)
)
_MbriU_ObjectIdentity = ObjectIdentity
mbriU = _MbriU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 50)
)
_QWan_ObjectIdentity = ObjectIdentity
qWan = _QWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 51)
)
_DpePlus_ObjectIdentity = ObjectIdentity
dpePlus = _DpePlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 52)
)
_Nboc1x2_ObjectIdentity = ObjectIdentity
nboc1x2 = _Nboc1x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 53)
)
_ScoreCpu_ObjectIdentity = ObjectIdentity
scoreCpu = _ScoreCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 54)
)
_ScoreT1_ObjectIdentity = ObjectIdentity
scoreT1 = _ScoreT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 55)
)
_ScoreT3_ObjectIdentity = ObjectIdentity
scoreT3 = _ScoreT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 56)
)
_ScorePRI_ObjectIdentity = ObjectIdentity
scorePRI = _ScorePRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 57)
)
_BlueridgeBrd_ObjectIdentity = ObjectIdentity
blueridgeBrd = _BlueridgeBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 58)
)
_BlueridgeST_ObjectIdentity = ObjectIdentity
blueridgeST = _BlueridgeST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 59)
)
_BlueridgeU_ObjectIdentity = ObjectIdentity
blueridgeU = _BlueridgeU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 60)
)
_Blueridge56kCSU_ObjectIdentity = ObjectIdentity
blueridge56kCSU = _Blueridge56kCSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 61)
)
_BlueridgeT1CSU_ObjectIdentity = ObjectIdentity
blueridgeT1CSU = _BlueridgeT1CSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 62)
)
_ScoreE3_ObjectIdentity = ObjectIdentity
scoreE3 = _ScoreE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 63)
)
_ScoreLAN_ObjectIdentity = ObjectIdentity
scoreLAN = _ScoreLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 64)
)
_CopperCPU_ObjectIdentity = ObjectIdentity
copperCPU = _CopperCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 65)
)
_VoiceFXS_ObjectIdentity = ObjectIdentity
voiceFXS = _VoiceFXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 66)
)
_VoiceFXO_ObjectIdentity = ObjectIdentity
voiceFXO = _VoiceFXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 67)
)
_VoiceEaM_ObjectIdentity = ObjectIdentity
voiceEaM = _VoiceEaM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 68)
)
_CopperST_ObjectIdentity = ObjectIdentity
copperST = _CopperST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 69)
)
_CopperU_ObjectIdentity = ObjectIdentity
copperU = _CopperU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 70)
)
_Copper56kCSU_ObjectIdentity = ObjectIdentity
copper56kCSU = _Copper56kCSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 71)
)
_CopperT1CSU_ObjectIdentity = ObjectIdentity
copperT1CSU = _CopperT1CSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 72)
)
_ScoreATMMm_ObjectIdentity = ObjectIdentity
scoreATMMm = _ScoreATMMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 73)
)
_ScoreATMSm_ObjectIdentity = ObjectIdentity
scoreATMSm = _ScoreATMSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 74)
)
_ScoreT1x2_ObjectIdentity = ObjectIdentity
scoreT1x2 = _ScoreT1x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 75)
)
_ScorePRIx2_ObjectIdentity = ObjectIdentity
scorePRIx2 = _ScorePRIx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 76)
)
_CopperPRI_ObjectIdentity = ObjectIdentity
copperPRI = _CopperPRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 77)
)
_CopperBRIx4_ObjectIdentity = ObjectIdentity
copperBRIx4 = _CopperBRIx4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 78)
)
_CopperModem_ObjectIdentity = ObjectIdentity
copperModem = _CopperModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 79)
)
_CopperT1x1_ObjectIdentity = ObjectIdentity
copperT1x1 = _CopperT1x1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 14, 80)
)
_NetbuilderLocal_ObjectIdentity = ObjectIdentity
netbuilderLocal = _NetbuilderLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15)
)
_NetbuilderLocalBp_ObjectIdentity = ObjectIdentity
netbuilderLocalBp = _NetbuilderLocalBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 1)
)
_NetbuilderLocalCp_ObjectIdentity = ObjectIdentity
netbuilderLocalCp = _NetbuilderLocalCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 2)
)
_NetbuilderLocalXw_ObjectIdentity = ObjectIdentity
netbuilderLocalXw = _NetbuilderLocalXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 3)
)
_NetbuilderLocalCx_ObjectIdentity = ObjectIdentity
netbuilderLocalCx = _NetbuilderLocalCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 4)
)
_NetbuilderLocalBa_ObjectIdentity = ObjectIdentity
netbuilderLocalBa = _NetbuilderLocalBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 5)
)
_NetbuilderLocalAr_ObjectIdentity = ObjectIdentity
netbuilderLocalAr = _NetbuilderLocalAr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 6)
)
_NetbuilderLocalSn_ObjectIdentity = ObjectIdentity
netbuilderLocalSn = _NetbuilderLocalSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 7)
)
_NetbuilderLocalRb_ObjectIdentity = ObjectIdentity
netbuilderLocalRb = _NetbuilderLocalRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 8)
)
_NetbuilderLocalFf_ObjectIdentity = ObjectIdentity
netbuilderLocalFf = _NetbuilderLocalFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 9)
)
_NetbuilderLocalCf_ObjectIdentity = ObjectIdentity
netbuilderLocalCf = _NetbuilderLocalCf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 10)
)
_NetbuilderLocalBx_ObjectIdentity = ObjectIdentity
netbuilderLocalBx = _NetbuilderLocalBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 11)
)
_NetbuilderLocalAppn_ObjectIdentity = ObjectIdentity
netbuilderLocalAppn = _NetbuilderLocalAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 12)
)
_NetbuilderLocalLm_ObjectIdentity = ObjectIdentity
netbuilderLocalLm = _NetbuilderLocalLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 13)
)
_NetbuilderLocalLt_ObjectIdentity = ObjectIdentity
netbuilderLocalLt = _NetbuilderLocalLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 14)
)
_NetbuilderLocalWm_ObjectIdentity = ObjectIdentity
netbuilderLocalWm = _NetbuilderLocalWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 15)
)
_NetbuilderLocalWt_ObjectIdentity = ObjectIdentity
netbuilderLocalWt = _NetbuilderLocalWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 16)
)
_NetbuilderLocalAe_ObjectIdentity = ObjectIdentity
netbuilderLocalAe = _NetbuilderLocalAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 17)
)
_NetbuilderLocalAp_ObjectIdentity = ObjectIdentity
netbuilderLocalAp = _NetbuilderLocalAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 18)
)
_NetbuilderLocalAn_ObjectIdentity = ObjectIdentity
netbuilderLocalAn = _NetbuilderLocalAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 19)
)
_NetbuilderLocalLa_ObjectIdentity = ObjectIdentity
netbuilderLocalLa = _NetbuilderLocalLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 20)
)
_NetbuilderLocalWa_ObjectIdentity = ObjectIdentity
netbuilderLocalWa = _NetbuilderLocalWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 21)
)
_NetbuilderLocalAa_ObjectIdentity = ObjectIdentity
netbuilderLocalAa = _NetbuilderLocalAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 22)
)
_NetbuilderLocalAb_ObjectIdentity = ObjectIdentity
netbuilderLocalAb = _NetbuilderLocalAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 23)
)
_NetbuilderLocalBf_ObjectIdentity = ObjectIdentity
netbuilderLocalBf = _NetbuilderLocalBf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 15, 24)
)
_NetbuilderTrLocal_ObjectIdentity = ObjectIdentity
netbuilderTrLocal = _NetbuilderTrLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16)
)
_NetbuilderTrLocalBp_ObjectIdentity = ObjectIdentity
netbuilderTrLocalBp = _NetbuilderTrLocalBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 1)
)
_NetbuilderTrLocalCp_ObjectIdentity = ObjectIdentity
netbuilderTrLocalCp = _NetbuilderTrLocalCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 2)
)
_NetbuilderTrLocalXw_ObjectIdentity = ObjectIdentity
netbuilderTrLocalXw = _NetbuilderTrLocalXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 3)
)
_NetbuilderTrLocalCx_ObjectIdentity = ObjectIdentity
netbuilderTrLocalCx = _NetbuilderTrLocalCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 4)
)
_NetbuilderTrLocalBa_ObjectIdentity = ObjectIdentity
netbuilderTrLocalBa = _NetbuilderTrLocalBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 5)
)
_NetbuilderTrLocalAr_ObjectIdentity = ObjectIdentity
netbuilderTrLocalAr = _NetbuilderTrLocalAr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 6)
)
_NetbuilderTrLocalSn_ObjectIdentity = ObjectIdentity
netbuilderTrLocalSn = _NetbuilderTrLocalSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 7)
)
_NetbuilderTrLocalRb_ObjectIdentity = ObjectIdentity
netbuilderTrLocalRb = _NetbuilderTrLocalRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 8)
)
_NetbuilderTrLocalFf_ObjectIdentity = ObjectIdentity
netbuilderTrLocalFf = _NetbuilderTrLocalFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 9)
)
_NetbuilderTrLocalCf_ObjectIdentity = ObjectIdentity
netbuilderTrLocalCf = _NetbuilderTrLocalCf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 10)
)
_NetbuilderTrLocalBx_ObjectIdentity = ObjectIdentity
netbuilderTrLocalBx = _NetbuilderTrLocalBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 11)
)
_NetbuilderTrLocalAppn_ObjectIdentity = ObjectIdentity
netbuilderTrLocalAppn = _NetbuilderTrLocalAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 12)
)
_NetbuilderTrLocalLm_ObjectIdentity = ObjectIdentity
netbuilderTrLocalLm = _NetbuilderTrLocalLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 13)
)
_NetbuilderTrLocalLt_ObjectIdentity = ObjectIdentity
netbuilderTrLocalLt = _NetbuilderTrLocalLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 14)
)
_NetbuilderTrLocalWm_ObjectIdentity = ObjectIdentity
netbuilderTrLocalWm = _NetbuilderTrLocalWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 15)
)
_NetbuilderTrLocalWt_ObjectIdentity = ObjectIdentity
netbuilderTrLocalWt = _NetbuilderTrLocalWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 16)
)
_NetbuilderTrLocalAe_ObjectIdentity = ObjectIdentity
netbuilderTrLocalAe = _NetbuilderTrLocalAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 17)
)
_NetbuilderTrLocalAp_ObjectIdentity = ObjectIdentity
netbuilderTrLocalAp = _NetbuilderTrLocalAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 18)
)
_NetbuilderTrLocalAn_ObjectIdentity = ObjectIdentity
netbuilderTrLocalAn = _NetbuilderTrLocalAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 19)
)
_NetbuilderTrLocalLa_ObjectIdentity = ObjectIdentity
netbuilderTrLocalLa = _NetbuilderTrLocalLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 20)
)
_NetbuilderTrLocalWa_ObjectIdentity = ObjectIdentity
netbuilderTrLocalWa = _NetbuilderTrLocalWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 21)
)
_NetbuilderTrLocalAa_ObjectIdentity = ObjectIdentity
netbuilderTrLocalAa = _NetbuilderTrLocalAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 22)
)
_NetbuilderTrLocalAb_ObjectIdentity = ObjectIdentity
netbuilderTrLocalAb = _NetbuilderTrLocalAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 23)
)
_NetbuilderTrLocalBf_ObjectIdentity = ObjectIdentity
netbuilderTrLocalBf = _NetbuilderTrLocalBf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 16, 24)
)
_NetbuilderRC1x2_ObjectIdentity = ObjectIdentity
netbuilderRC1x2 = _NetbuilderRC1x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17)
)
_NetbuilderRC1x2bp_ObjectIdentity = ObjectIdentity
netbuilderRC1x2bp = _NetbuilderRC1x2bp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 1)
)
_NetbuilderRC1x2cp_ObjectIdentity = ObjectIdentity
netbuilderRC1x2cp = _NetbuilderRC1x2cp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 2)
)
_NetbuilderRC1x2xw_ObjectIdentity = ObjectIdentity
netbuilderRC1x2xw = _NetbuilderRC1x2xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 3)
)
_NetbuilderRC1x2cx_ObjectIdentity = ObjectIdentity
netbuilderRC1x2cx = _NetbuilderRC1x2cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 4)
)
_NetbuilderRC1x2ba_ObjectIdentity = ObjectIdentity
netbuilderRC1x2ba = _NetbuilderRC1x2ba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 5)
)
_NetbuilderRC1x2ar_ObjectIdentity = ObjectIdentity
netbuilderRC1x2ar = _NetbuilderRC1x2ar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 6)
)
_NetbuilderRC1x2sn_ObjectIdentity = ObjectIdentity
netbuilderRC1x2sn = _NetbuilderRC1x2sn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 7)
)
_NetbuilderRC1x2rb_ObjectIdentity = ObjectIdentity
netbuilderRC1x2rb = _NetbuilderRC1x2rb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 8)
)
_NetbuilderRC1x2ff_ObjectIdentity = ObjectIdentity
netbuilderRC1x2ff = _NetbuilderRC1x2ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 9)
)
_NetbuilderRC1x2cf_ObjectIdentity = ObjectIdentity
netbuilderRC1x2cf = _NetbuilderRC1x2cf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 10)
)
_NetbuilderRC1x2bx_ObjectIdentity = ObjectIdentity
netbuilderRC1x2bx = _NetbuilderRC1x2bx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 11)
)
_NetbuilderRC1x2appn_ObjectIdentity = ObjectIdentity
netbuilderRC1x2appn = _NetbuilderRC1x2appn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 12)
)
_NetbuilderRC1x2lm_ObjectIdentity = ObjectIdentity
netbuilderRC1x2lm = _NetbuilderRC1x2lm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 13)
)
_NetbuilderRC1x2lt_ObjectIdentity = ObjectIdentity
netbuilderRC1x2lt = _NetbuilderRC1x2lt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 14)
)
_NetbuilderRC1x2wm_ObjectIdentity = ObjectIdentity
netbuilderRC1x2wm = _NetbuilderRC1x2wm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 15)
)
_NetbuilderRC1x2wt_ObjectIdentity = ObjectIdentity
netbuilderRC1x2wt = _NetbuilderRC1x2wt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 16)
)
_NetbuilderRC1x2ae_ObjectIdentity = ObjectIdentity
netbuilderRC1x2ae = _NetbuilderRC1x2ae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 17)
)
_NetbuilderRC1x2ap_ObjectIdentity = ObjectIdentity
netbuilderRC1x2ap = _NetbuilderRC1x2ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 18)
)
_NetbuilderRC1x2an_ObjectIdentity = ObjectIdentity
netbuilderRC1x2an = _NetbuilderRC1x2an_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 19)
)
_NetbuilderRC1x2la_ObjectIdentity = ObjectIdentity
netbuilderRC1x2la = _NetbuilderRC1x2la_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 20)
)
_NetbuilderRC1x2wa_ObjectIdentity = ObjectIdentity
netbuilderRC1x2wa = _NetbuilderRC1x2wa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 21)
)
_NetbuilderRC1x2aa_ObjectIdentity = ObjectIdentity
netbuilderRC1x2aa = _NetbuilderRC1x2aa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 22)
)
_NetbuilderRC1x2ab_ObjectIdentity = ObjectIdentity
netbuilderRC1x2ab = _NetbuilderRC1x2ab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 23)
)
_NetbuilderRC1x2bf_ObjectIdentity = ObjectIdentity
netbuilderRC1x2bf = _NetbuilderRC1x2bf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 17, 24)
)
_NetbuilderTrRC1x2_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2 = _NetbuilderTrRC1x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18)
)
_NetbuilderTrRC1x2bp_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2bp = _NetbuilderTrRC1x2bp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 1)
)
_NetbuilderTrRC1x2cp_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2cp = _NetbuilderTrRC1x2cp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 2)
)
_NetbuilderTrRC1x2xw_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2xw = _NetbuilderTrRC1x2xw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 3)
)
_NetbuilderTrRC1x2cx_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2cx = _NetbuilderTrRC1x2cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 4)
)
_NetbuilderTrRC1x2ba_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2ba = _NetbuilderTrRC1x2ba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 5)
)
_NetbuilderTrRC1x2ar_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2ar = _NetbuilderTrRC1x2ar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 6)
)
_NetbuilderTrRC1x2sn_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2sn = _NetbuilderTrRC1x2sn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 7)
)
_NetbuilderTrRC1x2rb_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2rb = _NetbuilderTrRC1x2rb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 8)
)
_NetbuilderTrRC1x2ff_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2ff = _NetbuilderTrRC1x2ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 9)
)
_NetbuilderTrRC1x2cf_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2cf = _NetbuilderTrRC1x2cf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 10)
)
_NetbuilderTrRC1x2bx_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2bx = _NetbuilderTrRC1x2bx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 11)
)
_NetbuilderTrRC1x2appn_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2appn = _NetbuilderTrRC1x2appn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 12)
)
_NetbuilderTrRC1x2lm_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2lm = _NetbuilderTrRC1x2lm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 13)
)
_NetbuilderTrRC1x2lt_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2lt = _NetbuilderTrRC1x2lt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 14)
)
_NetbuilderTrRC1x2wm_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2wm = _NetbuilderTrRC1x2wm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 15)
)
_NetbuilderTrRC1x2wt_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2wt = _NetbuilderTrRC1x2wt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 16)
)
_NetbuilderTrRC1x2ae_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2ae = _NetbuilderTrRC1x2ae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 17)
)
_NetbuilderTrRC1x2ap_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2ap = _NetbuilderTrRC1x2ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 18)
)
_NetbuilderTrRC1x2an_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2an = _NetbuilderTrRC1x2an_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 19)
)
_NetbuilderTrRC1x2la_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2la = _NetbuilderTrRC1x2la_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 20)
)
_NetbuilderTrRC1x2wa_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2wa = _NetbuilderTrRC1x2wa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 21)
)
_NetbuilderTrRC1x2aa_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2aa = _NetbuilderTrRC1x2aa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 22)
)
_NetbuilderTrRC1x2ab_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2ab = _NetbuilderTrRC1x2ab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 23)
)
_NetbuilderTrRC1x2bf_ObjectIdentity = ObjectIdentity
netbuilderTrRC1x2bf = _NetbuilderTrRC1x2bf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 18, 24)
)
_Casper_ObjectIdentity = ObjectIdentity
casper = _Casper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19)
)
_NbrolBp_ObjectIdentity = ObjectIdentity
nbrolBp = _NbrolBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 1)
)
_NbrolCp_ObjectIdentity = ObjectIdentity
nbrolCp = _NbrolCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 2)
)
_NbrolXw_ObjectIdentity = ObjectIdentity
nbrolXw = _NbrolXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 3)
)
_Nbrol228_ObjectIdentity = ObjectIdentity
nbrol228 = _Nbrol228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 4)
)
_Nbrol201_ObjectIdentity = ObjectIdentity
nbrol201 = _Nbrol201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 5)
)
_Nbro222_ObjectIdentity = ObjectIdentity
nbro222 = _Nbro222_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 6)
)
_NbrolSn_ObjectIdentity = ObjectIdentity
nbrolSn = _NbrolSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 7)
)
_Nbrol200_ObjectIdentity = ObjectIdentity
nbrol200 = _Nbrol200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 8)
)
_NbrolFf_ObjectIdentity = ObjectIdentity
nbrolFf = _NbrolFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 9)
)
_Nbro227_ObjectIdentity = ObjectIdentity
nbro227 = _Nbro227_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 10)
)
_Nbro221_ObjectIdentity = ObjectIdentity
nbro221 = _Nbro221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 11)
)
_NbrolAppn_ObjectIdentity = ObjectIdentity
nbrolAppn = _NbrolAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 12)
)
_NbrolLm_ObjectIdentity = ObjectIdentity
nbrolLm = _NbrolLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 13)
)
_NbrolLt_ObjectIdentity = ObjectIdentity
nbrolLt = _NbrolLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 14)
)
_NbrolWm_ObjectIdentity = ObjectIdentity
nbrolWm = _NbrolWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 15)
)
_NbrolWt_ObjectIdentity = ObjectIdentity
nbrolWt = _NbrolWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 16)
)
_NbrolAe_ObjectIdentity = ObjectIdentity
nbrolAe = _NbrolAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 17)
)
_NbrolAp_ObjectIdentity = ObjectIdentity
nbrolAp = _NbrolAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 18)
)
_NbrolAn_ObjectIdentity = ObjectIdentity
nbrolAn = _NbrolAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 19)
)
_NbrolLa_ObjectIdentity = ObjectIdentity
nbrolLa = _NbrolLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 20)
)
_NbrolWa_ObjectIdentity = ObjectIdentity
nbrolWa = _NbrolWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 21)
)
_Nbrol224_ObjectIdentity = ObjectIdentity
nbrol224 = _Nbrol224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 22)
)
_NbrolAb_ObjectIdentity = ObjectIdentity
nbrolAb = _NbrolAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 23)
)
_Nbrol223_ObjectIdentity = ObjectIdentity
nbrol223 = _Nbrol223_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 19, 24)
)
_SpectreHuge_ObjectIdentity = ObjectIdentity
spectreHuge = _SpectreHuge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20)
)
_NbrohBp_ObjectIdentity = ObjectIdentity
nbrohBp = _NbrohBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 1)
)
_NbrohCp_ObjectIdentity = ObjectIdentity
nbrohCp = _NbrohCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 2)
)
_NbrohXw_ObjectIdentity = ObjectIdentity
nbrohXw = _NbrohXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 3)
)
_Nbro228_ObjectIdentity = ObjectIdentity
nbro228 = _Nbro228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 4)
)
_Nbroh201_ObjectIdentity = ObjectIdentity
nbroh201 = _Nbroh201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 5)
)
_Nbroh222_ObjectIdentity = ObjectIdentity
nbroh222 = _Nbroh222_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 6)
)
_NbrohSn_ObjectIdentity = ObjectIdentity
nbrohSn = _NbrohSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 7)
)
_Nbroh200_ObjectIdentity = ObjectIdentity
nbroh200 = _Nbroh200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 8)
)
_NbrohFf_ObjectIdentity = ObjectIdentity
nbrohFf = _NbrohFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 9)
)
_Nbroh227_ObjectIdentity = ObjectIdentity
nbroh227 = _Nbroh227_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 10)
)
_Nbroh221_ObjectIdentity = ObjectIdentity
nbroh221 = _Nbroh221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 11)
)
_NbrohAppn_ObjectIdentity = ObjectIdentity
nbrohAppn = _NbrohAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 12)
)
_NbrohLm_ObjectIdentity = ObjectIdentity
nbrohLm = _NbrohLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 13)
)
_NbrohLt_ObjectIdentity = ObjectIdentity
nbrohLt = _NbrohLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 14)
)
_NbrohWm_ObjectIdentity = ObjectIdentity
nbrohWm = _NbrohWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 15)
)
_NbrohWt_ObjectIdentity = ObjectIdentity
nbrohWt = _NbrohWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 16)
)
_NbrohAe_ObjectIdentity = ObjectIdentity
nbrohAe = _NbrohAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 17)
)
_NbrohAp_ObjectIdentity = ObjectIdentity
nbrohAp = _NbrohAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 18)
)
_NbrohAn_ObjectIdentity = ObjectIdentity
nbrohAn = _NbrohAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 19)
)
_NbrohLa_ObjectIdentity = ObjectIdentity
nbrohLa = _NbrohLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 20)
)
_NbrohWa_ObjectIdentity = ObjectIdentity
nbrohWa = _NbrohWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 21)
)
_Nbroh224_ObjectIdentity = ObjectIdentity
nbroh224 = _Nbroh224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 22)
)
_NbrohAb_ObjectIdentity = ObjectIdentity
nbrohAb = _NbrohAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 23)
)
_Nbroh223_ObjectIdentity = ObjectIdentity
nbroh223 = _Nbroh223_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 20, 24)
)
_SpectreIsdn_ObjectIdentity = ObjectIdentity
spectreIsdn = _SpectreIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21)
)
_NbroiBp_ObjectIdentity = ObjectIdentity
nbroiBp = _NbroiBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 1)
)
_NbroiCp_ObjectIdentity = ObjectIdentity
nbroiCp = _NbroiCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 2)
)
_NbroiXw_ObjectIdentity = ObjectIdentity
nbroiXw = _NbroiXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 3)
)
_NbroiCX_ObjectIdentity = ObjectIdentity
nbroiCX = _NbroiCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 4)
)
_NbroiBA_ObjectIdentity = ObjectIdentity
nbroiBA = _NbroiBA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 5)
)
_Nbro422_ObjectIdentity = ObjectIdentity
nbro422 = _Nbro422_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 6)
)
_NbroiSn_ObjectIdentity = ObjectIdentity
nbroiSn = _NbroiSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 7)
)
_Nbroi200_ObjectIdentity = ObjectIdentity
nbroi200 = _Nbroi200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 8)
)
_NbroiFf_ObjectIdentity = ObjectIdentity
nbroiFf = _NbroiFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 9)
)
_Nbroil427_ObjectIdentity = ObjectIdentity
nbroil427 = _Nbroil427_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 10)
)
_Nbro421_ObjectIdentity = ObjectIdentity
nbro421 = _Nbro421_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 11)
)
_NbroiAppn_ObjectIdentity = ObjectIdentity
nbroiAppn = _NbroiAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 12)
)
_NbroiLm_ObjectIdentity = ObjectIdentity
nbroiLm = _NbroiLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 13)
)
_NbroiLt_ObjectIdentity = ObjectIdentity
nbroiLt = _NbroiLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 14)
)
_NbroiWm_ObjectIdentity = ObjectIdentity
nbroiWm = _NbroiWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 15)
)
_NbroiWt_ObjectIdentity = ObjectIdentity
nbroiWt = _NbroiWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 16)
)
_NbroiAe_ObjectIdentity = ObjectIdentity
nbroiAe = _NbroiAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 17)
)
_NbroiAp_ObjectIdentity = ObjectIdentity
nbroiAp = _NbroiAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 18)
)
_NbroiAn_ObjectIdentity = ObjectIdentity
nbroiAn = _NbroiAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 19)
)
_NbroiLa_ObjectIdentity = ObjectIdentity
nbroiLa = _NbroiLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 20)
)
_NbroiWa_ObjectIdentity = ObjectIdentity
nbroiWa = _NbroiWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 21)
)
_Nbroi424_ObjectIdentity = ObjectIdentity
nbroi424 = _Nbroi424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 22)
)
_NbroiAb_ObjectIdentity = ObjectIdentity
nbroiAb = _NbroiAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 23)
)
_Nbroi423_ObjectIdentity = ObjectIdentity
nbroi423 = _Nbroi423_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 21, 24)
)
_Nb2_8_4fddi_ObjectIdentity = ObjectIdentity
nb2_8_4fddi = _Nb2_8_4fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22)
)
_Nb2_8_4fddiBp_ObjectIdentity = ObjectIdentity
nb2_8_4fddiBp = _Nb2_8_4fddiBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 1)
)
_Nb2_8_4fddiCp_ObjectIdentity = ObjectIdentity
nb2_8_4fddiCp = _Nb2_8_4fddiCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 2)
)
_Nb2_8_4fddiXw_ObjectIdentity = ObjectIdentity
nb2_8_4fddiXw = _Nb2_8_4fddiXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 3)
)
_Nb2_8_4fddiCx_ObjectIdentity = ObjectIdentity
nb2_8_4fddiCx = _Nb2_8_4fddiCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 4)
)
_Nb2_8_4fddiBa_ObjectIdentity = ObjectIdentity
nb2_8_4fddiBa = _Nb2_8_4fddiBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 5)
)
_Nb2_8_4fddiAr_ObjectIdentity = ObjectIdentity
nb2_8_4fddiAr = _Nb2_8_4fddiAr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 6)
)
_Nb2_8_4fddiSn_ObjectIdentity = ObjectIdentity
nb2_8_4fddiSn = _Nb2_8_4fddiSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 7)
)
_Nb2_8_4fddiRb_ObjectIdentity = ObjectIdentity
nb2_8_4fddiRb = _Nb2_8_4fddiRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 8)
)
_Nb2_8_4fddiFf_ObjectIdentity = ObjectIdentity
nb2_8_4fddiFf = _Nb2_8_4fddiFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 9)
)
_Nb2_8_4fddiCf_ObjectIdentity = ObjectIdentity
nb2_8_4fddiCf = _Nb2_8_4fddiCf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 10)
)
_Nb2_8_4fddiBx_ObjectIdentity = ObjectIdentity
nb2_8_4fddiBx = _Nb2_8_4fddiBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 11)
)
_Nb2_8_4fddiAppn_ObjectIdentity = ObjectIdentity
nb2_8_4fddiAppn = _Nb2_8_4fddiAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 12)
)
_Nb2_8_4fddiLm_ObjectIdentity = ObjectIdentity
nb2_8_4fddiLm = _Nb2_8_4fddiLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 13)
)
_Nb2_8_4fddiLt_ObjectIdentity = ObjectIdentity
nb2_8_4fddiLt = _Nb2_8_4fddiLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 14)
)
_Nb2_8_4fddiWm_ObjectIdentity = ObjectIdentity
nb2_8_4fddiWm = _Nb2_8_4fddiWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 15)
)
_Nb2_8_4fddiWt_ObjectIdentity = ObjectIdentity
nb2_8_4fddiWt = _Nb2_8_4fddiWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 16)
)
_Nb2_8_4fddiAe_ObjectIdentity = ObjectIdentity
nb2_8_4fddiAe = _Nb2_8_4fddiAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 17)
)
_Nb2_8_4fddiAp_ObjectIdentity = ObjectIdentity
nb2_8_4fddiAp = _Nb2_8_4fddiAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 18)
)
_Nb2_8_4fddiAn_ObjectIdentity = ObjectIdentity
nb2_8_4fddiAn = _Nb2_8_4fddiAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 19)
)
_Nb2_8_4fddiLa_ObjectIdentity = ObjectIdentity
nb2_8_4fddiLa = _Nb2_8_4fddiLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 20)
)
_Nb2_8_4fddiWa_ObjectIdentity = ObjectIdentity
nb2_8_4fddiWa = _Nb2_8_4fddiWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 21)
)
_Nb2_8_4fddiAa_ObjectIdentity = ObjectIdentity
nb2_8_4fddiAa = _Nb2_8_4fddiAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 22)
)
_Nb2_8_4fddiAb_ObjectIdentity = ObjectIdentity
nb2_8_4fddiAb = _Nb2_8_4fddiAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 23)
)
_Nb2_8_4fddiBf_ObjectIdentity = ObjectIdentity
nb2_8_4fddiBf = _Nb2_8_4fddiBf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 22, 24)
)
_Nb2_8_dualwide_ObjectIdentity = ObjectIdentity
nb2_8_dualwide = _Nb2_8_dualwide_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23)
)
_Nb2_8_dualwideBp_ObjectIdentity = ObjectIdentity
nb2_8_dualwideBp = _Nb2_8_dualwideBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 1)
)
_Nb2_8_dualwideCp_ObjectIdentity = ObjectIdentity
nb2_8_dualwideCp = _Nb2_8_dualwideCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 2)
)
_Nb2_8_dualwideXw_ObjectIdentity = ObjectIdentity
nb2_8_dualwideXw = _Nb2_8_dualwideXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 3)
)
_Nb2_8_dualwideCx_ObjectIdentity = ObjectIdentity
nb2_8_dualwideCx = _Nb2_8_dualwideCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 4)
)
_Nb2_8_dualwideBa_ObjectIdentity = ObjectIdentity
nb2_8_dualwideBa = _Nb2_8_dualwideBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 5)
)
_Nb2_8_dualwideAr_ObjectIdentity = ObjectIdentity
nb2_8_dualwideAr = _Nb2_8_dualwideAr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 6)
)
_Nb2_8_dualwideSn_ObjectIdentity = ObjectIdentity
nb2_8_dualwideSn = _Nb2_8_dualwideSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 7)
)
_Nb2_8_dualwideRb_ObjectIdentity = ObjectIdentity
nb2_8_dualwideRb = _Nb2_8_dualwideRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 8)
)
_Nb2_8_dualwideFf_ObjectIdentity = ObjectIdentity
nb2_8_dualwideFf = _Nb2_8_dualwideFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 9)
)
_Nb2_8_dualwideCf_ObjectIdentity = ObjectIdentity
nb2_8_dualwideCf = _Nb2_8_dualwideCf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 10)
)
_Nb2_8_dualwideBx_ObjectIdentity = ObjectIdentity
nb2_8_dualwideBx = _Nb2_8_dualwideBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 11)
)
_Nb2_8_dualwideAppn_ObjectIdentity = ObjectIdentity
nb2_8_dualwideAppn = _Nb2_8_dualwideAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 12)
)
_Nb2_8_dualwideLm_ObjectIdentity = ObjectIdentity
nb2_8_dualwideLm = _Nb2_8_dualwideLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 13)
)
_Nb2_8_dualwideLt_ObjectIdentity = ObjectIdentity
nb2_8_dualwideLt = _Nb2_8_dualwideLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 14)
)
_Nb2_8_dualwideWm_ObjectIdentity = ObjectIdentity
nb2_8_dualwideWm = _Nb2_8_dualwideWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 15)
)
_Nb2_8_dualwideWt_ObjectIdentity = ObjectIdentity
nb2_8_dualwideWt = _Nb2_8_dualwideWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 16)
)
_Nb2_8_dualwideAe_ObjectIdentity = ObjectIdentity
nb2_8_dualwideAe = _Nb2_8_dualwideAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 17)
)
_Nb2_8_dualwideAp_ObjectIdentity = ObjectIdentity
nb2_8_dualwideAp = _Nb2_8_dualwideAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 18)
)
_Nb2_8_dualwideAn_ObjectIdentity = ObjectIdentity
nb2_8_dualwideAn = _Nb2_8_dualwideAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 19)
)
_Nb2_8_dualwideLa_ObjectIdentity = ObjectIdentity
nb2_8_dualwideLa = _Nb2_8_dualwideLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 20)
)
_Nb2_8_dualwideWa_ObjectIdentity = ObjectIdentity
nb2_8_dualwideWa = _Nb2_8_dualwideWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 21)
)
_Nb2_8_dualwideAa_ObjectIdentity = ObjectIdentity
nb2_8_dualwideAa = _Nb2_8_dualwideAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 22)
)
_Nb2_8_dualwideAb_ObjectIdentity = ObjectIdentity
nb2_8_dualwideAb = _Nb2_8_dualwideAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 23)
)
_Nb2_8_dualwideBf_ObjectIdentity = ObjectIdentity
nb2_8_dualwideBf = _Nb2_8_dualwideBf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 23, 24)
)
_BrouterBrdFwVers_ObjectIdentity = ObjectIdentity
brouterBrdFwVers = _BrouterBrdFwVers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24)
)
_NoFw_ObjectIdentity = ObjectIdentity
noFw = _NoFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 1)
)
_CecFw_ObjectIdentity = ObjectIdentity
cecFw = _CecFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 2)
)
_HdwanFw_ObjectIdentity = ObjectIdentity
hdwanFw = _HdwanFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 3)
)
_Hdwan232Fw_ObjectIdentity = ObjectIdentity
hdwan232Fw = _Hdwan232Fw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 4)
)
_Hdwan449Fw_ObjectIdentity = ObjectIdentity
hdwan449Fw = _Hdwan449Fw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 5)
)
_Mp6ethFw_ObjectIdentity = ObjectIdentity
mp6ethFw = _Mp6ethFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 6)
)
_CecStarFw_ObjectIdentity = ObjectIdentity
cecStarFw = _CecStarFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 7)
)
_MpAtmFw_ObjectIdentity = ObjectIdentity
mpAtmFw = _MpAtmFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 8)
)
_MpFddiFw_ObjectIdentity = ObjectIdentity
mpFddiFw = _MpFddiFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 9)
)
_Mp6EthFlFw_ObjectIdentity = ObjectIdentity
mp6EthFlFw = _Mp6EthFlFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 10)
)
_NbroFw_ObjectIdentity = ObjectIdentity
nbroFw = _NbroFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 11)
)
_NbocFw_ObjectIdentity = ObjectIdentity
nbocFw = _NbocFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 12)
)
_DpeFw_ObjectIdentity = ObjectIdentity
dpeFw = _DpeFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 13)
)
_IntrepidFw_ObjectIdentity = ObjectIdentity
intrepidFw = _IntrepidFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 14)
)
_MbriFw_ObjectIdentity = ObjectIdentity
mbriFw = _MbriFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 15)
)
_QwanFw_ObjectIdentity = ObjectIdentity
qwanFw = _QwanFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 16)
)
_ScoreFw_ObjectIdentity = ObjectIdentity
scoreFw = _ScoreFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 17)
)
_BlueridgeFw_ObjectIdentity = ObjectIdentity
blueridgeFw = _BlueridgeFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 24, 18)
)
_BrouterBrdSwVers_ObjectIdentity = ObjectIdentity
brouterBrdSwVers = _BrouterBrdSwVers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 25)
)
_NoSw_ObjectIdentity = ObjectIdentity
noSw = _NoSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 25, 1)
)
_Mp6eth_ObjectIdentity = ObjectIdentity
mp6eth = _Mp6eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 25, 2)
)
_SpectreIsdnHuge_ObjectIdentity = ObjectIdentity
spectreIsdnHuge = _SpectreIsdnHuge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26)
)
_NbroihBp_ObjectIdentity = ObjectIdentity
nbroihBp = _NbroihBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 1)
)
_NbroihCp_ObjectIdentity = ObjectIdentity
nbroihCp = _NbroihCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 2)
)
_NbroihXw_ObjectIdentity = ObjectIdentity
nbroihXw = _NbroihXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 3)
)
_NbroihCx_ObjectIdentity = ObjectIdentity
nbroihCx = _NbroihCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 4)
)
_NbroihBa_ObjectIdentity = ObjectIdentity
nbroihBa = _NbroihBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 5)
)
_Nbroih422_ObjectIdentity = ObjectIdentity
nbroih422 = _Nbroih422_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 6)
)
_NbroihSn_ObjectIdentity = ObjectIdentity
nbroihSn = _NbroihSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 7)
)
_NbroihRb_ObjectIdentity = ObjectIdentity
nbroihRb = _NbroihRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 8)
)
_NbroihFf_ObjectIdentity = ObjectIdentity
nbroihFf = _NbroihFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 9)
)
_Nbroih427_ObjectIdentity = ObjectIdentity
nbroih427 = _Nbroih427_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 10)
)
_Nbroih421_ObjectIdentity = ObjectIdentity
nbroih421 = _Nbroih421_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 11)
)
_NbroihAppn_ObjectIdentity = ObjectIdentity
nbroihAppn = _NbroihAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 12)
)
_NbroihLm_ObjectIdentity = ObjectIdentity
nbroihLm = _NbroihLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 13)
)
_NbroihLt_ObjectIdentity = ObjectIdentity
nbroihLt = _NbroihLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 14)
)
_NbroihWm_ObjectIdentity = ObjectIdentity
nbroihWm = _NbroihWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 15)
)
_NbroihWt_ObjectIdentity = ObjectIdentity
nbroihWt = _NbroihWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 16)
)
_NbroihAe_ObjectIdentity = ObjectIdentity
nbroihAe = _NbroihAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 17)
)
_NbroihAp_ObjectIdentity = ObjectIdentity
nbroihAp = _NbroihAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 18)
)
_NbroihAn_ObjectIdentity = ObjectIdentity
nbroihAn = _NbroihAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 19)
)
_NbroihLa_ObjectIdentity = ObjectIdentity
nbroihLa = _NbroihLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 20)
)
_NbroihWa_ObjectIdentity = ObjectIdentity
nbroihWa = _NbroihWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 21)
)
_Nbroih424_ObjectIdentity = ObjectIdentity
nbroih424 = _Nbroih424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 22)
)
_NbroihAb_ObjectIdentity = ObjectIdentity
nbroihAb = _NbroihAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 23)
)
_Nbroih423_ObjectIdentity = ObjectIdentity
nbroih423 = _Nbroih423_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 26, 24)
)
_NbroTrHuge_ObjectIdentity = ObjectIdentity
nbroTrHuge = _NbroTrHuge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27)
)
_NbroTrlBp_ObjectIdentity = ObjectIdentity
nbroTrlBp = _NbroTrlBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 1)
)
_NbroTrlCp_ObjectIdentity = ObjectIdentity
nbroTrlCp = _NbroTrlCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 2)
)
_NbroTrlXw_ObjectIdentity = ObjectIdentity
nbroTrlXw = _NbroTrlXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 3)
)
_NbroTrlCx_ObjectIdentity = ObjectIdentity
nbroTrlCx = _NbroTrlCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 4)
)
_NbroTrlBa_ObjectIdentity = ObjectIdentity
nbroTrlBa = _NbroTrlBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 5)
)
_Nbro322_ObjectIdentity = ObjectIdentity
nbro322 = _Nbro322_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 6)
)
_NbroTrlSn_ObjectIdentity = ObjectIdentity
nbroTrlSn = _NbroTrlSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 7)
)
_NbroTrlRb_ObjectIdentity = ObjectIdentity
nbroTrlRb = _NbroTrlRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 8)
)
_NbroTrlFf_ObjectIdentity = ObjectIdentity
nbroTrlFf = _NbroTrlFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 9)
)
_NbroTrl327_ObjectIdentity = ObjectIdentity
nbroTrl327 = _NbroTrl327_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 10)
)
_Nbro321_ObjectIdentity = ObjectIdentity
nbro321 = _Nbro321_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 11)
)
_NbroTrlAppn_ObjectIdentity = ObjectIdentity
nbroTrlAppn = _NbroTrlAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 12)
)
_NbroTrlLm_ObjectIdentity = ObjectIdentity
nbroTrlLm = _NbroTrlLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 13)
)
_NbroTrlLt_ObjectIdentity = ObjectIdentity
nbroTrlLt = _NbroTrlLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 14)
)
_NbroTrlWm_ObjectIdentity = ObjectIdentity
nbroTrlWm = _NbroTrlWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 15)
)
_NbroTrlWt_ObjectIdentity = ObjectIdentity
nbroTrlWt = _NbroTrlWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 16)
)
_NbroTrlAe_ObjectIdentity = ObjectIdentity
nbroTrlAe = _NbroTrlAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 17)
)
_NbroTrlAp_ObjectIdentity = ObjectIdentity
nbroTrlAp = _NbroTrlAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 18)
)
_NbroTrlAn_ObjectIdentity = ObjectIdentity
nbroTrlAn = _NbroTrlAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 19)
)
_NbroTrlLa_ObjectIdentity = ObjectIdentity
nbroTrlLa = _NbroTrlLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 20)
)
_NbroTrlWa_ObjectIdentity = ObjectIdentity
nbroTrlWa = _NbroTrlWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 21)
)
_NbroTrlAa_ObjectIdentity = ObjectIdentity
nbroTrlAa = _NbroTrlAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 22)
)
_NbroTrlAb_ObjectIdentity = ObjectIdentity
nbroTrlAb = _NbroTrlAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 23)
)
_NbroTrl323_ObjectIdentity = ObjectIdentity
nbroTrl323 = _NbroTrl323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 27, 24)
)
_NbroTrIsdn_ObjectIdentity = ObjectIdentity
nbroTrIsdn = _NbroTrIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28)
)
_NbroTrIsdnBp_ObjectIdentity = ObjectIdentity
nbroTrIsdnBp = _NbroTrIsdnBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 1)
)
_NbroTrIsdnCp_ObjectIdentity = ObjectIdentity
nbroTrIsdnCp = _NbroTrIsdnCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 2)
)
_NbroTrIsdnXw_ObjectIdentity = ObjectIdentity
nbroTrIsdnXw = _NbroTrIsdnXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 3)
)
_NbroTrIsdnCx_ObjectIdentity = ObjectIdentity
nbroTrIsdnCx = _NbroTrIsdnCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 4)
)
_NbroTrIsdnBa_ObjectIdentity = ObjectIdentity
nbroTrIsdnBa = _NbroTrIsdnBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 5)
)
_NbroTrIsdnAr_ObjectIdentity = ObjectIdentity
nbroTrIsdnAr = _NbroTrIsdnAr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 6)
)
_NbroTrIsdnSn_ObjectIdentity = ObjectIdentity
nbroTrIsdnSn = _NbroTrIsdnSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 7)
)
_NbroTrIsdnRb_ObjectIdentity = ObjectIdentity
nbroTrIsdnRb = _NbroTrIsdnRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 8)
)
_NbroTrIsdnFf_ObjectIdentity = ObjectIdentity
nbroTrIsdnFf = _NbroTrIsdnFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 9)
)
_Nbro527_ObjectIdentity = ObjectIdentity
nbro527 = _Nbro527_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 10)
)
_NbroTrIsdnBx_ObjectIdentity = ObjectIdentity
nbroTrIsdnBx = _NbroTrIsdnBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 11)
)
_NbroTrIsdnAppn_ObjectIdentity = ObjectIdentity
nbroTrIsdnAppn = _NbroTrIsdnAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 12)
)
_NbroTrIsdnLm_ObjectIdentity = ObjectIdentity
nbroTrIsdnLm = _NbroTrIsdnLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 13)
)
_NbroTrIsdnLt_ObjectIdentity = ObjectIdentity
nbroTrIsdnLt = _NbroTrIsdnLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 14)
)
_NbroTrIsdnWm_ObjectIdentity = ObjectIdentity
nbroTrIsdnWm = _NbroTrIsdnWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 15)
)
_NbroTrIsdnWt_ObjectIdentity = ObjectIdentity
nbroTrIsdnWt = _NbroTrIsdnWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 16)
)
_NbroTrIsdnAe_ObjectIdentity = ObjectIdentity
nbroTrIsdnAe = _NbroTrIsdnAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 17)
)
_NbroTrIsdnAp_ObjectIdentity = ObjectIdentity
nbroTrIsdnAp = _NbroTrIsdnAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 18)
)
_NbroTrIsdnAn_ObjectIdentity = ObjectIdentity
nbroTrIsdnAn = _NbroTrIsdnAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 19)
)
_NbroTrIsdnLa_ObjectIdentity = ObjectIdentity
nbroTrIsdnLa = _NbroTrIsdnLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 20)
)
_NbroTrIsdnWa_ObjectIdentity = ObjectIdentity
nbroTrIsdnWa = _NbroTrIsdnWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 21)
)
_NbroTrIsdnAa_ObjectIdentity = ObjectIdentity
nbroTrIsdnAa = _NbroTrIsdnAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 22)
)
_NbroTrIsdnAb_ObjectIdentity = ObjectIdentity
nbroTrIsdnAb = _NbroTrIsdnAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 23)
)
_Nbro523_ObjectIdentity = ObjectIdentity
nbro523 = _Nbro523_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 28, 24)
)
_NbroTrNext_ObjectIdentity = ObjectIdentity
nbroTrNext = _NbroTrNext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29)
)
_NbroTrhBp_ObjectIdentity = ObjectIdentity
nbroTrhBp = _NbroTrhBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 1)
)
_NbroTrhCp_ObjectIdentity = ObjectIdentity
nbroTrhCp = _NbroTrhCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 2)
)
_NbroTrhXw_ObjectIdentity = ObjectIdentity
nbroTrhXw = _NbroTrhXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 3)
)
_NbroTrhCx_ObjectIdentity = ObjectIdentity
nbroTrhCx = _NbroTrhCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 4)
)
_NbroTrhBa_ObjectIdentity = ObjectIdentity
nbroTrhBa = _NbroTrhBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 5)
)
_NbroTrh322_ObjectIdentity = ObjectIdentity
nbroTrh322 = _NbroTrh322_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 6)
)
_NbroTrhSn_ObjectIdentity = ObjectIdentity
nbroTrhSn = _NbroTrhSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 7)
)
_NbroTrhRb_ObjectIdentity = ObjectIdentity
nbroTrhRb = _NbroTrhRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 8)
)
_NbroTrhFf_ObjectIdentity = ObjectIdentity
nbroTrhFf = _NbroTrhFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 9)
)
_NbroTrh327_ObjectIdentity = ObjectIdentity
nbroTrh327 = _NbroTrh327_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 10)
)
_NbroTrh321_ObjectIdentity = ObjectIdentity
nbroTrh321 = _NbroTrh321_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 11)
)
_NbroTrhAppn_ObjectIdentity = ObjectIdentity
nbroTrhAppn = _NbroTrhAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 12)
)
_NbroTrhLm_ObjectIdentity = ObjectIdentity
nbroTrhLm = _NbroTrhLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 13)
)
_NbroTrhLt_ObjectIdentity = ObjectIdentity
nbroTrhLt = _NbroTrhLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 14)
)
_NbroTrhWm_ObjectIdentity = ObjectIdentity
nbroTrhWm = _NbroTrhWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 15)
)
_NbroTrhWt_ObjectIdentity = ObjectIdentity
nbroTrhWt = _NbroTrhWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 16)
)
_NbroTrhAe_ObjectIdentity = ObjectIdentity
nbroTrhAe = _NbroTrhAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 17)
)
_NbroTrhAp_ObjectIdentity = ObjectIdentity
nbroTrhAp = _NbroTrhAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 18)
)
_NbroTrhAn_ObjectIdentity = ObjectIdentity
nbroTrhAn = _NbroTrhAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 19)
)
_NbroTrhLa_ObjectIdentity = ObjectIdentity
nbroTrhLa = _NbroTrhLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 20)
)
_NbroTrhWa_ObjectIdentity = ObjectIdentity
nbroTrhWa = _NbroTrhWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 21)
)
_NbroTrhAa_ObjectIdentity = ObjectIdentity
nbroTrhAa = _NbroTrhAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 22)
)
_NbroTrhAb_ObjectIdentity = ObjectIdentity
nbroTrhAb = _NbroTrhAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 23)
)
_NbroTrh323_ObjectIdentity = ObjectIdentity
nbroTrh323 = _NbroTrh323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 29, 24)
)
_Nbro2Eth_ObjectIdentity = ObjectIdentity
nbro2Eth = _Nbro2Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 30)
)
_Nbro2EthIsdn_ObjectIdentity = ObjectIdentity
nbro2EthIsdn = _Nbro2EthIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 31)
)
_OfficeConnRtr_ObjectIdentity = ObjectIdentity
officeConnRtr = _OfficeConnRtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32)
)
_OcRtrBp_ObjectIdentity = ObjectIdentity
ocRtrBp = _OcRtrBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 1)
)
_OcRtrCp_ObjectIdentity = ObjectIdentity
ocRtrCp = _OcRtrCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 2)
)
_OcRtrXw_ObjectIdentity = ObjectIdentity
ocRtrXw = _OcRtrXw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 3)
)
_OcRtrCx_ObjectIdentity = ObjectIdentity
ocRtrCx = _OcRtrCx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 4)
)
_OcRtrBa_ObjectIdentity = ObjectIdentity
ocRtrBa = _OcRtrBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 5)
)
_OcRtrAr_ObjectIdentity = ObjectIdentity
ocRtrAr = _OcRtrAr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 6)
)
_OcRtrSn_ObjectIdentity = ObjectIdentity
ocRtrSn = _OcRtrSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 7)
)
_OcRtrRb_ObjectIdentity = ObjectIdentity
ocRtrRb = _OcRtrRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 8)
)
_OcRtrFf_ObjectIdentity = ObjectIdentity
ocRtrFf = _OcRtrFf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 9)
)
_OcRtrCf_ObjectIdentity = ObjectIdentity
ocRtrCf = _OcRtrCf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 10)
)
_OcRtrBx_ObjectIdentity = ObjectIdentity
ocRtrBx = _OcRtrBx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 11)
)
_OcRtrAppn_ObjectIdentity = ObjectIdentity
ocRtrAppn = _OcRtrAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 12)
)
_OcRtrLm_ObjectIdentity = ObjectIdentity
ocRtrLm = _OcRtrLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 13)
)
_OcRtrLt_ObjectIdentity = ObjectIdentity
ocRtrLt = _OcRtrLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 14)
)
_OcRtrWm_ObjectIdentity = ObjectIdentity
ocRtrWm = _OcRtrWm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 15)
)
_OcRtrWt_ObjectIdentity = ObjectIdentity
ocRtrWt = _OcRtrWt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 16)
)
_OcRtrAe_ObjectIdentity = ObjectIdentity
ocRtrAe = _OcRtrAe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 17)
)
_OcRtrAp_ObjectIdentity = ObjectIdentity
ocRtrAp = _OcRtrAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 18)
)
_OcRtrAn_ObjectIdentity = ObjectIdentity
ocRtrAn = _OcRtrAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 19)
)
_OcRtrLa_ObjectIdentity = ObjectIdentity
ocRtrLa = _OcRtrLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 20)
)
_OcRtrWa_ObjectIdentity = ObjectIdentity
ocRtrWa = _OcRtrWa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 21)
)
_OcRtrAa_ObjectIdentity = ObjectIdentity
ocRtrAa = _OcRtrAa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 22)
)
_OcRtrAb_ObjectIdentity = ObjectIdentity
ocRtrAb = _OcRtrAb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 23)
)
_OcRtrBf_ObjectIdentity = ObjectIdentity
ocRtrBf = _OcRtrBf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 32, 24)
)
_IntrepidRtr_ObjectIdentity = ObjectIdentity
intrepidRtr = _IntrepidRtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 33)
)
_SuperStackSwitch1100Router_ObjectIdentity = ObjectIdentity
superStackSwitch1100Router = _SuperStackSwitch1100Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 34)
)
_ScoreRtr_ObjectIdentity = ObjectIdentity
scoreRtr = _ScoreRtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 35)
)
_CopperRtr_ObjectIdentity = ObjectIdentity
copperRtr = _CopperRtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 36)
)
_EasterRtr_ObjectIdentity = ObjectIdentity
easterRtr = _EasterRtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 37)
)
_Rtr400Hw_ObjectIdentity = ObjectIdentity
rtr400Hw = _Rtr400Hw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 37, 1)
)
_Rtr400Hs_ObjectIdentity = ObjectIdentity
rtr400Hs = _Rtr400Hs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4, 37, 2)
)
_GenericMSWorkstation_ObjectIdentity = ObjectIdentity
genericMSWorkstation = _GenericMSWorkstation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5)
)
_DeskManProduct_ObjectIdentity = ObjectIdentity
deskManProduct = _DeskManProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5, 1)
)
_EthernetSoftHub_ObjectIdentity = ObjectIdentity
ethernetSoftHub = _EthernetSoftHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5, 1, 1)
)
_EthernetDTAnode_ObjectIdentity = ObjectIdentity
ethernetDTAnode = _EthernetDTAnode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5, 1, 2)
)
_TokenRingSoftHub_ObjectIdentity = ObjectIdentity
tokenRingSoftHub = _TokenRingSoftHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5, 1, 3)
)
_TokenRingDTAnode_ObjectIdentity = ObjectIdentity
tokenRingDTAnode = _TokenRingDTAnode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5, 1, 4)
)
_GenericMSServer_ObjectIdentity = ObjectIdentity
genericMSServer = _GenericMSServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 6)
)
_GenericUnixServer_ObjectIdentity = ObjectIdentity
genericUnixServer = _GenericUnixServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 7)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8)
)
_LinkBuilder3GH_ObjectIdentity = ObjectIdentity
linkBuilder3GH = _LinkBuilder3GH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 1)
)
_LinkBuilder10BTi_ObjectIdentity = ObjectIdentity
linkBuilder10BTi = _LinkBuilder10BTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 2)
)
_LinkBuilderECS_ObjectIdentity = ObjectIdentity
linkBuilderECS = _LinkBuilderECS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3)
)
_LinkBuilderMSH_ObjectIdentity = ObjectIdentity
linkBuilderMSH = _LinkBuilderMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4)
)
_LinkBuilderFMS_ObjectIdentity = ObjectIdentity
linkBuilderFMS = _LinkBuilderFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 5)
)
_LinkBuilderFddiWorkGroupHub_ObjectIdentity = ObjectIdentity
linkBuilderFddiWorkGroupHub = _LinkBuilderFddiWorkGroupHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 6)
)
_LinkBuilderFMSII_ObjectIdentity = ObjectIdentity
linkBuilderFMSII = _LinkBuilderFMSII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 7)
)
_LinkSwitchFMS_ObjectIdentity = ObjectIdentity
linkSwitchFMS = _LinkSwitchFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 8)
)
_LinkSwitchMSH_ObjectIdentity = ObjectIdentity
linkSwitchMSH = _LinkSwitchMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 9)
)
_LinkBuilderFMSLBridge_ObjectIdentity = ObjectIdentity
linkBuilderFMSLBridge = _LinkBuilderFMSLBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 10)
)
_LinkBuilderTP8i_ObjectIdentity = ObjectIdentity
linkBuilderTP8i = _LinkBuilderTP8i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 11)
)
_LinkBuilderMSHFddi_ObjectIdentity = ObjectIdentity
linkBuilderMSHFddi = _LinkBuilderMSHFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 12)
)
_LinkSwitch1000_ObjectIdentity = ObjectIdentity
linkSwitch1000 = _LinkSwitch1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 13)
)
_LinkSwitch500_ObjectIdentity = ObjectIdentity
linkSwitch500 = _LinkSwitch500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 14)
)
_LinkSwitch2700AU_ObjectIdentity = ObjectIdentity
linkSwitch2700AU = _LinkSwitch2700AU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 15)
)
_LinkSwitch2700Bridge_ObjectIdentity = ObjectIdentity
linkSwitch2700Bridge = _LinkSwitch2700Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 16)
)
_LinkBuilderFMS100LBridge_ObjectIdentity = ObjectIdentity
linkBuilderFMS100LBridge = _LinkBuilderFMS100LBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 17)
)
_LinkSwitch2700TliAU_ObjectIdentity = ObjectIdentity
linkSwitch2700TliAU = _LinkSwitch2700TliAU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 18)
)
_LinkSwitch2700TliBridge_ObjectIdentity = ObjectIdentity
linkSwitch2700TliBridge = _LinkSwitch2700TliBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 19)
)
_LinkBuilderFMS100_ObjectIdentity = ObjectIdentity
linkBuilderFMS100 = _LinkBuilderFMS100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 20)
)
_OfficeConnect_Hub8M_ObjectIdentity = ObjectIdentity
officeConnect_Hub8M = _OfficeConnect_Hub8M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 21)
)
_LinkSwitch3000_ObjectIdentity = ObjectIdentity
linkSwitch3000 = _LinkSwitch3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 22)
)
_MshSwitch_ObjectIdentity = ObjectIdentity
mshSwitch = _MshSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 23)
)
_LinkSwitch2000TR_ObjectIdentity = ObjectIdentity
linkSwitch2000TR = _LinkSwitch2000TR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 24)
)
_OncoreFastModuleFPA100_ObjectIdentity = ObjectIdentity
oncoreFastModuleFPA100 = _OncoreFastModuleFPA100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 25)
)
_OncoreFastModuleFPA10_ObjectIdentity = ObjectIdentity
oncoreFastModuleFPA10 = _OncoreFastModuleFPA10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 26)
)
_OncoreFastModuleFPA10FX_ObjectIdentity = ObjectIdentity
oncoreFastModuleFPA10FX = _OncoreFastModuleFPA10FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 27)
)
_OncoreFastModuleBPA_ObjectIdentity = ObjectIdentity
oncoreFastModuleBPA = _OncoreFastModuleBPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 28)
)
_SuperStackDesktopSwitch_ObjectIdentity = ObjectIdentity
superStackDesktopSwitch = _SuperStackDesktopSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 29)
)
_OncoreFastModuleFPA100TX_ObjectIdentity = ObjectIdentity
oncoreFastModuleFPA100TX = _OncoreFastModuleFPA100TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 30)
)
_OfficeConnect_Switch140M_ObjectIdentity = ObjectIdentity
officeConnect_Switch140M = _OfficeConnect_Switch140M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 31)
)
_SuperStackSwitch9000SX_ObjectIdentity = ObjectIdentity
superStackSwitch9000SX = _SuperStackSwitch9000SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 32)
)
_CoreBuilder9000_ObjectIdentity = ObjectIdentity
coreBuilder9000 = _CoreBuilder9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 33)
)
_CoreBuilder9000_chassis_ObjectIdentity = ObjectIdentity
coreBuilder9000_chassis = _CoreBuilder9000_chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 33, 2)
)
_CoreBuilder9000_16slot_ObjectIdentity = ObjectIdentity
coreBuilder9000_16slot = _CoreBuilder9000_16slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 33, 2, 1)
)
_CoreBuilder9000_7slot_ObjectIdentity = ObjectIdentity
coreBuilder9000_7slot = _CoreBuilder9000_7slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 33, 2, 2)
)
_CoreBuilder9000_8slot_ObjectIdentity = ObjectIdentity
coreBuilder9000_8slot = _CoreBuilder9000_8slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 33, 2, 3)
)
_CoreBuilder9000_4slot_ObjectIdentity = ObjectIdentity
coreBuilder9000_4slot = _CoreBuilder9000_4slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 33, 2, 4)
)
_SuperStackSwitch3800_ObjectIdentity = ObjectIdentity
superStackSwitch3800 = _SuperStackSwitch3800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 34)
)
_Cb5000TRFastModule_ObjectIdentity = ObjectIdentity
cb5000TRFastModule = _Cb5000TRFastModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 35)
)
_SuperStackSwitch9100_ObjectIdentity = ObjectIdentity
superStackSwitch9100 = _SuperStackSwitch9100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 36)
)
_SuperStackSwitchSoyuz_ObjectIdentity = ObjectIdentity
superStackSwitchSoyuz = _SuperStackSwitchSoyuz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 37)
)
_SuperStackSwitch4300_ObjectIdentity = ObjectIdentity
superStackSwitch4300 = _SuperStackSwitch4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 38)
)
_SuperStackSwitch3824_ObjectIdentity = ObjectIdentity
superStackSwitch3824 = _SuperStackSwitch3824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 39)
)
_SuperStackSwitch3812_ObjectIdentity = ObjectIdentity
superStackSwitch3812 = _SuperStackSwitch3812_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 40)
)
_Switch3226_ObjectIdentity = ObjectIdentity
switch3226 = _Switch3226_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 41)
)
_Switch3250_ObjectIdentity = ObjectIdentity
switch3250 = _Switch3250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 42)
)
_Switch3870_24_port_ObjectIdentity = ObjectIdentity
switch3870_24_port = _Switch3870_24_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 43)
)
_Switch3870_48_port_ObjectIdentity = ObjectIdentity
switch3870_48_port = _Switch3870_48_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 44)
)
_Switch3848_ObjectIdentity = ObjectIdentity
switch3848 = _Switch3848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 45)
)
_Switch3228_ObjectIdentity = ObjectIdentity
switch3228 = _Switch3228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 46)
)
_Switch3252_ObjectIdentity = ObjectIdentity
switch3252 = _Switch3252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 47)
)
_Cards_ObjectIdentity = ObjectIdentity
cards = _Cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9)
)
_LinkBuilder3GH_cards_ObjectIdentity = ObjectIdentity
linkBuilder3GH_cards = _LinkBuilder3GH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 1)
)
_LinkBuilder10BTi_cards_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards = _LinkBuilder10BTi_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2)
)
_LinkBuilder10BTi_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards_utp = _LinkBuilder10BTi_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 1)
)
_LinkBuilder10BT_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BT_cards_utp = _LinkBuilder10BT_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 2)
)
_LinkBuilderECS_cards_ObjectIdentity = ObjectIdentity
linkBuilderECS_cards = _LinkBuilderECS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 3)
)
_LinkBuilderMSH_cards_ObjectIdentity = ObjectIdentity
linkBuilderMSH_cards = _LinkBuilderMSH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 4)
)
_LinkBuilderFMS_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards = _LinkBuilderFMS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5)
)
_LinkBuilderFMS_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_utp = _LinkBuilderFMS_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 1)
)
_LinkBuilderFMS_cards_coax_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_coax = _LinkBuilderFMS_cards_coax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 2)
)
_LinkBuilderFMS_cards_fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_fiber = _LinkBuilderFMS_cards_fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 3)
)
_LinkBuilderFMS_cards_12fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_12fiber = _LinkBuilderFMS_cards_12fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 4)
)
_LinkBuilderFMS_cards_24utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_24utp = _LinkBuilderFMS_cards_24utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 5)
)
_LinkBuilderFMSII_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards = _LinkBuilderFMSII_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6)
)
_LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12tp_rj45 = _LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 1)
)
_LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_10coax_bnc = _LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 2)
)
_LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_6fiber_st = _LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 3)
)
_LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12fiber_st = _LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 4)
)
_LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_rj45 = _LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 5)
)
_LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_telco = _LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 6)
)
_SuperStackHub10_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
superStackHub10_cards_12tp_rj45 = _SuperStackHub10_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 7)
)
_SuperStackHub10_cards_24tp_rj45_ObjectIdentity = ObjectIdentity
superStackHub10_cards_24tp_rj45 = _SuperStackHub10_cards_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 8)
)
_SuperStackHub10_cards_6fiber_st_ObjectIdentity = ObjectIdentity
superStackHub10_cards_6fiber_st = _SuperStackHub10_cards_6fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 9)
)
_SuperStackHub10_cards_24tp_telco_ObjectIdentity = ObjectIdentity
superStackHub10_cards_24tp_telco = _SuperStackHub10_cards_24tp_telco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 10)
)
_A3C512_ObjectIdentity = ObjectIdentity
a3C512 = _A3C512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 7)
)
_A3C512_withBNC_expn_card_ObjectIdentity = ObjectIdentity
a3C512_withBNC_expn_card = _A3C512_withBNC_expn_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 7, 1)
)
_A3C512_withAUI_expn_card_ObjectIdentity = ObjectIdentity
a3C512_withAUI_expn_card = _A3C512_withAUI_expn_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 7, 2)
)
_A3C512_withFOIRL_expn_card_ObjectIdentity = ObjectIdentity
a3C512_withFOIRL_expn_card = _A3C512_withFOIRL_expn_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 7, 3)
)
_LinkBuilderTP8i_cards_ObjectIdentity = ObjectIdentity
linkBuilderTP8i_cards = _LinkBuilderTP8i_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 8)
)
_LinkBuilderTP8i_cards_8tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderTP8i_cards_8tp_rj45 = _LinkBuilderTP8i_cards_8tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 8, 1)
)
_LinkSwitch1000_cards_ObjectIdentity = ObjectIdentity
linkSwitch1000_cards = _LinkSwitch1000_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9)
)
_LinkSwitch1000_cards_24tp_rj45_ObjectIdentity = ObjectIdentity
linkSwitch1000_cards_24tp_rj45 = _LinkSwitch1000_cards_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 1)
)
_LinkSwitch1000_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
linkSwitch1000_cards_12tp_rj45 = _LinkSwitch1000_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 2)
)
_LinkSwitch3000_cards_5fiber_sc_ObjectIdentity = ObjectIdentity
linkSwitch3000_cards_5fiber_sc = _LinkSwitch3000_cards_5fiber_sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 3)
)
_LinkSwitch3000_cards_8tp_rj45_ObjectIdentity = ObjectIdentity
linkSwitch3000_cards_8tp_rj45 = _LinkSwitch3000_cards_8tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 4)
)
_SuperStackSwitch1000_cards_24tp_rj45_ObjectIdentity = ObjectIdentity
superStackSwitch1000_cards_24tp_rj45 = _SuperStackSwitch1000_cards_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 5)
)
_SuperStackSwitch1000_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
superStackSwitch1000_cards_12tp_rj45 = _SuperStackSwitch1000_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 6)
)
_SuperStackSwitch3000_cards_5fiber_sc_ObjectIdentity = ObjectIdentity
superStackSwitch3000_cards_5fiber_sc = _SuperStackSwitch3000_cards_5fiber_sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 7)
)
_SuperStackSwitch3000_cards_8tp_rj45_ObjectIdentity = ObjectIdentity
superStackSwitch3000_cards_8tp_rj45 = _SuperStackSwitch3000_cards_8tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 8)
)
_Oncore_cards_5fiber_sc_2tp_rj45_blk_ObjectIdentity = ObjectIdentity
oncore_cards_5fiber_sc_2tp_rj45_blk = _Oncore_cards_5fiber_sc_2tp_rj45_blk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 9)
)
_Oncore_cards_24tp_telco_blk_ObjectIdentity = ObjectIdentity
oncore_cards_24tp_telco_blk = _Oncore_cards_24tp_telco_blk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 10)
)
_Oncore_cards_24tp_telco_1fiber_sc_blk_ObjectIdentity = ObjectIdentity
oncore_cards_24tp_telco_1fiber_sc_blk = _Oncore_cards_24tp_telco_1fiber_sc_blk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 11)
)
_Oncore_cards_1fiber_sc_7blk_ObjectIdentity = ObjectIdentity
oncore_cards_1fiber_sc_7blk = _Oncore_cards_1fiber_sc_7blk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 12)
)
_SuperStackSwitch1000_3000_cards_atm_ObjectIdentity = ObjectIdentity
superStackSwitch1000_3000_cards_atm = _SuperStackSwitch1000_3000_cards_atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 13)
)
_Oncore_cards_2fiber_sc_7blk_ObjectIdentity = ObjectIdentity
oncore_cards_2fiber_sc_7blk = _Oncore_cards_2fiber_sc_7blk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 14)
)
_Oncore_cards_1fiber_sc_tp_rj45_7blk_ObjectIdentity = ObjectIdentity
oncore_cards_1fiber_sc_tp_rj45_7blk = _Oncore_cards_1fiber_sc_tp_rj45_7blk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 15)
)
_Oncore_cards_1fiber_sc_atm_7blk_ObjectIdentity = ObjectIdentity
oncore_cards_1fiber_sc_atm_7blk = _Oncore_cards_1fiber_sc_atm_7blk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 16)
)
_SuperStackDesktopSwitch_24tp_rj45_ObjectIdentity = ObjectIdentity
superStackDesktopSwitch_24tp_rj45 = _SuperStackDesktopSwitch_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 17)
)
_LinkSwitch3000_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
linkSwitch3000_cards_12tp_rj45 = _LinkSwitch3000_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 18)
)
_SuperStackSwitch3000_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
superStackSwitch3000_cards_12tp_rj45 = _SuperStackSwitch3000_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 19)
)
_Oncore_cards_7tp_rj45_blk_ObjectIdentity = ObjectIdentity
oncore_cards_7tp_rj45_blk = _Oncore_cards_7tp_rj45_blk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 20)
)
_OfficeConnect_Switch140M_5tp_rj45_ObjectIdentity = ObjectIdentity
officeConnect_Switch140M_5tp_rj45 = _OfficeConnect_Switch140M_5tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 21)
)
_SuperStackSwitch3000_cards_12tp_rj45_ten100_ObjectIdentity = ObjectIdentity
superStackSwitch3000_cards_12tp_rj45_ten100 = _SuperStackSwitch3000_cards_12tp_rj45_ten100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 9, 22)
)
_LinkBuilderFMS100_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMS100_cards = _LinkBuilderFMS100_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 10)
)
_LinkBuilderFMS100_cards_12utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS100_cards_12utp = _LinkBuilderFMS100_cards_12utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 10, 1)
)
_LinkBuilderFMS100_cards_12T4_ObjectIdentity = ObjectIdentity
linkBuilderFMS100_cards_12T4 = _LinkBuilderFMS100_cards_12T4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 10, 2)
)
_LinkBuilderFMS100_cards_24TX_ObjectIdentity = ObjectIdentity
linkBuilderFMS100_cards_24TX = _LinkBuilderFMS100_cards_24TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 10, 3)
)
_LinkBuilderFMS100_cards_12TX_ObjectIdentity = ObjectIdentity
linkBuilderFMS100_cards_12TX = _LinkBuilderFMS100_cards_12TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 10, 4)
)
_OfficeConnect_Hub8M_cards_ObjectIdentity = ObjectIdentity
officeConnect_Hub8M_cards = _OfficeConnect_Hub8M_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 11)
)
_OfficeConnect_Hub8M_cards_8tp_rj45_ObjectIdentity = ObjectIdentity
officeConnect_Hub8M_cards_8tp_rj45 = _OfficeConnect_Hub8M_cards_8tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 11, 1)
)
_LinkSwitch2000TR_cards_ObjectIdentity = ObjectIdentity
linkSwitch2000TR_cards = _LinkSwitch2000TR_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 12)
)
_LinkSwitch2000TR_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
linkSwitch2000TR_cards_12tp_rj45 = _LinkSwitch2000TR_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 12, 1)
)
_CoreBuilder9000_cards_ObjectIdentity = ObjectIdentity
coreBuilder9000_cards = _CoreBuilder9000_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13)
)
_CoreBuilder9000_packet_cards_ObjectIdentity = ObjectIdentity
coreBuilder9000_packet_cards = _CoreBuilder9000_packet_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1)
)
_Cb9000_layer2_switch_cards_ObjectIdentity = ObjectIdentity
cb9000_layer2_switch_cards = _Cb9000_layer2_switch_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1)
)
_Cb9000_cards_20_rj45_10T_100T_ObjectIdentity = ObjectIdentity
cb9000_cards_20_rj45_10T_100T = _Cb9000_cards_20_rj45_10T_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 1)
)
_Cb9000_cards_36_rj45_10T_100T_ObjectIdentity = ObjectIdentity
cb9000_cards_36_rj45_10T_100T = _Cb9000_cards_36_rj45_10T_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 2)
)
_Cb9000_cards_36_rj45_10T_ObjectIdentity = ObjectIdentity
cb9000_cards_36_rj45_10T = _Cb9000_cards_36_rj45_10T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 3)
)
_Cb9000_cards_10_fiber_100T_ObjectIdentity = ObjectIdentity
cb9000_cards_10_fiber_100T = _Cb9000_cards_10_fiber_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 4)
)
_Cb9000_cards_36_telco_10T_100T_ObjectIdentity = ObjectIdentity
cb9000_cards_36_telco_10T_100T = _Cb9000_cards_36_telco_10T_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 5)
)
_Cb9000_cards_9_fiber_1000T_ObjectIdentity = ObjectIdentity
cb9000_cards_9_fiber_1000T = _Cb9000_cards_9_fiber_1000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 6)
)
_Cb9000_cards_20_mt_fiber_100T_ObjectIdentity = ObjectIdentity
cb9000_cards_20_mt_fiber_100T = _Cb9000_cards_20_mt_fiber_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 7)
)
_Cb9000_cards_tb_36_rj45_10T_100T_ObjectIdentity = ObjectIdentity
cb9000_cards_tb_36_rj45_10T_100T = _Cb9000_cards_tb_36_rj45_10T_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 8)
)
_Cb9000_cards_tb_36_telco_10T_100T_ObjectIdentity = ObjectIdentity
cb9000_cards_tb_36_telco_10T_100T = _Cb9000_cards_tb_36_telco_10T_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 9)
)
_Cb9000_cards_20_fiber_1000T_ObjectIdentity = ObjectIdentity
cb9000_cards_20_fiber_1000T = _Cb9000_cards_20_fiber_1000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 10)
)
_Cb9000_cards_9_fiber_1000LX_ObjectIdentity = ObjectIdentity
cb9000_cards_9_fiber_1000LX = _Cb9000_cards_9_fiber_1000LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 11)
)
_Cb9000_cards_12BT_1000T_ObjectIdentity = ObjectIdentity
cb9000_cards_12BT_1000T = _Cb9000_cards_12BT_1000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 1, 12)
)
_Cb9000_layer3_switch_cards_ObjectIdentity = ObjectIdentity
cb9000_layer3_switch_cards = _Cb9000_layer3_switch_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 2)
)
_Cb9000_cards_12_rj45_100T_ObjectIdentity = ObjectIdentity
cb9000_cards_12_rj45_100T = _Cb9000_cards_12_rj45_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 2, 1)
)
_Cb9000_cards_6_fddi_ObjectIdentity = ObjectIdentity
cb9000_cards_6_fddi = _Cb9000_cards_6_fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 2, 2)
)
_Cb9000_cards_router_ObjectIdentity = ObjectIdentity
cb9000_cards_router = _Cb9000_cards_router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 2, 3)
)
_Cb9000_cards_10_fiber_ObjectIdentity = ObjectIdentity
cb9000_cards_10_fiber = _Cb9000_cards_10_fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 2, 4)
)
_Cb9000_cards_4_gbic_1000T_ObjectIdentity = ObjectIdentity
cb9000_cards_4_gbic_1000T = _Cb9000_cards_4_gbic_1000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 2, 5)
)
_Cb9000_cards_carrier_ObjectIdentity = ObjectIdentity
cb9000_cards_carrier = _Cb9000_cards_carrier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 2, 6)
)
_Cb9000_cards_18tx_ObjectIdentity = ObjectIdentity
cb9000_cards_18tx = _Cb9000_cards_18tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 2, 7)
)
_Cb9000_cards_18fx_ObjectIdentity = ObjectIdentity
cb9000_cards_18fx = _Cb9000_cards_18fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 2, 8)
)
_Cb9000_layer2_fabric_cards_ObjectIdentity = ObjectIdentity
cb9000_layer2_fabric_cards = _Cb9000_layer2_fabric_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 3)
)
_Cb9000_cards_fabric_24_ObjectIdentity = ObjectIdentity
cb9000_cards_fabric_24 = _Cb9000_cards_fabric_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 3, 1)
)
_Cb9000_cards_fabric_24T_ObjectIdentity = ObjectIdentity
cb9000_cards_fabric_24T = _Cb9000_cards_fabric_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 3, 2)
)
_Cb9000_cards_fabric_6_3_ObjectIdentity = ObjectIdentity
cb9000_cards_fabric_6_3 = _Cb9000_cards_fabric_6_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 3, 3)
)
_Cb9000_cards_fabric_36_ObjectIdentity = ObjectIdentity
cb9000_cards_fabric_36 = _Cb9000_cards_fabric_36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 3, 4)
)
_Cb9000_layer1_cards_ObjectIdentity = ObjectIdentity
cb9000_layer1_cards = _Cb9000_layer1_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 4)
)
_Cb9000_cards_2_fiber_1000T_ObjectIdentity = ObjectIdentity
cb9000_cards_2_fiber_1000T = _Cb9000_cards_2_fiber_1000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 4, 1)
)
_Cb9000_cards_4_fiber_1000T_ObjectIdentity = ObjectIdentity
cb9000_cards_4_fiber_1000T = _Cb9000_cards_4_fiber_1000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 4, 2)
)
_Cb9000_cards_2_fiber_lx_1000T_ObjectIdentity = ObjectIdentity
cb9000_cards_2_fiber_lx_1000T = _Cb9000_cards_2_fiber_lx_1000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 4, 3)
)
_Cb9000_layer2_tb_cards_ObjectIdentity = ObjectIdentity
cb9000_layer2_tb_cards = _Cb9000_layer2_tb_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 5)
)
_Cb9000_layer3_fabric_cards_ObjectIdentity = ObjectIdentity
cb9000_layer3_fabric_cards = _Cb9000_layer3_fabric_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 6)
)
_Cb9000_cards_fabric_fba8_ObjectIdentity = ObjectIdentity
cb9000_cards_fabric_fba8 = _Cb9000_cards_fabric_fba8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 6, 1)
)
_Cb9000_cards_fabric_16_ObjectIdentity = ObjectIdentity
cb9000_cards_fabric_16 = _Cb9000_cards_fabric_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 1, 6, 2)
)
_CoreBuilder9000_cell_cards_ObjectIdentity = ObjectIdentity
coreBuilder9000_cell_cards = _CoreBuilder9000_cell_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2)
)
_Cb9000_cell_switch_cards_ObjectIdentity = ObjectIdentity
cb9000_cell_switch_cards = _Cb9000_cell_switch_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1)
)
_Cb9000_cell_carrier_cards_ObjectIdentity = ObjectIdentity
cb9000_cell_carrier_cards = _Cb9000_cell_carrier_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 1)
)
_Cb9000_cell_modularIfc_2_groups_ObjectIdentity = ObjectIdentity
cb9000_cell_modularIfc_2_groups = _Cb9000_cell_modularIfc_2_groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 1, 1)
)
_Cb9000_cell_daughter_cards_ObjectIdentity = ObjectIdentity
cb9000_cell_daughter_cards = _Cb9000_cell_daughter_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2)
)
_Cb9000_cell_1_OC12_MM_ObjectIdentity = ObjectIdentity
cb9000_cell_1_OC12_MM = _Cb9000_cell_1_OC12_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 1)
)
_Cb9000_cell_1_OC12_SM_ObjectIdentity = ObjectIdentity
cb9000_cell_1_OC12_SM = _Cb9000_cell_1_OC12_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 2)
)
_Cb9000_cell_4_OC3_MM_ObjectIdentity = ObjectIdentity
cb9000_cell_4_OC3_MM = _Cb9000_cell_4_OC3_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 3)
)
_Cb9000_cell_4_OC3_SM_ObjectIdentity = ObjectIdentity
cb9000_cell_4_OC3_SM = _Cb9000_cell_4_OC3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 4)
)
_Cb9000_cell_1_OC3_SM_3_OC3_MM_ObjectIdentity = ObjectIdentity
cb9000_cell_1_OC3_SM_3_OC3_MM = _Cb9000_cell_1_OC3_SM_3_OC3_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 5)
)
_Cb9000_cell_4_OC3_rj45_ObjectIdentity = ObjectIdentity
cb9000_cell_4_OC3_rj45 = _Cb9000_cell_4_OC3_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 6)
)
_Cb9000_cell_2_T3_BNC_ObjectIdentity = ObjectIdentity
cb9000_cell_2_T3_BNC = _Cb9000_cell_2_T3_BNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 7)
)
_Cb9000_cell_2_E3_BNC_ObjectIdentity = ObjectIdentity
cb9000_cell_2_E3_BNC = _Cb9000_cell_2_E3_BNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 8)
)
_Cb9000_cell_4_OC3_SM_LR_ObjectIdentity = ObjectIdentity
cb9000_cell_4_OC3_SM_LR = _Cb9000_cell_4_OC3_SM_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 9)
)
_Cb9000_cell_2_OC3_SM_LR_ObjectIdentity = ObjectIdentity
cb9000_cell_2_OC3_SM_LR = _Cb9000_cell_2_OC3_SM_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 2, 10)
)
_Cb9000_cell_integrated_cards_ObjectIdentity = ObjectIdentity
cb9000_cell_integrated_cards = _Cb9000_cell_integrated_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 3)
)
_Cb9000_cell_8_T1_IMA_rj48c_ObjectIdentity = ObjectIdentity
cb9000_cell_8_T1_IMA_rj48c = _Cb9000_cell_8_T1_IMA_rj48c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 3, 1)
)
_Cb9000_cell_8_E1_IMA_rj48c_ObjectIdentity = ObjectIdentity
cb9000_cell_8_E1_IMA_rj48c = _Cb9000_cell_8_E1_IMA_rj48c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 3, 2)
)
_Cb9000_cell_8_T1_CES_rj48c_ObjectIdentity = ObjectIdentity
cb9000_cell_8_T1_CES_rj48c = _Cb9000_cell_8_T1_CES_rj48c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 3, 3)
)
_Cb9000_cell_8_E1_CES_rj48c_ObjectIdentity = ObjectIdentity
cb9000_cell_8_E1_CES_rj48c = _Cb9000_cell_8_E1_CES_rj48c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 3, 4)
)
_Cb9000_cell_combined_cards_ObjectIdentity = ObjectIdentity
cb9000_cell_combined_cards = _Cb9000_cell_combined_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 4)
)
_Cb9000_cellsw_4_fiber_1000T_ObjectIdentity = ObjectIdentity
cb9000_cellsw_4_fiber_1000T = _Cb9000_cellsw_4_fiber_1000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 4, 1)
)
_Cb9000_cellsw_20_rj45_10T_100T_ObjectIdentity = ObjectIdentity
cb9000_cellsw_20_rj45_10T_100T = _Cb9000_cellsw_20_rj45_10T_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 4, 2)
)
_Cb9000_cellsw_36_rj45_10T_100T_ObjectIdentity = ObjectIdentity
cb9000_cellsw_36_rj45_10T_100T = _Cb9000_cellsw_36_rj45_10T_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 4, 3)
)
_Cb9000_cellsw_36_telco_10T_100T_ObjectIdentity = ObjectIdentity
cb9000_cellsw_36_telco_10T_100T = _Cb9000_cellsw_36_telco_10T_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 4, 4)
)
_Cb9000_cellsw_40_telco_10T_100T_ObjectIdentity = ObjectIdentity
cb9000_cellsw_40_telco_10T_100T = _Cb9000_cellsw_40_telco_10T_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 1, 4, 5)
)
_Cb9000_cell_fabric_cards_ObjectIdentity = ObjectIdentity
cb9000_cell_fabric_cards = _Cb9000_cell_fabric_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 2)
)
_Cb9000_cards_cell_fabric_1_ObjectIdentity = ObjectIdentity
cb9000_cards_cell_fabric_1 = _Cb9000_cards_cell_fabric_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 2, 1)
)
_Cb9000_cards_cell_fabric_1_7slot_ObjectIdentity = ObjectIdentity
cb9000_cards_cell_fabric_1_7slot = _Cb9000_cards_cell_fabric_1_7slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 2, 2, 2)
)
_CoreBuilder9000_mgmt_cards_ObjectIdentity = ObjectIdentity
coreBuilder9000_mgmt_cards = _CoreBuilder9000_mgmt_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 3)
)
_Cb9000_cards_eme_ObjectIdentity = ObjectIdentity
cb9000_cards_eme = _Cb9000_cards_eme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 3, 1)
)
_Cb9000_cards_emec_ObjectIdentity = ObjectIdentity
cb9000_cards_emec = _Cb9000_cards_emec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 3, 2)
)
_Cb9000_cards_emel_ObjectIdentity = ObjectIdentity
cb9000_cards_emel = _Cb9000_cards_emel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 3, 3)
)
_CoreBuilder9000_app_cards_ObjectIdentity = ObjectIdentity
coreBuilder9000_app_cards = _CoreBuilder9000_app_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 4)
)
_Cb9000_app_BIG_ip_ObjectIdentity = ObjectIdentity
cb9000_app_BIG_ip = _Cb9000_app_BIG_ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 4, 1)
)
_Cb9000_app_3DNS_ObjectIdentity = ObjectIdentity
cb9000_app_3DNS = _Cb9000_app_3DNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 4, 2)
)
_Cb9000_app_global_site_ObjectIdentity = ObjectIdentity
cb9000_app_global_site = _Cb9000_app_global_site_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 13, 4, 3)
)
_Cb5000TRFastModule_cards_ObjectIdentity = ObjectIdentity
cb5000TRFastModule_cards = _Cb5000TRFastModule_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 14)
)
_Cb5000TRFastModule_card_6508M_ObjectIdentity = ObjectIdentity
cb5000TRFastModule_card_6508M = _Cb5000TRFastModule_card_6508M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 14, 1)
)
_Cb5000TRFastModule_card_6508M2_ObjectIdentity = ObjectIdentity
cb5000TRFastModule_card_6508M2 = _Cb5000TRFastModule_card_6508M2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 14, 2)
)
_Cb5000TRFastModule_card_atm_ObjectIdentity = ObjectIdentity
cb5000TRFastModule_card_atm = _Cb5000TRFastModule_card_atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 14, 3)
)
_Cb5000TRFastModule_card_fddi_ObjectIdentity = ObjectIdentity
cb5000TRFastModule_card_fddi = _Cb5000TRFastModule_card_fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 14, 4)
)
_Cb5000TRFastModule_card_tif_sc_ObjectIdentity = ObjectIdentity
cb5000TRFastModule_card_tif_sc = _Cb5000TRFastModule_card_tif_sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 14, 5)
)
_Cb5000TRFastModule_card_tif_rj45_ObjectIdentity = ObjectIdentity
cb5000TRFastModule_card_tif_rj45 = _Cb5000TRFastModule_card_tif_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 14, 6)
)
_SuperStack3300_cards_ObjectIdentity = ObjectIdentity
superStack3300_cards = _SuperStack3300_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 15)
)
_Stanley_ObjectIdentity = ObjectIdentity
stanley = _Stanley_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 15, 1)
)
_SuperStack_3300_atm_uplink_ObjectIdentity = ObjectIdentity
superStack_3300_atm_uplink = _SuperStack_3300_atm_uplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 15, 2)
)
_ChipSets_ObjectIdentity = ObjectIdentity
chipSets = _ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 10)
)
_Valcan_ObjectIdentity = ObjectIdentity
valcan = _Valcan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 10, 1)
)
_Oem_ObjectIdentity = ObjectIdentity
oem = _Oem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 11)
)
_LinkConv250_ObjectIdentity = ObjectIdentity
linkConv250 = _LinkConv250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 11, 1)
)
_LinkConv251_ObjectIdentity = ObjectIdentity
linkConv251 = _LinkConv251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 11, 2)
)
_LinkConv350_ObjectIdentity = ObjectIdentity
linkConv350 = _LinkConv350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 11, 3)
)
_LinkConv351_ObjectIdentity = ObjectIdentity
linkConv351 = _LinkConv351_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 11, 4)
)
_Atm_ObjectIdentity = ObjectIdentity
atm = _Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12)
)
_CELLplex7000_ObjectIdentity = ObjectIdentity
cELLplex7000 = _CELLplex7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 1)
)
_CELLplex7000_cards_ObjectIdentity = ObjectIdentity
cELLplex7000_cards = _CELLplex7000_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 2)
)
_CELLplex_7x00cardBridge_ObjectIdentity = ObjectIdentity
cELLplex_7x00cardBridge = _CELLplex_7x00cardBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 2, 1)
)
_CELLplex_7200card_ObjectIdentity = ObjectIdentity
cELLplex_7200card = _CELLplex_7200card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 2, 2)
)
_CELLplex_7200Fcard_ObjectIdentity = ObjectIdentity
cELLplex_7200Fcard = _CELLplex_7200Fcard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 2, 3)
)
_CELLplex_7400card_ObjectIdentity = ObjectIdentity
cELLplex_7400card = _CELLplex_7400card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 2, 4)
)
_CELLplex_7600card_ObjectIdentity = ObjectIdentity
cELLplex_7600card = _CELLplex_7600card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 2, 5)
)
_CELLplex_7800card_ObjectIdentity = ObjectIdentity
cELLplex_7800card = _CELLplex_7800card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 2, 6)
)
_CELLplex_7900card_ObjectIdentity = ObjectIdentity
cELLplex_7900card = _CELLplex_7900card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 2, 7)
)
_PathBuilder_ObjectIdentity = ObjectIdentity
pathBuilder = _PathBuilder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 3)
)
_CoreBuilderSip7000_ObjectIdentity = ObjectIdentity
coreBuilderSip7000 = _CoreBuilderSip7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 4)
)
_Cb7000Family_ObjectIdentity = ObjectIdentity
cb7000Family = _Cb7000Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5)
)
_Cb7000_fabric_cards_ObjectIdentity = ObjectIdentity
cb7000_fabric_cards = _Cb7000_fabric_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 1)
)
_Cb7000_fabric_switch_ObjectIdentity = ObjectIdentity
cb7000_fabric_switch = _Cb7000_fabric_switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 1, 1)
)
_Cb7000_fabric_switch_hd_ObjectIdentity = ObjectIdentity
cb7000_fabric_switch_hd = _Cb7000_fabric_switch_hd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 1, 2)
)
_Cb7000_accelerator_cards_ObjectIdentity = ObjectIdentity
cb7000_accelerator_cards = _Cb7000_accelerator_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 2)
)
_Cb7000_FastBUS_ObjectIdentity = ObjectIdentity
cb7000_FastBUS = _Cb7000_FastBUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 2, 1)
)
_Cb7000_FastBUS_Java_ObjectIdentity = ObjectIdentity
cb7000_FastBUS_Java = _Cb7000_FastBUS_Java_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 2, 2)
)
_Cb7000_FastBUS_7600_ObjectIdentity = ObjectIdentity
cb7000_FastBUS_7600 = _Cb7000_FastBUS_7600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 2, 3)
)
_Cb7000_FastBUS_7600_Java_ObjectIdentity = ObjectIdentity
cb7000_FastBUS_7600_Java = _Cb7000_FastBUS_7600_Java_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 2, 4)
)
_Cb7000_carrier_cards_ObjectIdentity = ObjectIdentity
cb7000_carrier_cards = _Cb7000_carrier_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3)
)
_Cb7000_4_ports_ifc_ObjectIdentity = ObjectIdentity
cb7000_4_ports_ifc = _Cb7000_4_ports_ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3, 1)
)
_Cb7000_8_ports_ifc_ObjectIdentity = ObjectIdentity
cb7000_8_ports_ifc = _Cb7000_8_ports_ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3, 2)
)
_Cb7000_OC12_carrier_ifc_ObjectIdentity = ObjectIdentity
cb7000_OC12_carrier_ifc = _Cb7000_OC12_carrier_ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3, 3)
)
_Cb7000_7200_ifc_ObjectIdentity = ObjectIdentity
cb7000_7200_ifc = _Cb7000_7200_ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3, 4)
)
_Cb7000_7200F_ifc_ObjectIdentity = ObjectIdentity
cb7000_7200F_ifc = _Cb7000_7200F_ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3, 5)
)
_Cb7000_7400_ifc_ObjectIdentity = ObjectIdentity
cb7000_7400_ifc = _Cb7000_7400_ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3, 6)
)
_Cb7000_7600_ifc_ObjectIdentity = ObjectIdentity
cb7000_7600_ifc = _Cb7000_7600_ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3, 7)
)
_Cb7000_7800_ifc_ObjectIdentity = ObjectIdentity
cb7000_7800_ifc = _Cb7000_7800_ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3, 8)
)
_Cb7000_7900_ifc_ObjectIdentity = ObjectIdentity
cb7000_7900_ifc = _Cb7000_7900_ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 3, 9)
)
_Cb7000_daughter_cards_ObjectIdentity = ObjectIdentity
cb7000_daughter_cards = _Cb7000_daughter_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4)
)
_Cb7000_1_OC3_SM_ObjectIdentity = ObjectIdentity
cb7000_1_OC3_SM = _Cb7000_1_OC3_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 1)
)
_Cb7000_1_OC3_MM_ObjectIdentity = ObjectIdentity
cb7000_1_OC3_MM = _Cb7000_1_OC3_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 2)
)
_Cb7000_1_DS3_BNC_ObjectIdentity = ObjectIdentity
cb7000_1_DS3_BNC = _Cb7000_1_DS3_BNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 3)
)
_Cb7000_1_OC3_rj45_ObjectIdentity = ObjectIdentity
cb7000_1_OC3_rj45 = _Cb7000_1_OC3_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 4)
)
_Cb7000_1_OC12_SM_ObjectIdentity = ObjectIdentity
cb7000_1_OC12_SM = _Cb7000_1_OC12_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 5)
)
_Cb7000_1_OC12_MM_ObjectIdentity = ObjectIdentity
cb7000_1_OC12_MM = _Cb7000_1_OC12_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 6)
)
_Cb7000_12_10T_rj45_in_7200_ObjectIdentity = ObjectIdentity
cb7000_12_10T_rj45_in_7200 = _Cb7000_12_10T_rj45_in_7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 7)
)
_Cb7000_12_fiber_10T_FL_in_7200_ObjectIdentity = ObjectIdentity
cb7000_12_fiber_10T_FL_in_7200 = _Cb7000_12_fiber_10T_FL_in_7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 8)
)
_Cb7000_12_10T_rj21_ObjectIdentity = ObjectIdentity
cb7000_12_10T_rj21 = _Cb7000_12_10T_rj21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 9)
)
_Cb7000_2_fiber_100T_ObjectIdentity = ObjectIdentity
cb7000_2_fiber_100T = _Cb7000_2_fiber_100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 10)
)
_Cb7000_2_10T_100T_rj45_ObjectIdentity = ObjectIdentity
cb7000_2_10T_100T_rj45 = _Cb7000_2_10T_100T_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 11)
)
_Cb7000_4_fiber_1000T_in_7800_ObjectIdentity = ObjectIdentity
cb7000_4_fiber_1000T_in_7800 = _Cb7000_4_fiber_1000T_in_7800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 12)
)
_Cb7000_36_10T_100T_rj45_in_7900_ObjectIdentity = ObjectIdentity
cb7000_36_10T_100T_rj45_in_7900 = _Cb7000_36_10T_100T_rj45_in_7900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 13)
)
_Cb7000_1_E3_BNC_ObjectIdentity = ObjectIdentity
cb7000_1_E3_BNC = _Cb7000_1_E3_BNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 12, 5, 4, 14)
)
_PowerSupplies_ObjectIdentity = ObjectIdentity
powerSupplies = _PowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 13)
)
_RpsIIMgmtModule_ObjectIdentity = ObjectIdentity
rpsIIMgmtModule = _RpsIIMgmtModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 13, 1)
)
_Tdm_ObjectIdentity = ObjectIdentity
tdm = _Tdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 14)
)
_BroadbandAccess_ObjectIdentity = ObjectIdentity
broadbandAccess = _BroadbandAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 14, 1)
)
_CableModems_ObjectIdentity = ObjectIdentity
cableModems = _CableModems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 15)
)
_McnsCmHeadend_ObjectIdentity = ObjectIdentity
mcnsCmHeadend = _McnsCmHeadend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 15, 1)
)
_McnsExt2WayCm_ObjectIdentity = ObjectIdentity
mcnsExt2WayCm = _McnsExt2WayCm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 15, 2)
)
_McnsExtTelcoCm_ObjectIdentity = ObjectIdentity
mcnsExtTelcoCm = _McnsExtTelcoCm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 15, 3)
)
_Switches_ObjectIdentity = ObjectIdentity
switches = _Switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16)
)
_CorebuilderProductsIII_ObjectIdentity = ObjectIdentity
corebuilderProductsIII = _CorebuilderProductsIII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1)
)
_CorebuilderModularProducts_ObjectIdentity = ObjectIdentity
corebuilderModularProducts = _CorebuilderModularProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 1)
)
_CbModular3500Family_ObjectIdentity = ObjectIdentity
cbModular3500Family = _CbModular3500Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 1, 1)
)
_Cb3500_ObjectIdentity = ObjectIdentity
cb3500 = _Cb3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 1, 1, 1)
)
_CorebuilderSystemProducts_ObjectIdentity = ObjectIdentity
corebuilderSystemProducts = _CorebuilderSystemProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 2)
)
_CbSystem9400Family_ObjectIdentity = ObjectIdentity
cbSystem9400Family = _CbSystem9400Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 2, 1)
)
_Cb9400_ObjectIdentity = ObjectIdentity
cb9400 = _Cb9400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 2, 1, 1)
)
_CorebuilderChassisProducts_ObjectIdentity = ObjectIdentity
corebuilderChassisProducts = _CorebuilderChassisProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 3)
)
_SuperstackProducts_ObjectIdentity = ObjectIdentity
superstackProducts = _SuperstackProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2)
)
_SuperstackModularProducts_ObjectIdentity = ObjectIdentity
superstackModularProducts = _SuperstackModularProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 1)
)
_SuperstackSystemProducts_ObjectIdentity = ObjectIdentity
superstackSystemProducts = _SuperstackSystemProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2)
)
_SsSystem3900Family_ObjectIdentity = ObjectIdentity
ssSystem3900Family = _SsSystem3900Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 1)
)
_Ss3900_24_ObjectIdentity = ObjectIdentity
ss3900_24 = _Ss3900_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 1, 1)
)
_Ss3900_36_ObjectIdentity = ObjectIdentity
ss3900_36 = _Ss3900_36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 1, 2)
)
_SsSystem9300Family_ObjectIdentity = ObjectIdentity
ssSystem9300Family = _SsSystem9300Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 2)
)
_Ss9300_ObjectIdentity = ObjectIdentity
ss9300 = _Ss9300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 2, 1)
)
_SsServerLoadBalancers_ObjectIdentity = ObjectIdentity
ssServerLoadBalancers = _SsServerLoadBalancers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 3)
)
_BaseLoadBalancer_ObjectIdentity = ObjectIdentity
baseLoadBalancer = _BaseLoadBalancer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 3, 1)
)
_PlusLoadBalancer_ObjectIdentity = ObjectIdentity
plusLoadBalancer = _PlusLoadBalancer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 3, 2)
)
_SuperstackChassisProducts_ObjectIdentity = ObjectIdentity
superstackChassisProducts = _SuperstackChassisProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 3)
)
_MinicoreProducts_ObjectIdentity = ObjectIdentity
minicoreProducts = _MinicoreProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 3)
)
_MiniChassisSwitch4005_ObjectIdentity = ObjectIdentity
miniChassisSwitch4005 = _MiniChassisSwitch4005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 3, 1)
)
_JvProducts_ObjectIdentity = ObjectIdentity
jvProducts = _JvProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4)
)
_CoreChassisSwitch7700_ObjectIdentity = ObjectIdentity
coreChassisSwitch7700 = _CoreChassisSwitch7700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 1)
)
_JvRouters_ObjectIdentity = ObjectIdentity
jvRouters = _JvRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2)
)
_JvWanRouter5009_ObjectIdentity = ObjectIdentity
jvWanRouter5009 = _JvWanRouter5009_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 1)
)
_JvWanRouter5231_ObjectIdentity = ObjectIdentity
jvWanRouter5231 = _JvWanRouter5231_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 2)
)
_JvWanRouter5640_ObjectIdentity = ObjectIdentity
jvWanRouter5640 = _JvWanRouter5640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 3)
)
_JvWanRouter5680_ObjectIdentity = ObjectIdentity
jvWanRouter5680 = _JvWanRouter5680_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 4)
)
_JvWanRouter3012_ObjectIdentity = ObjectIdentity
jvWanRouter3012 = _JvWanRouter3012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 5)
)
_JvWanRouter3013_ObjectIdentity = ObjectIdentity
jvWanRouter3013 = _JvWanRouter3013_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 6)
)
_JvWanRouter3014_ObjectIdentity = ObjectIdentity
jvWanRouter3014 = _JvWanRouter3014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 7)
)
_JvWanRouter3015_ObjectIdentity = ObjectIdentity
jvWanRouter3015 = _JvWanRouter3015_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 8)
)
_JvWanRouter3016_ObjectIdentity = ObjectIdentity
jvWanRouter3016 = _JvWanRouter3016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 9)
)
_JvWanRouter3018_ObjectIdentity = ObjectIdentity
jvWanRouter3018 = _JvWanRouter3018_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 10)
)
_JvWanRouter6040_ObjectIdentity = ObjectIdentity
jvWanRouter6040 = _JvWanRouter6040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 11)
)
_JvWanRouter6080_ObjectIdentity = ObjectIdentity
jvWanRouter6080 = _JvWanRouter6080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 12)
)
_JvWanRouter3030_ObjectIdentity = ObjectIdentity
jvWanRouter3030 = _JvWanRouter3030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 13)
)
_JvWanRouter3031_ObjectIdentity = ObjectIdentity
jvWanRouter3031 = _JvWanRouter3031_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 14)
)
_JvWanRouter3032_ObjectIdentity = ObjectIdentity
jvWanRouter3032 = _JvWanRouter3032_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 15)
)
_JvWanRouter3033_ObjectIdentity = ObjectIdentity
jvWanRouter3033 = _JvWanRouter3033_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 16)
)
_JvWanRouter3034_ObjectIdentity = ObjectIdentity
jvWanRouter3034 = _JvWanRouter3034_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 17)
)
_JvRouter3035_ObjectIdentity = ObjectIdentity
jvRouter3035 = _JvRouter3035_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 18)
)
_JvRouterxxxx_ObjectIdentity = ObjectIdentity
jvRouterxxxx = _JvRouterxxxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 19)
)
_JvRouteryyyy_ObjectIdentity = ObjectIdentity
jvRouteryyyy = _JvRouteryyyy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 20)
)
_JvRouter5012_ObjectIdentity = ObjectIdentity
jvRouter5012 = _JvRouter5012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 21)
)
_JvRouter5232_ObjectIdentity = ObjectIdentity
jvRouter5232 = _JvRouter5232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 22)
)
_JvRouter5642_ObjectIdentity = ObjectIdentity
jvRouter5642 = _JvRouter5642_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 23)
)
_JvRouter5682_ObjectIdentity = ObjectIdentity
jvRouter5682 = _JvRouter5682_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 2, 24)
)
_JvSwitches_ObjectIdentity = ObjectIdentity
jvSwitches = _JvSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3)
)
_JvSwitch7700_8_ObjectIdentity = ObjectIdentity
jvSwitch7700_8 = _JvSwitch7700_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 1)
)
_JvSwitch7700_4_ObjectIdentity = ObjectIdentity
jvSwitch7700_4 = _JvSwitch7700_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 2)
)
_JvSwitch5500_MC6_EI_ObjectIdentity = ObjectIdentity
jvSwitch5500_MC6_EI = _JvSwitch5500_MC6_EI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 3)
)
_JvSwitch8807_ObjectIdentity = ObjectIdentity
jvSwitch8807 = _JvSwitch8807_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 4)
)
_JvSwitch8810_ObjectIdentity = ObjectIdentity
jvSwitch8810 = _JvSwitch8810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 5)
)
_JvSwitch8814_ObjectIdentity = ObjectIdentity
jvSwitch8814 = _JvSwitch8814_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 6)
)
_JvSwitch5500G_ei_24_ObjectIdentity = ObjectIdentity
jvSwitch5500G_ei_24 = _JvSwitch5500G_ei_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 7)
)
_JvSwitch5500G_ei_48_ObjectIdentity = ObjectIdentity
jvSwitch5500G_ei_48 = _JvSwitch5500G_ei_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 8)
)
_JvSwitch5500_si_24_ObjectIdentity = ObjectIdentity
jvSwitch5500_si_24 = _JvSwitch5500_si_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 9)
)
_JvSwitch5500_si_28t_ObjectIdentity = ObjectIdentity
jvSwitch5500_si_28t = _JvSwitch5500_si_28t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 10)
)
_JvSwitch5500_si_28_ObjectIdentity = ObjectIdentity
jvSwitch5500_si_28 = _JvSwitch5500_si_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 11)
)
_JvSwitch5500_si_52_ObjectIdentity = ObjectIdentity
jvSwitch5500_si_52 = _JvSwitch5500_si_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 12)
)
_JvSwitch5500_ei_28_ObjectIdentity = ObjectIdentity
jvSwitch5500_ei_28 = _JvSwitch5500_ei_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 13)
)
_JvSwitch5500_ei_52_ObjectIdentity = ObjectIdentity
jvSwitch5500_ei_52 = _JvSwitch5500_ei_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 14)
)
_JvSwitch5500_eipwr_28_ObjectIdentity = ObjectIdentity
jvSwitch5500_eipwr_28 = _JvSwitch5500_eipwr_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 15)
)
_JvSwitch5500_eipwr_52_ObjectIdentity = ObjectIdentity
jvSwitch5500_eipwr_52 = _JvSwitch5500_eipwr_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 16)
)
_JvSwitch5500_ei_28fx_ObjectIdentity = ObjectIdentity
jvSwitch5500_ei_28fx = _JvSwitch5500_ei_28fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 4, 3, 17)
)
_Voice_ObjectIdentity = ObjectIdentity
voice = _Voice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17)
)
_Phones_ObjectIdentity = ObjectIdentity
phones = _Phones_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 1)
)
_BasicPhone_ObjectIdentity = ObjectIdentity
basicPhone = _BasicPhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 1, 1)
)
_BusinessPhone_ObjectIdentity = ObjectIdentity
businessPhone = _BusinessPhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 1, 2)
)
_Bp3104ProfessionalPhone_ObjectIdentity = ObjectIdentity
bp3104ProfessionalPhone = _Bp3104ProfessionalPhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 1, 2, 1)
)
_ExecutivePhone_ObjectIdentity = ObjectIdentity
executivePhone = _ExecutivePhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 1, 3)
)
_WirelessPhone_ObjectIdentity = ObjectIdentity
wirelessPhone = _WirelessPhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 1, 4)
)
_Gateways_ObjectIdentity = ObjectIdentity
gateways = _Gateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 2)
)
_CallProcessors_ObjectIdentity = ObjectIdentity
callProcessors = _CallProcessors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 3)
)
_Nbx100_ObjectIdentity = ObjectIdentity
nbx100 = _Nbx100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 3, 1)
)
_Nbx25_ObjectIdentity = ObjectIdentity
nbx25 = _Nbx25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 3, 2)
)
_SuperStackNbxCallProcessor_ObjectIdentity = ObjectIdentity
superStackNbxCallProcessor = _SuperStackNbxCallProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 3, 3)
)
_Nbx250_ObjectIdentity = ObjectIdentity
nbx250 = _Nbx250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 3, 3, 1)
)
_Nbx500_ObjectIdentity = ObjectIdentity
nbx500 = _Nbx500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 3, 3, 2)
)
_Nbx750_ObjectIdentity = ObjectIdentity
nbx750 = _Nbx750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 3, 3, 3)
)
_OfficeConnectNbxCallProcessor_ObjectIdentity = ObjectIdentity
officeConnectNbxCallProcessor = _OfficeConnectNbxCallProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 3, 4)
)
_Nbxv3000_ObjectIdentity = ObjectIdentity
nbxv3000 = _Nbxv3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 17, 3, 5)
)
_IntranetAppliances_ObjectIdentity = ObjectIdentity
intranetAppliances = _IntranetAppliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18)
)
_FireWalls_ObjectIdentity = ObjectIdentity
fireWalls = _FireWalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 1)
)
_SuperStackFireWall_ObjectIdentity = ObjectIdentity
superStackFireWall = _SuperStackFireWall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 1, 1)
)
_SecureIX3100_10_ObjectIdentity = ObjectIdentity
secureIX3100_10 = _SecureIX3100_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 1, 2)
)
_SecureIX3100_50_ObjectIdentity = ObjectIdentity
secureIX3100_50 = _SecureIX3100_50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 1, 3)
)
_SecureIX3100_ObjectIdentity = ObjectIdentity
secureIX3100 = _SecureIX3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 1, 4)
)
_SecureIX4100_ObjectIdentity = ObjectIdentity
secureIX4100 = _SecureIX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 1, 5)
)
_SecureIX5100_ObjectIdentity = ObjectIdentity
secureIX5100 = _SecureIX5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 1, 6)
)
_Servers_ObjectIdentity = ObjectIdentity
servers = _Servers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 3)
)
_OfficeConnectStorageServer_ObjectIdentity = ObjectIdentity
officeConnectStorageServer = _OfficeConnectStorageServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 3, 1)
)
_OfficeConnectInternetServer_ObjectIdentity = ObjectIdentity
officeConnectInternetServer = _OfficeConnectInternetServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 3, 2)
)
_OfficeConnectEmailServer_ObjectIdentity = ObjectIdentity
officeConnectEmailServer = _OfficeConnectEmailServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 3, 3)
)
_StorageServer150_ObjectIdentity = ObjectIdentity
storageServer150 = _StorageServer150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 3, 4)
)
_Accelerators_ObjectIdentity = ObjectIdentity
accelerators = _Accelerators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 4)
)
_SslAccelerator_ObjectIdentity = ObjectIdentity
sslAccelerator = _SslAccelerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 18, 4, 1)
)
_XDSL_ObjectIdentity = ObjectIdentity
xDSL = _XDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19)
)
_SDSLGateway_ObjectIdentity = ObjectIdentity
sDSLGateway = _SDSLGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 1)
)
_VDSL_ObjectIdentity = ObjectIdentity
vDSL = _VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 2)
)
_VCNMultiAccessConcentrator_ObjectIdentity = ObjectIdentity
vCNMultiAccessConcentrator = _VCNMultiAccessConcentrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 2, 1)
)
_ADSLRouterVoDSLPorts_ObjectIdentity = ObjectIdentity
aDSLRouterVoDSLPorts = _ADSLRouterVoDSLPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 3)
)
_ADSLRouterNoVoDSLPorts_ObjectIdentity = ObjectIdentity
aDSLRouterNoVoDSLPorts = _ADSLRouterNoVoDSLPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 4)
)
_GSHDSLRouterVoDSLPorts_ObjectIdentity = ObjectIdentity
gSHDSLRouterVoDSLPorts = _GSHDSLRouterVoDSLPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 5)
)
_GSHDSLRouterNoVoDSLPorts_ObjectIdentity = ObjectIdentity
gSHDSLRouterNoVoDSLPorts = _GSHDSLRouterNoVoDSLPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 6)
)
_CableDSLGateway_ObjectIdentity = ObjectIdentity
cableDSLGateway = _CableDSLGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 7)
)
_CableDSLSecureGateway_ObjectIdentity = ObjectIdentity
cableDSLSecureGateway = _CableDSLSecureGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 8)
)
_CableWirelessDSLGateway_ObjectIdentity = ObjectIdentity
cableWirelessDSLGateway = _CableWirelessDSLGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 9)
)
_CableWireless54Mbps11gDSLGateway_ObjectIdentity = ObjectIdentity
cableWireless54Mbps11gDSLGateway = _CableWireless54Mbps11gDSLGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 10)
)
_XdslvpnFirewall_ObjectIdentity = ObjectIdentity
xdslvpnFirewall = _XdslvpnFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 11)
)
_XdslsecureRouter_ObjectIdentity = ObjectIdentity
xdslsecureRouter = _XdslsecureRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 12)
)
_Wireless11gAdslRouter_ObjectIdentity = ObjectIdentity
wireless11gAdslRouter = _Wireless11gAdslRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 19, 13)
)
_WirelessDevices_ObjectIdentity = ObjectIdentity
wirelessDevices = _WirelessDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20)
)
_WLanAP8000_ObjectIdentity = ObjectIdentity
wLanAP8000 = _WLanAP8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 1)
)
_WLanAP6000_ObjectIdentity = ObjectIdentity
wLanAP6000 = _WLanAP6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 2)
)
_WLanAP2000_ObjectIdentity = ObjectIdentity
wLanAP2000 = _WLanAP2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 3)
)
_WLanWrkgrpBridge_ObjectIdentity = ObjectIdentity
wLanWrkgrpBridge = _WLanWrkgrpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 4)
)
_WLantoLanBridge_ObjectIdentity = ObjectIdentity
wLantoLanBridge = _WLantoLanBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 5)
)
_WLanAP8500_ObjectIdentity = ObjectIdentity
wLanAP8500 = _WLanAP8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 6)
)
_WLanAPOfficeConnect11Mbps_ObjectIdentity = ObjectIdentity
wLanAPOfficeConnect11Mbps = _WLanAPOfficeConnect11Mbps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 7)
)
_WLanAP8200_ObjectIdentity = ObjectIdentity
wLanAP8200 = _WLanAP8200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 8)
)
_WLanAPOfficeConnect54Mbps11g_ObjectIdentity = ObjectIdentity
wLanAPOfficeConnect54Mbps11g = _WLanAPOfficeConnect54Mbps11g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 9)
)
_WlanAP8700_ObjectIdentity = ObjectIdentity
wlanAP8700 = _WlanAP8700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 10)
)
_WlanAP8250_ObjectIdentity = ObjectIdentity
wlanAP8250 = _WlanAP8250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 11)
)
_WlanAP8750_ObjectIdentity = ObjectIdentity
wlanAP8750 = _WlanAP8750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 12)
)
_WlanAP7250_ObjectIdentity = ObjectIdentity
wlanAP7250 = _WlanAP7250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 13)
)
_WlanWXR104_ObjectIdentity = ObjectIdentity
wlanWXR104 = _WlanWXR104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 14)
)
_WlanWX1206_ObjectIdentity = ObjectIdentity
wlanWX1206 = _WlanWX1206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 15)
)
_WlanWX4400_ObjectIdentity = ObjectIdentity
wlanWX4400 = _WlanWX4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 16)
)
_Wlan80211agWBridge_ObjectIdentity = ObjectIdentity
wlan80211agWBridge = _Wlan80211agWBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 17)
)
_Wlan11gOutdoorBtoBBridge_ObjectIdentity = ObjectIdentity
wlan11gOutdoorBtoBBridge = _Wlan11gOutdoorBtoBBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 18)
)
_Wlan11gIndoorBtoBBridge_ObjectIdentity = ObjectIdentity
wlan11gIndoorBtoBBridge = _Wlan11gIndoorBtoBBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 19)
)
_WlanAP11gPoE_ObjectIdentity = ObjectIdentity
wlanAP11gPoE = _WlanAP11gPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 20, 20)
)
_NetworkJacks_ObjectIdentity = ObjectIdentity
networkJacks = _NetworkJacks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 21)
)
_Nj200_ObjectIdentity = ObjectIdentity
nj200 = _Nj200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 21, 1)
)
_Nj205_ObjectIdentity = ObjectIdentity
nj205 = _Nj205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 21, 2)
)
_Nj220_ObjectIdentity = ObjectIdentity
nj220 = _Nj220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 21, 3)
)
_Nj225_ObjectIdentity = ObjectIdentity
nj225 = _Nj225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 21, 4)
)
_Nj225FXSC_ObjectIdentity = ObjectIdentity
nj225FXSC = _Nj225FXSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 21, 5)
)
_Nj225FXST_ObjectIdentity = ObjectIdentity
nj225FXST = _Nj225FXST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 21, 6)
)
_SecuritySwitches_ObjectIdentity = ObjectIdentity
securitySwitches = _SecuritySwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 22)
)
_SecuritySwitch6200_ObjectIdentity = ObjectIdentity
securitySwitch6200 = _SecuritySwitch6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 22, 1)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_Amp_mib_ObjectIdentity = ObjectIdentity
amp_mib = _Amp_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 3)
)
_GenericTrap_ObjectIdentity = ObjectIdentity
genericTrap = _GenericTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 4)
)
_ViewBuilderApps_ObjectIdentity = ObjectIdentity
viewBuilderApps = _ViewBuilderApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 5)
)
_SpecificTrap_ObjectIdentity = ObjectIdentity
specificTrap = _SpecificTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 6)
)
_LinkBuilder3GH_mib_ObjectIdentity = ObjectIdentity
linkBuilder3GH_mib = _LinkBuilder3GH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7)
)
_LinkBuilder10BTi_mib_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_mib = _LinkBuilder10BTi_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8)
)
_LinkBuilderECS_mib_ObjectIdentity = ObjectIdentity
linkBuilderECS_mib = _LinkBuilderECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_NetBuilder_mib_ObjectIdentity = ObjectIdentity
netBuilder_mib = _NetBuilder_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 11)
)
_LBridgeECS_mib_ObjectIdentity = ObjectIdentity
lBridgeECS_mib = _LBridgeECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 12)
)
_DeskMan_ObjectIdentity = ObjectIdentity
deskMan = _DeskMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 13)
)
_LinkBuilderMSH_mib_ObjectIdentity = ObjectIdentity
linkBuilderMSH_mib = _LinkBuilderMSH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 14)
)
_A3ComUnused15_ObjectIdentity = ObjectIdentity
a3ComUnused15 = _A3ComUnused15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 15)
)
_A3comFddiWGHubMib_ObjectIdentity = ObjectIdentity
a3comFddiWGHubMib = _A3comFddiWGHubMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 16)
)
_LinkSwitch_mib_ObjectIdentity = ObjectIdentity
linkSwitch_mib = _LinkSwitch_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 17)
)
_LinkSwitch1000_mib_ObjectIdentity = ObjectIdentity
linkSwitch1000_mib = _LinkSwitch1000_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 18)
)
_LinkBuilderFMS100_mib_ObjectIdentity = ObjectIdentity
linkBuilderFMS100_mib = _LinkBuilderFMS100_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 19)
)
_NcdMibs_ObjectIdentity = ObjectIdentity
ncdMibs = _NcdMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 20)
)
_OfficeConnect_Hub8M_mib_ObjectIdentity = ObjectIdentity
officeConnect_Hub8M_mib = _OfficeConnect_Hub8M_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 21)
)
_LinkSwitch2000TR_mib_ObjectIdentity = ObjectIdentity
linkSwitch2000TR_mib = _LinkSwitch2000TR_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 22)
)
_VlanServer_mib_ObjectIdentity = ObjectIdentity
vlanServer_mib = _VlanServer_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 23)
)
_TerminalServerMib_ObjectIdentity = ObjectIdentity
terminalServerMib = _TerminalServerMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 24)
)
_RpsIIMgmtModule_mib_ObjectIdentity = ObjectIdentity
rpsIIMgmtModule_mib = _RpsIIMgmtModule_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 25)
)
_TranscendEnterpriseMgr_ObjectIdentity = ObjectIdentity
transcendEnterpriseMgr = _TranscendEnterpriseMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 26)
)
_WatchModule_ObjectIdentity = ObjectIdentity
watchModule = _WatchModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 26, 1)
)
_SuperStackSwitch9000SX_mib_ObjectIdentity = ObjectIdentity
superStackSwitch9000SX_mib = _SuperStackSwitch9000SX_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 27)
)
_CoreBuilder9000_mib_ObjectIdentity = ObjectIdentity
coreBuilder9000_mib = _CoreBuilder9000_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 28)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_CableModem_mib_ObjectIdentity = ObjectIdentity
cableModem_mib = _CableModem_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 30)
)
_Edgemonitor_mib_ObjectIdentity = ObjectIdentity
edgemonitor_mib = _Edgemonitor_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 31)
)
_Nic_mib_ObjectIdentity = ObjectIdentity
nic_mib = _Nic_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 32)
)
_Palm_mib_ObjectIdentity = ObjectIdentity
palm_mib = _Palm_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 33)
)
_Grand_prix_mib_ObjectIdentity = ObjectIdentity
grand_prix_mib = _Grand_prix_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 34)
)
_Wlan_mib_ObjectIdentity = ObjectIdentity
wlan_mib = _Wlan_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35)
)
_IcdSipProxy_mib_ObjectIdentity = ObjectIdentity
icdSipProxy_mib = _IcdSipProxy_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 36)
)
_WebCache_mib_ObjectIdentity = ObjectIdentity
webCache_mib = _WebCache_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 37)
)
_XDSLCommon_mib_ObjectIdentity = ObjectIdentity
xDSLCommon_mib = _XDSLCommon_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 38)
)
_SuperStack4300_mib_ObjectIdentity = ObjectIdentity
superStack4300_mib = _SuperStack4300_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 39)
)
_Ldap3Com_ObjectIdentity = ObjectIdentity
ldap3Com = _Ldap3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 40)
)
_LdapGeneric_ObjectIdentity = ObjectIdentity
ldapGeneric = _LdapGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 40, 1)
)
_LdapCommWorks_ObjectIdentity = ObjectIdentity
ldapCommWorks = _LdapCommWorks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 40, 2)
)
_A3ComLdapVcx_ObjectIdentity = ObjectIdentity
a3ComLdapVcx = _A3ComLdapVcx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 40, 3)
)
_SslAcceleration_mib_ObjectIdentity = ObjectIdentity
sslAcceleration_mib = _SslAcceleration_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 41)
)
_NetworkManagement_mib_ObjectIdentity = ObjectIdentity
networkManagement_mib = _NetworkManagement_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 42)
)
_ComponentMgmtModule_mib_ObjectIdentity = ObjectIdentity
componentMgmtModule_mib = _ComponentMgmtModule_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 43)
)
_Firewall_mib_ObjectIdentity = ObjectIdentity
firewall_mib = _Firewall_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 44)
)
_Jv_mib_ObjectIdentity = ObjectIdentity
jv_mib = _Jv_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45)
)
_A3ComPoe_mib_ObjectIdentity = ObjectIdentity
a3ComPoe_mib = _A3ComPoe_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 46)
)
_A3Com496MIB_ObjectIdentity = ObjectIdentity
a3Com496MIB = _A3Com496MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 47)
)
_VoiceCoreExchange_mib_ObjectIdentity = ObjectIdentity
voiceCoreExchange_mib = _VoiceCoreExchange_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 48)
)
_A3ComEntityIdentifier_mib_ObjectIdentity = ObjectIdentity
a3ComEntityIdentifier_mib = _A3ComEntityIdentifier_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 49)
)
_A3ComTrpz_mib_ObjectIdentity = ObjectIdentity
a3ComTrpz_mib = _A3ComTrpz_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 50)
)
_A3ComNetworkJack_mib_ObjectIdentity = ObjectIdentity
a3ComNetworkJack_mib = _A3ComNetworkJack_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 51)
)
_Synernetics_ObjectIdentity = ObjectIdentity
synernetics = _Synernetics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114)
)
_Lanplex_ObjectIdentity = ObjectIdentity
lanplex = _Lanplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1)
)
_LANplex_12_slot_support_ObjectIdentity = ObjectIdentity
lANplex_12_slot_support = _LANplex_12_slot_support_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1)
)
_LANplex_4_slot_support_ObjectIdentity = ObjectIdentity
lANplex_4_slot_support = _LANplex_4_slot_support_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 2)
)
_LpsProducts_ObjectIdentity = ObjectIdentity
lpsProducts = _LpsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3)
)
_Lps6000_ObjectIdentity = ObjectIdentity
lps6000 = _Lps6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2)
)
_Lps6012_ObjectIdentity = ObjectIdentity
lps6012 = _Lps6012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1)
)
_Lps6012System_ObjectIdentity = ObjectIdentity
lps6012System = _Lps6012System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 1)
)
_Lanplex_6012_System_2_ObjectIdentity = ObjectIdentity
lanplex_6012_System_2 = _Lanplex_6012_System_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 1, 2)
)
_Lanplex_6012_System_3_ObjectIdentity = ObjectIdentity
lanplex_6012_System_3 = _Lanplex_6012_System_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 1, 3)
)
_Lanplex_6012_System_4_ObjectIdentity = ObjectIdentity
lanplex_6012_System_4 = _Lanplex_6012_System_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 1, 4)
)
_Lanplex_6012_System_5_ObjectIdentity = ObjectIdentity
lanplex_6012_System_5 = _Lanplex_6012_System_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 1, 5)
)
_Lanplex_6012_System_6_ObjectIdentity = ObjectIdentity
lanplex_6012_System_6 = _Lanplex_6012_System_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 1, 6)
)
_Lps6012Chassis_ObjectIdentity = ObjectIdentity
lps6012Chassis = _Lps6012Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 2)
)
_Lanplex_6012_Chassis_2_ObjectIdentity = ObjectIdentity
lanplex_6012_Chassis_2 = _Lanplex_6012_Chassis_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 2, 2)
)
_Lanplex_6012_Chassis_3_ObjectIdentity = ObjectIdentity
lanplex_6012_Chassis_3 = _Lanplex_6012_Chassis_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 2, 3)
)
_Lanplex_6012_Chassis_4_ObjectIdentity = ObjectIdentity
lanplex_6012_Chassis_4 = _Lanplex_6012_Chassis_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 2, 4)
)
_Lanplex_6012_Chassis_5_ObjectIdentity = ObjectIdentity
lanplex_6012_Chassis_5 = _Lanplex_6012_Chassis_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 2, 5)
)
_Lanplex_6012_Chassis_6_ObjectIdentity = ObjectIdentity
lanplex_6012_Chassis_6 = _Lanplex_6012_Chassis_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 2, 6)
)
_Lps6012ESM_ObjectIdentity = ObjectIdentity
lps6012ESM = _Lps6012ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 3)
)
_Lanplex_6012_ESM_2_ObjectIdentity = ObjectIdentity
lanplex_6012_ESM_2 = _Lanplex_6012_ESM_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 3, 2)
)
_Lanplex_6012_ESM_3_ObjectIdentity = ObjectIdentity
lanplex_6012_ESM_3 = _Lanplex_6012_ESM_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 3, 3)
)
_Lanplex_6012_ESM_4_ObjectIdentity = ObjectIdentity
lanplex_6012_ESM_4 = _Lanplex_6012_ESM_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 3, 4)
)
_Lanplex_6012_ESM_5_ObjectIdentity = ObjectIdentity
lanplex_6012_ESM_5 = _Lanplex_6012_ESM_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 3, 5)
)
_Lanplex_6012_ESM_6_ObjectIdentity = ObjectIdentity
lanplex_6012_ESM_6 = _Lanplex_6012_ESM_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 3, 6)
)
_Lps6012EFSM_ObjectIdentity = ObjectIdentity
lps6012EFSM = _Lps6012EFSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 4)
)
_Lanplex_6012_EFSM_2_ObjectIdentity = ObjectIdentity
lanplex_6012_EFSM_2 = _Lanplex_6012_EFSM_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 4, 2)
)
_Lanplex_6012_EFSM_3_ObjectIdentity = ObjectIdentity
lanplex_6012_EFSM_3 = _Lanplex_6012_EFSM_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 4, 3)
)
_Lanplex_6012_EFSM_4_ObjectIdentity = ObjectIdentity
lanplex_6012_EFSM_4 = _Lanplex_6012_EFSM_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 4, 4)
)
_Lanplex_6012_EFSM_5_ObjectIdentity = ObjectIdentity
lanplex_6012_EFSM_5 = _Lanplex_6012_EFSM_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 4, 5)
)
_Lanplex_6012_EFSM_6_ObjectIdentity = ObjectIdentity
lanplex_6012_EFSM_6 = _Lanplex_6012_EFSM_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 4, 6)
)
_Lps6012TRSM_ObjectIdentity = ObjectIdentity
lps6012TRSM = _Lps6012TRSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 5)
)
_Lanplex_6012_TRSM_5_ObjectIdentity = ObjectIdentity
lanplex_6012_TRSM_5 = _Lanplex_6012_TRSM_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 5, 5)
)
_Lanplex_6012_TRSM_6_ObjectIdentity = ObjectIdentity
lanplex_6012_TRSM_6 = _Lanplex_6012_TRSM_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 5, 6)
)
_Lps6012TMM_ObjectIdentity = ObjectIdentity
lps6012TMM = _Lps6012TMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 6)
)
_Lanplex_6012_TMM_6_ObjectIdentity = ObjectIdentity
lanplex_6012_TMM_6 = _Lanplex_6012_TMM_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 6, 6)
)
_Lps6012FSM_ObjectIdentity = ObjectIdentity
lps6012FSM = _Lps6012FSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 7)
)
_Lanplex_6012_FSM_7_ObjectIdentity = ObjectIdentity
lanplex_6012_FSM_7 = _Lanplex_6012_FSM_7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 7, 7)
)
_Lps6004_ObjectIdentity = ObjectIdentity
lps6004 = _Lps6004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2)
)
_Lps6004System_ObjectIdentity = ObjectIdentity
lps6004System = _Lps6004System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 1)
)
_Lanplex_6004_System_2_ObjectIdentity = ObjectIdentity
lanplex_6004_System_2 = _Lanplex_6004_System_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 1, 2)
)
_Lanplex_6004_System_3_ObjectIdentity = ObjectIdentity
lanplex_6004_System_3 = _Lanplex_6004_System_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 1, 3)
)
_Lanplex_6004_System_4_ObjectIdentity = ObjectIdentity
lanplex_6004_System_4 = _Lanplex_6004_System_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 1, 4)
)
_Lanplex_6004_System_5_ObjectIdentity = ObjectIdentity
lanplex_6004_System_5 = _Lanplex_6004_System_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 1, 5)
)
_Lanplex_6004_System_6_ObjectIdentity = ObjectIdentity
lanplex_6004_System_6 = _Lanplex_6004_System_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 1, 6)
)
_Lps6004Chassis_ObjectIdentity = ObjectIdentity
lps6004Chassis = _Lps6004Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 2)
)
_Lanplex_6004_Chassis_2_ObjectIdentity = ObjectIdentity
lanplex_6004_Chassis_2 = _Lanplex_6004_Chassis_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 2, 2)
)
_Lanplex_6004_Chassis_3_ObjectIdentity = ObjectIdentity
lanplex_6004_Chassis_3 = _Lanplex_6004_Chassis_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 2, 3)
)
_Lanplex_6004_Chassis_4_ObjectIdentity = ObjectIdentity
lanplex_6004_Chassis_4 = _Lanplex_6004_Chassis_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 2, 4)
)
_Lanplex_6004_Chassis_5_ObjectIdentity = ObjectIdentity
lanplex_6004_Chassis_5 = _Lanplex_6004_Chassis_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 2, 5)
)
_Lanplex_6004_Chassis_6_ObjectIdentity = ObjectIdentity
lanplex_6004_Chassis_6 = _Lanplex_6004_Chassis_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 2, 6)
)
_Lps6004ESM_ObjectIdentity = ObjectIdentity
lps6004ESM = _Lps6004ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 3)
)
_Lanplex_6004_ESM_2_ObjectIdentity = ObjectIdentity
lanplex_6004_ESM_2 = _Lanplex_6004_ESM_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 3, 2)
)
_Lanplex_6004_ESM_3_ObjectIdentity = ObjectIdentity
lanplex_6004_ESM_3 = _Lanplex_6004_ESM_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 3, 3)
)
_Lanplex_6004_ESM_4_ObjectIdentity = ObjectIdentity
lanplex_6004_ESM_4 = _Lanplex_6004_ESM_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 3, 4)
)
_Lanplex_6004_ESM_5_ObjectIdentity = ObjectIdentity
lanplex_6004_ESM_5 = _Lanplex_6004_ESM_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 3, 5)
)
_Lanplex_6004_ESM_6_ObjectIdentity = ObjectIdentity
lanplex_6004_ESM_6 = _Lanplex_6004_ESM_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 3, 6)
)
_Lps6004EFSM_ObjectIdentity = ObjectIdentity
lps6004EFSM = _Lps6004EFSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 4)
)
_Lanplex_6004_EFSM_2_ObjectIdentity = ObjectIdentity
lanplex_6004_EFSM_2 = _Lanplex_6004_EFSM_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 4, 2)
)
_Lanplex_6004_EFSM_3_ObjectIdentity = ObjectIdentity
lanplex_6004_EFSM_3 = _Lanplex_6004_EFSM_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 4, 3)
)
_Lanplex_6004_EFSM_4_ObjectIdentity = ObjectIdentity
lanplex_6004_EFSM_4 = _Lanplex_6004_EFSM_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 4, 4)
)
_Lanplex_6004_EFSM_5_ObjectIdentity = ObjectIdentity
lanplex_6004_EFSM_5 = _Lanplex_6004_EFSM_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 4, 5)
)
_Lanplex_6004_EFSM_6_ObjectIdentity = ObjectIdentity
lanplex_6004_EFSM_6 = _Lanplex_6004_EFSM_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 4, 6)
)
_Lps6004TRSM_ObjectIdentity = ObjectIdentity
lps6004TRSM = _Lps6004TRSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 5)
)
_Lanplex_6004_TRSM_5_ObjectIdentity = ObjectIdentity
lanplex_6004_TRSM_5 = _Lanplex_6004_TRSM_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 5, 5)
)
_Lanplex_6004_TRSM_6_ObjectIdentity = ObjectIdentity
lanplex_6004_TRSM_6 = _Lanplex_6004_TRSM_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 5, 6)
)
_Lps6004TMM_ObjectIdentity = ObjectIdentity
lps6004TMM = _Lps6004TMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 6)
)
_Lanplex_6004_TMM_6_ObjectIdentity = ObjectIdentity
lanplex_6004_TMM_6 = _Lanplex_6004_TMM_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 6, 6)
)
_Lps6004FSM_ObjectIdentity = ObjectIdentity
lps6004FSM = _Lps6004FSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 7)
)
_Lanplex_6004_FSM_7_ObjectIdentity = ObjectIdentity
lanplex_6004_FSM_7 = _Lanplex_6004_FSM_7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 7, 7)
)
_Lps2000_ObjectIdentity = ObjectIdentity
lps2000 = _Lps2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3)
)
_Lps2500_ObjectIdentity = ObjectIdentity
lps2500 = _Lps2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 1)
)
_Lanplex_2500_2_ObjectIdentity = ObjectIdentity
lanplex_2500_2 = _Lanplex_2500_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 1, 2)
)
_Lanplex_2500_3_ObjectIdentity = ObjectIdentity
lanplex_2500_3 = _Lanplex_2500_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 1, 3)
)
_Lanplex_2500_4_ObjectIdentity = ObjectIdentity
lanplex_2500_4 = _Lanplex_2500_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 1, 4)
)
_Lanplex_2500_5_ObjectIdentity = ObjectIdentity
lanplex_2500_5 = _Lanplex_2500_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 1, 5)
)
_Lanplex_2500_6_ObjectIdentity = ObjectIdentity
lanplex_2500_6 = _Lanplex_2500_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 1, 6)
)
_Lss2200_ObjectIdentity = ObjectIdentity
lss2200 = _Lss2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 2)
)
_LinkSwitch_2200_2_ObjectIdentity = ObjectIdentity
linkSwitch_2200_2 = _LinkSwitch_2200_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 2, 2)
)
_LinkSwitch_2200_3_ObjectIdentity = ObjectIdentity
linkSwitch_2200_3 = _LinkSwitch_2200_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 2, 3)
)
_LinkSwitch_2200_4_ObjectIdentity = ObjectIdentity
linkSwitch_2200_4 = _LinkSwitch_2200_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 2, 4)
)
_LinkSwitch_2200_5_ObjectIdentity = ObjectIdentity
linkSwitch_2200_5 = _LinkSwitch_2200_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 2, 5)
)
_LinkSwitch_2200_6_ObjectIdentity = ObjectIdentity
linkSwitch_2200_6 = _LinkSwitch_2200_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 2, 6)
)
_Lps2016_ObjectIdentity = ObjectIdentity
lps2016 = _Lps2016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 3)
)
_Lanplex_2016_2_ObjectIdentity = ObjectIdentity
lanplex_2016_2 = _Lanplex_2016_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 3, 2)
)
_Lanplex_2016_3_ObjectIdentity = ObjectIdentity
lanplex_2016_3 = _Lanplex_2016_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 3, 3)
)
_Lanplex_2016_4_ObjectIdentity = ObjectIdentity
lanplex_2016_4 = _Lanplex_2016_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 3, 4)
)
_Lanplex_2016_5_ObjectIdentity = ObjectIdentity
lanplex_2016_5 = _Lanplex_2016_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 3, 5)
)
_Lanplex_2016_6_ObjectIdentity = ObjectIdentity
lanplex_2016_6 = _Lanplex_2016_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 3, 6)
)
_Lss2200SS2_ObjectIdentity = ObjectIdentity
lss2200SS2 = _Lss2200SS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 4)
)
_LinkSwitch_2200_SS2_7_ObjectIdentity = ObjectIdentity
linkSwitch_2200_SS2_7 = _LinkSwitch_2200_SS2_7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 4, 7)
)
_LanplexSystemsMib_ObjectIdentity = ObjectIdentity
lanplexSystemsMib = _LanplexSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4)
)
_LanplexOptFddi_ObjectIdentity = ObjectIdentity
lanplexOptFddi = _LanplexOptFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 10)
)
_Bicc_ObjectIdentity = ObjectIdentity
bicc = _Bicc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170)
)
_Bdn_ObjectIdentity = ObjectIdentity
bdn = _Bdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1)
)
_BdnDevices_ObjectIdentity = ObjectIdentity
bdnDevices = _BdnDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1)
)
_Centrum_ObjectIdentity = ObjectIdentity
centrum = _Centrum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1)
)
_CentrumRemote_ObjectIdentity = ObjectIdentity
centrumRemote = _CentrumRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1)
)
_UsRobotics_ObjectIdentity = ObjectIdentity
usRobotics = _UsRobotics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_UsrSysOIDs_ObjectIdentity = ObjectIdentity
usrSysOIDs = _UsrSysOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2)
)
_NetServerII8_ObjectIdentity = ObjectIdentity
netServerII8 = _NetServerII8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 10)
)
_NetServerII16_ObjectIdentity = ObjectIdentity
netServerII16 = _NetServerII16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 11)
)
_LanLinkerBRI_ObjectIdentity = ObjectIdentity
lanLinkerBRI = _LanLinkerBRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 12)
)
_LanLinkerD56k_ObjectIdentity = ObjectIdentity
lanLinkerD56k = _LanLinkerD56k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 13)
)
_NetServerII8imdm_ObjectIdentity = ObjectIdentity
netServerII8imdm = _NetServerII8imdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 14)
)
_NetServerII16imdm_ObjectIdentity = ObjectIdentity
netServerII16imdm = _NetServerII16imdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 15)
)
_PilgrimCore_ObjectIdentity = ObjectIdentity
pilgrimCore = _PilgrimCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 16)
)
_Viper_ObjectIdentity = ObjectIdentity
viper = _Viper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 17)
)
_Alc_ObjectIdentity = ObjectIdentity
alc = _Alc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 18)
)
_Duala_ObjectIdentity = ObjectIdentity
duala = _Duala_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 2, 21)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3Com-products-MIB",
    **{"a3Com": a3Com,
       "products": products,
       "terminalServer": terminalServer,
       "cs2500": cs2500,
       "cs2500to": cs2500to,
       "cs2500tlo": cs2500tlo,
       "cs2600": cs2600,
       "cs2600to": cs2600to,
       "cs2600tlo": cs2600tlo,
       "cs2000": cs2000,
       "cs2000to": cs2000to,
       "cs2000tlo": cs2000tlo,
       "cs1": cs1,
       "cs210": cs210,
       "cs2100": cs2100,
       "cs2100to": cs2100to,
       "cs2100tlo": cs2100tlo,
       "cs3000": cs3000,
       "cs3000to": cs3000to,
       "cs3000tlo": cs3000tlo,
       "cs3100": cs3100,
       "cs3100to": cs3100to,
       "cs3100tlo": cs3100tlo,
       "callisto": callisto,
       "termServerPlatform": termServerPlatform,
       "series1": series1,
       "series200": series200,
       "callistoPlatfor": callistoPlatfor,
       "series2500": series2500,
       "series3000": series3000,
       "dedicatedBridgeServer": dedicatedBridgeServer,
       "dedicatedRouteServer": dedicatedRouteServer,
       "brouter": brouter,
       "netbuilder1": netbuilder1,
       "netbuilder2": netbuilder2,
       "lBridgeECS": lBridgeECS,
       "netbuilderTrRA": netbuilderTrRA,
       "netbuilderTrRAbp": netbuilderTrRAbp,
       "netbuilderTrRAcp": netbuilderTrRAcp,
       "netbuilderTrRAxw": netbuilderTrRAxw,
       "netbuilderTrRAcx": netbuilderTrRAcx,
       "netbuilderTrRAba": netbuilderTrRAba,
       "netbuilderTrRAar": netbuilderTrRAar,
       "netbuilderTrRAsn": netbuilderTrRAsn,
       "netbuilderTrRArb": netbuilderTrRArb,
       "netbuilderTrRAff": netbuilderTrRAff,
       "netbuidlerTrRAcf": netbuidlerTrRAcf,
       "netbuilderTrRAbx": netbuilderTrRAbx,
       "netbuilderTrRAappn": netbuilderTrRAappn,
       "netbuilderTrRAlm": netbuilderTrRAlm,
       "netbuilderTrRAlt": netbuilderTrRAlt,
       "netbuilderTrRAwm": netbuilderTrRAwm,
       "netbuilderTrRAwt": netbuilderTrRAwt,
       "netbuilderTrRAae": netbuilderTrRAae,
       "netbuilderTrRAap": netbuilderTrRAap,
       "netbuilderTrRAan": netbuilderTrRAan,
       "netbuilderTrRAla": netbuilderTrRAla,
       "netbuilderTrRAwa": netbuilderTrRAwa,
       "netbuilderTrRAaa": netbuilderTrRAaa,
       "netbuilderTrRAab": netbuilderTrRAab,
       "netbuilderTrRAbf": netbuilderTrRAbf,
       "brouterPlatform": brouterPlatform,
       "nb1": nb1,
       "nb2": nb2,
       "nbroPlatform": nbroPlatform,
       "casperPlatform": casperPlatform,
       "spectreIsdnPform": spectreIsdnPform,
       "spectreIITr": spectreIITr,
       "nbroIITrIsdnPform": nbroIITrIsdnPform,
       "nbroIIEthPform": nbroIIEthPform,
       "nbroIIEthIsdnPform": nbroIIEthIsdnPform,
       "ocGen": ocGen,
       "ocIsdnSt": ocIsdnSt,
       "ocIsdnU": ocIsdnU,
       "ocCsuDsu": ocCsuDsu,
       "ocWanOnly": ocWanOnly,
       "ocT1CsuDsu": ocT1CsuDsu,
       "intrepidGen": intrepidGen,
       "intrepidIsdnSt": intrepidIsdnSt,
       "intrepidIsdnU": intrepidIsdnU,
       "intrepid56kCsuDsu": intrepid56kCsuDsu,
       "intrepidT1CsuDsu": intrepidT1CsuDsu,
       "oc1x2": oc1x2,
       "scorePform": scorePform,
       "blueridgeGen": blueridgeGen,
       "blueridgeIsdnSt": blueridgeIsdnSt,
       "blueridgeIsdnU": blueridgeIsdnU,
       "blueridge56kCsuDsu": blueridge56kCsuDsu,
       "blueridgeT1CsuCsu": blueridgeT1CsuCsu,
       "scoreLanToLan": scoreLanToLan,
       "scoreFlex": scoreFlex,
       "scoreFlexPri": scoreFlexPri,
       "scoreDualT3": scoreDualT3,
       "scoreDualE3": scoreDualE3,
       "scoreDualPri": scoreDualPri,
       "copperHead": copperHead,
       "scoreMMATM": scoreMMATM,
       "scoreSMATM": scoreSMATM,
       "scoreFlexPri2port": scoreFlexPri2port,
       "oc10St": oc10St,
       "oc10U": oc10U,
       "scorePri4port": scorePri4port,
       "easterST": easterST,
       "easterU": easterU,
       "netbuilderRem": netbuilderRem,
       "netbuilderRemBp": netbuilderRemBp,
       "netbuilderRemCp": netbuilderRemCp,
       "netbuilderRemXw": netbuilderRemXw,
       "netbuilderRemCx": netbuilderRemCx,
       "netbuilderRemBa": netbuilderRemBa,
       "netbuilderRemAr": netbuilderRemAr,
       "netbuilderRemSn": netbuilderRemSn,
       "netbuilderRemRb": netbuilderRemRb,
       "netbuilderRemFf": netbuilderRemFf,
       "netbuilderRemCf": netbuilderRemCf,
       "netbuilderRemBx": netbuilderRemBx,
       "netbuilderRemAppn": netbuilderRemAppn,
       "netbuilderRemLm": netbuilderRemLm,
       "netbuilderRemLt": netbuilderRemLt,
       "netbuilderRemWm": netbuilderRemWm,
       "netbuilderRemWt": netbuilderRemWt,
       "netbuilderRemAe": netbuilderRemAe,
       "netbuilderRemAp": netbuilderRemAp,
       "netbuilderRemAn": netbuilderRemAn,
       "netbuilderRemLa": netbuilderRemLa,
       "netbuilderRemWa": netbuilderRemWa,
       "netbuilderRemAa": netbuilderRemAa,
       "netbuilderRemAb": netbuilderRemAb,
       "netbuilderRemBf": netbuilderRemBf,
       "netbuilderRA": netbuilderRA,
       "netbuilderRAbp": netbuilderRAbp,
       "netbuilderRAcp": netbuilderRAcp,
       "netbuilderRAxw": netbuilderRAxw,
       "netbuilderRAcx": netbuilderRAcx,
       "netbuilderRAba": netbuilderRAba,
       "netbuilderRAar": netbuilderRAar,
       "netbuilderRAsn": netbuilderRAsn,
       "netbuilderRArb": netbuilderRArb,
       "netbuilderRAff": netbuilderRAff,
       "netbuilderRAcf": netbuilderRAcf,
       "netbuilderRAbx": netbuilderRAbx,
       "netbuilderRAappn": netbuilderRAappn,
       "netbuilderRAlm": netbuilderRAlm,
       "netbuilderRAlt": netbuilderRAlt,
       "netbuilderRAwm": netbuilderRAwm,
       "netbuilderRAwt": netbuilderRAwt,
       "netbuilderRAae": netbuilderRAae,
       "netbuilderRAap": netbuilderRAap,
       "netbuilderRAan": netbuilderRAan,
       "netbuilderRAla": netbuilderRAla,
       "netbuilderRAwa": netbuilderRAwa,
       "netbuilderRAaa": netbuilderRAaa,
       "netbuilderRAab": netbuilderRAab,
       "netbuilderRAbf": netbuilderRAbf,
       "netbuilderRC": netbuilderRC,
       "netbuilderRCbp": netbuilderRCbp,
       "netbuilderRCcp": netbuilderRCcp,
       "netbuilderRCxw": netbuilderRCxw,
       "netbuilderRCcx": netbuilderRCcx,
       "netbuilderRCba": netbuilderRCba,
       "netbuilderRCar": netbuilderRCar,
       "netbuilderRCsn": netbuilderRCsn,
       "netbuilderRCrb": netbuilderRCrb,
       "netbuilderRCff": netbuilderRCff,
       "netbuilderRCcf": netbuilderRCcf,
       "netbuilderRCbx": netbuilderRCbx,
       "netbuilderRCappn": netbuilderRCappn,
       "netbuilderRClm": netbuilderRClm,
       "netbuilderRClt": netbuilderRClt,
       "netbuilderRCwm": netbuilderRCwm,
       "netbuilderRCwt": netbuilderRCwt,
       "netbuilderRCae": netbuilderRCae,
       "netbuilderRCap": netbuilderRCap,
       "netbuilderRCan": netbuilderRCan,
       "netbuilderRCla": netbuilderRCla,
       "netbuilderRCwa": netbuilderRCwa,
       "netbuilderRCaa": netbuilderRCaa,
       "netbuilderRCab": netbuilderRCab,
       "netbuilderRCbf": netbuilderRCbf,
       "netbuilderTrRem": netbuilderTrRem,
       "netbuilderTrRemBp": netbuilderTrRemBp,
       "netbuilderTrRemCp": netbuilderTrRemCp,
       "netbuilderTrRemXw": netbuilderTrRemXw,
       "netbuilderTrRemCx": netbuilderTrRemCx,
       "netbuilderTrRemBa": netbuilderTrRemBa,
       "netbuilderTrRemAr": netbuilderTrRemAr,
       "netbuilderTrRemSn": netbuilderTrRemSn,
       "netbuilderTrRemRb": netbuilderTrRemRb,
       "netbuilderTrRemFf": netbuilderTrRemFf,
       "netbuilderTrRemCf": netbuilderTrRemCf,
       "netbuilderTrRemBx": netbuilderTrRemBx,
       "netbuilderTrRemAppn": netbuilderTrRemAppn,
       "netbuilderTrRemLm": netbuilderTrRemLm,
       "netbuilderTrRemLt": netbuilderTrRemLt,
       "netbuilderTrRemWm": netbuilderTrRemWm,
       "netbuilderTrRemWt": netbuilderTrRemWt,
       "netbuilderTrRemAe": netbuilderTrRemAe,
       "netbuilderTrRemAp": netbuilderTrRemAp,
       "netbuilderTrRemAn": netbuilderTrRemAn,
       "netbuilderTrRemLa": netbuilderTrRemLa,
       "netbuilderTrRemWa": netbuilderTrRemWa,
       "netbuilderTrRemAa": netbuilderTrRemAa,
       "netbuilderTrRemAb": netbuilderTrRemAb,
       "netbuilderTrRemBf": netbuilderTrRemBf,
       "netbuilderTrRC": netbuilderTrRC,
       "netbuilderTrRCbp": netbuilderTrRCbp,
       "netbuilderTrRCcp": netbuilderTrRCcp,
       "netbuilderTrRCxw": netbuilderTrRCxw,
       "netbuilderTrRCcx": netbuilderTrRCcx,
       "netbuilderTrRCba": netbuilderTrRCba,
       "netbuilderTrRCar": netbuilderTrRCar,
       "netbuilderTrRCsn": netbuilderTrRCsn,
       "netbuilderTrRCrb": netbuilderTrRCrb,
       "netbuilderTrRCff": netbuilderTrRCff,
       "netbuilderTrRCcf": netbuilderTrRCcf,
       "netbuilderTrRCbx": netbuilderTrRCbx,
       "netbuilderTrRCappn": netbuilderTrRCappn,
       "netbuilderTrRClm": netbuilderTrRClm,
       "netbuilderTrRClt": netbuilderTrRClt,
       "netbuilderTrRCwm": netbuilderTrRCwm,
       "netbuilderTrRCwt": netbuilderTrRCwt,
       "netbuilderTrRCae": netbuilderTrRCae,
       "netbuilderTrRCap": netbuilderTrRCap,
       "netbuilderTrRCan": netbuilderTrRCan,
       "netbuilderTrRCla": netbuilderTrRCla,
       "netbuilderTrRCwa": netbuilderTrRCwa,
       "netbuilderTrRCaa": netbuilderTrRCaa,
       "netbuilderTrRCab": netbuilderTrRCab,
       "netbuilderTrRCbf": netbuilderTrRCbf,
       "nb2-4": nb2_4,
       "nb2-4Bp": nb2_4Bp,
       "nb2-4Cp": nb2_4Cp,
       "nb2-4Xw": nb2_4Xw,
       "nb2-4Cx": nb2_4Cx,
       "nb2-4Ba": nb2_4Ba,
       "nb2-4Ar": nb2_4Ar,
       "nb2-4Sn": nb2_4Sn,
       "nb2-4Rb": nb2_4Rb,
       "nb2-4Ff": nb2_4Ff,
       "nb2-4Cf": nb2_4Cf,
       "nb2-4Bx": nb2_4Bx,
       "nb2-4Appn": nb2_4Appn,
       "nb2-4Lm": nb2_4Lm,
       "nb2-4Lt": nb2_4Lt,
       "nb2-4Wm": nb2_4Wm,
       "nb2-4Wt": nb2_4Wt,
       "nb2-4Ae": nb2_4Ae,
       "nb2-4Ap": nb2_4Ap,
       "nb2-4An": nb2_4An,
       "nb2-4La": nb2_4La,
       "nb2-4Wa": nb2_4Wa,
       "nb2-4Aa": nb2_4Aa,
       "nb2-4Ab": nb2_4Ab,
       "nb2-4Bf": nb2_4Bf,
       "nb2-8": nb2_8,
       "nb2-8Bp": nb2_8Bp,
       "nb2-8Cp": nb2_8Cp,
       "nb2-8Xw": nb2_8Xw,
       "nb2-8Cx": nb2_8Cx,
       "nb2-8Ba": nb2_8Ba,
       "nb2-8Ar": nb2_8Ar,
       "nb2-8Sn": nb2_8Sn,
       "nb2-8Rb": nb2_8Rb,
       "nb2-8Ff": nb2_8Ff,
       "nb2-8Cf": nb2_8Cf,
       "nb2-8Bx": nb2_8Bx,
       "nb2-8Appn": nb2_8Appn,
       "nb2-8Lm": nb2_8Lm,
       "nb2-8Lt": nb2_8Lt,
       "nb2-8Wm": nb2_8Wm,
       "nb2-8Wt": nb2_8Wt,
       "nb2-8Ae": nb2_8Ae,
       "nb2-8Ap": nb2_8Ap,
       "nb2-8An": nb2_8An,
       "nb2-8La": nb2_8La,
       "nb2-8Wa": nb2_8Wa,
       "nb2-8Aa": nb2_8Aa,
       "nb2-8Ab": nb2_8Ab,
       "nb2-8Bf": nb2_8Bf,
       "nbro": nbro,
       "nbroBp": nbroBp,
       "nbroCp": nbroCp,
       "nbroXw": nbroXw,
       "nbroCx": nbroCx,
       "nbro201": nbro201,
       "nbroAr": nbroAr,
       "nbroSn": nbroSn,
       "nbro200": nbro200,
       "nbroFf": nbroFf,
       "nbroCf": nbroCf,
       "nbroBx": nbroBx,
       "nbroAppn": nbroAppn,
       "nbroLm": nbroLm,
       "nbroLt": nbroLt,
       "nbroWm": nbroWm,
       "nbroWt": nbroWt,
       "nbroAe": nbroAe,
       "nbroAp": nbroAp,
       "nbroAn": nbroAn,
       "nbroLa": nbroLa,
       "nbroWa": nbroWa,
       "nbro224": nbro224,
       "nbroAb": nbroAb,
       "nbro223": nbro223,
       "brouterBoards": brouterBoards,
       "ethernet": ethernet,
       "fddiPhy": fddiPhy,
       "fddiMac": fddiMac,
       "hss": hss,
       "tokenRingBrd": tokenRingBrd,
       "hssG703": hssG703,
       "hssRS449": hssRS449,
       "t3HSSI": t3HSSI,
       "dualEth": dualEth,
       "cec": cec,
       "fddiPhySm": fddiPhySm,
       "fddiPhyMmSm": fddiPhyMmSm,
       "fddiPhySmMm": fddiPhySmMm,
       "hdwan": hdwan,
       "hdwan449": hdwan449,
       "hdwan232": hdwan232,
       "mp6Eth": mp6Eth,
       "trPlus": trPlus,
       "macPlus": macPlus,
       "cecStar": cecStar,
       "isdnBri": isdnBri,
       "isdnPri": isdnPri,
       "mpAtm": mpAtm,
       "hssI431": hssI431,
       "mpFddi": mpFddi,
       "mp6EthFl": mp6EthFl,
       "ethV3": ethV3,
       "ethV3Fl": ethV3Fl,
       "nbroBrd": nbroBrd,
       "mpAtmFiber": mpAtmFiber,
       "dpe": dpe,
       "flatFddiMm": flatFddiMm,
       "flatFddiSs": flatFddiSs,
       "flatFddiSm": flatFddiSm,
       "flatFddiMs": flatFddiMs,
       "mpAtmFiberMm": mpAtmFiberMm,
       "nbocBrd": nbocBrd,
       "nbocST": nbocST,
       "nbocU": nbocU,
       "nboc56kCSU": nboc56kCSU,
       "nbocT1CSU": nbocT1CSU,
       "nboc1x1": nboc1x1,
       "nboc2FlexWAN": nboc2FlexWAN,
       "intrepidBrd": intrepidBrd,
       "intrepidST": intrepidST,
       "intrepidU": intrepidU,
       "intrepid56kCSU": intrepid56kCSU,
       "intrepidT1CSU": intrepidT1CSU,
       "mbriSt": mbriSt,
       "mbriU": mbriU,
       "qWan": qWan,
       "dpePlus": dpePlus,
       "nboc1x2": nboc1x2,
       "scoreCpu": scoreCpu,
       "scoreT1": scoreT1,
       "scoreT3": scoreT3,
       "scorePRI": scorePRI,
       "blueridgeBrd": blueridgeBrd,
       "blueridgeST": blueridgeST,
       "blueridgeU": blueridgeU,
       "blueridge56kCSU": blueridge56kCSU,
       "blueridgeT1CSU": blueridgeT1CSU,
       "scoreE3": scoreE3,
       "scoreLAN": scoreLAN,
       "copperCPU": copperCPU,
       "voiceFXS": voiceFXS,
       "voiceFXO": voiceFXO,
       "voiceEaM": voiceEaM,
       "copperST": copperST,
       "copperU": copperU,
       "copper56kCSU": copper56kCSU,
       "copperT1CSU": copperT1CSU,
       "scoreATMMm": scoreATMMm,
       "scoreATMSm": scoreATMSm,
       "scoreT1x2": scoreT1x2,
       "scorePRIx2": scorePRIx2,
       "copperPRI": copperPRI,
       "copperBRIx4": copperBRIx4,
       "copperModem": copperModem,
       "copperT1x1": copperT1x1,
       "netbuilderLocal": netbuilderLocal,
       "netbuilderLocalBp": netbuilderLocalBp,
       "netbuilderLocalCp": netbuilderLocalCp,
       "netbuilderLocalXw": netbuilderLocalXw,
       "netbuilderLocalCx": netbuilderLocalCx,
       "netbuilderLocalBa": netbuilderLocalBa,
       "netbuilderLocalAr": netbuilderLocalAr,
       "netbuilderLocalSn": netbuilderLocalSn,
       "netbuilderLocalRb": netbuilderLocalRb,
       "netbuilderLocalFf": netbuilderLocalFf,
       "netbuilderLocalCf": netbuilderLocalCf,
       "netbuilderLocalBx": netbuilderLocalBx,
       "netbuilderLocalAppn": netbuilderLocalAppn,
       "netbuilderLocalLm": netbuilderLocalLm,
       "netbuilderLocalLt": netbuilderLocalLt,
       "netbuilderLocalWm": netbuilderLocalWm,
       "netbuilderLocalWt": netbuilderLocalWt,
       "netbuilderLocalAe": netbuilderLocalAe,
       "netbuilderLocalAp": netbuilderLocalAp,
       "netbuilderLocalAn": netbuilderLocalAn,
       "netbuilderLocalLa": netbuilderLocalLa,
       "netbuilderLocalWa": netbuilderLocalWa,
       "netbuilderLocalAa": netbuilderLocalAa,
       "netbuilderLocalAb": netbuilderLocalAb,
       "netbuilderLocalBf": netbuilderLocalBf,
       "netbuilderTrLocal": netbuilderTrLocal,
       "netbuilderTrLocalBp": netbuilderTrLocalBp,
       "netbuilderTrLocalCp": netbuilderTrLocalCp,
       "netbuilderTrLocalXw": netbuilderTrLocalXw,
       "netbuilderTrLocalCx": netbuilderTrLocalCx,
       "netbuilderTrLocalBa": netbuilderTrLocalBa,
       "netbuilderTrLocalAr": netbuilderTrLocalAr,
       "netbuilderTrLocalSn": netbuilderTrLocalSn,
       "netbuilderTrLocalRb": netbuilderTrLocalRb,
       "netbuilderTrLocalFf": netbuilderTrLocalFf,
       "netbuilderTrLocalCf": netbuilderTrLocalCf,
       "netbuilderTrLocalBx": netbuilderTrLocalBx,
       "netbuilderTrLocalAppn": netbuilderTrLocalAppn,
       "netbuilderTrLocalLm": netbuilderTrLocalLm,
       "netbuilderTrLocalLt": netbuilderTrLocalLt,
       "netbuilderTrLocalWm": netbuilderTrLocalWm,
       "netbuilderTrLocalWt": netbuilderTrLocalWt,
       "netbuilderTrLocalAe": netbuilderTrLocalAe,
       "netbuilderTrLocalAp": netbuilderTrLocalAp,
       "netbuilderTrLocalAn": netbuilderTrLocalAn,
       "netbuilderTrLocalLa": netbuilderTrLocalLa,
       "netbuilderTrLocalWa": netbuilderTrLocalWa,
       "netbuilderTrLocalAa": netbuilderTrLocalAa,
       "netbuilderTrLocalAb": netbuilderTrLocalAb,
       "netbuilderTrLocalBf": netbuilderTrLocalBf,
       "netbuilderRC1x2": netbuilderRC1x2,
       "netbuilderRC1x2bp": netbuilderRC1x2bp,
       "netbuilderRC1x2cp": netbuilderRC1x2cp,
       "netbuilderRC1x2xw": netbuilderRC1x2xw,
       "netbuilderRC1x2cx": netbuilderRC1x2cx,
       "netbuilderRC1x2ba": netbuilderRC1x2ba,
       "netbuilderRC1x2ar": netbuilderRC1x2ar,
       "netbuilderRC1x2sn": netbuilderRC1x2sn,
       "netbuilderRC1x2rb": netbuilderRC1x2rb,
       "netbuilderRC1x2ff": netbuilderRC1x2ff,
       "netbuilderRC1x2cf": netbuilderRC1x2cf,
       "netbuilderRC1x2bx": netbuilderRC1x2bx,
       "netbuilderRC1x2appn": netbuilderRC1x2appn,
       "netbuilderRC1x2lm": netbuilderRC1x2lm,
       "netbuilderRC1x2lt": netbuilderRC1x2lt,
       "netbuilderRC1x2wm": netbuilderRC1x2wm,
       "netbuilderRC1x2wt": netbuilderRC1x2wt,
       "netbuilderRC1x2ae": netbuilderRC1x2ae,
       "netbuilderRC1x2ap": netbuilderRC1x2ap,
       "netbuilderRC1x2an": netbuilderRC1x2an,
       "netbuilderRC1x2la": netbuilderRC1x2la,
       "netbuilderRC1x2wa": netbuilderRC1x2wa,
       "netbuilderRC1x2aa": netbuilderRC1x2aa,
       "netbuilderRC1x2ab": netbuilderRC1x2ab,
       "netbuilderRC1x2bf": netbuilderRC1x2bf,
       "netbuilderTrRC1x2": netbuilderTrRC1x2,
       "netbuilderTrRC1x2bp": netbuilderTrRC1x2bp,
       "netbuilderTrRC1x2cp": netbuilderTrRC1x2cp,
       "netbuilderTrRC1x2xw": netbuilderTrRC1x2xw,
       "netbuilderTrRC1x2cx": netbuilderTrRC1x2cx,
       "netbuilderTrRC1x2ba": netbuilderTrRC1x2ba,
       "netbuilderTrRC1x2ar": netbuilderTrRC1x2ar,
       "netbuilderTrRC1x2sn": netbuilderTrRC1x2sn,
       "netbuilderTrRC1x2rb": netbuilderTrRC1x2rb,
       "netbuilderTrRC1x2ff": netbuilderTrRC1x2ff,
       "netbuilderTrRC1x2cf": netbuilderTrRC1x2cf,
       "netbuilderTrRC1x2bx": netbuilderTrRC1x2bx,
       "netbuilderTrRC1x2appn": netbuilderTrRC1x2appn,
       "netbuilderTrRC1x2lm": netbuilderTrRC1x2lm,
       "netbuilderTrRC1x2lt": netbuilderTrRC1x2lt,
       "netbuilderTrRC1x2wm": netbuilderTrRC1x2wm,
       "netbuilderTrRC1x2wt": netbuilderTrRC1x2wt,
       "netbuilderTrRC1x2ae": netbuilderTrRC1x2ae,
       "netbuilderTrRC1x2ap": netbuilderTrRC1x2ap,
       "netbuilderTrRC1x2an": netbuilderTrRC1x2an,
       "netbuilderTrRC1x2la": netbuilderTrRC1x2la,
       "netbuilderTrRC1x2wa": netbuilderTrRC1x2wa,
       "netbuilderTrRC1x2aa": netbuilderTrRC1x2aa,
       "netbuilderTrRC1x2ab": netbuilderTrRC1x2ab,
       "netbuilderTrRC1x2bf": netbuilderTrRC1x2bf,
       "casper": casper,
       "nbrolBp": nbrolBp,
       "nbrolCp": nbrolCp,
       "nbrolXw": nbrolXw,
       "nbrol228": nbrol228,
       "nbrol201": nbrol201,
       "nbro222": nbro222,
       "nbrolSn": nbrolSn,
       "nbrol200": nbrol200,
       "nbrolFf": nbrolFf,
       "nbro227": nbro227,
       "nbro221": nbro221,
       "nbrolAppn": nbrolAppn,
       "nbrolLm": nbrolLm,
       "nbrolLt": nbrolLt,
       "nbrolWm": nbrolWm,
       "nbrolWt": nbrolWt,
       "nbrolAe": nbrolAe,
       "nbrolAp": nbrolAp,
       "nbrolAn": nbrolAn,
       "nbrolLa": nbrolLa,
       "nbrolWa": nbrolWa,
       "nbrol224": nbrol224,
       "nbrolAb": nbrolAb,
       "nbrol223": nbrol223,
       "spectreHuge": spectreHuge,
       "nbrohBp": nbrohBp,
       "nbrohCp": nbrohCp,
       "nbrohXw": nbrohXw,
       "nbro228": nbro228,
       "nbroh201": nbroh201,
       "nbroh222": nbroh222,
       "nbrohSn": nbrohSn,
       "nbroh200": nbroh200,
       "nbrohFf": nbrohFf,
       "nbroh227": nbroh227,
       "nbroh221": nbroh221,
       "nbrohAppn": nbrohAppn,
       "nbrohLm": nbrohLm,
       "nbrohLt": nbrohLt,
       "nbrohWm": nbrohWm,
       "nbrohWt": nbrohWt,
       "nbrohAe": nbrohAe,
       "nbrohAp": nbrohAp,
       "nbrohAn": nbrohAn,
       "nbrohLa": nbrohLa,
       "nbrohWa": nbrohWa,
       "nbroh224": nbroh224,
       "nbrohAb": nbrohAb,
       "nbroh223": nbroh223,
       "spectreIsdn": spectreIsdn,
       "nbroiBp": nbroiBp,
       "nbroiCp": nbroiCp,
       "nbroiXw": nbroiXw,
       "nbroiCX": nbroiCX,
       "nbroiBA": nbroiBA,
       "nbro422": nbro422,
       "nbroiSn": nbroiSn,
       "nbroi200": nbroi200,
       "nbroiFf": nbroiFf,
       "nbroil427": nbroil427,
       "nbro421": nbro421,
       "nbroiAppn": nbroiAppn,
       "nbroiLm": nbroiLm,
       "nbroiLt": nbroiLt,
       "nbroiWm": nbroiWm,
       "nbroiWt": nbroiWt,
       "nbroiAe": nbroiAe,
       "nbroiAp": nbroiAp,
       "nbroiAn": nbroiAn,
       "nbroiLa": nbroiLa,
       "nbroiWa": nbroiWa,
       "nbroi424": nbroi424,
       "nbroiAb": nbroiAb,
       "nbroi423": nbroi423,
       "nb2-8-4fddi": nb2_8_4fddi,
       "nb2-8-4fddiBp": nb2_8_4fddiBp,
       "nb2-8-4fddiCp": nb2_8_4fddiCp,
       "nb2-8-4fddiXw": nb2_8_4fddiXw,
       "nb2-8-4fddiCx": nb2_8_4fddiCx,
       "nb2-8-4fddiBa": nb2_8_4fddiBa,
       "nb2-8-4fddiAr": nb2_8_4fddiAr,
       "nb2-8-4fddiSn": nb2_8_4fddiSn,
       "nb2-8-4fddiRb": nb2_8_4fddiRb,
       "nb2-8-4fddiFf": nb2_8_4fddiFf,
       "nb2-8-4fddiCf": nb2_8_4fddiCf,
       "nb2-8-4fddiBx": nb2_8_4fddiBx,
       "nb2-8-4fddiAppn": nb2_8_4fddiAppn,
       "nb2-8-4fddiLm": nb2_8_4fddiLm,
       "nb2-8-4fddiLt": nb2_8_4fddiLt,
       "nb2-8-4fddiWm": nb2_8_4fddiWm,
       "nb2-8-4fddiWt": nb2_8_4fddiWt,
       "nb2-8-4fddiAe": nb2_8_4fddiAe,
       "nb2-8-4fddiAp": nb2_8_4fddiAp,
       "nb2-8-4fddiAn": nb2_8_4fddiAn,
       "nb2-8-4fddiLa": nb2_8_4fddiLa,
       "nb2-8-4fddiWa": nb2_8_4fddiWa,
       "nb2-8-4fddiAa": nb2_8_4fddiAa,
       "nb2-8-4fddiAb": nb2_8_4fddiAb,
       "nb2-8-4fddiBf": nb2_8_4fddiBf,
       "nb2-8-dualwide": nb2_8_dualwide,
       "nb2-8-dualwideBp": nb2_8_dualwideBp,
       "nb2-8-dualwideCp": nb2_8_dualwideCp,
       "nb2-8-dualwideXw": nb2_8_dualwideXw,
       "nb2-8-dualwideCx": nb2_8_dualwideCx,
       "nb2-8-dualwideBa": nb2_8_dualwideBa,
       "nb2-8-dualwideAr": nb2_8_dualwideAr,
       "nb2-8-dualwideSn": nb2_8_dualwideSn,
       "nb2-8-dualwideRb": nb2_8_dualwideRb,
       "nb2-8-dualwideFf": nb2_8_dualwideFf,
       "nb2-8-dualwideCf": nb2_8_dualwideCf,
       "nb2-8-dualwideBx": nb2_8_dualwideBx,
       "nb2-8-dualwideAppn": nb2_8_dualwideAppn,
       "nb2-8-dualwideLm": nb2_8_dualwideLm,
       "nb2-8-dualwideLt": nb2_8_dualwideLt,
       "nb2-8-dualwideWm": nb2_8_dualwideWm,
       "nb2-8-dualwideWt": nb2_8_dualwideWt,
       "nb2-8-dualwideAe": nb2_8_dualwideAe,
       "nb2-8-dualwideAp": nb2_8_dualwideAp,
       "nb2-8-dualwideAn": nb2_8_dualwideAn,
       "nb2-8-dualwideLa": nb2_8_dualwideLa,
       "nb2-8-dualwideWa": nb2_8_dualwideWa,
       "nb2-8-dualwideAa": nb2_8_dualwideAa,
       "nb2-8-dualwideAb": nb2_8_dualwideAb,
       "nb2-8-dualwideBf": nb2_8_dualwideBf,
       "brouterBrdFwVers": brouterBrdFwVers,
       "noFw": noFw,
       "cecFw": cecFw,
       "hdwanFw": hdwanFw,
       "hdwan232Fw": hdwan232Fw,
       "hdwan449Fw": hdwan449Fw,
       "mp6ethFw": mp6ethFw,
       "cecStarFw": cecStarFw,
       "mpAtmFw": mpAtmFw,
       "mpFddiFw": mpFddiFw,
       "mp6EthFlFw": mp6EthFlFw,
       "nbroFw": nbroFw,
       "nbocFw": nbocFw,
       "dpeFw": dpeFw,
       "intrepidFw": intrepidFw,
       "mbriFw": mbriFw,
       "qwanFw": qwanFw,
       "scoreFw": scoreFw,
       "blueridgeFw": blueridgeFw,
       "brouterBrdSwVers": brouterBrdSwVers,
       "noSw": noSw,
       "mp6eth": mp6eth,
       "spectreIsdnHuge": spectreIsdnHuge,
       "nbroihBp": nbroihBp,
       "nbroihCp": nbroihCp,
       "nbroihXw": nbroihXw,
       "nbroihCx": nbroihCx,
       "nbroihBa": nbroihBa,
       "nbroih422": nbroih422,
       "nbroihSn": nbroihSn,
       "nbroihRb": nbroihRb,
       "nbroihFf": nbroihFf,
       "nbroih427": nbroih427,
       "nbroih421": nbroih421,
       "nbroihAppn": nbroihAppn,
       "nbroihLm": nbroihLm,
       "nbroihLt": nbroihLt,
       "nbroihWm": nbroihWm,
       "nbroihWt": nbroihWt,
       "nbroihAe": nbroihAe,
       "nbroihAp": nbroihAp,
       "nbroihAn": nbroihAn,
       "nbroihLa": nbroihLa,
       "nbroihWa": nbroihWa,
       "nbroih424": nbroih424,
       "nbroihAb": nbroihAb,
       "nbroih423": nbroih423,
       "nbroTrHuge": nbroTrHuge,
       "nbroTrlBp": nbroTrlBp,
       "nbroTrlCp": nbroTrlCp,
       "nbroTrlXw": nbroTrlXw,
       "nbroTrlCx": nbroTrlCx,
       "nbroTrlBa": nbroTrlBa,
       "nbro322": nbro322,
       "nbroTrlSn": nbroTrlSn,
       "nbroTrlRb": nbroTrlRb,
       "nbroTrlFf": nbroTrlFf,
       "nbroTrl327": nbroTrl327,
       "nbro321": nbro321,
       "nbroTrlAppn": nbroTrlAppn,
       "nbroTrlLm": nbroTrlLm,
       "nbroTrlLt": nbroTrlLt,
       "nbroTrlWm": nbroTrlWm,
       "nbroTrlWt": nbroTrlWt,
       "nbroTrlAe": nbroTrlAe,
       "nbroTrlAp": nbroTrlAp,
       "nbroTrlAn": nbroTrlAn,
       "nbroTrlLa": nbroTrlLa,
       "nbroTrlWa": nbroTrlWa,
       "nbroTrlAa": nbroTrlAa,
       "nbroTrlAb": nbroTrlAb,
       "nbroTrl323": nbroTrl323,
       "nbroTrIsdn": nbroTrIsdn,
       "nbroTrIsdnBp": nbroTrIsdnBp,
       "nbroTrIsdnCp": nbroTrIsdnCp,
       "nbroTrIsdnXw": nbroTrIsdnXw,
       "nbroTrIsdnCx": nbroTrIsdnCx,
       "nbroTrIsdnBa": nbroTrIsdnBa,
       "nbroTrIsdnAr": nbroTrIsdnAr,
       "nbroTrIsdnSn": nbroTrIsdnSn,
       "nbroTrIsdnRb": nbroTrIsdnRb,
       "nbroTrIsdnFf": nbroTrIsdnFf,
       "nbro527": nbro527,
       "nbroTrIsdnBx": nbroTrIsdnBx,
       "nbroTrIsdnAppn": nbroTrIsdnAppn,
       "nbroTrIsdnLm": nbroTrIsdnLm,
       "nbroTrIsdnLt": nbroTrIsdnLt,
       "nbroTrIsdnWm": nbroTrIsdnWm,
       "nbroTrIsdnWt": nbroTrIsdnWt,
       "nbroTrIsdnAe": nbroTrIsdnAe,
       "nbroTrIsdnAp": nbroTrIsdnAp,
       "nbroTrIsdnAn": nbroTrIsdnAn,
       "nbroTrIsdnLa": nbroTrIsdnLa,
       "nbroTrIsdnWa": nbroTrIsdnWa,
       "nbroTrIsdnAa": nbroTrIsdnAa,
       "nbroTrIsdnAb": nbroTrIsdnAb,
       "nbro523": nbro523,
       "nbroTrNext": nbroTrNext,
       "nbroTrhBp": nbroTrhBp,
       "nbroTrhCp": nbroTrhCp,
       "nbroTrhXw": nbroTrhXw,
       "nbroTrhCx": nbroTrhCx,
       "nbroTrhBa": nbroTrhBa,
       "nbroTrh322": nbroTrh322,
       "nbroTrhSn": nbroTrhSn,
       "nbroTrhRb": nbroTrhRb,
       "nbroTrhFf": nbroTrhFf,
       "nbroTrh327": nbroTrh327,
       "nbroTrh321": nbroTrh321,
       "nbroTrhAppn": nbroTrhAppn,
       "nbroTrhLm": nbroTrhLm,
       "nbroTrhLt": nbroTrhLt,
       "nbroTrhWm": nbroTrhWm,
       "nbroTrhWt": nbroTrhWt,
       "nbroTrhAe": nbroTrhAe,
       "nbroTrhAp": nbroTrhAp,
       "nbroTrhAn": nbroTrhAn,
       "nbroTrhLa": nbroTrhLa,
       "nbroTrhWa": nbroTrhWa,
       "nbroTrhAa": nbroTrhAa,
       "nbroTrhAb": nbroTrhAb,
       "nbroTrh323": nbroTrh323,
       "nbro2Eth": nbro2Eth,
       "nbro2EthIsdn": nbro2EthIsdn,
       "officeConnRtr": officeConnRtr,
       "ocRtrBp": ocRtrBp,
       "ocRtrCp": ocRtrCp,
       "ocRtrXw": ocRtrXw,
       "ocRtrCx": ocRtrCx,
       "ocRtrBa": ocRtrBa,
       "ocRtrAr": ocRtrAr,
       "ocRtrSn": ocRtrSn,
       "ocRtrRb": ocRtrRb,
       "ocRtrFf": ocRtrFf,
       "ocRtrCf": ocRtrCf,
       "ocRtrBx": ocRtrBx,
       "ocRtrAppn": ocRtrAppn,
       "ocRtrLm": ocRtrLm,
       "ocRtrLt": ocRtrLt,
       "ocRtrWm": ocRtrWm,
       "ocRtrWt": ocRtrWt,
       "ocRtrAe": ocRtrAe,
       "ocRtrAp": ocRtrAp,
       "ocRtrAn": ocRtrAn,
       "ocRtrLa": ocRtrLa,
       "ocRtrWa": ocRtrWa,
       "ocRtrAa": ocRtrAa,
       "ocRtrAb": ocRtrAb,
       "ocRtrBf": ocRtrBf,
       "intrepidRtr": intrepidRtr,
       "superStackSwitch1100Router": superStackSwitch1100Router,
       "scoreRtr": scoreRtr,
       "copperRtr": copperRtr,
       "easterRtr": easterRtr,
       "rtr400Hw": rtr400Hw,
       "rtr400Hs": rtr400Hs,
       "genericMSWorkstation": genericMSWorkstation,
       "deskManProduct": deskManProduct,
       "ethernetSoftHub": ethernetSoftHub,
       "ethernetDTAnode": ethernetDTAnode,
       "tokenRingSoftHub": tokenRingSoftHub,
       "tokenRingDTAnode": tokenRingDTAnode,
       "genericMSServer": genericMSServer,
       "genericUnixServer": genericUnixServer,
       "hub": hub,
       "linkBuilder3GH": linkBuilder3GH,
       "linkBuilder10BTi": linkBuilder10BTi,
       "linkBuilderECS": linkBuilderECS,
       "linkBuilderMSH": linkBuilderMSH,
       "linkBuilderFMS": linkBuilderFMS,
       "linkBuilderFddiWorkGroupHub": linkBuilderFddiWorkGroupHub,
       "linkBuilderFMSII": linkBuilderFMSII,
       "linkSwitchFMS": linkSwitchFMS,
       "linkSwitchMSH": linkSwitchMSH,
       "linkBuilderFMSLBridge": linkBuilderFMSLBridge,
       "linkBuilderTP8i": linkBuilderTP8i,
       "linkBuilderMSHFddi": linkBuilderMSHFddi,
       "linkSwitch1000": linkSwitch1000,
       "linkSwitch500": linkSwitch500,
       "linkSwitch2700AU": linkSwitch2700AU,
       "linkSwitch2700Bridge": linkSwitch2700Bridge,
       "linkBuilderFMS100LBridge": linkBuilderFMS100LBridge,
       "linkSwitch2700TliAU": linkSwitch2700TliAU,
       "linkSwitch2700TliBridge": linkSwitch2700TliBridge,
       "linkBuilderFMS100": linkBuilderFMS100,
       "officeConnect-Hub8M": officeConnect_Hub8M,
       "linkSwitch3000": linkSwitch3000,
       "mshSwitch": mshSwitch,
       "linkSwitch2000TR": linkSwitch2000TR,
       "oncoreFastModuleFPA100": oncoreFastModuleFPA100,
       "oncoreFastModuleFPA10": oncoreFastModuleFPA10,
       "oncoreFastModuleFPA10FX": oncoreFastModuleFPA10FX,
       "oncoreFastModuleBPA": oncoreFastModuleBPA,
       "superStackDesktopSwitch": superStackDesktopSwitch,
       "oncoreFastModuleFPA100TX": oncoreFastModuleFPA100TX,
       "officeConnect-Switch140M": officeConnect_Switch140M,
       "superStackSwitch9000SX": superStackSwitch9000SX,
       "coreBuilder9000": coreBuilder9000,
       "coreBuilder9000-chassis": coreBuilder9000_chassis,
       "coreBuilder9000-16slot": coreBuilder9000_16slot,
       "coreBuilder9000-7slot": coreBuilder9000_7slot,
       "coreBuilder9000-8slot": coreBuilder9000_8slot,
       "coreBuilder9000-4slot": coreBuilder9000_4slot,
       "superStackSwitch3800": superStackSwitch3800,
       "cb5000TRFastModule": cb5000TRFastModule,
       "superStackSwitch9100": superStackSwitch9100,
       "superStackSwitchSoyuz": superStackSwitchSoyuz,
       "superStackSwitch4300": superStackSwitch4300,
       "superStackSwitch3824": superStackSwitch3824,
       "superStackSwitch3812": superStackSwitch3812,
       "switch3226": switch3226,
       "switch3250": switch3250,
       "switch3870-24-port": switch3870_24_port,
       "switch3870-48-port": switch3870_48_port,
       "switch3848": switch3848,
       "switch3228": switch3228,
       "switch3252": switch3252,
       "cards": cards,
       "linkBuilder3GH-cards": linkBuilder3GH_cards,
       "linkBuilder10BTi-cards": linkBuilder10BTi_cards,
       "linkBuilder10BTi-cards-utp": linkBuilder10BTi_cards_utp,
       "linkBuilder10BT-cards-utp": linkBuilder10BT_cards_utp,
       "linkBuilderECS-cards": linkBuilderECS_cards,
       "linkBuilderMSH-cards": linkBuilderMSH_cards,
       "linkBuilderFMS-cards": linkBuilderFMS_cards,
       "linkBuilderFMS-cards-utp": linkBuilderFMS_cards_utp,
       "linkBuilderFMS-cards-coax": linkBuilderFMS_cards_coax,
       "linkBuilderFMS-cards-fiber": linkBuilderFMS_cards_fiber,
       "linkBuilderFMS-cards-12fiber": linkBuilderFMS_cards_12fiber,
       "linkBuilderFMS-cards-24utp": linkBuilderFMS_cards_24utp,
       "linkBuilderFMSII-cards": linkBuilderFMSII_cards,
       "linkBuilderFMSII-cards-12tp-rj45": linkBuilderFMSII_cards_12tp_rj45,
       "linkBuilderFMSII-cards-10coax-bnc": linkBuilderFMSII_cards_10coax_bnc,
       "linkBuilderFMSII-cards-6fiber-st": linkBuilderFMSII_cards_6fiber_st,
       "linkBuilderFMSII-cards-12fiber-st": linkBuilderFMSII_cards_12fiber_st,
       "linkBuilderFMSII-cards-24tp-rj45": linkBuilderFMSII_cards_24tp_rj45,
       "linkBuilderFMSII-cards-24tp-telco": linkBuilderFMSII_cards_24tp_telco,
       "superStackHub10-cards-12tp-rj45": superStackHub10_cards_12tp_rj45,
       "superStackHub10-cards-24tp-rj45": superStackHub10_cards_24tp_rj45,
       "superStackHub10-cards-6fiber-st": superStackHub10_cards_6fiber_st,
       "superStackHub10-cards-24tp-telco": superStackHub10_cards_24tp_telco,
       "a3C512": a3C512,
       "a3C512-withBNC-expn-card": a3C512_withBNC_expn_card,
       "a3C512-withAUI-expn-card": a3C512_withAUI_expn_card,
       "a3C512-withFOIRL-expn-card": a3C512_withFOIRL_expn_card,
       "linkBuilderTP8i-cards": linkBuilderTP8i_cards,
       "linkBuilderTP8i-cards-8tp-rj45": linkBuilderTP8i_cards_8tp_rj45,
       "linkSwitch1000-cards": linkSwitch1000_cards,
       "linkSwitch1000-cards-24tp-rj45": linkSwitch1000_cards_24tp_rj45,
       "linkSwitch1000-cards-12tp-rj45": linkSwitch1000_cards_12tp_rj45,
       "linkSwitch3000-cards-5fiber-sc": linkSwitch3000_cards_5fiber_sc,
       "linkSwitch3000-cards-8tp-rj45": linkSwitch3000_cards_8tp_rj45,
       "superStackSwitch1000-cards-24tp-rj45": superStackSwitch1000_cards_24tp_rj45,
       "superStackSwitch1000-cards-12tp-rj45": superStackSwitch1000_cards_12tp_rj45,
       "superStackSwitch3000-cards-5fiber-sc": superStackSwitch3000_cards_5fiber_sc,
       "superStackSwitch3000-cards-8tp-rj45": superStackSwitch3000_cards_8tp_rj45,
       "oncore-cards-5fiber-sc-2tp-rj45-blk": oncore_cards_5fiber_sc_2tp_rj45_blk,
       "oncore-cards-24tp-telco-blk": oncore_cards_24tp_telco_blk,
       "oncore-cards-24tp-telco-1fiber-sc-blk": oncore_cards_24tp_telco_1fiber_sc_blk,
       "oncore-cards-1fiber-sc-7blk": oncore_cards_1fiber_sc_7blk,
       "superStackSwitch1000-3000-cards-atm": superStackSwitch1000_3000_cards_atm,
       "oncore-cards-2fiber-sc-7blk": oncore_cards_2fiber_sc_7blk,
       "oncore-cards-1fiber-sc-tp-rj45-7blk": oncore_cards_1fiber_sc_tp_rj45_7blk,
       "oncore-cards-1fiber-sc-atm-7blk": oncore_cards_1fiber_sc_atm_7blk,
       "superStackDesktopSwitch-24tp-rj45": superStackDesktopSwitch_24tp_rj45,
       "linkSwitch3000-cards-12tp-rj45": linkSwitch3000_cards_12tp_rj45,
       "superStackSwitch3000-cards-12tp-rj45": superStackSwitch3000_cards_12tp_rj45,
       "oncore-cards-7tp-rj45-blk": oncore_cards_7tp_rj45_blk,
       "officeConnect-Switch140M-5tp-rj45": officeConnect_Switch140M_5tp_rj45,
       "superStackSwitch3000-cards-12tp-rj45-ten100": superStackSwitch3000_cards_12tp_rj45_ten100,
       "linkBuilderFMS100-cards": linkBuilderFMS100_cards,
       "linkBuilderFMS100-cards-12utp": linkBuilderFMS100_cards_12utp,
       "linkBuilderFMS100-cards-12T4": linkBuilderFMS100_cards_12T4,
       "linkBuilderFMS100-cards-24TX": linkBuilderFMS100_cards_24TX,
       "linkBuilderFMS100-cards-12TX": linkBuilderFMS100_cards_12TX,
       "officeConnect-Hub8M-cards": officeConnect_Hub8M_cards,
       "officeConnect-Hub8M-cards-8tp-rj45": officeConnect_Hub8M_cards_8tp_rj45,
       "linkSwitch2000TR-cards": linkSwitch2000TR_cards,
       "linkSwitch2000TR-cards-12tp-rj45": linkSwitch2000TR_cards_12tp_rj45,
       "coreBuilder9000-cards": coreBuilder9000_cards,
       "coreBuilder9000-packet-cards": coreBuilder9000_packet_cards,
       "cb9000-layer2-switch-cards": cb9000_layer2_switch_cards,
       "cb9000-cards-20-rj45-10T-100T": cb9000_cards_20_rj45_10T_100T,
       "cb9000-cards-36-rj45-10T-100T": cb9000_cards_36_rj45_10T_100T,
       "cb9000-cards-36-rj45-10T": cb9000_cards_36_rj45_10T,
       "cb9000-cards-10-fiber-100T": cb9000_cards_10_fiber_100T,
       "cb9000-cards-36-telco-10T-100T": cb9000_cards_36_telco_10T_100T,
       "cb9000-cards-9-fiber-1000T": cb9000_cards_9_fiber_1000T,
       "cb9000-cards-20-mt-fiber-100T": cb9000_cards_20_mt_fiber_100T,
       "cb9000-cards-tb-36-rj45-10T-100T": cb9000_cards_tb_36_rj45_10T_100T,
       "cb9000-cards-tb-36-telco-10T-100T": cb9000_cards_tb_36_telco_10T_100T,
       "cb9000-cards-20-fiber-1000T": cb9000_cards_20_fiber_1000T,
       "cb9000-cards-9-fiber-1000LX": cb9000_cards_9_fiber_1000LX,
       "cb9000-cards-12BT-1000T": cb9000_cards_12BT_1000T,
       "cb9000-layer3-switch-cards": cb9000_layer3_switch_cards,
       "cb9000-cards-12-rj45-100T": cb9000_cards_12_rj45_100T,
       "cb9000-cards-6-fddi": cb9000_cards_6_fddi,
       "cb9000-cards-router": cb9000_cards_router,
       "cb9000-cards-10-fiber": cb9000_cards_10_fiber,
       "cb9000-cards-4-gbic-1000T": cb9000_cards_4_gbic_1000T,
       "cb9000-cards-carrier": cb9000_cards_carrier,
       "cb9000-cards-18tx": cb9000_cards_18tx,
       "cb9000-cards-18fx": cb9000_cards_18fx,
       "cb9000-layer2-fabric-cards": cb9000_layer2_fabric_cards,
       "cb9000-cards-fabric-24": cb9000_cards_fabric_24,
       "cb9000-cards-fabric-24T": cb9000_cards_fabric_24T,
       "cb9000-cards-fabric-6-3": cb9000_cards_fabric_6_3,
       "cb9000-cards-fabric-36": cb9000_cards_fabric_36,
       "cb9000-layer1-cards": cb9000_layer1_cards,
       "cb9000-cards-2-fiber-1000T": cb9000_cards_2_fiber_1000T,
       "cb9000-cards-4-fiber-1000T": cb9000_cards_4_fiber_1000T,
       "cb9000-cards-2-fiber-lx-1000T": cb9000_cards_2_fiber_lx_1000T,
       "cb9000-layer2-tb-cards": cb9000_layer2_tb_cards,
       "cb9000-layer3-fabric-cards": cb9000_layer3_fabric_cards,
       "cb9000-cards-fabric-fba8": cb9000_cards_fabric_fba8,
       "cb9000-cards-fabric-16": cb9000_cards_fabric_16,
       "coreBuilder9000-cell-cards": coreBuilder9000_cell_cards,
       "cb9000-cell-switch-cards": cb9000_cell_switch_cards,
       "cb9000-cell-carrier-cards": cb9000_cell_carrier_cards,
       "cb9000-cell-modularIfc-2-groups": cb9000_cell_modularIfc_2_groups,
       "cb9000-cell-daughter-cards": cb9000_cell_daughter_cards,
       "cb9000-cell-1-OC12-MM": cb9000_cell_1_OC12_MM,
       "cb9000-cell-1-OC12-SM": cb9000_cell_1_OC12_SM,
       "cb9000-cell-4-OC3-MM": cb9000_cell_4_OC3_MM,
       "cb9000-cell-4-OC3-SM": cb9000_cell_4_OC3_SM,
       "cb9000-cell-1-OC3-SM-3-OC3-MM": cb9000_cell_1_OC3_SM_3_OC3_MM,
       "cb9000-cell-4-OC3-rj45": cb9000_cell_4_OC3_rj45,
       "cb9000-cell-2-T3-BNC": cb9000_cell_2_T3_BNC,
       "cb9000-cell-2-E3-BNC": cb9000_cell_2_E3_BNC,
       "cb9000-cell-4-OC3-SM-LR": cb9000_cell_4_OC3_SM_LR,
       "cb9000-cell-2-OC3-SM-LR": cb9000_cell_2_OC3_SM_LR,
       "cb9000-cell-integrated-cards": cb9000_cell_integrated_cards,
       "cb9000-cell-8-T1-IMA-rj48c": cb9000_cell_8_T1_IMA_rj48c,
       "cb9000-cell-8-E1-IMA-rj48c": cb9000_cell_8_E1_IMA_rj48c,
       "cb9000-cell-8-T1-CES-rj48c": cb9000_cell_8_T1_CES_rj48c,
       "cb9000-cell-8-E1-CES-rj48c": cb9000_cell_8_E1_CES_rj48c,
       "cb9000-cell-combined-cards": cb9000_cell_combined_cards,
       "cb9000-cellsw-4-fiber-1000T": cb9000_cellsw_4_fiber_1000T,
       "cb9000-cellsw-20-rj45-10T-100T": cb9000_cellsw_20_rj45_10T_100T,
       "cb9000-cellsw-36-rj45-10T-100T": cb9000_cellsw_36_rj45_10T_100T,
       "cb9000-cellsw-36-telco-10T-100T": cb9000_cellsw_36_telco_10T_100T,
       "cb9000-cellsw-40-telco-10T-100T": cb9000_cellsw_40_telco_10T_100T,
       "cb9000-cell-fabric-cards": cb9000_cell_fabric_cards,
       "cb9000-cards-cell-fabric-1": cb9000_cards_cell_fabric_1,
       "cb9000-cards-cell-fabric-1-7slot": cb9000_cards_cell_fabric_1_7slot,
       "coreBuilder9000-mgmt-cards": coreBuilder9000_mgmt_cards,
       "cb9000-cards-eme": cb9000_cards_eme,
       "cb9000-cards-emec": cb9000_cards_emec,
       "cb9000-cards-emel": cb9000_cards_emel,
       "coreBuilder9000-app-cards": coreBuilder9000_app_cards,
       "cb9000-app-BIG-ip": cb9000_app_BIG_ip,
       "cb9000-app-3DNS": cb9000_app_3DNS,
       "cb9000-app-global-site": cb9000_app_global_site,
       "cb5000TRFastModule-cards": cb5000TRFastModule_cards,
       "cb5000TRFastModule-card-6508M": cb5000TRFastModule_card_6508M,
       "cb5000TRFastModule-card-6508M2": cb5000TRFastModule_card_6508M2,
       "cb5000TRFastModule-card-atm": cb5000TRFastModule_card_atm,
       "cb5000TRFastModule-card-fddi": cb5000TRFastModule_card_fddi,
       "cb5000TRFastModule-card-tif-sc": cb5000TRFastModule_card_tif_sc,
       "cb5000TRFastModule-card-tif-rj45": cb5000TRFastModule_card_tif_rj45,
       "superStack3300-cards": superStack3300_cards,
       "stanley": stanley,
       "superStack-3300-atm-uplink": superStack_3300_atm_uplink,
       "chipSets": chipSets,
       "valcan": valcan,
       "oem": oem,
       "linkConv250": linkConv250,
       "linkConv251": linkConv251,
       "linkConv350": linkConv350,
       "linkConv351": linkConv351,
       "atm": atm,
       "cELLplex7000": cELLplex7000,
       "cELLplex7000-cards": cELLplex7000_cards,
       "cELLplex-7x00cardBridge": cELLplex_7x00cardBridge,
       "cELLplex-7200card": cELLplex_7200card,
       "cELLplex-7200Fcard": cELLplex_7200Fcard,
       "cELLplex-7400card": cELLplex_7400card,
       "cELLplex-7600card": cELLplex_7600card,
       "cELLplex-7800card": cELLplex_7800card,
       "cELLplex-7900card": cELLplex_7900card,
       "pathBuilder": pathBuilder,
       "coreBuilderSip7000": coreBuilderSip7000,
       "cb7000Family": cb7000Family,
       "cb7000-fabric-cards": cb7000_fabric_cards,
       "cb7000-fabric-switch": cb7000_fabric_switch,
       "cb7000-fabric-switch-hd": cb7000_fabric_switch_hd,
       "cb7000-accelerator-cards": cb7000_accelerator_cards,
       "cb7000-FastBUS": cb7000_FastBUS,
       "cb7000-FastBUS-Java": cb7000_FastBUS_Java,
       "cb7000-FastBUS-7600": cb7000_FastBUS_7600,
       "cb7000-FastBUS-7600-Java": cb7000_FastBUS_7600_Java,
       "cb7000-carrier-cards": cb7000_carrier_cards,
       "cb7000-4-ports-ifc": cb7000_4_ports_ifc,
       "cb7000-8-ports-ifc": cb7000_8_ports_ifc,
       "cb7000-OC12-carrier-ifc": cb7000_OC12_carrier_ifc,
       "cb7000-7200-ifc": cb7000_7200_ifc,
       "cb7000-7200F-ifc": cb7000_7200F_ifc,
       "cb7000-7400-ifc": cb7000_7400_ifc,
       "cb7000-7600-ifc": cb7000_7600_ifc,
       "cb7000-7800-ifc": cb7000_7800_ifc,
       "cb7000-7900-ifc": cb7000_7900_ifc,
       "cb7000-daughter-cards": cb7000_daughter_cards,
       "cb7000-1-OC3-SM": cb7000_1_OC3_SM,
       "cb7000-1-OC3-MM": cb7000_1_OC3_MM,
       "cb7000-1-DS3-BNC": cb7000_1_DS3_BNC,
       "cb7000-1-OC3-rj45": cb7000_1_OC3_rj45,
       "cb7000-1-OC12-SM": cb7000_1_OC12_SM,
       "cb7000-1-OC12-MM": cb7000_1_OC12_MM,
       "cb7000-12-10T-rj45-in-7200": cb7000_12_10T_rj45_in_7200,
       "cb7000-12-fiber-10T-FL-in-7200": cb7000_12_fiber_10T_FL_in_7200,
       "cb7000-12-10T-rj21": cb7000_12_10T_rj21,
       "cb7000-2-fiber-100T": cb7000_2_fiber_100T,
       "cb7000-2-10T-100T-rj45": cb7000_2_10T_100T_rj45,
       "cb7000-4-fiber-1000T-in-7800": cb7000_4_fiber_1000T_in_7800,
       "cb7000-36-10T-100T-rj45-in-7900": cb7000_36_10T_100T_rj45_in_7900,
       "cb7000-1-E3-BNC": cb7000_1_E3_BNC,
       "powerSupplies": powerSupplies,
       "rpsIIMgmtModule": rpsIIMgmtModule,
       "tdm": tdm,
       "broadbandAccess": broadbandAccess,
       "cableModems": cableModems,
       "mcnsCmHeadend": mcnsCmHeadend,
       "mcnsExt2WayCm": mcnsExt2WayCm,
       "mcnsExtTelcoCm": mcnsExtTelcoCm,
       "switches": switches,
       "corebuilderProductsIII": corebuilderProductsIII,
       "corebuilderModularProducts": corebuilderModularProducts,
       "cbModular3500Family": cbModular3500Family,
       "cb3500": cb3500,
       "corebuilderSystemProducts": corebuilderSystemProducts,
       "cbSystem9400Family": cbSystem9400Family,
       "cb9400": cb9400,
       "corebuilderChassisProducts": corebuilderChassisProducts,
       "superstackProducts": superstackProducts,
       "superstackModularProducts": superstackModularProducts,
       "superstackSystemProducts": superstackSystemProducts,
       "ssSystem3900Family": ssSystem3900Family,
       "ss3900-24": ss3900_24,
       "ss3900-36": ss3900_36,
       "ssSystem9300Family": ssSystem9300Family,
       "ss9300": ss9300,
       "ssServerLoadBalancers": ssServerLoadBalancers,
       "baseLoadBalancer": baseLoadBalancer,
       "plusLoadBalancer": plusLoadBalancer,
       "superstackChassisProducts": superstackChassisProducts,
       "minicoreProducts": minicoreProducts,
       "miniChassisSwitch4005": miniChassisSwitch4005,
       "jvProducts": jvProducts,
       "coreChassisSwitch7700": coreChassisSwitch7700,
       "jvRouters": jvRouters,
       "jvWanRouter5009": jvWanRouter5009,
       "jvWanRouter5231": jvWanRouter5231,
       "jvWanRouter5640": jvWanRouter5640,
       "jvWanRouter5680": jvWanRouter5680,
       "jvWanRouter3012": jvWanRouter3012,
       "jvWanRouter3013": jvWanRouter3013,
       "jvWanRouter3014": jvWanRouter3014,
       "jvWanRouter3015": jvWanRouter3015,
       "jvWanRouter3016": jvWanRouter3016,
       "jvWanRouter3018": jvWanRouter3018,
       "jvWanRouter6040": jvWanRouter6040,
       "jvWanRouter6080": jvWanRouter6080,
       "jvWanRouter3030": jvWanRouter3030,
       "jvWanRouter3031": jvWanRouter3031,
       "jvWanRouter3032": jvWanRouter3032,
       "jvWanRouter3033": jvWanRouter3033,
       "jvWanRouter3034": jvWanRouter3034,
       "jvRouter3035": jvRouter3035,
       "jvRouterxxxx": jvRouterxxxx,
       "jvRouteryyyy": jvRouteryyyy,
       "jvRouter5012": jvRouter5012,
       "jvRouter5232": jvRouter5232,
       "jvRouter5642": jvRouter5642,
       "jvRouter5682": jvRouter5682,
       "jvSwitches": jvSwitches,
       "jvSwitch7700-8": jvSwitch7700_8,
       "jvSwitch7700-4": jvSwitch7700_4,
       "jvSwitch5500-MC6-EI": jvSwitch5500_MC6_EI,
       "jvSwitch8807": jvSwitch8807,
       "jvSwitch8810": jvSwitch8810,
       "jvSwitch8814": jvSwitch8814,
       "jvSwitch5500G-ei-24": jvSwitch5500G_ei_24,
       "jvSwitch5500G-ei-48": jvSwitch5500G_ei_48,
       "jvSwitch5500-si-24": jvSwitch5500_si_24,
       "jvSwitch5500-si-28t": jvSwitch5500_si_28t,
       "jvSwitch5500-si-28": jvSwitch5500_si_28,
       "jvSwitch5500-si-52": jvSwitch5500_si_52,
       "jvSwitch5500-ei-28": jvSwitch5500_ei_28,
       "jvSwitch5500-ei-52": jvSwitch5500_ei_52,
       "jvSwitch5500-eipwr-28": jvSwitch5500_eipwr_28,
       "jvSwitch5500-eipwr-52": jvSwitch5500_eipwr_52,
       "jvSwitch5500-ei-28fx": jvSwitch5500_ei_28fx,
       "voice": voice,
       "phones": phones,
       "basicPhone": basicPhone,
       "businessPhone": businessPhone,
       "bp3104ProfessionalPhone": bp3104ProfessionalPhone,
       "executivePhone": executivePhone,
       "wirelessPhone": wirelessPhone,
       "gateways": gateways,
       "callProcessors": callProcessors,
       "nbx100": nbx100,
       "nbx25": nbx25,
       "superStackNbxCallProcessor": superStackNbxCallProcessor,
       "nbx250": nbx250,
       "nbx500": nbx500,
       "nbx750": nbx750,
       "officeConnectNbxCallProcessor": officeConnectNbxCallProcessor,
       "nbxv3000": nbxv3000,
       "intranetAppliances": intranetAppliances,
       "fireWalls": fireWalls,
       "superStackFireWall": superStackFireWall,
       "secureIX3100-10": secureIX3100_10,
       "secureIX3100-50": secureIX3100_50,
       "secureIX3100": secureIX3100,
       "secureIX4100": secureIX4100,
       "secureIX5100": secureIX5100,
       "servers": servers,
       "officeConnectStorageServer": officeConnectStorageServer,
       "officeConnectInternetServer": officeConnectInternetServer,
       "officeConnectEmailServer": officeConnectEmailServer,
       "storageServer150": storageServer150,
       "accelerators": accelerators,
       "sslAccelerator": sslAccelerator,
       "xDSL": xDSL,
       "sDSLGateway": sDSLGateway,
       "vDSL": vDSL,
       "vCNMultiAccessConcentrator": vCNMultiAccessConcentrator,
       "aDSLRouterVoDSLPorts": aDSLRouterVoDSLPorts,
       "aDSLRouterNoVoDSLPorts": aDSLRouterNoVoDSLPorts,
       "gSHDSLRouterVoDSLPorts": gSHDSLRouterVoDSLPorts,
       "gSHDSLRouterNoVoDSLPorts": gSHDSLRouterNoVoDSLPorts,
       "cableDSLGateway": cableDSLGateway,
       "cableDSLSecureGateway": cableDSLSecureGateway,
       "cableWirelessDSLGateway": cableWirelessDSLGateway,
       "cableWireless54Mbps11gDSLGateway": cableWireless54Mbps11gDSLGateway,
       "xdslvpnFirewall": xdslvpnFirewall,
       "xdslsecureRouter": xdslsecureRouter,
       "wireless11gAdslRouter": wireless11gAdslRouter,
       "wirelessDevices": wirelessDevices,
       "wLanAP8000": wLanAP8000,
       "wLanAP6000": wLanAP6000,
       "wLanAP2000": wLanAP2000,
       "wLanWrkgrpBridge": wLanWrkgrpBridge,
       "wLantoLanBridge": wLantoLanBridge,
       "wLanAP8500": wLanAP8500,
       "wLanAPOfficeConnect11Mbps": wLanAPOfficeConnect11Mbps,
       "wLanAP8200": wLanAP8200,
       "wLanAPOfficeConnect54Mbps11g": wLanAPOfficeConnect54Mbps11g,
       "wlanAP8700": wlanAP8700,
       "wlanAP8250": wlanAP8250,
       "wlanAP8750": wlanAP8750,
       "wlanAP7250": wlanAP7250,
       "wlanWXR104": wlanWXR104,
       "wlanWX1206": wlanWX1206,
       "wlanWX4400": wlanWX4400,
       "wlan80211agWBridge": wlan80211agWBridge,
       "wlan11gOutdoorBtoBBridge": wlan11gOutdoorBtoBBridge,
       "wlan11gIndoorBtoBBridge": wlan11gIndoorBtoBBridge,
       "wlanAP11gPoE": wlanAP11gPoE,
       "networkJacks": networkJacks,
       "nj200": nj200,
       "nj205": nj205,
       "nj220": nj220,
       "nj225": nj225,
       "nj225FXSC": nj225FXSC,
       "nj225FXST": nj225FXST,
       "securitySwitches": securitySwitches,
       "securitySwitch6200": securitySwitch6200,
       "brouterMIB": brouterMIB,
       "amp-mib": amp_mib,
       "genericTrap": genericTrap,
       "viewBuilderApps": viewBuilderApps,
       "specificTrap": specificTrap,
       "linkBuilder3GH-mib": linkBuilder3GH_mib,
       "linkBuilder10BTi-mib": linkBuilder10BTi_mib,
       "linkBuilderECS-mib": linkBuilderECS_mib,
       "generic": generic,
       "netBuilder-mib": netBuilder_mib,
       "lBridgeECS-mib": lBridgeECS_mib,
       "deskMan": deskMan,
       "linkBuilderMSH-mib": linkBuilderMSH_mib,
       "a3ComUnused15": a3ComUnused15,
       "a3comFddiWGHubMib": a3comFddiWGHubMib,
       "linkSwitch-mib": linkSwitch_mib,
       "linkSwitch1000-mib": linkSwitch1000_mib,
       "linkBuilderFMS100-mib": linkBuilderFMS100_mib,
       "ncdMibs": ncdMibs,
       "officeConnect-Hub8M-mib": officeConnect_Hub8M_mib,
       "linkSwitch2000TR-mib": linkSwitch2000TR_mib,
       "vlanServer-mib": vlanServer_mib,
       "terminalServerMib": terminalServerMib,
       "rpsIIMgmtModule-mib": rpsIIMgmtModule_mib,
       "transcendEnterpriseMgr": transcendEnterpriseMgr,
       "watchModule": watchModule,
       "superStackSwitch9000SX-mib": superStackSwitch9000SX_mib,
       "coreBuilder9000-mib": coreBuilder9000_mib,
       "switchingSystemsMibs": switchingSystemsMibs,
       "cableModem-mib": cableModem_mib,
       "edgemonitor-mib": edgemonitor_mib,
       "nic-mib": nic_mib,
       "palm-mib": palm_mib,
       "grand-prix-mib": grand_prix_mib,
       "wlan-mib": wlan_mib,
       "icdSipProxy-mib": icdSipProxy_mib,
       "webCache-mib": webCache_mib,
       "xDSLCommon-mib": xDSLCommon_mib,
       "superStack4300-mib": superStack4300_mib,
       "ldap3Com": ldap3Com,
       "ldapGeneric": ldapGeneric,
       "ldapCommWorks": ldapCommWorks,
       "a3ComLdapVcx": a3ComLdapVcx,
       "sslAcceleration-mib": sslAcceleration_mib,
       "networkManagement-mib": networkManagement_mib,
       "componentMgmtModule-mib": componentMgmtModule_mib,
       "firewall-mib": firewall_mib,
       "jv-mib": jv_mib,
       "a3ComPoe-mib": a3ComPoe_mib,
       "a3Com496MIB": a3Com496MIB,
       "voiceCoreExchange-mib": voiceCoreExchange_mib,
       "a3ComEntityIdentifier-mib": a3ComEntityIdentifier_mib,
       "a3ComTrpz-mib": a3ComTrpz_mib,
       "a3ComNetworkJack-mib": a3ComNetworkJack_mib,
       "synernetics": synernetics,
       "lanplex": lanplex,
       "lANplex-12-slot-support": lANplex_12_slot_support,
       "lANplex-4-slot-support": lANplex_4_slot_support,
       "lpsProducts": lpsProducts,
       "lps6000": lps6000,
       "lps6012": lps6012,
       "lps6012System": lps6012System,
       "lanplex-6012-System-2": lanplex_6012_System_2,
       "lanplex-6012-System-3": lanplex_6012_System_3,
       "lanplex-6012-System-4": lanplex_6012_System_4,
       "lanplex-6012-System-5": lanplex_6012_System_5,
       "lanplex-6012-System-6": lanplex_6012_System_6,
       "lps6012Chassis": lps6012Chassis,
       "lanplex-6012-Chassis-2": lanplex_6012_Chassis_2,
       "lanplex-6012-Chassis-3": lanplex_6012_Chassis_3,
       "lanplex-6012-Chassis-4": lanplex_6012_Chassis_4,
       "lanplex-6012-Chassis-5": lanplex_6012_Chassis_5,
       "lanplex-6012-Chassis-6": lanplex_6012_Chassis_6,
       "lps6012ESM": lps6012ESM,
       "lanplex-6012-ESM-2": lanplex_6012_ESM_2,
       "lanplex-6012-ESM-3": lanplex_6012_ESM_3,
       "lanplex-6012-ESM-4": lanplex_6012_ESM_4,
       "lanplex-6012-ESM-5": lanplex_6012_ESM_5,
       "lanplex-6012-ESM-6": lanplex_6012_ESM_6,
       "lps6012EFSM": lps6012EFSM,
       "lanplex-6012-EFSM-2": lanplex_6012_EFSM_2,
       "lanplex-6012-EFSM-3": lanplex_6012_EFSM_3,
       "lanplex-6012-EFSM-4": lanplex_6012_EFSM_4,
       "lanplex-6012-EFSM-5": lanplex_6012_EFSM_5,
       "lanplex-6012-EFSM-6": lanplex_6012_EFSM_6,
       "lps6012TRSM": lps6012TRSM,
       "lanplex-6012-TRSM-5": lanplex_6012_TRSM_5,
       "lanplex-6012-TRSM-6": lanplex_6012_TRSM_6,
       "lps6012TMM": lps6012TMM,
       "lanplex-6012-TMM-6": lanplex_6012_TMM_6,
       "lps6012FSM": lps6012FSM,
       "lanplex-6012-FSM-7": lanplex_6012_FSM_7,
       "lps6004": lps6004,
       "lps6004System": lps6004System,
       "lanplex-6004-System-2": lanplex_6004_System_2,
       "lanplex-6004-System-3": lanplex_6004_System_3,
       "lanplex-6004-System-4": lanplex_6004_System_4,
       "lanplex-6004-System-5": lanplex_6004_System_5,
       "lanplex-6004-System-6": lanplex_6004_System_6,
       "lps6004Chassis": lps6004Chassis,
       "lanplex-6004-Chassis-2": lanplex_6004_Chassis_2,
       "lanplex-6004-Chassis-3": lanplex_6004_Chassis_3,
       "lanplex-6004-Chassis-4": lanplex_6004_Chassis_4,
       "lanplex-6004-Chassis-5": lanplex_6004_Chassis_5,
       "lanplex-6004-Chassis-6": lanplex_6004_Chassis_6,
       "lps6004ESM": lps6004ESM,
       "lanplex-6004-ESM-2": lanplex_6004_ESM_2,
       "lanplex-6004-ESM-3": lanplex_6004_ESM_3,
       "lanplex-6004-ESM-4": lanplex_6004_ESM_4,
       "lanplex-6004-ESM-5": lanplex_6004_ESM_5,
       "lanplex-6004-ESM-6": lanplex_6004_ESM_6,
       "lps6004EFSM": lps6004EFSM,
       "lanplex-6004-EFSM-2": lanplex_6004_EFSM_2,
       "lanplex-6004-EFSM-3": lanplex_6004_EFSM_3,
       "lanplex-6004-EFSM-4": lanplex_6004_EFSM_4,
       "lanplex-6004-EFSM-5": lanplex_6004_EFSM_5,
       "lanplex-6004-EFSM-6": lanplex_6004_EFSM_6,
       "lps6004TRSM": lps6004TRSM,
       "lanplex-6004-TRSM-5": lanplex_6004_TRSM_5,
       "lanplex-6004-TRSM-6": lanplex_6004_TRSM_6,
       "lps6004TMM": lps6004TMM,
       "lanplex-6004-TMM-6": lanplex_6004_TMM_6,
       "lps6004FSM": lps6004FSM,
       "lanplex-6004-FSM-7": lanplex_6004_FSM_7,
       "lps2000": lps2000,
       "lps2500": lps2500,
       "lanplex-2500-2": lanplex_2500_2,
       "lanplex-2500-3": lanplex_2500_3,
       "lanplex-2500-4": lanplex_2500_4,
       "lanplex-2500-5": lanplex_2500_5,
       "lanplex-2500-6": lanplex_2500_6,
       "lss2200": lss2200,
       "linkSwitch-2200-2": linkSwitch_2200_2,
       "linkSwitch-2200-3": linkSwitch_2200_3,
       "linkSwitch-2200-4": linkSwitch_2200_4,
       "linkSwitch-2200-5": linkSwitch_2200_5,
       "linkSwitch-2200-6": linkSwitch_2200_6,
       "lps2016": lps2016,
       "lanplex-2016-2": lanplex_2016_2,
       "lanplex-2016-3": lanplex_2016_3,
       "lanplex-2016-4": lanplex_2016_4,
       "lanplex-2016-5": lanplex_2016_5,
       "lanplex-2016-6": lanplex_2016_6,
       "lss2200SS2": lss2200SS2,
       "linkSwitch-2200-SS2-7": linkSwitch_2200_SS2_7,
       "lanplexSystemsMib": lanplexSystemsMib,
       "lanplexOptFddi": lanplexOptFddi,
       "bicc": bicc,
       "bdn": bdn,
       "bdnDevices": bdnDevices,
       "centrum": centrum,
       "mibDoc": mibDoc,
       "centrumRemote": centrumRemote,
       "usRobotics": usRobotics,
       "usrSysOIDs": usrSysOIDs,
       "netServerII8": netServerII8,
       "netServerII16": netServerII16,
       "lanLinkerBRI": lanLinkerBRI,
       "lanLinkerD56k": lanLinkerD56k,
       "netServerII8imdm": netServerII8imdm,
       "netServerII16imdm": netServerII16imdm,
       "pilgrimCore": pilgrimCore,
       "viper": viper,
       "alc": alc,
       "duala": duala}
)
