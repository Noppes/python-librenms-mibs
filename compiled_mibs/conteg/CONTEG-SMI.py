# SNMP MIB module (CONTEG-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\conteg\CONTEG-SMI

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

conteg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28402)
)
if mibBuilder.loadTexts:
    conteg.setRevisions(
        ("2021-06-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ContegProducts_ObjectIdentity = ObjectIdentity
contegProducts = _ContegProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28402, 11)
)
if mibBuilder.loadTexts:
    contegProducts.setStatus("current")
_ContegMgmt_ObjectIdentity = ObjectIdentity
contegMgmt = _ContegMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28402, 12)
)
if mibBuilder.loadTexts:
    contegMgmt.setStatus("current")
_ContegModules_ObjectIdentity = ObjectIdentity
contegModules = _ContegModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28402, 13)
)
if mibBuilder.loadTexts:
    contegModules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTEG-SMI",
    **{"conteg": conteg,
       "contegProducts": contegProducts,
       "contegMgmt": contegMgmt,
       "contegModules": contegModules}
)
