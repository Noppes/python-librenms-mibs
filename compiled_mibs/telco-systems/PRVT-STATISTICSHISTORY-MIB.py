# SNMP MIB module (PRVT-STATISTICSHISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-STATISTICSHISTORY-MIB

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtStatisticsHistoryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140)
)
if mibBuilder.loadTexts:
    prvtStatisticsHistoryMib.setRevisions(
        ("2010-02-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtStatisticsHistoryNotifications_ObjectIdentity = ObjectIdentity
prvtStatisticsHistoryNotifications = _PrvtStatisticsHistoryNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 0)
)
_PrvtStatisticsHistoryObjects_ObjectIdentity = ObjectIdentity
prvtStatisticsHistoryObjects = _PrvtStatisticsHistoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1)
)
_PrvtStatisticsHistoryCfg_ObjectIdentity = ObjectIdentity
prvtStatisticsHistoryCfg = _PrvtStatisticsHistoryCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 1)
)


class _PrvtStatHistAdminStatus_Type(Integer32):
    """Custom type prvtStatHistAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PrvtStatHistAdminStatus_Type.__name__ = "Integer32"
_PrvtStatHistAdminStatus_Object = MibScalar
prvtStatHistAdminStatus = _PrvtStatHistAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 1, 1),
    _PrvtStatHistAdminStatus_Type()
)
prvtStatHistAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatHistAdminStatus.setStatus("current")


class _PrvtStatHistGetInterval_Type(Integer32):
    """Custom type prvtStatHistGetInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interval15min", 1),
          ("interval30min", 2),
          ("interval60min", 3))
    )


_PrvtStatHistGetInterval_Type.__name__ = "Integer32"
_PrvtStatHistGetInterval_Object = MibScalar
prvtStatHistGetInterval = _PrvtStatHistGetInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 1, 2),
    _PrvtStatHistGetInterval_Type()
)
prvtStatHistGetInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatHistGetInterval.setStatus("current")
if mibBuilder.loadTexts:
    prvtStatHistGetInterval.setUnits("minutes")


class _PrvtStatHistWriteInterval_Type(Integer32):
    """Custom type prvtStatHistWriteInterval based on Integer32"""
    defaultValue = 1

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
        *(("interval1h", 1),
          ("interval6h", 2),
          ("interval12h", 3),
          ("interval24h", 4))
    )


_PrvtStatHistWriteInterval_Type.__name__ = "Integer32"
_PrvtStatHistWriteInterval_Object = MibScalar
prvtStatHistWriteInterval = _PrvtStatHistWriteInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 1, 3),
    _PrvtStatHistWriteInterval_Type()
)
prvtStatHistWriteInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatHistWriteInterval.setStatus("current")
if mibBuilder.loadTexts:
    prvtStatHistWriteInterval.setUnits("hours")


class _PrvtStatHistPath_Type(DisplayString):
    """Custom type prvtStatHistPath based on DisplayString"""
    defaultValue = OctetString("/var/stats")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PrvtStatHistPath_Type.__name__ = "DisplayString"
_PrvtStatHistPath_Object = MibScalar
prvtStatHistPath = _PrvtStatHistPath_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 1, 4),
    _PrvtStatHistPath_Type()
)
prvtStatHistPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatHistPath.setStatus("current")
_PrvtStatisticsHistoryIntCfgTable_Object = MibTable
prvtStatisticsHistoryIntCfgTable = _PrvtStatisticsHistoryIntCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 1, 5)
)
if mibBuilder.loadTexts:
    prvtStatisticsHistoryIntCfgTable.setStatus("current")
_PrvtStatisticsHistoryIntCfgEntry_Object = MibTableRow
prvtStatisticsHistoryIntCfgEntry = _PrvtStatisticsHistoryIntCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 1, 5, 1)
)
prvtStatisticsHistoryIntCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtStatisticsHistoryIntCfgEntry.setStatus("current")


class _PrvtStatHistIntAdminStatus_Type(Integer32):
    """Custom type prvtStatHistIntAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PrvtStatHistIntAdminStatus_Type.__name__ = "Integer32"
_PrvtStatHistIntAdminStatus_Object = MibTableColumn
prvtStatHistIntAdminStatus = _PrvtStatHistIntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 1, 5, 1, 1),
    _PrvtStatHistIntAdminStatus_Type()
)
prvtStatHistIntAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatHistIntAdminStatus.setStatus("current")
_PrvtStatHistDailySnapshotData_ObjectIdentity = ObjectIdentity
prvtStatHistDailySnapshotData = _PrvtStatHistDailySnapshotData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2)
)


class _PrvtStatHistDailySnapshotAdminStatus_Type(Integer32):
    """Custom type prvtStatHistDailySnapshotAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PrvtStatHistDailySnapshotAdminStatus_Type.__name__ = "Integer32"
_PrvtStatHistDailySnapshotAdminStatus_Object = MibScalar
prvtStatHistDailySnapshotAdminStatus = _PrvtStatHistDailySnapshotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 1),
    _PrvtStatHistDailySnapshotAdminStatus_Type()
)
prvtStatHistDailySnapshotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDailySnapshotAdminStatus.setStatus("current")


class _PrvtStatHistDailySnapshotGetInterval_Type(Integer32):
    """Custom type prvtStatHistDailySnapshotGetInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interval15min", 1),
          ("interval30min", 2),
          ("interval60min", 3))
    )


_PrvtStatHistDailySnapshotGetInterval_Type.__name__ = "Integer32"
_PrvtStatHistDailySnapshotGetInterval_Object = MibScalar
prvtStatHistDailySnapshotGetInterval = _PrvtStatHistDailySnapshotGetInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 2),
    _PrvtStatHistDailySnapshotGetInterval_Type()
)
prvtStatHistDailySnapshotGetInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDailySnapshotGetInterval.setStatus("current")
if mibBuilder.loadTexts:
    prvtStatHistDailySnapshotGetInterval.setUnits("minutes")


class _PrvtStatHistDailySnapshotWriteInterval_Type(Integer32):
    """Custom type prvtStatHistDailySnapshotWriteInterval based on Integer32"""
    defaultValue = 1

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
        *(("interval1h", 1),
          ("interval6h", 2),
          ("interval12h", 3),
          ("interval24h", 4))
    )


_PrvtStatHistDailySnapshotWriteInterval_Type.__name__ = "Integer32"
_PrvtStatHistDailySnapshotWriteInterval_Object = MibScalar
prvtStatHistDailySnapshotWriteInterval = _PrvtStatHistDailySnapshotWriteInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 3),
    _PrvtStatHistDailySnapshotWriteInterval_Type()
)
prvtStatHistDailySnapshotWriteInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDailySnapshotWriteInterval.setStatus("current")
if mibBuilder.loadTexts:
    prvtStatHistDailySnapshotWriteInterval.setUnits("hours")


class _PrvtStatHistDailySnapshotPath_Type(DisplayString):
    """Custom type prvtStatHistDailySnapshotPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PrvtStatHistDailySnapshotPath_Type.__name__ = "DisplayString"
_PrvtStatHistDailySnapshotPath_Object = MibScalar
prvtStatHistDailySnapshotPath = _PrvtStatHistDailySnapshotPath_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 4),
    _PrvtStatHistDailySnapshotPath_Type()
)
prvtStatHistDailySnapshotPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDailySnapshotPath.setStatus("current")
_PrvtStatisticsHistoryDataTable_Object = MibTable
prvtStatisticsHistoryDataTable = _PrvtStatisticsHistoryDataTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5)
)
if mibBuilder.loadTexts:
    prvtStatisticsHistoryDataTable.setStatus("current")
_PrvtStatisticsHistoryDataEntry_Object = MibTableRow
prvtStatisticsHistoryDataEntry = _PrvtStatisticsHistoryDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1)
)
prvtStatisticsHistoryDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-STATISTICSHISTORY-MIB", "prvtStatHistInterval"),
)
if mibBuilder.loadTexts:
    prvtStatisticsHistoryDataEntry.setStatus("current")
_PrvtStatHistInterval_Type = Unsigned32
_PrvtStatHistInterval_Object = MibTableColumn
prvtStatHistInterval = _PrvtStatHistInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 1),
    _PrvtStatHistInterval_Type()
)
prvtStatHistInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStatHistInterval.setStatus("current")
_PrvtStatHistLast5secInPkts_Type = Counter32
_PrvtStatHistLast5secInPkts_Object = MibTableColumn
prvtStatHistLast5secInPkts = _PrvtStatHistLast5secInPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 2),
    _PrvtStatHistLast5secInPkts_Type()
)
prvtStatHistLast5secInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast5secInPkts.setStatus("current")
_PrvtStatHistLast1minInPkts_Type = Counter32
_PrvtStatHistLast1minInPkts_Object = MibTableColumn
prvtStatHistLast1minInPkts = _PrvtStatHistLast1minInPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 3),
    _PrvtStatHistLast1minInPkts_Type()
)
prvtStatHistLast1minInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast1minInPkts.setStatus("current")
_PrvtStatHistLast5minInPkts_Type = Counter32
_PrvtStatHistLast5minInPkts_Object = MibTableColumn
prvtStatHistLast5minInPkts = _PrvtStatHistLast5minInPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 4),
    _PrvtStatHistLast5minInPkts_Type()
)
prvtStatHistLast5minInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast5minInPkts.setStatus("current")
_PrvtStatHistLast5secOutPkts_Type = Counter32
_PrvtStatHistLast5secOutPkts_Object = MibTableColumn
prvtStatHistLast5secOutPkts = _PrvtStatHistLast5secOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 5),
    _PrvtStatHistLast5secOutPkts_Type()
)
prvtStatHistLast5secOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast5secOutPkts.setStatus("current")
_PrvtStatHistLast1minOutPkts_Type = Counter32
_PrvtStatHistLast1minOutPkts_Object = MibTableColumn
prvtStatHistLast1minOutPkts = _PrvtStatHistLast1minOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 6),
    _PrvtStatHistLast1minOutPkts_Type()
)
prvtStatHistLast1minOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast1minOutPkts.setStatus("current")
_PrvtStatHistLast5minOutPkts_Type = Counter32
_PrvtStatHistLast5minOutPkts_Object = MibTableColumn
prvtStatHistLast5minOutPkts = _PrvtStatHistLast5minOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 7),
    _PrvtStatHistLast5minOutPkts_Type()
)
prvtStatHistLast5minOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast5minOutPkts.setStatus("current")
_PrvtStatHistLast5secInBps_Type = Counter64
_PrvtStatHistLast5secInBps_Object = MibTableColumn
prvtStatHistLast5secInBps = _PrvtStatHistLast5secInBps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 8),
    _PrvtStatHistLast5secInBps_Type()
)
prvtStatHistLast5secInBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast5secInBps.setStatus("current")
_PrvtStatHistLast1minInBps_Type = Counter64
_PrvtStatHistLast1minInBps_Object = MibTableColumn
prvtStatHistLast1minInBps = _PrvtStatHistLast1minInBps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 9),
    _PrvtStatHistLast1minInBps_Type()
)
prvtStatHistLast1minInBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast1minInBps.setStatus("current")
_PrvtStatHistLast5minInBps_Type = Counter64
_PrvtStatHistLast5minInBps_Object = MibTableColumn
prvtStatHistLast5minInBps = _PrvtStatHistLast5minInBps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 10),
    _PrvtStatHistLast5minInBps_Type()
)
prvtStatHistLast5minInBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast5minInBps.setStatus("current")
_PrvtStatHistLast5secOutBps_Type = Counter64
_PrvtStatHistLast5secOutBps_Object = MibTableColumn
prvtStatHistLast5secOutBps = _PrvtStatHistLast5secOutBps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 11),
    _PrvtStatHistLast5secOutBps_Type()
)
prvtStatHistLast5secOutBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast5secOutBps.setStatus("current")
_PrvtStatHistLast1minOutBps_Type = Counter64
_PrvtStatHistLast1minOutBps_Object = MibTableColumn
prvtStatHistLast1minOutBps = _PrvtStatHistLast1minOutBps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 12),
    _PrvtStatHistLast1minOutBps_Type()
)
prvtStatHistLast1minOutBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast1minOutBps.setStatus("current")
_PrvtStatHistLast5minOutBps_Type = Counter64
_PrvtStatHistLast5minOutBps_Object = MibTableColumn
prvtStatHistLast5minOutBps = _PrvtStatHistLast5minOutBps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 13),
    _PrvtStatHistLast5minOutBps_Type()
)
prvtStatHistLast5minOutBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistLast5minOutBps.setStatus("current")
_PrvtStatHistEtherStatsDropEvents_Type = Counter32
_PrvtStatHistEtherStatsDropEvents_Object = MibTableColumn
prvtStatHistEtherStatsDropEvents = _PrvtStatHistEtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 14),
    _PrvtStatHistEtherStatsDropEvents_Type()
)
prvtStatHistEtherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsDropEvents.setStatus("current")
_PrvtStatHistEtherStatsPkts_Type = Counter32
_PrvtStatHistEtherStatsPkts_Object = MibTableColumn
prvtStatHistEtherStatsPkts = _PrvtStatHistEtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 15),
    _PrvtStatHistEtherStatsPkts_Type()
)
prvtStatHistEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsPkts.setStatus("current")
_PrvtStatHistEtherStatsBroadcastPkts_Type = Counter32
_PrvtStatHistEtherStatsBroadcastPkts_Object = MibTableColumn
prvtStatHistEtherStatsBroadcastPkts = _PrvtStatHistEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 16),
    _PrvtStatHistEtherStatsBroadcastPkts_Type()
)
prvtStatHistEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsBroadcastPkts.setStatus("current")
_PrvtStatHistEtherStatsMulticastPkts_Type = Counter32
_PrvtStatHistEtherStatsMulticastPkts_Object = MibTableColumn
prvtStatHistEtherStatsMulticastPkts = _PrvtStatHistEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 17),
    _PrvtStatHistEtherStatsMulticastPkts_Type()
)
prvtStatHistEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsMulticastPkts.setStatus("current")
_PrvtStatHistEtherStatsCRCAlignErrors_Type = Counter32
_PrvtStatHistEtherStatsCRCAlignErrors_Object = MibTableColumn
prvtStatHistEtherStatsCRCAlignErrors = _PrvtStatHistEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 18),
    _PrvtStatHistEtherStatsCRCAlignErrors_Type()
)
prvtStatHistEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsCRCAlignErrors.setStatus("current")
_PrvtStatHistEtherStatsUndersizePkts_Type = Counter32
_PrvtStatHistEtherStatsUndersizePkts_Object = MibTableColumn
prvtStatHistEtherStatsUndersizePkts = _PrvtStatHistEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 19),
    _PrvtStatHistEtherStatsUndersizePkts_Type()
)
prvtStatHistEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsUndersizePkts.setStatus("current")
_PrvtStatHistEtherStatsOversizePkts_Type = Counter32
_PrvtStatHistEtherStatsOversizePkts_Object = MibTableColumn
prvtStatHistEtherStatsOversizePkts = _PrvtStatHistEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 20),
    _PrvtStatHistEtherStatsOversizePkts_Type()
)
prvtStatHistEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsOversizePkts.setStatus("current")
_PrvtStatHistEtherStatsFragments_Type = Counter32
_PrvtStatHistEtherStatsFragments_Object = MibTableColumn
prvtStatHistEtherStatsFragments = _PrvtStatHistEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 21),
    _PrvtStatHistEtherStatsFragments_Type()
)
prvtStatHistEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsFragments.setStatus("current")
_PrvtStatHistEtherStatsJabbers_Type = Counter32
_PrvtStatHistEtherStatsJabbers_Object = MibTableColumn
prvtStatHistEtherStatsJabbers = _PrvtStatHistEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 22),
    _PrvtStatHistEtherStatsJabbers_Type()
)
prvtStatHistEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsJabbers.setStatus("current")
_PrvtStatHistEtherStatsCollisions_Type = Counter32
_PrvtStatHistEtherStatsCollisions_Object = MibTableColumn
prvtStatHistEtherStatsCollisions = _PrvtStatHistEtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 23),
    _PrvtStatHistEtherStatsCollisions_Type()
)
prvtStatHistEtherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsCollisions.setStatus("current")
_PrvtStatHistEtherStatsDroppedFrames_Type = Counter32
_PrvtStatHistEtherStatsDroppedFrames_Object = MibTableColumn
prvtStatHistEtherStatsDroppedFrames = _PrvtStatHistEtherStatsDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 24),
    _PrvtStatHistEtherStatsDroppedFrames_Type()
)
prvtStatHistEtherStatsDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsDroppedFrames.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityOverflowPkts_Type = Counter32
_PrvtStatHistEtherStatsHighCapacityOverflowPkts_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityOverflowPkts = _PrvtStatHistEtherStatsHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 25),
    _PrvtStatHistEtherStatsHighCapacityOverflowPkts_Type()
)
prvtStatHistEtherStatsHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityOverflowPkts.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityOverflowOctets_Type = Counter32
_PrvtStatHistEtherStatsHighCapacityOverflowOctets_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityOverflowOctets = _PrvtStatHistEtherStatsHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 26),
    _PrvtStatHistEtherStatsHighCapacityOverflowOctets_Type()
)
prvtStatHistEtherStatsHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityOverflowOctets.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityPkts_Type = Counter64
_PrvtStatHistEtherStatsHighCapacityPkts_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityPkts = _PrvtStatHistEtherStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 27),
    _PrvtStatHistEtherStatsHighCapacityPkts_Type()
)
prvtStatHistEtherStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityPkts.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityOctets_Type = Counter64
_PrvtStatHistEtherStatsHighCapacityOctets_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityOctets = _PrvtStatHistEtherStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 28),
    _PrvtStatHistEtherStatsHighCapacityOctets_Type()
)
prvtStatHistEtherStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityOctets.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityPkts64Octets_Type = Counter64
_PrvtStatHistEtherStatsHighCapacityPkts64Octets_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityPkts64Octets = _PrvtStatHistEtherStatsHighCapacityPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 29),
    _PrvtStatHistEtherStatsHighCapacityPkts64Octets_Type()
)
prvtStatHistEtherStatsHighCapacityPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityPkts64Octets.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityPkts65to127Octets_Type = Counter64
_PrvtStatHistEtherStatsHighCapacityPkts65to127Octets_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityPkts65to127Octets = _PrvtStatHistEtherStatsHighCapacityPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 30),
    _PrvtStatHistEtherStatsHighCapacityPkts65to127Octets_Type()
)
prvtStatHistEtherStatsHighCapacityPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityPkts65to127Octets.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityPkts128to255Octets_Type = Counter64
_PrvtStatHistEtherStatsHighCapacityPkts128to255Octets_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityPkts128to255Octets = _PrvtStatHistEtherStatsHighCapacityPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 31),
    _PrvtStatHistEtherStatsHighCapacityPkts128to255Octets_Type()
)
prvtStatHistEtherStatsHighCapacityPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityPkts128to255Octets.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityPkts256to511Octets_Type = Counter64
_PrvtStatHistEtherStatsHighCapacityPkts256to511Octets_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityPkts256to511Octets = _PrvtStatHistEtherStatsHighCapacityPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 32),
    _PrvtStatHistEtherStatsHighCapacityPkts256to511Octets_Type()
)
prvtStatHistEtherStatsHighCapacityPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityPkts256to511Octets.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityPkts512to1023Octets_Type = Counter64
_PrvtStatHistEtherStatsHighCapacityPkts512to1023Octets_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityPkts512to1023Octets = _PrvtStatHistEtherStatsHighCapacityPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 33),
    _PrvtStatHistEtherStatsHighCapacityPkts512to1023Octets_Type()
)
prvtStatHistEtherStatsHighCapacityPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityPkts512to1023Octets.setStatus("current")
_PrvtStatHistEtherStatsHighCapacityPkts1024to1518Octets_Type = Counter64
_PrvtStatHistEtherStatsHighCapacityPkts1024to1518Octets_Object = MibTableColumn
prvtStatHistEtherStatsHighCapacityPkts1024to1518Octets = _PrvtStatHistEtherStatsHighCapacityPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 34),
    _PrvtStatHistEtherStatsHighCapacityPkts1024to1518Octets_Type()
)
prvtStatHistEtherStatsHighCapacityPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistEtherStatsHighCapacityPkts1024to1518Octets.setStatus("current")
_PrvtStatHistDot3StatsAlignmentErrors_Type = Counter32
_PrvtStatHistDot3StatsAlignmentErrors_Object = MibTableColumn
prvtStatHistDot3StatsAlignmentErrors = _PrvtStatHistDot3StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 35),
    _PrvtStatHistDot3StatsAlignmentErrors_Type()
)
prvtStatHistDot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsAlignmentErrors.setStatus("current")
_PrvtStatHistDot3StatsFCSErrors_Type = Counter32
_PrvtStatHistDot3StatsFCSErrors_Object = MibTableColumn
prvtStatHistDot3StatsFCSErrors = _PrvtStatHistDot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 36),
    _PrvtStatHistDot3StatsFCSErrors_Type()
)
prvtStatHistDot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsFCSErrors.setStatus("current")
_PrvtStatHistDot3StatsSingleCollisionFrames_Type = Counter32
_PrvtStatHistDot3StatsSingleCollisionFrames_Object = MibTableColumn
prvtStatHistDot3StatsSingleCollisionFrames = _PrvtStatHistDot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 37),
    _PrvtStatHistDot3StatsSingleCollisionFrames_Type()
)
prvtStatHistDot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsSingleCollisionFrames.setStatus("current")
_PrvtStatHistDot3StatsMultipleCollisionFrames_Type = Counter32
_PrvtStatHistDot3StatsMultipleCollisionFrames_Object = MibTableColumn
prvtStatHistDot3StatsMultipleCollisionFrames = _PrvtStatHistDot3StatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 38),
    _PrvtStatHistDot3StatsMultipleCollisionFrames_Type()
)
prvtStatHistDot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsMultipleCollisionFrames.setStatus("current")
_PrvtStatHistDot3StatsSQETestErrors_Type = Counter32
_PrvtStatHistDot3StatsSQETestErrors_Object = MibTableColumn
prvtStatHistDot3StatsSQETestErrors = _PrvtStatHistDot3StatsSQETestErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 39),
    _PrvtStatHistDot3StatsSQETestErrors_Type()
)
prvtStatHistDot3StatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsSQETestErrors.setStatus("current")
_PrvtStatHistDot3StatsDeferredTransmissions_Type = Counter32
_PrvtStatHistDot3StatsDeferredTransmissions_Object = MibTableColumn
prvtStatHistDot3StatsDeferredTransmissions = _PrvtStatHistDot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 40),
    _PrvtStatHistDot3StatsDeferredTransmissions_Type()
)
prvtStatHistDot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsDeferredTransmissions.setStatus("current")
_PrvtStatHistDot3StatsLateCollisions_Type = Counter32
_PrvtStatHistDot3StatsLateCollisions_Object = MibTableColumn
prvtStatHistDot3StatsLateCollisions = _PrvtStatHistDot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 41),
    _PrvtStatHistDot3StatsLateCollisions_Type()
)
prvtStatHistDot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsLateCollisions.setStatus("current")
_PrvtStatHistDot3StatsExcessiveCollisions_Type = Counter32
_PrvtStatHistDot3StatsExcessiveCollisions_Object = MibTableColumn
prvtStatHistDot3StatsExcessiveCollisions = _PrvtStatHistDot3StatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 42),
    _PrvtStatHistDot3StatsExcessiveCollisions_Type()
)
prvtStatHistDot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsExcessiveCollisions.setStatus("current")
_PrvtStatHistDot3StatsInternalMacTransmitErrors_Type = Counter32
_PrvtStatHistDot3StatsInternalMacTransmitErrors_Object = MibTableColumn
prvtStatHistDot3StatsInternalMacTransmitErrors = _PrvtStatHistDot3StatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 43),
    _PrvtStatHistDot3StatsInternalMacTransmitErrors_Type()
)
prvtStatHistDot3StatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsInternalMacTransmitErrors.setStatus("current")
_PrvtStatHistDot3StatsCarrierSenseErrors_Type = Counter32
_PrvtStatHistDot3StatsCarrierSenseErrors_Object = MibTableColumn
prvtStatHistDot3StatsCarrierSenseErrors = _PrvtStatHistDot3StatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 44),
    _PrvtStatHistDot3StatsCarrierSenseErrors_Type()
)
prvtStatHistDot3StatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsCarrierSenseErrors.setStatus("current")
_PrvtStatHistDot3StatsFrameTooLongs_Type = Counter32
_PrvtStatHistDot3StatsFrameTooLongs_Object = MibTableColumn
prvtStatHistDot3StatsFrameTooLongs = _PrvtStatHistDot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 45),
    _PrvtStatHistDot3StatsFrameTooLongs_Type()
)
prvtStatHistDot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsFrameTooLongs.setStatus("current")
_PrvtStatHistDot3StatsInternalMacReceiveErrors_Type = Counter32
_PrvtStatHistDot3StatsInternalMacReceiveErrors_Object = MibTableColumn
prvtStatHistDot3StatsInternalMacReceiveErrors = _PrvtStatHistDot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 46),
    _PrvtStatHistDot3StatsInternalMacReceiveErrors_Type()
)
prvtStatHistDot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDot3StatsInternalMacReceiveErrors.setStatus("current")
_PrvtStatHistIfInDiscards_Type = Counter32
_PrvtStatHistIfInDiscards_Object = MibTableColumn
prvtStatHistIfInDiscards = _PrvtStatHistIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 47),
    _PrvtStatHistIfInDiscards_Type()
)
prvtStatHistIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfInDiscards.setStatus("current")
_PrvtStatHistIfInErrors_Type = Counter32
_PrvtStatHistIfInErrors_Object = MibTableColumn
prvtStatHistIfInErrors = _PrvtStatHistIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 48),
    _PrvtStatHistIfInErrors_Type()
)
prvtStatHistIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfInErrors.setStatus("current")
_PrvtStatHistIfInUnknownProtos_Type = Counter32
_PrvtStatHistIfInUnknownProtos_Object = MibTableColumn
prvtStatHistIfInUnknownProtos = _PrvtStatHistIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 49),
    _PrvtStatHistIfInUnknownProtos_Type()
)
prvtStatHistIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfInUnknownProtos.setStatus("current")
_PrvtStatHistIfOutDiscards_Type = Counter32
_PrvtStatHistIfOutDiscards_Object = MibTableColumn
prvtStatHistIfOutDiscards = _PrvtStatHistIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 50),
    _PrvtStatHistIfOutDiscards_Type()
)
prvtStatHistIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfOutDiscards.setStatus("current")
_PrvtStatHistIfOutErrors_Type = Counter32
_PrvtStatHistIfOutErrors_Object = MibTableColumn
prvtStatHistIfOutErrors = _PrvtStatHistIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 51),
    _PrvtStatHistIfOutErrors_Type()
)
prvtStatHistIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfOutErrors.setStatus("current")
_PrvtStatHistIfHCInOctets_Type = Counter64
_PrvtStatHistIfHCInOctets_Object = MibTableColumn
prvtStatHistIfHCInOctets = _PrvtStatHistIfHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 52),
    _PrvtStatHistIfHCInOctets_Type()
)
prvtStatHistIfHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfHCInOctets.setStatus("current")
_PrvtStatHistIfHCInUcastPkts_Type = Counter64
_PrvtStatHistIfHCInUcastPkts_Object = MibTableColumn
prvtStatHistIfHCInUcastPkts = _PrvtStatHistIfHCInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 53),
    _PrvtStatHistIfHCInUcastPkts_Type()
)
prvtStatHistIfHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfHCInUcastPkts.setStatus("current")
_PrvtStatHistIfHCInMulticastPkts_Type = Counter64
_PrvtStatHistIfHCInMulticastPkts_Object = MibTableColumn
prvtStatHistIfHCInMulticastPkts = _PrvtStatHistIfHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 54),
    _PrvtStatHistIfHCInMulticastPkts_Type()
)
prvtStatHistIfHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfHCInMulticastPkts.setStatus("current")
_PrvtStatHistIfHCInBroadcastPkts_Type = Counter64
_PrvtStatHistIfHCInBroadcastPkts_Object = MibTableColumn
prvtStatHistIfHCInBroadcastPkts = _PrvtStatHistIfHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 55),
    _PrvtStatHistIfHCInBroadcastPkts_Type()
)
prvtStatHistIfHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfHCInBroadcastPkts.setStatus("current")
_PrvtStatHistIfHCOutOctets_Type = Counter64
_PrvtStatHistIfHCOutOctets_Object = MibTableColumn
prvtStatHistIfHCOutOctets = _PrvtStatHistIfHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 56),
    _PrvtStatHistIfHCOutOctets_Type()
)
prvtStatHistIfHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfHCOutOctets.setStatus("current")
_PrvtStatHistIfHCOutUcastPkts_Type = Counter64
_PrvtStatHistIfHCOutUcastPkts_Object = MibTableColumn
prvtStatHistIfHCOutUcastPkts = _PrvtStatHistIfHCOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 57),
    _PrvtStatHistIfHCOutUcastPkts_Type()
)
prvtStatHistIfHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfHCOutUcastPkts.setStatus("current")
_PrvtStatHistIfHCOutMulticastPkts_Type = Counter64
_PrvtStatHistIfHCOutMulticastPkts_Object = MibTableColumn
prvtStatHistIfHCOutMulticastPkts = _PrvtStatHistIfHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 58),
    _PrvtStatHistIfHCOutMulticastPkts_Type()
)
prvtStatHistIfHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfHCOutMulticastPkts.setStatus("current")
_PrvtStatHistIfHCOutBroadcastPkts_Type = Counter64
_PrvtStatHistIfHCOutBroadcastPkts_Object = MibTableColumn
prvtStatHistIfHCOutBroadcastPkts = _PrvtStatHistIfHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 59),
    _PrvtStatHistIfHCOutBroadcastPkts_Type()
)
prvtStatHistIfHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistIfHCOutBroadcastPkts.setStatus("current")
_PrvtStatHistValidInterval_Type = TruthValue
_PrvtStatHistValidInterval_Object = MibTableColumn
prvtStatHistValidInterval = _PrvtStatHistValidInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 1, 2, 5, 1, 60),
    _PrvtStatHistValidInterval_Type()
)
prvtStatHistValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistValidInterval.setStatus("current")
_PrvtStatisticsHistoryConformance_ObjectIdentity = ObjectIdentity
prvtStatisticsHistoryConformance = _PrvtStatisticsHistoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 2)
)
_PrvtStatisticsHistoryCompliances_ObjectIdentity = ObjectIdentity
prvtStatisticsHistoryCompliances = _PrvtStatisticsHistoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 2, 1)
)
_PrvtStatisticsHistoryGroups_ObjectIdentity = ObjectIdentity
prvtStatisticsHistoryGroups = _PrvtStatisticsHistoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 2, 2)
)

# Managed Objects groups

prvtStatisticsHistoryIntCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 2, 2, 1)
)
prvtStatisticsHistoryIntCfgGroup.setObjects(
    ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIntAdminStatus")
)
if mibBuilder.loadTexts:
    prvtStatisticsHistoryIntCfgGroup.setStatus("current")

prvtStatisticsHistoryDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 2, 2, 2)
)
prvtStatisticsHistoryDataGroup.setObjects(
      *(("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast5secInPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast1minInPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast5minInPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast5secOutPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast1minOutPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast5minOutPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast5secInBps"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast1minInBps"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast5minInBps"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast5secOutBps"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast1minOutBps"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistLast5minOutBps"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsDropEvents"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsBroadcastPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsMulticastPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsCRCAlignErrors"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsUndersizePkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsOversizePkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsFragments"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsJabbers"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsCollisions"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsDroppedFrames"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityOverflowPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityOverflowOctets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityOctets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityPkts64Octets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityPkts65to127Octets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityPkts128to255Octets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityPkts256to511Octets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityPkts512to1023Octets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistEtherStatsHighCapacityPkts1024to1518Octets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsAlignmentErrors"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsFCSErrors"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsSingleCollisionFrames"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsMultipleCollisionFrames"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsSQETestErrors"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsDeferredTransmissions"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsLateCollisions"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsExcessiveCollisions"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsInternalMacTransmitErrors"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsCarrierSenseErrors"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsFrameTooLongs"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDot3StatsInternalMacReceiveErrors"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfInDiscards"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfInErrors"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfInUnknownProtos"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfOutDiscards"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfOutErrors"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfHCInOctets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfHCInUcastPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfHCInMulticastPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfHCInBroadcastPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfHCOutOctets"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfHCOutUcastPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfHCOutMulticastPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistIfHCOutBroadcastPkts"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistValidInterval"))
)
if mibBuilder.loadTexts:
    prvtStatisticsHistoryDataGroup.setStatus("current")

prvtStatisticsHistoryCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 2, 2, 3)
)
prvtStatisticsHistoryCfgGroup.setObjects(
      *(("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistAdminStatus"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistGetInterval"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistWriteInterval"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistPath"))
)
if mibBuilder.loadTexts:
    prvtStatisticsHistoryCfgGroup.setStatus("current")

prvtStatHistDailySnapshotDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 2, 2, 4)
)
prvtStatHistDailySnapshotDataGroup.setObjects(
      *(("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDailySnapshotAdminStatus"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDailySnapshotGetInterval"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDailySnapshotWriteInterval"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDailySnapshotPath"))
)
if mibBuilder.loadTexts:
    prvtStatHistDailySnapshotDataGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

prvtStatisticsHistoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 140, 2, 1, 1)
)
prvtStatisticsHistoryCompliance.setObjects(
      *(("PRVT-STATISTICSHISTORY-MIB", "prvtStatisticsHistoryIntCfgGroup"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatisticsHistoryDataGroup"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatisticsHistoryCfgGroup"),
        ("PRVT-STATISTICSHISTORY-MIB", "prvtStatHistDailySnapshotDataGroup"))
)
if mibBuilder.loadTexts:
    prvtStatisticsHistoryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-STATISTICSHISTORY-MIB",
    **{"prvtStatisticsHistoryMib": prvtStatisticsHistoryMib,
       "prvtStatisticsHistoryNotifications": prvtStatisticsHistoryNotifications,
       "prvtStatisticsHistoryObjects": prvtStatisticsHistoryObjects,
       "prvtStatisticsHistoryCfg": prvtStatisticsHistoryCfg,
       "prvtStatHistAdminStatus": prvtStatHistAdminStatus,
       "prvtStatHistGetInterval": prvtStatHistGetInterval,
       "prvtStatHistWriteInterval": prvtStatHistWriteInterval,
       "prvtStatHistPath": prvtStatHistPath,
       "prvtStatisticsHistoryIntCfgTable": prvtStatisticsHistoryIntCfgTable,
       "prvtStatisticsHistoryIntCfgEntry": prvtStatisticsHistoryIntCfgEntry,
       "prvtStatHistIntAdminStatus": prvtStatHistIntAdminStatus,
       "prvtStatHistDailySnapshotData": prvtStatHistDailySnapshotData,
       "prvtStatHistDailySnapshotAdminStatus": prvtStatHistDailySnapshotAdminStatus,
       "prvtStatHistDailySnapshotGetInterval": prvtStatHistDailySnapshotGetInterval,
       "prvtStatHistDailySnapshotWriteInterval": prvtStatHistDailySnapshotWriteInterval,
       "prvtStatHistDailySnapshotPath": prvtStatHistDailySnapshotPath,
       "prvtStatisticsHistoryDataTable": prvtStatisticsHistoryDataTable,
       "prvtStatisticsHistoryDataEntry": prvtStatisticsHistoryDataEntry,
       "prvtStatHistInterval": prvtStatHistInterval,
       "prvtStatHistLast5secInPkts": prvtStatHistLast5secInPkts,
       "prvtStatHistLast1minInPkts": prvtStatHistLast1minInPkts,
       "prvtStatHistLast5minInPkts": prvtStatHistLast5minInPkts,
       "prvtStatHistLast5secOutPkts": prvtStatHistLast5secOutPkts,
       "prvtStatHistLast1minOutPkts": prvtStatHistLast1minOutPkts,
       "prvtStatHistLast5minOutPkts": prvtStatHistLast5minOutPkts,
       "prvtStatHistLast5secInBps": prvtStatHistLast5secInBps,
       "prvtStatHistLast1minInBps": prvtStatHistLast1minInBps,
       "prvtStatHistLast5minInBps": prvtStatHistLast5minInBps,
       "prvtStatHistLast5secOutBps": prvtStatHistLast5secOutBps,
       "prvtStatHistLast1minOutBps": prvtStatHistLast1minOutBps,
       "prvtStatHistLast5minOutBps": prvtStatHistLast5minOutBps,
       "prvtStatHistEtherStatsDropEvents": prvtStatHistEtherStatsDropEvents,
       "prvtStatHistEtherStatsPkts": prvtStatHistEtherStatsPkts,
       "prvtStatHistEtherStatsBroadcastPkts": prvtStatHistEtherStatsBroadcastPkts,
       "prvtStatHistEtherStatsMulticastPkts": prvtStatHistEtherStatsMulticastPkts,
       "prvtStatHistEtherStatsCRCAlignErrors": prvtStatHistEtherStatsCRCAlignErrors,
       "prvtStatHistEtherStatsUndersizePkts": prvtStatHistEtherStatsUndersizePkts,
       "prvtStatHistEtherStatsOversizePkts": prvtStatHistEtherStatsOversizePkts,
       "prvtStatHistEtherStatsFragments": prvtStatHistEtherStatsFragments,
       "prvtStatHistEtherStatsJabbers": prvtStatHistEtherStatsJabbers,
       "prvtStatHistEtherStatsCollisions": prvtStatHistEtherStatsCollisions,
       "prvtStatHistEtherStatsDroppedFrames": prvtStatHistEtherStatsDroppedFrames,
       "prvtStatHistEtherStatsHighCapacityOverflowPkts": prvtStatHistEtherStatsHighCapacityOverflowPkts,
       "prvtStatHistEtherStatsHighCapacityOverflowOctets": prvtStatHistEtherStatsHighCapacityOverflowOctets,
       "prvtStatHistEtherStatsHighCapacityPkts": prvtStatHistEtherStatsHighCapacityPkts,
       "prvtStatHistEtherStatsHighCapacityOctets": prvtStatHistEtherStatsHighCapacityOctets,
       "prvtStatHistEtherStatsHighCapacityPkts64Octets": prvtStatHistEtherStatsHighCapacityPkts64Octets,
       "prvtStatHistEtherStatsHighCapacityPkts65to127Octets": prvtStatHistEtherStatsHighCapacityPkts65to127Octets,
       "prvtStatHistEtherStatsHighCapacityPkts128to255Octets": prvtStatHistEtherStatsHighCapacityPkts128to255Octets,
       "prvtStatHistEtherStatsHighCapacityPkts256to511Octets": prvtStatHistEtherStatsHighCapacityPkts256to511Octets,
       "prvtStatHistEtherStatsHighCapacityPkts512to1023Octets": prvtStatHistEtherStatsHighCapacityPkts512to1023Octets,
       "prvtStatHistEtherStatsHighCapacityPkts1024to1518Octets": prvtStatHistEtherStatsHighCapacityPkts1024to1518Octets,
       "prvtStatHistDot3StatsAlignmentErrors": prvtStatHistDot3StatsAlignmentErrors,
       "prvtStatHistDot3StatsFCSErrors": prvtStatHistDot3StatsFCSErrors,
       "prvtStatHistDot3StatsSingleCollisionFrames": prvtStatHistDot3StatsSingleCollisionFrames,
       "prvtStatHistDot3StatsMultipleCollisionFrames": prvtStatHistDot3StatsMultipleCollisionFrames,
       "prvtStatHistDot3StatsSQETestErrors": prvtStatHistDot3StatsSQETestErrors,
       "prvtStatHistDot3StatsDeferredTransmissions": prvtStatHistDot3StatsDeferredTransmissions,
       "prvtStatHistDot3StatsLateCollisions": prvtStatHistDot3StatsLateCollisions,
       "prvtStatHistDot3StatsExcessiveCollisions": prvtStatHistDot3StatsExcessiveCollisions,
       "prvtStatHistDot3StatsInternalMacTransmitErrors": prvtStatHistDot3StatsInternalMacTransmitErrors,
       "prvtStatHistDot3StatsCarrierSenseErrors": prvtStatHistDot3StatsCarrierSenseErrors,
       "prvtStatHistDot3StatsFrameTooLongs": prvtStatHistDot3StatsFrameTooLongs,
       "prvtStatHistDot3StatsInternalMacReceiveErrors": prvtStatHistDot3StatsInternalMacReceiveErrors,
       "prvtStatHistIfInDiscards": prvtStatHistIfInDiscards,
       "prvtStatHistIfInErrors": prvtStatHistIfInErrors,
       "prvtStatHistIfInUnknownProtos": prvtStatHistIfInUnknownProtos,
       "prvtStatHistIfOutDiscards": prvtStatHistIfOutDiscards,
       "prvtStatHistIfOutErrors": prvtStatHistIfOutErrors,
       "prvtStatHistIfHCInOctets": prvtStatHistIfHCInOctets,
       "prvtStatHistIfHCInUcastPkts": prvtStatHistIfHCInUcastPkts,
       "prvtStatHistIfHCInMulticastPkts": prvtStatHistIfHCInMulticastPkts,
       "prvtStatHistIfHCInBroadcastPkts": prvtStatHistIfHCInBroadcastPkts,
       "prvtStatHistIfHCOutOctets": prvtStatHistIfHCOutOctets,
       "prvtStatHistIfHCOutUcastPkts": prvtStatHistIfHCOutUcastPkts,
       "prvtStatHistIfHCOutMulticastPkts": prvtStatHistIfHCOutMulticastPkts,
       "prvtStatHistIfHCOutBroadcastPkts": prvtStatHistIfHCOutBroadcastPkts,
       "prvtStatHistValidInterval": prvtStatHistValidInterval,
       "prvtStatisticsHistoryConformance": prvtStatisticsHistoryConformance,
       "prvtStatisticsHistoryCompliances": prvtStatisticsHistoryCompliances,
       "prvtStatisticsHistoryCompliance": prvtStatisticsHistoryCompliance,
       "prvtStatisticsHistoryGroups": prvtStatisticsHistoryGroups,
       "prvtStatisticsHistoryIntCfgGroup": prvtStatisticsHistoryIntCfgGroup,
       "prvtStatisticsHistoryDataGroup": prvtStatisticsHistoryDataGroup,
       "prvtStatisticsHistoryCfgGroup": prvtStatisticsHistoryCfgGroup,
       "prvtStatHistDailySnapshotDataGroup": prvtStatHistDailySnapshotDataGroup}
)
