# SNMP MIB module (HUAWEI-STORAGE-SPACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\huawei\HUAWEI-STORAGE-SPACE-MIB

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hwStorage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4)
)
if mibBuilder.loadTexts:
    hwStorage.setRevisions(
        ("2013-04-06 13:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NodeCodeString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 17),
    )



# MIB Managed Objects in the order of their OIDs

_Huaweistorage_ObjectIdentity = ObjectIdentity
huaweistorage = _Huaweistorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774)
)
_HwISM_ObjectIdentity = ObjectIdentity
hwISM = _HwISM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1)
)
_HwStorageDevice_ObjectIdentity = ObjectIdentity
hwStorageDevice = _HwStorageDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23)
)
_HwSpaceInfo_ObjectIdentity = ObjectIdentity
hwSpaceInfo = _HwSpaceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4)
)
_HwInfoDiskDomainTable_Object = MibTable
hwInfoDiskDomainTable = _HwInfoDiskDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1)
)
if mibBuilder.loadTexts:
    hwInfoDiskDomainTable.setStatus("current")
_HwInfoDiskDomainEntry_Object = MibTableRow
hwInfoDiskDomainEntry = _HwInfoDiskDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1)
)
hwInfoDiskDomainEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainID"),
)
if mibBuilder.loadTexts:
    hwInfoDiskDomainEntry.setStatus("current")
_HwInfoDiskDomainID_Type = OctetString
_HwInfoDiskDomainID_Object = MibTableColumn
hwInfoDiskDomainID = _HwInfoDiskDomainID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 1),
    _HwInfoDiskDomainID_Type()
)
hwInfoDiskDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainID.setStatus("current")
_HwInfoDiskDomainName_Type = OctetString
_HwInfoDiskDomainName_Object = MibTableColumn
hwInfoDiskDomainName = _HwInfoDiskDomainName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 2),
    _HwInfoDiskDomainName_Type()
)
hwInfoDiskDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainName.setStatus("current")
_HwInfoDiskDomainHealthStatus_Type = Unsigned32
_HwInfoDiskDomainHealthStatus_Object = MibTableColumn
hwInfoDiskDomainHealthStatus = _HwInfoDiskDomainHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 3),
    _HwInfoDiskDomainHealthStatus_Type()
)
hwInfoDiskDomainHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainHealthStatus.setStatus("current")
_HwInfoDiskDomainRunningStatus_Type = Unsigned32
_HwInfoDiskDomainRunningStatus_Object = MibTableColumn
hwInfoDiskDomainRunningStatus = _HwInfoDiskDomainRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 4),
    _HwInfoDiskDomainRunningStatus_Type()
)
hwInfoDiskDomainRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainRunningStatus.setStatus("current")
_HwInfoDiskDomainTotalCapacity_Type = Counter64
_HwInfoDiskDomainTotalCapacity_Object = MibTableColumn
hwInfoDiskDomainTotalCapacity = _HwInfoDiskDomainTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 5),
    _HwInfoDiskDomainTotalCapacity_Type()
)
hwInfoDiskDomainTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainTotalCapacity.setStatus("current")
_HwInfoDiskDomainFreeCapacity_Type = Counter64
_HwInfoDiskDomainFreeCapacity_Object = MibTableColumn
hwInfoDiskDomainFreeCapacity = _HwInfoDiskDomainFreeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 6),
    _HwInfoDiskDomainFreeCapacity_Type()
)
hwInfoDiskDomainFreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainFreeCapacity.setStatus("current")
_HwInfoDiskDomainHotSpareCapacity_Type = Counter64
_HwInfoDiskDomainHotSpareCapacity_Object = MibTableColumn
hwInfoDiskDomainHotSpareCapacity = _HwInfoDiskDomainHotSpareCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 7),
    _HwInfoDiskDomainHotSpareCapacity_Type()
)
hwInfoDiskDomainHotSpareCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainHotSpareCapacity.setStatus("current")
_HwInfoDiskDomainUsedHotSpareCapacity_Type = Counter64
_HwInfoDiskDomainUsedHotSpareCapacity_Object = MibTableColumn
hwInfoDiskDomainUsedHotSpareCapacity = _HwInfoDiskDomainUsedHotSpareCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 8),
    _HwInfoDiskDomainUsedHotSpareCapacity_Type()
)
hwInfoDiskDomainUsedHotSpareCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainUsedHotSpareCapacity.setStatus("current")
_HwInfoDiskDomainTier0DiskNumber_Type = Unsigned32
_HwInfoDiskDomainTier0DiskNumber_Object = MibTableColumn
hwInfoDiskDomainTier0DiskNumber = _HwInfoDiskDomainTier0DiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 9),
    _HwInfoDiskDomainTier0DiskNumber_Type()
)
hwInfoDiskDomainTier0DiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainTier0DiskNumber.setStatus("current")
_HwInfoDiskDomainTier0TotalCapacity_Type = Counter64
_HwInfoDiskDomainTier0TotalCapacity_Object = MibTableColumn
hwInfoDiskDomainTier0TotalCapacity = _HwInfoDiskDomainTier0TotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 10),
    _HwInfoDiskDomainTier0TotalCapacity_Type()
)
hwInfoDiskDomainTier0TotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainTier0TotalCapacity.setStatus("current")
_HwInfoDiskDomainTier0FreeCapacity_Type = Counter64
_HwInfoDiskDomainTier0FreeCapacity_Object = MibTableColumn
hwInfoDiskDomainTier0FreeCapacity = _HwInfoDiskDomainTier0FreeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 11),
    _HwInfoDiskDomainTier0FreeCapacity_Type()
)
hwInfoDiskDomainTier0FreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainTier0FreeCapacity.setStatus("current")
_HwInfoDiskDomainTier0HotSpareCapacity_Type = Counter64
_HwInfoDiskDomainTier0HotSpareCapacity_Object = MibTableColumn
hwInfoDiskDomainTier0HotSpareCapacity = _HwInfoDiskDomainTier0HotSpareCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 12),
    _HwInfoDiskDomainTier0HotSpareCapacity_Type()
)
hwInfoDiskDomainTier0HotSpareCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainTier0HotSpareCapacity.setStatus("current")
_HwInfoDiskDomainTier0UsedHotSpareCapacity_Type = Counter64
_HwInfoDiskDomainTier0UsedHotSpareCapacity_Object = MibTableColumn
hwInfoDiskDomainTier0UsedHotSpareCapacity = _HwInfoDiskDomainTier0UsedHotSpareCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 13),
    _HwInfoDiskDomainTier0UsedHotSpareCapacity_Type()
)
hwInfoDiskDomainTier0UsedHotSpareCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainTier0UsedHotSpareCapacity.setStatus("current")
_HwInfoDiskDomainTier0HotSpareStrategy_Type = Unsigned32
_HwInfoDiskDomainTier0HotSpareStrategy_Object = MibTableColumn
hwInfoDiskDomainTier0HotSpareStrategy = _HwInfoDiskDomainTier0HotSpareStrategy_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 1, 1, 14),
    _HwInfoDiskDomainTier0HotSpareStrategy_Type()
)
hwInfoDiskDomainTier0HotSpareStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDomainTier0HotSpareStrategy.setStatus("current")
_HwInfoStoragePoolTable_Object = MibTable
hwInfoStoragePoolTable = _HwInfoStoragePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2)
)
if mibBuilder.loadTexts:
    hwInfoStoragePoolTable.setStatus("current")
_HwInfoStoragePoolEntry_Object = MibTableRow
hwInfoStoragePoolEntry = _HwInfoStoragePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1)
)
hwInfoStoragePoolEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolID"),
)
if mibBuilder.loadTexts:
    hwInfoStoragePoolEntry.setStatus("current")
_HwInfoStoragePoolID_Type = OctetString
_HwInfoStoragePoolID_Object = MibTableColumn
hwInfoStoragePoolID = _HwInfoStoragePoolID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 1),
    _HwInfoStoragePoolID_Type()
)
hwInfoStoragePoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolID.setStatus("current")
_HwInfoStoragePoolName_Type = OctetString
_HwInfoStoragePoolName_Object = MibTableColumn
hwInfoStoragePoolName = _HwInfoStoragePoolName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 2),
    _HwInfoStoragePoolName_Type()
)
hwInfoStoragePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolName.setStatus("current")
_HwInfoStoragePoolDiskDomainID_Type = OctetString
_HwInfoStoragePoolDiskDomainID_Object = MibTableColumn
hwInfoStoragePoolDiskDomainID = _HwInfoStoragePoolDiskDomainID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 3),
    _HwInfoStoragePoolDiskDomainID_Type()
)
hwInfoStoragePoolDiskDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolDiskDomainID.setStatus("current")
_HwInfoStoragePoolDiskDomainName_Type = OctetString
_HwInfoStoragePoolDiskDomainName_Object = MibTableColumn
hwInfoStoragePoolDiskDomainName = _HwInfoStoragePoolDiskDomainName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 4),
    _HwInfoStoragePoolDiskDomainName_Type()
)
hwInfoStoragePoolDiskDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolDiskDomainName.setStatus("current")
_HwInfoStoragePoolHealthStatus_Type = Unsigned32
_HwInfoStoragePoolHealthStatus_Object = MibTableColumn
hwInfoStoragePoolHealthStatus = _HwInfoStoragePoolHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 5),
    _HwInfoStoragePoolHealthStatus_Type()
)
hwInfoStoragePoolHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolHealthStatus.setStatus("current")
_HwInfoStoragePoolRunningStatus_Type = Unsigned32
_HwInfoStoragePoolRunningStatus_Object = MibTableColumn
hwInfoStoragePoolRunningStatus = _HwInfoStoragePoolRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 6),
    _HwInfoStoragePoolRunningStatus_Type()
)
hwInfoStoragePoolRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolRunningStatus.setStatus("current")
_HwInfoStoragePoolTotalCapacity_Type = Counter64
_HwInfoStoragePoolTotalCapacity_Object = MibTableColumn
hwInfoStoragePoolTotalCapacity = _HwInfoStoragePoolTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 7),
    _HwInfoStoragePoolTotalCapacity_Type()
)
hwInfoStoragePoolTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolTotalCapacity.setStatus("current")
_HwInfoStoragePoolSubscribedCapacity_Type = Counter64
_HwInfoStoragePoolSubscribedCapacity_Object = MibTableColumn
hwInfoStoragePoolSubscribedCapacity = _HwInfoStoragePoolSubscribedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 8),
    _HwInfoStoragePoolSubscribedCapacity_Type()
)
hwInfoStoragePoolSubscribedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolSubscribedCapacity.setStatus("current")
_HwInfoStoragePoolFreeCapacity_Type = Counter64
_HwInfoStoragePoolFreeCapacity_Object = MibTableColumn
hwInfoStoragePoolFreeCapacity = _HwInfoStoragePoolFreeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 9),
    _HwInfoStoragePoolFreeCapacity_Type()
)
hwInfoStoragePoolFreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolFreeCapacity.setStatus("current")
_HwInfoStoragePoolTier0Capacity_Type = Counter64
_HwInfoStoragePoolTier0Capacity_Object = MibTableColumn
hwInfoStoragePoolTier0Capacity = _HwInfoStoragePoolTier0Capacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 11),
    _HwInfoStoragePoolTier0Capacity_Type()
)
hwInfoStoragePoolTier0Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolTier0Capacity.setStatus("current")
_HwInfoStoragePoolFullThreshold_Type = Unsigned32
_HwInfoStoragePoolFullThreshold_Object = MibTableColumn
hwInfoStoragePoolFullThreshold = _HwInfoStoragePoolFullThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 2, 1, 14),
    _HwInfoStoragePoolFullThreshold_Type()
)
hwInfoStoragePoolFullThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoStoragePoolFullThreshold.setStatus("current")
_HwInfoPortGroupTable_Object = MibTable
hwInfoPortGroupTable = _HwInfoPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 4)
)
if mibBuilder.loadTexts:
    hwInfoPortGroupTable.setStatus("current")
_HwInfoPortGroupEntry_Object = MibTableRow
hwInfoPortGroupEntry = _HwInfoPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 4, 1)
)
hwInfoPortGroupEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-SPACE-MIB", "hwInfoPortGroupID"),
)
if mibBuilder.loadTexts:
    hwInfoPortGroupEntry.setStatus("current")
_HwInfoPortGroupID_Type = OctetString
_HwInfoPortGroupID_Object = MibTableColumn
hwInfoPortGroupID = _HwInfoPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 4, 1, 1),
    _HwInfoPortGroupID_Type()
)
hwInfoPortGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortGroupID.setStatus("current")
_HwInfoPortGroupName_Type = OctetString
_HwInfoPortGroupName_Object = MibTableColumn
hwInfoPortGroupName = _HwInfoPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 4, 1, 2),
    _HwInfoPortGroupName_Type()
)
hwInfoPortGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortGroupName.setStatus("current")
_HwInfoPortGroupPortList_Type = OctetString
_HwInfoPortGroupPortList_Object = MibTableColumn
hwInfoPortGroupPortList = _HwInfoPortGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 4, 1, 3),
    _HwInfoPortGroupPortList_Type()
)
hwInfoPortGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortGroupPortList.setStatus("current")
_HwInfoHostTable_Object = MibTable
hwInfoHostTable = _HwInfoHostTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5)
)
if mibBuilder.loadTexts:
    hwInfoHostTable.setStatus("current")
_HwInfoHostEntry_Object = MibTableRow
hwInfoHostEntry = _HwInfoHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1)
)
hwInfoHostEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostID"),
)
if mibBuilder.loadTexts:
    hwInfoHostEntry.setStatus("current")
_HwInfoHostID_Type = OctetString
_HwInfoHostID_Object = MibTableColumn
hwInfoHostID = _HwInfoHostID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1, 1),
    _HwInfoHostID_Type()
)
hwInfoHostID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostID.setStatus("current")
_HwInfoHostName_Type = OctetString
_HwInfoHostName_Object = MibTableColumn
hwInfoHostName = _HwInfoHostName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1, 2),
    _HwInfoHostName_Type()
)
hwInfoHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostName.setStatus("current")
_HwInfoHostLocation_Type = OctetString
_HwInfoHostLocation_Object = MibTableColumn
hwInfoHostLocation = _HwInfoHostLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1, 3),
    _HwInfoHostLocation_Type()
)
hwInfoHostLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostLocation.setStatus("current")
_HwInfoHostHealthStatus_Type = Unsigned32
_HwInfoHostHealthStatus_Object = MibTableColumn
hwInfoHostHealthStatus = _HwInfoHostHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1, 4),
    _HwInfoHostHealthStatus_Type()
)
hwInfoHostHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostHealthStatus.setStatus("current")
_HwInfoHostRunningStatus_Type = Unsigned32
_HwInfoHostRunningStatus_Object = MibTableColumn
hwInfoHostRunningStatus = _HwInfoHostRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1, 5),
    _HwInfoHostRunningStatus_Type()
)
hwInfoHostRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostRunningStatus.setStatus("current")
_HwInfoHostOperatingSystem_Type = Unsigned32
_HwInfoHostOperatingSystem_Object = MibTableColumn
hwInfoHostOperatingSystem = _HwInfoHostOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1, 6),
    _HwInfoHostOperatingSystem_Type()
)
hwInfoHostOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostOperatingSystem.setStatus("current")
_HwInfoHostIPAddress_Type = OctetString
_HwInfoHostIPAddress_Object = MibTableColumn
hwInfoHostIPAddress = _HwInfoHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1, 7),
    _HwInfoHostIPAddress_Type()
)
hwInfoHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostIPAddress.setStatus("current")
_HwInfoHostNetworkName_Type = OctetString
_HwInfoHostNetworkName_Object = MibTableColumn
hwInfoHostNetworkName = _HwInfoHostNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1, 8),
    _HwInfoHostNetworkName_Type()
)
hwInfoHostNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostNetworkName.setStatus("current")
_HwInfoHostModel_Type = OctetString
_HwInfoHostModel_Object = MibTableColumn
hwInfoHostModel = _HwInfoHostModel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 5, 1, 9),
    _HwInfoHostModel_Type()
)
hwInfoHostModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostModel.setStatus("current")
_HwInfoHostGroupTable_Object = MibTable
hwInfoHostGroupTable = _HwInfoHostGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 6)
)
if mibBuilder.loadTexts:
    hwInfoHostGroupTable.setStatus("current")
_HwInfoHostGroupEntry_Object = MibTableRow
hwInfoHostGroupEntry = _HwInfoHostGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 6, 1)
)
hwInfoHostGroupEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostGroupID"),
)
if mibBuilder.loadTexts:
    hwInfoHostGroupEntry.setStatus("current")
_HwInfoHostGroupID_Type = OctetString
_HwInfoHostGroupID_Object = MibTableColumn
hwInfoHostGroupID = _HwInfoHostGroupID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 6, 1, 1),
    _HwInfoHostGroupID_Type()
)
hwInfoHostGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostGroupID.setStatus("current")
_HwInfoHostGroupName_Type = OctetString
_HwInfoHostGroupName_Object = MibTableColumn
hwInfoHostGroupName = _HwInfoHostGroupName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 6, 1, 2),
    _HwInfoHostGroupName_Type()
)
hwInfoHostGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostGroupName.setStatus("current")
_HwInfoHostGroupHostList_Type = OctetString
_HwInfoHostGroupHostList_Object = MibTableColumn
hwInfoHostGroupHostList = _HwInfoHostGroupHostList_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 6, 1, 3),
    _HwInfoHostGroupHostList_Type()
)
hwInfoHostGroupHostList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoHostGroupHostList.setStatus("current")
_HwInfoLunGroupTable_Object = MibTable
hwInfoLunGroupTable = _HwInfoLunGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 7)
)
if mibBuilder.loadTexts:
    hwInfoLunGroupTable.setStatus("current")
_HwInfoLunGroupEntry_Object = MibTableRow
hwInfoLunGroupEntry = _HwInfoLunGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 7, 1)
)
hwInfoLunGroupEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunGroupID"),
)
if mibBuilder.loadTexts:
    hwInfoLunGroupEntry.setStatus("current")
_HwInfoLunGroupID_Type = OctetString
_HwInfoLunGroupID_Object = MibTableColumn
hwInfoLunGroupID = _HwInfoLunGroupID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 7, 1, 1),
    _HwInfoLunGroupID_Type()
)
hwInfoLunGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunGroupID.setStatus("current")
_HwInfoLunGroupName_Type = OctetString
_HwInfoLunGroupName_Object = MibTableColumn
hwInfoLunGroupName = _HwInfoLunGroupName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 7, 1, 2),
    _HwInfoLunGroupName_Type()
)
hwInfoLunGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunGroupName.setStatus("current")
_HwInfoLunGroupLunList_Type = OctetString
_HwInfoLunGroupLunList_Object = MibTableColumn
hwInfoLunGroupLunList = _HwInfoLunGroupLunList_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 7, 1, 3),
    _HwInfoLunGroupLunList_Type()
)
hwInfoLunGroupLunList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunGroupLunList.setStatus("current")
_HwInfoLunTable_Object = MibTable
hwInfoLunTable = _HwInfoLunTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8)
)
if mibBuilder.loadTexts:
    hwInfoLunTable.setStatus("current")
_HwInfoLunEntry_Object = MibTableRow
hwInfoLunEntry = _HwInfoLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1)
)
hwInfoLunEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunID"),
)
if mibBuilder.loadTexts:
    hwInfoLunEntry.setStatus("current")
_HwInfoLunID_Type = OctetString
_HwInfoLunID_Object = MibTableColumn
hwInfoLunID = _HwInfoLunID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 1),
    _HwInfoLunID_Type()
)
hwInfoLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunID.setStatus("current")
_HwInfoLunName_Type = OctetString
_HwInfoLunName_Object = MibTableColumn
hwInfoLunName = _HwInfoLunName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 2),
    _HwInfoLunName_Type()
)
hwInfoLunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunName.setStatus("current")
_HwInfoLunPoolID_Type = OctetString
_HwInfoLunPoolID_Object = MibTableColumn
hwInfoLunPoolID = _HwInfoLunPoolID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 3),
    _HwInfoLunPoolID_Type()
)
hwInfoLunPoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunPoolID.setStatus("current")
_HwInfoLunPoolName_Type = OctetString
_HwInfoLunPoolName_Object = MibTableColumn
hwInfoLunPoolName = _HwInfoLunPoolName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 4),
    _HwInfoLunPoolName_Type()
)
hwInfoLunPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunPoolName.setStatus("current")
_HwInfoLunCapacity_Type = Counter64
_HwInfoLunCapacity_Object = MibTableColumn
hwInfoLunCapacity = _HwInfoLunCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 5),
    _HwInfoLunCapacity_Type()
)
hwInfoLunCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunCapacity.setStatus("current")
_HwInfoLunSubscribedCapacity_Type = Counter64
_HwInfoLunSubscribedCapacity_Object = MibTableColumn
hwInfoLunSubscribedCapacity = _HwInfoLunSubscribedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 6),
    _HwInfoLunSubscribedCapacity_Type()
)
hwInfoLunSubscribedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunSubscribedCapacity.setStatus("current")
_HwInfoLunProtectionCapacity_Type = Counter64
_HwInfoLunProtectionCapacity_Object = MibTableColumn
hwInfoLunProtectionCapacity = _HwInfoLunProtectionCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 7),
    _HwInfoLunProtectionCapacity_Type()
)
hwInfoLunProtectionCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunProtectionCapacity.setStatus("current")
_HwInfoLunSectorSize_Type = Unsigned32
_HwInfoLunSectorSize_Object = MibTableColumn
hwInfoLunSectorSize = _HwInfoLunSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 8),
    _HwInfoLunSectorSize_Type()
)
hwInfoLunSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunSectorSize.setStatus("current")
_HwInfoLunHealthStatus_Type = Unsigned32
_HwInfoLunHealthStatus_Object = MibTableColumn
hwInfoLunHealthStatus = _HwInfoLunHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 9),
    _HwInfoLunHealthStatus_Type()
)
hwInfoLunHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunHealthStatus.setStatus("current")
_HwInfoLunRunningStatus_Type = Unsigned32
_HwInfoLunRunningStatus_Object = MibTableColumn
hwInfoLunRunningStatus = _HwInfoLunRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 10),
    _HwInfoLunRunningStatus_Type()
)
hwInfoLunRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunRunningStatus.setStatus("current")
_HwInfoLunType_Type = Unsigned32
_HwInfoLunType_Object = MibTableColumn
hwInfoLunType = _HwInfoLunType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 11),
    _HwInfoLunType_Type()
)
hwInfoLunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunType.setStatus("current")
_HwInfoLunIOPriority_Type = Unsigned32
_HwInfoLunIOPriority_Object = MibTableColumn
hwInfoLunIOPriority = _HwInfoLunIOPriority_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 12),
    _HwInfoLunIOPriority_Type()
)
hwInfoLunIOPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunIOPriority.setStatus("current")
_HwInfoLunWWN_Type = OctetString
_HwInfoLunWWN_Object = MibTableColumn
hwInfoLunWWN = _HwInfoLunWWN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 13),
    _HwInfoLunWWN_Type()
)
hwInfoLunWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunWWN.setStatus("current")
_HwInfoLunExposedToInitiator_Type = Unsigned32
_HwInfoLunExposedToInitiator_Object = MibTableColumn
hwInfoLunExposedToInitiator = _HwInfoLunExposedToInitiator_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 14),
    _HwInfoLunExposedToInitiator_Type()
)
hwInfoLunExposedToInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunExposedToInitiator.setStatus("current")
_HwInfoLunWritePolicy_Type = Unsigned32
_HwInfoLunWritePolicy_Object = MibTableColumn
hwInfoLunWritePolicy = _HwInfoLunWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 15),
    _HwInfoLunWritePolicy_Type()
)
hwInfoLunWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunWritePolicy.setStatus("current")
_HwInfoLunRunningWritePolicy_Type = Unsigned32
_HwInfoLunRunningWritePolicy_Object = MibTableColumn
hwInfoLunRunningWritePolicy = _HwInfoLunRunningWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 16),
    _HwInfoLunRunningWritePolicy_Type()
)
hwInfoLunRunningWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunRunningWritePolicy.setStatus("current")
_HwInfoLunPrefetchPolicy_Type = Unsigned32
_HwInfoLunPrefetchPolicy_Object = MibTableColumn
hwInfoLunPrefetchPolicy = _HwInfoLunPrefetchPolicy_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 17),
    _HwInfoLunPrefetchPolicy_Type()
)
hwInfoLunPrefetchPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunPrefetchPolicy.setStatus("current")
_HwInfoLunPrefetchValue_Type = Unsigned32
_HwInfoLunPrefetchValue_Object = MibTableColumn
hwInfoLunPrefetchValue = _HwInfoLunPrefetchValue_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 20),
    _HwInfoLunPrefetchValue_Type()
)
hwInfoLunPrefetchValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunPrefetchValue.setStatus("current")
_HwInfoLunOwnerController_Type = OctetString
_HwInfoLunOwnerController_Object = MibTableColumn
hwInfoLunOwnerController = _HwInfoLunOwnerController_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 21),
    _HwInfoLunOwnerController_Type()
)
hwInfoLunOwnerController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunOwnerController.setStatus("current")
_HwInfoLunWorkController_Type = OctetString
_HwInfoLunWorkController_Object = MibTableColumn
hwInfoLunWorkController = _HwInfoLunWorkController_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 22),
    _HwInfoLunWorkController_Type()
)
hwInfoLunWorkController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunWorkController.setStatus("current")
_HwInfoLunIsAddToLunGroup_Type = Unsigned32
_HwInfoLunIsAddToLunGroup_Object = MibTableColumn
hwInfoLunIsAddToLunGroup = _HwInfoLunIsAddToLunGroup_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 25),
    _HwInfoLunIsAddToLunGroup_Type()
)
hwInfoLunIsAddToLunGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunIsAddToLunGroup.setStatus("current")
_HwInfoLunDIFSwitch_Type = Unsigned32
_HwInfoLunDIFSwitch_Object = MibTableColumn
hwInfoLunDIFSwitch = _HwInfoLunDIFSwitch_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 26),
    _HwInfoLunDIFSwitch_Type()
)
hwInfoLunDIFSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunDIFSwitch.setStatus("current")
_HwInfoLunRemoteLUNWWN_Type = OctetString
_HwInfoLunRemoteLUNWWN_Object = MibTableColumn
hwInfoLunRemoteLUNWWN = _HwInfoLunRemoteLUNWWN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 27),
    _HwInfoLunRemoteLUNWWN_Type()
)
hwInfoLunRemoteLUNWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunRemoteLUNWWN.setStatus("current")
_HwInfoLunUsageType_Type = Unsigned32
_HwInfoLunUsageType_Object = MibTableColumn
hwInfoLunUsageType = _HwInfoLunUsageType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 4, 8, 1, 28),
    _HwInfoLunUsageType_Type()
)
hwInfoLunUsageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLunUsageType.setStatus("current")
_IsoConformance_ObjectIdentity = ObjectIdentity
isoConformance = _IsoConformance_ObjectIdentity(
    (1, 6)
)
_IsoGroups_ObjectIdentity = ObjectIdentity
isoGroups = _IsoGroups_ObjectIdentity(
    (1, 6, 1)
)
_IsoCompliances_ObjectIdentity = ObjectIdentity
isoCompliances = _IsoCompliances_ObjectIdentity(
    (1, 6, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 6, 1, 1)
)
currentObjectGroup.setObjects(
      *(("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainID"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainHealthStatus"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainRunningStatus"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainTotalCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainFreeCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainHotSpareCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainUsedHotSpareCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainTier0DiskNumber"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainTier0TotalCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainTier0FreeCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainTier0HotSpareCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainTier0UsedHotSpareCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoDiskDomainTier0HotSpareStrategy"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolID"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolDiskDomainID"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolHealthStatus"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolRunningStatus"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolTotalCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolSubscribedCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolFreeCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolTier0Capacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolFullThreshold"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostID"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostLocation"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostHealthStatus"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostRunningStatus"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostOperatingSystem"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostIPAddress"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostModel"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostNetworkName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostGroupID"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostGroupName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunGroupID"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunGroupName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunID"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunPoolID"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunPoolName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunSubscribedCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunProtectionCapacity"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunSectorSize"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunHealthStatus"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunRunningStatus"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunType"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunIOPriority"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunWWN"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunExposedToInitiator"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunWritePolicy"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunRunningWritePolicy"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunPrefetchPolicy"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunPrefetchValue"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunOwnerController"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunWorkController"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunIsAddToLunGroup"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunDIFSwitch"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunRemoteLUNWWN"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoStoragePoolDiskDomainName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoPortGroupID"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoPortGroupName"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoPortGroupPortList"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoHostGroupHostList"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunGroupLunList"),
        ("HUAWEI-STORAGE-SPACE-MIB", "hwInfoLunUsageType"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 6, 2, 1)
)
basicCompliance.setObjects(
    ("HUAWEI-STORAGE-SPACE-MIB", "currentObjectGroup")
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-STORAGE-SPACE-MIB",
    **{"NodeCodeString": NodeCodeString,
       "huaweistorage": huaweistorage,
       "hwStorage": hwStorage,
       "hwISM": hwISM,
       "hwStorageDevice": hwStorageDevice,
       "hwSpaceInfo": hwSpaceInfo,
       "hwInfoDiskDomainTable": hwInfoDiskDomainTable,
       "hwInfoDiskDomainEntry": hwInfoDiskDomainEntry,
       "hwInfoDiskDomainID": hwInfoDiskDomainID,
       "hwInfoDiskDomainName": hwInfoDiskDomainName,
       "hwInfoDiskDomainHealthStatus": hwInfoDiskDomainHealthStatus,
       "hwInfoDiskDomainRunningStatus": hwInfoDiskDomainRunningStatus,
       "hwInfoDiskDomainTotalCapacity": hwInfoDiskDomainTotalCapacity,
       "hwInfoDiskDomainFreeCapacity": hwInfoDiskDomainFreeCapacity,
       "hwInfoDiskDomainHotSpareCapacity": hwInfoDiskDomainHotSpareCapacity,
       "hwInfoDiskDomainUsedHotSpareCapacity": hwInfoDiskDomainUsedHotSpareCapacity,
       "hwInfoDiskDomainTier0DiskNumber": hwInfoDiskDomainTier0DiskNumber,
       "hwInfoDiskDomainTier0TotalCapacity": hwInfoDiskDomainTier0TotalCapacity,
       "hwInfoDiskDomainTier0FreeCapacity": hwInfoDiskDomainTier0FreeCapacity,
       "hwInfoDiskDomainTier0HotSpareCapacity": hwInfoDiskDomainTier0HotSpareCapacity,
       "hwInfoDiskDomainTier0UsedHotSpareCapacity": hwInfoDiskDomainTier0UsedHotSpareCapacity,
       "hwInfoDiskDomainTier0HotSpareStrategy": hwInfoDiskDomainTier0HotSpareStrategy,
       "hwInfoStoragePoolTable": hwInfoStoragePoolTable,
       "hwInfoStoragePoolEntry": hwInfoStoragePoolEntry,
       "hwInfoStoragePoolID": hwInfoStoragePoolID,
       "hwInfoStoragePoolName": hwInfoStoragePoolName,
       "hwInfoStoragePoolDiskDomainID": hwInfoStoragePoolDiskDomainID,
       "hwInfoStoragePoolDiskDomainName": hwInfoStoragePoolDiskDomainName,
       "hwInfoStoragePoolHealthStatus": hwInfoStoragePoolHealthStatus,
       "hwInfoStoragePoolRunningStatus": hwInfoStoragePoolRunningStatus,
       "hwInfoStoragePoolTotalCapacity": hwInfoStoragePoolTotalCapacity,
       "hwInfoStoragePoolSubscribedCapacity": hwInfoStoragePoolSubscribedCapacity,
       "hwInfoStoragePoolFreeCapacity": hwInfoStoragePoolFreeCapacity,
       "hwInfoStoragePoolTier0Capacity": hwInfoStoragePoolTier0Capacity,
       "hwInfoStoragePoolFullThreshold": hwInfoStoragePoolFullThreshold,
       "hwInfoPortGroupTable": hwInfoPortGroupTable,
       "hwInfoPortGroupEntry": hwInfoPortGroupEntry,
       "hwInfoPortGroupID": hwInfoPortGroupID,
       "hwInfoPortGroupName": hwInfoPortGroupName,
       "hwInfoPortGroupPortList": hwInfoPortGroupPortList,
       "hwInfoHostTable": hwInfoHostTable,
       "hwInfoHostEntry": hwInfoHostEntry,
       "hwInfoHostID": hwInfoHostID,
       "hwInfoHostName": hwInfoHostName,
       "hwInfoHostLocation": hwInfoHostLocation,
       "hwInfoHostHealthStatus": hwInfoHostHealthStatus,
       "hwInfoHostRunningStatus": hwInfoHostRunningStatus,
       "hwInfoHostOperatingSystem": hwInfoHostOperatingSystem,
       "hwInfoHostIPAddress": hwInfoHostIPAddress,
       "hwInfoHostNetworkName": hwInfoHostNetworkName,
       "hwInfoHostModel": hwInfoHostModel,
       "hwInfoHostGroupTable": hwInfoHostGroupTable,
       "hwInfoHostGroupEntry": hwInfoHostGroupEntry,
       "hwInfoHostGroupID": hwInfoHostGroupID,
       "hwInfoHostGroupName": hwInfoHostGroupName,
       "hwInfoHostGroupHostList": hwInfoHostGroupHostList,
       "hwInfoLunGroupTable": hwInfoLunGroupTable,
       "hwInfoLunGroupEntry": hwInfoLunGroupEntry,
       "hwInfoLunGroupID": hwInfoLunGroupID,
       "hwInfoLunGroupName": hwInfoLunGroupName,
       "hwInfoLunGroupLunList": hwInfoLunGroupLunList,
       "hwInfoLunTable": hwInfoLunTable,
       "hwInfoLunEntry": hwInfoLunEntry,
       "hwInfoLunID": hwInfoLunID,
       "hwInfoLunName": hwInfoLunName,
       "hwInfoLunPoolID": hwInfoLunPoolID,
       "hwInfoLunPoolName": hwInfoLunPoolName,
       "hwInfoLunCapacity": hwInfoLunCapacity,
       "hwInfoLunSubscribedCapacity": hwInfoLunSubscribedCapacity,
       "hwInfoLunProtectionCapacity": hwInfoLunProtectionCapacity,
       "hwInfoLunSectorSize": hwInfoLunSectorSize,
       "hwInfoLunHealthStatus": hwInfoLunHealthStatus,
       "hwInfoLunRunningStatus": hwInfoLunRunningStatus,
       "hwInfoLunType": hwInfoLunType,
       "hwInfoLunIOPriority": hwInfoLunIOPriority,
       "hwInfoLunWWN": hwInfoLunWWN,
       "hwInfoLunExposedToInitiator": hwInfoLunExposedToInitiator,
       "hwInfoLunWritePolicy": hwInfoLunWritePolicy,
       "hwInfoLunRunningWritePolicy": hwInfoLunRunningWritePolicy,
       "hwInfoLunPrefetchPolicy": hwInfoLunPrefetchPolicy,
       "hwInfoLunPrefetchValue": hwInfoLunPrefetchValue,
       "hwInfoLunOwnerController": hwInfoLunOwnerController,
       "hwInfoLunWorkController": hwInfoLunWorkController,
       "hwInfoLunIsAddToLunGroup": hwInfoLunIsAddToLunGroup,
       "hwInfoLunDIFSwitch": hwInfoLunDIFSwitch,
       "hwInfoLunRemoteLUNWWN": hwInfoLunRemoteLUNWWN,
       "hwInfoLunUsageType": hwInfoLunUsageType,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
