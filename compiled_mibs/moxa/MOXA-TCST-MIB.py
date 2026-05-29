# SNMP MIB module (MOXA-TCST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-TCST-MIB

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

(layer2Diagnosic,) = mibBuilder.importSymbols(
    "MOXA-SWITCHING-MIB",
    "layer2Diagnosic")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mxTcst = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4)
)
if mibBuilder.loadTexts:
    mxTcst.setRevisions(
        ("2022-02-17 00:00",
         "2019-06-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TcstConfiguration_ObjectIdentity = ObjectIdentity
tcstConfiguration = _TcstConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 1)
)
_TcstConfigClearAllStatistics_Type = TruthValue
_TcstConfigClearAllStatistics_Object = MibScalar
tcstConfigClearAllStatistics = _TcstConfigClearAllStatistics_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 1, 1),
    _TcstConfigClearAllStatistics_Type()
)
tcstConfigClearAllStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcstConfigClearAllStatistics.setStatus("current")
_TcstConfigClearPortStatisticsTable_Object = MibTable
tcstConfigClearPortStatisticsTable = _TcstConfigClearPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    tcstConfigClearPortStatisticsTable.setStatus("current")
_TcstConfigClearPortStatisticsEntry_Object = MibTableRow
tcstConfigClearPortStatisticsEntry = _TcstConfigClearPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 1, 2, 1)
)
tcstConfigClearPortStatisticsEntry.setIndexNames(
    (0, "MOXA-TCST-MIB", "tcstConfigIfIndex"),
)
if mibBuilder.loadTexts:
    tcstConfigClearPortStatisticsEntry.setStatus("current")
_TcstConfigIfIndex_Type = Integer32
_TcstConfigIfIndex_Object = MibTableColumn
tcstConfigIfIndex = _TcstConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 1, 2, 1, 1),
    _TcstConfigIfIndex_Type()
)
tcstConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcstConfigIfIndex.setStatus("current")
_TcstConfigClearPortStatistics_Type = Integer32
_TcstConfigClearPortStatistics_Object = MibTableColumn
tcstConfigClearPortStatistics = _TcstConfigClearPortStatistics_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 1, 2, 1, 2),
    _TcstConfigClearPortStatistics_Type()
)
tcstConfigClearPortStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcstConfigClearPortStatistics.setStatus("current")
_TcstStatus_ObjectIdentity = ObjectIdentity
tcstStatus = _TcstStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2)
)
_TcstStatGroupTable_Object = MibTable
tcstStatGroupTable = _TcstStatGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tcstStatGroupTable.setStatus("current")
_TcstStatGroupEntry_Object = MibTableRow
tcstStatGroupEntry = _TcstStatGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1)
)
tcstStatGroupEntry.setIndexNames(
    (0, "MOXA-TCST-MIB", "tcstStatIfIndex"),
)
if mibBuilder.loadTexts:
    tcstStatGroupEntry.setStatus("current")
_TcstStatIfIndex_Type = Integer32
_TcstStatIfIndex_Object = MibTableColumn
tcstStatIfIndex = _TcstStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 1),
    _TcstStatIfIndex_Type()
)
tcstStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcstStatIfIndex.setStatus("current")
_TcstStatTxTotalOctets_Type = Counter32
_TcstStatTxTotalOctets_Object = MibTableColumn
tcstStatTxTotalOctets = _TcstStatTxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 2),
    _TcstStatTxTotalOctets_Type()
)
tcstStatTxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatTxTotalOctets.setStatus("current")
_TcstStatTxTotalPackets_Type = Counter32
_TcstStatTxTotalPackets_Object = MibTableColumn
tcstStatTxTotalPackets = _TcstStatTxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 3),
    _TcstStatTxTotalPackets_Type()
)
tcstStatTxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatTxTotalPackets.setStatus("current")
_TcstStatTxUnicastPackets_Type = Counter32
_TcstStatTxUnicastPackets_Object = MibTableColumn
tcstStatTxUnicastPackets = _TcstStatTxUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 4),
    _TcstStatTxUnicastPackets_Type()
)
tcstStatTxUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatTxUnicastPackets.setStatus("current")
_TcstStatTxMulticastPackets_Type = Counter32
_TcstStatTxMulticastPackets_Object = MibTableColumn
tcstStatTxMulticastPackets = _TcstStatTxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 5),
    _TcstStatTxMulticastPackets_Type()
)
tcstStatTxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatTxMulticastPackets.setStatus("current")
_TcstStatTxBroadcastPackets_Type = Counter32
_TcstStatTxBroadcastPackets_Object = MibTableColumn
tcstStatTxBroadcastPackets = _TcstStatTxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 6),
    _TcstStatTxBroadcastPackets_Type()
)
tcstStatTxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatTxBroadcastPackets.setStatus("current")
_TcstStatRxTotalOctets_Type = Counter32
_TcstStatRxTotalOctets_Object = MibTableColumn
tcstStatRxTotalOctets = _TcstStatRxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 7),
    _TcstStatRxTotalOctets_Type()
)
tcstStatRxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatRxTotalOctets.setStatus("current")
_TcstStatRxTotalPackets_Type = Counter32
_TcstStatRxTotalPackets_Object = MibTableColumn
tcstStatRxTotalPackets = _TcstStatRxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 8),
    _TcstStatRxTotalPackets_Type()
)
tcstStatRxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatRxTotalPackets.setStatus("current")
_TcstStatRxUnicastPackets_Type = Counter32
_TcstStatRxUnicastPackets_Object = MibTableColumn
tcstStatRxUnicastPackets = _TcstStatRxUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 9),
    _TcstStatRxUnicastPackets_Type()
)
tcstStatRxUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatRxUnicastPackets.setStatus("current")
_TcstStatRxMulticastPackets_Type = Counter32
_TcstStatRxMulticastPackets_Object = MibTableColumn
tcstStatRxMulticastPackets = _TcstStatRxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 10),
    _TcstStatRxMulticastPackets_Type()
)
tcstStatRxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatRxMulticastPackets.setStatus("current")
_TcstStatRxBroadcastPackets_Type = Counter32
_TcstStatRxBroadcastPackets_Object = MibTableColumn
tcstStatRxBroadcastPackets = _TcstStatRxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 11),
    _TcstStatRxBroadcastPackets_Type()
)
tcstStatRxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatRxBroadcastPackets.setStatus("current")
_TcstStatRxPausePackets_Type = Counter32
_TcstStatRxPausePackets_Object = MibTableColumn
tcstStatRxPausePackets = _TcstStatRxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 12),
    _TcstStatRxPausePackets_Type()
)
tcstStatRxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatRxPausePackets.setStatus("current")
_TcstStatCollisionPackets_Type = Counter32
_TcstStatCollisionPackets_Object = MibTableColumn
tcstStatCollisionPackets = _TcstStatCollisionPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 13),
    _TcstStatCollisionPackets_Type()
)
tcstStatCollisionPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatCollisionPackets.setStatus("current")
_TcstStatLateCollisionPackets_Type = Counter32
_TcstStatLateCollisionPackets_Object = MibTableColumn
tcstStatLateCollisionPackets = _TcstStatLateCollisionPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 14),
    _TcstStatLateCollisionPackets_Type()
)
tcstStatLateCollisionPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatLateCollisionPackets.setStatus("current")
_TcstStatExcessiveCollisionPackets_Type = Counter32
_TcstStatExcessiveCollisionPackets_Object = MibTableColumn
tcstStatExcessiveCollisionPackets = _TcstStatExcessiveCollisionPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 15),
    _TcstStatExcessiveCollisionPackets_Type()
)
tcstStatExcessiveCollisionPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatExcessiveCollisionPackets.setStatus("current")
_TcstStatsCRCAlignErrorPackets_Type = Counter32
_TcstStatsCRCAlignErrorPackets_Object = MibTableColumn
tcstStatsCRCAlignErrorPackets = _TcstStatsCRCAlignErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 16),
    _TcstStatsCRCAlignErrorPackets_Type()
)
tcstStatsCRCAlignErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatsCRCAlignErrorPackets.setStatus("current")
_TcstStatDropPackets_Type = Counter32
_TcstStatDropPackets_Object = MibTableColumn
tcstStatDropPackets = _TcstStatDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 17),
    _TcstStatDropPackets_Type()
)
tcstStatDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatDropPackets.setStatus("current")
_TcstStatUndersizePackets_Type = Counter32
_TcstStatUndersizePackets_Object = MibTableColumn
tcstStatUndersizePackets = _TcstStatUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 18),
    _TcstStatUndersizePackets_Type()
)
tcstStatUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatUndersizePackets.setStatus("current")
_TcstStatOversizePackets_Type = Counter32
_TcstStatOversizePackets_Object = MibTableColumn
tcstStatOversizePackets = _TcstStatOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 19),
    _TcstStatOversizePackets_Type()
)
tcstStatOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatOversizePackets.setStatus("current")
_TcstStatFragmentPackets_Type = Counter32
_TcstStatFragmentPackets_Object = MibTableColumn
tcstStatFragmentPackets = _TcstStatFragmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 20),
    _TcstStatFragmentPackets_Type()
)
tcstStatFragmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatFragmentPackets.setStatus("current")
_TcstStatJabberPackets_Type = Counter32
_TcstStatJabberPackets_Object = MibTableColumn
tcstStatJabberPackets = _TcstStatJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 21),
    _TcstStatJabberPackets_Type()
)
tcstStatJabberPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatJabberPackets.setStatus("current")
_TcstStatRxNonUnicastPackets_Type = Counter32
_TcstStatRxNonUnicastPackets_Object = MibTableColumn
tcstStatRxNonUnicastPackets = _TcstStatRxNonUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 22),
    _TcstStatRxNonUnicastPackets_Type()
)
tcstStatRxNonUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatRxNonUnicastPackets.setStatus("current")
_TcstStatRxErrorsPackets_Type = Counter32
_TcstStatRxErrorsPackets_Object = MibTableColumn
tcstStatRxErrorsPackets = _TcstStatRxErrorsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 23),
    _TcstStatRxErrorsPackets_Type()
)
tcstStatRxErrorsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatRxErrorsPackets.setStatus("current")
_TcstStatRxUnknownProtosPackets_Type = Counter32
_TcstStatRxUnknownProtosPackets_Object = MibTableColumn
tcstStatRxUnknownProtosPackets = _TcstStatRxUnknownProtosPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 24),
    _TcstStatRxUnknownProtosPackets_Type()
)
tcstStatRxUnknownProtosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatRxUnknownProtosPackets.setStatus("current")
_TcstStatTxNonUnicastPackets_Type = Counter32
_TcstStatTxNonUnicastPackets_Object = MibTableColumn
tcstStatTxNonUnicastPackets = _TcstStatTxNonUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 25),
    _TcstStatTxNonUnicastPackets_Type()
)
tcstStatTxNonUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatTxNonUnicastPackets.setStatus("current")
_TcstStatTxDiscardsPackets_Type = Counter32
_TcstStatTxDiscardsPackets_Object = MibTableColumn
tcstStatTxDiscardsPackets = _TcstStatTxDiscardsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 26),
    _TcstStatTxDiscardsPackets_Type()
)
tcstStatTxDiscardsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatTxDiscardsPackets.setStatus("current")
_TcstStatTxErrorsPackets_Type = Counter32
_TcstStatTxErrorsPackets_Object = MibTableColumn
tcstStatTxErrorsPackets = _TcstStatTxErrorsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 27),
    _TcstStatTxErrorsPackets_Type()
)
tcstStatTxErrorsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatTxErrorsPackets.setStatus("current")
_TcstStatMultipleCollisionsPackets_Type = Counter32
_TcstStatMultipleCollisionsPackets_Object = MibTableColumn
tcstStatMultipleCollisionsPackets = _TcstStatMultipleCollisionsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 28),
    _TcstStatMultipleCollisionsPackets_Type()
)
tcstStatMultipleCollisionsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatMultipleCollisionsPackets.setStatus("current")
_TcstStatSQETestErrorsPackets_Type = Counter32
_TcstStatSQETestErrorsPackets_Object = MibTableColumn
tcstStatSQETestErrorsPackets = _TcstStatSQETestErrorsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 29),
    _TcstStatSQETestErrorsPackets_Type()
)
tcstStatSQETestErrorsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatSQETestErrorsPackets.setStatus("current")
_TcstStatDeferredTransmissionsPackets_Type = Counter32
_TcstStatDeferredTransmissionsPackets_Object = MibTableColumn
tcstStatDeferredTransmissionsPackets = _TcstStatDeferredTransmissionsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 30),
    _TcstStatDeferredTransmissionsPackets_Type()
)
tcstStatDeferredTransmissionsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatDeferredTransmissionsPackets.setStatus("current")
_TcstStatMacTransmitErrorsPackets_Type = Counter32
_TcstStatMacTransmitErrorsPackets_Object = MibTableColumn
tcstStatMacTransmitErrorsPackets = _TcstStatMacTransmitErrorsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 31),
    _TcstStatMacTransmitErrorsPackets_Type()
)
tcstStatMacTransmitErrorsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatMacTransmitErrorsPackets.setStatus("current")
_TcstStatCarrierSenseErrorsPackets_Type = Counter32
_TcstStatCarrierSenseErrorsPackets_Object = MibTableColumn
tcstStatCarrierSenseErrorsPackets = _TcstStatCarrierSenseErrorsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 32),
    _TcstStatCarrierSenseErrorsPackets_Type()
)
tcstStatCarrierSenseErrorsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatCarrierSenseErrorsPackets.setStatus("current")
_TcstStatFrameTooLongPackets_Type = Counter32
_TcstStatFrameTooLongPackets_Object = MibTableColumn
tcstStatFrameTooLongPackets = _TcstStatFrameTooLongPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 33),
    _TcstStatFrameTooLongPackets_Type()
)
tcstStatFrameTooLongPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatFrameTooLongPackets.setStatus("current")
_TcstStatMacReceiveErrorsPackets_Type = Counter32
_TcstStatMacReceiveErrorsPackets_Object = MibTableColumn
tcstStatMacReceiveErrorsPackets = _TcstStatMacReceiveErrorsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 34),
    _TcstStatMacReceiveErrorsPackets_Type()
)
tcstStatMacReceiveErrorsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatMacReceiveErrorsPackets.setStatus("current")
_TcstStatSymbolErrorsPackets_Type = Counter32
_TcstStatSymbolErrorsPackets_Object = MibTableColumn
tcstStatSymbolErrorsPackets = _TcstStatSymbolErrorsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 35),
    _TcstStatSymbolErrorsPackets_Type()
)
tcstStatSymbolErrorsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatSymbolErrorsPackets.setStatus("current")
_TcstStatAlignmentErrorsPackets_Type = Counter32
_TcstStatAlignmentErrorsPackets_Object = MibTableColumn
tcstStatAlignmentErrorsPackets = _TcstStatAlignmentErrorsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 4, 2, 1, 1, 36),
    _TcstStatAlignmentErrorsPackets_Type()
)
tcstStatAlignmentErrorsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcstStatAlignmentErrorsPackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-TCST-MIB",
    **{"mxTcst": mxTcst,
       "tcstConfiguration": tcstConfiguration,
       "tcstConfigClearAllStatistics": tcstConfigClearAllStatistics,
       "tcstConfigClearPortStatisticsTable": tcstConfigClearPortStatisticsTable,
       "tcstConfigClearPortStatisticsEntry": tcstConfigClearPortStatisticsEntry,
       "tcstConfigIfIndex": tcstConfigIfIndex,
       "tcstConfigClearPortStatistics": tcstConfigClearPortStatistics,
       "tcstStatus": tcstStatus,
       "tcstStatGroupTable": tcstStatGroupTable,
       "tcstStatGroupEntry": tcstStatGroupEntry,
       "tcstStatIfIndex": tcstStatIfIndex,
       "tcstStatTxTotalOctets": tcstStatTxTotalOctets,
       "tcstStatTxTotalPackets": tcstStatTxTotalPackets,
       "tcstStatTxUnicastPackets": tcstStatTxUnicastPackets,
       "tcstStatTxMulticastPackets": tcstStatTxMulticastPackets,
       "tcstStatTxBroadcastPackets": tcstStatTxBroadcastPackets,
       "tcstStatRxTotalOctets": tcstStatRxTotalOctets,
       "tcstStatRxTotalPackets": tcstStatRxTotalPackets,
       "tcstStatRxUnicastPackets": tcstStatRxUnicastPackets,
       "tcstStatRxMulticastPackets": tcstStatRxMulticastPackets,
       "tcstStatRxBroadcastPackets": tcstStatRxBroadcastPackets,
       "tcstStatRxPausePackets": tcstStatRxPausePackets,
       "tcstStatCollisionPackets": tcstStatCollisionPackets,
       "tcstStatLateCollisionPackets": tcstStatLateCollisionPackets,
       "tcstStatExcessiveCollisionPackets": tcstStatExcessiveCollisionPackets,
       "tcstStatsCRCAlignErrorPackets": tcstStatsCRCAlignErrorPackets,
       "tcstStatDropPackets": tcstStatDropPackets,
       "tcstStatUndersizePackets": tcstStatUndersizePackets,
       "tcstStatOversizePackets": tcstStatOversizePackets,
       "tcstStatFragmentPackets": tcstStatFragmentPackets,
       "tcstStatJabberPackets": tcstStatJabberPackets,
       "tcstStatRxNonUnicastPackets": tcstStatRxNonUnicastPackets,
       "tcstStatRxErrorsPackets": tcstStatRxErrorsPackets,
       "tcstStatRxUnknownProtosPackets": tcstStatRxUnknownProtosPackets,
       "tcstStatTxNonUnicastPackets": tcstStatTxNonUnicastPackets,
       "tcstStatTxDiscardsPackets": tcstStatTxDiscardsPackets,
       "tcstStatTxErrorsPackets": tcstStatTxErrorsPackets,
       "tcstStatMultipleCollisionsPackets": tcstStatMultipleCollisionsPackets,
       "tcstStatSQETestErrorsPackets": tcstStatSQETestErrorsPackets,
       "tcstStatDeferredTransmissionsPackets": tcstStatDeferredTransmissionsPackets,
       "tcstStatMacTransmitErrorsPackets": tcstStatMacTransmitErrorsPackets,
       "tcstStatCarrierSenseErrorsPackets": tcstStatCarrierSenseErrorsPackets,
       "tcstStatFrameTooLongPackets": tcstStatFrameTooLongPackets,
       "tcstStatMacReceiveErrorsPackets": tcstStatMacReceiveErrorsPackets,
       "tcstStatSymbolErrorsPackets": tcstStatSymbolErrorsPackets,
       "tcstStatAlignmentErrorsPackets": tcstStatAlignmentErrorsPackets}
)
