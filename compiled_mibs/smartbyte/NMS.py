# SNMP MIB module (NMS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartbyte\NMS

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

nmsGlobalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 1, 1)
)
if mibBuilder.loadTexts:
    nmsGlobalModule.setRevisions(
        ("2021-05-14 09:47",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nms_ObjectIdentity = ObjectIdentity
nms = _Nms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166)
)
if mibBuilder.loadTexts:
    nms.setStatus("current")
_NmsModule_ObjectIdentity = ObjectIdentity
nmsModule = _NmsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 1)
)
_NmsGeneric_ObjectIdentity = ObjectIdentity
nmsGeneric = _NmsGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 2)
)
if mibBuilder.loadTexts:
    nmsGeneric.setStatus("current")
_NmsProducts_ObjectIdentity = ObjectIdentity
nmsProducts = _NmsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 3)
)
if mibBuilder.loadTexts:
    nmsProducts.setStatus("current")
_NmsCaps_ObjectIdentity = ObjectIdentity
nmsCaps = _NmsCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 4)
)
if mibBuilder.loadTexts:
    nmsCaps.setStatus("current")
_NmsReqs_ObjectIdentity = ObjectIdentity
nmsReqs = _NmsReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 5)
)
if mibBuilder.loadTexts:
    nmsReqs.setStatus("current")
_NmsExpr_ObjectIdentity = ObjectIdentity
nmsExpr = _NmsExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 6)
)
if mibBuilder.loadTexts:
    nmsExpr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS",
    **{"nms": nms,
       "nmsModule": nmsModule,
       "nmsGlobalModule": nmsGlobalModule,
       "nmsGeneric": nmsGeneric,
       "nmsProducts": nmsProducts,
       "nmsCaps": nmsCaps,
       "nmsReqs": nmsReqs,
       "nmsExpr": nmsExpr}
)
