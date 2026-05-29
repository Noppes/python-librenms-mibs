# SNMP MIB module (PRVT-NETWORK-LOOPBACK-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-NETWORK-LOOPBACK-TEST-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(accessListControlListGroup,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-ACCESS-LIST-MIB",
    "accessListControlListGroup")

(ipSwitch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "ipSwitch")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

prvtNetworkLoopbackTestMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7)
)
if mibBuilder.loadTexts:
    prvtNetworkLoopbackTestMib.setRevisions(
        ("2010-08-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtNetworkLoopbackTestNotifications_ObjectIdentity = ObjectIdentity
prvtNetworkLoopbackTestNotifications = _PrvtNetworkLoopbackTestNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 0)
)
_PrvtNetworkLoopbackTestObjects_ObjectIdentity = ObjectIdentity
prvtNetworkLoopbackTestObjects = _PrvtNetworkLoopbackTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1)
)
_PrvtNetworkLoopbackTestTable_Object = MibTable
prvtNetworkLoopbackTestTable = _PrvtNetworkLoopbackTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1)
)
if mibBuilder.loadTexts:
    prvtNetworkLoopbackTestTable.setStatus("current")
_PrvtNetworkLoopbackTestEntry_Object = MibTableRow
prvtNetworkLoopbackTestEntry = _PrvtNetworkLoopbackTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1)
)
prvtNetworkLoopbackTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup"),
)
if mibBuilder.loadTexts:
    prvtNetworkLoopbackTestEntry.setStatus("current")


class _PrvtNetworkLoopTestDuration_Type(Integer32):
    """Custom type prvtNetworkLoopTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PrvtNetworkLoopTestDuration_Type.__name__ = "Integer32"
_PrvtNetworkLoopTestDuration_Object = MibTableColumn
prvtNetworkLoopTestDuration = _PrvtNetworkLoopTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1, 1),
    _PrvtNetworkLoopTestDuration_Type()
)
prvtNetworkLoopTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtNetworkLoopTestDuration.setStatus("current")
_PrvtNetworkLoopStartDuration_Type = TimeStamp
_PrvtNetworkLoopStartDuration_Object = MibTableColumn
prvtNetworkLoopStartDuration = _PrvtNetworkLoopStartDuration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1, 2),
    _PrvtNetworkLoopStartDuration_Type()
)
prvtNetworkLoopStartDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtNetworkLoopStartDuration.setStatus("current")
_PrvtNetworkLoopEndDuration_Type = TimeStamp
_PrvtNetworkLoopEndDuration_Object = MibTableColumn
prvtNetworkLoopEndDuration = _PrvtNetworkLoopEndDuration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1, 3),
    _PrvtNetworkLoopEndDuration_Type()
)
prvtNetworkLoopEndDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtNetworkLoopEndDuration.setStatus("current")
_PrvtNetworkLoopRowStatus_Type = RowStatus
_PrvtNetworkLoopRowStatus_Object = MibTableColumn
prvtNetworkLoopRowStatus = _PrvtNetworkLoopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1, 4),
    _PrvtNetworkLoopRowStatus_Type()
)
prvtNetworkLoopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtNetworkLoopRowStatus.setStatus("current")
_PrvtNetworkLoopbackTestConformance_ObjectIdentity = ObjectIdentity
prvtNetworkLoopbackTestConformance = _PrvtNetworkLoopbackTestConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2)
)
_PrvtNetworkLoopTestCompliances_ObjectIdentity = ObjectIdentity
prvtNetworkLoopTestCompliances = _PrvtNetworkLoopTestCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 1)
)
_PrvtNetworkLoopTestGroups_ObjectIdentity = ObjectIdentity
prvtNetworkLoopTestGroups = _PrvtNetworkLoopTestGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 2)
)

# Managed Objects groups

prvtNetworkLoopTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 2, 1)
)
prvtNetworkLoopTestGroup.setObjects(
      *(("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopTestDuration"),
        ("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopStartDuration"),
        ("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopEndDuration"),
        ("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopRowStatus"))
)
if mibBuilder.loadTexts:
    prvtNetworkLoopTestGroup.setStatus("current")


# Notification objects

prvtNetworkLoopbackTestFinish = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 0, 1)
)
prvtNetworkLoopbackTestFinish.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup"))
)
if mibBuilder.loadTexts:
    prvtNetworkLoopbackTestFinish.setStatus(
        "current"
    )


# Notifications groups

prvtNetworkLoopTestNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 2, 2)
)
prvtNetworkLoopTestNotificationsGroup.setObjects(
    ("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopbackTestFinish")
)
if mibBuilder.loadTexts:
    prvtNetworkLoopTestNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prvtNetworkLoopTestCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 1, 1)
)
prvtNetworkLoopTestCompliance.setObjects(
      *(("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopTestGroup"),
        ("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopTestNotificationsGroup"))
)
if mibBuilder.loadTexts:
    prvtNetworkLoopTestCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-NETWORK-LOOPBACK-TEST-MIB",
    **{"prvtNetworkLoopbackTestMib": prvtNetworkLoopbackTestMib,
       "prvtNetworkLoopbackTestNotifications": prvtNetworkLoopbackTestNotifications,
       "prvtNetworkLoopbackTestFinish": prvtNetworkLoopbackTestFinish,
       "prvtNetworkLoopbackTestObjects": prvtNetworkLoopbackTestObjects,
       "prvtNetworkLoopbackTestTable": prvtNetworkLoopbackTestTable,
       "prvtNetworkLoopbackTestEntry": prvtNetworkLoopbackTestEntry,
       "prvtNetworkLoopTestDuration": prvtNetworkLoopTestDuration,
       "prvtNetworkLoopStartDuration": prvtNetworkLoopStartDuration,
       "prvtNetworkLoopEndDuration": prvtNetworkLoopEndDuration,
       "prvtNetworkLoopRowStatus": prvtNetworkLoopRowStatus,
       "prvtNetworkLoopbackTestConformance": prvtNetworkLoopbackTestConformance,
       "prvtNetworkLoopTestCompliances": prvtNetworkLoopTestCompliances,
       "prvtNetworkLoopTestCompliance": prvtNetworkLoopTestCompliance,
       "prvtNetworkLoopTestGroups": prvtNetworkLoopTestGroups,
       "prvtNetworkLoopTestGroup": prvtNetworkLoopTestGroup,
       "prvtNetworkLoopTestNotificationsGroup": prvtNetworkLoopTestNotificationsGroup}
)
