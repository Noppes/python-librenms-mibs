# SNMP MIB module (PRVT-JDSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-JDSU-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

prvtJdsuMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137)
)
if mibBuilder.loadTexts:
    prvtJdsuMib.setRevisions(
        ("2011-03-15 00:00",
         "2011-02-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtJdsuNotifications_ObjectIdentity = ObjectIdentity
prvtJdsuNotifications = _PrvtJdsuNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 0)
)
_PrvtJdsuObjects_ObjectIdentity = ObjectIdentity
prvtJdsuObjects = _PrvtJdsuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1)
)
_PrvtJdsuLoopback_ObjectIdentity = ObjectIdentity
prvtJdsuLoopback = _PrvtJdsuLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1, 1)
)
_PrvtJdsuLoopbackTable_Object = MibTable
prvtJdsuLoopbackTable = _PrvtJdsuLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtJdsuLoopbackTable.setStatus("current")
_PrvtJdsuLoopbackEntry_Object = MibTableRow
prvtJdsuLoopbackEntry = _PrvtJdsuLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1, 1, 1, 1)
)
prvtJdsuLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtJdsuLoopbackEntry.setStatus("current")


class _PrvtJdsuLoopbackAdminStatus_Type(Integer32):
    """Custom type prvtJdsuLoopbackAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("forced", 2),
          ("remote", 3))
    )


_PrvtJdsuLoopbackAdminStatus_Type.__name__ = "Integer32"
_PrvtJdsuLoopbackAdminStatus_Object = MibTableColumn
prvtJdsuLoopbackAdminStatus = _PrvtJdsuLoopbackAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1, 1, 1, 1, 1),
    _PrvtJdsuLoopbackAdminStatus_Type()
)
prvtJdsuLoopbackAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtJdsuLoopbackAdminStatus.setStatus("current")
_PrvtJdsuLoopbackRemoteMac_Type = MacAddress
_PrvtJdsuLoopbackRemoteMac_Object = MibTableColumn
prvtJdsuLoopbackRemoteMac = _PrvtJdsuLoopbackRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1, 1, 1, 1, 2),
    _PrvtJdsuLoopbackRemoteMac_Type()
)
prvtJdsuLoopbackRemoteMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtJdsuLoopbackRemoteMac.setStatus("current")
_PrvtJdsuLoopbackRemoteInnerVlan_Type = VlanId
_PrvtJdsuLoopbackRemoteInnerVlan_Object = MibTableColumn
prvtJdsuLoopbackRemoteInnerVlan = _PrvtJdsuLoopbackRemoteInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1, 1, 1, 1, 3),
    _PrvtJdsuLoopbackRemoteInnerVlan_Type()
)
prvtJdsuLoopbackRemoteInnerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtJdsuLoopbackRemoteInnerVlan.setStatus("current")
_PrvtJdsuLoopbackRemoteOuterVlan_Type = VlanId
_PrvtJdsuLoopbackRemoteOuterVlan_Object = MibTableColumn
prvtJdsuLoopbackRemoteOuterVlan = _PrvtJdsuLoopbackRemoteOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1, 1, 1, 1, 4),
    _PrvtJdsuLoopbackRemoteOuterVlan_Type()
)
prvtJdsuLoopbackRemoteOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtJdsuLoopbackRemoteOuterVlan.setStatus("current")


class _PrvtJdsuLoopbackOperationalStatus_Type(Integer32):
    """Custom type prvtJdsuLoopbackOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_PrvtJdsuLoopbackOperationalStatus_Type.__name__ = "Integer32"
_PrvtJdsuLoopbackOperationalStatus_Object = MibTableColumn
prvtJdsuLoopbackOperationalStatus = _PrvtJdsuLoopbackOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1, 1, 1, 1, 5),
    _PrvtJdsuLoopbackOperationalStatus_Type()
)
prvtJdsuLoopbackOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtJdsuLoopbackOperationalStatus.setStatus("current")
_PrvtJdsuLoopbackRowStatus_Type = RowStatus
_PrvtJdsuLoopbackRowStatus_Object = MibTableColumn
prvtJdsuLoopbackRowStatus = _PrvtJdsuLoopbackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 1, 1, 1, 1, 6),
    _PrvtJdsuLoopbackRowStatus_Type()
)
prvtJdsuLoopbackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtJdsuLoopbackRowStatus.setStatus("current")
_PrvtJdsuConformance_ObjectIdentity = ObjectIdentity
prvtJdsuConformance = _PrvtJdsuConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 2)
)
_PrvtJdsuCompliances_ObjectIdentity = ObjectIdentity
prvtJdsuCompliances = _PrvtJdsuCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 2, 1)
)
_PrvtJdsuGroups_ObjectIdentity = ObjectIdentity
prvtJdsuGroups = _PrvtJdsuGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 2, 2)
)

# Managed Objects groups

prvtJdsuLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 2, 2, 1)
)
prvtJdsuLoopbackGroup.setObjects(
      *(("PRVT-JDSU-MIB", "prvtJdsuLoopbackAdminStatus"),
        ("PRVT-JDSU-MIB", "prvtJdsuLoopbackRemoteMac"),
        ("PRVT-JDSU-MIB", "prvtJdsuLoopbackRemoteInnerVlan"),
        ("PRVT-JDSU-MIB", "prvtJdsuLoopbackRemoteOuterVlan"),
        ("PRVT-JDSU-MIB", "prvtJdsuLoopbackOperationalStatus"),
        ("PRVT-JDSU-MIB", "prvtJdsuLoopbackRowStatus"))
)
if mibBuilder.loadTexts:
    prvtJdsuLoopbackGroup.setStatus("current")


# Notification objects

prvtJdsuAdminStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 0, 1)
)
prvtJdsuAdminStateChange.setObjects(
    ("PRVT-JDSU-MIB", "prvtJdsuLoopbackAdminStatus")
)
if mibBuilder.loadTexts:
    prvtJdsuAdminStateChange.setStatus(
        "current"
    )

prvtJdsuOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 0, 2)
)
prvtJdsuOperStateChange.setObjects(
    ("PRVT-JDSU-MIB", "prvtJdsuLoopbackOperationalStatus")
)
if mibBuilder.loadTexts:
    prvtJdsuOperStateChange.setStatus(
        "current"
    )


# Notifications groups

prvtJdsuLoopbackNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 2, 2, 2)
)
prvtJdsuLoopbackNotificationsGroup.setObjects(
      *(("PRVT-JDSU-MIB", "prvtJdsuAdminStateChange"),
        ("PRVT-JDSU-MIB", "prvtJdsuOperStateChange"))
)
if mibBuilder.loadTexts:
    prvtJdsuLoopbackNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prvtJdsuCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 137, 2, 1, 1)
)
prvtJdsuCompliance.setObjects(
      *(("PRVT-JDSU-MIB", "prvtJdsuLoopbackGroup"),
        ("PRVT-JDSU-MIB", "prvtJdsuLoopbackNotificationsGroup"))
)
if mibBuilder.loadTexts:
    prvtJdsuCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-JDSU-MIB",
    **{"prvtJdsuMib": prvtJdsuMib,
       "prvtJdsuNotifications": prvtJdsuNotifications,
       "prvtJdsuAdminStateChange": prvtJdsuAdminStateChange,
       "prvtJdsuOperStateChange": prvtJdsuOperStateChange,
       "prvtJdsuObjects": prvtJdsuObjects,
       "prvtJdsuLoopback": prvtJdsuLoopback,
       "prvtJdsuLoopbackTable": prvtJdsuLoopbackTable,
       "prvtJdsuLoopbackEntry": prvtJdsuLoopbackEntry,
       "prvtJdsuLoopbackAdminStatus": prvtJdsuLoopbackAdminStatus,
       "prvtJdsuLoopbackRemoteMac": prvtJdsuLoopbackRemoteMac,
       "prvtJdsuLoopbackRemoteInnerVlan": prvtJdsuLoopbackRemoteInnerVlan,
       "prvtJdsuLoopbackRemoteOuterVlan": prvtJdsuLoopbackRemoteOuterVlan,
       "prvtJdsuLoopbackOperationalStatus": prvtJdsuLoopbackOperationalStatus,
       "prvtJdsuLoopbackRowStatus": prvtJdsuLoopbackRowStatus,
       "prvtJdsuConformance": prvtJdsuConformance,
       "prvtJdsuCompliances": prvtJdsuCompliances,
       "prvtJdsuCompliance": prvtJdsuCompliance,
       "prvtJdsuGroups": prvtJdsuGroups,
       "prvtJdsuLoopbackGroup": prvtJdsuLoopbackGroup,
       "prvtJdsuLoopbackNotificationsGroup": prvtJdsuLoopbackNotificationsGroup}
)
