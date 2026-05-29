# SNMP MIB module (MIB-4RF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\4rf\MIB-4RF

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

fourRFRootModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 2, 1)
)
if mibBuilder.loadTexts:
    fourRFRootModule.setRevisions(
        ("2007-04-30 00:00",
         "2004-02-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FourRFRoot_ObjectIdentity = ObjectIdentity
fourRFRoot = _FourRFRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817)
)
if mibBuilder.loadTexts:
    fourRFRoot.setStatus("current")
_FourRFRegistrations_ObjectIdentity = ObjectIdentity
fourRFRegistrations = _FourRFRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 1)
)
if mibBuilder.loadTexts:
    fourRFRegistrations.setStatus("current")
_FourRFModules_ObjectIdentity = ObjectIdentity
fourRFModules = _FourRFModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 2)
)
if mibBuilder.loadTexts:
    fourRFModules.setStatus("current")
_FourRFGeneric_ObjectIdentity = ObjectIdentity
fourRFGeneric = _FourRFGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 3)
)
if mibBuilder.loadTexts:
    fourRFGeneric.setStatus("current")
_FourRFProducts_ObjectIdentity = ObjectIdentity
fourRFProducts = _FourRFProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 4)
)
if mibBuilder.loadTexts:
    fourRFProducts.setStatus("current")
_FourRFCapabilities_ObjectIdentity = ObjectIdentity
fourRFCapabilities = _FourRFCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 5)
)
if mibBuilder.loadTexts:
    fourRFCapabilities.setStatus("current")
_FourRFRequirements_ObjectIdentity = ObjectIdentity
fourRFRequirements = _FourRFRequirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 6)
)
if mibBuilder.loadTexts:
    fourRFRequirements.setStatus("current")
_FourRFExperimental_ObjectIdentity = ObjectIdentity
fourRFExperimental = _FourRFExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7)
)
if mibBuilder.loadTexts:
    fourRFExperimental.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB-4RF",
    **{"fourRFRoot": fourRFRoot,
       "fourRFRegistrations": fourRFRegistrations,
       "fourRFModules": fourRFModules,
       "fourRFRootModule": fourRFRootModule,
       "fourRFGeneric": fourRFGeneric,
       "fourRFProducts": fourRFProducts,
       "fourRFCapabilities": fourRFCapabilities,
       "fourRFRequirements": fourRFRequirements,
       "fourRFExperimental": fourRFExperimental}
)
