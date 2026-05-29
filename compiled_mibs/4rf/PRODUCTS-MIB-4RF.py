# SNMP MIB module (PRODUCTS-MIB-4RF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\4rf\PRODUCTS-MIB-4RF

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

(fourRFExperimental,
 fourRFModules,
 fourRFProducts) = mibBuilder.importSymbols(
    "MIB-4RF",
    "fourRFExperimental",
    "fourRFModules",
    "fourRFProducts")

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

fourRFProductsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 2, 2)
)
if mibBuilder.loadTexts:
    fourRFProductsModule.setRevisions(
        ("2007-04-30 00:00",
         "2004-02-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FourRFCommon_ObjectIdentity = ObjectIdentity
fourRFCommon = _FourRFCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1)
)
if mibBuilder.loadTexts:
    fourRFCommon.setStatus("current")
_FourRFAprisa_ObjectIdentity = ObjectIdentity
fourRFAprisa = _FourRFAprisa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 2)
)
if mibBuilder.loadTexts:
    fourRFAprisa.setStatus("current")
_FourRFAprisaXE_ObjectIdentity = ObjectIdentity
fourRFAprisaXE = _FourRFAprisaXE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 3)
)
if mibBuilder.loadTexts:
    fourRFAprisaXE.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRODUCTS-MIB-4RF",
    **{"fourRFProductsModule": fourRFProductsModule,
       "fourRFCommon": fourRFCommon,
       "fourRFAprisa": fourRFAprisa,
       "fourRFAprisaXE": fourRFAprisaXE}
)
