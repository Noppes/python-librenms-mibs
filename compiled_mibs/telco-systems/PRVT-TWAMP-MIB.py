# SNMP MIB module (PRVT-TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-TWAMP-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtTwampMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240)
)
if mibBuilder.loadTexts:
    prvtTwampMIB.setRevisions(
        ("2010-05-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtTwampTestNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class PrvtTwampDecimalPercent(TextualConvention, OctetString):
    status = "current"
    displayHint = "3d.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )



# MIB Managed Objects in the order of their OIDs

_PrvtTwampNotifications_ObjectIdentity = ObjectIdentity
prvtTwampNotifications = _PrvtTwampNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 0)
)
_PrvtTwampObjects_ObjectIdentity = ObjectIdentity
prvtTwampObjects = _PrvtTwampObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1)
)
_PrvtTwampTest_ObjectIdentity = ObjectIdentity
prvtTwampTest = _PrvtTwampTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1)
)
_PrvtTwampTestTable_Object = MibTable
prvtTwampTestTable = _PrvtTwampTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtTwampTestTable.setStatus("current")
_PrvtTwampTestEntry_Object = MibTableRow
prvtTwampTestEntry = _PrvtTwampTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1, 1)
)
prvtTwampTestEntry.setIndexNames(
    (0, "PRVT-TWAMP-MIB", "prvtTwampTestName"),
)
if mibBuilder.loadTexts:
    prvtTwampTestEntry.setStatus("current")
_PrvtTwampTestName_Type = PrvtTwampTestNameType
_PrvtTwampTestName_Object = MibTableColumn
prvtTwampTestName = _PrvtTwampTestName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1, 1, 1),
    _PrvtTwampTestName_Type()
)
prvtTwampTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtTwampTestName.setStatus("current")
_PrvtTwampTestRowStatus_Type = RowStatus
_PrvtTwampTestRowStatus_Object = MibTableColumn
prvtTwampTestRowStatus = _PrvtTwampTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1, 1, 2),
    _PrvtTwampTestRowStatus_Type()
)
prvtTwampTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestRowStatus.setStatus("current")
_PrvtTwampTestServer_Type = IpAddress
_PrvtTwampTestServer_Object = MibTableColumn
prvtTwampTestServer = _PrvtTwampTestServer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1, 1, 3),
    _PrvtTwampTestServer_Type()
)
prvtTwampTestServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestServer.setStatus("current")


class _PrvtTwampTestSessionsCount_Type(Integer32):
    """Custom type prvtTwampTestSessionsCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtTwampTestSessionsCount_Type.__name__ = "Integer32"
_PrvtTwampTestSessionsCount_Object = MibTableColumn
prvtTwampTestSessionsCount = _PrvtTwampTestSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1, 1, 4),
    _PrvtTwampTestSessionsCount_Type()
)
prvtTwampTestSessionsCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestSessionsCount.setStatus("current")


class _PrvtTwampTestPackets_Type(Integer32):
    """Custom type prvtTwampTestPackets based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_PrvtTwampTestPackets_Type.__name__ = "Integer32"
_PrvtTwampTestPackets_Object = MibTableColumn
prvtTwampTestPackets = _PrvtTwampTestPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1, 1, 5),
    _PrvtTwampTestPackets_Type()
)
prvtTwampTestPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestPackets.setStatus("current")


class _PrvtTwampTestTimeout_Type(Integer32):
    """Custom type prvtTwampTestTimeout based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_PrvtTwampTestTimeout_Type.__name__ = "Integer32"
_PrvtTwampTestTimeout_Object = MibTableColumn
prvtTwampTestTimeout = _PrvtTwampTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1, 1, 6),
    _PrvtTwampTestTimeout_Type()
)
prvtTwampTestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestTimeout.setStatus("current")


class _PrvtTwampTestDelay_Type(Integer32):
    """Custom type prvtTwampTestDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_PrvtTwampTestDelay_Type.__name__ = "Integer32"
_PrvtTwampTestDelay_Object = MibTableColumn
prvtTwampTestDelay = _PrvtTwampTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1, 1, 7),
    _PrvtTwampTestDelay_Type()
)
prvtTwampTestDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestDelay.setStatus("current")


class _PrvtTwampTestExecuteNow_Type(Integer32):
    """Custom type prvtTwampTestExecuteNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PrvtTwampTestExecuteNow_Type.__name__ = "Integer32"
_PrvtTwampTestExecuteNow_Object = MibTableColumn
prvtTwampTestExecuteNow = _PrvtTwampTestExecuteNow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 1, 1, 1, 8),
    _PrvtTwampTestExecuteNow_Type()
)
prvtTwampTestExecuteNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampTestExecuteNow.setStatus("current")
_PrvtTwampServer_ObjectIdentity = ObjectIdentity
prvtTwampServer = _PrvtTwampServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2)
)


class _PrvtTwampServerInnactivity_Type(Integer32):
    """Custom type prvtTwampServerInnactivity based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_PrvtTwampServerInnactivity_Type.__name__ = "Integer32"
_PrvtTwampServerInnactivity_Object = MibScalar
prvtTwampServerInnactivity = _PrvtTwampServerInnactivity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 2),
    _PrvtTwampServerInnactivity_Type()
)
prvtTwampServerInnactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerInnactivity.setStatus("current")


class _PrvtTwampServerSessionInnactivity_Type(Integer32):
    """Custom type prvtTwampServerSessionInnactivity based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_PrvtTwampServerSessionInnactivity_Type.__name__ = "Integer32"
_PrvtTwampServerSessionInnactivity_Object = MibScalar
prvtTwampServerSessionInnactivity = _PrvtTwampServerSessionInnactivity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 3),
    _PrvtTwampServerSessionInnactivity_Type()
)
prvtTwampServerSessionInnactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerSessionInnactivity.setStatus("current")


class _PrvtTwampServerMaxSessions_Type(Integer32):
    """Custom type prvtTwampServerMaxSessions based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PrvtTwampServerMaxSessions_Type.__name__ = "Integer32"
_PrvtTwampServerMaxSessions_Object = MibScalar
prvtTwampServerMaxSessions = _PrvtTwampServerMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 4),
    _PrvtTwampServerMaxSessions_Type()
)
prvtTwampServerMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerMaxSessions.setStatus("current")


class _PrvtTwampServerMaxParallelSessions_Type(Integer32):
    """Custom type prvtTwampServerMaxParallelSessions based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtTwampServerMaxParallelSessions_Type.__name__ = "Integer32"
_PrvtTwampServerMaxParallelSessions_Object = MibScalar
prvtTwampServerMaxParallelSessions = _PrvtTwampServerMaxParallelSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 5),
    _PrvtTwampServerMaxParallelSessions_Type()
)
prvtTwampServerMaxParallelSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerMaxParallelSessions.setStatus("current")


class _PrvtTwampServerShutdown_Type(TruthValue):
    """Custom type prvtTwampServerShutdown based on TruthValue"""
    defaultValue = 1


_PrvtTwampServerShutdown_Type.__name__ = "TruthValue"
_PrvtTwampServerShutdown_Object = MibScalar
prvtTwampServerShutdown = _PrvtTwampServerShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 6),
    _PrvtTwampServerShutdown_Type()
)
prvtTwampServerShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTwampServerShutdown.setStatus("current")
_PrvtTwampClientTable_Object = MibTable
prvtTwampClientTable = _PrvtTwampClientTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 7)
)
if mibBuilder.loadTexts:
    prvtTwampClientTable.setStatus("current")
_PrvtTwampClientEntry_Object = MibTableRow
prvtTwampClientEntry = _PrvtTwampClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 7, 1)
)
prvtTwampClientEntry.setIndexNames(
    (0, "PRVT-TWAMP-MIB", "prvtTwampClientIp"),
)
if mibBuilder.loadTexts:
    prvtTwampClientEntry.setStatus("current")
_PrvtTwampClientIp_Type = IpAddress
_PrvtTwampClientIp_Object = MibTableColumn
prvtTwampClientIp = _PrvtTwampClientIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 7, 1, 1),
    _PrvtTwampClientIp_Type()
)
prvtTwampClientIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtTwampClientIp.setStatus("current")
_PrvtTwampClientRowStatus_Type = RowStatus
_PrvtTwampClientRowStatus_Object = MibTableColumn
prvtTwampClientRowStatus = _PrvtTwampClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 7, 1, 2),
    _PrvtTwampClientRowStatus_Type()
)
prvtTwampClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtTwampClientRowStatus.setStatus("current")
_PrvtTwampServerControlSessions_Type = Integer32
_PrvtTwampServerControlSessions_Object = MibScalar
prvtTwampServerControlSessions = _PrvtTwampServerControlSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 8),
    _PrvtTwampServerControlSessions_Type()
)
prvtTwampServerControlSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampServerControlSessions.setStatus("current")
_PrvtTwampServerTestSessions_Type = Integer32
_PrvtTwampServerTestSessions_Object = MibScalar
prvtTwampServerTestSessions = _PrvtTwampServerTestSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 2, 9),
    _PrvtTwampServerTestSessions_Type()
)
prvtTwampServerTestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampServerTestSessions.setStatus("current")
_PrvtTwampTestResult_ObjectIdentity = ObjectIdentity
prvtTwampTestResult = _PrvtTwampTestResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3)
)
_PrvtTwampTestResultTable_Object = MibTable
prvtTwampTestResultTable = _PrvtTwampTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1)
)
if mibBuilder.loadTexts:
    prvtTwampTestResultTable.setStatus("current")
_PrvtTwampTestResultEntry_Object = MibTableRow
prvtTwampTestResultEntry = _PrvtTwampTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1)
)
prvtTwampTestResultEntry.setIndexNames(
    (0, "PRVT-TWAMP-MIB", "prvtTwampTestId"),
    (0, "PRVT-TWAMP-MIB", "prvtTwampTestResultName"),
)
if mibBuilder.loadTexts:
    prvtTwampTestResultEntry.setStatus("current")
_PrvtTwampTestId_Type = Unsigned32
_PrvtTwampTestId_Object = MibTableColumn
prvtTwampTestId = _PrvtTwampTestId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 1),
    _PrvtTwampTestId_Type()
)
prvtTwampTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestId.setStatus("current")
_PrvtTwampTestResultName_Type = PrvtTwampTestNameType
_PrvtTwampTestResultName_Object = MibTableColumn
prvtTwampTestResultName = _PrvtTwampTestResultName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 2),
    _PrvtTwampTestResultName_Type()
)
prvtTwampTestResultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestResultName.setStatus("current")
_PrvtTwampTestStartTime_Type = Unsigned32
_PrvtTwampTestStartTime_Object = MibTableColumn
prvtTwampTestStartTime = _PrvtTwampTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 3),
    _PrvtTwampTestStartTime_Type()
)
prvtTwampTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestStartTime.setStatus("current")
_PrvtTwampTestServerAddress_Type = IpAddress
_PrvtTwampTestServerAddress_Object = MibTableColumn
prvtTwampTestServerAddress = _PrvtTwampTestServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 4),
    _PrvtTwampTestServerAddress_Type()
)
prvtTwampTestServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestServerAddress.setStatus("current")


class _PrvtTwampTestSessions_Type(Unsigned32):
    """Custom type prvtTwampTestSessions based on Unsigned32"""
    defaultValue = 0


_PrvtTwampTestSessions_Type.__name__ = "Unsigned32"
_PrvtTwampTestSessions_Object = MibTableColumn
prvtTwampTestSessions = _PrvtTwampTestSessions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 5),
    _PrvtTwampTestSessions_Type()
)
prvtTwampTestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestSessions.setStatus("current")


class _PrvtTwampTestState_Type(Integer32):
    """Custom type prvtTwampTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("running", 2),
          ("stopped", 3),
          ("finished", 4))
    )


_PrvtTwampTestState_Type.__name__ = "Integer32"
_PrvtTwampTestState_Object = MibTableColumn
prvtTwampTestState = _PrvtTwampTestState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 6),
    _PrvtTwampTestState_Type()
)
prvtTwampTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestState.setStatus("current")


class _PrvtTwampTestRtt_Type(Counter64):
    """Custom type prvtTwampTestRtt based on Counter64"""
    defaultValue = 0


_PrvtTwampTestRtt_Type.__name__ = "Counter64"
_PrvtTwampTestRtt_Object = MibTableColumn
prvtTwampTestRtt = _PrvtTwampTestRtt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 7),
    _PrvtTwampTestRtt_Type()
)
prvtTwampTestRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestRtt.setStatus("current")


class _PrvtTwampTestMinRtt_Type(Counter64):
    """Custom type prvtTwampTestMinRtt based on Counter64"""
    defaultValue = 0


_PrvtTwampTestMinRtt_Type.__name__ = "Counter64"
_PrvtTwampTestMinRtt_Object = MibTableColumn
prvtTwampTestMinRtt = _PrvtTwampTestMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 8),
    _PrvtTwampTestMinRtt_Type()
)
prvtTwampTestMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestMinRtt.setStatus("current")


class _PrvtTwampTestMaxRtt_Type(Counter64):
    """Custom type prvtTwampTestMaxRtt based on Counter64"""
    defaultValue = 0


_PrvtTwampTestMaxRtt_Type.__name__ = "Counter64"
_PrvtTwampTestMaxRtt_Object = MibTableColumn
prvtTwampTestMaxRtt = _PrvtTwampTestMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 9),
    _PrvtTwampTestMaxRtt_Type()
)
prvtTwampTestMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestMaxRtt.setStatus("current")


class _PrvtTwampTestPcktSent_Type(Unsigned32):
    """Custom type prvtTwampTestPcktSent based on Unsigned32"""
    defaultValue = 0


_PrvtTwampTestPcktSent_Type.__name__ = "Unsigned32"
_PrvtTwampTestPcktSent_Object = MibTableColumn
prvtTwampTestPcktSent = _PrvtTwampTestPcktSent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 10),
    _PrvtTwampTestPcktSent_Type()
)
prvtTwampTestPcktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestPcktSent.setStatus("current")


class _PrvtTwampTestPcktLost_Type(Unsigned32):
    """Custom type prvtTwampTestPcktLost based on Unsigned32"""
    defaultValue = 0


_PrvtTwampTestPcktLost_Type.__name__ = "Unsigned32"
_PrvtTwampTestPcktLost_Object = MibTableColumn
prvtTwampTestPcktLost = _PrvtTwampTestPcktLost_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 11),
    _PrvtTwampTestPcktLost_Type()
)
prvtTwampTestPcktLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestPcktLost.setStatus("current")


class _PrvtTwampTestPcktDrop_Type(Unsigned32):
    """Custom type prvtTwampTestPcktDrop based on Unsigned32"""
    defaultValue = 0


_PrvtTwampTestPcktDrop_Type.__name__ = "Unsigned32"
_PrvtTwampTestPcktDrop_Object = MibTableColumn
prvtTwampTestPcktDrop = _PrvtTwampTestPcktDrop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 12),
    _PrvtTwampTestPcktDrop_Type()
)
prvtTwampTestPcktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestPcktDrop.setStatus("current")


class _PrvtTwampTestVariation_Type(Counter64):
    """Custom type prvtTwampTestVariation based on Counter64"""
    defaultValue = 0


_PrvtTwampTestVariation_Type.__name__ = "Counter64"
_PrvtTwampTestVariation_Object = MibTableColumn
prvtTwampTestVariation = _PrvtTwampTestVariation_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 13),
    _PrvtTwampTestVariation_Type()
)
prvtTwampTestVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestVariation.setStatus("current")
_PrvtTwampTestVariationLow_Type = PrvtTwampDecimalPercent
_PrvtTwampTestVariationLow_Object = MibTableColumn
prvtTwampTestVariationLow = _PrvtTwampTestVariationLow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 14),
    _PrvtTwampTestVariationLow_Type()
)
prvtTwampTestVariationLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestVariationLow.setStatus("current")
_PrvtTwampTestVariationMiddle_Type = PrvtTwampDecimalPercent
_PrvtTwampTestVariationMiddle_Object = MibTableColumn
prvtTwampTestVariationMiddle = _PrvtTwampTestVariationMiddle_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 15),
    _PrvtTwampTestVariationMiddle_Type()
)
prvtTwampTestVariationMiddle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestVariationMiddle.setStatus("current")
_PrvtTwampTestVariationHigh_Type = PrvtTwampDecimalPercent
_PrvtTwampTestVariationHigh_Object = MibTableColumn
prvtTwampTestVariationHigh = _PrvtTwampTestVariationHigh_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 240, 1, 3, 1, 1, 16),
    _PrvtTwampTestVariationHigh_Type()
)
prvtTwampTestVariationHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTwampTestVariationHigh.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-TWAMP-MIB",
    **{"PrvtTwampTestNameType": PrvtTwampTestNameType,
       "PrvtTwampDecimalPercent": PrvtTwampDecimalPercent,
       "prvtTwampMIB": prvtTwampMIB,
       "prvtTwampNotifications": prvtTwampNotifications,
       "prvtTwampObjects": prvtTwampObjects,
       "prvtTwampTest": prvtTwampTest,
       "prvtTwampTestTable": prvtTwampTestTable,
       "prvtTwampTestEntry": prvtTwampTestEntry,
       "prvtTwampTestName": prvtTwampTestName,
       "prvtTwampTestRowStatus": prvtTwampTestRowStatus,
       "prvtTwampTestServer": prvtTwampTestServer,
       "prvtTwampTestSessionsCount": prvtTwampTestSessionsCount,
       "prvtTwampTestPackets": prvtTwampTestPackets,
       "prvtTwampTestTimeout": prvtTwampTestTimeout,
       "prvtTwampTestDelay": prvtTwampTestDelay,
       "prvtTwampTestExecuteNow": prvtTwampTestExecuteNow,
       "prvtTwampServer": prvtTwampServer,
       "prvtTwampServerInnactivity": prvtTwampServerInnactivity,
       "prvtTwampServerSessionInnactivity": prvtTwampServerSessionInnactivity,
       "prvtTwampServerMaxSessions": prvtTwampServerMaxSessions,
       "prvtTwampServerMaxParallelSessions": prvtTwampServerMaxParallelSessions,
       "prvtTwampServerShutdown": prvtTwampServerShutdown,
       "prvtTwampClientTable": prvtTwampClientTable,
       "prvtTwampClientEntry": prvtTwampClientEntry,
       "prvtTwampClientIp": prvtTwampClientIp,
       "prvtTwampClientRowStatus": prvtTwampClientRowStatus,
       "prvtTwampServerControlSessions": prvtTwampServerControlSessions,
       "prvtTwampServerTestSessions": prvtTwampServerTestSessions,
       "prvtTwampTestResult": prvtTwampTestResult,
       "prvtTwampTestResultTable": prvtTwampTestResultTable,
       "prvtTwampTestResultEntry": prvtTwampTestResultEntry,
       "prvtTwampTestId": prvtTwampTestId,
       "prvtTwampTestResultName": prvtTwampTestResultName,
       "prvtTwampTestStartTime": prvtTwampTestStartTime,
       "prvtTwampTestServerAddress": prvtTwampTestServerAddress,
       "prvtTwampTestSessions": prvtTwampTestSessions,
       "prvtTwampTestState": prvtTwampTestState,
       "prvtTwampTestRtt": prvtTwampTestRtt,
       "prvtTwampTestMinRtt": prvtTwampTestMinRtt,
       "prvtTwampTestMaxRtt": prvtTwampTestMaxRtt,
       "prvtTwampTestPcktSent": prvtTwampTestPcktSent,
       "prvtTwampTestPcktLost": prvtTwampTestPcktLost,
       "prvtTwampTestPcktDrop": prvtTwampTestPcktDrop,
       "prvtTwampTestVariation": prvtTwampTestVariation,
       "prvtTwampTestVariationLow": prvtTwampTestVariationLow,
       "prvtTwampTestVariationMiddle": prvtTwampTestVariationMiddle,
       "prvtTwampTestVariationHigh": prvtTwampTestVariationHigh}
)
