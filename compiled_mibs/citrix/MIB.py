# SNMP MIB module (MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\citrix\MIB

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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

netScaler = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5951)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SdxRoot_ObjectIdentity = ObjectIdentity
sdxRoot = _SdxRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 6)
)
_SdxEventGroup_ObjectIdentity = ObjectIdentity
sdxEventGroup = _SdxEventGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 6, 1)
)
_SystemGroup_ObjectIdentity = ObjectIdentity
systemGroup = _SystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2)
)
_SystemPlatform_Type = OctetString
_SystemPlatform_Object = MibScalar
systemPlatform = _SystemPlatform_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1),
    _SystemPlatform_Type()
)
systemPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPlatform.setStatus("current")
_SystemProduct_Type = OctetString
_SystemProduct_Object = MibScalar
systemProduct = _SystemProduct_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 2),
    _SystemProduct_Type()
)
systemProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProduct.setStatus("current")
_SystemBuildNumber_Type = OctetString
_SystemBuildNumber_Object = MibScalar
systemBuildNumber = _SystemBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 3),
    _SystemBuildNumber_Type()
)
systemBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBuildNumber.setStatus("current")
_SystemSvmIPAddressType_Type = InetAddressType
_SystemSvmIPAddressType_Object = MibScalar
systemSvmIPAddressType = _SystemSvmIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 4),
    _SystemSvmIPAddressType_Type()
)
systemSvmIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSvmIPAddressType.setStatus("current")
_SystemSvmIPAddress_Type = InetAddress
_SystemSvmIPAddress_Object = MibScalar
systemSvmIPAddress = _SystemSvmIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 5),
    _SystemSvmIPAddress_Type()
)
systemSvmIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSvmIPAddress.setStatus("current")
_SystemXenIPAddressType_Type = InetAddressType
_SystemXenIPAddressType_Object = MibScalar
systemXenIPAddressType = _SystemXenIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 6),
    _SystemXenIPAddressType_Type()
)
systemXenIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemXenIPAddressType.setStatus("current")
_SystemXenIPAddress_Type = InetAddress
_SystemXenIPAddress_Object = MibScalar
systemXenIPAddress = _SystemXenIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 7),
    _SystemXenIPAddress_Type()
)
systemXenIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemXenIPAddress.setStatus("current")
_SystemNetmaskType_Type = InetAddressType
_SystemNetmaskType_Object = MibScalar
systemNetmaskType = _SystemNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 8),
    _SystemNetmaskType_Type()
)
systemNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNetmaskType.setStatus("current")
_SystemNetmask_Type = InetAddress
_SystemNetmask_Object = MibScalar
systemNetmask = _SystemNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 9),
    _SystemNetmask_Type()
)
systemNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNetmask.setStatus("current")
_SystemGatewayType_Type = InetAddressType
_SystemGatewayType_Object = MibScalar
systemGatewayType = _SystemGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 10),
    _SystemGatewayType_Type()
)
systemGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemGatewayType.setStatus("current")
_SystemGateway_Type = InetAddress
_SystemGateway_Object = MibScalar
systemGateway = _SystemGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 11),
    _SystemGateway_Type()
)
systemGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemGateway.setStatus("current")
_SystemNetworkInterface_Type = OctetString
_SystemNetworkInterface_Object = MibScalar
systemNetworkInterface = _SystemNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 12),
    _SystemNetworkInterface_Type()
)
systemNetworkInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNetworkInterface.setStatus("current")
_SystemDns_Type = OctetString
_SystemDns_Object = MibScalar
systemDns = _SystemDns_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 13),
    _SystemDns_Type()
)
systemDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDns.setStatus("current")
_SystemSysId_Type = OctetString
_SystemSysId_Object = MibScalar
systemSysId = _SystemSysId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 15),
    _SystemSysId_Type()
)
systemSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSysId.setStatus("current")
_SystemSerial_Type = OctetString
_SystemSerial_Object = MibScalar
systemSerial = _SystemSerial_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 16),
    _SystemSerial_Type()
)
systemSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSerial.setStatus("current")
_SystemCurrentTime_Type = Integer32
_SystemCurrentTime_Object = MibScalar
systemCurrentTime = _SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 17),
    _SystemCurrentTime_Type()
)
systemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCurrentTime.setStatus("current")
_SystemUptime_Type = OctetString
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 18),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_SystemBiosVersion_Type = OctetString
_SystemBiosVersion_Object = MibScalar
systemBiosVersion = _SystemBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 19),
    _SystemBiosVersion_Type()
)
systemBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBiosVersion.setStatus("current")
_SystemMaxThroughput_Type = OctetString
_SystemMaxThroughput_Object = MibScalar
systemMaxThroughput = _SystemMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 20),
    _SystemMaxThroughput_Type()
)
systemMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMaxThroughput.setStatus("current")
_SystemAvailableThroughput_Type = OctetString
_SystemAvailableThroughput_Object = MibScalar
systemAvailableThroughput = _SystemAvailableThroughput_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 21),
    _SystemAvailableThroughput_Type()
)
systemAvailableThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAvailableThroughput.setStatus("current")
_SystemHostId_Type = OctetString
_SystemHostId_Object = MibScalar
systemHostId = _SystemHostId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 22),
    _SystemHostId_Type()
)
systemHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHostId.setStatus("current")
_SystemCustomID_Type = OctetString
_SystemCustomID_Object = MibScalar
systemCustomID = _SystemCustomID_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 23),
    _SystemCustomID_Type()
)
systemCustomID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCustomID.setStatus("current")
_SysHealthGroup_ObjectIdentity = ObjectIdentity
sysHealthGroup = _SysHealthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000)
)
_HardwareResourceTable_Object = MibTable
hardwareResourceTable = _HardwareResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 1)
)
if mibBuilder.loadTexts:
    hardwareResourceTable.setStatus("current")
_HardwareResourceEntry_Object = MibTableRow
hardwareResourceEntry = _HardwareResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 1, 1)
)
hardwareResourceEntry.setIndexNames(
    (0, "MIB", "hardwareResourceName"),
    (0, "MIB", "hardwareResourceHostIPAddressType"),
    (0, "MIB", "hardwareResourceHostIPAddress"),
)
if mibBuilder.loadTexts:
    hardwareResourceEntry.setStatus("current")
_HardwareResourceName_Type = OctetString
_HardwareResourceName_Object = MibTableColumn
hardwareResourceName = _HardwareResourceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 1, 1, 1),
    _HardwareResourceName_Type()
)
hardwareResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareResourceName.setStatus("current")
_HardwareResourceHostIPAddressType_Type = InetAddressType
_HardwareResourceHostIPAddressType_Object = MibTableColumn
hardwareResourceHostIPAddressType = _HardwareResourceHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 1, 1, 2),
    _HardwareResourceHostIPAddressType_Type()
)
hardwareResourceHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareResourceHostIPAddressType.setStatus("current")
_HardwareResourceHostIPAddress_Type = InetAddress
_HardwareResourceHostIPAddress_Object = MibTableColumn
hardwareResourceHostIPAddress = _HardwareResourceHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 1, 1, 3),
    _HardwareResourceHostIPAddress_Type()
)
hardwareResourceHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareResourceHostIPAddress.setStatus("current")
_HardwareResourceCurrentValue_Type = OctetString
_HardwareResourceCurrentValue_Object = MibTableColumn
hardwareResourceCurrentValue = _HardwareResourceCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 1, 1, 4),
    _HardwareResourceCurrentValue_Type()
)
hardwareResourceCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareResourceCurrentValue.setStatus("current")
_HardwareResourceExpectedValue_Type = OctetString
_HardwareResourceExpectedValue_Object = MibTableColumn
hardwareResourceExpectedValue = _HardwareResourceExpectedValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 1, 1, 5),
    _HardwareResourceExpectedValue_Type()
)
hardwareResourceExpectedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareResourceExpectedValue.setStatus("current")
_HardwareResourceUnit_Type = OctetString
_HardwareResourceUnit_Object = MibTableColumn
hardwareResourceUnit = _HardwareResourceUnit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 1, 1, 6),
    _HardwareResourceUnit_Type()
)
hardwareResourceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareResourceUnit.setStatus("current")
_HardwareResourceStatus_Type = OctetString
_HardwareResourceStatus_Object = MibTableColumn
hardwareResourceStatus = _HardwareResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 1, 1, 7),
    _HardwareResourceStatus_Type()
)
hardwareResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareResourceStatus.setStatus("current")
_SoftwareResourceTable_Object = MibTable
softwareResourceTable = _SoftwareResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 2)
)
if mibBuilder.loadTexts:
    softwareResourceTable.setStatus("current")
_SoftwareResourceEntry_Object = MibTableRow
softwareResourceEntry = _SoftwareResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 2, 1)
)
softwareResourceEntry.setIndexNames(
    (0, "MIB", "softwareResourceName"),
    (0, "MIB", "softwareResourceHostIPAddressType"),
    (0, "MIB", "softwareResourceHostIPAddress"),
)
if mibBuilder.loadTexts:
    softwareResourceEntry.setStatus("current")
_SoftwareResourceName_Type = OctetString
_SoftwareResourceName_Object = MibTableColumn
softwareResourceName = _SoftwareResourceName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 2, 1, 1),
    _SoftwareResourceName_Type()
)
softwareResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareResourceName.setStatus("current")
_SoftwareResourceHostIPAddressType_Type = InetAddressType
_SoftwareResourceHostIPAddressType_Object = MibTableColumn
softwareResourceHostIPAddressType = _SoftwareResourceHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 2, 1, 2),
    _SoftwareResourceHostIPAddressType_Type()
)
softwareResourceHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareResourceHostIPAddressType.setStatus("current")
_SoftwareResourceHostIPAddress_Type = InetAddress
_SoftwareResourceHostIPAddress_Object = MibTableColumn
softwareResourceHostIPAddress = _SoftwareResourceHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 2, 1, 3),
    _SoftwareResourceHostIPAddress_Type()
)
softwareResourceHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareResourceHostIPAddress.setStatus("current")
_SoftwareResourceCurrentValue_Type = OctetString
_SoftwareResourceCurrentValue_Object = MibTableColumn
softwareResourceCurrentValue = _SoftwareResourceCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 2, 1, 4),
    _SoftwareResourceCurrentValue_Type()
)
softwareResourceCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareResourceCurrentValue.setStatus("current")
_SoftwareResourceExpectedValue_Type = OctetString
_SoftwareResourceExpectedValue_Object = MibTableColumn
softwareResourceExpectedValue = _SoftwareResourceExpectedValue_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 2, 1, 5),
    _SoftwareResourceExpectedValue_Type()
)
softwareResourceExpectedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareResourceExpectedValue.setStatus("current")
_SoftwareResourceUnit_Type = OctetString
_SoftwareResourceUnit_Object = MibTableColumn
softwareResourceUnit = _SoftwareResourceUnit_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 2, 1, 6),
    _SoftwareResourceUnit_Type()
)
softwareResourceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareResourceUnit.setStatus("current")
_SoftwareResourceStatus_Type = OctetString
_SoftwareResourceStatus_Object = MibTableColumn
softwareResourceStatus = _SoftwareResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 2, 1, 7),
    _SoftwareResourceStatus_Type()
)
softwareResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareResourceStatus.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1)
)
diskEntry.setIndexNames(
    (0, "MIB", "diskName"),
    (0, "MIB", "diskHostIPAddressType"),
    (0, "MIB", "diskHostIPAddress"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")
_DiskName_Type = OctetString
_DiskName_Object = MibTableColumn
diskName = _DiskName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 1),
    _DiskName_Type()
)
diskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskName.setStatus("current")
_DiskHostIPAddressType_Type = InetAddressType
_DiskHostIPAddressType_Object = MibTableColumn
diskHostIPAddressType = _DiskHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 2),
    _DiskHostIPAddressType_Type()
)
diskHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskHostIPAddressType.setStatus("current")
_DiskHostIPAddress_Type = InetAddress
_DiskHostIPAddress_Object = MibTableColumn
diskHostIPAddress = _DiskHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 3),
    _DiskHostIPAddress_Type()
)
diskHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskHostIPAddress.setStatus("current")
_DiskTransactionRate_Type = OctetString
_DiskTransactionRate_Object = MibTableColumn
diskTransactionRate = _DiskTransactionRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 4),
    _DiskTransactionRate_Type()
)
diskTransactionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTransactionRate.setStatus("current")
_DiskBlockReadRate_Type = OctetString
_DiskBlockReadRate_Object = MibTableColumn
diskBlockReadRate = _DiskBlockReadRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 5),
    _DiskBlockReadRate_Type()
)
diskBlockReadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBlockReadRate.setStatus("current")
_DiskBlockWriteRate_Type = OctetString
_DiskBlockWriteRate_Object = MibTableColumn
diskBlockWriteRate = _DiskBlockWriteRate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 6),
    _DiskBlockWriteRate_Type()
)
diskBlockWriteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBlockWriteRate.setStatus("current")
_DiskTotalBlocksRead_Type = OctetString
_DiskTotalBlocksRead_Object = MibTableColumn
diskTotalBlocksRead = _DiskTotalBlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 7),
    _DiskTotalBlocksRead_Type()
)
diskTotalBlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalBlocksRead.setStatus("current")
_DiskTotalBlocksWritten_Type = OctetString
_DiskTotalBlocksWritten_Object = MibTableColumn
diskTotalBlocksWritten = _DiskTotalBlocksWritten_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 8),
    _DiskTotalBlocksWritten_Type()
)
diskTotalBlocksWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalBlocksWritten.setStatus("current")
_DiskUtilized_Type = OctetString
_DiskUtilized_Object = MibTableColumn
diskUtilized = _DiskUtilized_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 9),
    _DiskUtilized_Type()
)
diskUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskUtilized.setStatus("current")
_DiskSize_Type = OctetString
_DiskSize_Object = MibTableColumn
diskSize = _DiskSize_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 10),
    _DiskSize_Type()
)
diskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSize.setStatus("current")
_DiskBayNumber_Type = OctetString
_DiskBayNumber_Object = MibTableColumn
diskBayNumber = _DiskBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 3, 1, 11),
    _DiskBayNumber_Type()
)
diskBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBayNumber.setStatus("current")
_SrTable_Object = MibTable
srTable = _SrTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 4)
)
if mibBuilder.loadTexts:
    srTable.setStatus("current")
_SrEntry_Object = MibTableRow
srEntry = _SrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 4, 1)
)
srEntry.setIndexNames(
    (0, "MIB", "srName"),
    (0, "MIB", "srBayNumber"),
    (0, "MIB", "srHostIPAddressType"),
    (0, "MIB", "srHostIPAddress"),
)
if mibBuilder.loadTexts:
    srEntry.setStatus("current")
_SrName_Type = OctetString
_SrName_Object = MibTableColumn
srName = _SrName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 4, 1, 1),
    _SrName_Type()
)
srName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srName.setStatus("current")
_SrBayNumber_Type = OctetString
_SrBayNumber_Object = MibTableColumn
srBayNumber = _SrBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 4, 1, 2),
    _SrBayNumber_Type()
)
srBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srBayNumber.setStatus("current")
_SrHostIPAddressType_Type = InetAddressType
_SrHostIPAddressType_Object = MibTableColumn
srHostIPAddressType = _SrHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 4, 1, 3),
    _SrHostIPAddressType_Type()
)
srHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srHostIPAddressType.setStatus("current")
_SrHostIPAddress_Type = InetAddress
_SrHostIPAddress_Object = MibTableColumn
srHostIPAddress = _SrHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 4, 1, 4),
    _SrHostIPAddress_Type()
)
srHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srHostIPAddress.setStatus("current")
_SrUtilized_Type = OctetString
_SrUtilized_Object = MibTableColumn
srUtilized = _SrUtilized_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 4, 1, 5),
    _SrUtilized_Type()
)
srUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srUtilized.setStatus("current")
_SrSize_Type = OctetString
_SrSize_Object = MibTableColumn
srSize = _SrSize_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 4, 1, 6),
    _SrSize_Type()
)
srSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srSize.setStatus("current")
_SrStatus_Type = OctetString
_SrStatus_Object = MibTableColumn
srStatus = _SrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 4, 1, 7),
    _SrStatus_Type()
)
srStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srStatus.setStatus("current")
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("current")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1)
)
interfaceEntry.setIndexNames(
    (0, "MIB", "interfaceMappedPort"),
    (0, "MIB", "interfaceHostIPAddressType"),
    (0, "MIB", "interfaceHostIPAddress"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("current")
_InterfacePort_Type = OctetString
_InterfacePort_Object = MibTableColumn
interfacePort = _InterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 1),
    _InterfacePort_Type()
)
interfacePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacePort.setStatus("current")
_InterfaceHostIPAddressType_Type = InetAddressType
_InterfaceHostIPAddressType_Object = MibTableColumn
interfaceHostIPAddressType = _InterfaceHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 2),
    _InterfaceHostIPAddressType_Type()
)
interfaceHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHostIPAddressType.setStatus("current")
_InterfaceHostIPAddress_Type = InetAddress
_InterfaceHostIPAddress_Object = MibTableColumn
interfaceHostIPAddress = _InterfaceHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 3),
    _InterfaceHostIPAddress_Type()
)
interfaceHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHostIPAddress.setStatus("current")
_InterfaceState_Type = OctetString
_InterfaceState_Object = MibTableColumn
interfaceState = _InterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 4),
    _InterfaceState_Type()
)
interfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceState.setStatus("current")
_InterfaceRxPackets_Type = OctetString
_InterfaceRxPackets_Object = MibTableColumn
interfaceRxPackets = _InterfaceRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 5),
    _InterfaceRxPackets_Type()
)
interfaceRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPackets.setStatus("current")
_InterfaceTxPackets_Type = OctetString
_InterfaceTxPackets_Object = MibTableColumn
interfaceTxPackets = _InterfaceTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 6),
    _InterfaceTxPackets_Type()
)
interfaceTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPackets.setStatus("current")
_InterfaceRxBytes_Type = OctetString
_InterfaceRxBytes_Object = MibTableColumn
interfaceRxBytes = _InterfaceRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 7),
    _InterfaceRxBytes_Type()
)
interfaceRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxBytes.setStatus("current")
_InterfaceTxBytes_Type = OctetString
_InterfaceTxBytes_Object = MibTableColumn
interfaceTxBytes = _InterfaceTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 8),
    _InterfaceTxBytes_Type()
)
interfaceTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxBytes.setStatus("current")
_InterfaceRxErrors_Type = OctetString
_InterfaceRxErrors_Object = MibTableColumn
interfaceRxErrors = _InterfaceRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 9),
    _InterfaceRxErrors_Type()
)
interfaceRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxErrors.setStatus("current")
_InterfaceTxErrors_Type = OctetString
_InterfaceTxErrors_Object = MibTableColumn
interfaceTxErrors = _InterfaceTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 10),
    _InterfaceTxErrors_Type()
)
interfaceTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxErrors.setStatus("current")
_InterfaceVfTotal_Type = Integer32
_InterfaceVfTotal_Object = MibTableColumn
interfaceVfTotal = _InterfaceVfTotal_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 11),
    _InterfaceVfTotal_Type()
)
interfaceVfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceVfTotal.setStatus("current")
_InterfaceVfAssigned_Type = Integer32
_InterfaceVfAssigned_Object = MibTableColumn
interfaceVfAssigned = _InterfaceVfAssigned_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 12),
    _InterfaceVfAssigned_Type()
)
interfaceVfAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceVfAssigned.setStatus("current")
_InterfaceMappedPort_Type = OctetString
_InterfaceMappedPort_Object = MibTableColumn
interfaceMappedPort = _InterfaceMappedPort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 2, 1000, 5, 1, 13),
    _InterfaceMappedPort_Type()
)
interfaceMappedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMappedPort.setStatus("current")
_DeviceGroup_ObjectIdentity = ObjectIdentity
deviceGroup = _DeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3)
)
_XenTable_Object = MibTable
xenTable = _XenTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1)
)
if mibBuilder.loadTexts:
    xenTable.setStatus("current")
_XenEntry_Object = MibTableRow
xenEntry = _XenEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1)
)
xenEntry.setIndexNames(
    (0, "MIB", "xenIpAddressType"),
    (0, "MIB", "xenIpAddress"),
)
if mibBuilder.loadTexts:
    xenEntry.setStatus("current")
_XenIpAddressType_Type = InetAddressType
_XenIpAddressType_Object = MibTableColumn
xenIpAddressType = _XenIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 1),
    _XenIpAddressType_Type()
)
xenIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenIpAddressType.setStatus("current")
_XenIpAddress_Type = InetAddress
_XenIpAddress_Object = MibTableColumn
xenIpAddress = _XenIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 2),
    _XenIpAddress_Type()
)
xenIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenIpAddress.setStatus("current")
_XenHostname_Type = OctetString
_XenHostname_Object = MibTableColumn
xenHostname = _XenHostname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 3),
    _XenHostname_Type()
)
xenHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenHostname.setStatus("current")
_XenDescription_Type = OctetString
_XenDescription_Object = MibTableColumn
xenDescription = _XenDescription_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 4),
    _XenDescription_Type()
)
xenDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenDescription.setStatus("current")
_XenVersion_Type = OctetString
_XenVersion_Object = MibTableColumn
xenVersion = _XenVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 5),
    _XenVersion_Type()
)
xenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenVersion.setStatus("current")
_XenUuid_Type = OctetString
_XenUuid_Object = MibTableColumn
xenUuid = _XenUuid_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 6),
    _XenUuid_Type()
)
xenUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenUuid.setStatus("current")
_XenNumberOfCPU_Type = Integer32
_XenNumberOfCPU_Object = MibTableColumn
xenNumberOfCPU = _XenNumberOfCPU_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 7),
    _XenNumberOfCPU_Type()
)
xenNumberOfCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenNumberOfCPU.setStatus("current")
_XenCpuUsage_Type = OctetString
_XenCpuUsage_Object = MibTableColumn
xenCpuUsage = _XenCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 8),
    _XenCpuUsage_Type()
)
xenCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenCpuUsage.setStatus("current")
_XenMemoryTotal_Type = OctetString
_XenMemoryTotal_Object = MibTableColumn
xenMemoryTotal = _XenMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 9),
    _XenMemoryTotal_Type()
)
xenMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenMemoryTotal.setStatus("current")
_XenMemoryFree_Type = OctetString
_XenMemoryFree_Object = MibTableColumn
xenMemoryFree = _XenMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 10),
    _XenMemoryFree_Type()
)
xenMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenMemoryFree.setStatus("current")
_XenMemoryUsage_Type = OctetString
_XenMemoryUsage_Object = MibTableColumn
xenMemoryUsage = _XenMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 11),
    _XenMemoryUsage_Type()
)
xenMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenMemoryUsage.setStatus("current")
_XenTx_Type = OctetString
_XenTx_Object = MibTableColumn
xenTx = _XenTx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 12),
    _XenTx_Type()
)
xenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenTx.setStatus("current")
_XenRx_Type = OctetString
_XenRx_Object = MibTableColumn
xenRx = _XenRx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 13),
    _XenRx_Type()
)
xenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenRx.setStatus("current")
_XenUptime_Type = OctetString
_XenUptime_Object = MibTableColumn
xenUptime = _XenUptime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 14),
    _XenUptime_Type()
)
xenUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenUptime.setStatus("current")
_XenSslCoresTotal_Type = Integer32
_XenSslCoresTotal_Object = MibTableColumn
xenSslCoresTotal = _XenSslCoresTotal_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 15),
    _XenSslCoresTotal_Type()
)
xenSslCoresTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenSslCoresTotal.setStatus("current")
_XenIscsiIQN_Type = OctetString
_XenIscsiIQN_Object = MibTableColumn
xenIscsiIQN = _XenIscsiIQN_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 16),
    _XenIscsiIQN_Type()
)
xenIscsiIQN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenIscsiIQN.setStatus("current")
_XenEdition_Type = OctetString
_XenEdition_Object = MibTableColumn
xenEdition = _XenEdition_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 17),
    _XenEdition_Type()
)
xenEdition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenEdition.setStatus("current")
_XenExpiry_Type = OctetString
_XenExpiry_Object = MibTableColumn
xenExpiry = _XenExpiry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 18),
    _XenExpiry_Type()
)
xenExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenExpiry.setStatus("current")
_XenProductCode_Type = OctetString
_XenProductCode_Object = MibTableColumn
xenProductCode = _XenProductCode_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 19),
    _XenProductCode_Type()
)
xenProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenProductCode.setStatus("current")
_XenSerialNumber_Type = OctetString
_XenSerialNumber_Object = MibTableColumn
xenSerialNumber = _XenSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 20),
    _XenSerialNumber_Type()
)
xenSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenSerialNumber.setStatus("current")
_XenVersionLong_Type = OctetString
_XenVersionLong_Object = MibTableColumn
xenVersionLong = _XenVersionLong_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 21),
    _XenVersionLong_Type()
)
xenVersionLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenVersionLong.setStatus("current")
_XenVersionShort_Type = OctetString
_XenVersionShort_Object = MibTableColumn
xenVersionShort = _XenVersionShort_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 22),
    _XenVersionShort_Type()
)
xenVersionShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenVersionShort.setStatus("current")
_XenBuildNumber_Type = OctetString
_XenBuildNumber_Object = MibTableColumn
xenBuildNumber = _XenBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 23),
    _XenBuildNumber_Type()
)
xenBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenBuildNumber.setStatus("current")
_XenBuildDate_Type = OctetString
_XenBuildDate_Object = MibTableColumn
xenBuildDate = _XenBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 1, 1, 24),
    _XenBuildDate_Type()
)
xenBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xenBuildDate.setStatus("current")
_NetscalerTable_Object = MibTable
netscalerTable = _NetscalerTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2)
)
if mibBuilder.loadTexts:
    netscalerTable.setStatus("current")
_NetscalerEntry_Object = MibTableRow
netscalerEntry = _NetscalerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1)
)
netscalerEntry.setIndexNames(
    (0, "MIB", "nsIpAddressType"),
    (0, "MIB", "nsIpAddress"),
    (0, "MIB", "nsHostIPAddressType"),
    (0, "MIB", "nsHostIPAddress"),
)
if mibBuilder.loadTexts:
    netscalerEntry.setStatus("current")
_NsIpAddressType_Type = InetAddressType
_NsIpAddressType_Object = MibTableColumn
nsIpAddressType = _NsIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 1),
    _NsIpAddressType_Type()
)
nsIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpAddressType.setStatus("current")
_NsIpAddress_Type = InetAddress
_NsIpAddress_Object = MibTableColumn
nsIpAddress = _NsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 2),
    _NsIpAddress_Type()
)
nsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIpAddress.setStatus("current")
_NsHostIPAddressType_Type = InetAddressType
_NsHostIPAddressType_Object = MibTableColumn
nsHostIPAddressType = _NsHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 3),
    _NsHostIPAddressType_Type()
)
nsHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHostIPAddressType.setStatus("current")
_NsHostIPAddress_Type = InetAddress
_NsHostIPAddress_Object = MibTableColumn
nsHostIPAddress = _NsHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 4),
    _NsHostIPAddress_Type()
)
nsHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHostIPAddress.setStatus("current")
_NsProfileName_Type = OctetString
_NsProfileName_Object = MibTableColumn
nsProfileName = _NsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 5),
    _NsProfileName_Type()
)
nsProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsProfileName.setStatus("current")
_NsName_Type = OctetString
_NsName_Object = MibTableColumn
nsName = _NsName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 6),
    _NsName_Type()
)
nsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsName.setStatus("current")
_NsNetmaskType_Type = InetAddressType
_NsNetmaskType_Object = MibTableColumn
nsNetmaskType = _NsNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 7),
    _NsNetmaskType_Type()
)
nsNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNetmaskType.setStatus("current")
_NsNetmask_Type = InetAddress
_NsNetmask_Object = MibTableColumn
nsNetmask = _NsNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 8),
    _NsNetmask_Type()
)
nsNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNetmask.setStatus("current")
_NsGatewayType_Type = InetAddressType
_NsGatewayType_Object = MibTableColumn
nsGatewayType = _NsGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 9),
    _NsGatewayType_Type()
)
nsGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsGatewayType.setStatus("current")
_NsGateway_Type = InetAddress
_NsGateway_Object = MibTableColumn
nsGateway = _NsGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 10),
    _NsGateway_Type()
)
nsGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsGateway.setStatus("current")
_NsHostname_Type = OctetString
_NsHostname_Object = MibTableColumn
nsHostname = _NsHostname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 11),
    _NsHostname_Type()
)
nsHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHostname.setStatus("current")
_NsDescription_Type = OctetString
_NsDescription_Object = MibTableColumn
nsDescription = _NsDescription_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 12),
    _NsDescription_Type()
)
nsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsDescription.setStatus("current")
_NsVersion_Type = OctetString
_NsVersion_Object = MibTableColumn
nsVersion = _NsVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 13),
    _NsVersion_Type()
)
nsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVersion.setStatus("current")
_NsUuid_Type = OctetString
_NsUuid_Object = MibTableColumn
nsUuid = _NsUuid_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 14),
    _NsUuid_Type()
)
nsUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsUuid.setStatus("current")
_NsInstanceState_Type = OctetString
_NsInstanceState_Object = MibTableColumn
nsInstanceState = _NsInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 15),
    _NsInstanceState_Type()
)
nsInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsInstanceState.setStatus("current")
_NsVirtualFunctions_Type = OctetString
_NsVirtualFunctions_Object = MibTableColumn
nsVirtualFunctions = _NsVirtualFunctions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 16),
    _NsVirtualFunctions_Type()
)
nsVirtualFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVirtualFunctions.setStatus("current")
_NsSslVirtualFunctions_Type = OctetString
_NsSslVirtualFunctions_Object = MibTableColumn
nsSslVirtualFunctions = _NsSslVirtualFunctions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 17),
    _NsSslVirtualFunctions_Type()
)
nsSslVirtualFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSslVirtualFunctions.setStatus("current")
_NsVmState_Type = OctetString
_NsVmState_Object = MibTableColumn
nsVmState = _NsVmState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 18),
    _NsVmState_Type()
)
nsVmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVmState.setStatus("current")
_NsNumberOfCPU_Type = Integer32
_NsNumberOfCPU_Object = MibTableColumn
nsNumberOfCPU = _NsNumberOfCPU_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 19),
    _NsNumberOfCPU_Type()
)
nsNumberOfCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNumberOfCPU.setStatus("current")
_NsVmMemoryTotal_Type = OctetString
_NsVmMemoryTotal_Object = MibTableColumn
nsVmMemoryTotal = _NsVmMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 21),
    _NsVmMemoryTotal_Type()
)
nsVmMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVmMemoryTotal.setStatus("current")
_NsUptime_Type = OctetString
_NsUptime_Object = MibTableColumn
nsUptime = _NsUptime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 26),
    _NsUptime_Type()
)
nsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsUptime.setStatus("current")
_NsNumberOfSSLCores_Type = Integer32
_NsNumberOfSSLCores_Object = MibTableColumn
nsNumberOfSSLCores = _NsNumberOfSSLCores_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 27),
    _NsNumberOfSSLCores_Type()
)
nsNumberOfSSLCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNumberOfSSLCores.setStatus("current")
_NsCpuCoreMgmt_Type = OctetString
_NsCpuCoreMgmt_Object = MibTableColumn
nsCpuCoreMgmt = _NsCpuCoreMgmt_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 28),
    _NsCpuCoreMgmt_Type()
)
nsCpuCoreMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCpuCoreMgmt.setStatus("current")
_NsCpuCorePE_Type = OctetString
_NsCpuCorePE_Object = MibTableColumn
nsCpuCorePE = _NsCpuCorePE_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 29),
    _NsCpuCorePE_Type()
)
nsCpuCorePE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCpuCorePE.setStatus("current")
_NsVmDescription_Type = OctetString
_NsVmDescription_Object = MibTableColumn
nsVmDescription = _NsVmDescription_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 30),
    _NsVmDescription_Type()
)
nsVmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVmDescription.setStatus("current")
_NsThroughput_Type = OctetString
_NsThroughput_Object = MibTableColumn
nsThroughput = _NsThroughput_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 31),
    _NsThroughput_Type()
)
nsThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsThroughput.setStatus("current")
_NsNumberOfCores_Type = Integer32
_NsNumberOfCores_Object = MibTableColumn
nsNumberOfCores = _NsNumberOfCores_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 32),
    _NsNumberOfCores_Type()
)
nsNumberOfCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNumberOfCores.setStatus("current")
_NsNsCPUUsage_Type = OctetString
_NsNsCPUUsage_Object = MibTableColumn
nsNsCPUUsage = _NsNsCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 33),
    _NsNsCPUUsage_Type()
)
nsNsCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsCPUUsage.setStatus("current")
_NsNsMemoryUsage_Type = OctetString
_NsNsMemoryUsage_Object = MibTableColumn
nsNsMemoryUsage = _NsNsMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 35),
    _NsNsMemoryUsage_Type()
)
nsNsMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsMemoryUsage.setStatus("current")
_NsNsTx_Type = OctetString
_NsNsTx_Object = MibTableColumn
nsNsTx = _NsNsTx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 36),
    _NsNsTx_Type()
)
nsNsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsTx.setStatus("current")
_NsNsRx_Type = OctetString
_NsNsRx_Object = MibTableColumn
nsNsRx = _NsNsRx_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 37),
    _NsNsRx_Type()
)
nsNsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsRx.setStatus("current")
_NsHttpReq_Type = OctetString
_NsHttpReq_Object = MibTableColumn
nsHttpReq = _NsHttpReq_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 38),
    _NsHttpReq_Type()
)
nsHttpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHttpReq.setStatus("current")
_NsUpsince_Type = OctetString
_NsUpsince_Object = MibTableColumn
nsUpsince = _NsUpsince_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 39),
    _NsUpsince_Type()
)
nsUpsince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsUpsince.setStatus("current")
_NsLicense_Type = OctetString
_NsLicense_Object = MibTableColumn
nsLicense = _NsLicense_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 40),
    _NsLicense_Type()
)
nsLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsLicense.setStatus("current")
_NsHaMasterState_Type = OctetString
_NsHaMasterState_Object = MibTableColumn
nsHaMasterState = _NsHaMasterState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 41),
    _NsHaMasterState_Type()
)
nsHaMasterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHaMasterState.setStatus("current")
_NsHaIPAddressType_Type = InetAddressType
_NsHaIPAddressType_Object = MibTableColumn
nsHaIPAddressType = _NsHaIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 42),
    _NsHaIPAddressType_Type()
)
nsHaIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHaIPAddressType.setStatus("current")
_NsHaIPAddress_Type = InetAddress
_NsHaIPAddress_Object = MibTableColumn
nsHaIPAddress = _NsHaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 43),
    _NsHaIPAddress_Type()
)
nsHaIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHaIPAddress.setStatus("current")
_NsNodeState_Type = OctetString
_NsNodeState_Object = MibTableColumn
nsNodeState = _NsNodeState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 44),
    _NsNodeState_Type()
)
nsNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNodeState.setStatus("current")
_NsHaSync_Type = OctetString
_NsHaSync_Object = MibTableColumn
nsHaSync = _NsHaSync_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 45),
    _NsHaSync_Type()
)
nsHaSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsHaSync.setStatus("current")
_NsPps_Type = OctetString
_NsPps_Object = MibTableColumn
nsPps = _NsPps_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 46),
    _NsPps_Type()
)
nsPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsPps.setStatus("current")
_NsNumberOfSslCoresUp_Type = Integer32
_NsNumberOfSslCoresUp_Object = MibTableColumn
nsNumberOfSslCoresUp = _NsNumberOfSslCoresUp_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 47),
    _NsNumberOfSslCoresUp_Type()
)
nsNumberOfSslCoresUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNumberOfSslCoresUp.setStatus("current")
_NsIfOby1_Type = OctetString
_NsIfOby1_Object = MibTableColumn
nsIfOby1 = _NsIfOby1_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 48),
    _NsIfOby1_Type()
)
nsIfOby1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfOby1.setStatus("current")
_NsIf0by2_Type = OctetString
_NsIf0by2_Object = MibTableColumn
nsIf0by2 = _NsIf0by2_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 49),
    _NsIf0by2_Type()
)
nsIf0by2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIf0by2.setStatus("current")
_NsNsVLANId_Type = Integer32
_NsNsVLANId_Object = MibTableColumn
nsNsVLANId = _NsNsVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 50),
    _NsNsVLANId_Type()
)
nsNsVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsVLANId.setStatus("current")
_NsNsVLANTagged_Type = OctetString
_NsNsVLANTagged_Object = MibTableColumn
nsNsVLANTagged = _NsNsVLANTagged_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 51),
    _NsNsVLANTagged_Type()
)
nsNsVLANTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNsVLANTagged.setStatus("current")
_NsVlanType_Type = Integer32
_NsVlanType_Object = MibTableColumn
nsVlanType = _NsVlanType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 2, 1, 52),
    _NsVlanType_Type()
)
nsVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVlanType.setStatus("current")
_CloudBridgeInstanceTable_Object = MibTable
cloudBridgeInstanceTable = _CloudBridgeInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3)
)
if mibBuilder.loadTexts:
    cloudBridgeInstanceTable.setStatus("current")
_CloudBridgeInstanceEntry_Object = MibTableRow
cloudBridgeInstanceEntry = _CloudBridgeInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1)
)
cloudBridgeInstanceEntry.setIndexNames(
    (0, "MIB", "cbIpAddressType"),
    (0, "MIB", "cbIpAddress"),
    (0, "MIB", "cbHostIPAddressType"),
    (0, "MIB", "cbHostIPAddress"),
)
if mibBuilder.loadTexts:
    cloudBridgeInstanceEntry.setStatus("current")
_CbIpAddressType_Type = InetAddressType
_CbIpAddressType_Object = MibTableColumn
cbIpAddressType = _CbIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 1),
    _CbIpAddressType_Type()
)
cbIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbIpAddressType.setStatus("current")
_CbIpAddress_Type = InetAddress
_CbIpAddress_Object = MibTableColumn
cbIpAddress = _CbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 2),
    _CbIpAddress_Type()
)
cbIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbIpAddress.setStatus("current")
_CbHostIPAddressType_Type = InetAddressType
_CbHostIPAddressType_Object = MibTableColumn
cbHostIPAddressType = _CbHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 3),
    _CbHostIPAddressType_Type()
)
cbHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbHostIPAddressType.setStatus("current")
_CbHostIPAddress_Type = InetAddress
_CbHostIPAddress_Object = MibTableColumn
cbHostIPAddress = _CbHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 4),
    _CbHostIPAddress_Type()
)
cbHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbHostIPAddress.setStatus("current")
_CbProfileName_Type = OctetString
_CbProfileName_Object = MibTableColumn
cbProfileName = _CbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 5),
    _CbProfileName_Type()
)
cbProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbProfileName.setStatus("current")
_CbName_Type = OctetString
_CbName_Object = MibTableColumn
cbName = _CbName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 6),
    _CbName_Type()
)
cbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbName.setStatus("current")
_CbNetmaskType_Type = InetAddressType
_CbNetmaskType_Object = MibTableColumn
cbNetmaskType = _CbNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 7),
    _CbNetmaskType_Type()
)
cbNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbNetmaskType.setStatus("current")
_CbNetmask_Type = InetAddress
_CbNetmask_Object = MibTableColumn
cbNetmask = _CbNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 8),
    _CbNetmask_Type()
)
cbNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbNetmask.setStatus("current")
_CbGatewayType_Type = InetAddressType
_CbGatewayType_Object = MibTableColumn
cbGatewayType = _CbGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 9),
    _CbGatewayType_Type()
)
cbGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbGatewayType.setStatus("current")
_CbGateway_Type = InetAddress
_CbGateway_Object = MibTableColumn
cbGateway = _CbGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 10),
    _CbGateway_Type()
)
cbGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbGateway.setStatus("current")
_CbHostname_Type = OctetString
_CbHostname_Object = MibTableColumn
cbHostname = _CbHostname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 11),
    _CbHostname_Type()
)
cbHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbHostname.setStatus("current")
_CbDescription_Type = OctetString
_CbDescription_Object = MibTableColumn
cbDescription = _CbDescription_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 12),
    _CbDescription_Type()
)
cbDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbDescription.setStatus("current")
_CbVersion_Type = OctetString
_CbVersion_Object = MibTableColumn
cbVersion = _CbVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 13),
    _CbVersion_Type()
)
cbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVersion.setStatus("current")
_CbInstanceState_Type = OctetString
_CbInstanceState_Object = MibTableColumn
cbInstanceState = _CbInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 14),
    _CbInstanceState_Type()
)
cbInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbInstanceState.setStatus("current")
_CbUuid_Type = OctetString
_CbUuid_Object = MibTableColumn
cbUuid = _CbUuid_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 15),
    _CbUuid_Type()
)
cbUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbUuid.setStatus("current")
_CbVirtualFunctions_Type = OctetString
_CbVirtualFunctions_Object = MibTableColumn
cbVirtualFunctions = _CbVirtualFunctions_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 16),
    _CbVirtualFunctions_Type()
)
cbVirtualFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVirtualFunctions.setStatus("current")
_CbVmState_Type = OctetString
_CbVmState_Object = MibTableColumn
cbVmState = _CbVmState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 17),
    _CbVmState_Type()
)
cbVmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmState.setStatus("current")
_CbNumberOfCPU_Type = Integer32
_CbNumberOfCPU_Object = MibTableColumn
cbNumberOfCPU = _CbNumberOfCPU_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 18),
    _CbNumberOfCPU_Type()
)
cbNumberOfCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbNumberOfCPU.setStatus("current")
_CbVmCPUUsage_Type = OctetString
_CbVmCPUUsage_Object = MibTableColumn
cbVmCPUUsage = _CbVmCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 19),
    _CbVmCPUUsage_Type()
)
cbVmCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmCPUUsage.setStatus("current")
_CbVmMemoryTotal_Type = OctetString
_CbVmMemoryTotal_Object = MibTableColumn
cbVmMemoryTotal = _CbVmMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 20),
    _CbVmMemoryTotal_Type()
)
cbVmMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmMemoryTotal.setStatus("current")
_CbVmMemoryFree_Type = OctetString
_CbVmMemoryFree_Object = MibTableColumn
cbVmMemoryFree = _CbVmMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 21),
    _CbVmMemoryFree_Type()
)
cbVmMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmMemoryFree.setStatus("current")
_CbVmMemoryUsage_Type = OctetString
_CbVmMemoryUsage_Object = MibTableColumn
cbVmMemoryUsage = _CbVmMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 22),
    _CbVmMemoryUsage_Type()
)
cbVmMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbVmMemoryUsage.setStatus("current")
_CbUptime_Type = OctetString
_CbUptime_Object = MibTableColumn
cbUptime = _CbUptime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 25),
    _CbUptime_Type()
)
cbUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbUptime.setStatus("current")
_CbDiskAllocation_Type = OctetString
_CbDiskAllocation_Object = MibTableColumn
cbDiskAllocation = _CbDiskAllocation_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 30),
    _CbDiskAllocation_Type()
)
cbDiskAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbDiskAllocation.setStatus("current")
_CbAPAIPADDRESSType_Type = InetAddressType
_CbAPAIPADDRESSType_Object = MibTableColumn
cbAPAIPADDRESSType = _CbAPAIPADDRESSType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 47),
    _CbAPAIPADDRESSType_Type()
)
cbAPAIPADDRESSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPAIPADDRESSType.setStatus("current")
_CbAPAIPADDRESS_Type = InetAddress
_CbAPAIPADDRESS_Object = MibTableColumn
cbAPAIPADDRESS = _CbAPAIPADDRESS_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 48),
    _CbAPAIPADDRESS_Type()
)
cbAPAIPADDRESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPAIPADDRESS.setStatus("current")
_CbAPANetMaskType_Type = InetAddressType
_CbAPANetMaskType_Object = MibTableColumn
cbAPANetMaskType = _CbAPANetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 49),
    _CbAPANetMaskType_Type()
)
cbAPANetMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPANetMaskType.setStatus("current")
_CbAPANetMask_Type = InetAddress
_CbAPANetMask_Object = MibTableColumn
cbAPANetMask = _CbAPANetMask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 50),
    _CbAPANetMask_Type()
)
cbAPANetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPANetMask.setStatus("current")
_CbAPAGatewayType_Type = InetAddressType
_CbAPAGatewayType_Object = MibTableColumn
cbAPAGatewayType = _CbAPAGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 51),
    _CbAPAGatewayType_Type()
)
cbAPAGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPAGatewayType.setStatus("current")
_CbAPAGateway_Type = InetAddress
_CbAPAGateway_Object = MibTableColumn
cbAPAGateway = _CbAPAGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 52),
    _CbAPAGateway_Type()
)
cbAPAGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAPAGateway.setStatus("current")
_CbPluginIPADDRESSType_Type = InetAddressType
_CbPluginIPADDRESSType_Object = MibTableColumn
cbPluginIPADDRESSType = _CbPluginIPADDRESSType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 53),
    _CbPluginIPADDRESSType_Type()
)
cbPluginIPADDRESSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbPluginIPADDRESSType.setStatus("current")
_CbPluginIPADDRESS_Type = InetAddress
_CbPluginIPADDRESS_Object = MibTableColumn
cbPluginIPADDRESS = _CbPluginIPADDRESS_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 54),
    _CbPluginIPADDRESS_Type()
)
cbPluginIPADDRESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbPluginIPADDRESS.setStatus("current")
_CbMgmtIPAddressType_Type = InetAddressType
_CbMgmtIPAddressType_Object = MibTableColumn
cbMgmtIPAddressType = _CbMgmtIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 57),
    _CbMgmtIPAddressType_Type()
)
cbMgmtIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbMgmtIPAddressType.setStatus("current")
_CbMgmtIPAddress_Type = InetAddress
_CbMgmtIPAddress_Object = MibTableColumn
cbMgmtIPAddress = _CbMgmtIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 3, 1, 58),
    _CbMgmtIPAddress_Type()
)
cbMgmtIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbMgmtIPAddress.setStatus("current")
_CloudBridgeAcceleratorTable_Object = MibTable
cloudBridgeAcceleratorTable = _CloudBridgeAcceleratorTable_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4)
)
if mibBuilder.loadTexts:
    cloudBridgeAcceleratorTable.setStatus("current")
_CloudBridgeAcceleratorEntry_Object = MibTableRow
cloudBridgeAcceleratorEntry = _CloudBridgeAcceleratorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1)
)
cloudBridgeAcceleratorEntry.setIndexNames(
    (0, "MIB", "cbAcceleratorIpAddressType"),
    (0, "MIB", "cbAcceleratorIpAddress"),
    (0, "MIB", "cbAcceleratorHostIPAddressType"),
    (0, "MIB", "cbAcceleratorHostIPAddress"),
)
if mibBuilder.loadTexts:
    cloudBridgeAcceleratorEntry.setStatus("current")
_CbAcceleratorIpAddressType_Type = InetAddressType
_CbAcceleratorIpAddressType_Object = MibTableColumn
cbAcceleratorIpAddressType = _CbAcceleratorIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 1),
    _CbAcceleratorIpAddressType_Type()
)
cbAcceleratorIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorIpAddressType.setStatus("current")
_CbAcceleratorIpAddress_Type = InetAddress
_CbAcceleratorIpAddress_Object = MibTableColumn
cbAcceleratorIpAddress = _CbAcceleratorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 2),
    _CbAcceleratorIpAddress_Type()
)
cbAcceleratorIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorIpAddress.setStatus("current")
_CbAcceleratorHostIPAddressType_Type = InetAddressType
_CbAcceleratorHostIPAddressType_Object = MibTableColumn
cbAcceleratorHostIPAddressType = _CbAcceleratorHostIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 3),
    _CbAcceleratorHostIPAddressType_Type()
)
cbAcceleratorHostIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorHostIPAddressType.setStatus("current")
_CbAcceleratorHostIPAddress_Type = InetAddress
_CbAcceleratorHostIPAddress_Object = MibTableColumn
cbAcceleratorHostIPAddress = _CbAcceleratorHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 4),
    _CbAcceleratorHostIPAddress_Type()
)
cbAcceleratorHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorHostIPAddress.setStatus("current")
_CbAcceleratorProfileName_Type = OctetString
_CbAcceleratorProfileName_Object = MibTableColumn
cbAcceleratorProfileName = _CbAcceleratorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 5),
    _CbAcceleratorProfileName_Type()
)
cbAcceleratorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorProfileName.setStatus("current")
_CbAcceleratorName_Type = OctetString
_CbAcceleratorName_Object = MibTableColumn
cbAcceleratorName = _CbAcceleratorName_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 6),
    _CbAcceleratorName_Type()
)
cbAcceleratorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorName.setStatus("current")
_CbAcceleratorNetmaskType_Type = InetAddressType
_CbAcceleratorNetmaskType_Object = MibTableColumn
cbAcceleratorNetmaskType = _CbAcceleratorNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 7),
    _CbAcceleratorNetmaskType_Type()
)
cbAcceleratorNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorNetmaskType.setStatus("current")
_CbAcceleratorNetmask_Type = InetAddress
_CbAcceleratorNetmask_Object = MibTableColumn
cbAcceleratorNetmask = _CbAcceleratorNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 8),
    _CbAcceleratorNetmask_Type()
)
cbAcceleratorNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorNetmask.setStatus("current")
_CbAcceleratorGatewayType_Type = InetAddressType
_CbAcceleratorGatewayType_Object = MibTableColumn
cbAcceleratorGatewayType = _CbAcceleratorGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 9),
    _CbAcceleratorGatewayType_Type()
)
cbAcceleratorGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorGatewayType.setStatus("current")
_CbAcceleratorGateway_Type = InetAddress
_CbAcceleratorGateway_Object = MibTableColumn
cbAcceleratorGateway = _CbAcceleratorGateway_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 10),
    _CbAcceleratorGateway_Type()
)
cbAcceleratorGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorGateway.setStatus("current")
_CbAcceleratorHostname_Type = OctetString
_CbAcceleratorHostname_Object = MibTableColumn
cbAcceleratorHostname = _CbAcceleratorHostname_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 11),
    _CbAcceleratorHostname_Type()
)
cbAcceleratorHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorHostname.setStatus("current")
_CbAcceleratorDescription_Type = OctetString
_CbAcceleratorDescription_Object = MibTableColumn
cbAcceleratorDescription = _CbAcceleratorDescription_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 12),
    _CbAcceleratorDescription_Type()
)
cbAcceleratorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorDescription.setStatus("current")
_CbAcceleratorVersion_Type = OctetString
_CbAcceleratorVersion_Object = MibTableColumn
cbAcceleratorVersion = _CbAcceleratorVersion_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 13),
    _CbAcceleratorVersion_Type()
)
cbAcceleratorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVersion.setStatus("current")
_CbAcceleratorInstanceState_Type = OctetString
_CbAcceleratorInstanceState_Object = MibTableColumn
cbAcceleratorInstanceState = _CbAcceleratorInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 14),
    _CbAcceleratorInstanceState_Type()
)
cbAcceleratorInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorInstanceState.setStatus("current")
_CbAcceleratorUuid_Type = OctetString
_CbAcceleratorUuid_Object = MibTableColumn
cbAcceleratorUuid = _CbAcceleratorUuid_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 15),
    _CbAcceleratorUuid_Type()
)
cbAcceleratorUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorUuid.setStatus("current")
_CbAcceleratorVmState_Type = OctetString
_CbAcceleratorVmState_Object = MibTableColumn
cbAcceleratorVmState = _CbAcceleratorVmState_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 16),
    _CbAcceleratorVmState_Type()
)
cbAcceleratorVmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmState.setStatus("current")
_CbAcceleratorNumberOfCPU_Type = Integer32
_CbAcceleratorNumberOfCPU_Object = MibTableColumn
cbAcceleratorNumberOfCPU = _CbAcceleratorNumberOfCPU_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 17),
    _CbAcceleratorNumberOfCPU_Type()
)
cbAcceleratorNumberOfCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorNumberOfCPU.setStatus("current")
_CbAcceleratorVmCPUUsage_Type = OctetString
_CbAcceleratorVmCPUUsage_Object = MibTableColumn
cbAcceleratorVmCPUUsage = _CbAcceleratorVmCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 18),
    _CbAcceleratorVmCPUUsage_Type()
)
cbAcceleratorVmCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmCPUUsage.setStatus("current")
_CbAcceleratorVmMemoryTotal_Type = OctetString
_CbAcceleratorVmMemoryTotal_Object = MibTableColumn
cbAcceleratorVmMemoryTotal = _CbAcceleratorVmMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 19),
    _CbAcceleratorVmMemoryTotal_Type()
)
cbAcceleratorVmMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmMemoryTotal.setStatus("current")
_CbAcceleratorVmMemoryFree_Type = OctetString
_CbAcceleratorVmMemoryFree_Object = MibTableColumn
cbAcceleratorVmMemoryFree = _CbAcceleratorVmMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 20),
    _CbAcceleratorVmMemoryFree_Type()
)
cbAcceleratorVmMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmMemoryFree.setStatus("current")
_CbAcceleratorVmMemoryUsage_Type = OctetString
_CbAcceleratorVmMemoryUsage_Object = MibTableColumn
cbAcceleratorVmMemoryUsage = _CbAcceleratorVmMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 21),
    _CbAcceleratorVmMemoryUsage_Type()
)
cbAcceleratorVmMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorVmMemoryUsage.setStatus("current")
_CbAcceleratorUptime_Type = OctetString
_CbAcceleratorUptime_Object = MibTableColumn
cbAcceleratorUptime = _CbAcceleratorUptime_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 24),
    _CbAcceleratorUptime_Type()
)
cbAcceleratorUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorUptime.setStatus("current")
_CbAcceleratorIpList_Type = OctetString
_CbAcceleratorIpList_Object = MibTableColumn
cbAcceleratorIpList = _CbAcceleratorIpList_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 31),
    _CbAcceleratorIpList_Type()
)
cbAcceleratorIpList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorIpList.setStatus("current")
_CbAcceleratorMgmtIPAddressType_Type = InetAddressType
_CbAcceleratorMgmtIPAddressType_Object = MibTableColumn
cbAcceleratorMgmtIPAddressType = _CbAcceleratorMgmtIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 38),
    _CbAcceleratorMgmtIPAddressType_Type()
)
cbAcceleratorMgmtIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorMgmtIPAddressType.setStatus("current")
_CbAcceleratorMgmtIPAddress_Type = InetAddress
_CbAcceleratorMgmtIPAddress_Object = MibTableColumn
cbAcceleratorMgmtIPAddress = _CbAcceleratorMgmtIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5951, 6, 3, 4, 1, 39),
    _CbAcceleratorMgmtIPAddress_Type()
)
cbAcceleratorMgmtIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAcceleratorMgmtIPAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB",
    **{"netScaler": netScaler,
       "sdxRoot": sdxRoot,
       "sdxEventGroup": sdxEventGroup,
       "systemGroup": systemGroup,
       "systemPlatform": systemPlatform,
       "systemProduct": systemProduct,
       "systemBuildNumber": systemBuildNumber,
       "systemSvmIPAddressType": systemSvmIPAddressType,
       "systemSvmIPAddress": systemSvmIPAddress,
       "systemXenIPAddressType": systemXenIPAddressType,
       "systemXenIPAddress": systemXenIPAddress,
       "systemNetmaskType": systemNetmaskType,
       "systemNetmask": systemNetmask,
       "systemGatewayType": systemGatewayType,
       "systemGateway": systemGateway,
       "systemNetworkInterface": systemNetworkInterface,
       "systemDns": systemDns,
       "systemSysId": systemSysId,
       "systemSerial": systemSerial,
       "systemCurrentTime": systemCurrentTime,
       "systemUptime": systemUptime,
       "systemBiosVersion": systemBiosVersion,
       "systemMaxThroughput": systemMaxThroughput,
       "systemAvailableThroughput": systemAvailableThroughput,
       "systemHostId": systemHostId,
       "systemCustomID": systemCustomID,
       "sysHealthGroup": sysHealthGroup,
       "hardwareResourceTable": hardwareResourceTable,
       "hardwareResourceEntry": hardwareResourceEntry,
       "hardwareResourceName": hardwareResourceName,
       "hardwareResourceHostIPAddressType": hardwareResourceHostIPAddressType,
       "hardwareResourceHostIPAddress": hardwareResourceHostIPAddress,
       "hardwareResourceCurrentValue": hardwareResourceCurrentValue,
       "hardwareResourceExpectedValue": hardwareResourceExpectedValue,
       "hardwareResourceUnit": hardwareResourceUnit,
       "hardwareResourceStatus": hardwareResourceStatus,
       "softwareResourceTable": softwareResourceTable,
       "softwareResourceEntry": softwareResourceEntry,
       "softwareResourceName": softwareResourceName,
       "softwareResourceHostIPAddressType": softwareResourceHostIPAddressType,
       "softwareResourceHostIPAddress": softwareResourceHostIPAddress,
       "softwareResourceCurrentValue": softwareResourceCurrentValue,
       "softwareResourceExpectedValue": softwareResourceExpectedValue,
       "softwareResourceUnit": softwareResourceUnit,
       "softwareResourceStatus": softwareResourceStatus,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskName": diskName,
       "diskHostIPAddressType": diskHostIPAddressType,
       "diskHostIPAddress": diskHostIPAddress,
       "diskTransactionRate": diskTransactionRate,
       "diskBlockReadRate": diskBlockReadRate,
       "diskBlockWriteRate": diskBlockWriteRate,
       "diskTotalBlocksRead": diskTotalBlocksRead,
       "diskTotalBlocksWritten": diskTotalBlocksWritten,
       "diskUtilized": diskUtilized,
       "diskSize": diskSize,
       "diskBayNumber": diskBayNumber,
       "srTable": srTable,
       "srEntry": srEntry,
       "srName": srName,
       "srBayNumber": srBayNumber,
       "srHostIPAddressType": srHostIPAddressType,
       "srHostIPAddress": srHostIPAddress,
       "srUtilized": srUtilized,
       "srSize": srSize,
       "srStatus": srStatus,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfacePort": interfacePort,
       "interfaceHostIPAddressType": interfaceHostIPAddressType,
       "interfaceHostIPAddress": interfaceHostIPAddress,
       "interfaceState": interfaceState,
       "interfaceRxPackets": interfaceRxPackets,
       "interfaceTxPackets": interfaceTxPackets,
       "interfaceRxBytes": interfaceRxBytes,
       "interfaceTxBytes": interfaceTxBytes,
       "interfaceRxErrors": interfaceRxErrors,
       "interfaceTxErrors": interfaceTxErrors,
       "interfaceVfTotal": interfaceVfTotal,
       "interfaceVfAssigned": interfaceVfAssigned,
       "interfaceMappedPort": interfaceMappedPort,
       "deviceGroup": deviceGroup,
       "xenTable": xenTable,
       "xenEntry": xenEntry,
       "xenIpAddressType": xenIpAddressType,
       "xenIpAddress": xenIpAddress,
       "xenHostname": xenHostname,
       "xenDescription": xenDescription,
       "xenVersion": xenVersion,
       "xenUuid": xenUuid,
       "xenNumberOfCPU": xenNumberOfCPU,
       "xenCpuUsage": xenCpuUsage,
       "xenMemoryTotal": xenMemoryTotal,
       "xenMemoryFree": xenMemoryFree,
       "xenMemoryUsage": xenMemoryUsage,
       "xenTx": xenTx,
       "xenRx": xenRx,
       "xenUptime": xenUptime,
       "xenSslCoresTotal": xenSslCoresTotal,
       "xenIscsiIQN": xenIscsiIQN,
       "xenEdition": xenEdition,
       "xenExpiry": xenExpiry,
       "xenProductCode": xenProductCode,
       "xenSerialNumber": xenSerialNumber,
       "xenVersionLong": xenVersionLong,
       "xenVersionShort": xenVersionShort,
       "xenBuildNumber": xenBuildNumber,
       "xenBuildDate": xenBuildDate,
       "netscalerTable": netscalerTable,
       "netscalerEntry": netscalerEntry,
       "nsIpAddressType": nsIpAddressType,
       "nsIpAddress": nsIpAddress,
       "nsHostIPAddressType": nsHostIPAddressType,
       "nsHostIPAddress": nsHostIPAddress,
       "nsProfileName": nsProfileName,
       "nsName": nsName,
       "nsNetmaskType": nsNetmaskType,
       "nsNetmask": nsNetmask,
       "nsGatewayType": nsGatewayType,
       "nsGateway": nsGateway,
       "nsHostname": nsHostname,
       "nsDescription": nsDescription,
       "nsVersion": nsVersion,
       "nsUuid": nsUuid,
       "nsInstanceState": nsInstanceState,
       "nsVirtualFunctions": nsVirtualFunctions,
       "nsSslVirtualFunctions": nsSslVirtualFunctions,
       "nsVmState": nsVmState,
       "nsNumberOfCPU": nsNumberOfCPU,
       "nsVmMemoryTotal": nsVmMemoryTotal,
       "nsUptime": nsUptime,
       "nsNumberOfSSLCores": nsNumberOfSSLCores,
       "nsCpuCoreMgmt": nsCpuCoreMgmt,
       "nsCpuCorePE": nsCpuCorePE,
       "nsVmDescription": nsVmDescription,
       "nsThroughput": nsThroughput,
       "nsNumberOfCores": nsNumberOfCores,
       "nsNsCPUUsage": nsNsCPUUsage,
       "nsNsMemoryUsage": nsNsMemoryUsage,
       "nsNsTx": nsNsTx,
       "nsNsRx": nsNsRx,
       "nsHttpReq": nsHttpReq,
       "nsUpsince": nsUpsince,
       "nsLicense": nsLicense,
       "nsHaMasterState": nsHaMasterState,
       "nsHaIPAddressType": nsHaIPAddressType,
       "nsHaIPAddress": nsHaIPAddress,
       "nsNodeState": nsNodeState,
       "nsHaSync": nsHaSync,
       "nsPps": nsPps,
       "nsNumberOfSslCoresUp": nsNumberOfSslCoresUp,
       "nsIfOby1": nsIfOby1,
       "nsIf0by2": nsIf0by2,
       "nsNsVLANId": nsNsVLANId,
       "nsNsVLANTagged": nsNsVLANTagged,
       "nsVlanType": nsVlanType,
       "cloudBridgeInstanceTable": cloudBridgeInstanceTable,
       "cloudBridgeInstanceEntry": cloudBridgeInstanceEntry,
       "cbIpAddressType": cbIpAddressType,
       "cbIpAddress": cbIpAddress,
       "cbHostIPAddressType": cbHostIPAddressType,
       "cbHostIPAddress": cbHostIPAddress,
       "cbProfileName": cbProfileName,
       "cbName": cbName,
       "cbNetmaskType": cbNetmaskType,
       "cbNetmask": cbNetmask,
       "cbGatewayType": cbGatewayType,
       "cbGateway": cbGateway,
       "cbHostname": cbHostname,
       "cbDescription": cbDescription,
       "cbVersion": cbVersion,
       "cbInstanceState": cbInstanceState,
       "cbUuid": cbUuid,
       "cbVirtualFunctions": cbVirtualFunctions,
       "cbVmState": cbVmState,
       "cbNumberOfCPU": cbNumberOfCPU,
       "cbVmCPUUsage": cbVmCPUUsage,
       "cbVmMemoryTotal": cbVmMemoryTotal,
       "cbVmMemoryFree": cbVmMemoryFree,
       "cbVmMemoryUsage": cbVmMemoryUsage,
       "cbUptime": cbUptime,
       "cbDiskAllocation": cbDiskAllocation,
       "cbAPAIPADDRESSType": cbAPAIPADDRESSType,
       "cbAPAIPADDRESS": cbAPAIPADDRESS,
       "cbAPANetMaskType": cbAPANetMaskType,
       "cbAPANetMask": cbAPANetMask,
       "cbAPAGatewayType": cbAPAGatewayType,
       "cbAPAGateway": cbAPAGateway,
       "cbPluginIPADDRESSType": cbPluginIPADDRESSType,
       "cbPluginIPADDRESS": cbPluginIPADDRESS,
       "cbMgmtIPAddressType": cbMgmtIPAddressType,
       "cbMgmtIPAddress": cbMgmtIPAddress,
       "cloudBridgeAcceleratorTable": cloudBridgeAcceleratorTable,
       "cloudBridgeAcceleratorEntry": cloudBridgeAcceleratorEntry,
       "cbAcceleratorIpAddressType": cbAcceleratorIpAddressType,
       "cbAcceleratorIpAddress": cbAcceleratorIpAddress,
       "cbAcceleratorHostIPAddressType": cbAcceleratorHostIPAddressType,
       "cbAcceleratorHostIPAddress": cbAcceleratorHostIPAddress,
       "cbAcceleratorProfileName": cbAcceleratorProfileName,
       "cbAcceleratorName": cbAcceleratorName,
       "cbAcceleratorNetmaskType": cbAcceleratorNetmaskType,
       "cbAcceleratorNetmask": cbAcceleratorNetmask,
       "cbAcceleratorGatewayType": cbAcceleratorGatewayType,
       "cbAcceleratorGateway": cbAcceleratorGateway,
       "cbAcceleratorHostname": cbAcceleratorHostname,
       "cbAcceleratorDescription": cbAcceleratorDescription,
       "cbAcceleratorVersion": cbAcceleratorVersion,
       "cbAcceleratorInstanceState": cbAcceleratorInstanceState,
       "cbAcceleratorUuid": cbAcceleratorUuid,
       "cbAcceleratorVmState": cbAcceleratorVmState,
       "cbAcceleratorNumberOfCPU": cbAcceleratorNumberOfCPU,
       "cbAcceleratorVmCPUUsage": cbAcceleratorVmCPUUsage,
       "cbAcceleratorVmMemoryTotal": cbAcceleratorVmMemoryTotal,
       "cbAcceleratorVmMemoryFree": cbAcceleratorVmMemoryFree,
       "cbAcceleratorVmMemoryUsage": cbAcceleratorVmMemoryUsage,
       "cbAcceleratorUptime": cbAcceleratorUptime,
       "cbAcceleratorIpList": cbAcceleratorIpList,
       "cbAcceleratorMgmtIPAddressType": cbAcceleratorMgmtIPAddressType,
       "cbAcceleratorMgmtIPAddress": cbAcceleratorMgmtIPAddress}
)
