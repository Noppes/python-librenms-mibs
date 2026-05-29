# SNMP MIB module (PRVT-PORTS-AGGREGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-PORTS-AGGREGATION-MIB

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

(ifAdminStatus,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifIndex",
    "ifOperStatus")

(configL2IfacePort,
 configL2IfaceSlot,
 configL2IfaceUnit,
 switch) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "configL2IfacePort",
    "configL2IfaceSlot",
    "configL2IfaceUnit",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtPortsAggregationMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106)
)
if mibBuilder.loadTexts:
    prvtPortsAggregationMib.setRevisions(
        ("2008-09-20 00:00",
         "2005-02-16 00:00",
         "2004-10-29 00:00",
         "2003-05-06 00:00",
         "2002-12-24 00:00",
         "2002-11-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PortsAggregation_ObjectIdentity = ObjectIdentity
portsAggregation = _PortsAggregation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1)
)
_MaxAggregatorId_Type = Integer32
_MaxAggregatorId_Object = MibScalar
maxAggregatorId = _MaxAggregatorId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 1),
    _MaxAggregatorId_Type()
)
maxAggregatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAggregatorId.setStatus("current")


class _AggregationLacpSystemPriority_Type(Integer32):
    """Custom type aggregationLacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AggregationLacpSystemPriority_Type.__name__ = "Integer32"
_AggregationLacpSystemPriority_Object = MibScalar
aggregationLacpSystemPriority = _AggregationLacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 2),
    _AggregationLacpSystemPriority_Type()
)
aggregationLacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggregationLacpSystemPriority.setStatus("current")
_PortsAggregationTable_Object = MibTable
portsAggregationTable = _PortsAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3)
)
if mibBuilder.loadTexts:
    portsAggregationTable.setStatus("current")
_PortsAggregationEntry_Object = MibTableRow
portsAggregationEntry = _PortsAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1)
)
portsAggregationEntry.setIndexNames(
    (0, "PRVT-PORTS-AGGREGATION-MIB", "aggregatorId"),
)
if mibBuilder.loadTexts:
    portsAggregationEntry.setStatus("current")


class _AggregatorId_Type(Integer32):
    """Custom type aggregatorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AggregatorId_Type.__name__ = "Integer32"
_AggregatorId_Object = MibTableColumn
aggregatorId = _AggregatorId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 1),
    _AggregatorId_Type()
)
aggregatorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aggregatorId.setStatus("current")
_AggregatorIfIndex_Type = Integer32
_AggregatorIfIndex_Object = MibTableColumn
aggregatorIfIndex = _AggregatorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 2),
    _AggregatorIfIndex_Type()
)
aggregatorIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorIfIndex.setStatus("current")


class _AggregatorType_Type(Integer32):
    """Custom type aggregatorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("staticTrunk", 1),
          ("protocol-802-1ad", 2))
    )


_AggregatorType_Type.__name__ = "Integer32"
_AggregatorType_Object = MibTableColumn
aggregatorType = _AggregatorType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 3),
    _AggregatorType_Type()
)
aggregatorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorType.setStatus("current")
_AggregatorName_Type = DisplayString
_AggregatorName_Object = MibTableColumn
aggregatorName = _AggregatorName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 4),
    _AggregatorName_Type()
)
aggregatorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggregatorName.setStatus("current")
_AggregatorPortsMembers_Type = PortList
_AggregatorPortsMembers_Object = MibTableColumn
aggregatorPortsMembers = _AggregatorPortsMembers_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 5),
    _AggregatorPortsMembers_Type()
)
aggregatorPortsMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorPortsMembers.setStatus("current")
_AggregatorPortsActive_Type = PortList
_AggregatorPortsActive_Object = MibTableColumn
aggregatorPortsActive = _AggregatorPortsActive_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 6),
    _AggregatorPortsActive_Type()
)
aggregatorPortsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorPortsActive.setStatus("current")
_AggregatorL2DropEvents_Type = Counter32
_AggregatorL2DropEvents_Object = MibTableColumn
aggregatorL2DropEvents = _AggregatorL2DropEvents_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 7),
    _AggregatorL2DropEvents_Type()
)
aggregatorL2DropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2DropEvents.setStatus("current")
_AggregatorL2Octets_Type = Counter32
_AggregatorL2Octets_Object = MibTableColumn
aggregatorL2Octets = _AggregatorL2Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 8),
    _AggregatorL2Octets_Type()
)
aggregatorL2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Octets.setStatus("current")
_AggregatorL2Pkts_Type = Counter32
_AggregatorL2Pkts_Object = MibTableColumn
aggregatorL2Pkts = _AggregatorL2Pkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 9),
    _AggregatorL2Pkts_Type()
)
aggregatorL2Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Pkts.setStatus("current")
_AggregatorL2BroadcastPkts_Type = Counter32
_AggregatorL2BroadcastPkts_Object = MibTableColumn
aggregatorL2BroadcastPkts = _AggregatorL2BroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 10),
    _AggregatorL2BroadcastPkts_Type()
)
aggregatorL2BroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2BroadcastPkts.setStatus("current")
_AggregatorL2MulticastPkts_Type = Counter32
_AggregatorL2MulticastPkts_Object = MibTableColumn
aggregatorL2MulticastPkts = _AggregatorL2MulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 11),
    _AggregatorL2MulticastPkts_Type()
)
aggregatorL2MulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2MulticastPkts.setStatus("current")
_AggregatorL2CRCAlignErrors_Type = Counter32
_AggregatorL2CRCAlignErrors_Object = MibTableColumn
aggregatorL2CRCAlignErrors = _AggregatorL2CRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 12),
    _AggregatorL2CRCAlignErrors_Type()
)
aggregatorL2CRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2CRCAlignErrors.setStatus("current")
_AggregatorL2UndersizePkts_Type = Counter32
_AggregatorL2UndersizePkts_Object = MibTableColumn
aggregatorL2UndersizePkts = _AggregatorL2UndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 13),
    _AggregatorL2UndersizePkts_Type()
)
aggregatorL2UndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2UndersizePkts.setStatus("current")
_AggregatorL2OversizePkts_Type = Counter32
_AggregatorL2OversizePkts_Object = MibTableColumn
aggregatorL2OversizePkts = _AggregatorL2OversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 14),
    _AggregatorL2OversizePkts_Type()
)
aggregatorL2OversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2OversizePkts.setStatus("current")
_AggregatorL2Fragments_Type = Counter32
_AggregatorL2Fragments_Object = MibTableColumn
aggregatorL2Fragments = _AggregatorL2Fragments_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 15),
    _AggregatorL2Fragments_Type()
)
aggregatorL2Fragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Fragments.setStatus("current")
_AggregatorL2Jabbers_Type = Counter32
_AggregatorL2Jabbers_Object = MibTableColumn
aggregatorL2Jabbers = _AggregatorL2Jabbers_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 16),
    _AggregatorL2Jabbers_Type()
)
aggregatorL2Jabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Jabbers.setStatus("current")
_AggregatorL2Collisions_Type = Counter32
_AggregatorL2Collisions_Object = MibTableColumn
aggregatorL2Collisions = _AggregatorL2Collisions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 17),
    _AggregatorL2Collisions_Type()
)
aggregatorL2Collisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Collisions.setStatus("current")
_AggregatorL2Pkts64Octets_Type = Counter32
_AggregatorL2Pkts64Octets_Object = MibTableColumn
aggregatorL2Pkts64Octets = _AggregatorL2Pkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 18),
    _AggregatorL2Pkts64Octets_Type()
)
aggregatorL2Pkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Pkts64Octets.setStatus("current")
_AggregatorL2Pkts65to127Octets_Type = Counter32
_AggregatorL2Pkts65to127Octets_Object = MibTableColumn
aggregatorL2Pkts65to127Octets = _AggregatorL2Pkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 19),
    _AggregatorL2Pkts65to127Octets_Type()
)
aggregatorL2Pkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Pkts65to127Octets.setStatus("current")
_AggregatorL2Pkts128to255Octets_Type = Counter32
_AggregatorL2Pkts128to255Octets_Object = MibTableColumn
aggregatorL2Pkts128to255Octets = _AggregatorL2Pkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 20),
    _AggregatorL2Pkts128to255Octets_Type()
)
aggregatorL2Pkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Pkts128to255Octets.setStatus("current")
_AggregatorL2Pkts256to511Octets_Type = Counter32
_AggregatorL2Pkts256to511Octets_Object = MibTableColumn
aggregatorL2Pkts256to511Octets = _AggregatorL2Pkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 21),
    _AggregatorL2Pkts256to511Octets_Type()
)
aggregatorL2Pkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Pkts256to511Octets.setStatus("current")
_AggregatorL2Pkts512to1023Octets_Type = Counter32
_AggregatorL2Pkts512to1023Octets_Object = MibTableColumn
aggregatorL2Pkts512to1023Octets = _AggregatorL2Pkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 22),
    _AggregatorL2Pkts512to1023Octets_Type()
)
aggregatorL2Pkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Pkts512to1023Octets.setStatus("current")
_AggregatorL2Pkts1024to1518Octets_Type = Counter32
_AggregatorL2Pkts1024to1518Octets_Object = MibTableColumn
aggregatorL2Pkts1024to1518Octets = _AggregatorL2Pkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 3, 1, 23),
    _AggregatorL2Pkts1024to1518Octets_Type()
)
aggregatorL2Pkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregatorL2Pkts1024to1518Octets.setStatus("current")
_AggregationLacpSystemEnable_Type = TruthValue
_AggregationLacpSystemEnable_Object = MibScalar
aggregationLacpSystemEnable = _AggregationLacpSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 1, 4),
    _AggregationLacpSystemEnable_Type()
)
aggregationLacpSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggregationLacpSystemEnable.setStatus("current")
_PortsAggregationConfig_ObjectIdentity = ObjectIdentity
portsAggregationConfig = _PortsAggregationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 2)
)
_PortsAggregationConfigTable_Object = MibTable
portsAggregationConfigTable = _PortsAggregationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 2, 1)
)
if mibBuilder.loadTexts:
    portsAggregationConfigTable.setStatus("current")
_PortsAggregationConfigEntry_Object = MibTableRow
portsAggregationConfigEntry = _PortsAggregationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 2, 1, 1)
)
portsAggregationConfigEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "configL2IfaceUnit"),
    (0, "PRVT-SWITCH-MIB", "configL2IfaceSlot"),
    (0, "PRVT-SWITCH-MIB", "configL2IfacePort"),
)
if mibBuilder.loadTexts:
    portsAggregationConfigEntry.setStatus("current")
_StaticAggregationID_Type = Integer32
_StaticAggregationID_Object = MibTableColumn
staticAggregationID = _StaticAggregationID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 2, 1, 1, 1),
    _StaticAggregationID_Type()
)
staticAggregationID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticAggregationID.setStatus("current")
_DynamicAggregationID_Type = Integer32
_DynamicAggregationID_Object = MibTableColumn
dynamicAggregationID = _DynamicAggregationID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 2, 1, 1, 2),
    _DynamicAggregationID_Type()
)
dynamicAggregationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicAggregationID.setStatus("current")


class _AggregationType_Type(Integer32):
    """Custom type aggregationType based on Integer32"""
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
        *(("disable", 1),
          ("static", 2),
          ("protocol-802-1adAcive", 3),
          ("protocol-802-1adPassive", 4))
    )


_AggregationType_Type.__name__ = "Integer32"
_AggregationType_Object = MibTableColumn
aggregationType = _AggregationType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 2, 1, 1, 3),
    _AggregationType_Type()
)
aggregationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggregationType.setStatus("current")


class _AggregationLacpPortPriority_Type(Integer32):
    """Custom type aggregationLacpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AggregationLacpPortPriority_Type.__name__ = "Integer32"
_AggregationLacpPortPriority_Object = MibTableColumn
aggregationLacpPortPriority = _AggregationLacpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 2, 1, 1, 4),
    _AggregationLacpPortPriority_Type()
)
aggregationLacpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggregationLacpPortPriority.setStatus("current")


class _AggregationLacpPortKey_Type(Integer32):
    """Custom type aggregationLacpPortKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AggregationLacpPortKey_Type.__name__ = "Integer32"
_AggregationLacpPortKey_Object = MibTableColumn
aggregationLacpPortKey = _AggregationLacpPortKey_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 2, 1, 1, 5),
    _AggregationLacpPortKey_Type()
)
aggregationLacpPortKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggregationLacpPortKey.setStatus("current")
_PortsAggregationTraps_ObjectIdentity = ObjectIdentity
portsAggregationTraps = _PortsAggregationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 3)
)

# Managed Objects groups


# Notification objects

lagMemberLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 3, 1)
)
lagMemberLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    lagMemberLinkUp.setStatus(
        "current"
    )

lagMemberLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 3, 2)
)
lagMemberLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    lagMemberLinkDown.setStatus(
        "current"
    )

lagMemberAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 3, 3)
)
lagMemberAdd.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    lagMemberAdd.setStatus(
        "current"
    )

lagMemberRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 106, 3, 4)
)
lagMemberRemove.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    lagMemberRemove.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-PORTS-AGGREGATION-MIB",
    **{"prvtPortsAggregationMib": prvtPortsAggregationMib,
       "portsAggregation": portsAggregation,
       "maxAggregatorId": maxAggregatorId,
       "aggregationLacpSystemPriority": aggregationLacpSystemPriority,
       "portsAggregationTable": portsAggregationTable,
       "portsAggregationEntry": portsAggregationEntry,
       "aggregatorId": aggregatorId,
       "aggregatorIfIndex": aggregatorIfIndex,
       "aggregatorType": aggregatorType,
       "aggregatorName": aggregatorName,
       "aggregatorPortsMembers": aggregatorPortsMembers,
       "aggregatorPortsActive": aggregatorPortsActive,
       "aggregatorL2DropEvents": aggregatorL2DropEvents,
       "aggregatorL2Octets": aggregatorL2Octets,
       "aggregatorL2Pkts": aggregatorL2Pkts,
       "aggregatorL2BroadcastPkts": aggregatorL2BroadcastPkts,
       "aggregatorL2MulticastPkts": aggregatorL2MulticastPkts,
       "aggregatorL2CRCAlignErrors": aggregatorL2CRCAlignErrors,
       "aggregatorL2UndersizePkts": aggregatorL2UndersizePkts,
       "aggregatorL2OversizePkts": aggregatorL2OversizePkts,
       "aggregatorL2Fragments": aggregatorL2Fragments,
       "aggregatorL2Jabbers": aggregatorL2Jabbers,
       "aggregatorL2Collisions": aggregatorL2Collisions,
       "aggregatorL2Pkts64Octets": aggregatorL2Pkts64Octets,
       "aggregatorL2Pkts65to127Octets": aggregatorL2Pkts65to127Octets,
       "aggregatorL2Pkts128to255Octets": aggregatorL2Pkts128to255Octets,
       "aggregatorL2Pkts256to511Octets": aggregatorL2Pkts256to511Octets,
       "aggregatorL2Pkts512to1023Octets": aggregatorL2Pkts512to1023Octets,
       "aggregatorL2Pkts1024to1518Octets": aggregatorL2Pkts1024to1518Octets,
       "aggregationLacpSystemEnable": aggregationLacpSystemEnable,
       "portsAggregationConfig": portsAggregationConfig,
       "portsAggregationConfigTable": portsAggregationConfigTable,
       "portsAggregationConfigEntry": portsAggregationConfigEntry,
       "staticAggregationID": staticAggregationID,
       "dynamicAggregationID": dynamicAggregationID,
       "aggregationType": aggregationType,
       "aggregationLacpPortPriority": aggregationLacpPortPriority,
       "aggregationLacpPortKey": aggregationLacpPortKey,
       "portsAggregationTraps": portsAggregationTraps,
       "lagMemberLinkUp": lagMemberLinkUp,
       "lagMemberLinkDown": lagMemberLinkDown,
       "lagMemberAdd": lagMemberAdd,
       "lagMemberRemove": lagMemberRemove}
)
