# SNMP MIB module (PRVT-SUPER-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-SUPER-VLAN-MIB

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
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

prvtSuperVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136)
)
if mibBuilder.loadTexts:
    prvtSuperVlanMIB.setRevisions(
        ("2010-08-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtSuperVlanMIBObjects_ObjectIdentity = ObjectIdentity
prvtSuperVlanMIBObjects = _PrvtSuperVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1)
)
_PrvtSuperVlanIfTable_Object = MibTable
prvtSuperVlanIfTable = _PrvtSuperVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 1)
)
if mibBuilder.loadTexts:
    prvtSuperVlanIfTable.setStatus("current")
_PrvtSuperVlanIfEntry_Object = MibTableRow
prvtSuperVlanIfEntry = _PrvtSuperVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 1, 1)
)
prvtSuperVlanIfEntry.setIndexNames(
    (0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfIndex"),
)
if mibBuilder.loadTexts:
    prvtSuperVlanIfEntry.setStatus("current")
_PrvtSuperVlanIfIndex_Type = InterfaceIndex
_PrvtSuperVlanIfIndex_Object = MibTableColumn
prvtSuperVlanIfIndex = _PrvtSuperVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 1, 1, 1),
    _PrvtSuperVlanIfIndex_Type()
)
prvtSuperVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSuperVlanIfIndex.setStatus("current")
_PrvtSuperVlanIfTargetPort_Type = InterfaceIndexOrZero
_PrvtSuperVlanIfTargetPort_Object = MibTableColumn
prvtSuperVlanIfTargetPort = _PrvtSuperVlanIfTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 1, 1, 2),
    _PrvtSuperVlanIfTargetPort_Type()
)
prvtSuperVlanIfTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSuperVlanIfTargetPort.setStatus("current")
_PrvtSuperVlanIfRowStatus_Type = RowStatus
_PrvtSuperVlanIfRowStatus_Object = MibTableColumn
prvtSuperVlanIfRowStatus = _PrvtSuperVlanIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 1, 1, 3),
    _PrvtSuperVlanIfRowStatus_Type()
)
prvtSuperVlanIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSuperVlanIfRowStatus.setStatus("current")
_PrvtSuperVlanIfCVlanTable_Object = MibTable
prvtSuperVlanIfCVlanTable = _PrvtSuperVlanIfCVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 2)
)
if mibBuilder.loadTexts:
    prvtSuperVlanIfCVlanTable.setStatus("current")
_PrvtSuperVlanIfCVlanEntry_Object = MibTableRow
prvtSuperVlanIfCVlanEntry = _PrvtSuperVlanIfCVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 2, 1)
)
prvtSuperVlanIfCVlanEntry.setIndexNames(
    (0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfIndex"),
    (0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfCVlanId"),
)
if mibBuilder.loadTexts:
    prvtSuperVlanIfCVlanEntry.setStatus("current")


class _PrvtSuperVlanIfCVlanId_Type(Integer32):
    """Custom type prvtSuperVlanIfCVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4092),
    )


_PrvtSuperVlanIfCVlanId_Type.__name__ = "Integer32"
_PrvtSuperVlanIfCVlanId_Object = MibTableColumn
prvtSuperVlanIfCVlanId = _PrvtSuperVlanIfCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 2, 1, 1),
    _PrvtSuperVlanIfCVlanId_Type()
)
prvtSuperVlanIfCVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSuperVlanIfCVlanId.setStatus("current")


class _PrvtSuperVlanIfCVlanMask_Type(OctetString):
    """Custom type prvtSuperVlanIfCVlanMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PrvtSuperVlanIfCVlanMask_Type.__name__ = "OctetString"
_PrvtSuperVlanIfCVlanMask_Object = MibTableColumn
prvtSuperVlanIfCVlanMask = _PrvtSuperVlanIfCVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 2, 1, 2),
    _PrvtSuperVlanIfCVlanMask_Type()
)
prvtSuperVlanIfCVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSuperVlanIfCVlanMask.setStatus("current")
_PrvtSuperVlanIfCVlanRowStatus_Type = RowStatus
_PrvtSuperVlanIfCVlanRowStatus_Object = MibTableColumn
prvtSuperVlanIfCVlanRowStatus = _PrvtSuperVlanIfCVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 2, 1, 3),
    _PrvtSuperVlanIfCVlanRowStatus_Type()
)
prvtSuperVlanIfCVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSuperVlanIfCVlanRowStatus.setStatus("current")
_PrvtSuperVlanIfRingPortTable_Object = MibTable
prvtSuperVlanIfRingPortTable = _PrvtSuperVlanIfRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 3)
)
if mibBuilder.loadTexts:
    prvtSuperVlanIfRingPortTable.setStatus("current")
_PrvtSuperVlanIfRingPortEntry_Object = MibTableRow
prvtSuperVlanIfRingPortEntry = _PrvtSuperVlanIfRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 3, 1)
)
prvtSuperVlanIfRingPortEntry.setIndexNames(
    (0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfIndex"),
    (0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfRingPort1"),
    (0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfRingPort2"),
)
if mibBuilder.loadTexts:
    prvtSuperVlanIfRingPortEntry.setStatus("current")
_PrvtSuperVlanIfRingPort1_Type = InterfaceIndex
_PrvtSuperVlanIfRingPort1_Object = MibTableColumn
prvtSuperVlanIfRingPort1 = _PrvtSuperVlanIfRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 3, 1, 1),
    _PrvtSuperVlanIfRingPort1_Type()
)
prvtSuperVlanIfRingPort1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSuperVlanIfRingPort1.setStatus("current")
_PrvtSuperVlanIfRingPort2_Type = InterfaceIndex
_PrvtSuperVlanIfRingPort2_Object = MibTableColumn
prvtSuperVlanIfRingPort2 = _PrvtSuperVlanIfRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 3, 1, 2),
    _PrvtSuperVlanIfRingPort2_Type()
)
prvtSuperVlanIfRingPort2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtSuperVlanIfRingPort2.setStatus("current")


class _PrvtSuperVlanIfRingPortVlanId_Type(Integer32):
    """Custom type prvtSuperVlanIfRingPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4092),
    )


_PrvtSuperVlanIfRingPortVlanId_Type.__name__ = "Integer32"
_PrvtSuperVlanIfRingPortVlanId_Object = MibTableColumn
prvtSuperVlanIfRingPortVlanId = _PrvtSuperVlanIfRingPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 3, 1, 3),
    _PrvtSuperVlanIfRingPortVlanId_Type()
)
prvtSuperVlanIfRingPortVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSuperVlanIfRingPortVlanId.setStatus("current")
_PrvtSuperVlanIfRingPortPreferred_Type = InterfaceIndexOrZero
_PrvtSuperVlanIfRingPortPreferred_Object = MibTableColumn
prvtSuperVlanIfRingPortPreferred = _PrvtSuperVlanIfRingPortPreferred_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 3, 1, 4),
    _PrvtSuperVlanIfRingPortPreferred_Type()
)
prvtSuperVlanIfRingPortPreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSuperVlanIfRingPortPreferred.setStatus("current")
_PrvtSuperVlanIfRingPortActive_Type = InterfaceIndexOrZero
_PrvtSuperVlanIfRingPortActive_Object = MibTableColumn
prvtSuperVlanIfRingPortActive = _PrvtSuperVlanIfRingPortActive_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 3, 1, 5),
    _PrvtSuperVlanIfRingPortActive_Type()
)
prvtSuperVlanIfRingPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSuperVlanIfRingPortActive.setStatus("current")
_PrvtSuperVlanIfRingPortRowStatus_Type = RowStatus
_PrvtSuperVlanIfRingPortRowStatus_Object = MibTableColumn
prvtSuperVlanIfRingPortRowStatus = _PrvtSuperVlanIfRingPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 136, 1, 3, 1, 6),
    _PrvtSuperVlanIfRingPortRowStatus_Type()
)
prvtSuperVlanIfRingPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtSuperVlanIfRingPortRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SUPER-VLAN-MIB",
    **{"prvtSuperVlanMIB": prvtSuperVlanMIB,
       "prvtSuperVlanMIBObjects": prvtSuperVlanMIBObjects,
       "prvtSuperVlanIfTable": prvtSuperVlanIfTable,
       "prvtSuperVlanIfEntry": prvtSuperVlanIfEntry,
       "prvtSuperVlanIfIndex": prvtSuperVlanIfIndex,
       "prvtSuperVlanIfTargetPort": prvtSuperVlanIfTargetPort,
       "prvtSuperVlanIfRowStatus": prvtSuperVlanIfRowStatus,
       "prvtSuperVlanIfCVlanTable": prvtSuperVlanIfCVlanTable,
       "prvtSuperVlanIfCVlanEntry": prvtSuperVlanIfCVlanEntry,
       "prvtSuperVlanIfCVlanId": prvtSuperVlanIfCVlanId,
       "prvtSuperVlanIfCVlanMask": prvtSuperVlanIfCVlanMask,
       "prvtSuperVlanIfCVlanRowStatus": prvtSuperVlanIfCVlanRowStatus,
       "prvtSuperVlanIfRingPortTable": prvtSuperVlanIfRingPortTable,
       "prvtSuperVlanIfRingPortEntry": prvtSuperVlanIfRingPortEntry,
       "prvtSuperVlanIfRingPort1": prvtSuperVlanIfRingPort1,
       "prvtSuperVlanIfRingPort2": prvtSuperVlanIfRingPort2,
       "prvtSuperVlanIfRingPortVlanId": prvtSuperVlanIfRingPortVlanId,
       "prvtSuperVlanIfRingPortPreferred": prvtSuperVlanIfRingPortPreferred,
       "prvtSuperVlanIfRingPortActive": prvtSuperVlanIfRingPortActive,
       "prvtSuperVlanIfRingPortRowStatus": prvtSuperVlanIfRingPortRowStatus}
)
