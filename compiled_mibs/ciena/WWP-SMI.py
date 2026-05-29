# SNMP MIB module (WWP-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\WWP-SMI

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

wwp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141)
)
if mibBuilder.loadTexts:
    wwp.setRevisions(
        ("2013-04-23 00:00",
         "2012-12-26 00:00",
         "2005-07-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpProducts_ObjectIdentity = ObjectIdentity
wwpProducts = _WwpProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1)
)
if mibBuilder.loadTexts:
    wwpProducts.setStatus("current")
_WwpModules_ObjectIdentity = ObjectIdentity
wwpModules = _WwpModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2)
)
if mibBuilder.loadTexts:
    wwpModules.setStatus("current")
_WwpModulesLeos_ObjectIdentity = ObjectIdentity
wwpModulesLeos = _WwpModulesLeos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60)
)
if mibBuilder.loadTexts:
    wwpModulesLeos.setStatus("current")
_WwpModulesLeosTce_ObjectIdentity = ObjectIdentity
wwpModulesLeosTce = _WwpModulesLeosTce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 61)
)
if mibBuilder.loadTexts:
    wwpModulesLeosTce.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-SMI",
    **{"wwp": wwp,
       "wwpProducts": wwpProducts,
       "wwpModules": wwpModules,
       "wwpModulesLeos": wwpModulesLeos,
       "wwpModulesLeosTce": wwpModulesLeosTce}
)
