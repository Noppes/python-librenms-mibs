# SNMP MIB module (PACKETFLUX-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetflux\PACKETFLUX-TC

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

(packetfluxModuleIdentities,) = mibBuilder.importSymbols(
    "PACKETFLUX-SMI",
    "packetfluxModuleIdentities")

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

packetfluxTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 4, 1)
)
if mibBuilder.loadTexts:
    packetfluxTC.setRevisions(
        ("2018-07-07 13:02",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Fixed1DecimalDigit(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class Fixed2DecimalDigits(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


class Fixed3DecimalDigits(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class Fixed4DecimalDigits(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-4"


class Fixed5DecimalDigits(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-5"


class Fixed6DecimalDigits(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-6"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFLUX-TC",
    **{"Fixed1DecimalDigit": Fixed1DecimalDigit,
       "Fixed2DecimalDigits": Fixed2DecimalDigits,
       "Fixed3DecimalDigits": Fixed3DecimalDigits,
       "Fixed4DecimalDigits": Fixed4DecimalDigits,
       "Fixed5DecimalDigits": Fixed5DecimalDigits,
       "Fixed6DecimalDigits": Fixed6DecimalDigits,
       "packetfluxTC": packetfluxTC}
)
