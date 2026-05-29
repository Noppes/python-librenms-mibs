# SNMP MIB module (ARISTA-BGP4V2-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arista\ARISTA-BGP4V2-TC-MIB

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

(aristaExperiment,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaExperiment")

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

aristaBgp4V2TC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 4, 2)
)
if mibBuilder.loadTexts:
    aristaBgp4V2TC.setRevisions(
        ("2020-12-29 00:00",
         "2014-08-15 00:00",
         "2012-10-19 00:00",
         "2011-01-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AristaBgp4V2IdentifierTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class AristaBgp4V2AddressFamilyIdentifierTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              25)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("l2vpn", 25))
    )



class AristaBgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              70)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("mpls", 4),
          ("evpn", 70))
    )



class AristaBgp4V2EvpnNlriTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("autoDiscovery", 1),
          ("macIp", 2),
          ("imet", 3),
          ("ethernetSegment", 4),
          ("ipPrefixIpv4", 5),
          ("ipPrefixIpv6", 6),
          ("smet", 7),
          ("joinSync", 8),
          ("leaveSync", 9),
          ("spmsi", 10))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-BGP4V2-TC-MIB",
    **{"AristaBgp4V2IdentifierTC": AristaBgp4V2IdentifierTC,
       "AristaBgp4V2AddressFamilyIdentifierTC": AristaBgp4V2AddressFamilyIdentifierTC,
       "AristaBgp4V2SubsequentAddressFamilyIdentifierTC": AristaBgp4V2SubsequentAddressFamilyIdentifierTC,
       "AristaBgp4V2EvpnNlriTC": AristaBgp4V2EvpnNlriTC,
       "aristaBgp4V2TC": aristaBgp4V2TC}
)
