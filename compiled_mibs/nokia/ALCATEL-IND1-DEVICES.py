# SNMP MIB module (ALCATEL-IND1-DEVICES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-DEVICES

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

(hardwareIND1Devices,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "hardwareIND1Devices")

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

alcatelIND1DevicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DevicesMIB.setRevisions(
        ("2007-04-03 00:00",
         "2019-10-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FamilyOmniSwitch7000_ObjectIdentity = ObjectIdentity
familyOmniSwitch7000 = _FamilyOmniSwitch7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    familyOmniSwitch7000.setStatus("current")
_ChassisOmniSwitch7000_ObjectIdentity = ObjectIdentity
chassisOmniSwitch7000 = _ChassisOmniSwitch7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch7000.setStatus("current")
_DeviceOmniSwitch7700_ObjectIdentity = ObjectIdentity
deviceOmniSwitch7700 = _DeviceOmniSwitch7700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch7700.setStatus("current")
_DeviceOmniSwitch7800_ObjectIdentity = ObjectIdentity
deviceOmniSwitch7800 = _DeviceOmniSwitch7800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch7800.setStatus("current")
_FansOmniSwitch7000_ObjectIdentity = ObjectIdentity
fansOmniSwitch7000 = _FansOmniSwitch7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch7000.setStatus("current")
_FansOmniSwitch7000FT_ObjectIdentity = ObjectIdentity
fansOmniSwitch7000FT = _FansOmniSwitch7000FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fansOmniSwitch7000FT.setStatus("current")
_PowersOmniSwitch7000_ObjectIdentity = ObjectIdentity
powersOmniSwitch7000 = _PowersOmniSwitch7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch7000.setStatus("current")
_PowersOmniSwitch7000PS600AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch7000PS600AC = _PowersOmniSwitch7000PS600AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch7000PS600AC.setStatus("current")
_PowersOmniSwitch7000PS600DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch7000PS600DC = _PowersOmniSwitch7000PS600DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch7000PS600DC.setStatus("current")
_PowersOmniSwitch7000PDShelf_ObjectIdentity = ObjectIdentity
powersOmniSwitch7000PDShelf = _PowersOmniSwitch7000PDShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch7000PDShelf.setStatus("current")
_PowersOmniSwitch7000PDPS600AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch7000PDPS600AC = _PowersOmniSwitch7000PDPS600AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    powersOmniSwitch7000PDPS600AC.setStatus("current")
_PowersOmniSwitch7000PDPS900DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch7000PDPS900DC = _PowersOmniSwitch7000PDPS900DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    powersOmniSwitch7000PDPS900DC.setStatus("current")
_ModulesOmniSwitch7000_ObjectIdentity = ObjectIdentity
modulesOmniSwitch7000 = _ModulesOmniSwitch7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch7000.setStatus("current")
_ModulesOmniSwitch7000CM_ObjectIdentity = ObjectIdentity
modulesOmniSwitch7000CM = _ModulesOmniSwitch7000CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch7000CM.setStatus("current")
_CmmOmniSwitch7700_ObjectIdentity = ObjectIdentity
cmmOmniSwitch7700 = _CmmOmniSwitch7700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch7700.setStatus("current")
_CmmOmniSwitch7700PROC_ObjectIdentity = ObjectIdentity
cmmOmniSwitch7700PROC = _CmmOmniSwitch7700PROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch7700PROC.setStatus("current")
_CmmOmniSwitch7700BBUS_ObjectIdentity = ObjectIdentity
cmmOmniSwitch7700BBUS = _CmmOmniSwitch7700BBUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch7700BBUS.setStatus("current")
_CmmOmniSwitch7800_ObjectIdentity = ObjectIdentity
cmmOmniSwitch7800 = _CmmOmniSwitch7800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch7800.setStatus("current")
_CmmOmniSwitch7800PROC_ObjectIdentity = ObjectIdentity
cmmOmniSwitch7800PROC = _CmmOmniSwitch7800PROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch7800PROC.setStatus("current")
_CmmOmniSwitch7800BBUS_ObjectIdentity = ObjectIdentity
cmmOmniSwitch7800BBUS = _CmmOmniSwitch7800BBUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch7800BBUS.setStatus("current")
_ModulesOmniSwitch7000NI_ObjectIdentity = ObjectIdentity
modulesOmniSwitch7000NI = _ModulesOmniSwitch7000NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch7000NI.setStatus("current")
_NiOmniSwitch7000ENI_ObjectIdentity = ObjectIdentity
niOmniSwitch7000ENI = _NiOmniSwitch7000ENI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    niOmniSwitch7000ENI.setStatus("current")
_EniOmniSwitch7000C24_ObjectIdentity = ObjectIdentity
eniOmniSwitch7000C24 = _EniOmniSwitch7000C24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eniOmniSwitch7000C24.setStatus("current")
_EniOmniSwitch7000FM12_ObjectIdentity = ObjectIdentity
eniOmniSwitch7000FM12 = _EniOmniSwitch7000FM12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    eniOmniSwitch7000FM12.setStatus("current")
_EniOmniSwitch7000PDPS24ENI_ObjectIdentity = ObjectIdentity
eniOmniSwitch7000PDPS24ENI = _EniOmniSwitch7000PDPS24ENI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    eniOmniSwitch7000PDPS24ENI.setStatus("current")
_NiOmniSwitch7000GNI_ObjectIdentity = ObjectIdentity
niOmniSwitch7000GNI = _NiOmniSwitch7000GNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    niOmniSwitch7000GNI.setStatus("current")
_GniOmniSwitch7000U2_ObjectIdentity = ObjectIdentity
gniOmniSwitch7000U2 = _GniOmniSwitch7000U2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gniOmniSwitch7000U2.setStatus("current")
_Gni2OmniSwitch7000C12_ObjectIdentity = ObjectIdentity
gni2OmniSwitch7000C12 = _Gni2OmniSwitch7000C12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gni2OmniSwitch7000C12.setStatus("current")
_Gni2OmniSwitch7000U12_ObjectIdentity = ObjectIdentity
gni2OmniSwitch7000U12 = _Gni2OmniSwitch7000U12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    gni2OmniSwitch7000U12.setStatus("current")
_NiOmniSwitch7000IC_ObjectIdentity = ObjectIdentity
niOmniSwitch7000IC = _NiOmniSwitch7000IC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    niOmniSwitch7000IC.setStatus("current")
_IcOmniSwitch7000GIC_ObjectIdentity = ObjectIdentity
icOmniSwitch7000GIC = _IcOmniSwitch7000GIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    icOmniSwitch7000GIC.setStatus("current")
_GicOmniSwitch7000LH70_ObjectIdentity = ObjectIdentity
gicOmniSwitch7000LH70 = _GicOmniSwitch7000LH70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    gicOmniSwitch7000LH70.setStatus("current")
_GicOmniSwitch7000LX_ObjectIdentity = ObjectIdentity
gicOmniSwitch7000LX = _GicOmniSwitch7000LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gicOmniSwitch7000LX.setStatus("current")
_GicOmniSwitch7000SX_ObjectIdentity = ObjectIdentity
gicOmniSwitch7000SX = _GicOmniSwitch7000SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    gicOmniSwitch7000SX.setStatus("current")
_GicOmniSwitch7000C_ObjectIdentity = ObjectIdentity
gicOmniSwitch7000C = _GicOmniSwitch7000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    gicOmniSwitch7000C.setStatus("current")
_GicOmniSwitch7000100FX_ObjectIdentity = ObjectIdentity
gicOmniSwitch7000100FX = _GicOmniSwitch7000100FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    gicOmniSwitch7000100FX.setStatus("current")
_GicOmniSwitch70001001000_ObjectIdentity = ObjectIdentity
gicOmniSwitch70001001000 = _GicOmniSwitch70001001000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3, 1, 6)
)
if mibBuilder.loadTexts:
    gicOmniSwitch70001001000.setStatus("current")
_GicOmniSwitch7000BX_ObjectIdentity = ObjectIdentity
gicOmniSwitch7000BX = _GicOmniSwitch7000BX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3, 1, 7)
)
if mibBuilder.loadTexts:
    gicOmniSwitch7000BX.setStatus("current")
_GicOmniSwitch7000101001000_ObjectIdentity = ObjectIdentity
gicOmniSwitch7000101001000 = _GicOmniSwitch7000101001000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 3, 1, 8)
)
if mibBuilder.loadTexts:
    gicOmniSwitch7000101001000.setStatus("current")
_NiOmniSwitch7000DM_ObjectIdentity = ObjectIdentity
niOmniSwitch7000DM = _NiOmniSwitch7000DM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    niOmniSwitch7000DM.setStatus("current")
_DmOmniSwitch7000Power_ObjectIdentity = ObjectIdentity
dmOmniSwitch7000Power = _DmOmniSwitch7000Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dmOmniSwitch7000Power.setStatus("current")
_DmOmniSwitch7000PowerDsine_ObjectIdentity = ObjectIdentity
dmOmniSwitch7000PowerDsine = _DmOmniSwitch7000PowerDsine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dmOmniSwitch7000PowerDsine.setStatus("current")
_NiOmniSwitch7000ANI_ObjectIdentity = ObjectIdentity
niOmniSwitch7000ANI = _NiOmniSwitch7000ANI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    niOmniSwitch7000ANI.setStatus("current")
_AniOmniSwitch7000U4_ObjectIdentity = ObjectIdentity
aniOmniSwitch7000U4 = _AniOmniSwitch7000U4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    aniOmniSwitch7000U4.setStatus("current")
_AniOmniSwitch7000U1_ObjectIdentity = ObjectIdentity
aniOmniSwitch7000U1 = _AniOmniSwitch7000U1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 1, 4, 2, 5, 2)
)
if mibBuilder.loadTexts:
    aniOmniSwitch7000U1.setStatus("current")
_FamilyOmniSwitch8000_ObjectIdentity = ObjectIdentity
familyOmniSwitch8000 = _FamilyOmniSwitch8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    familyOmniSwitch8000.setStatus("current")
_ChassisOmniSwitch8000_ObjectIdentity = ObjectIdentity
chassisOmniSwitch8000 = _ChassisOmniSwitch8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch8000.setStatus("current")
_DeviceOmniSwitch8800_ObjectIdentity = ObjectIdentity
deviceOmniSwitch8800 = _DeviceOmniSwitch8800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch8800.setStatus("current")
_FansOmniSwitch8000_ObjectIdentity = ObjectIdentity
fansOmniSwitch8000 = _FansOmniSwitch8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch8000.setStatus("current")
_FansOmniSwitch8800CFT_ObjectIdentity = ObjectIdentity
fansOmniSwitch8800CFT = _FansOmniSwitch8800CFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fansOmniSwitch8800CFT.setStatus("current")
_FansOmniSwitch8800FFT_ObjectIdentity = ObjectIdentity
fansOmniSwitch8800FFT = _FansOmniSwitch8800FFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch8800FFT.setStatus("current")
_PowersOmniSwitch8000_ObjectIdentity = ObjectIdentity
powersOmniSwitch8000 = _PowersOmniSwitch8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch8000.setStatus("current")
_PowersOmniSwitch8000PS1375AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch8000PS1375AC = _PowersOmniSwitch8000PS1375AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch8000PS1375AC.setStatus("current")
_PowersOmniSwitch8000PS1375DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch8000PS1375DC = _PowersOmniSwitch8000PS1375DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch8000PS1375DC.setStatus("current")
_ModulesOmniSwitch8000_ObjectIdentity = ObjectIdentity
modulesOmniSwitch8000 = _ModulesOmniSwitch8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch8000.setStatus("current")
_ModulesOmniSwitch8000CM_ObjectIdentity = ObjectIdentity
modulesOmniSwitch8000CM = _ModulesOmniSwitch8000CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch8000CM.setStatus("current")
_CmmOmniSwitch8800_ObjectIdentity = ObjectIdentity
cmmOmniSwitch8800 = _CmmOmniSwitch8800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch8800.setStatus("current")
_CmmOmniSwitch8800PROC_ObjectIdentity = ObjectIdentity
cmmOmniSwitch8800PROC = _CmmOmniSwitch8800PROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch8800PROC.setStatus("current")
_CmmOmniSwitch8800BBUS_ObjectIdentity = ObjectIdentity
cmmOmniSwitch8800BBUS = _CmmOmniSwitch8800BBUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch8800BBUS.setStatus("current")
_ModulesOmniSwitch8000NI_ObjectIdentity = ObjectIdentity
modulesOmniSwitch8000NI = _ModulesOmniSwitch8000NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch8000NI.setStatus("current")
_NiOmniSwitch8000ENI_ObjectIdentity = ObjectIdentity
niOmniSwitch8000ENI = _NiOmniSwitch8000ENI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    niOmniSwitch8000ENI.setStatus("current")
_EniOmniSwitch8000C24_ObjectIdentity = ObjectIdentity
eniOmniSwitch8000C24 = _EniOmniSwitch8000C24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eniOmniSwitch8000C24.setStatus("current")
_NiOmniSwitch8000GNI_ObjectIdentity = ObjectIdentity
niOmniSwitch8000GNI = _NiOmniSwitch8000GNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    niOmniSwitch8000GNI.setStatus("current")
_GniOmniSwitch8000U8_ObjectIdentity = ObjectIdentity
gniOmniSwitch8000U8 = _GniOmniSwitch8000U8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gniOmniSwitch8000U8.setStatus("current")
_GniOmniSwitch8000C8_ObjectIdentity = ObjectIdentity
gniOmniSwitch8000C8 = _GniOmniSwitch8000C8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gniOmniSwitch8000C8.setStatus("current")
_Gni2OmniSwitch8000U8_ObjectIdentity = ObjectIdentity
gni2OmniSwitch8000U8 = _Gni2OmniSwitch8000U8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    gni2OmniSwitch8000U8.setStatus("current")
_Gni2OmniSwitch8000C24_ObjectIdentity = ObjectIdentity
gni2OmniSwitch8000C24 = _Gni2OmniSwitch8000C24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    gni2OmniSwitch8000C24.setStatus("current")
_Gni2OmniSwitch8000U24_ObjectIdentity = ObjectIdentity
gni2OmniSwitch8000U24 = _Gni2OmniSwitch8000U24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 2, 5)
)
if mibBuilder.loadTexts:
    gni2OmniSwitch8000U24.setStatus("current")
_NiOmniSwitch8000G10NI_ObjectIdentity = ObjectIdentity
niOmniSwitch8000G10NI = _NiOmniSwitch8000G10NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    niOmniSwitch8000G10NI.setStatus("current")
_G10niOmniSwitch8000U1_ObjectIdentity = ObjectIdentity
g10niOmniSwitch8000U1 = _G10niOmniSwitch8000U1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    g10niOmniSwitch8000U1.setStatus("current")
_NiOmniSwitch8000IC_ObjectIdentity = ObjectIdentity
niOmniSwitch8000IC = _NiOmniSwitch8000IC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    niOmniSwitch8000IC.setStatus("current")
_IcOmniSwitch8000GIC_ObjectIdentity = ObjectIdentity
icOmniSwitch8000GIC = _IcOmniSwitch8000GIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    icOmniSwitch8000GIC.setStatus("current")
_MgicOmniSwitch8000SX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch8000SX = _MgicOmniSwitch8000SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch8000SX.setStatus("current")
_MgicOmniSwitch8000LX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch8000LX = _MgicOmniSwitch8000LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch8000LX.setStatus("current")
_MgicOmniSwitch8000LH70_ObjectIdentity = ObjectIdentity
mgicOmniSwitch8000LH70 = _MgicOmniSwitch8000LH70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch8000LH70.setStatus("current")
_MgicOmniSwitch6800LRM_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800LRM = _MgicOmniSwitch6800LRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800LRM.setStatus("current")
_MgicOmniSwitch6800SFPP_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800SFPP = _MgicOmniSwitch6800SFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800SFPP.setStatus("current")
_MgicOmniSwitch6800KF2SFPP_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800KF2SFPP = _MgicOmniSwitch6800KF2SFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800KF2SFPP.setStatus("current")
_MgicOmniSwitch6800KF2HDMI_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800KF2HDMI = _MgicOmniSwitch6800KF2HDMI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 7)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800KF2HDMI.setStatus("current")
_MgicOmniSwitch6800SFPPSR_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800SFPPSR = _MgicOmniSwitch6800SFPPSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 8)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800SFPPSR.setStatus("current")
_MgicOmniSwitch6800SFPPLR_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800SFPPLR = _MgicOmniSwitch6800SFPPLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 9)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800SFPPLR.setStatus("current")
_MgicOmniSwitch6800SFPPER_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800SFPPER = _MgicOmniSwitch6800SFPPER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 10)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800SFPPER.setStatus("current")
_MgicOmniSwitch6800SFPPLRM_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800SFPPLRM = _MgicOmniSwitch6800SFPPLRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 11)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800SFPPLRM.setStatus("current")
_MgicOmniSwitch6800XFPSR_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800XFPSR = _MgicOmniSwitch6800XFPSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 12)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800XFPSR.setStatus("current")
_MgicOmniSwitch6800T_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800T = _MgicOmniSwitch6800T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800T.setStatus("current")
_ModulesOmniSwitch8000SF_ObjectIdentity = ObjectIdentity
modulesOmniSwitch8000SF = _ModulesOmniSwitch8000SF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch8000SF.setStatus("current")
_SfOmniSwitch8800SFM_ObjectIdentity = ObjectIdentity
sfOmniSwitch8800SFM = _SfOmniSwitch8800SFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    sfOmniSwitch8800SFM.setStatus("current")
_FamilyOmniSwitch6600_ObjectIdentity = ObjectIdentity
familyOmniSwitch6600 = _FamilyOmniSwitch6600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6600.setStatus("current")
_ChassisOmniSwitch6600_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6600 = _ChassisOmniSwitch6600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6600.setStatus("current")
_DeviceOmniSwitch6624_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6624 = _DeviceOmniSwitch6624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6624.setStatus("current")
_DeviceOmniSwitch6648_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6648 = _DeviceOmniSwitch6648_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6648.setStatus("current")
_DeviceOmniSwitch6624Fiber_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6624Fiber = _DeviceOmniSwitch6624Fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6624Fiber.setStatus("current")
_DeviceOmniSwitch660224_ObjectIdentity = ObjectIdentity
deviceOmniSwitch660224 = _DeviceOmniSwitch660224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch660224.setStatus("current")
_DeviceOmniSwitch660248_ObjectIdentity = ObjectIdentity
deviceOmniSwitch660248 = _DeviceOmniSwitch660248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch660248.setStatus("current")
_DeviceOmniSwitch6624PoE_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6624PoE = _DeviceOmniSwitch6624PoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6624PoE.setStatus("current")
_DeviceOmniSwitch6648PoE_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6648PoE = _DeviceOmniSwitch6648PoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6648PoE.setStatus("current")
_FansOmniSwitch6600_ObjectIdentity = ObjectIdentity
fansOmniSwitch6600 = _FansOmniSwitch6600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6600.setStatus("current")
_PowersOmniSwitch6600_ObjectIdentity = ObjectIdentity
powersOmniSwitch6600 = _PowersOmniSwitch6600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6600.setStatus("current")
_PowersOmniSwitch6600BSP_ObjectIdentity = ObjectIdentity
powersOmniSwitch6600BSP = _PowersOmniSwitch6600BSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6600BSP.setStatus("current")
_ModulesOmniSwitch6600_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6600 = _ModulesOmniSwitch6600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6600.setStatus("current")
_ExpOmniSwitch6600_ObjectIdentity = ObjectIdentity
expOmniSwitch6600 = _ExpOmniSwitch6600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    expOmniSwitch6600.setStatus("current")
_MgicOmniSwitch66002_ObjectIdentity = ObjectIdentity
mgicOmniSwitch66002 = _MgicOmniSwitch66002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch66002.setStatus("current")
_GsmOmniSwitch6600T2_ObjectIdentity = ObjectIdentity
gsmOmniSwitch6600T2 = _GsmOmniSwitch6600T2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    gsmOmniSwitch6600T2.setStatus("current")
_StkOmniSwitch6600Kit_ObjectIdentity = ObjectIdentity
stkOmniSwitch6600Kit = _StkOmniSwitch6600Kit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    stkOmniSwitch6600Kit.setStatus("current")
_IcOmniSwitch6600GIC_ObjectIdentity = ObjectIdentity
icOmniSwitch6600GIC = _IcOmniSwitch6600GIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    icOmniSwitch6600GIC.setStatus("current")
_MgicOmniSwitch6600SX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6600SX = _MgicOmniSwitch6600SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6600SX.setStatus("current")
_MgicOmniSwitch6600LX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6600LX = _MgicOmniSwitch6600LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6600LX.setStatus("current")
_MgicOmniSwitch6600LH70_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6600LH70 = _MgicOmniSwitch6600LH70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 3, 4, 2, 3)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6600LH70.setStatus("current")
_FamilyOmniAccess200_ObjectIdentity = ObjectIdentity
familyOmniAccess200 = _FamilyOmniAccess200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    familyOmniAccess200.setStatus("current")
_ChassisOmniAccess200_ObjectIdentity = ObjectIdentity
chassisOmniAccess200 = _ChassisOmniAccess200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccess200.setStatus("current")
_DeviceOmniAccess210_ObjectIdentity = ObjectIdentity
deviceOmniAccess210 = _DeviceOmniAccess210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccess210.setStatus("current")
_DeviceOmniAccess250_ObjectIdentity = ObjectIdentity
deviceOmniAccess250 = _DeviceOmniAccess250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniAccess250.setStatus("current")
_FansOmniSwitch200_ObjectIdentity = ObjectIdentity
fansOmniSwitch200 = _FansOmniSwitch200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch200.setStatus("current")
_PowersOmniAccess200_ObjectIdentity = ObjectIdentity
powersOmniAccess200 = _PowersOmniAccess200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    powersOmniAccess200.setStatus("current")
_ModulesOmniAccess200_ObjectIdentity = ObjectIdentity
modulesOmniAccess200 = _ModulesOmniAccess200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    modulesOmniAccess200.setStatus("current")
_FamilyOmniStack6300_ObjectIdentity = ObjectIdentity
familyOmniStack6300 = _FamilyOmniStack6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    familyOmniStack6300.setStatus("current")
_ChassisOmniStack6300_ObjectIdentity = ObjectIdentity
chassisOmniStack6300 = _ChassisOmniStack6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    chassisOmniStack6300.setStatus("current")
_DeviceOmniStack6324_ObjectIdentity = ObjectIdentity
deviceOmniStack6324 = _DeviceOmniStack6324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniStack6324.setStatus("current")
_FansOmniStack6300_ObjectIdentity = ObjectIdentity
fansOmniStack6300 = _FansOmniStack6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    fansOmniStack6300.setStatus("current")
_PowersOmniStack6300_ObjectIdentity = ObjectIdentity
powersOmniStack6300 = _PowersOmniStack6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    powersOmniStack6300.setStatus("current")
_ModulesOmniStack6300_ObjectIdentity = ObjectIdentity
modulesOmniStack6300 = _ModulesOmniStack6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    modulesOmniStack6300.setStatus("current")
_FamilyOmniSwitch6800_ObjectIdentity = ObjectIdentity
familyOmniSwitch6800 = _FamilyOmniSwitch6800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6800.setStatus("current")
_ChassisOmniSwitch6800_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6800 = _ChassisOmniSwitch6800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6800.setStatus("current")
_DeviceOmniSwitch6824_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6824 = _DeviceOmniSwitch6824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6824.setStatus("current")
_DeviceOmniSwitch6848_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6848 = _DeviceOmniSwitch6848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6848.setStatus("current")
_DeviceOmniSwitch6824Fiber_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6824Fiber = _DeviceOmniSwitch6824Fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6824Fiber.setStatus("current")
_DeviceOmniSwitch6824PoE_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6824PoE = _DeviceOmniSwitch6824PoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6824PoE.setStatus("current")
_DeviceOmniSwitch6848PoE_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6848PoE = _DeviceOmniSwitch6848PoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6848PoE.setStatus("current")
_DeviceOmniSwitch6824L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6824L = _DeviceOmniSwitch6824L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6824L.setStatus("current")
_DeviceOmniSwitch6848L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6848L = _DeviceOmniSwitch6848L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 7)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6848L.setStatus("current")
_DeviceOmniSwitch6824LU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6824LU = _DeviceOmniSwitch6824LU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 8)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6824LU.setStatus("current")
_DeviceOmniSwitch6848LU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6848LU = _DeviceOmniSwitch6848LU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 9)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6848LU.setStatus("current")
_DeviceOmniSwitch6824LPoE_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6824LPoE = _DeviceOmniSwitch6824LPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 10)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6824LPoE.setStatus("current")
_DeviceOmniSwitch6848LPoE_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6848LPoE = _DeviceOmniSwitch6848LPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 11)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6848LPoE.setStatus("current")
_DeviceOmniSwitch6824LUPoE_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6824LUPoE = _DeviceOmniSwitch6824LUPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 12)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6824LUPoE.setStatus("current")
_DeviceOmniSwitch6848LUPoE_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6848LUPoE = _DeviceOmniSwitch6848LUPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 1, 13)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6848LUPoE.setStatus("current")
_FansOmniSwitch6800_ObjectIdentity = ObjectIdentity
fansOmniSwitch6800 = _FansOmniSwitch6800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6800.setStatus("current")
_PowersOmniSwitch6800_ObjectIdentity = ObjectIdentity
powersOmniSwitch6800 = _PowersOmniSwitch6800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6800.setStatus("current")
_PowersOmniSwitch6800BPS_ObjectIdentity = ObjectIdentity
powersOmniSwitch6800BPS = _PowersOmniSwitch6800BPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6800BPS.setStatus("current")
_PowersOmniSwitch6800MOD_ObjectIdentity = ObjectIdentity
powersOmniSwitch6800MOD = _PowersOmniSwitch6800MOD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6800MOD.setStatus("current")
_PowersOmniSwitch6800SHLF_ObjectIdentity = ObjectIdentity
powersOmniSwitch6800SHLF = _PowersOmniSwitch6800SHLF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6800SHLF.setStatus("current")
_ModulesOmniSwitch6800_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6800 = _ModulesOmniSwitch6800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6800.setStatus("current")
_IcOmniSwitch8000TenGIC_ObjectIdentity = ObjectIdentity
icOmniSwitch8000TenGIC = _IcOmniSwitch8000TenGIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    icOmniSwitch8000TenGIC.setStatus("current")
_MgicOmniSwitch6800SR_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800SR = _MgicOmniSwitch6800SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800SR.setStatus("current")
_MgicOmniSwitch6800LR_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800LR = _MgicOmniSwitch6800LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800LR.setStatus("current")
_IcOmniSwitch6800GIC_ObjectIdentity = ObjectIdentity
icOmniSwitch6800GIC = _IcOmniSwitch6800GIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    icOmniSwitch6800GIC.setStatus("current")
_MgicOmniSwitch6800SX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800SX = _MgicOmniSwitch6800SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800SX.setStatus("current")
_MgicOmniSwitch6800LX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800LX = _MgicOmniSwitch6800LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4, 2, 2)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800LX.setStatus("current")
_MgicOmniSwitch6800LH70_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6800LH70 = _MgicOmniSwitch6800LH70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4, 2, 3)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6800LH70.setStatus("current")
_ExpOmniSwitch6800_ObjectIdentity = ObjectIdentity
expOmniSwitch6800 = _ExpOmniSwitch6800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4, 3)
)
if mibBuilder.loadTexts:
    expOmniSwitch6800.setStatus("current")
_ExpOmniSwitch6800U2_ObjectIdentity = ObjectIdentity
expOmniSwitch6800U2 = _ExpOmniSwitch6800U2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    expOmniSwitch6800U2.setStatus("current")
_FamilyOmniSwitch6850_ObjectIdentity = ObjectIdentity
familyOmniSwitch6850 = _FamilyOmniSwitch6850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6850.setStatus("current")
_ChassisOmniSwitch6850_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6850 = _ChassisOmniSwitch6850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6850.setStatus("current")
_DeviceOmniSwitch685024_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685024 = _DeviceOmniSwitch685024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685024.setStatus("current")
_DeviceOmniSwitch685048_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685048 = _DeviceOmniSwitch685048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685048.setStatus("current")
_DeviceOmniSwitch685024X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685024X = _DeviceOmniSwitch685024X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685024X.setStatus("current")
_DeviceOmniSwitch685048X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685048X = _DeviceOmniSwitch685048X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685048X.setStatus("current")
_DeviceOmniSwitch6850P24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P24 = _DeviceOmniSwitch6850P24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P24.setStatus("current")
_DeviceOmniSwitch6850P48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P48 = _DeviceOmniSwitch6850P48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P48.setStatus("current")
_DeviceOmniSwitch6850P24X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P24X = _DeviceOmniSwitch6850P24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 7)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P24X.setStatus("current")
_DeviceOmniSwitch6850P48X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P48X = _DeviceOmniSwitch6850P48X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 8)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P48X.setStatus("current")
_DeviceOmniSwitch6850U24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850U24 = _DeviceOmniSwitch6850U24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 9)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850U24.setStatus("current")
_DeviceOmniSwitch6850U24X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850U24X = _DeviceOmniSwitch6850U24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 10)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850U24X.setStatus("current")
_DeviceOmniSwitch685024L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685024L = _DeviceOmniSwitch685024L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 11)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685024L.setStatus("current")
_DeviceOmniSwitch685048L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685048L = _DeviceOmniSwitch685048L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 12)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685048L.setStatus("current")
_DeviceOmniSwitch685024XL_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685024XL = _DeviceOmniSwitch685024XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 13)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685024XL.setStatus("current")
_DeviceOmniSwitch685048XL_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685048XL = _DeviceOmniSwitch685048XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 14)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685048XL.setStatus("current")
_DeviceOmniSwitch6850P24L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P24L = _DeviceOmniSwitch6850P24L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 15)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P24L.setStatus("current")
_DeviceOmniSwitch6850P48L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P48L = _DeviceOmniSwitch6850P48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 16)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P48L.setStatus("current")
_DeviceOmniSwitch6850P24XL_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P24XL = _DeviceOmniSwitch6850P24XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 17)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P24XL.setStatus("current")
_DeviceOmniSwitch6850P48XL_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P48XL = _DeviceOmniSwitch6850P48XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 18)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P48XL.setStatus("current")
_DeviceOmniSwitch685024LU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685024LU = _DeviceOmniSwitch685024LU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 19)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685024LU.setStatus("current")
_DeviceOmniSwitch685048LU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685048LU = _DeviceOmniSwitch685048LU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 20)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685048LU.setStatus("current")
_DeviceOmniSwitch685024XLU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685024XLU = _DeviceOmniSwitch685024XLU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 21)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685024XLU.setStatus("current")
_DeviceOmniSwitch685048XLU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685048XLU = _DeviceOmniSwitch685048XLU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 22)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685048XLU.setStatus("current")
_DeviceOmniSwitch6850P24LU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P24LU = _DeviceOmniSwitch6850P24LU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 23)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P24LU.setStatus("current")
_DeviceOmniSwitch6850P48LU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P48LU = _DeviceOmniSwitch6850P48LU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 24)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P48LU.setStatus("current")
_DeviceOmniSwitch6850P24XLU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P24XLU = _DeviceOmniSwitch6850P24XLU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 25)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P24XLU.setStatus("current")
_DeviceOmniSwitch6850P48XLU_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850P48XLU = _DeviceOmniSwitch6850P48XLU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 26)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850P48XLU.setStatus("current")
_DeviceOmniSwitch6850EP48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850EP48 = _DeviceOmniSwitch6850EP48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 40)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850EP48.setStatus("current")
_DeviceOmniSwitch6850EP48X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850EP48X = _DeviceOmniSwitch6850EP48X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 41)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850EP48X.setStatus("current")
_DeviceOmniSwitch6850EP24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850EP24 = _DeviceOmniSwitch6850EP24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 42)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850EP24.setStatus("current")
_DeviceOmniSwitch6850EP24X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850EP24X = _DeviceOmniSwitch6850EP24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 43)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850EP24X.setStatus("current")
_DeviceOmniSwitch6850E48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850E48 = _DeviceOmniSwitch6850E48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 44)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850E48.setStatus("current")
_DeviceOmniSwitch6850E48X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850E48X = _DeviceOmniSwitch6850E48X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 45)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850E48X.setStatus("current")
_DeviceOmniSwitch6850E24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850E24 = _DeviceOmniSwitch6850E24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 46)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850E24.setStatus("current")
_DeviceOmniSwitch6850E24X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850E24X = _DeviceOmniSwitch6850E24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 47)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850E24X.setStatus("current")
_DeviceOmniSwitch6850EU24X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6850EU24X = _DeviceOmniSwitch6850EU24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 1, 48)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6850EU24X.setStatus("current")
_FansOmniSwitch6850_ObjectIdentity = ObjectIdentity
fansOmniSwitch6850 = _FansOmniSwitch6850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6850.setStatus("current")
_PowersOmniSwitch6850_ObjectIdentity = ObjectIdentity
powersOmniSwitch6850 = _PowersOmniSwitch6850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6850.setStatus("current")
_PowersOmniSwitch6850BPS_ObjectIdentity = ObjectIdentity
powersOmniSwitch6850BPS = _PowersOmniSwitch6850BPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6850BPS.setStatus("current")
_PowersOmniSwitch120DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch120DC = _PowersOmniSwitch120DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch120DC.setStatus("current")
_PowersOmniSwitch126AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch126AC = _PowersOmniSwitch126AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch126AC.setStatus("current")
_PowersOmniSwitch360AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch360AC = _PowersOmniSwitch360AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 3, 4)
)
if mibBuilder.loadTexts:
    powersOmniSwitch360AC.setStatus("current")
_PowersOmniSwitch510AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch510AC = _PowersOmniSwitch510AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 3, 5)
)
if mibBuilder.loadTexts:
    powersOmniSwitch510AC.setStatus("current")
_PowersOmniSwitch900AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch900AC = _PowersOmniSwitch900AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 3, 6)
)
if mibBuilder.loadTexts:
    powersOmniSwitch900AC.setStatus("current")
_PowersOmniSwitchOsBPS_ObjectIdentity = ObjectIdentity
powersOmniSwitchOsBPS = _PowersOmniSwitchOsBPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 3, 7)
)
if mibBuilder.loadTexts:
    powersOmniSwitchOsBPS.setStatus("current")
_ModulesOmniSwitch6850_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6850 = _ModulesOmniSwitch6850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6850.setStatus("current")
_DaughterBoardOmniSwitch6850_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6850 = _DaughterBoardOmniSwitch6850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6850.setStatus("current")
_DaughterBoardOmniSwitch6850ESFPplus_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6850ESFPplus = _DaughterBoardOmniSwitch6850ESFPplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 7, 5, 1)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6850ESFPplus.setStatus("current")
_FamilyOmniSwitch9000_ObjectIdentity = ObjectIdentity
familyOmniSwitch9000 = _FamilyOmniSwitch9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    familyOmniSwitch9000.setStatus("current")
_ChassisOmniSwitch9000_ObjectIdentity = ObjectIdentity
chassisOmniSwitch9000 = _ChassisOmniSwitch9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch9000.setStatus("current")
_DeviceOmniSwitch9700_ObjectIdentity = ObjectIdentity
deviceOmniSwitch9700 = _DeviceOmniSwitch9700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch9700.setStatus("current")
_DeviceOmniSwitch9800_ObjectIdentity = ObjectIdentity
deviceOmniSwitch9800 = _DeviceOmniSwitch9800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch9800.setStatus("current")
_DeviceOmniSwitch9600_ObjectIdentity = ObjectIdentity
deviceOmniSwitch9600 = _DeviceOmniSwitch9600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch9600.setStatus("current")
_DeviceOmniSwitch9700E_ObjectIdentity = ObjectIdentity
deviceOmniSwitch9700E = _DeviceOmniSwitch9700E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch9700E.setStatus("current")
_DeviceOmniSwitch9800E_ObjectIdentity = ObjectIdentity
deviceOmniSwitch9800E = _DeviceOmniSwitch9800E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch9800E.setStatus("current")
_DeviceOmniSwitch9600E_ObjectIdentity = ObjectIdentity
deviceOmniSwitch9600E = _DeviceOmniSwitch9600E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch9600E.setStatus("current")
_FansOmniSwitch9000_ObjectIdentity = ObjectIdentity
fansOmniSwitch9000 = _FansOmniSwitch9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch9000.setStatus("current")
_PowersOmniSwitch9000_ObjectIdentity = ObjectIdentity
powersOmniSwitch9000 = _PowersOmniSwitch9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch9000.setStatus("current")
_ModulesOmniSwitch9000_ObjectIdentity = ObjectIdentity
modulesOmniSwitch9000 = _ModulesOmniSwitch9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch9000.setStatus("current")
_ModulesOmniSwitch9000CM_ObjectIdentity = ObjectIdentity
modulesOmniSwitch9000CM = _ModulesOmniSwitch9000CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch9000CM.setStatus("current")
_CmmOmniSwitch9700_ObjectIdentity = ObjectIdentity
cmmOmniSwitch9700 = _CmmOmniSwitch9700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch9700.setStatus("current")
_CmmOmniSwitch9700PROC_ObjectIdentity = ObjectIdentity
cmmOmniSwitch9700PROC = _CmmOmniSwitch9700PROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch9700PROC.setStatus("current")
_CmmOmniSwitch9800_ObjectIdentity = ObjectIdentity
cmmOmniSwitch9800 = _CmmOmniSwitch9800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch9800.setStatus("current")
_CmmOmniSwitch9800PROC_ObjectIdentity = ObjectIdentity
cmmOmniSwitch9800PROC = _CmmOmniSwitch9800PROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch9800PROC.setStatus("current")
_CmmOmniSwitch9600_ObjectIdentity = ObjectIdentity
cmmOmniSwitch9600 = _CmmOmniSwitch9600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 1, 3)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch9600.setStatus("current")
_CmmOmniSwitch9600PROC_ObjectIdentity = ObjectIdentity
cmmOmniSwitch9600PROC = _CmmOmniSwitch9600PROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch9600PROC.setStatus("current")
_ModulesOmniSwitch9000NI_ObjectIdentity = ObjectIdentity
modulesOmniSwitch9000NI = _ModulesOmniSwitch9000NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch9000NI.setStatus("current")
_NiOmniSwitch9000ENI_ObjectIdentity = ObjectIdentity
niOmniSwitch9000ENI = _NiOmniSwitch9000ENI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 1)
)
if mibBuilder.loadTexts:
    niOmniSwitch9000ENI.setStatus("current")
_NiOmniSwitch9000GNI_ObjectIdentity = ObjectIdentity
niOmniSwitch9000GNI = _NiOmniSwitch9000GNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2)
)
if mibBuilder.loadTexts:
    niOmniSwitch9000GNI.setStatus("current")
_GniOmniSwitch9000C24_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000C24 = _GniOmniSwitch9000C24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000C24.setStatus("current")
_GniOmniSwitch9000U24_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000U24 = _GniOmniSwitch9000U24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000U24.setStatus("current")
_GniOmniSwitch9000U2_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000U2 = _GniOmniSwitch9000U2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000U2.setStatus("current")
_GniOmniSwitch9000U6_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000U6 = _GniOmniSwitch9000U6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000U6.setStatus("current")
_GniOmniSwitch9000P24_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000P24 = _GniOmniSwitch9000P24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 5)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000P24.setStatus("current")
_GniOmniSwitch900048T_ObjectIdentity = ObjectIdentity
gniOmniSwitch900048T = _GniOmniSwitch900048T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 6)
)
if mibBuilder.loadTexts:
    gniOmniSwitch900048T.setStatus("current")
_GniOmniSwitch9000GC20L_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000GC20L = _GniOmniSwitch9000GC20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 7)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000GC20L.setStatus("current")
_GniOmniSwitch9000EC20L_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000EC20L = _GniOmniSwitch9000EC20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 8)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000EC20L.setStatus("current")
_GniOmniSwitchLockedC20L_ObjectIdentity = ObjectIdentity
gniOmniSwitchLockedC20L = _GniOmniSwitchLockedC20L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 9)
)
if mibBuilder.loadTexts:
    gniOmniSwitchLockedC20L.setStatus("current")
_GniOmniSwitch900048TE_ObjectIdentity = ObjectIdentity
gniOmniSwitch900048TE = _GniOmniSwitch900048TE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    gniOmniSwitch900048TE.setStatus("current")
_GniOmniSwitch9000EC20LE_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000EC20LE = _GniOmniSwitch9000EC20LE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 11)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000EC20LE.setStatus("current")
_GniOmniSwitchLockedC20LE_ObjectIdentity = ObjectIdentity
gniOmniSwitchLockedC20LE = _GniOmniSwitchLockedC20LE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 12)
)
if mibBuilder.loadTexts:
    gniOmniSwitchLockedC20LE.setStatus("current")
_GniOmniSwitch9000C24E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000C24E = _GniOmniSwitch9000C24E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 13)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000C24E.setStatus("current")
_GniOmniSwitch9000P24E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000P24E = _GniOmniSwitch9000P24E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 14)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000P24E.setStatus("current")
_GniOmniSwitch9000U24E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000U24E = _GniOmniSwitch9000U24E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 15)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000U24E.setStatus("current")
_GniOmniSwitch9000GC20LE_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000GC20LE = _GniOmniSwitch9000GC20LE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 16)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000GC20LE.setStatus("current")
_GniOmniSwitch9000U2E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000U2E = _GniOmniSwitch9000U2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 17)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000U2E.setStatus("current")
_GniOmniSwitch9000U6E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000U6E = _GniOmniSwitch9000U6E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 18)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000U6E.setStatus("current")
_GniOmniSwitch9000C24FJ2E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000C24FJ2E = _GniOmniSwitch9000C24FJ2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 19)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000C24FJ2E.setStatus("current")
_GniOmniSwitch9000U24FJ2E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000U24FJ2E = _GniOmniSwitch9000U24FJ2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 20)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000U24FJ2E.setStatus("current")
_GniOmniSwitch9000U2FJ2E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000U2FJ2E = _GniOmniSwitch9000U2FJ2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 21)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000U2FJ2E.setStatus("current")
_GniOmniSwitch9000U12PlusFJ2E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000U12PlusFJ2E = _GniOmniSwitch9000U12PlusFJ2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 22)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000U12PlusFJ2E.setStatus("current")
_GniOmniSwitch9000P24FJ2E_ObjectIdentity = ObjectIdentity
gniOmniSwitch9000P24FJ2E = _GniOmniSwitch9000P24FJ2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 2, 25)
)
if mibBuilder.loadTexts:
    gniOmniSwitch9000P24FJ2E.setStatus("current")
_NiOmniSwitch9000IC_ObjectIdentity = ObjectIdentity
niOmniSwitch9000IC = _NiOmniSwitch9000IC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 3)
)
if mibBuilder.loadTexts:
    niOmniSwitch9000IC.setStatus("current")
_NiOmniSwitch9000DM_ObjectIdentity = ObjectIdentity
niOmniSwitch9000DM = _NiOmniSwitch9000DM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 8, 4, 2, 4)
)
if mibBuilder.loadTexts:
    niOmniSwitch9000DM.setStatus("current")
_FamilyOmniSwitch6855_ObjectIdentity = ObjectIdentity
familyOmniSwitch6855 = _FamilyOmniSwitch6855_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6855.setStatus("current")
_ChassisOmniSwitch6855_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6855 = _ChassisOmniSwitch6855_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6855.setStatus("current")
_DeviceOmniSwitch685514_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685514 = _DeviceOmniSwitch685514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685514.setStatus("current")
_DeviceOmniSwitch6855U10_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6855U10 = _DeviceOmniSwitch6855U10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6855U10.setStatus("current")
_DeviceOmniSwitch685524_ObjectIdentity = ObjectIdentity
deviceOmniSwitch685524 = _DeviceOmniSwitch685524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch685524.setStatus("current")
_DeviceOmniSwitch6855U24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6855U24 = _DeviceOmniSwitch6855U24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6855U24.setStatus("current")
_DeviceOmniSwitch6855U24X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6855U24X = _DeviceOmniSwitch6855U24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6855U24X.setStatus("current")
_DeviceOmniSwitch6855P14_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6855P14 = _DeviceOmniSwitch6855P14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6855P14.setStatus("current")
_FansOmniSwitch6855_ObjectIdentity = ObjectIdentity
fansOmniSwitch6855 = _FansOmniSwitch6855_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6855.setStatus("current")
_PowersOmniSwitch6855_ObjectIdentity = ObjectIdentity
powersOmniSwitch6855 = _PowersOmniSwitch6855_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6855.setStatus("current")
_PowersOmniSwitch6855Devices40DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6855Devices40DC = _PowersOmniSwitch6855Devices40DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6855Devices40DC.setStatus("current")
_PowersOmniSwitch6855Devices62DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6855Devices62DC = _PowersOmniSwitch6855Devices62DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6855Devices62DC.setStatus("current")
_PowersOmniSwitch6855Devices180DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6855Devices180DC = _PowersOmniSwitch6855Devices180DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6855Devices180DC.setStatus("current")
_ModulesOmniSwitch6855_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6855 = _ModulesOmniSwitch6855_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 9, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6855.setStatus("current")
_FamilyOmniSwitch6400_ObjectIdentity = ObjectIdentity
familyOmniSwitch6400 = _FamilyOmniSwitch6400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6400.setStatus("current")
_ChassisOmniSwitch6400_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6400 = _ChassisOmniSwitch6400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6400.setStatus("current")
_DeviceOmniSwitch640024_ObjectIdentity = ObjectIdentity
deviceOmniSwitch640024 = _DeviceOmniSwitch640024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch640024.setStatus("current")
_DeviceOmniSwitch6400P24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6400P24 = _DeviceOmniSwitch6400P24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6400P24.setStatus("current")
_DeviceOmniSwitch6400U24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6400U24 = _DeviceOmniSwitch6400U24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6400U24.setStatus("current")
_DeviceOmniSwitch6400DU24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6400DU24 = _DeviceOmniSwitch6400DU24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6400DU24.setStatus("current")
_DeviceOmniSwitch640048_ObjectIdentity = ObjectIdentity
deviceOmniSwitch640048 = _DeviceOmniSwitch640048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch640048.setStatus("current")
_DeviceOmniSwitch6400P48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6400P48 = _DeviceOmniSwitch6400P48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6400P48.setStatus("current")
_FansOmniSwitch6400_ObjectIdentity = ObjectIdentity
fansOmniSwitch6400 = _FansOmniSwitch6400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6400.setStatus("current")
_PowersOmniSwitch6400_ObjectIdentity = ObjectIdentity
powersOmniSwitch6400 = _PowersOmniSwitch6400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6400.setStatus("current")
_PowersOmniSwitch6400BPS_ObjectIdentity = ObjectIdentity
powersOmniSwitch6400BPS = _PowersOmniSwitch6400BPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6400BPS.setStatus("current")
_ModulesOmniSwitch6400_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6400 = _ModulesOmniSwitch6400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 10, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6400.setStatus("current")
_FamilyOmniSwitch6250_ObjectIdentity = ObjectIdentity
familyOmniSwitch6250 = _FamilyOmniSwitch6250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6250.setStatus("current")
_ChassisOmniSwitch6250M_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6250M = _ChassisOmniSwitch6250M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6250M.setStatus("current")
_DeviceOmniSwitch62508M_ObjectIdentity = ObjectIdentity
deviceOmniSwitch62508M = _DeviceOmniSwitch62508M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch62508M.setStatus("current")
_DeviceOmniSwitch625024M_ObjectIdentity = ObjectIdentity
deviceOmniSwitch625024M = _DeviceOmniSwitch625024M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch625024M.setStatus("current")
_DeviceOmniSwitch625024MD_ObjectIdentity = ObjectIdentity
deviceOmniSwitch625024MD = _DeviceOmniSwitch625024MD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch625024MD.setStatus("current")
_DeviceOmniSwitch6250U24M_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6250U24M = _DeviceOmniSwitch6250U24M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6250U24M.setStatus("current")
_ChassisOmniSwitch6250ENT_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6250ENT = _ChassisOmniSwitch6250ENT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6250ENT.setStatus("current")
_DeviceOmniSwitch625024ENT_ObjectIdentity = ObjectIdentity
deviceOmniSwitch625024ENT = _DeviceOmniSwitch625024ENT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch625024ENT.setStatus("current")
_DeviceOmniSwitch6250P24ENT_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6250P24ENT = _DeviceOmniSwitch6250P24ENT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6250P24ENT.setStatus("current")
_FansOmniSwitch6250_ObjectIdentity = ObjectIdentity
fansOmniSwitch6250 = _FansOmniSwitch6250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 3)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6250.setStatus("current")
_PowersOmniSwitch6250_ObjectIdentity = ObjectIdentity
powersOmniSwitch6250 = _PowersOmniSwitch6250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 4)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6250.setStatus("current")
_PowersOmniSwitch6250BPS_ObjectIdentity = ObjectIdentity
powersOmniSwitch6250BPS = _PowersOmniSwitch6250BPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 4, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6250BPS.setStatus("current")
_ModulesOmniSwitch6250_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6250 = _ModulesOmniSwitch6250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 11, 5)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6250.setStatus("current")
_FamilyOmniSwitch6450_ObjectIdentity = ObjectIdentity
familyOmniSwitch6450 = _FamilyOmniSwitch6450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6450.setStatus("current")
_ChassisOmniSwitch6450_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6450 = _ChassisOmniSwitch6450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6450.setStatus("current")
_DeviceOmniSwitch6450C10_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C10 = _DeviceOmniSwitch6450C10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C10.setStatus("current")
_DeviceOmniSwitch6450P10_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450P10 = _DeviceOmniSwitch6450P10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450P10.setStatus("current")
_DeviceOmniSwitch6450C10L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C10L = _DeviceOmniSwitch6450C10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C10L.setStatus("current")
_DeviceOmniSwitch6450P10L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450P10L = _DeviceOmniSwitch6450P10L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450P10L.setStatus("current")
_DeviceOmniSwitch6450C24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C24 = _DeviceOmniSwitch6450C24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C24.setStatus("current")
_DeviceOmniSwitch6450P24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450P24 = _DeviceOmniSwitch6450P24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450P24.setStatus("current")
_DeviceOmniSwitch6450U24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450U24 = _DeviceOmniSwitch6450U24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 7)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450U24.setStatus("current")
_DeviceOmniSwitch6450C48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C48 = _DeviceOmniSwitch6450C48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 8)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C48.setStatus("current")
_DeviceOmniSwitch6450P48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450P48 = _DeviceOmniSwitch6450P48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 9)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450P48.setStatus("current")
_DeviceOmniSwitch6450C24L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C24L = _DeviceOmniSwitch6450C24L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 10)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C24L.setStatus("current")
_DeviceOmniSwitch6450P24L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450P24L = _DeviceOmniSwitch6450P24L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 11)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450P24L.setStatus("current")
_DeviceOmniSwitch6450C48L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C48L = _DeviceOmniSwitch6450C48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 12)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C48L.setStatus("current")
_DeviceOmniSwitch6450P48L_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450P48L = _DeviceOmniSwitch6450P48L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 13)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450P48L.setStatus("current")
_DeviceOmniSwitch6450P10S_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450P10S = _DeviceOmniSwitch6450P10S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 14)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450P10S.setStatus("current")
_DeviceOmniSwitch6450U24S_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450U24S = _DeviceOmniSwitch6450U24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 15)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450U24S.setStatus("current")
_DeviceOmniSwitch6450C10M_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C10M = _DeviceOmniSwitch6450C10M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 16)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C10M.setStatus("current")
_DeviceOmniSwitch6450C24XM_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C24XM = _DeviceOmniSwitch6450C24XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 17)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C24XM.setStatus("current")
_DeviceOmniSwitch6450C24X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C24X = _DeviceOmniSwitch6450C24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 18)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C24X.setStatus("current")
_DeviceOmniSwitch6450P24X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450P24X = _DeviceOmniSwitch6450P24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 19)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450P24X.setStatus("current")
_DeviceOmniSwitch6450C48X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450C48X = _DeviceOmniSwitch6450C48X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 20)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450C48X.setStatus("current")
_DeviceOmniSwitch6450P48X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450P48X = _DeviceOmniSwitch6450P48X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 21)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450P48X.setStatus("current")
_DeviceOmniSwitch6450U24SXM_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450U24SXM = _DeviceOmniSwitch6450U24SXM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 22)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450U24SXM.setStatus("current")
_DeviceOmniSwitch6450U24X_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6450U24X = _DeviceOmniSwitch6450U24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 1, 23)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6450U24X.setStatus("current")
_FansOmniSwitch6450_ObjectIdentity = ObjectIdentity
fansOmniSwitch6450 = _FansOmniSwitch6450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6450.setStatus("current")
_PowersOmniSwitch6450_ObjectIdentity = ObjectIdentity
powersOmniSwitch6450 = _PowersOmniSwitch6450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6450.setStatus("current")
_PowersOmniSwitch90AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch90AC = _PowersOmniSwitch90AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch90AC.setStatus("current")
_PowersOmniSwitch550AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch550AC = _PowersOmniSwitch550AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch550AC.setStatus("current")
_PowersOmniSwitch90DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch90DC = _PowersOmniSwitch90DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch90DC.setStatus("current")
_PowersOmniSwitch320AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch320AC = _PowersOmniSwitch320AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 3, 4)
)
if mibBuilder.loadTexts:
    powersOmniSwitch320AC.setStatus("current")
_PowersOmniSwitch6450900AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6450900AC = _PowersOmniSwitch6450900AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 3, 5)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6450900AC.setStatus("current")
_ModulesOmniSwitch6450_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6450 = _ModulesOmniSwitch6450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6450.setStatus("current")
_IcOmniSwitch6000TenGIC_ObjectIdentity = ObjectIdentity
icOmniSwitch6000TenGIC = _IcOmniSwitch6000TenGIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 1)
)
if mibBuilder.loadTexts:
    icOmniSwitch6000TenGIC.setStatus("current")
_MgicOmniSwitch6000SR_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000SR = _MgicOmniSwitch6000SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000SR.setStatus("current")
_MgicOmniSwitch6000LR_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000LR = _MgicOmniSwitch6000LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000LR.setStatus("current")
_MgicOmniSwitch6000ER_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000ER = _MgicOmniSwitch6000ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 1, 3)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000ER.setStatus("current")
_MgicOmniSwitch6000LRM_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000LRM = _MgicOmniSwitch6000LRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 1, 4)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000LRM.setStatus("current")
_IcOmniSwitch6000GIC_ObjectIdentity = ObjectIdentity
icOmniSwitch6000GIC = _IcOmniSwitch6000GIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 2)
)
if mibBuilder.loadTexts:
    icOmniSwitch6000GIC.setStatus("current")
_MgicOmniSwitch6000LH70_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000LH70 = _MgicOmniSwitch6000LH70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000LH70.setStatus("current")
_MgicOmniSwitch6000LX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000LX = _MgicOmniSwitch6000LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 2, 2)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000LX.setStatus("current")
_MgicOmniSwitch6000SX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000SX = _MgicOmniSwitch6000SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 2, 3)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000SX.setStatus("current")
_MgicOmniSwitch6000C_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000C = _MgicOmniSwitch6000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 2, 4)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000C.setStatus("current")
_MgicOmniSwitch6000100FX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000100FX = _MgicOmniSwitch6000100FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 2, 5)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000100FX.setStatus("current")
_MgicOmniSwitch60001001000_ObjectIdentity = ObjectIdentity
mgicOmniSwitch60001001000 = _MgicOmniSwitch60001001000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 2, 6)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch60001001000.setStatus("current")
_MgicOmniSwitch6000BX_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000BX = _MgicOmniSwitch6000BX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 2, 7)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000BX.setStatus("current")
_MgicOmniSwitch6000XFPDAC_ObjectIdentity = ObjectIdentity
mgicOmniSwitch6000XFPDAC = _MgicOmniSwitch6000XFPDAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 4, 2, 8)
)
if mibBuilder.loadTexts:
    mgicOmniSwitch6000XFPDAC.setStatus("current")
_DaughterBoardOmniSwitch6450_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6450 = _DaughterBoardOmniSwitch6450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 5)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6450.setStatus("current")
_DaughterBoardOmniSwitch6450RJ45_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6450RJ45 = _DaughterBoardOmniSwitch6450RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 5, 4)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6450RJ45.setStatus("current")
_DaughterBoardOmniSwitch6450XNI_U2_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6450XNI_U2 = _DaughterBoardOmniSwitch6450XNI_U2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 5, 5)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6450XNI_U2.setStatus("current")
_DaughterBoardOmniSwitch6450XNI_U2_HDMI_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6450XNI_U2_HDMI = _DaughterBoardOmniSwitch6450XNI_U2_HDMI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 5, 6)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6450XNI_U2_HDMI.setStatus("current")
_DaughterBoardOmniSwitch6450GNI_U2_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6450GNI_U2 = _DaughterBoardOmniSwitch6450GNI_U2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 12, 5, 7)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6450GNI_U2.setStatus("current")
_FamilyOmniSwitch6350_ObjectIdentity = ObjectIdentity
familyOmniSwitch6350 = _FamilyOmniSwitch6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6350.setStatus("current")
_ChassisOmniSwitch6350_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6350 = _ChassisOmniSwitch6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6350.setStatus("current")
_DeviceOmniSwitch6350C24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6350C24 = _DeviceOmniSwitch6350C24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6350C24.setStatus("current")
_DeviceOmniSwitch6350P24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6350P24 = _DeviceOmniSwitch6350P24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6350P24.setStatus("current")
_DeviceOmniSwitch6350C48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6350C48 = _DeviceOmniSwitch6350C48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6350C48.setStatus("current")
_DeviceOmniSwitch6350P48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6350P48 = _DeviceOmniSwitch6350P48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6350P48.setStatus("current")
_DeviceOmniSwitch6350C10_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6350C10 = _DeviceOmniSwitch6350C10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6350C10.setStatus("current")
_DeviceOmniSwitch6350P10_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6350P10 = _DeviceOmniSwitch6350P10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6350P10.setStatus("current")
_FansOmniSwitch6350_ObjectIdentity = ObjectIdentity
fansOmniSwitch6350 = _FansOmniSwitch6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6350.setStatus("current")
_PowersOmniSwitch6350_ObjectIdentity = ObjectIdentity
powersOmniSwitch6350 = _PowersOmniSwitch6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6350.setStatus("current")
_PowersOmniSwitch30AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch30AC = _PowersOmniSwitch30AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch30AC.setStatus("current")
_PowersOmniSwitch525AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch525AC = _PowersOmniSwitch525AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch525AC.setStatus("current")
_PowersOmniSwitch60AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch60AC = _PowersOmniSwitch60AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch60AC.setStatus("current")
_PowersOmniSwitch915AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch915AC = _PowersOmniSwitch915AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 3, 4)
)
if mibBuilder.loadTexts:
    powersOmniSwitch915AC.setStatus("current")
_ModulesOmniSwitch6350_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6350 = _ModulesOmniSwitch6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 1, 13, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6350.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DEVICES",
    **{"alcatelIND1DevicesMIB": alcatelIND1DevicesMIB,
       "familyOmniSwitch7000": familyOmniSwitch7000,
       "chassisOmniSwitch7000": chassisOmniSwitch7000,
       "deviceOmniSwitch7700": deviceOmniSwitch7700,
       "deviceOmniSwitch7800": deviceOmniSwitch7800,
       "fansOmniSwitch7000": fansOmniSwitch7000,
       "fansOmniSwitch7000FT": fansOmniSwitch7000FT,
       "powersOmniSwitch7000": powersOmniSwitch7000,
       "powersOmniSwitch7000PS600AC": powersOmniSwitch7000PS600AC,
       "powersOmniSwitch7000PS600DC": powersOmniSwitch7000PS600DC,
       "powersOmniSwitch7000PDShelf": powersOmniSwitch7000PDShelf,
       "powersOmniSwitch7000PDPS600AC": powersOmniSwitch7000PDPS600AC,
       "powersOmniSwitch7000PDPS900DC": powersOmniSwitch7000PDPS900DC,
       "modulesOmniSwitch7000": modulesOmniSwitch7000,
       "modulesOmniSwitch7000CM": modulesOmniSwitch7000CM,
       "cmmOmniSwitch7700": cmmOmniSwitch7700,
       "cmmOmniSwitch7700PROC": cmmOmniSwitch7700PROC,
       "cmmOmniSwitch7700BBUS": cmmOmniSwitch7700BBUS,
       "cmmOmniSwitch7800": cmmOmniSwitch7800,
       "cmmOmniSwitch7800PROC": cmmOmniSwitch7800PROC,
       "cmmOmniSwitch7800BBUS": cmmOmniSwitch7800BBUS,
       "modulesOmniSwitch7000NI": modulesOmniSwitch7000NI,
       "niOmniSwitch7000ENI": niOmniSwitch7000ENI,
       "eniOmniSwitch7000C24": eniOmniSwitch7000C24,
       "eniOmniSwitch7000FM12": eniOmniSwitch7000FM12,
       "eniOmniSwitch7000PDPS24ENI": eniOmniSwitch7000PDPS24ENI,
       "niOmniSwitch7000GNI": niOmniSwitch7000GNI,
       "gniOmniSwitch7000U2": gniOmniSwitch7000U2,
       "gni2OmniSwitch7000C12": gni2OmniSwitch7000C12,
       "gni2OmniSwitch7000U12": gni2OmniSwitch7000U12,
       "niOmniSwitch7000IC": niOmniSwitch7000IC,
       "icOmniSwitch7000GIC": icOmniSwitch7000GIC,
       "gicOmniSwitch7000LH70": gicOmniSwitch7000LH70,
       "gicOmniSwitch7000LX": gicOmniSwitch7000LX,
       "gicOmniSwitch7000SX": gicOmniSwitch7000SX,
       "gicOmniSwitch7000C": gicOmniSwitch7000C,
       "gicOmniSwitch7000100FX": gicOmniSwitch7000100FX,
       "gicOmniSwitch70001001000": gicOmniSwitch70001001000,
       "gicOmniSwitch7000BX": gicOmniSwitch7000BX,
       "gicOmniSwitch7000101001000": gicOmniSwitch7000101001000,
       "niOmniSwitch7000DM": niOmniSwitch7000DM,
       "dmOmniSwitch7000Power": dmOmniSwitch7000Power,
       "dmOmniSwitch7000PowerDsine": dmOmniSwitch7000PowerDsine,
       "niOmniSwitch7000ANI": niOmniSwitch7000ANI,
       "aniOmniSwitch7000U4": aniOmniSwitch7000U4,
       "aniOmniSwitch7000U1": aniOmniSwitch7000U1,
       "familyOmniSwitch8000": familyOmniSwitch8000,
       "chassisOmniSwitch8000": chassisOmniSwitch8000,
       "deviceOmniSwitch8800": deviceOmniSwitch8800,
       "fansOmniSwitch8000": fansOmniSwitch8000,
       "fansOmniSwitch8800CFT": fansOmniSwitch8800CFT,
       "fansOmniSwitch8800FFT": fansOmniSwitch8800FFT,
       "powersOmniSwitch8000": powersOmniSwitch8000,
       "powersOmniSwitch8000PS1375AC": powersOmniSwitch8000PS1375AC,
       "powersOmniSwitch8000PS1375DC": powersOmniSwitch8000PS1375DC,
       "modulesOmniSwitch8000": modulesOmniSwitch8000,
       "modulesOmniSwitch8000CM": modulesOmniSwitch8000CM,
       "cmmOmniSwitch8800": cmmOmniSwitch8800,
       "cmmOmniSwitch8800PROC": cmmOmniSwitch8800PROC,
       "cmmOmniSwitch8800BBUS": cmmOmniSwitch8800BBUS,
       "modulesOmniSwitch8000NI": modulesOmniSwitch8000NI,
       "niOmniSwitch8000ENI": niOmniSwitch8000ENI,
       "eniOmniSwitch8000C24": eniOmniSwitch8000C24,
       "niOmniSwitch8000GNI": niOmniSwitch8000GNI,
       "gniOmniSwitch8000U8": gniOmniSwitch8000U8,
       "gniOmniSwitch8000C8": gniOmniSwitch8000C8,
       "gni2OmniSwitch8000U8": gni2OmniSwitch8000U8,
       "gni2OmniSwitch8000C24": gni2OmniSwitch8000C24,
       "gni2OmniSwitch8000U24": gni2OmniSwitch8000U24,
       "niOmniSwitch8000G10NI": niOmniSwitch8000G10NI,
       "g10niOmniSwitch8000U1": g10niOmniSwitch8000U1,
       "niOmniSwitch8000IC": niOmniSwitch8000IC,
       "icOmniSwitch8000GIC": icOmniSwitch8000GIC,
       "mgicOmniSwitch8000SX": mgicOmniSwitch8000SX,
       "mgicOmniSwitch8000LX": mgicOmniSwitch8000LX,
       "mgicOmniSwitch8000LH70": mgicOmniSwitch8000LH70,
       "mgicOmniSwitch6800LRM": mgicOmniSwitch6800LRM,
       "mgicOmniSwitch6800SFPP": mgicOmniSwitch6800SFPP,
       "mgicOmniSwitch6800KF2SFPP": mgicOmniSwitch6800KF2SFPP,
       "mgicOmniSwitch6800KF2HDMI": mgicOmniSwitch6800KF2HDMI,
       "mgicOmniSwitch6800SFPPSR": mgicOmniSwitch6800SFPPSR,
       "mgicOmniSwitch6800SFPPLR": mgicOmniSwitch6800SFPPLR,
       "mgicOmniSwitch6800SFPPER": mgicOmniSwitch6800SFPPER,
       "mgicOmniSwitch6800SFPPLRM": mgicOmniSwitch6800SFPPLRM,
       "mgicOmniSwitch6800XFPSR": mgicOmniSwitch6800XFPSR,
       "mgicOmniSwitch6800T": mgicOmniSwitch6800T,
       "modulesOmniSwitch8000SF": modulesOmniSwitch8000SF,
       "sfOmniSwitch8800SFM": sfOmniSwitch8800SFM,
       "familyOmniSwitch6600": familyOmniSwitch6600,
       "chassisOmniSwitch6600": chassisOmniSwitch6600,
       "deviceOmniSwitch6624": deviceOmniSwitch6624,
       "deviceOmniSwitch6648": deviceOmniSwitch6648,
       "deviceOmniSwitch6624Fiber": deviceOmniSwitch6624Fiber,
       "deviceOmniSwitch660224": deviceOmniSwitch660224,
       "deviceOmniSwitch660248": deviceOmniSwitch660248,
       "deviceOmniSwitch6624PoE": deviceOmniSwitch6624PoE,
       "deviceOmniSwitch6648PoE": deviceOmniSwitch6648PoE,
       "fansOmniSwitch6600": fansOmniSwitch6600,
       "powersOmniSwitch6600": powersOmniSwitch6600,
       "powersOmniSwitch6600BSP": powersOmniSwitch6600BSP,
       "modulesOmniSwitch6600": modulesOmniSwitch6600,
       "expOmniSwitch6600": expOmniSwitch6600,
       "mgicOmniSwitch66002": mgicOmniSwitch66002,
       "gsmOmniSwitch6600T2": gsmOmniSwitch6600T2,
       "stkOmniSwitch6600Kit": stkOmniSwitch6600Kit,
       "icOmniSwitch6600GIC": icOmniSwitch6600GIC,
       "mgicOmniSwitch6600SX": mgicOmniSwitch6600SX,
       "mgicOmniSwitch6600LX": mgicOmniSwitch6600LX,
       "mgicOmniSwitch6600LH70": mgicOmniSwitch6600LH70,
       "familyOmniAccess200": familyOmniAccess200,
       "chassisOmniAccess200": chassisOmniAccess200,
       "deviceOmniAccess210": deviceOmniAccess210,
       "deviceOmniAccess250": deviceOmniAccess250,
       "fansOmniSwitch200": fansOmniSwitch200,
       "powersOmniAccess200": powersOmniAccess200,
       "modulesOmniAccess200": modulesOmniAccess200,
       "familyOmniStack6300": familyOmniStack6300,
       "chassisOmniStack6300": chassisOmniStack6300,
       "deviceOmniStack6324": deviceOmniStack6324,
       "fansOmniStack6300": fansOmniStack6300,
       "powersOmniStack6300": powersOmniStack6300,
       "modulesOmniStack6300": modulesOmniStack6300,
       "familyOmniSwitch6800": familyOmniSwitch6800,
       "chassisOmniSwitch6800": chassisOmniSwitch6800,
       "deviceOmniSwitch6824": deviceOmniSwitch6824,
       "deviceOmniSwitch6848": deviceOmniSwitch6848,
       "deviceOmniSwitch6824Fiber": deviceOmniSwitch6824Fiber,
       "deviceOmniSwitch6824PoE": deviceOmniSwitch6824PoE,
       "deviceOmniSwitch6848PoE": deviceOmniSwitch6848PoE,
       "deviceOmniSwitch6824L": deviceOmniSwitch6824L,
       "deviceOmniSwitch6848L": deviceOmniSwitch6848L,
       "deviceOmniSwitch6824LU": deviceOmniSwitch6824LU,
       "deviceOmniSwitch6848LU": deviceOmniSwitch6848LU,
       "deviceOmniSwitch6824LPoE": deviceOmniSwitch6824LPoE,
       "deviceOmniSwitch6848LPoE": deviceOmniSwitch6848LPoE,
       "deviceOmniSwitch6824LUPoE": deviceOmniSwitch6824LUPoE,
       "deviceOmniSwitch6848LUPoE": deviceOmniSwitch6848LUPoE,
       "fansOmniSwitch6800": fansOmniSwitch6800,
       "powersOmniSwitch6800": powersOmniSwitch6800,
       "powersOmniSwitch6800BPS": powersOmniSwitch6800BPS,
       "powersOmniSwitch6800MOD": powersOmniSwitch6800MOD,
       "powersOmniSwitch6800SHLF": powersOmniSwitch6800SHLF,
       "modulesOmniSwitch6800": modulesOmniSwitch6800,
       "icOmniSwitch8000TenGIC": icOmniSwitch8000TenGIC,
       "mgicOmniSwitch6800SR": mgicOmniSwitch6800SR,
       "mgicOmniSwitch6800LR": mgicOmniSwitch6800LR,
       "icOmniSwitch6800GIC": icOmniSwitch6800GIC,
       "mgicOmniSwitch6800SX": mgicOmniSwitch6800SX,
       "mgicOmniSwitch6800LX": mgicOmniSwitch6800LX,
       "mgicOmniSwitch6800LH70": mgicOmniSwitch6800LH70,
       "expOmniSwitch6800": expOmniSwitch6800,
       "expOmniSwitch6800U2": expOmniSwitch6800U2,
       "familyOmniSwitch6850": familyOmniSwitch6850,
       "chassisOmniSwitch6850": chassisOmniSwitch6850,
       "deviceOmniSwitch685024": deviceOmniSwitch685024,
       "deviceOmniSwitch685048": deviceOmniSwitch685048,
       "deviceOmniSwitch685024X": deviceOmniSwitch685024X,
       "deviceOmniSwitch685048X": deviceOmniSwitch685048X,
       "deviceOmniSwitch6850P24": deviceOmniSwitch6850P24,
       "deviceOmniSwitch6850P48": deviceOmniSwitch6850P48,
       "deviceOmniSwitch6850P24X": deviceOmniSwitch6850P24X,
       "deviceOmniSwitch6850P48X": deviceOmniSwitch6850P48X,
       "deviceOmniSwitch6850U24": deviceOmniSwitch6850U24,
       "deviceOmniSwitch6850U24X": deviceOmniSwitch6850U24X,
       "deviceOmniSwitch685024L": deviceOmniSwitch685024L,
       "deviceOmniSwitch685048L": deviceOmniSwitch685048L,
       "deviceOmniSwitch685024XL": deviceOmniSwitch685024XL,
       "deviceOmniSwitch685048XL": deviceOmniSwitch685048XL,
       "deviceOmniSwitch6850P24L": deviceOmniSwitch6850P24L,
       "deviceOmniSwitch6850P48L": deviceOmniSwitch6850P48L,
       "deviceOmniSwitch6850P24XL": deviceOmniSwitch6850P24XL,
       "deviceOmniSwitch6850P48XL": deviceOmniSwitch6850P48XL,
       "deviceOmniSwitch685024LU": deviceOmniSwitch685024LU,
       "deviceOmniSwitch685048LU": deviceOmniSwitch685048LU,
       "deviceOmniSwitch685024XLU": deviceOmniSwitch685024XLU,
       "deviceOmniSwitch685048XLU": deviceOmniSwitch685048XLU,
       "deviceOmniSwitch6850P24LU": deviceOmniSwitch6850P24LU,
       "deviceOmniSwitch6850P48LU": deviceOmniSwitch6850P48LU,
       "deviceOmniSwitch6850P24XLU": deviceOmniSwitch6850P24XLU,
       "deviceOmniSwitch6850P48XLU": deviceOmniSwitch6850P48XLU,
       "deviceOmniSwitch6850EP48": deviceOmniSwitch6850EP48,
       "deviceOmniSwitch6850EP48X": deviceOmniSwitch6850EP48X,
       "deviceOmniSwitch6850EP24": deviceOmniSwitch6850EP24,
       "deviceOmniSwitch6850EP24X": deviceOmniSwitch6850EP24X,
       "deviceOmniSwitch6850E48": deviceOmniSwitch6850E48,
       "deviceOmniSwitch6850E48X": deviceOmniSwitch6850E48X,
       "deviceOmniSwitch6850E24": deviceOmniSwitch6850E24,
       "deviceOmniSwitch6850E24X": deviceOmniSwitch6850E24X,
       "deviceOmniSwitch6850EU24X": deviceOmniSwitch6850EU24X,
       "fansOmniSwitch6850": fansOmniSwitch6850,
       "powersOmniSwitch6850": powersOmniSwitch6850,
       "powersOmniSwitch6850BPS": powersOmniSwitch6850BPS,
       "powersOmniSwitch120DC": powersOmniSwitch120DC,
       "powersOmniSwitch126AC": powersOmniSwitch126AC,
       "powersOmniSwitch360AC": powersOmniSwitch360AC,
       "powersOmniSwitch510AC": powersOmniSwitch510AC,
       "powersOmniSwitch900AC": powersOmniSwitch900AC,
       "powersOmniSwitchOsBPS": powersOmniSwitchOsBPS,
       "modulesOmniSwitch6850": modulesOmniSwitch6850,
       "daughterBoardOmniSwitch6850": daughterBoardOmniSwitch6850,
       "daughterBoardOmniSwitch6850ESFPplus": daughterBoardOmniSwitch6850ESFPplus,
       "familyOmniSwitch9000": familyOmniSwitch9000,
       "chassisOmniSwitch9000": chassisOmniSwitch9000,
       "deviceOmniSwitch9700": deviceOmniSwitch9700,
       "deviceOmniSwitch9800": deviceOmniSwitch9800,
       "deviceOmniSwitch9600": deviceOmniSwitch9600,
       "deviceOmniSwitch9700E": deviceOmniSwitch9700E,
       "deviceOmniSwitch9800E": deviceOmniSwitch9800E,
       "deviceOmniSwitch9600E": deviceOmniSwitch9600E,
       "fansOmniSwitch9000": fansOmniSwitch9000,
       "powersOmniSwitch9000": powersOmniSwitch9000,
       "modulesOmniSwitch9000": modulesOmniSwitch9000,
       "modulesOmniSwitch9000CM": modulesOmniSwitch9000CM,
       "cmmOmniSwitch9700": cmmOmniSwitch9700,
       "cmmOmniSwitch9700PROC": cmmOmniSwitch9700PROC,
       "cmmOmniSwitch9800": cmmOmniSwitch9800,
       "cmmOmniSwitch9800PROC": cmmOmniSwitch9800PROC,
       "cmmOmniSwitch9600": cmmOmniSwitch9600,
       "cmmOmniSwitch9600PROC": cmmOmniSwitch9600PROC,
       "modulesOmniSwitch9000NI": modulesOmniSwitch9000NI,
       "niOmniSwitch9000ENI": niOmniSwitch9000ENI,
       "niOmniSwitch9000GNI": niOmniSwitch9000GNI,
       "gniOmniSwitch9000C24": gniOmniSwitch9000C24,
       "gniOmniSwitch9000U24": gniOmniSwitch9000U24,
       "gniOmniSwitch9000U2": gniOmniSwitch9000U2,
       "gniOmniSwitch9000U6": gniOmniSwitch9000U6,
       "gniOmniSwitch9000P24": gniOmniSwitch9000P24,
       "gniOmniSwitch900048T": gniOmniSwitch900048T,
       "gniOmniSwitch9000GC20L": gniOmniSwitch9000GC20L,
       "gniOmniSwitch9000EC20L": gniOmniSwitch9000EC20L,
       "gniOmniSwitchLockedC20L": gniOmniSwitchLockedC20L,
       "gniOmniSwitch900048TE": gniOmniSwitch900048TE,
       "gniOmniSwitch9000EC20LE": gniOmniSwitch9000EC20LE,
       "gniOmniSwitchLockedC20LE": gniOmniSwitchLockedC20LE,
       "gniOmniSwitch9000C24E": gniOmniSwitch9000C24E,
       "gniOmniSwitch9000P24E": gniOmniSwitch9000P24E,
       "gniOmniSwitch9000U24E": gniOmniSwitch9000U24E,
       "gniOmniSwitch9000GC20LE": gniOmniSwitch9000GC20LE,
       "gniOmniSwitch9000U2E": gniOmniSwitch9000U2E,
       "gniOmniSwitch9000U6E": gniOmniSwitch9000U6E,
       "gniOmniSwitch9000C24FJ2E": gniOmniSwitch9000C24FJ2E,
       "gniOmniSwitch9000U24FJ2E": gniOmniSwitch9000U24FJ2E,
       "gniOmniSwitch9000U2FJ2E": gniOmniSwitch9000U2FJ2E,
       "gniOmniSwitch9000U12PlusFJ2E": gniOmniSwitch9000U12PlusFJ2E,
       "gniOmniSwitch9000P24FJ2E": gniOmniSwitch9000P24FJ2E,
       "niOmniSwitch9000IC": niOmniSwitch9000IC,
       "niOmniSwitch9000DM": niOmniSwitch9000DM,
       "familyOmniSwitch6855": familyOmniSwitch6855,
       "chassisOmniSwitch6855": chassisOmniSwitch6855,
       "deviceOmniSwitch685514": deviceOmniSwitch685514,
       "deviceOmniSwitch6855U10": deviceOmniSwitch6855U10,
       "deviceOmniSwitch685524": deviceOmniSwitch685524,
       "deviceOmniSwitch6855U24": deviceOmniSwitch6855U24,
       "deviceOmniSwitch6855U24X": deviceOmniSwitch6855U24X,
       "deviceOmniSwitch6855P14": deviceOmniSwitch6855P14,
       "fansOmniSwitch6855": fansOmniSwitch6855,
       "powersOmniSwitch6855": powersOmniSwitch6855,
       "powersOmniSwitch6855Devices40DC": powersOmniSwitch6855Devices40DC,
       "powersOmniSwitch6855Devices62DC": powersOmniSwitch6855Devices62DC,
       "powersOmniSwitch6855Devices180DC": powersOmniSwitch6855Devices180DC,
       "modulesOmniSwitch6855": modulesOmniSwitch6855,
       "familyOmniSwitch6400": familyOmniSwitch6400,
       "chassisOmniSwitch6400": chassisOmniSwitch6400,
       "deviceOmniSwitch640024": deviceOmniSwitch640024,
       "deviceOmniSwitch6400P24": deviceOmniSwitch6400P24,
       "deviceOmniSwitch6400U24": deviceOmniSwitch6400U24,
       "deviceOmniSwitch6400DU24": deviceOmniSwitch6400DU24,
       "deviceOmniSwitch640048": deviceOmniSwitch640048,
       "deviceOmniSwitch6400P48": deviceOmniSwitch6400P48,
       "fansOmniSwitch6400": fansOmniSwitch6400,
       "powersOmniSwitch6400": powersOmniSwitch6400,
       "powersOmniSwitch6400BPS": powersOmniSwitch6400BPS,
       "modulesOmniSwitch6400": modulesOmniSwitch6400,
       "familyOmniSwitch6250": familyOmniSwitch6250,
       "chassisOmniSwitch6250M": chassisOmniSwitch6250M,
       "deviceOmniSwitch62508M": deviceOmniSwitch62508M,
       "deviceOmniSwitch625024M": deviceOmniSwitch625024M,
       "deviceOmniSwitch625024MD": deviceOmniSwitch625024MD,
       "deviceOmniSwitch6250U24M": deviceOmniSwitch6250U24M,
       "chassisOmniSwitch6250ENT": chassisOmniSwitch6250ENT,
       "deviceOmniSwitch625024ENT": deviceOmniSwitch625024ENT,
       "deviceOmniSwitch6250P24ENT": deviceOmniSwitch6250P24ENT,
       "fansOmniSwitch6250": fansOmniSwitch6250,
       "powersOmniSwitch6250": powersOmniSwitch6250,
       "powersOmniSwitch6250BPS": powersOmniSwitch6250BPS,
       "modulesOmniSwitch6250": modulesOmniSwitch6250,
       "familyOmniSwitch6450": familyOmniSwitch6450,
       "chassisOmniSwitch6450": chassisOmniSwitch6450,
       "deviceOmniSwitch6450C10": deviceOmniSwitch6450C10,
       "deviceOmniSwitch6450P10": deviceOmniSwitch6450P10,
       "deviceOmniSwitch6450C10L": deviceOmniSwitch6450C10L,
       "deviceOmniSwitch6450P10L": deviceOmniSwitch6450P10L,
       "deviceOmniSwitch6450C24": deviceOmniSwitch6450C24,
       "deviceOmniSwitch6450P24": deviceOmniSwitch6450P24,
       "deviceOmniSwitch6450U24": deviceOmniSwitch6450U24,
       "deviceOmniSwitch6450C48": deviceOmniSwitch6450C48,
       "deviceOmniSwitch6450P48": deviceOmniSwitch6450P48,
       "deviceOmniSwitch6450C24L": deviceOmniSwitch6450C24L,
       "deviceOmniSwitch6450P24L": deviceOmniSwitch6450P24L,
       "deviceOmniSwitch6450C48L": deviceOmniSwitch6450C48L,
       "deviceOmniSwitch6450P48L": deviceOmniSwitch6450P48L,
       "deviceOmniSwitch6450P10S": deviceOmniSwitch6450P10S,
       "deviceOmniSwitch6450U24S": deviceOmniSwitch6450U24S,
       "deviceOmniSwitch6450C10M": deviceOmniSwitch6450C10M,
       "deviceOmniSwitch6450C24XM": deviceOmniSwitch6450C24XM,
       "deviceOmniSwitch6450C24X": deviceOmniSwitch6450C24X,
       "deviceOmniSwitch6450P24X": deviceOmniSwitch6450P24X,
       "deviceOmniSwitch6450C48X": deviceOmniSwitch6450C48X,
       "deviceOmniSwitch6450P48X": deviceOmniSwitch6450P48X,
       "deviceOmniSwitch6450U24SXM": deviceOmniSwitch6450U24SXM,
       "deviceOmniSwitch6450U24X": deviceOmniSwitch6450U24X,
       "fansOmniSwitch6450": fansOmniSwitch6450,
       "powersOmniSwitch6450": powersOmniSwitch6450,
       "powersOmniSwitch90AC": powersOmniSwitch90AC,
       "powersOmniSwitch550AC": powersOmniSwitch550AC,
       "powersOmniSwitch90DC": powersOmniSwitch90DC,
       "powersOmniSwitch320AC": powersOmniSwitch320AC,
       "powersOmniSwitch6450900AC": powersOmniSwitch6450900AC,
       "modulesOmniSwitch6450": modulesOmniSwitch6450,
       "icOmniSwitch6000TenGIC": icOmniSwitch6000TenGIC,
       "mgicOmniSwitch6000SR": mgicOmniSwitch6000SR,
       "mgicOmniSwitch6000LR": mgicOmniSwitch6000LR,
       "mgicOmniSwitch6000ER": mgicOmniSwitch6000ER,
       "mgicOmniSwitch6000LRM": mgicOmniSwitch6000LRM,
       "icOmniSwitch6000GIC": icOmniSwitch6000GIC,
       "mgicOmniSwitch6000LH70": mgicOmniSwitch6000LH70,
       "mgicOmniSwitch6000LX": mgicOmniSwitch6000LX,
       "mgicOmniSwitch6000SX": mgicOmniSwitch6000SX,
       "mgicOmniSwitch6000C": mgicOmniSwitch6000C,
       "mgicOmniSwitch6000100FX": mgicOmniSwitch6000100FX,
       "mgicOmniSwitch60001001000": mgicOmniSwitch60001001000,
       "mgicOmniSwitch6000BX": mgicOmniSwitch6000BX,
       "mgicOmniSwitch6000XFPDAC": mgicOmniSwitch6000XFPDAC,
       "daughterBoardOmniSwitch6450": daughterBoardOmniSwitch6450,
       "daughterBoardOmniSwitch6450RJ45": daughterBoardOmniSwitch6450RJ45,
       "daughterBoardOmniSwitch6450XNI-U2": daughterBoardOmniSwitch6450XNI_U2,
       "daughterBoardOmniSwitch6450XNI-U2-HDMI": daughterBoardOmniSwitch6450XNI_U2_HDMI,
       "daughterBoardOmniSwitch6450GNI-U2": daughterBoardOmniSwitch6450GNI_U2,
       "familyOmniSwitch6350": familyOmniSwitch6350,
       "chassisOmniSwitch6350": chassisOmniSwitch6350,
       "deviceOmniSwitch6350C24": deviceOmniSwitch6350C24,
       "deviceOmniSwitch6350P24": deviceOmniSwitch6350P24,
       "deviceOmniSwitch6350C48": deviceOmniSwitch6350C48,
       "deviceOmniSwitch6350P48": deviceOmniSwitch6350P48,
       "deviceOmniSwitch6350C10": deviceOmniSwitch6350C10,
       "deviceOmniSwitch6350P10": deviceOmniSwitch6350P10,
       "fansOmniSwitch6350": fansOmniSwitch6350,
       "powersOmniSwitch6350": powersOmniSwitch6350,
       "powersOmniSwitch30AC": powersOmniSwitch30AC,
       "powersOmniSwitch525AC": powersOmniSwitch525AC,
       "powersOmniSwitch60AC": powersOmniSwitch60AC,
       "powersOmniSwitch915AC": powersOmniSwitch915AC,
       "modulesOmniSwitch6350": modulesOmniSwitch6350}
)
