# SNMP MIB module (AcPerfMediaGateway) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\audiocodes\AcPerfMediaGateway

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

acPerfMediaGateway = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1)
)
if mibBuilder.loadTexts:
    acPerfMediaGateway.setRevisions(
        ("2021-02-16 09:55",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcRegistrations_ObjectIdentity = ObjectIdentity
acRegistrations = _AcRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 7)
)
_AcGeneric_ObjectIdentity = ObjectIdentity
acGeneric = _AcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8)
)
_AcProducts_ObjectIdentity = ObjectIdentity
acProducts = _AcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9)
)
_AcPerformance_ObjectIdentity = ObjectIdentity
acPerformance = _AcPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10)
)
_AcPerfCp_ObjectIdentity = ObjectIdentity
acPerfCp = _AcPerfCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1)
)
_AcPerfCpNumDupsForCompletedTransactions_Type = Counter32
_AcPerfCpNumDupsForCompletedTransactions_Object = MibScalar
acPerfCpNumDupsForCompletedTransactions = _AcPerfCpNumDupsForCompletedTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 1),
    _AcPerfCpNumDupsForCompletedTransactions_Type()
)
acPerfCpNumDupsForCompletedTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpNumDupsForCompletedTransactions.setStatus("obsolete")
_AcPerfCpNumDupsForOutstandingTransactions_Type = Counter32
_AcPerfCpNumDupsForOutstandingTransactions_Object = MibScalar
acPerfCpNumDupsForOutstandingTransactions = _AcPerfCpNumDupsForOutstandingTransactions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 2),
    _AcPerfCpNumDupsForOutstandingTransactions_Type()
)
acPerfCpNumDupsForOutstandingTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpNumDupsForOutstandingTransactions.setStatus("obsolete")
_AcPerfCpMessageSendSuccesses_Type = Counter32
_AcPerfCpMessageSendSuccesses_Object = MibScalar
acPerfCpMessageSendSuccesses = _AcPerfCpMessageSendSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 3),
    _AcPerfCpMessageSendSuccesses_Type()
)
acPerfCpMessageSendSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpMessageSendSuccesses.setStatus("obsolete")
_AcPerfCpMessageSendErrors_Type = Counter32
_AcPerfCpMessageSendErrors_Object = MibScalar
acPerfCpMessageSendErrors = _AcPerfCpMessageSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 4),
    _AcPerfCpMessageSendErrors_Type()
)
acPerfCpMessageSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpMessageSendErrors.setStatus("obsolete")
_AcPerfCpMessageReceiveSuccesses_Type = Counter32
_AcPerfCpMessageReceiveSuccesses_Object = MibScalar
acPerfCpMessageReceiveSuccesses = _AcPerfCpMessageReceiveSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 5),
    _AcPerfCpMessageReceiveSuccesses_Type()
)
acPerfCpMessageReceiveSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpMessageReceiveSuccesses.setStatus("obsolete")
_AcPerfCpMessageReceiveErrors_Type = Counter32
_AcPerfCpMessageReceiveErrors_Object = MibScalar
acPerfCpMessageReceiveErrors = _AcPerfCpMessageReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 6),
    _AcPerfCpMessageReceiveErrors_Type()
)
acPerfCpMessageReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpMessageReceiveErrors.setStatus("obsolete")
_AcPerfCpProtocolSyntaxErrors_Type = Counter32
_AcPerfCpProtocolSyntaxErrors_Object = MibScalar
acPerfCpProtocolSyntaxErrors = _AcPerfCpProtocolSyntaxErrors_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 7),
    _AcPerfCpProtocolSyntaxErrors_Type()
)
acPerfCpProtocolSyntaxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpProtocolSyntaxErrors.setStatus("obsolete")
_AcPerfCpMessageRetransmissions_Type = Counter32
_AcPerfCpMessageRetransmissions_Object = MibScalar
acPerfCpMessageRetransmissions = _AcPerfCpMessageRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 8),
    _AcPerfCpMessageRetransmissions_Type()
)
acPerfCpMessageRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpMessageRetransmissions.setStatus("obsolete")
_AcPerfCpMessageMaxRetransmissionsExceeded_Type = Counter32
_AcPerfCpMessageMaxRetransmissionsExceeded_Object = MibScalar
acPerfCpMessageMaxRetransmissionsExceeded = _AcPerfCpMessageMaxRetransmissionsExceeded_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 9),
    _AcPerfCpMessageMaxRetransmissionsExceeded_Type()
)
acPerfCpMessageMaxRetransmissionsExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpMessageMaxRetransmissionsExceeded.setStatus("obsolete")
_AcPerfCpMessagesFromUntrustedSources_Type = Counter32
_AcPerfCpMessagesFromUntrustedSources_Object = MibScalar
acPerfCpMessagesFromUntrustedSources = _AcPerfCpMessagesFromUntrustedSources_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 1, 10),
    _AcPerfCpMessagesFromUntrustedSources_Type()
)
acPerfCpMessagesFromUntrustedSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfCpMessagesFromUntrustedSources.setStatus("obsolete")
_AcPerfRtp_ObjectIdentity = ObjectIdentity
acPerfRtp = _AcPerfRtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2)
)
_AcPerfRtpSenderPackets_Type = Counter32
_AcPerfRtpSenderPackets_Object = MibScalar
acPerfRtpSenderPackets = _AcPerfRtpSenderPackets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 1),
    _AcPerfRtpSenderPackets_Type()
)
acPerfRtpSenderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpSenderPackets.setStatus("obsolete")
_AcPerfRtpSenderOctets_Type = Counter32
_AcPerfRtpSenderOctets_Object = MibScalar
acPerfRtpSenderOctets = _AcPerfRtpSenderOctets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 2),
    _AcPerfRtpSenderOctets_Type()
)
acPerfRtpSenderOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpSenderOctets.setStatus("obsolete")
_AcPerfRtpReceiverPackets_Type = Counter32
_AcPerfRtpReceiverPackets_Object = MibScalar
acPerfRtpReceiverPackets = _AcPerfRtpReceiverPackets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 3),
    _AcPerfRtpReceiverPackets_Type()
)
acPerfRtpReceiverPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpReceiverPackets.setStatus("obsolete")
_AcPerfRtpReceiverOctets_Type = Counter32
_AcPerfRtpReceiverOctets_Object = MibScalar
acPerfRtpReceiverOctets = _AcPerfRtpReceiverOctets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 4),
    _AcPerfRtpReceiverOctets_Type()
)
acPerfRtpReceiverOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpReceiverOctets.setStatus("obsolete")
_AcPerfRtpRcvrLostPackets_Type = Counter32
_AcPerfRtpRcvrLostPackets_Object = MibScalar
acPerfRtpRcvrLostPackets = _AcPerfRtpRcvrLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 5),
    _AcPerfRtpRcvrLostPackets_Type()
)
acPerfRtpRcvrLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpRcvrLostPackets.setStatus("obsolete")
_AcPerfRtpFailedDueToLackOfResources_Type = Counter32
_AcPerfRtpFailedDueToLackOfResources_Object = MibScalar
acPerfRtpFailedDueToLackOfResources = _AcPerfRtpFailedDueToLackOfResources_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 6),
    _AcPerfRtpFailedDueToLackOfResources_Type()
)
acPerfRtpFailedDueToLackOfResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpFailedDueToLackOfResources.setStatus("obsolete")
_AcPerfRtpSimplexInSessionsTotal_Type = Counter32
_AcPerfRtpSimplexInSessionsTotal_Object = MibScalar
acPerfRtpSimplexInSessionsTotal = _AcPerfRtpSimplexInSessionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 7),
    _AcPerfRtpSimplexInSessionsTotal_Type()
)
acPerfRtpSimplexInSessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpSimplexInSessionsTotal.setStatus("obsolete")
_AcPerfRtpSimplexInSessionsCurrent_Type = Gauge32
_AcPerfRtpSimplexInSessionsCurrent_Object = MibScalar
acPerfRtpSimplexInSessionsCurrent = _AcPerfRtpSimplexInSessionsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 8),
    _AcPerfRtpSimplexInSessionsCurrent_Type()
)
acPerfRtpSimplexInSessionsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpSimplexInSessionsCurrent.setStatus("obsolete")
_AcPerfRtpSimplexOutSessionsTotal_Type = Counter32
_AcPerfRtpSimplexOutSessionsTotal_Object = MibScalar
acPerfRtpSimplexOutSessionsTotal = _AcPerfRtpSimplexOutSessionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 9),
    _AcPerfRtpSimplexOutSessionsTotal_Type()
)
acPerfRtpSimplexOutSessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpSimplexOutSessionsTotal.setStatus("obsolete")
_AcPerfRtpSimplexOutSessionsCurrent_Type = Gauge32
_AcPerfRtpSimplexOutSessionsCurrent_Object = MibScalar
acPerfRtpSimplexOutSessionsCurrent = _AcPerfRtpSimplexOutSessionsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 10),
    _AcPerfRtpSimplexOutSessionsCurrent_Type()
)
acPerfRtpSimplexOutSessionsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpSimplexOutSessionsCurrent.setStatus("obsolete")
_AcPerfRtpDuplexSessionsTotal_Type = Counter32
_AcPerfRtpDuplexSessionsTotal_Object = MibScalar
acPerfRtpDuplexSessionsTotal = _AcPerfRtpDuplexSessionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 11),
    _AcPerfRtpDuplexSessionsTotal_Type()
)
acPerfRtpDuplexSessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpDuplexSessionsTotal.setStatus("obsolete")
_AcPerfRtpDuplexSessionsCurrent_Type = Gauge32
_AcPerfRtpDuplexSessionsCurrent_Object = MibScalar
acPerfRtpDuplexSessionsCurrent = _AcPerfRtpDuplexSessionsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 2, 12),
    _AcPerfRtpDuplexSessionsCurrent_Type()
)
acPerfRtpDuplexSessionsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfRtpDuplexSessionsCurrent.setStatus("obsolete")
_AcPerfSystem_ObjectIdentity = ObjectIdentity
acPerfSystem = _AcPerfSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 3)
)
_AcPerfSystemPacketEndpoints_Type = Gauge32
_AcPerfSystemPacketEndpoints_Object = MibScalar
acPerfSystemPacketEndpoints = _AcPerfSystemPacketEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 3, 1),
    _AcPerfSystemPacketEndpoints_Type()
)
acPerfSystemPacketEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfSystemPacketEndpoints.setStatus("obsolete")
_AcPerfSystemPacketEndpointsInUse_Type = Gauge32
_AcPerfSystemPacketEndpointsInUse_Object = MibScalar
acPerfSystemPacketEndpointsInUse = _AcPerfSystemPacketEndpointsInUse_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 1, 3, 2),
    _AcPerfSystemPacketEndpointsInUse_Type()
)
acPerfSystemPacketEndpointsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfSystemPacketEndpointsInUse.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AcPerfMediaGateway",
    **{"audioCodes": audioCodes,
       "acRegistrations": acRegistrations,
       "acGeneric": acGeneric,
       "acProducts": acProducts,
       "acPerformance": acPerformance,
       "acPerfMediaGateway": acPerfMediaGateway,
       "acPerfCp": acPerfCp,
       "acPerfCpNumDupsForCompletedTransactions": acPerfCpNumDupsForCompletedTransactions,
       "acPerfCpNumDupsForOutstandingTransactions": acPerfCpNumDupsForOutstandingTransactions,
       "acPerfCpMessageSendSuccesses": acPerfCpMessageSendSuccesses,
       "acPerfCpMessageSendErrors": acPerfCpMessageSendErrors,
       "acPerfCpMessageReceiveSuccesses": acPerfCpMessageReceiveSuccesses,
       "acPerfCpMessageReceiveErrors": acPerfCpMessageReceiveErrors,
       "acPerfCpProtocolSyntaxErrors": acPerfCpProtocolSyntaxErrors,
       "acPerfCpMessageRetransmissions": acPerfCpMessageRetransmissions,
       "acPerfCpMessageMaxRetransmissionsExceeded": acPerfCpMessageMaxRetransmissionsExceeded,
       "acPerfCpMessagesFromUntrustedSources": acPerfCpMessagesFromUntrustedSources,
       "acPerfRtp": acPerfRtp,
       "acPerfRtpSenderPackets": acPerfRtpSenderPackets,
       "acPerfRtpSenderOctets": acPerfRtpSenderOctets,
       "acPerfRtpReceiverPackets": acPerfRtpReceiverPackets,
       "acPerfRtpReceiverOctets": acPerfRtpReceiverOctets,
       "acPerfRtpRcvrLostPackets": acPerfRtpRcvrLostPackets,
       "acPerfRtpFailedDueToLackOfResources": acPerfRtpFailedDueToLackOfResources,
       "acPerfRtpSimplexInSessionsTotal": acPerfRtpSimplexInSessionsTotal,
       "acPerfRtpSimplexInSessionsCurrent": acPerfRtpSimplexInSessionsCurrent,
       "acPerfRtpSimplexOutSessionsTotal": acPerfRtpSimplexOutSessionsTotal,
       "acPerfRtpSimplexOutSessionsCurrent": acPerfRtpSimplexOutSessionsCurrent,
       "acPerfRtpDuplexSessionsTotal": acPerfRtpDuplexSessionsTotal,
       "acPerfRtpDuplexSessionsCurrent": acPerfRtpDuplexSessionsCurrent,
       "acPerfSystem": acPerfSystem,
       "acPerfSystemPacketEndpoints": acPerfSystemPacketEndpoints,
       "acPerfSystemPacketEndpointsInUse": acPerfSystemPacketEndpointsInUse}
)
