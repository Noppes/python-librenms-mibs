# SNMP MIB module (PRVT-EGRESS-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-EGRESS-COUNTERS-MIB

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

prvtEgressCounterMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160)
)
if mibBuilder.loadTexts:
    prvtEgressCounterMib.setRevisions(
        ("2010-05-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtEgressCntNotifications_ObjectIdentity = ObjectIdentity
prvtEgressCntNotifications = _PrvtEgressCntNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 0)
)
_PrvtEgressCntObjects_ObjectIdentity = ObjectIdentity
prvtEgressCntObjects = _PrvtEgressCntObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1)
)
_PrvtEgressCntCounterSetTable_Object = MibTable
prvtEgressCntCounterSetTable = _PrvtEgressCntCounterSetTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1)
)
if mibBuilder.loadTexts:
    prvtEgressCntCounterSetTable.setStatus("current")
_PrvtEgressCntCounterSetEntry_Object = MibTableRow
prvtEgressCntCounterSetEntry = _PrvtEgressCntCounterSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1)
)
prvtEgressCntCounterSetEntry.setIndexNames(
    (0, "PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCounterSetID"),
)
if mibBuilder.loadTexts:
    prvtEgressCntCounterSetEntry.setStatus("current")


class _PrvtEgressCntCounterSetID_Type(Unsigned32):
    """Custom type prvtEgressCntCounterSetID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PrvtEgressCntCounterSetID_Type.__name__ = "Unsigned32"
_PrvtEgressCntCounterSetID_Object = MibTableColumn
prvtEgressCntCounterSetID = _PrvtEgressCntCounterSetID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 1),
    _PrvtEgressCntCounterSetID_Type()
)
prvtEgressCntCounterSetID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtEgressCntCounterSetID.setStatus("current")
_PrvtEgressCntAllPriorities_Type = TruthValue
_PrvtEgressCntAllPriorities_Object = MibTableColumn
prvtEgressCntAllPriorities = _PrvtEgressCntAllPriorities_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 2),
    _PrvtEgressCntAllPriorities_Type()
)
prvtEgressCntAllPriorities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntAllPriorities.setStatus("current")


class _PrvtEgressCntPriority_Type(Unsigned32):
    """Custom type prvtEgressCntPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtEgressCntPriority_Type.__name__ = "Unsigned32"
_PrvtEgressCntPriority_Object = MibTableColumn
prvtEgressCntPriority = _PrvtEgressCntPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 3),
    _PrvtEgressCntPriority_Type()
)
prvtEgressCntPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEgressCntPriority.setStatus("current")
_PrvtEgressCntAllDropLevels_Type = TruthValue
_PrvtEgressCntAllDropLevels_Object = MibTableColumn
prvtEgressCntAllDropLevels = _PrvtEgressCntAllDropLevels_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 4),
    _PrvtEgressCntAllDropLevels_Type()
)
prvtEgressCntAllDropLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntAllDropLevels.setStatus("current")


class _PrvtEgressCntDropLevelMode_Type(Integer32):
    """Custom type prvtEgressCntDropLevelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_PrvtEgressCntDropLevelMode_Type.__name__ = "Integer32"
_PrvtEgressCntDropLevelMode_Object = MibTableColumn
prvtEgressCntDropLevelMode = _PrvtEgressCntDropLevelMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 5),
    _PrvtEgressCntDropLevelMode_Type()
)
prvtEgressCntDropLevelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEgressCntDropLevelMode.setStatus("current")
_PrvtEgressCntAllVlans_Type = TruthValue
_PrvtEgressCntAllVlans_Object = MibTableColumn
prvtEgressCntAllVlans = _PrvtEgressCntAllVlans_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 6),
    _PrvtEgressCntAllVlans_Type()
)
prvtEgressCntAllVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntAllVlans.setStatus("current")


class _PrvtEgressCntVlan_Type(Unsigned32):
    """Custom type prvtEgressCntVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PrvtEgressCntVlan_Type.__name__ = "Unsigned32"
_PrvtEgressCntVlan_Object = MibTableColumn
prvtEgressCntVlan = _PrvtEgressCntVlan_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 7),
    _PrvtEgressCntVlan_Type()
)
prvtEgressCntVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEgressCntVlan.setStatus("current")
_PrvtEgressCntAllInterfaces_Type = TruthValue
_PrvtEgressCntAllInterfaces_Object = MibTableColumn
prvtEgressCntAllInterfaces = _PrvtEgressCntAllInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 8),
    _PrvtEgressCntAllInterfaces_Type()
)
prvtEgressCntAllInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntAllInterfaces.setStatus("current")
_PrvtEgressCntInterfaces_Type = InterfaceIndex
_PrvtEgressCntInterfaces_Object = MibTableColumn
prvtEgressCntInterfaces = _PrvtEgressCntInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 9),
    _PrvtEgressCntInterfaces_Type()
)
prvtEgressCntInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEgressCntInterfaces.setStatus("current")


class _PrvtEgressCntPort_Type(Integer32):
    """Custom type prvtEgressCntPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("set", 1))
    )


_PrvtEgressCntPort_Type.__name__ = "Integer32"
_PrvtEgressCntPort_Object = MibTableColumn
prvtEgressCntPort = _PrvtEgressCntPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 10),
    _PrvtEgressCntPort_Type()
)
prvtEgressCntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEgressCntPort.setStatus("current")


class _PrvtEgressCntClearCounterSet_Type(Integer32):
    """Custom type prvtEgressCntClearCounterSet based on Integer32"""
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


_PrvtEgressCntClearCounterSet_Type.__name__ = "Integer32"
_PrvtEgressCntClearCounterSet_Object = MibTableColumn
prvtEgressCntClearCounterSet = _PrvtEgressCntClearCounterSet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 11),
    _PrvtEgressCntClearCounterSet_Type()
)
prvtEgressCntClearCounterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEgressCntClearCounterSet.setStatus("current")
_PrvtEgressCntCounterSetRowStatus_Type = RowStatus
_PrvtEgressCntCounterSetRowStatus_Object = MibTableColumn
prvtEgressCntCounterSetRowStatus = _PrvtEgressCntCounterSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 12),
    _PrvtEgressCntCounterSetRowStatus_Type()
)
prvtEgressCntCounterSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEgressCntCounterSetRowStatus.setStatus("current")
_PrvtEgressCntCountersTable_Object = MibTable
prvtEgressCntCountersTable = _PrvtEgressCntCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2)
)
if mibBuilder.loadTexts:
    prvtEgressCntCountersTable.setStatus("current")
_PrvtEgressCntCountersEntry_Object = MibTableRow
prvtEgressCntCountersEntry = _PrvtEgressCntCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1)
)
prvtEgressCntCountersEntry.setIndexNames(
    (0, "PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCounterSetID"),
)
if mibBuilder.loadTexts:
    prvtEgressCntCountersEntry.setStatus("current")
_PrvtEgressCntOutBcFrames_Type = Unsigned32
_PrvtEgressCntOutBcFrames_Object = MibTableColumn
prvtEgressCntOutBcFrames = _PrvtEgressCntOutBcFrames_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 1),
    _PrvtEgressCntOutBcFrames_Type()
)
prvtEgressCntOutBcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntOutBcFrames.setStatus("current")
_PrvtEgressCntOutNUcFrames_Type = Unsigned32
_PrvtEgressCntOutNUcFrames_Object = MibTableColumn
prvtEgressCntOutNUcFrames = _PrvtEgressCntOutNUcFrames_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 2),
    _PrvtEgressCntOutNUcFrames_Type()
)
prvtEgressCntOutNUcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntOutNUcFrames.setStatus("current")
_PrvtEgressCntOutUcFrames_Type = Unsigned32
_PrvtEgressCntOutUcFrames_Object = MibTableColumn
prvtEgressCntOutUcFrames = _PrvtEgressCntOutUcFrames_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 3),
    _PrvtEgressCntOutUcFrames_Type()
)
prvtEgressCntOutUcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntOutUcFrames.setStatus("current")
_PrvtEgressCntEgrFilterDisc_Type = Unsigned32
_PrvtEgressCntEgrFilterDisc_Object = MibTableColumn
prvtEgressCntEgrFilterDisc = _PrvtEgressCntEgrFilterDisc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 4),
    _PrvtEgressCntEgrFilterDisc_Type()
)
prvtEgressCntEgrFilterDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntEgrFilterDisc.setStatus("current")
_PrvtEgressCntTxqFilterDisc_Type = Unsigned32
_PrvtEgressCntTxqFilterDisc_Object = MibTableColumn
prvtEgressCntTxqFilterDisc = _PrvtEgressCntTxqFilterDisc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 5),
    _PrvtEgressCntTxqFilterDisc_Type()
)
prvtEgressCntTxqFilterDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntTxqFilterDisc.setStatus("current")
_PrvtEgressCntOutCtrlFrames_Type = Unsigned32
_PrvtEgressCntOutCtrlFrames_Object = MibTableColumn
prvtEgressCntOutCtrlFrames = _PrvtEgressCntOutCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 6),
    _PrvtEgressCntOutCtrlFrames_Type()
)
prvtEgressCntOutCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntOutCtrlFrames.setStatus("current")
_PrvtEgressCntEgrFrwFilterDisc_Type = Unsigned32
_PrvtEgressCntEgrFrwFilterDisc_Object = MibTableColumn
prvtEgressCntEgrFrwFilterDisc = _PrvtEgressCntEgrFrwFilterDisc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 7),
    _PrvtEgressCntEgrFrwFilterDisc_Type()
)
prvtEgressCntEgrFrwFilterDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntEgrFrwFilterDisc.setStatus("current")


class _PrvtEgressCntClearCounters_Type(Integer32):
    """Custom type prvtEgressCntClearCounters based on Integer32"""
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


_PrvtEgressCntClearCounters_Type.__name__ = "Integer32"
_PrvtEgressCntClearCounters_Object = MibTableColumn
prvtEgressCntClearCounters = _PrvtEgressCntClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 8),
    _PrvtEgressCntClearCounters_Type()
)
prvtEgressCntClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEgressCntClearCounters.setStatus("current")
_PrvtEgressCntQosCountersTable_Object = MibTable
prvtEgressCntQosCountersTable = _PrvtEgressCntQosCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3)
)
if mibBuilder.loadTexts:
    prvtEgressCntQosCountersTable.setStatus("current")
_PrvtEgressCntQosCountersEntry_Object = MibTableRow
prvtEgressCntQosCountersEntry = _PrvtEgressCntQosCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3, 1)
)
prvtEgressCntQosCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtEgressCntQosCountersEntry.setStatus("current")
_PrvtEgressCntQosYellowPacketCounters_Type = Unsigned32
_PrvtEgressCntQosYellowPacketCounters_Object = MibTableColumn
prvtEgressCntQosYellowPacketCounters = _PrvtEgressCntQosYellowPacketCounters_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3, 1, 1),
    _PrvtEgressCntQosYellowPacketCounters_Type()
)
prvtEgressCntQosYellowPacketCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntQosYellowPacketCounters.setStatus("current")
_PrvtEgressCntQosRedPacketCounters_Type = Unsigned32
_PrvtEgressCntQosRedPacketCounters_Object = MibTableColumn
prvtEgressCntQosRedPacketCounters = _PrvtEgressCntQosRedPacketCounters_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3, 1, 2),
    _PrvtEgressCntQosRedPacketCounters_Type()
)
prvtEgressCntQosRedPacketCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntQosRedPacketCounters.setStatus("current")
_PrvtEgressCntQosMaximumRateReached_Type = TruthValue
_PrvtEgressCntQosMaximumRateReached_Object = MibTableColumn
prvtEgressCntQosMaximumRateReached = _PrvtEgressCntQosMaximumRateReached_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3, 1, 3),
    _PrvtEgressCntQosMaximumRateReached_Type()
)
prvtEgressCntQosMaximumRateReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEgressCntQosMaximumRateReached.setStatus("current")
_PrvtEgressCntConformance_ObjectIdentity = ObjectIdentity
prvtEgressCntConformance = _PrvtEgressCntConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2)
)
_PrvtEgressCntCompliances_ObjectIdentity = ObjectIdentity
prvtEgressCntCompliances = _PrvtEgressCntCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 1)
)
_PrvtEgressCntGroups_ObjectIdentity = ObjectIdentity
prvtEgressCntGroups = _PrvtEgressCntGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 2)
)

# Managed Objects groups

prvtEgressCntCounterSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 2, 1)
)
prvtEgressCntCounterSetGroup.setObjects(
      *(("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntAllPriorities"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntPriority"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntAllDropLevels"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntDropLevelMode"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntAllVlans"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntVlan"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntAllInterfaces"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntInterfaces"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntPort"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntClearCounterSet"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCounterSetRowStatus"))
)
if mibBuilder.loadTexts:
    prvtEgressCntCounterSetGroup.setStatus("current")

prvtEgressCntCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 2, 2)
)
prvtEgressCntCountersGroup.setObjects(
      *(("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntOutBcFrames"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntOutNUcFrames"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntOutUcFrames"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntEgrFilterDisc"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntTxqFilterDisc"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntOutCtrlFrames"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntEgrFrwFilterDisc"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntClearCounters"))
)
if mibBuilder.loadTexts:
    prvtEgressCntCountersGroup.setStatus("current")

prvtEgressCntQosCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 2, 3)
)
prvtEgressCntQosCountersGroup.setObjects(
      *(("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntQosYellowPacketCounters"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntQosRedPacketCounters"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntQosMaximumRateReached"))
)
if mibBuilder.loadTexts:
    prvtEgressCntQosCountersGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

prvtEgressCntCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 1, 1)
)
prvtEgressCntCompliance.setObjects(
      *(("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCounterSetGroup"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCountersGroup"),
        ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntQosCountersGroup"))
)
if mibBuilder.loadTexts:
    prvtEgressCntCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-EGRESS-COUNTERS-MIB",
    **{"prvtEgressCounterMib": prvtEgressCounterMib,
       "prvtEgressCntNotifications": prvtEgressCntNotifications,
       "prvtEgressCntObjects": prvtEgressCntObjects,
       "prvtEgressCntCounterSetTable": prvtEgressCntCounterSetTable,
       "prvtEgressCntCounterSetEntry": prvtEgressCntCounterSetEntry,
       "prvtEgressCntCounterSetID": prvtEgressCntCounterSetID,
       "prvtEgressCntAllPriorities": prvtEgressCntAllPriorities,
       "prvtEgressCntPriority": prvtEgressCntPriority,
       "prvtEgressCntAllDropLevels": prvtEgressCntAllDropLevels,
       "prvtEgressCntDropLevelMode": prvtEgressCntDropLevelMode,
       "prvtEgressCntAllVlans": prvtEgressCntAllVlans,
       "prvtEgressCntVlan": prvtEgressCntVlan,
       "prvtEgressCntAllInterfaces": prvtEgressCntAllInterfaces,
       "prvtEgressCntInterfaces": prvtEgressCntInterfaces,
       "prvtEgressCntPort": prvtEgressCntPort,
       "prvtEgressCntClearCounterSet": prvtEgressCntClearCounterSet,
       "prvtEgressCntCounterSetRowStatus": prvtEgressCntCounterSetRowStatus,
       "prvtEgressCntCountersTable": prvtEgressCntCountersTable,
       "prvtEgressCntCountersEntry": prvtEgressCntCountersEntry,
       "prvtEgressCntOutBcFrames": prvtEgressCntOutBcFrames,
       "prvtEgressCntOutNUcFrames": prvtEgressCntOutNUcFrames,
       "prvtEgressCntOutUcFrames": prvtEgressCntOutUcFrames,
       "prvtEgressCntEgrFilterDisc": prvtEgressCntEgrFilterDisc,
       "prvtEgressCntTxqFilterDisc": prvtEgressCntTxqFilterDisc,
       "prvtEgressCntOutCtrlFrames": prvtEgressCntOutCtrlFrames,
       "prvtEgressCntEgrFrwFilterDisc": prvtEgressCntEgrFrwFilterDisc,
       "prvtEgressCntClearCounters": prvtEgressCntClearCounters,
       "prvtEgressCntQosCountersTable": prvtEgressCntQosCountersTable,
       "prvtEgressCntQosCountersEntry": prvtEgressCntQosCountersEntry,
       "prvtEgressCntQosYellowPacketCounters": prvtEgressCntQosYellowPacketCounters,
       "prvtEgressCntQosRedPacketCounters": prvtEgressCntQosRedPacketCounters,
       "prvtEgressCntQosMaximumRateReached": prvtEgressCntQosMaximumRateReached,
       "prvtEgressCntConformance": prvtEgressCntConformance,
       "prvtEgressCntCompliances": prvtEgressCntCompliances,
       "prvtEgressCntCompliance": prvtEgressCntCompliance,
       "prvtEgressCntGroups": prvtEgressCntGroups,
       "prvtEgressCntCounterSetGroup": prvtEgressCntCounterSetGroup,
       "prvtEgressCntCountersGroup": prvtEgressCntCountersGroup,
       "prvtEgressCntQosCountersGroup": prvtEgressCntQosCountersGroup}
)
