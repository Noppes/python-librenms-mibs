# SNMP MIB module (RADIUS-AUTH-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\RADIUS-AUTH-CLIENT-MIB

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

radiusAuthClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2)
)
if mibBuilder.loadTexts:
    radiusAuthClientMIB.setRevisions(
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
_RadiusAuthentication_ObjectIdentity = ObjectIdentity
radiusAuthentication = _RadiusAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1)
)
_RadiusAuthClientMIBObjects_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBObjects = _RadiusAuthClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1)
)
_RadiusAuthClient_ObjectIdentity = ObjectIdentity
radiusAuthClient = _RadiusAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1)
)
_RadiusAuthClientInvalidServerAddresses_Type = Counter32
_RadiusAuthClientInvalidServerAddresses_Object = MibScalar
radiusAuthClientInvalidServerAddresses = _RadiusAuthClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 1),
    _RadiusAuthClientInvalidServerAddresses_Type()
)
radiusAuthClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientInvalidServerAddresses.setStatus("current")
_RadiusAuthClientIdentifier_Type = SnmpAdminString
_RadiusAuthClientIdentifier_Object = MibScalar
radiusAuthClientIdentifier = _RadiusAuthClientIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 2),
    _RadiusAuthClientIdentifier_Type()
)
radiusAuthClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientIdentifier.setStatus("current")
_RadiusAuthServerTable_Object = MibTable
radiusAuthServerTable = _RadiusAuthServerTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAuthServerTable.setStatus("current")
_RadiusAuthServerEntry_Object = MibTableRow
radiusAuthServerEntry = _RadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1)
)
radiusAuthServerEntry.setIndexNames(
    (0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthServerEntry.setStatus("current")


class _RadiusAuthServerIndex_Type(Integer32):
    """Custom type radiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAuthServerIndex_Type.__name__ = "Integer32"
_RadiusAuthServerIndex_Object = MibTableColumn
radiusAuthServerIndex = _RadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 1),
    _RadiusAuthServerIndex_Type()
)
radiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthServerIndex.setStatus("current")
_RadiusAuthServerAddress_Type = IpAddress
_RadiusAuthServerAddress_Object = MibTableColumn
radiusAuthServerAddress = _RadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 2),
    _RadiusAuthServerAddress_Type()
)
radiusAuthServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServerAddress.setStatus("current")


class _RadiusAuthClientServerPortNumber_Type(Integer32):
    """Custom type radiusAuthClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAuthClientServerPortNumber_Type.__name__ = "Integer32"
_RadiusAuthClientServerPortNumber_Object = MibTableColumn
radiusAuthClientServerPortNumber = _RadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 3),
    _RadiusAuthClientServerPortNumber_Type()
)
radiusAuthClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientServerPortNumber.setStatus("current")
_RadiusAuthClientRoundTripTime_Type = TimeTicks
_RadiusAuthClientRoundTripTime_Object = MibTableColumn
radiusAuthClientRoundTripTime = _RadiusAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 4),
    _RadiusAuthClientRoundTripTime_Type()
)
radiusAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientRoundTripTime.setStatus("current")
_RadiusAuthClientAccessRequests_Type = Counter32
_RadiusAuthClientAccessRequests_Object = MibTableColumn
radiusAuthClientAccessRequests = _RadiusAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 5),
    _RadiusAuthClientAccessRequests_Type()
)
radiusAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRequests.setStatus("current")
_RadiusAuthClientAccessRetransmissions_Type = Counter32
_RadiusAuthClientAccessRetransmissions_Object = MibTableColumn
radiusAuthClientAccessRetransmissions = _RadiusAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 6),
    _RadiusAuthClientAccessRetransmissions_Type()
)
radiusAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRetransmissions.setStatus("current")
_RadiusAuthClientAccessAccepts_Type = Counter32
_RadiusAuthClientAccessAccepts_Object = MibTableColumn
radiusAuthClientAccessAccepts = _RadiusAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 7),
    _RadiusAuthClientAccessAccepts_Type()
)
radiusAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessAccepts.setStatus("current")
_RadiusAuthClientAccessRejects_Type = Counter32
_RadiusAuthClientAccessRejects_Object = MibTableColumn
radiusAuthClientAccessRejects = _RadiusAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 8),
    _RadiusAuthClientAccessRejects_Type()
)
radiusAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessRejects.setStatus("current")
_RadiusAuthClientAccessChallenges_Type = Counter32
_RadiusAuthClientAccessChallenges_Object = MibTableColumn
radiusAuthClientAccessChallenges = _RadiusAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 9),
    _RadiusAuthClientAccessChallenges_Type()
)
radiusAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientAccessChallenges.setStatus("current")
_RadiusAuthClientMalformedAccessResponses_Type = Counter32
_RadiusAuthClientMalformedAccessResponses_Object = MibTableColumn
radiusAuthClientMalformedAccessResponses = _RadiusAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 10),
    _RadiusAuthClientMalformedAccessResponses_Type()
)
radiusAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientMalformedAccessResponses.setStatus("current")
_RadiusAuthClientBadAuthenticators_Type = Counter32
_RadiusAuthClientBadAuthenticators_Object = MibTableColumn
radiusAuthClientBadAuthenticators = _RadiusAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 11),
    _RadiusAuthClientBadAuthenticators_Type()
)
radiusAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientBadAuthenticators.setStatus("current")
_RadiusAuthClientPendingRequests_Type = Gauge32
_RadiusAuthClientPendingRequests_Object = MibTableColumn
radiusAuthClientPendingRequests = _RadiusAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 12),
    _RadiusAuthClientPendingRequests_Type()
)
radiusAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientPendingRequests.setStatus("current")
_RadiusAuthClientTimeouts_Type = Counter32
_RadiusAuthClientTimeouts_Object = MibTableColumn
radiusAuthClientTimeouts = _RadiusAuthClientTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 13),
    _RadiusAuthClientTimeouts_Type()
)
radiusAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientTimeouts.setStatus("current")
_RadiusAuthClientUnknownTypes_Type = Counter32
_RadiusAuthClientUnknownTypes_Object = MibTableColumn
radiusAuthClientUnknownTypes = _RadiusAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 14),
    _RadiusAuthClientUnknownTypes_Type()
)
radiusAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientUnknownTypes.setStatus("current")
_RadiusAuthClientPacketsDropped_Type = Counter32
_RadiusAuthClientPacketsDropped_Object = MibTableColumn
radiusAuthClientPacketsDropped = _RadiusAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 15),
    _RadiusAuthClientPacketsDropped_Type()
)
radiusAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthClientPacketsDropped.setStatus("current")
_RadiusAuthClientMIBConformance_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBConformance = _RadiusAuthClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2)
)
_RadiusAuthClientMIBCompliances_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBCompliances = _RadiusAuthClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1)
)
_RadiusAuthClientMIBGroups_ObjectIdentity = ObjectIdentity
radiusAuthClientMIBGroups = _RadiusAuthClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2)
)

# Managed Objects groups

radiusAuthClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 1)
)
radiusAuthClientMIBGroup.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientRoundTripTime"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRequests"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRetransmissions"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessAccepts"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRejects"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessChallenges"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMalformedAccessResponses"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientBadAuthenticators"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPendingRequests"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientTimeouts"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientUnknownTypes"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPacketsDropped"))
)
if mibBuilder.loadTexts:
    radiusAuthClientMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusAuthClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 1)
)
radiusAuthClientMIBCompliance.setObjects(
    ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMIBGroup")
)
if mibBuilder.loadTexts:
    radiusAuthClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    **{"radiusMIB": radiusMIB,
       "radiusAuthentication": radiusAuthentication,
       "radiusAuthClientMIB": radiusAuthClientMIB,
       "radiusAuthClientMIBObjects": radiusAuthClientMIBObjects,
       "radiusAuthClient": radiusAuthClient,
       "radiusAuthClientInvalidServerAddresses": radiusAuthClientInvalidServerAddresses,
       "radiusAuthClientIdentifier": radiusAuthClientIdentifier,
       "radiusAuthServerTable": radiusAuthServerTable,
       "radiusAuthServerEntry": radiusAuthServerEntry,
       "radiusAuthServerIndex": radiusAuthServerIndex,
       "radiusAuthServerAddress": radiusAuthServerAddress,
       "radiusAuthClientServerPortNumber": radiusAuthClientServerPortNumber,
       "radiusAuthClientRoundTripTime": radiusAuthClientRoundTripTime,
       "radiusAuthClientAccessRequests": radiusAuthClientAccessRequests,
       "radiusAuthClientAccessRetransmissions": radiusAuthClientAccessRetransmissions,
       "radiusAuthClientAccessAccepts": radiusAuthClientAccessAccepts,
       "radiusAuthClientAccessRejects": radiusAuthClientAccessRejects,
       "radiusAuthClientAccessChallenges": radiusAuthClientAccessChallenges,
       "radiusAuthClientMalformedAccessResponses": radiusAuthClientMalformedAccessResponses,
       "radiusAuthClientBadAuthenticators": radiusAuthClientBadAuthenticators,
       "radiusAuthClientPendingRequests": radiusAuthClientPendingRequests,
       "radiusAuthClientTimeouts": radiusAuthClientTimeouts,
       "radiusAuthClientUnknownTypes": radiusAuthClientUnknownTypes,
       "radiusAuthClientPacketsDropped": radiusAuthClientPacketsDropped,
       "radiusAuthClientMIBConformance": radiusAuthClientMIBConformance,
       "radiusAuthClientMIBCompliances": radiusAuthClientMIBCompliances,
       "radiusAuthClientMIBCompliance": radiusAuthClientMIBCompliance,
       "radiusAuthClientMIBGroups": radiusAuthClientMIBGroups,
       "radiusAuthClientMIBGroup": radiusAuthClientMIBGroup}
)
