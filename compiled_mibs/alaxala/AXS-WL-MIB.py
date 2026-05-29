# SNMP MIB module (AXS-WL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AXS-WL-MIB

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

(axsMib,) = mibBuilder.importSymbols(
    "AX2530S",
    "axsMib")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxsWhitelist_ObjectIdentity = ObjectIdentity
axsWhitelist = _AxsWhitelist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500)
)
_AxsWhitelistControl_ObjectIdentity = ObjectIdentity
axsWhitelistControl = _AxsWhitelistControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 1)
)
_AxsWhitelistDataGroup_ObjectIdentity = ObjectIdentity
axsWhitelistDataGroup = _AxsWhitelistDataGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 2)
)
_AxsWhitelistAlarmGroup_ObjectIdentity = ObjectIdentity
axsWhitelistAlarmGroup = _AxsWhitelistAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 3)
)
_AxsWhitelistSourceBlockGroup_ObjectIdentity = ObjectIdentity
axsWhitelistSourceBlockGroup = _AxsWhitelistSourceBlockGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 4)
)
_AxsWhitelistSourceBlockTable_Object = MibTable
axsWhitelistSourceBlockTable = _AxsWhitelistSourceBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 4, 1)
)
if mibBuilder.loadTexts:
    axsWhitelistSourceBlockTable.setStatus("mandatory")
_AxsWhitelistSourceBlockEntry_Object = MibTableRow
axsWhitelistSourceBlockEntry = _AxsWhitelistSourceBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 4, 1, 1)
)
axsWhitelistSourceBlockEntry.setIndexNames(
    (0, "AXS-WL-MIB", "axsWhitelistSourceBlockAddressType"),
    (0, "AXS-WL-MIB", "axsWhitelistSourceBlockAddress"),
)
if mibBuilder.loadTexts:
    axsWhitelistSourceBlockEntry.setStatus("current")
_AxsWhitelistSourceBlockAddressType_Type = InetAddressType
_AxsWhitelistSourceBlockAddressType_Object = MibTableColumn
axsWhitelistSourceBlockAddressType = _AxsWhitelistSourceBlockAddressType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 4, 1, 1, 1),
    _AxsWhitelistSourceBlockAddressType_Type()
)
axsWhitelistSourceBlockAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsWhitelistSourceBlockAddressType.setStatus("current")
_AxsWhitelistSourceBlockAddress_Type = InetAddress
_AxsWhitelistSourceBlockAddress_Object = MibTableColumn
axsWhitelistSourceBlockAddress = _AxsWhitelistSourceBlockAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 4, 1, 1, 2),
    _AxsWhitelistSourceBlockAddress_Type()
)
axsWhitelistSourceBlockAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axsWhitelistSourceBlockAddress.setStatus("current")
_AxsWhitelistSourceBlockRowStatus_Type = RowStatus
_AxsWhitelistSourceBlockRowStatus_Object = MibTableColumn
axsWhitelistSourceBlockRowStatus = _AxsWhitelistSourceBlockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 4, 1, 1, 3),
    _AxsWhitelistSourceBlockRowStatus_Type()
)
axsWhitelistSourceBlockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axsWhitelistSourceBlockRowStatus.setStatus("current")
_AxsWhitelistSourceBlockStorageType_Type = StorageType
_AxsWhitelistSourceBlockStorageType_Object = MibTableColumn
axsWhitelistSourceBlockStorageType = _AxsWhitelistSourceBlockStorageType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 4, 1, 1, 4),
    _AxsWhitelistSourceBlockStorageType_Type()
)
axsWhitelistSourceBlockStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axsWhitelistSourceBlockStorageType.setStatus("current")


class _AxsWhitelistSourceBlockTime_Type(Integer32):
    """Custom type axsWhitelistSourceBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxsWhitelistSourceBlockTime_Type.__name__ = "Integer32"
_AxsWhitelistSourceBlockTime_Object = MibTableColumn
axsWhitelistSourceBlockTime = _AxsWhitelistSourceBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 2, 1, 500, 4, 1, 1, 5),
    _AxsWhitelistSourceBlockTime_Type()
)
axsWhitelistSourceBlockTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axsWhitelistSourceBlockTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AXS-WL-MIB",
    **{"axsWhitelist": axsWhitelist,
       "axsWhitelistControl": axsWhitelistControl,
       "axsWhitelistDataGroup": axsWhitelistDataGroup,
       "axsWhitelistAlarmGroup": axsWhitelistAlarmGroup,
       "axsWhitelistSourceBlockGroup": axsWhitelistSourceBlockGroup,
       "axsWhitelistSourceBlockTable": axsWhitelistSourceBlockTable,
       "axsWhitelistSourceBlockEntry": axsWhitelistSourceBlockEntry,
       "axsWhitelistSourceBlockAddressType": axsWhitelistSourceBlockAddressType,
       "axsWhitelistSourceBlockAddress": axsWhitelistSourceBlockAddress,
       "axsWhitelistSourceBlockRowStatus": axsWhitelistSourceBlockRowStatus,
       "axsWhitelistSourceBlockStorageType": axsWhitelistSourceBlockStorageType,
       "axsWhitelistSourceBlockTime": axsWhitelistSourceBlockTime}
)
