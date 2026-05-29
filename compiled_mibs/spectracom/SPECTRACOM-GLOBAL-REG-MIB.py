# SNMP MIB module (SPECTRACOM-GLOBAL-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\spectracom\SPECTRACOM-GLOBAL-REG-MIB

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

spectracomGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 1, 1)
)
if mibBuilder.loadTexts:
    spectracomGlobalRegModule.setRevisions(
        ("2022-01-07 00:00",
         "2020-03-29 00:00",
         "2012-05-17 00:00",
         "2010-04-17 00:00",
         "2009-06-19 12:00",
         "2004-08-30 02:00",
         "2004-08-30 01:00",
         "2004-08-30 00:00",
         "2004-07-13 00:00",
         "2004-05-21 00:00",
         "2004-05-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Spectracom_ObjectIdentity = ObjectIdentity
spectracom = _Spectracom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837)
)
_SpecReg_ObjectIdentity = ObjectIdentity
specReg = _SpecReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1)
)
_SpecModules_ObjectIdentity = ObjectIdentity
specModules = _SpecModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 1)
)
_SpecTimeFreqProducts_ObjectIdentity = ObjectIdentity
specTimeFreqProducts = _SpecTimeFreqProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2)
)
_TfTTS200Reg_ObjectIdentity = ObjectIdentity
tfTTS200Reg = _TfTTS200Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tfTTS200Reg.setStatus("current")
_TfTTS220Reg_ObjectIdentity = ObjectIdentity
tfTTS220Reg = _TfTTS220Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tfTTS220Reg.setStatus("current")
_TfTTS240Reg_ObjectIdentity = ObjectIdentity
tfTTS240Reg = _TfTTS240Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tfTTS240Reg.setStatus("current")
_TfTTS260Reg_ObjectIdentity = ObjectIdentity
tfTTS260Reg = _TfTTS260Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tfTTS260Reg.setStatus("current")
_TfTTS280Reg_ObjectIdentity = ObjectIdentity
tfTTS280Reg = _TfTTS280Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tfTTS280Reg.setStatus("current")
_Tf9183Reg_ObjectIdentity = ObjectIdentity
tf9183Reg = _Tf9183Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tf9183Reg.setStatus("current")
_Tf9188Reg_ObjectIdentity = ObjectIdentity
tf9188Reg = _Tf9188Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tf9188Reg.setStatus("current")
_Tf9188sReg_ObjectIdentity = ObjectIdentity
tf9188sReg = _Tf9188sReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tf9188sReg.setStatus("current")
_Tf9189Reg_ObjectIdentity = ObjectIdentity
tf9189Reg = _Tf9189Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 9)
)
if mibBuilder.loadTexts:
    tf9189Reg.setStatus("current")
_Tf9183esReg_ObjectIdentity = ObjectIdentity
tf9183esReg = _Tf9183esReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 10)
)
if mibBuilder.loadTexts:
    tf9183esReg.setStatus("current")
_Tf240oReg_ObjectIdentity = ObjectIdentity
tf240oReg = _Tf240oReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 11)
)
if mibBuilder.loadTexts:
    tf240oReg.setStatus("current")
_Tf240rbReg_ObjectIdentity = ObjectIdentity
tf240rbReg = _Tf240rbReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 12)
)
if mibBuilder.loadTexts:
    tf240rbReg.setStatus("current")
_Tf260rbReg_ObjectIdentity = ObjectIdentity
tf260rbReg = _Tf260rbReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 13)
)
if mibBuilder.loadTexts:
    tf260rbReg.setStatus("current")
_Tf9283Reg_ObjectIdentity = ObjectIdentity
tf9283Reg = _Tf9283Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 14)
)
if mibBuilder.loadTexts:
    tf9283Reg.setStatus("current")
_Tf9288Reg_ObjectIdentity = ObjectIdentity
tf9288Reg = _Tf9288Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 15)
)
if mibBuilder.loadTexts:
    tf9288Reg.setStatus("current")
_Tf9289Reg_ObjectIdentity = ObjectIdentity
tf9289Reg = _Tf9289Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 16)
)
if mibBuilder.loadTexts:
    tf9289Reg.setStatus("current")
_Tf9383Reg_ObjectIdentity = ObjectIdentity
tf9383Reg = _Tf9383Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 17)
)
if mibBuilder.loadTexts:
    tf9383Reg.setStatus("current")
_Tf9388Reg_ObjectIdentity = ObjectIdentity
tf9388Reg = _Tf9388Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 18)
)
if mibBuilder.loadTexts:
    tf9388Reg.setStatus("current")
_Tf9389Reg_ObjectIdentity = ObjectIdentity
tf9389Reg = _Tf9389Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 2, 19)
)
if mibBuilder.loadTexts:
    tf9389Reg.setStatus("current")
_SpecSecureSyncProducts_ObjectIdentity = ObjectIdentity
specSecureSyncProducts = _SpecSecureSyncProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 3)
)
_SsSecureSyncReg_ObjectIdentity = ObjectIdentity
ssSecureSyncReg = _SsSecureSyncReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ssSecureSyncReg.setStatus("current")
_SpecNetClockProducts_ObjectIdentity = ObjectIdentity
specNetClockProducts = _SpecNetClockProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 4)
)
_Nc9483Reg_ObjectIdentity = ObjectIdentity
nc9483Reg = _Nc9483Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 4, 1)
)
if mibBuilder.loadTexts:
    nc9483Reg.setStatus("current")
_Nc9489Reg_ObjectIdentity = ObjectIdentity
nc9489Reg = _Nc9489Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 4, 2)
)
if mibBuilder.loadTexts:
    nc9489Reg.setStatus("current")
_SpecSkydelProducts_ObjectIdentity = ObjectIdentity
specSkydelProducts = _SpecSkydelProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 5)
)
_SpecGeneric_ObjectIdentity = ObjectIdentity
specGeneric = _SpecGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 2)
)
_SpecProducts_ObjectIdentity = ObjectIdentity
specProducts = _SpecProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3)
)
_SpecCaps_ObjectIdentity = ObjectIdentity
specCaps = _SpecCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 4)
)
_SpecReqs_ObjectIdentity = ObjectIdentity
specReqs = _SpecReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 5)
)
_SpecExpr_ObjectIdentity = ObjectIdentity
specExpr = _SpecExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPECTRACOM-GLOBAL-REG-MIB",
    **{"spectracom": spectracom,
       "specReg": specReg,
       "specModules": specModules,
       "spectracomGlobalRegModule": spectracomGlobalRegModule,
       "specTimeFreqProducts": specTimeFreqProducts,
       "tfTTS200Reg": tfTTS200Reg,
       "tfTTS220Reg": tfTTS220Reg,
       "tfTTS240Reg": tfTTS240Reg,
       "tfTTS260Reg": tfTTS260Reg,
       "tfTTS280Reg": tfTTS280Reg,
       "tf9183Reg": tf9183Reg,
       "tf9188Reg": tf9188Reg,
       "tf9188sReg": tf9188sReg,
       "tf9189Reg": tf9189Reg,
       "tf9183esReg": tf9183esReg,
       "tf240oReg": tf240oReg,
       "tf240rbReg": tf240rbReg,
       "tf260rbReg": tf260rbReg,
       "tf9283Reg": tf9283Reg,
       "tf9288Reg": tf9288Reg,
       "tf9289Reg": tf9289Reg,
       "tf9383Reg": tf9383Reg,
       "tf9388Reg": tf9388Reg,
       "tf9389Reg": tf9389Reg,
       "specSecureSyncProducts": specSecureSyncProducts,
       "ssSecureSyncReg": ssSecureSyncReg,
       "specNetClockProducts": specNetClockProducts,
       "nc9483Reg": nc9483Reg,
       "nc9489Reg": nc9489Reg,
       "specSkydelProducts": specSkydelProducts,
       "specGeneric": specGeneric,
       "specProducts": specProducts,
       "specCaps": specCaps,
       "specReqs": specReqs,
       "specExpr": specExpr}
)
