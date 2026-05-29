# SNMP MIB module (CISCO-AAA-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-AAA-SERVER-MIB

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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoAAAServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56)
)
if mibBuilder.loadTexts:
    ciscoAAAServerMIB.setRevisions(
        ("2023-04-06 00:00",
         "2023-03-01 00:00",
         "2003-11-17 00:00",
         "2002-03-28 00:00",
         "2000-01-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoAAAProtocol(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("tacacsplus", 1),
          ("radius", 2),
          ("ldap", 3),
          ("kerberos", 4),
          ("ntlm", 5),
          ("sdi", 6),
          ("other", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CAAAServerMIBObjects_ObjectIdentity = ObjectIdentity
cAAAServerMIBObjects = _CAAAServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1)
)
_CasConfig_ObjectIdentity = ObjectIdentity
casConfig = _CasConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1)
)
_CasServerStateChangeEnable_Type = TruthValue
_CasServerStateChangeEnable_Object = MibScalar
casServerStateChangeEnable = _CasServerStateChangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 1),
    _CasServerStateChangeEnable_Type()
)
casServerStateChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casServerStateChangeEnable.setStatus("current")
_CasConfigTable_Object = MibTable
casConfigTable = _CasConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2)
)
if mibBuilder.loadTexts:
    casConfigTable.setStatus("current")
_CasConfigEntry_Object = MibTableRow
casConfigEntry = _CasConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1)
)
casConfigEntry.setIndexNames(
    (0, "CISCO-AAA-SERVER-MIB", "casProtocol"),
    (0, "CISCO-AAA-SERVER-MIB", "casIndex"),
)
if mibBuilder.loadTexts:
    casConfigEntry.setStatus("current")
_CasProtocol_Type = CiscoAAAProtocol
_CasProtocol_Object = MibTableColumn
casProtocol = _CasProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 1),
    _CasProtocol_Type()
)
casProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casProtocol.setStatus("current")


class _CasIndex_Type(Unsigned32):
    """Custom type casIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CasIndex_Type.__name__ = "Unsigned32"
_CasIndex_Object = MibTableColumn
casIndex = _CasIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 2),
    _CasIndex_Type()
)
casIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casIndex.setStatus("current")
_CasAddress_Type = IpAddress
_CasAddress_Object = MibTableColumn
casAddress = _CasAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 3),
    _CasAddress_Type()
)
casAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casAddress.setStatus("current")


class _CasAuthenPort_Type(Integer32):
    """Custom type casAuthenPort based on Integer32"""
    defaultValue = 1645

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CasAuthenPort_Type.__name__ = "Integer32"
_CasAuthenPort_Object = MibTableColumn
casAuthenPort = _CasAuthenPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 4),
    _CasAuthenPort_Type()
)
casAuthenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casAuthenPort.setStatus("current")


class _CasAcctPort_Type(Integer32):
    """Custom type casAcctPort based on Integer32"""
    defaultValue = 1646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CasAcctPort_Type.__name__ = "Integer32"
_CasAcctPort_Object = MibTableColumn
casAcctPort = _CasAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 5),
    _CasAcctPort_Type()
)
casAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casAcctPort.setStatus("current")


class _CasKey_Type(DisplayString):
    """Custom type casKey based on DisplayString"""
    defaultValue = OctetString("")


_CasKey_Type.__name__ = "DisplayString"
_CasKey_Object = MibTableColumn
casKey = _CasKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 6),
    _CasKey_Type()
)
casKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casKey.setStatus("current")


class _CasPriority_Type(Unsigned32):
    """Custom type casPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CasPriority_Type.__name__ = "Unsigned32"
_CasPriority_Object = MibTableColumn
casPriority = _CasPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 7),
    _CasPriority_Type()
)
casPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casPriority.setStatus("current")
_CasConfigRowStatus_Type = RowStatus
_CasConfigRowStatus_Object = MibTableColumn
casConfigRowStatus = _CasConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 8),
    _CasConfigRowStatus_Type()
)
casConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casConfigRowStatus.setStatus("current")
_CasStatistics_ObjectIdentity = ObjectIdentity
casStatistics = _CasStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2)
)
_CasStatisticsTable_Object = MibTable
casStatisticsTable = _CasStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1)
)
if mibBuilder.loadTexts:
    casStatisticsTable.setStatus("current")
_CasStatisticsEntry_Object = MibTableRow
casStatisticsEntry = _CasStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    casStatisticsEntry.setStatus("current")
_CasAuthenRequests_Type = Counter32
_CasAuthenRequests_Object = MibTableColumn
casAuthenRequests = _CasAuthenRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 1),
    _CasAuthenRequests_Type()
)
casAuthenRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenRequests.setStatus("current")
_CasAuthenRequestTimeouts_Type = Counter32
_CasAuthenRequestTimeouts_Object = MibTableColumn
casAuthenRequestTimeouts = _CasAuthenRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 2),
    _CasAuthenRequestTimeouts_Type()
)
casAuthenRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenRequestTimeouts.setStatus("current")
_CasAuthenUnexpectedResponses_Type = Counter32
_CasAuthenUnexpectedResponses_Object = MibTableColumn
casAuthenUnexpectedResponses = _CasAuthenUnexpectedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 3),
    _CasAuthenUnexpectedResponses_Type()
)
casAuthenUnexpectedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenUnexpectedResponses.setStatus("current")
_CasAuthenServerErrorResponses_Type = Counter32
_CasAuthenServerErrorResponses_Object = MibTableColumn
casAuthenServerErrorResponses = _CasAuthenServerErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 4),
    _CasAuthenServerErrorResponses_Type()
)
casAuthenServerErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenServerErrorResponses.setStatus("current")
_CasAuthenIncorrectResponses_Type = Counter32
_CasAuthenIncorrectResponses_Object = MibTableColumn
casAuthenIncorrectResponses = _CasAuthenIncorrectResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 5),
    _CasAuthenIncorrectResponses_Type()
)
casAuthenIncorrectResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenIncorrectResponses.setStatus("current")
_CasAuthenResponseTime_Type = TimeInterval
_CasAuthenResponseTime_Object = MibTableColumn
casAuthenResponseTime = _CasAuthenResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 6),
    _CasAuthenResponseTime_Type()
)
casAuthenResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenResponseTime.setStatus("current")
_CasAuthenTransactionSuccesses_Type = Counter32
_CasAuthenTransactionSuccesses_Object = MibTableColumn
casAuthenTransactionSuccesses = _CasAuthenTransactionSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 7),
    _CasAuthenTransactionSuccesses_Type()
)
casAuthenTransactionSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenTransactionSuccesses.setStatus("current")
_CasAuthenTransactionFailures_Type = Counter32
_CasAuthenTransactionFailures_Object = MibTableColumn
casAuthenTransactionFailures = _CasAuthenTransactionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 8),
    _CasAuthenTransactionFailures_Type()
)
casAuthenTransactionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenTransactionFailures.setStatus("current")
_CasAuthorRequests_Type = Counter32
_CasAuthorRequests_Object = MibTableColumn
casAuthorRequests = _CasAuthorRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 9),
    _CasAuthorRequests_Type()
)
casAuthorRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorRequests.setStatus("current")
_CasAuthorRequestTimeouts_Type = Counter32
_CasAuthorRequestTimeouts_Object = MibTableColumn
casAuthorRequestTimeouts = _CasAuthorRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 10),
    _CasAuthorRequestTimeouts_Type()
)
casAuthorRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorRequestTimeouts.setStatus("current")
_CasAuthorUnexpectedResponses_Type = Counter32
_CasAuthorUnexpectedResponses_Object = MibTableColumn
casAuthorUnexpectedResponses = _CasAuthorUnexpectedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 11),
    _CasAuthorUnexpectedResponses_Type()
)
casAuthorUnexpectedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorUnexpectedResponses.setStatus("current")
_CasAuthorServerErrorResponses_Type = Counter32
_CasAuthorServerErrorResponses_Object = MibTableColumn
casAuthorServerErrorResponses = _CasAuthorServerErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 12),
    _CasAuthorServerErrorResponses_Type()
)
casAuthorServerErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorServerErrorResponses.setStatus("current")
_CasAuthorIncorrectResponses_Type = Counter32
_CasAuthorIncorrectResponses_Object = MibTableColumn
casAuthorIncorrectResponses = _CasAuthorIncorrectResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 13),
    _CasAuthorIncorrectResponses_Type()
)
casAuthorIncorrectResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorIncorrectResponses.setStatus("current")
_CasAuthorResponseTime_Type = TimeInterval
_CasAuthorResponseTime_Object = MibTableColumn
casAuthorResponseTime = _CasAuthorResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 14),
    _CasAuthorResponseTime_Type()
)
casAuthorResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorResponseTime.setStatus("current")
_CasAuthorTransactionSuccesses_Type = Counter32
_CasAuthorTransactionSuccesses_Object = MibTableColumn
casAuthorTransactionSuccesses = _CasAuthorTransactionSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 15),
    _CasAuthorTransactionSuccesses_Type()
)
casAuthorTransactionSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorTransactionSuccesses.setStatus("current")
_CasAuthorTransactionFailures_Type = Counter32
_CasAuthorTransactionFailures_Object = MibTableColumn
casAuthorTransactionFailures = _CasAuthorTransactionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 16),
    _CasAuthorTransactionFailures_Type()
)
casAuthorTransactionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorTransactionFailures.setStatus("current")
_CasAcctRequests_Type = Counter32
_CasAcctRequests_Object = MibTableColumn
casAcctRequests = _CasAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 17),
    _CasAcctRequests_Type()
)
casAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctRequests.setStatus("current")
_CasAcctRequestTimeouts_Type = Counter32
_CasAcctRequestTimeouts_Object = MibTableColumn
casAcctRequestTimeouts = _CasAcctRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 18),
    _CasAcctRequestTimeouts_Type()
)
casAcctRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctRequestTimeouts.setStatus("current")
_CasAcctUnexpectedResponses_Type = Counter32
_CasAcctUnexpectedResponses_Object = MibTableColumn
casAcctUnexpectedResponses = _CasAcctUnexpectedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 19),
    _CasAcctUnexpectedResponses_Type()
)
casAcctUnexpectedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctUnexpectedResponses.setStatus("current")
_CasAcctServerErrorResponses_Type = Counter32
_CasAcctServerErrorResponses_Object = MibTableColumn
casAcctServerErrorResponses = _CasAcctServerErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 20),
    _CasAcctServerErrorResponses_Type()
)
casAcctServerErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctServerErrorResponses.setStatus("current")
_CasAcctIncorrectResponses_Type = Counter32
_CasAcctIncorrectResponses_Object = MibTableColumn
casAcctIncorrectResponses = _CasAcctIncorrectResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 21),
    _CasAcctIncorrectResponses_Type()
)
casAcctIncorrectResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctIncorrectResponses.setStatus("current")
_CasAcctResponseTime_Type = TimeInterval
_CasAcctResponseTime_Object = MibTableColumn
casAcctResponseTime = _CasAcctResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 22),
    _CasAcctResponseTime_Type()
)
casAcctResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctResponseTime.setStatus("current")
_CasAcctTransactionSuccesses_Type = Counter32
_CasAcctTransactionSuccesses_Object = MibTableColumn
casAcctTransactionSuccesses = _CasAcctTransactionSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 23),
    _CasAcctTransactionSuccesses_Type()
)
casAcctTransactionSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctTransactionSuccesses.setStatus("current")
_CasAcctTransactionFailures_Type = Counter32
_CasAcctTransactionFailures_Object = MibTableColumn
casAcctTransactionFailures = _CasAcctTransactionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 24),
    _CasAcctTransactionFailures_Type()
)
casAcctTransactionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctTransactionFailures.setStatus("current")


class _CasState_Type(Integer32):
    """Custom type casState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasState_Type.__name__ = "Integer32"
_CasState_Object = MibTableColumn
casState = _CasState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 25),
    _CasState_Type()
)
casState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casState.setStatus("current")
_CasCurrentStateDuration_Type = TimeInterval
_CasCurrentStateDuration_Object = MibTableColumn
casCurrentStateDuration = _CasCurrentStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 26),
    _CasCurrentStateDuration_Type()
)
casCurrentStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casCurrentStateDuration.setStatus("current")
_CasPreviousStateDuration_Type = TimeInterval
_CasPreviousStateDuration_Object = MibTableColumn
casPreviousStateDuration = _CasPreviousStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 27),
    _CasPreviousStateDuration_Type()
)
casPreviousStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casPreviousStateDuration.setStatus("current")
_CasTotalDeadTime_Type = TimeInterval
_CasTotalDeadTime_Object = MibTableColumn
casTotalDeadTime = _CasTotalDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 28),
    _CasTotalDeadTime_Type()
)
casTotalDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casTotalDeadTime.setStatus("current")
_CasDeadCount_Type = Counter32
_CasDeadCount_Object = MibTableColumn
casDeadCount = _CasDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 29),
    _CasDeadCount_Type()
)
casDeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casDeadCount.setStatus("current")


class _CasWiredServerState_Type(Integer32):
    """Custom type casWiredServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasWiredServerState_Type.__name__ = "Integer32"
_CasWiredServerState_Object = MibTableColumn
casWiredServerState = _CasWiredServerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 30),
    _CasWiredServerState_Type()
)
casWiredServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWiredServerState.setStatus("current")
_CasAuthenRetrans_Type = Counter32
_CasAuthenRetrans_Object = MibTableColumn
casAuthenRetrans = _CasAuthenRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 31),
    _CasAuthenRetrans_Type()
)
casAuthenRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenRetrans.setStatus("current")
_CasAuthenRequestFailover_Type = Counter32
_CasAuthenRequestFailover_Object = MibTableColumn
casAuthenRequestFailover = _CasAuthenRequestFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 32),
    _CasAuthenRequestFailover_Type()
)
casAuthenRequestFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenRequestFailover.setStatus("current")
_CasAuthenResponseAccept_Type = Counter32
_CasAuthenResponseAccept_Object = MibTableColumn
casAuthenResponseAccept = _CasAuthenResponseAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 33),
    _CasAuthenResponseAccept_Type()
)
casAuthenResponseAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenResponseAccept.setStatus("current")
_CasAuthenResponseReject_Type = Counter32
_CasAuthenResponseReject_Object = MibTableColumn
casAuthenResponseReject = _CasAuthenResponseReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 34),
    _CasAuthenResponseReject_Type()
)
casAuthenResponseReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenResponseReject.setStatus("current")
_CasAuthenResponseChallenge_Type = Counter32
_CasAuthenResponseChallenge_Object = MibTableColumn
casAuthenResponseChallenge = _CasAuthenResponseChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 35),
    _CasAuthenResponseChallenge_Type()
)
casAuthenResponseChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenResponseChallenge.setStatus("current")
_CasAuthenThrottledTransaction_Type = Counter32
_CasAuthenThrottledTransaction_Object = MibTableColumn
casAuthenThrottledTransaction = _CasAuthenThrottledTransaction_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 36),
    _CasAuthenThrottledTransaction_Type()
)
casAuthenThrottledTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenThrottledTransaction.setStatus("current")
_CasAuthenThrottledTimeout_Type = Counter32
_CasAuthenThrottledTimeout_Object = MibTableColumn
casAuthenThrottledTimeout = _CasAuthenThrottledTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 37),
    _CasAuthenThrottledTimeout_Type()
)
casAuthenThrottledTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenThrottledTimeout.setStatus("current")
_CasAuthenThrottledFailure_Type = Counter32
_CasAuthenThrottledFailure_Object = MibTableColumn
casAuthenThrottledFailure = _CasAuthenThrottledFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 38),
    _CasAuthenThrottledFailure_Type()
)
casAuthenThrottledFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenThrottledFailure.setStatus("current")
_CasAuthenMalformedResponses_Type = Counter32
_CasAuthenMalformedResponses_Object = MibTableColumn
casAuthenMalformedResponses = _CasAuthenMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 39),
    _CasAuthenMalformedResponses_Type()
)
casAuthenMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenMalformedResponses.setStatus("current")
_CasAuthenBadAuthenticators_Type = Counter32
_CasAuthenBadAuthenticators_Object = MibTableColumn
casAuthenBadAuthenticators = _CasAuthenBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 40),
    _CasAuthenBadAuthenticators_Type()
)
casAuthenBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenBadAuthenticators.setStatus("current")
_CasAuthenDot1xTotalResponses_Type = Counter32
_CasAuthenDot1xTotalResponses_Object = MibTableColumn
casAuthenDot1xTotalResponses = _CasAuthenDot1xTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 41),
    _CasAuthenDot1xTotalResponses_Type()
)
casAuthenDot1xTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenDot1xTotalResponses.setStatus("current")
_CasAuthenDot1xAvgResponseTime_Type = TimeInterval
_CasAuthenDot1xAvgResponseTime_Object = MibTableColumn
casAuthenDot1xAvgResponseTime = _CasAuthenDot1xAvgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 42),
    _CasAuthenDot1xAvgResponseTime_Type()
)
casAuthenDot1xAvgResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenDot1xAvgResponseTime.setStatus("current")
_CasAuthenDot1xTransactionTimeouts_Type = Counter32
_CasAuthenDot1xTransactionTimeouts_Object = MibTableColumn
casAuthenDot1xTransactionTimeouts = _CasAuthenDot1xTransactionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 43),
    _CasAuthenDot1xTransactionTimeouts_Type()
)
casAuthenDot1xTransactionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenDot1xTransactionTimeouts.setStatus("current")
_CasAuthenDot1xTransactionFailover_Type = Counter32
_CasAuthenDot1xTransactionFailover_Object = MibTableColumn
casAuthenDot1xTransactionFailover = _CasAuthenDot1xTransactionFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 44),
    _CasAuthenDot1xTransactionFailover_Type()
)
casAuthenDot1xTransactionFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenDot1xTransactionFailover.setStatus("current")
_CasAuthenDot1xTransactionTotal_Type = Counter32
_CasAuthenDot1xTransactionTotal_Object = MibTableColumn
casAuthenDot1xTransactionTotal = _CasAuthenDot1xTransactionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 45),
    _CasAuthenDot1xTransactionTotal_Type()
)
casAuthenDot1xTransactionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenDot1xTransactionTotal.setStatus("current")
_CasAuthenDot1xTransactionSuccess_Type = Counter32
_CasAuthenDot1xTransactionSuccess_Object = MibTableColumn
casAuthenDot1xTransactionSuccess = _CasAuthenDot1xTransactionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 46),
    _CasAuthenDot1xTransactionSuccess_Type()
)
casAuthenDot1xTransactionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenDot1xTransactionSuccess.setStatus("current")
_CasAuthenDot1xTransactionFailure_Type = Counter32
_CasAuthenDot1xTransactionFailure_Object = MibTableColumn
casAuthenDot1xTransactionFailure = _CasAuthenDot1xTransactionFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 47),
    _CasAuthenDot1xTransactionFailure_Type()
)
casAuthenDot1xTransactionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenDot1xTransactionFailure.setStatus("current")
_CasAuthenMACTotalResponses_Type = Counter32
_CasAuthenMACTotalResponses_Object = MibTableColumn
casAuthenMACTotalResponses = _CasAuthenMACTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 48),
    _CasAuthenMACTotalResponses_Type()
)
casAuthenMACTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenMACTotalResponses.setStatus("current")
_CasAuthenMACAvgResponseTime_Type = TimeInterval
_CasAuthenMACAvgResponseTime_Object = MibTableColumn
casAuthenMACAvgResponseTime = _CasAuthenMACAvgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 49),
    _CasAuthenMACAvgResponseTime_Type()
)
casAuthenMACAvgResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenMACAvgResponseTime.setStatus("current")
_CasAuthenMACTransactionTimeouts_Type = Counter32
_CasAuthenMACTransactionTimeouts_Object = MibTableColumn
casAuthenMACTransactionTimeouts = _CasAuthenMACTransactionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 50),
    _CasAuthenMACTransactionTimeouts_Type()
)
casAuthenMACTransactionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenMACTransactionTimeouts.setStatus("current")
_CasAuthenMACTransactionFailover_Type = Counter32
_CasAuthenMACTransactionFailover_Object = MibTableColumn
casAuthenMACTransactionFailover = _CasAuthenMACTransactionFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 51),
    _CasAuthenMACTransactionFailover_Type()
)
casAuthenMACTransactionFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenMACTransactionFailover.setStatus("current")
_CasAuthenMACTransactionTotal_Type = Counter32
_CasAuthenMACTransactionTotal_Object = MibTableColumn
casAuthenMACTransactionTotal = _CasAuthenMACTransactionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 52),
    _CasAuthenMACTransactionTotal_Type()
)
casAuthenMACTransactionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenMACTransactionTotal.setStatus("current")
_CasAuthenMACTransactionSuccess_Type = Counter32
_CasAuthenMACTransactionSuccess_Object = MibTableColumn
casAuthenMACTransactionSuccess = _CasAuthenMACTransactionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 53),
    _CasAuthenMACTransactionSuccess_Type()
)
casAuthenMACTransactionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenMACTransactionSuccess.setStatus("current")
_CasAuthenMACTransactionFailure_Type = Counter32
_CasAuthenMACTransactionFailure_Object = MibTableColumn
casAuthenMACTransactionFailure = _CasAuthenMACTransactionFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 54),
    _CasAuthenMACTransactionFailure_Type()
)
casAuthenMACTransactionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthenMACTransactionFailure.setStatus("current")
_CasAuthorRequestFailover_Type = Counter32
_CasAuthorRequestFailover_Object = MibTableColumn
casAuthorRequestFailover = _CasAuthorRequestFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 55),
    _CasAuthorRequestFailover_Type()
)
casAuthorRequestFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorRequestFailover.setStatus("current")
_CasAuthorRequestRetransmission_Type = Counter32
_CasAuthorRequestRetransmission_Object = MibTableColumn
casAuthorRequestRetransmission = _CasAuthorRequestRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 56),
    _CasAuthorRequestRetransmission_Type()
)
casAuthorRequestRetransmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorRequestRetransmission.setStatus("current")
_CasAuthorResponseAccept_Type = Counter32
_CasAuthorResponseAccept_Object = MibTableColumn
casAuthorResponseAccept = _CasAuthorResponseAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 57),
    _CasAuthorResponseAccept_Type()
)
casAuthorResponseAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorResponseAccept.setStatus("current")
_CasAuthorResponseReject_Type = Counter32
_CasAuthorResponseReject_Object = MibTableColumn
casAuthorResponseReject = _CasAuthorResponseReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 58),
    _CasAuthorResponseReject_Type()
)
casAuthorResponseReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorResponseReject.setStatus("current")
_CasAuthorResponseChallenge_Type = Counter32
_CasAuthorResponseChallenge_Object = MibTableColumn
casAuthorResponseChallenge = _CasAuthorResponseChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 59),
    _CasAuthorResponseChallenge_Type()
)
casAuthorResponseChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorResponseChallenge.setStatus("current")
_CasAuthorThrottledTransaction_Type = Counter32
_CasAuthorThrottledTransaction_Object = MibTableColumn
casAuthorThrottledTransaction = _CasAuthorThrottledTransaction_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 60),
    _CasAuthorThrottledTransaction_Type()
)
casAuthorThrottledTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorThrottledTransaction.setStatus("current")
_CasAuthorThrottledTimeout_Type = Counter32
_CasAuthorThrottledTimeout_Object = MibTableColumn
casAuthorThrottledTimeout = _CasAuthorThrottledTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 61),
    _CasAuthorThrottledTimeout_Type()
)
casAuthorThrottledTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorThrottledTimeout.setStatus("current")
_CasAuthorThrottledFailure_Type = Counter32
_CasAuthorThrottledFailure_Object = MibTableColumn
casAuthorThrottledFailure = _CasAuthorThrottledFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 62),
    _CasAuthorThrottledFailure_Type()
)
casAuthorThrottledFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorThrottledFailure.setStatus("current")
_CasAuthorMalformedResponses_Type = Counter32
_CasAuthorMalformedResponses_Object = MibTableColumn
casAuthorMalformedResponses = _CasAuthorMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 63),
    _CasAuthorMalformedResponses_Type()
)
casAuthorMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorMalformedResponses.setStatus("current")
_CasAuthorBadAuthenticators_Type = Counter32
_CasAuthorBadAuthenticators_Object = MibTableColumn
casAuthorBadAuthenticators = _CasAuthorBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 64),
    _CasAuthorBadAuthenticators_Type()
)
casAuthorBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorBadAuthenticators.setStatus("current")
_CasAuthorMACTotalResponses_Type = Counter32
_CasAuthorMACTotalResponses_Object = MibTableColumn
casAuthorMACTotalResponses = _CasAuthorMACTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 65),
    _CasAuthorMACTotalResponses_Type()
)
casAuthorMACTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorMACTotalResponses.setStatus("current")
_CasAuthorMACAvgResponseTime_Type = TimeInterval
_CasAuthorMACAvgResponseTime_Object = MibTableColumn
casAuthorMACAvgResponseTime = _CasAuthorMACAvgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 66),
    _CasAuthorMACAvgResponseTime_Type()
)
casAuthorMACAvgResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorMACAvgResponseTime.setStatus("current")
_CasAuthorMACTransactionTimeouts_Type = Counter32
_CasAuthorMACTransactionTimeouts_Object = MibTableColumn
casAuthorMACTransactionTimeouts = _CasAuthorMACTransactionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 67),
    _CasAuthorMACTransactionTimeouts_Type()
)
casAuthorMACTransactionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorMACTransactionTimeouts.setStatus("current")
_CasAuthorMACTransactionFailover_Type = Counter32
_CasAuthorMACTransactionFailover_Object = MibTableColumn
casAuthorMACTransactionFailover = _CasAuthorMACTransactionFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 68),
    _CasAuthorMACTransactionFailover_Type()
)
casAuthorMACTransactionFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorMACTransactionFailover.setStatus("current")
_CasAuthorMACTransactionTotal_Type = Counter32
_CasAuthorMACTransactionTotal_Object = MibTableColumn
casAuthorMACTransactionTotal = _CasAuthorMACTransactionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 69),
    _CasAuthorMACTransactionTotal_Type()
)
casAuthorMACTransactionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorMACTransactionTotal.setStatus("current")
_CasAuthorMACTransactionSuccess_Type = Counter32
_CasAuthorMACTransactionSuccess_Object = MibTableColumn
casAuthorMACTransactionSuccess = _CasAuthorMACTransactionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 70),
    _CasAuthorMACTransactionSuccess_Type()
)
casAuthorMACTransactionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorMACTransactionSuccess.setStatus("current")
_CasAuthorMACTransactionFailure_Type = Counter32
_CasAuthorMACTransactionFailure_Object = MibTableColumn
casAuthorMACTransactionFailure = _CasAuthorMACTransactionFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 71),
    _CasAuthorMACTransactionFailure_Type()
)
casAuthorMACTransactionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAuthorMACTransactionFailure.setStatus("current")
_CasAcctRequestFailover_Type = Counter32
_CasAcctRequestFailover_Object = MibTableColumn
casAcctRequestFailover = _CasAcctRequestFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 72),
    _CasAcctRequestFailover_Type()
)
casAcctRequestFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctRequestFailover.setStatus("current")
_CasAcctRequestRetransmission_Type = Counter32
_CasAcctRequestRetransmission_Object = MibTableColumn
casAcctRequestRetransmission = _CasAcctRequestRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 73),
    _CasAcctRequestRetransmission_Type()
)
casAcctRequestRetransmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctRequestRetransmission.setStatus("current")
_CasAcctRequestStart_Type = Counter32
_CasAcctRequestStart_Object = MibTableColumn
casAcctRequestStart = _CasAcctRequestStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 74),
    _CasAcctRequestStart_Type()
)
casAcctRequestStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctRequestStart.setStatus("current")
_CasAcctRequestInterim_Type = Counter32
_CasAcctRequestInterim_Object = MibTableColumn
casAcctRequestInterim = _CasAcctRequestInterim_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 75),
    _CasAcctRequestInterim_Type()
)
casAcctRequestInterim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctRequestInterim.setStatus("current")
_CasAcctRequestStop_Type = Counter32
_CasAcctRequestStop_Object = MibTableColumn
casAcctRequestStop = _CasAcctRequestStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 76),
    _CasAcctRequestStop_Type()
)
casAcctRequestStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctRequestStop.setStatus("current")
_CasAcctResponseStart_Type = Counter32
_CasAcctResponseStart_Object = MibTableColumn
casAcctResponseStart = _CasAcctResponseStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 77),
    _CasAcctResponseStart_Type()
)
casAcctResponseStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctResponseStart.setStatus("current")
_CasAcctResponseInterim_Type = Counter32
_CasAcctResponseInterim_Object = MibTableColumn
casAcctResponseInterim = _CasAcctResponseInterim_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 78),
    _CasAcctResponseInterim_Type()
)
casAcctResponseInterim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctResponseInterim.setStatus("current")
_CasAcctResponseStop_Type = Counter32
_CasAcctResponseStop_Object = MibTableColumn
casAcctResponseStop = _CasAcctResponseStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 79),
    _CasAcctResponseStop_Type()
)
casAcctResponseStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctResponseStop.setStatus("current")
_CasAcctThrottledTransaction_Type = Counter32
_CasAcctThrottledTransaction_Object = MibTableColumn
casAcctThrottledTransaction = _CasAcctThrottledTransaction_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 80),
    _CasAcctThrottledTransaction_Type()
)
casAcctThrottledTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctThrottledTransaction.setStatus("current")
_CasAcctThrottledTimeout_Type = Counter32
_CasAcctThrottledTimeout_Object = MibTableColumn
casAcctThrottledTimeout = _CasAcctThrottledTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 81),
    _CasAcctThrottledTimeout_Type()
)
casAcctThrottledTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctThrottledTimeout.setStatus("current")
_CasAcctThrottledFailure_Type = Counter32
_CasAcctThrottledFailure_Object = MibTableColumn
casAcctThrottledFailure = _CasAcctThrottledFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 82),
    _CasAcctThrottledFailure_Type()
)
casAcctThrottledFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctThrottledFailure.setStatus("current")
_CasAcctMalformedResponses_Type = Counter32
_CasAcctMalformedResponses_Object = MibTableColumn
casAcctMalformedResponses = _CasAcctMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 83),
    _CasAcctMalformedResponses_Type()
)
casAcctMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctMalformedResponses.setStatus("current")
_CasAcctBadAuthenticators_Type = Counter32
_CasAcctBadAuthenticators_Object = MibTableColumn
casAcctBadAuthenticators = _CasAcctBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 84),
    _CasAcctBadAuthenticators_Type()
)
casAcctBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casAcctBadAuthenticators.setStatus("current")
_CasWiredDuration_Type = TimeInterval
_CasWiredDuration_Object = MibTableColumn
casWiredDuration = _CasWiredDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 85),
    _CasWiredDuration_Type()
)
casWiredDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWiredDuration.setStatus("current")
_CasWiredPreDuration_Type = TimeInterval
_CasWiredPreDuration_Object = MibTableColumn
casWiredPreDuration = _CasWiredPreDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 86),
    _CasWiredPreDuration_Type()
)
casWiredPreDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWiredPreDuration.setStatus("current")
_CasWiredTotalDeadTime_Type = TimeInterval
_CasWiredTotalDeadTime_Object = MibTableColumn
casWiredTotalDeadTime = _CasWiredTotalDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 87),
    _CasWiredTotalDeadTime_Type()
)
casWiredTotalDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWiredTotalDeadTime.setStatus("current")
_CasWiredDeadCount_Type = Counter32
_CasWiredDeadCount_Object = MibTableColumn
casWiredDeadCount = _CasWiredDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 88),
    _CasWiredDeadCount_Type()
)
casWiredDeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWiredDeadCount.setStatus("current")


class _CasWirelessServerState0_Type(Integer32):
    """Custom type casWirelessServerState0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasWirelessServerState0_Type.__name__ = "Integer32"
_CasWirelessServerState0_Object = MibTableColumn
casWirelessServerState0 = _CasWirelessServerState0_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 89),
    _CasWirelessServerState0_Type()
)
casWirelessServerState0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessServerState0.setStatus("current")


class _CasWirelessServerState1_Type(Integer32):
    """Custom type casWirelessServerState1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasWirelessServerState1_Type.__name__ = "Integer32"
_CasWirelessServerState1_Object = MibTableColumn
casWirelessServerState1 = _CasWirelessServerState1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 90),
    _CasWirelessServerState1_Type()
)
casWirelessServerState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessServerState1.setStatus("current")


class _CasWirelessServerState2_Type(Integer32):
    """Custom type casWirelessServerState2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasWirelessServerState2_Type.__name__ = "Integer32"
_CasWirelessServerState2_Object = MibTableColumn
casWirelessServerState2 = _CasWirelessServerState2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 91),
    _CasWirelessServerState2_Type()
)
casWirelessServerState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessServerState2.setStatus("current")


class _CasWirelessServerState3_Type(Integer32):
    """Custom type casWirelessServerState3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasWirelessServerState3_Type.__name__ = "Integer32"
_CasWirelessServerState3_Object = MibTableColumn
casWirelessServerState3 = _CasWirelessServerState3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 92),
    _CasWirelessServerState3_Type()
)
casWirelessServerState3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessServerState3.setStatus("current")


class _CasWirelessServerState4_Type(Integer32):
    """Custom type casWirelessServerState4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasWirelessServerState4_Type.__name__ = "Integer32"
_CasWirelessServerState4_Object = MibTableColumn
casWirelessServerState4 = _CasWirelessServerState4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 93),
    _CasWirelessServerState4_Type()
)
casWirelessServerState4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessServerState4.setStatus("current")


class _CasWirelessServerState5_Type(Integer32):
    """Custom type casWirelessServerState5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasWirelessServerState5_Type.__name__ = "Integer32"
_CasWirelessServerState5_Object = MibTableColumn
casWirelessServerState5 = _CasWirelessServerState5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 94),
    _CasWirelessServerState5_Type()
)
casWirelessServerState5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessServerState5.setStatus("current")


class _CasWirelessServerState6_Type(Integer32):
    """Custom type casWirelessServerState6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasWirelessServerState6_Type.__name__ = "Integer32"
_CasWirelessServerState6_Object = MibTableColumn
casWirelessServerState6 = _CasWirelessServerState6_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 95),
    _CasWirelessServerState6_Type()
)
casWirelessServerState6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessServerState6.setStatus("current")


class _CasWirelessServerState7_Type(Integer32):
    """Custom type casWirelessServerState7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("dead", 2))
    )


_CasWirelessServerState7_Type.__name__ = "Integer32"
_CasWirelessServerState7_Object = MibTableColumn
casWirelessServerState7 = _CasWirelessServerState7_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 96),
    _CasWirelessServerState7_Type()
)
casWirelessServerState7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessServerState7.setStatus("current")
_CasWirelessDuration0_Type = TimeInterval
_CasWirelessDuration0_Object = MibTableColumn
casWirelessDuration0 = _CasWirelessDuration0_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 97),
    _CasWirelessDuration0_Type()
)
casWirelessDuration0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessDuration0.setStatus("current")
_CasWirelessDuration1_Type = TimeInterval
_CasWirelessDuration1_Object = MibTableColumn
casWirelessDuration1 = _CasWirelessDuration1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 98),
    _CasWirelessDuration1_Type()
)
casWirelessDuration1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessDuration1.setStatus("current")
_CasWirelessDuration2_Type = TimeInterval
_CasWirelessDuration2_Object = MibTableColumn
casWirelessDuration2 = _CasWirelessDuration2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 99),
    _CasWirelessDuration2_Type()
)
casWirelessDuration2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessDuration2.setStatus("current")
_CasWirelessDuration3_Type = TimeInterval
_CasWirelessDuration3_Object = MibTableColumn
casWirelessDuration3 = _CasWirelessDuration3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 100),
    _CasWirelessDuration3_Type()
)
casWirelessDuration3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessDuration3.setStatus("current")
_CasWirelessDuration4_Type = TimeInterval
_CasWirelessDuration4_Object = MibTableColumn
casWirelessDuration4 = _CasWirelessDuration4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 101),
    _CasWirelessDuration4_Type()
)
casWirelessDuration4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessDuration4.setStatus("current")
_CasWirelessDuration5_Type = TimeInterval
_CasWirelessDuration5_Object = MibTableColumn
casWirelessDuration5 = _CasWirelessDuration5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 102),
    _CasWirelessDuration5_Type()
)
casWirelessDuration5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessDuration5.setStatus("current")
_CasWirelessDuration6_Type = TimeInterval
_CasWirelessDuration6_Object = MibTableColumn
casWirelessDuration6 = _CasWirelessDuration6_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 103),
    _CasWirelessDuration6_Type()
)
casWirelessDuration6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessDuration6.setStatus("current")
_CasWirelessDuration7_Type = TimeInterval
_CasWirelessDuration7_Object = MibTableColumn
casWirelessDuration7 = _CasWirelessDuration7_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 104),
    _CasWirelessDuration7_Type()
)
casWirelessDuration7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessDuration7.setStatus("current")
_CasWirelessPreDuration0_Type = TimeInterval
_CasWirelessPreDuration0_Object = MibTableColumn
casWirelessPreDuration0 = _CasWirelessPreDuration0_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 105),
    _CasWirelessPreDuration0_Type()
)
casWirelessPreDuration0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessPreDuration0.setStatus("current")
_CasWirelessPreDuration1_Type = TimeInterval
_CasWirelessPreDuration1_Object = MibTableColumn
casWirelessPreDuration1 = _CasWirelessPreDuration1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 106),
    _CasWirelessPreDuration1_Type()
)
casWirelessPreDuration1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessPreDuration1.setStatus("current")
_CasWirelessPreDuration2_Type = TimeInterval
_CasWirelessPreDuration2_Object = MibTableColumn
casWirelessPreDuration2 = _CasWirelessPreDuration2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 107),
    _CasWirelessPreDuration2_Type()
)
casWirelessPreDuration2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessPreDuration2.setStatus("current")
_CasWirelessPreDuration3_Type = TimeInterval
_CasWirelessPreDuration3_Object = MibTableColumn
casWirelessPreDuration3 = _CasWirelessPreDuration3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 108),
    _CasWirelessPreDuration3_Type()
)
casWirelessPreDuration3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessPreDuration3.setStatus("current")
_CasWirelessPreDuration4_Type = TimeInterval
_CasWirelessPreDuration4_Object = MibTableColumn
casWirelessPreDuration4 = _CasWirelessPreDuration4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 109),
    _CasWirelessPreDuration4_Type()
)
casWirelessPreDuration4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessPreDuration4.setStatus("current")
_CasWirelessPreDuration5_Type = TimeInterval
_CasWirelessPreDuration5_Object = MibTableColumn
casWirelessPreDuration5 = _CasWirelessPreDuration5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 110),
    _CasWirelessPreDuration5_Type()
)
casWirelessPreDuration5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessPreDuration5.setStatus("current")
_CasWirelessPreDuration6_Type = TimeInterval
_CasWirelessPreDuration6_Object = MibTableColumn
casWirelessPreDuration6 = _CasWirelessPreDuration6_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 111),
    _CasWirelessPreDuration6_Type()
)
casWirelessPreDuration6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessPreDuration6.setStatus("current")
_CasWirelessPreDuration7_Type = TimeInterval
_CasWirelessPreDuration7_Object = MibTableColumn
casWirelessPreDuration7 = _CasWirelessPreDuration7_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 112),
    _CasWirelessPreDuration7_Type()
)
casWirelessPreDuration7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessPreDuration7.setStatus("current")
_CasWirelessTotalDeadTime_Type = TimeInterval
_CasWirelessTotalDeadTime_Object = MibTableColumn
casWirelessTotalDeadTime = _CasWirelessTotalDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 113),
    _CasWirelessTotalDeadTime_Type()
)
casWirelessTotalDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessTotalDeadTime.setStatus("current")
_CasWirelessDeadCount_Type = Counter32
_CasWirelessDeadCount_Object = MibTableColumn
casWirelessDeadCount = _CasWirelessDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 114),
    _CasWirelessDeadCount_Type()
)
casWirelessDeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casWirelessDeadCount.setStatus("current")


class _CasQuarantined_Type(Integer32):
    """Custom type casQuarantined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_CasQuarantined_Type.__name__ = "Integer32"
_CasQuarantined_Object = MibTableColumn
casQuarantined = _CasQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 115),
    _CasQuarantined_Type()
)
casQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casQuarantined.setStatus("current")
_CAAAServerMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cAAAServerMIBNotificationPrefix = _CAAAServerMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 2)
)
_CAAAServerMIBNotifications_ObjectIdentity = ObjectIdentity
cAAAServerMIBNotifications = _CAAAServerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 2, 0)
)
_CAAAServerMIBConformance_ObjectIdentity = ObjectIdentity
cAAAServerMIBConformance = _CAAAServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3)
)
_CasMIBCompliances_ObjectIdentity = ObjectIdentity
casMIBCompliances = _CasMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 1)
)
_CasMIBGroups_ObjectIdentity = ObjectIdentity
casMIBGroups = _CasMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2)
)
casConfigEntry.registerAugmentions(
    ("CISCO-AAA-SERVER-MIB",
     "casStatisticsEntry")
)
casStatisticsEntry.setIndexNames(*casConfigEntry.getIndexNames())

# Managed Objects groups

casStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2, 1)
)
casStatisticsGroup.setObjects(
      *(("CISCO-AAA-SERVER-MIB", "casAuthenRequests"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenRequestTimeouts"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenUnexpectedResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenServerErrorResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenIncorrectResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenResponseTime"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenTransactionSuccesses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenTransactionFailures"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorRequests"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorRequestTimeouts"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorUnexpectedResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorServerErrorResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorIncorrectResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorResponseTime"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorTransactionSuccesses"),
        ("CISCO-AAA-SERVER-MIB", "casAuthorTransactionFailures"),
        ("CISCO-AAA-SERVER-MIB", "casAcctRequests"),
        ("CISCO-AAA-SERVER-MIB", "casAcctRequestTimeouts"),
        ("CISCO-AAA-SERVER-MIB", "casAcctUnexpectedResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAcctServerErrorResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAcctIncorrectResponses"),
        ("CISCO-AAA-SERVER-MIB", "casAcctResponseTime"),
        ("CISCO-AAA-SERVER-MIB", "casAcctTransactionSuccesses"),
        ("CISCO-AAA-SERVER-MIB", "casAcctTransactionFailures"),
        ("CISCO-AAA-SERVER-MIB", "casState"),
        ("CISCO-AAA-SERVER-MIB", "casCurrentStateDuration"),
        ("CISCO-AAA-SERVER-MIB", "casPreviousStateDuration"),
        ("CISCO-AAA-SERVER-MIB", "casTotalDeadTime"),
        ("CISCO-AAA-SERVER-MIB", "casDeadCount"))
)
if mibBuilder.loadTexts:
    casStatisticsGroup.setStatus("current")

casConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2, 2)
)
casConfigGroup.setObjects(
      *(("CISCO-AAA-SERVER-MIB", "casServerStateChangeEnable"),
        ("CISCO-AAA-SERVER-MIB", "casAddress"),
        ("CISCO-AAA-SERVER-MIB", "casAuthenPort"),
        ("CISCO-AAA-SERVER-MIB", "casAcctPort"),
        ("CISCO-AAA-SERVER-MIB", "casKey"),
        ("CISCO-AAA-SERVER-MIB", "casPriority"),
        ("CISCO-AAA-SERVER-MIB", "casConfigRowStatus"))
)
if mibBuilder.loadTexts:
    casConfigGroup.setStatus("current")


# Notification objects

casServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 2, 0, 1)
)
casServerStateChange.setObjects(
      *(("CISCO-AAA-SERVER-MIB", "casState"),
        ("CISCO-AAA-SERVER-MIB", "casPreviousStateDuration"),
        ("CISCO-AAA-SERVER-MIB", "casTotalDeadTime"))
)
if mibBuilder.loadTexts:
    casServerStateChange.setStatus(
        "current"
    )


# Notifications groups

casServerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2, 3)
)
casServerNotificationGroup.setObjects(
    ("CISCO-AAA-SERVER-MIB", "casServerStateChange")
)
if mibBuilder.loadTexts:
    casServerNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

casMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 1, 1)
)
casMIBCompliance.setObjects(
      *(("CISCO-AAA-SERVER-MIB", "casConfigGroup"),
        ("CISCO-AAA-SERVER-MIB", "casStatisticsGroup"),
        ("CISCO-AAA-SERVER-MIB", "casServerNotificationGroup"))
)
if mibBuilder.loadTexts:
    casMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AAA-SERVER-MIB",
    **{"CiscoAAAProtocol": CiscoAAAProtocol,
       "ciscoAAAServerMIB": ciscoAAAServerMIB,
       "cAAAServerMIBObjects": cAAAServerMIBObjects,
       "casConfig": casConfig,
       "casServerStateChangeEnable": casServerStateChangeEnable,
       "casConfigTable": casConfigTable,
       "casConfigEntry": casConfigEntry,
       "casProtocol": casProtocol,
       "casIndex": casIndex,
       "casAddress": casAddress,
       "casAuthenPort": casAuthenPort,
       "casAcctPort": casAcctPort,
       "casKey": casKey,
       "casPriority": casPriority,
       "casConfigRowStatus": casConfigRowStatus,
       "casStatistics": casStatistics,
       "casStatisticsTable": casStatisticsTable,
       "casStatisticsEntry": casStatisticsEntry,
       "casAuthenRequests": casAuthenRequests,
       "casAuthenRequestTimeouts": casAuthenRequestTimeouts,
       "casAuthenUnexpectedResponses": casAuthenUnexpectedResponses,
       "casAuthenServerErrorResponses": casAuthenServerErrorResponses,
       "casAuthenIncorrectResponses": casAuthenIncorrectResponses,
       "casAuthenResponseTime": casAuthenResponseTime,
       "casAuthenTransactionSuccesses": casAuthenTransactionSuccesses,
       "casAuthenTransactionFailures": casAuthenTransactionFailures,
       "casAuthorRequests": casAuthorRequests,
       "casAuthorRequestTimeouts": casAuthorRequestTimeouts,
       "casAuthorUnexpectedResponses": casAuthorUnexpectedResponses,
       "casAuthorServerErrorResponses": casAuthorServerErrorResponses,
       "casAuthorIncorrectResponses": casAuthorIncorrectResponses,
       "casAuthorResponseTime": casAuthorResponseTime,
       "casAuthorTransactionSuccesses": casAuthorTransactionSuccesses,
       "casAuthorTransactionFailures": casAuthorTransactionFailures,
       "casAcctRequests": casAcctRequests,
       "casAcctRequestTimeouts": casAcctRequestTimeouts,
       "casAcctUnexpectedResponses": casAcctUnexpectedResponses,
       "casAcctServerErrorResponses": casAcctServerErrorResponses,
       "casAcctIncorrectResponses": casAcctIncorrectResponses,
       "casAcctResponseTime": casAcctResponseTime,
       "casAcctTransactionSuccesses": casAcctTransactionSuccesses,
       "casAcctTransactionFailures": casAcctTransactionFailures,
       "casState": casState,
       "casCurrentStateDuration": casCurrentStateDuration,
       "casPreviousStateDuration": casPreviousStateDuration,
       "casTotalDeadTime": casTotalDeadTime,
       "casDeadCount": casDeadCount,
       "casWiredServerState": casWiredServerState,
       "casAuthenRetrans": casAuthenRetrans,
       "casAuthenRequestFailover": casAuthenRequestFailover,
       "casAuthenResponseAccept": casAuthenResponseAccept,
       "casAuthenResponseReject": casAuthenResponseReject,
       "casAuthenResponseChallenge": casAuthenResponseChallenge,
       "casAuthenThrottledTransaction": casAuthenThrottledTransaction,
       "casAuthenThrottledTimeout": casAuthenThrottledTimeout,
       "casAuthenThrottledFailure": casAuthenThrottledFailure,
       "casAuthenMalformedResponses": casAuthenMalformedResponses,
       "casAuthenBadAuthenticators": casAuthenBadAuthenticators,
       "casAuthenDot1xTotalResponses": casAuthenDot1xTotalResponses,
       "casAuthenDot1xAvgResponseTime": casAuthenDot1xAvgResponseTime,
       "casAuthenDot1xTransactionTimeouts": casAuthenDot1xTransactionTimeouts,
       "casAuthenDot1xTransactionFailover": casAuthenDot1xTransactionFailover,
       "casAuthenDot1xTransactionTotal": casAuthenDot1xTransactionTotal,
       "casAuthenDot1xTransactionSuccess": casAuthenDot1xTransactionSuccess,
       "casAuthenDot1xTransactionFailure": casAuthenDot1xTransactionFailure,
       "casAuthenMACTotalResponses": casAuthenMACTotalResponses,
       "casAuthenMACAvgResponseTime": casAuthenMACAvgResponseTime,
       "casAuthenMACTransactionTimeouts": casAuthenMACTransactionTimeouts,
       "casAuthenMACTransactionFailover": casAuthenMACTransactionFailover,
       "casAuthenMACTransactionTotal": casAuthenMACTransactionTotal,
       "casAuthenMACTransactionSuccess": casAuthenMACTransactionSuccess,
       "casAuthenMACTransactionFailure": casAuthenMACTransactionFailure,
       "casAuthorRequestFailover": casAuthorRequestFailover,
       "casAuthorRequestRetransmission": casAuthorRequestRetransmission,
       "casAuthorResponseAccept": casAuthorResponseAccept,
       "casAuthorResponseReject": casAuthorResponseReject,
       "casAuthorResponseChallenge": casAuthorResponseChallenge,
       "casAuthorThrottledTransaction": casAuthorThrottledTransaction,
       "casAuthorThrottledTimeout": casAuthorThrottledTimeout,
       "casAuthorThrottledFailure": casAuthorThrottledFailure,
       "casAuthorMalformedResponses": casAuthorMalformedResponses,
       "casAuthorBadAuthenticators": casAuthorBadAuthenticators,
       "casAuthorMACTotalResponses": casAuthorMACTotalResponses,
       "casAuthorMACAvgResponseTime": casAuthorMACAvgResponseTime,
       "casAuthorMACTransactionTimeouts": casAuthorMACTransactionTimeouts,
       "casAuthorMACTransactionFailover": casAuthorMACTransactionFailover,
       "casAuthorMACTransactionTotal": casAuthorMACTransactionTotal,
       "casAuthorMACTransactionSuccess": casAuthorMACTransactionSuccess,
       "casAuthorMACTransactionFailure": casAuthorMACTransactionFailure,
       "casAcctRequestFailover": casAcctRequestFailover,
       "casAcctRequestRetransmission": casAcctRequestRetransmission,
       "casAcctRequestStart": casAcctRequestStart,
       "casAcctRequestInterim": casAcctRequestInterim,
       "casAcctRequestStop": casAcctRequestStop,
       "casAcctResponseStart": casAcctResponseStart,
       "casAcctResponseInterim": casAcctResponseInterim,
       "casAcctResponseStop": casAcctResponseStop,
       "casAcctThrottledTransaction": casAcctThrottledTransaction,
       "casAcctThrottledTimeout": casAcctThrottledTimeout,
       "casAcctThrottledFailure": casAcctThrottledFailure,
       "casAcctMalformedResponses": casAcctMalformedResponses,
       "casAcctBadAuthenticators": casAcctBadAuthenticators,
       "casWiredDuration": casWiredDuration,
       "casWiredPreDuration": casWiredPreDuration,
       "casWiredTotalDeadTime": casWiredTotalDeadTime,
       "casWiredDeadCount": casWiredDeadCount,
       "casWirelessServerState0": casWirelessServerState0,
       "casWirelessServerState1": casWirelessServerState1,
       "casWirelessServerState2": casWirelessServerState2,
       "casWirelessServerState3": casWirelessServerState3,
       "casWirelessServerState4": casWirelessServerState4,
       "casWirelessServerState5": casWirelessServerState5,
       "casWirelessServerState6": casWirelessServerState6,
       "casWirelessServerState7": casWirelessServerState7,
       "casWirelessDuration0": casWirelessDuration0,
       "casWirelessDuration1": casWirelessDuration1,
       "casWirelessDuration2": casWirelessDuration2,
       "casWirelessDuration3": casWirelessDuration3,
       "casWirelessDuration4": casWirelessDuration4,
       "casWirelessDuration5": casWirelessDuration5,
       "casWirelessDuration6": casWirelessDuration6,
       "casWirelessDuration7": casWirelessDuration7,
       "casWirelessPreDuration0": casWirelessPreDuration0,
       "casWirelessPreDuration1": casWirelessPreDuration1,
       "casWirelessPreDuration2": casWirelessPreDuration2,
       "casWirelessPreDuration3": casWirelessPreDuration3,
       "casWirelessPreDuration4": casWirelessPreDuration4,
       "casWirelessPreDuration5": casWirelessPreDuration5,
       "casWirelessPreDuration6": casWirelessPreDuration6,
       "casWirelessPreDuration7": casWirelessPreDuration7,
       "casWirelessTotalDeadTime": casWirelessTotalDeadTime,
       "casWirelessDeadCount": casWirelessDeadCount,
       "casQuarantined": casQuarantined,
       "cAAAServerMIBNotificationPrefix": cAAAServerMIBNotificationPrefix,
       "cAAAServerMIBNotifications": cAAAServerMIBNotifications,
       "casServerStateChange": casServerStateChange,
       "cAAAServerMIBConformance": cAAAServerMIBConformance,
       "casMIBCompliances": casMIBCompliances,
       "casMIBCompliance": casMIBCompliance,
       "casMIBGroups": casMIBGroups,
       "casStatisticsGroup": casStatisticsGroup,
       "casConfigGroup": casConfigGroup,
       "casServerNotificationGroup": casServerNotificationGroup}
)
