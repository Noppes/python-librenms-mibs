# SNMP MIB module (PRVT-SWITCH-EFM-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SWITCH-EFM-OAM-MIB

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

(dot3OamAdminState,
 dot3OamLoopbackStatus,
 dot3OamMode) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "dot3OamAdminState",
    "dot3OamLoopbackStatus",
    "dot3OamMode")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtSwitchEfmOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133)
)
if mibBuilder.loadTexts:
    prvtSwitchEfmOamMIB.setRevisions(
        ("2010-02-11 00:00",
         "2009-12-01 00:00",
         "2009-06-01 00:00",
         "2009-04-29 00:00",
         "2009-03-18 00:00",
         "2009-03-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtEfmOamNotifications_ObjectIdentity = ObjectIdentity
prvtEfmOamNotifications = _PrvtEfmOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 0)
)
_PrvtEfmOamObjects_ObjectIdentity = ObjectIdentity
prvtEfmOamObjects = _PrvtEfmOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1)
)
_PrvtEfmOamEnable_Type = TruthValue
_PrvtEfmOamEnable_Object = MibScalar
prvtEfmOamEnable = _PrvtEfmOamEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 1),
    _PrvtEfmOamEnable_Type()
)
prvtEfmOamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEnable.setStatus("current")


class _PrvtEfmOamMultiPduCount_Type(Unsigned32):
    """Custom type prvtEfmOamMultiPduCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtEfmOamMultiPduCount_Type.__name__ = "Unsigned32"
_PrvtEfmOamMultiPduCount_Object = MibScalar
prvtEfmOamMultiPduCount = _PrvtEfmOamMultiPduCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 2),
    _PrvtEfmOamMultiPduCount_Type()
)
prvtEfmOamMultiPduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamMultiPduCount.setStatus("current")


class _PrvtEfmOamRemoteEvent_Type(TruthValue):
    """Custom type prvtEfmOamRemoteEvent based on TruthValue"""
    defaultValue = 1


_PrvtEfmOamRemoteEvent_Type.__name__ = "TruthValue"
_PrvtEfmOamRemoteEvent_Object = MibScalar
prvtEfmOamRemoteEvent = _PrvtEfmOamRemoteEvent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 3),
    _PrvtEfmOamRemoteEvent_Type()
)
prvtEfmOamRemoteEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamRemoteEvent.setStatus("current")


class _PrvtEfmOamLocalSysLog_Type(TruthValue):
    """Custom type prvtEfmOamLocalSysLog based on TruthValue"""
    defaultValue = 1


_PrvtEfmOamLocalSysLog_Type.__name__ = "TruthValue"
_PrvtEfmOamLocalSysLog_Object = MibScalar
prvtEfmOamLocalSysLog = _PrvtEfmOamLocalSysLog_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 4),
    _PrvtEfmOamLocalSysLog_Type()
)
prvtEfmOamLocalSysLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLocalSysLog.setStatus("current")


class _PrvtEfmOamPriority_Type(Unsigned32):
    """Custom type prvtEfmOamPriority based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PrvtEfmOamPriority_Type.__name__ = "Unsigned32"
_PrvtEfmOamPriority_Object = MibScalar
prvtEfmOamPriority = _PrvtEfmOamPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 5),
    _PrvtEfmOamPriority_Type()
)
prvtEfmOamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamPriority.setStatus("current")


class _PrvtEfmOamKeepAlive_Type(Unsigned32):
    """Custom type prvtEfmOamKeepAlive based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 15000),
    )


_PrvtEfmOamKeepAlive_Type.__name__ = "Unsigned32"
_PrvtEfmOamKeepAlive_Object = MibScalar
prvtEfmOamKeepAlive = _PrvtEfmOamKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 6),
    _PrvtEfmOamKeepAlive_Type()
)
prvtEfmOamKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamKeepAlive.setStatus("current")


class _PrvtEfmOamHelloInterval_Type(Unsigned32):
    """Custom type prvtEfmOamHelloInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_PrvtEfmOamHelloInterval_Type.__name__ = "Unsigned32"
_PrvtEfmOamHelloInterval_Object = MibScalar
prvtEfmOamHelloInterval = _PrvtEfmOamHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 7),
    _PrvtEfmOamHelloInterval_Type()
)
prvtEfmOamHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamHelloInterval.setStatus("current")
_PrvtEfmOamPktsSent_Type = Unsigned32
_PrvtEfmOamPktsSent_Object = MibScalar
prvtEfmOamPktsSent = _PrvtEfmOamPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 8),
    _PrvtEfmOamPktsSent_Type()
)
prvtEfmOamPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPktsSent.setStatus("current")
_PrvtEfmOamPktsReceived_Type = Unsigned32
_PrvtEfmOamPktsReceived_Object = MibScalar
prvtEfmOamPktsReceived = _PrvtEfmOamPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 9),
    _PrvtEfmOamPktsReceived_Type()
)
prvtEfmOamPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPktsReceived.setStatus("current")
_PrvtEfmOamTable_Object = MibTable
prvtEfmOamTable = _PrvtEfmOamTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 10)
)
if mibBuilder.loadTexts:
    prvtEfmOamTable.setStatus("current")
_PrvtEfmOamEntry_Object = MibTableRow
prvtEfmOamEntry = _PrvtEfmOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 10, 1)
)
prvtEfmOamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamEntry.setStatus("current")


class _PrvtEfmOamEnhanceMode_Type(Integer32):
    """Custom type prvtEfmOamEnhanceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("enhance", 2))
    )


_PrvtEfmOamEnhanceMode_Type.__name__ = "Integer32"
_PrvtEfmOamEnhanceMode_Object = MibTableColumn
prvtEfmOamEnhanceMode = _PrvtEfmOamEnhanceMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 10, 1, 1),
    _PrvtEfmOamEnhanceMode_Type()
)
prvtEfmOamEnhanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEnhanceMode.setStatus("current")


class _PrvtEfmOamEventReturn_Type(Integer32):
    """Custom type prvtEfmOamEventReturn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_PrvtEfmOamEventReturn_Type.__name__ = "Integer32"
_PrvtEfmOamEventReturn_Object = MibTableColumn
prvtEfmOamEventReturn = _PrvtEfmOamEventReturn_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 10, 1, 2),
    _PrvtEfmOamEventReturn_Type()
)
prvtEfmOamEventReturn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventReturn.setStatus("current")


class _PrvtEfmOamForceLoopbackLocal_Type(TruthValue):
    """Custom type prvtEfmOamForceLoopbackLocal based on TruthValue"""
    defaultValue = 2


_PrvtEfmOamForceLoopbackLocal_Type.__name__ = "TruthValue"
_PrvtEfmOamForceLoopbackLocal_Object = MibTableColumn
prvtEfmOamForceLoopbackLocal = _PrvtEfmOamForceLoopbackLocal_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 10, 1, 3),
    _PrvtEfmOamForceLoopbackLocal_Type()
)
prvtEfmOamForceLoopbackLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamForceLoopbackLocal.setStatus("current")


class _PrvtEfmOamForceLoopbackRemote_Type(TruthValue):
    """Custom type prvtEfmOamForceLoopbackRemote based on TruthValue"""
    defaultValue = 2


_PrvtEfmOamForceLoopbackRemote_Type.__name__ = "TruthValue"
_PrvtEfmOamForceLoopbackRemote_Object = MibTableColumn
prvtEfmOamForceLoopbackRemote = _PrvtEfmOamForceLoopbackRemote_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 10, 1, 4),
    _PrvtEfmOamForceLoopbackRemote_Type()
)
prvtEfmOamForceLoopbackRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamForceLoopbackRemote.setStatus("current")
_PrvtEfmOamEventForwardStatus_Type = PortList
_PrvtEfmOamEventForwardStatus_Object = MibTableColumn
prvtEfmOamEventForwardStatus = _PrvtEfmOamEventForwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 10, 1, 5),
    _PrvtEfmOamEventForwardStatus_Type()
)
prvtEfmOamEventForwardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardStatus.setStatus("current")
_PrvtEfmOamEventForwardShutdown_Type = PortList
_PrvtEfmOamEventForwardShutdown_Object = MibTableColumn
prvtEfmOamEventForwardShutdown = _PrvtEfmOamEventForwardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 10, 1, 6),
    _PrvtEfmOamEventForwardShutdown_Type()
)
prvtEfmOamEventForwardShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardShutdown.setStatus("current")
_PrvtEfmOamPing_ObjectIdentity = ObjectIdentity
prvtEfmOamPing = _PrvtEfmOamPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11)
)
_PrvtEfmOamPingTable_Object = MibTable
prvtEfmOamPingTable = _PrvtEfmOamPingTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 1)
)
if mibBuilder.loadTexts:
    prvtEfmOamPingTable.setStatus("current")
_PrvtEfmOamPingEntry_Object = MibTableRow
prvtEfmOamPingEntry = _PrvtEfmOamPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 1, 1)
)
prvtEfmOamPingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamPingEntry.setStatus("current")


class _PrvtEfmOamPingEchoNumber_Type(Unsigned32):
    """Custom type prvtEfmOamPingEchoNumber based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtEfmOamPingEchoNumber_Type.__name__ = "Unsigned32"
_PrvtEfmOamPingEchoNumber_Object = MibTableColumn
prvtEfmOamPingEchoNumber = _PrvtEfmOamPingEchoNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 1, 1, 1),
    _PrvtEfmOamPingEchoNumber_Type()
)
prvtEfmOamPingEchoNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamPingEchoNumber.setStatus("current")


class _PrvtEfmOamPingDelayTime_Type(Unsigned32):
    """Custom type prvtEfmOamPingDelayTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PrvtEfmOamPingDelayTime_Type.__name__ = "Unsigned32"
_PrvtEfmOamPingDelayTime_Object = MibTableColumn
prvtEfmOamPingDelayTime = _PrvtEfmOamPingDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 1, 1, 2),
    _PrvtEfmOamPingDelayTime_Type()
)
prvtEfmOamPingDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamPingDelayTime.setStatus("current")


class _PrvtEfmOamPingTimeOut_Type(Unsigned32):
    """Custom type prvtEfmOamPingTimeOut based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PrvtEfmOamPingTimeOut_Type.__name__ = "Unsigned32"
_PrvtEfmOamPingTimeOut_Object = MibTableColumn
prvtEfmOamPingTimeOut = _PrvtEfmOamPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 1, 1, 3),
    _PrvtEfmOamPingTimeOut_Type()
)
prvtEfmOamPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamPingTimeOut.setStatus("current")


class _PrvtEfmOamPingCounterBranch_Type(Integer32):
    """Custom type prvtEfmOamPingCounterBranch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("branch", 7)
    )


_PrvtEfmOamPingCounterBranch_Type.__name__ = "Integer32"
_PrvtEfmOamPingCounterBranch_Object = MibTableColumn
prvtEfmOamPingCounterBranch = _PrvtEfmOamPingCounterBranch_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 1, 1, 4),
    _PrvtEfmOamPingCounterBranch_Type()
)
prvtEfmOamPingCounterBranch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamPingCounterBranch.setStatus("current")


class _PrvtEfmOamPingCounterLeaf_Type(Integer32):
    """Custom type prvtEfmOamPingCounterLeaf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              8,
              14,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("framesTransmittedOK", 2),
          ("framesReceivedOK", 5),
          ("octetsTransmittedOK", 8),
          ("octetsReceivedOK", 14),
          ("multicastFramesReceivedOK", 21),
          ("broadcastFramesReceivedOK", 22))
    )


_PrvtEfmOamPingCounterLeaf_Type.__name__ = "Integer32"
_PrvtEfmOamPingCounterLeaf_Object = MibTableColumn
prvtEfmOamPingCounterLeaf = _PrvtEfmOamPingCounterLeaf_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 1, 1, 5),
    _PrvtEfmOamPingCounterLeaf_Type()
)
prvtEfmOamPingCounterLeaf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamPingCounterLeaf.setStatus("current")
_PrvtEfmOamPingRowStatus_Type = RowStatus
_PrvtEfmOamPingRowStatus_Object = MibTableColumn
prvtEfmOamPingRowStatus = _PrvtEfmOamPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 1, 1, 6),
    _PrvtEfmOamPingRowStatus_Type()
)
prvtEfmOamPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamPingRowStatus.setStatus("current")
_PrvtEfmOamPingResultTable_Object = MibTable
prvtEfmOamPingResultTable = _PrvtEfmOamPingResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2)
)
if mibBuilder.loadTexts:
    prvtEfmOamPingResultTable.setStatus("current")
_PrvtEfmOamPingResultEntry_Object = MibTableRow
prvtEfmOamPingResultEntry = _PrvtEfmOamPingResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1)
)
prvtEfmOamPingResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamPingResultEntry.setStatus("current")


class _PrvtEfmOamPingResultStatus_Type(Integer32):
    """Custom type prvtEfmOamPingResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noPing", 1),
          ("running", 2),
          ("terminated", 3))
    )


_PrvtEfmOamPingResultStatus_Type.__name__ = "Integer32"
_PrvtEfmOamPingResultStatus_Object = MibTableColumn
prvtEfmOamPingResultStatus = _PrvtEfmOamPingResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 1),
    _PrvtEfmOamPingResultStatus_Type()
)
prvtEfmOamPingResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultStatus.setStatus("current")
_PrvtEfmOamPingResultSentPackets_Type = Counter32
_PrvtEfmOamPingResultSentPackets_Object = MibTableColumn
prvtEfmOamPingResultSentPackets = _PrvtEfmOamPingResultSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 2),
    _PrvtEfmOamPingResultSentPackets_Type()
)
prvtEfmOamPingResultSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultSentPackets.setStatus("current")
_PrvtEfmOamPingResultReceivedPackets_Type = Counter32
_PrvtEfmOamPingResultReceivedPackets_Object = MibTableColumn
prvtEfmOamPingResultReceivedPackets = _PrvtEfmOamPingResultReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 3),
    _PrvtEfmOamPingResultReceivedPackets_Type()
)
prvtEfmOamPingResultReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultReceivedPackets.setStatus("current")
_PrvtEfmOamPingResultRcvRateInteger_Type = Unsigned32
_PrvtEfmOamPingResultRcvRateInteger_Object = MibTableColumn
prvtEfmOamPingResultRcvRateInteger = _PrvtEfmOamPingResultRcvRateInteger_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 4),
    _PrvtEfmOamPingResultRcvRateInteger_Type()
)
prvtEfmOamPingResultRcvRateInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultRcvRateInteger.setStatus("current")
_PrvtEfmOamPingResultRcvRateFractional_Type = Unsigned32
_PrvtEfmOamPingResultRcvRateFractional_Object = MibTableColumn
prvtEfmOamPingResultRcvRateFractional = _PrvtEfmOamPingResultRcvRateFractional_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 5),
    _PrvtEfmOamPingResultRcvRateFractional_Type()
)
prvtEfmOamPingResultRcvRateFractional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultRcvRateFractional.setStatus("current")
_PrvtEfmOamPingResultTimeMin_Type = Unsigned32
_PrvtEfmOamPingResultTimeMin_Object = MibTableColumn
prvtEfmOamPingResultTimeMin = _PrvtEfmOamPingResultTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 6),
    _PrvtEfmOamPingResultTimeMin_Type()
)
prvtEfmOamPingResultTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultTimeMin.setStatus("current")
_PrvtEfmOamPingResultTimeMax_Type = Unsigned32
_PrvtEfmOamPingResultTimeMax_Object = MibTableColumn
prvtEfmOamPingResultTimeMax = _PrvtEfmOamPingResultTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 7),
    _PrvtEfmOamPingResultTimeMax_Type()
)
prvtEfmOamPingResultTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultTimeMax.setStatus("current")
_PrvtEfmOamPingResultAverageTimeInteger_Type = Unsigned32
_PrvtEfmOamPingResultAverageTimeInteger_Object = MibTableColumn
prvtEfmOamPingResultAverageTimeInteger = _PrvtEfmOamPingResultAverageTimeInteger_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 8),
    _PrvtEfmOamPingResultAverageTimeInteger_Type()
)
prvtEfmOamPingResultAverageTimeInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultAverageTimeInteger.setStatus("current")
_PrvtEfmOamPingResultAverageTimeFractional_Type = Unsigned32
_PrvtEfmOamPingResultAverageTimeFractional_Object = MibTableColumn
prvtEfmOamPingResultAverageTimeFractional = _PrvtEfmOamPingResultAverageTimeFractional_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 9),
    _PrvtEfmOamPingResultAverageTimeFractional_Type()
)
prvtEfmOamPingResultAverageTimeFractional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultAverageTimeFractional.setStatus("current")


class _PrvtEfmOamPingResultClear_Type(Integer32):
    """Custom type prvtEfmOamPingResultClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_PrvtEfmOamPingResultClear_Type.__name__ = "Integer32"
_PrvtEfmOamPingResultClear_Object = MibTableColumn
prvtEfmOamPingResultClear = _PrvtEfmOamPingResultClear_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11, 2, 1, 10),
    _PrvtEfmOamPingResultClear_Type()
)
prvtEfmOamPingResultClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultClear.setStatus("current")
_PrvtEfmOamLoopback_ObjectIdentity = ObjectIdentity
prvtEfmOamLoopback = _PrvtEfmOamLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12)
)
_PrvtEfmOamLoopbackTable_Object = MibTable
prvtEfmOamLoopbackTable = _PrvtEfmOamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1)
)
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackTable.setStatus("current")
_PrvtEfmOamLoopbackEntry_Object = MibTableRow
prvtEfmOamLoopbackEntry = _PrvtEfmOamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1, 1)
)
prvtEfmOamLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackEntry.setStatus("current")


class _PrvtEfmOamLoopbackOperation_Type(Integer32):
    """Custom type prvtEfmOamLoopbackOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("storm", 1),
          ("burst", 2))
    )


_PrvtEfmOamLoopbackOperation_Type.__name__ = "Integer32"
_PrvtEfmOamLoopbackOperation_Object = MibTableColumn
prvtEfmOamLoopbackOperation = _PrvtEfmOamLoopbackOperation_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1, 1, 1),
    _PrvtEfmOamLoopbackOperation_Type()
)
prvtEfmOamLoopbackOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackOperation.setStatus("current")


class _PrvtEfmOamLoopbackDuration_Type(Unsigned32):
    """Custom type prvtEfmOamLoopbackDuration based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PrvtEfmOamLoopbackDuration_Type.__name__ = "Unsigned32"
_PrvtEfmOamLoopbackDuration_Object = MibTableColumn
prvtEfmOamLoopbackDuration = _PrvtEfmOamLoopbackDuration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1, 1, 2),
    _PrvtEfmOamLoopbackDuration_Type()
)
prvtEfmOamLoopbackDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackDuration.setStatus("current")


class _PrvtEfmOamLoopbackCount_Type(Unsigned32):
    """Custom type prvtEfmOamLoopbackCount based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483646),
    )


_PrvtEfmOamLoopbackCount_Type.__name__ = "Unsigned32"
_PrvtEfmOamLoopbackCount_Object = MibTableColumn
prvtEfmOamLoopbackCount = _PrvtEfmOamLoopbackCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1, 1, 3),
    _PrvtEfmOamLoopbackCount_Type()
)
prvtEfmOamLoopbackCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackCount.setStatus("current")


class _PrvtEfmOamLoopbackPacketSize_Type(Unsigned32):
    """Custom type prvtEfmOamLoopbackPacketSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1512),
    )


_PrvtEfmOamLoopbackPacketSize_Type.__name__ = "Unsigned32"
_PrvtEfmOamLoopbackPacketSize_Object = MibTableColumn
prvtEfmOamLoopbackPacketSize = _PrvtEfmOamLoopbackPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1, 1, 4),
    _PrvtEfmOamLoopbackPacketSize_Type()
)
prvtEfmOamLoopbackPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackPacketSize.setStatus("current")


class _PrvtEfmOamLoopbackDelay_Type(Unsigned32):
    """Custom type prvtEfmOamLoopbackDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PrvtEfmOamLoopbackDelay_Type.__name__ = "Unsigned32"
_PrvtEfmOamLoopbackDelay_Object = MibTableColumn
prvtEfmOamLoopbackDelay = _PrvtEfmOamLoopbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1, 1, 5),
    _PrvtEfmOamLoopbackDelay_Type()
)
prvtEfmOamLoopbackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackDelay.setStatus("current")


class _PrvtEfmOamLoopbackTimeout_Type(Unsigned32):
    """Custom type prvtEfmOamLoopbackTimeout based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PrvtEfmOamLoopbackTimeout_Type.__name__ = "Unsigned32"
_PrvtEfmOamLoopbackTimeout_Object = MibTableColumn
prvtEfmOamLoopbackTimeout = _PrvtEfmOamLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1, 1, 6),
    _PrvtEfmOamLoopbackTimeout_Type()
)
prvtEfmOamLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackTimeout.setStatus("current")


class _PrvtEfmOamLoopbackNoRemote_Type(TruthValue):
    """Custom type prvtEfmOamLoopbackNoRemote based on TruthValue"""
    defaultValue = 2


_PrvtEfmOamLoopbackNoRemote_Type.__name__ = "TruthValue"
_PrvtEfmOamLoopbackNoRemote_Object = MibTableColumn
prvtEfmOamLoopbackNoRemote = _PrvtEfmOamLoopbackNoRemote_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1, 1, 7),
    _PrvtEfmOamLoopbackNoRemote_Type()
)
prvtEfmOamLoopbackNoRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackNoRemote.setStatus("current")
_PrvtEfmOamLoopbackRowStatus_Type = RowStatus
_PrvtEfmOamLoopbackRowStatus_Object = MibTableColumn
prvtEfmOamLoopbackRowStatus = _PrvtEfmOamLoopbackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 1, 1, 8),
    _PrvtEfmOamLoopbackRowStatus_Type()
)
prvtEfmOamLoopbackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackRowStatus.setStatus("current")
_PrvtEfmOamLoopbackResultTable_Object = MibTable
prvtEfmOamLoopbackResultTable = _PrvtEfmOamLoopbackResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 2)
)
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultTable.setStatus("current")
_PrvtEfmOamLoopbackResultEntry_Object = MibTableRow
prvtEfmOamLoopbackResultEntry = _PrvtEfmOamLoopbackResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 2, 1)
)
prvtEfmOamLoopbackResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultEntry.setStatus("current")


class _PrvtEfmOamLoopbackResultStatus_Type(Integer32):
    """Custom type prvtEfmOamLoopbackResultStatus based on Integer32"""
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
        *(("noLoopback", 1),
          ("startCmdSent", 2),
          ("startFail", 3),
          ("dataStarted", 4),
          ("stopCmdSent", 5),
          ("terminated", 6),
          ("remoteFailure", 7))
    )


_PrvtEfmOamLoopbackResultStatus_Type.__name__ = "Integer32"
_PrvtEfmOamLoopbackResultStatus_Object = MibTableColumn
prvtEfmOamLoopbackResultStatus = _PrvtEfmOamLoopbackResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 2, 1, 1),
    _PrvtEfmOamLoopbackResultStatus_Type()
)
prvtEfmOamLoopbackResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultStatus.setStatus("current")
_PrvtEfmOamLoopbackResultFlood_Type = Integer32
_PrvtEfmOamLoopbackResultFlood_Object = MibTableColumn
prvtEfmOamLoopbackResultFlood = _PrvtEfmOamLoopbackResultFlood_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 2, 1, 2),
    _PrvtEfmOamLoopbackResultFlood_Type()
)
prvtEfmOamLoopbackResultFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultFlood.setStatus("current")
_PrvtEfmOamLoopbackResultSentPackets_Type = Counter32
_PrvtEfmOamLoopbackResultSentPackets_Object = MibTableColumn
prvtEfmOamLoopbackResultSentPackets = _PrvtEfmOamLoopbackResultSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 2, 1, 3),
    _PrvtEfmOamLoopbackResultSentPackets_Type()
)
prvtEfmOamLoopbackResultSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultSentPackets.setStatus("current")
_PrvtEfmOamLoopbackResultReceivedPackets_Type = Counter32
_PrvtEfmOamLoopbackResultReceivedPackets_Object = MibTableColumn
prvtEfmOamLoopbackResultReceivedPackets = _PrvtEfmOamLoopbackResultReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 2, 1, 4),
    _PrvtEfmOamLoopbackResultReceivedPackets_Type()
)
prvtEfmOamLoopbackResultReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultReceivedPackets.setStatus("current")


class _PrvtEfmOamLoopbackResultClear_Type(Integer32):
    """Custom type prvtEfmOamLoopbackResultClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_PrvtEfmOamLoopbackResultClear_Type.__name__ = "Integer32"
_PrvtEfmOamLoopbackResultClear_Object = MibTableColumn
prvtEfmOamLoopbackResultClear = _PrvtEfmOamLoopbackResultClear_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12, 2, 1, 5),
    _PrvtEfmOamLoopbackResultClear_Type()
)
prvtEfmOamLoopbackResultClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultClear.setStatus("current")
_PrvtEfmOamPeerTable_Object = MibTable
prvtEfmOamPeerTable = _PrvtEfmOamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 13)
)
if mibBuilder.loadTexts:
    prvtEfmOamPeerTable.setStatus("current")
_PrvtEfmOamPeerEntry_Object = MibTableRow
prvtEfmOamPeerEntry = _PrvtEfmOamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 13, 1)
)
prvtEfmOamPeerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamPeerEntry.setStatus("current")
_PrvtEfmOamPeerPort_Type = DisplayString
_PrvtEfmOamPeerPort_Object = MibTableColumn
prvtEfmOamPeerPort = _PrvtEfmOamPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 13, 1, 1),
    _PrvtEfmOamPeerPort_Type()
)
prvtEfmOamPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerPort.setStatus("current")
_PrvtEfmOamPeerName_Type = DisplayString
_PrvtEfmOamPeerName_Object = MibTableColumn
prvtEfmOamPeerName = _PrvtEfmOamPeerName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 13, 1, 2),
    _PrvtEfmOamPeerName_Type()
)
prvtEfmOamPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerName.setStatus("current")


class _PrvtEfmOamHistorySize_Type(Unsigned32):
    """Custom type prvtEfmOamHistorySize based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_PrvtEfmOamHistorySize_Type.__name__ = "Unsigned32"
_PrvtEfmOamHistorySize_Object = MibScalar
prvtEfmOamHistorySize = _PrvtEfmOamHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 14),
    _PrvtEfmOamHistorySize_Type()
)
prvtEfmOamHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamHistorySize.setStatus("current")
_PrvtEfmOamConformance_ObjectIdentity = ObjectIdentity
prvtEfmOamConformance = _PrvtEfmOamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 2)
)

# Managed Objects groups


# Notification objects

prvtOamLoopBackState = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 0, 1)
)
prvtOamLoopBackState.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOT3-OAM-MIB", "dot3OamAdminState"),
        ("DOT3-OAM-MIB", "dot3OamMode"),
        ("DOT3-OAM-MIB", "dot3OamLoopbackStatus"))
)
if mibBuilder.loadTexts:
    prvtOamLoopBackState.setStatus(
        "current"
    )

prvtOamDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 0, 2)
)
if mibBuilder.loadTexts:
    prvtOamDyingGasp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SWITCH-EFM-OAM-MIB",
    **{"prvtSwitchEfmOamMIB": prvtSwitchEfmOamMIB,
       "prvtEfmOamNotifications": prvtEfmOamNotifications,
       "prvtOamLoopBackState": prvtOamLoopBackState,
       "prvtOamDyingGasp": prvtOamDyingGasp,
       "prvtEfmOamObjects": prvtEfmOamObjects,
       "prvtEfmOamEnable": prvtEfmOamEnable,
       "prvtEfmOamMultiPduCount": prvtEfmOamMultiPduCount,
       "prvtEfmOamRemoteEvent": prvtEfmOamRemoteEvent,
       "prvtEfmOamLocalSysLog": prvtEfmOamLocalSysLog,
       "prvtEfmOamPriority": prvtEfmOamPriority,
       "prvtEfmOamKeepAlive": prvtEfmOamKeepAlive,
       "prvtEfmOamHelloInterval": prvtEfmOamHelloInterval,
       "prvtEfmOamPktsSent": prvtEfmOamPktsSent,
       "prvtEfmOamPktsReceived": prvtEfmOamPktsReceived,
       "prvtEfmOamTable": prvtEfmOamTable,
       "prvtEfmOamEntry": prvtEfmOamEntry,
       "prvtEfmOamEnhanceMode": prvtEfmOamEnhanceMode,
       "prvtEfmOamEventReturn": prvtEfmOamEventReturn,
       "prvtEfmOamForceLoopbackLocal": prvtEfmOamForceLoopbackLocal,
       "prvtEfmOamForceLoopbackRemote": prvtEfmOamForceLoopbackRemote,
       "prvtEfmOamEventForwardStatus": prvtEfmOamEventForwardStatus,
       "prvtEfmOamEventForwardShutdown": prvtEfmOamEventForwardShutdown,
       "prvtEfmOamPing": prvtEfmOamPing,
       "prvtEfmOamPingTable": prvtEfmOamPingTable,
       "prvtEfmOamPingEntry": prvtEfmOamPingEntry,
       "prvtEfmOamPingEchoNumber": prvtEfmOamPingEchoNumber,
       "prvtEfmOamPingDelayTime": prvtEfmOamPingDelayTime,
       "prvtEfmOamPingTimeOut": prvtEfmOamPingTimeOut,
       "prvtEfmOamPingCounterBranch": prvtEfmOamPingCounterBranch,
       "prvtEfmOamPingCounterLeaf": prvtEfmOamPingCounterLeaf,
       "prvtEfmOamPingRowStatus": prvtEfmOamPingRowStatus,
       "prvtEfmOamPingResultTable": prvtEfmOamPingResultTable,
       "prvtEfmOamPingResultEntry": prvtEfmOamPingResultEntry,
       "prvtEfmOamPingResultStatus": prvtEfmOamPingResultStatus,
       "prvtEfmOamPingResultSentPackets": prvtEfmOamPingResultSentPackets,
       "prvtEfmOamPingResultReceivedPackets": prvtEfmOamPingResultReceivedPackets,
       "prvtEfmOamPingResultRcvRateInteger": prvtEfmOamPingResultRcvRateInteger,
       "prvtEfmOamPingResultRcvRateFractional": prvtEfmOamPingResultRcvRateFractional,
       "prvtEfmOamPingResultTimeMin": prvtEfmOamPingResultTimeMin,
       "prvtEfmOamPingResultTimeMax": prvtEfmOamPingResultTimeMax,
       "prvtEfmOamPingResultAverageTimeInteger": prvtEfmOamPingResultAverageTimeInteger,
       "prvtEfmOamPingResultAverageTimeFractional": prvtEfmOamPingResultAverageTimeFractional,
       "prvtEfmOamPingResultClear": prvtEfmOamPingResultClear,
       "prvtEfmOamLoopback": prvtEfmOamLoopback,
       "prvtEfmOamLoopbackTable": prvtEfmOamLoopbackTable,
       "prvtEfmOamLoopbackEntry": prvtEfmOamLoopbackEntry,
       "prvtEfmOamLoopbackOperation": prvtEfmOamLoopbackOperation,
       "prvtEfmOamLoopbackDuration": prvtEfmOamLoopbackDuration,
       "prvtEfmOamLoopbackCount": prvtEfmOamLoopbackCount,
       "prvtEfmOamLoopbackPacketSize": prvtEfmOamLoopbackPacketSize,
       "prvtEfmOamLoopbackDelay": prvtEfmOamLoopbackDelay,
       "prvtEfmOamLoopbackTimeout": prvtEfmOamLoopbackTimeout,
       "prvtEfmOamLoopbackNoRemote": prvtEfmOamLoopbackNoRemote,
       "prvtEfmOamLoopbackRowStatus": prvtEfmOamLoopbackRowStatus,
       "prvtEfmOamLoopbackResultTable": prvtEfmOamLoopbackResultTable,
       "prvtEfmOamLoopbackResultEntry": prvtEfmOamLoopbackResultEntry,
       "prvtEfmOamLoopbackResultStatus": prvtEfmOamLoopbackResultStatus,
       "prvtEfmOamLoopbackResultFlood": prvtEfmOamLoopbackResultFlood,
       "prvtEfmOamLoopbackResultSentPackets": prvtEfmOamLoopbackResultSentPackets,
       "prvtEfmOamLoopbackResultReceivedPackets": prvtEfmOamLoopbackResultReceivedPackets,
       "prvtEfmOamLoopbackResultClear": prvtEfmOamLoopbackResultClear,
       "prvtEfmOamPeerTable": prvtEfmOamPeerTable,
       "prvtEfmOamPeerEntry": prvtEfmOamPeerEntry,
       "prvtEfmOamPeerPort": prvtEfmOamPeerPort,
       "prvtEfmOamPeerName": prvtEfmOamPeerName,
       "prvtEfmOamHistorySize": prvtEfmOamHistorySize,
       "prvtEfmOamConformance": prvtEfmOamConformance}
)
