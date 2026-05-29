# SNMP MIB module (PACKETFLUX-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetflux\PACKETFLUX-SMI

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

packetflux = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32050)
)
if mibBuilder.loadTexts:
    packetflux.setRevisions(
        ("2018-07-07 12:55",
         "2013-06-04 16:32")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PacketfluxProductIDs_ObjectIdentity = ObjectIdentity
packetfluxProductIDs = _PacketfluxProductIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 1)
)
if mibBuilder.loadTexts:
    packetfluxProductIDs.setStatus("current")
_PacketfluxProductSpecific_ObjectIdentity = ObjectIdentity
packetfluxProductSpecific = _PacketfluxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 2)
)
if mibBuilder.loadTexts:
    packetfluxProductSpecific.setStatus("current")
_PacketfluxFeatureSpecific_ObjectIdentity = ObjectIdentity
packetfluxFeatureSpecific = _PacketfluxFeatureSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3)
)
if mibBuilder.loadTexts:
    packetfluxFeatureSpecific.setStatus("current")
_PacketfluxModuleIdentities_ObjectIdentity = ObjectIdentity
packetfluxModuleIdentities = _PacketfluxModuleIdentities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 4)
)
if mibBuilder.loadTexts:
    packetfluxModuleIdentities.setStatus("current")
_PacketfluxExperimental_ObjectIdentity = ObjectIdentity
packetfluxExperimental = _PacketfluxExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 5)
)
if mibBuilder.loadTexts:
    packetfluxExperimental.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFLUX-SMI",
    **{"packetflux": packetflux,
       "packetfluxProductIDs": packetfluxProductIDs,
       "packetfluxProductSpecific": packetfluxProductSpecific,
       "packetfluxFeatureSpecific": packetfluxFeatureSpecific,
       "packetfluxModuleIdentities": packetfluxModuleIdentities,
       "packetfluxExperimental": packetfluxExperimental}
)
