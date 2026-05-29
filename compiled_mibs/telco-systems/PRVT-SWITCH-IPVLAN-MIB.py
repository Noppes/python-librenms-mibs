# SNMP MIB module (PRVT-SWITCH-IPVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SWITCH-IPVLAN-MIB

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

(ipSwitch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "ipSwitch")

(dot1qVlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtSwitchIpVLANMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2)
)
if mibBuilder.loadTexts:
    prvtSwitchIpVLANMib.setRevisions(
        ("2008-01-01 00:00",
         "2006-11-03 09:59",
         "2005-02-16 09:59",
         "2000-11-24 09:59")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpInterface_ObjectIdentity = ObjectIdentity
ipInterface = _IpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1)
)
_IpInterfaceTable_Object = MibTable
ipInterfaceTable = _IpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipInterfaceTable.setStatus("current")
_IpInterfaceEntry_Object = MibTableRow
ipInterfaceEntry = _IpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1)
)
ipInterfaceEntry.setIndexNames(
    (0, "PRVT-SWITCH-IPVLAN-MIB", "ipInterfaceName"),
)
if mibBuilder.loadTexts:
    ipInterfaceEntry.setStatus("current")


class _IpInterfaceName_Type(Integer32):
    """Custom type ipInterfaceName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpInterfaceName_Type.__name__ = "Integer32"
_IpInterfaceName_Object = MibTableColumn
ipInterfaceName = _IpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 1),
    _IpInterfaceName_Type()
)
ipInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceName.setStatus("current")
_IpInterfaceIndex_Type = Integer32
_IpInterfaceIndex_Object = MibTableColumn
ipInterfaceIndex = _IpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 2),
    _IpInterfaceIndex_Type()
)
ipInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceIndex.setStatus("current")


class _IpInterfaceType_Type(Integer32):
    """Custom type ipInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pseudoInterface", 1),
          ("ipInterface", 2))
    )


_IpInterfaceType_Type.__name__ = "Integer32"
_IpInterfaceType_Object = MibTableColumn
ipInterfaceType = _IpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 3),
    _IpInterfaceType_Type()
)
ipInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipInterfaceType.setStatus("current")
_IpInterfaceIpAddress_Type = IpAddress
_IpInterfaceIpAddress_Object = MibTableColumn
ipInterfaceIpAddress = _IpInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 4),
    _IpInterfaceIpAddress_Type()
)
ipInterfaceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipInterfaceIpAddress.setStatus("current")
_IpInterfaceSubnetMask_Type = IpAddress
_IpInterfaceSubnetMask_Object = MibTableColumn
ipInterfaceSubnetMask = _IpInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 5),
    _IpInterfaceSubnetMask_Type()
)
ipInterfaceSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipInterfaceSubnetMask.setStatus("current")
_IpInterfaceRowStatus_Type = RowStatus
_IpInterfaceRowStatus_Object = MibTableColumn
ipInterfaceRowStatus = _IpInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 6),
    _IpInterfaceRowStatus_Type()
)
ipInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipInterfaceRowStatus.setStatus("current")
_IpLoInterfaceTable_Object = MibTable
ipLoInterfaceTable = _IpLoInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ipLoInterfaceTable.setStatus("current")
_IpLoInterfaceEntry_Object = MibTableRow
ipLoInterfaceEntry = _IpLoInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1)
)
ipLoInterfaceEntry.setIndexNames(
    (0, "PRVT-SWITCH-IPVLAN-MIB", "ipLoInterfaceName"),
)
if mibBuilder.loadTexts:
    ipLoInterfaceEntry.setStatus("current")


class _IpLoInterfaceName_Type(Integer32):
    """Custom type ipLoInterfaceName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_IpLoInterfaceName_Type.__name__ = "Integer32"
_IpLoInterfaceName_Object = MibTableColumn
ipLoInterfaceName = _IpLoInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 1),
    _IpLoInterfaceName_Type()
)
ipLoInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLoInterfaceName.setStatus("current")
_IpLoInterfaceIndex_Type = Integer32
_IpLoInterfaceIndex_Object = MibTableColumn
ipLoInterfaceIndex = _IpLoInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 2),
    _IpLoInterfaceIndex_Type()
)
ipLoInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLoInterfaceIndex.setStatus("current")


class _IpLoInterfaceType_Type(Integer32):
    """Custom type ipLoInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pseudoInterface", 1),
          ("ipInterface", 2))
    )


_IpLoInterfaceType_Type.__name__ = "Integer32"
_IpLoInterfaceType_Object = MibTableColumn
ipLoInterfaceType = _IpLoInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 3),
    _IpLoInterfaceType_Type()
)
ipLoInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipLoInterfaceType.setStatus("current")
_IpLoInterfaceIpAddress_Type = IpAddress
_IpLoInterfaceIpAddress_Object = MibTableColumn
ipLoInterfaceIpAddress = _IpLoInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 4),
    _IpLoInterfaceIpAddress_Type()
)
ipLoInterfaceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipLoInterfaceIpAddress.setStatus("current")
_IpLoInterfaceSubnetMask_Type = IpAddress
_IpLoInterfaceSubnetMask_Object = MibTableColumn
ipLoInterfaceSubnetMask = _IpLoInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 5),
    _IpLoInterfaceSubnetMask_Type()
)
ipLoInterfaceSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipLoInterfaceSubnetMask.setStatus("current")
_IpLoInterfaceRowStatus_Type = RowStatus
_IpLoInterfaceRowStatus_Object = MibTableColumn
ipLoInterfaceRowStatus = _IpLoInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 6),
    _IpLoInterfaceRowStatus_Type()
)
ipLoInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipLoInterfaceRowStatus.setStatus("current")
_IpVLAN_ObjectIdentity = ObjectIdentity
ipVLAN = _IpVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2)
)
_IpVLANTable_Object = MibTable
ipVLANTable = _IpVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipVLANTable.setStatus("current")
_IpVLANEntry_Object = MibTableRow
ipVLANEntry = _IpVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 1, 1)
)
ipVLANEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "PRVT-SWITCH-IPVLAN-MIB", "ipInterfaceName"),
)
if mibBuilder.loadTexts:
    ipVLANEntry.setStatus("current")


class _IpVLANStatus_Type(Integer32):
    """Custom type ipVLANStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 1),
          ("detached", 2))
    )


_IpVLANStatus_Type.__name__ = "Integer32"
_IpVLANStatus_Object = MibTableColumn
ipVLANStatus = _IpVLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 1, 1, 1),
    _IpVLANStatus_Type()
)
ipVLANStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipVLANStatus.setStatus("current")
_IpPortMappingTable_Object = MibTable
ipPortMappingTable = _IpPortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ipPortMappingTable.setStatus("current")
_IpPortMappingEntry_Object = MibTableRow
ipPortMappingEntry = _IpPortMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 2, 1)
)
ipPortMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ipPortMappingEntry.setStatus("current")
_IpPortSwIface_Type = Integer32
_IpPortSwIface_Object = MibTableColumn
ipPortSwIface = _IpPortSwIface_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 2, 1, 1),
    _IpPortSwIface_Type()
)
ipPortSwIface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipPortSwIface.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SWITCH-IPVLAN-MIB",
    **{"prvtSwitchIpVLANMib": prvtSwitchIpVLANMib,
       "ipInterface": ipInterface,
       "ipInterfaceTable": ipInterfaceTable,
       "ipInterfaceEntry": ipInterfaceEntry,
       "ipInterfaceName": ipInterfaceName,
       "ipInterfaceIndex": ipInterfaceIndex,
       "ipInterfaceType": ipInterfaceType,
       "ipInterfaceIpAddress": ipInterfaceIpAddress,
       "ipInterfaceSubnetMask": ipInterfaceSubnetMask,
       "ipInterfaceRowStatus": ipInterfaceRowStatus,
       "ipLoInterfaceTable": ipLoInterfaceTable,
       "ipLoInterfaceEntry": ipLoInterfaceEntry,
       "ipLoInterfaceName": ipLoInterfaceName,
       "ipLoInterfaceIndex": ipLoInterfaceIndex,
       "ipLoInterfaceType": ipLoInterfaceType,
       "ipLoInterfaceIpAddress": ipLoInterfaceIpAddress,
       "ipLoInterfaceSubnetMask": ipLoInterfaceSubnetMask,
       "ipLoInterfaceRowStatus": ipLoInterfaceRowStatus,
       "ipVLAN": ipVLAN,
       "ipVLANTable": ipVLANTable,
       "ipVLANEntry": ipVLANEntry,
       "ipVLANStatus": ipVLANStatus,
       "ipPortMappingTable": ipPortMappingTable,
       "ipPortMappingEntry": ipPortMappingEntry,
       "ipPortSwIface": ipPortSwIface}
)
