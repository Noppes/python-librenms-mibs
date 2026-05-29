# SNMP MIB module (RADIUS-ACC-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\RADIUS-ACC-CLIENT-MIB

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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

radiusAccClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2)
)
if mibBuilder.loadTexts:
    radiusAccClientMIB.setRevisions(
        ("1999-06-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusMIB_ObjectIdentity = ObjectIdentity
radiusMIB = _RadiusMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67)
)
if mibBuilder.loadTexts:
    radiusMIB.setStatus("current")
_RadiusAccounting_ObjectIdentity = ObjectIdentity
radiusAccounting = _RadiusAccounting_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2)
)
_RadiusAccClientMIBObjects_ObjectIdentity = ObjectIdentity
radiusAccClientMIBObjects = _RadiusAccClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1)
)
_RadiusAccClient_ObjectIdentity = ObjectIdentity
radiusAccClient = _RadiusAccClient_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1)
)
_RadiusAccClientInvalidServerAddresses_Type = Counter32
_RadiusAccClientInvalidServerAddresses_Object = MibScalar
radiusAccClientInvalidServerAddresses = _RadiusAccClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 1),
    _RadiusAccClientInvalidServerAddresses_Type()
)
radiusAccClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientInvalidServerAddresses.setStatus("current")
_RadiusAccClientIdentifier_Type = SnmpAdminString
_RadiusAccClientIdentifier_Object = MibScalar
radiusAccClientIdentifier = _RadiusAccClientIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 2),
    _RadiusAccClientIdentifier_Type()
)
radiusAccClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientIdentifier.setStatus("current")
_RadiusAccServerTable_Object = MibTable
radiusAccServerTable = _RadiusAccServerTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAccServerTable.setStatus("current")
_RadiusAccServerEntry_Object = MibTableRow
radiusAccServerEntry = _RadiusAccServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1)
)
radiusAccServerEntry.setIndexNames(
    (0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAccServerEntry.setStatus("current")


class _RadiusAccServerIndex_Type(Integer32):
    """Custom type radiusAccServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAccServerIndex_Type.__name__ = "Integer32"
_RadiusAccServerIndex_Object = MibTableColumn
radiusAccServerIndex = _RadiusAccServerIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 1),
    _RadiusAccServerIndex_Type()
)
radiusAccServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAccServerIndex.setStatus("current")
_RadiusAccServerAddress_Type = IpAddress
_RadiusAccServerAddress_Object = MibTableColumn
radiusAccServerAddress = _RadiusAccServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 2),
    _RadiusAccServerAddress_Type()
)
radiusAccServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServerAddress.setStatus("current")


class _RadiusAccClientServerPortNumber_Type(Integer32):
    """Custom type radiusAccClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAccClientServerPortNumber_Type.__name__ = "Integer32"
_RadiusAccClientServerPortNumber_Object = MibTableColumn
radiusAccClientServerPortNumber = _RadiusAccClientServerPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 3),
    _RadiusAccClientServerPortNumber_Type()
)
radiusAccClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientServerPortNumber.setStatus("current")
_RadiusAccClientRoundTripTime_Type = TimeTicks
_RadiusAccClientRoundTripTime_Object = MibTableColumn
radiusAccClientRoundTripTime = _RadiusAccClientRoundTripTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 4),
    _RadiusAccClientRoundTripTime_Type()
)
radiusAccClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientRoundTripTime.setStatus("current")
_RadiusAccClientRequests_Type = Counter32
_RadiusAccClientRequests_Object = MibTableColumn
radiusAccClientRequests = _RadiusAccClientRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 5),
    _RadiusAccClientRequests_Type()
)
radiusAccClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientRequests.setStatus("current")
_RadiusAccClientRetransmissions_Type = Counter32
_RadiusAccClientRetransmissions_Object = MibTableColumn
radiusAccClientRetransmissions = _RadiusAccClientRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 6),
    _RadiusAccClientRetransmissions_Type()
)
radiusAccClientRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientRetransmissions.setStatus("current")
_RadiusAccClientResponses_Type = Counter32
_RadiusAccClientResponses_Object = MibTableColumn
radiusAccClientResponses = _RadiusAccClientResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 7),
    _RadiusAccClientResponses_Type()
)
radiusAccClientResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientResponses.setStatus("current")
_RadiusAccClientMalformedResponses_Type = Counter32
_RadiusAccClientMalformedResponses_Object = MibTableColumn
radiusAccClientMalformedResponses = _RadiusAccClientMalformedResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 8),
    _RadiusAccClientMalformedResponses_Type()
)
radiusAccClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientMalformedResponses.setStatus("current")
_RadiusAccClientBadAuthenticators_Type = Counter32
_RadiusAccClientBadAuthenticators_Object = MibTableColumn
radiusAccClientBadAuthenticators = _RadiusAccClientBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 9),
    _RadiusAccClientBadAuthenticators_Type()
)
radiusAccClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientBadAuthenticators.setStatus("current")
_RadiusAccClientPendingRequests_Type = Gauge32
_RadiusAccClientPendingRequests_Object = MibTableColumn
radiusAccClientPendingRequests = _RadiusAccClientPendingRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 10),
    _RadiusAccClientPendingRequests_Type()
)
radiusAccClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientPendingRequests.setStatus("current")
_RadiusAccClientTimeouts_Type = Counter32
_RadiusAccClientTimeouts_Object = MibTableColumn
radiusAccClientTimeouts = _RadiusAccClientTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 11),
    _RadiusAccClientTimeouts_Type()
)
radiusAccClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientTimeouts.setStatus("current")
_RadiusAccClientUnknownTypes_Type = Counter32
_RadiusAccClientUnknownTypes_Object = MibTableColumn
radiusAccClientUnknownTypes = _RadiusAccClientUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 12),
    _RadiusAccClientUnknownTypes_Type()
)
radiusAccClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientUnknownTypes.setStatus("current")
_RadiusAccClientPacketsDropped_Type = Counter32
_RadiusAccClientPacketsDropped_Object = MibTableColumn
radiusAccClientPacketsDropped = _RadiusAccClientPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 13),
    _RadiusAccClientPacketsDropped_Type()
)
radiusAccClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientPacketsDropped.setStatus("current")
_RadiusAccClientMIBConformance_ObjectIdentity = ObjectIdentity
radiusAccClientMIBConformance = _RadiusAccClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2)
)
_RadiusAccClientMIBCompliances_ObjectIdentity = ObjectIdentity
radiusAccClientMIBCompliances = _RadiusAccClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1)
)
_RadiusAccClientMIBGroups_ObjectIdentity = ObjectIdentity
radiusAccClientMIBGroups = _RadiusAccClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2)
)

# Managed Objects groups

radiusAccClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2, 1)
)
radiusAccClientMIBGroup.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccClientIdentifier"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientInvalidServerAddresses"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRoundTripTime"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRequests"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientRetransmissions"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientResponses"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientMalformedResponses"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientBadAuthenticators"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPendingRequests"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientTimeouts"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientUnknownTypes"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientPacketsDropped"))
)
if mibBuilder.loadTexts:
    radiusAccClientMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusAccClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1, 1)
)
radiusAccClientMIBCompliance.setObjects(
    ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientMIBGroup")
)
if mibBuilder.loadTexts:
    radiusAccClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    **{"radiusMIB": radiusMIB,
       "radiusAccounting": radiusAccounting,
       "radiusAccClientMIB": radiusAccClientMIB,
       "radiusAccClientMIBObjects": radiusAccClientMIBObjects,
       "radiusAccClient": radiusAccClient,
       "radiusAccClientInvalidServerAddresses": radiusAccClientInvalidServerAddresses,
       "radiusAccClientIdentifier": radiusAccClientIdentifier,
       "radiusAccServerTable": radiusAccServerTable,
       "radiusAccServerEntry": radiusAccServerEntry,
       "radiusAccServerIndex": radiusAccServerIndex,
       "radiusAccServerAddress": radiusAccServerAddress,
       "radiusAccClientServerPortNumber": radiusAccClientServerPortNumber,
       "radiusAccClientRoundTripTime": radiusAccClientRoundTripTime,
       "radiusAccClientRequests": radiusAccClientRequests,
       "radiusAccClientRetransmissions": radiusAccClientRetransmissions,
       "radiusAccClientResponses": radiusAccClientResponses,
       "radiusAccClientMalformedResponses": radiusAccClientMalformedResponses,
       "radiusAccClientBadAuthenticators": radiusAccClientBadAuthenticators,
       "radiusAccClientPendingRequests": radiusAccClientPendingRequests,
       "radiusAccClientTimeouts": radiusAccClientTimeouts,
       "radiusAccClientUnknownTypes": radiusAccClientUnknownTypes,
       "radiusAccClientPacketsDropped": radiusAccClientPacketsDropped,
       "radiusAccClientMIBConformance": radiusAccClientMIBConformance,
       "radiusAccClientMIBCompliances": radiusAccClientMIBCompliances,
       "radiusAccClientMIBCompliance": radiusAccClientMIBCompliance,
       "radiusAccClientMIBGroups": radiusAccClientMIBGroups,
       "radiusAccClientMIBGroup": radiusAccClientMIBGroup}
)
