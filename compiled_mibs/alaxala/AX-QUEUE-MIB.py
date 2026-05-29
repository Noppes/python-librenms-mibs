# SNMP MIB module (AX-QUEUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-QUEUE-MIB

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

axQueue = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46)
)
if mibBuilder.loadTexts:
    axQueue.setRevisions(
        ("2013-10-03 00:00",
         "2013-06-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxPortQueue_ObjectIdentity = ObjectIdentity
axPortQueue = _AxPortQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71)
)
_AxPortOutQueue_ObjectIdentity = ObjectIdentity
axPortOutQueue = _AxPortOutQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21)
)
_AxPortOutQueueStatusTable_Object = MibTable
axPortOutQueueStatusTable = _AxPortOutQueueStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 11)
)
if mibBuilder.loadTexts:
    axPortOutQueueStatusTable.setStatus("current")
_AxPortOutQueueStatusEntry_Object = MibTableRow
axPortOutQueueStatusEntry = _AxPortOutQueueStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 11, 1)
)
axPortOutQueueStatusEntry.setIndexNames(
    (0, "AX-QUEUE-MIB", "axPortOutQueueStatusIfIndex"),
)
if mibBuilder.loadTexts:
    axPortOutQueueStatusEntry.setStatus("current")


class _AxPortOutQueueStatusIfIndex_Type(Integer32):
    """Custom type axPortOutQueueStatusIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxPortOutQueueStatusIfIndex_Type.__name__ = "Integer32"
_AxPortOutQueueStatusIfIndex_Object = MibTableColumn
axPortOutQueueStatusIfIndex = _AxPortOutQueueStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 11, 1, 1),
    _AxPortOutQueueStatusIfIndex_Type()
)
axPortOutQueueStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPortOutQueueStatusIfIndex.setStatus("current")


class _AxPortOutQueueStatusMaxQueue_Type(Integer32):
    """Custom type axPortOutQueueStatusMaxQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_AxPortOutQueueStatusMaxQueue_Type.__name__ = "Integer32"
_AxPortOutQueueStatusMaxQueue_Object = MibTableColumn
axPortOutQueueStatusMaxQueue = _AxPortOutQueueStatusMaxQueue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 11, 1, 11),
    _AxPortOutQueueStatusMaxQueue_Type()
)
axPortOutQueueStatusMaxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatusMaxQueue.setStatus("current")
_AxPortOutQueueStatusQTable_Object = MibTable
axPortOutQueueStatusQTable = _AxPortOutQueueStatusQTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 51)
)
if mibBuilder.loadTexts:
    axPortOutQueueStatusQTable.setStatus("current")
_AxPortOutQueueStatusQEntry_Object = MibTableRow
axPortOutQueueStatusQEntry = _AxPortOutQueueStatusQEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 51, 1)
)
axPortOutQueueStatusQEntry.setIndexNames(
    (0, "AX-QUEUE-MIB", "axPortOutQueueStatusQIfIndex"),
    (0, "AX-QUEUE-MIB", "axPortOutQueueStatusQQueIndex"),
)
if mibBuilder.loadTexts:
    axPortOutQueueStatusQEntry.setStatus("current")


class _AxPortOutQueueStatusQIfIndex_Type(Integer32):
    """Custom type axPortOutQueueStatusQIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxPortOutQueueStatusQIfIndex_Type.__name__ = "Integer32"
_AxPortOutQueueStatusQIfIndex_Object = MibTableColumn
axPortOutQueueStatusQIfIndex = _AxPortOutQueueStatusQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 51, 1, 1),
    _AxPortOutQueueStatusQIfIndex_Type()
)
axPortOutQueueStatusQIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPortOutQueueStatusQIfIndex.setStatus("current")


class _AxPortOutQueueStatusQQueIndex_Type(Integer32):
    """Custom type axPortOutQueueStatusQQueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AxPortOutQueueStatusQQueIndex_Type.__name__ = "Integer32"
_AxPortOutQueueStatusQQueIndex_Object = MibTableColumn
axPortOutQueueStatusQQueIndex = _AxPortOutQueueStatusQQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 51, 1, 2),
    _AxPortOutQueueStatusQQueIndex_Type()
)
axPortOutQueueStatusQQueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPortOutQueueStatusQQueIndex.setStatus("current")
_AxPortOutQueueStatusQQlen_Type = Integer32
_AxPortOutQueueStatusQQlen_Object = MibTableColumn
axPortOutQueueStatusQQlen = _AxPortOutQueueStatusQQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 51, 1, 11),
    _AxPortOutQueueStatusQQlen_Type()
)
axPortOutQueueStatusQQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatusQQlen.setStatus("current")
_AxPortOutQueueStatusQPeakQlen_Type = Integer32
_AxPortOutQueueStatusQPeakQlen_Object = MibTableColumn
axPortOutQueueStatusQPeakQlen = _AxPortOutQueueStatusQPeakQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 51, 1, 12),
    _AxPortOutQueueStatusQPeakQlen_Type()
)
axPortOutQueueStatusQPeakQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatusQPeakQlen.setStatus("current")
_AxPortOutQueueStatusQLimitQlen_Type = Integer32
_AxPortOutQueueStatusQLimitQlen_Object = MibTableColumn
axPortOutQueueStatusQLimitQlen = _AxPortOutQueueStatusQLimitQlen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 51, 1, 13),
    _AxPortOutQueueStatusQLimitQlen_Type()
)
axPortOutQueueStatusQLimitQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatusQLimitQlen.setStatus("current")
_AxPortOutQueueStatsQTable_Object = MibTable
axPortOutQueueStatsQTable = _AxPortOutQueueStatsQTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61)
)
if mibBuilder.loadTexts:
    axPortOutQueueStatsQTable.setStatus("current")
_AxPortOutQueueStatsQEntry_Object = MibTableRow
axPortOutQueueStatsQEntry = _AxPortOutQueueStatsQEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1)
)
axPortOutQueueStatsQEntry.setIndexNames(
    (0, "AX-QUEUE-MIB", "axPortOutQueueStatsQIfIndex"),
    (0, "AX-QUEUE-MIB", "axPortOutQueueStatsQQueIndex"),
)
if mibBuilder.loadTexts:
    axPortOutQueueStatsQEntry.setStatus("current")


class _AxPortOutQueueStatsQIfIndex_Type(Integer32):
    """Custom type axPortOutQueueStatsQIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxPortOutQueueStatsQIfIndex_Type.__name__ = "Integer32"
_AxPortOutQueueStatsQIfIndex_Object = MibTableColumn
axPortOutQueueStatsQIfIndex = _AxPortOutQueueStatsQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 1),
    _AxPortOutQueueStatsQIfIndex_Type()
)
axPortOutQueueStatsQIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQIfIndex.setStatus("current")


class _AxPortOutQueueStatsQQueIndex_Type(Integer32):
    """Custom type axPortOutQueueStatsQQueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AxPortOutQueueStatsQQueIndex_Type.__name__ = "Integer32"
_AxPortOutQueueStatsQQueIndex_Object = MibTableColumn
axPortOutQueueStatsQQueIndex = _AxPortOutQueueStatsQQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 2),
    _AxPortOutQueueStatsQQueIndex_Type()
)
axPortOutQueueStatsQQueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQQueIndex.setStatus("current")
_AxPortOutQueueStatsQDiscard1SendPackets_Type = Counter64
_AxPortOutQueueStatsQDiscard1SendPackets_Object = MibTableColumn
axPortOutQueueStatsQDiscard1SendPackets = _AxPortOutQueueStatsQDiscard1SendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 11),
    _AxPortOutQueueStatsQDiscard1SendPackets_Type()
)
axPortOutQueueStatsQDiscard1SendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQDiscard1SendPackets.setStatus("current")
_AxPortOutQueueStatsQDiscard1DiscardPackets_Type = Counter64
_AxPortOutQueueStatsQDiscard1DiscardPackets_Object = MibTableColumn
axPortOutQueueStatsQDiscard1DiscardPackets = _AxPortOutQueueStatsQDiscard1DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 12),
    _AxPortOutQueueStatsQDiscard1DiscardPackets_Type()
)
axPortOutQueueStatsQDiscard1DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQDiscard1DiscardPackets.setStatus("current")
_AxPortOutQueueStatsQDiscard2SendPackets_Type = Counter64
_AxPortOutQueueStatsQDiscard2SendPackets_Object = MibTableColumn
axPortOutQueueStatsQDiscard2SendPackets = _AxPortOutQueueStatsQDiscard2SendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 21),
    _AxPortOutQueueStatsQDiscard2SendPackets_Type()
)
axPortOutQueueStatsQDiscard2SendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQDiscard2SendPackets.setStatus("current")
_AxPortOutQueueStatsQDiscard2DiscardPackets_Type = Counter64
_AxPortOutQueueStatsQDiscard2DiscardPackets_Object = MibTableColumn
axPortOutQueueStatsQDiscard2DiscardPackets = _AxPortOutQueueStatsQDiscard2DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 22),
    _AxPortOutQueueStatsQDiscard2DiscardPackets_Type()
)
axPortOutQueueStatsQDiscard2DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQDiscard2DiscardPackets.setStatus("current")
_AxPortOutQueueStatsQDiscard3SendPackets_Type = Counter64
_AxPortOutQueueStatsQDiscard3SendPackets_Object = MibTableColumn
axPortOutQueueStatsQDiscard3SendPackets = _AxPortOutQueueStatsQDiscard3SendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 31),
    _AxPortOutQueueStatsQDiscard3SendPackets_Type()
)
axPortOutQueueStatsQDiscard3SendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQDiscard3SendPackets.setStatus("current")
_AxPortOutQueueStatsQDiscard3DiscardPackets_Type = Counter64
_AxPortOutQueueStatsQDiscard3DiscardPackets_Object = MibTableColumn
axPortOutQueueStatsQDiscard3DiscardPackets = _AxPortOutQueueStatsQDiscard3DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 32),
    _AxPortOutQueueStatsQDiscard3DiscardPackets_Type()
)
axPortOutQueueStatsQDiscard3DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQDiscard3DiscardPackets.setStatus("current")
_AxPortOutQueueStatsQDiscard4SendPackets_Type = Counter64
_AxPortOutQueueStatsQDiscard4SendPackets_Object = MibTableColumn
axPortOutQueueStatsQDiscard4SendPackets = _AxPortOutQueueStatsQDiscard4SendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 41),
    _AxPortOutQueueStatsQDiscard4SendPackets_Type()
)
axPortOutQueueStatsQDiscard4SendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQDiscard4SendPackets.setStatus("current")
_AxPortOutQueueStatsQDiscard4DiscardPackets_Type = Counter64
_AxPortOutQueueStatsQDiscard4DiscardPackets_Object = MibTableColumn
axPortOutQueueStatsQDiscard4DiscardPackets = _AxPortOutQueueStatsQDiscard4DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 42),
    _AxPortOutQueueStatsQDiscard4DiscardPackets_Type()
)
axPortOutQueueStatsQDiscard4DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQDiscard4DiscardPackets.setStatus("current")
_AxPortOutQueueStatsQTotalSendPackets_Type = Counter64
_AxPortOutQueueStatsQTotalSendPackets_Object = MibTableColumn
axPortOutQueueStatsQTotalSendPackets = _AxPortOutQueueStatsQTotalSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 101),
    _AxPortOutQueueStatsQTotalSendPackets_Type()
)
axPortOutQueueStatsQTotalSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQTotalSendPackets.setStatus("current")
_AxPortOutQueueStatsQTotalDiscardPackets_Type = Counter64
_AxPortOutQueueStatsQTotalDiscardPackets_Object = MibTableColumn
axPortOutQueueStatsQTotalDiscardPackets = _AxPortOutQueueStatsQTotalDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 102),
    _AxPortOutQueueStatsQTotalDiscardPackets_Type()
)
axPortOutQueueStatsQTotalDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQTotalDiscardPackets.setStatus("current")
_AxPortOutQueueStatsQTotalSendBytes_Type = Counter64
_AxPortOutQueueStatsQTotalSendBytes_Object = MibTableColumn
axPortOutQueueStatsQTotalSendBytes = _AxPortOutQueueStatsQTotalSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 71, 21, 61, 1, 103),
    _AxPortOutQueueStatsQTotalSendBytes_Type()
)
axPortOutQueueStatsQTotalSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPortOutQueueStatsQTotalSendBytes.setStatus("current")
_AxQueueConformance_ObjectIdentity = ObjectIdentity
axQueueConformance = _AxQueueConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 1000)
)
_AxQueueCompliances_ObjectIdentity = ObjectIdentity
axQueueCompliances = _AxQueueCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 1000, 1)
)
_AxQueueGroups_ObjectIdentity = ObjectIdentity
axQueueGroups = _AxQueueGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 1000, 2)
)

# Managed Objects groups

axQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 1000, 2, 1)
)
axQueueGroup.setObjects(
      *(("AX-QUEUE-MIB", "axPortOutQueueStatusMaxQueue"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatusQQlen"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatusQPeakQlen"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatusQLimitQlen"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQDiscard1SendPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQDiscard1DiscardPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQDiscard2SendPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQDiscard2DiscardPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQDiscard3SendPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQDiscard3DiscardPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQDiscard4SendPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQDiscard4DiscardPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQTotalSendPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQTotalDiscardPackets"),
        ("AX-QUEUE-MIB", "axPortOutQueueStatsQTotalSendBytes"))
)
if mibBuilder.loadTexts:
    axQueueGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axQueueCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 46, 1000, 1, 1)
)
axQueueCompliance.setObjects(
    ("AX-QUEUE-MIB", "axQueueGroup")
)
if mibBuilder.loadTexts:
    axQueueCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-QUEUE-MIB",
    **{"axQueue": axQueue,
       "axPortQueue": axPortQueue,
       "axPortOutQueue": axPortOutQueue,
       "axPortOutQueueStatusTable": axPortOutQueueStatusTable,
       "axPortOutQueueStatusEntry": axPortOutQueueStatusEntry,
       "axPortOutQueueStatusIfIndex": axPortOutQueueStatusIfIndex,
       "axPortOutQueueStatusMaxQueue": axPortOutQueueStatusMaxQueue,
       "axPortOutQueueStatusQTable": axPortOutQueueStatusQTable,
       "axPortOutQueueStatusQEntry": axPortOutQueueStatusQEntry,
       "axPortOutQueueStatusQIfIndex": axPortOutQueueStatusQIfIndex,
       "axPortOutQueueStatusQQueIndex": axPortOutQueueStatusQQueIndex,
       "axPortOutQueueStatusQQlen": axPortOutQueueStatusQQlen,
       "axPortOutQueueStatusQPeakQlen": axPortOutQueueStatusQPeakQlen,
       "axPortOutQueueStatusQLimitQlen": axPortOutQueueStatusQLimitQlen,
       "axPortOutQueueStatsQTable": axPortOutQueueStatsQTable,
       "axPortOutQueueStatsQEntry": axPortOutQueueStatsQEntry,
       "axPortOutQueueStatsQIfIndex": axPortOutQueueStatsQIfIndex,
       "axPortOutQueueStatsQQueIndex": axPortOutQueueStatsQQueIndex,
       "axPortOutQueueStatsQDiscard1SendPackets": axPortOutQueueStatsQDiscard1SendPackets,
       "axPortOutQueueStatsQDiscard1DiscardPackets": axPortOutQueueStatsQDiscard1DiscardPackets,
       "axPortOutQueueStatsQDiscard2SendPackets": axPortOutQueueStatsQDiscard2SendPackets,
       "axPortOutQueueStatsQDiscard2DiscardPackets": axPortOutQueueStatsQDiscard2DiscardPackets,
       "axPortOutQueueStatsQDiscard3SendPackets": axPortOutQueueStatsQDiscard3SendPackets,
       "axPortOutQueueStatsQDiscard3DiscardPackets": axPortOutQueueStatsQDiscard3DiscardPackets,
       "axPortOutQueueStatsQDiscard4SendPackets": axPortOutQueueStatsQDiscard4SendPackets,
       "axPortOutQueueStatsQDiscard4DiscardPackets": axPortOutQueueStatsQDiscard4DiscardPackets,
       "axPortOutQueueStatsQTotalSendPackets": axPortOutQueueStatsQTotalSendPackets,
       "axPortOutQueueStatsQTotalDiscardPackets": axPortOutQueueStatsQTotalDiscardPackets,
       "axPortOutQueueStatsQTotalSendBytes": axPortOutQueueStatsQTotalSendBytes,
       "axQueueConformance": axQueueConformance,
       "axQueueCompliances": axQueueCompliances,
       "axQueueCompliance": axQueueCompliance,
       "axQueueGroups": axQueueGroups,
       "axQueueGroup": axQueueGroup}
)
