# SNMP MIB module (PRVT-EFM-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-EFM-OAM-MIB

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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

prvtEfmOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133)
)
if mibBuilder.loadTexts:
    prvtEfmOamMIB.setRevisions(
        ("2010-01-10 00:00",)
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
_PrvtEfmOamRemoteEvent_Type = TruthValue
_PrvtEfmOamRemoteEvent_Object = MibScalar
prvtEfmOamRemoteEvent = _PrvtEfmOamRemoteEvent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 3),
    _PrvtEfmOamRemoteEvent_Type()
)
prvtEfmOamRemoteEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamRemoteEvent.setStatus("current")
_PrvtEfmOamLogEvents_Type = TruthValue
_PrvtEfmOamLogEvents_Object = MibScalar
prvtEfmOamLogEvents = _PrvtEfmOamLogEvents_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 4),
    _PrvtEfmOamLogEvents_Type()
)
prvtEfmOamLogEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamLogEvents.setStatus("current")


class _PrvtEfmOamPriority_Type(Unsigned32):
    """Custom type prvtEfmOamPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
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
_PrvtEfmOamPriorityEnable_Type = TruthValue
_PrvtEfmOamPriorityEnable_Object = MibScalar
prvtEfmOamPriorityEnable = _PrvtEfmOamPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 6),
    _PrvtEfmOamPriorityEnable_Type()
)
prvtEfmOamPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamPriorityEnable.setStatus("current")


class _PrvtEfmOamKeepAliveInterval_Type(Unsigned32):
    """Custom type prvtEfmOamKeepAliveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 15000),
    )


_PrvtEfmOamKeepAliveInterval_Type.__name__ = "Unsigned32"
_PrvtEfmOamKeepAliveInterval_Object = MibScalar
prvtEfmOamKeepAliveInterval = _PrvtEfmOamKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 7),
    _PrvtEfmOamKeepAliveInterval_Type()
)
prvtEfmOamKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamKeepAliveInterval.setStatus("current")


class _PrvtEfmOamHelloInterval_Type(Unsigned32):
    """Custom type prvtEfmOamHelloInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_PrvtEfmOamHelloInterval_Type.__name__ = "Unsigned32"
_PrvtEfmOamHelloInterval_Object = MibScalar
prvtEfmOamHelloInterval = _PrvtEfmOamHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 8),
    _PrvtEfmOamHelloInterval_Type()
)
prvtEfmOamHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamHelloInterval.setStatus("current")


class _PrvtEfmOamHistoryLimit_Type(Unsigned32):
    """Custom type prvtEfmOamHistoryLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_PrvtEfmOamHistoryLimit_Type.__name__ = "Unsigned32"
_PrvtEfmOamHistoryLimit_Object = MibScalar
prvtEfmOamHistoryLimit = _PrvtEfmOamHistoryLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 9),
    _PrvtEfmOamHistoryLimit_Type()
)
prvtEfmOamHistoryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamHistoryLimit.setStatus("current")
_PrvtEfmOamHistoryCount_Type = Unsigned32
_PrvtEfmOamHistoryCount_Object = MibScalar
prvtEfmOamHistoryCount = _PrvtEfmOamHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 10),
    _PrvtEfmOamHistoryCount_Type()
)
prvtEfmOamHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamHistoryCount.setStatus("current")


class _PrvtEfmOamHistoryClear_Type(Integer32):
    """Custom type prvtEfmOamHistoryClear based on Integer32"""
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


_PrvtEfmOamHistoryClear_Type.__name__ = "Integer32"
_PrvtEfmOamHistoryClear_Object = MibScalar
prvtEfmOamHistoryClear = _PrvtEfmOamHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 11),
    _PrvtEfmOamHistoryClear_Type()
)
prvtEfmOamHistoryClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamHistoryClear.setStatus("current")
_PrvtEfmOamPacketSent_Type = Unsigned32
_PrvtEfmOamPacketSent_Object = MibScalar
prvtEfmOamPacketSent = _PrvtEfmOamPacketSent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 12),
    _PrvtEfmOamPacketSent_Type()
)
prvtEfmOamPacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPacketSent.setStatus("current")
_PrvtEfmOamPacketReceived_Type = Unsigned32
_PrvtEfmOamPacketReceived_Object = MibScalar
prvtEfmOamPacketReceived = _PrvtEfmOamPacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 13),
    _PrvtEfmOamPacketReceived_Type()
)
prvtEfmOamPacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPacketReceived.setStatus("current")
_PrvtEfmOamLocalMac_Type = OctetString
_PrvtEfmOamLocalMac_Object = MibScalar
prvtEfmOamLocalMac = _PrvtEfmOamLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 14),
    _PrvtEfmOamLocalMac_Type()
)
prvtEfmOamLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLocalMac.setStatus("current")
_PrvtEfmOamPingTable_Object = MibTable
prvtEfmOamPingTable = _PrvtEfmOamPingTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 15)
)
if mibBuilder.loadTexts:
    prvtEfmOamPingTable.setStatus("current")
_PrvtEfmOamPingEntry_Object = MibTableRow
prvtEfmOamPingEntry = _PrvtEfmOamPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 15, 1)
)
prvtEfmOamPingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamPingEntry.setStatus("current")
_PrvtEfmOamPingRowStatus_Type = RowStatus
_PrvtEfmOamPingRowStatus_Object = MibTableColumn
prvtEfmOamPingRowStatus = _PrvtEfmOamPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 15, 1, 1),
    _PrvtEfmOamPingRowStatus_Type()
)
prvtEfmOamPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamPingRowStatus.setStatus("current")


class _PrvtEfmOamPingStatus_Type(Integer32):
    """Custom type prvtEfmOamPingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startPing", 1),
          ("stopPing", 2))
    )


_PrvtEfmOamPingStatus_Type.__name__ = "Integer32"
_PrvtEfmOamPingStatus_Object = MibTableColumn
prvtEfmOamPingStatus = _PrvtEfmOamPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 15, 1, 2),
    _PrvtEfmOamPingStatus_Type()
)
prvtEfmOamPingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamPingStatus.setStatus("current")


class _PrvtEfmOamPingEchoNumber_Type(Unsigned32):
    """Custom type prvtEfmOamPingEchoNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtEfmOamPingEchoNumber_Type.__name__ = "Unsigned32"
_PrvtEfmOamPingEchoNumber_Object = MibTableColumn
prvtEfmOamPingEchoNumber = _PrvtEfmOamPingEchoNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 15, 1, 3),
    _PrvtEfmOamPingEchoNumber_Type()
)
prvtEfmOamPingEchoNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamPingEchoNumber.setStatus("current")


class _PrvtEfmOamPingDelayTime_Type(Unsigned32):
    """Custom type prvtEfmOamPingDelayTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PrvtEfmOamPingDelayTime_Type.__name__ = "Unsigned32"
_PrvtEfmOamPingDelayTime_Object = MibTableColumn
prvtEfmOamPingDelayTime = _PrvtEfmOamPingDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 15, 1, 4),
    _PrvtEfmOamPingDelayTime_Type()
)
prvtEfmOamPingDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamPingDelayTime.setStatus("current")


class _PrvtEfmOamPingTimeOut_Type(Unsigned32):
    """Custom type prvtEfmOamPingTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PrvtEfmOamPingTimeOut_Type.__name__ = "Unsigned32"
_PrvtEfmOamPingTimeOut_Object = MibTableColumn
prvtEfmOamPingTimeOut = _PrvtEfmOamPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 15, 1, 5),
    _PrvtEfmOamPingTimeOut_Type()
)
prvtEfmOamPingTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamPingTimeOut.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 15, 1, 6),
    _PrvtEfmOamPingResultClear_Type()
)
prvtEfmOamPingResultClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultClear.setStatus("current")
_PrvtEfmOamPingResultTable_Object = MibTable
prvtEfmOamPingResultTable = _PrvtEfmOamPingResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 16)
)
if mibBuilder.loadTexts:
    prvtEfmOamPingResultTable.setStatus("current")
_PrvtEfmOamPingResultEntry_Object = MibTableRow
prvtEfmOamPingResultEntry = _PrvtEfmOamPingResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 16, 1)
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
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 16, 1, 1),
    _PrvtEfmOamPingResultStatus_Type()
)
prvtEfmOamPingResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultStatus.setStatus("current")
_PrvtEfmOamPingResultSentPackets_Type = Counter32
_PrvtEfmOamPingResultSentPackets_Object = MibTableColumn
prvtEfmOamPingResultSentPackets = _PrvtEfmOamPingResultSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 16, 1, 2),
    _PrvtEfmOamPingResultSentPackets_Type()
)
prvtEfmOamPingResultSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultSentPackets.setStatus("current")
_PrvtEfmOamPingResultReceivedPackets_Type = Counter32
_PrvtEfmOamPingResultReceivedPackets_Object = MibTableColumn
prvtEfmOamPingResultReceivedPackets = _PrvtEfmOamPingResultReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 16, 1, 3),
    _PrvtEfmOamPingResultReceivedPackets_Type()
)
prvtEfmOamPingResultReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultReceivedPackets.setStatus("current")
_PrvtEfmOamPingResultReceiveRate_Type = Unsigned32
_PrvtEfmOamPingResultReceiveRate_Object = MibTableColumn
prvtEfmOamPingResultReceiveRate = _PrvtEfmOamPingResultReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 16, 1, 4),
    _PrvtEfmOamPingResultReceiveRate_Type()
)
prvtEfmOamPingResultReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultReceiveRate.setStatus("current")
_PrvtEfmOamPingResultTimeMin_Type = Unsigned32
_PrvtEfmOamPingResultTimeMin_Object = MibTableColumn
prvtEfmOamPingResultTimeMin = _PrvtEfmOamPingResultTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 16, 1, 5),
    _PrvtEfmOamPingResultTimeMin_Type()
)
prvtEfmOamPingResultTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultTimeMin.setStatus("current")
_PrvtEfmOamPingResultTimeMax_Type = Unsigned32
_PrvtEfmOamPingResultTimeMax_Object = MibTableColumn
prvtEfmOamPingResultTimeMax = _PrvtEfmOamPingResultTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 16, 1, 6),
    _PrvtEfmOamPingResultTimeMax_Type()
)
prvtEfmOamPingResultTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultTimeMax.setStatus("current")
_PrvtEfmOamPingResultAverageTime_Type = Unsigned32
_PrvtEfmOamPingResultAverageTime_Object = MibTableColumn
prvtEfmOamPingResultAverageTime = _PrvtEfmOamPingResultAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 16, 1, 7),
    _PrvtEfmOamPingResultAverageTime_Type()
)
prvtEfmOamPingResultAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPingResultAverageTime.setStatus("current")
_PrvtEfmOamLoopbackTable_Object = MibTable
prvtEfmOamLoopbackTable = _PrvtEfmOamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17)
)
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackTable.setStatus("current")
_PrvtEfmOamLoopbackEntry_Object = MibTableRow
prvtEfmOamLoopbackEntry = _PrvtEfmOamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17, 1)
)
prvtEfmOamLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackEntry.setStatus("current")
_PrvtEfmOamLoopbackRowStatus_Type = RowStatus
_PrvtEfmOamLoopbackRowStatus_Object = MibTableColumn
prvtEfmOamLoopbackRowStatus = _PrvtEfmOamLoopbackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17, 1, 1),
    _PrvtEfmOamLoopbackRowStatus_Type()
)
prvtEfmOamLoopbackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackRowStatus.setStatus("current")


class _PrvtEfmOamLoopbackType_Type(Integer32):
    """Custom type prvtEfmOamLoopbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("storm", 1))
    )


_PrvtEfmOamLoopbackType_Type.__name__ = "Integer32"
_PrvtEfmOamLoopbackType_Object = MibTableColumn
prvtEfmOamLoopbackType = _PrvtEfmOamLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17, 1, 2),
    _PrvtEfmOamLoopbackType_Type()
)
prvtEfmOamLoopbackType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackType.setStatus("current")


class _PrvtEfmOamLoopbackStatus_Type(Integer32):
    """Custom type prvtEfmOamLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("initiatingLoopback", 2),
          ("terminatingLoopback", 4))
    )


_PrvtEfmOamLoopbackStatus_Type.__name__ = "Integer32"
_PrvtEfmOamLoopbackStatus_Object = MibTableColumn
prvtEfmOamLoopbackStatus = _PrvtEfmOamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17, 1, 3),
    _PrvtEfmOamLoopbackStatus_Type()
)
prvtEfmOamLoopbackStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackStatus.setStatus("current")


class _PrvtEfmOamLoopbackCount_Type(Unsigned32):
    """Custom type prvtEfmOamLoopbackCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PrvtEfmOamLoopbackCount_Type.__name__ = "Unsigned32"
_PrvtEfmOamLoopbackCount_Object = MibTableColumn
prvtEfmOamLoopbackCount = _PrvtEfmOamLoopbackCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17, 1, 4),
    _PrvtEfmOamLoopbackCount_Type()
)
prvtEfmOamLoopbackCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackCount.setStatus("current")


class _PrvtEfmOamLoopbackPacketSize_Type(Unsigned32):
    """Custom type prvtEfmOamLoopbackPacketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1512),
    )


_PrvtEfmOamLoopbackPacketSize_Type.__name__ = "Unsigned32"
_PrvtEfmOamLoopbackPacketSize_Object = MibTableColumn
prvtEfmOamLoopbackPacketSize = _PrvtEfmOamLoopbackPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17, 1, 5),
    _PrvtEfmOamLoopbackPacketSize_Type()
)
prvtEfmOamLoopbackPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackPacketSize.setStatus("current")


class _PrvtEfmOamLoopbackDelay_Type(Unsigned32):
    """Custom type prvtEfmOamLoopbackDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PrvtEfmOamLoopbackDelay_Type.__name__ = "Unsigned32"
_PrvtEfmOamLoopbackDelay_Object = MibTableColumn
prvtEfmOamLoopbackDelay = _PrvtEfmOamLoopbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17, 1, 6),
    _PrvtEfmOamLoopbackDelay_Type()
)
prvtEfmOamLoopbackDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackDelay.setStatus("current")


class _PrvtEfmOamLoopbackTimeout_Type(Unsigned32):
    """Custom type prvtEfmOamLoopbackTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PrvtEfmOamLoopbackTimeout_Type.__name__ = "Unsigned32"
_PrvtEfmOamLoopbackTimeout_Object = MibTableColumn
prvtEfmOamLoopbackTimeout = _PrvtEfmOamLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17, 1, 7),
    _PrvtEfmOamLoopbackTimeout_Type()
)
prvtEfmOamLoopbackTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackTimeout.setStatus("current")


class _PrvtEfmOamLoopbackResultsClear_Type(Integer32):
    """Custom type prvtEfmOamLoopbackResultsClear based on Integer32"""
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


_PrvtEfmOamLoopbackResultsClear_Type.__name__ = "Integer32"
_PrvtEfmOamLoopbackResultsClear_Object = MibTableColumn
prvtEfmOamLoopbackResultsClear = _PrvtEfmOamLoopbackResultsClear_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 17, 1, 8),
    _PrvtEfmOamLoopbackResultsClear_Type()
)
prvtEfmOamLoopbackResultsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultsClear.setStatus("current")
_PrvtEfmOamLoopbackResultTable_Object = MibTable
prvtEfmOamLoopbackResultTable = _PrvtEfmOamLoopbackResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18)
)
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultTable.setStatus("current")
_PrvtEfmOamLoopbackResultEntry_Object = MibTableRow
prvtEfmOamLoopbackResultEntry = _PrvtEfmOamLoopbackResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1)
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
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 1),
    _PrvtEfmOamLoopbackResultStatus_Type()
)
prvtEfmOamLoopbackResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultStatus.setStatus("current")
_PrvtEfmOamLoopbackResultSentPackets_Type = Counter32
_PrvtEfmOamLoopbackResultSentPackets_Object = MibTableColumn
prvtEfmOamLoopbackResultSentPackets = _PrvtEfmOamLoopbackResultSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 2),
    _PrvtEfmOamLoopbackResultSentPackets_Type()
)
prvtEfmOamLoopbackResultSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultSentPackets.setStatus("current")
_PrvtEfmOamLoopbackResultReceivedPackets_Type = Counter32
_PrvtEfmOamLoopbackResultReceivedPackets_Object = MibTableColumn
prvtEfmOamLoopbackResultReceivedPackets = _PrvtEfmOamLoopbackResultReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 3),
    _PrvtEfmOamLoopbackResultReceivedPackets_Type()
)
prvtEfmOamLoopbackResultReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultReceivedPackets.setStatus("current")
_PrvtEfmOamLoopbackResultRateBurst_Type = OctetString
_PrvtEfmOamLoopbackResultRateBurst_Object = MibTableColumn
prvtEfmOamLoopbackResultRateBurst = _PrvtEfmOamLoopbackResultRateBurst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 4),
    _PrvtEfmOamLoopbackResultRateBurst_Type()
)
prvtEfmOamLoopbackResultRateBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultRateBurst.setStatus("current")
_PrvtEfmOamLoopbackResultLocalInOctets_Type = OctetString
_PrvtEfmOamLoopbackResultLocalInOctets_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalInOctets = _PrvtEfmOamLoopbackResultLocalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 5),
    _PrvtEfmOamLoopbackResultLocalInOctets_Type()
)
prvtEfmOamLoopbackResultLocalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalInOctets.setStatus("current")
_PrvtEfmOamLoopbackResultLocalOutOctets_Type = OctetString
_PrvtEfmOamLoopbackResultLocalOutOctets_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalOutOctets = _PrvtEfmOamLoopbackResultLocalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 6),
    _PrvtEfmOamLoopbackResultLocalOutOctets_Type()
)
prvtEfmOamLoopbackResultLocalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalOutOctets.setStatus("current")
_PrvtEfmOamLoopbackResultLocalInUcastPkts_Type = OctetString
_PrvtEfmOamLoopbackResultLocalInUcastPkts_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalInUcastPkts = _PrvtEfmOamLoopbackResultLocalInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 7),
    _PrvtEfmOamLoopbackResultLocalInUcastPkts_Type()
)
prvtEfmOamLoopbackResultLocalInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalInUcastPkts.setStatus("current")
_PrvtEfmOamLoopbackResultLocalOutUcastPkts_Type = OctetString
_PrvtEfmOamLoopbackResultLocalOutUcastPkts_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalOutUcastPkts = _PrvtEfmOamLoopbackResultLocalOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 8),
    _PrvtEfmOamLoopbackResultLocalOutUcastPkts_Type()
)
prvtEfmOamLoopbackResultLocalOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalOutUcastPkts.setStatus("current")
_PrvtEfmOamLoopbackResultLocalInNUcastPkts_Type = OctetString
_PrvtEfmOamLoopbackResultLocalInNUcastPkts_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalInNUcastPkts = _PrvtEfmOamLoopbackResultLocalInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 9),
    _PrvtEfmOamLoopbackResultLocalInNUcastPkts_Type()
)
prvtEfmOamLoopbackResultLocalInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalInNUcastPkts.setStatus("current")
_PrvtEfmOamLoopbackResultLocalOutNUcastPkts_Type = OctetString
_PrvtEfmOamLoopbackResultLocalOutNUcastPkts_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalOutNUcastPkts = _PrvtEfmOamLoopbackResultLocalOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 10),
    _PrvtEfmOamLoopbackResultLocalOutNUcastPkts_Type()
)
prvtEfmOamLoopbackResultLocalOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalOutNUcastPkts.setStatus("current")
_PrvtEfmOamLoopbackResultLocalInDiscards_Type = OctetString
_PrvtEfmOamLoopbackResultLocalInDiscards_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalInDiscards = _PrvtEfmOamLoopbackResultLocalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 11),
    _PrvtEfmOamLoopbackResultLocalInDiscards_Type()
)
prvtEfmOamLoopbackResultLocalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalInDiscards.setStatus("current")
_PrvtEfmOamLoopbackResultLocalOutDiscards_Type = OctetString
_PrvtEfmOamLoopbackResultLocalOutDiscards_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalOutDiscards = _PrvtEfmOamLoopbackResultLocalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 12),
    _PrvtEfmOamLoopbackResultLocalOutDiscards_Type()
)
prvtEfmOamLoopbackResultLocalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalOutDiscards.setStatus("current")
_PrvtEfmOamLoopbackResultLocalInErrors_Type = OctetString
_PrvtEfmOamLoopbackResultLocalInErrors_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalInErrors = _PrvtEfmOamLoopbackResultLocalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 13),
    _PrvtEfmOamLoopbackResultLocalInErrors_Type()
)
prvtEfmOamLoopbackResultLocalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalInErrors.setStatus("current")
_PrvtEfmOamLoopbackResultLocalOutErrors_Type = OctetString
_PrvtEfmOamLoopbackResultLocalOutErrors_Object = MibTableColumn
prvtEfmOamLoopbackResultLocalOutErrors = _PrvtEfmOamLoopbackResultLocalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 18, 1, 14),
    _PrvtEfmOamLoopbackResultLocalOutErrors_Type()
)
prvtEfmOamLoopbackResultLocalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamLoopbackResultLocalOutErrors.setStatus("current")
_PrvtEfmOamPeerTable_Object = MibTable
prvtEfmOamPeerTable = _PrvtEfmOamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19)
)
if mibBuilder.loadTexts:
    prvtEfmOamPeerTable.setStatus("current")
_PrvtEfmOamPeerEntry_Object = MibTableRow
prvtEfmOamPeerEntry = _PrvtEfmOamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1)
)
prvtEfmOamPeerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamPeerEntry.setStatus("current")
_PrvtEfmOamPeerMacAddress_Type = MacAddress
_PrvtEfmOamPeerMacAddress_Object = MibTableColumn
prvtEfmOamPeerMacAddress = _PrvtEfmOamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 1),
    _PrvtEfmOamPeerMacAddress_Type()
)
prvtEfmOamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerMacAddress.setStatus("current")
_PrvtEfmOamPeerVendorOui_Type = OctetString
_PrvtEfmOamPeerVendorOui_Object = MibTableColumn
prvtEfmOamPeerVendorOui = _PrvtEfmOamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 2),
    _PrvtEfmOamPeerVendorOui_Type()
)
prvtEfmOamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerVendorOui.setStatus("current")
_PrvtEfmOamPeerVendorInfo_Type = Unsigned32
_PrvtEfmOamPeerVendorInfo_Object = MibTableColumn
prvtEfmOamPeerVendorInfo = _PrvtEfmOamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 3),
    _PrvtEfmOamPeerVendorInfo_Type()
)
prvtEfmOamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerVendorInfo.setStatus("current")


class _PrvtEfmOamPeerRole_Type(Integer32):
    """Custom type prvtEfmOamPeerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2),
          ("unknown", 3))
    )


_PrvtEfmOamPeerRole_Type.__name__ = "Integer32"
_PrvtEfmOamPeerRole_Object = MibTableColumn
prvtEfmOamPeerRole = _PrvtEfmOamPeerRole_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 4),
    _PrvtEfmOamPeerRole_Type()
)
prvtEfmOamPeerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerRole.setStatus("current")
_PrvtEfmOamPeerMaxOamPduSize_Type = Unsigned32
_PrvtEfmOamPeerMaxOamPduSize_Object = MibTableColumn
prvtEfmOamPeerMaxOamPduSize = _PrvtEfmOamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 5),
    _PrvtEfmOamPeerMaxOamPduSize_Type()
)
prvtEfmOamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerMaxOamPduSize.setStatus("current")
_PrvtEfmOamPeerConfigRevision_Type = Unsigned32
_PrvtEfmOamPeerConfigRevision_Object = MibTableColumn
prvtEfmOamPeerConfigRevision = _PrvtEfmOamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 6),
    _PrvtEfmOamPeerConfigRevision_Type()
)
prvtEfmOamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerConfigRevision.setStatus("current")


class _PrvtEfmOamPeerFunctionsSupported_Type(Bits):
    """Custom type prvtEfmOamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_PrvtEfmOamPeerFunctionsSupported_Type.__name__ = "Bits"
_PrvtEfmOamPeerFunctionsSupported_Object = MibTableColumn
prvtEfmOamPeerFunctionsSupported = _PrvtEfmOamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 7),
    _PrvtEfmOamPeerFunctionsSupported_Type()
)
prvtEfmOamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerFunctionsSupported.setStatus("current")
_PrvtEfmOamPeerPort_Type = OctetString
_PrvtEfmOamPeerPort_Object = MibTableColumn
prvtEfmOamPeerPort = _PrvtEfmOamPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 8),
    _PrvtEfmOamPeerPort_Type()
)
prvtEfmOamPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerPort.setStatus("current")
_PrvtEfmOamPeerName_Type = OctetString
_PrvtEfmOamPeerName_Object = MibTableColumn
prvtEfmOamPeerName = _PrvtEfmOamPeerName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 9),
    _PrvtEfmOamPeerName_Type()
)
prvtEfmOamPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerName.setStatus("current")


class _PrvtEfmOamPeerMode_Type(Integer32):
    """Custom type prvtEfmOamPeerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("enhanced", 2))
    )


_PrvtEfmOamPeerMode_Type.__name__ = "Integer32"
_PrvtEfmOamPeerMode_Object = MibTableColumn
prvtEfmOamPeerMode = _PrvtEfmOamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 19, 1, 10),
    _PrvtEfmOamPeerMode_Type()
)
prvtEfmOamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamPeerMode.setStatus("current")
_PrvtEfmOamStatisticsTable_Object = MibTable
prvtEfmOamStatisticsTable = _PrvtEfmOamStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20)
)
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsTable.setStatus("current")
_PrvtEfmOamStatisticsEntry_Object = MibTableRow
prvtEfmOamStatisticsEntry = _PrvtEfmOamStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1)
)
prvtEfmOamStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsEntry.setStatus("current")
_PrvtEfmOamStatisticsInformationTx_Type = Counter32
_PrvtEfmOamStatisticsInformationTx_Object = MibTableColumn
prvtEfmOamStatisticsInformationTx = _PrvtEfmOamStatisticsInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 1),
    _PrvtEfmOamStatisticsInformationTx_Type()
)
prvtEfmOamStatisticsInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsInformationTx.setStatus("current")
_PrvtEfmOamStatisticsInformationRx_Type = Counter32
_PrvtEfmOamStatisticsInformationRx_Object = MibTableColumn
prvtEfmOamStatisticsInformationRx = _PrvtEfmOamStatisticsInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 2),
    _PrvtEfmOamStatisticsInformationRx_Type()
)
prvtEfmOamStatisticsInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsInformationRx.setStatus("current")
_PrvtEfmOamStatisticsUniqueEventNotificationTx_Type = Counter32
_PrvtEfmOamStatisticsUniqueEventNotificationTx_Object = MibTableColumn
prvtEfmOamStatisticsUniqueEventNotificationTx = _PrvtEfmOamStatisticsUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 3),
    _PrvtEfmOamStatisticsUniqueEventNotificationTx_Type()
)
prvtEfmOamStatisticsUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsUniqueEventNotificationTx.setStatus("current")
_PrvtEfmOamStatisticsUniqueEventNotificationRx_Type = Counter32
_PrvtEfmOamStatisticsUniqueEventNotificationRx_Object = MibTableColumn
prvtEfmOamStatisticsUniqueEventNotificationRx = _PrvtEfmOamStatisticsUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 4),
    _PrvtEfmOamStatisticsUniqueEventNotificationRx_Type()
)
prvtEfmOamStatisticsUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsUniqueEventNotificationRx.setStatus("current")
_PrvtEfmOamStatisticsDuplicateEventNotificationTx_Type = Counter32
_PrvtEfmOamStatisticsDuplicateEventNotificationTx_Object = MibTableColumn
prvtEfmOamStatisticsDuplicateEventNotificationTx = _PrvtEfmOamStatisticsDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 5),
    _PrvtEfmOamStatisticsDuplicateEventNotificationTx_Type()
)
prvtEfmOamStatisticsDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsDuplicateEventNotificationTx.setStatus("current")
_PrvtEfmOamStatisticsDuplicateEventNotificationRx_Type = Counter32
_PrvtEfmOamStatisticsDuplicateEventNotificationRx_Object = MibTableColumn
prvtEfmOamStatisticsDuplicateEventNotificationRx = _PrvtEfmOamStatisticsDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 6),
    _PrvtEfmOamStatisticsDuplicateEventNotificationRx_Type()
)
prvtEfmOamStatisticsDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsDuplicateEventNotificationRx.setStatus("current")
_PrvtEfmOamStatisticsLoopbackControlTx_Type = Counter32
_PrvtEfmOamStatisticsLoopbackControlTx_Object = MibTableColumn
prvtEfmOamStatisticsLoopbackControlTx = _PrvtEfmOamStatisticsLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 7),
    _PrvtEfmOamStatisticsLoopbackControlTx_Type()
)
prvtEfmOamStatisticsLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsLoopbackControlTx.setStatus("current")
_PrvtEfmOamStatisticsLoopbackControlRx_Type = Counter32
_PrvtEfmOamStatisticsLoopbackControlRx_Object = MibTableColumn
prvtEfmOamStatisticsLoopbackControlRx = _PrvtEfmOamStatisticsLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 8),
    _PrvtEfmOamStatisticsLoopbackControlRx_Type()
)
prvtEfmOamStatisticsLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsLoopbackControlRx.setStatus("current")
_PrvtEfmOamStatisticsVariableRequestTx_Type = Counter32
_PrvtEfmOamStatisticsVariableRequestTx_Object = MibTableColumn
prvtEfmOamStatisticsVariableRequestTx = _PrvtEfmOamStatisticsVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 9),
    _PrvtEfmOamStatisticsVariableRequestTx_Type()
)
prvtEfmOamStatisticsVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsVariableRequestTx.setStatus("current")
_PrvtEfmOamStatisticsVariableRequestRx_Type = Counter32
_PrvtEfmOamStatisticsVariableRequestRx_Object = MibTableColumn
prvtEfmOamStatisticsVariableRequestRx = _PrvtEfmOamStatisticsVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 10),
    _PrvtEfmOamStatisticsVariableRequestRx_Type()
)
prvtEfmOamStatisticsVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsVariableRequestRx.setStatus("current")
_PrvtEfmOamStatisticsVariableResponseTx_Type = Counter32
_PrvtEfmOamStatisticsVariableResponseTx_Object = MibTableColumn
prvtEfmOamStatisticsVariableResponseTx = _PrvtEfmOamStatisticsVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 11),
    _PrvtEfmOamStatisticsVariableResponseTx_Type()
)
prvtEfmOamStatisticsVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsVariableResponseTx.setStatus("current")
_PrvtEfmOamStatisticsVariableResponseRx_Type = Counter32
_PrvtEfmOamStatisticsVariableResponseRx_Object = MibTableColumn
prvtEfmOamStatisticsVariableResponseRx = _PrvtEfmOamStatisticsVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 12),
    _PrvtEfmOamStatisticsVariableResponseRx_Type()
)
prvtEfmOamStatisticsVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsVariableResponseRx.setStatus("current")
_PrvtEfmOamStatisticsOrganizationSpecificTx_Type = Counter32
_PrvtEfmOamStatisticsOrganizationSpecificTx_Object = MibTableColumn
prvtEfmOamStatisticsOrganizationSpecificTx = _PrvtEfmOamStatisticsOrganizationSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 13),
    _PrvtEfmOamStatisticsOrganizationSpecificTx_Type()
)
prvtEfmOamStatisticsOrganizationSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsOrganizationSpecificTx.setStatus("current")
_PrvtEfmOamStatisticsOrganizationSpecificRx_Type = Counter32
_PrvtEfmOamStatisticsOrganizationSpecificRx_Object = MibTableColumn
prvtEfmOamStatisticsOrganizationSpecificRx = _PrvtEfmOamStatisticsOrganizationSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 14),
    _PrvtEfmOamStatisticsOrganizationSpecificRx_Type()
)
prvtEfmOamStatisticsOrganizationSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsOrganizationSpecificRx.setStatus("current")
_PrvtEfmOamStatisticsUnsupportedCodesTx_Type = Counter32
_PrvtEfmOamStatisticsUnsupportedCodesTx_Object = MibTableColumn
prvtEfmOamStatisticsUnsupportedCodesTx = _PrvtEfmOamStatisticsUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 15),
    _PrvtEfmOamStatisticsUnsupportedCodesTx_Type()
)
prvtEfmOamStatisticsUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsUnsupportedCodesTx.setStatus("current")
_PrvtEfmOamStatisticsUnsupportedCodesRx_Type = Counter32
_PrvtEfmOamStatisticsUnsupportedCodesRx_Object = MibTableColumn
prvtEfmOamStatisticsUnsupportedCodesRx = _PrvtEfmOamStatisticsUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 16),
    _PrvtEfmOamStatisticsUnsupportedCodesRx_Type()
)
prvtEfmOamStatisticsUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsUnsupportedCodesRx.setStatus("current")
_PrvtEfmOamStatisticsFramesLostDueToOam_Type = Counter32
_PrvtEfmOamStatisticsFramesLostDueToOam_Object = MibTableColumn
prvtEfmOamStatisticsFramesLostDueToOam = _PrvtEfmOamStatisticsFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 20, 1, 17),
    _PrvtEfmOamStatisticsFramesLostDueToOam_Type()
)
prvtEfmOamStatisticsFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamStatisticsFramesLostDueToOam.setStatus("current")
_PrvtEfmOamEventConfigTable_Object = MibTable
prvtEfmOamEventConfigTable = _PrvtEfmOamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 21)
)
if mibBuilder.loadTexts:
    prvtEfmOamEventConfigTable.setStatus("current")
_PrvtEfmOamEventConfigEntry_Object = MibTableRow
prvtEfmOamEventConfigEntry = _PrvtEfmOamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 21, 1)
)
prvtEfmOamEventConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamEventConfigEntry.setStatus("current")


class _PrvtEfmOamEventConfigErrorSymbolPeriodWindow_Type(Unsigned32):
    """Custom type prvtEfmOamEventConfigErrorSymbolPeriodWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PrvtEfmOamEventConfigErrorSymbolPeriodWindow_Type.__name__ = "Unsigned32"
_PrvtEfmOamEventConfigErrorSymbolPeriodWindow_Object = MibTableColumn
prvtEfmOamEventConfigErrorSymbolPeriodWindow = _PrvtEfmOamEventConfigErrorSymbolPeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 21, 1, 1),
    _PrvtEfmOamEventConfigErrorSymbolPeriodWindow_Type()
)
prvtEfmOamEventConfigErrorSymbolPeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventConfigErrorSymbolPeriodWindow.setStatus("current")


class _PrvtEfmOamEventConfigErrorSymbolPeriodThreshold_Type(Unsigned32):
    """Custom type prvtEfmOamEventConfigErrorSymbolPeriodThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_PrvtEfmOamEventConfigErrorSymbolPeriodThreshold_Type.__name__ = "Unsigned32"
_PrvtEfmOamEventConfigErrorSymbolPeriodThreshold_Object = MibTableColumn
prvtEfmOamEventConfigErrorSymbolPeriodThreshold = _PrvtEfmOamEventConfigErrorSymbolPeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 21, 1, 2),
    _PrvtEfmOamEventConfigErrorSymbolPeriodThreshold_Type()
)
prvtEfmOamEventConfigErrorSymbolPeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventConfigErrorSymbolPeriodThreshold.setStatus("current")
_PrvtEfmOamEventConfigErrorSymbolPeriodEventNotificationEnable_Type = TruthValue
_PrvtEfmOamEventConfigErrorSymbolPeriodEventNotificationEnable_Object = MibTableColumn
prvtEfmOamEventConfigErrorSymbolPeriodEventNotificationEnable = _PrvtEfmOamEventConfigErrorSymbolPeriodEventNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 21, 1, 3),
    _PrvtEfmOamEventConfigErrorSymbolPeriodEventNotificationEnable_Type()
)
prvtEfmOamEventConfigErrorSymbolPeriodEventNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventConfigErrorSymbolPeriodEventNotificationEnable.setStatus("current")
_PrvtEfmOamEventConfigErrorFrameWindow_Type = Unsigned32
_PrvtEfmOamEventConfigErrorFrameWindow_Object = MibTableColumn
prvtEfmOamEventConfigErrorFrameWindow = _PrvtEfmOamEventConfigErrorFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 21, 1, 4),
    _PrvtEfmOamEventConfigErrorFrameWindow_Type()
)
prvtEfmOamEventConfigErrorFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventConfigErrorFrameWindow.setStatus("current")
_PrvtEfmOamEventConfigErrorFrameThreshold_Type = Unsigned32
_PrvtEfmOamEventConfigErrorFrameThreshold_Object = MibTableColumn
prvtEfmOamEventConfigErrorFrameThreshold = _PrvtEfmOamEventConfigErrorFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 21, 1, 5),
    _PrvtEfmOamEventConfigErrorFrameThreshold_Type()
)
prvtEfmOamEventConfigErrorFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventConfigErrorFrameThreshold.setStatus("current")
_PrvtEfmOamEventConfigErrorFrameEventNotificationEnable_Type = TruthValue
_PrvtEfmOamEventConfigErrorFrameEventNotificationEnable_Object = MibTableColumn
prvtEfmOamEventConfigErrorFrameEventNotificationEnable = _PrvtEfmOamEventConfigErrorFrameEventNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 21, 1, 6),
    _PrvtEfmOamEventConfigErrorFrameEventNotificationEnable_Type()
)
prvtEfmOamEventConfigErrorFrameEventNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventConfigErrorFrameEventNotificationEnable.setStatus("current")
_PrvtEfmOamEventConfigDyingGaspEnable_Type = TruthValue
_PrvtEfmOamEventConfigDyingGaspEnable_Object = MibTableColumn
prvtEfmOamEventConfigDyingGaspEnable = _PrvtEfmOamEventConfigDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 21, 1, 7),
    _PrvtEfmOamEventConfigDyingGaspEnable_Type()
)
prvtEfmOamEventConfigDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamEventConfigDyingGaspEnable.setStatus("current")
_PrvtEfmOamEventLogTable_Object = MibTable
prvtEfmOamEventLogTable = _PrvtEfmOamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22)
)
if mibBuilder.loadTexts:
    prvtEfmOamEventLogTable.setStatus("current")
_PrvtEfmOamEventLogEntry_Object = MibTableRow
prvtEfmOamEventLogEntry = _PrvtEfmOamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1)
)
prvtEfmOamEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogId"),
)
if mibBuilder.loadTexts:
    prvtEfmOamEventLogEntry.setStatus("current")
_PrvtEfmOamEventLogId_Type = Unsigned32
_PrvtEfmOamEventLogId_Object = MibTableColumn
prvtEfmOamEventLogId = _PrvtEfmOamEventLogId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 1),
    _PrvtEfmOamEventLogId_Type()
)
prvtEfmOamEventLogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogId.setStatus("current")
_PrvtEfmOamEventLogTimeStamp_Type = Unsigned32
_PrvtEfmOamEventLogTimeStamp_Object = MibTableColumn
prvtEfmOamEventLogTimeStamp = _PrvtEfmOamEventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 2),
    _PrvtEfmOamEventLogTimeStamp_Type()
)
prvtEfmOamEventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogTimeStamp.setStatus("current")
_PrvtEfmOamEventLogOui_Type = OctetString
_PrvtEfmOamEventLogOui_Object = MibTableColumn
prvtEfmOamEventLogOui = _PrvtEfmOamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 3),
    _PrvtEfmOamEventLogOui_Type()
)
prvtEfmOamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogOui.setStatus("current")


class _PrvtEfmOamEventLogType_Type(Integer32):
    """Custom type prvtEfmOamEventLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              256,
              257,
              258)
        )
    )
    namedValues = NamedValues(
        *(("erroredSymbolEvent", 1),
          ("erroredFramePeriodEvent", 2),
          ("erroredFrameEvent", 3),
          ("erroredFrameSecondsEvent", 4),
          ("linkFault", 256),
          ("dyingGaspEvent", 257),
          ("criticalEvent", 258))
    )


_PrvtEfmOamEventLogType_Type.__name__ = "Integer32"
_PrvtEfmOamEventLogType_Object = MibTableColumn
prvtEfmOamEventLogType = _PrvtEfmOamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 4),
    _PrvtEfmOamEventLogType_Type()
)
prvtEfmOamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogType.setStatus("current")


class _PrvtEfmOamEventLogLocation_Type(Integer32):
    """Custom type prvtEfmOamEventLogLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_PrvtEfmOamEventLogLocation_Type.__name__ = "Integer32"
_PrvtEfmOamEventLogLocation_Object = MibTableColumn
prvtEfmOamEventLogLocation = _PrvtEfmOamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 5),
    _PrvtEfmOamEventLogLocation_Type()
)
prvtEfmOamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogLocation.setStatus("current")
_PrvtEfmOamEventLogWindow_Type = Counter64
_PrvtEfmOamEventLogWindow_Object = MibTableColumn
prvtEfmOamEventLogWindow = _PrvtEfmOamEventLogWindow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 6),
    _PrvtEfmOamEventLogWindow_Type()
)
prvtEfmOamEventLogWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogWindow.setStatus("current")
_PrvtEfmOamEventLogThreshold_Type = Counter64
_PrvtEfmOamEventLogThreshold_Object = MibTableColumn
prvtEfmOamEventLogThreshold = _PrvtEfmOamEventLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 7),
    _PrvtEfmOamEventLogThreshold_Type()
)
prvtEfmOamEventLogThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogThreshold.setStatus("current")
_PrvtEfmOamEventLogValue_Type = Counter64
_PrvtEfmOamEventLogValue_Object = MibTableColumn
prvtEfmOamEventLogValue = _PrvtEfmOamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 8),
    _PrvtEfmOamEventLogValue_Type()
)
prvtEfmOamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogValue.setStatus("current")
_PrvtEfmOamEventLogRunningTotal_Type = Counter64
_PrvtEfmOamEventLogRunningTotal_Object = MibTableColumn
prvtEfmOamEventLogRunningTotal = _PrvtEfmOamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 9),
    _PrvtEfmOamEventLogRunningTotal_Type()
)
prvtEfmOamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogRunningTotal.setStatus("current")
_PrvtEfmOamEventLogEventTotal_Type = Unsigned32
_PrvtEfmOamEventLogEventTotal_Object = MibTableColumn
prvtEfmOamEventLogEventTotal = _PrvtEfmOamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 22, 1, 10),
    _PrvtEfmOamEventLogEventTotal_Type()
)
prvtEfmOamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamEventLogEventTotal.setStatus("current")
_PrvtEfmOamInterfaceTable_Object = MibTable
prvtEfmOamInterfaceTable = _PrvtEfmOamInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23)
)
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceTable.setStatus("current")
_PrvtEfmOamInterfaceEntry_Object = MibTableRow
prvtEfmOamInterfaceEntry = _PrvtEfmOamInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1)
)
prvtEfmOamInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceEntry.setStatus("current")
_PrvtEfmOamInterfaceEnable_Type = TruthValue
_PrvtEfmOamInterfaceEnable_Object = MibTableColumn
prvtEfmOamInterfaceEnable = _PrvtEfmOamInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 1),
    _PrvtEfmOamInterfaceEnable_Type()
)
prvtEfmOamInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceEnable.setStatus("current")


class _PrvtEfmOamInterfaceOperStatus_Type(Integer32):
    """Custom type prvtEfmOamInterfaceOperStatus based on Integer32"""
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
        *(("disabled", 1),
          ("linkFault", 2),
          ("passiveWait", 3),
          ("activeSendLocal", 4),
          ("sendLocalAndRemote", 5),
          ("sendLocalAndRemoteOk", 6),
          ("oamPeeringLocallyRejected", 7),
          ("oamPeeringRemoteRejected", 8),
          ("operational", 9),
          ("nonOperHalfDuplex", 10))
    )


_PrvtEfmOamInterfaceOperStatus_Type.__name__ = "Integer32"
_PrvtEfmOamInterfaceOperStatus_Object = MibTableColumn
prvtEfmOamInterfaceOperStatus = _PrvtEfmOamInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 2),
    _PrvtEfmOamInterfaceOperStatus_Type()
)
prvtEfmOamInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceOperStatus.setStatus("current")


class _PrvtEfmOamInterfaceRole_Type(Integer32):
    """Custom type prvtEfmOamInterfaceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2))
    )


_PrvtEfmOamInterfaceRole_Type.__name__ = "Integer32"
_PrvtEfmOamInterfaceRole_Object = MibTableColumn
prvtEfmOamInterfaceRole = _PrvtEfmOamInterfaceRole_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 3),
    _PrvtEfmOamInterfaceRole_Type()
)
prvtEfmOamInterfaceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceRole.setStatus("current")
_PrvtEfmOamInterfaceMaxPduSize_Type = Unsigned32
_PrvtEfmOamInterfaceMaxPduSize_Object = MibTableColumn
prvtEfmOamInterfaceMaxPduSize = _PrvtEfmOamInterfaceMaxPduSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 4),
    _PrvtEfmOamInterfaceMaxPduSize_Type()
)
prvtEfmOamInterfaceMaxPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceMaxPduSize.setStatus("current")
_PrvtEfmOamInterfaceConfigRevision_Type = Unsigned32
_PrvtEfmOamInterfaceConfigRevision_Object = MibTableColumn
prvtEfmOamInterfaceConfigRevision = _PrvtEfmOamInterfaceConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 5),
    _PrvtEfmOamInterfaceConfigRevision_Type()
)
prvtEfmOamInterfaceConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceConfigRevision.setStatus("current")


class _PrvtEfmOamInterfaceFunctionsSupported_Type(Bits):
    """Custom type prvtEfmOamInterfaceFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_PrvtEfmOamInterfaceFunctionsSupported_Type.__name__ = "Bits"
_PrvtEfmOamInterfaceFunctionsSupported_Object = MibTableColumn
prvtEfmOamInterfaceFunctionsSupported = _PrvtEfmOamInterfaceFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 6),
    _PrvtEfmOamInterfaceFunctionsSupported_Type()
)
prvtEfmOamInterfaceFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceFunctionsSupported.setStatus("current")
_PrvtEfmOamInterfacePacketSent_Type = Unsigned32
_PrvtEfmOamInterfacePacketSent_Object = MibTableColumn
prvtEfmOamInterfacePacketSent = _PrvtEfmOamInterfacePacketSent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 7),
    _PrvtEfmOamInterfacePacketSent_Type()
)
prvtEfmOamInterfacePacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamInterfacePacketSent.setStatus("current")
_PrvtEfmOamInterfacePacketReceived_Type = Unsigned32
_PrvtEfmOamInterfacePacketReceived_Object = MibTableColumn
prvtEfmOamInterfacePacketReceived = _PrvtEfmOamInterfacePacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 8),
    _PrvtEfmOamInterfacePacketReceived_Type()
)
prvtEfmOamInterfacePacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamInterfacePacketReceived.setStatus("current")


class _PrvtEfmOamInterfaceMode_Type(Integer32):
    """Custom type prvtEfmOamInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("enhanced", 2))
    )


_PrvtEfmOamInterfaceMode_Type.__name__ = "Integer32"
_PrvtEfmOamInterfaceMode_Object = MibTableColumn
prvtEfmOamInterfaceMode = _PrvtEfmOamInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 9),
    _PrvtEfmOamInterfaceMode_Type()
)
prvtEfmOamInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceMode.setStatus("current")


class _PrvtEfmOamInterfaceLoopbackStatus_Type(Integer32):
    """Custom type prvtEfmOamInterfaceLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("initiatingLoopback", 2),
          ("remoteLoopback", 3),
          ("terminatingLoopback", 4),
          ("localLoopback", 5),
          ("unknownLoopback", 6))
    )


_PrvtEfmOamInterfaceLoopbackStatus_Type.__name__ = "Integer32"
_PrvtEfmOamInterfaceLoopbackStatus_Object = MibTableColumn
prvtEfmOamInterfaceLoopbackStatus = _PrvtEfmOamInterfaceLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 10),
    _PrvtEfmOamInterfaceLoopbackStatus_Type()
)
prvtEfmOamInterfaceLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceLoopbackStatus.setStatus("current")
_PrvtEfmOamInterfaceAcceptLoopbackCommands_Type = TruthValue
_PrvtEfmOamInterfaceAcceptLoopbackCommands_Object = MibTableColumn
prvtEfmOamInterfaceAcceptLoopbackCommands = _PrvtEfmOamInterfaceAcceptLoopbackCommands_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 11),
    _PrvtEfmOamInterfaceAcceptLoopbackCommands_Type()
)
prvtEfmOamInterfaceAcceptLoopbackCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceAcceptLoopbackCommands.setStatus("current")


class _PrvtEfmOamInterfaceEventReturnShutdown_Type(Unsigned32):
    """Custom type prvtEfmOamInterfaceEventReturnShutdown based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PrvtEfmOamInterfaceEventReturnShutdown_Type.__name__ = "Unsigned32"
_PrvtEfmOamInterfaceEventReturnShutdown_Object = MibTableColumn
prvtEfmOamInterfaceEventReturnShutdown = _PrvtEfmOamInterfaceEventReturnShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 23, 1, 12),
    _PrvtEfmOamInterfaceEventReturnShutdown_Type()
)
prvtEfmOamInterfaceEventReturnShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEfmOamInterfaceEventReturnShutdown.setStatus("current")
_PrvtEfmOamEventForwardStatusTable_Object = MibTable
prvtEfmOamEventForwardStatusTable = _PrvtEfmOamEventForwardStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 24)
)
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardStatusTable.setStatus("current")
_PrvtEfmOamEventForwardStatusEntry_Object = MibTableRow
prvtEfmOamEventForwardStatusEntry = _PrvtEfmOamEventForwardStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 24, 1)
)
prvtEfmOamEventForwardStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-EFM-OAM-MIB", "prvtEfmOamEventForwardStatusIdx"),
)
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardStatusEntry.setStatus("current")
_PrvtEfmOamEventForwardStatusIdx_Type = InterfaceIndex
_PrvtEfmOamEventForwardStatusIdx_Object = MibTableColumn
prvtEfmOamEventForwardStatusIdx = _PrvtEfmOamEventForwardStatusIdx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 24, 1, 1),
    _PrvtEfmOamEventForwardStatusIdx_Type()
)
prvtEfmOamEventForwardStatusIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardStatusIdx.setStatus("current")
_PrvtEfmOamEventForwardStatusRowStatus_Type = RowStatus
_PrvtEfmOamEventForwardStatusRowStatus_Object = MibTableColumn
prvtEfmOamEventForwardStatusRowStatus = _PrvtEfmOamEventForwardStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 24, 1, 2),
    _PrvtEfmOamEventForwardStatusRowStatus_Type()
)
prvtEfmOamEventForwardStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardStatusRowStatus.setStatus("current")
_PrvtEfmOamEventForwardShutdownTable_Object = MibTable
prvtEfmOamEventForwardShutdownTable = _PrvtEfmOamEventForwardShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 25)
)
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardShutdownTable.setStatus("current")
_PrvtEfmOamEventForwardShutdownEntry_Object = MibTableRow
prvtEfmOamEventForwardShutdownEntry = _PrvtEfmOamEventForwardShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 25, 1)
)
prvtEfmOamEventForwardShutdownEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-EFM-OAM-MIB", "prvtEfmOamEventForwardShutdownIdx"),
)
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardShutdownEntry.setStatus("current")
_PrvtEfmOamEventForwardShutdownIdx_Type = InterfaceIndex
_PrvtEfmOamEventForwardShutdownIdx_Object = MibTableColumn
prvtEfmOamEventForwardShutdownIdx = _PrvtEfmOamEventForwardShutdownIdx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 25, 1, 1),
    _PrvtEfmOamEventForwardShutdownIdx_Type()
)
prvtEfmOamEventForwardShutdownIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardShutdownIdx.setStatus("current")
_PrvtEfmOamEventForwardShutdownRowStatus_Type = RowStatus
_PrvtEfmOamEventForwardShutdownRowStatus_Object = MibTableColumn
prvtEfmOamEventForwardShutdownRowStatus = _PrvtEfmOamEventForwardShutdownRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 1, 25, 1, 2),
    _PrvtEfmOamEventForwardShutdownRowStatus_Type()
)
prvtEfmOamEventForwardShutdownRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEfmOamEventForwardShutdownRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

prvtEfmOamLoopBackState = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 0, 1)
)
prvtEfmOamLoopBackState.setObjects(
      *(("PRVT-EFM-OAM-MIB", "prvtEfmOamInterfaceEnable"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamInterfaceRole"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamInterfaceLoopbackStatus"))
)
if mibBuilder.loadTexts:
    prvtEfmOamLoopBackState.setStatus(
        "current"
    )

prvtEfmOamDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 0, 2)
)
if mibBuilder.loadTexts:
    prvtEfmOamDyingGasp.setStatus(
        "current"
    )

prvtEfmOamThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 0, 3)
)
prvtEfmOamThresholdEvent.setObjects(
      *(("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogTimeStamp"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogOui"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogType"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogLocation"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogWindow"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogThreshold"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogValue"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogRunningTotal"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    prvtEfmOamThresholdEvent.setStatus(
        "current"
    )

prvtEfmOamNonThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 133, 0, 4)
)
prvtEfmOamNonThresholdEvent.setObjects(
      *(("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogTimeStamp"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogOui"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogType"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogLocation"),
        ("PRVT-EFM-OAM-MIB", "prvtEfmOamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    prvtEfmOamNonThresholdEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-EFM-OAM-MIB",
    **{"prvtEfmOamMIB": prvtEfmOamMIB,
       "prvtEfmOamNotifications": prvtEfmOamNotifications,
       "prvtEfmOamLoopBackState": prvtEfmOamLoopBackState,
       "prvtEfmOamDyingGasp": prvtEfmOamDyingGasp,
       "prvtEfmOamThresholdEvent": prvtEfmOamThresholdEvent,
       "prvtEfmOamNonThresholdEvent": prvtEfmOamNonThresholdEvent,
       "prvtEfmOamObjects": prvtEfmOamObjects,
       "prvtEfmOamEnable": prvtEfmOamEnable,
       "prvtEfmOamMultiPduCount": prvtEfmOamMultiPduCount,
       "prvtEfmOamRemoteEvent": prvtEfmOamRemoteEvent,
       "prvtEfmOamLogEvents": prvtEfmOamLogEvents,
       "prvtEfmOamPriority": prvtEfmOamPriority,
       "prvtEfmOamPriorityEnable": prvtEfmOamPriorityEnable,
       "prvtEfmOamKeepAliveInterval": prvtEfmOamKeepAliveInterval,
       "prvtEfmOamHelloInterval": prvtEfmOamHelloInterval,
       "prvtEfmOamHistoryLimit": prvtEfmOamHistoryLimit,
       "prvtEfmOamHistoryCount": prvtEfmOamHistoryCount,
       "prvtEfmOamHistoryClear": prvtEfmOamHistoryClear,
       "prvtEfmOamPacketSent": prvtEfmOamPacketSent,
       "prvtEfmOamPacketReceived": prvtEfmOamPacketReceived,
       "prvtEfmOamLocalMac": prvtEfmOamLocalMac,
       "prvtEfmOamPingTable": prvtEfmOamPingTable,
       "prvtEfmOamPingEntry": prvtEfmOamPingEntry,
       "prvtEfmOamPingRowStatus": prvtEfmOamPingRowStatus,
       "prvtEfmOamPingStatus": prvtEfmOamPingStatus,
       "prvtEfmOamPingEchoNumber": prvtEfmOamPingEchoNumber,
       "prvtEfmOamPingDelayTime": prvtEfmOamPingDelayTime,
       "prvtEfmOamPingTimeOut": prvtEfmOamPingTimeOut,
       "prvtEfmOamPingResultClear": prvtEfmOamPingResultClear,
       "prvtEfmOamPingResultTable": prvtEfmOamPingResultTable,
       "prvtEfmOamPingResultEntry": prvtEfmOamPingResultEntry,
       "prvtEfmOamPingResultStatus": prvtEfmOamPingResultStatus,
       "prvtEfmOamPingResultSentPackets": prvtEfmOamPingResultSentPackets,
       "prvtEfmOamPingResultReceivedPackets": prvtEfmOamPingResultReceivedPackets,
       "prvtEfmOamPingResultReceiveRate": prvtEfmOamPingResultReceiveRate,
       "prvtEfmOamPingResultTimeMin": prvtEfmOamPingResultTimeMin,
       "prvtEfmOamPingResultTimeMax": prvtEfmOamPingResultTimeMax,
       "prvtEfmOamPingResultAverageTime": prvtEfmOamPingResultAverageTime,
       "prvtEfmOamLoopbackTable": prvtEfmOamLoopbackTable,
       "prvtEfmOamLoopbackEntry": prvtEfmOamLoopbackEntry,
       "prvtEfmOamLoopbackRowStatus": prvtEfmOamLoopbackRowStatus,
       "prvtEfmOamLoopbackType": prvtEfmOamLoopbackType,
       "prvtEfmOamLoopbackStatus": prvtEfmOamLoopbackStatus,
       "prvtEfmOamLoopbackCount": prvtEfmOamLoopbackCount,
       "prvtEfmOamLoopbackPacketSize": prvtEfmOamLoopbackPacketSize,
       "prvtEfmOamLoopbackDelay": prvtEfmOamLoopbackDelay,
       "prvtEfmOamLoopbackTimeout": prvtEfmOamLoopbackTimeout,
       "prvtEfmOamLoopbackResultsClear": prvtEfmOamLoopbackResultsClear,
       "prvtEfmOamLoopbackResultTable": prvtEfmOamLoopbackResultTable,
       "prvtEfmOamLoopbackResultEntry": prvtEfmOamLoopbackResultEntry,
       "prvtEfmOamLoopbackResultStatus": prvtEfmOamLoopbackResultStatus,
       "prvtEfmOamLoopbackResultSentPackets": prvtEfmOamLoopbackResultSentPackets,
       "prvtEfmOamLoopbackResultReceivedPackets": prvtEfmOamLoopbackResultReceivedPackets,
       "prvtEfmOamLoopbackResultRateBurst": prvtEfmOamLoopbackResultRateBurst,
       "prvtEfmOamLoopbackResultLocalInOctets": prvtEfmOamLoopbackResultLocalInOctets,
       "prvtEfmOamLoopbackResultLocalOutOctets": prvtEfmOamLoopbackResultLocalOutOctets,
       "prvtEfmOamLoopbackResultLocalInUcastPkts": prvtEfmOamLoopbackResultLocalInUcastPkts,
       "prvtEfmOamLoopbackResultLocalOutUcastPkts": prvtEfmOamLoopbackResultLocalOutUcastPkts,
       "prvtEfmOamLoopbackResultLocalInNUcastPkts": prvtEfmOamLoopbackResultLocalInNUcastPkts,
       "prvtEfmOamLoopbackResultLocalOutNUcastPkts": prvtEfmOamLoopbackResultLocalOutNUcastPkts,
       "prvtEfmOamLoopbackResultLocalInDiscards": prvtEfmOamLoopbackResultLocalInDiscards,
       "prvtEfmOamLoopbackResultLocalOutDiscards": prvtEfmOamLoopbackResultLocalOutDiscards,
       "prvtEfmOamLoopbackResultLocalInErrors": prvtEfmOamLoopbackResultLocalInErrors,
       "prvtEfmOamLoopbackResultLocalOutErrors": prvtEfmOamLoopbackResultLocalOutErrors,
       "prvtEfmOamPeerTable": prvtEfmOamPeerTable,
       "prvtEfmOamPeerEntry": prvtEfmOamPeerEntry,
       "prvtEfmOamPeerMacAddress": prvtEfmOamPeerMacAddress,
       "prvtEfmOamPeerVendorOui": prvtEfmOamPeerVendorOui,
       "prvtEfmOamPeerVendorInfo": prvtEfmOamPeerVendorInfo,
       "prvtEfmOamPeerRole": prvtEfmOamPeerRole,
       "prvtEfmOamPeerMaxOamPduSize": prvtEfmOamPeerMaxOamPduSize,
       "prvtEfmOamPeerConfigRevision": prvtEfmOamPeerConfigRevision,
       "prvtEfmOamPeerFunctionsSupported": prvtEfmOamPeerFunctionsSupported,
       "prvtEfmOamPeerPort": prvtEfmOamPeerPort,
       "prvtEfmOamPeerName": prvtEfmOamPeerName,
       "prvtEfmOamPeerMode": prvtEfmOamPeerMode,
       "prvtEfmOamStatisticsTable": prvtEfmOamStatisticsTable,
       "prvtEfmOamStatisticsEntry": prvtEfmOamStatisticsEntry,
       "prvtEfmOamStatisticsInformationTx": prvtEfmOamStatisticsInformationTx,
       "prvtEfmOamStatisticsInformationRx": prvtEfmOamStatisticsInformationRx,
       "prvtEfmOamStatisticsUniqueEventNotificationTx": prvtEfmOamStatisticsUniqueEventNotificationTx,
       "prvtEfmOamStatisticsUniqueEventNotificationRx": prvtEfmOamStatisticsUniqueEventNotificationRx,
       "prvtEfmOamStatisticsDuplicateEventNotificationTx": prvtEfmOamStatisticsDuplicateEventNotificationTx,
       "prvtEfmOamStatisticsDuplicateEventNotificationRx": prvtEfmOamStatisticsDuplicateEventNotificationRx,
       "prvtEfmOamStatisticsLoopbackControlTx": prvtEfmOamStatisticsLoopbackControlTx,
       "prvtEfmOamStatisticsLoopbackControlRx": prvtEfmOamStatisticsLoopbackControlRx,
       "prvtEfmOamStatisticsVariableRequestTx": prvtEfmOamStatisticsVariableRequestTx,
       "prvtEfmOamStatisticsVariableRequestRx": prvtEfmOamStatisticsVariableRequestRx,
       "prvtEfmOamStatisticsVariableResponseTx": prvtEfmOamStatisticsVariableResponseTx,
       "prvtEfmOamStatisticsVariableResponseRx": prvtEfmOamStatisticsVariableResponseRx,
       "prvtEfmOamStatisticsOrganizationSpecificTx": prvtEfmOamStatisticsOrganizationSpecificTx,
       "prvtEfmOamStatisticsOrganizationSpecificRx": prvtEfmOamStatisticsOrganizationSpecificRx,
       "prvtEfmOamStatisticsUnsupportedCodesTx": prvtEfmOamStatisticsUnsupportedCodesTx,
       "prvtEfmOamStatisticsUnsupportedCodesRx": prvtEfmOamStatisticsUnsupportedCodesRx,
       "prvtEfmOamStatisticsFramesLostDueToOam": prvtEfmOamStatisticsFramesLostDueToOam,
       "prvtEfmOamEventConfigTable": prvtEfmOamEventConfigTable,
       "prvtEfmOamEventConfigEntry": prvtEfmOamEventConfigEntry,
       "prvtEfmOamEventConfigErrorSymbolPeriodWindow": prvtEfmOamEventConfigErrorSymbolPeriodWindow,
       "prvtEfmOamEventConfigErrorSymbolPeriodThreshold": prvtEfmOamEventConfigErrorSymbolPeriodThreshold,
       "prvtEfmOamEventConfigErrorSymbolPeriodEventNotificationEnable": prvtEfmOamEventConfigErrorSymbolPeriodEventNotificationEnable,
       "prvtEfmOamEventConfigErrorFrameWindow": prvtEfmOamEventConfigErrorFrameWindow,
       "prvtEfmOamEventConfigErrorFrameThreshold": prvtEfmOamEventConfigErrorFrameThreshold,
       "prvtEfmOamEventConfigErrorFrameEventNotificationEnable": prvtEfmOamEventConfigErrorFrameEventNotificationEnable,
       "prvtEfmOamEventConfigDyingGaspEnable": prvtEfmOamEventConfigDyingGaspEnable,
       "prvtEfmOamEventLogTable": prvtEfmOamEventLogTable,
       "prvtEfmOamEventLogEntry": prvtEfmOamEventLogEntry,
       "prvtEfmOamEventLogId": prvtEfmOamEventLogId,
       "prvtEfmOamEventLogTimeStamp": prvtEfmOamEventLogTimeStamp,
       "prvtEfmOamEventLogOui": prvtEfmOamEventLogOui,
       "prvtEfmOamEventLogType": prvtEfmOamEventLogType,
       "prvtEfmOamEventLogLocation": prvtEfmOamEventLogLocation,
       "prvtEfmOamEventLogWindow": prvtEfmOamEventLogWindow,
       "prvtEfmOamEventLogThreshold": prvtEfmOamEventLogThreshold,
       "prvtEfmOamEventLogValue": prvtEfmOamEventLogValue,
       "prvtEfmOamEventLogRunningTotal": prvtEfmOamEventLogRunningTotal,
       "prvtEfmOamEventLogEventTotal": prvtEfmOamEventLogEventTotal,
       "prvtEfmOamInterfaceTable": prvtEfmOamInterfaceTable,
       "prvtEfmOamInterfaceEntry": prvtEfmOamInterfaceEntry,
       "prvtEfmOamInterfaceEnable": prvtEfmOamInterfaceEnable,
       "prvtEfmOamInterfaceOperStatus": prvtEfmOamInterfaceOperStatus,
       "prvtEfmOamInterfaceRole": prvtEfmOamInterfaceRole,
       "prvtEfmOamInterfaceMaxPduSize": prvtEfmOamInterfaceMaxPduSize,
       "prvtEfmOamInterfaceConfigRevision": prvtEfmOamInterfaceConfigRevision,
       "prvtEfmOamInterfaceFunctionsSupported": prvtEfmOamInterfaceFunctionsSupported,
       "prvtEfmOamInterfacePacketSent": prvtEfmOamInterfacePacketSent,
       "prvtEfmOamInterfacePacketReceived": prvtEfmOamInterfacePacketReceived,
       "prvtEfmOamInterfaceMode": prvtEfmOamInterfaceMode,
       "prvtEfmOamInterfaceLoopbackStatus": prvtEfmOamInterfaceLoopbackStatus,
       "prvtEfmOamInterfaceAcceptLoopbackCommands": prvtEfmOamInterfaceAcceptLoopbackCommands,
       "prvtEfmOamInterfaceEventReturnShutdown": prvtEfmOamInterfaceEventReturnShutdown,
       "prvtEfmOamEventForwardStatusTable": prvtEfmOamEventForwardStatusTable,
       "prvtEfmOamEventForwardStatusEntry": prvtEfmOamEventForwardStatusEntry,
       "prvtEfmOamEventForwardStatusIdx": prvtEfmOamEventForwardStatusIdx,
       "prvtEfmOamEventForwardStatusRowStatus": prvtEfmOamEventForwardStatusRowStatus,
       "prvtEfmOamEventForwardShutdownTable": prvtEfmOamEventForwardShutdownTable,
       "prvtEfmOamEventForwardShutdownEntry": prvtEfmOamEventForwardShutdownEntry,
       "prvtEfmOamEventForwardShutdownIdx": prvtEfmOamEventForwardShutdownIdx,
       "prvtEfmOamEventForwardShutdownRowStatus": prvtEfmOamEventForwardShutdownRowStatus}
)
