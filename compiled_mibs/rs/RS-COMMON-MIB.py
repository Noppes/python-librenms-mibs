# SNMP MIB module (RS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\rs\RS-COMMON-MIB

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

rsRoot = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2566)
)
if mibBuilder.loadTexts:
    rsRoot.setRevisions(
        ("2006-05-17 08:40",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsCommon_ObjectIdentity = ObjectIdentity
rsCommon = _RsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 113)
)
if mibBuilder.loadTexts:
    rsCommon.setStatus("current")
_RsProducts_ObjectIdentity = ObjectIdentity
rsProducts = _RsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127)
)
if mibBuilder.loadTexts:
    rsProducts.setStatus("current")
_RsProdBroadcast_ObjectIdentity = ObjectIdentity
rsProdBroadcast = _RsProdBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1)
)
if mibBuilder.loadTexts:
    rsProdBroadcast.setStatus("current")
_RsProdBroadcastMeasurement_ObjectIdentity = ObjectIdentity
rsProdBroadcastMeasurement = _RsProdBroadcastMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 1)
)
if mibBuilder.loadTexts:
    rsProdBroadcastMeasurement.setStatus("current")
_RsProdBroadcastTransmitter_ObjectIdentity = ObjectIdentity
rsProdBroadcastTransmitter = _RsProdBroadcastTransmitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2)
)
if mibBuilder.loadTexts:
    rsProdBroadcastTransmitter.setStatus("current")
_RsRequirements_ObjectIdentity = ObjectIdentity
rsRequirements = _RsRequirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 131)
)
if mibBuilder.loadTexts:
    rsRequirements.setStatus("current")
_RsExperimental_ObjectIdentity = ObjectIdentity
rsExperimental = _RsExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 137)
)
if mibBuilder.loadTexts:
    rsExperimental.setStatus("current")
_RsCapabilities_ObjectIdentity = ObjectIdentity
rsCapabilities = _RsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 139)
)
if mibBuilder.loadTexts:
    rsCapabilities.setStatus("current")
_RsRegistration_ObjectIdentity = ObjectIdentity
rsRegistration = _RsRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 149)
)
if mibBuilder.loadTexts:
    rsRegistration.setStatus("current")
_RsRegModules_ObjectIdentity = ObjectIdentity
rsRegModules = _RsRegModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 149, 1)
)
if mibBuilder.loadTexts:
    rsRegModules.setStatus("current")
_RsRegBroadcast_ObjectIdentity = ObjectIdentity
rsRegBroadcast = _RsRegBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 149, 2)
)
if mibBuilder.loadTexts:
    rsRegBroadcast.setStatus("current")
_RsRegBroadcastMeasurement_ObjectIdentity = ObjectIdentity
rsRegBroadcastMeasurement = _RsRegBroadcastMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 149, 2, 1)
)
if mibBuilder.loadTexts:
    rsRegBroadcastMeasurement.setStatus("current")
_RsRegBroadcastTransmitter_ObjectIdentity = ObjectIdentity
rsRegBroadcastTransmitter = _RsRegBroadcastTransmitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 149, 2, 2)
)
if mibBuilder.loadTexts:
    rsRegBroadcastTransmitter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RS-COMMON-MIB",
    **{"rsRoot": rsRoot,
       "rsCommon": rsCommon,
       "rsProducts": rsProducts,
       "rsProdBroadcast": rsProdBroadcast,
       "rsProdBroadcastMeasurement": rsProdBroadcastMeasurement,
       "rsProdBroadcastTransmitter": rsProdBroadcastTransmitter,
       "rsRequirements": rsRequirements,
       "rsExperimental": rsExperimental,
       "rsCapabilities": rsCapabilities,
       "rsRegistration": rsRegistration,
       "rsRegModules": rsRegModules,
       "rsRegBroadcast": rsRegBroadcast,
       "rsRegBroadcastMeasurement": rsRegBroadcastMeasurement,
       "rsRegBroadcastTransmitter": rsRegBroadcastTransmitter}
)
