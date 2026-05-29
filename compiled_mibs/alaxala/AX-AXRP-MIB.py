# SNMP MIB module (AX-AXRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-AXRP-MIB

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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

axAxrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200)
)
if mibBuilder.loadTexts:
    axAxrp.setRevisions(
        ("2016-11-17 00:00",
         "2016-10-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxAxrpNotifications_ObjectIdentity = ObjectIdentity
axAxrpNotifications = _AxAxrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 0)
)
_AxAxrpGroupTable_Object = MibTable
axAxrpGroupTable = _AxAxrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1)
)
if mibBuilder.loadTexts:
    axAxrpGroupTable.setStatus("current")
_AxAxrpGroupEntry_Object = MibTableRow
axAxrpGroupEntry = _AxAxrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1)
)
axAxrpGroupEntry.setIndexNames(
    (0, "AX-AXRP-MIB", "axAxrpGroupRingId"),
)
if mibBuilder.loadTexts:
    axAxrpGroupEntry.setStatus("current")
_AxAxrpGroupRingId_Type = Integer32
_AxAxrpGroupRingId_Object = MibTableColumn
axAxrpGroupRingId = _AxAxrpGroupRingId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 1),
    _AxAxrpGroupRingId_Type()
)
axAxrpGroupRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAxrpGroupRingId.setStatus("current")


class _AxAxrpGroupRowStatus_Type(Integer32):
    """Custom type axAxrpGroupRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("valid", 1)
    )


_AxAxrpGroupRowStatus_Type.__name__ = "Integer32"
_AxAxrpGroupRowStatus_Object = MibTableColumn
axAxrpGroupRowStatus = _AxAxrpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 2),
    _AxAxrpGroupRowStatus_Type()
)
axAxrpGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupRowStatus.setStatus("current")


class _AxAxrpGroupMode_Type(Integer32):
    """Custom type axAxrpGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-config", 1),
          ("master", 2),
          ("transit", 3))
    )


_AxAxrpGroupMode_Type.__name__ = "Integer32"
_AxAxrpGroupMode_Object = MibTableColumn
axAxrpGroupMode = _AxAxrpGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 3),
    _AxAxrpGroupMode_Type()
)
axAxrpGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupMode.setStatus("current")


class _AxAxrpGroupRingAttribute_Type(Integer32):
    """Custom type axAxrpGroupRingAttribute based on Integer32"""
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
        *(("no-config", 1),
          ("rift-ring", 2),
          ("rift-ring-edge1", 3),
          ("rift-ring-edge2", 4))
    )


_AxAxrpGroupRingAttribute_Type.__name__ = "Integer32"
_AxAxrpGroupRingAttribute_Object = MibTableColumn
axAxrpGroupRingAttribute = _AxAxrpGroupRingAttribute_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 4),
    _AxAxrpGroupRingAttribute_Type()
)
axAxrpGroupRingAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupRingAttribute.setStatus("current")


class _AxAxrpGroupMonitoringState_Type(Integer32):
    """Custom type axAxrpGroupMonitoringState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("disable", 2),
          ("fault-monitoring", 3),
          ("recovery-monitoring", 4),
          ("flush-monitoring", 5),
          ("not-operating", 6),
          ("preempt-delay", 8))
    )


_AxAxrpGroupMonitoringState_Type.__name__ = "Integer32"
_AxAxrpGroupMonitoringState_Object = MibTableColumn
axAxrpGroupMonitoringState = _AxAxrpGroupMonitoringState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 5),
    _AxAxrpGroupMonitoringState_Type()
)
axAxrpGroupMonitoringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupMonitoringState.setStatus("current")
_AxAxrpGroupRingport1_Type = InterfaceIndexOrZero
_AxAxrpGroupRingport1_Object = MibTableColumn
axAxrpGroupRingport1 = _AxAxrpGroupRingport1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 6),
    _AxAxrpGroupRingport1_Type()
)
axAxrpGroupRingport1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupRingport1.setStatus("current")


class _AxAxrpGroupRingport1Shared_Type(Integer32):
    """Custom type axAxrpGroupRingport1Shared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-ring-port", 0),
          ("no-config", 1),
          ("shared-edge", 2),
          ("shared", 3))
    )


_AxAxrpGroupRingport1Shared_Type.__name__ = "Integer32"
_AxAxrpGroupRingport1Shared_Object = MibTableColumn
axAxrpGroupRingport1Shared = _AxAxrpGroupRingport1Shared_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 7),
    _AxAxrpGroupRingport1Shared_Type()
)
axAxrpGroupRingport1Shared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupRingport1Shared.setStatus("current")
_AxAxrpGroupRingport2_Type = InterfaceIndexOrZero
_AxAxrpGroupRingport2_Object = MibTableColumn
axAxrpGroupRingport2 = _AxAxrpGroupRingport2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 8),
    _AxAxrpGroupRingport2_Type()
)
axAxrpGroupRingport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupRingport2.setStatus("current")


class _AxAxrpGroupRingport2Shared_Type(Integer32):
    """Custom type axAxrpGroupRingport2Shared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-ring-port", 0),
          ("no-config", 1),
          ("shared-edge", 2),
          ("shared", 3))
    )


_AxAxrpGroupRingport2Shared_Type.__name__ = "Integer32"
_AxAxrpGroupRingport2Shared_Object = MibTableColumn
axAxrpGroupRingport2Shared = _AxAxrpGroupRingport2Shared_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 9),
    _AxAxrpGroupRingport2Shared_Type()
)
axAxrpGroupRingport2Shared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupRingport2Shared.setStatus("current")
_AxAxrpGroupTransitionToFaultCounts_Type = Counter64
_AxAxrpGroupTransitionToFaultCounts_Object = MibTableColumn
axAxrpGroupTransitionToFaultCounts = _AxAxrpGroupTransitionToFaultCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 10),
    _AxAxrpGroupTransitionToFaultCounts_Type()
)
axAxrpGroupTransitionToFaultCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupTransitionToFaultCounts.setStatus("current")
_AxAxrpGroupTransitionToNormalCounts_Type = Counter64
_AxAxrpGroupTransitionToNormalCounts_Object = MibTableColumn
axAxrpGroupTransitionToNormalCounts = _AxAxrpGroupTransitionToNormalCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 11),
    _AxAxrpGroupTransitionToNormalCounts_Type()
)
axAxrpGroupTransitionToNormalCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupTransitionToNormalCounts.setStatus("current")
_AxAxrpGroupLastTransitionTime_Type = TimeStamp
_AxAxrpGroupLastTransitionTime_Object = MibTableColumn
axAxrpGroupLastTransitionTime = _AxAxrpGroupLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1, 1, 12),
    _AxAxrpGroupLastTransitionTime_Type()
)
axAxrpGroupLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpGroupLastTransitionTime.setStatus("current")
_AxAxrpVlanGroupTable_Object = MibTable
axAxrpVlanGroupTable = _AxAxrpVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2)
)
if mibBuilder.loadTexts:
    axAxrpVlanGroupTable.setStatus("current")
_AxAxrpVlanGroupEntry_Object = MibTableRow
axAxrpVlanGroupEntry = _AxAxrpVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2, 1)
)
axAxrpVlanGroupEntry.setIndexNames(
    (0, "AX-AXRP-MIB", "axAxrpVlanGroupRingId"),
    (0, "AX-AXRP-MIB", "axAxrpVlanGroupId"),
)
if mibBuilder.loadTexts:
    axAxrpVlanGroupEntry.setStatus("current")
_AxAxrpVlanGroupRingId_Type = Integer32
_AxAxrpVlanGroupRingId_Object = MibTableColumn
axAxrpVlanGroupRingId = _AxAxrpVlanGroupRingId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2, 1, 1),
    _AxAxrpVlanGroupRingId_Type()
)
axAxrpVlanGroupRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAxrpVlanGroupRingId.setStatus("current")
_AxAxrpVlanGroupId_Type = Integer32
_AxAxrpVlanGroupId_Object = MibTableColumn
axAxrpVlanGroupId = _AxAxrpVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2, 1, 2),
    _AxAxrpVlanGroupId_Type()
)
axAxrpVlanGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAxrpVlanGroupId.setStatus("current")
_AxAxrpVlanGroupRingport1_Type = Integer32
_AxAxrpVlanGroupRingport1_Object = MibTableColumn
axAxrpVlanGroupRingport1 = _AxAxrpVlanGroupRingport1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2, 1, 3),
    _AxAxrpVlanGroupRingport1_Type()
)
axAxrpVlanGroupRingport1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpVlanGroupRingport1.setStatus("current")


class _AxAxrpVlanGroupRingport1Role_Type(Integer32):
    """Custom type axAxrpVlanGroupRingport1Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("other", 3))
    )


_AxAxrpVlanGroupRingport1Role_Type.__name__ = "Integer32"
_AxAxrpVlanGroupRingport1Role_Object = MibTableColumn
axAxrpVlanGroupRingport1Role = _AxAxrpVlanGroupRingport1Role_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2, 1, 4),
    _AxAxrpVlanGroupRingport1Role_Type()
)
axAxrpVlanGroupRingport1Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpVlanGroupRingport1Role.setStatus("current")


class _AxAxrpVlanGroupRingport1OperState_Type(Integer32):
    """Custom type axAxrpVlanGroupRingport1OperState based on Integer32"""
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
        *(("forwarding", 1),
          ("blocking", 2),
          ("other", 3),
          ("down", 4))
    )


_AxAxrpVlanGroupRingport1OperState_Type.__name__ = "Integer32"
_AxAxrpVlanGroupRingport1OperState_Object = MibTableColumn
axAxrpVlanGroupRingport1OperState = _AxAxrpVlanGroupRingport1OperState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2, 1, 5),
    _AxAxrpVlanGroupRingport1OperState_Type()
)
axAxrpVlanGroupRingport1OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpVlanGroupRingport1OperState.setStatus("current")
_AxAxrpVlanGroupRingport2_Type = Integer32
_AxAxrpVlanGroupRingport2_Object = MibTableColumn
axAxrpVlanGroupRingport2 = _AxAxrpVlanGroupRingport2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2, 1, 6),
    _AxAxrpVlanGroupRingport2_Type()
)
axAxrpVlanGroupRingport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpVlanGroupRingport2.setStatus("current")


class _AxAxrpVlanGroupRingport2Role_Type(Integer32):
    """Custom type axAxrpVlanGroupRingport2Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("other", 3))
    )


_AxAxrpVlanGroupRingport2Role_Type.__name__ = "Integer32"
_AxAxrpVlanGroupRingport2Role_Object = MibTableColumn
axAxrpVlanGroupRingport2Role = _AxAxrpVlanGroupRingport2Role_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2, 1, 7),
    _AxAxrpVlanGroupRingport2Role_Type()
)
axAxrpVlanGroupRingport2Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpVlanGroupRingport2Role.setStatus("current")


class _AxAxrpVlanGroupRingport2OperState_Type(Integer32):
    """Custom type axAxrpVlanGroupRingport2OperState based on Integer32"""
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
        *(("forwarding", 1),
          ("blocking", 2),
          ("other", 3),
          ("down", 4))
    )


_AxAxrpVlanGroupRingport2OperState_Type.__name__ = "Integer32"
_AxAxrpVlanGroupRingport2OperState_Object = MibTableColumn
axAxrpVlanGroupRingport2OperState = _AxAxrpVlanGroupRingport2OperState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 2, 1, 8),
    _AxAxrpVlanGroupRingport2OperState_Type()
)
axAxrpVlanGroupRingport2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAxrpVlanGroupRingport2OperState.setStatus("current")
_AxAxrpConformance_ObjectIdentity = ObjectIdentity
axAxrpConformance = _AxAxrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1000)
)
_AxAxrpCompliances_ObjectIdentity = ObjectIdentity
axAxrpCompliances = _AxAxrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1000, 1)
)
_AxAxrpGroups_ObjectIdentity = ObjectIdentity
axAxrpGroups = _AxAxrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1000, 2)
)

# Managed Objects groups

axAxrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1000, 2, 1)
)
axAxrpGroup.setObjects(
      *(("AX-AXRP-MIB", "axAxrpGroupRowStatus"),
        ("AX-AXRP-MIB", "axAxrpGroupMode"),
        ("AX-AXRP-MIB", "axAxrpGroupRingAttribute"),
        ("AX-AXRP-MIB", "axAxrpGroupMonitoringState"),
        ("AX-AXRP-MIB", "axAxrpGroupRingport1"),
        ("AX-AXRP-MIB", "axAxrpGroupRingport1Shared"),
        ("AX-AXRP-MIB", "axAxrpGroupRingport2"),
        ("AX-AXRP-MIB", "axAxrpGroupRingport2Shared"),
        ("AX-AXRP-MIB", "axAxrpGroupTransitionToFaultCounts"),
        ("AX-AXRP-MIB", "axAxrpGroupTransitionToNormalCounts"),
        ("AX-AXRP-MIB", "axAxrpGroupLastTransitionTime"),
        ("AX-AXRP-MIB", "axAxrpVlanGroupRingport1"),
        ("AX-AXRP-MIB", "axAxrpVlanGroupRingport1Role"),
        ("AX-AXRP-MIB", "axAxrpVlanGroupRingport1OperState"),
        ("AX-AXRP-MIB", "axAxrpVlanGroupRingport2"),
        ("AX-AXRP-MIB", "axAxrpVlanGroupRingport2Role"),
        ("AX-AXRP-MIB", "axAxrpVlanGroupRingport2OperState"))
)
if mibBuilder.loadTexts:
    axAxrpGroup.setStatus("current")


# Notification objects

axAxrpStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 0, 1)
)
axAxrpStateTransitionTrap.setObjects(
      *(("AX-AXRP-MIB", "axAxrpGroupRingId"),
        ("AX-AXRP-MIB", "axAxrpGroupMode"),
        ("AX-AXRP-MIB", "axAxrpGroupRingAttribute"),
        ("AX-AXRP-MIB", "axAxrpGroupMonitoringState"))
)
if mibBuilder.loadTexts:
    axAxrpStateTransitionTrap.setStatus(
        "current"
    )


# Notifications groups

axAxrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1000, 2, 10)
)
axAxrpNotificationGroup.setObjects(
    ("AX-AXRP-MIB", "axAxrpStateTransitionTrap")
)
if mibBuilder.loadTexts:
    axAxrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axAxrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 200, 1000, 1, 1)
)
axAxrpCompliance.setObjects(
      *(("AX-AXRP-MIB", "axAxrpGroup"),
        ("AX-AXRP-MIB", "axAxrpNotificationGroup"))
)
if mibBuilder.loadTexts:
    axAxrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-AXRP-MIB",
    **{"axAxrp": axAxrp,
       "axAxrpNotifications": axAxrpNotifications,
       "axAxrpStateTransitionTrap": axAxrpStateTransitionTrap,
       "axAxrpGroupTable": axAxrpGroupTable,
       "axAxrpGroupEntry": axAxrpGroupEntry,
       "axAxrpGroupRingId": axAxrpGroupRingId,
       "axAxrpGroupRowStatus": axAxrpGroupRowStatus,
       "axAxrpGroupMode": axAxrpGroupMode,
       "axAxrpGroupRingAttribute": axAxrpGroupRingAttribute,
       "axAxrpGroupMonitoringState": axAxrpGroupMonitoringState,
       "axAxrpGroupRingport1": axAxrpGroupRingport1,
       "axAxrpGroupRingport1Shared": axAxrpGroupRingport1Shared,
       "axAxrpGroupRingport2": axAxrpGroupRingport2,
       "axAxrpGroupRingport2Shared": axAxrpGroupRingport2Shared,
       "axAxrpGroupTransitionToFaultCounts": axAxrpGroupTransitionToFaultCounts,
       "axAxrpGroupTransitionToNormalCounts": axAxrpGroupTransitionToNormalCounts,
       "axAxrpGroupLastTransitionTime": axAxrpGroupLastTransitionTime,
       "axAxrpVlanGroupTable": axAxrpVlanGroupTable,
       "axAxrpVlanGroupEntry": axAxrpVlanGroupEntry,
       "axAxrpVlanGroupRingId": axAxrpVlanGroupRingId,
       "axAxrpVlanGroupId": axAxrpVlanGroupId,
       "axAxrpVlanGroupRingport1": axAxrpVlanGroupRingport1,
       "axAxrpVlanGroupRingport1Role": axAxrpVlanGroupRingport1Role,
       "axAxrpVlanGroupRingport1OperState": axAxrpVlanGroupRingport1OperState,
       "axAxrpVlanGroupRingport2": axAxrpVlanGroupRingport2,
       "axAxrpVlanGroupRingport2Role": axAxrpVlanGroupRingport2Role,
       "axAxrpVlanGroupRingport2OperState": axAxrpVlanGroupRingport2OperState,
       "axAxrpConformance": axAxrpConformance,
       "axAxrpCompliances": axAxrpCompliances,
       "axAxrpCompliance": axAxrpCompliance,
       "axAxrpGroups": axAxrpGroups,
       "axAxrpGroup": axAxrpGroup,
       "axAxrpNotificationGroup": axAxrpNotificationGroup}
)
