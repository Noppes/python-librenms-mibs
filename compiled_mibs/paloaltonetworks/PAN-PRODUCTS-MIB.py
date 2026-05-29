# SNMP MIB module (PAN-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\paloaltonetworks\PAN-PRODUCTS-MIB

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

(panModules,
 panProductsMibs) = mibBuilder.importSymbols(
    "PAN-GLOBAL-REG",
    "panModules",
    "panProductsMibs")

(TcChassisType,) = mibBuilder.importSymbols(
    "PAN-GLOBAL-TC",
    "TcChassisType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

panProductsMibsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 4)
)
if mibBuilder.loadTexts:
    panProductsMibsModule.setRevisions(
        ("2013-04-15 16:50",
         "2011-02-09 16:10")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanPA_4050_ObjectIdentity = ObjectIdentity
panPA_4050 = _PanPA_4050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 1)
)
if mibBuilder.loadTexts:
    panPA_4050.setStatus("current")
_PanPA_4020_ObjectIdentity = ObjectIdentity
panPA_4020 = _PanPA_4020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 2)
)
if mibBuilder.loadTexts:
    panPA_4020.setStatus("current")
_PanPA_2050_ObjectIdentity = ObjectIdentity
panPA_2050 = _PanPA_2050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 3)
)
if mibBuilder.loadTexts:
    panPA_2050.setStatus("current")
_PanPA_2020_ObjectIdentity = ObjectIdentity
panPA_2020 = _PanPA_2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 4)
)
if mibBuilder.loadTexts:
    panPA_2020.setStatus("current")
_PanPA_4060_ObjectIdentity = ObjectIdentity
panPA_4060 = _PanPA_4060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 5)
)
if mibBuilder.loadTexts:
    panPA_4060.setStatus("current")
_PanPA_500_ObjectIdentity = ObjectIdentity
panPA_500 = _PanPA_500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 6)
)
if mibBuilder.loadTexts:
    panPA_500.setStatus("current")
_PanPanorama_ObjectIdentity = ObjectIdentity
panPanorama = _PanPanorama_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 7)
)
if mibBuilder.loadTexts:
    panPanorama.setStatus("current")
_PanPA_5060_ObjectIdentity = ObjectIdentity
panPA_5060 = _PanPA_5060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 8)
)
if mibBuilder.loadTexts:
    panPA_5060.setStatus("current")
_PanPA_5050_ObjectIdentity = ObjectIdentity
panPA_5050 = _PanPA_5050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 9)
)
if mibBuilder.loadTexts:
    panPA_5050.setStatus("current")
_PanPA_5020_ObjectIdentity = ObjectIdentity
panPA_5020 = _PanPA_5020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 11)
)
if mibBuilder.loadTexts:
    panPA_5020.setStatus("current")
_PanPA_200_ObjectIdentity = ObjectIdentity
panPA_200 = _PanPA_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 12)
)
if mibBuilder.loadTexts:
    panPA_200.setStatus("current")
_PanPA_3050_ObjectIdentity = ObjectIdentity
panPA_3050 = _PanPA_3050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 17)
)
if mibBuilder.loadTexts:
    panPA_3050.setStatus("current")
_PanPA_3020_ObjectIdentity = ObjectIdentity
panPA_3020 = _PanPA_3020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 18)
)
if mibBuilder.loadTexts:
    panPA_3020.setStatus("current")
_PanPA_3060_ObjectIdentity = ObjectIdentity
panPA_3060 = _PanPA_3060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 19)
)
if mibBuilder.loadTexts:
    panPA_3060.setStatus("current")
_PanPA_3200_ObjectIdentity = ObjectIdentity
panPA_3200 = _PanPA_3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 20)
)
if mibBuilder.loadTexts:
    panPA_3200.setStatus("current")
_PanPA_3250_ObjectIdentity = ObjectIdentity
panPA_3250 = _PanPA_3250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 21)
)
if mibBuilder.loadTexts:
    panPA_3250.setStatus("current")
_PanPA_5260_ObjectIdentity = ObjectIdentity
panPA_5260 = _PanPA_5260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 22)
)
if mibBuilder.loadTexts:
    panPA_5260.setStatus("current")
_PanPA_5250_ObjectIdentity = ObjectIdentity
panPA_5250 = _PanPA_5250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 23)
)
if mibBuilder.loadTexts:
    panPA_5250.setStatus("current")
_PanPA_5220_ObjectIdentity = ObjectIdentity
panPA_5220 = _PanPA_5220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 24)
)
if mibBuilder.loadTexts:
    panPA_5220.setStatus("current")
_PanPA_VM_ObjectIdentity = ObjectIdentity
panPA_VM = _PanPA_VM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 29)
)
if mibBuilder.loadTexts:
    panPA_VM.setStatus("current")
_PanM_100_ObjectIdentity = ObjectIdentity
panM_100 = _PanM_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30)
)
if mibBuilder.loadTexts:
    panM_100.setStatus("current")
_PanPA_7050_ObjectIdentity = ObjectIdentity
panPA_7050 = _PanPA_7050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 31)
)
if mibBuilder.loadTexts:
    panPA_7050.setStatus("current")
_PanGP_100_ObjectIdentity = ObjectIdentity
panGP_100 = _PanGP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 32)
)
if mibBuilder.loadTexts:
    panGP_100.setStatus("current")
_PanWF_500_ObjectIdentity = ObjectIdentity
panWF_500 = _PanWF_500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 33)
)
if mibBuilder.loadTexts:
    panWF_500.setStatus("current")
_PanPA_7080_ObjectIdentity = ObjectIdentity
panPA_7080 = _PanPA_7080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 34)
)
if mibBuilder.loadTexts:
    panPA_7080.setStatus("current")
_PanM_500_ObjectIdentity = ObjectIdentity
panM_500 = _PanM_500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 35)
)
if mibBuilder.loadTexts:
    panM_500.setStatus("current")
_PanPA_820_ObjectIdentity = ObjectIdentity
panPA_820 = _PanPA_820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 36)
)
if mibBuilder.loadTexts:
    panPA_820.setStatus("current")
_PanPA_850_ObjectIdentity = ObjectIdentity
panPA_850 = _PanPA_850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 37)
)
if mibBuilder.loadTexts:
    panPA_850.setStatus("current")
_PanPA_220_ObjectIdentity = ObjectIdentity
panPA_220 = _PanPA_220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 38)
)
if mibBuilder.loadTexts:
    panPA_220.setStatus("current")
_PanM_600_ObjectIdentity = ObjectIdentity
panM_600 = _PanM_600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 39)
)
if mibBuilder.loadTexts:
    panM_600.setStatus("current")
_PanM_200_ObjectIdentity = ObjectIdentity
panM_200 = _PanM_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 40)
)
if mibBuilder.loadTexts:
    panM_200.setStatus("current")
_PanPA_220R_ObjectIdentity = ObjectIdentity
panPA_220R = _PanPA_220R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 41)
)
if mibBuilder.loadTexts:
    panPA_220R.setStatus("current")
_PanPA_5280_ObjectIdentity = ObjectIdentity
panPA_5280 = _PanPA_5280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 42)
)
if mibBuilder.loadTexts:
    panPA_5280.setStatus("current")
_PanPA_3220_ObjectIdentity = ObjectIdentity
panPA_3220 = _PanPA_3220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 43)
)
if mibBuilder.loadTexts:
    panPA_3220.setStatus("current")
_PanPA_3260_ObjectIdentity = ObjectIdentity
panPA_3260 = _PanPA_3260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 44)
)
if mibBuilder.loadTexts:
    panPA_3260.setStatus("current")
_PanWF_600_ObjectIdentity = ObjectIdentity
panWF_600 = _PanWF_600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 45)
)
if mibBuilder.loadTexts:
    panWF_600.setStatus("current")
_PanProcessingCards_ObjectIdentity = ObjectIdentity
panProcessingCards = _PanProcessingCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100)
)
if mibBuilder.loadTexts:
    panProcessingCards.setStatus("current")
_PanPA_7000_SMC_ObjectIdentity = ObjectIdentity
panPA_7000_SMC = _PanPA_7000_SMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 1)
)
if mibBuilder.loadTexts:
    panPA_7000_SMC.setStatus("current")
_PanPA_7000_LPC_ObjectIdentity = ObjectIdentity
panPA_7000_LPC = _PanPA_7000_LPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 2)
)
if mibBuilder.loadTexts:
    panPA_7000_LPC.setStatus("current")
_PanPA_7000_20G_NPC_ObjectIdentity = ObjectIdentity
panPA_7000_20G_NPC = _PanPA_7000_20G_NPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 3)
)
if mibBuilder.loadTexts:
    panPA_7000_20G_NPC.setStatus("current")
_PanPA_7080_SMC_ObjectIdentity = ObjectIdentity
panPA_7080_SMC = _PanPA_7080_SMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 4)
)
if mibBuilder.loadTexts:
    panPA_7080_SMC.setStatus("current")
_PanPA_7050_SMC_B_ObjectIdentity = ObjectIdentity
panPA_7050_SMC_B = _PanPA_7050_SMC_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 5)
)
if mibBuilder.loadTexts:
    panPA_7050_SMC_B.setStatus("current")
_PanPA_7000_LFC_ObjectIdentity = ObjectIdentity
panPA_7000_LFC = _PanPA_7000_LFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 6)
)
if mibBuilder.loadTexts:
    panPA_7000_LFC.setStatus("current")
_PanPA_7000_100G_NPC_ObjectIdentity = ObjectIdentity
panPA_7000_100G_NPC = _PanPA_7000_100G_NPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 7)
)
if mibBuilder.loadTexts:
    panPA_7000_100G_NPC.setStatus("current")
_PanPA_7080_SMC_B_ObjectIdentity = ObjectIdentity
panPA_7080_SMC_B = _PanPA_7080_SMC_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 8)
)
if mibBuilder.loadTexts:
    panPA_7080_SMC_B.setStatus("current")
_PanFans_ObjectIdentity = ObjectIdentity
panFans = _PanFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 101)
)
if mibBuilder.loadTexts:
    panFans.setStatus("current")
_PanPowerSupplies_ObjectIdentity = ObjectIdentity
panPowerSupplies = _PanPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 102)
)
if mibBuilder.loadTexts:
    panPowerSupplies.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAN-PRODUCTS-MIB",
    **{"panProductsMibsModule": panProductsMibsModule,
       "panPA-4050": panPA_4050,
       "panPA-4020": panPA_4020,
       "panPA-2050": panPA_2050,
       "panPA-2020": panPA_2020,
       "panPA-4060": panPA_4060,
       "panPA-500": panPA_500,
       "panPanorama": panPanorama,
       "panPA-5060": panPA_5060,
       "panPA-5050": panPA_5050,
       "panPA-5020": panPA_5020,
       "panPA-200": panPA_200,
       "panPA-3050": panPA_3050,
       "panPA-3020": panPA_3020,
       "panPA-3060": panPA_3060,
       "panPA-3200": panPA_3200,
       "panPA-3250": panPA_3250,
       "panPA-5260": panPA_5260,
       "panPA-5250": panPA_5250,
       "panPA-5220": panPA_5220,
       "panPA-VM": panPA_VM,
       "panM-100": panM_100,
       "panPA-7050": panPA_7050,
       "panGP-100": panGP_100,
       "panWF-500": panWF_500,
       "panPA-7080": panPA_7080,
       "panM-500": panM_500,
       "panPA-820": panPA_820,
       "panPA-850": panPA_850,
       "panPA-220": panPA_220,
       "panM-600": panM_600,
       "panM-200": panM_200,
       "panPA-220R": panPA_220R,
       "panPA-5280": panPA_5280,
       "panPA-3220": panPA_3220,
       "panPA-3260": panPA_3260,
       "panWF-600": panWF_600,
       "panProcessingCards": panProcessingCards,
       "panPA-7000-SMC": panPA_7000_SMC,
       "panPA-7000-LPC": panPA_7000_LPC,
       "panPA-7000-20G-NPC": panPA_7000_20G_NPC,
       "panPA-7080-SMC": panPA_7080_SMC,
       "panPA-7050-SMC-B": panPA_7050_SMC_B,
       "panPA-7000-LFC": panPA_7000_LFC,
       "panPA-7000-100G-NPC": panPA_7000_100G_NPC,
       "panPA-7080-SMC-B": panPA_7080_SMC_B,
       "panFans": panFans,
       "panPowerSupplies": panPowerSupplies}
)
