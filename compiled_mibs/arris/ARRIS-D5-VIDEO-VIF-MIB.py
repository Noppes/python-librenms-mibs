# SNMP MIB module (ARRIS-D5-VIDEO-VIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-VIDEO-VIF-MIB

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

(arrisD5UEQam,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisD5UEQam")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arrisD5UEQamVIFMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_D5UEQamVirtualInterfaceLbTable_Object = MibTable
d5UEQamVirtualInterfaceLbTable = _D5UEQamVirtualInterfaceLbTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1)
)
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbTable.setStatus("current")
_D5UEQamVirtualInterfaceLbEntry_Object = MibTableRow
d5UEQamVirtualInterfaceLbEntry = _D5UEQamVirtualInterfaceLbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1)
)
d5UEQamVirtualInterfaceLbEntry.setIndexNames(
    (0, "ARRIS-D5-VIDEO-VIF-MIB", "d5UEQamVirtualInterfaceLbVifNumber"),
)
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbEntry.setStatus("current")


class _D5UEQamVirtualInterfaceLbVifNumber_Type(Unsigned32):
    """Custom type d5UEQamVirtualInterfaceLbVifNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_D5UEQamVirtualInterfaceLbVifNumber_Type.__name__ = "Unsigned32"
_D5UEQamVirtualInterfaceLbVifNumber_Object = MibTableColumn
d5UEQamVirtualInterfaceLbVifNumber = _D5UEQamVirtualInterfaceLbVifNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 1),
    _D5UEQamVirtualInterfaceLbVifNumber_Type()
)
d5UEQamVirtualInterfaceLbVifNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbVifNumber.setStatus("current")


class _D5UEQamVirtualInterfaceLbNumber_Type(Unsigned32):
    """Custom type d5UEQamVirtualInterfaceLbNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_D5UEQamVirtualInterfaceLbNumber_Type.__name__ = "Unsigned32"
_D5UEQamVirtualInterfaceLbNumber_Object = MibTableColumn
d5UEQamVirtualInterfaceLbNumber = _D5UEQamVirtualInterfaceLbNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 2),
    _D5UEQamVirtualInterfaceLbNumber_Type()
)
d5UEQamVirtualInterfaceLbNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbNumber.setStatus("current")
_D5UEQamVirtualInterfaceLbIpAddress_Type = IpAddress
_D5UEQamVirtualInterfaceLbIpAddress_Object = MibTableColumn
d5UEQamVirtualInterfaceLbIpAddress = _D5UEQamVirtualInterfaceLbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 3),
    _D5UEQamVirtualInterfaceLbIpAddress_Type()
)
d5UEQamVirtualInterfaceLbIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbIpAddress.setStatus("current")
_D5UEQamVirtualInterfaceLbIpMask_Type = IpAddress
_D5UEQamVirtualInterfaceLbIpMask_Object = MibTableColumn
d5UEQamVirtualInterfaceLbIpMask = _D5UEQamVirtualInterfaceLbIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 4),
    _D5UEQamVirtualInterfaceLbIpMask_Type()
)
d5UEQamVirtualInterfaceLbIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbIpMask.setStatus("current")
_D5UEQamVirtualInterfaceLbIpBCastAddress_Type = IpAddress
_D5UEQamVirtualInterfaceLbIpBCastAddress_Object = MibTableColumn
d5UEQamVirtualInterfaceLbIpBCastAddress = _D5UEQamVirtualInterfaceLbIpBCastAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 5),
    _D5UEQamVirtualInterfaceLbIpBCastAddress_Type()
)
d5UEQamVirtualInterfaceLbIpBCastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbIpBCastAddress.setStatus("current")
_D5UEQamVirtualInterfaceLbIpDHCP_Type = TruthValue
_D5UEQamVirtualInterfaceLbIpDHCP_Object = MibTableColumn
d5UEQamVirtualInterfaceLbIpDHCP = _D5UEQamVirtualInterfaceLbIpDHCP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 6),
    _D5UEQamVirtualInterfaceLbIpDHCP_Type()
)
d5UEQamVirtualInterfaceLbIpDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbIpDHCP.setStatus("current")
_D5UEQamVirtualInterfaceLbManagementAccess_Type = TruthValue
_D5UEQamVirtualInterfaceLbManagementAccess_Object = MibTableColumn
d5UEQamVirtualInterfaceLbManagementAccess = _D5UEQamVirtualInterfaceLbManagementAccess_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 7),
    _D5UEQamVirtualInterfaceLbManagementAccess_Type()
)
d5UEQamVirtualInterfaceLbManagementAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbManagementAccess.setStatus("current")
_D5UEQamVirtualInterfaceLbAdminState_Type = TruthValue
_D5UEQamVirtualInterfaceLbAdminState_Object = MibTableColumn
d5UEQamVirtualInterfaceLbAdminState = _D5UEQamVirtualInterfaceLbAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 8),
    _D5UEQamVirtualInterfaceLbAdminState_Type()
)
d5UEQamVirtualInterfaceLbAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbAdminState.setStatus("current")
_D5UEQamVirtualInterfaceLbIfIndex_Type = InterfaceIndex
_D5UEQamVirtualInterfaceLbIfIndex_Object = MibTableColumn
d5UEQamVirtualInterfaceLbIfIndex = _D5UEQamVirtualInterfaceLbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 9),
    _D5UEQamVirtualInterfaceLbIfIndex_Type()
)
d5UEQamVirtualInterfaceLbIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbIfIndex.setStatus("current")
_D5UEQamVirtualInterfaceLbStatus_Type = RowStatus
_D5UEQamVirtualInterfaceLbStatus_Object = MibTableColumn
d5UEQamVirtualInterfaceLbStatus = _D5UEQamVirtualInterfaceLbStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 1, 1, 10),
    _D5UEQamVirtualInterfaceLbStatus_Type()
)
d5UEQamVirtualInterfaceLbStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfaceLbStatus.setStatus("current")
_D5UEQamVirtualInterfacePhyTable_Object = MibTable
d5UEQamVirtualInterfacePhyTable = _D5UEQamVirtualInterfacePhyTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 2)
)
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfacePhyTable.setStatus("current")
_D5UEQamVirtualInterfacePhyEntry_Object = MibTableRow
d5UEQamVirtualInterfacePhyEntry = _D5UEQamVirtualInterfacePhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 2, 1)
)
d5UEQamVirtualInterfacePhyEntry.setIndexNames(
    (0, "ARRIS-D5-VIDEO-VIF-MIB", "d5UEQamVirtualInterfacePhyNumber"),
    (0, "ARRIS-D5-VIDEO-VIF-MIB", "d5UEQamVirtualInterfacePhyPriority"),
)
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfacePhyEntry.setStatus("current")


class _D5UEQamVirtualInterfacePhyNumber_Type(Unsigned32):
    """Custom type d5UEQamVirtualInterfacePhyNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_D5UEQamVirtualInterfacePhyNumber_Type.__name__ = "Unsigned32"
_D5UEQamVirtualInterfacePhyNumber_Object = MibTableColumn
d5UEQamVirtualInterfacePhyNumber = _D5UEQamVirtualInterfacePhyNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 2, 1, 1),
    _D5UEQamVirtualInterfacePhyNumber_Type()
)
d5UEQamVirtualInterfacePhyNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfacePhyNumber.setStatus("current")


class _D5UEQamVirtualInterfacePhyPriority_Type(Unsigned32):
    """Custom type d5UEQamVirtualInterfacePhyPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_D5UEQamVirtualInterfacePhyPriority_Type.__name__ = "Unsigned32"
_D5UEQamVirtualInterfacePhyPriority_Object = MibTableColumn
d5UEQamVirtualInterfacePhyPriority = _D5UEQamVirtualInterfacePhyPriority_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 2, 1, 2),
    _D5UEQamVirtualInterfacePhyPriority_Type()
)
d5UEQamVirtualInterfacePhyPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfacePhyPriority.setStatus("current")
_D5UEQamVirtualInterfacePhyIfIndex_Type = InterfaceIndex
_D5UEQamVirtualInterfacePhyIfIndex_Object = MibTableColumn
d5UEQamVirtualInterfacePhyIfIndex = _D5UEQamVirtualInterfacePhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 2, 1, 3),
    _D5UEQamVirtualInterfacePhyIfIndex_Type()
)
d5UEQamVirtualInterfacePhyIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfacePhyIfIndex.setStatus("current")


class _D5UEQamVirtualInterfacePhyVlan_Type(Unsigned32):
    """Custom type d5UEQamVirtualInterfacePhyVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_D5UEQamVirtualInterfacePhyVlan_Type.__name__ = "Unsigned32"
_D5UEQamVirtualInterfacePhyVlan_Object = MibTableColumn
d5UEQamVirtualInterfacePhyVlan = _D5UEQamVirtualInterfacePhyVlan_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 2, 1, 4),
    _D5UEQamVirtualInterfacePhyVlan_Type()
)
d5UEQamVirtualInterfacePhyVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfacePhyVlan.setStatus("current")
_D5UEQamVirtualInterfacePhyStatus_Type = RowStatus
_D5UEQamVirtualInterfacePhyStatus_Object = MibTableColumn
d5UEQamVirtualInterfacePhyStatus = _D5UEQamVirtualInterfacePhyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 14, 2, 1, 5),
    _D5UEQamVirtualInterfacePhyStatus_Type()
)
d5UEQamVirtualInterfacePhyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5UEQamVirtualInterfacePhyStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-VIDEO-VIF-MIB",
    **{"arrisD5UEQamVIFMib": arrisD5UEQamVIFMib,
       "d5UEQamVirtualInterfaceLbTable": d5UEQamVirtualInterfaceLbTable,
       "d5UEQamVirtualInterfaceLbEntry": d5UEQamVirtualInterfaceLbEntry,
       "d5UEQamVirtualInterfaceLbVifNumber": d5UEQamVirtualInterfaceLbVifNumber,
       "d5UEQamVirtualInterfaceLbNumber": d5UEQamVirtualInterfaceLbNumber,
       "d5UEQamVirtualInterfaceLbIpAddress": d5UEQamVirtualInterfaceLbIpAddress,
       "d5UEQamVirtualInterfaceLbIpMask": d5UEQamVirtualInterfaceLbIpMask,
       "d5UEQamVirtualInterfaceLbIpBCastAddress": d5UEQamVirtualInterfaceLbIpBCastAddress,
       "d5UEQamVirtualInterfaceLbIpDHCP": d5UEQamVirtualInterfaceLbIpDHCP,
       "d5UEQamVirtualInterfaceLbManagementAccess": d5UEQamVirtualInterfaceLbManagementAccess,
       "d5UEQamVirtualInterfaceLbAdminState": d5UEQamVirtualInterfaceLbAdminState,
       "d5UEQamVirtualInterfaceLbIfIndex": d5UEQamVirtualInterfaceLbIfIndex,
       "d5UEQamVirtualInterfaceLbStatus": d5UEQamVirtualInterfaceLbStatus,
       "d5UEQamVirtualInterfacePhyTable": d5UEQamVirtualInterfacePhyTable,
       "d5UEQamVirtualInterfacePhyEntry": d5UEQamVirtualInterfacePhyEntry,
       "d5UEQamVirtualInterfacePhyNumber": d5UEQamVirtualInterfacePhyNumber,
       "d5UEQamVirtualInterfacePhyPriority": d5UEQamVirtualInterfacePhyPriority,
       "d5UEQamVirtualInterfacePhyIfIndex": d5UEQamVirtualInterfacePhyIfIndex,
       "d5UEQamVirtualInterfacePhyVlan": d5UEQamVirtualInterfacePhyVlan,
       "d5UEQamVirtualInterfacePhyStatus": d5UEQamVirtualInterfacePhyStatus}
)
