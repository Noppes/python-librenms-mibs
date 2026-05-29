# SNMP MIB module (AX-SHAPER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-SHAPER-MIB

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

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

axShaper = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    axShaper.setRevisions(
        ("2017-01-10 00:00",
         "2016-10-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxShaperUser_ObjectIdentity = ObjectIdentity
axShaperUser = _AxShaperUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1)
)
_AxShaperUserStatsTable_Object = MibTable
axShaperUserStatsTable = _AxShaperUserStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    axShaperUserStatsTable.setStatus("current")
_AxShaperUserStatsEntry_Object = MibTableRow
axShaperUserStatsEntry = _AxShaperUserStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1)
)
axShaperUserStatsEntry.setIndexNames(
    (0, "AX-SHAPER-MIB", "axShaperUserStatsNifIndex"),
    (0, "AX-SHAPER-MIB", "axShaperUserStatsPortIndex"),
    (0, "AX-SHAPER-MIB", "axShaperUserStatsUserId"),
)
if mibBuilder.loadTexts:
    axShaperUserStatsEntry.setStatus("current")
_AxShaperUserStatsNifIndex_Type = Integer32
_AxShaperUserStatsNifIndex_Object = MibTableColumn
axShaperUserStatsNifIndex = _AxShaperUserStatsNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 1),
    _AxShaperUserStatsNifIndex_Type()
)
axShaperUserStatsNifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axShaperUserStatsNifIndex.setStatus("current")
_AxShaperUserStatsPortIndex_Type = Integer32
_AxShaperUserStatsPortIndex_Object = MibTableColumn
axShaperUserStatsPortIndex = _AxShaperUserStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 2),
    _AxShaperUserStatsPortIndex_Type()
)
axShaperUserStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axShaperUserStatsPortIndex.setStatus("current")
_AxShaperUserStatsUserId_Type = Integer32
_AxShaperUserStatsUserId_Object = MibTableColumn
axShaperUserStatsUserId = _AxShaperUserStatsUserId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 3),
    _AxShaperUserStatsUserId_Type()
)
axShaperUserStatsUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axShaperUserStatsUserId.setStatus("current")
_AxShaperUserStatsShaperMode_Type = Integer32
_AxShaperUserStatsShaperMode_Object = MibTableColumn
axShaperUserStatsShaperMode = _AxShaperUserStatsShaperMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 4),
    _AxShaperUserStatsShaperMode_Type()
)
axShaperUserStatsShaperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsShaperMode.setStatus("current")
_AxShaperUserStatsSchedulingMode_Type = Integer32
_AxShaperUserStatsSchedulingMode_Object = MibTableColumn
axShaperUserStatsSchedulingMode = _AxShaperUserStatsSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 5),
    _AxShaperUserStatsSchedulingMode_Type()
)
axShaperUserStatsSchedulingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsSchedulingMode.setStatus("current")
_AxShaperUserStatsTotalSendPackets_Type = Counter64
_AxShaperUserStatsTotalSendPackets_Object = MibTableColumn
axShaperUserStatsTotalSendPackets = _AxShaperUserStatsTotalSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 6),
    _AxShaperUserStatsTotalSendPackets_Type()
)
axShaperUserStatsTotalSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsTotalSendPackets.setStatus("current")
_AxShaperUserStatsTotalDiscardPackets_Type = Counter64
_AxShaperUserStatsTotalDiscardPackets_Object = MibTableColumn
axShaperUserStatsTotalDiscardPackets = _AxShaperUserStatsTotalDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 7),
    _AxShaperUserStatsTotalDiscardPackets_Type()
)
axShaperUserStatsTotalDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsTotalDiscardPackets.setStatus("current")
_AxShaperUserStatsTotalSendBytes_Type = Counter64
_AxShaperUserStatsTotalSendBytes_Object = MibTableColumn
axShaperUserStatsTotalSendBytes = _AxShaperUserStatsTotalSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 8),
    _AxShaperUserStatsTotalSendBytes_Type()
)
axShaperUserStatsTotalSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsTotalSendBytes.setStatus("current")
_AxShaperUserStatsTotalDiscardBytes_Type = Counter64
_AxShaperUserStatsTotalDiscardBytes_Object = MibTableColumn
axShaperUserStatsTotalDiscardBytes = _AxShaperUserStatsTotalDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 9),
    _AxShaperUserStatsTotalDiscardBytes_Type()
)
axShaperUserStatsTotalDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsTotalDiscardBytes.setStatus("current")
_AxShaperUserStatsLlpqTotalSendPackets_Type = Counter64
_AxShaperUserStatsLlpqTotalSendPackets_Object = MibTableColumn
axShaperUserStatsLlpqTotalSendPackets = _AxShaperUserStatsLlpqTotalSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 10),
    _AxShaperUserStatsLlpqTotalSendPackets_Type()
)
axShaperUserStatsLlpqTotalSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsLlpqTotalSendPackets.setStatus("current")
_AxShaperUserStatsLlpqTotalDiscardPackets_Type = Counter64
_AxShaperUserStatsLlpqTotalDiscardPackets_Object = MibTableColumn
axShaperUserStatsLlpqTotalDiscardPackets = _AxShaperUserStatsLlpqTotalDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 11),
    _AxShaperUserStatsLlpqTotalDiscardPackets_Type()
)
axShaperUserStatsLlpqTotalDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsLlpqTotalDiscardPackets.setStatus("current")
_AxShaperUserStatsLlpqTotalSendBytes_Type = Counter64
_AxShaperUserStatsLlpqTotalSendBytes_Object = MibTableColumn
axShaperUserStatsLlpqTotalSendBytes = _AxShaperUserStatsLlpqTotalSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 12),
    _AxShaperUserStatsLlpqTotalSendBytes_Type()
)
axShaperUserStatsLlpqTotalSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsLlpqTotalSendBytes.setStatus("current")
_AxShaperUserStatsLlpqTotalDiscardBytes_Type = Counter64
_AxShaperUserStatsLlpqTotalDiscardBytes_Object = MibTableColumn
axShaperUserStatsLlpqTotalDiscardBytes = _AxShaperUserStatsLlpqTotalDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1, 1, 1, 13),
    _AxShaperUserStatsLlpqTotalDiscardBytes_Type()
)
axShaperUserStatsLlpqTotalDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserStatsLlpqTotalDiscardBytes.setStatus("current")
_AxShaperUserOutQueue_ObjectIdentity = ObjectIdentity
axShaperUserOutQueue = _AxShaperUserOutQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2)
)
_AxShaperUserOutQueueStatsTable_Object = MibTable
axShaperUserOutQueueStatsTable = _AxShaperUserOutQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsTable.setStatus("current")
_AxShaperUserOutQueueStatsEntry_Object = MibTableRow
axShaperUserOutQueueStatsEntry = _AxShaperUserOutQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1)
)
axShaperUserOutQueueStatsEntry.setIndexNames(
    (0, "AX-SHAPER-MIB", "axShaperUserOutQueueStatsNifIndex"),
    (0, "AX-SHAPER-MIB", "axShaperUserOutQueueStatsPortIndex"),
    (0, "AX-SHAPER-MIB", "axShaperUserOutQueueStatsUserId"),
    (0, "AX-SHAPER-MIB", "axShaperUserOutQueueStatsQueueNumber"),
)
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsEntry.setStatus("current")
_AxShaperUserOutQueueStatsNifIndex_Type = Integer32
_AxShaperUserOutQueueStatsNifIndex_Object = MibTableColumn
axShaperUserOutQueueStatsNifIndex = _AxShaperUserOutQueueStatsNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 1),
    _AxShaperUserOutQueueStatsNifIndex_Type()
)
axShaperUserOutQueueStatsNifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsNifIndex.setStatus("current")
_AxShaperUserOutQueueStatsPortIndex_Type = Integer32
_AxShaperUserOutQueueStatsPortIndex_Object = MibTableColumn
axShaperUserOutQueueStatsPortIndex = _AxShaperUserOutQueueStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 2),
    _AxShaperUserOutQueueStatsPortIndex_Type()
)
axShaperUserOutQueueStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsPortIndex.setStatus("current")
_AxShaperUserOutQueueStatsUserId_Type = Integer32
_AxShaperUserOutQueueStatsUserId_Object = MibTableColumn
axShaperUserOutQueueStatsUserId = _AxShaperUserOutQueueStatsUserId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 3),
    _AxShaperUserOutQueueStatsUserId_Type()
)
axShaperUserOutQueueStatsUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsUserId.setStatus("current")
_AxShaperUserOutQueueStatsQueueNumber_Type = Integer32
_AxShaperUserOutQueueStatsQueueNumber_Object = MibTableColumn
axShaperUserOutQueueStatsQueueNumber = _AxShaperUserOutQueueStatsQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 4),
    _AxShaperUserOutQueueStatsQueueNumber_Type()
)
axShaperUserOutQueueStatsQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsQueueNumber.setStatus("current")
_AxShaperUserOutQueueStatsQueueLen_Type = Integer32
_AxShaperUserOutQueueStatsQueueLen_Object = MibTableColumn
axShaperUserOutQueueStatsQueueLen = _AxShaperUserOutQueueStatsQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 5),
    _AxShaperUserOutQueueStatsQueueLen_Type()
)
axShaperUserOutQueueStatsQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsQueueLen.setStatus("current")
_AxShaperUserOutQueueStatsQueueLimitLen_Type = Integer32
_AxShaperUserOutQueueStatsQueueLimitLen_Object = MibTableColumn
axShaperUserOutQueueStatsQueueLimitLen = _AxShaperUserOutQueueStatsQueueLimitLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 6),
    _AxShaperUserOutQueueStatsQueueLimitLen_Type()
)
axShaperUserOutQueueStatsQueueLimitLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsQueueLimitLen.setStatus("current")
_AxShaperUserOutQueueStatsDiscard1SendPackets_Type = Counter64
_AxShaperUserOutQueueStatsDiscard1SendPackets_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard1SendPackets = _AxShaperUserOutQueueStatsDiscard1SendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 7),
    _AxShaperUserOutQueueStatsDiscard1SendPackets_Type()
)
axShaperUserOutQueueStatsDiscard1SendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard1SendPackets.setStatus("current")
_AxShaperUserOutQueueStatsDiscard1DiscardPackets_Type = Counter64
_AxShaperUserOutQueueStatsDiscard1DiscardPackets_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard1DiscardPackets = _AxShaperUserOutQueueStatsDiscard1DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 8),
    _AxShaperUserOutQueueStatsDiscard1DiscardPackets_Type()
)
axShaperUserOutQueueStatsDiscard1DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard1DiscardPackets.setStatus("current")
_AxShaperUserOutQueueStatsDiscard1SendBytes_Type = Counter64
_AxShaperUserOutQueueStatsDiscard1SendBytes_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard1SendBytes = _AxShaperUserOutQueueStatsDiscard1SendBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 9),
    _AxShaperUserOutQueueStatsDiscard1SendBytes_Type()
)
axShaperUserOutQueueStatsDiscard1SendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard1SendBytes.setStatus("current")
_AxShaperUserOutQueueStatsDiscard1DiscardBytes_Type = Counter64
_AxShaperUserOutQueueStatsDiscard1DiscardBytes_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard1DiscardBytes = _AxShaperUserOutQueueStatsDiscard1DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 10),
    _AxShaperUserOutQueueStatsDiscard1DiscardBytes_Type()
)
axShaperUserOutQueueStatsDiscard1DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard1DiscardBytes.setStatus("current")
_AxShaperUserOutQueueStatsDiscard2SendPackets_Type = Counter64
_AxShaperUserOutQueueStatsDiscard2SendPackets_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard2SendPackets = _AxShaperUserOutQueueStatsDiscard2SendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 11),
    _AxShaperUserOutQueueStatsDiscard2SendPackets_Type()
)
axShaperUserOutQueueStatsDiscard2SendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard2SendPackets.setStatus("current")
_AxShaperUserOutQueueStatsDiscard2DiscardPackets_Type = Counter64
_AxShaperUserOutQueueStatsDiscard2DiscardPackets_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard2DiscardPackets = _AxShaperUserOutQueueStatsDiscard2DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 12),
    _AxShaperUserOutQueueStatsDiscard2DiscardPackets_Type()
)
axShaperUserOutQueueStatsDiscard2DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard2DiscardPackets.setStatus("current")
_AxShaperUserOutQueueStatsDiscard2SendBytes_Type = Counter64
_AxShaperUserOutQueueStatsDiscard2SendBytes_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard2SendBytes = _AxShaperUserOutQueueStatsDiscard2SendBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 13),
    _AxShaperUserOutQueueStatsDiscard2SendBytes_Type()
)
axShaperUserOutQueueStatsDiscard2SendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard2SendBytes.setStatus("current")
_AxShaperUserOutQueueStatsDiscard2DiscardBytes_Type = Counter64
_AxShaperUserOutQueueStatsDiscard2DiscardBytes_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard2DiscardBytes = _AxShaperUserOutQueueStatsDiscard2DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 14),
    _AxShaperUserOutQueueStatsDiscard2DiscardBytes_Type()
)
axShaperUserOutQueueStatsDiscard2DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard2DiscardBytes.setStatus("current")
_AxShaperUserOutQueueStatsDiscard3SendPackets_Type = Counter64
_AxShaperUserOutQueueStatsDiscard3SendPackets_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard3SendPackets = _AxShaperUserOutQueueStatsDiscard3SendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 15),
    _AxShaperUserOutQueueStatsDiscard3SendPackets_Type()
)
axShaperUserOutQueueStatsDiscard3SendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard3SendPackets.setStatus("current")
_AxShaperUserOutQueueStatsDiscard3DiscardPackets_Type = Counter64
_AxShaperUserOutQueueStatsDiscard3DiscardPackets_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard3DiscardPackets = _AxShaperUserOutQueueStatsDiscard3DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 16),
    _AxShaperUserOutQueueStatsDiscard3DiscardPackets_Type()
)
axShaperUserOutQueueStatsDiscard3DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard3DiscardPackets.setStatus("current")
_AxShaperUserOutQueueStatsDiscard3SendBytes_Type = Counter64
_AxShaperUserOutQueueStatsDiscard3SendBytes_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard3SendBytes = _AxShaperUserOutQueueStatsDiscard3SendBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 17),
    _AxShaperUserOutQueueStatsDiscard3SendBytes_Type()
)
axShaperUserOutQueueStatsDiscard3SendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard3SendBytes.setStatus("current")
_AxShaperUserOutQueueStatsDiscard3DiscardBytes_Type = Counter64
_AxShaperUserOutQueueStatsDiscard3DiscardBytes_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard3DiscardBytes = _AxShaperUserOutQueueStatsDiscard3DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 18),
    _AxShaperUserOutQueueStatsDiscard3DiscardBytes_Type()
)
axShaperUserOutQueueStatsDiscard3DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard3DiscardBytes.setStatus("current")
_AxShaperUserOutQueueStatsDiscard4SendPackets_Type = Counter64
_AxShaperUserOutQueueStatsDiscard4SendPackets_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard4SendPackets = _AxShaperUserOutQueueStatsDiscard4SendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 19),
    _AxShaperUserOutQueueStatsDiscard4SendPackets_Type()
)
axShaperUserOutQueueStatsDiscard4SendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard4SendPackets.setStatus("current")
_AxShaperUserOutQueueStatsDiscard4DiscardPackets_Type = Counter64
_AxShaperUserOutQueueStatsDiscard4DiscardPackets_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard4DiscardPackets = _AxShaperUserOutQueueStatsDiscard4DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 20),
    _AxShaperUserOutQueueStatsDiscard4DiscardPackets_Type()
)
axShaperUserOutQueueStatsDiscard4DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard4DiscardPackets.setStatus("current")
_AxShaperUserOutQueueStatsDiscard4SendBytes_Type = Counter64
_AxShaperUserOutQueueStatsDiscard4SendBytes_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard4SendBytes = _AxShaperUserOutQueueStatsDiscard4SendBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 21),
    _AxShaperUserOutQueueStatsDiscard4SendBytes_Type()
)
axShaperUserOutQueueStatsDiscard4SendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard4SendBytes.setStatus("current")
_AxShaperUserOutQueueStatsDiscard4DiscardBytes_Type = Counter64
_AxShaperUserOutQueueStatsDiscard4DiscardBytes_Object = MibTableColumn
axShaperUserOutQueueStatsDiscard4DiscardBytes = _AxShaperUserOutQueueStatsDiscard4DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 22),
    _AxShaperUserOutQueueStatsDiscard4DiscardBytes_Type()
)
axShaperUserOutQueueStatsDiscard4DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsDiscard4DiscardBytes.setStatus("current")
_AxShaperUserOutQueueStatsTotalSendPackets_Type = Counter64
_AxShaperUserOutQueueStatsTotalSendPackets_Object = MibTableColumn
axShaperUserOutQueueStatsTotalSendPackets = _AxShaperUserOutQueueStatsTotalSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 23),
    _AxShaperUserOutQueueStatsTotalSendPackets_Type()
)
axShaperUserOutQueueStatsTotalSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsTotalSendPackets.setStatus("current")
_AxShaperUserOutQueueStatsTotalDiscardPackets_Type = Counter64
_AxShaperUserOutQueueStatsTotalDiscardPackets_Object = MibTableColumn
axShaperUserOutQueueStatsTotalDiscardPackets = _AxShaperUserOutQueueStatsTotalDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 24),
    _AxShaperUserOutQueueStatsTotalDiscardPackets_Type()
)
axShaperUserOutQueueStatsTotalDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsTotalDiscardPackets.setStatus("current")
_AxShaperUserOutQueueStatsTotalSendBytes_Type = Counter64
_AxShaperUserOutQueueStatsTotalSendBytes_Object = MibTableColumn
axShaperUserOutQueueStatsTotalSendBytes = _AxShaperUserOutQueueStatsTotalSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 25),
    _AxShaperUserOutQueueStatsTotalSendBytes_Type()
)
axShaperUserOutQueueStatsTotalSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsTotalSendBytes.setStatus("current")
_AxShaperUserOutQueueStatsTotalDiscardBytes_Type = Counter64
_AxShaperUserOutQueueStatsTotalDiscardBytes_Object = MibTableColumn
axShaperUserOutQueueStatsTotalDiscardBytes = _AxShaperUserOutQueueStatsTotalDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 2, 1, 1, 26),
    _AxShaperUserOutQueueStatsTotalDiscardBytes_Type()
)
axShaperUserOutQueueStatsTotalDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperUserOutQueueStatsTotalDiscardBytes.setStatus("current")
_AxShaperPort_ObjectIdentity = ObjectIdentity
axShaperPort = _AxShaperPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3)
)
_AxShaperPortStatsTable_Object = MibTable
axShaperPortStatsTable = _AxShaperPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    axShaperPortStatsTable.setStatus("current")
_AxShaperPortStatsEntry_Object = MibTableRow
axShaperPortStatsEntry = _AxShaperPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1, 1)
)
axShaperPortStatsEntry.setIndexNames(
    (0, "AX-SHAPER-MIB", "axShaperPortStatsNifIndex"),
    (0, "AX-SHAPER-MIB", "axShaperPortStatsPortIndex"),
)
if mibBuilder.loadTexts:
    axShaperPortStatsEntry.setStatus("current")
_AxShaperPortStatsNifIndex_Type = Integer32
_AxShaperPortStatsNifIndex_Object = MibTableColumn
axShaperPortStatsNifIndex = _AxShaperPortStatsNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1, 1, 1),
    _AxShaperPortStatsNifIndex_Type()
)
axShaperPortStatsNifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axShaperPortStatsNifIndex.setStatus("current")
_AxShaperPortStatsPortIndex_Type = Integer32
_AxShaperPortStatsPortIndex_Object = MibTableColumn
axShaperPortStatsPortIndex = _AxShaperPortStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1, 1, 2),
    _AxShaperPortStatsPortIndex_Type()
)
axShaperPortStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axShaperPortStatsPortIndex.setStatus("current")
_AxShaperPortStatsShaperMode_Type = Integer32
_AxShaperPortStatsShaperMode_Object = MibTableColumn
axShaperPortStatsShaperMode = _AxShaperPortStatsShaperMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1, 1, 3),
    _AxShaperPortStatsShaperMode_Type()
)
axShaperPortStatsShaperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperPortStatsShaperMode.setStatus("current")
_AxShaperPortStatsSchedulingMode_Type = Integer32
_AxShaperPortStatsSchedulingMode_Object = MibTableColumn
axShaperPortStatsSchedulingMode = _AxShaperPortStatsSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1, 1, 4),
    _AxShaperPortStatsSchedulingMode_Type()
)
axShaperPortStatsSchedulingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperPortStatsSchedulingMode.setStatus("current")
_AxShaperPortStatsTotalSendPackets_Type = Counter64
_AxShaperPortStatsTotalSendPackets_Object = MibTableColumn
axShaperPortStatsTotalSendPackets = _AxShaperPortStatsTotalSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1, 1, 5),
    _AxShaperPortStatsTotalSendPackets_Type()
)
axShaperPortStatsTotalSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperPortStatsTotalSendPackets.setStatus("current")
_AxShaperPortStatsTotalDiscardPackets_Type = Counter64
_AxShaperPortStatsTotalDiscardPackets_Object = MibTableColumn
axShaperPortStatsTotalDiscardPackets = _AxShaperPortStatsTotalDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1, 1, 6),
    _AxShaperPortStatsTotalDiscardPackets_Type()
)
axShaperPortStatsTotalDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperPortStatsTotalDiscardPackets.setStatus("current")
_AxShaperPortStatsTotalSendBytes_Type = Counter64
_AxShaperPortStatsTotalSendBytes_Object = MibTableColumn
axShaperPortStatsTotalSendBytes = _AxShaperPortStatsTotalSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1, 1, 7),
    _AxShaperPortStatsTotalSendBytes_Type()
)
axShaperPortStatsTotalSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperPortStatsTotalSendBytes.setStatus("current")
_AxShaperPortStatsTotalDiscardBytes_Type = Counter64
_AxShaperPortStatsTotalDiscardBytes_Object = MibTableColumn
axShaperPortStatsTotalDiscardBytes = _AxShaperPortStatsTotalDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 3, 1, 1, 8),
    _AxShaperPortStatsTotalDiscardBytes_Type()
)
axShaperPortStatsTotalDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axShaperPortStatsTotalDiscardBytes.setStatus("current")
_AxShaperConformance_ObjectIdentity = ObjectIdentity
axShaperConformance = _AxShaperConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1000)
)
_AxShaperCompliances_ObjectIdentity = ObjectIdentity
axShaperCompliances = _AxShaperCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1000, 1)
)
_AxShaperGroups_ObjectIdentity = ObjectIdentity
axShaperGroups = _AxShaperGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1000, 2)
)

# Managed Objects groups

axShaperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1000, 2, 1)
)
axShaperGroup.setObjects(
      *(("AX-SHAPER-MIB", "axShaperUserStatsShaperMode"),
        ("AX-SHAPER-MIB", "axShaperUserStatsSchedulingMode"),
        ("AX-SHAPER-MIB", "axShaperUserStatsTotalSendPackets"),
        ("AX-SHAPER-MIB", "axShaperUserStatsTotalDiscardPackets"),
        ("AX-SHAPER-MIB", "axShaperUserStatsTotalSendBytes"),
        ("AX-SHAPER-MIB", "axShaperUserStatsTotalDiscardBytes"),
        ("AX-SHAPER-MIB", "axShaperUserStatsLlpqTotalSendPackets"),
        ("AX-SHAPER-MIB", "axShaperUserStatsLlpqTotalDiscardPackets"),
        ("AX-SHAPER-MIB", "axShaperUserStatsLlpqTotalSendBytes"),
        ("AX-SHAPER-MIB", "axShaperUserStatsLlpqTotalDiscardBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsQueueLen"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsQueueLimitLen"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard1SendPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard1DiscardPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard1SendBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard1DiscardBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard2SendPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard2DiscardPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard2SendBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard2DiscardBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard3SendPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard3DiscardPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard3SendBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard3DiscardBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard4SendPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard4DiscardPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard4SendBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsDiscard4DiscardBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsTotalSendPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsTotalDiscardPackets"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsTotalSendBytes"),
        ("AX-SHAPER-MIB", "axShaperUserOutQueueStatsTotalDiscardBytes"),
        ("AX-SHAPER-MIB", "axShaperPortStatsShaperMode"),
        ("AX-SHAPER-MIB", "axShaperPortStatsSchedulingMode"),
        ("AX-SHAPER-MIB", "axShaperPortStatsTotalSendPackets"),
        ("AX-SHAPER-MIB", "axShaperPortStatsTotalDiscardPackets"),
        ("AX-SHAPER-MIB", "axShaperPortStatsTotalSendBytes"),
        ("AX-SHAPER-MIB", "axShaperPortStatsTotalDiscardBytes"))
)
if mibBuilder.loadTexts:
    axShaperGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axShaperCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 13, 1000, 1, 1)
)
axShaperCompliance.setObjects(
    ("AX-SHAPER-MIB", "axShaperGroup")
)
if mibBuilder.loadTexts:
    axShaperCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-SHAPER-MIB",
    **{"axShaper": axShaper,
       "axShaperUser": axShaperUser,
       "axShaperUserStatsTable": axShaperUserStatsTable,
       "axShaperUserStatsEntry": axShaperUserStatsEntry,
       "axShaperUserStatsNifIndex": axShaperUserStatsNifIndex,
       "axShaperUserStatsPortIndex": axShaperUserStatsPortIndex,
       "axShaperUserStatsUserId": axShaperUserStatsUserId,
       "axShaperUserStatsShaperMode": axShaperUserStatsShaperMode,
       "axShaperUserStatsSchedulingMode": axShaperUserStatsSchedulingMode,
       "axShaperUserStatsTotalSendPackets": axShaperUserStatsTotalSendPackets,
       "axShaperUserStatsTotalDiscardPackets": axShaperUserStatsTotalDiscardPackets,
       "axShaperUserStatsTotalSendBytes": axShaperUserStatsTotalSendBytes,
       "axShaperUserStatsTotalDiscardBytes": axShaperUserStatsTotalDiscardBytes,
       "axShaperUserStatsLlpqTotalSendPackets": axShaperUserStatsLlpqTotalSendPackets,
       "axShaperUserStatsLlpqTotalDiscardPackets": axShaperUserStatsLlpqTotalDiscardPackets,
       "axShaperUserStatsLlpqTotalSendBytes": axShaperUserStatsLlpqTotalSendBytes,
       "axShaperUserStatsLlpqTotalDiscardBytes": axShaperUserStatsLlpqTotalDiscardBytes,
       "axShaperUserOutQueue": axShaperUserOutQueue,
       "axShaperUserOutQueueStatsTable": axShaperUserOutQueueStatsTable,
       "axShaperUserOutQueueStatsEntry": axShaperUserOutQueueStatsEntry,
       "axShaperUserOutQueueStatsNifIndex": axShaperUserOutQueueStatsNifIndex,
       "axShaperUserOutQueueStatsPortIndex": axShaperUserOutQueueStatsPortIndex,
       "axShaperUserOutQueueStatsUserId": axShaperUserOutQueueStatsUserId,
       "axShaperUserOutQueueStatsQueueNumber": axShaperUserOutQueueStatsQueueNumber,
       "axShaperUserOutQueueStatsQueueLen": axShaperUserOutQueueStatsQueueLen,
       "axShaperUserOutQueueStatsQueueLimitLen": axShaperUserOutQueueStatsQueueLimitLen,
       "axShaperUserOutQueueStatsDiscard1SendPackets": axShaperUserOutQueueStatsDiscard1SendPackets,
       "axShaperUserOutQueueStatsDiscard1DiscardPackets": axShaperUserOutQueueStatsDiscard1DiscardPackets,
       "axShaperUserOutQueueStatsDiscard1SendBytes": axShaperUserOutQueueStatsDiscard1SendBytes,
       "axShaperUserOutQueueStatsDiscard1DiscardBytes": axShaperUserOutQueueStatsDiscard1DiscardBytes,
       "axShaperUserOutQueueStatsDiscard2SendPackets": axShaperUserOutQueueStatsDiscard2SendPackets,
       "axShaperUserOutQueueStatsDiscard2DiscardPackets": axShaperUserOutQueueStatsDiscard2DiscardPackets,
       "axShaperUserOutQueueStatsDiscard2SendBytes": axShaperUserOutQueueStatsDiscard2SendBytes,
       "axShaperUserOutQueueStatsDiscard2DiscardBytes": axShaperUserOutQueueStatsDiscard2DiscardBytes,
       "axShaperUserOutQueueStatsDiscard3SendPackets": axShaperUserOutQueueStatsDiscard3SendPackets,
       "axShaperUserOutQueueStatsDiscard3DiscardPackets": axShaperUserOutQueueStatsDiscard3DiscardPackets,
       "axShaperUserOutQueueStatsDiscard3SendBytes": axShaperUserOutQueueStatsDiscard3SendBytes,
       "axShaperUserOutQueueStatsDiscard3DiscardBytes": axShaperUserOutQueueStatsDiscard3DiscardBytes,
       "axShaperUserOutQueueStatsDiscard4SendPackets": axShaperUserOutQueueStatsDiscard4SendPackets,
       "axShaperUserOutQueueStatsDiscard4DiscardPackets": axShaperUserOutQueueStatsDiscard4DiscardPackets,
       "axShaperUserOutQueueStatsDiscard4SendBytes": axShaperUserOutQueueStatsDiscard4SendBytes,
       "axShaperUserOutQueueStatsDiscard4DiscardBytes": axShaperUserOutQueueStatsDiscard4DiscardBytes,
       "axShaperUserOutQueueStatsTotalSendPackets": axShaperUserOutQueueStatsTotalSendPackets,
       "axShaperUserOutQueueStatsTotalDiscardPackets": axShaperUserOutQueueStatsTotalDiscardPackets,
       "axShaperUserOutQueueStatsTotalSendBytes": axShaperUserOutQueueStatsTotalSendBytes,
       "axShaperUserOutQueueStatsTotalDiscardBytes": axShaperUserOutQueueStatsTotalDiscardBytes,
       "axShaperPort": axShaperPort,
       "axShaperPortStatsTable": axShaperPortStatsTable,
       "axShaperPortStatsEntry": axShaperPortStatsEntry,
       "axShaperPortStatsNifIndex": axShaperPortStatsNifIndex,
       "axShaperPortStatsPortIndex": axShaperPortStatsPortIndex,
       "axShaperPortStatsShaperMode": axShaperPortStatsShaperMode,
       "axShaperPortStatsSchedulingMode": axShaperPortStatsSchedulingMode,
       "axShaperPortStatsTotalSendPackets": axShaperPortStatsTotalSendPackets,
       "axShaperPortStatsTotalDiscardPackets": axShaperPortStatsTotalDiscardPackets,
       "axShaperPortStatsTotalSendBytes": axShaperPortStatsTotalSendBytes,
       "axShaperPortStatsTotalDiscardBytes": axShaperPortStatsTotalDiscardBytes,
       "axShaperConformance": axShaperConformance,
       "axShaperCompliances": axShaperCompliances,
       "axShaperCompliance": axShaperCompliance,
       "axShaperGroups": axShaperGroups,
       "axShaperGroup": axShaperGroup}
)
