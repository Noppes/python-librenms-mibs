# SNMP MIB module (TN-PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-PRIVATE-VLAN-MIB

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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnPrivateVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnPrivateVlansMIBObjects_ObjectIdentity = ObjectIdentity
tnPrivateVlansMIBObjects = _TnPrivateVlansMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1)
)
_TnPrivateVlanMgmt_ObjectIdentity = ObjectIdentity
tnPrivateVlanMgmt = _TnPrivateVlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1, 1)
)
_TnPVlanMembershipTable_Object = MibTable
tnPVlanMembershipTable = _TnPVlanMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnPVlanMembershipTable.setStatus("current")
_TnPVlanMembershipEntry_Object = MibTableRow
tnPVlanMembershipEntry = _TnPVlanMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1, 1, 1, 1)
)
tnPVlanMembershipEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-PRIVATE-VLAN-MIB", "tnPVlanMembershipPVlanId"),
)
if mibBuilder.loadTexts:
    tnPVlanMembershipEntry.setStatus("current")
_TnPVlanMembershipPVlanId_Type = Unsigned32
_TnPVlanMembershipPVlanId_Object = MibTableColumn
tnPVlanMembershipPVlanId = _TnPVlanMembershipPVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1, 1, 1, 1, 1),
    _TnPVlanMembershipPVlanId_Type()
)
tnPVlanMembershipPVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPVlanMembershipPVlanId.setStatus("current")
_TnPVlanMembershipPortMember_Type = PortList
_TnPVlanMembershipPortMember_Object = MibTableColumn
tnPVlanMembershipPortMember = _TnPVlanMembershipPortMember_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1, 1, 1, 1, 2),
    _TnPVlanMembershipPortMember_Type()
)
tnPVlanMembershipPortMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPVlanMembershipPortMember.setStatus("current")
_TnPVlanMembershipRowStatus_Type = RowStatus
_TnPVlanMembershipRowStatus_Object = MibTableColumn
tnPVlanMembershipRowStatus = _TnPVlanMembershipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1, 1, 1, 1, 3),
    _TnPVlanMembershipRowStatus_Type()
)
tnPVlanMembershipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPVlanMembershipRowStatus.setStatus("current")
_TnPVlanPortIsolationTable_Object = MibTable
tnPVlanPortIsolationTable = _TnPVlanPortIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnPVlanPortIsolationTable.setStatus("current")
_TnPVlanPortIsolationEntry_Object = MibTableRow
tnPVlanPortIsolationEntry = _TnPVlanPortIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1, 1, 2, 1)
)
tnPVlanPortIsolationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnPVlanPortIsolationEntry.setStatus("current")
_TnPVlanPortIsolationPortMember_Type = PortList
_TnPVlanPortIsolationPortMember_Object = MibTableColumn
tnPVlanPortIsolationPortMember = _TnPVlanPortIsolationPortMember_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 1, 1, 2, 1, 1),
    _TnPVlanPortIsolationPortMember_Type()
)
tnPVlanPortIsolationPortMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPVlanPortIsolationPortMember.setStatus("current")
_TnPrivateVlanMIBNotifications_ObjectIdentity = ObjectIdentity
tnPrivateVlanMIBNotifications = _TnPrivateVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 26, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-PRIVATE-VLAN-MIB",
    **{"tnPrivateVlanMIB": tnPrivateVlanMIB,
       "tnPrivateVlansMIBObjects": tnPrivateVlansMIBObjects,
       "tnPrivateVlanMgmt": tnPrivateVlanMgmt,
       "tnPVlanMembershipTable": tnPVlanMembershipTable,
       "tnPVlanMembershipEntry": tnPVlanMembershipEntry,
       "tnPVlanMembershipPVlanId": tnPVlanMembershipPVlanId,
       "tnPVlanMembershipPortMember": tnPVlanMembershipPortMember,
       "tnPVlanMembershipRowStatus": tnPVlanMembershipRowStatus,
       "tnPVlanPortIsolationTable": tnPVlanPortIsolationTable,
       "tnPVlanPortIsolationEntry": tnPVlanPortIsolationEntry,
       "tnPVlanPortIsolationPortMember": tnPVlanPortIsolationPortMember,
       "tnPrivateVlanMIBNotifications": tnPrivateVlanMIBNotifications}
)
